---
name: responsive-layout-design
description: "Responsive layout design workflow for defining adaptive structure and component behavior across screen sizes and device contexts. Trigger when UI layouts must adapt across breakpoints/devices and teams need explicit responsive behavior rules before implementation; do not use for backend data-model or deployment pipeline decisions."
---

# Responsive Layout Design

## Trigger Boundary
- Use when layouts break or become unusable across device sizes.
- Do not use for visual token definition; use `design-tokens`.
- Do not use for end-to-end handoff packaging; use `figma-handoff`.

## Goal
Ensure layouts remain usable, readable, and consistent across screen contexts.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.

## Inputs
- Breakpoint requirements and device usage data
- Current layout failures and overflow risks
- Content constraints and localization expansion risk

## Outputs
- Responsive rule set with project-defined IDs (example: `RESP-RUL-*` when no existing policy is available)
- Breakpoint behavior and component adaptation specs
- Risk list for overflow, truncation, and interaction issues

## Workflow
1. Define breakpoint model and layout priorities.
2. Specify component adaptation per breakpoint.
3. Validate text expansion and localization stress cases.
4. Define interaction affordance changes for touch and pointer contexts.
5. Document regression checkpoints for critical screens.

6. Compare at least two feasible approaches and explain why one is preferred.
7. Record key assumptions, unknowns, confidence, and rollback considerations.

## Quality Gates
- Core tasks remain usable at all supported breakpoints.
- Overflow and truncation are controlled for long localized strings.
- Interaction targets remain accessible on touch devices.
- Responsive rules are traceable and non-conflicting.

- Decision rationale and trade-offs are explicit.
- Assumptions, unknowns, and confidence are explicitly documented.

## Failure Handling
- Stop when breakpoints are chosen without user/device evidence.
- Escalate when critical flows fail on supported viewport ranges.
