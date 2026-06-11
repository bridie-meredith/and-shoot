# Library Improvement Loop — Ledger

Each entry records one improvement-loop pass: scope scanned, op performed, cards touched, next candidate.

---

## Pass 2026-06-11

**Branch:** `claude/bold-thompson-6yrk3o`

### Scan scope

- `cards/` (all classes: conditions, dialects/behaviors, locations, persona-exemplars, personas, props)
- `active-project/warehouse/`

### Findings

| Finding | Candidate | Severity |
|---------|-----------|----------|
| Scant location — all 7 required sections present, quality tag wrong | `loc-red-keep-outer-ring` | HIGH — card actively used in b01c18-c19; MARGIT REFERRAL logged at SEAM-C19-LOC-002 |
| Scant location — missing Fixed Props + Ambient Interruption Hooks sections | `oc-stitch-house-lane` | MEDIUM — in active-project warehouse |
| Scant location — missing Fixed Props, Hazards, Ambient Interruption Hooks | `forest-clearing-dusk` | LOW — not in active warehouse |
| Slug mismatch | Library slug `loc-red-keep-outer-ring` vs active-project slug `the-red-keep-outer-ring` (SEAM-C19-LOC-002: "no warehouse card confirmed") | HIGH — resolution: either rename library card or add alias mechanism (aliases field is persona-class only per schema; rename is the clean fix) |
| dialect cards already migrated | all 12 cards in `cards/dialects/` already use `class: behavior` | CLEAN |
| `condition-*` vs `cond-*` naming inconsistency | `condition-dragon-bonding-incomplete`, `condition-dragon-presence`, `condition-language-barrier`, `condition-riverlands-contested`, `condition-shard-in-dragon-body`, `condition-swarm-in-foreign-ecology`, `condition-targaryen-claim-disputed`, `condition-war-of-five-kings-riverlands` — consistent `scope: library` / `quality: full` content | LOW — cosmetic; content is fine |

### Operation performed

**RESCUE — quality tag promotion**

Card: `cards/locations/loc-red-keep-outer-ring.card.md`
Change: `quality: scant` → `quality: full`
Rationale: All 7 required location-card sections are present (Geography, Layout, Sensory Vocabulary, Fixed Props, Exits, Hazards, Ambient Interruption Hooks) with substantive content in each. Card is actively referenced in b01c18-c19 scenes (`the-red-keep-outer-ring` slug; SEAM-C19-LOC-002 Margit referral in `active-project/staff/studio/ltm.md`). The `quality: scant` tag was incorrect — the card had been fully authored before the tag was updated.

### Cards touched

- `cards/locations/loc-red-keep-outer-ring.card.md` — quality: scant → full

### Next candidate

**Slug reconciliation — `loc-red-keep-outer-ring` vs `the-red-keep-outer-ring`.**
Studio LTM (`SEAM-C19-LOC-002`) flags: "no warehouse card confirmed" for `the-red-keep-outer-ring`. The library card name is `loc-red-keep-outer-ring` (different slug). Operation: rename the library card from `loc-red-keep-outer-ring` to `the-red-keep-outer-ring` (update `name:` frontmatter + filename + INDEX.md entry + the `references:` field in `active-project/warehouse/oc-rushwick.md`). Scope: 4 file edits. This resolves the warehouse-card-confirmed gap.

Runner-up: rescue `oc-stitch-house-lane` (in active-project warehouse, scant) — add Fixed Props section ("None catalogued") and Ambient Interruption Hooks section.
