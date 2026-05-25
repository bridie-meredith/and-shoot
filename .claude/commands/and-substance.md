---
description: Recursive chunker authoring substance contracts at four chunk levels (series → book → chapter → scene). Three invocation levels (series / book / chapter). Stops at scene chunks — bones authored by /and-write. Per-level review fires inline. --cascade chains down through /and-write + /and-facets + /and-stitch to draft/<chapter>.md. Usage - /and-substance series|book <slug>|chapter <slug> [revise|add|redo] [--cascade [--resume|--restart]]
---

The recursive chunker. One command body; three invocation levels (`series` / `book <slug>` / `chapter <slug>`); four chunk levels produced (series → book → chapter → scene). At series level, also authors the substance signature (state axes + cost ledger + antagonist pressure + chunk_targets). Stops at scene chunks — `/and-substance` does NOT decompose scenes into bones; that's `/and-write`'s job.

You are the orchestrator. Dispatches: screen-writer, audience (3 personas), dramatist, auditor. All dispatches use the Agent tool. Showrunner is read-mostly.

Re-runnable per `design/substance/rerun-protocol.md`. Cascade-aware per `design/substance/staleness-cascade.md`.

## Args

```
/and-substance series                           [revise|redo|add] [--cascade [--resume|--restart]]
/and-substance book b<NN>                       [revise|redo|add] [--cascade [--resume|--restart]]
/and-substance chapter b<NN>c<MM>               [revise|redo|add] [--cascade [--resume|--restart]]
```

- Invocation level (`series` / `book <slug>` / `chapter <slug>`) — required first token.
  - `series` takes no slug arg.
  - `book` requires a book slug (e.g. `b01`).
  - `chapter` requires a chapter slug (e.g. `b01c01`).
- Mode (`revise` / `add` / `redo`) — optional. Same semantics as `design/substance/rerun-protocol.md`. `add` is meaningful for chunkers (adds new child chunks); not all levels support all modes.
- `--cascade` (optional) — drives the pipeline forward to `draft/<chapter>.md` for every chapter in scope. See "Cascade" section below.
- `--resume` / `--restart` (optional, requires `--cascade`) — used to resume from `staff/showrunner/cascade-checkpoint.md` or restart fresh.

**Rejected:** `/and-substance scene <slug>` — scene chunks are produced by `/and-substance chapter`, not invoked separately. Error message points the user at `/and-write` for bone authoring.

---

## Common phases (same shape at every level)

### Phase 0 — Validate + mode select

1. Read `staff/showrunner/memory.md`. Confirm upstream:
   - **`series` level:** `series.chunk.path` + `series.chunk.prose` + `series.structure.*` populated. If not, abort: `/and-substance series Phase 0 abort: series.chunk missing — run /and-series first.` (Schema note: `series.chunk` is a structured object under `/and-series` v2; v1-compat consumers in this command body read `series.chunk.prose` for the string form. Migration TODO: read `series.chunk.path` + `.trajectory` directly.)
   - **`book b<NN>` level:** `books[b<NN>].chunk` + `books[b<NN>].substance_delta` populated (authored by `/and-substance series` Phase 6). `project.series_audit.approved_at` set, `stale_since` null. If audit not approved, **HARD-ABORT:** `/and-substance book Phase 0 abort: project.series_audit not approved — run /and-cast Phase 5 and approve.` Additionally: **`series.substance.actor_baselines[]` must be DENSE** — for every actor in `series.cast_roster[]` and every axis in `series.substance.state_axes[]`, an entry must exist with `applicability ∈ {moves, static, not-applicable}`. If any cell is missing, **HARD-ABORT:** `/and-substance book Phase 0 abort: actor_baselines[] sparse — run /and-substance series add actor_baselines to fill the matrix. Missing cells: <list of actor × axis pairs>.` (Per the 2026-05-21 axis-bookkeeping split; `actor_baselines[]` is authored at `/and-substance series` Step 4d post-cast pass.)
   - **`chapter b<NN>c<MM>` level:** `books[b<NN>].chapters[b<NN>c<MM>].chunk` + `substance_delta` populated (authored by `/and-substance book` Phase 6).
