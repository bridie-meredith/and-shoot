# Process improvement-loop ledger

Append-only. One entry per run. Format: date | surveyed | action | next-candidate.

---

## 2026-06-11

**Surveyed:** `staff/admin/process-proposals.md` (6586 lines, PROP-0001 through PROP-0052) + CLAUDE.md Rules 13–22 + key command bodies (`and-stitch.md`, `and-facets.md`) + `schemas/facet.schema.md` + `staff/exposition-author/rubric-exposition.md`.

**Action:** Implemented remaining PROP-0004 work (accepted 2026-05-26, `pr_ref: null`). PROP-0004 added a `surface: render|reference|both` field to exposition entries; the behavioral parts were already wired in `and-stitch.md` (Phase 1) and `and-facets.md` (Phase 1 authoring + Phase 4 FREQUENCY-BAND), but the schema definition and the rubric's audit gates were missing. Edited:
- `schemas/facet.schema.md` — added `surface: <surface-kind>` to the exposition entry format line + full field description including the per-chapter ≤3 render cap rule.
- `staff/exposition-author/rubric-exposition.md` — added four surface-related bullets to §Form discipline (surface-field required HARD, render cap HARD, reference-only default, render-as guidance scoping); added SURFACE-FIELD-MISSING and RENDER-CAP-BREACH HARD checks to §Audit classes.

**Next candidate:** PROP-0052 (`status: open`, untriaged) — structural-sameness pre-scan gap (no detector for ≥4 consecutive chapters sharing a scene-shape template). When triaged/accepted, cost estimate S (one dispatch sub-step addition to `/and-review cohere` or `/and-stitch` Phase 10 forward-thread).
