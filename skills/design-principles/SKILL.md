---
name: design-principles
description: "Design principle definition workflow for establishing stable UX guardrails before visual or component-level work. Trigger when product or UX direction is ambiguous and teams need explicit design principles and decision guardrails before detailed screens or components are produced; do not use for backend data-model or deployment pipeline decisions."
---

# Design Principles

## Trigger Boundary
- Use when team-level design principles are missing or inconsistent.
- Do not use for component inventory design; use `design-system-foundations`.
- Do not use for visual polish-only tasks; use `visual-design`.

## Goal
Define clear principles that guide interaction, visual, and content decisions.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- Use `references/design-governance-contract.md` only as an optional default policy when no existing project rules are available.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.
- Use `references/engineering-judgment-defaults.md` for default decision scoring, risk gating, uncertainty handling, and output structure.
- Optional validator for governed mode only: `python3 scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Product strategy and user outcomes
- Existing design inconsistencies and pain points
- Accessibility and localization requirements

## Outputs
- Principle catalog with project-defined IDs (example: `DSN-PRN-*` when no existing policy is available)
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

## Engineering Judgment Application
1. Generate at least two plausible options before recommending one.
2. Evaluate options using project-defined criteria; if missing, use defaults in `references/engineering-judgment-defaults.md`.
3. Record assumptions, unknowns, confidence, and key trade-offs in the final output.

## Failure Handling
- Stop when principles are abstract slogans without test criteria.
- Escalate when principles conflict with mandatory compliance constraints.
