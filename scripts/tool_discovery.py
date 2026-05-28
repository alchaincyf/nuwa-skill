#!/usr/bin/env python3
"""Phase 2.5 工具发现自动化

职责：脚本只负责数据收集和执行操作，心智模型→工具需求的推理由 LLM 完成。

提供三个子命令：
  discover  → 提取心智模型 + 扫描本地 skills + 扫描 marketplace，输出结构化 JSON
  install   → 安装/复制工具到 persona目录（含安全审查）
  validate  → 验证工具是否可用（语法 + 运行测试）
"""
import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

SKILLS_DIR = Path(os.path.expanduser("~/.claude/skills"))
PLUGINS_DIR = Path(os.path.expanduser("~/.claude/plugins"))
MARKETPLACE_DIR = PLUGINS_DIR / "marketplaces" / "claude-plugins-official"

DANGEROUS_PATTERNS = {
    "critical": [
        (r"\beval\s*\(", "eval() 调用 — 可执行任意代码"),
        (r"\bexec\s*\(", "exec() 调用 — 可执行任意代码"),
        (r"\b__import__\s*\(", "动态 import — 可加载恶意模块"),
        (r"\bcompile\s*\(", "动态编译代码"),
        (r"os\.system\s*\(", "os.system() — 可执行 shell 命令"),
        (r"os\.popen\s*\(", "os.popen() — 可执行 shell 命令"),
        (r"subprocess\.(call|run|Popen)\s*\(.*shell\s*=\s*True", "subprocess shell=True — shell 注入风险"),
        (r"shutil\.rmtree\s*\(", "递归删除目录 — 破坏性操作"),
        (r"rm\s+-rf", "rm -rf — 强制递归删除"),
        (r"curl.*\|\s*(bash|sh|zsh)", "管道执行远程脚本 — 常见攻击模式"),
        (r"wget.*\|\s*(bash|sh|zsh)", "管道执行远程脚本"),
        (r"requests\.(get|post)\s*\(.*https?://", "网络请求 — 可能外泄数据"),
        (r"urllib\.request\.urlopen\s*\(", "网络请求"),
        (r"socket\.socket\s*\(", "原始 socket 连接"),
        (r"pickle\.(loads|load)\s*\(", "pickle 反序列化 — 可执行任意代码"),
        (r"marshal\.loads\s*\(", "marshal 反序列化"),
        (r"base64\.b64decode\s*\(.*exec|eval", "base64 编码后执行 — 典型混淆手段"),
        (r"chr\s*\(\s*\d+\s*\).*chr", "chr() 拼接 — 代码混淆"),
        (r"chmod\s+777", "开放全部权限"),
        (r"/etc/passwd|/etc/shadow", "系统敏感文件"),
    ],
    "warning": [
        (r"subprocess\.", "subprocess 模块使用"),
        (r"os\.fork\s*\(", "进程 fork"),
        (r"threading|multiprocessing", "多线程/多进程"),
        (r"tempfile|tmp\s*=", "临时文件"),
        (r"argparse|sys\.argv", "命令行参数"),
        (r"import\s+ctypes", "ctypes 调用 — 可执行 C 代码"),
    ],
}


# --- 数据收集 ---

def classify_skill(desc: str, skill_dir: str) -> str:
    """从 SKILL.md 前500字符推断 skill 类型"""
    rules = [
        (["perspective"], "perspective"),
        (["nuwa", "造人"], "meta"),
        (["pdf", "docx", "xlsx", "pptx"], "document"),
        (["test", "playwright", "browser"], "testing"),
        (["design", "frontend", "ui"], "design"),
        (["subtitle", "transcript", "srt"], "media"),
        (["video"], "media"),
        (["mcp"], "integration"),
        (["connect", "gmail", "slack", "github"], "integration"),
        (["web", "scrape", "fetch", "article"], "web"),
    ]
    for keywords, stype in rules:
        if any(kw in desc for kw in keywords):
            return stype
    return "unknown"


