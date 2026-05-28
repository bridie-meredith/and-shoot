```yaml
audit:
  scope: chapter
  target: b01c05
  timestamp: 2026-05-28
  verdict: FINDINGS-PRESENT
  finding_counts:
    HARD: 1
    SIGNAL: 2
    FLAG: 2
  findings:

    - id: fault-001
      type: fault
      what: >
        b01c05s03, chunk line 2 (draft line 128):
        "The Rushwick reads differently in review than it read in acquisition."
        This sentence is untagged. It immediately precedes the [mechanism:] block
        that explains it and the [event:] tag that registers the recognition. The
        sentence is the pivotal story claim of the chapter — it announces the
        central perception shift — and is load-bearing under URI-CHUNK-TAG-PROTOCOL.
        No [event:], [image:], [force:], or [mechanism:] tag is applied to it.
      why: >
        This is the hinge sentence of the entire b01c05 arc. If /and-write receives
        the chunk with the pivot claim untagged, the bones pass may not anchor a
        bone to this exact moment. The opening of political_register-prot's account
        depends on the audience seeing the recognition arrive — if the pivot is not
        tagged, it risks being absorbed into surrounding texture rather than receiving
        its own bone and substance note at the writing stage. Downstream structural
        gap at the bones level.
      criteria: >
        The sentence "The Rushwick reads differently in review than it read in
        acquisition" (or the equivalent pivot claim that announces the register-shift)
        must carry a chunk tag — [event:] or [mechanism:] — that marks it as
        load-bearing. The mechanism block that follows may remain; the tag must appear
        on the claim itself, not only on the explanation.

    - id: fault-002
      type: flag
      what: >
        b01c05s02, chunk line 3 (draft line 66):
        "The third sighting is five days into the Rushwick coverage."
        This sentence announces the time-anchor of the third observation —
        the event that establishes the recurrence pattern for the cf-d10 thread.
        It is not directly tagged. The closing [event: cf-d10-courier-face thread
        initiated — courier body flagged as recurring, three observations now logged...]
        covers the pattern retroactively, but the third-sighting announcement itself
        is untagged.
      why: >
        The third sighting is the specific trigger that activates the recurrence
        classification. Without a tag on the announcement, the bones author receives
        the third sighting as implicit setup text rather than a discrete event. The
        cf-d10 thread anchor (the courier will be recognized again at d10) depends
        on /and-write having a clear event hook for the third observation. Partial
        coverage by the closing cf-d10 event tag means the gap is low-severity, but
        the tag does not confirm the time anchor (five days in) or the observation
        itself — only the filing result. This is a SIGNAL, not a FAULT, because the
        retrospective event tag partially covers it and the load-bearing element
        (thread initiation) is tagged.

    - id: fault-003
      type: flag
      what: >
        b01c05s01, axes_held[political_register-prot].rationale (draft lines 47-48)
        and b01c05s02, axes_held[moral_framework].rationale (draft lines 106-107).
        Both rationales are compound multi-clause strings: s01's political_register-prot
        rationale runs four semicolon-separated clauses; s02's moral_framework rationale
        runs three clauses with an embedded parenthetical. Schema constraint
        (per audit dispatch): "axes_held[].rationale is one line and names the discipline."
      why: >
        Over-long rationales at the chunk layer surface ambiguity about what the
        actual held-discipline claim is. The schema's one-line constraint forces the
        author to commit to a single discipline statement; compound clauses produce
        rationales that partially describe the scene rather than naming the hold.
        Non-blocking (both rationales do name the discipline) but violates the
        schema's form constraint.

    - id: fault-004
      type: flag
      what: >
        b01c05s01, chunk lines 29-33 (draft lines 29-33):
        "A message-runner passes the junction at the double-step of someone on a
        specific errand. The feed tracks him to the lane-mouth and releases him from
        coverage range. Taylor reads: message-running body, institutional function,
        no anomaly."
        These sentences describe body-movement in the feed (a story event: message-
        runner observed, tracked, released) without a chunk tag. They appear inside
        the [force:] block's supporting passage.
      why: >
        The message-runner passage is illustrative texture rather than load-bearing
        (this body does not recur; no cf- thread is opened). The surrounding [force:]
        tag provides context. Non-blocking, but the body-movement sentences are
        technically story events without tags. Noted for /and-write: bones author
        should treat this as supporting texture inside the force-block's bone rather
        than a discrete event bone.

    - id: fault-005
      type: signal
      what: >
        Roll-up math discrepancy: book/series notes declare political_register-prot
        +3 at d05; chapter b01c05 delivers +1.5 against cl-d05.
        
        Evidence:
        - Series axis notes (memory.md line 165): "d05 resentment readable (+3 from 1 to ~4)"
        - Book substance_delta notes (memory.md line 1556): "d05 readable-resentment (+3)"
        - cl-d05 gain field (memory.md line 1363): "political_register-prot +3"
        - Chapter b01c05 target_delta_magnitude: 1.5 (memory.md line 3410)
        - Scene s03 target_delta_magnitude: 1.5 (draft line 164)
        
        The chapter delivers exactly 1.5 of the 3.0 landmark declared at d05 in both
        the book and series plans. The remaining 1.5 ranks have no declared home in
        this chapter plan.
      why: >
        If the remaining +1.5 is not assigned to an adjacent chapter (b01c06 or
        earlier in c05's plan), the d05 landmark will land at rank ~2.5 rather than
        the book-declared ~4. The book and series plans both treat rank ~4 as the
        d05 end-state for political_register-prot; a shortfall of 1.5 would compress
        the window for d09 articulated-contempt and d13 contempt-without-refusal
        arrivals, which depend on a steeper early accumulation curve. This may be
        a deliberate split across chapters (c05 opens the account; subsequent chapters
        carry the remainder), but the chapter plan does not document this and the
        cl-d05 gain field declares +3 as a single unit. Screen-writer must confirm
        whether the remaining +1.5 is assigned downstream and to which chapter.
```

---

## Summary

**Verdict: FINDINGS-PRESENT. HARD: 1 | SIGNAL: 1 | FLAG: 3.**

The chunk set is substantively coherent: the three-scene structure delivers the chapter goal (color arrives before Taylor names it; cf-d10 courier thread planted), the roll-up math is internally consistent (scenes sum to chapter target), cl-d05's cost is made legible in s03's prose, mechanism tags are specific causal claims rather than theme-restatements, and Earth-Bet fence is clean. One HARD finding: the pivot sentence of s03 ("The Rushwick reads differently in review than it read in acquisition") is untagged under URI-CHUNK-TAG-PROTOCOL — this is the most load-bearing single sentence in the chapter and must carry a chunk tag before /and-write receives the file. One SIGNAL: book and series plans declare +3 at the d05 landmark but the chapter plan assigns only +1.5 to cl-d05, leaving 1.5 ranks unaccounted for; screen-writer must confirm distribution. Three FLAGS: s02's third-sighting announcement is partially covered but not directly tagged; rationales in s01 and s02 exceed the one-line schema form constraint; s01's message-runner body-movement sentences are untagged illustrative events inside a force block.
