---
name: acceptance-criteria-design
description: Pass/fail criteria authoring for approved requirements. Trigger when approved `REQ-*` items need executable acceptance checks for implementation handoff, QA validation, or release sign-off, whether the request starts as a high-level goal or a detailed spec; do not use for requirement discovery or prioritization.
---

# Acceptance Criteria Design

## Trigger Boundary
- Use when requirement wording is approved and implementation readiness is needed.
- Do not use to define requirement intent; use `requirements-definition`.
- Do not use to split sprint work; use `user-story-writing`.

## Goal
Translate stable requirements into binary, testable acceptance conditions.

## Shared Requirements Contract (Canonical)
- Use `../requirements-definition/references/requirements-governance-contract.md` as the primary reference for recommended structure.
- Track requirements workflow artifacts with project-defined IDs (for example `RQM-*`).
- Optional consistency check (only if your repository enforces manifest validation): `python3 ../requirements-definition/scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Approved `REQ-*` and relevant `NFR-*`
- Boundary conditions and known failure paths
- Test environment capabilities

## Outputs
- `AC-*` conditions mapped to `REQ-*`
- Positive, negative, and boundary test scenarios
- Traceability table from requirement to verification method

## Workflow
1. Write behavior-focused pass/fail statements per requirement.
2. Assign `AC-*` IDs and map each to one `REQ-*` ID.
3. Include normal flow, edge conditions, and failure outcomes.
4. Specify setup, inputs, and expected observable results.
5. Review for ambiguity, overlap, and missing failure coverage.

## Quality Gates
- Every `AC-*` is independently verifiable.
- Coverage includes negative and boundary paths.
- Criteria map to requirement and NFR obligations.
- Compliance conditions are testable and explicit.

## Failure Handling
- Reject criteria that cannot be executed in available environments.
- Stop when requirement ambiguity prevents binary criteria.
