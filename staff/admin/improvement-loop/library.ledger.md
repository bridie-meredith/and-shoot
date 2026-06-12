# Improvement-Loop Ledger — LIBRARY

Records one operation per pass. Scan summary, op chosen, cards touched, next candidate.

---

## Pass 001 — 2026-06-12

**Branch:** claude/pensive-ride-5c1p30

### Scan summary

Walked `cards/` (personas, locations, props, conditions, dialects, persona-exemplars) and `active-project/warehouse/`.

- **Scant cards:** `forest-clearing-dusk` (location, library-scope) — has Geography, Layout, Sensory Vocabulary, Exits; missing Hazards and Ambient Interruption Hooks.
- **Tombstoned supersede chains:** `cond-reincarnation-rules` (correctly tombstoned; `superseded_by` set); `cond-kl-witch-label-formation` project-scoped card — the library 122ac card `supersedes` it but the project card lacks `superseded_by`. Noted; low-priority because the project card is scope=project for mirror-tragedy and the 122ac card is a parallel mechanism for a different trigger, not a true version successor.
- **Fuzzy duplicates:** `loc-flea-bottom` / `loc-flea-bottom-base` / `loc-flea-bottom-mirror` — legitimate separate cards (district-level, sub-location, project-variant). `cond-reincarnation-mechanics` / `cond-reincarnation-mechanics-84ac` / `cond-reincarnation-mechanics-125ac` — era-specific variants, chain visible in frontmatter.
- **Dialect/behavior class drift:** All `cards/dialects/` cards already carry `class: behavior`; directory rename deferred per CLAUDE.md.
- **Thin zones:** Props (9 cards) is sparse but all present cards are well-formed; no lone-slot requiring harvest.
- **Archetype recurring ≥3 with no paradigm:** Westeros shared-behavior cards (smallfolk, noble-courtly, septon, maester, northern) — legitimate distinct registers, not the same archetype.

**Decision:** `forest-clearing-dusk` rescue is the highest-impact / lowest-cost op: library-scope, well-framed content already in place, two sections short of full.

### Operation

**Type:** rescue — scant → full  
**Card:** `cards/locations/forest-clearing-dusk.card.md`  
**Changes:**
- `quality: scant` → `quality: full`
- Added `## Hazards` section (4 bullets: rapid-dark exit loss, treeline ambush cover, weather exposure, stream-crossing in dark)
- Added `## Ambient Interruption Hooks` section (6 hooks: wood-pigeon stop, woodsmoke, farm dog, unresolved rustling, second fire-smell, stream-sound change)

### Next candidate

`cond-kl-witch-label-formation` (scope=project, mirror-tragedy) — the library 122ac card declares `supersedes: [cond-kl-witch-label-formation]` but the project card lacks `superseded_by`. One-line frontmatter fix if the supersede relationship is confirmed correct. Low-cost if confirmed; confirm first because the two cards describe genuinely different trigger mechanisms (flicker-behavioral vs insect-control) and may be parallel rather than sequential.
