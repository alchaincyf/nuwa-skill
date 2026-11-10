#!/usr/bin/env python3
"""
机检一个人物 Skill 的必备件：结构在不在、证据带没带、有没有会出事故的东西。
它查的是「有没有」，不是「好不好」——好不好由验证阶段的三项测试回答。

用法:
    python3 quality_check.py <人物Skill目录 或 SKILL.md 路径>

每一项输出 ✓ / ! / ✗ 和原因；✗ 必须修，! 是提醒。有 ✗ 时退出码为 1。
没有招式和案例库的旧版 Skill 会按旧标准检查，并提示可以升级。
"""

import re
import sys
from pathlib import Path

# Windows 的 GBK 控制台打不出 ✓ 和中文，统一成 UTF-8
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

OK, WARN, BAD = "✓", "!", "✗"

DESC_SOFT = 300    # 产物 description 的建议上限：每个会话都加载，长了烧 token、抬高误触发
DESC_HARD = 1024   # 多数宿主的硬上限，超过会报错
LINES_SOFT = 350   # 核心文件每次激活都占上下文
LINES_HARD = 500
MIN_MOVES = 5
MIN_CASES = 6      # 快速档的下限；标准档 12、深度档 20
STD_CASES = 12
ABS_PATH = re.compile(r"(/Users/[^\s/`)]+/|/home/[^\s/`)]+/|\b[A-Za-z]:\\\\?[A-Za-z])")


def split_frontmatter(text):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}, text
    fm, body = m.group(1), text[m.end():]
    data = {}
    key = None
    for line in fm.split("\n"):
        km = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if km and not line.startswith(" "):
            key = km.group(1)
            val = km.group(2).strip()
            data[key] = "" if val in ("|", ">", "|-", ">-") else val.strip("\"'")
        elif key and line.startswith(" "):
            data[key] = (data[key] + " " + line.strip()).strip()
    return data, body


def sections(body, level=2):
    """按 ## 标题切段，返回 [(标题, 正文)]。代码块里的 # 不算标题。"""
    out, title, buf, fence = [], None, [], False
    mark = "#" * level + " "
    for line in body.split("\n"):
        if line.lstrip().startswith("```"):
            fence = not fence
        if not fence and line.startswith(mark):
            if title is not None:
                out.append((title, "\n".join(buf)))
            title, buf = line[len(mark):].strip(), []
        else:
            buf.append(line)
    if title is not None:
        out.append((title, "\n".join(buf)))
    return out


def find(secs, pattern):
    rx = re.compile(pattern, re.IGNORECASE)
    for title, text in secs:
        if rx.search(title):
            return title, text
    return None, None


def list_items(text):
    """无序和有序列表项都算（顶格的）。"""
    return re.findall(r"^(?:[-*+]|\d+[.、)])\s+\S", text, re.MULTILINE)


def has_source(text):
    return bool(re.search(r"——|—\s*\S|出处|https?://|《[^》]+》|\b(19|20)\d{2}\b", text))


def quote_blocks(text):
    blocks, cur = [], []
    for line in text.split("\n"):
        if line.startswith(">"):
            cur.append(line)
        elif cur:
            blocks.append("\n".join(cur))
            cur = []
    if cur:
        blocks.append("\n".join(cur))
    return blocks


class Report:
    def __init__(self):
        self.rows = []

    def add(self, mark, name, msg, fix=""):
        self.rows.append((mark, name, msg, fix))

    def dump(self):
        for mark, name, msg, fix in self.rows:
            print(f"  {mark} {name}：{msg}")
            if fix and mark != OK:
                print(f"      → {fix}")
        bad = sum(1 for r in self.rows if r[0] == BAD)
        warn = sum(1 for r in self.rows if r[0] == WARN)
        print("-" * 56)
        if bad:
            print(f"{bad} 项必须修（✗），{warn} 项提醒（!）。按箭头后的改法逐项处理，再跑一遍。")
        elif warn:
            print(f"必备件齐了，有 {warn} 项提醒。接下来做验证阶段的三项测试。")
        else:
            print("必备件齐了。接下来做验证阶段的三项测试。")
        return 1 if bad else 0


