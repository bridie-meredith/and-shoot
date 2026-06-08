```yaml
audit:
  scope: chapter
  target: b01c16
  timestamp: 2026-06-04
  findings:
    - id: fault-001
      type: pass
      what: >
        THEMATIC-AXIS-UNDECLARED check. Chapter goal names suppression-vs-foreclosure /
        moral_legibility turn as thesis. Contract lists moral_legibility_to_self in
        axes_in_motion (+0.5, anchored s03). Goal and axis declaration are co-referential —
        the axis is declared, the chapter is about the axis.
      why: No downstream mismatch between stated goal and tracked axis.

    - id: fault-002
      type: pass
      what: >
        Contract-text match: s01. Taylor enters on routine coverage pass. No axis shift
        claimed or legible in prose. She does not stop, does not change register. Consistent
        with "s01 holds moral_legibility_to_self."
      why: No roll-up contribution from s01; contract says hold; prose holds.

    - id: fault-003
      type: pass
      what: >
        Contract-text match: s02. Taylor has the answer ready (s02 lines 5–8: "she has had
        it since the third time"), recognizes the argument is not wrong ("He is not wrong
        about the people he named"), continues. No rank move on moral_legibility_to_self.
        Position-arithmetic runs and the collapse-visibility event fires (see fault-004
        below for collapse-axis discipline check). Consistent with "s02 holds it."
      why: No premature axis movement in s02.

    - id: fault-004
      type: pass
      what: >
        Collapse-axis discipline. Contract holds social_tether-prot-collapse and
        position-prot-collapse as latent-activating (dormant→latent; rank held; collapse
        events contracted to c17 at -1.0 each). s02 prose surfaces the position-arithmetic
        explicitly: "The position is worth less to her now than it costs to hold. Not by a
        margin that triggers a different accounting. By enough to notice." The prose then
        explicitly forecloses the collapse event: "She continues holding it. The position
        will continue to be held until the arithmetic goes somewhere it cannot come back
        from, and it has not done that yet." No collapse event fires. No rank claimed to
        move. The visibility of the arithmetic is consistent with dormant→latent status
        transition; this is what "latent-activating" means. The contract is internally
        consistent with the prose.
      why: >
        No contract-under-declaration. The prose does not fire a collapse event the
        contract says is held. The arithmetic surfacing is a held-but-visible state, not
        a move. c17 collapse events are not anticipated or triggered.

    - id: fault-005
      type: pass
      what: >
        Cheap-gain check: moral_legibility_to_self +0.5. The on-page cost is that Taylor
        forecloses a true argument rather than rebuts it. Evidence: s02 — "He is not wrong
        about the people he named. She knows that. The argument is not wrong. The argument
        addresses the wrong thing." Evidence: s03 — "she has confirmed that the argument is
        not live — what Halvard's question asks for is a response to the contempt, which is
        correct." She does not dispute the argument; she declines to treat it as live. The
        gain (she can articulate suppression vs. foreclosure as distinct) is earned by paying
        the cost (valid challenge closed rather than engaged). Final lines: "She did not
        suppress the recognition. She looked at it… and she walked away from the person
        holding it up. That is not the same thing. She knows the difference. She has the
        accounting for both." The cost precedes the gain in the prose. Not asserted.
      why: No SUBSTANCE-SUSPECT finding. The +0.5 is paid.

    - id: fault-006
      type: flag
      what: >
        s03 final two sentences: "She knows the difference. She has the accounting for both."
        These are direct self-attributions of the moral_legibility axis move — the prose
        explicitly names the gain. The four preceding paragraphs earn it. The flag is that
        the attribution is explicit rather than implied, which places the axis movement in
        narration rather than event.
      why: >
        Not a blocking problem — the earning is on-page before the attribution. Advisory for
        downstream facet and stitch work: the narrator is doing the accounting out loud.
        Whether that register is the right close for this chapter is a voice question, not a
        substance-contract question. No fixer dispatch warranted.
```
