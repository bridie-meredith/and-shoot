# Bones Schema

The bones file is the SVO bone-structure of a chapter (formerly "episode" under shoot-v2 pre-substance). Each line is a **bone** — a subject doing a discrete, observable action — and the file is the flattened scene-ordered view of `chapters[].scenes[].bones[]` from showrunner memory.

Schema authority: this file. Renamed 2026-05-17 from `proto-line.schema.md` under the substance overhaul (no body-format change; renamed for vocabulary consistency with `/and-write`). Pre-substance "proto-line" terminology in the body text below has been replaced with "bone"; the unit is the same. The earlier two-coexisting-path conventions (per-episode + season-aggregate) are dropped — under the new chain only the per-chapter path is authored.

---

## File path convention

**Per-chapter (current):** `active-project/theater/bones/<book>-<chapter>.md` (e.g. `theater/bones/b01-c01.md`). Authored by `/and-write` Phase 7 from `chapters[<chapter>].scenes[].bones[]` in showrunner memory. Source of truth is memory; the bones file is a flattened serialization for downstream `/and-facets` and `/and-stitch` consumption.

**Atomic emit set (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25).** The bones file + the scene-map facet + per-character dialogue files at `theater/dialogue/<character-slug>.md` are co-emitted by `/and-write` Phase 7 as an atomic set. Dialogue is no longer authored downstream by `/and-facets`. The bones file ships with dialogue-citation tokens already attached on dialogue-anchor bones (see § Citations).

Legacy paths (`theater/proto-lines/<slug>.md`, `theater/proto-lines/<season-slug>.aggregate.md`, top-level `theater/proto-lines.md`) are no longer authored. Pre-substance projects on disk remain readable but the new chain does not write to those paths.

---

## File header (required — seven fields)

Every bones file begins with a seven-field extended header (preserved from the pre-substance per-episode emission shape):

```
# bones — <chapter-slug>

episode: <chapter-slug>
narrator: <pov-actor-slug>
goal: <one sentence — what this chapter shows the audience>
cast: <slug>, <slug>, <slug>, ...
locations: <loc-slug>, <loc-slug>, ...
prior_episode: <prior-chapter-slug | none>
aggregate_range: 1-<N>
```

Field rules:

- **`episode:`** — the chapter slug (matches filename). The field name stays `episode:` for downstream-compatibility with `/and-facets` Phase 0's existing parser; the value is the chapter slug (e.g. `b01c01`). Facet authors lift verbatim into facet-file `episode:` frontmatter.
- **`narrator:`** — POV actor slug. Sourced from `chapters[<chapter>].pov_narrator` in showrunner memory (populated by `/and-substance chapter` Phase 3). Pass 5 continuity enforces narrator-consistency; lines whose content cannot be observed from this POV fault as `FAULT-POV`.
- **`goal:`** — one-sentence north star for the chapter. Sourced from `chapters[<chapter>].goal` in showrunner memory (populated by `/and-substance chapter` Phase 4). Pass 4 trim consults `goal` when judging chatter.
- **`cast:`** — comma-separated actor slugs that appear as a SUBJECT or as a `speaks to <listener>` listener anywhere in the chapter's bones. Computed at serialization via slug-grep over the chapter's bones (no inference, no card lookup). Order: by first-appearance flat_id.
- **`locations:`** — comma-separated location slugs the studio fork must load to author location-state. Computed via slug-grep over bone OBJECTs/SUBJECTs and resolved against the active warehouse's loc cards.
- **`prior_episode:`** — slug of the previous chapter in chapter order, or `none` for the first chapter of the first book. Field name kept for downstream-compatibility; value is the chapter slug.
- **`aggregate_range:`** — kept for schema compatibility; trivially `1-<N>` since `/and-write` authors the chapter directly without aggregate-split.

A missing or empty header field faults `FAULT-HEADER-<FIELD>` at Pass 2.

A blank line follows the header before the body begins.

