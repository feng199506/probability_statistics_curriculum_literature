"""Resolve cross-group paper duplicates after seeds changed.

  python3 -I scripts/reconcile_claims_en.py [--apply]

A paper counts only in the lowest-numbered group whose seed list contains it (papers_en.all_claims).
A state record in any other group (ok / pending / fail) is turned into 'dup_elsewhere'; its file is
moved out of the library to <WORK>/crossdup/ (not deleted). Afterwards rerun
`papers_en.py download NN` for affected groups: the claiming group fetches the paper if it does not
have it yet, and groups that fell below target are topped up from their reserves.
Dry run unless --apply.
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import CATS, ROOT, WORK, load, save  # noqa: E402
import papers_en as P  # noqa: E402


def main(apply):
    claims = P.all_claims()
    out = WORK / "crossdup"
    for c in CATS:
        st = load(P.state_path(c), {})
        changed = False
        for k, rec in st.items():
            owner = claims.get(k)
            if rec["status"] == "dup_elsewhere" or owner == c:
                continue
            print(f"{c}: {k} [{rec['status']}] -> claimed by {owner}  {rec.get('path', '')}")
            if not apply:
                continue
            if rec.get("path") and (ROOT / rec["path"]).exists():
                out.mkdir(parents=True, exist_ok=True)
                shutil.move(str(ROOT / rec["path"]), out / Path(rec["path"]).name)
            why = f"已由 {owner} 群收录，本群不重复计数" if owner else "种子已移除该条"
            st[k] = {"status": "dup_elsewhere", "note": f"{why}（种子调整后对账移出）",
                     "moved_to": str(out)}
            changed = True
        if changed:
            save(P.state_path(c), st)


if __name__ == "__main__":
    main("--apply" in sys.argv)
