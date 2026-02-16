# RBAC And NetworkPolicy Baselines

- Start with deny-by-default for both permissions and network paths.
- Grant namespace-scoped rights before cluster-wide rights.
- Separate service account roles by workload function.
- Keep network policies aligned to actual service dependency graph.
