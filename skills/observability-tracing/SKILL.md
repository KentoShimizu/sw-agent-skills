---
name: observability-tracing
description: "Observability tracing workflow for distributed trace coverage and critical-path diagnosis. Use when cross-service request paths need instrumentation or analysis to localize latency/error bottlenecks; do not use for business-feature implementation logic."
---

# Observability Tracing

## Overview
Use this skill to make critical request flows traceable end-to-end for latency and failure diagnosis.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Span attribute and sampling rules:
  - `references/span-attribute-and-sampling-rules.md`

## Templates And Assets
- Trace coverage map template:
  - `assets/trace-coverage-map-template.md`
- Trace quality checklist:
  - `assets/trace-quality-checklist.md`

## Inputs To Gather
- Critical cross-service user flows.
- Current instrumentation and propagation gaps.
- Sampling constraints and storage budget.
- Incident diagnosis requirements.

## Deliverables
- Trace coverage map for critical paths.
- Span attribute conventions and sampling policy.
- Validation evidence for trace queryability.

## Workflow
1. Define coverage targets in `assets/trace-coverage-map-template.md`.
2. Apply span/sampling policy from `references/span-attribute-and-sampling-rules.md`.
3. Validate quality via `assets/trace-quality-checklist.md`.
4. Fix missing spans/attributes on critical paths.
5. Publish tracing baseline and ownership.

## Quality Standard
- Critical flows are traceable end-to-end.
- Span attributes are consistent for diagnosis queries.
- Sampling preserves incident usability.

## Failure Conditions
- Stop when critical paths remain untraceable.
- Stop when trace context propagation is inconsistent.
- Escalate when tracing gaps block root-cause isolation.
