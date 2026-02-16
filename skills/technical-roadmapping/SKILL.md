---
name: technical-roadmapping
description: Specialized workflow for sequencing of technical investments and dependency-aware milestones. Trigger when teams need a roadmap for technical initiatives with dependency ordering, milestone planning, and risk-aware sequencing across releases or quarters; do not use for low-level implementation design details.
---

# Technical Roadmapping

## Trigger Boundary
- Use when planning artifacts must convert uncertain inputs into executable milestones.
- Do not use for incident response execution; use `runbook-authoring` or `incident-postmortem`.
- Do not use for code-level quality review.

## Goal
Create realistic plans with explicit assumptions, risks, and sequencing.

## Inputs
- Change scope and risk profile
- Domain evidence for sequencing of technical investments and dependency-aware milestones
- Operational, compliance, and rollout constraints

## Outputs
- Technical roadmap with dependency map
- Decision log for sequencing of technical investments and dependency-aware milestones
- Verification checklist with measurable pass-fail criteria

## Workflow
1. Clarify outcomes and hard constraints for sequencing of technical investments and dependency-aware milestones.
2. Produce options and select an approach for sequencing of technical investments and dependency-aware milestones.
3. Evaluate trade-offs across security, performance, operability, and maintainability.
4. Verify decisions using milestone dependency and risk review.
5. Publish decisions, residual risks, and accountable follow-up actions.

## Quality Gates
- Scope and assumptions for sequencing of technical investments and dependency-aware milestones are explicit and reviewable.
- Decision rationale is backed by evidence instead of preference.
- Rollout and rollback criteria are defined when production impact exists.
- Residual risks have owners, due dates, and verification steps.

## Failure Handling
- Stop when roadmap milestones ignore critical technical dependencies.
- Escalate when accepted risk exceeds team policy thresholds.
