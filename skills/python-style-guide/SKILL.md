---
name: python-style-guide
description: "Style, review, and refactoring standards for Python codebases. Use when editing or reviewing `.py` files, Python runtime/packaging configuration (`pyproject.toml`, `requirements*.txt`, `uv.lock`), or Python application/test code executed by Python runtimes. Do not use for notebook-only data analysis conventions, shell scripting style, or non-Python language style concerns unless Python artifacts are also changed. In multi-language pull requests, run together with other applicable `*-style-guide` skills."
---

# Python Style Guide

Apply this checklist when writing or reviewing Python code.

## Trigger Reference

- Use `references/trigger-matrix.md` as the canonical trigger and co-activation matrix.
- Resolve skill activation from changed files with `python3 scripts/resolve_style_guides.py <changed-path>...` when automation is available.
- Validate trigger matrix consistency with `python3 scripts/validate_trigger_matrix_sync.py`.

## Architecture and module boundaries
## Quality Gate Reference

- Use `references/quality-gate-command-matrix.md` for CI check-only vs local autofix command mapping.

1. Keep modules cohesive and focused on one responsibility.
2. Isolate side effects (I/O, network, DB) behind clear interfaces.
3. Keep orchestration layers thin and move business rules into domain modules.
4. Avoid circular imports by keeping dependency direction explicit.

## Naming and code structure

1. Follow PEP 8 naming conventions (`snake_case`, `PascalCase`, `UPPER_CASE` constants).
2. Write small functions with explicit inputs/outputs.
3. Replace magic numbers with named constants that include units (`REQUEST_TIMEOUT_SECONDS`).
4. Add short comments only where intent is non-obvious.

## Typing and data modeling

1. Add type hints for public functions, methods, and complex locals.
2. Prefer explicit models (`dataclass`, `TypedDict`, Pydantic model) over loose dicts.
3. Avoid `Any` unless unavoidable and justified inline.
4. Define precise protocols/interfaces for pluggable dependencies.

## Error handling and control flow

1. Raise specific exception types with actionable messages.
2. Catch exceptions intentionally at boundaries and preserve causal chains.
3. Avoid broad `except Exception` unless rethrowing after required cleanup/logging.
4. Do not suppress failures with silent fallback logic by default.

## Configuration and environment

1. Parse and validate configuration at startup.
2. Fail startup when required environment variables are missing.
3. Do not hardcode fallback defaults for required environment variables.
4. Keep secrets in secret managers or injected environment, never in code.

## Security and compliance

1. Validate untrusted input at boundaries.
2. Use parameterized DB queries; never build SQL with string concatenation.
3. Avoid unsafe deserialization and command execution with unchecked input.
4. Redact secrets and sensitive fields from logs.

## Performance and efficiency

1. Measure bottlenecks before optimizing (`cProfile`, tracing, metrics).
2. Avoid N+1 data access patterns and repeated expensive computation.
3. Stream large datasets instead of loading everything into memory.
4. Use bounded retries/backoff with named constants.

## Testing and verification

1. Add unit tests for core logic and integration tests for boundaries.
2. Cover edge cases: invalid data, timeout, retry exhaustion, concurrency hazards.
3. Add regression tests for every bug fix.
4. Document manual verification when automation cannot cover behavior.

## Observability and operations

1. Use structured logs with trace/request IDs.
2. Emit metrics for latency, throughput, and errors.
3. Normalize exception-to-error response mapping at API boundaries.
4. Ensure alertable signals exist for critical failure paths.

## CI required quality gates (check-only)

1. Run `uv run ruff format --check .`.
2. Run `uv run ruff check .`.
3. Run `uv run mypy .` (or project type checker equivalent).
4. Run `uv run pytest -q`.

## Optional autofix commands (local)

1. Run `uv run ruff format .`.
2. Run `uv run ruff check --fix .` for safe lint autofixes, then re-run checks.
