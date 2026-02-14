---
name: design-review
description: "Structured design review workflow for validating UX quality, implementation readiness, and governance compliance before delivery. Use when UX, interaction, visual, or design-governance artifacts are the primary deliverable; do not use for backend data-model or deployment pipeline decisions."
---

# Design Review

## Trigger Boundary
- Use when a design artifact is ready for formal review before implementation or release.
- Do not use for creating principles from scratch; use `design-principles`.
- Do not use for designing accessibility remediation plans; use `accessibility-design`.

## Goal
Identify design risks early and provide concrete, reviewable fixes.

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the single schema and gate source.
- Validate IDs, lifecycle states, and approval requirements against this contract.
- Run machine validation: `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Design artifact and review scope
- Relevant flow IDs and spec IDs
- Accessibility and localization constraints

## Outputs
- `DREV-*` findings list with severity and owner
- Approval decision with blockers and conditions
- Follow-up action log with due dates

## Workflow
1. Confirm review scope and acceptance criteria.
2. Check usability, consistency, and implementation feasibility.
3. Verify accessibility gate status using existing `A11Y-CHK-*` results.
4. Record findings with severity, owner, and remediation path.
5. Conclude approval or rejection with explicit rationale.

## Quality Gates
- Findings are evidence-based and reproducible.
- Blockers are clearly separated from improvements.
- Required approvers are assigned and traceable.
- Contract validation passes for IDs and gates.

## Failure Handling
- Stop review when scope or artifact is ambiguous.
- Stop release recommendation when blocker findings remain unresolved.
