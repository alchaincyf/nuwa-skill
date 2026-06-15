# Runtime Adapters

Use this reference when mapping a Loop System Definition to Claude Code, Codex, GitHub Actions, or another runtime.

## Important Caveat

Runtime details change quickly. Before prescribing exact current commands, flags, product limits, or cloud availability, verify official documentation or clearly label the advice as conceptual.

This reference is a mapping guide, not a live product manual.

## Runtime-Agnostic Mapping

| Loop stage | Runtime capability to look for |
|---|---|
| Discover tasks | Tool access, connectors, scripts, search, issue APIs, CI APIs |
| Dispatch tasks | Task queue, subagents, worktrees, branches, issue assignment |
| Execute | Agent run, skill invocation, script, job runner |
| Verify | Tests, independent reviewer agent, policy checks, human approval |
| Persist state | Markdown file, issue tracker, database, artifact, queue |
| Decide next round | Scheduler, webhook, state cursor, retry policy, inbox |

## Claude-Style Notes

Conceptual mapping:

- Scheduled or repeated execution maps to a loop or automation facility when available.
- Goal-driven stopping maps to an independent completion checker when available.
- Parallel execution maps to subagents and worktree-style isolation when available.
- Skills should be invoked by name rather than pasted as long prompt walls.

Before implementation, verify current official docs for command names, expiry behavior, worktree flags, cloud availability, and scheduling limits.

## Codex-Style Notes

Conceptual mapping:

- Use a dedicated background worktree or branch for isolated execution when supported by the environment.
- Use Skills for reusable loop instructions.
- Use connectors or MCP tools for GitHub, Slack, issue trackers, databases, and external systems.
- Use an inbox or triage area for tasks that need human judgment.

Before implementation, verify current official docs for Automations, background worktrees, available connectors, and any cloud-job behavior.

## GitHub Actions Notes

GitHub Actions can provide scheduling and repository access, but it is not an evaluator by itself.

Use it for:

- Scheduled discovery.
- Running deterministic scripts.
- Running tests and lint.
- Persisting artifacts or opening issues.

Add separately:

- Agent execution environment.
- State file or issue-backed queue.
- Human review gate before merge.
- Budget or run-time limits.

## Local vs Cloud Scheduling

| Need | Prefer |
|---|---|
| Needs local dev server or local files | Local runner |
| Must run while laptop is off | Cloud runner |
| Needs minute-level checks | Local or supported scheduler with that granularity |
| Needs clean clone each run | Cloud or CI |
| Needs private logged-in desktop state | Local machine with explicit user control |

No scheduler choice removes the need for state, verification, and next-round policy.

## Implementation Readiness

Do not move from architecture to execution until the Loop System Definition includes:

- Discovery source and cursor.
- Dispatch policy.
- Executor contract.
- Independent verifier.
- Durable state.
- Next-round policy.
- Budget and retry limits.
- Human gate for external side effects.
