# Express Middleware Ordering Guidance

## Recommended Order
1. Request ID and logging context.
2. Security headers and coarse request filters.
3. Authentication and authorization.
4. Input validation and normalization.
5. Route handler.
6. Central error handler.

## Common Risks
- Auth after handler can expose unauthorized execution paths.
- Validation after handler can produce hidden runtime failures.
