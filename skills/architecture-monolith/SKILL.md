---
name: architecture-monolith
description: "Modular monolith architecture workflow for strong domain boundaries, transactional consistency, and operational simplicity in a single deployable. Use when teams need fast delivery and coherent data consistency with controlled complexity; do not use when independent runtime scaling boundaries are mandatory."
---

# Architecture Monolith

## Overview
Use this skill to design modular monoliths that preserve internal autonomy without introducing distributed-system overhead.

## Scope Boundaries
- Product scope or team size favors a single deployable unit.
- Cross-domain workflows require strong transactional consistency.
- Operational simplicity is a top constraint.

## Core Judgments
- Module boundaries: domain cohesion and dependency direction inside one codebase.
- Internal contracts: which module APIs are allowed and how enforced.
- Data ownership in shared database: logical ownership and write access discipline.
- Future extraction seams: where boundaries should support later service splits.

## Practitioner Heuristics
- Treat modules like products with stable public interfaces.
- Forbid cross-module database writes except through explicit module APIs.
- Keep shared kernel minimal and intentionally versioned.
- In dynamic languages, define explicit module interface types to avoid ad hoc maps and pervasive casts at boundaries.

## Workflow
1. Partition core domains into modules with clear responsibility.
2. Define allowed dependency directions and anti-corruption boundaries.
3. Specify module-level contracts for commands, queries, and events.
4. Align transactional scope with module invariants.
5. Add observability by module to expose coupling hotspots.
6. Record extraction candidates and triggers for future decomposition.

## Common Failure Modes
- Modular monolith degrades into "big ball of mud" via unrestricted imports.
- Shared tables bypass module contracts and break ownership.
- Runtime simplicity hides growing conceptual complexity.

## Failure Conditions
- Stop when module boundaries cannot be enforced in code review/tooling.
- Stop when critical invariants span modules without clear ownership.
- Escalate when required independent scaling/deployment is no longer feasible.
