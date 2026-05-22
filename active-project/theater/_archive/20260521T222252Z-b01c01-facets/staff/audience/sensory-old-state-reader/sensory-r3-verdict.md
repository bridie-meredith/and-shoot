---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 3
episode: b01-c01
date: 2026-05-20
verdict: revise
---

# Verdict reasoning

Cycle-2 I held a revise. My finding: sensory:1 @3's old-state "corner-room-dim" required an explicit light-level field in loc-state:1, not just the inference-chain through "door-shadow across the entry." The fixer's cycle-2 defense-anchor comment documented the inference correctly but did not constitute explicit loc-state anchoring. I demanded: add an explicit light-level note to loc-state:1 so "corner-room-dim" traces near-verbatim.

Cycle-3 addresses that demand and introduces one new entry. I walk both now.

## sensory:1 @3 — light: corner-room-dim -> overcast-yard-diffuse

My cycle-2 revise finding: resolved.

The cycle-3 fix added an explicit light field to loc-state:1 @1: `light: threshold-dim, interior-corner dim under overcast morning backlight`.

Lineage walk: loc-state:1 @1 is the most recent prior loc-state entry before @3. Its light field now reads: "threshold-dim, interior-corner dim under overcast morning backlight." sensory:1's old-state is "corner-room-dim." I apply my near-verbatim test: "interior-corner dim" against "corner-room-dim." These are near-verbatim. "Interior-corner" and "corner-room" describe the same spatial register. "Dim" is shared. The modifier "under overcast morning backlight" contextualizes the source. Single-step lineage: loc-state:1 light field → sensory:1 old-state. Not two-step inference through shadow geometry. The explicit field is present and the trace is direct.

My cycle-2 demand is met. sensory:1 PASS.

## sensory:3 @17 — sound: street-quiet-of-mid-afternoon -> bootfall-on-cobbles-from-the-Hook-bend

This entry is new. I walk its old-state lineage cold.

Old-state: `street-quiet-of-mid-afternoon`

I identify the most recent prior loc-state entry at @17. Walking the loc-state file:
- loc-state:1 @1: flea-bottom | morning | rain-recent | threshold-open | light field added
- loc-state:2 @3: flea-bottom | morning | rain-recent | mud-recent, yard-open
- loc-state:3 deleted (F-007)
- loc-state:4 @18: flea-bottom | afternoon | overcast | cobbles, hook-corner-visible
- loc-state:5 @22: flea-bottom | afternoon | overcast | street-open

The most recent prior loc-state before @17 is loc-state:2 @3. That entry reads: `flea-bottom | morning | rain-recent | mud-recent, yard-open | the far-yard drain-channel at the distance where Coll works the net`. It has no sound field. It declares time = morning. It describes the yard, not the street.

The old-state of sensory:3 is `street-quiet-of-mid-afternoon`. I apply the lineage test:

1. "street-quiet" — does this trace to any loc-state field before @17? No. loc-state:2 @3 is yard-context, no sound field. No prior loc-state entry declares a street-sound baseline on the sound modality. There is no sound-modality prior sensory entry (sensory:2 was deleted). No loc-state carries "street-quiet" or any equivalent sound baseline for the Hook exterior at any point before @17.

2. "mid-afternoon" — does this trace to any loc-state field before @17? No. loc-state:4 declaring afternoon fires at @18 — one beat after @17. loc-state:2 @3 declares morning. There is no loc-state between @3 and @18 (loc-state:3 deleted at F-007). The afternoon time-of-day at @17 is not established by any prior loc-state entry.

The old-state "street-quiet-of-mid-afternoon" is not traceable to any prior loc-state entry or prior sensory entry on the sound modality. This is the unanchored-old-state pattern named in my card's loc-state-gap-protoline failure mode: "A sensory fire at a protoline that has NO prior loc-state entry establishing a baseline is unanchored." At @17, no loc-state has established a street-sound baseline, and no prior sensory-sound entry exists (sensory:2 was the only sound-candidate and was deleted). The old-state is a free-floating baseline invented for this entry.

