# Express API Verification Checklist

- [ ] Middleware order is explicit and deterministic.
- [ ] Validation executes before business handlers.
- [ ] Error handler returns consistent response shape.
- [ ] Auth and rate limits are applied to protected endpoints.
- [ ] Correlation ID and core request logs are present.