2. Check own output:
   - **`series`:** `books[*].chunk` populated AND `series.substance.*` populated.
   - **`book b<NN>`:** `books[b<NN>].chapters[*].chunk` populated AND `books[b<NN>].drama` populated.
   - **`chapter b<NN>c<MM>`:** `chapters[b<NN>c<MM>].scenes[*].chunk` + `scene_conflict` populated AND `chapters[b<NN>c<MM>].{pov_narrator, dramatic_shape, goal}` populated.
3. **Mode resolution:**
   - Output empty → fresh-authoring mode.
   - Output populated + mode arg → mode preselected.
   - Output populated + mode arg omitted → prompt `revise` / `add` / `redo`.
4. Cascade warning per staleness-cascade rules. Default surfacing is `mark-stale`.
5. **Parking-lot scan (Rule 14).** Read `active-project/staff/showrunner/parking-lot.md`. Items matching this invocation (`target.command: /and-substance` + `target.scope` matches the current invocation level + slug exact or `*` wildcard + `status: open`): HARD → abort unless this run's resolving phase completes the item; SOFT → carry to Phase 7 summary. Resolving phase stamps `resolved_at` + `resolved_by` + `resolution_note`; never delete.
6. Run.

### Phase 1 — Read parent

| level | reads |
|---|---|
| `series` | `series.chunk.prose` + `series.chunk.path` + `series.chunk.trajectory` + `series.structure.*` + `project.constraints.*` + `series.{laws, lore, behaviors}` + `staff/showrunner/world-notes.md` |
| `book b<NN>` | `books[b<NN>].chunk` + `books[b<NN>].substance_delta` + `series.chunk.prose` + `series.chunk.path` + `series.substance.*` + `series.structure.book_length.*` + `books[b<NN-1>].handoff_out` if `NN > 1` |
| `chapter b<NN>c<MM>` | `chapters[b<NN>c<MM>].chunk` + `chapters[b<NN>c<MM>].substance_delta` + `books[b<NN>].drama` + `books[b<NN>].substance_delta` + `series.substance.*` + `series.structure.book_length.scenes_per_chapter` |

### Phase 2 — Author sub-chunks

Dispatch **screen-writer** with the parent context (per Phase 1) + the level's authoring brief.

| level | screen-writer task |
|---|---|
| `series` | Author one chunk per book (`books[1..book_count]`). Each chunk is one paragraph, Star-Wars-trilogy register, naming this book's collision shape and what cannot survive it. Honors `series.structure.cyclical` / `pov` / `world_evolution` / `series_end_shape`. Last book chunk delivers the named `series_end_shape`. |
| `book b<NN>` | Author one chunk per chapter (`chapters[1..chapter_count]`). Each chunk is one paragraph naming the chapter's local collision and what shifts. Honors book drama (from Phase 4) and POV pattern. |
| `chapter b<NN>c<MM>` | Author one chunk per scene (`scenes[1..scene_count]`). Each chunk is substantial — scenes typically fill most of a chapter, 1-3 scenes per chapter default. Each names the scene's collision shape (without explicitly stating per-bone Δ — that's authored at Phase 3). |

**Child-count selection.** Picked from the parent's structural range:
- Series level: picks `books[b<NN>].structure.chapter_count` per book from `series.structure.book_length.chapters_per_book` range. Books are not interchangeable — opening / mid / climax / denouement books typically take different chapter counts within the range.
- Book level: picks `chapters[].structure.scene_count` per chapter from `scenes_per_chapter` range. Climactic chapters typically take more scenes.
- Chapter level: produces scenes per `scenes[]`; bone counts are deferred to `/and-write` Phase 1.

Persist child slugs at Phase 6 per the slug-auto-generation rules below.

### Phase 3 — Author sub-chunk substance contracts

For each sub-chunk, screen-writer authors a `substance_delta` block per the 2026-05-21 axis-bookkeeping split (`schemas/showrunner-memory.schema.md`):

