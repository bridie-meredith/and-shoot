---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 3
episode: b01c01
date: 2026-05-19
verdict: accept
---

# Verdict reasoning

Cycle-3 introduced one structural change with old-state-lineage consequences: the cut of sensory:2 @9 destroyed the sound-modality chain's only prior anchor for the surviving sensory:2 @15 (was sensory:3). The within-cycle remediation added a loc-state:2 @9 studio note to re-establish that anchor. I read both surviving entries against both files.

## sensory:1 @1 — smell: tallow-smoke-ambient -> tallow-smoke-room-density

Old-state-source token: `loc-state:1 sensory-baseline-note (smell: tallow-smoke-ambient, Hook-alley exterior morning; documented in location-state.md @1 studio note, cycle-2 ratification 2026-05-19; rendered-fat component removed — loc-flea-bottom §Sensory localizes that note to the rendering yards not the Hook alley exterior)`

Lineage walk: loc-state:1 @1 exists. The studio note at loc-state:1 reads: "smell at loc-state:1 = tallow-smoke-ambient (Hook-alley exterior, morning; sourced from loc-flea-bottom card §Sensory palette + b01c01 chapter-layer canonical usage; tallow-smoke carries at range from the rendering yards into the Hook alley; rendered-fat token removed...)." The old-state `tallow-smoke-ambient` traces exactly to this note. The new-state `tallow-smoke-room-density` describes the intensification when crossing the threshold into the interior. No loc-state contradiction exists. No inheritance skip. Delta direction consistent with a threshold-crossing (exterior ambient → interior density). Old-state is anchored. PASS.

Note: loc-state:1 @1 also carries a second studio note documenting the now-cut sound baseline (corner-room-interior-quiet). The note correctly appends a cycle-3 lineage clarification: the sound chain from corner-room-interior-quiet is no longer active; the surviving sound entry anchors to loc-state:2 @9. I read this as housekeeping, not a new sensory-1 problem. The smell-chain for sensory:1 is unaffected.

## sensory:2 @15 — sound: hook-street-ambient -> watch-column-passing

Old-state-source token: `loc-state:2 sensory-baseline-note (sound: hook-street-ambient post-door-open baseline established at @9; documented in location-state.md @9 studio note, cycle-3 within-cycle remediation 2026-05-19)`

Lineage walk: loc-state:2 @9 exists. The cycle-3 within-cycle studio note reads: "sound at loc-state:2 = hook-street-ambient (Hook street-level sound baseline established at the door-open-street-facing transition; with the facing door open, the interior acoustic environment shifts from corner-room-interior-quiet to the street-level ambient of Hook alley foot-traffic and waterfront district activity; this is the established post-door-open sound baseline that persists through @15 until the Watch column spike at sensory:2 @15; sourced from loc-flea-bottom card §Sensory palette [Hook-alley street-level sound] + cond-kl-geography-122ac...)."

The old-state `hook-street-ambient` traces to this note verbatim. The note is correctly authored: it identifies `sound: hook-street-ambient` as the baseline, sources it to loc-flea-bottom and cond-kl-geography-122ac, explains the mechanism (door-open-street-facing acoustic transition), marks the persistence range (@9 through @15), and explicitly names its function as the old-state anchor for sensory:2 @15.

The new-state `watch-column-passing` is a transient spike above the hook-street-ambient baseline. The delta direction is consistent with loc-state:3 @15's content ("the Watch column passes at the Hook's curve — visible from the corner-room's street-facing side"). Sound accompanies the Watch column; no charged word in the proto-line self-carries the acoustic profile. The delta is coherent with the loc-state narrative at @15. PASS.

## Cite-index AUDIT-NOTE status

The cite-index at `_cite-index.md` carries an AUDIT-NOTE: "sensory:2 @15 old-state `hook-street-ambient` has no old-state-source token; unanchored-old-state HARD finding raised in cycle-3 audit report." This note documents the pre-remediation state. The remediation (within-cycle studio dispatch, 2026-05-19) added the old-state-source token to sensory:2 @15 in sensory.md and added the loc-state:2 @9 studio note in location-state.md. The cite-index note is a historical artifact. The sensory.md file itself — the authoritative source — now carries the token. I read the token as present and valid. The HARD finding is resolved.

## Full anchor summary

- sensory:1 @1: old-state `tallow-smoke-ambient` → loc-state:1 @1 studio note (smell). Anchored. Pass.
- sensory:2 @15: old-state `hook-street-ambient` → loc-state:2 @9 studio note (sound). Anchored. Pass.

Both surviving entries have anchored old-states tracing to authored studio notes with named sources. No free-floating baselines. No loc-state contradictions. No inheritance skips.

# Convergence trace

The unanchored-old-state HARD finding (fault-C3-001 in the cycle-3 audit) drove the within-cycle remediation. The resolution path taken — adding a sensory-baseline studio note at loc-state:2 @9 as Path (a) anchor per rubric §1 — is the correct rubric-sanctioned resolution. I find the anchor present, correctly authored, and sufficient.
