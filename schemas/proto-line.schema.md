# Proto-line Schema

The proto-line file is the SVO bone-structure of an episode (or chapter). It is authored under shoot-v2 (replaces the old `episode-plan.md` script section + `show.md`).

Schema authority: this file. shoot-v2 introduces this format. shoot-v1's episode-plan.md script bullets and show.md are deprecated and not produced under shoot-v2.

---

## File path conventions

Three conventions coexist:

- **Per-episode (default):** `active-project/theater/proto-lines/<slug>.md` (e.g. `s01e01.md`). Used by `/and-protolines-v2` against an episode-plan, and as the canonical post-split artifact emitted by `/and-season` Phase 4.
- **Per-chapter (season-scope):** `active-project/theater/proto-lines/chapter-NN.md`. Used by `/and-season` when a season is decomposed into chapter-scoped chunks (target ~100 finished lines per chapter). Each chapter has its own plan at `design/shoot-v2/season-chapters-run/chapter-NN-plan.md` (or, post-promotion, `active-project/theater/<slug>/episode-plan.md` per chapter).
- **Season aggregate (Phase 2/3 working artifact):** `active-project/theater/proto-lines/<season-slug>.aggregate.md`. Authored by `/and-season` Phase 2 as a single object covering the whole season; reviewed and revised in place during Phase 3; split into per-episode (or per-chapter) files at Phase 4. Internal sections are delimited by `# === episode: <slug> ===` (or `# === chapter: NN ===`) lines, each immediately followed by the standard `narrator:` and `goal:` headers, then the section's numbered bones starting at ID 1.

The legacy singular `active-project/theater/proto-lines.md` is no longer authored. Pre-existing files at that path remain readable but are not written.

---

## File header (required)

Every proto-line file begins with `narrator:` and `goal:` at minimum:

```
narrator: <actor-slug>
goal: <one sentence — what this chapter shows the audience>
```

Both fields are mandatory under shoot-v2. The reviewer passes (Pass 2 constraint, Pass 3 shape, Pass 4 trim, Pass 5 continuity) consume both headers:
- **narrator** — the POV character. Pass 5 enforces narrator-consistency. Lines whose content cannot be observed from this POV fault as `FAULT-POV`.
- **goal** — the per-chapter north star. Pass 4 (trim) walks the line set against this goal; lines that don't serve it are deletion candidates.

A header missing or empty faults `FAULT-HEADER-NARRATOR` or `FAULT-HEADER-GOAL` at Pass 2.

A blank line follows the header before the body begins.

### Extended header (per-episode files emitted by `/and-season` Phase 4)

Per-episode proto-line files emitted by `/and-season` Phase 4 mechanical write-out carry five additional header fields (in addition to `narrator:` and `goal:`) so the downstream `/and-shoot-v2` facet pass has the per-episode handles it needs without re-scanning the aggregate. Full header (seven fields, in order):

```
# proto-lines — <episode-slug>

episode: <episode-slug>
narrator: <pov-actor-slug>
goal: <one sentence — what this episode shows the audience>
cast: <slug>, <slug>, <slug>, ...
locations: <loc-slug>, <loc-slug>, ...
prior_episode: <previous-episode-slug | none>
aggregate_range: <from>-<to>
```

Field rules for the extended fields:

- **`episode:`** — the episode slug (matches filename). Facet authors lift verbatim into facet-file `episode:` frontmatter.
- **`cast:`** — comma-separated actor slugs that appear as a SUBJECT or as a `speaks to <listener>` listener anywhere in this episode's bones. Computed at split time via slug-grep over the episode's proto-lines (no inference, no card lookup). Order: by first-appearance ID. Listener-only slugs included plain (no suffix).
- **`locations:`** — comma-separated location slugs that the studio fork must load to author location-state. Computed via slug-grep over proto-line OBJECTs/SUBJECTs and resolved against the active warehouse's loc cards.
- **`prior_episode:`** — slug of the previous episode in season order, or `none` for e01. Consumed by `/and-shoot-v2` Phase 0 to know which prior-episode state files to snapshot for handoff baseline.
- **`aggregate_range:`** — the contiguous aggregate-id range covered by this episode (e.g. `1-87`). Replaces per-line `# aggregate-id:` comments. Computed from the Phase 4 Step 3.2 renumbering.

