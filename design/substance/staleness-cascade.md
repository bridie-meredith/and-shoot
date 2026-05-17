# Staleness Cascade — Surfacing Protocol

When a re-run mutates an upstream artifact, downstream work derived from that artifact may be left silently outdated. This doc defines the cascade detection, surfacing, and resolution protocol shared by all re-runnable commands.

Referenced from `/and-series`, `/and-substance`, `/and-cast`, `/and-write`, `/and-review verdict`.

---

## Surfacing — defined

When Phase 0 of a re-runnable command detects downstream work that depends on the about-to-change output, "surface" means:

1. **Print a numbered list** of the affected downstream artifacts (chunks, bones files, verdict blocks) with their slugs and last-write timestamps.
2. **Prompt the user** to choose one of:
   - `mark-stale` (default) — write `stale_since: <iso-timestamp>` on each affected downstream block; leave content intact.
   - `keep-fresh` — leave staleness fields null; user accepts that downstream may be silently outdated.
   - `abort` — cancel the re-run.
3. **Record the choice** in `staff/showrunner/staleness-log.md` — one entry per cascade event: who-ran-what, what was marked, user choice, timestamp.

---

## Staleness cascade — per-level rules

| Re-run at | Stale-marks |
|---|---|
| `/and-series revise/redo` | All `books[*]` blocks (entire series-substance refresh invalidates downstream chunks) + `project.series_audit` |
| `/and-substance series redo` | All `books[*]` blocks downstream + `project.series_audit` |
| `/and-substance series revise` | Only the affected book blocks if individual book chunks change; whole series otherwise |
| `/and-substance book b01 redo` | All `chapters[*]` under `b01` + `books[b01].orchestrator_critic_verdict` if set |
| `/and-substance book b01 revise` | Affected chapter blocks under b01 + verdict if substance-relevant |
| `/and-substance chapter b01c01 redo` | All `scenes[*]` under b01c01 + `chapters[b01c01]` downstream artifacts (bones file, facet outputs, draft) + `books[b01].orchestrator_critic_verdict` if set |
| `/and-substance chapter b01c01 revise` | Affected scenes + downstream artifacts |
| `/and-cast revise/redo` | `project.series_audit` (any cast change invalidates the audit checkpoint) |
| `/and-write b01c01 redo` | Per-chapter facet outputs + `draft/b01-c01.md` + `draft/b01-c01.annotated.md` + `books[b01].orchestrator_critic_verdict` if set |
| `/and-write b01c01 revise` (partial) | Same as redo — bone-level Δ propagates non-locally through facet citation accrual; status drops to `bones-written` regardless of partial scope |
| `/and-facets b01c01 revise/redo` | `draft/b01-c01.md` + `draft/b01-c01.annotated.md` |
| `/and-stitch b01c01` re-run | No downstream — stitcher is the terminal command under the polish-deferred chain |

---

## Downstream behavior on stale parents

When a downstream command next runs and reads a parent block with `stale_since` set:

- **Default:** print a warning line ("parent `<slug>` stale since `<timestamp>`; consider re-running parent first") but do NOT block. Stale-marking is informational, not enforcing.
- **Exception — `/and-review verdict`:** if any block under the book is stale and the verdict itself is stale, the verdict subcommand warns and offers to re-fire. The verdict's own `stale_since` clears on PASS/PASS-WITH-NOTES/FAIL re-issue.
- **Exception — `project.series_audit.stale_since`:** if set, `/and-substance book b<NN>` Phase 0 HARD-aborts on any new book invocation. The series-audit checkpoint must be re-approved (`/and-cast` Phase 5 again) before downstream can re-run.

---

## Status state-machine reset on re-run

Re-running a command in `revise`/`redo` mode resets `chapters[].status` to the earliest value that command owns. Downstream status moves are invalidated; downstream artifacts are stale-marked.

| Re-running | Resets `chapters[].status` to |
|---|---|
| `/and-substance book` | `planned` |
| `/and-substance chapter` | `scened` |
| `/and-write` | `bones-written` (after Phase 7 success) |
| `/and-facets` | `bones-written` (then advances to `audited-r1` etc. as phases complete) |
| `/and-stitch` | `audited-r1` or `faceted-r2` (whichever was last reached before stitch ran), then `stitched` on completion |

Status only ever moves forward within a fresh authoring pass. The reset is recorded in `staff/showrunner/staleness-log.md` alongside the cascade entry.

---

## Cascade-checkpoint interaction

`/and-substance --cascade` writes `staff/showrunner/cascade-checkpoint.md` after each child chunk completes. When `--resume` is invoked, Phase 0 validates the checkpoint against current `stale_since` fields:

- If the checkpoint is older than the root's `stale_since`, warn and prompt `--resume` (continue from `next.command` despite staleness) vs. `--restart` (discard checkpoint, run from the beginning). Default action is to warn and wait for user pick — do NOT auto-restart, since the user may want to push through a staleness mark deliberately.

See `rerun-protocol.md` for the cascade-checkpoint payload schema.

---

## Staleness-log format

`active-project/staff/showrunner/staleness-log.md`:

```yaml
# Staleness log — one entry per cascade event
- timestamp: 2026-05-17T14:23:11Z
  command: /and-substance book b01 redo
  invoked_by: user
  marked_stale:
    - block: chapters[b01c01]
      reason: parent redo
    - block: chapters[b01c02]
      reason: parent redo
    - block: theater/bones/b01-c01.md
      reason: parent redo (bones file derives from chapters[].scenes[].bones[])
    - block: books[b01].orchestrator_critic_verdict
      reason: substance under verdict was re-authored
  user_choice: mark-stale
```

`keep-fresh` and `abort` choices are logged with `marked_stale: []` and a `note:` field explaining the user's intent.
