audit:
  scope: scene
  target: b01c06s03
  timestamp: 2026-05-31
  phase: 6-revise (substance bone-gate — depth-pass scope)
  context: >
    Scoped to b01c06s03 only. s01 and s02 carry prior PASS verdicts and are not re-gated.
    Three sub-tasks: (A) per-bone Phase 6 substance bone-gate for all 11 s03 bones using
    the final revised sequence per showrunner memory; (B) fold-in (a) — FAULT-FORM re-check
    on new bone @20 `holds the stylus`; (C) fold-in (b) — continuity/reachability confirm.
    Flat_ids in this report use the dispatch-intended numbering (@16-@26) which Phase 7 will
    reassign; in-memory slugs are authoritative.
  findings:

    # ─────────────────────────────────────────────────────────────────────────
    # FOLD-IN (a): FAULT-FORM re-check on new bone @20 `holds the stylus`
    # ─────────────────────────────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        b01c06s03 in-memory bone b01c06s03n11 (dispatch @20), SVO:
          "taylor-hebert-kl-122ac holds the stylus"
        The narrow `holds` license in schemas/bones.schema.md permits `holds` only when:
          (1) The object is a body part of the subject and the action is
              stillness-against-pressure (e.g. `taylor holds the feet`), OR
          (2) The object is a physical object resisting pressure
              (e.g. `the door holds`).
        "The stylus" is neither a body part of the subject nor a physical object
        resisting external pressure. The schema's explicit deny-list example is
        "`taylor holds the ledger`" — faults FAULT-FORM-NON-ACTION-VERB. A stylus
        is directly parallel: a physical writing implement held by the subject, not
        a body part and not pressure-resistant. The "instrument-stillness" framing
        in the dispatch brief is not a licensed category in the schema. Condition
        (1) and (2) are exhaustive.
      why: >
        A FAULT-FORM-NON-ACTION-VERB on the new verdict-pause bone blocks Phase 7
        emission for s03. The bone was added by the dramatist as a missing-transition
        fix (the rise into the seal); without a schema-clean substitute, the
        climax-prerequisite pause the dramatist identified is absent. The downstream
        consequence is twofold: (a) the causal chain "write names → close ledger-board
        → lift form → seal" loses its verdict-pause beat and the rise into the seal
        reads as a step-function rather than a pressure-loaded pause; (b) if the bone
        ships with a FAULT-FORM, the bones file fails its own schema gate and
        /and-facets is not cleared.
      criteria: >
        The verdict-pause bone at @20 must be replaced with a schema-clean SVO that:
        (a) passes the strict holds-license test OR uses a different verb;
        (b) enacts stillness or suspension as a concrete physical act observable
            from outside; (c) carries moral_framework in axes_held with the
            existing rationale ("verdict-pause — accounting's own logic closes here;
            the move fires at the seal, not here"); (d) remains a single-subject,
            no-modifier, no-interiority, no-copula, no-negation, no-conjunction SVO.
        Candidate forms that do not require the holds license (non-exhaustive):
        `taylor-hebert-kl-122ac rests the stylus` (rests is transitive physical;
        subject places object down; observable act), or a body-posture form such as
        `taylor-hebert-kl-122ac stills the hand` (body part — satisfies condition (1)
        if the hand IS the body part, and stillness-against-pressure is the act of
        halting the writing motion against the implicit pull to continue). Fixer
        determines the minimum-change form. Pass-2 must re-run on this bone only.

    # ─────────────────────────────────────────────────────────────────────────
    # BONES FILE SYNC NOTE (not a new fault — carried from write-b01c06-pass2-revise.md)
    # ─────────────────────────────────────────────────────────────────────────

    - id: fault-002
      type: fault
      what: >
        theater/bones/b01-c06.md flat_ids 16–22 still carry the pre-revise SVOs.
        Current flat bones file content (lines 29-35):
          16: "taylor-hebert-kl-122ac opens the accounting ledger"    ← OLD
          17: "taylor-hebert-kl-122ac writes the first arm — names against Sera's protection"  ← OLD
          18: "taylor-hebert-kl-122ac writes the second arm — omission risk against Sera's exposure"  ← OLD
          19: "taylor-hebert-kl-122ac marks the red-keep coverage record"  ← unchanged
          20: "taylor-hebert-kl-122ac holds the stylus"  ← NEW (present in file, but FAULT-FORM per fault-001)
          21: "taylor-hebert-kl-122ac closes the accounting entry"  ← OLD
          22: "taylor-hebert-kl-122ac squares the jarvis-channel form"  ← OLD
        The showrunner memory (source of truth per schemas/bones.schema.md) contains the
        final revised sequence with 11 bones (n01–n11 in s03, including the new n11 at @20).
        The bones file is the flattened serialization that /and-facets and /and-stitch
        consume. write-b01c06-pass2-revise.md fault-001 identified this gap and criteria
        specified the six recast SVOs; the Phase 7 emit also inserts the new @20 bone and
        renumbers @21-@26 accordingly. This fault is the same root gap, now folding in the
        new @20 bone and the renumbering. It is noted separately because (a) fault-001 above
        requires fixer to resolve the @20 form before Phase 7 emits, and (b) fault-002 tracks
        that the bones file sync cannot complete until fault-001 is resolved — the two faults
        must be resolved in dependency order.
      why: >
        /and-facets reads theater/bones/b01-c06.md, not showrunner memory. If the bones
        file is not updated after fault-001 resolution, the downstream pipeline operates on
        the old apparatus-abstraction SVOs and the unresolved @20 FAULT-FORM bone. The
        depth-pass improvement is blocked end-to-end until the file reflects memory.
      criteria: >
        After fault-001 is resolved (the @20 bone recast to a schema-clean form):
        theater/bones/b01-c06.md flat_ids 16–26 must reflect the 11-bone final sequence
        exactly as it appears in showrunner memory after the @20 fix:
          16: (n01) opens the ledger-board
          17: (n02) writes the ward-elder names
          18: (n03) writes the sera-coverage entry
          19: (n04) marks the red-keep coverage record
          20: (n11) <schema-clean verdict-pause SVO — per fault-001 fixer resolution>
          21: (n05) closes the ledger-board
          22: (n10) lifts the jarvis-channel form
          23: (n06) seals the jarvis-channel form
          24: (n07) the courier takes the jarvis-channel form
          25: (n08) opens the ward-coverage notes
          26: (n09) closes the ward-coverage notes
        No other lines in the bones file may change. Flat_ids 1–15 are unaffected.

    # ─────────────────────────────────────────────────────────────────────────
    # PER-BONE PHASE 6 SUBSTANCE BONE-GATE — s03 (11 bones)
    # Evaluated against showrunner memory; @20 evaluated subject to fault-001
    # ─────────────────────────────────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: >
        Per-bone bonefide check — moving bones @23 and @25.

        @23 "taylor-hebert-kl-122ac seals the jarvis-channel form"
        shape: moving; axis_moves: moral_framework −1.0; cost_ledger_anchor: cl-d06
        Bonefide: sealing the jarvis-channel form IS the named-person delivery; the
        physical act of sealing transmits the four-name list into the arrangement's
        downstream. The Δ (moral_framework −1.0) follows causally from the physical
        act of completing the delivery. cl-d06 cost direction is down; schema:
        cl-d06 gain="relational_anchor_status +2" / cost="moral_framework -1";
        cost direction matches the declared axis_moves direction (down). BONEFIDE.

        @25 "taylor-hebert-kl-122ac opens the ward-coverage notes"
        shape: moving; axis_moves: moral_legibility_to_self +1.0
        Bonefide: opening the ward-coverage notes after the send exposes the contrast
        record — four names sent vs. the blank contact-source field where Wren's name
        is not. The physical act of opening the notes causes the legibility increment
        by making the contrast visible in the record. The +1.0 magnitude (realizing the
        +0.5 scene-contract target at bone-floor; prior signal-001 disposition
        accept-with-rationale) follows from the SVO. BONEFIDE.
      why: null

    - id: pass-002
      type: pass
      what: >
        Per-bone held-bone discipline-enactment check — held bones @16, @17, @18,
        @19, @21, @22, @24, @26.

        @16 "opens the ledger-board" — axes_held: moral_framework.
        Rationale: "accounting has not yet arrived at delivery; ledger-board opens on
        the cost-side names; moral_framework holds at current crack-level pending
        completion." Opening the ledger-board as a physical preparatory act enacts the
        framework-operative discipline: the accounting has not completed; the send has
        not fired; the prohibition is not yet a closed ledger entry. Discipline
        rationale names the opposing pressure (pending completion). ENACTED.

        @17 "writes the ward-elder names" — axes_held: moral_framework,
        relational_anchor_status.
        Rationale: moral_framework — "writing the ward-elder names is the cost-side
        write; framework holds — delivery not completed in this bone; writing the names
        is the mechanism that makes the breach legible." relational_anchor_status —
        "writing the ward-elder names does not add further weight to the anchor; the
        contrast between the four names and Wren's absent name is structurally present
        but does not move the axis." Both rationales name what the bone enacts (the
        cost-side record) and why the axis holds (delivery incomplete; contrast present
        without requiring a second Δ). ENACTED.

        @18 "writes the sera-coverage entry" — axes_held: moral_framework,
        political_register-prot.
        Rationale: moral_framework — "the sera-coverage entry is the exposure-side
        write; it runs without embellishment; the accounting is honest and not yet
        complete; framework holds pending the close." political_register-prot — "Sera
        is the protect-target; the sera-coverage entry carries no court-tier content
        that activates the resentment register; political_register-prot holds."
        Both rationales name the discipline. ENACTED.

        @19 "marks the red-keep coverage record" — axes_held: capability,
        relational_anchor_status.
        Rationale: capability — "the Red Keep coverage is the existing capability
        architecture; marking the record is coverage-recall, not new deployment."
        relational_anchor_status — "Sera's presence in the coverage record is the
        protection architecture's object; the relational anchor holds at its post-s01
        rank." Both rationales name the discipline. ENACTED.

        @21 "closes the ledger-board" — axes_held: moral_framework.
        Rationale: "the accounting runs as stated; both writes have landed; the move
        fires at the seal (n06), not at the ledger-board close; the ledger-board
        closing IS the moment the breach becomes inevitable." The closing enacts the
        final accounting-complete beat before the send; the discipline (framework holds
        at this bone) names what holds and why (the move is fire-on-seal). ENACTED.

        @22 "lifts the jarvis-channel form" — axes_held: moral_framework.
        Rationale: "deliberation complete; the accounting's verdict has converted to
        act; the framework holds at this bone — the move fires on the seal at n06, not
        here; lifting the form is the close→act hinge that makes the causation of the
        breach visible (write names → close ledger-board → lift form → seal)."
        The close→act hinge enacts the post-deliberation transitional act; discipline
        rationale names what the bone enacts. ENACTED.

        @24 "the courier takes the jarvis-channel form" — axes_held: moral_framework,
        social_tether-prot-rise.
        Rationale: moral_framework — "post-move hold — moral_framework moved at @23;
        the courier taking the form is the physical completion of the send; the axis
        holds at its new rank." social_tether-prot-rise — "the delivery is within the
        existing tether structure; no new tether formation event; tether holds." Both
        rationales name the post-move hold discipline. ENACTED.

        @26 "closes the ward-coverage notes" — axes_held: moral_legibility_to_self,
        position-prot-rise.
        Rationale: moral_legibility_to_self — "post-move hold — moral_legibility moved
        at @25; closing the notes is the physical completion of the contrast-moment;
        the crack deepens from precision not suppression." position-prot-rise —
        "the delivery is within the existing arrangement; no new formalization event;
        position holds." Both rationales name the post-move hold discipline. ENACTED.
      why: null

    - id: pass-003
      type: pass
      what: >
        Held-axis-contracted check — all held bones (Phase 6 HELD-AXIS-UNCONTRACTED).
        For each held axis at bone level, the axis must appear in s03's scene-level
        axes_held[] or axes_in_motion[] (stakes_axis resolution).

        s03 scene-contract:
          axes_in_motion: moral_framework −1.0, moral_legibility_to_self +0.5→+1.0
          axes_held: relational_anchor_status, capability, position-prot-rise,
                     political_register-prot, social_tether-prot-rise
          stakes_axis: moral_framework (in axes_in_motion — resolves via stakes_axis
                       union check)

        Bone-level held axes by bone:
          @16: moral_framework — in axes_in_motion (stakes_axis). CONTRACTED.
          @17: moral_framework (stakes_axis), relational_anchor_status (held). CONTRACTED.
          @18: moral_framework (stakes_axis), political_register-prot (held). CONTRACTED.
          @19: capability (held), relational_anchor_status (held). CONTRACTED.
          @21: moral_framework (stakes_axis). CONTRACTED.
          @22: moral_framework (stakes_axis). CONTRACTED.
          @24: moral_framework (stakes_axis), social_tether-prot-rise (held). CONTRACTED.
          @26: moral_legibility_to_self (in axes_in_motion), position-prot-rise (held).
               CONTRACTED.

        Zero HELD-AXIS-UNCONTRACTED findings.
      why: null

    - id: pass-004
      type: pass
      what: >
        Per-axis aggregate Δ delivery within ±1 of scene contract.

        moral_framework: scene contract −1.0; @23 delivers −1.0. Delta = 0.0. EXACT.
        moral_legibility_to_self: scene contract +0.5 (target); @25 delivers +1.0
          (bone-floor magnitude 1.0 forces minimum bone magnitude against fractional
          scene target). Deviation = +0.5. Within ±1 tolerance. Prior signal-001
          disposition: accept-with-rationale (multi-scene distribution artifact;
          DEC-0030 bone-floor). No new fault; disposition carries forward.

        No AXIS-DELTA-MISMATCH.
      why: null

    - id: pass-005
      type: pass
      what: >
        Stakes-axis-dominant check. stakes_axis = moral_framework (in axes_in_motion).
        Delivered magnitudes: moral_framework = 1.0; moral_legibility_to_self = 1.0.
        Tie: both axes deliver magnitude 1.0. Prior signal-002 disposition:
        accept-with-rationale (co-equal delivery is a bone-floor artifact; at contract
        level mf −1.0 > mls +0.5; the tie exists only because bone-floor forces
        minimum 1.0 on the +0.5 mls target). No new fault; prior disposition
        accept-with-rationale carries forward. STAKES-AXIS-NOT-DOMINANT does not
        re-fire as a new fault.
      why: null

    - id: pass-006
      type: pass
      what: >
        Held-axes-witnessed check. For each s03 scene-level axes_held[] entry, ≥1
        bone must carry that axis in its bone-level axes_held[].

        relational_anchor_status: @17 (axes_held: relational_anchor_status),
          @19 (axes_held: relational_anchor_status). WITNESSED.
        capability: @19 (axes_held: capability). WITNESSED.
        position-prot-rise: @26 (axes_held: position-prot-rise). WITNESSED.
        political_register-prot: @18 (axes_held: political_register-prot). WITNESSED.
        social_tether-prot-rise: @24 (axes_held: social_tether-prot-rise). WITNESSED.

        All 5 scene-level held axes have ≥1 bone-level witness. Zero HELD-AXIS-NOT-WITNESSED.
        (Note: the prior Phase 6 fault-001 on s01's political_register-prot was a
        DIFFERENT scene; s03 had no such finding in the original gate and has none here.)
      why: null

    - id: pass-007
      type: pass
      what: >
        Opposing-force-visible check. scene_conflict.opposing_force: "the accounting's
        HONESTY as the breach mechanism — the ledger runs correctly and arrives at
        delivery; the opposing force is the accounting's own correct output."

        Multiple bones enact this: @17 (writes the ward-elder names) + @18 (writes the
        sera-coverage entry) together enact the two-arm accounting arriving complete and
        correct; @21 (closes the ledger-board) enacts the accounting concluding; @23
        (seals the jarvis-channel form) enacts the delivery as the output of the
        correctly-run accounting. The opposing force is not an external pressure but the
        accounting's own output — this is the contracted form (from scene_contract) and
        the bones are structured so the discipline-accounting IS the breach mechanism.
        OPPOSING-FORCE-VISIBLE.
      why: null

    - id: pass-008
      type: pass
      what: >
        Cost-ledger check. cl-d06: gain="relational_anchor_status +2" /
        cost="moral_framework -1". The cost side of cl-d06 must be paid by a bone in
        this chapter with cost_ledger_anchor: cl-d06 and direction: down.
        @23 (seals the jarvis-channel form): cost_ledger_anchor: cl-d06; axis_moves
        direction: down (moral_framework −1.0). Cost direction matches. The gain side
        of cl-d06 was already paid by s01 @4 (relational_anchor_status +1.0; cost_ledger
        cl-d06). The cost side settles here at @23. COST-PAID.
      why: null

    - id: pass-009
      type: pass
      what: >
        Event-map coverage check. s03 event_map entries per showrunner memory:

        (a) "the four-name accounting / cost side" → covered by @17 (writes the
            ward-elder names). COVERED.
        (b) "the Sera-protection weighing / exposure side" → covered by @18 (writes
            the sera-coverage entry), @19 (marks the red-keep coverage record). COVERED.
        (c) "the accounting concluding" → covered by @20 (the verdict-pause, subject
            to fault-001 form fix) + @21 (closes the ledger-board). The verdict-pause
            bone at @20 participates in this coverage regardless of its form issue
            (the form fault does not negate the event-map coverage; it blocks emission
            separately). COVERED.
        (d) "the SEND" → covered by @23 (seals the jarvis-channel form) + @24
            (the courier takes the jarvis-channel form). COVERED.
        (e) "the omission-contrast / Wren's name not written" → covered by @25
            (opens the ward-coverage notes) + @26 (closes the ward-coverage notes).
            The contrast is enacted when Taylor opens the notes after the send — the
            blank field where Wren's name is not present is the event. COVERED.

        All 5 event_map entries covered. Central event (the SEND, @23) covered.
        protagonist_force (the accounting discipline — write, close, lift, seal before
        acting) covered by @16/@17/@18/@21/@22. Zero EVENT-UNCOVERED.
      why: null

    - id: pass-010
      type: pass
      what: >
        EVENT-NOT-CONCRETE check (URI-WRITE-EVENT-CONCRETENESS — spine legibility).
        Central event: the SEND at @23 "seals the jarvis-channel form."
        The SVO is a concrete actor-verb-object physical act: subject (taylor), verb
        (seals — a transitive physical action, wax or closure mechanism applied to
        the form), object (the jarvis-channel form — named physical prop). The event
        does NOT reach the bone through the apparatus (compare the failing form:
        "the feed flags the contact" — apparatus-mediated). The sealing IS the delivery
        act. PASS on central-event-concreteness.

        The de-abstracted accounting bones @16–@22 also pass this check individually:
        "opens the ledger-board" — concrete; "writes the ward-elder names" — concrete
        inscription; "writes the sera-coverage entry" — concrete inscription; "marks
        the red-keep coverage record" — concrete annotation act; "closes the
        ledger-board" — concrete; "lifts the jarvis-channel form" — concrete force
        application. All pass EVENT-NOT-CONCRETE. The de-abstraction confirmed effective
        (PASS more strongly than the prior apparatus-abstraction emit, as anticipated).
      why: null

    - id: pass-011
      type: pass
      what: >
        ABSTRACTION-DOMINANCE check (SIGNAL — grounding-class bones < 25% of
        non-chatter bones).

        s03 bone count: 11 (all held or moving; zero chatter). Non-chatter count: 11.
        Threshold: ceil(0.25 × 11) = ceil(2.75) = 3 grounding-class bones required.

        Grounding-class bones (concrete, place-situated physical actions, naming a
        physical object/surface/particular of the scene's location):
          @16 opens the ledger-board — physical record-substrate; place-situated (at
              the accounting surface). GROUNDING.
          @17 writes the ward-elder names — physical inscription on a record. GROUNDING.
          @18 writes the sera-coverage entry — physical inscription. GROUNDING.
          @19 marks the red-keep coverage record — physical annotation. GROUNDING.
          @21 closes the ledger-board — physical record closure. GROUNDING.
          @22 lifts the jarvis-channel form — physical force application. GROUNDING.
          @23 seals the jarvis-channel form — physical sealing. GROUNDING.
          @24 the courier takes the jarvis-channel form — physical transfer. GROUNDING.
          @25 opens the ward-coverage notes — physical record access. GROUNDING.
          @26 closes the ward-coverage notes — physical record closure. GROUNDING.
          @20 (verdict-pause bone, subject to fault-001) — form-dependent; if resolved
              to a physical stillness act (e.g. rests the stylus), grounding. If resolved
              to a body-posture form (e.g. stills the hand), grounding.

        Conservative count excluding @20: 10/11 = 91% grounding-class bones.
        Threshold: 3 grounding-class bones. Delivered: ≥10. ABSTRACTION-DOMINANCE does
        not fire. The de-abstraction pass has reversed the prior BONES-AIRLESS-RISK
        advisory at the s03 accounting-middle level.
      why: null

    - id: pass-012
      type: pass
      what: >
        SENSORY-GROUNDING check (HARD). Scene must contain ≥1 grounding bone (a
        concrete, place-situated physical action). Per pass-011 analysis: @16 through
        @26 are predominantly physical record-manipulation acts. ≥1 grounding bone
        present. SENSORY-GROUNDING PASS.

        (Note: the sensory facet's job is to add sensory-modality texture around these
        physical bones; the bone layer supplies the substrate. The voice-fixable watch
        items at @20 and @21 from context_followability carry forward to /and-stitch
        Phase 4 voice-embodiment but do not affect the bone-gate sensory-grounding
        check.)
      why: null

    - id: pass-013
      type: pass
      what: >
        Underdelivery-rationale check. No axes_in_motion entry is below 50% of target.
        moral_framework: target 1.0, delivered 1.0 = 100%. No underdelivery.
        moral_legibility_to_self: target 0.5, delivered 1.0 (bone-floor artifact) =
        200% of target — overdelivery, not underdelivery; covered by prior signal-001
        accept-with-rationale. Zero AXIS-UNDERDELIVERED.
      why: null

    # ─────────────────────────────────────────────────────────────────────────
    # PER-CHAPTER (REGISTER-AS-MANNERISM CHECK)
    # ─────────────────────────────────────────────────────────────────────────

    - id: pass-014
      type: pass
      what: >
        REGISTER-AS-MANNERISM check (URI-WRITE-REGISTER-MANNERISM — SIGNAL if any
        VERB OBJECT pair appears ≥3 times across the chapter's full post-trim bone
        set). Check focused on the revised s03 verb-object pairs and specifically
        on the new `holds the stylus` bone (fault-001) and the `opens`/`closes`/
        `writes` pairs.

        Full chapter post-revise verb-object inventory (relevant pairs):
          "opens the coverage-notes entry" (s01 flat 6): ×1
          "opens the jarvis-channel message" (s02 flat 11): ×1
          "opens the ledger-board" (s03 @16): ×1
          "opens the ward-coverage notes" (s03 @25): ×1
          → "opens <X>": 4 occurrences but 4 DISTINCT objects. No mannerism.

          "closes the coverage-notes entry" (s01 flat 9): ×1
          "closes the ledger-board" (s03 @21): ×1
          "closes the ward-coverage notes" (s03 @26): ×1
          → "closes <X>": 3 occurrences, 3 DISTINCT objects. No mannerism (the check
          is per VERB OBJECT pair, not per VERB alone).

          "writes the ward-elder names" (s03 @17): ×1
          "writes the sera-coverage entry" (s03 @18): ×1
          → "writes <X>": 2 occurrences, 2 distinct objects. No mannerism.

          "holds the stylus" (s03 @20, subject to fault-001): ×1 — only occurrence
          of "holds <non-body-part>" in the chapter. No mannerism concern independent
          of the form fault. (b01c01 has "holds the feet" but that is a different
          chapter; mannerism check runs chapter-scoped.)

        Zero REGISTER-AS-MANNERISM findings.
      why: null

    # ─────────────────────────────────────────────────────────────────────────
    # FOLD-IN (b): CONTINUITY / REACHABILITY CONFIRM
    # ─────────────────────────────────────────────────────────────────────────

    - id: pass-015
      type: pass
      what: >
        Chapter goal reachability. Goal: "Show the audience the first named-person
        delivery and the accounting that precedes it, so the rationalize-each-trade
        pattern is legible — and show Wren's omission from the deliverable as the
        un-priced move it is."

        Both elements survive in the revised bone set:
        (1) Named-person delivery + accounting: @16–@23 carry the full accounting
            arc (ledger-board open → names written → coverage written → record marked
            → verdict-pause → close → lift → seal). Central event delivered by @23.
        (2) Wren's omission: @25–@26 (opens/closes the ward-coverage notes) carry
            the omission-contrast moment. The blank field is the event; the contrast
            between the four-name list sent and Wren's name not present is legible
            in the record. Goal REACHABLE.
      why: null

    - id: pass-016
      type: pass
      what: >
        Physical plausibility of "the stylus" on set. Taylor is writing on the
        ledger-board (a physical record substrate) and filling the jarvis-channel form
        (a physical form). A stylus — a writing implement — is physically required to
        write on a ledger-board or fill a form with ink. The prop is plausible on set
        given the scene's established physical actions (@17 writes names, @18 writes
        entry). No FAULT-PHYSICAL.

        Note: physical plausibility of the prop does not resolve the FAULT-FORM-NON-
        ACTION-VERB on "holds the stylus" (fault-001) — that is a schema-form fault,
        not a physical-plausibility fault.
      why: null

    - id: pass-017
      type: pass
      what: >
        Unresolved reference check. No new proper nouns or entity references introduced
        by the revised bones:
          "the ledger-board" — established by the de-abstraction recast; compound-noun
            prop convention (pass-2-revise pass-003 confirmed clean).
          "the ward-elder names" — the four ward-elder names are the content of the list;
            the names themselves are not referenced as characters in the bones file; the
            object is the aggregate data ("the names"), not named actors. No new slug
            needed.
          "the sera-coverage entry" — "Sera" resolves to sera-hightower-kl-122ac
            (pass-2-revise pass-006 confirmed); compound-noun record-object. No new
            slug needed.
          "the stylus" — physical prop; no slug required for an unnamed implement.
            (If fixer recasts to "rests the stylus" or similar, same applies.)
        Zero FAULT-REFERENCE introduced by revised bones.
      why: null

    - id: pass-018
      type: pass
      what: >
        Handoff_out consistency. The revised bone sequence does not alter the
        substantive content of the handoff_out:
          - moral_framework: moves −1.0 (delivered by @23 seal). handoff_out records
            "Taylor: moral_framework rank 0 (rationalized breach on record)". Consistent.
          - relational_anchor_status: moved in s01 (unchanged); handoff_out records
            "Wren: first spoken exchange; omitted from deliverable; anchor rank 3".
            Consistent; s03 adds the omission-contrast visibility (@25/@26) which
            deepens the readable legibility without requiring a second Δ. Consistent.
          - moral_legibility_to_self: +1.0 delivered (bone-floor realization of +0.5
            target; prior signal-001 accept-with-rationale). handoff_out records
            "moral_legibility crack: deeper; accounting is honest and that honesty is
            visible." Consistent.
          - No new open threads introduced by the revised bones.
          - No actor exits or location changes introduced.
        Handoff_out UNAFFECTED by the depth-pass revision.
      why: null

  summary: >
    TWO FAULTS. The depth-pass de-abstraction of the six s03 bones (@16-@18, @21-@22)
    passes all Phase 6 checks: bonefide CLEAN on @23/@25; held-bone discipline
    ENACTED on all eight held bones; all five held axes WITNESSED; opposing-force
    VISIBLE; cost-ledger cl-d06 PAID at @23; event-map COVERED 5/5; central-event
    CONCRETE; abstraction-dominance 91% grounding (above floor); sensory-grounding
    PASS; per-axis Δ WITHIN TOLERANCE; stakes-axis tie carries prior signal-002
    accept-with-rationale; register-as-mannerism CLEAN; chapter goal REACHABLE;
    continuity UNAFFECTED.

    The two faults are:
      fault-001 (HARD): @20 "holds the stylus" fails the narrow holds license.
        "The stylus" is neither a body part of the subject nor an object resisting
        external pressure — both required conditions for the holds license in
        schemas/bones.schema.md. The deny-list example "`taylor holds the ledger`"
        is directly parallel. Fixer must recast to a schema-clean verdict-pause SVO
        before Phase 7 emit. Pass-2 must re-run on this bone only after the recast.
      fault-002 (HARD): bones file theater/bones/b01-c06.md has not been updated to
        reflect the revised in-memory sequence. This fault is blocked on fault-001
        resolution; Phase 7 emit resolves both atomically once fault-001 is fixed.

    Gate verdict: HARD-BLOCKED on fault-001 and fault-002.
    All other s03 checks: PASS. s01 and s02 prior PASS verdicts unchanged.
