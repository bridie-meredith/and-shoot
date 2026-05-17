# Substance Framework — Reference

Authoring authority for substance terminology, state-axis catalog, 1–9 scale anchors, Δ/cost/density definitions, plot-by-states + plot-by-action duality, perspective-bound measurement, antagonist-pressure, failure-mode catalog, and the pipeline-threading map.

**Companion docs:** `questionnaire.md` (screen-writer's authoring rubric for the signature) · `delta-targets.md` (default bands per chunk level) · `rerun-protocol.md` (Phase 0 shared shape) · `staleness-cascade.md` (downstream surfacing) · `run-book.md` (first-time-execution user-facing guide) · `plan.md` (implementer-facing design).

---

## Chapter ≈ episode (bridge for prior users)

A **chapter** is the terminal unit of consumption under the substance chain. One chapter ≈ one previous episode in scope and length — roughly 3000–5000 words across 1–3 scenes. Reader feedback authored against "episodes" (s01e01, s01e02, ...) maps to chapter-level concerns under the new chain; **books** map to the prior season concept. The "season"/"episode" framing is dropped from command bodies, schemas, and design docs, but is documented here once for the bridge.

The shoot-v2 chain (bones → ten facets + dialogue → cite-index → stitcher draft) is preserved end-to-end. What changed is upstream: chunking is now recursive (series → book → chapter → scene) with a declared substance contract at each level, and bones are scene-children with per-bone state-deltas.

---

## What substance is

A story has **substance** when its events cause measurable state-change in something the audience values, and that change is **earned** through cost. A scene where the protagonist gains community standing because they helped a friend has substance — community went up, the cost of helping was paid. A scene where the protagonist gains community standing because the king happens to like them today is substance-flat (a/k/a "cheap gain") — community went up but no cost was paid; the change isn't earned.

The substance contract is the **declared, measurable, auditable** version of that intuition. Every chunk (series, book, chapter, scene) declares:
- **Which axes shift** — the state dimensions in motion (wealth, health, community, emotional, capability, knowledge, reputation, agency, trust).
- **By how much** — the Δ between start-rank and end-rank on a 1–9 scale.
- **At what cost** — what the protagonist (or antagonist, or world) loses or pays to drive the gain.
- **From whose perspective** — protagonist / antagonist / world; the same event reads differently from each.

A reviewer can ask: did this chunk deliver its declared Δ? Did the cost get paid in visible bones? Is the gain cheap? Substance becomes a verifiable property, not just a felt quality.

---

## The recursive `/and-substance` design

**Four chunk levels** exist:
- **Series** — the top-level shape. Has a signature: state axes + 1–9 anchors + cost ledger + antagonist pressure.
- **Book** — one entry per top-level act-of-the-story. Has a chunk (Star-Wars-trilogy paragraph) + substance Δ + drama statement.
- **Chapter** — terminal unit of consumption. Has a chunk + substance Δ + dramatic shape + goal + handoff_in/out + pov_narrator.
- **Scene** — substantial; 1–3 per chapter. Has a chunk + substance Δ + scene_conflict (protagonist_force / opposing_force / stakes_axis).

**Three invocation levels** author them:
- `/and-substance series` — produces book chunks + per-book Δ. Also authors the series signature in Phase 4.
- `/and-substance book <slug>` — produces chapter chunks + per-chapter Δ. Also authors book drama in Phase 4.
- `/and-substance chapter <slug>` — produces scene chunks + per-scene Δ + scene_conflict. Also authors chapter dramatic_shape + goal in Phase 4.

Scenes are **produced but never invoke** — they are the deepest chunks. `/and-write` consumes scene chunks and decomposes them into bones.

---

## The bone-is-the-beat principle

The **bone** is the smallest substance unit. Each bone declares one axis-movement (occasionally two) with declared cost. The bone IS the beat — what used to be a separate "beat chunk" planning level is collapsed into the bone itself, authored by `/and-write` during scene decomposition.

A scene contains 5–15 bones. Each bone earns its place by causing Δ. Chatter bones (no declared Δ) do not survive `/and-write` Pass 4 trim. This addresses the user-feedback complaint that protolines under the prior chain were "too fine grained" — under the substance contract, a bone-without-Δ is a schema violation, not a craft choice.

**Bones are scene-children, not flat-per-chapter.** The source of truth is `chapters[].scenes[].bones[]` in showrunner memory. The per-chapter file `theater/bones/<book>-<chapter>.md` is a **flattened view** emitted by `/and-write` Phase 7 for downstream `/and-facets`/`/and-stitch` consumption. Per-bone state-delta lives in memory only — the bones file is comment-clean.

**Scene-action-sized, not micro.** A bone covers a meaningful scene-action — one declared axis-movement with declared cause. "Maya confronts her brother about the missing key, +2 community, −1 emotional" is one bone. Not "Maya opens her mouth" + "Maya speaks" + "Maya pauses" as separate micro-beats.

---

## State axes — the universal catalog

`/and-substance series` Phase 4 (signature authoring) proposes a 9-axis baseline. The user may add, remove, or rename axes; the proposal is a starting point, not a fixed list.

| axis | dimension | rank-1 anchor (example) | rank-5 anchor | rank-9 anchor |
|---|---|---|---|---|
| **wealth** | material resources + economic security | destitute; cannot eat without help | comfortable; one mid-cost emergency away from danger | independently rich; supports a household |
| **health** | physical wellbeing + capacity for action | bedridden or near death | normal vigor | peak athletic/martial condition |
| **community** | belonging + relational support | isolated; nobody comes for you | a circle of reliable people | a constituency that mobilizes for you |
| **emotional** | inner stability + self-coherence | dissociated, grief-flattened, or shattered | functional; emotionally available | self-secure; can hold space for others |
| **capability** | skill + competence in domains that matter to the story | helpless at the central task | competent professional | virtuoso; nobody in the story can match you |
| **knowledge** | situational awareness + information possession | knows nothing critical to the situation | informed peer | knows what others don't; informational lead |
| **reputation** | external read on the character | unknown or actively despised | respected within their circle | famous; their name precedes them |
| **agency** | ability to direct outcomes through choice | imprisoned, coerced, or paralyzed | autonomous within ordinary scope | shapes the world around them |
| **trust** | mutual reliance with named others | trusts no one; trusted by no one | reliable two-way trust with a handful | the keystone of a trust-network |

Anchors are **per-story** — the screen-writer rewrites the rank-1 / rank-5 / rank-9 anchors per project to fit the source world. "Rank 9 wealth" in a flea-bottom-Westeros story is different from "rank 9 wealth" in a Silicon Valley story. The anchors written into `series.substance.state_axes[].{one_means, five_means, nine_means}` are binding for the project.

**Perspectives.** Each axis is tracked from one or more of three perspectives — protagonist / antagonist / world. The same axis can have separate entries per perspective. Protagonist-wealth and antagonist-wealth move independently. The signature lists axes per perspective.

**Class** *(optional, for future emotional-substance orthogonality check).* Axes may be tagged `class: plot` or `class: emotional`. Plot-axes (wealth, capability, knowledge, reputation, agency) drive event-substance. Emotional axes (community, emotional, trust) drive felt-substance. A chapter whose contract moves only plot-axes while the chunk-text describes a plot event with clear emotional consequence (death, betrayal, revelation) may HARD-fault on the future emotional-substance orthogonality check — currently OOS but recorded for follow-on.

---

## Δ / cost / density definitions

**Δ (delta)** — the rank difference between start and end on a 1–9 axis. Series Δ is the difference between the protagonist's series-start rank and series-end rank, per axis. Book Δ is the same, scoped to the book. Chapter Δ, scene Δ, bone Δ likewise.

**Cost** — the negative-direction Δ paid to drive a positive-direction gain. The cost-ledger entries pair gains with costs explicitly: `gain: community +2 / cost: emotional -1` records that the +2 community at this scene was paid by a -1 emotional cost. Free gains (gain without cost in the ledger) are `SUBSTANCE-SUSPECT-cheap-gain-<axis>` and are HARD findings at the bone-gate.

Three cost variants:
- **Axis cost** — another axis pays. The canonical case. `community +2 / emotional -1`.
- **Opportunity missed** — a free-text one-line description of what the protagonist could have done instead. Used when no countable axis is paid (e.g. the cost is "didn't talk to her father one last time before he left").
- **Journey required** — a free-text description of the bridge-effort the protagonist had to traverse to get the gain. Used when the cost is structural/setup (e.g. "had to cross the war-zone to reach the library").

**Density** — the ratio of substance-bearing bones to total bones in a chunk. A density-target band is declared per chunk level (see `delta-targets.md`). Density measures how concentrated the substance is; a chapter whose declared Δ is delivered but spread thin across many chatter-bones reads slack.

---

## Plot-by-states + plot-by-action (the duality)

A bone records what *happened* (plot-by-action). A bone's substance_delta records what *changed* (plot-by-states). Both are required — a bone with action but no state-change is chatter; a bone claiming state-change without a physical action that causes it is `SUBSTANCE-FLAT` (rank claim without visible cause).

The bone-gate at `/and-write` Phase 6 verifies the SVO physically causes the declared Δ — **bonefide** check. "maya confronts tomas, +2 community, -1 emotional" is bonefide if the SVO "maya confronts tomas" plausibly causes community-+2 and emotional--1 given the scene contract. "maya enters the yard, +2 community" is not bonefide — entering a yard doesn't move community without further setup.

---

## Antagonist pressure

The signature includes `antagonist_pressure[]` entries — per-axis pressure sources and cost curves. For each axis the antagonist (or world) pushes on, the signature names:
- `pressure_source` — what is doing the pushing (a named character, an institution, an environmental force).
- `cost_curve` — how the pressure escalates across the series.

Reviewers verify antagonist pressure shows up in bones. A chapter whose protagonist takes a +1 community gain while the antagonist's reputation pressure is mid-curve should have a visible push-back somewhere in the bones — `SUBSTANCE-FLAT-pressure` if not.

---

## Failure mode catalog

The bone-gate at `/and-write` Phase 6 classifies findings:

| class | severity | meaning |
|---|---|---|
| `SUBSTANCE-FLAT-<axis>` | HARD | A bone or scene declared Δ on `<axis>` but the SVO doesn't cause it; rank claim without visible cause. |
| `SUBSTANCE-SUSPECT-cheap-gain-<axis>` | HARD | A gain on `<axis>` with no cost paid (no cost-ledger anchor, no opposing-force-visible). |
| `BONE-FORM-<form-fault>` | HARD | SVO discipline violation per `schemas/bones.schema.md` (copula, negation, modifier, etc.). |
| `COST-NOT-PAID` | HARD | A cost-ledger entry exists at a level whose anchor sits at-or-under this chapter, but no visible bone pays it. |
| `OPPOSING-FORCE-MISSING` | HARD | A scene's `scene_conflict.opposing_force` is not visible in the bones. |
| `AXIS-DELTA-MISMATCH` | HARD (>±2) / SIGNAL (±1–±2) | Aggregate bone-Δ on an axis differs from the scene's declared Δ. |
| `BONE-COUNT-BELOW-TARGET` | SIGNAL | Scene's bone count is under the declared `bones_per_scene` minimum. |
| `CHATTER-BONE-OVER-CAP` | SIGNAL | A bone with no declared Δ that survives past the density-target cap. |

HARD findings block emission at Phase 7. SIGNAL findings record but pass — they're surfaced in the emit-summary so the user can address them via `/and-write <chapter> revise --from-signals` if desired.

---

## Pipeline-threading map

How substance flows through the chain:

```
/and-project
  ↓ project.constraints + project.staff
/and-series
  ↓ series.chunk + series.structure
/and-substance series
  ↓ series.substance.{state_axes, cost_ledger, antagonist_pressure, chunk_targets}
  ↓ books[*].chunk + books[*].substance_delta + books[*].structure
/and-cast
  ↓ series.cast_roster
  ↓ project.series_audit.approved_at  ← human checkpoint
/and-substance book b01
  ↓ books[b01].drama
  ↓ chapters[*].{chunk, substance_delta, structure, handoff_in, handoff_out}
/and-substance chapter b01c01
  ↓ chapters[b01c01].{pov_narrator, dramatic_shape, goal}
  ↓ scenes[*].{chunk, substance_delta, scene_conflict, structure}
/and-write b01c01
  ↓ scenes[*].bones[*].{slug, svo, substance_delta, gate_verdict, flat_id}
  ↓ theater/bones/b01-c01.md         ← flattened bones file
  ↓ theater/facets/scene-map-b01-c01.md  ← scene-map facet
/and-facets b01c01
  ↓ theater/facets/<facet>-b01-c01.md (×9, tens dropped)
  ↓ theater/dialogue/b01-c01.md
/and-stitch b01c01
  ↓ draft/b01-c01.md (clean) + draft/b01-c01.annotated.md
```

Reviews fire inline at each authoring level (audience + dramatist + auditor); `/and-review` is the post-hoc spot-check + sweep + orchestrator-critic verdict.

---

## What this framework does NOT do

- It does not measure prose quality. Stitcher draft prose is judged by `/and-stitch`'s own phases and (when revived) the polish-deferred `/and-wrap` pass.
- It does not guarantee a draft is good. A chapter can satisfy its substance contract and still be flat to read; substance is necessary but not sufficient.
- It does not handle world-detail consistency. Class/economic-level setting detail ("do smallfolk have salt?") is tracked OOS for follow-on.
- It does not enforce absolute length floors. The density-target is a ratio; the absolute-length floor mechanism is OOS for follow-on.
- It does not promise emotional-substance orthogonality. A contract movement on plot-axes alone is currently permitted; future work tags axes by class and HARD-faults emotional-flatness when stakes-events appear without emotional Δ.
