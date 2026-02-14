---
name: data-structures
description: Specialized workflow for data structure selection by access pattern and mutation profile. Use when implementation risk depends on algorithm correctness, complexity, or state-coordination tradeoffs; do not use for persistence schema design or deployment topology choices.
---

# Data Structures

## Trigger Boundary
- Use when algorithmic correctness or complexity drives implementation risk.
- Do not use for persistence-schema decisions; use `db-*`.
- Do not use for runtime deployment topology; use `deployment-*` or `kubernetes-*`.

## Goal
Deliver correct and efficient computational designs with clear tradeoffs.

## Inputs
- Change scope and risk profile
- Domain evidence for data structure selection by access pattern and mutation profile
- Operational, compliance, and rollout constraints

## Outputs
- Data structure decision matrix
- Decision log for data structure selection by access pattern and mutation profile
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for data structure selection by access pattern and mutation profile.
2. Produce options and select an approach for data structure selection by access pattern and mutation profile.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using operation-cost benchmark for target workloads.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for data structure selection by access pattern and mutation profile are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when chosen structure does not fit dominant access patterns.
- Escalate when accepted risk exceeds team policy thresholds.
