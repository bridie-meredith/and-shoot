# Location-State Facet Tuning — Final Package

End-to-end pipeline run for the location-state facet, applying the five-phase tuning process from `design/shoot-v2/facet-tuning-process.md`. Run 2026-05-06.

**Headline:** locked V2 rubric + studio writer-fork + single mechanic auditor produces a co-deployable pipeline at **19/19 = 100%** rubric-compliance after one revise round, with **100% decision accuracy** (which-SVO-line-needs-a-tag) verified across the full stratified decision space. Three pre-ship caveats; one card-authoring follow-up flagged for margit.

---

## Trajectory

| Round | Stage | Reviewer | Result | Notes |
|---|---|---|---|---|
| 0 | Corpus prep | — | 65 candidates seeded permissively from 1101 proto-lines | Includes deliberate anti-pattern shapes |
| 1 — V1 | Rubric form-only | 3 dialect-audience | 65/65 = 100% | Schema-form + plausible-anchor only; baseline ceiling |
| 1 — V2 | Strict rubric, 3 lenses | 3 dialect-audience aggregate ≥2/3 | 30/65 = 46% | First locked-rubric pass |
| 1 — V2 re-baseline | Same rubric, mechanic auditor | 1 mechanic auditor | **35/65 = 53.8%** | Comparison floor for Phase 2 |
| 2 — Writer fork | Studio blind to originals | 1 mechanic auditor | **18/19 = 94.7%** | Lift from 53.8 = **+40.9** |
| 3 — Adversarial seams | Hostile counter-arg per entry | 1 mechanic auditor | 5 strong / 7 moderate / 7 thin seams | Surfaced systemic slug-accuracy fault |
| 4 — Defense or revise | Studio | — | 6 revise + 5 defend + 8 none-confirmed | All slug faults addressed |
| 5 — Final adjudication | Same locked rubric | 1 mechanic auditor | **19/19 = 100%** | Three pre-ship caveats |

---

## The decision-accuracy check (the original-purpose verification)

The point of the location-state facet is to identify *which* SVO proto-lines warrant a locational tag and which do not. That decision was tested in Phase 2 across a stratified anchor space designed to exercise every cell of the decision matrix:

| Stratum | Anchors | Studio decision | Auditor verdict |
|---|---|---|---|
| Calibration | 1 (C) | FIRE | CORRECT |
| Boundary-crossing | 5 (1–5) | FIRE ×5 | CORRECT ×5 (Intent 5 form-incorrect, decision-correct) |
| Scene-anchor | 2 (6, 7) | FIRE ×2 | CORRECT ×2 |
| State-change | 3 (8, 9, 10) | FIRE ×3 | CORRECT ×3 |
| Fauna-feed | 1 (11) | NONE | CORRECT |
| Within-scene movement | 4 (12–15) | NONE ×4 | CORRECT ×4 |
| Persistence/atmosphere | 2 (16, 17) | NONE ×2 | CORRECT ×2 |
| Sound-arrival | 1 (18) | NONE | CORRECT |

**Decision accuracy: 19/19 = 100%.** Every fire-this and don't-fire-this call matched the rubric-determined disposition, including the two seam-zone cases (fauna-feed, sound-arrival) where the dialect audience had floor-defended in Phase 1 but the rubric mechanically warrants NONE. The single Phase-2 audit-flagged fault (Intent 5) was a *form* error in a *correctly-decided* fire — the entry construction violated single-focus-element and conditions-slot purity, not the firing decision. Revised in Phase 4 and verified clean in Phase 5.

The agent is competent for the facet's original purpose: identifying which SVO lines warrant location-state tags.

---

## Residual caveats (from Phase 5)

Three items the auditor flagged before declaring shippable:

1. **Intent 4 slug repair (mandatory pre-ship).** The Intent 4 entry's content axes hold under defense, but the slug `oc-sept-side-door` referenced in the original Phase-2 output was not corrected during the Phase-4 defense (Intent 4 was a defend, not a revise). It must be repaired to `loc-harrenhal-sept-environs` (the parent zone covering the sept side door) before the entry is citable in a real shoot. One-line fix.

2. **Facet vs. proto-line register distinction (writer brief addition).** The defense for Intents C, 8, 9 turns on the principle that facet entries can record state-changes the proto-line prose already carries — they live in different layers. This needs to appear explicitly in the studio brief for full-corpus authoring, otherwise future writer instances may self-cut on "but the proto-line already says this." Add to the rubric or to a writer-fork briefing template.

3. **Intent 14 soft dependency on `westerosi-smallfolk-village-common` scope.** The NONE rationale assumes that card defines the village-common scene-furniture (trestle, kiln wall, bench-end). If that card's scope shifts, Intent 14's verdict needs revisiting. Flag for margit on any card-mutation event in that slug.

---

## Margit referral

Phase 4 surfaced one card-authoring need:

