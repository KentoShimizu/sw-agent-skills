---
name: react-component-design
description: "React component design workflow for state ownership, composition boundaries, and predictable rendering behavior. Use when React component behavior or structure must be implemented or revised; do not use for repository-wide architecture governance or release policy decisions."
---

# React Component Design

## Overview
Use this skill to build React components that are composable, testable, and stable under evolving UI requirements.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Rendering and hooks rules:
  - `references/rendering-and-hooks-rules.md`

## Templates And Assets
- Component boundary template:
  - `assets/react-component-boundary-template.md`
- State flow checklist:
  - `assets/react-state-flow-checklist.md`

## Inputs To Gather
- UI and interaction requirements.
- Reuse boundaries and design-system constraints.
- State ownership and data-flow expectations.
- Performance and accessibility requirements.
- Prop and state shape contracts (explicit type/interface/schema expectations).

## Deliverables
- Component boundary and prop/state contract.
- Effect and async-behavior policy.
- Rendering-risk and accessibility checks.

## Workflow
1. Define component boundaries with `assets/react-component-boundary-template.md`.
2. Apply state/effect rules from `references/rendering-and-hooks-rules.md`.
3. Define explicit prop/state contracts; avoid `any`/opaque object bags for component boundaries.
4. Validate state ownership and transitions.
5. Review loading/empty/error/accessibility behavior.
6. Finalize with `assets/react-state-flow-checklist.md`.

## Quality Standard
- Component responsibilities are single-purpose and explicit.
- State ownership is minimal and predictable.
- Effects are scoped and cleanup-safe.
- Performance choices are evidence-driven.
- Data shape mismatches are handled at boundary adapters, not via repeated casts in render/effect logic.

## Failure Conditions
- Stop when component boundaries are ambiguous or cyclic.
- Stop when effect logic substitutes for missing state design.
- Escalate when state ownership cannot be resolved cleanly.
