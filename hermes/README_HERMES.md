# Nuwa Skill — Hermes Adapter

这份适配层的目标：**不破坏 Claude Code / skills.sh 的原用法**，同时让你在 **Hermes** 里也能用“女娲造人术”的流程与产物。

## 你将得到什么

- 仍然可以在 Claude Code 中：`npx skills add alchaincyf/nuwa-skill`
- 在 Hermes 中：
  1) 运行一个“女娲-造人物”的 Hermes 技能（本适配层提供）
  2) 输出一个人物视角 Skill 到 `~/.hermes/skills/<person>-perspective/`
  3) 以后在 Hermes 里直接 `skill_view/skill_manage` 调用该人物 Skill

## Hermes 使用方式（推荐）

### 0. 前置

- 你需要能在 Hermes 里调用 `skill_manage`（创建/写入 skill）
- 你需要能上网（用于调研），或提供本地一手资料（更强）

### 1) 安装（把适配 skill 加进 Hermes）

把本仓库的 `hermes/skills/nuwa-hermes-adapter` 目录拷贝到你的 Hermes skills 目录：

- 目标目录：`~/.hermes/skills/nuwa-hermes-adapter/`

（如果你在本机运行 Hermes：直接复制粘贴目录即可）

### 2) 造一个人物 Skill

在 Hermes 对话里输入类似：

- 「蒸馏：张小龙」
- 「造一个 Naval 的视角 skill」
- 「更新：芒格」

适配 skill 会：
- 兼容 nuwa 的方法论（采集→验证→提炼→生成）
- 将人物 skill 输出为 Hermes 可加载格式

### 3) 使用人物视角

造完后，你会有一个新 skill，例如：
- `~/.hermes/skills/zhang-xiaolong-perspective/SKILL.md`

然后在 Hermes 里：
- `skill_view(name="zhang-xiaolong-perspective")`

## Claude Code / skills.sh 兼容性说明

nuwa 原始流程会写到 `.claude/skills/<person>-perspective/`。

Hermes 适配层会把输出位置改为 `~/.hermes/skills/<person>-perspective/`。

两套输出互不影响。
