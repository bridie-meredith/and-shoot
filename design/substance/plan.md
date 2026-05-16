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

Bake a **declared, measurable, auditable substance contract** into the pipeline at every chunk level (series → book → chapter → scene → beat/bone), so that:

- Every project has its scope (constraints/settings/themes) and staff (personas for planning/reviewing/editing/judging) explicitly bound before any content is authored.
- Every series has a brief substance-bearing chunk (Star-Wars-trilogy-style paragraph) plus structural commitments (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape).
- Every series has a substance signature (state axes + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets).
- Every cast is assembled to deliver named substance commitments.
- **One recursive command (`/and-substance`) authors substance and structure at every level below series** — book→chapter, chapter→scene, scene→beat (bones). Each level fires its own review. /and-substance replaces the previous `/and-season` and is the entire authoring chain from the series signature down to the bones.
- Every polished prose pass is audited for whether the substance lands (felt by audience, traceable to bones by auditor).

**Bones and facets preserved.** The shoot-v2 chain (bones → facets → stitcher → editor) keeps its shape. `/and-substance scene` emits per-chapter proto-line files that the existing `/and-facets`, `/and-stitch`, `/and-wrap` chain consumes. **Exception:** the **tensometer facet is dropped** — the substance contract (state-axis Δ + cost ledger + density target) is what tensometer was reaching for, more directly and with a declared cause. Tensometer is removed from `/and-facets` output and its rubric is archived; URI-026 "tens-gate" is replaced by the substance bone-gate at `/and-substance scene` Phase 5.

---

## Pipeline restructure

**Current chain (pre-overhaul):** `/and-project → /and-season → [shoot chain] → /and-wrap`

**New chain:**

```
/and-project (scope + staff)
  ↓
/and-series (series chunk + structural prompts)
  ↓
/and-substance series (signature + per-book Δ commitments)
  ↓
/and-cast (cast roster)
  ↓ [series-level human audit checkpoint]
/and-substance book b01 (book chunk + per-chapter Δ; book drama; review)
  ↓
/and-substance chapter b01c01 (chapter chunk + per-scene Δ; chapter dramatic shape; review)
                                  ← fires once per chapter in the book
  ↓
/and-substance scene b01c01s01 (scene chunk + per-beat bones; bone-gate review)
                                  ← fires once per scene in the chapter
  ↓
[shoot chain: /and-protolines → /and-facets → /and-stitch]
  ↓
/and-wrap (substance-aware editor)
```

**Five live commands; one removed.**

| command | status | scope |
|---|---|---|
| `/and-project` | **overhauled (shrinks)** | Scope + staff binding. No story content. |
| `/and-series` | **net new** | Series chunk (Star-Wars-style paragraph) + structural prompts (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape). |
| `/and-substance` | **net new, recursive** | Single command body, fires at four levels (`series`/`book`/`chapter`/`scene`). Authors the substance contract and the next-level-down chunks at each level. The whole authoring pipeline from signature to bones. |
| `/and-cast` | **net new** | Cast roster + series-level human audit checkpoint. |
| `/and-season` | **DROPPED** | Absorbed by `/and-substance` (book + chapter + scene levels). |
| `/and-shoot`/`/and-protolines`/`/and-facets`/`/and-stitch` | unchanged | Operate on the per-chapter proto-line files that `/and-substance scene` emits. |
| `/and-wrap` | **overhauled** | Three-phase v2. Substance-aware: `SUBSTANCE-FELT`/`-FLAT`/`-SUSPECT` audience flags; `SUBSTANCE-COVERAGE` auditor class; editor allowed-moves extended for substance remediation within fences. |

### Why drop /and-season entirely

