# Mock Boundary Decision Rules

- Mock only external dependencies that are expensive, flaky, or non-deterministic.
- Keep domain logic and core transformations unmocked when possible.
- If mocking hides contract behavior, add integration-level evidence.
- Explicitly document why each high-impact dependency is mocked or real.
