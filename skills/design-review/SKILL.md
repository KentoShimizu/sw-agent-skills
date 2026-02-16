---
name: design-review
description: "Run structured design reviews that produce actionable findings and clear approval decisions. Use when a design artifact needs formal review for usability, accessibility, consistency, and implementation readiness before handoff or approval; do not use for backend data-model or deployment pipeline decisions."
---

# Design Review

## Overview
Use this skill to convert subjective design feedback into prioritized, evidence-based decisions that unblock implementation.

## Inputs To Gather
- Review target (screens, flows, interaction states) and intended users.
- Acceptance criteria and non-negotiable constraints.
- Accessibility and localization expectations for in-scope surfaces.
- Delivery timeline and risk tolerance for unresolved issues.

## Deliverables
- Findings list with severity, user impact, engineering impact, and owner.
- Explicit approval decision: approved, conditional approval, or rejected.
- Remediation plan with due dates and verification method.
- Residual risk statement for any deferred non-blocker issues.

## Quick Example
- Blocker: keyboard focus order breaks checkout completion.
- Major: ambiguous copy causes wrong destructive action selection.
- Minor: visual rhythm inconsistency without measurable task impact.
- Decision: reject due to blocker; re-review only affected flow after fix.

## Quality Standard
- Findings are reproducible and linked to concrete evidence.
- Severity reflects impact, not reviewer preference.
- Blockers are separated from improvements and tracked independently.
- Approval decision is auditable and tied to explicit criteria.

## Workflow
1. Confirm review scope, criteria, and decision authority.
2. Evaluate critical user journeys before secondary surfaces.
3. Log findings with impact, severity, and remediation guidance.
4. Resolve or defer issues using explicit risk acceptance rules.
5. Publish final decision and follow-up actions.

## Failure Conditions
- Stop when review scope or acceptance criteria are ambiguous.
- Stop when critical flows cannot be validated end-to-end.
- Escalate when blocker findings remain open near implementation handoff.
