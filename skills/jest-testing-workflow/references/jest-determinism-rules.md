# Jest Determinism Rules

- Avoid assertions that depend on unordered asynchronous side effects.
- Use deterministic timer control for timeout/retry logic.
- Remove hidden state leakage between tests (module cache, globals, env).
- Ensure command profiles are stable across local and CI environments.
