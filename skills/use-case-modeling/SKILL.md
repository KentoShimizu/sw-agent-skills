---
name: use-case-modeling
description: "Use case modeling workflow for clarifying actor interactions, boundary behavior, and exception handling of approved requirements. Use when requirement behavior remains ambiguous and teams need explicit main/alternate/exception flows; do not use for backlog prioritization."
---

# Use Case Modeling

## Overview
Use this skill to make behavior explicit across actors and system boundaries before coding.

## Scope Boundaries
- Approved requirements still leave interaction behavior unclear.
- Teams need aligned understanding of success, alternate, and failure flows.
- Boundary responsibilities across systems or roles are disputed.

## Templates And Assets
- Use case specification template:
  - `assets/use-case-template.md`

## Inputs To Gather
- Approved requirement set and known constraints.
- Actor definitions, permissions, and system boundaries.
- Business rules, integration dependencies, and error-handling expectations.

## Deliverables
- Use case set with preconditions, triggers, outcomes, and postconditions.
- Main, alternate, and exception flow definitions.
- Requirement-gap list mapped to unresolved use-case steps.

## Workflow
1. Identify actors and goals with clear boundary ownership.
2. Define main success flow from trigger to postcondition.
3. Add alternate flows for expected variation (authorization differences, optional paths, retries).
4. Add exception flows for failure and recovery behavior.
5. Validate data/state transitions and side effects at each step.
6. Trace uncovered ambiguity back to requirement items for refinement.

## Quality Standard
- Every critical actor goal has an explicit end-to-end flow.
- Exception behavior is concrete, not implied by generic error text.
- Boundary handoffs specify who validates, who mutates, and who observes.
- Gaps are actionable and linked to requirement refinement tasks.

## Failure Conditions
- Stop when system boundaries are not defined.
- Stop when exception handling cannot be mapped to responsible components.
- Escalate when unresolved use-case gaps block implementation planning.
