---
name: design-review
description: "Structured design review workflow for validating UX quality, implementation readiness, and governance compliance before delivery. Trigger when a design artifact needs formal review for usability, accessibility, consistency, and implementation readiness before handoff or approval; do not use for backend data-model or deployment pipeline decisions."
---

# Design Review

## Trigger Boundary
- Use when a design artifact is ready for formal review before implementation or release.
- Do not use for creating principles from scratch; use `design-principles`.
- Do not use for designing accessibility remediation plans; use `accessibility-design`.

## Goal
Identify design risks early and provide concrete, reviewable fixes.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.

## Inputs
- Design artifact and review scope
- Relevant flow IDs and spec IDs
- Accessibility and localization constraints

## Outputs
- Findings list with project-defined IDs (example: `DREV-*` when no existing policy is available), severity, and owner
- Approval decision with blockers and conditions
- Follow-up action log with due dates

## Workflow
1. Confirm review scope and acceptance criteria.
2. Check usability, consistency, and implementation feasibility.
3. Verify accessibility gate status using existing results under project-defined IDs (for example `A11Y-CHK-*`).
4. Record findings with severity, owner, and remediation path.
5. Conclude approval or rejection with explicit rationale.

6. Compare at least two feasible approaches and explain why one is preferred.
7. Record key assumptions, unknowns, confidence, and rollback considerations.

## Quality Gates
- Findings are evidence-based and reproducible.
- Blockers are clearly separated from improvements.
- Project-required approvers are assigned and traceable.

- Decision rationale and trade-offs are explicit.
- Assumptions, unknowns, and confidence are explicitly documented.

## Failure Handling
- Stop review when scope or artifact is ambiguous.
- Stop release recommendation when blocker findings remain unresolved.
