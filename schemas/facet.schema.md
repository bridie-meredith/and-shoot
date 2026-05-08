# Facet Schema

Facets are independent citable artifacts that decorate proto-lines with one specific kind of information per file. Authored independently, reviewed independently, culled independently. Read by the stitcher as a citation graph.

Path: `active-project/theater/facets/<facet-type>.md`

---

## Uniform line shape

Every facet file uses the same line shape, regardless of facet type:

```
<id> @<proto-line-id> <content>
```

- **`<id>`** — monotonic positive integer, scoped per facet file. Starts at 1 in each file.
- **`@<proto-line-id>`** — required anchor. The proto-line this facet entry decorates. Multiple facet entries may share the same anchor (e.g. several audience interest flags on the same beat).
- **`<content>`** — facet-type-specific. See per-type rules below.

Header (frontmatter) optional but recommended for traceability:

```
facet: <type>
episode: <slug>
author: <agent-slug>
---
```

---

## Facet types and content shape

### tensometer (`facets/tensometer.md`)

Tension scalar per proto-line, scale 1–3.

```
<id> @<proto-line-id> <1|2|3>
```

- 1 — quiet; ambient or transitional.
- 2 — pressure; stakes visible, escalation possible.
- 3 — peak; rupture, crisis, or held-breath threshold.

**Author:** dramatist (single rater pass).

---

### interest flags — audience (`facets/interest-aud-<persona>.md`)

One file per audience persona. Free-text content describing what catches that persona's attention at the proto-line.

```
<id> @<proto-line-id> <one-clause description of what is interesting to this persona>
```

**Author:** the named audience persona.

---

### interest flags — narrator (`facets/interest-narrator.md`)

What the POV character (the narrator) notices and registers. Free-text content. May be silent on proto-lines the narrator does not perceive.

```
<id> @<proto-line-id> <one-clause description of what the narrator registers>
```

