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

Bake a **declared, measurable, auditable substance contract** into the pipeline at every chunk level (series → season → episode → scene), so that:

- Every project has its scope (constraints/settings/themes) and staff (personas for planning/reviewing/editing/judging) explicitly bound before any content is authored.
- Every series declares its substance signature (state axes + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets) and its content (theme, plot, protagonist arc, cast, season chunks).
- Every season inherits the signature and commits per-axis Δ + per-beat substance tags.
- Every episode bone-set is audited for Δ delivery + cost paid + density curve.
- Every polished prose pass is audited for whether the substance lands (felt by audience, traceable to bones by auditor).

---

## Pipeline restructure

The overhaul also restructures the command chain. The current `/and-project` does three different jobs (scope + series + cast); they get split.

**Current chain:** `/and-project → /and-season → /and-shoot* → /and-wrap`

**New chain:** `/and-project → /and-series → /and-season → /and-shoot* → /and-wrap`

Four commands change; one is net new.

| command | status | scope |
|---|---|---|
| `/and-project` | **overhauled (shrinks)** | Scaffold the project; bound scope from the prompt (constraints / settings / themes); select staff personas (planning / reviewing / editing / judging). Hand off to `/and-series`. No story content. |
| `/and-series` | **net new** | Build the series content from project scope: theme / plot start-end / protagonist arc / series question / cast / season chunks. Author the substance signature (state axes + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets). Series-level audit checkpoint. Hand off to `/and-season s01`. |
| `/and-season` | **overhauled** | As current command, plus per-beat substance tags in Phase 1d, substance gate in Phase 1e, new Pass S11 (substance audit) in Phase 3, per-episode substance verdict in Phase 7. |
| `/and-wrap` | **overhauled** | As current command, plus new audience flag class (`SUBSTANCE-FELT` / `-FLAT` / `-SUSPECT`), new auditor class `SUBSTANCE-COVERAGE`, editor allowed-moves extended (within the no-plot-invention fence). |

`/and-shoot`, `/and-stitch`, `/and-facets`, `/and-protolines*` are **downstream** of the substance contract. They execute on what the bones carry. No structural change required in this overhaul — the substance contract feeds them through season-plan inputs and bone-tags. If review during the new chain surfaces facet-level substance gaps, those go into a follow-on `/and-facets` revision separately.

---

## Boundary table — what moves out of `/and-project`

| Current `/and-project` step | Stays / moves | Lands in |
|---|---|---|
| Phase 1 Scaffold (dir tree + stub files) | **stays** | `/and-project` |
| Phase 1.5 Brief expansion (concept-space) | **stays** | `/and-project` |
| Phase 1.6 Audience selection | **stays** | `/and-project` |
| Phase 2 1a — Decided constraints + open questions | **stays** | `/and-project` (this IS project scope) |
| Phase 2 1b — Open question resolution | **stays** | `/and-project` |
| Phase 2 1c — Candidate menu + cast selection | **moves** | `/and-series` (cast is series content) |
| Phase 2 1d — World-law finalization (cond cards) | **stays** | `/and-project` (laws/lore/behaviors ARE scope) |
| Series Plan (theme + plot + protag arc + series Q + season chunks) | **moves** | `/and-series` |
| Series-level audit checkpoint | **moves** | `/and-series` |
| **NEW** — staff persona binding (screen-writer / dramatist / auditor / editor / orchestrator-critic, in addition to audience) | n/a | `/and-project` (new sub-step) |
| **NEW** — substance signature (state axes + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets) | n/a | `/and-series` |

After the split, `/and-project` produces **scope + staff** — no story content, no cast, no themes-as-story-shape (themes-as-scope-limits do stay; the distinction is whether a theme is a *boundary* or a *story*).

---

## Archive plan

Archive current versions of the three overhauled commands to `archive/commands/` with the suffix `-pre-substance` so they coexist with previously-archived versions (current `archive/commands/and-wrap.md` is the older v1 pre-stitcher wrap).

```
git mv .claude/commands/and-project.md archive/commands/and-project-pre-substance.md
git mv .claude/commands/and-season.md  archive/commands/and-season-pre-substance.md
git mv .claude/commands/and-wrap.md    archive/commands/and-wrap-pre-substance.md
```

