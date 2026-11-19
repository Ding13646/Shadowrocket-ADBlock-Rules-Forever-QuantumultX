import importlib.util
import sys
import unittest
from collections import Counter
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "convert.py"
spec = importlib.util.spec_from_file_location("converter", SCRIPT)
converter = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = converter
spec.loader.exec_module(converter)


class ConverterTests(unittest.TestCase):
    def test_rule_aliases_and_policies(self):
        issues, counts = [], Counter()
        aliases = {"proxy": "proxy", "direct": "direct", "reject": "reject", "ai": "AI Group"}
        cases = {
            "DOMAIN,example.com,Proxy": "host, example.com, proxy",
            "DOMAIN-SUFFIX,example.com,Direct": "host-suffix, example.com, direct",
            "DOMAIN-KEYWORD,ads,Reject": "host-keyword, ads, reject",
            "GEOIP,CN,DIRECT": "geoip, CN, direct",
            "FINAL,Proxy": "final, proxy",
            "RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/YouTube/YouTube.list,AI": "# Remote resource source: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/YouTube/YouTube.list\nhttps://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/YouTube/YouTube.list, tag=YouTube, force-policy=AI Group, enabled=true",
        }
        for source, expected in cases.items():
            self.assertEqual(converter.transform_rule(source, "fixture.conf", 1, issues, counts, aliases), expected)
        self.assertEqual(issues[0].status, "changed")

    def test_ip_family_detection_and_network_normalization(self):
        self.assertEqual(converter.map_ip_rule("IP-CIDR", "2001:4860::1/64"), ("ip6-cidr", "2001:4860::/64", None))
        self.assertEqual(converter.map_ip_rule("IP-CIDR", "192.0.2.3/24"), ("ip-cidr", "192.0.2.0/24", None))
        self.assertIn("IPv4 network", converter.map_ip_rule("IP-CIDR6", "192.0.2.0/24")[2])
        self.assertIsNotNone(converter.map_ip_rule("IP-CIDR", "bad-network")[2])

    def test_group_mappings_and_unknown_group_are_reported(self):
        issues, counts = [], Counter()
        groups, aliases = converter.parse_groups([
            (1, "AI = select,PROXY,DIRECT,policy-select-name=PROXY"),
            (2, "香港 = url-test,url=https://example.com,interval=600,tolerance=5,policy-regex-filter=HK|香港"),
        ], "lazy_group.conf", issues, counts)
        self.assertEqual(aliases["ai"], "AI")
        self.assertIn("static = AI, proxy, direct", groups[0])
        self.assertIn("static = 香港, server-tag-regex=HK|香港", groups[1])
        self.assertEqual(len(issues), 2)

    def test_unknown_active_rule_blocks_conversion(self):
        result = converter.parse_shadowrocket("test.conf", ["[Rule]", "AND,((DOMAIN,a.com)),DIRECT"])
        self.assertTrue(result.failed)
        self.assertIn("Unsupported rule type", result.issues[0].message)
        self.assertNotIn("AND", result.output)

    def test_known_sections_mapped_and_differences_reported(self):
        lines = [
            "[General]", "ipv6 = false", "bypass-tun = 10.0.0.0/8", "skip-proxy = *.local, localhost", "dns-server = https://doh.example/dns-query",
            "[Proxy Group]", "AI = select,PROXY,DIRECT,policy-select-name=PROXY",
            "[Rule]", "DOMAIN-SUFFIX,example.com,AI", "IP-CIDR,2001:db8::1/64,DIRECT", "GEOIP,CN,DIRECT", "FINAL,AI",
            "[Host]", "*.example.net = server:system",
            "[URL Rewrite]", "^https?://example\\.cn https://example.com 302",
            "[MITM]", "hostname = *.example.cn",
        ]
        result = converter.parse_shadowrocket("sample.conf", lines)
        self.assertFalse(result.failed, [issue.message for issue in result.issues])
        for expected in ("[filter_local]", "host-suffix, example.com, AI", "ip6-cidr, 2001:db8::/64, direct", "final, AI", "[general]", "no-ipv6", "excluded_routes = 10.0.0.0/8", "[dns]", "[policy]", "[rewrite_local]", "302", "[mitm]"):
            self.assertIn(expected, result.output)
        self.assertGreater(len([issue for issue in result.issues if issue.status == "changed"]), 0)

    def test_bad_rewrite_and_bad_host_block(self):
        result = converter.parse_shadowrocket("bad.conf", ["[Rule]", "FINAL,DIRECT", "[URL Rewrite]", "^https://x/ reject", "[Host]", "host = not-an-ip"])
        self.assertTrue(result.failed)
        self.assertTrue(any("Unsupported URL Rewrite" in issue.message for issue in result.issues))
        self.assertTrue(any("Unsupported Host value" in issue.message for issue in result.issues))

    def test_filter_resource_keeps_duplicate_entries_and_order(self):
        result = converter.convert_filter_only("sr_ad_only.conf", ["[Rule]", "DOMAIN-SUFFIX,a.example,Reject", "DOMAIN-SUFFIX,b.example,Reject", "DOMAIN-SUFFIX,a.example,Reject"])
        self.assertFalse(result.failed)
        rules = [line for line in result.output.splitlines() if line.startswith("host-suffix,")]
        self.assertEqual(rules, ["host-suffix, a.example, reject", "host-suffix, b.example, reject", "host-suffix, a.example, reject"])


if __name__ == "__main__":
    unittest.main()
