# Docker Runtime Checklist

- [ ] Runs as non-root unless exception approved.
- [ ] Required env vars fail fast when missing.
- [ ] Only required ports/volumes are exposed.
- [ ] Health checks represent real readiness.
- [ ] Secrets are injected at runtime, not baked into image.
