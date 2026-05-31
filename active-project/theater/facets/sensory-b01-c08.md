facet: sensory
episode: b01c08
author: studio
generated: 2026-05-31
---

# rubric-carve-out — PARTIALLY RESOLVED at cycle-2 (2026-05-31)
# Carve-out was active at sensory-R1 authoring time (loc-state not yet authored).
# At cycle-2 fixer pass: loc-state:4 @9 was updated to carry `sensory: enclosed-receipt-quiet`.
# Carve-out for sensory:1 @10 is NOW RETIRED — old-state traces to locked-graph loc-state:4 @9.
# Carve-out for sensory:2 @16 remains advisory-only (old-state "afternoon" confirmed by loc-state:2/@3
#   and loc-state:3/@4; "stone-lane-light" is a constrained extrapolation; old-state-reader flagged
#   as SOFT-FLAG not HARD — does not independently block acceptance).
#
# design/shoot-v2/rubric-sensory.md § Modality-inflection / Anchored to a real perceptual baseline
#
# Per-entry annotations:
# - sensory:1 @10: carve-out RESOLVED at cycle-2 — loc-state:4 @9 now carries `sensory: enclosed-receipt-quiet`
#   (added at cycle-2 fixer pass 2026-05-31). Old-state `enclosed-receipt-quiet` traces directly to
#   loc-state:4 @9 sensory field (verbatim match). Original carve-out clause (a) retired; anchor is now
#   locked-graph fact, not series-class inference.
# - sensory:2 @16: carve-out clause (b) — old-state afternoon-stone-lane-light sourced from the
#   scene-map time-of-day field: scene-A/B = "afternoon"; scene-C = "evening (return circuit pass)".
#   The afternoon-to-evening light shift is a structural fact the scene-map asserts. Loc-state-side
#   anchor expected when loc-state for b01c08 is authored; if contradicted, revise.

1 @12 sound: enclosed-receipt-quiet -> wax-seal-crack # tag: spike
2 @19 light: afternoon-stone-lane-light -> evening-lane-dusk-fall # tag: down
