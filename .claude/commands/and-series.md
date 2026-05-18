---
description: Author the series chunk + structural commitments. Phase 1 collects seven structural prompts. Phase 1.5 designs the premise — gap-detect, brainstorm 6 candidate paths via 6 lenses, user picks/mutates, expand to trajectory. Phase 2 renders prose from the structured chunk. Phase 3 audience + dramatist + naive-reader review. Phase 4 persists series.chunk (structured) + series.structure.*. Usage - /and-series [revise|redo]
---

Authors `series.chunk` (structured: path + trajectory + prose) and `series.structure.*` from the scope laid down by `/and-project`. The canonical chunk is the structured object; the prose paragraph is a rendering for human reading. Per-book content is authored by `/and-substance series` Phase 2.

You are the orchestrator. Dispatches: screen-writer, audience trio, dramatist, naive-reader. All dispatches use the Agent tool.

Re-runnable. See `design/substance/rerun-protocol.md` for the shared Phase 0 shape.

## Args

- `$1` (optional) — `revise` or `redo` mode. If omitted and `series.chunk.path` is populated, Phase 0 prompts.

---

## Phase 0 — Validate + mode select

1. Read `staff/showrunner/memory.md`. Confirm `project.brief` is populated and `project.constraints` is non-empty. If not, abort: `/and-series Phase 0 abort: project scope incomplete — run /and-project first.`
2. Inspect `series.chunk.path` and `series.structure.*`:
   - **Empty:** proceed to fresh-authoring mode.
   - **Populated, `$1` = `revise`:** mode preselected; skip prompt.
   - **Populated, `$1` = `redo`:** mode preselected; skip prompt.
   - **Populated, `$1` omitted:** prompt `revise` / `redo`.
3. **Cascade warning** *(per `design/substance/staleness-cascade.md`)*. If `books[*]` non-empty or `project.series_audit.approved_at` set, surface affected downstream artifacts:
   - `revise` mode: stale-marks only the affected books if individual structural fields change.
   - `redo` mode: stale-marks all books + `project.series_audit`.
   - Default surfacing choice is `mark-stale`. User may pick `keep-fresh` or `abort`.
4. Run.

---

## Phase 1 — Structural prompts

Seven interactive prompts. Defaults in brackets; pressing enter accepts. Required prompts re-prompt on empty input.

| prompt | type | default | notes |
|---|---|---|---|
| `book_count` | integer (≥1; multiple of 3 if `cyclical: true`) | **required** | top-level shape decision |
| `chapters_per_book` | range `min-max` | `[4-8]` | from `design/substance/delta-targets.md` |
| `scenes_per_chapter` | range | `[1-3]` | scenes are substantial; don't widen |
| `bones_per_scene` | range | `[5-15]` | bones are scene-action-sized |
| `cyclical` | true / false | `[false]` | true for HP-style book-as-school-year |
| `pov` | `single` / `multi` / `rotating-per-book` | **required** | affects `chapters[].pov_narrator` flow |
| `cross_book_continuity.recurring_antagonists` | list | `[empty]` | user adds as needed |
| `cross_book_continuity.ongoing_subplots` | list | `[empty]` | user adds as needed |
| `world_evolution` | `static` / `evolving` | `[evolving]` | static for fairytale-stasis |
| `series_end_shape` | `definitive` / `open-ended` / `ambiguous` / `tragic` / `triumphant` | **required** | shape decision |

Persist answers to `series.structure.*` in showrunner memory immediately after collection.

---

## Phase 1.5 — Premise design

The chunk is authored here as a structured artifact (path + trajectory). Phase 2 only renders prose from this structure.

### 1.5a — Gap detection

Dispatch **screen-writer** with `project.brief`, `project.constraints`, `series.structure`, world-notes / brief-expansion / boundary-scope. Brief:

