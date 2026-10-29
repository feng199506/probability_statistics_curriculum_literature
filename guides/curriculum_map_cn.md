# 课程关系与先修顺序

> 层次与核心/选修属性依据 `curricula/` 中 25 份官方培养方案（逐群依据与课程代码见 `scripts/annotations/curricula_level_map_cn.md`）。这些是课程群，不声称每所学校都全部开设。资料数为本库已核验、按主课程群计数（跨群资料只在主群计一次，通过"关联课程群"列引用）。

## 先修关系图（箭头表示"先修"）

```
01 数学基础 ──► 02 高阶数学工具 ──► 04 高等概率论 ──► 06 随机分析及专题
   │                                   ▲  │
   └──► 03 基础概率论 ──► 05 随机过程 ──┘  └──► 08 渐近统计与理论
             │                                   ▲
             └──► 07 数理统计与决策 ─────────────┘
                     │
                     ├──► 09 回归与线性模型 ──► 10 多元/高维/学习 ──► 12 非参数/半参数/稳健
                     ├──► 11 贝叶斯统计
                     └──► 14 实验/调查/因果 ──► 15 生物统计、16 经济金融、17 工业环境
   09 + 05 ──► 13 时间序列与空间 ──► 16、17
19 统计编程 ──► 18 统计计算 ──► 11、10 的计算部分
07 + 09 + 18 ──► 20 研究方法与实战（贯穿硕博论文阶段）
```

## 各课程群层次、属性与资料数

| 课程群 | 层次（方案依据） | 属性 | 先修群 | 教材 | 课程 | 实践 | 论文 |
|---|---|---|---|---|---|---|---|
| 01 数学基础 | 本科（先修） | 先修 | 无 | 5 | 3 | 2 | 不设 |
| 02 高阶数学工具 | 本科高年级/硕士 | 理论方向核心/选修 | 01 | 4 | 3 | 2 | 不设 |
| 03 基础概率论 | 本科 | 核心 | 01 | 3 | 3 | 3 | 不设 |
| 04 高等概率论 | 硕士/博士（英国本科 Part II 已见） | 博士核心（资格考试） | 02、03 | 3 | 4 | 2 | 40 |
| 05 随机过程 | 本科高年级/硕士 | 核心（部分项目）/选修 | 03 | 4 | 3 | 2 | 41 |
| 06 随机分析及概率专题 | 博士 | 选修（博士专题） | 04、05 | 5 | 3 | 2 | 40 |
| 07 数理统计与统计决策 | 本科高年级/硕士 | 核心 | 03 | 2 | 4 | 2 | 42 |
| 08 渐近统计与理论专题 | 博士（资格考试） | 博士核心（资格考试） | 04、07 | 3 | 3 | 2 | 40 |
| 09 回归与线性模型 | 本科/硕士 | 核心 | 07、01（线性代数） | 3 | 2 | 2 | 40 |
| 10 多元、高维与统计学习 | 硕士/博士 | 核心/选修 | 09、01 | 5 | 2 | 2 | 40 |
| 11 贝叶斯统计 | 本科高年级/硕士/博士 | 多为选修 | 07 | 4 | 2 | 3 | 42 |
| 12 非参数、半参数与稳健统计 | 硕士/博士 | 选修 | 07、08 | 3 | 3 | 3 | 40 |
| 13 时间序列与空间统计 | 本科高年级/硕士 | 选修 | 09、05 | 4 | 3 | 3 | 42 |
| 14 实验设计、调查抽样与因果推断 | 本科高年级/硕士/博士 | 核心（应用）/选修 | 07、09 | 5 | 2 | 2 | 40 |
| 15 生物统计与公共卫生 | 硕士/博士 | 专业方向 | 09、14 | 3 | 3 | 3 | 41 |
| 16 经济、金融、保险与风险 | 硕士/博士 | 专业方向 | 05、09、13 | 3 | 3 | 2 | 40 |
| 17 工业、环境与其他专业应用 | 本科高年级/硕士 | 专业方向 | 09、13 | 4 | 3 | 2 | 42 |
| 18 统计计算与数据科学 | 本科高年级/硕士/博士 | 核心 | 19、01 | 4 | 3 | 3 | 42 |
| 19 统计编程与分析工程 | 本科/硕士 | 核心技能 | 无 | 4 | 3 | 5 | 不设 |
| 20 研究方法与实战 | 硕士/博士 | 论文/项目 | 07、09、18 | 3 | 2 | 3 | 40 |

