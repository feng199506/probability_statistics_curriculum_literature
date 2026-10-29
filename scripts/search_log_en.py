"""Write search_log_cn.md from the query files, candidate caches and paper / material states.

  python3 -I scripts/search_log_en.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import ANNOT, CACHE, CATS, ROOT, SEEDS, SEARCH_DATE, WINDOW_START, WINDOW_END, load  # noqa: E402
import papers_en as P  # noqa: E402


def main():
    out = [f"# 检索日志\n\n检索日：{SEARCH_DATE}；论文近三年窗口：首次公开 {WINDOW_START} 至 {WINDOW_END}。",
           "论文检索走 arXiv API（检索式见下，日期窗口由脚本追加；标 old 的为经典检索不加窗口），候选经人工筛选写入种子，"
           "非 arXiv 开放全文（出版方/PMC/JSS 等）由人工核对后加入。教材、课程、实践、案例、软件文档与培养方案通过官方页面人工检索，"
           "来源 URL 记录在 catalog_cn.csv 与 download_failures_cn.csv。\n"]
    for c in CATS:
        qs = load(SEEDS / "queries" / f"{c}_en.json", [])
        if not qs:
            continue
        cands = load(CACHE / "candidates" / f"{c}_en.json", {})
        ss = P.seeds(c)
        st = load(P.state_path(c), {})
        ok = sum(1 for v in st.values() if v["status"] == "ok")
        out.append(f"\n## {c} {CATS[c][1]}\n\n候选 {len(cands)} 条 → 种子 {len(ss)} 条（主列表 "
                   f"{sum(1 for s in ss if not s.get('reserve'))}，后备 {sum(1 for s in ss if s.get('reserve'))}）→ 核验通过 {ok} 条。\n")
        out.append("| 子主题 | 检索式 |\n|---|---|")
        for q in qs:
            out.append(f"| {q.get('subtopic', '')} | `{q['q']}`{'（经典，不限日期）' if q.get('old') else ''} |")
    gaps = sorted(ANNOT.glob("*gap*_cn.md"))
    if gaps:
        out.append("\n## 缺口说明文件\n")
        out += [f"- scripts/annotations/{g.name}" for g in gaps]
    (ROOT / "search_log_cn.md").write_text("\n".join(out) + "\n")
    print("search_log_cn.md written")


if __name__ == "__main__":
    main()
