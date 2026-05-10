---
design: three-pass-facet-pipeline
date: 2026-05-09
revised: 2026-05-09 (Alpha → Beta after design conversation)
scope: facet authoring pipeline for shoot-v2 (post per-facet tuning)
status: DESIGN-ACCEPTED — no implementation yet
relates-to: facet-dependency-audit.md, schemas/facet.schema.md, schemas/proto-line.schema.md
---

# Three-Pass Facet Pipeline — Design

## Premise

Per-facet tuning is locked for ten facets. Composing them into a single authoring run is unbuilt. Single-pass authoring leaves enrichment value on the table: downstream facets (metaphor especially) routinely want to fire on anchors that upstream facets (memory / feeling) didn't write strongly enough, and unused upstream entries pile up as dead weight.

Beta solves this with three rounds per episode plus a final cross-cutting audit.

## The three rounds (Beta — chosen variant)

| Round | Visibility | Operation | Scope |
|---|---|---|---|
| 1 | bones-only protolines (no foreign citations) | blind authoring (current per-facet tuning Phase-2 spec) | all ten facets |
| 2 | full citation graph + gap-logs | per-entry judge: keep / add / delete-own | NI, memory, feeling, metaphor (interpretive midband) |
| 3 | post-Round-2 state | per-entry judge: keep / add / delete-own | midband; same authors as Round 2 |

**Final audit** runs after Round 3: cross-cutting constraint check, dedup, superfluous-removal, contradiction detection.

vibes-updates runs once at end of Round 1. Re-run after final audit is deferred until licensing-skew impact is observed.

### Round semantics

**Round 1 — Blind.** Each facet author reads bones-only protolines and authors per its existing per-facet tuning Phase-2 rubric. No visibility into other facets' citations. Same as current single-pass design. Pass-1 midband authors additionally emit a gap-log: `@<proto-id>: wanted <kind>; missing <anchor-type>; gloss: <one clause>`.

**Round 2 — Judge with full graph.** Each midband facet author reads the full Round-1 graph (all foreign citations on protolines, all foreign facet entries) plus all gap-logs. The author's unit of work is per-entry: for each existing entry, decide keep / delete; for unfilled niches the graph reveals, decide add. **Deletion is self-scoped** — memory can delete `mem:7` but cannot delete `feel:3`. New entries follow the same rubric as Round-1 authoring (gap-log is a hint, not a license).

**Round 3 — Judge again.** Same operation as Round 2 against the post-Round-2 state. This is the relaxation iteration that lets the system settle after Round-2 mutations cascade.

### Self-scope rule (default)

Each facet author can delete only entries authored by their own facet. Cross-facet deletion authority belongs to the final audit only. Confirmed default; revise if measurement shows authors need cross-facet pruning power.

### Final audit teeth

Final audit is **delete-authoritative**. It can remove any entry from any facet — cross-facet authority — when the entry contradicts a constraint, duplicates another entry, is superfluous, or fails a cross-cutting consistency check. The auditor itself will be tuned (rubric, thresholds, refusal discipline) before delete authority is exercised in production; until tuning lands, audit findings are flag-only and routed back to facet authors. Once tuned, the auditor's deletions are final — facet authors are not consulted on individual cuts.

Rationale for full delete authority: the auditor sees the whole graph in one pass and has the standing to enforce cross-cutting constraints that no single facet author can enforce locally. Self-scope deletion at Round 2/3 covers the within-facet case; the auditor covers the across-facet case.

## Four required mechanisms

1. **Cite-index** — derived `_cite-index.md` rebuilt at end of Round 1, end of Round 2, end of Round 3. Maps `<facet>:<id>` → `cited-by [<facet>:<id>, ...]` + cite-count. Round-2 and Round-3 deletion-candidate input.
2. **Gap-logs** — per-midband-facet side-log emitted in Round 1 (`_gaps/<facet>-gaps.md`). Format: `@<proto-id>: wanted <kind>; missing <anchor-type>; gloss: <one clause>`. Round-2 enrichment input. Hint, not contract.
3. **Snapshot dirs** — `_round1/`, `_round2/`, `_round3/` frozen copies of facet files AND of the proto-lines file at each round boundary. Final audit and oscillation measurement read these.
4. **Convergence-by-measurement** — no formal monotonicity audit between rounds. Instead, post-Round-3 measurement reports per-facet diff sizes (Round-1→Round-2, Round-2→Round-3) and oscillation detection (entries added in one round and deleted in the next, or deletion+re-add patterns). See "Empirical measurement plan" below.