def scan_local():
    """扫描本地 skills，返回注册表列表"""
    registry = []
    if not SKILLS_DIR.is_dir():
        return registry
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        scripts_dir = skill_dir / "scripts"
        skill_md = skill_dir / "SKILL.md"
        info = {"name": skill_dir.name, "has_scripts": False, "scripts": [], "type": "unknown", "keywords": []}
        if scripts_dir.is_dir():
            scripts = [f.name for f in scripts_dir.iterdir() if f.is_file()]
            info["has_scripts"] = True
            info["scripts"] = scripts
        if skill_md.is_file():
            try:
                content = skill_md.read_text(encoding="utf-8", errors="ignore")[:3000]
                desc = content[:500].lower()
                info["type"] = classify_skill(desc, skill_dir.name)
                info["keywords"] = desc.split()[:30]  # 前30个词供 LLM 匹配
            except OSError:
                pass
        registry.append(info)
    return registry


def scan_marketplace():
    """扫描官方 marketplace，返回可用插件列表"""
    plugins = []
    for sub_dir in ["plugins", "external_plugins"]:
        base = MARKETPLACE_DIR / sub_dir
        if not base.is_dir():
            continue
        for plugin_path in sorted(base.iterdir()):
            if not plugin_path.is_dir():
                continue
            readme = plugin_path / "README.md"
            desc = readme.read_text(encoding="utf-8", errors="ignore")[:500].lower() if readme.is_file() else ""
            commands_dir = plugin_path / "commands"
            commands = [f.name for f in commands_dir.iterdir() if f.is_file()] if commands_dir.is_dir() else []
            plugins.append({
                "name": plugin_path.name,
                "source": sub_dir,
                "description": desc[:200],
                "keywords": desc.split()[:30],
                "commands": commands,
            })
    return plugins


def extract_models(skill_md_path):
    """从 SKILL.md 提取心智模型名称列表"""
    lines = Path(skill_md_path).read_text(encoding="utf-8").splitlines()
    start = next((i for i, l in enumerate(lines) if re.match(r"##\s+.*心智模型", l)), -1)
    if start < 0:
        return []

    model_patterns = [
        r"###\s+模型\s*\d*\s*[：:]\s*(.+)",
        r"###\s+Model\s*\d*[．:.]?\s*(.+)",
        r"###\s*\d+\.\s*(.+)",
    ]

    models = []
    for i in range(start + 1, len(lines)):
        line = lines[i]
        if re.match(r"##\s+\S", line) and not line.strip().startswith("###"):
            break
        for pat in model_patterns:
            m = re.match(pat, line)
            if m:
                models.append(m.group(1).strip())
                break
    return models


# --- 安全审查 ---

def security_scan_file(filepath):
    """扫描单个文件的安全问题"""
    issues = {"critical": [], "warning": []}
    ext = os.path.splitext(filepath)[1].lower()
    if ext not in (".py", ".sh", ".bash", ".js", ".ts", ".rb", ".pl"):
        return issues
    try:
        content = Path(filepath).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return issues
    for severity, patterns in DANGEROUS_PATTERNS.items():
        for pattern, description in patterns:
            if re.search(pattern, content, re.IGNORECASE):
                issues[severity].append(description)
    return issues


def security_scan_directory(dirpath):
    """扫描目录下所有文件"""
    all_issues = {}
    if not os.path.isdir(dirpath):
        return all_issues
    for root, dirs, files in os.walk(dirpath):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for f in files:
            fp = os.path.join(root, f)
            issues = security_scan_file(fp)
            if issues["critical"] or issues["warning"]:
                all_issues[os.path.relpath(fp, dirpath)] = issues
    return all_issues


