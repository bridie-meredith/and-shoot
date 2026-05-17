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
