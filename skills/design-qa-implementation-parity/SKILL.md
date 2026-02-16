---
name: design-qa-implementation-parity
description: "UI parity verification workflow between design specs and implemented interfaces. Trigger when implemented UI must be compared against approved design specs and mismatches need structured severity judgment plus fix guidance before release or sign-off; do not use for backend data-model or deployment pipeline decisions."
---

# Design Qa Implementation Parity

## Trigger Boundary
- Use when implemented UI must be validated against approved design artifacts.
- Do not use for creating new visual specifications; use `visual-design`.
- Do not use for accessibility remediation planning; use `accessibility-design`.

## Goal
Prevent design-to-implementation drift with objective parity evidence.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.

## Inputs
- Approved design artifacts and version identifiers
- Implemented UI build or staging environment
- Scope of screens, states, and variants under validation

## Outputs
- Parity report with project-defined IDs (example: `DPAR-*` when no existing policy is available), mismatch severity, and ownership
- Screen/state-level pass-fail checklist
- Remediation actions with priority and due date

## Workflow
1. Lock design and implementation versions before comparison.
2. Validate layout, spacing, typography, and component states.
3. Validate interaction behavior and transition timing.
4. Record mismatches with reproducible evidence.
5. Publish parity decision and remediation backlog with contract validation evidence.

6. Compare at least two feasible approaches and explain why one is preferred.
7. Record key assumptions, unknowns, confidence, and rollback considerations.

## Quality Gates
- Critical user flows have zero unresolved blocker mismatches.
- State coverage includes loading, empty, error, and success states.
- Findings are reproducible across reviewers.
- Ownership is assigned for every mismatch.
- Policy-required approvers and privacy controls are explicitly recorded.

- Decision rationale and trade-offs are explicit.
- Assumptions, unknowns, and confidence are explicitly documented.

## Failure Handling
- Stop parity sign-off when source versions are not locked.
- Escalate when blocker mismatches remain unresolved.
