# Process improvement-loop ledger

Append-only. One entry per run. Format: date | surveyed | action taken | next candidate noticed.

---

## 2026-06-11

**Surveyed:**
- `staff/admin/process-proposals.md` — 52 PROPs total. Scanned for `status: accepted` entries: PROP-0003 (pr_ref: null; the exposition surface:render/reference system — confirmed implemented via PROP-0004/DEC-0014 wiring in and-facets.md + and-stitch.md), PROP-0046/0047/0048/0049/0050/0051 (pr_ref: claude/optimistic-newton-YCnTC or ecstatic-volta-14ixm1).
- Confirmed implemented on this branch: PROP-0047 (ledger-register prohibition in and-stitch.md), PROP-0049 (ABSTRACTION-AS-SUBJECT + SCENE-ABSTRACT-DOMINANT in and-write.md), PROP-0051 (and-facets slim rewrite per DEC-0116).
- Confirmed NOT implemented in this branch: PROP-0050 part 2 — `readability_floor` schema field absent from `schemas/showrunner-memory.schema.md`; no `SIGNATURE-NO-READABILITY-FLOOR` gate in `.claude/commands/and-substance.md` Phase 5. CLAUDE.md Rule 22 declares the policy but the command body had no enforcement wiring.

**Action taken:** Implemented PROP-0050 part 2 (S cost; 2 files).
- `schemas/showrunner-memory.schema.md`: added `readability_floor` field to `series.substance` block with authoring semantics + HARD-gate reference.
- `.claude/commands/and-substance.md`: (a) Step 4a — added screen-writer instruction to author `readability_floor`; (b) Phase 5 auditor row — added `SIGNATURE-NO-READABILITY-FLOOR` + `SIGNATURE-REGISTER-ONLY-FLOOR` HARD findings (series level only).

**Not addressed:** PROP-0050 part 1 (mandatory cohere at book-thirds) — RUNBOOK.md + CLAUDE.md Rule 18 both still say cohere is "opt-in." This is the remaining un-wired half of PROP-0050; it is M-cost (RUNBOOK.md + CLAUDE.md Rule 18 + possibly and-substance.md cascade context) and would require care not to conflict with Rule 18's explicit "NOT in the chain" language. Next candidate for the next run.

**Next candidate noticed:** PROP-0050 part 1 (mandatory cohere at book-thirds). PROP-0048's consecutive-caveat circuit breaker enforcement is also missing from command bodies (CLAUDE.md Rule 22 declares it but and-stitch.md Phase 9 Step 4 has no counter/check; no `consecutive_caveat_streak` field in showrunner-memory.schema.md). Either is a bounded S-M cost next step.
