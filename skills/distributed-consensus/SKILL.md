---
name: distributed-consensus
description: "Consensus workflow for quorum, leader election, commit semantics, and membership change safety. Use when replicated-state correctness requires coordinated agreement across nodes under faults; do not use for non-replicated single-node workflows."
---

# Distributed Consensus

## Overview
Use this skill when system correctness depends on multiple nodes agreeing on state transitions under crash and partition conditions.

## Scope Boundaries
- Replicated writes require explicit safety/liveness guarantees.
- Quorum and leadership behavior determine correctness.
- Membership changes and failover policy must be defined safely.

## Shared References
- Consensus policy rules:
  - `references/consensus-policy-rules.md`

## Templates And Assets
- Consensus policy template:
  - `assets/consensus-policy-template.md`

## Inputs To Gather
- Replicated state machine requirements.
- Fault model (crash, partition, byzantine assumptions).
- Latency/availability targets and quorum constraints.
- Membership change and recovery expectations.

## Deliverables
- Consensus policy decisions (quorum, election, commit semantics).
- Safety/liveness assumptions and risks.
- Operational policy for split-brain and degraded mode.
- Validation plan for failover and rejoin scenarios.

## Workflow
1. Capture policy baseline in `assets/consensus-policy-template.md`.
2. Define safety invariants and availability targets.
3. Select quorum, leadership, and commit rules using `references/consensus-policy-rules.md`.
4. Define partition, degraded-mode, and recovery behavior.
5. Define membership change strategy and validation sequence.
6. Validate with failure simulation and state convergence checks.

## Quality Standard
- Safety invariants are explicit (no divergent committed state).
- Liveness tradeoffs are acknowledged under partition conditions.
- Membership changes preserve quorum guarantees.
- Recovery/rejoin behavior is deterministic and tested.

## Failure Conditions
- Stop when quorum or commit semantics are undefined.
- Stop when partition behavior can cause split-brain writes.
- Escalate when membership change procedure risks safety violation.
