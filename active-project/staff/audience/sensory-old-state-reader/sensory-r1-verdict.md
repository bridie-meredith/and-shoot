---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 1
episode: b01-c01
date: 2026-05-20
verdict: fail
---

# Verdict reasoning

Two entries. Both carry old-states with broken or absent loc-state lineage. I walk the lineage for each.

sensory:1 @3 `light: corner-room-dim -> overcast-yard-diffuse` — I need the most recent prior loc-state entry at @3. That is loc-state:1 @1 (`flea-bottom | morning | rain-recent | threshold-open | the door-shadow across the entry marks where the building-keeper stands`). The loc-state:2 @3 entry is co-anchored with sensory:1 at the same protoline — it describes the yard-open state FROM @3, so it governs the new-state, not the old-state baseline. The old-state must derive from loc-state:1.

What does loc-state:1 give me for light? "threshold-open" and "door-shadow across the entry." That is a geometry description and a partial light cue — a shadow across the entry implies the threshold is dim relative to outside. "Corner-room-dim" requires me to infer: (1) Taylor was in the corner-room, (2) the corner-room is dim, (3) "door-shadow" licenses "corner-room-dim" as the old-state name. Step (1) is confirmed by proto-line @1 (`taylor-hebert-kl-122ac enters the corner-room [loc-state:1]`). Steps (2) and (3) are extrapolations. loc-state:1 does not declare a named light level for the corner-room interior. "Corner-room-dim" is not near-verbatim to any loc-state:1 field. The rubric requires old-state to trace "verbatim or near-verbatim to a loc-state entry." This entry extrapolates past what loc-state:1 explicitly states.

I distinguish this from the unanchored case: there IS a prior loc-state entry (loc-state:1 @1). The lineage is present but the old-state name is inventively filled in beyond what the loc-state field licenses. This is a baseline-extrapolation problem, not a structural absence. I flag it as a moderate finding — the loc-state exists and the inference is plausible, but the cross-facet contract requires explicit anchoring, not plausibility. Studio needs to add a light-level field to loc-state:1 (e.g., "threshold-dim, morning-backlight filtered by overcast") to make the old-state traceable.

sensory:2 @16 `thermal: wall-daytime-ambient-warmth -> wall-surface-cooling` — I walk the lineage. The most recent prior loc-state at @16 is loc-state:3 @11 (`flea-bottom | midday | overcast | yard-open, net-work-set | continuity-from 2: tallow-smoke from the rendering-alley still threading across the yard`). loc-state:4 is at @18, after sensory:2.

Does loc-state:3 @11 establish a thermal baseline? No. loc-state:3 names midday, overcast, yard-open, and a smell continuity note (tallow-smoke). No thermal field. No prior sensory-flag entry on thermal modality exists — sensory:1 is on light, not thermal. So there is NO baseline for "wall-daytime-ambient-warmth" derivable from either:
- The most recent loc-state (loc-state:3 @11, no thermal field), or
- A prior sensory-flag on the same modality (none exist).

This is the unanchored old-state failure mode: "A sensory fire at a protoline that has NO prior loc-state entry establishing a baseline is unanchored." The rubric specifically promoted this pattern to a HARD anti-pattern via URI-FACETS-CYCLE-1 (2026-05-19), citing prior audience-gate attacks on this very episode's sensory entries. "wall-daytime-ambient-warmth" is invented for this entry. There is no loc-state thermal field from which it can be derived. The delta is asserting a baseline the file does not establish.

Both entries fail lineage verification. sensory:2 is the stronger failure (structurally unanchored — no thermal loc-state field exists at all). sensory:1 is a weaker failure (loc-state exists but old-state naming extrapolates beyond its explicit fields). The file cannot stand on either entry as currently anchored.

# Entry-level callouts

[sensory:1] @3 — old-state `corner-room-dim` extrapolates past loc-state:1 @1. loc-state:1 names "door-shadow across the entry" — a geometry cue, not a named interior light level. "Corner-room-dim" is not traceable near-verbatim to any loc-state:1 field. Studio must add an explicit light-level note to loc-state:1 (e.g., interior threshold illumination quality) for this old-state to be anchored.

[sensory:2] @16 — old-state `wall-daytime-ambient-warmth` is unanchored. The governing loc-state at @16 is loc-state:3 @11; it has no thermal field. No prior sensory-thermal entry exists. There is no loc-state lineage for this old-state. The entry fires a thermal delta against a baseline the file never establishes. This is the URI-FACETS-CYCLE-1 unanchored-old-state HARD pattern applied directly. Studio must backfill a thermal baseline in loc-state:3 (or an earlier loc-state) before this entry can be anchored, or the entry must be deleted.

# Convergence trace

- [sensory:2] @16 unanchored old-state — convergent with URI-FACETS-CYCLE-1 promotion in rubric-sensory.md §1 (HARD anti-pattern added 2026-05-19: "sensory-old-state-reader specialist flagged the unanchored old-state pattern across both entries"). The rubric explicitly records this failure mode as having been flagged in a prior audience-gate cycle on this episode. My reading confirms the pattern persists in the current file.
- [sensory:2] @16 — convergent with auditor S-008 (r1, FREQUENCY-BAND: sensory breach-high). Striking sensory:2 resolves the frequency-band overrun; my finding is independent and arrives via lineage failure, not density arithmetic.
- [sensory:1] @3 baseline-extrapolation — not surfaced by the r1 or r2 auditor. The mechanical audit's loc-state-contradiction check looks for explicit contradiction, not for absence of explicit anchoring. This seam is original to this review.
