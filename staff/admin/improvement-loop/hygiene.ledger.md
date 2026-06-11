# Hygiene Ledger

Tracks improvement-loop hygiene passes. Append-only. One entry per run.

---

## Pass 2026-06-11

**Branch:** claude/gifted-hawking-4onsbj
**Sweep agent:** artur (read-only investigation → findings reported here)
**Action taken:** trivial fix — cascade-checkpoint.md `current` field corrected (SEV-2 #5)

### Findings (severity order)

| # | SEV | Category | Item | Affected file | Route |
|---|-----|----------|------|---------------|-------|
| 1 | SEV-1 | Open HARD parking-lot items post-book-close | 4 HARD depth-pass items stranded: pl-2026-06-04-002, pl-2026-06-04-c15-004, pl-2026-06-04-c16-001, pl-2026-06-05-c19-deptpass. b01 is shipped; their stated gate (`/and-substance book b02`) is either already behind us (verdict ran as DEC-0107) or blocked by b02 not being authorized. Not auto-resolvable — requires principal disposition (execute the depth passes or stamp accepted-caveat). | active-project/staff/showrunner/parking-lot.md | **→ admin (user-proxy)** for disposition decision |
| 2 | SEV-1 | Non-routable parking-lot targets | 5+ items use `target.command: margit-card-class-review` or `margit-card-authoring` — not valid pipeline command names. Phase 0 scanning will never surface them. Items: pl-2026-05-25-005, pl-2026-06-03-005, pl-2026-06-04-001, pl-2026-06-04-c15-002, pl-2026-06-04-c15-003. | active-project/staff/showrunner/parking-lot.md | **→ oskar** — retarget to valid command + phase or add margit dispatch step to relevant `/and-facets` Phase 0 |
| 3 | SEV-1 | Broken context_refs (archived facet paths) | b01c01 facet and dialogue paths cited in parking-lot items are missing from disk — archived to `active-project/theater/_archive/20260526T031937Z-b01c01-facets/`. Dead audit trail on: memory-b01-c01.md, state-updates-b01-c01.md, narrator-interest-b01-c01.md, feeling-b01-c01.md, sensory-b01-c01.md, taylor-hebert-kl-122ac.drafts.md. These are in resolved/advisory items so nothing is blocked. | active-project/staff/showrunner/parking-lot.md | No block. Route to **margit** if active re-examination of these items is needed; otherwise annotation-only. |
| 4 | SEV-2 | Broken context_refs (wrong path prefix) | pl-2026-06-01-002 cites `active-project/staff/audience/sensory-old-state-reader/` — this path does not exist (correct prefix is `active-project/audience/`). Also cites `active-project/staff/auditor/facets-audience-gate-r1.md` which is absent. Item is open and targets `/and-review pipeline`. | active-project/staff/showrunner/parking-lot.md | **→ oskar or fixer** — correct context_refs paths |
| 5 | SEV-2 | Cascade checkpoint `current` field inconsistency | `cascade-checkpoint.md` declares `status: COMPLETE` (all 20 b01 chapters converted, completed_at: 2026-06-08) but `current: {chapter: b01c01, step: "/and-write b01c01 revise", verdict: null}` — never updated before stamping complete. **FIXED THIS PASS** (updated current to b01c20/complete/COMPLETE). | active-project/staff/showrunner/cascade-checkpoint.md | fix-trivial ✓ DONE |
| 6 | SEV-2 | Live stale_since on pre-supersede b01c06 record | memory.md line 3926 carries `stale_since: 2026-05-31` on the pre-revise cold_read record for b01c06. Intentional documentation (the field is inline-commented as superseded), but a naive Phase 0 scan for non-null stale_since will surface it as a live staleness flag against a resolved chapter. | active-project/staff/showrunner/memory.md | **→ oskar** — schema question: should pre-supersede stale markers use a distinct key (e.g., `historical_stale_since`)? |
| 7 | SEV-2 | Open acknowledged-debt item with wildcard scope | pl-2026-06-08-formdebt-001 documents ~95 SVO-form debt instances across b01 chapters, status open, scope `*` — will surface on every `/and-write` Phase 0. The description says it does not block forward motion. Needs explicit disposition stamp. | active-project/staff/showrunner/parking-lot.md | **→ admin (user-proxy)** — stamp `accepted-as-b01-known-debt` or close |
| 8 | SEV-3 | Admin STM bloated — never pruned | staff/admin/stm.md has 127 DEC entries (DEC-0001 through DEC-0116) spanning the entire b01 run. Schema header says prune to ~20 at session-open; LTM has only 22 entries all from 2026-05-24–25. Historical DECs from the completed book are not load-bearing in any current run. | staff/admin/stm.md, staff/admin/ltm.md | **→ ingrid** — prune pass; promote ~10 permanent methodology rulings to LTM, archive or drop the rest |
| 9 | SEV-3 | Open sameness item targets assembled manuscript | pl-2026-06-08-sameness-001 targets `/and-cohere b01 c11-c19`, is principal-gated (explicitly noted), but has no `pending_principal_decision` annotation. Will surface at every `/and-cohere` Phase 0 session-open. | active-project/staff/showrunner/parking-lot.md | **→ admin (user-proxy)** — add `pending_principal_decision: true` annotation or disposition |
| 10 | SEV-3 | b02-deferred item without b02 decision | pl-2026-06-07-pipeline-001 (`design/shoot-v2/rubric-exposition.md` at b02-activation) is correctly parked SOFT. No action until b02 is authorized; if b02 is never pursued, stamp resolved as "b02 not authorized; item voided." | active-project/staff/showrunner/parking-lot.md | No action now; note for principal |

### Action taken

**SEV-2 #5 — trivial fix applied:** Updated `cascade-checkpoint.md` `current` field from `{chapter: b01c01, step: "/and-write b01c01 revise", verdict: null}` to `{chapter: b01c20, step: "complete", verdict: "COMPLETE"}` to match the declared `status: COMPLETE` and `batch: ALL 20 chapters converted`.

### Routing summary

| Route | Items |
|-------|-------|
| admin (user-proxy) | SEV-1 #1 (4 stranded HARD depth-pass items), SEV-2 #7 (formdebt disposition), SEV-3 #9 (sameness annotation) |
| oskar | SEV-1 #2 (non-routable targets), SEV-2 #4 (broken path prefix in context_refs), SEV-2 #6 (stale_since schema question) |
| margit | SEV-1 #3 (archived facet path annotation, if re-examination needed) |
| ingrid | SEV-3 #8 (STM prune pass) |
| no action | SEV-3 #10 (b02-deferred) |
