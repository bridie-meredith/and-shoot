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
- ~~**Persona-exemplar for viserys-i-targaryen**~~ — **CLEARED 2026-06-06.** Authored and stored at `and-experiment/persona-exemplars/viserys-i-targaryen.md`. Voice demonstrated: indulgent-paternal register, spirited-child-filter conversion in live operation, the "within reason" dissolve.
- ~~**Persona-exemplar for helaena-targaryen-122ac, daenys-velaryon, ser-harwin-the-patient, nymeria-summer-isles, saerys-septa**~~ — **CLEARED 2026-06-06.** All five authored. See persona-exemplar build session entry below.
- **Promotion of project-only cards to library** — `saerys-septa.card.md` and the Viserys project variant are candidates for library promotion if the characters recur in future projects. Flagged; no action this session.
- ~~**Per-character behavior cards for daenys-velaryon and helaena-targaryen-122ac**~~ — **CLEARED 2026-06-06.** Both cards authored in the 2026-06-06 session below. Flag from original session note removed.

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

Principal directive: "more cards" — build the triaged subset of cultivation-library candidate cards that are genuinely card-worthy (real on-page objects + load-bearing world-state). Source material: seven cultivation-library docs + existing warehouse cards for consistency. Schema authority: `schemas/card.schema.md`. All cards initially stored `scope: project` in `and-experiment/warehouse/`. **Promoted to `scope: both` on 2026-06-06** — see library-promotion pass entry. Library copies now live in `cards/<class>/`.

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

No library index updates at initial authoring — all cards were project-scoped at the time. **Updated on 2026-06-06 promotion pass** — see library-promotion pass entry for full index update log.

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

---

## Per-character behavior build: 2026-06-06

### Session scope

Principal directive: author the two per-character behavior cards deferred in the original card-build session (2026-06-05) — flagged as "a per-character behavior card would add value before active shoot." Cards: `daenys-velaryon-behavior` and `helaena-targaryen-122ac-behavior`. Schema authority: `schemas/card.schema.md`. Both cards are `scope: both` — project copies in `and-experiment/warehouse/`, library copies in `cards/dialects/`.

### Cards authored this session

| slug | class | subclass | quality | scope | path (project copy) | path (library copy) |
|------|-------|----------|---------|-------|---------------------|---------------------|
| `daenys-velaryon-behavior` | behavior | per-character-behavior | full | both | `and-experiment/warehouse/daenys-velaryon-behavior.card.md` | `cards/dialects/daenys-velaryon-behavior.card.md` |
| `helaena-targaryen-122ac-behavior` | behavior | per-character-behavior | full | both | `and-experiment/warehouse/helaena-targaryen-122ac-behavior.card.md` | `cards/dialects/helaena-targaryen-122ac-behavior.card.md` |

### Scope decisions

- **daenys-velaryon-behavior → both (project + library).** Daenys is an OC, but her persona card was already promoted to library in the prior session. The counter-thesis register she carries — mechanism-first puncture, deadpan warmth, living-louder vs. living-forever — has cross-project reuse value as an archetype. Consistent with the saerys-targaryen-behavior precedent. Library copy strips the project-specific `references:` entries (`saerys-targaryen-behavior`, `comedy-register`).
- **helaena-targaryen-122ac-behavior → both (project + library).** Canon HOTD character; high cross-project reuse value across all Targaryen-era projects. The riddle-notation register is canon-stable and project-agnostic. Library copy generalizes the samples slightly (removes Saerys-specific framing where possible without losing the voice).

### Register captured

- **daenys-velaryon-behavior:** the counter-thesis register — blunt, warm, mechanism-first; goes to the dose-log before the cultivation gloss; uses apposition to name the accurate thing alongside the cosmological name; the pause before weight; the run-on for affection (the only place she lets the sentence accumulate); the flat-affect delivery of *I love you very much* in the same register as *your stomach is not a furnace.* Primary puncture cadence: deadpan, one saying, no repeat. Non-verbal: economic movement, mechanism-inquiry posture, physical stillness when delivering the load-bearing argument.
- **helaena-targaryen-122ac-behavior:** the riddle-notation register — associative, prophetic non-sequiturs, observation-without-argument, the trailing incomplete sentence; the naturalist's long look before speaking; comfortable silence; follows her own observation track rather than the conversation's surface; finds unusual people simply interesting rather than alarming. Non-verbal: the specimen jar as ambient presence, the crouching attention, the pause before the trailing incomplete.

