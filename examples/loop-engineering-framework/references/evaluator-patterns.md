# Evaluator Patterns

Use this reference when designing verification gates, reviewer agents, deterministic checks, or human approval points.

## Principle

The executor should not be the only judge of its own work. A loop needs something that can say no.

Use a maker-checker structure:

- **Maker**: discovers or executes work.
- **Checker**: independently verifies the result.
- **Gate**: decides whether the task can advance state.

## Evaluator Types

| Evaluator | Best for | Limits |
|---|---|---|
| Deterministic tests | Code behavior, lint, build, type checks | Only covers encoded expectations |
| Independent agent | Design review, code review, report critique | Needs skeptical instructions and evidence |
| Different model or fresh context | Reducing self-justification | Still needs tools or evidence |
| Human reviewer | Judgment, risk, production effects | Slower; should be placed at high-leverage gates |
| Policy checklist | Security, privacy, compliance, brand, cost | Must be explicit and current |

Prefer combinations. For code loops, use tests plus independent review. For content loops, use policy checks plus human approval before publishing.

## Skeptical Evaluator Contract

An evaluator should receive:

- Task ID and original source.
- Executor output.
- Done criteria.
- Verification commands or inspection steps.
- Rejection reasons to check.
- Authority to mark rejected, blocked, or needs-human.

Evaluator stance:

- Assume the output is incomplete until evidence proves otherwise.
- Check behavior, not only explanation.
- Treat missing evidence as failure.
- Do not repair the output unless explicitly assigned a separate repair task.
- Write a verdict and evidence into state.

## Evaluator Output Template

```markdown
## Verification Result: [task-id]
- Verdict: verified / rejected / blocked / needs-human
- Evidence checked:
- Commands or tools run:
- Failed checks:
- Risk notes:
- Required next action:
```

## Rejection Reasons

Reject when:

- The expected output is missing.
- Tests, lints, builds, or policy checks fail.
- The change exceeds allowed scope.
- The output has no evidence.
- The executor changed unrelated behavior.
- The task requires judgment that was not approved by a human.
- The state update claims success without verification.

## Human Review Gates

Require human approval before:

- Merge to protected branch.
- Production deploy.
- Public publish.
- External notification.
- Spending money.
- Deleting data.
- Changing permissions or secrets.
- Sending messages as a person or organization.

## Stop Conditions

Stop the loop round when:

- The same task fails verification twice.
- Required context or credentials are missing.
- Budget, retry, or time limit is reached.
- The evaluator cannot run.
- The next action requires human judgment.

Do not let retries become a substitute for diagnosis.