> Read the project inputs and emit a **brief-gap report** against the premise-complete checklist. For each field, mark `specified`, `inferable`, or `gap`:
> - protagonist start-state by axis (capability / social tether / moral framework / legibility / position)
> - protagonist end-state by axis (some may be locked by hard fences)
> - protagonist motivation engine (what gets them up at start-state; what they protect or pursue)
> - relational anchor (the person/thing whose threat or loss drives the protagonist; may be null if motivation is non-relational)
> - antagonist class (self / man / society / environment; which dominates)
>
> For each `gap`, propose 1-2 candidate fillings drawn from the brief's implied direction. For each `inferable`, name the source and the inference.

If gaps exist, halt and present to user. User picks for each gap: `(a)` answer inline, `(b)` revise brief at /and-project layer and re-run, or `(c)` accept gap as "unbacked premise inference" (logged in `series-plan.md`).

### 1.5b — Path brainstorm

Spawn **six parallel screen-writer dispatches**, one per lens. Each returns ONE candidate path as a five-component structured blurb:

```
path-N (lens: <lens>):
  motivation: <one line>
  anchor: <one line; may be null>
  escalation: <one line>
  trade: <one line>
  irony: <one line>
```

Lens menu (default 6). Each lens biases the motivation/anchor model the screen-writer proposes:

1. **relational** — "Motivation is one specific human connection. The protagonist gets up because of one other person — to protect them, to be seen by them, to stay worthy of them. Road-to-hell hinges on what the protagonist does *for* this person that destroys the person or the relationship."
2. **political** — "Motivation is the protagonist's position in an institutional or factional system — holding, gaining, or refusing a position. Road-to-hell hinges on a positional compromise that turns the position into the catastrophe."
3. **interior** — "Motivation is internal compulsion — repetition, atonement, suppression, refusal of self. Road-to-hell hinges on the protagonist enacting the compulsion they were trying to escape, and the enactment being what destroys what they care about."
4. **penitential** — "Motivation is atonement for past harm. The protagonist is trying to be useful, healing, restorative. Road-to-hell hinges on the atonement work itself becoming the new harm — trying-to-help being the new damage."
5. **escape** — "Motivation is wanting out — out of the world, the role, the obligations. Protagonist is trying to disappear. Road-to-hell hinges on the act meant to buy the exit being the act that closes the exit and destroys what they would have taken."
6. **vocational** — "Motivation is the protagonist's craft or capability — the thing they are good at. Road-to-hell hinges on the capability being deployed for good reasons in a context where it has wrong effects at scale."

Reserve lenses (swap in via arg if user requests):

7. **structural** — "Motivation is being caught between two larger forces neither of which the protagonist created. Road-to-hell hinges on the navigation itself making the collision worse."
8. **accidental** — "Motivation is small and local. Protagonist is not trying to change anything large. Road-to-hell hinges on a small protagonist action having wildly disproportionate consequences because of system brittleness."

Each parallel screen-writer dispatch receives:
- The full project context (brief, constraints, structure, world-notes, gap-report resolutions from 1.5a)
- Its single lens prompt (verbatim)
- Instruction to produce exactly one path in the five-component structured format
- Hard fence: must satisfy locked end-state requirements from `project.constraints.hard_fences`

Append the six paths to `staff/showrunner/series-plan.md` under `## Path brainstorm — round N`.

### 1.5c — Selection

Present the six paths to the user. User options:

- **Pick.** `pick <path-N>` — chosen path becomes canonical.
- **Mutate.** `mutate <path-N> --<component>=<path-M>` (one or more) — compose a mutant by swapping components across paths. Example: `pick 3 --anchor 7 --escalation 5`.
- **Free-text compose.** Plain-English instruction — pipeline parses or asks back.
- **Reject all.** `brainstorm --more [--lenses <list>]` — re-run 1.5b with a fresh lens menu or modified bias prompts.

3-round cap on brainstorms. On cap reached without selection, halt with the latest 18 paths and ask user to pick, compose, or abort.

