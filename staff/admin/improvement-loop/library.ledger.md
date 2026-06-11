# Library Improvement-Loop Ledger

Owned by margit. One op per pass. Append-only.

---

## Pass 1 — 2026-06-11

### Scan summary

- **cards/personas/**: ~100 cards. Scant personas: `aegon-ii-targaryen`, `aemond-targaryen`, `oc-girl-from-hamlet`, `oc-plumms-man`, `oc-tributary-village-newcomer`, `peasant-woman-forest`, `victoria-dallon`, `viserys-i-targaryen`. All are either minor/supporting OC placeholders or legacy pre-stamp variants — none currently casting-blocked (not in active cast as on-stage requirements). No schema violations.
- **cards/dialects/**: 12 cards. All already migrated to `class: behavior`. No `class: dialect` stragglers. All have `Direct samples` section (load-bearing). Clean.
- **cards/locations/**: 47 cards. Scant: `forest-clearing-dusk`, `loc-red-keep-outer-ring`, `oc-stitch-house-lane`. `loc-red-keep-outer-ring` has all 7 sections present (thin but complete; scant intentional — surveillance-only reference). `oc-stitch-house-lane` is a project-variant oc card, scant-flagged intentionally. `forest-clearing-dusk` is `scope: library`, generic-Westeros, high reuse — and missing Hazards + Ambient Interruption Hooks.
- **cards/conditions/**: ~70 cards. Tombstoned cards present with proper `superseded_by` chains. No schema violations found. Era-variant families (`-84ac`, `-122ac`, `-125ac`, `-jaehaerys`) are intentional variant-of chains, not fuzzy duplicates. `cond-reincarnation-rules` properly tombstoned → `cond-reincarnation-mechanics`.
- **cards/props/**: 15 cards. All short but prop class requires minimal sections. No scant flags in need of rescue.
- **and-experiment/warehouse/ + active-project/warehouse/**: Working files, not library taxonomy scope. Skipped for this pass.
- **Fuzzy-duplicate scan**: No actionable clusters. The `mira-stonefield` / `mira-stonefield-dragon-gate` / `mira-stonefield-jaehaerys` cluster are legitimate era/project variants with `variant-of:` chains. The condition family clusters are intentional era-splits.
- **Thin-zone scan**: No single-card class+world slots requiring paradigm extraction. The `westeros-grrm-mannerisms` shared-behavior card already serves as the paradigm for the GRRM-mannerism archetype.

### Op selected

**RESCUE** — `forest-clearing-dusk.card.md`

Rationale: highest impact-to-cost in the library. Scope: library, world: planetos. Broadly reusable across any Westerosi forest/travel scene. Two load-bearing sections absent (Hazards, Ambient Interruption Hooks) plus Fixed Props stub. Existing content (Geography, Layout, Sensory Vocabulary, Exits) is strong and well-authored. Rescue adds the missing sections and promotes `quality: scant` → `quality: full`.

### Cards touched

- `cards/locations/forest-clearing-dusk.card.md` — rescued scant → full; added Fixed Props (none), Hazards (4 entries: dark arrival speed, treeline concealment asymmetry, rotten log instability, dusk wildlife), Ambient Interruption Hooks (5 entries: bird silence, stream-sound change, distant fire, road rider, circling animal).

### Next candidate

**`oc-stitch-house-lane.card.md`** — scant location, missing Hazards and Ambient Interruption Hooks. Smaller impact than `forest-clearing-dusk` (project-variant, narrower scope) but next in the rescue queue if the card sees active use in a flea-bottom chapter.

**Scant persona queue** (for future passes, in order of potential on-stage exposure): `viserys-i-targaryen`, `aegon-ii-targaryen`, `peasant-woman-forest`. All three are horizon/encounter characters who may be cast in upcoming books.
