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

---

## RE-AUDIT (cycle 1)

```yaml
audit:
  scope: chapter
  target: b01c13
  cycle: 1
  timestamp: 2026-06-03
  basis: corrected 30-bone draft at active-project/staff/screen-writer/b01c13-bones-draft.md
  findings:

    - id: r1-fault-001
      type: fault
      what: >
        b01c13s03 scene header declares axes_held including social_tether-antag, but no bone
        in s03 carries social_tether-antag in its axes_held entry. Roll-up commentary attributes
        social_tether-antag witness to n02, but n02's actual axes_held block declares only
        moral_framework. The attribution exists only in the prose roll-up comment, not in the
        bone's structured field.
      why: >
        A scene-declared held axis with no witnessing bone is a substance gap. The requirement
        is that each declared axes_held entry at scene level be witnessed by ≥1 bone explicitly
        holding it. Downstream facet authors and the stitcher consult bone-level axes_held
        entries, not roll-up commentary, when confirming held-axis discipline. If social_tether-antag
        is not anchored by a bone in s03, the scene's held-axis contract is unverifiable at the
        bone layer.
      criteria: >
        Either (a) one of the four s03 bones must declare social_tether-antag in its axes_held
        block (n02 is the natural candidate since its rationale already references the familiar
        lane environment and the absence of patron-lever), or (b) social_tether-antag must be
        removed from the s03 scene-level axes_held declaration if it cannot be legitimately
        witnessed at the bone layer in a 4-bone scene. The bone's axes_held rationale need not
        change — only the structured axes_held field must carry the axis slug.

    - id: r1-fault-002
      type: fault
      what: >
        b01c13s03 bone count = 4. Scene-level chunk_targets band (memory.md line 1463) specifies
        bone_count: 5-15 for scenes. The re-decomposition from 7 bones to 4 bones falls below
        the declared scene minimum.
      why: >
        The scene-level band is the schema-declared production target for this tier. A 4-bone
        scene is below floor. While the chapter-level aggregate (30 bones, target 15-75) is
        satisfied, the scene-level band exists because scene structural integrity requires
        sufficient bone resolution to cover all declared held axes and both the central-event
        and grounding needs. With only 4 bones and 4 declared held axes (plus 1 moving axis),
        each bone is doing exactly one axis job — there is zero redundancy, and the social_tether-antag
        gap in r1-fault-001 is a direct consequence of the under-bone count.
      criteria: >
        s03 must reach a minimum of 5 bones. The additional bone(s) must not introduce
        SVO violations and must witness at least the missing social_tether-antag held-axis.
        The scene's substance_delta allocation (political_register-prot +0.5, mapped to one
        magnitude-1 moving bone) does not change — additional bones are held bones.

    - id: r1-flag-001
      type: flag
      what: >
        b01c13s03n03 — SVO: taylor-hebert-kl-122ac takes the two-breaths. Object "the
        two-breaths" is a hyphenated compound denoting a measured duration of physical action.
      why: >
        "the two-breaths" is at the edge of the abstraction-as-object rule. Breath is a
        physical act; a counted quantity of breaths is still physically realizable and the
        stitcher can anchor to it. The hyphenated compound form is idiomatic rather than abstract
        in the way "the contempt" or "the weight" are abstract. Classification: FLAG not FAULT —
        the object is physically realizable, but the unusual compound form may prompt a renderer
        to treat it as a duration-abstraction rather than a concrete physical act. Advisory only.
      criteria: null
```

### Prior-fault clearance table

