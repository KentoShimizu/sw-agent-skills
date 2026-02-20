# Java Review Checklist

## Architecture
- [ ] Dependency direction is one-way (domain -> application -> infrastructure).
- [ ] Controllers/resources are thin; business logic is in services/domain.
- [ ] External integrations are isolated behind adapters.

## Type And Data Safety
- [ ] Raw types are avoided; generics are explicit.
- [ ] Domain-critical payloads use dedicated types, not generic maps.
- [ ] Invariants are enforced at construction/boundary validation.

## Error And Configuration
- [ ] Exception mapping is explicit at boundaries.
- [ ] Broad `catch (Exception)` is avoided unless boundary-required.
- [ ] Required configuration fails fast when missing.

## Security And Performance
- [ ] Input validation/sanitization exists at trust boundaries.
- [ ] SQL/command injection paths are avoided.
- [ ] N+1 and repeated remote call risks are assessed.

## Verification
- [ ] Unit and integration coverage matches risk profile.
- [ ] Regression tests exist for defect fixes.
