# improvement-loop/process ledger

Schema: date | surveyed | action | next-candidate

---

## 2026-06-11

**Surveyed:** process-proposals.md (all PROPs 0001–0052) + CLAUDE.md Rules 13–22 + key command bodies (and-stitch.md, and-review.md, and-substance.md, RUNBOOK.md). All PROPs 0046–0051 carry `status: accepted`; most have `disposition_note: "implemented this session"`. Checked actual command bodies: PROP-0049 wired (ABSTRACTION-AS-SUBJECT + SCENE-ABSTRACT-DOMINANT in and-write.md Phase 6 ✓). PROP-0050 NOT wired: RUNBOOK.md line 157 still says `/and-cohere` is "opt-in" + "NOT in this chain"; and-substance.md Phase 5 auditor has no register-floor check.

**Action:** Implemented PROP-0050 (accepted, not yet wired).
- `RUNBOOK.md` lines 157 + 282: mandatory cohere at book-third + two-thirds milestones; FAIL-COHERE blocks further ships. Opt-in for all other chapters.
- `.claude/commands/and-substance.md` Phase 5 auditor row: added `SIGNATURE-REGISTER-ONLY` HARD check (series level) — signature must declare explicit readability/concreteness floor per CLAUDE.md Rule 22.

**Next candidate:** PROP-0048 — consecutive-caveat circuit breaker (`and-stitch.md` Phase 9 Step 4 + `and-review.md` verdict). CLAUDE.md Rule 22 has the N=2 policy but command-body enforcement counter is absent. Requires a tracking field in `aggregate-state.md` (schema: `schemas/aggregate-state.schema.md`) + check-and-promote logic in 2 command bodies (~3 files).
