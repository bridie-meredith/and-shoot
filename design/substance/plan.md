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

**Clean split between substance and bones.** `/and-substance` is a **chunker only** — it authors chunks at each level (series → book → chapter → scene → **beat**) and attaches a substance contract to each (Δ axes, costs, density target). It stops at beat chunks; it does NOT write SVO bones. Bones are authored by **`/and-write`** (renamed from `/and-protolines`), which reads beat chunks + their substance contracts and produces the SVO units. This separation matters: chunking (how meaningful, what shifts, at what cost) and bone-writing (subject-verb-object craft, line economy, continuity) are different jobs at different levels of resolution. Conflating them is the failure mode `/and-season` has today. The rename to `/and-write` also drops pipeline-jargon framing ("protolines") in favor of creative-writing language.

**Bones and facets preserved.** The shoot-v2 chain (bones → facets → stitcher → editor) keeps its shape. `/and-write` consumes beat chunks instead of an "episode chunk," runs the existing five-pass SVO pipeline (inventory → constraint → shape → trim → continuity), and emits the per-chapter bones file that `/and-facets`, `/and-stitch`, `/and-wrap` consume. **Exception:** the **tensometer facet is dropped** — the substance contract (Δ + cost ledger + density target) is what tensometer was reaching for, more directly and with a declared cause. Tensometer is removed from `/and-facets` output and its rubric is archived; URI-026 "tens-gate" is replaced by the **substance bone-gate** as a pass inside `/and-write`, which verifies the bones actually deliver the declared substance contract.

---

## Pipeline restructure

**Current chain (pre-overhaul):** `/and-project → /and-season → [shoot chain] → /and-wrap`

**New chain:**

```
/and-project (scope + staff)
  ↓
/and-series (series chunk + structural prompts)
  ↓
/and-substance series (signature + per-book Δ + book chunks)
  ↓
/and-cast (cast roster)
  ↓ [series-level human audit checkpoint]
/and-substance book b01 (book drama + per-chapter Δ + chapter chunks)
  ↓
/and-substance chapter b01c01 (dramatic shape + per-scene Δ + scene chunks)
                                  ← fires once per chapter
  ↓
/and-substance scene b01c01s01 (per-beat Δ + beat chunks)
                                  ← fires once per scene; deepest chunker level
  ↓
/and-write b01c01 (reads beat chunks; produces SVO bones; substance bone-gate)
                                  ← fires once per chapter
  ↓
[shoot chain: /and-facets → /and-stitch]
  ↓
/and-wrap (substance-aware editor)
```

**Seven live commands; one removed; one renamed.**

