# Bridge Improvement-Loop Ledger

Tracks passes of the BRIDGE routine: mining brighid-creative-writing for patterns
worth porting to and-shoot. One pattern per pass; proposals go to
staff/admin/process-proposals.md for principal triage.

Schema per entry:
- pass: integer (monotonic)
- date: ISO date
- area_mined: which brighid area was read
- pattern_found: one-line description
- prop_filed: PROP-<NNNN>
- next_area: area for the next pass (rotation)

---

## Pass 1

```yaml
pass: 1
date: 2026-06-11
area_mined: |
  staff/agents/ingrid/rut-detection.plan.md
  staff/agents/ingrid/project-improvement-tracking.plan.md
pattern_found: |
  Auto-trigger registry at project-close: ingrid runs a standing recurrence sweep
  over all accumulated signal artifacts (critic findings, audience stink, postop
  reports) at project/book close — regardless of whether individual chapters passed
  — and auto-fires tuning routines for fault classes that recur across N>=2 boards.
  This is a proactive, book-scope complement to the reactive per-chapter trigger.
  And-shoot's admin fires only reactively (per-chapter non-PASS). No standing
  book-close sweep exists. Ported form: admin recurrence-sweep mode wired at
  /and-review verdict <book>.
prop_filed: PROP-0053
next_area: |
  critics/INDEX.md + audience/INDEX.md + narrators/INDEX.md
  (Registry conventions — how brighid maintains indices across persona pools;
  compare to and-shoot's staff/audience/INDEX.md to find indexing gaps.)
```
