# Substance Overhaul — Implementation Plan

**Status:** DRAFT, 2026-05-16 (revised 2026-05-17). Awaiting user approval before execution.

**Revision 2026-05-17 (post intent-gaps audit):** beat level dropped; bones are now scene-children with their own per-bone state-delta, authored by `/and-write` during scene-decomposition. `/and-substance` shrinks from four invocation levels to three (`series` / `book` / `chapter`); the former `/and-substance scene` is absorbed into `/and-write` Phase 1. Scene-conflict block added to scene chunks. `SUBSTANCE-FLAT` classified HARD at the bone-gate. Scenes default to 1–3 per chapter. See `intent-gaps.md` for the surrounding rationale.

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

Bake a **declared, measurable, auditable substance contract** into the pipeline at every level of resolution (series → book → chapter → scene chunks, plus per-bone state-deltas inside each scene), so that:

- Every project has its scope (constraints/settings/themes) and staff (personas for planning/reviewing/editing/judging) explicitly bound before any content is authored.
- Every series has a brief substance-bearing chunk (Star-Wars-trilogy-style paragraph) plus structural commitments (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape).
- Every series has a substance signature (state axes + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets).
- Every cast is assembled to deliver named substance commitments.
- **One recursive command (`/and-substance`) authors substance and structure at every chunk level below series, stopping at scene** — book→chapter, chapter→scene. Each level fires its own review. /and-substance replaces the previous `/and-season` and is the chunker authoring chain from the series signature down to scene chunks.
- **Bones are scene-children that carry their own state-delta.** `/and-write` decomposes each scene into bones, each bone declaring one or two axis-movements with declared cost. The bone IS the beat — what used to be a separate "beat chunk" planning level is collapsed into the bone itself, authored by `/and-write` during scene decomposition.
- Every polished prose pass is audited for whether the substance lands (felt by audience, traceable to bones by auditor).

**Clean split between chunkers and bones.** `/and-substance` is a **chunker only** — it authors chunks at four levels (series → book → chapter → scene) and attaches a substance contract to each (Δ axes, costs, density target). It stops at scene chunks; it does NOT write SVO bones and does NOT decompose scenes into bones. Bones are authored by **`/and-write`** (renamed from `/and-protolines`), which reads scene chunks + their substance contracts and produces SVO bones — each bone carrying its own declared axis-movement (its per-bone state-delta) plus the SVO craft. This separation matters: chunking (how meaningful, what shifts, at what cost, in what nested unit) and bone-writing (decompose-scene-into-actions + subject-verb-object craft + line economy + continuity) are different jobs at different levels of resolution. Conflating them is the failure mode `/and-season` has today. The rename to `/and-write` also drops pipeline-jargon framing ("protolines") in favor of creative-writing language.

**Bones-grain principle: scene-action-sized, not micro.** A bone covers a meaningful scene-action — one declared axis-movement with declared cause. "Maya confronts her brother about the missing key, +2 community, −1 emotional" is one bone. A scene has 5–15 bones; each one earns its place by causing Δ. Chatter-bones (no declared Δ) do not survive Phase 4 trim. This directly addresses the user-feedback complaint that protolines were "too fine grained" — under the new contract, a bone-without-Δ is a schema violation, not a craft choice.

**Bones and facets preserved.** The shoot-v2 chain (bones → facets → stitcher) keeps its shape. `/and-write` consumes scene chunks instead of an "episode chunk," runs the existing five-pass SVO pipeline (inventory → constraint → shape → trim → continuity) with a new scene-decomposition pass at the front, and emits the per-chapter bones file that `/and-facets` and `/and-stitch` consume. **Exception:** the **tensometer facet is dropped** — the substance contract (per-bone Δ + per-scene aggregate + cost ledger + density target) is what tensometer was reaching for, more directly and with declared cause. Tensometer is removed from `/and-facets` output and its rubric is archived; URI-026 "tens-gate" is replaced by the **substance bone-gate** as a pass inside `/and-write`, which verifies the bones actually deliver the declared substance contract and that aggregate scene-Δ matches the scene's contract.

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
                                  ← fires once per chapter; deepest chunker level
  ↓
/and-write b01c01 (decomposes each scene into bones with per-bone Δ;
                   produces SVO bones; substance bone-gate)
                                  ← fires once per chapter
  ↓
/and-facets b01c01 (per-facet runners; tensometer dropped)
  ↓
/and-stitch b01c01 (unchanged; eight-phase prose render → draft/<chapter>.md)
  ↓ [optional /and-review at any point for spot-checks / verdicts]

