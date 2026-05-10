---
phase: B2b-baseline — main-session decision-discipline review (Plan B execution)
project: R2 hybrid judge tuning
date: 2026-05-10
inputs: active-project/theater/facets/{interest-narrator,memory,feeling,metaphor}.md as of post-Phase-4 r2_tuning_defense state; design/shoot-v2/feeling-tuning-final.md (URI-024 reference)
class-source: design/shoot-v2/r2-judge-tuning/A-corpus.md (canonical; schema's F-R2-* summary diverges — see upstream-tuning-queue.md URI-027)
status: AUTHORED — baseline review against R2-touched entries on the existing corpus
---

# Phase B2b-baseline — Decision-Discipline Review

## Scope

Review the 14 R2-touched entries on s01e01 against G1–G4 of `B-locked-rubric.md` (mapping to F-R2-1..4 per `A-corpus.md`). The R2-touched set per the `0996013` commit summary:

- **narrator-interest:** 7 R2-touched (2 DELETE, 5 ADD)
- **memory:** 4 R2-touched (4 ADD, 0 DELETE)
- **feeling:** 3 R2-touched (1 DELETE, 2 ADD)
- **metaphor:** 0 R2-touched (1 KEEP, 0 mutations; 7 cap-refusals)

Plus the historical F-R2-1 instance from `feeling-tuning-final.md` URI-024 (feel:10 Phase-E.c regression).

Three of four classes scoreable directly; F-R2-1 falls back to single-instance dossier source per `1-baseline-reconstruction.md`.

## Per-class scoring

### G1 / F-R2-1 — Form-discipline drift on revisions

Raw R2 (commit `0996013`) ran KEEP / DELETE / ADD only — no REVISE verdicts in the raw decision set, so the structural F-R2-1 surface is empty by construction at raw-R2 stage.

Single dossier-sourced instance: **feel:10 Phase-E.c revision** (`feeling-tuning-final.md` Phase 5, REJECT verdict; URI-024). The Phase-E author revision swapped an angular-measurement violation for an AP6 comparison violation ("the way an estimate gets one" parses as comparison-operator). Caught at Phase-F audience adjudication, not at R2-author time. Subsequently re-revised (URI-008-revised, "the voice steps down a margin and holds at the lower mark" — comparison construction removed, body-as-subject discipline applied).

**F-R2-1 raw R2 count: 0. Dossier count: 1 (feel:10).** B4 measures whether B3's §Form re-test prevents the structural pattern from re-emerging on a fresh R2 run.

### G2 / F-R2-2 — Multi-justification under-strictness on R2-adds

**11 R2-adds total.** Per-add score:

| Entry | Anchor | Verdict | Reasoning |
|---|---|---|---|
| narrator:22 | @24 | CLEAN | "shoulder tracking, not eye" — register-shift, perceptual-access, terse spotlight; not niche-driven. |
| narrator:23 | @94 | CLEAN | "eyes hold the seam… count she had not yet finished" — perceptual + interior; reads at-rest. |
| narrator:24 | @113 | CLEAN-marginal | "post-mark hand has not yet learned to release" — leans on @99 apprentice-mark beat; the body-lag claim stands at-rest. |
| narrator:25 | @131 | CLEAN | "second mark is the day's commit, priced and filed" — pricing register is the established household-vocabulary. |
| narrator:26 | @9 | CLEAN | "feet plant at the spread the body had not yet sized to the floorline" — co-cites mem:5 same round; body-larger-than-room register stands. |
| mem:5 | @9 | CLEAN | "body inside the body keeps its older height in the joints" — monument-grade, target-reference resolvable to `cond-reincarnation-mechanics-84ac`. |
| mem:6 | @103 | CLEAN | "cloth lifts at the height the body knows without being told; the knowing is the year-long drain" — monument-grade reframe; NI co-cite at narrator:19 @103. |
| mem:7 | @113 | CLEAN | "grip stays closed past the moment the action ended" — monument-grade chronic-body claim; NI co-cite. |
| mem:8 | @131 | CLEAN | "day closes in the shape of a thing already filed" — intra-episode callback to apprentice-mark @99; the reframe stands at-rest. |
| feel:13 | @129 | F-R2-2 (caught Phase-4) | r2_tuning_defense log: "R2-add NI-dependence on proto-line-as-somatic-action." Reshape addressed the lean. |
| feel:14 | @36 | F-R2-2 (caught Phase-4) | r2_tuning_defense log: "R2-add NI-dependence on speech act + 'before the words come' cross-character formula." Reshape addressed the lean. |

**F-R2-2 raw R2 count: 2** (feel:13, feel:14). Both caught at the Phase-4 defense pass and reshaped before Phase-F audience adjudication. Pattern: feeling-layer adds at bare-protoline anchors fire on the structural absence (no NI/mem at the anchor) rather than the at-rest somatic register; the §Form re-test in B3 is the structural fix.

### G3 / F-R2-3 — Lonely-entry adjacent-context dependency

Per `1-cite-index-summary.md`: 11 → 8 lonely entries; 2 of the 8 are R2-adds at bare protolines (feel:13 @129, feel:14 @36). These are the structural F-R2-3 candidates by construction — adds at bare anchors have no co-cite to validate at-rest reading.

The two entries overlap exactly with the F-R2-2 hits above. A-corpus.md notes: "the patterns overlap but are mechanically distinct." Same instances, different lens.

**F-R2-3 raw R2 count: 2** (feel:13, feel:14). Same instances as F-R2-2. Closed in Phase-4 defense reshape.

### G4 / F-R2-4 — Cross-character / within-character pattern blindness

Per the `r2_tuning_defense` Phase-4 logs in `feeling.md` (Taylor / mother / father blocks), four pattern clusters were detected and broken at Phase 4:

1. **Cross-character "breath-as-duration" formula** — fired across feel:1 (Taylor), feel:2 (Taylor), feel:4 (Taylor), feel:7 (mother), feel:9 (father), feel:11 (father). 6 entries across 3 characters. Defense work cleared all but feel:1 (kept breath as breath-out-as-deploy-trigger per Taylor card §Non-verbal-tics).
2. **Cross-character "before the X lands / falls / comes" formula** — fired on feel:13 (Taylor) and feel:14 (mother). Both reshaped.
3. **Within-character "negative-continuity" strategy saturation** — fired on feel:5 + feel:6 (mother, both used "what does NOT stop" as somatic strategy). Both shifted to positive somatic registers.
4. **POV NI register-overlap** — feel:2 (Taylor) overlapped Taylor's NI register; revised to break the overlap.

**F-R2-4 raw R2 count: 4 patterns** (each is one cluster surfaced; entry-level count would be 6+2+2+1 = 11 entries affected). Closed in Phase-4 defense.

## Headline against B4 gate

| Class | Raw R2 instances | Gate budget | Status |
|---|---|---|---|
| F-R2-1 | 0 raw + 1 dossier (feel:10) | 0 | **OVER budget** at dossier scope, **clean** at raw-R2 scope |
| F-R2-2 | 2 (feel:13, feel:14) | combined ≤2 with F-R2-3 + F-R2-4 | **OVER** if combined |
| F-R2-3 | 2 (feel:13, feel:14; same as F-R2-2) | — | — |
| F-R2-4 | 4 patterns | — | — |

Combined F-R2-2 + F-R2-3 + F-R2-4 (entry-deduplicated): **2 entries** (feel:13, feel:14) caught both for F-R2-2/3, plus 4 patterns of F-R2-4 affecting other entries. If counted at the entry level with deduplication: ~6 entries flagged. If counted at the pattern level: 4 patterns + 2 lonely-entry adjacency = 6.

Either accounting puts the historical raw R2 over the ≤2 combined budget by 3-4× margin. **The corpus confirms the failure modes A-corpus.md catalogued.** This is the expected baseline finding; the locked rubric exists because raw R2 fails the gate.

## What B4 measures (different question)

B4 is **not** "does the historical raw R2 hit the gate." B4 is "does B3's per-layer §Form re-test, free-prose decision shard, and arbiter T1+T4 prevent the failure modes from re-emerging on a fresh R2 run against the same corpus."

The historical 6+ failure-mode hits were caught in two ways: (a) Phase-4 defense (cross-character pattern audit, after R2 closed), and (b) Phase-F audience adjudication (URI-024 feel:10). Both are post-hoc — they fix what R2 produced rather than constraining R2 at decision time. B3's structural change moves the discipline to decision time. B4 measures whether that move closes the gap.

## Recommendation

Proceed to B2a (audience review of R2-touched entries on the existing corpus — measures audience-clean-ACCEPT %, not the failure-mode counts) and B4 (validation re-run with edited command).

**B2a gate** (≥70% audience clean-ACCEPT) is the precondition for B4. If audience finds the existing R2-touched entries below threshold even after Phase-4 defense, the load-bearing problem is R1 entry quality, not R2 judge discipline; B4 re-scopes to R1-author re-tuning.

**B4 expectation:** 0 F-R2-1 + ≤2 combined F-R2-2/3/4 on R2-touched entries from the fresh re-run. If the gate clears, the locked-rubric + arbiter discipline is doing the structural work; if not, B3's edits need refinement.
