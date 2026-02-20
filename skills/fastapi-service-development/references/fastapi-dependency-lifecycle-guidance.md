# FastAPI Dependency Lifecycle Guidance

- Use dependency providers to manage shared resources (DB clients, service clients, auth context).
- Keep dependency scope explicit (`request` vs longer-lived).
- Ensure cleanup behavior is deterministic for resources with connections/state.
