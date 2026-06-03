cascade:
  root: b01c12
  invoked_at: 2026-06-03T00:00:00Z
  invoked_command: "/and-substance chapter b01c12 --cascade  (produce-chapter-protocol b01c12)"
  mode: unattended
  last_completed:
    level: chapter-complete   # b01c12 COMPLETE end-to-end: substance + write + review-bones + facets + stitch (P9 SHIPPED-WITH-CAVEATS DEC-0078 + P10 PASS-THREAD). draft/b01-c12.md TERMINAL (1213 words).
    slug: b01c12
    completed_at: 2026-06-03T00:00:00Z
  prev_completed:
    level: chapter-complete
    slug: b01c11
    completed_at: 2026-06-03T00:00:00Z
  next:
    command: produce-chapter-protocol b01c13
    args: [b01c13]
  reason: chapter-complete
  failure: null
  pending_depth_passes: []   # c12 cold-read SHIPPED-WITH-CAVEATS (DEC-0078; admin A) — NOT PASS-WITH-DEPTH-PASS-REQUIRED; design-inherent, no mandated per-chapter depth pass.
  pending_threading_holds: []   # c12 Phase 10 PASS-THREAD clean (0 substantive); aggregate-state through c12; c13 Phase 0 CLEAR (0 unack substantive).
  pending_cohere: |
    HIGH URGENCY — RUN /and-cohere b01 BEFORE c13. c12 is the 3rd consecutive SHIPPED-WITH-CAVEATS (c10 DEC-0072, c11 DEC-0074, c12 DEC-0078); N=7 consecutive-abstract (c06-c12). The apparatus-register density makes uninformed cold-reads airless; the per-chapter pipeline (person-first embodiment + grounding-ledger) is applied and the substance-aware checks pass, but the cross-chapter accumulation is a cohere-layer problem. DEC-0073/0075/0077/0078 all reaffirm. NEW: PROP-0037/DEC-0079 (Phase 9.5) proposes making /and-substance chapter Phase 0 HARD-abort on consecutive_shipped_with_caveats>=3 without cohere-ack — pending principal triage; if accepted, c13 is hard-gated on cohere.
  triage_queue:
    - "PROP-0011 recurrence_count=4 (HELD-AXIS-NOT-WITNESSED c04/c06/c10/c12) — DEC-0077; triage before c13 (Phase-1 step-4a completion gate would prevent it)."
    - "PROP-0037/DEC-0079 — consecutive-SHIPPED-WITH-CAVEATS>=3 cohere-gate; triage."
    - "pl-2026-06-03-005 (margit card-referrals: witch-label monument + east-water-gate-lanes + muddy-way) before /and-review verdict b01."
