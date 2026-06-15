# Dispatch And Isolation

Use this reference when a loop needs task splitting, parallel execution, worktree isolation, inbox handling, or clear handoff contracts.

## Dispatch Goal

Dispatch converts discovered work into bounded tasks that can be executed, verified, and persisted independently. If dispatch is vague, verification and rollback become vague.

## Task Boundary Rules

A dispatched task should have:

- One source item or tightly related cluster.
- One owner or executor.
- One expected output.
- One verification path.
- One state entry.
- A small allowed scope.

Avoid tasks that say "improve", "clean up", "fix everything", or "investigate all failures" without a bounded output.

## Dispatch Policy Template

```markdown
## Dispatch Policy
- Intake queue:
- Batch size per round:
- Priority order:
- Task grouping rule:
- Max parallel tasks:
- Isolation method:
- Handoff artifact:
- Escalation trigger:
```

## Isolation Choices

| Situation | Recommended isolation |
|---|---|
| One task, read-only report | No worktree required; persist report state |
| One code change | Dedicated branch or worktree preferred |
| Multiple parallel code changes | One worktree per task |
| Production mutation | No autonomous execution without human approval |
| External notifications | Draft first, human approves send |

Worktree isolation matters when multiple agents can modify files. Without isolation, outputs blur together and review loses attribution.

## Handoff Contract

Each task handed to an executor must include:

- Task ID.
- Source evidence.
- Allowed scope.
- Forbidden actions.
- Expected output.
- Verification command or evaluator.
- Where to write status.

Example:

```markdown
### Task LOOP-2026-001
- Source: failing CI job `auth-tests`
- Scope: `test/auth/**`, `src/auth/**`
- Executor: code-fix agent with project test skill
- Expected output: patch plus short explanation
- Forbidden: dependency upgrades, database migrations, broad refactors
- Verify: `npm test -- test/auth` and independent reviewer agent
- State path: `loop-state.md`
```

## Inbox Handling

Use an inbox when the loop discovers work it should not execute automatically.

Inbox items should include:

- Why the task was not dispatched.
- What information is missing.
- Who should decide.
- Whether it should be retried next round.

Good inbox reasons:

- Scope too broad.
- Requires product judgment.
- Requires credentials or permissions.
- Could affect production users.
- Verification path unavailable.

## Parallelism Limits

Parallelism is a multiplier for both throughput and confusion. Set limits:

- Max tasks per round.
- Max concurrent agents.
- Max changed files per task.
- Max retries per task.
- Merge or publish only after verification and human review.

If conflicts appear repeatedly, reduce batch size before adding more automation.
