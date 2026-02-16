# Testing Contract Trigger And Examples

## Positive Trigger Signals
- User request implies provider-consumer contract compatibility.
- User asks for merge/release confidence from executable evidence, not only narrative discussion.
- User needs explicit test-level decision with traceable rationale.

## Non-Matching Signals
- 画面の見た目検証だけをしたい（`testing-e2e` / `playwright` を使う）
- 単体ロジックの網羅をしたい（`testing-unit` を使う）

## Example Requests That Should Trigger This Skill
- `APIレスポンス変更で既存consumerが壊れないか検証したい`
- `イベントスキーマ変更を契約テストで担保したい`
- `providerとconsumerのCIで互換性ゲートを張りたい`

## Minimal Deliverable Example
1. Decision question and constraints
2. Alternatives considered with trade-offs
3. Selected strategy and why
4. Executed evidence (commands/artifacts)
5. Residual risks and follow-up actions
