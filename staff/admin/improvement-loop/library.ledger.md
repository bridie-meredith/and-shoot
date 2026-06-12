# Library Improvement Loop — Ledger

Append-only. Each entry records one operation: what was scanned, what was done, cards touched, next candidate.

---

## 2026-06-12 — Pass 1

### Scan summary

**Cards scanned:** cards/ (256 .card.md files across 6 subdirectories) + active-project/warehouse/ (14 condition/location files) + and-experiment/warehouse/ (14 condition/location files).

**Class counts:** personas 103 | conditions 79 | locations 47 | props 15 | behaviors/dialects 12 | persona-exemplars 23.

**Scant cards found:**
- Props (3): oc-fish-account-ledger, oc-procedural-form, oc-water-skin — single-scene props used in b01c13; scant remains valid for props per schema.
- Personas (8): aegon-ii-targaryen, aemond-targaryen, oc-girl-from-hamlet, oc-plumms-man, oc-tributary-village-newcomer, peasant-woman-forest, victoria-dallon, viserys-i-targaryen — none in active cast; no blocking urgency.

**Schema violations:** None. Dialect → behavior class migration confirmed complete. Variant/supersede chains properly structured.

**Fuzzy duplicates:** None. reincarnation-mechanics, customary-authority, kl-witch-label-formation families are properly structured via variant-of/supersedes chains.

**Thin zones:**
- Behavior class: NO root behavior card for `taylor-hebert-kl-122ac` (the active project's LEAD character, tier: lead). Only two monument supplement cards exist under her slug. The existing `taylor-hebert-westeros` behavior card is scoped to a different project/era (120 AC Riverlands, age 11). This is the highest-impact thin zone in the library.
- No behavior cards for ANY other active cast member (otto-hightower, alicent-hightower-122ac, rhaenyra-targaryen-122ac, septon-halvard-flea-bottom, criston-cole-122ac, etc.).

**Archetypes:** No ≥3-card archetype clusters without a paradigm card identified that warranted extraction this pass.

### Operation performed

**HARVEST** — thin slot fill.

Authored `cards/dialects/taylor-hebert-kl-122ac.card.md`: root per-character behavior card for the active project's lead character in her current configuration (adult, post-Gold-Morning, King's Landing 122 AC, Flea Bottom, insect-network, Earth-Bet noun fence).

Card sourced from:
- `cards/personas/taylor-hebert-kl-122ac.card.md` (persona card voice section)
- `cards/dialects/taylor-hebert.card.md` (base behavior card, for inheritance anchor)
- `active-project/theater/dialogue/taylor-hebert-kl-122ac.md` (live dialogue samples)
- `active-project/draft/b01-c01.md`, `b01-c03.md`, `b01-c07.md` (inner monologue and spoken-dialogue samples)

Card covers: 7 direct samples (inner monologue + spoken dialogue) / cadence KL-overlay / vocabulary additions + forbidden list / syntax patterns unique to KL config / voice tells / non-verbal tics (5) / memory monuments (4: Gold Morning, operating rule, named dead, multi-shard absence).

Updated `cards/dialects/INDEX.md`: added entry in by_world/planetos, by_character/taylor-hebert-kl-122ac, and composition-stack note.

### Cards touched

- `cards/dialects/taylor-hebert-kl-122ac.card.md` — created (new)
- `cards/dialects/INDEX.md` — updated (new entry, composition stack note)

### Next candidate

**HIGH:** Behavior card for `septon-halvard-flea-bottom` (active cast, supporting, b01c13 recently completed; persona card is rich with dialogue samples; shares slot with `westeros-septon` as inherits parent; per-character card needed for dialogue-writer fork specificity).

**MEDIUM:** Behavior card for `otto-hightower` (active cast, political antagonist, major dialogue presence; has full persona card; would compose via westeros-noble-courtly + westeros-grrm-mannerisms).

**MEDIUM:** Rescue `oc-girl-from-hamlet`, `peasant-woman-forest`, or `oc-plumms-man` scant personas to full if any of the three is cast for a future chapter (currently off-stage; rescue on-demand at cast entry per schema persona quality gate).

**LOW:** Scant props (oc-fish-account-ledger, oc-procedural-form, oc-water-skin) — already used in completed scenes; single-scene purpose; schema permits scant for props; defer unless reuse is planned.
