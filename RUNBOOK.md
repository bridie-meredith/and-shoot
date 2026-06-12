# and-shoot RUNBOOK

**For Claude, at session start.** When the user says "write" / "continue" / "what's next" / "next chapter" / "produce c<MM>" / "do chapter X" / anything implying forward motion through the pipeline — DO NOT ask them what to do. Run this protocol.

The most common operation in this project is **producing a chapter end-to-end**. That operation has its own protocol below ("Producing a chapter — end-to-end protocol"). When the trigger map points there, follow it exactly.

---

## 60-second orientation

Read these in order; stop when you have enough state to act:

1. `active-project/staff/showrunner/memory.md` — single source of truth for project state. The `## State` block names the current chapter, the last completed phase, and any blocking conditions.
2. `active-project/staff/showrunner/parking-lot.md` — open HARD items that must resolve at named phases. Surface them; HARD items at the current phase abort.
3. `active-project/staff/showrunner/aggregate-state.md` — if present, the rolling forward-feed state through the most recently threaded chapter. Check for unacknowledged substantive revision-layer entries (these block the next chapter's `/and-substance chapter` Phase 0).
4. `git log --oneline -10` — what shipped recently. Confirms memory.md isn't stale.
5. `ls active-project/draft/` — what chapters are actually on disk.

If `active-project/` is empty: no project active. Tell the user and ask whether to activate a new one (`/and-project`) or restore a shelved one from `projects/`.

**Book-complete check (do this before treating any forward-motion trigger as "produce a chapter").** If memory.md shows the active book is **complete** — every planned chapter shipped AND the last chapter is series-terminal (e.g. `b01c20` carries `SERIES-TERMINAL`) AND `/and-review verdict b<NN>` has issued (PASS / PASS-WITH-NOTES) — then there is **no next chapter**. "Write" / "continue" / "next" do NOT mean chapter-production. Route to **Producing revisions — book-complete protocol** below, or print the post-completion menu (revise · archive to `projects/` · extend to b<NN+1> · new project). Do not engage the chapter-production protocol against a nonexistent chapter.

---

## Pipeline state machine

```
/and-project (one-time)
  └─> /and-series
        └─> /and-substance series  →  /and-cast  →  series-audit (HUMAN CHECKPOINT)
                                                          │
                                                          ▼
              /and-substance book b<NN>
                    │
                    ▼
              loop per chapter b<NN>c<MM>:
                /and-substance chapter b<NN>c<MM>     ← Phase 0 reads aggregate-state.md
                  └─> /and-write b<NN>c<MM>
                        └─> /and-review bones b<NN>c<MM>     (MANDATORY gate)
                              └─> /and-facets b<NN>c<MM>
                                    └─> /and-stitch b<NN>c<MM>
                                          ├─ Phase 9 cold-read terminal gate
                                          └─ Phase 10 FORWARD-THREAD     ← reads past, edits current, updates aggregate-state.md
                                                └─> [optional] /and-postop b<NN>c<MM>

  [periodic, opt-in]  /and-cohere b<NN> [<from>-<to>]   ← cross-chapter coherence loop;
                                                          PASS-COHERE updates aggregate-state.md
```

`/and-substance --cascade` chains chapter → write → bones-review → facets → stitch (including Phase 10) automatically. **Producing a chapter follows the protocol below, which uses `--cascade` as its backbone and adds discipline rules so the operator (Claude) does not bail mid-run.**

---

## Trigger → action map

| User says | Do this |
|---|---|
| "produce c<MM>" / "do chapter X" / "write the next chapter" / "walk away while you do c<MM>" / any phrasing meaning "give me a finished chapter" | **Engage the chapter-production protocol below.** This is the canonical operation. |
| "write" / "continue" / "next" / "go" | Read memory.md. **First run the book-complete check (above).** If the book is complete: there is no next chapter — print the post-completion menu or, if revisions are in progress, resume the revisions protocol. Otherwise: if a chapter is mid-chain (some phases done, some not), resume from the next phase; if the most recent chapter shipped through Phase 10, engage chapter-production for the next chapter. |
| "revise" / "begin revisions" / "fix the book" / "revise c<MM>" | **Engage the revisions protocol below.** Works on a complete (or any shipped) book — picks revision scope from the cohere/parking-lot queue + postop + your direction, then re-cascades the affected chapters. |
| "consolidate" / "single file" / "assemble the manuscript" | Build/refresh `active-project/draft/b<NN>-manuscript.md` (concatenated chapter drafts with dividers). The revision read-surface. |
| "finalize the book" / "export for Google Docs" / "package the completed work" / "close out the project" | **Engage the finalize & export protocol** (`design/finalize-export-protocol.md`). Cold-read forks → editor trim pass on an export copy → assemble one reader-facing file → save to `completed-works/<slug>/` → archive `active-project/` to `projects/` → harvest new personas/cards (margit). Book-close operation; does NOT re-cascade the bones chain. |
| "ship it" / "stitch" | If facets are done: `/and-stitch <slug>` (will include Phase 10). Else: figure out what's missing and route there. |
| "review the chapter" | `/and-review verdict b<NN>` (book-level) or `/and-postop b<NN>c<MM>` (chapter-level depth-of-quality). |
| "cohere" / "check the stretch" / "is the book hanging together" | `/and-cohere b<NN> [<from>-<to>]`. Opt-in cross-chapter loop. |
| "what's next" / "where are we" | Just print the state summary. Don't act. |
| "fix this" / "this is wrong" | Read the user's specific concern. Don't just rerun a phase blindly. |

---

## Producing a chapter — end-to-end protocol

When the user asks for a chapter, this is the operation. It is silent, disciplined, and produces one finished chapter (or one clean halt with a checkpoint). The principal walks away and reads the end-of-run summary when it lands.

### The five rules (binding for the whole run)

**R1 — No `AskUserQuestion`. Ever.** Every prompt that the chain would have routed to the principal is dispatched to admin in user-proxy mode per CLAUDE.md Rule 13. Admin's response is honored without second-guessing. Admin `ESCALATE` returns are queued to the end-of-run summary, NOT prompted mid-run.

**R2 — Drive through cap-bounded gate FAILs.** The chain has three retry-capped gates. On FAIL, auto-iterate within cap before halting:

| Gate | Auto-action on FAIL | Cap |
|------|---------------------|-----|
| `/and-review bones` FOLLOW-FAIL or fidelity-FAIL | `/and-write <slug> revise` + re-run `/and-review bones` | 1 retry |
| `/and-facets` Phase 4 mechanical auditor HARD | fixer + re-audit (internal; no principal prompt) | 2 passes (internal) |
| `/and-stitch` Phase 9 cold-read FAIL | `/and-write <slug> revise --from-signals` + re-run `/and-facets` + `/and-stitch` | 1 retry |

(The `/and-facets` Phase 5b adversarial audience-gate cycle is RETIRED under DEC-0116. The facet layer's gate is now the Phase 4 mechanical auditor, which self-remediates ≤2 passes internally; HARD-persist past that surfaces as a NOT-SUCCESSFUL Phase 5 verdict and halts per R5, not a principal-facing cycle loop.)

Cap exhaustion → HALT cleanly with checkpoint.

`/and-stitch` Phase 10 HOLD-THREAD does NOT halt this chapter (chapter is already shipped per Phase 9 PASS); it surfaces substantive revision-layer entries that gate the NEXT chapter's Phase 0. End-of-run summary flags it; principal acknowledges before the next chapter-production run.

**R3 — Pre-flight, then silent.** Before going silent, emit the pre-flight block (below). After that, NO interim narration, NO progress beats, NO mid-run check-ins. Tool calls remain visible in the UI but are not narrated. Silent until the end-of-run summary.

**R4 — Single end-of-run summary.** When the protocol completes or halts, emit one summary block (below). All gate verdicts, all admin ESCALATE entries, all process-critic findings, the checkpoint state, next-step suggestion.

**R5 — Hard halts always abort cleanly.** Any of these → write cascade-checkpoint with halt reason, emit end-of-run summary, exit:
- Cap exhaustion (R2).
- Pre-flight check failure (below).
- Mid-run discovery of a parking-lot HARD item targeting a phase already passed in this run.
- `/and-cut` invocation by the principal.
- `/and-substance chapter` Phase 0 HARD-abort on unacknowledged substantive aggregate-state entries.
- Any HARD-abort the chain documents that is not in the R2 cap-iteration table.
- Tool failure that cannot be retried.

### Pre-flight (run all checks; print one block; halt before chain begins if any hard-block surfaces)

Pre-flight checks (all read-only):

- `project.series_audit.approved_at` set AND `stale_since` null.
- `active-project/staff/showrunner/parking-lot.md` open HARD items matching `/and-substance chapter` / `/and-write` / `/and-review bones` / `/and-facets` / `/and-stitch` for the target chapter slug.
- For book-level scope with `<NN> > 1`: prior book's chapters with `cold_read.verdict: PASS-WITH-DEPTH-PASS-REQUIRED` all have `depth_pass_resolved_at` set.
- `active-project/staff/showrunner/aggregate-state.md` present? If yes: any `revision_layer[]` entries with `class: substantive` AND `acknowledged: false`? (These are R5 hard-blocks until acknowledged.)
- `active-project/voice-exemplar.md` presence (informational; absence is fine).
- Disk-write permissions on `active-project/staff/showrunner/`, `active-project/draft/`, `active-project/theater/bones/`, `active-project/theater/facets/`, `active-project/theater/dialogue/`, `active-project/staff/stitcher/`, `active-project/staff/cohere/`.

Pre-flight print format:

```
================================================================
PRODUCE CHAPTER b<NN>c<MM> — PRE-FLIGHT
================================================================
Series audit       : APPROVED 2026-MM-DD  |  STALE: <reason>
Parking-lot HARD   : <N> items in scope (list IDs)  |  CLEAR
Prior-book depth   : N/A (book 1)  |  <N> unresolved (HALT)
Aggregate-state    : PRESENT through b<NN>c<MM-1>, <N> unack substantive (<HALT if >0>)  |  ABSENT (first chapter)
Voice exemplar     : PRESENT  |  ABSENT
Disk paths         : OK  |  <which path failed>
----------------------------------------------------------------
Scope              : b<NN>c<MM>  (single chapter end-to-end)
Cap-bound gates    : bones (1 retry) / facet-audit (2 internal passes) / stitch P9 (1 retry)
Expected halts on  : cap exhaustion, P10 HOLD-THREAD (gates next chapter, not this one)
Estimated cost     : ~35-55 dispatches typical; up to ~90 with full cap-iteration (DEC-0116 slim /and-facets: ~10-12, was ~60-100)
Estimated runtime  : ~20-35 minutes
================================================================
Going silent. End-of-run summary will be the next message.
================================================================
```

If any pre-flight line is HALT, do not enter the chain. Print the pre-flight block with the halt line called out, plus a single "next:" line naming what the principal needs to resolve, and exit.

### The chain (silent execution)

Sequence — no principal output between steps:

1. **`/and-substance chapter b<NN>c<MM>`** (mode: cascade-implicit; Phase 0 reads aggregate-state.md and HARD-aborts on unacknowledged substantive entries — caught at pre-flight, but re-verified at Phase 0).
2. **`/and-write b<NN>c<MM>`** (decomposition + bones + per-character dialogue + scene-map).
3. **`/and-review bones b<NN>c<MM>`** (mandatory gate; on FOLLOW-FAIL or fidelity-FAIL → R2 auto-iterate).
4. **`/and-facets b<NN>c<MM>`** (slim — DEC-0116: single R1 authoring round + context/aliveness review + Phase 4 mechanical auditor as the facet-layer gate; the R2 round and Phase 5b audience-gate are retired; the auditor self-remediates ≤2 passes, no principal prompt).
5. **`/and-stitch b<NN>c<MM>`** through Phase 9 (cold-read terminal gate; on FAIL → R2 auto-iterate).
6. **`/and-stitch b<NN>c<MM>` Phase 10 FORWARD-THREAD** (reads aggregate-state.md / prior drafts; threading-review fork; classify-and-apply; emit/update aggregate-state.md; PASS-THREAD or HOLD-THREAD).

Every command's Phase 0 reads `active-project/staff/showrunner/cascade-checkpoint.md` and observes `mode: unattended` to suppress per-command narration. Update cascade-checkpoint at every step transition with the current command and verdict.

`/and-postop` does NOT fire automatically. It is optional and surfaces in the end-of-run summary as a suggested next step only.

**`/and-cohere` fires as a mandatory gate at book-thirds checkpoints (PROP-0050, accepted 2026-06-08).** After Phase 10 completes, check whether the just-shipped chapter is the first chapter to reach the ~1/3 or ~2/3 threshold of the current book's planned chapter count. Compute the two thresholds as `ceil(chapter_count × 1/3)` and `ceil(chapter_count × 2/3)` from `books[b<NN>].chapter_count` in `active-project/staff/showrunner/memory.md`; each threshold fires exactly once (mark `cohere_fired_at_third: [1/3|2/3]` in the cascade-checkpoint after firing). If the completed chapter's index equals either threshold: fire `/and-cohere b<NN>` over the full completed range (`from: b<NN>c01 to: b<NN>c<MM>`) before printing the end-of-run summary. A `FAIL-COHERE` on structural sameness or setup/payoff failure blocks the next chapter ship until addressed — do NOT continue the cascade past FAIL-COHERE. `PASS-COHERE` or `PASS-COHERE-WITH-SOFT-ITEMS` continues normally; soft items surface in the end-of-run summary. Outside book-thirds triggers, `/and-cohere` is opt-in (suggest in summary on HOLD-THREAD signals; do not fire automatically).

### End-of-run summary (single message on completion or halt)

```
================================================================
PRODUCE CHAPTER b<NN>c<MM> — <COMPLETE | HALTED-<class>>
================================================================
Outcome            : COMPLETED | HALTED-CAP-EXHAUSTION | HALTED-HARD-BLOCK | HALTED-CUT | HALTED-TOOL-FAILURE
Chapter            : b<NN>c<MM>
Phase 9 verdict    : PASS | PASS-WITH-DEPTH-PASS-REQUIRED | FAIL (after N retries)
Phase 10 verdict   : PASS-THREAD | HOLD-THREAD (M substantive items surfaced)
Retries            : bones <0|1> / facet-cycles <1|2|3> / stitch <0|1>
Aggregate-state    : updated through_chapter=b<NN>c<MM>, <K> unack substantive
Parking-lot        : <N> new HARD, <M> new SOFT items written
ESCALATE queue     : <N> items (file: active-project/staff/showrunner/escalate-queue-<ts>.md)
Process-critic     : <N> proposal candidates logged
Checkpoint         : active-project/staff/showrunner/cascade-checkpoint.md
Dispatches         : <count>
Runtime            : <min>
Draft              : active-project/draft/b<NN>-c<MM>.md  (<word-count> words)
----------------------------------------------------------------
Next               : /and-postop b<NN>c<MM> (optional)  |  produce b<NN>c<MM+1>  |  resolve <halt-reason>
================================================================
```

If Phase 10 returned HOLD-THREAD with substantive items: the summary explicitly names what the principal needs to acknowledge (or upstream-rerun) before the next chapter-production run can proceed. Do NOT prompt; just name.

### Mid-run discipline (silent)

While the chain runs:
- All admin dispatches use `subagent_type: admin`, `mode: user-proxy` per CLAUDE.md Rule 13.
- Admin OK/disposition → apply silently.
- Admin ESCALATE → append to `active-project/staff/showrunner/escalate-queue-<ts>.md`; do NOT prompt; continue the chain with admin's tentative disposition or the chain's default.
- Process-critic dispatches at chain tail-steps (URI-ADMIN-PROCESS-CRITIC; `/and-write` Phase 6.5, `/and-facets` Phase 4.5 (renamed from the retired Phase 5c under DEC-0116), `/and-stitch` Phase 9.5, etc.) fire as documented; outputs are logged to the proposals log; not surfaced mid-run.
- Tool failures: retry once with backoff. If still failing, R5 hard halt.

### What NOT to do during chapter production

- Do NOT call `AskUserQuestion`. Use admin user-proxy.
- Do NOT narrate Phase transitions to the principal.
- Do NOT pause to "check in" between gates.
- Do NOT skip Phase 10 (it is part of the chapter-production motion, not optional).
- Do NOT fire `/and-postop` as part of this chain; it is an opt-in suggestion in the summary only.
- Exception: `/and-cohere` DOES fire automatically at book-thirds checkpoints per the rule above — it is the one permitted automatic dispatch outside the 6-step chain. Do NOT suppress it at those checkpoints.
- Do NOT decide to upgrade an R2 cap-bounded retry into a hard halt before cap is exhausted.
- Do NOT decide to upgrade a hard halt into "let me try one more thing" past R5 conditions.

---

## Producing revisions — book-complete protocol

When the book is shipped and the user asks to revise it, this is the operation. Revisions **mutate already-shipped drafts** — that is irreversible relative to the terminal deliverable, so the discipline below is mandatory. Unlike chapter-production, revisions are *targeted*: you change named chapters for named reasons, not the whole book on spec.

### Where revision scope comes from (in priority order)

1. **The cohere / parking-lot revise queue.** `active-project/staff/showrunner/parking-lot.md` items with `created_by: /and-review cohere` (or any `target.command: /and-write` revise item) are the pre-identified, evidence-backed revision targets. The b01 standing queue: `pl-2026-06-06-cohere-001` (c03 Sera establish-leg) + `pl-2026-06-06-cohere-002` (c20 Sera confirm-leg) — both SOFT, principal-deferred per DEC-0108.
2. **`/and-postop` findings** on shipped chapters (depth-of-quality calls).
3. **Principal direction** — a specific concern the user names ("the middle sags", "Sera never lands"). Read the consolidated manuscript (below) to ground it.
4. **A fresh `/and-cohere` run** if the book hasn't been cohered recently or the revision question is cross-chapter.

Do NOT invent revision targets the queue and the principal did not name. A complete book is the deliverable; the bar for re-opening it is an evidence-backed finding, not a vibe.

### The two revision mechanisms

- **Per-chapter re-cascade (the workhorse).** For a finding localized to one chapter's bones: `/and-write b<NN>c<MM> revise [--from-signals]` → `/and-review bones` → `/and-facets` → `/and-stitch` (through Phase 9, and Phase 10 re-thread if the change is substantive). This is the same chain as chapter-production, run in `revise` mode against an existing chapter. Cap-bounded gates (R2) apply identically.
- **Cross-chapter cohere loop.** For a finding that spans chapters (a setup/payoff that crosses chapter boundaries, like the Sera arc): `/and-cohere b<NN> [<from>-<to>]`, which consumes the revise queue and re-cascades each affected chapter until `PASS-COHERE` or convergence cap. `--strict` promotes SOFT queue items to HARD.

### Mandatory discipline

- **Archive before mutating.** Before any chapter re-cascade, copy the current `active-project/draft/b<NN>-c<MM>.md` into `active-project/draft/_archive/<date>-pre-revise-<reason>/`. The shipped version is the baseline you must be able to diff against and restore.
- **Rules 19/20/21 apply to every dispatch** (verify emitted artifacts exist on disk; read-back any async agent's shared-state edits before committing; RECONCILE hand-authored aggregates before commit).
- **One revision reason at a time.** Don't bundle the Sera fix with an unrelated prose pass — each revision should be traceable to its queue item / DEC.
- **Re-thread and re-consolidate after.** A substantive change ripples: run `/and-stitch` Phase 10 forward-thread for downstream chapters if continuity moved, then refresh the consolidated manuscript (below). Stamp the resolved parking-lot item (`resolved_at` / `resolved_by` / `resolution_note`).
- **Re-cohere to confirm.** After applying a cohere-queue revision, re-run `/and-cohere` (or `/and-review cohere`) on the affected range to confirm the finding closed and nothing regressed.

### Consolidated manuscript (the revision read-surface)

Keep a single assembled file at `active-project/draft/b<NN>-manuscript.md` — the 20 chapter drafts concatenated with chapter dividers. This is what you read to decide and judge revisions (not 20 separate files). Rebuild it after any chapter re-cascade so it never lies. It is a *derived* artifact — never hand-edit it; edit the per-chapter drafts via the chain and regenerate.

### What NOT to do during revisions

- Do NOT hand-edit `draft/b<NN>-c<MM>.md` or the consolidated manuscript directly to "just fix a line." Prose changes go through `/and-write revise` → chain, so bones/facets/state stay coherent. (Polish-layer direct prose editing is `/and-wrap`, still deferred.)
- Do NOT mutate a shipped draft without archiving the baseline first.
- Do NOT re-open chapters the queue and principal did not name.
- Do NOT skip the re-thread / re-cohere confirmation after a substantive change.

---

## Common gotchas (check before advancing)

- **`project.series_audit.stale_since` is set** → `/and-substance book` HARD-aborts. Series-level audit needs re-approval at `/and-cast` Phase 5.
- **`active-project/` exists but no `series_audit.approved_at`** → cannot author book content yet. Run `/and-cast` Phase 5.
- **Parking-lot HARD item matching current phase** → must resolve at this run, not later.
- **`aggregate-state.md` has unacknowledged substantive revision-layer entries** → `/and-substance chapter` Phase 0 HARD-aborts. Principal must acknowledge each entry (or upstream-rerun) before producing the next chapter.
- **PROP-0002 (em-dash-fold caps) and PROP-0004 (exposition surface field) are in queue, not implemented.** Don't pretend the gates exist.
- **Rules 19/20/21 are LIVE (PROP-0043/44/45, implemented 2026-06-07).** Every dispatch: (19) verify a Write-capable agent's contracted artifact is on disk before consuming/committing — an in-message-only result is NOT delivered; (20) read-back any async agent's edits to shared state (parking-lot / memory / decisions / cohere-state / proposals) before committing on top; (21) RECONCILE hand-authored cohere/verdict aggregates (citation resolution + report↔state field-equality + self-contradiction split) before commit. These are not optional.
- **PROP-0003-A voice exemplar at `active-project/voice-exemplar.md`** is optional but recommended for `/and-stitch`. Absence is fine; just note `voice-exemplar: ABSENT` in pre-flight.
- **PROP-0005 persona-exemplars auto-resolve at agent dispatch.** Tier-1 agents (impersonator, audience) self-load from `cards/persona-exemplars/` or `active-project/persona-exemplars/` — no dispatcher action needed.
- **Polish / `/and-wrap` is deferred.** `draft/<book>-<chapter>.md` is the terminal deliverable. Don't try to author polish.

---

## Hard human checkpoints (never auto-advance past)

- **`/and-cast` Phase 5 — series-level audit.** Only blocking human checkpoint in the chain. If the user hasn't approved at this gate, you cannot proceed to book authoring. (This is upstream of any chapter-production run; never arises inside the protocol.)

Every other prompt that *looks* like a human checkpoint (accept/redraft, mode picks, branch choices) routes to admin user-proxy per Rule 13. The main session does not call `AskUserQuestion` directly except on admin's explicit ESCALATE — and during a chapter-production run, even ESCALATE is queued, not prompted.

---

## When you're truly stuck

- Memory.md disagrees with the filesystem → trust the filesystem, propose a memory update, ask admin.
- A command body references a phase that doesn't exist → check `archive/commands/` for migrated names.
- An agent dispatch returns nonsense → check whether the agent's persona-exemplar exists and isn't excluded (PROP-0005).
- User says "no, not that" twice → stop. Ask admin user-proxy what they actually want.
- A chapter-production run produces an end-of-run summary the user clearly disagrees with → don't immediately re-fire. Read their specific concern, route to admin user-proxy.

---

## What NOT to do at session start

- Don't ask "what do you want to work on" if memory.md has a clear `current_chapter` + `last_phase`. Just continue.
- Don't re-litigate prior decisions by reading `staff/admin/decisions.md` end-to-end. Trust DEC entries; only read details if relevant to the current action.
- Don't run `/and-postop` reflexively after `/and-stitch`. It's optional; only fire if the user asks or it's a book-mid/close milestone.
- Don't run `/and-cohere` reflexively outside of the book-thirds checkpoints. The two book-thirds triggers are mandatory (see "The chain" above) and fire automatically; outside them, only fire if the user asks.
- Don't open a new ablation/experiment unless asked. They're on-demand.

---

## Authority

This runbook is operational guidance. `CLAUDE.md` and `schemas/` are authoritative on rules and formats. When this runbook disagrees with them, they win — and this file needs updating.

**The "Producing a chapter" section above is the canonical protocol for the project's primary operation.** Command bodies (`/and-substance`, `/and-write`, `/and-review`, `/and-facets`, `/and-stitch`) implement the chain steps; this runbook owns the discipline (R1–R5), the pre-flight, and the end-of-run summary. When a command body's behavior conflicts with the runbook's discipline rules, the runbook wins for chapter-production runs.
