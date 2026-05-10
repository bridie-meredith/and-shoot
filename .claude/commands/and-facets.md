---
description: Master facet pipeline — chains Round 1 + Round 2 + final audit on one episode's proto-lines. Calls /and-facets-r1, /and-facets-r2, /and-facets-audit in sequence. R3 default-skipped (production-default per convergence signal); fire /and-facets-r3 explicitly if needed. Output - active-project/theater/facets/ + audit report. Usage - /and-facets [episode-slug]
---

Master facet pipeline. Runs the full chain on one episode's protolines:

```
protolines (status: protolined)
        │
        ▼
   PHASE 1 — Round 1: blind authoring (9 facets)         → status: faceted-r1
        │
        ▼
   PHASE 2 — Round 2: hybrid judge (4 midband facets)    → status: faceted-r2
        │
        ▼
   PHASE 3 — Final audit (flag-only)                     → status: audited-r1
        │
        ▼
   final report at active-project/staff/auditor/facets-final-audit.md
```

R3 (relaxation pass) is **default-skipped** in the master chain. Empirical signal from s01e01 (2026-05-10): all 6 R3 dispatches reported zero-change → R2 produces a fixed point under the current rubric set. The standalone `/and-facets-r3` remains callable if a future episode or rubric change makes R3 worth firing explicitly.

You are the orchestrator. The chain executes the dispatch logic from the four sub-commands by reference; this master is a thin sequencer plus a unified summary.

## Args

- `$1` — optional. Episode slug (e.g. `s01e01`). If omitted, use `active.episode` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate (master)

1. Resolve episode slug (arg or `active.episode`).
2. Read `active-project/staff/showrunner/memory.md`. Determine starting status:
   - `protolined` — fresh run; chain starts at Phase 1.
   - `faceted-r1` — partial-run resume; skip Phase 1, start at Phase 2.
   - `faceted-r2` or `faceted-r3` — partial-run resume; skip Phase 1 + 2, start at Phase 3.
   - `audited-r1` — already done; print "already audited; re-running Phase 3 only" and proceed only if explicit re-audit is wanted.
3. Print:
```
Episode: <slug>
Starting status: <status>
Plan: <Phase 1 | Phase 2 | Phase 3 — depending on resume point>
Beginning master chain.
```

---

## Phase 1 — Round 1 (delegated to /and-facets-r1)

If status is `protolined`, execute the full body of `.claude/commands/and-facets-r1.md`. Read that file and follow its dispatch logic verbatim:

- Phase 0 of -r1 (validate `protolined` precondition + read protoline header) — re-runs but is idempotent against the master Phase 0 above.
- Round 1 layers 1-6: tens (dramatist), loc-state (studio), NI (POV impersonator), sensory (studio), state-updates env (studio) + per-actor (impersonators), memory (POV impersonator), feeling (per-character impersonators), metaphor (editor), vibes (showrunner).
- Phase 6 of -r1: status `protolined` → `faceted-r1`.
- Phase 7 of -r1: rebuild cite-index.

**Key reminder enforced by the master:** the dramatist is Read-only; the orchestrator writes `tensometer.md` from the dramatist's returned ratings payload. Per-character impersonator briefs MUST list explicit absolute paths to all nine facet files when reading the graph (the agent has no globbing tool — implicit paths cause refusal).

If status is already `faceted-r1` or beyond, skip Phase 1.

---

## Phase 2 — Round 2 (delegated to /and-facets-r2)

If status is `faceted-r1` (or just transitioned from Phase 1), execute the full body of `.claude/commands/and-facets-r2.md`. Read that file and follow its dispatch logic verbatim:

- Phase 0 of -r2: validate `faceted-r1` + cite-index present.
- Round 2 layers R2.1-R2.4: NI judge, memory judge, feeling judge per character (×N cast), metaphor judge.
- Phase 6 of -r2: status `faceted-r1` → `faceted-r2`.
- Phase 7 of -r2: rebuild cite-index.

