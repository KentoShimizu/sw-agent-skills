# Express API Error Catalog Template

| Error Code | HTTP Status | Meaning | Retryable | Client Action |
| --- | --- | --- | --- | --- |
| EXAMPLE_INVALID_INPUT | 400 | Request validation failed | no | Fix request payload |
| EXAMPLE_CONFLICT | 409 | Conflict with existing state | no | Resolve conflict and retry |
| EXAMPLE_RATE_LIMIT | 429 | Request rate exceeded | yes | Backoff and retry |
