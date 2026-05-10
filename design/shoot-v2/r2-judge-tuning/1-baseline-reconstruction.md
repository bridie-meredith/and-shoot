---
phase: B1 — manual baseline reconstruction (Plan B execution)
project: R2 hybrid judge tuning
date: 2026-05-10
inputs: git history of active-project/theater/facets/{memory.md,feeling.md}; commit 0996013 (R2 complete) and ancestors
status: BLOCKED — baseline commit unrecoverable from this branch's git history
---

# Phase B1 — Baseline Reconstruction (Result: BLOCKED)

## What Plan B B1 asked for

> `git diff 3cd53e5..0996013 -- active-project/theater/facets/memory.md active-project/theater/facets/feeling.md`. Classify the 20 R2-raw entries (8 memory + 12 feeling: Taylor 5, mother 4, father 3) by which were audience-clean on first pass. Build cite-index R1↔R2 mutation summary across all 10 facets.

## What this branch's git can deliver

- `0996013` ("Round 2 complete: s01e01 faceted-r2") **is** reachable. Its tree contains the post-R2 facet files.
- The plan's reference baseline `3cd53e5` **is not** in this repo. `git rev-parse 3cd53e5` errors `unknown revision`.
- `0996013`'s on-object parent SHA is `e390feb022920e73d0c977a3baf32855e146c30d`. That commit is also unreachable: `git rev-parse e390feb...^{commit}` errors `Needed a single revision`.
- The `git log -- active-project/theater/facets/memory.md` chain on this branch starts at `0d92240 shoot-v2 memory-flags facet tuning: full five-phase pipeline` and skips directly to `0996013`. Intermediate R1 raw-author state, if it ever existed as its own commit, is not reachable on this branch.

The most likely cause: `0996013` was authored on a since-collapsed feature branch whose pre-R2 ancestors did not survive a rebase or PR merge. The PR-merge artifact (`c22d26e Merge pull request #3 from bridie-meredith/claude/tune-shoot-v2-facets-uwtdo`) names a branch but the branch's pre-merge tip is not present locally and was not asked-for at this session's start.

## Implications for the metric

Plan B's B2b-baseline depends on classifying the R2-raw entries against the rubric without the post-R2 audit-driven housekeeping. With the baseline blocked, B2b-baseline can score:

- **F-R2-1 (form-drift on revisions):** weakly — the post-R2 entry text is readable, but the pre-revision text is not, so "did this revision introduce a violation while answering the seam" cannot be tested directly. The single confirmed F-R2-1 instance (feel:10 in URI-024) is documented in `feeling-tuning-final.md` and survives outside the git baseline.
- **F-R2-2 (multi-justification under-strictness on adds):** scoreable — the post-R2 entry is the add itself; reading it against the rubric tests the at-rest discipline directly.
- **F-R2-3 (lonely-entry adjacent-context dependency):** scoreable — the post-R2 entry plus its anchor proto-line are present; the cover-the-next-proto-line discipline can be applied.
- **F-R2-4 (cross-character / within-character pattern blindness):** scoreable — pattern-scan is a property of the post-R2 facet as a whole.

Net: three of four failure modes remain testable at B2b-baseline; F-R2-1 falls back to URI-024's named instance plus B4 native logs (which capture pre-revision and post-revision text by construction).

## Recovery options (not pursued in this branch)

1. **Cross-branch cherry-pick.** Fetch the original feature branch (`claude/tune-shoot-v2-facets-uwtdo`) from origin if its tip is still resolvable; check out the pre-R2 commit; export memory.md and feeling.md; diff against current. Not pursued: branch presence on remote not verified in this session and would require remote interaction outside the plan's read-only reconstruction step.
2. **Project archive comparison.** `projects/project_03/theater/facets/` is present (per `ls projects/project_03/theater/facets/`) and contains R1-era facet content. Caveat: project_03 is a different corpus from the active project; it cannot stand in for the s01e01 R1 baseline. Not pursued.
3. **`feeling-tuning-final.md` Phase E.c per-entry pre/post text.** The feeling tuning dossier may carry pre/post text for the entries that went through Phase E revision. This is the closest available recovery for F-R2-1 evidence specifically; it is what URI-024 cites for the feel:10 instance. Use this for any F-R2-1 claim B2b-baseline needs to make.

## What B2b-baseline can do without the baseline diff

Author against the post-R2 corpus only. Score F-R2-2 / F-R2-3 / F-R2-4 directly. Surface F-R2-1 only through the feel:10 reference and any other named instance in the feeling / memory tuning dossiers. Mark the F-R2-1 score as **single-instance / dossier-sourced**, not corpus-derived.

The Plan B headline metric (0 F-R2-1 + ≤2 combined F-R2-2/3/4 across R2-touched entries on a re-run corpus) is unaffected — the metric is scored against B4 native logs, not the historical baseline. The baseline limitation only narrows what B2b-baseline can adjudicate; it does not block the validation gate.
