```yaml
audit:
  scope: season
  target: s01 — all 14 proto-line files (chapter-01 through chapter-10, plus chapter-03 interlude split noted below)
  timestamp: 2026-05-07
  pass: S4 — season-scope continuity
  dimensions_checked:
    - reachability
    - state_persistence
    - reference_resolution
    - pov_consistency
    - time_consistency
    - cause_and_effect

  file_level:
    chapter-01.md: PASS
    chapter-02.md: PASS
    chapter-03.md: FLAG (see fault-005)
    chapter-04.md: PASS
    chapter-05.md: PASS
    chapter-06.md: PASS
    chapter-07.md: PASS
    chapter-08.md: FLAG (see fault-007)
    chapter-09.md: FAULT (see fault-001, fault-003)
    chapter-10.md: FAULT (see fault-002, fault-006)

  findings:

    # ── REACHABILITY ──────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      fault_class: FAULT-CONTINUITY-REACHABILITY
      chapter: 09
      what: >
        Chapter-09 lines 1–2: taylor-hebert-westeros dispatches a raven and a sparrow.
        Lines 7–14: ser-harwick-plumm enters the gatehouse and speaks to oc-castellan-harrenhal
        (a scene inside Harrenhal's gatehouse room). Lines 36–37: the raven lands on the
        gatehouse sill. The chapter goal states Taylor is observing the argument from her
        fauna instruments. However, taylor-hebert-westeros's last established location
        (studio/state.md, Taylor's state.md carry-forward) is loc-harrenhal-sept-environs —
        specifically the sept exterior yard or sept interior, half a league south of Harrenhal.
        The gatehouse sill (inside the Harrenhal curtain wall) is the watch-point for the raven.
        The chapter's POV depends on Taylor receiving an interior-room audio/visual feed
        from the raven at the gatehouse sill (lines 9–14, 17–27 all depict dialogue and
        document-handling that Taylor can only perceive via the fauna channel). cond-fauna-control-rules
        constrains range and fidelity. The raven on the gatehouse sill would be at the outer edge
        of viable passive-to-active range from the sept (half a league). No prior chapter
        establishes that a raven on the gatehouse sill yields reliable speech-level fidelity.
        The chapter treats the raven's position as giving Taylor a speech-level feed on the
        castellan-Plumm-Bracken argument without establishing that the sill position delivers
        that fidelity at half-a-league range.
      why: >
        If the raven's sill position does not deliver speech-level fidelity at half-league range
        under cond-fauna-control-rules, the entire observational premise of chapter-09 is
        undermined. Taylor cannot know what Plumm says to the castellan, what Bracken says,
        or what the document contains — she can only register gross movement and physical
        proximity. The cause-and-effect chain (Taylor knows what was argued; she knows the
        outcome) is invalid if the channel cannot carry it. This also propagates into chapter-10
        where Taylor appears to have foreknowledge of the administrative resolution.
      criteria: >
        Either (a) a prior chapter or chapter-09 itself must establish that the raven-on-sill
        position at the gatehouse delivers sufficient fidelity for Taylor to perceive voices and
        documents at the table, citing cond-fauna-control-rules range/cost terms; or (b) chapter-09
        must be revised so Taylor observes gross physical behavior only (arrivals, departures,
        document exchanges as physical acts) without speech-level or document-content access,
        and the chapter goal is recalibrated to match that ceiling. The chapter as written must
        not require Taylor to know specific argument content she could not perceive through
        fauna fidelity at that range and position.

    - id: fault-002
      type: fault
      fault_class: FAULT-CONTINUITY-REACHABILITY
      chapter: 10
      what: >
        Chapter-10 lines 1–35: all five active participants (ser-edwyn-celtigar,
        oc-castellan-harrenhal, ser-harwick-plumm, septon-rowan, and taylor-hebert-westeros)
        are simultaneously present "in the hall" at Harrenhal. Taylor's state.md places her
        at loc-harrenhal-sept-environs through episode s01e06. The chapter-10 goal says the
        season's final state shows Taylor "named, placed, and functional inside a structure she
        did not choose." This implies Taylor has been transported from the sept to Harrenhal's
        hall. No prior chapter in the proto-line sequence establishes a transit for Taylor from
        the sept to Harrenhal. The chapter-10 proto-lines open with all actors already present
        in the hall and do not contain a line for Taylor's arrival or transport. The nearest
        prior location for Taylor in the proto-line sequence is inside the sept (chapters 06–08,
        studio/state.md carry-forward to s01e06). Taylor's state file does not record a location
        change to any Harrenhal interior. A half-league transit on foot for an eleven-year-old
        girl under escort is a non-trivial event that cannot be elided without a recorded
        state change.
      why: >
        Without an established transit or escort, Taylor's presence in Harrenhal's hall violates
        the state-persistence rule (nothing changes without being recorded) and the reachability
        rule (she cannot teleport half a league). The wardship resolution scene — the season's
        climactic administrative beat — rests on Taylor being physically present, so this is
        not a minor detail: the entire chapter depends on her presence in a location she has
        not been placed in.
      criteria: >
        A chapter or proto-line segment must establish Taylor's transit from the sept to
        Harrenhal's hall (whether under escort, summoned, or self-walked) and record the
        corresponding location change. Taylor's state file must show loc-harrenhal (or equivalent
        interior) before chapter-10's hall scene opens. The transit may be compressed into a
        time-skip beat but must appear in the proto-line sequence and must update studio/state.

    # ── STATE PERSISTENCE ─────────────────────────────────────────────────────

    - id: fault-003
      type: fault
      fault_class: FAULT-CONTINUITY-STATE
      chapter: 09
      what: >
        Chapter-09 lines 77–101: ser-edwyn-celtigar enters the postern gate and then
        appears in scene with oc-castellan-harrenhal, who produces the document (line 81)
        and the page (line 82). These are the same document and page that ser-harwick-plumm
        presented in chapter-05 (lines 42–55: ser-harwick-plumm draws the record book,
        writes the name, writes the sept entry, etc.) and that oc-castellan-harrenhal last
        held in the chapter-09 Plumm/Bracken contest (lines 10–14, 31–32, 38–46).
        Ser-harwick-plumm's state.md records his last known location as
        westerosi-smallfolk-village-common with an empty inventory. However in chapter-09
        lines 56–60, ser-harwick-plumm exits the outer ward after the argument, and his
        inventory at that point should include the rolled page he produced in chapter-04
        (line 80: "ser-harwick-plumm rolls the page"; line 81: "ser-harwick-plumm pockets
        the roll"). His state.md records inventory as empty — a contradiction. The roll
        that was pocketed in chapter-04 does not appear in his inventory but is implicitly
        active as the "page" in chapters-05, -07, -09.
      why: >
        The rolled page / record book is a load-bearing prop that drives the administrative
        contest across five chapters. If Plumm's state.md does not carry it, studio cannot
        track when it changes hands, who holds it when, and what the castellan is examining in
        chapter-09 lines 84–89. Fixer and editor cannot safely resolve the chapter-09 document
        handling without knowing the prop's chain of custody.
      criteria: >
        Plumm's state file must be updated to carry the rolled page / record book from
        chapter-04 line 81 (pocketed) through each subsequent chapter in which it appears as
        a prop. If the prop was formally transferred to oc-castellan-harrenhal at any prior
        beat, that transfer must be recorded in both actor inventories and studio state.
        The prop's current holder at chapter-09's close must be unambiguous.

    - id: fault-004
      type: fault
      fault_class: FAULT-CONTINUITY-STATE
      chapter: 07
      what: >
        Chapter-07 lines 62–63: septon-rowan produces a document from his satchel, and
        taylor-hebert-westeros flips it. Lines 65–66: taylor-hebert-westeros speaks to
        septon-rowan; septon-rowan speaks back. The document is not named or slugged.
        Chapter-06 established that septon-rowan drafted and sealed a parchment (lines 34–44:
        septon-rowan writes heading, claimant entry, ward entry, grounds clause, closing line,
        lifts the parchment, blows the ink, folds, seals). In chapter-07 line 93, the line reads
        "ser-harwick-plumm takes the claim document." This is the only beat in the chapter-07
        sequence where the guardianship claim document changes hands — but septon-rowan's
        state.md shows his inventory as [folio-with-motherhouse-and-recorder-papers], not
        a sealed succession parchment from chapter-06. The chapter-06 sealed parchment is
        not recorded in Rowan's inventory and is not tracked through chapter-07's custody chain.
        Additionally, chapter-07 line 93 ("ser-harwick-plumm takes the claim document") occurs
        after line 27 ("ser-harwick-plumm exits the recorder's room"), which means Plumm
        takes the claim document in the sept yard while Taylor is there — but the surrounding
        lines (86–92) place Taylor inside and at the sept door, not in a position where she
        witnesses Plumm physically taking the document. This is either a POV gap or a
        temporal collision.
      why: >
        The chapter-06 sealed parchment is the legal instrument on which the entire chapter-07
        refusal and chapter-08/09/10 resolution depend. If it is not in Rowan's inventory
        (or Taylor's, or the recorder's), the recorder cannot have refused it and Plumm cannot
        take it. The prop chain-of-custody is broken between chapter-06 close and chapter-07.
      criteria: >
        The chapter-06 sealed parchment must be added to septon-rowan's inventory at chapter-06
        close and carried into chapter-07. If it was transferred to the recorder's desk and
        then seized by Plumm, each transfer must be recorded in studio state. The prop must
        have a slug and must appear in actor inventories at each chapter boundary where it
        changes hands. The chapter-07 line 93 sequencing must be auditable against actor
        positions at that beat.

    # ── REFERENCE RESOLUTION ─────────────────────────────────────────────────

    - id: fault-005
      type: flag
      fault_class: FAULT-CONTINUITY-REFERENCE
      chapter: 03
      what: >
        Chapter-03 file header reads: narrator: taylor-hebert-westeros. The chapter-03 plan
        (design/shoot-v2/season-chapters-run/chapter-03-plan.md) marks interlude: false.
        However, the season plan (showrunner/season-s01-plan.md) describes episode s01e03 as
        combining the inspection visit AND Rowan's intercession in the same episode chunk.
        The proto-line split separates these into chapter-03 (Taylor POV, inspection) and
        chapter-05 (Rowan POV, intercession). This split is narratively sound and confirmed by
        the chapter-05 plan (interlude: true). No reference fault exists in chapter-03 itself.
        However: chapter-03's proto-line file contains no chapter metadata header (no
        "chapter: 03" line, no "title:" field) unlike chapters 06–10 which carry full headers.
        This is a file-format inconsistency that creates ambiguity in pass-5 stitcher runs:
        the stitcher cannot confirm chapter ordering from file-internal metadata for chapters
        01–05. Flagged, not faulted, because the file name provides ordering and the narrative
        sequence is internally coherent.
      why: >
        Missing chapter-header metadata in chapters 01–05 means pass-5 stitcher and
        continuity tooling must rely solely on filename ordering. If files are ever reordered
        or renamed, the stitcher loses its ordering anchor. Not a blocking continuity fault at
        this pass, but increases fragility.
      criteria: null

    - id: fault-006
      type: fault
      fault_class: FAULT-CONTINUITY-REFERENCE
      chapter: 10
      what: >
        Chapter-10 line 9: "septon-rowan speaks to oc-castellan-harrenhal." Chapter-10 line 36:
        "septon-rowan speaks to taylor-hebert-westeros." Chapter-10 line 45: "septon-rowan speaks
        to taylor-hebert-westeros." Chapter-10 line 47: "septon-rowan exits the hall."
        Septon-rowan's state.md records his last known location as loc-harrenhal-village-common.
        This is the settlement common adjacent to the sept, not Harrenhal. No prior chapter
        in the proto-line sequence establishes Rowan's transit from the village common to
        Harrenhal's hall. Rowan appears in the chapter-10 hall scene without a recorded
        transit, the same reachability gap as Taylor (fault-002) — but Rowan's baseline
        location in state.md (loc-harrenhal-village-common) is closer to Harrenhal than
        Taylor's (loc-harrenhal-sept-environs), making the reachability window more plausible,
        though still unrecorded. The reference to "septon-rowan" in chapter-10 must resolve to
        the Rowan who was in the village common, and the chapter must show or imply how he
        came to be in the hall.
      why: >
        Rowan's presence in the hall is dramatically load-bearing: he speaks to the castellan
        on Taylor's behalf (line 9) and he is present for the formal naming (lines 36, 45).
        If his transit is unrecorded, any future continuity audit or editor pass cannot
        establish the scene's spatial setup. Combined with Taylor's unrecorded transit
        (fault-002), chapter-10 opens with two unplaced actors in a location neither has
        been recorded reaching.
      criteria: >
        Rowan's transit from loc-harrenhal-village-common to Harrenhal's hall must be
        established in the proto-line sequence (either in a chapter-09 tail, a chapter-10
        pre-scene beat, or an explicit time-skip note). Rowan's state file must record the
        location change before chapter-10's hall scene opens.

    # ── POV CONSISTENCY ──────────────────────────────────────────────────────

    - id: fault-007
      type: flag
      fault_class: FAULT-CONTINUITY-POV
      chapter: 08
      what: >
        Chapter-08: narrator is taylor-hebert-westeros. Lines 1–26 depict the westerosi-traveling-maester
        setting up and conducting an assessment inside the cottage (with taylor-hebert-westeros
        present as the subject of the assessment — she is in the room: line 8 "taylor-hebert-westeros
        takes the seat"). Lines 61–63 then show taylor-hebert-westeros crossing the sept nave and
        reaching the chancel steps — a spatial displacement that implies the assessment has ended
        and Taylor has moved to the nave. This is internally consistent. However, lines 89–96 then
        show Taylor "taking the septon's seat" and opening/closing the septon's ledger — placing
        her back in the cottage. The chapter contains two location shifts (cottage → nave → cottage)
        without explicit transit proto-lines for the return from nave to cottage. Line 89 ("taylor-hebert-westeros
        exits the sept") follows line 63 ("taylor-hebert-westeros stops") with a large numbered gap
        (lines 64–88 are blank time-skip), so the return transit is presumably absorbed into the
        time-skip. This is a flag rather than a fault because time-skips can legitimately absorb
        routine transits; however, the direction of the second transit is ambiguous: line 89 says
        "exits the sept" (moving from sept to outside) and line 91 says "enters the cottage"
        — this sequence is spatially coherent only if the cottage is accessible from outside the
        sept. The sept and cottage are established as adjacent but distinct structures. The transit
        is plausible but the line-89 "exits the sept" → line-90 "crosses the yard" → line-91
        "enters the cottage" sequence depends on the cottage being in the yard, which is consistent
        with loc-harrenhal-sept-environs as established.
        Flag retained because the blank gap (lines 27–60, 64–88) makes the chapter's interior
        structure difficult to audit for completeness — two large blank ranges may contain
        structural beats that were not extracted.
      why: >
        If the large blank ranges in chapter-08 represent unextracted or unwritten content
        (rather than deliberate time-skips), the chapter's POV spine has holes that cannot
        be audited for continuity. This is not a blocking fault at the proto-line level but
        should be verified before pass-5 stitching.
      criteria: null

    # ── TIME CONSISTENCY ─────────────────────────────────────────────────────

    - id: fault-008
      type: flag
      fault_class: FAULT-CONTINUITY-TIME
      chapter: "03 → 04 transition"
      what: >
        Chapter-03 goal and plan describe Taylor managing fauna cost accumulation at the sept
        while Plumm's man delivers his report to Harrenhal — she senses the disturbance but
        does not know its cause. Chapter-03 plan states: start is "Taylor holding at the sept,
        managing cost accumulation"; end is "she enters the sept, speaks to the septon, and
        returns to the loft without resolution." Studio LTM records the chapter-03 episode
        transition as "several weeks elapsed" before chapter-04 opens (s01e04 bullet 1 LTM
        entry: "several weeks elapsed"). Chapter-03 is 120–121 AC per the season plan. The
        chapter-03 proto-line itself has 47 lines and shows a single-session fauna spend (nosebleed
        at line 15, raven drop at line 46). The time-skip between chapter-03 and chapter-04
        is consistent. However, the chapter-02 to chapter-03 transition is not recorded in
        studio LTM with a named interval; studio LTM records chapter-03 as "several weeks
        elapsed" from chapter-02, and the season plan places both in 120–121 AC. This is
        internally consistent but the "several weeks" figure is studio's notation, not a
        chapter-plan-specified value. Flagged as a time consistency note: if the chapter plans
        specify elapsed time between chapters, studio's "several weeks" must match or be sourced
        from the plan rather than estimated.
      why: >
        The Plumm inspection (chapter-04) is triggered by Plumm's man's report from chapter-02.
        If the interval between chapter-02 (report delivered) and chapter-04 (inspection arrives)
        is "several weeks," the administrative response time must be plausible for 120 AC
        Riverlands bureaucracy traveling from Harrenhal-shadow settlements to the castellan
        and back. "Several weeks" is plausible; the flag is that it is unanchored to a specific
        chapter-plan value and could drift if chapter plans are revised.
      criteria: null

    # ── CAUSE AND EFFECT ─────────────────────────────────────────────────────

    - id: fault-009
      type: flag
      fault_class: FAULT-CONTINUITY-CAUSE
      chapter: "05 → 07 transition"
      what: >
        Chapter-05 (Rowan's intercession, interlude) closes with two names in the inspector's
        report: Taylor's and Rowan's. Chapter-05 line 66: "ser-harwick-plumm pockets the
        record book." This is the ledger containing both names. Chapter-06 opens with the
        septon's death and Taylor's active attempt to redirect the succession mechanism (Rowan
        drafts the sealed parchment). Chapter-07 shows the refusal at the recorder's desk and
        Plumm's counter-move. The cause-effect chain (Plumm's report → refusal of Rowan's
        claim → Plumm files his own claim) is coherent. However, no proto-line in chapters
        05, 06, or 07 shows the inspector's report (containing both Taylor's and Rowan's names)
        being formally entered into the castellan's administrative record at Harrenhal. Chapter-02
        line 89 shows Plumm's man marking an entry in the garrison hall, establishing the
        upstream record. But the chapter-05 record book (pocketed by Plumm) is the intercession
        record, not the original report. The chapter-07 recorder's cross-reference entry (line 25)
        presumably references the upstream file, but the linkage between chapter-05's intercession
        ledger and the recorder's office file is implicit, not explicit. This is a flag because
        the linkage is narratively inferable; it would become a fault if the downstream script
        required Taylor or another actor to explicitly reference a specific entry that has no
        proto-line establishing its existence in the recorder's file.
      why: >
        The administrative documentation chain is the season's structural spine. Each link in
        the chain (original census → Plumm's anomaly report → inspection → intercession →
        recorder refusal → Plumm's claim → maester's report → Celtigar's inquiry → resolution)
        must be traceable to a proto-line. The intercession ledger → recorder's file step is
        currently implied rather than documented. An editor or stitcher writing the full manuscript
        will need this causal link to be explicit or explicitly elided.
      criteria: null

    - id: fault-010
      type: fault
      fault_class: FAULT-CONTINUITY-CAUSE
      chapter: "08 → 09 → 10"
      what: >
        Chapter-08 closes with "a raven strikes the bell tower beam" (line 96) — a physical
        environmental beat with no stated cause. The chapter goal specifies that "Bracken's
        filing locks a timeline" and "Celtigar's letter read aloud is the irreversible action
        that ends the chapter." However, chapter-08's proto-lines do not include a beat
        showing Bracken filing a document, showing Celtigar's letter being read aloud in company,
        or showing the castellan responding to either. Lines 37–96 (after the maester departs
        at line 26) contain only taylor-hebert-westeros crossing the nave and entering the
        cottage — no Bracken, no Celtigar, no filing beat. The stated irreversible board-
        worsening action (Celtigar's letter read aloud before the castellan in company) is a
        season-plan requirement (s01e05 planning note) that was specified as the chapter-08
        close. Chapter-09 opens with Taylor dispatching a raven and sparrow (lines 1–2) and
        then immediately shows Plumm and Bracken at the castellan — implying the Celtigar
        inquiry has already been received and is driving the chapter-09 contest. But if
        chapter-08 did not deliver the "Celtigar's letter read aloud" beat, the cause that
        drives chapter-09 (the crown visibility pressure that forces resolution) is unestablished
        in the proto-line sequence. The large blank gap in chapter-08 (lines 27–88) may
        contain unextracted beats — if Bracken's filing and Celtigar's letter scene occurred
        in that gap and were simply not extracted as proto-lines, this is a pipeline gap, not
        a narrative fault. But as audited from the proto-line files alone, the causal trigger
        for chapter-09 is absent from chapter-08.
      why: >
        Chapter-09's entire premise (Taylor observing her own capture being contested) depends
        on the administrative escalation that Celtigar's letter and Bracken's filing created.
        If that escalation is not in the proto-line sequence, the chapter-09 contest scene
        has no documented cause. This propagates to chapter-10 where the resolution is driven
        by Celtigar's inquiry forcing the castellan's hand — that pressure is in chapter-10's
        proto-lines (lines 6–12) but its origin (Celtigar's letter) is not confirmed established
        in any prior chapter's proto-lines. The chapter-09 chapter goal and studio state both
        reference the "ten-day Celtigar clock" as an established running condition, but the
        proto-line that set the clock is in the blank gap of chapter-08.
      criteria: >
        Either (a) the blank gap in chapter-08 (lines 27–88) must be confirmed as containing
        the Bracken filing and Celtigar's letter read-aloud scene (and those beats must be
        extracted into the proto-line sequence), or (b) a note must be added to chapter-08
        explicitly recording that these beats occur in the time-skip. The Celtigar ten-day
        clock must be traceable to a specific proto-line at which it started. Until the blank
        gap is resolved, chapter-08's causal output cannot be confirmed, and chapter-09's
        premise is unanchored.

  # ── CROSS-CHAPTER SUMMARY ──────────────────────────────────────────────────

  cross_chapter_findings:

    - id: fault-011
      type: fault
      fault_class: FAULT-CONTINUITY-STATE
      scope: season
      what: >
        Three actor state files carry stale or incomplete location/inventory data relative
        to the proto-line sequence:
        (1) ser-harwick-plumm/state.md: location is westerosi-smallfolk-village-common,
            inventory is empty. Chapter-04 line 81 establishes he pocketed a rolled page;
            chapter-05 lines 42–66 show him drawing a record book, writing in it, and
            pocketing it; chapter-09 shows him entering the outer ward with a document.
            His inventory has never been updated across the chapter sequence.
        (2) ser-aemon-bracken/state.md: location is oc-riverlands-river-ford. Chapter-09
            lines 16–60 show him entering Harrenhal's outer ward, entering the gatehouse,
            drawing a page, and exiting. His state file still shows oc-riverlands-river-ford —
            not updated to reflect his arrival at and departure from Harrenhal.
        (3) westerosi-traveling-maester/state.md: location is westerosi-smallfolk-village-common.
            Chapter-08 lines 1–26 show the maester conducting the assessment inside the cottage
            at the sept and then departing. His state file records him at the village common
            (consistent with chapter-05 positioning: post-interview departure heading east),
            but the chapter-08 assessment occurs at the sept cottage, not the common. If
            chapter-08 precedes the chapter-05 events in the timeline this is fine; if
            chapter-05 is a later interlude occurring before chapter-08 in the story timeline,
            the maester's movement back to the sept cottage needs to be recorded.
      why: >
        State files are the pipeline's source of truth for actor positions. Stale state means
        every downstream check (reachability, POV, prop handling) that relies on actor state
        is working from wrong baseline data. The Plumm inventory gap (1) is the most acute
        because it directly affects the prop chain-of-custody for the load-bearing administrative
        document (see fault-003 and fault-004).
      criteria: >
        All three actor state files must be updated to reflect their last-confirmed location
        and inventory at the end of the proto-line sequence (post-chapter-10). Updates must
        be derived from proto-line beats, not inferred. Each inventory item carried through
        the chapter sequence must be explicitly entered at the chapter where it first appears
        and tracked through transfers.

  # ── INTERLUDE HEADER CHECK ────────────────────────────────────────────────

    - id: fault-012
      type: flag
      fault_class: FAULT-CONTINUITY-POV
      scope: season
      what: >
        Chapter-05 carries "# interlude: true" as a comment rather than as a YAML field.
        The chapter-05-plan.md marks interlude: true as a YAML field. The proto-line file
        (chapter-05.md) has the interlude marker in a comment line: "# interlude: true —
        septon-rowan is not the series protagonist; this chapter is narrator-POV of a secondary
        actor." This is consistent with intent but the comment-form rather than YAML field
        form means automated header parsers would not detect the interlude flag. Chapters
        01–04 and 06–10 do not carry an interlude field at all (they are Taylor POV, so
        interlude: false is the default). No non-Taylor chapters other than chapter-05 are
        present in the 14-file sequence, so this is the only interlude case. Flagged for
        consistency, not blocked.
      why: >
        If pass-5 stitcher tooling uses a header parser expecting interlude: true as a YAML
        field (not a comment), chapter-05 will be treated as Taylor-POV and the narrator
        assignment may be incorrect in the assembled manuscript.
      criteria: null

  # ── PASSING DIMENSIONS ───────────────────────────────────────────────────

  passing_findings:

    - id: pass-001
      type: pass
      what: >
        Reachability: chapter-01 through chapter-07 (excluding fault-001 and fault-002).
        All chapter-to-chapter actor location transitions are plausible within the established
        geography (sept environs / village common / Harrenhal half a league). Chapter-04
        shows Taylor and Rowan walking to the recorder's hall and back in a single afternoon
        session, which is consistent with Harrenhal being within walking distance of the
        sept. No impossible transits identified in chapters 01–07 beyond those already
        faulted.

    - id: pass-002
      type: pass
      what: >
        Knowledge state propagation: Taylor's knowledge of the administrative machinery
        is correctly bounded across the chapter sequence. She does not know the contents
        of Plumm's report in chapter-02 (correct — she only observes his movement), she
        does not know the intercession ledger content in chapter-05 (correct — she is not
        present for the writing), and she does not know the maester's Citadel notation
        (correct — the notation goes in the maester's private notebook). No chapter shows
        Taylor claiming knowledge she could not have obtained through her fauna network
        or direct observation.

    - id: pass-003
      type: pass
      what: >
        Septon-dying-protector state persistence: established dead at chapter-04 (condition:
        [dead] in state.md), confirmed by chapter-06 opening (lines 1–5: breathing stops,
        Taylor closes eyes). The death event is handled consistently across all subsequent
        chapters — no chapter shows the septon acting after chapter-04.

    - id: pass-004
      type: pass
      what: >
        POV consistency chapters 01–04, 06–07, 10: all narrated by taylor-hebert-westeros;
        all events depicted are within Taylor's direct-observation range (she is present in
        the same physical space as the events, or observing via fauna channel at close
        range). No Taylor-POV chapter shows events she could not have perceived.

    - id: pass-005
      type: pass
      what: >
        Cause-and-effect: the core escalation spine (census → anomaly report → inspection
        → intercession → succession → claim contest → maester assessment → Celtigar inquiry
        → resolution) is present in the proto-line sequence and each link in chapters 01–07
        generates the condition required by the next chapter. The cause-effect chain is intact
        through chapter-07 at the proto-line level, with the chapter-08 gap noted in fault-010.

  # ── ESCALATION NOTE ──────────────────────────────────────────────────────

  escalate_note: >
    Faults fault-001 (chapter-09 fauna fidelity at half-league range) and fault-002 /
    fault-006 (Taylor and Rowan unplaced in chapter-10's hall scene) are the two
    highest-priority findings. Fault-001 is episode-scope (chapter-09 revision). Faults
    fault-002 and fault-006 may require inserting a transit beat between chapter-09 close
    and chapter-10 open — this is episode-scope, not season-scope. Fault-010 (chapter-08
    blank gap / Celtigar clock origin) requires verification of whether the blank gap
    contains intentionally unextracted beats or genuine missing content; if missing content,
    this is a pipeline gap requiring a new extraction pass on the source material.
    No findings require changes to the season plan or series plan. All faults are
    episode-scope or chapter-scope.
```
