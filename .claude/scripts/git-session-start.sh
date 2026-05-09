#!/usr/bin/env bash
# SessionStart hook: ensure main is checked out and rebased onto origin/main.
# Silent on success; emits {"systemMessage": "..."} JSON on failure/warning.
set -u

repo="${CLAUDE_PROJECT_DIR:-}"
[ -z "$repo" ] && exit 0
cd "$repo" 2>/dev/null || exit 0
[ -d .git ] || exit 0

emit() {
  # $1 = message string
  printf '{"systemMessage":%s}\n' "$(printf '%s' "$1" | jq -Rs .)"
}

branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "DETACHED")
if [ "$branch" != "main" ]; then
  emit "and-shoot session-start: HEAD is '$branch', not main. Only main is used in this repo. Switch to main before continuing."
  exit 0
fi

if ! git fetch origin main --quiet 2>/dev/null; then
  emit "and-shoot session-start: git fetch origin main failed (offline?). Skipping rebase."
  exit 0
fi

local_sha=$(git rev-parse main)
remote_sha=$(git rev-parse origin/main)
if [ "$local_sha" = "$remote_sha" ]; then
  exit 0
fi

# Check for dirty tree before rebase — git rebase will refuse anyway, but the message is clearer here.
if ! git diff --quiet || ! git diff --cached --quiet; then
  ahead=$(git rev-list --count origin/main..main)
  behind=$(git rev-list --count main..origin/main)
  emit "and-shoot session-start: working tree is dirty; cannot rebase. main is ahead $ahead / behind $behind vs origin/main. Commit or stash, then rebase manually."
  exit 0
fi

out=$(git rebase origin/main 2>&1)
rc=$?
if [ $rc -ne 0 ]; then
  git rebase --abort 2>/dev/null
  snippet=$(printf '%s' "$out" | head -15)
  emit "and-shoot session-start: rebase onto origin/main FAILED and was aborted. Resolve manually.\n---\n$snippet"
fi
exit 0
