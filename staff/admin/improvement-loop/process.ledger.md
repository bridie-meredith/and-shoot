# Improvement-loop / process ledger

Append-only. One entry per run. Schema: date | surveyed | action | next-candidate.

---

## 2026-06-12

**Surveyed:** `staff/admin/process-proposals.md` (PROP-0002 through PROP-0052) + CLAUDE.md Rules 13–22 + RUNBOOK.md + `.claude/commands/and-stitch.md` + `.claude/commands/and-substance.md`.

**Status scan:**
- PROP-0043/0044/0045: accepted + implemented (CLAUDE.md Rules 19/20/21).
- PROP-0046: accepted; CLAUDE.md Rule 22 + stitch/write Phase 6 edits landed; schema + persona-card edits marked "staged" (not yet in bones.schema.md / facet.schema.md / audience persona cards).
- PROP-0047: accepted + implemented (and-stitch.md Phase 4 LEDGER-REGISTER + Phase 9 naive-follow).
- PROP-0048: accepted; CLAUDE.md Rule 22 disposition circuit-breaker policy landed; **command-body wiring marked "staged"** — consecutive-caveat counter absent from and-stitch.md Phase 9.5 and and-review.md verdict.
- PROP-0049: accepted + implemented (and-write.md Phase 6 ABSTRACTION-AS-SUBJECT HARD + SCENE-ABSTRACT-DOMINANT).
- PROP-0050: accepted; policy in CLAUDE.md Rule 22 (signature constraint) and RUNBOOK.md authority line (89: "wiring staged"); **RUNBOOK.md still says `/and-cohere` is opt-in at three locations (lines 157, 200, 282)**; `and-substance.md` Phase 4 has no readability-floor constraint; `/and-cohere` will never auto-fire under the current operational text.
- PROP-0051: accepted + implemented (and-facets.md DEC-0116 slim rewrite).
- PROP-0052: open / untriaged.

**Highest impact-to-cost item:** PROP-0050 Part 1 — wire mandatory `/and-cohere` at book-thirds into RUNBOOK.md and CLAUDE.md Rule 18. The contradiction is explicit: the runbook says "NOT in this chain / opt-in" while the accepted proposal and CLAUDE.md Rule 22 require mandatory firing at book-thirds. This is the live operational document for every chapter-production run.

**Action taken:** Implemented PROP-0050 Part 1 — edited RUNBOOK.md (3 locations: chain step note, "What NOT to do" bullet, session-start "don't" entry) + CLAUDE.md Rule 18 (1 sentence). Files changed: `RUNBOOK.md`, `CLAUDE.md`.

**Not implemented this run:** PROP-0050 Part 2 (and-substance.md Phase 4 readability-floor constraint + `schemas/showrunner-memory.schema.md` new `readability_floor` field) — requires schema addition first; left for next run.

**Next candidate:** PROP-0050 Part 2 — add `readability_floor` field to `schemas/showrunner-memory.schema.md` + wire the authoring constraint into `and-substance.md` Phase 4 Step 4a. Cost S–M; 2 files.

Runner-up: PROP-0048 command-body wiring (consecutive-caveat counter in and-stitch.md Phase 9.5 + and-review.md verdict; requires designing state storage in aggregate-state.schema.md). Cost M; 3 files.
