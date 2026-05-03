---
description: Wrap a completed shoot: dramatist structure review and scene boundary flagging, audience entertainment pass, auditor constraints audit, fixer, editor final draft. Reads the active episode from showrunner memory. Run after /and-shoot. Usage: /and-wrap [episode-slug]
---

Takes the raw show file from a completed shoot and produces a final manuscript in `active-project/polish/`. Requires the episode to be in `shot` status. Run `/and-shoot` first.

## Args

- `$1` — optional episode slug. If omitted, wraps the episode currently marked active in `active-project/staff/showrunner/memory.md`. If provided, must match a slug whose status is `shot`.

---

## Phase 1 — Validate

Read `active-project/staff/showrunner/memory.md`. Confirm:
- `active.episode` is set (or matches `$1` if provided)
- The episode's status is `shot` — not `planned`, not `complete`
- `active-project/theater/show.md` exists and is non-empty
- `active-project/theater/episode-plan.md` exists (auditor needs it)

If any check fails, print the problem and stop.

Also check: if any wrap log files already exist (`active-project/theater/wrap-structure-log.md` or `active-project/theater/wrap-audience-log.md`), stop and print:
```
Wrap log files already exist — wrap may have been interrupted mid-run.
Review the existing logs to see how far wrap progressed.
Delete wrap-structure-log.md and wrap-audience-log.md manually to restart, then re-run /and-wrap.
```

---

## Phase 2 — Dispatch showrunner

Dispatch showrunner as a subagent. It runs the full wrap pipeline agent-to-agent with no further input from this command.

**Prompt to showrunner:**

