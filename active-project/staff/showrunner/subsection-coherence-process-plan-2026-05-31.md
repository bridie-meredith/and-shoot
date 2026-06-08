# Sub-section coherence process — design plan

Session: 2026-05-31. Branch: `session/audit-and-stitch-2026-05-31`.
Pairs with: PROP-0030 (`/and-review cohere` primitive) and PROP-0031
(`/and-cohere` iteration loop).

This plan specifies the new pipeline stage the principal directed:

> "Draft process that will stitch chapters together, identify and plug
> holes in narrative, and then ensure readability is high. Cold reads
> must pass with positive content. If not, iterate in fixing the material
> until all reviews are positive."

---

## Where this fits in the chain

```
   per-chapter loop (unchanged):
     /and-substance chapter → /and-write → /and-review bones
                            → /and-facets → /and-stitch
                            → optional /and-postop

   NEW sub-section loop (after N chapters ship):
     /and-cohere <book> [range]
       ├── Phase 1: /and-review cohere — cold-read primitive
       ├── Phase 2: triage chapter-revise queue
       ├── Phase 3: dispatch /and-write revise per chapter (re-cascade)
       ├── Phase 4: re-run /and-review cohere
       └── loop until PASS-COHERE or convergence cap
```

`/and-cohere` is *post-ship* and *opt-in*. It does not gate
chapter-ship. Individual chapters continue to ship through
`/and-stitch` Phase 9 cold-read. The cohere process runs against
the *combined* sub-section and is responsible for cross-chapter
quality only.

---

## Two-command shape

The process splits into two artifacts because /and-review is read-only
by design and the iteration loop is read-then-mutate:

1. **`/and-review cohere`** (PROP-0030) — single-pass cold-read of N
   chapters as a continuous stretch. Surfaces holes. Writes
   chapter-revise queue to parking-lot. Does not edit anything.
2. **`/and-cohere`** (PROP-0031) — iteration loop. Calls
   `/and-review cohere`, dispatches the revise queue through the
   existing chain, re-runs `/and-review cohere`, repeats until
   PASS-COHERE or cap.

The split lets the principal run `/and-review cohere` standalone
(diagnostic, no mutation) without committing to the full loop.

---

## /and-review cohere — phases

**Phase 0: validate + parking-lot scan + concatenate.**
- Args: `<book> [<from>-<to>]`. Default range = all shipped chapters.
- Read showrunner memory; confirm range chapters are shipped to
  `active-project/draft/`.
- Read parking-lot; surface any open cohere-targeted items.
- Concatenate `draft/<book>-c<XX>.md` files into
  `active-project/staff/reviews/cohere-<book>-<range>-<ts>.combined.md`
  with chapter divider markers.
- Compute combined word-count + chapter-count for the report header.

**Phase 1: cold-read fanout (3 forks).**

Dispatch in parallel:

- **Fork A — naive cold-reader.** Impersonator-loaded naive-reader
  persona (same persona as `/and-postop` Phase 1). System context:
  "You are reading this as a single continuous sub-section of a
  book. Do not bring outside context. Respond to the prose."
  Prompts target cross-chapter axes:
  - Q1 voice/register consistency across the stretch.
  - Q2 setup→payoff: which beats land, which drop. Itemize.
  - Q3 calendar/time legibility.
  - Q4 character-presence accumulation: who arrives cold, who is
    felt as carried.
  - Q5 sensory texture distribution: where prose embeds vs lists.
  - Q6 apparatus-register cumulative load. (Load-bearing question.)
  - Q7 "does this feel like a sub-section of a book or seven shipped
    chapters with prologue glue?"
  - Q8 close-of-section pleasure: do I want the next chapter?

  Verdict per question: `PASS` / `CAUTION` / `FAIL` + one-paragraph
  evidence excerpt + line reference. Forks return a YAML report.

- **Fork B — dramatist axis.** Same combined file. Structural-shape
  review across the window:
  - Arc legibility (does the trajectory move?).
  - Promise/payoff inventory (every promise → payoff or hold).
  - Antagonist pressure curve (sustained or fragmented).
  - Scene-shape distribution (action/argument/interior balance).

  Verdict per axis: `ACCEPT` / `CAUTION` / `REVISE` + evidence.

- **Fork C — audience persona rotation.** One of three project
  audience personas (round-robin tracked in
  `active-project/audience/<slug>/cohere-history.md`). Reviews with
  substance-felt axes extended to multi-chapter (cross-chapter
  substance accumulation).

  Verdict: `SUBSTANCE-FELT` / `SUBSTANCE-PARTIAL` / `SUBSTANCE-FLAT`
  + per-axis call.

