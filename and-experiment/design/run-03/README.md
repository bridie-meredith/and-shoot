# design/run-03/ — the span-A working layer (the Gael intake)

Created by the **OUTLINE-INTAKE migration** (2026-06-09; `/and-reoutline`), re-baselining the planning
around `intake/spine.md`. Supersedes the **run-02** layer (span-B / Saerys / 11-ch Book I), which is
retained as provenance.

## What's canonical here
- **`series-outline.md`** — the tokenized, thread-checkable 3-book span-A outline (19 beats). The
  structural spine; full prose/comedy detail lives in `intake/spine.md`.
- **`chapters/`** — per-chapter **detailed summaries** (scene-by-scene treatments off the spine beats,
  grounded in the live character layer + cultivation substrate; the layer between the spine beat and bones).
  Authored so far: `chapters/i1-dragonbane.md`.
- **`thread-config.txt`** — checker exceptions (parked/diffuse PLANT-ONLY + the SLATE-MATCH alias).
  `python3 scripts/check-threads.py design/run-03/series-outline.md --config design/run-03/thread-config.txt` → **PASS**.

## Source-of-truth pointers (the live span-A canon)
- **Narrative + comedy architecture + per-chapter gag map:** `intake/spine.md`
- **Cast profiles + scholar ladder:** `intake/character-profiles.md`
- **Per-foil comedy design (reviewed):** `intake/character-reactions.md`
- **Motivation + state-axes + growth/setback per role (state-ledger seed):** `intake/character-arc-ledger.md`
- **Live cards (10) + tombstones:** `and-experiment/warehouse/` (Gael, Wylla, Jaehaerys, Otto, Barth,
  Alicent, Maester Lorren, Septa Aldith, Hobb, Daemon)
- **Lead voice exemplars:** `and-experiment/persona-exemplars/{gael-targaryen,wylla-maid}.md`
- **Decisions record:** `intake/reconciliation-worksheet.md` (§A dispositions · §B GUARDs · §D rulings ·
  §D-slots open-slot resolutions · §E migration checklist)
- **Index:** `intake/CHARACTER-LAYER-INDEX.md`

## Migration status (Phase-4)
**Done:** run-03 created · spine tokenized as canonical outline · checker PASS · run-02 Book-I outline
archived (tombstone) · convergence-ledger Round 9 appended · live cast carded (Gael/Jaehaerys/span-A) ·
**character-refinement fold (2026-06-10)** — named the household straight-men (Lorren/Aldith/Hobb/Daemon)
in the beats, added a per-beat `Foils:` line carrying the four escalating foil gags, and wired the
**scholar-ladder relay** (Lorren → Barth, R0–R6) + the **Alicent-WTH** thread (new tokens `SCHOLAR-LADDER`
[plant-only] + `ALICENT-WTH`; checker re-run → PASS). Fulfils worksheet §C/§D Phase-4 actions (per-chapter
foil/comedy notes as PLANT/FIRE threads).

**Pending (tracked — heavier ADAPT carry-overs; staged for adaptiveness):**
- `time-anchor.md` §4 span fork → settle to span-A; roll §5 drift rows forward.
- state-ledger → re-found on the 3-book structure (adapt `run-02/book-i-state-ledger.md`; carry the
  entity registry + GUARDs). **Seed now available:** `intake/character-arc-ledger.md` provides the
  per-character motivation + state-axes + growth/setback trajectory the re-founded ledger builds on.
- `timeline-and-family-tree.md` → re-derive §2 family tree to Gael/Jaehaerys/Alicent + seat the
  antagonist faces (settle the Otto/Daemon AU-age vs rename call).
- `staff/showrunner/memory.md` + `project-history.md` → roll forward to span-A (L8); replace the stale
  Saerys/Viserys/Dance framing in `project.brief` + `themes_as_bounds`.
- **`warehouse/prop-cradle-egg.card.md` re-derive** (surfaced by `chapters/i1-dragonbane.md`) → the card
  encodes the superseded Saerys/christening-spoon/dud-egg version; the live span-A I.1 is the *living
  gift-egg that hatches and is killed*. Roll GUARD-2/3 framing forward likewise (dud → visible-but-misread
  hatchling-kill; R0-stays-a-laugh intent intact). **Blocking for `/and-write` I.1.**

## Open principal call (does not block)
Otto/Daemon seating — **AU-age (recommended)** vs rename to original era-appropriate figures. See
worksheet §D-slots.
