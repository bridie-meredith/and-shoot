# Library Improvement Loop — Ledger

Running log of improvement-loop/library passes. One op per pass.

---

## Pass 2026-06-11

### Scan scope
- `cards/personas/` (100+ cards), `cards/locations/` (47 cards), `cards/props/` (15 cards), `cards/conditions/` (70+ cards), `cards/dialects/` (12 behavior cards)
- `active-project/warehouse/`, `and-experiment/warehouse/` (absent)

### Findings

**Scant props (3):** `oc-fish-account-ledger`, `oc-water-skin`, `oc-procedural-form` — bodies complete; acceptable per schema at margit's discretion.

**Scant locations (3):** `forest-clearing-dusk` (missing Hazards + Ambient Interruption Hooks), `loc-red-keep-outer-ring` (body complete, quality flag possibly stale), `oc-stitch-house-lane` (missing H1 title + Ambient Interruption Hooks).

**Scant personas (8):** `aegon-ii-targaryen`, `aemond-targaryen`, `oc-girl-from-hamlet`, `oc-plumms-man`, `oc-tributary-village-newcomer`, `peasant-woman-forest`, `victoria-dallon`, `viserys-i-targaryen`. None are in the active cast (active cast personas are all `quality: full`). No blocking issue; monitor on next /and-cast.

**Behavior/dialect migration:** Already complete — all `cards/dialects/` files carry `class: behavior`. Directory rename deferred per CLAUDE.md (OOS).

**Fuzzy-duplicate clusters:** None found. Reincarnation-mechanics and series-tone-constraints condition clusters are proper versioned variants (84ac / 125ac / base), not duplicates.

**Archetype candidates:** No ≥3-card archetype cluster without a paradigm card identified.

### Op chosen

**RESCUE `oc-stitch-house-lane`** — scant → full.

Rationale: cheapest quality-bearing rescue in the library. Card had all required sections except Ambient Interruption Hooks and a missing H1 title heading. One section + one heading = full. Card is project-scoped to `taylor-westeros-good-intentions` (active project lineage).

### Cards touched

- `cards/locations/oc-stitch-house-lane.card.md`
  - Added `# Stitch House Lane — Hook District Service Lane, Flea Bottom` title heading
  - Added `## Fixed Props` section (None card-level)
  - Added `## Ambient Interruption Hooks` section (4 hooks)
  - `quality: scant` → `quality: full`

### Next candidate

`forest-clearing-dusk.card.md` (scant → full; add Hazards + Ambient Interruption Hooks — 2 sections, natural forest clearing content). Or `loc-red-keep-outer-ring.card.md` quality-flag review (body appears complete; may only need flag flip).
