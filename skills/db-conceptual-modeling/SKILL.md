---
name: db-conceptual-modeling
description: "Model domain entities, relationships, and bounded data responsibilities before logical table design. Use when business concepts, ownership boundaries, or relationship semantics are unclear and must be defined to avoid schema drift; do not use for index tuning or physical storage optimization."
---

# DB Conceptual Modeling

## Overview
Use this skill to build a domain-aligned conceptual model that stabilizes later logical and physical design decisions.

## Inputs To Gather
- Core business concepts and terminology.
- Ownership boundaries across teams/domains.
- Critical workflows and invariants.
- Reporting/analytics requirements that influence relationship shape.

## Deliverables
- Entity relationship concept map.
- Definition of ownership and source-of-truth per concept.
- Invariant list requiring transactional consistency.
- Open ambiguity list that blocks logical design.

## Quick Example
- Concept split: `Order` vs `Payment`.
- Decision: `Order` owns fulfillment lifecycle; `Payment` owns authorization/capture/refund lifecycle.
- Integration: explicit reference by immutable IDs, not shared mutable fields.

## Quality Standard
- Entities reflect business language, not implementation artifacts.
- Ownership boundaries are explicit and non-overlapping.
- Relationship cardinality and optionality are defined.
- Invariants are identified before table-level design.

## Workflow
1. Normalize terminology with domain stakeholders.
2. Define entities, relationships, and ownership boundaries.
3. Identify invariants and consistency-sensitive flows.
4. Validate conceptual model against major use cases.
5. Publish model and unresolved domain questions.

## Failure Conditions
- Stop when core terms have conflicting meanings.
- Stop when ownership boundaries remain ambiguous.
- Escalate when invariants conflict across domains without arbitration.
