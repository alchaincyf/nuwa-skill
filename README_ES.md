<div align="center">

# 女娲.skill (Nuwa)

> *"La próxima persona que quieras destilar no tiene por qué ser un colega"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green)](https://agentskills.io)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatible-blue)](https://skills.sh)
[![Multi-Runtime](https://img.shields.io/badge/Runtime-Claude%20Code%20·%20Codex%20·%20Cursor%20·%20OpenClaw%20·%20Hermes%20·%20DeepSeek%20Harness-blueviolet)](#instalación)

<br>

**Nuwa destila la forma de pensar de cualquier persona. Haz que Musk, Naval, Munger y Feynman trabajen para ti.**

<sub>Construido sobre el estándar abierto [Agent Skills](https://agentskills.io). Funciona en Claude Code, Codex, Cursor, OpenClaw, Hermes Agent, CodeBuddy, Workbuddy, Gemini CLI, OpenCode, DeepSeek Harness y 50+ runtimes compatibles con skills.</sub>

<br>

[colleague-skill](https://github.com/titanwings/colleague-skill) demostró que destilar a una persona en un skill de IA es viable.
¿Por qué quedarse con colegas? Destila a Munger, Feynman, Musk.
Solo ingresa un nombre: Nuwa maneja la investigación, extracción y validación automáticamente.

[Ejemplos](#ejemplos) · [Instalación](#instalación) · [Qué destila Nuwa](#qué-destila-nuwa) · [Cómo funciona](#cómo-funciona)

<br>

**Otros idiomas:**

[中文](README.md) · [English](README_EN.md) · [日本語](README_JA.md) · [한국어](README_KO.md)

</div>

---

## Ejemplos

```
Usuario  ❯ Quiero hacer creación de contenido, escribir un libro y
            desarrollar una app independiente, pero nunca tengo energía.

Naval    ❯ Has listado tres deseos. Cada deseo es un contrato
            que firmaste con la infelicidad.
            No es falta de energía — es exceso de contratos.

            Pregúntate: ¿cuál te hace perder la noción del tiempo?
            Ahí está tu conocimiento específico.

            No es elegir uno para siempre. Solo uno primero,
            luego otro, luego otro.
            Interés compuesto en serie, no agotamiento en paralelo.
```

```
Usuario  ❯ El costo de adquisición de clientes de nuestro SaaS es demasiado alto.

Musk     ❯ No pienses en cómo reducirlo todavía. Calcula el mínimo físico primero.
            ¿Cuál es la acción mínima necesaria para adquirir un cliente?
            ¿Cuál es el camino teóricamente más corto desde que te conocen hasta que pagan?

            ¿Cuántas veces más largo es tu camino real vs. el teórico?
            Si supera 3 veces, hay pasos que se pueden eliminar.
            No optimices el embudo — cuestiona si el embudo debería existir.
```

Esto no es juego de roles. Naval usa su modelo mental "deseo como contrato". Musk usa el razonamiento de "límite asintótico". **No están recitando citas — están analizando tu problema a través de sus marcos cognitivos.**

---

## Instalación

Nuwa está construido sobre el estándar abierto [Agent Skills](https://agentskills.io). Funciona en cualquier runtime de agente IA compatible con skills.

### Opción 1: Una línea (recomendado, multi-runtime)

Abre tu agente compatible con skills — Claude Code, Codex, Cursor, OpenClaw, Hermes, CodeBuddy, Workbuddy, Gemini CLI, OpenCode y 50+ más — y dile:

```
Instala este skill: https://github.com/alchaincyf/nuwa-skill
```

O usa el instalador CLI universal ([vercel-labs/skills](https://github.com/vercel-labs/skills), soporta 55+ runtimes):

```bash
npx skills add alchaincyf/nuwa-skill
```

Auto-detecta tu runtime y coloca el skill en el directorio correcto. Agrega `-a claude-code` / `-a codex` / `-a cursor` / `-a openclaw` para apuntar a uno específico.

### Opción 2: Instalación manual

<details>
<summary>Directorios skills por runtime</summary>

| Runtime | Ruta |
|---|---|
| Claude Code | `~/.claude/skills/nuwa-skill/` |
| Codex CLI | `~/.codex/skills/nuwa-skill/` |
| Cursor | `~/.cursor/skills/nuwa-skill/` |
| OpenClaw | `~/.openclaw/workspace/skills/nuwa-skill/` |
| DeepSeek Harness | `~/.dsh/skills/nuwa-skill/` |
| Hermes Agent | ejecuta `tools/install_hermes_skill.py` |
| Cualquier otro | clonar en el directorio `skills/` de ese runtime |

```bash
git clone https://github.com/alchaincyf/nuwa-skill <ruta-de-arriba>
```

</details>

### Plugin para DeepSeek Harness

Nuwa también es un plugin de [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DSH). Añádelo a un perfil (aquí `web`) con un solo comando y reinicia DSH:

```bash
dsh plugin --profile web add github:alchaincyf/nuwa-skill
```

Para quitarlo: `dsh plugin --profile web remove huashu-nuwa`. Los skills de personas destilados dentro de DSH se guardan en `.dsh/skills/` del proyecto, y DSH los carga automáticamente.

### Opción 3: Usar como referencia (sin runtime)

Incluso sin un runtime con skills automáticos, puedes pegar cualquier `SKILL.md` en tu contexto — Nuwa es markdown plano + YAML frontmatter.

---

### Uso

Una vez instalado, dile a tu agente:

```
> Destila a Paul Graham
> Crea un skill de perspectiva de Zhang Xiaolong
> Hazme un skill de Duan Yongping
```

Después de la creación, invoca directamente:

```
> Usa la perspectiva de Munger para analizar esta decisión de inversión
> ¿Cómo explicaría Feynman la computación cuántica?
> Cambia a Naval, estoy indeciso entre tres cosas
```

---

## Qué destila Nuwa

Destilar las mejores mentes en cualquier campo requiere extraer algo más profundo que los hábitos de trabajo diarios. Nuwa extrae seis capas:

| Capa | Descripción |
|---|---|
| **Cómo hablan** | ADN de expresión — tono, ritmo, preferencias de vocabulario |
| **Cómo piensan** | Modelos mentales, marcos cognitivos |
| **Cómo juzgan** | Heurísticas de decisión |
| **Qué no hacen** | Antipatrones, piso de valores |
| **Límites honestos** | Lo que el skill genuinamente no puede hacer |

Los hábitos de trabajo se pueden transmitir con documentos de proceso. Pero lo que hace que Munger y Musk lleguen a conclusiones diferentes sobre el mismo problema son sus marcos cognitivos. Nuwa extrae el sistema operativo cognitivo.

### Límites honestos

Cada skill indica explícitamente lo que no puede hacer:

- No puede destilar intuición — los marcos se pueden extraer, la inspiración no
- No puede capturar cambios — solo una instantánea hasta la fecha de investigación
- Declaraciones públicas ≠ pensamientos reales — solo basado en información pública

**Un skill que no te dice sus límites no merece confianza.**

---

## Personajes destilados

Nuwa ya ha destilado 14 personas + 1 tema. Cada uno es un skill independiente y listo para instalar, construido sobre el estándar Agent Skills, y funciona en Claude Code / Codex / Cursor / OpenClaw / Hermes y otros runtimes:

### Skills de personas

| Persona | Dominio | Repo independiente | Instalación en una línea (multi-runtime) |
|------|------|---------|---------|
| 🔥 **Paul Graham** | Startups / escritura / producto / filosofía de vida | [paul-graham-skill](https://github.com/alchaincyf/paul-graham-skill) | `npx skills add alchaincyf/paul-graham-skill` |
| 🔥 **Zhang Yiming** | Producto / organización / globalización / talento | [zhang-yiming-skill](https://github.com/alchaincyf/zhang-yiming-skill) | `npx skills add alchaincyf/zhang-yiming-skill` |
| 🔥 **Karpathy** | IA / ingeniería / educación / código abierto | [karpathy-skill](https://github.com/alchaincyf/karpathy-skill) | `npx skills add alchaincyf/karpathy-skill` |
| 🔥 **Ilya Sutskever** | Seguridad de IA / scaling / gusto en investigación | [ilya-sutskever-skill](https://github.com/alchaincyf/ilya-sutskever-skill) | `npx skills add alchaincyf/ilya-sutskever-skill` |
| 🔥 **MrBeast** | Creación de contenido / metodología de YouTube | [mrbeast-skill](https://github.com/alchaincyf/mrbeast-skill) | `npx skills add alchaincyf/mrbeast-skill` |
| 🔥 **Trump** | Negociación / poder / comunicación / predicción de comportamiento | [trump-skill](https://github.com/alchaincyf/trump-skill) | `npx skills add alchaincyf/trump-skill` |
| ⭐ **Steve Jobs** | Producto / diseño / estrategia | [steve-jobs-skill](https://github.com/alchaincyf/steve-jobs-skill) | `npx skills add alchaincyf/steve-jobs-skill` |
| **Elon Musk** | Ingeniería / costos / primeros principios | [elon-musk-skill](https://github.com/alchaincyf/elon-musk-skill) | `npx skills add alchaincyf/elon-musk-skill` |
| **Munger** | Inversión / pensamiento multidisciplinar / pensamiento inverso | [munger-skill](https://github.com/alchaincyf/munger-skill) | `npx skills add alchaincyf/munger-skill` |
| **Feynman** | Aprendizaje / enseñanza / pensamiento científico | [feynman-skill](https://github.com/alchaincyf/feynman-skill) | `npx skills add alchaincyf/feynman-skill` |
| **Naval** | Riqueza / apalancamiento / filosofía de vida | [naval-skill](https://github.com/alchaincyf/naval-skill) | `npx skills add alchaincyf/naval-skill` |
| **Taleb** | Riesgo / antifragilidad / incertidumbre | [taleb-skill](https://github.com/alchaincyf/taleb-skill) | `npx skills add alchaincyf/taleb-skill` |
| **Zhang Xuefeng** | Elecciones educativas / planificación de carrera / movilidad social | [zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) | `npx skills add alchaincyf/zhangxuefeng-skill` |
| **Sun Yuchen** | Marketing / economía de la atención / control narrativo | [examples/ en este repo](examples/sun-yuchen-perspective/) | copia `examples/sun-yuchen-perspective/` en tu directorio de skills |

### Skill temático

| Tema | Dominio | Repo independiente | Instalación en una línea (multi-runtime) |
|------|------|---------|---------|
| **X Mentor** | Crecimiento full-stack en X/Twitter | [x-mentor-skill](https://github.com/alchaincyf/x-mentor-skill) | `npx skills add alchaincyf/x-mentor-skill` |

Los skills de personas destilan cómo piensa una mente; el skill temático destila la metodología de un campo. Cada repo incluye datos completos de investigación y conversaciones de ejemplo.

🧪 **Tarjeta de fidelidad**: los 15 skills oficiales pasaron pruebas ciegas independientes con doble agente (consistencia de postura / reconocibilidad de estilo / honestidad en los límites / transparencia de fuentes / completitud estructural; metodología en [references/fidelity-scorecard.md](references/fidelity-scorecard.md)), **todos grado A (≥85)**. Puntuaciones: MrBeast/Naval/Taleb/Jobs/Karpathy/Paul Graham/Zhang Xuefeng 97 · Munger/Feynman/X Mentor 96 · Trump 95 · Ilya 94 · Zhang Yiming 93 · Sun Yuchen 91 · Musk 89. Tarjeta completa en el `FIDELITY.md` de cada skill.

¿Quieres a alguien que no está en la lista? Instala Nuwa y solo di «destila a XXX».

---

## Contribuir y comunidad

El ecosistema de Nuwa crece con la comunidad, por dos caminos distintos:

- **`SKILL.md` es el activo central y no acepta PRs externos**. ¿Encontraste un bug o mejora en la metodología? → abre un issue para discutir; las ideas adoptadas las implementa el mantenedor y se agradecen en el commit (precedente en el PR #59).
- **Los skills de personas destilados por la comunidad pasan por el índice [COMMUNITY.md](COMMUNITY.md)**: mantenlos en tu propio repo (las estrellas son tuyas), pasa la [tarjeta de fidelidad](references/fidelity-scorecard.md) para alcanzar grado B o superior, y envía un PR de una línea para ser incluido.

Reglas completas en [CONTRIBUTING.md](CONTRIBUTING.md). Para colecciones comunitarias existentes, orquestación multi-persona y aplicaciones temáticas, consulta [COMMUNITY.md](COMMUNITY.md).

---

## Cómo funciona

Ingresa un nombre y Nuwa hace cinco cosas:

**1. Escribir primero una instantánea previa** — antes de investigar, se anota lo que el modelo ya sabe de la persona sin consultar nada. La investigación busca solo tres cosas: lo que contradice esa instantánea, lo que va más hondo y lo que le falta. Lo que el modelo ya sabría responder no ocupa espacio en el skill.

**2. Recopilar y sellar** — escritos, podcasts/entrevistas, redes sociales, perspectivas de críticos, registros de decisiones, línea de vida, cada uno archivado. Un conjunto de decisiones reales y respuestas completas de la persona se sella fuera del paso de extracción y se guarda como examen final.

**3. Extraer** — 5–8 jugadas (qué hace en concreto ante un tipo de problema), 3–7 modelos mentales, heurísticas de decisión, fichas de casos con fuente, al menos 2 malentendidos comunes, voz, tensiones y límites. Los modelos mentales siguen pasando la triple verificación: aparece en 2+ dominios, predice posiciones sobre preguntas nuevas, no es algo que pensaría cualquier persona inteligente.

**4. Dar forma** — tres capas: un SKILL.md de 350 líneas como máximo, un libro de casos en `references/casebook.md` y un banco de citas en `references/voice.md`. Cada skill lleva siete reglas de ejecución, como «que no esté en el material no significa que nunca lo dijera» y «separar las citas reales de la extrapolación».

**5. Validar** — pruebas a ciegas con agentes independientes: las mismas preguntas de tarea respondidas con y sin el skill, evaluadas por un juez que no sabe cuál es cuál, más las preguntas selladas y las de límite. Los resultados se escriben en FIDELITY.md, también cuando pierde.

Dos formas de ejecutarlo: los modelos más capaces trabajan con libertad contra los criterios de cada paso; los modelos ligeros siguen paso a paso los manuales de `references/`. Los skills creados con v1.x se pueden actualizar («actualiza el skill de X»); si los archivos de investigación siguen ahí, no hace falta investigar de nuevo. En `examples/`, los skills de Munger y Steve Jobs ya están actualizados a v2; el resto sigue en formato v1.

Los detalles del método están en `references/`: `research-playbook.md` (recopilación), `extraction-framework.md` (extracción), `validation-playbook.md` (validación).

---

## Estructura del repositorio

```
nuwa-skill/
├── SKILL.md                    # Nuwa misma
├── references/
│   ├── extraction-framework.md # Metodología de extracción (léelo para profundizar)
│   ├── research-playbook.md / validation-playbook.md / diagnose-playbook.md
│   ├── special-cases.md / fidelity-scorecard.md
│   └── skill-template.md       # Plantilla para generar skills
└── examples/
    ├── naval-perspective/       # Ejemplo completo de Naval + datos de investigación
    └── elon-musk-perspective/   # Ejemplo completo de Musk + datos de investigación
```

Toda la investigación es completamente transparente. Los ejemplos incluyen archivos de investigación completos: puedes ver cómo se recopiló, filtró y convirtió la información en modelos mentales.

---

## Star History

<div align="center">

[![Star History Chart](https://api.star-history.com/svg?repos=alchaincyf/nuwa-skill&type=Date)](https://star-history.com/#alchaincyf/nuwa-skill&Date)

</div>

---

## La historia detrás

[colleague-skill](https://github.com/titanwings/colleague-skill) explotó recientemente en GitHub — destilar colegas que se van en skills de IA, superando las 5,000 estrellas en días. Demostró una cosa: destilar a una persona es completamente viable.

Dado que tenemos la capacidad de destilar personas, ¿por qué quedarse con colegas cercanos? Ve a destilar las mejores mentes en cada campo. Y afortunadamente, estas personas generalmente dejaron atrás vastas cantidades de material destilable — libros, charlas, entrevistas, redes sociales. Esto es una mejora enorme de tu propio pensamiento.

He estado haciendo algo así por un tiempo — no destilando colegas, sino a Munger, Feynman, Naval, Musk, Taleb. Hoy estoy publicando la metodología como código abierto.

Nuwa no copia personas. Extrae sistemas operativos cognitivos.

**Nuwa (女娲)**, la diosa en la mitología china que creó humanos de arcilla. Aquí la arcilla es información pública, y lo que se crea no es una persona — es un espejo.

---

## Sobre el autor

Huashu / Huasheng, AI Native Coder, desarrollador independiente. Todos los productos están construidos con código escrito por IA ([Kitten Fill Light](https://apps.apple.com/app/id6738028637) llegó al #1 en el chart de pago de App Store China). Ejecutando 40+ skills personalizados en Claude Code. Nuwa es el skill que crea skills.

- Cuenta oficial WeChat: 花叔 (Huashu)
- X: [@AlchainHust](https://x.com/AlchainHust)
- Bilibili: [花叔](https://space.bilibili.com/14097567)
- YouTube: [@Alchain](https://www.youtube.com/@Alchain)

## Licencia

MIT — úsalo, modifícalo, construye con él.

---

<div align="center">

**colleague-skill** destila lo que una persona hace.<br>
**Nuwa** destila cómo una persona piensa.<br><br>
*La próxima persona que quieras destilar no tiene por qué ser un colega.*

<br>

MIT License © [Huashu](https://github.com/alchaincyf)

</div>
