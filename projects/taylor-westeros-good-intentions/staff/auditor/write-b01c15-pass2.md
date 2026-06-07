```yaml
audit:
  scope: chapter
  target: b01c15
  timestamp: 2026-06-04
  phase: /and-write Phase 2 — constraint + SVO-form audit
  bone_count: 40
  findings:

    # ─── FAULT-FORM: MODIFIER ──────────────────────────────────────────────────

    - id: fault-001
      type: fault
      what: >
        b01c15s01n05 SVO: "the sapphire catches the morning light differently from the eye beside it"
        Offending tokens: `differently` (adverb) + `from the eye beside it` (prepositional comparison
        phrase).
      why: >
        Two schema violations in a single bone: `differently` is an adverb (FAULT-FORM-MODIFIER);
        `from the eye beside it` is a prepositional phrase that cannot be the direct object of
        `catches`. The bone is on the concreteness-watch adjacency list (sapphire image, S01 peak).
        If left, the stitch-register imports the adverb and comparison phrase into prose where they
        read as authorial editorializing.
      criteria: >
        Recast to modifier-free SVO that preserves the physical fact: the sapphire does not track
        like the organic eye. Concreteness-preserving candidates: "the sapphire holds flat against
        the drill-angle change" (narrow holds license: body part resisting movement — the sapphire
        IS in the eye socket, a body-implanted surface); or split into two bones: one for the sapphire
        catching the light (physical), one for the organic eye adjusting (physical contrast made
        concrete). Do NOT collapse to "the sapphire catches the morning light" alone — the contrast
        between sapphire and organic eye is the image:sapphire-fixed-against-moving payload; losing
        the contrast loses the event.

    - id: fault-002
      type: fault
      what: >
        b01c15s01n07 SVO: "aemond-targaryen sets the approach angle wide"
        Offending token: `wide` (adverb/adjective MODIFIER).
      why: >
        `wide` modifies the verb's manner. The SVO must record the observable action; the width-quality
        is facet material. The bone covers image:vhagar-behavioral-imprint and a held axes_held entry;
        an unresolved MODIFIER passes the adverb into the stitcher's bone-faithfulness render.
      criteria: >
        Recast to remove the modifier while preserving the physical action. Concreteness-preserving
        candidate: "aemond-targaryen opens the approach angle" (opens = transitive physical action
        expanding the angle to a wider position — the wideness is in the verb, not an adverb hanging
        off it). Alternative: split — one bone for "sets the approach angle" and a second grounding
        bone naming the result concretely if the physical consequence requires a second beat.

    - id: fault-003
      type: fault
      what: >
        b01c15s01n08 SVO: "aemond-targaryen holds the weight ready at a height that clears more
        ground than the yard provides"
        Offending tokens: `ready` (adjective MODIFIER); `at a height that clears more ground than the
        yard provides` (extended prepositional MODIFIER clause); `holds` (narrow-license violation —
        object is `the weight`, an abstract force, not a body part or physical object resisting pressure).
      why: >
        Triple violation on a concreteness-watch bone (mechanism:vhagar-behavioral-imprint-gait-read
        completion). `ready` is an adjective hanging off the verb. `at a height that clears more ground
        than the yard provides` is a prepositional phrase of place + a comparative clause — both banned.
        The narrow `holds` license (body part + stillness-against-pressure, OR physical object resisting
        pressure) does not cover `the weight`: weight is an abstract quantity, not a discrete physical
        object. `holds the weight ready` fails the license. Author's own notes flag this as a Phase 2
        adjudication item. The c03 contamination lesson applies: fixing MODIFIER violations on
        concreteness-watch bones by abstracting is itself a fault (pl-2026-06-04-c15-001).
      criteria: >
        Recast to remove all three violations while preserving the physical content: Vhagar-scale
        body-position enacted in a yard-scale space. Concreteness-preserving candidates: "aemond-
        targaryen braces the sword-grip at Vhagar-clearance height" (transitive concrete verb, named
        physical object, no prep modifier); or "aemond-targaryen lifts the blade past the yard's
        overhead margin" (physical action, location as direct object). The key physical content is:
        the arm/blade position assumes dragon-clearance that the yard cannot justify. The recast MUST
        name the physical action and the physical object. Do NOT recast to "aemond-targaryen holds
        the stance" or similar abstraction.

    - id: fault-004
      type: fault
      what: >
        b01c15s01n13 SVO: "aemond-targaryen runs the correction again"
        Offending token: `again` (adverb MODIFIER).
      why: >
        `again` modifies the verb's iteration. Adverbs are banned. The bone covers
        force:taylor-cold-read completion (the repetition beat) and is the chapter-close-of-scene
        marker. The iteration-quality is the narrative payload of this bone — but it must be encoded
        in the verb or object, not in an adverb.
      criteria: >
        Recast to remove `again` while preserving the physical repetition event. Candidate: "aemond-
        targaryen repeats the correction sequence" (the repetition is in the verb `repeats`, not an
        adverb). The bone must make the second-run physically observable without using `again`.

    - id: fault-005
      type: fault
      what: >
        b01c15s03n03 SVO: "the east-water-gate lanes return no thermal-noise against the noisy fringe"
        Offending tokens: `no` (NEGATION — schema: "no/not/without/never" banned); `noisy` (adjective
        MODIFIER); `against the noisy fringe` (prepositional MODIFIER phrase).
      why: >
        `no` is an explicit schema negation — the bone records a non-event rather than what happened.
        `noisy` is an adjective. `against the noisy fringe` is prepositional padding. This is a
        concreteness-watch bone (1) setup: it establishes the figure-ground contrast before n04 fires
        the relational_anchor_status move. The negation form actively undermines the concreteness-watch
        requirement because it names what is absent rather than what is present. The pl-2026-06-04-
        c15-001 watch explicitly names this bone. Fixer note: do NOT let form-fixing collapse the
        figure-ground contrast to an abstraction.
      criteria: >
        Recast to positive-SVO form that preserves the physical figure-ground contrast while removing
        negation and modifiers. Concreteness-preserving split: (a) one bone for the fringe returning
        signal-interference (what IS happening); (b) one bone for the gap-lane returning silence
        (what the gap DOES — routes the absence as an action, not a negation). Example split:
        "the fringe-flies return signal-interference at the eastern boundary" / "the east-water-gate
        lanes return silence to the feed." Both are positive SVOs. The silence is what the lane DOES,
        not what it fails to do. This may require inserting one bone (n03 becomes two thin bones) and
        adjusting n04 accordingly; or fusing the content into a recast n03 if a single positive SVO
        can carry both sides of the contrast.

    - id: fault-006
      type: fault
      what: >
        b01c15s03n04 SVO: "the gap-lane holds a clean window against the noisy fringe"
        Offending tokens: `clean` (adjective MODIFIER); `noisy` (adjective MODIFIER); `against the
        noisy fringe` (prepositional MODIFIER phrase). Additional issue: `holds` narrow-license
        adjudication — object is `a clean window`, which is an abstraction (a window of absence/
        silence), not a physical object resisting pressure and not a body part.
      why: >
        This is the HARD concreteness-watch (1) bone carrying relational_anchor_status +2 (magnitude
        2). Two adjective modifiers (`clean`, `noisy`) and one prepositional modifier phrase are
        schema violations. The `holds` license is borderline: the author argues the gap holds absence
        against the noise filling it (gap as physical space resisting fringe-noise). However the schema
        requires the object to be a body part OR a physical object resisting pressure — `a clean
        window` is a metaphor-object, not a physical discrete object. The distinction matters because
        the stitch-register must render bone-faithfully; a metaphor-holding-verb is interiority-
        adjacent. The pl-2026-06-04-c15-001 watch names this bone explicitly. Fixer note: the
        concreteness — gap returning silence vs fringe returning interference — MUST survive the recast.
        Do NOT abstract to "the exclusion advances" or similar.
      criteria: >
        Recast to remove all modifier tokens and replace the `holds` construction with a transitive
        verb whose object is a concrete physical datum. The physical content to preserve: the gap-lane
        returns a different signal-texture than the fringe (absence vs interference). Concreteness-
        preserving candidates: "the gap-lane returns silence against the fringe-interference" — but
        `against` is still a prepositional MODIFIER. Better: split the contrast into the parallel
        bone pair established at fault-005 recast, with n04 carrying only the axis-moving element
        (the gap's distinctiveness as a figure-ground event): "the gap-lane returns the absence to
        the feed" (the absence IS the signal, the physical datum the feed receives). The
        relational_anchor_status +2 move anchors to the bone recording the gap as a physical feed-event,
        not to a comparison-with-fringe that requires modifier adjectives to express.

    - id: fault-007
      type: fault
      what: >
        b01c15s03n05 SVO: "the gap-lane stands as shadow stands against a lit wall"
        Offending tokens: `stands` (stative position-naming verb — schema: banned when describing
        position, not a posture-act); `as shadow stands against a lit wall` (comparison clause =
        MODIFIER / simile construction = INTERIORITY); `lit` (adjective MODIFIER).
      why: >
        Three violations: (1) `stands` in the subject-position describes the gap-lane's position/
        state, not a discrete physical action — stative position-naming per schema. (2) The simile
        "as shadow stands against a lit wall" is a thought-figure (the gap does not literally stand
        against a wall — this is Taylor's comparative perception), which routes to the narrator-
        interest facet, not the bone. (3) `lit` is an adjective modifier. This bone carries
        social_tether-antag +1 (the lock-completion move for cl-antag-d03). The simile-as-SVO
        leaves the axis-moving event unanchored to a concrete observable action. Concreteness-watch
        concern: the simile could be rendered as metaphor rather than physical event.
      criteria: >
        Recast to a positive SVO recording a concrete observable action that carries the perceptual
        confirmation without simile or stative verb. The physical content to preserve: the gap-lane
        is perceptually distinguishable from the disrupted fringe — its absence has a shape. Candidate:
        "the gap-lane edge stands against the fringe-boundary" fails (stative). Better: "the feed
        returns the gap-lane edge as a distinct boundary" (the feed DOES something; the gap-lane
        edge IS the physical object receiving the action). Or: "the gap-lane boundary sharpens
        against the fringe-noise" — but `sharpens against` uses `against` as prep phrase. Best:
        the physical event is the gap registering differently in the feed output. Frame as the feed
        acting, not the gap standing: "the feed renders the gap-lane boundary above the fringe-noise."
        The simile's content (shadow against wall = figure against ground) moves to the narrator-
        interest or metaphor facet citing this bone.

    - id: fault-008
      type: fault
      what: >
        b01c15s04n08 SVO: "the coverage-record notation rests without a name-field entry for the
        gap-lane"
        Offending tokens: `rests` (stative/non-action verb — schema: stative position-naming banned);
        `without` (NEGATION — schema: "no/not/without/never" banned).
      why: >
        Double violation on a concreteness-watch (2) bone (force:wren-as-named-absence). `rests` is
        stative: the coverage-record is in a position, not performing an action. `without a name-field
        entry` is a negation form — it names the absence, not an action. Author's notes flag this bone
        explicitly as Phase 2 adjudication required and propose "the coverage-record name-field holds
        the gap-lane entry blank" as a candidate recast — but this recast also uses `holds`, and the
        narrow `holds` license requires a physical object resisting pressure; `the gap-lane entry
        blank` is abstract. Fixer note: the concrete physical content to preserve is that the name-
        field has no name written in it — the actual physical state of the paper/record-surface.
      criteria: >
        Recast to remove both `rests` and `without` while preserving the physical fact: the name-field
        is blank where a name could be written. Positive-SVO form required. Concreteness-preserving
        candidates: "the coverage-record name-field carries the gap-lane row without entry" still
        uses `without`. Better: "the gap-lane row in the coverage-record carries a blank name-field"
        — `carries` is on the schema's sustained-carrying banned list. Better still: "the coverage-
        record name-field leaves the gap-lane row empty" — but `leaves` is ambiguous. Best approach:
        make the physical object (the blank surface) the subject of an action the stitcher can
        render concretely: "the gap-lane name-field in the coverage-record holds the stylus-blank"
        — `holds` narrow license: the paper surface (physical object) resisting being written on;
        the stylus-blank is the concrete absence as a physical state of the surface. This is on the
        edge of the narrow license but closer than `rests without`. Phase 6 substance-gate at
        /and-write Phase 6 re-verification required after recast.

    # ─── FAULT-FORM: NEGATION ─────────────────────────────────────────────────
    # (covered under fault-005 for s03n03 and fault-008 for s04n08 above)

    # ─── FAULT-BONE-DELTA-MALFORMED: CHATTER BONE WITHOUT ANCHOR ─────────────

    - id: fault-009
      type: fault
      what: >
        b01c15s01n04 SVO: "aemond-targaryen steps onto the outer-court-ground"
        axis_moves: []  axes_held: []  cost_ledger_anchor: none
        Declared chatter bone; notes state coverage by n01's cl05 entry.
      why: >
        A bone with empty axis_moves, empty axes_held, AND no cost_ledger_anchor is a chatter bone
        with no substance anchor. The dispatch schema requires: chatter bone must have
        cost_ledger_anchor, OR the bone must appear in axes_held of another bone's rationale as an
        explicit referenced anchor, OR it must be a declared scene-transition chatter bone with
        documented omission_rationale in the event_map. n04's notes point to n01's cl05 entry as
        the cover — but the schema requires the chatter bone itself to carry the anchor reference, not
        the adjacent bone. The chatter bone inherits no anchor from sibling bones. Additionally,
        n04 carries prepositional modifier `onto the outer-court-ground` (FAULT-FORM-MODIFIER —
        `onto` is a direction prep phrase).
      criteria: >
        Either (a) add cost_ledger_anchor: cl05 to n04 explicitly, documenting that this is the
        second half of the same cl05 draw as n01 (the two-bone coverage setup event); or (b) fold
        n04's event coverage into n03 or n01 and remove n04 entirely if the transition beat is
        redundant given those bones. Also recast the SVO to remove the prepositional MODIFIER:
        "aemond-targaryen enters the outer-court-ground" (enters is transitive with location as direct
        object). The chatter anchor gap is the blocking issue; the SVO recast is secondary.

    # ─── FAULT-CONSTRAINT: AEMOND AGE INTER-DOCUMENT CONFLICT ────────────────

    - id: fault-010
      type: fault
      what: >
        b01c15s01 event_map source chunk: "Aemond Targaryen, twelve years old"
        b01c15 chapter goal text: "Show the audience Aemond through compound eyes — the escalation
        engine in physical form, 13 years old..."
        b01c15 chapter chunk: "Aemond (now 13)"
        actor card (active-project/actors/aemond-targaryen-122ac/card.md): "12 at 122 AC (born 110 AC)"
        cond-kl-court-state-122ac: "Sixteen at 122 AC (born 106 AC)"
      why: >
        Four documents carry four different figures: scene chunk says twelve, chapter goal says
        thirteen, chapter chunk says "now 13," lore card says sixteen, actor card says twelve.
        The actor card is a project-scoped variant card explicitly authored for this project at 12
        (born 110 AC). The lore card cites F&B canon at 16 (born 106 AC). These two authoritative
        project documents are in irreconcilable conflict — they use different birth years (110 AC
        vs 106 AC). The c15 bones use "twelve" (actor card consistent) but the chapter-goal text
        says "13" (neither consistent). This conflict has been present since at least c01
        handoff_in ("Aemond: 12 years old, Vhagar-bonded") and is not a c15-specific error. If
        the project has been running on the actor card's 12-year baseline, the lore card's 16 is
        the error; if F&B canon governs, the actor card's birth year is incorrect. Either way, the
        chapter goal text ("13 years old") contradicts BOTH the actor card (12) and the lore card
        (16), and must be corrected.
      criteria: >
        Showrunner must resolve which birth year is authoritative for this project before /and-write
        Phase 7 emits the flat bones file. Resolution options:
        (a) Actor card governs (project-authored; 12 at 122 AC; born 110 AC): update
        cond-kl-court-state-122ac to reflect the project-specific AU birth year (born 110 AC, not
        106 AC); update all chapter goal/chunk text references from "twelve" or "thirteen" to the
        single correct age for 122 AC; audit all prior chapter handoff_out entries for consistency.
        (b) F&B lore card governs (16 at 122 AC; born 106 AC): update the actor card variant-reason
        + all biography fields + all chapter handoff entries + all scene chunk references to sixteen;
        reconsider the "Otto-directed only; not independent" characterization which may not fit a
        sixteen-year-old by the project's own analysis.
        In either case, the chapter goal text must be corrected from "13" to the resolved age.
        This is a chapter-scope fix with cascading handoff implications through all prior chapters
        that reference Aemond's age.

    # ─── FLAGS ────────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      what: >
        b01c15s01n01 SVO: "taylor-hebert-kl-122ac anchors two flies above the stone-lip of the
        outer-court approach"
        b01c15s01n02 SVO: "taylor-hebert-kl-122ac anchors one fly in the corner-gutter of the
        passage-arch"
      why: >
        Both bones carry prepositional phrases of place (`above the stone-lip`, `in the corner-gutter`)
        that are technically FAULT-FORM-MODIFIER violations under the strictest reading of the schema
        ("Prepositional phrases of place / destination / source / direction / instrument / accompaniment
        are explicitly banned"). However, these are place-of-deployment constructions that give the
        physical anchor context required for the passage-adjacent ward circuit to be legible as a
        location (not interior abstraction). The schema's preferred form is "a transitive verb that
        takes the location as direct object" — `anchors` is already transitive with the fly as direct
        object; the place phrase is additional context. These bones are grounding-bones (n01, n02 both
        marked grounding: YES). Flagging rather than faulting because: (1) the schema's direct-object
        exception is primarily about motion verbs, not placement verbs; (2) these are grounding bones
        where physical specificity is load-bearing for the followability track per the bones-review
        FOLLOW-CHECK preconditions; (3) the stitch-register will use these as location-context that
        the loc-state facet should absorb anyway. Fixer should verify intent but these do not block.

    - id: flag-002
      type: flag
      what: >
        b01c15s02n09 SVO: "taylor-hebert-kl-122ac marks the thermal-rise as site-condition in the
        internal record"
        Verb: `marks` — form-watch advisory per b01c11 precedent (memory.md b01c11s02n09 note:
        "instrument-class ('marks') — carried to /and-stitch P4").
      why: >
        `marks` carries an instrument-class verb watch from prior chapter production. The schema does
        not explicitly ban it but it is semantically adjacent to `noted` (on the banned-perception-
        verb list). Additionally, `as site-condition in the internal record` contains `in the internal
        record` (prepositional MODIFIER of place). This is a flag rather than a fault because (1) the
        instrument-class watch is a soft advisory, not a hard ban; (2) this bone has no axis_moves so
        it does not carry the load of an axis event. The prepositional phrase is a borderline modifier.
        Stitch-phase should address the instrument-class register at Phase 4 voice-embodiment.

    - id: flag-003
      type: flag
      what: >
        b01c15s03n01 SVO: "the eastern-fringe flies pick up more thermal-noise than the arch-flies"
        Tokens: `more thermal-noise than the arch-flies` (comparative construction).
      why: >
        The comparative form (`more X than Y`) introduces a modifier-class construction (the
        comparative `more` and the comparative clause `than the arch-flies`). Under strict schema
        this is a MODIFIER. However the sentence is a grounding bone (n01 marked grounding: YES)
        and the comparison encodes the physical differential that the S03 scene requires to exist
        before the figure-ground event. The comparative form is not a direct adjective or adverb
        modifier of the verb — it compares two named physical populations. Flagging rather than
        faulting because the concreteness-watch value of this bone is load-bearing (establishes
        the degraded-coverage state that makes n03-n04 legible). Stitch-phase should render the
        differential as physical rather than comparative.

    - id: flag-004
      type: flag
      what: >
        b01c15s03n06 SVO: "the eastern-boundary edge sharpens against the fringe where the two
        stone edges named at c12 meet the disrupted feed"
        Token: `where the two stone edges named at c12 meet the disrupted feed` (relative-clause
        MODIFIER); `disrupted` (adjective MODIFIER).
      why: >
        The relative clause `where ... meet the disrupted feed` is a modifier qualifying the
        subject/location further. `disrupted` is an adjective. These are schema violations under
        the strict reading. However this bone is a grounding bone with axes_held only (no axis
        move) and serves primarily as a physical anchor for the c12 coverage-record cross-reference.
        The c12 stone-edge reference is important for context-ledger continuity and the bones-review
        FOLLOW-CHECK track. Flagging rather than hard-faulting because the relative clause is doing
        referential work (connecting to a prior chapter's concrete detail) rather than decorative
        padding, and its removal would require a separate grounding bone for the c12 stone-edge
        reference. Stitch-phase Phase 4 should assess whether the clause survives voice-embodiment.

    - id: flag-005
      type: flag
      what: >
        b01c15s02n05 SVO: "the arch-flies register the hill-warm against the bay-warm at the
        passage-arch edge"
        Token: `register` — functionally a perception verb (equivalent to `notice`, which is on the
        banned list).
      why: >
        `register` is not on the schema's explicit banned-perception-verb list (`read, took, tracked,
        noted, counted, measured, watches, sees, hears, notices`) but is semantically identical to
        `notices` or `reads`. The bone carries social_tether-antag +1 (cl-antag-d03 first half).
        If the stitch-phase renders this as a perception-verb sentence, the prose will carry a
        FAULT-POV violation at the narrator layer. Flagging because `register` is not explicitly
        banned; also, this bone describes the insects performing a thermal-detection function, which
        is arguably the insects DOING something (detecting), not Taylor perceiving. The distinction
        is: if Taylor perceives the insects registering the differential, it's POV-leak; if the
        insects ARE the registration mechanism (the feed IS the instrument), it's a physical action
        on the insects' part. The context notes confirm the intent is the latter (n04's notes: "the
        concreteness watch requirement: the warm-airstream registers as motion-pressure in the
        flight-musculature, NOT as Taylor perceiving temperature"). Stitch-phase must render this
        as the insects' physical action, not Taylor's perception.

    # ─── PASSES ───────────────────────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: >
        Constraint check: cond-dragon-proximity-122ac
      why: >
        Vhagar is present in c15 as thermal/pressure backwash only — not on-stage, not a direct
        scene partner, not a tool Taylor deploys or interacts with. The insect dead-zone behavior
        (thermal degradation creating the fringe-noise that makes the gap-lane visible) is consistent
        with the card's dead-zone mechanism. Taylor reads the thermal footprint from outside the
        zone. No on-stage dragon appearance. No Taylor-dragon interaction. PASS.

    - id: pass-002
      type: pass
      what: >
        Constraint check: cond-earth-bet-noun-fence
      why: >
        No parahuman jargon in any of the 40 bone SVOs. No Earth-Bet proper nouns. No cape-name
        vocabulary. The "compound eyes" construction uses the Westerosi-adjacent description per the
        substitution register. PASS.

    - id: pass-003
      type: pass
      what: >
        Constraint check: cond-override-architecture-residue-122ac — range and capability scope
      why: >
        c15's coverage is at the Red Keep outer-court approach margin — passage-adjacent. This is
        within operational range. No Dragonpit-interior coverage attempted. No Khepri-mantle
        capability implied (no human body coordination). The thermal-read mechanism operates through
        insects' flight-musculature response, not direct override. PASS.

    - id: pass-004
      type: pass
      what: >
        Cost ledger validation: cl05, cl-antag-d03, cl04
      why: >
        All three anchors are present in memory.md series.substance.cost_ledger[]:
        cl05 (capability +2, moral_framework -1) — valid, at line ~1398.
        cl-antag-d03 (social_tether-antag +4) — valid, at line ~1378.
        cl04 (relational_anchor_status +3) — valid, at line ~1390.
        No FAULT-COST-LEDGER-UNRESOLVED. PASS.

    - id: pass-005
      type: pass
      what: >
        State_axes slug validation for all axis_moves entries across 40 bones
      why: >
        All axis slugs used in axis_moves — capability, political_register-prot, social_tether-antag,
        relational_anchor_status — match slugs in memory.md series.substance.state_axes[]. Direction
        values are all `up` (correct for these axes in their c15 chapter contract direction).
        Magnitudes: all 1 or 2 (within the 1-3 bone delta range). No FAULT-BONE-DELTA-MALFORMED on
        slug, direction, or magnitude. PASS.

    - id: pass-006
      type: pass
      what: >
        Aggregate delta vs chapter target check (all four scenes)
      why: >
        S01: capability actual +1 vs target 0.5 → within ±1. political_register-prot actual +1 vs
        target 0.5 → within ±1.
        S02: social_tether-antag actual +1 vs target 0.75 → within ±1. capability actual +1 vs
        target 0.5 → within ±1.
        S03: relational_anchor_status actual +2 vs target 1.5 → within ±1. social_tether-antag actual
        +1 vs target 0.75 → within ±1. (Magnitude-2 bone licensed by 1-3 range; ±1 tolerance absorbs.)
        S04: all held, all delivered held → exact match.
        No FAULT-AGGREGATE-DELTA-MISMATCH. PASS.

    - id: pass-007
      type: pass
      what: >
        Perception-verb scan (primary list: read, took, tracked, noted, counted, measured, watches,
        sees, hears, notices) across all 40 bone SVOs
      why: >
        No instance of any schema-listed perception verb in any bone SVO. The bones consistently use
        the world-doing-things construction: flies judder, arch-flies register (flagged separately as
        flag-005), feed returns, stone channels, master-at-arms reduces, etc. Taylor's actions are
        physical (anchors, returns the feed, exhales, writes, closes, runs) not perceptual labeling.
        PASS on the explicit banned-list check. See flag-005 for `register` as adjacent concern.

    - id: pass-008
      type: pass
      what: >
        Conjunction scan (and, but, while, as) across all 40 bone SVOs
      why: >
        No conjunction tokens in any bone SVO. All SVOs are single-clause. PASS.

    - id: pass-009
      type: pass
      what: >
        Copula scan (is, was, will, am, are, were, be, been, being) across all 40 bone SVOs
      why: >
        No copula tokens in any bone SVO. PASS.

    - id: pass-010
      type: pass
      what: >
        Vhagar on-stage check (cond-dragon-proximity-122ac: "dragons backgrounded with instrumental
        pressure; not on-stage as scene partners")
      why: >
        Vhagar appears only in event_map metadata tags and in the grounding mechanism of the thermal
        backwash. No bone SVO places Vhagar on-stage as an actor. The dragon's presence is the feed-
        degradation effect, read from outside the dead-zone. PASS.

    - id: pass-011
      type: pass
      what: >
        Interiority-in-bone check: no thought, intent, feeling, or perception in any bone SVO
      why: >
        All axes_held rationales route interiority to that field (not the SVO). SVOs are physical
        actions or environmental events. n12 ("returns the feed to routine scan density") is a
        physical feed-management act, not interiority. n07 S03 ("exhales one breath above the feed")
        is a physical act. PASS on primary interiority check. Note: `above the feed` in n07 is a
        prepositional MODIFIER (flagged implicitly by the modifier-scan but not elevated to fault
        given the clean intransitive exhale verb and the minimal padding).

  # ─── ROUTING DIRECTIVE FOR FIXER ─────────────────────────────────────────
  fixer_routing_directive: |
    CRITICAL: Any FAULT-FORM recast on the concreteness-watch bones (S03 figure-ground contrast
    n03/n04/n05; S04 ledger-acts n05/n08) MUST PRESERVE the concrete physical content. Do NOT let
    form-fixing abstract the event away (the c03 contamination lesson; pl-2026-06-04-c15-001 watch).

    Per-bone guidance:
    - fault-005 (s03n03 negation + modifier): split into two positive-SVO bones preserving the
      fringe-returns-interference / gap-returns-silence figure-ground contrast. The silence is what
      the lane DOES, not what it fails to do.
    - fault-006 (s03n04 modifier + holds-license): recast preserves gap-as-physical-feed-event;
      removes `clean`/`noisy` adjectives; replaces `holds a clean window` with a transitive verb
      whose object is a concrete feed-datum (not an abstract window). The relational_anchor_status
      +2 move stays on the bone that names the gap as a physical feed-event.
    - fault-007 (s03n05 stative + simile): recast preserves the gap-boundary's perceptual
      distinctiveness as a feed-output event; removes the simile entirely (simile content routes
      to narrator-interest or metaphor facet citing this bone); uses an action verb with the feed
      or boundary as subject.
    - fault-008 (s04n08 stative + negation): recast preserves the blank name-field as a physical
      surface state; uses a positive SVO that names what the record DOES (or what the surface
      holds physically). Do NOT replace with a drawn conclusion ("she chose not to name it").
    - fault-003 (s01n08 holds-license + modifier): recast names the physical action of the arm/
      blade position at Vhagar-clearance height; no abstract weight-holding; concrete physical
      object and action.

    For fault-010 (Aemond age): this is a showrunner decision (cross-document resolution), not a
    fixer recast. Fixer should not attempt to resolve the age conflict independently. Flag to
    showrunner for decision before flat-file emission at Phase 7.
```
