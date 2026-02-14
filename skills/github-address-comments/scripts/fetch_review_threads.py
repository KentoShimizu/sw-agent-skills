#!/usr/bin/env python3
"""Fetch and summarize review threads for a GitHub pull request."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

GRAPHQL_CONNECTION_PAGE_SIZE = 100
LATEST_THREAD_COMMENT_COUNT = 1
PREVIEW_LIMIT_CHARS = 180


@dataclass(frozen=True)
class ThreadSummary:
    thread_id: str
    is_resolved: bool
    is_outdated: bool
    author: str
    path: str | None
    line: int | None
    body: str
    url: str


@dataclass(frozen=True)
class CommentSummary:
    comment_id: str
    author: str
    body: str
    url: str


def run_gh(args: list[str], cwd: Path) -> str:
    cmd = ["gh", *args]
    proc = subprocess.run(
        cmd,
        cwd=str(cwd),
        check=False,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(cmd)}\n{proc.stderr.strip()}")
    return proc.stdout


def resolve_repo_owner_name(repo_dir: Path) -> tuple[str, str]:
    payload = run_gh(["repo", "view", "--json", "nameWithOwner"], repo_dir)
    data = json.loads(payload)
    name_with_owner = data.get("nameWithOwner") if isinstance(data, dict) else None
    if not isinstance(name_with_owner, str) or "/" not in name_with_owner:
        raise RuntimeError("failed to resolve repository owner/name")
    owner, name = name_with_owner.split("/", 1)
    return owner, name


def resolve_pr_number(repo_dir: Path, pr_value: str | None) -> int:
    if pr_value is not None:
        try:
            return int(pr_value)
        except ValueError as exc:
            raise RuntimeError("--pr must be a pull request number") from exc

    payload = run_gh(["pr", "view", "--json", "number"], repo_dir)
    data = json.loads(payload)
    number = data.get("number") if isinstance(data, dict) else None
    if not isinstance(number, int):
        raise RuntimeError("failed to resolve current branch PR number")
    return number


def run_graphql(
    repo_dir: Path, query: str, variables: dict[str, str | int | None]
) -> dict[str, Any]:
    args = ["api", "graphql", "-f", f"query={query}"]
    for key, value in variables.items():
        if value is None:
            continue
        args.extend(["-F", f"{key}={value}"])

    payload = run_gh(args, repo_dir)
    data = json.loads(payload)
    if not isinstance(data, dict):
        raise RuntimeError("invalid GraphQL response payload")
    graphql_errors = data.get("errors")
    if isinstance(graphql_errors, list) and graphql_errors:
        raise RuntimeError("failed to load pull request review threads")
    return data


def extract_pull_request(data: dict[str, Any]) -> dict[str, Any]:
    repository = (data.get("data") or {}).get("repository")
    pull_request = (repository or {}).get("pullRequest")
    if not isinstance(pull_request, dict):
        raise RuntimeError("failed to load pull request review threads")
    return pull_request


def parse_page_info(connection: dict[str, Any], label: str) -> tuple[bool, str | None]:
    page_info = connection.get("pageInfo")
    if not isinstance(page_info, dict):
        raise RuntimeError(f"invalid {label} pageInfo payload")

    has_next_page = page_info.get("hasNextPage")
    end_cursor = page_info.get("endCursor")
    if not isinstance(has_next_page, bool):
        raise RuntimeError(f"invalid {label} pageInfo.hasNextPage value")
    if end_cursor is not None and not isinstance(end_cursor, str):
        raise RuntimeError(f"invalid {label} pageInfo.endCursor value")
    return has_next_page, end_cursor


def fetch_pr_threads(
    repo_dir: Path, owner: str, name: str, pr_number: int
) -> tuple[list[ThreadSummary], list[CommentSummary]]:
    review_threads_query = """
