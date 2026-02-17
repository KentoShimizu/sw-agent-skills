---
name: documentation-architecture
description: "Author architecture documentation that explains boundaries, dependencies, and operational constraints for engineering decision-making. Use when architecture docs are primary deliverables or must be updated after structural changes; do not use for implementing production feature logic."
---

# Documentation Architecture

## Overview
Use this skill to produce architecture documents that improve shared understanding and reduce design/review ambiguity.

## Scope Boundaries
- Use this skill when the task matches the trigger condition described in `description`.
- Do not use this skill when the primary task falls outside this skill's domain.

## Shared References
- Review checklist:
  - `references/architecture-doc-review-checklist.md`

## Templates And Assets
- Architecture document template:
  - `assets/architecture-doc-template.md`
- Risk register template:
  - `assets/architecture-risk-register-template.csv`

## Inputs To Gather
- System boundary and component inventory.
- Dependency relationships and data/control flows.
- Key constraints (security, reliability, compliance, cost).
- Existing ADRs and known architecture risks.

## Deliverables
- Architecture narrative and structural views.
- Boundary and dependency explanations.
- Constraint and tradeoff summary.
- Open risks/assumptions and follow-up items.

## Quick Structure Template
1. Context and goals.
2. System boundaries and major components.
3. Interaction/data flow and trust boundaries.
4. Operational constraints and failure behavior.
5. Known risks and decision links.

## Quality Standard
- Audience can answer "what talks to what" and "why" quickly.
- Boundaries and ownership are explicit.
- Constraints and tradeoffs are concrete.
- Document links to decisions and unresolved risks.

## Workflow
1. Identify target audience and key questions.
2. Build boundary/dependency narrative and diagrams using `assets/architecture-doc-template.md`.
3. Capture constraints and tradeoffs, and track open risks in `assets/architecture-risk-register-template.csv`.
4. Validate against current implementation and decisions with `references/architecture-doc-review-checklist.md`.
5. Publish with ownership and update cadence.

## Failure Conditions
- Stop when architecture boundaries remain ambiguous.
- Stop when documentation omits critical operational constraints.
- Escalate when docs conflict with accepted architecture decisions.
