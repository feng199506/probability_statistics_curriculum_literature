# 软件文档分片 sw 缺口与注意事项（检索日 2026-10-29）

清单：`scripts/seeds/materials/software_sw_cn.json`（35 条，S01–S06）。生成脚本不在库内。

## 版本/来源上的折中
- **IBM SPSS Statistics**：当前产品版本 31，其 PDF（ibm.com/docs/SSLVMB_31.0.0/pdf/…）对脚本访问返回 HTTP 403（疑似反爬），未绕过。改收 IBM 公共文档服务器 public.dhe.ibm.com 上 **27.0.1** 英文手册（7 个 PDF）。缺口：SPSS 28–31 版手册。
- **SAS/STAT**：15.4 完整用户指南合订本约 600 MB（statug.pdf，15.1 版 608 MiB），超过单条上限；改收 documentation.sas.com 上 15.4 的 **28 个章节 PDF**（9 个导论章 + 19 个核心过程）。缺口：其余约 80 个过程章节。
- **Stata 19**：只收 User's Guide、Getting Started、Base Reference 三本；ME/ST/SVY/TS/BAYES 等专题手册（同页可下）未收。
- **SciPy**：官方离线包为 1.18.0，PyPI 最新为 1.18.1（补丁版本，没有对应的离线包）。
- **R 手册**：r-release 目录仍是 4.6.1（2026-06-24）；R 4.6.2 今天（10-29）发布，手册可能随后更新。
- **ReadTheDocs 离线格式**（JupyterLab、pytest 的 PDF/htmlzip）：下载接口返回 429，改用 html 方式，只保存用户指南部分。

## CRAN 包混合格式 vignette 只收了一种格式
脚本的 pdfs 类型只能存 PDF，html 类型只能存 HTML 页，同一个包没法两种都收：
- lme4（pdfs）：未收 3 篇 HTML vignette（autoscale、covariance_structures、lmerperf）
- survey（pdfs）：未收 2 篇 HTML vignette（multiphase、survey-sae）
- glmmTMB（html）：未收 2 篇 PDF vignette（glmmTMB、model_evaluation）
- brms（html）：未收 2 篇 PDF vignette（brms_overview（JSS 2017）、brms_multilevel（R Journal 2018），均为开放获取论文）

## 只收用户指南/教程的条目
statsmodels、PyMC、ArviZ+EABM、lifelines、Quarto、JupyterLab、pytest、conda 只保存了用户指南或教程页，不含 API 参考；具体范围写在各条的 summary 里。

## 许可
Stata、SAS、SPSS 手册的版权页都写明保留全部权利（Stata 明文禁止复制）。官方免费公开下载，库内仅作个人学习留存，不应再分发。EABM 在线书为 CC-BY-NC 4.0，Stan 文档为 CC-BY-ND 4.0。

## 失败条目
- **S05-07 conda 26.9.4 User Guide**（html）：docs.conda.io 对本机 IP 返回 HTTP 429 限流，首轮下载在第 7 页中断，重试时连索引页都没取到。清单和 URL 正确，限流解除后执行 `python3 -I scripts/materials_en.py fetch software --only S05-07` 即可重跑。环境管理目前只有 renv（S05-06）通过核验。