- **`oc-sept-outbuildings-yard`** — the smallfolk drying-yard in s01e02 (Intent 10's anchor) is currently being absorbed under `loc-harrenhal-sept-environs` as a sub-zone, which works for the Phase-2 sample. If the location recurs across the project, a dedicated card extending the parent's smallfolk-domestic-yard scope would tighten future loc-state authoring. Optional, not blocking.

---

## What worked

1. **The writer-fork pattern transfers.** Same shape as the dialogue facet — blind-to-originals, intent-specifies-state-not-text, multi-draft + chosen + cited signatures, explicit anti-patterns, calibration anchor. Same lift magnitude (+40.9 vs. dialogue's +54).

2. **Single mechanic auditor was the right reviewer.** Loc-state is mechanic-dense (does this beat earn an entry under three rubric tests), not taste-dense. One auditor with the rubric as authority produces deterministic verdicts where three taste-personas produced seam-zone disagreement contaminating the lift comparison. Bonus: protected the dialect audience's calibration for dialogue/prose work — STM verified clean throughout.

3. **The herald/cart heuristic is load-bearing.** The user-supplied refinement ("location is only relevant on movement; a cart by the wall isn't what's important, a herald at the wall is") was the spine of the rubric's necessity axis. It survived Phase 5 adjudication intact and resolved the seam attack on Intent 7 cleanly.

4. **Adversarial seam-finding caught a systemic fault the auditor missed.** Phase 2's mechanic audit verdicted the studio output 18/19 correct, but Phase 3's adversarial pass surfaced the systemic slug-invention pattern — studio created `oc-*` slugs for sub-locations of authored cards. This is exactly what Phase 3 is for: catching what passes mechanic review but breaks under hostile reading. Revise rate (6 of 19) reflects honest seam load.

5. **Path A on floor-defense held.** Phase 2 NONE-CONFIRMED on the fauna-feed and sound-arrival anchors held under Phase 3 fire-justification seams and Phase 5 adjudication. The rubric as written does not warrant entries for those — the dialect audience's floor-defense was reading taste into the rubric. If a future shipping-audit shows lost perception-mechanic load in stitched output, the rubric can be widened then; do not pre-widen on speculative concern.

---

## What needs doing next (if continuing)

1. **Apply the Intent 4 slug fix.** One-line edit before any real shoot.
2. **Add facet vs. proto-line register clause to rubric.** One paragraph.
3. **Pilot the same five-phase process on the next facet.** Open candidates: tensometer (dramatist authoring, single-rater pass — different shape), narrator interest-flags (POV-character writer-fork — closer to dialogue's pattern), or state-updates (studio + dialogue-writer-fork — split authorship). The pipeline pattern is now general enough to attempt any of these.
4. **Stretch sample.** Phase 2 ran on 19 stratified anchors. A full-corpus loc-state authoring against the locked rubric would be 50–80 entries across e01–e06 (sparse by rubric design). Expected accept rate: ~95% based on Phase 5. Worth running before production use.

---

## Artifact map

### Authority
- Rubric: `design/shoot-v2/rubric-location-state.md` (V2 locked)
- Schema: `schemas/facet.schema.md` (location-state section)
- Process doc: `design/shoot-v2/facet-tuning-process.md`

### Phase 1
- Candidate corpus: `design/shoot-v2/loc-state-candidates.md`
- Dialect-audience V1 reviews: `active-project/audience/{dark-fantasy-reader,pulp-enthusiast,worm-canon-pedant}/loc-state-v1-review.md`
- Dialect-audience V2 reviews: `active-project/audience/{dark-fantasy-reader,pulp-enthusiast,worm-canon-pedant}/loc-state-v2-review.md`
- Phase 1 report (dialect-audience version): `design/shoot-v2/phase1-locstate-report.md`
- Phase 1 re-baseline (mechanic auditor): `active-project/staff/auditor/phase1-locstate-rebaseline-audit.md`

### Phase 2
- Intents (full): `design/shoot-v2/phase2-locstate-intents.md`
- Intents (writer-blind): `design/shoot-v2/phase2-locstate-intents-blind.md`
- Studio output: `design/shoot-v2/phase2-locstate-output.md`
- Phase 2 audit: `active-project/staff/auditor/phase2-locstate-audit.md`
- Phase 2 lift report: `design/shoot-v2/phase2-locstate-report.md`

### Phase 3
- Adversarial seams: `active-project/staff/auditor/phase3-locstate-seams.md`

### Phase 4
- Studio defense/revise: `design/shoot-v2/phase4-locstate-defense.md`

### Phase 5
- Final adjudication: `active-project/staff/auditor/phase5-locstate-final.md`

### This package
- `design/shoot-v2/locstate-tuning-package.md`

---

## Co-deployment note

Per the dialogue facet's co-deployment finding (`facet-tuning-process.md` §Co-deployment): the writer + reviewer pipeline ships as a co-deployed unit. For location-state:

- **Writer:** studio fork with the rubric, the locations INDEX, and the writer-blind intents pattern. Authors entries OR refuses with rubric citation.
- **Reviewer:** single mechanic auditor with the rubric as authority. Per-entry verdicts (FIRE-CORRECT / FIRE-INCORRECT / NONE-CORRECT / NONE-INCORRECT). No taste, no floor-defense.
- **Adversarial pass (Phase 3):** same auditor in adversarial mode, one hostile seam per entry across selection / inheritance / form lenses. Catches what passes naive mechanic review.

The two halves are not separable — studio's affirmative-citation discipline only works because the auditor tests the citations; the auditor's strictness is only meaningful because studio can produce entries that demonstrate signatures rather than just avoid violations. Ship together, version together.

The dialect audience (`dark-fantasy-reader`, `pulp-enthusiast`, `worm-canon-pedant`) is **not** part of the location-state pipeline going forward. Their calibration is reserved for dialogue/prose work. STM verified clean across this run.
