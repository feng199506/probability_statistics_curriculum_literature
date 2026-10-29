# 检索日志

检索日：2026-10-29；论文近三年窗口：首次公开 2023-10-29 至 2026-10-29。
论文检索走 arXiv API（检索式见下，日期窗口由脚本追加；标 old 的为经典检索不加窗口），候选经人工筛选写入种子，非 arXiv 开放全文（出版方/PMC/JSS 等）由人工核对后加入。教材、课程、实践、案例、软件文档与培养方案通过官方页面人工检索，来源 URL 记录在 catalog_cn.csv 与 download_failures_cn.csv。


## 04 高等概率论

候选 519 条 → 种子 48 条（主列表 41，后备 7）→ 核验通过 40 条。

| 子主题 | 检索式 |
|---|---|
| 集中不等式 | `(ti:survey OR ti:review OR ti:introduction OR ti:"lecture notes" OR ti:tutorial) AND abs:"concentration inequalities"` |
| 集中不等式 | `abs:"concentration of measure" AND cat:math.PR AND (ti:survey OR ti:notes OR ti:introduction OR ti:inequalities)` |
| 大偏差 | `(ti:survey OR ti:review OR ti:introduction OR ti:"lecture notes" OR ti:tutorial) AND abs:"large deviations"` |
| 大偏差 | `ti:"large deviation" AND cat:math.PR` |
| Stein 方法 | `(ti:survey OR ti:review OR ti:introduction OR ti:"lecture notes" OR ti:tutorial) AND abs:"Stein's method"` |
| Stein 方法 | `ti:"Stein's method" AND cat:math.PR` |
| 耦合 | `(ti:survey OR ti:review OR ti:introduction OR ti:"lecture notes" OR ti:tutorial) AND abs:coupling AND cat:math.PR` |
| 极限定理与收敛速率 | `(ti:"central limit theorem" OR ti:"Berry-Esseen") AND cat:math.PR` |
| 极限定理与收敛速率 | `(ti:survey OR ti:review OR ti:introduction OR ti:"lecture notes") AND abs:"limit theorems" AND cat:math.PR` |
| 弱收敛与概率距离 | `(ti:"weak convergence" OR ti:"convergence in distribution" OR ti:"Wasserstein distance" OR ti:"probability metrics") AND cat:math.PR` |
| 特征函数 | `(ti:"characteristic function" OR ti:"characteristic functions" OR ti:"Fourier analysis") AND cat:math.PR` |
| 测度论概率与条件期望 | `(ti:"conditional expectation" OR ti:"regular conditional" OR ti:disintegration OR ti:"measure-theoretic") AND (cat:math.PR OR cat:math.ST)` |
| 大数定律 | `(ti:"law of large numbers" OR ti:"strong law" OR ti:"laws of large numbers") AND cat:math.PR` |
| Stein 方法 | `(ti:"Malliavin" AND ti:"Stein") OR (ti:"fourth moment" AND cat:math.PR)` |
| 集中不等式 | `(ti:inequality OR ti:inequalities) AND (abs:"sub-Gaussian" OR abs:"martingale" OR abs:"log-Sobolev" OR abs:"Poincare") AND cat:math.PR` |
| 极限定理与收敛速率 | `(ti:"heavy tails" OR ti:"heavy-tailed" OR ti:"stable laws" OR ti:"infinitely divisible") AND cat:math.PR AND (ti:survey OR ti:introduction OR ti:review OR abs:survey)` |
| 综述总览 | `ti:survey AND cat:math.PR AND abs:probability` |
| 经典综述 | `(ti:"Stein's method" OR ti:"concentration inequalities" OR ti:"large deviations") AND (ti:introduction OR ti:survey)`（经典，不限日期） |
| 经典综述 | `(ti:coupling AND ti:"lecture notes") OR (ti:"concentration of measure" AND ti:survey)`（经典，不限日期） |
| 讲义总览 | `co:"lecture notes" AND cat:math.PR` |
| 综述总览 | `(jr:"Probability Surveys" OR jr:"Probab. Surv" OR jr:"Probab. Surveys") AND cat:math.PR` |
| Stein 方法 | `abs:"Stein's method" AND (abs:survey OR abs:"we review" OR abs:overview OR abs:expository OR abs:"these notes")` |
| 集中不等式 | `abs:concentration AND (abs:"we survey" OR abs:"this survey" OR abs:"these notes" OR abs:"lecture notes" OR abs:expository) AND cat:math.PR` |
| 大偏差 | `abs:"large deviations" AND (abs:"these notes" OR abs:"lecture notes" OR abs:"we review" OR abs:survey OR abs:expository) AND cat:math.PR` |
| 耦合 | `abs:coupling AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository) AND cat:math.PR` |
| 极限定理与收敛速率 | `abs:"central limit theorem" AND (abs:survey OR abs:"we review" OR abs:"these notes" OR abs:expository) AND cat:math.PR` |
| 弱收敛与概率距离 | `(abs:Wasserstein OR abs:"weak convergence" OR abs:"total variation") AND (abs:survey OR abs:expository OR abs:"these notes" OR abs:"we review") AND cat:math.PR` |
| 集中不等式 | `(abs:"high-dimensional probability" OR ti:"high-dimensional probability") AND (abs:notes OR abs:survey OR abs:introduction OR abs:course)` |
| 综述总览 | `abs:expository AND cat:math.PR AND (abs:probability OR abs:random)` |
| 测度论概率与条件期望 | `(abs:"de Finetti" OR abs:exchangeability OR abs:"conditional expectation" OR abs:"regular conditional") AND (abs:survey OR abs:expository OR abs:"we review" OR abs:tutorial) AND (cat:math.PR OR cat:math.ST)` |
| 集中不等式 | `(abs:"log-Sobolev" OR abs:"Poincare inequality" OR abs:"functional inequalities" OR abs:"transport inequalities") AND (abs:survey OR abs:"these notes" OR abs:"lecture notes" OR abs:"we review")` |

## 05 随机过程

候选 598 条 → 种子 48 条（主列表 41，后备 7）→ 核验通过 41 条。

| 子主题 | 检索式 |
|---|---|
| 马尔可夫链 | `(ti:survey OR ti:review OR ti:introduction OR ti:"lecture notes" OR ti:tutorial) AND abs:"Markov chains" AND cat:math.PR` |
| 混合时间 | `(ti:"mixing time" OR ti:"mixing times" OR ti:cutoff) AND cat:math.PR` |
| 混合时间 | `(ti:survey OR ti:review OR ti:introduction OR ti:"lecture notes") AND abs:"mixing times"` |
| 泊松与点过程 | `(ti:"point process" OR ti:"point processes" OR ti:"Poisson process") AND (ti:survey OR ti:review OR ti:introduction OR ti:tutorial OR ti:"lecture notes")` |
| 泊松与点过程 | `(ti:"Hawkes process" OR ti:"Hawkes processes" OR ti:"Cox process" OR ti:"determinantal point") AND (ti:review OR ti:survey OR ti:tutorial OR ti:introduction)` |
| 更新过程 | `(ti:renewal OR ti:"regenerative") AND cat:math.PR` |
| 鞅 | `(ti:martingale OR ti:martingales) AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes" OR ti:tutorial)` |
| 鞅 | `ti:martingale AND cat:math.PR AND (abs:"optional stopping" OR abs:"convergence theorem" OR abs:"maximal inequality")` |
| 布朗运动 | `(ti:"Brownian motion") AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes" OR ti:primer)` |
| 布朗运动 | `ti:"Brownian motion" AND cat:math.PR` |
| 平稳过程 | `(ti:"stationary process" OR ti:"stationary processes" OR ti:"stationary sequences" OR ti:"Gaussian processes") AND cat:math.PR` |
| 遍历性 | `(ti:ergodic OR ti:ergodicity) AND (abs:"Markov" OR abs:"stationary") AND (ti:survey OR ti:introduction OR ti:review OR ti:tutorial OR ti:notes)` |
| 遍历性 | `(ti:ergodicity OR ti:"convergence to equilibrium" OR ti:"Lyapunov") AND abs:"Markov process" AND cat:math.PR` |
| 排队论 | `(ti:queue OR ti:queueing OR ti:queues) AND (ti:survey OR ti:review OR ti:tutorial OR ti:introduction)` |
| 排队论 | `(ti:queue OR ti:queueing) AND cat:math.PR AND (abs:"heavy traffic" OR abs:"fluid limit" OR abs:"diffusion approximation")` |
| 连续时间马尔可夫过程与分支过程 | `(ti:"continuous-time Markov" OR ti:"birth-death" OR ti:"jump process" OR ti:"branching process" OR ti:"branching processes") AND (ti:survey OR ti:review OR ti:introduction OR ti:tutorial)` |
| 随机游走 | `(ti:"random walk" OR ti:"random walks") AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes")` |
| 混合时间 | `(ti:"Markov chain" OR ti:"Markov chains") AND (abs:"spectral gap" OR abs:"hitting time" OR abs:"total variation") AND cat:math.PR` |
| 经典综述 | `(ti:"mixing times" OR ti:"Markov chains" OR ti:"point processes" OR ti:"Brownian motion") AND (ti:survey OR ti:introduction OR ti:"lecture notes")`（经典，不限日期） |
| 讲义总览 | `co:"lecture notes" AND (abs:"Markov chain" OR abs:"Markov chains" OR abs:"Markov process" OR abs:martingale OR abs:"Brownian motion" OR abs:"point process" OR abs:queue OR abs:"random walk")` |
| 马尔可夫链 | `(abs:"Markov chain" OR abs:"Markov chains") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository OR abs:tutorial) AND cat:math.PR` |
| 混合时间 | `(abs:"mixing time" OR abs:cutoff OR abs:"spectral gap") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository) AND cat:math.PR` |
| 泊松与点过程 | `(abs:"point process" OR abs:"point processes" OR abs:"Poisson process") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository OR abs:tutorial) AND (cat:math.PR OR cat:stat.ME OR cat:stat.TH)` |
| 鞅 | `(abs:martingale OR abs:martingales) AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository OR abs:tutorial) AND (cat:math.PR OR cat:math.ST)` |
| 布朗运动 | `(abs:"Brownian motion") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository) AND cat:math.PR` |
| 排队论 | `(abs:queue OR abs:queueing OR abs:"queueing network") AND (abs:survey OR abs:"we review" OR abs:tutorial OR abs:"these notes") AND (cat:math.PR OR cat:math.OC OR cat:cs.PF)` |
| 遍历性 | `(abs:ergodic OR abs:ergodicity OR abs:"Harris recurrence" OR abs:"Lyapunov function") AND abs:"Markov" AND (abs:survey OR abs:"these notes" OR abs:"we review" OR abs:expository OR abs:tutorial)` |
| 平稳过程 | `(abs:"stationary process" OR abs:"stationary processes" OR abs:"Gaussian process" OR abs:"long-range dependence") AND (abs:survey OR abs:"we review" OR abs:"these notes" OR abs:expository) AND cat:math.PR` |
| 连续时间马尔可夫过程与分支过程 | `(abs:"branching process" OR abs:"branching processes" OR abs:"Galton-Watson" OR abs:"random walk in random environment") AND (abs:survey OR abs:"we review" OR abs:"these notes" OR abs:expository)` |
| 综述总览 | `(jr:"Probability Surveys" OR jr:"Probab. Surv") AND (abs:Markov OR abs:martingale OR abs:process)` |
| 混合时间 | `(ti:"Markov chain" OR ti:"Markov chains" OR ti:"random walk") AND (ti:"mixing" OR ti:"cutoff" OR ti:"hitting" OR ti:"cover time") AND cat:math.PR` |
| 泊松与点过程 | `(ti:"Hawkes process" OR ti:"Hawkes processes") AND (cat:math.PR OR cat:stat.ME OR cat:stat.TH)` |
| 泊松与点过程 | `(ti:"Poisson process" OR ti:"Poisson processes" OR ti:"Poisson point process") AND cat:math.PR` |
| 连续时间马尔可夫过程与分支过程 | `(ti:"birth-death" OR ti:"birth and death" OR ti:"continuous-time Markov chain" OR ti:"continuous-time Markov chains") AND cat:math.PR` |

