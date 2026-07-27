#!/usr/bin/env python3
"""COMMUNITY.md 收录PR的半自动检查。

机器检查（本脚本）：
1. PR只改动 COMMUNITY.md（动了SKILL.md等核心文件直接判❌）
2. 新增行里的GitHub仓库真实存在且公开
3. 若目标仓库含SKILL.md（人物/主题skill类）→ 额外要求：
   - FIDELITY.md 存在且总分≥70（B级）
   - FIDELITY.md 关键字段行（测试日期/总分/各维评分）不得为占位或预估
     （待跑、预估、TBD、YYYY-MM-DD等——分数须为独立双agent实测结果；
     只扫字段行不扫全文，诚实边界等正文表述不会触发）
   - SKILL.md 含「诚实边界」章节
   - 有 references/ 目录；references/research/ 子目录缺失仅记⚠️请人工确认
   若不含SKILL.md（合集/工具类）→ 仅存在性检查，标注请人工确认类别
4. 结果贴成PR评论

人工检查（维护者）：伦理红线 + 内容质量抽查 + 合并。

本地测试：python3 community_check.py --check-repo owner/repo
"""
import json
import os
import re
import sys
import urllib.request

API = "https://api.github.com"

# FIDELITY.md 占位/预估检测：结构化字段扫描，命中即判❌。
# 依据：保真度分数必须来自独立双agent实测（见 references/fidelity-scorecard.md），
# 「预填模板+补一行总分」不算跑过测试（先例：PR #70）。
# 设计约束（2026-07-26对抗审查 P1-22/P1-23）：
# 1. 只扫「关键字段行」（测试日期/总分/各维评分等），绝不全文搜词——
#    「诚实边界：xx未实测」是项目自己要求写的内容，不能被判成造假；
# 2. 否定语境免疫：「不是自评分」「NOT a self-assessment」不算命中；
# 3. 英文词绑定分数上下文（estimated score），不拦 "Estimated reading time"。
# 宁可漏判交给人工，也不让守规矩的投稿被机器误拒。

# 关键字段行：行首（允许 >、#、*、-、| 等markdown前缀）出现「字段名 + 冒号/表格分隔符」。
# 「评分日期格式统一为YYYY-MM-DD」这类叙述句因字段名后无分隔符，不会被当成字段行。
FIDELITY_KEY_FIELD_RE = re.compile(
    r"^[\s>#*\-|]*(?:测试日期|评分日期|测试时间|测试模型|总分|综合得分|最终得分|得分|评分"
    r"|维度\s*\d+|立场一致性|风格辨识度|边缘诚实度|来源透明度|结构完整度"
    r"|total(?:\s+score)?|overall(?:\s+score)?|final\s+score|test\s+date|score|date)"
    r"[\s*]*[:：|]",
    re.IGNORECASE,
)
# 占位/预估标记（仅在关键字段行内查找）
FIDELITY_PLACEHOLDER_PATTERNS = [
    (r"预估", "预估"),
    (r"待跑", "待跑"),
    (r"待测", "待测"),
    (r"待补", "待补"),
    (r"待定", "待定"),
    (r"待填", "待填"),
    (r"占位", "占位"),
    (r"未实测", "未实测"),
    (r"未测试", "未测试"),
    (r"自评分", "自评分"),   # 区别于论文引用里的「自评准确率」，裸「自评」不收
    (r"YYYY[-/年]?\s*MM", "YYYY-MM-DD（模板日期没填）"),
    (r"\bTBD\b", "TBD"),
    (r"\bTODO\b", "TODO"),
    (r"self[- ]assess\w*", "self-assessed"),
    (r"\bestimated\s+(?:score|total|rating|grade)", "estimated score"),
    (r"\bplaceholder\b", "placeholder"),
    (r"\bNN\s*/\s*\d+", "NN/100（模板分数没填）"),
]
# 否定语境：命中词紧邻的前文若是否定表达，视为主动澄清而非占位
FIDELITY_NEGATION_RE = re.compile(
    r"(?:不是|并非|绝不|从不|不算|不做|没有|不存在|未使用|无"
    r"|not(?:\s+an?)?|isn'?t(?:\s+an?)?|never|no)[\s*'\"「」（(]*$",
    re.IGNORECASE,
)


def find_fidelity_red_flags(text):
    """结构化字段扫描FIDELITY.md：只检查关键字段行是否为占位/预估。

    返回命中标记列表（去重、保持顺序）。非字段行（诚实边界、局限说明等正文）不扫描。
    """
    hits = []
    for line in text.splitlines():
        if not FIDELITY_KEY_FIELD_RE.match(line):
            continue
        for pat, label in FIDELITY_PLACEHOLDER_PATTERNS:
            for m in re.finditer(pat, line, re.IGNORECASE):
                prefix = line[max(0, m.start() - 16):m.start()]
                if FIDELITY_NEGATION_RE.search(prefix):
                    continue  # 否定语境（「不是自评分」「NOT a self-assessment」）
                hits.append(label)
                break
    return list(dict.fromkeys(hits))


def gh(path, token, raw=False):
    req = urllib.request.Request(API + path)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    if raw:
        req.add_header("Accept", "application/vnd.github.raw+json")
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read().decode("utf-8", "replace")
            return data if raw else json.loads(data)
    except Exception:
        return None


