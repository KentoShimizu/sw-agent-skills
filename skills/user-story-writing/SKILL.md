---
name: user-story-writing
description: Implementation-slice authoring for prioritized requirements. Trigger when approved and prioritized requirement items (for example `REQ-*`) must be decomposed into sprint-ready user stories with explicit user value, scope boundaries, and testability; do not use for requirement discovery.
---

# User Story Writing

## Trigger Boundary
- Use when requirements are prioritized and delivery slicing is required.
- Do not use to define canonical requirements; use `requirements-definition`.
- Do not use to assign release ranking; use `requirement-prioritization`.

## Goal
Create sprint-ready stories with explicit user value and clear completion conditions.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, evidence handling, privacy handling, and artifact lifecycle.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.

## Inputs
- Prioritized requirement backlog (example IDs: `REQ-*` when no existing policy is available)
- Relevant acceptance/non-functional/dependency context (examples: `AC-*`, `NFR-*`)
- Team capacity and planning horizon

## Outputs
- Story set linked to project-defined requirement IDs
- Story-level acceptance mapping and constraints
- Blockers, assumptions, and dependency notes

## Workflow
1. Derive small vertical slices from prioritized requirements.
2. Write actor-need-value statement for each story.
3. Link each story to one or more project-defined requirement and acceptance IDs.
4. Add non-functional and compliance constraints explicitly.
5. Split oversized stories until estimable in one cycle.

6. Compare at least two feasible approaches and explain why one is preferred.
7. Record key assumptions, unknowns, confidence, and rollback considerations.

## Quality Gates
- Every story has clear value and linked requirement IDs.
- Story scope fits one delivery cycle.
- Story completion criteria are testable.
- Compliance-related stories are not optional when legally required.

- Decision rationale and trade-offs are explicit.
- Assumptions, unknowns, and confidence are explicitly documented.

## Failure Handling
- Reject stories without requirement linkage.
- Stop planning when critical dependencies are unresolved.
