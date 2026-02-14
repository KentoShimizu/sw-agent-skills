---
name: testing-bdd
description: Specialized workflow for behavior-driven scenarios and ubiquitous language alignment. Use when designing verification strategy and evidence at this test level; do not use for observability ownership or release scheduling policy.
---

# Testing Bdd

## Trigger Boundary
- Use when verification strategy or release confidence evidence must be designed.
- Do not use for production observability ownership; use `observability-*`.
- Do not use for architecture topology selection.

## Goal
Build sufficient verification evidence to prevent regressions.

## Inputs
- Change scope and risk profile
- Domain evidence for behavior-driven scenarios and ubiquitous language alignment
- Operational, compliance, and rollout constraints

## Outputs
- Given-When-Then scenario suite
- Decision log for behavior-driven scenarios and ubiquitous language alignment
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for behavior-driven scenarios and ubiquitous language alignment.
2. Produce options and select an approach for behavior-driven scenarios and ubiquitous language alignment.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using stakeholder-readable scenario execution evidence.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for behavior-driven scenarios and ubiquitous language alignment are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when critical business behaviors are not captured as executable scenarios.
- Escalate when accepted risk exceeds team policy thresholds.