**Authority:** these fields are required when the file is emitted by `/and-season` Phase 4 (the validator at Phase 4 Step 3 enforces them). They are **optional** for ad-hoc per-episode files authored via `/and-protolines-v2` (those files don't go through facet authoring without an `/and-shoot-v2` dispatch that supplies the missing context separately).

**Per-line `# aggregate-id:` comments are not authored.** The per-episode body remains comment-clean per the no-decoration rule (POV markers excepted; copied through from the aggregate). Fixers route faults back to the aggregate by computing `aggregate_id = aggregate_range_start + episode_id - 1`.

---

## Body format

Plain text, newline-separated entries. One proto-line per line. No section headers, no scene markers, no markdown bullets.

```
<id> SUBJECT VERB OBJECT [<cited-id>, <cited-id>, ...]
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

### `<id>`

- Monotonic positive integer, file-scoped. Starts at 1.
- **Stable** — once assigned, never reused, never reassigned. Re-ordering preserves IDs; the stitcher walks IDs in citation order, not numeric order.
- Deletions leave the ID gap visible. A skipped ID = a deleted proto-line. Do not renumber to fill gaps.
- Implementation may promote to scoped (`s1.42`) only if collisions become a problem at scale. Default flat.

### Blank numbered lines = time-skips

A line of the form `<id>` (an id followed by no content) is a **time-skip marker**. It signals a non-trivial elapsed interval between the prior numbered beat and the next. The stitcher renders a chapter-break or paragraph-break here. Multiple consecutive blank-numbered lines are legal and indicate a longer skip.

A fully blank line (no id, no content) is decoration only and may be inserted between paragraphs of body text for human readability. The reviewers ignore fully blank lines.

### `SUBJECT VERB OBJECT` (harsh-SVO discipline)

- **One sentence, SVO order.** No fragments. No statements (declarative thought without action). No questions.
- **Subject is a named entity** — actor slug, prop slug, or `the <noun>` for unnamed environment elements. Subject MUST be singular; multi-subject (`taylor and rowan walk`) faults `FAULT-FORM-MULTI-SUBJECT`.
- **Verb is concrete and physical** — what an observer would see or hear. Internal states are facets, not proto-lines.
- **No copulas.** `is`, `was`, `will`, `am`, `are`, `were`, `be`, `been`, `being` are banned in proto-lines (`FAULT-FORM-COPULA`). State-of-being routes to facets.
- **No negations.** `didn't`, `does not`, `won't`, etc. are banned (`FAULT-FORM-NEGATION`). A non-event is not a proto-line; the proto-line records what *did* happen.
- **No perception verbs.** `read`, `took`, `tracked`, `noted`, `counted`, `measured`, `watches`, `sees`, `hears`, `notices` are POV-leaks; they describe internal observation, not external action (`FAULT-FORM-PERCEPTION`). Perception belongs to narrator-interest / sensory facets, which cite the physical proto-line that triggered them.
- **No non-action verbs.** Verbs whose primary semantic is *being* or *having* rather than *doing* are banned (`FAULT-FORM-NON-ACTION-VERB`). Non-exhaustive deny-list:
  - Possession: `has`, `had`, `have`, `having`, `owns`, `owned`, `belongs to`, `possesses`.
  - Sustained carrying: `carries`, `carried`, `carrying`, `bears`, `bore`, `wears`, `wore`, `keeps`, `kept`.
  - Containment: `contains`, `houses`, `occupies`, `inhabits`, `consists of`, `comprises`.
  - Stative position-naming: `lies`, `sits`, `stands` describing position not posture-act (`taylor stands at the door` faults; `taylor stands` as the discrete act of rising from sitting passes).
  - Disallowed `holds` uses (see narrow license below).
  Recast as the discrete act that initiated/terminated the state, or route the state to a state-update / location-state facet that cites a real action proto-line.
- **Narrow `holds` license.** `holds` is licensed only when (1) the object is a body part of the subject and the action is stillness-against-pressure (`taylor holds the feet`, `mira holds the eyes`), or (2) the object is a physical object resisting pressure (`the door holds` against being opened). Anything else (`taylor holds the ledger`, `the yard holds the silence`, `the wards hold their positions`) faults `FAULT-FORM-NON-ACTION-VERB`.
- **Abstraction-as-object is INTERIORITY.** A physical verb whose object is an abstract noun (`the yard holds the silence`, `taylor carries the weight`, `the room holds the tension`) is a thought-figure, not an event. Faults `FAULT-FORM-INTERIORITY`.
- **No modifiers.** No adjectives, no adverbs, no prepositional padding. Time and place go in citations to location-state, not in the proto-line. Prepositional phrases of place / destination / source / direction / instrument / accompaniment are explicitly banned (`FAULT-FORM-MODIFIER`). Use a transitive verb that takes the location as direct object (`taylor enters the yard`, not `taylor walks into the yard`).
- **`turns to <named entity>` is banned** as a directional-prep variant of FAULT-FORM-MODIFIER. The `to <X>` is a prepositional padding phrase, not a direct object. Recast to a transitive form: `faces <X>`, `pivots toward <X>` if motion-in-progress is required, or `swings the head` (intransitive) if the orientation target is unstated. Ruling established 2026-05-07b after fixer drift surfaced; consistent with the original Pass 1 brief intent. The single exception is the dialogue form `<speaker> speaks to <listener>` which is licensed by the dialogue-beat shape, not by `turns to`.
- **Bare intransitive motion verbs without destination fault `FAULT-FORM-NO-VERB`.** `taylor moves` is not observable; `taylor enters the yard` is. The intransitive-lands-cleanly exception (`taylor exhales`) does not extend to motion verbs that imply destination.
- **No conjunctions.** No `and`, `but`, `while`, `as`. If two things happen, they are two proto-lines (`FAULT-FORM-CONJUNCTION`).
- **No interiority.** Thought, intent, feeling, perception are facets, not proto-lines. The proto-line records only the physical act (`FAULT-FORM-INTERIORITY`).
- **No compound objects.** Comma-list of objects where the verb does not act on the set as one physical event faults `FAULT-FORM-COMPOUND-OBJECTS`.

If a candidate sentence cannot be reduced to clean SVO without loss, the underlying beat is too compound. Split it.

### `[<cited-id>, ...]`

- Optional citation list at end of line, in square brackets, comma-separated.
- **Citations accrue at facet-authoring time, not at proto-line extraction time.** A freshly authored or freshly extracted proto-line carries no citations. As facets are authored against the proto-line file, citations attach back to the proto-lines they reference. Pre-seeding citation anchors (`[loc-state:?]`, `[<speaker>:?]`, etc.) at extraction time contaminates downstream facet-authoring training data and is not allowed.
- Each citation is a typed reference into another shoot-v2 artifact. Format: `<artifact>:<id>`.
- Recognized artifact prefixes:
  - `loc-state` — location-state facet entry (environment / time / weather).
  - `<character-slug>` — dialogue file for that character. The cited ID is the dialogue entry within that file.
  - `tens` — tensometer entry.
  - `aud-<persona>` — audience interest-flag file for that persona.
  - `narrator` — narrator interest-flag entries (POV character's narrator-mode output).
  - `mem` — memory-flag entry.
  - `sensory` — sensory-flag entry (formerly `loud`).
  - `feel` — feeling-flag entry.
  - `meta` — metaphor-flag entry.
  - `state` — state-update facet entry.
  - `vibes` — vibes-update facet entry.
- Citations are unordered. The stitcher reads the proto-line's citations as a bag of available material to consult when rendering the beat.

A proto-line with no citations is valid; it means the beat is bone-only and the stitcher renders it as the SVO sentence verbatim (with at most "and" connectives if joining adjacent proto-lines).

---

## Authoring rules

- **Screen-writer authors** under the locked Pass 1 brief (`design/shoot-v2/svo-writer-pass1-brief.md`).
- **Reviewed by the five-pass pipeline** (`/and-protolines`): Pass 1 inventory → Pass 2 constraint audit → Pass 3 shape (dramatist) → Pass 4 trim (audience ×3) → Pass 5 continuity (auditor #2 fresh fork). At season scope, an additional nine-pass review (S1–S9) runs through `/and-season` after all chapters individually converge.
- **Edits delete-only after lock.** Once cross-facet consistency runs, proto-lines may only be deleted, not rewritten. A new beat = a new proto-line with a new ID.

---

## What proto-lines are not

- Not prose. Not the show file. Not stitched output.
- Not interiority. Internal states are facets that *cite* proto-lines.
- Not dialogue. Spoken content lives in per-character dialogue files; the proto-line marks `<speaker> speaks to <listener>` only — no spoken content, no dialogue-id citation.

For dialogue beats, the proto-line shape is:
```
<id> <speaker-slug> speaks to <listener-slug-or-group>
```
The dialogue file carries content + objective and cites the proto-line by id. The proto-line itself does **not** carry a forward-anchor to the dialogue entry — citations accrue at facet-authoring time, not at proto-line extraction time. Bone-only is the rule (revised 2026-05-06; prior version of this schema prescribed `[<speaker-slug>:<dialogue-id>]` on the proto-line, which contaminated facet-authoring training data).
