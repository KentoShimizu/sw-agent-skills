---
name: dynamic-programming
description: Specialized workflow for state definition, transition design, and memoization strategy. Use when implementation risk depends on algorithm correctness, complexity, or state-coordination tradeoffs; do not use for persistence schema design or deployment topology choices.
---

# Dynamic Programming

## Trigger Boundary
- Use when algorithmic correctness or complexity drives implementation risk.
- Do not use for persistence-schema decisions; use `db-*`.
- Do not use for runtime deployment topology; use `deployment-*` or `kubernetes-*`.

## Goal
Deliver correct and efficient computational designs with clear tradeoffs.

## Inputs
- Change scope and risk profile
- Domain evidence for state definition, transition design, and memoization strategy
- Operational, compliance, and rollout constraints

## Outputs
- DP state-transition specification
- Decision log for state definition, transition design, and memoization strategy
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for state definition, transition design, and memoization strategy.
2. Produce options and select an approach for state definition, transition design, and memoization strategy.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using state coverage and recurrence correctness checks.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for state definition, transition design, and memoization strategy are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when state transitions are incomplete or violate recurrence assumptions.
- Escalate when accepted risk exceeds team policy thresholds.
