---
name: performance-profiling
description: "Performance profiling workflow for CPU/memory/I/O hotspot localization and optimization prioritization. Use when regressions or inefficiencies require profiler-based evidence for optimization decisions; do not use for non-performance functional acceptance decisions."
---

# Performance Profiling

## Overview
Use this skill to identify true runtime hotspots and prioritize optimizations by measurable impact.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Profiling evidence rules:
  - `references/profiling-evidence-rules.md`

## Templates And Assets
- Profiling report template:
  - `assets/profiling-report-template.md`
- Optimization priority matrix:
  - `assets/optimization-priority-matrix-template.csv`

## Inputs To Gather
- Performance symptom and target path.
- Reproducible profiling environment.
- Relevant profiling tools and sampling strategy.
- Acceptable optimization risk constraints.

## Deliverables
- Profiling report with hotspot evidence.
- Prioritized optimization backlog.
- Before/after impact validation plan.

## Workflow
1. Capture profiling scope in `assets/profiling-report-template.md`.
2. Gather baseline profiler evidence.
3. Prioritize opportunities with `assets/optimization-priority-matrix-template.csv`.
4. Apply `references/profiling-evidence-rules.md` for decision quality.
5. Publish optimization plan and verification gates.

## Quality Standard
- Hotspots are tied to specific code paths and user impact.
- Priority reflects impact, effort, and risk.
- Optimization decisions are evidence-backed.

## Failure Conditions
- Stop when hotspots cannot be attributed to concrete paths.
- Stop when expected gains are speculative without evidence.
- Escalate when high-impact bottlenecks remain unresolved.
