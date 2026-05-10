# Plan B — `/and-facets` R2 judge tuning execution

**Date:** 2026-05-10
**Pipeline:** `/and-facets` (R2 layer)
**Predecessor:** `~/.claude/plans/twinkling-questing-hanrahan.md` (canonical plan-mode output) + `design/shoot-v2/r2-judge-tuning/PLAN.md` v2.
**Parallel sibling:** Plan A — `plan-and-season-followon-2026-05-10.md` (bone-gate Phase 1.5 + Phase 2).
**Supersedes:** PLAN v2 in the r2-judge-tuning dossier (will be marked v3 at project close).

---

## Context

R1 facet authors are tuned (100% on s01e01); R2 (graph-aware judge — keep/delete/add against locked R1 output) has been tuned only opportunistically through memory and feeling work. URI-023 item 9 names the load-bearing finding: R2 revisions and adds drift from rubric form discipline because the judge focuses on the named seam rather than the full rubric.

Path Z (hybrid): manual reconstruction from git for the existing 20-entry baseline, then land native decision-log emission alongside the §Form re-test, then re-run R2 to produce native logs across the full 10-facet corpus.

URI-025's tensometer-promotion block is **superseded** by URI-026 (already landed). Plan B no longer claims to "unblock URI-025"; instead, Plan B emits decision-log frontmatter that the bone-gate's F7 verdict consumes (see Plan A Action A2).

---

## Outcome

- R2 produces decisions that survive audience adjudication on the first pass: 0 F-R2-1, ≤2 combined F-R2-2/3/4 on s01e01 R2-touched entries.
- Native `.r2-decisions.md` infrastructure persists across runs.
- Decision-shard frontmatter conforms to the schema Plan A A2 lands; F7 in the orchestrator-critic card consumes it.
- URI-023 item 9 closed in queue.

---

## Action sequence

