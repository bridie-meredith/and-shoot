---
description: Cross-chapter coherence iteration loop (PROP-0031). Calls /and-review cohere, dispatches the chapter-revise queue through the existing /and-write revise → /and-review bones → /and-facets → /and-stitch chain, re-runs /and-review cohere, repeats until PASS-COHERE or convergence cap. Opt-in, post-ship, principal-invoked. Not part of the default chain; does not gate per-chapter ship. Usage - /and-cohere <book> [<from>-<to>] [--strict] [--max-iter N] [--dry-run] [--restart]
---

# /and-cohere

Cross-chapter coherence iteration loop. Runs *after* a sub-section of chapters has shipped through `/and-stitch`. Calls `/and-review cohere` to surface cross-chapter holes, dispatches the chapter-revise queue through the existing chain, re-runs `/and-review cohere`, repeats until `PASS-COHERE` or convergence cap.

**Opt-in.** Not part of `/and-substance --cascade`. Not part of the default chapter loop. Principal-invoked when a sub-section is ready for a coherence pass. Designed to fit between per-chapter `/and-postop` calls and book-level `/and-review verdict`.

**Post-ship.** All chapters in the range MUST have shipped through `/and-stitch` Phase 9 (cold-read `PASS` or `PASS-WITH-DEPTH-PASS-REQUIRED`). Un-shipped chapters are out of scope — they have their own per-chapter gates.

**Not a per-chapter ship-gate.** Individual chapters retain their `/and-stitch` Phase 9 cold-read as the canonical ship gate. `/and-cohere` gates the *sub-section as a sub-section*.

You are the orchestrator. All dispatches use the Agent tool. The iteration loop is implemented in this command body; per-chapter re-cascade is delegated to existing commands (`/and-write`, `/and-review bones`, `/and-facets`, `/and-stitch`) — `/and-cohere` does not re-implement them.

Re-runnable per `design/substance/rerun-protocol.md`. State file is the resume checkpoint (see `schemas/cohere-state.schema.md`).

---

## Inputs (read-only at Phase 0; read-write across iterations)

- `active-project/staff/showrunner/memory.md` — chapter shipped-status; `chapters[<slug>].cold_read.verdict` per chapter in range
- `active-project/draft/<book>-<chapter>.md` — shipped chapters in the range
- `active-project/staff/cohere/<book>-<range>-state.md` — resume checkpoint (created if absent; updated per iteration)
- `active-project/staff/showrunner/parking-lot.md` — the chapter-revise queue lives here between iterations
- `staff/admin/decisions.md` — for principal-dismissed cohere items (Phase 3 triage drops them)

---

## Flags

- `--strict` — `CAUTION-COHERE` also blocks. Phase 2 routes CAUTION verdicts to Phase 3 revise queue rather than exiting success. Use when the sub-section is downstream-load-bearing (e.g. it is the opening of the book) and CAUTION-level concerns warrant fixing before downstream chapters build on the sub-section.
- `--max-iter N` — convergence cap override. Default 3. Lower bound 1; admin process-critic escalates if `N > 5`.
- `--dry-run` — Phase 3 surfaces the chapter-revise queue but Phase 4 skips dispatch. State file records `revise_queue[].executed: false`, `result: SKIPPED`. Useful for inspecting what the cohere run would mutate before committing the spend.
- `--restart` — force a fresh run even if open state exists. Archives existing state file to `_archive/<book>-<range>-state-<closed_ts>.md` and opens new state. Default behavior on existing open state is resume.
- `--range <from>-<to>` — alias for the positional range arg, for clarity in cascade invocations.

---

## Phase 0 — Argument resolution + resume

1. Parse `<book>` (required) and `<range>` (optional; default = `all` — every shipped chapter under the book).
2. Validate `<book>` exists in showrunner memory (`books[<slug>]`); abort if not.
3. Resolve range to a chapter list:
   - `<from>-<to>` form: enumerate `c<NN>` from `<from>` to `<to>` inclusive.
   - `all` form: all chapters under the book where `chapters[<slug>].cold_read.verdict` is `PASS` or `PASS-WITH-DEPTH-PASS-REQUIRED`.
