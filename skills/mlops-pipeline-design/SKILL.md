---
name: mlops-pipeline-design
description: "MLOps pipeline design workflow for orchestrating training, validation, packaging, and promotion with explicit gates. Use when ML lifecycle stages must be automated end-to-end with traceable promotion criteria; do not use for model-architecture research decisions."
---

# Mlops Pipeline Design

## Overview
Use this skill to design ML pipelines that are reproducible, governable, and promotion-safe.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Promotion gate rules:
  - `references/promotion-gate-rules.md`

## Templates And Assets
- Pipeline stage template:
  - `assets/mlops-pipeline-stage-template.md`

## Inputs To Gather
- Required lifecycle stages and ownership model.
- Artifact lineage and reproducibility requirements.
- Promotion/rollback policy constraints.
- Failure handling and rerun expectations.

## Deliverables
- Pipeline stage contracts with inputs/outputs/gates.
- Promotion criteria and rollback strategy.
- Audit-ready lineage and execution policy.

## Workflow
1. Define stage contracts in `assets/mlops-pipeline-stage-template.md`.
2. Apply gate policy from `references/promotion-gate-rules.md`.
3. Validate success/failure branches and rerun behavior.
4. Confirm lineage traceability across stages.
5. Publish pipeline governance and operational ownership.

## Quality Standard
- Every stage has explicit pass/fail gates.
- Promotion path is auditable and reversible.
- Artifact lineage remains intact end-to-end.

## Failure Conditions
- Stop when stages are not reproducible or traceable.
- Stop when promotion criteria are ambiguous.
- Escalate when manual overrides lack governance controls.
