# Software Development Agent Skills

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](../LICENSE)

オープンな `SKILL.md` 形式に基づく、ソフトウェア開発向け Agent Skills リポジトリです。

[English](../README.md) | [中国語](README.zh-CN.md)

## 概要

このリポジトリには、次の内容が含まれます。

- 再利用可能な skills の標準ディレクトリ構成
- Codex、Claude Code、OpenCode 向けインストールスクリプト
- リンクやパス整合性を確認する検証スクリプト

## リポジトリ構成

- `skills/<skill-name>/SKILL.md`: 必須のスキル定義
- `skills/<skill-name>/scripts/`: 任意の補助スクリプト
- `skills/<skill-name>/references/`: 任意の参考資料
- `scripts/`: インストーラーとバリデーター
- `docs/`: 多言語 README

## クイックセットアップ

```bash
git clone https://github.com/KentoShimizu/sw-agent-skills.git
cd sw-agent-skills
bash scripts/install-skills.sh --agent all --scope global
```

プレビューのみ（ファイル変更なし）:

```bash
bash scripts/install-skills.sh --agent all --scope global --dry-run
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-skills.ps1 -Agent all -Scope global
```

## インストールオプション

### Bash (`scripts/install-skills.sh`)

| オプション | 必須 | 説明 | デフォルト |
| --- | --- | --- | --- |
| `--agent <all/codex/claude/opencode>` | いいえ | インストール対象のエージェント。 | `all` |
| `--scope <global/local>` | いいえ | インストール範囲。`local` は `--project-root` 配下へ配置。 | `global` |
| `--mode <symlink/copy>` | いいえ | 各スキルディレクトリの配置方式。 | `symlink` |
| `--source <path>` | いいえ | スキルのソースディレクトリ。`SKILL.md` を持つサブディレクトリを含む必要があります。 | `<repo>/skills` |
| `--project-root <path>` | いいえ | `--scope local` 時に使うプロジェクトルート。 | カレントディレクトリ |
| `--dry-run` | いいえ | ファイル変更せず実行内容のみ表示。 | 無効 |
| `--verbose` | いいえ | 詳細なコマンド出力を表示。 | 無効 |
| `--force` | いいえ | 既存の配置先スキルディレクトリを置換。 | 無効 |
| `-h`, `--help` | いいえ | ヘルプを表示。 | 無効 |

### PowerShell (`scripts/install-skills.ps1`)

| オプション | 必須 | 説明 | デフォルト |
| --- | --- | --- | --- |
| `-Agent <all/codex/claude/opencode>` | いいえ | インストール対象のエージェント。 | `all` |
| `-Scope <global/local>` | いいえ | インストール範囲。`local` は `-ProjectRoot` 配下へ配置。 | `global` |
| `-Mode <symlink/copy>` | いいえ | 各スキルディレクトリの配置方式。 | `symlink` |
| `-Source <path>` | いいえ | スキルのソースディレクトリ。`SKILL.md` を持つサブディレクトリを含む必要があります。 | `<repo>/skills` |
| `-ProjectRoot <path>` | いいえ | `-Scope local` 時に使うプロジェクトルート。 | カレントディレクトリ |
| `-DryRun` | いいえ | ファイル変更せず実行内容のみ表示。 | 無効 |
| `-VerboseList` | いいえ | 詳細な処理ログを表示。 | 無効 |
| `-Force` | いいえ | 既存の配置先スキルディレクトリを置換。 | 無効 |

## 検証

```bash
python3 scripts/validate_skill_links.py
python3 scripts/validate_no_absolute_paths.py
```

## 参考資料

- [Agent Skills](https://agentskills.io/home)
- [Codex](https://developers.openai.com/codex/skills)
- [Claude](https://docs.claude.com/en/docs/claude-code/skills)
- [OpenCode](https://opencode.ai/docs/skills)

## ライセンス

Apache License 2.0。`LICENSE` を参照してください。
