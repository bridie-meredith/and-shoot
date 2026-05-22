---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 2
episode: b01c02
date: 2026-05-21
verdict: accept
---

# Verdict reasoning

Cycle-1 findings: both old-states unanchored. Fix added conditions notes to loc-state:2 @4 (anchor for sensory:1) and loc-state:11 @22 (anchor for sensory:2); sensory:2 relocated @22→@23. I hold both files and re-walk the lineage for each entry.

**sensory:1 @7 — sound: watch-press-alley-ambient -> watch-column-footfall**

Cycle-1 finding: no loc-state sensory/conditions note in entries @2-@6 established the ambient-sound baseline. Fix: loc-state:2 @4 now carries a conditions note — "ambient-sound baseline before column arrival — ordinary morning street noise and shoe-leather on cobbles; no column-echo yet; this is the watch-press-alley-ambient state (anchor for sensory:1 old-state)."

Lineage walk: loc-state:2 @4 conditions note explicitly names `watch-press-alley-ambient` as the prior ambient baseline and marks it as the sensory:1 anchor. sensory:1 fires at @7 — three beats later, same location (flea-bottom), same morning-watch-press-day scene. No intervening loc-state entry between @4 and @7 introduces a sound-level change: loc-state:3 @5 describes lane-mouth sealing by insect-mass (spatial geometry, not sound); loc-state:4 @6 describes Wren at far threshold (spatial, not sound); loc-state:5 @7 is co-located with sensory:1 and describes the Hook spatial position (no sound-level change). The ambient baseline established at @4 carries unbroken to @7. Old-state traces directly to loc-state:2 @4 conditions note. No contradiction; no chain-skip.

PASS.

**sensory:2 @23 — light: unlit-lodging-interior -> lamp-lit-tight-radius**

Cycle-1 finding: no loc-state entry between @17 and @22 established the lodging's pre-lamp darkness. Fix: (a) loc-state:11 @22 now carries a conditions note — "interior-darkness baseline before @22 — lodging-interior unlit, night scene-open (time-skip blank @21); this is the unlit-lodging-interior old-state (anchor for sensory:2 old-state at @23)"; (b) sensory:2 anchor relocated to @23.

Lineage walk: the conditions note on loc-state:11 @22 explicitly names `unlit-lodging-interior` as the pre-lamp darkness baseline and identifies itself as the anchor for sensory:2. The note grounds the darkness in the time-skip blank at @21 (scene-open at night, interior unlit from scene entry). sensory:2 fires at @23, claiming `unlit-lodging-interior` as old-state. The derivation chain: time-skip @21 establishes night interior entry; loc-state:11 @22 conditions note records pre-lamp darkness baseline; sensory:2 @23 inherits that baseline as old-state. Chain is explicit and traceable.

I check for contradiction: at @23 the most-recent loc-state is loc-state:11 @22, whose conditions note describes the pre-@22 darkness. The main body of loc-state:11 @22 describes the post-lamp state ("lamp: single flame, tight radius"). The old-state in sensory:2 uses the pre-lamp darkness (from the conditions note), not the post-lamp state (from the main body). The conditions note explicitly frames the darkness as "baseline before @22" — this is the state the sensory entry is inheriting. No contradiction with the main-body post-lamp description, because the sensory entry is describing the transition FROM the darkness state that obtained before @22, not re-describing the current-at-@23 state.

Modality chain: light modality has no prior sensory-flag in this file before sensory:2 (sensory:1 is on sound). Old-state must trace to loc-state — it does, via the conditions note. Chain-skip test: no loc-state between @17 and @23 covers the lodging interior except loc-state:11 @22, which is the anchor. No skip.

Timing note (staying in my lane): sensory:2's old-state refers to the pre-@22 darkness; the fire is at @23. The old-state traces correctly to the pre-@22 conditions note. Whether @23 is the right inflection beat for this fire is an inflection-not-sustained question — that is the disambiguation-pedant's axis, not mine. My axis is lineage only: does the old-state trace to a loc-state entry? Yes. Does it contradict that entry? No. PASS on lineage.

Both old-states now have verifiable loc-state lineage. No invented baselines. No contradictions. No chain-skips.

ACCEPT.

# Entry-level callouts

None. Both old-state lineages trace cleanly after the conditions note additions.

Cycle-1 findings resolved:
- `[sensory:1] @7 unanchored` → resolved by loc-state:2 @4 conditions note naming `watch-press-alley-ambient` as the ambient baseline anchor.
- `[sensory:2] @22 unanchored` → resolved by loc-state:11 @22 conditions note naming `unlit-lodging-interior` as pre-lamp darkness baseline; relocation to @23 does not disturb the lineage claim.

No new lineage-invention or lineage-contradiction seams introduced by the fix.

# Convergence trace

- Cycle-1 unanchored-old-state findings: directly addressed by conditions note additions. The fix followed the rubric §Axis-1 prescribed path ("backfill the loc-state baseline"). Conditions notes are a correct vehicle for baselines that predate the anchor beat without requiring a new standalone loc-state entry.
- A3 sequencing (rubric §14 anti-pattern URI-FACETS-V3-CYCLE-N-ADD): fix-log item 8b confirms upstream loc-state conditions notes landed first before sensory entries updated. The sequencing requirement is met. The conditions notes are in place before the sensory old-state claims depend on them.
- URI-FACETS-CYCLE-1 HARD (unanchored old-state): both instances resolved. The conditions-note mechanism correctly backfills baseline anchors that were established by narrative context (watch-press-day morning ambient; night interior at scene-open) but not formally documented in the loc-state file until cycle-2.
- Cite-index: sensory:2 now at @23, co=[exposition:5, state:5]. loc-state:11 @22 co-citations updated (sensory:2 removed from @22 co-citations). The cross-file consistency supports the lineage trace — no residual @22 citation for sensory:2 that would suggest a lingering anchor conflict.
- Disambiguation-pedant cycle-2 and modality-coverage cycle-2 both surface concerns about the @23 anchor. Those concerns (inflection-beat-lagging; inflection-skip at @22) are outside my axis. I note their convergence here for the orchestrator's aggregation but do not let them migrate into my lineage verdict. The lineage is clean; the inflection-beat problem is theirs to name.