---

## Body format

Plain text, newline-separated entries. One bone per line. No section headers, no scene markers in the body, no markdown bullets. Scene boundaries are carried by the co-emitted scene-map facet at `theater/facets/scene-map-<book>-<chapter>.md`, not by markers inside the bones file.

```
<flat_id> SUBJECT VERB OBJECT [<cited-id>, <cited-id>, ...]
```

Example:
```
narrator: taylor-hebert-westeros
goal: Show the audience Taylor's first brush with Westerosi administrative machinery.

1 taylor-hebert-westeros wakes in the loft
2 taylor-hebert-westeros descends the loft ladder
3 septon-dying-protector breathes
4 taylor-hebert-westeros crosses the cottage floor

5
6 taylor-hebert-westeros lights a candle
```

---

## Field rules

### `<flat_id>`

- Monotonic positive integer, file-scoped. Starts at 1.
- Assigned by `/and-write` Phase 7 at serialization, walking scenes in order. The in-memory bone slug (`b01c01s01n01`) is the authoring/audit handle; the flat_id is the file/citation handle that `/and-facets` writes `[<facet>:<flat_id>]` against.
- **Stable within a run** — once assigned, never reused, never reassigned during the same `/and-write` invocation. Re-running `/and-write redo` produces the same flat_ids as long as scene/bone counts are stable; `revise` mode preserves flat_ids for unchanged bones (revised bones get new flat_ids by gap-filling within the chapter to keep monotonicity tight).
- Deletions leave the flat_id gap visible. A skipped flat_id = a deleted bone. Do not renumber to fill gaps.

### Blank numbered lines = time-skips

A line of the form `<flat_id>` (an id followed by no content) is a **time-skip marker**. It signals a non-trivial elapsed interval between the prior numbered beat and the next. The stitcher renders a paragraph-break here. Multiple consecutive blank-numbered lines are legal and indicate a longer skip.

A fully blank line (no id, no content) is decoration only and may be inserted between paragraphs of body text for human readability. The reviewers ignore fully blank lines.

### `SUBJECT VERB OBJECT` (harsh-SVO discipline)

- **One sentence, SVO order.** No fragments. No statements (declarative thought without action). No questions.
- **Subject is a named entity** — actor slug, prop slug, or `the <noun>` for unnamed environment elements. Subject MUST be singular; multi-subject (`taylor and rowan walk`) faults `FAULT-FORM-MULTI-SUBJECT`.
- **Verb is concrete and physical** — what an observer would see or hear. Internal states are facets, not bones.
- **No copulas.** `is`, `was`, `will`, `am`, `are`, `were`, `be`, `been`, `being` are banned in bones (`FAULT-FORM-COPULA`). State-of-being routes to facets.
- **No negations.** `didn't`, `does not`, `won't`, etc. are banned (`FAULT-FORM-NEGATION`). A non-event is not a bone; the bone records what *did* happen.
- **No perception verbs.** `read`, `took`, `tracked`, `noted`, `counted`, `measured`, `watches`, `sees`, `hears`, `notices` are POV-leaks; they describe internal observation, not external action (`FAULT-FORM-PERCEPTION`). Perception belongs to narrator-interest / sensory facets, which cite the physical bone that triggered them.
- **No non-action verbs.** Verbs whose primary semantic is *being* or *having* rather than *doing* are banned (`FAULT-FORM-NON-ACTION-VERB`). Non-exhaustive deny-list:
  - Possession: `has`, `had`, `have`, `having`, `owns`, `owned`, `belongs to`, `possesses`.
  - Sustained carrying: `carries`, `carried`, `carrying`, `bears`, `bore`, `wears`, `wore`, `keeps`, `kept`.
  - Containment: `contains`, `houses`, `occupies`, `inhabits`, `consists of`, `comprises`.
  - Stative position-naming: `lies`, `sits`, `stands` describing position not posture-act (`taylor stands at the door` faults; `taylor stands` as the discrete act of rising from sitting passes).
  - Disallowed `holds` uses (see narrow license below).
  Recast as the discrete act that initiated/terminated the state, or route the state to a state-update / location-state facet that cites a real action bone.
