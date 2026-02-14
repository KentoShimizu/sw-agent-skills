---
name: algorithm-complexity-analysis
description: Specialized workflow for time and space complexity analysis for candidate approaches. Use when implementation risk depends on algorithm correctness, complexity, or state-coordination tradeoffs; do not use for persistence schema design or deployment topology choices.
---

# Algorithm Complexity Analysis

## Trigger Boundary
- Use when algorithmic correctness or complexity drives implementation risk.
- Do not use for persistence-schema decisions; use `db-*`.
- Do not use for runtime deployment topology; use `deployment-*` or `kubernetes-*`.

## Goal
Deliver correct and efficient computational designs with clear tradeoffs.

## Inputs
- Change scope and risk profile
- Domain evidence for time and space complexity analysis for candidate approaches
- Operational, compliance, and rollout constraints

## Outputs
- Complexity analysis report with worst-case bounds
- Decision log for time and space complexity analysis for candidate approaches
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for time and space complexity analysis for candidate approaches.
2. Produce options and select an approach for time and space complexity analysis for candidate approaches.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using input-growth simulation against complexity assumptions.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for time and space complexity analysis for candidate approaches are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when selected approach cannot meet complexity constraints.
- Escalate when accepted risk exceeds team policy thresholds.
