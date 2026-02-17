# Failure Mode And Consistency Rules

- Define per-flow consistency needs first (strong, bounded staleness, eventual).
- Never apply retries without idempotency analysis and retry budget limits.
- Timeouts must reflect dependency SLOs and avoid cascading retry storms.
- Explicitly model duplicate, delayed, and out-of-order delivery behavior.
- Prefer monotonic versioning or conflict resolution where concurrent writes occur.
- Validate assumptions with chaos/fault tests, not only unit tests.