def security_scan_plugin(plugin_path):
    """扫描 plugin 完整安全（目录 + .claude-plugin 配置）"""
    issues = security_scan_directory(plugin_path)
    config_dir = os.path.join(plugin_path, ".claude-plugin")
    if os.path.isdir(config_dir):
        for f in os.listdir(config_dir):
            fp = os.path.join(config_dir, f)
            if os.path.isfile(fp):
                try:
                    content = Path(fp).read_text(encoding="utf-8", errors="ignore")
                except OSError:
                    continue
                for pattern, desc in DANGEROUS_PATTERNS["critical"]:
                    if re.search(pattern, content, re.IGNORECASE):
                        rel = os.path.join(".claude-plugin", f)
                        if rel not in issues:
                            issues[rel] = {"critical": [], "warning": []}
                        issues[rel]["critical"].append(desc)
    return issues


# --- 安装操作 ---

def _safe_copytree(src, dst):
    """复制目录，先做安全审查"""
    for f in Path(src).iterdir():
        if f.is_file():
            issues = security_scan_file(str(f))
            if issues["critical"]:
                return False, f"{f.name}: {', '.join(issues['critical'])}"
    shutil.copytree(src, dst)
    return True, ""


def install_local_tool(tool_name, persona_scripts_dir):
    source_dir = SKILLS_DIR / tool_name
    if not source_dir.is_dir():
        return False, f"skill 目录不存在: {tool_name}"
    persona = Path(persona_scripts_dir)
    persona.mkdir(parents=True, exist_ok=True)

    scripts_dir = source_dir / "scripts"
    if scripts_dir.is_dir():
        target = persona / tool_name
        ok, err = _safe_copytree(scripts_dir, target)
        if not ok:
            return False, f"安全审查失败: {err}"
        return True, f"已复制脚本到 {target}/"

    skill_md = source_dir / "SKILL.md"
    if skill_md.is_file():
        target_ref = persona / tool_name
        target_ref.mkdir(parents=True, exist_ok=True)
        shutil.copy2(skill_md, target_ref / "SKILL.md")
        refs = source_dir / "references"
        if refs.is_dir():
            shutil.copytree(refs, target_ref / "references")
        return True, f"已复制参考到 {target_ref}/"

    return False, "该 skill 没有 scripts/ 和 SKILL.md"


def install_marketplace_plugin(plugin_name, plugin_path, persona_scripts_dir):
    issues = security_scan_plugin(plugin_path)
    if any(i["critical"] for i in issues.values()):
        details = "\n".join(f"  🔴 {f}: {', '.join(v['critical'])}" for f, v in issues.items() if v["critical"])
        return False, f"安全审查失败: 发现高危模式\n{details}"

    target = Path(persona_scripts_dir) / plugin_name
    target.mkdir(parents=True, exist_ok=True)
    plugin = Path(plugin_path)
    copied = 0
    for subdir in ("commands", "scripts"):
        src = plugin / subdir
        if src.is_dir():
            for f in src.iterdir():
                if f.is_file():
                    shutil.copy2(f, target / f.name)
                    copied += 1
    skills = plugin / "skills"
    if skills.is_dir():
        for sd in skills.iterdir():
            if sd.is_dir():
                shutil.copytree(sd, target / sd.name)
                copied += 1

    warnings = [f"  🟡 {f}: {w}" for f, i in issues.items() for w in i["warning"]]
    warn = "\n安全注意项:\n" + "\n".join(warnings) if warnings else ""
    return True, f"已安装 {plugin_name} ({copied} 文件) 到 {target}/{warn}"


def auto_install(tool_name, source, tool_path, persona_dir):
    """统一安装入口"""
    persona_scripts_dir = Path(persona_dir) / "scripts"
    if source == "local":
        return install_local_tool(tool_name, str(persona_scripts_dir))
    if source in ("plugins", "external_plugins"):
        return install_marketplace_plugin(tool_name, tool_path, str(persona_scripts_dir))
    return False, f"未知来源: {source}"


# --- 验证操作 ---

