# 教材、课程、实践、案例、软件文档与培养方案规范

库根目录 LIB=`/root/probability_statistics_curriculum_literature`。命令在 LIB 下运行，Python 一律 `python3 -I`。
下载核验脚本：`scripts/materials_en.py`（先读其文档字符串，了解 kind：pdf / pdfs / zip / html / reuse / git）。
检索日 2026-10-29。只收合法公开全文；不绕过付费墙、登录、表单或访问限制；不下载视频、商业软件本体、独立大型数据集；不收非公开考试题或教师专用答案。不运行下载的任何代码。

## 每个课程群的目标
- **B 教材/专著/参考书 3–5 本**：作者或出版社官方免费全文（作者主页 PDF、开放获取图书、CC 许可在线书）。区分 `rigor`：`严格理论`（定义-定理-证明为主）/ `应用入门` / `兼顾`。优先最新适用版本；经典教材允许。分章节公开的书必须核对目录，用 `pdfs`（全部章节 URL）或 `html`（全部章节页）保存全部正文，整本计一次；只有试读章节、样章、目录的不计。
- **A 大学官方课程及完整讲义 2–4 套**：只计完整资料——完整文字讲义（全部讲次 notes 或整本讲义 PDF）、完整课件包（全部讲次 slides）、OCW 官方整门课程压缩包。只有大纲/视频/阅读清单的不计；只有课件的标 `完整课件包`，不冒充文字教材。
  - `pdfs` + `index_url` + `link_regex` 从官方日程页抓全部讲次 PDF；`min_files` 设为页面实际讲次数（先人工看页面确认）。
  - MIT OCW 整门课程包：课程页 `/download` 下的官方 zip，用 `zip`；设 `max_mb`（默认 600，含视频的大包不要）。
- **D 配套习题、实验或公开实践材料 2–5 套**：公开作业/习题集（含合法公开的解答）、实验说明、官方教程仓库、模拟检验与理论现象演示等。官方仓库用 `git`（记录 commit，`max_mb` 默认 150）。
- 同一课程不同学期只收一个；同一书不同版本只收一个。
- 兄弟库已核验资料可复用：`kind: "reuse"`，`src`（源绝对路径）、`src_lib`、`src_id`。可复用清单 `scripts/annotations/sibling_reusable_cn.csv`。复用不算新下载，但计入本库去重总数。
- 中文资料：有合法公开的高质量中文课程讲义/教材也收（`lang: "cn"`），不强求。

