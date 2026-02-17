# Service Discovery And Probe Rules

- Use readiness probes for traffic eligibility, liveness for restart signals.
- Avoid probes that pass while dependencies needed for critical paths are down.
- Keep Service selectors stable and minimal to prevent accidental traffic shifts.
- Prefer DNS/service abstraction over hardcoded Pod addressing.
