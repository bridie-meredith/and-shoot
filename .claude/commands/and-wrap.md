---
description: Wrap a completed shoot. Supports single-episode and bulk modes. Reads from theater/<slug>-archive/ for already-archived episodes (the default after /and-shoot Phase 0). Usage: /and-wrap [episode-slug | --all-shot | s01e01..s01e05]
---

Takes the raw show file from a completed shoot and produces a final manuscript in `active-project/polish/`. Requires the episode to be in `shot` status. Run `/and-shoot` first.

You are the orchestrator for this command. You dispatch subagents directly — dramatist, audience, auditor, fixer, editor. Do not dispatch showrunner. Showrunner is not in the orchestration chain here.

**All dispatches use the Agent tool.** Inline generation is not a valid substitute. An agent not spawned in its own isolated context will not have the role constraints the pipeline depends on.

## Args

- `$1` — selects what to wrap. Forms:
  - omitted → wraps the most recent episode whose status is `shot`
  - episode slug (e.g., `s01e03`) → wraps that single episode (status must be `shot`)
  - `--all-shot` → wraps every episode currently in `shot` status, in season order
  - range `s01e01..s01e05` → wraps each episode in the range whose status is `shot`, in order

In bulk modes, episodes wrap one at a time, sequentially. If one fails or escalates, stop and surface state — do not continue past a failure.

---

## File source resolution

Default flow leaves shot episodes archived at `active-project/theater/<slug>-archive/`. Wrap reads from there, not from the live `theater/` directory. Resolve per target:

1. If `active-project/theater/<slug>-archive/` exists with `show.md` and `episode-plan.md` → that's the source. Wrap reads and writes log files inside the archive directory (`<slug>-archive/wrap-structure-log.md`, etc.). The auditor report still goes to `active-project/staff/auditor/<slug>-wrap-audit.md`.
2. Else if `active-project/theater/show.md` exists and its header matches `<slug>` → that's the source (the just-shot episode that hasn't been archived yet). Wrap reads/writes inside the live `theater/` directory.
3. Else stop with a clear error naming the slug and where it looked.

This means /and-wrap works whether you call it immediately after /and-shoot (live theater) or weeks later in bulk (from archives).

---

## Phase 1 — Validate (per target)

Read `active-project/staff/showrunner/memory.md`. For each target slug:
- Status in season plan must be `shot` — not `planned`, not `complete`
- Resolved source (live or archive) must contain `show.md` (non-empty) and `episode-plan.md`

If any check fails, print the problem and stop.

Also check: if any wrap log files already exist for this target (`wrap-structure-log.md` or `wrap-audience-log.md` in the resolved source dir), stop and print:
```
Wrap log files already exist for <slug> — wrap may have been interrupted mid-run.
Review the existing logs to see how far wrap progressed.
Delete the wrap log files in <source-dir> to restart, then re-run /and-wrap.
```

---

## Phase 2 — Wrap pipeline (per target)

At each step that dispatches a subagent, record the result in the log file for that step before continuing. A missing log file means the step did not run.

Read `<source-dir>/episode-plan.md` and `<source-dir>/show.md` — both must be in context before wrap begins. `<source-dir>` is whichever was resolved in Phase 1 (the archive dir or the live theater dir). All wrap log file paths below — `wrap-structure-log.md`, `wrap-audience-log.md` — live inside `<source-dir>`.

---

### STEP 1 — Dramatist: structure review

Dispatch dramatist with: the completed show file, the episode plan, the series plan (`active-project/staff/showrunner/series-plan.md`), and the active season plan (path from `routing.season_plan` in memory). Dramatist checks four thresholds:
- **Problem solves:** the episode's central problem reaches resolution (even if partial or pyrrhic)
- **End state ≠ start state:** at least one meaningful thing has changed — character, relationship, situation, world
- **Builds toward season finale:** the episode advances or complicates the season arc
- **Builds toward series finale:** the episode is legible in terms of the long game

**Log file: `active-project/theater/wrap-structure-log.md`**
```
problem solves: pass/fail — <one line>
end state delta: pass/fail — <one line>
season build: pass/fail — <one line>
series build: pass/fail — <one line>
overall: pass / flagged
[if flagged: disposition — patched at episode scope / escalated]
```

Threshold failures:
- Minor (a line or scene can patch it) → dispatch fixer with target and reason. Note in log.
- Structural (requires replanning) → flag for escalation. Note in log. Do not block wrap — continue to step 2 and return the escalation at the end.

---

### STEP 2 — Dramatist: scene boundary flagging

Dispatch dramatist to mark the show file in-place:
- `[scene-start: <label>]` at the opening of each scene
- `[scene-end: <label>]` at the close of each scene

Everything inside the flags is episode content — kept, edited, published. Everything outside (pre-scene warmup, post-scene trailing) is cut by the editor. The flags themselves are not cut.

No separate log file for this step. The flags in the show file are the record.

---

### STEP 3 — Audience: entertainment review

Dispatch all three audience agents with: the flagged show file, the episode vibe-cloud (from `active-project/staff/studio/vibes.md`), and their STM files (`active-project/audience/<slug>/stm.md` — load prior feedback before reviewing). Each identifies:
- Lines that land flat or feel inert
- Moments that break immersion or feel out of register with the vibe-cloud
- Any exchanges that are actively bad — confusing, boring, false to character

Each audience agent marks qualifying lines in the show file as `[⚑ audience: <slug>: <reason>]`.

