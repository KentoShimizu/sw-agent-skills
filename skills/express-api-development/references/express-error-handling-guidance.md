# Express Error Handling Guidance

- Use a centralized error middleware as the single response boundary.
- Normalize known domain errors into stable API error codes.
- Avoid swallowing async errors; always call `next(error)`.
- Include request correlation IDs in all error responses/log entries.
