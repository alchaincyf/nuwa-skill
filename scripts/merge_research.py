#!/usr/bin/env python3
"""
合并各路调研底稿，生成采集阶段结束时给用户看的摘要表格。
扫描 references/research/ 下的 01-06 文件，统计每一路的来源数量、一手/二手占比、
关键发现，以及「和先验不一样的地方」各有几条（推翻 / 加深 / 新增）。

用法:
    python3 merge_research.py <skill目录路径>

示例:
    python3 merge_research.py .claude/skills/elon-musk-perspective

输出: 打印markdown格式的摘要表格到stdout
"""

import sys
import re
from pathlib import Path

# Windows 的 GBK 控制台打不出表格线和中文，统一成 UTF-8
for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

AGENTS = {
    '01-writings': '著作',
    '02-conversations': '对话',
    '03-expression-dna': '表达',
    '04-external-views': '他者',
    '05-decisions': '决策',
    '06-timeline': '时间线',
}


def count_sources(content: str) -> dict:
    """统计来源数量和一手/二手占比"""
    # 计算URL数量作为来源数
    urls = re.findall(r'https?://[^\s\)]+', content)

    # 检测一手/二手标记
    primary_markers = len(re.findall(r'一手|primary|本人|原文|原始|直接引用', content, re.IGNORECASE))
    secondary_markers = len(re.findall(r'二手|secondary|转述|总结|评论|分析', content, re.IGNORECASE))

    return {
        'url_count': len(urls),
        'unique_urls': len(set(urls)),
        'primary_markers': primary_markers,
        'secondary_markers': secondary_markers,
    }


def extract_key_findings(content: str, max_items: int = 3) -> list[str]:
    """提取关键发现（取前几个二级标题或加粗项）"""
    # 尝试提取##标题
    headings = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    if headings:
        return headings[:max_items]

    # fallback: 提取加粗项
    bolds = re.findall(r'\*\*(.+?)\*\*', content)
    if bolds:
        return bolds[:max_items]

    # fallback: 取前3个非空行
    lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
    return [l[:50] + '...' if len(l) > 50 else l for l in lines[:max_items]]


def count_surprises(content: str) -> dict:
    """数「和先验不一样的地方」一段里推翻/加深/新增各几条。"""
    m = re.search(r'^#+\s*.*(?:和先验不一样|先验).*$', content, re.MULTILINE)
    if not m:
        return None
    tail = content[m.end():]
    nxt = re.search(r'^#{1,2}\s+\S', tail, re.MULTILINE)
    seg = tail[:nxt.start()] if nxt else tail
    items = [l for l in seg.split('\n') if re.match(r'^\s*(?:[-*+]|\d+[.、)])\s+\S', l)]
    if not items:
        # 写成表格的：数表头和分隔线之外的行
        rows = [l for l in seg.split('\n') if l.strip().startswith('|')]
        items = [l for l in rows[2:] if not re.match(r'^\s*\|[\s:|-]+\|\s*$', l)]
    return {
        '推翻': sum(1 for l in items if '推翻' in l),
        '加深': sum(1 for l in items if '加深' in l),
        '新增': sum(1 for l in items if '新增' in l),
        'total': len(items),
    }


def find_contradictions(files: dict[str, str]) -> list[str]:
    """简单检测跨文件矛盾（同一关键词出现不同判断）"""
    contradictions = []
    # 检测「但是」「然而」「相反」「矛盾」等矛盾标记
    for name, content in files.items():
        matches = re.findall(r'(?:矛盾|相反|但实际上|然而.*?不同|争议).{0,100}', content)
        for m in matches:
            contradictions.append(f"{AGENTS.get(name, name)}: {m[:80]}")
    return contradictions[:5]  # 最多5条


