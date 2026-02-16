# Compose Dependency Guidance

## Principles
- Use health-check based dependencies for stateful services.
- Avoid implicit startup race dependencies.
- Separate optional tools using profiles.
- Keep service contracts (port/env/volume) explicit.
