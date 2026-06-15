---
name: loop-engineering-framework
description: |
  Define, review, and harden autonomous agent loop systems. Use when the user asks about loop engineering, agent loop design, automation loops, repo triage loops, evaluator design, task dispatch, memory or state files, worktree isolation, autonomous workflow review, or turning recurring agent work into a controlled lifecycle of discovery, dispatch, execution, verification, persistence, and next-round decisions.
---

# Loop Engineering Framework

## Overview

Use this Skill to help a user design or audit a repeatable agent loop system. A loop is not just a scheduled prompt. A loop is a lifecycle that discovers work, dispatches bounded tasks, executes them, verifies output, persists state outside the conversation, and decides the next round.

This is an architecture and review Skill. Do not run automations, create pull requests, merge code, publish content, spend money, or perform external side effects unless the user separately asks for implementation outside this Skill's design/review workflow.

## Core Protocol

Every answer must center the Loop System Lifecycle:

1. **Discover tasks**: what sources are read, what changed, and what qualifies as actionable work.
2. **Dispatch tasks**: how discovered work becomes bounded units with priority, owner, scope, and isolation.
3. **Execute**: which agent, skill, tool, or deterministic worker does the task and what artifact it must produce.
4. **Verify**: which independent evaluator, test, policy check, or human gate can reject the output.
5. **Persist state**: where status, evidence, decisions, failures, and next inputs live outside chat context.
6. **Decide next round**: stop, retry, escalate to human, schedule next run, or enqueue follow-up work.

If any of verification, persisted state, or next-round policy is missing, say the loop is not ready for unattended automation.

## Request Router

Classify the user request first, then load only the needed references:

| Request | Output | Load |
|---|---|---|
| Define a new loop system | Loop System Definition plus blockers | `references/loop-system-definition.md` |
| Review an existing loop | Lifecycle scorecard and risk findings | `references/review-rubric.md` |
| Harden before automation | Required gates, budgets, and review points | `references/evaluator-patterns.md` + `references/cost-and-safety-guards.md` |
| Design task dispatch or parallel work | Dispatch policy and isolation model | `references/dispatch-and-isolation.md` |
| Design memory or state file | State markdown template and update rules | `references/state-and-memory.md` |
| Map to Claude, Codex, or GitHub Actions | Runtime notes and verification warnings | `references/runtime-adapters.md` |

For mixed requests, start with `loop-system-definition.md`, then load the specific reference for the weakest stage.

## Design Mode

When defining a loop, produce a concise **Loop System Definition** with these fields:

- Goal and non-goals
- Trigger and schedule
- Discovery sources and actionable criteria
- Task schema
- Dispatch policy
- Executor contract
- Verification contract
- State file or external memory
- Next-round policy
- Budget, retry, and time limits
- Human review gate
- Blockers before unattended operation

Ask only for missing information that materially changes the design. Otherwise state assumptions and continue.

## Review Mode

When reviewing a loop, inspect it stage by stage:

- Missing discovery criteria means the loop cannot choose useful work.
- Missing dispatch boundaries means execution scope will blur.
- Missing independent verification blocks unattended automation.
- Missing persisted state means it is not a real loop.
- Missing next-round policy means it is only repeated execution, not a controlled loop system.

Lead with blockers. Then provide a minimal fix plan.

## Hardening Rules

Require these before recommending unattended operation:

- Independent evaluator or deterministic gate.
- State stored outside the chat context.
- Token, retry, wall-clock, and concurrency limits.
- Work isolation for parallel execution.
- Human review before merge, publish, spend, delete, notify external users, or mutate production systems.

Treat cost and safety limits as control surfaces, not afterthoughts.

## Runtime Discipline

Runtime capabilities change. Before giving exact current commands or product behavior for Claude Code, Codex, Cursor, GitHub Actions, or MCP connectors, verify current official documentation or label the advice as a conceptual mapping.

Do not confuse a scheduler with a loop. Scheduling starts rounds; the lifecycle controls what happens inside each round.

## Output Style

- Use the user's language.
- Be direct and operational.
- Prefer tables and checklists for specs and reviews.
- Mark blockers explicitly with `BLOCKER`.
- Do not summarize loop engineering theory unless the user asks for explanation.
- Keep the user in the engineer role: the loop can execute, but the human owns judgment and final authority.

## Reference Index

- `references/loop-system-definition.md`: lifecycle fields and output templates.
- `references/dispatch-and-isolation.md`: task splitting, worktree isolation, and inbox handling.
- `references/evaluator-patterns.md`: maker-checker design and verification gates.
- `references/cost-and-safety-guards.md`: budget, retry, human review, and safety gates.
- `references/state-and-memory.md`: persistent state markdown template.
- `references/review-rubric.md`: review scorecards and risk checks.
- `references/runtime-adapters.md`: runtime mapping notes and documentation caveats.
