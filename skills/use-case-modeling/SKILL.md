---
name: use-case-modeling
description: Actor-flow modeling for behavior clarification of defined requirements. Trigger when approved requirements need explicit main, alternate, and exception interaction flows across actors/system boundaries to remove behavior ambiguity; do not use for backlog ranking or acceptance test authoring.
---

# Use Case Modeling

## Trigger Boundary
- Use when actor interactions are unclear after requirements are defined.
- Do not use for priority decisions; use `requirement-prioritization`.
- Do not use for executable pass/fail checks; use `acceptance-criteria-design`.

## Goal
Reveal requirement gaps by modeling complete interaction flows.

## Shared Requirements Contract (Canonical)
- Use `../requirements-definition/references/requirements-governance-contract.md` as the primary reference for recommended structure.
- Track requirements workflow artifacts with project-defined IDs (for example `RQM-*`).
- Optional consistency check (only if your repository enforces manifest validation): `python3 ../requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Approved `REQ-*`
- Actor roles, permissions, and boundary definitions
- Business rules and integration constraints

## Outputs
- Use cases with preconditions and postconditions
- Main, alternate, and exception flows
- Gap list linked back to `REQ-*` IDs

## Workflow
1. Define actors and goals with permission boundaries.
2. Draft main success flow from trigger to completion.
3. Add alternate flows for realistic path variation.
4. Add exception flows for failure and recovery.
5. Link discovered gaps to impacted `REQ-*` IDs.

## Quality Gates
- Critical actor goals are covered by at least one use case.
- Alternate and exception paths are explicit.
- Data handling constraints are visible in relevant flows.
- Gaps are traceable and assigned owners.

## Failure Handling
- Rework model when system boundary is ambiguous.
- Stop when policy constraints for exception handling are undefined.