```yaml
substance_delta:
  axes_in_motion:                          # axes that actually move at this chunk level
    - axis: <axis-slug>                    # must match series.substance.state_axes[].slug
      direction: up | down                 # REQUIRED; null/~ malformed (use axes_held for held-flat)
      target_delta_magnitude: <positive>   # REQUIRED; > 0 (zero malformed — use axes_held)
      cost_ledger_anchor: <id> | [<id>, ...] | null
      notes: <one line>
  axes_held:                               # axes deliberately held flat by discipline; load-bearing dormancy
    - axis: <axis-slug>
      rationale: <one line>                # names the discipline the chunk enacts on this axis
  density_target: <range>
```

Per-axis discipline:
- **`axes_in_motion[]`** lists axes that move across this chunk. Direction (`up | down`) + magnitude (> 0) + cost-ledger anchor when applicable. `direction: null` / `magnitude: 0` are schema violations.
- **`axes_held[]`** lists axes deliberately held flat (the held axis is load-bearing — usually the scene's stakes-axis). Hinge chapters often have axes-held entries on the discipline axis (e.g. capability held by the protagonist's prohibition). A held axis contributes zero to the per-axis Δ aggregate by definition.
- **`scene_conflict.stakes_axis`** may resolve to either `axes_in_motion[]` (the conflict moves it) or `axes_held[]` (the conflict holds it); `/and-write` Phase 6 bone-gate validates against the union.

Contracts must:
- Sum-roll-up to parent within ±1 rank, on `axes_in_motion[]` only (audited at Phase 5). Held axes have zero rank-Δ contribution.
- Honor `series.substance.chunk_targets.<this-level>` bands (delta + density + bone-count where applicable).
- Reference cost-ledger entries when paying a series-level cost (sets `cost_ledger_anchor`).
- Have at least one of `axes_in_motion[]` or `axes_held[]` non-empty per non-frame chunk. A chunk with both empty is malformed unless `chapter_class: frame-coda` is set (b01c18 Corvan-coda pattern is the canonical exempt case).

**Chapter level additionally authors per-scene `scene_conflict`** for every scene:
```yaml
scene_conflict:
  protagonist_force: <one line>     # what the protagonist is pushing for
  opposing_force: <one line>        # what is pushing back
  stakes_axis: <axis-slug>          # must appear in this scene's substance_delta.axes_in_motion[] OR axes_held[] (union; per 2026-05-21 axis-bookkeeping split — held-discipline scenes pin stakes to the held axis)
```

**Book level additionally authors `chapters[].handoff_in` + `chapters[].handoff_out`** for every chapter:
```yaml
handoff_in:
  open_threads: [...]
  world_state: [...]
  character_state: [...]
  source_chapter: <prior-chapter-slug> | null
handoff_out:
  open_threads: [...]
  world_state: [...]
  character_state: [...]
  target_chapter: <next-chapter-slug> | null
```

**First-chapter fallback (F7).**
- For chapter N where N > 1 within a book: `handoff_in.source_chapter = chapter N-1`; mirror chapter N-1's `handoff_out`.
- For the **very first chapter of the first book** (`b01c01`): `handoff_in.source_chapter: null`. Seed `world_state` from `project.constraints.settings`; seed `character_state` from `series.substance.state_axes[].start_rank` for the protagonist + named antagonists.
- For the **first chapter of book N > 1** (`b<NN>c01`): `handoff_in.source_chapter = last chapter of book N-1`; mirror that chapter's `handoff_out`.

Dramatist Phase 5 cross-checks the handoff mirror for every adjacent pair except the very first (`b01c01` has no prior).

**Cost-ledger refinement (G4).** Chapter-level Phase 3 may refine `series.substance.cost_ledger[].anchor.{chapter, scene}` when a scene pays a previously-coarsely-anchored cost. Non-destructive — coarser anchors stay populated; finer anchors add on top.

### Phase 4 — Level-specific extras

**Series level — substance signature authoring (B2 — agent-proposes / user-edits).**

Phase 4 at series level is where the signature itself is born. The 1–9 archetype questionnaire (`design/substance/questionnaire.md`) is the screen-writer's authoring rubric, not a user prompt sequence.

