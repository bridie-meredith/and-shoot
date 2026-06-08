audit:
  scope: book
  target: b01
  timestamp: 2026-06-06
  subject: /and-cohere b01 all AGGREGATE (rolled-up verdict + Phase 3 triage + parking-lot item + state write)
  summary:
    faults: 5      # fault-001..005 — ALL RESOLVED by fixer pass (cohere-b01-all-aggregate-audit fixer log)
    flags: 2       # flag-001, flag-002 — advisory, no action
    passes: 10     # pass-001..010
  resolution_note: "All 5 faults resolved 2026-06-06 (commit 8481c2f). See active-project/staff/fixer/fixer-log.md."
  findings:

    # ---------- AXIS 1 — VERDICT MATH ----------
    - id: fault-001
      type: fault
      what: "aggregate triage_note (report front-matter + Phase 3 DROPPED naive-q6 bullet) — 'naive-q6 is design-inherent + principal-accepted at DEC-0105'"
      why: |
        DEC-0105 authorizes skipping the depth-pass revise loop before running /and-review verdict b01
        ("accept the pre-authorized Class-B cohort caveat and run /and-review verdict b01 now"). It says
        nothing about treating naive-q6 (apparatus-register cumulative load) as design-accepted at
        whole-book COHERE scope. The per-chapter DEC chain (DEC-0060..DEC-0104) pre-authorized
        SHIPPED-WITH-CAVEATS on apparatus register for individual chapters at Phase 9; none adjudicate
        the cohere aggregate verdict's load-bearing naive-q6 axis. The triage conflates the depth-pass
        skip (DEC-0105's actual subject) with cohere-axis acceptance (which DEC-0105 does not grant).
        The substantive case for the drop is strong (the per-chapter chain + DEC-0109 ratify it) but the
        CITATION is imprecise/circular (DEC-0109 was authored by this run's own admin dispatch).
      criteria: "Cite a DEC that adjudicates apparatus-register at COHERE scope, OR correct the note to describe DEC-0105's true scope (depth-pass deferral) and justify the drop on the per-chapter chain (DEC-0060/0062/0066/0072/0074/0085/0087/0090/0096/0099/0104) + DEC-0109 directly."
      resolution: RESOLVED
    - id: pass-001
      type: pass
      what: "load_bearing_fails count (=2) and FAIL-COHERE verdict"
      why: "Q6 FAIL (load-bearing) + dramatist promise/payoff REVISE (load-bearing) = 2. Audience SUBSTANCE-FELT = not FLAT = PASS. Naive Q5 FAIL correctly non-load-bearing; dramatist scene-shape REVISE correctly non-load-bearing. Math internally consistent."
    - id: pass-002
      type: pass
      what: "naive Q2 and Q4 in caution_axes"
      why: "Both are load-bearing axes but returned CAUTION (not FAIL) → caution_axes not failed_axes. Correct; no misclassification."

    # ---------- AXIS 2 — FORK-TO-AGGREGATE DRIFT ----------
    - id: pass-003
      type: pass
      what: "naive fork row vs naive report front-matter"
      why: "Aggregate 'Q1 PASS · Q2/Q3/Q4 CAUTION · Q5 FAIL · Q6 FAIL · Q7/Q8 CAUTION' matches naive front-matter exactly. No drift."
    - id: flag-001
      type: flag
      what: "aggregate dramatist row + caution_axes token dramatist-scene-shape"
      why: |
        Dramatist fork returned scene_shape_distribution: REVISE, but the aggregate lists
        dramatist-scene-shape in caution_axes. This is CORRECT per the cohere gate (non-load-bearing
        axis; REVISE normalizes to caution for the FAIL gate). Advisory only: the front-matter
        caution_axes field loses the CAUTION-vs-REVISE distinction for non-load-bearing dramatist axes —
        a downstream state-file consumer cannot recover which returned REVISE vs CAUTION. No action.
    - id: pass-004
      type: pass
      what: "audience fork row SUBSTANCE-FELT / PASS (not FLAT)"
      why: "Audience verdict is SUBSTANCE-FELT; aggregate maps it as PASS on the load-bearing audience axis. No drift."

    # ---------- AXIS 3 — TRIAGE SOUNDNESS ----------
    # (fault-001 above covers the DEC-0105 authorization gap)
    - id: pass-005
      type: pass
      what: "distinction between Sera on-page non-naming (pl-2026-05-28-002) and Sera payoff-weight drop"
      why: "pl-2026-05-28-002 = on-page articulation is by design (facet layer). The dramatist finding = whole-book reader-reception payoff (reader never feels Sera's weight; c20 doesn't confirm protection). Genuinely distinct; aggregate does not conflate them. The surviving finding is legitimately fresh at whole-book scope."
    - id: pass-006
      type: pass
      what: "no load-bearing fail dropped that should not have been"
      why: "Only two load-bearing fails existed; dramatist-promise-payoff kept (queue), naive-q6 dropped (authorization-citation problem per fault-001, but substantively correct). No other load-bearing axis silently dropped."

    # ---------- AXIS 4 — STATE CONSISTENCY ----------
    - id: fault-002
      type: fault
      what: "state file b01-all-state.md revise_queue[0] — duplicate result key (result: null AND result: SKIPPED)"
      why: "YAML duplicate key = well-formedness violation; conforming parsers cannot reliably parse. Schema defines result as a single field (enum PASS|FAIL|HELD|SKIPPED). The result: null must not coexist with result: SKIPPED. (Introduced by the admin DEC-0108 edit.)"
      criteria: "Exactly one result key per revise_queue entry; the null initial value stamped to SKIPPED in-place, not duplicated."
      resolution: RESOLVED
    - id: flag-002
      type: flag
      what: "state file final_verdict: null with status: dismissed"
      why: "Schema-conformant (dismissed → final_verdict: null). Advisory: a FAIL-COHERE run deliberated to accept-with-notes differs structurally from the schema's envisioned /and-cut dismissal; status: dismissed suppresses the FAIL-COHERE verdict from the closing record. No resume risk (Phase 0 scans status: open). No action — but fault-005's command-body documentation closes the conceptual gap."
    - id: pass-007
      type: pass
      what: "verdict_trace[0] axes vs report front-matter"
      why: "failed_axes / caution_axes / load_bearing_fails identical between state and report. No mismatch."
    - id: pass-008
      type: pass
      what: "revise_queue chapter target vs parking-lot target.scope"
      why: "Both b01c03 (consistent). [Post-fix: both b01c03 + b01c20 after fault-004 split.]"
    - id: pass-009
      type: pass
      what: "admin_process_critic entry — OK-MERGED / PROP-0042 / DEC-0109"
      why: "PROP-0042 recurrence_count: 4 with b01-all ref appended; DEC-0109 = OK-MERGED. State summary (recurrence 3→4) matches proposals file. Consistent."

    # ---------- AXIS 5 — QUEUE / PARKING-LOT WELL-FORMEDNESS ----------
    - id: fault-003
      type: fault
      what: "pl-2026-06-06-cohere-001 id format — cohere- infix violates schema pl-<YYYY-MM-DD>-<NNN>"
      why: "Schema (lines 21/43) specifies pl-<YYYY-MM-DD>-<NNN> with no infix. The cohere- infix is a SYSTEMATIC deviation (pl-2026-06-01-cohere-001..005 + this item). Schema-vs-practice drift; conforming ID parsers fail."
      criteria: "Bring ID format and schema into alignment. PINNED: amend schema to pl-<YYYY-MM-DD>[-<label>]-<NNN> (legitimize the established convention); do NOT rename items."
      resolution: RESOLVED
    - id: fault-004
      type: fault
      what: "pl-2026-06-06-cohere-001 — single item for a two-chapter (c03 + c20) fix"
      why: "Schema (line 90): 'One item per atomic resolution. If a finding needs work at two distinct downstream points, file two items.' The item's own note + resolution_suggestion name c03 establish + c20 confirm, but target.scope is only b01c03 — the c20 confirm-leg is untracked; /and-write b01c20 Phase 0 would not surface it."
      criteria: "File a second item targeting b01c20 (the confirm-leg) so both resolution points are tracked independently."
      resolution: RESOLVED
    - id: pass-010
      type: pass
      what: "pl-2026-06-06-cohere-001 severity (SOFT) vs aggregate's deferred (non-auto-fire) treatment"
      why: "SOFT = surfaced in exit summary, advisory, does not block. Aggregate defers (does not auto-fire). Consistent."

    # ---------- AXIS 6 — PROTOCOL FIDELITY ----------
    - id: fault-005
      type: fault
      what: "Phase 4 not fired without --dry-run flag — disposition path undefined by command body"
      why: |
        The /and-cohere command body defines exactly one Phase-4-skip path: --dry-run. It otherwise flows
        unconditionally Phase 3 → Phase 4 on FAIL-COHERE. The aggregate deferred Phase 4 on Rule 13
        grounds (route fire-vs-defer to admin), citing DEC-0108. But Rule 13 governs routing QUESTIONS to
        admin, not admin authority to skip a mandatory command phase. The result is a state disposition
        (result: SKIPPED with flags.dry_run: false) that the command body provides no defined path to —
        even though the cohere-state schema's SKIPPED enum + 'principal-dismissed' language contemplate it.
        Highest-stakes finding: the underlying decision (reversibility, cost, declared-next-step analysis)
        is defensible, but the PATHWAY lacked a command-body anchor.
      criteria: "One of: (a) command body defines an explicit Phase 4 principal-routing fork; (b) the run used --dry-run; (c) a principal-dismiss mechanism is defined in the command body alongside --dry-run. PINNED REMEDY: (c) — document the principal-defer fork the schema's SKIPPED/dismissed enum already permits."
      resolution: RESOLVED
