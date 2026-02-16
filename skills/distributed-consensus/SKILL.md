---
name: distributed-consensus
description: "Design consensus-related decisions (quorum, leader election, commit rules, failure handling) for replicated state correctness. Use when correctness requires coordinated agreement across nodes under faults; do not use for non-replicated single-node workflows."
---

# Distributed Consensus

## Overview
Use this skill when system correctness depends on nodes agreeing on state transitions under crashes and partitions.

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

## Quick Example
- 5-node cluster with quorum = 3.
- Rule: writes require quorum acknowledgment before commit.
- Partition handling: minority side serves reads only (or no service) to prevent split-brain writes.

## Quality Standard
- Safety invariants are explicit (no divergent committed state).
- Liveness tradeoffs are acknowledged under partition conditions.
- Membership changes preserve quorum guarantees.
- Recovery/rejoin behavior is deterministic and tested.

## Workflow
1. Define safety invariants and availability targets.
2. Select quorum and leadership policy.
3. Define partition and recovery behavior.
4. Define membership change strategy.
5. Validate with failure simulation and state convergence checks.

## Failure Conditions
- Stop when quorum or commit semantics are undefined.
- Stop when partition behavior can cause split-brain writes.
- Escalate when membership change procedure risks safety violation.
