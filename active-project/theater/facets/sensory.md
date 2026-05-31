facet: sensory
episode: b01c07
author: studio
---

# rubric-carve-out — short-chapter floor-vs-ceiling exemption (V3)
#
# design/shoot-v2/rubric-sensory.md § Curve-shape rubric / Episode-level shape
#
# Carve-out scope: this file (bone_count=25 < 30; modality count=2 = floor minimum)
# Carve-out rule: effective sparsity ceiling = max(6%, 2/25) = 8% (advisory, not blocking).
#   Standard 6% ceiling would permit ~1 entry on 25 bones; the floor (≥2 modalities) requires
#   at minimum 2 entries. The exemption resolves the arithmetic collision; modality-floor takes
#   precedence. Two entries at 8% density is ADVISORY-above-band, not a HARD finding.
# Coverage justification: monoculture is the load-bearing pathology; 2 entries at 2 modalities
#   preserves the disambiguation gradient (23 unflagged bones remain the contrast baseline).
#
# Per-entry annotations:
# - sensory:1 @12: exemption clause — 2nd entry needed to meet modality floor; sound+tactile pair
# - sensory:2 @17: exemption clause — floor-entry; tactile modality; airless-span grounding anchor

1 @12 sound: halvard-pastoral-account -> halvard-direct-address # tag: up
2 @17 tactile: passage-lane-packed-earth -> sept-corner-cobble-grip # tag: up
