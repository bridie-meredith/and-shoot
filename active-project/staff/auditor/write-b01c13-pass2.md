```yaml
audit:
  scope: chapter
  target: b01c13
  timestamp: 2026-06-03
  findings:

    - id: fault-001
      type: fault
      what: "b01c13s01n04 — SVO: the supplier's-son carries the wrapped-crates"
      why: >
        "carries" is on the schema's non-action-verb deny-list (sustained-carrying: carries,
        carried, carrying, bears, bore). A stative carrying state is not a bone. The discrete
        act that initiated or terminated the carrying state is. Downstream renderer will find
        no observable action at this beat.
      criteria: >
        The bone must record a discrete observable physical act — the initiation or termination
        of the carrying (e.g., the son picks up the crates, or loads the crates) rather than
        the sustained state of carrying them.

    - id: fault-002
      type: fault
      what: "b01c13s01n06 — SVO: taylor-hebert-kl-122ac holds the blowfly"
      why: >
        "holds" fails the narrow holds-license. License covers: (1) object is a body part of
        the subject in stillness-against-pressure, or (2) object is a physical object resisting
        external pressure. A blowfly maintained in position by Taylor's insect-control is
        neither. This is sustained-state control; not licensed holds.
      criteria: >
        The bone must record a concrete observable act — the specific physical action Taylor
        performs to maintain the fly's position. A recast form naming the observable action is
        required; unlicensed holds is not the mechanism.

    - id: fault-003
      type: fault
      what: "b01c13s02n07 — SVO: taylor-hebert-kl-122ac holds the fly"
      why: >
        Same holds-license violation as fault-002. Second instance across the chapter's
        fly-observation beats.
      criteria: Same as fault-002.

    - id: fault-004
      type: fault
      what: "b01c13s02n09 — SVO: taylor-hebert-kl-122ac holds the fly"
      why: >
        Same holds-license violation as fault-002. Third instance of the unlicensed holds form.
      criteria: Same as fault-002.

    - id: fault-005
      type: fault
      what: "b01c13s02n08 — SVO: aldric places his hands on the table"
      why: >
        "on the table" is a prepositional phrase of place/surface — explicitly banned per the
        modifier rule. PP padding of direction/place/surface must be eliminated; a transitive
        verb taking the surface as direct object is required. "his" is also a possessive
        modifier on the object noun.
      criteria: >
        The bone must remove the PP "on the table." Restructure to a transitive verb form that
        absorbs the surface as direct object, or split if the hands and table surface are
        separate beat elements. The object must be an unmodified noun.

    - id: fault-006
      type: fault
      what: "b01c13s03n02 — SVO: the accounting holds the household-agent-image"
      why: >
        Three compound violations. (1) Subject "the accounting" is an interior cognitive
        process, not a named entity, actor slug, prop slug, or unnamed environment element —
        interiority as subject. (2) "holds" fails the narrow license; the object is not a
        body part of the subject nor a physical object resisting external pressure. (3) Object
        "the household-agent-image" is an abstract mental image-noun — abstraction-as-object
        is interiority by schema rule. A thought-figure expressed as subject-verb-object is
        not a bone.
      criteria: >
        The beat must be recast so that the subject is a named physical entity, the verb is a
        concrete observable action, and the object is a non-abstract noun. If this beat is
        purely interior (Taylor running her mental accounting), it does not belong as a bone —
        it belongs in a facet that cites the surrounding physical bones.

    - id: fault-007
      type: fault
      what: "b01c13s03n03 — SVO: the accounting holds the magistrate-document-image"
      why: >
        Same compound violations as fault-006. Subject is an interior process; holds is
        unlicensed; object is an abstract mental image.
      criteria: Same as fault-006.

    - id: fault-008
      type: fault
      what: "b01c13s03n04 — SVO: the accounting holds the aldric-hands-image"
      why: >
        Same compound violations as fault-006. Subject is an interior process; holds is
        unlicensed; object is an abstract mental image.
      criteria: Same as fault-006.

    - id: fault-009
      type: fault
      what: >
        b01c13s03n05 — SVO: taylor-hebert-kl-122ac names the contempt
        CENTRAL-EVENT BONE for scene s03 (political_register-prot +1, magnitude 1)
      why: >
        Object "the contempt" is an abstract noun. Schema rule: "Abstraction-as-object is
        INTERIORITY. A physical verb whose object is an abstract noun is a thought-figure,
        not an event." Even if "names" is treated as a speech-act verb, the object fails the
        concreteness test. This is the most load-bearing bone in the chapter — the
        articulate-contempt threshold crossing — and it carries no physical event for a
        renderer to anchor. EVENT-NOT-CONCRETE on the central-event bone is HARD.
      criteria: >
        The central-event bone must name a concrete physical act with a non-abstract direct
        object. If the naming event is externalized as a speech-act (Taylor says the word
        aloud), the bone should record that speech act in a form with a physical/concrete
        object. If it remains a solo interior event, the bone must find the physical form of
        the act — a body-anchored gesture, concrete verbal output, physical stop or breath —
        not the cognitive classification itself.

    - id: fault-010
      type: fault
      what: "b01c13s04n05 — SVO: taylor-hebert-kl-122ac holds the route"
      why: >
        "holds" fails the narrow license. The route is not a body part of Taylor nor a
        physical object resisting external pressure. "Holds the route" is a figure of speech
        for continues-on-the-route — a sustained locomotion state, not a licensed holds use.
      criteria: >
        The bone must record a concrete observable act. If the intent is Taylor continuing to
        walk the circuit, the bone must name that physical act directly (a transitive motion
        verb taking the route or lane as direct object). The CARRY_TO_WRITE rationale for
        physical non-movement toward the ledger is sound; holds is not the mechanism.

    - id: fault-011
      type: fault
      what: "b01c13s04n08 — SVO: halvard stands the water-trough"
      why: >
        "stands" is on the non-action-verb deny-list when describing stative position rather
        than the discrete act of rising. "halvard stands [at] the water-trough" is position
        description — Halvard is still at the trough after Taylor departs. The exception is
        the discrete act of standing up from sitting; this bone is not that. Stative
        position-naming is not a bone.
      criteria: >
        The bone must record Halvard's concrete action at the trough after Taylor departs —
        the physical act that makes his continued presence visible and observable. The static
        position state is not the act. A different verb that names the observable beat is
        required.

    - id: fault-012
      type: fault
      what: >
        b01c13s04n03 — dialogue-anchor bone: halvard speaks to taylor-hebert-kl-122ac;
        shape: held; axis_moves: []
      why: >
        Schema (bones.schema.md, Dialogue-anchor bones section): canonical speech form
        requires substance_delta with ≥1 communication-class axis movement (community /
        knowledge / reputation / trust). This bone has shape: held and zero axis_moves.
        Speech bones that move no axes are malformed per the substance bone-gate. The
        schema is unambiguous: "speech bones whose substance_delta lists only physical-action
        axes are malformed" — and this bone moves no axes at all.
      criteria: >
        The bone must declare at least one axis_moves entry for a communication-class axis
        (or the closest project analog) and shape must be moving. If no communication-class
        axis in this project's state_axes covers the communicative dimension of Halvard's
        speech, fixer must escalate to screen-writer — the bone cannot remain shape: held
        with no axis movement.

    - id: fault-013
      type: fault
      what: >
        b01c13s04n04 — dialogue-anchor bone: taylor-hebert-kl-122ac speaks to halvard;
        shape: held; axis_moves: []
      why: >
        Same violation as fault-012. Taylor's counter-argument is the scene's substantive
        communicative event and it moves no axes. Malformed per the substance bone-gate.
      criteria: Same as fault-012.

    - id: fault-014
      type: fault
      what: >
        b01c13s04n06 — dialogue-anchor bone: halvard speaks to taylor-hebert-kl-122ac;
        shape: held; axis_moves: []
      why: >
        Same violation as fault-012. Third speech bone with zero axis movement in the same
        scene.
      criteria: Same as fault-012.

    - id: flag-001
      type: flag
      what: "b01c13s01n07 — SVO: the household-agent leans the trestle-table"
      why: >
        "leans the trestle-table" is grammatically strained as a transitive. "Leans"
        transitively in English means tips or tilts the named object; the intended meaning
        (agent leans forward over the table, post-coercion posture) would use a PP that the
        schema bans. The PP-suppression technique is schema-conformant in principle, but this
        specific verb-object pairing risks renderer misreading: the agent physically tilting
        the table vs. the agent adopting a forward-lean posture over it are different images.
        Not a FAULT since the PP-suppression approach follows the schema's instruction, but
        the ambiguity may produce the wrong beat in prose.
      criteria: null

    - id: flag-002
      type: flag
      what: "b01c13s02n06 — SVO: the magistrate glances the d06-document (CENTRAL-EVENT BONE)"
      why: >
        "glances" is a visual perception verb (directional gaze). The schema's explicit
        deny-list names sees, watches, notices; glances is not listed by name but is in the
        same semantic category. An observer can see a glance as a head/eye movement, giving
        it marginal physical dimension, but its primary semantic is perceptual observation.
        This is not a FAULT since glances is not on the explicit deny-list; however the bone
        risks rendering as a perception beat rather than a physical action beat, particularly
        as the central-event bone for political_register-world where concreteness is required.
      criteria: null
```

