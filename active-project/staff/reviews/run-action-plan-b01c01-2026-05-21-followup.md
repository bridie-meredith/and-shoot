# Follow-on action plan — picking up from the 2026-05-21 axis-bookkeeping work

**Date:** 2026-05-21
**Status:** Items 1 and 2 of the four-item next-step list from `run-action-plan-b01c01-2026-05-20.md` are done. This note captures the remaining work, scoped for the next session.

---

## What landed in this session (2026-05-21)

1. **Schema-tightened the axis bookkeeping.** `schemas/showrunner-memory.schema.md` updated:
   - At every chunk level (book / chapter / scene) `axes_in_motion[]` is now explicit: `{axis, direction: up|down, target_delta_magnitude: positive number > 0, cost_ledger_anchor, notes}`. `direction: null` and `magnitude: 0` are rejected.
   - At every chunk level, new sibling block `axes_held[]: {axis, rationale}` records axes deliberately held flat by discipline.
   - At bone level, `axis_moves[]` standardized to `direction: up|down` (was `+|-`), `magnitude > 0`. Sibling `axes_held[]` added. Chatter bones use `axis_moves: []` (empty list) + no `axes_held`.
   - `scene_conflict.stakes_axis` may resolve to either `axes_in_motion[]` or `axes_held[]`; `/and-write` Phase 6 bone-gate validates against the union.
   - `design/substance/delta-targets.md` updated with the three-bone-shape table (held / chatter / malformed).

2. **Pinned per-actor positions on every signature axis (dense 8 × 9 = 72-cell matrix).** `series.substance.actor_baselines[]` block added to `active-project/staff/showrunner/memory.md`. Each cell carries an explicit `applicability` field: `moves` (start_rank ≠ end_rank), `static` (start_rank = end_rank — examined and pinned, not skipped), or `not-applicable` (deliberate exclusion with rationale). Absent entries are schema violations under the new shape — no judgment-by-omission. Final distribution:
   - **taylor-hebert-kl-122ac:** 9 moves (lifted-from-state-axes; protagonist-perspective verbatim).
   - **otto-hightower:** 9 moves (lifted-from-state-axes; Otto IS the antagonist-perspective archetype).
   - **aemond-targaryen-122ac:** 4 static + 5 not-applicable (walk-on; appearances DEPLOY pre-existing capability at structural crisis points).
   - **wren-stitch-maker-flea-bottom-ward:** 2 moves + 3 static + 4 not-applicable (cost-bearer arc on social-tether + relational-anchor-status).
   - **sera-hightower-kl-122ac:** 4 static + 5 not-applicable (protect-target; positions preserved by architecture).
   - **gylda-saltwater-flea-bottom:** 1 moves + 3 static + 5 not-applicable (witness-mirror; knowledge spike at d09-d10 only).
   - **coll-net-mender-flea-bottom:** 4 static + 5 not-applicable (Flea Bottom social-physics baseline; non-interpretive substrate).
   - **corvan-archmaester-retrospective-coda:** 2 static + 7 not-applicable (frame-coda voice c.160 AC; in-book Δ exempt).

   Total: 21 moves + 20 static + 31 not-applicable = 72 cells.

3. **Active-project memory converted.** All `direction: null` and `direction: ~` and `magnitude: 0` entries in `active-project/staff/showrunner/memory.md` rewritten under the new split:
   - Chunk-level: book b01 position-axis split into rise + fall phase entries; chapter b01c01 + scenes s01/s02/s03 capability-null entries moved to `axes_held`; chapter b01c18 (Corvan coda) moved to `axes_held` with `chapter_class: frame-coda` (exempt from bone-gate).
   - Bone-level: 11 capability-null bones moved to `axes_held` (held-by-discipline pattern); 4 knowledge-null bones moved to `axis_moves: []` (chatter pattern); 1 redundant knowledge-null entry on b01c01s02n08 dropped (capability hold carries that bone alone).
   - `substance_delta_measured.axes_moved` cleaned: was `{capability: 0, knowledge: 0.53}`; now `{knowledge: 0.53}` + `axes_held_verified: [capability]`.

---

## What's still owed before `/and-substance chapter b01c02`

### IMMEDIATE — must land before c02 authoring

**F1. Sync `/and-substance` Phase 3 template + `/and-write` Phase 6 bone-gate with the new schema.** [P0 · S effort]
- `.claude/commands/and-substance.md` Phase 3 currently shows `axes_in_motion: [<axis-slug>, <axis-slug>, ...]` (the pre-split simplified form). Update to the explicit `{axis, direction, target_delta_magnitude, cost_ledger_anchor, notes}` object shape plus a sibling `axes_held: [{axis, rationale}]` block.
- `.claude/commands/and-write.md` Phase 6 substance bone-gate (`SUBSTANCE-FLAT-<axis>` / `SUBSTANCE-SUSPECT-cheap-gain-<axis>` / `AXIS-DELTA-MISMATCH` / `FAULT-BONE-DELTA-MALFORMED` rules) must:
  - Accept `axes_held[]` as a valid place to satisfy `scene_conflict.stakes_axis`.
  - Reject `axis_moves[]` entries with `direction: null` or `magnitude: 0` as `FAULT-BONE-DELTA-MALFORMED` HARD.
  - Validate that the chunk's `axes_in_motion[]` + `axes_held[]` together cover the parent contract's union.
  - Treat `chapter_class: frame-coda` as a bone-gate exemption (b01c18 Corvan coda).