## 培养方案中的共同规律（依据 P 编号方案原文）
- 博士资格考试稳定覆盖三块：概率（04）、理论统计（07→08）、应用/回归（09）；清华（P-21）另将高等统计计算（18）列入资格考试。
- 测度论概率在英国本科（P-16 Part II Probability and Measure）即出现，在美/中多为研究生核心。
- 贝叶斯（11）、非参数（12）、时间序列（13）在多数方案中是选修；清华本科（P-20）把贝叶斯导论与实验设计列为专业课。
- 生物统计（15）有独立学位体系（P-05、P-06、P-12、P-13、P-25），核心为回归/推断/流行病学，生存与纵向数据为常见选修。

## 培养方案文件
- P-01《Statistics PhD (Doctoral Program)》（博士 / 兼顾；[curricula/Stanford_Statistics_PhD_Requirements_html_en](../curricula/Stanford_Statistics_PhD_Requirements_html_en)）
- P-02《M.S. in Statistics; M.S. in Statistics – Data Science track》（硕士 / 兼顾；[curricula/Stanford_Statistics_MS_Requirements_html_en](../curricula/Stanford_Statistics_MS_Requirements_html_en)）
- P-03《Statistics Major (B.A.)》（本科 / 兼顾；[curricula/UCBerkeley_Statistics_Major_BA_Requirements_html_en](../curricula/UCBerkeley_Statistics_Major_BA_Requirements_html_en)）
- P-04《Ph.D. in Statistics》（博士 / 兼顾；[curricula/UCBerkeley_Statistics_PhD_Program_html_en](../curricula/UCBerkeley_Statistics_PhD_Program_html_en)）
- P-05《PhD in Biostatistics》（博士 / 兼顾；[curricula/Harvard_Biostatistics_PhD_Program_html_en](../curricula/Harvard_Biostatistics_PhD_Program_html_en)）
- P-06《Master of Science (SM) in Biostatistics》（硕士 / 兼顾；[curricula/Harvard_Biostatistics_SM_Program_html_en](../curricula/Harvard_Biostatistics_SM_Program_html_en)）
- P-07《B.S. in Statistics and Data Science（含 Mathematical Sciences / Neuroscience / Machine Learning 等方向）》（本科 / 兼顾；[curricula/CMU_StatisticsDataScience_BS_Catalog_html_en](../curricula/CMU_StatisticsDataScience_BS_Catalog_html_en)）
- P-08《Ph.D. in Statistics（含 Statistics & Machine Learning 等联合项目）》（博士 / 兼顾；[curricula/CMU_Statistics_PhD_Core_html_en](../curricula/CMU_Statistics_PhD_Core_html_en)）
- P-09《B.A./B.S. in Statistics；Minor；Joint BA/MS or BS/MS》（本科 / 兼顾；[curricula/UChicago_Statistics_College_Catalog_BA_BS_html_en](../curricula/UChicago_Statistics_College_Catalog_BA_BS_html_en)）
- P-10《Ph.D. and M.S. in Statistics》（硕士/博士 / 兼顾；[curricula/UChicago_Statistics_Graduate_Announcements_PhD_MS_html_en](../curricula/UChicago_Statistics_Graduate_Announcements_PhD_MS_html_en)）
- P-11《Major / Concentration / Minor in Statistics；与 CS/Econ/Math/PoliSci 的交叉专业》（本科 / 兼顾；[curricula/Columbia_Statistics_College_Bulletin_Major_html_en](../curricula/Columbia_Statistics_College_Bulletin_Major_html_en)）
- P-12《PhD in Biostatistics》（博士 / 兼顾；[curricula/UW_Biostatistics_PhD_Requirements_html_en](../curricula/UW_Biostatistics_PhD_Requirements_html_en)）
- P-13《MS in Biostatistics (Thesis track)》（硕士 / 兼顾；[curricula/UW_Biostatistics_MS_Thesis_Requirements_html_en](../curricula/UW_Biostatistics_MS_Thesis_Requirements_html_en)）
- P-14《BA/MMath Mathematics and Statistics（本科手册 + Part A/B/C 课程大纲补充）》（本科/硕士（Part C 为第四年 MMath） / 兼顾；[curricula/Oxford_MathematicsStatistics_BA_MMath_Handbook_Synopses_en/01_Maths_and_Stats_UG_Handbook_2025-26_en.pdf](../curricula/Oxford_MathematicsStatistics_BA_MMath_Handbook_Synopses_en/01_Maths_and_Stats_UG_Handbook_2025-26_en.pdf) 等 4 项）
- P-15《MSc / PGDip in Statistical Science》（硕士 / 兼顾；[curricula/Oxford_MSc_StatisticalScience_Handbook_2026-27_en.pdf](../curricula/Oxford_MSc_StatisticalScience_Handbook_2026-27_en.pdf)）
- P-16《Mathematical Tripos Parts IA, IB, II — Schedules of Lecture Courses and Form of Examinations》（本科 / 兼顾；[curricula/Cambridge_MathematicalTripos_Schedules_2026-27_en.pdf](../curricula/Cambridge_MathematicalTripos_Schedules_2026-27_en.pdf)）
- P-17《Part III Guide to Courses — Probability and Statistics sections（含统计先修说明 Statsprereq）》（硕士 / 兼顾；[curricula/Cambridge_PartIII_GuideToCourses_ProbabilityStatistics_en/01_Advanced_Probability_en.pdf](../curricula/Cambridge_PartIII_GuideToCourses_ProbabilityStatistics_en/01_Advanced_Probability_en.pdf) 等 15 项）
- P-18《Master of Science ETH in Statistics》（硕士 / 兼顾；[curricula/ETHZ_MSc_Statistics_StudyGuide_html_en](../curricula/ETHZ_MSc_Statistics_StudyGuide_html_en)）
- P-19《MSc in Statistics（含 with Finance / with Probability / Data Science 等路径）》（硕士 / 兼顾；[curricula/Warwick_MSc_Statistics_Course_html_en](../curricula/Warwick_MSc_Statistics_Course_html_en)）
- P-20《清华大学统计与数据科学系 统计学专业本科培养方案》（本科 / 兼顾；[curricula/Tsinghua_Statistics_BS_Program_Plan_cn.pdf](../curricula/Tsinghua_Statistics_BS_Program_Plan_cn.pdf)）
- P-21《清华大学统计与数据科学系 博士研究生培养方案 统计学（适用于 2025 级）》（博士 / 兼顾；[curricula/Tsinghua_Statistics_PhD_Program_Plan_2025_cn.pdf](../curricula/Tsinghua_Statistics_PhD_Program_Plan_2025_cn.pdf)）
- P-22《北京大学数学科学学院本科生教学手册（2023 年 7 月修订）》（本科 / 兼顾；[curricula/PKU_SMS_Undergraduate_Handbook_2023_incl_Statistics_cn.pdf](../curricula/PKU_SMS_Undergraduate_Handbook_2023_incl_Statistics_cn.pdf)）
- P-23《中国科学技术大学 统计学学科研究生培养方案（2025 版）：硕士、普通招考博士、硕博一体化博士》（硕士/博士 / 兼顾；[curricula/USTC_Statistics_Graduate_Program_Plans_2025_cn/01_1758537318823-948976_cn.pdf](../curricula/USTC_Statistics_Graduate_Program_Plans_2025_cn/01_1758537318823-948976_cn.pdf) 等 3 项）
- P-24《中山大学 统计学（071400）学术学位硕士、博士研究生培养方案（2024 年级起执行）》（硕士/博士 / 兼顾；[curricula/SYSU_Statistics_Graduate_Program_Plans_2024_cn/01_2024_071400_cn.pdf](../curricula/SYSU_Statistics_Graduate_Program_Plans_2024_cn/01_2024_071400_cn.pdf) 等 2 项）
- P-25《中国人民大学统计学院 2024 级研究生培养方案（直博-统计学理学、流行病与卫生统计学硕士）》（硕士/博士 / 兼顾；[curricula/RUC_Statistics_Graduate_Program_Plans_2024_cn/01_63431393d70248cd98cd7fed5440d67a_cn.pdf](../curricula/RUC_Statistics_Graduate_Program_Plans_2024_cn/01_63431393d70248cd98cd7fed5440d67a_cn.pdf) 等 2 项）