- **Narrow `holds` license.** `holds` is licensed only when (1) the object is a body part of the subject and the action is stillness-against-pressure (`taylor holds the feet`, `mira holds the eyes`), or (2) the object is a physical object resisting pressure (`the door holds` against being opened). Anything else (`taylor holds the ledger`, `the yard holds the silence`, `the wards hold their positions`) faults `FAULT-FORM-NON-ACTION-VERB`.
- **Abstraction-as-object is INTERIORITY.** A physical verb whose object is an abstract noun (`the yard holds the silence`, `taylor carries the weight`, `the room holds the tension`) is a thought-figure, not an event. Faults `FAULT-FORM-INTERIORITY`.
- **Abstraction-as-subject is REJECT (DEC-0115 / PROP-0046 / PROP-0049).** A bone whose grammatical subject is the apparatus or an abstraction rather than a concrete actor — `the count closes`, `the gap propagates`, `the node forecloses`, `the feed returns the body`, `the ledger takes the entry` — is schema-invalid. Fault: `ABSTRACTION-AS-SUBJECT-<bone>` (HARD at `/and-write` Phase 6; blocks emission). An apparatus the narrator perceives *through* (a feed, a count, a ledger, a column, an insect-network, a sense-power) is a *lens*, not a valid subject. Recast with a concrete actor: `I stop tracking him` (not `I close the count`); `the three figures step back` (not `the gap propagates`). Named environment elements (`the door`, `the wall`, `the corridor`) are concrete and permitted; process-abstractions and apparatus-concepts are not. The `the <noun>` license on line 93 extends only to concrete unnamed environment elements — it does not cover apparatus or abstraction nouns.
- **No modifiers.** No adjectives, no adverbs, no prepositional padding. Time and place go in citations to location-state, not in the bone. Prepositional phrases of place / destination / source / direction / instrument / accompaniment are explicitly banned (`FAULT-FORM-MODIFIER`). Use a transitive verb that takes the location as direct object (`taylor enters the yard`, not `taylor walks into the yard`).
- **`turns to <named entity>` is banned** as a directional-prep variant of FAULT-FORM-MODIFIER. The `to <X>` is a prepositional padding phrase, not a direct object. Recast to a transitive form: `faces <X>`, `pivots toward <X>` if motion-in-progress is required. The single exception is the dialogue form `<speaker> speaks to <listener>` which is licensed by the dialogue-beat shape, not by `turns to`.
- **Bare intransitive motion verbs without destination fault `FAULT-FORM-NO-VERB`.** `taylor moves` is not observable; `taylor enters the yard` is. The intransitive-lands-cleanly exception (`taylor exhales`) does not extend to motion verbs that imply destination.
- **No conjunctions.** No `and`, `but`, `while`, `as`. If two things happen, they are two bones (`FAULT-FORM-CONJUNCTION`).
- **No interiority.** Thought, intent, feeling, perception are facets, not bones. The bone records only the physical act (`FAULT-FORM-INTERIORITY`).
- **No compound objects.** Comma-list of objects where the verb does not act on the set as one physical event faults `FAULT-FORM-COMPOUND-OBJECTS`.

If a candidate sentence cannot be reduced to clean SVO without loss, the underlying beat is too compound. Split it.

### `[<cited-id>, ...]`

