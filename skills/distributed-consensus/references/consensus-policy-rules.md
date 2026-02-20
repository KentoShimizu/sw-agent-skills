# Consensus Policy Rules

- Choose quorum size based on tolerated simultaneous node failures and latency budget.
- Ensure commit rules preserve safety before optimizing for throughput.
- Define explicit behavior for minority partitions (read-only, fail closed, or unavailable).
- Membership changes should be staged to avoid transient quorum loss.
- Recovery and rejoin must include log/state catch-up guarantees.
- Validate split-brain prevention with targeted partition simulations.
