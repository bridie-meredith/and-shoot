# design/run-03/ — the span-A working layer (the Gael intake)

Created by the **OUTLINE-INTAKE migration** (2026-06-09; `/and-reoutline`), re-baselining the planning
around `intake/spine.md`. Supersedes the **run-02** layer (span-B / Saerys / 11-ch Book I), which is
retained as provenance.

## What's canonical here
- **`series-outline.md`** — the tokenized, thread-checkable 3-book span-A outline (19 beats). The
  structural spine; full prose/comedy detail lives in `intake/spine.md`.
- **`thread-config.txt`** — checker exceptions (parked/diffuse PLANT-ONLY + the SLATE-MATCH alias).
  `python3 scripts/check-threads.py design/run-03/series-outline.md --config design/run-03/thread-config.txt` → **PASS**.

## Source-of-truth pointers (the live span-A canon)
- **Narrative + comedy architecture + per-chapter gag map:** `intake/spine.md`
- **Cast profiles + scholar ladder:** `intake/character-profiles.md`
- **Per-foil comedy design (reviewed):** `intake/character-reactions.md`
- **Live cards (10) + tombstones:** `and-experiment/warehouse/` (Gael, Wylla, Jaehaerys, Otto, Barth,
  Alicent, Maester Lorren, Septa Aldith, Hobb, Daemon)
- **Lead voice exemplars:** `and-experiment/persona-exemplars/{gael-targaryen,wylla-maid}.md`
- **Decisions record:** `intake/reconciliation-worksheet.md` (§A dispositions · §B GUARDs · §D rulings ·
  §D-slots open-slot resolutions · §E migration checklist)
- **Index:** `intake/CHARACTER-LAYER-INDEX.md`

## Migration status (Phase-4)
**Done:** run-03 created · spine tokenized as canonical outline · checker PASS · run-02 Book-I outline
archived (tombstone) · convergence-ledger Round 9 appended · live cast carded (Gael/Jaehaerys/span-A).

**Pending (tracked — heavier ADAPT carry-overs; staged for adaptiveness):**
- `time-anchor.md` §4 span fork → settle to span-A; roll §5 drift rows forward.
- state-ledger → re-found on the 3-book structure (adapt `run-02/book-i-state-ledger.md`; carry the
  entity registry + GUARDs).
- `timeline-and-family-tree.md` → re-derive §2 family tree to Gael/Jaehaerys/Alicent + seat the
  antagonist faces (settle the Otto/Daemon AU-age vs rename call).
- `staff/showrunner/memory.md` + `project-history.md` → roll forward to span-A (L8); replace the stale
  Saerys/Viserys/Dance framing in `project.brief` + `themes_as_bounds`.

## Open principal call (does not block)
Otto/Daemon seating — **AU-age (recommended)** vs rename to original era-appropriate figures. See
worksheet §D-slots.
