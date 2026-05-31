facet: sensory
episode: b01c08
author: studio
generated: 2026-05-31
---

# rubric-carve-out — old-state anchor from series-established vocabulary + scene-map time-of-day record (no loc-state file authored at sensory-R1 stage)
#
# design/shoot-v2/rubric-sensory.md § Modality-inflection / Anchored to a real perceptual baseline
#
# Carve-out scope: sensory:1 @10 (old-state sourced from series-established indoor-administrative-quiet
#   vocabulary, not a loc-state entry); sensory:2 @16 (old-state sourced from scene-map time-of-day
#   transition record afternoon → evening, not a loc-state entry)
# Carve-out rule: location-state facet for b01c08 has not yet been authored at this fork's dispatch.
#   Per the b01c06 precedent (SEAM-009; rubric-carve-out preamble in sensory-b01-c06.md), when the
#   loc-state file is absent at sensory-R1 authoring time, old-state may be sourced from (a) series-
#   established sensory vocabulary for the location class (indoor-administrative-quiet for the
#   feed-station) or (b) the scene-map time-of-day transition field (afternoon → evening at @16 scene-C
#   open). Both anchors are structural assertions of environmental fact; both will be ratified or
#   corrected when the loc-state file is authored. If loc-state contradicts either old-state, this
#   sensory entry must be revised or deleted (cross-facet contract).
# Coverage justification: the modality-floor (≥2 modalities) cannot be sacrificed even on a 24-bone
#   short chapter. Two entries at 2 modalities (sound + light) is the minimum compliant configuration.
#   With no loc-state baseline on record at authoring time, the carve-out is the only path to a
#   clean old-state anchor that survives the four-axis rubric.
#
# Per-entry annotations:
# - sensory:1 @10: carve-out clause (a) — old-state feed-station-working-quiet sourced from
#   series-established indoor-administrative-quiet vocabulary (the feed-station is an enclosed receipt
#   space; the baseline is corroborated by the calibration anchor s01e01:41 context: "yard-quiet →
#   wax-crack" for an analogous seal-break in a working space). Loc-state-side anchor expected when
#   loc-state for b01c08 is authored; if contradicted, revise.
# - sensory:2 @16: carve-out clause (b) — old-state afternoon-stone-lane-light sourced from the
#   scene-map time-of-day field: scene-A/B = "afternoon"; scene-C = "evening (return circuit pass)".
#   The afternoon-to-evening light shift is a structural fact the scene-map asserts. Loc-state-side
#   anchor expected when loc-state for b01c08 is authored; if contradicted, revise.

1 @10 sound: feed-station-working-quiet -> wax-seal-crack # tag: spike
2 @16 light: afternoon-stone-lane-light -> evening-lane-dusk-fall # tag: down