> Read `active-project/staff/showrunner/memory.md` before proceeding. That is your working state.
>
> Also read `active-project/theater/episode-plan.md` and `active-project/theater/show.md`. Both must be in context before wrap begins.
>
> The active episode is `<episode-slug>`. Run the wrap pipeline below. At each step that dispatches a subagent, record the result in the log file for that step before continuing. A missing log file means the step did not run.
>
> ---
>
> ## STEP 1 — Dramatist: structure review
>
> Dispatch dramatist with the completed show file and the episode plan. Dramatist checks four thresholds:
> - **Problem solves:** the episode's central problem reaches resolution (even if partial or pyrrhic)
> - **End state ≠ start state:** at least one meaningful thing has changed — character, relationship, situation, world
> - **Builds toward season finale:** the episode advances or complicates the season arc
> - **Builds toward series finale:** the episode is legible in terms of the long game
>
> **Log file: `active-project/theater/wrap-structure-log.md`**
> ```
> problem solves: pass/fail — <one line>
> end state delta: pass/fail — <one line>
> season build: pass/fail — <one line>
> series build: pass/fail — <one line>
> overall: pass / flagged
> [if flagged: disposition — patched at episode scope / escalated to showrunner]
> ```
>
> Threshold failures:
> - Minor (a line or scene can patch it) → dispatch fixer with target and reason. Note in log.
> - Structural (requires replanning) → flag for escalation. Note in log. Do not block wrap — continue to step 2 and return the escalation at the end.
>
> ---
>
> ## STEP 2 — Dramatist: scene boundary flagging
>
> Dramatist marks the show file in-place:
> - `[scene-start: <label>]` at the opening of each scene
> - `[scene-end: <label>]` at the close of each scene
>
> Everything inside the flags is episode content — kept, edited, published. Everything outside (pre-scene warmup, post-scene trailing) is cut by the editor. The flags themselves are not cut.
>
> No separate log file for this step. The flags in the show file are the record.
>
> ---
>
> ## STEP 3 — Audience: entertainment review
>
> Dispatch all three audience agents to read the flagged show file in full. Each identifies:
> - Lines that land flat or feel inert
> - Moments that break immersion or feel out of register with the vibe-cloud
> - Any exchanges that are actively bad — confusing, boring, false to character
>
> Each audience agent marks qualifying lines in the show file as `[⚑ audience: <slug>: <reason>]`.
>
> **Log file: `active-project/theater/wrap-audience-log.md`**
> ```
> # Audience Wrap Review — <episode-slug>
> cape-fic-reader: <N flags> — <summary of concerns, or "no flags">
> worm-canon-pedant: <N flags> — <summary of concerns, or "no flags">
> dark-fantasy-reader: <N flags> — <summary of concerns, or "no flags">
> lines patched by fixer now: <list or "none">
> lines carried to editor: <list or "none">
> ```
>
> Showrunner decides whether to dispatch fixer for flagged lines now or pass them to editor as advisory. Default: carry to editor unless the flag identifies something that will confuse continuity.
>
> ---
>
> ## STEP 4 — Auditor: constraints audit
>
> Dispatch auditor (fork) with:
> - The flagged show file (`active-project/theater/show.md`)
> - All active constraint cards (`active-project/warehouse/constraint-*.card.md`)
> - The episode plan (`active-project/theater/episode-plan.md`)
> - The studio state file (`active-project/staff/studio/state.md`)
> - Actor state files for all characters active this episode (`active-project/actors/<slug>/state.md`)
>
> Auditor checks: law/lore/behavior compliance, show-file-vs-plan drift, state consistency (does the show file reflect what state records say happened?).
>
> **Log file: `active-project/staff/auditor/<episode-slug>-wrap-audit.md`**
> Full classified report (schema: `schemas/audit-report.schema.md`). A clean pass still produces a report — existence proves the check ran.
>
> Route faults to fixer with scope and reason. Escalate only what cannot be resolved at episode scope.
>
> ---
>
> ## STEP 5 — Editor: final draft
>
> Dispatch editor with the fully flagged show file. The editor receives:
> - `active-project/theater/show.md` (with scene markers, needs-edit markers, and audience flags all present)
> - `active-project/staff/auditor/<episode-slug>-wrap-audit.md` (advisory flags from auditor)
>
> Editor:
> - Applies scene boundary cuts: removes content outside `[scene-start]` / `[scene-end]` flags; keeps the flags as context markers
> - Addresses `[⚑ needs edit]` lines from three-try failures
> - Considers `[⚑ audience]` flags — rewrites where warranted, leaves where the flag is overcautious
> - Prose pass: economy, continuity, tense, blocking, voice consistency
>
> Editor saves the final draft to `active-project/polish/<episode-slug>.md`.
>
> Editor does not add content. Editor does not make plot decisions.
>
> ---
>
> ## STEP 6 — Memory: minimal movement
>
> After the editor completes:
> 1. Mark episode status `complete` in `active-project/staff/showrunner/memory.md`.
> 2. Advance `active.episode` to the next planned episode in the season, if one exists. If the season is complete, set `active.episode` to `~` and note the season close.
> 3. **Timeskip check:** if the next episode picks up significantly later in time, update affected actor state files (`active-project/actors/<slug>/state.md`) and studio state (`active-project/staff/studio/state.md`) to reflect what changed during the gap.
> 4. **Off-scene event check:** if something significant happened off-screen between episodes, record it in the relevant actor LTMs and append to `active-project/staff/showrunner/world-notes.md`.
> 5. Default: no timeskip, no off-scene event → memory stays exactly where the show file left it. Do not advance state without a reason.
>
> ---
>
> ## RETURN TO CALLER
>
> Return concise summary (no transcripts, no deliberation):
> - Episode slug and title
> - Structure review: pass or flagged thresholds (one line each if flagged)
> - Audience flags: count per persona; any patched by fixer
> - Auditor: pass / faults (count and scope) / escalations
> - Final draft path
> - Next active episode (if any)
> - Any escalations requiring human decision
> - Log files written (list of paths)

---

## On return

Take showrunner's return. Present it to the human.

```
--- WRAP COMPLETE: <episode-slug> ---

STRUCTURE
  pass  [or: flagged — <threshold>: <one line>]

AUDIENCE FLAGS
  cape-fic-reader: N | worm-canon-pedant: N | dark-fantasy-reader: N
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

If showrunner returned escalations, present them before the closing line with: `ESCALATIONS REQUIRING YOUR DECISION:` followed by each one.

---

## Notes

- Wrap requires episode status `shot`. It will not run on a `planned` episode.
- Scene boundary flags are written in-place to the show file by the dramatist. The editor reads the marked-up file — it does not re-flag.
- Audience agents in wrap read the full episode, not individual lines. This is a different task from their per-line shoot role.
- The auditor is a fork — showrunner context is preserved; only the report travels back.
- Memory moves minimally. The default after close is no state change. Only timeskips and off-scene events justify memory updates between episodes.
- Episode status lifecycle: `planned` → `shot` (after /and-shoot) → `complete` (after /and-wrap).
