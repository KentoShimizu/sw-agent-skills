---
name: design-principles
description: "Design principle definition workflow for establishing stable UX guardrails before visual or component-level work. Use when UX, interaction, visual, or design-governance artifacts are the primary deliverable; do not use for backend data-model or deployment pipeline decisions."
---

# Design Principles

## Trigger Boundary
- Use when team-level design principles are missing or inconsistent.
- Do not use for component inventory design; use `design-system-foundations`.
- Do not use for visual polish-only tasks; use `visual-design`.

## Goal
Define clear principles that guide interaction, visual, and content decisions.

## Shared Design Contract (Canonical)
- Use `references/design-governance-contract.md` as the single schema and gate source.
- Validate principle IDs as `DSN-PRN-*` and keep append-only history.
- Run machine validation: `python3 scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Product strategy and user outcomes
- Existing design inconsistencies and pain points
- Accessibility and localization requirements

## Outputs
- Principle catalog with `DSN-PRN-*` IDs
- Principle rationale and anti-pattern examples
- Review checklist aligned to principles

## Workflow
1. Convert user and business outcomes into principle candidates.
2. Define principles as actionable and testable statements.
3. Attach anti-pattern examples for each principle.
4. Validate principles against accessibility and localization gates.
5. Publish principle set with ownership and revision policy.

## Quality Gates
- Each principle is specific and reviewable.
- Principle set has no unresolved contradiction.
- Accessibility and localization constraints are represented.
- Review checklist maps directly to principles.

## Failure Handling
- Stop when principles are abstract slogans without test criteria.
- Escalate when principles conflict with mandatory compliance constraints.
