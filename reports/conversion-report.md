# Conversion report

Generated from https://github.com/Johnshall/Shadowrocket-ADBlock-Rules-Forever `release`.

Status: **passed with documented caveats**

| Source | Exact mappings | Behavior changes | Blocking issues |
|---|---:|---:|---:|
| `lazy.conf` | 12 | 37 | 0 |
| `lazy_group.conf` | 12 | 60 | 0 |
| `sr_ad_only.conf` | 54044 | 0 | 0 |
| `sr_adb.conf` | 54767 | 5 | 0 |
| `sr_backcn.conf` | 4 | 5 | 0 |
| `sr_backcn_ad.conf` | 54048 | 5 | 0 |
| `sr_cnip.conf` | 393 | 5 | 0 |
| `sr_cnip_ad.conf` | 54437 | 5 | 0 |
| `sr_direct_banad.conf` | 54046 | 5 | 0 |
| `sr_proxy_banad.conf` | 54053 | 5 | 0 |
| `sr_top500_banlist.conf` | 30265 | 6 | 0 |
| `sr_top500_banlist_ad.conf` | 84309 | 6 | 0 |
| `sr_top500_whitelist.conf` | 780 | 6 | 0 |
| `sr_top500_whitelist_ad.conf` | 54824 | 6 | 0 |

## `lazy.conf`

