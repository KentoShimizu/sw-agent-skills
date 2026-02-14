---
name: testing-mutation
description: Specialized workflow for mutation score improvement and weak assertion detection. Use when designing verification strategy and evidence at this test level; do not use for observability ownership or release scheduling policy.
---

# Testing Mutation

## Trigger Boundary
- Use when verification strategy or release confidence evidence must be designed.
- Do not use for production observability ownership; use `observability-*`.
- Do not use for architecture topology selection.

## Goal
Build sufficient verification evidence to prevent regressions.

## Inputs
- Change scope and risk profile
- Domain evidence for mutation score improvement and weak assertion detection
- Operational, compliance, and rollout constraints

## Outputs
- Mutation analysis report with surviving mutants
- Decision log for mutation score improvement and weak assertion detection
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for mutation score improvement and weak assertion detection.
2. Produce options and select an approach for mutation score improvement and weak assertion detection.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using mutation testing execution with kill-rate targets.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for mutation score improvement and weak assertion detection are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when surviving mutants expose untested behavior.
- Escalate when accepted risk exceeds team policy thresholds.
