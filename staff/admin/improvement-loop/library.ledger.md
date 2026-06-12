# Library Improvement Loop — Ledger

Maintained by margit. One op per pass. Append-only.

---

## Pass 2026-06-12

### Scan summary

Scanned: `cards/locations/` (47 cards), `cards/conditions/` (68 cards), `cards/props/` (15 cards), `cards/personas/` (99 cards), `cards/dialects/` (12 cards). No `and-experiment/warehouse/` or `active-project/warehouse/` path present at scan time.

**Scant cards found:**
- `loc-red-keep-outer-ring` (location) — all 7 required schema sections present; quality flag was stale
- `oc-stitch-house-lane` (location) — missing Fixed Props + Ambient Interruption Hooks (genuine content gap)
- `forest-clearing-dusk` (location) — missing Fixed Props, Hazards, Ambient Interruption Hooks
- `oc-fish-account-ledger`, `oc-procedural-form`, `oc-water-skin` (props)
- `aegon-ii-targaryen`, `aemond-targaryen`, `viserys-i-targaryen`, `victoria-dallon`, `oc-girl-from-hamlet`, `oc-plumms-man`, `oc-tributary-village-newcomer`, `peasant-woman-forest` (personas)

**Fuzzy duplicates:** Reincarnation mechanics cluster (`cond-reincarnation-rules` tombstoned → `cond-reincarnation-mechanics` → `cond-reincarnation-mechanics-125ac` with `cond-reincarnation-mechanics-84ac` as variant-of). Supersede chain correctly formed. No merge needed.

**Class: dialect vs class: behavior:** All 12 cards in `cards/dialects/` already carry `class: behavior`. Directory rename deferred per CLAUDE.md.

**Thin zones:** Prop class is thin (15 cards); earth-bet / Worm world has only behavior cards, no location or prop cards. Low urgency — these are project-specific props.

### Op performed

**Type:** rescue (metadata correction)  
**Card:** `loc-red-keep-outer-ring`  
**Change:** `quality: scant` → `quality: full`  
**Rationale:** The card has all 7 schema-required body sections (Geography, Layout, Sensory Vocabulary, Fixed Props, Exits, Hazards, Ambient Interruption Hooks) with substantive content. The scant flag was a stale label from initial authoring, never updated after the card reached full content. No content added; metadata corrected to match actual state.

### Next candidate

`oc-stitch-house-lane` (location, scant) — needs `## Fixed Props` (none) + `## Ambient Interruption Hooks` (author from lane geometry: narrow service lane, stitch-house tallow lamp on east wall, drain channel at south angle, lane-mouth to Hook District). Dispatch card-rescue on next pass.
