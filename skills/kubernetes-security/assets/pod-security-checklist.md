# Pod Security Checklist

- [ ] Containers run as non-root unless exception approved.
- [ ] Privileged mode and host namespace usage are restricted.
- [ ] Read-only root filesystem used where feasible.
- [ ] Capability drops/additions are explicit.
- [ ] Secret mounts and env exposure are minimized.
