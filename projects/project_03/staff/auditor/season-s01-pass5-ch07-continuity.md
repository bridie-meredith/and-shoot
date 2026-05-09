audit:
  scope: episode
  target: chapter-07 (proto-lines) — Pass 5 Continuity
  timestamp: 2026-05-07
  file_level: FAIL
  special_focus_adjudicated:
    - IDs 95-96 (Rowan produces/sets parchment): COHERENT
    - ID 93 (Plumm takes claim document): FAULT — POV violation, not spatial collision
    - ch07 → ch08 boundary: COHERENT
  total_lines_checked: 79  # content lines, excluding blank timeskip IDs 16/28/36/43/67/72/82/85
  findings:

    - id: fault-continuity-001
      type: fault
      what: ch06→ch07 boundary — Taylor and Rowan transit from sept environs to Harrenhal recorder's room
      why: >
        Ch06 ends with Taylor at the sept environs (IDs 103–105: Taylor drops, presses hands, ravens land;
        Rowan has tucked the parchment at ID 114). Ch07 opens with the recorder processing a filing (IDs 1–3)
        and Taylor pressing the recorder's counter (ID 4). The recorder's room is an interior Harrenhal
        administrative space, approximately half a league from the sept environs per the studio state file
        (loc-harrenhal-sept-environs, harrenhal-towers recorded as NORTH, HALF A LEAGUE). No transit beat
        is recorded in ch06 or at the open of ch07 covering Taylor's and Rowan's movement from sept to
        the Harrenhal recorder's room. Taylor arrives at the counter (ID 4) without any recorded approach,
        entry, or gatehouse clearance. This is a reachability fault: the body cannot be at a location
        it has not traveled to.
      class: FAULT-CONTINUITY-REACHABILITY
      criteria: >
        The file (or a preceding interlude/bridge) must establish Taylor and Rowan's transit from sept
        environs to the Harrenhal recorder's room before ID 4 can stand. The transit must cover: departure
        from sept, half-league road travel, arrival at Harrenhal, and entry to the recorder's room. If this
        transit is established by a ch06-close interlude or a ch07-open transit block, the chapter-07 file
        must reference or follow from that established arrival state.

    - id: fault-continuity-002
      type: fault
      what: ID 93 — `ser-harwick-plumm takes the claim document` — POV violation in Taylor-POV file
      why: >
        Chapter-07 is a Taylor-POV file (narrator: taylor-hebert-westeros). At ID 93, Taylor's position
        is at the sept doorframe (IDs 90–92 establish her exiting the sept, passing the sept door, and
        gripping the sept doorframe — she is at loc-harrenhal-sept-environs, at or near the sept entrance).
        The recorder's room where the claim document would be located is inside Harrenhal, approximately
        half a league north. Taylor cannot observe Plumm taking a document inside Harrenhal from the sept
        doorframe with normal perception. No fauna-assisted observation beat precedes ID 93 in this
        sequence (the raven launches at ID 68 and Taylor releases the wall at ID 98; no active fauna
        channel is established pointing at the recorder's room at this point in the chapter). ID 93 records
        an action by Plumm at a location Taylor cannot witness, in a Taylor-POV file, without any
        established observational bridge. This is a POV fragmentation fault.

        Note on spatial collision adjudication: Plumm himself is not spatially incoherent. He exited the
        recorder's room at ID 27. He could return to the recorder's room or remain in Harrenhal interior
        and take the document there. The fault is not that Plumm is in the wrong place — it is that
        Taylor cannot witness the action from where she stands, and the file does not establish how she
        knows this event occurred.

        Additional structural context: The Pass 3 shape report (ch07-pass3-shape.md) issued a
        STRUCTURAL-FAILURE verdict and prescribed a specific re-order placing ID 93 immediately after
        ID 15 (early in the sequence, before Plumm's recorder-room scene). The current as-filed sequence
        retains ID 93 at the chapter's end (between IDs 92 and 94). The Pass 3 re-order was not applied.
        This means the structural fix that would have resolved the double-peak and POV-fragmentation flags
        has not been executed. ID 93 at the chapter's end in a Taylor-POV file is unresolvable as written
        without either: (a) an established fauna observational beat covering the recorder's room at this
        moment, or (b) re-ordering to place ID 93 in the pre-Plumm-exit sequence where it is legible as
        an administrative action Taylor witnesses directly (she is present at the counter through ID 15).
      class: FAULT-CONTINUITY-POV
      criteria: >
        ID 93 at its current position (between IDs 92 and 94, with Taylor at the sept doorframe) must
        be resolved by one of: (a) establishing a fauna-channel beat that gives Taylor remote observation
        of the recorder's room at this moment in the sequence; (b) re-ordering ID 93 to a position where
        Taylor is physically present at the recorder's room and can directly witness Plumm taking the
        document (consistent with the Pass 3 prescribed re-order, which places 93 between IDs 15 and 17);
        or (c) removing ID 93 and routing the Plumm-takes-document action to a non-POV file or interlude.
        The Pass 3 structural re-order (if applied) resolves this without new authoring.

    - id: fault-continuity-003
      type: fault
      what: Pass 3 structural re-order not applied — file remains in STRUCTURAL-FAILURE state
      why: >
        The Pass 3 shape audit (ch07-pass3-shape.md) returned verdict STRUCTURAL-FAILURE on grounds of
        DOUBLE-PEAK (IDs 77–80 competing with IDs 62–65) and POV-fragmentation (IDs 43–50 and 73–81
        recording scenes Taylor cannot witness). The Pass 3 report prescribed an explicit re-order:
        `1–15, 93, 17–27, 43–50, 73–81, 83–84, 29–34, 36–41, 52–66, 68–71, 86–92` and directed:
        "apply prescribed re-order → route inert-stretch decision to screen-writer → add transition
        beat → pass 2 on new beats → pass 3 re-evaluate."

        The current ch07.md does not reflect this re-order. The file retains its pre-Pass-3 ID sequence
        with only the Iter1 additions (IDs 95–96 and 97–98) inserted at their narrative positions.
        The POV-fragmentation blocks (IDs 17–27: Plumm in recorder's room; IDs 43–50 and 73–81:
        other non-POV blocks per Pass 3 identification) remain interleaved in the Taylor-POV sequence.
        The double-peak has not been resolved by re-ordering.

        Pass 5 continuity cannot certify a file as structurally coherent when the Pass 3 re-order has
        not been executed. The structural re-order is a prerequisite for continuity-level review of
        POV consistency across the chapter.
      class: FAULT-CONTINUITY-CAUSE-EFFECT
      criteria: >
        The Pass 3 prescribed re-order must be applied before the file can pass Pass 5 continuity.
        The prescribed sequence is: IDs 1–15, 93, 17–27, 43–50, 73–81, 83–84, 29–34, 36–41, 52–66,
        68–71, 86–92 (plus Iter1 additions 95–96 at their insertion point between IDs 5 and 6, and
        97–98 at their insertion point between IDs 71 and 72). After re-order, Pass 3 re-evaluation
        must confirm the double-peak is resolved and POV-fragmentation blocks are correctly
        sequenced. Only then does Pass 5 continuity review proceed.

    - id: fault-continuity-004
      type: fault
      what: ID 62 — `septon-rowan produces a document` at the cottage — prop custody gap
      why: >
        In the cottage scene (IDs 52–66), Rowan produces "a document" (ID 62) that Taylor then reads
        (ID 63: `taylor-hebert-westeros turns the document`). The prop identity of this document is
        ambiguous, and its custody chain is broken.

        Rowan's parchment (the wardship claim) was drafted and sealed in ch06 (IDs 31–45, ID 114:
        `septon-rowan tucks the parchment`). At ch07 open, IDs 95–96 show Rowan producing and setting
        this parchment at the recorder's counter. After the refusal is stamped (IDs 9–11: recorder stamps
        refusal entry, closes ledger), there is no beat recording the recorder returning the parchment
        to Rowan, and no beat recording the parchment leaving the counter or being retained by the
        recorder. Then, at ID 62 in the cottage, Rowan produces "a document." If this is Rowan's
        original claim parchment, the prop custody chain between ID 96 (parchment set on counter) and
        ID 62 (parchment produced at cottage) is unrecorded. If it is a different document (a refusal
        notice, a copy), that document has no establishment beat and no stated origin.

        Downstream: Taylor reading the document at ID 63 is the chapter's structural climax (per Pass 3:
        "Climax: IDs 62–65 — Taylor receives and reads the document Rowan produces"). A climax beat
        anchored to a prop with a broken custody chain is a continuity failure at the most load-bearing
        moment in the chapter.
      class: FAULT-CONTINUITY-STATE-PERSISTENCE
      criteria: >
        The document Rowan produces at ID 62 must have a complete and unbroken custody chain from its
        origin through to its appearance in Rowan's hand at the cottage. If it is the original claim
        parchment: a beat must establish the recorder returning it to Rowan (or Rowan retrieving it)
        between IDs 96 and 62. If it is a different document (refusal notice, administrative copy):
        that document must be established with a source beat before Rowan produces it. The prop
        identity must be unambiguous at ID 62.

    - id: fault-continuity-005
      type: fault
      what: IDs 17–27 — Plumm in recorder's room — non-POV scene in Taylor-POV file without fauna bridge
      why: >
        IDs 17–27 record an extended scene inside the recorder's room: Plumm enters, files his claim,
        and the recorder processes it. At ID 15, Taylor crosses the yard (she is at loc-harrenhal-sept-
        environs, having exited Harrenhal after the refusal). At ID 16 (blank timeskip), the POV
        transitions to the recorder's room interior. Taylor has no established line of sight or fauna
        channel into the recorder's room at this point. The recorder's room has no windows per studio
        state implications (it is an interior administrative space). No fauna-use beat precedes this
        block for this observational purpose. IDs 17–27 are 11 beats of action Taylor cannot witness
        from her position outside Harrenhal on the approach road.

        This is the same POV-fragmentation identified in the Pass 3 shape report. The file has not been
        restructured to resolve it. In the Pass 3 prescribed re-order, IDs 17–27 were to be sequenced
        after IDs 1–15 and 93 (while Taylor is still inside Harrenhal at the recorder's room) — but
        as noted in fault-continuity-003, that re-order has not been applied. In the current sequence,
        IDs 17–27 appear after Taylor has crossed the yard (ID 14–15) and exited toward the approach
        road — she cannot witness the Plumm filing.
      class: FAULT-CONTINUITY-POV
      criteria: >
        IDs 17–27 must either: (a) be repositioned per the Pass 3 re-order so they appear while Taylor
        is still inside Harrenhal at the recorder's room (resolving the POV fragmentation by keeping
        Taylor present); or (b) be extracted to a non-POV interlude file with appropriate interlude
        header. Under option (b), the Taylor-POV file would register Plumm's filing through its effects
        on Taylor (e.g., she is told of it, or she learns of it via fauna observation later) rather
        than directly recording Plumm's actions. The Pass 3 re-order (option a) is the lower-cost fix.

    - id: flag-continuity-001
      type: flag
      what: IDs 95–96 — `septon-rowan produces the parchment` / `septon-rowan sets the parchment` — continuity coherent; noted
      why: >
        These Iter1-added beats appear between ID 5 (Rowan reaches the counter) and ID 6 (recorder
        speaks to Rowan). The prop chain is coherent: ch06 IDs 31–45 establish Rowan drafting, sealing,
        and tucking the parchment on his person (ID 114: `septon-rowan tucks the parchment`). At ch07
        ID 95, Rowan produces the parchment from his person at the counter; at ID 96 he sets it on
        the counter for the recorder to review. This is a clean prop-in-hand → prop-on-surface sequence
        immediately followed by the recorder processing the claim. No continuity fault.

        Advisory: "the parchment" at ID 96 requires that the recorder takes or retains it. After ID 96,
        the parchment is on the counter. The recorder then stamps the refusal (IDs 9–10) and closes the
        ledger (ID 11). The parchment's fate after ID 96 is not recorded — this feeds into fault-
        continuity-004 (prop custody gap at ID 62). The IDs 95–96 beats are themselves coherent;
        the custody gap begins at ID 96.
      class: PASS

    - id: flag-continuity-002
      type: flag
      what: IDs 97–98 — `the castle bell strikes` / `taylor-hebert-westeros releases the wall` — continuity coherent; noted
      why: >
        These Iter1-added beats appear between ID 71 (Taylor grips the wall) and ID 72 (blank timeskip).
        Taylor is in the sept yard at this point (IDs 68–71: raven launches, Taylor crosses yard, stops,
        grips wall). The sept is adjacent to Harrenhal; the studio state file records `harrenhal-towers:
        NORTH, HALF A LEAGUE` and confirms Taylor heard a shod hoof on cobbles half a league north
        with normal hearing (taylor-hebert-westeros state.md). A castle bell at Harrenhal, half a league
        distant, would be audible in the sept yard under normal conditions. The beat sequence is
        physically coherent: Taylor grips the wall → bell sounds (external environmental trigger) →
        Taylor releases the wall (physical response to sound). No reachability or cause-effect fault.
      class: PASS

    - id: flag-continuity-003
      type: flag
      what: ch07→ch08 boundary — Taylor crosses outer ward (ID 94) → ch08 opens outer ward → side chamber
      why: >
        Ch07 ends with `taylor-hebert-westeros crosses the outer ward` (ID 94). Ch08 opens with:
        ID 4 `an armed man plants the feet` (environmental/other actor), ID 5 `taylor-hebert-westeros
        crosses the outer ward`, ID 6 `taylor-hebert-westeros enters the side chamber`. The boundary
        is coherent: Taylor is in the outer ward at ch07 close; ch08 ID 5 places her continuing through
        the outer ward into the side chamber. The outer ward is a continuous space within loc-harrenhal-
        exterior. No reachability fault; position persists correctly across the chapter boundary.
        The showrunner memory.md records this path: "ch07 outer ward → ch08 side chamber path now
        recorded per restructure 2026-05-07." Boundary state is confirmed coherent.
      class: PASS

    - id: flag-continuity-004
      type: flag
      what: IDs 29–35 — postern gate inert stretch — continuity coherent but narratively flagged
      why: >
        Pass 3 identified IDs 29–35 as an `[inert-stretch]` (six beats with no consequence, at the
        postern gate guardsman). These beats are continuity-coherent — they record a spatial transit
        from inside Harrenhal to the approach road — but they do not advance the dramatic situation.
        Pass 3 noted: "Cut and supply one transition beat, OR give the guardsman challenge consequence."
        This is not a continuity fault; it is a structural flag carried forward from Pass 3. Pass 5
        records it as advisory for the screen-writer / restructure phase.
      class: flag

    - id: flag-continuity-005
      type: flag
      what: Time compression — IDs 1–15 (Rowan refusal) immediately adjacent to IDs 17–27 (Plumm filing)
      why: >
        The chapter plan states Plumm files "within the same week" of Rowan's refusal. The current
        sequence (blank timeskip ID 16 between IDs 15 and 17) could read as same-day or days later —
        the blank is not specified. The chapter plan's "within the same week" framing is satisfied by
        any reading of the blank. No time-consistency fault. However, if the re-order is applied
        (fault-continuity-003) and IDs 17–27 become adjacent to IDs 1–15 in the Taylor-POV sequence,
        the temporal compression will appear even tighter. Editor should confirm the timeskip blank
        is carrying sufficient time-bridge weight to honor "within the same week" rather than
        same-hour or same-day.
      class: flag

  summary: >
    FILE-LEVEL: FAIL.

    Four continuity faults found. Two flags on Iter1 additions (IDs 95–96 and 97–98) confirm those
    beats are coherent. One flag on the ch07→ch08 boundary confirms that handoff is clean.

    The dominant structural problem is that the Pass 3 re-order was never applied
    (fault-continuity-003). This is the root cause of fault-continuity-002 (ID 93 POV violation)
    and fault-continuity-005 (IDs 17–27 POV fragmentation). If the Pass 3 re-order is applied first,
    fault-continuity-002 and fault-continuity-005 may resolve without additional authoring.

    fault-continuity-001 (ch06→ch07 reachability gap) is independent of the re-order and requires
    either a transit block at ch07 open or a bridge established at ch06 close.

    fault-continuity-004 (prop custody gap at ID 62) is independent of the re-order and requires a
    beat establishing the document's chain between ID 96 (parchment set on counter) and ID 62
    (Rowan produces document at cottage).

    Adjudication on the three special-focus items:
    - IDs 95–96: COHERENT. Prop chain from ch06 tuck → ch07 produce/set is intact.
    - IDs 97–98: COHERENT. Bell audibility at half-league confirmed; cause-effect (bell → release) clean.
    - ID 93 spatial collision: NOT a Plumm spatial collision — Plumm's position inside Harrenhal
      after ID 27 makes the taking-of-document physically possible. The fault is POV: Taylor at the
      sept doorframe cannot witness this action, and ID 93 at that position in the file is a POV
      violation. Resolution via Pass 3 re-order (placing ID 93 early, while Taylor is at the counter)
      is the minimum-cost fix.

    Recommended fixer sequence:
    1. Apply Pass 3 prescribed re-order (resolves fault-continuity-003; likely resolves
       fault-continuity-002 and fault-continuity-005 as side effects).
    2. Add ch06→ch07 transit block (resolves fault-continuity-001).
    3. Establish prop custody chain for document at ID 62 (resolves fault-continuity-004).
    4. Route restructured file to Pass 3 re-evaluation, then Pass 5 re-verify.
