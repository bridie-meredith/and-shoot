# Process improvement-loop ledger

Append-only. One entry per run. Each entry: date, what was surveyed, action taken, next candidate noticed.

---

## 2026-06-11

**Surveyed:** `staff/admin/process-proposals.md` (all accepted proposals: PROP-0004 / 0046–0051); `CLAUDE.md` Rules 13–22; RUNBOOK.md chapter-production protocol; `.claude/commands/and-stitch.md` Phase 0.6 / 9.5; `.claude/commands/and-review.md` verdict subcommand; `schemas/facet.schema.md` exposition section; `staff/exposition-author/rubric-exposition.md` Form discipline.

**Action taken:** `PROP-0004` — added the `surface` field definition to `schemas/facet.schema.md` § exposition entry format. The command bodies (`and-facets.md`, `and-stitch.md` Phase 0.6) already reference `surface: reference` / `surface: render` split per PROP-0004/DEC-0014, but the schema — the authoritative source the rubric cites — had no `surface` field. Added field definition (render / reference / both), default-reference backward-compat rule, and per-chapter render cap note. File: `schemas/facet.schema.md`.

**Next candidate noticed:** `PROP-0050` (accepted, "wiring staged") — RUNBOOK.md line 157 still says `/and-cohere` is opt-in; the mandatory-at-book-thirds cadence from PROP-0050 part (1) is not wired into the chapter-production protocol. One RUNBOOK.md edit would close it. Note: CLAUDE.md Rule 18 also says "opt-in" — both files would need updating for full consistency, so this is a 2-file bounded step.
