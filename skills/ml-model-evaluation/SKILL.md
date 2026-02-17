---
name: ml-model-evaluation
description: "ML model evaluation workflow for metric design, threshold setting, and failure segmentation. Use when model readiness decisions require explicit accept/reject criteria and segment-level evidence; do not use for generic API-layer or infrastructure-only changes."
---

# Ml Model Evaluation

## Overview
Use this skill to evaluate models with decision-grade evidence across aggregate and high-risk segments.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Threshold and segmentation rules:
  - `references/threshold-and-segmentation-rules.md`

## Templates And Assets
- Evaluation report template:
  - `assets/evaluation-report-template.md`

## Inputs To Gather
- Dataset splits and baseline/candidate definitions.
- Business cost trade-offs for false positives/negatives.
- Segment definitions for fairness/risk-critical cohorts.
- Acceptance thresholds and calibration requirements.

## Deliverables
- Evaluation report with thresholds and decision.
- Segment-level failure analysis.
- Acceptance/rejection rationale and follow-ups.

## Workflow
1. Build evaluation report in `assets/evaluation-report-template.md`.
2. Apply threshold/segment policy via `references/threshold-and-segmentation-rules.md`.
3. Validate calibration and error concentration risks.
4. Compare baseline vs candidate under same conditions.
5. Publish release recommendation and unresolved risks.

## Quality Standard
- Thresholds are tied to business risk trade-offs.
- Critical segments are explicitly evaluated.
- Decision rationale is traceable to evidence.

## Failure Conditions
- Stop when evaluation omits high-risk segments.
- Stop when acceptance thresholds are undefined.
- Escalate when model risk is unacceptable for rollout.