### Signature lines / monuments anchored

**daenys-velaryon-behavior:**
- Anchor line: *"The dragon doesn't make me less going to die. It makes the dying worth watching. You want to never die. I want to have done something that doesn't need me to last. We are both wrong and both right and I love you very much and your stomach is not a furnace."* — placed in Direct samples as the counter-thesis, fully stated.
- Monument: **the blank line** — named in Memory monuments as the reader's monument, not Daenys's; register-rule makes explicit that she never signals awareness of what she will become; she does not pre-mourn.

**helaena-targaryen-122ac-behavior:**
- Load-bearing sample: *"This one has been dead for a week but the pattern on the wing is the same. They always keep their patterns. I find that useful to remember."* — the pattern-persists monument in direct sample form.
- Monument: **the observation of someone found ordinary** — generalized in library copy from Saerys-specific to the general pattern: there is usually one person Helaena is following closely who she finds interesting rather than alarming; demonstrated through follow-up questions (*"How did you know it would work?"*) and sustained presence.

### Deferred flag cleared

The original card-build session (2026-06-05) noted: "a per-character behavior card would add value before active shoot" for both characters. That flag is cleared. No remaining deferred behavior cards for the and-experiment project cast.

### Index updates

- `cards/dialects/INDEX.md` — added `saerys-targaryen-behavior`, `comedy-register`, `daenys-velaryon-behavior`, `helaena-targaryen-122ac-behavior` to `by_world/planetos` section; added all four to `by_character` section; added per-character (and-experiment) sub-list to `shared/inheritable` section. Note: `saerys-targaryen-behavior` and `comedy-register` were stored to library in the 2026-06-05 session but the INDEX.md had not been updated then; both were added in this session alongside the two new cards.

### Validation pass

Both cards validated against `schemas/card.schema.md`:
- Frontmatter complete: `name`, `class`, `subclass`, `scope`, `project` (project copies), `world`, `character`, `inherits`, `references`, `period`, `region`, `social-class`, `origin`, `quality` all present and correct
- Required body sections present: Direct samples (8 samples each, all tagged `synthesized`), Cadence, Vocabulary (reaches-for, refuses-to-say, register-markers), Syntax, Voice tells, Non-verbal tics, Memory monuments
- Hard-fence compliance: neither card enters the cultivation-register; neither character is a cultivator or setting-blind; both are Westerosi natives
- Canon compliance: Helaena's card consistent with HOTD canon (riddles, insects, prophetic non-sequiturs, gentle affect, no uninvited contact) and with her persona card; Daenys's card consistent with her OC persona card

### Preservation

Both cards are net-new files. No existing warehouse cards overwritten or modified. Persona cards for both characters not touched.

---

## Persona-exemplar build: 2026-06-06

### Session scope

Principal directive: "more cards" + "author the six actor-exemplars margit deferred in the original build session." Six project-bound persona-exemplars for the and-experiment cast. Schema authority: `schemas/persona-exemplar.schema.md`. Authoring process: `staff/margit/exemplar-authoring-process.md`. Model: `and-experiment/persona-exemplars/saerys-targaryen.md`.

### Exemplars authored

