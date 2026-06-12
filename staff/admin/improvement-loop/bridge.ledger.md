# Bridge improvement-loop ledger

Cross-repo mining log: brighid-creative-writing → and-shoot.
One pattern per pass. Rotation cycles through source areas in order.

Schema: area_mined | pattern_found | prop_filed | next_area

---

## Pass 1 — 2026-06-12

**Area mined:** `staff/agents/ingrid/rut-detection.plan.md` +
`staff/agents/ingrid/project-improvement-tracking.plan.md` (ingrid's rut-detection and
cross-project improvement tracking plans, including the §Auto-trigger registry section).

**Pattern found:** Auto-trigger mechanism at project/book close. At project close, ingrid
scans signal artifacts (dialogue-audit findings, peeve-critic survivals), identifies defect
classes that have repeated across multiple boards/chapters, and auto-dispatches structured
tuning routines (parroting-tuning, subtraction-pass-tuning) rather than just noting the
recurrence. The key structural element: the book/project close gate receives a structured
recurrence manifest — "which defect classes fired N times in this run" — before dispatching
the improvement agent, so the agent can produce a RECURRENCE-SUMMARY with ranked triage
calls instead of only per-chapter PROP bumps.

**Gap confirmed in and-shoot:** `/and-review verdict` Phase 4.5 dispatches admin with only
the book verdict report. Admin has no structured per-book recurrence manifest — it discovers
recurrences by scanning process-proposals.md ad-hoc. High-recurrence proposals (PROP-0037
recurrence_count: 8; PROP-0030/0031/0041 recurrence_count: 4) accumulated without a
book-close triage trigger.

**PROP filed:** PROP-0053 — "Book-close recurrence-manifest pre-pass at `/and-review verdict`
Phase 4.5". Modifies `.claude/commands/and-review.md §verdict Phase 4.5`. Cost: M.

**Next area in rotation:** critic/audience/narrator INDEX registries
(`critics/INDEX.md`, `narrators/INDEX.md`, `audience/INDEX.md`) — whether brighid's registry
convention (structured slug + description + last-used + stink fields) has a counterpart
worth porting to and-shoot's `staff/audience/INDEX.md`.
