---
name: ml-data-preprocessing
description: "ML data preprocessing workflow for cleaning, normalization, and leakage-safe dataset preparation. Use when training/inference data pipelines need explicit preprocessing decisions; do not use for generic API-layer or infrastructure-only changes."
---

# Ml Data Preprocessing

## Overview
Use this skill to define preprocessing that improves model quality without introducing leakage or unreproducible transforms.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Leakage prevention rules:
  - `references/leakage-prevention-rules.md`

## Templates And Assets
- Preprocessing spec template:
  - `assets/preprocessing-spec-template.md`

## Inputs To Gather
- Source datasets, schema quality, and time boundaries.
- Missing/outlier characteristics and domain constraints.
- Train/validation/test split policy.
- Reproducibility and compliance requirements.

## Deliverables
- Preprocessing specification with transformation rationale.
- Leakage and data-quality validation plan.
- Reproducibility notes and versioning requirements.

## Workflow
1. Draft transform plan with `assets/preprocessing-spec-template.md`.
2. Validate temporal and label safety via `references/leakage-prevention-rules.md`.
3. Define split-safe transformations and quality checks.
4. Verify transform repeatability across runs.
5. Publish preprocessing contract and residual risks.

## Quality Standard
- Transformations are deterministic and versioned.
- Leakage risk is explicitly checked and mitigated.
- Data loss/quality trade-offs are documented.

## Failure Conditions
- Stop when preprocessing introduces label or temporal leakage.
- Stop when transforms are not reproducible.
- Escalate when data quality blocks decision-grade training.
