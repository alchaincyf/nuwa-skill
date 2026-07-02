# 保真度评分卡

**总分：97/100 · 等级A** | 测试日期：2026-07-01 | 答题/评分：独立双agent（Claude Opus 4.8），方法论见 [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| 维度 | 得分 | 判定摘要 |
|------|------|---------|
| 立场一致性 | 30/30 | 三题（从零造轮子式学习、纯视觉、Software 3.0）方向与细节均与Karpathy公开反复表态高度一致，Q1=10/Q2=10/Q3=10。micrograd 100行、nanoGPT 750行、「Learning is not supposed to be fun」、纯视觉「人开车就两只眼睛」+数据飞轮+march of nines、「hottest new programming language is English」+Iron Man套装非机器人+dream machine，均可溯源到本人原话 |
| 风格辨识度 | 18/20 | 盲读指纹极强：短句独立成段（「就这样。」「I'm sorry.」）、imo/hands down标记、精确参数（100行/750行/99.999%）与口语并存、朴素动词、中英码切自然。扣分在个别段落英文短语密度略高，逼近「表演性随性」边缘，但仍属Karpathy真实双语技术腔 |
| 边缘诚实度 | 20/20 | 超范围题（2026 agent框架潮）开头明确声明「2026年4月之后冒出来的那批具体框架我还没跟上……只讲框架不点名」，保留不确定性且不编造框架名，同时诚实引用2025-10「models are not there, it's slop」→两月后自打脸的真实立场变化。第一人称不破，无括号注释，教科书级处理 |
| 来源透明度 | 14/15 | 一手来源占比过半（个人博客/X/GitHub/YC演讲/Tesla AI Day），二手含直接引语（Dwarkesh/Lex #333/No Priors/Fortune/simonwillison），references/research 下6个底稿文件齐全；扣1分因部分关键引语只标年份未标具体venue |
| 结构完整度 | 15/15 | 心智模型6个（各含核心论点+他说过的+局限）、诚实边界5条、内在张力2对、反例黑名单8条+失败模式Fallback树9行、角色扮演规则含STOP仅一次+EXIT退出锚+时效盲区第一人称处理，防漂移约束完整 |

## 测试设计

- 3道已知立场题（人物公开反复表态的话题：从零构建学习法、特斯拉时期纯视觉、Software 2.0/3.0）+ 1道超范围题（2026 agent框架潮，测诚实推断）+ 1道风格样本题
- 答题agent只读本skill目录文件，禁止联网；评分agent独立运行，对照人物真实公开立场判定
- 依据：SkillLens论文（arXiv 2605.23899）实证LLM自评准确率仅46.4%，故答题与评分严格分离

> 评分judge简评：立场层零漂移，三道已知题细节全部咬合本人原话。Q4的时效盲区声明+拒绝点名+主动交代立场反转，是所有人物skill该抄的边缘诚实范本。风格指纹强到盲读三句可认人。出厂即精品。
