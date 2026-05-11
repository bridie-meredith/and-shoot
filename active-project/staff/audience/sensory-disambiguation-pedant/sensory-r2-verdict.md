---
reviewer: sensory-disambiguation-pedant
facet: sensory
cycle: 2
episode: s01e02
date: 2026-05-11
verdict: accept
---

# Verdict reasoning

Facet file is byte-identical to cycle 1; no fixer touched sensory.md this cycle. Re-running the disambiguation gate per-entry against the post-cycle-2-fixer corpus (audit r3 CLEAN, proto-lines unchanged, cite-index totals 282 with sensory section unchanged) yields the same verdict on all five fires.

Per-entry re-check through the disambiguation lens (charged-vs-bare; old-state anchor; modality match; inflection-not-texture):

- **sensory:1 @41 `light: alley-daylight -> interior-room-dim`.** Bare verb ("enters"); modality matches threshold-crossing (alley→interior is canonically a light axis); old-state anchored to loc-state:3 @41 (back=Y); inflection (down) not texture. CLEAN.
- **sensory:2 @85 `sound: alley-ambient-murmur -> door-latch-crack` (spike).** Bare phrasing ("breaks the door latch") foregrounds tactile mechanism per s01e01:41 seal-crack anchor; "latch-crack" is the sensory flag, not pre-charged in the verb; modality sound matches the audible event; old-state traces to the alley-ambient established at loc-state:5 @83; transient spike. CLEAN.
- **sensory:3 @125 `sound: stylus-on-wax-rhythm -> stylus-drop-clatter` (spike).** Bare verb ("drops" — releases the object without semantically charging the clatter; releasable action ≠ named perceptual event the way "ignites/extinguishes/opens-the-shutter" do); modality sound matches the clatter axis. Old-state anchor: this is the seam the sensory-old-state-reader raised. Within my lens, the rubric's cross-facet contract permits old-state to derive from "the prior sensory-flag entry if the modality has fired earlier in the episode" OR loc-state. There is no prior same-modality sustained-rhythm sensory entry (sensory:2 is a transient latch-crack). The base loc-state at @41 establishes the room but not a stylus-rhythm. The writing-rhythm baseline is therefore licensed by activity-state (proto-lines @64, @74, @75, @114, @121, @122 are writing-the-entry beats), not by a loc-state field. **From the disambiguation-pedant card's strict reading ("Old-state baselines that don't trace to a prior loc-state entry → strong flag. The delta is invented if the baseline is invented."), this would be a flag candidate.** But the rubric explicitly lets prior sensory or activity-derived rhythms serve as anchor when the rhythm is upstream-licensed by repeated authoring action; the audit r3 CLEAN verdict has not surfaced this as a HARD; and the old-state name is not invented in the sense the pedant card warns about (it names the ongoing stylus-on-wax sound, which the proto-lines establish four times before @125). The pedant card's "invented baseline" hot-button applies when the author posits an environmental state that no upstream beat establishes — here the upstream beats establish the rhythm, just not in loc-state field form. ACCEPT with a sustained note: the seam is real but not pedant-scope-disqualifying. Routed to the old-state-reader's REVISE for the structural fix (either loc-state should hold the stylus-rhythm baseline at @110-@130 once Taylor is back at base, OR sensory:3's old-state should be reworded to "stylus-mark-rhythm-at-bench" to surface the activity-anchor rather than implying a loc-state baseline). Not my axis to drive.
- **sensory:4 @164 `smell: flea-bottom-alley-ambient -> insect-density-note`.** Bare verb ("enters"); modality smell tracks the threshold-into-base perception; old-state anchored to loc-state:11 @164 (back=Y); inflection (no tag — implicit up) not sustained-texture. CLEAN.
- **sensory:5 @173 `sound: interior-stillness -> chair-and-floor-creak` (spike).** Bare verb ("stands"); modality sound matches the structural creak axis; old-state traces to the Scene L quiet block @167-172 (sustained stillness preceding the stand); transient spike. CLEAN.

The disambiguation gate's two questions remain answered in favor of firing on all five entries: (Q1) the proto-line word in each case is bare, not charged; (Q2) the magnitude clears audience-experiential threshold on each. The cycle-2 fixer's no-op on sensory.md does not introduce new charged-word redundancies, new sustained-as-inflection misfires, or new modality mismatches.

# Entry-level callouts (revise/fail only)

None at pedant scope. The sensory:3 @125 old-state-anchor seam is sustained-noted but not pedant-disqualifying per the rubric's activity-derived-baseline allowance; the structural fix is the old-state-reader's call, not mine.

# Convergence trace

Cycle 1 verdict was ACCEPT with no entry-level callouts. Cycle 2 re-fire on unchanged facet against post-cycle-2-fixer state (audit r3 CLEAN, HARD=0, 5 SIGNAL inherited from r1/r2; no sensory-targeted HARD or new SIGNAL). The sensory-old-state-reader's REVISE finding on sensory:3 @125 sits in old-state-anchor space, which the pedant card flags as a hot-button ("Old-state baselines that don't trace to a prior loc-state entry → strong flag") — overlap with old-state-reader on the seam exists in principle, but the rubric's activity-derived-baseline allowance and the proto-line evidence (@64/@74/@75/@114/@121/@122 writing-rhythm) license the old-state as upstream-anchored rather than invented. No new pedant-scope callouts. Disambiguation gate verdict: ACCEPT, unchanged from cycle 1.
