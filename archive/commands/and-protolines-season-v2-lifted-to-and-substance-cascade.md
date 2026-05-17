---
description: Run /and-protolines-v2 across every planned episode in the active season. Two modes - sequential (default, safe) and parallel (faster, requires per-episode output paths). Usage - /and-protolines-season-v2 [season-slug] [--parallel]
---

Season-scope chain wrapper around `/and-protolines-v2`. Drafts proto-lines files for every episode in the named (or active) season that has status `planned`.

## Args

- `$1` — optional. Season slug (e.g. `s01`). If omitted, use `active.season` from `active-project/staff/showrunner/memory.md`.
- `$2` — optional flag. `--parallel` to fan out all episodes simultaneously. Default is sequential.

---

## Phase 0 — Validate

1. Resolve season slug.
2. Read `active-project/staff/showrunner/memory.md`. Confirm:
   - Named season exists in `seasons[]`.
   - Each episode under that season has a chunk statement + status field.
   - `seasons[<slug>].status` is `active` (not `wrapped`).
3. Build the work list: `[ep for ep in season.episodes if ep.status == "planned"]`. If list is empty, abort with `No planned episodes; nothing to draft.`
4. Resolve output path convention. Per-episode files at `active-project/theater/proto-lines/<slug>.md`. If `active-project/theater/proto-lines.md` (singular path) exists, abort with the path printed and a note that it must be moved to the per-episode subdir before season-chain can run.
5. Confirm `cards/dialects/INDEX.md` exists.

Print:
```
Season: <slug>
Episodes to draft: <comma-separated slug list>
Mode: <sequential | parallel>
Beginning season-chain.
```

---

## Phase 1 — Per-episode dispatch

### Sequential mode (default)

For each episode in the work list, in order:

1. Update `active.episode` in showrunner memory (writes through showrunner agent, not direct).
2. Invoke `/and-protolines-v2 <slug>` and wait for completion. The v2 command runs its own five-pass pipeline; this command does not re-implement the passes.
3. On completion: confirm output exists at `active-project/theater/proto-lines/<slug>.md`. Confirm episode status is `protolined` in showrunner memory.
4. Append to season-chain log: `<slug> | <pipeline iterations to converge> | <pass-2-final-accept-rate> | <pass-5-verdict>`.
5. If the pipeline failed to converge (status remains `planned` after 3 internal iterations), halt the chain and surface the episode for human review. Do NOT continue to subsequent episodes — cross-episode drift is more dangerous than partial progress.

### Parallel mode (--parallel)

1. For each episode in the work list, dispatch `/and-protolines-v2 <slug>` as a background agent. All dispatches fire simultaneously.
2. Wait for all dispatches to return.
3. Aggregate per-episode results into the season-chain log.
4. Audience STM is **not** carried between episodes in parallel mode — each persona starts each dispatch from the season-open STM state. Document in the log if persona STM divergence is detected.

**Risk acknowledgement for parallel mode:** episodes are dispatched as independent units, but the season's escalation spine ties them together. Cross-episode drift (e.g., a state-change in episode 2 that contradicts episode 3's chunk-start assumption) is detectable only at the cross-season pass below. Use parallel only when wall time matters more than first-pass coherence.

---

## Phase 2 — Cross-episode reachability check

After all episodes have individually converged (all five per-episode passes clean), run a single cross-episode reachability audit.

Dispatch **auditor** (fork) with:
- All per-episode proto-lines files (`active-project/theater/proto-lines/<slug>.md` × N).
- Each episode's `chunk` and `change` from `episode-plan.md`.
- Season escalation spine from `season-<slug>-plan.md`.
- Series laws from showrunner memory.

Auditor's task:
- For each adjacent episode pair (N, N+1), verify that episode N's chunk-end state is consistent with episode N+1's chunk-start state. Specifically: actor locations at end of N must reach the cast roster at start of N+1; props in actor inventories must persist or be released; world-state changes (e.g. a registration entered) must propagate.
- Report any seams where episode boundaries leak inconsistent state.

Output: `active-project/staff/auditor/protolines-season-<slug>-cross-episode.md`.

Faults route to fixer with episode-pair scope. A cross-episode fault may require revising one or both adjacent files; this is the only place season-chain modifies a converged per-episode file.

---

## Phase 3 — Persist

1. Update `active-project/staff/showrunner/memory.md`:
   - For each episode: status `planned` → `protolined`.
   - Add `protolines: active-project/theater/proto-lines/<slug>.md` per episode.
   - Add a `season.protolines_complete` field at season scope with timestamp.
2. Print summary:

```
--- SEASON PROTO-LINES COMPLETE: <season-slug> ---

Episodes drafted: <list>
Total proto-lines authored (across all episodes): <count>
Total time-skips: <count>
Total deletions: <count>

Per-episode trajectory:
  <slug> | <iterations> | <pass-2-final> | <verdict>
  ...

Cross-episode reachability: <CLEAN | <fault count>>

Files:
  active-project/theater/proto-lines/<slug>.md (× N)
  active-project/staff/auditor/protolines-season-<slug>-cross-episode.md

Next: facet authoring per episode (/and-locstate, /and-dialogue, etc.) or season-wrap (/and-wrap).
```

---

## Notes

- This command **does not modify** `/and-protolines-v2` itself. It is a thin chain wrapper that loops or fans out the per-episode command.
- Cross-episode reachability is intentionally *post-convergence*. Catching cross-episode seams during per-episode authoring would require each episode's writer to load adjacent episodes' proto-lines, which violates the blind-to-past-shoot-artifacts rule. The post-convergence check accepts the seam-discovery cost in exchange for keeping the writer contract clean.
- Sequential mode is the recommended first-time-on-a-season default. Parallel mode is for re-runs after a season's structure is known stable.
- This command is gated on the per-episode output path convention (`active-project/theater/proto-lines/<slug>.md`). A schema update formalizing this path is a prerequisite — until the schema lands, `and-protolines-season-v2` aborts at Phase 0 step 4.
