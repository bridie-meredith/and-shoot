# Substance Overhaul — Implementation Plan

**Status:** DRAFT, 2026-05-16. Awaiting user approval before execution.

**Triggering feedback** (from `active-project/feedback.md`, s01e01–s01e03):
- "Episodes felt empty and meaningless and like a puff of air, there was no substance."
- "No meaningful plot."
- "The characters don't seem to have a desire."
- "Potential for drama, for the tension to cause movement... but not shown."
- "The plot is very very weak. I believe that the protolines aren't being focused enough or the bones are too fine grained."
- "Scenes should have meaningful suspense and action with something against something."
- "Next time maybe I need to check in on /and-project to make sure things are chunked at the right size."

**Triggering notes** (handwritten, three pages):
1. Measure gain and loss from a perspective (experience-ee + audience), via comparative poll (rank state at Start, rank state at End, difference = Δ).
2. Gain-without-cost vs gain-with-cost — only weighted gain matters.
3. Plot-by-states (has, is) + plot-by-action (did, do) — both required.
4. Status axes: wealth, health, community, emotional well-being (+ spent, possess, journeyed).
5. Δ State / Σ Bones — substance density.
6. Δ required per chunk depends on what chunk abstracts (series / book / chapter / scene).
7. 1–9 scale questionnaire on protagonist state (and world, and antagonist, and story).
8. Impersonator should know what is valued most — overlap with audience values.
9. Bounds → noise/clusters/themes/ideas → meets constraints (setting, protag, antag, clear theme) → expected project plot delta (Δ Start, Δ End, N directions) → plot check gate → reviewer/critic check.

---

## Goal

Bake a **declared, measurable, auditable substance contract** into the pipeline at every chunk level (series → book/season → chapter/episode → scene), so that:

- Every project has its scope (constraints/settings/themes) and staff (personas for planning/reviewing/editing/judging) explicitly bound before any content is authored.
- Every series has a brief substance-bearing chunk (Star-Wars-trilogy-style paragraph) plus structural commitments (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape).
- Every series has a substance signature (state axes + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets) and per-book Δ commitments produced by a generic `/and-substance` command.
- Every cast is assembled to deliver named substance commitments.
- Every season (= book) inherits its Δ commitments and produces per-beat substance tags.
- Every episode bone-set is audited for Δ delivery + cost paid + density curve.
- Every polished prose pass is audited for whether the substance lands (felt by audience, traceable to bones by auditor).

---

## Pipeline restructure

The current `/and-project` does five different jobs (scope + cast + series plan + audit checkpoint). The replacement splits these and adds substance-authoring commands.

**Current chain:** `/and-project → /and-season → /and-shoot-chain → /and-wrap`

**New chain:**

```
/and-project (scope + staff)
  ↓
/and-series (series chunk + structural prompts)
  ↓
/and-substance series (substance signature + per-book Δ commitments)
  ↓
/and-cast (cast roster)
  ↓ [series-level human audit checkpoint here]
/and-season s01 (substance-aware planning + bones + review)
  ↓
[shoot chain: /and-protolines → /and-facets → /and-stitch]
  ↓
/and-wrap (substance-aware editor pass)
```

Six commands change; three are net new.

