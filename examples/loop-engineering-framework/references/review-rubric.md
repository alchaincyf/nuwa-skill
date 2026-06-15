# Review Rubric

Use this reference when the user asks whether a loop design is complete, safe, or ready for automation.

## Review Output Template

```markdown
# Loop Review

## Verdict
- Readiness: not a loop / design-only / supervised pilot / unattended-ready
- Main blocker:
- Highest-risk failure mode:

## Lifecycle Scorecard
| Stage | Score | Finding | Required fix |
|---|---:|---|---|
| Discover tasks | 0-2 | | |
| Dispatch tasks | 0-2 | | |
| Execute | 0-2 | | |
| Verify | 0-2 | | |
| Persist state | 0-2 | | |
| Decide next round | 0-2 | | |

## Blockers
- BLOCKER:

## Hardening Plan
1.
2.
3.
```

Score:

- `0`: missing or unsafe.
- `1`: present but vague or manually dependent.
- `2`: explicit, bounded, and reviewable.

## Lifecycle Findings

### Discover Tasks

Check:

- Sources are named.
- Cursors or time windows exist.
- Actionable criteria are explicit.
- Non-actionable items go to inbox or skipped state.

Missing criteria means the loop cannot choose useful work.

### Dispatch Tasks

Check:

- Discovered work becomes bounded task units.
- Priority and batch size are defined.
- Each task has allowed scope and expected output.
- Parallel work has isolation.

Missing dispatch boundaries means execution scope will blur.

### Execute

Check:

- Executor is named: agent, skill, script, or human.
- Allowed tools and forbidden actions are clear.
- Done condition is artifact-based.
- External side effects are gated.

### Verify

Check:

- Verification is independent from execution.
- The verifier can reject.
- Evidence is behavioral where possible.
- Deterministic checks run when available.

Missing independent verification blocks unattended automation.

### Persist State

Check:

- State lives outside chat context.
- Task queue and run log are durable.
- Verification evidence is stored.
- Rejections and human decisions are preserved.

Missing persisted state means it is not a real loop.

### Decide Next Round

Check:

- Continue, retry, escalate, and stop rules exist.
- Retry limits exist.
- Human inbox is handled.
- Schedule or trigger uses state from previous rounds.

Missing next-round policy means repeated execution, not a controlled loop system.

## Six Parts Check

| Part | Review question |
|---|---|
| Automation | What starts the round, and under what limits? |
| Isolation | How are parallel or risky tasks separated? |
| Skill | What reusable instructions does the executor use? |
| Connector | What external systems can the loop read or write? |
| Evaluator | Who or what can say no? |
| Memory | Where does durable state live? |

## Four Cost Checks

| Cost | Symptom | Guard |
|---|---|---|
| Verification debt | Outputs pile up without real review | Independent evaluator and human gate |
| Comprehension rot | Human stops understanding generated changes | Scheduled review of sampled outputs |
| Cognitive surrender | Human accepts whatever loop returns | Explicit owner and reject authority |
| Token blowout | Run count or retries explode | Budget, retry, and concurrency limits |

## Readiness Verdicts

- **Not a loop**: no persisted state or next-round policy.
- **Design-only**: lifecycle exists on paper but no tested verifier or state file.
- **Supervised pilot**: lifecycle, state, and verifier exist; human reviews every external side effect.
- **Unattended-ready**: only for low-risk domains with tested evaluator, limits, rollback path, and human-visible audit log.

Default to supervised pilot unless the user proves the risk is low and gates are tested.
