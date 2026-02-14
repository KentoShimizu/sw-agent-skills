---
name: csharp-style-guide
description: "Style, review, and refactoring standards for C#/.NET codebases. Use when editing or reviewing `.cs`, `.csproj`, `.sln`, `.props`, `.targets`, or `.razor` files, or `dotnet`-compiled application/test code. Do not use for Java/Kotlin or JavaScript/TypeScript style concerns unless C# artifacts are also changed. In multi-language pull requests, run together with other applicable `*-style-guide` skills."
---

# Csharp Style Guide

Apply this checklist when writing or reviewing C# code.

## Trigger Reference

- Use `references/trigger-matrix.md` as the canonical trigger and co-activation matrix.
- Resolve skill activation from changed files with `python3 scripts/resolve_style_guides.py <changed-path>...` when automation is available.
- Validate trigger matrix consistency with `python3 scripts/validate_trigger_matrix_sync.py`.

## Architecture and module boundaries
## Quality Gate Reference

- Use `references/quality-gate-command-matrix.md` for CI check-only vs local autofix command mapping.

1. Keep dependency direction explicit: domain -> application -> infrastructure.
2. Isolate side effects (I/O, DB, network) behind interfaces.
3. Keep controllers/handlers thin; move business rules into services.
4. Avoid god classes; split by responsibility and bounded context.

## Naming and code structure

1. Use PascalCase for types/methods/properties, camelCase for locals/parameters.
2. Use descriptive names that capture intent, not implementation detail.
3. Keep methods focused; extract private methods for complex branches.
4. Replace magic numbers with named constants including units (`RetryDelayMilliseconds`).

## Types and data modeling

1. Enable nullable reference types and treat warnings as actionable.
2. Prefer explicit DTO/value objects over `dynamic` or loosely typed maps.
3. Use `record` for immutable data where semantics fit.
4. Define clear request/response contracts at boundaries.

## Error handling and async behavior

1. Throw specific exception types with actionable context.
2. Catch exceptions at boundaries to map behavior intentionally (retry/log/translate/rethrow).
3. Avoid blanket `catch (Exception)` unless rethrowing after required logging/cleanup.
4. Pass `CancellationToken` through async call chains.
5. Avoid sync-over-async patterns (`.Result`, `.Wait()`).

## Configuration and environment

1. Bind configuration to typed options classes and validate on startup.
2. Fail application startup when required environment variables are missing.
3. Do not assign fallback defaults for required environment variables.
4. Keep secrets in secret stores; do not hardcode credentials.

## Security and compliance

1. Validate and sanitize all external input.
2. Use parameterized queries/ORM bindings; never concatenate SQL.
3. Enforce auth/authz checks close to entry points.
4. Avoid logging sensitive data (tokens, passwords, PII).

## Performance and resource usage

1. Avoid unnecessary allocations in hot paths; profile before micro-optimizing.
2. Use streaming/pagination for large datasets.
3. Reuse `HttpClient` through factory patterns.
4. Respect cancellation and timeouts for outbound I/O.

## Testing and verification

1. Add unit tests for business logic and integration tests for external boundaries.
2. Cover edge cases: nullability, cancellation, timeout, invalid payloads, concurrency.
3. Add regression tests for each fixed bug.
4. Document manual verification when automation is not feasible.

## Observability and operations

1. Use structured logs with correlation/request IDs.
2. Emit metrics for latency, errors, and dependency calls.
3. Map errors to stable operational signals (status codes, error codes).
4. Ensure logs and metrics are sufficient for incident triage.

## CI required quality gates (check-only)

1. Run `dotnet format --verify-no-changes`.
2. Run `dotnet build -warnaserror`.
3. Run `dotnet test`.
4. Reject changes that hide failures with broad fallbacks.

## Optional autofix commands (local)

1. Run `dotnet format` to apply style fixes.
