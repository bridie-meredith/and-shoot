adversarial seam-finding (TIGHTER AUDIENCE PATTERN): sensory facet, s01e01
date: 2026-05-10
mode: hostile-attack; tighter-audience pilot
target: 5 sensory entries (sensory:1-5)
critics:
  - sensory-disambiguation-pedant
  - sensory-modality-coverage
  - sensory-old-state-reader
attack-grounding: direct adversarial reading; rubric-citation supplementary only
pattern-comparison: legacy 3-persona pattern would have used dfr/pe/wcp uniformly

---

## Per-entry attacks

### sensory:1 @1 — `thermal: loft-sleep-warmth -> dawn-cold-air  # tag: drop`

- disambiguation-pedant (severity: MODERATE): Proto-line is "taylor wakes in the loft" — "wakes" is bare and licenses a thermal flag, but "wakes" is also the inflection-act itself; the thermal delta arguably belongs in narrator-interest as Taylor's first registered perception, not as audience-side environmental change.
- old-state-reader (severity: STRONG): old-state "loft-sleep-warmth" has no anchor in loc-state:1, which records only `dawn | clear | shutter-shut, loft-dark`. The warmth baseline is invented from a body-state inference, not from loc-state's environmental record.
- **STRONGEST PER-ENTRY SEAM:** old-state-reader — baseline "loft-sleep-warmth" is invented; loc-state:1 establishes only shutter-shut and loft-dark, no thermal baseline.

### sensory:2 @3 — `smell: workshop-mordant-ambient -> mordant-stir-sharp  # tag: up`

- disambiguation-pedant (severity: MODERATE): Proto-line is "mother stirs the mordant pot" — "mordant" is technical/charged for a dyer's-trade reader and self-carries chemical sharpness. The flag's "stir-sharp" delta is partly redundant against "mordant pot" already seeded.
- old-state-reader (severity: STRONG): Sensory:2 fires at @3 but no loc-state entry exists between loc-state:1 @1 and loc-state:2 @8. Old-state "workshop-mordant-ambient" is unanchored; loc-state:1 records nothing about mordant ambient. Baseline is sourced from the loc card's palette, not the locked loc-state.
- **STRONGEST PER-ENTRY SEAM:** old-state-reader — @3 falls in a loc-state gap; old-state is loc-card-derived, not loc-state-derived; cross-facet contract names loc-state as the baseline source.

### sensory:3 @8 — `light: dawn-shuttered-dim -> morning-daylight-cut-through  # tag: up`

- disambiguation-pedant (severity: THIN): Proto-line is "father opens the workshop shutter" — "opens" and "shutter" are bare; magnitude tag ("cut-through") adds register the verb does not supply. Defensible fire; weakest hostile reading is "shutter-opening already self-carries light-in."
- old-state-reader (severity: THIN): Old-state "dawn-shuttered-dim" traces cleanly to loc-state:1's `dawn | shutter-shut, loft-dark`. New-state "morning-daylight-cut-through" near-verbatim-matches loc-state:2's "daylight cutting the workshop floor." Lineage is the cleanest in the file.
- **STRONGEST PER-ENTRY SEAM:** disambiguation-pedant — narrow Q1 challenge that "opens the shutter" arguably charges light-in; survives but is the weakest cell on the disambiguation axis.

### sensory:4 @58 — `light: workshop-dusk-dim -> tallow-lamp-glow  # tag: up`

- disambiguation-pedant (severity: STRONG): Proto-line is "mother lights the tallow lamp" — "lights" self-carries the light-up event. The audience knows lighting a lamp produces light without the flag. Only the "glow" specificity does work the verb does not.
- old-state-reader (severity: MODERATE): Old-state "workshop-dusk-dim" has no direct loc-state anchor. loc-state:3 @32 records `afternoon | workshop-door-open` — no dim baseline. loc-state:4 @58 sets `dusk | tallow-lamp-lit` post-action. The "dusk-dim" old-state is inferred from time-progression, not traced to a loc-state field.
- **STRONGEST PER-ENTRY SEAM:** disambiguation-pedant — "lights the tallow lamp" charges light-up at the verb; the fire violates the bare-word gate the rubric names load-bearing.

### sensory:5 @130 — `light: tallow-lamp-guttering-unsteady -> candle-steady-flame  # tag: up`

- disambiguation-pedant (severity: THIN): Proto-line "the candle catches" — "catches" is bare for a wick-igniting context; "steady-flame" specificity does work the verb does not. The "guttering-unsteady" → "steady" contrast is the actual register-shift; defensible.
- old-state-reader (severity: THIN): Old-state "tallow-lamp-guttering-unsteady" traces verbatim to loc-state:7's `tallow-lamp-guttering`. New-state "candle-steady-flame" traces to loc-state:8's "candle flame the only steady light in the room." Tightest lineage in the file; near-zero seam.
- **STRONGEST PER-ENTRY SEAM:** disambiguation-pedant — narrow weak attack that "candle catches" implies light-up at the verb; survives the gate, but is the only cell with any traction.

---

## File-level seam (modality-coverage)