## 06 随机分析及概率专题

候选 410 条 → 种子 47 条（主列表 40，后备 7）→ 核验通过 40 条。

| 子主题 | 检索式 |
|---|---|
| 随机积分与 SDE | `(ti:survey OR ti:review OR ti:introduction OR ti:"lecture notes" OR ti:tutorial OR ti:primer) AND abs:"stochastic differential equations"` |
| 随机积分与 SDE | `(ti:"stochastic calculus" OR ti:"stochastic integration" OR ti:"Ito calculus" OR ti:"stochastic integral") AND (cat:math.PR OR cat:q-fin.MF)` |
| 扩散过程 | `(ti:diffusion OR ti:diffusions OR ti:Langevin) AND cat:math.PR AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes" OR ti:tutorial)` |
| 扩散过程 | `(ti:"diffusion models" OR ti:"score-based") AND (ti:tutorial OR ti:survey OR ti:review OR ti:primer) AND (cat:math.PR OR cat:stat.ML OR cat:math.ST)` |
| 随机控制与平均场 | `(ti:"stochastic control" OR ti:"optimal control" OR ti:"mean field games" OR ti:"mean-field games") AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes" OR ti:tutorial)` |
| 粗糙路径 | `(ti:"rough paths" OR ti:"rough path" OR ti:signature OR ti:"regularity structures") AND (ti:survey OR ti:introduction OR ti:primer OR ti:review OR ti:"lecture notes" OR ti:course)` |
| SPDE | `(ti:"stochastic partial differential" OR ti:SPDE OR ti:SPDEs OR ti:KPZ) AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes")` |
| 随机矩阵 | `(ti:"random matrix" OR ti:"random matrices") AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes" OR ti:tutorial)` |
| 随机图 | `(ti:"random graph" OR ti:"random graphs" OR ti:"random networks") AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes")` |
| 渗流 | `(ti:percolation) AND cat:math.PR AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes" OR abs:survey)` |
| 交互粒子系统 | `(ti:"interacting particle" OR ti:"exclusion process" OR ti:"particle systems" OR ti:"contact process" OR ti:"hydrodynamic limit") AND cat:math.PR` |
| 最优传输与概率 | `(ti:"optimal transport" OR ti:Wasserstein OR ti:"Schrodinger bridge" OR ti:"Schroedinger bridge") AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes" OR ti:tutorial)` |
| 最优传输与概率 | `(ti:"optimal transport" OR ti:"entropic") AND cat:math.PR` |
| 随机控制与平均场 | `(ti:"McKean-Vlasov" OR ti:"propagation of chaos" OR ti:"mean-field limit") AND (ti:survey OR ti:review OR ti:introduction OR ti:"lecture notes" OR abs:review)` |
| 高斯分析与分数布朗运动 | `(ti:"Malliavin calculus" OR ti:"fractional Brownian motion" OR ti:"Gaussian multiplicative chaos") AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes")` |
| 随机控制与平均场 | `(ti:"backward stochastic differential" OR ti:BSDE OR ti:BSDEs) AND (ti:survey OR ti:introduction OR ti:review OR ti:numerical OR ti:"deep")` |
| 随机几何与 SLE | `(ti:"Schramm-Loewner" OR ti:SLE OR ti:"Liouville quantum gravity" OR ti:"random planar maps" OR ti:"conformal invariance") AND (ti:survey OR ti:introduction OR ti:"lecture notes" OR ti:review)` |
| 统计物理中的概率 | `(ti:"spin glass" OR ti:"spin glasses" OR ti:"Ising model" OR ti:"random field") AND cat:math.PR AND (ti:survey OR ti:introduction OR ti:review OR ti:"lecture notes")` |
| 经典综述 | `(ti:"random matrices" OR ti:"rough paths" OR ti:"random graphs" OR ti:"optimal transport" OR ti:"interacting particle" OR ti:"stochastic partial") AND (ti:introduction OR ti:survey OR ti:"lecture notes" OR ti:course)`（经典，不限日期） |
| 讲义总览 | `co:"lecture notes" AND (abs:"stochastic differential" OR abs:SPDE OR abs:"random matrices" OR abs:"rough paths" OR abs:percolation OR abs:"random graphs" OR abs:"optimal transport" OR abs:"particle systems")` |
| 随机积分与 SDE | `(abs:"stochastic differential equations" OR abs:"stochastic calculus") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository OR abs:tutorial) AND cat:math.PR` |
| 随机矩阵 | `(abs:"random matrix" OR abs:"random matrices") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository) AND cat:math.PR` |
| 随机图与渗流 | `(abs:"random graph" OR abs:"random graphs" OR abs:percolation) AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository) AND cat:math.PR` |
| 最优传输与概率 | `(abs:"optimal transport" OR abs:"Schrodinger bridge" OR abs:"Schrödinger bridge") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:tutorial OR abs:expository) AND (cat:math.PR OR cat:math.OC OR cat:stat.ML)` |
| 随机控制与平均场 | `(abs:"stochastic control" OR abs:"mean field games" OR abs:"mean-field games") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:tutorial) AND (cat:math.PR OR cat:math.OC)` |
| 交互粒子系统 | `(abs:"interacting particle" OR abs:"exclusion process" OR abs:"KPZ" OR abs:"hydrodynamic limit") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository) AND cat:math.PR` |
| 粗糙路径 | `(abs:"rough paths" OR abs:"signature" OR abs:"regularity structures" OR abs:"paracontrolled") AND (abs:"these notes" OR abs:survey OR abs:"we review" OR abs:expository OR abs:introduction) AND cat:math.PR` |
| 综述总览 | `(jr:"Probability Surveys" OR jr:"Probab. Surv") AND (abs:stochastic OR abs:random)` |

## 07 数理统计与统计决策

候选 792 条 → 种子 49 条（主列表 42，后备 7）→ 核验通过 42 条。

