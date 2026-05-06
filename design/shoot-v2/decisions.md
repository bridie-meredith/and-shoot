# Decisions

Resolutions to open questions, in order received. User's call unless marked **(claude default)** — those are committed defaults that the user can override at any time.

## 2026-05-06 — first batch (user)

### Proto-line file format

Newline-separated entries. Each entry: `<id-number> SUBJECT VERB OBJECT [<cited-id>, <cited-id>, ...]`.

- One sentence, SVO. No fragments, modifiers, statements.
- Cited IDs in square brackets at end. Citations point at facet entries and dialogue entries.
- ID numbers are stable and survive re-ordering.

### Facet file format

Newline-separated entries. Each entry: `<id-number> <content>` after a bullet point.

- One file per facet type (one tensometer file, one memory-flag file, etc.) — keeps each facet's review scope tight.
- Content shape varies by facet (scalar for tensometer, free text for metaphor flags, structured delta for state updates), but the line-level format is uniform: `<id> <content>`.

### Review order — per-file cull before cross-facet consistency

Each independent file is audited first to delete boring / inane / weak content. This per-file cull happens before the holistic cross-facet drift check, so the drift check operates on smaller, already-pruned inputs.

### Behavior cards — new card type, new library section (originally "dialect", expanded 2026-05-06)

A new card class carries direct voice samples, **non-verbal tics**, and **memory-monument register** per character or per shared period × region × class. Originally scoped as "dialect"; expanded on 2026-05-06 to a behavior card after observation that verbal register alone undersells the load — tics and monument-handling are equally load-bearing.

Lives at `cards/dialects/` (directory rename to `cards/behaviors/` pending). Tied to critic (audience), constraint pass (auditor), coach, and the dialogue-writer (see below). Adds a fifth card class (`behavior`) to `schemas/card.schema.md`; margit validates same as today.

Subclasses: `shared-behavior` (period × region × class pattern bank, no `character:` field) and `per-character-behavior` (one specific speaker, `character:` required).

### Actor memory — unchanged shape, batched updates

Existing actor memory (ltm/stm/state) stays as-is structurally. Updates batched, not line-by-line. Source: state-update facet entries, applied by showrunner at the phase boundary noted below.

### Stitching — Opus agent, cherry-pick, minimal edit

Stitching is generative. A dedicated Opus agent reads proto-lines + dialogue + facets, cherry-picks the best material (most entertaining, most relevant, most dramatic), and assembles with minimal editing of stitched material. Voice quality is sourced from dialogue artifacts; the stitcher selects and arranges, never rewrites voice.

---

## 2026-05-06 — second batch

### Dialogue source: forked dialogue-writer (user direction + claude default)

Dialogue is authored by a **fork of the orchestrator** — context isolated, results returned, fork discarded. **Flushable at end of run.** No persistent agent home, no carried context between invocations.

- **Spawn pattern:** one fork per character per episode. Same shape as auditor today (fork → bundle → return → discard).
- **Context bundle (loaded fresh into the fork):** character card + ltm + stm + state + **behavior card stack** + coach prompt. The behavior stack is the per-character behavior card with all `inherits:` and `references:` cards resolved (universal mannerisms + region + class + per-character). Loader: margit, on fork-spawn request. The stack is composed in load order (universal → region → class → per-character) and the fork sees it as a single concatenated context section. Coach prompt carries bullet intent for every speaking beat the character has across the episode: who-speaks-to-whom, content list, objective list, anchor proto-line IDs.
- **Output:** the character's dialogue file (`active-project/theater/dialogue/<character-slug>.md`), authored in one sitting across all the character's screen time for the episode.
- **Reviewed by:** audience critics + constraint pass, run *after* the fork returns and writes.
- **Why a fork, not a persistent agent:** flushability. The dialogue-writer should not accumulate context across episodes or characters. Each run is hermetic — load context, author, write, discard. Mirrors the auditor pattern that the codebase already uses.
- **Why not impersonator:** brainstorm rejected immersed impersonators. The fork-writer treats voice as a *target*, not a *self*, and authors across the whole episode in one sitting.
- **Why not coach:** coach is a translator (bullet → prompt). Making coach a generator is role drift.

