---
description: Decompose scene chunks into bones with per-bone state-deltas, then run the five-pass SVO pipeline + substance bone-gate. Emits the flattened bones file + scene-map facet. Replaces /and-protolines as the shoot-v2 chain entry. Usage - /and-write b<NN>c<MM> [revise|redo] [--from-signals]
---

Reads scene chunks + substance contracts produced by `/and-substance chapter`. **Decomposes each scene into bones-with-deltas, then SVOs them.** Produces the per-chapter flattened bones file at `theater/bones/<book>-<chapter>.md` + the scene-map facet at `theater/facets/scene-map-<book>-<chapter>.md`.

You are the orchestrator. Each pass is an Agent dispatch. Showrunner is read-mostly memory; do not dispatch showrunner.

Re-runnable per `design/substance/rerun-protocol.md`. Phase 7 emit pre-verifies URI-DIALOGUE-COVERAGE-GATE + URI-SCENE-WINDOW.

---

## SVO Discipline (the spine all five passes enforce)

A bone is **a subject doing something, optionally to object(s)**. Subject action, never subject non-action.

- Subject = one named entity (actor slug, prop slug, or `the <noun>`).
- Verb = one concrete physical action.
- Object(s) = zero or more named/quantified things acted upon.
- Object-as-subject form permitted when the actor is unknown/ambient (`the page tears`); optional `by <slug>` tail when the actor matters.
- **No modifiers** (no adjectives, adverbs, prepositional padding).
- **No copulas** (`is`, `was`, `will`, `am`, `are`, `were`, `be`, `been`, `being`).
- **No negations** (collapse to positive holds).
- **No interiority, no perception verbs.**
- **No conjunctions** (no `and`, `but`, `while`, `as`).
- Full schema: `schemas/bones.schema.md § field rules`.

**Speech-bone form (URI-DIALOGUE-COVERAGE-GATE anchor):** speech bones use the licensed dialogue form `<speaker-slug> speaks to <listener-slug>`. Non-`speaks to` speech forms (`says`, `tells`, `whispers`, etc.) are banned.

---

## Args

- `$1` (required) — chapter slug (e.g. `b01c01`).
- `$2` (optional positional) — `revise` or `redo` mode.
- `--from-signals` (optional, revise mode only) — scope revise to bones flagged SIGNAL by the prior `/and-write` Phase 6 bone-gate.

---

## Phase 0 — Validate + mode select

1. Resolve chapter slug. Parse `b<NN>c<MM>`.
2. Read `staff/showrunner/memory.md`. Confirm:
   - `chapters[<slug>]` exists.
   - `chapters[<slug>].status >= scened` (scene chunks authored). If `planned`, abort: `/and-write Phase 0 abort: chapter <slug> at status 'planned' — run /and-substance chapter <slug> first.`
   - For each scene: `scenes[].chunk` populated AND `scenes[].substance_delta` populated AND `scenes[].scene_conflict` populated. Any missing → abort: `/and-write Phase 0 abort: scene <slug> is unsubstanced — re-run /and-substance chapter <chapter-slug>.`
   - `chapters[<slug>].{pov_narrator, dramatic_shape, goal}` populated.
   - `project.series_audit.approved_at` set, `stale_since` null. If audit not approved → HARD-ABORT.
3. Check own output:
   - `chapters[<slug>].bones_file` set AND `theater/bones/<book>-<chapter>.md` exists on disk → re-run state.
   - In re-run state:
     - If `$2 = revise`: scope to specific scenes/bones. If `--from-signals` flag set, read `chapters[].scenes[].bones[].gate_verdict.signals[]`; offer SIGNAL-flagged bones/scenes for revise targeting. Else prompt for scope (named scenes or bone-range).
     - If `$2 = redo`: confirm; clear all bones + flat_ids; full Phase 1 re-run.
     - If `$2` omitted: prompt `revise` / `redo`.