## Build order

Build incrementally; each step has standalone value and can be a stopping point.

| Step | What | Status |
|---|---|---|
| A | `/and-facets` Phase-0 + Round 1 only, on s01e01 | **shipped 2026-05-10** |
| B | Cite-index builder | **shipped 2026-05-10** — `active-project/staff/cite-index/build_cite_index.py`; wired into `/and-facets` Phase 7 as default output |
| C | Gap-log emission added to Round-1 midband authoring | **deferred indefinitely** — reclassified as debug-only per user direction 2026-05-10b; Round 2 gates additions through the per-facet rubric, gap-logs are not load-bearing for default flow |
| D | Round 2 (hybrid judge with full graph) on memory + feeling | unbuilt |
| E | Round 3 (repeat hybrid judge) on memory + feeling | unbuilt |
| F | Add NI + metaphor to Rounds 2 and 3 | unbuilt |
| G | Final audit (flag-only initially; delete-authoritative once auditor tuned) | unbuilt |
| H | Wire all rounds into `/and-facets` with `--from-round=N` resume | unbuilt |
| I | Oscillation measurement + decide whether convergence machinery is needed | unbuilt |

Step I is the empirical decision point. If measurement shows clean convergence, we ship Beta. If oscillation is observed, we add Gamma machinery (oscillation detector + zero-change skip) without redesigning the pipeline.

## Empirical measurement plan

Before adding any convergence machinery, run Beta on real corpus and measure:

1. **Per-facet diff sizes.** `|Round-2 − Round-1|` and `|Round-3 − Round-2|` per facet. Hypothesis: Round-3 diff is smaller than Round-2 diff (relaxation settling). If Round-3 diff ≥ Round-2 diff, system is not settling and Round 3 is harming, not helping.
2. **Oscillation rate.** Per facet, count entries that were added in Round 2 and deleted in Round 3 (or deleted in Round 2 and re-added in Round 3 in semantically-similar form). Threshold tbd; even a low rate is signal worth investigating.
3. **Final-audit finding count.** If final-audit surfaces lots of contradictions or duplications, the round-2/3 judgment process is missing things and either the gap-log mechanism or the visibility set needs tuning.
4. **Round-3 zero-change rate.** Per facet, frequency of "Round 3 made zero changes." High rate = Round 3 is structurally unnecessary for that facet (skip in production).

Measurement runs on s01e01 first (single episode, full instrumentation). Promote to s01e02-e06 once Step I has produced a baseline judgment.

## Risks and mitigations

### R1 — Author-fork drift between rounds

Same dialogue-writer fork firing on the same character at Rounds 1 / 2 / 3 may produce inconsistent voice (different turn of phrase, different somatic register, different memory-monument selection bias).

**Mitigation:** Round-2 and Round-3 authors read prior-round output as authoritative context. Additions must be voice-consistent with prior-round entries on the same character; final audit flags voice-inconsistent additions for the facet author to reconsider.

### R2 — Token cost

Three rounds + final audit ≈ 1.8–2.5× single-round cost (Round 1 is bulk; Rounds 2 and 3 are smaller because midband only). Final audit adds a fixed cost for cross-cutting review.

**Mitigation:** per-facet per-round add-cap (default ≤3–5 new entries). Cap enforced at audit time. Cap is per-facet per-round per-episode and tunable per-facet (memory and feeling may warrant higher caps than NI). Round-3 skip when Round-2 produced zero changes for a facet (added in Step I once empirical zero-change rate is known).

### R3 — Gap-log hallucination

The "wanted but couldn't" gap-log can be invented retroactively by the Round-1 author — there is no ground truth that says a metaphor author *actually* wanted to fire on @73. A motivated author could pad the gap-log to influence Round-2 judgment.

**Mitigation:** gap-logs are treated as hints, not contracts. Round-2 author must meet the regular per-facet rubric to add an entry — the gap-log only directs attention, it does not license entries. Final audit deletes Round-2 additions that fail the regular rubric on cite-count or anchor-quality grounds, regardless of gap-log provenance.

### R4 — Round-3 over-pruning at sparsity floor

Original framing: memory (1–5%) and feeling (2–5%) bands could be breached by aggressive Round-3 deletion, putting the facet structurally below its tuned floor.