**Phase 2: aggregate.** Merge verdicts into a single verdict shape:

- `PASS-COHERE` — all three forks PASS on load-bearing axes.
  No chapter revises required.
- `CAUTION-COHERE` — at least one CAUTION on any axis; advisory
  parking-lot entries written; sub-section ships.
- `FAIL-COHERE` — at least one FAIL on a load-bearing axis. Routes
  to revise queue.

Load-bearing axes (FAIL on these is blocking):
- Naive Q2 (setup→payoff drop on a structural beat).
- Naive Q4 (character arrives cold at a load-bearing moment).
- Naive Q6 (apparatus-register exceeds sustainable density).
- Dramatist promise/payoff inventory (a promise is dropped).
- Audience substance-felt (FLAT verdict).

Non-load-bearing axes (FAIL surfaces but does not block):
- Naive Q3 (calendar drift — annoying, not catastrophic).
- Naive Q5 (sensory thinness — annoying, not catastrophic).
- Dramatist scene-shape distribution.

**Phase 3: write chapter-revise queue.** For each FAIL on a
load-bearing axis, author a parking-lot item:
- `target.command: /and-write`
- `target.scope: <chapter-slug>` (the chapter the revise targets)
- `severity: HARD` if FAIL-COHERE; `SOFT` if CAUTION-COHERE
- `description`: cite the failing question/axis + the proposed
  bone-level fix (item-shape mirrors the `narrative-improvement-plan`
  per-item specs).

**Phase 4: persist.**
- `active-project/staff/reviews/cohere-<book>-<range>-<ts>.md` — the
  full verdict + evidence + chapter-revise queue.
- `chapters[<slug>].cohere_review = { verdict, report_path, ts }` per
  chapter in the range.
- Parking-lot append (the revise items).

**Phase 5: admin process-critic** (always-fires, per Rule 13 pattern).

**Phase 6: summary.**

**Gates:**
- `FAIL-COHERE` is NOT a ship-gate on individual chapters (they
  already shipped). It IS a gate on shipping the sub-section as a
  sub-section.
- `CAUTION-COHERE` never blocks.

---

## /and-cohere — phases (iteration loop)

**Phase 0: validate + resume.**
- Args: `<book> [range] [--strict] [--max-iter N] [--dry-run]`.
- If a prior `/and-cohere` iteration is open on the same range, resume
  from its checkpoint (state file:
  `active-project/staff/cohere/<book>-<range>-state.md`).
- Initialize iteration counter (0 if new).

**Phase 1: run `/and-review cohere`.** Capture verdict.

**Phase 2: gate.**
- `PASS-COHERE` → write convergence record; exit success.
- `CAUTION-COHERE` → exit success (unless `--strict`).
- `FAIL-COHERE` → Phase 3.

**Phase 3: triage queue.**
- Read the chapter-revise queue from parking-lot (Phase 3 of cohere).
- Group by chapter; order by dependency (revise upstream chapters
  before downstream consumers).
- Drop items the principal has previously dismissed (read
  `staff/admin/decisions.md`).
- Surface the ordered queue in the iteration log.

**Phase 4: execute revises.** For each chapter:
- `/and-write <chapter> revise` (mode flag: `--cohere-driven` if a
  cohere-revise mode is added; otherwise `--from-signals` with the
  cohere-authored signal cluster).
- `/and-review bones <chapter>` (mandatory gate per existing chain).
- `/and-facets <chapter>` (re-cascade).
- `/and-stitch <chapter>` (re-cascade; terminal gate).

Failures at any sub-phase bubble up; iteration enters held state;
principal triage required.

**Phase 5: re-run `/and-review cohere`.**
- Compare verdict to prior iteration.
- If improved (FAIL→CAUTION, CAUTION→PASS) → continue loop.
- If unchanged or regressed → admin process-critic fires
  (`trigger.reason: cohere-iteration-not-converging`); loop continues
  toward cap.

**Phase 6: convergence cap (default 3 iterations).**
- On cap-hit without `PASS-COHERE`:
  - Write final verdict `CAP-HIT` (advisory).
  - Surface unresolved revise queue.
  - admin process-critic fires.
  - Exit to principal triage. No infinite loop.

**Phase 7: persist.**
- `active-project/staff/cohere/<book>-<range>-<ts>/iteration-log.md`
- `chapters[<slug>].cohere_iterations` per touched chapter
- Parking-lot resolutions for plugged items

**Phase 7.5: admin process-critic** (always-fires).

**Phase 8: summary.**

---

## State file format

`active-project/staff/cohere/<book>-<range>-state.md`:

