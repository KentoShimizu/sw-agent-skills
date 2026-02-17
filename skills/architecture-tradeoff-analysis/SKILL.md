---
name: architecture-tradeoff-analysis
description: "Architecture trade-off analysis workflow for comparing options with explicit criteria, weighting, and sensitivity under uncertainty. Use when multiple viable architecture choices exist and rationale must be defensible; do not use after architecture direction is already fixed."
---

# Architecture Tradeoff Analysis

## Overview
Use this skill to make architecture choices explicit, comparable, and auditable instead of preference-driven.

## Scope Boundaries
- There are several plausible architecture options.
- Decision stakes are high and reversal is expensive.
- Teams need a shared basis for selecting one option.

## Core Judgments
- Option quality: whether candidates are realistic for the current context.
- Criteria set: business and technical dimensions that actually drive success.
- Weighting model: which criteria dominate and why.
- Sensitivity: how decision changes when assumptions shift.

## Practitioner Heuristics
- Keep criteria small and high-impact; too many criteria hide real priorities.
- Separate hard constraints from weighted preferences.
- Include operational burden and team capability as first-class criteria.
- Document dominant assumptions and the signals that would invalidate them.

## Workflow
1. Define decision question, constraints, and decision horizon.
2. Enumerate candidate options and reject non-viable ones early.
3. Set criteria and weighting aligned to current strategy.
4. Score options with evidence-backed rationale per criterion.
5. Run sensitivity analysis on top-weighted criteria and uncertain assumptions.
6. Select preferred option and document fallback decision path.

## Common Failure Modes
- Scoring hides biased assumptions rather than exposing them.
- Analysis compares abstract patterns, not implementable options.
- Sensitivity analysis is skipped, leading to brittle conclusions.

## Failure Conditions
- Stop when decision criteria cannot be agreed.
- Stop when option scoring lacks evidence for key criteria.
- Escalate when sensitivity analysis shows no robust winner.