**TODO (v2):** replace user-driven selection with an audience-critic dispatch that scores all paths against project taste and proposes a pick + rationale. Held for v1; user is the gate.

### 1.5d — Trajectory expansion

Dispatch **screen-writer** with the chosen/composed path. Brief:

> Expand the locked path into a state-trajectory.
>
> - **Start state** — axis-keyed map. Pick the axes that matter for THIS path (capability / social tether / moral framework / legibility / position / health / etc.). Specify the state of each at book-open.
> - **End state** — axis-keyed map, same axes. May inherit values from `project.constraints.hard_fences`.
> - **Deltas** — ordered list of what changes between start and end, in narrative order. Each delta names what shifts and (where load-bearing) what causes the shift.
>
> The deltas are the road. They are the spine /and-substance will compress into per-book chunks.

Write the structured chunk to `series.chunk` in showrunner memory:

```yaml
series.chunk:
  path:
    motivation: ...
    anchor: ...
    escalation: ...
    trade: ...
    irony: ...
  trajectory:
    start_state: { ... }
    end_state: { ... }
    deltas: [ ... ]
  lens_used: <lens-or-"composed">
  prose: ~                                    # rendered at Phase 2
```

Also build series-level **vibe-cloud** at this phase (derived from path + trajectory; tone/mood/genre-feel keys). Write to `series.vibe_cloud.keys`.

---

## Phase 2 — Prose rendering

Dispatch **screen-writer** with the structured `series.chunk` + `series.structure` + project context. Brief:

> Render the structured chunk into one prose paragraph (3-5 sentences) for human reading. This is a *translation* of a locked structure, not invention. The path components and trajectory are the source of truth — do not introduce content not in them.
>
> Required craft moves:
> 1. Lead with the protagonist by name, doing a verb of person. Abstractions banned ("a foreign operator surfaces" = fail).
> 2. Compress protagonist backstory into a relative clause on first name-appearance (derived from start_state).
> 3. Name the relational anchor within the first two sentences (if `path.anchor` is non-null).
> 4. Name the trade — derived from `path.trade` — as the spine of the paragraph.
> 5. Land the irony in plain language at the close — derived from `path.irony`. Show the trap close; don't assert it has.
>
> Banned register (no apparatus prose unless explicitly justified by the trade or irony): ledger / operation / architecture / node / accounting / intelligence-value / asset / infrastructure / regime. Cleft constructions ("it is to X that Y") require justification. Nested appositives capped at one deep.

Write to `series.chunk.prose`.

In `revise` mode with `path` and `trajectory` unchanged, prose rendering is optional (skip unless user requests re-render).

---

## Phase 3 — Review

Dispatch in parallel:

### 3a. Audience trio (full context)

The three project audience personas (from `project.staff.audience`) read the structured chunk + prose + `series.structure` + project context. Two axes of verdict:

- **Structural** — rise-peak-fall, named load-bearing elements, fence-honored, dramatic potency.
- **Premise legibility** — is the motivation engine intact in the chunk itself, or only inferable from dossier?

3-of-3 ACCEPT on each axis. Any axis fails → REVISE with reasons.

Each persona writes verdicts to STM (`active-project/audience/<slug>/stm.md`) under `## /and-series Attempt N verdict`. A planning step whose audience dispatch did not write to STM has not completed correctly.

### 3b. Dramatist (structural shape)

Reads the structured chunk + `series.structure`. Verdict: is the path shape sound? Do the trajectory deltas span the structural commitments (book_count, cyclical, pov, series_end_shape)? ACCEPT or REVISE.

### 3c. Naive-reader gate (context-stripped)

Dispatch the audience agent in single-card config with `staff/audience/naive-reader/card.md`. Hand it ONLY:

- `series.chunk` (path + trajectory + prose if rendered)
- `series.structure.book_count`
- `series.structure.series_end_shape`
- One-line genre orientation (derived from project context, e.g. "tragic-fantasy series in low-magic feudal setting")

