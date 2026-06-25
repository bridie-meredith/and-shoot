---
description: Iterate-to-best loop. Given a one-line story/series prompt and a max iteration count, generate a summary then loop[independent harsh critic -> fresh reviser] up to N times, returning the full history (best assumed = last). Usage - /iterate-to-best "<prompt>" [N] [story|series]
---

Run the **iterate-to-best loop** at `pitch-lab/iterate-to-best/iterate-to-best.workflow.js`.

This command is a thin wrapper: it parses your arguments and invokes the workflow. The mechanism, rubric, and lessons live in the script + `pitch-lab/iterate-to-best/README.md`; do not re-implement them here.

## Args

Parse `$ARGUMENTS`:
- **prompt** (required) — the quoted one-line story or series prompt. If unquoted, take the whole argument string up to a trailing integer/mode token.
- **N** (optional integer, default `3`) — maximum iterations.
- **mode** (optional, `story` | `series`, default `story`) — `series` produces a multi-book arc summary.

If no prompt is given, do NOT guess — ask the user (or admin user-proxy per CLAUDE.md Rule 13 during an unattended run) for the one-line prompt.

## Execution

1. Invoke the workflow:
   ```
   Workflow({
     scriptPath: "pitch-lab/iterate-to-best/iterate-to-best.workflow.js",
     args: { prompt: "<parsed prompt>", mode: "<story|series>", maxIterations: <N> }
   })
   ```
   The workflow runs in the background and returns when done. It is multi-agent orchestration; this command body IS the explicit opt-in for invoking the Workflow tool.
2. When it completes, read the returned object's `trajectory` + `finalBand`/`finalTotal`, and confirm the full per-iteration history was persisted to `pitch-lab/iterate-to-best/demo-run.md` (the script writes it via a final agent — verify the file exists per CLAUDE.md Rule 19; if absent, persist from the returned object).
3. Report to the user: the band/score trajectory, the final summary's band, and the path to the persisted history. Flag the `best = last` caveat if the final score is below an earlier iteration's peak (PI-19) — name the higher-scored iteration.

## Notes

- Each fork (generator / critic / reviser) is a fresh independent subagent; the critic self-escalates its bar each iteration. See `pitch-lab/reviewer-spec.md` (10-criterion brutal rubric) and `pitch-lab/generator-spec.md` (GEN-v2 rules) for what the forks enforce.
- This iterate-to-best loop improves ONE summary. Field-level faults (formula sameness, range deficit) need the non-blind field-critic across many prompts — out of scope for this command.
- Re-running the same prompt + args against an existing run id can resume from cache: `Workflow({ scriptPath, resumeFromRunId, args })`.
