---
name: nuwa-hermes-adapter
version: 0.1.0
source: https://github.com/alchaincyf/nuwa-skill
adapter_repo: https://github.com/MEJ50749/nuwa-skill
license: MIT
---

# 女娲（Hermes 适配层）

目的：把 `alchaincyf/nuwa-skill` 的“蒸馏人物→生成可运行 skill”的方法论，适配到 Hermes 的 skill 体系中。

## 你说一句话就能触发

- 「女娲，蒸馏张小龙」
- 「造一个 Naval 视角 skill」
- 「更新芒格的 skill」

## 输出

- 新建/更新 Hermes skill：`~/.hermes/skills/<person>-perspective/SKILL.md`

## 执行步骤（Hermes Agent）

1) 识别用户输入：
   - 明确人名：直接蒸馏
   - 模糊需求：先用 1-2 个追问定位维度，再推荐 1-3 个候选人物，用户选定后蒸馏

2) 采集语料（六路并行思想，但在 Hermes 中可串行执行）：
   - 著作/文章
   - 访谈/播客
   - 社交媒体/公开讲话
   - 批评者视角
   - 决策记录/案例
   - 人生时间线

3) 三重验证提炼（收录为心智模型的准入门槛）：
   - 跨 2+ 领域出现
   - 能推断对新问题立场（预测力）
   - 具排他性（不是人人都这么想）

4) 生成人物 Skill（Hermes 兼容格式）：
   - 3-7 心智模型
   - 5-10 决策启发式
   - 表达 DNA
   - 价值观/反模式
   - 诚实边界
   - 3 个公开问答回测 + 1 个未知问题的不确定性测试

5) 写入 skill：
   - skill 名：`<slug>-perspective`
   - 用 `skill_manage(action='create', name=..., content=...)` 创建

## 产物模板（生成的 SKILL.md 必须包含）

- YAML frontmatter：name / description / triggers（可选）
- 使用方式：
  - “用 XX 视角分析/解释/决策”
  - “当我输入材料 A 时，XX 会如何提问/拆解”
- 诚实边界：哪些问题它不该装懂

## 注意

- 不要冒充本人。明确：这是对其公开思维方式的蒸馏。
- 遇到缺乏材料或冲突材料：给出不确定性，并标注依据来源类型。
