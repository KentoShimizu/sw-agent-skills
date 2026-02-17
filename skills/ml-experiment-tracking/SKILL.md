---
name: ml-experiment-tracking
description: "ML experiment tracking workflow for reproducibility, metadata integrity, and run comparison traceability. Use when multiple ML runs must be compared or reproduced reliably; do not use for generic API-layer or infrastructure-only changes."
---

# Ml Experiment Tracking

## Overview
Use this skill to make ML experiments comparable, reproducible, and audit-friendly.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Reproducibility metadata rules:
  - `references/reproducibility-metadata-rules.md`

## Templates And Assets
- Tracking schema template:
  - `assets/experiment-tracking-schema-template.md`

## Inputs To Gather
- Required metadata fields (code/data/config/artifacts).
- Tooling constraints for run logging and artifact storage.
- Reproducibility requirements by project risk level.
- Comparison dimensions for model decisions.

## Deliverables
- Experiment tracking schema and mandatory fields.
- Run comparison protocol.
- Reproducibility verification checklist.

## Workflow
1. Define required metadata with `assets/experiment-tracking-schema-template.md`.
2. Validate sufficiency using `references/reproducibility-metadata-rules.md`.
3. Enforce run logging and artifact lineage.
4. Re-run selected experiments from metadata only.
5. Publish reproducibility confidence and gaps.

## Quality Standard
- Every decision-grade run is reproducible.
- Artifact lineage is complete and queryable.
- Comparison views are consistent across runs.

## Failure Conditions
- Stop when runs cannot be reproduced from recorded metadata.
- Stop when artifact lineage is incomplete.
- Escalate when tracking gaps block release decisions.