```yaml
cohere_state:
  book: <slug>
  range: <from>-<to>
  invocation_ts: <ISO>
  iteration_count: <int>
  verdict_trace:
    - iteration: 0
      verdict: <PASS-COHERE | CAUTION-COHERE | FAIL-COHERE>
      report_path: <path>
      failed_axes: [<axis>, ...]
    - iteration: 1
      ...
  revise_queue:
    - chapter: <slug>
      items: [<pl-id>, ...]
      executed: <bool>
      result: <PASS | FAIL | HELD>
  status: <open | converged | cap-hit | held>
  final_verdict: <set on converged or cap-hit>
```

State file is append-update; readable as resume checkpoint by any
re-invocation of `/and-cohere` on the same `<book>-<range>`.

---

## What positive looks like

`PASS-COHERE` requires:
- Naive Q1 (voice consistency) PASS or CAUTION
- Naive Q2 (setup→payoff) PASS (no FAIL allowed on load-bearing beats)
- Naive Q4 (character-presence) PASS (no cold walk-ons on load-bearing
  characters)
- Naive Q6 (apparatus-register) PASS (cumulative load sustainable)
- Naive Q8 (close-of-section pleasure) PASS or CAUTION
- Dramatist promise/payoff inventory: every promise paid, held, or
  explicitly deferred
- Audience substance: FELT or PARTIAL (FLAT is blocking)

Calendar drift (Q3), sensory thinness (Q5), scene-shape distribution
are CAUTION-permitted at PASS-COHERE.

---

## Cost shape

- `/and-review cohere` single run: ~5 dispatches (naive + dramatist +
  one audience + aggregate + admin). ~10 minutes wall-clock.
- `/and-cohere` per iteration: cohere run (~5) + per-chapter re-cascade
  (~12 per chapter: write revise, bones review, facets fanout/fanin,
  stitch). Worst case for 3-chapter revise: ~5 + 36 = 41 dispatches.
- Cap = 3 iterations → worst-case ~123 dispatches across all chapters.
- Realistic case: 1 iteration converges or 2 iterations to PASS.

Comparable to `/and-substance --cascade` cost across the same chapter
range. Not free; appropriate as opt-in, not in default flow.

---

## Interaction with existing pipeline

- **Per-chapter ship gate** stays at `/and-stitch` Phase 9. Chapters
  ship without `/and-cohere`.
- **`/and-postop`** continues to be the per-chapter depth-of-quality
  review. `/and-cohere` is the per-sub-section equivalent. Both
  optional; both post-ship; do not block each other.
- **PROP-0023** (false-ALIVE bone-level catch) is upstream of
  `/and-cohere` and reduces its load by catching apparatus-dominant
  chapters before they ship.
- **PROP-0024** (argument-spine bone-authoring) is upstream and reduces
  argument-chapter cold walk-on probability.
- **`/and-substance --cascade`** does NOT auto-call `/and-cohere`.
  Cohere is principal-invoked or on-demand.

---

## Fork B scope

Fork B in this session does:

1. Author the command body at `.claude/commands/and-cohere.md` (full
   prose; ready to execute on accept).
2. Author the command body at `.claude/commands/and-review-cohere.md`
   (or extend `.claude/commands/and-review.md` subcommand router) for
   the cohere subcommand.
3. Author the state-file schema at
   `schemas/cohere-state.schema.md`.
4. Run the new process against the current shipped c01-c07 stretch
   end-to-end (first iteration only — does NOT re-cascade chapters
   in Fork B; instead surfaces the revise queue, which Fork A consumes).
5. Document the output: the cohere verdict, the revise queue, the
   handoff to Fork A.

**Out of scope for Fork B:**
- Schema-level memory.md changes (`chapters[<slug>].cohere_review`,
  `chapters[<slug>].cohere_iterations`) — defer to principal triage of
  PROP-0030 / PROP-0031.
- Iterating against Fork A's revised output (Fork A and Fork B run in
  parallel on separate worktrees; convergence is a follow-on session).
- Live process-proposal acceptance — Fork B builds the machinery as if
  PROP-0030 / PROP-0031 were accepted; principal triages after the run.

---

## Convergence (this session)

After Fork A and Fork B both return:
- Fork A: revised chapter drafts on its worktree.
- Fork B: new command body + first-iteration cohere report + revise
  queue on its worktree.
- Principal review: merge Fork A's revises into main; review Fork B's
  command bodies + report; decide on PROP-0030 / PROP-0031 triage.
- Follow-on session: re-run `/and-cohere` against Fork A's revised
  drafts to verify convergence to PASS-COHERE (or the next iteration).
