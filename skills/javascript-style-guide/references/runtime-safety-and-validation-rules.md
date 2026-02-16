# JavaScript Runtime Safety And Validation Rules

- Validate untrusted inputs before business logic.
- Keep schema validation close to trust boundaries.
- Prefer explicit error classes for operationally distinct failures.
- Avoid fallback behavior that masks required configuration gaps.
- Ensure logging contains enough context for triage without leaking secrets.
