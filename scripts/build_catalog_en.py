"""Build catalog_cn.csv, progress_cn.csv, download_failures_cn.csv and search_log_cn.md for PSCL.

  python3 -I scripts/build_catalog_en.py

Inputs: seeds (scripts/seeds/...), per-item state (scripts/state/...), arXiv metadata cache.
Paper ids are stable: scripts/state/id_map.json maps item key -> C<group>-<nnn> once assigned.
Only items whose state is verified/ok are catalogued as complete; failed / partial / pending /
excluded items go to download_failures_cn.csv. Duplicates are detected from the sha256 values
recorded at download time (no re-hashing of the library).
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common_en import CATS, ROOT, SEEDS, STATE, WINDOW_START, WINDOW_END, load, save, window_status  # noqa: E402
import papers_en as P  # noqa: E402
import materials_en as M  # noqa: E402

COLS = ["编号", "课程群", "关联课程群", "专业方向", "学位层次", "课程属性", "资料类型", "资料包类型", "标题", "作者或教师",
        "学校或出版社", "课程代码", "学期或版本", "原著年份", "版本年份", "首次公开日期", "首次公开依据", "时间窗口",
        "三年前或经典保留理由", "网页更新时间", "语言", "标识符", "原始来源", "下载地址", "本地路径", "完整性",
        "核验说明", "来源性质", "复用来源", "许可证", "先修要求", "理论严格度", "理论难度", "编程要求", "习题", "学习用途",
        "大纲要点", "选入理由", "简介", "简介依据",
        # cases
        "应用领域", "研究问题", "数据类型", "统计任务", "方法", "所用软件", "代码公开", "数据公开", "数据来源",
        "数据许可证", "数据获取方式", "数据规模", "分析流程覆盖", "可复现条件",
        # software
        "软件项目", "文档版本", "官方归属", "维护状态", "文档范围",
        # curricula
        "项目名称", "学位", "适用学年", "课程与先修要点", "SHA256（下载时记录）"]

TYPE = {"books": "教科书/专著/参考书", "courses": "大学官方课程与讲义", "practice": "习题/实验/实践材料",
        "cases": "专业应用案例", "software": "统计软件官方文档", "curricula": "培养方案与课程目录"}
TARGET = {"books": (3, 5), "courses": (2, 4), "practice": (2, 5)}
PAPER_GROUPS = ["04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "20"]
CASE_DOMAINS = {"E1": "生物医学", "E2": "经济金融", "E3": "工业", "E4": "环境水文", "E5": "社会调查", "E6": "公共政策"}


def j(v):
    if isinstance(v, list):
        return "; ".join(str(x) for x in v)
    if isinstance(v, dict):
        return json.dumps(v, ensure_ascii=False)
    return "" if v is None else str(v)


def mat_rows():
    rows, fails = [], []
    for s in M.SETS:
        for it in M.manifest(s):
            r = load(M.res_path(it["mid"]), {})
            st = r.get("status")
            if it.get("exclude") or st != "verified":
                why = it.get("exclude_reason") if it.get("exclude") else (r.get("note") or "未运行下载")
                fails.append({"编号": it["mid"], "课程群": it.get("group", ""), "资料类型": TYPE[s], "标题": it.get("title", ""),
                              "状态": "已排除" if it.get("exclude") else ("下载失败/核验未通过" if st == "failed" else "待核验"),
                              "原因": why, "来源": it.get("url") or it.get("index_url") or it.get("repo") or it.get("src", "")})
                continue
            files = r.get("files", [])
            reuse = r.get("reuse") or it.get("kind") == "reuse"
            row = {
                "编号": it["mid"], "课程群": it.get("group", ""), "关联课程群": j(it.get("related")),
                "专业方向": it.get("track", "") or it.get("domain", ""), "学位层次": it.get("level", it.get("degree", "")),
                "课程属性": it.get("requirement", ""), "资料类型": TYPE[s], "资料包类型": it.get("pack_type", it.get("practice_type", it.get("doc_scope", ""))),
                "标题": it.get("title", ""), "作者或教师": j(it.get("authors", it.get("instructors", ""))),
                "学校或出版社": it.get("institution", it.get("owner", "")), "课程代码": it.get("code", ""),
                "学期或版本": it.get("term") or it.get("edition") or it.get("version", ""),
                "原著年份": it.get("orig_year", ""), "版本年份": it.get("edition_year", it.get("year", "")),
                "网页更新时间": it.get("page_updated", ""), "语言": it.get("lang", "en"), "标识符": it.get("identifier", ""),
                "原始来源": it.get("syllabus_url") or it.get("landing") or it.get("repo") or it.get("index_url") or it.get("url", ""),
                "下载地址": it.get("url") or it.get("index_url") or it.get("repo") or "; ".join(it.get("urls", [])[:3]),
                "本地路径": "; ".join(f["path"] for f in files), "完整性": "完整（核验通过）",
                "核验说明": r.get("note", ""), "来源性质": "已有复用" if reuse else "本轮新下载",
                "复用来源": f"{it.get('src_lib', '')} {it.get('src_id', '')}".strip() if reuse else "",
                "许可证": it.get("license", ""), "先修要求": it.get("prereq", ""), "理论严格度": it.get("rigor", ""),
                "理论难度": it.get("difficulty", ""), "编程要求": it.get("programming", it.get("environment", "")),
                "习题": it.get("exercises", ""), "学习用途": it.get("use", it.get("learning_goals", "")),
                "大纲要点": it.get("syllabus_note", it.get("courses_note", "")), "选入理由": it.get("reason", ""),
                "简介": it.get("summary", ""), "简介依据": it.get("summary_basis", ""),
                "应用领域": it.get("domain", ""), "研究问题": it.get("question", ""), "数据类型": it.get("data_type", ""),
                "统计任务": it.get("stat_task", ""), "方法": j(it.get("methods", "")), "所用软件": j(it.get("software", "")),
                "代码公开": j(it.get("code_open", "")), "数据公开": j(it.get("data_open", "")),
                "数据来源": it.get("data_source", ""), "数据许可证": it.get("data_license", ""),
                "数据获取方式": it.get("data_access", ""), "数据规模": it.get("data_size", ""),
                "分析流程覆盖": j(it.get("workflow", "")), "可复现条件": it.get("reproducibility", ""),
                "软件项目": it.get("project", ""), "文档版本": it.get("version", ""), "官方归属": it.get("owner", ""),
                "维护状态": it.get("maintenance", ""), "文档范围": it.get("doc_scope", ""),
                "项目名称": it.get("program", ""), "学位": it.get("degree", ""), "适用学年": it.get("year", ""),
                "课程与先修要点": it.get("courses_note", ""),
                "SHA256（下载时记录）": "; ".join(f.get("sha256", f.get("archive_sha256", "")) for f in files if f.get("sha256") or f.get("archive_sha256")),
            }
            rows.append((s, row))
    return rows, fails


def paper_rows(idmap):
    rows, fails = [], []
    for c in CATS:
        ss = P.seeds(c)
        if not ss:
            continue
        st = load(P.state_path(c), {})
        for s in ss:
            k = P.key_of(s)
            rec = st.get(k)
            if not rec:
                if not s.get("reserve"):
                    fails.append({"编号": "", "课程群": c, "资料类型": "论文/综述/教程", "标题": s.get("title", k),
                                  "状态": "待核验", "原因": "未运行下载", "来源": k})
                continue
            if rec["status"] == "dup_elsewhere":
                continue
            m = P.entry_meta(s) or {}
            if rec["status"] != "ok":
                fails.append({"编号": "", "课程群": c, "资料类型": "论文/综述/教程", "标题": m.get("title", k),
                              "状态": {"fail": "下载失败/核验未通过", "pending": "待核验（标题/作者自动比对未过）",
                                       "rejected": "人工拒收"}.get(rec["status"], rec["status"]),
                              "原因": rec.get("note", ""), "来源": rec.get("pdf", k)})
                continue
            if k not in idmap:
                n = 1 + sum(1 for v in idmap.values() if v.startswith(f"C{c}-"))
                idmap[k] = f"C{c}-{n:03d}"
            reuse = rec.get("source") == "reuse"
            w = window_status(m.get("date", ""))
            rows.append(("papers", {
                "编号": idmap[k], "课程群": c, "关联课程群": j(s.get("related")), "专业方向": s.get("track", ""),
                "学位层次": s.get("level", ""), "课程属性": "研究专题阅读", "资料类型": "论文/" + s.get("type", ""),
                "资料包类型": s.get("subtopic", ""), "标题": m.get("title", ""), "作者或教师": "; ".join(m.get("authors", [])[:8])
                + (" 等" if len(m.get("authors", [])) > 8 else ""),
                "学校或出版社": m.get("journal_ref", "") or ("arXiv" if s.get("arxiv") else ""),
                "学期或版本": m.get("version", ""), "版本年份": m.get("version_date", ""),
                "首次公开日期": m.get("date", ""), "首次公开依据": m.get("date_basis", ""), "时间窗口": w,
                "三年前或经典保留理由": s.get("classic_reason", "") if w != "近三年" else "",
                "语言": "en", "标识符": (f"arXiv:{s['arxiv']}" if s.get("arxiv") else "") + (f"; DOI:{m['doi']}" if m.get("doi") else ""),
                "原始来源": m.get("landing", ""), "下载地址": rec.get("pdf", ""), "本地路径": rec.get("path", ""),
                "完整性": "完整（核验通过）", "核验说明": rec.get("note", ""),
                "来源性质": "已有复用" if reuse else "本轮新下载",
                "复用来源": f"{rec.get('reuse_lib', '')} {rec.get('reuse_id', '')}".strip() if reuse else "",
                "许可证": "arXiv 分发许可（以 arXiv 页面为准）" if s.get("arxiv") else s.get("license", "出版方开放获取（以出版方页面为准）"),
                "理论难度": s.get("difficulty", ""), "学习用途": "研究论文（按需精读）",
                "选入理由": s.get("reason", ""), "简介": s.get("summary", ""), "简介依据": s.get("summary_basis", ""),
                "SHA256（下载时记录）": rec.get("sha256", ""),
            }))
    return rows, fails


def main():
    idmap = load(STATE / "id_map.json", {})
    mrows, mfails = mat_rows()
    prows, pfails = paper_rows(idmap)
    save(STATE / "id_map.json", idmap)
    rows = mrows + prows
    # duplicate check on recorded hashes
    seen, dups = {}, []
    for s, r in rows:
        for h in filter(None, r["SHA256（下载时记录）"].split("; ")):
            if h in seen and seen[h] != r["编号"]:
                dups.append((seen[h], r["编号"]))
            seen.setdefault(h, r["编号"])
    order = {"curricula": 0, "courses": 1, "books": 2, "practice": 3, "cases": 4, "software": 5, "papers": 6}
    rows.sort(key=lambda x: (order[x[0]], x[1]["课程群"], x[1]["编号"]))
    with open(ROOT / "catalog_cn.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, COLS, extrasaction="ignore")
        w.writeheader()
        for s, r in rows:
            w.writerow({c: r.get(c, "") for c in COLS})
    with open(ROOT / "download_failures_cn.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, ["编号", "课程群", "资料类型", "标题", "状态", "原因", "来源"])
        w.writeheader()
        for r in mfails + pfails:
            w.writerow(r)
    # progress per group
    cnt = defaultdict(Counter)
    recent = defaultdict(Counter)
    for s, r in rows:
        cnt[r["课程群"]][s] += 1
        if r["来源性质"] == "已有复用":
            cnt[r["课程群"]][s + "_reuse"] += 1
        if s == "papers":
            recent[r["课程群"]][r["时间窗口"]] += 1
    fcnt = Counter((r["课程群"], r["资料类型"]) for r in mfails + pfails)
    with open(ROOT / "progress_cn.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["课程群", "名称", "层次（规划）", "属性（规划）", "教材 已核验/目标3–5", "课程讲义 已核验/目标2–4",
                    "实践 已核验/目标2–5", "论文 已核验/目标30–50", "论文近三年占比", "其中已有复用", "失败/待核验", "状态"])
        for c, (slug, name, lvl, req) in CATS.items():
            k = cnt[c]
            pt = "30–50" if c in PAPER_GROUPS else "不设"
            rc = recent[c]
            share = f"{rc['近三年'] / max(1, sum(rc.values())):.1%}" if sum(rc.values()) else "-"
            reuse = sum(v for kk, v in k.items() if kk.endswith("_reuse"))
            nf = sum(v for (g, t), v in fcnt.items() if g == c)
            ok = (k["books"] >= 3 and k["courses"] >= 2 and k["practice"] >= 2
                  and (c not in PAPER_GROUPS or k["papers"] >= 30))
            w.writerow([f"{c}", name, lvl, req, f"{k['books']}", f"{k['courses']}", f"{k['practice']}",
                        f"{k['papers']} / {pt}", share, reuse, nf, "达标" if ok else "未达标"])
        for zone, sset in (("案例区", "cases"), ("软件参考区", "software"), ("培养方案", "curricula")):
            n = sum(1 for s, r in rows if s == sset)
            w.writerow([zone, TYPE[sset], "", "", "", "", "", "", "", "", "", f"已核验 {n}"])
        doms = Counter(r["编号"][:2] for s, r in rows if s == "cases")
        for d, nm in CASE_DOMAINS.items():
            w.writerow([f"案例 {d}", nm, "", "", "", "", "", "", "", "", "", f"已核验 {doms[d]} / 目标 3–5"])
    tot = Counter(s for s, r in rows)
    reuse_n = sum(1 for s, r in rows if r["来源性质"] == "已有复用")
    print("catalog rows", len(rows), dict(tot), "reuse", reuse_n, "failures", len(mfails) + len(pfails),
          "hash-dups", dups[:10])


if __name__ == "__main__":
    main()
