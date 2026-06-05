# Margit Working Memory — and-experiment

## Card build session: 2026-06-05

### Session scope
Gap-card build for the and-experiment project (cultivation-reincarnation comedy, pre-Dance Westeros). Authored per instruction: conform to `schemas/card.schema.md`, honor hard fences (setting-blind protagonist, canon-clean OC, comedy re-tone of grimdark substrate, broken-clock guard).

### Cards authored this session

| slug | class | subclass | quality | tier | scope | path (project copy) | path (library copy) |
|------|-------|----------|---------|------|-------|---------------------|---------------------|
| saerys-targaryen | persona | — | full | lead | both | `and-experiment/warehouse/saerys-targaryen.card.md` | `cards/personas/saerys-targaryen.card.md` |
| saerys-targaryen-behavior | behavior | per-character-behavior | full | — | both | `and-experiment/warehouse/saerys-targaryen-behavior.card.md` | `cards/dialects/saerys-targaryen-behavior.card.md` |
| saerys-targaryen (exemplar) | persona-exemplar | — | — | — | project-bound | `and-experiment/persona-exemplars/saerys-targaryen.md` | (not promoted; project-bound only at this stage) |
| viserys-i-targaryen | persona | — | full | supporting | project | `and-experiment/warehouse/viserys-i-targaryen.card.md` | (not separately stored; promoted from projects/project_05 actor copy; library card at cards/personas/viserys-i-targaryen.card.md remains scant) |
| helaena-targaryen-122ac | persona | — | full | supporting | both | `and-experiment/warehouse/helaena-targaryen-122ac.card.md` | `cards/personas/helaena-targaryen-122ac.card.md` |
| daenys-velaryon | persona | — | full | supporting | both | `and-experiment/warehouse/daenys-velaryon.card.md` | `cards/personas/daenys-velaryon.card.md` |
| ser-harwin-the-patient | persona | — | full | supporting | both | `and-experiment/warehouse/ser-harwin-the-patient.card.md` | `cards/personas/ser-harwin-the-patient.card.md` |
| nymeria-summer-isles | persona | — | full | supporting | both | `and-experiment/warehouse/nymeria-summer-isles.card.md` | `cards/personas/nymeria-summer-isles.card.md` |
| saerys-septa | persona | — | full | minor | project | `and-experiment/warehouse/saerys-septa.card.md` | (not separately stored; project-only OC) |
| comedy-register | behavior | shared-behavior | full | — | both | `and-experiment/warehouse/comedy-register.card.md` | `cards/dialects/comedy-register.card.md` |
| loc-red-keep-interior | location | — | full | — | both | `and-experiment/warehouse/loc-red-keep-interior.card.md` | `cards/locations/loc-red-keep-interior.card.md` |

### Index updates

- `cards/personas/INDEX.md` — added: `daenys-velaryon`, `helaena-targaryen-122ac`, `nymeria-summer-isles`, `saerys-targaryen`, `ser-harwin-the-patient` to `by_world/planetos`; added all five to `by_quality/full`; added all five to `targaryen-era` trope; added five new entries to `original_characters`.
- `cards/dialects/INDEX.md` — added: `saerys-targaryen-behavior` (per-character) and `comedy-register` (shared) to `by_world/planetos` and `shared/inheritable` sections; added `saerys-targaryen` to `by_character` section.
- `cards/locations/INDEX.md` — added: `loc-red-keep-interior` to `by_world/planetos` and `by_quality/full`.
- `cards/persona-exemplars/INDEX.md` — added project-bound exemplar entry for `saerys-targaryen`.

### Deferred / not built