The previous plan kept `/and-season` because building `/and-substance` at all four levels was a bigger upfront lift than wiring it at the series level alone. But `/and-season`'s actual job — book→chapter chunking + chapter→scene chunking + scene→bones expansion + per-level review — is *structurally* what `/and-substance` does recursively. Compressing it into one inline command is a leaky abstraction: it hides the recursive substance contract from the model (and from re-run protocol, and from staleness cascade). Build `/and-substance` fully and the abstraction is clean: there is exactly one authoring primitive, and it operates the same way at every level.

Secondary benefit: the "season"/"episode" framing dissolves. `/and-substance` operates on `book`/`chapter`/`scene` arguments. The model never reads "episode" while planning or authoring.

---

## Boundary table — what moves where

Three commands are being restructured (`/and-project` shrinks, `/and-season` is dissolved, `/and-wrap` extends).

### Out of `/and-project`

| Current `/and-project` step | Stays / moves | Lands in |
|---|---|---|
| Phase 1 Scaffold | stays | `/and-project` |
| Phase 1.5 Brief expansion | stays | `/and-project` |
| Phase 1.6 Audience selection | stays | `/and-project` |
| Phase 2 1a — Decided constraints + open questions | stays | `/and-project` |
| Phase 2 1b — Open question resolution | stays | `/and-project` |
| Phase 2 1c — Candidate menu + cast selection | moves | `/and-cast` |
| Phase 2 1d — World-law finalization (condition cards) | stays | `/and-project` |
| Series Plan (theme + plot + protag arc + series Q + season chunks) | splits | series chunk → `/and-series`; signature + per-book Δ → `/and-substance series` |
| Series-level audit checkpoint | moves | after `/and-cast` |
| **NEW** — staff persona binding (planning/reviewing/editing/judging staff, beyond audience) | n/a | `/and-project` |
| **NEW** — structural prompts (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape) | n/a | `/and-series` |
| **NEW** — substance signature + per-book Δ | n/a | `/and-substance series` |

### Out of `/and-season` (dissolved)

| Current `/and-season` step | Moves to |
|---|---|
| Phase 1 drama statement | `/and-substance book` Phase 4 (book drama authoring) |
| Phase 1 content beat authoring | `/and-substance book` Phase 3 (per-chapter chunks + per-chapter Δ) + `/and-substance chapter` Phase 3 (per-scene chunks + per-scene Δ) |
| Phase 2 bone expansion | `/and-substance scene` Phase 3 (per-beat bones) |
| Phase 3 review sweeps (S1–S10, S11 substance) | fires inside each `/and-substance` level (audience + dramatist + auditor at the chunk being authored) |
| URI-026 bone-gate (tens-gate) | `/and-substance scene` Phase 5 — **replaced by substance bone-gate**: per-bone axis-movement verification + per-scene Δ delivery + cost-paid check, against the scene's substance contract. Tens rubric retired. |
| Phase 6 orchestrator-critic verdict | `/and-substance book` Phase 7 (auto-fires when all chapters + scenes below are complete) |
| Phase 7 per-chapter file emission | `/and-substance scene` Phase 6 (append bones to `theater/proto-lines/<book>-<chapter>.md`; chapter file finalizes when last scene completes) |

After dissolution, no command body contains the literal word "season."

---

## Re-runnability

Every new command except `/and-project` is **re-runnable**. The authoring loop is: draft → review → revise → revise → settle. Hard-abort-on-existing would force manual state deletion to iterate, which is wrong for creative work.

| command | re-runnable? | re-run modes |
|---|---|---|
| `/and-project` | **NO** — exception | Phase 0 hard-aborts if scope already populated. Project scope is foundational; revising it requires a new project. (User-confirmed.) |
| `/and-series` | yes | `revise` / `redo`. |
| `/and-substance` (any level) | yes | `revise` (refine in place — same children, retune contracts), `add` (add new sub-chunks or axes/costs without touching existing), `redo` (replace all children — current set kept as prior to avoid). |
| `/and-cast` | yes | `revise` / `redo` (margit decommissions current roster to `actors/<slug>-decommissioned-<timestamp>/` on redo). |
| `/and-wrap` | yes | Per-chapter. |

