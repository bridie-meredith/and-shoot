# Parking-lot Schema

Cross-chunk watch-items that span multiple commands or chunks. Authored by any command body, auditor, fixer, or screen-writer when a finding's resolution belongs in a later run. Read by Phase 0 of every re-runnable command per CLAUDE.md Rule 14.

**File location.** `active-project/staff/showrunner/parking-lot.md`. One file per active project; git-tracked; append-only; resolution stamps add fields rather than delete entries (audit trail).

**Lifecycle.**
1. Authoring command appends an entry with `status: open` and `resolved_at: null`.
2. The targeted command's Phase 0 scans for items where `target` matches its invocation.
3. On successful resolution, the resolving command appends `resolved_at`, `resolved_by`, `resolution_note` and sets `status: resolved`.
4. Resolved items stay. Periodic compaction permitted but not required; never destructive.

---

## Format

```yaml
parking_lot:
  version: 1
  items:
    - id: pl-<YYYY-MM-DD>[-<label>]-<NNN>  # ISO date of creation + optional lowercase-hyphenated label (e.g. `cohere`) + 3-digit counter; uniqueness scoped to (date, label) pair
      created_at: <ISO timestamp>
      created_by: <command + phase>       # e.g. "/and-substance chapter b01c01 Phase 5 (fixer fault-001)"
      target:                             # who resolves
        command: <command-name>           # e.g. "/and-substance"
        scope: <invocation-slug or "*">   # e.g. "chapter b01c03"; "*" for any invocation of the command
        phase: <phase-id or null>         # e.g. "Phase 3"; null = any phase
      severity: HARD | SOFT               # HARD = target Phase 0 HARD-aborts if unresolved; SOFT = advisory, surfaced in Phase 7
      description: |
        <one paragraph; what needs to happen and why>
      context_refs:                       # paths or memory.md line references that establish provenance
        - <path or memory.md:LINE>
      status: open | resolved | dismissed
      resolved_at: <ISO timestamp> | null
      resolved_by: <command + phase> | null
      resolution_note: <one line> | null
```

---

## Field semantics

**`id`** — `pl-<YYYY-MM-DD>[-<label>]-<NNN>` where `<label>` is an OPTIONAL lowercase-hyphenated tag identifying the originating command or context (e.g. `cohere`, `write`, `substance`), and `<NNN>` is a 3-digit counter unique within the `(date, label)` pair — or within the day when no label is used. Stable forever — never reused even after resolution.

**`target.command`** — bare command name including leading slash (`/and-substance`, `/and-write`, etc.).

**`target.scope`** — invocation specifier the resolving command will match against:
- Specific: `chapter b01c03`, `book b01`, `b01c01` (for `/and-write`-style positional), `series`.
- Wildcard: `*` matches any invocation of the command.

**`target.phase`** — phase identifier (`Phase 0`, `Phase 3`, etc.) when resolution must happen in a specific phase. `null` allows any phase in the targeted invocation.

**`severity`**:
- **HARD** — Phase 0 of the matching invocation HARD-aborts with the item list unless that run resolves the item. Use when the missing work would corrupt downstream state.
- **SOFT** — surfaced in Phase 7 exit summary of the matching invocation; advisory, does not block. Use for taste-flags and quality watches that don't break correctness.

**`status`**:
- `open` — pending resolution.
- `resolved` — work completed; `resolved_at` + `resolved_by` + `resolution_note` stamped.
- `dismissed` — explicit "no longer applicable"; requires `resolution_note` naming the dismissal reason.

**`context_refs[]`** — paths or `memory.md:<line>` pointers establishing where the item originated. Reviewers should be able to reconstruct context from these refs without rereading session history.

---

## Matching rules (Phase 0 scan)

A command invocation `<command> <scope-args>` matches a parking-lot item iff:
1. `item.target.command == <command>` (exact match).
2. `item.target.scope == "*"` OR `item.target.scope` matches the invocation's scope spec (exact slug match; e.g. `chapter b01c03` matches `/and-substance chapter b01c03` but not `/and-substance chapter b01c04`).
3. `item.status == open`.

**Phase 0 surfaces matching items in its print block:**
- HARD items: list item id + description + resolving phase. The orchestrator MUST do this work this run; the named resolving phase is where the work lands.
- SOFT items: list item id + description. The orchestrator carries them to Phase 7 / final summary; non-blocking.

**When the HARD-abort fires.** Two cases:
1. **At resolving-phase completion.** If the named `target.phase` completes without stamping resolution on the matching HARD item, that phase HARD-aborts the run. The next re-run's Phase 0 finds the same HARD item still open and re-surfaces it.
2. **At final-summary time, when `target.phase` is null.** If no resolving phase was named, the run's final summary phase HARD-aborts if any matching HARD item is still open.

Phase 0 itself does NOT abort merely because matching HARD items exist — Phase 0 can't resolve future-phase work. Phase 0's job is surface + commit-to-resolve.

---

## Authoring discipline

- **Minimum viable item:** id, created_at, created_by, target, severity, description, status. Other fields default appropriately.
- **Specific over wildcard.** Prefer concrete `target.scope`. Wildcard is for genuinely cross-cutting concerns (e.g. "every `/and-write` run carries this prose watch").
- **HARD is rare.** Use HARD only when unresolved state would corrupt downstream artifacts. Default SOFT.
- **One item per atomic resolution.** If a finding needs work at two distinct downstream points, file two items.
- **Resolution is the resolver's job.** Authors do not pre-stamp resolutions. The resolving command stamps after the work lands.
