# Improvement-loop / process ledger

Append-only. One entry per run. Format: date | surveyed | action taken | next candidate noticed.

---

## 2026-06-12

**Surveyed:**
- `staff/admin/process-proposals.md` — all PROPs (PROP-0001 through PROP-0052). Checked `status` fields for accepted-but-unimplemented items.
- `RUNBOOK.md` § Common gotchas — explicit "not implemented" flags.
- `schemas/facet.schema.md` — current exposition entry format.
- `.claude/commands/and-facets.md` and `.claude/commands/and-stitch.md` — current command-body state.

**Finding:** PROP-0004 (`schemas/facet.schema.md` `surface` field for exposition entries) is `status: accepted` (`pr_ref: null`) and the RUNBOOK gotcha explicitly calls it unimplemented. Command bodies (`and-facets.md`, `and-stitch.md`) already reference `surface: reference` default and `surface: render` / `reference` / `both` semantics, but `schemas/facet.schema.md` had no `surface` field in the exposition entry format or field documentation. This is the schema-authority gap: the format line, the field definitions, and the per-episode caps section all lacked the `surface` field.

**Action taken:** PROP-0004 partial — `schemas/facet.schema.md` updated:
1. Entry format line: added `| surface: <surface-kind>` after `renders-as: <position>`.
2. Field documentation: added `surface` field definition (render/reference/both; default `reference` for new entries; legacy = `render` with `WARN-SURFACE-ABSENT` SIGNAL).
3. Per-episode caps: added `surface:render + surface:both ≤3 per chapter` cap line.

Command bodies were already current; this closes the schema-authority gap. File: `schemas/facet.schema.md`.

**Remaining gap / next candidate:** `staff/exposition-author/rubric-exposition.md` does not exist at the repo root (only in archived projects). PROP-0004's proposed_diff also calls for a rubric gate (`surface-field required → HARD at Phase 5 auditor scan` + per-chapter render cap audit check). This is the remaining unimplemented piece of PROP-0004 (cost S — single file creation). Next run should create `staff/exposition-author/rubric-exposition.md` with the surface-required HARD gate and the ≤3 render cap AP-SCAN entry.