| command | status | scope |
|---|---|---|
| `/and-project` | **overhauled (shrinks)** | Scaffold; bound project scope (constraints/settings/themes/world laws/behaviors); select staff personas (planning/reviewing/editing/judging). No story content. |
| `/and-series` | **net new** | Take project scope; produce a brief substance-bearing series chunk (Star-Wars-trilogy-paragraph-style); collect structural prompts: book count, book length, cyclical?, POV structure, cross-book continuity, world evolution, series-end shape. No formal signature, no cast. |
| `/and-substance` | **net new — generic recursive chunker** | Read the series chunk + structural prompts. Produce: substance signature (state axes + 1/5/9 anchors + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets) + per-book Δ commitments. **Today:** series→book only. **Future:** book→chapter, chapter→scene, scene→beat using the same command body with a chunk-level argument. |
| `/and-cast` | **net new** | Read series chunk + substance signature + per-book Δ commitments. Margit candidate menu + screen-writer cast review + dramatist viability check + per-actor provisioning + vibes. Output: cast roster (the bodies that will carry the substance). |
| `/and-season` | **overhauled** | As current command. Reads per-book Δ commitments from /and-substance series. Phase 1d adds per-beat substance tags; Phase 1e adds substance gate; Phase 3 adds Pass S11 substance audit; Phase 7 adds per-episode substance verdict. |
| `/and-wrap` | **overhauled** | Three-phase v2. Phase 1 audience review adds `SUBSTANCE-FELT` / `-FLAT` / `-SUSPECT` flags. Phase 2 auditor adds `SUBSTANCE-COVERAGE` class. Phase 3 editor allowed-moves extended for substance remediation within fences. |

`/and-shoot`, `/and-stitch`, `/and-facets`, `/and-protolines*` are downstream and unchanged structurally. They execute on what the bones carry.

---

## Re-runnability

Every new command except `/and-project` is **re-runnable**. The authoring loop is: draft → review → revise → revise → settle. Hard-abort-on-existing would force the user to delete state by hand to iterate, which is the wrong default for creative work.

| command | re-runnable? | re-run modes |
|---|---|---|
| `/and-project` | **NO** — exception | Phase 0 hard-aborts if `project.constraints` already populated. Project scope is foundational; revising it requires a new project. (User-confirmed exception.) |
| `/and-series` | yes | `revise` (build on top of existing chunk + structural answers — pass to screen-writer with current draft + revision intent), `redo` (replace from scratch — current values become priors to avoid). |
| `/and-substance` | yes | `revise` (refine signature in place — same axes, retune anchors/ranks/costs), `add` (add new axes or cost-ledger entries without touching existing), `redo` (replace signature from scratch). |
| `/and-cast` | yes | `revise` (adjust roster — swap one actor, add a new actor, retire an actor without touching others), `redo` (replace roster from scratch — current actors become reference). |
| `/and-season` | yes (existing) | Per-season — Phase 1 auto-handles existing-plan detection today. New: also detects existing per-episode substance verdicts and supports per-episode revision. |
| `/and-wrap` | yes (existing) | Per-episode — re-running re-runs the three phases against the current draft. |

**Phase 0 protocol for re-runnable commands:**

