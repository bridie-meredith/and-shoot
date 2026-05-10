final adjudication (TIGHTER AUDIENCE PATTERN): sensory facet, s01e01, post-Phase-4-defense
date: 2026-05-10
rubric: design/shoot-v2/rubric-sensory.md V2 (locked, unchanged)
mode: review; tighter-audience pattern (first end-to-end Phase F)
critics: sensory-disambiguation-pedant, sensory-modality-coverage, sensory-old-state-reader

---

## Per-entry adjudication

### sensory:1 @1 — `thermal: loft-pre-dawn-still -> dawn-cold-air  # tag: drop`

- disambiguation-pedant: ACCEPT. Proto-line is "taylor wakes in the loft" — "wakes" is bare; thermal modality matches a waking-skin perceptual axis. Action-verb self-charge clause does not apply (waking is not a thermal event).
- old-state-reader: ACCEPT. `loft-pre-dawn-still` derives from loc-state:1's `shutter-shut, loft-dark` (sealed enclosure inferable as still). The original "warmth" body-state inference is gone; no warmth claim is made.
- AGGREGATED: ACCEPT.
- Seam-closure: closes original (old-state-reader STRONG: invented warmth baseline). Revision withdraws the warmth claim and roots the baseline in loc-state:1's recorded conditions. No new fault introduced.

### sensory:2 @3 — `smell: workshop-shutter-shut-enclosed -> mordant-stir-sharp  # tag: up`

- disambiguation-pedant: ACCEPT-WITH-CAVEAT. Proto-line is "mother stirs the mordant pot" — "mordant" is borderline charged for a dyer's-trade reader (chemical sharpness is partially seeded by the technical noun). However, "stir-sharp" supplies the inflection-onset that "mordant pot" alone leaves ambient. Defensible; not a doubling. Caveat: the original MODERATE attack on partial redundancy was not directly addressed; only the old-state seam was.
- old-state-reader: ACCEPT. `workshop-shutter-shut-enclosed` traces near-verbatim to loc-state:1's `shutter-shut` condition. The loc-state-gap unanchoring is closed — old-state is now derived from loc-state:1 (most recent prior entry), not from the loc card's palette. The new clause's loc-state-gap failure mode is satisfied because loc-state:1 IS the prior anchor; @3 simply inherits forward.
- AGGREGATED: ACCEPT-WITH-CAVEAT.
- Seam-closure: closes original (old-state-reader STRONG seam). Disambiguation-pedant's MODERATE seam was not the strongest and was not surfaced for adjudication; carries forward as residual but not blocking.

### sensory:3 @8 — `light: dawn-shuttered-dim -> morning-daylight-cut-through  # tag: up`

- disambiguation-pedant: ACCEPT. Proto-line is "father opens the workshop shutter" — "opens" is an action-verb but its semantic content is mechanical (the act of unfastening), not perceptual (the light-quality that follows). The clause's example list ("light/open/ignite/extinguish") does include "opens" — narrow attack vector — but the pedant's own example renders "opens the shutter" as charged for onset only, and the delta `cut-through` is magnitude/quality, which the verb does not supply. Defense's reading aligns with the card's own action-verb clause: "charged for the onset, bare for magnitude and quality." Survives.
- old-state-reader: ACCEPT. `dawn-shuttered-dim` traces verbatim to loc-state:1's `dawn | shutter-shut, loft-dark`; new-state `morning-daylight-cut-through` near-verbatim-matches loc-state:2's "daylight cutting the workshop floor." Cleanest lineage in the file.
- AGGREGATED: ACCEPT.
- Seam-closure: closes original (disambiguation-pedant THIN, acknowledged "survives the gate").

### sensory:4 @60 — `light: workshop-dusk-closed -> tallow-lamp-glow-settle  # tag: up`

