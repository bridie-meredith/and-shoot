```yaml
audit:
  scope: season
  target: s01
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
