# Testing Integration Trigger And Examples

## Positive Trigger Signals
- User request implies integration boundary correctness.
- User asks for merge/release confidence from executable evidence, not only narrative discussion.
- User needs explicit test-level decision with traceable rationale.

## Non-Matching Signals
- ブラウザ導線のE2E検証をしたい（`testing-e2e` / `playwright` を使う）
- 単体関数だけを高速検証したい（`testing-unit` を使う）

## Example Requests That Should Trigger This Skill
- `Repository層とDBの結合部を検証したい`
- `service間API連携の失敗系を明示的にテストしたい`
- `adapter差し替え時の境界契約を確認したい`

## Minimal Deliverable Example
1. Decision question and constraints
2. Alternatives considered with trade-offs
3. Selected strategy and why
4. Executed evidence (commands/artifacts)
5. Residual risks and follow-up actions
