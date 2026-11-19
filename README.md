# Johnshall Shadowrocket Rules → Quantumult X

将 [Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) 的 `release` 分支配置转换为 Quantumult X（QuanX）格式，并定时检查上游更新。

> **状态：自动转换验证中。** 本项目生成 QuanX 语法并标注已知差异，不保证 Shadowrocket 与 QuanX 的网络行为完全等价。尤其 `lazy.conf` / `lazy_group.conf` 依赖你的 QuanX 策略和服务器资源，必须按本文配置后才能使用。

## 规则文件

每个上游 `.conf` 会生成 `dist/<源文件名>.quanx.conf`。例如：

- `dist/sr_ad_only.quanx.conf` — 独立广告过滤规则；可作为本地过滤规则内容或经你的托管服务分发。
- `dist/sr_top500_whitelist_ad.quanx.conf` — Top 500 白名单路由与广告规则配置。
- `dist/lazy_group.quanx.conf` — 使用策略组的完整配置片段。

最新输出和逐行转换备注见 [`reports/conversion-report.md`](reports/conversion-report.md)。首次仓库建立并成功运行 Actions 后，公开订阅链接将形如：

```text
https://raw.githubusercontent.com/<owner>/Shadowrocket-ADBlock-Rules-Forever-QuantumultX/main/dist/sr_ad_only.quanx.conf
```

因远程资源发布是 QuanX 的不同入口（过滤资源列表与带 section 的配置片段不能混用），请按具体文件格式导入。私有配置里的自定义策略组无法仅靠规则文件带来代理节点。

## 自动更新

GitHub Actions 每天 23:15 UTC 执行，并支持手动触发。上游构建工作流在 23:00 UTC 更新 `release`，此处安排在之后；如上游调度变化，可编辑 `.github/workflows/sync.yml`。转换器从上游根目录枚举全部 `.conf`，下载、转换、生成报告；遇到下载失败或未知活动指令时工作流失败并阻止不完整输出合入。输出无变化时不会产生提交。

## 转换策略与限制

转换器 `scripts/convert.py` 是严格解析器，不是通用 Shadowrocket 配置执行器：

- 常见 `DOMAIN*`、`USER-AGENT`、`GEOIP`、`IP-ASN`、`DST-PORT`、`IP-CIDR`、`FINAL` 映射到 QuanX `filter_local` 语法；IP 地址族单独识别并规范化 CIDR。
- `RULE-SET` 对 `/Shadowrocket/` 资源尝试替换为同一规则项目的 `/QuantumultX/` 路径；转换日志中列出所有改写。第三方列表内容和可用性可能独立变化。
- Shadowrocket 的 `select`、`url-test` 组转换为 QuanX `[policy]` 的 `static` 组；地区测速组用 `server-tag-regex` 过滤候选。它们不保留 Shadowrocket 原有的初始选择与自动延迟选择，使用前需在 QuanX 验证策略候选及订阅服务器标签。
- DNS server、`skip-proxy`、TUN exclusions、Host、重写、MITM 主机名仅按报告中的规则转换；细节可能不同。MITM 还需要在 QuanX 单独安装并信任证书。
- `lazy*` 的 `[Proxy]` 没有实际节点定义，其他 Shadowrocket 专属 General 设置可能没有 QuanX 对等项，并在报告中作为差异提醒。未识别的活动规则、组或 section 会失败，不会静默丢弃。
- 客户端导入和真实流量未在本自动化中验证；首次使用应先检查策略引用、DNS、证书和流量行为。不要把本仓库输出当作安全审计结果。

## 本地运行

需要 Python 3.9+，不依赖第三方包：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/convert.py --input-dir ./fixtures --output-dir ./dist --report ./reports/conversion-report.md
python3 scripts/convert.py --output-dir ./dist --report ./reports/conversion-report.md
```

默认运行会从 GitHub API 读取上游 `release` 根目录并下载配置。可使用 `--input-dir` 进行离线测试。注意上游文件很大，测试数据不提交在仓库内。

## 署名与许可

上游项目 [Johnshall/Shadowrocket-ADBlock-Rules-Forever](https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever) 声明采用 **CC BY-SA 4.0**。本项目为其转换/改编，保留来源及许可链接，修改说明见转换报告；本项目发布的转换输出也按 CC BY-SA 4.0 提供。许可文本见 [`LICENSE`](LICENSE)。第三方远程资源各自可能有单独的许可和维护者，本项目不将其重新托管。
