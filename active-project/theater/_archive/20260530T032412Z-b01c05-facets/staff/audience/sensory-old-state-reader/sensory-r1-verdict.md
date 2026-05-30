---
reviewer: sensory-old-state-reader
facet: sensory
episode: b01-c04
cycle: r1
date: 2026-05-27
verdict: revise
---

# Per-Entry Adversarial Review — sensory-b01-c04.md

## Old-state lineage protocol

For each of the 3 entries:
1. Identify the most recent loc-state entry at or before this protoline.
2. Read the sensory entry's old-state field.
3. Check consistency: does old-state trace to loc-state, OR to the most recent prior sensory entry on the same modality?
4. Check delta direction: does loc-state's palette actually produce this new-state?

---

## Entry-level callouts

### [sensory:1] @1 — `smell: eel-alley-dawn-air -> tallow-damp-lane-caulking`

**ATTACK — STRONG.**

Most recent loc-state at or before @1: loc-state:1 @1. Entry reads: `oc-cooper-yard-eel-alley | predawn | none | tallow-damp-present, yard-workers-at-near-shed, third-bell-quiet | the tallow-damp off the lane-caulking reaches the shed-wall before the yard is visible.`

Old-state claimed: `eel-alley-dawn-air`. Walk the lineage:

Step 1: No loc-state entry precedes @1 in this chapter. @1 is the chapter-open anchor. There is no prior entry to inherit from.

Step 2: No prior sensory entry on smell-modality exists. sensory:1 is the first smell fire in the episode.

Step 3: The old-state `eel-alley-dawn-air` cannot be derived from any loc-state entry. It names a pre-tallow ambient that no file establishes. This is a baseline invented by the sensory entry itself.

Step 4: Compound problem. loc-state:1 @1 declares `tallow-damp-present` as the condition already in place at @1. The entry's own language — "the tallow-damp off the lane-caulking reaches the shed-wall before the yard is visible" — places the tallow-damp as the chapter-open environment, not as a new arrival. If tallow-damp is already present at @1, the sensory entry's new-state (`tallow-damp-lane-caulking`) is recording the baseline, not a delta arriving at @1. The entry claims an inflection is occurring (old: eel-alley-dawn-air → new: tallow-damp-lane-caulking) but loc-state:1 puts tallow-damp in place from the chapter's first beat. There is no prior ambient to delta from.

This is the loc-state-gap protoline failure mode: sensory:1 fires at @1 with no prior loc-state entry establishing the `eel-alley-dawn-air` baseline. The baseline cannot be derived.

Convergence-trace: No auditor finding in `facets-final-audit.md` covers this old-state lineage fault. flag-003 identifies the 7.7% density geometry issue (above-band) for the file as a whole, but does not surface the per-entry baseline-invention problem at sensory:1. This callout is independent of and additional to the auditor's findings.

**Verdict: REVISE.** The old-state `eel-alley-dawn-air` is unanchored — no loc-state entry at or before @1 establishes this baseline. Minimum resolution: (a) backfill a loc-state entry prior to @1 naming the pre-tallow ambient, OR (b) reframe sensory:1 as a scene-open establishment with old-state derived from the chapter's prior-chapter close (if that is accessible), OR (c) recognize that if tallow-damp is already the opening condition per loc-state:1, there is no delta to fire here — the entry should be deleted and the tallow-damp assigned to loc-state as a sustained baseline, not a sensory inflection.

---

### [sensory:2] @13 — `smell: tallow-damp-lane-caulking -> middens-discard-compound`

**ACCEPT — conditional note.**

Old-state claimed: `tallow-damp-lane-caulking`. Lineage walk:

Step 1: sensory:1 @1 fired on smell-modality; its new-state is `tallow-damp-lane-caulking`. The rubric permits old-state inheritance from the most recent prior sensory entry on the same modality. This is a valid chain: sensory:2 inherits from sensory:1's new-state.

Step 2: Most recent loc-state at or before @13: loc-state:3 @13 — `oc-pig-tallow-lane | morning | middens-junction-active, carter-work-ongoing | the discard-air sits heaviest at the junction-mouth.` New-state `middens-discard-compound` maps directly to loc-state:3's `discard-air sits heaviest.` Delta direction is correct: the scene moves from cooper's-yard tallow zone to pig-tallow-lane middens junction; the smell intensifies. Loc-state:3 grounds the new-state cleanly.

Step 3: Direct loc-state fallback is also available. loc-state:1 @1 names `tallow-damp-present`, which independently licenses `tallow-damp-lane-caulking` as an old-state description. Even if the prior-sensory chain is discounted (because sensory:1 itself has a baseline-invention fault), the direct loc-state derivation holds: tallow-damp is the established ambient of the eel-alley / cooper's-yard zone per loc-state:1.

Conditional note: the cleaner path is the sensory:1 new-state inheritance. If sensory:1 is deleted as part of resolution, the old-state must trace directly to loc-state:1 `tallow-damp-present` — which it can, without structural change to sensory:2.

Convergence-trace: No auditor finding targets sensory:2 old-state lineage. flag-003 is file-level only. sensory:2 survives both resolution paths for sensory:1.

**Verdict: ACCEPT** (old-state lineage holds via either the prior-sensory chain or the direct loc-state derivation; new-state grounded in loc-state:3).

---