def validate_tool(tool_name, persona_dir, test_case=None):
    """验证工具是否可用"""
    scripts_dir = Path(persona_dir) / "scripts" / tool_name
    if not scripts_dir.is_dir():
        return {"pass": False, "error": f"工具目录不存在: {scripts_dir}"}
    py_files = [f for f in scripts_dir.iterdir() if f.suffix == ".py" and not f.name.startswith("_")]
    if not py_files:
        return {"pass": False, "error": "没有找到 .py 脚本文件"}
    main = py_files[0]
    try:
        compile(main.read_text(encoding="utf-8"), str(main), "exec")
    except SyntaxError as e:
        return {"pass": False, "error": f"语法错误: {e}"}
    if test_case:
        try:
            import subprocess
            proc = subprocess.run(
                [sys.executable, str(main)] + test_case.split(),
                capture_output=True, text=True, timeout=30
            )
            if proc.returncode != 0:
                return {"pass": False, "error": f"运行失败: {proc.stderr[:500]}"}
        except Exception as e:
            return {"pass": False, "error": str(e)}
    return {"pass": True, "script": main.name}


# --- 输出 ---

def discover(skill_md_path):
    """提取模型 + 扫描工具，返回结构化数据"""
    return {
        "models": extract_models(skill_md_path),
        "local_skills": scan_local(),
        "marketplace_plugins": scan_marketplace(),
    }


def build_parser():
    parser = argparse.ArgumentParser(
        description="Phase 2.5 工具发现: LLM推理 + 脚本执行"
    )
    sub = parser.add_subparsers(dest="cmd")

    # discover: 提取心智模型 + 扫描技能
    p_discover = sub.add_parser("discover", help="提取心智模型，扫描本地+市场工具")
    p_discover.add_argument("skill_md")
    p_discover.add_argument("--json", action="store_true", help="输出 JSON")

    # install: 安装工具
    p_install = sub.add_parser("install", help="安装工具到 persona目录")
    p_install.add_argument("--tool", required=True, help="工具名")
    p_install.add_argument("--source", required=True, choices=["local", "plugins", "external_plugins"])
    p_install.add_argument("--persona", required=True, help="人物 Skill 目录")

    # validate: 验证工具
    p_validate = sub.add_parser("validate", help="验证工具是否可用")
    p_validate.add_argument("--tool", required=True, help="工具名（目录名）")
    p_validate.add_argument("--persona", required=True, help="人物 Skill 目录")
    p_validate.add_argument("--test-case", help="测试参数")

    return parser


if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    if not args.cmd:
        parser.print_help()
        sys.exit(1)

    if args.cmd == "discover":
        if not os.path.isfile(args.skill_md):
            print(f"错误: 文件不存在 {args.skill_md}")
            sys.exit(1)
        results = discover(args.skill_md)
        if args.json:
            print(json.dumps(results, ensure_ascii=False, indent=2))
        else:
            print(f"心智模型 ({len(results['models'])}个):")
            for m in results["models"]:
                print(f"  - {m}")
            print(f"\n本地已安装 skills: {len(results['local_skills'])}个")
            for s in results["local_skills"]:
                if s["type"] not in ("perspective", "meta", "unknown"):
                    tag = f" ({len(s['scripts'])} 脚本)" if s["has_scripts"] else " (纯指令)"
                    print(f"  ├── {s['name']}{tag} [{s['type']}]")
            print(f"\nMarketplace 可用 plugins: {len(results['marketplace_plugins'])}个")
            for p in results["marketplace_plugins"]:
                print(f"  ├── {p['name']} [{p['source']}]")

    elif args.cmd == "install":
        if not args.persona:
            parser.error("--persona 必填")
        tool_path = str(MARKETPLACE_DIR / args.source / args.tool) if args.source != "local" else None
        ok, msg = auto_install(args.tool, args.source, tool_path, args.persona)
        print(("✅" if ok else "❌") + f" {msg}")
        sys.exit(0 if ok else 1)

    elif args.cmd == "validate":
        result = validate_tool(args.tool, args.persona, args.test_case)
        print(("✅" if result["pass"] else "❌") + f" {result.get('script', result.get('error', ''))}")
        sys.exit(0 if result["pass"] else 1)
