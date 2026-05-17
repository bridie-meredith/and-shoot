# Margit Working Memory — cards authored, indexed, and promoted this project.

---

## Phase 1c Step 5 — Location card authoring and warehouse provisioning

**Date:** 2026-05-17
**Operation:** Author 6 approved location cards; copy all 6 to active-project warehouse; update INDEX.md.

---

### Cards processed

| slug | library path | warehouse path | authored/existed | schema validation | INDEX updated |
|---|---|---|---|---|---|
| `loc-flea-bottom-mirror` | `cards/locations/loc-flea-bottom-mirror.card.md` | `active-project/warehouse/loc-flea-bottom-mirror.card.md` | existed (pre-authored) | PASS | confirmed |
| `loc-velaryon-kl-townhouse` | `cards/locations/loc-velaryon-kl-townhouse.card.md` | `active-project/warehouse/loc-velaryon-kl-townhouse.card.md` | existed (pre-authored) | PASS | confirmed |
| `loc-dragonpit-exterior` | `cards/locations/loc-dragonpit-exterior.card.md` | `active-project/warehouse/loc-dragonpit-exterior.card.md` | authored this session | PASS | confirmed |
| `loc-dragonpit-interior` | `cards/locations/loc-dragonpit-interior.card.md` | `active-project/warehouse/loc-dragonpit-interior.card.md` | authored this session | PASS | confirmed |
| `loc-sept-of-baelor-margin` | `cards/locations/loc-sept-of-baelor-margin.card.md` | `active-project/warehouse/loc-sept-of-baelor-margin.card.md` | authored this session | PASS | confirmed |
| `loc-kl-burning-street` | `cards/locations/loc-kl-burning-street.card.md` | `active-project/warehouse/loc-kl-burning-street.card.md` | authored this session | PASS | confirmed |

### Schema validation notes

All six cards: `class: location`, `scope: library`, `world: planetos`, `origin: authored`, `quality: full`. All required body sections present: Geography, Layout, Sensory Vocabulary, Fixed Props, Exits, Hazards, Ambient Interruption Hooks. `loc-flea-bottom-mirror` carries `variant-of`, `variant-reason`, `variant-project`, and `references` per variant-card schema requirement.

### INDEX.md update — `cards/locations/INDEX.md`

Added to `by_world.planetos`:
- `loc-dragonpit-exterior`
- `loc-dragonpit-interior`
- `loc-flea-bottom-mirror`
- `loc-kl-burning-street`
- `loc-sept-of-baelor-margin`
- `loc-velaryon-kl-townhouse`

Added to `by_quality.full`:
- `loc-dragonpit-exterior`
- `loc-dragonpit-interior`
- `loc-flea-bottom-mirror`
- `loc-kl-burning-street`
- `loc-sept-of-baelor-margin`
- `loc-velaryon-kl-townhouse`

### Authoring notes

- `loc-flea-bottom-mirror`: thin variant of `loc-flea-bottom`. Inherits base geography, layout, sensory vocab, exits. Adds flicker-cost topology (Dragonpit-proximity gradient), social geography via observation (water-carrier routes, watch corridor, witch-reputation radius), and project-specific hazards. Does not duplicate base card content.
- `loc-velaryon-kl-townhouse`: Rhaenys's KL premises. Full patron-access card including exterior approach, receiving-room social geography (lower chair, empty table, managed warmth), Taylor-identified exits (forecourt gate + courtyard postern), and Dragonpit proximity note.
- `loc-dragonpit-exterior`: approach road, terraced open ground, outer wall. Flicker-misread origin site. First patron misidentification of amplification theory. Sensory vocabulary built around sound (chest-register resonance), smell (animal-musk / cold-fire compound), thermal differential. Full faction-exposure and commitment-point hazards.
- `loc-dragonpit-interior`: dual-function card. Keeper gallery / chain-anchor consultation space AND kill site. Shadow zone (west, between torches, damaged mounting) is the structural enabler of Taylor's misidentification. Flicker-saturation hazard documents the degradation of interpretive reliability that makes the misfire possible. Post-kill containment hazard documented.
- `loc-sept-of-baelor-margin`: outer courts and approach streets of the Great Sept. Neutral-ground logic documented (Faith-territory, not lord-governed). Septon observation network as institutional hazard. Taylor's discomfort with Faith presence as category-threat documented. Shrine stations as natural pause-point for the Taylor/opposite-number crossing.
- `loc-kl-burning-street`: closing-image site. Project-binding coordinates fixed: north-south lateral between eastern quarter and Fish Gate, Silverwing / Ulf White visible to northwest. Lyra's blocking at the well. Reference-baseline vs. Dance-days scene state documented. Chronicler coda ordering noted (coda arrives before closing image — not a location detail, but cross-referenced). Sensory vocabulary built around absence (what is not present in the shuttered street) and Silverwing's low-frequency shadow-before-sound.

---

## Phase 1c Step 5 — Persona card authoring and actor provisioning

**Date:** 2026-05-17
**Operation:** Author 9 approved persona cards; copy all 9 to active-project actors; create stub memory files; update INDEX.md.