def check_target_repo(slug, token):
    """检查被收录的仓库，返回 (是否通过, 检查项列表)。"""
    items = []
    repo = gh(f"/repos/{slug}", token)
    if not repo:
        return False, [("❌", f"`{slug}` 仓库不存在或不可访问")]
    items.append(("✅", f"[`{slug}`](https://github.com/{slug}) 存在（★{repo.get('stargazers_count', 0)}）"))

    skill_md = gh(f"/repos/{slug}/contents/SKILL.md", token, raw=True)
    if skill_md is None:
        items.append(("ℹ️", "无根目录SKILL.md → 按「合集/工具类」处理，请人工确认类别与内容"))
        return True, items
    items.append(("✅", "含 SKILL.md（按skill类审核）"))

    if "诚实边界" in skill_md or "Honest" in skill_md or "honest-limits" in skill_md.lower():
        items.append(("✅", "SKILL.md 含诚实边界章节"))
    else:
        items.append(("❌", "SKILL.md 缺「诚实边界」章节（收录门槛之一）"))

    refs = gh(f"/repos/{slug}/contents/references", token)
    if isinstance(refs, list) and refs:
        items.append(("✅", "含 references/ 目录"))
        research = gh(f"/repos/{slug}/contents/references/research", token)
        if isinstance(research, list) and research:
            items.append(("✅", "含 references/research/ 调研底稿目录"))
        else:
            items.append(("⚠️", "未见 references/research/ 子目录（CONTRIBUTING期望的调研底稿结构）。"
                                "若调研底稿直接放在 references/ 下，请维护者人工确认可溯源性即可，不作硬性拦截"))
    else:
        items.append(("❌", "缺 references/ 调研底稿（skill需自包含可溯源）"))

    fidelity = gh(f"/repos/{slug}/contents/FIDELITY.md", token, raw=True)
    if fidelity is None:
        items.append(("❌", "缺 FIDELITY.md 保真度评分卡（见 references/fidelity-scorecard.md）"))
    else:
        m = re.search(r"总分[：:]\s*(\d+)\s*/\s*100", fidelity)
        if not m:
            items.append(("❌", "FIDELITY.md 存在但未解析到「总分：NN/100」"))
        elif int(m.group(1)) >= 70:
            items.append(("✅", f"保真度 {m.group(1)}/100 ≥ 70（B级门槛）"))
        else:
            items.append(("❌", f"保真度 {m.group(1)}/100 未达B级门槛（70）"))
        red_flags = find_fidelity_red_flags(fidelity)
        if red_flags:
            items.append(("❌", "FIDELITY.md 关键字段（测试日期/总分/评分）检出占位或预估：`"
                          + "`、`".join(red_flags[:8])
                          + ("`" if len(red_flags) <= 8 else f"`…等{len(red_flags)}项")
                          + "。保真度分数须由独立双agent实测产生（方法见 references/fidelity-scorecard.md），"
                            "预填模板或自评预估分不满足收录门槛，请实测后更新评分卡"))
        else:
            items.append(("✅", "FIDELITY.md 关键字段未检出占位/预估"))

    ok = all(mark != "❌" for mark, _ in items)
    return ok, items


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--check-repo":
        ok, items = check_target_repo(sys.argv[2], os.environ.get("GITHUB_TOKEN", ""))
        for mark, text in items:
            print(mark, text)
        sys.exit(0 if ok else 1)

    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ["GITHUB_REPOSITORY"]
    pr = os.environ["PR_NUMBER"]

    files = gh(f"/repos/{repo}/pulls/{pr}/files?per_page=100", token) or []
    names = [f["filename"] for f in files]
    lines = ["## 🤖 社区收录检查\n"]
    all_ok = True

    core_touched = [n for n in names if n != "COMMUNITY.md"]
    if core_touched:
        all_ok = False
        lines.append(f"❌ PR改动了 COMMUNITY.md 以外的文件：`{'`, `'.join(core_touched[:10])}`")
        if any(n == "SKILL.md" for n in core_touched):
            lines.append("　　⚠️ SKILL.md 是核心资产，不接受外部PR改动（见 CONTRIBUTING.md），请从PR中移除")
    else:
        lines.append("✅ 只改动 COMMUNITY.md")

    added = []
    for f in files:
        if f["filename"] == "COMMUNITY.md":
            for ln in (f.get("patch") or "").splitlines():
                if ln.startswith("+") and not ln.startswith("+++"):
                    added += re.findall(r"github\.com/([\w.-]+/[\w.-]+)", ln)
    added = list(dict.fromkeys(s.rstrip(")/") for s in added))

    if not added:
        all_ok = False
        lines.append("❌ 未在新增行中检测到GitHub仓库链接")
    for slug in added[:5]:
        ok, items = check_target_repo(slug, token)
        all_ok = all_ok and ok
        lines.append(f"\n**{slug}**")
        lines += [f"- {mark} {text}" for mark, text in items]

    lines.append("\n---")
    lines.append(("✅ **机器检查通过**。" if all_ok else "❌ **机器检查未通过**，请按上述项修改后推送更新（会自动重跑）。"))
    lines.append("最终合并前维护者还会人工确认：伦理红线（CONTRIBUTING.md）+ 内容质量抽查。")

    body = "\n".join(lines)
    req = urllib.request.Request(
        f"{API}/repos/{repo}/issues/{pr}/comments",
        data=json.dumps({"body": body}).encode(),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    urllib.request.urlopen(req, timeout=15)
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