def main():
    if len(sys.argv) < 2:
        print("用法: python3 merge_research.py <人物Skill目录>（含 references/research/ 的那一层）")
        sys.exit(1)

    skill_dir = Path(sys.argv[1])
    research_dir = skill_dir / 'references' / 'research'
    # 直接传了 research 目录也认
    if not research_dir.exists() and skill_dir.name == 'research' and skill_dir.is_dir():
        research_dir = skill_dir

    if not research_dir.exists():
        print(f"❌ 目录不存在: {research_dir}")
        sys.exit(1)

    files = {}
    rows = []
    surprises = {'推翻': 0, '加深': 0, '新增': 0, 'total': 0}
    no_surprise_section = []
    total_sources = 0
    total_primary = 0
    total_secondary = 0
    missing = []

    for key, label in AGENTS.items():
        md_file = research_dir / f"{key}.md"
        if not md_file.exists():
            missing.append(label)
            rows.append(f"│ {label:<12} │ {'❌ 缺失':<8} │ {'—':<24} │")
            continue

        content = md_file.read_text(encoding='utf-8')
        files[key] = content
        stats = count_sources(content)
        findings = extract_key_findings(content)
        sp = count_surprises(content)
        if sp is None:
            no_surprise_section.append(label)
        else:
            for k in surprises:
                surprises[k] += sp[k]

        total_sources += stats['unique_urls']
        total_primary += stats['primary_markers']
        total_secondary += stats['secondary_markers']

        findings_str = ', '.join(findings) if findings else '—'
        if len(findings_str) > 40:
            findings_str = findings_str[:37] + '...'

        rows.append(f"│ {label:<12} │ {stats['unique_urls']:<8} │ {findings_str:<24} │")

    # 升级或补搜时新加的底稿（07-xxx.md 及以后）：只把「和先验不一样的地方」计入
    for md_file in sorted(research_dir.glob('[0-9][0-9]-*.md')):
        if md_file.stem in AGENTS or md_file.stem.startswith('00-'):
            continue
        sp = count_surprises(md_file.read_text(encoding='utf-8'))
        if sp is not None:
            for k in surprises:
                surprises[k] += sp[k]

    # 矛盾检测
    contradictions = find_contradictions(files)

    # 输出
    print("┌──────────────┬──────────┬──────────────────────────┐")
    print("│ 调研分路      │ 来源数量  │ 关键发现                  │")
    print("├──────────────┼──────────┼──────────────────────────┤")
    for row in rows:
        print(row)
    print("├──────────────┼──────────┼──────────────────────────┤")

    primary_ratio = f"{total_primary}/{total_primary + total_secondary}" if (total_primary + total_secondary) > 0 else "未标记"
    print(f"│ 总来源数      │ {total_sources:<8} │ 一手占比: {primary_ratio:<15} │")

    if contradictions:
        print(f"│ 矛盾点        │ {len(contradictions)}处      │ {contradictions[0][:24]:<24} │")
    else:
        print(f"│ 矛盾点        │ 0处      │ {'—':<24} │")

    if missing:
        print(f"│ 信息不足维度   │ {len(missing)}个      │ {', '.join(missing):<24} │")
    else:
        print(f"│ 信息不足维度   │ 无       │ {'—':<24} │")

    print("└──────────────┴──────────┴──────────────────────────┘")

    print(f"\n和先验不一样的地方：共 {surprises['total']} 条（推翻 {surprises['推翻']} / 加深 {surprises['加深']} / 新增 {surprises['新增']}）")
    if no_surprise_section:
        print(f"⚠️ 这几路底稿末尾没有「和先验不一样的地方」一段: {', '.join(no_surprise_section)}")
    if surprises['total'] < 8:
        print("⚠️ 不到 8 条，说明还在复述常识：换更深的来源（长访谈原文、早期文章、当事人回忆、批评文章）再找")
    if not (research_dir / '00-prior.md').exists():
        print("⚠️ 没有 00-prior.md（先验快照），无从判断哪些是增量")
    if not (research_dir / 'holdout.md').exists():
        print("提醒：还没有 holdout.md。提炼之前挑 3–5 件一手材料封存，留作验证的考题")

    # 总结
    if total_sources < 10:
        print("\n⚠️ 总来源数 <10，建议降低期望或补充调研")
    if missing:
        print(f"\n⚠️ 缺失维度: {', '.join(missing)}，建议补充或在诚实边界中标注")


if __name__ == '__main__':
    main()
