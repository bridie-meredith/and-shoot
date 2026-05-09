audit:
  scope: season
  target: chapter-09 (Two Claims, One File)
  pass: 5 (continuity)
  run: fresh-fork independent re-verify
  timestamp: 2026-05-07
  file_level: FAIL
  auditor: fork (fresh context, no prior ch09 pass history loaded)
  findings:

    - id: fault-001
      type: fault
      what: >
        IDs 96–97 and ID 99. Line 96: `the ravens lift`. Line 97: `the ravens circle the central
        tower`. Line 99: `taylor-hebert-westeros repositions the raven`. Taylor withdrew both the
        raven and the sparrow at IDs 62–63 (`taylor-hebert-westeros withdraws the raven`;
        `taylor-hebert-westeros withdraws the sparrow`). The only subsequent deployment is a fly
        (ID 78), withdrawn at ID 92. No raven or sparrow re-dispatch proto-line exists between
        ID 63 and ID 96.
      why: >
        The `the ravens lift` / `the ravens circle` beats at IDs 96–97 assert active fauna that
        were explicitly withdrawn and never re-deployed. The definite article `the ravens` carries
        an anaphoric reference to no live antecedent. ID 99 (`repositions the raven`) compounds
        the fault by asserting ongoing control of a withdrawn instrument. Downstream facet authoring
        (state-updates, feeling-flags) will cite these beats and inherit a false state — Taylor in
        active raven control she does not have. Stitcher output will show Taylor commanding ravens
        that should not be hers at this point.
      criteria: >
        The file must either (a) insert a raven re-dispatch proto-line before ID 96 that establishes
        the specific bird(s) Taylor commands in the closing sequence, or (b) recast IDs 96–97 as
        uncontrolled ambient raven behavior (wild birds — not Taylor's instruments) using indefinite
        article form (`a raven lifts`, `ravens circle`) and delete ID 99 (which implies active
        control). If the intent is Taylor releasing fauna and observing natural bird behavior as
        her closing image, the recast path (b) is the minimum change.

    - id: fault-002
      type: fault
      what: >
        Pass 3 shape report verdict (RE-ORDER-AND-TRANSITIONS) not applied to the file. Pass 3
        prescribed: move IDs 62–64 (and blank 65) from their current position — immediately after
        ID 60 (Plumm/Bracken departure sequence) — to immediately after ID 90 (Celtigar's final
        dialogue beat), before existing blank 91. Pass 3 also prescribed one transition beat
        between IDs 60 and 66 (Celtigar arrival). The current file reflects the pre-Pass 3 order:
        IDs 62–64 precede IDs 66–90, and no transition beat exists between IDs 60 and 66.
      why: >
        In the current order, ID 64 (`taylor-hebert-westeros exhales`) reads as resolution before
        Celtigar arrives, producing a double-peak structure the Pass 3 auditor identified. The
        chapter plan requires Celtigar's arrival as the climax beat, not as an anticlimactic
        appendix after Taylor has already processed and closed. Without the re-order and transition,
        the spine's arc contradicts the chapter's `change` statement and the season's structural
        escalation logic. The missing transition beat also leaves a POV gap: how does Taylor
        re-acquire fauna visibility on Celtigar before he reaches the postern?
      criteria: >
        IDs 62–64 (and blank 65) must be relocated to after ID 90, before blank 95. A transition
        beat must be inserted between ID 60 and ID 66 that establishes Taylor maintaining fauna
        position on the approach road and acquiring Celtigar's cart in her field before it reaches
        the gate. Pass 2 must run on the new transition beat before Pass 5 re-evaluates the re-ordered
        sequence.

    - id: fault-003
      type: fault
      what: >
        Ch09 → ch10 boundary broken. Ch09 closes with Taylor at the roadside rise (established ID
        102; no movement proto-line removes her from this position). Last Taylor position in ch09:
        roadside rise on approach road to Harrenhal. Ch10 ID 52 reads: `taylor-hebert-westeros
        exits the sept`. This requires Taylor to be inside the sept at ch10 open — a location she
        was not at during all of ch09. No proto-line in ch09 records Taylor returning from the
        roadside rise to the sept; no interlude or time-skip chapter bridges the gap.
      why: >
        Taylor cannot exit the sept (ch10 ID 52) from a position she never re-entered after leaving
        it at ch08 close (ch08 line 91: exits postern gate; ch08 line 92: takes the road). The
        boundary places Taylor in an unrecorded location. Stitcher output will show Taylor
        teleporting from the roadside rise into the sept with no transit. This is the fault-002
        documented in showrunner/memory.md (open continuity fault — "ch09 roadside-rise to ch10
        hall entry" gap). The fault is confirmed present and unresolved in the current ch09 file.
        Ch10 cannot open correctly without this gap resolved.
      criteria: >
        Either (a) ch09 must add a closing transit sequence returning Taylor from the roadside rise
        to the sept (or to some location consistent with ch10 ID 52), or (b) ch10 must restructure
        its opening to place Taylor on the approach road / postern gate approach rather than exiting
        the sept. The minimum change should be identified by fixer in consultation with the ch10
        proto-line file and the chapter plans for both chapters. Showrunner memory open fault
        fault-002 must be marked resolved when criteria are met.

    - id: fault-004
      type: flag
      what: >
        ID 103: `ser-harwick-plumm produces the roll`. First and only mention of `the roll` in
        ch09; definite article used on first introduction. The prop's prior history is at ch04
        line 81 (`ser-harwick-plumm pockets the roll`). Chain-of-custody is unbroken (Plumm
        carried the roll from ch04 through ch09 per showrunner/memory.md prop_custody_summary).
        The continuity fault is not in the custody chain but in the referential expectation: a
        reader encountering ch09 as a standalone unit or after any chapter between ch04 and ch09
        will find `the roll` without local antecedent.
      why: >
        The stitcher must render this beat in prose. If the stitcher treats `the roll` as a known
        prop with prior context, prose can introduce it with a back-reference. If the stitcher
        treats proto-lines as scene-local, it will introduce a definite reference to an
        unestablished prop. This is not a proto-line schema fault (the schema does not govern
        cross-chapter prop introduction conventions), but it is an editorial continuity flag for
        the stitcher or editor pass. No fixer action required; editor pass should note the
        cross-chapter prop establishment requirement.
      criteria: null

    - id: fault-005
      type: flag
      what: >
        Open continuity fault fault-001 (showrunner memory) — range of raven/sparrow deployment
        from roadside rise. Showrunner memory records: "ch09 raven fidelity at half-league range
        — fauna channel ceiling for speech-level feed from gatehouse sill." The task brief
        specifies Taylor at ~400-500m from Harrenhal walls at IDs 100–102. No proto-line in ch09
        and no state file entry quantifies the roadside rise distance from the walls. The 600m
        ceiling (cond-fauna-control-rules) is satisfied IF the ~400-500m estimate is correct,
        but no documentary evidence in the file confirms this.
      why: >
        If the roadside rise is beyond 600m, IDs 1, 2, and 78 (fauna dispatches), and ID 36
        (raven repositions to gatehouse sill) all violate cond-fauna-control-rules. The chapter's
        entire fauna-observation mechanic depends on Taylor being within the ceiling. The ch08
        restructure (sept relocated to Harrenhal interior to resolve RESIDUAL-1) demonstrates that
        the pipeline does enforce this ceiling with structural consequences. The ch09 range has not
        been similarly validated. This is a pre-existing open fault carried forward without
        resolution; the current ch09 file does not resolve it.
      why: >
        Flagged for showrunner resolution. If the chapter plan supports 400-500m as the intended
        roadside rise distance, a state file note confirming this resolves the open fault without
        changing proto-lines. If the distance is indeterminate or greater than 600m, fauna
        deployment beats require restructure.
      criteria: null

---

## Dimension summary

**Reachability:** PASS — IDs 100–102 (roadside rise transit) are reachable from ch08 close
(Taylor on the approach road after exiting postern gate). Time-skip ID 100 bridges the gap.

**State persistence:** FAIL — IDs 96–97 and 99 assert active raven control that does not exist:
raven/sparrow withdrawn at IDs 62–63, only fly re-deployed (78) and withdrawn (92), no raven
re-dispatch before ID 96. See fault-001.

**Reference resolution:** PASS on dialogue form (all 21 `speaks to` beats are schema-licensed,
no content transcribed). FLAG on `the roll` (ID 103) — cross-chapter prop introduction without
local antecedent (fault-004, flag only).

**POV consistency:** PASS on direct POV violations — all observed action is accessible to Taylor
through dispatched fauna from the roadside rise. Open range question for the 600m ceiling (fault-005,
flag) is pre-existing and not introduced by this file.

**Time consistency:** PASS — time-skip markers are correctly placed; sequence of three separate
arrivals (Plumm, Bracken, Celtigar) is internally consistent with the chapter plan's timeline.

**Cause-effect:** PASS — action chains (man-at-arms doorway sequence; document/page exchange;
castellan stacking and retaining documents; Celtigar examining both documents) are internally
consistent.

**Ch08 → ch09 boundary:** PASS — ch08 close places Taylor on the road; ID 100 (blank time-skip)
bridges to ID 101–102 (crosses approach road, reaches roadside rise). Ch08 raven/fly withdrawals
at lines 94–95 are consistent with fresh dispatches at ch09 IDs 1–2.

**Ch09 → ch10 boundary:** FAIL — ch09 closes with Taylor at roadside rise; ch10 ID 52 opens
with Taylor exiting the sept. Taylor was never recorded re-entering the sept after ch08 line 91
(exits postern gate). Transit gap confirmed open and unresolved. See fault-003.

**Pass 3 re-order:** FAIL — re-order not applied; IDs 62–64 remain in pre-Pass 3 position
(before Celtigar sequence). No transition beat between IDs 60 and 66. See fault-002.

---

## File-level verdict

FAIL — three faults (fault-001 state persistence, fault-002 Pass 3 re-order not applied,
fault-003 ch09/ch10 boundary broken) block continuity-clean status. Two flags (fault-004,
fault-005) are advisory. Fixer dispatch required for fault-001, fault-002, fault-003.
After fixer commits, Pass 5 re-runs on changed lines only.
