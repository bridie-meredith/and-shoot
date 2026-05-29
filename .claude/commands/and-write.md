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
7. **Parking-lot scan (Rule 14).** Read `active-project/staff/showrunner/parking-lot.md`. Items matching this invocation (`target.command: /and-write` + `target.scope` = chapter slug or `*` wildcard + `status: open`): HARD → abort unless this run resolves; SOFT → carry to Phase 7 summary (Wren-style prose-texture watches typically resolve at Phase 1 scene-decomposition or Phase 4 prose trim). Resolving phase stamps `resolved_at` + `resolved_by` + `resolution_note`; never delete.

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
6. **Sensory-grounding quota (URI-WRITE-SENSORY-GROUNDING — fixes the recurring modality-floor breach).** The decomposer owns the physical world. Every scene's bone set must include grounding bones — bones whose SVO is a concrete physical action situated in the scene's location, naming a physical object, surface, or sensory particular of the place — not only the protagonist's perceptual postures (`lifts the eyes`, `faces the alley-mouth`, `works the net`). Minimum one grounding bone per scene; for scenes longer than the `bones_per_scene` midpoint, scale toward roughly one grounding bone per five bones. A scene whose bone set is entirely perceptual posture / abstraction gives the facet layer nothing physical to anchor to and forces the sensory facet to collapse to a single modality (the c01 *and* c02 failure — a "documented trade-off" that fires every chapter is not a trade-off, it is the system's actual output). Grounding bones are normal moving / held / chatter bones — the quota is about the SVO being physically concrete and place-situated, not a new bone shape.
7. **Event-coverage map (URI-WRITE-EVENT-COVERAGE — fixes the b01c02 hollow-chapter root cause; tightened 2026-05-25 to close the c01 mechanism-gap).** Two-source mandatory coverage:
   - **(a) Mechanical chunk-tag extraction (URI-CHUNK-TAG-PROTOCOL — the lightening leg).** Read the scene chunk and extract every inline `[event: <name>]` / `[image: <name>]` / `[force: <name>]` / `[mechanism: <name>]` tag authored at `/and-substance chapter`. **Each tagged span becomes a mandatory `event_map[]` entry.** The chunk-author already decided what's load-bearing; the bone-author does not re-litigate. This is mechanical extraction, not judgment.
   - **(b) Author-noticed events (the existing rule, scoped down).** The bone-author may add additional `event_map[]` entries for events / images / forces / mechanisms they notice but the chunk did not tag. Encouraged where the chunk is older than the current substance contract; not required.

   For every `event_map[]` entry, name the bone(s) (≥1) that cover it. If an entry has no covering bone, the bone-author MUST either add a bone for it or log a deliberate omission with a one-line `omission_rationale`. **A tagged span (leg a) cannot be omitted via "no bone added" — only via explicit `omission_rationale`.** The decomposition is not complete until every entry maps to ≥1 bone or carries a non-null `omission_rationale`. Authoring-time requirement; the bone-author cannot finish Phase 1 without it. A rescue, a verdict, a threat materializing, a witness reacting are *events*, not perceptual postures; the event-coverage map exists because the SVO bone format stores actions cleanly but stores the causal relations *between* actions (the substance of a rescue, an accounting, a turn) only in the gaps between bones — and the gaps have no schema slot. The map forces those events to become bones rather than dissolving. Persist the result to `chapters[].scenes[].event_map[]` per `schemas/showrunner-memory.schema.md`. **Back-compatibility:** chunks authored before URI-CHUNK-TAG-PROTOCOL (pre-2026-05-25) that contain zero `[*:*]` tags fall back to leg (b) only — the bone-author extracts named events / load-bearing images themselves, as in the pre-tightening rule.

Each bone is appended to `chapters[<chapter>].scenes[<scene>].bones[]` in memory with `slug: b<NN>c<MM>s<KK>n<II>` (auto-generated). `flat_id` is NOT yet assigned (Phase 7 owns flat_id assignment).

**Forbid loading:** other chapters' bones files, audience personas, source prose, deprecated v1 script bullets.

After Phase 1: bones present in memory, scene-decomposed, with declared per-bone substance_delta. No SVO craft work yet.

---

## Phase 1.5 — Dialogue authoring (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25)

**Dialogue ships with bones.** Per the principal's 2026-05-25 ruling, dialogue is inseparable from the bones it anchors to — the dialogue facet is no longer a downstream `/and-facets` concern, it is part of what `/and-write` emits.

