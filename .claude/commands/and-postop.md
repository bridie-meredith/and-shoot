---
description: Post-op review for a shipped chapter. Slim 3-fork routine (substance-delivery + naive cold-read + one audience persona) or full 5-fork milestone mode (adds forward-hook + orchestrator-critic synthesizer). Distilled from the b01c01 8-fork post-ship audit suite; 60% less spend, same signal. Usage - /and-postop <book>-<chapter> [milestone] [--persona <slug>]
---

# /and-postop

Post-op review for a shipped chapter. Runs *after* `/and-stitch` has emitted `draft/<book>-<chapter>.md` with cold-read PASS or PASS-WITH-DEPTH-PASS-REQUIRED. **Not a gate** — the chapter has already shipped. This is the depth-of-quality call: did the contract land on the page, was it fun to read, and (at book milestones) does the chapter pay forward into the rest of the book.

Distilled from the b01c01 8-fork post-ship audit suite (`active-project/staff/showrunner/post-ship-audit-prompts-b01c01.md`). The original suite ran eight forks and converged on a single finding from seven different angles — most of the convergence was confirmation-spend, not new signal. This command keeps the forks that earned their slot and drops the rest.

---

## Modes

- **Routine** (default): 3 forks — substance-delivery + naive cold-read + one audience persona. Fires after every chapter ship.
- **Milestone** (`milestone` positional): 5 forks — routine three plus forward-hook (dramatist) plus orchestrator-critic running as synthesizer (with the other four reports as input, not in parallel). Fires at book midpoint and book close.

What's NOT included and why:
- **Pipeline-fidelity audit** (b01c01 Fork 1): only fires when `.claude/commands/and-stitch.md` or stitch schemas change. Routine post-ship re-auditing produced metadata-only findings.
- **Two additional audience personas in parallel** (b01c01 Forks 4b/4c after 4a): diminishing returns past one persona. The naive cold-read covers the general-reader axis; one persona adds domain-canon specificity. The other two reads largely confirm the same axis.
- **Orchestrator-critic as a parallel fork**: wrong place in the wave order. It re-derives what the other forks said because it has the same raw materials. Milestone mode promotes it to synthesizer.

---

## Inputs (read-only)

- `active-project/draft/<book>-<chapter>.md` — the shipped chapter
- `active-project/draft/<book>-<chapter>.annotated.md` — for sentence-IDs
- `active-project/staff/showrunner/memory.md` — chapter substance contract + measured deltas; for milestone mode, also c+1..c+N for forward-hook
- `active-project/staff/reviews/coldread-<book>-<chapter>-*.md` — Phase 9 cold-read (referenced, not re-run)
- `active-project/staff/reviews/staging-<book>-<chapter>-*.md` — Phase 9 staging signals (referenced)
- `active-project/audience/<slug>/card.md` (+ ltm.md + stm.md) — for the persona fork; one slug per run

---

## Phase 0 — Argument resolution + cluster cross-check

1. Parse `<book>-<chapter>` from $1.
2. Mode: `milestone` if $2 is `milestone`, else `routine`.
3. Persona slug: `--persona <slug>` override; else select one persona from `active-project/audience/` (round-robin against `chapters[<slug>].postop.personas_used[]` so the routine rotates through the three available personas across chapters).
4. **Cluster cross-check.** Read `chapters[<slug>].cold_read.signal_clusters[]` from showrunner memory. If a cluster is present and `chapters[<slug>].cold_read.verdict == PASS-WITH-DEPTH-PASS-REQUIRED`, surface a NOTE before dispatching: the depth-pass is already known. /and-postop runs as planned but its findings should fold into the same revise --from-signals queue rather than open a separate one.
5. If `chapters[<slug>].cold_read.verdict != PASS` and `!= PASS-WITH-DEPTH-PASS-REQUIRED`, abort: the chapter is not terminal; /and-postop only runs on shipped chapters.
6. **Parking-lot scan (Rule 14).** Read `active-project/staff/showrunner/parking-lot.md`. Items matching this invocation (`target.command: /and-postop` + `target.scope` = `<book>-<chapter>` or `*` wildcard + `status: open`): HARD → abort unless this run resolves; SOFT → fold into the post-op forks' surface area + final report. Resolving phase stamps `resolved_at` + `resolved_by` + `resolution_note`; never delete.

---

## Phase 1 — Routine forks (parallel; 3 dispatches)

### Fork A — Substance-delivery audit · `subagent_type: general-purpose`

The most informative fork from the b01c01 suite. Reads the prose against the contract, checks per-axis Δ on the page, per-bone opposing-force visibility (the prose-layer check that Phase 6 bone-gate cannot do because it audits at rationale layer), per-scene protagonist_force delivery, dramatic_shape integrity, goal triplet landing. Cites paragraph + sentence numbers. Cross-checks against the staging review's body-staging cluster (if any).

Output: `active-project/staff/reviews/substance-delivery-<book>-<chapter>-<timestamp>.md`. Verdict: DELIVERED / PARTIAL / SHORTFALL with per-dimension calls.

### Fork B — Naive cold-read · `subagent_type: general-purpose`

Cheapest fork by token, highest reader-pleasure signal density. Reads ONLY the clean draft — no other project files. Answers six questions: enjoyed it? where attention drifted? where prose grabbed? voice (person or machinery)? want chapter+1? genre/tone read?