[final-edits / polish / ship-ready manuscript: deferred until upstream is proven]
```

**Six live commands; three removed; one renamed.**

| command | status | scope |
|---|---|---|
| `/and-project` | **overhauled (shrinks)** | Scope + staff binding. No story content. |
| `/and-series` | **net new** | Series chunk (Star-Wars-style paragraph) + structural prompts (book count, length, cyclical, POV, cross-book continuity, world evolution, series-end shape). |
| `/and-substance` | **net new, recursive** | Single command body, fires at three invocation levels (`series`/`book`/`chapter`). Authors chunks + substance contracts at the four chunk levels (series, book, chapter, scene). Stops at scene chunks — does NOT decompose scenes into bones and does NOT write bones. |
| `/and-cast` | **net new** | Cast roster + series-level human audit checkpoint. |
| `/and-season` | **DROPPED** | Chunking jobs absorbed by `/and-substance`; bone-writing + scene-decomposition jobs absorbed by `/and-write`. |
| `/and-write` | **renamed + substantively overhauled** (was `/and-protolines`) | NOT a simple rename: input shape changes (was "episode chunk" → now scene chunks with substance contracts from `/and-substance chapter` output), and `/and-write` now owns scene-decomposition (a job the prior plan parked at `/and-substance scene`). New scene-decomposition Phase authors bones-with-deltas from each scene; substance bone-gate verifies per-bone Δ + scene aggregate Δ + cost-paid. Runs five-pass SVO pipeline + decomposition + substance bone-gate. Emits per-chapter bones file. |
| `/and-review` | **net new** | Universal review primitive with subcommand router. Reviews anything (signature / chunk / contract / bones / facets / prose / cast / consistency / tree / feedback / verdict) on demand. Absorbs `/and-judge-book` (orchestrator-critic) via `verdict <book>` subcommand. |
| `/and-judge-book` | **DROPPED** | Absorbed by `/and-review verdict <book>`. |
| `/and-facets` | overhauled (light) | Tensometer facet removed from R1/R2 fanout. Otherwise unchanged. |
| `/and-stitch` | unchanged | Out of scope for this overhaul. Existing Phase 7 (editorial reflection) is what it is. Output is `draft/<chapter>.md` — the deliverable until upstream substance machinery is proven. |
| `/and-wrap` | **DROPPED** | Wasn't pulling its weight. Polish concerns deferred entirely until upstream chain is working end-to-end. |

### Why drop /and-judge-book and /and-wrap entirely

**`/and-judge-book`** existed to fire the orchestrator-critic verdict against a finished book. That's a single review type. `/and-review` is the universal review primitive — folding the verdict into `/and-review verdict <book>` consolidates the review surface. A separate command added a row in the table without separate value.

**`/and-wrap`** wasn't pulling its weight. Three phases (audience review, auditor pass, editor pass), but the editor pass produced marginal changes on top of what `/and-stitch`'s Phase 7 (editorial reflection) already did, and the audience+auditor phases were mandatory dispatch cost for a review the user might or might not want at that moment. Dropped outright.

**Polish / final-edits is deferred entirely as a concern.** The substance overhaul ships when the upstream chain — `/and-project` → `/and-series` → `/and-substance series` → `/and-cast` → `/and-substance` (recursive) → `/and-write` → `/and-facets` → `/and-stitch` — produces a draft that is *substantively right*. Prose polish, cross-chapter percussion, repetition culling across the book, ship-ready manuscript work: all of that waits until the substance machinery is proven. `/and-stitch` is **unchanged** by this overhaul (its existing Phase 7 editorial reflection is what it is); `/and-review prose <chapter>` and any prose-focused review subcommands are **deferred**. The chain ends at `draft/<chapter>.md`; that's the deliverable until upstream is trusted.

### Why drop /and-season entirely

The previous plan kept `/and-season` because building `/and-substance` recursively was a bigger upfront lift than wiring it at the series level alone. But `/and-season`'s actual job — book→chapter chunking + chapter→scene chunking + scene→bones expansion + per-level review — is *structurally* what `/and-substance` + `/and-write` now do (chunker recursion + scene-decomposition). Compressing it into one inline command is a leaky abstraction: it hides the recursive substance contract from the model (and from re-run protocol, and from staleness cascade). Build the chunker and the bones-crafter as separate primitives and the abstraction is clean: `/and-substance` operates the same way at every chunk level above scenes; `/and-write` owns everything below.

Secondary benefit: the "season"/"episode" framing dissolves. `/and-substance` operates on `book`/`chapter`/`scene` arguments. The model never reads "episode" while planning or authoring.

---

## Boundary table — what moves where

Four commands are being restructured: `/and-project` shrinks, `/and-season` is dissolved, `/and-wrap` is dropped without replacement, and `/and-protolines` is renamed-and-overhauled to `/and-write` (substantive change, not a rename — new input shape; see `/and-write` spec below).

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
| Phase 1 content beat authoring | `/and-substance book` Phase 3 (per-chapter chunks + per-chapter Δ) + `/and-substance chapter` Phase 3 (per-scene chunks + per-scene Δ) + `/and-write` Phase 1 (scene-decomposition: bones-with-deltas authored from each scene) |
| Phase 2 bone expansion (SVO writing) | `/and-write` Phases 2–4 (constraint audit → SVO craft → trim) |
| Phase 3 review sweeps (S1–S10, S11 substance) | chunk-quality reviews fire inside each `/and-substance` level (audience: meaningful? dramatist: shape? auditor: contract match?); decomposition + SVO + continuity reviews fire inside `/and-write`. |
| URI-026 bone-gate (tens-gate) | `/and-write` Phase 6 substance bone-gate — **replaces tens-gate**: per-bone axis-movement verification + per-scene aggregate Δ delivery + cost-paid check, against each scene's substance contract. Tens rubric retired. |
| Phase 6 orchestrator-critic verdict | `/and-review verdict <book-slug>` (subcommand of `/and-review`) — fires when both `/and-substance` (all chunks under the book) and `/and-write` (all chapter bones files) are complete for the book. |
| Phase 7 per-chapter file emission | `/and-write` Phase 7 (emit bones to `theater/bones/<book>-<chapter>.md`) |

After dissolution, no command body contains the literal word "season."

---

## Re-runnability

Every new command except `/and-project` is **re-runnable**. The authoring loop is: draft → review → revise → revise → settle. Hard-abort-on-existing would force manual state deletion to iterate, which is wrong for creative work.

| command | re-runnable? | re-run modes |
|---|---|---|
| `/and-project` | **NO** — exception | Phase 0 hard-aborts if scope already populated. Project scope is foundational; revising it requires a new project. (User-confirmed.) |
| `/and-series` | yes | `revise` / `redo`. |
| `/and-substance` (any of the three invocation levels) | yes | `revise` (refine in place — same children, retune contracts), `add` (add new sub-chunks or axes/costs without touching existing), `redo` (replace all children — current set kept as prior to avoid). |
| `/and-cast` | yes | `revise` (swap/add/retire; new actors get fresh margit Phase 4 provisioning — working dir + LTM + STM + state + vibes; retired actors are decommissioned to `actors/<slug>-decommissioned-<timestamp>/`; untouched actors are left as-is) / `redo` (margit decommissions full current roster, full re-provisioning from scratch). |
| `/and-write` | yes | Per-chapter. `revise` (re-decompose specific scenes flagged SIGNAL by bone-gate, or re-write specific bone ranges) / `redo` (full rewrite — preserves scene chunks, replaces all bones). |
| `/and-review` | yes (idempotent) | Any subcommand can be re-fired any number of times. Each invocation persists a new timestamped report; nothing else is mutated. `verdict` subcommand updates `books[<slug>].orchestrator_critic_verdict` in place. |
| `/and-stitch` | yes (unchanged) | Per-chapter. Re-running re-runs the full eight-phase pipeline. No new revise mode in this overhaul. |

**Phase 0 protocol for re-runnable commands:**

1. Read upstream inputs. Abort if upstream missing.
2. Check own output. If populated, prompt mode (`revise` / `add` where applicable / `redo`).
3. Cascade warning. Surface downstream blocks that depend on what's about to change; offer staleness-marking (see "Surfacing" below).
4. Run.

**Surfacing — defined.** When Phase 0 detects downstream work that depends on the about-to-change output, "surface" means: (a) print a numbered list of the affected downstream artifacts (chunks, bones files, verdict block) with their slugs and last-write timestamps; (b) prompt the user to choose `mark-stale` (write `stale_since: <iso-timestamp>` on each affected downstream block; leave content intact) / `keep-fresh` (leave staleness fields null; user accepts that downstream may be silently outdated) / `abort` (cancel the re-run). Default is `mark-stale`. The chosen mode is recorded in showrunner memory under `staff/showrunner/staleness-log.md` (one entry per cascade event: who-ran-what, what was marked, user choice).

When a downstream command next runs and reads a parent block with `stale_since` set, it prints a warning line ("parent <slug> stale since <timestamp>; consider re-running parent first") but does NOT block. Stale-marking is informational, not enforcing.

**Staleness cascade across /and-substance levels + /and-write.** Re-running `/and-substance series` `redo` stale-marks every `/and-substance book` output. Re-running `/and-substance book b01` `redo` stale-marks every `/and-substance chapter` under b01. Re-running `/and-substance chapter b01c01` `redo` stale-marks every `/and-write` bones file whose source scenes sit under b01c01. Each level's `stale_since: <iso-timestamp>` field is surfaced when that level next runs. No silent overwrites of downstream work.

**Staleness also invalidates the orchestrator-critic verdict.** Any `/and-substance` or `/and-write` re-run whose scope is at-or-under a book that already has an `orchestrator_critic_verdict.ruling` set MUST stale-mark that verdict block (`books[<slug>].orchestrator_critic_verdict.stale_since: <iso-timestamp>`). A PASS verdict sitting on top of substance that has been redone underneath is a false signal; the stale flag forces re-judgment via `/and-review verdict <book>` before the verdict is trusted again. `/and-review verdict` Phase 0 warns (not blocks) if it sees an existing stale verdict; re-running it clears the stale flag on PASS/PASS-WITH-NOTES/FAIL re-issue.

---

## Archive plan

```
git mv .claude/commands/and-project.md      archive/commands/and-project-pre-substance.md
git mv .claude/commands/and-season.md       archive/commands/and-season-dissolved.md
git mv .claude/commands/and-wrap.md         archive/commands/and-wrap-dissolved.md
git mv .claude/commands/and-protolines.md   archive/commands/and-protolines-pre-substance.md
# and-protolines-v2 and and-protolines-season-v2: archived alongside; replaced by /and-write
```

`/and-season` and `/and-wrap` use the `-dissolved` suffix to mark they aren't coming back — their jobs moved into other commands (`/and-substance` + `/and-write` for season; `/and-review` + `/and-stitch` Phase 7 for wrap). `/and-project` and `/and-protolines` are overhauls/renames; their pre-overhaul versions stay reachable via `-pre-substance`.

`/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-review` are net new — nothing to archive (other than `/and-protolines` which is the predecessor to `/and-write`).

Update `archive/commands/README.md`:

> **2026-05-16 — substance overhaul.** Two reasons. (1) The pre-substance chain optimized per-line craft, dramatic shape, mechanic discipline, continuity, and prose economy — but had no declared substance contract; episodes shipped through it were structurally clean and substance-flat. (2) `/and-project` conflated scope with series content; `/and-season` conflated recursive chunking (book→chapter→scene) with bone-writing and emission; `/and-wrap`'s editor pass produced marginal lift on top of `/and-stitch`'s existing Phase 7 editorial reflection. Replacement chain: `/and-project` (scope+staff) → `/and-series` (series chunk + structural prompts) → `/and-substance series` (signature + per-book Δ) → `/and-cast` (roster) → series-level audit checkpoint → `/and-substance book/chapter` (recursive chunker authoring; three invocation levels; four chunk levels stopping at scene) → `/and-write` (scene-decomposition into bones-with-deltas + five-pass SVO + substance bone-gate; replaces `/and-protolines`) → `/and-facets` (tensometer dropped) → `/and-stitch` (unchanged). The bone is the smallest substance unit — it carries its own declared axis-movement; the former "beat chunk" planning level is collapsed into the bone itself. `/and-review` is the universal review primitive with subcommand router (includes `verdict <book>`, absorbing the former `/and-judge-book`). Dissolved: `/and-season` (into `/and-substance` + `/and-write`); `/and-wrap` (polish concerns deferred entirely until upstream substance machinery is proven; `/and-stitch`'s `draft/<chapter>.md` is the terminal deliverable); `/and-judge-book` (into `/and-review verdict`). Renamed-overhauled: `/and-protolines` → `/and-write`. URI-026 tens-gate replaced by `/and-write` substance bone-gate; tensometer facet retired. See `design/substance/`.

---

## New artifacts

### `design/substance/README.md`

Framework reference. Authoring authority for substance terminology, state-axis catalog, 1–9 scale anchors, Δ/cost/density definitions, plot-by-states + plot-by-action duality, perspective-bound measurement, antagonist-pressure, failure-mode catalog, pipeline-threading map. **Includes the recursive `/and-substance` design at three invocation levels** (`series` / `book` / `chapter`) producing four chunk levels (series → book → chapter → scene), **plus the `/and-write` scene-decomposition principle**: the bone IS the smallest substance unit (each bone carries one axis-movement with declared cause), `/and-write` decomposes scene chunks into bones, the former "beat chunk" planning level is collapsed into the bone itself.

### `design/substance/questionnaire.md`

1–9 archetype questionnaire (story / protagonist / world / antagonist) used by `/and-substance` at any level to pin axis ranks honestly. Per-archetype question banks. Example scoring trace.

### `design/substance/delta-targets.md`

Per-chunk Δ targets + bone-count bands.
- Series-scale Δ across the signature.
- Book-scale Δ per book by position (opening / mid / climax / denouement).
- Chapter-scale Δ.
- Scene-scale Δ.
- Per-bone Δ — typical magnitude (one axis +/− one rank; occasionally two axes); guidance on when a bone earns more.
- Bones-per-scene target (5–15 default), scenes-per-chapter target (1–3 default — scenes are substantial, per user feedback).
- Curve commentary: density is a curve across a chunk, not a constant. Within a scene, bones cluster — opening bones may be lower-Δ (setup), climactic bones higher-Δ (the scene's hinge action).

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
    book_length:
      chapters_per_book: <range>           # e.g. 4-8
      scenes_per_chapter: <range>          # e.g. 1-3 — scenes are substantial; per user feedback "a scene should be most of a chapter"
      bones_per_scene: <range>             # e.g. 5-15 — bones are scene-action-sized; each bone declares one axis-movement
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
        anchor:                                # fine-grained anchor; populate from the level where the cost is paid
          book: <book-slug>
          chapter: <chapter-slug> | null       # null when cost spans the whole book
          scene: <scene-slug> | null           # null when cost spans the whole chapter
        # `/and-write` Phase 6 (substance bone-gate) verifies "for each scene under the chapter:
        # cost-ledger entries are paid by visible bones" — that check resolves against the
        # finest-grained anchor populated. Authored top-down: `/and-substance series` writes
        # book-anchored entries; `/and-substance chapter`/`scene` may refine them by populating
        # the deeper fields. See `design/substance/README.md` for the refinement protocol.
    antagonist_pressure:
      - axis: <axis-slug>
        pressure_source: <one line>
        cost_curve: <one line>
    chunk_targets:
      series:  { delta_per_signature_axis: <range>, density_target: <range> }
      book:    { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      chapter: { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      scene:   { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
      bone:    { delta_per_axis: <range>, axes_per_bone: <range> }   # typical 1-axis ±1 rank; occasionally 2-axis

  # from /and-cast
  cast_roster: [...]
  stage_elements: [...]
```

