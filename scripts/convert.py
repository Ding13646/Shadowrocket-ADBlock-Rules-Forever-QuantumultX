#!/usr/bin/env python3
"""Convert the upstream Shadowrocket release configurations to QuanX syntax.

Active directives are either mapped, reported with an explicit behavior caveat,
or rejected. Unknown active syntax is never silently discarded.
"""
from __future__ import annotations

import argparse
import ipaddress
import json
import re
import sys
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

UPSTREAM_API = "https://api.github.com/repos/Johnshall/Shadowrocket-ADBlock-Rules-Forever/contents?ref=release"
UPSTREAM_REPO = "https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever"

RULE_TYPES = {
    "DOMAIN": "host",
    "DOMAIN-SUFFIX": "host-suffix",
    "DOMAIN-KEYWORD": "host-keyword",
    "DOMAIN-WILDCARD": "host-wildcard",
    "USER-AGENT": "user-agent",
    "GEOIP": "geoip",
    "IP-ASN": "ip-asn",
    "DST-PORT": "port",
}
POLICY_MAP = {
    "proxy": "proxy", "direct": "direct", "reject": "reject",
    "reject-drop": "reject", "reject-tinygif": "reject",
}

@dataclass
class Issue:
    source: str
    line: int
    severity: str
    status: str
    message: str
    text: str = ""

@dataclass
class Result:
    name: str
    output: str = ""
    issues: List[Issue] = field(default_factory=list)
    counts: Counter = field(default_factory=Counter)
    failed: bool = False


def strip_inline_comment(text: str) -> str:
    return re.split(r"\s+#", text, maxsplit=1)[0].strip()


def split_fields(text: str) -> List[str]:
    return [part.strip() for part in text.split(",")]


def normalize_policy(source: str, aliases: Optional[Dict[str, str]] = None) -> str:
    key = source.strip().lower()
    if key in POLICY_MAP:
        return POLICY_MAP[key]
    if aliases:
        for alias, target in aliases.items():
            if alias.lower() == key:
                return target
    return source.strip()


def checked_policy(source: str, aliases: Optional[Dict[str, str]], issues: List[Issue],
                   file_name: str, line_no: int) -> str:
    key = source.strip().lower()
    known_aliases = {alias.lower() for alias in aliases} if aliases is not None else set()
    if aliases is not None and key not in POLICY_MAP and key not in known_aliases:
        issues.append(Issue(file_name, line_no, "error", "unsupported", f"Unresolved policy/group reference: {source}", source))
        return normalize_policy(source, aliases)
    return normalize_policy(source, aliases)


def map_ip_rule(kind: str, value: str) -> Tuple[str, str, Optional[str]]:
    try:
        network = ipaddress.ip_network(value, strict=False)
    except ValueError:
        return "", value, f"Invalid IP network: {value}"
    if kind == "IP-CIDR6" and network.version != 6:
        return "", value, "IP-CIDR6 source contains an IPv4 network"
    if kind == "IP-CIDR" and network.version == 6:
        return "ip6-cidr", str(network), None
    return ("ip-cidr" if network.version == 4 else "ip6-cidr"), str(network), None


def parse_groups(entries: Sequence[Tuple[int, str]], source: str, issues: List[Issue], counts: Counter) -> Tuple[List[str], Dict[str, str]]:
    aliases: Dict[str, str] = {"proxy": "proxy", "direct": "direct", "reject": "reject"}
    definitions: List[Tuple[str, str, int]] = []
    for line_no, original in entries:
        clean = strip_inline_comment(original.strip())
        if not clean or clean.startswith(("#", ";", "//")):
            continue
        if "=" not in clean:
            issues.append(Issue(source, line_no, "error", "unsupported", "Malformed [Proxy Group] entry", clean))
            continue
        name, value = (part.strip() for part in clean.split("=", 1))
        definitions.append((name, value, line_no))
        aliases[name.lower()] = name

    output: List[str] = []
    for name, value, line_no in definitions:
        fields = split_fields(value)
        kind = fields[0].lower()
        if kind == "select":
            candidates = []
            for item in fields[1:]:
                if "=" not in item:
                    candidate = item.strip()
                    candidates.append(aliases.get(candidate.lower(), normalize_policy(candidate, aliases)))
            if not candidates:
                issues.append(Issue(source, line_no, "error", "unsupported", f"Policy group {name} has no candidates", value))
                continue
            output.append(f"static = {name}, " + ", ".join(candidates))
            counts["changed"] += 1
            issues.append(Issue(source, line_no, "warning", "changed", "Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ", value))
        elif kind == "url-test":
            options = {}
            for item in fields[1:]:
                if "=" in item:
                    key, val = item.split("=", 1)
                    options[key.strip().lower()] = val.strip()
            pattern = options.get("policy-regex-filter")
            if not pattern:
                issues.append(Issue(source, line_no, "error", "unsupported", f"url-test group {name} has no policy-regex-filter", value))
                continue
            output.append(f"static = {name}, server-tag-regex={pattern}")
            counts["changed"] += 1
            issues.append(Issue(source, line_no, "warning", "changed", "Shadowrocket url-test mapped to a QuanX static group filtered by server tags; automatic latency selection, test interval, tolerance, timeout, and selected node are not preserved", value))
        else:
            issues.append(Issue(source, line_no, "error", "unsupported", f"Unsupported proxy group type: {kind}", value))
    return output, aliases