**Phase 0 protocol for re-runnable commands:**

1. Read upstream inputs. Abort if upstream missing.
2. Check own output. If populated, prompt mode (`revise` / `add` where applicable / `redo`).
3. Cascade warning. Surface downstream blocks that depend on what's about to change; offer staleness-marking.
4. Run.

**Staleness cascade across /and-substance levels.** Re-running `/and-substance series` `redo` stale-marks every `/and-substance book` output. Re-running `/and-substance book b01` `redo` stale-marks every `/and-substance chapter` under b01. Etc. Each level's `stale_since: <date>` field is surfaced when that level next runs. No silent overwrites of downstream work.

---

## Archive plan

```
git mv .claude/commands/and-project.md archive/commands/and-project-pre-substance.md
git mv .claude/commands/and-season.md  archive/commands/and-season-dissolved.md
git mv .claude/commands/and-wrap.md    archive/commands/and-wrap-pre-substance.md
```

`/and-season` archive suffix is `-dissolved` (not `-pre-substance`) to mark that it's not coming back — its job moved into `/and-substance`. `/and-project` and `/and-wrap` are overhauls, not removals; their pre-overhaul versions stay reachable via the `-pre-substance` suffix.

`/and-series`, `/and-substance`, `/and-cast` are net new — nothing to archive.

Update `archive/commands/README.md`:

> **2026-05-16 — substance overhaul.** Two reasons. (1) The pre-substance chain optimized per-line craft, dramatic shape, mechanic discipline, continuity, and prose economy — but had no declared substance contract; episodes shipped through it were structurally clean and substance-flat. (2) `/and-project` conflated scope with series content; `/and-season` conflated three levels of recursive chunking (book→chapter→scene→bones) with review and emission. Replacement chain: `/and-project` (scope+staff) → `/and-series` (chunk + structural prompts) → `/and-substance series` (signature + per-book Δ) → `/and-cast` (roster) → series-level audit checkpoint → `/and-substance book/chapter/scene` (recursive authoring) → shoot chain → `/and-wrap` (substance-aware). `/and-season` is dissolved into `/and-substance`. See `design/substance/`.

---

## New artifacts

### `design/substance/README.md`

Framework reference. Authoring authority for substance terminology, state-axis catalog, 1–9 scale anchors, Δ/cost/density definitions, plot-by-states + plot-by-action duality, perspective-bound measurement, antagonist-pressure, failure-mode catalog, pipeline-threading map. **Includes the recursive `/and-substance` design at all four levels** (series / book / chapter / scene): per-level inputs, outputs, review surfaces, and constraints.

### `design/substance/questionnaire.md`

1–9 archetype questionnaire (story / protagonist / world / antagonist) used by `/and-substance` at any level to pin axis ranks honestly. Per-archetype question banks. Example scoring trace.

### `design/substance/delta-targets.md`

Per-chunk Δ targets + bone-count bands.
- Series-scale Δ across the signature.
- Book-scale Δ per book by position (opening / mid / climax / denouement).
- Chapter-scale Δ.
- Scene-scale Δ.
- Bone-count targets per chunk, computed from Δ × density-target.
- Curve commentary: density is a curve across a chunk, not a constant.

### `schemas/showrunner-memory.schema.md` (updated)

New top-level `project:` block (scope+staff from `/and-project`):
```yaml
project:
  brief: <one-line distill>
  constraints:
    settings: [...]
    themes_as_bounds: [...]
    hard_fences: [...]
  staff:
    audience: [<slug>, <slug>, <slug>]
    screen_writer: <persona-or-default>
    dramatist: <persona-or-default>
    auditor: <persona-or-default>
    editor: <persona-or-default>
    orchestrator_critic: <card-version>
```

