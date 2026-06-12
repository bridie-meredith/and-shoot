# Improvement-loop / process — ledger

Append-only. One entry per run. Date · surveyed · action taken · next candidate.

---

## 2026-06-12

**Surveyed:** `staff/admin/process-proposals.md` (51 entries); CLAUDE.md Rules 13–22; RUNBOOK.md; `.claude/commands/and-write.md`; `.claude/commands/and-stitch.md`; `.claude/commands/and-review.md`.

**Findings:**
- PROP-0046–0049 and 0051: command-body changes are present in main (PROP-0047 NAIVE-FOLLOW + LEDGER-REGISTER PROHIBITED in and-stitch; PROP-0049 ABSTRACTION-AS-SUBJECT + SCENE-ABSTRACT-DOMINANT in and-write; PROP-0051 and-facets slim). Statuses still say `accepted`, not `implemented` — but the wiring is present. Deferred status-stamp cleanup to a future run (low value, high noise).
- PROP-0048 (CONSECUTIVE-CAVEAT circuit breaker): CLAUDE.md Rule 22 states the N=2 policy; and-stitch.md line 886 references "see Step 4 / PROP-0048" but Phase 9 Step 4 contains no counter-tracking or enforcement logic. Flagged as next candidate.
- **PROP-0050 (mandatory cohere at book-thirds):** ACCEPTED, status `accepted`. RUNBOOK had three explicit "opt-in / NOT in this chain" statements contradicting the accepted proposal. CLAUDE.md Rule 22 captured the signature-floor constraint (part 2) but not the RUNBOOK chain wiring (part 1).

**Action taken:** Implemented PROP-0050 in `RUNBOOK.md`. Changes:
1. Pipeline diagram: `[periodic, opt-in]` → `[mandatory at book-thirds; opt-in otherwise]`
2. Chain note (line 157 area): replaced "NOT in this chain / opt-in" with mandatory book-thirds trigger logic (`floor(N/3)` + `floor(2N/3)` completed chapters; `FAIL-COHERE` blocks next chapter)
3. What-NOT-to-do: split postop/cohere line; added book-thirds exception to cohere restriction
4. End-of-run summary template: added `Cohere-trigger` status line + updated `Next` line
5. Session-start do-not list: updated cohere note to name book-thirds exemption

Stamped `PROP-0050` → `status: implemented` + `implemented_at: 2026-06-12` in process-proposals.md.

**Next candidate:** PROP-0048 — CONSECUTIVE-CAVEAT circuit breaker. CLAUDE.md Rule 22 states the N=2 cap but and-stitch.md Phase 9 Step 4 has no counter logic. Needs: (1) `defect_class_caveats` counter field in `schemas/aggregate-state.schema.md`, (2) check in and-stitch Phase 9 Step 4 that reads the counter and auto-promotes at N+1=3. Cost M; ~2 files.
