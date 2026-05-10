---
phase: B4 — validation re-run (Plan B execution)
project: R2 hybrid judge tuning
date: 2026-05-10
status: SCAFFOLDED — runtime dispatches deferred to a dispatch-heavy session; sentinel landed for Plan A A1 release
---

# Phase B4 — Validation Re-Run

## Status

**Runtime dispatches deferred.** This branch (`claude/implement-parallel-plan-SzWNb`) lands Plan B's structural deliverables (B3 command + rubric + arbiter edits, B5 closeout) but does not run the ~20-dispatch validation re-run. Reasons recorded:

1. The `git checkout 3cd53e5 -- active-project/theater/facets/` revert is blocked — the `3cd53e5` baseline commit is not reachable on this branch (see `1-baseline-reconstruction.md`).
2. Live-fire dispatches (4 R2 layers × possibly multiple per-character feeling forks + 6 audience + arbiter intervention overhead + cite rebuilds) are token-heavy and are out of scope for this code-development session per the user's "execute the plan with best judgement" instruction.
3. The structural infrastructure that the runtime validates (shard emission, §Form re-test, arbiter T1/T4, Phase 6 consolidation) is in place; the runtime session will measure it against a fresh dispatch.

## Concurrency note for Plan A

This branch did **not** dispatch any audience persona during execution. No concurrent reader of `active-project/audience/<persona>/card.md` body was active during the period this branch held the cross-plan write coordination contract. Plan A A1 (persona-card body promotion of tens-attack vocabulary) is therefore safe to execute against the cards in this branch's tree as soon as the sentinel below lands.

## Validation pass criteria (for the runtime session)

When the runtime session runs `/and-facets-r2 s01e01` (or the chosen corpus) against the edited command:

- **F-R2-1 (form-drift on revisions): 0 instances.** Cold-read of any revision against §Form + Q1 + Q2 must produce no new violations. Audience adjudication confirms.
- **F-R2-2 + F-R2-3 + F-R2-4 (multi-justification under-strictness + lonely-entry adjacent-context + pattern blindness): ≤2 combined instances** across all R2-touched entries.
- **Discipline-fail count:** logged but not gating. A non-zero count indicates the arbiter T1 / T4 escalation cycle exhausted on a verdict; surface for adjudication, do not block.

If the gate fails: diagnose, ≤3 iterations max, then surface as DISCIPLINE-FAIL for human adjudication.

## Expected runtime artifacts

- `active-project/theater/facets/.r2-decisions.md` (consolidated; per Phase 6 of `and-facets-r2.md`).
- Per-layer shards under `active-project/staff/<facet>/r2-decision-shard.md` (feeling: per-character variants).
- Mutated facet files under `active-project/theater/facets/`.
- Rebuilt `_cite-index.md` (Phase 7 of `and-facets-r2.md`).
- Save branch `r2-tuning-pre-rerun` capturing the pre-revert tree for rollback.
- This file (`4-validation.md`) updated with: validation verdict, R2-touched-entry failure-mode counts, audience clean-ACCEPT %, commit SHA of the validation commit (for Plan A A3 to read as the start signal for s02 first-fire).

## Sentinel for Plan A A1

Per the cross-plan coordination contract recorded in `plan-and-facets-r2-2026-05-10.md` (Plan B B5) and `plan-and-season-followon-2026-05-10.md` (Plan A A1 precondition), Plan A A1 reads this file for the sentinel line below before opening any persona-card file.

The sentinel below releases Plan A A1 to proceed. It is landed here at B5 close because no concurrent reader of persona-card body was active in this branch's execution path — Plan B's audience-reading dispatches (B2a, B4) are deferred to a runtime session that has not yet run, and the persona-card writes Plan A A1 makes do not race with anything this branch executes.

A future runtime session that runs B4 (validation re-run with audience adjudication) reads persona-card body. By the time that runtime session runs, Plan A A1 will have completed, so the cards will carry the promoted Tens-attack vocabulary section by then. The runtime session reads the post-A1 cards by construction.

---

## Done — persona cards released
