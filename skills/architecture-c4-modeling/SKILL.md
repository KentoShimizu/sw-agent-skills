---
name: architecture-c4-modeling
description: "C4 architecture modeling workflow for context, container, and component views that make boundaries and responsibilities explicit. Use when teams need a shared structural model before major implementation or refactoring; do not use as a substitute for decision records."
---

# Architecture C4 Modeling

## Overview
Use this skill to produce C4 views that remove architectural ambiguity and help teams reason about scope, ownership, and risk.

## Scope Boundaries
- System boundaries are unclear across teams or services.
- People disagree on where responsibilities belong.
- A large change requires shared architecture context before coding.

## Core Judgments
- System boundary: what is inside the system and what is external dependency.
- Container split: what deserves a runtime boundary versus a module boundary.
- Component granularity: where decomposition clarifies behavior versus adds noise.
- Trust boundaries and data sensitivity: where stronger controls are required.

## Practitioner Heuristics
- Each relationship in diagrams must answer one operational question: ownership, protocol, failure impact, or data-classification.
- If two boxes cannot be owned by different teams or deployed/scaled independently, they are usually not separate containers.
- Component diagrams are useful only for high-change or high-risk containers; do not draw them by default.
- Keep names consistent with runtime artifacts and code modules to avoid translation loss.

## Workflow
1. Define the audience and the questions each C4 level must answer.
2. Draw the context view around real external actors and systems.
3. Draw container boundaries based on runtime and ownership constraints.
4. Add component views only where behavior is too complex for container-level reasoning.
5. Annotate critical interactions with trust, latency, and failure assumptions.
6. Reconcile naming and dependencies with actual repositories and runtime topology.

## Common Failure Modes
- Diagrams mirror org charts instead of runtime behavior.
- Container boundaries are chosen by technology preference rather than coupling/ownership.
- Component diagrams become full class diagrams and lose decision value.

## Failure Conditions
- Stop when source system inventory is stale or contradictory.
- Stop when critical boundaries cannot be represented unambiguously.
- Escalate when diagram conclusions conflict with approved architectural decisions.
