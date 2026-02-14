---
name: requirement-prioritization
description: Release planning ranker for already-defined requirements. Use only when `REQ-*` items are finalized and Codex must produce a dependency-aware priority order and release cut line; do not use for requirement discovery.
---

# Requirement Prioritization

## Trigger Boundary
- Use when canonical `REQ-*` items exist and release sequencing is needed.
- Do not use before baseline definition; use `requirements-definition` first.
- Do not use for implementation decomposition; use `user-story-writing`.

## Goal
Produce a defensible and reproducible priority order under capacity constraints.

## Shared Requirements Contract (Canonical)
- Use `../requirements-definition/references/requirements-governance-contract.md` as the single schema and gate source.
- Track requirements workflow artifacts with `RQM-*` IDs.
- Run machine validation: `python3 ../requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Approved `REQ-*` backlog
- Effort and dependency estimates
- `RSK-*` risk scores and mandatory compliance constraints
- Capacity and release window

## Outputs
- Ranked backlog with rationale
- Release cut line and deferred set
- Dependency-feasible implementation order

## Workflow
1. Freeze scoring dimensions and weighting before ranking.
2. Score each `REQ-*` using value, urgency, effort, and risk reduction.
3. Apply dependency constraints to enforce executable sequence.
4. Force mandatory compliance items above discretionary items.
5. Publish ranked list with rationale and deferred-item triggers.

## Quality Gates
- Priority decisions are reproducible from documented rules.
- Dependency violations are absent.
- Compliance-blocking requirements are never deferred without escalation.
- Ranking references source IDs and risk IDs where applicable.

## Failure Handling
- Re-score when assumptions or capacity inputs change.
- Stop approval when mandatory legal or security requirements are deprioritized.
