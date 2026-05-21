---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 2
episode: b01-c01
date: 2026-05-20
verdict: revise
---

# Verdict reasoning

Cycle-1 I failed two entries on old-state lineage. sensory:1 @3 was a moderate finding — loc-state:1 exists, but "corner-room-dim" extrapolates past its explicit fields, which name a geometry cue ("door-shadow across the entry") not a declared interior light level. sensory:2 @16 was a HARD finding — loc-state:3 @11 had no thermal field and no prior sensory-thermal entry existed; "wall-daytime-ambient-warmth" was structurally unanchored.

The cycle-2 fixer resolved the HARD finding by cutting sensory:2. The unanchored thermal old-state no longer exists in the file. That finding is satisfied.

For sensory:1: the fixer added a defense-anchor comment under the entry:

> `# defense-anchor: old-state "corner-room-dim" is inferred from loc-state:1's "door-shadow across the entry"`
> `# geometry cue (shadow implies dim interior relative to exterior threshold) + the time-of-day implication`
> `# of pre-noon Hook arrival. Not a free-floating old-state; anchored to the loc-state:1 light-field geometry.`

I walk the lineage now.

The most recent prior loc-state at @3 is loc-state:1 @1. Its full text: `flea-bottom | morning | rain-recent | threshold-open | the door-shadow across the entry marks where the building-keeper stands`.

The defense-anchor argument is: "door-shadow across the entry" is a geometry cue; a shadow across the entry implies dim interior relative to exterior threshold; therefore "corner-room-dim" is anchored.

My rubric requires old-state to trace "verbatim or near-verbatim to a loc-state entry." I walk the specific test: does "corner-room-dim" appear verbatim or near-verbatim in loc-state:1? It does not. loc-state:1 names "the door-shadow across the entry" — a shadow placement, not a room illumination level. The defense-anchor comment asks me to accept a two-step inference: (1) a shadow across the entry implies the interior is dimmer than the exterior, (2) therefore "corner-room-dim" is a valid old-state name. That inference is plausible. It is not the same as explicit anchoring.

The rubric's Axis 1 (modality-inflection) REJECT signature states: "Unanchored old-state (HARD). Entry's old-state does not resolve to (a) the most recent loc-state file's § sensory or § conditions baseline for the beat's location, OR (b) the most recent prior sensory-flag entry on the same modality." loc-state:1 has no § sensory or § conditions field. It has a spatial description that includes a shadow cue. The question is whether a shadow cue in a spatial description field constitutes a "light-field baseline" for sensory-flag old-state sourcing.

I will not call this HARD in cycle-2. The cycle-1 finding was already graded as moderate (loc-state exists, inference is plausible, not the absence case). The defense-anchor comment is the minimum-change response the fixer could apply without editing loc-state:1 or cutting sensory:1. The fixer explicitly chose not to add a light-level field to loc-state:1 — that would have been the clean resolution.

But the defense comment does not satisfy my standard. A comment in the sensory file asserting that an inference licenses the old-state is not the same as loc-state:1 declaring the light level. My rubric asks for explicit lineage, not documented inference. The shadow cue in loc-state:1 is a geometry fact, not a light-level declaration. A reader opening loc-state:1 cold does not see a declared interior light level; they see a shadow position.

I hold a revise verdict. The required fix remains what I stated in cycle-1: studio adds an explicit light-level note to loc-state:1 (e.g., "threshold-dim, interior backlight filtered by overcast morning") that makes "corner-room-dim" near-verbatim traceable. The defense-anchor comment is advisory; it is not a lineage chain.

Downgrade from fail to revise: cycle-1 was a fail (two entries, both with broken lineage). In cycle-2, one finding is resolved (sensory:2 cut). One entry remains with an insufficiently resolved old-state. One entry, one moderate finding, correct modality, no structural-absence failure. This is a revise, not a fail.

# Entry-level callouts

[sensory:1] @3 — old-state `corner-room-dim` insufficiently anchored. loc-state:1 @1 names "door-shadow across the entry" — a shadow-position geometry descriptor, not a declared interior light level. The defense-anchor comment correctly identifies the inference chain but does not constitute explicit loc-state anchoring. Required fix: add an explicit light-level note to loc-state:1 (interior threshold illumination quality, e.g., "threshold-dim, morning-backlight filtered by overcast") so that "corner-room-dim" traces near-verbatim to a loc-state field.

# Convergence trace

- [sensory:1] @3 baseline-extrapolation — original to cycle-1 review; not surfaced by the mechanical auditor (contradiction-check looks for explicit contradiction, not for absence of explicit anchoring; this seam is a lineage-gap, not a contradiction). The cycle-2 defense-anchor comment addresses the gap by inference documentation, not by explicit loc-state revision. My finding persists.
- [sensory:2] @16 unanchored old-state — RESOLVED by cut. Convergent with URI-FACETS-CYCLE-1 HARD anti-pattern (rubric-sensory.md §1). The entry no longer exists; the finding is satisfied.
- [sensory:1] @3 — downgrade from fail-driver to revise: cycle-1 was a moderate finding alongside the HARD sensory:2 finding; together they produced a fail. With sensory:2 gone, the remaining finding is a revise-class lineage gap, not a structural absence.