Restructured `series:` block:
```yaml
series:
  # from /and-series
  chunk: |
    <substance-bearing prose paragraph>
  structure:
    book_count: <N>
    book_length: { chapters_per_book: <range>, bones_per_chapter: <range> }
    cyclical: true | false
    pov: single | multi | rotating-per-book
    cross_book_continuity: { recurring_antagonists: [...], ongoing_subplots: [...] }
    world_evolution: static | evolving
    series_end_shape: definitive | open-ended | ambiguous | tragic | triumphant
  laws: [...]
  lore: [...]
  behaviors: [...]

  # from /and-substance series
  substance:
    state_axes:
      - slug: <axis-slug>
        dimension: <one line>
        one_means: <one line>
        five_means: <one line>
        nine_means: <one line>
        perspective: protagonist | antagonist | world
        start_rank: <1-9>
        end_rank: <1-9>
    cost_ledger:
      - gain: <axis-slug> +<delta>
        cost: <axis-slug> -<delta> | opportunity-missed:<one line> | journey-required:<one line>
        anchor: <book-slug>
    antagonist_pressure:
      - axis: <axis-slug>
        pressure_source: <one line>
        cost_curve: <one line>
    chunk_targets:
      series:  { delta_per_signature_axis: <range>, density_target: <range> }
      book:    { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      chapter: { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      scene:   { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }

  # from /and-cast
  cast_roster: [...]
  stage_elements: [...]
```

Recursive nesting under `books[]` (replaces `seasons[]`):
```yaml
books:
  - slug: b01
    chunk: |
      <book chunk authored by /and-substance series>
    substance_delta:                       # from /and-substance series Phase 6
      axes_in_motion: [...]
      density_target: <range>
    # from /and-substance book
    drama: |
      <"what cannot survive this book" statement>
    structure:
      chapter_count: <N>
    chapters:
      - slug: b01c01
        chunk: |
          <chapter chunk authored by /and-substance book>
        substance_delta:                   # from /and-substance book
          axes_in_motion: [...]
          density_target: <range>
        # from /and-substance chapter
        dramatic_shape: <rising | climax | falling | hinge | ...>
        scenes:
          - slug: b01c01s01
            chunk: |
              <scene chunk authored by /and-substance chapter>
            substance_delta:               # from /and-substance chapter
              axes_in_motion: [...]
              density_target: <range>
            # from /and-substance scene
            bones_count: <N>
            bones_file: theater/proto-lines/b01-c01.md
            bone_gate_verdict: PASS | FAIL-<reason>
        # filled after all scenes complete
        orchestrator_critic_verdict: PASS | PASS-WITH-NOTES | FAIL
        substance_delta_measured:          # post-bones aggregate
          axes_moved: [...]
          density_measured: <ratio>
          s11_verdict: CLEAN | FELT-RISK-<reason> | FLAT-<axis>
```

---

## Command specs

### `/and-project` (overhauled — strict scope + staff)

Three jobs only:

1. Scaffold (directory tree, stub files, audience working dirs).
2. Project scope (Phase 1.5 brief expansion, Phase 2 1a constraints, Phase 2 1b open-question resolution, Phase 2 1d world-law finalization). Output: `project.constraints` block + `staff/showrunner/world-notes.md` + condition cards.
3. Staff selection (audience ×3 + screen-writer / dramatist / auditor / editor / orchestrator-critic library defaults bound to this project). Output: `project.staff` block.

Does NOT do: cast, series chunk, structural prompts, substance signature, audit checkpoint.

Output: project-scope-approval checkpoint. Human reviews. On approval, `/and-series` next.

Estimated size: ~50% of current `/and-project`.

### `/and-series` (net new — series chunk + structural prompts)

1. Phase 0 — Validate + mode select. Read `project:` block; abort if scope/staff incomplete. If `series.chunk` populated, prompt `revise`/`redo`. If downstream populated, surface cascade and offer staleness-marking.
2. Phase 1 — Structural prompts. Interactive: book count, book length (chapters per book + bones per chapter), cyclical?, POV, cross-book continuity, world evolution, series-end shape. Persist to `series.structure.*`.
3. Phase 2 — Series chunk authoring. Screen-writer takes project scope + structure. Produces a brief substance-bearing prose paragraph (Star-Wars-trilogy-style). Substance implicit, not yet measured.
4. Phase 3 — Review. Audience + dramatist accept/revise loop (3-try cap).
5. Phase 4 — Persist `series.chunk` + `series.structure.*`. No checkpoint here.

