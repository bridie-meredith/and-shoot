# Process improvement-loop ledger

Append-only. One entry per run. Each entry: date, survey scope, action taken, next candidate noticed.

---

## 2026-06-11

**Surveyed:** `staff/admin/process-proposals.md` (PROP-0001 through PROP-0052), CLAUDE.md Rules 13-22, command bodies for PROP-0046–0051 wiring.

**Accepted-but-unwired PROPs found:**
- **PROP-0046** — no-ledger fence: `bones.schema.md` abstraction-as-subject reject + audience card reviewer-excuse ban NOT added (CLAUDE.md Rule 22 + and-stitch/and-write edits were done; schema + card edits "staged").
- **PROP-0048** — CONSECUTIVE-CAVEAT CIRCUIT BREAKER: wiring absent in `and-stitch.md` Phase 9 Step 4, `and-review.md` verdict section, and `aggregate-state.schema.md` (no caveat_streaks block). Disposition note: "Command-body wiring staged; binding policy recorded now."
- **PROP-0050** — mandatory cohere at book-thirds: RUNBOOK.md still says "opt-in"; `and-substance.md` has no signature-constraint gate. Disposition note: "Wiring staged; binding policy recorded now."

**Action taken:** Implemented **PROP-0048** (highest impact-to-cost: circuit breaker is the mechanical enforcement of Rule 22's core policy).
- `schemas/aggregate-state.schema.md` — added `caveat_streaks[]` block + validation rule 9.
- `.claude/commands/and-stitch.md` — added circuit breaker check in Phase 9 Step 4 (between axis scoring and verdict printing); AIRLESS streak ≥ 2 → auto-promote PASS → PASS-WITH-DEPTH-PASS-REQUIRED; update caveat_streaks in aggregate-state after verdict.
- `.claude/commands/and-review.md` — added `CAVEAT-STREAK-UNRESOLVED` / `CAVEAT-STREAK-EXCEEDED` HARD scan in verdict Phase 0.

**Next candidate noticed:** PROP-0050 (mandatory cohere at book-thirds in RUNBOOK.md + signature constraint gate in and-substance.md) — two files, simple text change, accepted.