## 清单文件与字段
只写自己的分片文件（分片名由主会话指定）：`scripts/seeds/materials/<set>_<分片>_cn.json`，set ∈ books / courses / practice / cases / software / curricula。JSON 列表，列表顺序 = 群内建议阅读顺序。每条：
- 公共：
  - `mid`：书 `B<群>-<两位序号>`（B07-01）、课程 `A<群>-NN`、实践 `D<群>-NN`、案例 `E<领域号>-NN`、软件 `S<类号>-NN`、培养方案 `P-NN`。
  - `group`（主课程群 "07"；案例/软件/培养方案可写相关群）、`related`（列表）、`kind`、`name`（文件/目录名主体，不含语言后缀与扩展名，如 `Durrett_ProbabilityTheoryAndExamples_5th`、`MIT_18650_2016Fall_OCW`；脚本自动加 `_en`）、`lang`（en / cn / cn_en …）。
  - `title`、`authors`（作者或教师；课程填教师）、`institution`（学校或出版社）、`code`（课程代码）、`term`（课程学年/学期）或 `edition`、`orig_year`、`edition_year`、`page_updated`（网页更新时间，如能查到）、`identifier`（ISBN/DOI/arXiv/OCW 编号等）。
  - `level`：`本科` / `本科高年级` / `硕士` / `博士`（可写 `本科高年级/硕士`）；依据官方课程目录或课程页面。
  - `requirement`：`核心` / `选修` / `专业方向` / `先修`；`prereq`（先修要求，依据课程官网）。
  - `track`（专业方向，如 `概率论` / `数理统计` / `应用统计` / `生物统计` / `计量经济` …）。
  - `rigor`（见上）、`difficulty`（入门 / 中级 / 高级）、`programming`（编程要求：无 / R / Python / R+Python / Stan / SAS …）、`use`（学习用途：通读教材 / 按需参考 / 课程配套 / 习题练习 / 项目实战）。
  - `syllabus_url`（官方大纲或主页）、`syllabus_note`（大纲要点，中文 1–2 句）、`reason`（选入理由）、`summary`（简介，注明依据）、`summary_basis`、`license`（依据页面或 LICENSE；未声明写"未声明许可证"）。
  - 书另加 `exercises`（是否含习题：有 / 无 / 有（含部分解答））、`toc_check`（分章节书写清目录核对结果）。
  - 课程另加 `pack_type`（完整文字讲义 / 完整课件包 / 讲义+课件 / OCW 官方课程包）。
  - 实践另加 `learning_goals`、`environment`（语言/软件要求）、`practice_type`（模拟演示 / 方法比较 / 回归诊断 / 贝叶斯计算 / 时间序列预测 / 实验与调查 / 因果分析 / 生存与纵向 / 综合项目 / 习题集）。
  - 案例另加：`domain`（生物医学 / 经济金融 / 工业 / 环境水文 / 社会调查 / 公共政策）、`question`（研究问题）、`data_type`、`stat_task`、`methods`、`software`、`code_open`、`data_open`、`data_source`、`data_license`、`data_access`（获取方式）、`data_size`、`workflow`（该资料实际覆盖的分析流程环节：问题/数据/目标/假设/方法/诊断/不确定性/敏感性/解释，逐项写有/无，依据 README 或报告目录）、`reproducibility`（可复现条件）。
  - 软件文档另加：`project`、`version`（文档对应版本，依据页面）、`owner`（官方归属，如 R Core / NumFOCUS / Stan Dev Team / SAS Institute）、`maintenance`（维护状态：活跃 / 维护中 / 停止维护，依据最近发布日期）、`doc_scope`（用户指南 / 参考手册 / 教程 / 方法说明）。
  - 培养方案另加：`program`（项目名称）、`degree`（学士 / 硕士 / 博士）、`year`（适用学年）、`courses_note`（核心/选修课程及先修关系要点，中文）。
- kind 参数：`url` / `urls` / `index_url` + `link_regex` + `min_files` / `min_pages` / `min_pages_each` / `title_phrase` / `skip_regex` / `min_chars` / `allow_short` / `extra_pages` / `repo` + `ref` + `must_contain` + `max_mb` / `min_pdfs` / `min_html` / `src`。
- 被排除的条目保留在清单里加 `"exclude": true, "exclude_reason": "..."`（作为失败记录进报告）。

## 流程
1. 逐群查官方页面（WebFetch / curl 看结构，确认讲次数、链接规律、版本、许可证）。HTTP 请求要节制。
2. 写清单 → `python3 -I scripts/materials_en.py fetch <set> --only <mid>[,<mid>...]`（**必须带 --only，只跑自己的条目**）→ 看结果。失败就换合法来源或换资料。
3. 每群达到 B≥3、A≥2、D≥2 核验通过后再做下一群；做不到的写入 `scripts/annotations/materials_gap_<分片>_cn.md`。
4. 不要修改 `scripts/*.py`、他人分片、兄弟库目录；不要动 `papers/`。一个 PDF 是否真为目标资料（标题、作者、版本、正文完整）用 `title_phrase` 和页数下限把关；对不确定的，手动抽查首页文字（pypdf 在 `/root/.cache/pscl_lit/pylib`）。
5. 磁盘：单个资料一般不超过 600 MB；整片合计尽量不超过 6 GB。

## 回报（给主会话）
每群一行：B / A（完整文字讲义 / 完整课件包 / OCW 包）/ D 核验通过数（其中复用数）、失败数；额外区域（案例/软件/培养方案）的条目数；缺口文件路径；需要主会话注意的问题。不要贴清单全文。
