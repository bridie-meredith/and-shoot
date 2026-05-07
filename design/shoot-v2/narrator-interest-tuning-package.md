# Narrator-Interest Facet Tuning — Final Package

End-to-end pipeline run for the narrator-interest facet, applying the five-phase tuning process from `design/shoot-v2/facet-tuning-process.md`. Run 2026-05-06.

**Headline:** locked V2 rubric + dialogue-writer Taylor-POV fork (interiority output mode, two-pass author) + mechanic auditor + dialect audience (voice-fidelity-only mode, hybrid gate) produces a co-deployable pipeline at **20/20 = 100% mechanic + 20/20 = 100% dialect** on s01e01 (77 beats), after one revise round. Combined gate passes both reviewers independently. Behavior-pack-as-rubric-authority (the user's mid-Phase-0 nudge) is the structural addition for this facet. Dialect audience reactivated cleanly for the right facet without bleeding into mechanic-domain adjudication — independent signal confirmed in 4 of 5 flagged entries.

---

## Trajectory

| Round | Stage | Reviewer | Result | Notes |
|---|---|---|---|---|
| 0 | Corpus prep + rubric author | — | s01e01 (77 proto-lines), V2 rubric authored with behavior-pack-as-authority | No prior narrator-interest file; baseline must be synthesized |
| 1 — V1 | Lenient form-only review | mechanic auditor | 51/63 = 81.0% | Baseline ceiling; semicolon-spine drops 12 |
| 1 — V2 | Strict review of naive baseline | mechanic auditor | **14/63 = 22.2%** | Baseline to beat; SHAPE-FAIL (81.8% density vs 15-25% target; 6 systemic faults named) |
| 2 — Writer fork | Taylor-POV fork blind to baseline, rubric-aware | mechanic auditor | **16/18 = 88.9%** | Lift from 22.2 = **+66.7**; SHAPE-OK; 2 SKIP-MISSED flagged |
| 2 — Writer fork | Same output | dialect audience (voice-only) | **14/18 = 77.8%** + 2 MIXED | Independent gate; 2 VOICE-FAIL (@43 figurative-weight, @77 meta-vocab); 2 VOICE-MIXED (@60 trailing fragment, @64 dangling preposition) |
| 2 — Combined | Both gates required | — | **12/18 = 66.7%** | The strictly-clean intersection |
| 3 — Adversarial seams | Same auditor, hostile mode | — | 6 STRONG / 7 MODERATE / 3 THIN seams + 1 STRONG curve seam | Surfaced 4 additional faults Phase 2 audit accepted (cost+eyes composite, foreknowledge-clamp back-loading, @11 plot-importance, @52 cross-facet POV-state mismatch) |
| 4 — Defense or revise | Same Taylor-POV fork | — | 7 revise + 11 defend + 2 add (@48, @37) | All defenses rubric+behavior-pack cited; curve seam repaired by @48 add |
| 5 — Final adjudication | Same locked rubric | mechanic auditor | **20/20 = 100%** | SHAPE-OK with band soft-fail (26.0%); READY-WITH-CAVEATS (4 residuals) |
| 5 — Final adjudication | Same locked rubric | dialect audience | **20/20 = 100%** | SHIP; both prior VOICE-FAILs resolved; hard-fence verified on @48 |
| 5 — Combined | Both gates | — | **20/20 = 100%** | Strict gate. Co-deployment confirmed. |

Lift comparable to or stronger than prior runs: dialogue +54, loc-state +46, tensometer +49, **narrator-interest +77.8** (largest single-phase lift to date — function of higher contamination ceiling on the naive baseline because narrator-interest has the highest signal-to-noise ratio of any facet to date: density-on-flat is the dominant naive contamination, and the baseline fired on 81.8% of beats).

---

## What the user-supplied requirements added

User mid-Phase-0 nudge: "make sure to consider behavior pack for narrator" — and a frame correction during rubric authoring: "not necessarily every line either. just highlight the stuff that narrator would care about... end result is to give more weight to the focused elements and basic nothing for the rest."

These reshaped the rubric:

### Behavior-pack-as-rubric-authority

The behavior pack (`cards/dialects/taylor-hebert.card.md` + `cards/dialects/taylor-hebert-westeros.card.md`) is the explicit authority for what counts as "Taylor noticing this." The rubric's perceptual-access channels (passive fauna-feed, eyes-to-exits, pre-calc, cost-tracking, refusal-to-look, mask-thin, foreknowledge-clamp, fauna-track tilt, age-mismatch) come straight from the behavior pack §"Voice tells" and §"Non-verbal tics" with project-variant overlays from the Westeros card.

**This means the rubric is POV-character-specific.** Each project's POV character gets its own narrator-interest rubric instance because the behavior pack is the authority. The rubric's structure (3 axes + anti-patterns + curve-shape + cross-facet contract) transfers across POV characters; the channel list, voice-fidelity samples, and calibration anchors do not.

### Spotlight-not-ledger framing

Original Phase 0 draft of the rubric framed narrator-interest as "what the POV character notices about each beat." The user's correction reframed it: **fires mark beats Taylor's attention actually lands on; everything else stays silent and gets baseline render-weight (or compression). The contrast between fired and silent beats is the signal the stitcher consumes.**

Reshaped rubric components:

- **Spotlight contract added at top** of §"What narrator-interest is for". The stitcher reads fires as render-weight; if every beat fires, there is no weight gradient and the spotlight has no value.
- **Earning axis simplified.** The test is "does she care about this beat enough that a reader should weigh it more than the surrounding beats?" Triggers (transitions, peaks, behavior-pack triggers) are the canonical reasons attention lands, not the test itself.
- **Density target lowered** from initial 25-45% draft to **15-25%** target band. Spotlight, not ledger.
- **No-contrast firing added as anti-pattern** (anti-pattern #9). Saturating the file destroys the gradient.

### Hybrid mechanic + dialect-audience reviewer combination

User explicitly named the test for this run: dialect-audience reactivation as a real test of whether the audience can come back online for the right facet without bleeding into mechanic-facet adjudication. Reshaped review pipeline:

- **Mechanic auditor:** form, perceptual access, earning, anti-pattern check, curve-shape, cross-facet contract.
- **Dialect audience:** voice fidelity ONLY. Worm-canon-pedant primary (calibrated to Taylor's base card), dark-fantasy-reader and pulp-enthusiast secondary.
- **Independent gates.** Both must pass for ACCEPT. Either reject = revise. They cannot substitute.

Phase 5 verdict on dialect audience interaction (per auditor): **independent signal confirmed in 4 of 5 flagged entries.** The dialect audience caught voice failures the mechanic audit missed or underweighted at Phase 2 (@43 figurative-weight, @60 trailing fragment, @64 dangling preposition); the mechanic audit caught a form failure outside dialect's scope (@63 semicolon-spine). One redundant signal at @77 (expected for a clear vocabulary violation). **No bleeding of dialect audience into mechanic-domain adjudication detected.** Co-deployment architecture confirmed working.

---

## What worked

1. **The five-phase pattern transfers to free-text-content facets with hybrid review.** Same trajectory shape (~22% baseline → ~89%/78% writer-fork on each gate → 100% on both gates post-revise) as prior runs. The pipeline is now demonstrably general across binary (loc-state), enumerated (dialogue), scalar (tensometer), and free-text-content-with-curve (narrator-interest) facet types.

2. **Behavior-pack-as-rubric-authority is the right structural addition.** Where loc-state's authority was the locations INDEX and tensometer's was 3-axes-plus-curve, narrator-interest's authority is the POV character's behavior pack. The pack pre-enumerates the perceptual channels and voice signatures, which makes the rubric short and the failure modes specific. This pattern likely transfers to feeling-flags (non-POV character behavior pack as authority) and audience interest-flags (per-persona card as authority).

3. **Spotlight framing prevented density-on-flat.** Phase 1 baseline fired on 81.8% of beats; Phase 2 writer-fork fired on 23.4% (in band, upper edge); Phase 5 final landed at 26.0% (1pt above band, defensible). The correction at rubric-author time (not after) saved a Phase 2 do-over.

4. **Hybrid review with independent gates produced complementary signal.** Mechanic catches form, earning, structural fault. Dialect catches voice-register, base-card-violation, doubled-register-leak. Phase 5's independent-signal verification is the test the user named: dialect audience caught 4 of 5 flagged faults that mechanic missed or underweighted, with one redundant. Neither reviewer was sufficient alone.

5. **Adversarial seams caught what mechanic audit missed, again.** Phase 2 mechanic accepted 16/18; Phase 3 hostile mode surfaced 4 additional structural faults (composite-channel overcount, foreknowledge-clamp back-loading, @11 plot-importance, @52 cross-facet POV-state mismatch) and re-pressed the dialect-audience MIXEDs to revise. Same pattern as loc-state's systemic slug-invention surfacing and tensometer's adjacency-fault surfacing — Phase 3 is doing structural work, not redundant work.

6. **SKIP-MISSED is real signal.** Phase 2 audit flagged @48 (foreknowledge-clamp on "provisional") and @37 (transition into peak) as MISSED. Phase 4 added both. The @48 add was the highest-leverage repair of the curve-level seam (foreknowledge-clamp back-loading) — adding mid-episode foreknowledge-clamp resolved the back-loading concern in one move.

7. **Two-pass authoring (per-beat + file-shape) absorbed the curve-shape requirement cleanly.** Same pattern as tensometer; the writer-fork's Pass 2 caught its own density alignment and channel diversity without auditor prompting. Pattern likely transfers to all curve-bearing facets.

8. **Hard fences held.** Zero Earth-Bet proper noun leaks, zero Dance specifics named. The @48 displacement-cue construction ("in another tongue") was specifically tested by Phase 5 dialect audience as a hard-fence near-miss; verified LICIT — circling without naming, per variant card §"Memory monuments / Earth-Bet monuments: Surface as displacement only."

---

## Residual caveats (from Phase 5)

Four items the auditor flagged before declaring shippable:

1. **Band soft-fail (notation, applied to shipped file).** 26.0% vs 15-25% target. +1pt excursion. Driven by mandated @48 SKIP-MISSED repair and rubric-earned @37 addition. Not a miscalibration; honest revision. If a downstream consumer requires strict band compliance, @37 is the soft-cut candidate (lands 19/77 = 24.7% inside band); @48 is mandatory and must not be dropped. Header notation applied.

2. **Loc-state cross-facet verification advisory.** The shipped file cites @4, @69, @77 as frame-turnover-aligned with location-state. Verify these align with the locked location-state file (not blocking; soft contract per rubric §"Cross-facet contract / Back-contract: Location-state alignment (soft)"). One-line check before stitcher consumes.

3. **@73 "stays the size" formula-watch (advisory; future episodes).** Phase 3 MODERATE seam: the @33 / @73 echo construction ("stays the size [X]") could become a formula across episodes. For s01e01 it is the doubled-register channel exercising consistently under matched displacement triggers; for the project as a whole, monitor — three or more "stays the size [X]" constructions across the season is a kickback.

4. **Composite-channel dominance note (advisory; future authoring).** Cost-tracking and eyes-to-exits operate as a composite (8 of 20 fires co-cite both); the file's middle is dominated by the composite. This is rubric-aligned for a confrontation-heavy episode; for episodes with different structures (interior-only, peer-only, low-confrontation), the composite-dominance pattern should not transfer by default. Future writer-fork instances should rebalance by episode shape.

---

## What needs doing next (if continuing)

1. **Pilot narrator-interest on a second episode (s01e02 or s01e03) for stretch-sample.** s01e01 is 77 beats; e03 is 232. Verify the rubric scales — particularly that the spotlight density holds as the corpus grows, that doubled-register visibility still lands at three registers across longer episodes, and that the cost+eyes composite-dominance is correctly episode-specific.

2. **Pilot the next facet in sequence.** Open candidates per the original sequence:
   - **state-updates** (split studio + dialogue-writer-fork — most operationally important for shoot-v2 because state updates write back to canonical memory at the cross-facet phase boundary). Tests whether the pipeline holds across split authorship.
   - **memory flags** (POV-character writer-fork like narrator-interest; closest pattern transfer; uses narrator-interest as anchor per cross-facet contract). Lower-leverage but tractable.
   - **loudness flags** (studio-authored, sparse, gates on tensometer ≥ 2). Simplest remaining facet; first consumer-side test of tensometer's cross-facet contract.

3. **Backport the behavior-pack-as-rubric-authority pattern to dialogue and feeling-flags.** Dialogue's per-category-fork already loads behavior pack; the rubric pattern of channel-enumeration could tighten its anti-pattern list. Feeling-flags (when authored) should follow the same pattern with the non-POV character's behavior pack as authority.

4. **Address residual caveats.** Loc-state alignment one-line check (caveat-002); future-episode formula-watch on @73 echo (caveat-003); composite-dominance advisory for non-confrontation episodes (caveat-004); band soft-fail notation (caveat-001 — already applied).

---

## Artifact map

### Authority
- Rubric: `design/shoot-v2/rubric-narrator-interest.md` (V2 locked)
- Schema: `schemas/facet.schema.md` (interest-narrator section)
- Process doc: `design/shoot-v2/facet-tuning-process.md`
- Behavior pack: `cards/dialects/taylor-hebert.card.md` + `cards/dialects/taylor-hebert-westeros.card.md`

### Phase 0
- Corpus selection: `design/shoot-v2/narrator-interest-corpus.md`
- Rubric (V1 → V2): `design/shoot-v2/rubric-narrator-interest.md`

### Phase 1
- Naive baseline (rubric-blind): `design/shoot-v2/phase1-narrator-interest-baseline-naive.md`
- V1 lenient + V2 strict review: `active-project/staff/auditor/phase1-narrator-interest-baseline-review.md`

### Phase 2
- Writer-fork output: `design/shoot-v2/phase2-narrator-interest-output.md`
- Mechanic audit: `active-project/staff/auditor/phase2-narrator-interest-audit.md`
- Dialect audience review: `active-project/audience/narrator-interest-phase2-review.md`

### Phase 3
- Adversarial seams: `active-project/staff/auditor/phase3-narrator-interest-seams.md`

### Phase 4
- Defense or revise: `design/shoot-v2/phase4-narrator-interest-defense.md`

### Phase 5
- Final mechanic adjudication: `active-project/staff/auditor/phase5-narrator-interest-final.md`
- Final dialect audience review: `active-project/audience/narrator-interest-phase5-review.md`

### Shipped
- Locked narrator-interest facet: `active-project/theater/facets/interest-narrator.md` (s01e01, 20 entries, READY-WITH-CAVEATS)

### This package
- `design/shoot-v2/narrator-interest-tuning-package.md`

---

## Co-deployment note

Per dialogue, loc-state, and tensometer packages: writer + reviewer ships as a co-deployed unit. For narrator-interest, the unit has three components:

- **Writer:** dialogue-writer fork for the POV character, in interiority output mode. Loads: base behavior card, variant behavior card, persona card, locked tensometer file (transition+peak alignment), locked location-state file (frame-turnover alignment, soft), this rubric, the corpus-selection note. Two-pass authoring discipline (per-beat → file-shape audit). Authors fires OR refuses with rubric citation OR kicks back to screen-writer with named structural gaps.

- **Reviewer (mechanic auditor):** single mechanic auditor with the rubric as authority. Per-entry verdicts (CORRECT / INCORRECT-{axis-or-anti-pattern}); skip verdicts (SKIP-CORRECT / SKIP-MISSED); curve verdict (SHAPE-OK / SHAPE-FAIL); cross-facet contract pre-ship check. Voice fidelity is checked at the axis level but the reviewer does not have the dialect audience's calibration to base-card register samples.

- **Reviewer (dialect audience, voice-fidelity-only mode):** worm-canon-pedant primary, dark-fantasy-reader and pulp-enthusiast secondary. Per-entry verdicts: VOICE-OK / VOICE-FAIL / VOICE-MIXED with citation to behavior-pack §. Domain restricted to voice fidelity; does not adjudicate firing decision, channel selection, earning, or cross-facet contract.

- **Verdict combination:** mechanic and dialect audience are **independent gates**. Both must pass for ACCEPT. They cannot substitute. Phase 5 verified this works as designed: 4 of 5 flagged entries had independent signal, 1 redundant (a clear vocabulary violation any reviewer would catch). No bleeding detected.

- **Adversarial pass (Phase 3):** same mechanic auditor in hostile mode, one strongest seam per entry plus one curve-level seam. Catches what passes naive mechanic review and presses dialect-audience MIXEDs to revise.

The four parts (writer + mechanic + dialect-audience + adversarial-pass) are not separable. The writer's affirmative-citation discipline (channel + trigger + signature) only works because the mechanic auditor tests citations. The dialect audience's voice-fidelity verdict only works because the writer produces entries that *demonstrate* voice signatures rather than merely avoid violations. The mechanic auditor's strict rubric is only meaningful because the writer can produce entries that demonstrate signatures rather than just avoid violations. The adversarial pass is what surfaces what the other three accept.

The dialect audience (`dark-fantasy-reader`, `pulp-enthusiast`, `worm-canon-pedant`) IS part of the narrator-interest pipeline — fidelity-only, voice-only, no scope creep into mechanic adjudication. Their calibration to Taylor's base-card voice was preserved across this run (no STM contamination from mechanic concerns). Phase 5 confirmed clean reactivation; STM verified clean across the run.