1. Read upstream inputs from memory. Abort if upstream is missing (e.g., `/and-substance series` aborts if `series.chunk` is empty — `/and-series` hasn't run).
2. Check own output. If already populated, prompt the user: `revise` / `add` (where applicable) / `redo`.
3. **Cascade warning.** If downstream commands have run against the current output, flag them as potentially stale. Example: `/and-substance series` is re-run while `seasons[].substance_delta` is populated and `/and-season s01` has authored content beats — warn that beats reference axes/ranks that are about to change; offer to mark season plans for re-validation.
4. Run the chosen mode.

**Staleness marking.** When a re-run changes output that downstream commands depend on, the affected downstream blocks get a `stale_since: <YYYY-MM-DD>` field. The downstream command's next invocation surfaces this and re-validates. No silent overwrites of downstream work.

---

## Boundary table — what moves out of `/and-project`

| Current `/and-project` step | Stays / moves | Lands in |
|---|---|---|
| Phase 1 Scaffold | **stays** | `/and-project` |
| Phase 1.5 Brief expansion | **stays** | `/and-project` |
| Phase 1.6 Audience selection | **stays** | `/and-project` |
| Phase 2 1a — Decided constraints + open questions | **stays** | `/and-project` |
| Phase 2 1b — Open question resolution | **stays** | `/and-project` |
| Phase 2 1c — Candidate menu + cast selection | **moves** | `/and-cast` |
| Phase 2 1d — World-law finalization (condition cards) | **stays** | `/and-project` |
| Series Plan (theme + plot + protag arc + series Q + season chunks) | **splits** | series chunk → `/and-series`; per-season chunks → derived by `/and-season` from `/and-substance series` output |
| Series-level audit checkpoint | **moves** | after `/and-cast` (last series-level command) |
| **NEW** — staff persona binding (planning/reviewing/editing/judging staff, beyond audience) | n/a | `/and-project` |
| **NEW** — structural prompts (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape) | n/a | `/and-series` |
| **NEW** — substance signature (state axes + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets) | n/a | `/and-substance series` |
| **NEW** — per-book Δ commitments | n/a | `/and-substance series` |

After the split, `/and-project` is scope+staff only — no story content, no cast, no themes-as-story-shape.

---

## Archive plan

Archive current versions of the three overhauled commands to `archive/commands/` with the suffix `-pre-substance`:

```
git mv .claude/commands/and-project.md archive/commands/and-project-pre-substance.md
git mv .claude/commands/and-season.md  archive/commands/and-season-pre-substance.md
git mv .claude/commands/and-wrap.md    archive/commands/and-wrap-pre-substance.md
```

`/and-series`, `/and-substance`, `/and-cast` are net new — nothing to archive.

Update `archive/commands/README.md`:

> **2026-05-16 — substance overhaul + project chain split.** The planning + finalization commands were shelved together for two reasons: (1) the pre-substance versions optimize per-line craft, dramatic shape, mechanic discipline, continuity, and prose economy — but have no declared substance contract; episodes shipped through the pre-substance chain were structurally clean and substance-flat. (2) `/and-project` was conflating scope (constraints/settings/themes/staff) with series content (chunk/cast/substance signature). The replacement chain is `/and-project` (scope+staff) → `/and-series` (chunk + structural prompts) → `/and-substance series` (signature + per-book Δ) → `/and-cast` (cast roster) → series-level audit checkpoint → `/and-season` (substance-aware) → `/and-wrap` (substance-aware). See `design/substance/`.

The pre-substance files stay reachable via git for diff/comparison and via `git mv` back to `.claude/commands/` for reactivation if the substance chain regresses.

---

## New artifacts

### `design/substance/README.md`

Framework reference. Authoring authority for substance terminology, state-axis catalog, 1–9 scale anchors, Δ/cost/density definitions, plot-by-states + plot-by-action duality, perspective-bound measurement, antagonist-pressure, failure-mode catalog, pipeline-threading map. **Includes the recursive `/and-substance` design**: per-level inputs, outputs, and constraints for series→book (built today), book→chapter, chapter→scene, scene→beat (documented for future).

### `design/substance/questionnaire.md`

The 1–9 archetype questionnaire (story / protagonist / world / antagonist) used by `/and-substance` to pin axis ranks honestly. Per-archetype question banks. Includes example scoring trace for at least one archetype.

### `design/substance/delta-targets.md`

Per-chunk Δ targets and target bone counts:
- Series-scale Δ (signature axis ranks across the whole series).
- Book-scale Δ (per book, by position: opening / mid / climax / denouement).
- Chapter-scale Δ (per episode).
- Scene-scale Δ.
- Bone-count targets per chunk, computed from Δ × density-target.
- Curve commentary: substance density is a curve across a chunk, not a constant.

### `schemas/showrunner-memory.schema.md` (updated)

Add new top-level `project:` block (the scope+staff output of `/and-project`):
```yaml
project:
  brief: <one-line distill of the user prompt>
  constraints:
    settings: [<one-line each>]
    themes_as_bounds: [<one-line each>]   # thematic bounds, NOT story themes
    hard_fences: [<one-line each>]
  staff:
    audience: [<persona-slug>, <persona-slug>, <persona-slug>]
    screen_writer: <persona-or-library-default>
    dramatist: <persona-or-library-default>
    auditor: <persona-or-library-default>
    editor: <persona-or-library-default>
    orchestrator_critic: <card-version>
```

Update `series:` block — split into content (from `/and-series`), substance (from `/and-substance series`), and cast (from `/and-cast`):
```yaml
series:
  # from /and-series
  chunk: |
    <substance-bearing paragraph — Star-Wars-trilogy-style. The whole arc in prose. e.g.,
    "Luke Skywalker, a moisture farmer with a hidden lineage, learns the ways of the Jedi
    as he is drawn into the rebellion against the Empire, gaining mastery, comrades, and
    a fractured family truth at the cost of his mentor, his innocence, and his hand."
    Substance is implied, not formally measured here.>
  structure:
    book_count: <N>
    book_length: { episodes_per_book: <range>, bones_per_episode: <range> }
    cyclical: true | false
    pov: single | multi | rotating-per-book
    cross_book_continuity: { recurring_antagonists: [...], ongoing_subplots: [...] }
    world_evolution: static | evolving
    series_end_shape: definitive | open-ended | ambiguous | tragic | triumphant
  laws: [...]   # existing
  lore: [...]   # existing
  behaviors: [...]   # existing

  # from /and-substance series
  substance:
    state_axes:
      - slug: <axis-slug>
        dimension: <one line — what this axis measures>
        one_means: <one line>
        five_means: <one line>
        nine_means: <one line>
        perspective: protagonist | antagonist | world
        start_rank: <1-9>
        end_rank: <1-9>
    cost_ledger:
      - gain: <axis-slug> +<delta>
        cost: <axis-slug> -<delta> | opportunity-missed:<one line> | journey-required:<one line>
        arc: <book-slug>
    antagonist_pressure:
      - axis: <axis-slug>
        pressure_source: <one line>
        cost_curve: <one line>
    chunk_targets:
      series: { delta_per_signature_axis: <range>, density_target: <range> }
      book:    { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      chapter: { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      scene:   { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }

  # from /and-cast
  cast_roster: [...]   # existing
  stage_elements: [...]   # existing
```

Add to each `seasons[]` entry (each season = one book; output of `/and-substance series`):
```yaml
substance_delta:
  axes_in_motion:
    - axis: <axis-slug>
      open_rank: <1-9>
      close_rank: <1-9>
      direction: gain | loss | hold-under-pressure
      cost: <axis-slug> -<delta> | opportunity-missed:<one line>
  density_target: <range>
```

Add to each `seasons[].episodes[]` entry (post-Phase-7 of `/and-season`):
```yaml
substance_delta:
  axes_moved:
    - axis: <axis-slug>
      open_rank: <1-9>
      close_rank: <1-9>
      cost_paid: <axis-slug> -<delta> | opportunity-missed:<one line> | none
  density_measured: <ratio>
  s11_verdict: SUBSTANCE-CLEAN | SUBSTANCE-FELT-RISK-<reason> | SUBSTANCE-FLAT-<axis>
```

---

## Command specs

### `/and-project` (overhauled — strict scope + staff)

Three jobs only:

1. **Scaffold** — directory tree, stub files, audience working dirs (mechanical).
2. **Project scope** — bound from the prompt:
   - Phase 1.5 brief expansion (concept-space).
   - Phase 2 1a — decided constraints + open questions.
   - Phase 2 1b — open-question resolution.
   - Phase 2 1d — world-law finalization (condition cards: laws + lore + behaviors).
   - Output: `project.constraints` block + `staff/showrunner/world-notes.md` + condition cards.
3. **Staff selection** — bound personas for planning / reviewing / editing / judging:
   - Audience ×3 (existing Phase 1.6).
   - Screen-writer / dramatist / auditor / editor / orchestrator-critic — record library-default version bound to this project.
   - Output: `project.staff` block.

**Does NOT do:** cast, series chunk, structural prompts, substance signature, audit checkpoint.

**Output:** project-scope-approval checkpoint. Human reviews scope + staff. On approval, `/and-series` is next.

**Estimated size:** ~50% of current `/and-project`.

### `/and-series` (net new — series chunk + structural prompts)

1. **Phase 0 — Validate + mode select.** Read `project:` block. Abort if scope/staff incomplete. If `series.chunk` already populated, prompt the user: `revise` (build on existing) vs `redo` (replace). If downstream (`series.substance`, `series.cast_roster`, `seasons[]`) is populated, surface the cascade and offer staleness-marking.
2. **Phase 1 — Structural prompts.** Interactive collection of:
   - Book count (N).
   - Book length (episodes per book + target bones per episode range).
   - Cyclical (each book ends near its start state, like Harry Potter)? Y/N.
   - POV structure (single / multi / rotating-per-book).
   - Cross-book continuity (recurring antagonists, ongoing subplots, or fully self-contained).
   - World evolution (static / evolving).
   - Series-end shape (definitive / open-ended / ambiguous / tragic / triumphant).
   - Each prompt persists to `series.structure.*`.
3. **Phase 2 — Series chunk authoring.** Screen-writer takes project scope + structural commitments. Produces a brief substance-bearing prose paragraph capturing the whole-series arc. Substance is **implicit** in the chunk — gain language, cost language, conflict language — not yet formally measured.
   - Example target shape: "Luke Skywalker, a moisture farmer with a hidden lineage, learns the ways of the Jedi as he is drawn into the rebellion against the Empire, gaining mastery, comrades, and a fractured family truth at the cost of his mentor, his innocence, and his hand."
4. **Phase 3 — Audience + dramatist review.** Accept/revise loop (3-try cap). Audience checks: does the chunk feel substantive, not airless? Does it match structural commitments (cyclical books should imply cyclical state-return; multi-POV should imply multiple-perspective hooks)? Dramatist checks: dramatic shape, viability, structural soundness.
5. **Phase 4 — Persist.** Write `series.chunk` + `series.structure.*`. No human checkpoint (the checkpoint comes after `/and-cast`).
6. **Output:** series chunk + structural commitments ready. Next: `/and-substance series`.

**Estimated size:** ~150–200 lines.

### `/and-substance` (net new — generic recursive chunker; today: series→book)

Generic substance-chunking command. Takes a parent chunk + a chunk-level argument; produces sub-chunks with per-axis Δ commitments. Today only `series` level is wired; lower levels (`book` / `chapter` / `scene`) are documented in the command body and `design/substance/README.md` for future build.

**Usage today:** `/and-substance series`

**Phases (for `series` level):**

1. **Phase 0 — Validate + mode select.** Read `series.chunk` + `series.structure.*` + `project.constraints`. Abort if upstream missing. If `series.substance` already populated, prompt the user: `revise` (refine in place — same axes, retune anchors/ranks/costs/pressure/targets), `add` (introduce new axes or cost-ledger entries without touching existing), `redo` (replace from scratch — current signature kept as prior for screen-writer to avoid drift). If downstream (`seasons[].substance_delta`, `series.cast_roster`, content beats in season plans) is populated, surface the cascade and offer staleness-marking.
2. **Phase 1 — State-axis signature.** Screen-writer authors 5–9 state axes drawn from `design/substance/README.md` universal catalog + project-specific. For each axis: dimension, 1/5/9 anchor descriptions, perspective tag (protagonist / antagonist / world).
3. **Phase 2 — Δ Start/End.** Using `design/substance/questionnaire.md`, rank the protagonist (and antagonist if present, and world if relevant) on each axis at series open and series close.
4. **Phase 3 — Cost ledger.** For each gain across the arc, name the paired cost (axis loss / opportunity missed / journey required). Anchor each trade to a book.
5. **Phase 4 — Antagonist pressure.** For each protagonist axis, name the opposing force and cost-curve.
6. **Phase 5 — Chunk-Δ targets.** Defaults from `design/substance/delta-targets.md`; project may override.
7. **Phase 6 — Per-book Δ commitments.** For each of the N books (per `series.structure.book_count`), name which signature axes shift, direction, target Δ-magnitude, density target. Honor `series.structure.cyclical` (cyclical books must show state-return, so any in-book Δ is paid back by book close).
8. **Phase 7 — Audience + dramatist substance gate.** Accept/revise loop (3-try cap). Dramatist checks: does the per-book Δ sequence sum to the series Δ? Are cost-ledger entries paid? Audience checks: do the axes feel like the right axes? Are anchors honest?
9. **Phase 8 — Persist.** Write `series.substance.*` + each `seasons[].substance_delta`.
10. **Output:** signature + per-book Δ commitments ready. Next: `/and-cast`.

**Lower-level invocations (documented but NOT implemented today):**
- `/and-substance book <book-slug>` — read book Δ commitments + book chunk; produce per-chapter (episode) Δ commitments.
- `/and-substance chapter <chapter-slug>` — read chapter Δ commitments + chapter chunk; produce per-scene Δ commitments.
- `/and-substance scene <scene-slug>` — read scene Δ commitments + scene chunk; produce per-beat (bone) Δ commitments.

Lower levels remain as docs+stubs in the command body. The current `/and-season` Phase 1 content-beat authoring continues to do the book→chapter chunking inline (now reading per-book Δ commitments as input instead of inventing them).

**Estimated size:** ~250–300 lines (most of it the series-level Phases 1–8; lower levels are stubs).

### `/and-cast` (net new — cast roster)

1. **Phase 0 — Validate + mode select.** Read `series.chunk` + `series.structure.*` + `series.substance.*`. Abort if upstream missing. If `series.cast_roster` already populated, prompt the user: `revise` (swap one actor, add a new actor, retire an actor — preserves untouched actors and their LTM/STM/state/vibes), `redo` (replace roster from scratch — current actors become reference but are decommissioned). If `seasons[]` has content referencing current cast, surface the cascade and offer staleness-marking. **Decommission protocol on `redo`:** margit archives current actor working dirs to `active-project/actors/<slug>-decommissioned-<timestamp>/` so cast history is preserved.
2. **Phase 1 — Substance-driven cast brief.** Screen-writer composes the cast brief from the series chunk + substance signature: which axes need which kinds of carriers (protagonist for the protagonist-perspective axes; antagonist for antagonist-perspective axes; mentor / foil / ally for cost-ledger entries that name relational losses; etc.).
3. **Phase 2 — Margit candidate menu.** Margit produces a candidate menu from `cards/personas/INDEX.md` filtered by world/quality/trope match against the brief.
4. **Phase 3 — Screen-writer cast review.** Select from candidate menu + commission new personas where gap exists. Dramatist viability check on the assembled roster.
5. **Phase 4 — Margit provisioning.** Provision selected personas into `active-project/actors/`. Initialize per-actor LTM/STM/state/vibes.
6. **Phase 5 — Series-level audit checkpoint.** Auditor (fork) against the full series picture: project scope + series chunk + structural commitments + substance signature + per-book Δ commitments + cast roster. Faults route to fixer or escalate. Result presented to user — human reviews and approves. On approval, `/and-season s01` is next.

**Estimated size:** ~200–250 lines.

### `/and-season` (overhauled — substance-aware)

Inherits all current phases. Substance work lands as:

- **Phase 0 validate:** abort if `series.substance` is empty (means `/and-substance series` hasn't run) or if this season's `seasons[].substance_delta` is empty (means per-book Δ commitments weren't authored).
- **Phase 1c (drama):** read the season's per-book Δ commitments. Season drama statement names what cannot survive this book *in terms of axis movement* — not just collision, but Δ.
- **Phase 1d (content beat authoring):** each beat carries a substance tag — which axis moves, direction, target Δ-magnitude, cost (if any). Beats with no axis movement tagged `setup` or `transition` (capped at ~25% of beats per density target).
- **Phase 1e (review):** substance gate — does the beat list deliver the book's named Δ on each axis? Are costs paid? Is the density curve shaped?
- **Phase 2 (bone expansion):** screen-writer brief includes per-beat substance tags. Bones must carry the axis movement — every named Δ has visible cause bones.
- **Phase 3 Sweep A:** add **Pass S11 — Substance audit**:
  - S11.a — dramatist per-window: every book-named axis Δ has visible cause bones; rank movement implied by bones matches named Δ within ±1 rank; cost-ledger entries are paid.
  - S11.b — audience ×3 per-window: `SUBSTANCE-FELT` / `SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>` per persona.
  - Failures route to screen-writer for stretch regen with substance-deficit named.
- **Phase 7 Step 5:** per-episode `substance_delta` block computed from bones-roster + window substance verdicts; persisted to memory.

Sweep A grows from 18 forks to 22 forks (+1 dramatist + 3 audience).

### `/and-wrap` (overhauled — substance-aware)

Inherits three-phase v2 (audience review → auditor pass → editor pass). Substance work:

- **Phase 1 audience review:** persona briefs extended with felt-substance verdict per scene. New flag class: `SUBSTANCE-FELT` (positive) / `SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>` (negative). Advisory.
- **Phase 2 auditor pass:** new class **SUBSTANCE-COVERAGE**. Verifies rendered prose carries per-episode `substance_delta`:
  - Every axis in `axes_moved` has prose-traceable cause language at the named open→close shift.
  - Cost-ledger entries appear in prose at the costed beat.
  - Density curve is shape-honest — peak bones get prose density.
  - HARD findings block the editor; SIGNAL findings inform.
- **Phase 3 editor pass:** allowed-moves extended with substance remediation within fences — prose density tightening at peak beats, percussion naming cost at cost-ledger beats, audience-flagged substance-flat scenes get prose-economy / repetition cuts. **Forbidden:** adding plot, inventing rank shifts, modifying dialogue verbatim. Substance must already be in the bones; editor sharpens its surface.

---

## Order of operations

1. **Plan approval.** This doc reviewed and accepted (or revised).
2. **Design docs first.**
   - `design/substance/README.md` — framework + recursive `/and-substance` design (full).
   - `design/substance/questionnaire.md` — 1–9 archetype questionnaire.
   - `design/substance/delta-targets.md` — per-chunk Δ + bone-count bands.
3. **Schema update.**
   - `schemas/showrunner-memory.schema.md` — new `project:` block, restructured `series:` (chunk + structure + substance + cast subblocks), `seasons[].substance_delta`, `seasons[].episodes[].substance_delta`.
4. **Archive current commands.**
   - `git mv` the three to `archive/commands/<name>-pre-substance.md`.
   - Update `archive/commands/README.md`.
5. **Write new + overhauled commands** (in pipeline order):
   - `.claude/commands/and-project.md` — strict scope+staff.
   - `.claude/commands/and-series.md` — series chunk + structural prompts.
   - `.claude/commands/and-substance.md` — series→book live; lower-level stubs.
   - `.claude/commands/and-cast.md` — cast roster + series-level audit checkpoint.
   - `.claude/commands/and-season.md` — substance-aware (Pass S11).
   - `.claude/commands/and-wrap.md` — substance-aware (SUBSTANCE-COVERAGE).
6. **Update `CLAUDE.md`.**
   - Add `design/substance/README.md` to schemas/authority section.
   - Add substance-framework note to rules.
   - Update command table (new rows for `/and-series`, `/and-substance`, `/and-cast`; updated descriptions for `/and-project`, `/and-season`, `/and-wrap`).
   - Update primary-pattern line to include the new chain.
7. **Commit + push** to `claude/improve-story-substance-CVi58` at logical breakpoints (design docs / schema / archive / each new command / CLAUDE.md).

---

## What is explicitly out of scope

- **Retrofitting flea-bottom-dance.** The current active project keeps its state. The new chain applies to the next `/and-project` run.
- **Facet rubric changes.** Existing facet rubrics (tensometer, feeling, memory-flags, etc.) are not modified.
- **Impersonator card "values block."** Note 8 suggests adding values to actor cards. Deferred — follow-on card-schema task after one full new-chain run.
- **`/and-shoot` overhaul.** Shoot pipeline already in shoot-v2 chain.
- **New facet for substance.** Substance is a contract (planning) and an audit (review), not a facet.
- **Lower-level `/and-substance` invocations.** `/and-substance book`, `chapter`, `scene` are designed and documented in `design/substance/README.md` + the command body, but only `series` ships as live. Lower levels build incrementally as the chain proves stable.
- **Refactor of `/and-season` Phase 1 content-beat authoring into `/and-substance book`.** Stays inline in `/and-season` Phase 1d; reads per-book Δ commitments as input. The `/and-substance book` refactor lands when lower-level chunking is built.
- **Persona library expansion for non-audience staff.** `/and-project` records library-default version; substantive variant composition is a follow-on.

---

## Open questions for user

1. **Archive suffix:** `-pre-substance` (semantic) vs `-v1` / `-v2` (version). Defaulting to `-pre-substance`.
2. **Universal axis set:** `design/substance/README.md` ships with 9 universal axes (wealth, health, community, emotional, capability, knowledge, reputation, agency, trust). Add / remove?
3. **Chunk-Δ defaults:** default ratio (series Δ ≥ 6 ranks across signature, book Δ = 2–3 ranks, chapter Δ ≈ 1 rank, scene Δ = 0–1 rank). Close enough for the first run, or calibrate now?
4. **Pass S11 audience dispatch count:** 3 personas × per-window = scales with N windows. For N=6, that's 18 extra audience dispatches per Sweep A. Acceptable, or run S11.b on whole-season instead of per-window?
5. **Auto-fire upstream from a re-run.** When `/and-substance series` is re-run in `redo` mode and downstream (`/and-cast`, `/and-season`) has run, the downstream work gets staleness-marked. Should downstream commands be **auto-re-fired** when staleness is detected, or hard-abort with a prompt asking the user to re-run them explicitly? Recommend hard-abort — re-running cast or seasons is a substantial operation that deserves explicit user invocation.
6. **Series-end shape values.** Listed five: definitive / open-ended / ambiguous / tragic / triumphant. Add / remove?
7. **Cyclical books — exact semantics.** Cyclical means "each book's protagonist state at close is near its state at open." Does cyclical apply to all axes or only protagonist-perspective ones? (Recommend: only protagonist axes; world axes can drift across cyclical books — that's the HP pattern, Hogwarts evolves while Harry resets.)
8. **Re-run modes naming.** Settled on `revise` (build on existing) / `add` (extend) / `redo` (replace). Acceptable, or prefer different verbs (e.g., `amend` / `extend` / `restart`)?

---

## Verification on completion

After execution, sanity checks:

- `design/substance/{README,questionnaire,delta-targets}.md` exist and parse. README includes the full recursive `/and-substance` design.
- `schemas/showrunner-memory.schema.md` updated with `project:` block + restructured `series:` block (chunk, structure, substance, cast subblocks) + per-season + per-episode substance blocks.
- `archive/commands/and-{project,season,wrap}-pre-substance.md` exist.
- `.claude/commands/and-{project,series,substance,cast,season,wrap}.md` all exist and parse.
- `archive/commands/README.md` updated.
- `CLAUDE.md` updated — new commands in command table, primary-pattern line updated.
- Each new command's Phase 0 validates upstream inputs and hard-aborts on missing.
- Commit + push lands clean on `claude/improve-story-substance-CVi58` at each major step.
