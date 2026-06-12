# Library Improvement Loop — Ledger

Each entry records one improvement-loop LIBRARY pass: what was scanned, the op chosen, cards touched, next candidate.

---

## Pass 1 — 2026-06-12

### Scan coverage

- `cards/personas/` — 100 cards. Found 8 scant personas: `aegon-ii-targaryen`, `aemond-targaryen`, `oc-girl-from-hamlet`, `oc-plumms-man`, `oc-tributary-village-newcomer`, `peasant-woman-forest`, `victoria-dallon`, `viserys-i-targaryen`. Note: `oc-plumms-man` is an acknowledged `variant-of: plumms-man` (scant by design — thin variant wrapper). Pre-dated backup file `otto-hightower.pre-2026-05-18T000000Z.card.md` is also scant (archived state, expected).
- `cards/locations/` — 46 cards. Found 3 scant locations: `forest-clearing-dusk`, `loc-red-keep-outer-ring`, `oc-stitch-house-lane`. Schema notes scant is valid for locations at margit's discretion.
- `cards/props/` — 15 cards. Found 3 scant props: `oc-fish-account-ledger`, `oc-procedural-form`, `oc-water-skin`.
- `cards/conditions/` — 68 cards. No scant. Naming convention split (`cond-*` vs `condition-*`) — 8 cards with `condition-` prefix are all `quality: full` and schema-valid; inconsistency is cosmetic only.
- `cards/dialects/` — 12 behavior cards (directory name deferred from `dialects/` → `behaviors/` per CLAUDE.md). **One schema compliance fault:** `westeros-grrm-mannerisms.card.md` marked `quality: full` but missing the required `## Direct samples` section (behavior schema: "required load-bearing section; a behavior card with no direct samples is incomplete").
- `and-experiment/warehouse/` and `active-project/warehouse/` — scanned; no scant/schema-fail conditions found; these are mostly project-scope condition cards at full quality.
- Duplicate/archetype scan: no near-duplicate clusters identified. Several near-related conditions (`cond-reincarnation-mechanics-84ac`, `cond-reincarnation-mechanics-125ac`, `cond-reincarnation-mechanics`) are deliberate era-variants with distinct content, not duplicates. Three `monument-*` behavior cards exist but are per-character behavior monuments for Taylor, not the same archetype across multiple characters — paradigm-extract not warranted yet.

### Op chosen

**Rescue** — `cards/dialects/westeros-grrm-mannerisms.card.md`

**Rationale:** Highest impact-to-cost in the library. This card is the universal overlay for ALL Westeros behavior cards; it is referenced by ~10 per-character and per-class cards. The quality: full label was inaccurate — the card was missing the behavior schema's required load-bearing section. Fixing this single card strengthens every downstream Westeros behavior composition.

**Operation:** Added `## Direct samples` section (10 verbatim/near-verbatim canon passages from ASOIAF/A Game of Thrones/A Storm of Swords) inserted immediately after the intro paragraphs and before `## Time-keeping vocabulary`. Samples cover all five required mannerism classes: time-keeping vocabulary (moons, fortnight, sennight, morrow), X-and-Y number form, short declarative + tag-line sentence pattern, archaic a-prefix + compound words, register-locked idioms (words are wind, death-register formula, much-and-more), high-register inversion + list-of-three, and phonetic class-marker + m'lord smallfolk register. All existing content preserved. `quality: full` label now accurate.

### Cards touched

- `cards/dialects/westeros-grrm-mannerisms.card.md` — rescued (additive; `## Direct samples` section added)

### Side artifacts

- `staff/margit/roster-provenance.md` — card-mutation log created by card-rescue agent; relocated from repo root to margit home.

### Next candidate

**`aegon-ii-targaryen.card.md`** (persona, `quality: scant`, `tier: supporting`). Card has good Description, Voice, Hard Fences, Stats, Fiction Role overlay but is missing: Taste, Pet Peeves, Look, Default Stance, Action Menu, Action Costs, Triggers, Off-Screen Cadence. The active project (b01, 20 chapters, Taylor Hebert in KL 122 AC) is complete, but Aegon II is a library-scope canon character who will appear in future HotD-era projects. Dispatch card-rescue next pass.
