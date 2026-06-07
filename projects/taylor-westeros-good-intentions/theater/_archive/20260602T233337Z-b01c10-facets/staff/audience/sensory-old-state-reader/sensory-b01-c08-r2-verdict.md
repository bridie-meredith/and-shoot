persona: sensory-old-state-reader
facet: sensory
episode: b01c08
cycle: r2
verdict: accept
prior-verdict: revise (cycle r1)
blocking-finding-from-r1: HARD UNANCHORED-OLD-STATE on sensory:1 @10
updated: 2026-05-31
---

# Scope of cycle-2 review

Single question: does the HARD UNANCHORED-OLD-STATE finding on sensory:1 close?

The r1 verdict named the exact fix path required:
1. Studio adds sound annotation to loc-state:4 @9.
2. sensory:1 old-state revised to trace to that annotation (near-verbatim or verbatim match).

Both steps are reported as landed at cycle-2.

---

# Lineage walk — sensory:1 @10

## loc-state:4 check

loc-state:4 now reads:

> `@9 the-feed-station | afternoon | none | packet on intake surface | the Jarvis channel's intake station — a fixed-point receipt location inside the Hook coverage radius | sensory: enclosed-receipt-quiet`

The `sensory: enclosed-receipt-quiet` annotation is present. It is temporally adjacent to the sensory fire (loc-state @9, sensory fire @10 — one bone later, same location). The annotation names the acoustic baseline of the feed-station in this scene.

## sensory:1 old-state check

sensory:1 now reads:

> `1 @10 sound: enclosed-receipt-quiet -> wax-seal-crack # tag: spike`

Old-state: `enclosed-receipt-quiet`. This is a verbatim match to loc-state:4's `sensory: enclosed-receipt-quiet` annotation.

## Rubric Axis 1 resolution

The rubric states: "Anchored to a real perceptual baseline. The old-state matches the most recent location-state file's § sensory or § conditions field for the beat's location."

Most recent loc-state entry for the-feed-station prior to @10: loc-state:4 @9. That entry now carries `sensory: enclosed-receipt-quiet`. sensory:1's old-state is `enclosed-receipt-quiet` — verbatim match.

**UNANCHORED-OLD-STATE HARD finding: CLOSED.**

The lineage is: loc-state:4 @9 sensory field → sensory:1 @10 old-state. Direct, verbatim, locked-graph. The carve-out clause (a) retirement recorded in the facet header is correct — the series-class inference is no longer load-bearing; the anchor is now a locked-graph fact for this chapter.

---

# Remaining entry check — sensory:2 @16

sensory:2 was classified SOFT FLAG in r1. It remains unchanged. The r1 SOFT finding did not block acceptance and does not block here. The sensory:2 old-state "afternoon-stone-lane-light" still carries the thin-lineage condition: "afternoon" is confirmed by loc-state:2/@3 and loc-state:3/@4; "stone-lane-light" is a constrained location-type extrapolation. The delta direction and new-state are fully ratified by loc-state:5 @16 ("evening," "lit low").

This is not a blocking finding. No change in disposition from r1. Remains SOFT-documented in the facet header as an advisory note.

---

# File-level shape check

Two entries. Two modalities (sound, light). Bone count for b01c08: 24 bones. Short-chapter exemption applies (bone_count < 30). Two entries on 24 bones = 8.3%, above the standard 6% ceiling. Under the V3 exemption: when (a) bone_count < 30 AND (b) modality count equals the floor (2), effective ceiling is max(6%, 2/bone_count) = max(6%, 8.3%) = 8.3%. Two entries at 8.3% is exactly at the relaxed ceiling, not over it. Modality-floor met; cross-modal coverage met; short-chapter exemption holds.

No anti-patterns triggered. No cycle-N ADD without pre-validation concern (the fix path was an old-state revision and a loc-state annotation add — not an ADD of a new sensory entry).

---

# Verdict

**verdict: accept**

The HARD UNANCHORED-OLD-STATE finding that drove the r1 revise verdict is closed. The fix followed the exact path prescribed: loc-state:4 @9 received a `sensory: enclosed-receipt-quiet` annotation; sensory:1's old-state was revised to `enclosed-receipt-quiet` as a verbatim match. Rubric Axis 1 lineage is now traceable to a locked-graph anchor. sensory:2's SOFT thin-lineage condition is advisory-only and does not block. File-level shape passes under the V3 short-chapter exemption.

Facet passes cycle-2. No further revision required from this reviewer.
