---
name: accessibility-design
description: "Accessibility-first design workflow for ensuring inclusive interaction, semantics, and visual clarity across product experiences. Trigger when screens, flows, or components need accessibility decisions (semantics, keyboard behavior, contrast, assistive-tech behavior) before implementation or design sign-off; do not use for backend data-model or deployment pipeline decisions."
---

# Accessibility Design

## Trigger Boundary
- Use when accessibility requirements must be designed, audited, or remediated.
- Do not use for final release approval decisions; use `design-review`.
- Do not use for global navigation taxonomy changes; use `information-architecture`.

## Goal
Guarantee inclusive user experience through proactive accessibility design.

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the primary reference for recommended structure.
- Track checks with project-defined IDs (for example `A11Y-CHK-*`).
- Optional consistency check (only if your repository enforces manifest validation): `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- User journeys and critical UI surfaces
- Known accessibility defects and constraints
- Assistive technology support targets

## Outputs
- Accessibility checklist and findings with project-defined IDs (for example `A11Y-CHK-*`)
- Remediation plan with owners and priorities
- Verification criteria for release gating

## Workflow
1. Define applicable accessibility requirements per surface.
2. Audit navigation, semantics, contrast, and feedback patterns.
3. Document defects with severity and affected user impact.
4. Design remediation and verify feasibility with engineering.
5. Re-validate and publish results under project-defined IDs (for example `A11Y-CHK-*`) for review consumption.

## Quality Gates
- Keyboard, focus, and semantics meet baseline requirements.
- Contrast and readability pass target thresholds.
- Critical user flows are assistive-technology compatible.
- Blockers are resolved or explicitly escalated with owner and due date.

## Failure Handling
- Stop when critical accessibility checks are skipped.
- Escalate when remediation ownership or timeline is missing.
