---
design: three-pass-alpha-facet-pipeline
date: 2026-05-09
scope: facet authoring pipeline for shoot-v2 (post per-facet tuning)
status: DESIGN-ACCEPTED — no implementation yet
relates-to: facet-dependency-audit.md, schemas/facet.schema.md
---

# Three-Pass Alpha Facet Pipeline — Design

## Premise

Per-facet tuning is locked for ten facets. Composing them into a single authoring run is unbuilt. Single-pass authoring leaves enrichment value on the table: downstream facets (metaphor especially) routinely want to fire on anchors that upstream facets (memory / feeling) didn't write strongly enough, and unused upstream entries pile up as dead weight.

Alpha solves this with three monotonic passes per episode.

## The three passes (Alpha order: write → add → delete)

| Pass | Direction | Operation | Scope |
|---|---|---|---|
| 1 | forward DAG | blind authoring (current per-facet tuning Phase-2 spec) | all ten facets |
| 2 | forward DAG | enrichment **add-only**; authors see full pass-1 graph + gap-logs | NI, memory, feeling, metaphor (interpretive midband) |
| 3 | **reverse DAG** | cull **delete-only**; authors see full pass-1+2 graph + cite-index | NI, memory, feeling, metaphor |

Monotonicity per pass is the convergence guarantee — pass 2 cannot delete; pass 3 cannot add. Without monotonicity the pipeline can oscillate.

vibes-updates runs once at end of pass 1. Re-run after pass 3 is deferred until licensing-skew impact is observed.

## Four required mechanisms

1. **Cite-index** — derived `_cite-index.md` rebuilt at end of pass 1 and end of pass 2. Maps `<facet>:<id>` → `cited-by [<facet>:<id>, ...]` + cite-count. Pass-3 deletion candidate input.
2. **Gap-logs** — per-midband-facet side-log emitted in pass 1 (`_gaps/<facet>-gaps.md`). Format: `@<proto-id>: wanted <kind>; missing <anchor-type>; gloss: <one clause>`. Pass-2 enrichment input.
3. **Monotonicity audit** — auditor task between passes. Post-pass-2: diff against `_pass1` snapshot, assert add-only. Post-pass-3: diff against `_pass2` snapshot, assert delete-only. Failure halts pipeline.
4. **Snapshot dirs** — `_pass1/`, `_pass2/` frozen copies for diff and audit trail. Canonical files are what stitch reads.

## Build order

Build incrementally; each step has standalone value and can be a stopping point.

| Step | What | Status |
|---|---|---|
| A | `/and-facets` Phase-0 + Pass 1 only, on s01e01 | unbuilt |
| B | Cite-index builder | unbuilt |
| C | Pass 3 on memory + NI (delete-only) | unbuilt |
| D | Gap-log emission added to Pass-1 midband authoring | unbuilt |
| E | Pass 2 on memory + feeling (enrichment add-only) | unbuilt |
| F | Full Alpha wired into `/and-facets` with `--from-pass=N` resume | unbuilt |
| G | Add metaphor to Pass 2/3; decide vibes-updates re-run | unbuilt |

## Risks and mitigations

### R1 — Author-fork drift between passes

Same dialogue-writer fork firing on the same character at pass 1 and pass 2 may produce inconsistent voice (different turn of phrase, different somatic register, different memory-monument selection bias).

**Mitigation:** pass-2 author reads pass-1 output as authoritative context. Additions must be voice-consistent with pass-1 entries on the same character; pass-3 cull treats voice-inconsistent pass-2 additions as deletion candidates regardless of cite-count.

### R2 — Token cost

Three passes ≈ 1.5–2× single-pass cost (pass 1 is the bulk; passes 2 and 3 are smaller because midband only and add-only / delete-only).

**Mitigation:** pass-2 hard cap of ≤3–5 additions per facet per episode. Cap enforced at audit time, not at authoring prompt — over-cap additions are deleted by the monotonicity auditor as add-budget violations. Cap is per-facet, per-episode, and tunable per-facet (memory and feeling may warrant higher caps than NI).

### R3 — Gap-log hallucination

The "wanted but couldn't" gap-log can be invented retroactively by the pass-1 author — there is no ground truth that says a metaphor author *actually* wanted to fire on @73. A motivated author could pad the gap-log to influence pass-2 enrichment.

**Mitigation:** gap-logs are treated as hints, not contracts. Pass-2 author must meet the regular per-facet rubric to add an entry — the gap-log only directs attention, it does not license entries. Pass-3 cull deletes pass-2 additions that fail the regular rubric on cite-count or anchor-quality grounds, regardless of gap-log provenance.

### R4 — Pass-3 over-pruning at sparsity floor

Original framing: memory (1–5%) and feeling (2–5%) bands could be breached by aggressive pass-3 deletion, putting the facet structurally below its tuned floor.

**REVISED — no deletion floor.** Per design decision 2026-05-09: non-value-added entries are removed regardless of band minimums. Sparsity floors were authored as guides for pass-1 authoring density, not as inviolable structural minimums. If pass-3 deletion drops a facet below its tuning-package band, that is *signal*, not *failure*:

- It may mean pass-1 over-fired (the floor was overcalibrated as a target rather than a baseline).
- It may mean the episode's content shape genuinely doesn't support that density.
- Either reading is more useful than retaining dead-weight entries to hit a number.

**Mitigation:** pass-3 cull is unconstrained by floors. Below-floor outcomes are surfaced in the post-pass-3 audit as a flagged finding for the tuning-package author to consider, not as a deletion-blocker. The cite-index and audit output together are sufficient diagnostic — no retention rule is needed.

This decision implies tuning packages may need re-reading: any rubric that *gates* on hitting a floor (rather than treating the floor as a soft target) is mis-tuned. Audit pass over the ten tuning packages for floor-as-gate language is a follow-on if pass-3 results indicate.

### R5 — No facet-authoring command exists yet

Per-facet tuning packages have Phase-2 dispatch specs, but they have never been composed into a single orchestrator. Step A absorbs the integration cost regardless of whether Alpha continues; this is unbuilt baseline work, not Alpha-specific overhead.

**Mitigation:** none required — this is a build cost, not a risk. Acknowledged so the cost is not double-counted as Alpha overhead.

## Open decisions (deferred)

- Whether to re-run vibes-updates after pass 3. Default: no, accept licensing skew. Revisit after first end-to-end run if skew is observed in stitched output.
- Whether metaphor needs pass 2/3 at all. Default: include in step G after seeing memory/feeling pass-2/3 behavior.
- Whether per-character pass-2 additions should be capped per-character or per-facet aggregate. Default: per-facet aggregate; revisit if one character monopolizes additions.

## What this document is not

- Not a build spec. Per-step build specs are written when each step starts; this document is the architecture and the design constraints those specs must respect.
- Not a re-tuning of any locked facet. Pass-1 authoring follows existing tuning packages verbatim. Pass 2/3 are additive machinery that does not modify per-facet rubrics, with one possible exception flagged under R4 (floor-as-gate audit if surfaced).