`/and-series` is net new — nothing to archive.

Update `archive/commands/README.md` with a new "Why shelved" entry:

> **2026-05-16 — substance overhaul + project/series split.** The planning + finalization commands were shelved together for two reasons: (1) the pre-substance versions optimize per-line craft, dramatic shape, mechanic discipline, continuity, and prose economy — but have no declared substance contract; episodes shipped through the pre-substance chain were structurally clean and substance-flat. (2) `/and-project` was conflating scope (constraints/settings/themes/staff) with series content (theme/plot/cast/season chunks). The replacement chain is `/and-project` (scope+staff) → `/and-series` (series content + substance signature) → `/and-season` (substance-aware) → `/and-wrap` (substance-aware). See `design/substance/`.

The pre-substance files stay reachable via git for diff/comparison during the rewrite, and via `git mv` back to `.claude/commands/` for reactivation if the substance chain regresses.

---

## New artifacts

### `design/substance/README.md`

The framework reference. Authoring authority for substance terminology, state-axis catalog, 1–9 scale anchors, Δ/cost/density definitions, plot-by-states + plot-by-action duality, perspective-bound measurement, antagonist-pressure, failure-mode catalog, pipeline-threading map.

### `design/substance/questionnaire.md`

The 1–9 archetype questionnaire (story / protagonist / world / antagonist) used to pin axis ranks honestly at series-plan and season-plan time. Per-archetype question banks. Includes example scoring trace for at least one archetype.

### `design/substance/delta-targets.md`

The per-chunk Δ targets and target bone counts. Spells out:
- Series-scale Δ — total signature-axis movement across the full series.
- Season-scale Δ — fraction of series Δ owed per season, by season position (opening / mid / climax / denouement).
- Episode-scale Δ — typical Δ per episode, scaled by season position.
- Scene-scale Δ — smallest unit; one rank shift on one axis is a substantial scene.
- Bone-count targets per chunk, computed from Δ × density-target.
- The relationship between target chunk size and Δ — substance density is a curve, not a constant.

### `schemas/showrunner-memory.schema.md` (updated)

Add a new top-level `project:` block (the scope output of `/and-project`):
```yaml
project:
  brief: <one-line distill of the user prompt>
  constraints:
    settings: [<one-line each>]
    themes_as_bounds: [<one-line each>]   # NOT story themes; thematic bounds (e.g. "no gratuitous cruelty", "grimdark register").
    hard_fences: [<one-line each>]        # e.g. "no Earth-Bet proper nouns".
  staff:
    audience: [<persona-slug>, <persona-slug>, <persona-slug>]
    screen_writer: <persona-or-library-default>
    dramatist: <persona-or-library-default>
    auditor: <persona-or-library-default>
    editor: <persona-or-library-default>
    orchestrator_critic: <card-version>
```

Add to `series:` (the output of `/and-series`):
```yaml
series:
  theme: <one line>
  laws: [...]   # existing
  lore: [...]   # existing
  behaviors: [...]   # existing
  plot: {start, end, protagonist_arc, series_question}   # existing
  cast_roster: [...]   # existing (moved from /and-project)
  stage_elements: [...]   # existing
  state_axes:
    - slug: <axis-slug>
      dimension: <one line — what this axis measures>
      one_means: <one line — what rank 1 looks like in this story>
      nine_means: <one line — what rank 9 looks like>
      perspective: protagonist | antagonist | world
      start_rank: <1-9>
      end_rank: <1-9>
  cost_ledger:
    - gain: <axis-slug> +<delta>
      cost: <axis-slug> -<delta> | opportunity-missed:<one line> | journey-required:<one line>
      arc: <where in the series this trade is paid — season slug>
  antagonist_pressure:
    - axis: <axis-slug>
      pressure_source: <one line — what force pushes back on this axis>
      cost_curve: <one line — what gain on this axis costs as it scales>
  chunk_targets:
    series: { delta_per_signature_axis: <range>, density_target: <range> }
    season: { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
    episode: { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
    scene: { delta_per_signature_axis: <range>, density_target: <range>, bone_count: <range> }
```

