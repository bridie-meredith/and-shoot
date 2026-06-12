# Hygiene Ledger — and-shoot
# Maintained by artur. Append-only. One entry per hygiene pass.

---

## Pass 2026-06-12 — branch claude/gifted-hawking-caas6g

### Sweep scope
- `active-project/staff/showrunner/parking-lot.md`
- `active-project/staff/showrunner/` (STM/memory/ledger files)
- `active-project/theater/bones/` and `draft/` (orphan check)
- `active-project/staff/showrunner/_drafts/` vs `_archive/` path drift

### Findings (severity order)

1. **MEDIUM — Duplicate item ID `pl-2026-06-05-c17-001` in parking-lot.md**
   Two distinct SOFT items assigned the same ID (schema violation; `id` must be unique).
   - First occurrence line 2337: created_at 2026-06-05T00:30:00Z — `/and-facets b01c17 Phase 5 audit (signal-008/009)`, target `/and-facets b01c18 Phase 1`, status resolved.
   - Second occurrence line 2375: created_at 2026-06-05T01:00:00Z — `/and-stitch b01-c17 Phase 9 cold-read terminal gate`, target `/and-write b01-c17`, status open.
   No cross-references to the duplicate ID elsewhere in the file. Trivial-fix allowlist: renumber second to `pl-2026-06-05-c17-002`.

2. **LOW — Duplicate section-comment block at parking-lot.md lines 1126–1131**
   The 6-line comment block (`# ── Session 2026-05-31 cold-read audit findings …`) duplicates
   lines 1126–1128 verbatim (3 comment lines appear twice back-to-back). Cosmetic; does not
   affect YAML parse. Trivial fix; deferred to next pass (only one action allowed per pass).

3. **LOW — Five stranded draft files in showrunner root**
   Files `b01c09-bones-draft-2026-05-31.md`, `b01c11-bones-draft.md`, `b01c11-draft.md`,
   `b01c15-bones-draft.md`, `b01c15-draft.md`, `b01c19-bones-draft.md`, `b01c20-draft.md`
   sit at `active-project/staff/showrunner/` root, not in `_drafts/`. Directory contains
   `_drafts/` for exactly this class of file. Route: **oskar** (owns studio housing; decide
   move-to-_drafts vs _archive vs keep-at-root as design choice, since memory.md may cite
   some at root path).

4. **LOW — Missing context-ledger for b01-c16**
   `active-project/theater/bones/b01-c16.md` is present (chapter terminal) but no
   `context-ledger-b01-c16.md` in showrunner. Also missing: `context-ledger-b01-c19.md`
   (grounding-ledger-b01-c19.md IS present). Route: **oskar** (check whether c16/c19 were
   authored inline in memory.md rather than as standalone files, or were simply omitted;
   if omitted, determine if a retroactive ledger is needed).

5. **LOW — Three dead context_refs paths (parking-lot comment fields)**
   Paths in `context_refs` fields that do not exist on disk:
   - `active-project/staff/showrunner/_drafts/b01c01-draft-2026-05-25.md` (pl-2026-05-25-001)
   - `active-project/staff/showrunner/_drafts/b01c05-revise-fromsignals-2026-05-28.md` (pl-2026-05-28-002)
   - `active-project/staff/showrunner/_drafts/b01c07-bones-draft-2026-05-30-rev2.md` (pl-2026-05-31-003)
   These refs are human-readable commentary only (not machine-parsed at Phase 0); files likely
   moved to `_archive/` or never written to disk. Informational; no blocking effect.
   Route: **oskar** (verify files exist under _archive/ or accept as resolved-content-lost).

### Action taken
**Fixed finding #1** (trivial fix — duplicate ID): renamed second occurrence of
`pl-2026-06-05-c17-001` at parking-lot.md line 2375 to `pl-2026-06-05-c17-002`.
This is a purely mechanical renaming; no content changed; no cross-references existed
to the old duplicate ID.

### Routing notes written
- Finding #3, #4, #5 → **oskar** (see above; no parking-lot item added — all are advisory
  or informational, none rises to HARD).

---
