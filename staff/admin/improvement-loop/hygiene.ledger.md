# improvement-loop / hygiene ledger

Append-only. Each pass appends one dated block. Format: date, branch, sweep summary, severity-ordered findings, action taken.

---

## 2026-06-12 — branch claude/gifted-hawking-1aq2au

**Scope swept:** active-project/staff/showrunner/ (parking lot, draft stragglers, ledger gaps),
active-project/theater/ (facets, bones coverage), active-project/warehouse/ (pre-version files),
cards/locations/INDEX.md (index drift check), staff/admin/ (STM bloat check).

**Context:** Project `taylor-westeros-good-intentions` is COMPLETE (ARCHIVE_NOTE 2026-06-07;
verdict PASS-WITH-NOTES 2026-06-06). active-project/ is the completed book archive in-place
(migration to projects/ not yet executed).

---

### Findings (severity order)

**1. MEDIUM — Stale HARD parking-lot item after book-close.**
`pl-2026-06-04-c16-001` (`depth-pass-mandatory-b01c16`) carries `status: open` and `severity:
HARD`. Its description explicitly gates `/and-review verdict b01`. But the verdict was issued
2026-06-06 and the project was archived 2026-06-07, while this item is still open. Either the
depth-pass was executed but never stamped, or the gate was bypassed via a decision not recorded
in the parking lot. A HARD item that gated a delivered milestone and was never resolved or
overridden is a state inconsistency in the append-only tracking system.
→ **Route: oskar.** Needs a resolution stamp (resolved_at + resolved_by + resolution_note) or an
explicit admin decision recording that the gate was bypassed.

**2. MEDIUM — 7 draft files stranded in showrunner root (not in `_drafts/`).**
Files: `b01c09-bones-draft-2026-05-31.md`, `b01c11-bones-draft.md`, `b01c11-draft.md`,
`b01c15-bones-draft.md`, `b01c15-draft.md`, `b01c19-bones-draft.md`, `b01c20-draft.md`.
All are in `active-project/staff/showrunner/` root, not in `_drafts/`. None duplicated in
`_drafts/`. `b01c09-bones-draft-2026-05-31.md` is cited in pl-2026-06-01-001 at the current
(root) path — moving it would break that reference without a parking-lot update.
→ **Route: oskar.** Relocation to `_drafts/` requires coordinated parking-lot path update for
the b01c09 file; scope is beyond trivial-fix.

**3. LOW — `context-ledger-b01-c16.md` and `grounding-ledger-b01-c16.md` absent.**
All chapters c07–c20 have both ledger files. c16 alone has neither. Facets for c16 were run
(archive evidence: `20260605T000326Z-b01c16-facets`). The missing ledgers may be a related symptom
of finding #1 (depth-pass deferred / gate bypassed at c16). In a completed project this is a
pipeline-output gap, not a blocking issue.
→ **Route: oskar.** Confirm whether c16's `/and-facets` run was clean (ledgers authored but not
persisted) or whether the ledgers were simply never written due to a skipped phase.

**4. LOW — Pre-version backup file in active warehouse.**
`active-project/warehouse/cond-road-to-hell-chain-shape.pre-2026-05-18T123000Z.md` persists
alongside the live `cond-road-to-hell-chain-shape.md`. Pre-version sidecars are archival noise
in the active warehouse. Project is now complete; this is cosmetic.
→ **Route: margit.** Confirm the pre-version is superseded and safe to archive/remove.

**5. INFO — 60 open SOFT parking-lot items across completed b01 project.**
All open HARD items reviewed: only pl-2026-06-04-c16-001 is anomalous (see finding #1).
Remaining SOFT items are documented optional-depth-pass candidates, future-b02 deferred work,
or cross-pipeline spec-improvement notes. These are standing technical debt, not hygiene errors.
No action.

**6. INFO — Index drift: CLEAN.** `cards/locations/INDEX.md` checked against disk files:
no entries without files, no files without entries. Other indexes not showing drift signals.

**7. INFO — Memory/state file sizes in normal range.** `showrunner/memory.md` 13,401 lines
(expected for 20-chapter book). `staff/admin/decisions.md` 553KB + `process-proposals.md`
404KB — both append-only logs, large but structurally correct.

---

### Action taken

**Routed finding #1 to oskar** (highest severity — state inconsistency in closed-project
parking lot). Routing note appended to `active-project/staff/showrunner/parking-lot.md` as
`pl-2026-06-12-hygiene-001`.

No files moved or deleted. No schema files modified.
