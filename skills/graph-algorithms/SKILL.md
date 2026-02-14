---
name: graph-algorithms
description: Specialized workflow for graph modeling and traversal/path algorithm selection. Use when implementation risk depends on algorithm correctness, complexity, or state-coordination tradeoffs; do not use for persistence schema design or deployment topology choices.
---

# Graph Algorithms

## Trigger Boundary
- Use when algorithmic correctness or complexity drives implementation risk.
- Do not use for persistence-schema decisions; use `db-*`.
- Do not use for runtime deployment topology; use `deployment-*` or `kubernetes-*`.

## Goal
Deliver correct and efficient computational designs with clear tradeoffs.

## Inputs
- Change scope and risk profile
- Domain evidence for graph modeling and traversal/path algorithm selection
- Operational, compliance, and rollout constraints

## Outputs
- Graph algorithm choice rationale
- Decision log for graph modeling and traversal/path algorithm selection
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for graph modeling and traversal/path algorithm selection.
2. Produce options and select an approach for graph modeling and traversal/path algorithm selection.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using graph property tests and path correctness validation.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for graph modeling and traversal/path algorithm selection are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when graph representation or algorithm choice mismatches problem constraints.
- Escalate when accepted risk exceeds team policy thresholds.
