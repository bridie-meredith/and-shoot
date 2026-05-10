---
phase: B4 — validation re-run (executed as Plan C C1)
project: R2 hybrid judge tuning
date: 2026-05-10
status: COMPLETE — Plan C C1 executed the re-run on s01e01 R1 baseline; native .r2-decisions.md emitted; gate PASS (0× F-R2-1; F-R2-2/3/4 sum=2 ≤ 2). Discipline review at 2b-rerun.md.
plan-c-c1-artifacts:
  - active-project/theater/facets/.r2-decisions.md (consolidated; 456 lines)
  - active-project/staff/interest-narrator/r2-decision-shard.md
  - active-project/staff/memory/r2-decision-shard.md
  - active-project/staff/feeling/r2-decision-shard-{taylor-hebert-jaehaerys,oc-craftsman-mother,oc-craftsman-father}.md
  - active-project/staff/metaphor/r2-decision-shard.md
  - active-project/theater/facets/_cite-index.md (rebuilt)
companion-scoring: design/shoot-v2/r2-judge-tuning/2b-rerun.md
preserved-baseline-branch: r2-tuning-pre-rerun (full pre-revert state including audit-r5 + orchestrator-critic verdict on s01e01)
---

## Done — persona cards released

(Historical sentinel from Plan A/B coordination protocol; superseded by Plan C single-session execution. Retained for trace.)

## Plan C C1 outcome

Per-layer summary:

| Layer | K | D | R | A | Cap-refusals | F-R2-1 | F-R2-2 | F-R2-3 | F-R2-4 | Discipline-fails |
|---|---|---|---|---|---|---|---|---|---|---|
| R2.1 NI | 17 | 0 | 4 | 2 | 5 | 0 | 0 | 0 | 1 | 0 |
| R2.2 memory | 3 | 0 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 0 |
| R2.3 feeling (Taylor) | 1 | 1 | 2 | 0 | 5 | 0 | 0 | 0 | 1 | 0 |
| R2.3 feeling (mother) | 4 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 |
| R2.3 feeling (father) | 3 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 |
| R2.4 metaphor | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **28** | **1** | **8** | **3** | **25** | **0** | **0** | **0** | **2** | **0** |

**Gate PASS.** Detailed discipline scoring in `2b-rerun.md`.

---

# Phase B4 — Validation Re-Run (historical scaffolding)

# Phase B4 — Validation Re-Run

## B2a precondition gate: PASS

B2a (`2a-audience.md`) cleared the precondition gate at 12/14 = **85.7% clean ACCEPT** (≥70% threshold). PROCEED-TO-B4.

Per-persona summary:
- dark-fantasy-reader: 12/14 clean (REVISE on @131 paired-archive only)
- pulp-enthusiast: 9/14 clean (5 individual REVISEs clustered on position-dependent momentum; only 2 aggregated to REVISE)
- worm-canon-pedant: 14/14 clean (no canon-fidelity, lore-leak, or voice-register failures)

Two REVISEs aggregated to ≥2-persona threshold:
- **narrator:25 @131** — "the second mark is the day's commit, priced and filed"
- **mem:8 @131** — "the day closes in the shape of a thing already filed; the filing was the whole day -> e01:99"

Both close on administrative-filing register that archives the @99 apprentice-mark consequence rather than holding it live. Single structural seam, paired across two layers at the same anchor.

## B2a carry-back: G5 added to B-locked-rubric

The @131 seam plus pulp-enthusiast's five-entry position-dependency pattern is concrete audience evidence for a fifth gate. Landed in this branch (commit pending):

- `B-locked-rubric.md` — new **Gate G5** ("does this entry want to fire here, given where the scene is?") with episode-close special-case clause requiring at least one entry at any episode-end anchor to hold the prior peak's consequence live rather than confirming its filing.
- `.claude/commands/and-facets-r2.md` — top-of-file "Locked-rubric + arbiter discipline" section now references G1–G5 and surfaces the position-gate with a per-add justification requirement (position-category note + episode-close paired-archive check).
- `2a-audience.md` per-persona observations preserve the underlying evidence so future tuning rounds can re-pressure G5's calibration.