Add to each `seasons[]` entry:
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

Add to each `seasons[].episodes[]` entry (post-Phase-7):
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

## Command rewrites

### `/and-project` (new version — strict scope + staff)

Three jobs only:

1. **Scaffold** — directory tree, stub files, audience working dirs (mechanical, as current).
2. **Project scope** — bound from the prompt:
   - Phase 1.5 brief expansion (concept-space — unchanged).
   - Phase 2 1a — decided constraints + open questions (unchanged).
   - Phase 2 1b — open-question resolution (unchanged).
   - Phase 2 1d — world-law finalization (condition cards: laws + lore + behaviors).
   - Output: `project.constraints` block in showrunner memory + `staff/showrunner/world-notes.md` + condition cards in `cards/conditions/`.
3. **Staff selection** — bound personas for the roles required for planning / reviewing / editing / judging:
   - Audience ×3 (existing Phase 1.6).
   - Screen-writer persona (currently library default; if the project benefits from a specific taste/voice variant, margit composes it from a base card).
   - Dramatist persona (currently library default).
   - Auditor persona (currently library default).
   - Editor persona (currently library default).
   - Orchestrator-critic card version (currently library-only).
   - Output: `project.staff` block in showrunner memory.

**What `/and-project` does NOT do:** no cast, no series plan, no substance signature, no story themes, no series question, no season chunks, no series-level audit checkpoint.

**Output:** project-scope-approval checkpoint. Human reviews the scope + staff. On approval, `/and-series` is the next command.

**Estimated size:** the new `/and-project` is roughly **half** the size of the current one (no series plan, no cast selection — those are the bulkiest sections).

### `/and-series` (net new)

The series-content + substance-signature command. Reads project scope + staff from showrunner memory. Produces the series plan and the substance signature, with audience + dramatist review.

**Phases:**

1. **Phase 0 — Validate.** Read `project:` block from showrunner memory. Abort if scope is incomplete (constraints missing, staff unbound). Abort if `series:` block already populated (series plan already exists).
2. **Phase 1 — Cast selection.** Margit candidate menu + screen-writer cast review + dramatist viability check + margit provisioning into `active-project/actors/` + per-actor vibes. (Moved verbatim from current `/and-project` step 1c.)
3. **Phase 2 — Series plan.** Build series vibe-cloud, establish series drama, screen-writer authors one chunk statement per planned season (≥3 seasons; final-season open). Audience + dramatist review with accept/revise loop (3-try cap).
4. **Phase 3 — Substance signature.** Five sub-steps (each goes through audience+dramatist substance gate):
   - 3.a — State-axis signature: 5–9 axes (universal + project-specific), 1/5/9 anchor descriptions, perspective tag.
   - 3.b — Δ Start/End per axis (protagonist + antagonist if present + world if relevant). Uses `design/substance/questionnaire.md`.
   - 3.c — Cost ledger: every gain paired with cost / opportunity-missed / journey-required, anchored to a season.
   - 3.d — Antagonist pressure: per protagonist axis, the opposing force and cost-curve.
   - 3.e — Chunk-Δ targets: defaults from `design/substance/delta-targets.md`; project may override.
5. **Phase 4 — Per-season chunk substance commitments.** Each season chunk additionally names: which signature axes shift, direction, target Δ-magnitude. Audience+dramatist re-review with the substance commitments included.
6. **Phase 5 — Series-level audit.** Auditor (fork) against the full series plan + substance signature + project constraints. Faults route to fixer or escalate.
7. **Phase 6 — Present results.** Series-level audit checkpoint — human reviews. On approval, `/and-season s01` is the next command.

**Memory write-out:** `series:` block populated. `seasons[]` get their chunk + substance commitments. `active.season` stays `~` until `/and-season s01`.

**Estimated size:** ~300–350 lines (comparable to current `/and-project`).

### `/and-season` (new version)

Inherits all current phases. Substance work lands in Phase 1 (planning) and Phase 3 (review):

