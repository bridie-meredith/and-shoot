```yaml
# === CYCLE 2 (current) ===

audit:
  scope: season
  target: s01
  cycle: 2
  timestamp: 2026-05-11
  pass: S1 — Constraint audit (season scope), re-fire after fixer cycle 1
  verdict: FAIL
  findings:

    - id: fault-001
      type: fault
      what: >
        UNRESOLVED FROM CYCLE 1. Non-monotonic ID placement persists throughout
        s01.bones.md. In addition, all nine new bones added by screen-writer
        (509–517) are also placed at non-monotonic positions: 517 appears
        between IDs 57 and 58 (file line 69); 511 and 512 appear between IDs
        158 and 159 (file lines 196–197); 516 appears between IDs 152 and 153
        (file line 187); 509 appears between IDs 195 and 199 (file line 239);
        510 appears between IDs 500–502 and 205 (file line 252); 513, 514, 515
        appear between time-skip 329 and bone 330 (file lines 396–398). The
        original non-monotonic placements (IDs 495, 496, 497, 498, 499, 500,
        501, 502, 503, 504, 505, 506, 507, 508) are also unresolved.
        Total non-monotonic insertions: at least 23 distinct out-of-order IDs
        embedded across the file.
      why: >
        The proto-line schema mandates "monotonic positive integer, file-scoped."
        Phase 4 episode-boundary computation by aggregate_range arithmetic and
        any ID-order assumption in the split logic remain broken. New bones added
        by screen-writer replicate the same violation, compounding the fault
        rather than holding for a bulk-reorder fix.
      criteria: >
        All bones in s01.bones.md must appear in strictly ascending ID order
        in the file. Every late-inserted ID (495–517) must be placed at its
        correct narrative position while retaining its assigned ID. File-order
        must equal ID-order throughout.

    - id: fault-002
      type: fault
      what: >
        UNRESOLVED FROM CYCLE 1. Bones 111, 128, 129, 506 still use subject
        "the maester" instead of actor slug oc-broken-maester. Additionally,
        bones 285 and 286 — not named in cycle-1 fault-002 but present in the
        file at cycle 1 — also use "the maester": bone 285 reads "the visitor
        speaks to the maester" (listener form) and bone 286 reads "the maester
        speaks to the visitor" (subject form). All six instances name the same
        registered cast member (oc-broken-maester, eastern-quarter apothecary
        upper room) under the wrong token.
      why: >
        Cast members must appear under their actor slug. Slug-grep at Phase 4
        split time computes the cast: header field for each episode; "the
        maester" will not match oc-broken-maester's slug, producing an incorrect
        cast list for the episodes covering beats 7–8 and beat 15. The
        cite-index DAG for dialogue and narrator facets authored against these
        bones will not resolve back to the registered actor.
      criteria: >
        Bones 111, 128, 129, 285 (listener position), 286, and 506 must use
        the actor slug oc-broken-maester. In bone 285 the listener "the maester"
        must become oc-broken-maester. All six instances must be consistent with
        every other oc-broken-maester appearance in the file.

    - id: fault-003
      type: fault
      what: >
        UNRESOLVED FROM CYCLE 1. Bone 129: "the maester speaks" — bare
        intransitive speaks with no listener. File line 158. Unchanged since
        cycle 1.
      why: >
        The dialogue proto-line form requires "<speaker-slug> speaks to
        <listener-slug-or-group>". A bare "speaks" with no listener cannot
        anchor a dialogue-file entry; the dialogue schema requires the listener.
        The cond-clinical-self-erasure requirement for at least one s1-or-early-s2
        scene where Taylor hears the broken maester through the network cannot be
        demonstrated by facet citation if this proto-line has no listener to root
        the relay chain.
      criteria: >
        Bone 129 must specify a listener: "oc-broken-maester speaks to the room"
        if the target is diffuse, or a specific actor slug if identifiable. The
        subject correction per fault-002 is a co-requirement.

    - id: fault-004
      type: fault
      what: >
        NEW. Bone 515: "taylor-hebert-flea-bottom writes the entry." This bone
        was added by screen-writer in the 509–517 batch. It appears between
        time-skip ID 329 and bone 330 (file lines 396–398), without a paired
        "opens the log" bone preceding it or a "closes the log" bone following
        it. The immediately prior complete log-cluster is bones 326–328
        (open→write→close). Bone 515 is a bare write with no framing.
      why: >
        Every other log-write sequence in s01.bones.md follows the
        open → write → close pattern. A bare write implies the log was already
        open, but no preceding bone in the cluster opens it. The procedural
        texture of Taylor's research notation — mandated by cond-clinical-self-
        erasure — requires the physical act sequence to be complete. This is
        the identical structural fault as cycle-1 fault-003 (bone 109, now
        deleted). The screen-writer reintroduced the pattern in the new bones.
      criteria: >
        Bone 515 must either be preceded by an "opens the log" bone and followed
        by a "closes the log" bone (as new bones with new IDs above 517), or
        bone 515 must be removed if its write event is already carried by an
        adjacent complete log-cluster.

    - id: fault-005
      type: fault
      what: >
        NEW (scope expansion of cycle-1 fault-006). Two additional abstraction-
        as-object relay bones not addressed by the cycle-1 fix pass:
        (a) Bone 190: "the wasps relay the Fish Gate margin traffic." Object is
        "the Fish Gate margin traffic" — traffic is a collective event-abstraction,
        not a physical entity, location, or sound-event.
        (b) Bone 238: "the flies relay the alley event." Object is "the alley
        event" — an event abstraction (the eviction described in bones 232–236),
        not a physical entity or location noun.
      why: >
        The proto-line schema bars abstraction-as-object: "A physical verb whose
        object is an abstract noun is a thought-figure, not an event. Faults
        FAULT-FORM-INTERIORITY." The insect-relay bones in this file consistently
        use location-nouns or entity-slugs as objects (the Watch position,
        oc-dock-runner, the south-wall footfall, the door lintel, oc-tanner-elder,
        the clerk). "Traffic" and "the alley event" are activity-abstractions.
        They name what Taylor infers from the relay, not what the insects
        physically transmit. The distinction preserves the contemplative-procedural
        register required by cond-series-tone-constraints-125ac.
      criteria: >
        Bone 190 must identify the physical thing being relayed: a named entity
        in the Fish Gate margin, a sound-event (footfall, voice-register), or
        the location itself. Bone 238 must identify the physical relay anchor:
        the door (being broken), an entity present (the lords-man's man, the
        tenant family), or a sound-event — not "the alley event" as an
        abstraction.

    - id: flag-001
      type: flag
      what: >
        CARRIED FROM CYCLE 1. Bone 318: "oc-tanner-mother sits." Ambiguous
        between stative position-naming (deny-listed) and the discrete act of
        taking a seat (passes). Context (bone 317: enters the base room; bone
        319: taylor faces oc-tanner-mother) suggests act, not state, but the
        bone is ambiguous.
      why: >
        If rendered as stative, faults FAULT-FORM-NON-ACTION-VERB. No downstream
        structural consequence if intent is the act. Editor should confirm.

    - id: flag-002
      type: flag
      what: >
        CARRIED FROM CYCLE 1. Bones 178 and 179: "oc-tanner-mother pivots toward
        the road south" and "oc-tanner-father pivots toward the road south."
        "The road south" is a directional compound, not a named entity or
        registered location slug.
      why: >
        The schema bans prepositional padding and modifier-phrases. "The road
        south" may read as a directional modifier applied to "the road." The
        canonical form would be "the south road" as a named environment element,
        or a location slug if one is registered in the warehouse. Advisory for
        fixer or Phase 4 split.

    - id: flag-003
      type: flag
      what: >
        CARRIED FROM CYCLE 1. Bones 49, 50, 56, 57, 86: verb "routes" used as
        a causative-direction verb (oc-tanner-father routes oc-tanner-mother /
        the neighbor-boy; oc-tanner-elder routes taylor-hebert-flea-bottom).
      why: >
        "Routes" implies the object's movement as a consequence of the subject's
        internal decision — borderline interiority-attribution. Not a schema-
        enumerated fault but creates facet-authoring ambiguity. Advisory.

    - id: flag-004
      type: flag
      what: >
        CARRIED FROM CYCLE 1. Bone 507: "taylor-hebert-flea-bottom faces the Red
        Keep." loc-red-keep-outer-ring is a registered warehouse location card.
        "The Red Keep" approximates but does not match the slug.
      why: >
        Phase 4 slug-grep for locations: field will not capture "the Red Keep"
        as a reference to loc-red-keep-outer-ring. Low consequence for one
        facing-action bone but inconsistent with slug-discipline.

    - id: flag-005
      type: flag
      what: >
        NEW. Bones 338 and 339 are consecutive and identical: both read
        "the flies relay the clerk." These are two distinct IDs with the same
        subject, verb, and object in sequence.
      why: >
        May be an intentional double-relay (the flies register the clerk twice
        as they track movement through two positions) or a duplicate that
        survived the cycle-1 duplicate-pair deletion pass. If a duplicate, the
        two bones share the same logical beat and one should be deleted. If
        intentional, no action needed. Advisory for screen-writer to confirm
        intent.

    - id: flag-006
      type: flag
      what: >
        POLICY CARRY-FORWARD. "Walks-the-path" form: bones 28, 30, 91, 92, 98,
        105, 110, 118, 222, 270, 351, 445, 479, 481, 483, 485, 489 — 17 total
        instances of "taylor-hebert-flea-bottom walks the <path-or-perimeter>"
        and two instances using other subjects (oc-tanner-elder walks the road,
        bone 91). Cycle-1 fault-005 raised this as an 11-instance structural
        fault. The policy decision documented between cycles accepted
        "walks the <path>" as a defensible idiom parallel to "enters the yard"
        and declined to fault it.
      why: >
        Documenting the policy decision in the audit record so subsequent passes
        do not re-raise this as a fresh fault. If the policy is reversed, all
        ~17 instances require recast. The new bones (477–489) add five additional
        instances of the form in the denouement walk sequence; the idiom is now
        load-bearing in the season-close beat 26 bones. Reversal at that stage
        would require splitting each walk into entry + traversal pairs.

    - id: flag-007
      type: flag
      what: >
        CARRIED FROM CYCLE 1 (formerly flag-006). cond-clinical-self-erasure
        requires at least one s1-or-early-s2 scene where Taylor hears the broken
        maester through the network and adjusts behavior in response. Bone 112
        carries the physical relay of maester-speech; bone 131 (straightens the
        spine) is the nearest behavioral-adjustment candidate. No bone explicitly
        marks behavioral consequence triggered by the maester's speech.
      why: >
        The facet layer (narrator, memory) must anchor the adjustment to a bone.
        If bone 131 is the intended consequence beat, its causal link to bones
        112/129 must be confirmed for facet authoring. Advisory.

    - id: flag-008
      type: flag
      what: >
        CARRIED FROM CYCLE 1 (formerly flag-007). Range-expansion threshold-
        events (bones 209–221, 266–269, 344–347, 438–444) show territorial
        spread but no bone records Taylor's proprioceptive awareness of the new
        edge. cond-fauna-control-rules-125ac-addendum requires this registration
        as "not a quiet background process."
      why: >
        The log-write clusters (e.g., bones 228–230, 276–278) may carry the
        threshold registration at facet level, but the bone layer has no anchor
        for the proprioceptive moment. Advisory for facet authoring.

    - id: flag-009
      type: flag
      what: >
        CARRIED FROM CYCLE 1 (formerly flag-008). Fish Gate margin surviving
        subject (s4 constraint) forward-note. S01 bones do not violate this;
        the spatial infrastructure is established. No s01 fault.
      why: >
        Advisory for s02–s03 planning: when the surviving subject is introduced
        in the Fish Gate margin, they must appear in insect-relay bones without
        appearing in Taylor's log-write sequences.

## Cycle 2 fault resolution summary

| Cycle-1 ID  | Status in cycle 2                                                   |
|-------------|----------------------------------------------------------------------|
| fault-001   | UNRESOLVED — non-monotonic placement persists; 9 new bones compound it |
| fault-002   | UNRESOLVED — "the maester" slug persists at bones 111, 128, 129, 506; scope expands to include bones 285/286 |
| fault-003   | RESOLVED — bone 109 deleted; gap at 108→110 confirmed               |
| fault-004   | UNRESOLVED — bone 129 "speaks" still bare, no listener              |
| fault-005   | POLICY DECISION — "walks the <path>" accepted as idiom; carried as flag-006 |
| fault-006   | PARTIALLY RESOLVED — bone 187 recast to "the flies relay oc-tanner-elder"; bones 190 and 238 not addressed; raised as new fault-005 in cycle 2 |
| flag-001    | CARRIED                                                              |
| flag-002    | CARRIED                                                              |
| flag-003    | CARRIED                                                              |
| flag-004    | CARRIED                                                              |
| flag-005    | CARRIED                                                              |
| flag-006    | CARRIED                                                              |
| flag-007    | CARRIED                                                              |
| flag-008    | CARRIED                                                              |

New cycle-2 faults: fault-004 (bone 515 bare write), fault-005 (bones 190/238 abstraction-as-object relay).
New cycle-2 flags: flag-005 (bones 338/339 potential duplicate), flag-006 (walks-the-path policy carry).

VERDICT: FAIL
```

