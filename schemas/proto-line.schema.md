# Proto-line Schema

The proto-line file is the SVO bone-structure of an episode. It lives at `active-project/theater/proto-lines.md` and is authored under shoot-v2 (replaces the old `episode-plan.md` script section + `show.md`).

Schema authority: this file. shoot-v2 introduces this format. shoot-v1's episode-plan.md script bullets and show.md are deprecated and not produced under shoot-v2.

---

## Format

Plain text, newline-separated entries. One proto-line per line. No section headers, no scene markers, no markdown bullets.

```
<id> SUBJECT VERB OBJECT [<cited-id>, <cited-id>, ...]
```

Example:
```
1 Taylor crosses the muck square
2 Taylor reaches the cart [loc-state:3]
3 Mira sets the bucket on flagstone [loc-state:4, taylor-hebert-westeros:1]
4 Edric scans the road [feeling-flags:7]
5 The clerk produces a parchment [loc-state:5]
```

---

## Field rules

### `<id>`

- Monotonic positive integer, episode-scoped. Starts at 1.
- **Stable** — once assigned, never reused, never reassigned. Re-ordering preserves IDs; the stitcher walks IDs in citation order, not numeric order.
- Deletions leave the ID gap visible. A skipped ID = a deleted proto-line. Do not renumber to fill gaps.
- Implementation may promote to scoped (`s1.42`) only if collisions become a problem at scale. Default flat.

### `SUBJECT VERB OBJECT`

- **One sentence, SVO order.** No fragments. No statements (declarative thought without action). No questions.
- **Subject is a named entity** — actor slug, prop slug, or `the <noun>` for unnamed environment elements.
- **Verb is concrete and physical** — what an observer would see or hear. Not "feels," "wonders," "considers." Internal states are facets, not proto-lines.
- **Object is named or quantified** — the thing the verb acts upon. May be omitted only for intransitive verbs that land cleanly without one (e.g. `Taylor exhales`).
- **No modifiers.** No adjectives, no adverbs, no prepositional padding. Time and place go in citations to location-state, not in the proto-line.
- **No conjunctions.** No "and," "but," "while," "as." If two things happen, they are two proto-lines. The stitcher inserts "and" if joining is wanted; that is the stitcher's only generative power.
- **No interiority.** Thought, intent, feeling, perception are facets. The proto-line records only the physical act.

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
  - `loud` — loudness-flag entry.
  - `feel` — feeling-flag entry.
  - `meta` — metaphor-flag entry.
  - `state` — state-update facet entry.
  - `vibes` — vibes-update facet entry.
- Citations are unordered. The stitcher reads the proto-line's citations as a bag of available material to consult when rendering the beat.

A proto-line with no citations is valid; it means the beat is bone-only and the stitcher renders it as the SVO sentence verbatim (with at most "and" connectives if joining adjacent proto-lines).

---

## Authoring rules

- **Screen-writer authors.** Same agent as today; new constraint set (SVO, no modifiers).
- **Reviewed by audience and dramatist** in the proto-line review phase (multi-pass: delete / re-arrange / constraint-check / behavior-check / entertainment-check). See `/and-protolines` command.
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
