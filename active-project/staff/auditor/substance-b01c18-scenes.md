```yaml
audit:
  scope: chapter
  target: b01c18
  timestamp: 2026-06-05
  findings:

    - id: fault-001
      type: fault
      what: >
        b01c18s05 substance_delta.axes_in_motion[political_register-prot].notes:
        "cl06 fully landed at this scene"
      why: >
        cl06's declared total gain is political_register-prot +5. c18 delivers +2.0
        (s03 +1.5, s05 +0.5), bringing the political_register-prot aggregate to 7.5
        (near-saturation) per the handoff_out. c19's chapter contract draws political_
        register-prot +1.5 anchored at cl06 with notes "cl06 paid," taking the axis to
        rank 9 LOCKED. The c18 s05 "fully landed" assertion is therefore false: 2.0 of
        cl06's 5.0 gain has been delivered at c18, not 5.0. If "fully landed" is read
        literally by any downstream consumer (screen-writer, fixer, auditor, or
        /and-substance book b02), it will appear that cl06 is exhausted, making the c19
        draw look like an overage or double-draw on a closed ledger entry. c19's
        handoff_out already shows rank 9 LOCKED on this axis; if cl06 is treated as
        closed at c18, the c19 +1.5 draw becomes unanchored.
      criteria: >
        The s05 notes for political_register-prot must not claim cl06 is fully landed.
        The note must accurately represent the status of cl06 at c18 close: that c18's
        c18-allocated portion (+2.0) of cl06 has been delivered, and the remaining +1.5
        will draw at c19 per that chapter's contract. "cl06 c18 allocation complete" or
        equivalent non-exhaustion language replaces "cl06 fully landed."

    - id: fault-002
      type: fault
      what: >
        b01c18 handoff_out world_state: "position-world rank 9; political_register-world
        rank 9" — both values stated at rank 9 at c18 close.
      why: >
        c18 draws position-world +1.0 (cl07b; s04 notes say "cl07b begins delivering
        its position-world gain") and political_register-world +1.0 (cl07c; s04 notes
        say "cl07c begins"). The use of "begins" in both notes confirms these are the
        first cl07b/cl07c gain deliveries. c20's chapter contract draws position-world
        +1.0 (cl07b; notes "cl07b gain completed") and political_register-world +1.0
        (cl07c; notes "cl07c completed"). Two +1.0 draws on each axis remain: one
        at c18, one at c20. For both to land at rank 9 the pre-c18 baseline would have
        to be rank 8, making c20's draw put both axes at rank 10, which exceeds the
        series end_rank cap (9). The consistent reading is: pre-c18 baseline = rank 7
        (from cl-world-d04/cl-world-d07 prior draws), c18 brings both to rank 8, c20
        brings both to rank 9. The c18 handoff_out overstates by +1 rank on each axis.
        This error cascades: c19 handoff_in inherits "rank 9" on both world axes, and
        c20 handoff_in inherits the same — then c20 attempts a +1.0 draw on axes already
        stated at their series cap. /and-substance chapter b01c20 Phase 0 continuity
        check will encounter an apparent overage on two axes.
      criteria: >
        c18 handoff_out world_state must state position-world rank 8 and
        political_register-world rank 8 at c18 close, consistent with c18 delivering
        the first +1.0 draw on cl07b/cl07c from a rank-7 baseline, leaving c20 to
        deliver the second +1.0 draw that reaches rank 9 LOCKED. If the pre-c18
        baseline on either axis is confirmed as rank 8 by upstream chapter auditing,
        the handoff_out values should be updated to reflect the correct baseline-plus-
        c18-draw total, not assumed rank 9.

    - id: fault-003
      type: flag
      what: >
        b01c18s02 substance_delta.axes_in_motion[moral_framework].notes:
        "cl02 cost side completed"; c18 handoff_in shows moral_framework aggregate at
        -3 (i.e., 3 degradation units already paid); cl02's total declared cost is
        moral_framework -3.
      why: >
        If the entire -3 aggregate at c18 handoff_in was drawn under cl02, then cl02's
        cost side was fully exhausted before c18, and the c18 -1.0 draw is attributed
        to an entry with no remaining capacity. Alternatively, if prior draws split
        -3 across multiple ledger entries (cl03a at -2, cl-d06 at -1, cl05 at -1
        being the other moral_framework-cost entries in the ledger), some portion of
        the prior -3 aggregate may have been drawn on non-cl02 entries, leaving cl02
        capacity for c18. In that case "completed" is accurate. Without a full upstream
        draw-by-draw audit this cannot be verified from c18's scope alone. The risk:
        if cl02 cost was already exhausted before c18, the c18 s02 anchor is
        mis-attributed, and the "completed" annotation will mislead downstream roll-up
        verification. The book-level cl02 accounting at /and-substance book b02 Phase 0
        continuity check may surface this as a double-draw detection. Classified as
        flag (not fault) because the c18 content is internally consistent — only the
        anchor attribution is uncertain pending upstream verification.
      criteria: null

    - id: fault-004
      type: flag
      what: >
        Parking-lot item pl-2026-06-04-c17-001 remains status: open. c18 draft
        satisfies the item's resolution suggestion ("document cost-forward carry to
        d14") with explicit notation at s01, s02, s03, s05 axes_held[relational_anchor_status]
        and in AUTHORING NOTES section (c). The content disposition is coherent.
      why: >
        The parking-lot item remains open at b01c18 Phase 5, but the draft has
        resolved the substance question it raised. The open status means /and-substance
        chapter b01c19 Phase 0 will surface this item again as an unresolved SOFT item
        targeting b01c18, potentially causing unnecessary Phase 0 noise. The item should
        be stamped resolved (resolved_by: "/and-substance chapter b01c18 Phase 3 — cost-
        forward carry to d14 documented at every applicable scene"; resolved_at: current
        timestamp). Not a content fault; a process-hygiene item.
      criteria: null

    - id: fault-005
      type: pass
      what: >
        Check 1 — chunk text vs substance_delta axis-rank claims. Four specific
        tests: s02 moral_framework -1.0 irrevocable act in prose; s03 political_
        register-prot +1.5 court-read-at-scale staging; s04 position-world +1.0 /
        political_register-world +1.0 succession-move landing; s02+s05 collapse
        allocations.
      why: >
        (a) s02 irrevocable act: full-coverage simultaneous node activation, body-count
        running past the prior-city number, Khepri-echo named, Wren's gap-lane held
        blank amid maximum density — all concretely in the prose. (b) s03 court-read-
        at-scale: grooms with variant saddlebag patterns, maids with Green and non-Green
        contact points, knight's enclosed-grip style, septa whose timing matches a
        ward-elder handoff interval — specific bodies with specific functions, the
        machinery entire. (c) s04 succession move: intelligence product delivered in
        three drops over 24 hours (format named), counter-bundle returns single margin-
        cipher line confirming document moved. (d) s02 collapse: deployment makes Taylor
        "more load-bearing" and therefore "more precisely disposable" — concrete
        structural statement in s02. s05 collapse: accounting close names "the network
        now covers more bodies than it covered before this fortnight" and "Taylor is
        more load-bearing to the apparatus" with the "disposal calculus visible." All
        four tests PASS.
      criteria: null

    - id: fault-006
      type: pass
      what: >
        Check 3 — THEMATIC-AXIS-coverage (URI-CONTRACT-THEMATIC-AXIS). Chapter goal
        names the irrevocable deployment and moral_framework collapse as its thesis.
      why: >
        moral_framework is declared in axes_in_motion at s02. political_register-prot
        (the contempt near-saturation) is also in motion and named in the goal. No
        thesis axis is undeclared or held when it should be in motion. PASS.
      criteria: null

    - id: fault-007
      type: pass
      what: >
        Check 4 — sum/enum mechanical checks. Six axes_in_motion; per-scene sums vs
        chapter contract; direction membership; magnitude floors; held-axis rationale
        presence; stakes_axis containment.
      why: >
        All six axes sum exactly to chapter contract (roll-up verification table in
        AUTHORING NOTES section (b) confirmed correct): moral_framework -1.0 exact,
        political_register-prot +2.0 exact, position-world +1.0 exact, political_
        register-world +1.0 exact, position-prot-collapse -1.0 exact, social_tether-
        prot-collapse -1.0 exact. All directions are "up" or "down." All magnitudes
        are > 0 (0.5 minimum at split scenes). All held axes carry explicit rationale
        prose. All five scenes have stakes_axis ∈ union(in_motion, held) for that
        scene. PASS.
      criteria: null

    - id: fault-008
      type: pass
      what: >
        Check 5 — cl-d11 partial-settle (pl-2026-06-04-c17-001). c18 holds
        relational_anchor_status flat and documents the +0.5 as cost-forward-carry-
        to-d14.
      why: >
        The disposition is coherent. The remaining cl-d11 +0.5 tranche is not settled
        at c18 because Wren is screened throughout the deployment and her gap-lane is
        held blank — no recognition event fires that would move the axis. The cost-
        forward carry to d14 is explicitly documented at four scene-level rationales
        (s01, s02, s03, s05) and in AUTHORING NOTES section (c). The choice to carry
        rather than force-settle is structurally justified: the recognition event cl-d11's
        remaining tranche requires (Wren's operational weight becoming un-ignorable)
        belongs to d14's collapse settlement, not to a chapter where Wren is screened
        and the axis is structurally held. PASS on this check.
      criteria: null
```