def transform_rule(text: str, source: str, line_no: int, issues: List[Issue], counts: Counter,
                   policy_aliases: Optional[Dict[str, str]] = None) -> Optional[str]:
    raw = strip_inline_comment(text)
    if not raw:
        return None
    fields = split_fields(raw)
    kind = fields[0].upper()
    if kind == "FINAL":
        if len(fields) != 2:
            issues.append(Issue(source, line_no, "error", "unsupported", "Malformed FINAL rule", text))
            return None
        counts["exact"] += 1
        return f"final, {checked_policy(fields[1], policy_aliases, issues, source, line_no)}"
    if kind == "RULE-SET":
        if len(fields) != 3:
            issues.append(Issue(source, line_no, "error", "unsupported", "Malformed RULE-SET rule", text))
            return None
        url, policy = fields[1], checked_policy(fields[2], policy_aliases, issues, source, line_no)
        status = "exact" if "QuantumultX/" in url else "changed"
        if "/Shadowrocket/" in url:
            url = url.replace("/Shadowrocket/", "/QuantumultX/")
        if status == "changed":
            counts["changed"] += 1
            issues.append(Issue(source, line_no, "warning", "changed", "Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability", text))
        else:
            counts["exact"] += 1
        tag = re.sub(r"[^A-Za-z0-9_-]", "-", Path(url).stem)
        return f"# Remote resource source: {fields[1]}\n{url}, tag={tag}, force-policy={policy}, enabled=true"
    if kind in ("IP-CIDR", "IP-CIDR6"):
        if len(fields) not in (3, 4):
            issues.append(Issue(source, line_no, "error", "unsupported", "Malformed IP-CIDR rule", text))
            return None
        matcher, network, err = map_ip_rule(kind, fields[1])
        if err:
            issues.append(Issue(source, line_no, "error", "unsupported", err, text))
            return None
        policy = checked_policy(fields[2], policy_aliases, issues, source, line_no)
        suffix = ""
        if len(fields) == 4:
            if fields[3].lower() != "no-resolve":
                issues.append(Issue(source, line_no, "error", "unsupported", f"Unknown IP-CIDR option: {fields[3]}", text))
                return None
            suffix = ", no-resolve"
            counts["changed"] += 1
            issues.append(Issue(source, line_no, "warning", "changed", "Preserved no-resolve option; confirm behavior in the QuanX client", text))
        counts["exact"] += 1
        return f"{matcher}, {network}, {policy}{suffix}"
    if kind in RULE_TYPES:
        if len(fields) != 3:
            issues.append(Issue(source, line_no, "error", "unsupported", f"Malformed {kind} rule", text))
            return None
        counts["exact"] += 1
        return f"{RULE_TYPES[kind]}, {fields[1]}, {checked_policy(fields[2], policy_aliases, issues, source, line_no)}"
    issues.append(Issue(source, line_no, "error", "unsupported", f"Unsupported rule type: {kind}", text))
    return None


def parse_sections(name: str, lines: Sequence[str]) -> Dict[str, List[Tuple[int, str]]]:
    sections: Dict[str, List[Tuple[int, str]]] = {}
    section = ""
    for line_no, original in enumerate(lines, 1):
        raw = original.strip()
        if raw.startswith("[") and raw.endswith("]"):
            section = raw.lower()
            sections.setdefault(section, [])
        else:
            sections.setdefault(section, []).append((line_no, original.rstrip("\r\n")))
    return sections


