---
name: git-revert-recovery
description: "Recover safely from problematic merges or commits using explicit revert strategy and validation. Use when a bad commit/merge has landed and rollback intent plus blast radius must be controlled; do not use for CI workflow design or application behavior implementation."
---

# Git Revert Recovery

## Overview
Use this skill to restore stability quickly on shared branches without destructive history rewrite.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Revert scope selection guidance:
  - `references/revert-scope-selection.md`

## Templates And Assets
- Revert runbook template:
  - `assets/revert-execution-runbook-template.md`
- Revert communication template:
  - `assets/revert-communication-template.md`

## Inputs To Gather
- Problematic commit/merge identifiers.
- Blast radius, urgency, and rollback success criteria.
- Verification scope for critical user paths.
- Communication and ownership requirements.

## Deliverables
- Revert execution runbook and results.
- Validation evidence for recovered state.
- Impact communication and follow-up action ownership.

## Workflow
1. Define revert target and expected recovered behavior.
2. Choose scope via `references/revert-scope-selection.md`.
3. Execute and track steps in `assets/revert-execution-runbook-template.md`.
4. Validate critical/regression-prone flows.
5. Communicate impact using `assets/revert-communication-template.md`.

## Quality Standard
- Revert scope is minimal but sufficient for stability recovery.
- Recovery validation covers critical user/business paths.
- Communication includes impact, owner, and follow-up timeline.
- Permanent fix path is recorded separately from emergency rollback.

## Failure Conditions
- Stop when revert target/scope is ambiguous.
- Stop when rollback cannot be validated against expected stable behavior.
- Escalate when revert does not restore stability within required window.
