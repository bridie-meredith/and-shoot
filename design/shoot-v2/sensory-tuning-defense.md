sensory facet — Phase 4 defense / revision record
round: r2-tuning
date: 2026-05-10
author: studio
target: active-project/theater/facets/sensory.md (entries sensory:1–6)

---

## Per-entry decisions

### sensory:1 @1 — thermal | REVISE

Seam (old-state-reader STRONG): "loft-sleep-warmth" is a body-warmth inference with no anchor in loc-state:1, which records only `shutter-shut, loft-dark`. Baseline invented.

Original: `thermal: loft-sleep-warmth -> dawn-cold-air`
Seam: old-state traces to no loc-state field; "warmth" is body-state inference.

Draft A: `thermal: loft-dark-enclosed -> dawn-cold-air` — traces to "loft-dark" directly, but "dark" is a light descriptor pressed into thermal service.
Draft B: `thermal: loft-pre-dawn-still -> dawn-cold-air` — "pre-dawn-still" derives from "shutter-shut" (sealed, undisturbed) and "dawn" time-marker in loc-state:1; "still" describes thermal stasis before cold air contacts skin, not an invented warmth.
Draft C: `thermal: workshop-sealed-night -> dawn-cold-air` — over-extends; loc-state:1 marks time as dawn, not night.

Chosen: Draft B. `loft-pre-dawn-still` avoids the body-warmth claim and derives the old-state from loc-state:1's two traceable fields: time="dawn" (pre-dawn implied for a waking-moment) and condition="shutter-shut" (sealed, thermally still). "Still" is thermal-neutral, not thermal-positive; the critic's attack was specifically against "warmth" being invented. Draft B withdraws that claim and replaces it with spatial-stillness inferred from loc-state architecture.

How seam answered: old-state no longer invents a warmth baseline. "loft-pre-dawn-still" is traceable to loc-state:1's shutter-shut/loft-dark conditions. The delta (still → dawn-cold-air) fires on the proto-line "taylor wakes in the loft" — "wakes" is bare; the thermal drop of dawn air contacting waking skin is not self-carried by the word.

Applied: sensory:1 old-state updated from `loft-sleep-warmth` to `loft-pre-dawn-still`.

---

### sensory:2 @3 — smell | REVISE

Seam (old-state-reader STRONG): @3 falls in a loc-state gap (between loc-state:1 @1 and loc-state:2 @8). Old-state "workshop-mordant-ambient" sourced from loc card palette, not from any loc-state entry.

Original: `smell: workshop-mordant-ambient -> mordant-stir-sharp`
Seam: no loc-state entry between @1 and @3; old-state sources from loc card, not loc-state.

Draft A: `smell: loft-dark-wood-dry -> mordant-stir-sharp` — traces to loft, but sensory:2 fires at @3 which is in the workshop (mother stirs the mordant pot); loft smell is wrong location-register.
Draft B: `smell: workshop-shutter-shut-enclosed -> mordant-stir-sharp` — loc-state:1 records "shutter-shut" as a condition applying to the whole loc-craftsman-workshop-home; "enclosed" is a direct spatial inference from "shutter-shut". Smell in an enclosed workshop before any aeration = captured-air baseline. Not sourced from loc card's mordant-ambient claim; sourced from loc-state:1's architectural condition.
Draft C: `smell: workshop-dawn-still -> mordant-stir-sharp` — parallel to sensory:1 Draft B pattern; thins the smell specificity.

Chosen: Draft B. "workshop-shutter-shut-enclosed" traces near-verbatim to loc-state:1's "shutter-shut" condition. The cross-facet contract says source old-state from the most recent loc-state entry — that is loc-state:1 @1. "Shutter-shut, loft-dark" is what loc-state:1 holds; "enclosed" derives from shutter-shut. The old-state is no longer lifted from the loc card's palette; it is derived from the locked loc-state architecture.

How seam answered: old-state is now loc-state-derived, not loc-card-derived. The critic's specific attack was "baseline is sourced from the loc card's palette, not the locked loc-state" — Draft B roots the old-state in loc-state:1's conditions field verbatim.

Applied: sensory:2 old-state updated from `workshop-mordant-ambient` to `workshop-shutter-shut-enclosed`.

---

### sensory:3 @8 — light | DEFEND

Seam (disambiguation-pedant THIN): "opens the shutter" arguably self-carries light-in; the verb charges the onset. "cut-through" magnitude descriptor added by the flag may be redundant.

