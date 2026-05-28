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

---

## Attempt 2 (2026-05-28)

### fault-001 (HARD — pivot sentence untagged): RESOLVED

The pivot sentence is now the opening clause of the [mechanism:] block at draft lines 133-138. The tag opens on the sentence itself: `[mechanism: The Rushwick reads differently in review than it read in acquisition — ...]`. The claim is not outside the tag; it is the tag's opening statement. Criteria satisfied: the pivot carries a [mechanism:] tag. HARD cleared.

### fault-005 (SIGNAL — multi-chapter distribution unconfirmed): RESOLVED

s03 axes_in_motion notes (draft line 175) now read: "first tranche (+1.5 of +3 cl-d05 ledger gain; remaining +1.5 anchors at b01c06-b01c08 during the readable-resentment escalation toward d09 articulated-contempt)". The split is declared, the downstream chapters named, and the math adds to +3. The chapter plan now documents the deliberate distribution. SIGNAL cleared.

### fault-002 (FLAG — s02 third-sighting untagged): RESOLVED

Draft lines 66-68 now read: `[event: third sighting — five days into the Rushwick coverage; the feed confirms: recurring body, same heel-first gait, same morning-hour transit window]`. The third-sighting announcement, its time anchor ("five days into the Rushwick coverage"), and the observation are all inside a direct [event:] tag. Previously the cf-d10 closing tag covered only the thread-initiation result; the new tag covers the event itself. FLAG cleared.

### fault-003 (FLAG — multi-clause rationales): PARTIAL

s02 moral_framework rationale (draft line 110): "routing enforcement as pattern-data is inside the licensed exception; 'this is what the feed reads' echo is rationalization running, not interrogated." Reduced from three clauses to two. Still two semicolon-separated clauses, which is not one line naming the discipline; form constraint is not fully met, but the reduction is meaningful and the discipline is named in the first clause. FLAG persists on s02, reduced severity. s01 political_register-prot rationale (draft lines 47-48) is unchanged: four semicolon-separated clauses. FLAG persists on s01. Overall: FLAG persists, not resolved.

### fault-004 (FLAG — s01 message-runner untagged): ACCEPTED / UNCHANGED

Screen-writer confirmed this as deliberate (dark-fantasy ACCEPT). No change to draft. FLAG remains on record for /and-write; bones author should treat the message-runner body-movement sentences as supporting texture inside the force-block's bone, not a discrete event bone. No new action required.

### New content audit

**s02 alley-sound passage (draft lines 78-82):** "What it does not return is the sound from the alley before the courier finds his feet — a low, effortful sound, not a cry, the kind a body makes when it is trying not to make any sound at all. The feed has no field for that. It logs: brief contact, courier retained on feet." This passage is untagged. Assessment: illustrative texture inside the [force:] block on observation specificity and [mechanism:] block on enforcement-vs-robbery geometry, both of which precede and frame it. No new thread opened; no axis move anchored here; no downstream cf- tag attached. Same category as fault-004 (message-runner): non-load-bearing prose inside a tagged structural block. No new fault. Noted for /and-write: bones author should absorb this as texture inside the enforcement-event bone, not a separate bone.

**s03 try-flat-read-fails passage (draft lines 162-168):** "She closes the evening review. She tries to run the Rushwick back through the flat-document read... It does not resolve... The neutral read is not available to her for this content anymore, and she files the unavailability as texture, but the filing does not return the read." This follows the [event:] tag at lines 158-161 that announces "political_register-prot opens its account — resentment color present; neutral-instrumentally-observant foreclosed; cl-d05 anchor lands." The passage is the dramatized enactment of the already-tagged foreclosure. It carries no new load-bearing claim beyond what the preceding [event:] tag declares. No tag required; no violation. Clean.

**Mechanism tag specificity (s03 revised [mechanism:]):** The tag reads: "evening replay strips the acquisition-layer's real-time categorization discipline; there is no action to take, no report to route, no function being performed; the content sits without the discipline's organizational frame, and what remains is not flat; the provisioner train's institutional-gait signature carries something that the factual-categorization register was holding at distance during the day." This is a specific causal claim — frame-removal exposes accumulated affect — not a verbatim thesis restatement. Passes the mechanism-specificity check.

**Earth-Bet fence:** No contemporary or non-Westerosi referents in either new passage. Clean.

### Roll-up math confirmation

s01: 0 axes in motion. s02: 0 axes in motion. s03: political_register-prot +1.5. Sum: 1.5. Chapter target: 1.5. Math confirmed unchanged.

---

### Attempt 2 verdict: FINDINGS-PRESENT

**HARD: 0 | SIGNAL: 0 | FLAG: 2**

Both HARD and SIGNAL findings from attempt 1 are resolved. fault-002 (third-sighting tag) resolved. Two FLAGS remain open: fault-003 (multi-clause rationales on s01 political_register-prot and s02 moral_framework — form constraint not fully met; non-blocking) and fault-004 (s01 message-runner untagged — accepted, non-blocking). No new faults introduced by the new content. The chapter chunk set is clear to proceed to /and-write with the two non-blocking flags on record for the bones author.
