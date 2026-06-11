# Process improvement-loop ledger

Append-only. One entry per run.

---

## 2026-06-11

**Surveyed:** `staff/admin/process-proposals.md` (PROP-0001 through PROP-0052) + CLAUDE.md Rules 13-22.

**Status scan:**
- PROP-0043/0044/0045: `implemented` — CLAUDE.md Rules 19/20/21.
- PROP-0046/0047/0049/0051: `accepted` — no-ledger fence + and-stitch/and-write changes; disposition notes say "this session" / PR merged.
- PROP-0048: `accepted` — CLAUDE.md Rule 22 records the N=2 policy; disposition note says "Command-body wiring staged." Counter tracking in aggregate-state + Phase 9.5/and-review verdict check NOT present in any command body. M-cost.
- PROP-0050: `accepted` — CLAUDE.md Rule 22 records the signature-floor constraint (part 2); disposition note says "Wiring staged." RUNBOOK.md part (1) NOT wired: `/and-cohere` still described as "periodic and opt-in" with no book-thirds gate. S-cost, 1 file.
- PROP-0052: `open`, untriaged — not eligible for implementation.

**Action taken:** Implemented PROP-0050 part (1) — wired mandatory book-thirds cohere gate into `RUNBOOK.md`. Changes: pipeline state machine annotation, pre-flight check (COHERE-DUE/COHERE-BLOCKED halt conditions), pre-flight print format (Cohere due line), chain notes (opt-in language replaced with mandatory-at-thirds), end-of-run summary (Next field), What NOT to do (cohere line qualified), trigger map (opt-in → mandatory at thirds), session-start gotchas (updated). CLAUDE.md Rule 22 already covers part (2).

**File changed:** `RUNBOOK.md` (1 file, S-cost).

**Next candidate noticed:** PROP-0048 (consecutive-caveat circuit-breaker counter not wired into aggregate-state.md or any command body — M-cost; needs schema + and-stitch.md + and-review.md).
