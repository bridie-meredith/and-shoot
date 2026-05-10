---
design: shared-review-mechanism
date: 2026-05-10
status: SKETCH — pre-implementation; URI-025 in upstream-tuning-queue
purpose: Factor the /and-facets cross-cutting review stack into a shared module that both /and-facets and /and-season consume. Same auditor, same rubrics, same sub-classes — invoked at multiple stages of the pipeline.
parent: design/shoot-v2/upstream-tuning-queue.md (URI-025)
---

# Shared Review Mechanism — /and-season + /and-facets

## Principle

**One review surface, multiple invocation points.** The facet review stack — tensometer, sensory, state-updates, and the cross-cutting auditor (CURVE-SHAPE, FREQUENCY-BAND, AP-SCAN, STRUCTURAL, CONSTRAINT) — is authored once and called from both pipelines.

Today /and-facets owns this stack and runs it on the per-episode facet graph. /and-season owns its own season-scope review (S1–S9) plus the orchestrator-critic verdict at Phase 6, but has no facet-shape verdict on the aggregate or per-episode SVOs.

The result: shape-class failures originating at the bone level (e.g. URI-002 SHAPE-FAIL on s01e01: 6 of 8 scenes lacking rung-3 peaks) are caught at facet-stage where the fix is most expensive — re-author protolines, re-run facets, redo audit. Catching the same failure at /and-season's aggregate stage costs only a screen-writer regeneration of the aggregate bones.

This document specifies the factoring.

---

## What the shared module is

A logical module — not necessarily a new directory. The "module" is the set of subagent rubrics + class definitions that both pipelines call:

| Asset | Location | Used by |
|---|---|---|
| Facet authors (tensometer, sensory, state-updates, etc.) | `design/shoot-v2/rubric-*.md` + agent definitions | /and-facets-r1, /and-facets-r2; **(new)** /and-season Pass S9.5 |
| Facet auditor classes | `.claude/commands/and-facets-audit.md` | /and-facets-audit; **(new)** /and-season Pass S9.5 |
| Auditor sub-classes (URI-018/019/020 when landed) | same | both pipelines |

**No fork.** The rubrics are the source of truth. /and-season does not author its own copy of CURVE-SHAPE; it calls the same auditor command/dispatch and consumes the same verdict.

---

## The three invocation points

### IP-1 — /and-facets (existing, unchanged)

Per-episode facet graph review. Runs after R1 author + R2 hybrid judge + audit. This is the canonical home of the review stack. **No change.**

### IP-2 — /and-season Pass S9.5 (new — aggregate-scope)

Position: between Pass S9 and Phase 4 split.

Subset of facets fired at the aggregate level (treat the season aggregate as one giant proto-line file):

- **tensometer** — full rung distribution + curve-shape across 900-line aggregate.
- **sensory** — modality density + delta continuity at season scope.
- **state-updates** — env + actor state coverage at season scope.
- *(not at S9.5)* feeling, vibes-updates, metaphor, narrator-interest, memory-flags. These need scene-stable POV and per-character context that the aggregate stage does not provide cleanly. Reserve them for IP-3.

Auditor classes fired at S9.5:

