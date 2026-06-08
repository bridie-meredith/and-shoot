```yaml
audit:
  scope: chapter
  target: b01c19
  timestamp: 2026-06-05
  phases: [phase-5-continuity, phase-6-substance-bone-gate]
  source_files:
    - active-project/staff/showrunner/b01c19-bones-draft.md   # 36 bones (incl. n02b companion; flat_id pending)
    - active-project/staff/showrunner/memory.md               # chapters[b01c18].handoff_out + chapters[b01c19] full entry

  findings:

    # ─────────────────────────────────────────────
    # PHASE 5 — CONTINUITY
    # ─────────────────────────────────────────────

    - id: continuity-verdict
      type: pass
      what: PHASE 5 overall — CONTINUITY-OK
      why: >
        All four continuity axes pass. Detailed sub-verdicts below; no fault classification
        fires on any axis. The chapter is cleared for Phase 6.

    - id: phase5-reachability
      type: pass
      what: FAULT-REACHABILITY check — chapter goal vs. bones delivery
      why: >
        Chapter goal: "contempt-without-refusal at completion + first non-suppressed
        recognition (non-terminal)."
        Delivery verified:
        - Contempt-lock: flat_id 24 (taylor lifts the stylus, pol-reg +0.5 → rank 9 LOCK)
          + flat_id 25 (stylus meets ledger-edge, holds-at-LOCK) + flat_id 26
          (ledger-edge receives stylus, LOCK image). The lock is enacted as physical
          choreography per CFR-2; it is not stated as interior conclusion.
        - First non-suppressed recognition: flat_id 14 (taylor sets the stylus, moral-leg
          +0.5) in s02, carried by the physical enumeration arc (flat_ids 10–14) that
          constitutes CFR-1. The recognition begins without completing; flat_id 15
          (factional-reading structure assembles) holds the recognition at beginning-not-terminal.
        - handoff_out matches: political_register-prot rank 9 LOCKED, moral_legibility rank 7
          (recognition beginning), social_tether-prot-collapse rank 4.5, position-prot-collapse
          rank 4, capability 8.5, relational_anchor 7.5, moral_framework -4. All consistent
          with the bone-level movement totals (pol-reg +1.5 from 7.5 → 9; moral-leg +0.5 from
          6.5 → 7; tether-collapse -1.5 from 6 → 4.5; pos-collapse -1.0 from 5 → 4).
      what: No reachability fault.

    - id: phase5-state-reference
      type: pass
      what: FAULT-STATE / FAULT-REFERENCE check — prop/location/actor consistency
      why: >
        Sole on-page actor: taylor-hebert-kl-122ac. Confirmed in chapter header and consistent
        with bones throughout. Named-but-not-present: Daven (rendered as absence via object-as-subject
        form per no-negation rule — flat_ids 28/31/29; acceptable). Jarvis: named as dead-drop channel
        (flat_id 22, "the Jarvis channel receives the compiled-reading") — correctly rendered as
        institutional mechanism, not a present actor. Wren: not named in any bone; relational_anchor
        held discipline maintained.
        Locations: the-tallow-render-works (s01-s03 primary); Tallow Croft corner / Daven's lane (s04).
        Both consistent with chapter header and memory.md chapter entry.
        Props: trough (dead-drop, flat_id 1), cost-ledger/stylus (s01-s03), running-architecture record
        (flat_id 33/34/35). All within established architecture per c18 handoff_out
        ("Wren: anchor rank 7.5; screened; Jarvis channel; coverage-map").
      what: No state or reference fault.

    - id: phase5-pov
      type: pass
      what: FAULT-POV check — perception-verb leak / narrator consistency
      why: >
        All 36 bones use concrete physical SVO form. No perception-verb from a non-Taylor
        subject applied to Taylor's interior. The n02b companion bone ("the grey-dark covers
        the sheet") correctly uses environment as SVO subject. The "daven absents the corner"
        (flat_id 31) uses object-as-subject form — the note in the bones file explicitly
        licenses this ("SVO collapses to positive per the no-negation rule: Daven's absence
        is rendered as Daven-absents"). No perception-verb leak detected. Chapter is silent
        and solitary (zero speech bones confirmed); no narrator inconsistency.
      what: No POV fault.

    - id: phase5-handoff-in-mismatch
      type: pass
      what: FAULT-HANDOFF-IN-MISMATCH check — handoff_in vs. b01c18 handoff_out
      why: >
        b01c18 handoff_out (memory.md lines ~11404–11417 aggregate close) states:
        - pol-reg-prot: near-saturation 7.5 (s05 final +0.5 landing)
        - moral_framework: -4.0
        - position-prot-collapse: ~5 (s05 final -0.5 landing from 5.5 → 5)
        - social_tether-prot-collapse: ~6 (s05 final -0.5 landing from 6 → 6... wait)

        Reconciliation: memory.md chapters[b01c19].handoff_in states:
        - pol-reg-prot rank 7.5 ✓ (matches c18 s05 final move landing +0.5 at ~7.5)
        - position-prot-collapse rank 5 ✓ (matches c18 s05 final -0.5: 5.5 → 5)
        - social_tether-prot-collapse rank 6 ✓ (matches c18 s05 final -0.5: 6 → 6... )

        Note: c18 s05 notes say social_tether-prot-collapse goes "toward 6" (-0.5 from
        6 → landing ~6?). The c18 s02 fired -0.5 from 7→6.5, s05 fires -0.5 from 6.5→6. 
        c19 handoff_in declares tether-collapse rank 6. Consistent.
        - moral_legibility: legibility held at crack-level through c18 (no c18 gain).
          c18 does not move moral_legibility. c19 handoff_in does not state moral_legibility
          explicitly in character_state, but the c19 chapter contract enters at 6.5 per the
          bone notes (flat_id 14 notes "legibility from 6.5 toward 7"). Consistent with c18
          holding at 6.5 (c16's +0.5 gave 6.5; c18 held it flat).
        - capability rank 8.5 ✓ (c18 handoff_out corrected to 8.5)
        - relational_anchor rank 7.5 ✓
        Open threads from c18 carried: irrevocable deployment complete ✓; Green succession move
        landed ✓; contempt near-saturation ✓; position-prot-collapse rank 5 ✓; tether-collapse
        rank 6 ✓; false attribution in Otto's picture ✓.
        Opening bones honor handoff_in: flat_id 1 (trough releases cipher-bundle = dead-drop channel
        operational per open threads), flat_id 2 (taylor opens the sheet = accounting at existing
        rank). No open thread from c18 is dropped or contradicted.
      what: No handoff-in mismatch fault.

    # ─────────────────────────────────────────────
    # PHASE 6 — SUBSTANCE BONE-GATE
    # ─────────────────────────────────────────────

    # --- PER-BONE MOVING BONES ---

    - id: p6-bone-flat8
      type: pass
      what: Moving bone flat_id 8 — "the column receives the contempt-entry" (pol-reg-prot +0.5)
      why: >
        BONEFIDE check: The column physically receives the contempt-entry because the ambient
        outer-ring feed (flat_id 7, "the bottlefly nodes return the outer-ring feed") returns
        court-content while the accounting is still open. The causal chain is concrete: feed
        returns → color arrives → column receives entry. The SVO causes the declared +0.5.
        Rank-claim visible: flat_id 7 holds pol-reg pending the move at flat_id 8; the move
        is grounded in the specific feed content arriving (court-machinery performing function
        for no lower-city audience). SUBSTANCE-FLAT check: cause visible and specific. PASS.

    - id: p6-bone-flat14
      type: pass
      what: Moving bone flat_id 14 — "taylor sets the stylus" (moral-leg +0.5)
      why: >
        BONEFIDE check: The set-stylus is the physical form of the recognition-beginning-not-terminal
        event. The preceding arc (flat_ids 10–13) builds the physical enumeration the CFR-1 requires:
        the column runs (flat_id 10), repeats its shape (flat_id 11), the lane-shape marks the stone
        (flat_id 12), Taylor marks the column entry (flat_id 13). Flat_id 14 is the movement bone
        at the correct causal position: after physical enumeration but before continued assembly
        (flat_id 15). The SVO causes the declared +0.5 through enacted physical discipline, not
        interior sentiment. Rank-claim visible. PASS.

    - id: p6-bone-flat17
      type: pass
      what: Moving bone flat_id 17 — "taylor files the entry" (pol-reg-prot +0.5)
      why: >
        BONEFIDE check: The groom with the message-case (flat_id 16) is the specific court-tier body
        that generates the court-content; flat_id 17 files the entry into the column whose shape has
        now been named. The causal chain is concrete: court-body returns via ambient feed → body
        performs factional function → entry filed. Notes are explicit: "naming [the pattern] changed
        nothing about where the entry goes" — the filing despite the naming is the enacted contempt
        accumulation. SVO causes the declared +0.5. SUBSTANCE-FLAT check: cause visible. PASS.

    - id: p6-bone-flat24
      type: pass
      what: Moving bone flat_id 24 — "taylor lifts the stylus" (pol-reg-prot +0.5 LOCK)
      why: >
        BONEFIDE check: Flat_id 24 is BONE 1 of the CFR-2 two-bone enacted distinction. The lift is
        the closing gesture that precedes the beside-placement at flat_id 25. The causal chain:
        request executed (flat_ids 18–22) → compiled reading dropped through Jarvis (flat_id 22) →
        cost-ledger column closes (flat_id 23) → stylus lifts (flat_id 24, +0.5 LOCK). The final +0.5
        draws pol-reg to rank 9 LOCK; the lift is the physical form of the lock (the close, not an
        interior naming). This is the final cl06 draw. SUBSTANCE-FLAT check: cause is the request-
        completion + column-close sequence, visible across flat_ids 18–23. PASS.

    - id: p6-bone-flat32
      type: pass
      what: Moving bone flat_id 32 — "taylor walks the lane" (social_tether-prot-collapse -1.5)
      why: >
        BONEFIDE check: The walk-without-pausing is causally downstream of the concrete inference
        instruments: flat_id 28 (second-bell passes empty corner), flat_id 29 (vat-house shutter
        closes window), flat_id 30 (taylor takes lane-position / second approach), flat_id 31
        (daven absents the corner). The physical fact of the closed shutter against forty-three
        prior-unshuttered approaches (staged in flat_id 29 notes) IS the tether-node severance
        signal. Flat_id 32 walks past it — this physical action is the protagonist-force's concrete
        response to the opposing-force's concrete evidence. The SVO causes the declared -1.5 because
        the walk-without-pausing is the enacted form of processing the inference-instrument and
        continuing. Rank-claim: collapse in motion since c18; the first full tether-node severance
        fires here, landing tether-collapse 6 → 4.5. Cause visible. PASS.

    - id: p6-bone-flat33
      type: pass
      what: Moving bone flat_id 33 — "taylor opens the running-architecture record" (pos-collapse -1.0)
      why: >
        BONEFIDE check: Opening the record to write Daven out is the concrete act that enacts the
        position-prot-collapse. The notes make the causal chain explicit: "the witch-label in the
        upper city means contacts who know the accessible face of the architecture are making cost
        calculations; the act of documenting the node-loss is the position-collapse event." The SVO
        causes the declared -1.0 because it is the formal operational response to the position-risk
        becoming structural. Rank-claim: pos-collapse in motion from c17/c18; this is the witch-label
        reaching the upper city's effect on Taylor's position. Cause visible. PASS.

    # --- PER-BONE HELD BONES SPOT-CHECK (HELD-AXIS-NOT-ENACTED) ---

    - id: p6-held-bones
      type: pass
      what: HELD-AXIS-NOT-ENACTED check — sample of held bones across all four scenes
      why: >
        Sample of held bones reviewed against "enacts discipline/dormancy on the held axis":

        s01 flat_id 1 (trough releases, social_tether-antag held): the trough is the structural
        conduit of the tether; operating at its locked rank. Enacted as location-grounded
        physical gesture. PASS.

        s01 flat_id 2 (taylor opens sheet, moral_framework held): eleven-months-same-posture
        same-reading-light enacted through the grey-dark reading-light detail (flat_id n02b
        companion bone). Physical form of the consumed-as-compass state. PASS.

        s01 flat_id 6 (protection-line ratio runs, pos-collapse + tether-collapse held):
        rationale explicitly states both collapse axes are "in motion from c18; held at this
        scene; the severance fires in s04." Dormancy properly scoped. PASS.

        s02 flat_id 13 (taylor marks the column entry, moral-leg held + relational_anchor held):
        the marking is the physical enumeration act that carries CFR-1. Enacted; not asserted.
        PASS.

        s03 flat_id 25 (stylus meets ledger-edge, pol-reg held-at-LOCK): the beside-placement
        is the CFR-2 BONE 2, physically enacted as the spatial adjacency form. PASS.

        s03 flat_id 26 (ledger-edge receives stylus, pol-reg held + tether-collapse held + pos-collapse held):
        the ledger-edge receiving is the image bone for the alongside-not-inside form. Held axes
        properly scoped to s04 fire. PASS.

        s04 flat_id 34 (coverage-map drops the daven node, tether-collapse held-post-move + capability held):
        writing Daven out formally. The -1.5 already fired at flat_id 32; flat_id 34 is the
        formal documentation of the landing. PASS.

        No HELD-AXIS-NOT-ENACTED fault found.

    - id: p6-held-uncontracted
      type: pass
      what: HELD-AXIS-UNCONTRACTED check — held bones reference axes in scene axes_held or stakes_axis
      why: >
        Per pl-2026-05-25-018, post-move holding of an in-motion axis is implicitly licensed (schema
        ambiguity ruled). Held axes in bones that are not in scene axes_held but are the scene's
        stakes_axis or are axes in scene axes_in_motion (post-move discipline) are acceptable.
        No bone holds an axis that is neither in axes_held, axes_in_motion, nor the stakes_axis
        for its scene. The social_tether-antag "locked at 9" hold appears across all four scenes;
        social_tether-antag is listed as locked (axes_held) in the chapter contract. PASS.

    # --- PER-SCENE CHECKS ---

    - id: p6-s01-event-presence
      type: pass
      what: EVENT-PRESENCE check — s01
      why: >
        event_map: 6 tag entries + 2 author-noticed. All 8 covered. Central event for s01:
        "new-request-arrives-via-dead-drop" (tagged [event]) covered by flat_ids 1 + 2. Scene_conflict
        protagonist_force ("opens the accounting") covered by flat_id 5 (taylor opens cost-ledger column).
        PASS.

    - id: p6-s01-chunk-tag-completeness
      type: pass
      what: CHUNK-TAG-COMPLETENESS check — s01
      why: >
        s01 chunk tags: [event: new-request-arrives-via-dead-drop] ✓, [mechanism: request-scope-identified] ✓,
        [force: opposing] ✓, [image: folded-sheet-lighter-than-its-weight] ✓, [force: protagonist] ✓,
        [event: request-accounting-opens-contempt-color-arrives] ✓. All 6 tags have event_map entries.
        Bones file checklist (vi) confirms ALL TAGS COVERED. PASS.

    - id: p6-s01-axis-delta
      type: pass
      what: PER-AXIS Δ check — s01 (contract: pol-reg +0.5)
      why: >
        Delivered: flat_id 8 pol-reg-prot +0.5. Total s01 pol-reg: +0.5. Contract: +0.5. EXACT. PASS.

    - id: p6-s01-stakes-dominant
      type: pass
      what: STAKES-AXIS-DOMINANT check — s01 (stakes: pol-reg-prot)
      why: >
        Only one mover in s01: pol-reg +0.5. Stakes axis is pol-reg. No non-stakes axis exceeds it. PASS.

    - id: p6-s01-sensory-grounding
      type: pass
      what: SENSORY-GROUNDING check — s01 (≥1 grounding bone required)
      why: >
        flat_id 1: trough (named physical dead-drop location). flat_id n02b: grey-dark (sensory/environment).
        flat_id 4: tallow-render room floor (named location). Three grounding bones in 9 total = 33%.
        Hard minimum met. PASS.

    - id: p6-s01-event-not-concrete
      type: pass
      what: EVENT-NOT-CONCRETE check — s01 central event
      why: >
        Central event "new-request-arrives-via-dead-drop" is carried by flat_id 1 ("the trough releases
        the cipher-bundle") — concrete actor-verb-object SVO. Not instrument/process/perception rendering.
        PASS.

    - id: p6-s01-opposing-force
      type: pass
      what: OPPOSING-FORCE-MISSING check — s01
      why: >
        Opposing force (arrangement structural logic; access within existing architecture; accounting
        runs clean) is visible at flat_id 3 (sheet names chamberlain; capability held because "the request
        is within the existing node-map") and flat_id 6 (protection-line ratio runs; tether/position held
        because no mechanism produces refusal). PASS.

    - id: p6-s01-cost-ledger
      type: pass
      what: COST-NOT-PAID check — s01 (cl06 resolving at this scene)
      why: >
        cl06 gain-side (pol-reg +0.5 first tranche) is paid by flat_id 8 with cost_ledger_anchor: cl06.
        Direction matches (pol-reg up). PASS.

    - id: p6-s01-held-axis-witnessed
      type: pass
      what: HELD-AXIS-NOT-WITNESSED check — s01 axes_held
      why: >
        s01 axes_held: social_tether-antag, moral_framework, capability, moral_legibility_to_self,
        relational_anchor_status, social_tether-prot-collapse, position-prot-collapse, political_register-prot.
        Witnessed:
        - social_tether-antag: flat_id 1 (rationale explicit).
        - moral_framework: flat_id 2 + flat_id n02b + flat_id 4 + flat_id 5 (consumed-as-compass enacted).
        - capability: flat_id 3 (existing node-map; no expansion).
        - moral_legibility_to_self: flat_id 5 (suppression still fully operational; pattern-recognition
          fires in s02; held at existing rank).
        - relational_anchor_status: flat_id 4 (eastern gap not touched).
        - social_tether-prot-collapse: flat_id 6 (held; severance fires s04).
        - position-prot-collapse: flat_id 6 (held; fires s04).
        - political_register-prot: flat_id 7 (accumulating toward move at flat_id 8; held pending).
        All axes_held have ≥1 witness bone. PASS.

    - id: p6-s01-stakes-axis-missing
      type: pass
      what: STAKES-AXIS-MISSING check — s01 (stakes_axis: political_register-prot)
      why: >
        pol-reg-prot is in s01 axes_in_motion (target_delta_magnitude 0.5). PASS.

    - id: p6-s02-event-presence
      type: pass
      what: EVENT-PRESENCE check — s02
      why: >
        event_map: 7 tag entries + 1 author-noticed. All 8 covered. Central event "accounting-catches-its-
        own-pattern" covered by flat_ids 9 + 10 + 11. Scene_conflict protagonist_force ("accounting sees
        its own pattern mid-run") covered by flat_ids 10 + 13 + 14. PASS.

    - id: p6-s02-chunk-tag-completeness
      type: pass
      what: CHUNK-TAG-COMPLETENESS check — s02
      why: >
        s02 tags: [event: accounting-catches-its-own-pattern] ✓, [mechanism: pattern-recognition-in-the-ledger] ✓,
        [image: ledger-column-with-its-own-shape] ✓, [force: opposing] ✓, [force: protagonist] ✓,
        [event: suppression-no-longer-fully-operational] ✓, [mechanism: recognition-beginning-not-terminal] ✓.
        All 7 tags covered. PASS.

    - id: p6-s02-axis-delta
      type: pass
      what: PER-AXIS Δ check — s02 (contract: moral-leg +0.5 + pol-reg +0.5)
      why: >
        Delivered: flat_id 14 moral-leg +0.5; flat_id 17 pol-reg +0.5. Both exact. PASS.

    - id: p6-s02-stakes-dominant
      type: pass
      what: STAKES-AXIS-DOMINANT check — s02 (stakes: moral_legibility_to_self)
      why: >
        Two movers: moral-leg +0.5 and pol-reg +0.5. Equal magnitudes. Stakes axis is moral-leg.
        The equal case: the instruction states "equal is acceptable, flag only if a non-stakes EXCEEDS."
        pol-reg does not exceed moral-leg (equal). PASS.

    - id: p6-s02-sensory-grounding
      type: pass
      what: SENSORY-GROUNDING check — s02 (≥1 grounding bone required)
      why: >
        flat_id 9: cost-ledger (named physical document, grounding). flat_id 12: lane-stone worn track
        (named concrete surface, grounding). Two grounding bones. Hard minimum met. PASS.

    - id: p6-s02-event-not-concrete
      type: pass
      what: EVENT-NOT-CONCRETE check — s02 central event
      why: >
        Central event "accounting-catches-its-own-pattern" is carried by flat_id 10 ("taylor runs the
        factional-reading column") — a concrete physical enumeration act, not an interior-state label.
        The CFR-1 compliance is explicit in the bones notes: "the counting is the physical enumeration
        act." PASS.

    - id: p6-s02-opposing-force
      type: pass
      what: OPPOSING-FORCE-MISSING check — s02
      why: >
        Opposing force (the column's own structure; the discipline that makes suppression possible is
        what allows the pattern to name itself) is visible at flat_id 9 (column runs eleven months of
        entries; the framework's most violated line runs through every entry) and flat_id 11 (column
        repeats its shape — the shape is in the document, not in Taylor's interior). PASS.

    - id: p6-s02-cost-ledger
      type: pass
      what: COST-NOT-PAID check — s02 (cl07a gain opens + cl06 second tranche)
      why: >
        cl07a gain-side (moral-leg +0.5) paid by flat_id 14 with cost_ledger_anchor: cl07a. PASS.
        cl06 draw (pol-reg +0.5 second tranche) paid by flat_id 17 with cost_ledger_anchor: cl06. PASS.

    - id: p6-s02-held-axis-witnessed
      type: pass
      what: HELD-AXIS-NOT-WITNESSED check — s02 axes_held
      why: >
        s02 axes_held: moral_framework, relational_anchor_status, social_tether-prot-collapse,
        position-prot-collapse, capability, social_tether-antag.
        Witnessed:
        - moral_framework: flat_id 9 (column's weight = consumed-as-compass form), flat_id 11
          (shape the column has worn = framework's most violated line).
        - relational_anchor_status: flat_id 13 (pattern-recognition at accounting's shape, not Wren-gap).
        - social_tether-prot-collapse: flat_id 15 (held; severance fires s04).
        - position-prot-collapse: flat_id 15 (held; fires s04).
        - capability: flat_id 10 (targeted chamberlain-reading assembles in existing column; no expansion).
        - social_tether-antag: flat_id 15 (locked at 9; does not move).
        All axes_held have ≥1 witness bone. PASS.

    - id: p6-s02-stakes-axis-missing
      type: pass
      what: STAKES-AXIS-MISSING check — s02 (stakes_axis: moral_legibility_to_self)
      why: >
        moral_legibility_to_self is in s02 axes_in_motion. PASS.

    - id: p6-s03-event-presence
      type: pass
      what: EVENT-PRESENCE check — s03
      why: >
        event_map: 8 tag entries + 2 author-noticed. All 10 covered. Central event "contempt-without-refusal-
        locked" covered by flat_ids 24 + 25. Scene_conflict protagonist_force ("closes the cost-ledger")
        covered by flat_id 23. PASS.

    - id: p6-s03-chunk-tag-completeness
      type: pass
      what: CHUNK-TAG-COMPLETENESS check — s03
      why: >
        s03 tags: [event: request-execution-enacted] ✓, [mechanism: targeted-reading-completes] ✓,
        [image: chamberlain-corridor-in-compound-register] ✓, [event: contempt-without-refusal-locked] ✓,
        [force: protagonist] ✓, [force: opposing] ✓, [mechanism: contempt-sits-alongside-not-inside] ✓,
        [image: contempt-alongside-the-accounting] ✓. All 8 tags covered. PASS.

    - id: p6-s03-axis-delta
      type: pass
      what: PER-AXIS Δ check — s03 (contract: pol-reg +0.5 LOCK)
      why: >
        Delivered: flat_id 24 pol-reg +0.5 → rank 9 LOCK. Exact. PASS.

    - id: p6-s03-stakes-dominant
      type: pass
      what: STAKES-AXIS-DOMINANT check — s03 (stakes: pol-reg-prot)
      why: >
        Only one mover: pol-reg +0.5. No non-stakes axis exceeds it. PASS.

    - id: p6-s03-sensory-grounding
      type: pass
      what: SENSORY-GROUNDING check — s03 (≥1 grounding bone required)
      why: >
        flat_id 19: chamberlain crosses pillar junction (named architectural feature, grounding).
        flat_id 22: Jarvis channel receives compiled-reading (named institutional mechanism + concrete
        physical drop act, grounding). Two grounding bones. Hard minimum met. PASS.

    - id: p6-s03-event-not-concrete
      type: pass
      what: EVENT-NOT-CONCRETE check — s03 central event (contempt-lock) — per-dispatch requirement
      why: >
        Central event "contempt-without-refusal-locked" is carried by flat_id 24 ("taylor lifts the
        stylus") and flat_id 25 ("the stylus meets the ledger-edge"). These are concrete actor-verb-object
        SVOs. The lock is enacted as physical choreography (CFR-2: two-bone sequence: lift → beside-set).
        flat_id 25 note: "the beside-placement is the enacted physical distinction." Not instrument/
        process/perception rendering. CONCRETE. PASS.

    - id: p6-s03-opposing-force
      type: pass
      what: OPPOSING-FORCE-MISSING check — s03
      why: >
        Opposing force (contempt at lock, sitting alongside the accounting with no exit attached) is
        visible at flat_id 25 (stylus meets ledger-edge; "beside, not away from" enacted) and flat_id 26
        (ledger-edge receives stylus; "contempt adjacent to every line but not itself a line" — the form
        the lock takes). PASS.

    - id: p6-s03-cost-ledger
      type: pass
      what: COST-NOT-PAID check — s03 (cl06 final draw)
      why: >
        cl06 final draw (pol-reg +0.5 → LOCK) paid by flat_id 24 with cost_ledger_anchor: cl06.
        s03 notes on flat_id 24 state: "cl06 paid: contempt-without-refusal complete; cl06 cost-entry
        complete." PASS.

    - id: p6-s03-held-axis-witnessed
      type: pass
      what: HELD-AXIS-NOT-WITNESSED check — s03 axes_held
      why: >
        s03 axes_held: moral_framework, moral_legibility_to_self, relational_anchor_status,
        social_tether-prot-collapse, position-prot-collapse, capability, social_tether-antag.
        Witnessed:
        - moral_framework: flat_id 18 (bottlefly routes open; existing channel; no new threshold),
          flat_id 23 (cost-ledger closes; consumed-as-compass holds).
        - moral_legibility_to_self: flat_id 23 (recognition begun in s02 does not extend here;
          blank column holds; legibility holds at 7).
        - relational_anchor_status: flat_id 21 (chamberlain-reading; eastern gap not touched).
        - social_tether-prot-collapse: flat_id 26 (collapse in motion; held; severance fires s04).
        - position-prot-collapse: flat_id 26 (held; fires s04).
        - capability: flat_id 18 (targeted reading; three outer-ring corridor nodes; no scope expansion).
        - social_tether-antag: flat_id 22 (Jarvis channel completing its current cycle; no new leverage).
        All axes_held have ≥1 witness bone. PASS.

    - id: p6-s03-stakes-axis-missing
      type: pass
      what: STAKES-AXIS-MISSING check — s03 (stakes_axis: political_register-prot)
      why: >
        pol-reg-prot is in s03 axes_in_motion. PASS.

    - id: p6-s04-event-presence
      type: pass
      what: EVENT-PRESENCE check — s04
      why: >
        event_map: 9 tag entries + 1 author-noticed (pl-2026-06-05-c19-001 shutter instrument).
        All 10 entries covered. Central event "witch-label-reached-upper-city-contact" covered by
        flat_ids 30 + 31. Scene_conflict protagonist_force ("Taylor walks the lane without pausing")
        covered by flat_id 32. PASS.

    - id: p6-s04-chunk-tag-completeness
      type: pass
      what: CHUNK-TAG-COMPLETENESS check — s04
      why: >
        s04 tags: [event: ward-contact-stops-responding] ✓, [mechanism: reciprocity-channel-check-runs] ✓,
        [image: empty-corner-second-bell] ✓, [force: opposing] ✓, [event: witch-label-reached-upper-city-contact] ✓,
        [force: protagonist] ✓, [mechanism: position-risk-named-in-walking] ✓, [event: tether-node-removed-
        architecture-still-running] ✓, [image: coverage-map-with-node-written-out] ✓. All 9 tags covered.
        Screen-writer reported 22 tags all mapped; count verified across all four scenes: 22 total tags,
        all have event_map entries. PASS.

    - id: p6-s04-axis-delta
      type: pass
      what: PER-AXIS Δ check — s04 (contract: tether-collapse -1.5 + pos-collapse -1.0)
      why: >
        Delivered: flat_id 32 tether-collapse -1.5; flat_id 33 pos-collapse -1.0. Both exact.
        PASS.

    - id: p6-s04-stakes-dominant
      type: pass
      what: STAKES-AXIS-DOMINANT check — s04 (stakes: social_tether-prot-collapse)
      why: >
        Two movers: tether-collapse -1.5 and pos-collapse -1.0. Stakes axis is tether-collapse.
        Magnitude 1.5 > 1.0 — tether-collapse exceeds pos-collapse. No non-stakes axis exceeds the
        stakes axis. PASS.

    - id: p6-s04-sensory-grounding
      type: pass
      what: SENSORY-GROUNDING check — s04 (≥1 grounding bone required)
      why: >
        flat_id 27: Tallow Croft corner position (named physical location + concrete positioning).
        flat_id 29: vat-house shutter closes window (named physical object, concrete state-change).
        flat_id 34: coverage-map drops the daven node (named physical document + concrete scribal act).
        Three grounding bones in 9 total = 33%. Hard minimum met. PASS.

    - id: p6-s04-event-not-concrete
      type: pass
      what: EVENT-NOT-CONCRETE check — s04 central event (witch-label-reach) — pl-2026-06-05-c19-001 RESOLUTION
      why: >
        This is the parking-lot HARD watch item. Resolution determination follows.

        The s04 central event — witch-label reaching upper city / Daven severance — is carried by:
        - flat_id 28: "the second-bell passes the Tallow Croft corner" — concrete location-state fact
          (the corner holds empty at second-bell). SVO subject is the bell/time, staging the absence
          as a physical temporal fact, not as Taylor's inference. Notes: "staged as a physical fact of
          the location (the corner holds empty)."
        - flat_id 29: "the vat-house shutter closes the window" — the concrete inference instrument.
          Notes explicitly: "the shuttered window IS the concrete information; this bone stages it as
          a physical object-state change (the shutter closes the window) rather than as an inferred
          conclusion." The shutter has been unshuttered across forty-three prior approaches in seven
          months — the closure IS the information. A Westerosi physical object carries the narrative
          work.
        - flat_id 30: "taylor takes the lane-position" — second approach enacted as physical
          positioning; Daven's absence confirmed through Taylor's own held position that returns
          nothing.
        - flat_id 31: "daven absents the corner" — absence rendered as positive SVO per no-negation
          rule (object-as-subject permitted for ambient/unknown actors acting as absence).

        The inference is not narrated as interior conclusion. The physical instruments (empty corner at
        second-bell, closed shutter against forty-three-prior-open-approaches, second approach confirming)
        carry the inference. Taylor then walks (flat_id 32), opens the record (flat_id 33), writes Daven
        out (flat_id 34), closes the record (flat_id 35). Concrete sequence from inference-instrument →
        physical response throughout.

        The label-reach event is ON-PAGE and CONCRETE, not inferred-off-page / asserted-not-dramatized.

        **pl-2026-06-05-c19-001 STATUS: RESOLVED.**
        The EVENT-NOT-CONCRETE HARD condition from the parking-lot watch does not fire.
        The bones satisfy the resolution suggestion: "ensure s04 has a concrete central-event bone
        staging the shuttered-window/empty-corner instrument of the inference" — met by flat_ids 28/29/30/31.

    - id: p6-s04-opposing-force
      type: pass
      what: OPPOSING-FORCE-MISSING check — s04
      why: >
        Opposing force (witch-label in upper city; contacts who can calculate the cost will) is visible
        at flat_id 28 (empty corner at second-bell — first concrete signal), flat_id 29 (vat-house shutter
        closed — the inference instrument), and flat_id 31 (daven absents the corner — enacted severance).
        Three bones show opposing force concretely. PASS.

    - id: p6-s04-cost-ledger
      type: pass
      what: COST-NOT-PAID check — s04 (cl07a cost accelerating + cl07b cost)
      why: >
        cl07a cost-side (tether-collapse -1.5) paid by flat_id 32 with cost_ledger_anchor: cl07a. PASS.
        cl07b cost-side (pos-collapse -1.0) paid by flat_id 33 with cost_ledger_anchor: cl07b. PASS.

    - id: p6-s04-held-axis-witnessed
      type: pass
      what: HELD-AXIS-NOT-WITNESSED check — s04 axes_held
      why: >
        s04 axes_held: political_register-prot, moral_legibility_to_self, moral_framework,
        relational_anchor_status, capability, social_tether-antag.
        Witnessed:
        - political_register-prot: flat_id 35 (LOCKED at 9; close-coverage-record; does not move further).
        - moral_legibility_to_self: flat_id 30 (second approach; node-severance recorded with accounting
          discipline; does not advance legibility further; terminal recognition is c20).
        - moral_framework: flat_id 35 (write-out is operational response to a loss; no new breach).
        - relational_anchor_status: flat_id 31 (Daven explicitly NOT Wren; eastern gap not touched),
          flat_id 35 (Wren in coverage; anchor holds at 7.5).
        - capability: flat_id 34 (scope-adjustment within existing architecture; bottlefly-node at Croft
          intersection holds lane without reciprocity layer).
        - social_tether-antag: flat_id 35 (locked at 9; does not move).
        All axes_held have ≥1 witness bone. PASS.

    - id: p6-s04-stakes-axis-missing
      type: pass
      what: STAKES-AXIS-MISSING check — s04 (stakes_axis: social_tether-prot-collapse)
      why: >
        social_tether-prot-collapse is in s04 axes_in_motion. PASS.

    # --- PER-CHAPTER CHECKS ---

    - id: p6-chapter-axis-sum
      type: pass
      what: Per-axis chapter Δ sums vs. contract targets
      why: >
        From the bones file summary table:
        - pol-reg-prot: s01 +0.5 + s02 +0.5 + s03 +0.5 = +1.5. Target +1.5. EXACT.
        - moral-leg: s02 +0.5. Target +0.5. EXACT.
        - tether-collapse: s04 -1.5. Target -1.5. EXACT.
        - pos-collapse: s04 -1.0. Target -1.0. EXACT.
        - moral_framework: held 0. Target hold. PASS.
        - relational_anchor_status: held 0. Target hold. PASS.
        - capability: held 0. Target hold. PASS.
        - social_tether-antag: locked 0. Target locked. PASS.
        All axes within ±0 of contract (all EXACT). PASS.

    - id: p6-abstraction-dominant
      type: flag
      what: ABSTRACTION-DOMINANT check — s02 grounding percentage borderline
      why: >
        s02: 2 grounding bones in 9 total non-chatter bones = 22.2%, just below the 25% soft floor.
        The flat_id 9 (cost-ledger) and flat_id 12 (lane-stone) are both named physical objects;
        the 22% falls 3 percentage points below threshold. Chapter-wide: 12/36 bones = 33%, well
        above the 25% floor. The s02 borderline is partially structural (s02's bones are
        predominantly physical enumeration acts in the accounting — which are concrete but not
        place-situated in the same sensory-grounding sense as trough / floor / shutter).
        Note: pl-2026-06-05-c19-002 (SOFT, targets /and-stitch Phase 8.5) already carries the
        ABSTRACTION-DOMINANT voice-risk for the chapter. This flag is advisory only; the
        chapter-wide count is clean. Does not block. Disposition needed: carry to /and-stitch
        Phase 8.5 alongside pl-2026-06-05-c19-002.

    - id: p6-register-mannerism
      type: flag
      what: REGISTER-AS-MANNERISM check — chapter-wide VERB+OBJECT pair frequency
      why: >
        Observed recurring VERB+OBJECT pairs across 36 bones:
        - "opens the [X]": flat_id 5 (cost-ledger column), flat_id 18 (outer-ring bottlefly routes),
          flat_id 33 (running-architecture record), flat_id n02 (the sheet). Four instances of "opens."
          Note: flat_id 2 is "opens the sheet" (different object but same verb). The object varies
          (cost-ledger column / bottlefly routes / running-architecture record / sheet) — the verb
          "opens" recurs 4× chapter-wide across different objects, meeting the ≥3 SIGNAL threshold.
        - "closes the [X]": flat_id 23 (cost-ledger column), flat_id 35 (coverage-record). Two instances
          of "closes" — below threshold.
        - "receives the [X]": flat_id 4 (tallow-render room floor receives the sheet), flat_id 8 (column
          receives the contempt-entry), flat_id 26 (ledger-edge receives the stylus), flat_id 22 (Jarvis
          channel receives the compiled-reading). Four instances of "receives" — meets the ≥3 threshold.
        - "the stylus [X]": flat_id 14 (sets the stylus), flat_id 24 (lifts the stylus), flat_id 25
          (stylus meets the ledger-edge), flat_id 26 (ledger-edge receives the stylus). The stylus is
          the prop in 4 consecutive s03 bones — not a verb+object pair repetition per se, but a prop-
          concentration that accompanies the CFR-2 sequence. Structurally motivated (CFR-2 requires
          stylus choreography), not incidental mannerism.

        Assessment: "opens" (4×) and "receives" (4×) are the flagged pairs. "Opens the [X]" serves
        structurally distinct functions in each instance (sheet-reading = request receipt; cost-ledger =
        accounting discipline; bottlefly routes = capability deployment; architecture record = severance
        documentation), but the register-as-mannerism SIGNAL fires on frequency alone. Carry to
        /and-stitch Phase 3/8 for voice-embodiment variety on the repeated verb.

        Both "opens" and "receives" cluster: advisory to /and-stitch, not blocking.

    # --- PHASE 6 AGGREGATE VERDICT ---

    - id: p6-verdict
      type: pass
      what: PHASE 6 SUBSTANCE BONE-GATE overall verdict — PASS
      why: >
        HARD count: 0. No SUBSTANCE-FLAT-<axis>, no HELD-AXIS-NOT-ENACTED, no HELD-AXIS-UNCONTRACTED,
        no EVENT-PRESENCE fault, no CHUNK-TAG-COMPLETENESS fault, no STAKES-AXIS-DOMINANT fault,
        no SENSORY-GROUNDING fault, no EVENT-NOT-CONCRETE fault (pl-2026-06-05-c19-001 RESOLVED),
        no HELD-AXIS-NOT-WITNESSED fault, no STAKES-AXIS-MISSING fault, no OPPOSING-FORCE-MISSING fault,
        no COST-NOT-PAID fault.

        SIGNAL list (disposition needed at /and-stitch):
        - signal-001: ABSTRACTION-DOMINANT (s02 grounding 22.2%, borderline; chapter-wide 33% clean).
          Disposition: carry to /and-stitch Phase 8.5 alongside pl-2026-06-05-c19-002 (already SOFT-
          documented). Low severity; chapter-wide pass.
        - signal-002: REGISTER-AS-MANNERISM ("opens" ×4, "receives" ×4 chapter-wide).
          Disposition: carry to /and-stitch Phase 3/8 for verb-variety during voice-embodiment.
          Not blocking.

        pl-2026-06-05-c19-001 (c19 s04 label-reach concreteness, HARD watch): RESOLVED at Phase 6.
        The parking-lot item resolves here; the bones satisfy the resolution criteria.
```