The naive-reader scores the chunk on its five-question rubric and returns `ACCEPT N/5` or `REVISE N/5` with per-question gaps.

**Hard gate.** ACCEPT at ≥4/5 required to pass.

### 3d. Aggregation + revise routing

All three pass (audience 3-of-3 on both axes + dramatist ACCEPT + naive-reader ≥4/5) → Phase 4.

Any fail → present consolidated revision report to user. User picks the revise scope:

- **(a) Re-render prose only.** Bounce to Phase 2. Use when only the prose/voice failed, structure is sound.
- **(b) Reselect path.** Bounce to Phase 1.5c with the current brainstorm slate still available.
- **(c) Re-brainstorm.** Bounce to Phase 1.5b for a fresh round (within 3-round cap).
- **(d) Edit path inline.** User specifies the component-level change; skip back to 1.5d trajectory expansion.

3-try cap on overall Phase 3 iterations. On cap reached without pass, halt with all reviewer reports and ask user to override-accept, abandon, or restart.

---

## Phase 4 — Persist

1. Confirm `series.chunk.path.*`, `series.chunk.trajectory.*`, `series.chunk.lens_used`, `series.chunk.prose`, `series.structure.*`, `series.vibe_cloud.keys` are written to `staff/showrunner/memory.md`.
2. Append decision summary to `staff/showrunner/series-plan.md`:

```
## Series chunk — accepted at attempt N

Path (lens: <lens>):
  motivation: <...>
  anchor: <...>
  escalation: <...>
  trade: <...>
  irony: <...>

Trajectory:
  start_state: <axis map>
  end_state: <axis map>
  deltas: <ordered list>

Prose render:
  <final prose>

Structural commitments:
  book_count: <N>
  chapters_per_book: <range>
  scenes_per_chapter: <range>
  bones_per_scene: <range>
  cyclical: <bool>
  pov: <value>
  world_evolution: <value>
  series_end_shape: <value>

Reviewer verdicts (Attempt N):
  audience: <persona-1>=<accept|revise>, ...
  dramatist: <accept|revise>
  naive-reader: <ACCEPT|REVISE> N/5
```

3. Write session log to `staff/showrunner/series-log.md`:

```
## Attempt N
brainstorm rounds: <count>
path picked: <path-N or "composed from X+Y+Z">
audience verdicts: ...
dramatist: ...
naive-reader: ...

## Final: accepted at attempt N
```

4. Print summary:

```
--- /and-series COMPLETE ---

Path (lens: <lens>):
  motivation: <...>
  trade: <...>
  irony: <...>

Trajectory deltas: <N total>

Prose:
  <prose>

Structure:
  <book_count> books × <chapters_per_book> chapters × <scenes_per_chapter> scenes × <bones_per_scene> bones
  POV: <value>; cyclical: <bool>; world: <value>; end-shape: <value>

next: /and-substance series
```

---

## Re-run notes

- `revise` keeps structural answers (Phase 1) and the most recent brainstorm slate; user may pick a different path, mutate, or re-brainstorm. Prose re-renders only if path or trajectory changed.
- `redo` re-prompts Phase 1 and discards prior brainstorm slate.
- Both modes stale-mark downstream per `design/substance/staleness-cascade.md`.

## TODOs deferred from v1

- **Audience-critic-as-path-selector.** Replace user-driven 1.5c with an audience dispatch that scores all paths against project taste and proposes a pick.
- **Per-project lens generation.** Generate the lens menu from `project.constraints` instead of using the fixed default 6+2.
- **Path-brainstorm pattern lifted to /and-substance.** Same shape at book and chapter levels.
- **Structured-chunk consumers.** /and-substance series currently reads `series.chunk.prose` (string, backward-compatible). Migrate to read `series.chunk.path` + `.trajectory` directly.
- **Prose chunk retirement.** Demote `series.chunk.prose` to human-facing-only once downstream consumers read structured form.
