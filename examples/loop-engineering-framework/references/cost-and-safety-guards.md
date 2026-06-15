# Cost And Safety Guards

Use this reference when hardening a loop before automation or reviewing risks from unattended operation.

## Guardrail Principle

An unattended loop can make unattended mistakes. Every loop needs explicit limits, rejection paths, and human authority.

## Required Limits

Set these before a loop runs without direct supervision:

- Token or cost budget per round.
- Daily or weekly cost budget.
- Max retries per task.
- Max wall-clock time per round.
- Max concurrent tasks.
- Max changed files or external actions.
- Stop condition when evaluator fails.

If a limit cannot be measured, define an observable proxy.

## Safety Gates

| Side effect | Minimum gate |
|---|---|
| Code change | Tests plus independent review |
| Pull request | Human review before merge |
| Production deploy | Human approval and rollback plan |
| Public content | Draft plus human approval |
| External message | Human approval before send |
| Money spend | Human approval and spend cap |
| Data deletion | Human approval and backup or restore plan |
| Permission change | Human approval and audit log |

## Four Loop Costs

### Verification Debt

Symptom: the loop produces more artifacts than anyone verifies.

Guards:

- Independent evaluator.
- Human sample review.
- Queue limits.
- Reject and blocked states.

### Comprehension Rot

Symptom: the project changes faster than the owner understands.

Guards:

- Weekly sampled output review.
- Require executor summaries with rationale.
- Keep small task scope.
- Track changed systems in state.

### Cognitive Surrender

Symptom: humans stop having opinions and accept loop output by default.

Guards:

- Named human owner.
- Explicit reject authority.
- Human review for high-impact actions.
- Periodic "why was this right" review.

### Token Blowout

Symptom: retries, subagents, or schedules multiply cost unexpectedly.

Guards:

- Budget caps.
- Backoff after failure.
- Retry only with changed hypothesis.
- Stop on repeated verifier failure.
- Summarize state instead of rereading full history.

## Hardening Checklist

Before unattended operation, answer yes to all:

- Is there an independent evaluator or deterministic gate?
- Is state durable and readable next round?
- Are retry, time, cost, and concurrency limited?
- Is there an inbox for tasks needing human judgment?
- Are external side effects gated?
- Does the loop know when to stop?
- Can a human audit what happened?

Any no is a blocker or a supervised-pilot constraint.
