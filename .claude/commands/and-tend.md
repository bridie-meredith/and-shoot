---
description: The single consolidated improvement routine. Runs several times a day, work-queue + cadence driven. Conducts the meta-layer pyramid (artur hygiene, oskar triage, ingrid retrospective, margit library, arbiter judging, admin proposals, /and-forge tuning) to improve the library, the agents, and the processes. Defers when a chapter cascade is in flight. Full authority within owning-agent rules - persona content escalates; non-persona mutations are save-as-new. Budget-bounded; no-op-friendly. Mirrors the RUNBOOK R1-R5 discipline. Usage - /and-tend [--budget N] [--force] [--only <module>] [--dry-run]
---

# /and-tend

One routine, run several times a day, that does the work the scattered cadence routines used to do — consolidated. It conducts the meta-layer: hygiene (artur), triage (oskar), retrospective (ingrid), library (margit), judging (arbiter), proposals (admin), tuning (`/and-forge`). It improves **the library, the agents, and the processes** — not the fiction.

**The design that lets it run several times a day:** cadence is decoupled from frequency. Each scan-class has a *cadence* (how often it's worth doing); each run drains whatever is *due* within a *budget*. Most runs are cheap (nothing due → near-no-op). A weekly card-audit doesn't run on every invocation — it runs on the first invocation after it comes due. Over a day, several runs chew through the backlog.

**Full authority within owning-agent rules** (principal-granted). The routine may dispatch the seats to make real fixes. But: **persona content escalates** (admin → principal; never auto-applied); **non-persona card mutations are save-as-new** (margit reconciles); Rules 19/20/21 apply to every dispatch; agent-`.md`/spec edits go through ingrid's delegated authority.

---

## Phase 0 — Orient & gate (read-only)

1. Read the ledger `staff/ingrid/tend-state.md` (scan-class cadences + last-run stamps + carried work queue + run-history tail). If absent, treat all scan-classes as due and seed it in Phase 4.
2. **Defer gate.** Read `active-project/staff/showrunner/cascade-checkpoint.md`. If a chapter cascade is in flight (`mode: unattended` and not terminal), **defer**: print `DEFERRED: cascade-active` + the in-flight chapter, write nothing, exit. (`--force` overrides — only for read-only modules; never contend on state a cascade is writing.)
3. **Parking-lot scan (Rule 14)** for `/and-tend` items.
4. Compute the **due set**: scan-classes whose `last_run + cadence < now`, plus any `open` carried queue items, plus any `--only <module>` filter.
5. Mirror RUNBOOK **R3**: print one pre-flight block, then go silent.

```
================================================================
AND-TEND — PRE-FLIGHT
================================================================
Cascade            : CLEAR | DEFERRED (b<NN>c<MM> in flight)
Due this run       : <scan-classes due>  |  none (no-op)
Carried queue      : <N> open items
Budget             : <N> dispatches (default 12)
Parking-lot        : <N> /and-tend items
----------------------------------------------------------------
Going silent. End-of-run digest will be the next message.
================================================================
```

If nothing is due and the queue is empty → print `NO-OP: nothing due` and exit (cheap).

---

## Phase 1 — Survey (cheap signal refresh)

Within budget, refresh the work queue:
- Dispatch **artur** for any due hygiene op (`taxonomy_audit` / `index_sweep` / `stm_sweep` / `parking_lot_hygiene` / `state_sync`). Artur applies trivial fixes in-dispatch and returns routed findings.
- Read `staff/admin/process-proposals.md`: deferred proposals past `defer_until` (→ re-surface), `open` proposals with rising recurrence.
- Read `staff/oskar/patterns.md`: patterns at/over promotion threshold.
- Read recent `/and-stitch` Phase 9 cold-reads + `/and-postop` convergence reports for unrouted findings.

Append new findings to the queue (in the ledger).

---

## Phase 2 — Triage (oskar)

Dispatch **oskar** to rank the queue by impact-to-cost and assign each item a route (the routing table in `oskar.md`). Oskar returns an ordered, routed work-list. High-impact/high-cost items are flagged for ingrid/principal rather than started.

---

## Phase 3 — Execute a budget-bounded slice (full authority, owning-agent rules)

Drain the routed list top-down until budget is spent. Dispatch the owning seat per route:
- card content / catalogue / near-dup / malformed-repair → **margit** (and reconcile any oskar save-as-new mutations due).
- non-persona card mutation → **oskar** writes save-as-new → margit reconciles.
- agent-`.md` / rubric / spec edit (non-persona) → **ingrid** (delegated authority).
- process / gate change → **admin** authors a process-proposal.
- a tunable agent whose tuning is **due** (new signal since last forge) → dispatch **`/and-forge <agent>`**.
- a contested item (tie, "design-inherent vs. defect", competing fixes) → **arbiter** rules.
- **persona content → admin → ESCALATE queue** (never auto-apply). Queue to the digest.

Each dispatch: confirm contracted artifacts on disk (Rule 19); read-back shared-state edits before building on them (Rule 20).

---

## Phase 3.5 — Retrospective leg (ingrid; conditional)

If a **book/series boundary** has been crossed since the last retrospective, OR the retrospective scan-class is due, dispatch **ingrid** for the book/series-close retrospective (survey four sources → improvement-verification pass → rank → route/dispatch → memo). Otherwise skip (mid-run runs don't need a full retrospective).

---

## Phase 4 — Reconcile, log, digest (mirror RUNBOOK R4)

1. **RECONCILE (Rule 21)** any hand-authored rollup before commit: citation resolution, report↔state field-equality, self-contradiction split.
2. Update `staff/ingrid/tend-state.md`: stamp `last_run` for every scan-class touched; update the carried queue (resolved items stamped, new items appended); append a run-history line.
3. Write any new parking-lot items for findings whose resolution belongs to a future command.
4. Commit the touched files (the routine commits its own maintenance work).
5. Print the single end-of-run digest:

```
================================================================
AND-TEND — <COMPLETE | DEFERRED | NO-OP> — <ts>
================================================================
Ran modules        : <hygiene / triage / forge:<agent> / retrospective / ...>
Findings           : <N total>  (BLOCKER <b> / DRIFT <d> / NIT <n>)
Fixed this run     : <N>  (trivial <t> / margit <m> / mutation <x> / agent-edit <a>)
Forge              : <agent> → <winner | no-lift | upstream>  | none
Proposals          : <N> authored (PROP-...)  | none
Arbiter rulings    : <N>  | none
ESCALATE queue     : <N> persona/irreversible items (file: <path>)  | none
Carried queue      : <N> open
Next due            : <scan-class> in <when>
Budget used        : <N>/<budget>
================================================================
```

---

## Discipline (binding)

- **R1 — no `AskUserQuestion`.** Every prompt routes to **admin** user-proxy; admin `ESCALATE` is *queued to the digest*, not prompted. (Hard human checkpoints don't arise here — `/and-tend` never touches the series-audit gate.)
- **R3 — pre-flight, then silent.** No interim narration; one digest at the end.
- **R5 — clean halts.** Defer-gate trip, budget exhaustion, an unretryable tool failure, or a parking-lot HARD item targeting `/and-tend` → write the ledger, emit the digest, exit. Never half-commit a mutation.
- **Idempotent / no-op-friendly.** Re-running within a cadence window finds nothing due and exits cheap. Safe to fire on any schedule.
- **Never contend with a live cascade.** The defer gate is absolute for state-writing modules.

---

## Scheduling (operator note)

`/and-tend` is designed to be fired by a scheduled Claude Code web trigger several times a day. The routine self-throttles via the cadence ledger, so over-scheduling is harmless (extra runs no-op). Recommended cadence config lives in `staff/ingrid/tend-state.md` and is tunable there without editing this command.

## What this routine does not do

- Author or revise the fiction (that's the chain).
- Run during a chapter cascade (defers).
- Auto-apply persona content (escalates).
- Overwrite live cards/configs (save-as-new + reconcile).
- Replace `/and-postop` / `/and-cohere` (those are opt-in quality passes on shipped chapters, not maintenance).
