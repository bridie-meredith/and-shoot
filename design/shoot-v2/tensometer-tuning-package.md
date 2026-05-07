# Tensometer Facet Tuning — Final Package

End-to-end pipeline run for the tensometer facet, applying the five-phase tuning process from `design/shoot-v2/facet-tuning-process.md`. Run 2026-05-06.

**Headline:** locked V2 rubric + dramatist two-pass authoring + single mechanic auditor produces a co-deployable pipeline at **77/77 = 100%** rubric-compliance after one revise round, with a **SHAPE-OK** curve verdict (frequency-band soft-fail noted on 2-rung, ruled honest revision not miscalibration). User-supplied requirements (cross-facet coordination signal + chapter-escalation guarantor) baked into the rubric and verified through the pipeline.

---

## Trajectory

| Round | Stage | Reviewer | Result | Notes |
|---|---|---|---|---|
| 0 | Corpus prep | — | s01e01 (77 proto-lines) selected as full-curve corpus | No prior tensometer file exists; baseline must be synthesized |
| 1 — V1 | Lenient form-only review | mechanic auditor | 77/77 = 100% | Axis-plausibility floor; expected ceiling |
| 1 — V2 | Strict review of naive baseline | mechanic auditor | **39/77 = 50.6%** | Baseline to beat; SHAPE-FAIL (24.7% 3-rate, climax non-uniqueness) |
| 2 — Writer fork | Dramatist with rubric, blind to naive | mechanic auditor | **75/77 = 97.4%** | Lift from 50.6 = **+46.8**; SHAPE-OK; 5 hard-calls flagged for Phase 3 |
| 3 — Adversarial seams | Same auditor, hostile mode | — | 5 STRONG / 8 MODERATE / 3 THIN seams + 1 curve seam | Surfaced 3 additional Phase-2-passed faults |
| 4 — Defense or revise | Dramatist | — | 5 revise (4 strong-seam + auditor-confirmed @35) + 8 defend + curve-seam dissolved | All defenses rubric-cited |
| 5 — Final adjudication | Same locked rubric | mechanic auditor | **77/77 = 100%** | SHAPE-OK with frequency-band soft-fail; READY-WITH-CAVEATS |

Comparable lift to loc-state run (53.8 → 94.7 → 100); slightly stronger Phase 2 (97.4 vs 94.7) likely because tensometer's 3-axis mechanic discriminates more cleanly than loc-state's three-axis-PLUS-form check.

---

## What the user-supplied requirements added

User mid-Phase-0 amendment: "Tensometer should produce a signal other facets can use AND a guarantee that chapters follow optimal escalation patterns."

These were not in the loc-state or dialogue runs and reshaped the rubric:

### Cross-facet coordination signal (now §"Cross-facet contract" in the rubric)

The rubric now names downstream consumers and the gates/expectations they depend on:
- **Stitcher rendering density:** 3 → full; 2 → normal; 1 → compressible.
- **Loudness flags:** gate at tens ≥ 2.
- **Metaphor flags:** gate at tens = 3.
- **Memory flags:** expected to cluster at tens-transitions.
- **Audience-interest flags:** expected dense at 3-clusters and adjacent 2s.
- **Narrator-interest flags:** expected dense at tens-transitions.
- **State-updates:** 3-beats expect co-citation (or registration-only justification); 1-beats with state-updates are suspicious.
- **Loc-state:** clusters at tens-transitions.

Phase 5's contract pre-ship check (`active-project/staff/auditor/phase5-tensometer-final.md` §"Cross-facet contract pre-ship check") verifies the locked file supports the contract. Three contract risks were named and mitigated via inline annotations on the shipped facet:
1. @39 must not receive canonical state-updates (held-against-turn registration class only).
2. @48 vs. @64 distinction must survive into the filed facet via annotations.
3. The @1-@22 approach zone is anchor-sparse for downstream facets.

### Chapter-escalation guarantor (now §"Curve-shape rubric" in the rubric)

The rubric now contains scene-level and episode-level shape requirements:
- Each scene needs a 3 (or dramatist exception flag).
- Rise to peak through 2s; release after through descending rungs.
- No flatlining (>30 beats with no 2 or 3 = kickback).
- Episode-level: act-shape visible, climax unique, frequency band 60-75 / 20-30 / 5-10.

