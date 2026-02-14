---
name: chaos-engineering-basics
description: "Foundational chaos engineering workflow for validating resilience assumptions through controlled fault injection in non-production and guarded production contexts. Use when designing controlled resilience experiments with explicit blast-radius controls; do not use for active incident command or postmortem document authoring."
---

# Chaos Engineering Basics

## Trigger Boundary
- Use when resilience assumptions need validation through controlled failure experiments.
- Do not use for incident postmortem documentation only; use `incident-postmortem`.
- Do not use when observability signals are not yet established; use `observability-*` first.

## Goal
Improve reliability confidence by exposing hidden failure modes safely.

## Inputs
- Service criticality and dependency map
- Existing SLO/SLI and alerting baseline
- Operational guardrails and blast-radius constraints

## Outputs
- Chaos experiment plan with safety controls
- Hypothesis and expected steady-state metrics
- Findings, remediation actions, and re-test criteria

## Workflow
1. Define steady-state behavior and safety guardrails.
2. Select one controlled fault scenario and blast radius.
3. Execute experiment with live monitoring and abort criteria.
4. Analyze impact against expected resilience behavior.
5. Publish remediation and schedule follow-up verification.

## Quality Gates
- Experiment has explicit abort and rollback criteria.
- Observability is sufficient to detect degradation quickly.
- Blast radius remains within approved limits.
- Findings produce owned remediation actions.

## Failure Handling
- Stop when guardrails or abort conditions are undefined.
- Escalate when experiment risk exceeds approved blast radius.