query(
  $owner: String!,
  $name: String!,
  $number: Int!,
  $cursor: String,
  $pageSize: Int!,
  $latestCommentCount: Int!
) {
  repository(owner: $owner, name: $name) {
    pullRequest(number: $number) {
      reviewThreads(first: $pageSize, after: $cursor) {
        nodes {
          id
          isResolved
          isOutdated
          comments(last: $latestCommentCount) {
            nodes {
              id
              body
              path
              line
              url
              author { login }
            }
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  }
}
""".strip()

    issue_comments_query = """
query(
  $owner: String!,
  $name: String!,
  $number: Int!,
  $cursor: String,
  $pageSize: Int!
) {
  repository(owner: $owner, name: $name) {
    pullRequest(number: $number) {
      comments(first: $pageSize, after: $cursor) {
        nodes {
          id
          body
          url
          author { login }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  }
}
""".strip()

    threads: list[ThreadSummary] = []
    thread_cursor: str | None = None
    while True:
        data = run_graphql(
            repo_dir,
            review_threads_query,
            {
                "owner": owner,
                "name": name,
                "number": pr_number,
                "cursor": thread_cursor,
                "pageSize": GRAPHQL_CONNECTION_PAGE_SIZE,
                "latestCommentCount": LATEST_THREAD_COMMENT_COUNT,
            },
        )
        pull_request = extract_pull_request(data)
        review_threads = pull_request.get("reviewThreads")
        if not isinstance(review_threads, dict):
            raise RuntimeError("invalid reviewThreads payload")

        thread_nodes = review_threads.get("nodes")
        if not isinstance(thread_nodes, list):
            raise RuntimeError("invalid review thread list payload")

        for node in thread_nodes:
            if not isinstance(node, dict):
                raise RuntimeError("invalid review thread payload")
            comments_connection = node.get("comments")
            if not isinstance(comments_connection, dict):
                raise RuntimeError("invalid review comment connection payload")
            comment_nodes = comments_connection.get("nodes")
            if not isinstance(comment_nodes, list):
                raise RuntimeError("invalid review comment list payload")
            if not comment_nodes:
                continue

            latest_comment = comment_nodes[0]
            if not isinstance(latest_comment, dict):
                raise RuntimeError("invalid review comment payload")

            threads.append(
                ThreadSummary(
                    thread_id=str(node.get("id") or ""),
                    is_resolved=bool(node.get("isResolved")),
                    is_outdated=bool(node.get("isOutdated")),
                    author=str((latest_comment.get("author") or {}).get("login") or "unknown"),
                    path=(
                        latest_comment.get("path")
                        if isinstance(latest_comment.get("path"), str)
                        else None
                    ),
                    line=(
                        latest_comment.get("line")
                        if isinstance(latest_comment.get("line"), int)
                        else None
                    ),
                    body=str(latest_comment.get("body") or ""),
                    url=str(latest_comment.get("url") or ""),
                )
            )

        has_next_page, thread_cursor = parse_page_info(review_threads, "reviewThreads")
        if not has_next_page:
            break
        if thread_cursor is None:
            raise RuntimeError(
                "reviewThreads pageInfo.endCursor is required when hasNextPage is true"
            )

    comments: list[CommentSummary] = []
    comment_cursor: str | None = None
    while True:
        data = run_graphql(
            repo_dir,
            issue_comments_query,
            {
                "owner": owner,
                "name": name,
                "number": pr_number,
                "cursor": comment_cursor,
                "pageSize": GRAPHQL_CONNECTION_PAGE_SIZE,
            },
        )
        pull_request = extract_pull_request(data)
        issue_comments = pull_request.get("comments")
        if not isinstance(issue_comments, dict):
            raise RuntimeError("invalid issue comment payload")

        comment_nodes = issue_comments.get("nodes")
        if not isinstance(comment_nodes, list):
            raise RuntimeError("invalid issue comment list payload")

        for node in comment_nodes:
            if not isinstance(node, dict):
                raise RuntimeError("invalid issue comment payload")
            comments.append(
                CommentSummary(
                    comment_id=str(node.get("id") or ""),
                    author=str((node.get("author") or {}).get("login") or "unknown"),
                    body=str(node.get("body") or ""),
                    url=str(node.get("url") or ""),
                )
            )

        has_next_page, comment_cursor = parse_page_info(issue_comments, "comments")
        if not has_next_page:
            break
        if comment_cursor is None:
            raise RuntimeError("comments pageInfo.endCursor is required when hasNextPage is true")

    return threads, comments


def body_preview(text: str, limit: int = PREVIEW_LIMIT_CHARS) -> str:
    compact = " ".join(text.split())
    if len(compact) <= limit:
        return compact
    return compact[: limit - 3] + "..."


def render_text(pr_number: int, threads: list[ThreadSummary], comments: list[CommentSummary]) -> str:
    lines: list[str] = []
    lines.append(f"pr={pr_number}")
    lines.append(f"review_threads={len(threads)}")
    lines.append(f"issue_comments={len(comments)}")

    unresolved = [t for t in threads if not t.is_resolved]
    resolved = [t for t in threads if t.is_resolved]

    lines.append("\n[unresolved_review_threads]")
    if not unresolved:
        lines.append("none")
    for idx, thread in enumerate(unresolved, start=1):
        location = ""
        if thread.path is not None:
            location = thread.path
            if thread.line is not None:
                location += f":{thread.line}"
        lines.append(
            f"{idx}. author={thread.author} outdated={thread.is_outdated} "
            f"location={location or '-'}"
        )
        lines.append(f"   preview={body_preview(thread.body)}")
        lines.append(f"   url={thread.url}")

    lines.append("\n[resolved_review_threads]")
    if not resolved:
        lines.append("none")
    for idx, thread in enumerate(resolved, start=1):
        lines.append(f"{idx}. author={thread.author} url={thread.url}")

    lines.append("\n[issue_comments]")
    if not comments:
        lines.append("none")
    for idx, comment in enumerate(comments, start=1):
        lines.append(f"{idx}. author={comment.author} preview={body_preview(comment.body)}")
        lines.append(f"   url={comment.url}")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch PR review threads via gh GraphQL")
    parser.add_argument("--repo", default=".", help="Path to repository")
    parser.add_argument("--pr", help="Pull request number")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    repo_dir = Path(args.repo).resolve()
    try:
        owner, name = resolve_repo_owner_name(repo_dir)
        pr_number = resolve_pr_number(repo_dir, args.pr)
        threads, comments = fetch_pr_threads(repo_dir, owner, name, pr_number)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if args.json:
        payload = {
            "pr": pr_number,
            "threads": [
                {
                    "thread_id": t.thread_id,
                    "is_resolved": t.is_resolved,
                    "is_outdated": t.is_outdated,
                    "author": t.author,
                    "path": t.path,
                    "line": t.line,
                    "body": t.body,
                    "url": t.url,
                }
                for t in threads
            ],
            "issue_comments": [
                {
                    "comment_id": c.comment_id,
                    "author": c.author,
                    "body": c.body,
                    "url": c.url,
                }
                for c in comments
            ],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(render_text(pr_number, threads, comments))

    return 0


if __name__ == "__main__":
    sys.exit(main())
