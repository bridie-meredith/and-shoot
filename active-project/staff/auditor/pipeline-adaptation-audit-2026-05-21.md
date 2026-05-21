# Pipeline-adaptation audit — 2026-05-21

**Auditor:** fork dispatched 2026-05-21 post the F1/A1/A2/A3/A9/A12 + V3-rubric session.
**Scope:** Tri-walk: schema-vs-command-body, schema-vs-rubrics, command-body-vs-rubrics. Plus tensometer/URI-026 residue scan and CLAUDE.md review.
**Trigger:** S-12 in `run-postmortem-harness-2026-05-20.md` — schema-audit was never run as a gate, only as reactive forks. Re-run before `/and-substance chapter b01c02` to flush remnants from the substance-overhaul + the 2026-05-21 schema split + V3 rubric lock + command-body sync.

---

## Findings

### HARD findings

**STRUCT-001 — `/and-stitch` Phase 0-1 dispatch payload tensometer residue.** File `.claude/commands/and-stitch.md` lines 380 / 385 / 392. Fork input payload table listed `"tens"` as a facet citation type, included a `"Tensometer slice for the scene"` row, and the procedure said `"Load inputs. Bones, facets, ..., tensometer slice."` These are load-bearing dispatch instructions, not historical commentary. Tensometer was dropped 2026-05-17.

**STRUCT-002 — `/and-stitch` Rhythm guidance section tens= scalar vocabulary.** File `.claude/commands/and-stitch.md` lines 406 / 411 / 413 / 416. Rhythm guidance table used `tens=1` / `tens=2` / `tens=3` scalar notation as primary labels in operationally instructional prose. The scene-map vocabulary (`rhythm-shape`, `peak-bones`, etc.) should replace.

**STRUCT-003 — `chapter_class: frame-coda` referenced but not in schema.** File `.claude/commands/and-write.md` Phase 6 frame-coda exemption + `schemas/showrunner-memory.schema.md` chapter substance_delta block. The field is load-bearing (gates the entire bone-gate skip) but had no schema definition.

**STRUCT-004 — `/and-substance` Phase 3 stakes_axis comment contradicts schema.** File `.claude/commands/and-substance.md` line 109. Said `stakes_axis` "must appear in this scene's substance_delta.axes_in_motion" but the schema (post 2026-05-21 split) says `stakes_axis` may resolve to either `axes_in_motion[]` OR `axes_held[]`. Live blocker for any held-discipline scene.

**STRUCT-005 — `theater/proto-lines/` path used but not documented.** File `.claude/commands/and-facets.md` Phase 2 / 4c / 5 reference `theater/proto-lines/<slug>.md` as canonical audit read-source, but the path was absent from CLAUDE.md's directory map.

### SIGNAL findings

**STRUCT-006 — `/and-season` in audit-report schema.** File `schemas/audit-report.schema.md` line 98. Pre-overhaul command name referenced as consumer of F-R2 counts.

**STRUCT-007 — "Schema rename (pending)" stale notice.** File `design/shoot-v2/rubric-sensory.md` line 337. The rename was completed in `schemas/facet.schema.md` line 80 (2026-05-07) but the rubric's pending notice persisted through V2 → V3 lock.

**STRUCT-008 — `tens-discipline holds` in metaphor judge KEEP criteria.** File `.claude/commands/and-facets.md` Phase 3 R2.4 line 207. Legacy vocabulary in metaphor R2 judge dispatch.

**STRUCT-009 — `tens: citations preserved` instruction in R1 loc-state dispatch.** File `.claude/commands/and-facets.md` Phase 1 line 131. Dead-code instruction; new-chain bones files carry no `tens:` citations.

**STRUCT-010 — `and-write.md` line 397 Notes section correctly documents tens removal.** Confirmation; no action required.

**STRUCT-011 — `dramatic_shape: denouement` not in schema enum.** File `.claude/commands/and-facets.md` Phase 5 CURVE-SHAPE class description line 297. Schema enum is `rising | climax | falling | hinge`; `denouement` is not a value.

### TASTE-FLAGs (intentional; no action)

**TASTE-FLAG-001** — `URI-026` provenance tag in audit-report schema (historical lineage).
**TASTE-FLAG-002** — calibration anchors in rubric-sensory.md with parenthetical `tens=N` cross-references (intentional bridge documentation).
**TASTE-FLAG-003** — V3 changes summary in rubric-memory-flags.md with cap-burn provenance (intentional audit trail).

---

## Resolution trace (2026-05-21, same-session fixes)

All 5 HARD findings and 4 actionable SIGNALs landed in the same session. Commits chained from the audit dispatch.