| slug | path | length | voice demonstrated |
|------|------|--------|--------------------|
| `viserys-i-targaryen` | `and-experiment/persona-exemplars/viserys-i-targaryen.md` | ~210 words | Indulgent-paternal register; spirited-child-filter converting alarming to charming in real time; the "within reason" caveat that always dissolves |
| `helaena-targaryen-122ac` | `and-experiment/persona-exemplars/helaena-targaryen-122ac.md` | ~220 words | Riddle-notation register; observation-without-argument; trailing incomplete sentence; the naturalist's long look; comfortable silence; follow-up question as warmth |
| `daenys-velaryon` | `and-experiment/persona-exemplars/daenys-velaryon.md` | ~230 words | Counter-thesis register; mechanism-first construction; data-before-interpretation; fond-amused lift; blunt warmth (precise emotional content, flat delivery register) |
| `ser-harwin-the-patient` | `and-experiment/persona-exemplars/ser-harwin-the-patient.md` | ~215 words | Bone-dry incident-log register; the list as primary argument; the sigh as sentence-terminal punctuation; oblique approach to the thing he cannot say directly |
| `nymeria-summer-isles` | `and-experiment/persona-exemplars/nymeria-summer-isles.md` | ~200 words | Flat-precise anthropological register; polite question that already knows; accurate-statement-once discipline; "all right" as full-acceptance closure; witness posture |
| `saerys-septa` | `and-experiment/persona-exemplars/saerys-septa.md` | ~215 words | Formal-devout-courtly register; precision-under-alarm; register tightens as distress rises; Seven-invocation as distress signal; the correct report that will not land |

### QC checklist (per `staff/margit/exemplar-authoring-process.md`)

**Frontmatter validation — all six:**
- [x] All required fields present: `name`, `persona-ref`, `class: persona-exemplar`, `purpose`, `content-match`, `authored-by`, `length`, `fences`
- [x] Names are unique within `and-experiment/persona-exemplars/` and within `cards/persona-exemplars/`
- [x] `persona-ref` resolves to existing project warehouse cards for all six
- [x] `class: persona-exemplar` literal on all six
- [x] `content-match: high` on all six (scene context is adjacent, period-appropriate, not from any active chapter)
- [x] Length within 150-350 words for all six (200-230 word range)
- [x] `fences` has two entries on all six: no-content-import + what-transfers-vs-what-doesn't
- [x] No `dispatch-status: excluded` entries — all six are active

**Body validation — all six:**
- [x] Each opens with `# Exemplar — <persona display name>` header
- [x] Each demonstrates 2-3 load-bearing voice features from the card + behavior card (where present)
- [x] No content overlap with active-project theater/ or draft/ (no chapters exist yet for and-experiment)
- [x] No violation of card hard fences:
  - Viserys: does not discover the note's full scope; not a villain; comedy-tolerant — PASS
  - Helaena: no faction-advocacy; no ambition; riddle-notation is direct not ironic — PASS
  - Daenys: no cultivation-register; no pre-mourning; has own arc — PASS
  - Harwin: no panic; no preachiness; no sycophancy; does not say the direct thing — PASS
  - Nymeria: no cultivation-register; says the accurate thing once; not interrogative — PASS
  - Septa: maintains register; does not lose composure; does not yet know she has lost — PASS
- [x] No meta-commentary in any passage body
- [x] Impersonator discipline: each opens with action or perception, not interior analysis

**Surface-convention fence:**
- [x] None of the six exemplars carry Saerys's cultivation-register, parenthetical-as-aside construction, or account-book cadence. The six are straight, grounded voices — the foils and witnesses. Register separation maintained throughout.
- [x] Comedy register noted: these are the voices Saerys's register-vs-stakes mismatch produces comedy *against*. Each exemplar reads as the unmediated character, not as a straight-man performance.

**Consumer-fit:**
- [x] All six are Tier-1 impersonator targets; no Tier-2 or Tier-3 consumers involved

### Scope decisions

All six stored project-bound at `and-experiment/persona-exemplars/<slug>.md`. Not library-promoted, consistent with the saerys-targaryen precedent. Rationale:
- `viserys-i-targaryen` — the project variant is comedy-tuned; the library card remains scant; library promotion of the exemplar requires library promotion of the card first (flagged for principal triage in prior session)
- `helaena-targaryen-122ac` and `daenys-velaryon` — persona cards were library-promoted; behavior cards were library-promoted; exemplars *could* be library-promoted. However, both exemplars contain Saerys-adjacent scene-setting (the still-room smell, reagent-adjacent context) that gives them higher and-experiment content-match. Recommend library promotion on next pass if the project's voice register proves stable.
- `ser-harwin-the-patient`, `nymeria-summer-isles` — library-promoted persona cards; exemplars are neutral enough to be library candidates. Deferred; project-bound for now.
- `saerys-septa` — project-only OC (no library card); project-bound exemplar only by definition.

