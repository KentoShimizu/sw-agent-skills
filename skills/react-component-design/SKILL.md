---
name: react-component-design
description: "React component design workflow. Trigger when React component behavior (props/state/effects, composition, rendering performance, accessibility behavior) must be implemented or revised with framework-level decisions in scope; do not use for repository-wide architecture governance or release management policy."
---

# React Component Design

## Trigger Boundary
- Use when building or restructuring React UI components.
- Do not use for framework-neutral visual design planning; use `visual-design`.
- Do not use for backend API design.

## Goal
Create composable React components with clear state ownership and predictable rendering behavior.

## Inputs
- UI requirements and interaction states
- Shared component and hook constraints
- Performance and accessibility expectations

## Outputs
- Component boundary and prop contract design
- State ownership and data flow plan
- Rendering/performance risk checklist

## Workflow
1. Split UI by responsibility and reuse potential.
2. Define props, local state, and lifted state boundaries.
3. Isolate side effects and asynchronous behavior in hooks.
4. Validate loading, empty, success, and error states.
5. Review rerender patterns and memoization only where justified.

## Quality Gates
- Component responsibilities are single-purpose and testable.
- State flow is explicit and avoids hidden coupling.
- Accessibility and keyboard behavior are considered for interactive parts.
- Performance decisions are evidence-driven, not premature.

## Failure Handling
- Stop when component boundaries are unclear or cyclic.
- Escalate when required state ownership cannot be resolved cleanly.
