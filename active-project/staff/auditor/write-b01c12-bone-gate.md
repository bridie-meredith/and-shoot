```yaml
audit:
  scope: chapter
  target: b01c12
  gate: /and-write Phase 6 substance bone-gate (mechanical leg)
  timestamp: 2026-06-03
  auditor_note: >
    This is the mechanical leg of the Phase 6 bone-gate. Three audience persona forks run
    in parallel separately. Source files: active-project/staff/screen-writer/b01c12-bones-draft.md
    (42 bones: s01×10, s02×6, s03×12, s04×14 incl. n14 bridge; n07 trimmed) and
    active-project/staff/showrunner/memory.md chapters[b01c12] substance_delta contracts.

  # ============================================================
  # CHAPTER CONTRACT VERIFICATION (from memory.md b01c12)
  # ============================================================
  # axes_in_motion:
  #   moral_framework -1.0 (cl05 cost)
  #   capability +1.0 (cl05 gain)
  #   relational_anchor_status +1.0 ([cl-d08, cl-d06])
  #   social_tether-prot-rise +0.5 (cl-d08b)
  #   position-prot-rise +1.0 (cl02)
  # axes_held: political_register-prot, moral_legibility_to_self, social_tether-antag
  #
  # SCENE CONTRACTS (from memory.md scenes[]):
  # s01: capability +0.5, social_tether-prot-rise +0.5; held: relational_anchor_status, political_register-prot
  #      stakes_axis: social_tether-prot-rise
  # s02: axes_in_motion: none; held: relational_anchor_status, position-prot-rise, social_tether-antag
  #      stakes_axis: relational_anchor_status
  # s03: position-prot-rise +1.0, relational_anchor_status +1.0; held: political_register-prot, social_tether-antag, moral_legibility_to_self
  #      stakes_axis: position-prot-rise
  # s04: capability +0.5, moral_framework -1.0; held: moral_legibility_to_self, political_register-prot, social_tether-antag
  #      stakes_axis: moral_legibility_to_self

  findings:

    # ===========================================================
    # SECTION A: PER-BONE CHECKS — MOVING BONES (bonefide)
    # ===========================================================

    - id: pass-001
      type: pass
      what: >
        b01c12s01n09 (moving — capability +0.5, cl05). SVO: "taylor-hebert-kl-122ac extends
        the northern ward-cluster." Physical cause: Taylor's act of extending the ward-cluster
        physically places insects in a new coverage region. The capability Δ is directly caused
        by the SVO. cl05 gain side cited. Bonefide: PASS.
      why: null

    - id: pass-002
      type: pass
      what: >
        b01c12s01n10 (moving — social_tether-prot-rise +0.5, cl-d08b). SVO: "the ledger column
        closes the water-gate entry." The closing of the boundary-confirmation entry is the concrete
        ledger act that consolidates tether by recording Wren's free movement as the map's eastern
        boundary. cl-d08b cited. Bonefide: PASS.
      why: null

    - id: pass-003
      type: pass
      what: >
        b01c12s03n03 (moving — position-prot-rise +0.5, cl02). SVO: "taylor-hebert-kl-122ac
        writes the boundary entry." The refusal written into the channel record as a structural
        limit constitutes the physical withholding-from-Otto act. The SVO physically causes the
        first position-prot-rise increment. cl02. Bonefide: PASS.
      why: null

    - id: pass-004
      type: pass
      what: >
        b01c12s03n06 (moving — position-prot-rise +0.5, cl02). SVO: "taylor-hebert-kl-122ac
        closes the response entry." The sealing of the refusal makes the withholding load-bearing
        and recorded. Bonefide: PASS. Combined n03+n06 = +1.0, matches s03 contract.
      why: null

    - id: pass-005
      type: pass
      what: >
        b01c12s03n10 (moving — relational_anchor_status +0.5, cl-d08). SVO: "taylor-hebert-kl-122ac
        writes the anchor-column entry." The concrete ledger-act of writing the anchor-column entry
        physically causes the first relational_anchor_status increment. cl-d08 mechanism. Bonefide: PASS.
      why: null

    - id: pass-006
      type: pass
      what: >
        b01c12s03n11 (moving — relational_anchor_status +0.5, cl-d06). SVO: "taylor-hebert-kl-122ac
        closes the anchor-column entry." Parallel to n06 "closes the response entry"; the closing
        physically settles the second tranche. cl-d06 debt settled. Combined n10+n11 = +1.0, matches
        s03 contract. cl-d06 settlement per DEC-0071. Bonefide: PASS.
      why: null

    - id: pass-007
      type: pass
      what: >
        b01c12s04n02 (moving — capability +0.5, cl05). SVO: "the insects fill the muddy-way
        upper-margin." Insects physically occupy a named location (Muddy Way upper margin). The
        SVO is concrete actor-verb-object. The capability Δ is caused by the physical fill. cl05
        gain side second tranche. EVENT-NOT-CONCRETE check: PASS (insects = actor; fill = concrete
        transitive verb; muddy-way upper-margin = named physical object). Bonefide: PASS.
      why: null

    - id: pass-008
      type: pass
      what: >
        b01c12s04n13 (moving — moral_framework -1.0, cl05). SVO: "the breach column takes the
        threshold entry." The breach column is a named physical ledger surface; the entry going
        down is a concrete ledger-act. The moral_framework Δ is physically caused by the threshold
        entry being recorded. EVENT-NOT-CONCRETE check: "takes" is a concrete transitive verb with
        physical object ("the threshold entry"). cl05 cost side. Bonefide: PASS.
      why: null

    # ===========================================================
    # SECTION B: PER-BONE CHECKS — HELD BONES (discipline-enactment)
    # ===========================================================

    # S01 HELD BONES
    # S01 contract axes_held: relational_anchor_status, political_register-prot
    # S01 scene_conflict.stakes_axis: social_tether-prot-rise (held N/A for stakes check — stakes_axis is MOVING in s01)

    - id: pass-009
      type: pass
      what: >
        b01c12s01n01 (held — relational_anchor_status). SVO: "the insects return the
        overhang-joints." The eaves and gutter-joints are the terrain geometry that makes
        dense placement readable as witch-label and forces the gap. The SVO enacts the
        structural constraint — the physical texture of opposition that holds the coverage
        gap in place. Axis is in s01 contract axes_held[]. HELD-AXIS-NOT-ENACTED check: the
        overhang-joints as the specific feature making placement problematic is the architectural
        constraint force enacting stillness against the deployment-pressure. PASS.
        HELD-AXIS-UNCONTRACTED check: relational_anchor_status is in s01 axes_held[]. PASS.
      why: null

    - id: pass-010
      type: pass
      what: >
        b01c12s01n02 (held — relational_anchor_status). SVO: "the insects fan the lane-mouth."
        Ambient deployment at the placement ceiling is the terrain-constraint that makes Wren's
        route the boundary. Axis held. In contract. PASS.
      why: null

    - id: pass-011
      type: pass
      what: >
        b01c12s01n03 (held — political_register-prot). SVO: "taylor-hebert-kl-122ac takes
        the gate-tower shadow." The gap-mapping is a cold technical accounting act; no contempt-
        register fires. Taylor operates in flat operational mode. The SVO enacts the cold-
        utilitarian posture that holds the register. Opposing-force visible: lane geometry enforces
        constraint; upper stories refuse clean placement. In contract axes_held[]. PASS.
      why: null

    - id: pass-012
      type: pass
      what: >
        b01c12s01n04 (held — relational_anchor_status). SVO: "the coverage map closes the
        gate-tower boundary." Physical marking of the gap's western limit as a confirmed operational
        fact. Axis in contract. Held-enactment: the map act itself defines what the anchor inhabits.
        PASS.
      why: null

    - id: pass-013
      type: pass
      what: >
        b01c12s01n05 (held — relational_anchor_status). SVO: "the map closes the rendering-yard
        boundary." Eastern limit confirmed; gap formally bounded. Axis in contract. PASS.
      why: null

    - id: pass-014
      type: pass
      what: >
        b01c12s01n06 (held — relational_anchor_status). SVO: "the insects return the stitch-house
        route." Wren's daily pattern re-confirmed as an indexed operational fact. The anchor-axis
        move belonging to s03; held here as indexing-without-weighting. In contract. PASS.
      why: null

    - id: pass-015
      type: pass
      what: >
        b01c12s01n07 (held — relational_anchor_status). SVO: "the map marks the stitch-maker route."
        Route indexed as the gap's operative eastern boundary. Axis in contract. PASS. Phase-2 fix
        (fault-005) from non-action verb to concrete transitive "marks" already applied.
      why: null

    - id: pass-016
      type: pass
      what: >
        b01c12s01n08 (held — relational_anchor_status). SVO: "taylor-hebert-kl-122ac lifts
        the stylus." Physical stopping-before-writing enacted; the indexed-but-unwritten state
        re-enacted; opposing-force (apparatus expects a priced source) held off by the physical
        withdrawal. Axis in contract. PASS. Phase-2 fix (fault-006) applied (PP dropped).
      why: null

    # S02 HELD BONES
    # S02 contract axes_held: relational_anchor_status, position-prot-rise, social_tether-antag
    # S02 stakes_axis: relational_anchor_status (HELD — N/A for stakes-axis-dominant check)

    - id: pass-017
      type: pass
      what: >
        b01c12s02n01 (held — social_tether-antag). SVO: "jarvis-coin-kl-courier places the
        packet." Opposing force enters via the standard channel. Axis in s02 contract axes_held[].
        Held-enactment: the terrain-literate delivery embodies Otto's apparatus knowing the territory.
        PASS.
      why: null

    - id: pass-018
      type: pass
      what: >
        b01c12s02n02 (held — relational_anchor_status). SVO: "taylor-hebert-kl-122ac breaks
        the wax seal." Physical threshold action that delivers the collision. Axis in contract. PASS.
      why: null

    - id: pass-019
      type: pass
      what: >
        b01c12s02n03 (held — relational_anchor_status). SVO: "taylor-hebert-kl-122ac opens
        the covering-sheet." The request arrives naming the gap-lanes (via content the facet layer
        will carry). Axis in contract. Held-enactment: physical act of opening delivers the
        collision-trigger. PASS. Phase-2 fix (fault-009) applied.
      why: null

    - id: pass-020
      type: pass
      what: >
        b01c12s02n05 (held — social_tether-antag; Phase-3 dramatist reorder positions before n04).
        SVO: "taylor-hebert-kl-122ac turns the covering-sheet." Otto's apparatus targets the gap
        lanes as structural leverage — apparatus knows the territory, names the exact corridor. Axis
        in contract. Opposing-force enacted. PASS. Phase-2 fix (fault-011) applied.
      why: null

    - id: pass-021
      type: pass
      what: >
        b01c12s02n04 (held — position-prot-rise; Phase-3 dramatist reorder positions after n05).
        SVO: "taylor-hebert-kl-122ac sets the packet." Withholding-from-Otto position-move belongs
        to s03; the request arriving is the condition. Axis in contract. Held-enactment: physical
        stillness at decision threshold; the stilling-reaction lands after both corridor boundaries
        named. PASS. Phase-2 fix (fault-010) applied.
      why: null

    - id: pass-022
      type: pass
      what: >
        b01c12s02n06 (held — position-prot-rise). SVO: "taylor-hebert-kl-122ac sets the stylus."
        Physical stillness at the decision threshold; stylus set without writing; withholding-before-
        refusal enacted physically. Axis in contract. Enacts pl-2026-06-03-004 (a) watch. PASS.
        Phase-2 fix (fault-012) applied.
      why: null

    # S03 HELD BONES
    # S03 contract axes_held: political_register-prot, social_tether-antag, moral_legibility_to_self
    # S03 stakes_axis: position-prot-rise (MOVING — stakes-axis-dominant check applies at scene level)

    - id: pass-023
      type: pass
      what: >
        b01c12s03n01 (held — political_register-prot). SVO: "taylor-hebert-kl-122ac takes the
        stylus." Taking the stylus in flat operational register — refusal-writing opens in cold-
        utilitarian mode; no contempt-register fires. Axis in contract. PASS. Phase-2 fix (fault-013)
        applied.
      why: null

    - id: pass-024
      type: pass
      what: >
        b01c12s03n02 (held — political_register-prot). SVO: "the coverage-entry opens the
        gap-column." Gap-column opens in flat format as every prior entry. Axis in contract. PASS.
        Phase-2 fix (fault-014) applied.
      why: null

    - id: pass-025
      type: pass
      what: >
        b01c12s03n04 (held — moral_legibility_to_self). SVO: "taylor-hebert-kl-122ac holds
        the hand." The hand stops before reaching the explanation field — physical enactment of
        withholding-before-writing; stylus does not reach the source-clause; suppression-pattern
        enacted physically. Axis in s03 contract axes_held[]. Opposing-force visible: channel
        expects explanation; Taylor's hand goes elsewhere. PASS.
      why: null

    - id: pass-026
      type: pass
      what: >
        b01c12s03n05 (held — moral_legibility_to_self). SVO: "the stylus lifts." Stylus does
        not reach the explanation field; the physical withholding is the held-discipline beat.
        Axis in contract. Opposing-force: channel expects an explanation. PASS. Phase-2 fix
        (fault-015) applied (PP dropped).
      why: null

    - id: pass-027
      type: pass
      what: >
        b01c12s03n07 (held — social_tether-antag). SVO: "jarvis-coin-kl-courier takes the
        sealed packet." Apparatus receives the refusal via standard channel without press. Axis
        in contract. Held-enactment: acceptance enacted as the apparatus's structural behavior —
        coverage limits accepted, making Taylor's withholding structurally invisible. PASS.
      why: null

    - id: pass-028
      type: pass
      what: >
        b01c12s03n08 (held — political_register-prot). SVO: "the response entry closes the
        gap-column." Gap-column closes in flat operational register; no resentment-color fires;
        the tactical operational close is not a contempt-register event. Axis in contract.
        Opposing-force enacted: channel entry is now a named gap but delivered in flat register.
        PASS.
      why: null

    - id: pass-029
      type: pass
      what: >
        b01c12s03n12 (held — moral_legibility_to_self). SVO: "taylor-hebert-kl-122ac lifts
        the hand." Hand lifts without suppression cracking; accounting filed, column closed;
        legibility holds at 5.5; lift-and-move per pl-2026-06-03-004 (c). Axis in contract.
        PASS. Phase-2 fix (fault-019) applied.
      why: null

    # S03 CHATTER BONE
    - id: pass-030
      type: pass
      what: >
        b01c12s03n09 (chatter — cost_ledger_anchor: cl-d08). SVO: "taylor-hebert-kl-122ac
        opens the anchor-column." Chatter-with-anchor per meta-rule 2 override: the anchor-column
        opening prefigures the n10 relational_anchor_status +0.5 settlement. cl-d08 gain side.
        CHATTER-UNPAID check: cl-d08 resolves at-or-under s03 (the relational_anchor_status move
        at n10+n11 IS in s03). PASS. axis_moves [] and axes_held [] confirm it is chatter.
        Phase-2 fix (fault-016) applied.
      why: null

    # S04 HELD BONES
    # S04 contract axes_held: moral_legibility_to_self, political_register-prot, social_tether-antag
    # S04 stakes_axis: moral_legibility_to_self (HELD — N/A for stakes-axis-dominant check)

    - id: pass-031
      type: pass
      what: >
        b01c12s04n14 (held — moral_legibility_to_self; Phase-3 causal bridge, slug n14
        monotonic). SVO: "the muddy-way entry closes the fifth-ward circuit." The last
        accumulation beat before the threshold: muddy-way fill (n02) causes the fifth-ward
        circuit to close, which causes all five wards to return simultaneously (n03). Axis in
        contract. Held-enactment: the threshold has not yet arrived (shape-word has not surfaced);
        legibility held at 5.5. Causal bridge enacted as physical ledger act (muddy-way entry
        closing the named circuit). PASS. Addresses cold-read s04-seam per DEC-0076.
      why: null

    - id: pass-032
      type: pass
      what: >
        b01c12s04n03 (held — moral_legibility_to_self). SVO: "the feed returns all five wards."
        Full-circuit feed returning all five wards simultaneously — aggregate shape now differs
        from any prior count; word has not yet surfaced. Axis in contract. PASS. Phase-2 fix
        (fault-021) applied.
      why: null

    - id: pass-033
      type: pass
      what: >
        b01c12s04n04 (held — moral_legibility_to_self). SVO: "the count runs the full-circuit
        return." Count runs the full-circuit return at full deployment — aggregate scale establishing
        the referent-weight. Axis in contract. PASS. Phase-2 fix (fault-022) applied (transitive
        recast + PP dropped).
      why: null

    - id: pass-034
      type: pass
      what: >
        b01c12s04n05 (held — moral_legibility_to_self). SVO: "the feed returns the Flea Bottom
        approaches." Accumulation beat before threshold crossing; full-feed density presses toward
        it. Axis in contract. PASS. Phase-2 fix (fault-023) applied.
      why: null

    - id: pass-035
      type: pass
      what: >
        b01c12s04n06 (held — moral_legibility_to_self). SVO: "the accounting reaches the
        aggregate-shape entry." Threshold where the internal accounting's natural shape-word
        surfaces; the accounting reaches this entry and the architecture's own scope becomes the
        opposing-force. Axis in contract. PASS.
      why: null

    - id: pass-036
      type: pass
      what: >
        b01c12s04n07 (held — moral_legibility_to_self). SVO: "the accounting runs the harm-
        prevention column." Harm-prevention column is the rational framework Taylor uses to
        suppress the shape-word's claim; accounting runs it as always; the gap between
        surveillance-and-inference and the override method is the held reality. Axis in contract.
        PASS.
      why: null

    - id: pass-037
      type: pass
      what: >
        b01c12s04n08 (held — moral_legibility_to_self). SVO: "the accounting reaches the breach
        column." Pre-Phase-6 fix applied (orchestrator): held axis changed moral_framework →
        moral_legibility_to_self to avoid held-on-in-motion (moral_framework is s04's MOVING axis
        at n13). Moral_legibility_to_self IS s04's declared held axis. The accounting reaching the
        breach column without yet recording the shape-word is the suppression-discipline. Axis in
        contract. HELD-AXIS-UNCONTRACTED check: moral_legibility_to_self is in s04 axes_held[]. PASS.
      why: null

    - id: pass-038
      type: pass
      what: >
        b01c12s04n10 (held — moral_legibility_to_self). SVO: "the accounting advances the count."
        Accounting advances forward without settling on the shape-word — suppression act enacted as
        physical ledger-progression. Axis in contract. PASS.
      why: null

    - id: pass-039
      type: pass
      what: >
        b01c12s04n11 (held — moral_legibility_to_self). SVO: "taylor-hebert-kl-122ac closes the
        architecture entry." Architecture entry closes without the shape-word in it; suppression
        complete in physical-ledger form; the feed continues past the suppression at full deployment.
        Axis in contract. PASS.
      why: null

    - id: pass-040
      type: pass
      what: >
        b01c12s04n12 (held — moral_legibility_to_self). SVO: "the ledger entry takes the
        full-circuit count." Record-close of the capability gain; full-circuit count filed; legibility
        held at 5.5. Phase-2 fix (flag-003 recast): removed redundant third cl05 citation; capability
        +0.5 stays solely on n02. Axis in contract. PASS.
      why: null

    # S04 CHATTER BONE
    - id: pass-041
      type: pass
      what: >
        b01c12s04n01 (chatter — cost_ledger_anchor: cl05). SVO: "taylor-hebert-kl-122ac extends
        the muddy-way ward-cluster." Chatter-with-anchor per meta-rule 2 override: prefigures
        capability +0.5 at n02 (cl05 gain side). Do NOT hold capability — s04 MOVES that axis.
        CHATTER-UNPAID check: cl05 resolves at-or-under s04 (n02 IS in s04). PASS. Phase-2 fix
        (fault-020) applied.
      why: null

    # ===========================================================
    # SECTION C: HELD-AXIS-NOT-WITNESSED — S04 RISK
    # ===========================================================
    # S04 contract axes_held: moral_legibility_to_self, political_register-prot, social_tether-antag
    # Verified above: moral_legibility_to_self is held by n14, n03, n04, n05, n06, n07, n08, n09, n10, n11, n12 — fully witnessed.
    # Now verify political_register-prot and social_tether-antag in s04.

    - id: fault-001
      type: fault
      what: >
        S04 axes_held declared: [moral_legibility_to_self, political_register-prot, social_tether-antag].
        Inspection of all 14 s04 bones:
        - n01 (chatter, cl05, no axes_held)
        - n02 (moving, capability, no axes_held)
        - n14 (held, moral_legibility_to_self)
        - n03 (held, moral_legibility_to_self)
        - n04 (held, moral_legibility_to_self)
        - n05 (held, moral_legibility_to_self)
        - n06 (held, moral_legibility_to_self)
        - n07 (held, moral_legibility_to_self)
        - n08 (held, moral_legibility_to_self)
        - n09 (held, moral_legibility_to_self)
        - n10 (held, moral_legibility_to_self)
        - n11 (held, moral_legibility_to_self)
        - n12 (held, moral_legibility_to_self)
        - n13 (moving, moral_framework, no axes_held)

        FINDING: zero bones in s04 hold political_register-prot.
        FINDING: zero bones in s04 hold social_tether-antag.

        This is HELD-AXIS-NOT-WITNESSED (HARD) for both political_register-prot and
        social_tether-antag in scene s04. The scene contract declares these two axes held, which
        means the scene must enact their stillness-against-pressure. No bone does so.

        NOTE on the dispatch context: The dispatch prompt states "s04 contract axes_held =
        [moral_legibility_to_self, political_register-prot, social_tether-antag]. Verify
        political_register-prot AND social_tether-antag each have ≥1 holding bone in s04."
        The bones draft confirms the gap — every held bone in s04 holds moral_legibility_to_self
        exclusively. The two contracted held axes are UNWITNESSED.
      why: >
        If political_register-prot and social_tether-antag have no holding bones, the scene
        contract's commitment to hold these axes against pressure is unverified at the bone level.
        Political_register-prot is the chapter's principal held narrative constraint (Taylor's
        flat operational register); social_tether-antag is the antagonist pressure axis. Both
        require at least one bone physically enacting their stillness. Without witnessing bones,
        fixer and stitch have no anchor for the discipline; prose may drift these axes without
        detection.
      criteria: >
        At minimum one bone per axis must hold political_register-prot in s04 (enacting the
        flat-utilitarian accounting mode through which the Khepri suppression runs — no contempt-
        register fires during the interior accounting). At minimum one bone per axis must hold
        social_tether-antag in s04 (enacting Otto's leverage as structural-but-not-advancing —
        the accounting delivers to Otto's channel without exposing the suppression event, so the
        leverage holds at 6 and does not press). Both witnessing bones must use the held axis in
        their axes_held[] field with rationale showing the SVO enacts stillness-against-pressure.

    # ===========================================================
    # SECTION D: PER-SCENE CHECKS
    # ===========================================================

    # --- S01 EVENT-PRESENCE AND CHUNK-TAG COMPLETENESS ---

    - id: pass-042
      type: pass
      what: >
        S01 event-presence (URI-WRITE-EVENT-COVERAGE). Event_map entries:
        [image: east-of-water-gate-lanes] → n01, n02 — both exist and carry the eaves/lane image.
        [mechanism: witch-label-trigger-geometry] → n03 — exists (gate-tower shadow = the terrain constraint).
        [event: coverage-gap-established] → n04, n05 — both exist (map closes gate-tower and rendering-yard boundaries).
        [image: wren-daily-pattern-through-gap] → n06 — exists (insects return stitch-house route).
        [mechanism: wren-as-effective-eastern-boundary] → n07, n08 — both exist (map marks stitch-maker route; stylus lifts without writing source).
        [event: first-ward-cluster-added] → n09, n10 — both exist (extends ward-cluster; ledger closes water-gate entry).

        Central event = "first-ward-cluster-added" (n09+n10). n09 is the concrete SVO of the
        ward-cluster extension (axis-bearing). EVENT-NOT-CONCRETE check: "extends the northern
        ward-cluster" (actor-verb-object, physical). PASS.
        Protagonist_force ("Taylor mapping the gap's exact legal boundaries") appears as n03–n08
        collectively. EVENT-UNCOVERED check: PASS all entries.
        Chunk-tag completeness: all inline [image:/mechanism:/event:] tags covered by event_map entries. PASS.
      why: null

    - id: pass-043
      type: pass
      what: >
        S01 per-axis Δ vs contract (±1 tolerance, EXACT per note). Contract: capability +0.5,
        social_tether-prot-rise +0.5. Delivered: capability +0.5 (n09), social_tether-prot-rise
        +0.5 (n10). EXACT. PASS.
      why: null

    - id: pass-044
      type: pass
      what: >
        S01 STAKES-AXIS-DOMINANT check. stakes_axis = social_tether-prot-rise. s01 axes_in_motion:
        social_tether-prot-rise +0.5, capability +0.5. Dispatch note: "s01 stakes=social_tether
        (+0.5) ties capability (+0.5) → passes (tie passes)." PASS.
      why: null

    - id: pass-045
      type: pass
      what: >
        S01 sensory-grounding (SENSORY-GROUNDING-ABSENT HARD threshold). Grounding bones in s01:
        n01 (eaves/gutter-joints — grounding: true), n03 (gate-tower shadow — grounding: true),
        n05 (rendering-yard east wall — grounding: true), n08 (stylus — grounding: true), n10
        (ledger column — grounding: true). Count: 5 grounding bones of 10. Threshold: ≥1 per scene.
        PASS.
      why: null

    - id: pass-046
      type: pass
      what: >
        S01 abstraction-dominance SIGNAL check (grounding-class < ceil(0.25 × (bone_count −
        chatter_count)) per scene). S01: 10 bones, 0 chatter. Threshold: ceil(0.25 × 10) = 3.
        Grounding bones: 5. 5 ≥ 3. ABSTRACTION-DOMINANT does NOT fire for s01. PASS.
      why: null

    - id: pass-047
      type: pass
      what: >
        S01 held-axes-witnessed. Contract axes_held: relational_anchor_status (witnessed by n01,
        n02, n04, n05, n06, n07, n08 — 7 bones), political_register-prot (witnessed by n03 — 1
        bone). Both witnessed. PASS.
      why: null

    # --- S02 EVENT-PRESENCE AND CHUNK-TAG COMPLETENESS ---

    - id: pass-048
      type: pass
      what: >
        S02 event-presence. Event_map entries:
        [event: jarvis-delivers-new-request] → n01, n02 — both exist (places packet; breaks wax seal).
        [event: otto-requests-east-water-gate-lane-coverage] → n03 — exists (opens covering-sheet).
        [image: packet-describing-the-gap-lanes] → n03, n04 — both exist (opens sheet; sets packet).
        [mechanism: request-collides-with-gap-boundary] → n04, n05 — both exist (sets packet; turns sheet).
        [force: otto-apparatus-knowing-the-terrain] → n05 — exists (turns covering-sheet / apparatus knows territory).
        [event: collision-between-request-and-gap-confirmed] → n05, n06 — both exist.

        Central event = "collision-between-request-and-gap-confirmed" (n05+n06, with n03 as
        the delivery vehicle). Protagonist_force ("Taylor reading the new request against the
        coverage map") appears via n02–n06 (reading, setting packet, setting stylus).

        NOTE: The event_map in the bones file lists the bones in the DRAMATIST-REORDERED sequence
        (n03, n05, n04, n06), but the event_map entries still use original slug names. Event-map
        covers correct bones; bone slugs match. EVENT-UNCOVERED check: all tags have covering bones
        that exist. PASS.
      why: null

    - id: pass-049
      type: pass
      what: >
        S02 per-axis Δ vs contract. Contract: axes_in_motion EMPTY. Delivered: zero axis moves.
        EXACT. PASS.
      why: null

    - id: pass-050
      type: pass
      what: >
        S02 STAKES-AXIS-DOMINANT check. stakes_axis = relational_anchor_status (HELD). When
        stakes_axis is HELD, N/A per dispatch note ("s02 stakes=relational_anchor (HELD) → N/A").
        PASS.
      why: null

    - id: pass-051
      type: pass
      what: >
        S02 sensory-grounding. Grounding bones: n01 (packet — grounding: true), n02 (wax seal
        — grounding: true), n04 (packet set — grounding: true), n06 (stylus — grounding: true).
        Count: 4 of 6. ≥1. PASS.
      why: null

    - id: pass-052
      type: pass
      what: >
        S02 abstraction-dominance SIGNAL check. 6 bones, 0 chatter. Threshold: ceil(0.25 × 6) = 2.
        Grounding bones: 4. 4 ≥ 2. Does NOT fire. PASS.
      why: null

    - id: pass-053
      type: pass
      what: >
        S02 held-axes-witnessed. Contract axes_held: relational_anchor_status (witnessed by n02,
        n03), position-prot-rise (witnessed by n04, n06), social_tether-antag (witnessed by n01,
        n05). All three witnessed. PASS.
      why: null

    # --- S03 EVENT-PRESENCE AND CHUNK-TAG COMPLETENESS ---

    - id: pass-054
      type: pass
      what: >
        S03 event-presence. All 9 event_map entries audited against bone existence:
        [event: taylor-drafts-refusal-to-otto] → n01, n02 — both exist.
        [image: bare-source-field-in-the-response] → n03 — exists (writes boundary entry).
        [mechanism: refusal-without-explanation] → n04, n05 — both exist (holds hand; stylus lifts).
        [event: response-sealed-and-routed-to-jarvis] → n06, n07 — both exist.
        [force: taylor-withholding-the-gap] → n05, n08 — both exist.
        [force: apparatus-accepting-the-boundary] → n07 — exists.
        [event: ledger-entry-anchor-column-opened] → n09 — exists.
        [mechanism: cl-d06-settlement-via-cl-d08-refusal-act] → n10, n11 — both exist.
        [event: relational-anchor-weight-settles] → n11, n12 — both exist.

        Central event = "response-sealed-and-routed-to-jarvis" (n06+n07) and "relational-anchor-
        weight-settles" (n11+n12). Axis-bearing central event bones for position-prot-rise: n03
        (writes boundary entry, +0.5) and n06 (closes response entry, +0.5). Both are concrete
        actor-verb-object SVOs. EVENT-NOT-CONCRETE check: PASS.
        Protagonist_force coverage present. EVENT-UNCOVERED check: all tags covered. PASS.
      why: null

    - id: pass-055
      type: pass
      what: >
        S03 per-axis Δ vs contract. Contract: position-prot-rise +1.0, relational_anchor_status
        +1.0. Delivered: position-prot-rise +0.5 (n03) + 0.5 (n06) = +1.0 ✓;
        relational_anchor_status +0.5 (n10) + 0.5 (n11) = +1.0 ✓. EXACT. PASS.
      why: null

    - id: pass-056
      type: pass
      what: >
        S03 STAKES-AXIS-DOMINANT check. stakes_axis = position-prot-rise. Both axes_in_motion
        deliver +1.0 each. Tie passes per dispatch note ("s03 stakes=position (+1.0) ties
        relanchor (+1.0) → passes"). PASS.
      why: null

    - id: pass-057
      type: pass
      what: >
        S03 sensory-grounding. Grounding bones: n01 (stylus — grounding: true), n04 (hand —
        grounding: true), n05 (stylus — grounding: true), n07 (sealed packet — grounding: true),
        n09 (ledger — grounding: true), n12 (hand — grounding: true). Count: 6 of 12. ≥1. PASS.
      why: null

    - id: pass-058
      type: pass
      what: >
        S03 abstraction-dominance SIGNAL check. 12 bones, 1 chatter (n09). Bone-count minus
        chatter = 11. Threshold: ceil(0.25 × 11) = 3. Grounding bones: 6. 6 ≥ 3. Does NOT fire.
        PASS.
      why: null

    - id: pass-059
      type: pass
      what: >
        S03 held-axes-witnessed. Contract axes_held: political_register-prot (witnessed by n01,
        n02, n08), social_tether-antag (witnessed by n07), moral_legibility_to_self (witnessed by
        n04, n05, n12). All three witnessed. PASS.
      why: null

    # --- S04 EVENT-PRESENCE AND CHUNK-TAG COMPLETENESS ---

    - id: pass-060
      type: pass
      what: >
        S04 event-presence. All 9 event_map entries:
        [event: second-ward-cluster-added] → n01, n02 — both exist (extends muddy-way cluster; insects fill margin).
        [image: aggregate-feed-scale-at-full-deployment] → n14, n03, n04 — all exist.
        [mechanism: khepri-threshold-crossed-in-aggregate] → n05, n06 — both exist.
        [event: internal-accounting-runs-at-full-scale] → n07, n08 — both exist.
        [event: khepri-word-surfaces-in-accounting] → n09 — exists.
        [mechanism: khepri-suppression-act] → n10, n11 — both exist.
        [image: feed-continuing-past-the-suppression] → n11, n12 — both exist.
        [event: capability-full-deployment-confirmed] → n12 — exists.
        [event: moral-framework-ledger-entry-for-threshold] → n13 — exists.

        Axis-bearing central event bones for capability: n02 (insects fill muddy-way upper-margin,
        +0.5). Axis-bearing central event bones for moral_framework: n13 (breach column takes
        threshold entry, -1.0). Both verified concrete. EVENT-UNCOVERED: all tags covered. PASS.
      why: null

    - id: pass-061
      type: pass
      what: >
        S04 per-axis Δ vs contract. Contract: capability +0.5, moral_framework -1.0. Delivered:
        capability +0.5 (n02) ✓; moral_framework -1.0 (n13) ✓. EXACT. PASS.
      why: null

    - id: pass-062
      type: pass
      what: >
        S04 STAKES-AXIS-DOMINANT check. stakes_axis = moral_legibility_to_self (HELD). When
        stakes_axis is HELD, N/A per dispatch note ("s04 stakes=moral_legibility (HELD) → N/A").
        PASS.
      why: null

    - id: pass-063
      type: pass
      what: >
        S04 sensory-grounding. Grounding bones: n02 (muddy-way upper-margin — grounding: true),
        n11 (architecture entry, Taylor's hand closing column — grounding: true), n13 (breach
        column — grounding: true). Count: 3 of 14. ≥1. Sensory-grounding present. PASS.
        Note: the 3-bone count against 14 bones is at the minimum acceptable floor; see SIGNAL
        below.
      why: null

    - id: fault-002
      type: flag
      what: >
        S04 abstraction-dominance SIGNAL (ABSTRACTION-DOMINANT). 14 bones, 1 chatter (n01).
        Bone-count minus chatter = 13. Threshold: ceil(0.25 × 13) = 4. Grounding bones in s04:
        n02 (grounding: true), n11 (grounding: true), n13 (grounding: true). Count: 3. 3 < 4.
        ABSTRACTION-DOMINANT fires as a SIGNAL.

        Disposition: ACCEPT-WITH-RATIONALE. S04 is the chapter's interior-climax scene — the
        Khepri-suppression accounting sequence is by design an interior accumulation of abstract
        ledger-process bones (n03–n12 are the referent-weight buildup). The cold-read risk carry
        (DEC-0076) explicitly arms /and-stitch Phase 8.5 to verify the Khepri-recognition beat
        registers THROUGH the accounting vocabulary. This SIGNAL is design-inherent for an interior-
        climax scene and does not block; route to /and-stitch Phase 4 and Phase 8.5 for physical-
        materiality reinforcement at the prose layer. The auditor's disposition is the same as
        the b01c08/b01c11 precedent (ABSTRACTION-DOMINANT SIGNAL accepted-with-rationale in
        interior-heavy scenes).
      why: >
        If the abstraction-dominance persists at the prose layer, the Khepri-surfacing beat (n09)
        may dissolve into ledger-register fog rather than landing as felt weight. This is the
        "most dangerous register-point in the chapter" per DEC-0076. The stitch must materialize
        the suppression physically.

    # ===========================================================
    # SECTION E: S04 HELD-AXES-WITNESSED (the noted risk)
    # ===========================================================
    # This finding is the primary HARD of this gate. Already captured as fault-001.
    # Restate as explicit finding for clarity.

    - id: fault-003
      type: fault
      what: >
        S04 HELD-AXIS-NOT-WITNESSED — political_register-prot. The s04 contract declares
        political_register-prot as a held axis. Zero bones in s04 carry political_register-prot
        in their axes_held[] field. The axis is declared but unwitnessed in the bone set.

        This is a standalone HARD finding distinct from fault-001 (which covers both unwitnessed
        axes together). Flagged separately for fixer targeting.
      why: >
        Without a bone holding political_register-prot, the scene cannot demonstrate that Taylor's
        Khepri-suppression runs in flat operational register (no contempt-register fire). The axis
        is the prose-register discipline that keeps s04 from becoming a resentment scene or an
        interiority dump. Without a witnessing bone the constraint is invisible to fixer, stitcher,
        and downstream review.
      criteria: >
        At least one bone in s04 must hold political_register-prot with a rationale showing the
        SVO enacts the flat-utilitarian accounting mode — Khepri-suppression occurring in cold
        operational register, no contempt coloring the Khepri beat, the internal accounting running
        as it always runs (harm-prevention column, breach column, gain-side/cost-side). The
        witnessing bone must use the scene's existing idiom (accounting, ledger, column, count)
        without adding a new structural beat.

    - id: fault-004
      type: fault
      what: >
        S04 HELD-AXIS-NOT-WITNESSED — social_tether-antag. The s04 contract declares
        social_tether-antag as a held axis. Zero bones in s04 carry social_tether-antag in their
        axes_held[] field. The axis is declared but unwitnessed.
      why: >
        Without a bone holding social_tether-antag, the scene cannot demonstrate that Otto's
        leverage is structural but non-advancing during the Khepri-suppression accounting. The
        scene contract specifies "Otto's channel receives the second ward-cluster confirmation
        via the standard deliverable update; leverage structural, not advancing." This requires
        at least one bone where the accounting's delivery to Otto's channel is enacted as an
        opposed-by-no-new-leverage-event. Without a witnessing bone this constraint is invisible
        at the bone level.
      criteria: >
        At least one bone in s04 must hold social_tether-antag with a rationale showing the SVO
        enacts the apparatus channel receiving the update without the suppression event becoming
        visible to Otto — leverage holds at 6 because the accounting delivers the ward-cluster
        confirmation via the standard channel while withholding the Khepri-word beat. The bone
        must use an existing s04 physical surface (ledger, entry, column close) without introducing
        a new narrative beat.

    # ===========================================================
    # SECTION F: COST-LEDGER ENTRIES — PAID BY VISIBLE BONES
    # ===========================================================

    - id: pass-064
      type: pass
      what: >
        cl02 (withholding-from-Otto; position-prot-rise +4 / moral_framework -3). Chapter draws
        from the gain side. S03 contract cost_ledger_anchor: cl02 on n03 (position-prot-rise +0.5)
        and n06 (position-prot-rise +0.5). Total s03 cl02 draw: +1.0 position-prot-rise.

        cl02 paid by: n03 ("writes the boundary entry" — the withholding enacted as the refusal
        written into the channel) and n06 ("closes the response entry" — the withholding sealed
        in the deliverable). Both bones are axis-moving with correct direction (up). The SVO in
        each physically IS the withholding act. cl02 gain-side causation verified. PASS.
      why: null

    - id: pass-065
      type: pass
      what: >
        cl05 (capability +2 / moral_framework -1). Chapter draws both gain and cost sides.
        Gain side: n09 (s01, +0.5 capability), n02 (s04, +0.5 capability). Combined +1.0. ✓
        Cost side: n13 (s04, -1.0 moral_framework). ✓
        S04n01 (chatter, cl05 anchor) prefigures n02's gain; does not carry axis-move itself.

        Gain-side bones: n09 ("extends the northern ward-cluster") and n02 ("the insects fill
        the muddy-way upper-margin") — both physically cause the capability increase.
        Cost-side bone: n13 ("the breach column takes the threshold entry") — physically causes
        the moral_framework decrease. Direction verified (capability up; moral_framework down).
        cl05 paid by visible bones. PASS.
      why: null

    - id: pass-066
      type: pass
      what: >
        cl-d06 (relational_anchor_status +2 / moral_framework -1). Chapter draws the +1.0 gain
        side (settlement per DEC-0071 — 2nd tranche, outstanding since c06, re-windowed from
        pl-2026-05-30-001). cl-d06 debt settled via n11 ("closes the anchor-column entry",
        relational_anchor_status +0.5). Combined with cl-d08 at n10 (+0.5) to deliver +1.0.

        n11 SVO physically enacts the settlement: the anchor-column entry closing is the concrete
        ledger-act that records the deferred weight. cl-d06 payment verified through n11.
        Direction correct (up). PASS.
      why: null

    - id: pass-067
      type: pass
      what: >
        cl-d08 (relational_anchor_status +2 / journey-required: [cost-bearer] structurally
        necessary to coverage map without appearing in the ledger). Chapter draws the mechanism
        side (+0.5 gain toward the +1.0 chapter target). cl-d08 cited on: s03n09 (chatter,
        prefigures the settlement); s03n10 (moving, +0.5); s03n11 (cl-d06 cited, but the combined
        move IS the cl-d08 mechanism outcome). n10 ("writes the anchor-column entry") is the
        physical act that enacts the first tranche of the anchor weight settling. The mechanism
        (lane-refusal IS the mechanism by which Wren's free movement becomes load-bearing
        eastern boundary) is established by n03–n08 collectively (the refusal sequence) and
        paid causally. PASS.
      why: null

    - id: pass-068
      type: pass
      what: >
        cl-d08b (social_tether-prot-rise +1 / journey-required: cl-d08). Chapter draws +0.5
        gain side. s01n10 ("the ledger column closes the water-gate entry", social_tether-prot-rise
        +0.5) anchored to cl-d08b. The SVO physically enacts the boundary consolidation that
        closes the tether gap (the map entry closing without Wren's route entering the architecture
        is the gap-boundary confirmation). Direction correct (up). PASS.
      why: null

    # ===========================================================
    # SECTION G: OPPOSING-FORCE-VISIBLE (per-scene)
    # ===========================================================

    - id: pass-069
      type: pass
      what: >
        S01 opposing-force (structural geometry of east-of-water-gate lanes: close overhangs,
        inhabited upper stories, community-label-formation active). Enacted by: n01 (overhang-
        joints returned by insects — terrain constraint), n03 (gate-tower shadow as the cold
        operational positioning — genre contrast to the constraint). Opposing-force: the terrain
        refuses clean placement. Visible in bone set. PASS.
      why: null

    - id: pass-070
      type: pass
      what: >
        S02 opposing-force (apparatus's request, precise and terrain-literate). Enacted by: n05
        (covering-sheet turned — apparatus names the exact corridor, has prior intelligence of
        the terrain). Opposing-force visible in bone set. PASS.
      why: null

    - id: pass-071
      type: pass
      what: >
        S03 opposing-force (apparatus's precision request and what it costs Taylor to decline).
        Enacted by: n07 (jarvis takes the sealed packet — apparatus receives refusal via standard
        channel, the indifference of the apparatus acceptance is the opposing-force enacted). Plus
        the physical field that Taylor's stylus does not reach (n04, n05). PASS.
      why: null

    - id: pass-072
      type: pass
      what: >
        S04 opposing-force (aggregate scale itself: at full-feed density, the internal accounting
        reaches for the Khepri shape-word — the architecture's own scope is the pressure). Enacted
        by: n06 ("the accounting reaches the aggregate-shape entry" — the opposing-force is the
        architecture's natural shape-word surfacing, explicitly named in the rationale). PASS.
      why: null

    # ===========================================================
    # SECTION H: STAKES-AXIS IN UNION (chapter-level)
    # ===========================================================

    - id: pass-073
      type: pass
      what: >
        Stakes-axis-in-union (chapter): each scene's stakes_axis either appears in that scene's
        axes_in_motion or is declared in the scene's axes_held. Verified:
        - s01: stakes_axis = social_tether-prot-rise → in axes_in_motion. PASS.
        - s02: stakes_axis = relational_anchor_status → in axes_held. PASS.
        - s03: stakes_axis = position-prot-rise → in axes_in_motion. PASS.
        - s04: stakes_axis = moral_legibility_to_self → in axes_held. PASS.
      why: null

    # ===========================================================
    # SECTION I: CHAPTER ROLL-UP
    # ===========================================================

    - id: pass-074
      type: pass
      what: >
        Chapter roll-up (from bones header):
        capability: +0.5 (s01/n09) + 0.5 (s04/n02) = +1.0 vs contract +1.0. EXACT.
        social_tether-prot-rise: +0.5 (s01/n10) = +0.5 vs contract +0.5. EXACT.
        relational_anchor_status: +0.5 (s03/n10) + 0.5 (s03/n11) = +1.0 vs contract +1.0. EXACT.
        position-prot-rise: +0.5 (s03/n03) + 0.5 (s03/n06) = +1.0 vs contract +1.0. EXACT.
        moral_framework: -1.0 (s04/n13) vs contract -1.0. EXACT.
        ALL 5 chapter axes EXACT. No SUBSTANCE-FLAT-<axis> fires. PASS.
      why: null

    # ===========================================================
    # SECTION J: S04n09 — THE KHEPRI-SURFACING ADJUDICATION
    # ===========================================================

    - id: fault-005
      type: flag
      what: >
        b01c12s04n09 (held — moral_legibility_to_self). SVO: "the accounting reaches the
        shape-word." CLASSIFICATION: ACCEPT-WITH-RATIONALE FLAG CARRIED TO STITCH. NOT a
        fresh blocking HARD.

        Reasoning:
        (1) n09 is NOT an axis-bearing central-event bone. The axis-bearing central event bones
        for s04 are n02 (capability +0.5, concrete: "insects fill muddy-way upper-margin") and
        n13 (moral_framework -1.0, concrete: "breach column takes threshold entry"). EVENT-NOT-CONCRETE
        (HARD) applies only to axis-bearing central-event bones. n09 does not bear an axis move.
        (2) n09's abstraction is EARTH-BET-FENCE-MANDATED. The concrete formulation of "the
        accounting reaches the Khepri-name" requires the proper noun "Khepri," which is banned by
        the fence. This was adjudicated at Phase-2 (flag-002 minimum-violation compliant),
        worm-canon-pedant ruled the surfacing CLEAN, and admin DEC-0076 armed /and-stitch Phase 8.5
        Check 3 to verify the Khepri-beat lands in assembled prose.
        (3) A concrete in-fence recast is theoretically possible (e.g., "the accounting reaches
        the Gold-Morning entry" or "the accounting reaches the override-architecture column") but
        the project has established "the shape-word" as the canonical cipher-noun for the Khepri-
        referent within the Earth-Bet fence. Deviation would break the chapter's idiom consistency
        without a net benefit. Noted as SIGNAL for fixer/stitcher consideration only.

        SIGNAL: If a concrete cipher-noun that does not use the proper noun "Khepri" exists within
        the established idiom (e.g., a named ledger-column established earlier in the scene
        sequence), screen-writer or stitch may substitute it. This is an invitation, not a requirement.
        The "shape-word" formulation is defensible as established project idiom.

        Route to /and-stitch Phase 8.5 Check 3 per DEC-0076 (Khepri-beat must land as felt weight
        in assembled prose; the cipher-noun must carry accumulated referent-weight from n03–n08).
      why: >
        The Khepri-surfacing is the chapter's interior climax and the most load-bearing event in
        the s04 sequence. If the abstraction of "the shape-word" reads as vague rather than as a
        deliberately blinded proper noun, the scene's emotional payload collapses. The flag ensures
        downstream stages verify the phrase carries weight, not evasion.

    # ===========================================================
    # SECTION K: CHATTER-OVER-CAP SIGNAL
    # ===========================================================

    - id: pass-075
      type: pass
      what: >
        Chatter density-cap check. Chatter bones per scene:
        s01: 0 chatter. s02: 0 chatter. s03: 1 chatter (n09). s04: 1 chatter (n01).
        Chapter total: 2 chatter of 42 bones = 4.8%. No CHATTER-OVER-CAP signal fires.
        Both chatter bones have valid cost_ledger_anchors resolving at-or-under their scene.
        PASS.
      why: null

    # ===========================================================
    # SECTION L: PER-CHAPTER REGISTER-AS-MANNERISM CHECK
    # ===========================================================

    - id: fault-006
      type: flag
      what: >
        REGISTER-AS-MANNERISM: "closes the <X>" appears in ≥3 bones (chapter-wide VERB+OBJECT
        scan, subject-independent).

        Full audit of "closes" as VERB:
        - s01n10: "the ledger column closes the water-gate entry"
        - s02: none
        - s03n06: "taylor-hebert-kl-122ac closes the response entry"
        - s03n08: "the response entry closes the gap-column"
        - s03n11: "taylor-hebert-kl-122ac closes the anchor-column entry"
        - s04n11: "taylor-hebert-kl-122ac closes the architecture entry"

        Count of bones using "closes" as main verb: 5 (n10-s01, n06-s03, n08-s03, n11-s03, n11-s04).
        Threshold: ≥3. FIRES.

        The specific VERB+OBJECT pairs (subject-independent):
        - "closes the water-gate entry" (s01n10) — 1 occurrence
        - "closes the response entry" (s03n06) — 1 occurrence
        - "closes the gap-column" (s03n08) — 1 occurrence
        - "closes the anchor-column entry" (s03n11) — 1 occurrence
        - "closes the architecture entry" (s04n11) — 1 occurrence

        No single VERB+OBJECT pair appears ≥3 times (each "closes the X" names a different object).
        However, the VERB alone ("closes") appears 5 times across the chapter. The dispatch brief
        directs: "Watch 'closes the <X>'" as a mannerism pattern.

        Second verb scan — "reaches the <X>":
        - s04n06: "the accounting reaches the aggregate-shape entry"
        - s04n08: "the accounting reaches the breach column"
        - s04n09: "the accounting reaches the shape-word"
        Count: 3 occurrences within s04. Threshold: ≥3. FIRES within s04 for "reaches" as verb.

        DISPOSITION: ACCEPT-WITH-RATIONALE REFRAIN for both patterns.

        "closes the <X>": Each instance names a different ledger object (water-gate entry, response
        entry, gap-column, anchor-column entry, architecture entry). The repetition is a deliberate
        accounting-refrain — the same structural pattern of "entry closed" reflects Taylor's ledger-
        accounting discipline as a formal narrative device, not accidental repetition. Per the b01c11s04
        precedent (s04n02-n05 "closes the X entry" annotated "intentional accounting-refrain — NOT
        mannerism"). The refrain is load-bearing: it signals that each accounting unit closes in the
        same flat operational way. Accept as intentional.

        "reaches the <X>": All three instances are in s04, which is the interior-accumulation scene
        by design. The "the accounting reaches" idiom is the established project verb for the internal
        accounting running through columns and entries (b01-c02 line 38 precedent: "the accounting
        reaches the ward-junction entry"). The three uses of "reaches" in s04 build the accumulation
        sequence toward the shape-word: each "reaches" is a different column in the progression
        (aggregate-shape → breach → shape-word). This is an intentional refrain-within-scene, not
        chapter-wide mannerism. Accept as intentional.

        SIGNAL: Route both patterns to /and-stitch Phase 4 (voice-embodiment discipline) for
        confirmation that the refrains land as intentional-rhythm rather than register-fog at prose
        level. If the stitcher finds either pattern collapses into deadening repetition at assembled-
        prose layer, targeted REWORD of 1–2 instances is appropriate without restructuring.
      why: >
        Mannerism patterns at prose layer can flatten the chapter's emotional register. The two
        refrains are intentional but should be confirmed by the stitcher.

    # ===========================================================
    # SECTION M: HELD-ON-IN-MOTION VERIFICATION
    # ===========================================================

    - id: pass-076
      type: pass
      what: >
        Held-on-in-motion scan. Confirmed no bone holds an axis its scene moves.
        S01 moves: capability, social_tether-prot-rise. S01 held bones: relational_anchor_status
        and political_register-prot only. No overlap.
        S02 moves: nothing. S02 held bones: relational_anchor_status, position-prot-rise,
        social_tether-antag. No overlap (by definition — no moving axes in s02).
        S03 moves: position-prot-rise, relational_anchor_status. S03 held bones: political_register-prot,
        social_tether-antag, moral_legibility_to_self only. No overlap.
        S04 moves: capability, moral_framework. S04 held bones: moral_legibility_to_self,
        (unwitnessed: political_register-prot, social_tether-antag). n08 (pre-Phase-6 fix): now
        holds moral_legibility_to_self, NOT moral_framework. Verified: moral_framework not held
        anywhere in s04 bones. No held-on-in-motion. PASS.
      why: null

    # ===========================================================
    # SECTION N: COST-LEDGER COMPLETENESS (all ledger entries cited in chapter paid)
    # ===========================================================

    - id: pass-077
      type: pass
      what: >
        Chapter cost-ledger entries cited: cl02, cl05, cl-d06, cl-d08, cl-d08b.
        All five verified paid by visible bones with correct direction (see pass-064 through pass-068).
        No ledger entry cited in the chapter contract lacks a covering bone. PASS.
      why: null

    # ===========================================================
    # SECTION O: SUMMARY
    # ===========================================================

  summary:
    hard_count: 3
    hard_ids: [fault-001, fault-003, fault-004]
    hard_slugs:
      - fault-001: "S04 HELD-AXIS-NOT-WITNESSED — both political_register-prot AND social_tether-antag unwitnessed in s04 (zero holding bones for either axis)"
      - fault-003: "S04 HELD-AXIS-NOT-WITNESSED — political_register-prot (standalone itemization)"
      - fault-004: "S04 HELD-AXIS-NOT-WITNESSED — social_tether-antag (standalone itemization)"
    note_on_hard_count: >
      fault-001 names both missing axes; fault-003 and fault-004 are separate actionable items for
      fixer targeting. The underlying defect is one structural gap (two contracted axes unwitnessed
      in s04), but fixer needs two separate criteria entries to resolve each axis independently.
      Effective unique HARD defect count: 1 (one structural gap, two axis manifestations).

    signal_count: 2
    signal_ids: [fault-002, fault-006]
    signal_dispositions:
      - fault-002: "S04 ABSTRACTION-DOMINANT — 3 grounding bones vs threshold 4; ACCEPT-WITH-RATIONALE (interior-climax by design); routed to /and-stitch Phase 4 and Phase 8.5."
      - fault-006: "REGISTER-AS-MANNERISM — 'closes the <X>' ×5 chapter-wide and 'reaches the <X>' ×3 within s04; ACCEPT-WITH-RATIONALE REFRAIN (intentional accounting-refrain per b01c11 precedent and established project idiom); route to /and-stitch Phase 4 for prose-layer confirmation."

    s04n09_ruling: >
      ACCEPT-WITH-RATIONALE FLAG CARRIED TO STITCH. b01c12s04n09 ("the accounting reaches the
      shape-word") is NOT an axis-bearing central-event bone; EVENT-NOT-CONCRETE (HARD) does not
      apply. The abstraction is EARTH-BET-FENCE-MANDATED (the concrete formulation requires the
      proper noun "Khepri," which is banned). The adjudication (Phase-2 flag-002, worm-canon-pedant
      CLEAN, admin DEC-0076) stands. Route to /and-stitch Phase 8.5 Check 3 to verify the beat
      lands as felt weight in assembled prose. A concrete in-fence alternative (named ledger-column)
      is noted as a SIGNAL for stitcher consideration but is not required.

    s04_held_axes_witnessed:
      moral_legibility_to_self: "WITNESSED — 11 holding bones (n14, n03, n04, n05, n06, n07, n08, n09, n10, n11, n12)"
      political_register_prot: "NOT WITNESSED — zero holding bones in s04 (HARD: fault-003)"
      social_tether_antag: "NOT WITNESSED — zero holding bones in s04 (HARD: fault-004)"

    mannerism_count: 2
      - pattern: "closes the <X>"
        count: 5
        disposition: "ACCEPT-WITH-RATIONALE REFRAIN (intentional accounting-refrain, b01c11 precedent)"
      - pattern: "reaches the <X>"
        count: 3 (all within s04)
        disposition: "ACCEPT-WITH-RATIONALE REFRAIN (established project idiom; intentional accumulation sequence)"

    gate_verdict: FAIL
    fail_reason: >
      3 HARD findings (fault-001/003/004) — all from the same structural gap: two contracted
      axes (political_register-prot, social_tether-antag) are declared held in s04 but have
      zero witnessing bones. Fixer must add at minimum one holding bone per axis in s04 using
      existing scene surfaces without introducing new narrative beats or disturbing the contracted
      axis-moves (n02 capability, n13 moral_framework) or the chatter-with-anchor (n01 cl05).
      All 2 SIGNALS accepted-with-rationale and do not block; both route to stitch.
      All other checks (bonefide, chunk-tag completeness, event-presence, per-axis Δ EXACT,
      stakes-axis-dominant, sensory-grounding, cost-ledger paid, opposing-force visible,
      held-on-in-motion, roll-up EXACT) PASS cleanly.
```