## Status

**B4 runtime dispatches re-routed to fresh corpus.** Three converging reasons re-route B4 from s01e01 to s01e02+ or s02e01 rather than running on the existing corpus:

1. **R1 baseline blocked.** The `git checkout 3cd53e5 -- active-project/theater/facets/` revert per the original Plan B B4 spec cannot run — the `3cd53e5` baseline commit is not reachable on this branch (see `1-baseline-reconstruction.md`). Without the revert, B4 would run R2 against the post-R2 facets, not raw-R1.

2. **s01e01 post-defense corpus is no-op-prone.** B2b-baseline (`2b-baseline.md`) confirmed the historical failure modes (F-R2-2/3 on feel:13, feel:14; F-R2-4 across 4 patterns; F-R2-1 dossier-sourced from feel:10) were caught and reshaped during r2_tuning_defense Phase 4. Re-running R2 on the post-defense corpus would largely produce zero mutations — not because B3's discipline is working, but because the input has already been hand-fixed. A "clean" rerun on s01e01 cannot distinguish "B3 discipline held" from "input already clean."

3. **Honest validation requires fresh data.** The validation question is whether B3's edits + G5 prevent the failure modes from re-emerging when the locked rubric is the only line of defense. That requires a corpus that has not been hand-cleaned. The next opportunities:
   - **s01e02+** — once R1 facets are authored for those episodes (currently s01e02-s01e06 have proto-lines per the season-plan but no R1 facet runs in `active-project/theater/facets/`).
   - **s02e01** — once `/and-season-plan s02` and `/and-season s02` fire (Plan A A3); the s02 first-fire produces fresh R1 + R2 + audit on a corpus authored under the post-A1 / post-A4 bone-gate discipline. This is the cleanest test — both bone-gate and R2 disciplines are exercised on first-of-corpus data.

## Concurrency note for Plan A

This branch did **not** mutate `active-project/theater/facets/*.md` during execution. No concurrent writer of facets was active. Plan A A3 (s02 first-fire) is unblocked from this branch's tree on the facet-mutation seam.

This branch did **not** dispatch any audience persona in a way that mutates the persona cards. B2a was a read-only dispatch against the post-A1 cards (the merge of `origin/main` at commit `5fc965f` brought the A1-promoted Tens-attack vocabulary into-tree before B2a fired against the persona cards). The sentinel below remains valid.

## Validation pass criteria (for the runtime session, when B4 fires on fresh corpus)

- **F-R2-1 (form-drift on revisions): 0 instances** in the per-layer REVISE shard entries. Cold-read of any revision against §Form + Q1 + Q2 must produce no new violations.
- **F-R2-2 + F-R2-3 + F-R2-4 combined: ≤2 instances** across all R2-touched entries.
- **G5 informational** — 0 paired-archive at episode-close anchors. (Not gating the verdict; flagged as carry-back if violated.)
- **Discipline-fail count:** logged but not gating.

If gate fails: diagnose, ≤3 iterations max, then surface as DISCIPLINE-FAIL for adjudication.

## Expected runtime artifacts (for the runtime session)

- `active-project/theater/facets/.r2-decisions.md` (consolidated; per Phase 6 of `and-facets-r2.md`).
- Per-layer shards under `active-project/staff/<facet>/r2-decision-shard.md` (feeling: per-character variants).
- Mutated facet files under `active-project/theater/facets/`.
- Rebuilt `_cite-index.md` (Phase 7 of `and-facets-r2.md`).
- Save branch capturing the pre-revert tree for rollback.
- This file (`4-validation.md`) updated with: validation verdict, R2-touched-entry failure-mode counts, audience clean-ACCEPT %, commit SHA of the validation commit (for Plan A A3 to read as the start signal for s02 first-fire — though A3's start signal is already cleanly the sentinel below per A1's completion).

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
