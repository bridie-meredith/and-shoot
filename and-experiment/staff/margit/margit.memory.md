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

### Artifacts authored (seven documents — full cultivation library)

All seven documents are co-located at `and-experiment/design/cultivation-library/` (subdirectory created 2026-06-05 during cataloging pass; git mv from flat `and-experiment/design/` location **completed 2026-06-05**).

| # | filename | type | scope | path |
|---|---|---|---|---|
| 1 | cultivation-genre-reference.md | authoring substrate | project-scoped | `and-experiment/design/cultivation-library/cultivation-genre-reference.md` |
| 2 | cultivation-types-methods-phenomenology.md | authoring substrate | project-scoped | `and-experiment/design/cultivation-library/cultivation-types-methods-phenomenology.md` |
| 3 | westeros-alchemy-substances-mystica.md | authoring substrate | project-scoped | `and-experiment/design/cultivation-library/westeros-alchemy-substances-mystica.md` |
| 4 | cultivation-techniques-arts-and-artifacts.md | authoring substrate | project-scoped | `and-experiment/design/cultivation-library/cultivation-techniques-arts-and-artifacts.md` |
| 5 | cultivation-cosmology-dao-law-and-dark-paths.md | authoring substrate | project-scoped | `and-experiment/design/cultivation-library/cultivation-cosmology-dao-law-and-dark-paths.md` |
| 6 | cultivation-metagenre-roots-and-archetypes.md | authoring substrate | project-scoped | `and-experiment/design/cultivation-library/cultivation-metagenre-roots-and-archetypes.md` |
| 7 | cultivation-aphorisms-and-dao-sayings.md | authoring substrate | project-scoped | `and-experiment/design/cultivation-library/cultivation-aphorisms-and-dao-sayings.md` |

**Note on file locations:** Docs #1–7 were physically authored at `and-experiment/design/<filename>`, then moved into `and-experiment/design/cultivation-library/` via `git mv` on 2026-06-05 (the cataloging session had no shell tool; the principal executed the recorded git mv block immediately after). All seven now reside at the paths above; the INDEX.md sits beside them.

**What the library is:** The genre layer beneath `comedy-register.card.md` and `saerys-targaryen-behavior.card.md` — the full cultivation (xianxia/xiuzhen) reference set for and-experiment. Hard fence: the broken clock stays broken; nothing in the library makes qi/cultivation magic real in-story; only mithridatism and Westerosi magical materials produce real effects.

**Doc #1 summary (cultivation-genre-reference.md):** 10 cultivation domains with broken-clock mappings: realm ladder (9 stages), alchemy/pill refining, spirit beasts, resources/reagents (Tier 0–4 table), social order, sects, moral axes, tribulations, detachment doctrine, standard tropes. Closes with precision-of-wrongness vocabulary bank. Foundational doc — read first.

**Doc #2 summary (cultivation-types-methods-phenomenology.md):** 22-path taxonomy (body = PRIMARY, poison = SECONDARY, gluttony = structural THIRD unconscious). Methods of cultivation (14 methods). Body-tempering 7-stage deep-dive. Phenomenology table (what she perceives vs. what is happening). Perk table (one real perk: mithridatism resistance).

**Doc #3 summary (westeros-alchemy-substances-mystica.md):** Western alchemical science (Great Work, tria prima, spagyric). ASOIAF substances catalogue (dragonglass, Valyrian steel, wildfire, dragon blood/bone/eggs, weirwood, shade of the evening, 10-poison list, oily black stone as Tier 4 horror). Mystical entity bestiary. Three-register cross-map (cultivation reading / maester reading / ASOIAF truth). 16 canon-uncertain items.

**Doc #4 summary (cultivation-techniques-arts-and-artifacts.md):** Technique hierarchy (mortal-grade through divine-grade), martial arts/divine abilities, artifact grade ladder, formations/arrays. Saerys-mappings: account-book = fabao/natal artifact; factors = puppets-with-free-will; Red Keep = grand defensive formation; document-heist = formation-breaking.

