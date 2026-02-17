---
name: java-style-guide
description: "Style, review, and refactoring standards for Java codebases with strong typing, explicit failure handling, and maintainable architecture boundaries. Use when `.java`, `pom.xml`, `build.gradle`, or `build.gradle.kts` artifacts are created, changed, or reviewed and Java-specific quality rules must be enforced. Do not use for Kotlin-only, Android-Gradle-only, or non-JVM language style concerns unless Java artifacts are also changed."
---

# Java Style Guide

## Overview
Use this skill to evaluate and improve Java code for correctness, maintainability, and operational reliability.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Trigger Reference
- Use `references/trigger-matrix.md` as the canonical trigger and co-activation matrix.
- Resolve skill activation from changed files with `python3 scripts/resolve_style_guides.py <changed-path>...` when automation is available.
- Validate trigger matrix consistency with `python3 scripts/validate_trigger_matrix_sync.py`.

## Quality Gate Reference
- Use `references/quality-gate-command-matrix.md` for CI check-only vs local autofix command mapping.

## Shared References
- Null and exception handling rules:
  - `references/null-and-exception-rules.md`

## Templates And Assets
- Java review checklist:
  - `assets/java-review-checklist.md`
- Refactor planning template:
  - `assets/java-refactor-plan-template.md`

## Inputs To Gather
- Changed modules and architectural boundaries impacted.
- Current quality risks (null handling, exception mapping, performance hotspots).
- Team conventions for formatting, static analysis, and test requirements.
- Operational constraints (security/compliance/latency/SLO concerns).

## Deliverables
- Review findings prioritized by production risk.
- Refactor plan with explicit scope and rollback assumptions.
- Verification plan covering tests and operational checks.
- Clear go/no-go criteria for merge readiness.

## Workflow
1. Confirm trigger fit and impacted Java artifacts.
2. Build/refine change plan using `assets/java-refactor-plan-template.md`.
3. Review code with `assets/java-review-checklist.md` and project quality gates.
4. Apply refactors that reduce coupling, ambiguity, and hidden failure paths.
5. Validate with CI check-only gates and targeted runtime checks.
6. Publish residual risks and follow-up owners.

## Review And Refactor Checklist

### Architecture and layering
1. Keep dependency direction clean: domain -> application -> infrastructure.
2. Keep controllers/resources thin and delegate business logic to services.
3. Isolate integration concerns (DB, HTTP, queues) behind clear adapters.
4. Keep modules cohesive and avoid utility classes that become dumping grounds.

### Naming and structure
1. Use standard Java naming (`UpperCamelCase` classes, `lowerCamelCase` fields/methods).
2. Keep methods focused and short; extract intent-revealing helpers.
3. Use `static final` constants for fixed values; include units in names (`CACHE_TTL_SECONDS`).
4. Prefer composition over deep inheritance unless polymorphism is essential.

### Types and data modeling
1. Use explicit types and generics; avoid raw types.
2. Prefer immutable DTO/value objects where possible.
3. Model boundary payloads with dedicated classes, not generic maps.
4. Validate object invariants at construction time.

### Exceptions and failure handling
1. Throw domain-specific exceptions with actionable context.
2. Catch exceptions at service/API boundaries and map to stable error responses.
3. Avoid broad `catch (Exception)` except for mandatory boundary handling.
4. Preserve root cause (`throw new XException("...", cause)`).
5. Do not hide failures behind fallback logic without explicit business requirement.

### Configuration and environment
1. Bind configuration into typed classes (`@ConfigurationProperties`, equivalent).
2. Validate required configuration during startup and fail fast when missing.
3. Do not provide silent default values for required environment variables.
4. Store secrets outside code and avoid logging them.

### Security and compliance
1. Validate and sanitize all untrusted input.
2. Use parameterized queries/ORM APIs; never construct SQL by concatenation.
3. Enforce authorization at entry points and sensitive operations.
4. Avoid exposing internal stack traces or sensitive fields to clients.

### Performance and scalability
1. Measure with profiling before optimization.
2. Avoid N+1 queries and repeated remote calls in loops.
3. Use pagination/streaming for large result sets.
4. Set explicit timeouts/retries for outbound network calls.

### Testing and verification
1. Add unit tests for domain logic and integration tests for adapters.
2. Cover edge cases: invalid inputs, null handling, timeout, concurrency.
3. Add regression tests for bug fixes.
4. Document manual verification when automation is unavailable.

### Observability and operations
1. Use structured logging with trace/request IDs.
2. Emit metrics for latency, failures, and dependency health.
3. Keep error codes stable and actionable for operations.
4. Ensure readiness/liveness checks reflect dependency state.

## CI Required Quality Gates (check-only)
1. Run project check-only formatter/lint (`spotlessCheck`, `checkstyle`, or equivalent).
2. Run static analysis (`errorprone`, `spotbugs`, or configured equivalent).
3. Run automated tests (`./gradlew test` or `mvn test`).
4. Reject changes that degrade type safety or mask failures.

## Optional Autofix Commands (local)
1. Run formatter autofix (`spotlessApply`, or project equivalent) and then re-run checks.

## Failure Conditions
- Stop when architectural boundaries are ambiguous and cannot be validated.
- Stop when required config/secret handling relies on hidden defaults.
- Escalate when static analysis or tests reveal unresolved high-risk defects.
