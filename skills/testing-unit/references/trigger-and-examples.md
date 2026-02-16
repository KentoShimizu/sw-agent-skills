# Testing Unit Trigger And Examples

## Positive Trigger Signals
- User request implies isolated deterministic unit behavior.
- User asks for merge/release confidence from executable evidence, not only narrative discussion.
- User needs explicit test-level decision with traceable rationale.

## Non-Matching Signals
- サービス間互換性確認（`testing-contract` / `testing-integration`）
- UI導線の実ブラウザ検証（`testing-e2e` / `playwright`）

## Example Requests That Should Trigger This Skill
- `ドメインロジックの境界条件を高速に固めたい`
- `例外系や分岐網羅をユニットで担保したい`
- `依存を分離して原因局所化したい`

## Minimal Deliverable Example
1. Decision question and constraints
2. Alternatives considered with trade-offs
3. Selected strategy and why
4. Executed evidence (commands/artifacts)
5. Residual risks and follow-up actions