Recursive nesting under `books[]` (replaces `seasons[]`). Each chunk-count decision lands at its parent's invocation: `/and-substance series` decides `books[*].structure.chapter_count`; `/and-substance book` decides `chapters[*].structure.scene_count`. Scenes are the deepest chunker output; `/and-write` decomposes each scene into `bones[]` with per-bone deltas at write-time. Counts must fall inside the ranges declared in `series.structure.book_length`.

```yaml
books:
  - slug: b01
    chunk: |
      <book chunk authored by /and-substance series>
    structure:                             # populated by /and-substance series Phase 2
      chapter_count: <N>                   # picked inside series.structure.book_length.chapters_per_book
    substance_delta:                       # from /and-substance series Phase 3
      axes_in_motion: [...]
      density_target: <range>
    stale_since: <iso-timestamp> | null    # set when /and-substance series re-runs with `redo` after persistence
    # from /and-substance book
    drama: |
      <"what cannot survive this book" statement>
    chapters:
      - slug: b01c01
        chunk: |
          <chapter chunk authored by /and-substance book>
        structure:                         # populated by /and-substance book Phase 2
          scene_count: <N>                 # picked inside series.structure.book_length.scenes_per_chapter
        substance_delta:                   # from /and-substance book Phase 3
          axes_in_motion: [...]
          density_target: <range>
        stale_since: <iso-timestamp> | null
        # from /and-substance chapter
        dramatic_shape: <rising | climax | falling | hinge | ...>
        scenes:
          - slug: b01c01s01
            chunk: |
              <scene chunk authored by /and-substance chapter — substantial; one scene typically fills most of a chapter>
            substance_delta:               # from /and-substance chapter Phase 3
              axes_in_motion: [...]
              density_target: <range>
            scene_conflict:                # from /and-substance chapter Phase 3 — sibling of substance_delta; added per user-feedback "scenes should have meaningful suspense and action with something against something"
              protagonist_force: <one line>
              opposing_force: <one line>
              stakes_axis: <axis-slug>
            stale_since: <iso-timestamp> | null
            bones:                         # from /and-write Phase 1 (scene-decomposition)
              - slug: b01c01s01n01        # n-prefix for bones (b would collide with book)
                svo: |
                  <one-line subject-verb-object bone — scene-action-sized; e.g. "Maya confronts Tomas about the missing key.">
                substance_delta:           # per-bone — the smallest substance unit
                  axis_moves:
                    - axis: <axis-slug>
                      direction: + | -
                      magnitude: <1-3>     # typical ±1; ±2-3 for hinge bones
                  cost:                    # may be null when the bone is paying a prior gain rather than incurring new cost
                    axis: <axis-slug> | null
                    direction: -
                    magnitude: <1-3>
                  cost_ledger_anchor: <cost-ledger-entry-id> | null  # link to series.substance.cost_ledger when this bone pays one
                facet_tags: [feeling, dialogue, memory-flag, ...]   # optional pre-tagging for /and-facets
                gate_verdict:              # filled by /and-write Phase 6
                  bonefide: true | false   # does the SVO actually cause the declared Δ?
                  flat: false | <axis>     # SUBSTANCE-FLAT on this bone
        # chapter-level fields filled by /and-write
        bones_file: theater/bones/b01-c01.md
        bones_count: <N>
        substance_bone_gate_verdict: PASS | FAIL-<reason>
        substance_delta_measured:          # post-bones aggregate
          axes_moved: [...]
          density_measured: <ratio>
          felt_verdict: SUBSTANCE-FELT | SUBSTANCE-FLAT-<axis> | SUBSTANCE-SUSPECT-cheap-gain-<axis>
    # book-level field filled by /and-review verdict <book-slug>
    orchestrator_critic_verdict:
      ruling: PASS | PASS-WITH-NOTES | FAIL
      report_path: staff/reviews/verdict-<book-slug>-<timestamp>.md
      verdict_at: <iso-timestamp>
      stale_since: <iso-timestamp> | null   # set when any /and-substance or /and-write under this book re-runs after the verdict was recorded
```

