"""Write README_cn.md (library report) from catalog_cn.csv, download_failures_cn.csv and progress_cn.csv.

  python3 -I scripts/build_readme_en.py
Run after build_catalog_en.py. Prose that is not computed lives in scripts/readme_notes_cn.md and is
inserted verbatim under "说明与缺口".
"""
import csv
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import CATS, ROOT, SCRIPTS, SEARCH_DATE, WINDOW_START, WINDOW_END  # noqa: E402

KIND = [("教科书", "教材"), ("大学官方课程", "课程讲义"), ("习题/实验", "实践"), ("论文/", "论文"),
        ("专业应用案例", "案例"), ("统计软件", "软件文档"), ("培养方案", "培养方案")]


def kind(r):
    for k, v in KIND:
        if r["资料类型"].startswith(k):
            return v
    return "其他"


def main():
    rows = list(csv.DictReader(open(ROOT / "catalog_cn.csv", encoding="utf-8-sig")))
    fails = list(csv.DictReader(open(ROOT / "download_failures_cn.csv", encoding="utf-8-sig")))
    tot = Counter(kind(r) for r in rows)
    reuse = [r for r in rows if r["来源性质"] == "已有复用"]
    per = defaultdict(Counter)
    for r in rows:
        per[r["课程群"]][kind(r)] += 1
    rec = defaultdict(Counter)
    years = Counter()
    for r in rows:
        if kind(r) == "论文":
            rec[r["课程群"]][r["时间窗口"]] += 1
            years[r["首次公开日期"][:4]] += 1
    du = subprocess.run(["du", "-sh", "--exclude=scripts", str(ROOT)], capture_output=True, text=True).stdout.split()[0]
    L = []
    L.append("# 概率与统计课程文献库（本科—硕士—博士）\n")
    L.append(f"检索与下载日：{SEARCH_DATE}。库路径：`{ROOT}`（不含 scripts 约 {du}）。只计已完整下载并通过内容核验的资料；"
             "失败、残缺、待核实、排除项见 `download_failures_cn.csv`。本轮未做整库 SHA256 扫描或下载回验（SHA256 列为下载当时记录的值）；"
             "未运行任何案例代码、未安装依赖、未上传。\n")
    L.append("## 一、总量（全库按独立资料去重）\n")
    L.append("| 资料类型 | 已核验 | 其中已有复用 |\n|---|---|---|")
    for _, v in KIND:
        L.append(f"| {v} | {tot[v]} | {sum(1 for r in reuse if kind(r) == v)} |")
    L.append(f"| **合计** | **{len(rows)}** | **{len(reuse)}**（本轮新下载 {len(rows) - len(reuse)}） |\n")
    L.append("复用来源：工业过程监控库、时间序列库（复制并重新核验，原库文件未移动或删除；原库编号见 catalog 的“复用来源”列）。"
             "原计划复用的机器学习/深度学习库在本轮执行期间已不在本机，相关资料改从官方来源直接下载。\n")
    L.append("## 二、各课程群数量\n")
    L.append("目标：教材 3–5、课程讲义 2–4、实践 2–5；研究型群论文 30–50（01–03、19 以教材为主，不设论文目标）。"
             "跨群资料只在主群计一次，通过“关联课程群”列引用。\n")
    L.append("| 课程群 | 教材 | 课程讲义 | 实践 | 论文 | 论文近三年占比 | 三年前经典 |\n|---|---|---|---|---|---|---|")
    for c, (slug, name, *_rest) in CATS.items():
        k = per[c]
        n = sum(rec[c].values())
        share = f"{rec[c]['近三年'] / n:.1%}" if n else "—"
        old = n - rec[c]["近三年"] if n else 0
        L.append(f"| {c} {name} | {k['教材']} | {k['课程讲义']} | {k['实践']} | {k['论文'] or '不设'} | {share} | {old if n else '—'} |")
    allp = sum(sum(v.values()) for v in rec.values())
    allr = sum(v["近三年"] for v in rec.values())
    L.append(f"\n论文合计 {allp} 篇，近三年（首次公开 {WINDOW_START} 至 {WINDOW_END}）{allr} 篇，占 {allr / max(1, allp):.1%}；"
             "三年前条目均为必要经典，理由见 catalog 的“三年前或经典保留理由”列。\n")
    L.append("### 专业区\n")
    doms = Counter(r["编号"][:2] for r in rows if kind(r) == "案例")
    names = {"E1": "生物医学", "E2": "经济金融", "E3": "工业", "E4": "环境水文", "E5": "社会调查", "E6": "公共政策"}
    L.append("| 案例领域 | 已核验 |\n|---|---|")
    for d, nm in names.items():
        L.append(f"| {d} {nm} | {doms[d]} |")
    sw = Counter(r["编号"][:3] for r in rows if kind(r) == "软件文档")
    swn = {"S01": "R 基础/数据处理/可视化/报告", "S02": "Python 科学栈", "S03": "贝叶斯与概率编程",
           "S04": "混合模型/生存/调查/时间序列/空间", "S05": "Quarto/Jupyter/Git/测试/环境", "S06": "SAS/Stata/SPSS 公开手册"}
    L.append("\n| 软件类别（按项目+版本计） | 已核验 |\n|---|---|")
    for d, nm in swn.items():
        L.append(f"| {d} {nm} | {sw[d]} |")
    deg = Counter()
    for r in rows:
        if kind(r) == "培养方案":
            deg[r["学位层次"]] += 1
    L.append("\n培养方案按学位层次：" + "，".join(f"{k} {v}" for k, v in sorted(deg.items())) + "。\n")
    L.append("## 三、层次与理论/应用覆盖（教材、课程、实践）\n")
    lv, rg = Counter(), Counter()
    for r in rows:
        if kind(r) in ("教材", "课程讲义", "实践"):
            s = r["学位层次"]
            for tag in ("本科", "硕士", "博士"):
                if tag in s:
                    lv[tag] += 1
            rg[r["理论严格度"] or "未标注"] += 1
    L.append("学位层次（一条可跨多个层次）：" + "，".join(f"{k} {lv[k]}" for k in ("本科", "硕士", "博士")) + "。")
    L.append("理论严格度：" + "，".join(f"{k} {v}" for k, v in rg.most_common()) + "。")
    pt = Counter(r["资料包类型"] for r in rows if kind(r) == "课程讲义")
    L.append("课程资料包类型：" + "，".join(f"{k} {v}" for k, v in pt.most_common()) + "。")
    pr = Counter(r["资料包类型"] for r in rows if kind(r) == "实践")
    L.append("实践类型：" + "，".join(f"{k} {v}" for k, v in pr.most_common()) + "。\n")
    L.append("## 四、论文年份分布（按首次公开年）\n")
    L.append("| 年份 | 篇数 |\n|---|---|")
    for y in sorted(years):
        L.append(f"| {y} | {years[y]} |")
    L.append("\n## 五、失败、残缺、待核实与排除\n")
    fs = Counter((f["资料类型"], f["状态"]) for f in fails)
    L.append("| 资料类型 | 状态 | 条数 |\n|---|---|---|")
    for (t, s), n in sorted(fs.items()):
        L.append(f"| {t} | {s} | {n} |")
    L.append("\n逐条原因见 `download_failures_cn.csv`。论文失败多为短篇笔记未达自动核验阈值（<4 页、<12000 字符或无参考文献节），由同群后备补位；“已排除”为跨区重复、超出大小上限或内容重复的主动排除；“人工拒收”为与教材重复的论文副本。\n")
    notes = SCRIPTS / "readme_notes_cn.md"
    if notes.exists():
        L.append(notes.read_text())
    (ROOT / "README_cn.md").write_text("\n".join(L) + "\n")
    print("README_cn.md written:", len(rows), "rows")


if __name__ == "__main__":
    main()
