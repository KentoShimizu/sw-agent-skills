---
name: requirements-definition
description: Canonical requirement baseline design after evidence collection is complete. Use only when elicitation artifacts already exist and Codex must synthesize them into a traceable requirement specification; do not use for prioritization or implementation slicing.
---

# Requirements Definition

## Trigger Boundary
- Use when interview and research evidence already exists and a canonical requirement baseline is missing.
- Do not use for ranking backlog items; use `requirement-prioritization`.
- Do not use for sprint-sized implementation items; use `user-story-writing`.

## Goal
Define a testable requirement baseline aligned with business outcomes and decision history.

## Shared Requirements Contract (Canonical)
- Use `references/requirements-governance-contract.md` as the single schema and gate source.
- Track requirements workflow artifacts with `RQM-*` IDs.
- Run machine validation: `python3 scripts/validate_requirements_contract.py --manifest <path/to/manifest.json>`.
- Reference valid samples:
  - `references/samples/rqm-def-manifest.valid.json`
  - `references/samples/rqm-cmp-manifest.valid.json`
- Use field mapping guide:
  - `references/manifest-field-guide.md`

## Inputs
- Product goals, constraints, and timeline
- Elicitation outputs with `INT-*`, `UR-*`, and `EVD-*` references
- Existing architecture and operational constraints

## Outputs
- Canonical requirement set with `REQ-*` IDs
- Scope and out-of-scope decisions with rationale
- Traceability links from goals to requirements and evidence
- Open decision log with owners and due dates

## Workflow
1. Convert validated evidence into atomic requirement statements.
2. Assign `REQ-*` IDs and map each to supporting evidence IDs.
3. Separate functional requirements and candidate NFR placeholders.
4. Mark assumptions explicitly and escalate unresolved contradictions.
5. Confirm owner, validation method, and decision deadline per requirement.

## Quality Gates
- Each requirement is atomic, testable, and source-traceable.
- Every requirement links to at least one evidence ID.
- Scope exclusions are explicit and reviewable.
- Compliance constraints are represented as requirements when mandatory.

## Failure Handling
- Stop when conflicting requirements lack decision authority.
- Stop when personal data appears without lawful basis or masking rules.
