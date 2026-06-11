# improvement-loop/process ledger

One bounded step per run. Append only.

---

## 2026-06-11

**Surveyed:** `staff/admin/process-proposals.md` (all accepted PROPs) + `CLAUDE.md` Rules 13–22 + `RUNBOOK.md` + `.claude/commands/and-substance.md` + `schemas/showrunner-memory.schema.md`.

**Findings:**
- PROP-0049 (ABSTRACTION-AS-SUBJECT / SCENE-ABSTRACT-DOMINANT): implemented — terms present in `.claude/commands/and-write.md`.
- PROP-0051 (slim /and-facets per DEC-0116): implemented — disposition_note confirms.
- PROP-0050 part 1 (mandatory /and-cohere at book-thirds in RUNBOOK.md): NOT yet wired — `RUNBOOK.md` still reads `[periodic, opt-in]` at the state machine diagram and explicitly says "DO NOT fire /and-cohere as part of this chain."
- PROP-0050 part 2 (signature readability floor in and-substance.md + schema): NOT yet wired — no `readability_floor` field in `schemas/showrunner-memory.schema.md` or validation in `/and-substance` Phase 4.

**Action taken:** Implemented PROP-0050 part 2 (smaller, root-cause fix):
- `schemas/showrunner-memory.schema.md`: added `readability_floor` block (3 required fields) to `series.substance` block after `chunk_targets`.
- `.claude/commands/and-substance.md` Phase 4 Step 4a: added `readability_floor` to screen-writer authoring brief.
- `.claude/commands/and-substance.md` Phase 4 Step 4c: added `SIGNATURE-NO-READABILITY-FLOOR` (HARD) validation before persist.

**Next candidate:** PROP-0050 part 1 — mandatory `/and-cohere` at book-thirds in `RUNBOOK.md`. Pre-flight check block + pipeline state machine need updating. ~1-file change.
