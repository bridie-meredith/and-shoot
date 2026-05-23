---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 1
episode: b01c02
date: 2026-05-21
verdict: revise
---

# Verdict reasoning

I hold both files open: sensory.md and location-state.md. For each sensory fire I walk the lineage.

**sensory:1 @7** — old-state: `watch-press-alley-ambient`. Proto-line @7: `the city-watch passes the hook`. loc-state:5 @7 co-located: "the Hook corner: the specific point where the Watch column turns and loses sightline into the sealed alley." The loc-state entry names spatial position, not a sound baseline. The prior loc-state entries (@2 through @4) describe: doorway threshold geometry; alley-mouth framing; lane-mouths sealed by insect-mass. None of the four prior loc-state entries contain a `§ sensory` or conditions note naming `watch-press-alley-ambient` as the established ambient sound level.

The old-state `watch-press-alley-ambient` is the sensory entry's claim about what the sound level was before the column passed the Hook. That claim must trace to either (a) a prior loc-state sensory/conditions note, or (b) a prior sensory-flag entry on the sound modality. There is no prior sensory-flag in this file before sensory:1 (it is the first entry). There is no loc-state sensory note in entries @2-@6. The old-state `watch-press-alley-ambient` is unanchored — it is descriptively plausible (a watch press involves audible commotion in the broader street; `ambient` from that press is reasonable as a diegetic baseline) but it is not established in the loc-state file at any prior beat.

This is the loc-state-gap unanchored case per my card: the old-state has no verifiable loc-state lineage. I cannot verify the baseline was set. Flag.

Notably: the old-state is descriptively reasonable — watch-press-day morning conditions would plausibly generate an ambient street-level noise from the press activity. But descriptive plausibility is not lineage. The rubric requires the old-state to trace. It does not trace here.

REVISE: old-state lineage for sensory:1 is unanchored. The loc-state file must either (a) add a sensory/conditions note to one of the pre-@7 entries establishing `watch-press-alley-ambient` as the ambient baseline, or (b) the old-state must be rewritten to reflect what is actually anchored (the spatial-only baseline the loc-state provides).

**sensory:2 @22** — old-state: `unlit-lodging-interior`. loc-state:11 @22 co-located: "the lamp: single flame, tight radius, the ledger surface lit and the rest of the room falling off into dark." The loc-state entry at @22 describes the post-lamp state, not the pre-lamp state. The prior loc-state entry is loc-state:10 @17, which covers Flea Bottom exterior lane-mouth, outdoors. There is no loc-state entry between @17 and @22 covering the lodging interior in its pre-lamp state. The sensory entry's old-state `unlit-lodging-interior` claims a baseline — interior darkness before the lamp — that no loc-state entry establishes.

This is the loc-state-gap unanchored case: sensory:2 fires at @22 with an old-state that must be derived from a prior loc-state covering the interior darkness, but no such loc-state entry exists. The location change from exterior alley to interior lodging happens between @17 and @22 with no loc-state entry anchoring the interior's initial state. The sensory entry is firing against a baseline it invented.

REVISE: old-state lineage for sensory:2 is unanchored. The loc-state file must add an entry between @17 and @22 (or at the interior-entry beat) establishing the lodging's pre-lamp darkness state, so the sensory old-state `unlit-lodging-interior` has a traceable anchor.

Both entries fail old-state lineage. File cannot pass on my axis.

# Entry-level callouts

`[sensory:1] @7 — old-state "watch-press-alley-ambient" has no loc-state anchor. No loc-state sensory/conditions note in entries @2-@6 establishes this as the prior ambient level. Baseline unanchored.`

`[sensory:2] @22 — old-state "unlit-lodging-interior" has no loc-state anchor. loc-state:10 @17 covers exterior lane; no entry covers interior-lodging darkness prior to @22. Baseline unanchored.`

# Convergence trace

- sensory:1 @7 unanchored old-state: no direct auditor finding in `facets-final-audit.md`. The auditor's FREQUENCY-BAND section notes the short-chapter exemption applies and calls the file advisory; it does not run per-entry old-state lineage checks. The auditor CURVE-SHAPE section passes the sensory file on coverage grounds. The auditor RUBRIC-FIDELITY section does not touch sensory per-entry content. This finding is new relative to the mechanical audit.
- sensory:2 @22 unanchored old-state: same — no auditor finding surfaced this. The auditor's only sensory-specific engagement is the FREQUENCY-BAND exemption note. Old-state lineage is a cross-facet gate the mechanical audit's frequency-band and curve-shape classes do not check per-entry. Both findings are seams the auditor scan cannot surface; they require holding the loc-state file and tracing the old-state field's lineage beat by beat.
- The URI-FACETS-CYCLE-1 HARD finding from b01c01 (`sensory-old-state-reader flagged the unanchored old-state pattern across both entries`) is structurally analogous to both findings here. The same failure mode — firing without a prior loc-state anchor — repeats in b01c02. The rubric's §Axis-1 REJECT signature "Unanchored old-state (HARD)" (promoted from the b01c01 cycle-1 attack, URI-FACETS-CYCLE-1) directly covers both cases here.
