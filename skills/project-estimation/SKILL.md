---
name: project-estimation
description: "Project estimation workflow for dependency-aware breakdowns and uncertainty-calibrated effort ranges. Use when initiatives need planning-grade estimates with explicit assumptions and confidence ranges; do not use for low-level implementation design details."
---

# Project Estimation

## Overview
Use this skill to create realistic estimates that expose uncertainty and sequencing risk instead of false precision.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Estimation calibration rules:
  - `references/estimation-calibration-rules.md`

## Templates And Assets
- Estimation breakdown template:
  - `assets/estimation-breakdown-template.csv`
- Uncertainty register template:
  - `assets/uncertainty-register-template.md`

## Inputs To Gather
- Scope definition and dependency graph.
- Team capacity and delivery constraints.
- Historical delivery data for calibration.
- Risk factors and assumption volatility.

## Deliverables
- Work breakdown with range estimates.
- Uncertainty/risk register with owners.
- Sequencing recommendation and confidence level.

## Workflow
1. Create breakdown in `assets/estimation-breakdown-template.csv`.
2. Calibrate ranges with `references/estimation-calibration-rules.md`.
3. Track assumptions and risks in `assets/uncertainty-register-template.md`.
4. Review dependencies and critical path sensitivity.
5. Publish estimate with confidence and update policy.

## Quality Standard
- Estimates include explicit uncertainty ranges.
- Dependencies and assumptions are visible and owned.
- Calibration uses historical evidence when available.

## Failure Conditions
- Stop when estimates hide assumptions or uncertainty.
- Stop when dependencies are ignored in schedule confidence.
- Escalate when estimation risk blocks planning decisions.
