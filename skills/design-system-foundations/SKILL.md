---
name: design-system-foundations
description: "Design system foundation workflow for defining reusable component foundations, patterns, and ownership boundaries. Trigger when multiple teams need shared component standards, token foundations, and ownership rules to scale consistent UI delivery across products; do not use for backend data-model or deployment pipeline decisions."
---

# Design System Foundations

## Trigger Boundary
- Use when reusable foundation elements are missing or fragmented.
- Do not use for token schema design; use `design-tokens`.
- Do not use for page-level navigation structure; use `information-architecture`.

## Goal
Create a coherent and maintainable design system foundation.

## Project Rule Policy
- Follow existing repository or organization rules first for IDs, approvers, quality gates, locale scope, and privacy handling.
- If no existing rule is available, define a lightweight project default and mark it as provisional.
- Treat example IDs in this skill as non-binding guidance.
- Skip manifest validation for documentation-only deliverables unless the project explicitly requests governed validation.

## Inputs
- Existing UI inventory and inconsistency map
- Product surface priorities
- Engineering implementation constraints

## Outputs
- Foundation map with project-defined IDs (example: `DSN-SYS-*` when no existing policy is available)
- Pattern ownership and lifecycle definitions
- Component adoption roadmap

## Workflow
1. Audit current components and usage fragmentation.
2. Define foundational primitives and composition boundaries.
3. Specify ownership and lifecycle state per foundation item.
4. Align foundation patterns with implementation constraints.
5. Publish adoption plan with migration sequence.

6. Compare at least two feasible approaches and explain why one is preferred.
7. Record key assumptions, unknowns, confidence, and rollback considerations.

## Quality Gates
- Foundation scope is complete for target product surfaces.
- Ownership and lifecycle are explicit for each item.
- Patterns are implementable without hidden dependencies.
- Accessibility requirements are part of foundation definitions.

- Decision rationale and trade-offs are explicit.
- Assumptions, unknowns, and confidence are explicitly documented.

## Failure Handling
- Stop when foundation boundaries overlap ambiguously.
- Escalate when ownership model cannot be established.