Estimated size: ~150–200 lines.

### `/and-substance` (net new — recursive, four levels)

Single command body. Argument is the level: `series` / `book <slug>` / `chapter <slug>` / `scene <slug>`. Same five-phase shape at every level.

**Common phases (every level):**

1. **Phase 0 — Validate + mode select.** Read upstream chunk + parent substance commitment. Abort if upstream missing. If own output populated, prompt `revise` / `add` (where applicable) / `redo`. If downstream substance/bones exist, surface cascade + offer staleness-marking.
2. **Phase 1 — Read parent.** Series: read `series.chunk` + structural commitments. Book: read book chunk (from `/and-substance series` output) + per-book Δ commitment. Chapter: read chapter chunk + per-chapter Δ. Scene: read scene chunk + per-scene Δ.
3. **Phase 2 — Author sub-chunks.** Series: produce per-book chunks (one prose paragraph per book in `series.structure.book_count`). Book: per-chapter chunks. Chapter: per-scene chunks. Scene: per-beat bones (SVO units).
4. **Phase 3 — Author sub-chunk substance contracts.** For each sub-chunk: which axes shift, direction, target Δ-magnitude, cost, density. At scene level, bones ARE the contract — each bone carries an axis-movement tag.
5. **Phase 4 — Level-specific extras.** Series: authors the signature itself (state axes, anchors, cost ledger, antagonist pressure). Book: authors the book drama statement. Chapter: authors the chapter dramatic shape (rising / climax / falling / hinge). Scene: nothing extra (bones ARE the contract at scene level).
6. **Phase 5 — Review.** Audience + dramatist + auditor at this level. Accept/revise loop (3-try cap). Substance-felt verdict from audience; structural-soundness from dramatist; constraint adherence + cost-paid verification from auditor. **At scene level**, Phase 5 is the **substance bone-gate** (replaces URI-026 tens-gate): for each bone, verify the declared axis movement is bonefide (SVO actually causes the named Δ; no rank claim without visible cause); for the scene, verify per-axis Δ matches contract within ±1 rank; for each cost-ledger entry tagged to this scene, verify a visible paying bone; audience review for `SUBSTANCE-FELT` vs `SUBSTANCE-FLAT-<axis>` at scene granularity. HARD findings block file emission; SIGNAL findings inform but pass.
7. **Phase 6 — Persist.** Write outputs to showrunner memory at this level's nesting depth. **At scene level**, append bones to `active-project/theater/proto-lines/<book>-<chapter>.md`; when the last scene of a chapter completes, that file finalizes and is ready for `/and-facets`.
8. **Phase 7 — Conditional orchestrator-critic.** **Only at book level**, and only when every chapter and every scene under this book has been substanced (full bone-coverage). Fires the orchestrator-critic against the book-scope output. PASS/PASS-WITH-NOTES/FAIL recorded in `books[<slug>].orchestrator_critic_verdict`.

**`--cascade` flag (book/chapter levels).** Default off (manual level-by-level invocation). With `--cascade`, `/and-substance book b01` auto-fires `/and-substance chapter` for each chapter, then auto-fires `/and-substance scene` for each scene. Reviews still fire at each level; failure at any level halts the cascade. Useful for late-stage runs where the substance contract is settled and the user wants one command to drive everything down to bones.

Estimated size: ~400–500 lines (the largest of the new commands — it carries the whole recursive authoring contract).

### `/and-cast` (net new — cast roster + series audit checkpoint)

