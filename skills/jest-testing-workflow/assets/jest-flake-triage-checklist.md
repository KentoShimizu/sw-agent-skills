# Jest Flake Triage Checklist

- [ ] Test uses deterministic timers (`fakeTimers` where appropriate).
- [ ] Test does not depend on wall-clock timing noise.
- [ ] Async expectations await all pending promises/events.
- [ ] Shared global state is reset between tests.
- [ ] Mocks are isolated and restored reliably.
