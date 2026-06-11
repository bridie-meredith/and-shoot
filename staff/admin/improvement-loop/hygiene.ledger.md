# Hygiene Ledger — improvement-loop/hygiene

Records artur hygiene passes: findings + actions. Append-only. Most recent pass at bottom.

---

## Pass 2026-06-11 (artur)

**Scope:** repo-wide sweep — parking lot, STM/memory files, state, path refs, catalogue drift.

### Findings (severity-ordered)

**SEV-1 (HIGH) — 4 open HARD depth-pass items with mismatch between description-gate and mechanical-gate**

Four HARD parking-lot items remain open after book-close:

| id | label | target.command | target.scope |
|----|-------|---------------|-------------|
| pl-2026-06-04-002 | depth-pass-mandatory-b01c14 | /and-write | b01c14 |
| pl-2026-06-04-c15-004 | depth-pass-mandatory-b01c15 | /and-write | b01c15 |
| pl-2026-06-04-c16-001 | depth-pass-mandatory-b01c16 | /and-write | b01c16 |
| pl-2026-06-05-c19-deptpass | depth-pass-required-b01c19-book-close | /and-write | book-close |

All four descriptions say they "gate `/and-substance book b02 Phase 0`." However, their `target.command` is `/and-write` (not `/and-substance`), so Phase 0 of `/and-substance book b02` will NOT see them in its parking-lot scan — the mechanical gate is absent. Additionally, `/and-review verdict b01` (book-close) ran without resolving them, meaning the intended pre-b02 triage never occurred. DEC-0115 (2026-06-08) retroactively changes the project's abstraction/apparatus stance, raising the question of whether these depth passes are still obligatory or supersedable. This requires an oskar/ingrid triage decision before any b02 activation.

Action taken: parking-lot item `pl-2026-06-11-hygiene-001` added (SOFT, targets `/and-substance book b02 Phase 0`; routes to oskar).

---

**SEV-2 (MEDIUM) — Dead path reference in `and-facets.md` Phase 4 Source enumeration**

`.claude/commands/and-facets.md:333` lists `rubric-exposition.md` in the Phase 4 auditor Source enumeration. The file `design/shoot-v2/rubric-exposition.md` does not exist (the rubric files are in `design/shoot-v2/` and exposition is absent from that directory). DEC-0111 (2026-06-07) decided to de-reference this pointer (Option b), but the Phase 4 enumeration was not updated. Phase 1 item 10 (line 179) is already correct — it names the real authority sources. Only the Phase 4 list carries the stale reference. Every future STRUCT scan will re-fire STRUCT-025 until it is removed.

Action: routed to oskar. Not in artur trivial-fix allowlist (command-body content edit).

---

**SEV-3 (LOW) — Stale chapter-specific SOFT parking-lot items**

Multiple open SOFT items target commands/scopes on chapters already stitched and shipped:

- pl-2026-05-25-006: `/and-stitch b01c01` (shipped)
- pl-2026-05-25-007: `/and-write b01c01` (shipped)
- pl-2026-05-25-014: `/and-facets b01c01` (shipped)
- pl-2026-05-25-015, -016: `/and-write b01c01` (shipped)
- pl-2026-05-30-002: `/and-write b01c06` (shipped)
- pl-2026-06-01-001: `/and-facets b01c09` (shipped)
- pl-2026-06-02-001: `/and-write b01c10` (shipped)
- pl-2026-06-03-003: `/and-stitch b01-c11` (shipped)
- pl-2026-06-03-004: `/and-write b01c12` (shipped)
- pl-2026-06-03-c14-001: `/and-write b01c14` (shipped)
- pl-2026-06-05-c18-002: `/and-write b01c18` (shipped)

These will never match a future invocation scan (chapters are complete). They are SOFT so they do not block anything. Per schema they are append-only and must not be deleted. No action needed unless a depth-pass re-opens those chapters.

---

**SEV-4 (INFO) — `staff/showrunner/stm.md` is empty**

`/home/user/and-shoot/staff/showrunner/stm.md` is 0 bytes. This is the library-level (non-project) showrunner STM, not `active-project/staff/showrunner/memory.md`. Expected: the library-level showrunner has no active state. Not actionable.

---

### Action taken

Top finding (SEV-1) is not trivially fixable — requires an oskar/ingrid triage decision. Routing note written. New parking-lot item `pl-2026-06-11-hygiene-001` added targeting `/and-substance book b02 Phase 0` to ensure the triage fires mechanically when b02 is activated.

**Route to: oskar** — triage the 4 open HARD depth-pass items before b02 activation. Options: (a) execute depth passes on c14/c15/c16/c19, or (b) dismiss items under DEC-0115 rationale with explicit `dismissed` status + resolution_note. Also fix the dead `rubric-exposition.md` reference at `and-facets.md:333` per DEC-0111 decision.