After the review, audience writes wrap verdicts to their STM files (`active-project/audience/<slug>/stm.md`) — what they flagged, what they accepted, and why. A wrap review that does not write to STM has not completed correctly.

**Log file: `active-project/theater/wrap-audience-log.md`**
```
# Audience Wrap Review — <episode-slug>
<slug-1>: <N flags> — <summary of concerns, or "no flags">
<slug-2>: <N flags> — <summary of concerns, or "no flags">
<slug-3>: <N flags> — <summary of concerns, or "no flags">
lines patched by fixer now: <list or "none">
lines carried to editor: <list or "none">
```

Decide whether to dispatch fixer for flagged lines now or pass them to editor as advisory. Default: carry to editor unless the flag identifies something that will confuse continuity.

---

### STEP 4 — Auditor: constraints audit

Dispatch auditor (fork) with:
- The flagged show file (`active-project/theater/show.md`)
- All active constraint cards (`active-project/warehouse/constraint-*.card.md`)
- The episode plan (`active-project/theater/episode-plan.md`)
- The studio state file (`active-project/staff/studio/state.md`)
- Actor state files for all characters active this episode (`active-project/actors/<slug>/state.md`)

Auditor checks: law/lore/behavior compliance, show-file-vs-plan drift, state consistency (does the show file reflect what state records say happened?).

**Log file: `active-project/staff/auditor/<episode-slug>-wrap-audit.md`**
Full classified report (schema: `schemas/audit-report.schema.md`). A clean pass still produces a report — existence proves the check ran.

Route faults to fixer with scope and reason. Escalate only what cannot be resolved at episode scope.

---

### STEP 5 — Editor: final draft

Dispatch editor with the fully flagged show file. The editor receives:
- `active-project/theater/show.md` (with scene markers, needs-edit markers, and audience flags all present)
- `active-project/staff/auditor/<episode-slug>-wrap-audit.md` (advisory flags from auditor)

Editor:
- Applies scene boundary cuts: removes content outside `[scene-start]` / `[scene-end]` flags; keeps the flags as context markers
- Addresses `[⚑ needs edit]` lines from three-try failures
- Considers `[⚑ audience]` flags — rewrites where warranted, leaves where the flag is overcautious
- Prose pass: economy, continuity, tense, blocking, voice consistency

Editor saves the final draft to `active-project/polish/<episode-slug>.md`.

Editor does not add content. Editor does not make plot decisions.

---

### STEP 6 — Memory: minimal movement

After the editor completes:
1. Mark episode status `complete` in `active-project/staff/showrunner/memory.md`.
2. Advance `active.episode` **only if** the just-wrapped slug is the current `active.episode` AND no later episode has already been shot. (In the default shoot-shoot-shoot flow, `active.episode` is already pointing at the next unshot episode — wrap of an earlier episode does not move it.) If the season is complete (all episodes wrapped) and active was pointing at the just-wrapped one, set `active.episode` to `~` and note the season close.
3. **Timeskip check:** if the next episode picks up significantly later in time, update affected actor state files (`active-project/actors/<slug>/state.md`) and studio state (`active-project/staff/studio/state.md`) to reflect what changed during the gap. Skip this in bulk wrap of past episodes — actor state has already moved on; do not rewind it.
4. **Off-scene event check:** if something significant happened off-screen between episodes, record it in the relevant actor LTMs and append to `active-project/staff/showrunner/world-notes.md`.
5. Default: no timeskip, no off-scene event → memory stays exactly where the show file left it. Do not advance state without a reason.
6. **Actor memory close (mandatory).** For each actor active this episode: read the show file and identify any significant events — relationship shifts, discoveries, arc notes, residue that will carry forward. Append qualifying events to `active-project/actors/<slug>/ltm.md` (format: `[YYYY-MM-DD] EVENT: what changed | why significant`). Then prune `active-project/actors/<slug>/stm.md` to ~10 items: keep only what is genuinely on top of mind going into the next episode. Overwrite STM — do not append. If no significant events occurred, still confirm the STM is current. A missing or stale LTM/STM at episode close is a schema violation.

---

## Phase 3 — Present results

Present to the human:

```
--- WRAP COMPLETE: <episode-slug> ---

STRUCTURE
  pass  [or: flagged — <threshold>: <one line>]

AUDIENCE FLAGS
  <slug-1>: N | <slug-2>: N | <slug-3>: N
  patched: N | carried to editor: N

AUDITOR
  pass  [or: N faults (<scope>) / N escalations]

FINAL DRAFT
  active-project/polish/<episode-slug>.md

NEXT EPISODE
  <slug>  [or: season complete]

LOG FILES
  active-project/theater/wrap-structure-log.md
  active-project/theater/wrap-audience-log.md
  active-project/staff/auditor/<episode-slug>-wrap-audit.md

[Episode closed. Review final draft or run /and-shoot to begin the next episode.]
```

If there are escalations requiring human decision, present them before the closing line with: `ESCALATIONS REQUIRING YOUR DECISION:` followed by each one.

---

## Notes

- Wrap requires episode status `shot`. It will not run on a `planned` episode.
- Scene boundary flags are written in-place to the show file by the dramatist. The editor reads the marked-up file — it does not re-flag.
- Audience agents in wrap read the full episode, not individual lines. This is a different task from their per-line shoot role.
- The auditor is a fork — orchestrator context is preserved; only the report travels back.
- Memory moves minimally. The default after close is no state change. Only timeskips and off-scene events justify memory updates between episodes.
- Episode status lifecycle: `planned` → `shot` (after /and-shoot) → `complete` (after /and-wrap).
