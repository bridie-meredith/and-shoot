---
description: Author the series chunk + structural commitments. Phase 1 collects seven structural prompts (book count, length ranges, cyclical, POV, cross-book continuity, world evolution, series-end shape). Phase 2 dispatches screen-writer to author a substance-bearing series chunk. Phase 3 audience + dramatist review. Phase 4 persists series.chunk + series.structure.*. Usage - /and-series [revise|redo]
---

Authors `series.chunk` + `series.structure.*` from the scope laid down by `/and-project`. The series chunk is a brief substance-bearing paragraph (Star-Wars-trilogy register) — it names the collision and what cannot survive it, without specifying per-book content yet. Per-book content is authored by `/and-substance series` Phase 2.

You are the orchestrator. Dispatches: screen-writer, audience, dramatist. All dispatches use the Agent tool.

Re-runnable. See `design/substance/rerun-protocol.md` for the shared Phase 0 shape.

## Args

- `$1` (optional) — `revise` or `redo` mode. If omitted and `series.chunk` is populated, Phase 0 prompts.

---

## Phase 0 — Validate + mode select

1. Read `staff/showrunner/memory.md`. Confirm `project.brief` is populated and `project.constraints` is non-empty. If not, abort: `/and-series Phase 0 abort: project scope incomplete — run /and-project first.`
2. Inspect `series.chunk` and `series.structure.*`:
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

Persist answers to `series.structure.*` in showrunner memory immediately after collection (so Phase 2 can read them).

---

## Phase 2 — Series chunk authoring

Dispatch **screen-writer** with:
- `project.brief` (verbatim).
- `project.constraints.*` (settings, themes-as-bounds, hard fences).
- `series.structure.*` (just collected).
- `series.laws`, `series.lore`, `series.behaviors` (from `/and-project` Phase 2).
- `staff/showrunner/world-notes.md` + `brief-expansion.md` (for context).

**Screen-writer brief.** Author one substance-bearing prose paragraph (Star-Wars-trilogy register; 2–4 sentences). **Chunk format:** name the collision and what cannot survive it. State what forces are building against each other and what the series' pressure costs or breaks. External and structural — not character psychology. Name stakes and collision shape, not why anyone feels or decides anything.

The chunk does NOT specify per-book content. Per-book chunks are authored by `/and-substance series` Phase 2.

The chunk does NOT include a series title — slugs only.

Output: draft `series.chunk` (proposed; not persisted until Phase 4).

Also build series-level **vibe-cloud** at this phase. The vibe-cloud captures tone / mood / genre-feel keys (e.g. "noir", "wry", "fairytale", "siege-tension"). Write to `series.vibe_cloud.keys`.

---

## Phase 3 — Audience + dramatist review

Dispatch the project's three audience personas + dramatist in parallel:
- Each audience persona reads: proposed chunk, `series.structure.*`, project brief + constraints, their own card + STM.
- Dramatist reads: proposed chunk, `series.structure.*`, project brief.

**Audience verdict:** does the chunk feel like a series's worth of collision? Is the collision specific enough to drive `book_count` books? Audience accept/revise.

**Dramatist verdict:** is the chunk shape sound? Does the named collision span the structural commitments (book_count, cyclical, pov, series_end_shape)?

Accept/revise loop. 3-try cap. On the third revise, ship with reviewer flags annotated in `series-plan.md` and proceed to Phase 4.

After each loop iteration, audience personas write verdicts to their STM (`active-project/audience/<slug>/stm.md`). A planning step whose audience dispatch did not write to STM has not completed correctly.

---

## Phase 4 — Persist

1. Write final `series.chunk`, `series.structure.*`, `series.vibe_cloud.keys` to `staff/showrunner/memory.md`.
2. Append decision summary to `staff/showrunner/series-plan.md`:

```
## Series chunk — accepted at attempt N

<final chunk>

Structural commitments:
  book_count: <N>
  chapters_per_book: <range>
  scenes_per_chapter: <range>
  bones_per_scene: <range>
  cyclical: <bool>
  pov: <value>
  world_evolution: <value>
  series_end_shape: <value>

Audience verdict trace: <one line per persona>
Dramatist verdict: <one line>
```

3. Write a session log to `staff/showrunner/series-log.md`:

```
## Attempt N
audience verdicts: <persona-1>=<accept|revise>, ...
dramatist: <accept|revise>

## Final: accepted at attempt N
```

4. Print summary:

```
--- /and-series COMPLETE ---

Series chunk:
  <chunk>

Structure:
  <book_count> books × <chapters_per_book> chapters × <scenes_per_chapter> scenes × <bones_per_scene> bones
  POV: <value>; cyclical: <bool>; world: <value>; end-shape: <value>

next: /and-substance series
```

---

## Re-run notes

- `revise` keeps structural answers (Phase 1) and re-proposes the chunk (Phase 2 onward). The user may edit structural answers via the Phase 1 prompts if they re-key any of them; the prompt defaults show the prior-run values.
- `redo` re-prompts everything from Phase 1.
- Both modes stale-mark downstream per `design/substance/staleness-cascade.md`.
