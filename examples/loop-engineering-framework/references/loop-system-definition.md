# Loop System Definition

Use this reference when the user wants to design a new loop or turn recurring agent work into a controlled system.

## Lifecycle Backbone

A real loop has six stages:

1. **Discover tasks**: read sources and decide what work exists.
2. **Dispatch tasks**: turn discoveries into bounded task units.
3. **Execute**: run the worker that produces an artifact or decision.
4. **Verify**: run an independent check that can reject the result.
5. **Persist state**: write durable memory outside the chat context.
6. **Decide next round**: stop, retry, escalate, schedule, or enqueue.

Scheduling alone is not a loop. A repeated prompt without persisted state and next-round logic is only a repeated run.

## Required Fields

| Field | Required answer |
|---|---|
| Goal | What outcome the loop exists to improve |
| Non-goals | What it must not do automatically |
| Trigger | Manual, schedule, webhook, issue event, CI event, or inbox event |
| Discovery sources | CI, issues, commits, logs, Slack, tickets, docs, dashboards, files |
| Actionable criteria | Exact rules for what becomes a task |
| Task schema | ID, source, summary, priority, owner, scope, inputs, expected output |
| Dispatch policy | One task per worktree, batch size, priority rules, escalation rules |
| Executor | Agent, skill, script, deterministic worker, or human |
| Executor contract | Allowed tools, forbidden actions, output artifact, done condition |
| Verifier | Independent agent, tests, linter, policy check, human review, or combined gate |
| State store | Markdown file, issue board, database, queue, or ticket system |
| Next-round policy | Stop, retry, backoff, escalate, enqueue follow-up, or schedule next run |
| Limits | Token, cost, retries, time, concurrency, changed-files, blast radius |
| Human gate | Where a person must approve before external side effects |

## Output Template

```markdown
# Loop System Definition: [name]

## Purpose
- Goal:
- Non-goals:
- Human owner:

## Lifecycle
| Stage | Design |
|---|---|
| Discover tasks | |
| Dispatch tasks | |
| Execute | |
| Verify | |
| Persist state | |
| Decide next round | |

## Task Schema
| Field | Meaning |
|---|---|
| id | Stable task ID |
| source | Discovery source |
| summary | One-sentence task |
| priority | P0/P1/P2 or low/medium/high |
| scope | Files, services, tickets, or systems allowed |
| executor | Agent, skill, or script |
| expected_output | Patch, report, PR, comment, dashboard, or decision |
| verifier | Required gate |
| state | pending, running, blocked, verified, rejected, escalated, done |

## Controls
- Verification gate:
- State file:
- Retry policy:
- Budget limits:
- Concurrency limits:
- Human review gate:

## Next-Round Policy
- Continue when:
- Retry when:
- Escalate when:
- Stop when:

## Blockers Before Unattended Operation
- BLOCKER:
```

## Design Defaults

Use these defaults when the user has not specified otherwise:

- Start with one narrow discovery source.
- Use one task per isolated execution unit.
- Require independent verification before persistence marks a task done.
- Keep the first version human-reviewed before merge, publish, spend, or external notification.
- Store memory in a repository markdown file unless the user already has a ticketing or queue system.

## Common Mistakes

- Treating a cron job as a complete loop.
- Letting the executor decide its own success.
- Storing important state only in the chat transcript.
- Dispatching broad tasks such as "clean up the repo".
- Retrying without a limit or a changed strategy.
- Automating external side effects before human review exists.
