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
