---
name: requirement-elicitation
description: "Requirement elicitation workflow for collecting, reconciling, and structuring evidence before requirement baseline writing. Use when requirement inputs are incomplete and teams need high-confidence evidence gathering; do not use for final canonical requirement synthesis."
---

# Requirement Elicitation

## Overview
Use this skill to collect requirement evidence with traceability, confidence, and contradiction visibility.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Evidence strength rules:
  - `references/evidence-strength-rules.md`

## Templates And Assets
- Evidence intake template:
  - `assets/evidence-intake-template.csv`
- Clarification question log:
  - `assets/clarification-question-log-template.md`

## Inputs To Gather
- Stakeholder map and decision owners.
- Existing docs/tickets/incidents/analytics.
- Known unknowns and contested assumptions.

## Deliverables
- Structured evidence set with confidence scores.
- Clarification question backlog with owners.
- Requirement candidate seeds for baseline synthesis.

## Workflow
1. Capture evidence in `assets/evidence-intake-template.csv`.
2. Apply confidence/contradiction rules from `references/evidence-strength-rules.md`.
3. Separate evidence, assumptions, and unknowns.
4. Track unresolved questions in `assets/clarification-question-log-template.md`.
5. Publish elicitation package for requirements-definition.

## Quality Standard
- Evidence has source traceability and confidence labels.
- Contradictions are explicit and unresolved items are owned.
- Inputs are sufficient for canonical baseline synthesis.

## Failure Conditions
- Stop when evidence depends on weak single-source claims.
- Stop when critical unknowns have no owner/due date.
- Escalate when legal/privacy constraints are unclear.