def check_common(rep, root, text, fm, body):
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name or not desc:
        rep.add(BAD, "frontmatter", "缺 name 或 description", "文件开头用 --- 包住 name 和 description 两个字段")
    else:
        n = len(desc)
        if n > DESC_HARD:
            rep.add(BAD, "description", f"{n} 字，超过宿主约 {DESC_HARD} 字的上限，会加载失败",
                    "压到 300 字内：一句定位＋明确触发语＋一句「不在一般性问题上自动触发」")
        elif n > DESC_SOFT:
            rep.add(WARN, "description", f"{n} 字，建议 {DESC_SOFT} 字内",
                    "删掉长尾关键词；负责命中的是人名和专属概念")
        else:
            rep.add(OK, "description", f"{n} 字")
        if not re.search(r"视角|怎么看|perspective|切换到", desc, re.IGNORECASE):
            rep.add(WARN, "触发语", "description 里没有明确的触发语", "加上「用XX的视角」「XX会怎么看」这类说法")

    n_lines = text.count("\n") + 1
    if n_lines > LINES_HARD:
        rep.add(BAD, "篇幅", f"SKILL.md {n_lines} 行，超过 {LINES_HARD} 行",
                "把案例详情移到 references/casebook.md，原话移到 references/voice.md，时间线和谱系移到 references/")
    elif n_lines > LINES_SOFT:
        rep.add(WARN, "篇幅", f"SKILL.md {n_lines} 行，建议 {LINES_SOFT} 行内", "核心文件每次激活都加载；只在特定问题上用到的内容下沉到 references/")
    else:
        rep.add(OK, "篇幅", f"SKILL.md {n_lines} 行")

    hits = []
    for f in [root / "SKILL.md", root / "references" / "casebook.md", root / "references" / "voice.md"]:
        if f.exists():
            for i, line in enumerate(f.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
                if ABS_PATH.search(line):
                    hits.append(f"{f.name}:{i}")
    if hits:
        rep.add(BAD, "绝对路径", "出现本机绝对路径：" + "、".join(hits[:5]) + ("…" if len(hits) > 5 else ""),
                "改成相对本 Skill 目录的路径（references/…）")
    else:
        rep.add(OK, "绝对路径", "没有")


def check_sources(rep, secs):
    title, text = find(secs, r"来源|source|reference")
    if text is None:
        rep.add(BAD, "来源", "没有来源一节", "列出一手来源（他本人写的、说的、做的）和二手来源")
        return
    primary = secondary = 0
    mode = None
    for line in text.split("\n"):
        if re.match(r"^(#{3,}|\*\*)", line.strip()):
            if re.search(r"一手|primary", line, re.IGNORECASE):
                mode = "p"
            elif re.search(r"二手|secondary", line, re.IGNORECASE):
                mode = "s"
            else:
                mode = None
            continue
        if re.match(r"^\s*(?:[-*+]|\d+[.、)])\s+\S", line):
            if mode == "p":
                primary += 1
            elif mode == "s":
                secondary += 1
    total = primary + secondary
    if total == 0:
        rep.add(WARN, "来源", "来源没有分成「一手」「二手」两组，无法统计占比",
                "用「**一手**」「**二手**」两个小标题分组，每个来源一行")
    elif primary / total <= 0.5:
        rep.add(BAD, "一手来源占比", f"{primary}/{total}，没过半", "补本人著作、访谈原文、决策记录；二手转述找到原文再用")
    else:
        rep.add(OK, "一手来源占比", f"{primary}/{total}")


def check_boundary(rep, secs, v2):
    title, text = find(secs, r"边界|boundar")
    if text is None:
        rep.add(BAD, "边界", "没有边界一节", "写清他熟悉的、可以推断的、沉默与盲区三格，以及这个 Skill 的局限")
        return
    n = len(list_items(text))
    if n < 3:
        rep.add(BAD, "局限", f"边界一节只有 {n} 条列表项", "至少 3 条具体局限（哪段时间、哪类材料、哪个领域信息不足）")
    else:
        rep.add(OK, "局限", f"{n} 条")
    if not re.search(r"调研时间|截至|as of", text, re.IGNORECASE):
        rep.add(BAD, "调研时间", "没写调研时间", "加一行「调研时间：YYYY-MM-DD，之后的变化没有覆盖」")
    if not v2:
        return
    grid = [k for k, rx in (("熟悉", r"熟悉"), ("可以推断", r"推断"), ("沉默与盲区", r"沉默|盲区")) if not re.search(rx, text)]
    if grid:
        rep.add(BAD, "边界三格", "缺：" + "、".join(grid), "每一格写话题和对应的回应方式，运行时才照得着做")
    else:
        rep.add(OK, "边界三格", "齐")
    decl = [k for k, rx in (("这次蒸馏的盲区", r"盲区"), ("先验偏向", r"先验"), ("什么会推翻结论", r"推翻")) if not re.search(rx, text)]
    if decl:
        rep.add(WARN, "申报", "缺：" + "、".join(decl), "三条申报让这份蒸馏有保质期")


def check_v2(rep, root, secs, text):
    # 运行纪律
    title, t = find(secs, r"怎么用|使用说明|角色扮演|运行纪律|how to use")
    if t is None:
        rep.add(BAD, "运行纪律", "没有「怎么用我」一节", "按 skill-template.md 保留七条运行纪律")
    else:
        need = {"推断要说明": r"推断", "先翻案例": r"案例", "可退出": r"退出", "原话带出处": r"出处", "点破盲区": r"盲区"}
        miss = [k for k, rx in need.items() if not re.search(rx, t)]
        if miss:
            rep.add(BAD, "运行纪律", "缺：" + "、".join(miss), "七条的意思一条都不能少，措辞可以换成他的口吻")
        else:
            rep.add(OK, "运行纪律", "要点齐")

    # 招式
    title, t = find(secs, r"招式|动手|moves?\b")
    if t is None:
        rep.add(BAD, "招式", "没有招式一节", "从决策与对话底稿里挑过去时的叙事句，归并成 5–8 个可照做的动作")
    else:
        subs = sections(t, 3)
        nosrc = [s for s, b in subs if not has_source(b)]
        if len(subs) < MIN_MOVES:
            rep.add(BAD, "招式", f"{len(subs)} 个，至少 {MIN_MOVES} 个", "检查底稿里记了事实、成品里没有对应动作的条目")
        elif nosrc:
            rep.add(WARN, "招式", f"{len(subs)} 个，其中没带出处的：" + "、".join(nosrc[:4]), "每个招式配一个带年份和出处的例子")
        else:
            rep.add(OK, "招式", f"{len(subs)} 个，都带例子")

    # 心智模型
    title, t = find(secs, r"心智模型|看世界|mental model")
    if t is None:
        rep.add(BAD, "心智模型", "没有心智模型一节", "过三重验证（跨域复现、有生成力、有排他性）的 3–7 个")
    else:
        subs = sections(t, 3)
        n = len(subs)
        nolimit = [s for s, b in subs if not re.search(r"不灵|失效|局限|不适用|limit", b, re.IGNORECASE)]
        noevid = [s for s, b in subs if not re.search(r"证据|evidence", b, re.IGNORECASE)]
        if not 3 <= n <= 7:
            rep.add(BAD, "心智模型", f"{n} 个，应为 3–7 个", "太多说明没筛：只过一两重验证的降为启发式")
        elif nolimit or noevid:
            lack = []
            if noevid:
                lack.append("缺证据：" + "、".join(noevid[:3]))
            if nolimit:
                lack.append("缺失效条件：" + "、".join(nolimit[:3]))
            rep.add(BAD, "心智模型", f"{n} 个；" + "；".join(lack), "每个模型写证据（两个不同领域）和什么时候不灵")
        else:
            rep.add(OK, "心智模型", f"{n} 个，证据与失效条件齐")

    # 常见误读
    title, t = find(secs, r"误读|以为|misread|misconception")
    if t is None:
        rep.add(BAD, "常见误读", "没有这一节", "从「和先验不一样的地方」里的「推翻」挑至少 2 条")
    else:
        n = max(len(re.findall(r"其实|实际上|in fact", t, re.IGNORECASE)), len(list_items(t)) // 2)
        if n < 2:
            rep.add(BAD, "常见误读", f"{n} 条，至少 2 条", "找不到误读多半是调研还停在二手转述里")
        else:
            rep.add(OK, "常见误读", f"{n} 条")

    # 声音
    title, t = find(secs, r"说话|声音|表达|voice")
    if t is None:
        rep.add(BAD, "声音", "没有声音一节", "规则加带出处的原话样本")
    else:
        blocks = quote_blocks(t)
        sourced = [b for b in blocks if has_source(b)]
        if len(sourced) < 2:
            rep.add(BAD, "原话样本", f"带出处的原话段落 {len(sourced)} 段，至少 2 段", "用 > 引用块放原话，结尾写「—— 出处」")
        else:
            rep.add(OK, "原话样本", f"{len(sourced)} 段")

    # 案例
    title, t = find(secs, r"案例|case")
    casebook = root / "references" / "casebook.md"
    if t is None or not casebook.exists():
        rep.add(BAD, "案例库", "缺案例索引一节或 references/casebook.md", "按 skill-template.md 的格式写案例卡，并在 SKILL.md 里建索引")
    else:
        cb = casebook.read_text(encoding="utf-8", errors="replace")
        cards = sections(cb, 2)
        ids = {m.group(1) for s, _ in cards for m in [re.match(r"(C\d+)", s)] if m}
        idx = set(re.findall(r"\bC\d+\b", t))
        nosrc = [s.split("·")[0].strip() for s, b in cards if re.match(r"C\d+", s) and not re.search(r"出处|https?://|《", b)]
        if len(ids) < MIN_CASES:
            rep.add(BAD, "案例库", f"{len(ids)} 张案例卡，快速档至少 {MIN_CASES} 张", "标准档 12 张、深度档 20 张；失败和改口的案例至少占四分之一")
        elif idx - ids:
            rep.add(BAD, "案例索引", "索引里有、案例库里没有：" + "、".join(sorted(idx - ids)), "索引和 casebook.md 的编号要对得上")
        elif nosrc:
            rep.add(BAD, "案例库", "没有出处的案例卡：" + "、".join(nosrc[:6]), "每张卡写出处和可信度；查不到出处的不收")
        elif ids - idx:
            rep.add(WARN, "案例索引", f"{len(ids)} 张卡，没进索引的：" + "、".join(sorted(ids - idx)[:6]), "不进索引，运行时就找不到")
        elif len(ids) < STD_CASES:
            rep.add(WARN, "案例库", f"{len(ids)} 张，够快速档；标准档要 {STD_CASES} 张")
        else:
            rep.add(OK, "案例库", f"{len(ids)} 张，索引对得上，都有出处")

    if not (root / "references" / "voice.md").exists():
        rep.add(WARN, "原话库", "没有 references/voice.md", "8–15 段原话，按场合分组")

    # 张力
    title, t = find(secs, r"没想清楚|张力|矛盾|tension")
    if t is None:
        rep.add(BAD, "张力", "没有这一节", "至少 2 对他身上真实存在的矛盾，两头各给证据，不调和")
    else:
        n = len(list_items(t)) or len([p for p in re.split(r"\n\s*\n", t.strip()) if p.strip()])
        if n < 2:
            rep.add(BAD, "张力", f"{n} 对，至少 2 对")
        else:
            rep.add(OK, "张力", f"{n} 处")

    check_boundary(rep, secs, v2=True)
    check_sources(rep, secs)

    # 底稿
    rdir = root / "references" / "research"
    if not rdir.is_dir():
        rep.add(BAD, "调研底稿", "没有 references/research/", "底稿必须存在产物目录内，Skill 才是自包含的")
    else:
        if not (rdir / "00-prior.md").exists():
            rep.add(WARN, "先验快照", "没有 research/00-prior.md", "没有它就无从判断哪些是增量")
        files = [f for f in rdir.glob("0[1-6]-*.md") if f.stat().st_size > 200]
        if len(files) < 3:
            rep.add(BAD, "调研底稿", f"只有 {len(files)} 路底稿", "快速档至少著作、对话、决策三路")
        else:
            rep.add(OK, "调研底稿", f"{len(files)} 路")
        hold = rdir / "holdout.md"
        if hold.exists():
            urls = set(re.findall(r"https?://[^\s)>\]]+", hold.read_text(encoding="utf-8", errors="replace")))
            if casebook.exists():
                leak = [u for u in urls if u in casebook.read_text(encoding="utf-8", errors="replace")]
                if leak:
                    rep.add(WARN, "封存件", "封存件的出处也出现在案例库里：" + leak[0][:60],
                            "确认案例卡写的不是封存的那段内容；是的话换一件封存件或删掉那张卡")
                else:
                    rep.add(OK, "封存件", f"有，{len(re.findall(r'^## H', hold.read_text(encoding='utf-8', errors='replace'), re.MULTILINE))} 件")
        elif re.search(r"未做增量测试", text):
            rep.add(WARN, "封存件", "没有封存件，已在 Skill 里写明未做增量测试")
        else:
            rep.add(BAD, "封存件", "没有 research/holdout.md，也没写明未做增量测试",
                    "提炼前挑 3–5 件一手材料封存；来源不足 10 条时在边界里写「未做增量测试」")


def check_v1(rep, secs, text):
    title, t = find(secs, r"心智模型|mental model")
    n = len(sections(t, 3)) if t else 0
    if not 3 <= n <= 7:
        rep.add(BAD, "心智模型", f"{n} 个，应为 3–7 个")
    else:
        rep.add(OK, "心智模型", f"{n} 个")
    if t and not re.search(r"局限|失效|不适用|盲区|limit", t, re.IGNORECASE):
        rep.add(BAD, "模型局限", "心智模型没有写失效条件")
    title, t = find(secs, r"表达|说话|voice|expression")
    if t is None:
        rep.add(BAD, "表达", "没有表达一节")
    else:
        rep.add(OK, "表达", "有")
    title, t = find(secs, r"张力|矛盾|没想清楚|价值观|tension")
    if t is None or not re.search(r"张力|矛盾|tension|paradox", t, re.IGNORECASE):
        rep.add(BAD, "内在张力", "没找到张力或矛盾的记录")
    else:
        rep.add(OK, "内在张力", "有")
    check_boundary(rep, secs, v2=False)
    check_sources(rep, secs)


def main():
    if len(sys.argv) < 2:
        print(__doc__.strip())
        sys.exit(2)
    p = Path(sys.argv[1])
    root = p if p.is_dir() else p.parent
    skill = root / "SKILL.md"
    if not skill.exists():
        print(f"✗ 找不到 {skill}。参数应是人物 Skill 的目录，或其中的 SKILL.md。")
        sys.exit(2)

    text = skill.read_text(encoding="utf-8", errors="replace")
    fm, body = split_frontmatter(text)
    secs = sections(body, 2)
    v2 = (root / "references" / "casebook.md").exists() or find(secs, r"招式|动手")[1] is not None

    rep = Report()
    print(f"机检：{root.name}（{'新骨架' if v2 else '旧版骨架'}）")
    print("-" * 56)
    check_common(rep, root, text, fm, body)
    if v2:
        check_v2(rep, root, secs, text)
    else:
        check_v1(rep, secs, text)
    code = rep.dump()
    if not v2:
        print("这是没有招式、案例库和常见误读的旧版 Skill。底稿还在的话，可以让女娲「升级」它，不用重新调研。")
    sys.exit(code)


if __name__ == "__main__":
    main()
