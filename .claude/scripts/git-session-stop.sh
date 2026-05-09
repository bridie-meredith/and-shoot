#!/usr/bin/env bash
# Stop hook: push main to origin/main if there are unpushed commits.
# Never auto-commits. Warns on dirty tree or wrong branch. Silent on success.
set -u

repo="${CLAUDE_PROJECT_DIR:-}"
[ -z "$repo" ] && exit 0
cd "$repo" 2>/dev/null || exit 0
[ -d .git ] || exit 0

emit() {
  printf '{"systemMessage":%s}\n' "$(printf '%s' "$1" | jq -Rs .)"
}

branch=$(git symbolic-ref --short HEAD 2>/dev/null || echo "DETACHED")
if [ "$branch" != "main" ]; then
  emit "and-shoot stop: HEAD is '$branch', not main. Not pushing. Only main is used in this repo."
  exit 0
fi

dirty=""
if ! git diff --quiet || ! git diff --cached --quiet; then
  dirty="yes"
fi
untracked=$(git ls-files --others --exclude-standard | head -1)

# Try to update remote-tracking ref (non-fatal if offline).
git fetch origin main --quiet 2>/dev/null || true

ahead=$(git rev-list --count origin/main..main 2>/dev/null || echo 0)
behind=$(git rev-list --count main..origin/main 2>/dev/null || echo 0)

if [ "$behind" -gt 0 ]; then
  emit "and-shoot stop: main is BEHIND origin/main by $behind (also ahead $ahead). Not pushing — rebase first."
  exit 0
fi

if [ "$ahead" -eq 0 ]; then
  # Nothing to push. If dirty, surface a quiet reminder so work isn't lost on session end.
  if [ -n "$dirty" ] || [ -n "$untracked" ]; then
    emit "and-shoot stop: working tree has uncommitted changes (no auto-commit). Commit before next session if you want them on origin/main."
  fi
  exit 0
fi

# We have commits to push.
out=$(git push origin main 2>&1)
rc=$?
if [ $rc -ne 0 ]; then
  snippet=$(printf '%s' "$out" | head -10)
  emit "and-shoot stop: git push origin main FAILED.\n---\n$snippet"
  exit 0
fi

if [ -n "$dirty" ] || [ -n "$untracked" ]; then
  emit "and-shoot stop: pushed $ahead commit(s) to origin/main. Working tree still has uncommitted changes (no auto-commit)."
fi
exit 0
