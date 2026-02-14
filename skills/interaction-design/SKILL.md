---
name: interaction-design
description: "Interaction design workflow for defining user flows, state transitions, and feedback behaviors for key product tasks. Use when UX, interaction, visual, or design-governance artifacts are the primary deliverable; do not use for backend data-model or deployment pipeline decisions."
---

# Interaction Design

## Trigger Boundary
- Use when user flow behavior, transitions, or state logic is unclear.
- Do not use for high-level navigation hierarchy; use `information-architecture`.
- Do not use for aesthetic styling decisions only; use `visual-design`.

## Goal
Define predictable and accessible interaction behavior across core flows.

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the single schema and gate source.
- Assign flow IDs as `UX-FLW-*`.
- Run machine validation: `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- User tasks and business-critical journeys
- Existing flow issues and support signals
- Platform interaction constraints

## Outputs
- Flow specifications with `UX-FLW-*` IDs
- State transition and feedback behavior map
- Edge-case and failure-state definitions

## Workflow
1. Define start/end conditions for each key flow.
2. Map primary, alternative, and failure paths.
3. Specify state transitions and user feedback timing.
4. Add explicit empty, loading, and error states.
5. Validate keyboard and assistive-technology operability.

## Quality Gates
- Critical flows have explicit state models.
- Failure states are defined and user-actionable.
- Interaction behavior is consistent across similar patterns.
- Accessibility gates pass for keyboard and focus behavior.

## Failure Handling
- Stop when flow goals or state boundaries are ambiguous.
- Escalate when critical error states are undefined.
