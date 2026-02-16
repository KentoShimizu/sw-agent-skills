# Testing Regression Strategy Trigger And Examples

## Positive Trigger Signals
- User request implies regression suite selection by risk and impact.
- User asks for merge/release confidence from executable evidence, not only narrative discussion.
- User needs explicit test-level decision with traceable rationale.

## Non-Matching Signals
- 単一テストケース実装のみ（`testing-unit` など個別skillを使う）
- 監視設計そのもの（`observability-*` を使う）

## Example Requests That Should Trigger This Skill
- `CI時間制約の中で回帰セットを最適化したい`
- `毎回全部回せないので高リスク優先で選びたい`
- `変更影響とテスト優先度を紐付けたい`

## Minimal Deliverable Example
1. Decision question and constraints
2. Alternatives considered with trade-offs
3. Selected strategy and why
4. Executed evidence (commands/artifacts)
5. Residual risks and follow-up actions
