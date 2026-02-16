---
name: interaction-design
description: "Interaction design workflow for defining user flows, state transitions, and feedback behaviors for key product tasks. Trigger when user journeys require explicit interaction rules (state changes, validation feedback, error recovery, empty/loading behavior) before UI implementation; do not use for backend data-model or deployment pipeline decisions."
---

# Interaction Design

## Trigger Boundary
- Use when user flow behavior, transitions, or state logic is unclear.
- Do not use for high-level navigation hierarchy; use `information-architecture`.
- Do not use for aesthetic styling decisions only; use `visual-design`.

## Goal
Define predictable and accessible interaction behavior across core flows.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.
- Use `references/engineering-judgment-defaults.md` for default decision scoring, risk gating, uncertainty handling, and output structure.

## Inputs
- User tasks and business-critical journeys
- Existing flow issues and support signals
- Platform interaction constraints

## Outputs
- Flow specifications with project-defined IDs (example: `UX-FLW-*` when no existing policy is available)
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

## Engineering Judgment Application
1. Generate at least two plausible options before recommending one.
2. Evaluate options using project-defined criteria; if missing, use defaults in `references/engineering-judgment-defaults.md`.
3. Record assumptions, unknowns, confidence, and key trade-offs in the final output.

## Failure Handling
- Stop when flow goals or state boundaries are ambiguous.
- Escalate when critical error states are undefined.