**Bones as scene-children, not flat-per-chapter.** The source of truth is `chapters[].scenes[].bones[]` in showrunner memory. The per-chapter file `theater/bones/<book>-<chapter>.md` is a **flattened view** emitted by `/and-write` Phase 7 for downstream `/and-facets`/`/and-stitch` consumption — bones in scene order, with scene-boundary markers preserved (so the scene-map facet `/and-facets` derives can resolve every bone to its scene without extra lookup). If schemas and memory disagree, memory wins; the file is regenerated from memory.

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
2. Phase 1 — Structural prompts. Interactive: book count, book length (chapters per book + scenes per chapter + bones per scene), cyclical?, POV, cross-book continuity, world evolution, series-end shape. Persist to `series.structure.*`.
3. Phase 2 — Series chunk authoring. Screen-writer takes project scope + structure. Produces a brief substance-bearing prose paragraph (Star-Wars-trilogy-style). Substance implicit, not yet measured.
4. Phase 3 — Review. Audience + dramatist accept/revise loop (3-try cap).
5. Phase 4 — Persist `series.chunk` + `series.structure.*`. No checkpoint here.

Estimated size: ~150–200 lines.

### `/and-substance` (net new — recursive, three invocation levels)

**Four chunk levels exist** (series → book → chapter → scene); **three invocation levels** author them (`series` produces book chunks; `book` produces chapter chunks; `chapter` produces scene chunks). Scenes are produced but never invoke — they are the deepest chunks and are consumed by `/and-write`, which decomposes each scene into bones (the bones live in `scenes[].bones[]`; per-bone deltas are authored by `/and-write`, not `/and-substance`).

Single command body. Argument is the invocation level: `series` / `book <slug>` / `chapter <slug>`. Same seven-phase shape at every level.

**Common phases (every level):**

1. **Phase 0 — Validate + mode select.** Read upstream chunk + parent substance commitment. Abort if upstream missing. If own output populated, prompt `revise` / `add` (where applicable) / `redo`. If downstream chunks or `/and-write` bones exist, surface cascade + offer staleness-marking.
2. **Phase 1 — Read parent.** Series: read `series.chunk` + structural commitments. Book: read book chunk + per-book Δ. Chapter: read chapter chunk + per-chapter Δ.
3. **Phase 2 — Author sub-chunks.** One prose paragraph per child unit. Series → per-book chunks. Book → per-chapter chunks. Chapter → per-scene chunks (substantial; scenes typically fill most of a chapter, 1–3 scenes per chapter default).
4. **Phase 3 — Author sub-chunk substance contracts.** For each sub-chunk: which axes shift, direction, target Δ-magnitude, cost, density target. **Chapter level additionally authors per-scene `scene_conflict`** (protagonist_force / opposing_force / stakes_axis) so every scene has named opposition.
5. **Phase 4 — Level-specific extras.** Series: authors the signature itself (state axes, anchors, cost ledger, antagonist pressure). Book: authors the book drama statement. Chapter: authors the chapter dramatic shape (rising / climax / falling / hinge) and the chapter-arc completion line ("what changed by end of this chapter, in one sentence").
6. **Phase 5 — Chunk-quality review.** Audience + dramatist + auditor at this level. Accept/revise loop (3-try cap). **Audience:** does this chunk feel substantive — does the named Δ feel earned, the cost feel real, the meaningfulness land? `SUBSTANCE-FELT` vs `SUBSTANCE-FLAT-<axis>` vs `SUBSTANCE-SUSPECT-cheap-gain-<axis>`. **Dramatist:** is the chunk shape sound? Do the children fit within the parent's Δ? Scenes-not-too-small (chapter-level check)? Cyclical / cross-book / structural commitments honored? Chapter has dramatic-arc completion? **Auditor:** does the chunk text match the substance contract (no rank claim without described cause; cost-ledger consistency)?
7. **Phase 6 — Persist.** Write chunks + contracts to showrunner memory at this level's nesting depth. **No bones at any level** — bones are written by `/and-write`.

