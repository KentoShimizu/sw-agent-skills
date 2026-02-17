---
name: testing-bdd
description: "Behavior-driven scenario design for shared business language and executable acceptance evidence. Use when teams must align on Given-When-Then scenarios before implementation sign-off or release; do not use for performance benchmarking or deployment policy design."
---

# Testing BDD

## Overview
Use this skill to encode requirement intent as executable behavior scenarios that product, QA, and engineering can all review.

## Scope Boundaries
- Use when behavior semantics need alignment across stakeholders before or during implementation.
- Typical requests:
  - `Turn ambiguous requirements into Given-When-Then scenarios.`
  - `Align PO, QA, and engineering on acceptance behavior.`
  - `Define executable acceptance evidence before release.`
- Do not use when:
  - The primary task is load/performance benchmark design (`performance-*`).
  - The task is operational monitoring/alert policy (`observability-*`).

## Inputs
- Requirement candidates and acceptance concerns
- Domain language and business rules
- Existing test policy and release constraints

## Outputs
- Scenario suite in Given-When-Then format with requirement mapping
- Decision record describing scenario strategy and assumptions
- Verification checklist with pass/fail signals

## Workflow
1. Clarify behavior decisions and non-negotiable constraints.
2. Model happy-path, alternate, and failure behavior in ubiquitous language.
3. Compare scenario granularity options and choose one with rationale.
4. Make scenarios executable and traceable to acceptance decisions.
5. Publish residual risks and unresolved semantic disputes.

## Quality Gates
- Scenarios are understandable by non-engineering stakeholders.
- Acceptance semantics are explicit and testable.
- Assumptions and confidence are documented.
- Evidence is reproducible and linked to requirements.

## Failure Handling
- Stop when critical behavior cannot be expressed unambiguously.
- Escalate when stakeholder interpretations remain incompatible.

## Bundled Resources
- `references/trigger-and-examples.md`: trigger patterns, anti-patterns, and deliverable expectations.
