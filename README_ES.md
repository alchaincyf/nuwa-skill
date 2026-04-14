<div align="center">

# 女娲.skill (Nuwa)

> *"La próxima persona que quieras destilar no tiene por qué ser un colega"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**Nuwa destila la forma de pensar de cualquier persona. Haz que Musk, Naval, Munger y Feynman trabajen para ti.**

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

```bash
npx skills add alchaincyf/nuwa-skill
```

En Claude Code:

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

## Cómo funciona

Ingresa un nombre y Nuwa hace cuatro cosas:

**1. Seis corrientes de investigación paralela** — escritos, podcasts/entrevistas, redes sociales, perspectivas de críticos, registros de decisiones, línea de vida. 6 agentes ejecutándose simultáneamente, cada uno archivando.

**2. Extracción de triple verificación** — una afirmación debe pasar tres pruebas para ser registrada como modelo mental: aparece en 2+ dominios (no es una declaración de una sola vez), puede predecir posiciones sobre nuevas preguntas (tiene poder predictivo), no es algo que cualquier persona inteligente pensaría (tiene exclusividad). Las tres son necesarias.

**3. Construir el skill** — 3-7 modelos mentales + 5-10 heurísticas de decisión + ADN de expresión + valores y antipatrones + límites honestos, escritos en SKILL.md.

**4. Validación de calidad** — prueba con 3 preguntas que la persona respondió públicamente; la dirección debe coincidir. Luego prueba con 1 pregunta que nunca discutió; el skill debería mostrar incertidumbre apropiada en lugar de falsa confianza.

Metodología completa en `references/extraction-framework.md`.

---

## Estructura del repositorio

```
nuwa-skill/
├── SKILL.md                    # Nuwa misma
├── references/
│   ├── extraction-framework.md # Metodología de extracción (léelo para profundizar)
│   └── skill-template.md       # Plantilla para generar skills
└── examples/                          # 15 personas + 1 tema, con datos de investigación completos
    ├── steve-jobs-perspective/        # Jobs (con conversación demo)
    ├── paul-graham-perspective/       # Paul Graham
    ├── zhang-yiming-perspective/      # Zhang Yiming
    ├── andrej-karpathy-perspective/   # Karpathy
    ├── ilya-sutskever-perspective/    # Ilya Sutskever
    ├── trump-perspective/             # Trump
    ├── mrbeast-perspective/           # MrBeast
    ├── elon-musk-perspective/         # Elon Musk
    ├── munger-perspective/            # Charlie Munger
    ├── buffett-perspective/           # Warren Buffett
    ├── feynman-perspective/           # Feynman
    ├── naval-perspective/             # Naval Ravikant
    ├── taleb-perspective/             # Taleb
    ├── liurun-perspective/            # Liu Run (刘润)
    ├── zhangxuefeng-perspective/      # Zhang Xuefeng
    └── x-mastery-mentor/             # X Mastery Mentor (skill temático)
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