- **Step 4a — Screen-writer proposes.** Dispatch screen-writer with `project.brief` + `project.constraints` + `series.chunk.prose` + `series.chunk.path` + `series.chunk.trajectory` + `series.structure.*`. For each universal axis (~9: wealth / health / community / emotional / capability / knowledge / reputation / agency / trust), screen-writer:
  - Produces `start_rank` (1-9) and `end_rank` (1-9) per perspective (protagonist / antagonist / world), with one-line justification per rank citing source text.
  - Writes `one_means` / `five_means` / `nine_means` anchors calibrated to the story-world.
  - Drafts cost-ledger entries (gain ↔ cost pairings) and antagonist-pressure entries.
  - Drafts `chunk_targets` (defaults from `design/substance/delta-targets.md`, may be tuned per project).

  Writes draft to `staff/showrunner/signature-draft.md` (full YAML).

- **Step 4b — User edits.** Phase 4 surfaces:
  ```
  Signature draft written to staff/showrunner/signature-draft.md.

  Rendered table:
  <ASCII table of axes × perspectives × start/end ranks + cost-ledger summary>

  Edit the YAML in place. Add/remove axes, adjust ranks, rewrite cost-ledger entries.
  When ready, type `accept`. Type `redraft` to ask the screen-writer for a fresh proposal.
  ```

- **Step 4c — Persist on accept.** Edited YAML moves from `signature-draft.md` to `series.substance.*` in memory. Phase 5 review runs against the accepted signature. **NOTE:** `series.substance.actor_baselines[]` (per-actor positional grid, dense 8×9 matrix or similar per `schemas/showrunner-memory.schema.md`) is NOT authored at this step — the cast roster doesn't exist yet (cast is provisioned by `/and-cast` after `/and-substance series`). `actor_baselines[]` is authored later: see Step 4d below for the post-cast pass.

