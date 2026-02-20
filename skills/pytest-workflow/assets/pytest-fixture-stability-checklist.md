# Pytest Fixture Stability Checklist

- [ ] Fixtures avoid hidden shared mutable state.
- [ ] Fixture scope choices are intentional.
- [ ] Cleanup behavior is explicit.
- [ ] External dependencies are deterministic or controlled.
- [ ] Parametrized cases remain readable and debuggable.
