# Process Improvement Ledger

Records one bounded step per run. Each entry: date, survey scope, action taken, next candidate.

---

## 2026-06-11

**Surveyed:** `staff/admin/process-proposals.md` (PROP-0043 through PROP-0052) + CLAUDE.md Rules 13-22 + command bodies (`and-write.md`, `and-stitch.md`, `and-review.md`) + `schemas/bones.schema.md`.

**Landscape:**
- PROP-0043/0044/0045: accepted + implemented (CLAUDE.md Rules 19/20/21).
- PROP-0046: accepted; disposition note "schema + card edits staged." and-write.md Phase 6 has `ABSTRACTION-AS-SUBJECT` as HARD gate; bones.schema.md § SUBJECT VERB OBJECT discipline did NOT. The authoritative schema was missing the clause. Audience persona card portion → ESCALATE (persona-card content; off-limits).
- PROP-0047: accepted + implemented (and-stitch.md Phase 4 LEDGER-REGISTER + Phase 9 NAIVE-FOLLOW).
- PROP-0048: accepted; "command-body wiring staged." Circuit-breaker referenced in and-stitch.md line 886 parenthetical but NO counter-tracking or enforcement logic present in Phase 9 Step 4 or and-review.md. Requires aggregate-state counter field → 3+ files; larger scope.
- PROP-0049: accepted + implemented (and-write.md Phase 6 ABSTRACTION-AS-SUBJECT + SCENE-ABSTRACT-DOMINANT HARD gates).
- PROP-0050: accepted; "wiring staged." RUNBOOK still says cohere is "opt-in"; no mandatory trigger at book-thirds. → Next candidate.
- PROP-0051: accepted + implemented (and-facets.md slim rewrite, DEC-0116).
- PROP-0052: open/untriaged → no-touch.

**Action taken:** Added `ABSTRACTION-AS-SUBJECT is REJECT` clause to `schemas/bones.schema.md` § SUBJECT VERB OBJECT discipline — closing the gap between the Phase 6 gate (PROP-0049, implemented) and the authoritative schema (PROP-0046, staged). 1 file. Fault code `ABSTRACTION-AS-SUBJECT-<bone>` now documented at the schema layer, not just the gate layer.

**ESCALATE for Brighid:** PROP-0046 also requires a Threshold-Discipline clause on audience persona cards ("a reviewer may NOT excuse opacity as intended register; followability is judged against a naive reader"). That is persona-card content and is off-limits for this routine. Brighid should add this clause to the three active audience persona cards at `active-project/audience/`.

**Next candidate (priority order):**
1. **PROP-0050 wiring** — RUNBOOK.md § "Producing a chapter" still says `/and-cohere` is "opt-in"; the mandatory book-thirds checkpoint accepted per PROP-0050 / DEC-0115 is not wired. 2 files (RUNBOOK.md + possibly and-substance.md). Small.
2. **PROP-0048 circuit-breaker** — consecutive-caveat counter needs a new field in showrunner-memory.schema.md + check in and-stitch.md Phase 9.5 + and-review.md. 3+ files; larger scope but high impact.
