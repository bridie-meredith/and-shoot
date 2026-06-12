# Agent Improvement-Loop Ledger

Round-robin tuning log. One entry per pass. Agents rotate in alphabetical order across `.claude/agents/` before any repeats.

---

## 2026-06-12 — admin.md

**Change:** In process-critic Decision Procedure Step 4 (Count recurrence), expanded the grep scope from `active-project/staff/reviews/` only to include `active-project/staff/auditor/` as well (plus the matching `projects/*/staff/auditor/` for cross-project boundary searches). Bone-gate reports (`staff/auditor/write-<chapter>-bone-gate.md`) and facets audit reports (`staff/auditor/facets-final-audit.md`) are the primary trigger sources for process-critic dispatches but land in `staff/auditor/`, not `staff/reviews/`. The prior gap caused recurrence counts to undercount prior occurrences of the same finding class from the two most common trigger sources.

**Next agent:** audience.md