### Index updates

- `cards/persona-exemplars/INDEX.md` — added a new section "Impersonator exemplars — project-bound (and-experiment)" with all six entries; updated Coverage notes to record and-experiment 7/7 complete and deferred flags cleared.

### Preservation

All six exemplars are net-new files. No existing persona cards, behavior cards, or warehouse files modified. The saerys-targaryen exemplar at `and-experiment/persona-exemplars/saerys-targaryen.md` was read for format reference only; not modified.

---

## Library-promotion pass: 2026-06-06

### Standing policy (new — record for future card work)

**Cards authored for and-experiment default to `scope: both`** — a library copy in `cards/<class>/` PLUS a project working copy in `and-experiment/warehouse/` (or `and-experiment/persona-exemplars/` for exemplars). Exceptions only when a card genuinely cannot have a library home (e.g. an exemplar whose persona has no library card, such as `saerys-septa`). This matches how persona + behavior cards were already stored. Effective 2026-06-06 per principal directive.

### Cards promoted this pass (7 cards + 6 exemplars)

#### Props (project → library)

| slug | class | project copy scope update | library path |
|------|-------|---------------------------|--------------|
| prop-dose-log | prop | `scope: project` → `scope: both` | `cards/props/prop-dose-log.card.md` |
| prop-harwins-list | prop | `scope: project` → `scope: both` | `cards/props/prop-harwins-list.card.md` |
| prop-account-book | prop | `scope: project` → `scope: both` | `cards/props/prop-account-book.card.md` |

#### Location (project → library)

| slug | class | project copy scope update | library path |
|------|-------|---------------------------|--------------|
| loc-still-room | location | `scope: project` → `scope: both` | `cards/locations/loc-still-room.card.md` |

#### Conditions (project → library)

| slug | class | project copy scope update | library path |
|------|-------|---------------------------|--------------|
| cond-inferior-path-doctrine | condition | `scope: project` → `scope: both` | `cards/conditions/cond-inferior-path-doctrine.card.md` |
| cond-westerosi-poison-pharmacology | condition | `scope: project` → `scope: both` | `cards/conditions/cond-westerosi-poison-pharmacology.card.md` |
| cond-transmigration-previous-life | condition | `scope: project` → `scope: both` | `cards/conditions/cond-transmigration-previous-life.card.md` |

#### Persona-exemplars (project-bound → library-promoted)

| slug | persona-ref | project path | library path |
|------|-------------|--------------|--------------|
| saerys-targaryen | saerys-targaryen | `and-experiment/persona-exemplars/saerys-targaryen.md` | `cards/persona-exemplars/saerys-targaryen.md` |
| viserys-i-targaryen | viserys-i-targaryen | `and-experiment/persona-exemplars/viserys-i-targaryen.md` | `cards/persona-exemplars/viserys-i-targaryen.md` |
| helaena-targaryen-122ac | helaena-targaryen-122ac | `and-experiment/persona-exemplars/helaena-targaryen-122ac.md` | `cards/persona-exemplars/helaena-targaryen-122ac.md` |
| daenys-velaryon | daenys-velaryon | `and-experiment/persona-exemplars/daenys-velaryon.md` | `cards/persona-exemplars/daenys-velaryon.md` |
| ser-harwin-the-patient | ser-harwin-the-patient | `and-experiment/persona-exemplars/ser-harwin-the-patient.md` | `cards/persona-exemplars/ser-harwin-the-patient.md` |
| nymeria-summer-isles | nymeria-summer-isles | `and-experiment/persona-exemplars/nymeria-summer-isles.md` | `cards/persona-exemplars/nymeria-summer-isles.md` |

#### Not promoted

