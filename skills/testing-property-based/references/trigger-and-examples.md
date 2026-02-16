# Testing Property Based Trigger And Examples

## Positive Trigger Signals
- User request implies invariant validation with generated inputs.
- User asks for merge/release confidence from executable evidence, not only narrative discussion.
- User needs explicit test-level decision with traceable rationale.

## Non-Matching Signals
- 固定ケースのみで十分な小規模ロジック（`testing-unit` を使う）
- UI導線検証（`testing-e2e` / `playwright` を使う）

## Example Requests That Should Trigger This Skill
- `入力空間が広く、例ベースだけでは漏れが怖い`
- `エンコード/デコードの恒等性を保証したい`
- `集約ロジックの不変条件を乱択で検証したい`

## Minimal Deliverable Example
1. Decision question and constraints
2. Alternatives considered with trade-offs
3. Selected strategy and why
4. Executed evidence (commands/artifacts)
5. Residual risks and follow-up actions
