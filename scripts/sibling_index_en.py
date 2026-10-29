"""List verified non-paper items (books, course packs, OCW zips) of sibling libraries that may be reused.

  python3 -I scripts/sibling_index_en.py   -> scripts/annotations/sibling_reusable_cn.csv
Read-only on sibling libraries. Only rows whose local file/dir exists are listed.
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import ANNOT  # noqa: E402

LIBS = [  # lib, id col, type col, title col, author col, path col, keep types (substring)
    ("machine_learning_deep_learning_literature", "文献编号", "资料类型", "标题", "作者或教师", "本地路径", ("教科书", "课程")),
    ("industrial_process_monitoring_literature", "文献编号", "资料类型", "标题", "作者", "本地相对路径", ("书籍", "课程")),
]


def main():
    out = []
    for lib, idc, tc, tic, auc, pc, keep in LIBS:
        base = Path("/root") / lib
        if not (base / "catalog_cn.csv").exists():
            continue
        for r in csv.DictReader(open(base / "catalog_cn.csv", encoding="utf-8-sig")):
            if not any(k in r[tc] for k in keep):
                continue
            p = base / r[pc]
            if r[pc] and p.exists():
                out.append([lib, r[idc], r[tc], r[tic], r[auc][:60], str(p)])
    ANNOT.mkdir(parents=True, exist_ok=True)
    with open(ANNOT / "sibling_reusable_cn.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["源库", "源编号", "资料类型", "标题", "作者或教师", "源路径"])
        w.writerows(out)
    print(len(out), "rows")


if __name__ == "__main__":
    main()
