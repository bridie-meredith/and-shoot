# Hygiene Ledger — and-shoot

Schema: append-only. Each pass adds a dated block.

---

## Pass 2026-06-12

**Sweep scope:** STM/LTM files, showrunner memory, parking-lot, staleness markers, internal path refs, proto-lines, index drift, draft clutter.

### Findings (severity-ordered)

1. **SEV-1 | proto-lines naming-convention duplicate**
   `active-project/theater/proto-lines/b01c19.md` is an exact duplicate of
   `b01-c19.md` (both 2374 bytes; `diff` returns empty). Canonical convention
   is `b01-<NN>.md` (with dash). `b01c19.md` is the orphaned misnamed copy.
   → **trivial fix applied** (see Action below)

2. **SEV-2 | missing context-ledger for c16**
   `active-project/staff/showrunner/context-ledger-b01-c16.md` does not exist.
   All other chapters c07–c20 (except c16 and c19) have context-ledgers.
   b01-c16 is a shipped chapter; its `/and-facets` Phase 2.5 run either did
   not emit the ledger or it was not persisted.
   → routes to **oskar**

3. **SEV-3 | missing context-ledger for c19**
   `context-ledger-b01-c19.md` absent (grounding-ledger-b01-c19.md IS present).
   Same class as SEV-2.
   → routes to **oskar**

4. **SEV-4 | 60 open SOFT parking-lot items, many targeting shipped chapters**
   Chapters b01c01–b01c10 have multiple SOFT items still `status: open`
   targeting `/and-write`, `/and-stitch`, `/and-facets` invocations that
   have long since run. These surface at every Phase 0 scan. Also: several
   items have malformed `command/scope` fields (inline `}` artifacts in values,
   e.g. scope: "/and-stitch, scope: "*", phase: null}"). The parking-lot
   schema prohibits deletion but a mass-SOFT-dismiss sweep (stamping
   `resolved_at` + `resolution_note: "chapter shipped; SOFT carried past
   resolving command; auto-dismissed by hygiene pass"`) would reduce noise.
   → routes to **oskar** (decision + execution; requires per-item review)

5. **SEV-5 | 7 loose scratch files at showrunner root**
   The following files sit at `active-project/staff/showrunner/` root rather
   than in `_drafts/`:
   - `b01c09-bones-draft-2026-05-31.md`
   - `b01c11-bones-draft.md`, `b01c11-draft.md`
   - `b01c15-bones-draft.md`, `b01c15-draft.md`
   - `b01c19-bones-draft.md`
   - `b01c20-draft.md`
   These predate or duplicate content in `_drafts/`. Clutter that adds to
   Phase 0 orientation cost.
   → routes to **oskar** (archive or delete decision)

6. **SEV-6 | INFO — theater/facets only holds c07 (expected)**
   Live facets directory contains only the 13 c07 facet files. All other
   chapters' facets are in `theater/_archive/` timestamped snapshots. This
   matches the slim-facets pipeline design (facets consumed by stitch, then
   archived). No action.

7. **SEV-7 | INFO — staleness markers clean**
   All `stale_since:` fields in `memory.md` are `null`. No stale cascade
   issues active.

8. **SEV-8 | INFO — actor STMs thin (2–5 lines each)**
   All 11 actor STMs are 2–5 lines. Likely intentional — primary chapter-level
   state is tracked in `memory.md chapters[]` rather than individual STM files.
   No action.

### Action taken

**SEV-1 FIX:** Deleted `active-project/theater/proto-lines/b01c19.md`
(naming-convention violation; exact duplicate of canonical `b01-c19.md`).

### Routing notes

- **oskar:** SEV-2/3 (missing c16/c19 context-ledgers — investigate whether
  `/and-facets` Phase 2.5 failed to persist for those chapters); SEV-4 (mass
  SOFT parking-lot item dismiss sweep for shipped chapters); SEV-5 (loose
  scratch files at showrunner root — archive or delete).