- **saerys-septa library copy** — the Septa is a project-scoped OC without reuse potential outside and-experiment. Library copy deferred; project copy is in `and-experiment/warehouse/saerys-septa.card.md`.
- **viserys-i-targaryen library upgrade** — the existing library card at `cards/personas/viserys-i-targaryen.card.md` remains scant. The and-experiment project variant is full-quality and lives at `and-experiment/warehouse/viserys-i-targaryen.card.md`. A formal library promotion (scant→full merge) was not executed because the project variant is tailored to comedy-tolerant tone and the generic library card serves other projects in different registers. Promotion flagged for principal triage.
- **Persona-exemplar for viserys-i-targaryen** — not authored; he is supporting, on-stage, and Tier-1 eligible but his scenes are warm-cage-comedy beats that are well-covered by the card alone at this stage. Flag for authoring when active.
- **Persona-exemplar for helaena-targaryen-122ac, daenys-velaryon, ser-harwin-the-patient, nymeria-summer-isles, saerys-septa** — not authored; all five are supporting/minor tier. Per the gate, exemplars are required before `/and-cast` Phase 5 (if that gate fires for this project). Flag for authoring when cast is locked.
- **Promotion of project-only cards to library** — `saerys-septa.card.md` and the Viserys project variant are candidates for library promotion if the characters recur in future projects. Flagged; no action this session.

### Validation pass

All authored cards validated against `schemas/card.schema.md`:
- All persona cards: frontmatter complete (`name`, `class`, `scope`, `world`, `persona-purpose`, `origin`, `quality`, `tier`); required body sections present (Description, Voice, Taste, Pet Peeves); Fiction Role Overlay populated for all.
- All behavior cards: frontmatter complete (`character` or sentinel, `subclass`, `inherits`, `period`); required body sections present (Direct samples, Cadence, Vocabulary, Syntax, Voice tells, Non-verbal tics, Memory monuments).
- Location card: all required sections present (Geography, Layout, Sensory Vocabulary, Fixed Props, Exits, Hazards, Ambient Interruption Hooks).
- Persona-exemplar: frontmatter complete per exemplar schema; length ~230 words (within 150–350 range); fences declared.

### Preservation notes

No pre-existing cards were overwritten. All new cards are net-new files. The existing `viserys-i-targaryen.card.md` (scant, library) was read but not modified; the project variant is stored separately under `and-experiment/warehouse/`. No destructive operations this session.

---

## Reference authoring session: 2026-06-05

### Artifact authored

| artifact | type | scope | path |
|---|---|---|---|
| cultivation-genre-reference.md | authoring substrate (reference doc) | project-scoped | `and-experiment/design/cultivation-genre-reference.md` |

**What it is:** A catalogued cultivation (xianxia) genre conventions reference — the genre layer beneath `comedy-register.card.md` and `saerys-targaryen-behavior.card.md`. Covers 10 domains: (1) cosmology and realm ladder, (2) alchemy and pill refining, (3) spirit beasts, (4) resources and reagents, (5) social order, (6) sects, (7) moral axes and the Heavenly Demon title, (8) tribulations, (9) the detachment doctrine, (10) standard narrative tropes. Each domain carries a two-layer treatment: genre canon (A) + project broken-clock mapping (B). Closes with a precision-of-wrongness vocabulary bank, terminology reconciliations, candidate card flags, and principal tensions/gaps.

**Terminology reconciliations made:**
- Foundation Establishment confirmed at Stage 2 of the canonical realm ladder; consistent with behavior card usage
- The seven emotions (七情) confirmed as real cultivation term; canonical list grounded
- Outer disciples / sect hierarchy confirmed; consistent with behavior card vocabulary
- Tier/grade usage documented as intentionally loose in the cards; prose authors may follow card convention

**Candidate card flags (for principal triage; none built this session):**
- `cond-inferior-path-doctrine.card.md`
- `prop-dose-log.card.md`
- `prop-harwins-list.card.md`
- `cond-westeros-reagent-tier-map.card.md`
- `cond-yi-ti-cultivation-milieu.card.md`

**Principal tensions/gaps flagged:**
1. Oily black stone actual properties — does the cauldron's appetite register anything real, or is the horror purely appetite?
2. Realm-ladder vs project-tier-system reconciliation — formal mapping deferred to principal
3. Human-cauldron trope legibility in prose — latent vs explicit; register decision for principal

**Preservation:** net-new file; no existing files overwritten or modified.