---

## Per-bone verdict table

| bone | verdict | offending token(s) |
|------|---------|-------------------|
| b01c13s01n01 | CORRECT | — |
| b01c13s01n02 | CORRECT | — |
| b01c13s01n03 | CORRECT | — |
| b01c13s01n04 | FAULT-FORM-NON-ACTION-VERB | `carries` |
| b01c13s01n05 | CORRECT | — |
| b01c13s01n06 | FAULT-FORM-NON-ACTION-VERB | `holds` (unlicensed: fly is not body part of subject nor physical object resisting pressure) |
| b01c13s01n07 | FLAG | `leans the trestle-table` (transitive ambiguity; not a FAULT) |
| b01c13s01n08 | CORRECT | — |
| b01c13s01n09 | CORRECT | — |
| b01c13s02n01 | CORRECT | — |
| b01c13s02n02 | CORRECT | — |
| b01c13s02n03 | CORRECT | — |
| b01c13s02n04 | CORRECT | — |
| b01c13s02n05 | CORRECT | — |
| b01c13s02n06 | FLAG | `glances` (perception-verb borderline; not on explicit deny-list; advisory only) |
| b01c13s02n07 | FAULT-FORM-NON-ACTION-VERB | `holds` (unlicensed) |
| b01c13s02n08 | FAULT-FORM-MODIFIER | `on the table` (PP of surface); `his` (possessive modifier on object) |
| b01c13s02n09 | FAULT-FORM-NON-ACTION-VERB | `holds` (unlicensed) |
| b01c13s03n01 | CORRECT | — |
| b01c13s03n02 | FAULT-FORM-INTERIORITY | `the accounting` (interiority as subject); `holds` (unlicensed); `the household-agent-image` (abstract object) |
| b01c13s03n03 | FAULT-FORM-INTERIORITY | `the accounting` (interiority as subject); `holds` (unlicensed); `the magistrate-document-image` (abstract object) |
| b01c13s03n04 | FAULT-FORM-INTERIORITY | `the accounting` (interiority as subject); `holds` (unlicensed); `the aldric-hands-image` (abstract object) |
| b01c13s03n05 | FAULT-FORM-INTERIORITY | `the contempt` (abstract object) — CENTRAL-EVENT BONE |
| b01c13s03n06 | CORRECT | — |
| b01c13s03n07 | CORRECT | — |
| b01c13s04n01 | CORRECT | — |
| b01c13s04n02 | CORRECT | — |
| b01c13s04n03 | FAULT-BONE-DELTA-MALFORMED | speech bone; shape: held; axis_moves: [] (communication-class axis required) |
| b01c13s04n04 | FAULT-BONE-DELTA-MALFORMED | speech bone; shape: held; axis_moves: [] (communication-class axis required) |
| b01c13s04n05 | FAULT-FORM-NON-ACTION-VERB | `holds` (unlicensed: route is not body part of subject nor physical object resisting pressure) |
| b01c13s04n06 | FAULT-BONE-DELTA-MALFORMED | speech bone; shape: held; axis_moves: [] (communication-class axis required) |
| b01c13s04n07 | CORRECT | — |
| b01c13s04n08 | FAULT-FORM-NON-ACTION-VERB | `stands` (stative position-naming, not discrete act of rising) |

