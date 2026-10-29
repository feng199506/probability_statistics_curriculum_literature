
## 案例（cases，分片 m6，E1–E6；检索日 2026-10-29）

清单：scripts/seeds/materials/cases_m6_cn.json（25 条）。状态以 scripts/state/materials/E*.json 为准。

### 缺口
- E2 经济金融：缺“公开市场数据 + 代码”的金融计量/风险管理案例（资产定价、VaR、波动率）。Tidy Finance 等依赖 WRDS 订阅数据，不收；BLS Handbook of Methods 对脚本返回 HTTP 403，未绕过。
- E6 公共政策：缺“政府机构发布、带代码”的政策评估报告（如 CBO 最低工资报告仅有文字，无代码）；Card-Krueger 原始数据未单列，经 E2-01（MHE 复现脚本运行时下载）覆盖；Lalonde/NSW 经 E6-04 与 E5-04（ROS Lalonde 目录）覆盖。
- E1 生物医学：Epi R Handbook（appliedepi/epiRhandbook_eng）与 Imperial covid19model 未收——GitHub API 被共享 IP 限流，未能确认大小，估计超过 150 MB 上限；可后续确认后补。
- scunning1975/mixtape：归档 > 150 MB（实测下载超 160 MB 截断），不收。
- joonho112/Bayesian-causal-inference（E1-03/E6-04 的源码仓库）归档约 100 MB，主要是 knitr 缓存，未收；页面已内嵌全部代码。

### 注意事项
- HTML 案例只保存页面本身：NIST 案例页链接的 .dp/.r 脚本与 datasets/*.DAT、NHANES Sample Code 页链接的 .sas/.do/.r 文件不是 HTML，脚本不保存，需另行下载；Stan 案例的数据在 stan-dev/example-models（仓库大，未下载）。
- 未声明许可证：E2-01、E4-03、E5-03、E6-01、E6-02（仓库无 LICENSE）；E5-04 仓库无 LICENSE（rosdata 包 DESCRIPTION 写 Code BSD3、数据按来源）；E1-01、E1-03、E4-04、E6-04 页面无许可证声明；NIST e-Handbook 无显式许可证（美国政府出版物）。E1-04 为 CC BY-NC-ND 4.0（不可改作）。
- 数据需另行获取：E2-01（MIT Angrist 数据存档，部分旧链接可能失效）、E2-02（完整生产数据因再分发限制不提供）、E2-04/E5-02（CPS/ACS 公共使用微观数据）、E4-01（ScienceBase 配套材料 doi:10.5066/P9JWL6XR）、E5-01（NHANES XPT 文件）。
- 已核验 git 快照解压后最大：E5-04 ROS-Examples 约 267 MB、E1-04 r4csr 约 104 MB（ADaM sas7bdat）。
- 下载代码均未运行。
- E5-01 NHANES 教程：首页同时链接大小写两种 URL（如 Datasets.aspx / datasets.aspx），link_regex 匹配到 17 个页面，实为 9 个模块（含 8 个大小写重复页），内容完整，重复无害。

## 培养方案（curricula，分片 m6，P-01…P-25；检索日 2026-10-29）

清单：scripts/seeds/materials/curricula_m6_cn.json（25 条，全部核验通过）；层次/属性简表：scripts/annotations/curricula_level_map_cn.md。

### 缺口
- 未收：LSE 课程章程（calendar 新学年链接 404）；Columbia 统计研究生项目页（stat.columbia.edu 对脚本 403，仅收 Columbia College Bulletin 本科部分 P-11）；Stanford 统计本科（无统计学士，仅辅修，未收）。
- 中文：复旦大数据学院、华东师大统计学院的培养方案栏目为脚本渲染/无附件链接，未取得；人大 2024 级普通博士方案 PDF 服务器极慢多次截断，仅收直博（理学）与流病硕士（P-25）；人大本科最新公开为 2020 级理科试验班（较旧，未收）；中国科大本科统计方案未找到官方公开文件（只收研究生 2025 版 P-23）。
- 北大 P-22 为 2023 年修订的数学科学学院本科生教学手册（整院手册，含统计学专业方案），不是独立统计学方案；北大统计中心站点 stat.pku.edu.cn 证书链不完整，脚本无法访问。

### 注意事项
- HTML 方案页只保存页面本身与页面资源；页面链接到的学生手册 PDF（如 Harvard handbook、ETH 学期样表 PDF）未下载。
- P-17 Cambridge Part III 课程说明来自现行页面，部分文件标 2025-26、部分标 2026-27；P-14 Oxford 手册 2025-26 与 Part B/C 2026-27 补充册混合，适用学年按文件各自标注。
- 美国项目页大多未标学年（记为"现行"）；Chicago/CMU/Columbia 为 2026-27 官方目录。
- 课程名称凡未在页面原文中核对到的只写课号（UW BIOST、Columbia GU42xx 以上选修），并在 courses_note 注明"以页面为准"。
- 中国方案 PDF 下载速度慢（中国站点 10–60 KB/s），P-23 首次抓取截断失败，--only 重跑通过。
