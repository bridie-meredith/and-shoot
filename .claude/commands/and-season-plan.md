---
description: Plan a subsequent season (N+1) for an active project. Lifts the season-planning subroutine from /and-project Phase 1d and parameterizes the slug. Reads the previous season's terminal state so the new season's drama reacts to where the previous season actually ended. Usage - /and-season-plan <season-slug>
---

Subsequent-season planning command. /and-project handles season 1 inline; this command handles seasons 2+ as standalone planning acts.

You are the orchestrator. All work routes through subagent dispatches (screen-writer, audience, dramatist, auditor, fixer). Do not dispatch showrunner — it is a memory holder, not an orchestrator.

**All dispatches use the Agent tool.** Inline generation is not a valid substitute.

## Args

- `$1` — required. Season slug to plan (e.g. `s02`). Must not already exist in `seasons[]` in showrunner memory.

---

## Phase 0 — Validate

1. Read `active-project/staff/showrunner/memory.md`.
2. Confirm:
   - Project is active (memory.md exists, series-plan.md exists, `series.theme` is non-null).
   - `$1` is not already in `seasons[]`.
   - Previous season `seasons[N-1]` exists with `status: wrapped` OR `season.protolines_complete` is set. If neither, **abort** — the previous season's terminal state must be settled before its outcomes can shape the next season's drama. Surface for human review.
3. Print:

```
Planning season: <slug>
Previous season: <prev-slug> | status: <wrapped|protolines_complete> | terminal-episode: <slug>
```

---

## Phase 1 — Read previous season terminal state

Inputs the screen-writer needs to react to *where the previous season actually ended* (not just to the series-plan sketch):

1. Previous season's plan (`active-project/staff/showrunner/season-<prev-slug>-plan.md`).
2. Previous season's terminal episode proto-line file (`active-project/theater/proto-lines/<prev-terminal-slug>.md`) — read the closing 20–30 IDs.
3. Active actor state files (`active-project/actors/<slug>/state.md` for every actor on the closing roster). Each captures the actor's location, custody chain, vibe shifts at season-end.
4. Studio state (`active-project/staff/studio/state.md`) — terminal location/prop state.
5. Showrunner memory `seasons[N-1]` block — recorded outcomes, threads carried, deltas.
6. Series-plan.md — the long-arc sketch this season fits into.
7. The series and season-N-minus-1 vibe-clouds (from `active-project/staff/studio/vibes.md`).

Bundle these as the **terminal-state brief** for the screen-writer dispatch.

---

## Phase 2 — Author season plan

Lifted from `/and-project` Phase 1d steps 1–5, parameterized for `$1`.

### 1. Derive season vibe-cloud

Read series vibe-cloud + previous-season vibe-cloud from `active-project/staff/studio/vibes.md`. Note season-to-season deltas — what the previous season's terminal state shifts about register, mood, escalation register. Append the new season section to `vibes.md` with explicit deltas from both series and previous-season vibe-clouds.

### 2. Establish season drama

Drama-sized statement: the season's central collision and what cannot survive it. Two sentences. External and structural. **The previous season's terminal state is load-bearing here** — the new season's drama reacts to what was settled, broken, or carried forward, not to a clean slate.

### 3. Dispatch screen-writer (season-plan authoring)

Inputs:
- Series plan (`series-plan.md`).
- Season drama statement (from step 2).
- Series + new-season vibe-clouds.
- Series constraints (laws, lore, behaviors from showrunner memory).
- `active-project/staff/showrunner/brief-expansion.md`.
- **Terminal-state brief from Phase 1.**

Task: write one chunk statement per episode of season `$1`.

**Chunk format:** the episode's central dramatic pressure — drama-sized, enough to fill a chapter, not a minor incident inside one. Name the collision or threshold the episode turns on, and what cannot remain unchanged after it. Concrete and specific, external and structural, no character psychology. "The soldier marks her location on a route-map from twelve feet away while Plumm's men inventory the settlement — she watches it happen and does not move" not "X runs because they fear being caught."

