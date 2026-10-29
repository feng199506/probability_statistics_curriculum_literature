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
| 01 数学基础 | 本科（先修） | 先修 | 无 | 〔COUNT:books:01〕 | 〔COUNT:courses:01〕 | 〔COUNT:practice:01〕 | 不设 |
| 02 高阶数学工具 | 本科高年级/硕士 | 理论方向核心/选修 | 01 | 〔COUNT:books:02〕 | 〔COUNT:courses:02〕 | 〔COUNT:practice:02〕 | 不设 |
| 03 基础概率论 | 本科 | 核心 | 01 | 〔COUNT:books:03〕 | 〔COUNT:courses:03〕 | 〔COUNT:practice:03〕 | 不设 |
| 04 高等概率论 | 硕士/博士（英国本科 Part II 已见） | 博士核心（资格考试） | 02、03 | 〔COUNT:books:04〕 | 〔COUNT:courses:04〕 | 〔COUNT:practice:04〕 | 〔COUNT:papers:04〕 |
| 05 随机过程 | 本科高年级/硕士 | 核心（部分项目）/选修 | 03 | 〔COUNT:books:05〕 | 〔COUNT:courses:05〕 | 〔COUNT:practice:05〕 | 〔COUNT:papers:05〕 |
| 06 随机分析及概率专题 | 博士 | 选修（博士专题） | 04、05 | 〔COUNT:books:06〕 | 〔COUNT:courses:06〕 | 〔COUNT:practice:06〕 | 〔COUNT:papers:06〕 |
| 07 数理统计与统计决策 | 本科高年级/硕士 | 核心 | 03 | 〔COUNT:books:07〕 | 〔COUNT:courses:07〕 | 〔COUNT:practice:07〕 | 〔COUNT:papers:07〕 |
| 08 渐近统计与理论专题 | 博士（资格考试） | 博士核心（资格考试） | 04、07 | 〔COUNT:books:08〕 | 〔COUNT:courses:08〕 | 〔COUNT:practice:08〕 | 〔COUNT:papers:08〕 |
| 09 回归与线性模型 | 本科/硕士 | 核心 | 07、01（线性代数） | 〔COUNT:books:09〕 | 〔COUNT:courses:09〕 | 〔COUNT:practice:09〕 | 〔COUNT:papers:09〕 |
| 10 多元、高维与统计学习 | 硕士/博士 | 核心/选修 | 09、01 | 〔COUNT:books:10〕 | 〔COUNT:courses:10〕 | 〔COUNT:practice:10〕 | 〔COUNT:papers:10〕 |
| 11 贝叶斯统计 | 本科高年级/硕士/博士 | 多为选修 | 07 | 〔COUNT:books:11〕 | 〔COUNT:courses:11〕 | 〔COUNT:practice:11〕 | 〔COUNT:papers:11〕 |
| 12 非参数、半参数与稳健统计 | 硕士/博士 | 选修 | 07、08 | 〔COUNT:books:12〕 | 〔COUNT:courses:12〕 | 〔COUNT:practice:12〕 | 〔COUNT:papers:12〕 |
| 13 时间序列与空间统计 | 本科高年级/硕士 | 选修 | 09、05 | 〔COUNT:books:13〕 | 〔COUNT:courses:13〕 | 〔COUNT:practice:13〕 | 〔COUNT:papers:13〕 |
| 14 实验设计、调查抽样与因果推断 | 本科高年级/硕士/博士 | 核心（应用）/选修 | 07、09 | 〔COUNT:books:14〕 | 〔COUNT:courses:14〕 | 〔COUNT:practice:14〕 | 〔COUNT:papers:14〕 |
| 15 生物统计与公共卫生 | 硕士/博士 | 专业方向 | 09、14 | 〔COUNT:books:15〕 | 〔COUNT:courses:15〕 | 〔COUNT:practice:15〕 | 〔COUNT:papers:15〕 |
| 16 经济、金融、保险与风险 | 硕士/博士 | 专业方向 | 05、09、13 | 〔COUNT:books:16〕 | 〔COUNT:courses:16〕 | 〔COUNT:practice:16〕 | 〔COUNT:papers:16〕 |
| 17 工业、环境与其他专业应用 | 本科高年级/硕士 | 专业方向 | 09、13 | 〔COUNT:books:17〕 | 〔COUNT:courses:17〕 | 〔COUNT:practice:17〕 | 〔COUNT:papers:17〕 |
| 18 统计计算与数据科学 | 本科高年级/硕士/博士 | 核心 | 19、01 | 〔COUNT:books:18〕 | 〔COUNT:courses:18〕 | 〔COUNT:practice:18〕 | 〔COUNT:papers:18〕 |
| 19 统计编程与分析工程 | 本科/硕士 | 核心技能 | 无 | 〔COUNT:books:19〕 | 〔COUNT:courses:19〕 | 〔COUNT:practice:19〕 | 不设 |
| 20 研究方法与实战 | 硕士/博士 | 论文/项目 | 07、09、18 | 〔COUNT:books:20〕 | 〔COUNT:courses:20〕 | 〔COUNT:practice:20〕 | 〔COUNT:papers:20〕 |

## 培养方案中的共同规律（依据 P 编号方案原文）
- 博士资格考试稳定覆盖三块：概率（04）、理论统计（07→08）、应用/回归（09）；清华（P-21）另将高等统计计算（18）列入资格考试。
- 测度论概率在英国本科（P-16 Part II Probability and Measure）即出现，在美/中多为研究生核心。
- 贝叶斯（11）、非参数（12）、时间序列（13）在多数方案中是选修；清华本科（P-20）把贝叶斯导论与实验设计列为专业课。
- 生物统计（15）有独立学位体系（P-05、P-06、P-12、P-13、P-25），核心为回归/推断/流行病学，生存与纵向数据为常见选修。

## 培养方案文件
- 〔P-01〕
- 〔P-02〕
- 〔P-03〕
- 〔P-04〕
- 〔P-05〕
- 〔P-06〕
- 〔P-07〕
- 〔P-08〕
- 〔P-09〕
- 〔P-10〕
- 〔P-11〕
- 〔P-12〕
- 〔P-13〕
- 〔P-14〕
- 〔P-15〕
- 〔P-16〕
- 〔P-17〕
- 〔P-18〕
- 〔P-19〕
- 〔P-20〕
- 〔P-21〕
- 〔P-22〕
- 〔P-23〕
- 〔P-24〕
- 〔P-25〕