| prior fault | bone targeted | corrected SVO | cleared? | note |
|-------------|---------------|---------------|----------|------|
| fault-001 | s01n04 `carries` | `the supplier's-son shoulders the wrapped-crates` | YES | `shoulders` = discrete hoisting act; transitive; not on deny-list |
| fault-002 | s01n06 `taylor holds the blowfly` | `the blowfly grips the crate-ledge` | YES | object-as-subject ambient insect form; `grips` a physical surface = narrow holds license (surface resisting pressure) or clean `grips` verb; fly as subject not Taylor |
| fault-003 | s02n07 `taylor holds the fly` | `the fly grips the ceiling-corner` | YES | same ambient insect form; concrete surface object |
| fault-004 | s02n09 `taylor holds the fly` | `the fly works the ceiling-corner` | YES | `works` = physically traverses/engages; not a holds form; concrete |
| fault-005 | s02n08 `places his hands on the table` | `aldric grips the table` | YES | transitive `grips` absorbs the surface as direct object; no PP; no possessive modifier |
| fault-006 | s03n02 `the accounting holds the household-agent-image` | `the tallow-smoke crosses the lane` | YES | environment element as subject; `crosses` = concrete transitive motion verb; `the lane` = concrete object |
| fault-007 | s03n03 `the accounting holds the magistrate-document-image` | `taylor-hebert-kl-122ac takes the two-breaths` | YES (with r1-flag-001 advisory) | physical subject; `takes` = concrete act verb; see flag |
| fault-008 | s03n04 `the accounting holds the aldric-hands-image` | `taylor-hebert-kl-122ac resumes the lane` | YES | PP-suppression: `resumes` takes `the lane` as direct object; concrete transitive |
| fault-009 | s03n05 `names the contempt` (CENTRAL-EVENT BONE) | s03 re-decomposed; central-event is now s03n01 `taylor-hebert-kl-122ac stops the lane` | YES | actor-slug subject; `stops` = concrete motion-termination verb; `the lane` = non-abstract object; EVENT-NOT-CONCRETE resolved |
| fault-010 | s04n05 `holds the route` | `taylor-hebert-kl-122ac walks the route` | YES | `walks` = transitive motion verb taking `the route` as direct object; not `holds` |
| fault-011 | s04n08 `halvard stands the water-trough` | `halvard fills the water-skin` | YES | `fills` = concrete transitive physical act; `the water-skin` = concrete object; no stative position |
| fault-012 | s04n03 speech bone; shape: held; axis_moves: [] | shape: held; axes_held: social_tether-antag; citation [septon-halvard-flea-bottom:1] present | YES — under pl-2026-05-30-003 ruling | held-discipline speech bone; comm-class analog axis (social_tether-antag) declared in axes_held; foreclosure rationale present; ruling confirmed by dispatch |
| fault-013 | s04n04 speech bone; shape: held; axis_moves: [] | shape: held; axes_held: relational_anchor_status; citation [taylor-hebert-kl-122ac:1] present | YES — under pl-2026-05-30-003 ruling | same ruling; relational_anchor_status = comm-class analog |
| fault-014 | s04n06 speech bone; shape: held; axis_moves: [] | shape: held; axes_held: social_tether-antag; citation [septon-halvard-flea-bottom:2] present | YES — under pl-2026-05-30-003 ruling | same ruling |
| flag-001 | s01n07 `leans the trestle-table` (transitive ambiguity) | `the household-agent drops the shoulders` | RESOLVED | `drops` transitive; `the shoulders` = body-part object; unambiguous physical posture-release; ambiguity eliminated |
| flag-002 | s02n06 `glances` (perception-verb borderline) | `the magistrate lifts the d06-document` | RESOLVED | `lifts` = clean physical-handling verb; no perception component; central-event concreteness confirmed |

### New per-bone verdict table (corrected 30-bone draft)

