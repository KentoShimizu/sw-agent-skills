---
name: algorithm-design
description: Specialized workflow for problem decomposition and algorithmic strategy selection. Trigger when a task needs algorithm choice or decomposition and correctness/complexity tradeoffs are still unclear, whether the input is a vague outcome request or a concrete implementation directive; do not use for persistence schema design or deployment topology choices.
---

# Algorithm Design

## Trigger Boundary
- Use when algorithmic correctness or complexity drives implementation risk.
- Do not use for persistence-schema decisions; use `db-*`.
- Do not use for runtime deployment topology; use `deployment-*` or `kubernetes-*`.

## Goal
Deliver correct and efficient computational designs with clear tradeoffs.

## Inputs
- Change scope and risk profile
- Domain evidence for problem decomposition and algorithmic strategy selection
- Operational, compliance, and rollout constraints

## Outputs
- Algorithm design decision with trade-off matrix
- Decision log for problem decomposition and algorithmic strategy selection
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for problem decomposition and algorithmic strategy selection.
2. Produce options and select an approach for problem decomposition and algorithmic strategy selection.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using correctness proof sketch and benchmark sanity checks.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for problem decomposition and algorithmic strategy selection are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when algorithm choice lacks correctness reasoning or trade-off evidence.
- Escalate when accepted risk exceeds team policy thresholds.
