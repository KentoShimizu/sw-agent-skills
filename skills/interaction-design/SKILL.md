---
name: interaction-design
description: "Interaction design workflow for user flows, state transitions, and feedback behavior across key tasks. Use when user journeys require explicit interaction rules (state changes, validation feedback, error recovery, empty/loading behavior) before UI implementation; do not use for backend data-model or deployment pipeline decisions."
---

# Interaction Design

## Overview
Use this skill to define clear, accessible interaction behavior for primary and edge-case user journeys.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Interaction feedback principles:
  - `references/interaction-feedback-principles.md`

## Templates And Assets
- Flow spec template:
  - `assets/flow-spec-template.md`
- State transition template:
  - `assets/state-transition-template.csv`
- Edge-case checklist:
  - `assets/interaction-edge-case-checklist.md`

## Inputs To Gather
- User tasks and business-critical journeys.
- Existing flow issues and support signals.
- Platform interaction constraints.
- Error/retry expectations and accessibility constraints.

## Deliverables
- Flow specifications with start/end/alternate/failure paths.
- State transition and feedback behavior map.
- Explicit edge-case behavior definitions.
- Accessibility-ready interaction checkpoints.

## Workflow
1. Define flow boundaries in `assets/flow-spec-template.md`.
2. Map state transitions in `assets/state-transition-template.csv`.
3. Apply feedback principles from `references/interaction-feedback-principles.md`.
4. Cover failure and edge behavior via `assets/interaction-edge-case-checklist.md`.
5. Validate consistency and accessibility across similar patterns.

## Quality Standard
- Critical flows have explicit state and transition models.
- Failure states are actionable and recovery paths are clear.
- Interaction behavior is consistent for similar intents.
- Keyboard/focus behavior supports accessibility requirements.

## Failure Conditions
- Stop when flow goals or state boundaries are ambiguous.
- Stop when edge-case behavior is undefined for critical tasks.
- Escalate when interaction rules conflict with accessibility requirements.
