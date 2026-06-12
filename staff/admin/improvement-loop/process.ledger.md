# Improvement-loop / process ledger

Append-only. One entry per run. Each entry: date, survey scope, action taken, next candidate.

---

## 2026-06-12

**Surveyed:** `staff/admin/process-proposals.md` accepted proposals (lines 368, 6292–6526); CLAUDE.md Rules 13–22; command bodies `and-stitch.md`, `and-review.md`; `schemas/aggregate-state.schema.md`.

**Finding:** PROP-0048 (consecutive-caveat circuit breaker, accepted 2026-06-08) was only partially implemented. CLAUDE.md Rule 22 records the binding policy (N=2 cap). The aggregate-state schema had no `caveat_history[]` field; `/and-stitch` Phase 9 Step 4 had only a cross-reference comment ("see Step 4 / PROP-0048") with no counter logic; Phase 10 Step 4 had no update step; `/and-review verdict` had no caveat check. The other accepted proposals (PROP-0046/0047/0049/0051) were fully implemented in PR #101 + #ecstatic-volta-14ixm1. PROP-0050 (/and-cohere mandatory at book thirds) was partially implemented (the signature-constraint half is in CLAUDE.md Rule 22; the mandatory-cadence RUNBOOK wiring is not done — noted as next candidate).

**Action taken:** Implemented the missing PROP-0048 wiring across 3 files:
- `schemas/aggregate-state.schema.md` — added `caveat_history[]` block + validation rules §9–10.
- `.claude/commands/and-stitch.md` Phase 9 Step 4 — added FAIL-CONSECUTIVE-CAVEAT circuit-breaker check; Phase 10 Step 4 — added `caveat_history[]` read/update/reset logic.
- `.claude/commands/and-review.md` verdict subcommand — added consecutive-caveat pre-check + SYSTEMIC-CAVEAT auto-promote at N≥4.

**Next candidate:** PROP-0050 component 1 — wire `/and-cohere` mandatory at book thirds into RUNBOOK.md (the chapter-production protocol). The RUNBOOK still says "opt-in" at lines 46, 157, 200, 282; the mandate from PROP-0050 (accepted 2026-06-08) is not reflected there. 2 files (RUNBOOK.md + optionally `.claude/commands/and-substance.md`), small.
