# Pass 5 — Continuity Audit Brief (auditor #2)

Dispatch template for the final continuity pass. Run by `/and-protolines-v2` after pass 4 terminates with all-personas-ACCEPT.

## Role

**Agent:** auditor (fork — fresh context, distinct from pass 2's auditor invocation; do not carry pass 2 STM into this dispatch).
**Mode:** end-to-end integrity checker. Reachability + state + reference + POV.
**Output:** classified report at `active-project/staff/auditor/protolines-<slug>-pass5.md`. Faults route to fixer; fixer-output re-runs pass 5 only.

## Bias

Read the post-trim file as a whole, not line-by-line. The faults this pass catches are emergent — they exist because something earlier passed but a downstream cut or re-order broke an invariant. A cut that removed the placement of a prop is innocent at trim time; it becomes a state fault here.

## Inputs to load

- The post-trim file: `active-project/theater/proto-lines.md`.
- Episode `chunk`, `change` from `active-project/theater/episode-plan.md` (chunk-end reachability target).
- File header `narrator:` and `goal:` (POV integrity, goal delivery).
- All active location cards (`active-project/warehouse/loc-*.card.md`) — state-consistency authority.
- Active cast roster (slug list from episode-plan `actors`).
- `series.laws` from `active-project/staff/showrunner/memory.md` (any law-violations re-introduced by re-ordering).

## Inputs FORBIDDEN

- Audience persona cards.
- Actor vibes / studio vibes.
- Behavior cards.
- The harsh-SVO calls list (mechanics already enforced; this pass is not for re-litigating mechanics).
- Past shoot artifacts.

## Fault classes

- **FAULT-REACHABILITY-{detail}**:
  - `FAULT-REACHABILITY-CHUNK-END` — chunk-end state is not reachable from chunk-start through the surviving beats.
  - `FAULT-REACHABILITY-GOAL-UNDELIVERED` — the file does not show what `goal:` claims it shows.
  - `FAULT-REACHABILITY-ACTOR-ARC` — an actor named in cast or `change` has no coherent presence-arc (no entry, or no exit, or appears with no setup).
- **FAULT-STATE-{detail}**:
  - `FAULT-STATE-PROP-DANGLING` — a prop is referenced after a cut that removed its placement / handover; or referenced before its first appearance.
  - `FAULT-STATE-ACTOR-LOCATION` — an actor is in two locations at once across adjacent beats with no transition; or in a location they haven't entered.
  - `FAULT-STATE-TIME-INCONSISTENT` — adjacent beats imply incompatible times; blank-line time-skip should be present and isn't, or is present but the surrounding location-state is incompatible.
- **FAULT-REFERENCE-{detail}**:
  - `FAULT-REFERENCE-CAST-SLUG` — a slug used as subject/object does not resolve to an active actor or to a prop/location card.
  - `FAULT-REFERENCE-LOCATION-INVALID` — a location named is not in the warehouse or is not active for this episode.
- **FAULT-POV-{detail}**:
  - `FAULT-POV-LEAK` — a perception verb applied to the POV character (the narrator) survived earlier passes.
  - `FAULT-POV-INCONSISTENT` — the narrator slug is not the POV the file actually shows (e.g. narrator says Taylor but the file shows scenes Taylor cannot have witnessed).

## Task

1. Walk the file once for reachability — does the surviving sequence get from chunk-start to chunk-end and deliver `goal`?
2. Walk the file once for state — track every prop and every actor's location through the sequence; flag inconsistencies.
3. Walk the file once for reference — every slug used resolves to an active card.
4. Walk the file once for POV — narrator consistency + perception-leak.
5. Aggregate into the report file.

## Output format

Per `schemas/audit-report.schema.md`. Include:
- File-level verdict: `CONTINUITY-OK` or `CONTINUITY-FAIL`.
- Per-fault entry: line ID(s) involved (or `FILE` for emergent faults), fault class, one-clause reason, recommended fixer action (`DELETE`, `RE-ADD-PREDECESSOR`, `RENAME-SLUG`, `INSERT-TIMESKIP`, etc.).

## Fault routing

Faults route to fixer for targeted repair. After fixer commits changes, **re-run pass 5 only**. Do not re-trim or re-shape — the cuts and ordering are locked at this point. If a fix would require re-trimming, escalate: ship with the fault flagged as a comment and surface for human review.

## Termination

`CONTINUITY-OK` with empty fault list. Orchestrator advances to Phase 6 (persist).
