# Bones-vs-/and-facets Compatibility Gaps

**Source:** Cross-check of the revised plan's new bones schema (`scenes[].bones[]` with per-bone state-delta) against what `/and-facets` and `/and-stitch` actually consume from the bones file.
**Status:** Open. Must resolve before plan execution — the plan says `/and-facets` and `/and-stitch` are "unchanged" except for tensometer-drop, but the new bones structure as written would break both.
**Date:** 2026-05-17.

The plan asserts the downstream chain (`/and-facets`, `/and-stitch`) is preserved. That promise only holds if the **flattened per-chapter bones file** preserves the existing `schemas/proto-line.schema.md` shape exactly. The current plan does not say so, and several details point the other way. Below: the gaps, with recommended resolution.

---

## GAP 1 — Bone ID format

**What consumers expect:** Flat positive integers (`1`, `2`, `3`, …), file-scoped, monotonic, stable. Citations look like `[feeling:42]`, `[taylor-hebert:7]`. Scene-map uses `@<start>-@<end>` integer ranges. `proto-line.schema.md § <id>`.

**What the plan currently shows:** Scoped slugs (`b01c01s01n01`) in the in-memory `scenes[].bones[]`. The plan does not say whether the flattened file uses the slug or an integer.

**Break:** If the flattened file uses slug IDs, every facet author's citation accrual breaks, scene-map ranges break, stitcher bone-walking breaks.

**Resolution:** The flattened file uses **flat integer IDs**, assigned by `/and-write` Phase 7 at serialization time in scene-order across the chapter. The in-memory `scenes[].bones[]` keeps both: the slug (`b01c01s01n01`) for authoring/audit cross-reference, and a derived `flat_id: <int>` for serialization. The serialization is deterministic — re-running `/and-write redo` produces the same flat IDs as long as the scene/bone count is stable.

---

## GAP 2 — Header fields not populated by `/and-write` Phase 7

**What `/and-facets` Phase 0 expects** (per `and-facets.md` line 79): seven fields, in order — `episode`, `narrator`, `goal`, `cast`, `locations`, `prior_episode`, `aggregate_range`.

**What the plan currently shows:** Nothing. `/and-write` Phase 7 just says "Write bones to `theater/bones/<book>-<chapter>.md` (flattened scene-ordered view)."

**Break:** `/and-facets` Phase 0 aborts on missing header.

