# hygiene.ledger.md
# Improvement-loop hygiene pass log. Append-only per run.
# Owning agent: artur (janitor). Routing targets: margit / oskar / ingrid / Brighid.

---

## Run 2026-06-11 — first pass

**Branch:** `claude/gifted-hawking-50mfh4`
**Repo:** `/home/user/and-shoot`

### Finding inventory (severity-ordered)

**SEV-1 [ROUTE→oskar] `memory.md` severely bloated**
- File: `active-project/staff/showrunner/memory.md`
- Size: 13,401 lines
- Detail: Grew across 20-chapter original cascade + no-ledger revision pass. Per-bone state-deltas
  are by-design here (CLAUDE.md memory rules), but context-load cost at this size is significant for
  every session that opens showrunner memory. Oskar should assess what is archivable (early-chapter
  bones records, pre-no-ledger-revision phase records) and whether a split into live-session +
  archived portion is warranted.
- Parking-lot entry: `pl-2026-06-11-hygiene-001`

**SEV-2 [ROUTE→oskar] 60/86 parking-lot items open, many targeting completed chapters**
- File: `active-project/staff/showrunner/parking-lot.md`
- Detail: 60 open, 26 resolved. Open SOFT items with scope `b01c01`–`b01c07` target `/and-write`,
  `/and-facets`, `/and-stitch` runs that shipped terminal drafts (all 20 chapters present in
  `active-project/draft/`). The no-ledger revision cascade (COMPLETE 2026-06-08) ran without
  resolving parking-lot items from the original chapter runs. Oskar should perform a batch
  staleness review: items whose resolving command clearly completed should be stamped
  `resolved` (or `dismissed` if scope is permanently moot). Schema allows compaction.
- Rolled into: `pl-2026-06-11-hygiene-001`

**SEV-3 [TRIVIAL — deferred to next pass] `cascade-checkpoint.md` `current` cursor is stale**
- File: `active-project/staff/showrunner/cascade-checkpoint.md`
- Detail: `status: COMPLETE`, `completed_at: 2026-06-08`, but `current.chapter: b01c01`,
  `current.step: "/and-write b01c01 revise"`, `current.verdict: null` — leftover cursor from
  when the cascade was live. No operational block (COMPLETE is clearly marked), but the stale
  cursor could mislead future session orientation. One-line fix: set `current` to `null` or
  `COMPLETE`.
- Action: NOT taken this pass (one-action rule; top finding routes to oskar). Candidate for
  next trivial-fix pass.

**SEV-4 [ROUTE→oskar] Orphaned draft files at showrunner root**
- Files: `active-project/staff/showrunner/b01c09-bones-draft-2026-05-31.md`,
  `b01c11-bones-draft.md`, `b01c11-draft.md`, `b01c15-bones-draft.md`, `b01c15-draft.md`,
  `b01c19-bones-draft.md`, `b01c20-draft.md`
- Detail: 7 intermediate/working draft files at showrunner root rather than in `_drafts/`.
  Chapters c01–c08 have working files in `_drafts/`; c09–c20 range has these 7 outliers.
  Likely escaped during later cascade runs. Oskar should confirm intentional placement or
  direct margit to move them into `_drafts/`.
- Rolled into: `pl-2026-06-11-hygiene-001`

**SEV-5 [ROUTE→oskar] Missing context/grounding ledger pairs for c16 and c19**
- Missing: `context-ledger-b01-c16` (both context and grounding absent), `context-ledger-b01-c19`
  (grounding-ledger exists; context-ledger absent)
- Detail: All other chapters c07–c20 have paired ledgers except c16 (both absent) and c19
  (context absent). Chapters c01–c06 predate the ledger system. The no-ledger revision pass
  may have bypassed ledger authoring for these chapters if the combined revise+render pass
  skipped the facet pipeline. Oskar decides whether gaps are legitimate or need backfill.
- Rolled into: `pl-2026-06-11-hygiene-001`

**SEV-6 [INFO] `staff/admin/improvement-loop/` directory created this pass**
- Did not exist; created with this ledger.

### Top action taken this pass

**Route to oskar** — `memory.md` bloat (SEV-1) is the top finding; not on the trivial-fix
allowlist. Routing note written to `active-project/staff/showrunner/parking-lot.md` as
`pl-2026-06-11-hygiene-001` (SOFT, target: `oskar-session-review`, scope: `*`).
