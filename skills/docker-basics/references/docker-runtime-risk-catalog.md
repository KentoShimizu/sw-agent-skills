# Docker Runtime Risk Catalog

## High-Risk Patterns
- Privileged container execution.
- Broad writable filesystem with unclear ownership.
- Host network usage without clear need.
- Environment defaults that hide missing required config.
