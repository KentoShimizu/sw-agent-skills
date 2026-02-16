---
name: architecture-c4-modeling
description: "Create C4 context, container, and component views that clarify boundaries, dependencies, and responsibilities. Use when architecture alignment needs clear structural communication; do not use as a final decision record."
---

# Architecture C4 Modeling

## Overview
Use this skill to produce C4 diagrams that reduce ambiguity and improve architecture communication. The output should support decision-making, implementation planning, and review.

## Inputs To Gather
- System landscape and external dependencies.
- Runtime/deployment boundaries.
- Trust boundaries and sensitive data flows.
- Existing ADRs and known risks.

## Deliverables
- Context diagram.
- Container diagram.
- Component diagrams only where complexity justifies them.
- Assumptions, omissions, and trace links to risks/ADRs.

## Quality Standard
- Each diagram answers a concrete audience question.
- Cross-level consistency is maintained (names, boundaries, relationships).
- Trust boundaries and critical data paths are explicit.
- Scope is controlled: only useful detail, no diagram noise.

## Workflow
1. Define target audience and questions each diagram must answer.
2. Draft context view with external actors/systems and trust boundaries.
3. Draft container view with runtime responsibilities and key interactions.
4. Add component views only for complex containers.
5. Validate consistency and annotate assumptions.

## Failure Conditions
- Stop when source inventory is stale or contradictory.
- Stop when diagram scope is unclear.
- Escalate when critical boundaries cannot be represented unambiguously.
