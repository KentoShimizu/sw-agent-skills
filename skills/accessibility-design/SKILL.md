---
name: accessibility-design
description: "Design accessibility requirements for product flows and components, including semantics, keyboard/focus behavior, contrast, error feedback, and assistive-technology behavior. Use when UI accessibility decisions must be specified before implementation or design sign-off; do not use for backend data modeling or deployment pipeline decisions."
---

# Accessibility Design

## Overview
Use this skill to define concrete accessibility behavior so implemented UI is usable by keyboard users, screen-reader users, and users with visual/cognitive constraints.

## Inputs To Gather
- Critical user journeys and high-impact screens/components.
- Current UX constraints and known accessibility defects.
- Target platforms and assistive technologies.
- Applicable policy/baseline level required by the project.

## Deliverables
- Accessibility specification per flow/component.
- Defect/remediation list with severity and user impact.
- Verification checklist for design review and implementation QA.
- Risk list for unresolved accessibility gaps.

## Quality Standard
- Semantic structure and accessible names are explicit for interactive elements.
- Keyboard navigation order, focus visibility, and focus trap/escape behavior are defined.
- Error, loading, empty, and success states provide perceivable and understandable feedback.
- Color contrast and non-color affordances are specified for critical interactions.
- Screen-reader announcements and dynamic-content updates are specified where state changes occur.
- Requirements are testable with manual and automated checks.

## Workflow
1. Identify critical journeys and accessibility-sensitive interactions.
2. Specify semantic roles, labels, and heading/landmark structure.
3. Define keyboard and focus behavior for each interactive state.
4. Define visual readability and feedback behavior for all states.
5. Define assistive-technology behavior for dynamic updates and errors.
6. Produce verification checklist and prioritized remediation plan.

## Failure Conditions
- Stop when critical journeys are not covered by accessibility requirements.
- Stop when requirements are not testable in target environments.
- Escalate when unresolved critical issues block safe release.