Defense: "opens" and "shutter" together describe a mechanical action — the verb names the physical event, not the perceptual register. A reader parsing "opens the shutter" receives the action of opening; they do not receive the quality or magnitude of the light that enters. "Morning-daylight-cut-through" is the delta the verb does not supply: it disambiguates shaft-of-cutting-morning-light from the dim-fill that opening a shutter at dusk would produce. The word "opens" is charged for the onset (something happens) but bare for magnitude and quality. The seam rates this THIN; the critic acknowledges it "survives the gate." The old-state "dawn-shuttered-dim" traces verbatim to loc-state:1's "dawn | shutter-shut, loft-dark"; the new-state "morning-daylight-cut-through" near-verbatim-matches loc-state:2's "daylight cutting the workshop floor." Lineage is the cleanest in the file. No revision needed.

---

### sensory:4 @58→@60 — light | REVISE

Seam (disambiguation-pedant STRONG): "lights the tallow lamp" — "lights" names the perceptual act. Action-verb self-charge clause (added to disambiguation-pedant card 2026-05-10): action verbs whose semantic content IS the sensory event are charged, not bare. "Lights" carries the light-onset. Fire at @58 doubles the verb.

Original: `4 @58 light: workshop-dusk-dim -> tallow-lamp-glow`
Seam: "lights" is a charged action-verb; the verb IS the light-onset; the fire doubles.

Resolution path: strip the fire at @58 (verb-charged) and re-anchor at @60, the first beat after the lamp is established where the quality of the lamp-glow becomes perceptible without the onset verb doing the work. @60 in the proto-lines is a post-speech beat (following @59 "oc-craftsman-mother speaks to taylor-hebert-jaehaerys") — the lamp is burning, the quality settles, and there is no charged verb at @60.

Revised entry: `4 @60 light: workshop-dusk-closed -> tallow-lamp-glow-settle`
Old-state: "workshop-dusk-closed" traces to loc-state:4 @58 which records `dusk | tallow-lamp-lit, shutter-shut`. "Dusk" + "shutter-shut" → "workshop-dusk-closed" captures the enclosed dusk state before lamp quality registers. This is the most recent loc-state at @60.
New-state: "tallow-lamp-glow-settle" names the quality of tallow-lamp ambient — warm, unsteady glow stabilizing after lighting — distinct from the onset the verb already named.

How seam answered: fire moved off the verb-charged proto-line. @60 has no action-verb self-charge; the fire at @60 flags the lamp-quality register once the onset is past. The disambiguation gate clears because "settles" is the ambient-quality beat, not the ignition beat.

Cite-cascade: sensory:4 removed from @58 co-citations; sensory:4 added to @60. tens:44 @58 co-list updated (sensory:4 dropped). Proto-lines file already had @60: [sensory:4].

---

### sensory:5 @130 — light | DEFEND

Seam (disambiguation-pedant THIN): "candle catches" — "catches" implies light-up at the verb; narrow argument that the fire doubles.

Defense: "catches" (in "the candle catches") describes the wick-igniting event in a dye-craft register — it is distinctly weaker than "lights" as a perceptual self-carrier. "Lights" announces a subject performing a deliberate illuminating act; "catches" describes the candle responding to contact, foregrounding the physical mechanism over the perceptual output. The fire's real work is the `guttering-unsteady -> candle-steady-flame` contrast — the quality-shift from an unstable tallow lamp's irregular shadow-casting to the clean, still candle flame. That quality-register (unsteady vs. steady) is not in "catches"; the audience cannot infer flame-steadiness from "catches" alone. The old-state "tallow-lamp-guttering-unsteady" traces verbatim to loc-state:7's "tallow-lamp-guttering"; the new-state "candle-steady-flame" traces verbatim to loc-state:8's "candle flame the only steady light in the room." Lineage is clean on both ends. The seam rates this THIN and the seam document acknowledges it "survives the gate." No revision needed.

---

## File-level seam — modality-coverage | REVISE by ADD

Seam (modality-coverage STRONG): 3 light / 1 thermal / 1 smell = light at 60%, breaching the >50% single-channel threshold. Zero sound fires despite stylus-marking (@98, @131), candle-catching (@130), and workshop soundscape. Zero tactile despite physical-contact beats. Workshop palette (thermal/smell per loc card) undertreated in lamp-lit second half.

