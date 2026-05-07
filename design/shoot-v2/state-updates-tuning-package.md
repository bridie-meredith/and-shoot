# State-Updates Facet Tuning — Final Package

End-to-end pipeline run for the state-updates facet, applying the five-phase tuning process from `design/shoot-v2/facet-tuning-process.md`. Run 2026-05-07.

**Headline:** locked V2 rubric + split authorship (studio + per-character dialogue-writer-forks) + single mechanic auditor produces a co-deployable pipeline at **13/13 = 100%** rubric-compliance after one revise round on s01e01 (77 beats). Trajectory: V1 lenient = 78.9% → V2 baseline = 6.7% → Phase 2 = 76.9% → Phase 5 = 100%. Lift from baseline: **+93.3pp** (largest absolute lift to date). Four pre-ship caveats; one mandatory margit referral for prop card authoring.

This is the first **split-authorship facet** tuned end-to-end. The pipeline pattern is now demonstrated across binary (loc-state), enumerated (dialogue), scalar (tensometer), free-text-content-with-curve (narrator-interest), AND structural-delta-with-split-authorship (state-updates) facet types.

---

## Trajectory

| Round | Stage | Author(s) | Reviewer | Result | Notes |
|---|---|---|---|---|---|
| 0 | Corpus prep + rubric author | — | — | 12 stratified intents, V1 rubric authored | Decision matrix exercises target × authorship × verdict |
| 1 — V1 lenient | Form-only review of naive baseline | naive (rubric-blind) | mechanic auditor | **71/90 = 78.9%** | Form rejects on invented-fields (gaze-target, attention-target, speech-target, weight, activity, etc.) |
| 1 — V2 strict | Full rubric on naive baseline | naive (rubric-blind) | mechanic auditor | **6/90 = 6.7%** | Baseline-to-beat. Six systemic faults named: invented-field epidemic, registration-as-state, density-on-flat, cross-POV writing, transient-as-state, drift-old |
| 2 — Writer-fork (split) | studio + Taylor fork + Edric fork (parallel, blind) | three forks | mechanic auditor | **10/13 = 76.9%** | Lift from 6.7 = **+70.2pp**; SHAPE-OK; 1 INCORRECT (cottage-door drift-old), 3 FLAG, 2 SKIP-MISSED |
| 3 — Adversarial seams | Same auditor, hostile mode | — | — | 25 seams (11 STRONG / 13 MODERATE / 1 THIN) | Surfaced prop-slug authority + chain-dependency-collapse (load-bearing on ID-2 ledger first-touch) |
| 4 — Defense or revise | Three forks, isolated | — | — | studio: 3 cull / 2 revise / 5 defend / 1 new fire; Taylor: 0 cull / 1 revise / 3 defend / 1 new fire (SM-1); Edric: 1 defend | Slug rename oc-* applied; @30 ledger entry culled (chain repair); @57 cottage-door culled |
| 5 — Final adjudication | Locked rubric | mechanic auditor | **13/13 = 100%** | SHAPE-OK with density-alignment soft-fail (notation); READY-WITH-CAVEATS |

**Lift comparable to or stronger than prior runs:**

| Facet | Baseline V2 | Final | Lift |
|---|---|---|---|
| dialogue | 40% | 100% | +60pp |
| loc-state | 53.8% | 100% | +46.2pp |
| tensometer | 50.6% | 100% | +49.4pp |
| narrator-interest | 22.2% | 100% | +77.8pp |
| **state-updates** | **6.7%** | **100%** | **+93.3pp** |

Largest absolute lift to date — function of the highest baseline-contamination ceiling across all five facets. State-updates has the highest signal-to-noise ratio because the naive author's dominant failure mode (invented-field epidemic + registration-as-state) is structurally at odds with the rubric's narrowest authority surface. The naive author can't stumble into compliance; once the rubric is internalized, the writer either fires correctly or refuses.

---

## What the user-supplied requirements added

The user-named structural addition for this run was **"split authorship: studio for environment/prop, dialogue-writer-fork for actor-state"** plus the explicit POV-restriction rule that narrator-interest's revised @52 baked into the cross-facet contract.

These reshaped the rubric:

### Split-authorship architecture as authority surface

The rubric introduces an **authorship axis** alongside the target axis:

- **`studio.*` and `prop:*`** — studio's authority. Includes prop holder-changes (props are studio's domain regardless of who is holding them).
- **`actor:<character>.*`** — that character's dialogue-writer-fork's authority. POV-restricted: each fork writes its own actor-state and only its own.