- **Step 4d — Post-cast actor_baselines pass (`/and-substance series add actor_baselines`, fires after `/and-cast` lands).** Dispatch screen-writer with `series.substance.state_axes[]` (the 9 axes authored at 4a) + `series.cast_roster[]` (provisioned by `/and-cast`) + every cast member's role description. Screen-writer authors the dense actor × axis matrix (every cast member × every state-axis = N × M cells) with explicit `applicability` per cell:
  - `moves` (start_rank ≠ end_rank; actor arcs on this axis across the book) — with both ranks pinned and `source: lifted-from-state-axes | inferred-from-role-card`.
  - `static` (start_rank = end_rank; deliberately pinned, examined not skipped) — with `source` + rationale in `notes`.
  - `not-applicable` (actor does not participate in this axis's machinery) — with `notes` REQUIRED naming the deliberate exclusion (e.g. "walk-on; no per-axis arc"; "frame-coda; outside in-book scope"; "Aemond IS elite; axis tracks register TOWARD elite from non-elite — does not apply").
  
  No cell may be omitted — absence is a schema violation. The dense matrix prevents judgment-by-omission. Writes draft to `staff/showrunner/actor-baselines-draft.md`; user edits in place; `accept` persists to `series.substance.actor_baselines[]`. The first `/and-substance book b<NN>` Phase 0 HARD-ABORTS if the matrix is empty or missing any cast × axis cell.

**Book level — drama statement.** Screen-writer authors `books[b<NN>].drama` — a one-paragraph "what cannot survive this book" statement. Names the structural collision at book scope.

**Chapter level — dramatic_shape + goal + pov_narrator + chapter_class.**
- `chapters[].dramatic_shape`: one of `rising` / `climax` / `falling` / `hinge`. Picked per chapter to honor book drama curve.
- `chapters[].goal`: one-line "what this chapter shows the audience." Pass 4 trim and `/and-write` Phase 7 `goal:` header source.
- `chapters[].pov_narrator`: resolved from `series.structure.pov`:
  - `single` → inherited from series (the protagonist actor slug).
  - `rotating-per-book` → inherited from book-level POV decision.
  - `multi` → picked per chapter from cast roster (screen-writer chooses based on chunk).
- `chapters[].substance_delta.chapter_class`: one of `standard` (default) | `frame-coda`. Set to `frame-coda` ONLY when the chapter is an interlude / retrospective outside the protagonist-axis scope (e.g. b01c18 archmaester-retrospective coda authored from a non-Taylor POV at a temporally-displaced moment). Frame-coda chapters are exempt from `/and-write` Phase 6 substance bone-gate; the per-chapter Δ contract still authors `axes_held[]` rationale to document why the chapter is outside the standard accounting. The default (omitted or `standard`) is the normal substance-bone-gate path.

Always populated on every chapter so `/and-write` can write the bones-file header without further lookup. `chapter_class` defaults to `standard` if omitted.

### Phase 5 — Chunk-quality review

Dispatch the project's three audience personas + dramatist + auditor in parallel.

| reviewer | role |
|---|---|
| audience (×3) | Does this chunk *feel* substantive — Δ feel earned, cost feel real, meaningfulness land? Verdicts: `SUBSTANCE-FELT` / `SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>` |
| dramatist | Is the chunk shape sound? Do children fit within parent's Δ? Scenes-not-too-small (chapter level)? Cyclical / cross-book / structural commitments honored? Chapter dramatic-arc completion? **Book level additionally checks cross-chapter handoff:** for every adjacent chapter pair (N, N+1) under the book, `chapters[N].handoff_out` is consistent with `chapters[N+1].handoff_in`. Mismatches HARD-fail and force revise on the offending chapter chunks. |
| auditor | Does the chunk text match the substance contract? No rank claim without described cause. Cost-ledger consistency. Per `schemas/audit-report.schema.md`. **Thematic-axis-coverage (chapter level, URI-CONTRACT-THEMATIC-AXIS):** the chapter `goal` names a thesis; the contract must declare that thesis axis in `axes_in_motion[]` or `axes_held[]`. A `goal` about a moral-framework turn whose contract never lists `moral-framework` is under-declaring its own thesis — `THEMATIC-AXIS-UNDECLARED-<axis>`, HARD at this level (blocks persist, forces revise). The mechanical sum/enum checks never catch this; it asks whether the contract is about what the chapter is about. |

**SUBSTANCE-FLAT and SUBSTANCE-SUSPECT-cheap-gain are HARD findings** at this level (per intent-gaps rationale). They block persist and force revise.

Accept/revise loop. 3-try cap. Audience personas write verdicts to STM after each loop iteration.

### Phase 6 — Persist + slug auto-generation

Write chunks + contracts to showrunner memory.

**Slug auto-generation (G3).** Each persist phase generates child slugs deterministically:
- `/and-substance series` Phase 6 generates `books[*].slug` as `b01`, `b02`, …, `bN` (`N = series.structure.book_count`).
- `/and-substance book b<NN>` Phase 6 generates `chapters[*].slug` as `b<NN>c01`, `b<NN>c02`, …, `b<NN>cM`.
- `/and-substance chapter b<NN>c<MM>` Phase 6 generates `scenes[*].slug` as `b<NN>c<MM>s01`, …, `b<NN>c<MM>sP`.

`add` mode appends to existing list (next index continues monotonically). `redo` regenerates from index 1.

After persist, advance any applicable status:
- `book` Phase 6 sets each new `chapters[].status = planned`.
- `chapter` Phase 6 sets `chapters[<slug>].status = scened`.

**Persist-time intermediate cleanup (URI-SUBSTANCE-DRAFT-PRUNE, A11 — 2026-05-21).** After the YAML accept moves working content from `staff/showrunner/<level>-draft.md` to memory, move the draft file to `staff/showrunner/_drafts/<level>-draft-<timestamp>.md` (do NOT delete — preserve for post-hoc inspection). The `_drafts/` subdir is git-tracked but conceptually archival; the top-level `staff/showrunner/` keeps only active working files. Drafts named for pruning:
- `signature-draft.md` (series level, Step 4a/c)
- `actor-baselines-draft.md` (series level, Step 4d)
- `b<NN>-draft.md` (book level, Phase 4 drama statement)
- `b<NN>c<MM>-draft.md` (chapter level, Phase 4)

The SUPERSEDED-by-memory marker is preserved in the pruned file's header for traceability. Re-runs (`add` / `redo`) write a fresh draft at the top-level path; the prior version stays archived.

### Phase 7 — Print summary + exit-state

```
--- /and-substance <level> [<slug>] COMPLETE ---

[level-specific summary — see per-level templates below]

next: <next-command>
```

Per-level exit-state hand-off:
- `series` (without cascade): `next: /and-cast`.
- `book b<NN>` (without cascade): `next: /and-substance chapter b<NN>c01`.
- `chapter b<NN>c<MM>` (without cascade): `next: /and-write b<NN>c<MM>`.
- With `--cascade`: `next:` is the cascade `next.command` from the checkpoint.

---

## Cascade flag

`--cascade` chains the pipeline forward to `draft/<book>-<chapter>.md`:

| invocation | cascade unwinds to |
|---|---|
| `/and-substance series --cascade` | per book: `/and-substance book` → per chapter: `/and-substance chapter` → `/and-write` → `/and-review bones` → `/and-facets` → `/and-stitch` |
| `/and-substance book b<NN> --cascade` | per chapter under b<NN>: `/and-substance chapter` → `/and-write` → `/and-review bones` → `/and-facets` → `/and-stitch` |
| `/and-substance chapter b<NN>c<MM> --cascade` | `/and-write b<NN>c<MM>` → `/and-review bones b<NN>c<MM>` → `/and-facets b<NN>c<MM>` → `/and-stitch b<NN>c<MM>` (single-chapter convenience, G7) |

`/and-review bones` is a mandatory cascade step — `/and-facets` Phase 0 HARD-aborts without a fresh `bones_review` record (URI-WRITE-BONES-REVIEW-GATE). `/and-stitch`'s Phase 9 cold-read terminal gate is the cascade's last step; a cold-read FAIL halts the cascade and routes to `/and-write revise`.

Reviews still fire at each level inside each command. Failure at any level **halts the cascade**.

### Checkpoint

After each child command completes inside the cascade (book persist / chapter persist / bones emit / facets emit / draft emit), write `staff/showrunner/cascade-checkpoint.md`:

```yaml
cascade:
  root: <root-slug>
  invoked_at: <iso-timestamp>
  invoked_command: /and-substance <level> <slug> --cascade
  last_completed:
    level: book | chapter | scene | bones | facets | draft
    slug: <slug>
    completed_at: <iso-timestamp>
  next:
    command: /and-substance chapter b<NN>c<MM> | /and-write b<NN>c<MM> | ...
    args: [<positional-args>]
  reason: continue | halted-on-failure | halted-on-cut
  failure: <one-line description if reason=halted-on-failure> | null
```

`/and-cut` mid-cascade writes the same file with `reason: halted-on-cut`.

### `--resume`

`/and-substance <root> --cascade --resume`:
1. Reads `cascade-checkpoint.md`.
2. Validates `root` matches `cascade.root`.
3. Validates checkpoint is not stale (warns + offers `--restart` if older than root's `stale_since`).
4. Re-fires from `next.command`.

`--cascade` without `--resume` that finds an existing checkpoint warns and prompts `--resume` vs. `--restart`.

### Cascade failure surfacing (F8)

When the cascade halts:

```
[failing command's normal failure output, including the offending finding(s)]

Cascade halted at <failing-command>: <N> HARD findings (<finding-class-list>).
Checkpoint: staff/showrunner/cascade-checkpoint.md (reason: halted-on-failure)
Resume: /and-substance <root> --cascade --resume
```

---

## Re-run notes

- `revise` refines in place — same children, retune contracts.
- `add` appends new sub-chunks. Useful at series level for adding a book; at book level for adding a chapter.
- `redo` replaces all children. Existing set retained as `<level>-prior-<timestamp>` for comparison.
- `revise` / `redo` stale-mark downstream per `design/substance/staleness-cascade.md`. Any `/and-substance` re-run scoped at-or-under a book that already has an `orchestrator_critic_verdict` stale-marks that verdict.
- Per-scene-conflict gate-verdict clearing (F3) is owned by `/and-write revise`, not by `/and-substance`.

---

## Error: scene-level invocation

`/and-substance scene <slug>` is rejected with:

```
Error: /and-substance does not author bones. Scene chunks are produced by /and-substance chapter; bones are decomposed and authored by /and-write.

For bones authoring: /and-write <chapter-slug>
For scene revision:  /and-substance chapter <chapter-slug> revise
```
