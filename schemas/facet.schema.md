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

### loudness flags (`facets/loudness.md`)

Volume spikes and drops. Sparse — only at inflection points.

```
<id> @<proto-line-id> <up|down|spike|drop> <one-clause description>
```

**Author:** studio.

---

### feeling flags (`facets/feeling.md`)

What a non-POV character feels and whether they would express it.

```
<id> @<proto-line-id> <character-slug> feels <feeling> | expressed: <yes|no|partial> | <one-clause if expressed>
```

**Author:** dialogue-writer fork for that non-POV character.

---

### metaphor flags (`facets/metaphor.md`)

Comparisons, similes, allegories. Sparse by design — almost never used in end state unless dark humor or memory callback.

```
<id> @<proto-line-id> <metaphor / simile / allegory>: <text>
```

**Author:** editor (taste call). May be culled aggressively in cross-facet pass.

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

Where vibe-cloud entries shift — episode, season, or series vibes.

```
<id> @<proto-line-id> <scope>:<key> <op> <value>
```

`<scope>` is `episode | season | series`. `<op>` is `+` (add), `-` (remove), or `=` (replace). Showrunner applies at the same phase boundary as state updates.

**Author:** showrunner (cross-cutting; the only agent with all-vibe-cloud visibility).

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
