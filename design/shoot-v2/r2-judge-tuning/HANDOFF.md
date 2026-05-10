---
doc: handoff note — R2 judge tuning planning session
date: 2026-05-10
session-purpose: produce an executable plan for tuning R2 (the round-2 graph-aware judge in /and-facets); plan-mode workflow with subagent audit + Phase-1 codebase exploration + Plan agent design.
---

# Handoff — R2 Judge Tuning Plan

## Where the plan lives

- **Plan file (canonical, plan-mode output):** `~/.claude/plans/twinkling-questing-hanrahan.md` (outside the repo).
- **In-repo design dossier:** `design/shoot-v2/r2-judge-tuning/`
  - `PLAN.md` — v2 (the simplified-then-audited plan); supersedes A/B/C in places. Plan-mode output (`twinkling-questing-hanrahan.md`) supersedes PLAN.md v2 with Phase-1 findings integrated. PLAN.md will be updated to v3 in Action 3 of execution.
  - `A-corpus.md` — failure-mode taxonomy (F-R2-1 through F-R2-4).
  - `B-locked-rubric.md` — locked rubric with G1–G4 taste-questions.
  - `C-arbiter-protocol.md` — arbiter triggers T1–T6 (Action 3 reduces to T1, T4).
- **Audit report (subagent fork):** `active-project/staff/auditor/r2-tuning-plan-audit.md` — 3 HARD + 5 SIGNAL findings on PLAN v1, all addressed in v2 + plan-mode output.

## Parallel session — and-season counterpart

The user ran a parallel session producing a plan for /and-season at the same time. The counterpart artifact is in this repo at:

- `design/shoot-v2/session-plan-2026-05-10-bone-gate.md` (bone-gate planning, parallel to this R2 work).

A new session will compare the two side by side. This handoff note exists so the comparing session has a single anchor pointing at both plans.

## What this session committed

Commits on `main` from this session (in order):

1. `abef893` — URI-025: shared facet-review mechanism across /and-season + /and-facets
2. `284ff55` — URI-025: add IP-2b probe-mode to shared-review design
3. `5ed0799` — R2 judge tuning Phase A + B; URI-025 tensometer-promotion follow-up
4. `16c17b4` — R2 judge tuning: justification-first revision + arbiter protocol
5. `9a33fea` — R2 tuning PLAN v2: address audit findings

Plus the merge of PR #5 (`bb0a1b8`) which preceded this session's work.

## What this session did NOT commit

Working-tree modifications at the time of handoff (`git status` will show these) belong to the **parallel and-season session**, not this one:

- `.claude/commands/and-season.md`
- `CLAUDE.md`
- `active-project/staff/showrunner/memory.md`
- `design/shoot-v2/upstream-tuning-queue.md`
- `schemas/facet.schema.md`
- `staff/orchestrator-critic/card.md`
- `design/shoot-v2/session-plan-2026-05-10-bone-gate.md` (untracked)

These are intentionally untouched by this session.

## What the next session should do

If the next session is the comparison session: read both plan files (`twinkling-questing-hanrahan.md` for R2, `session-plan-2026-05-10-bone-gate.md` for and-season) plus this handoff. The two plans share architectural concepts (audit-first, fork-review, taste-justification-over-mechanics, corpus-internal-caveat-discipline) and are intended to be compared on those axes.

If the next session executes this plan: start at Action 1 of `~/.claude/plans/twinkling-questing-hanrahan.md`. Action 1 is read-only (`git diff 3cd53e5..0996013 -- active-project/theater/facets/memory.md feeling.md` + audience-verdict cross-reference) and produces `1-cite-index-summary.md` + `1-baseline-reconstruction.md` in this directory.