**`--cascade` flag (book/chapter levels).** Default off (manual level-by-level invocation). With `--cascade`, `/and-substance book b01` auto-fires `/and-substance chapter` for each chapter under b01, then `/and-write` for each chapter (each `/and-write` invocation reads the chapter's scenes and authors bones). Reviews still fire at each level; failure at any level halts the cascade. Useful for late-stage runs where the substance contract is settled and the user wants one command to drive everything to bones.

Estimated size: ~350–450 lines (recursive across three invocation levels; one fewer level than the prior plan).

### `/and-cast` (net new — cast roster + series audit checkpoint)

1. Phase 0 — Validate + mode select. Read `series.chunk` + `series.structure.*` + `series.substance.*`. Abort if upstream missing. If `series.cast_roster` populated, prompt `revise` (swap/add/retire — untouched actors are preserved as-is; added actors flow through Phases 1–4 normally; retired actors are decommissioned by margit to `actors/<slug>-decommissioned-<timestamp>/`; swapped actors are retire+add in one pass) / `redo` (margit decommissions the full current roster, then re-run Phases 1–4 from scratch).
2. Phase 1 — Substance-driven cast brief. Screen-writer composes brief from chunk + signature: which axes need which carriers. In `revise` mode, the brief is scoped to the requested swap/add/retire delta only.
3. Phase 2 — Margit candidate menu (filtered from `cards/personas/INDEX.md`). Skipped for actors being retired.
4. Phase 3 — Screen-writer selection + dramatist viability check. Viability check considers the full post-revise roster, not only the added actors.
5. Phase 4 — Margit provisioning (actor working dirs, LTM/STM/state/vibes). Fresh provisioning for every added actor; untouched actors keep their existing working dirs unchanged.
6. Phase 5 — Series-level audit checkpoint. Auditor (fork) against full picture (project scope + series chunk + structural commitments + signature + per-book Δ + cast). Result to user. On approval, `/and-substance book b01` next.

Estimated size: ~200–250 lines.

### `/and-write` (renamed + overhauled — was `/and-protolines`; the bones crafter)

Reads scene chunks + substance contracts produced by `/and-substance chapter`. **Decomposes each scene into bones-with-deltas, then SVOs them.** Produces the per-chapter bones file. Replaces `/and-protolines` as the shoot-v2 chain entry.

**Phases (per chapter):**

1. **Phase 0 — Validate + mode select.** Read all scene chunks under the chapter. Abort if any scene is unsubstanced (`substance_delta` missing or `scene_conflict` unpopulated). If `theater/bones/<book>-<chapter>.md` already exists, prompt `revise` (re-decompose specific scenes flagged SIGNAL by bone-gate, or re-write specific bone ranges) / `redo` (full rewrite — scene chunks preserved, all bones replaced).
2. **Phase 1 — Scene-decomposition (the work that used to be `/and-substance scene`).** For each scene chunk: decompose into N bones (within `series.structure.book_length.bones_per_scene` range, typical 5–15). Each bone declares one axis-movement (occasionally two) with declared cost and links to the cost-ledger when applicable. Bones are scene-action-sized — one scene-significant action per bone, not micro-beats. The scene's substance contract is the aggregation target: per-axis sum of bone-Δ must equal the scene's declared Δ within ±1 rank.
3. **Phase 2 — Constraint audit.** Verify each bone's declared Δ is well-formed (no rank claims without parent-cost backing; no axis movements outside the scene's contract; no costs unaccounted-for in the cost ledger). Verify aggregate-bones-Δ ≈ scene-Δ per axis.
4. **Phase 3 — Shape (SVO writing).** For each bone, author the SVO craft: subject-verb-object, line economy, voice-consistent. The bone's declared Δ is the cause-claim the SVO must visibly support.
5. **Phase 4 — Trim.** Drop bones that don't cause Δ (chatter bones — schema violation, not just style). Bones for setup/transition are allowed only if they pay a later gain (cost-ledger link required). Capped at density-target ratio.
6. **Phase 5 — Continuity audit.** State-thread check across bones (props move, actors track, conditions persist). Cross-scene continuity within the chapter (handoff from scene N to scene N+1).
7. **Phase 6 — Substance bone-gate.** **Replaces URI-026 tens-gate.** For each bone: verify the declared axis movement is **bonefide** (SVO actually causes named Δ; no rank claim without visible cause; otherwise `SUBSTANCE-FLAT-<axis>` HARD). For each scene: verify per-axis Δ delivered within ±1 rank of contract; verify `scene_conflict.opposing_force` is visible in the bones (something is *against* something). For each scene under the chapter: verify cost-ledger entries are paid by visible bones (`SUBSTANCE-SUSPECT-cheap-gain-<axis>` HARD if cost not visible). Audience review (3 personas) per scene window: `SUBSTANCE-FELT` PASS / `SUBSTANCE-FLAT-<axis>` HARD / `SUBSTANCE-SUSPECT-cheap-gain-<axis>` HARD. **HARD/SIGNAL classification:** flat-bones, cost-not-paid, missing-opposing-force, per-axis-Δ-mismatch-beyond-±2 → HARD (blocks emission). Bones-count-below-density-target, per-axis-Δ-mismatch-within-±1-to-±2, chatter-bones-just-over-cap → SIGNAL (records but passes).
8. **Phase 7 — Emit + downstream-gate pre-verify.** Write bones to `active-project/theater/bones/<book>-<chapter>.md` (flattened scene-ordered view of `chapters[].scenes[].bones[]` in memory; source of truth stays in memory). Before write, pre-verify the two downstream `/and-facets` gates so this command HARD-aborts rather than letting `/and-facets` Phase 0 abort later: (a) **URI-DIALOGUE-COVERAGE-GATE** — every `speaks to` bone has an addressee and a speaker resolvable from the cast roster; the file shape supports per-character dialogue file emission downstream. (b) **URI-SCENE-WINDOW** — every bone is taggable to exactly one scene slug under the chapter (no dangling anchors, no scene-spanning bones); the scene-map facet `/and-facets` will derive can resolve every bone. Both pre-verifications are HARD findings at this Phase; SIGNAL versions are tolerated and recorded. File ready for `/and-facets`.

Estimated size: ~400–500 lines (scene-decomposition + five-pass SVO pipeline + substance bone-gate + emission). The size grew vs. the prior plan because `/and-write` absorbs scene-level decomposition that was previously parked at `/and-substance scene`.

### `/and-review` (net new — universal review primitive with subcommand router)

Top-level router dispatches to one of N pre-defined review types. No authored writes; reports persist to `staff/reviews/<type>-<target>-<timestamp>.md`.

**Router subcommands:**

| subcommand | target | fires | what it reviews |
|---|---|---|---|
| `/and-review chunk <slug>` | any chunk slug (series / b01 / b01c01 / b01c01s01) | audience + dramatist + auditor | Does the chunk match its substance contract? Is it the right depth for its level? Does it feel meaningful? Cost language honest? For scene-level: is `scene_conflict` populated and concrete? |
| `/and-review bone <slug>` | bone slug (b01c01s01n01) | auditor + audience-fork | Does the SVO actually cause the declared Δ (bonefide check)? Is the cost real (cost-ledger anchored)? Substance-flat? |
| `/and-review contract <slug>` | any chunk slug | dramatist + auditor | Is the substance contract well-formed? Do per-axis Δ-magnitudes sum correctly to parent? Cost-ledger consistent? No rank claims without backing? |
| `/and-review signature` | series only | audience + dramatist + auditor | Series signature health: are the axes the right axes? Anchors honest? Cost ledger paid across the arc? Antagonist pressure named per axis? |
| `/and-review bones <chapter-slug>` | chapter slug | bones critics (SVO craft) + bone-gate logic | Per-bone axis-movement bonefide? Per-scene Δ delivered? Cost-paid? `SUBSTANCE-FELT`/`-FLAT` per scene. |
| `/and-review facets <chapter-slug>` | chapter slug | per-facet rubric runners | Facet-by-facet review against rubric. |
| `/and-review prose <chapter-slug>` | chapter slug | audience + auditor | **DEFERRED.** Felt-substance per scene + `SUBSTANCE-COVERAGE` audit on rendered prose. Not in scope until upstream chain produces drafts the user wants to spot-check. Listed here so the eventual subcommand has a home, but skipped during initial build. |
| `/and-review cast` | — | dramatist + auditor | Roster substance-fit: does the roster have carriers for every signature axis perspective? Viability check. |
| `/and-review consistency [<root-slug>]` | optional root (defaults to series) | dramatist + auditor | Cross-level: do per-book Δ aggregates sum to series Δ? Do chapter dramatic shapes honor book drama? Do scene contracts fit within chapter contract? Cost-ledger entries paid? Cyclical commitments honored? |
| `/and-review tree [<root-slug>]` | optional root | all of the above, scoped to the subtree | Full sweep at and below root. Defaults to whole series. |
| `/and-review feedback <feedback-file> [<root-slug>]` | feedback file + optional root | audience + auditor | Re-fires reviewers carrying named feedback as context. Use case: "review s01 against `active-project/feedback.md`." |
| `/and-review verdict <book-slug>` | book slug | orchestrator-critic | Fires the orchestrator-critic (`staff/orchestrator-critic/card.md`) against book-scope output. Phase 0 HARD-aborts if: (a) the book has no `chunk`, no `drama`, or no `chapters[]` populated; (b) any chapter under the book is missing `chunk`, `dramatic_shape`, `scenes[]`, or any scene is unsubstanced (missing `substance_delta` or `scene_conflict`); (c) any chapter under the book has no `bones_file` recorded or that file does not exist on disk, or any scene under any chapter has empty `bones[]`; (d) the orchestrator-critic card version recorded in `project.staff.orchestrator_critic` is missing from the library. On pass, dispatches the critic against chunks at every level + bones for every chapter + rendered prose if present. Verdict PASS / PASS-WITH-NOTES / FAIL persisted to `books[<slug>].orchestrator_critic_verdict.ruling`; report path + timestamp written alongside. Absorbs the former `/and-judge-book`. |