- disambiguation-pedant: REJECT-anchor-vacuum. Mechanical verification of @60: the proto-line file shows `60 [sensory:4]` — @60 has NO surface SVO, no verb at all. The defense correctly removed the fire from @58 (where "lights" self-charges), but @60 is not a bare-word anchor — it is a blank line whose only content is the citation back-pointer. The disambiguation gate asks "is the proto-line word bare?" and the answer for @60 is "there is no proto-line word." A sensory delta that fires on no-surface is structurally undefined under the bare-vs-charged gate; the gate cannot resolve. This is a new fault introduced by the revision: the action-verb self-charge problem was solved by moving the fire to a beat with no anchor word at all.
- old-state-reader: ACCEPT-WITH-CAVEAT. `workshop-dusk-closed` traces to loc-state:4 @58's `dusk | tallow-lamp-lit, shutter-shut`. Lineage is clean. Caveat: loc-state:4 is at @58, two beats prior; loc-state:5 is at @61, one beat after. @60 sits in a one-line gap where the lamp is established but the loft-vent state is not yet active. Old-state is anchored, but the new-state `tallow-lamp-glow-settle` describes a quality the loc-state record never explicitly distinguishes from `tallow-lamp-lit`. Under the loc-state-gap clause this is a soft flag, not a strong one — loc-state:4 is the prior anchor and the inheritance is forward.
- AGGREGATED: REJECT.
- Seam-closure: shifts. Original disambiguation-pedant STRONG seam ("lights" verb self-charge) is closed at @58. New seam introduced at @60: anchor-vacuum. The defense's claim that @60 "has no charged verb" is true but insufficient — a sensory fire requires a bare WORD, not the absence of a word. Recommended fix: relocate to @61 ("taylor reaches the pallet" — bare verb, loft-vent-open licenses lamp-glow leaking up) or restore @58 with the fire's delta narrowed to glow-quality only and the verb's self-charge accepted as redundant in the magnitude register only.

### sensory:5 @130 — `light: tallow-lamp-guttering-unsteady -> candle-steady-flame  # tag: up`

- disambiguation-pedant: ACCEPT. Proto-line "the candle catches" — "catches" is a weaker self-charger than "lights" (responsive event vs. agentive act); the `guttering-unsteady -> steady-flame` quality contrast is not carried by the verb. Defense's distinction (catches = wick-igniting mechanism; lights = deliberate illumination) is mechanically sound; the delta's work is in the steadiness register, which `catches` leaves bare.
- old-state-reader: ACCEPT. `tallow-lamp-guttering-unsteady` traces verbatim to loc-state:7's `tallow-lamp-guttering`; `candle-steady-flame` traces verbatim to loc-state:8's "candle flame the only steady light." Tightest lineage in the file.
- AGGREGATED: ACCEPT.
- Seam-closure: closes original (disambiguation-pedant THIN, acknowledged "survives the gate").

### sensory:6 @126 — `thermal: workshop-evening-settled -> room-chill-winter-candle-needed  # tag: drop`

- disambiguation-pedant: ACCEPT. Proto-line is "oc-craftsman-mother draws the winter-candle" — "draws" is bare for thermal (the verb names retrieval, not temperature). "Winter-candle" is a charged noun for cold-context, but the delta's work is the room-chill register that licenses the draw, which the noun alone does not carry (a winter-candle could be drawn for ceremonial reasons, stockpile-rotation, etc.; the thermal motivation is what the fire flags). Action-verb self-charge clause does not trigger — "draws" is not perceptually self-carrying for thermal.
- old-state-reader: ACCEPT-WITH-CAVEAT. `workshop-evening-settled` derives from loc-state:6 @92's `late-evening | tallow-lamp-lit, ledger-open` (the most recent prior loc-state). New-state `room-chill-winter-candle-needed` is licensed forward by loc-state:7 @126's `winter-candle-drawn` field. The lineage is bidirectional and clean. Caveat: "settled-warm" is implied (lamp burning in enclosed room), but loc-state:6 does not record temperature explicitly; the warmth baseline is inferred from architecture (lamp + enclosed = settled). This is a softer inference than sensory:1's revised baseline, which was anchored in sealed-stillness rather than warmth. Soft flag; not blocking.
- AGGREGATED: ACCEPT.
- Seam-closure: addresses file-level seam by adding thermal coverage to the lamp-lit half. Per-entry, the addition is structurally sound.

---

## File-level adjudication (modality-coverage)

