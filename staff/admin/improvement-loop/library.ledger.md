# Library Improvement Loop — Ledger

Tracks each improvement-loop/library pass: what was scanned, the single op performed, cards touched, next candidate.

---

## Pass 001 — 2026-06-12

### Scan summary

- **Cards scanned:** 246 active cards across `cards/` (conditions, dialects/behaviors, locations, props, personas) + `and-experiment/warehouse/` + `active-project/warehouse/`
- **Dialect-class migration:** All 12 cards in `cards/dialects/` already carry `class: behavior` — migration complete, no action needed.
- **Fuzzy-duplicate clusters checked:** Reincarnation-mechanics chain (4 cards — distinct era-variants, not duplicates; supersede chain intact). KL witch-label pair (`cond-kl-witch-label-formation` / `cond-kl-witch-label-formation-122ac`) — supersede chain has a broken backlink on the old card (missing `superseded_by:`). Westerosi-customary-authority cluster (3 era-variants — intended coexistence). Series-tone-constraints cluster (3 era-variants — intended coexistence). Taylor behavior cards (proper `inherits:` chain). All persona clusters with timestamped variants (aemond-targaryen, rhaenyra-targaryen, mira-stonefield) are intentional period-variants, not fuzzy duplicates.
- **Broken supersede backlinks found:** 2 — `cond-kl-witch-label-formation` (missing `superseded_by: cond-kl-witch-label-formation-122ac`) and `cond-khepri-residue-122ac` (missing `superseded_by: cond-override-architecture-residue-122ac`). Both are project-scoped cards; noted as next candidate.
- **Thin zones / lone-slot check:** `cards/locations/` has exactly one forest/natural-clearing card (`forest-clearing-dusk`), and it carried `quality: scant`. All other location cards are urban (King's Landing, Flea Bottom, Red Keep, riverlands settlements) or structured buildings. This is a lone-slot + scant condition: highest priority for rescue.
- **Scant personas (no full variant):** `viserys-i-targaryen` (48 lines; no 122ac variant; off-stage S1 but will be needed), `aegon-ii-targaryen` (51 lines; no 122ac variant; appears at s3 climax), `victoria-dallon` (26 lines; earth-bet; no current project use). These are next-pass candidates for card-rescue dispatch.
- **Scant cards addressed this pass:** `forest-clearing-dusk.card.md` — missing Fixed Props, Hazards, Ambient Interruption Hooks.

### Operation

**RESCUE** — `forest-clearing-dusk.card.md`

Added the three missing location sections (Fixed Props, Hazards, Ambient Interruption Hooks) and promoted `quality` to `full`. No existing content changed — additive only.

### Cards touched

- `cards/locations/forest-clearing-dusk.card.md` — `quality: scant` → `quality: full`; added Fixed Props (natural site / fallen log is geography not prop), Hazards (darkness after dusk / treeline concealment / animal presence / weather exposure / sound carry), Ambient Interruption Hooks (8 hooks: wood-pigeon, bracken movement, stream-sound dropout, distant dog-bark, road torchlight, rain smell, horses on road, fire smell)

### Next candidates

**Priority 1 — Broken supersede backlinks** (two targeted one-line edits, schema-compliance):
- `cards/conditions/cond-kl-witch-label-formation.card.md` — add `superseded_by: cond-kl-witch-label-formation-122ac`
- `cards/conditions/cond-khepri-residue-122ac.card.md` — add `superseded_by: cond-override-architecture-residue-122ac`
Bundle as a single "schema-compliance — supersede backlinks" pass.

**Priority 2 — Scant persona rescue** (dispatch card-rescue subagent):
- `viserys-i-targaryen` — no full-quality variant; missing Taste, Pet Peeves, Look, Default Stance, Action Menu, Action Costs, Triggers, Off-Screen Cadence, Vibe Seeds. Will block any scene requiring his on-stage cast.
- `aegon-ii-targaryen` — same gap profile; appears at s3 climax; no 122ac variant.
