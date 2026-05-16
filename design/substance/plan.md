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

- Every series declares its substance signature (state axes + Δ Start/End + cost ledger + antagonist pressure + chunk-Δ targets).
- Every season inherits the signature and commits per-axis Δ + per-beat substance tags.
- Every episode bone-set is audited for Δ delivery + cost paid + density curve.
- Every polished prose pass is audited for whether the substance lands (felt by audience, traceable to bones by auditor).

---

## Scope of overhaul

Three commands are being replaced. The current versions are sound for shape/mechanic/continuity but have no substance contract. The replacements layer substance on top of the existing capabilities without losing them.

| command | overhaul reason | new artifacts inside |
|---|---|---|
| `/and-project` | Series plan has no substance signature. Season chunks have no per-axis Δ commitments. | State-axis signature step; cost ledger; antagonist pressure block; chunk-Δ targets; per-season chunk Δ axes. |
| `/and-season` | Content beats are action-only. Phase 3 review has no substance pass. Per-episode files have no substance verdict. | Per-beat substance tag in Phase 1d; substance gate in Phase 1e; new Pass S11 (substance audit) in Phase 3; per-episode substance verdict in Phase 7. |
| `/and-wrap` | Auditor classes don't include substance-coverage. Audience flags don't carry felt-substance verdicts forward into editor remediation. | New auditor class SUBSTANCE-COVERAGE; new audience flag class SUBSTANCE-FELT / SUBSTANCE-FLAT; editor allowed-moves extended with prose-density-for-substance (within the no-plot-invention fence). |

`/and-shoot`, `/and-stitch`, `/and-facets`, `/and-protolines*` are **downstream** of the substance contract. They execute on what the bones carry. No structural change required in this overhaul — the substance contract feeds them through season-plan inputs and bone-tags. If review during the new pipeline surfaces facet-level substance gaps, those go into a follow-on `/and-facets` revision separately.

---

## Archive plan

Archive current versions of all three commands to `archive/commands/` with the suffix `-pre-substance` so they coexist with previously-archived versions (current `archive/commands/and-wrap.md` is the older v1 pre-stitcher wrap).

```
git mv .claude/commands/and-project.md archive/commands/and-project-pre-substance.md
git mv .claude/commands/and-season.md  archive/commands/and-season-pre-substance.md
git mv .claude/commands/and-wrap.md    archive/commands/and-wrap-pre-substance.md
```

Update `archive/commands/README.md` with a new "Why shelved" entry for the three:

> **2026-05-16 — substance overhaul.** The three planning + finalization commands were shelved together. The pre-substance versions optimize per-line craft, dramatic shape, mechanic discipline, continuity, and prose economy — but have no declared substance contract. Episodes shipped through the pre-substance chain were structurally clean and substance-flat (audience felt them as empty). The replacement chain layers a state-axis-driven substance contract on top of the existing capabilities. See `design/substance/`.

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

