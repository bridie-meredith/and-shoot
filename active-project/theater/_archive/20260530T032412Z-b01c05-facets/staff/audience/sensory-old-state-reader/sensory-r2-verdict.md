---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 2
episode: b01-c01
date: 2026-05-25
verdict: revise
---

# Cycle-2 context

Cycle-1 ACCEPT was against sensory:2 @16 (sound: crowd-ambient-murmur -> taylor-raised-voice). That entry's old-state traced to bones 7-11 — crowd, fish-cart, lane-mouth, lane-occupancy context — a genuine scene-stated sound ambient. I held. The fixer then REPLACED sensory:2 entirely: deleted the @16 sound entry, wrote a new @9 tactile entry (tactile: lane-ambient -> crowd-compression). The facet changed. My prior accept does not carry.

# Entry-level callouts

[sensory:2] @9 — old-state "lane-ambient" on tactile modality. Lineage walk:

Step 1 — most recent loc-state entry at this beat: loc-state:1 @1. Read its content: `oc-stitch-house-lane | morning | none | stitch-house-lamp-burning | drain-water trickle audible at the angle-gap pinch-point`. The entry's sensory note is auditory — drain-water trickle. No tactile field. loc-state:1 does not establish a tactile baseline. The loc-state path fails.

Step 2 — most recent prior sensory entry on tactile modality: none. sensory:1 fires on smell. No prior tactile sensory entry exists in the file. The prior-sensory path fails.

Both rubric-enumerated anchoring paths (rubric-sensory.md §1: "the most recent location-state file's § sensory or § conditions field for the beat's location, OR the most recent prior sensory-flag entry on the same modality") are empty on tactile. The old-state "lane-ambient" is a free-floating tactile description with no traceable anchor in either file.

The carve-out header claims a third path: "scene-internal sensory context established by bones 1-8." The rubric does not enumerate this path. The rubric's REJECT signature is explicit: "Either backfill the loc-state baseline OR cite a prior sensory entry." The carve-out's cited instruction — "treat scene-internal sensory anchors as scene-tier sensory when the locations: header is empty" — does not appear in rubric-sensory.md anywhere in the text I hold. The carve-out is invoking an instruction the rubric does not contain.

The carve-out's own factual premise is also stale. It states "no location-state file entries exist for b01c01." loc-state:1 now exists, added at @1 by the cycle-1 dark-fantasy-reader remediation. The zero-entry condition that grounded the carve-out no longer holds. This does not help sensory:2's old-state (loc-state:1 still provides no tactile field), but it means the carve-out's structural justification is misrepresenting the current loc-state.

Bones 1-8 do not name a tactile ambient state. "Lane occupied but not crowd-compressed" is a negative inference — the crowd compresses at bone 9, so before bone 9 it was not compressing, therefore the old tactile state was pre-compression ambient. That is a derivation from the absence of the new-state event, not a positive statement of a prior tactile baseline. It is the same negative-inference structure I flagged as the thinnest possible carve-out application for sensory:1 @2's smell old-state in cycle 1, but weaker: for smell, bone 2 at least names the onset event directly (tallow smoke crosses), so "pre-bone-2 = pre-smoke" has a positive anchor in the prose. For tactile, no bone names a tactile state at all before @9.

Anti-pattern #14 pre-validation logged in the header claims old-state lineage cleared. The anti-pattern's requirement is "old-state lineage from loc-state or prior sensory entry on the same modality." The pre-validation satisfies this claim only by relying on the unenumerated scene-internal path. The check passed itself on a path the rubric does not authorize. This is a pre-validation that reached a conclusion the rubric does not support.

VERDICT: [sensory:2] @9 — unanchored-old-state HARD. loc-state:1 supplies no tactile field; no prior sensory entry on tactile exists; the carve-out's scene-internal path is not enumerated in the rubric; the carve-out's factual premise is stale. The inflection is asserted against a tactile baseline the file does not establish.

# Sensory:1 status

[sensory:1] @2 — no change from cycle-1 assessment. Old-state "lane-ambient" on smell modality remains a negative-inference derivation (smoke first appears at bone 2, so pre-bone-2 = pre-smoke), and this is still the thinnest defensible application of the carve-out. The cycle-1 advisory note stands. No new HARD here.

# Convergence trace

fault-C2C-001 (auditor cycle-2 confirm): identifies the broken sensory:2 @16 citations in the dialogue sidecar (entries 1 and 2 reference a sensory:2 anchor that no longer resolves in the cite-index). That is a downstream consequence of the fixer's anchor move. The old-state lineage finding here is upstream of that fault — the new @9 tactile entry is itself not rubric-grounded on old-state; downstream citation problems compound the upstream problem.

flag-C2C-003 (carried forward): flag-C2-001 (sensory carve-out header factual premise stale) is directly confirmed here — the "no location-state file entries exist" claim is false after cycle-1 loc-state:1 addition.

# Required correction path

The rubric names two resolution paths: (1) backfill the loc-state baseline — add a tactile field or tactile-ambient note to loc-state:1 (or a new loc-state entry) that establishes the pre-compression tactile state for oc-stitch-house-lane; then update sensory:2's old-state to match. (2) Demonstrate a prior sensory entry on tactile — which would require adding one earlier in the file, itself requiring the same anchor problem solved at that earlier beat. Path 1 (loc-state edit first) is the correct resolution sequence per rubric §1 and anti-pattern #14.

Until loc-state:1 is updated to carry a tactile note establishing the lane-ambient-tactile baseline, sensory:2's old-state is unanchored and the entry does not pass the rubric.
