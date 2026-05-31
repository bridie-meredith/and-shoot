facet: sensory
episode: b01c06
author: studio
---

# rubric-carve-out — pressure old-state sourced from location card baseline (no loc-state pressure entry)
#
# design/shoot-v2/rubric-sensory.md § 1. Modality-inflection / Anchored to a real perceptual baseline
#
# Carve-out scope: sensory:1 @2 (pressure fire in scene-A)
# Carve-out rule: old-state `lane-passable-morning-flow` is sourced from the location card's
#   §Geography and §Hazards sections (oc-stitch-house-lane: "Width: one cart plus pressed shoulders";
#   "crowd compression blocks retreat") rather than from a loc-state entry, because the loc-state file
#   for b01c06 opens at @1 with the blocked/crowd-backed state already established — no pre-blockage
#   loc-state entry exists for this chapter. Precedent: b01c05 sensory:1 used `lane-stone-surface-baseline`
#   derived from the location card's tactile vocabulary (documented in studio state.md 2026-05-28).
#   The location card's §Hazards baseline is the authoritative source for lane-pressure state before
#   crowd-compression; it qualifies as the "locked location-state file's §sensory or §conditions baseline"
#   in spirit when loc-state does not extend earlier than the inflection's change-point.
# Coverage justification: blocking this fire on anchor grounds would require either (a) authoring a
#   pre-@1 loc-state entry for the open-lane state, or (b) refusing the scene-A pressure fire entirely
#   and finding a different modality for the floor — both worse outcomes than sourcing from the card.
#
# Per-entry annotations:
# - sensory:1 @2: carve-out clause — location card §Hazards baseline for lane-pressure (no loc-state pre-blockage entry)

1 @2 pressure: lane-passable-morning-flow -> crowd-backed-body-compression # tag: up

2 @17 sound: drain-water-trickle-ambient -> stylus-on-board-rhythm # tag: up

3 @20 sound: stylus-on-board-rhythm -> silence # tag: drop