**Common phases (every subcommand):**

1. Phase 0 — Parse subcommand. Validate target exists in memory / on disk.
2. Phase 1 — Compose review brief specific to subcommand (which reviewers, what rubric, what scope).
3. Phase 2 — Dispatch reviewers in parallel (audience persona forks per persona; dramatist; auditor).
4. Phase 3 — Aggregate findings into a structured report. Classify HARD / SIGNAL / TASTE per the existing auditor taxonomy.
5. Phase 4 — Persist report to `staff/reviews/<subcommand>-<target>-<timestamp>.md`. Surface to user. Optionally offer to materialize findings into a fix queue for the appropriate authoring command (e.g., HARD findings on `chunk b01c03` → fix queue for `/and-substance chapter b01c03 revise`).

**Relationship to inline reviews.** Authoring commands (`/and-substance` Phase 5, `/and-write` Phases 5/6, `/and-cast` Phase 5) still have inline review *gates* that catch problems before persistence — `/and-write` Phase 5 is continuity, Phase 6 is the substance bone-gate. `/and-review` is for AFTER persistence — going back to spot-check or sweep on demand. Same reviewer infrastructure (audience cards, dramatist, auditor) is shared. The inline gates can call into the same review subroutines `/and-review` dispatches.

**`/and-cast` Phase 5 vs `/and-review tree --series-scope`.** The series-level audit checkpoint inside `/and-cast` is a synchronous blocking gate (the command body owns it; on FAIL the command halts before persisting cast handoff). `/and-review` is post-hoc — fires after persistence, never blocks an authoring command's own flow. They share auditor infrastructure but are not interchangeable: keep the inline auditor fork inside `/and-cast` Phase 5; use `/and-review tree` for later spot-checks against the same scope.

Estimated size: ~300–400 lines (the router + N subcommand implementations; each subcommand is small because the reviewers do the heavy lifting).

### `/and-stitch` (unchanged — out of scope for this overhaul)

Eight-phase pipeline (lens-anchored render → redundancy cull → compression → voice transform → local flow → buildup preservation → editorial reflection → finalize). Output `draft/<chapter>.md` (clean) + `draft/<chapter>.annotated.md` (traced). The clean draft is the deliverable until upstream substance machinery is proven and the user wants to revisit polish.

No `revise --feedback` mode, no Phase 7 substance-allowed-moves enhancement. Both flagged in earlier plan drafts; both deferred.

---

## Decisions on spec gaps (resolved 2026-05-16 post-audit)

These were flagged as IMPORTANT spec gaps in the self-audit. Resolved in-plan rather than escalated to user, per "act independently" directive. Each decision should be re-confirmed at plan approval.

### Vibe-clouds under recursive substance

**Decision: keep series + book vibe-clouds; deprecate chapter/scene/bone vibes.** Substance contracts now carry the explicit-substance role vibes were biasing toward implicitly; preserving vibes at every recursive level would double up with no obvious lift and would blow up the dispatch budget. Series and book vibes remain because they carry tone/mood/genre-feel that substance contracts don't capture directly (e.g. "noir," "wry," "fairytale" — biasing word-choice, not measurable Δ).

- `/and-series` continues to author a series-level vibe-cloud as part of the series chunk.
- `/and-substance series` continues to author per-book vibe-cloud entries when authoring book chunks.
- `/and-substance chapter` and `/and-write` do NOT author vibe-clouds; chapter/scene/bone-level shaping comes from the substance contract.
- CLAUDE.md "Memory rules" line about vibe-clouds is updated to: "Vibe-clouds are built at series and book level. Both are active during authoring; book-level takes priority on key conflicts."

### URI gates compatibility from `/and-write`

**Decision: `/and-write` Phase 7 pre-verifies URI-DIALOGUE-COVERAGE-GATE and URI-SCENE-WINDOW before emission.** See `/and-write` spec Phase 7 above. Pre-verification HARD-aborts `/and-write` rather than letting `/and-facets` Phase 0 abort later; the abort surface stays close to the bone-writing pass that introduced the violation.

### Verdict block staleness invalidation

**Decision: any `/and-substance` or `/and-write` re-run scoped at-or-under a book stale-marks that book's `orchestrator_critic_verdict` block.** See "Staleness cascade" section above. The verdict's `stale_since` field forces re-judgment via `/and-review verdict <book>` before the verdict is trusted again.

### `/and-cast` Phase 5 stays inline

**Decision: keep the inline auditor fork; `/and-review tree --series-scope` is the post-hoc spot-check, not a replacement.** See `/and-review` "Relationship to inline reviews" subsection above.

### `/and-cast revise` provisioning

**Decision: new actors get fresh margit Phase 4 provisioning; untouched actors are left as-is.** See `/and-cast` Phase 0 and re-runnability table.

### Staleness "surfacing" behavior

**Decision: surfacing prints affected downstream artifacts with timestamps + prompts user for `mark-stale` / `keep-fresh` / `abort`; default `mark-stale`; choice logged to `staff/showrunner/staleness-log.md`; downstream commands warn (do not block) on stale parents.** See "Surfacing — defined" subsection above.

---

## Notes on deferred concerns

Items flagged as DEFER in the self-audit. Not blockers; recorded so the implementer knows the team is aware.

- **Dispatch budget.** Naive worst case under the revised plan (6 books × 6 chapters × 3 scenes × per-level reviews ×3 retries, plus per-chapter `/and-write` with internal bone-gate dispatches) is in the low hundreds of subagent dispatches per series — meaningfully lower than the prior plan's beat-level recursion (which multiplied dispatches by an additional 5× per scene). Mitigations available: per-level review parallelism (audience personas + dramatist + auditor fire concurrently — already the pattern), lower retry caps for `/and-write` revisions (capped at 2 instead of 3 since revise is targeted), `--cascade` flag with checkpoint flush every chapter (so `/and-cut` can resume). Treat as observation, not a redesign blocker; revisit after first end-to-end run produces real numbers.
- **`/and-cut` interaction.** `/and-substance --cascade` should checkpoint after every chapter completes (i.e. after `/and-substance chapter` finishes a chapter's scenes, or after `/and-write` finishes a chapter's bones — whichever the cascade is currently at). `/and-cut` mid-cascade saves the resume point (`next: /and-write b01c04` or `next: /and-substance chapter b01c05`). Detail to land in the `/and-substance` command body, not in this plan.
- **Filesystem migration.** Active project `flea-bottom-dance` is out-of-scope; its existing `theater/proto-lines/...` layout is left alone. New projects use `theater/bones/<book>-<chapter>.md`. No migration script needed.
- **Estimated sizes are loose.** `/and-substance` 350–450 lines (three invocation levels) and `/and-write` 400–500 lines (decomposition + SVO pipeline + bone-gate) are working estimates. Total command-body line count under the revised plan is similar to the prior plan — work just shifted from `/and-substance` to `/and-write`. Not a blocker — size will be what it is.

