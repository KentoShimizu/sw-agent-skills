---
name: jest-testing-workflow
description: "Jest testing workflow for JavaScript/TypeScript projects. Trigger when implementation changes need executable verification via Jest (unit/integration behavior, mocks, coverage evidence, regression checks) before merge; do not use for product requirement prioritization or architecture topology selection."
---

# Jest Testing Workflow

## Trigger Boundary
- Use when JS/TS test implementation relies on Jest.
- Do not use for end-to-end browser runs; use `playwright` or `testing-e2e`.
- Do not use for language-agnostic testing policy only.

## Goal
Deliver maintainable Jest suites with deterministic behavior and clear failure signals.

## Inputs
- Module behavior and test target scope
- Mocking boundaries and dependency behavior
- Runtime environment (node/jsdom) constraints

## Outputs
- Test suite structure and mock strategy
- Assertion plan for happy, edge, and failure paths
- Execution profile plan (watch mode, CI mode, coverage)

## Workflow
1. Define test scope by module responsibility and risk.
2. Set environment and mocking boundaries explicitly.
3. Write focused tests with minimal, meaningful assertions.
4. Use fake timers and async controls intentionally.
5. Keep coverage goals aligned to behavior risk, not raw percentages.

## Quality Gates
- Mock usage does not hide integration-critical behavior.
- Async tests are stable and free from timing flakiness.
- Assertions are specific enough to localize failures quickly.
- CI execution settings are reproducible from local commands.

## Failure Handling
- Stop when mock strategy breaks behavior realism.
- Escalate when flakiness persists despite deterministic controls.
