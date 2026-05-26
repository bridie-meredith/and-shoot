---
reviewer: sensory-old-state-reader
facet: sensory
episode: b01-c02
cycle: r1
date: 2026-05-25
verdict: accept
---

# Verdict reasoning

Both entries carry the loc-state negative-inference carve-out declared in the facet file header. The carve-out is specific: no loc-state facet file was authored for b01c02; old-states are derived from the location card (oc-stitch-house-lane) Sensory Vocabulary section. This reviewer's attack axis is old-state lineage correctness. The carve-out must be interrogated, not merely accepted.

**sensory:1 @4 — sound: lane-quiet -> alley-mouth-murmur**

Walk the lineage:
1. Most recent prior loc-state at @4: loc-state:2 @4. Entry reads: "oc-stitch-house-lane | dawn-to-day | none | lane-mouth-occupied | threshold at the lane-mouth: controls sight-line in both directions; compressed single-file width governs who can pass while Taylor holds position." The loc-state:2 entry does not carry a sensory note naming the sound register; it names the tactical geometry (threshold, sight-line, compressed width).
2. Most recent loc-state before @4: loc-state:1 @1. Entry reads: "oc-stitch-house-lane | dawn-to-day | none | drain-angle-vacated | lane-mouth forty paces north: visible from angle-gap, governing line-of-sight both into the lane and out to the Hook alley." No sensory note at loc-state:1 either.
3. Old-state derivation: "lane-quiet." The location card's Sensory Vocabulary states: "The drain-water trickle at the angle-gap — audible when the lane is quiet." The phrase "audible when the lane is quiet" positively names lane-quiet as a real perceptual condition — it is not a negative inference but a direct statement of baseline. The location card establishes lane-quiet as the condition under which the drain-water becomes audible, identifying lane-quiet as the lane's ambient sound baseline. The old-state "lane-quiet" traces directly to the location card's Sensory Vocabulary.
4. New-state: "alley-mouth-murmur." The location card names "Compressed foot-traffic sound" as a named Sensory Vocabulary feature. The alley-mouth murmur is the acoustic character of the junction at the lane's north end, where the lane opens onto the broader Hook District alley. The new-state is consistent with the location card's named sound palette for the lane-mouth zone.
5. Delta direction: old (lane-quiet) → new (alley-mouth-murmur) is an up transition — the acoustic level rises as Taylor reaches the junction. Consistent with the positional move from enclosed lane interior to lane-mouth.

**Lineage verdict for sensory:1: TRACES.** The old-state "lane-quiet" derives from a positive statement in the location card Sensory Vocabulary. The new-state "alley-mouth-murmur" is consistent with the card's "Compressed foot-traffic sound" naming. The carve-out is not needed in the strong form for sensory:1; the location card directly supplies the baseline.

---

**sensory:2 @11 — smell: pre-tallow-lane-ambient -> tallow-smoke-onset**

Walk the lineage:
1. Most recent prior loc-state at @11: loc-state:3 @11. Entry reads: "oc-stitch-house-lane | days-of-coverage | none | stitch-house-lamp-burning | tallow smoke pooling at lane-floor level in the east wall's reach: the insect-feed's location marker for the stitch-house threshold." The loc-state:3 entry names the tallow smoke's presence and character — pooling at lane-floor level, east wall's reach. It establishes the new state, not the old state.
2. No prior sensory entry on the smell modality in this file; no prior loc-state entry names an ambient smell baseline for the lane before the tallow smoke arrives.
3. Old-state derivation: "pre-tallow-lane-ambient." This is a negative inference — the carve-out declares it explicitly: "Marks the stitch-house lane implies the smoke is arriving/spreading as an event. Pre-event state is the smoke-free lane ambient." The derivation logic is: the location card describes tallow smoke as an onset-and-pool event ("pooling at lane-floor level in still air"), not a continuous ambient. Therefore before the onset, the lane is smoke-free. The old-state names the pre-onset condition.
4. Is the negative-inference defensible? The location card Sensory Vocabulary names tallow smoke as pooling "in still air" — framing it as a condition-dependent event, not always-on ambient. Loc-state:1 and loc-state:2 (the chapter's earlier loc-state entries) do not mention tallow smoke as present, which is consistent with the smoke not yet having arrived. The negative inference has chain support: the silence of the prior loc-state entries on tallow smell + the location card's onset-and-pool framing → the pre-@11 state is smoke-free.
5. New-state: "tallow-smoke-onset." Traces directly to loc-state:3 @11's content: "tallow smoke pooling at lane-floor level." The new-state name accurately describes what loc-state:3 establishes. Strong match.
6. Delta direction: old (pre-tallow-lane-ambient / smoke-free) → new (tallow-smoke-onset / smoke arriving and pooling). Up. Consistent with loc-state:3's description.

**The old-state name "pre-tallow-lane-ambient" is the weakest link.** It is defined by absence: the lane before the smoke. The attack available here: "pre-tallow-lane-ambient" is not a named perceptual state in the location card; it is derived by subtracting the onset event. The location card does not positively state "the lane smells of nothing before the lamp burns." The old-state exists only because the new-state happens.

However: this is the canonical negative-inference derivation case. The alternative — leaving the old-state unspecified or as a free-floating generic — would be strictly worse. The carve-out was designed for exactly this structural condition: no loc-state file, onset event named in the location card, pre-event state inferred from the card's onset framing. The precedent from the b01c01 cycle-1 negative-inference derivation (referenced in the carve-out preamble) was accepted on the same logic. The carve-out is internally consistent; the derivation logic is documented; the negative inference is the only defensible baseline given the chapter's loc-state structure.

**Lineage verdict for sensory:2: TRACES — under carve-out.** The old-state is a negative inference from the location card's onset framing. Thin but documented. The new-state traces directly to loc-state:3. The delta direction is unambiguous. No baseline-invention; the derivation logic is explicit and named.

---

# Entry-level callouts

No blocking callouts. Advisory notes only:

[sensory:2] @11 — "pre-tallow-lane-ambient" as old-state is the thinnest defensible derivation in this file. If any future revise pass adds a second smell fire, it must inherit from either "tallow-smoke-onset" (if the smoke persists) or document a new loc-state entry first. The negative-inference carve-out is a single-use mechanism; it does not create a floating smell baseline for downstream fires.

# Convergence-trace notes

- auditor carve-out preamble (loc-state negative-inference derivation from location card): this reviewer's gate is directly addressed by the carve-out. The preamble documentation is specific and named per-entry. The lineage walk above confirms the carve-out logic holds for both entries.
- auditor flag-001 (6.9% density): density is not this reviewer's axis.
- auditor RUBRIC-FIDELITY: "sensory modality distribution: 2 modalities (sound @4, smell @11). ≥2 floor met." Both modalities' old-states trace. No cross-facet contradiction with loc-state found.
- b01-c01 cycle-1 verdict (this reviewer): that chapter's carve-out covered "lane-ambient" as smell old-state for sensory:1 @2 by negative inference, with a notation that it was "the thinnest possible carve-out application." b01-c02's sensory:2 old-state derivation is structurally similar but marginally stronger: the location card explicitly frames tallow smoke as an onset-and-pool event (not always-on), which makes the pre-event state more clearly inferrable. The derivation is one notch stronger than the b01-c01 precedent.
- No auditor finding targets old-state correctness for either entry. The carve-out preamble preempts the unanchored-old-state HARD.

**File verdict: ACCEPT.**