- **CURVE-SHAPE** — at season scope (already done by S9; the auditor adds bone-level peak-coverage check that S9 does not).
- **AP-SCAN** — anti-pattern surface scan across aggregate.
- *(not at S9.5)* STRUCTURAL (per-section monotonicity is a per-facet-file concern; aggregate has one stream), CONSTRAINT (behavior-card sequence checks need the per-character facets that aren't authored at S9.5).

**Output:** S9.5 verdict report at `active-project/staff/auditor/season-s<N>-pass-S9.5.md`. Classified findings, same schema as /and-facets-audit.

**Dispatch budget:** ~12 dispatches (3 facet authors + 1 auditor + R2 if shape findings warrant + revision dispatches).

**Failure handling:** HARD findings at S9.5 route to screen-writer regeneration of bones in the affected aggregate range, with re-pass through Pass S9.5 to confirm clean. Iteration cap inherits from orchestrator-critic (3 per phase).

### IP-3 — /and-season Phase 5.5 (new — per-episode-scope, flag-driven)

Position: after Phase 4 split, before Phase 6 verdict.

Per-episode /and-facets pass on the split SVO files. **Default: skip.** Opt-in by:
- explicit flag (`/and-season --facet-pass`), or
- S9.5 auditor flagged the affected aggregate range as suspect and Phase 4 split assigned it to a specific episode.

When fired: identical to existing /and-facets pipeline — R1, R2, audit. Output goes to `active-project/theater/facets/` per episode (the canonical location).

**Dispatch budget:** ~25–30 per episode. With 6 episodes flagged-only typically 1–2, total ~30–60. Fits under the orchestrator-critic 60-dispatch hard cap **only** if flag-driven; running by-default on every episode breaks the cap.

**Failure handling:** HARD findings route to per-episode screen-writer or per-facet author revision; re-pass; recurse with the same iteration cap.

---

## Phase 6 verdict integration

The orchestrator-critic card produces a PASS / PASS-WITH-NOTES / FAIL verdict. With S9.5 and Phase 5.5 added, the verdict template extends:

- **Convergence** — already covers iteration counts and dispatch totals. Adds: did S9.5 / Phase 5.5 converge inside their iteration caps?
- **Quality** — already covers content-critic verdicts. Adds: S9.5 auditor verdict; Phase 5.5 facet-graph verdict (if fired).
- **Routing** — already covers dispatch routing. No change.

If S9.5 returns HARD findings that the iteration cap could not close, the verdict is PASS-WITH-NOTES at minimum (named residuals) or FAIL (if budget exhausted on the same finding). Same decision logic the orchestrator-critic already runs.

---

## Phased rollout

**Phase 1 — Now (Pass S9.5, reduced):**

- tensometer + facet-auditor (CURVE-SHAPE + AP-SCAN classes only).
- ~12 dispatches.
- Validates the architecture cheaply. URI-002 is the test case — does S9.5 catch on the s01 aggregate the SHAPE-FAIL that surfaced at facet-stage?

**Phase 2 — After URI-006 (auditor tuning) lands:**

- Promote S9.5 auditor to delete-authoritative (currently flag-only).
- Land URI-018 (CURVE-SHAPE-EPISODE-INTERIOR), URI-019 (CONSTRAINT behavior sub-classes), URI-020 (AP-SCAN-POST-PEAK-WINDOW-QUALITY) into the shared auditor — both pipelines benefit.
- Add sensory + state-updates to S9.5's facet set if Phase 1 verdict-discipline data warrants.

**Phase 3 — After Phase 1+2 produce verdict-discipline data:**

- Wire Phase 5.5 (flag-driven per-episode /and-facets).
- Recalibrate orchestrator-critic dispatch budget against measured per-run costs. The card permits this empirically.

---

## What changes in the codebase (Phase 1 only)

- `.claude/commands/and-season.md` — new Pass S9.5 between S9 and Phase 4. Calls tensometer + facet-auditor (CURVE-SHAPE + AP-SCAN). Records verdict to `active-project/staff/auditor/season-s<N>-pass-S9.5.md`.
- `.claude/commands/and-facets-audit.md` — no change in Phase 1 (calling shape stays scoped to /and-facets). The shared call surface emerges naturally as Phase 2 lands sub-classes that are aggregate-aware.
- `staff/orchestrator-critic/card.md` — Phase 6 verdict template grows a §S9.5-findings line.
- `CLAUDE.md` — Rule 10 updated to name S9.5 alongside Phase 6 as gates.

No new agent classes. No new file schemas. The factoring is a routing change, not a re-architecture.

---

## What this is NOT

- **Not** a fork of the facet auditor. The same auditor command runs from both pipelines.
- **Not** a replacement for /and-facets. /and-facets remains the canonical per-episode review path; S9.5 is upstream coverage, not substitution.
- **Not** a guarantee against facet-stage findings. S9.5 catches shape and AP-SCAN; per-character facets (feeling, vibes, metaphor) still need IP-3 or /and-facets to surface.

---

## Open questions

1. **Aggregate vs per-scene tens distribution thresholds.** Tensometer rubric is calibrated on per-episode corpus. At aggregate scope, the rung-band targets (e.g. 5–10% rung-3) should hold *per scene-equivalent window* but may need a different aggregation rule. Phase 1 first run is the calibration data point.
2. **What flags Phase 5.5?** Is it "S9.5 returned HARD on a window assigned to episode N" or "user invoked --facet-pass" or both? Default: both, OR semantics.
3. **Does Phase 5.5 redo R2 or only R1?** R1 is faster but less thorough. Phase 1 will not answer this; Phase 3 calibrates.

---

## Success criteria for the URI-025 close

URI-025 closes when:

- Phase 1 lands and produces a verdict on at least one /and-season run.
- The verdict's S9.5 findings either (a) catch a known shape failure that previously surfaced at /and-facets stage, or (b) clean-pass with documented justification (the season aggregate genuinely had no aggregate-scope shape problem to catch).
- The orchestrator-critic Phase 6 verdict template includes S9.5 findings as inputs.
- Phase 2 + Phase 3 are scoped as separate URIs with named dependencies.
