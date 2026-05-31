facet: sensory
episode: b01c07
author: studio
---

# rubric-carve-out — short-chapter floor-vs-ceiling exemption (V3)
#
# design/shoot-v2/rubric-sensory.md § Curve-shape rubric / Episode-level shape
#
# Carve-out scope: this file (bone_count=25 < 30; modality count=2 = floor minimum for R1)
# Carve-out rule: effective sparsity ceiling = max(6%, 2/25) = 8% (advisory, not blocking).
#   Standard 6% ceiling would permit ~1 entry on 25 bones; the floor (≥2 modalities) requires
#   at minimum 2 entries. The exemption resolves the arithmetic collision; modality-floor takes
#   precedence. Two entries at 8% density is ADVISORY-above-band, not a HARD finding.
# Coverage justification: monoculture is the load-bearing pathology; 2 entries at 2 modalities
#   preserves the disambiguation gradient (23 unflagged bones remain the contrast baseline).
#
# Phase 4.6 grounding adds (entries 3 + 4):
#   Density post-add: 4/25 = 16% — above both the standard 6% ceiling and the V3 exemption 8%
#   advisory ceiling. Entries 3 and 4 are GROUNDING-REQUIRED ledger-licensed exceptions
#   (grounding-ledger-b01-c07.md grd-001 / grd-002; PROP-0022 aliveness twin). The frequency-band
#   cap is explicitly waived for these two by the ledger license. Phase 5 auditor and Phase 5b
#   audience must apply the licensed-grounding-exception exemption, not the standard cap verdict.
#
# Per-entry annotations:
# - sensory:1 @12: exemption clause — 2nd entry needed to meet modality floor; sound+tactile pair
# - sensory:2 @17: exemption clause — floor-entry; tactile modality; airless-span grounding anchor
# - sensory:3 @16: licensed-grounding-exception: grd-001 — thermal; halvard exhale in held cold; cap-exempt
# - sensory:4 @22: licensed-grounding-exception: grd-002 — pressure; heel-settles-cobble-edge at steadying; cap-exempt; discrete event (heel-settle weight on @22 steadying action, not cumulative thermal drift). modality=pressure (schema-valid; weight/load sensation), distinct from sensory:2@17 tactile cobble-grip texture.

1 @12 sound: halvard-pastoral-account-register -> halvard-direct-address # tag: up | old-state-anchor: loc-state:3@9
2 @17 tactile: sept-corner-stone-firm -> sept-corner-cobble-grip # tag: up | old-state-anchor: loc-state:4@15
3 @16 thermal: sept-corner-held-cold -> halvard-breath-in-cold-air # tag: spike | licensed-grounding-exception: grd-001
4 @22 pressure: sept-corner-stone-firm -> heel-settles-cobble-edge # tag: spike | licensed-grounding-exception: grd-002 | old-state-anchor: loc-state:4@15
