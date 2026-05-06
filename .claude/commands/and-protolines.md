---
description: Expand the active episode chunk into a proto-line file (SVO bones). First phase of the shoot-v2 chain. Output - active-project/theater/proto-lines.md. Usage - /and-protolines [episode-slug]
---

First phase of the shoot-v2 chain. Replaces `/and-shoot` Phase A (which is now archived under `archive/commands/`).

Takes the active episode's chunk statement and produces a clean proto-line file: SVO bones only, no modifiers, no interiority, no dialogue content. Dialogue beats are recorded as `<speaker> speaks to <listener>` proto-lines that will later be cited by the per-character dialogue files.

You are the orchestrator. You dispatch screen-writer, audience, and dramatist directly. Do not dispatch showrunner — showrunner is read-only memory holder.

**All dispatches use the Agent tool.** Inline generation does not honor role isolation.

## Args

- `$1` — optional. Episode slug (e.g. `s01e07`). If omitted, use `active.episode` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate

1. Resolve episode slug (arg or `active.episode`).
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - The episode appears in the active season's episode list.
   - Its chunk statement is present.
   - Its status is `planned` (not `shot`, not `wrapped`).
3. Confirm `active-project/theater/proto-lines.md` does **not** already exist for this episode. If it does, abort with the path printed — proto-line generation is one-shot per episode. To re-author, archive the existing file first.
4. Confirm `cards/dialects/INDEX.md` exists (the behavior-card library lives there; the path is named `dialects/` for legacy reasons but the cards are `class: behavior`. Required for downstream phases; this command does not author behavior cards but the chain depends on them).

Print:
```
Episode: <slug>
Chunk: <chunk statement>
Beginning proto-line authoring.
```

---

## Phase 1 — Initial proto-line draft

Dispatch **screen-writer** with:
- The episode chunk statement (verbatim from season plan).
- The active series and season constraints from `active-project/staff/showrunner/memory.md`.
- The active cast roster (actor slugs).
- The schema reference: `schemas/proto-line.schema.md`.
- The series and season vibe-clouds for tonal grounding.

Screen-writer's task:
- Expand the chunk into a sequence of proto-lines per `schemas/proto-line.schema.md`.
- **SVO discipline is the entire point.** No fragments, no modifiers, no interiority, no dialogue content. Speaking beats render as `<speaker> speaks to <listener>` with no further detail.
- Each beat is one thing that happens. Compound actions split into multiple proto-lines.
- IDs assigned monotonically from 1.
- Citations may be left empty in the initial draft — they get attached when downstream artifacts (location-state, dialogue, facets) are authored. The exception: if a beat is fundamentally about an environment change, screen-writer may insert a `[loc-state:?]` placeholder citation, to be resolved when location-state is authored.

Output: `active-project/theater/proto-lines.md`.

---

## Phase 2 — Multi-pass review

Five passes, each with a specific lens. Default order, runnable in sequence:

### Pass A — delete

Dispatch the three audience personas in parallel. Each reads the full proto-line file and proposes deletions: weak SVOs, redundant beats, beats that don't serve the chunk. Audience writes proposals; you (orchestrator) merge — a deletion proposed by ≥2 personas is accepted automatically; one-persona proposals are accepted unless screen-writer flags them as load-bearing.

Apply deletions by removing entire lines from `proto-lines.md`. **Do not renumber.** Gaps in IDs are intentional.

### Pass B — re-arrange

Dispatch **dramatist** with the surviving proto-line file. Dramatist proposes re-ordering for dramatic shape — compression, escalation, beat sequencing. Dramatist outputs a new ID order list (e.g. `1, 4, 2, 3, 7, 9`).

Apply by re-ordering lines in the file according to the new sequence. **IDs do not change.** The file's line order changes; the IDs stay attached to their proto-lines.

### Pass C — constraint-check

Dispatch **auditor** (fork) with the proto-line file and the active constraint cards. Auditor returns a classified report at `active-project/staff/auditor/protolines-<slug>-audit.md` per `schemas/audit-report.schema.md`. Faults route to **fixer**, which makes the minimum change required (typically: deleting offending proto-lines or splitting compound ones). Fixer logs to `active-project/staff/fixer/fixer-log.md`.

### Pass D — behavior-check

Dispatch **dramatist** again, this time with the cast cards and the proto-line file. Dramatist checks: does each subject act in character? Are any verbs untrue to the actor's voice and tier? Output: a list of suspect proto-line IDs with one-line concerns.

For each flagged proto-line, you (orchestrator) decide: delete or accept. Behavior calls have no automatic deletion threshold — they require taste. Log each decision to `active-project/staff/showrunner/protolines-<slug>-log.md` (append-only).

### Pass E — entertainment-check

Dispatch the three audience personas again (parallel). Each reads the post-pass-D file and verdicts accept/revise per persona, with one-clause feedback per revise.

If all three accept: phase 2 terminates.
If any revise: feed the feedback to screen-writer for a delete-only revision, then re-run Pass E. Maximum two revise rounds; on the third the file ships with audience flags annotated as comments at end of file.

---

## Phase 3 — Termination

Phase 2 terminates when **two consecutive passes (any combination of A–E) produce no changes** — the file has converged.

A pass that produces a change resets the convergence counter. A pass that produces no changes increments it. Two zero-change passes in a row = terminated.

If convergence is not reached after **15 total passes**, ship the current file with a header comment noting non-convergence. Flag for human review.

---

## Phase 4 — Persist

1. Confirm `active-project/theater/proto-lines.md` is final.
2. Update `active-project/staff/showrunner/memory.md`:
   - Episode status: `planned` → `protolined`.
   - Add a `protolines` field under the episode entry pointing at the file.
3. Print summary:

```
--- PROTO-LINES COMPLETE: <episode-slug> ---

Total proto-lines: <count>
Deleted during review: <count>
Re-arrangements: <count>
Convergence: <pass count>

File: active-project/theater/proto-lines.md
Log:  active-project/staff/showrunner/protolines-<slug>-log.md

Next: /and-locstate (location-state facet) or /and-dialogue (per-character dialogue forks).
```

---

## Notes

- This command does **not** author location-state, dialogue, or any other facet. Those are downstream commands. Citations in proto-lines are left as placeholders or empty until those phases run.
- Proto-line IDs are stable from the moment they are first assigned. Re-running this command for the same episode is not supported — archive the existing file first if you need to re-author.
- Audience and dramatist are stateful between passes. Their STM should be loaded at each dispatch and updated after each verdict, same protocol as in `/and-project` planning phases.