| ID | Class | Resolution |
|---|---|---|
| STRUCT-001 | HARD | `.claude/commands/and-stitch.md` lines 30, 274, 380, 385, 392 — `tens` citation listing dropped from lens-loader, fork payload, and procedure load-list. `"Tensometer slice for the scene"` table row removed entirely. |
| STRUCT-002 | HARD | `.claude/commands/and-stitch.md` lines 404, 410-413, 415, 428, 432, 474, 496 — `tens=1/2/3` scalar labels replaced with `flat-low-zone bones` / `peak-bones-class bones` / `mid-magnitude bones` (with reference to per-bone `axis_moves[].magnitude`). Section heading renamed from "Tens-aware rhythm guidance" to "Rhythm-shape guidance." `COLLAPSE-TENS1-RUN` renamed to `COLLAPSE-FLAT-LOW-RUN`. |
| STRUCT-003 | HARD | `schemas/showrunner-memory.schema.md` — `chapter_class: standard | frame-coda` added to `chapters[].substance_delta` block with default note. `.claude/commands/and-substance.md` Phase 4 chapter level — `chapters[].substance_delta.chapter_class` added to the per-chapter authoring list alongside `dramatic_shape`/`goal`/`pov_narrator`. The `/and-write` Phase 6 frame-coda exemption now resolves against a schema-defined field. |
| STRUCT-004 | HARD | `.claude/commands/and-substance.md` Phase 3 line 109 — comment updated from "must appear in this scene's substance_delta.axes_in_motion" to "must appear in this scene's substance_delta.axes_in_motion[] OR axes_held[] (union; per 2026-05-21 axis-bookkeeping split — held-discipline scenes pin stakes to the held axis)." |
| STRUCT-005 | HARD | `CLAUDE.md` directory map — added `theater/proto-lines/` entry documenting it as the canonical merged proto-line file with `[<facet>:<id>]` citations written by `/and-facets` Phase 2 / `build_cite_index.py`, consumed by `/and-facets` Phase 5 auditor + `/and-stitch` Phase 0/1. |
| STRUCT-006 | SIGNAL | `schemas/audit-report.schema.md` line 98 — `/and-season` reference replaced with `/and-facets` Phase 6 + `/and-review verdict <book>` (the actual current consumers). |
| STRUCT-007 | SIGNAL | `design/shoot-v2/rubric-sensory.md` line 335 — "Schema rename (pending)" section heading renamed to "Schema rename (COMPLETE)"; bullet items struck-through; completion record retained for audit-trail with date and STRUCT-007 trace. |
| STRUCT-008 | SIGNAL | `.claude/commands/and-facets.md` Phase 3 R2.4 line 207 — `"tens-discipline holds"` replaced with `"magnitude-band discipline holds (bone fires in hinge-magnitude-class zone per rubric AP7, equivalent to scene-map peak-bones membership)"`. DELETE criterion updated to reference `peak-bones` + `axis_moves[].magnitude` instead of `tens ≠ 3`. |
| STRUCT-009 | SIGNAL | `.claude/commands/and-facets.md` Phase 1 line 131 — `"Upstream tens: citations on the base proto-line are preserved"` replaced with a parenthetical noting that new-chain bones files carry no `tens:` citations and the legacy preservation rule is dropped; legacy archives in `projects/` are ignored on read. |
| STRUCT-010 | SIGNAL | No action required (informational confirmation). |
| STRUCT-011 | SIGNAL | `.claude/commands/and-facets.md` Phase 5 CURVE-SHAPE line 297 — `denouement` chapter description changed to `falling` chapter (the schema's actual enum value); parenthetical note added recording the 2026-05-21 fix. |
| TASTE-FLAG-001 | — | No action (intentional). |
| TASTE-FLAG-002 | — | No action (intentional). |
| TASTE-FLAG-003 | — | No action (intentional). |

---

## Chain-readiness after resolution

All five HARDs resolved. The blocker for `/and-substance chapter b01c02` (STRUCT-004 — `stakes_axis` comment restricting to `axes_in_motion` only) is closed. The `chapter_class` schema gap (STRUCT-003) is closed; held-discipline scenes and frame-coda chapters now have full schema → command-body → rubric coherence.

`/and-substance chapter b01c02` is chain-clean to fire. The remaining followup pre-flight items (F4 — actor_baselines per-chapter validation, F5 — chunk-level rescan, A6 — R2 stale-shard verification, A11 — prune persist-time intermediates, A13 — `/and-review verdict b01`, A14 — schema support for `# rubric-carve-out` preambles, A15 — done via F1, A16 — stitch-profile tuning) are NEAR-TERM or LOW-priority and can land asynchronously.

The audit revealed that the substance-overhaul tensometer-removal landed only ~80% in the previous fixer pass; `/and-stitch.md` and `/and-facets.md` carried operational tensometer residue that hadn't been caught. This pattern is what S-12 (schema-audit-as-gate) is intended to prevent going forward; promoting the tri-walk to `/and-review pipeline` (A10) closes the procedural loop.
