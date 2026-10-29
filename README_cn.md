# 概率与统计课程文献库（本科—硕士—博士）

检索与下载日：2026-10-29。库路径：`/root/probability_statistics_curriculum_literature`（不含 scripts 约 7.5G）。只计已完整下载并通过内容核验的资料；失败、残缺、待核实、排除项见 `download_failures_cn.csv`。本轮未做整库 SHA256 扫描或下载回验（SHA256 列为下载当时记录的值）；未运行任何案例代码、未安装依赖、未上传。

## 一、总量（全库按独立资料去重）

| 资料类型 | 已核验 | 其中已有复用 |
|---|---|---|
| 教材 | 74 | 10 |
| 课程讲义 | 57 | 6 |
| 实践 | 50 | 0 |
| 论文 | 652 | 0 |
| 案例 | 25 | 0 |
| 软件文档 | 34 | 0 |
| 培养方案 | 25 | 0 |
| **合计** | **917** | **16**（本轮新下载 901） |

复用来源：工业过程监控库、时间序列库（复制并重新核验，原库文件未移动或删除；原库编号见 catalog 的“复用来源”列）。原计划复用的机器学习/深度学习库在本轮执行期间已不在本机，相关资料改从官方来源直接下载。

## 二、各课程群数量

目标：教材 3–5、课程讲义 2–4、实践 2–5；研究型群论文 30–50（01–03、19 以教材为主，不设论文目标）。跨群资料只在主群计一次，通过“关联课程群”列引用。

| 课程群 | 教材 | 课程讲义 | 实践 | 论文 | 论文近三年占比 | 三年前经典 |
|---|---|---|---|---|---|---|
| 01 数学基础 | 5 | 3 | 2 | 不设 | — | — |
| 02 高阶数学工具 | 4 | 3 | 2 | 不设 | — | — |
| 03 基础概率论 | 3 | 3 | 3 | 不设 | — | — |
| 04 高等概率论 | 3 | 4 | 2 | 40 | 90.0% | 4 |
| 05 随机过程 | 4 | 3 | 2 | 41 | 92.7% | 3 |
| 06 随机分析及概率专题 | 5 | 3 | 2 | 40 | 90.0% | 4 |
| 07 数理统计与统计决策 | 2 | 4 | 2 | 42 | 90.5% | 4 |
| 08 渐近统计与理论专题 | 3 | 3 | 2 | 40 | 90.0% | 4 |
| 09 回归与线性模型 | 3 | 2 | 2 | 40 | 87.5% | 5 |
| 10 多元、高维与统计学习 | 5 | 2 | 2 | 40 | 90.0% | 4 |
| 11 贝叶斯统计 | 4 | 2 | 3 | 42 | 88.1% | 5 |
| 12 非参数、半参数与稳健统计 | 3 | 3 | 3 | 40 | 90.0% | 4 |
| 13 时间序列与空间统计 | 4 | 3 | 3 | 42 | 90.5% | 4 |
| 14 实验设计、调查抽样与因果推断 | 5 | 2 | 2 | 40 | 92.5% | 3 |
| 15 生物统计与公共卫生 | 3 | 3 | 3 | 41 | 95.1% | 2 |
| 16 经济、金融、保险与风险 | 3 | 3 | 2 | 40 | 90.0% | 4 |
| 17 工业、环境与其他专业应用 | 4 | 3 | 2 | 42 | 97.6% | 1 |
| 18 统计计算与数据科学 | 4 | 3 | 3 | 42 | 88.1% | 5 |
| 19 统计编程与分析工程 | 4 | 3 | 5 | 不设 | — | — |
| 20 研究方法与实战 | 3 | 2 | 3 | 40 | 90.0% | 4 |

论文合计 652 篇，近三年（首次公开 2023-10-29 至 2026-10-29）592 篇，占 90.8%；三年前条目均为必要经典，理由见 catalog 的“三年前或经典保留理由”列。

### 专业区

| 案例领域 | 已核验 |
|---|---|
| E1 生物医学 | 4 |
| E2 经济金融 | 4 |
| E3 工业 | 4 |
| E4 环境水文 | 5 |
| E5 社会调查 | 4 |
| E6 公共政策 | 4 |

| 软件类别（按项目+版本计） | 已核验 |
|---|---|
| S01 R 基础/数据处理/可视化/报告 | 5 |
| S02 Python 科学栈 | 6 |
| S03 贝叶斯与概率编程 | 4 |
| S04 混合模型/生存/调查/时间序列/空间 | 10 |
| S05 Quarto/Jupyter/Git/测试/环境 | 6 |
| S06 SAS/Stata/SPSS 公开手册 | 3 |