1. Phase 0 — Validate + mode select. Read `series.chunk` + `series.structure.*` + `series.substance.*`. Abort if upstream missing. If `series.cast_roster` populated, prompt `revise` (swap/add/retire — preserves untouched actors) / `redo` (replace; margit decommissions current actors to `actors/<slug>-decommissioned-<timestamp>/`).
2. Phase 1 — Substance-driven cast brief. Screen-writer composes brief from chunk + signature: which axes need which carriers.
3. Phase 2 — Margit candidate menu (filtered from `cards/personas/INDEX.md`).
4. Phase 3 — Screen-writer selection + dramatist viability check.
5. Phase 4 — Margit provisioning (actor working dirs, LTM/STM/state/vibes).
6. Phase 5 — Series-level audit checkpoint. Auditor (fork) against full picture (project scope + series chunk + structural commitments + signature + per-book Δ + cast). Result to user. On approval, `/and-substance book b01` next.

Estimated size: ~200–250 lines.

### `/and-wrap` (overhauled — substance-aware)

Three-phase v2 unchanged in shape. Substance work:

- Phase 1 audience review: persona briefs extended with felt-substance verdict per scene. Flag class `SUBSTANCE-FELT` / `SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>`. Advisory.
- Phase 2 auditor pass: new class `SUBSTANCE-COVERAGE`. Verifies rendered prose carries per-chapter `substance_delta_measured` (axes moved have prose-traceable cause language; cost-ledger entries appear at costed beats; density curve is shape-honest). HARD findings block editor; SIGNAL findings inform.
- Phase 3 editor pass: allowed-moves extended for substance remediation within fences — prose density tightening at peak beats; percussion naming cost at cost-ledger beats; audience-flagged flat scenes get prose-economy + repetition cuts. Forbidden: adding plot, inventing rank shifts, modifying dialogue verbatim.

---

## Order of operations

1. **Plan approval.**
2. **Design docs.** `design/substance/README.md` (incl. full recursive design at four levels) + `questionnaire.md` + `delta-targets.md`.
3. **Schema update.** `schemas/showrunner-memory.schema.md` — `project:` block, restructured `series:` with substance subblock, `books[]` nesting (chapters, scenes, bones-file pointer).
4. **Archive current commands + tensometer rubric.**
   - `git mv .claude/commands/and-project.md archive/commands/and-project-pre-substance.md`
   - `git mv .claude/commands/and-season.md  archive/commands/and-season-dissolved.md`
   - `git mv .claude/commands/and-wrap.md    archive/commands/and-wrap-pre-substance.md`
   - `git mv design/shoot-v2/rubric-tensometer.md archive/rubrics/rubric-tensometer-replaced-by-substance.md`
   - Update `archive/commands/README.md` and (new) `archive/rubrics/README.md`.
   - Update `/and-facets` command body to drop tensometer from R1/R2 fanout + facet list. Update CLAUDE.md's URI-026 shared-resources line to remove tens-rubric reference.
5. **Write new + overhauled commands** in pipeline order:
   - `.claude/commands/and-project.md`
   - `.claude/commands/and-series.md`
   - `.claude/commands/and-substance.md` (recursive; four levels)
   - `.claude/commands/and-cast.md`
   - `.claude/commands/and-wrap.md`
6. **Update CLAUDE.md.** New command table rows; `/and-season` removed; primary-pattern line updated to the new chain; substance framework added to schemas/authority section.
7. **Commit + push** to `claude/improve-story-substance-CVi58` at logical breakpoints.

---

## Out of scope