### 1.5a — Identify dialogue-anchor bones

A **dialogue-anchor bone** is one of:
- A canonical speech-form bone (`<speaker-slug> speaks to <listener-slug>`).
- A licensed action-form bone whose `substance_delta.axis_moves[]` (or `axes_held[]`) declares a communication-class axis movement (community / knowledge / reputation / trust) AND whose scene chunk text licenses a speech-act at that bone. The c01 b01 `taylor raises the voice` anchor (parking-lot disposition pl-2026-05-25-004 routing (a)) is the canonical example; the form discipline preserved flat_id stability while letting the bone carry dialogue.

For each scene in scope, walk `chapters[].scenes[].bones[]` and mark each dialogue-anchor bone. Build the `speakers` inventory (set of distinct speaker slugs across anchors).

### 1.5b — Dispatch dialogue-writer (per-behavior-card fanout)

For each distinct behavior card present in the speakers set (resolved by reading `cards/dialects/<character-slug>.card.md` per `cast:` slug and grouping by card), fan out one `general-purpose` dispatch in a parallel block. Each fork authors all speakers sharing that card.

Each fork carries:
- Behavior card stack (margit-composed: leaf → `inherits:` parent → universal overlay → `references:` adjacent cards).
- Speaker persona + ltm + stm + state for every speaker the fork covers.
- The list of dialogue-anchor bones for the fork's speakers, with per-bone substance_delta + the bone's owning scene's `substance_delta` + `scene_conflict`.
- `staff/dialogue-writer/rubric-dialogue.md` (the v1 round-trip writer-pattern rubric).
- `schemas/dialogue.schema.md`.

