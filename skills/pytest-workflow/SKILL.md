---
name: pytest-workflow
description: "Pytest test design workflow. Use when test or evidence artifacts are the primary output for verification; do not use for product requirement prioritization or architecture topology selection."
---

# Pytest Workflow

## Trigger Boundary
- Use when Python verification is implemented with pytest.
- Do not use for framework-agnostic test strategy only; use `testing-*` skills.
- Do not use for load/performance benchmarking scripts.

## Goal
Create fast, reliable, and debuggable pytest suites aligned with change risk.

## Inputs
- Change scope and risk profile
- Existing fixture and test structure
- Environment and data setup constraints

## Outputs
- Test case matrix with fixture strategy
- Parametrized tests for boundary and error scenarios
- Failure triage notes with reproducible commands

## Workflow
1. Map behavior risks to unit/integration pytest scopes.
2. Build reusable fixtures with explicit lifecycle.
3. Use parametrization for edge-case coverage without duplication.
4. Keep assertions specific and failure messages actionable.
5. Optimize runtime by isolating slow tests and markers.

## Quality Gates
- Fixtures are deterministic and avoid hidden global state.
- Parametrization improves coverage without unreadable tests.
- Test failures point to a single clear cause.
- Test runtime remains practical for local and CI execution.

## Failure Handling
- Stop when fixtures produce non-deterministic outcomes.
- Escalate when test runtime blocks practical feedback loops.