| slug | reason |
|------|--------|
| saerys-septa (exemplar) | persona `saerys-septa` is a project-only OC with no library card; exemplar has no library home; stays at `and-experiment/persona-exemplars/saerys-septa.md` permanently unless persona is promoted |

### Library-copy discipline applied

- Props: all three library copies have `scope: library`; `project:` field omitted (not project-scoped). `references:` entries are all library-resident cards so no stripping was needed.
- Location: library copy has `scope: library`; `project:` field omitted. References to `loc-red-keep-interior`, `saerys-targaryen`, `prop-account-book`, `prop-dose-log`, `cond-inferior-path-doctrine` are all library-resident; no stripping needed.
- Conditions: library copies have `scope: library`; `project:` field omitted. `cond-inferior-path-doctrine` library copy strips the `and-experiment/design/` cross-references from the project copy (those pointed at cultivation-library design docs that are project-scoped); the project-copy references those docs by path; the library copy relies on its own body text and the card's substance only.
- Exemplars: library copies are identical to project copies (no project-specific scene content in the exemplar bodies; fences cover content isolation). Project copies remain at `and-experiment/persona-exemplars/` as working copies.

### Index updates

- `cards/props/INDEX.md` — added `prop-dose-log`, `prop-harwins-list`, `prop-account-book` to `by_world/planetos`, `by_quality/full`, `by_type/portable`.
- `cards/locations/INDEX.md` — added `loc-still-room` to `by_world/planetos` and `by_quality/full`.
- `cards/conditions/INDEX.md` — added `cond-inferior-path-doctrine`, `cond-westerosi-poison-pharmacology`, `cond-transmigration-previous-life` to `by_world/planetos`, `by_quality/full`, and appropriate `by_type` categories (`protagonist-rules` for doctrine + transmigration; `lore-ambient` for pharmacology).
- `cards/persona-exemplars/INDEX.md` — added new "Impersonator exemplars — library (planetos / and-experiment cast)" section with all six promoted exemplars + saerys-targaryen; collapsed project-bound section to saerys-septa only with clear non-promotion rationale; updated coverage notes; recorded standing policy.

### Validation

All library copies validated against their respective schemas:
- 3 prop cards: `class: prop`, `scope: library`, `portability:` set, all required body sections present (Physical Description, Affordances / Uses, Sensory Hooks, Portability, Carry State, Functional State). PASS.
- 1 location card: `class: location`, `scope: library`, all required sections present (Geography, Layout, Sensory Vocabulary, Fixed Props, Exits, Hazards, Ambient Interruption Hooks). PASS.
- 3 condition cards: `class: condition`, `scope: library`, all required sections present (Description, Sensory Impact, Duration, Interaction Notes). PASS.
- 6 exemplars: `class: persona-exemplar`, `persona-ref` resolves to existing library cards, `dispatch-status: active`, lengths within 150-350 range, fences declared, no `excluded-by`/`excluded-reason` needed. PASS.

### Preservation

All library copies are net-new files. Project copies were edited only at the `scope:` field (one line each). No destructive overwrites. Exemplar project copies untouched (library copies are additions, not replacements).

---

## Coverage audit: 2026-06-06

Full Axis-A + Axis-B coverage audit filed at `and-experiment/staff/margit/coverage-audit-2026-06-06.md`. 47 Axis-A entities audited (10 P1 gaps, 8 P2 gaps, 5 P3 gaps, 9 P4 skip/stub); 29 Axis-B candidates assessed (12 recommended build, 7 already built, 10 data-only, 2 ruling-blocked). P1 build manifest: 18 cards across 7 batches. Principal decisions needed on T-1 (oily black stone), T-2 (human-cauldron explicit/latent), unnamed Bk III entourage member, Daenys's dragon name, and Viserys library upgrade.

---

## Cultivation library expansion: 2026-06-06

### Session scope

Principal directive: author a comprehensive maester's cabinet glossary as the 8th document in the cultivation library. The doc is the exhaustive, breadth-first companion to `westeros-alchemy-substances-mystica.md` — the granular apothecary-inventory layer backing every still-room / sick-house / poisoning scene.