Pre-add distribution: 3 light / 1 thermal / 1 smell / 0 sound / 0 tactile = 60% light, breaching the >50% single-channel hot-button.

Post-add distribution: 3 light / 2 thermal / 1 smell / 0 sound / 0 tactile = 50% light, exactly at threshold (not breaching).

Verdict: ACCEPT-WITH-CAVEAT. The >50% hot-button is technically cleared (50% ≤ 50%, not >). Thermal coverage now spans both halves of the episode (@1 dawn, @126 night), addressing the lamp-lit-half thermal gap that was the seam's secondary attack. Sparsity moves from 4.9% to 5.9% (6/102), still in the 3-6% target band.

Caveats:
1. The 50% / breach-line clearance is mechanical-minimum, not sharp; one more light fire would re-trigger.
2. Sound remains absent; the seam's recommended @98/@99/@131 candidates were defensibly refused on magnitude grounds (wax-marking is fine-grain), but the file's "sound-quiet" character is preserved rather than addressed. The modality-coverage critic's hot-button #2 ("major modalities absent that the location's palette should carry") could re-fire here — the workshop's loc card is sound-rich (apprentice-mark, stylus, household). Defense's refusal is valid but the absence is residual.
3. Tactile remains absent; defensibly routed to feel-facet, but tactile-as-environment is genuinely uncovered.

The file-level seam clears at the >50% threshold but does not become *textured* across all earned modalities — it shifts from STRONG breach to MODERATE single-channel-leaning. Acceptable, not pristine.

---

## Critical verifications

- **sensory:4 anchor change @58 → @60:** RESIDUAL. Mechanically: "lights" qualifies as action-verb self-charge per the pedant's expanded clause, so stripping @58 is correct. BUT @60's proto-line surface is empty (`60 [sensory:4]` only) — the move solved the verb-charge problem by eliminating the verb entirely. The disambiguation gate cannot operate on no-surface; this is a structurally novel fault not anticipated by the seam document. Old-state at @60 traces to loc-state:4 cleanly enough.
- **sensory:6 file-level add:** CLOSES with caveats. "Draws the winter-candle" is bare for thermal and licenses the delta. Distribution moves from 60% to 50% light — at the breach line, not below it. Sound-gap and tactile-gap are residual but defensibly refused on magnitude grounds.
- **DEFEND verifications (sensory:3, sensory:5):** both hold. sensory:3's "opens" survives because the magnitude/quality work isn't in the verb. sensory:5's "catches" is genuinely weaker self-charge than "lights" and the steadiness contrast is the load-bearing delta.
- **REVISE verifications (sensory:1, sensory:2, sensory:4):** sensory:1 closes cleanly (warmth claim withdrawn, baseline re-anchored). sensory:2 closes the strongest seam (loc-state lineage restored) but leaves the moderate disambiguation seam unaddressed. sensory:4 shifts (moves problem from verb-charge to anchor-vacuum).

## Final accept rate

- Pre-tuning: 5 entries; 4 STRONG + 0 MOD + 2 THIN strongest seams + 1 file-level STRONG.
- Post-tuning: 6 entries (5 + 1 file-level add); 5 / 6 = 83% ACCEPT (counting ACCEPT-WITH-CAVEAT as accept; sensory:4 is the lone REJECT).
  - Clean ACCEPT: 3/6 = 50% (sensory:1, sensory:3, sensory:5)
  - ACCEPT-WITH-CAVEAT: 2/6 = 33% (sensory:2, sensory:6)
  - REJECT: 1/6 = 17% (sensory:4)
- File-level: ACCEPT-WITH-CAVEAT.
- Lift comparison vs legacy-pattern facets:
  - memory: 100% / 75%
  - feeling: 92% / 75%
  - NI: 100% / 78%
  - vibes: 100% / 95%
  - sensory (tighter): 83% / 50%

## Pattern-comparison observations

