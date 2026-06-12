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

---

## 2026-06-12

**Surveyed:** `staff/admin/improvement-loop/process.ledger.md` (prior entry named PROP-0050 part 1 as next) + `staff/admin/process-proposals.md` (PROP-0050 status: accepted) + `RUNBOOK.md` (lines 46, 65, 157, 200, 282 confirmed opt-in language) + `schemas/showrunner-memory.schema.md` (no cohere_checkpoints field).

**Findings:**
- PROP-0050 part 2 (readability_floor): confirmed implemented per prior run.
- PROP-0050 part 1 (mandatory book-thirds cohere): NOT yet wired — RUNBOOK still said `[periodic, opt-in]` and explicitly prohibited cohere mid-chain.

**Action taken:** Implemented PROP-0050 part 1 across 2 files:
- `RUNBOOK.md`: pipeline state machine → `[book-thirds: mandatory; otherwise opt-in]`; trigger map entry updated; added step 7 (book-thirds conditional cohere after Phase 10); added FAIL-COHERE to R5 halt list; split postop/cohere prohibition and qualified it; added `Cohere (step 7)` line to end-of-run summary template; added `HALTED-FAIL-COHERE` to Outcome enum; updated "What NOT to do at session start" cohere caution.
- `schemas/showrunner-memory.schema.md`: added `cohere_checkpoints[]` block to `books[]` (threshold + chapter_at_cohere + cohered_at + verdict + report_path).

**Next candidate:** Survey new PROPs (PROP-0052 structural-sameness scan, PROP-0053) for accepted+unimplemented status, or drift scan for command-body → CLAUDE.md Rule mismatches not yet filed.