4. **Behavior-card directory:** read `cards/dialects/INDEX.md` (the current path; `behaviors/` rename deferred). One-line edit if the rename lands later.
5. Cascade warning per `design/substance/staleness-cascade.md`. Any bone change drops `status` back to `bones-written` at Phase 7 emit and stale-marks facets + drafts.
6. **Per-scene gate_verdict clear (F3, revise mode).** Phase 0 clears `gate_verdict` only on bones inside scenes scoped by the revise target. Scenes not in scope keep their prior `bonefide: true` / `flat: false`. Phase 6 re-runs against the union of revised + unchanged scenes' bones, but only revised-scene bones can produce new gate_verdict writes.

Print:
```
Chapter: <slug>
Narrator: <pov-actor-slug>
Goal: <chapters[].goal>
Mode: fresh | revise | redo
Scenes: <N> (in revise scope: <list> or "all")
Beginning five-pass SVO + scene-decomposition + substance bone-gate.
```

---

## Phase 1 — Scene-decomposition (the work that used to be `/and-substance scene`)

**Net-new under the substance overhaul.** For each scene chunk in scope:

Dispatch **screen-writer** with:
- The scene chunk + scene's `substance_delta` + `scene_conflict`.
- The chapter's `dramatic_shape` + `goal` + `pov_narrator`.
- The parent book's `drama` + `substance_delta`.
- `series.substance.state_axes[]` (axis names, anchors, and per-axis allowed-direction context).
- `series.substance.cost_ledger[]` filtered to entries whose `anchor` resolves at-or-above this scene (so the screen-writer knows which costs need to be paid by bones in this scene).
- The active cast roster + active warehouse (locations, props, conditions).
- `cards/dialects/INDEX.md` for voice cards.
- `series.structure.book_length.bones_per_scene` range.

**Screen-writer task — per scene:**

1. Decompose the scene chunk into N bones, N inside `bones_per_scene` range (typical 5-15).
2. **Each bone takes one of three shapes** per the 2026-05-21 axis-bookkeeping split (`schemas/showrunner-memory.schema.md`):
   - **Moving bone (typical).** `axis_moves: [{axis, direction: up|down, magnitude: > 0}]` — one axis-movement (occasionally two for hinge bones). Cost links to `series.substance.cost_ledger[].id` when applicable.
   - **Held bone (discipline-enacting).** `axis_moves: []` + `axes_held: [{axis, rationale}]` — the SVO enacts a discipline that holds an axis flat (e.g. `taylor holds the feet` enacts capability-held). The held axis is load-bearing for the scene's stakes; `rationale` names the discipline.
   - **Chatter bone (setup / transition).** `axis_moves: []` + no `axes_held` — pure setup/transition, allowed only when it pays a later gain (`cost_ledger_anchor` REQUIRED). Trim pass culls chatter over the density cap.
   Scene-action-sized in all three cases: one scene-significant action per bone, not micro-beats. `direction: null` / `magnitude: 0` in `axis_moves[]` is malformed (Phase 2 `FAULT-BONE-DELTA-MALFORMED`).
3. The scene's `substance_delta` is the **aggregation target**: per-axis sum of bone-Δ from `axis_moves[]` must equal scene's `axes_in_motion[<axis>]` target within ±1 rank. Held axes contribute zero by definition and must each have at least one bone in the scene with that axis in its bone-level `axes_held[]`.
4. Honor `scene_conflict`: the protagonist_force is visible across multiple bones; the opposing_force is visible in at least one bone (or HARD `OPPOSING-FORCE-MISSING` at Phase 6). In held-discipline scenes, the opposing_force may be enacted by the held bone itself (the rule catches the assessment; the body holds against pressure) — the rationale on `axes_held[]` should name how the bone-level enactment satisfies the opposing-force requirement.
5. Author with full SVO discipline. Speech bones use `speaks to` form.

Each bone is appended to `chapters[<chapter>].scenes[<scene>].bones[]` in memory with `slug: b<NN>c<MM>s<KK>n<II>` (auto-generated). `flat_id` is NOT yet assigned (Phase 7 owns flat_id assignment).

