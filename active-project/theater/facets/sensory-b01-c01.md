facet: sensory
episode: b01-c01
author: studio
date: 2026-05-25
revised: 2026-05-25 (cycle-1 remediation — sensory:2 replaced; see fixer log and-facets-cycle1-fixes-sensory.md)
---

# rubric-carve-out — unanchored-old-state exemption for empty locations: header
#
# design/shoot-v2/rubric-sensory.md § 1. Modality-inflection / Unanchored old-state (HARD)
#
# Carve-out scope: all entries in this file (sensory:1, sensory:2)
# Carve-out rule: no location-state file entries exist for b01c01 (oc-stitch-house-lane
#   declared in bones header but no authored card; loc-state zero-entry discipline applies).
#   The rubric requires old-state to resolve to either the most recent loc-state baseline
#   OR the most recent prior sensory entry on the same modality. With no loc-state,
#   the old-state for the chapter's first entry on each modality is sourced from scene-internal
#   sensory context established by the opening bones — the earliest viable baseline for
#   a chapter with no prior sensory history and no loc-state. Per-entry old-states are
#   scene-internally defensible (see annotations below).
# Coverage justification: instruction explicitly states "treat scene-internal sensory anchors
#   as scene-tier sensory" when the locations: header is empty. The old-state for sensory:1
#   resolves to the lane-ambient-pre-smoke state established by bone 1 (drain water; no smoke
#   yet). The old-state for sensory:2 resolves to the lane-ambient-tactile state established
#   by bones 1-8 (drain water, tallow smoke onset, Taylor holding, insects swelling,
#   angle-wall narrowing — lane occupied but not yet compressed; no prior tactile inflection).
#
# Per-entry annotations:
# - sensory:1 @2: old-state lane-ambient sourced from scene-internal opening (bone 1 drain
#   water; smoke first appears at bone 2); no prior sensory entry on smell modality; no
#   loc-state; carve-out applies.
# - sensory:2 @9: old-state lane-ambient-tactile sourced from scene-internal bones 1-8
#   (lane occupied but not crowd-compressed; no prior sensory entry on tactile modality;
#   no loc-state; carve-out applies). Anti-pattern #14 pre-validation passed: modality
#   (tactile) identifiable; inflection class (up — discrete onset of crowd-compression);
#   bare proto-line ("the crowd compresses" — bare physical-process verb, does not
#   self-carry tactile-register); Q1 clears (audience needs flag to register the
#   flesh-against-flesh compression as tactile inflection vs. abstract movement);
#   Q2 clears (crowd-compression in a narrow Flea Bottom lane is register-shifting at
#   audience-experiential scale — not micro-grain); audience-side perceptible (universally
#   legible once flagged; no fauna-feed extension); inflection-not-sustained (this is the
#   onset bone; the compression state established here is the new baseline, not sustained
#   already). No loc-state edit required: existing carve-out scope covers this entry.

1 @2 smell: lane-ambient -> tallow-smoke-onset # tag: up
2 @9 tactile: lane-ambient -> crowd-compression # tag: up
