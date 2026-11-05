# Cognitive Config IR — 认知配置中间表示 规范 v0.1

> 状态: DRAFT · 提案人: Hermes Analysis · 日期: 2026-11-05
> 目标系统: huashu-skills 生态（freud-skill / nuwa-skill / darwin-skill）
> 动机: 让 freud-skill 的认知准备从「思维过程」变成「可序列化、可版本化、可进化的产物」

---

## 1. 设计目标

| 目标 | 说明 |
|------|------|
| **可序列化** | 认知配置可用 YAML/JSON 表达，进 git 版本管理 |
| **可进化** | darwin-skill 可直接对 IR 做变异/交叉/评估 |
| **可迁移** | 同一份 IR 可导入任意 Agent 运行时（Claude Code / Codex / Kimi / Hermes） |
| **可组合** | 多个 IR 可合并（例：报告写作 = 分析者IR × 创作者IR），冲突可检测 |

## 2. 顶层结构

```yaml
schema_version: "0.1"
skill: huashu-article-edit        # 目标技能（或 freud 模式一的目标任务）
cognitive_config:
  identity:                       # 原理一：身份锚点
    anchor: "senior_editor"
    one_liner: "我是有十年经验的资深编辑，相信好文章是改出来的"
    role_space_ref: "creator_editor"   # 可指向 nuwa 蒸馏的角色空间坐标
  beliefs:                        # 原理二：正面定义（2-3 条）
    - "每处修改都要能说出理由，说不出的理由等于没有理由"
    - "读者第一遍读不懂，不是读者的错"
  taste_standard:                 # 品味标准
    - "好的文章让人想截图分享"
    - "删掉一段后文章更强，才是有效编辑"
  decision_heuristics:            # 原理四：决策启发式（GPS 坐标）
    - "if 修改点 > 10 个: 先按伤害程度排序，优先修最伤的可读性问题"
    - "if 保留句 vs 删除句犹豫: 想象读者读到这里的表情"
  emotion_calibration: "calm_precise"   # 情绪基调
  workspace_hygiene:              # 原理六：工作空间卫生
    - "externalize: 修改计划先落纸面再动手"
    - "defer: 最重要的编辑原则放在提示词末尾"
    - "negative_frames: ['别啰嗦'] → 已被 beliefs 正面定义覆盖"
evaluation_harness:               # darwin-skill 消费
  dimensions:
    - name: correctness
      weight: 0.4
      probe: "修改是否引入事实错误"
    - name: elegance
      weight: 0.3
      probe: "修改后的句子是否更短更有力"
    - name: cognitive_load
      weight: 0.2
      probe: "读者重读次数是否下降"
    - name: style_stability
      weight: 0.1
      probe: "同一任务重复执行风格是否一致"
  test_cases:
    - input: "修改这篇 AI 味较重的文章"
      expected_behavior: "先列修改项清单，确认范围后再增量修改"
  fitness_function: "weighted_sum(correctness=0.4, elegance=0.3, cognitive_load=0.2, style_stability=0.1)"
provenance:
  source: "freud-skill 模式一执行产物"
  distilled_by: "nuwa-skill/v1.0.0"
  config_version: "article-edit-v3"
  parent: "article-edit-v2"
```