**Forbid loading:** other chapters' bones files, audience personas, source prose, deprecated v1 script bullets.

After Phase 1: bones present in memory, scene-decomposed, with declared per-bone substance_delta. No SVO craft work yet.

---

## Phase 2 — Constraint audit (auditor fork)

Dispatch **auditor** (fork) with:
- The Phase 1 bones for the scenes in scope.
- `schemas/bones.schema.md` + harsh-SVO rules.
- Full content of every active cond-* card (under `active-project/warehouse/`).
- `series.laws` + `series.lore`.
- Active location cards (physical-possibility checks).
- `series.substance.state_axes[]` + `series.substance.cost_ledger[]`.
- Per-scene `substance_delta` + `scene_conflict`.

**Auditor brief.** Classify each bone as CORRECT or FAULT-{class}. Fault classes:

| class | meaning |
|---|---|
| FAULT-FORM | SVO shape violation (copula, negation, conjunction, modifier, perception verb, interiority — per `schemas/bones.schema.md`) |
| FAULT-CONSTRAINT | Violates a cond-* card, series law, or lore fact |
| FAULT-PHYSICAL | Prop not on set, actor not present, exit doesn't exist |
| FAULT-BONE-DELTA-MALFORMED | `substance_delta.axis_moves[].axis` not in `series.substance.state_axes[].slug`; `axis_moves[].direction` not in `{up, down}` (null / `~` / `+` / `-` all malformed); `axis_moves[].magnitude` not strictly positive (zero or negative malformed — use `axes_held[]` for held-flat axes or empty `axis_moves: []` for chatter bones); magnitude outside `chunk_targets.bone.delta_per_axis`; cost lists an axis not in scene's `substance_delta.axes_in_motion[]` or in cost_ledger anchor scope; `axes_held[]` entry missing `rationale` field; `axes_held[]` entry's axis not in `series.substance.state_axes[].slug`; chatter bone (`axis_moves: []` + no `axes_held`) without `cost_ledger_anchor` (chatter bones must pay a later gain) |
| FAULT-AGGREGATE-DELTA-MISMATCH | Aggregate per-axis bone-Δ for this scene differs from scene `substance_delta` by more than ±1 rank |
| FAULT-COST-LEDGER-UNRESOLVED | `bones[].substance_delta.cost_ledger_anchor` points at an id missing from `series.substance.cost_ledger[]` |

Auditor returns classified report at `staff/auditor/write-<chapter>-pass2.md` per `schemas/audit-report.schema.md`.

**Fault routing:** faults route to **fixer** with minimum-change directive. Fixer logs to `staff/fixer/fixer-log.md`.

**Pass 2 terminates** when the auditor's report is empty (no faults). Otherwise: fix, re-run Pass 2 only.

---

## Phase 3 — Shape (dramatist)

Dispatch **dramatist** with:
- Constraint-clean bones from Phase 2.
- Chapter `goal` + `dramatic_shape` + chapter `substance_delta`.
- Book `drama` + book `substance_delta`.
- `series.substance.state_axes[]` + `series.substance.antagonist_pressure[]`.
- Per-scene `substance_delta` + `scene_conflict`.
- Behavior cards for the active cast (per `cards/dialects/INDEX.md`).

**Forbid loading:** vibes, audience personas, raw constraint cards.

