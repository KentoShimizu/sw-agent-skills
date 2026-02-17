# GitHub Actions Workflow Design Checklist

- [ ] Triggers are scoped to required events only.
- [ ] Job boundaries map to clear responsibilities.
- [ ] Permissions are least privilege per job.
- [ ] Cache strategy improves runtime without stale-risk.
- [ ] Concurrency/cancel policy avoids duplicated work.
- [ ] Failure logs are actionable.