---

## HARD fault list

All 14 faults below are HARD and block.

| id | bone | class |
|----|------|-------|
| fault-001 | b01c13s01n04 | FAULT-FORM-NON-ACTION-VERB |
| fault-002 | b01c13s01n06 | FAULT-FORM-NON-ACTION-VERB |
| fault-003 | b01c13s02n07 | FAULT-FORM-NON-ACTION-VERB |
| fault-004 | b01c13s02n09 | FAULT-FORM-NON-ACTION-VERB |
| fault-005 | b01c13s02n08 | FAULT-FORM-MODIFIER |
| fault-006 | b01c13s03n02 | FAULT-FORM-INTERIORITY |
| fault-007 | b01c13s03n03 | FAULT-FORM-INTERIORITY |
| fault-008 | b01c13s03n04 | FAULT-FORM-INTERIORITY |
| fault-009 | b01c13s03n05 | FAULT-FORM-INTERIORITY (CENTRAL-EVENT BONE) |
| fault-010 | b01c13s04n05 | FAULT-FORM-NON-ACTION-VERB |
| fault-011 | b01c13s04n08 | FAULT-FORM-NON-ACTION-VERB |
| fault-012 | b01c13s04n03 | FAULT-BONE-DELTA-MALFORMED |
| fault-013 | b01c13s04n04 | FAULT-BONE-DELTA-MALFORMED |
| fault-014 | b01c13s04n06 | FAULT-BONE-DELTA-MALFORMED |