**Resolution:** `/and-write` Phase 7 emits the full 7-field header, sourced as follows:
- **`episode:`** — the chapter slug (e.g. `b01c01`). The field name stays `episode:` for `/and-facets` compatibility, but value is the chapter slug. Or rename to `chapter:` and update `/and-facets` Phase 0 to accept either — pick one and commit.
- **`narrator:`** — chapter's POV character. **This requires a new field on `chapters[]` in memory** (`chapters[].pov_narrator: <actor-slug>`), authored by `/and-substance chapter` Phase 2 when the chapter chunk is produced. The plan currently has `series.structure.pov` (single | multi | rotating-per-book) but no chapter-level narrator picker. Add it.
- **`goal:`** — chapter substance contract distilled into one line ("what this chapter shows the audience"). Drawn from `chapters[].dramatic_shape` + chapter-arc completion line (already in the plan's `/and-substance chapter` Phase 4). `/and-write` derives or `/and-substance chapter` writes it explicitly to `chapters[].goal: |`.
- **`cast:`** — grepped from the chapter's bones SUBJECTs + `speaks to` listeners (same algorithm as today).
- **`locations:`** — grepped from bones OBJECTs against warehouse loc cards (same as today).
- **`prior_episode:`** — slug of the previous chapter in chapter order (`b01c01` ⇒ `none`; `b01c02` ⇒ `b01c01`; `b02c01` ⇒ last chapter of b01). Field name stays `prior_episode:` for compatibility; rename later if vocabulary refactor lands.
- **`aggregate_range:`** — `1-<N>` where N is the chapter's bone count. Trivially `1-N` since `/and-write` authors the chapter directly (no season-aggregate-then-split flow); the field is kept for `/and-facets` schema compatibility.

---

## GAP 3 — Scene-map authoring loses its tensometer source

**What `/and-facets` Phase 4d currently does:** Derives the scene-map facet (`theater/facets/scene-map-<slug>.md`) by walking the tensometer's scene-footer + interest-narrator's sparsity gradient + loc-state transitions + time-skip blanks. Tensometer's `peak-bones` (bones with tens ≥ 2) anchors the scene-boundary picks. `/and-stitch` has a tensometer-derivation fallback when the scene-map facet is absent.

**What the plan removes:** Tensometer. Across the board.

**Break:** Scene-map derivation has no tensometer scene-footer to read. `/and-stitch`'s fallback path silently breaks.

**Resolution:** `/and-write` Phase 7 **emits the scene-map facet directly** from the in-memory `chapters[].scenes[]` structure — the scene boundaries are already known (one scene per `scenes[]` element, with bone-ranges computed from the bone serialization). `/and-facets`'s scene-map "derivation" pass becomes a **validation pass only** (URI-SCENE-WINDOW coverage check still fires; no derivation needed). Update:
- `/and-write` Phase 7 spec: add "emit `theater/facets/scene-map-<chapter>.md` from the in-memory `scenes[]` structure" alongside the flattened bones file.
- `/and-facets` Phase 4d: drop the derivation logic; keep the coverage-validation logic. (Light edit to `/and-facets`, on top of the tensometer-drop edit already planned.)
- `/and-stitch` Phase 0: the tensometer-derivation fallback is now dead code. Either remove it or leave it with a comment that it's a no-op under the new chain. Pick removal — keeps the command body cleaner.

**Implication for the "and-stitch unchanged" promise:** `/and-stitch` IS touched, narrowly. Drop the tensometer-derivation fallback path. Update the plan's "Out of scope" line about `/and-stitch` to say "unchanged structurally, except for dead-code removal of the tensometer-derivation fallback in Phase 0."

---

## GAP 4 — Scene-boundary markers in the flattened file

**What `proto-line.schema.md § body format` says:** "No section headers, no scene markers, no markdown bullets."

**What the plan currently says:** "bones in scene order, with scene-boundary markers preserved" (in the schema note after the YAML block).

**Break:** Direct contradiction. If markers are inserted, the existing 5-pass review (constraint/shape/trim/continuity) sees unfamiliar tokens and faults. If markers are omitted, the plan's note is misleading.

**Resolution:** No scene markers in the flattened file body. Scene boundaries are conveyed by **the scene-map facet emitted alongside** (per Gap 3 resolution). The flattened file stays comment-clean per the schema. Update the plan's note to: "bones in scene order; scene boundaries conveyed via the co-emitted scene-map facet, not via in-file markers."

The existing **blank-numbered-ID time-skip marker** convention is preserved: `/and-write` may emit `<id>` lines with no body where the in-memory scene transitions or a within-scene time-skip is declared. These are handled by `/and-stitch` Phase 1 (paragraph/chapter break).

---

## GAP 5 — Per-bone state-delta has no home in the flattened file

**What the plan adds:** `bones[].substance_delta.{axis_moves, cost, cost_ledger_anchor}` per bone in memory.

**What the proto-line schema allows in the file:** Only the SVO line + optional `[<artifact>:<id>]` citations. No YAML metadata; comment-clean (POV markers excepted).

**Break:** If state-delta is dumped into the file as comments, the existing constraint audit faults the lines. If it's omitted from the file, `/and-facets` and `/and-stitch` can't read it — but the plan says the substance contract is what the audience and auditor reason against during review, including at `/and-write` Phase 6 bone-gate (which fires BEFORE Phase 7 emission, so it has memory access — fine) and at `/and-review bone <slug>` (post-hoc — also memory access, fine).

**Resolution:** Per-bone state-delta lives **only in memory** (`chapters[].scenes[].bones[]`). The flattened file is pure SVO + citations, matching the current schema. Reviewers and auditors that need the delta read it from memory by bone-slug; the flat_id ↔ slug map is the bridge. The plan should explicitly say: "the per-bone substance_delta is not written to the flattened bones file; reviewers consult it from showrunner memory."

**Implication for `/and-review bone <slug>`:** The subcommand reads memory, not the file. Already implied by "bone slug (b01c01s01n01)" target; restate explicitly.

---

## GAP 6 — Speech-bone shape

**What the plan currently shows:** SVO example "Maya confronts Tomas about the missing key" — not a speech-form bone.

**What URI-DIALOGUE-COVERAGE-GATE requires** (per `proto-line.schema.md` and `/and-facets`/`/and-stitch`): Speech bones use the exact form `<speaker-slug> speaks to <listener-slug>`. The `speaks to <listener>` shape is the licensed exception to the "no preposition" rule. Dialogue files cite back by `<character-slug>:<id>`.

**Break:** If the new chain authors speech bones in some other shape (e.g. `<speaker> says <utterance>` or `<speaker> tells <listener>`), URI-DIALOGUE-COVERAGE-GATE breaks at `/and-facets` Phase 0 and `/and-stitch` Phase 0.5.

**Resolution:** `/and-write` Phase 3 (SVO craft) must preserve the licensed forms — `<X> speaks to <Y>` for dialogue, `<X> turns to <Y>` banned (already), perception verbs banned (already). Add to `/and-write` Phase 3 spec: "SVO craft is governed by `schemas/proto-line.schema.md § field rules`; the dialogue-shape (`<speaker-slug> speaks to <listener-slug>`) is mandatory for any bone whose declared axis-movement is communication-mediated. Substance_delta tags on speech bones must declare communication-axis movements (community, knowledge, reputation), not physical-action axes."

This also gives the substance-contract a useful constraint: a speech bone's per-bone delta must be on a communication-class axis. Naturally couples substance-grain with bone-shape.

---

## GAP 7 — `facet_tags` field on bones — purpose unclear

**What the plan currently shows:** `bones[].facet_tags: [feeling, dialogue, memory-flag, ...]` annotated "optional pre-tagging for /and-facets."

**What `/and-facets` actually does:** Each R1 facet author scans the base bones file (no `facet_tags` access — the schema doesn't have such a field) and decides which bones to author facet entries against, citing back via `[<prefix>:<id>]` tokens that accrue post-hoc. `facet_tags` as a forward-pointer would invert this accrual direction.

**Break:** If `facet_tags` is treated as a forward-anchor (telling `/and-facets` which facets to write for this bone), it contaminates R1 facet-authoring training data — the exact failure mode `proto-line.schema.md § <cited-id>` Section calls out: "Pre-seeding citation anchors at extraction time contaminates downstream facet-authoring training data and is not allowed."

**Resolution:** Drop `facet_tags` from the bones schema, OR repurpose as a **post-hoc audit hint** populated by `/and-facets` Phase 4 (citation union) — i.e. it's the in-memory mirror of the file's citation list, populated after `/and-facets` runs, not before. Pick drop — cleanest.

The substance-contract carries enough information (axis class) to let `/and-facets` reason about likely facet routing without explicit pre-tags; the per-bone state-delta on a community-axis bone implies dialogue, on an emotional-axis bone implies feeling, etc. That's emergent routing, not pre-tag routing.

---

## GAP 8 — `gate_verdict` field — when and by whom

**What the plan currently shows:** `bones[].gate_verdict.{bonefide, flat}` "filled by /and-write Phase 6."

**No break here**, but two questions:
- Phase 6 runs BEFORE Phase 7 emission. If `gate_verdict.bonefide: false` or `gate_verdict.flat: <axis>` (HARD), Phase 6 blocks emission entirely — so why persist a HARD verdict to memory at all? The bone shouldn't ship.
- On `/and-write revise`, the prior `gate_verdict` is now stale.

**Resolution:** `gate_verdict` is only persisted when the bone PASSES Phase 6 (`bonefide: true`, `flat: false`). On revise/redo, prior verdicts are cleared at Phase 0 and re-filled at Phase 6. State the lifecycle in the plan.

---

## GAP 9 — `/and-substance chapter` needs to author chapter-level fields the bones file header requires

Surfaces only because of Gap 2's resolution. New fields on `chapters[]`:
- `pov_narrator: <actor-slug>` — used for the bones file `narrator:` header. Authored by `/and-substance chapter` Phase 2 when scene chunks are produced (or `/and-substance book` Phase 4 if narrator is fixed across a book's chapters — depends on `series.structure.pov` value: `single` → fixed at book or series level; `rotating-per-book` → fixed at book level; `multi` → chapter-level pick required).
- `goal: |` — one-line "what this chapter shows the audience"; authored by `/and-substance chapter` Phase 4 alongside the dramatic-arc completion line. May be the same field.

Add both to the schema YAML under `chapters[]`. Add to `/and-substance chapter` Phase 2 / Phase 4 spec.

---

## Summary of changes to land

In the plan:
1. Bones file uses **flat integer IDs**, derived at `/and-write` Phase 7 serialization. The in-memory bone slug is the authoring/audit handle; the flat ID is the file/citation handle.
2. `/and-write` Phase 7 emits the **full 7-field header** (`episode` / `narrator` / `goal` / `cast` / `locations` / `prior_episode` / `aggregate_range`); the existing field names stay for compatibility.
3. `/and-write` Phase 7 **also emits the scene-map facet directly** from `scenes[]` structure. `/and-facets` scene-map derivation pass downgrades to validation-only.
4. The flattened bones file is **comment-clean per the existing proto-line schema** — no scene markers in body, no YAML metadata, no facet pre-tags. Per-bone state-delta lives only in memory.
5. **Speech bones preserve the `<speaker-slug> speaks to <listener-slug>` form**; substance_delta on speech bones must be on communication-class axes.
6. Drop `bones[].facet_tags` from the schema.
7. `bones[].gate_verdict` persisted only on PASS; lifecycle stated.
8. Add `chapters[].pov_narrator` and `chapters[].goal` to the schema and to `/and-substance chapter` authoring phases.
9. `/and-stitch` Phase 0 has the tensometer-derivation fallback removed (small carve-out from "and-stitch unchanged" promise).

In `/and-facets`:
- Existing tensometer-drop already planned.
- Scene-map Phase 4d: derivation → validation. Light additional edit.

In `/and-stitch`:
- Tensometer-derivation fallback removed (dead code under the new chain). Light additional edit. Plan's "unchanged" line needs a carve-out.

If these land, the new bones schema is consistent with the existing downstream chain. If they don't, the plan's "shoot-v2 chain unchanged" promise breaks at the first `/and-facets` run.
