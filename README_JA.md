<div align="center">

# 女娲.skill (Nuwa)

> *「蒸留すべき次の人物は、同僚である必要はない」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**Nuwaは誰の思考法でも蒸留できる。マスク、Naval、マンガー、ファインマンをあなたのために働かせよう。**

<br>

[colleague-skill](https://github.com/titanwings/colleague-skill) は、人をAIスキルに蒸留することが実現可能だと証明した。
なぜ同僚だけに留まるのか？マンガー、ファインマン、マスクを蒸留しよう。
名前を入力するだけで、Nuwaが調査・抽出・検証の全プロセスを自動で行う。

[使用例](#使用例) · [インストール](#インストール) · [Nuwaが蒸留するもの](#nuwaが蒸留するもの) · [仕組み](#仕組み)

<br>

**他の言語:**

[中文](README.md) · [English](README_EN.md) · [한국어](README_KO.md) · [Español](README_ES.md)

</div>

---

## 使用例

```
ユーザー  ❯ コンテンツ制作、本の執筆、個人開発を同時にやりたいが、
             エネルギーが全然足りない。

Naval    ❯ 君は三つの欲望をリストアップした。
             それぞれの欲望は、不幸と結んだ契約だ。
             エネルギーが足りないのではなく、契約が多すぎるんだ。

             自分に問いかけてみろ：どれをやると時間を忘れる？
             それが君の固有知識のありかだ。

             三つの中からひとつを選び続けるわけじゃない。
             まず一つ、次に一つ、またその次に一つ。
             直列の複利、並列の消耗ではなく。
```

```
ユーザー  ❯ 私たちのSaaSの顧客獲得コストが高すぎる。

マスク    ❯ まず削減方法を考えるな。物理的な最小値を計算しろ。
             顧客獲得に必要な最小限のアクションは何だ？
             ユーザーがあなたを知ってから支払うまでの、
             理論上の最短経路は何だ？

             実際の経路は理論上の経路の何倍か？
             3倍を超えているなら、必ず削除できるステップがある。
             ファネルを最適化するな、ファネル自体の存在を疑え。
```

これはロールプレイではない。Navalは「欲望=契約」というメンタルモデルを使い、マスクは「漸近的限界法」を使っている。**名言を繰り返しているのではなく、これらの人物の認知フレームワークを通じてあなたの問題を分析している。**

---

## インストール

```bash
npx skills add alchaincyf/nuwa-skill
```

Claude Codeで:

```
> ポール・グレアムを蒸留して
> 張小龍の視点スキルを作って
> 段永平のスキルを作ってほしい
```

作成後、直接呼び出す:

```
> マンガーの視点でこの投資判断を分析して
> ファインマンなら量子計算をどう説明する？
> Navalに切り替えて、三つのことで迷っている
```

---

## Nuwaが蒸留するもの

各分野の最高の人物を蒸留するには、日常の作業習慣よりも深いものを抽出する必要がある。Nuwaは六層を抽出する:

| 層 | 説明 |
|---|---|
| **話し方** | 表現のDNA — 口調、リズム、語彙の好み |
| **考え方** | メンタルモデル、認知フレームワーク |
| **判断の仕方** | 意思決定のヒューリスティクス |
| **しないこと** | アンチパターン、価値観の底線 |
| **誠実な限界** | スキルが本当にできないこと |

作業習慣はプロセス文書で伝えられる。だが、マンガーとマスクが同じ問題に対して異なる結論を出す理由は、認知フレームワークにある。Nuwaが抽出するのは認知オペレーティングシステムだ。

### 誠実な限界

すべてのスキルは、できないことを明示する:

- 直感は蒸留できない — フレームワークは抽出できるが、インスピレーションはできない
- 変化は捉えられない — 調査時点のスナップショットに過ぎない
- 公開発言 ≠ 本音 — 公開情報のみに基づく

**自分の限界を教えてくれないスキルは、信頼に値しない。**

---

## 仕組み

名前を入力すると、Nuwaは四つのことを行う:

**1. 六つの並列調査** — 著作、ポッドキャスト/インタビュー、SNS、批評者の視点、意思決定記録、人生年表。6つのエージェントが同時に動き、それぞれアーカイブする。

**2. 三重検証による抽出** — ある主張をメンタルモデルとして記録するには三つのテストをパスする必要がある: 2つ以上の領域で登場している（一度限りの発言ではない）、新しい問題への立場を予測できる（予測力がある）、賢い人なら誰でも考えることではない（排他性がある）。三つすべてが必要。

**3. スキルの構築** — 3〜7のメンタルモデル + 5〜10の意思決定ヒューリスティクス + 表現DNA + 価値観・アンチパターン + 誠実な限界をSKILL.mdに書き込む。

**4. 品質検証** — その人が公開で回答したことがある3つの質問でテスト、方向性が一致していれば合格。次に、その人が議論したことのない1つの質問でテスト、スキルは断言せず適度な不確実性を示すべき。

完全な方法論は `references/extraction-framework.md` にある。

---

## リポジトリ構造

```
nuwa-skill/
├── SKILL.md                    # Nuwa本体
├── references/
│   ├── extraction-framework.md # 抽出方法論（深く理解したい人はこれを）
│   └── skill-template.md       # スキル生成テンプレート
└── examples/                          # 15人物 + 1テーマ、完全な調査データ付き
    ├── steve-jobs-perspective/        # ジョブズ（デモ対話付き）
    ├── paul-graham-perspective/       # Paul Graham
    ├── zhang-yiming-perspective/      # 張一鳴
    ├── andrej-karpathy-perspective/   # Karpathy
    ├── ilya-sutskever-perspective/    # Ilya Sutskever
    ├── trump-perspective/             # トランプ
    ├── mrbeast-perspective/           # MrBeast
    ├── elon-musk-perspective/         # マスク
    ├── munger-perspective/            # マンガー
    ├── buffett-perspective/           # バフェット
    ├── feynman-perspective/           # ファインマン
    ├── naval-perspective/             # Naval Ravikant
    ├── taleb-perspective/             # タレブ
    ├── liurun-perspective/            # 劉潤
    ├── zhangxuefeng-perspective/      # 張雪峰
    └── x-mastery-mentor/             # X導師（テーマスキル）
```

調査プロセスはすべて透明だ。examplesには完全な調査ファイルが含まれており、情報がどのように収集・フィルタリングされ、メンタルモデルになったかを確認できる。

---

## Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=alchaincyf/nuwa-skill&type=Date)](https://star-history.com/#alchaincyf/nuwa-skill&Date)

</div>

---

## 背景

[colleague-skill](https://github.com/titanwings/colleague-skill) は最近GitHubで爆発的に広まった — 退職した同僚をAIスキルに蒸留し、数日で5000スターを突破した。これは一つのことを証明した: 人を蒸留することは完全に実現可能だ。

人を蒸留する能力があるなら、なぜ近くにいる同僚だけに留まるのか？各分野で最高の人物を蒸留しよう。幸いにも、そういう人たちは通常、大量の蒸留可能な素材を残している — 著作、講演、インタビュー、SNS。これは自分の能力を大幅に補強することになる。

以前からこのようなことをやっていた — 同僚ではなく、マンガー、ファインマン、Naval、マスク、タレブを蒸留していた。今日、その方法論をオープンソース化する。

Nuwaは人をコピーしない。認知オペレーティングシステムを抽出する。

**女娲（Nuwa）**は、中国神話で泥から人間を創った女神だ。ここでの泥は公開情報であり、創られるのは人ではなく、鏡だ。

---

## 作者について

花叔（Huashu）/花生（Huasheng）、AI Native Coder、インディー開発者。すべての製品はAIが書いたコードで構築（[子猫フィルライト](https://apps.apple.com/app/id6738028637)が中国App Store有料チャート1位を達成）。Claude Codeで40+のカスタムスキルを実行中。Nuwaはスキルを作るスキルだ。

- WeChat公式アカウント: 花叔
- X: [@AlchainHust](https://x.com/AlchainHust)
- Bilibili: [花叔](https://space.bilibili.com/14097567)
- YouTube: [@Alchain](https://www.youtube.com/@Alchain)

## ライセンス

MIT — 自由に使い、改変し、構築しよう。

---

<div align="center">

**colleague-skill** は人が何をするかを蒸留した。<br>
**Nuwa** は人がどのように考えるかを蒸留する。<br><br>
*蒸留すべき次の人物は、同僚である必要はない。*

<br>

MIT License © [Huashu](https://github.com/alchaincyf)

</div>
