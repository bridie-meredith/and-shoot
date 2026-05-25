# Dialogue Schema

Per-character dialogue files. One file per speaking character per chapter. Authored by the dialogue-writer fork dispatched from `/and-write` Phase 1.5 (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25) and co-emitted with the bones file at `/and-write` Phase 7. Pre-2026-05-25 the author dispatch lived at `/and-facets` Phase 1; that authoring step is retired. The R2 dialogue judge at `/and-facets` Phase 2 remains as a locked-graph review pass (KEEP / DELETE / REWRITE against the facet graph the upstream author was blind to) — review only, no authoring.

Path: `active-project/theater/dialogue/<character-slug>.md`

---

## Format

Plain text. Newline-separated entries with a frontmatter header.

```
character: <slug>
episode: <slug>
behavior-card: <dialect-card-slug>
---
<id> @<proto-line-id> | <objective> | <utterance>
<id> @<proto-line-id> | <objective> | <utterance>
...
```

### Header fields

- **`character:`** — actor slug. Matches the filename and the speaker in cited proto-lines.
- **`episode:`** — episode slug for traceability.
- **`behavior-card:`** — slug of the behavior card consulted by the writer fork. Recorded so review can verify the right voice/tic/monument anchor was loaded. Multi-card composition (per-character + shared region/class/period overlays) lists the per-character card here; the writer fork resolves `inherits:` and `references:` from there.

### Entry fields

```
<id> @<proto-line-id> | <objective> | <utterance>
```

- **`<id>`** — monotonic positive integer, **scoped to this character file**. Starts at 1 in each character's dialogue file. The full citable identifier from a proto-line is `<character-slug>:<id>`.
- **`@<proto-line-id>`** — anchor proto-line ID. The proto-line where this speech act lives. Required; an utterance with no anchor is unmoored. One proto-line may have multiple dialogue entries (multi-utterance exchange) — they share the same anchor.
- **`<objective>`** — one short clause stating what the speaker is trying to accomplish with this utterance. Carried from coach prompt's objective list. Used by audience review to check whether the utterance lands the objective.
- **`<utterance>`** — the spoken content. Verbatim, written in voice. Single line; multi-sentence utterances stay on one line (split into multiple entries if rhythm demands separation).

---

## Authoring

- **Writer:** fork-spawned dialogue-writer dispatched from `/and-write` Phase 1.5 (URI-WRITE-DIALOGUE-COBONDED). One fork per behavior card; each fork authors all speakers sharing that card. Fork loads behavior card stack (margit-composed: leaf → inherits → universal overlay → references), speaker persona + ltm + stm + state for every speaker the fork covers, the dialogue-anchor bone list with substance_delta + scene_conflict, `staff/dialogue-writer/rubric-dialogue.md`, and this schema. Blind to facet content (none exist yet at Phase 1.5). Writes the file(s) in one hermetic run; discarded.
- **Review:** audience critics + constraint pass, after the fork returns. Reviews operate on the file as a unit, not per-entry.
- **Edits:** during review, deletions are preferred over rewrites. If a rewrite is needed, the entry is deleted and a new entry with a new ID replaces it. IDs are stable per the same rules as proto-lines.

---

## Ordering

Dialogue entries within a character file are written in **screen-time order** (the order the character speaks across the episode), but the stitcher reassembles by anchor proto-line ID, not by file order. The screen-time order in the file is for the writer's coherence; the citation graph is what drives stitch.

---

## Stitch interface

The stitcher reads proto-lines in citation order. For each proto-line with a `<character-slug>:<id>` citation, the stitcher fetches that dialogue entry and includes the utterance verbatim. Per the stitcher edit budget (only "and"), the utterance is not rewritten. Attribution ("she said," "he answered") is generated only as connective tissue — and even attribution is constrained: the stitcher may use the literal speaker slug (resolved to a name via persona card) and the behavior card's preferred attribution patterns, but may not invent dialogue tags with new verbs.

If a proto-line cites a dialogue entry that does not exist (deleted, never authored), the stitcher flags the gap for re-author. It does not paper over.

---

## Example

```
character: taylor-hebert-westeros
episode: s01e01
behavior-card: taylor-hebert-westeros-narration
---
1 @14 | deflect the clerk's question | "I'm passing through."
2 @14 | imply she has business elsewhere | "There's a road north of here, isn't there?"
3 @19 | warn Mira off without being seen warning her | "Wait."
```

The proto-line at ID 14 reads (e.g.):
```
14 taylor speaks to clerk [taylor-hebert-westeros:1, taylor-hebert-westeros:2]
```

Citation graph: proto-line 14 → dialogue entries 1 and 2 in `taylor-hebert-westeros.md`. Stitcher renders both utterances under proto-line 14's beat in the order the citations list them.