**Key reminder enforced by the master:** every midband author dispatch payload MUST include the full nine-facet graph + cite-index, not the DAG-upstream subset. Per the captured Round 2 directive (user 2026-05-10).

If status is already `faceted-r2` or beyond, skip Phase 2.

---

## Phase 3 — Final audit (delegated to /and-facets-audit)

If status is `faceted-r2` or `faceted-r3` (or just transitioned from Phase 2), execute the full body of `.claude/commands/and-facets-audit.md`. Read that file and follow its dispatch logic verbatim:

- Phase 0 of -audit: validate `faceted-r2` or `faceted-r3` + cite-index present.
- Single auditor dispatch with full graph; produces classified findings report.
- Phase 6 of -audit: status `faceted-r2|r3` → `audited-r1`.

**Key reminder:** audit runs in flag-only mode. No mutations to facet or protoline files. Findings are advisory; remediation routes back to facet authors as a separate work cycle.

If status is already `audited-r1`, the audit has already run. The master prints the existing report path and exits unless an explicit re-audit is wanted.

---

## Phase 4 — Master summary

After all delegated phases complete, the master prints a unified summary that aggregates the per-phase summaries:

```
========================================================
=== /and-facets MASTER CHAIN COMPLETE: <episode-slug> ===
========================================================

Phase 1 — Round 1 (Step A):
  9 facet files authored
  <count> total entries; <count>/<count> protolines decorated
  Process gaps fixed: <list>

Phase 2 — Round 2 (Step D):
  4 midband facets judged
  R1 → R2 deltas:
    narrator-interest:    K=<n> D=<n> A=<n>
    memory:               K=<n> D=<n> A=<n>
    feeling:              K=<n> D=<n> A=<n>
    metaphor:             K=<n> D=<n> A=<n>
  Citation accrual: <count> → <count> protolines decorated.

Phase 3 — Final audit (Step G):
  Mode: flag-only
  Findings:
    CONTRADICTION:    <count>
    DEDUP:            <count>
    SUPERFLUOUS:      <count>
    CONSTRAINT:       <count>
    PILE-UP REVIEW:   <warranted> warranted / <over> over-decoration
  Total: <count> findings (CLEAN if zero)
  Report: active-project/staff/auditor/facets-final-audit.md

R3 (relaxation pass) skipped per default. Fire /and-facets-r3 explicitly
if R2's diff is non-trivial and Step I oscillation measurement is wanted.

Status: <slug> audited-r1
```

---

## Skipping R3 — what to do when audit findings warrant another judge round

If Phase 3 surfaces FINDINGS-PRESENT and the findings include rubric-violations that are likely to be addressed by another midband author judge pass (e.g., constraint violations on memory or feeling), the recommended path is **NOT** to fire R3. R3 is an unconditioned relaxation pass; it cannot target specific findings.

Instead, fire **targeted remediation dispatches** against the specific findings — one dispatch per routed author, with the audit report's specific findings as the brief. This is the "tuning loop" entry point. The fixer agent or the original facet author handles each finding per its routing.

Once remediations land, re-run `/and-facets-audit` to verify the findings cleared.

---

## Notes

- **Sub-commands remain callable.** `/and-facets-r1`, `/and-facets-r2`, `/and-facets-r3`, `/and-facets-audit` each remain individually invocable for partial runs, resume after a failure, or re-running a specific phase.
- **The master's source-of-truth is the sub-commands.** When you read `.claude/commands/and-facets-r{1,2}.md` and `.claude/commands/and-facets-audit.md` for dispatch rules, those files are authoritative. The master is a sequencer plus aggregated reporting; do not duplicate the sub-commands' dispatch logic into this file.
- **Status flips happen in the sub-commands, not in the master.** Each sub-command updates `active-project/staff/showrunner/memory.md` at its own Phase 6. The master's Phase 0 inspects the current status to decide where to start; the master's Phase 4 inspects the final status to print the summary.
- **R3 default-skip is a Step I production-deployment decision** based on the s01e01 convergence signal (R2 produced a fixed point; R3 zero-change rate 100%). Revisit this default if a future episode shows R2 producing oscillation or large diffs.
