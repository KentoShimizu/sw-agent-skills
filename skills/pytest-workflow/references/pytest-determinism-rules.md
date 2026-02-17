# Pytest Determinism Rules

- Eliminate reliance on wall clock, random seeds, and hidden environment state.
- Use explicit time/random control in tests for reproducibility.
- Keep command profiles stable between local and CI environments.