---

## Clean checks (no findings)

- Axis slugs: all six axis slugs used in bones are in the series state_axes list. PASS.
- Cost ledger anchors: all 33 bones carry cost_ledger_anchor: null; no orphan references. PASS.
- Aggregate delta — s01: political_register-prot +1 bone-Δ against scene target +0.5. Within ±1 convention. PASS.
- Aggregate delta — s02: political_register-world +1 and political_register-prot +1 against scene targets +0.5 each. Within ±1 convention. PASS.
- Aggregate delta — s03: political_register-prot +1 against scene target +0.5. PASS.
- Aggregate delta — s04: zero bone-Δ against declared axes_in_motion: []. PASS.
- Chapter aggregate: political_register-prot +3 bone-Δ (s01+s02+s03) maps to +1.5 fractional. Matches chapter target. PASS.
- Chapter aggregate: political_register-world +1 bone-Δ (s02) maps to +0.5 fractional. Matches chapter target. PASS.
- Constraint — cond-earth-bet-noun-fence: no Earth-Bet proper nouns in any bone. PASS.
- Constraint — cond-kl-geography-122ac: all locations (upper Hook provisioning store, chandler's back-room in fringe district at Hook/ward boundary, evening lane, lower-Hook water-trough) consistent with Hook/Flea Bottom geography. PASS.
- Constraint — cond-kl-social-physics-122ac: copper-penny provisioning dispute and rented-room magistrate proceeding consistent with ward-level commerce and informal justice. PASS.
- Constraint — cond-westerosi-magic-dormant-122ac: no Westerosi magic mechanisms. PASS.
- Constraint — cond-kl-court-state-122ac: Green-faction household agent, clerk, magistrate all consistent with 122 AC faction apparatus. Aldric as ward-elder from d06 list consistent with chapter plan. No characters placed in wrong locations. PASS.
- Constraint — cond-taylor-pov-behavior: bones layer is third-limited by pipeline convention; first-person check deferred to rendered draft. No theme-narration in bones. PASS.
- Physical possibility: flies pre-placed by Taylor consistent with capability rank 6. Halvard at the Hook water-trough on ordinary circuit consistent with chapter chunk. PASS.
- Bone count: 33 total (s01:9, s02:9, s03:7, s04:8). Chapter target 15–75. PASS.
- Opposing force visible: Green apparatus in s01 (n02, n05, n07), s02 (n02, n04, n06); accumulated feed-record in s03 (n02, n03, n04); Halvard in s04 (n03, n06, n08). PASS.

---

## Terminate-or-fix verdict

**FIX REQUIRED. Pass 2 does not terminate.**

14 HARD faults. Dispatch to fixer.

Priority cluster — s03: fault-006/007/008 (three "accounting holds the X-image" bones) plus fault-009 (CENTRAL-EVENT BONE: "taylor names the contempt"). The scene's entire accumulation mechanism and its central event are FAULT-FORM-INTERIORITY. Fixer must reconstruct s03's interior naming event in physical SVO form. s03 is a solo interior scene by design; the physical form of the naming must anchor to a body action or externalized speech act, not to the cognitive classification or abstract accounting.

Priority cluster — dialogue-anchor malformation: fault-012/013/014 (all three s04 speech bones). The project's state_axes include no axis labeled community / knowledge / reputation / trust. The closest project analog for the communicative dimension of these bones requires screen-writer determination. Fixer must either map to an existing axis or escalate.

Non-action-verb cluster: fault-001 (carries), fault-002/003/004 (three unlicensed holds on the fly-observation beats), fault-010 (holds the route), fault-011 (stands the water-trough). Six bones.