| 子主题 | 检索式 |
|---|---|
| e-value与任意时刻有效推断 | `(ti:survey OR ti:review OR ti:tutorial OR ti:introduction OR ti:primer) AND (abs:"e-values" OR abs:"e-value" OR abs:"anytime-valid" OR abs:"safe testing")` |
| e-value与任意时刻有效推断 | `abs:"anytime-valid" AND (abs:"confidence sequence" OR abs:"sequential test") AND (cat:math.ST OR cat:stat.ME)` |
| e-value与任意时刻有效推断 | `abs:"testing by betting" OR abs:"universal inference" OR ti:"e-processes"` |
| 多重检验基础 | `(ti:review OR ti:survey OR ti:tutorial OR ti:introduction) AND (abs:"multiple testing" OR abs:"false discovery rate")` |
| 多重检验基础 | `ti:"false discovery rate" AND (cat:math.ST OR cat:stat.ME) AND abs:"Benjamini"` |
| 选择后推断基础 | `(ti:review OR ti:survey OR ti:tutorial OR ti:introduction OR ti:overview) AND (abs:"selective inference" OR abs:"post-selection inference")` |
| 选择后推断基础 | `(abs:"selective inference" OR abs:"data fission" OR abs:"data thinning") AND (cat:stat.ME OR cat:math.ST)` |
| 假设检验 | `(ti:tutorial OR ti:review OR ti:introduction OR ti:"lecture notes") AND (abs:"hypothesis testing" OR abs:"p-values") AND (cat:math.ST OR cat:stat.ME OR cat:stat.OT)` |
| 假设检验 | `(ti:"permutation test" OR ti:"permutation tests" OR ti:"randomization test") AND (cat:math.ST OR cat:stat.ME)` |
| 置信区间与区间估计 | `(ti:"confidence interval" OR ti:"confidence intervals" OR ti:"confidence distribution") AND (cat:math.ST OR cat:stat.ME)` |
| 似然推断 | `(abs:"likelihood ratio" OR abs:"likelihood principle" OR ti:likelihood) AND (ti:review OR ti:tutorial OR ti:introduction OR ti:foundations OR ti:perspective) AND (cat:math.ST OR cat:stat.ME OR cat:stat.OT)` |
| 似然推断 | `(ti:"maximum likelihood" OR ti:"likelihood ratio test" OR ti:"Wilks") AND cat:math.ST` |
| 决策理论与收缩估计 | `(ti:"decision theory" OR ti:admissibility OR ti:"Stein" OR ti:shrinkage OR ti:"empirical Bayes") AND (cat:math.ST OR cat:stat.ME)` |
| 充分性与点估计 | `(ti:"sufficient statistic" OR ti:sufficiency OR ti:"Rao-Blackwell" OR ti:"unbiased estimat" OR ti:"Cramer-Rao" OR ti:"Cramér-Rao") AND (cat:math.ST OR cat:stat.ME)` |
| 统计推断基础与哲学 | `(ti:"foundations of statistics" OR ti:"statistical inference" OR ti:fiducial OR ti:"inferential model") AND (ti:review OR ti:survey OR ti:perspective OR ti:foundations OR ti:introduction) AND (cat:math.ST OR cat:stat.ME OR cat:stat.OT)` |
| 贝叶斯基础 | `(ti:bayesian OR ti:bayes) AND (ti:foundations OR ti:introduction OR ti:primer OR ti:tutorial OR ti:"lecture notes") AND (cat:math.ST OR cat:stat.ME OR cat:stat.OT)` |
| 贝叶斯基础 | `(ti:"Bayes factor" OR ti:"Bayes factors" OR ti:"posterior predictive") AND (cat:math.ST OR cat:stat.ME)` |
| 统计推断基础与哲学 | `(ti:"lecture notes" OR ti:notes OR ti:course) AND (abs:"mathematical statistics" OR abs:"statistical inference")` |
| 经典 | `(ti:"e-values" OR ti:"safe testing" OR ti:"confidence sequences" OR ti:"universal inference" OR ti:"selective inference")`（经典，不限日期） |
| 决策理论与收缩估计 | `(ti:review OR ti:survey OR ti:overview OR ti:tutorial OR ti:introduction OR ti:perspective) AND abs:"empirical Bayes" AND (cat:math.ST OR cat:stat.ME)` |
| e-value与任意时刻有效推断 | `(ti:"e-values" OR ti:"e-value" OR ti:"e-variables") AND (cat:math.ST OR cat:stat.ME)` |
| e-value与任意时刻有效推断 | `ti:"confidence sequences" AND (cat:math.ST OR cat:stat.ME OR cat:stat.ML)` |
| 假设检验 | `(ti:"p-value" OR ti:"p-values") AND (cat:math.ST OR cat:stat.ME) AND (abs:combination OR abs:calibration OR abs:validity OR abs:evidence)` |
| 假设检验 | `(ti:"Neyman-Pearson" OR ti:"most powerful" OR ti:"uniformly most powerful") AND (cat:math.ST OR cat:stat.ME)` |
| 贝叶斯基础 | `(ti:"objective Bayes" OR ti:"reference prior" OR ti:"Jeffreys prior" OR ti:"default prior") AND (cat:math.ST OR cat:stat.ME)` |
| 决策理论与收缩估计 | `(ti:admissible OR ti:inadmissible OR ti:inadmissibility OR ti:"minimax estimation") AND cat:math.ST` |
| 充分性与点估计 | `(ti:"exponential family" OR ti:"exponential families") AND cat:math.ST AND (abs:estimation OR abs:inference)` |
| 多重检验基础 | `(ti:"multiple testing" OR ti:"multiple comparisons" OR ti:"familywise" OR ti:"closed testing") AND (cat:math.ST OR cat:stat.ME)` |
| 多重检验基础 | `(ti:"knockoff" OR ti:knockoffs) AND (ti:review OR ti:tutorial OR ti:introduction OR ti:survey OR ti:overview)` |
| 似然推断 | `(ti:"higher-order" OR ti:saddlepoint OR ti:Bartlett OR ti:"likelihood asymptotics") AND (ti:likelihood OR abs:likelihood) AND (cat:math.ST OR cat:stat.ME)` |
| 贝叶斯基础 | `(ti:"Bayesian" AND ti:"frequentist") AND (cat:math.ST OR cat:stat.ME OR cat:stat.OT)` |

## 08 渐近统计与理论专题

候选 609 条 → 种子 46 条（主列表 39，后备 7）→ 核验通过 40 条。

| 子主题 | 检索式 |
|---|---|
| 经验过程 | `(ti:"empirical process" OR ti:"empirical processes") AND (ti:introduction OR ti:notes OR ti:survey OR ti:review OR ti:tutorial OR ti:lectures)` |
| 经验过程 | `abs:"empirical process" AND (abs:"uniform" OR abs:"chaining" OR abs:"maximal inequality") AND cat:math.ST` |
| LAN与Le Cam理论 | `(abs:"local asymptotic normality" OR ti:LAN OR abs:"Le Cam") AND (cat:math.ST OR cat:math.PR)` |
| 渐近效率 | `(abs:"asymptotic efficiency" OR abs:"efficient estimator" OR abs:"Hajek" OR abs:"Hájek") AND cat:math.ST` |
| 极小极大理论 | `(ti:minimax OR abs:"minimax rate" OR abs:"minimax risk") AND (ti:survey OR ti:tutorial OR ti:introduction OR ti:review OR ti:notes OR ti:lower)` |
| 信息论下界 | `(abs:"Fano" OR abs:"Assouad" OR abs:"information-theoretic lower bound") AND (cat:math.ST OR cat:cs.IT) AND abs:minimax` |
| 非参数收敛率 | `(ti:"nonparametric" AND (ti:rate OR ti:rates OR ti:"convergence")) AND cat:math.ST` |
| 半参数效率理论 | `(abs:"semiparametric efficiency" OR abs:"efficiency bound" OR abs:"efficient influence function") AND cat:math.ST` |
| 半参数效率理论 | `(ti:semiparametric) AND (ti:review OR ti:tutorial OR ti:introduction OR ti:primer OR ti:"lecture notes" OR ti:theory)` |
| 渐近分布 | `(ti:"Bernstein-von Mises" OR ti:"Bernstein--von Mises") AND (cat:math.ST OR cat:stat.ME)` |
| 渐近分布 | `(ti:asymptotic OR ti:asymptotics) AND (ti:"maximum likelihood" OR ti:"M-estimators" OR ti:"M-estimation" OR ti:"Z-estimators") AND cat:math.ST` |
| 渐近分布 | `(ti:"high-dimensional" OR ti:"proportional asymptotics") AND (ti:"maximum likelihood" OR ti:"likelihood ratio" OR ti:"M-estimation") AND cat:math.ST` |
| 渐近分布 | `(ti:"Berry-Esseen" OR ti:"Edgeworth" OR ti:"Gaussian approximation") AND cat:math.ST` |
| 渐近分布 | `(ti:"delta method" OR ti:"functional delta" OR ti:"Hadamard" OR ti:"von Mises") AND cat:math.ST` |
| 讲义 | `(ti:"lecture notes" OR ti:lectures OR ti:"course notes") AND (abs:"asymptotic statistics" OR abs:"statistical theory" OR abs:minimax OR abs:"high-dimensional statistics")` |
| 信息论下界 | `(abs:"local differential privacy" OR abs:"communication constraints" OR abs:"privacy") AND abs:"minimax" AND abs:"lower bound" AND cat:math.ST` |
| 经典 | `(ti:"Le Cam" OR ti:"local asymptotic normality" OR ti:"empirical processes" OR ti:"minimax lower bounds" OR ti:"semiparametric efficiency")`（经典，不限日期） |
| 讲义 | `(ti:survey OR ti:review OR ti:tutorial OR ti:introduction OR ti:"lecture notes" OR ti:primer OR ti:overview) AND cat:math.ST` |
| 非参数收敛率 | `(ti:survey OR ti:review OR ti:tutorial OR ti:"lecture notes" OR ti:introduction OR ti:overview) AND (abs:"optimal transport" OR abs:"Wasserstein") AND (cat:math.ST OR cat:stat.ML)` |
| 渐近分布 | `(ti:survey OR ti:review OR ti:tutorial OR ti:introduction OR ti:overview OR ti:notes) AND (abs:"approximate message passing" OR abs:"proportional asymptotics" OR abs:"high-dimensional asymptotics" OR abs:"statistical-computational")` |
| 半参数效率理论 | `(ti:"influence function" OR abs:"pathwise derivative" OR abs:"efficient influence function") AND (ti:tutorial OR ti:introduction OR ti:primer OR ti:review OR ti:guide OR ti:calculus OR ti:"lecture notes")` |
| 渐近分布 | `(ti:"Stein's method" OR ti:"Stein method") AND (cat:math.ST OR cat:stat.ME OR cat:stat.ML)` |
| 极小极大理论 | `(ti:"minimax testing" OR ti:"goodness-of-fit testing" OR abs:"minimax separation" OR ti:"testing") AND abs:"minimax" AND abs:"separation rate" AND cat:math.ST` |
| 渐近分布 | `(ti:"U-statistics" OR ti:"U-statistic" OR ti:"V-statistics") AND cat:math.ST` |
| 渐近效率 | `(ti:"van Trees" OR ti:"Cramer-Rao" OR ti:"local minimax" OR ti:"instance-optimal" OR ti:"instance optimality") AND cat:math.ST` |
| 信息论下界 | `(ti:"differential privacy" OR ti:"differentially private") AND (ti:minimax OR ti:"lower bounds" OR ti:optimal) AND cat:math.ST` |
| 经验过程 | `(ti:"empirical process" OR ti:"empirical processes" OR ti:"uniform central limit" OR ti:"Donsker" OR ti:"VC" OR ti:"metric entropy") AND (cat:math.ST OR cat:math.PR)` |
| 渐近分布 | `(ti:"Gaussian approximation" OR ti:"bootstrap") AND ti:"high-dimensional" AND (cat:math.ST OR cat:math.PR)` |
| 讲义 | `(ti:"lecture notes" OR ti:"lectures on" OR ti:"Saint-Flour" OR ti:"St-Flour") AND (cat:math.ST OR cat:stat.ML OR cat:math.PR)` |

