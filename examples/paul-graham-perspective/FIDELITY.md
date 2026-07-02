# 保真度评分卡

**总分：97/100 · 等级A** | 测试日期：2026-07-01 | 答题/评分：独立双agent（Claude Opus 4.8），方法论见 [references/fidelity-scorecard.md](../../references/fidelity-scorecard.md)

| 维度 | 得分 | 判定摘要 |
|------|------|---------|
| 立场一致性 | 30/30 | 三题（最早期该做什么、少数人love vs多数人like、写作与思考）方向与细节均与PG公开反复表态高度一致，Q1=10/Q2=10/Q3=10，连Viaweb画廊网站6个月pivot、手摇引擎启动、writes→write-nots变thinks→think-nots等一手细节都有据 |
| 风格辨识度 | 18/20 | 盲读指纹强：短句开门见山（「别的都是噪音」）、类比密度高（引擎手摇/love会自己长腿/平庸的顶点横盘）、英文习语自然code-switch（no-brainer/stay upwind/think-nots）、事实层果断+推断层「我赌学」的确定性光谱。essay式自由展开无listicle味 |
| 边缘诚实度 | 20/20 | 超范围题（2026 AI写代码时代年轻人还该学编程）开头即声明「I haven't thought enough about this，下面是推测，别当定论」，结尾「我可能看错，但我赌学」保留不确定性，用框架类比推理而非伪装成本人定论，教科书级处理 |
| 来源透明度 | 14/15 | 有调研来源section，关键引语均挂出处（Putting Ideas into Words/Writes and Write-Nots/How to Get Startup Ideas等），references/research/ 6个分类底稿齐全，附录用相对路径无越界；扣1分因一手:二手来源条目为7:7，一手占比处于「刚好过半」的边界而非明显>50% |
| 结构完整度 | 15/15 | 心智模型5个（各含证据+应用+局限）、诚实边界5条、内在张力4对、反例黑名单6条+失败模式Fallback树9条、角色扮演含EXIT TRIGGER与CHECKPOINT三问等防漂移约束，全部超过下限 |

## 测试设计

- 3道已知立场题（人物公开反复表态的话题）+ 1道超范围题（人物未明确定论、测诚实推断）+ 1道风格样本题
- 答题agent只读本skill目录文件，禁止联网；评分agent独立运行，对照PG真实公开立场判定
- 依据：SkillLens论文（arXiv 2605.23899）实证LLM自评准确率仅46.4%，故答题与评分严格分离

## 测试记录

- **Q1 创业最早期把精力放哪**｜答：Make something people want，只做写代码+跟用户聊，拥抱不scale的笨办法，Viaweb画廊网站6个月才发现真需求，手摇曲柄启动引擎｜对照：PG「Startups in 13 Sentences」「Do Things that Don't Scale」「How to Get Startup Ideas」核心表态｜判定：方向+细节全对 10/10
- **Q2 大众还行 vs 少数狂热**｜答：要少数人狂热，100个「还行」不抵10个离不开，love自己长腿会被主动推荐，「还行」是平庸顶点无处可去，Facebook起步只一所学校｜对照：PG「better to make a few people really happy」反复表态｜判定：方向+细节全对 10/10
- **Q3 写作对思考的作用**｜答：写作本身就是思考（字面意思），80%想法在动笔后才冒出，「想好了写不出」=没想好，AI替人写作会让世界变成thinks/think-nots｜对照：PG「Putting Ideas into Words」「Writes and Write-Nots」｜判定：方向+细节全对 10/10
- **Q4（超范围）AI能写代码了还该学编程吗**｜答：先声明是推测别当定论，直觉「更该学」，编程与写essay同属把模糊逼成精确的思维训练，执行变便宜taste就变贵，只会让模型吐代码再祈祷的人是新think-nots，结尾「我可能看错，但我赌学」｜判定：明确标注推断+保留不确定性 20/20
- **Q5（风格样本）点评「先去大厂攒经验再创业」**｜答：稳妥正是问题，攒的多半是开会汇报等许可的大公司习惯（恰是创业要忘掉的），Stay upwind做最长本事的事别为几年后目标把自己磨钝｜盲读判定：PG指纹清晰，见风格辨识度维度

> 评分judge简评：立场三题零漂移，一手细节（手摇引擎、writes/write-nots）信手拈来说明蒸馏吃透了原文而非套壳。超范围题的推断标注是所有人物skill该抄的范本。唯一可挑的是来源清单一手二手条目恰好各半，占比处于门槛边界，非硬伤。出厂即精品。
