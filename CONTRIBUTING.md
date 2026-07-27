# 贡献指南 / Contributing

感谢你想为女娲生态出力。先读这一页，能帮你的贡献走对路，也能省掉双方的往返。

## 一条核心规则

**`SKILL.md` 是本仓库的核心资产，不接受外部PR改动。** 女娲方法论的每一行都经过维护者的实测验证和版本化优化（见darwin-skill流程），任何对它的修改只由维护者本人完成。

这不是拒绝你的想法——如果你发现了方法论的bug或改进点，**开issue讨论**。被采纳的想法会由维护者写进SKILL.md，并在commit中致谢你（先例：PR #59发现的description超限bug已按此方式采纳）。

## 贡献人物Skill：走社区索引，不走examples/

`examples/` 是维护者出品的官方示范，保持统一的质量口径。社区蒸馏的人物skill走这条路：

1. **放进你自己的GitHub仓库**（一个skill一个仓库，star和维护权都归你）
2. **跑一遍保真度评分**（见 [references/fidelity-scorecard.md](references/fidelity-scorecard.md)），在仓库里放一份 `FIDELITY.md`
3. **提PR把你的仓库链接加进 [COMMUNITY.md](COMMUNITY.md)**，一行搞定

这对你更划算：你的作品有自己的门牌和star数，还能持续迭代不受本仓库节奏限制。

### 收录COMMUNITY.md的门槛

- 用女娲流程蒸馏，仓库内含 `references/research/` 调研底稿（自包含，可溯源）
- 有「诚实边界」和「反模式」章节
- 保真度评分卡 ≥ B（70分），仓库根目录放 `FIDELITY.md`
- `FIDELITY.md` 的关键字段（测试日期/总分/各维评分）须为独立双agent实测的真实值，不得是「待跑」「预估」「TBD」「YYYY-MM-DD」等占位或预估——机器检查按此拦截
- 通过伦理红线检查（见下）

提交收录PR后，机器人会自动检查以上形式门槛并把✅/❌清单贴成评论（改完推送会自动重跑）；机器检查通过后，维护者人工确认伦理红线和内容质量即可合并。

## 伦理红线（不收录，也请不要提交）

- 未经本人同意蒸馏**在世的非公众人物**（同事、前任、普通人）
- 用于冒充、骚扰、诈骗场景的skill
- 医疗、法律、投资等高责任领域的skill，若无明确免责声明和「不能替代专业人士」边界

## 其他贡献类型

| 类型 | 怎么提 |
|------|--------|
| 方法论bug/改进想法 | 开issue讨论（不要直接PR改SKILL.md） |
| scripts/工具脚本修复 | 直接PR，说明复现步骤 |
| README翻译/文档错别字 | 直接PR |
| 衍生工具/合集/编排项目 | 提PR加进COMMUNITY.md |

## PR Checklist

- [ ] 没有改动 `SKILL.md`
- [ ] 没有 `.DS_Store` 等垃圾文件
- [ ] 一个PR只做一件事（不要多个人物打包）
- [ ] PR描述说清楚：做了什么、为什么、怎么验证的

---

## English Summary

- **`SKILL.md` is the core asset and does not accept external PRs.** Found a bug or improvement? Open an issue — adopted ideas are implemented by the maintainer with credit in the commit.
- **Persona skills go to the community index, not `examples/`**: host the skill in your own repo (you keep the stars), run the [fidelity scorecard](references/fidelity-scorecard.md) (grade B or above), then PR a one-line entry to [COMMUNITY.md](COMMUNITY.md).
- **Ethics**: no distilling living private individuals without consent; no impersonation/harassment use cases; medical/legal/financial personas need explicit disclaimers.