**Author:** dialogue-writer fork for the POV character (interiority output mode of the same fork that writes that character's dialogue).

---

### memory flags (`facets/memory.md`)

Where the narrator (or any actor) has a call-back to prior story content.

```
<id> @<proto-line-id> <one-clause description of the callback> -> <target reference>
```

The target reference may be a prior episode's proto-line ID, a card slug (e.g. `cond-fauna-control-rules`), or a free-text gloss when no formal target exists yet.

**Author:** dialogue-writer fork for the POV character.

---

### sensory flags (`facets/sensory.md`)

Cross-modal sensory inflections — discrete perceptual deltas the proto-line language does not self-carry. Sparse and frugal — only at inflection points where the audience needs the flag to land the perception.

```
<id> @<proto-line-id> <modality>: <old-state> -> <new-state>
```

`<modality>` is one of: `sound | light | smell | thermal | humidity | pressure | tactile`. Optional `# tag: <up|down|spike|drop>` annotation may follow the delta for inflection-class shorthand.

The disambiguation gate: fire where the proto-line word is *bare* (e.g., "wind" needs flagging to convey "blistering wind"); refuse where the proto-line word is *charged* and self-carries (e.g., "thunder", "shadow", "stench" — flagging is redundant). Per-scene cap ≤ 3; sparsity 3-6%; modality-coverage ≥2 per episode (per-season ≥3).

**Author:** studio.

(Previous loudness-only definition deprecated 2026-05-07 with sensory-flags facet tuning. See `design/shoot-v2/sensory-tuning-package.md`.)

---

### feeling flags (`facets/feeling.md`)

What a character (POV or non-POV) **shows** through a somatic tell — body, gesture, posture, breath, gaze — when the audience cannot read the interior from the proto-line + already-cited facets alone. The somatic tell is the entry; the named feeling is forbidden in description.

```
<id> @<proto-line-id> <character-slug>: <somatic-tell-one-clause> | expressed: <yes|partial|no>
```

`expressed:` denotes whether the in-scene audience reads the tell — `yes` (visible to others present), `partial` (visible to attentive observer), `no` (interior-only; reader sees, in-scene characters miss).

Forbidden: named-feeling vocabulary, `feels` verb, hedges (`like` / `as if` / `kind of` / `almost`), similes, comparisons, idioms-for-feeling, original-figure metaphors, synonym-ladder evasion. Body register only; the action is what it is, not what it resembles.

Per-character per-scene cap ≤1 (hard). Sparsity 2-5%. Multi-justification ≥3 of 5 (somatic-tell-card-match + Q1-audience-cannot-otherwise-read + Q2-meaningful + scene-eligible + functional-register ≥2 of 4 from {realization / grim humor / social commentary / painting characterization}).

**Author:** dialogue-writer fork per character (POV and non-POV both eligible). Each fork authors only its own character's feelings.

(Previous non-POV-only + named-feeling content shape deprecated 2026-05-07 with feeling-flags facet tuning. See `design/shoot-v2/feeling-tuning-package.md`.)

---

### metaphor flags (`facets/metaphor.md`)

Comparisons, similes, allegories. Sparse by design — fires only when licensed by a memory or feeling anchor, in callback or dark-humor register. Reading A scope: **explicit comparisons only** (similes, predicative metaphors, single-anchor allegories). Idioms, environmental-agency personifications, and figurative-compression-without-comparator are out of scope.

```
<id> @<proto-line-id> <kind>: <text> | licensed-by: <anchor> [+<support> ...]
```

`<kind>` is one of `metaphor | simile | allegory`. `<anchor>` is exactly one of `memory:<id>` or `feeling:<id>` (mandatory). `<support>` is zero-or-more of `tens:<reading>` | `sensory:<id>` | `ni:<id>` | the other anchor type. Multi-justification requires ≥2 layers from `{memory, feeling, tens}`; anchor counts as one.

Per-scene cap ≤1 cross-character. Sparsity 0-3% (zero-fires-per-episode acceptable). Functional registers: callback OR dark-humor (other registers refused). Hard fences absolute (no Earth-Bet proper nouns; AP5 is a label-fence, not a figure-fence — Earth-Bet monument resonance carried through structural figure is the intended doubled-register mechanism). Allegory single-anchor only (multi-beat allegory collapses to strongest beat or refuses). Audience-meaningful inherited transitively from the cited memory or feeling anchor.

**Author:** editor (taste call; refuse-by-default). Author-time hard cull + cross-facet hardest cull (delete-only).

(Previous schema-current shape `<metaphor / simile / allegory>: <text>` without explicit `licensed-by:` field deprecated 2026-05-07 with metaphor-flags facet tuning. See `design/shoot-v2/metaphor-tuning-package.md`.)

---

### state updates (`facets/state-updates.md`)

Where state changes — actor state, location state, prop state. Source for batched memory write-back at the end of cross-facet consistency.

```
<id> @<proto-line-id> <target>.<field>: <old> -> <new>
```

`<target>` is `actor:<slug>` / `studio` / `prop:<slug>`. Showrunner applies these to canonical state files at the phase boundary between cross-facet consistency and stitch.

**Author:** studio (environment / location / prop) and dialogue-writer fork (per-character actor state).

---

### vibes updates (`facets/vibes.md`)

Persistent operator-bias tags that stick to entities (actors, locations, props) or scopes (episode / season / series). Each vibe is a `keyword: [token-bundle]` — keyword indexes; tokens are word-algebra read by downstream operators (dialogue-writer, studio, NI, feeling, metaphor, behavior-pack). Vibes are **read** by operators before generation; they are **never rendered as prose**. They bias the writer; they do not appear on the page.

```
<id> [@<proto-line-id>] <target> <op> <keyword>: [<token>, <token>, ...] | licensed-by: <source>[, <source>...]
```

- `[@<proto-line-id>]` — **optional** anchor. Required when licensed by an on-screen beat; omitted when licensed by off-screen / pre-episode / inter-episode reflective context.
- `<target>` — `actor:<slug>` | `loc:<slug>` | `prop:<slug>` | `episode` | `season` | `series`. Entity targets are primary; scope targets reserve for ambient atmosphere not entity-bound.
- `<op>` — `+` (add new keyword to target's vibe-set; token-bundle required) | `-` (retire keyword; token-bundle omitted) | `++` (extend tokens for an existing keyword; token-bundle required, must not duplicate existing tokens by string match). No `=` op.
- `<keyword>` — hyphenated index handle. Semantic. One per vibe.
- `<token>` — hyphenated word-algebra phrase, comma-separated within `[...]`. No prose, no sentences. Sentence-parsability test: a token is forbidden if it parses as a complete sentence with subject + finite verb + object. Long compressions (8+ segments) are permissible if structured as a single noun-phrase with compressed modifiers.
- `<source>` — one or more of `state-update:<id>` | `memory:<id>` | `feeling:<id>` | `proto:<id>` | `tens:<reading>` | `canon:<gloss>` | `world-build:<gloss>`. ≥1 required.

Vibes are permanent stickers — a vibe added in s01e01 persists to s01e02+ unless explicitly retired with `-`. Transient mood / scene-tone / momentary feeling are NOT vibes (those belong to sensory / feeling / tens facets). Sparsity is liberal — no upper ceiling, since vibes are not rendered in prose. Pre-seeded projects (world-build authored vibe-clouds before facet authoring) force `++`-or-skip op behavior on pre-loaded keywords; gate-2 (op coherence) applies to all targets including episode/season/series scope without exception.

`licensed-by:` is mandatory and machine-resolvable. Multi-source preferred. Cross-target fan-out — events affecting multiple entities should fan-out fires across the affected entities (POV + on-stage co-witnesses + scope target + on-stage location if charged).

**Author:** showrunner (cross-cutting; the only agent with all-vibe-cloud visibility). No per-character forks. **Reviewer:** mechanic auditor only (no dialect audience — vibes are not voice-bearing).

(Previous schema-current shape `<scope>:<key> <op> <value>` with scope episode/season/series only and no `licensed-by:` field deprecated 2026-05-07 with vibes-updates facet tuning. Schema content shape revised to entity-target-primary form with formal `licensed-by:` field. See `design/shoot-v2/vibes-tuning-package.md`.)

---

### location-state (`facets/location-state.md`)

Replaces shoot-v1's `STUDIO:` bullets. Environmental state at each proto-line: where, when, weather, sensory palette, active conditions, lighting.

```
<id> @<proto-line-id> <location-slug> | <time> | <weather> | <conditions> | <one-clause sensory note>
```

**Author:** studio.

Proto-lines cite this facet (`[loc-state:<id>]`) when the environment is load-bearing for the action. Proto-lines without a location-state citation render in the most recent cited environment.

---

## Per-file cull

Each facet file is culled by its author after authoring, before cross-facet consistency. The cull is **delete-only** — boring, inane, weak, or duplicative entries are removed. No rewrites at cull time.

Convergence: one cull pass per file. If the author cannot produce a culled file in one pass, the authoring stage failed and the file is re-authored from scratch (rare; flagged).

---

## Cross-facet consistency

After all per-file culls complete, a holistic pass checks for contradictions across facet files (e.g. two state-update entries setting the same field to different values for the same proto-line). The contradiction rule: **delete both, flag for re-author.** Do not pick a winner.

---

## Stitch interface

The stitcher reads proto-lines in citation order. For each citation, it fetches the corresponding facet entry and uses it as guidance for *selection and arrangement*, not for prose generation. Per the stitcher edit budget (only "and"), facet content is either quoted or used as a selection signal — it is not paraphrased into the manuscript.

Some facets are pure selection signals (tensometer, interest flags) — they bias which proto-lines the stitcher chooses to render in full vs. compress. Others are content-bearing (location-state, metaphor) — their content may appear in the stitched output verbatim, surrounded by selected proto-line and dialogue text.

---

## What facets are not

- Not prose. The stitcher does the only prose work, and that work is constrained to "and" plus selection.
- Not editable after cross-facet consistency. State updates write back to canonical memory; that write happens once.
- Not authored by a single agent. Each facet type has its own author per the table above; this is what makes per-file authorship parallelizable and per-file cull tractable.
