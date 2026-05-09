```yaml
audit:
  scope: season
  target: s01 — all 14 proto-line files (chapter-01 through chapter-10) + actor state files
  timestamp: 2026-05-07
  pass: S4-iter2 — season-scope continuity re-verify after structural revisions
  prior_report: active-project/staff/auditor/season-s01-pass-S4-continuity.md
  dimensions_checked:
    - reachability
    - state_persistence
    - reference_resolution
    - pov_consistency
    - time_consistency
    - cause_and_effect
    - fauna_range (new: explicit verdict on ch08 fly range per dispatch brief)

  file_level:
    chapter-01.md: PASS
    chapter-02.md: PASS
    chapter-03.md: FLAG (fault-005 carried — metadata header; no new findings)
    chapter-04.md: PASS
    chapter-05.md: FLAG (fault-012 carried — interlude comment form vs. YAML field; no new findings)
    chapter-06.md: PASS (fault-004 partially addressed — ch06 line 114 added; residual gap in ch07 sequencing)
    chapter-07.md: RESIDUAL (fault-004 sequencing ambiguity remains; see below)
    chapter-08.md: PASS (fault-010 gap-fill confirmed; new fauna-range FAULT raised — see new-001)
    chapter-09.md: RESIDUAL (fault-001 fidelity question not resolved by IDs 100-102; see below)
    chapter-10.md: PASS (fault-002 and fault-006 transit gaps closed by IDs 51-56 and 53)

  prior_fault_dispositions:

    # ── FAULT-002 (ch10 Taylor transit) ──────────────────────────────────────

    - id: fault-002
      prior_type: fault
      disposition: CLOSED
      what: >
        SW added IDs 51, 52, 54, 55, 56 to chapter-10: taylor-hebert-westeros exits the sept
        (51), enters the approach road (54), enters the postern gate (55), enters the hall (56).
        ID 52 also adds taylor-hebert-westeros to the approach road sequence.
        Taylor's state.md transit note updated. The transit from loc-harrenhal-sept-environs
        to the hall is now proto-line-documented.
      residual: >
        Taylor's state.md still carries a TRANSIT NOTE reading "transit from
        loc-harrenhal-sept-environs to Harrenhal hall is not recorded in proto-line sequence."
        This note is now factually incorrect — the transit IS recorded via IDs 51-56.
        The note should be updated to reflect closure. This is a state-file housekeeping gap,
        not a continuity fault.
      residual_type: flag

    # ── FAULT-006 (ch10 Rowan transit) ───────────────────────────────────────

    - id: fault-006
      prior_type: fault
      disposition: CLOSED
      what: >
        SW added ID 53 to chapter-10: septon-rowan enters the approach road. Combined with
        ID 52 (taylor-hebert-westeros enters the approach road), ID 55 (postern gate), and
        ID 56 (enters the hall), Rowan's presence at Harrenhal is established through a
        shared approach-road transit.
        Rowan's state.md transit note updated. State file records fault-006 as the gap;
        IDs 51-56 collectively close it.
      residual: >
        The chapter-10 sequence now shows Rowan entering the approach road at ID 53 and then
        appearing inside the hall at ID 9 (septon-rowan speaks to oc-castellan-harrenhal).
        The postern-gate transit (ID 55) references taylor-hebert-westeros entering; Rowan
        is not explicitly stated to pass through the postern. His approach-road placement at
        ID 53 and his hall presence at ID 9 leave a small step unrecorded (postern passage).
        However, the approach road → postern → hall chain is established for Taylor at IDs 54-56,
        and Rowan is on the same road at ID 53. The gap is trivially inferable; the reachability
        fault is resolved. Rowan's state.md TRANSIT NOTE is stale and should be corrected.
      residual_type: flag

    # ── FAULT-001 (ch09 raven fidelity at range) ─────────────────────────────

    - id: fault-001
      prior_type: fault
      disposition: OPEN
      what: >
        SW added IDs 100-102 to chapter-09: taylor-hebert-westeros crosses the approach road
        (100-101), taylor-hebert-westeros reaches the roadside rise (102). ID 104 adds a
        physiological cost beat (pinches the nose). These IDs establish Taylor's location
        outside the walls at a roadside rise — approximately 400-500m from the gatehouse
        sill per the dispatch brief.
      why_still_open: >
        The S4 criteria required either (a) establishing that the raven-on-sill position
        delivers speech-level fidelity at that range under cond-fauna-control-rules, OR
        (b) recalibrating the chapter so Taylor observes gross physical behavior only without
        speech-level or document-content access.
        IDs 100-102 close only the location gap — Taylor is now placed outside the walls.
        They do not address the fidelity ceiling. The chapter's interior content (IDs/lines
        9-14, 38-49, 78-93) still depicts argument content and document handling that Taylor
        can only perceive if the raven-on-sill channel delivers speech and document-visual
        fidelity. The cost beat (ID 104: pinches the nose) signals fauna cost is being paid,
        but cost payment is not equivalent to fidelity establishment — cond-fauna-control-rules
        governs both cost AND capability ceiling.
        The 600m ceiling in cond-fauna-control-rules is described in the dispatch brief as a
        "hard ceiling." Taylor at the roadside rise (~400-500m from the gatehouse sill) is
        within or at the edge of that ceiling — closer than the half-league (~800m) the S4
        report cited as the concern. This reduces but does not eliminate the fault: the
        question is whether speech-level fidelity is achievable at 400-500m under
        cond-fauna-control-rules, and this has not been established in the proto-line sequence.
        No prior chapter has demonstrated speech-level fauna fidelity at this range with a cost
        signature. Chapter-02 fly use was at farmstead distance (~200m or less). The closest
        prior precedent is the s01e06 scene raven at half-a-league (an active motor-channel
        deployment, not a fidelity channel). Until cond-fauna-control-rules is cited or the
        chapter is revised to gross-behavior-only observation, the speech-level premise remains
        unsupported.
      criteria_unchanged: >
        Either (a) the chapter must explicitly invoke cond-fauna-control-rules to establish
        that raven-on-sill at ~400-500m range delivers speech-level and document-visual fidelity
        (and at what cost), or (b) chapter-09's content must be revised so Taylor observes
        only gross physical behavior at that range — arrivals, departures, physical transfers —
        without access to argument content or document specifics. The chapter goal may need
        recalibration if option (b) is chosen.

    # ── FAULT-003 (Plumm inventory) ──────────────────────────────────────────

    - id: fault-003
      prior_type: fault
      disposition: CLOSED
      what: >
        Plumm's state.md now carries prop-intercession-record-book (from ch05 line 66)
        and prop-ward-record-scroll (from ch10). The notes section documents the full
        prop chain-of-custody for all three load-bearing documents (rolled inspection page,
        intercession record book, ward-record scroll) with chapter-by-chapter tracking.
        ID 103 in chapter-09 adds "ser-harwick-plumm produces the roll" as an explicit beat.
      residual: >
        Plumm's state.md inventory lists prop-intercession-record-book as the primary item
        but the notes acknowledge the ch04 rolled-inspection-page is a distinct prop that
        transferred to the castellan's table at ch09 close. The rolled-inspection-page
        does not appear in Plumm's inventory as a separate slug — it is documented in notes
        only. This is acceptable for current continuity tracking but fixer should ensure
        the prop receives a formal slug (prop-rolled-inspection-page) at or before
        editor pass. Not a blocking fault.
      residual_type: flag

    # ── FAULT-004 (ch07 sealed parchment custody) ─────────────────────────────

    - id: fault-004
      prior_type: fault
      disposition: RESIDUAL
      what: >
        SW added ch06 ID 114 (septon-rowan tucks the parchment) — the sealed parchment from
        ch06 lines 31-45 now enters Rowan's possession at a proto-line beat. SW added ch07
        IDs 95-96 (septon-rowan produces the sealed parchment, sets the parchment on the
        counter) — the parchment is now explicitly produced at the recorder's desk.
        These additions partially address the S4 criteria.
      why_still_residual: >
        The ch07 line 93 sequencing ambiguity remains. Line 93 reads: "ser-harwick-plumm
        takes the claim document." At this point in the chapter, ser-harwick-plumm exited
        the recorder's room at line 27. Lines 86-94 show taylor-hebert-westeros crossing
        the yard, entering the sept, kneeling, rising, exiting the sept, passing the sept
        door, gripping the sept doorframe — at which point line 93 appears.
        The problem: Plumm exited the recorder's room (inside Harrenhal) at line 27.
        Taylor is exiting the sept (outside Harrenhal, having transited through the postern
        gate at lines 29-35 and crossed the approach road at lines 37-47) at lines 86-94.
        The "claim document" that Plumm takes at line 93 cannot be in Taylor's immediate
        spatial vicinity (she is outside, at the sept); Plumm cannot take a document in the
        same spatial frame as Taylor if they are in different locations at this beat.
        This remains a POV + spatial collision: either (a) line 93 is not a Taylor-POV-
        observed beat (she cannot see Plumm take the document from outside the sept) and
        should be marked as an inferred/reported beat, or (b) the document is taken in
        the yard outside the postern gate and Plumm's position at line 27 (inside recorder's
        room) versus line 93 needs a transit beat.
        Rowan's state.md notes the fault-004 sequencing ambiguity but records it as
        "unresolved." The prop-sealed-parchment-ch06 disposition after ch07 line 93 is
        "likely seized by Plumm" but not formally closed. The prop has no slug in the
        proto-line files.
      criteria_for_close: >
        (a) The prop-sealed-parchment-ch06 must receive a formal slug.
        (b) The transfer at ch07 line 93 must be auditable against actor positions — either
        Plumm returns to the postern area and takes the document there (with a transit beat
        between line 27 and line 93), or line 93 is reframed as a non-POV inference beat
        that Taylor did not directly witness.
        (c) Rowan's state.md note about fault-004 should be updated to reflect the partial
        resolution (IDs 95-96 and 114 added) while retaining the line-93 sequencing gap.

    # ── FAULT-010 (ch08 blank gap / Celtigar clock origin) ────────────────────

    - id: fault-010
      prior_type: fault
      disposition: CLOSED
      what: >
        SW added 34 new beats to chapter-08: IDs 29-46 cover Bracken's filing via raven
        relay (Taylor in the yard/sept door, raven at the recorder's counter, Bracken's
        hand dropping the document), and IDs 65-88 cover the Celtigar letter scene (fly
        on the hall ceiling, castellan reading the letter aloud, the hall emptying).
        The Celtigar ten-day clock is now traceable to a specific chapter-08 proto-line
        segment. The cause that drives chapter-09 is established.
      residual: >
        See new-001 below — the ch08 fauna deployments raise a new fault on range.
        The gap-fill itself satisfies fault-010's criteria. Fault-010 is CLOSED as a
        structural gap; the range fault is a separate and new finding.
      residual_type: none (gap closed; new finding raised separately)

    # ── FAULT-011 (state files stale) ────────────────────────────────────────

    - id: fault-011
      prior_type: fault
      disposition: CLOSED
      what: >
        All five actor state files updated per showrunner session-log 2026-05-07:
        - ser-harwick-plumm/state.md: location updated; inventory populated; prop chain
          documented in notes.
        - ser-aemon-bracken/state.md: location updated; movement log added.
        - westerosi-traveling-maester/state.md: location updated; prop-assessment-roll added;
          transit gap from ch05 to ch08 noted.
        - taylor-hebert-westeros/state.md: location updated; inventory cleared; transit gap noted.
        - septon-rowan/state.md: location updated; prop-sealed-parchment-ch06 gap documented.
        Showrunner memory.md end_of_season_state block added with all actor positions and
        prop custody summary.
      residual: >
        Two state files still carry transit notes that are now factually incorrect (fault-002
        and fault-006 have been closed by IDs 51-56). Taylor and Rowan state files should
        have their TRANSIT NOTE language updated from "not recorded in proto-line sequence"
        to "recorded via IDs 51-56 in chapter-10." Housekeeping, not a continuity fault.
      residual_type: flag

    # ── FAULT-005, FAULT-007, FAULT-008, FAULT-009, FAULT-012 ────────────────

    - id: fault-005
      prior_type: flag
      disposition: CARRIED (unchanged — ch01-05 missing chapter-header metadata)

    - id: fault-007
      prior_type: flag
      disposition: CARRIED (unchanged — ch08 POV spine structure flag; blank gap now filled
        by IDs 29-88, which reduces the flag's structural concern but does not retire it
        entirely — the nav transition from chancel steps at line 63 → inside the hall via
        fly channel at line 65 still depends on the fly being pre-positioned in the hall
        before Taylor reaches the chancel steps; see new-001 for the range component of this)

    - id: fault-008
      prior_type: flag
      disposition: CARRIED (unchanged — ch03→04 time interval unanchored to chapter-plan value)

    - id: fault-009
      prior_type: flag
      disposition: CARRIED (unchanged — intercession ledger → recorder's file causal link still implicit)

    - id: fault-012
      prior_type: flag
      disposition: CARRIED (unchanged — ch05 interlude marker in comment form vs. YAML field)

  # ── NEW FINDINGS ──────────────────────────────────────────────────────────

  new_findings:

    # ── FAUNA RANGE — CH08 FLY DEPLOYMENT ─────────────────────────────────────

    - id: new-001
      type: fault
      fault_class: FAULT-CONTINUITY-CONSTRAINT
      chapter: 08
      what: >
        Chapter-08 IDs 65-88 (Celtigar letter scene): taylor-hebert-westeros deploys a fly
        inside Harrenhal's hall. The fly observations begin at line 65 ("a fly crosses the
        hall ceiling") and the observation feed continues through line 88 ("taylor-hebert-westeros
        presses the stone") — covering the castellan opening the letter, reading it aloud,
        the hall emptying, and Taylor's physiological cost response.
        At the moment this fly observation begins, Taylor is established at or near the chancel
        steps inside the sept (chapter-08 lines 61-63: "taylor-hebert-westeros crosses the
        sept nave / reaches the chancel steps / stops"). The sept is approximately half a
        league (~2.5km, as repeatedly established in studio LTM and actor state files) from
        Harrenhal's hall.
        The cond-fauna-control-rules constraint sets a 600m hard ceiling (per dispatch brief
        and consistent with all prior cost-tracking in studio state files). The fly in
        Harrenhal's hall at 2.5km from Taylor's position is at more than four times that ceiling.
        Two interpretations are possible:
        (a) The 600m ceiling is an operational-control ceiling (active motor-channel range),
        not a perception ceiling — pre-positioned fauna (a fly already inside the hall) can
        stream observation back to Taylor at greater range. Under this reading, Taylor did not
        dispatch the fly 2.5km; the fly was already in the hall and she connected to it at
        short range earlier, then held the channel while she transited the nave.
        (b) The 600m ceiling applies to the full fauna channel (control and perception) —
        Taylor cannot receive sensory data from a fly at 2.5km regardless of how the fly
        arrived in the hall.
        VERDICT: Interpretation (a) is the more favorable reading of the constraint text
        as described, and there is a plausible temporal argument: Taylor could have pre-
        positioned the fly in the hall during an earlier chapter when she was within range.
        However, no proto-line in any chapter establishes that Taylor pre-positioned a fly
        inside Harrenhal's hall. Chapter-09 establishes fly deployment inside the gatehouse
        (ID 78: taylor-hebert-westeros dispatches a fly; this occurs with Taylor at the
        roadside rise ~400-500m from the walls, within ceiling range). Chapter-08's fly
        appears at line 65 without a dispatch beat — it is simply "there" on the hall ceiling.
        If interpretation (a) is operative, the pre-positioning must be established somewhere
        in the proto-line sequence before ch08 line 65. It is not. If interpretation (b)
        is operative, the ch08 fly observation at 2.5km range is a hard constraint violation.
        Either way, the current state of the proto-line sequence does not support the ch08
        fly observation.
        The ch08 IDs also show Taylor paying physiological cost (nosebleed: lines 82-83,
        pressing nose bridge: line 82, presses temple: line 77, presses palms: line 79)
        during the fly observation — cost signature is consistent with active fauna use.
        This supports interpretation (a) (she is actively running the channel, not passively
        receiving ambient relay), which strengthens the range fault rather than mitigating it:
        she is actively controlling a fly at 2.5km.
      why: >
        The Celtigar letter scene is the irreversible cause that drives chapter-09 and
        chapter-10. Taylor's knowledge that the letter was read aloud — and her specific
        awareness of what was said — is load-bearing for the season's climactic sequence.
        If the fly observation violates cond-fauna-control-rules, Taylor cannot know the
        letter's content or that it was read publicly. The cause-effect chain for chapter-09
        (Taylor aware of the Celtigar pressure driving the contest) is compromised. This
        is not a peripheral detail — it is the mechanism by which Taylor learns the most
        important administrative fact of the season.
      criteria: >
        One of the following must be established:
        (a) A proto-line (in ch07 or earlier, when Taylor was within ~600m of Harrenhal)
        showing Taylor pre-positioning a fly inside the hall — with the pre-positioning
        explicitly noted as a persistent placement rather than a dispatched channel that
        would terminate on release. cond-fauna-control-rules must explicitly permit
        persistent pre-positioned channels that relay at range beyond the operational ceiling.
        (b) Chapter-08 must be revised so Taylor observes the Celtigar letter scene at
        gross-behavior level only (letter delivered, hall assembles, hall disperses — no
        speech content, no letter-interior knowledge), and chapters-09 and -10 must be
        checked to ensure Taylor's foreknowledge of the letter's content is recalibrated
        to what gross observation would yield.
        (c) The 600m ceiling in cond-fauna-control-rules is explicitly designated as a
        control-only ceiling, not a perception ceiling, and pre-positioned fauna perception
        at range is confirmed as permitted with appropriate cost. In that case, a pre-
        positioning proto-line is still required (even if not a range-busting dispatch),
        and the current gap (no pre-positioning beat) must be filled.

    # ── SHOWRUNNER-FLAGGED: THREE DISTINCT PLUMM DOCUMENT PROPS ──────────────

    - id: new-002
      type: flag
      fault_class: FAULT-CONTINUITY-STATE
      scope: season
      what: >
        Showrunner identified three distinct Plumm-associated props:
        (1) prop-rolled-inspection-page (ch04 line 80-81: rolled and pocketed by Plumm)
        (2) prop-intercession-record-book (ch05 line 66: pocketed by Plumm after writing
            Taylor's name and Rowan's sept entry)
        (3) wardship claim document / prop-sealed-parchment-ch06 (ch07: Rowan's sealed
            parchment, seized by Plumm at ch07 line 93)
        Plumm's state.md now distinguishes these three and tracks them in notes. The
        notes are detailed and accurate. However, none of the three props carries a formal
        slug in the proto-line files themselves — they are referenced by description
        only ("a document," "the page," "the roll," "the claim document"). Without slugs,
        the stitcher and editor cannot trace prop custody from proto-line beats directly;
        they must cross-reference Plumm's state notes.
        The custody chains as documented in state notes are internally consistent for (1)
        and (2). Prop (3) has the unresolved ch07 line 93 sequencing issue (see fault-004
        RESIDUAL above).
      why: >
        Three props with overlapping descriptions ("document," "page," "roll") that change
        hands multiple times across five chapters will create editorial confusion if they
        are not slugged at the proto-line level. The editor pass will require disambiguation
        of every "the document" and "the page" in chapters 07, 09, and 10.
      criteria: null (flag only; fixer should assign slugs at editor prep, not blocking)

    # ── SHOWRUNNER-FLAGGED: PROP-CENSUS-FILE CH10 UPSTREAM ESTABLISHMENT ──────

    - id: new-003
      type: fault
      fault_class: FAULT-CONTINUITY-STATE
      chapter: 10
      what: >
        Chapter-10 line 4: "ser-harwick-plumm sets the census file." Lines 7, 10: the
        castellan lifts and returns the census file. This prop (referred to in Plumm's
        state.md as prop-census-file) is treated as a known document that Plumm arrives
        with and presents as supporting documentation for the ward-of-administration
        proceeding.
        No prior chapter in the proto-line sequence establishes prop-census-file. The
        prop-rolled-inspection-page (ch04) and prop-intercession-record-book (ch05) are
        established; neither is labeled "census file" in any prior chapter. The chapter-10
        proceeding treats the census file as a pre-existing administrative record that
        substantiates the ward determination — implying it is either the original census
        ledger entry (from ch01: the census officer's notation), the Plumm inspection
        record (ch04), or the intercession record (ch05), or a compiled derivative of
        all three.
        No proto-line beat in chapters 01-09 shows Plumm or anyone else assembling,
        compiling, or carrying a document specifically called a "census file" or equivalent
        compiled administrative record. The prop appears in chapter-10 without upstream
        establishment.
      why: >
        The ward-of-administration determination depends on there being a legitimate
        documentary record that the castellan can review and accept. If prop-census-file
        is not traceable to prior proto-line beats, the legal instrument used to finalize
        the season's climactic administrative resolution is an unestablished prop. This
        does not make the scene impossible to write — an editor can define what the census
        file is — but it means the document's content and authority are undefined in the
        proto-line sequence.
      criteria: >
        Either (a) a proto-line beat in chapters 01-09 must be identified or added showing
        prop-census-file being assembled, held, or referenced by name (or by the equivalent
        description — e.g., "the compiled census and inspection record"); or (b) chapter-10
        line 4's "census file" must be explicitly identified in Plumm's state notes as
        a derivative of named prior props (e.g., "prop-census-file = prop-rolled-inspection-
        page + prop-intercession-record-book, compiled and presented by Plumm as administrative
        package"), with that identification noted in the proto-line file header or a margin
        note so the editor knows what the prop is.

    # ── SHOWRUNNER-FLAGGED: TAYLOR'S FOLIO CH07 FATE ─────────────────────────

    - id: new-004
      type: flag
      fault_class: FAULT-CONTINUITY-STATE
      scope: "ch07 → ch10"
      what: >
        Taylor's state.md carries an inventory note: "Folio-with-motherhouse-and-recorder-
        papers: was under Taylor's arm at ch07 (she followed Rowan out of recorder's room
        per state note); not confirmed in her hands at ch10."
        The folio is separately tracked in Rowan's state.md inventory as "folio-with-
        motherhouse-and-recorder-papers." Both Taylor and Rowan are associated with the
        same folio label. Chapter-04 (studio LTM) establishes Taylor carrying a folio
        concealed under her shirt; chapter-05 and chapter-07 show Rowan carrying a folio
        under his arm. These may be the same folio or two different documents.
        At chapter-07 close: Taylor is exiting Harrenhal via the postern gate and crossing
        the approach road; Rowan is crossing the yard and speaking to Taylor (lines 14-42).
        Neither chapter-07 nor any subsequent chapter has a proto-line showing Taylor's
        folio changing hands, being set down, or being disposed of. Chapter-10 does not
        show Taylor carrying anything.
        The folio is not load-bearing for the chapter-10 resolution — it is not referenced
        in the ward-of-administration proceeding. However, its unresolved fate creates a
        state-file inconsistency: if Taylor carried it out of Harrenhal at ch07, she either
        still has it at ch10 (in which case her inventory should list it) or it was
        transferred/disposed (in which case a transfer beat is missing).
      why: >
        Not blocking — the folio does not drive chapter-10. However, an untracked prop
        in a protagonist's inventory is a state-persistence gap. If the editor or a later
        season picks up the folio as a narrative object, the current state leaves its
        provenance unclear.
      criteria: null (flag only; resolve at editor pass or season-2 planning)

  # ── CROSS-CHAPTER SUMMARY ─────────────────────────────────────────────────

  cross_chapter_summary:

    prior_faults_closed: [fault-002, fault-003, fault-010, fault-011]
    prior_faults_open: [fault-001]
    prior_faults_residual: [fault-004]
    prior_flags_carried: [fault-005, fault-007, fault-008, fault-009, fault-012]
    new_faults: [new-001, new-003]
    new_flags: [new-002, new-004]
    state_file_housekeeping_flags:
      - taylor/state.md TRANSIT NOTE language stale (fault-002 closed but note not updated)
      - rowan/state.md TRANSIT NOTE language stale (fault-006 closed but note not updated)
      - prop-rolled-inspection-page needs formal slug in proto-line files

  # ── FILE-LEVEL VERDICT ────────────────────────────────────────────────────

  file_level_verdict: FAIL

  verdict_basis: >
    Two OPEN/RESIDUAL faults carry forward (fault-001, fault-004), two new faults are raised
    (new-001 on ch08 fauna range, new-003 on prop-census-file upstream establishment). The
    season cannot be declared clean while fault-001 (ch09 speech-level fidelity unestablished)
    and new-001 (ch08 fly at 2.5km range) remain unresolved — both touch Taylor's
    knowledge-state at the most load-bearing scenes of the season.

  # ── PRIORITY RANKING ─────────────────────────────────────────────────────

  priority:
    critical:
      - new-001: ch08 fly range at 2.5km — either constraint interpretation or pre-positioning
          must be resolved; drives Taylor's foreknowledge of the Celtigar letter, which
          drives chapters 09 and 10
      - fault-001: ch09 raven fidelity at ~400-500m — speech-level channel unestablished;
          Taylor's knowledge of the gatehouse argument is the chapter's entire premise
    standard:
      - new-003: prop-census-file has no upstream establishment — needs at least a state-note
          definition before editor pass
      - fault-004: ch07 line 93 sequencing ambiguity — prop-sealed-parchment-ch06 transfer
          audit trail incomplete
    housekeeping:
      - new-002: three Plumm props need formal slugs at editor prep
      - new-004: Taylor's folio fate unresolved through ch10
      - fault-002/fault-006 state.md TRANSIT NOTE language stale
      - prop-rolled-inspection-page needs slug
      - fault-005, fault-007, fault-008, fault-009, fault-012 carried as flags (no action required before editor pass)
```