**Dramatist task:**
- Output a bone-order list reflecting the desired sequence inside each scene (cross-scene ordering is fixed by scene order; intra-scene reordering is the dramatist's call).
- Output a flagged-missing-transition list: where a beat is missing and what state-change it should bridge.

**Dramatist may not author lines.** Missing transitions route back to screen-writer with a one-line brief; screen-writer authors only the additions; Pass 2 re-runs on additions only.

Apply the order list by re-arranging bones in memory. **Bone slugs do not change** — only order. (`flat_id` is assigned at Phase 7 in final order.)

**Speech-bone licensed-form check.** Dramatist verifies every speech-class bone uses `speaks to` form. Non-conforming forms route to fixer.

**Pass 3 terminates** when dramatist returns an unchanged order list + empty missing-transition list.

---

## Phase 4 — Trim (audience, 3 personas)

Dispatch the three audience personas in parallel, each loaded with:
- The re-shaped bones.
- Chapter `goal` (the north star).
- `series.theme` + chapter `substance_delta` + per-scene `substance_delta` + `scene_conflict`.
- The persona's own card + STM.
- Series vibe-cloud (`series.vibe_cloud.keys`) + book vibe-cloud (`books[<book>].vibe_cloud.keys`) ONLY — chapter / scene / bone level vibes deprecated under the substance overhaul.
- Studio vibes (`staff/studio/vibes.md`).

**Forbid loading:** raw constraints, behavior cards, calls list.

**Per-persona output:**
- Per-bone deletion proposals (bones that don't serve `goal` and aren't voice-load-bearing OR don't cause declared Δ).
- File-level verdict: ACCEPT or REVISE-{one-clause-reason}.

**Trim criterion (changed under substance overhaul):** chatter bones — bones with **empty `substance_delta.axis_moves`** AND no cost-ledger-paying role — are schema violations, not style. Drop them.

**Threshold for deletion:** ≥2 personas propose deletion → auto-accept. 1 persona → advisory; orchestrator decides.

Apply deletions by removing bones from memory. **Do not renumber.** Slugs become non-monotonic; that's expected.

**Pass 4 terminates** when all three personas ACCEPT in one round. Max 2 revise rounds; on the third, ship with audience flags annotated and flag for downstream review.

---

## Phase 5 — Continuity audit (auditor, second fork, fresh context)

Dispatch **auditor** (fork, second invocation) with:
- The post-trim bones.
- Chapter `goal` + chunk + `dramatic_shape`.
- Active location cards.
- Active cast roster.
- `series.laws`.
- **Prior chapter's `handoff_out`** (for the chapter immediately before the current one in chapter order). Reads `chapters[<prior-slug>].handoff_out` from showrunner memory — a structured read, not the prior bones file.

**Forbid loading:** vibes, audience personas, behavior cards, other chapters' bones files.

**Auditor brief.** Classify the chapter as CONTINUITY-OK or report classified faults:

| class | meaning |
|---|---|
| FAULT-REACHABILITY | Chapter goal not delivered by surviving bones; chapter handoff_out not consistent with what the bones leave behind |
| FAULT-STATE | Prop referenced after deletion of placement; actor in two locations; time/location inconsistency around time-skip blank-numbered lines |
| FAULT-REFERENCE | Cast slug doesn't resolve; prop/location not on set |
| FAULT-POV | Perception-verb leak on POV character; narrator inconsistent with the SVO subject pattern |
| FAULT-HANDOFF-IN-MISMATCH | `chapters[<slug>].handoff_in` is not honored by the chapter's opening bones (open_threads not picked up; world_state contradicted; character_state ranks contradicted) |

Auditor returns report at `staff/auditor/write-<chapter>-pass5.md`.

**Fault routing:** route to fixer for targeted repair. After repair, re-run Pass 5 only.

**Pass 5 terminates** when the auditor returns CONTINUITY-OK with empty faults.

---

## Phase 6 — Substance bone-gate

**Replaces URI-026 tens-gate.** This is the substance overhaul's primary authoring gate. Dispatch **auditor** (third fork) + the three **audience personas** in parallel against scene-window slices.

**Frame-coda exemption (2026-05-21).** If `chapters[<slug>].substance_delta.chapter_class: frame-coda` is set, Phase 6 substance bone-gate is skipped entirely. Frame-coda chapters (e.g. archmaester-retrospective interludes) are reviewed for frame-shape by dramatist only; their bones do not need to deliver protagonist-axis Δ. Phase 7 emission proceeds without bone-gate verdict writes.

### Per-bone verification (auditor)

For each bone, classify by shape (per the 2026-05-21 axis-bookkeeping split):

**Moving bones (`axis_moves` non-empty):**
- **Bonefide check:** the SVO physically causes the declared Δ. "maya confronts tomas, +2 community, -1 emotional" is bonefide if confronting tomas plausibly causes those movements given the scene contract. "maya enters the yard, +2 community" is not bonefide.
- **Rank claim has visible cause:** no axis-move without a physical action that drives it. Otherwise `SUBSTANCE-FLAT-<axis>` (HARD).

**Held bones (`axis_moves: []` + `axes_held` non-empty):**
- **Discipline-enactment check:** the SVO enacts a stillness-against-pressure / dormancy / restraint pattern on the held axis. Licit verbs: `holds` (narrow body-part-stillness license per `schemas/bones.schema.md`), bare-action-with-discipline-rationale (e.g. `the insects fill the block` with `axes_held: [{axis: capability, rationale: "ambient-drift verb; rule holds capability at rank N"}]`). The rationale must name the discipline the bone enacts. Otherwise `HELD-AXIS-NOT-ENACTED` (HARD).
- **Held axis is load-bearing:** the held axis must appear in the scene's `axes_held[]` list (parent contract) OR the scene's `scene_conflict.stakes_axis` resolves to this axis. A bone-level `axes_held` entry on an axis the parent scene didn't declare is `HELD-AXIS-UNCONTRACTED` (HARD).

**Chatter bones (`axis_moves: []` + no `axes_held`):**
- **Cost-ledger payment check:** must have `cost_ledger_anchor` pointing at a `series.substance.cost_ledger[]` entry that resolves at-or-under this scene. Otherwise `CHATTER-UNPAID` (HARD).
- **Density-cap check:** count of chatter bones per scene cannot exceed `(1 - density_target.min) × bone_count`. Beyond → SIGNAL `CHATTER-OVER-CAP` (the trim pass should have culled).

### Per-scene verification (auditor)

For each scene:
- **Per-axis Δ delivered within ±1 rank of contract (axes_in_motion only):** aggregate bone-Δ on each axis is within ±1 of `scenes[].substance_delta.axes_in_motion[]` where `axes_in_motion[].axis == <axis>`. Beyond ±2 → HARD `AXIS-DELTA-MISMATCH`; ±1-±2 → SIGNAL. Held axes contribute zero by definition and are not checked under this rule.
- **Held axes have bone-level enactment:** for each entry in `scenes[].substance_delta.axes_held[]`, at least one bone in the scene must have that axis in its bone-level `axes_held[]`. Otherwise `HELD-AXIS-NOT-WITNESSED` (HARD).
- **`scene_conflict.stakes_axis` is in union:** resolves to either `scenes[].substance_delta.axes_in_motion[<axis>]` OR `scenes[].substance_delta.axes_held[<axis>]`. Otherwise `STAKES-AXIS-MISSING` (HARD).
- **`scene_conflict.opposing_force` visible:** at least one bone shows the opposing force pushing. In held-discipline scenes (stakes_axis ∈ axes_held), a bone whose `axes_held` rationale names the opposing-force enactment satisfies this check (the rule catching the pull is the opposing force made visible). Otherwise `OPPOSING-FORCE-MISSING` (HARD).
- **Cost-ledger entries paid by visible bones:** for each `series.substance.cost_ledger[]` entry whose anchor resolves at-or-under this scene, at least one bone has `substance_delta.cost_ledger_anchor` matching the entry's id AND the bone's cost direction matches. Otherwise `SUBSTANCE-SUSPECT-cheap-gain-<axis>` (HARD) OR `COST-NOT-PAID` (HARD).

### Per-scene-window audience review

Each of the three audience personas reviews per scene window:
- `SUBSTANCE-FELT` PASS — the scene's declared Δ lands felt by this persona.
- `SUBSTANCE-FLAT-<axis>` HARD — the persona doesn't feel the declared movement on `<axis>`.
- `SUBSTANCE-SUSPECT-cheap-gain-<axis>` HARD — the persona feels the gain but doesn't feel the cost.

**Per-scene coverage discipline (URI-WRITE-BONE-GATE-COVERAGE, A9 — 2026-05-21).** Every scene in the chapter must be reviewed by all three personas. Output: one verdict file per persona, with an explicit per-scene block for EVERY scene in the chapter. The verdict file shape:

```yaml
---
reviewer: <persona-slug>
chapter: <chapter-slug>
phase: write-bone-gate
date: <YYYY-MM-DD>
scenes_reviewed: [<scene-slug>, <scene-slug>, ...]   # MUST equal the chapter's full scene list
---

## scene <scene-slug>
verdict: SUBSTANCE-FELT | SUBSTANCE-FLAT-<axis> | SUBSTANCE-SUSPECT-cheap-gain-<axis>
<reasoning>

## scene <scene-slug>
verdict: ...
...
```

Orchestrator validation: before persisting bone-gate verdicts, verify `scenes_reviewed[]` in every persona's verdict file equals the chapter's full scene list (`chapters[<slug>].scenes[].slug`). If any scene is missing from any persona's coverage, **HARD-ABORT:** re-dispatch that persona with the missing scenes named in the brief. **Promoted from b01c01 audit-gap discovered post-hoc: s03 was never voted by the audience trio in the bone-gate; only the auditor covered it. The per-scene coverage check makes coverage gaps mechanically detectable instead of discovery-by-postmortem.**

### HARD / SIGNAL classification

| finding | severity |
|---|---|
| flat-bone, cost-not-paid, missing-opposing-force, per-axis-Δ-mismatch beyond ±2, SUBSTANCE-FLAT, SUBSTANCE-SUSPECT | HARD (blocks emission) |
| bones-count-below-density-target, per-axis-Δ-mismatch ±1 to ±2, chatter-bone just-over-cap | SIGNAL (records but passes) |

**HARD findings block Phase 7 emission.** Re-fire Phase 1 (scene-decomposition) on the offending scenes; cycle 1 of the same `/and-write` invocation; max 2 internal HARD-resolution cycles. After 2 cycles, surface to user.

**SIGNAL findings record but pass.** They land in `chapters[].scenes[].bones[].gate_verdict.signals[]` for later `/and-write revise --from-signals` targeting or `/and-review bones <chapter>` post-hoc inspection.

Write `gate_verdict` per bone on PASS only — HARD findings block emission, so no PASS-state is written for bones inside a failing scene.

Save full bone-gate report to `staff/auditor/write-<chapter>-bone-gate.md`.

---

## Phase 7 — Emit + downstream-gate pre-verify + scene-map co-emit

Two artifacts written, both derived from `chapters[].scenes[].bones[]` in showrunner memory.

### (a) Flattened bones file

`active-project/theater/bones/<book>-<chapter>.md` — conforms to `schemas/bones.schema.md`:

**Step 1 — flat_id assignment.** Walk scenes in order; for each scene walk bones in order; assign each bone a monotonic positive `flat_id` starting at 1, file-scoped. Persist `bones[].flat_id` to memory. In revise mode: preserve flat_ids for unchanged bones; revised bones get new flat_ids via gap-filling within the chapter to keep monotonicity tight.

**Step 2 — header.** Write the 7-field extended header:

```
# bones — <chapter-slug>

episode: <chapter-slug>
narrator: <chapters[].pov_narrator>
goal: <chapters[].goal>
cast: <comma-list>
locations: <comma-list>
prior_episode: <prior-chapter-slug | none>
aggregate_range: 1-<N>
```

- `cast:` computed via slug-grep over the chapter's bone SUBJECTs + `speaks to` listeners. Order: by first-appearance flat_id.
- `locations:` computed via slug-grep over OBJECTs/SUBJECTs resolved against warehouse loc cards.
- `prior_episode:` = the previous chapter's slug in chapter order, or `none` for first-chapter-of-first-book.
- `aggregate_range:` = `1-<N>` where N = max(flat_id).

Field name `episode:` is preserved for downstream-compatibility with `/and-facets` Phase 0 parser. Value is the chapter slug.

**Step 3 — body.** Plain SVO lines, one bone per line, blank-numbered-ID lines for time-skips, no scene markers, no YAML metadata, no facet pre-tags, no per-bone substance annotations (substance_delta lives only in memory).

### (b) Scene-map facet

`active-project/theater/facets/scene-map-<book>-<chapter>.md` — conforms to `schemas/scene-map.schema.md`. Emitted directly from `scenes[]`:
- One scene-map entry per scene.
- Bone-range computed from the flat_ids of bones inside each scene.
- Scene boundaries, scene chunks, scene_conflict, and substance_delta carried forward.

This **replaces** `/and-facets` Phase 4d derivation; `/and-facets` Phase 4d downgrades to coverage-validation only.

### Downstream-gate pre-verify (HARD, blocks write)

1. **URI-DIALOGUE-COVERAGE-GATE.** Every `speaks to` bone has a speaker AND a listener resolvable from the cast roster. Speech bones' `substance_delta` lists at least one communication-class axis (community / knowledge / reputation / trust).
2. **URI-SCENE-WINDOW.** Every bone lands inside exactly one scene's flat_id range; no dangling anchors; no scene-spanning bones.

Both pre-verifications run before write. HARD-fail aborts emission with the offending bone(s) named.

### Memory updates

- Set `chapters[<slug>].bones_file = theater/bones/<book>-<chapter>.md`.
- Set `chapters[<slug>].bones_count = <N>`.
- Set `chapters[<slug>].substance_bone_gate_verdict = PASS`.
- Set `chapters[<slug>].substance_delta_measured.{axes_moved, density_measured, felt_verdict}`.
- Set `chapters[<slug>].status = bones-written` (G1 — even in revise mode, regardless of partial scope).
- Stale-mark downstream artifacts (facet outputs, draft) per `design/substance/staleness-cascade.md`.

### Emit-summary surfacing (F3 — SIGNAL discoverability)

```
/and-write <chapter>: PASS. <N> bones across <S> scenes. Bones file: theater/bones/<book>-<chapter>.md
                                                          Scene-map: theater/facets/scene-map-<book>-<chapter>.md

Bone-gate verdict: PASS (HARD: 0, SIGNAL: <K>, TASTE: 0).
```

If SIGNAL count > 0, append:

```
<K> SIGNAL findings recorded — see `/and-review bones <chapter>` to inspect, or
                                  `/and-write <chapter> revise --from-signals` to address.
```

```
next: /and-facets <chapter>
```

---

## Convergence

The pipeline converges when **all five passes plus the substance bone-gate produce clean verdicts in a single end-to-end run**. A change at any pass invalidates downstream passes for that run; downstream re-runs from the changed point. Maximum 3 full pipeline iterations; on the third, ship with reviewer flags annotated and surface to user.

Substance bone-gate cycles are capped at 2 internal re-fires (Phase 1 re-decompose offending scenes → Phase 2-5 → Phase 6 re-fire). After 2 cycles, surface to user.

---

## Re-run notes

- **revise** mode without `--from-signals`: user names scenes or bone-ranges to re-decompose.
- **revise --from-signals**: read `bones[].gate_verdict.signals[]`; offer SIGNAL-flagged bones/scenes for revise targeting; user picks subset.
- **redo**: scene chunks preserved; all bones cleared; full Phase 1-7 re-run.
- Per-scene gate_verdict clearing (F3): only bones inside revised scenes get verdict cleared.
- Any bone change drops chapter status to `bones-written` at Phase 7 emit, regardless of partial scope. Downstream artifacts stale-marked.

---

## Notes

- Citations in bones stay empty here. They accrue at facet-authoring time per `schemas/bones.schema.md § citations`.
- Per-bone `substance_delta` lives only in showrunner memory. The bones file is comment-clean.
- Audience and dramatist are stateful within an invocation. Their STM is loaded at each dispatch and updated after each verdict.
- `tens:` citation prefix is removed from the recognized list (`schemas/bones.schema.md § citation prefixes`) — tensometer dropped.
