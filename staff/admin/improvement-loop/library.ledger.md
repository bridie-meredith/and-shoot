# Library Improvement Loop — Ledger

Format per entry: date, scan scope, op performed, cards touched, next candidate.

---

## Pass 1 — 2026-06-11

**Scan scope:**
- `cards/` (all five classes: personas, locations, props, conditions, dialects/behaviors)
- `and-experiment/warehouse/` — not present; directory absent
- `active-project/warehouse/` — cross-checked for warehouse copies of library cards

**Findings summary:**

| Finding class | Count | Notes |
|---|---|---|
| Scant personas (not in cast) | 8 | viserys-i-targaryen (has exemplar), aegon-ii-targaryen, aemond-targaryen (base), peasant-woman-forest, oc-girl-from-hamlet, oc-plumms-man (intentional alias variant), oc-tributary-village-newcomer, victoria-dallon |
| Scant locations | 3 | loc-red-keep-outer-ring (false-scant), forest-clearing-dusk (genuinely thin — missing 3 sections), oc-stitch-house-lane (narrow-scope, missing some sections) |
| Scant props | 3 | oc-water-skin, oc-fish-account-ledger, oc-procedural-form (all have complete body sections; scant may be conservative labeling; OK at margit's discretion per schema) |
| Fuzzy duplicates | 0 | All similar-named cards (flea-bottom cluster, reincarnation-mechanics cluster, witch-label cluster) are properly structured as project-variants or variant-of chains — not near-duplicates |
| Thin zones | 0 blocking | Props zone (15 cards) is small but covers active-project needs; dialects/behaviors (12 cards) all class:behavior already |
| Schema-failing | 0 | No missing required frontmatter fields found across any class |
| Paradigm card opportunity | 0 | No ≥3 cards sharing an unextracted archetype found; institutional-observer personas (plumms-man, census-officer) only 2 full cards |

**Op performed:** RESCUE — false-scant label correction on `loc-red-keep-outer-ring`

The card has all 7 schema-required location body sections (Geography, Layout, Sensory Vocabulary, Fixed Props, Exits, Hazards, Ambient Interruption Hooks) fully populated and richly developed. The `quality: scant` label was incorrect — the card can anchor a scene, which is the definition of `quality: full`. The Red Keep outer ring is a structurally important surveillance location for s2/s3; a scant label would cause agents to undervalue it.

**Change:** `quality: scant` → `quality: full` in `cards/locations/loc-red-keep-outer-ring.card.md`

**Cards touched:** `loc-red-keep-outer-ring`

---

**Next candidate (for Pass 2):**

`forest-clearing-dusk` — genuinely thin scant location: missing Fixed Props, Hazards, and Ambient Interruption Hooks. Extracted from brighid-creative-writing, generic Westerosi forest. Low urgency (no active-project scenes anchored here) but complete-able in one card-rescue pass. Worth rescuing when a forest-clearing scene enters the near-term chapter plan.

After that: `viserys-i-targaryen` persona rescue — has exemplar, has clear series role, missing Taste/Pet Peeves/Look/Default Stance/Action Menu/Action Costs/Triggers/Off-Screen Cadence/Vibe Seeds. Will be needed for s2 institutional-pressure scenes. Dispatch card-rescue agent when s2 planning begins.