Add to `series:`
```yaml
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

### `/and-project` (new version)

Inherits all current phases. Substance work lands in Phase 2 Series Plan as new sub-steps:

1. **Series state-axis signature.** Screen-writer authors 5–9 axes (universal-library + project-specific), 1/5/9 anchor descriptions per axis, perspective tag (protagonist / antagonist / world).
2. **Series Δ Start/End.** For each axis, protagonist (and antagonist if present, and world if relevant) rank at series open and series close, using the questionnaire.
3. **Cost ledger.** For each gain across the arc, named cost (axis loss / opportunity missed / journey required) and which season pays the trade.
4. **Antagonist pressure.** For each protagonist axis, the opposing force and cost-curve.
5. **Chunk-Δ targets.** Per-chunk Δ targets and bone-count bands (defaults from `design/substance/delta-targets.md`; project may override).
6. **Per-season chunk substance commitments.** Each season chunk additionally names: which signature axes shift this season, direction, target Δ-magnitude.

All five steps go through audience+dramatist review (substance gate added to the existing accept/revise loop). Memory write-out includes the new fields.

### `/and-season` (new version)

Inherits all current phases. Substance work lands in Phase 1 (planning) and Phase 3 (review):

- **Phase 1c (drama):** read the series signature and the season's chunk substance commitment. Season drama statement must name what cannot survive the season *in terms of axis movement* — not just collision, but Δ.
- **Phase 1d (content beat authoring):** each beat carries a substance tag — which axis moves, direction, target Δ-magnitude on 1–9, cost (if any). Beats with no axis movement are explicitly tagged `setup` or `transition` (legitimate but capped at ~25% of beats per season per density target).
- **Phase 1e (review):** new substance gate — does the beat list deliver the season's named Δ on each axis? Are costs paid? Is the density curve shaped (low-mid-high-mid pattern through the season)?
- **Phase 2 (bone expansion):** screen-writer brief includes the per-beat substance tags. The bones must carry the axis movement — every named Δ has visible cause bones.
- **Phase 3 Sweep A:** add **Pass S11 — Substance audit**. Two fork roles:
  - **S11.a — dramatist** per-window verifies: every season-named axis Δ has visible cause bones; the rank movement implied by the bones matches the named Δ within ±1 rank; cost-ledger entries are paid (loss axis has loss bones).
  - **S11.b — audience ×3** per-window verifies felt-substance: `SUBSTANCE-FELT` / `SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>` per persona.
  - Substance failures route to screen-writer for stretch regen with explicit substance-deficit named.
- **Phase 7 Step 5:** per-episode `substance_delta` block computed from the bones-roster and the window substance verdicts; persisted to memory.

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
   - Write `design/substance/README.md` (the framework reference).
   - Write `design/substance/questionnaire.md` (the 1–9 archetype questionnaire).
   - Write `design/substance/delta-targets.md` (per-chunk Δ + bone-count bands).
3. **Schema update.**
   - Update `schemas/showrunner-memory.schema.md` with new fields + field notes.
4. **Archive current commands.**
   - `git mv` the three to `archive/commands/<name>-pre-substance.md`.
   - Update `archive/commands/README.md`.
5. **Write new commands.**
   - `.claude/commands/and-project.md` — substance-aware v2.
   - `.claude/commands/and-season.md` — substance-aware v2 (with Pass S11).
   - `.claude/commands/and-wrap.md` — substance-aware v3 (with SUBSTANCE-COVERAGE).
6. **Update `CLAUDE.md`.**
   - Add `design/substance/README.md` to the schemas/authority section.
   - Add a brief substance-framework note to the rules section.
   - Update the command table.
7. **Commit + push** to `claude/improve-story-substance-CVi58`.

---

## What is explicitly out of scope

- **Retrofitting flea-bottom-dance.** Per user decision, the current active project keeps its current state. The new chain applies to the next `/and-project` run.
- **Facet rubric changes.** Existing facet rubrics (tensometer, feeling, memory-flags, etc.) are not modified. Substance is enforced upstream (planning + bones) and downstream (rendered-prose audit) — facet authoring sits between and is unaffected.
- **Impersonator card changes.** The note "impersonator should know what is valued most" suggests adding a values block to actor cards. Deferred — handle as a follow-on card-schema task if needed, after one full new-chain run reveals whether actor-card values are missing in practice.
- **`/and-shoot` overhaul.** The shoot pipeline (v1) is already archived. The current authoring path is `/and-protolines* → /and-facets → /and-stitch → /and-wrap`. Substance lands in proto-lines (via /and-season) and in wrap (via SUBSTANCE-COVERAGE). No shoot-loop change.
- **New facet for substance.** Considered and rejected — substance is a *contract* (planning) and an *audit* (review), not a facet (authoring layer). Facets are perception/voice channels for stitching; substance is the structural Δ commitment.

---

## Open questions for user

1. **Archive suffix:** `-pre-substance` (semantic) vs `-v1` / `-v2` (version). Defaulting to `-pre-substance`.
2. **Universal axis set:** the `design/substance/README.md` ships with 9 universal axes (wealth, health, community, emotional, capability, knowledge, reputation, agency, trust). User may want to add/remove.
3. **Chunk-Δ defaults:** is the default ratio (series Δ = 6+ ranks across signature, season Δ = 2–3 ranks, episode Δ = 1 rank, scene Δ = 0–1 rank) close enough? Will calibrate after one new-chain run.
4. **Pass S11 audience dispatch count:** 3 personas × per-window = scales with N windows. For N=6, that's 18 extra audience dispatches. Acceptable, or should S11.b run on whole-season instead of per-window?

---

## Verification on completion

After execution, sanity checks:

- `design/substance/{README,questionnaire,delta-targets}.md` exist and parse.
- `schemas/showrunner-memory.schema.md` updated with new blocks.
- `archive/commands/and-{project,season,wrap}-pre-substance.md` exist; current versions of those three are rewritten under `.claude/commands/`.
- `archive/commands/README.md` updated.
- `CLAUDE.md` updated.
- Each new command file parses, has unchanged Phase 0 + dispatch protocol, and the new substance sections are clearly delimited.
- Commit + push lands clean on `claude/improve-story-substance-CVi58`.