### 4. Audience + dramatist review (3-try max)

Dispatch audience (3 personas, the same set that has been active for the project — read from `active-project/audience/`) and dramatist in parallel.

- Audience: does the season satisfy your persona's appetite given where the previous season ended? Per-episode ENGAGED/TOLERATED/BORED on chunk statements.
- Dramatist: shape check (rise-peak-fall, escalation spine, climax in back half, no flatlines, terminal beat reacts to where the previous season ended).

Accept/revise loop, max 3 attempts. On non-convergence, surface for human review with the failing reasons.

### 5. Persist

- Write season plan to `active-project/staff/showrunner/season-<slug>-plan.md`.
- Update `active-project/staff/showrunner/memory.md`:
  - `routing.season_plan: active-project/staff/showrunner/season-<slug>-plan.md`.
  - Append to `seasons[]` array with `status: active` and all episode slugs with `status: planned`.
  - Set `active.season: <slug>`.
  - Leave `active.episode` as-is (next /and-season run sets it; or human sets it explicitly if running episode-by-episode).
- Append the terminal-state delta summary to the previous season's `seasons[N-1].terminal_handoff` field in memory.

**Log file:** `active-project/staff/showrunner/season-<slug>-plan-log.md` — same format as `season-s01-plan-log.md`.

---

## Phase 3 — Cross-season audit

Dispatch **auditor** (fork, fresh context) against the new season plan + the previous season's terminal state + the series plan.

Brief — verify:
- The new season's chunks remain consistent with series-plan.md's long-arc sketch.
- The new season opens from the previous season's terminal state without contradicting recorded outcomes (actor locations, prop custody, condition deltas, surviving threads).
- Series laws and lore hold across the season transition.
- The new season's terminal beat does not contradict any series-plan commitment for season N+2 (if sketched).

Output: `active-project/staff/auditor/season-<slug>-plan-audit.md`.

Faults route to fixer (line-level recasts) or surface for human review (structural contradictions with series plan).

---

## Phase 4 — Present results

Print to the human:

```
--- SEASON PLAN COMPLETE: <slug> ---

PREVIOUS SEASON TERMINAL STATE
  status: ...
  terminal episode: ...
  carried threads: ...
  vibe deltas to new season: ...

SEASON <slug>
  Drama: ...
  Vibe-cloud delta from series: ...
  Vibe-cloud delta from previous season: ...
  Episodes:
    E01 — ...
    E02 — ...
    ...

CROSS-SEASON AUDIT: <PASS | FAULTS-{count}>

LOG FILES
  active-project/staff/showrunner/season-<slug>-plan.md
  active-project/staff/showrunner/season-<slug>-plan-log.md
  active-project/staff/auditor/season-<slug>-plan-audit.md

Next: /and-season <slug> to draft proto-lines for the season.
```

---

## Notes

- This command is the cross-season equivalent of `/and-project` Phase 1d. Same five-step planning subroutine; the only structural addition is the **terminal-state brief** in Phase 1, which conditions the screen-writer on the previous season's actual ending.
- This command does NOT mark the previous season `wrapped`. That is `/and-wrap`'s job. Per the default-skip-wrap rule, /and-wrap is opt-in and may be deferred or bulk-run after multiple seasons of proto-lines exist.
- This command does NOT generate proto-lines. It produces episode chunks only. `/and-season <slug>` handles the proto-line authoring.
- Audience persona membership is fixed at project activation. Do NOT change personas at season planning time.
- Cross-season coherence is checked at Phase 3. Per `/and-season` Phase 3's intra-season scope: that audit only checks within a single season; this Phase 3 is the cross-season pair.
- Prereq: `/and-season` has been run on the previous season (so `protolines_complete` exists) OR `/and-wrap` has been run (so `status: wrapped` exists). If neither, the previous season's terminal state is not settled and this command aborts.
