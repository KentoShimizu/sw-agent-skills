---
name: design-qa-implementation-parity
description: "UI parity verification workflow between design specs and implemented interfaces. Use when UX, interaction, visual, or design-governance artifacts are the primary deliverable; do not use for backend data-model or deployment pipeline decisions."
---

# Design Qa Implementation Parity

## Trigger Boundary
- Use when implemented UI must be validated against approved design artifacts.
- Do not use for creating new visual specifications; use `visual-design`.
- Do not use for accessibility remediation planning; use `accessibility-design`.

## Goal
Prevent design-to-implementation drift with objective parity evidence.

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the single schema and gate source.
- Track parity review artifacts with `DREV-*` IDs.
- Run machine validation: `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Approved design artifacts and version identifiers
- Implemented UI build or staging environment
- Scope of screens, states, and variants under validation

## Outputs
- `DREV-*` parity report with mismatch severity and ownership
- Screen/state-level pass-fail checklist
- Remediation actions with priority and due date

## Workflow
1. Lock design and implementation versions before comparison.
2. Validate layout, spacing, typography, and component states.
3. Validate interaction behavior and transition timing.
4. Record mismatches with reproducible evidence.
5. Publish parity decision and remediation backlog with contract validation evidence.

## Quality Gates
- Critical user flows have zero unresolved blocker mismatches.
- State coverage includes loading, empty, error, and success states.
- Findings are reproducible across reviewers.
- Ownership is assigned for every mismatch.
- Contract validation passes for `DREV-*` artifact manifests.
- When `checks.user_facing_change` is `true`, Privacy Reviewer approval and privacy evidence are present.

## Failure Handling
- Stop parity sign-off when source versions are not locked.
- Escalate when blocker mismatches remain unresolved.