---

## Order of operations

1. **Plan approval.**
2. **Design docs.** `design/substance/README.md` (incl. full recursive design at three invocation levels / four chunk levels + the bone-is-the-beat principle) + `questionnaire.md` + `delta-targets.md`.
3. **Schema updates.**
   - `schemas/showrunner-memory.schema.md` — `project:` block, restructured `series:` with substance subblock, `books[]` nesting (chapters, scenes, scene_conflict block, scenes[].bones[] with per-bone state-delta, chunk-count fields at each authoring level, `bones_file` pointer, `stale_since` at each level, structured `orchestrator_critic_verdict` block).
   - `git mv schemas/proto-line.schema.md schemas/bones.schema.md` — rename to match `/and-write` output naming. Update internal references in the schema body (s/proto-line/bone/g where it refers to the unit itself; keep historical references in archived schemas alone). Update CLAUDE.md's schema authority table accordingly.
4. **Archive current commands + tensometer rubric.**
   - `git mv .claude/commands/and-project.md      archive/commands/and-project-pre-substance.md`
   - `git mv .claude/commands/and-season.md       archive/commands/and-season-dissolved.md`
   - `git mv .claude/commands/and-wrap.md         archive/commands/and-wrap-dissolved.md`
   - `git mv .claude/commands/and-protolines.md   archive/commands/and-protolines-pre-substance.md`
   - `git mv .claude/commands/and-protolines-v2.md archive/commands/and-protolines-v2-pre-substance.md` (if present)
   - `git mv .claude/commands/and-protolines-season-v2.md archive/commands/and-protolines-season-v2-pre-substance.md` (if present)
   - `git mv design/shoot-v2/rubric-tensometer.md archive/rubrics/rubric-tensometer-replaced-by-substance.md`
   - Update `archive/commands/README.md` and (new) `archive/rubrics/README.md`.
   - Update `/and-facets` command body to drop tensometer from R1/R2 fanout + facet list. Update CLAUDE.md's URI-026 shared-resources line to remove tens-rubric reference.
