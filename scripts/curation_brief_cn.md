# 论文选题规范（C 类：研究论文、综述与学术教程）

库根目录 LIB=`/root/probability_statistics_curriculum_literature`。命令都在 LIB 下运行，Python 一律 `python3 -I`。
检索日 2026-10-29；近三年窗口 = 首次公开日（arXiv v1 或出版方首次在线日）在 2023-10-29 至 2026-10-29 之间。

## 目标（每个研究型课程群）
- 主列表 38–42 条 + 后备 6–8 条（`"reserve": true`，主列表下载失败时按顺序补位）。核验通过的全文目标为每群 30–50 篇。
- 主列表中三年前（首次公开 < 2023-10-29）的必要经典**最多 5 条**，每条写 `classic_reason`（为什么非它不可）。近三年占主列表比例须 ≥ 88%（留余量保证核验后 ≥ 85%）。
- 内容定位：概率与统计专业**本科—硕士—博士系统学习**资料库，不只是 AI 所需的统计基础。优先：综述（survey/review）、学术教程（tutorial/primer/lecture notes/长篇讲义式文章）、Probability Surveys / Statistics Surveys / Statistical Science 类综述、该子方向近三年代表性的方法或理论论文、软件与方法说明（如 Journal of Statistical Software 的方法包论文，用于计算/应用群）。约一半综述/教程、一半代表性研究即可。
- 只收与本群教学内容直接相关的资料；做不到 30 篇时**宁缺毋滥**，在 `scripts/annotations/papers_gap_NN_cn.md` 写明缺口和原因。
- 不收：博客、新闻、只有摘要、撤稿/作者撤回、与本群教学关联弱的纯应用论文、纯 AI 工程论文（深度学习模型结构等）。

## 来源与检索
- arXiv 为主（math.PR、math.ST、stat.TH、stat.ME、stat.CO、stat.AP、stat.ML、econ.EM、q-fin.*、q-bio.QM 等）。
- 非 arXiv 的合法开放全文（JSS、PLOS、BMC、Biometrika/JRSS 的 OA 文章、PMC 开放获取全文、会议官方开放 PDF 等）可以收，写 `pdf_url` 等字段（见下）。不绕过付费墙、登录或访问限制。
- 步骤：
  1. 写检索式 `scripts/seeds/queries/NN_en.json`：列表，元素 `{"q": "<arXiv search_query>", "subtopic": "<中文子主题>"}`，覆盖本群全部子主题，一般 12–20 条。语法示例：`ti:survey AND abs:"stochastic differential equations"`，`(ti:tutorial OR ti:review OR ti:introduction OR ti:"lecture notes") AND abs:"empirical process"`，`abs:"conformal prediction" AND cat:stat.ME`。日期窗口由脚本自动追加；检索经典（不加窗口）写 `"old": true`。
  2. `python3 -I scripts/papers_en.py search NN`（走共享限速锁，arXiv 每 5 秒一个请求，多个会话共用，要耐心；429 会自动退避）。
  3. 浏览：`python3 -I scripts/papers_en.py show NN --abs 300`（只列窗口内；`--all` 含窗口外）。确知的重要论文可直接加 arXiv ID：先 `python3 -I scripts/papers_en.py meta ID1 ID2 ...` 取官方元数据，**以返回的标题、日期为准**，不要凭记忆填标题或日期。
  4. 写种子 `scripts/seeds/papers/NN_<slug>_seed_cn.json`（slug 见下表），JSON 列表，**顺序 = 建议阅读顺序**（先综述/教程，再代表性研究，再前沿专题）。字段：
     - `arxiv`：arXiv ID（不带版本号）。非 arXiv 的开放 PDF 改填 `pdf_url`、`title`、`authors`（列表）、`date`（首次公开 YYYY-MM-DD）、`date_basis`、`venue`、`doi`、`landing`。
     - `subtopic`：中文子主题。
     - `type`：`综述` / `学术教程` / `原始研究论文` / `方法与软件` / `立场与方法论` 之一。
     - `level`：`硕士` / `博士` / `硕士/博士`。
     - `track`：`理论` / `应用` / `计算` / `理论+应用` 之一。
     - `difficulty`：`入门` / `中级` / `高级`。
     - `reason`：选入理由（中文 1 句，说明在课程学习中的用途）。
     - `summary`：简介（中文 2–3 句，**只依据摘要**，用"作者称/摘要称"等措辞，不声称读过全文，不编造数字）。
     - `summary_basis`：固定写 `arXiv 摘要；未读全文`（非 arXiv 写 `出版方摘要；未读全文`）。
     - `classic_reason`：仅三年前条目需要。
     - `reserve`：后备条目写 `true`。
     - 可选 `related`：相关课程群编号列表，如 `["08","12"]`。
  5. `python3 -I scripts/papers_en.py check NN`，直到 `problems 0`。`CLAIMED-BY-xx` 表示编号更小的群已收录该论文（本群不计数），请换一篇避免跨群重复。
  6. **不要运行 download**（主会话集中下载）。不要改 `scripts/*.py`、其他群的种子、兄弟库目录。

