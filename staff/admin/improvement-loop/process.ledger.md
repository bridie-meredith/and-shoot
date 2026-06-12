# Process improvement-loop ledger

Append-only. One entry per run. Format: date | surveyed | action | next-candidate.

---

## 2026-06-12

**Surveyed:** process-proposals.md (all entries); CLAUDE.md Rules 13-22; schemas/facet.schema.md; staff/exposition-author/rubric-exposition.md; .claude/commands/and-facets.md; .claude/commands/and-stitch.md.

**Action:** Implemented remaining gap in PROP-0004 (accepted 2026-05-26, pr_ref: null). The command files (and-facets.md, and-stitch.md) already referenced the `surface:` field per PROP-0004, but two files had not been updated: (1) `schemas/facet.schema.md` — exposition entry format line lacked `surface:` field + no field-level documentation; (2) `staff/exposition-author/rubric-exposition.md` — Form discipline lacked surface-field-required gate and render cap; Audit classes lacked the corresponding CONSTRAINT + FREQUENCY-BAND checks. Applied both changes per PROP-0004 proposed_diff and accepted disposition.

**Files changed:** schemas/facet.schema.md, staff/exposition-author/rubric-exposition.md (2 files).

**Next candidate noticed:** `rubric-exposition.md § Audience-gate (Phase 5b) hooks` still describes the old 3-of-3 adversarial audience-gate (ATTACK / ACCEPT / 3-of-3 rule / author-call on ADDS) that was retired under DEC-0116 and PROP-0051. This section is now dead code — the audience-gate no longer runs at /and-facets. Candidate action: file a proposal to delete or archive the Phase 5b hooks section (change_type: delete; cost_estimate: S). Not filed this run — only one action per run.