**Doc #5 summary (cultivation-cosmology-dao-law-and-dark-paths.md):** Realm cosmology, Heavenly Dao metaphysics, karma/merit/luck system, dark-cultivation cluster in full (blood sacrifice, corpse cultivation, ghost cultivation, soul refining, human-cauldron as cultivation-genre horror, devil transformation, soul-erosion, corruption mechanics). Escalation trajectory table Bk I → Bk III.

**Doc #6 summary (cultivation-metagenre-roots-and-archetypes.md):** Transmigration/reincarnation sub-genre (Saerys as meta-transmigrator, golden finger = library of incorrect maps, no system). Genre-family taxonomy (wuxia/xianxia/xuanhuan/xiuzhen/LitRPG/cultivation-comedy). Cast archetype map. Comedy/deconstruction conventions. Real-world Daoist/Buddhist/Chinese roots.

**Doc #7 summary (cultivation-aphorisms-and-dao-sayings.md):** 100 original aphorisms in 12 groups, curdle-tagged ([farce], [gallows], [farce→gallows]). 8 signature lines (H-02, D-01, D-02, D-07, D-14, R-02, P-02, X-01) with three-deployment escalation arc. Public-domain Daoist/Buddhist/Confucian roots appendix with Saerys's register-warp for each classical source.