| # | Name | Owns | Locked-shared | Dispatches |
|---|---|---|---|---|
| B1 | Cite-index inspection + manual baseline reconstruction | `r2-judge-tuning/1-*.md` | git history | 0 |
| B2a | Audience entry-quality review on existing R2 corpus | `r2-judge-tuning/2a-audience.md` | persona cards (read) | ≤6 |
| B2b-baseline | Decision-discipline review on reconstructed baseline | `r2-judge-tuning/2b-baseline.md` | `B-locked-rubric.md` | 0 |
| B3 | Carry-back synthesis + command edits (URI-023 #9 lands) | `.claude/commands/and-facets-r2.md`, `B-`/`C-` rubrics, `r2-judge-tuning/3-carry-back.md` | `schemas/audit-report.schema.md` (Plan A A2 must precede) | 0 |
| B4 | Validation re-run | `active-project/theater/facets/*.md` (s01e01) | persona cards (read) | ~20 |
| B2b-rerun | Decision-discipline review against native logs | `r2-judge-tuning/2b-rerun.md` | — | 0 |
| B5 | Project close + sentinel | `r2-judge-tuning/4-validation.md`, `upstream-tuning-queue.md`, `PLAN.md` v3 | — | 0 |

### B1 — cite-index inspection + manual baseline reconstruction

`git diff 3cd53e5..0996013 -- active-project/theater/facets/memory.md active-project/theater/facets/feeling.md`. Classify the 20 R2-raw entries (8 memory + 12 feeling: Taylor 5, mother 4, father 3) by which were audience-clean on first pass. Build cite-index R1↔R2 mutation summary across all 10 facets.

**Outputs:** `design/shoot-v2/r2-judge-tuning/1-cite-index-summary.md`, `1-baseline-reconstruction.md`. ~45 min main-session work.

### B2a — audience entry-quality review

Dispatch the 3 audience personas (dark-fantasy-reader, pulp-enthusiast, worm-canon-pedant) against R2-touched entries on s01e01 (35+ entries: NI 7, sensory 7, vibes 21, memory 4, feeling 3). Free-form per-entry verdicts. **Arbiter does not run on persona output.**

**Gate:** <70% clean ACCEPT re-scopes to R1-author re-tuning; ≥70% proceeds.

**Output:** `2a-audience.md`. ≤6 dispatches.

### B2b-baseline — decision-discipline review on reconstructed baseline

Main session reads B1's reconstruction for the 20 mem+feel entries against `B-locked-rubric.md` G1–G4. Score F-R2-1/3/4 reliably; F-R2-2 (motive honesty) scored weakly because raw decisions lack stated motive in the diff.

**Output:** `2b-baseline.md`. 0 dispatches.

### B3 — carry-back synthesis + command edits

**Precondition:** Plan A Action A2 has landed `schemas/audit-report.schema.md` `.r2-decisions.md` frontmatter spec. B3 reads it before authoring the decision-shard emission. Coordination signal: A2 commit message includes `r2-decisions schema` and lands on `main`.

Single edit pass to `.claude/commands/and-facets-r2.md`:

1. **§Form re-test** (per-layer, lines ~92, ~120, ~149, ~174): cold-read re-test against §Form + Q1 + Q2 before the KEEP/DELETE verdict, customized per facet rubric. **URI-023 item 9 lands here.**
2. **Decision-log shard emission** (per-layer Output blocks): each layer writes `active-project/staff/<facet>/r2-decision-shard.md` with one free-prose-with-verdict-line entry per decision/add. Feeling uses per-character shards. **Frontmatter conforms to the schema A2 landed** — `f-r2-counts: {f-r2-1: N, f-r2-2: N, f-r2-3: N, f-r2-4: N}` at the top of each shard.
3. **Mid-layer cite-index rebuild flipped optional → mandatory** between layers (line ~245); +3 cheap rebuild calls per run (forever-cost noted; bone-gate dispatch budget already accommodates).
4. **New Phase 5.5 — arbiter glue:** main-session arbiter reads each layer's shard, fires triggers T1 (rubric-label-heavy) and T4 (niche-driven adds) only — others dropped pending B2a evidence.
5. **Phase 6 update:** consolidate shards → `active-project/theater/facets/.r2-decisions.md`. Sum per-shard `f-r2-counts` into the consolidated frontmatter.

Parallel edits:
- `B-locked-rubric.md`: simplify decision log format to free-prose (drop labeled subfields per audit SIGNAL-004).
- `C-arbiter-protocol.md`: reduce 6 triggers to 2 (T1, T4); other triggers deferred until evidence supports them.

URI-023 item 9 lands here unconditionally — even if B2a produces no findings beyond the queue commitment, the §Form re-test still ships.

**Output:** `3-carry-back.md`. 0 dispatches.

### B4 — validation re-run

`git branch r2-tuning-pre-rerun` (save). Then `git checkout 3cd53e5 -- active-project/theater/facets/`. Run `/and-facets-r2 s01e01` with the edited command. Rebuild cite-index. Audience adjudication of new R2 output (3 personas, 1 sweep — pattern from `memory-tuning-r2-final.md`).

**Validation passes when:** 0 instances of F-R2-1, ≤2 combined F-R2-2/3/4 across all R2-touched entries. Failure → diagnose, ≤3 iterations max, then DISCIPLINE-FAIL surfaced.

**Output:** `4-validation.md` + native `active-project/theater/facets/.r2-decisions.md`. ~20 dispatches (6 R2 layers including feeling × 3 + 6 audience + ~3 arbiter + cite rebuilds).

**Concurrency note:** B4 mutates `active-project/theater/facets/` (s01e01 files). Plan A Action A3 (s02 first-fire) writes new s02 files under the same directory. Plan A A3 explicitly waits for B4's commit before starting; B4 records the commit SHA in `4-validation.md`.

### B2b-rerun — decision-discipline review against native logs

Main session reads `.r2-decisions.md` from B4 against G1–G4 across the full 10-facet corpus. Native logs make F-R2-2 motive-honesty scoreable.

**Output:** `2b-rerun.md`. 0 dispatches. Merges with B4 verdict for project close.

### B5 — project close + sentinel

1. Append `## Done — persona cards released` to `4-validation.md`. **This is the sentinel Plan A A1 reads** to start persona-card promotion. Without this line, A1 does not open any persona-card file.
2. Close URI-023 in `design/shoot-v2/upstream-tuning-queue.md`. URI-025 status note: mark as superseded by URI-026 (no-op if already done; idempotent check).
3. PLAN.md → v3 in `design/shoot-v2/r2-judge-tuning/`; annotate A/B/C as historical where superseded by execution.

---

## Files this plan edits

- `.claude/commands/and-facets-r2.md` — B3
- `design/shoot-v2/r2-judge-tuning/B-locked-rubric.md` — B3
- `design/shoot-v2/r2-judge-tuning/C-arbiter-protocol.md` — B3
- `design/shoot-v2/r2-judge-tuning/PLAN.md` — B5 (→ v3)
- `design/shoot-v2/r2-judge-tuning/{1,2a,2b-baseline,3,4,2b-rerun}-*.md` — created during execution
- `active-project/theater/facets/*.md` (s01e01) — B4 (revert + re-run)
- `active-project/theater/facets/.r2-decisions.md` — B4 (created)
- `active-project/staff/<facet>/r2-decision-shard.md` — B4 (created per facet/character)
- `design/shoot-v2/upstream-tuning-queue.md` — B5 (URI-023 close)

## Files this plan does NOT touch (Plan A territory)

- `.claude/commands/and-season.md`
- `.claude/commands/and-shoot.md`
- `.claude/commands/and-facets-r1.md`
- `staff/orchestrator-critic/card.md`
- `schemas/audit-report.schema.md`, `schemas/facet.schema.md`
- `active-project/audience/*/card.md` (read-only during B2a / B4; body-text writes are A1's)

## Concurrency contracts (mirror of Plan A)

| Resource | Plan A access | Plan B access | Serialization |
|---|---|---|---|
| `schemas/audit-report.schema.md` | A2 writes | B3 reads | **A2 must commit before B3 starts** |
| `active-project/audience/*/card.md` body | A1 writes | B2a / B4 read | A1 waits for B5 sentinel |
| `active-project/theater/facets/` | A3 writes new s02 files | B4 mutates s01e01 files | A3 waits for B4 commit SHA |
| `active-project/staff/showrunner/memory.md` | A3 writes | not touched | none |

**Cross-plan ordering:** A2 → B1 → B2a → B2b-baseline → B3 → B4 → B2b-rerun → B5 → A1 → A3 → A4 → A5.

A2 is the only Plan A item upstream of any Plan B step. Everything from B1 to B5 then runs without further coordination, ending with the sentinel that releases A1.

---

## Verification

1. `grep -n "§Form re-test\|cold-read re-test" .claude/commands/and-facets-r2.md` → 4 hits (one per layer).
2. `cat active-project/theater/facets/.r2-decisions.md` shows free-prose entries for every R2-touched entry; top-of-file `f-r2-counts:` frontmatter present and conforms to schema A2 landed.
3. Parse `4-validation.md` for F-R2-1/3/4 counts; assert 0 + ≤2 combined.
4. `grep "URI-023.*CLOSED" design/shoot-v2/upstream-tuning-queue.md` → 1 hit.
5. `grep "Done — persona cards released" design/shoot-v2/r2-judge-tuning/4-validation.md` → 1 hit (sentinel for A1).
6. Synthetic check: feed Plan A A2's verdict-template logic a `.r2-decisions.md` with `f-r2-1: 1`; F7 must trigger with `/and-facets` attribution. (This is A2's verification, run with B's output as the fixture.)
7. Re-run `/and-facets-r2 s01e01` after `git checkout r2-tuning-pre-rerun -- facets/` then `git checkout 3cd53e5 -- facets/`; decision logs regenerate; failure-mode counts remain inside thresholds (model variance acceptable).

---

## Risks

1. **B2b-baseline cannot score F-R2-2 fully** — git diff doesn't preserve author motive. Plan accepts asymmetry; B4 native logs close the gap for the rerun corpus.
2. **`git checkout 3cd53e5 -- facets/` is destructive** — mitigated by `r2-tuning-pre-rerun` save branch in B4.
3. **Decision-shard write inflates layer dispatch token cost** — feeling layer writes per-character shards; consolidation at Phase 6.
4. **Arbiter calibration drift across the 4-layer chain** — main-session arbiter holds context; later-layer interventions may be more permissive. Re-anchor against `C-arbiter-protocol.md` at start of each layer's arbiter pass.
5. **Path Z assumes B2b-baseline findings stable enough to drive B3 before native logs exist.** If B4 native logs surface failure modes B2b-baseline missed, budget one additional carry-back edit pass post-B4.
6. **Audience personas not tuned for decision-discipline review** — B2b-baseline + B2b-rerun are single-source (main session). Optional: dispatch an auditor fork at B2b close for second-line check.
7. **A2 schema delay blocks B3.** If Plan A is slower to land A2 than expected, B1/B2a/B2b-baseline can run in parallel without it; B3 stalls. Mitigation: A2 is a small, isolated edit and should land first regardless.
8. **F-R2-* threshold may not match Plan A's F7 sensitivity.** If A2 sets F-R2-1 > 0 = HARD but B4 surfaces 1 stubborn F-R2-1 it cannot eliminate, the s01e01 corpus blocks `/and-shoot` until manually adjudicated. Adjudication path: orchestrator-critic Open question 4 (two-card unification) becomes urgent.