**Discipline:** eight v1 round-trip writer patterns (per-card forks, card-stack load order, blind to other R1 facets, intent-as-state, multi-draft + chosen-mark, affirmative card-signature citation, anti-patterns explicit, calibration anchor) — all load-bearing per the rubric. The fork is blind to other facets (none exist yet at this phase — `/and-facets` hasn't run). The fork authors verbatim utterances + objectives per anchor bone.

**Output:**
- Per-character dialogue files at `active-project/theater/dialogue/<character-slug>.md` per `schemas/dialogue.schema.md`.
- Per-character drafts sidecar at `active-project/staff/dialogue-writer/<character-slug>.drafts.md` (multi-draft + chosen-mark + card-signature citations).
- In-memory annotation: `chapters[].scenes[].bones[].dialogue_citations[]` populated with `<character-slug>:<id>` tokens for each dialogue-anchor bone whose entries the fork authored. (Used by Phase 7 to emit citation tokens in the bones file.)

**Forbid loading:** facet rubrics (no facets exist yet), source prose, behavior cards not in this fork's domain.

### 1.5c — Dialogue-only scenes

If a scene has zero dialogue-anchor bones (an entirely silent scene), no dispatch fires for that scene. This is valid — many scenes are bodies-only. Phase 6 verifies coverage; bare-anchor-without-utterance is a HARD finding.

### 1.5d — Cap on add-cycles

If a dialogue-writer fork's output fails Phase 6 dialogue checks (see below), one re-dispatch per fork is permitted within the same `/and-write` invocation. Second failure surfaces to the user.

After Phase 1.5: per-character dialogue files present on disk; bone dialogue_citations populated in memory; behavior-card fences enforced inline by the writer fork. Phase 6 verifies.

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

**Replaces URI-026 tens-gate.** This is the substance overhaul's primary authoring gate. Dispatch **auditor** (third fork) + the three **audience personas** in parallel against scene-window slices. The auditor's payload includes, per scene: the bones, the scene chunk text, `scene_conflict`, `substance_delta`, and `event_map[]` — the event-presence check below reads the chunk text and `event_map[]`, so both must be in the brief.

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
- **Event-presence check (URI-WRITE-EVENT-COVERAGE — HARD).** Read `scenes[].event_map[]`. For every entry, confirm the named bone(s) still exist in the post-trim bone set and that the entry's event is actually carried by them (the bone SVO physically *is* the event, not a perceptual posture *about* it). Additionally, independently confirm the scene chunk's central event and its `scene_conflict.protagonist_force` each appear as ≥1 bone — this is checked against the chunk text, not only against the event_map (an event_map that omitted the central event is itself the defect). An event_map entry whose covering bones were trimmed away with no `omission_rationale`, or a central event / protagonist_force with no bone, is `EVENT-UNCOVERED-<event>` (HARD). "Axes moved" and "the scene happened" are different claims; this check gates the second. A scene can pass every axis-tick check and still fail here — that is the intended catch.
- **Chunk-tag completeness check (URI-WRITE-EVENT-COVERAGE / URI-CHUNK-TAG-PROTOCOL — HARD; 2026-05-25 tightening).** Mechanically parse the scene chunk text for every inline `[event: <name>]` / `[image: <name>]` / `[force: <name>]` / `[mechanism: <name>]` tag. For each tag, confirm a corresponding `event_map[]` entry exists (`event:` field matches the tag's `<name>` or the entry explicitly references the tag via the `omission_rationale`). A tagged span absent from `event_map[]` is `EVENT-MAP-INCOMPLETE-<tag-name>` (HARD). The tightening closes the failure mode where chunk-author intent ("how the swarm physically parts the crowd" tagged at /and-substance) is silently dropped at bone-decomposition time; the URI-WRITE-EVENT-COVERAGE event-presence check above gates the *coverage of map entries by bones*, this check gates the *coverage of chunk tags by map entries*. Both legs must pass. For chunks that contain zero `[*:*]` tags (pre-2026-05-25 chunks), this check is N/A — the existing event-presence check carries the gate alone.
- **Per-axis Δ delivered within ±1 rank of contract (axes_in_motion only):** aggregate bone-Δ on each axis is within ±1 of `scenes[].substance_delta.axes_in_motion[]` where `axes_in_motion[].axis == <axis>`. Beyond ±2 → HARD `AXIS-DELTA-MISMATCH`; ±1-±2 → SIGNAL. Held axes contribute zero by definition and are not checked under this rule.
- **Stakes-axis-dominant check (URI-WRITE-STAKES-AWARE — HARD).** When `scene_conflict.stakes_axis` resolves to an `axes_in_motion[]` axis, that axis's delivered aggregate magnitude MUST be the largest delivered delta in the scene. If a non-stakes axis delivers a larger aggregate than the declared stakes axis, the scene is mis-shaped — `STAKES-AXIS-NOT-DOMINANT` (HARD). (A scene of *watching* delivering a knowledge overrun while its declared capability stakes axis under-delivers is the canonical failure this catches.) When `stakes_axis` resolves to an `axes_held[]` axis, this check is N/A (held axes deliver zero by design).
- **Underdelivery-rationale check (URI-WRITE-STAKES-AWARE — HARD).** For every `axes_in_motion[]` axis whose delivered aggregate magnitude is below 50% of its `target_delta_magnitude`, the scene must carry an explicit one-line rationale (logged in the bone-gate report) for the shortfall. An axis under 50% of target with no rationale is `AXIS-UNDERDELIVERED-<axis>` (HARD) — the ±1 tolerance band is not wide enough to silently absorb a headline axis realized at 40% of target.
- **Sensory-grounding check (URI-WRITE-SENSORY-GROUNDING — HARD).** The scene's bone set must contain ≥1 grounding bone (a concrete, place-situated physical action — see Phase 1 step 6). A scene whose entire bone set is perceptual posture / abstraction is `SENSORY-GROUNDING-ABSENT` (HARD) — it is a bones-revise trigger, not a downstream facet trade-off. The facet layer cannot author a physical world the bones did not give it; a sensory-empty bone set must fail here, at authoring time.
- **Central-event concreteness check (URI-WRITE-EVENT-CONCRETENESS — HARD; 2026-05-29).** The ≥1-grounding-bone floor above is a floor of *one*; this check protects the *spine* specifically. The bone(s) carrying the scene's central event — the event the scene chunk / `event_map[]` names as the scene's reason to exist — must themselves be grounding-class: a concrete actor-verb-object physical action, NOT an instrument/process/perception rendering of the event. `the three figures strike the courier` passes; `the feed flags the contact` does not (the event reaches the bone only through the apparatus). A central-event bone rendered process-first is `EVENT-NOT-CONCRETE-<event>` (HARD) — spine legibility cannot be deferred to the facet/stitch layer, which is exactly where it gets lost (the c05 muffle mechanism). **Scope caveat:** this catches a central event authored *abstractly at the bone*; it does NOT and cannot prevent a *concrete* bone being *rendered* abstractly at stitch — that airless-voice failure mode lives at the stitch/voice layer, not here.
- **Abstraction-dominance check (URI-WRITE-EVENT-CONCRETENESS — SIGNAL; 2026-05-29).** If grounding-class bones number fewer than `ceil(0.25 × (bone_count − chatter_count))` in a scene, fire `ABSTRACTION-DOMINANT` (SIGNAL): the ≥1 floor is satisfied but the scene is carried overwhelmingly by perception/process verbs and will read airless downstream. Disposition: accept-with-rationale (stylized instrument-POV intentional — log the one-line rationale in the bone-gate report) or remediate (add grounding bones). A calibration signal, not a hard gate — some POVs are legitimately abstract, and the call is the author's with the rationale on record.
- **Held axes have bone-level enactment:** for each entry in `scenes[].substance_delta.axes_held[]`, at least one bone in the scene must have that axis in its bone-level `axes_held[]`. Otherwise `HELD-AXIS-NOT-WITNESSED` (HARD).
- **`scene_conflict.stakes_axis` is in union:** resolves to either `scenes[].substance_delta.axes_in_motion[<axis>]` OR `scenes[].substance_delta.axes_held[<axis>]`. Otherwise `STAKES-AXIS-MISSING` (HARD).
- **`scene_conflict.opposing_force` visible:** at least one bone shows the opposing force pushing. In held-discipline scenes (stakes_axis ∈ axes_held), a bone whose `axes_held` rationale names the opposing-force enactment satisfies this check (the rule catching the pull is the opposing force made visible). Otherwise `OPPOSING-FORCE-MISSING` (HARD).
- **Cost-ledger entries paid by visible bones:** for each `series.substance.cost_ledger[]` entry whose anchor resolves at-or-under this scene, at least one bone has `substance_delta.cost_ledger_anchor` matching the entry's id AND the bone's cost direction matches. Otherwise `SUBSTANCE-SUSPECT-cheap-gain-<axis>` (HARD) OR `COST-NOT-PAID` (HARD).

### Per-chapter verification (auditor)

- **Register-as-mannerism check (URI-WRITE-REGISTER-MANNERISM — SIGNAL; 2026-05-24).** Across the chapter's full bone set, count occurrences of each unique SVO `VERB OBJECT` pair (subject-independent). If any single `VERB OBJECT` pair appears in ≥3 bones, fire `REGISTER-AS-MANNERISM-<verb-object>` (SIGNAL) — the load-bearing idiom has graduated to register tic. Promoted from the b01c01 post-ship audit (worm-canon-pedant flagged "I held the eyes" appearing at L11/L19/L25 in twenty-seven lines as the discipline tic showing through). The check runs on the post-trim bone set. Disposition options: remediate (recast 1+ of the recurring bones to a synonymous beat) or accept-with-rationale (the recurrence is intentional refrain). The bare-intransitive exception (`exhales`, `breathes`) does not apply — those have no OBJECT to count against. The dialogue form `<speaker> speaks to <listener>` is exempt — repeated speech bones across a conversation are not mannerism.

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
| flat-bone, cost-not-paid, missing-opposing-force, per-axis-Δ-mismatch beyond ±2, SUBSTANCE-FLAT, SUBSTANCE-SUSPECT, EVENT-UNCOVERED, EVENT-MAP-INCOMPLETE, STAKES-AXIS-NOT-DOMINANT, AXIS-UNDERDELIVERED, SENSORY-GROUNDING-ABSENT, **EVENT-NOT-CONCRETE**, **FAULT-DIALOGUE-MISSING-AT-ANCHOR, FAULT-DIALOGUE-CARD-VIOLATION, FAULT-DIALOGUE-OBJECTIVE-MISSING, FAULT-DIALOGUE-EARTH-BET-FENCE** | HARD (blocks emission) |
| bones-count-below-density-target, per-axis-Δ-mismatch ±1 to ±2, chatter-bone just-over-cap, register-as-mannerism (verb-object pair ≥3 occurrences), **ABSTRACTION-DOMINANT (grounding bones < 25% of non-chatter bones)** | SIGNAL (records but passes) |

### Dialogue checks (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25)

Phase 6 now verifies the Phase 1.5 dialogue output as part of the bone-gate (since dialogue ships with bones):

- **FAULT-DIALOGUE-MISSING-AT-ANCHOR (HARD)** — a dialogue-anchor bone has zero entries in any per-character dialogue file. Disposition: re-dispatch Phase 1.5 fork for the missing speaker; cap-burn DELETE the anchor's dialogue-anchor flag (recasting the bone as silent-action) requires explicit user authorization.
- **FAULT-DIALOGUE-CARD-VIOLATION (HARD)** — an utterance violates the speaker's behavior card §hard fences or §forbidden vocabulary, OR the file's `behavior-card:` header does not match the resolved card slug. Disposition: re-dispatch Phase 1.5 fork in revise mode.
- **FAULT-DIALOGUE-OBJECTIVE-MISSING (HARD)** — an entry's `<objective>` field is empty or does not match a speech-act the anchor bone's substance_delta licenses (e.g. utterance carries community-axis movement but objective names no community-class purpose).
- **FAULT-DIALOGUE-EARTH-BET-FENCE (HARD)** — substring scan of every utterance and objective against the Earth-Bet hard-fence list (Khepri, Brockton Bay, Skitter, etc. per the auditor class library §Earth-Bet hard-fence scan).
- **FAULT-DIALOGUE-COVERAGE (HARD)** — every speaker in the chapter's dialogue-anchor inventory has a per-character file on disk with ≥1 entry. Missing speaker file → HARD per speaker.

These checks are MECHANICAL; the auditor enumerates them at audit time. Content-quality checks (does the line *land*, does it pay the substance) remain with `/and-facets` Phase 5b audience-gate downstream.

**HARD findings block Phase 7 emission.** Re-fire Phase 1 (scene-decomposition) on the offending scenes; cycle 1 of the same `/and-write` invocation; max 2 internal HARD-resolution cycles. After 2 cycles, surface to user.

**SIGNAL findings record but pass — with disposition (URI-WRITE-SIGNAL-DISPOSITION).** Each SIGNAL must reach a disposition before Phase 7 emit: either **remediated** (re-decompose / re-shape the offending bone or scene) or **explicitly accepted** with a one-line rationale recorded in the bone-gate report. A SIGNAL with no disposition blocks emit — emission is gated on `every SIGNAL has disposition ∈ {remediated, accepted}`, not on SIGNAL count being zero. SIGNALs land in `chapters[].scenes[].bones[].gate_verdict.signals[]` with their disposition for later `/and-write revise --from-signals` targeting or `/and-review bones <chapter>` post-hoc inspection. The pre-overhaul behavior — log the SIGNAL and ship it untouched — is the failure this fixes (a fragile proxy-hold SIGNAL shipped unremediated through b01c02).

Write `gate_verdict` per bone on PASS only — HARD findings block emission, so no PASS-state is written for bones inside a failing scene.

Save full bone-gate report to `staff/auditor/write-<chapter>-bone-gate.md`.

---

## Phase 6.5 — Admin process-critic dispatch (URI-ADMIN-PROCESS-CRITIC, 2026-05-25; non-blocking)

If the Phase 6 bone-gate verdict carries any HARD finding OR any SIGNAL that reached emit with disposition `accepted` rather than `remediated`, dispatch admin in process-critic mode. Non-blocking — Phase 7 proceeds whether or not admin returns.

Dispatch:
- `subagent_type: admin`
- prompt carries:
  - `mode: process-critic`
  - `trigger.reason: failure`
  - `trigger.source_report: active-project/staff/auditor/write-<chapter>-bone-gate.md`
  - `trigger.source_verdict: <HARD-count / SIGNAL-accepted-count summary>`
  - `gate_path: .claude/commands/and-write.md#phase-6`

Admin's return (`OK | OK-MERGED | OK-PRIOR-REJECTION | OK-RE-SURFACED | PROCESS-CHANGE-PROPOSED PROP-<NNNN> | ESCALATE`) is logged in the bone-gate report tail under `## admin-process-critic` but does not gate emit. New proposals land in `staff/admin/process-proposals.md` for principal triage. See CLAUDE.md Rules §13 and `schemas/admin-proposal.schema.md`.

If verdict is fully clean (no HARDs, all SIGNALs remediated), skip the dispatch.

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

**Step 3a — dialogue citations (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25).** For each dialogue-anchor bone, append the bone's `dialogue_citations[]` from memory as a bracketed list at line end: `<flat_id> SUBJECT VERB OBJECT [<character-slug>:<id>, <character-slug>:<id>, ...]`. The citation tokens are emitted at bones-write time because dialogue ships with bones — they no longer accrue at downstream facet-author time. Non-dialogue-anchor bones carry no citations at emit (other facet citations still accrue at `/and-facets` author time, per `schemas/bones.schema.md`).

### (b) Scene-map facet

`active-project/theater/facets/scene-map-<book>-<chapter>.md` — conforms to `schemas/scene-map.schema.md`. Emitted directly from `scenes[]`:
- One scene-map entry per scene.
- Bone-range computed from the flat_ids of bones inside each scene.
- Scene boundaries, scene chunks, scene_conflict, and substance_delta carried forward.

This **replaces** `/and-facets` Phase 4d derivation; `/and-facets` Phase 4d downgrades to coverage-validation only.

### (c) Per-character dialogue files (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25)

`active-project/theater/dialogue/<character-slug>.md` per speaker in the dialogue-anchor inventory. Authored at Phase 1.5; serialized here at Phase 7 alongside bones + scene-map. Conforms to `schemas/dialogue.schema.md`. **The bones file + scene-map facet + per-character dialogue files are the atomic Phase 7 emit set** — partial emit is a HARD fault.

### Downstream-gate pre-verify (HARD, blocks write)

1. **URI-DIALOGUE-COVERAGE-GATE.** Every dialogue-anchor bone (speech-form `speaks to` OR licensed action-form with communication-class axis movement) has a speaker resolvable from the cast roster AND ≥1 utterance in `theater/dialogue/<speaker-slug>.md` AND ≥1 citation token `[<speaker-slug>:<id>]` on the bone in the bones file. For speech-form bones, listener is also cast-resolvable. Bare dialogue-anchor bone (no utterance / no citation) → HARD per bone. Missing speaker file (anchor names a speaker with no file on disk) → HARD per speaker. **This is the canonical gate location** — `/and-facets` Phase 5's dialogue-coverage gate is removed under URI-WRITE-DIALOGUE-COBONDED (dialogue is upstream now).
2. **URI-SCENE-WINDOW.** Every bone lands inside exactly one scene's flat_id range; no dangling anchors; no scene-spanning bones.

Both pre-verifications run before write. HARD-fail aborts emission with the offending bone(s) named.

### Memory updates

- Set `chapters[<slug>].bones_file = theater/bones/<book>-<chapter>.md`.
- Set `chapters[<slug>].bones_count = <N>`.
- Set `chapters[<slug>].substance_bone_gate_verdict = PASS`.
- Set `chapters[<slug>].substance_delta_measured.{axes_moved, density_measured, felt_verdict}`.
- Set `chapters[<slug>].status = bones-written` (G1 — even in revise mode, regardless of partial scope).
- Stale-mark downstream artifacts (facet outputs, draft) per `design/substance/staleness-cascade.md`.
- **Depth-pass intent flag (URI-STITCH-SIGNAL-CLUSTER MANDATORY, 2026-05-25).** If this invocation was `revise --from-signals` AND the chapter had `cold_read.verdict == PASS-WITH-DEPTH-PASS-REQUIRED`, set `chapters[<slug>].depth_pass_pending = true`. `/and-stitch` Phase 9 Step 4 reads this flag and, on PASS verdict, stamps `chapters[<slug>].depth_pass_resolved_at` to confirm delivery (intent recorded here; delivery confirmed at the next clean stitch). The resolved stamp is consumed by `/and-substance book <next-book>` Phase 0 + `/and-review verdict <book>` precondition. The prior `cold_read.verdict` is preserved as history; resolution is a separate field on the chapter.

### Emit-summary surfacing (F3 — SIGNAL discoverability)

```
/and-write <chapter>: PASS. <N> bones across <S> scenes. Bones file: theater/bones/<book>-<chapter>.md
                                                          Scene-map: theater/facets/scene-map-<book>-<chapter>.md

Bone-gate verdict: PASS (HARD: 0, SIGNAL: <K>, TASTE: 0).
```

If SIGNAL count > 0, append:

```
<K> SIGNAL findings recorded (all dispositioned: remediated | accepted) —
    see `/and-review bones <chapter>` to inspect, or
    `/and-write <chapter> revise --from-signals` to address accepted SIGNALs.
```

```
next: /and-review bones <chapter>   (MANDATORY — independent chunk→bones fidelity review;
                                     /and-facets Phase 0 HARD-aborts without it)
then: /and-facets <chapter>
```

**`/and-review bones` is a mandatory step between `/and-write` and `/and-facets`** (URI-WRITE-BONES-REVIEW-GATE). The decomposition is the highest-consequence step in the chain and the Phase 6 bone-gate is the only check on it during `/and-write` itself — a mechanical gate, no independent review. `/and-review bones <chapter>` provides that independent review and writes the `chapters[<slug>].bones_review` record; `/and-facets` Phase 0 HARD-aborts if the record is absent or stale against the bones file.

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
