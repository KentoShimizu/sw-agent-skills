---
name: visual-design
description: "Visual design workflow for defining coherent color, typography, spacing, and composition systems. Use when teams need implementation-ready visual direction for product surfaces; do not use for backend architecture, data modeling, or deployment policy."
---

# Visual Design

## Overview
Use this skill to create visual systems that are consistent, accessible, and implementation-ready.

## Scope Boundaries
- Product surfaces need a coherent visual language or redesign.
- Teams must align brand expression with usability and accessibility constraints.
- Implementation teams need explicit visual rules rather than isolated mockups.

## Templates And Assets
- Visual spec template:
  - `assets/visual-spec-template.md`

## Inputs To Gather
- Brand and product positioning goals.
- Existing UI inconsistencies and readability issues.
- Accessibility requirements (contrast, legibility, scaling).
- Platform constraints (web/mobile/native, theming model).

## Deliverables
- Visual specification covering color roles, typography, spacing, and hierarchy.
- Component-level visual usage guidelines and anti-pattern notes.
- Accessibility validation notes for key visual decisions.

## Workflow
1. Define hierarchy goals by task criticality and information density.
2. Build typography and spacing scales with explicit rationale.
3. Define semantic color roles and permitted usage boundaries.
4. Apply rules to representative screens and states.
5. Validate readability/contrast and adjust conflicting decisions.
6. Deliver implementation-ready specs and examples.

## Quality Standard
- Visual system supports content hierarchy and task focus.
- Rules are reusable across pages and components.
- Accessibility checks are integrated into visual decisions.
- Spec quality is high enough to reduce interpretation drift in implementation.

## Failure Conditions
- Stop when specs rely on one-off exceptions as default behavior.
- Stop when contrast or legibility fails baseline requirements.
- Escalate when brand constraints conflict with accessibility requirements.
