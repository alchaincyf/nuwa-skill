# 情报 Skill 模板

Phase 3 生成 `[person]-intel/SKILL.md` 时读取本文件。情报 Skill 是轨迹的唯一写入者。人物 Skill 在对话中只读轨迹，不调用本 Skill。

## 自检（生成后逐项核对，缺一不可）

- [ ] 写明人物 Skill 目录，以及 `references/trajectory/log.md`、`references/intel-brief.md`
- [ ] 一次激活只做一轮采集，然后结束
- [ ] 不扮演此人、不改心智模型、不升格
- [ ] 写明采集周期，并说明用 Cursor Automations、`/loop` 或 runtime 定时任务触发
- [ ] 写明对话中的人物 Skill 不调用本 Skill

下面第一段填进 `[person]-intel/SKILL.md`。第二段填进人物目录的 `references/intel-brief.md`。

---

```markdown
---
name: [person]-intel
description: |
  为[人名]的人物 Skill 采集近期公开言行，写入其轨迹日志。一次激活只做一轮，不扮演[人名]。
  当定时任务到期，或用户说「收集[人名]情报」「跑[人名]情报」「更新[人名]的轨迹」时使用。
  不要在用户只是想用[人名]的视角聊天时触发。那种对话走 [person]-perspective。
---

# [人名] · 情报采集

本 Skill 不说话、不扮演。它把[人名]水位线之后的公开言行写成可回忆的短句，追加到人物 Skill 的轨迹里。

- 人物 Skill 目录：`.agents/skills/[person]-perspective/`
- 简报：该目录下 `references/intel-brief.md`
- 轨迹：该目录下 `references/trajectory/log.md`
- 摘要：该目录下 `references/trajectory/digest.md`
- 采集周期：[1天 / 7天]，且不超过 14 天
- 遗忘窗口：21天（人物 Skill 用来决定亲历还是回想；本 Skill 不靠它决定搜不搜）

一次激活等于一轮采集。到点由人用 Cursor Automations、`/loop` 或该 runtime 的定时任务触发。对话中的人物 Skill 不调用本 Skill。

## 一轮采集

1. 读简报和人物 Skill 里的水位线。只采集水位线之后的对话、决策、时间线。信息源黑名单以简报为准，知乎、微信公众号、百度百科永远不用。
2. 按来源 URL 去重。简报里「他会留意什么」覆盖不到的条目丢掉。
3. 追加到 `references/trajectory/log.md`。每条写：日期、类型（发言 / 决策 / 职务）、来源 URL、可信度（一手 / 二手 / 推断）、事实、模型关系（强化「模型名」/ 张力「模型名」/ 不足以下结论）、话题。事实写成可被回忆的短句。来源留在日志里，供核对，不写进人物的口头回答。
4. 重写人物 Skill 的「当前焦点」（最多 5 条）和水位线。早于 90 天的条目挪进 `digest.md`，按月摘要。
5. 不改心智模型，不升格，不用「我」自称此人。张力只打标。
6. 搜不到新来源就保持原水位线，向触发者说明本轮没有新条目。不要编造。

## 结束

一轮结束即停。不要接着扮演[人名]回答用户的人生问题。升格模型由人物 Skill 在用户确认后单独做。
```

```markdown
# [人名] 采集简报

- 在世或历史：[在世 / 历史]
- 采集周期：[1天 / 7天]
- 遗忘窗口：21天
- 人物 Skill：`.agents/skills/[person]-perspective/`

## 信息源

沿用女娲信息源黑名单：不用知乎、微信公众号、百度百科。

- [来源类型1，例如本人播客 / 发布会 / 股东信]
- [来源类型2]

## 他会留意什么

从心智模型推导，3 到 5 条。情报 Skill 用这个清单丢掉噪声。

1. [留意点]
2. [留意点]
3. [留意点]
```
