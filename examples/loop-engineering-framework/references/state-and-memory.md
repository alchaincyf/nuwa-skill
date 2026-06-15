# State And Memory

Use this reference when designing persistent loop memory, markdown state files, task queues, run logs, and next-round inputs.

## Principle

The agent forgets; the repository, ticket system, or database does not. Loop memory must live outside the conversation context.

State is not a transcript. State is the minimum durable record required for the next round to continue safely.

## State File Requirements

A loop state file should record:

- Current round ID and timestamp.
- Discovery sources read.
- Task queue.
- Task status and owner.
- Verification evidence.
- Decisions and human approvals.
- Failures and retry counts.
- Inbox items needing human judgment.
- Next-round inputs.
- Budget usage or limit hits when available.

## Markdown State Template

```markdown
# Loop State: [loop-name]

## Control
- Owner:
- Last run:
- Next scheduled run:
- Max tasks per round:
- Max retries per task:
- Budget limit:
- Human review gate:

## Discovery Sources
| Source | Last checked | Cursor / filter | Notes |
|---|---|---|---|
| | | | |

## Task Queue
| ID | Source | Priority | Summary | State | Executor | Verifier | Retry | Next action |
|---|---|---|---|---|---|---|---|---|
| | | | | pending | | | 0 | |

## Run Log
### [timestamp] Round [id]
- Discovered:
- Dispatched:
- Verified:
- Rejected:
- Escalated:
- Budget:

## Verification Evidence
| Task ID | Verdict | Evidence | Checked by | Timestamp |
|---|---|---|---|---|
| | | | | |

## Decisions
| Decision | Human / gate | Reason | Timestamp |
|---|---|---|---|
| | | | |

## Inbox For Human Review
| ID | Reason | Needed decision | Retry next round |
|---|---|---|---|
| | | | |

## Next-Round Inputs
- Continue:
- Retry:
- Escalate:
- Skip:
```

## Status Vocabulary

Use stable task states:

- `pending`: discovered but not dispatched.
- `running`: assigned to an executor.
- `blocked`: cannot continue without missing context or permission.
- `rejected`: verification failed.
- `verified`: verification passed but final side effect may still need approval.
- `escalated`: waiting for human judgment.
- `done`: completed and persisted after required gates.
- `skipped`: intentionally ignored with reason.

Avoid ambiguous states such as "probably done" or "looks good".

## Update Rules

- Write state after discovery.
- Write state after dispatch.
- Write verification evidence before marking verified.
- Write human decision before external side effect.
- Increment retry count on each retry.
- Preserve rejected tasks and reasons for later learning.

## Common State Failures

- The next round has no cursor and rereads everything.
- Done tasks have no verification evidence.
- Rejected tasks disappear.
- Inbox items lack a needed decision.
- The state file becomes a narrative log instead of a queue and control surface.