### [sensory:3] @25 — `sound: carter-work-ambient -> roper's-court-near-silence`

**ACCEPT — inference gap noted, within rubric tolerance.**

Old-state claimed: `carter-work-ambient`. Lineage walk:

Step 1: No prior sound-modality sensory entry exists in this file (sensory:1 and :2 are both smell). Old-state must derive from loc-state.

Step 2: Most recent loc-state at or before @25 that names a sound-relevant condition: loc-state:3 @13 — `oc-pig-tallow-lane | morning | carter-work-ongoing.` `carter-work-ongoing` is a condition entry that licenses `carter-work-ambient` as the sound baseline carried from the prior location zone. The naming is a single-hop translation from condition-flag to sound-descriptor.

Step 3: loc-state:4 @25 — `oc-ropers-court | predawn | court-empty, far-tributaries-dark | the early-morning grey leaves the court sight-clear to all tributary mouths.` loc-state:4 names no explicit sound note. The new-state `roper's-court-near-silence` derives from `court-empty` and the predawn empty-court framing. Delta direction: the carter-work ambient of the prior zone drops away as Taylor enters the silent court. This is a cross-location transition-inflection: old-state is the sound of the zone left behind; new-state is the sound (near-silence) of the new zone.

Inference gap: loc-state:3 @13 is the pig-tallow-lane entry; `carter-work-ongoing` is that location's condition. The old-state `carter-work-ambient` derives from a different location's loc-state than the anchor protoline's own location (loc-state:4 is oc-ropers-court). The rubric requires the old-state to match "the most recent location-state file's § sensory or § conditions field for the beat's location, OR the most recent prior sensory-flag entry on the same modality." For sound-modality, with no prior sensory entry, the applicable loc-state is the most recent one prior to @25. loc-state:3 @13 is that entry; it is at a different location (pig-tallow-lane) from loc-state:4 (ropers-court). The rubric's phrasing is ambiguous about cross-location carry: "most recent location-state file's § conditions field for the beat's location" could be read as requiring the current location's loc-state (loc-state:4, which has no sound note) or as permitting the most recent loc-state overall (loc-state:3, which provides the sound basis).

The cross-location carry is the standard transition-inflection pattern: the old-state names the ambient that was present immediately before arriving at the new location. This is how sensory fires work at location transitions. loc-state:4's `court-empty` grounds the new-state directly. The inference from loc-state:3's condition `carter-work-ongoing` → old-state `carter-work-ambient` is single-hop and named. The delta is structurally defensible.

Convergence-trace: pass-007 (scene-map per-scene caps: sensory ≤3/scene PASS) is adjacent but does not address old-state lineage. No auditor finding targets sensory:3 old-state lineage.

**Verdict: ACCEPT** (old-state traces to loc-state:3's `carter-work-ongoing` via cross-location carry at scene transition; new-state grounded in loc-state:4 `court-empty`; inference gap minimal and within rubric tolerance).

---

## File-level old-state baseline summary

| entry | modality | old-state | loc-state anchor | lineage status |
|-------|----------|-----------|-----------------|----------------|
| sensory:1 @1 | smell | eel-alley-dawn-air | none — chapter-open, no prior entry | UNANCHORED |
| sensory:2 @13 | smell | tallow-damp-lane-caulking | sensory:1 new-state / loc-state:1 direct | VALID (dual path) |
| sensory:3 @25 | sound | carter-work-ambient | loc-state:3 @13 (carter-work-ongoing) | VALID (cross-location carry) |

One of three entries fails the old-state lineage gate. The cross-facet contract between loc-state and sensory is broken at the chapter-open entry.

---

## Convergence-trace (file-level)

- **sensory:1 unanchored old-state**: no auditor finding in `facets-final-audit.md` surfaces this. flag-003 identifies the density geometry issue (3/39 = 7.7% above 6%) but is file-level only and does not address per-entry baseline lineage. The unanchored old-state at sensory:1 is a new finding not overlapping any auditor flag. It independently warrants the revise verdict.
- **sensory:2 conditional validity**: no convergent auditor finding. Passes on both available derivation paths.
- **sensory:3 inference gap**: no convergent auditor finding. The cross-location carry is the expected pattern at scene transitions; the gap is within tolerance.

---

## VERDICT

**verdict: revise**

sensory:1 @1 fails old-state lineage review. The old-state `eel-alley-dawn-air` has no loc-state anchor: no prior loc-state entry at or before @1 names this ambient, and @1 is the chapter-open with no preceding entry to inherit from. Compound: loc-state:1 @1 places tallow-damp already present at the chapter-open, making the delta-from-prior-ambient structurally unsupported — there is no prior state to delta from.

sensory:2 and sensory:3 pass.

Minimum resolution paths for sensory:1:
(A) Delete sensory:1 — if tallow-damp is the chapter-open baseline (per loc-state:1), there is no inflection to flag; the entry is recording the opening condition, not a change.
(B) Revise the entry — if an inflection genuinely occurred (approaching the yard and crossing a threshold where the tallow-damp hit), backfill a loc-state entry or prior-chapter close-state that names the pre-tallow ambient, then anchor sensory:1's old-state to it.
(C) Reframe as prior-chapter carry — if the preceding chapter's close-state names an ambient smell (not tallow-damp), that entry provides the old-state basis; this requires cross-chapter loc-state consultation.
