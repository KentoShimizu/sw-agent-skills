---
name: testing-regression-strategy
description: Specialized workflow for regression suite curation and risk-based test selection. Use when designing verification strategy and evidence at this test level; do not use for observability ownership or release scheduling policy.
---

# Testing Regression Strategy

## Trigger Boundary
- Use when verification strategy or release confidence evidence must be designed.
- Do not use for production observability ownership; use `observability-*`.
- Do not use for architecture topology selection.

## Goal
Build sufficient verification evidence to prevent regressions.

## Inputs
- Change scope and risk profile
- Domain evidence for regression suite curation and risk-based test selection
- Operational, compliance, and rollout constraints

## Outputs
- Regression selection policy with impact mapping
- Decision log for regression suite curation and risk-based test selection
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for regression suite curation and risk-based test selection.
2. Produce options and select an approach for regression suite curation and risk-based test selection.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using change-impact to regression coverage traceability.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for regression suite curation and risk-based test selection are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when high-risk change areas are absent from regression gates.
- Escalate when accepted risk exceeds team policy thresholds.
