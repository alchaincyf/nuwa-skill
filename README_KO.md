<div align="center">

# 여와.skill (Nuwa)

> *"증류할 다음 사람이 꼭 동료일 필요는 없다"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**Nuwa는 누구의 사고방식도 증류한다. 머스크, 나발, 멍거, 파인만을 당신을 위해 일하게 하라.**

<br>

[colleague-skill](https://github.com/titanwings/colleague-skill)은 사람을 AI 스킬로 증류하는 것이 가능하다는 것을 증명했다.
왜 동료에서 멈추는가? 멍거, 파인만, 머스크를 증류하라.
이름 하나만 입력하면 Nuwa가 조사, 추출, 검증 전 과정을 자동으로 처리한다.

[예시](#예시) · [설치](#설치) · [Nuwa가 증류하는 것](#nuwa가-증류하는-것) · [작동 원리](#작동-원리)

<br>

**다른 언어:**

[中文](README.md) · [English](README_EN.md) · [日本語](README_JA.md) · [Español](README_ES.md)

</div>

---

## 예시

```
사용자  ❯ 콘텐츠 창작, 책 쓰기, 독립 개발을 동시에 하고 싶은데
           에너지가 전혀 부족하다.

Naval   ❯ 당신은 세 가지 욕망을 나열했다.
           각 욕망은 불행과 맺은 계약이다.
           에너지가 부족한 게 아니라, 계약이 너무 많은 것이다.

           스스로에게 물어라: 어느 것을 할 때 시간을 잊는가?
           그것이 당신의 특화된 지식이 있는 곳이다.

           셋 중 하나를 영원히 선택하는 게 아니다.
           먼저 하나, 그 다음 하나, 또 그 다음 하나.
           직렬 복리, 병렬 소모가 아닌.
```

```
사용자  ❯ 우리 SaaS의 고객 획득 비용이 너무 높다.

머스크  ❯ 줄이는 방법부터 생각하지 마라. 물리적 최솟값을 먼저 계산하라.
           고객 획득에 필요한 최소 행동이 무엇인가?
           사용자가 당신을 알고 결제하기까지 이론적 최단 경로는 무엇인가?

           실제 경로는 이론 경로의 몇 배인가?
           3배를 넘는다면 반드시 제거할 수 있는 단계가 있다.
           퍼널을 최적화하지 마라, 퍼널 자체가 존재해야 하는지를 의심하라.
```

이것은 역할극이 아니다. 나발은 "욕망=계약" 정신 모델을 사용하고, 머스크는 "점근 한계법"을 사용한다. **명언을 반복하는 것이 아니라, 이 인물들의 인지 프레임워크를 통해 당신의 문제를 분석하는 것이다.**

---

## 설치

```bash
npx skills add alchaincyf/nuwa-skill
```

Claude Code에서:

```
> 폴 그레이엄을 증류해 줘
> 장샤오룽 관점 스킬을 만들어 줘
> 단융핑 스킬을 만들어 줘
```

생성 후 직접 호출:

```
> 멍거의 관점으로 이 투자 결정을 분석해 줘
> 파인만이라면 양자 컴퓨팅을 어떻게 설명할까?
> 나발로 전환해 줘, 세 가지 일로 고민 중이야
```

---

## Nuwa가 증류하는 것

각 분야 최고의 인물을 증류하려면 일상적인 작업 습관보다 더 깊은 것을 추출해야 한다. Nuwa는 여섯 층을 추출한다:

| 층 | 설명 |
|---|---|
| **말하는 방식** | 표현 DNA — 어조, 리듬, 어휘 선호도 |
| **생각하는 방식** | 정신 모델, 인지 프레임워크 |
| **판단하는 방식** | 의사결정 휴리스틱 |
| **하지 않는 것** | 안티패턴, 가치관 마지노선 |
| **솔직한 한계** | 스킬이 진정으로 할 수 없는 것 |

작업 습관은 프로세스 문서로 전달할 수 있다. 하지만 멍거와 머스크가 같은 문제에 다른 결론을 내리는 이유는 인지 프레임워크에 있다. Nuwa가 추출하는 것은 인지 운영체제다.

### 솔직한 한계

모든 스킬은 할 수 없는 것을 명시한다:

- 직관은 증류할 수 없다 — 프레임워크는 추출 가능하지만 영감은 불가
- 변화는 포착할 수 없다 — 조사 시점의 스냅샷일 뿐
- 공개 발언 ≠ 진짜 생각 — 공개 정보에만 기반

**자신의 한계를 알려주지 않는 스킬은 신뢰할 가치가 없다.**

---

## 작동 원리

이름을 입력하면 Nuwa는 네 가지를 한다:

**1. 여섯 갈래 병렬 조사** — 저작, 팟캐스트/인터뷰, SNS, 비평가 관점, 의사결정 기록, 인생 타임라인. 6개 에이전트가 동시에 실행되며 각자 아카이브.

**2. 삼중 검증 추출** — 어떤 주장을 정신 모델로 기록하려면 세 가지 테스트를 통과해야 한다: 2개 이상의 분야에서 등장(일회성 발언이 아님), 새로운 문제에 대한 입장을 예측할 수 있음(예측력 있음), 모든 똑똑한 사람이 이렇게 생각하지는 않음(배타성 있음). 세 가지 모두 통과해야 함.

**3. 스킬 구축** — 3~7개 정신 모델 + 5~10개 의사결정 휴리스틱 + 표현 DNA + 가치관 & 안티패턴 + 솔직한 한계를 SKILL.md에 작성.

**4. 품질 검증** — 해당 인물이 공개적으로 답한 3가지 질문으로 테스트, 방향이 일치해야 통과. 그런 다음 그가 논의한 적 없는 1가지 질문으로 테스트, 스킬은 단호하게 답하지 않고 적절한 불확실성을 보여야 함.

전체 방법론은 `references/extraction-framework.md`에 있다.

---

## 저장소 구조

```
nuwa-skill/
├── SKILL.md                    # Nuwa 본체
├── references/
│   ├── extraction-framework.md # 추출 방법론 (깊이 이해하고 싶다면 이것)
│   └── skill-template.md       # 스킬 생성 템플릿
└── examples/                          # 15명 인물 + 1개 주제, 완전한 조사 데이터 포함
    ├── steve-jobs-perspective/        # 잡스 (데모 대화 포함)
    ├── paul-graham-perspective/       # Paul Graham
    ├── zhang-yiming-perspective/      # 장이밍
    ├── andrej-karpathy-perspective/   # Karpathy
    ├── ilya-sutskever-perspective/    # Ilya Sutskever
    ├── trump-perspective/             # 트럼프
    ├── mrbeast-perspective/           # MrBeast
    ├── elon-musk-perspective/         # 머스크
    ├── munger-perspective/            # 먼거
    ├── buffett-perspective/           # 버핏
    ├── feynman-perspective/           # 파인만
    ├── naval-perspective/             # Naval Ravikant
    ├── taleb-perspective/             # 탈레브
    ├── liurun-perspective/            # 류룬 (刘润)
    ├── zhangxuefeng-perspective/      # 장쉐펑
    └── x-mastery-mentor/             # X 마스터 멘토 (주제 스킬)
```

조사 과정은 완전히 투명하다. examples에는 완전한 조사 파일이 포함되어 있어 정보가 어떻게 수집, 필터링되어 정신 모델이 되었는지 확인할 수 있다.

---

## Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=alchaincyf/nuwa-skill&type=Date)](https://star-history.com/#alchaincyf/nuwa-skill&Date)

</div>

---

## 배경

[colleague-skill](https://github.com/titanwings/colleague-skill)은 최근 GitHub에서 폭발적으로 퍼졌다 — 퇴사한 동료를 AI 스킬로 증류해 며칠 만에 5000 스타를 돌파했다. 이것은 한 가지를 증명했다: 사람을 증류하는 것은 완전히 가능하다.

사람을 증류할 능력이 생겼다면, 왜 주변 동료에서 멈추는가? 각 분야 최고의 인물을 증류하라. 다행히 그런 사람들은 대개 방대한 증류 가능한 자료를 남겼다 — 저작, 강연, 인터뷰, SNS. 이것은 자신의 능력을 크게 보강하는 것이다.

예전부터 비슷한 일을 해왔다 — 동료가 아닌 멍거, 파인만, Naval, 머스크, 탈레브를 증류했다. 오늘 그 방법론을 오픈소스로 공개한다.

Nuwa는 사람을 복제하지 않는다. 인지 운영체제를 추출한다.

**여와(女娲)**는 중국 신화에서 흙으로 인간을 창조한 여신이다. 여기서 흙은 공개 정보이고, 창조되는 것은 사람이 아니라 거울이다.

---

## 작가 소개

화叔(Huashu)/화생(Huasheng), AI Native Coder, 독립 개발자. 모든 제품은 AI가 작성한 코드로 구축([새끼고양이 보조등](https://apps.apple.com/app/id6738028637)이 중국 App Store 유료 차트 1위 달성). Claude Code에서 40개 이상의 커스텀 스킬 실행 중. Nuwa는 스킬을 만드는 스킬이다.

- WeChat 공식 계정: 花叔 (Huashu)
- X: [@AlchainHust](https://x.com/AlchainHust)
- Bilibili: [花叔](https://space.bilibili.com/14097567)
- YouTube: [@Alchain](https://www.youtube.com/@Alchain)

## 라이선스

MIT — 자유롭게 사용하고, 수정하고, 만들어라.

---

<div align="center">

**colleague-skill**은 사람이 무엇을 하는지를 증류했다.<br>
**Nuwa**는 사람이 어떻게 생각하는지를 증류한다.<br><br>
*증류할 다음 사람이 꼭 동료일 필요는 없다.*

<br>

MIT License © [Huashu](https://github.com/alchaincyf)

</div>
