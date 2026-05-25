facet: sensory
episode: b01-c01
author: studio
date: 2026-05-25
---

# rubric-carve-out — unanchored-old-state exemption for empty locations: header
#
# design/shoot-v2/rubric-sensory.md § 1. Modality-inflection / Unanchored old-state (HARD)
#
# Carve-out scope: all entries in this file (sensory:1, sensory:2)
# Carve-out rule: bones file header `locations:` is empty; no location-state file was authored
#   for b01c01. The rubric requires old-state to resolve to either the most recent loc-state
#   baseline OR the most recent prior sensory entry on the same modality. With no loc-state,
#   the old-state for the chapter's first entry on each modality is sourced from scene-internal
#   sensory context established by the opening bones — the earliest viable baseline for
#   a chapter with no prior sensory history and no loc-state. Per-entry old-states are
#   scene-internally defensible (see annotations below).
# Coverage justification: instruction explicitly states "treat scene-internal sensory anchors
#   as scene-tier sensory" when the locations: header is empty. The old-state for sensory:1
#   resolves to the lane-ambient-pre-smoke state established by bone 1 (drain water; no smoke
#   yet). The old-state for sensory:2 resolves to the crowd-ambient-murmur established by
#   bones 7-11 (compressed crowd in a Flea Bottom lane; no raised voice yet).
#
# Per-entry annotations:
# - sensory:1 @2: old-state lane-ambient sourced from scene-internal opening (bone 1 drain
#   water; smoke first appears at bone 2); no prior sensory entry on smell modality; no
#   loc-state; carve-out applies.
# - sensory:2 @16: old-state crowd-ambient-murmur sourced from scene-internal bones 7-11
#   (compressed Flea Bottom crowd with no raised voice yet); no prior sensory entry on sound
#   modality; no loc-state; carve-out applies.

1 @2 smell: lane-ambient -> tallow-smoke-onset # tag: up
2 @16 sound: crowd-ambient-murmur -> taylor-raised-voice # tag: up
