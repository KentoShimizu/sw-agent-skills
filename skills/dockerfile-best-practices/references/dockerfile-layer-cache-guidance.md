# Dockerfile Layer And Cache Guidance

## Layer Ordering
- Place low-churn dependency install steps before high-churn source copy.
- Separate build and runtime stages to reduce final image size.

## Cache Discipline
- Keep deterministic dependency manifests.
- Avoid invalidating cache with unnecessary context changes.
