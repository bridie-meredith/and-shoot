# improvement-loop/assets ledger

Tracks each pass of the assets improvement routine (oskar/editor). One entry per run.

---

## Pass 001 — 2026-06-11

**Asset improved:** `staff/dialogue-writer/rubric-dialogue.md` — AP-SCAN class in `§Audit classes`

**Change:** Replaced single prose AP-SCAN bullet with four explicitly named codes matching `and-facets.md` Phase 4 AP-SCAN definition exactly:
- `AP-chassis-contamination`
- `AP-modern-hr-speak`
- `AP-deposition-cadence`
- `AP-nominalization-substituting-plain-English`

Each code now carries a mechanically-testable trigger description and register qualifier (e.g. "acceptable only in maester/court-functionary register").

**Why top-ranked:** The `and-facets.md` Phase 4 RUBRIC-FIDELITY class enumerates anti-patterns from each rubric's `§Audit classes > AP-SCAN` entries at audit time, expecting named codes it can check individually. The rubric had a prose paragraph naming the four concepts but no code identifiers — the auditor was forced to derive the codes from `and-facets.md` instead of the rubric that is supposed to be the authority. Cost was 5 lines → 6 lines; benefit is precise per-code enumeration for every future Phase 4 RUBRIC-FIDELITY pass, with no persona content touched.

**Surfaces surveyed (this pass):**
- `and-experiment/persona-exemplars/` — 9 exemplars exist; none match active cast slugs, but actor exemplars require persona voice content (HARD fence) → skipped.
- `.claude/commands/and-facets.md` class library — complete and current.
- `scripts/normalize_inflight_r2.py` — dead script (targets retired `_inflight-r2/`); deprecation notice is a valid follow-on but lower-priority than the rubric gap found.
- `scripts/check-threads.py` — functional.
- `schemas/` — not surveyed in depth this pass.

**Next candidate:** `scripts/normalize_inflight_r2.py` — add a deprecation notice at the top explaining the `_inflight-r2/` path no longer exists since R2 was retired (DEC-0116), so the script always fails and should not be used. Low cost, removes confusion.