- **Retrofitting flea-bottom-dance.** Current active project keeps its state. New chain applies to the next `/and-project` run.
- **Facet rubric changes — partial.** Bones and facets (feeling, memory-flags, scene-map, dialogue, exposition, etc.) are preserved. **Tensometer is removed** — its purpose (per-bone substance-density signal) is now served directly by the substance contract + scene-level bone-gate. `/and-facets` no longer emits a tensometer file; `design/shoot-v2/rubric-tensometer.md` is archived; CLAUDE.md's "shared reviewer resources" line (URI-026) is updated to drop the tens rubric. The Tens-gate in URI-026 is replaced by the substance bone-gate at `/and-substance scene` Phase 5.
- **Impersonator card "values block."** Deferred — follow-on card-schema task after one full new-chain run.
- **Shoot-v2 chain overhaul.** Unchanged structurally. Operates on the per-chapter proto-line files that `/and-substance scene` emits.
- **`/and-protolines` collapse into `/and-substance scene`.** Same output shape (SVO bones), so structurally `/and-protolines` could be subsumed too. Deferred until the recursive substance chain ships clean; left as a noted follow-on.
- **Persona library expansion for non-audience staff.** `/and-project` records library-default version; substantive variant composition is a follow-on.

---

## Open questions for user

1. **Archive suffix.** `-pre-substance` for `/and-project` + `/and-wrap`; `-dissolved` for `/and-season`. OK?
2. **Universal axis set.** `design/substance/README.md` ships with 9 universal axes (wealth, health, community, emotional, capability, knowledge, reputation, agency, trust). Add / remove?
3. **Chunk-Δ defaults.** Default ratio (series Δ ≥ 6 ranks, book Δ = 2–3, chapter Δ ≈ 1, scene Δ = 0–1). Close enough for first run, or calibrate now?
4. **`/and-substance --cascade` default.** Recommend default OFF (manual level-by-level invocation preserves per-level review checkpoints and dispatch budget). `--cascade` as opt-in for late-stage runs. Confirm?
5. **Orchestrator-critic firing point.** Auto-fire at end of `/and-substance book` when all chapters + scenes below are complete? Or separate `/and-judge-book` command? Recommend auto-fire (minimizes commands; `/and-substance book` can be re-run to re-trigger).
6. **Series-end shape values.** Five: definitive / open-ended / ambiguous / tragic / triumphant. Add / remove?
7. **Cyclical book semantics.** Cyclical applies to protagonist-perspective axes only (world axes can drift across cyclical books — HP pattern; Hogwarts evolves while Harry resets). Confirm?
8. **Re-run modes naming.** `revise` / `add` / `redo`. Acceptable, or different verbs (`amend` / `extend` / `restart`)?
9. **Vocabulary refactor scope.** "Season"/"episode" language still appears in legacy schemas, the shoot-v2 chain (`/and-protolines`, `/and-facets`, etc.), CLAUDE.md, and design docs. Recommended scope: **reading-context** — rename in command bodies, schemas, design docs, CLAUDE.md, and memory file templates the model reads while authoring. Keep filesystem slugs (`s01e01.md` style) and existing in-flight project state alone. Confirm scope, or wider (filesystem too) / narrower (just removed-command bodies)?

---

## Verification on completion

- `design/substance/{README,questionnaire,delta-targets}.md` exist; README documents the recursive design at all four levels.
- `schemas/showrunner-memory.schema.md` updated with `project:` block, restructured `series:`, `books[]` nesting down to scenes + bones-file pointer.
- `archive/commands/and-project-pre-substance.md`, `and-season-dissolved.md`, `and-wrap-pre-substance.md` exist.
- `archive/rubrics/rubric-tensometer-replaced-by-substance.md` exists; `design/shoot-v2/rubric-tensometer.md` gone.
- `/and-facets` command body no longer emits tensometer; CLAUDE.md URI-026 line no longer references tens rubric.
- `.claude/commands/and-{project,series,substance,cast,wrap}.md` exist and parse.
- No active `.claude/commands/and-season.md`.
- `archive/commands/README.md` updated.
- `CLAUDE.md` updated — `/and-season` row removed, new rows for `/and-series`, `/and-substance`, `/and-cast`; primary-pattern line reflects new chain.
- Each new command's Phase 0 validates upstream and supports re-run modes (except `/and-project`, which hard-aborts).
- Commit + push lands clean on `claude/improve-story-substance-CVi58`.