Additionally, the time component — "mid-afternoon" — is not yet established at @17. loc-state:4 @18 establishes "afternoon" one beat later. The sensory entry's old-state asserts a time-of-day context the loc-state file does not declare until the next beat. This is a forward-reference masquerading as an old-state: the afternoon palette is one beat downstream, not yet present.

**This is a HARD finding under my rubric.** Entry's old-state does not resolve to (a) the most recent loc-state file's sensory or conditions baseline (loc-state:2 @3 is morning, yard, no sound field) OR (b) a prior sensory-flag entry on the sound modality (none exists). "street-quiet-of-mid-afternoon" is structurally unanchored.

Required fix: one of the following paths —
- (a) Add a sound-baseline studio note to loc-state:2 @3 (or a new loc-state entry before @17) establishing the Hook exterior street-sound as "street-quiet" in the afternoon approach to the Watch pass. This gives the old-state a loc-state lineage.
- (b) Revise the old-state name to trace to what loc-state:2 actually establishes — but loc-state:2 is yard-context with no sound field, so this path requires a loc-state edit regardless.
- (c) Revise sensory:3's old-state away from a time-of-day-stamped street baseline to a formulation derivable from what the bones establish by narrative progression — but narrative progression alone is not a rubric-valid old-state source; loc-state is the required anchor.

The simplest fix: add an explicit sound-baseline note to loc-state:4 @18 that retroactively (as a carry-forward note) establishes the pre-Watch street ambient — but this has the same forward-reference problem since @18 is after @17. The correct fix is a studio note at or before @17 on the sound modality declaring "street-quiet" as the ambient level. loc-state:2 @3 is the nearest prior anchor point; a sound-field addition there would cover the gap.

## Verdict

sensory:1: PASS (cycle-2 demand met; explicit light field in loc-state:1 makes "corner-room-dim" near-verbatim traceable).

sensory:3: HARD FINDING — old-state "street-quiet-of-mid-afternoon" unanchored. No prior loc-state entry establishes a street-sound baseline before @17. "mid-afternoon" time-of-day not declared by any loc-state before @17 (loc-state:4 fires at @18). Free-floating baseline.

Overall verdict: **revise**. One entry passes; one entry carries a HARD unanchored-old-state finding.

# Entry-level callouts

[sensory:1] @3 — RESOLVED. Cycle-2 demand (explicit light field on loc-state:1) met. "interior-corner dim" in loc-state:1 traces near-verbatim to "corner-room-dim" in sensory:1 old-state. Single-step lineage. PASS.

[sensory:3] @17 — HARD FINDING. Old-state `street-quiet-of-mid-afternoon` unanchored. Most recent prior loc-state is loc-state:2 @3 (morning, yard, no sound field). No prior sensory-sound entry exists. "mid-afternoon" time-of-day not established by any loc-state before @17; loc-state:4 @18 establishes afternoon one beat later. The baseline is invented: no loc-state or prior sensory entry on the sound modality establishes "street-quiet" or "mid-afternoon" before @17. Required fix: add explicit sound-baseline note (establishing Hook exterior street-ambient as quiet before the Watch pass) to loc-state:2 @3 or to a new loc-state entry before @17.

# Convergence trace

- [sensory:1] @3 lineage gap — RESOLVED. My cycle-1 (fail) and cycle-2 (revise) findings demanded an explicit loc-state:1 light field. Cycle-3 fix delivered it. Near-verbatim trace confirmed. Finding closed.
- [sensory:3] @17 unanchored old-state — NEW finding, not surfaced in prior cycles (entry did not exist). Not present in any prior auditor report (the entry is cycle-3-new). My old-state lineage walk is the first pass against this entry. The HARD finding is original to this cycle-3 review.
- No convergence with mechanical auditor findings on this new entry (cite-index shows @17 was a bare protoline before cycle-3; no prior facet decoration; no prior auditor finding on the sensory old-state axis for @17).