| command | status | scope |
|---|---|---|
| `/and-project` | **overhauled (shrinks)** | Scope + staff binding. No story content. |
| `/and-series` | **net new** | Series chunk (Star-Wars-style paragraph) + structural prompts (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape). |
| `/and-substance` | **net new, recursive** | Single command body, fires at four levels (`series`/`book`/`chapter`/`scene`). Authors chunks + substance contracts at each level. Stops at beat chunks — does NOT write bones. |
| `/and-cast` | **net new** | Cast roster + series-level human audit checkpoint. |
| `/and-season` | **DROPPED** | Chunking jobs absorbed by `/and-substance` (book/chapter/scene levels); bone-writing job absorbed by `/and-write`. |
| `/and-write` | **renamed + overhauled** (was `/and-protolines`) | Reads beat chunks + substance contracts from `/and-substance scene` output. Runs five-pass SVO pipeline (inventory → constraint → shape → trim → continuity) + substance bone-gate. Emits per-chapter bones file. |
| `/and-review` | **net new** | Universal review primitive. Reviews any target (signature / chunk / contract / bones / prose / cast / whole-tree) on demand. Fires appropriate reviewers, produces a report, no authored writes. |
| `/and-judge-book` | **net new** | Orchestrator-critic verdict for a finished book. Fires when `/and-substance book` + `/and-write` (all chapters) complete. |
| `/and-facets`/`/and-stitch` | unchanged structurally | Operate on the per-chapter bones file `/and-write` emits. Tensometer facet removed from `/and-facets`. |
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
| Phase 1 content beat authoring | `/and-substance book` Phase 3 (per-chapter chunks + per-chapter Δ) + `/and-substance chapter` Phase 3 (per-scene chunks + per-scene Δ) + `/and-substance scene` Phase 3 (per-beat chunks + per-beat Δ) |
| Phase 2 bone expansion (SVO writing) | `/and-write` (reads beat chunks, produces SVO bones via five-pass pipeline) |
| Phase 3 review sweeps (S1–S10, S11 substance) | chunk-quality reviews fire inside each `/and-substance` level (audience: meaningful? dramatist: shape? auditor: contract match?); SVO + continuity reviews fire inside `/and-write`. |
| URI-026 bone-gate (tens-gate) | `/and-write` substance bone-gate pass — **replaces tens-gate**: per-bone axis-movement verification + per-scene Δ delivery + cost-paid check, against each beat's substance contract. Tens rubric retired. |
| Phase 6 orchestrator-critic verdict | `/and-judge-book <slug>` (separate command) — fires when both `/and-substance book` (all chunks) and `/and-write` (all chapter bones files) are complete for the book. |
| Phase 7 per-chapter file emission | `/and-write` Phase N (emit bones to `theater/bones/<book>-<chapter>.md`) |

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
| `/and-write` | yes | Per-chapter. `revise` (re-write specific bone ranges flagged SIGNAL by bone-gate) / `redo` (full rewrite — preserves chunks, replaces bones). |
| `/and-review` | yes (idempotent) | Any subcommand can be re-fired any number of times. Each invocation persists a new timestamped report; nothing else is mutated. |
| `/and-judge-book` | yes | Per-book. Re-firing re-judges against current state; useful after re-running `/and-substance` or `/and-write` at any level. |
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
git mv .claude/commands/and-project.md      archive/commands/and-project-pre-substance.md
git mv .claude/commands/and-season.md       archive/commands/and-season-dissolved.md
git mv .claude/commands/and-wrap.md         archive/commands/and-wrap-pre-substance.md
git mv .claude/commands/and-protolines.md   archive/commands/and-protolines-pre-substance.md
# and-protolines-v2 and and-protolines-season-v2: archived alongside; replaced by /and-write
```

`/and-season` archive suffix is `-dissolved` (not `-pre-substance`) to mark that it's not coming back — its chunking job moved into `/and-substance`, its bone-writing job moved into `/and-write`. `/and-project`, `/and-wrap`, and `/and-protolines` are overhauls/renames; their pre-overhaul versions stay reachable via the `-pre-substance` suffix.

`/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-judge-book` are net new — nothing to archive (other than `/and-protolines` which is the predecessor to `/and-write`).

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
      beat:    { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }

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
            beats:                         # from /and-substance scene
              - slug: b01c01s01b01
                chunk: |
                  <beat chunk — coarse description of what happens at this beat>
                substance_delta:           # from /and-substance scene
                  axes_in_motion: [...]
                  density_target: <range>
        # chapter-level fields filled by /and-write
        bones_file: theater/bones/b01-c01.md
        bones_count: <N>
        substance_bone_gate_verdict: PASS | FAIL-<reason>
        substance_delta_measured:          # post-bones aggregate
          axes_moved: [...]
          density_measured: <ratio>
          felt_verdict: SUBSTANCE-FELT | SUBSTANCE-FLAT-<axis> | SUBSTANCE-SUSPECT-cheap-gain-<axis>
    # book-level field filled by /and-judge-book
    orchestrator_critic_verdict: PASS | PASS-WITH-NOTES | FAIL
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

1. **Phase 0 — Validate + mode select.** Read upstream chunk + parent substance commitment. Abort if upstream missing. If own output populated, prompt `revise` / `add` (where applicable) / `redo`. If downstream chunks or `/and-write` bones exist, surface cascade + offer staleness-marking.
2. **Phase 1 — Read parent.** Series: read `series.chunk` + structural commitments. Book: read book chunk + per-book Δ. Chapter: read chapter chunk + per-chapter Δ. Scene: read scene chunk + per-scene Δ.
3. **Phase 2 — Author sub-chunks.** One prose paragraph per child unit. Series → per-book chunks. Book → per-chapter chunks. Chapter → per-scene chunks. Scene → **per-beat chunks** (the deepest chunks — coarse descriptions of what happens at each beat; "Maya confronts her brother about the missing key" is a beat chunk, not a bone).
4. **Phase 3 — Author sub-chunk substance contracts.** For each sub-chunk: which axes shift, direction, target Δ-magnitude, cost, density target.
5. **Phase 4 — Level-specific extras.** Series: authors the signature itself (state axes, anchors, cost ledger, antagonist pressure). Book: authors the book drama statement. Chapter: authors the chapter dramatic shape (rising / climax / falling / hinge). Scene: nothing extra.
6. **Phase 5 — Chunk-quality review.** Audience + dramatist + auditor at this level. Accept/revise loop (3-try cap). **Audience:** does this chunk feel substantive — does the named Δ feel earned, the cost feel real, the meaningfulness land? `SUBSTANCE-FELT` vs `SUBSTANCE-FLAT-<axis>` vs `SUBSTANCE-SUSPECT-cheap-gain-<axis>`. **Dramatist:** is the chunk shape sound? Do the children fit within the parent's Δ? Cyclical / cross-book / structural commitments honored? **Auditor:** does the chunk text match the substance contract (no rank claim without described cause; cost-ledger consistency)?
7. **Phase 6 — Persist.** Write chunks + contracts to showrunner memory at this level's nesting depth. **No bones at any level** — bones are written by `/and-write`.

**`--cascade` flag (book/chapter/scene levels).** Default off (manual level-by-level invocation). With `--cascade`, `/and-substance book b01` auto-fires `/and-substance chapter` for each chapter, then `/and-substance scene` for each scene under each chapter, then `/and-write` for each chapter (after all its scenes are substanced). Reviews still fire at each level; failure at any level halts the cascade. Useful for late-stage runs where the substance contract is settled and the user wants one command to drive everything to bones.

Estimated size: ~400–500 lines (the largest of the new commands — it carries the whole recursive authoring contract).

### `/and-cast` (net new — cast roster + series audit checkpoint)

1. Phase 0 — Validate + mode select. Read `series.chunk` + `series.structure.*` + `series.substance.*`. Abort if upstream missing. If `series.cast_roster` populated, prompt `revise` (swap/add/retire — preserves untouched actors) / `redo` (replace; margit decommissions current actors to `actors/<slug>-decommissioned-<timestamp>/`).
2. Phase 1 — Substance-driven cast brief. Screen-writer composes brief from chunk + signature: which axes need which carriers.
3. Phase 2 — Margit candidate menu (filtered from `cards/personas/INDEX.md`).
4. Phase 3 — Screen-writer selection + dramatist viability check.
5. Phase 4 — Margit provisioning (actor working dirs, LTM/STM/state/vibes).
6. Phase 5 — Series-level audit checkpoint. Auditor (fork) against full picture (project scope + series chunk + structural commitments + signature + per-book Δ + cast). Result to user. On approval, `/and-substance book b01` next.

Estimated size: ~200–250 lines.

### `/and-write` (renamed + overhauled — was `/and-protolines`; the bones crafter)

Reads beat chunks + substance contracts produced by `/and-substance scene`. Produces SVO bones for one chapter at a time. Replaces `/and-protolines` as the shoot-v2 chain entry.

**Phases (per chapter):**

1. **Phase 0 — Validate + mode select.** Read all beat chunks for the chapter (every scene under it, every beat under each scene). Abort if any beat is unsubstanced. If `theater/bones/<book>-<chapter>.md` already exists, prompt `revise` (re-write specific bone ranges identified by SIGNAL findings) / `redo` (full rewrite).
2. **Phase 1 — Inventory.** Walk every beat chunk; list the substance contract for each (axis movements, costs, density target).
3. **Phase 2 — Constraint audit.** Verify each beat's contract is well-formed (no rank claims without parent-cost backing; no axis movements outside the scene's contract; no costs unaccounted-for in the cost ledger).
4. **Phase 3 — Shape (SVO writing).** For each beat, author one or more SVO bones that cause the declared axis movement. Subject-verb-object craft, line economy. Bones inherit the beat's substance contract as a tag.
5. **Phase 4 — Trim.** Drop bones that don't cause Δ (chatter bones), unless they're needed for setup/transition (capped at density-target ratio).
6. **Phase 5 — Continuity audit.** State-thread check across bones (props move, actors track, conditions persist).
7. **Phase 6 — Substance bone-gate.** **Replaces URI-026 tens-gate.** For each bone: verify the declared axis movement is bonefide (SVO actually causes named Δ; no rank claim without visible cause). For each beat: verify per-axis Δ delivered within ±1 rank. For each scene under the chapter: verify cost-ledger entries are paid by visible bones. Audience review (3 personas) per scene window: `SUBSTANCE-FELT` / `SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>`. HARD findings block emission; SIGNAL findings record but pass.
8. **Phase 7 — Emit.** Write bones to `active-project/theater/bones/<book>-<chapter>.md` (renamed from `theater/proto-lines/...`). File ready for `/and-facets`.

Estimated size: ~300–400 lines (carries the existing five-pass SVO pipeline + substance bone-gate + emission).

### `/and-review` (net new — universal review primitive with subcommand router)

Top-level router dispatches to one of N pre-defined review types. No authored writes; reports persist to `staff/reviews/<type>-<target>-<timestamp>.md`.

**Router subcommands:**

| subcommand | target | fires | what it reviews |
|---|---|---|---|
| `/and-review chunk <slug>` | any chunk slug (series / b01 / b01c01 / b01c01s01 / b01c01s01b01) | audience + dramatist + auditor | Does the chunk match its substance contract? Is it the right depth for its level? Does it feel meaningful? Cost language honest? |
| `/and-review contract <slug>` | any chunk slug | dramatist + auditor | Is the substance contract well-formed? Do per-axis Δ-magnitudes sum correctly to parent? Cost-ledger consistent? No rank claims without backing? |
| `/and-review signature` | series only | audience + dramatist + auditor | Series signature health: are the axes the right axes? Anchors honest? Cost ledger paid across the arc? Antagonist pressure named per axis? |
| `/and-review bones <chapter-slug>` | chapter slug | bones critics (SVO craft) + bone-gate logic | Per-bone axis-movement bonefide? Per-scene Δ delivered? Cost-paid? `SUBSTANCE-FELT`/`-FLAT` per scene. |
| `/and-review facets <chapter-slug>` | chapter slug | per-facet rubric runners | Facet-by-facet review against rubric. |
| `/and-review prose <chapter-slug>` | chapter slug | audience + auditor | Polished prose — felt-substance per scene; `SUBSTANCE-COVERAGE` audit. (Overlaps `/and-wrap` Phase 1/2 but on-demand, no editor invocation.) |
| `/and-review cast` | — | dramatist + auditor | Roster substance-fit: does the roster have carriers for every signature axis perspective? Viability check. |
| `/and-review consistency [<root-slug>]` | optional root (defaults to series) | dramatist + auditor | Cross-level: do per-book Δ aggregates sum to series Δ? Do chapter dramatic shapes honor book drama? Do scene contracts fit within chapter contract? Cost-ledger entries paid? Cyclical commitments honored? |
| `/and-review tree [<root-slug>]` | optional root | all of the above, scoped to the subtree | Full sweep at and below root. Defaults to whole series. |
| `/and-review feedback <feedback-file> [<root-slug>]` | feedback file + optional root | audience + auditor | Re-fires reviewers carrying named feedback as context. Use case: "review s01 against `active-project/feedback.md`." |

**Common phases (every subcommand):**

1. Phase 0 — Parse subcommand. Validate target exists in memory / on disk.
2. Phase 1 — Compose review brief specific to subcommand (which reviewers, what rubric, what scope).
3. Phase 2 — Dispatch reviewers in parallel (audience persona forks per persona; dramatist; auditor).
4. Phase 3 — Aggregate findings into a structured report. Classify HARD / SIGNAL / TASTE per the existing auditor taxonomy.
5. Phase 4 — Persist report to `staff/reviews/<subcommand>-<target>-<timestamp>.md`. Surface to user. Optionally offer to materialize findings into a fix queue for the appropriate authoring command (e.g., HARD findings on `chunk b01c03` → fix queue for `/and-substance chapter b01c03 revise`).

**Relationship to inline reviews.** Authoring commands (`/and-substance` Phase 5, `/and-write` Phases 5/6, `/and-wrap` Phases 1/2) still have inline review *gates* that catch problems before persistence. `/and-review` is for AFTER persistence — going back to spot-check or sweep on demand. Same reviewer infrastructure (audience cards, dramatist, auditor) is shared. The inline gates can call into the same review subroutines `/and-review` dispatches.

Estimated size: ~300–400 lines (the router + N subcommand implementations; each subcommand is small because the reviewers do the heavy lifting).

### `/and-judge-book` (net new — orchestrator-critic gate for a finished book)

Fires the orchestrator-critic against the book-scope output once every chapter under the book has bones authored.

1. Phase 0 — Validate. For book `<slug>`: verify `/and-substance book <slug>` complete, every chapter and scene under it substanced, every chapter has a bones file in `theater/bones/<slug>-<chapter>.md`.
2. Phase 1 — Compose book-scope picture (chunks at every level + contracts + bones aggregate).
3. Phase 2 — Fire orchestrator-critic against `staff/orchestrator-critic/card.md` standard.
4. Phase 3 — Record verdict in `books[<slug>].orchestrator_critic_verdict`: PASS / PASS-WITH-NOTES / FAIL. FAIL escalates to user; downstream (`/and-facets` etc.) gated on user decision.

Re-runnable: yes (re-firing re-judges against current state).

Estimated size: ~80–120 lines (thin orchestration over an existing critic card).

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
   - `git mv .claude/commands/and-project.md      archive/commands/and-project-pre-substance.md`
   - `git mv .claude/commands/and-season.md       archive/commands/and-season-dissolved.md`
   - `git mv .claude/commands/and-wrap.md         archive/commands/and-wrap-pre-substance.md`
   - `git mv .claude/commands/and-protolines.md   archive/commands/and-protolines-pre-substance.md`
   - `git mv .claude/commands/and-protolines-v2.md archive/commands/and-protolines-v2-pre-substance.md` (if present)
   - `git mv .claude/commands/and-protolines-season-v2.md archive/commands/and-protolines-season-v2-pre-substance.md` (if present)
   - `git mv design/shoot-v2/rubric-tensometer.md archive/rubrics/rubric-tensometer-replaced-by-substance.md`
   - Update `archive/commands/README.md` and (new) `archive/rubrics/README.md`.
   - Update `/and-facets` command body to drop tensometer from R1/R2 fanout + facet list. Update CLAUDE.md's URI-026 shared-resources line to remove tens-rubric reference.
5. **Write new + overhauled commands** in pipeline order:
   - `.claude/commands/and-project.md`
   - `.claude/commands/and-series.md`
   - `.claude/commands/and-substance.md` (recursive; four levels; chunker only)
   - `.claude/commands/and-cast.md`
   - `.claude/commands/and-write.md` (bones crafter; carries five-pass SVO pipeline + substance bone-gate)
   - `.claude/commands/and-review.md` (universal review primitive; subcommand router)
   - `.claude/commands/and-judge-book.md` (orchestrator-critic verdict)
   - `.claude/commands/and-wrap.md`
6. **Update CLAUDE.md.** New command table rows; `/and-season` removed; primary-pattern line updated to the new chain; substance framework added to schemas/authority section.
7. **Commit + push** to `claude/improve-story-substance-CVi58` at logical breakpoints.

---

## Out of scope

- **Retrofitting flea-bottom-dance.** Current active project keeps its state. New chain applies to the next `/and-project` run.
- **Facet rubric changes — partial.** Bones and facets (feeling, memory-flags, scene-map, dialogue, exposition, etc.) are preserved. **Tensometer is removed** — its purpose (per-bone substance-density signal) is now served directly by the substance contract + scene-level bone-gate. `/and-facets` no longer emits a tensometer file; `design/shoot-v2/rubric-tensometer.md` is archived; CLAUDE.md's "shared reviewer resources" line (URI-026) is updated to drop the tens rubric. The Tens-gate in URI-026 is replaced by the substance bone-gate at `/and-substance scene` Phase 5.
- **Impersonator card "values block."** Deferred — follow-on card-schema task after one full new-chain run.
- **Shoot-v2 chain overhaul.** `/and-facets` and `/and-stitch` unchanged structurally. `/and-facets` drops tensometer from its R1/R2 fanout. They operate on the per-chapter bones files `/and-write` emits.
- **Persona library expansion for non-audience staff.** `/and-project` records library-default version; substantive variant composition is a follow-on.

---

## Open questions for user

1. **Archive suffix.** `-pre-substance` for `/and-project` + `/and-wrap`; `-dissolved` for `/and-season`. OK?
2. **Universal axis set.** `design/substance/README.md` ships with 9 universal axes (wealth, health, community, emotional, capability, knowledge, reputation, agency, trust). Add / remove?
3. **Chunk-Δ defaults.** Default ratio (series Δ ≥ 6 ranks, book Δ = 2–3, chapter Δ ≈ 1, scene Δ = 0–1). Close enough for first run, or calibrate now?
4. **`/and-substance --cascade` default.** Recommend default OFF (manual level-by-level invocation preserves per-level review checkpoints and dispatch budget). `--cascade` as opt-in for late-stage runs. Confirm?
5. **Orchestrator-critic firing point.** Settled on **separate `/and-judge-book <slug>` command** — fires when both `/and-substance book` (all chunks) and `/and-write` (all chapter bones files) are complete. Cleaner than auto-firing inside `/and-substance book`, since the gate genuinely depends on `/and-write` output that `/and-substance` doesn't produce. Confirm?
6. **Series-end shape values.** Five: definitive / open-ended / ambiguous / tragic / triumphant. Add / remove?
7. **Cyclical book semantics.** Cyclical applies to protagonist-perspective axes only (world axes can drift across cyclical books — HP pattern; Hogwarts evolves while Harry resets). Confirm?
8. **Re-run modes naming.** `revise` / `add` / `redo`. Acceptable, or different verbs (`amend` / `extend` / `restart`)?
9. **Vocabulary refactor scope.** "Season"/"episode" language still appears in legacy schemas, the shoot-v2 chain (`/and-protolines`, `/and-facets`, etc.), CLAUDE.md, and design docs. Recommended scope: **reading-context** — rename in command bodies, schemas, design docs, CLAUDE.md, and memory file templates the model reads while authoring. Keep filesystem slugs (`s01e01.md` style) and existing in-flight project state alone. Confirm scope, or wider (filesystem too) / narrower (just removed-command bodies)?

---

## Verification on completion

- `design/substance/{README,questionnaire,delta-targets}.md` exist; README documents the recursive design at all four levels.
- `schemas/showrunner-memory.schema.md` updated with `project:` block, restructured `series:`, `books[]` nesting down to scenes + bones-file pointer.
- `archive/commands/and-project-pre-substance.md`, `and-season-dissolved.md`, `and-wrap-pre-substance.md`, `and-protolines-pre-substance.md` exist (plus v2 variants if present).
- `archive/rubrics/rubric-tensometer-replaced-by-substance.md` exists; `design/shoot-v2/rubric-tensometer.md` gone.
- `/and-facets` command body no longer emits tensometer; CLAUDE.md URI-026 line no longer references tens rubric.
- `.claude/commands/and-{project,series,substance,cast,write,review,judge-book,wrap}.md` exist and parse.
- `/and-review` parses all router subcommands (chunk / contract / signature / bones / facets / prose / cast / consistency / tree / feedback); reports persist to `staff/reviews/`.
- No active `.claude/commands/and-season.md` or `.claude/commands/and-protolines*.md`.
- `/and-substance` command body contains NO bone-writing logic (chunker only — produces chunks + contracts, persists to memory).
- `/and-write` command body contains NO chunk authoring (reads beat chunks as input; produces bones only).
- `.claude/commands/and-{project,series,substance,cast,wrap}.md` exist and parse.
- No active `.claude/commands/and-season.md`.
- `archive/commands/README.md` updated.
- `CLAUDE.md` updated — `/and-season` row removed, new rows for `/and-series`, `/and-substance`, `/and-cast`; primary-pattern line reflects new chain.
- Each new command's Phase 0 validates upstream and supports re-run modes (except `/and-project`, which hard-aborts).
- Commit + push lands clean on `claude/improve-story-substance-CVi58`.
