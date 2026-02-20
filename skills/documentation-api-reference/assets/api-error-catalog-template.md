# API Error Catalog Template

| Code | HTTP Status | Meaning | Retryable | Client Action |
| --- | --- | --- | --- | --- |
| EXAMPLE_INVALID_INPUT | 400 | Input validation failed | no | fix input and retry |
| EXAMPLE_RATE_LIMITED | 429 | Request quota exceeded | yes | backoff and retry |