## 09 回归与线性模型

候选 629 条 → 种子 47 条（主列表 40，后备 7）→ 核验通过 40 条。

| 子主题 | 检索式 |
|---|---|
| 线性回归综述与教程 | `(ti:survey OR ti:review OR ti:tutorial OR ti:introduction) AND abs:"linear regression" AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST)` |
| 最小二乘理论 | `abs:"least squares" AND (abs:"high-dimensional" OR abs:overparameterized OR abs:"minimum norm") AND (cat:math.ST OR cat:stat.TH)` |
| 方差分析 | `abs:"analysis of variance" AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST)` |
| 广义线性模型 | `abs:"generalized linear models" AND (ti:review OR ti:tutorial OR ti:survey OR abs:inference) AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST)` |
| 广义线性模型 | `abs:"logistic regression" AND abs:"high-dimensional" AND (cat:math.ST OR cat:stat.TH)` |
| 混合效应模型 | `(abs:"mixed models" OR abs:"mixed-effects" OR abs:"linear mixed") AND (ti:review OR ti:tutorial OR ti:introduction OR ti:primer OR abs:inference) AND (cat:stat.ME OR cat:stat.CO OR cat:stat.AP)` |
| 混合效应模型 | `(abs:"generalized linear mixed" OR abs:"random effects") AND (cat:stat.ME OR cat:stat.TH OR cat:stat.CO)` |
| 模型诊断 | `(abs:"regression diagnostics" OR abs:"residual diagnostics" OR abs:"influential observations" OR abs:"model checking") AND (cat:stat.ME OR cat:stat.AP OR cat:stat.CO)` |
| 模型诊断与稳健标准误 | `abs:heteroskedasticity AND (abs:"robust standard errors" OR abs:"sandwich") AND (cat:stat.ME OR cat:econ.EM OR cat:math.ST)` |
| 模型选择 | `(abs:"model selection" OR abs:"variable selection") AND abs:regression AND (ti:review OR ti:survey OR ti:tutorial OR ti:comparison) AND (cat:stat.ME OR cat:stat.ML)` |
| 模型选择 | `(abs:"information criterion" OR abs:AIC OR abs:"cross-validation") AND abs:regression AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST)` |
| 分位数回归 | `abs:"quantile regression" AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST OR cat:econ.EM)` |
| 预测区间 | `abs:"prediction intervals" AND abs:regression AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST)` |
| 岭回归与收缩 | `(abs:"ridge regression" OR abs:"shrinkage") AND abs:"linear model" AND (cat:math.ST OR cat:stat.TH OR cat:stat.ME)` |
| 测量误差与回归 | `(abs:"measurement error" OR abs:"errors-in-variables") AND abs:regression AND (cat:stat.ME OR cat:stat.TH)` |
| 计数与离散响应回归 | `(abs:"count data" OR abs:"Poisson regression" OR abs:"negative binomial" OR abs:"zero-inflated") AND (ti:review OR ti:tutorial OR abs:regression) AND (cat:stat.ME OR cat:stat.AP)` |
| 广义可加与分布回归 | `(abs:"generalized additive models" OR abs:"distributional regression" OR abs:GAMLSS) AND (cat:stat.ME OR cat:stat.CO)` |
| 模型误设与稳健推断 | `(abs:"model misspecification" OR abs:"assumption-lean" OR abs:"misspecified linear") AND abs:regression AND (cat:stat.ME OR cat:math.ST OR cat:stat.TH)` |

## 10 多元、高维与统计学习

候选 565 条 → 种子 47 条（主列表 40，后备 7）→ 核验通过 40 条。

| 子主题 | 检索式 |
|---|---|
| 主成分分析 | `(ti:survey OR ti:review OR ti:tutorial OR ti:introduction) AND abs:"principal component analysis" AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST OR cat:stat.ML)` |
| 高维PCA与尖峰模型 | `abs:"principal component" AND abs:"high-dimensional" AND (abs:spiked OR abs:eigenvector) AND (cat:math.ST OR cat:stat.TH)` |
| 因子分析 | `abs:"factor model" AND abs:"high-dimensional" AND (cat:stat.ME OR cat:math.ST OR cat:econ.EM)` |
| 协方差与精度矩阵估计 | `(abs:"covariance matrix estimation" OR abs:"precision matrix" OR abs:"graphical lasso") AND (cat:math.ST OR cat:stat.TH OR cat:stat.ME)` |
| 稀疏与正则化 | `(ti:survey OR ti:review OR ti:tutorial) AND (abs:sparsity OR abs:lasso OR abs:regularization) AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST OR cat:stat.ML)` |
| 稀疏与正则化 | `abs:lasso AND (abs:"oracle inequality" OR abs:"support recovery" OR abs:"variable selection") AND (cat:math.ST OR cat:stat.TH)` |
| 高维推断 | `(abs:"debiased lasso" OR abs:"desparsified" OR abs:"high-dimensional inference" OR abs:"post-selection inference") AND (cat:math.ST OR cat:stat.TH OR cat:stat.ME)` |
| 高维推断 | `(abs:knockoffs OR abs:"false discovery rate") AND abs:"variable selection" AND (cat:stat.ME OR cat:math.ST)` |
| 比例渐近与随机矩阵 | `(abs:"proportional asymptotics" OR abs:"approximate message passing" OR abs:"random matrix theory") AND abs:statistic AND (cat:math.ST OR cat:stat.TH)` |
| 统计学习理论 | `(ti:"lecture notes" OR ti:tutorial OR ti:survey OR ti:introduction) AND (abs:"statistical learning theory" OR abs:"generalization bounds" OR abs:"Rademacher complexity" OR abs:"PAC-Bayes")` |
| 统计学习理论 | `(abs:"benign overfitting" OR abs:"double descent" OR abs:interpolation) AND abs:regression AND (cat:math.ST OR cat:stat.TH)` |
| 统计学习理论 | `(abs:"empirical risk minimization" OR abs:"excess risk" OR abs:"minimax rates") AND abs:classification AND (cat:math.ST OR cat:stat.TH)` |
| 共形预测 | `abs:"conformal prediction" AND (ti:tutorial OR ti:survey OR ti:review OR ti:introduction OR ti:"gentle")` |
| 共形预测 | `abs:"conformal" AND (abs:"coverage" OR abs:"distribution-free") AND (cat:math.ST OR cat:stat.TH OR cat:stat.ME)` |
| 经典多元分析 | `(abs:"canonical correlation" OR abs:"discriminant analysis" OR abs:"multivariate analysis") AND (cat:stat.ME OR cat:math.ST OR cat:stat.TH)` |
| 聚类与无监督学习 | `(abs:clustering OR abs:"mixture model") AND (abs:"high-dimensional" OR abs:"minimax" OR abs:consistency) AND (cat:math.ST OR cat:stat.TH OR cat:stat.ME)` |
| 低秩矩阵与张量 | `(abs:"matrix completion" OR abs:"low-rank matrix" OR abs:"tensor") AND abs:estimation AND (ti:survey OR ti:review OR ti:overview OR cat:math.ST)` |
| 核方法与学习理论 | `(abs:"kernel methods" OR abs:"reproducing kernel" OR abs:"random features") AND abs:"learning" AND (cat:math.ST OR cat:stat.TH) AND (ti:survey OR ti:review OR ti:introduction OR abs:rates)` |

## 11 贝叶斯统计

候选 636 条 → 种子 47 条（主列表 40，后备 7）→ 核验通过 42 条。

