# Testing Mutation Trigger And Examples

## Positive Trigger Signals
- User request implies mutation score and weak assertion detection.
- User asks for merge/release confidence from executable evidence, not only narrative discussion.
- User needs explicit test-level decision with traceable rationale.

## Non-Matching Signals
- まだ基礎テストがない段階で初回設計したい（先に `testing-unit`/`testing-integration`）
- パフォーマンス限界を測りたい（`performance-*` を使う）

## Example Requests That Should Trigger This Skill
- `テストは通るが壊しても落ちない不安がある`
- `生存mutantを起点にアサーション強化したい`
- `重要モジュールのテスト有効性を定量評価したい`

## Minimal Deliverable Example
1. Decision question and constraints
2. Alternatives considered with trade-offs
3. Selected strategy and why
4. Executed evidence (commands/artifacts)
5. Residual risks and follow-up actions
