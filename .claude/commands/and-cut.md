---
description: Stop the current pipeline, save a resume checkpoint, and print a clean "you are here" summary. Use before stepping back to revisit plans, wiping context, or ending a session mid-run. Usage: /and-cut
---

Pause the current pipeline. Write a resume checkpoint. Print state. Nothing is deleted.

---

## Phase 1 — Survey state

Read `active-project/staff/showrunner/memory.md`.

Then check the following files for existence and content:

| File | Meaning if present |
|------|--------------------|
| `active-project/theater/show.md` | Shoot in progress or complete |
| `active-project/theater/shoot-log.md` | Shoot log — how far through bullets |
| `active-project/theater/episode-plan.md` | Plan complete |
| `active-project/theater/episode-plan-log.md` | Plan review ran |
| `active-project/theater/wrap-structure-log.md` | Wrap started — structure step ran |
| `active-project/theater/wrap-audience-log.md` | Wrap started — audience step ran |
| `active-project/staff/auditor/<episode-slug>-wrap-audit.md` | Auditor step ran |
| `active-project/polish/<episode-slug>.md` | Wrap complete — final draft exists |

Derive current pipeline position:

- **between-episodes** — active episode is `complete`; next episode is `planned`; no in-progress theater files for the next episode
- **pre-shoot** — active episode is `planned`; no show.md or show.md is header-only (≤ 4 lines)
- **mid-shoot** — active episode is `planned`; show.md has content beyond the header; no wrap logs present
- **shoot-complete** — active episode is `shot`; show.md has content; no wrap logs present
- **mid-wrap** — active episode is `shot`; one or more wrap logs exist but polish file does not
- **wrap-complete** — active episode is `complete`; polish file exists

---

## Phase 2 — Write checkpoint

Write `active-project/staff/showrunner/cut-state.md`:

```markdown
# cut-state — <ISO date>

## Position
pipeline_phase: <between-episodes | pre-shoot | mid-shoot | shoot-complete | mid-wrap | wrap-complete>
active_season: <slug>
active_episode: <slug>
episode_status: <planned | shot | complete>

## In-progress files
<list each theater/ file that exists with a one-line status, e.g.:>
- show.md: present — <line count> lines
- shoot-log.md: present — bullet N of M complete
- wrap-structure-log.md: present
- [none]

## Resume instructions
<one of the blocks below, selected by pipeline_phase>
```

Resume instructions by phase:

**between-episodes:**
```
Next: /and-shoot  (begins s<NN>e<NN>)
Nothing in progress. Clean cut.
```

**pre-shoot:**
```
Next: /and-shoot  (plan not yet started or header-only)
Nothing to recover.
```

**mid-shoot:**
```
Next: review show.md to find last completed bullet, then either:
  (a) continue: re-run /and-shoot — it will detect show.md has content and stop; delete show.md + shoot-log.md manually to restart from scratch
  (b) abandon and restart: delete active-project/theater/show.md and active-project/theater/shoot-log.md, then re-run /and-shoot
```

**shoot-complete:**
```
Next: /and-wrap
Shoot is done. Run wrap to close the episode.
```

**mid-wrap:**
```
Next: /and-wrap — but check existing wrap logs first.
Wrap logs already exist. If wrap was interrupted, delete wrap-structure-log.md and wrap-audience-log.md manually, then re-run /and-wrap.
```

**wrap-complete:**
```
Wrap is done. Final draft at active-project/polish/<slug>.md.
Next: /and-shoot  (begins next episode)
```

---

## Phase 3 — Annotate showrunner memory

Append a `cut:` line to `active-project/staff/showrunner/memory.md` under a `# cut-log` section (create the section if it doesn't exist):

```
cut: <ISO date> — <pipeline_phase> — <active_episode>
```

This leaves a breadcrumb in the memory file without disrupting any existing fields.

---

## Phase 4 — Print summary

Print to the user:

```
--- CUT: <pipeline_phase> ---

YOU ARE HERE
  season:  <slug>
  episode: <slug> (<status>)
  phase:   <pipeline_phase>

IN-PROGRESS FILES
  <list or "none">

TO RESUME
  <resume instructions from checkpoint, verbatim>

Checkpoint saved: active-project/staff/showrunner/cut-state.md
Context is safe to wipe. Run the resume command above when you return.
```

---

## Notes

- `/and-cut` is non-destructive. It reads state and writes a checkpoint. Nothing is deleted or modified except the cut-log annotation in memory.md.
- It is safe to run at any point in the pipeline, including between episodes.
- The cut-state.md file is overwritten each time `/and-cut` runs. Only the most recent cut is kept.
- To actually clear in-progress work (restart a shoot from scratch), the human must delete the relevant files manually. `/and-cut` tells them exactly which files and why — it does not delete anything itself.
- The cut-log in memory.md accumulates across sessions. It is a breadcrumb trail, not state.
