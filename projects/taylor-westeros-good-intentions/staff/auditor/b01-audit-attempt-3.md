=== auditor attempt-3 narrow re-check ===
scope: book
target: b01
timestamp: 2026-05-24
prior_report: active-project/staff/auditor/b01-audit-attempt-2.md
change_reviewed: b01c15 relational_anchor_status cost_ledger_anchor cl-d08 → cl04

---

fault-005 status: RESOLVED — cl-d08 now drawn only at b01c12 (+1.0 of +2 gain); b01c15 redirected to cl04.

balance check (delta from attempt-2):
  cl-d08: b01c12 +1.0 | vs gain +2 | BALANCED-WITH-UNDERDRAW (0.5 unallocated; not an error)
  cl04:   b01c14 +1.0 + b01c15 +1.5 = 2.5 | vs gain +3 | BALANCED-WITH-UNDERDRAW (0.5 unallocated; not an error)

  Note: b01c15 notes reference "journey-required cl-d08" as a narrative prerequisite only — the anchor
  field is cl04; no second draw against cl-d08 is registered.

regression check on faults 001-004:
  cl-world-d04 (fault-001): b01c04 +1.0 + b01c10 +1.0 = 2.0 vs +2 — unchanged, RESOLVED holds
  cl-antag-d03 (fault-002): b01c03 +1.5 + b01c04 +1.0 + b01c15 +1.5 = 4.0 vs +4 — unchanged, RESOLVED holds
  cl-d07a (fault-003): b01c10 +1.0 + b01c14 +1.0 = 2.0 vs +2 — unchanged, RESOLVED holds
  cl05 / cl03a (fault-004): cl05 cost b01c12 -1.0 = -1.0 vs -1; cl03a cost b01c10 + b01c17 = -2.0 vs -2 — unchanged, RESOLVED holds

new HARD findings: none

aggregate: ACCEPT (0 HARD)

notes:
  The single-field edit (b01c15 relational_anchor_status anchor cl-d08 → cl04) resolves fault-005
  without introducing any new imbalance. cl04 gain capacity (+3) accommodates the combined c14 + c15
  draw (2.5) with 0.5 remaining. cl-d08 is now underfilled by 1.0 — acceptable per ledger rules.
  The 8 outstanding soft flags from attempt-2 (INFERENTIAL-ANCHOR + flag-010 NAMING-INCONSISTENCY)
  carry forward unchanged; no new soft findings introduced by this edit.
