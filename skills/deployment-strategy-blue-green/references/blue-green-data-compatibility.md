# Blue Green Data Compatibility

## Key Checks
- New writes remain readable by old version during rollback window.
- Backward-incompatible schema changes are gated by phased rollout.
- Cross-environment shared state behavior is explicitly tested.
