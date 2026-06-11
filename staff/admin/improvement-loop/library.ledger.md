# Library Improvement Loop — Ledger

Tracks each pass of the improvement-loop/library routine. One op per pass.

---

## Pass 2026-06-11

**Scanned:**
- `cards/locations/` — 43 cards. One card explicitly `quality: scant`: `forest-clearing-dusk`. Others spot-checked; `stormlands-coastal-cliffs` (full, complete). `reach-smallfolk-village` and `westerosi-smallfolk-*` (full). Flea-bottom cluster (3 cards: base/mirror/plain — coexisting variants, not duplicates; each has distinct scope/purpose).
- `cards/props/` — 9 cards. All structurally present; `oc-water-skin` is scant-acceptable by schema (props may stay scant at margit's discretion).
- `cards/conditions/` — ~70 cards. No schema fails on spot-check. Pre-2026 versioned copies are intentional provenance artifacts.
- `cards/dialects/` — 12 cards. All `class: dialect` (deprecated; should migrate to `class: behavior`). Migration is multi-card; deferred per schema note ("on touch").
- `cards/personas/` — ~100 cards. Not deeply scanned this pass.
- `and-experiment/warehouse/` + `active-project/warehouse/` — active project copies; not the canonical library source.

**Op chosen:** RESCUE `forest-clearing-dusk` (scant → full)

**Rationale:** Highest impact-to-cost. The card was `quality: scant` with three missing required location sections (Fixed Props, Hazards, Ambient Interruption Hooks). It's a generic, universe-agnostic Westerosi outdoor location with high reuse potential across any project using planetos. The existing Geography/Layout/Sensory Vocabulary sections were solid; the missing sections were straightforward to derive from established content.

**Cards touched:**
- `cards/locations/forest-clearing-dusk.card.md` — promoted `quality: scant` → `full`; added `Fixed Props`, `Hazards`, `Ambient Interruption Hooks` sections.

**Next candidate:**
- `cards/dialects/` migration: 12 cards should be migrated from `class: dialect` to `class: behavior` per schema note. Migration is multi-card (one per touch) and should be batched or done when a card is next used on-stage. Recommend handling as a follow-on pass — pick one dialect card per loop iteration when no higher-priority rescue exists.
- Thin zone: `cards/props/` has 9 cards and could benefit from a generic portable prop (e.g. a smallfolk coin-purse or a sealed letter) if a scene needs one without a project-specific card.
