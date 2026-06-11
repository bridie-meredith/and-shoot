# Library Improvement-Loop Ledger

Tracks each improvement-loop/library pass: what was scanned, the single op performed, cards touched, and the next candidate.

---

## Pass 1 — 2026-06-11

### Scan summary

- **cards/ (non-archived, non-.pre-2026):** 274 files across personas/, locations/, props/, conditions/, dialects/.
- **and-experiment/warehouse/:** 57 files; no cards marked `quality: scant`.
- **Dialect class:** all 12 cards already carry `class: behavior` — no migration needed.
- **Scant cards found (14):**
  - personas: `viserys-i-targaryen`, `aemond-targaryen`, `aegon-ii-targaryen`, `victoria-dallon`, `oc-girl-from-hamlet`, `oc-plumms-man`, `oc-tributary-village-newcomer`, `peasant-woman-forest`
  - locations: `forest-clearing-dusk` (missing Fixed Props / Hazards / Ambient Interruption Hooks), `loc-red-keep-outer-ring` (ALL 7 required sections present — flag is stale), `oc-stitch-house-lane`
  - props: `oc-fish-account-ledger`, `oc-procedural-form`, `oc-water-skin`
- **Fuzzy-duplicate flag:** `plumms-man` / `oc-plumms-man` — officially a variant-of relationship, not a duplicate; low priority.
- **Thin zone:** props (15 cards) — but most are project-specific OC props; not a genuine gap.
- **Active-cast check:** `aemond-targaryen-122ac` (full quality) is in active cast; the base `aemond-targaryen` scant card is a composition source only.

### Op performed

**RESCUE — `cards/personas/viserys-i-targaryen.card.md`**

Canonical library card for the king of Westeros was scant (missing Taste, Pet Peeves, Vibe Seeds; missing `tier:` frontmatter). The `and-experiment/warehouse/viserys-i-targaryen.card.md` (scope: project, quality: full) provided a well-developed Saerys-configuration variant; content was adapted to the canonical/main-project configuration (structural political force for S1, not on-stage as "Dad").

Changes made inline by margit (no card-rescue dispatch — source material was already in-library):
- `quality: scant` → `quality: full`
- Added `tier: supporting`
- Expanded `## Voice` to full-register description with forbidden-registers note
- Added `## Taste` (5 items: peace/good-reign, enabling-love pattern, model ships, feasts/court-assembled, council-without-hard-choices)
- Added `## Pet Peeves` (3 items: succession-as-open-question/strong, children-visibly-at-odds/soft, reports-requiring-choice/soft)
- Added `## Vibe Seeds` (5 history bullets + 4 private-association keys)

### Cards touched

- `cards/personas/viserys-i-targaryen.card.md` — rescued to quality: full

### Next candidates (ranked by impact-to-cost)

1. **`cards/locations/loc-red-keep-outer-ring.card.md`** — trivial flag-only fix: all 7 required location sections are already present; `quality: scant` is stale. One-line edit.
2. **`cards/personas/aemond-targaryen.card.md`** — scant base card missing Taste + Pet Peeves; the `aemond-targaryen-122ac` full variant exists, providing adaptation source.
3. **`cards/personas/aegon-ii-targaryen.card.md`** — same situation as Aemond; S3-relevant antagonist; currently no full variant to draw from.
4. **`cards/locations/forest-clearing-dusk.card.md`** — missing 3 sections (Fixed Props / Hazards / Ambient Interruption Hooks); generic library location applicable across planetos projects.
5. **`cards/personas/victoria-dallon.card.md`** — earth-bet scope; missing Voice detail, Taste, Pet Peeves; lower priority given project focus.
