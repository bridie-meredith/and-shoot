# Library Improvement Loop — Ledger

Tracks one-op passes over the card library. Each entry: scan summary → op chosen → cards touched → next candidate.

---

## Pass 1 — 2026-06-12

### Scan summary

**Directories scanned:** `cards/` (personas, locations, props, conditions, dialects/behaviors), `and-experiment/warehouse/`, `active-project/warehouse/` (absent).

**Scant cards found:**

| Card | Class | Notes |
|------|-------|-------|
| `cards/personas/viserys-i-targaryen.card.md` | persona | Missing: Taste, Pet Peeves, Relationships, Vibe Seeds, Look, Default Stance, Action Menu, Action Costs, Triggers, Off-Screen Cadence |
| `cards/personas/aegon-ii-targaryen.card.md` | persona | Very thin — same missing sections; s3 climax role only |
| `cards/personas/aemond-targaryen.card.md` | persona | Base card scant; project uses full `aemond-targaryen-122ac` variant |
| `cards/personas/victoria-dallon.card.md` | persona | Worm character; sparse; not in active project |
| `cards/personas/oc-plumms-man.card.md` | persona | Minor OC |
| `cards/personas/oc-girl-from-hamlet.card.md` | persona | Minor OC |
| `cards/personas/oc-tributary-village-newcomer.card.md` | persona | Minor OC |
| `cards/personas/peasant-woman-forest.card.md` | persona | Minor OC |
| `cards/locations/forest-clearing-dusk.card.md` | location | Scant OK per schema |
| `cards/locations/oc-stitch-house-lane.card.md` | location | Scant OK per schema |
| `cards/locations/loc-red-keep-outer-ring.card.md` | location | Scant OK per schema |
| `cards/props/oc-procedural-form.card.md` | prop | Scant OK per schema |
| `cards/props/oc-water-skin.card.md` | prop | Scant OK per schema |
| `cards/props/oc-fish-account-ledger.card.md` | prop | Scant OK per schema |

**Schema violations:** None found. All `cards/dialects/*.md` cards already use `class: behavior` (not deprecated `class: dialect`).

**Fuzzy-duplicate clusters:** Era-variant clusters present (`cond-reincarnation-mechanics` × 3, `cond-westerosi-customary-authority` × 3, `mira-stonefield` × 3) — intentional variant-of chains, not fuzzy duplicates.

**Thin zones:** No earth-bet location cards exist for Worm-setting projects; all locations are Westeros/planetos. Low priority — current project is Westeros-set.

**Archetype candidates:** Westeros shared-behavior cards (`westeros-grrm-mannerisms`, `westeros-noble-courtly`, `westeros-maester`, `westeros-septon`, `westeros-smallfolk`, `westeros-northern`) form a potential paradigm cluster. Not selected this pass — behavior cards are not the scant-gate concern.

### Operation chosen

**RESCUE** — `cards/personas/viserys-i-targaryen.card.md` → `quality: full`

**Rationale:** Highest impact-to-cost among scant personas. King Viserys is the structural apex of the political system in every HotD project. The existing scant card has a solid foundation (Description, Voice brief, Hard Fences, Stats, Thematic Purpose). Missing sections are well-supported by extensive Fire & Blood / HotD canon. Rescuing this unblocks the persona from the cast-gate (schema: "Scant + used = blocking rescue before cast entry") for any future HotD project that brings him on-stage.

`aemond-targaryen` skipped: project-scoped `aemond-targaryen-122ac` is already `quality: full`; the base card's scant status is lower urgency.

### Cards touched

- `cards/personas/viserys-i-targaryen.card.md` — rescued to `quality: full`

### Next candidate

`cards/personas/aegon-ii-targaryen.card.md` — very thin supporting persona (s3 climax role); same missing-sections pattern; ready for rescue next pass.

---
