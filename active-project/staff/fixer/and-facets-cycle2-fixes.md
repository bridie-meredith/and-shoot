# and-facets b01c10 cycle-2 fixes log

session: and-facets-b01c10-cycle2-fixes-round2
date: 2026-06-02
fixes-queued: 3
fixes-applied: 3

---

## Fix 1 — [sensory:7] @25 old-state unanchored
- entry: sensory:7 @25
- operation: REVISE
- callout: CONVERGENT — sensory-disambiguation-pedant + sensory-old-state-reader
- problem: old-state "ledger-accounting-writing-sound" unanchored — writing-sound ambient never established; cited anchors loc-state:7@20 and loc-state:8@23 name scene-D baseline as "still air, day's-end quiet"
- before (original callout text): `7 @25 sound: ledger-accounting-writing-sound -> silence # tag: drop`
- after (current file state): `7 @25 sound: end-of-day-station-quiet -> ledger-cover-close # tag: spike`
- old-state-anchor: `end-of-day-station-quiet` anchors directly to loc-state:7 @20 ("indoor station surface, still air, day's-end quiet") — verbatim match to baseline wording
- modality: sound (unchanged)
- tag: spike (cover closing is a discrete transient audible event; the quiet resumes after — correct spike not drop)
- old-state-anchor-trace: present in file § Old-state-anchor trace: "sensory:7 @25 end-of-day-station-quiet: anchors loc-state:7 @20 (scene-D baseline; 'indoor station surface, still air, day's-end quiet')"
- rubric check: rubric-sensory.md § Modality-inflection ACCEPT signature — "Anchored to a real perceptual baseline. The old-state matches the most recent location-state file's § sensory or § conditions field for the beat's location" — SATISFIED: old-state traces verbatim to loc-state:7 @20 baseline
- which callout: CONVERGENT sensory-disambiguation-pedant + sensory-old-state-reader
- verdict: REVISE-LANDED (applied in prior session; confirmed in place)
- note: ID sensory:7, anchor @25, and citation tokens unchanged

---

## Fix 2 — [mem:2] @24 doubled closing-simile
- entry: mem:2 @24
- operation: REVISE
- callout: CONVERGENT — worm-canon-pedant (memory AND interest-narrator) + metaphor-R2 AP4 corroboration
- problem: original text used "the record closing the same way the old architecture closed around bodies it never asked" — SAME "X closing the way Y closed" closing-simile structure as narrator:8 @24 ("the corridor closing behind him the way the channel closed over the entry"); mechanical doubling at the chapter's most sensitive anchor
- before (original callout text): `2 @24 the record closing the same way the old architecture closed around bodies it never asked -> cond-override-architecture-residue-122ac`
- after (current file state): `2 @24 the crossing is one more entry in the months of him she has held in the record without his leave, the architecture that does this to bodies it never asked doing it again in her hand -> cond-override-architecture-residue-122ac`
- rhetorical-form: "doing it again in her hand" — continuation/accumulation construction, NOT a "closing-the-way-X-closed" simile; structural rhyme with narrator:8 broken
- semantics preserved: override-architecture displacement (the architecture that does this to bodies it never asked); unconsented-instrumentation meaning (without his leave; bodies it never asked); accumulation register (months of him in the record)
- target-reference: cond-override-architecture-residue-122ac — unchanged
- khepri-absent check: no Earth-Bet proper noun in description or target-reference — FENCE HELD
- doubled-register: mem:1 @16 (clamp/monument) + mem:2 @24 (displacement) — doubled-register satisfied; mem:1 is the clamp, mem:2 is the displacement, neither naming the other's register
- which callout: CONVERGENT worm-canon-pedant (memory + interest-narrator) + metaphor-R2 AP4
- verdict: REVISE-LANDED (applied in prior session; confirmed in place)
- note: ID mem:2, anchor @24, citation token cond-override-architecture-residue-122ac unchanged; narrator:8 @24 left AS-IS per dispatch (Fix 2 resolves doubling by changing mem:2; narrator:8 remains the single closing-simile at @24)

---

## Fix 3 — [narrator:7] @16 inert spine-provision
- entry: narrator:7 @16
- operation: REVISE
- callout: cape-fic-reader
- problem: original text "the side-exit is the gap in the circuit geometry that accounts for the missing mark — one body leaves the lower-gate road without leaving the road, and the stone-post is the mechanism; she files the fixture as the board-state item that closes the deviation's open question" — "tactically inert": exists only to satisfy mem:1 @16 NI-spine, not as an earned attention-landing; "the stone-post is the mechanism" names the mechanism without saying what it's a mechanism OF; circuit-accounting register rather than apparatus-geometry recognition
- before: `7 @16 the side-exit is the gap in the circuit geometry that accounts for the missing mark — one body leaves the lower-gate road without leaving the road, and the stone-post is the mechanism; she files the fixture as the board-state item that closes the deviation's open question`
- after: `7 @16 the stone-post marks the geometry by which a body leaves the lower-gate road without the road registering a departure — the errand-corridor as a channel the circuit does not count; she files the fixture at the board-state cost the morning has just confirmed`
- attention-landing: Taylor's feed registers the stone-post as the specific geometry-point where a body exits the road without the road recording a departure — the disappearance-machinery recognition (the side-exit takes a body out without registering absence)
- information-asymmetry content: "the errand-corridor as a channel the circuit does not count" — names the information gap the stone-post's geometry creates; what the lower-gate road's circuit cannot track
- board-state content: "she files the fixture at the board-state cost the morning has just confirmed" — Taylor's active cost-pricing of the apparatus-geometry; concrete registration of what her attention does here (files, prices)
- mem:1 NI-spine: the reworded text carries the apparatus-geometry that empties a corridor (the disappearance-machinery the "old machinery" of mem:1's clamp leans on) — mem:1 @16 monument anchor INTACT; the stone-post as disappearance-apparatus now has genuine earned NI weight
- narrator:7 ID and @16 anchor: UNCHANGED
- narrator count: 7 fires — UNCHANGED (no entries trimmed or added)
- @24 closing-simile check: "the morning has just confirmed" — NOT a closing-simile structure; no "X closing the way Y closed" form; @24 doubling risk ABSENT
- khepri-absent fence: no Earth-Bet proper noun in text — FENCE HELD
- which callout: cape-fic-reader
- verdict: REVISE-LANDED

---

## Confirmation checks

- mem:1 @16 spine: INTACT — narrator:7 @16 rewording carries concrete apparatus-geometry weight; the monument (cond-kl-witch-label-formation-122ac) that leans on the stone-post as disappearance-apparatus now has an earned NI spotlight, not a circuit-accounting infrastructure entry
- narrator count: 7 fires (entries 1, 3, 4, 5, 6, 7, 8 in file) — UNCHANGED; 25.9% band-stretch documented and accepted per R2 note
- khepri-absent fence: checked on all reworded text — Fix 2 (mem:2 current text): no proper noun; Fix 3 (narrator:7 reworded text): no proper noun; FENCE HELD on both
- entry IDs unchanged: sensory:7, mem:2, narrator:7 — all IDs preserved
- anchors unchanged: @25, @24, @16 — all anchors preserved
- citation tokens unchanged: sensory:7 no citation token (sensory-flags schema does not use citation tokens); mem:2 -> cond-override-architecture-residue-122ac (unchanged); narrator:7 no citation token (NI entries do not carry citation tokens in this file)
- narrator:8 @24: left AS-IS per dispatch; remains the single closing-simile at @24
