# SVO Split — Pain Points & Open Calls

Notes captured during Phase 0 prep (splitting active s01e01–e06 show.md content into proto-line / SVO format per `schemas/proto-line.schema.md`). Rough-but-faithful pass for training-data prep; SVO extractor improvements are on the backlog.

---

## Output location

Schema `schemas/proto-line.schema.md` names a single canonical path: `active-project/theater/proto-lines.md` (one episode active at a time under shoot-v2). Active content here covers six episodes simultaneously (one current, five archived). Defensible call: per-episode files under `active-project/theater/proto-lines/<slug>.md`. Resolve at extractor-improvement time — likely the canonical path becomes a per-episode convention or the archived episodes' proto-lines move alongside their show.md into the per-episode archive dirs.

## Schema ambiguities encountered

1. **Interiority that *is* the physical act.** Paragraphs of Taylor's "passive feed" (mouse-shape steps, sparrow handoff, bird's grip telemetry) describe environment changes Taylor perceives but where the physical event is happening to other entities. Call: render as `the mouse repositions in the seam`, `the sparrow holds the rider`, etc. — physical SVO with `the <noun>` subject — and let the perception live in narrator/feel facet citations against that proto-line. Risk: under-counts Taylor's interiority work; flag for extractor improvement.
2. **Posture-holds and non-actions.** Taylor's "did not turn / did not move / chin stayed at quarter-inch" beats are dramatically load-bearing but violate "concrete and physical verb." Call: render as positive SVOs (`Taylor holds the chin angle`, `Taylor keeps the feet on the rushes`) — the holding *is* the act under pressure. Negation collapsed into hold-verbs.
3. **Compound-perception sentences.** A paragraph may say "the smear changes shape" then immediately reinterpret what that means across the next four sentences. Treated as one proto-line + facet citations, not four — a perception revision is not new physical action.
4. **Dialogue partial-syllable beats.** s01e03 has Taylor speaking across an interruption ("Since before the cold —" then later " — it comes for grain"). Rendered as two `Taylor speaks to inspector` proto-lines with the dialogue file expected to carry the split.
5. **Imagined / counterfactual content.** s01e01 NEEDS_EDIT rewrites describe Taylor *imagining* how she might have looked. Skipped — imagined frames are not physical events. Where the rewrite-note replaces actual content, the *original* prose was extracted; the bracketed rewrite-direction is metadata, not source.
6. **NEEDS_EDIT / DELETE annotations.** Bracketed editorial notes are not source content. Where a paragraph is annotated `DELETE`, the prose still exists in the show file and was extracted (rough-but-faithful). Future pass may filter against these annotations.
7. **Stitcher-only "and" in a paragraph that genuinely is multiple actions.** Paragraphs joined by "and" or "—" routinely encode 5–15 distinct beats. Split aggressively; under the schema, conjunctions are stitcher-territory.

## Pain points for the extractor backlog

- **Taylor's POV-leak verbs.** "Read," "took," "tracked," "noted," "counted," "measured" — these are perception verbs that pretend to be physical. Extractor needs a deny-list and a translation policy ("Taylor reads the inspector's stance" → drop the proto-line, make it a narrator/feel facet against the physical proto-line that the inspector executed).
- **No pre-loaded citation anchors.** *(Correction post-extraction, 2026-05-06.)* The first pass instructed extractors to insert `[loc-state:?]` placeholders on environment-change beats. Stripped after the fact: pre-seeding citations contaminates downstream facet-authoring training data — the extractor pre-decides which beats are environment-change, biasing the facet author. Bone-only is the rule; citations accrue when the facet is authored, not before. The schema-prescribed dialogue-beat citation `[<speaker>:<dialogue-id>]` was also stripped (~30 across e01–e04) and `schemas/proto-line.schema.md` was revised: dialogue beats now render as `<speaker> speaks to <listener>` with no citation, and the citation-list section now explicitly states citations accrue at facet-authoring time. **Resolved.**
- **ID stability vs. rough-pass.** This is a rough pass. If it is later refined, IDs assigned here are not promised stable until a downstream lock pass. Flag: do not treat this output as authoritative ID-keeping until the extractor is sharpened.
- **Compound sentences with semicolons / em-dashes.** The dominant Taylor chassis (per round-trip-method.md) is em-dash + semicolon-spine; these are usually genuine multi-beat compounds. Extractor should split on em-dash and semicolon by default, not preserve.
- **Subject ellipsis.** Taylor's prose drops her own subject for stretches ("turned toward the clerk and spoke the entry aloud"). Extractor must restore the subject in each proto-line (no implicit-subject continuations).

