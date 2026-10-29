# 分片 m1 资料缺口与说明（群 01–04，2026-10-29）

## 达标情况
- 01 数学基础：B 5 / A 3 / D 2，均核验通过。
- 02 高阶数学工具：B 4 / A 3 / D 2，均核验通过。
- 03 基础概率论：B 新增 2（B03-02、B03-03；连同主会话 B03-01 共 3）/ A 3 / D 3。
- 04 高等概率论：B 3 / A 4 / D 2。

## 缺口
1. **大偏差专著缺失**：Rassoul-Agha & Seppäläinen《A Course on Large Deviations》作者站 PDF 返回 HTTP 403（B04-04 已 exclude）；Dembo–Zeitouni、den Hollander 无合法公开全文。现由 A04-03（Norris Part III 第 6 章 Large deviations）、A04-04（6.436J 大偏差讲次）与 Durrett 覆盖。
2. **Blitzstein–Hwang《Introduction to Probability》**：官方入口跳转 Google Drive，所有者禁止下载（B03-05 已 exclude），不绕过。Harvard Stat 110 站点（stat110.hsites / projects.iq）对脚本 UA 返回 403，未收 Stat 110 习题。
3. **泛函分析专门教材**：Teschl《Topics in Linear and Nonlinear Functional Analysis》因 AMS 出版暂时撤下（作者页称 24 个月后恢复）；由 B02-02 Axler MIRA（Banach/Hilbert/谱理论章节）与 A02-02 MIT 18.102 讲义覆盖。
4. **Hefferon《Linear Algebra》**：作者页通过 OpenIntro 付费滑块表单分发，未走该途径，未收。
5. **Pishro-Nik probabilitycourse.com**：站点有反爬（HEAD 403）且 HTML 页多，未收。
6. **Chan《Introduction to Probability for Data Science》整本 PDF** 需在 Michigan Publishing 填表；已改为作者官网全部 10 个章节 PDF（B03-02）。

## 兄弟库复用
`sibling_reusable_cn.csv` 中 machine_learning_deep_learning_literature 的源路径（/root/machine_learning_deep_learning_literature/...）在本机均不存在，故本分片未使用 reuse，Axler LADR、Boyd 两书、Bubeck、Vershynin 均改为从作者官方地址直接下载核验。另：清单中 MLB022 实为 Grinstead–Snell，并非 Blitzstein–Hwang。