| 子主题 | 检索式 |
|---|---|
| 贝叶斯工作流 | `(ti:"Bayesian workflow" OR abs:"Bayesian workflow")` |
| 层级模型 | `(ti:tutorial OR ti:review OR ti:introduction OR ti:primer OR ti:survey) AND abs:Bayesian AND (abs:"hierarchical model" OR abs:multilevel) AND (cat:stat.ME OR cat:stat.AP OR cat:stat.CO)` |
| 层级模型 | `abs:"hierarchical" AND abs:Bayesian AND (abs:shrinkage OR abs:"partial pooling") AND (cat:stat.ME OR cat:stat.TH)` |
| 先验设定与诱导 | `(abs:"prior elicitation" OR abs:"prior specification" OR abs:"weakly informative prior" OR abs:"default prior") AND (cat:stat.ME OR cat:stat.TH OR cat:stat.AP)` |
| 收缩先验 | `(abs:"shrinkage prior" OR abs:horseshoe OR abs:"spike-and-slab" OR abs:"global-local") AND (cat:stat.ME OR cat:math.ST OR cat:stat.TH)` |
| 后验预测检验 | `(abs:"posterior predictive check" OR abs:"prior predictive" OR abs:"Bayesian model checking") AND (cat:stat.ME OR cat:stat.CO OR cat:stat.AP)` |
| 模型比较 | `(abs:"Bayes factor" OR abs:"marginal likelihood" OR abs:"Bayesian model comparison") AND (cat:stat.ME OR cat:stat.CO OR cat:stat.TH)` |
| 模型比较与预测评估 | `(abs:"leave-one-out cross-validation" OR abs:"Bayesian model averaging" OR abs:stacking OR abs:"predictive performance") AND abs:Bayesian AND (cat:stat.ME OR cat:stat.CO)` |
| 非参数贝叶斯 | `(ti:review OR ti:tutorial OR ti:survey OR ti:introduction) AND (abs:"Bayesian nonparametric" OR abs:"Dirichlet process" OR abs:"Gaussian process") AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST)` |
| 非参数贝叶斯 | `(abs:"Dirichlet process" OR abs:"Pitman-Yor" OR abs:"species sampling" OR abs:"completely random measure") AND (cat:math.ST OR cat:stat.TH OR cat:stat.ME)` |
| 后验收缩理论 | `(abs:"posterior contraction" OR abs:"posterior concentration") AND (cat:math.ST OR cat:stat.TH)` |
| 后验渐近与覆盖 | `(abs:"Bernstein-von Mises" OR abs:"frequentist coverage of credible") AND (cat:math.ST OR cat:stat.TH)` |
| 广义贝叶斯与误设 | `(abs:"generalized Bayesian" OR abs:"Gibbs posterior" OR abs:"power posterior" OR abs:"misspecified" AND abs:posterior) AND (cat:stat.ME OR cat:math.ST OR cat:stat.TH)` |
| 贝叶斯决策与客观贝叶斯 | `(abs:"Bayesian decision theory" OR abs:"objective Bayes" OR abs:"reference prior") AND (cat:stat.ME OR cat:math.ST OR cat:stat.TH)` |
| 经验贝叶斯 | `(abs:"empirical Bayes") AND (ti:review OR ti:tutorial OR abs:"nonparametric maximum likelihood" OR abs:compound) AND (cat:stat.ME OR cat:math.ST)` |
| 贝叶斯计算与软件 | `(abs:"simulation-based calibration" OR abs:"Bayesian computation" OR abs:"probabilistic programming" OR abs:Stan) AND (cat:stat.CO OR cat:stat.ME)` |
| 贝叶斯回归与变量选择 | `(abs:"Bayesian" AND abs:"variable selection" OR abs:"Bayesian linear regression") AND (cat:stat.ME OR cat:math.ST)` |
| 贝叶斯应用建模 | `(abs:"Bayesian" AND (abs:"meta-analysis" OR abs:"multilevel regression and poststratification")) AND (cat:stat.ME OR cat:stat.AP)` |

## 12 非参数、半参数与稳健统计

候选 781 条 → 种子 47 条（主列表 40，后备 7）→ 核验通过 40 条。

| 子主题 | 检索式 |
|---|---|
| 核平滑与密度估计 | `(ti:review OR ti:survey OR ti:tutorial OR ti:introduction) AND (abs:"kernel density estimation" OR abs:"kernel smoothing" OR abs:"local polynomial")` |
| 核平滑与密度估计 | `(ti:"kernel density" OR ti:"bandwidth selection" OR ti:"local polynomial") AND (cat:math.ST OR cat:stat.ME)` |
| RKHS核方法与核检验 | `(ti:"reproducing kernel" OR ti:"kernel mean embedding" OR ti:MMD OR ti:"maximum mean discrepancy" OR ti:HSIC) AND (ti:survey OR ti:review OR ti:tutorial OR ti:introduction OR ti:test)` |
| 样条与可加模型 | `(ti:spline OR ti:splines OR ti:"P-splines" OR ti:"smoothing spline") AND (cat:stat.ME OR cat:math.ST OR cat:stat.CO)` |
| 秩方法 | `(ti:"rank test" OR ti:"rank tests" OR ti:"rank-based" OR ti:Wilcoxon OR ti:"Mann-Whitney" OR ti:"signed rank") AND (cat:math.ST OR cat:stat.ME)` |
| 秩方法 | `(abs:"center-outward" OR abs:"multivariate ranks" OR abs:"optimal transport") AND (abs:rank OR abs:quantile) AND cat:math.ST` |
| 稳健统计 | `(ti:robust OR ti:robustness) AND (ti:survey OR ti:review OR ti:tutorial OR ti:introduction OR ti:"lecture notes") AND (cat:math.ST OR cat:stat.ME OR cat:stat.ML)` |
| 稳健统计 | `(abs:"median-of-means" OR abs:"heavy-tailed" OR abs:"Huber contamination") AND (abs:"mean estimation" OR abs:"robust estimation") AND cat:math.ST` |
| 稳健统计与影响函数 | `(ti:"breakdown point" OR ti:"M-estimator" OR ti:"M-estimators" OR ti:"Huber" OR ti:"influence function") AND (cat:math.ST OR cat:stat.ME)` |
| 影响函数与半参数估计 | `(ti:"influence function" OR ti:"influence functions" OR ti:"one-step" OR ti:"debiased" OR ti:"doubly robust") AND (ti:tutorial OR ti:review OR ti:introduction OR ti:primer OR ti:guide)` |
| 影响函数与半参数估计 | `(abs:"double machine learning" OR abs:"targeted maximum likelihood" OR abs:"debiased machine learning") AND (ti:review OR ti:tutorial OR ti:introduction OR ti:guide OR ti:primer OR ti:overview)` |
| 缺失数据 | `(ti:"missing data" OR ti:"incomplete data" OR ti:"missing not at random" OR ti:"missingness") AND (ti:review OR ti:tutorial OR ti:introduction OR ti:overview OR ti:guide)` |
| 缺失数据与多重插补 | `(ti:"multiple imputation" OR ti:imputation) AND (cat:stat.ME OR cat:stat.CO OR cat:math.ST)` |
| 缺失数据 | `(ti:"missing data" OR ti:"missing at random" OR ti:"nonignorable") AND (cat:math.ST OR cat:stat.ME) AND abs:identification` |
| 非参数方法综述 | `(ti:nonparametric) AND (ti:review OR ti:survey OR ti:tutorial OR ti:introduction) AND (cat:stat.ME OR cat:math.ST)` |
| 形状约束非参数估计 | `(ti:"isotonic" OR ti:"shape-constrained" OR ti:"shape constraints" OR ti:"log-concave") AND (cat:math.ST OR cat:stat.ME)` |
| 经典 | `(ti:"robust statistics" OR ti:"multiple imputation" OR ti:"kernel density estimation" OR ti:"influence function" OR ti:"smoothing splines" OR ti:"kernel mean embedding")`（经典，不限日期） |
| 秩方法与非参数检验 | `(ti:"distribution-free" OR ti:"nonparametric test" OR ti:"independence test") AND (cat:math.ST OR cat:stat.ME) AND (abs:kernel OR abs:rank)` |
| 稳健统计 | `(ti:survey OR ti:review OR ti:tutorial OR ti:introduction OR ti:overview OR ti:"lecture notes") AND (abs:"robust statistics" OR abs:"robust estimation" OR abs:"heavy-tailed" OR abs:"contamination") AND (cat:math.ST OR cat:stat.ME OR cat:stat.ML OR cat:cs.DS)` |
| 核平滑与密度估计 | `(ti:survey OR ti:review OR ti:tutorial OR ti:introduction OR ti:overview) AND (abs:"nonparametric regression" OR abs:"density estimation" OR abs:"nonparametric smoothing") AND (cat:stat.ME OR cat:math.ST OR cat:stat.ML)` |
| 样条与可加模型 | `(ti:review OR ti:tutorial OR ti:introduction OR ti:overview OR ti:primer) AND (abs:"generalized additive model" OR abs:"penalized splines" OR abs:"smoothing splines" OR abs:"P-splines")` |
| 缺失数据与多重插补 | `(ti:review OR ti:survey OR ti:tutorial OR ti:guide OR ti:overview) AND abs:"multiple imputation"` |
| 秩方法 | `(ti:review OR ti:survey OR ti:overview OR ti:introduction) AND (abs:"statistical depth" OR abs:"data depth" OR abs:"multivariate quantile" OR abs:"center-outward" OR abs:"multivariate ranks")` |
| 形状约束非参数估计 | `(ti:review OR ti:tutorial OR ti:introduction OR ti:survey OR ti:overview) AND (abs:"isotonic regression" OR abs:"shape constraint" OR abs:"shape-constrained" OR abs:"log-concave density")` |
| 影响函数与半参数估计 | `(ti:semiparametric OR ti:debiased OR ti:"doubly robust" OR ti:Riesz OR ti:"one-step" OR ti:"targeted") AND cat:math.ST` |
| 稳健统计 | `ti:robust AND (ti:"mean estimation" OR ti:"covariance" OR ti:"regression" OR ti:"location") AND cat:math.ST` |
| 非参数似然 | `ti:"empirical likelihood" AND (cat:math.ST OR cat:stat.ME)` |
| RKHS核方法与核检验 | `ti:kernel AND (ti:test OR ti:testing OR ti:"two-sample") AND (cat:math.ST OR cat:stat.ME OR cat:stat.ML)` |
| 缺失数据 | `(ti:"missing data" OR ti:"missing not at random" OR ti:"nonignorable" OR ti:"missing at random") AND (ti:semiparametric OR ti:efficient OR ti:"doubly robust" OR ti:identification OR ti:identifiability OR ti:graphical)` |

## 13 时间序列与空间统计

候选 737 条 → 种子 50 条（主列表 42，后备 8）→ 核验通过 42 条。

