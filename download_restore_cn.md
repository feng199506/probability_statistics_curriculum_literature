# 下载与解压恢复说明（概率与统计课程文献库，2026-10-29）

本资料库按“轻量 Git 分支 + Release 全文附件”的方式发布：

- **Git 分支 `release-lite-20261029`**：只包含以下内容，不含教材、讲义、论文、实践、案例、软件文档和培养方案全文：
  - 根目录的总报告与登记表：`README_cn.md`、`catalog_cn.csv`、`progress_cn.csv`、`download_failures_cn.csv`、`search_log_cn.md`；
  - `guides/`（学习路线与选读指南）；
  - 脚本 `scripts/`（含下载状态与种子数据）；
  - 本说明、分包索引、改名明细和未发布清单。

  仓库原有的 `main` 分支没有改动。这个分支的父提交是 `main`。
- **Release `probstat-full-20261029`**：5 个独立的不压缩 `.tar` 包，合起来就是资料库的发布内容。

Release 页面：https://github.com/feng199506/probability_statistics_curriculum_literature/releases/tag/probstat-full-20261029

## 1. 未发布的资料（仍保存在本机资料库中）

下列资料的许可声明明确限制为个人使用、禁止再分发或仅供本校学生使用，公开发布会超出许可范围，因此**没有放进 Release，也没有放进 Git 分支**。它们在 `catalog_cn.csv` 中仍有登记，解压后对应路径下没有文件。明细见 `release_excluded_cn.csv`。

| 编号 | 资料 | 许可声明（摘自 catalog_cn.csv） |
|---|---|---|
| S06-01 | Stata 19 手册（`software_docs/StataCorp_Stata19_Manuals_GSW_U_R_en/`） | StataCorp 保留全部权利，手册禁止复制 |
| S06-02 | SAS/STAT 15.4 用户指南选章（`software_docs/SAS_STAT_15.4_UsersGuide_SelectedChapters_en/`） | SAS Institute 保留全部权利 |
| S06-03 | IBM SPSS Statistics 27.0.1 手册（`software_docs/IBM_SPSS_Statistics_27.0.1_Manuals_en/`） | 仅供个人学习留存，勿再分发 |
| A03-03 | Norris《Probability》剑桥 Part IA 讲义 | 仅供 Tripos 学生使用 |
| B01-05 | Boyd & Vandenberghe《Introduction to Applied Linear Algebra》 | 作者主页免费公开，供个人使用 |
| B02-03 | Boyd & Vandenberghe《Convex Optimization》 | 作者主页免费公开，供个人使用 |
| B07-03 | Efron & Hastie《Computer Age Statistical Inference》 | for personal use only |
| B09-01 | Gelman, Hill & Vehtari《Regression and Other Stories》 | 仅供个人阅读，不得再分发 |
| B13-04 | Särkkä & Svensson《Bayesian Filtering and Smoothing》第 2 版 | 仅限个人浏览下载，不得再分发 |

这些资料都可以从原始来源免费获取，下载地址见 `catalog_cn.csv` 的“下载地址”列。

另外，许可声明为“仅限非商业用途”的资料（例如《Bayesian Data Analysis》第 3 版、《Bayesian Workflow》）没有禁止再分发，已照常发布。

## 2. 包列表

包按路径顺序切分，内容范围如下（文件名前缀都是 `probability_statistics_curriculum_literature_20261029_`，后缀都是 `_cn_en.tar`）：

| 包 | 内容范围（按路径顺序） |
|---|---|
| `batch001` | 根目录报告与登记表、`scripts/`，以及 `books/` 的大部分（到 The Turing Way 的一部分） |
| `batch002` | `books/` 其余部分、`courses/`，以及 `curricula/` 的前一部分（到 Harvard 生物统计 SM 培养方案的一部分） |
| `batch003` | `curricula/` 其余部分、`guides/`、`papers/`，以及 `practice/` 的开头部分（到 Data Science in a Box 的一部分） |
| `batch004` | `practice/` 中间部分（Data Science in a Box 其余部分，到 UMich STATS 531 的一部分） |
| `batch005` | `practice/` 其余部分（含 `practice/cases/` 案例）、`software_docs/` |

每个文件属于哪个包，见 `archive_index_cn.csv`。它是 UTF-8 带 BOM 编码，可直接用 Excel 打开，共 31,139 行，每行一个文件。

- 每个包都可以**单独解压**，不需要拼接。
- 包之间**没有重复文件**，解压到同一目录时不会互相覆盖。
- 包没有压缩，所需磁盘空间约等于包的大小。全部解压约需 **7.1 GiB**。

## 3. Windows：浏览器下载

