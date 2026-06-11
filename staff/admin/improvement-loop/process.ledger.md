# Improvement-Loop / Process — Ledger

Running log of process-layer improvement runs. One entry per session. Format: date, survey scope, action taken, next candidate noted.

---

## 2026-06-11

**Surveyed:** `staff/admin/process-proposals.md` (tail 200 lines; status grep full file); CLAUDE.md Rules 13–22; RUNBOOK.md cohere wiring; `.claude/commands/and-write.md` Phase 6; `.claude/commands/and-stitch.md` Phase 9 Step 4; `.claude/commands/and-review.md` verdict; `schemas/bones.schema.md` SVO discipline section.

**Findings:**
- PROP-0049 (ABSTRACTION-AS-SUBJECT HARD + CONCRETENESS FLOOR): **implemented** in and-write.md Phase 6.
- PROP-0047 (and-stitch Phase 4 LEDGER-REGISTER PROHIBITION + Phase 9 naive-follow): **implemented** per disposition note.
- PROP-0051 (and-facets slim): **implemented** per disposition note.
- PROP-0046 (no-ledger fence cross-surface): accepted; CLAUDE.md Rule 22 + stitch/write edits done this session per disposition; **schema + card edits staged (not done)**. The `bones.schema.md` SVO discipline section had no `FAULT-FORM-ABSTRACTION-AS-SUBJECT` rule despite the constraint being enforced at the Phase 6 gate — schema was not authoritative on this class.
- PROP-0048 (consecutive-caveat circuit breaker): accepted; "command-body wiring staged" — and-stitch.md Phase 9 Step 4 references PROP-0048 inline but has no counter logic; and-review.md has no mention. Not yet wired.
- PROP-0050 (mandatory cohere at book-thirds): accepted; "wiring staged" — RUNBOOK.md still says opt-in at three separate points (lines 157, 200, 282). Not yet wired.
- PROP-0052 (structural-sameness pre-scan in /and-review cohere): open, not yet triaged.

**Action taken:** PROP-0046 staged schema edit — added `FAULT-FORM-ABSTRACTION-AS-SUBJECT` HARD rule to `schemas/bones.schema.md` SVO discipline section. 1 file. Schema now authoritative on the abstraction-as-subject prohibition; cross-references the Phase 6 gate and provides concrete rewrite examples. Audience-card threshold-discipline clause (also in PROP-0046's proposed_diff) left untouched — persona card content.

**Next candidate:** PROP-0048 (consecutive-caveat circuit breaker). Medium cost. Requires: (1) a counter field added to `aggregate-state.md` schema for per-defect-class consecutive-ship count, (2) logic in `and-stitch.md` Phase 9 Step 4 to read + increment + check the counter, (3) and-review.md verdict to read the same counter. Three files, all non-persona. Highest remaining impact among staged accepted PROPs.
