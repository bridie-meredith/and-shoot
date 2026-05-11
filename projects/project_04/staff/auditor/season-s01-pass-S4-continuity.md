```yaml
audit:
  scope: season
  target: s01
  pass: S4-continuity
  timestamp: 2026-05-09
  verdict: SEASON-CONTINUITY-OK
  prior-audit: season-s01-pass-5-continuity-r2.md (SEASON-CONTINUITY-OK)
  note: >
    Fresh fork. No prior-audit context carried except the brief's note that Pass 5
    converged. All four sweeps conducted independently against the current aggregate
    state.

  findings:

    # ── SWEEP 1: REACHABILITY ──────────────────────────────────────────────────

    - id: S4-R-001
      type: pass
      what: >
        Season-open baseline → IGNITION traversal. Bones 1–80 establish the
        household stable with no surveillance and no sept-access. IGNITION beat
        is present at bones ~419–518 (swarm event, collection table overturned,
        oc-lords-steward draws and marks the incident folio at bones 496–499).
        The season-open conditions are satisfied; the IGNITION beat is present and
        structurally placed before the inquiry and maester beats.
      why: ~
      routing: ~

    - id: S4-R-002
      type: flag
      what: >
        Pryor's Taylor-specific naming in the incident record. The series plan
        requires: "Pryor watches from the far end of the square and makes the
        first institutional record of Taylor as a named anomaly." During the
        IGNITION sequence, the incident folio is drawn and marked at bones
        496–499 (oc-lords-steward draws the incident folio; marks it; faces the
        craft-stall edge; closes the folio). No bone within the IGNITION sequence
        (bones 419–519) explicitly shows Pryor writing or marking Taylor's name —
        only the collection-disruption is documented at that position. The
        inquiry folio (bones 604–619, during the witness-inquiry beat) contains
        Taylor-adjacent markings (oc-lords-steward marks the inquiry folio at
        613 and 618 after questioning Mira), but these are post-IGNITION and
        inquiry-scope, not the IGNITION-beat institutional naming. The two folios
        serve different beats. Whether the requirement is satisfied depends on
        whether the inquiry folio can stand as the "first record" — plausible
        under a reading that Pryor's formal naming of Taylor consolidates in the
        inquiry rather than at the incident — but the series plan's language
        locates this at the IGNITION beat itself.
      why: >
        If the Taylor-specific naming does not exist in the IGNITION-beat incident
        folio, the season-close condition "IGNITION incident on record (Pryor's
        note)" is nominally present but the naming beat is deferred to the inquiry
        sequence. This affects reachability of the S1 close: the plan's "note
        exists; it has reached one maester" presupposes a Taylor-specific record,
        not a general incident record. Phase 4 split and coach should confirm
        which folio carries the naming beat so the correct bone is in the correct
        episode. No reachability failure if the inquiry folio is the naming
        vehicle; advisory only.
      routing: editor (advisory; confirm folio assignment before Phase 4 split)

    - id: S4-R-003
      type: pass
      what: >
        Maester observation reaches network. Bones 802–898 cover the maester's
        visit end-to-end. Bone 893 (maester draws folio), 894 (passes to
        ferryman), 895 (ferryman takes), 898 (ferryman grips) and bone 906 (the
        ferry folio crosses the water) confirm the information carrier crossing
        the tier. Season-close condition satisfied.
      why: ~
      routing: ~

    - id: S4-R-004
      type: flag
      what: >
        S2 body-clock plant. The series plan (section H, structural note) requires:
        "the maester notes Taylor's age and physical state in his assessment — a
        detail he records, not a scene Taylor controls." The recording beats in
        the aggregate are bone 846 (the maester draws a notation) and bone 877
        (the maester marks the notation) — both are present. However no bone
        explicitly surfaces the age/body-state content of the notation; the
        recording action is present, the content is implicit. At Phase 3 shoot,
        coach will need to render the content of these notation bones explicitly
        enough that the plant is legible to a reader. The proto-line record is
        sufficient as a skeleton; the content requirement is a coach execution
        note.
      why: >
        If the maester's notation renders as a generic ledger observation rather
        than an age/body-state assessment, the S2 body-clock plant is absent from
        the prose even though the structural bone is present. Not a reachability
        fault at proto-line level; advisory for coach.
      routing: coach (advisory; notation bones 846, 877 must render age/body-state
               content in shoot)

    - id: S4-R-005
      type: pass
      what: >
        Mira-debt established. Witness-inquiry interlude (bones 564–643) transacts
        the earn: Mira withholds from Pryor at bones 608–626 (does not close the
        inquiry); the alley exchange at 628–641 creates the mutual
        acknowledgment. Plan condition "debt is real, unnamed, and not yet a
        coalition" is structurally present. No premature coalition-seeding found.
      why: ~
      routing: ~

    - id: S4-R-006
      type: pass
      what: >
        Elara's cover-protection irreversibly executed. Parents-act-in-concert
        interlude (bones 700–787) shows Elara at the sept with Rowan (704–729),
        at the reeve's house (741–746), back home with Edwyn (751–787), and the
        family unit re-cohering around Taylor (767–787). Taylor's present-tense
        decision is gestured at at bones 789–800 (holds feet, exhales, faces the
        table). The irreversible action and its cost to Taylor's operational cover
        are both structurally present.
      why: ~
      routing: ~

    # ── SWEEP 2: STATE ─────────────────────────────────────────────────────────

    - id: S4-S-001
      type: fault
      what: >
        The gifted volume — prop possession gap. At bones 206–208, septon-rowan
        offers the volume (206), taylor takes the volume (207), taylor grips the
        volume (208). Taylor exits the sept carrying this volume at bone 217
        (taylor exits the sept). At bones 220–232 (post-sept exchange between
        Taylor and Elara outside the sept), no volume release, set-down, or
        transfer is recorded. The volume is not mentioned again in the aggregate.
        At bones 234–250 (next sept scene), septon-rowan draws a volume (234)
        independently, which is consistent with Rowan having his own copy, but
        the volume Taylor was gifted and carries out of the sept at bone 217 has
        no recorded disposition. It is an open prop from bone 208 forward.
      why: >
        An ungifted prop — especially one Rowan explicitly offers and Taylor
        explicitly takes — that exits a location with an actor and is never
        released, referenced, or transferred creates a downstream possession
        ambiguity for Phase 4 split and shoot. The volume may reappear as a
        prop in a later household scene or become narratively significant (Elara
        noticing it; Taylor referencing it in the Elara interlude), and an
        unresolved release at the sept exit undermines that. Editor cannot safely
        assume the prop was left behind without a bone stating so.
      criteria: >
        The gifted volume must have a recorded disposition before or at the moment
        Taylor exits the sept at bone 217, or at the earliest subsequent bone
        where Taylor's possession state is established — either a bone releasing
        the volume within the sept, a bone showing Taylor sets or stores the volume
        upon returning home, or (if the volume travels with Taylor as a continuing
        prop) a bone acknowledging its continued presence at the next point where
        Taylor's carried items would be visible. The gap between bone 208 and the
        next scene where Taylor's hands/possession appear (bone 220) must not
        leave the volume in limbo.
      routing: fixer

    - id: S4-S-002
      type: flag
      what: >
        Cloth left open at bone 121. At bones 120–121, taylor-hebert-jaehaerys
        approaches the ledger bench (120) and lifts the cloth (121). The ledger
        is beneath (implied by the sequence context — Edwyn has the account ledger
        at bones 107–119). No bone records Taylor setting the cloth down. The
        scene ends at bone 124 (dye-yard swallow touches the gutter). The cloth
        is a minor domestic prop; its release is probably implicit in the scene
        close, but there is no explicit return bone.
      why: >
        Minor open prop. No downstream reference to the cloth suggests it is
        narratively dormant. Advisory only; editor may want to close it in prose
        pass.
      routing: editor (advisory)

    - id: S4-S-003
      type: pass
      what: >
        All series-cast actor entries and exits coherent across the season aggregate.
        Rymer Hedge: dock entry (335), IGNITION presence (464, 482, 516), post-
        alley observation (648–651), maester-exit observation (888–889). Mira
        Stonefield: passive IGNITION presence (429, 485–486), active witness-
        inquiry (553–641), maester-arrival observation (814–815). oc-child-peer:
        market scenes (253–295, 298–327), no further appearances. septon-rowan:
        sept scenes (152–217, 234–250, 399–411, 705–729, 864–883). oc-lords-
        steward: dock (335–417), IGNITION (421–517), inquiry (599–626),
        background in maester visit (offstage, per plan). Town reeve: inquiry
        rider (544–548), Mira exchange (584–597), Pryor approach (601–606),
        maester arrival (805–812, 823–825). All actor appearances are
        location-coherent and plan-consistent.
      why: ~
      routing: ~

    - id: S4-S-004
      type: pass
      what: >
        All major prop chains verified. Market slip (922→924 insert pair) closed.
        Census/literacy folio chain coherent (381–411). Inquiry folio chain
        coherent (604–619). Ferryman folio chain coherent (808→809→923→893→894→
        895→898→906) — confirmed by Pass 5, no new disruption found. Account
        ledger appearances coherent across workshop scenes. Market satchel
        (88→89→103) coherent. Winter candle (144→148→149) coherent. Dyed bolt
        (588→592→596–597→627) coherent. Water cup sequences coherent.
      why: ~
      routing: ~

    - id: S4-S-005
      type: flag
      what: >
        Bone numbering discontinuities. Three locations in the aggregate skip
        sequence numbers: (1) bones 388→390 (bone 389 absent); (2) bones 900→904
        (bones 901, 902, 903 absent); (3) bones 751→753 (bone 752 absent). These
        appear to be residue of prior fixer deletions. No content is orphaned by
        these gaps; no reference to the missing bone numbers exists in any
        insert-at annotation. Pass 5 did not flag these, consistent with their
        being pre-existing deletions.
      why: >
        Numbering gaps do not block Phase 3 shoot but will require reconciliation
        at Phase 4 split if the split algorithm uses bone numbers as index. Editor
        should be aware.
      routing: editor (advisory)

    # ── SWEEP 3: REFERENCE ─────────────────────────────────────────────────────

    - id: S4-REF-001
      type: pass
      what: >
        All named slugs resolve. Series-cast slugs (taylor-hebert-jaehaerys,
        oc-craftsman-mother, oc-craftsman-father, septon-rowan, oc-child-peer,
        mira-stonefield-jaehaerys, oc-lords-steward, rymer-hedge) confirmed
        against series plan section 5 cast list. Walk-on the-noun forms (the
        maester, the ferryman, the fishwife, the collector, the collector's man,
        the town reeve, the inquiry rider, a clerk, a mounted man, a townsman,
        the garrison man) are all structurally consistent with the plan's walk-on
        actor policy. "The maester" slug resolved per Pass 5 (cont-008):
        westerosi-traveling-maester.card.md confirmed.
      why: ~
      routing: ~

    - id: S4-REF-002
      type: pass
      what: >
        All insert-at annotations resolve. Nine insert bones (IDs 916–924) each
        carry a position marker referencing a bone number present in the aggregate
        (bones 48, 490, 519, 690, 787, 862, 36, 849, 42). All anchor bones exist.
        No orphan inserts. Split-from annotations (bones 914 from 334, 915 from
        511) reference existing bones. All annotations are internally consistent.
      why: ~
      routing: ~

    - id: S4-REF-003
      type: flag
      what: >
        Bone 219 absent. The aggregate goes from bone 217 (taylor exits the sept)
        to bone 218 (gap pacing bone) to bone 220 (oc-craftsman-mother speaks) —
        bone 219 is not present. No insert-at annotation targets 219; no reference
        to bone 219 exists anywhere in the aggregate. The gap between the sept
        exit and the post-sept exchange with Elara is covered by the pacing gap
        at 218, so no content is missing. The missing number is a sequencing
        artifact.
      why: >
        Advisory. No content gap. If Phase 4 split uses bone numbers as index
        anchors, the absence of 219 is a minor sequence irregularity. Editor
        should note.
      routing: editor (advisory)

    # ── SWEEP 4: POV ───────────────────────────────────────────────────────────

    - id: S4-POV-001
      type: pass
      what: >
        All five expected POV markers present with inline `# pov:` comment format.
        (1) Line 6: `# pov: taylor-hebert-jaehaerys` — aggregate open. (2)
        Line 620: `# pov: mira-stonefield-jaehaerys` — before bone 565, witness-
        inquiry interlude. (3) Line 710: `# pov: taylor-hebert-jaehaerys` —
        before bone 645, Taylor return after witness-inquiry. (4) Line 776:
        `# pov: oc-craftsman-mother` — before bone 701, parents-act-in-concert
        interlude. (5) Line 873: `# pov: taylor-hebert-jaehaerys` — before
        bone 789, Taylor return after Elara interlude. Count: 5. Expected: 5.
      why: ~
      routing: ~

    - id: S4-POV-002
      type: pass
      what: >
        All five POV switch positions are reachable from prior narrative bones.
        Switch 2 (Mira at bone 565): Taylor follows Mira into the alley at
        bone 563 — both characters co-located at switch point. Switch 3 (Taylor
        at bone 645): Mira exits alley at 641, Taylor holds feet at 642 and
        exhales at 643 — Taylor is the remaining subject at pov-return. Switch 4
        (Elara at bone 701): Elara present in workshop at bones 692–698 — the
        temporal jump to the sept lane entrance at bone 702 is a scene transition,
        not a location-coherence failure (Elara's agency to travel to the sept is
        established). Switch 5 (Taylor at bone 789): Taylor is at the family table
        at bones 785–787 — the return lands Taylor in situ.
      why: ~
      routing: ~

    - id: S4-POV-003
      type: flag
      what: >
        Witness-inquiry interlude POV boundary and Mira's entry. The season plan
        requires that no episode boundary cut a single POV-coherent stretch in
        two (section E, POV rulings). The Mira interlude runs from the pov-switch
        at line 620 (before bone 565) through the pov-return at line 710 (before
        bone 645). This is an 80-bone interlude (565–643). Phase 4 split must not
        place an episode boundary inside this range. Advisory flag for Phase 4
        split operator; not a current aggregate fault.
      why: >
        If Phase 4 split places a boundary inside bones 565–643, the Mira interlude
        is severed, violating the season-plan POV ruling (section E). The aggregate
        itself is clean; this is a Phase 4 constraint to honor.
      routing: Phase 4 split operator (advisory)

    - id: S4-POV-004
      type: flag
      what: >
        Parents-act-in-concert interlude POV boundary. The Elara interlude runs
        from the pov-switch at line 776 (before bone 701) through the pov-return
        at line 873 (before bone 789). This is an 88-bone interlude (701–787).
        Phase 4 split must not place an episode boundary inside this range.
      why: >
        Same as S4-POV-003. The aggregate is clean; Phase 4 must honor the
        interlude boundary.
      routing: Phase 4 split operator (advisory)
