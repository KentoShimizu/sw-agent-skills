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

## Shared Design Contract (Canonical)
- Use `../design-principles/references/design-governance-contract.md` as the primary reference for recommended structure.
- Track foundation elements with project-defined IDs (for example `DSN-SYS-*`).
- Optional consistency check (only if your repository enforces manifest validation): `python3 ../design-principles/scripts/validate_design_contract.py --manifest <path/to/manifest.json>`.

## Inputs
- Existing UI inventory and inconsistency map
- Product surface priorities
- Engineering implementation constraints

## Outputs
- Foundation map with project-defined IDs (for example `DSN-SYS-*`)
- Pattern ownership and lifecycle definitions
- Component adoption roadmap

## Workflow
1. Audit current components and usage fragmentation.
2. Define foundational primitives and composition boundaries.
3. Specify ownership and lifecycle state per foundation item.
4. Align foundation patterns with implementation constraints.
5. Publish adoption plan with migration sequence.

## Quality Gates
- Foundation scope is complete for target product surfaces.
- Ownership and lifecycle are explicit for each item.
- Patterns are implementable without hidden dependencies.
- Accessibility requirements are part of foundation definitions.

## Failure Handling
- Stop when foundation boundaries overlap ambiguously.
- Escalate when ownership model cannot be established.