4. **Cohere precondition.** For every chapter in the resolved range: verify `draft/<book>-<chapter>.md` exists on disk AND `chapters[<slug>].cold_read.verdict ∈ {PASS, PASS-WITH-DEPTH-PASS-REQUIRED}`. Any chapter failing either check → HARD abort with the failing chapter list (cohere is post-ship; the chapter must have shipped).
5. **State file resolution.** Check for `active-project/staff/cohere/<book>-<range>-state.md`:
   - **Present + `status: open`:** Resume. Read `iteration_count`, `verdict_trace[-1]`, `revise_queue[]`. Surface to user: "Resuming `/and-cohere <book> <range>` from iteration <N>, prior verdict <verdict>." Skip to Phase 1.
   - **Present + `status: converged | cap-hit | held | dismissed` + no `--restart`:** Surface the prior outcome and exit. Print: "Prior `/and-cohere <book> <range>` run closed at iteration <N> with verdict <verdict>. Use `--restart` to start a new run."
   - **Present + `--restart`:** Archive to `_archive/<book>-<range>-state-<prior-closed-ts>.md`. Open new state.
   - **Absent:** Create new state file per `schemas/cohere-state.schema.md` minimum viable shape. `iteration_count: 0`, `verdict_trace: []`, `revise_queue: []`, `status: open`, `final_verdict: null`. Capture flags in `flags{}`.
6. **Parking-lot scan (Rule 14).** Read `active-project/staff/showrunner/parking-lot.md`. Items matching this invocation (`target.command: /and-cohere` + `target.scope` = `<book> <range>` or `*` wildcard + `status: open`): HARD → abort unless this run resolves; SOFT → fold into the iteration log + final report. Resolving phase stamps `resolved_at` + `resolved_by` + `resolution_note`; never delete.
7. **Iteration ceiling check.** If `iteration_count >= max_iter` already at Phase 0, jump to Phase 6 (convergence cap fired in a prior session; finalize without firing another review).

---

## Phase 1 — Run `/and-review cohere`

Dispatch `/and-review cohere <book> <range>` as a sub-routine of this command. Capture the verdict by reading the persisted report at `active-project/staff/reviews/cohere-<book>-<range>-<ts>.md` after the subcommand returns.

Update state file:
- Increment `iteration_count`.
- Append to `verdict_trace[]`:
  ```yaml
  - iteration: <iteration_count - 1>   # 0-indexed
    verdict: <verdict>
    report_path: <path>
    ts: <ISO>
    failed_axes: [<token>, ...]
    caution_axes: [<token>, ...]
    load_bearing_fails: <int>
  ```
- Stamp `last_touched_ts`.

---

## Phase 2 — Gate

Read `verdict_trace[-1].verdict`:

- **`PASS-COHERE`** → Write convergence record. Set `status: converged`, `final_verdict: PASS-COHERE`, `closed_at`. Skip to Phase 7 (persist) + Phase 7.5 (admin) + Phase 8 (summary). Exit success.
- **`CAUTION-COHERE`** + `flags.strict == false` → Surface CAUTION-axes + advisory parking-lot SOFT items. Set `status: converged`, `final_verdict: CAUTION-COHERE`, `closed_at`. Skip to Phase 7 + 7.5 + 8. Exit success.
- **`CAUTION-COHERE`** + `flags.strict == true` → Promote SOFT cohere parking-lot items to HARD in-state-file (do NOT mutate parking-lot severity directly; the `--strict` promotion is a view-level decision recorded in `state.flags.strict_promoted_at: <ISO>`). Continue to Phase 3.
- **`FAIL-COHERE`** → Continue to Phase 3.

---

## Phase 3 — Triage queue