| 子主题 | 检索式 |
|---|---|
| 时间序列综述与教程 | `(ti:survey OR ti:review OR ti:tutorial OR ti:introduction OR ti:overview) AND abs:"time series" AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST OR cat:stat.AP)` |
| ARIMA 与线性时间序列模型 | `(abs:ARMA OR abs:ARIMA OR abs:autoregressive) AND abs:"time series" AND (cat:math.ST OR cat:stat.ME OR cat:stat.TH)` |
| 谱分析 | `abs:"spectral density" AND abs:"time series" AND (cat:math.ST OR cat:stat.ME OR cat:stat.TH)` |
| 状态空间与滤波 | `abs:"state space model" AND (abs:"Kalman filter" OR abs:"particle filter" OR abs:smoothing) AND (cat:stat.ME OR cat:stat.CO OR cat:math.ST)` |
| 多元时间序列 | `(abs:"vector autoregressive" OR abs:"VAR model" OR abs:cointegration) AND (cat:stat.ME OR cat:math.ST OR cat:econ.EM)` |
| 高维时间序列 | `abs:"high-dimensional time series" AND (cat:stat.ME OR cat:math.ST OR cat:stat.TH)` |
| 变点检测 | `(abs:"change point" OR abs:changepoint) AND abs:"time series" AND (cat:stat.ME OR cat:math.ST)` |
| 非平稳与长记忆 | `(abs:"locally stationary" OR abs:"long memory" OR abs:"long-range dependence") AND (cat:math.ST OR cat:stat.ME)` |
| 相依数据推断 | `abs:bootstrap AND abs:"time series" AND (abs:dependent OR abs:block) AND (cat:math.ST OR cat:stat.ME)` |
| 预测与预测评价 | `(abs:"probabilistic forecast" OR abs:"forecast evaluation" OR abs:"forecast reconciliation") AND (cat:stat.ME OR cat:stat.AP OR cat:stat.TH)` |
| 计数与非高斯时间序列 | `(abs:"count time series" OR abs:"integer-valued" OR abs:INGARCH) AND (cat:stat.ME OR cat:math.ST)` |
| 空间统计综述 | `(ti:review OR ti:survey OR ti:tutorial OR ti:overview OR ti:introduction) AND (abs:"spatial statistics" OR abs:geostatistics OR abs:"spatial data")` |
| 地统计与高斯过程 | `(abs:kriging OR abs:geostatistical OR abs:"spatial Gaussian process") AND (cat:stat.ME OR cat:stat.CO OR cat:math.ST)` |
| 大规模空间计算 | `(abs:Vecchia OR abs:"nearest neighbor Gaussian process" OR abs:"SPDE approach") AND (cat:stat.ME OR cat:stat.CO)` |
| 面数据与 CAR 模型 | `(abs:"areal data" OR abs:"conditional autoregressive" OR abs:"disease mapping") AND (cat:stat.ME OR cat:stat.AP)` |
| 空间点过程 | `abs:"spatial point process" AND (cat:stat.ME OR cat:math.ST OR cat:stat.CO)` |
| 时空建模 | `(abs:"spatio-temporal" OR abs:spatiotemporal) AND (ti:review OR ti:survey OR ti:tutorial OR ti:overview OR abs:"statistical model") AND (cat:stat.ME OR cat:stat.AP)` |
| 函数型数据 | `(abs:"functional data" OR abs:"functional time series") AND (ti:review OR ti:survey OR ti:tutorial OR ti:introduction OR ti:overview OR cat:math.ST)` |
| 空间协方差与空间混杂 | `(abs:"spatial confounding" OR abs:"nonstationary covariance" OR abs:"covariance function") AND abs:spatial AND (cat:stat.ME OR cat:math.ST)` |

## 14 实验设计、调查抽样与因果推断

候选 692 条 → 种子 50 条（主列表 42，后备 8）→ 核验通过 40 条。

| 子主题 | 检索式 |
|---|---|
| 因果推断综述与教程 | `(ti:review OR ti:survey OR ti:tutorial OR ti:introduction OR ti:primer) AND abs:"causal inference" AND (cat:stat.ME OR cat:stat.TH OR cat:econ.EM OR cat:math.ST)` |
| 随机化与基于设计的推断 | `(abs:"randomization inference" OR abs:"design-based inference" OR abs:"Fisher randomization test") AND (cat:stat.ME OR cat:math.ST)` |
| 区组、再随机化与协变量调整 | `(abs:rerandomization OR abs:"covariate adjustment" OR abs:"stratified randomization" OR abs:"blocking") AND abs:"randomized experiment" AND (cat:stat.ME OR cat:math.ST)` |
| 析因与最优设计 | `(abs:"factorial design" OR abs:"fractional factorial" OR abs:"optimal design" OR abs:"design of experiments") AND (cat:stat.ME OR cat:math.ST)` |
| 序贯与自适应实验 | `(abs:"adaptive experiment" OR abs:"response-adaptive" OR abs:"A/B test" OR abs:"sequential experiment") AND (cat:stat.ME OR cat:math.ST OR cat:stat.ML)` |
| 抽样与权重 | `(abs:"survey sampling" OR abs:"finite population" OR abs:"sampling weights" OR abs:calibration) AND abs:survey AND (cat:stat.ME OR cat:math.ST)` |
| 非概率样本与数据整合 | `(abs:"nonprobability sample" OR abs:"non-probability" OR abs:"data integration" OR abs:"multilevel regression and poststratification") AND (cat:stat.ME OR cat:stat.AP)` |
| 调查误差与小域估计 | `(abs:nonresponse OR abs:"total survey error" OR abs:"small area estimation" OR abs:"measurement error") AND abs:survey AND (cat:stat.ME OR cat:stat.AP)` |
| 因果识别 | `(abs:"causal graph" OR abs:"directed acyclic graph" OR abs:identification OR abs:"potential outcomes") AND (ti:review OR ti:tutorial OR ti:introduction OR ti:overview) AND (cat:stat.ME OR cat:econ.EM OR cat:stat.ML)` |
| 观察研究：匹配与加权 | `(abs:"propensity score" OR abs:matching OR abs:"inverse probability weighting" OR abs:"doubly robust") AND abs:"observational stud" AND (cat:stat.ME OR cat:econ.EM)` |
| 敏感性分析 | `(abs:"sensitivity analysis" AND abs:"unmeasured confounding") AND (cat:stat.ME OR cat:math.ST)` |
| 双重差分 | `(abs:"difference-in-differences" OR abs:"staggered adoption" OR abs:"event study") AND (cat:econ.EM OR cat:stat.ME)` |
| 断点回归 | `abs:"regression discontinuity" AND (cat:econ.EM OR cat:stat.ME OR cat:math.ST)` |
| 合成控制 | `(abs:"synthetic control" OR abs:"panel data" AND abs:"causal") AND (cat:econ.EM OR cat:stat.ME)` |
| 工具变量 | `(abs:"instrumental variable" OR abs:"weak instruments" OR abs:LATE) AND (cat:econ.EM OR cat:stat.ME) AND (ti:review OR ti:survey OR ti:guide OR abs:identification)` |
| 干扰与网络实验 | `(abs:interference OR abs:spillover OR abs:"network experiment") AND abs:"causal" AND (cat:stat.ME OR cat:math.ST)` |
| 异质处理效应与双重机器学习 | `(abs:"heterogeneous treatment effect" OR abs:"conditional average treatment effect" OR abs:"double machine learning") AND (cat:stat.ME OR cat:econ.EM)` |
| 外推与可迁移性 | `(abs:"generalizability" OR abs:transportability OR abs:"external validity") AND abs:"causal" AND (cat:stat.ME)` |

## 15 生物统计与公共卫生

候选 788 条 → 种子 50 条（主列表 42，后备 8）→ 核验通过 41 条。

| 子主题 | 检索式 |
|---|---|
| 生存分析综述与教程 | `(ti:review OR ti:tutorial OR ti:survey OR ti:introduction OR ti:primer) AND abs:"survival analysis" AND (cat:stat.ME OR cat:stat.AP OR cat:math.ST)` |
| 生存分析模型 | `(abs:"Cox model" OR abs:"proportional hazards" OR abs:"restricted mean survival time") AND (cat:stat.ME OR cat:math.ST)` |
| 竞争风险与多状态 | `(abs:"competing risks" OR abs:"multi-state model" OR abs:"cure model" OR abs:"interval censor") AND (cat:stat.ME OR cat:math.ST)` |
| 纵向数据 | `(abs:"longitudinal data" OR abs:"generalized estimating equations" OR abs:"joint model") AND (cat:stat.ME OR cat:stat.AP)` |
| 临床试验估计目标 | `(abs:estimand OR abs:"intercurrent event") AND (cat:stat.ME OR cat:stat.AP)` |
| 适应性与平台试验 | `(abs:"adaptive design" OR abs:"platform trial" OR abs:"group sequential" OR abs:"master protocol") AND abs:trial AND (cat:stat.ME OR cat:stat.AP)` |
| 历史借用与外部对照 | `(abs:"Bayesian" AND abs:"clinical trial") AND (abs:borrowing OR abs:"historical control" OR abs:"external control") AND (cat:stat.ME OR cat:stat.AP)` |
| 剂量探索试验 | `(abs:"dose-finding" OR abs:"phase I" OR abs:"dose escalation") AND (cat:stat.ME OR cat:stat.AP)` |
| 临床试验分析 | `(abs:"covariate adjustment" AND abs:"randomized clinical trial") OR (abs:"stratified" AND abs:"clinical trial" AND cat:stat.ME)` |
| 真实世界证据 | `(abs:"target trial emulation" OR abs:"real-world evidence" OR abs:"real-world data") AND (cat:stat.ME OR cat:stat.AP)` |
| 孟德尔随机化 | `(abs:"Mendelian randomization") AND (cat:stat.ME OR cat:stat.AP OR cat:q-bio.QM)` |
| 流行病学方法 | `(abs:epidemiolog* OR abs:"case-control" OR abs:"cohort study") AND (ti:review OR ti:tutorial OR ti:introduction OR ti:primer) AND (cat:stat.ME OR cat:stat.AP)` |
| 传染病统计 | `(abs:"reproduction number" OR abs:"infectious disease" OR abs:"epidemic model") AND (cat:stat.ME OR cat:stat.AP OR cat:q-bio.PE)` |
| 诊断试验 | `(abs:"diagnostic accuracy" OR abs:"ROC curve" OR abs:sensitivity AND abs:specificity AND abs:diagnostic) AND (cat:stat.ME OR cat:stat.AP)` |
| 多重检验 | `(abs:"multiple testing" OR abs:multiplicity OR abs:"familywise error" OR abs:"false discovery rate") AND (abs:"clinical trial" OR abs:genomic OR abs:biomedical) AND (cat:stat.ME OR cat:stat.AP)` |
| 荟萃分析 | `(abs:"meta-analysis" OR abs:"network meta-analysis" OR abs:"individual participant data") AND (cat:stat.ME OR cat:stat.AP)` |
| 动态治疗方案 | `(abs:"dynamic treatment regime" OR abs:"individualized treatment rule" OR abs:"SMART") AND (cat:stat.ME OR cat:stat.ML)` |
| 临床预测模型 | `(abs:"clinical prediction model" OR abs:"risk prediction" OR abs:"calibration" AND abs:"prediction model") AND (cat:stat.ME OR cat:stat.AP)` |
| 替代终点与中介 | `(abs:"surrogate endpoint" OR abs:"surrogate marker" OR abs:"mediation analysis") AND (cat:stat.ME OR cat:stat.AP)` |

