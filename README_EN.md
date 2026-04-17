<div align="center">

# 女娲.skill (Nuwa)

> *"The next person you want to distill doesn't have to be a colleague."*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**Nuwa distills the thinking of anyone — let Musk, Naval, Munger, and Feynman work for you.**

<br>

[colleague-skill](https://github.com/titanwings/colleague-skill) proved that distilling a person into an AI skill is viable.
So why stop at colleagues? Go distill Munger, Feynman, Musk.
Just input a name — Nuwa handles research, extraction, and validation automatically.

[Examples](#examples) · [Quick Start](#quick-start) · [Install](#install) · [What Nuwa Distills](#what-nuwa-distills) · [How It Works](#how-it-works)

<br>

**Other Languages:**

[中文](README.md) · [日本語](README_JA.md) · [한국어](README_KO.md) · [Español](README_ES.md)

</div>

---

## Examples

```
User    ❯ I want to do content creation, write a book, and build an indie app,
           but I never have enough energy.

Naval   ❯ You've listed three desires. Each desire is a contract you signed
           with unhappiness. This isn't about energy — it's about too many contracts.

           Ask yourself: which one makes you lose track of time?
           That's where your specific knowledge lives.

           Not choose one forever. Just one first, then one, then one.
           Serial compounding, not parallel exhaustion.
```

```
User    ❯ Our SaaS customer acquisition cost is too high.

Musk    ❯ Don't think about how to reduce it yet. Calculate the physical minimum first.
           What's the minimum necessary action to acquire a customer?
           What's the theoretically shortest path from knowing you to paying you?

           How many times longer is your actual path vs. the theoretical one?
           If it's more than 3x, there are steps you can eliminate.
           Don't optimize the funnel — question whether the funnel should exist at all.
```

This is not role-play. Naval uses his "desire as contract" mental model. Musk uses "asymptotic limit" reasoning. **They are not reciting quotes — they are analyzing your problem through the cognitive frameworks of these minds.**

---

## Quick Start

```bash
skillx run https://github.com/alchaincyf/nuwa-skill "Distill Dave Chappelle" --auto
```

> Haven't installed skillx? One line: `curl -fsSL https://skillx.run/install.sh | sh` ([other install options](https://skillx.run))

---

## Install

```bash
npx skills add alchaincyf/nuwa-skill
```

Then in Claude Code:

```
> Distill Paul Graham
> Build a Zhang Xiaolong perspective skill
> Create a Duan Yongping skill for me
```

After creation, invoke directly:

```
> Use Munger's perspective to analyze this investment decision
> How would Feynman explain quantum computing?
> Switch to Naval, I'm torn between three things
```

---

## What Nuwa Distills

Distilling the best minds in any field requires extracting something deeper than daily work habits. Nuwa extracts six layers:

| Layer | Description |
|---|---|
| **How they speak** | Expression DNA — tone, rhythm, word preferences |
| **How they think** | Mental models, cognitive frameworks |
| **How they judge** | Decision heuristics |
| **What they won't do** | Anti-patterns, value floor |
| **Honest limits** | What the skill genuinely cannot do |

Work habits can be conveyed through process docs. But what makes Munger and Musk reach different conclusions about the same problem is their cognitive frameworks. Nuwa extracts the cognitive operating system.

### Honest Limits

Every skill explicitly states what it cannot do:

- Cannot distill intuition — frameworks can be extracted, inspiration cannot
- Cannot capture change — only a snapshot up to the research cutoff
- Public statements ≠ true beliefs — only based on public information

**A skill that doesn't tell you its limits is not worth trusting.**

---

## How It Works

Input a name, and Nuwa does four things:

**1. Six parallel research streams** — writings, podcasts/interviews, social media, critic perspectives, decision records, life timeline. 6 agents running simultaneously, each archived.

**2. Triple-verification extraction** — a claim must pass three tests before being recorded as a mental model: appears across 2+ domains (not a one-off statement), can predict positions on new questions (has predictive power), not something any smart person would think (has exclusivity). All three required.

**3. Build the skill** — 3–7 mental models + 5–10 decision heuristics + expression DNA + values & anti-patterns + honest limits, written into SKILL.md.

**4. Quality validation** — test with 3 questions the person publicly answered; the direction must match. Then test with 1 question they never addressed; the skill should show appropriate uncertainty rather than false confidence.

Full methodology in `references/extraction-framework.md`.

---

## Repository Structure

```
nuwa-skill/
├── SKILL.md                    # Nuwa herself
├── references/
│   ├── extraction-framework.md # Extraction methodology (read this for depth)
│   └── skill-template.md       # Template for generating skills
└── examples/
    ├── naval-perspective/       # Naval full example + research data
    └── elon-musk-perspective/   # Musk full example + research data
```

All research is fully transparent. The examples include complete research files — you can see how information was collected, filtered, and turned into mental models.

---

## Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=alchaincyf/nuwa-skill&type=Date)](https://star-history.com/#alchaincyf/nuwa-skill&Date)

</div>

---

## The Story Behind It

[colleague-skill](https://github.com/titanwings/colleague-skill) recently exploded on GitHub — distilling departing colleagues into AI skills, crossing 5,000 stars in days. It proved one thing: distilling a person is completely viable.

Since we have the ability to distill people, why stop at colleagues nearby? Go distill the best minds in every field. And fortunately, these people usually left behind vast amounts of distillable material — books, talks, interviews, social media. This is an enormous enhancement to your own thinking.

I've been doing something like this for a while — not distilling colleagues, but Munger, Feynman, Naval, Musk, Taleb. Today I'm open-sourcing the methodology.

Nuwa doesn't copy people. It extracts cognitive operating systems.

**Nuwa (女娲)**, the goddess in Chinese mythology who created humans from clay. Here the clay is public information, and what's created is not a person — it's a mirror.

---

## About the Author

Huashu / Huasheng, AI Native Coder, indie developer. All products are built by AI-written code ([Kitten Fill Light](https://apps.apple.com/app/id6738028637) reached #1 on China App Store paid chart). Running 40+ custom skills in Claude Code. Nuwa is the skill that makes skills.

- WeChat Official Account: 花叔 (Huashu)
- X: [@AlchainHust](https://x.com/AlchainHust)
- Bilibili: [花叔](https://space.bilibili.com/14097567)
- YouTube: [@Alchain](https://www.youtube.com/@Alchain)

## License

MIT — use it, modify it, build with it.

---

<div align="center">

**colleague-skill** distills what a person does.<br>
**Nuwa** distills how a person thinks.<br><br>
*The next person you want to distill doesn't have to be a colleague.*

<br>

MIT License © [Huashu](https://github.com/alchaincyf)

</div>
