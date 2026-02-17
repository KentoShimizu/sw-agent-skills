---
name: go-style-guide
description: "Style, review, and refactoring standards for Go codebases. Trigger when `.go`, `go.mod`, `go.sum`, or `go.work` files are created, changed, or reviewed and Go-specific quality rules (error handling, concurrency patterns, interface design, package boundaries) must be enforced. Do not use for generic shell scripts, SQL-only changes, or non-Go runtime style concerns unless Go artifacts are also changed. In multi-language pull requests, run together with other applicable `*-style-guide` skills."
---

# Go Style Guide

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

Apply this checklist when writing or reviewing Go code.

## Trigger Reference

- Use `references/trigger-matrix.md` as the canonical trigger and co-activation matrix.
- Resolve skill activation from changed files with `python3 scripts/resolve_style_guides.py <changed-path>...` when automation is available.
- Validate trigger matrix consistency with `python3 scripts/validate_trigger_matrix_sync.py`.

## Package design and architecture
## Quality Gate Reference

- Use `references/quality-gate-command-matrix.md` for CI check-only vs local autofix command mapping.

1. Keep packages cohesive and small; avoid cyclic dependencies.
2. Depend on interfaces at boundaries and concrete types internally.
3. Keep handlers/controllers thin; isolate domain logic in dedicated services.
4. Keep `cmd/` orchestration separate from reusable package logic.

## Naming and structure

1. Use concise names that match Go conventions and package context.
2. Prefer small functions with clear contracts.
3. Replace magic numbers with named constants that include units (`requestTimeoutSeconds`).
4. Avoid global mutable state unless synchronized and justified.

## Types and data modeling

1. Model external payloads with explicit structs and tags.
2. Avoid `map[string]any` for core domain flows when a struct is known.
3. Use constructors/validators to keep structs in valid states.
4. Prefer explicit zero-value semantics; document when zero is invalid.

## Error handling and concurrency

1. Return errors instead of panicking for expected failures.
2. Wrap errors with context (`fmt.Errorf("...: %w", err)`) and inspect with `errors.Is/As`.
3. Avoid swallowing errors; handle or return intentionally.
4. Pass `context.Context` as the first parameter for request-scoped operations.
5. Design goroutine lifecycles explicitly; avoid leaks and orphaned workers.

## Configuration and environment

1. Parse configuration at startup into typed structs.
2. Fail startup when required environment variables are missing.
3. Do not assign fallback defaults for required environment variables.
4. Keep secrets out of source and logs.

## Security and compliance

1. Validate all external inputs and enforce allow-lists where possible.
2. Use parameterized SQL and safe encoding for outputs.
3. Set explicit HTTP timeouts on clients and servers.
4. Avoid leaking sensitive values in error messages or logs.

## Performance and scalability

1. Measure with benchmarks/profiles before optimizing.
2. Avoid unnecessary allocations in hot paths.
3. Stream large data instead of loading fully into memory.
4. Bound retries and worker pools with named limits.

## Testing and verification

1. Write table-driven tests for core logic and edge cases.
2. Add integration tests for DB/network boundaries.
3. Run race detection for concurrent code.
4. Add regression tests for every fixed bug.

## Observability and operations

1. Emit structured logs with request/correlation IDs.
2. Track latency, error rates, and saturation metrics.
3. Preserve wrapped error chains for faster incident diagnosis.
4. Ensure health/readiness checks reflect real dependencies.

## CI required quality gates (check-only)

1. Run `gofmt -l .` and require empty output.
2. Run `go vet ./...`.
3. Run `staticcheck ./...` when available.
4. Run `go test ./... -race`.

## Optional autofix commands (local)

1. Run `gofmt -w .` (or `go fmt ./...`) to apply formatting.