def convert_filter_only(name: str, lines: Sequence[str]) -> Result:
    result = Result(name)
    out = [f"# Converted from {UPSTREAM_REPO}/blob/release/{name}",
           "# Derived work under CC BY-SA 4.0. See README for attribution and differences."]
    for original in lines:
        text = original.strip()
        if text.startswith(("#", ";", "//")):
            out.append(text)
    for line_no, original in enumerate(lines, 1):
        text = original.strip()
        if not text or text.startswith(("#", ";", "//")) or (text.startswith("[") and text.endswith("]")):
            continue
        converted = transform_rule(text, name, line_no, result.issues, result.counts)
        if converted:
            out.append(converted)
    result.failed = any(issue.severity == "error" for issue in result.issues)
    result.output = "\n".join(out) + "\n"
    return result


def parse_shadowrocket(name: str, lines: Sequence[str]) -> Result:
    result = Result(name)
    sections = parse_sections(name, lines)
    if "[rule]" not in sections:
        result.issues.append(Issue(name, 1, "error", "unsupported", "Missing [Rule] section"))
        result.failed = True
        return result

    group_lines, aliases = parse_groups(sections.get("[proxy group]", []), name, result.issues, result.counts)
    rule_out: List[str] = []
    source_lines = sections["[rule]"]
    for line_no, original in source_lines:
        text = strip_inline_comment(original.strip())
        if not text or text.startswith(("#", ";", "//")):
            continue
        converted = transform_rule(text, name, line_no, result.issues, result.counts, aliases)
        if converted:
            rule_out.append(converted)

    local_rules = [line for line in rule_out if "tag=" not in line and not line.startswith("# Remote resource")]
    remote_rows = [line for line in rule_out if "tag=" in line or line.startswith("# Remote resource")]
    out = [f"# Converted from {UPSTREAM_REPO}/blob/release/{name}",
           "# Derived work under CC BY-SA 4.0. Review reports and comments for behavior differences."]
    if local_rules:
        out += ["", "[filter_local]", *local_rules]
    if remote_rows:
        out += ["", "[filter_remote]", *remote_rows]

    general_lines: List[str] = []
    dns_lines: List[str] = []
    skip_rules: List[str] = []
    general_known = {
        "ipv6", "bypass-system", "skip-proxy", "bypass-tun", "dns-server",
        "fallback-dns-server", "prefer-ipv6", "dns-direct-system", "icmp-auto-reply",
        "always-reject-url-rewrite", "private-ip-answer", "dns-direct-fallback-proxy",
        "hijack-dns", "udp-policy-not-supported-behaviour", "stun-response-ip",
        "stun-response-ipv6", "block-quic", "dns-server-policy", "allow-wifi-access",
        "tun-excluded-routes",
    }
    for line_no, line in sections.get("[general]", []):
        clean = strip_inline_comment(line.strip())
        if not clean or clean.startswith(("#", ";", "//")):
            continue
        if "=" not in clean:
            result.issues.append(Issue(name, line_no, "error", "unsupported", "Malformed [General] setting", clean))
            continue
        key, value = (part.strip() for part in clean.split("=", 1))
        key_lower = key.lower()
        if key_lower not in general_known:
            result.issues.append(Issue(name, line_no, "error", "unsupported", f"Unknown active [General] setting: {key}", clean))
            continue
        if key_lower == "dns-server":
            doh_servers = []
            plain_servers = []
            for server in [item.strip() for item in value.split(",") if item.strip()]:
                if server.startswith("https://"):
                    doh_servers.append(server)
                elif server.startswith("http://"):
                    result.issues.append(Issue(name, line_no, "error", "unsupported", "Plain HTTP DNS URI cannot be mapped to a QuanX server directive", server))
                else:
                    plain_servers.append(server)
            if doh_servers:
                dns_lines.append("doh-server = " + ", ".join(doh_servers))
            for server in plain_servers:
                dns_lines.append(f"server = {server}")
            result.counts["changed"] += 1
            result.issues.append(Issue(name, line_no, "warning", "changed", "DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ", value))
        elif key_lower == "ipv6":
            if value.lower() in ("false", "no", "0"):
                dns_lines.append("no-ipv6")
                result.counts["changed"] += 1
                result.issues.append(Issue(name, line_no, "warning", "changed", "IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ", clean))
            else:
                result.counts["exact"] += 1
        elif key_lower in ("bypass-tun", "tun-excluded-routes"):
            general_lines.append(f"excluded_routes = {value}")
            result.counts["changed"] += 1
            result.issues.append(Issue(name, line_no, "warning", "changed", f"{key} mapped to QuanX excluded_routes; validate equivalent tunnel scope", clean))
        elif key_lower == "skip-proxy":
            for item in [part.strip() for part in value.split(",") if part.strip()]:
                if "/" in item:
                    matcher, network, error = map_ip_rule("IP-CIDR", item)
                    if error:
                        result.issues.append(Issue(name, line_no, "error", "unsupported", error, item))
                    else:
                        skip_rules.append(f"{matcher}, {network}, direct")
                else:
                    wildcard = item.startswith("*.")
                    host = item[2:] if wildcard else item
                    skip_rules.append(f"{'host-suffix' if wildcard else 'host'}, {host}, direct")
            result.counts["changed"] += 1
            result.issues.append(Issue(name, line_no, "warning", "changed", "skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical", value))
        else:
            result.issues.append(Issue(name, line_no, "warning", "unsupported", f"Shadowrocket setting not represented in QuanX output: {key}={value}", clean))
    if general_lines:
        out += ["", "[general]", *general_lines]
    if skip_rules:
        if "[filter_local]" not in out:
            out += ["", "[filter_local]"]
        out[ out.index("[filter_local]") + 1 : out.index("[filter_local]") + 1 ] = skip_rules
    if dns_lines:
        out += ["", "[dns]", *dns_lines]

    if group_lines:
        out += ["", "[policy]", *group_lines]

    host_lines: List[str] = []
    for line_no, line in sections.get("[host]", []):
        clean = strip_inline_comment(line.strip())
        if not clean or clean.startswith(("#", ";", "//")):
            continue
        match = re.match(r"^(\S+)\s*=\s*(.+)$", clean)
        if not match:
            result.issues.append(Issue(name, line_no, "error", "unsupported", "Malformed [Host] mapping", clean))
            continue
        host, value = match.groups()
        wildcard = host.startswith("*.")
        host = host[2:] if wildcard else host
        if value.lower() == "server:system":
            host_lines.append(f"server = /{'*.' if wildcard else ''}{host}/system")
            result.counts["changed"] += 1
            result.issues.append(Issue(name, line_no, "warning", "changed", "Host system-resolution mapping converted to QuanX DNS policy; validate wildcard scope", clean))
        else:
            try:
                address = ipaddress.ip_address(value)
            except ValueError:
                result.issues.append(Issue(name, line_no, "error", "unsupported", f"Unsupported Host value: {value}", clean))
                continue
            if address.is_loopback:
                skip_rules.append(f"host, {host}, reject")
                result.counts["changed"] += 1
                result.issues.append(Issue(name, line_no, "warning", "changed", "Loopback host mapping translated to reject filter as recommended by QuanX sample; response semantics differ", clean))
            else:
                host_lines.append(f"address = /{'*.' if wildcard else ''}{host}/{address}")
                result.counts["changed"] += 1
                result.issues.append(Issue(name, line_no, "warning", "changed", "Host address mapping converted to QuanX [dns] address", clean))
    if host_lines:
        if "[dns]" not in out:
            out += ["", "[dns]"]
        out.extend(host_lines)
    # Host loopback directives can add rules after the first filter section.
    if skip_rules and "[filter_local]" in out:
        section_index = out.index("[filter_local]")
        # Insert only entries not already included above (localhost rule, if any).
        present = set(out[section_index + 1:])
        extra = [rule for rule in skip_rules if rule not in present]
        out[section_index + 1:section_index + 1] = extra

    rewrites: List[str] = []
    for line_no, line in sections.get("[url rewrite]", []):
        clean = strip_inline_comment(line.strip())
        if not clean or clean.startswith(("#", ";", "//")):
            continue
        match = re.match(r"^(\S+)\s+(\S+)\s+(30[127])\s*$", clean)
        if not match:
            result.issues.append(Issue(name, line_no, "error", "unsupported", "Unsupported URL Rewrite directive", clean))
            continue
        pattern, destination, status = match.groups()
        rewrites.append(f"{pattern} url {status} {destination}")
        result.counts["exact"] += 1
    if rewrites:
        out += ["", "[rewrite_local]", *rewrites]

    mitm: List[str] = []
    for line_no, line in sections.get("[mitm]", []):
        clean = strip_inline_comment(line.strip())
        if not clean or clean.startswith(("#", ";", "//")):
            continue
        match = re.match(r"^hostname\s*=\s*(.+)$", clean, re.I)
        if not match:
            result.issues.append(Issue(name, line_no, "error", "unsupported", "Unsupported [MITM] directive", clean))
            continue
        mitm.extend(item.strip() for item in match.group(1).split(",") if item.strip())
        result.counts["changed"] += 1
        result.issues.append(Issue(name, line_no, "warning", "changed", "Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately", clean))
    if mitm:
        out += ["", "[mitm]", "hostname = " + ", ".join(mitm)]

    handled = {"[general]", "[proxy]", "[proxy group]", "[rule]", "[host]", "[url rewrite]", "[mitm]"}
    for section, entries in sections.items():
        if section in handled or not section:
            continue
        for line_no, line in entries:
            clean = strip_inline_comment(line.strip())
            if clean and not clean.startswith(("#", ";", "//")):
                result.issues.append(Issue(name, line_no, "error", "unsupported", f"Unsupported section {section}", clean))
    for line_no, line in sections.get("[proxy]", []):
        clean = strip_inline_comment(line.strip())
        if clean and not clean.startswith(("#", ";", "//")):
            result.issues.append(Issue(name, line_no, "error", "unsupported", "Active Shadowrocket proxy definition requires secure manual migration", clean))

    result.failed = any(issue.severity == "error" for issue in result.issues)
    result.output = "\n".join(out) + "\n"
    return result


