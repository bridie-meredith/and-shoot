---
phase: A — corpus + failure-mode taxonomy
project: R2 hybrid judge tuning
date: 2026-05-10
parent: design/shoot-v2/upstream-tuning-queue.md (URI-023, URI-006-adjacent)
companion: design/shoot-v2/r2-judge-tuning/B-locked-rubric.md
---

# Phase A — R2 Judge Tuning: Corpus + Failure-Mode Taxonomy

## What's being tuned

R2 is the **graph-aware hybrid judge** that runs after R1 author-blind output is locked. R2 reads the full 9-facet graph + cite-index + proto-lines and decides per-entry KEEP / DELETE / ADD. R2 is called from `.claude/commands/and-facets-r2.md`.

Unlike the 10 per-facet authors which are tuned (R1 side), R2 has been tuned only **opportunistically** through facet-tuning side effects:

- **memory-flags** got a dedicated R2 cycle (`memory-tuning-r2-{seams,defense,final}.md`).
- **feeling** Phase 5 audience adjudication surfaced 9 R2-aware findings (URI-023, not yet landed).
- The other 8 facets ran R2 against an untuned hybrid-judge prompt.

## What R2 tuning is, and isn't

R2 is a **meta-agent**: it does not have its own content rubric. It inherits each facet's rubric and applies it under graph-awareness conditions. So tuning R2 is not "rebuild a rubric"; it is **codify the judge-mode discipline that applies regardless of which facet R2 is being applied to**.

The standard five-phase facet tuning template (`facet-tuning-process.md`) does not map cleanly. R2 is closest to the **/and-season meta-tuning loop** (URI-021): tightening brief → tightened audience attack → auditor self-review → critic-tuning carry-back. That's the structure we adopt.

## The corpus

Three artifact families serve as the tuning corpus:

### Family 1 — memory-flags R2 cycle (8 entries)

Source: `design/shoot-v2/memory-tuning-r2-{seams,defense,final}.md`.

R2 decisions on s01e01 memory-flags facet:
- 8 entries reviewed
- Phase-4 outcomes: 6 REVISE + 2 DEFEND
- Phase-5 audience adjudication: 6 ACCEPT + 2 ACCEPT-WITH-CAVEAT, 0 REJECT
- 2 named residuals (mem:4 passive-recipient register; mem:8 surface echo)
- 3 confirmed rubric carry-backs (URI-001 items 1-3)

### Family 2 — feeling R2 findings (9 process items)

Source: `design/shoot-v2/feeling-tuning-final.md` Phase 5 audience adjudication.

URI-023 catalog (verbatim from `upstream-tuning-queue.md`):

1. Q1 should explicitly test against proto-line-as-somatic-action (R2-graph-aware failure mode confirmed across memory + feeling).
2. AP §7 should gate cross-character same-strategy + within-character formula-repetition.
3. Within-character same-strategy gate (negative-continuity across fires).
4. Cross-character vocabulary saturation gate at structural level.
5. Cross-character temporal-anchor formula-repetition gate.
6. Lonely-entry Q2-must-stand-alone test (R2-add discipline; THIRD confirmation across memory + feeling).
7. Card-licensed-vs-saturation distinction at semantic-slot level.
8. Body-as-subject discipline for somatic-tell-card-match (NEW — surfaced from feel:10 reshape).
9. **Process protocol — NOT a per-facet rubric edit:** "R2-adds receive a mandatory blind §Form + Q1 + Q2 re-test before round close." This is **R2 judge discipline**, not feeling-rubric content.

Items 1-8 are feeling-rubric edits (URI-023 in queue, not landed). Item 9 is **the load-bearing R2 finding**: it is the protocol gap this tuning project closes.

### Family 3 — s01e01 cite-index R1 → R2 diff

Source: `active-project/theater/facets/_cite-index.md` (current R2 state) compared to git-history R1 state.

Provides:
- Citation accrual delta (which proto-lines gained/lost facet citations in R2)
- Pile-up changes (>4 facets/proto-line)
- Lonely-entry changes
- Bare-protoline changes

This corpus has never been formally analyzed against R2 discipline. Phase B defines the questions to ask of it.

## Failure-mode taxonomy

Across families 1 + 2, four classes of R2 failure are confirmed:

### F-R2-1 — Form-discipline drift on R2 revisions

When R2 revises an entry to close a seam, the revision is graded against the seam, not against the original §Form discipline. The revision can satisfy the seam while introducing a new violation the §Form pass would have caught.

**Confirmed instances:**
- feel:10 Phase-E.c: revision swapped angular-measurement violation for comparison violation ("the way an estimate gets one"). Caught in Phase 5 audience adjudication, not in R2 itself. [URI-024]

