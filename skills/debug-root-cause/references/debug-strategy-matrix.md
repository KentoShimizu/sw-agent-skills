# Debug Strategy Matrix

Use this matrix to choose the first investigation strategy from symptom shape.

| Symptom | Primary suspicion | First experiment | Evidence to capture |
| --- | --- | --- | --- |
| Deterministic crash or exception | Invalid state/input contract | Reproduce with minimal input and inspect exact throw site | Stack trace, input payload, boundary contract |
| Intermittent failure/flakiness | Race, timing, shared state, nondeterministic dependency | Repeat in loop with deterministic seed/time controls | Failure rate, timing distribution, conflicting writes |
| Performance regression | Algorithmic complexity change, I/O amplification, lock contention | Compare before/after profile on same workload | CPU flame graph, query count, lock wait time |
| Data mismatch/corruption | Serialization contract drift, stale cache, wrong transformation order | Trace one record end-to-end through pipeline stages | Input snapshot, transformed outputs, schema/version |
| Environment-specific failure | Config drift, dependency/runtime version mismatch | Diff runtime config and dependency graph across environments | Env vars, package versions, feature flags, infra metadata |
| Timeout/retry exhaustion | Downstream latency, deadlock, retry storm | Measure per-hop latency and retry behavior with correlation IDs | Request timeline, retry counts, queue depth |

## Hypothesis Quality Rules
1. State each hypothesis as a causal claim: "If X is true, then Y should happen."
2. Prefer hypotheses that can be falsified quickly with one controlled change.
3. Keep one variable per experiment to avoid ambiguous outcomes.
4. Drop disproven hypotheses immediately and record why.

## Root-Cause Confirmation Criteria
1. Removing the suspected cause removes the failure.
2. Reintroducing the suspected cause reproduces the failure (when safe).
3. The explanation accounts for all observed symptoms, not only one trace.
4. The fix and evidence align with the causal explanation.
