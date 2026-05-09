```yaml
audit:
  scope: season
  target: s01-chapter-01
  timestamp: 2026-05-07
  file_level: FAIL
  axes_checked:
    - reachability
    - state_persistence
    - reference_resolution
    - pov_consistency
    - time_consistency
    - cause_and_effect
    - boundary_check
  findings:

    - id: fault-001
      type: fault
      class: FAULT-CONTINUITY-REFERENCE
      what: >
        proto-lines/chapter-01.md uses the slug `oc-census-officer` throughout
        (lines 35, 44-48, 50-52, 55, 57-61, 63, 65-67, 70, 74, 76-77, 80, 82,
        95, 98-99, 101, 103-104, 106, 109, 111, 124). The slug is listed in
        cards/personas/INDEX.md as "authored 2026-05-07 for chapter-01 Pass 5
        continuity resolution" with variant-of: census-officer. No physical card
        file exists at cards/personas/oc-census-officer.card.md — the read
        attempt returned File does not exist.
      why: >
        The audit axiom is that every entity slug resolves to a card. An INDEX
        entry alone is not a card. The character's impersonator brief, constraint
        load, and voice discipline all derive from the card file at shoot time. If
        the file is absent, any downstream agent that tries to load the card by
        slug will find nothing. The existing census-officer card covers the same
        character and would satisfy all downstream needs, but the slug mismatch
        means the resolution chain is broken at the file level. The INDEX note
        "variant-of: census-officer" is a margit annotation, not a forwarding
        mechanism.
      criteria: >
        A card file at cards/personas/oc-census-officer.card.md must exist and
        must resolve fully as a persona card (class, scope, world, quality fields
        populated). Acceptable resolutions: create the file as a stub forwarding
        to census-officer with a note that all content is inherited, OR promote
        the existing census-officer card content into the oc-census-officer
        filename with appropriate header changes. The resolution must make
        cards/personas/oc-census-officer.card.md readable as a valid card.

    - id: pass-001
      type: pass
      what: Reachability — all actors throughout ch01
      why: >
        Chapter 01 is set entirely within loc-harrenhal-sept-environs (cottage,
        sept nave, yard). Taylor, septon-dying-protector, and oc-census-officer
        + escort all operate within this single compound. No transit across
        locations is required. The location card confirms all sub-locations
        (cottage, nave, yard) are reachable within the compound without
        time-gap. No reachability fault detected.

    - id: pass-002
      type: pass
      what: State persistence — props and conditions within ch01
      why: >
        "The materials" (writing materials) referenced at lines 41 and 124-126
        are fixed props established by the loc-harrenhal-sept-environs card
        ("septon's writing materials and seven books, in the cottage"). Their
        appearance is location-anchored, not carried, so no prop-custody
        tracking fault applies. No prop appears or disappears without a beat.
        Septon-dying-protector remains in the cottage throughout (consistent
        with state.md: location loc-harrenhal-sept-environs, condition: [dead]
        — he is still alive at ch01 time, dying, which the card confirms:
        "dying of fever"). No state-persistence fault detected.

    - id: pass-003
      type: pass
      what: POV consistency — narrator's physical observation throughout ch01
      why: >
        Taylor is in the yard when the ravens flush (line 31) and when the
        riders crest the road (line 34). The loc card confirms the road is
        visible from the sept's front door three minutes before arrival. All
        depicted events (raven calls, rider approach, yard and cottage
        interior scenes) are within Taylor's physical line of sight or
        within passive swarm-sense range. No POV event requires Taylor to
        perceive something beyond her physical or fauna-sense reach.

    - id: pass-004
      type: pass
      what: 600m fauna ceiling — cond-fauna-control-rules
      why: >
        No active long-range fauna deployment occurs in ch01. Ravens flushing
        (lines 6, 31) and resettling (line 122) are ambient/passive events
        consistent with the bell tower ravens in the location card. No proto-line
        depicts Taylor directing fauna beyond the compound perimeter. The 600m
        maximum range ceiling is not implicated.

    - id: pass-005
      type: pass
      what: Time consistency within ch01
      why: >
        The chapter covers a single morning-to-late-day arc: pre-dawn waking
        (line 1), morning sept visit (lines 10-15), ravens flush on rider
        approach (line 31), census encounter (lines 34-113), rider departure
        (lines 109-113), and a final cottage-to-sept return (lines 115-131).
        Blank gap lines (8-9, 11, 13-29, 33, 36, 43, 54, 62, 69, 80, 84-93,
        97, 108, 114, 120-121) represent normal ellision. The three-minute
        warning window from line 31 (ravens flush) to line 34 (riders crest)
        is consistent with the location card's stated visibility distance.
        No time-consistency fault detected.

    - id: pass-006
      type: pass
      what: Cause-and-effect chains within ch01
      why: >
        All major causal sequences are sound: ravens flush → riders visible →
        riders arrive; Taylor retreats → officer enters yard → officer enters
        cottage; septon rises → septon falls (per SHOOT NOTE constraint);
        officer produces quill → documentary exchange → officer exits; officer
        departs → Taylor re-enters cottage → final exchange → closing sept
        sequence. No broken causal chain detected.

    - id: pass-007
      type: pass
      what: >
        Boundary check — ch01 close (Taylor in sept nave, line 131) to ch02
        open (Taylor enters kitchen garden, line 4)
      why: >
        Taylor ends ch01 in the sept nave. Ch02 opens with oc-plumms-man
        departing Harrenhal (lines 1-3, a separate thread), then Taylor
        entering the kitchen garden (line 4). The kitchen garden is "against
        the south wall of the cottage" within the same sept-environs compound
        per the loc card. The transit from sept nave to cottage kitchen garden
        is a short walk within the compound — no recorded transit beat is
        required for intra-compound movement. The boundary handoff is clean.

    - id: pass-008
      type: pass
      what: Reference resolution — all other entity slugs in ch01
      why: >
        taylor-hebert-westeros: full card in library and active-project.
        septon-dying-protector: full card at cards/personas/septon-dying-protector.card.md.
        "the ravens": ambient fauna at loc-harrenhal-sept-environs, no card
        required — context-licensed by location card fixed props.
        "the men-at-arms" / "the man-at-arms" / "the riders": context-licensed
        unnamed escort group attendant to oc-census-officer; no card required.
        All unnamed entities fit the licensed-unnamed pattern (role-label
        identifiers with no independent action beyond their function in the
        scene). No additional reference fault beyond fault-001.
```
