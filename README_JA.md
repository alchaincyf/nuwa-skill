<div align="center">

# 女娲.skill (Nuwa)

> *「蒸留すべき次の人物は、同僚である必要はない」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green)](https://agentskills.io)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-blue)](https://skills.sh)
[![Multi-Runtime](https://img.shields.io/badge/Runtime-Claude%20Code%20·%20Codex%20·%20Cursor%20·%20OpenClaw%20·%20Hermes-blueviolet)](#インストール)

<br>

**Nuwaは誰の思考法でも蒸留できる。マスク、Naval、マンガー、ファインマンをあなたのために働かせよう。**

<sub>オープンな [Agent Skills](https://agentskills.io) 標準に基づき構築。Claude Code、Codex、Cursor、OpenClaw、Hermes Agent、CodeBuddy、Workbuddy、Gemini CLI、OpenCode など 50+ の skills 互換 runtime で動作。</sub>

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

Nuwa はオープンな [Agent Skills](https://agentskills.io) 標準に基づき構築されており、skills 互換の任意の AI agent runtime で動作する。

### 方法1：ワンライナー（推奨、クロス runtime）

お使いの agent（Claude Code、Codex、Cursor、OpenClaw、Hermes、CodeBuddy、Workbuddy、Gemini CLI、OpenCode など 50+ 対応）に伝える：

```
このskillをインストールして：https://github.com/alchaincyf/nuwa-skill
```

または、汎用 CLI インストーラ（[vercel-labs/skills](https://github.com/vercel-labs/skills)、55+ runtime 対応）を使う：

```bash
npx skills add alchaincyf/nuwa-skill
```

現在の runtime を自動検出し、正しいディレクトリに skill を配置する。特定 runtime を指定する場合は `-a claude-code` / `-a codex` / `-a cursor` / `-a openclaw` などを付ける。

### 方法2：手動インストール

<details>
<summary>各 runtime の skills ディレクトリ</summary>

| Runtime | パス |
|---|---|
| Claude Code | `~/.claude/skills/nuwa-skill/` |
| Codex CLI | `~/.codex/skills/nuwa-skill/` |
| Cursor | `~/.cursor/skills/nuwa-skill/` |
| OpenClaw | `~/.openclaw/workspace/skills/nuwa-skill/` |
| Hermes Agent | `tools/install_hermes_skill.py` を実行 |
| その他 | 該当 runtime の `skills/` ディレクトリに clone |

```bash
git clone https://github.com/alchaincyf/nuwa-skill <上記のパス>
```

</details>

### 方法3：参考資料として使う（runtime 不要）

skills を自動ロードしない runtime でも、`SKILL.md` の内容を会話にペーストすればよい——本質はただの markdown + YAML frontmatter。

---

### 使い方

インストール後、agent に伝える：

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

## 蒸留済みの人物

Nuwaはすでに14人の人物 + 1つのテーマを蒸留した。それぞれが独立した、すぐにインストールして使えるSkillで、すべてAgent Skills標準に基づき、Claude Code / Codex / Cursor / OpenClaw / Hermes などの runtime で汎用的に動作する：

### 人物Skill

| 人物 | 領域 | 独立リポジトリ | ワンライナーインストール（クロス runtime） |
|------|------|---------|---------|
| 🔥 **ポール・グレアム** | 起業/執筆/プロダクト/人生哲学 | [paul-graham-skill](https://github.com/alchaincyf/paul-graham-skill) | `npx skills add alchaincyf/paul-graham-skill` |
| 🔥 **張一鳴** | プロダクト/組織/グローバル化/人材 | [zhang-yiming-skill](https://github.com/alchaincyf/zhang-yiming-skill) | `npx skills add alchaincyf/zhang-yiming-skill` |
| 🔥 **カルパシー** | AI/エンジニアリング/教育/オープンソース | [karpathy-skill](https://github.com/alchaincyf/karpathy-skill) | `npx skills add alchaincyf/karpathy-skill` |
| 🔥 **イリヤ・サツケバー** | AI安全性/スケーリング/研究センス | [ilya-sutskever-skill](https://github.com/alchaincyf/ilya-sutskever-skill) | `npx skills add alchaincyf/ilya-sutskever-skill` |
| 🔥 **MrBeast** | コンテンツ制作/YouTube方法論 | [mrbeast-skill](https://github.com/alchaincyf/mrbeast-skill) | `npx skills add alchaincyf/mrbeast-skill` |
| 🔥 **トランプ** | 交渉/権力/伝播/行動予測 | [trump-skill](https://github.com/alchaincyf/trump-skill) | `npx skills add alchaincyf/trump-skill` |
| ⭐ **ジョブズ** | プロダクト/デザイン/戦略 | [steve-jobs-skill](https://github.com/alchaincyf/steve-jobs-skill) | `npx skills add alchaincyf/steve-jobs-skill` |
| **マスク** | エンジニアリング/コスト/第一原理 | [elon-musk-skill](https://github.com/alchaincyf/elon-musk-skill) | `npx skills add alchaincyf/elon-musk-skill` |
| **マンガー** | 投資/多元的思考/逆向思考 | [munger-skill](https://github.com/alchaincyf/munger-skill) | `npx skills add alchaincyf/munger-skill` |
| **ファインマン** | 学習/教育/科学的思考 | [feynman-skill](https://github.com/alchaincyf/feynman-skill) | `npx skills add alchaincyf/feynman-skill` |
| **Naval** | 富/レバレッジ/人生哲学 | [naval-skill](https://github.com/alchaincyf/naval-skill) | `npx skills add alchaincyf/naval-skill` |
| **タレブ** | リスク/反脆弱性/不確実性 | [taleb-skill](https://github.com/alchaincyf/taleb-skill) | `npx skills add alchaincyf/taleb-skill` |
| **張雪峰** | 教育選択/キャリア設計/階層移動 | [zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | `npx skills add alchaincyf/zhangxuefeng-skill` |
| **孫宇晨** | マーケティング/アテンションエコノミー/ナラティブ操作 | [リポジトリ内examples/](examples/sun-yuchen-perspective/) | `examples/sun-yuchen-perspective/` をskillsディレクトリにコピー |

### テーマSkill

| テーマ | 領域 | 独立リポジトリ | ワンライナーインストール（クロス runtime） |
|------|------|---------|---------|
| **Xメンター** | X/Twitter運用フルスタック | [x-mentor-skill](https://github.com/alchaincyf/x-mentor-skill) | `npx skills add alchaincyf/x-mentor-skill` |

人物Skillは一人の思考法を蒸留し、テーマSkillは一つの領域の方法論を蒸留する。各リポジトリには完全な調査データと効果例の対話が含まれている。

🧪 **忠実度スコアカード**：15個の公式Skillはすべて独立した2エージェントによるブラインドテストを通過し（立場の一貫性/スタイルの識別度/エッジの誠実さ/出典の透明度/構造の完全性、方法論は [references/fidelity-scorecard.md](references/fidelity-scorecard.md) 参照）、**全員Aグレード（≥85点）**。各スコア：MrBeast/Naval/タレブ/ジョブズ/カルパシー/ポール・グレアム/張雪峰 97 · マンガー/ファインマン/Xメンター 96 · トランプ 95 · イリヤ 94 · 張一鳴 93 · 孫宇晨 91 · マスク 89。完全なスコアカードは各skillディレクトリ内の `FIDELITY.md` にある。

リストにない人物やテーマを蒸留したい？Nuwaをインストールして「〇〇を蒸留して」と言うだけ。

---

## 貢献とコミュニティ

Nuwaのエコシステムはコミュニティと共に成長するが、二つの異なる道を進む：

- **`SKILL.md` はコア資産であり、外部PRによる変更は受け付けない**。方法論のバグや改善点を見つけたら→issueを立てて議論する。採用されたアイデアはメンテナーが実装し、commitで謝辞を記す（前例はPR #59）。
- **コミュニティが蒸留した人物skillは [COMMUNITY.md](COMMUNITY.md) インデックスを通す**：自分のリポジトリに置き（starはあなたのもの）、[忠実度スコアカード](references/fidelity-scorecard.md)を実行してBグレード以上を取り、一行のPRを出せば収録される。

完全なルールは [CONTRIBUTING.md](CONTRIBUTING.md) 参照。コミュニティの既存のコレクション、複数人格のオーケストレーション、テーマ応用は [COMMUNITY.md](COMMUNITY.md) を参照。

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
└── examples/
    ├── naval-perspective/       # Naval完全例 + 調査データ
    └── elon-musk-perspective/   # マスク完全例 + 調査データ
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