**Why it happens:** R2's keep/delete/add framing focuses author attention on the named seam. The form/anti-pattern surface that R1 had to honor blind is not re-surfaced at R2 revision time.

**Severity:** HIGH. Single confirmed regression but the failure-mode is structural — every R2 revision is potentially exposed.

### F-R2-2 — Multi-justification under-strictness on R2-adds

R2 adds new entries justified by graph-evidence (NI fired here, memory could anchor). But the multi-justification gate (≥3 of 5 in feeling; comparable gates in other facets) is not always re-tested at R2-add time.

**Confirmed instances:**
- feel:13 (Taylor): R2-add with Q2 verified by adjacent proto-line content rather than entry-at-rest.
- feel:14 (mother): same pattern.
- 4 memory entries (per URI-023 #6, "THIRD confirmation across two facets").

**Why it happens:** the cross-facet co-citation evidence ("memory anchored, NI fired, tens=3") is graph evidence; the rubric's multi-justification ladder is character-and-body evidence. R2 substitutes one for the other.

**Severity:** HIGH. Pattern confirmed across 7+ entries across two facets.

### F-R2-3 — Lonely-entry adjacent-context dependency

R2-adds for "lonely" entries (no co-cited facets at the same proto-line) often justify themselves through the *next* proto-line rather than the entry-at-rest. Reads as on-rubric in context, fails when read in isolation.

**Confirmed instances:** same 4-7 entries as F-R2-2; the patterns overlap but are mechanically distinct.

**Why it happens:** R2 reads the proto-line stream linearly with full context. The author can lean on the next-beat without realizing the rubric tests at-rest.

**Severity:** MEDIUM-HIGH. Pattern confirmed; subset of F-R2-2 but worth a separate gate because the mitigation is different (read entry in isolation, not "re-check multi-justification").

### F-R2-4 — Cross-character / within-character pattern blindness

R2 sees the full graph and could detect cross-character same-strategy or within-character formula-repetition. Currently only per-character per-line surface-token saturation is gated (R1 inherits this). R2 has no structural-level cross-character gate.

**Confirmed instances:** URI-023 items 2, 3, 4, 5 (cross-character same-strategy, within-character formula-repetition, cross-character vocabulary saturation, cross-character temporal-anchor formula).

**Why it happens:** R2's per-facet judge passes serialize per-facet. Cross-character patterns within a single facet are visible to the judge but not currently gated.

**Severity:** MEDIUM. Pattern surfaced from feeling tuning; not yet confirmed across other facets, but structurally likely to repeat.

## What's NOT in scope for R2 tuning

- **Per-facet rubric content** — items 1-8 of URI-023 are feeling-rubric edits, not R2-discipline. They land via URI-023 separately.
- **Auditor classes** (CURVE-SHAPE / AP-SCAN / CONSTRAINT) — these run at Step G, after R2. URI-006 is the auditor tuning project.
- **R3 / Step E** — relaxation pass. Default-skipped. R3 discipline is downstream of R2's; tune R2 first.
- **Per-facet add-caps** — the ≤5 cap is structural; calibration is open but not the load-bearing gap.

## Tuning sequence (this project)

| Phase | Output | Status |
|---|---|---|
| **A — Corpus + failure-mode taxonomy** | this file | **complete** |
| **B — Locked R2 rubric (justification-first)** | `B-locked-rubric.md` | **complete** |
| **C — Arbiter protocol** | `C-arbiter-protocol.md` | **complete** |
| **D — Tightened audience attack on R2 outputs** | `D-tightened-attack.md` | requires dispatch run |
| **E — R2-self-review under locked rubric + arbiter** | `E-r2-self-review.md` | depends on D |
| **F — Carry-back synthesis + and-facets-r2.md edit** | `F-carry-back.md` + command edit | depends on E |
| **G — Re-run on s01e01 + audience verdict** | `G-validation.md` | dispatch-heavy session |

**Phase numbering note:** the sequence table was revised after the user direction on 2026-05-10 to add the arbiter protocol as Phase C. Subsequent phases shifted by one.

Phases C–F are dispatch-heavy and run in subsequent sessions. Phase B is authored now to give Phase C its target.

## Success criteria for the project close

R2 tuning closes when:

1. `B-locked-rubric.md` lands and contains explicit gates for F-R2-1 through F-R2-4.
2. `.claude/commands/and-facets-r2.md` is updated to invoke the locked rubric at every layer.
3. A re-run of R2 on s01e01 under the new discipline produces audience verdicts with 0 instances of F-R2-1 (form-drift on revisions) confirmed by Phase F audience pass.
4. URI-023 is closed (item 9 lands as command-side; items 1-8 land in `rubric-feeling.md` V2.1 as a parallel item).
5. URI-025 Phase 1 (S9.5) and Phase 3 (Phase 5.5) both consume the tuned R2 — same review surface, both pipelines.