## 16 经济、金融、保险与风险

候选 574 条 → 种子 50 条（主列表 42，后备 8）→ 核验通过 40 条。

| 子主题 | 检索式 |
|---|---|
| 计量经济学综述 | `(ti:survey OR ti:review OR ti:introduction OR ti:tutorial OR ti:primer OR ti:overview) AND cat:econ.EM` |
| 面板数据 | `abs:"panel data" AND (ti:review OR ti:survey OR ti:introduction OR ti:guide OR ti:overview)` |
| 面板数据 | `abs:"panel data" AND (abs:"fixed effects" OR abs:"interactive effects" OR abs:"factor structure") AND cat:econ.EM` |
| 计量经济学（IV/GMM） | `(abs:"weak instruments" OR abs:"generalized method of moments" OR abs:"many instruments") AND cat:econ.EM` |
| 金融时间序列与波动率 | `(abs:GARCH OR abs:"stochastic volatility" OR abs:"realized volatility") AND (cat:q-fin.ST OR cat:econ.EM OR cat:stat.ME)` |
| 金融时间序列与波动率 | `(ti:survey OR ti:review OR ti:introduction) AND abs:volatility AND (cat:q-fin.ST OR cat:q-fin.RM OR cat:econ.EM OR cat:q-fin.CP)` |
| 高频金融计量 | `abs:"high-frequency" AND (abs:"realized" OR abs:"microstructure noise") AND (cat:econ.EM OR cat:math.ST OR cat:q-fin.ST)` |
| 风险度量 | `(abs:"expected shortfall" OR abs:"value-at-risk" OR abs:"value at risk") AND (abs:backtesting OR abs:elicitability OR abs:elicitable)` |
| 风险度量 | `abs:"risk measures" AND (ti:review OR ti:survey OR ti:introduction OR ti:tutorial OR ti:overview)` |
| 精算统计 | `(abs:"claims reserving" OR abs:"loss reserving" OR abs:"insurance pricing" OR abs:"ratemaking" OR abs:credibility) AND (cat:q-fin.RM OR cat:stat.AP OR cat:stat.ME)` |
| 精算统计 | `(ti:review OR ti:survey OR ti:tutorial OR ti:introduction OR ti:overview) AND abs:actuarial` |
| 精算统计（死亡率建模） | `abs:mortality AND (abs:"Lee-Carter" OR abs:"mortality forecasting" OR abs:"stochastic mortality")` |
| 极值统计 | `abs:"extreme value" AND (ti:review OR ti:survey OR ti:tutorial OR ti:introduction OR ti:overview)` |
| 极值统计 | `(abs:"extreme value theory" OR abs:"peaks over threshold" OR abs:"tail index" OR abs:"generalized Pareto") AND (cat:stat.ME OR cat:stat.TH OR cat:math.ST)` |
| 依赖建模与 copula | `abs:copula AND (ti:review OR ti:survey OR ti:introduction OR ti:overview OR ti:tutorial)` |
| 系统性风险 | `abs:"systemic risk" AND (abs:CoVaR OR abs:"tail dependence" OR abs:"extreme quantile") AND (cat:q-fin.RM OR cat:econ.EM OR cat:stat.ME)` |
| 资产定价计量 | `(abs:"asset pricing" AND abs:"factor") AND (abs:"inference" OR abs:"test") AND (cat:econ.EM OR cat:q-fin.ST)` |
| 宏观计量（VAR/局部投影） | `(abs:"local projections" OR abs:"vector autoregression" OR abs:"structural VAR") AND cat:econ.EM` |
| 预测评估 | `(abs:"forecast evaluation" OR abs:"density forecasts" OR abs:"quantile forecasts") AND (cat:econ.EM OR cat:q-fin.RM OR cat:stat.ME)` |

## 17 工业、环境与其他专业应用

候选 703 条 → 种子 50 条（主列表 42，后备 8）→ 核验通过 42 条。

| 子主题 | 检索式 |
|---|---|
| 统计过程控制 | `(abs:"control chart" OR abs:"control charts" OR abs:"statistical process control") AND (ti:review OR ti:survey OR ti:overview OR ti:tutorial OR ti:introduction)` |
| 统计过程控制 | `(abs:"control chart" OR abs:"statistical process control" OR abs:"statistical process monitoring") AND (cat:stat.ME OR cat:stat.AP)` |
| 统计过程控制（剖面/多元监控） | `(abs:"profile monitoring" OR abs:"multivariate process monitoring" OR abs:"high-dimensional process monitoring") AND (cat:stat.ME OR cat:stat.AP OR cat:stat.ML)` |
| 序贯变点检测 | `(abs:"quickest change detection" OR abs:"sequential change detection" OR abs:"online changepoint") AND (cat:stat.ME OR cat:math.ST OR cat:stat.TH)` |
| 可靠性与退化建模 | `(abs:"degradation data" OR abs:"degradation model" OR abs:"degradation modeling" OR abs:"accelerated life" OR abs:"accelerated degradation") AND (cat:stat.ME OR cat:stat.AP)` |
| 可靠性与退化建模 | `abs:reliability AND (abs:"lifetime data" OR abs:"failure time" OR abs:"remaining useful life") AND (cat:stat.ME OR cat:stat.AP)` |
| 可靠性与退化建模 | `(ti:review OR ti:survey OR ti:tutorial OR ti:overview) AND (abs:"reliability engineering" OR abs:"system reliability" OR abs:"reliability analysis") AND (cat:stat.ME OR cat:stat.AP OR cat:stat.CO)` |
| 环境统计 | `(abs:"environmental statistics" OR abs:"environmental data" OR abs:environmetrics) AND (ti:review OR ti:overview OR ti:tutorial OR ti:introduction OR ti:survey)` |
| 环境统计（气候极值） | `(abs:"spatial extremes" OR abs:"climate extremes" OR abs:"extreme precipitation" OR abs:"heatwave") AND (cat:stat.AP OR cat:stat.ME)` |
| 环境统计（气候） | `(abs:"detection and attribution" OR abs:"climate model" OR abs:"climate projections") AND (cat:stat.AP OR cat:stat.ME)` |
| 环境统计（空气质量） | `(abs:"air pollution" OR abs:"air quality" OR abs:"PM2.5") AND (cat:stat.AP OR cat:stat.ME)` |
| 水文频率分析 | `(abs:"flood frequency" OR abs:"frequency analysis" OR abs:"return level" OR abs:"return period") AND (abs:hydrolog* OR abs:flood OR abs:rainfall OR abs:streamflow)` |
| 能源统计 | `(abs:"probabilistic forecasting" OR abs:"probabilistic forecasts") AND (abs:"wind power" OR abs:solar OR abs:"electricity load" OR abs:"electricity price" OR abs:energy) AND (cat:stat.AP OR cat:stat.ME OR cat:stat.ML)` |
| 交通统计 | `(abs:traffic OR abs:transportation OR abs:"travel time") AND (cat:stat.AP OR cat:stat.ME)` |
| 农业试验 | `(abs:"field trials" OR abs:"plant breeding" OR abs:"agricultural experiments" OR abs:"crop yield" OR abs:"field experiments") AND (cat:stat.AP OR cat:stat.ME OR cat:q-bio.QM)` |
| 官方统计 | `(abs:"official statistics" OR abs:"national statistical" OR abs:"statistical agencies" OR abs:census)` |
| 官方统计 | `(abs:"small area estimation" OR abs:"record linkage" OR abs:"statistical disclosure control") AND (cat:stat.ME OR cat:stat.AP)` |
| 官方统计 | `(abs:nowcasting OR abs:"administrative data") AND (cat:stat.AP OR cat:stat.ME)` |
| 工业试验设计 | `(abs:"computer experiments" OR abs:"response surface" OR abs:"robust parameter design" OR abs:"industrial experiments") AND (cat:stat.ME OR cat:stat.AP)` |

## 18 统计计算与数据科学

候选 1145 条 → 种子 50 条（主列表 42，后备 8）→ 核验通过 42 条。

