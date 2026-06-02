---
reviewer: sensory-old-state-reader
facet: sensory
episode: b01c06
cycle: r1
verdict: revise
date: 2026-05-31
---

# Sensory Old-State Reader — Adversarial Verdict

## Entry-by-entry old-state anchoring

---

### sensory:1 @2 — pressure: lane-passable-morning-flow -> crowd-backed-body-compression

**Verdict: REVISE**

The carve-out preamble in sensory.md is honest about the problem and then argues past it. I hold both files open.

loc-state:1 fires at @1. Its state is `lane-mouth-blocked-handcart` — the chapter opens with the blockage already established. There is no loc-state entry that precedes @1. The lane-passable state is not in the loc-state file at any proto-line anchor.

The carve-out asserts the location card §Hazards baseline ("crowd compression blocks retreat") is a legitimate old-state source. That section names the hazard condition — it does not establish a prior state for the chapter. The distinction matters: §Hazards describes what the location is *capable of*, not what it *was* at any in-chapter beat. A capability is not a prior perceptual state. `lane-passable-morning-flow` is not in §Hazards verbatim or near-verbatim; it is an inference the author drew from the card's geography. The rubric requires old-state to resolve to "the most recent loc-state file's § sensory or § conditions baseline for the beat's location, OR the most recent prior sensory-flag entry on the same modality" — location card §Hazards is neither.

The studio state.md note (line 84) reads: "sensory:1 old-state sourced from location card §Hazards baseline (documented carve-out)." Documented, yes. Anchored per the rubric, no. The carve-out documents the gap; it doesn't close it.

The b01c05 precedent cited ("`lane-stone-surface-baseline` derived from location card §Tactile vocabulary") differs in kind: tactile surface-material is not a changing state, it's a physical constant. Pressure state is contextual and changing — the lane is sometimes passable and sometimes not. A static physical property carries differently from a dynamic contextual one. The precedent does not transfer cleanly.

The author's own SEAM-009 flag marks this for R2 attention. The carve-out is a good-faith attempt, but the rubric's Axis 1 REJECT signature "Unanchored old-state (HARD)" applies: the old-state does not resolve to a loc-state entry, and the location card §Hazards section is not the "§ sensory or § conditions baseline" the rubric specifies as the fallback. This is a HARD finding per URI-FACETS-CYCLE-1.

**Remediation criteria:** Either (a) author a pre-@1 loc-state entry establishing the lane-passable-morning-flow state as the chapter-open baseline before the blockage, then anchor sensory:1 to that entry, OR (b) find the pressure inflection defensible from loc-state:1's explicit "crowd pressure backing the junction solid" — in which case the old-state should be re-sourced as the implicit pre-block state that loc-state:1's own description implies. Option (b) is a borderline move: loc-state:1's narrative phrase "backing the junction solid" implies a prior open state, but whether a loc-state entry's embedded contrast constitutes a valid old-state anchor is contestable. Cleaner path is (a).

**Convergence-trace:** SEAM-009 (studio self-flag). URI-FACETS-CYCLE-1 unanchored-old-state HARD. The carve-out preamble is a concurrent self-awareness note, not a prior audit finding; convergence with the rubric's own REJECT signature at Axis 1.

---

### sensory:2 @17 — sound: drain-water-trickle-ambient -> stylus-on-board-rhythm

**Verdict: ACCEPT (conditional)**

The studio state.md reads: "sensory:2 old-state from loc-state:2 @5 sensory vocabulary (drain-water-trickle per location card oc-stitch-house-lane)."

I hold both files. The location card §Sensory Vocabulary states verbatim: "The drain-water trickle at the angle-gap — audible when the lane is quiet." This is named in the card's sensory palette. The question is whether card-sourcing is legitimate here — and unlike @2, it is defensible for a specific reason: the drain-water trickle is a *constant passive feature*, not a contextual crowd-state. It is the environmental ambient below every other sound in this location. It is not a state that was established or changed; it is the baseline beneath.

loc-state:2 @5 establishes `south-court-working-position` — it does not name audio conditions, but the south-court position is within the location (the angle-gap drain is the named trickle source; the south-court working position is at the south end of the lane where the angle-gap is). Taylor at @17 is in the south-court working position established at @5. The drain-trickle is present in the location card's sensory vocabulary as the ambient audio for that end of the lane.

The concern: there is no loc-state entry between @5 and @17 that explicitly establishes `drain-water-trickle-ambient` as the active sound state. The card supplies the vocabulary; loc-state:2 establishes position; together they make the old-state inferable. The rubric wants "the most recent loc-state file's § sensory or § conditions field." Neither loc-state entry has a § sensory sub-field — the location card is the sensory vocabulary source, and studio has treated card-plus-position as an anchoring pair.

This is lighter ground than the §Hazards-as-anchor problem at @2. The drain-trickle is a physical constant of the location (not a contextual state), Taylor is confirmed at the drain-adjacent south-court position from loc-state:2 @5, and the card names it verbatim. I do not rate this as a HARD unanchored finding — the old-state is traceable, even if the trace goes through the card rather than a loc-state §sensory sub-field.

**Conditional:** If the auditor's Phase 5 mechanical scan finds no loc-state §sensory sub-field and rates this as unanchored-HARD, this note should be elevated. My reading under the old-state-lineage lens: the trace is thin but present. The card's sensory vocabulary for a constant ambient feature (trickle is always there; it becomes audible when quiet enough) is more defensible than an inferred prior-crowd-state.

**Convergence-trace:** No prior audit finding on this entry. The studio self-note (state.md line 84) accepts it; I accept it under the card-ambient-constant reading, noting the thin anchoring.

---

### sensory:3 @20 — sound: stylus-on-board-rhythm -> silence

**Verdict: ACCEPT**

Cleanly anchored. sensory:3's old-state `stylus-on-board-rhythm` is verbatim equal to sensory:2's new-state `stylus-on-board-rhythm`. This is the in-stream inflection pair the rubric explicitly endorses: "the most recent prior sensory-flag entry on the same modality." The pair reads as: sound-up at @17 (trickle → stylus-rhythm), sound-drop at @20 (stylus-rhythm → silence). The drop's old-state inherits from the up's new-state without invention.

Inflection-pair coherence: @17's new-state = @20's old-state. Match is exact. Back-to-baseline logic: @17 up-fires establish the new level; @20 drop fires when the stylus stops. The pair is structurally coherent.

No old-state lineage issue. No loc-state contradiction. No invented baseline. The anchor is the prior sensory entry on the same modality — this is the standard correct anchor path.

**Convergence-trace:** No prior audit finding on this entry. Clean.

---

## Aggregated verdict

**REVISE**

sensory:1 @2 carries a HARD unanchored-old-state finding. The carve-out preamble is documented but not sufficient: location card §Hazards is a capability description, not a perceptual state established at a prior in-chapter proto-line anchor. The rubric's Axis 1 REJECT signature (URI-FACETS-CYCLE-1) applies. sensory:2 @17 is conditionally accepted under a card-ambient-constant reading with a thin anchor trail. sensory:3 @20 is clean.

The file cannot pass Phase 5b with sensory:1's old-state unresolved. The finding routes to fixer for loc-state remediation before sensory:1 can stand.
