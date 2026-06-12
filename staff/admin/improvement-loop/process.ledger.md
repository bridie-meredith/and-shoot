# Process improvement-loop ledger

Each entry: date · surveyed · action taken · next candidate noticed.

---

## 2026-06-12

**Surveyed:** `staff/admin/process-proposals.md` (all `status: accepted` entries at lines 368, 6292, 6334, 6376, 6417, 6460, 6526 = PROP-0003/0004/0005-A, PROP-0046–0051). CLAUDE.md Rules 13–22. RUNBOOK.md. `.claude/commands/and-stitch.md`, `and-review.md`, `and-substance.md` (spot-check).

**Finding:** PROP-0050 Part 1 is unwired. Disposition note says "wiring staged; binding policy recorded now" (session `claude/optimistic-newton-YCnTC`). CLAUDE.md Rule 22 captured Part 2 (signature may not be satisfiable by a prose register). But Part 1 — **make `/and-cohere` mandatory at book-thirds (~1/3 + ~2/3 of planned chapters)** — is absent from RUNBOOK.md, which still labels cohere `[periodic, opt-in]` in every reference (lines 46, 65, 157, 200, 282). CLAUDE.md Rule 18 also still says "both opt-in suggestions in the end-of-run summary." PROP-0048 circuit-breaker appears referenced at `and-stitch.md:886`; PROP-0051 (facets slim) disposition says "IMPLEMENTED this session."

**Action taken:** Implemented PROP-0050 Part 1 — wired mandatory book-thirds cohere cadence into RUNBOOK.md (six targeted edits: diagram label, trigger table, pre-flight check + print format, chain section, what-not-to-do, what-not-to-do-at-session-start) and CLAUDE.md Rule 18 (one sentence update). Files changed: `RUNBOOK.md`, `CLAUDE.md`. PROP-0052 is still `status: open` (untriaged) — not touched.

**Next candidate noticed:** PROP-0048 Part 2 — the "aggregate-state counter" for the consecutive-caveat circuit-breaker is mentioned in `and-stitch.md:886` as "see Step 4 / PROP-0048" but `and-review.md` has no matching wiring for the `verdict` subcommand (grep returned empty). Worth verifying in a future loop pass whether the counter write/read is fully wired in the verdict/cohere aggregate phases.
