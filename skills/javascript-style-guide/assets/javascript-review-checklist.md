# JavaScript Review Checklist

## Architecture
- [ ] Module boundaries are cohesive and side effects are isolated.
- [ ] Entry points are thin; domain logic is reusable and testable.

## Data And Runtime Safety
- [ ] Boundary payloads are validated with explicit schemas.
- [ ] Ambiguous object-bag passing is avoided on critical paths.
- [ ] Required env vars are validated at startup.

## Async And Errors
- [ ] Async flow uses consistent `async/await` style.
- [ ] Error handling preserves root cause and operational meaning.
- [ ] Failures are not silently swallowed.

## Security And Performance
- [ ] Input sanitization/escaping is context-appropriate.
- [ ] Concurrency is bounded for bulk async work.
- [ ] Large payload processing is streamed/paginated where required.

## Verification
- [ ] Tests cover happy, edge, and failure paths.
- [ ] Regression tests exist for bug fixes.