Open implementation question (deferred to implementation phase): the existing impersonator agent likely retires. Whether the fork-writer also handles narrator-flags / feeling-flags facets for that character (single fork, multiple outputs) or whether each facet gets its own fork is an implementation choice. The flushable principle holds either way.

### Proto-line ID scheme (claude default)

Flat monotonic integers, episode-scoped. `1`, `2`, `3`, ... — no scene prefix. Re-ordering preserves IDs; stitcher walks IDs in citation order, not numeric order. Promote to scoped (`s1.42`) only if collisions become a problem at scale.

### STUDIO bullets become a location-state facet (claude default)

Environment narration is its own facet file (`location-state.md` or similar). Studio agent authors it; same `<id> <content>` format as other facets. Proto-lines cite location-state IDs when the environment is load-bearing for the action.

### Dialogue file shape (claude default)

One file per character per episode: `active-project/theater/dialogue/<character-slug>.md`. ID space is per-character — entries cited from proto-lines as `<character-slug>:<id>`. Each dialogue entry includes its anchor proto-line ID so scene order is recoverable when the stitcher reassembles.

### Behavior cards (claude default; expanded 2026-05-06)

- **Path:** `cards/dialects/<character-slug>.card.md` (directory rename to `cards/behaviors/` pending). Flat directory with `INDEX.md`, same convention as other card classes.
- **Schema sections:**
  - Frontmatter: name, world, optional `character:` (required for per-character subclass), optional `inherits:` field for a parent shared card, optional `period:` / `region:` / `social-class:` axes, optional `references:` list for additional composition.
  - **Direct samples** — verbatim quotes from source material or prior episodes. Load-bearing; a behavior card with no samples is incomplete.
  - **Cadence** — rhythm / sentence-length / pause patterns.
  - **Vocabulary** — signature words; forbidden words.
  - **Syntax** — sentence-shape patterns (subordination habits, fragments, parallelism).
  - **Voice tells** — interiority cues for POV/narrator use.
  - **Non-verbal tics** — physical and behavioral patterns (posture, gesture, eye-line, the things the body does at moments of stress, comfort, formality). Studio and impersonator deploy these; the dialogue-writer fork should not write them into the spoken-line file. Listed on the behavior card so behavior is fully described and reviewers can audit against them.
  - **Memory monuments** — shared events, traumas, and cultural anchors that weigh on the speaker's mind whether named or not. Per-region cards describe the *register-around* the monument; structural cards for the monuments themselves live at `cards/conditions/memory-monuments/` (pending). Monuments produce both speech rules (how the speaker invokes / refuses to invoke them) and behavior rules (what triggers when adjacent).
- **Granularity:** one per-character card per character. Shared cards along period × region × class axes referenced via `inherits:` (one parent) and `references:` (additional composition).
- **Validation:** margit, same as other classes. `schemas/card.schema.md` carries the fifth class section.

### Behavior card loading and review (claude default, 2026-05-06)

- **Speaker (dialogue-writer fork):** receives the per-character behavior card slug. Margit resolves the composition stack (`inherits:` parent + `references:` cards + recursive parents up the tree, capped at depth 2 for now) and loads the full stack into the fork's context. Fork sees the stack as ordered text — universal overlays first, region next, class next, per-character last — so the per-character voice is the most-recent context the model attends to.
- **Reviewer (auditor — constraint pass):** the constraint pass reads the same behavior card stack. Auditor's behavior-correctness check evaluates the dialogue file against (a) the direct samples and patterns, (b) the non-verbal tics referenced in studio's location-state and feeling-flag files, (c) the memory-monument register — flags any spoken line that names a monument the role cannot have, or that fails to weight a monument the role would carry.
- **Reviewer (audience):** the audience reviews dialogue for *entertainment* (does this land for the reader-surrogate persona). Audience does NOT replicate the auditor's voice-correctness pass; that is owned by auditor with the behavior card as authority. Audience may incidentally flag voice issues but is not load-bearing for them.
- **Coach** does not load the behavior card stack. Coach is a translator (bullet → prompt); the behavior card is the writer's anchor, not the coach's.
- **Margit** is the loader. New responsibility: resolve a behavior card slug into a full composition stack, ordered, with frontmatter merged and body sections concatenated in load order. Pre-existing override-merge logic (project cards over library cards) is the closest precedent.