Cross-license writing is an authority violation (anti-pattern #2). This means the rubric is the **same** for all authors but the **authoring license** partitions the entry-space by target. One rubric, two-or-more writers, one shared cross-facet contract.

### POV-restriction inherited from narrator-interest

Narrator-interest's @52 fire ("the count of allies in the yard drops to one") is Taylor's *perception* of Mira's disengagement. The narrator-interest revised cross-facet contract baked in the rule: **POV-character perception of non-POV state is narrator-interest's territory; canonical state on non-POV characters is the non-POV fork's authority.** State-updates was the consumer-side test of this rule.

Phase 5 verified: Taylor fork wrote ZERO non-POV actor-state entries despite seam-pressure to expand into the @52 ally-count carve-out (the `actor:taylor.allies-in-yard-count` field-extension was considered and rejected). The rule held end-to-end.

### Cross-facet contract as ship-gate

State-updates is the consumer-side validator for tensometer's @64 strong-expect / @39 forbidden contracts and narrator-interest's POV co-citation requirement. The Phase 5 audit's cross-facet check is mandatory and blocking; an entry that violates either upstream contract cannot ship.

Phase 5 verification:
- @39 forbidden: 0 fires. ✓
- @64 strong-expect: 2 fires (studio + Taylor). ✓
- POV co-citation: 4/4 actor:taylor.* fires have narrator-interest entries on the exact `@<beat>`. ✓

### Field-extension protocol as authority safety-valve

State-updates is the first facet where the writer routinely needs **fields that don't yet exist on the target's schema** (administrative-status, knowledge.record-state, mask-state). The rubric's §"Field-extension protocol" admits these with documented justification, but flags any extension that's actually a perception or stylistic flourish (mood, register, voice-tone are NOT tracked-state).

Phase 5 verified: 7 of 13 entries are field-extensions; all 7 are tracked-state-aspects with documented baselines. Zero perception-as-state contamination in the shipped file.

---

## What worked

1. **The five-phase pattern transfers to split-authorship facets.** Same trajectory shape as prior runs: low naive baseline → ~75–90% writer-fork → 100% post-revise. The pipeline pattern is now general across single-author binary/scalar/free-text facets AND multi-author structural-delta facets. The split-authorship test was the user-named load-bearing structural risk for this run; the pipeline absorbed it.

2. **Single mechanic auditor across multiple writers held.** Despite three forks producing entries with different authority surfaces, one auditor with the locked rubric produced consistent verdicts. No need for per-author-class reviewers. The auditor's cross-author dependency check at Phase 5 was the only place the auditor crossed fork boundaries; the per-entry verdicts could be produced fork-by-fork without contamination.

3. **Phase 3 adversarial seams caught the load-bearing structural fault.** Phase 2 audit verdicted studio's output 7/8 CORRECT on its own entries; Phase 3 hostile mode surfaced the prop-slug authority issue (`prop:letter`, `prop:district-ledger` lacking `oc-` prefix and warehouse documentation) which propagated through 6 of 8 studio entries simultaneously. Same Phase-3-does-structural-work pattern as prior runs (loc-state slug-invention, tensometer adjacency, narrator-interest composite-channel overcount, foreknowledge-clamp back-loading). Phase 3 is doing real work; not redundant with Phase 2.

4. **Chain-dependency seam classification is novel for this facet.** State-updates entries form chains (the letter holder chain @38→@40→@45; the ledger taylor-entry chain @48→@64). Seam attacks on the chain-seed (@30 ledger first-touch ID-2) propagate through downstream entries. Phase 4 fixer must handle chain repair atomically: the cull of ID-2 automatically repairs ID-8's `<old>=pending` per calibration anchor. The auditor explicitly flagged this propagation in Phase 3; Phase 4 honored it.

5. **Floor defense on calibration anchors held.** Taylor fork's T1 @39 refusal (held-against-turn forbidden) and T5 @52 refusal (cross-POV trap) were rubric-correct; Phase 5 confirmed both. The studio fork's S6 @43 refusal (pre-empting the @45 flip) and the studio's culled @57 cottage-door (no proto-line evidence) were also rubric-correct refusals. Sparsity is load-bearing for state-updates because each entry is a canonical-memory write — over-firing corrupts memory.

6. **Field-extension protocol absorbed naturally.** No friction. Forks declared extensions in trailing comments per rubric §"Field-extension protocol"; auditor verified each as tracked-state-aspect not perception. The pattern likely transfers to feeling-flags and memory-flags where similar field-extension needs will surface.

7. **No dialect audience needed.** State-updates is mechanic-dense, not voice-dense. Skipping the dialect audience (per the locstate precedent) preserved their calibration for dialogue/prose/narrator-interest work. STM verified clean across the run.

8. **Hard fences held.** Zero Earth-Bet proper noun leaks in field values, descriptions, or extensions. All field-extensions defensible from the variant card and persona card.

---

## Residual caveats (from Phase 5)

Four items the auditor flagged before declaring shippable:

1. **Margit referral (mandatory pre-s01e02 follow-up; not blocking s01e01 ship).** `prop:oc-letter` and `prop:oc-district-ledger` are project-original props with no card in `cards/props/`. Phase 4 added `oc-` prefix per rubric §"Field-extension protocol" with explicit `# oc-flag` notation in the shipped file. Margit should author both prop cards before s01e02 authoring begins; both props recur as the season's identity-document and administrative spine respectively. Recommended schemas named in the shipped facet file.

2. **Density-alignment soft-fail (notation; applied to shipped file).** 1.46× (non-1-zone vs 1-zone fires-per-beat) vs. 2× rubric minimum. Driven by chain-flip-beat distribution: state-updates fires on the *mechanical* flip beat (e.g., the letter handover @40/@41/@45) even when the registration peak is at an adjacent non-1 beat (@38). This is structural to a flip-beat facet, not contaminating. The 2× heuristic was inherited from narrator-interest where peak/transition density IS the load-bearing curve test; for state-updates the chain-distribution argument defends a relaxed expectation. Future facet rubrics may want to specify whether the heuristic is peak-aligned (narrator-interest) or flip-beat-aligned (state-updates).

3. **Edric `<old>` baseline grounding (advisory; future episodes).** Edric's `<old>=yard (near sept door)` at @57 is project-setup-baseline-inferred; corroborated by @54 + @57 proto-line context but not in a formal s01e01-open state file. Future episodes should formalize Edric's project-setup state in a way that admits canonical-baseline references without re-derivation. Same pattern likely applies to other non-POV actors (mira, officer, clerk) when they first receive state-updates in future episodes.

4. **@77 cluster density (advisory; future authoring).** Two `actor:taylor-hebert-westeros.*` fires on a single beat (sublocation + mask-state) is the file's densest single-beat actor-state flip. Both are rubric-correct and narrator-interest co-cited; the cluster is honest. Watch for pattern across future episodes — three or more multi-fire single-beat actor-state clusters across a season would signal the rubric should mandate distribution across surrounding beats. For s01e01, the cluster is the episode-close compound transition (sept-threshold-cross + mask-thin) and the simultaneity is structural.

---

## What needs doing next (if continuing)

1. **Pilot state-updates on s01e02 or s01e03 for stretch-sample.** s01e01 is 77 beats; e03 is 232. Verify the rubric scales — particularly that the field-extension declarations carry forward cleanly (Taylor's administrative-status, knowledge.record-state, mask-state, sublocation should now have s01e01 closing values as project-open baselines for s01e02), that the chain-dependency review remains tractable as more chains accrue, and that cross-author dependency checks scale to longer episodes with more actor forks active.

2. **Pilot the next facet in sequence.** Open candidates:
   - **memory flags** (POV-character writer-fork; closest pattern transfer to narrator-interest; uses narrator-interest as anchor per the locked cross-facet contract; expected to be lower-leverage but tractable).
   - **loudness flags** (studio-authored, sparse, gates on tensometer ≥ 2 per locked tensometer cross-facet contract). First consumer-side test of tensometer's gate-on-2 contract from the consumer side, AND first consumer-side test of narrator-interest's loudness co-citation expectation. Likely simplest remaining facet.
   - **feeling flags** (non-POV character writer-fork; pattern transfer from state-updates' actor-fork pattern to a free-text-content variant). Higher complexity than memory or loudness; defer until at least one of those is tuned.

3. **Address residual caveats.** Margit referral for prop card authoring (caveat-001 — mandatory pre-s01e02); Edric baseline formalization (caveat-003 — advisory); @77 cluster pattern monitoring (caveat-004 — advisory across future episodes); density-alignment soft-fail notation (caveat-002 — already applied).

4. **Backport split-authorship pattern to dialogue and feeling-flags rubric drafts.** Dialogue's per-category-fork pattern is structurally similar to state-updates' per-character-fork pattern; the cross-author dependency check at Phase 5 may be a useful addition to the dialogue pipeline when multiple speakers' lines interact in a beat. Feeling-flags will need the per-character-fork pattern by design.

---

## Artifact map

### Authority
- Rubric: `design/shoot-v2/rubric-state-updates.md` (V2 LOCKED 2026-05-07)
- Schema: `schemas/facet.schema.md` (state-updates section)
- Process doc: `design/shoot-v2/facet-tuning-process.md`
- Cross-facet authorities: `active-project/theater/facets/tensometer.md`, `active-project/theater/facets/interest-narrator.md`

### Phase 0
- Corpus selection: `design/shoot-v2/state-updates-corpus.md`
- Rubric draft (V1 → V2): `design/shoot-v2/rubric-state-updates.md`

### Phase 1
- Naive baseline (rubric-blind): `design/shoot-v2/phase1-state-updates-baseline-naive.md`
- V1 + V2 review: `active-project/staff/auditor/phase1-state-updates-baseline-review.md`

### Phase 2
- Stratified intents (full): `design/shoot-v2/phase2-state-updates-intents.md`
- Stratified intents (writer-blind): `design/shoot-v2/phase2-state-updates-intents-blind.md`
- Studio fork output: `design/shoot-v2/phase2-state-updates-output-studio.md`
- Taylor fork output: `design/shoot-v2/phase2-state-updates-output-taylor.md`
- Edric fork output: `design/shoot-v2/phase2-state-updates-output-edric.md`
- Phase 2 audit: `active-project/staff/auditor/phase2-state-updates-audit.md`

### Phase 3
- Adversarial seams: `active-project/staff/auditor/phase3-state-updates-seams.md`

### Phase 4
- Studio defense/revise: `design/shoot-v2/phase4-state-updates-defense-studio.md`
- Taylor defense/revise: `design/shoot-v2/phase4-state-updates-defense-taylor.md`
- Edric defense: `design/shoot-v2/phase4-state-updates-defense-edric.md`

### Phase 5
- Final adjudication: `active-project/staff/auditor/phase5-state-updates-final.md`

### Shipped
- Locked state-updates facet: `active-project/theater/facets/state-updates.md` (s01e01, 13 entries, READY-WITH-CAVEATS)

### This package
- `design/shoot-v2/state-updates-tuning-package.md`

---

## Co-deployment note

Per dialogue, loc-state, tensometer, and narrator-interest packages: writer + reviewer ships as a co-deployed unit. For state-updates, the unit has FOUR components reflecting the split-authorship architecture:

- **Writer (studio):** studio fork in state-update authoring mode. Loads: this rubric, locked tensometer, locked narrator-interest, locked location-state (soft alignment), proto-line file, studio state schema, relevant location/prop cards. Authors `studio.*` and `prop:*` entries OR refuses with rubric citation. Does NOT author actor:* entries.

- **Writer (per-character dialogue-writer fork):** the same fork that writes a character's dialogue, in state-update output mode. Loads: this rubric, locked tensometer, locked narrator-interest (mandatory co-citation check for POV character), proto-line file, the character's persona/state/behavior cards. Authors `actor:<that-character>.*` entries OR refuses. Does NOT author other actors, studio, or prop entries.

- **Reviewer (mechanic auditor):** single mechanic auditor with the rubric as authority. Per-entry verdicts (CORRECT / INCORRECT-{class}); skip verdicts (SKIP-CORRECT / SKIP-MISSED); cross-author dependency check; cross-facet contract verification (tensometer @39/@64; narrator-interest POV co-citation); curve-shape verdict (SHAPE-OK / SHAPE-FAIL with named caveats). The auditor crosses fork boundaries only at the Phase 5 cross-author dependency check.

- **Adversarial pass (Phase 3):** same mechanic auditor in hostile mode, one strongest seam per entry across reality / authority / frugality / cross-facet, plus per-refusal fire-justification seams, plus a file-level seam and a curve-level seam. Catches what passes naive mechanic review.

The four parts are not separable. The split writers' affirmative-citation discipline (target + field + chain-grounded `<old>` + cross-facet co-citation) only works because the mechanic auditor tests citations and chains. The mechanic auditor's cross-author dependency check only works because the writers honor authorship boundaries. The adversarial pass surfaces what the others accept; without it, prop-slug authority and chain-seed faults ship invisible.

The dialect audience is **NOT** part of the state-updates pipeline (per the locstate precedent: state-updates is mechanic-dense, not voice-dense). Their calibration is reserved for dialogue/prose/narrator-interest work. STM verified clean across this run.

The split-authorship pattern is the structural addition for this facet. It is the authoring-time enforcement of the POV-restriction rule that narrator-interest's revised @52 baked into the cross-facet contract. Run end-to-end, the pattern held: no cross-license writing in any of the three forks' Phase 2 outputs; no chain inconsistency at the Phase 5 cross-author check; the @52 ally-count carve-out tempted the Taylor fork in Phase 4 free-add evaluation but was refused on rubric grounds. The constraint that narrator-interest planted across the facet boundary is now load-bearing for state-updates ship.