| 子主题 | 检索式 |
|---|---|
| MCMC | `abs:"Markov chain Monte Carlo" AND (ti:review OR ti:survey OR ti:tutorial OR ti:introduction OR ti:primer OR ti:"lecture notes" OR ti:overview)` |
| MCMC（HMC/Langevin） | `(abs:"Hamiltonian Monte Carlo" OR abs:"No-U-Turn" OR abs:"Langevin") AND cat:stat.CO` |
| MCMC 收敛诊断与理论 | `(abs:"MCMC" OR abs:"Markov chain Monte Carlo") AND (abs:"convergence diagnostics" OR abs:"effective sample size" OR abs:"R-hat" OR abs:"mixing time") AND (cat:stat.CO OR cat:stat.ME)` |
| MCMC（非可逆/PDMP） | `(abs:"piecewise deterministic" OR abs:"non-reversible" OR abs:"zig-zag" OR abs:"bouncy particle") AND cat:stat.CO` |
| SMC | `(abs:"sequential Monte Carlo" OR abs:"particle filter") AND (ti:review OR ti:tutorial OR ti:introduction OR ti:survey OR ti:overview)` |
| SMC | `(abs:"sequential Monte Carlo" OR abs:"particle filter" OR abs:"particle MCMC") AND cat:stat.CO` |
| 重要性采样 | `abs:"importance sampling" AND (cat:stat.CO OR cat:stat.ME) AND (ti:review OR ti:survey OR ti:tutorial OR ti:adaptive OR abs:"effective sample size" OR abs:"Pareto")` |
| Monte Carlo 与方差缩减 | `(abs:"quasi-Monte Carlo" OR abs:"multilevel Monte Carlo" OR abs:"variance reduction") AND (cat:stat.CO OR cat:math.NA)` |
| Bootstrap 与重抽样 | `abs:bootstrap AND (ti:review OR ti:survey OR ti:introduction OR ti:tutorial OR ti:overview)` |
| Bootstrap 与重抽样 | `(abs:bootstrap OR abs:resampling OR abs:jackknife) AND cat:stat.CO` |
| EM 与优化算法 | `(abs:"expectation-maximization" OR abs:"EM algorithm" OR abs:"MM algorithm") AND (cat:stat.CO OR cat:math.ST OR cat:stat.ME)` |
| 变分推断 | `abs:"variational inference" AND (ti:review OR ti:tutorial OR ti:introduction OR ti:survey OR ti:primer OR ti:overview)` |
| 变分推断理论 | `abs:"variational" AND (abs:"guarantees" OR abs:"consistency" OR abs:"mean-field") AND (cat:math.ST OR cat:stat.CO OR cat:stat.TH)` |
| ABC 与基于模拟的推断 | `abs:"approximate Bayesian computation" OR (abs:"simulation-based inference" AND cat:stat.CO)` |
| 可扩展计算 | `(abs:"divide-and-conquer" OR abs:"subsampling" OR abs:"distributed" OR abs:"coresets" OR abs:"sketching") AND (abs:"massive data" OR abs:"large-scale" OR abs:"big data") AND (cat:stat.CO OR cat:stat.ME)` |
| 可扩展 MCMC | `(abs:"stochastic gradient" AND (abs:MCMC OR abs:"Langevin")) AND (cat:stat.CO OR cat:stat.ML)` |
| 概率编程与自动微分 | `(abs:"probabilistic programming" OR abs:Stan OR abs:"automatic differentiation") AND cat:stat.CO` |
| 方法与软件 | `(ti:"R package" OR ti:"Python package" OR ti:"Julia package") AND cat:stat.CO` |
| 数值方法与 Monte Carlo | `(abs:"Monte Carlo" OR abs:"numerical") AND (ti:review OR ti:tutorial OR ti:"lecture notes" OR ti:introduction) AND cat:stat.CO` |
| 基于传输的采样 | `(abs:"diffusion models" OR abs:"normalizing flows" OR abs:"measure transport") AND (abs:sampling OR abs:"posterior sampling") AND cat:stat.CO` |
| MCMC 与 Monte Carlo 教程 | `(ti:"Markov chain Monte Carlo" OR ti:MCMC OR ti:"Monte Carlo" OR ti:sampling) AND (ti:review OR ti:tutorial OR ti:introduction OR ti:primer OR ti:guide OR ti:"lecture notes") AND (cat:stat.CO OR cat:stat.ME OR cat:math.ST OR cat:stat.ML)` |
| MCMC（Gibbs） | `(abs:"Gibbs sampler" OR abs:"Gibbs sampling" OR abs:"data augmentation") AND abs:convergence AND (cat:stat.CO OR cat:math.ST)` |
| MCMC（多峰与回火） | `(abs:"parallel tempering" OR abs:"replica exchange" OR abs:"multimodal") AND (abs:MCMC OR abs:"Markov chain Monte Carlo") AND cat:stat.CO` |
| Monte Carlo 与方差缩减 | `(abs:"control variates" OR abs:"Stein discrepancy" OR abs:"kernel Stein") AND cat:stat.CO` |
| 边际似然计算 | `(abs:"marginal likelihood" OR abs:"normalizing constant" OR abs:"evidence") AND (abs:"bridge sampling" OR abs:"thermodynamic integration" OR abs:"nested sampling") AND cat:stat.CO` |
| 确定性近似推断 | `(abs:"Laplace approximation" OR abs:INLA OR abs:"integrated nested Laplace") AND (cat:stat.CO OR cat:stat.ME)` |
| MCMC 收敛诊断与理论 | `(abs:couplings OR abs:"unbiased estimation") AND (abs:MCMC OR abs:"Markov chain") AND cat:stat.CO` |
| 优化与随机逼近 | `(abs:"stochastic approximation" OR abs:"stochastic optimization" OR abs:"stochastic gradient descent") AND (abs:"statistical inference" OR abs:"maximum likelihood") AND (cat:stat.CO OR cat:math.ST)` |
| 可扩展计算 | `(abs:"Gaussian process" AND (abs:scalable OR abs:"Vecchia" OR abs:"inducing points")) AND cat:stat.CO` |
| 重抽样与交叉验证计算 | `(abs:"cross-validation" AND (abs:"computation" OR abs:"approximate")) AND cat:stat.CO` |

## 20 研究方法与实战

候选 562 条 → 种子 50 条（主列表 42，后备 8）→ 核验通过 40 条。

| 子主题 | 检索式 |
|---|---|
| 模拟研究方法学 | `(abs:"simulation studies" OR abs:"simulation study") AND (abs:methodological OR abs:ADEMP OR abs:"neutral comparison" OR abs:"best practices" OR abs:guidance) AND (cat:stat.ME OR cat:stat.CO OR cat:stat.OT)` |
| 模拟研究方法学 | `(abs:"neutral comparison" OR abs:"benchmarking" OR abs:"methodological research") AND (abs:"statistical methods" OR abs:methodology) AND (cat:stat.ME OR cat:stat.OT OR cat:stat.CO)` |
| 估计目标定义 | `abs:estimand AND (cat:stat.ME OR cat:stat.AP OR cat:stat.OT)` |
| 可复现性 | `(abs:reproducibility OR abs:reproducible OR abs:replicability) AND (cat:stat.ME OR cat:stat.OT OR cat:stat.AP OR cat:stat.CO)` |
| 可重复性与重复研究 | `(abs:"replication success" OR abs:"replication studies" OR abs:"replication crisis" OR abs:"replication study") AND (cat:stat.ME OR cat:stat.AP OR cat:stat.OT)` |
| 敏感性分析 | `abs:"sensitivity analysis" AND (ti:tutorial OR ti:review OR ti:guide OR ti:primer OR ti:introduction OR ti:overview) AND (cat:stat.ME OR cat:stat.AP)` |
| 多元分析流程（multiverse） | `(abs:"multiverse analysis" OR abs:"many analysts" OR abs:"specification curve" OR abs:"analytic flexibility" OR abs:"researcher degrees of freedom")` |
| 预注册与分析计划 | `(abs:preregistration OR abs:"pre-registration" OR abs:"registered report" OR abs:"registered reports" OR abs:"statistical analysis plan")` |
| 统计报告规范 | `(abs:"reporting guidelines" OR abs:"reporting guideline" OR abs:"statistical reporting" OR abs:"reporting checklist") AND (cat:stat.ME OR cat:stat.AP OR cat:stat.OT OR cat:q-bio.QM)` |
| 统计显著性与报告 | `(abs:"p-values" OR abs:"statistical significance" OR abs:"null hypothesis significance testing") AND (abs:misinterpretation OR abs:misuse OR abs:reform OR abs:recommendations) AND (cat:stat.ME OR cat:stat.OT OR cat:stat.AP)` |
| 研究诚信与偏差 | `(abs:"questionable research practices" OR abs:"p-hacking" OR abs:"publication bias") AND (cat:stat.ME OR cat:stat.AP OR cat:stat.OT)` |
| 统计咨询与合作 | `(abs:"statistical consulting" OR abs:"collaborative statistics" OR abs:"statistical collaboration" OR abs:"collaborative biostatistics")` |
| 研究伦理 | `(abs:ethics OR abs:ethical) AND (abs:statisticians OR abs:"statistical practice" OR abs:"data science") AND (cat:stat.OT OR cat:stat.ME OR cat:stat.AP OR cat:cs.CY)` |
| 数据分析工作流 | `(abs:"data analysis" OR abs:"statistical analysis") AND (abs:workflow OR abs:"principles" OR abs:"practice") AND (ti:workflow OR ti:principles OR ti:guide OR ti:practice) AND (cat:stat.OT OR cat:stat.ME OR cat:stat.AP)` |
| 可复现性与开放科学 | `(abs:"open science" OR abs:"code sharing" OR abs:"data sharing" OR abs:"research software") AND (cat:stat.OT OR cat:stat.ME OR cat:stat.CO OR cat:stat.AP)` |
| 研究设计与样本量 | `(abs:"sample size" OR abs:"power analysis") AND (ti:tutorial OR ti:guide OR ti:review OR ti:primer) AND (cat:stat.ME OR cat:stat.AP)` |
| 敏感性分析（缺失数据） | `(abs:"missing data" OR abs:"multiple imputation") AND (ti:tutorial OR ti:guide OR ti:guidance OR ti:framework) AND (cat:stat.ME OR cat:stat.AP)` |
| 研究问题与估计目标 | `(abs:"target trial emulation" OR abs:"causal roadmap" OR abs:"protocol") AND (ti:tutorial OR ti:guide OR ti:roadmap OR ti:framework) AND (cat:stat.ME OR cat:stat.AP)` |

## 缺口说明文件

- scripts/annotations/materials_gap_m1_cn.md
- scripts/annotations/materials_gap_m6_cn.md
- scripts/annotations/materials_gap_sw_cn.md
