# FastAPI Schema Contract Guidance

- Define request and response models before handler implementation.
- Use strict field constraints where behavior depends on value ranges.
- Keep error response shape consistent across endpoints.
- Treat OpenAPI as a contract artifact, not a side effect.