| bone | verdict | note |
|------|---------|------|
| b01c13s01n01 | CORRECT | `the blowfly takes the crate-ledge` — ambient insect; `takes` = arrival action; concrete surface |
| b01c13s01n02 | CORRECT | `the household-agent stands the trestle-table` — note: `stands` here is the discrete act of taking a standing position at the table (not stative position-naming); context is scene-open, agent arriving at the table. Accepted. |
| b01c13s01n03 | CORRECT | `the salt-fish supplier faces the household-agent` — `faces` = discrete transitive act of turning to confront |
| b01c13s01n04 | CORRECT | `the supplier's-son shoulders the wrapped-crates` — `shoulders` = discrete hoisting act; cleared |
| b01c13s01n05 | CORRECT | `the household-agent tallies the fish-account` — concrete transitive |
| b01c13s01n06 | CORRECT | `the blowfly grips the crate-ledge` — ambient insect form; cleared |
| b01c13s01n07 | CORRECT | `the household-agent drops the shoulders` — `drops` transitive; `the shoulders` = body-part object; unambiguous |
| b01c13s01n08 | CORRECT | `the supplier's-son picks the empty-crate` — `picks` = discrete transitive; concrete object |
| b01c13s01n09 | CORRECT | `taylor-hebert-kl-122ac releases the blowfly` — `releases` = discrete transitive act |
| b01c13s02n01 | CORRECT | `the fly takes the ceiling-corner` — ambient insect; `takes` = arrival action |
| b01c13s02n02 | CORRECT | `the green-faction-clerk sets the document` — `sets` = concrete transitive placement act |
| b01c13s02n03 | CORRECT | `aldric takes the chair` — `takes` = concrete seating action |
| b01c13s02n04 | CORRECT | `the magistrate writes the procedural-form` — `writes` = concrete transitive |
| b01c13s02n05 | CORRECT | `aldric lifts the cord` — `lifts` = discrete transitive physical act |
| b01c13s02n06 | CORRECT | `the magistrate lifts the d06-document` — `lifts` = clean physical-handling; CENTRAL-EVENT bone; prior flag-002 resolved |
| b01c13s02n07 | CORRECT | `the fly grips the ceiling-corner` — ambient insect form; cleared |
| b01c13s02n08 | CORRECT | `aldric grips the table` — transitive; cleared |
| b01c13s02n09 | CORRECT | `the fly works the ceiling-corner` — `works` = concrete physical engagement; cleared |
| b01c13s03n01 | CORRECT | `taylor-hebert-kl-122ac stops the lane` — CENTRAL-EVENT BONE; PP-suppression; concrete motion-termination; cleared |
| b01c13s03n02 | CORRECT | `the tallow-smoke crosses the lane` — environment element; concrete motion; cleared |
| b01c13s03n03 | FLAG (r1-flag-001) | `taylor-hebert-kl-122ac takes the two-breaths` — object borderline; see r1-flag-001; not a FAULT |
| b01c13s03n04 | CORRECT | `taylor-hebert-kl-122ac resumes the lane` — PP-suppression; concrete transitive; cleared |
| b01c13s04n01 | CORRECT | `halvard finds the water-trough` — `finds` = concrete motion-arrival |
| b01c13s04n02 | CORRECT | `taylor-hebert-kl-122ac reaches the water-trough` — `reaches` = concrete transitive motion-arrival |
| b01c13s04n03 | CORRECT (under ruling) | speech bone; held; axes_held: social_tether-antag; citation present; pl-2026-05-30-003 ruling |
| b01c13s04n04 | CORRECT (under ruling) | speech bone; held; axes_held: relational_anchor_status; citation present; pl-2026-05-30-003 ruling |
| b01c13s04n05 | CORRECT | `taylor-hebert-kl-122ac walks the route` — `walks` transitive; cleared |
| b01c13s04n06 | CORRECT (under ruling) | speech bone; held; axes_held: social_tether-antag; citation present; pl-2026-05-30-003 ruling |
| b01c13s04n07 | CORRECT | `taylor-hebert-kl-122ac leaves the water-trough` — `leaves` = discrete transitive departure |
| b01c13s04n08 | CORRECT | `halvard fills the water-skin` — `fills` = concrete transitive physical act; cleared |

### Substance and aggregate checks (corrected draft)

