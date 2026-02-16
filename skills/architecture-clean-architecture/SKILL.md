---
name: architecture-clean-architecture
description: "Design enforceable dependency direction and layer boundaries using Clean Architecture. Use when domain rules leak into framework code or boundaries are unclear; do not use to choose service topology."
---

# Architecture Clean Architecture

## Overview
Use this skill to structure code so domain logic remains stable while frameworks and infrastructure can change safely. The output must be enforceable in code review and CI.

## Inputs To Gather
- Domain rules and use-case flows.
- Current module/dependency graph.
- Runtime/framework constraints.
- Non-functional goals (testability, latency, reliability).

## Deliverables
- Layer model and dependency rules.
- Port/adapter contracts with ownership.
- Refactoring plan for boundary violations.
- Enforcement approach for review/CI.

## Quality Standard
- Inner layers do not depend on outer technical layers.
- Use-case logic orchestrates behavior without infrastructure leakage.
- I/O translation is isolated at adapter boundaries.
- Transaction and consistency boundaries are explicit per use case.
- Rules are enforceable by static checks, tests, or review checklist.

## Workflow
1. Define target layers and allowed dependency direction.
2. Map current violations and classify risk.
3. Define ports/adapters for external interactions.
4. Plan incremental remediation with rollback-safe sequencing.
5. Add enforcement checks to prevent regression.

## Failure Conditions
- Stop when boundary rules are not technically enforceable.
- Stop when transaction boundaries remain ambiguous.
- Escalate when high-risk business logic stays in outer layers.