### Facet authorship mapping (claude default)

| Facet | Author |
|-------|--------|
| tensometer | dramatist (single rater pass over proto-lines) |
| interest flags (audience) | audience personas, one file per persona |
| interest flags (narrator) | dialogue-writer for the POV character (interiority output mode) |
| memory flags | dialogue-writer for the POV character |
| loudness flags | studio (extends location-state authorship) |
| feeling flags | dialogue-writer for each non-POV character on screen |
| metaphor flags | editor (taste call; sparse by design) |
| state updates | studio (environment) + dialogue-writer (per-character actor state) |
| vibes updates | showrunner (cross-cutting) |

The dialogue-writer thus authors three artifact types per character: dialogue, narrator-flags-if-POV, feeling-flags-if-on-screen. Single context load, multiple outputs.

### Per-file cull (claude default)

Single delete-only pass per file, run by the same agent class that authored it. Audience persona culls its own interest-flag file; dramatist culls tensometer; studio culls location-state and loudness; dialogue-writer culls each of its three outputs per character. Convergence: one pass. If the author can't cull boring/inane/weak content in one pass, the authoring stage failed and re-runs.

### Cross-facet contradictions (claude default)

When two entries contradict (e.g. two state updates for the same beat): **delete both, flag for re-author.** Do not pick a winner. Re-author goes back to the originating agent.

### Stitcher selection signals + edit budget + gap handling (user direction)

- **Selection signals (claude default):** high tensometer (≥2) + audience-interest density (cited by ≥2 audience personas) + memory-flag presence + constraint compliance + dramatic-arc fit. Stitcher prefers content that scores on multiple signals.
- **Edit budget:** **absolutely no new words besides "and."** No "then," "so," "while," "but." No pronoun resolution. No tense-agreement rewrites. No scene generation. No voice rewriting. The stitcher's only generative power is inserting the literal word "and" as connective tissue.
- **Gap handling:** if material can't be assembled with selected proto-lines + dialogue + facets joined only by "and," the gap is flagged for re-author upstream. Stitcher does not paper over.
- **Failure-mode prevention:** the "and only" rule is the structural bet against re-introducing line-time-voice failure. It pushes pressure backwards onto the proto-line and dialogue authors — they must produce material that *can* be assembled this thinly. If they can't, the redesign exposes that early instead of letting the stitcher silently rewrite to cover.

### Memory write-back (claude default)

Showrunner applies state-update and vibes-update facets to actor `state.md` / studio `state.md` / vibe-clouds at the phase boundary **between cross-facet consistency and stitch.** Stitcher reads canonical state, never the raw facet entries.

### Multi-pass proto-line review default order (claude default)

1. delete-pass (cut weak SVOs)
2. re-arrange-pass (sequence)
3. constraint-check (world / character / continuity)
4. behavior-check (does each subject act in-character)
5. entertainment-check (audience persona pass)

Three (delete, constraint, entertainment) may repeat if a downstream pass introduces material change. Two clean consecutive passes terminates the phase.

### Migration (claude default)

- **s01e06:** convert existing shoot-v1 bullets to proto-lines as the conversion exercise. The conversion itself dogfoods whether shoot-v1 plans survive translation.
- **s01e01 re-shoot:** yes. Same scene, shoot-v2 path, direct A/B against the audience-flagged shoot-v1 output.
- **Eval metric:** audience flag density on the first ~50 lines, both renders. Shoot-v2 must materially reduce flag density on Taylor's voice specifically.
