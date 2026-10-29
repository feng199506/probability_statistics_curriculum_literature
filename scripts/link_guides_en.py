"""Expand guide drafts (scripts/guide_src/*.md) into guides/*.md with verified ids and local paths.

  python3 -I scripts/link_guides_en.py

Markers in drafts:
  〔B03-01〕            -> B03-01《title》（local link）; the id must be a verified row of catalog_cn.csv
  〔PAPERS:08:10〕      -> table of up to 10 verified papers of group 08, surveys/tutorials first,
                         then other papers, each in seed (reading) order
  〔PAPERS:08:10:all〕  -> same but in pure seed order regardless of type
  〔COUNT:books:07〕    -> number of verified catalog rows of that set (books/courses/practice/papers/
                         cases/software/curricula) in that group ("*" = all groups)
Run after build_catalog_en.py. Unknown or unverified ids abort the run (nothing is written).
"""
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import ROOT, SCRIPTS  # noqa: E402

SRC = SCRIPTS / "guide_src"
OUT = ROOT / "guides"
SETMAP = {"books": "教科书", "courses": "大学官方课程", "practice": "习题/实验", "cases": "专业应用案例",
          "software": "统计软件", "curricula": "培养方案", "papers": "论文/"}


def load_catalog():
    rows = list(csv.DictReader(open(ROOT / "catalog_cn.csv", encoding="utf-8-sig")))
    return {r["编号"]: r for r in rows}, rows


def link(r):
    paths = [p for p in r["本地路径"].split("; ") if p]
    p = paths[0] if paths else ""
    extra = f" 等 {len(paths)} 项" if len(paths) > 1 else ""
    tag = " / ".join(x for x in (r["学位层次"], r["理论严格度"]) if x)
    return f"{r['编号']}《{r['标题']}》（{tag}；[{p}](../{p}){extra}）" if p else f"{r['编号']}《{r['标题']}》"


def papers(rows, grp, n, mode):
    ps = [r for r in rows if r["资料类型"].startswith("论文") and r["课程群"] == grp]
    ps.sort(key=lambda r: r["编号"])
    if mode != "all":
        first = [r for r in ps if any(t in r["资料类型"] for t in ("综述", "学术教程"))]
        ps = first + [r for r in ps if r not in first]
    ps = ps[:n]
    out = ["| 编号 | 类型 | 首次公开 | 标题 | 本地文件 |", "|---|---|---|---|---|"]
    for r in ps:
        t = r["标题"].replace("|", "/")
        out.append(f"| {r['编号']} | {r['资料类型'][3:]} | {r['首次公开日期']} | {t} | [PDF](../{r['本地路径']}) |")
    return "\n".join(out) if ps else "（本群暂无已核验论文）"


def main():
    cat, rows = load_catalog()
    bad = []
    outs = {}
    for src in sorted(SRC.glob("*_cn.md")):
        txt = src.read_text()

        def sub(m):
            tok = m.group(1)
            if tok.startswith("PAPERS:"):
                parts = tok.split(":")
                return papers(rows, parts[1], int(parts[2]), parts[3] if len(parts) > 3 else "")
            if tok.startswith("COUNT:"):
                _, s, g = tok.split(":")
                return str(sum(1 for r in rows if r["资料类型"].startswith(SETMAP[s]) and (g == "*" or r["课程群"] == g)))
            if tok not in cat:
                bad.append(f"{src.name}: {tok}")
                return tok
            return link(cat[tok])
        outs[src.name] = re.sub(r"〔([^〕]+)〕", sub, txt)
    if bad:
        print("UNKNOWN/UNVERIFIED IDS:\n  " + "\n  ".join(bad))
        sys.exit(1)
    OUT.mkdir(exist_ok=True)
    for name, txt in outs.items():
        (OUT / name).write_text(txt)
    print(f"{len(outs)} guides written to guides/")


if __name__ == "__main__":
    main()