1. Read the chapter-revise queue from the most-recent `/and-review cohere` report's `chapter_revise_queue[]` front-matter field. Cross-reference each entry to its parking-lot id.
2. **Drop principal-dismissed items.** Read `staff/admin/decisions.md`. For each queue item, check whether the principal has previously dismissed the same chapter + axis pair in a DEC entry. Dropped items are logged in the iteration log under `dismissed[]`; they do not block.
3. **Group by chapter.** Coalesce queue items targeting the same chapter into one chapter-revise dispatch (one `/and-write revise` per chapter, carrying the union of signals).
4. **Order by dependency.** Earlier chapters before later chapters. Rationale: a revise in `c03` that adds a setup might payoff in `c05`; revising `c03` before `c05` keeps the `c05` re-stitch from re-running against stale upstream state. Where two chapters are independent (no shared characters / threads), preserve numeric order.
5. **Surface the ordered queue.** Print to iteration log + user:
   ```
   /and-cohere iteration <N>: FAIL-COHERE on [<failed-axes>]. Revise queue:
     <chapter-slug> ← [<parking-lot-ids>] ← [<failing-axes>]
     ...
   ```
6. Write to state file: `revise_queue[]` rebuilt for this iteration (rewriting prior iteration's queue; prior queue is preserved in the prior `verdict_trace[].report_path`).

If `flags.dry_run == true`, skip Phase 4 and proceed directly to Phase 7. State records `revise_queue[].executed: false`, `result: SKIPPED` for every entry.

---

## Phase 4 — Execute revises (re-cascade per chapter)

### Phase 4 pre-step — principal-defer check

Before dispatching any chapter revise, evaluate whether ALL chapters in the revise queue target chapters that are already verdict-PASSED + principal-accepted (i.e. the book is complete, shipped, and the surviving cohere findings concern finished drafts whose mutation would be irreversible). If so:

Route the fire-vs-defer decision to admin user-proxy per CLAUDE.md Rule 13 **before** dispatching any revise. Supply:
- the revise queue (chapter list + parking-lot ids + failing axes)
- the book's close state (shipped, verdict-PASSED, principal-accepted per DEC chain)
- the estimated cascade cost per chapter
- options: (a) FIRE — dispatch the revise queue; (b) DEFER — accept the book as cohesion-verified-with-documented-notes; findings stay in parking-lot as SOFT open items + fold into analysis

On a **DEFER** answer from admin:
- Stamp each `revise_queue[].result: SKIPPED`, `result_ts: <ISO>`, `result_note: "<deciding DEC>: principal-deferred on finished+accepted book"`
- Set `status: dismissed`, `final_verdict: null`, `closed_at: <ISO>`
- Skip Phase 4 dispatch entirely
- Record the deciding DEC in the state file comment block
- Proceed directly to Phase 7 (persist) → Phase 7.5 (admin process-critic) → Phase 8 (summary)

On a **FIRE** answer: proceed with the per-chapter dispatch loop below as normal.

This path documents the disposition taken under DEC-0108 (/and-cohere b01 all, 2026-06-06) and the schema's `revise_queue[].result: SKIPPED` + `status: dismissed` enum values already permit.

For each chapter in the ordered queue (sequential, NOT parallel — downstream chapters may depend on upstream revise output):

1. **`/and-write <chapter> revise --from-signals`** (or `--cohere-driven` once that mode lands; until then, `--from-signals` with the cohere-authored signal cluster passed as the bones-revise input).
2. **`/and-review bones <chapter>`** — mandatory gate per the existing chain. FAIL routes to `/and-write revise` re-fire (one re-fire allowed; second FAIL escalates to `result: HELD`).
3. **`/and-facets <chapter>`** — re-cascade. Phase 5b audience-gate FAIL → `result: HELD`.
4. **`/and-stitch <chapter>`** — re-cascade. Phase 9 cold-read FAIL → `result: HELD`.

Per-chapter outcome stamps to state file `revise_queue[].result`:
- All four sub-phases succeed → `result: PASS`, `result_ts`, `result_note: re-cascade complete`.
- Any sub-phase fails after one re-fire → `result: FAIL` (sub-phase named in `result_note`).
- Sub-phase escalates to principal triage → `result: HELD`.

**Parking-lot resolution.** On `result: PASS` for a chapter, stamp `resolved_at` + `resolved_by: /and-cohere Phase 4 (iteration <N>)` + `resolution_note` on each `parking_lot_items[]` entry for that chapter. Items NOT resolved stay open and will re-appear in the next iteration's Phase 3 queue.

**Failure handling.** If any `result: FAIL` or `result: HELD` lands in this iteration's queue:
- The iteration completes (other chapters may still re-cascade).
- After all queue entries execute, `status: held`, `final_verdict: HELD`, `closed_at` stamped.
- Phase 5 (re-run review) is SKIPPED — held state requires principal triage before another iteration.
- Phase 7 + 7.5 + 8 still fire (persist + admin + summary).

---

## Phase 4.5 — Revision classification (PROP-0031 Amendment 1)

Per PROP-0031 Amendment 1, every re-cascaded chapter's draft delta is classified per-hunk into `cosmetic` / `presentation-reinforcement` / `substantive`. The classification feeds Phase 6.5 aggregate-emit (presentation-reinforcement entries land in `revision_layer[]` auto-acknowledged; substantive entries land with `acknowledged: false` and surface to Phase 8) and gives the iteration log a content-typed view of what the cohere loop actually moved on draft.

**Non-blocking.** Substantive classification does NOT halt the iteration. It is recorded for downstream (Phase 6.5 + Phase 8) consumption.

**Fires only on chapters with `revise_queue[].result: PASS` in this iteration.** HELD / FAIL chapters do not emit a post-revise draft worth diffing.

**Snapshot mechanism.** At the START of Phase 4 (before any chapter dispatches), this command takes an in-iteration snapshot of `active-project/draft/<book>-<chapter>.md` for every chapter in the revise queue and writes them to `active-project/staff/cohere/<book>-<range>-<invocation-ts>/snapshots/iter-<N>/<book>-<chapter>.pre.md`. Phase 4.5 diffs the post-revise on-disk draft against this snapshot (`diff -u`). Rationale: in-iteration snapshots are deterministic and do not depend on git-commit cadence; a session that hasn't committed mid-iteration still gets a valid diff base.

For each chapter with `result: PASS` in this iteration:

1. **Compute the diff.** `diff -u <snapshot-path> active-project/draft/<book>-<chapter>.md`. Empty diff (no draft change despite re-cascade) is recorded with `hunks: []` and skipped to next chapter.
2. **Dispatch the classifier fork.** One dispatch per chapter (haiku-class model preferred for cost):
   - `subagent_type: claude` (or the chain's existing classifier-fork agent if available)
   - prompt carries:
     - The unified diff content.
     - The three class definitions verbatim:
       - `cosmetic`: sentence-rhythm, paragraph joins, redundancy cuts. No substance change.
       - `presentation-reinforcement`: character callbacks, sensory anchors, calendar anchors, plant-establishing prose. Reader-facing but no new axis-movement, no new declared events.
       - `substantive`: new events, new axis-movement, new opposing-force resolution, new character introduction, declared-fact reframe.
     - JSON-output schema:
       ```json
       {
         "chapter": "<slug>",
         "hunks": [
           {
             "hunk_id": <int>,
             "summary": "<one-line description>",
             "class": "cosmetic | presentation-reinforcement | substantive",
             "file_location": "<path:line-range>"
           }
         ]
       }
       ```
3. **Append to iteration log.** Same log file Phase 7 writes (`active-project/staff/cohere/<book>-<range>-<invocation-ts>/iteration-log.md`). Append the block (one block per iteration; per_chapter[] aggregated across all classified chapters in the iteration):

   ```yaml
   revision_classification:
     iteration: <int>
     classified_at: <ISO timestamp>
     per_chapter:
       - chapter: <slug>
         hunks:
           - hunk_id: <int>
             summary: <one-line description>
             class: cosmetic | presentation-reinforcement | substantive
             file_location: <path:line-range>
   ```

4. **State file stamp.** Update `state.iterations[<N>].classification_complete_at: <ISO>` (extending the in-state-file iteration trace; if the schema does not name this field, add it as a `# Phase 4.5 stamped <ISO>` comment line beneath the iteration's `verdict_trace[]` entry).

Substantive hunks are gathered into Phase 8's final summary AND into Phase 6.5's aggregate-emit dispatch payload (where they become `revision_layer[]` entries with `acknowledged: false`).

---

## Phase 5 — Re-run `/and-review cohere`

Only fires if Phase 4 completed with all `result: PASS`.

Dispatch `/and-review cohere <book> <range>` again. Capture the new verdict; append to `verdict_trace[]` (same shape as Phase 1).

**Improvement check.**
- `verdict_trace[-2].verdict` → `verdict_trace[-1].verdict`:
  - `FAIL-COHERE` → `CAUTION-COHERE` or `PASS-COHERE`: improved. Continue loop.
  - `FAIL-COHERE` → `FAIL-COHERE` with reduced `load_bearing_fails`: partial improvement. Continue loop.
  - `FAIL-COHERE` → `FAIL-COHERE` with same or more `load_bearing_fails`: **not converging.** Admin process-critic fires with `trigger.reason: cohere-iteration-not-converging`. Loop continues toward cap (admin's call is advisory, not a stop).
  - `CAUTION-COHERE` → `CAUTION-COHERE` (under `--strict`): partial; continue.

**Loop continuation.** If `iteration_count < max_iter` AND `verdict_trace[-1].verdict != PASS-COHERE` (and not CAUTION-COHERE-non-strict, which already exited at Phase 2), loop back to Phase 2.

---

## Phase 6 — Convergence cap

Fires when `iteration_count >= max_iter` without `PASS-COHERE`.

- Set `status: cap-hit`, `final_verdict: CAP-HIT`, `closed_at` stamped.
- Surface unresolved revise queue + accumulated `verdict_trace[]` to user + iteration log.
- Admin process-critic fires with `trigger.reason: cohere-cap-hit` (in addition to the always-fires Phase 7.5 dispatch — cap-hit is a strong signal that the cohere loop's design or the upstream chain needs change).
- Exit to principal triage. No infinite loop. The unresolved revise items stay in parking-lot as `status: open` for the principal to inspect, dismiss, or re-queue under a new `/and-cohere --restart`.

---

## Phase 6.5 — Aggregate emit (PROP-0031 Amendment 1)

Per PROP-0031 Amendment 1, on cohere convergence to PASS-COHERE this command walks the converged stretch end-to-end and writes/updates `active-project/staff/showrunner/aggregate-state.md` — the forward-feed channel that closes the upstream/draft divergence the polish-deferred chain creates. See `schemas/aggregate-state.schema.md`.

**Fires only at PASS-COHERE.** Specifically: `verdict_trace[-1].verdict == PASS-COHERE` AND `status: converged`. Skipped on `CAUTION-COHERE` (even under `--strict`, since `--strict` routes CAUTION to Phase 3 rather than treating it as convergence), `FAIL-COHERE`, `CAP-HIT`, `HELD`.

**Schema authority.** READ `schemas/aggregate-state.schema.md` before authoring this phase's dispatch. The dispatched agent must follow that schema exactly.

1. **Resolve existing state.** Check for `active-project/staff/showrunner/aggregate-state.md`:
   - **Present:** read into the dispatch payload as `existing_aggregate_state`. Agent updates in place (advances `through_chapter`, appends/replaces axis_state / open_hooks / characters / world_state / revision_layer entries per schema § Conflict resolution rules — cohere overrides stitch-Phase-10 on per-entry conflict, conflict logged in `conflict_log[]`).
   - **Absent:** agent creates the initial file. `version: 1`, `through_book: <book>`, `through_chapter: <highest-chapter-in-stretch>`, schema-minimum-viable shape.

2. **Gather inputs for the dispatch payload.**
   - The schema path: `schemas/aggregate-state.schema.md`.
   - Existing `aggregate-state.md` content if present.
   - The final on-disk draft for every chapter in the converged stretch: `active-project/draft/<book>-<chapter>.md` for each `<chapter>` in `<from>-<to>`.
   - The Phase 4.5 classification output for THIS run (all iterations' `revision_classification` blocks from the iteration log). `presentation-reinforcement`-class hunks become `revision_layer[]` entries with `class: presentation-reinforcement`, `acknowledged: true` (auto). `substantive`-class hunks become `revision_layer[]` entries with `class: substantive`, `acknowledged: false`.
   - The current `series.substance.state_axes[]` block from `active-project/staff/showrunner/memory.md` (for `axis_state[]` population — every entry maps to one declared axis).

3. **Dispatch.** Single agent call:
   - `subagent_type: claude`
   - prompt carries:
     - `mode: aggregate-emit`
     - `trigger: and-cohere Phase 6.5 PASS-COHERE convergence`
     - `book: <book>`
     - `range: <from>-<to>`
     - `schema_path: schemas/aggregate-state.schema.md`
     - `existing_aggregate_state: <content or null>`
     - `chapter_drafts: { <chapter-slug>: <draft-content>, ... }`
     - `revision_classification: <Phase 4.5 aggregated blocks for this run>`
     - `state_axes: <series.substance.state_axes[] content>`
     - instruction: read the schema, then either create the initial file (absent case) or update in place (present case), following the schema's conflict resolution rules. Tag every new or updated entry with `last_updated_by: and-cohere`. Return the full updated file content.

4. **Write the file.** Persist the agent's return to `active-project/staff/showrunner/aggregate-state.md`. Stamp `last_updated: <ISO>`, `last_updated_by: and-cohere`.

5. **Update cohere state.** Stamp `cohere_state.aggregate_emit_at: <ISO>` (if the cohere-state schema does not declare this field, append `# Phase 6.5 stamped <ISO>` as a comment line to the end of the state file's `cohere_state:` block; do not block on schema absence).

6. **Surface substantive entries.** Any `revision_layer[]` entry with `class: substantive` + `acknowledged: false` written in this phase is collected for Phase 8's final summary under an `Unacknowledged substantive revision-layer entries:` section. Per schema validation rule 7, these will HARD-block the next `/and-substance chapter` Phase 0 until the principal stamps `acknowledged: true`.

---

## Phase 7 — Persist

1. **State file.** Final write to `active-project/staff/cohere/<book>-<range>-state.md`. All fields current per `schemas/cohere-state.schema.md`.
2. **Iteration log.** `active-project/staff/cohere/<book>-<range>-<invocation-ts>/iteration-log.md` — append-only per-iteration narrative log. One section per iteration:
   ```
   ## Iteration <N> — <verdict> — <ts>
   
   Review report: <path>
   Failed axes: [<tokens>]
   Revise queue (this iteration):
     <chapter> ← [<axes>] ← <result>
   Notes:
     <free-prose narrative — what changed, what didn't>
   ```
3. **Chapter-level memory record.** For every chapter that re-cascaded with `result: PASS`, append to `chapters[<slug>].cohere_iterations` in showrunner memory (schema field pending PROP-0031 triage; until then, persist to the iteration log).
4. **Parking-lot.** Resolution stamps from Phase 4 are already written; verify and surface the resolution-count to user.

---

## Phase 7.5 — Admin process-critic dispatch (URI-ADMIN-PROCESS-CRITIC, 2026-05-25; ALWAYS fires)

Per Rule 13, admin process-critic fires on every `/and-cohere` exit — converged, cap-hit, or held. The trigger reason varies but the dispatch is mandatory.

Dispatch:
- `subagent_type: admin`
- prompt carries:
  - `mode: process-critic`
  - `trigger.reason: cohere` (refine by status: `cohere-converged-pass`, `cohere-converged-caution`, `cohere-cap-hit`, `cohere-held`)
  - `trigger.source_report: <path to most recent /and-review cohere report>`
  - `trigger.source_verdict: <verdict + load_bearing_fails count + iteration_count>`
  - `gate_path: .claude/commands/and-cohere.md#phase-2` (the gate that produced the exit)
  - `secondary_gate_paths: [.claude/commands/and-review.md#cohere, .claude/commands/and-write.md#phase-6, .claude/commands/and-stitch.md#phase-9]` (upstream gates implicated by the failure axes — naive Q4 / dramatist promise-payoff implicate `/and-write` Phase 6; naive Q6 implicates `/and-stitch` Phase 9 PROP-0022 readability axis)

Non-blocking — Phase 8 summary proceeds. Admin's return logged under `cohere_state.admin_process_critic[]` (per `schemas/cohere-state.schema.md`). New proposals land in `staff/admin/process-proposals.md`. See CLAUDE.md Rules §13 and `schemas/admin-proposal.schema.md`.

---

## Phase 8 — Summary

Print to user:

```
/and-cohere <book> <range>: <final_verdict>

  Iterations: <count> / <max_iter>
  Verdict trace: <i0:verdict> → <i1:verdict> → ... → <iN:verdict>
  Final load-bearing fails: <count>
  Final failed axes: [<tokens>]
  
  Re-cascaded chapters: <count>
    <chapter>: <result>
    ...
  
  Unresolved revise queue: <count items>
    <chapter> ← [<axes>] — parking-lot id <pl-id>
    ...
  
  Reports:
    State: active-project/staff/cohere/<book>-<range>-state.md
    Iteration log: active-project/staff/cohere/<book>-<range>-<ts>/iteration-log.md
    Most recent review: <path>
  
  Admin process-critic: <verdict> (<proposal_id if any>)
  
[On status: converged + PASS-COHERE]
  Next: optional /and-review verdict <book>; otherwise the sub-section is sub-section-clean.
[On status: converged + CAUTION-COHERE]
  Next: CAUTION-axes surfaced as SOFT parking-lot items. Consider --strict re-run if the axes warrant.
[On status: cap-hit]
  Next: principal triage. Inspect unresolved queue; decide between --restart with revised max-iter, dismiss specific items, or escalate to upstream command-body / rubric revision per admin's proposal.
[On status: held]
  Next: principal triage of held sub-phase. Resolve the failure cause (cold-read FAIL, audience-gate FAIL, etc.) then --restart.
```

---

## What this command does not do

- Does not re-implement the per-chapter chain. `/and-write`, `/and-review bones`, `/and-facets`, `/and-stitch` are dispatched as-is.
- Does not gate per-chapter ship. Chapters ship through `/and-stitch` Phase 9 independent of `/and-cohere`.
- Does not run on un-shipped chapters. Phase 0 HARD-aborts if any chapter in range lacks a shipped `draft/<book>-<chapter>.md` with cold-read PASS / PASS-WITH-DEPTH-PASS-REQUIRED.
- Does not author parking-lot items itself. Phase 3 reads the queue authored by `/and-review cohere` Phase 3.
- Does not mutate showrunner memory's `cold_read` / `postop` / `bones_review` records. Those belong to their authoring commands.
- Does not run cross-book (range is always within one book). Cross-book coherence is a follow-on (PROP candidate, not in scope).

---

## Relationship to existing commands

- **`/and-stitch` Phase 9** — per-chapter ship gate. Runs at ship time. Independent of `/and-cohere`.
- **`/and-postop`** — per-chapter depth-of-quality review. Post-ship, per-chapter. Compositional sibling to `/and-cohere` (per-sub-section depth-of-quality).
- **`/and-review verdict <book>`** — book-level orchestrator-critic. Runs *after* `/and-cohere` has converged (or after principal decision to ship the sub-section as-is). Reads the most-recent `cohere-<book>-*` report as supplementary input when present.
- **`/and-substance --cascade`** — does NOT auto-call `/and-cohere`. Cohere is opt-in.
- **`/and-cut` mid-cohere** — supported. `/and-cut` writes a checkpoint and the state file's `status` becomes `dismissed` until the principal `--restart`s.

---

## Cost shape

Per `subsection-coherence-process-plan-2026-05-31.md` § Cost shape:
- One `/and-review cohere` run: ~5 dispatches (3 forks + admin + aggregation).
- One `/and-cohere` iteration: cohere run (5) + per-chapter re-cascade (~12 each: write revise + bones review + facets fanout/fanin + stitch).
- Worst case (3-chapter revise, cap-hit at 3 iterations): ~5 + 36 = 41 per iteration × 3 = ~123 dispatches.
- Realistic case: 1 or 2 iterations to PASS-COHERE; ~50-80 dispatches.
- Comparable to `/and-substance --cascade` across the same range. Opt-in, not default.

---

## Lift basis

Net-new under PROP-0030 + PROP-0031 (designed 2026-05-31 in `active-project/staff/showrunner/subsection-coherence-process-plan-2026-05-31.md`). Derives from the b01c05 three-FAIL postmortem and the c01-c07 sub-section audit that surfaced cross-chapter coherence gaps no per-chapter gate caught.
