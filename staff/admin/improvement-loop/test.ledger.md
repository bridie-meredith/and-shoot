# Improvement-Loop / TEST — Lens Rotation Ledger

Tracks which lens was last run, the headline verdict, findings filed, and which lens is next. One entry per pass. Append-only.

Rotation order:
  a. /and-review pipeline — schema vs command-body vs rubric tri-walk
  b. /and-review consistency or tree — recent chapter or and-experiment spine
  c. /and-ablate on a shipped chapter — facet-contribution evidence
  d. targeted auditor fork — most-recently-changed artifact

---

## Pass 1 — 2026-06-12

**Lens:** a — `/and-review pipeline` tri-walk (schema vs command bodies vs rubrics; residue scan; CLAUDE.md sync)

**Report:** `active-project/staff/reviews/pipeline-20260612T121301Z.md`

**Verdict:** FAIL-WITH-HARD

**Findings summary:**
- **1 HARD (persists):** STRUCT-025 — and-facets.md Phase 4 RUBRIC-FIDELITY source enumeration still names non-existent `rubric-exposition.md`. DEC-0111 fixed Phase 1 item 10 only; Phase 4 was not updated. Parking-lot: pl-2026-06-12-pipeline-001 (HARD, target `/and-facets *` Phase 4).
- **5 SIGNAL carryovers filed as SOFT parking-lot items:**
  - STRUCT-013 (rubric-dialogue.md at wrong path, outside and-review.md glob): pl-2026-06-12-pipeline-002
  - STRUCT-022 (rubric-feeling.md line 239 stale caveat-pre-ship notice): pl-2026-06-12-pipeline-003
  - STRUCT-024 (rubric-memory-flags.md line 166 "1–5%" vs FREQUENCY-BAND "5–12%"): pl-2026-06-12-pipeline-004
  - STRUCT-027 (and-facets.md Phase 1 routes pressure-signal to substance_delta instead of scene-map): pl-2026-06-12-pipeline-005
  - STRUCT-002 (axes_held[] post-move ambiguity): pre-existing pl-2026-05-25-018 (not re-filed)
- **2 PASSes (new wiring confirmed):** STRUCT-031 (Rule 22 ABSTRACTION-AS-SUBJECT + LEDGER-REGISTER + NAIVE-FOLLOW all wired); STRUCT-032 (Rule 21 RECONCILE wired in and-review.md)
- **4 prior HARDs confirmed CLOSED:** STRUCT-017 (rubric-metaphor tens), STRUCT-018 (rubric-vibes tens), STRUCT-019 (rubric-metaphor "proposed"), STRUCT-026 (AP7 tensometer)
- **1 prior HARD confirmed CLOSED via DEC-0116:** STRUCT-029 (R2 metaphor provisional anchor — R2 is gone)

**Next lens:** b — `/and-review consistency` or `/and-review tree` on a recent chapter (or and-experiment spine if active)