### Artifact authored

| # | filename | type | scope | path |
|---|---|---|---|---|
| 8 | maesters-cabinet-glossary.md | authoring substrate | project-scoped | `and-experiment/design/cultivation-library/maesters-cabinet-glossary.md` |

**Summary:** 11 categories, approximately 90 substance entries plus 10 preparation-form entries and 7 tool/equipment entries. Categories: analgesics/sedatives, poisons/toxins, antiseptics/wound care, fever/inflammation/infection, digestive/purgative/emetic, women's medicine/reproductive, stimulants/tonics/restoratives, minerals/chemical reagents, preparation bases/solvents, preparation forms, tools/equipment. Each entry: name + canon-tag + real properties + dose/effect at a glance + Saerys's cultivation-tier note (pointing at the Tier 0–4 table in `cultivation-genre-reference.md` § Part IV.B without restating it). Includes an opening access-structure section (who controls Westerosi medicines; the gradient from freely accessible to locked cabinet to external sourcing). Consistent with `cond-westerosi-poison-pharmacology.card.md` (dose details deferred to that card), `loc-still-room.card.md` (reagent inventory cross-referenced), and `westeros-alchemy-substances-mystica.md` (magical substances cross-referenced, not duplicated).

**Tag split (approximate):** ~25 `[canon]` or `[canon-uncertain]` entries; ~65 `[real-world / plausible in setting]` entries.

**New canon-uncertain items:** 5 (items 24–28 in the consolidated worklist; see INDEX.md).

**New candidate card flagged:** `cond-maesters-cabinet` — condensed 15–20 substance quick-ref for bones authors; see INDEX.md.

### Index updates

- `and-experiment/design/cultivation-library/INDEX.md` — added doc #8 to the doc table and "Use this when..." map; updated reading-order note to reflect 7 foundation docs + 1 apothecary doc; updated canon-uncertain count 23→28 (items 24–28 added); updated candidate-card list 28→29 (new `cond-maesters-cabinet` flag added); updated footer to record 2026-06-06 update.

### Preservation

`maesters-cabinet-glossary.md` is a net-new file. No existing library docs, warehouse cards, or persona files were modified. `INDEX.md` received additive edits only (new table row, reading-order note extension, canon-uncertain list extension, candidate-card list extension, footer update). `margit.memory.md` received additive log entry only.

---

## P1 card build — completion + cataloging (2026-06-06, principal-finished after agent stalls)

The P1 build (coverage-audit manifest) was run as 5 parallel batches; 4 stalled mid-run. Recovery: a completion pass wrote the 5 missing warehouse cards then also stalled before library copies + cataloging. The principal finished the remainder directly in-session:

- **All 18 P1 cards present in BOTH copies** (warehouse scope:both + cards/ scope:library). The 7 missing library copies were created by frontmatter transform (scope both→library, project field dropped; no design-path blocks present to strip).
- **Cataloging done by hand:** added the 18 P1 cards to `cards/personas/INDEX.md` (saerys-maester, the-factor), `cards/props/INDEX.md` (cradle-egg, christening-spoon, kings-hand-note, bill-of-exchange, still-room-kit, wildfire-shard), `cards/conditions/INDEX.md` (reagent-tier-map, technique-hierarchy, formation-map-red-keep, heavenly-dao-calibration, heartless-dao-scripture, alchemists-guild-122ac, trade-network-formation, maesters-cabinet), `cards/locations/INDEX.md` (maegors-holdfast, sick-house). Registered the GRRM×cultivation grid as cultivation-library doc #9.
- **FLAG — pre-existing INDEX gap discovered:** the and-experiment CAST persona library files (saerys-targaryen, helaena-targaryen-122ac, daenys-velaryon, ser-harwin-the-patient, nymeria-summer-isles) are ABSENT from `cards/personas/` on this branch (`claude/cool-feynman-gNpmm`), which is 38 commits behind origin/main. Likely they live on main; needs reconcile-with-main to confirm/restore. Not resolved here.
