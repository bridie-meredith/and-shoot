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

**F2. Facet tuning harness pass on sensory + memory (A7 + A8 from the parent plan). — DONE 2026-05-21**
- Harness pass executed (compressed Phase 0 + Phase 1 walk; cap-burn evidence served as the corpus). Both rubrics locked at V3.
- **Sensory V3** — `design/shoot-v2/rubric-sensory.md`. Two clauses added: (1) Short-chapter floor-vs-ceiling exemption — when `bone_count < 30` AND modality count equals floor, sparsity ceiling relaxes to `max(6%, 2/bone_count)`; modality-floor takes precedence over sparsity-ceiling because monoculture is the load-bearing pathology. (2) Anti-pattern #14 — Cycle-N ADD without pre-validation; fixer ADDs must satisfy the full per-entry rubric (including old-state lineage) before committing, since same-cycle audit has no remediation budget.
- **Memory V3** — `design/shoot-v2/rubric-memory-flags.md`. Feel-as-spine equivalence carve-out added on the Licensing-discipline axis (and propagated to the REJECT signature, cross-axis test, anti-pattern #7, and ceiling-defense protocol for consistency). When chapter `dramatic_shape: hinge` AND scene's `stakes_axis` is in `axes_held[]` AND a feel-flag fires on the same anchor AND all other discipline gates clear, memory-flag entries may co-cite the feel-flag as spine in place of narrator-interest. The carve-out is structurally compatible with the 2026-05-21 axis-bookkeeping split — held-discipline scenes are exactly the `axes_held[]` scenes the new schema makes mechanically checkable.
- Summary doc + re-audit walk at `design/shoot-v2/sensory-memory-v3-tuning-summary.md`. The `mem:1 @9` cap-burn is V3-resolvable retroactively (all four carve-out conditions hold for b01c01); the `sensory:3 @17` cap-burn still needs a chapter-level loc-state repair (V3 provides the rule that would have caught the issue at pre-add time, not a content fix).
- **No command body or auditor AP-SCAN edits needed** — per CLAUDE.md rule 11, the auditor's RUBRIC-FIDELITY class enumerates REJECT / anti-pattern / cross-facet sections at audit time, so the V3 rubric edits auto-promote to mechanical checks next cycle.
- Open: cycle-N ADD pre-validation enforcement at orchestration time (F1 / A3) is still owed at the command-body layer; rubric anti-pattern #14 flags the pattern at audit time but doesn't prevent it at fixer time.

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

**F5. Inspect b01c02-c17 chunk-level `substance_delta` blocks** for any remaining `direction: ~` / `direction: null` entries. **DONE 2026-05-21** — grep confirmed memory.md is clean; only Corvan-coda b01c18 has empty `axes_in_motion: []` (correct, frame-coda).

---

## Pre-flight checklist for `/and-substance chapter b01c02` (refreshed)

```
[x] F1  /and-substance + /and-write command bodies synced with new schema (axes_held + direction:up|down) (done 2026-05-21)
[x] F2  sensory + memory rubrics tuned to V3 via facet-tuning-process harness (done 2026-05-21)
[x] F5  b01c02-c17 chunk-level substance_delta rescan (done 2026-05-21 — clean)
[x] A1  anchor-refresh HARD-ABORT at /and-facets Phase 0 (done 2026-05-21)
[x] A2  cap-burn semantics codified (canonical = DELETE; done 2026-05-21)
[x] A3  cycle-N fixer ADD pre-validation (rubric anti-pattern #14 + orchestration Phase 5b; done 2026-05-21)
[x] A4  pipeline-adaptation audit re-run (done 2026-05-21 — 5 HARD + 6 SIGNAL + 3 TASTE-FLAG; all HARDs + 4 actionable SIGNALs resolved same-session)
[x] A5  cite-index builder deletion-aware (done 2026-05-21 — canonical `# DELETED <prefix>:<id>` marker recognized; auto-strip on render; deletion-aware stale-citation check)
[x] A6  R2 stale-shard verification at /and-facets Phase 3 (done 2026-05-21 — cite_index_hash freshness check)
[x] A9  bone-gate audience covers ALL scenes (done 2026-05-21 — per-scene coverage gate at /and-write Phase 6)
[x] A10 /and-review pipeline subcommand (done 2026-05-21 — schema↔command-body↔rubric tri-walk promoted from reactive-fork to routine subcommand)
[x] A11 prune persist-time intermediates (done 2026-05-21 — `_drafts/` archive subdir; signature/actor-baselines/b<NN>/b<NN>c<MM> drafts pruned at Phase 6)
[x] A12 world-notes.md Lucerys/Nessa cleanup (done 2026-05-21)
[x] A14 inline `# rubric-carve-out` schema support (done 2026-05-21 — facet.schema.md "Rubric carve-out preamble" section + parser contract + per-entry annotation rules)
```

All BLOCKING + HIGH + MEDIUM items now done. F4 (per-chapter actor_baselines promotion) is async per-chapter work. A13 (formal `/and-review verdict b01`) requires c02+ to exist. A15 (per-bone direction=null mechanical check) is done via F1. A16 (project-scoped stitch-profile tuning) is not blocking; revisit when polish is undeferred.

---

## Files touched this session

- `schemas/showrunner-memory.schema.md` — added `state_axes[].notes`, `actor_baselines[]` block, `axes_in_motion[]` explicit shape at all chunk levels, `axes_held[]` at all levels including bone, standardized `direction: up|down`, added field-notes paragraphs, added `chapter_class: standard | frame-coda` field.
- `schemas/facet.schema.md` — new "Rubric carve-out preamble" section (A14); parser contract for `# rubric-carve-out` / `# pragma carve-out` headers + per-entry annotation rules.
- `schemas/audit-report.schema.md` — `cite_index_hash` field added to R2 decision shard frontmatter (A6); `/and-season` reference replaced with current consumers.
- `design/substance/delta-targets.md` — `axis_moves` direction enum updated to `up|down`; new "three bone shapes" section (held / chatter / malformed).
- `active-project/staff/showrunner/memory.md` — converted all chunk-level + bone-level null/zero entries; added `series.substance.actor_baselines[]` (dense 8×9=72-cell matrix); cleaned `substance_delta_measured.axes_moved` for b01c01.
- `active-project/staff/cite-index/build_cite_index.py` — A5 deletion-aware: `DELETION_RE` regex, `parse_deletions()` + `collect_deletions()` functions, auto-strip stale tokens on canonical render, deletion-aware `stale_citation_check`.
- `active-project/staff/showrunner/world-notes.md` — A12 Lucerys/Nessa cleanup.
- `active-project/staff/showrunner/staleness-log.md` — cascade event appended.
- `active-project/staff/reviews/run-postmortem-harness-2026-05-20.md` (read-only context).
- `active-project/staff/auditor/pipeline-adaptation-audit-2026-05-21.md` — A4 audit report + resolution trace.
- `design/shoot-v2/rubric-sensory.md` — V3 lock; short-chapter floor-vs-ceiling exemption; anti-pattern #14; STRUCT-007 "Schema rename" notice cleaned.
- `design/shoot-v2/rubric-memory-flags.md` — V3 lock; feel-as-spine equivalence carve-out propagated through ACCEPT, REJECT, cross-axis test, anti-pattern #7, ceiling defense.
- `design/shoot-v2/sensory-memory-v3-tuning-summary.md` — V3 harness pass record + re-audit walk.
- `.claude/commands/and-substance.md` — F1 schema sync (Phase 3 axes_in_motion + axes_held); F1 Phase 4 Step 4d post-cast actor_baselines pass; Phase 0 book-level HARD-ABORT for sparse actor_baselines; A11 persist-time draft pruning at Phase 6; STRUCT-004 stakes_axis comment fix; STRUCT-003 chapter_class chapter-level authoring.
- `.claude/commands/and-write.md` — F1 Phase 1 three bone shapes; F1 Phase 2 FAULT-BONE-DELTA-MALFORMED extension; F1 Phase 6 bone-gate split per shape + chapter_class:frame-coda exemption; A9 per-scene audience coverage gate.
- `.claude/commands/and-facets.md` — A1 Phase 0 step 4a anchor-refresh HARD-ABORT; A6 Phase 3 R2 stale-shard pre-check; A3 Phase 5b cycle-N ADD pre-validation; A2 Phase 5b cap-burn DELETE semantics + canonical deletion marker shape; STRUCT-008/009/011 residue fixes; CURVE-SHAPE denouement → falling.
- `.claude/commands/and-stitch.md` — STRUCT-001/002 tensometer residue purge (dispatch payload, rhythm guidance section renamed, COLLAPSE-TENS1-RUN → COLLAPSE-FLAT-LOW-RUN, scene-window flow ASCII).
- `.claude/commands/and-review.md` — A10 new `pipeline` subcommand (schema↔command-body↔rubric tri-walk) + discovery-table entry.
- `CLAUDE.md` — STRUCT-005 `theater/proto-lines/` directory documented; pipeline subcommand mention in command table.
