---
name: architecture-microservices
description: "Design microservices boundaries, ownership, and integration contracts for independent deployability at domain level. Use when teams need service autonomy and scaling separation; do not use when one deployable can meet constraints."
---

# Architecture Microservices

## Overview
Use this skill to decide and design microservices in a way that is technically and operationally sustainable. The output must define clear ownership, contracts, and reliability expectations.

## Inputs To Gather
- Domain decomposition and team topology.
- Availability, latency, and scaling targets.
- Integration and consistency requirements.
- Operational maturity (on-call, observability, deployment discipline).

## Deliverables
- Service boundary map with owner per service.
- Inter-service contract strategy (API/event).
- Data ownership and cross-service consistency approach.
- Service-level reliability and observability requirements.

## Quality Standard
- Boundaries follow business capabilities, not technical layers.
- Each service has clear ownership and operational responsibility.
- Cross-service synchronous chains are minimized and justified.
- Data ownership conflicts are resolved explicitly.
- Failure handling across service boundaries is concrete and testable.

## Workflow
1. Derive candidate boundaries from domain and ownership.
2. Validate service autonomy across release and operations.
3. Define inter-service contracts and compatibility policy.
4. Define data ownership and cross-service consistency strategy.
5. Validate production readiness and rollout approach.

## Failure Conditions
- Stop when ownership is ambiguous.
- Stop when boundaries are layer splits rather than business splits.
- Escalate when consistency requirements invalidate service splits.