- **WARNING / changed**, line 271: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/iab0x00/ProxyRules/main/Rule/AI.txt,PROXY`)
- **WARNING / changed**, line 273: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/YouTube/YouTube.list,PROXY`)
- **WARNING / changed**, line 274: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Netflix/Netflix.list,PROXY`)
- **WARNING / changed**, line 275: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Disney/Disney.list,PROXY`)
- **WARNING / changed**, line 279: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/HBO/HBO.list,PROXY`)
- **WARNING / changed**, line 280: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Spotify/Spotify.list,PROXY`)
- **WARNING / changed**, line 281: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Telegram/Telegram.list,PROXY`)
- **WARNING / changed**, line 282: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/PayPal/PayPal.list,PROXY`)
- **WARNING / changed**, line 283: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Twitter/Twitter.list,PROXY`)
- **WARNING / changed**, line 284: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Facebook/Facebook.list,PROXY`)
- **WARNING / changed**, line 285: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Amazon/Amazon.list,PROXY`)
- **WARNING / changed**, line 287: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Sony/Sony.list,PROXY`)
- **WARNING / changed**, line 288: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Nintendo/Nintendo.list,PROXY`)
- **WARNING / changed**, line 289: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Epic/Epic.list,PROXY`)
- **WARNING / changed**, line 290: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/SteamCN/SteamCN.list,PROXY`)
- **WARNING / changed**, line 291: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Steam/Steam.list,PROXY`)
- **WARNING / changed**, line 292: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Game/Game.list,PROXY`)
- **WARNING / changed**, line 293: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/GitHub/GitHub.list,PROXY`)
- **WARNING / changed**, line 294: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Microsoft/Microsoft.list,PROXY`)
- **WARNING / changed**, line 295: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Google/Google.list,PROXY`)
- **WARNING / changed**, line 298: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/BiliBili/BiliBili.list,DIRECT`)
- **WARNING / changed**, line 299: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/NetEaseMusic/NetEaseMusic.list,DIRECT`)
- **WARNING / changed**, line 300: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Baidu/Baidu.list,DIRECT`)
- **WARNING / changed**, line 301: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/DouBan/DouBan.list,DIRECT`)
- **WARNING / changed**, line 303: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Sina/Sina.list,DIRECT`)
- **WARNING / changed**, line 304: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Zhihu/Zhihu.list,DIRECT`)
- **WARNING / changed**, line 305: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/XiaoHongShu/XiaoHongShu.list,DIRECT`)
- **WARNING / changed**, line 307: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/DouYin/DouYin.list,DIRECT`)
- **WARNING / changed**, line 308: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/TikTok/TikTok.list,PROXY`)
- **WARNING / changed**, line 314: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Lan/Lan.list,DIRECT`)
- **WARNING / changed**, line 23: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,localhost,*.local,captive.apple.com,*.ccb.com,*.abchina.com.cn,*.psbc.com,www.baidu.com,www.163.com`)
- **WARNING / changed**, line 26: tun-excluded-routes mapped to QuanX excluded_routes; validate equivalent tunnel scope (`tun-excluded-routes = 10.0.0.0/8, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0`)
- **WARNING / changed**, line 52: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://doh.pub/dns-query,https://dns.alidns.com/dns-query,223.5.5.5,119.29.29.29`)
- **WARNING / unsupported**, line 58: Shadowrocket setting not represented in QuanX output: fallback-dns-server=system (`fallback-dns-server = system`)
- **WARNING / unsupported**, line 64: Shadowrocket setting not represented in QuanX output: prefer-ipv6=false (`prefer-ipv6 = false`)
- **WARNING / unsupported**, line 67: Shadowrocket setting not represented in QuanX output: dns-direct-system=false (`dns-direct-system = false`)
- **WARNING / unsupported**, line 70: Shadowrocket setting not represented in QuanX output: icmp-auto-reply=true (`icmp-auto-reply = true`)
- **WARNING / unsupported**, line 73: Shadowrocket setting not represented in QuanX output: always-reject-url-rewrite=false (`always-reject-url-rewrite = false`)
- **WARNING / unsupported**, line 76: Shadowrocket setting not represented in QuanX output: private-ip-answer=true (`private-ip-answer = true`)
- **WARNING / unsupported**, line 79: Shadowrocket setting not represented in QuanX output: dns-direct-fallback-proxy=true (`dns-direct-fallback-proxy = true`)
- **WARNING / unsupported**, line 88: Shadowrocket setting not represented in QuanX output: hijack-dns=8.8.8.8:53,8.8.4.4:53 (`hijack-dns = 8.8.8.8:53,8.8.4.4:53`)
- **WARNING / unsupported**, line 91: Shadowrocket setting not represented in QuanX output: udp-policy-not-supported-behaviour=REJECT (`udp-policy-not-supported-behaviour = REJECT`)
- **WARNING / unsupported**, line 97: Shadowrocket setting not represented in QuanX output: stun-response-ip=1.1.1.1 (`stun-response-ip = 1.1.1.1`)
- **WARNING / unsupported**, line 98: Shadowrocket setting not represented in QuanX output: stun-response-ipv6=::1 (`stun-response-ipv6 = ::1`)
- **WARNING / unsupported**, line 116: Shadowrocket setting not represented in QuanX output: block-quic=all-proxy (`block-quic = all-proxy`)
- **WARNING / changed**, line 333: Host system-resolution mapping converted to QuanX DNS policy; validate wildcard scope (`*.apple.com = server:system`)
- **WARNING / changed**, line 334: Host system-resolution mapping converted to QuanX DNS policy; validate wildcard scope (`*.icloud.com = server:system`)
- **WARNING / changed**, line 335: Loopback host mapping translated to reject filter as recommended by QuanX sample; response semantics differ (`localhost = 127.0.0.1`)
- **WARNING / changed**, line 346: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn`)

## `lazy_group.conf`

- **WARNING / changed**, line 199: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 200: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 201: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 202: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 203: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 204: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 205: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,DIRECT,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 206: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 207: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 208: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 209: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,DIRECT,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 210: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,DIRECT,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 211: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,DIRECT,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=DIRECT`)
- **WARNING / changed**, line 212: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 213: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,DIRECT,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 214: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,DIRECT,PROXY,香港节点,台湾节点,policy-select-name=DIRECT`)
- **WARNING / changed**, line 215: Shadowrocket select group mapped to QuanX static policy; initial selection and node availability can differ (`select,DIRECT,PROXY,香港节点,台湾节点,日本节点,新加坡节点,韩国节点,美国节点,policy-select-name=PROXY`)
- **WARNING / changed**, line 216: Shadowrocket url-test mapped to a QuanX static group filtered by server tags; automatic latency selection, test interval, tolerance, timeout, and selected node are not preserved (`url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=🇭🇰|HK|Hong|hong|香港|深港|沪港|京港|港`)
- **WARNING / changed**, line 217: Shadowrocket url-test mapped to a QuanX static group filtered by server tags; automatic latency selection, test interval, tolerance, timeout, and selected node are not preserved (`url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=🇹🇼|TW|TWN|Taiwan|Taipei|taiwan|台湾|台灣|台北|台中|新北|彰化`)
- **WARNING / changed**, line 218: Shadowrocket url-test mapped to a QuanX static group filtered by server tags; automatic latency selection, test interval, tolerance, timeout, and selected node are not preserved (`url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=🇯🇵|JP|Japan|japan|Tokyo|tokyo|日本|东京|大阪|京日|苏日|沪日|上日|川日|深日|广日|日`)
- **WARNING / changed**, line 219: Shadowrocket url-test mapped to a QuanX static group filtered by server tags; automatic latency selection, test interval, tolerance, timeout, and selected node are not preserved (`url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=🇸🇬|SG|Sing|sing|新加坡|狮城|沪新|京新|深新|杭新|广新`)
- **WARNING / changed**, line 220: Shadowrocket url-test mapped to a QuanX static group filtered by server tags; automatic latency selection, test interval, tolerance, timeout, and selected node are not preserved (`url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=🇰🇷|KR|Korea|korea|KOR|韩国|首尔|韩|韓|春川`)
- **WARNING / changed**, line 221: Shadowrocket url-test mapped to a QuanX static group filtered by server tags; automatic latency selection, test interval, tolerance, timeout, and selected node are not preserved (`url-test,url=http://www.gstatic.com/generate_204,interval=600,tolerance=0,timeout=5,select=0,policy-regex-filter=🇺🇸|US|USA|America|america|United States|美国|凤凰城|洛杉矶|西雅图|芝加哥|纽约|沪美|美`)
- **WARNING / changed**, line 295: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/iab0x00/ProxyRules/main/Rule/AI.txt,AI`)
- **WARNING / changed**, line 297: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/YouTube/YouTube.list,YOUTUBE`)
- **WARNING / changed**, line 298: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Netflix/Netflix.list,NETFLIX`)
- **WARNING / changed**, line 299: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Disney/Disney.list,DISNEY+`)
- **WARNING / changed**, line 303: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/HBO/HBO.list,MAX`)
- **WARNING / changed**, line 304: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Spotify/Spotify.list,SPOTIFY`)
- **WARNING / changed**, line 305: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Telegram/Telegram.list,TELEGRAM`)
- **WARNING / changed**, line 306: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/PayPal/PayPal.list,PAYPAL`)
- **WARNING / changed**, line 307: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Twitter/Twitter.list,TWITTER`)
- **WARNING / changed**, line 308: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Facebook/Facebook.list,FACEBOOK`)
- **WARNING / changed**, line 309: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Amazon/Amazon.list,AMAZON`)
- **WARNING / changed**, line 311: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Sony/Sony.list,游戏平台`)
- **WARNING / changed**, line 312: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Nintendo/Nintendo.list,游戏平台`)
- **WARNING / changed**, line 313: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Epic/Epic.list,游戏平台`)
- **WARNING / changed**, line 314: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/SteamCN/SteamCN.list,游戏平台`)
- **WARNING / changed**, line 315: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Steam/Steam.list,游戏平台`)
- **WARNING / changed**, line 316: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Game/Game.list,游戏平台`)
- **WARNING / changed**, line 317: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/GitHub/GitHub.list,PROXY`)
- **WARNING / changed**, line 318: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Microsoft/Microsoft.list,微软服务`)
- **WARNING / changed**, line 319: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Google/Google.list,谷歌服务`)
- **WARNING / changed**, line 322: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/BiliBili/BiliBili.list,哔哩哔哩`)
- **WARNING / changed**, line 323: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/NetEaseMusic/NetEaseMusic.list,DIRECT`)
- **WARNING / changed**, line 324: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Baidu/Baidu.list,DIRECT`)
- **WARNING / changed**, line 325: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/DouBan/DouBan.list,DIRECT`)
- **WARNING / changed**, line 327: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Sina/Sina.list,DIRECT`)
- **WARNING / changed**, line 328: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Zhihu/Zhihu.list,DIRECT`)
- **WARNING / changed**, line 329: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/XiaoHongShu/XiaoHongShu.list,DIRECT`)
- **WARNING / changed**, line 331: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/DouYin/DouYin.list,DIRECT`)
- **WARNING / changed**, line 332: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/TikTok/TikTok.list,TIKTOK`)
- **WARNING / changed**, line 338: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/Lan/Lan.list,DIRECT`)
- **WARNING / changed**, line 23: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16,10.0.0.0/8,172.16.0.0/12,localhost,*.local,captive.apple.com,*.ccb.com,*.abchina.com.cn,*.psbc.com,www.baidu.com,www.163.com`)
- **WARNING / changed**, line 26: tun-excluded-routes mapped to QuanX excluded_routes; validate equivalent tunnel scope (`tun-excluded-routes = 10.0.0.0/8, 127.0.0.0/8, 169.254.0.0/16, 172.16.0.0/12, 192.0.0.0/24, 192.0.2.0/24, 192.88.99.0/24, 192.168.0.0/16, 198.51.100.0/24, 203.0.113.0/24, 224.0.0.0`)
- **WARNING / changed**, line 52: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://doh.pub/dns-query,https://dns.alidns.com/dns-query,223.5.5.5,119.29.29.29`)
- **WARNING / unsupported**, line 58: Shadowrocket setting not represented in QuanX output: fallback-dns-server=system (`fallback-dns-server = system`)
- **WARNING / unsupported**, line 64: Shadowrocket setting not represented in QuanX output: prefer-ipv6=false (`prefer-ipv6 = false`)
- **WARNING / unsupported**, line 67: Shadowrocket setting not represented in QuanX output: dns-direct-system=false (`dns-direct-system = false`)
- **WARNING / unsupported**, line 70: Shadowrocket setting not represented in QuanX output: icmp-auto-reply=true (`icmp-auto-reply = true`)
- **WARNING / unsupported**, line 73: Shadowrocket setting not represented in QuanX output: always-reject-url-rewrite=false (`always-reject-url-rewrite = false`)
- **WARNING / unsupported**, line 76: Shadowrocket setting not represented in QuanX output: private-ip-answer=true (`private-ip-answer = true`)
- **WARNING / unsupported**, line 79: Shadowrocket setting not represented in QuanX output: dns-direct-fallback-proxy=true (`dns-direct-fallback-proxy = true`)
- **WARNING / unsupported**, line 88: Shadowrocket setting not represented in QuanX output: hijack-dns=8.8.8.8:53,8.8.4.4:53 (`hijack-dns = 8.8.8.8:53,8.8.4.4:53`)
- **WARNING / unsupported**, line 91: Shadowrocket setting not represented in QuanX output: udp-policy-not-supported-behaviour=REJECT (`udp-policy-not-supported-behaviour = REJECT`)
- **WARNING / unsupported**, line 97: Shadowrocket setting not represented in QuanX output: stun-response-ip=1.1.1.1 (`stun-response-ip = 1.1.1.1`)
- **WARNING / unsupported**, line 98: Shadowrocket setting not represented in QuanX output: stun-response-ipv6=::1 (`stun-response-ipv6 = ::1`)
- **WARNING / unsupported**, line 116: Shadowrocket setting not represented in QuanX output: block-quic=all-proxy (`block-quic = all-proxy`)
- **WARNING / changed**, line 357: Host system-resolution mapping converted to QuanX DNS policy; validate wildcard scope (`*.apple.com = server:system`)
- **WARNING / changed**, line 358: Host system-resolution mapping converted to QuanX DNS policy; validate wildcard scope (`*.icloud.com = server:system`)
- **WARNING / changed**, line 359: Loopback host mapping translated to reject filter as recommended by QuanX sample; response semantics differ (`localhost = 127.0.0.1`)
- **WARNING / changed**, line 370: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn`)

## `sr_adb.conf`

- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 54876: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_backcn.conf`

- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 30: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_backcn_ad.conf`

- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 54100: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_cnip.conf`

- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 457: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_cnip_ad.conf`

- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 54527: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_direct_banad.conf`

- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 54096: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_proxy_banad.conf`

- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 54104: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_top500_banlist.conf`

- **WARNING / changed**, line 30336: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/AppleNews/AppleNews.list,PROXY`)
- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 30345: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_top500_banlist_ad.conf`

- **WARNING / changed**, line 84405: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/AppleNews/AppleNews.list,PROXY`)
- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 84414: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_top500_whitelist.conf`

- **WARNING / changed**, line 854: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/AppleNews/AppleNews.list,PROXY`)
- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 863: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)

## `sr_top500_whitelist_ad.conf`

- **WARNING / changed**, line 54924: Mapped external resource path from Shadowrocket to QuantumultX; verify target list semantics and URL availability (`RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/AppleNews/AppleNews.list,PROXY`)
- **WARNING / changed**, line 7: IPv6 disabled using QuanX [dns] no-ipv6; tunnel behavior may differ (`ipv6 = false`)
- **WARNING / unsupported**, line 8: Shadowrocket setting not represented in QuanX output: bypass-system=true (`bypass-system = true`)
- **WARNING / changed**, line 9: skip-proxy entries mapped to direct filter rules; bypassing the tunnel and direct routing are not identical (`192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.ap`)
- **WARNING / changed**, line 10: bypass-tun mapped to QuanX excluded_routes; validate equivalent tunnel scope (`bypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,`)
- **WARNING / changed**, line 11: DNS resolver list mapped to QuanX; resolver order/fallback and mixed encrypted/unencrypted DNS semantics may differ (`https://dns.alidns.com/dns-query, https://doh.pub/dns-query`)
- **WARNING / changed**, line 54933: Copied MITM hostnames; QuanX certificate installation/trust and TLS behavior must be configured separately (`hostname = *.google.cn,*.googlevideo.com`)