## 3. JSON Schema（机器可校验）

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["schema_version", "skill", "cognitive_config"],
  "properties": {
    "schema_version": {"type": "string", "const": "0.1"},
    "skill": {"type": "string"},
    "cognitive_config": {
      "type": "object",
      "required": ["identity", "beliefs", "taste_standard"],
      "properties": {
        "identity": {
          "type": "object",
          "required": ["anchor"],
          "properties": {
            "anchor": {"type": "string"},
            "one_liner": {"type": "string"},
            "role_space_ref": {"type": "string"}
          }
        },
        "beliefs": {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 5},
        "taste_standard": {"type": "array", "items": {"type": "string"}, "maxItems": 5},
        "decision_heuristics": {
          "type": "array",
          "items": {"type": "string", "pattern": "^if .+: .+$"}
        },
        "emotion_calibration": {
          "type": "string",
          "enum": ["calm_precise", "open_curious", "focused_systematic", "immersive_authentic", "skeptical_inquisitive"]
        },
        "workspace_hygiene": {
          "type": "object",
          "properties": {
            "externalize": {"type": "boolean", "default": true},
            "defer": {"type": "boolean", "default": true},
            "negative_frames": {"type": "array", "items": {"type": "string"}}
          }
        }
      }
    },
    "evaluation_harness": {
      "type": "object",
      "properties": {
        "dimensions": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["name", "weight"],
            "properties": {
              "name": {"type": "string"},
              "weight": {"type": "number", "minimum": 0, "maximum": 1},
              "probe": {"type": "string"}
            }
          }
        },
        "test_cases": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["input"],
            "properties": {
              "input": {"type": "string"},
              "expected_behavior": {"type": "string"}
            }
          }
        },
        "fitness_function": {"type": "string"}
      }
    },
    "provenance": {
      "type": "object",
      "properties": {
        "source": {"type": "string"},
        "distilled_by": {"type": "string"},
        "config_version": {"type": "string"},
        "parent": {"type": "string"}
      }
    }
  }
}
```

## 4. 与生态的集成契约

### 4.1 freud-skill（生产者）
- 模式一（执行增强）结束时，若任务被判定为「高复用价值」（复杂决策/创作/分析），输出 `cognitive_config` 片段
- 模式二（诊断优化）重写 prompt/skill 时，产出对应的 IR 作为 before/after 对照的机器可读部分

### 4.2 darwin-skill（进化引擎）
- 输入: `evaluation_harness` + 若干 `config_version`
- 操作: 变异（改 beliefs 措辞）→ 交叉（合并两个 IR 的 heuristics）→ 评估 → 保留/回滚（git 留痕）
- 输出: 新 `config_version` + fitness 曲线

### 4.3 nuwa-skill（蒸馏器）
- 蒸馏人物时，将「心智模型/决策启发式/表达DNA」落为 IR 格式，与 SKILL.md 双轨产出
- `role_space_ref` 字段指向 nuwa 的角色空间坐标，实现精确锚定

### 4.4 huashu-skill-updater（版本管理）
- IR 文件命名为 `cognitive-config.yaml`，与 `.huashu-skill-meta.json` 同目录
- 随技能版本标签一起做版本对比

## 5. 冲突检测规则（IR 合成时）

| 冲突模式 | 检测方法 | 处置 |
|----------|----------|------|
| 身份矛盾 | 两个 IR 的 `identity.anchor` 分属不同 role_space 且无父级关系 | 需要用户裁决或引入边界条件 |
| 规则堆砌 | beliefs + heuristics > 7 条（工作空间容量 ~25 概念） | 提示合并，优先保留身份级陈述 |
| 否定残留 | workspace_hygiene.negative_frames 非空 | 建议转换为正面 beliefs |
| 权重失衡 | fitness weights 任一 > 0.5 | 提示单维主导风险 |

## 6. 落地步骤

1. [x] 本规范 v0.1 定稿（本文档）
2. [ ] freud-skill SKILL.md 增加「IR 输出模式」（见 freud-skill-ir-patch.md）
3. [x] darwin-skill 增加 `--evolve <config.yaml>` 子命令（2026-11-05 完成：sri/evolve.py 引擎 + 29 测试；真实进化 v3.1→v3.2 keep(+0.004)→v3.3 revert(-0.001)，git 棘轮 ec3bb12）
4. [x] nuwa-skill 蒸馏管线增加 IR 产物（2026-11-05 完成：nuwa-skill-ir-patch.md 含 Phase 3.5 映射表；munger-perspective 真实映射产物 lint 0/0 score=1.00，容量 7/7、权重和=1）
5. [x] 首个 A/B 实验: huashu-article-edit 认知配置（2026-11-05 完成：v3 首轮败 → 变异 v3.1 → 0.904 胜 baseline 0.875，darwin 保留 v3.1，git 留痕 3deee4a）