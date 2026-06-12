# Hygiene Ledger — artur (janitor)

Append-only. One pass per session. Severity-ordered findings → one action (fix or route).

---

## Pass 2026-06-12

**Scope:** full repo sweep — memory/STM files, parking-lot, staleness cascade markers, card indexes, draft/archive bloat, dead path references.

**Branch:** `claude/gifted-hawking-64xd0d`

### Findings (severity order)

**1. MEDIUM — Orphaned `active-project/audience/literary-snob/` working directory**

`active-project/audience/literary-snob/` exists with a 19 KB `stm.md` and supporting files. The active project's audience members are `cape-fic-reader`, `dark-fantasy-reader`, `worm-canon-pedant` (confirmed: `memory.md` line 26). `literary-snob` is a library persona in `staff/audience/` but is not one of the three active audience members. The directory appears to be orphaned state from an earlier project-setup trial. It won't block any pipeline command but it can confuse any Phase-0 scan that globs `active-project/audience/*/stm.md` for the active trio.

**Action taken:** routing note to oskar; parking-lot item `pl-2026-06-12-hygiene-001` filed (see below).

---

**2. MEDIUM — Dead context_refs in open SOFT parking-lot items (c01 pre-rebuild artifacts)**

Two open items reference files that no longer exist:
- `pl-2026-05-25-005`: context_ref `active-project/theater/facets/memory-b01-c01.md` — missing. The b01c01 facets were not preserved after the no-ledger rebuild (cascade-checkpoint confirms the rebuild bypassed the 10-facet chain).
- `pl-2026-05-25-006`: context_refs `active-project/theater/facets/sensory-b01-c01.md` and `active-project/theater/dialogue/taylor-hebert-kl-122ac.drafts.md` — both missing. Same cause.

Both items are SOFT. The dead refs do not block resolution but remove their traceability. The items' substance concerns (slug class for monument-* vs cond-*, and the loose prose anchor on feel:2 @10) are separable from the missing artifacts. Noted for the owner of those open items.

**Action taken:** surfaced here; no file change. Resolution belongs to oskar/showrunner if the items are still live.

---

**3. LOW — `active-project/theater/facets/` only contains c07 facets**

c01-c06 and c08-c20 facets are absent. The cascade-checkpoint confirms this is expected: the no-ledger rebuild was a "combined revise+render pass, not the 10-facet/8-phase chain." Facets were not re-authored. Not a defect; surfaced for awareness.

---

**4. LOW — cascade-checkpoint `current:` field stale after COMPLETE**

`active-project/staff/showrunner/cascade-checkpoint.md` has `status: COMPLETE` (completed 2026-06-08) but `current: {chapter: b01c01, step: "/and-write b01c01 revise", verdict: null}` and `caps_per_chapter: {bones_retry: 0/1, ...}`. These are leftover running-state fields from the last chapter processed before COMPLETE was stamped. Cosmetic only; does not affect any pipeline command. Noted for the next session that reads this file.

---

**5. LOW — `active-project/staff/showrunner/_drafts/` has 51 files**

Historical working copies from c01-c20 development. The `_archive/` sibling holds one dated cleanup pass (2026-05-31). Not blocking. Noted for a future artur sweep if the directory grows further.

---

**6. NO FINDING — card index multi-section listing**

Initial sweep flagged locations/personas/conditions/props indexes as having "duplicate" entries (2–5× per slug). Confirmed NOT a defect: each index uses multiple organizational sections (`by_world`, `by_quality`, `by_type`/`by_trope`) and every slug correctly appears once per section. Disk files match index slugs.

---

**7. NO FINDING — staleness cascade markers**

All `stale_since` fields in `memory.md` are null. No stale markers to surface.

---

### Action — routing note to oskar

**Finding:** pl-2026-06-12-hygiene-001 (see parking-lot.md).  
**Owner:** oskar (manages audience health + cast balance per CLAUDE.md routing table).  
**Ask:** confirm whether `active-project/audience/literary-snob/` is safe to remove (oskar decision, not artur's). If oskar confirms it is orphaned, margit should archive or delete the directory and update any index that references it.
