# Secure Coding Review Checklist

- [ ] Trust boundaries and untrusted inputs are explicitly identified.
- [ ] Input validation and output encoding rules are defined at boundaries.
- [ ] Privileged operations include explicit server-side authorization checks.
- [ ] Sensitive data is redacted from logs and error messages.
- [ ] Dangerous patterns (unsafe deserialization, shell concatenation, path traversal) are prevented.
- [ ] Negative tests cover malicious payload classes relevant to the change.
