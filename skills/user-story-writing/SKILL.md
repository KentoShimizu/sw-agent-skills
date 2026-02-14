---
name: user-story-writing
description: Implementation-slice authoring for prioritized requirements. Use only when `REQ-*` priorities are approved and Codex must convert them into sprint-ready stories with explicit value and testability; do not use for requirement discovery.
---

# User Story Writing

## Trigger Boundary
- Use when requirements are prioritized and delivery slicing is required.
- Do not use to define canonical requirements; use `requirements-definition`.
- Do not use to assign release ranking; use `requirement-prioritization`.

## Goal
Create sprint-ready stories with explicit user value and clear completion conditions.

## Shared Requirements Contract (Canonical)
- Use `../requirements-definition/references/requirements-governance-contract.md` as the single schema and gate source.
- Track requirements workflow artifacts with `RQM-*` IDs.
- Run machine validation: `python3 ../requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Prioritized `REQ-*` backlog
- Relevant `AC-*`, `NFR-*`, and dependency context
- Team capacity and planning horizon

## Outputs
- Story set linked to `REQ-*` IDs
- Story-level acceptance mapping and constraints
- Blockers, assumptions, and dependency notes

## Workflow
1. Derive small vertical slices from prioritized requirements.
2. Write actor-need-value statement for each story.
3. Link each story to one or more `REQ-*` and `AC-*` IDs.
4. Add non-functional and compliance constraints explicitly.
5. Split oversized stories until estimable in one cycle.

## Quality Gates
- Every story has clear value and linked requirement IDs.
- Story scope fits one delivery cycle.
- Story completion criteria are testable.
- Compliance-related stories are not optional when legally required.

## Failure Handling
- Reject stories without requirement linkage.
- Stop planning when critical dependencies are unresolved.