- Axis slugs: all axis slugs in corrected draft (political_register-prot, political_register-world, moral_framework, relational_anchor_status, moral_legibility_to_self, social_tether-antag) are valid state_axes slugs. PASS.
- Cost ledger anchors: all 30 bones carry cost_ledger_anchor: null; no orphan references. PASS.
- Aggregate delta — s01: political_register-prot +1 (n07, magnitude 1) vs scene target +0.5. Within ±1 convention. PASS.
- Aggregate delta — s02: political_register-world +1 (n06) and political_register-prot +1 (n08) vs targets +0.5 each. Within ±1 convention. PASS.
- Aggregate delta — s03: political_register-prot +1 (n01, magnitude 1) vs scene target +0.5. PASS.
- Aggregate delta — s04: zero vs declared axes_in_motion: []. PASS.
- Chapter aggregate: political_register-prot +3 bone-Δ maps to +1.5 fractional; matches chapter target +1.5. PASS.
- Chapter aggregate: political_register-world +1 bone-Δ maps to +0.5 fractional; matches chapter target +0.5. PASS.
- STAKES-AXIS-DOMINANT (s02): political_register-world moving bone (n06) is the CENTRAL-EVENT bone (mechanism-primary); political_register-prot moving bone (n08) is the consequence-image. Satisfied by mechanism primacy. PASS.
- CARRY_TO_WRITE (s04): two held bones physically enact not-turning-inward — n05 `walks the route` (body on course) and n08 `halvard fills the water-skin` (mirror-still-present). Both grounding-class. PASS.
- Central-event concreteness: s01 n07 `drops the shoulders` (body-part object; discrete act); s02 n06 `lifts the d06-document` (physical-handling; concrete); s03 n01 `stops the lane` (motion-termination; concrete); s04 n07 `leaves the water-trough` (departure; concrete). All PASS.
- s04 held-axis coverage (5 declared axes): moral_framework(n02) ✓ relational_anchor_status(n04) ✓ moral_legibility_to_self(n05,n08) ✓ social_tether-antag(n01,n03,n06) ✓ political_register-prot(n07) ✓. PASS.
- s03 held-axis coverage (4 declared axes): moral_framework(n02) ✓ moral_legibility_to_self(n03) ✓ relational_anchor_status(n04) ✓ social_tether-antag: NO BONE (r1-fault-001 above). FAIL.
- s03 bone count: 4 (below scene minimum 5). FAIL (r1-fault-002 above).
- s01 held-axis coverage (4 declared axes): moral_framework(n03,n08) ✓ relational_anchor_status(n04) ✓ moral_legibility_to_self(n05) ✓ social_tether-antag(n02) ✓. PASS.
- s02 held-axis coverage (4 declared axes): moral_framework(n03) ✓ relational_anchor_status(n05) ✓ moral_legibility_to_self(n07) ✓ social_tether-antag(n02) ✓. PASS.
- Dialogue-anchor citation tokens: s04n03 [septon-halvard-flea-bottom:1] ✓ s04n04 [taylor-hebert-kl-122ac:1] ✓ s04n06 [septon-halvard-flea-bottom:2] ✓. PASS.
- Opposing force visible: s01 (n02,n05,n07) ✓ s02 (n02,n04,n06) ✓ s03 (accumulated feed-record — prior scenes establish the record; naming-threshold is the force; omission_rationale present) ✓ s04 (n03,n06,n08 — Halvard present and acting) ✓. PASS.
- omission_rationale present in s03 event_map for [image: two-feed-events-held-together] and [mechanism: contempt-crystallization]. PASS.
- Register-as-mannerism check: no single VERB+OBJECT pair recurs in ≥3 bones. `speaks to` appears 3 times in s04 but is schema-licensed dialogue form, not a descriptive verb. PASS.
- Bone count chapter total: 30; target 15-75. PASS.

### RE-AUDIT terminate-or-fix verdict

**FIX REQUIRED. Cycle 1 does not terminate.**

All 14 prior HARD faults are cleared. Two new faults introduced by the s03 re-decomposition.

**New HARD faults:**

| id | bone/scope | class |
|----|-----------|-------|
| r1-fault-001 | b01c13s03 (scene level) | social_tether-antag declared held; no witnessing bone in axes_held |
| r1-fault-002 | b01c13s03 (scene level) | bone_count 4 below scene minimum 5 |

Both faults are co-located in s03 and share a single fix path: add ≥1 held bone to s03 that (a) brings the count to ≥5 and (b) explicitly declares social_tether-antag in its axes_held block. The additional bone must satisfy SVO discipline (no copula, no PP, no perception verb, no non-action verb, no abstraction-as-object). r1-flag-001 (`the two-breaths` object) is advisory only and does not block.

The s04 speech-bone held-discipline recasts (fault-012/013/014) are confirmed licit under the pl-2026-05-30-003 extended ruling. No action required on those bones.
