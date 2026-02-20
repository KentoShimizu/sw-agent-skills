---
name: responsive-layout-design
description: "Responsive layout design workflow for defining adaptive structure and component behavior across viewport ranges. Use when UI layouts must remain usable and readable across device contexts; do not use for backend data modeling or deployment pipeline decisions."
---

# Responsive Layout Design

## Overview
Use this skill to define responsive behavior that keeps critical workflows usable across supported screen sizes.

## Scope Boundaries
- Layouts break, overflow, or lose usability across devices.
- Teams need explicit breakpoint and adaptation rules before implementation.
- Localization/content growth increases truncation and wrapping risk.

## Templates And Assets
- Responsive rule template:
  - `assets/responsive-rule-template.md`
- Breakpoint test checklist:
  - `assets/breakpoint-test-checklist.md`

## Inputs To Gather
- Device and viewport support matrix.
- Critical tasks and layout priority by context.
- Content constraints including localization expansion risk.
- Interaction modality requirements (touch, pointer, keyboard).

## Deliverables
- Responsive rule set with breakpoint-specific behavior.
- Component adaptation guidance for each viewport range.
- Risk list for overflow, truncation, and interaction regressions.
- Verification checklist for critical screens.

## Workflow
1. Define viewport model and breakpoint rationale.
2. Specify component behavior per breakpoint (reflow, collapse, hide, or transform).
3. Validate text expansion, dynamic data density, and media constraints.
4. Define interaction affordance adjustments by modality.
5. Verify critical workflows at each supported viewport range.
6. Publish responsive rules with ownership and review cadence.

## Quality Standard
- Core tasks remain usable at all supported viewport ranges.
- Overflow and truncation risks are addressed explicitly.
- Interactive targets remain accessible and operable.
- Rules are consistent and do not conflict across breakpoints.

## Failure Conditions
- Stop when breakpoint choices lack user/device evidence.
- Stop when critical workflows fail in supported viewport ranges.
- Escalate when responsive constraints conflict with required functionality.
