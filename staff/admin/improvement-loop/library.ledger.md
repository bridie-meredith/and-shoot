# improvement-loop / library — ledger

Schema: each run appends one entry. Fields: date, scanned, op, cards_touched, next_candidate.

---

## 2026-06-12

**date:** 2026-06-12

**scanned:**
- `cards/personas/` — 8 scant persona cards found: `aegon-ii-targaryen`, `viserys-i-targaryen`, `aemond-targaryen` (base; covered by full `aemond-targaryen-122ac` variant in cast), `victoria-dallon`, `oc-girl-from-hamlet`, `peasant-woman-forest`, `oc-plumms-man` (valid variant-of `plumms-man`, not a real scant), `oc-tributary-village-newcomer`
- `cards/dialects/` (12 behavior cards) — all already migrated to `class: behavior`; no `class: dialect` stragglers
- `cards/conditions/` — condition variant clusters checked (`cond-reincarnation-mechanics-*`, `cond-series-tone-constraints-*`, `cond-westerosi-customary-authority-*`); all properly project-scoped, not problematic near-duplicates; one tombstone (`cond-reincarnation-rules`) correctly marked
- `cards/locations/`, `cards/props/` — no scant/schema failures found (location + prop scant is margit-discretion; no blocking cases)
- `active-project/warehouse/` — no new library candidates
- Archetype scan: no recurring archetype across ≥3 cards without a paradigm card identified this pass

**op:** rescue — `aegon-ii-targaryen` scant → full

**rationale:** Supporting-tier named canon character (HOTD/Fire & Blood) who appears at the s3 climax convergence. Project is at chapter 11 of 18–22; climax approaches. No 122ac full variant exists (unlike `aemond-targaryen`, which is covered by `aemond-targaryen-122ac`). Schema hard gate: persona used on-stage must be `quality: full` before cast entry. Rescue is strictly additive — no prior content touched.

**cards_touched:**
- `cards/personas/aegon-ii-targaryen.card.md` — promoted `quality: scant` → `quality: full`; added: Taste (5 items), Pet Peeves (4 items with severity), Look, Default Stance, Action Menu (5 items), Action Costs (5 costs), Triggers (6 items), Off-Screen Cadence
- `staff/margit/roster-provenance.md` — provenance log entry appended by card-rescue agent

**next_candidate:**
- `viserys-i-targaryen` (scant) — structural background figure for the story; off-stage but institutional pressure source; rescue if he appears in chapters 12+
- `aemond-targaryen` (base card, scant) — low priority since `aemond-targaryen-122ac` (full) covers active cast use; rescue base only if a non-122ac project needs it
- `oc-girl-from-hamlet` / `peasant-woman-forest` / `oc-tributary-village-newcomer` (scant minor OCs) — low priority; minor-tier, single-scene use acceptable at scant
