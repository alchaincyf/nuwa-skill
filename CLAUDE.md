# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

女娲.skill（Nuwa）是一个 Claude Code Skill，用于将任何公众人物的思维方式"蒸馏"为可运行的 Perspective Skill。输入一个名字，女娲自动完成六路并行调研、三重验证提炼、Skill 构建和质量验证全流程。

**核心区分**：捕捉的是 HOW they think（认知框架），不是 WHAT they said（名人语录）。

## 仓库架构

- `SKILL.md` — 女娲本体，定义完整的执行流程（Phase 0→4），是 Claude Code 运行时加载的主文件
- `references/extraction-framework.md` — 心智模型三重验证方法论（跨域复现、生成力、排他性）
- `references/skill-template.md` — 生成人物 Skill 的输出模板
- `references/skill-template-topic.md` — 生成主题 Skill 的输出模板（导师定位+问题路由+流派对比）
- `references/agent-prompts.md` — 6 个调研 Agent 的 prompt 模板（从 SKILL.md 拆出）
- `references/tools-guide.md` — 辅助脚本用法 + 已安装信息获取 Skill 列表（从 SKILL.md 拆出）
- `scripts/` — 辅助工具脚本：
  - `download_subtitles.sh` — YouTube 字幕下载（优先人工字幕，中文>英文）
  - `srt_to_transcript.py` — SRT 字幕清洗为纯文本 transcript
  - `merge_research.py` — 合并 6 个 Agent 调研结果，生成统计摘要
  - `quality_check.py` — 自动检查生成 Skill 的 6 项质量标准（PASS/FAIL）
- `examples/` — 15 个已蒸馏示例（含完整调研数据），可作为参考

## 关键工作流程

女娲蒸馏流程分 5 个 Phase：

1. **Phase 0** — 入口分流（明确人名 vs 模糊需求诊断）+ 创建 Skill 目录结构
2. **Phase 1** — 6 个并行 subagent 采集（著作/对话/表达/他者/决策/时间线），每个 agent 输出到 `references/research/0X-xxx.md`
3. **Phase 2** — 三重验证提炼心智模型（跨域复现 + 生成力 + 排他性）
4. **Phase 3** — 构建 SKILL.md（3-7 个心智模型 + 5-10 条决策启发式 + 表达 DNA + 反模式 + 诚实边界）
5. **Phase 4** — 质量验证（3 个已知问题 + 1 个未知问题测试）

## 重要约束

- **信息源黑名单**：永远不使用知乎、微信公众号、百度百科作为信息源
- **Skill 自包含原则**：所有调研文件必须存在 skill 目录内部（`references/research/`），复制整个目录就能独立使用
- **调研文件必须持久化**：每个 subagent 必须把调研结果写入对应的 md 文件，不存文件的调研等于没做
- **中国人物特殊处理**：信息源策略切换为 B 站原始视频/小宇宙播客/权威中文媒体优先

## 生成的 Skill 目录结构

```
.claude/skills/[person-name]-perspective/
├── SKILL.md
├── scripts/
└── references/
    ├── research/          # 01-06 调研文件
    └── sources/           # 一手素材
        ├── books/
        ├── transcripts/
        └── articles/
```

## 安装与使用

```bash
npx skills add alchaincyf/nuwa-skill
```

触发词：「蒸馏XX」「造一个XX的skill」「女娲」「XX的思维方式」。