**F2. Facet tuning harness pass on sensory + memory (A7 + A8 from the parent plan).** [P0 · M effort]
- The harness lives at `design/shoot-v2/facet-tuning-process.md` (five-phase replicable pattern). Locked V2 rubrics at `design/shoot-v2/rubric-sensory.md` and `design/shoot-v2/rubric-memory-flags.md`. Worked examples: `sensory-tuning-final.md`, `memory-tuning-r2-final.md`.
- **Sensory (A8 — sparsity-vs-modality arithmetic collision):** Run Phase 1 reviewer-tune against b01c01's authored sensory corpus. Defend-or-update the modality-floor clause to scale with `dramatic_shape` (hinge chapters get exemption) OR raise the sparsity ceiling for chapters under 30 bones OR drop modality-floor when chapter substance is single-axis. Lock as V3.
- **Memory (A7 — feel-as-spine equivalence):** Run Phase 1 reviewer-tune against `mem:1 @9` and the three remediation paths that blocked uniformly. Add a "feel-as-spine equivalence clause" — memory entries may co-cite `feel:N` instead of `narrator:N` when the chapter's substance lives in feeling, not memory. Lift the held axes (axes_held) as a permitted co-citation surface (memory of a held-discipline moment is anchored to the held axis, not to a movement). Lock as V3.
- Update auditor's `RUBRIC-FIDELITY` AP-SCAN entries to enforce the V3 rules mechanically in cycle 1.

**F3. The remaining BLOCKING items from `run-action-plan-b01c01-2026-05-20.md`.** [P0]
The parent plan's pre-flight checklist had eight items. Two are now done. The remaining six:
- **A1** — anchor-refresh HARD-ABORT at `/and-facets` Phase 0 (bones newer than facets → halt, not warn).
- **A2** — codify cap-burn semantics (NOT-SUCCESSFUL coexists with `stitched: true`; pick the canonical resolution).
- **A3** — ban cycle-N fixer ADD operations (or audience-validate them in-cycle).
- **A4** — pipeline-adaptation audit re-run.
- **A9** — bone-gate audience covers ALL scenes (s03 was skipped at b01c01).
- **A12** — world-notes.md Lucerys/Nessa references cleanup.

### NEAR-TERM — should land within next 2-3 chapters

**F4. Validate the 72-cell actor_baselines matrix as chapters resolve cells.** [P1 · S effort per chapter]
- The dense matrix is seeded; the work going forward is **promotion** of cells, not adding new ones. At `/and-substance chapter` Phase 3 for each subsequent chapter, screen-writer should:
  - Re-examine `static` cells touched by the chapter's scenes — confirm the position is still flat, or promote to `moves` if the chapter actually arcs it.
  - Re-examine `not-applicable` cells if the chapter brings that actor into a previously-untouched axis — promote to `moves` or `static` with `source: scene-pinned-<chapter-slug>`.
  - Update `source` to `scene-pinned-<chapter-slug>` on any cell the chapter newly resolves.
- Specific high-likelihood promotions to watch for across c02-c17:
  - Wren `social-tether` is already `moves 5→1` — confirm d04 (load-bearing) + d10 (exposed) waypoints when those chapters author.
  - Aemond's currently `not-applicable` cells on knowledge, agency may need promotion if a walk-on chapter actually shifts those — the role-card commits "each appearance must shift a named plot axis," so each walk-on should produce at least one promotion.
  - Gylda's currently `not-applicable` political-register-toward-elite may promote at d09-d10 if the naming-the-pattern moment positions her against the elite layer.
  - Corvan b01c18 INTERLUDE chapter is `chapter_class: frame-coda` and exempt from bone-gate — his cells should stay `static` or `not-applicable` (no promotions expected).

**F5. Inspect b01c02-c17 chunk-level `substance_delta` blocks** for any remaining `direction: ~` / `direction: null` entries. [P1 · XS effort]
- A grep over the full memory file found none post-conversion, but the b01-level chunks (lines ~800–1530) weren't all individually rewritten — only the rise-and-fall position-axis entry was touched. Run a clean re-scan after `/and-substance book b01` re-fires (or as a one-shot check) and convert any remaining cases.

---

## Pre-flight checklist for `/and-substance chapter b01c02` (refreshed)

```
[ ] F1  /and-substance + /and-write command bodies synced with new schema (axes_held + direction:up|down)
[ ] F2  sensory + memory rubrics tuned to V3 via facet-tuning-process harness
[ ] A1  anchor-refresh HARD-ABORT at /and-facets Phase 0
[ ] A2  cap-burn semantics codified
[ ] A3  cycle-N fixer ADD policy decided
[ ] A4  pipeline-adaptation audit re-run
[ ] A9  bone-gate audience covers ALL scenes
[ ] A12 world-notes.md Lucerys/Nessa cleanup
```

F4 and F5 are async — they can land across c02-c04 as the per-chapter scene-pinning naturally generates them.

---

## Files touched this session

- `schemas/showrunner-memory.schema.md` — added `state_axes[].notes`, `actor_baselines[]` block, `axes_in_motion[]` explicit shape at all chunk levels, `axes_held[]` at all levels including bone, standardized `direction: up|down`, added field-notes paragraphs.
- `design/substance/delta-targets.md` — `axis_moves` direction enum updated to `up|down`; new "three bone shapes" section (held / chatter / malformed).
- `active-project/staff/showrunner/memory.md` — converted all chunk-level + bone-level null/zero entries; added `series.substance.actor_baselines[]` (dense 8×9=72-cell matrix; every actor × every axis with explicit applicability marker); cleaned `substance_delta_measured.axes_moved` for b01c01.

No command bodies were edited in this session — F1 captures that work.