**Terminology reconciliations (from doc #1):**
- Foundation Establishment confirmed at Stage 2 of the canonical realm ladder; consistent with behavior card usage
- The seven emotions (七情) confirmed as real cultivation term; canonical list grounded
- Outer disciples / sect hierarchy confirmed; consistent with behavior card vocabulary
- Tier/grade usage documented as intentionally loose in the cards; prose authors may follow card convention

**Preservation:** All seven docs are net-new files. No existing files overwritten or modified.

---

## Cataloging pass: 2026-06-05

### What was done

Consolidated the seven cultivation reference documents into a proper indexed library. Created `and-experiment/design/cultivation-library/` subdirectory. Authored `and-experiment/design/cultivation-library/INDEX.md` (the master index).

### INDEX.md at `and-experiment/design/cultivation-library/INDEX.md`

Contents: header (what the library is, the broken-clock fence, authored date, subdirectory location), reading order/dependency note, "Use this when..." map (7 rows, one per doc), consolidated candidate-card list (28 distinct slugs deduped across all 7 docs), consolidated canon-uncertain list (23 items), consolidated open rulings (20 items, 3 priority groups).

### Cross-reference integrity

Verified via grep: zero path-style cross-references exist among the seven documents. All inter-doc references use bare filenames. No body edits were needed. Co-location in the subdirectory preserves all references.

### Consolidated counts

| Category | Count |
|---|---|
| Candidate cards (distinct, deduped) | 28 |
| Canon-uncertain items | 23 |
| Open rulings (principal decisions needed) | 20 |

### Open rulings by priority tier

**High-priority (recur across 3+ docs — gate the most downstream work):**
- T-1: Oily black stone final disposition (docs #1, #3, #5) — 3 options: (A) Tier 4 inert horror-only, (B) Tier 4 genuine appetite-satisfier with cost, (C) Tier 4 corruption vector with no benefit. Must be decided before Book III bones.
- T-2: Human-cauldron in prose — explicit vs. latent register (docs #1, #5, #6). Must be decided before any Bk II/III dual-image beat is authored.
- T-3: Daenys's death — dao-companion archetype convergence or deviation (docs #6, and Dance canon). Must be decided before any Bk I close or Bk II open beats.

**Medium-priority (recur across 2 docs):**
- T-4: Wildfire-fever — real magic vs. toxic reaction (docs #3, #2)
- T-5: Dragon-egg foundational ambiguity — does ingestion produce any real effect? (docs #3, #2)
- T-6: Gluttony-path Book III framing — structural path named explicitly or latent? (docs #2, #5)
- T-7: Yi Ti magical status canon-uncertainty (docs #1, #5)
- T-8: Dao-heart cultivation and Saerys's genuine intellect — treated as spiritual or satirized? (docs #2, #6)
- T-9: Viserys as shizun — is the internal weight at account-closure Bk I or Bk II? (docs #6)

**Single-source (docs #1–7, one mention each):**
- T-10 through T-20: realm-ladder vs. project-tier-system formal mapping; lightning-tempering scene possibility; mithridatism payoff staging; ship-heist formation vocabulary; natal-artifact declaration and Bk III payoff; formation vocabulary for entourage; soul-erosion vs. blank-line reading; arhat vs. bodhisattva in endgame; Helaena's arc and warm-spot breakage; Aemond deviant-young-master with no face-slap; qi-projection absence and Bk III consequence.

### git mv commands (executed 2026-06-05)

The cataloging session had no shell tool; the principal ran the following block immediately after, moving the seven source files from `and-experiment/design/<filename>` to `and-experiment/design/cultivation-library/<filename>` with git history preserved.

```
git mv and-experiment/design/cultivation-genre-reference.md and-experiment/design/cultivation-library/cultivation-genre-reference.md
git mv and-experiment/design/cultivation-types-methods-phenomenology.md and-experiment/design/cultivation-library/cultivation-types-methods-phenomenology.md
git mv and-experiment/design/westeros-alchemy-substances-mystica.md and-experiment/design/cultivation-library/westeros-alchemy-substances-mystica.md
git mv and-experiment/design/cultivation-techniques-arts-and-artifacts.md and-experiment/design/cultivation-library/cultivation-techniques-arts-and-artifacts.md
git mv and-experiment/design/cultivation-cosmology-dao-law-and-dark-paths.md and-experiment/design/cultivation-library/cultivation-cosmology-dao-law-and-dark-paths.md
git mv and-experiment/design/cultivation-metagenre-roots-and-archetypes.md and-experiment/design/cultivation-library/cultivation-metagenre-roots-and-archetypes.md
git mv and-experiment/design/cultivation-aphorisms-and-dao-sayings.md and-experiment/design/cultivation-library/cultivation-aphorisms-and-dao-sayings.md
```

After running these, `and-experiment/design/` will contain only: `README.md`, `convergence-process.md`, `cultivation-library/` (subdirectory), and `run-01/` (subdirectory). The three non-moved items were explicitly excluded per task spec.

### Showrunner memory routing pointer recommendation

YES — recommend adding a pointer to showrunner memory (`and-experiment/staff/showrunner/memory.md`). Suggested routing: under the "World layer" or "Reference materials" section, add a one-line entry: "Cultivation library: `and-experiment/design/cultivation-library/INDEX.md` — 7 docs, 28 candidate cards, 23 canon-uncertain items, 20 open rulings (T-1/T-2/T-3 are blocking for Bk II+)." The showrunner should surface the top-3 rulings (T-1/T-2/T-3) in its active tensions list. Without this pointer, the library is inaccessible to screen-writer and impersonator dispatches that go through showrunner context first.

### Preservation

No existing files overwritten. INDEX.md is a net-new file. The seven docs were relocated into `cultivation-library/` via `git mv` (history preserved), executed by the principal right after this pass. No story cards were touched; the showrunner-memory routing pointer (recommended below) was added by the principal in the same step.

---

## Batch card build session: 2026-06-06

### Session scope

Principal directive: "more cards" — build the triaged subset of cultivation-library candidate cards that are genuinely card-worthy (real on-page objects + load-bearing world-state). Source material: seven cultivation-library docs + existing warehouse cards for consistency. Schema authority: `schemas/card.schema.md`. All cards are project-scoped; stored in `and-experiment/warehouse/`. No library promotions (same rationale as `saerys-septa` precedent — these are and-experiment-specific).

### Cards authored this session

| slug | class | path | one-line |
|---|---|---|---|
| `prop-dose-log` | prop | `and-experiment/warehouse/prop-dose-log.card.md` | Saerys's mithridatism record; simultaneously a poison-tolerance log and the Inferior Path's technique manual; 200 documented events across 40+ substances; the Book III broken-clock ring |
| `prop-harwins-list` | prop | `and-experiment/warehouse/prop-harwins-list.card.md` | Ser Harwin's running list of prohibited mouth-items (44 entries + one unfinished); primary running-gag instrument; also a love letter in incident-log form; the last entry is item 44 |
| `prop-account-book` | prop | `and-experiment/warehouse/prop-account-book.card.md` | The ledger only she can read; classified by her as Tier 2 dao-artifact approaching natal-artifact status; the network's formation eye; the one place deaths are entered; the blank line lives here |
| `loc-still-room` | location | `and-experiment/warehouse/loc-still-room.card.md` | The Red Keep maester's still-room as Saerys's operational domain; fixed layout + portable kit section (re-established at each location, incl. Essos); nested under `loc-red-keep-interior` |
| `cond-inferior-path-doctrine` | condition | `and-experiment/warehouse/cond-inferior-path-doctrine.card.md` | The codified cosmology as she believes it — realm ladder, cauldron method, heartless dao, karma accounting, the seven emotions classification; her subjective world-model with real-state column throughout; impersonator consistency anchor |
| `cond-westerosi-poison-pharmacology` | condition | `and-experiment/warehouse/cond-westerosi-poison-pharmacology.card.md` | Real pharmacological truth for all substances she works with — actual mechanisms, dose→lethality windows, mithridatism efficacy, tolerance ceilings; alongside her cultivation-gloss; the broken clock's factual substrate |
| `cond-transmigration-previous-life` | condition | `and-experiment/warehouse/cond-transmigration-previous-life.card.md` | The previous-life event — what she died doing (alone on a floor, reading), what carried over (the archive / incorrect maps / no-system condition), the wound the armor is built over; standalone card (see decision note in card body) |

### Transmigration decision

**Standalone condition card** — not folded into persona card. Rationale recorded in the card's Decision Note section. Summary: the persona card's Vibe Seeds already covers the previous life at the correct level of abstraction for a persona card; the condition card adds authoring-substrate depth (transmigrator sub-genre framing, no-system architecture, golden-finger analysis, wound structure) that belongs at the condition layer, not the persona layer. Persona card not modified.

### Cross-references wired (internal coherence)

- `prop-dose-log` ↔ `cond-inferior-path-doctrine` (the log is the doctrine's technique manual)
- `prop-dose-log` ↔ `cond-westerosi-poison-pharmacology` (the log records what the pharmacology explains)
- `prop-account-book` ↔ `cond-inferior-path-doctrine` (the account-book is where the doctrine meets the commercial network)
- `prop-account-book` ↔ `loc-still-room` (cross-referenced as both are primary workspace instruments)
- `loc-still-room` ↔ `loc-red-keep-interior` (nested reference; the still-room extends that card's Maester's Tower section)
- `cond-inferior-path-doctrine` ↔ `cond-westerosi-poison-pharmacology` (doctrine is framing; pharmacology is truth; every substance entry in the doctrine has a real-state counterpart in the pharmacology card)
- `cond-transmigration-previous-life` ↔ `cond-inferior-path-doctrine` (the doctrine is the previous life's archive, operationalized)
- All seven cards ↔ `saerys-targaryen` (the persona card is the root reference for all)

### Index updates

No library index updates — all cards are project-scoped. No promotions to `cards/` library executed.

### Validation pass

All seven cards validated against `schemas/card.schema.md`:

**Prop cards (3):**
- Frontmatter complete: `name`, `class`, `scope`, `project`, `world`, `portability`, `origin`, `quality`, `references` all present and correct
- Body sections present for all: Physical Description, Affordances / Uses, Sensory Hooks, Portability, Carry State, Functional State
- `portability: portable` correct for all three (none are fixed architectural)

**Location card (1):**
- Frontmatter complete: `name`, `class`, `scope`, `project`, `world`, `origin`, `quality`, `references` all present
- Body sections present: Geography, Layout, Sensory Vocabulary, Fixed Props, Exits, Hazards, Ambient Interruption Hooks
- Portable-vs-fixed elements section integrated into Layout (folded still-room kit as directed; not a separate card)

**Condition cards (3):**
- Frontmatter complete: `name`, `class`, `scope`, `project`, `world`, `origin`, `quality`, `references` all present
- Body sections present: Description, Sensory Impact, Duration, Interaction Notes
- Hard-fence compliance verified: all three explicitly label Saerys's beliefs vs. real-state; no card asserts qi is real in-story

### Preservation

All seven cards are net-new files. No existing warehouse cards overwritten or modified. Persona card (`saerys-targaryen.card.md`) not touched.