培养方案按学位层次：博士 6，本科 7，本科/硕士（Part C 为第四年 MMath） 1，硕士 7，硕士/博士 4。

## 三、层次与理论/应用覆盖（教材、课程、实践）

学位层次（一条可跨多个层次）：本科 88，硕士 106，博士 66。
理论严格度：应用入门 65，严格理论 62，兼顾 54。
课程资料包类型：完整文字讲义 27，OCW 官方课程包 22，OCW 官方课程包（课件为主） 3，完整课件包 3，讲义+课件 2。
实践类型：习题集 18，综合项目 8，模拟演示 7，方法比较 6，时间序列预测 4，贝叶斯计算 2，因果分析 2，回归诊断 1，实验与调查 1，生存与纵向 1。

## 四、论文年份分布（按首次公开年）

| 年份 | 篇数 |
|---|---|
| 2002 | 1 |
| 2004 | 1 |
| 2008 | 2 |
| 2009 | 1 |
| 2010 | 1 |
| 2011 | 3 |
| 2012 | 1 |
| 2013 | 1 |
| 2014 | 4 |
| 2015 | 6 |
| 2016 | 6 |
| 2017 | 7 |
| 2018 | 1 |
| 2019 | 9 |
| 2020 | 5 |
| 2021 | 4 |
| 2022 | 7 |
| 2023 | 29 |
| 2024 | 241 |
| 2025 | 184 |
| 2026 | 138 |

## 五、失败、残缺、待核实与排除

| 资料类型 | 状态 | 条数 |
|---|---|---|
| 习题/实验/实践材料 | 已排除 | 5 |
| 教科书/专著/参考书 | 已排除 | 5 |
| 统计软件官方文档 | 下载失败/核验未通过 | 1 |
| 论文/综述/教程 | 下载失败/核验未通过 | 11 |
| 论文/综述/教程 | 人工拒收 | 4 |

逐条原因见 `download_failures_cn.csv`。论文失败多为短篇笔记未达自动核验阈值（<4 页、<12000 字符或无参考文献节），由同群后备补位；“已排除”为跨区重复、超出大小上限或内容重复的主动排除；“人工拒收”为与教材重复的论文副本。

## 六、说明与已知缺口

### 主要缺口（未找到合法完整全文或受访问限制，均未绕过）
- 教材：Blitzstein–Hwang《Introduction to Probability》（官方入口为禁止下载的 Google Drive）、Rassoul-Agha–Seppäläinen 大偏差专著（作者站 403）、Hansen《Econometrics》与 Efron《Large-Scale Inference》（作者已不再提供全文）、Johnstone《Gaussian Estimation》（未找到官方公开地址）、Bijma–Jonker–van der Vaart《An Introduction to Mathematical Statistics》（出版社 DRM 电子书，非开放获取）。
- 07 群自有教材 2 本（Gentle、Efron–Hastie），另通过关联编号引用 B03-03（Evans–Rosenthal，以 B03-03 计一次）。
- 课程：Stanford Stats 300B 习题解答需 SSO 登录，仅收题目；Berkeley 210B 2013 作业链接全部 404；Harvard Stat 110、PSU STAT 503/506、Iowa（Breheny）站点无法以脚本合法访问。
- 部分 OCW 课程包本身不完整（如 HST.502 第 1、10 讲无讲义，17.801 仅 8 份课件），按官方完整课程包计数，内容不全已在核验说明中注明。Owen《Monte Carlo》第 12–14 章作者尚未放出。
- 培养方案：LSE（链接 404）、Columbia 研究生项目（403）、复旦大数据学院与华东师大统计学院（栏目由脚本渲染/无附件）、人大普博方案（下载截断）、中国科大统计本科方案（未见官方公开文件）未收；北大为数学科学学院整院本科手册。
- 案例：经济金融缺“公开市场数据 + 代码”的金融风险案例（Tidy Finance 依赖需订阅的 WRDS 数据）；公共政策缺政府机构附代码的政策评估报告；Mixtape、Epi R Handbook（仓库过大，后者以 D15-03 源仓库形式另收）、Imperial covid19model 未收。
- 软件：conda 用户指南（docs.conda.io 对本机 IP 限流，见失败清单）；SPSS 现行版 31 手册对脚本 403，收 27.0.1；SAS/STAT 15.4 只收导论与核心过程章节；lme4/survey/glmmTMB/brms 各缺 2–3 篇另一格式的 vignette；statsmodels、lifelines、pytest 只保存用户指南部分（非整站 API 参考）。

