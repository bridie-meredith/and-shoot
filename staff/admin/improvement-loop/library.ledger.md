# Library Improvement Loop Ledger

Records one operation per run. Append only.

---

## Run 2026-06-12

**Scan scope:** `cards/` (all classes: personas, locations, props, conditions, dialects/behaviors, persona-exemplars) + `active-project/warehouse/` + `and-experiment/warehouse/`

**Findings:**

| Finding | Detail |
|---------|--------|
| Scant cards | `oc-stitch-house-lane` (32 lines, missing Ambient Interruption Hooks); `forest-clearing-dusk` (36 lines, missing Fixed Props + Hazards + Ambient Interruption Hooks) |
| Dialect migration | All 12 `cards/dialects/*.card.md` already carry `class: behavior` — clean |
| Reincarnation cluster | `cond-reincarnation-rules` → `cond-reincarnation-mechanics` → `cond-reincarnation-mechanics-125ac` is a clean supersede chain, not duplicates |
| Thin zones | Stormlands: 1 location card (`stormlands-coastal-cliffs`); Reach: 1 location card (`reach-smallfolk-village`) |
| Fuzzy duplicates | `loc-flea-bottom` / `loc-flea-bottom-base` / `loc-flea-bottom-mirror` are correctly structured as base + specialization + variant; not duplicates |

**Operation: RESCUE**

**Card:** `cards/locations/oc-stitch-house-lane.card.md`

**Why (impact-to-cost):** Needed exactly one section (Ambient Interruption Hooks) to reach `quality: full`. Active project geography (Hook District / Flea Bottom — loaded by studio during scene authoring). Scant → full in one targeted add. Higher ratio than `forest-clearing-dusk` (which needs three sections) or any thin-zone harvest (which would require a full card from scratch).

**Changes:**
- Added `## Ambient Interruption Hooks` section (8 hooks grounded in the lane's specific physical properties)
- `quality: scant` → `quality: full`

**Next candidate:** `forest-clearing-dusk` rescue (needs Fixed Props `None` stub + Hazards + Ambient Interruption Hooks — three sections, generic Westerosi library location).