- Optional citation list at end of line, in square brackets, comma-separated.
- **Citations accrue at facet-authoring time, not at bone-extraction time.** A freshly authored bone carries no citations. As facets are authored against the bones file, citations attach back to the bones they reference.
- Each citation is a typed reference into another artifact. Format: `<artifact>:<flat_id>`.
- Recognized artifact prefixes (under the substance overhaul, `tens:` is removed — tensometer facet is dropped):
  - `loc-state` — location-state facet entry (environment / time / weather).
  - `<character-slug>` — dialogue file for that character. The cited ID is the dialogue entry within that file.
  - `aud-<persona>` — audience interest-flag file for that persona.
  - `narrator` — narrator interest-flag entries (POV character's narrator-mode output).
  - `mem` — memory-flag entry.
  - `sensory` — sensory-flag entry.
  - `feel` — feeling-flag entry.
  - `meta` — metaphor-flag entry.
  - `state` — state-update facet entry.
  - `vibes` — vibes-update facet entry.
- Citations are unordered. The stitcher reads the bone's citations as a bag of available material to consult when rendering the beat.

A bone with no citations is valid; it means the beat is bone-only and the stitcher renders it as the SVO sentence verbatim — **with one exception:** dialogue-anchor bones (see below) MUST carry `<character-slug>:<id>` citations at bones-write time. A dialogue-anchor bone with no dialogue citation is HARD `FAULT-DIALOGUE-MISSING-AT-ANCHOR` at `/and-write` Phase 6.

### Dialogue-anchor bones (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25)

A **dialogue-anchor bone** is a bone that carries spoken content. Two forms:

1. **Canonical speech form** — `<speaker-slug> speaks to <listener-slug>`. Required substance_delta: ≥1 communication/relational-class axis per the active signature (universal questionnaire: community / knowledge / reputation / trust; custom signature: the axis or axes the series.substance.state_axes block designates as relational/communicative per the signature note).
2. **Licensed action form** — a bone whose SVO is a concrete physical action AND whose `substance_delta.axis_moves[]` declares a communication-class axis movement AND whose scene chunk text licenses a speech-act at that bone (parking-lot disposition pl-2026-05-25-004 routing (a) is the canonical example: `taylor raises the voice` anchoring three utterances in c01 b01).

Dialogue-anchor bones carry `[<character-slug>:<id>, ...]` citation tokens at bones-write time (emitted by `/and-write` Phase 7 Step 3a, NOT accrued at facet-author time). These citations resolve into the per-character dialogue files at `theater/dialogue/<character-slug>.md` per `schemas/dialogue.schema.md`.

---

## Authoring rules

- **`/and-write` authors** under the substance bone-gate at Phase 6 — every bone declares an axis-movement (per-bone state-delta, stored in showrunner memory at `chapters[].scenes[].bones[].substance_delta`, NOT in this file).
- **Reviewed by the five-pass pipeline** lifted from `/and-protolines-v2`: Pass 1 inventory (now Phase 1 scene-decomposition in `/and-write`) → Pass 2 constraint audit → Pass 3 shape → Pass 4 trim → Pass 5 continuity → Phase 6 substance bone-gate (the substance overhaul's replacement for URI-026 tens-gate).
- **Per-bone state-delta lives only in showrunner memory.** This file is comment-clean — no YAML, no per-bone substance annotations, no scene markers, no facet pre-tags.

---

## What bones are not

- Not prose. Not the show file. Not stitched output.
- Not interiority. Internal states are facets that *cite* bones.
- Not dialogue. Spoken content lives in per-character dialogue files; the bone marks `<speaker> speaks to <listener>` only — no spoken content, no dialogue-id citation.

For dialogue beats, the bone shape is:
```
<flat_id> <speaker-slug> speaks to <listener-slug-or-group>
```
The dialogue file carries content + objective and cites the bone by flat_id. The bone itself does **not** carry a forward-anchor to the dialogue entry — citations accrue at facet-authoring time, not at bone extraction time. Speech bones must move at least one communication/relational-class axis per the active signature (universal questionnaire: community / knowledge / reputation / trust; custom signature: the axis or axes the series.substance.state_axes block designates as relational/communicative per the signature note) per the substance bone-gate; speech bones whose substance_delta lists only physical-action axes are malformed.
