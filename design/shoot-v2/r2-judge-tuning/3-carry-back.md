---
phase: B3 — carry-back synthesis (Plan B execution)
project: R2 hybrid judge tuning
date: 2026-05-10
inputs: PLAN.md v2, B-locked-rubric.md (v1), C-arbiter-protocol.md (v1), .claude/commands/and-facets-r2.md (pre-B3)
outputs: edits to .claude/commands/and-facets-r2.md, B-locked-rubric.md, C-arbiter-protocol.md
status: LANDED — edits applied in this branch (claude/implement-parallel-plan-SzWNb)
---

# Phase B3 — Carry-Back Synthesis

## Edits this phase landed

### `.claude/commands/and-facets-r2.md`

1. **Per-layer §Form re-test** (R2.1, R2.2, R2.3, R2.4). Cold-read against the facet's §Form + Q1 + Q2 + relevant AP gates before any KEEP / DELETE / REVISE / ADD verdict. URI-023 item 9 lands here unconditionally. Customised per facet:
   - R2.1 (NI): §Form + Q1 + Q2 of `rubric-narrator-interest.md`.
   - R2.2 (memory): §Form + Q1 + Q2 of `rubric-memory.md` (monument-grade test, NI-spine test, target-reference resolvability test).
   - R2.3 (feeling): §Form + Q1 + Q2 + AP6 + AP7 of `rubric-feeling.md`. AP6 / AP7 explicit because the feel:10 regression (URI-024) was an AP6 failure.
   - R2.4 (metaphor): §Form + AP3 + AP7 of `rubric-metaphor.md`. Refuse-by-default discipline carried into the cold read.
2. **Decision-log shard emission** per layer. Output blocks now name a shard path:
   - R2.1: `active-project/staff/interest-narrator/r2-decision-shard.md`.
   - R2.2: `active-project/staff/memory/r2-decision-shard.md`.
   - R2.3: `active-project/staff/feeling/r2-decision-shard-<character-slug>.md` (per-character).
   - R2.4: `active-project/staff/metaphor/r2-decision-shard.md`.

   Shard frontmatter conforms to the `.r2-decisions.md` schema clause Plan A A2 lands in `schemas/audit-report.schema.md` (per URI-026 cross-plan F7 emission contract). `f-r2-counts: {f-r2-1: N, f-r2-2: N, f-r2-3: N, f-r2-4: N}` per the Plan B B3.2 spec.

3. **Mid-layer cite-index rebuild flipped optional → mandatory** (Notes section line ~245). Each layer reads cite-index after the previous layer's protoline writes, so the rebuild is a precondition of the read, not an optimisation. Cost: +3 cheap rebuild calls per round.

4. **New Phase 5.5 — Arbiter glue.** Inserted between Round 2 layer execution and Phase 6 (Persist). Main session is the arbiter; reads each shard end-to-end; fires triggers T1 (rubric-label-heavy) and T4 (niche-driven add) only — T2 / T3 / T5 / T6 deferred per `C-arbiter-protocol.md` v2. Bound: ≤2 intervention rounds per verdict; `DISCIPLINE-FAIL` surfaces in shard frontmatter and Phase 6 print summary.

5. **Phase 6 consolidation.** Adds an explicit step concatenating the four layer shards into `active-project/theater/facets/.r2-decisions.md`. Sums per-shard `f-r2-counts:` into a top-of-file frontmatter line on the consolidated file. Threshold note: `f-r2-1 > 0` is HARD; `f-r2-2 + f-r2-3 + f-r2-4 > 2` is SIGNAL — these are informational at the command level; the gate is enforced at orchestrator-critic Phase 6 F7.

6. **Phase 6 print summary** updated to surface the consolidated `f-r2-counts:` and discipline-fail count alongside the existing keep/delete/add table.

7. **Top-of-file callout** added pointing every R2 layer dispatch at `B-locked-rubric.md` and `C-arbiter-protocol.md`. Establishes the locked-rubric + arbiter discipline as a global precondition rather than per-layer recapitulation.

### `design/shoot-v2/r2-judge-tuning/B-locked-rubric.md`

§ Decision-log discipline rewritten. The labeled-subfield template (Justification / Cascade / Original-seam / Cold-read-verdict / Motive / At-rest-test) is replaced with:

- One free-prose paragraph in reviewer voice per verdict.
- Single `VERDICT: KEEP | DELETE (cascade <n>) | REVISE | ADD` line at the end of each block.
- End-of-layer `PATTERN-SCAN:` paragraph (free prose).
- `CAP-REFUSAL:` lines for refused candidates.
- `[ARBITER T1: ...]` / `[ARBITER T4: ...]` traces append inline beneath the affected verdict; revised verdict follows.
- `DISCIPLINE-FAIL` marker for two-intervention exhaustion.

Audit SIGNAL-004 (labeled-subfield template is itself checklist-shaped) closes here. The free-prose discipline is structural — it forces the reviewer to carry the argument as a single thought rather than fill slots.

### `design/shoot-v2/r2-judge-tuning/C-arbiter-protocol.md`

Trigger set reduced from six (T1–T6) to two (T1, T4) live + four (T2, T3, T5, T6) deferred. Each deferred trigger has explicit re-activation criteria recorded; the deferral is evidence-driven, not abandonment. Subagent budget implication restated: ~10–15% inflation rather than the original ~20–30%. v2 revision flag added to frontmatter.

## Edits this phase did NOT land

- `schemas/audit-report.schema.md` `.r2-decisions.md` frontmatter clause — Plan A A2 territory. Plan B emits the format Plan B itself specifies (frontmatter shape recorded inline in `and-facets-r2.md` per layer); Plan A's parallel session lands the schema clause.
- `active-project/audience/*/card.md` body — Plan A A1 territory (tens-attack vocabulary promotion). Plan B's read-only access to these cards remains; B5 sentinel released A1 to proceed (see `4-validation.md`).
- `staff/orchestrator-critic/card.md` F7 amendment — Plan A A2 territory. Plan B's `f-r2-counts:` consolidation in `and-facets-r2.md` Phase 6 is what F7 will read once Plan A lands the verdict-template clause.

## Plan B execution residuals

Three of B's seven actions remain dispatch-heavy and are deferred to a runtime session:

- **B2a — Audience entry-quality review** on existing R2 corpus. ≤6 dispatches. Scaffolded as `2a-audience.md` placeholder (not authored in this branch — would carry per-persona free-form verdicts authored at runtime).
- **B4 — Validation re-run.** ~20 dispatches (4 R2 layers + 6 audience + arbiter overhead + cite rebuilds). Requires `git checkout 3cd53e5 -- active-project/theater/facets/`, which is blocked: `3cd53e5` is not in this repo's git history (see `1-baseline-reconstruction.md`). Recovery option: skip the revert and run R2 against the current post-R2 facets as a regression test, accepting that the run measures judge-discipline drift on a stable corpus rather than from-baseline behavior. Decision deferred to the runtime session.
- **B2b-rerun — Decision-discipline review against native logs.** Depends on B4 producing native `.r2-decisions.md`.

## Validation expectations

The B4 validation is the gate: 0 instances of F-R2-1, ≤2 combined F-R2-2/3/4 across R2-touched entries. The structural infrastructure for that validation — shard emission, free-prose discipline, arbiter T1/T4, consolidated frontmatter — is now in place. Whether the gate clears is a runtime question this session does not answer.
