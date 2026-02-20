# Model Selection Tradeoff Rules

- Do not optimize accuracy alone; include latency/cost/operability.
- Reject candidates that exceed serving constraints even if more accurate.
- Keep at least one fallback model candidate with known behavior.