5. **Write new + overhauled commands** in pipeline order:
   - `.claude/commands/and-project.md`
   - `.claude/commands/and-series.md`
   - `.claude/commands/and-substance.md` (recursive; three invocation levels stopping at chapter; chunker only)
   - `.claude/commands/and-cast.md`
   - `.claude/commands/and-write.md` (bones crafter; carries scene-decomposition + five-pass SVO pipeline + substance bone-gate)
   - `.claude/commands/and-review.md` (universal review primitive; subcommand router incl. `verdict`; `prose` subcommand stubbed-deferred)

   **Not touched:** `/and-facets` (light edit only — remove tensometer from R1/R2 fanout; no other changes) and `/and-stitch` (unchanged; still produces `draft/<chapter>.md` from bones+facets — the chain's terminal authoring step).
6. **Update CLAUDE.md.** Full enumerated change set:
   - **Primary pattern section.** Replace the `project activation → season start → (episode start → shoot)* → bulk and-wrap → repeat` block with the new chain: `/and-project → /and-series → /and-substance series → /and-cast → [series audit checkpoint] → /and-substance book/chapter → /and-write (decomposes scenes into bones) → /and-facets → /and-stitch → draft/<chapter>.md (terminal deliverable; polish deferred)`. Remove "Season start," "Episode start," "Shoot," "And-wrap" prose subsections — the names no longer exist. Add a short paragraph noting that polish/`/and-wrap` is dropped and `/and-stitch`'s output is the deliverable until upstream is proven.
   - **Agent routing table.** No agent additions/removals expected (the new commands reuse existing agents: showrunner, screen-writer, audience, dramatist, auditor, fixer, margit, orchestrator-critic). Confirm `editor` row stays or is marked DEFERRED (since `/and-wrap` is dropped and `/and-stitch` Phase 7 is the standing in for editorial work for now); remove the `editor` row entirely or annotate it as `library-only; not currently dispatched` — pick the latter to preserve the card for the eventual polish revival.
   - **Directory map.** Update `theater/` line: replace `proto-lines.md` reference with `bones/<book>-<chapter>.md`. Keep `draft/` and `polish/` lines but annotate `polish/` as "not written by the current chain — polish deferred." Add `staff/reviews/` line for `/and-review` reports.
   - **Schema authority table.** Update `Proto-line file (shoot-v2)` row to `Bones file → schemas/bones.schema.md` (the renamed schema). Add row for the substance design docs: `Substance framework → design/substance/{README,questionnaire,delta-targets}.md`. Confirm or remove `Per-character dialogue file` and `Facet file` rows — unchanged.
   - **Memory rules section.** Replace the vibe-clouds line. Old: "Vibe-clouds are built at each planning level. Series, season, and episode each have a vibe-cloud. All three are active during shoot; episode-level takes priority on key conflicts." New: "Vibe-clouds are built at series and book level. Both are active during authoring; book-level takes priority on key conflicts. Chapter/scene/bone-level shaping comes from the substance contract, not a vibe-cloud."
   - **Rules section.** Update Rule 10 (URI-026 bone-gate): remove tens-gate language; replace with "`/and-write` Phase 6 substance bone-gate is the bones-first authoring gate. Deformed substance contracts cannot be rescued by downstream facet skin." Update Rule 11 (URI-026 shared reviewer resources): remove `design/shoot-v2/rubric-tensometer.md` reference; keep the audience persona `Threshold Discipline` and AP-SCAN promotion path lines.
   - **Commands table.** Remove rows for `/and-season`, `/and-wrap`, `/and-protolines`, `/and-protolines-v2`, `/and-protolines-season-v2`. Add rows for `/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-review`. Update `/and-facets` row to drop tensometer mention. Update `/and-stitch` row to mark its `draft/<chapter>.md` as the terminal deliverable.
   - **"Not in scope" section.** No change (gacha / workshop-artifact still excluded). Optionally add "Polish / `/and-wrap` revival — deferred until substance machinery is proven."
7. **Commit + push** to `claude/improve-story-substance-CVi58` at logical breakpoints.

---

## Out of scope

- **Retrofitting flea-bottom-dance.** Current active project keeps its state. New chain applies to the next `/and-project` run.
- **Facet rubric changes — partial.** Bones and facets (feeling, memory-flags, scene-map, dialogue, exposition, etc.) are preserved. **Tensometer is removed** — its purpose (per-bone substance-density signal) is now served directly by the per-bone state-delta + bone-gate. `/and-facets` no longer emits a tensometer file; `design/shoot-v2/rubric-tensometer.md` is archived; CLAUDE.md's "shared reviewer resources" line (URI-026) is updated to drop the tens rubric. The Tens-gate in URI-026 is replaced by the substance bone-gate at `/and-write` Phase 6 (per-bone axis-movement verification + per-scene aggregate Δ delivery + cost-paid check against the upstream scene contracts authored by `/and-substance chapter`). `/and-substance` is the chunker only (stops at scene chunks); scene-decomposition + bone-writing + bone-gate logic all live in `/and-write`.
- **Impersonator card "values block."** Deferred — follow-on card-schema task after one full new-chain run.
- **Shoot-v2 chain overhaul.** `/and-facets` and `/and-stitch` unchanged structurally. `/and-facets` drops tensometer from its R1/R2 fanout. They operate on the per-chapter bones files `/and-write` emits.
- **Final-edits / polish / ship-ready manuscript work.** Deferred entirely until the upstream chain (project → series → substance → cast → substance recursive → write → facets → stitch → draft) is proven to produce substantively-right drafts end-to-end. The whole "is the prose ready to ship?" question waits. `/and-wrap` is dropped without replacement; `/and-stitch` is unchanged; `/and-review`'s `prose` subcommand is stubbed-deferred. Whole-text concerns (cross-chapter percussion, repetition cull across the book, polish/ directory) come back after the substance machinery is trusted.
- **Persona library expansion for non-audience staff.** `/and-project` records library-default version; substantive variant composition is a follow-on.

---

## Open questions for user

1. **Archive suffix.** `-pre-substance` for overhauls/renames (`/and-project`, `/and-protolines`); `-dissolved` for commands whose jobs migrated elsewhere and aren't coming back (`/and-season`, `/and-wrap`, `/and-judge-book`). OK?
2. **Universal axis set.** `design/substance/README.md` ships with 9 universal axes (wealth, health, community, emotional, capability, knowledge, reputation, agency, trust). Add / remove?
3. **Chunk-Δ defaults.** Default ratio (series Δ ≥ 6 ranks, book Δ = 2–3, chapter Δ ≈ 1, scene Δ = 0–1). Close enough for first run, or calibrate now?
4. **`/and-substance --cascade` default.** Recommend default OFF (manual level-by-level invocation preserves per-level review checkpoints and dispatch budget). `--cascade` as opt-in for late-stage runs. Confirm?
5. **Orchestrator-critic firing point.** Settled: `/and-review verdict <book-slug>` (subcommand of `/and-review`, absorbing the former `/and-judge-book`). Fires on demand once both `/and-substance book` (all chunks under the book) and `/and-write` (all chapter bones files under the book) are complete. Phase 0 of the subcommand hard-aborts if any chunk under the book is unsubstanced or any chapter is missing its bones file. Cleaner than auto-firing inside `/and-substance book` (which doesn't produce bones) and consolidates the review surface under one router. Confirm?
6. **Series-end shape values.** Five: definitive / open-ended / ambiguous / tragic / triumphant. Add / remove?
7. **Cyclical book semantics.** Cyclical applies to protagonist-perspective axes only (world axes can drift across cyclical books — HP pattern; Hogwarts evolves while Harry resets). Confirm?
8. **Re-run modes naming.** `revise` / `add` / `redo`. Acceptable, or different verbs (`amend` / `extend` / `restart`)?
9. **Vocabulary refactor scope.** "Season"/"episode" language still appears in legacy schemas, the shoot-v2 chain (`/and-protolines`, `/and-facets`, etc.), CLAUDE.md, and design docs. Recommended scope: **reading-context** — rename in command bodies, schemas, design docs, CLAUDE.md, and memory file templates the model reads while authoring. Keep filesystem slugs (`s01e01.md` style) and existing in-flight project state alone. Confirm scope, or wider (filesystem too) / narrower (just removed-command bodies)?

---

## Verification on completion

- `design/substance/{README,questionnaire,delta-targets}.md` exist; README documents the three-invocation / four-chunk-level design + the bone-is-the-beat principle (per-bone state-delta authored by `/and-write`, not by `/and-substance`).
- `schemas/showrunner-memory.schema.md` updated with: `project:` block; restructured `series:` (incl. `structure.book_length.{chapters_per_book, scenes_per_chapter, bones_per_scene}` ranges — note: `beats_per_scene` removed; `bones_per_scene` replaces it); `substance.cost_ledger[].anchor.{book, chapter, scene}` fine-grained anchors; `books[]` nesting down to scenes with `structure.{chapter_count, scene_count}` populated at each authoring level; `scenes[].scene_conflict.{protagonist_force, opposing_force, stakes_axis}` block; `scenes[].bones[]` with `svo`, `substance_delta.{axis_moves, cost, cost_ledger_anchor}`, `facet_tags`, `gate_verdict.{bonefide, flat}`; `bones_file` pointer; `stale_since` field at each level; `orchestrator_critic_verdict.{ruling, report_path, verdict_at, stale_since}` block.
- `schemas/proto-line.schema.md` renamed to `schemas/bones.schema.md`; internal references updated; the schema now reflects bones as scene-children with per-bone state-delta (was previously a flat per-chapter list); CLAUDE.md schema authority table reflects the rename.
- `archive/commands/and-project-pre-substance.md`, `and-season-dissolved.md`, `and-wrap-dissolved.md`, `and-protolines-pre-substance.md` exist (plus v2 variants if present).
- `archive/rubrics/rubric-tensometer-replaced-by-substance.md` exists; `design/shoot-v2/rubric-tensometer.md` gone.
- `/and-facets` command body no longer emits tensometer; CLAUDE.md URI-026 line no longer references tens rubric.
- `.claude/commands/and-{project,series,substance,cast,write,review}.md` exist and parse.
- `.claude/commands/and-stitch.md` is **unchanged from current** (no Phase 7 enhancement, no revise mode).
- No active `.claude/commands/and-season.md`, `and-wrap.md`, `and-judge-book.md`, or `and-protolines*.md`.
- `/and-substance` command body contains NO bone-writing logic and NO scene-decomposition logic (chunker only — produces chunks + contracts; stops at scene chunks).
- `/and-substance` accepts exactly three invocation levels (`series` / `book` / `chapter`); a `scene` invocation is rejected with a clear error pointing the user at `/and-write`.
- `/and-write` command body contains NO chunk authoring above scene level (reads scene chunks; decomposes into bones; produces bones-with-deltas; writes SVO craft).
- `/and-write` Phase 6 substance bone-gate explicitly classifies `SUBSTANCE-FLAT-<axis>` and `SUBSTANCE-SUSPECT-cheap-gain-<axis>` as HARD findings (blocks emission), not SIGNAL.
- `/and-review` parses live router subcommands (chunk / bone / contract / signature / bones / facets / cast / consistency / tree / feedback / verdict); reports persist to `staff/reviews/`. `prose` subcommand stubbed as DEFERRED.
- `polish/` directory not touched by the new chain — manuscript is `draft/<chapter>.md`. Polish concerns deferred entirely.
- `archive/commands/README.md` updated.
- `CLAUDE.md` updated — `/and-season` and `/and-wrap` rows removed; new rows for `/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-review`; primary-pattern line reflects new chain (`/and-project → /and-series → /and-substance series → /and-cast → /and-substance book/chapter → /and-write → /and-facets → /and-stitch`); polish deferred. Vibe-clouds line reflects series+book only.
- Each new command's Phase 0 validates upstream and supports re-run modes (except `/and-project`, which hard-aborts).
- Commit + push lands clean on `claude/improve-story-substance-CVi58`.