```

---

## Summary

**File-level verdict: SEASON-CONTINUITY-OK**

One fault, seven flags across four sweeps.

**Sweep 1 — Reachability (2 pass, 2 flag):**
All five season-close conditions are structurally reachable in the aggregate. S4-R-002 flags that the IGNITION-beat incident folio does not contain an explicit Taylor-naming bone — the inquiry folio (bones 613, 618) is the most plausible carrier, but the plan locates the naming at IGNITION. Advisory to editor before Phase 4 split. S4-R-004 flags that the maester's notation bones (846, 877) must render age/body-state content at shoot. Both are advisory; no reachability failure. No escalations.

**Sweep 2 — State (1 fault, 2 flag, 2 pass):**
S4-S-001 is the single fault: the volume Rowan gifts Taylor (bones 206–208) exits the sept with Taylor at bone 217 and has no recorded disposition thereafter — an open prop through the remainder of the aggregate. Routed to fixer (episode scope). S4-S-002 flags the cloth lifted at bone 121 with no explicit release — minor, advisory to editor. S4-S-005 flags three existing bone-numbering gaps as editor advisory.

**Sweep 3 — Reference (2 pass, 2 flag):**
All slugs resolve; all insert-at annotations have valid anchor bones. S4-REF-003 flags bone 219 absent as a sequencing artifact with no content consequence.

**Sweep 4 — POV (2 pass, 2 flag):**
All five POV markers present and all five transition positions are reachable. S4-POV-003 and S4-POV-004 flag the two interlude ranges (bones 565–643 and 701–787) as Phase 4 split constraints — no episode boundary may bisect either interlude.

**Routing summary:** 1 fault → fixer. 5 flags → editor (advisory). 2 flags → Phase 4 split operator. 1 flag → coach (shoot notation guidance).