*(Notes 8–14 added during parallel extraction of s01e01–e06; numbering reconciled post-hoc.)*

8. **Repeated holds within one paragraph (s01e02).** Plumms-man explicitly *not looking back* at the grain-keeper, then a sentence later *not turning his head* toward the grain-keeper or Taylor. Per call #2 these collapse to positive holds (`plumms-man holds his head forward`), but two adjacent identical proto-lines feel redundant even though the source genuinely re-asserts the hold across two distinct moments (book-finishing vs. lane-stepping). Kept both for rough-pass faithfulness; extractor may want a "hold-merge across adjacent beats" rule, or a hold-with-cited-occasion shape.

9. **POV-character perception verbs applied to other characters' physical acts (s01e02).** P2 includes "his eye taking in the floor the way I know it looks" — Plumms-man performs the look but the sentence is shaped by Taylor's certainty about what he sees. Rendered as `plumms-man scans the granary floor` (drop Taylor's certainty into a future feel/narrator facet). Flag: the extractor may need to detect POV-shaped descriptions of other-character action and split source-of-knowledge from physical event.

10. **Spatial holds of inanimate environment ("X holds the Y configuration") (s01e02).** Used liberally (cote ledge, south-ledge cluster, granary three-week shape, bench empty shape) to render persistence-against-expectation. These are arguably location-state facets, not proto-lines — the "act" is non-change. Kept as proto-lines for now since the persistence is narratively load-bearing (the configuration is what plumms-man will write down). Likely a future rule: persistence-of-environment is a loc-state assertion, not a proto-line, unless a character interacts with it.

11. **POV-subject ellipsis on body-parts (s01e04).** Late-scene Plumm POV writes "the eye stayed," "the hand went to the satchel," "the reins came across" — body-part as grammatical subject standing in for the POV character. Call: restore the POV character as the subject (`plumm crosses the eye to ...`, `plumm reaches into the satchel`) rather than rendering as `the eye <verbs>` with no actor. Body-as-actor sentences are POV-stylistic, not literally what an observer sees.

12. **Multi-recipient address inside one quoted block (s01e04).** Plumm delivers one speech where the first sentence addresses Rowan and the next addresses Taylor inside the same paragraph. Call: split into two `<speaker> speaks to <listener>` proto-lines with separate dialogue-file IDs, one per listener — even when the source prose is one quoted block.

13. **Census/inventory speech read aloud (s01e04 B63).** Plumm recites three administrative items (inspector's report, sketch, census entry) in one quoted block as a single speech act. Treated as one `plumm speaks to taylor` proto-line; the three-item structure is dialogue-file content, not three speech-act proto-lines.

14. **Remote-recon delivered through fauna feed (s01e05).** Taylor sending a raven to the Harrenhal gatehouse and receiving structured perception of the gate-yard from the bird's perch. Call: render the remote scene as physical SVOs at the remote location (`the outer gate stands closed`, `a guardsman tilts his head up the wall`) — the bird's feed is a perception layer that lives in narrator/feel facets citing those proto-lines, not a separate proto-line class. Same logic as ambiguity #1 extended across radius. Risk: collapses the *act of sensing* (a Taylor cost-event) into one proto-line plus surrounding cost-beats; the remote-scene proto-lines lose their causal tie to Taylor's body without facets. Flag for facet pass.

15. **Role-only / unnamed minor actors at scene edges (s01e05).** Bracken-rider, the Celtigar courier, the castellan's nearer functionary, the steward, the headman, a guardsman — listed in episode-plan cast slugs but unnamed in the prose. Call: `the <role>` per schema's `the <noun>` allowance, preferring prose-level naming over episode-plan slug. Where source distinguishes (`the second rider`), kept the distinguisher. Flag: extractor should decide whether episode-plan cast slugs override prose anonymity.

**Parallel-write pain point.** Six extractors wrote to this file concurrently and each picked the next-available number from its own local view, producing three #9s and three #10s. Future tooling: either give the notes file a stable sectioned schema with append-only blocks per source slug, or coordinate appends through a single writer.

## What was *not* attempted in this pass

- No facet authoring (location-state, dialogue, narrator, feel, etc.).
- No re-stitching back to verify round-trip fidelity.
- No deletion of weak SVOs — all beats present in source were extracted, faithful to the rough-pass mandate.
- No reconciliation against episode-plan.md bullets.