def fetch_source_files() -> List[Tuple[str, str]]:
    request = urllib.request.Request(UPSTREAM_API, headers={"User-Agent": "shadowrocket-quanx-converter"})
    with urllib.request.urlopen(request, timeout=45) as response:
        listing = json.load(response)
    return [(item["name"], item["download_url"]) for item in listing
            if item.get("type") == "file" and item["name"].endswith(".conf")]


def load_local_files(path: Path) -> List[Tuple[str, Path]]:
    return sorted((item.name, item) for item in path.rglob("*.conf") if item.is_file())


def render_report(results: Sequence[Result], download_errors: Sequence[Tuple[str, str]] = ()) -> str:
    failed = bool(download_errors) or any(result.failed for result in results)
    rows = ["# Conversion report", "", f"Generated from {UPSTREAM_REPO} `release`.", "",
            "Status: **" + ("FAILED — incomplete outputs were not published" if failed else "passed with documented caveats") + "**", "",
            "| Source | Exact mappings | Behavior changes | Blocking issues |", "|---|---:|---:|---:|"]
    for result in results:
        blockers = sum(issue.severity == "error" for issue in result.issues)
        rows.append(f"| `{result.name}` | {result.counts['exact']} | {result.counts['changed']} | {blockers} |")
    for result in results:
        if not result.issues:
            continue
        rows += ["", f"## `{result.name}`", ""]
        for issue in result.issues:
            line = f"- **{issue.severity.upper()} / {issue.status}**, line {issue.line}: {issue.message}"
            if issue.text:
                line += f" (`{issue.text[:180]}`)"
            rows.append(line)
    if download_errors:
        rows += ["", "## Download failures", ""]
        rows.extend(f"- `{name}`: {error}" for name, error in download_errors)
    return "\n".join(rows) + "\n"


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, help="Convert local *.conf files instead of fetching upstream")
    parser.add_argument("--output-dir", type=Path, default=Path("dist"))
    parser.add_argument("--report", type=Path, default=Path("reports/conversion-report.md"))
    args = parser.parse_args(argv)
    if args.input_dir:
        sources = [(name, "", path) for name, path in load_local_files(args.input_dir)]
    else:
        try:
            sources = [(name, url, None) for name, url in fetch_source_files()]
        except Exception as exc:
            print(f"Unable to list upstream files: {exc}", file=sys.stderr)
            return 2
    if not sources:
        print("No upstream .conf files found", file=sys.stderr)
        return 2
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    results: List[Result] = []
    download_errors: List[Tuple[str, str]] = []
    for name, url, local_path in sources:
        try:
            if local_path:
                content = local_path.read_text(encoding="utf-8-sig")
            else:
                request = urllib.request.Request(url, headers={"User-Agent": "shadowrocket-quanx-converter"})
                with urllib.request.urlopen(request, timeout=60) as response:
                    content = response.read().decode("utf-8-sig")
        except Exception as exc:
            download_errors.append((name, str(exc)))
            continue
        lines = content.splitlines()
        result = convert_filter_only(name, lines) if name == "sr_ad_only.conf" else parse_shadowrocket(name, lines)
        results.append(result)
        if not result.failed:
            output_name = name[:-5] + ".quanx.conf"
            (args.output_dir / output_name).write_text(result.output, encoding="utf-8")
        print(f"{name}: {'FAILED' if result.failed else 'ok'} ({result.counts['exact']} exact, {result.counts['changed']} changed, {len(result.issues)} notes)")
    args.report.write_text(render_report(results, download_errors), encoding="utf-8")
    return 1 if download_errors or any(result.failed for result in results) else 0

if __name__ == "__main__":
    raise SystemExit(main())
