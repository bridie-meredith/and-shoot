---
description: Stop the current pipeline, save a resume checkpoint, and print a clean "you are here" summary. Use before stepping back to revisit plans, wiping context, or ending a session mid-run. Usage: /and-cut
---

Pause the current pipeline. Read the cascade checkpoint (if a cascade is in flight), report position from showrunner memory, and print the resume command. Nothing is deleted.

`/and-cut` is non-destructive. It reads `staff/showrunner/memory.md` + `staff/showrunner/cascade-checkpoint.md` and prints "you are here." If a cascade is in-progress (`active.cascade_in_progress: true`), it annotates the existing checkpoint with `reason: halted-on-cut`. Otherwise it writes nothing besides the cut-log breadcrumb.

---

## Phase 1 — Survey state

Read `active-project/staff/showrunner/memory.md`. Extract:

- `active.book`
- `active.chapter`
- `active.cascade_in_progress`
- For the active chapter (if any): `books[<active.book>].chapters[<active.chapter>].status` (one of: `planned`, `bones-written`, `audited-r1`, `faceted-r2`, `stitched`).
- For the active book (if any): `books[<active.book>].orchestrator_critic_verdict` (if present).
- `project.series_audit.approved_at` + `project.series_audit.stale_since` (to detect pre-cast or post-cast position).

Then check the following files for existence:

| File | Meaning if present |
|------|--------------------|
| `active-project/staff/showrunner/cascade-checkpoint.md` | Cascade was invoked at some point (may or may not still be running) |
| `active-project/theater/bones/<book>-<chapter>.md` | Bones emitted for the active chapter |
| `active-project/theater/facets/scene-map-<book>-<chapter>.md` | `/and-write` Phase 7 scene-map facet present |
| `active-project/theater/facets/_cite-index.md` | `/and-facets` Phase 2 cite-index built |
| `active-project/draft/<book>-<chapter>.md` | `/and-stitch` Phase 8 draft emitted |

Derive `pipeline_position`:

- **pre-series** — `project.series_audit.approved_at` is missing. Next step: `/and-series`, `/and-substance series`, `/and-cast`.
- **pre-book** — series audit approved; no `books[<b>].chunk` populated. Next step: `/and-substance book b<NN>`.
- **pre-chapter** — book has `chunk` + `drama` + chapters[] populated; active chapter has no `pov_narrator` / `dramatic_shape` / `goal`. Next step: `/and-substance chapter b<NN>c<MM>`.
- **pre-write** — active chapter is `planned` (substance contract populated, no bones). Next step: `/and-write b<NN>c<MM>`.
- **pre-facets** — active chapter is `bones-written`. Next step: `/and-facets b<NN>c<MM>`.
- **pre-stitch** — active chapter is `audited-r1` or `faceted-r2`. Next step: `/and-stitch b<NN>c<MM>`.
- **chapter-complete** — active chapter is `stitched`. Next step: `/and-substance chapter b<NN>c<MM+1>` (or next book's c01 if last chapter in book).
- **book-complete** — every chapter under active book is `stitched`. Next step: `/and-review verdict b<NN>` (optional) → `/and-substance book b<NN+1>`.
- **cascade-in-progress** — `active.cascade_in_progress: true`. Position derived from `cascade-checkpoint.md` `last_completed` + `next` instead of the per-chapter status fields above.

---

## Phase 2 — Handle cascade-in-progress (if any)

If `active.cascade_in_progress: true`:

1. Read `staff/showrunner/cascade-checkpoint.md`. Validate it parses per the schema in `.claude/commands/and-substance.md § Cascade § Checkpoint`.
2. Update the checkpoint in place: set `reason: halted-on-cut`. Leave `last_completed` and `next` untouched (the cascade resumes from `next.command`).
3. The resume command is `/and-substance <cascade.root> --cascade --resume`.

If `active.cascade_in_progress: false`:

- No checkpoint mutation. Resume command is derived from `pipeline_position` directly (no `--cascade --resume` form needed).

---

## Phase 3 — Annotate showrunner memory

Append a `cut:` line to `active-project/staff/showrunner/memory.md` under a `# cut-log` section (create the section if it doesn't exist, at the very end of the file after `routing:`):

```
cut: <ISO date> — <pipeline_position> — book=<active.book> chapter=<active.chapter> cascade=<true|false>
```

Breadcrumb only. No state mutation.

---

## Phase 4 — Print summary

Print to the user:

```
--- CUT: <pipeline_position> ---

YOU ARE HERE
  book:    <active.book or "none">
  chapter: <active.chapter or "none"> (<status or "n/a">)
  cascade: <true | false>
  phase:   <pipeline_position>

IN-PROGRESS ARTIFACTS
  <list each existing file from the Phase 1 file table with a one-line status, or "none">

NEXT
  <single resume command line, e.g. "/and-substance chapter b01c02" or "/and-write b01c01">

[if cascade-in-progress, add:]
RESUME
  /and-substance <cascade.root> --cascade --resume
  Checkpoint: staff/showrunner/cascade-checkpoint.md (reason: halted-on-cut)

Context is safe to wipe. Run the NEXT (or RESUME) command above when you return.
```

---

## Notes

- `/and-cut` is non-destructive. It reads state, optionally annotates the cascade-checkpoint's `reason` field to `halted-on-cut`, and appends a breadcrumb to `memory.md` under `# cut-log`. Nothing else is mutated or deleted.
- It is safe to run at any pipeline position, including pre-series.
- The cut-log in `memory.md` accumulates across sessions. It is a breadcrumb trail, not state.
- To actually clear in-progress work (e.g. wipe bones + facets + draft to restart a chapter from scratch), the human or a targeted `revise` / `redo` re-run of the appropriate authoring command handles it. `/and-cut` only reports.
- A bare `cascade-checkpoint.md` (file exists but `active.cascade_in_progress: false` in memory) is a stale checkpoint from a prior, completed cascade. `/and-cut` reports it under IN-PROGRESS ARTIFACTS but does not mutate it.
