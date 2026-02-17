---
name: csharp-style-guide
description: "Style, review, and refactoring standards for C#/.NET codebases. Trigger when `.cs`, `.csproj`, `.sln`, `.props`, `.targets`, or `.razor` artifacts are created, modified, or reviewed and C#-specific quality rules (naming, nullability, async patterns, API design consistency) must be enforced. Do not use for Java/Kotlin or JavaScript/TypeScript style concerns unless C# artifacts are also changed. In multi-language pull requests, run together with other applicable `*-style-guide` skills."
---

# Csharp Style Guide

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

Use this skill to write and review C# code that is safe, maintainable, and production-ready.

## Trigger And Co-activation Reference

- If available, use `references/trigger-matrix.md` as the canonical trigger/co-activation matrix.
- If available, resolve style-guide activation from changed files with `python3 scripts/resolve_style_guides.py <changed-path>...`.
- If available, validate trigger matrix consistency with `python3 scripts/validate_trigger_matrix_sync.py`.

## Quality Gate Command Reference

- If available, use `references/quality-gate-command-matrix.md` for CI check-only vs local autofix mapping.

## Quick Start Snippets

### Startup options validation (fail fast)

```csharp
builder.Services
    .AddOptions<MyServiceOptions>()
    .Bind(builder.Configuration.GetSection("MyService"))
    .ValidateDataAnnotations()
    .ValidateOnStart();
```

### CancellationToken propagation

```csharp
public async Task<OrderDto> GetOrderAsync(Guid orderId, CancellationToken cancellationToken)
{
    var entity = await _repository.FindByIdAsync(orderId, cancellationToken);
    return entity is null ? throw new NotFoundException(orderId) : Map(entity);
}
```

### Specific exception handling at boundary

```csharp
try
{
    await _publisher.PublishAsync(message, cancellationToken);
}
catch (TimeoutException ex)
{
    _logger.LogWarning(ex, "Publish timeout for message {MessageId}", message.Id);
    throw new TransientDependencyException("Publish timed out", ex);
}
```

## Architecture And Module Boundaries

1. Keep dependency direction explicit (domain -> application -> infrastructure).
2. Isolate side effects (I/O, DB, network) behind interfaces.
3. Keep controllers/handlers thin; move business rules into domain/application services.
4. Split classes by responsibility; avoid god classes.

## Naming And Code Structure

1. Use PascalCase for types/methods/properties, camelCase for locals/parameters.
2. Use intent-revealing names instead of implementation detail names.
3. Keep methods focused; extract private helpers for complex branches.
4. Replace magic numbers with named constants including units (`RetryDelayMilliseconds`).

## Types And Data Modeling

1. Enable nullable reference types and treat warnings as actionable.
2. Prefer explicit DTO/value objects over `dynamic` or loosely typed dictionaries.
3. Use `record` for immutable data where semantics fit.
4. Define explicit boundary contracts for request/response models.

## Error Handling And Async Behavior

1. Throw specific exception types with actionable context.
2. Catch exceptions at boundaries and map intentionally (retry/log/translate/rethrow).
3. Avoid blanket `catch (Exception)` unless rethrowing after required handling.
4. Pass `CancellationToken` through async chains.
5. Avoid sync-over-async (`.Result`, `.Wait()`).

## Configuration And Environment

1. Bind configuration to typed options and validate at startup.
2. Fail startup when required environment variables/config are missing.
3. Do not add silent fallback defaults for required configuration.
4. Keep secrets in secret stores, not source code.

## Security And Compliance

1. Validate/sanitize external input.
2. Use parameterized queries/ORM bindings; never concatenate SQL.
3. Enforce authn/authz close to entry points.
4. Avoid logging sensitive data (tokens, passwords, PII).

## Performance And Resource Usage

1. Profile before micro-optimization.
2. Use streaming/pagination for large datasets.
3. Reuse outbound clients (`IHttpClientFactory`).
4. Respect cancellation and timeout policies for outbound I/O.

## Testing And Verification

1. Add unit tests for business logic and integration tests for boundaries.
2. Cover nullability, cancellation, timeout, invalid payloads, and concurrency edges.
3. Add regression tests for each fixed defect.
4. Document manual verification when automation is infeasible.

## Observability And Operations

1. Use structured logs with correlation/request IDs.
2. Emit metrics for latency, errors, and dependency calls.
3. Map failures to stable operational signals (status/error codes).
4. Ensure telemetry supports incident triage.

## CI Required Quality Gates (check-only)

1. Run `dotnet format --verify-no-changes`.
2. Run `dotnet build -warnaserror`.
3. Run `dotnet test`.
4. Reject changes that hide failures with broad fallbacks.

## Optional Autofix Commands (local)

1. Run `dotnet format`.
