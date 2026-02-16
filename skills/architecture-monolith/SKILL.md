---
name: architecture-monolith
description: "Design a modular monolith with clear module boundaries, dependency rules, and evolution seams. Use when one deployable can meet consistency, reliability, and delivery goals more effectively than service decomposition."
---

# Architecture Monolith

## Overview
Use this skill to design a modular monolith that keeps operational simplicity without sacrificing maintainability. The output must include clear boundaries and future extraction seams.

## Inputs To Gather
- Domain boundaries and transactional invariants.
- Team size, ownership model, and release process.
- Performance/reliability targets and expected growth.
- Known hotspots and contention risks.

## Deliverables
- Module boundary map with ownership.
- Dependency direction and interface rules.
- Cross-module transaction policy.
- Extraction seams and re-evaluation triggers.

## Quality Standard
- Module responsibilities are cohesive and non-overlapping.
- Dependency direction is explicit and enforceable.
- Cross-module coupling is intentional and minimized.
- Scaling hotspots and extraction candidates are visible.
- Evolution path to service split is realistic.

## Workflow
1. Partition domain into cohesive modules.
2. Define dependency rules and module interfaces.
3. Assign ownership and transaction boundaries.
4. Identify hotspots and coupling risks.
5. Define extraction seams and re-evaluation triggers.

## Failure Conditions
- Stop when cyclic dependencies appear.
- Stop when module ownership is unclear.
- Escalate when scaling or ownership constraints exceed monolith limits.
