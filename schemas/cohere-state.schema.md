# Cohere State Schema

Iteration state for the `/and-cohere` loop. One state file per `<book>-<range>` invocation. Tracks verdict trace across iterations, the per-iteration revise queue, dispatch results, and the final convergence outcome. Read by `/and-cohere` Phase 0 as a resume checkpoint; written/updated at every iteration boundary.

**File location.** `active-project/staff/cohere/<book>-<range>-state.md`. The `<range>` segment is the literal `<from>-<to>` chapter span (e.g. `c01-c07`) or the literal string `all` for an unconstrained-range invocation. One file per active `<book>-<range>` pair; git-tracked; append-update lifecycle.

**Lifecycle.**
1. `/and-cohere` Phase 0 scans for an existing state file matching `<book>-<range>`. If present and `status: open`, resume from the recorded `iteration_count`; if present and `status: converged | cap-hit | held | dismissed`, surface the prior outcome and either resume on `--restart` or exit (per Phase 0's resume rules in the command body).
2. `/and-cohere` Phase 1 appends a new entry to `verdict_trace[]` for the just-run `/and-review cohere` report (one entry per `/and-review cohere` execution).
3. `/and-cohere` Phase 3 writes / updates `revise_queue[]` with the chapter-grouped revise items pulled from parking-lot.
4. `/and-cohere` Phase 4 updates each `revise_queue[].executed` and `revise_queue[].result` as the re-cascade runs.
5. `/and-cohere` Phase 6 (convergence cap) or Phase 2 (PASS gate) sets `status` and `final_verdict`, stamps `closed_at`.
6. State entries stay. Periodic compaction of resolved files into `_archive/` permitted but not required; never destructive on open files.

---

## Format

```yaml
cohere_state:
  version: 1
  book: <slug>                          # e.g. b01
  range: <from>-<to> | all              # e.g. c01-c07 or all
  invocation_ts: <ISO timestamp>        # first /and-cohere invocation against this state file
  last_touched_ts: <ISO timestamp>      # most recent update
  iteration_count: <int>                # 0 on creation; incremented per /and-review cohere fire
  max_iter: <int>                       # default 3; overridable via --max-iter flag
  flags:
    strict: <bool>                      # --strict — CAUTION-COHERE also blocks
    dry_run: <bool>                     # --dry-run — Phase 3 surfaces queue but Phase 4 skips
  verdict_trace:                        # one entry per /and-review cohere execution
    - iteration: <int>                  # 0-indexed
      verdict: PASS-COHERE | CAUTION-COHERE | FAIL-COHERE
      report_path: <path>               # active-project/staff/reviews/cohere-<book>-<range>-<ts>.md
      ts: <ISO timestamp>
      failed_axes: [<axis-token>, ...]  # e.g. naive-q2, naive-q6, dramatist-promise-payoff, audience-substance
      caution_axes: [<axis-token>, ...] # axes returning CAUTION but not FAIL
      load_bearing_fails: <int>         # count of FAILs on load-bearing axes; PASS-COHERE requires 0
  revise_queue:                         # built at Phase 3 from parking-lot items the most-recent cohere run authored; rewritten per iteration
    - chapter: <slug>                   # e.g. b01c03 — the chapter the revise targets
      parking_lot_items: [<pl-id>, ...] # parking-lot ids feeding this chapter-revise
      revise_mode: --from-signals | --cohere-driven   # mode flag passed to /and-write revise
      executed: <bool>                  # set true after Phase 4 runs the revise+re-cascade for this chapter
      result: PASS | FAIL | HELD | SKIPPED  # PASS = re-cascade succeeded; FAIL = sub-phase failed; HELD = principal triage; SKIPPED = dry-run or dismissed
      result_ts: <ISO timestamp> | null
      result_note: <one line> | null    # e.g. "stitch Phase 9 FAIL — re-queue for next iteration"
  status: open | converged | cap-hit | held | dismissed
  final_verdict: PASS-COHERE | CAUTION-COHERE | CAP-HIT | HELD | null
  closed_at: <ISO timestamp> | null
  admin_process_critic:                 # populated by Phase 7.5 always-fires admin dispatch
    - iteration: <int>
      verdict: OK | OK-MERGED | OK-PRIOR-REJECTION | OK-RE-SURFACED | PROCESS-CHANGE-PROPOSED | ESCALATE
      proposal_id: <PROP-NNNN> | null
      summary: <one line>
      ts: <ISO timestamp>
```

---

## Field semantics

**`version`** — schema version. Bump on breaking changes.

**`book`** — book slug (e.g. `b01`). Matches `books[<slug>]` in showrunner memory.

**`range`** — chapter span this state covers. `<from>-<to>` form uses chapter slug suffixes (e.g. `c01-c07`); `all` covers every shipped chapter under the book at invocation time. The range is fixed at first invocation; subsequent `/and-cohere` runs on the same `<book>-<range>` resume the same state file. A different range against the same book opens a new state file.

**`iteration_count`** — number of `/and-review cohere` executions that have fired against this state. Phase 1 increments on each fire. Convergence cap fires when `iteration_count >= max_iter` without `PASS-COHERE`.

**`max_iter`** — convergence cap. Default 3. `--max-iter N` overrides; lower bound 1, no upper bound (but admin process-critic escalates if `max_iter > 5` per Rule 13 cost discipline).

**`flags.strict`** — `true` if `--strict` was passed. Under strict, `CAUTION-COHERE` blocks (Phase 2 routes to Phase 3 revise queue rather than exiting success).

**`flags.dry_run`** — `true` if `--dry-run` was passed. Phase 3 surfaces the queue but Phase 4 skips revise dispatch; state file records the queue + `executed: false` + `result: SKIPPED`.

**`verdict_trace[]`** — append-only history of `/and-review cohere` verdicts across iterations. Reading `verdict_trace[-1].verdict` gives the current verdict. `verdict_trace[-1].failed_axes` drives the Phase 3 revise queue. Compare `verdict_trace[-1]` to `verdict_trace[-2]` for the Phase 5 improvement check (FAIL→CAUTION, CAUTION→PASS, unchanged, regressed).

**`verdict_trace[].failed_axes`** — token list. Canonical tokens (cross-referenced to `/and-review cohere` Phase 1 axes):
- `naive-q1` voice/register consistency
- `naive-q2` setup→payoff (load-bearing)
- `naive-q3` calendar legibility
- `naive-q4` character-presence accumulation (load-bearing)
- `naive-q5` sensory texture distribution
- `naive-q6` apparatus-register cumulative load (load-bearing)
- `naive-q7` sub-section feel vs glued-chapters
- `naive-q8` close-of-section pleasure
- `dramatist-arc` arc legibility
- `dramatist-promise-payoff` promise/payoff inventory (load-bearing)
- `dramatist-antagonist` antagonist pressure curve
- `dramatist-scene-shape` scene-shape distribution
- `audience-substance` substance-felt rotation persona (load-bearing FLAT)
- `audience-rules` rule-coherence (cape-fic-reader / worm-canon-pedant specific)

**`verdict_trace[].load_bearing_fails`** — count of FAILs on load-bearing axes (the five named in the design plan's "What positive looks like" section). `PASS-COHERE` requires `load_bearing_fails == 0`.

**`revise_queue[]`** — rebuilt from parking-lot at each Phase 3 (not append-only across iterations; one queue per iteration). Items map 1:1 to chapter-revise dispatches. Order is dependency order — upstream chapters first.

**`revise_queue[].revise_mode`** — `--from-signals` (current canonical revise mode) is the default. `--cohere-driven` is a future revise mode pinned for `/and-write` once a cohere-aware signal cluster shape is added; until then, treat `--cohere-driven` as a synonym for `--from-signals` with the cohere-authored signals supplied as the cluster.

**`revise_queue[].result`** — outcome of the per-chapter re-cascade:
- `PASS` — `/and-write revise` → `/and-review bones` → `/and-facets` → `/and-stitch` all succeed.
- `FAIL` — any sub-phase fails; iteration enters held state.
- `HELD` — principal triage requested (e.g. orchestrator-critic NOT-SUCCESSFUL on the re-stitched chapter).
- `SKIPPED` — dry-run or principal-dismissed entry.

**`status`**:
- `open` — iteration loop in progress; resume permitted on re-invocation.
- `converged` — `PASS-COHERE` reached; `final_verdict: PASS-COHERE`; `closed_at` stamped.
- `cap-hit` — `iteration_count >= max_iter` without `PASS-COHERE`; `final_verdict: CAP-HIT`; admin process-critic escalation logged.
- `held` — a `revise_queue[].result == FAIL` or `HELD` bubbled up; principal triage required before next iteration; `final_verdict: HELD` until triaged.
- `dismissed` — principal explicit dismissal (e.g. `/and-cut` on a cohere run, or a `--dry-run` exit, or a DEFER answer at Phase 4's principal-defer check when all queue targets are finished+accepted chapters); `closed_at` stamped, `final_verdict: null`. In the defer case, `revise_queue[].result: SKIPPED` with `result_note` naming the deciding DEC.

**`final_verdict`** — set only on `status` transitions away from `open`. Distinct from `verdict_trace[-1].verdict` — `final_verdict` is the loop outcome, not the most-recent review verdict.

**`admin_process_critic[]`** — one entry per Phase 7.5 always-fires admin dispatch (Rule 13). Phase 7.5 fires at every iteration boundary (after Phase 5 verdict logging) and at convergence / cap-hit / held state transitions.

---

## Matching rules (Phase 0 resume scan)

`/and-cohere <book> [<range>]` matches an existing state file iff:
1. `state.book == <book>` (exact match).
2. `state.range == <range>` (exact match; `c01-c07` does NOT match `c01-c08` or `all`).
3. `state.status == open`.

On match:
- Resume from `iteration_count`; do not re-fire iteration 0.
- Surface the most-recent `verdict_trace[]` entry and any open `revise_queue[].result == HELD` entries before Phase 1.

On no match:
- New state file with `iteration_count: 0`, `verdict_trace: []`, `status: open`.

On `--restart` flag (forces a fresh run even if open state exists):
- Archive existing state file to `_archive/<book>-<range>-state-<closed_ts>.md`.
- Open new state file with fresh `invocation_ts`.

---

## Relationship to parking-lot

The parking-lot is the canonical surface for chapter-revise items the cohere run authors. `cohere_state.revise_queue[]` is a *view* of those items grouped by chapter — it cites `parking_lot_items[]` ids but does not duplicate item content. Parking-lot resolution stamps (`resolved_at` / `resolved_by` / `resolution_note`) are written by `/and-cohere` Phase 4 as it completes per-chapter revises; the state file's `revise_queue[].result` is the cohere-internal mirror of that resolution.

If the principal manually resolves or dismisses a parking-lot item between iterations, Phase 3 of the next iteration MUST detect that and update `revise_queue[].result` to `SKIPPED` with note `principal-resolved-out-of-band`.

---

## Authoring discipline

- **Minimum viable state file:** `version`, `book`, `range`, `invocation_ts`, `iteration_count`, `max_iter`, `flags`, `verdict_trace: []`, `revise_queue: []`, `status: open`, `final_verdict: null`.
- **One file per `<book>-<range>`.** Never split or merge state files; range identity is the keying field.
- **Append-update, not overwrite.** `verdict_trace[]` and `admin_process_critic[]` are append-only within a state file's life. `revise_queue[]` is rewritten per iteration but the prior iteration's queue is preserved in the previous `verdict_trace[]` entry's `report_path` (the cohere report carries the authored queue).
- **Closed state files are immutable.** Once `status` leaves `open`, the file is read-only. `--restart` archives and starts fresh rather than mutating in place.