## 课程群（编号 / slug / 范围）
| 编号 | slug | 范围 |
|---|---|---|
| 04 | advanced_probability | 测度化概率、条件期望、收敛、特征函数、弱收敛、极限定理、集中不等式、大偏差、Stein 方法、耦合 |
| 05 | stochastic_processes | 马尔可夫链与过程、混合时间、泊松与点过程、更新过程、鞅、布朗运动、平稳过程、遍历性、排队 |
| 06 | stochastic_analysis_topics | 随机积分、SDE、扩散、随机控制、粗糙路径、SPDE、随机矩阵、随机图、渗流、交互粒子系统、最优传输与概率等博士专题 |
| 07 | mathematical_statistics | 充分性、估计、置信区间、假设检验、似然、决策理论、贝叶斯基础、e-value/任意时刻有效推断、多重检验基础、选择后推断基础 |
| 08 | asymptotic_statistics_theory | 渐近分布、LAN、效率、极小极大、经验过程、非参数收敛率、信息论下界、半参数效率理论 |
| 09 | regression_linear_models | 最小二乘、方差分析、GLM、混合效应、模型诊断、模型选择、分位数回归、预测区间 |
| 10 | multivariate_highdim_learning | 多元分析、PCA/因子分析、协方差估计、稀疏与正则化、高维推断、统计学习理论、共形预测 |
| 11 | bayesian_statistics | 层级模型、先验、后验预测检验、模型比较、贝叶斯工作流、非参数贝叶斯、后验收缩理论 |
| 12 | nonparametric_robust | 核方法、样条、秩方法、稳健估计、影响函数、半参数效率、缺失数据与多重插补 |
| 13 | time_series_spatial | ARIMA、谱分析、状态空间与滤波、多元时间序列、空间过程、时空建模、函数型数据 |
| 14 | design_survey_causal | 随机化、区组、析因设计、序贯/自适应实验、抽样与权重、调查误差、因果识别、观察研究、准实验（DiD、RD、合成控制、IV） |
| 15 | biostatistics_public_health | 生存分析、纵向数据、临床试验（含适应性设计、估计目标 estimand）、流行病学、诊断试验、多重检验、真实世界证据 |
| 16 | econ_finance_insurance_risk | 计量经济学、面板数据、金融时间序列与波动率、风险度量、精算统计、极值统计 |
| 17 | industrial_environment_applied | 统计过程控制、可靠性、退化建模、环境统计、水文频率分析、能源与交通统计、农业试验、官方统计 |
| 18 | statistical_computing | 数值方法、Monte Carlo、MCMC（HMC 等）、SMC、重要性采样、Bootstrap、EM、变分推断、可扩展计算 |
| 20 | research_methods_practice | 估计目标定义、模拟研究方法学（ADEMP 等）、可复现性、敏感性分析、多元分析流程（multiverse）、预注册、统计报告规范、研究伦理、统计咨询 |
（01–03、19 以教材为主，本轮不设论文目标。）

## 回报（给主会话）
每群一行：种子总数、主列表数、后备数、主列表三年前条数、`check` 的 problems 数；缺口文件路径（若有）；需要主会话注意的问题。不要贴种子全文。