---

# === CYCLE 1 (archived) ===

```yaml
audit:
  scope: season
  target: s01
  cycle: 1
  timestamp: 2026-05-11
  pass: S1 — Constraint audit (season scope)
  verdict: FAIL
  findings:

    - id: fault-001
      type: fault
      what: >
        s01.bones.md — IDs 495, 504 appear between bones 84 and 86;
        ID 506 appears between bones 131 and 132; ID 496 appears between
        bones 298 and 299; ID 497 appears between bones 356 and 357;
        ID 503 appears between bones 417 and 420; IDs 498, 499 appear
        between bones 450 and 451; ID 507 appears after bone 453; IDs 500,
        508, 501, 502 appear interleaved between bones 202 and 205.
        In total, fourteen high-range IDs (495–508) are embedded at
        non-monotonic positions within the lower-ID sequence.
      why: >
        The proto-line schema mandates "monotonic positive integer, file-scoped"
        (schemas/proto-line.schema.md). Monotonicity means each bone's ID must
        exceed all preceding IDs in file order. The current file violates this
        in at least eight distinct locations. The stitcher's citation-order walk
        is the nominal consumer, not file order — but the schema's stability and
        monotonicity rules exist so that aggregate_range arithmetic and Phase 4
        split logic remain deterministic. Non-monotonic placement of late-added
        IDs means Phase 4 cannot reliably compute episode boundaries by
        ID-range, and any tool that assumes ID order approximates narrative
        order will misplace these beats.
      criteria: >
        All bones in s01.bones.md must appear in strictly ascending ID order in
        the file. Late-inserted bones with IDs 495–508 must be placed at their
        correct narrative positions while retaining their IDs (schema prohibits
        renumbering). File-order must be ID-order throughout.

    - id: fault-002
      type: fault
      what: >
        Bones 111, 128, 129, 506 use subject "the maester"; bones 305, 306,
        309, 310, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411,
        412, 413, 414, 415 use subject "oc-broken-maester". The character is
        identical (the same Citadel-chain-stripped maester in the eastern-quarter
        apothecary upper room, per season-plan beat 7 / beat 16). Two different
        subject tokens are used for the same cast member within the same file.
      why: >
        The proto-line schema requires the subject to be "a named entity — actor
        slug, prop slug, or `the <noun>` for unnamed environment elements."
        oc-broken-maester is a registered cast member (cast_roster in
        showrunner/memory.md). Cast members must appear under their actor slug,
        not under a bare-noun form. Using "the maester" as subject for a
        registered cast member is a slug-resolution fault: the stitcher,
        Phase 4 split logic, and any cast: field computed by slug-grep will
        miss this character's appearances in the early-season bones, producing
        an incorrect cast list for the episodes covering beats 7–8.
        Cross-stretch consequence: facet authoring (dialogue, narrator, memory)
        against bones 111, 128, 129, 506 will author against "the maester" and
        will not cite back to oc-broken-maester's dialogue file, breaking the
        cite-index DAG.
      criteria: >
        Bones 111, 128, 129, 506 must use the actor slug oc-broken-maester as
        subject, consistent with all other appearances of this character in
        s01.bones.md.

    - id: fault-003
      type: fault
      what: >
        Bone 109: `taylor-hebert-flea-bottom writes the entry` appears as a
        standalone write between bones 105 and 110 without a paired
        `opens the log` / `closes the log` framing. All other log-write
        sequences in the file follow the open → write → close pattern
        (e.g., bones 101–103, 114–116, 124–126, 132–134, 153–155, etc.).
        Bone 109 is the sole bare write without its framing pair.
      why: >
        The open/close framing is the established physical-act sequence for
        Taylor's research notation throughout s01. A bare write without open
        or close implies the log was already open from a prior beat — but
        no preceding bone in this cluster (105–108) opens the log. The stitcher
        would render this beat as Taylor writing without the physical act of
        opening the log, inconsistent with the procedural texture that
        cond-clinical-self-erasure mandates ("the procedure of Taylor's
        research — observation, hypothesis, test, notation, revision — is the
        story's primary mechanism"). The omission also breaks the parallelism
        that facet authors use to identify research-notation moments in this
        episode.
      criteria: >
        Bone 109 must either (a) be preceded by an `opens the log` bone and
        followed by a `closes the log` bone, or (b) be removed if the write
        event is already covered by the bones 114–116 cluster in the same
        scene-block.

    - id: fault-004
      type: fault
      what: >
        Bone 129: `the maester speaks` — bare intransitive `speaks` with no
        listener. The proto-line schema specifies that for dialogue beats,
        the canonical form is `<speaker-slug> speaks to <listener-slug-or-group>`.
        "the maester speaks" has no `to <listener>` complement and uses the
        unnamed-entity subject form (already faulted in fault-002, but the form
        violation is independent). Bone 506: `the maester laughs` — not a
        dialogue-form issue, but the same unnamed-subject issue applies.
      why: >
        A bare `speaks` without a listener cannot anchor a dialogue-file entry.
        The dialogue schema requires the proto-line to identify the listener;
        "speaks to the room" is the licensed form when the target is diffuse
        (per season-plan beat context: the maester is speaking in his upper room,
        audience unclear). Without the listener, no dialogue facet can be authored
        against this bone with correct form. The stitcher cannot route spoken
        content to a per-character dialogue file entry. Cross-stretch consequence:
        if the maester's first overheard speech (season-plan beat 7 / beat 8
        cross-reference) is not anchored to a dialogue entry, the requirement
        in cond-clinical-self-erasure ("at least one s1-or-early-s2 scene where
        Taylor hears the broken maester through the network") cannot be
        demonstrated by facet citation.
      criteria: >
        Bone 129 must specify a listener: `oc-broken-maester speaks to the room`
        (if diffuse) or a specific actor slug if the target is identifiable.
        The subject must be corrected to oc-broken-maester per fault-002 criteria.

    - id: fault-005
      type: fault
      what: >
        Bones 28 and 30: `taylor-hebert-flea-bottom walks the yard boundary`.
        Bones 98, 105, 110, 222, 270, 351, 445: `taylor-hebert-flea-bottom
        walks the perimeter`. Bones 479, 481, 483, 485, 489:
        `taylor-hebert-flea-bottom walks the [first alley / south alley /
        Fish Gate margin / south-wall colony / eastern-quarter approach]`.
        In all cases, `walks` takes a path-noun or perimeter-noun as direct
        object. The proto-line schema requires intransitive motion verbs to
        fault FAULT-FORM-NO-VERB ("taylor moves is not observable"), and
        bars prepositional padding. `walks the <path>` uses `walks` as a
        traversal verb whose object is the path traversed — not a destination.
        The canonical destination-verb form is `enters <location>`.
      why: >
        The schema's no-destination-motion rule is: "bare intransitive motion
        verbs without destination fault FAULT-FORM-NO-VERB." `walks` is the
        primary offender. The perimeter/alley/margin objects are paths, not
        destinations. The schema's bar on prepositional phrases of place /
        destination / direction covers the prepositional sense embedded in
        `walks the perimeter` (walking along the perimeter = walking through /
        around a place, which is the prepositional form rendered as transitive
        padding). The repeated use of this form (11 instances) across the full
        season establishes it as a structural pattern rather than an isolated
        slip. The stitcher's rendering of `walks the perimeter` as a discrete
        SVO event is ambiguous — it cannot be cleanly rendered as a single
        physical action that an observer would see.
      criteria: >
        Each `walks the <path>` bone must be recast as a verb that names the
        discrete observable act: `crosses`, `enters`, or (where traversal of a
        boundary is the act) a split into entry + traversal as separate bones.
        The object must be a destination or an entity that the verb acts on
        as a direct physical object, not a path-noun.

    - id: fault-006
      type: fault
      what: >
        Bone 187: `the flies relay the junction conversation`. The object "the
        junction conversation" is an abstraction — a conversation is an event,
        not a physical object that insects relay. The proto-line schema prohibits
        abstraction-as-object: "A physical verb whose object is an abstract noun
        is a thought-figure, not an event. Faults FAULT-FORM-INTERIORITY."
      why: >
        Insect-relay bones in this file consistently use location-nouns as object
        (`the flies relay the Watch position`, `the flies relay oc-dock-runner`,
        `the beetles relay the south-wall footfall`). "The junction conversation"
        is not a location or an entity; it is an event. The flies cannot relay
        an event; they relay sensory data that constitutes evidence of the event.
        The abstraction introduces an interiority-contaminated object into a
        bone that must be pure physical action. The distinction matters for the
        contemplative-procedural-horror register (cond-series-tone-constraints-125ac):
        the bone should show the physical relay act, leaving the inference of
        "conversation" to a facet.
      criteria: >
        Bone 187 must identify the physical thing being relayed — a location
        (the junction), an entity present at the junction, or a sound-event
        (footfall, voice-register) — not the conversation as an abstraction.

    - id: flag-001
      type: flag
      what: >
        Bone 318: `oc-tanner-mother sits`. `sits` in the schema's non-action
        deny-list context: "stative position-naming: `sits` describing position
        not posture-act (`taylor stands at the door` faults; `taylor stands`
        as the discrete act of rising from sitting passes)." The schema allows
        `sits` if it means the discrete act of taking a seat. In context (bone
        317: oc-tanner-mother enters the base room; bone 319: taylor-hebert-flea-bottom
        faces oc-tanner-mother), bone 318 is positioned as the entry action,
        suggesting it means "takes a seat" rather than "is seated." Ambiguous.
      why: >
        If `sits` is read as stative, it is FAULT-FORM-NON-ACTION-VERB. If read
        as the discrete sitting-down act, it passes. Editor should verify intent.
        No downstream structural consequence.

    - id: flag-002
      type: flag
      what: >
        Bones 178 and 179: `oc-tanner-mother pivots toward the road south` and
        `oc-tanner-father pivots toward the road south`. The schema licenses
        `pivots toward <X>` when motion-in-progress is required. However,
        "the road south" is a directional phrase, not a named entity (actor
        slug, prop slug, or `the <noun>` for a countable environment element).
        "The road south" is a direction expressed as a path-noun compound with
        a cardinal modifier.
      why: >
        The schema's ban on prepositional padding and modifier-phrases could
        apply to `the road south` as a directional-modifier compound. The
        canonical form would be `the south road` (a named environment element)
        or, better, a location slug if one exists. No fault classification without
        confirming whether a south-road location slug is registered in the
        warehouse. Advisory for fixer or Phase 4 split.

    - id: flag-003
      type: flag
      what: >
        Bones 49, 50, 56, 57, 86: verb `routes` used for oc-tanner-father
        directing oc-tanner-mother, oc-tanner-father directing the neighbor-boy,
        and oc-tanner-elder directing taylor-hebert-flea-bottom. `routes` is not
        in the schema's deny-list but it is a causative-direction verb that
        implies the object's movement as a consequence of the subject's action.
        Causative constructions straddle the line between observable physical
        act (pointing, gesturing) and interiority-attribution (causing an internal
        decision in the object).
      why: >
        If the stitcher renders `routes` as "caused X to move," the bone
        attributes an internal compliance to the object-actor, which is interiority
        by implication. A bone like `oc-tanner-father points toward the yard`
        + a separate bone for the routed actor's movement would be cleaner.
        The pattern recurs five times. Not a schema-enumerated fault, but the
        verb's causative semantics create facet-authoring ambiguity. Advisory.

    - id: flag-004
      type: flag
      what: >
        Bone 507: `taylor-hebert-flea-bottom faces the Red Keep`. "The Red Keep"
        is used as a bare-noun environment element, but loc-red-keep-outer-ring
        is a registered warehouse location card (listed in stage_elements in
        showrunner/memory.md). The subject faces toward a named location, and
        that location has a canonical slug.
      why: >
        The schema requires prop slugs and location slugs to be used when they
        exist. "The Red Keep" as a bare-noun approximates loc-red-keep-outer-ring
        but is not the slug. Phase 4 slug-grep for cast: and locations: fields
        will not capture `the Red Keep` as a reference to loc-red-keep-outer-ring,
        potentially omitting the location from the per-episode header. Low
        consequence for a single facing-action bone, but advisory for consistency.

    - id: flag-005
      type: flag
      what: >
        The season-plan beat 6 states: "she maps her 300m radius in 48 hours
        and identifies the eastern-quarter apothecary's upper room as a surface
        worth watching." Bones 94–99 cover the entry to loc-flea-bottom and
        loc-flea-bottom-base. The initial 300m mapping across the full block
        (beats 6–7) is shown in bones 95–97 (flies/beetles/wasps spread
        immediate block / market-side junction / Fish Gate margin). However,
        no bone in this cluster shows the apothecary approach being included
        in the initial survey — the eastern-quarter approach first appears at
        bone 106 (beetles spread the eastern-quarter approach). This is consistent
        with the narrative sequence but the 48-hour mapping from beat 6 and the
        "apothecary identified" milestone are not clearly distinguished from the
        later network operations at bones 105–116. Minor structural ambiguity
        about when the apothecary identification beat lands.
      why: >
        Potential partial bullet-to-bone drift for season-plan beat 6. Not a
        fault because the identification may be intended to emerge across the
        105–116 cluster rather than at the 95–97 cluster. Advisory for Phase 7
        episode-boundary placement: if the 48-hour mapping and apothecary
        identification are supposed to land in the same episode, the bone
        sequencing supports placing bones 94–116 in one episode.

    - id: flag-006
      type: flag
      what: >
        cond-clinical-self-erasure requires the prose to show "at least one
        s1-or-early-s2 scene where Taylor hears the broken maester through the
        network (fragment overheard, behavioral read-through, or direct adjacency)
        and adjusts her behavior in response." At bone level, bone 112 shows
        `the beetles relay the sound` (the maester speaking, per bones 111/129)
        and bone 113 shows `taylor-hebert-flea-bottom writes the entry`.
        The physical relay of maester-speech exists. However, no bone shows
        Taylor adjusting behavior in response — bone 113 (writes entry) and
        bone 131 (straightens spine) are the closest candidates, but neither
        is clearly a behavioral adjustment triggered by the maester's speech.
      why: >
        The cond-clinical-self-erasure requirement is a prose-level check that
        cannot be fully evaluated at bone level; the facet layer (narrator, memory)
        carries the adjustment. But if no bone records a behavioral consequence
        of hearing the maester, the facet layer has nothing to cite. The bone
        `taylor-hebert-flea-bottom straightens the spine` (bone 131) may be
        the intended behavioral-adjustment beat. If so, its position (between
        the maester relay and the log-write) should be confirmed as intentional
        consequence, not coincidental placement. Advisory for facet authoring.

    - id: flag-007
      type: flag
      what: >
        Range expansion across s01 bones: bones 95–97 show initial spread
        covering immediate block, market-side junction, Fish Gate margin (implies
        ~250–300m from the loc-flea-bottom-base reference point). Bones 209–221
        show overnight network expansion (flies spread northern block, wasps
        spread eastern-quarter adjacent — new territory). Bones 266–269 show
        autumn-density expansion (flies spread autumn-density network, wasps
        spread dock-side relay, spiders spread eastern-quarter relay). Bones
        344–347 show winter-onset expansion (flies/wasps/beetles/spiders across
        wider set). Bones 438–441, 444 show final expansion (overnight network,
        Fish Gate margin, south-wall colony, eastern-quarter relay, south-wall
        perimeter). The progression is visible in bones but no bone explicitly
        marks a threshold-event for the physiological cost registration required
        by cond-fauna-control-rules-125ac-addendum ("range expansion is organic
        and legible to the audience... Range expansion is not a quiet background
        process").
      why: >
        The addendum requires range expansion to be "registered in the prose"
        through scenes where Taylor reaches something she could not reach before.
        The bones show the territorial spread but do not include a bone recording
        Taylor's proprioceptive awareness of the new edge (which the addendum
        mandates: "Taylor knows her range precisely at all times"). Season-plan
        beats 11, 14, 19, 24 specify log entries at each expansion threshold.
        Bones 228–230 (writes entry after overnight operation) and similar
        write-clusters may carry this — but no bone specifically marks the
        threshold-event proprioception. Advisory: facet layer (narrator-mode,
        state-update) must ensure each expansion event is registered, with bones
        available to anchor it.

    - id: flag-008
      type: flag
      what: >
        cond-clinical-self-erasure requires the Fish Gate margin surviving
        subject (from s4) to appear in Taylor's surveillance network but not
        in her log, in at least one scene before s4. This is an s4 constraint
        that pre-seeds in s3; it is not an s1 requirement. However, s01.bones.md
        covers the full season arc including the Fish Gate margin territory
        (bones 97, 119, 190, 215, 439, 462, 482, 483). The Fish Gate margin
        is consistently present in the insect-network coverage. No bone in s01
        introduces a specific unnamed individual in the Fish Gate margin who
        recurs without log acknowledgment.
      why: >
        Not a fault in s01 — the surviving-subject requirement activates in s3.
        However, the Fish Gate margin's consistent coverage across s01 means the
        spatial infrastructure for the pre-s4 surveillance / log-gap is
        established. Advisory for s02–s03 planning: when the surviving subject
        is introduced to the Fish Gate margin territory, they must appear in
        insect-relay bones without appearing in Taylor's log-write sequences.
        S01 bones do not violate this; forward-note only.
```