- **Phase 1c (drama):** read the series signature and the season's chunk substance commitment from `/and-series`. Season drama statement must name what cannot survive the season *in terms of axis movement* — not just collision, but Δ.
- **Phase 1d (content beat authoring):** each beat carries a substance tag — which axis moves, direction, target Δ-magnitude on 1–9, cost (if any). Beats with no axis movement are explicitly tagged `setup` or `transition` (legitimate but capped at ~25% of beats per season per density target).
- **Phase 1e (review):** new substance gate — does the beat list deliver the season's named Δ on each axis? Are costs paid? Is the density curve shaped (low-mid-high-mid pattern through the season)?
- **Phase 2 (bone expansion):** screen-writer brief includes the per-beat substance tags. The bones must carry the axis movement — every named Δ has visible cause bones.
- **Phase 3 Sweep A:** add **Pass S11 — Substance audit**. Two fork roles:
  - **S11.a — dramatist** per-window verifies: every season-named axis Δ has visible cause bones; the rank movement implied by the bones matches the named Δ within ±1 rank; cost-ledger entries are paid.
  - **S11.b — audience ×3** per-window verifies felt-substance: `SUBSTANCE-FELT` / `SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>` per persona.
  - Substance failures route to screen-writer for stretch regen with explicit substance-deficit named.
- **Phase 7 Step 5:** per-episode `substance_delta` block computed from the bones-roster and the window substance verdicts; persisted to memory.