### 版本与许可提示
- 作者草稿或预出版版本：Durrett《Essentials of Stochastic Processes》（2011 Almost Final Version）、Tao《Topics in Random Matrix Theory》（草稿）、Owen《Monte Carlo》（书写中）、Aldous–Fill（未完成稿）。
- 仅限个人或非商业使用：CASI、ROS、BDA3、Bayesian Workflow、Bayesian Filtering and Smoothing；CC BY-NC-ND：Oehlert、Kim、r4csr 案例（E1-04）；CC BY-ND：Stan 文档；CC BY-NC：ArviZ EABM。
- Stata、SAS、SPSS 手册为官方免费下载但保留全部权利（Stata 明文禁止复制），仅作个人学习留存，不应再分发。
- 多个案例仓库与课程页面未声明许可证，catalog 中如实写“未声明许可证”。
- 15、16、17、18、20 群的非 arXiv 论文（PMC、JSS、ASCMO、Survey Methodology、PLOS）以出版方首次在线或发表日为首次公开日；未逐篇排查更早的预印本，个别条目实际首次公开可能更早。

### 核验方法
- PDF：HTTP 200、%PDF 头、pypdf 可解析、页数下限、前 12 页名称短语（教材/讲义）；论文另要求 ≥4 页、≥12000 可抽取字符、标题词匹配 ≥0.8、第一作者姓氏、参考文献节。未过标题/作者比对的进入“待核验”，经人工查看首页后放行或拒收（理由写入核验说明）。
- 课程包：官方索引页列出的全部匹配文件逐个下载并解析；OCW 为官方 zip，校验完整性并解析其中全部 PDF。
- HTML 教材/文档：目录页解析出的全部页面 HTTP 200 且正文达到字符下限，wget 离线保存（含页面资源、改写链接），页面清单在各目录 `PAGES_*.txt`。
- 代码仓库：固定 commit 的官方归档，zip 完整性 + 关键文件检查，记录许可证文件；未运行。
- 去重：同一论文只计入编号最小的课程群；同一文件（下载时 SHA256 相同）只计一次，重复副本移出库外（`/root/.cache/pscl_lit/crossdup/`、`rejected/`，未删除），失败清单记为“已排除/人工拒收”。

### 目录结构
- `curricula/` 培养方案与课程目录（P-xx）；`courses/` 大学课程讲义与课程包（Axx-xx）；`books/` 教材专著（Bxx-xx）；`papers/NN_slug/` 论文（Cxx-xxx）；`practice/` 习题、实验与实践仓库（Dxx-xx），`practice/cases/` 专业应用案例（Ex-xx）；`software_docs/` 软件官方文档（Sxx-xx）；`guides/` 学习指南；`scripts/` 流程脚本、清单（seeds）、状态（state）、注释（annotations）。
- 文件命名：自建与下载的独立文件在扩展名前标语言（`_en`、`_cn` 等）；上游源码仓库与离线 HTML 内部保留原文件名和引用结构，外层目录加语言后缀。

### 学习指南（`guides/`）
`undergraduate_path_cn.md`、`masters_theory_path_cn.md`、`masters_applied_path_cn.md`、`phd_probability_path_cn.md`、`phd_statistics_path_cn.md`、`professional_tracks_cn.md`、`statistical_computing_path_cn.md`、`practice_projects_cn.md`、`core_reading_list_cn.md`、`curriculum_map_cn.md`。指南中每条资料都带编号和本地路径（由 `scripts/link_guides_en.py` 校验，未核验编号会报错）；推荐基于资料定位与目录层面判断，不代表已精读或已复现实验。

### 续跑与重建命令
```bash
cd /root/probability_statistics_curriculum_literature
bash scripts/resume_all_en.sh            # 继续未完成下载（已核验条目自动跳过，不覆盖文件）
bash scripts/resume_all_en.sh --retry    # 同时重试失败条目（如 conda 文档 S05-07）
python3 -I scripts/reconcile_claims_en.py --apply   # 种子调整后处理跨群重复
python3 -I scripts/build_catalog_en.py && python3 -I scripts/search_log_en.py
python3 -I scripts/link_guides_en.py && python3 -I scripts/build_readme_en.py
```
单项：`python3 -I scripts/materials_en.py fetch <books|courses|practice|cases|software|curricula> --only <编号>`；论文：`python3 -I scripts/papers_en.py download NN`。pypdf 位于 `/root/.cache/pscl_lit/pylib`（本机无 pip）；arXiv 限速锁与兄弟库共用。

