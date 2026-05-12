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

#### Boundary-carry ID exception (tensometer only, URI-038, 2026-05-11)

In `tensometer-<season-slug>-window-<NN>.md` review-window files only (the intermediate form produced at `/and-season` Phase 3 S10 Step 2; NOT in finalized `tensometer-<season-slug>e<NN>.md` files), entries representing boundary-carry bones from the windowN's open region (the first 10 bones — bones that signal active constraints from windowN-1's close per the boundary-carry discipline at Phase 3 S10 Step 4) MAY use the alpha-suffix form `0a`, `0b`, `0c`, ... for their `<id>` field. These entries sort before the first monotonic integer (`1`, `2`, ...) entry and are visually distinguishable as pre-window-open carry-throughs.

This is a review-phase convention. The Phase 7 Step 4 finalization MUST normalize boundary-carry alpha-suffix IDs to monotonic integers continuing from the prior tens-entry-ID sequence (typically: rename `0a` → `1`, `0b` → `2`, and shift the rest of the file's IDs accordingly). The finalized per-episode tensometer file is strictly monotonic per the rule above — no alpha-suffix IDs survive into the deliverable form.

Inline-rupture bones inserted mid-scene at S10 Step 3 (e.g. `17a @519 3` placed between `17` and `18` to signal a Scene-A rupture inserted at file-position-after-bone-17) follow the same convention: alpha-suffix IDs permitted in `-window-` files for narrative-position clarity; normalized to monotonic integers at Phase 7 Step 4.

A `# boundary-carry` or `# inline-rupture` comment immediately preceding the alpha-suffix entry is recommended for traceability but not required for schema compliance.

Header (frontmatter) optional but recommended for traceability:

```
facet: <type>
episode: <slug>
author: <agent-slug>
---
```

---

## Facet types and content shape

### tensometer (`facets/tensometer.md` — canonical; or `facets/tensometer-<season-slug>e<NN>.md` — bone-gate provenance)

Tension scalar per proto-line, scale 1–3.

```
<id> @<proto-line-id> <1|2|3>
```

- 1 — quiet; ambient or transitional.
- 2 — pressure; stakes visible, escalation possible.
- 3 — peak; rupture, crisis, or held-breath threshold.

**Author:** dramatist (single rater pass).

**Dual provenance (URI-026, 2026-05-10).** Tens has two valid authoring sources:

1. **Primary (bone-gate):** `/and-season` Phase 4 Step 1.5 — per-proposed-episode dramatist fork during the season-scope bone-gate. Output path: `facets/tensometer-<season-slug>e<NN>.md` (slug-suffixed). This is the load-bearing source: it gates audience review of bones at Phase 4 Step 2 and feeds Phase 6 F7 (bone-gate residual). The per-episode file ships as part of /and-season's proto-line deliverable.

2. **Legacy:** `/and-facets-r1` Layer 1 — per-episode dramatist fork during the facet graph build. Output path: `facets/tensometer.md` (flat canonical). Retained operationally during Phase 1 of the migration; deferred for deletion in Phase 2.

**No path collision.** The slug-suffixed primary path and the flat canonical legacy path are distinct files; no single-writer guard needed.

**/and-shoot integration.** Phase 0 renames `facets/tensometer-<season-slug>e<NN>.md` → `facets/tensometer.md` for current-episode work. The slug-suffixed copy remains as canonical archive.

**Shared class library (URI-026).** The tens-relevant subset of `.claude/commands/and-facets-audit.md`'s rubric classes (`FREQUENCY-BAND`, `CURVE-SHAPE`, `AP-SCAN`) is consumed by both `/and-season` Phase 4 Step 2 (bone-gate mechanic verdict) and `/and-facets-audit` (per-episode audit). The audit command is the shared review surface; no /and-season-specific reimplementation.

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

### exposition (`facets/exposition-<episode-slug>.md`)

Audience-modeled context — the reader-gap content. For each thing a fresh reader cannot reasonably be expected to know on a cold read (Westeros-specific roles like `reeve` / `maester` / `Watch`; series-specific objects like `the log` / `the count`; pre-story circumstances like the resurrection and family acceptance), an exposition entry attaches a brief gloss to a specific anchor with a directive on how the stitcher should render it.

```
<id> @<anchor> <key>: <gloss-text> | scope: <scope-kind> | renders-as: <position> | sources: <list> | licensed-by: <list>
```

- **`@<anchor>`** — proto-line anchor where the gloss best lands. For episode-open scope, use `@0` (synthetic anchor; renders pre-body). For first-mention scope, use the proto-line ID where the term/object first appears in the rendered prose.
- **`<key>`** — the thing being glossed. Free-text noun-phrase or a category tag like `episode-open-preamble`, `morning-bowl`, `reeve`, `maester`. Keys SHOULD be slug-form for cross-episode reference.
- **`<gloss-text>`** — the explanatory text the stitcher will render. ≤30 words for first-mention scopes; ≤80 words for episode-open scopes. Plain English. No invented compounds. No new plot content beyond what the cited sources already establish.
- **`scope: <scope-kind>`** — one of:
  - `episode-open-preamble` — the cold-start or interval-bridge frame paragraph; renders before the body.
  - `episode-open-context` — additional context paragraph(s) in the preamble; renders after the preamble's first paragraph.
  - `first-mention-term` — Westeros-specific or series-specific term the audience won't know on cold read.
  - `first-mention-object` — series-specific object whose presence needs orientation (e.g. `the log`).
  - `first-mention-place` — location whose context the audience needs.
  - `prior-episode-bridge` — recap content for subsequent-episode interval-bridge.
  - `scene-open-orient` — micro-bridge at scene boundary (time / place / why-here). **Conditional fire** (see fire-rule below).
- **`renders-as: <position>`** — one of:
  - `italic-preamble` — italic paragraph before the body (episode-open scopes only).
  - `preamble-paragraph` — additional preamble paragraph (episode-open-context only).
  - `inline-appositive` — em-dash appositive after the first-mention noun: `"the reeve — the lord's bookkeeper for village debts"`.
  - `parenthetical-aside` — parenthetical immediately after the first-mention sentence: `"He spoke to the reeve. (The reeve was the lord's man for...)"`.
  - `post-bone-clause` — full clause after the bone, period-separated.
  - `em-dash-fold` — em-dash phrase mid-sentence: `"the morning bowl — porridge and salt — on the table"`.
  - `scene-bridge` — micro-orientation sentence at scene-open (≤15 words).
- **`sources: <list>`** — comma-separated graph sources the gloss content is derived from (series-plan paths, world-build cards, condition cards, character cards, prior facets). Every claim in `<gloss-text>` must trace to at least one source. Audit-able.
- **`licensed-by: <list>`** — comma-separated audience-model justifications. At minimum one persona-card slug + the gap-claim ("cape-fic-doesnt-know-westerosi-feudal-roles", "worm-canon-doesnt-know-flea-bottom-geography"). The exposition-author's reasoning surface.

**Author:** `exposition-author` — a dedicated audience-modeled subagent that loads the active audience persona cards (`active-project/audience/`) and the series/world-build sources, then asks per-anchor: "would the union of these audience personas know what X is on cold read?" If no, an exposition entry is authored.

**Per-anchor cap ≤2.** Multiple exposition entries on the same anchor are permitted only as one of these pairs: episode-open-* + scene-open-orient, scene-open-orient + first-mention-*, episode-open-* + first-mention-*. No two entries of the same scope on the same anchor.

**Scene-open-orient conditional fire-rule (2026-05-12 dogfood-validated).** A `scene-open-orient` entry fires for a scene boundary if AND ONLY IF:
- (a) the proto-line has a time-skip blank immediately preceding the scene-open anchor (i.e. the scene is genuinely discontinuous from the prior scene, not a paragraph break within a continuous time-frame), AND
- (b) `location-state` does NOT fire at the scene-open anchor (loc-state at-establishment carries the time/place; if it fires, the scene-orient is wallpaper), AND
- (c) no `interest-narrator` entry in the first 2 anchors of the new scene carries time-of-day or place-shift content (NI-cognition of "the morning was already half-gone" or "the city smell came up before the wall did" makes the scene-orient redundant; in that case NI carries the load).

The exposition-author MUST audit each scene-boundary against these three conditions and refuse to fire when (b) or (c) holds. The lens facets carry the orientation; exposition stays out. This is the validated routing principle from the s01e01 dogfood — the Phase 2 author (full graph in hand) refused scene-orient entries that the Phase 1 author (no facets) authored, and the audit-trail was: lens facet covers, exposition refuses.

When scene-orient fires, the entry is brief (≤15 words) and emits as `renders-as: scene-bridge` — a single short sentence at the scene-open, BEFORE the first bone's rendered prose. Examples (from s01e01): "After breakfast I went out to the yard." / "Mid-morning, my mother came back in." / "The next morning, the elder came." / "Down at street level," / "Within the hour,"

**Sparsity 1-5%.** Higher than feeling/sensory because the audience-gap surface is significant in cross-genre projects (Worm-in-Westeros has gap on both sides); lower than NI because most of the prose carries via lens-facets without needing exposition.

**Per-episode caps:**
- `episode-open-*` scopes: ≤4 entries total per episode (1 preamble + ≤3 context paragraphs).
- `first-mention-*` scopes: ≤12 entries per episode (one per first-mention term/object/place that needs glossing; if more are needed, audience-model is wrong or the episode is overloaded).
- `scene-open-orient` scopes: 1 entry per scene MAX (the micro-bridge).
- `prior-episode-bridge` scope: ≤1 entry per episode (replaces episode-open-preamble for non-first-episode runs).

**Cross-episode promotion.** Once a first-mention gloss for `reeve` is authored in s01e01, future episodes do NOT re-gloss `reeve` — the term is now reader-resident. The exposition-author tracks already-glossed terms via a per-project register at `active-project/staff/exposition-author/glossed-terms.md`. A reader who skips s01e01 sees the s01e02 episode-open-preamble's prior-episode-bridge content + their own first-mention exposures; explicit glossing past first-mention is wallpaper and forbidden.

**Audit-able.** The auditor's CONSTRAINT class scans each `<gloss-text>` against the `<sources>` list — any claim not derivable from sources is fault. AP-SCAN class scans for invented plot content (exposition is restatement of graph-resident facts, not new content). FREQUENCY-BAND validates the per-episode caps.

**Renders at Stitcher Phase 1 fold-in.** The stitcher reads exposition entries at Phase 1 alongside the lens facets. `scope: episode-open-*` entries are pulled by Phase 0.6 and rendered as the interval-bridge. `scope: first-mention-*` entries fold in at their `@<anchor>` per the `renders-as` directive. `scope: scene-open-orient` entries render as the scene's opening micro-bridge. Phase 7 evaluates exposition prose under Q1-Q9 like any other rendered content; the audience-model upstream is the primary defense against bad glosses.

(Schema added 2026-05-12. Replaces stitch-profile.schema.md's `interval-bridge:` block and the project-profile `first-mention-glosses:` ad-hoc list; both subsumed by upstream-authored exposition facets.)

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
