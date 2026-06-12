# Library Improvement Loop — Ledger

Tracks each improvement-loop/library pass: what was scanned, the single op performed, cards touched, next candidate.

---

## Pass 001 — 2026-06-12

### Scan summary

- **Cards scanned:** 246 active cards across `cards/` (conditions, dialects/behaviors, locations, props, personas) + `and-experiment/warehouse/` + `active-project/warehouse/`
- **Dialect-class migration:** All 12 cards in `cards/dialects/` already carry `class: behavior` — migration complete, no action needed.
- **Fuzzy-duplicate clusters checked:** Reincarnation-mechanics chain (4 cards — distinct era-variants, not duplicates; supersede chain intact). KL witch-label pair (`cond-kl-witch-label-formation` / `cond-kl-witch-label-formation-122ac`) — supersede chain has a broken backlink on the old card (missing `superseded_by:`). Westerosi-customary-authority cluster (3 era-variants — intended coexistence). Series-tone-constraints cluster (3 era-variants — intended coexistence).
- **Broken supersede backlinks found:** 2 — `cond-kl-witch-label-formation` (missing `superseded_by: cond-kl-witch-label-formation-122ac`) and `cond-khepri-residue-122ac` (missing `superseded_by: cond-override-architecture-residue-122ac`). Both are project-scoped cards; noted as next candidate.
- **Thin zones / lone-slot check:** `cards/locations/` has exactly one forest/natural-clearing card (`forest-clearing-dusk`), and it carries `quality: scant`. All other location cards are urban (King's Landing, Flea Bottom, Red Keep, riverlands settlements) or structured buildings. This is a lone-slot + scant condition: highest priority for rescue.
- **Scant cards found:** `forest-clearing-dusk.card.md` self-declares `quality: scant`. Missing sections: Fixed Props, Hazards, Ambient Interruption Hooks.

### Operation

**RESCUE** — `forest-clearing-dusk.card.md`

Added the three missing location sections (Fixed Props, Hazards, Ambient Interruption Hooks) and promoted `quality` to `full`. No existing content changed — additive only.

### Cards touched

- `cards/locations/forest-clearing-dusk.card.md` — `quality: scant` → `quality: full`; added Fixed Props, Hazards, Ambient Interruption Hooks sections

### Next candidate

**Broken supersede backlinks** — two project-scoped condition cards are missing `superseded_by:` fields:
- `cards/conditions/cond-kl-witch-label-formation.card.md` — add `superseded_by: cond-kl-witch-label-formation-122ac`
- `cards/conditions/cond-khepri-residue-122ac.card.md` — add `superseded_by: cond-override-architecture-residue-122ac`

These are two targeted one-line edits. Bundle as a single "schema-compliance — supersede backlinks" pass.