- **Concrete-evidence rate in adjudication:** 6/6 per-entry verdicts cite specific protoline words ("wakes", "stirs", "opens", "[sensory:4]" surface vacuum, "catches", "draws"), specific loc-state entries (loc-state:1, :4, :6, :7, :8 by ID and field), and modality counts (60% → 50%). Zero verdicts rest primarily on rubric-clause citation. **100% concrete-evidence rate.** Matches the seam-finding pass.
- **THIN-verdict rate:** 0 caveats are manufactured. 2 ACCEPT-WITH-CAVEAT verdicts (sensory:2, sensory:6) are surfaced from genuine residual seams (unaddressed disambiguation MODERATE; warmth-inference softness). 1 REJECT (sensory:4) is a mechanically verified anchor-vacuum, not fabricated. Tighter pattern's adjudicator is *more* willing to issue REJECT when a structural fault is found and *less* willing to caveat-pad clean entries (sensory:1, :3, :5 are clean ACCEPT, no manufactured doubt).
- **Critic-scope discipline:** held. disambiguation-pedant and old-state-reader stayed within per-entry scope; modality-coverage stayed file-level. No bleed across lenses. Cross-critic verdicts converged or diverged on independent grounds (e.g., sensory:4: disambiguation REJECT, old-state ACCEPT-WITH-CAVEAT — different axes, same entry, no contamination).
- **Did the tighter pattern produce sharper Phase F decisions than legacy would have?** YES, with specific evidence:
  1. The sensory:4 anchor-vacuum REJECT is something the legacy 3-persona panel (dfr/pe/wcp) would almost certainly have missed — it requires opening the proto-lines file, reading line 60, and noticing the surface is empty. Dark-fantasy-reader would say "this reads atmospheric"; pulp-enthusiast would say "lamp-glow lands"; worm-canon-pedant would have nothing to say. Tighter pattern's disambiguation-pedant has a *mechanical gate* that fires on this case.
  2. The 50%-threshold clearance call (file-level ACCEPT-WITH-CAVEAT rather than ACCEPT-clean) is something legacy critics would not have surfaced — they don't count modalities. Modality-coverage's specialized lens registers the at-threshold-not-below distinction.
  3. The clean ACCEPTs on sensory:1, :3, :5 are confident in a way legacy adjudication would have hedged. Legacy would have manufactured "this could be more dark-fantasy" or "register feels thin" caveats. Tighter pattern accepts when the gates clear.
- Counter-evidence: the disambiguation-pedant's MODERATE seam on sensory:2 "mordant" (charged-noun seeding) was not adjudicated explicitly in the seam-finding pass (only the STRONG old-state seam routed) and surfaces as a residual caveat here. Legacy's broader lens might have caught and weighted this earlier. Tighter pattern's narrowness can drop secondary attacks below the routing threshold.

## Shippability

SHIPPABLE-WITH-CAVEATS.

The file is 5/6 acceptable with one structural REJECT (sensory:4) requiring a small anchor relocation before shoot. Recommended remediation: move sensory:4 from @60 (no-surface) to @61 ("taylor reaches the pallet" — bare verb, loft-vent-open per loc-state:5 licenses lamp-glow-leak as the perceptible inflection). This is a one-line fix; old-state would shift to loc-state:5's `tallow-lamp-lit, loft-vent-open` derivation. Cite-cascade: tens:46 @61 co-list adds sensory:4; proto-line @60 citation back-pointer removed; proto-line @61 adds [sensory:4]. After this one fix, the file is shippable-clean.

Without the fix, the file is shippable but carries one structurally undefined sensory entry. Studio's call.

## Pattern note

This is the first end-to-end Phase F under the tighter-audience pattern. Comparison data: legacy 3-persona pattern shipped 4 facets at 75-95% clean ACCEPT. Tighter pattern's first run on a smaller corpus (6 entries vs memory's 8, feeling's 12, NI's 24, vibes' 20) produced 50% clean ACCEPT / 83% accept-overall — *lower* clean-accept rate than legacy, but on substantively different grounds: the tighter critics caught a mechanical fault (anchor-vacuum) and a threshold-edge clearance that legacy would have rubber-stamped. Lower accept rate ≠ worse adjudication; it reflects sharper gates surfacing real structural issues. Pattern is validated for facets where mechanical correctness gates exist (sensory's bare-vs-charged, old-state lineage, modality counting). Whether to extend to facets without comparable mechanical gates is a separate decision.