1. 打开上面的 Release 页面，展开 **Assets**。
2. 依次点击 5 个 `.tar` 文件，以及 `archive_index_cn.csv`、`windows_rename_map_cn.csv`、`release_excluded_cn.csv`、`download_restore_cn.md`、`upload_report_cn.md`，全部保存到**同一个下载文件夹**，例如 `D:\下载\probstat\`。
3. 单个包最大约 1.5 GB。浏览器提示“是否保留”时选择保留。下载中断时，可以在浏览器的下载列表里点“恢复”，或重新下载。
4. 对照 `upload_report_cn.md` 中的字节数，核对每个包的大小。在文件属性窗口里看“大小”一项的字节数，不要看“占用空间”。

## 4. Windows：WinRAR 解压（全部解压到同一个目标目录）

请使用 **WinRAR 6 或更新版本**。**目标目录必须用短路径**，例如 `D:\probstat\`，见下面的长路径说明。

1. 在下载文件夹中，按住 Ctrl 选中 5 个 `.tar` 文件。
2. 右键 → **WinRAR → 解压文件…**（Extract files…）。
3. “目标路径”填 `D:\probstat\`。
4. **不要**勾选“解压到单独的文件夹 / 在子文件夹中解压”（Extract archives to subfolders）。
5. 点确定。

也可以逐个解压：每个包都右键 → WinRAR → **解压文件…**，目标路径都填同一个 `D:\probstat\`。不要用“解压到 probability_statistics_curriculum_literature_20261029_batch00X_cn_en\”这个菜单项：它会给每个包各建一个子文件夹，目录结构就被拆散了，而且文件夹名很长，会让路径超出 Windows 的限制。

解压后的目录结构：

```
D:\probstat\
├─ README_cn.md、catalog_cn.csv、progress_cn.csv、download_failures_cn.csv、search_log_cn.md
├─ books\ courses\ curricula\ papers\ practice\ software_docs\
├─ guides\
└─ scripts\
```

### Windows 兼容处理

发布包里的文件名都已经处理过，在 Windows 下解压不会因为文件名报错。资料库的本地原件没有改动，每一处改名和改写都逐条记在 `windows_rename_map_cn.csv` 里。

- **文件名带 Windows 不允许的字符（371 个）**：主要是网页离线镜像里形如 `style.css?ver=…`、`js_….js?scope=footer&…` 的样式和脚本文件，集中在 `curricula/` 的大学培养方案网页和若干网页版教材、软件文档中。
  - 名字里的 `?` 等字符改成 `_`。
- **路径过长（169 个名字截短）**：
  - 有些网页镜像的文件名本身就长达一两百个字符，有些课程仓库（例如 `practice/CetinkayaRundel_DataScienceInABox_repo_en/`）目录很深，最长相对路径达 349 个字符。
  - 在超过 165 个字符的路径里，最长的那一级名字被截短为“前 12 个字符 + 原名的 8 位哈希”，例如 `u4-d05-more-_6fcc3c7a`。同一资料内同名的目录统一改成同一个新名字。
  - 涉及 152 个文件和若干目录，目录改名连带其下的 383 个文件路径变化。
- **同一目录下只差大小写的名字（10 处）**：都在 CDC NHANES 教程镜像（`practice/cases/CDC_NHANES_Tutorials_SurveyAnalysis_html_en/`）中，包括 2 个目录（`NCHS`/`nchs`、`Images`/`images`）和 8 个网页（例如 `Weighting.aspx.html`/`weighting.aspx.html`）。在 Windows 下它们会互相覆盖，因此小写的那个加了 `_case2` 后缀，例如 `nchs_case2`。
- **页面引用同步改写**：381 个网页、样式表、JSON、Markdown 等文本文件中，指向这些改名文件的链接已同步改写，离线打开时仍能正常显示。改写时会逐条核对：只有确实指向已改名文件的链接才会改，其他同名路径不受影响。改写前后全库的本地网页链接都核对过，失效链接没有增加。
- **SciPy 1.18.0 文档 `.zip`**：包内有 2 个只差大小写的文件，已在发布包中重新打包，加了 `_case2` 后缀，引用的 9 个网页同步改写。其余 39 个内层归档已逐个检查，没有改动。
- **长路径**：处理后，第一层最长相对路径为 204 个字符，都在 Data Science in a Box 课程仓库里。这些路径的每一级名字都已经很短，无法再缩短。解压到 `D:\probstat\` 这类短目录时，完整路径不超过 260 个字符。

## 5. Linux / macOS

```bash
mkdir -p ~/probstat
for f in probability_statistics_curriculum_literature_20261029_batch*_cn_en.tar; do tar -xf "$f" -C ~/probstat || echo "FAILED: $f"; done
```

## 6. 资料状态说明（来自资料库自身的报告，与打包无关）

- **只计已核验条目**：全库去重共 917 项，包括：
  - 教材 74、课程讲义 57、实践 50；
  - 论文 652（近三年占 90.8%）；
  - 案例 25、软件文档 34、培养方案 25。

  详见 `README_cn.md` 和 `catalog_cn.csv`。其中 9 项属于第 1 节的未发布资料（3 套软件手册、5 本教材、1 份讲义）。
- **失败、残缺、待核实和排除项**：记录在 `download_failures_cn.csv`，不计入，也没有对应文件。例如 conda 文档受限流影响未取得。
- **快照时间**：本次按 2026-10-29 22:25（中欧时间）的资料库内容打包。打包前先把整个资料库复制成一份快照，打包用的就是这份快照。资料库最后一次写入是在 22:16。

## 7. 完整性说明

- 本次发布只登记了上传状态：GitHub API 显示附件为 `uploaded`，且远端大小等于本地大小。**没有**做下载回验和哈希校验。
- `catalog_cn.csv` 的 SHA256 列是下载当时记录的值。改名或改写过的文件，以发布包中的为准。
- 除第 1 节的未发布资料外，资料库中的资料文件都已打包。另外只排除了以下不属于资料的内容：
  - 本地 `.git/`，约 2.6 MB；
  - `scripts/__pycache__/` 中的 3 个 `.pyc`；
  - 一个编辑器备份文件 `practice/BerkeleySCF_TutorialParallelization_repo_en/_layouts/default.html~`。
- 4 个 `poetry.lock`、`renv.lock` 是项目依赖锁文件，属于资料内容，已打包。