**SEVERITY: STRONG.** 5 entries / 102 protolines = 4.9% sparsity (in band). Modalities: 3 light, 1 thermal, 1 smell. Light = 60% of fires — file is single-channel light-dominant, breaching the >50% hot-button. Zero sound fires in an episode that contains stylus-marking (@98, @131), apprentice-mark (@99), candle-catching (@130), hair-ruffling (@47), and a household with "richest insect ecology" per loc card (flies @27/@48, moth @62-65, swallow @105, horsefly @79). Zero tactile despite physical-contact beats (@47 ruffle, @83 hair-pull, @119 shoulder-touch route to feel/state but tactile-as-environment is uncovered). Workshop palette per loc card leans thermal/smell — thermal fires once (@1), smell fires once (@3), neither in the lamp-lit second half (@58 onward). Recommended additions: (a) sound fire on @98 stylus-marking or @99 apprentice-mark — bare verb, perceptually load-bearing; (b) thermal fire late-evening (@126 winter-candle drawn signals room cooling around guttering lamp).

**Rationale:** the file passes ≥2-modality floor mechanically but reads as a "light-progression study" (dim → shutter → lamp → candle). The episode's emotional shape — mordant-pot morning, market-slip rupture, apprentice-mark, lamp-gutter night — is sound-quiet and thermal-quiet in the file when the proto-line surface offers earned candidates. Single-channel breach.

---

## Pattern-comparison observations

- **Concrete-evidence rate:** 10/10 per-entry attacks cite a specific protoline word, loc-state entry, or modality count. Zero attacks rely primarily on rubric-clause citation. The file-level attack cites concrete protoline IDs (@98, @99, @126) and loc-card content. **100% concrete-evidence rate.** Legacy 3-persona pattern (dfr/pe/wcp) on this corpus would have produced abstract register attacks ("doesn't read dark-fantasy enough", "where's the Worm-canon thread") — not bare-vs-charged or loc-state-trace attacks.
- **THIN-attack rate:** 4 of 10 per-entry attacks are THIN (sensory:3 both cells, sensory:5 both cells). 4/10 = 40% THIN. **Higher than legacy memory + feeling + NI runs (which had 0 THIN aggregate).** Two entries (sensory:3 and sensory:5) are genuinely tight under both per-entry critics — the tighter lens correctly registers low-attack-surface entries rather than fabricating attacks.
- **Modality-coverage file-level lens — value:** YES. The 60%-light dominance and silent-modality gaps (sound/thermal in lamp-lit half) are invisible to per-entry critics by design. The single STRONG file-level seam is the most actionable seam in the whole pass.
- **Legacy 3-persona pattern comparison:** The general dfr/pe/wcp would have:
  - **caught:** sensory:4 redundancy on "lights the lamp" (pulp-enthusiast sensitive to verb-charge); sensory:1's invented warmth baseline (dark-fantasy-reader notes "where does this come from?").
  - **missed:** sensory:2's loc-state-gap unanchoring (requires triangulating two facet files — none of dfr/pe/wcp does cross-facet trace); the file-level light-dominance (none counts modalities); sensory:3 and sensory:5's tight-lineage observations (legacy pattern would have fabricated atmospheric attacks rather than acknowledge tightness).
  - **weaker on:** every per-entry attack one register removed — "this doesn't feel sensory enough" rather than "old-state X is invented; loc-state:Y has Z."

## Rubric ambiguities surfaced (if any)

- **Old-state source ambiguity at loc-state-gap protolines.** Sensory:2 @3 falls between loc-state:1 (@1) and loc-state:2 (@8). Rubric § cross-facet contract says "Source the old-state from the locked location-state for the most recent loc-state-cited beat, OR from the prior sensory-flag entry on the same modality." Silent on what to do when the most-recent loc-state does not record the modality at all. Sensory:2's "workshop-mordant-ambient" is loc-card-derived, not loc-state-derived. The rubric should explicitly permit loc-card palette as a tertiary source OR forbid it (forcing studio to add a loc-state entry first).
- **"Lights"-class action verbs.** The rubric's charged-word list ("thunder", "shadow", "stench", "blistering"...) doesn't enumerate action-verbs that self-carry inflection (lights, opens, ignites). Should "lights the lamp" be treated as a charged-action even though "lights" alone is bare? Sensory:4 hangs on this question.

(Queue for optional rubric-tuning pass — not a primary product.)

## Adjudication routing

5 strongest per-entry seams + 1 file-level seam route to studio (sensory facet author) for defense or revision per facet-tuning-process.md Phase 4:

1. sensory:1 — old-state-reader STRONG: "loft-sleep-warmth" invented; defend or revise to loc-state-traceable baseline.
2. sensory:2 — old-state-reader STRONG: @3 in loc-state gap; defend palette-source or add loc-state entry.
3. sensory:3 — disambiguation-pedant THIN: weakest seam; likely survives defense.
4. sensory:4 — disambiguation-pedant STRONG: "lights the tallow lamp" verb self-carries; defend "glow"-specificity or strip.
5. sensory:5 — disambiguation-pedant THIN: weakest seam; likely survives defense.
6. **File-level — modality-coverage STRONG: 60% light-dominance; defend single-channel reading or add sound/thermal fires on earned candidates (@98/@99/@126).**
