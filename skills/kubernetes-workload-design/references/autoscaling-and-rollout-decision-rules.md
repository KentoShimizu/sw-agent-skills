# Autoscaling And Rollout Decision Rules

- Choose scaling signals that correlate with user impact, not only CPU.
- Tune HPA stabilization windows to avoid oscillation.
- Prefer conservative rollout for stateful or high-criticality workloads.
- Validate rollout + autoscaling interaction under burst and failure scenarios.
