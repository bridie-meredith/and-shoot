# Process Improvement Loop — Ledger

Each entry: date · what was surveyed · action taken · next candidate noted.

---

## 2026-06-12

**Surveyed:**
- `staff/admin/process-proposals.md` (PROP-0043 through PROP-0052; ~6586 lines)
- `CLAUDE.md` Rules 13–22
- `.claude/commands/and-substance.md`, `.claude/commands/and-stitch.md`, `.claude/commands/and-review.md`
- `RUNBOOK.md` (chapter-production protocol, cohere references)

**Action taken:**
- **Implemented PROP-0050 part (b) — signature constraint fence** in `.claude/commands/and-substance.md` Phase 4 Steps 4a and 4b.
  - Added `readability_floor` requirement to the screen-writer's Step 4a dispatch brief (declares the non-negotiable minimum the prose register must coexist with; rejects register-as-sole-optimization; CLAUDE.md Rule 22).
  - Added pre-surface validation gate in Step 4b: if `readability_floor` is absent or empty the edit prompt does not surface; screen-writer is re-dispatched to add it first. Fires on every `redraft` iteration.
  - 1 file changed; < 10 lines added.

**Why this item:**
- PROP-0050 `status: accepted` (triaged 2026-06-08 by principal). The disposition note ("Wiring staged; binding policy recorded now") recorded the policy in CLAUDE.md Rule 22 but deferred the command-body wiring. Confirmed absent in `and-substance.md` via grep.
- Directly prevents the b01 failure class: a single-axis register signature with no readability counterweight passed every gate until the naive reader could not reconstruct events.
- Smallest atomic wiring: 1 file, targeted addition at the exact authoring point.

**Next candidate noted:**
- **PROP-0048 (accepted, not wired):** The consecutive-caveat circuit-breaker counter (N=2 cap on "design-inherent" dispositions) is referenced in `and-stitch.md` line 886 as a note but has no counter-tracking or enforcement path in `and-review.md` or the aggregate-state. Estimated cost: M (needs aggregate-state field + check at `/and-stitch` Phase 9.5 + `/and-review verdict`). Worth a follow-on improvement-loop run.
- **PROP-0052 (open, not triaged):** Structural-sameness pre-scan. Cannot implement until triaged.