**Phase 1 auto-plan condition (unchanged):** /and-season auto-plans the season when no season-plan exists. Now also reads `series:` block (signature + season chunk substance commitments) as input. Aborts if `series:` block is empty (means `/and-series` hasn't run).

Sweep A grows from 18 forks to 22 forks (+1 dramatist + 3 audience). Dispatch budget impact: ~4 extra forks per Sweep A cycle.

### `/and-wrap` (new version)

Inherits the three-phase v2 architecture (audience review → auditor pass → editor pass). Substance work lands as:

- **Phase 1 audience review:** persona briefs extended with felt-substance verdict per scene. New flag class: `SUBSTANCE-FELT` (positive — substance lands) / `SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>` (negative). Advisory, not blocking — feeds editor remediation.
- **Phase 2 auditor pass:** new class **SUBSTANCE-COVERAGE**. Verifies the rendered prose carries the per-episode `substance_delta` from showrunner memory:
  - Every axis named in `axes_moved` has prose-traceable cause language at the named open→close shift.
  - Cost-ledger entries appear in the prose at the costed beat.
  - Density curve is shape-honest — peak bones get prose density.
  - HARD findings block the editor; SIGNAL findings inform.
- **Phase 3 editor pass:** allowed-moves extended with **substance remediation within fences** — prose density tightening at peak beats, percussion that names cost at cost-ledger beats, audience-flagged substance-flat scenes get prose-economy passes or repetition cuts. **Forbidden** — adding plot, inventing rank shifts, modifying dialogue verbatim. Substance must already be in the bones; editor only sharpens its surface.

---

## Order of operations

1. **Plan approval.** This doc reviewed and accepted (or revised).
2. **Design docs first.**
   - Write `design/substance/README.md` (framework).
   - Write `design/substance/questionnaire.md` (1–9 archetype questionnaire).
   - Write `design/substance/delta-targets.md` (per-chunk Δ + bone-count bands).
3. **Schema update.**
   - Update `schemas/showrunner-memory.schema.md` with new `project:` block + `series:` substance additions + `seasons[]` + `seasons[].episodes[]` blocks.
4. **Archive current commands.**
   - `git mv` the three to `archive/commands/<name>-pre-substance.md`.
   - Update `archive/commands/README.md`.
5. **Write new commands** (in order):
   - `.claude/commands/and-project.md` — strict scope+staff.
   - `.claude/commands/and-series.md` — net new; series content + substance signature.
   - `.claude/commands/and-season.md` — substance-aware (with Pass S11).
   - `.claude/commands/and-wrap.md` — substance-aware (with SUBSTANCE-COVERAGE).
6. **Update `CLAUDE.md`.**
   - Add `design/substance/README.md` to the schemas/authority section.
   - Add a brief substance-framework note to the rules section.
   - Update the command table (new `/and-series` row; updated `/and-project` description).
   - Update the "Primary pattern" line to include `/and-series`.
7. **Commit + push** to `claude/improve-story-substance-CVi58` after each major step (design docs, schema, archive, each new command, CLAUDE.md).

---

## What is explicitly out of scope

- **Retrofitting flea-bottom-dance.** Per user decision, the current active project keeps its current state. The new chain applies to the next `/and-project` run.
- **Facet rubric changes.** Existing facet rubrics (tensometer, feeling, memory-flags, etc.) are not modified. Substance is enforced upstream (planning + bones) and downstream (rendered-prose audit) — facet authoring sits between and is unaffected.
- **Impersonator card changes.** The note "impersonator should know what is valued most" suggests adding a values block to actor cards. Deferred — handle as a follow-on card-schema task if needed, after one full new-chain run reveals whether actor-card values are missing in practice.
- **`/and-shoot` overhaul.** The shoot pipeline (v1) is already archived. The current authoring path is `/and-protolines* → /and-facets → /and-stitch → /and-wrap`. Substance lands in proto-lines (via /and-season) and in wrap (via SUBSTANCE-COVERAGE). No shoot-loop change.
- **New facet for substance.** Considered and rejected — substance is a *contract* (planning) and an *audit* (review), not a facet (authoring layer). Facets are perception/voice channels for stitching; substance is the structural Δ commitment.
- **Persona library expansion for non-audience staff.** Right now screen-writer / dramatist / auditor / editor / orchestrator-critic are library defaults (singleton each). `/and-project` records which is bound; it does NOT compose new variants in this overhaul. If the project benefits from variants, that's a follow-on staff-library expansion task.

---

## Open questions for user

1. **Archive suffix:** `-pre-substance` (semantic) vs `-v1` / `-v2` (version). Defaulting to `-pre-substance`.
2. **Universal axis set:** `design/substance/README.md` ships with 9 universal axes (wealth, health, community, emotional, capability, knowledge, reputation, agency, trust). Add / remove?
3. **Chunk-Δ defaults:** is the default ratio (series Δ = 6+ ranks across signature, season Δ = 2–3 ranks, episode Δ = 1 rank, scene Δ = 0–1 rank) close enough? Will calibrate after one new-chain run.
4. **Pass S11 audience dispatch count:** 3 personas × per-window = scales with N windows. For N=6, that's 18 extra audience dispatches. Acceptable, or should S11.b run on whole-season instead of per-window?
5. **`/and-series` auto-fire from `/and-season`:** if `series:` block is empty when `/and-season s01` runs, should `/and-season` auto-fire `/and-series` (same pattern as the current season-plan auto-fire), or hard-abort and require explicit `/and-series` invocation? Recommend **hard-abort** — `/and-series` is a substantial command with its own human checkpoint, and silently chaining it inside `/and-season` would skip that checkpoint.
6. **Staff-persona-binding minimum:** for non-audience staff (screen-writer / dramatist / auditor / editor / orchestrator-critic), is the binding decision just "record library-default version" (lightweight, current behavior) or does `/and-project` need to do something more substantive (e.g., dispatch margit to compose a project-tuned variant)? Recommend **record library-default** for now; treat substantive variant-composition as a follow-on.

---

## Verification on completion

After execution, sanity checks:

- `design/substance/{README,questionnaire,delta-targets}.md` exist and parse.
- `schemas/showrunner-memory.schema.md` updated with `project:` block + `series:` substance additions + `seasons[]` and `seasons[].episodes[]` substance blocks.
- `archive/commands/and-{project,season,wrap}-pre-substance.md` exist; current `.claude/commands/and-{project,season,wrap}.md` are rewritten.
- `.claude/commands/and-series.md` exists (net new).
- `archive/commands/README.md` updated.
- `CLAUDE.md` updated — `/and-series` added to command table, primary-pattern line updated.
- Each new command file parses, has unchanged Phase 0 + dispatch protocol where applicable, and the new substance sections are clearly delimited.
- Commit + push lands clean on `claude/improve-story-substance-CVi58` after each major step.
