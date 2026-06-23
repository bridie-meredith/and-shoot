# Spine review & revision — the 3 books, together (2026-06-23)

**Scope (DEC-0118 / PROCEED-A):** review + revise `intake/spine.md` so the three books read as one coherent,
unambiguously-canonical unit; sync the tokenized layer; quarantine stale conflicting design material.
**No prose was commissioned** — the "draft" is the design spine. Revision aggressiveness: review-then-revise,
not wholesale rewrite (the changelog tail was preserved in place per the principal's standing preference).

## What was reviewed
- `intake/spine.md` (1025 lines) — Books I–III body + the dated FOLDED changelog tail, end to end.
- `design/run-04/series-outline.md` (tokenized, thread-checked) — `check-threads.py` = **PASS** (R0–R4 intact, R2=II.8).
- Cross-file conflict surfaces: `design/restructured-books-two-desires.md`, `design/run-01..03/`.

## Findings
1. **The story body (Books I–III) is internally consistent.** It reflects every final fold — R2=II.8, Caraxes
   maddened (not killed), pure-frame I.5, Book II = 8-ch gambling/Entertainment-Dao shape, ages 0–6 / ~6–9 /
   ~9–11, Dance parked. The per-chapter reverse-angle map, the gag map, the curdle-ladder block, and the chapter
   bodies agree with one another. **No structural continuity errors in the body.**
2. **One stale in-body contradiction (FIXED).** The *Resolved creative-fill (2026-06-09)* reference section still
   described **R2 as a single-exploiter poisoning at II.7** — superseded by DEC-0117 (R2 is the **suitor-party
   disappearance at II.8**). Corrected the R2 bullet to canon and stamped the update.
3. **Canonical ambiguity from the provenance tail (RESOLVED by demarcation).** ~590 lines of dated fold records
   sit below the body and include superseded snapshots (II.7-as-first-kill, Caraxes-killed) that contradict the
   body if read straight. The principal has deliberately preserved this tail (a prior rework verified it
   "byte-identical"), so it was **demarcated, not relocated**.
4. **Stale conflicting design files (QUARANTINED).** `restructured-books-two-desires.md` (run-02 two-desires
   re-axis) carried a contradictory structure — ages 3–9/9–13/13–15, Dance included, names Saerys/Daenys/Harwin.
   Its *engine* survived into canon; its *structure* is obsolete. run-01/02 lacked supersession markers (run-03
   already had one).

## Revisions applied (all in `projects/gael-cultivation-comedy/`)
- **`intake/spine.md`** — (a) new **"Canonical authority — read this first"** banner up top (declares the body
  canonical, names the latest canonical state, points away from the superseded layers); (b) **fixed the stale R2
  item** (II.7/single-exploiter → II.8/suitor-party disappearance, per DEC-0117); (c) new **"Provenance & revision
  history"** demarcation header at the body/changelog boundary ("the body above is canonical; where a note below
  conflicts, the body wins").
- **`design/restructured-books-two-desires.md`** — SUPERSEDED banner (engine-folded, structure-stale).
- **`design/run-02/README.md`, `design/run-01/book-outlines.md`, `design/run-01/outlines.md`** — SUPERSEDED banners
  pointing to the run-04 / spine canon.

## Not changed (deliberately)
- **`design/run-04/series-outline.md`** — no structural change was needed (the spine edits only corrected a stale
  reference note + added framing); check-threads re-confirmed **PASS** after the pass.
- The working title (`*(working title TBD)*`) — left open; naming is a principal creative call, not a defect.
- The Book-I-only *Themes* section — deliberate prior "go deeper on Book I" pass, not a hole.
- The standing open principal call (Otto/Daemon AU-seating vs rename) — un-raised, does not block.

## Result
`intake/spine.md` now reads as one clean 3-book document with an explicit canonical/provenance boundary and no
ambiguity about which version is authoritative. The tokenized layer remains thread-checked PASS.