The dramatist's authoring is now two-pass:
1. **Per-beat pass.** Three-axis rating per proto-line.
2. **Curve-shape pass.** Read the file as a curve. Fix misratings, kick back to screen-writer for structural gaps, OR flag scene-boundary issues. **Do not inflate to manufacture shape.**

The reviewer's verdict gained a SHAPE-OK / SHAPE-FAIL output beside per-entry accuracy. Phase 1 naive baseline was SHAPE-FAIL (climax non-uniqueness from bleed). Phase 5 final is SHAPE-OK with documented frequency-band soft-fail.

---

## What worked

1. **The five-phase pattern transfers to scalar facets.** Same trajectory shape (~50% baseline → ~95% writer-fork → ~100% post-revise) as loc-state and dialogue. The pipeline is now demonstrably general across binary (loc-state fire/don't-fire), enumerated (dialogue per-category-fork), and scalar (tensometer 1/2/3) facet types.

2. **Two-pass authoring vs. single-pass.** Tensometer required adding a curve-shape pass on top of per-beat rating because the user-supplied escalation requirement made the file as a whole an output, not just a bag of scalars. This pattern likely transfers to any facet where the corpus shape (not just per-entry shape) carries downstream load — state-updates and narrator-interest are candidates.

3. **Cross-facet contract as explicit pre-ship gate.** This is new with tensometer and is the clearest statement to date of what a locked facet owes to its downstream consumers. Worth backporting to loc-state's package (loc-state has implicit consumers but no explicit contract section).

4. **Frequency-band soft-fail handled correctly.** Phase 4's downward revisions pushed the 2-rung below the 20% floor (15.6%). The honest call was: don't inflate to hit the band. The correct mitigation was producer-note + flag for screen-writer kickback consideration, not retro-fitting ratings. This validates the rubric's "do not inflate" prohibition as a load-bearing principle.

5. **The dramatist agent is the right author.** Two-pass authoring with curve-shape audit is a natural extension of dramatist's existing role (structural critic). No new agent type needed; the agent's existing competence (rise-peak-fall vocabulary, inert-stretch detection) maps cleanly onto curve-shape verdicts.

6. **Adversarial seams catch what mechanic review misses, again.** Phase 2 audit verdicted 75/77 correct. Phase 3 hostile-mode surfaced 3 additional faults (@13, @29, @40) that passed naive mechanic review. This is the same pattern as loc-state's systemic slug-invention surfacing — Phase 3 is doing structural work, not redundant work.

7. **Defended residuals are honest signal.** Phase 5 has 8 defended ratings (D-OK or D-PARTIAL) and one rubric-gap flag (@60 body-charge POV). All survived rubric-grounded scrutiny without rating changes. A clean 100% with defended caveats is more shippable than an over-revised 100% that papered over real ambiguities.

---

## Residual caveats (from Phase 5)

Five items the auditor flagged before declaring shippable:

1. **@33 axis-citation correction (mandatory pre-ship — applied in shipped file).** Rubric reversal-proximity language is action-forward; does not admit negative events. @33 stays at 2 on stakes-visibility alone. Annotation in `active-project/theater/facets/tensometer.md` corrected.

2. **Annotations at @39, @48, @64 must survive into filed facet (mandatory — applied).** The cross-facet contract distinctions are invisible without the inline notes. Filed facet retains annotations.

3. **2-rung frequency soft-fail notation (mandatory — applied).** Filed facet header records the 79.2/15.6/5.2 distribution and notes that the 2-rung breach is honest revision, not miscalibration. Protects against future auditor reopening.

4. **Body-charge POV scope is a V2 rubric gap (V3 followup).** @60 defended on plain rubric text but exposes an ambiguity: are body-charge axes POV-restricted to the protagonist, or open to antagonist posture? V3 rubric revision should add explicit scope statement. No action on shipped facet; flag for rubric maintenance.

5. **@1-@22 anchor-sparseness producer note (downstream warning, no action required).** Loudness, memory, and audience-interest authors should be informed the approach zone has no tensometer 2-anchors. A future screen-writer kickback for additional charged beats in the approach is a producer observation, not a shippability blocker.

---

## What needs doing next (if continuing)

1. **Backport explicit cross-facet contract to loc-state package.** Loc-state has implicit consumers (stitcher, state-updates) but no explicit contract section. Add one. (~1 paragraph in `design/shoot-v2/locstate-tuning-package.md`.)

2. **Pilot the tensometer pipeline on a second episode (s01e02 or s01e03) for stretch-sample.** s01e01 is 77 beats; e03 is 232. Verify the rubric scales — particularly that the frequency-band test holds as the corpus grows, that the cross-facet contract survives across multi-scene episodes, and that the dramatist's two-pass authoring stays tractable at episode lengths >150 beats.

3. **Address V2 rubric gaps (V3 revision).** Two known gaps: body-charge POV scope (@60), and reversal-proximity treatment of negative events (@33). V3 should explicitly close both.

4. **Pilot the next facet.** Open candidates per the original sequence: narrator interest-flags (POV-character writer-fork — closer to dialogue's pattern; can use dialect audience for narrator voice), or state-updates (split studio + dialogue-writer-fork — most operationally important for shoot-v2 because of canonical-memory write-back).

5. **Consider whether the curve-shape rubric should retroactively apply to other multi-anchor facets.** Loc-state had no curve-shape verdict. Should it? An entire episode's loc-state file *is* a kind of environmental curve; flat episodes (no environmental change) are structural failures. Worth exploring as a process improvement.

---

## Artifact map

### Authority
- Rubric: `design/shoot-v2/rubric-tensometer.md` (V2 locked)
- Schema: `schemas/facet.schema.md` (tensometer section)
- Process doc: `design/shoot-v2/facet-tuning-process.md`

### Phase 0
- Corpus selection: `design/shoot-v2/tensometer-corpus.md`

### Phase 1
- Naive baseline: `design/shoot-v2/phase1-tensometer-baseline-naive.md`
- V1 lenient review: `active-project/staff/auditor/phase1-tensometer-v1-review.md`
- V2 strict review: `active-project/staff/auditor/phase1-tensometer-v2-review.md`

### Phase 2
- Writer-fork output: `design/shoot-v2/phase2-tensometer-output.md`
- Phase 2 audit: `active-project/staff/auditor/phase2-tensometer-audit.md`

### Phase 3
- Adversarial seams: `active-project/staff/auditor/phase3-tensometer-seams.md`

### Phase 4
- Defense/revise: `design/shoot-v2/phase4-tensometer-defense.md`

### Phase 5
- Final adjudication: `active-project/staff/auditor/phase5-tensometer-final.md`

### Shipped
- Locked tensometer facet: `active-project/theater/facets/tensometer.md` (s01e01, 77 entries, READY-WITH-CAVEATS)

### This package
- `design/shoot-v2/tensometer-tuning-package.md`

---

## Co-deployment note

Per the dialogue and loc-state packages: writer + reviewer ships as a co-deployed unit. For tensometer:

- **Writer:** dramatist with rubric, calibration anchors, and the two-pass authoring discipline (per-beat → curve-shape audit). Authors scalars OR refuses with rubric citation OR kicks back to screen-writer with named structural gaps.
- **Reviewer:** single mechanic auditor with the rubric as authority. Per-entry verdicts (CORRECT / MISRATED-{up|down}-by-N) AND curve-shape verdict (SHAPE-OK / SHAPE-FAIL) AND cross-facet contract pre-ship check.
- **Adversarial pass (Phase 3):** same auditor in hostile mode, one strongest seam per non-1 entry plus one curve-level seam. Catches what passes naive mechanic review.

The three-part output (per-entry + curve-shape + contract-check) is not separable. The two halves (writer + reviewer) are not separable. Ship together, version together.

The dialect audience (`dark-fantasy-reader`, `pulp-enthusiast`, `worm-canon-pedant`) is **not** part of the tensometer pipeline. Tensometer is mechanic-dense (axis tests under rubric authority), not taste-dense. STM verified clean (the dialect audience never fired during this run).