Decision: REVISE by ADD. The file-level seam is valid — 3/5 entries on light is documentably single-channel. The thermal gap in the second half is real. Sound was assessed for @98 and @131; both have concerns (magnitude threshold for stylus-marking is sub-threshold per rubric §3; @130 "candle catches" is the beat sensory:5 already fires on for light). Thermal at @126 is the recommended candidate: bare proto-line ("draws"), loc-state:7 licenses thermal motivation ("tallow-lamp-guttering, winter-candle-drawn"), and the draw-of-winter-candle is universally readable as a room-chill signal.

Addition: sensory:6 @126 `thermal: workshop-evening-settled -> room-chill-winter-candle-needed # tag: drop`

Anchor word: "draws" — bare verb; does not self-carry thermal register.
Old-state lineage: most recent prior loc-state is loc-state:6 @92 (`late-evening | clear | tallow-lamp-lit, ledger-open`). "Workshop-evening-settled" derives from "late-evening" + "tallow-lamp-lit" (heat from a burning lamp in an enclosed room = settled-warm). loc-state:7 then marks the lamp as guttering — the transition to cold is the inflection.
New-state: "room-chill-winter-candle-needed" — the act of drawing a winter candle is the audience-legible signal that room temperature has dropped enough to require it. "Winter-candle-drawn" in loc-state:7 licenses this directly.
Bare-word gate: "draws" is bare; does not self-carry thermal delta.
Magnitude: drawing a winter candle in a craftsman workshop at night signals a perceptible cold threshold. Audience-experiential scale.
Audience-side perceptibility: yes — a winter candle drawn is a universally legible cold-room signal.

Post-addition modality distribution: 3 light / 2 thermal / 1 smell. Light = 3/6 = 50%, no longer breaching the >50% threshold (at exactly 50% with 6 entries). Thermal now fires twice, covering the lamp-lit second half. Sound remains silent — @98 stylus-marking and @131 ledger-marking were assessed and refused on magnitude-sufficiency grounds (wax-marking is fine-grain, below audience experiential threshold at the scale of this episode's perceptual register). Tactile remains absent — physical-contact beats (@47 ruffle, @83 pull, @119 shoulder-touch) are feel-facet territory; tactile-as-environment has no earned candidate in this episode's location-state record.

Cite-cascade: proto-lines @126 already has `[sensory:6]` applied. Cite-index sensory:6 @126 added; loc-state:7 and tens:99 co-lists updated to include sensory:6.

---

## Summary

| Entry | Decision | Basis |
|---|---|---|
| sensory:1 | REVISE | old-state reanchored: `loft-sleep-warmth` → `loft-pre-dawn-still` (loc-state:1 shutter-shut derivation) |
| sensory:2 | REVISE | old-state reanchored: `workshop-mordant-ambient` → `workshop-shutter-shut-enclosed` (loc-state:1 conditions verbatim) |
| sensory:3 | DEFEND | "opens" charges onset not quality; "cut-through" delta is the unsupplied work; lineage cleanest in file |
| sensory:4 | REVISE | fire moved @58→@60; "lights" action-verb self-charge stripped; glow-quality fire after onset-verb |
| sensory:5 | DEFEND | "catches" weaker self-charge than "lights"; guttering→steady contrast is the uncarried delta; verbatim loc-state lineage both ends |
| file-level | REVISE (ADD sensory:6) | thermal gap in lamp-lit half; @126 "draws" bare, loc-state:7 licenses winter-candle thermal, audience-legible cold signal |

Counts: REVISE 3, DEFEND 2, WITHDRAW 0.
File-level: REVISE by ADD 1 entry (sensory:6).
Citation cascade: sensory:4 co-citation moved @58→@60 (tens:44 co-list updated); sensory:6 added to cite-index, loc-state:7 and tens:99 co-lists updated; proto-lines file was pre-cascaded.
Total cascade touches: 4 (sensory:4 move, sensory:6 add, loc-state:7 co-update, tens:44 co-update).

Defense register note: all 5 per-entry defenses and revisions cite specific proto-line words ("loft-sleep-warmth", "lights", "catches", "opens"), loc-state entry fields (loc-state:1 "shutter-shut, loft-dark"; loc-state:4 "dusk | tallow-lamp-lit"; loc-state:7 "tallow-lamp-guttering"; loc-state:8 "candle flame the only steady light"), and modality counts (3 light / 1 thermal / 1 smell pre-revision; 3 light / 2 thermal / 1 smell post). Zero rubric-clause citation used as primary defense basis.
