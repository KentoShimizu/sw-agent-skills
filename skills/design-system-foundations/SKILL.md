---
name: design-system-foundations
description: "Define scalable design-system foundations with clear ownership and adoption boundaries. Use when multiple teams need shared component standards, foundational patterns, and ownership rules to deliver consistent UI across products; do not use for backend data-model or deployment pipeline decisions."
---

# Design System Foundations

## Overview
Use this skill to establish stable UI foundations that multiple teams can adopt without diverging conventions.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Lifecycle governance guidance:
  - `references/foundation-lifecycle-guidance.md`

## Templates And Assets
- Foundation inventory:
  - `assets/foundation-inventory-template.csv`
- Ownership and lifecycle model:
  - `assets/foundation-ownership-model-template.md`

## Inputs To Gather
- Current component inventory, duplication hotspots, and drift patterns.
- Product surface priorities and expected growth areas.
- Engineering constraints (frameworks, theming model, release cadence).
- Governance expectations (ownership, review, and change control model).

## Deliverables
- Foundation architecture map (primitives, composition rules, and boundaries).
- Ownership model with lifecycle states (draft/active/deprecated/retired).
- Adoption strategy with migration sequence and risk notes.
- Decision log for rejected alternatives and rationale.

## Quick Example
- Primitive ownership: typography, spacing, and color scale managed centrally.
- Shared component ownership: cross-product components owned by design system team.
- Product extension policy: local variants allowed only with expiration and convergence plan.
- Lifecycle rule: deprecated components blocked for new usage after defined cutoff.

## Quality Standard
- Foundation boundaries are explicit and do not overlap ambiguously.
- Ownership and lifecycle are defined for every foundation artifact.
- Adoption plan minimizes breaking migrations for active teams.
- Accessibility and localization constraints are baked into foundation definitions.

## Workflow
1. Audit existing UI patterns and capture inventory in `assets/foundation-inventory-template.csv`.
2. Define foundational primitives and composition boundaries.
3. Assign ownership and lifecycle governance per foundation area using `assets/foundation-ownership-model-template.md`.
4. Validate technical feasibility with implementation teams.
5. Publish adoption plan with phased migration guidance and lifecycle policy from `references/foundation-lifecycle-guidance.md`.

## Failure Conditions
- Stop when foundation scope is too broad to govern consistently.
- Stop when ownership is undefined for shared artifacts.
- Escalate when migration cost is known but lacks mitigation plan.
