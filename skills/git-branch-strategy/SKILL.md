---
name: git-branch-strategy
description: "Define branch topology, lifecycle rules, and merge policy that match team delivery and release risk. Use when branch protection, release/hotfix flow, and merge discipline must be explicit to prevent unsafe history changes; do not use for CI workflow design or application behavior implementation."
---

# Git Branch Strategy

## Overview
Use this skill to design a branch model that teams can operate consistently under normal delivery and incident pressure.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Existing governance baseline:
  - `references/git-governance-contract.md`
- Topology decision guidance:
  - `references/branch-topology-decision-rules.md`

## Templates And Assets
- Branch policy template:
  - `assets/branch-policy-template.md`
- Branch protection checklist:
  - `assets/branch-protection-checklist.md`

## Inputs To Gather
- Team size, collaboration style, and review ownership model.
- Release cadence, hotfix urgency expectations, and support windows.
- Branch protection capabilities on the hosting platform.
- Current pain points (long-lived drift, merge conflicts, unclear ownership).

## Deliverables
- Branch class policy with creation/deletion/merge rules.
- Protection rules mapped to branch criticality.
- PR synchronization policy by branch class.
- Operational guidance for hotfix and release scenarios.

## Workflow
1. Define branch classes and responsibilities in `assets/branch-policy-template.md`.
2. Choose topology using `references/branch-topology-decision-rules.md`.
3. Set merge direction and sync policy per branch class.
4. Configure protection and verify with `assets/branch-protection-checklist.md`.
5. Publish policy with concrete examples for common workflows.

## Quality Standard
- Branch classes are minimal, non-overlapping, and enforceable.
- Protection rigor matches branch risk (stable > release > feature).
- Merge/sync strategy is clear enough to avoid per-PR ambiguity.
- Hotfix path is explicit and does not bypass traceability.

## Failure Conditions
- Stop when branch classes overlap without clear operational purpose.
- Stop when policy requires controls that the hosting platform cannot enforce.
- Escalate when hotfix process conflicts with protection and compliance requirements.
