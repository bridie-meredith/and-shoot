facet: sensory
episode: b01c09
author: studio
rubric: design/shoot-v2/rubric-sensory.md (V3 locked 2026-05-21)
source: theater/proto-lines/b01-c09.md (23 bones)
scene-map: theater/facets/scene-map-b01-c09.md
loc-state: theater/facets/location-state-b01-c09.md (not yet authored — seam flagged below)
generated: 2026-06-01
---

1 @8 thermal: stone-lane-late-morning-warmth -> hill-lane-evening-cool # tag: down

2 @23 tactile: wax-soft-warm -> wax-set-firm # tag: down

---

## File-shape record

bones: 23
fires: 2
density: 2/23 = 8.7%
modalities: thermal (@8), tactile (@23) — 2 distinct modalities (floor met exactly)
short-chapter-exemption: ACTIVE (23 < 30; modality-count = floor = 2; effective ceiling relaxed to max(6%, 2/23) = 8.7%; ADVISORY not blocking)

per-scene cap:
  scene-A @1-@7: 0 fires (cap ≤3 — ok)
  scene-B @8-@16: 1 fire (@8) (cap ≤3 — ok)
  scene-C @17-@23: 1 fire (@23) (cap ≤3 — ok)

## Per-entry rubric notes

### sensory:1 @8 — thermal: stone-lane-late-morning-warmth -> hill-lane-evening-cool

Directly addresses BONES-AIRLESS-RISK (bones-review advisory: scene-B opening @8-@11 reads apparatus-first; this fire grounds the @8 entry-beat as a physical event before @11 apparatus-fires).

- Modality-inflection: thermal down; Taylor transitions from the late-morning hook-ward circuit (scene-A; warm stone-lane ambient) into the Dragonpit-margin lane at evening; the hill-lane evening air is the inflection-point.
- Disambiguation: "enters" (@8: "taylor-hebert-kl-122ac enters the dragonpit-margin lane") is a bare verb; the word does not self-carry thermal register. Flag needed.
- Magnitude: a late-morning-to-evening temperature shift, crossing into a hill-side lane (Dragonpit sits on Rhaenys's Hill; the lanes toward it lose retained day-heat faster than the lower wards), is audience-experiential-scale. Physically registerable.
- Audience-side: universally legible once flagged; no fauna-feed extension.
- Inflection-not-sustained: @8 is the entry-point change; the hill-lane evening temperature then holds through scene-B.
- Old-state anchor: scene-A time-of-day is "late morning" (scene-map annotation); the stone-lane warmth from the morning hook-ward circuit is the prior thermal register. Old-state sources from scene-map time-of-day + location shift (Rhaenys's Hill proximity = faster evening-cool). No prior sensory fire on thermal in this chapter; no loc-state contradiction. Follows b01c08 sensory:2 precedent (old-state sourced from scene-map time-of-day transition; see studio state.md SEAM-009/010 carve-out preamble).

SEAM-011: old-state "stone-lane-late-morning-warmth" has no prior loc-state entry in b01c09 yet (loc-state facet not yet authored). R2 reviewer: confirm loc-state baseline does not contradict; if loc-state names a different thermal baseline for scene-A, revise or delete this entry.

### sensory:2 @23 — tactile: wax-soft-warm -> wax-set-firm

Directly addresses priority brief: "the seal-drying @23 (terminal image) wants a tactile/olfactory anchor."

- Modality-inflection: tactile down; the wax applied at @19 (sealing the packet) is soft and warm; by @23 it has set firm.
- Disambiguation: "dries" (@23: "the seal dries") is a bare process verb; it does not self-carry the tactile texture register (the yielding-warm → set-firm quality of cooling wax). Flag needed.
- Magnitude: wax transitioning from workably soft to finger-resist-firm is a physically distinct tactile event; audience-experiential-scale (wax seals are recognizable material objects with a known physical behavior). "Dries" alone gives only the result; the flag gives the texture of the transition.
- Audience-side: universally legible once flagged; the physical experience of cooling wax is a common enough material reference to land.
- Inflection-not-sustained: @23 is the terminal change-point; the set-firm state is the chapter-close condition.
- Old-state anchor: the sealing act occurs at @19 ("taylor-hebert-kl-122ac seals the packet"); the wax is necessarily soft-warm at application. Old-state "wax-soft-warm" is entailed by the @19 sealing-act (no prior tactile fire in this chapter to conflict with). Cross-facet: studio state.md b01c08 sensory:1 establishes wax-sealing as a concrete physical event in the feed-station context (sound:spike at @10); c09's tactile entry is a downstream cousin in a different modality at the same prop-class.

No loc-state contradiction expected; the tactile inflection is at the prop-level (wax hardening) not the room-level. Flagging nonetheless for R2 completeness.

## Considered and refused

### @3 "the stitch-shop door opens the lane-mouth" — smell: lane-outdoor-air -> tallow-and-cloth-interior
Genuine Q1+Q2 pass (bare verb; smell-spike magnitude is audience-perceptible; thematically resonant with c01 Wren-plant). Refused at cull stage: adding @3 raises the modality count to 3, which activates the standard 6% ceiling (not the short-chapter exemption); 3 fires on 23 bones = 13%, well above 6%. The priority brief targets scene-B and terminal @23 — not scene-A. @3 is the cull sacrifice to hold within exemption-ceiling arithmetic and honor the brief's stated priorities.

### @19 "taylor-hebert-kl-122ac seals the packet" — smell: station-closed-air -> molten-wax-scorch
Genuine Q1+Q2 pass (bare verb; hot wax application smell is a discrete spike). Refused at cull stage: would add a second smell fire (after @3 if @3 were kept) or would be a same-scene companion to @23 in scene-C. The tactile @23 is the stronger terminal anchor per the priority brief; smell at @19 + tactile at @23 in the same scene risks scene-C over-firing (2 entries) with both on the sealing prop-cluster — less separation than @8+@23 across two scenes.