Pre-mutation INDEX.md preserved at: `cards/personas/INDEX.pre-2026-05-17T00-00-00Z.md`

---

### Cards processed

| slug | library path | actor dir | authored/existed | schema validation | INDEX updated |
|---|---|---|---|---|---|
| `taylor-hebert-flea-bottom-mirror` | `cards/personas/taylor-hebert-flea-bottom-mirror.card.md` | `active-project/actors/taylor-hebert-flea-bottom-mirror/` | authored this session | PASS | confirmed |
| `rhaenys-targaryen` | `cards/personas/rhaenys-targaryen.card.md` | `active-project/actors/rhaenys-targaryen/` | authored this session | PASS | confirmed |
| `oc-vaegon-targaryen` | `cards/personas/oc-vaegon-targaryen.card.md` | `active-project/actors/oc-vaegon-targaryen/` | authored this session | PASS | confirmed |
| `oc-lyra-targaryen-ward` | `cards/personas/oc-lyra-targaryen-ward.card.md` | `active-project/actors/oc-lyra-targaryen-ward/` | authored this session | PASS | confirmed |
| `ulf-the-white` | `cards/personas/ulf-the-white.card.md` | `active-project/actors/ulf-the-white/` | authored this session | PASS | confirmed |
| `oc-maester-edwyn` | `cards/personas/oc-maester-edwyn.card.md` | `active-project/actors/oc-maester-edwyn/` | authored this session | PASS | confirmed |
| `oc-renderer-flea-bottom` | `cards/personas/oc-renderer-flea-bottom.card.md` | `active-project/actors/oc-renderer-flea-bottom/` | authored this session | PASS | confirmed |
| `oc-flea-bottom-boy` | `cards/personas/oc-flea-bottom-boy.card.md` | `active-project/actors/oc-flea-bottom-boy/` | authored this session | PASS | confirmed |
| `oc-apothecary-assistant` | `cards/personas/oc-apothecary-assistant.card.md` | `active-project/actors/oc-apothecary-assistant/` | authored this session | PASS | confirmed |

### Schema validation notes

All 9 cards: `class: persona`, `scope: library`, `world: planetos`, `origin: authored`, `quality: full`. All required persona sections present (Description, Voice, Taste, Pet Peeves, Stats, Relationships, Fiction Role Overlay). All lead/supporting cards carry Vibe Seeds. `taylor-hebert-flea-bottom-mirror` carries `variant-of`, `variant-reason`, `variant-project` per variant-card schema requirement.

**Instruction-specific compliance:**
- `oc-vaegon-targaryen`: `## Doppelganger Mirror` body section present; 5 behavioral overlaps named explicitly (both running prevention-logic; both willing to act against faction interest; both reasoning from catastrophe model; divergence is method; divergence is model-precision). On-page visibility requirement documented.
- `oc-maester-edwyn`: counterfactual deduction-path explicitly enumerated in Fiction Role Overlay / Thematic Purpose (6-step documented chain). Hard Fence: coda-only, no body presence.
- `taylor-hebert-flea-bottom-mirror`: Vibe Seeds present with post-Gold-Morning accumulated weight; flicker discipline documented in Hard Fences; dragon-proximity as Gold-Morning trigger documented.
- `rhaenys-targaryen`: amplification-theory documented as honest intellectual error (not manipulation); collision-trigger (Rhaenyra-survives floor) documented.
- `oc-lyra-targaryen-ward`: card built for cold-register rendering throughout; no Vibe Seeds (role too narrow); Hard Fences explicitly prohibit pathos-register and second-protagonist arc.
- `ulf-the-white`: walk-on function; Hard Fences block depth-rendering; Vaegon-blocking operational detail documented.

### Stub memory files created per actor

Each actor dir contains: `card.md` (library card copy), `ltm.md` (header, no entries), `stm.md` (STM: stub), `state.md` (initial STATE block with location and relevant stats), `vibes.md` (stub pending 1c step 6 derivation).

### INDEX.md update — `cards/personas/INDEX.md`

Added to `by_world.planetos`: oc-apothecary-assistant, oc-flea-bottom-boy, oc-lyra-targaryen-ward, oc-maester-edwyn, oc-renderer-flea-bottom, oc-vaegon-targaryen, rhaenys-targaryen, taylor-hebert-flea-bottom-mirror, ulf-the-white

Added to `by_quality.full`: all 9 above

Added to `by_trope`: young-depressed-hero (taylor-hebert-flea-bottom-mirror); targaryen-era (rhaenys-targaryen, ulf-the-white, oc-vaegon-targaryen, oc-lyra-targaryen-ward, oc-maester-edwyn); witness-figure (oc-maester-edwyn); false-ally (rhaenys-targaryen); doppelganger-opposite-number (oc-vaegon-targaryen); cost-bearer (oc-lyra-targaryen-ward); wrong-rider (ulf-the-white); flea-bottom-texture (oc-renderer-flea-bottom, oc-flea-bottom-boy, oc-apothecary-assistant); prevention-tragedy (taylor-hebert-flea-bottom-mirror, oc-vaegon-targaryen)

Added to `original_characters`: all 9, with full descriptive log entries
