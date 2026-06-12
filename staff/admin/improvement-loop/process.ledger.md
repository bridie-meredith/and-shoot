# Process improvement-loop ledger

Append-only log. One entry per run. Format: date | surveyed | action | next candidate.

---

## 2026-06-12

**Surveyed:** `staff/admin/process-proposals.md` (all accepted proposals), CLAUDE.md Rules 13-22.

**Finding:** PROP-0048 (consecutive-caveat circuit breaker, `status: accepted`, `pr_ref: claude/optimistic-newton-YCnTC`) was accepted 2026-06-08 with disposition "command-body wiring staged; recorded as binding policy now." The counter field and enforcement logic were entirely absent: `schemas/aggregate-state.schema.md` had no `design_inherent_tracking` block, `/and-stitch` Phase 9 Step 4 had no counter increment or circuit-breaker check, and `/and-review verdict` had no Phase 0 check for auto-promoted entries.

**Action taken:** Implemented PROP-0048 enforcement across 3 files:
- `schemas/aggregate-state.schema.md` — added `design_inherent_tracking[]` block + validation rule 9
- `.claude/commands/and-stitch.md` — added circuit-breaker update step at end of Phase 9 Step 4 (increment on PASS-WITH-DEPTH-PASS-REQUIRED, reset on clean PASS, escalate to CIRCUIT-BREAKER-BLOCKED at consecutive_count > 2)
- `.claude/commands/and-review.md` — added Phase 0 check (e) in `verdict <book-slug>` that HARD-aborts if any chapter in scope has an unresolved `auto_promoted_at` entry

**Next candidate:** PROP-0046 "schema + card edits staged" — `schemas/bones.schema.md` is missing the explicit "abstraction-as-subject is REJECT" entry (the runtime check in and-write Phase 6 exists, but the schema itself doesn't declare it). The audience card Threshold Discipline clauses are persona content (excluded per Rule 4 / task instructions). The bones schema note alone would be a single-file S-cost change. Alternatively, PROP-0050 "wiring staged" — mandatory `/and-cohere` at book-thirds in `RUNBOOK.md` is absent; the signature-constraint clause is already in CLAUDE.md Rule 22 but the RUNBOOK chapter-production protocol still marks cohere as opt-in.
