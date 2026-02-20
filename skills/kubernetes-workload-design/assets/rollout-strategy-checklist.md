# Workload Rollout Strategy Checklist

- [ ] Strategy (RollingUpdate/Canary/BlueGreen) is explicit.
- [ ] Max surge/unavailable settings align with risk tolerance.
- [ ] Startup/readiness timings match application warmup behavior.
- [ ] Autoscaling behavior is tested under representative load.
- [ ] Rollback criteria are measurable and monitored.
