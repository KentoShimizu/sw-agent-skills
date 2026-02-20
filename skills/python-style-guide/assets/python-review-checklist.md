# Python Review Checklist

## Architecture
- [ ] Module boundaries are cohesive.
- [ ] Side effects are isolated behind interfaces.

## Types And Data
- [ ] Public interfaces have type hints.
- [ ] Domain-critical structures use explicit models.
- [ ] `Any` usage is justified.

## Errors And Config
- [ ] Exception handling is explicit and meaningful.
- [ ] Required config fails fast at startup.

## Security And Ops
- [ ] Untrusted input validation exists.
- [ ] Sensitive data is redacted in logs.
- [ ] Metrics/logging support incident triage.