**REVISED — no deletion floor.** Per design decision 2026-05-09: non-value-added entries are removed regardless of band minimums. Sparsity floors were authored as guides for Round-1 authoring density, not as inviolable structural minimums. If Round-3 deletion drops a facet below its tuning-package band, that is *signal*, not *failure*:

- It may mean Round-1 over-fired (the floor was overcalibrated as a target rather than a baseline).
- It may mean the episode's content shape genuinely doesn't support that density.
- Either reading is more useful than retaining dead-weight entries to hit a number.

**Mitigation:** Round-3 cull is unconstrained by floors. Below-floor outcomes are surfaced in the final audit as a flagged finding for the tuning-package author to consider, not as a deletion-blocker. The cite-index and audit output together are sufficient diagnostic — no retention rule is needed.

This decision implies tuning packages may need re-reading: any rubric that *gates* on hitting a floor (rather than treating the floor as a soft target) is mis-tuned. Audit pass over the ten tuning packages for floor-as-gate language is a follow-on if Round-3 results indicate.

### R5 — No facet-authoring command exists yet

Per-facet tuning packages have Phase-2 dispatch specs, but they have never been composed into a single orchestrator. Step A absorbs the integration cost regardless of whether Beta continues; this is unbuilt baseline work, not Beta-specific overhead.

**Mitigation:** none required — this is a build cost, not a risk. Acknowledged so the cost is not double-counted as Beta overhead.

### R6 — Citation cascade on deletion

The proto-lines file IS the citation-bearing artifact (per `schemas/proto-line.schema.md` §"`[<cited-id>, ...]`"). When a facet author deletes `mem:7` in Round 2 or 3, every proto-line that had `[mem:7]` in its citation list also needs that citation stripped. Cross-file cascade.

**Mitigation:** facet-author dispatch responsibility. Each facet author who deletes one of their entries also strips that entry's citation from every proto-line that referenced it. Cite-index makes the affected proto-lines cheap to identify (it already maps `<facet>:<id>` → cited-by set). Final audit verifies no orphan citations remain on protolines.

### R7 — Coordination on shared protolines file

All facet authors write back to the same proto-lines file (citation accrual). If memory and feeling both want to add citations to proto-line @42 in the same round, there's a write race.

**Mitigation:** sequential dispatch within each layer of the DAG. Same-layer facets (e.g. memory and state-updates at LAYER 3) dispatch in series, not parallel, when both write protoline citations. Existing per-facet tuning packages likely already assume this; verify at Step A.

### R8 — Non-termination / oscillation between Rounds 2 and 3

Without monotonicity per round, Round 2 and Round 3 are non-monotonic judgment passes. Round 3 could reverse a Round-2 decision (delete what was added, add what was deleted).

**Mitigation (measurement-first):** do not pre-emptively add convergence machinery. Run Beta and measure (see "Empirical measurement plan"). If oscillation rate is low and Round-3 diff is consistently smaller than Round-2 diff, the relaxation is settling and no machinery is needed. If oscillation is real, Step I adds Gamma machinery: oscillation detector + Round-3 zero-change skip + (if needed) explicit settling criterion. Designed-in machinery for a problem we haven't observed is overhead; observe first, mitigate empirically.

## Open decisions (deferred)

- Whether to re-run vibes-updates after final audit. Default: no, accept licensing skew. Revisit after first end-to-end run if skew is observed in stitched output.
- Whether to add NI to Rounds 2 and 3 from the start, or only after memory + feeling Beta is validated. Default: only after — Step F. NI is the spine; mistakes there propagate.
- Whether to add metaphor to Rounds 2 and 3. Default: yes (Step F), but evaluate after seeing memory/feeling Round-2 behavior. Metaphor's refuse-by-default discipline may make Round 2 mostly add-only and Round 3 mostly no-op.

## What this document is not

- Not a build spec. Per-step build specs are written when each step starts; this document is the architecture and the design constraints those specs must respect.
- Not a re-tuning of any locked facet. Round-1 authoring follows existing tuning packages verbatim. Rounds 2 / 3 are additive judgment machinery that does not modify per-facet rubrics, with one possible exception flagged under R4 (floor-as-gate audit if surfaced).
- Not Alpha. The earlier Alpha variant (write → add-only → delete-only with monotonicity audits) is superseded by Beta after design conversation 2026-05-09. Alpha's monotonicity argument was for formal convergence; Beta accepts empirical convergence and validates by measurement instead. If measurement shows oscillation, Gamma machinery (oscillation detector + zero-change skip) is added on top of Beta — Alpha is not revived.
