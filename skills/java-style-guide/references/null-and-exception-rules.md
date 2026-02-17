# Java Null And Exception Rules

- Do not use null as implicit control flow across service boundaries.
- Validate nullable external inputs at API/deserialization boundaries.
- Throw domain-specific exceptions with actionable context.
- Preserve cause chains when wrapping exceptions.
- Convert exceptions to stable API/operational error contracts at boundaries.
