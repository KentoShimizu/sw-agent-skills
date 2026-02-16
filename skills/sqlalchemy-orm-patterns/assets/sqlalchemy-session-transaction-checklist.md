# SQLAlchemy Session And Transaction Checklist

- [ ] Session scope is explicit (request/unit-of-work).
- [ ] Transaction boundaries are explicit for multi-write operations.
- [ ] Rollback behavior is defined for failure paths.
- [ ] N+1 risk is reviewed for relationship loading.