Output: `active-project/staff/reviews/pleasure-read-<book>-<chapter>-<timestamp>.md`. Under 400 words.

### Fork C — Audience persona threshold read · `subagent_type: general-purpose`

Loads the selected persona card (card.md + ltm.md + stm.md if present). Reads in-character — voice, taste-thresholds, attention pattern. Answers six questions: finished? Threshold Discipline fires? liked? disliked? read chapter+1? one-sentence-to-friend.

This is NOT the /and-facets adversarial gate. Post-ship reader experience only.

Output: `active-project/staff/reviews/audience-<persona-slug>-<book>-<chapter>-<timestamp>.md`.

---

## Phase 2 — Milestone forks (parallel; 2 additional dispatches) — `milestone` mode only

### Fork D — Forward-hook audit · `subagent_type: dramatist`

Skip in routine mode. Fires at book midpoint and book close.

For each downstream chapter with an authored chunk: does the chapter under review plant the hooks that downstream chapter requires? Per-downstream verdict: HOOK-LANDED / HOOK-WEAK / HOOK-MISSING / NO-DOWNSTREAM-DEMAND. Wasted setup is a structural fault as much as missing setup is — flag hooks planted with no downstream pickup.

Output: `active-project/staff/reviews/forward-hook-<book>-<chapter>-<timestamp>.md`. Under 800 words.

Dramatist agent has no Write tool — orchestrator persists the returned content to the target path.

### Fork E — Orchestrator-critic synthesizer · `subagent_type: general-purpose`

Skip in routine mode. Fires AFTER Forks A/B/C/D have completed and their reports are written. Inputs include the four prior reports; the fork synthesizes them, does not re-derive their findings.

Loads `staff/orchestrator-critic/card.md` and applies the run-judge rubric. The verdict is advisory post-ship (the chapter has already passed Phase 9; this is the depth-of-quality call, not a re-gating).

Output: `active-project/staff/reviews/orchestrator-critic-<book>-<chapter>-<timestamp>.md`. Verdict: SUCCESSFUL / NOT-SUCCESSFUL / SUCCESSFUL-WITH-RESERVATIONS + 3-sentence rationale.

---

## Phase 3 — Convergence call

Read the routine reports (and milestone if present). Apply the convergence rule:

- **If 3+ forks converge on the same prose-surface gap** (e.g. all reads flag the same bone-cluster or same opening-drag paragraph), record `chapters[<slug>].postop.convergence = {pattern: <label>, fork_count: <N>, recommended_action: /and-write <chapter> revise --from-signals}`. This is the strongest case for a depth pass.
- **If fork verdicts diverge**, record `chapters[<slug>].postop.convergence = {divergent: true, fork_verdicts: [...]}`. Divergence is its own signal — usually means the chapter is doing one thing well and another thing poorly; the user decides which axis to act on.
- **If all forks return clean** (PASS / DELIVERED / yes-finish-yes-read-c+1), record `chapters[<slug>].postop.convergence = {pattern: clean, fork_count: <N>}`. No action.

Update `chapters[<slug>].postop = {ran_at, mode, personas_used: [...], reports: [...], convergence: {...}}` in showrunner memory.

---

## Phase 3.5 — Admin process-critic dispatch (URI-ADMIN-PROCESS-CRITIC, 2026-05-25; ALWAYS fires)

Postop's job is to find what got past the chain. Admin's job is to translate that into a process-change proposal. Therefore process-critic mode auto-fires on **every** postop run, regardless of convergence verdict — even on `pattern: clean`. (A clean convergence run still feeds admin the report; admin returns `OK` and the dispatch is cheap.)

Dispatch:
- `subagent_type: admin`
- prompt carries:
  - `mode: process-critic`
  - `trigger.reason: postop`
  - `trigger.source_report: <path to the postop convergence summary; the routine/milestone fork-report paths are linked from the convergence entry>`
  - `trigger.source_verdict: postop-convergence:<pattern>` (e.g. `postop-convergence:body-staging-gap`, `postop-convergence:divergent`, `postop-convergence:clean`)
  - `gate_path: .claude/commands/and-postop.md#phase-3`
  - `secondary_gate_paths: [<upstream gate paths the convergence pattern implicates — typically /and-write Phase 6 and/or /and-stitch Phase 9 if the cluster names a bone-level or stitch-level gap>]`

Non-blocking — Phase 4 summary proceeds. Admin's return logged under `chapters[<slug>].postop.admin_process_critic = {verdict, proposal_id, dec_id, summary}` in showrunner memory. See CLAUDE.md Rules §13 and `schemas/admin-proposal.schema.md`.

---

## Phase 4 — Summary

Print a concise summary: mode, fork verdicts in a table, convergence pattern, recommended next step (revise --from-signals | continue | none).

---

## What this command does not do

- Does not modify bones, facets, draft, or render-log. Read-only against the shipped artifacts.
- Does not re-gate the chapter. Phase 9 cold-read is the gate; /and-postop is depth-of-quality.
- Does not run the pipeline-fidelity audit. That fires when stitch command/schemas change — separate cadence.
- Does not run all three audience personas in parallel. Routine selects one; rotates across chapters.
- Does not run on un-shipped chapters. Phase 0 aborts if cold_read verdict is not PASS / PASS-WITH-DEPTH-PASS-REQUIRED.
