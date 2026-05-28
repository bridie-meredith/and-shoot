```yaml
audit:
  scope: chapter
  target: b01c05
  timestamp: 2026-05-28
  context: >
    /and-write b01c05 revise --from-signals Phase 5 continuity audit (second
    fork). Scope: 5 new bones (A1, B1, B2, B3, C1) integrated into the
    existing 31-bone scaffold. Existing bones 1-31 pre-cleared Phase 5 at
    original /and-write. Audit checks the integrated chapter for continuity
    faults introduced by the additions only, across FAULT-REACHABILITY,
    FAULT-STATE, FAULT-REFERENCE, FAULT-POV, and FAULT-HANDOFF-IN-MISMATCH
    axes.
  findings:

    - id: fault-001
      type: fault
      what: >
        B2 SVO "the enforcement-report enters the jarvis-channel" — "the
        jarvis-channel" used as a named routing-apparatus object. No prior
        bones file (b01c01-c04), handoff_in/out, substance note, or warehouse
        card has coined "the jarvis-channel" as a distinct named channel-object.
        Prior chapters use "routing through Jarvis," "Jarvis as structural
        vector," and "the Jarvis routing" — actor-referenced phrases, not a
        channel named as an autonomous apparatus.
      why: >
        A SVO referencing "the jarvis-channel" implies an established named
        entity that can be cited by /and-facets (state-env, loc-state, NI) and
        elaborated in prose at /and-stitch. No such entity exists in the
        project record. Downstream: facet authors have no anchor to validate
        channel-citations against; /and-review bones at the next revise cycle
        will surface FAULT-REFERENCE against the object. The cause-chain
        (courier beaten → report filed → jarvis-channel → sera-arrangement-file)
        cannot be made physically legible in prose if the channel itself is
        an unresolved reference.
      criteria: >
        The named object "the jarvis-channel" must resolve against an
        established entry before B2's insertion point. Acceptable paths: (a)
        revise B2's SVO to reference the already-established actor
        (jarvis-coin-kl-courier) or the mechanism already named in b01c04
        ("the Jarvis report" / "the courier channel" / "the Jarvis routing");
        (b) establish "the jarvis-channel" as a named object in a bone earlier
        in b01c05 (before B2's insertion point at after-@16); (c) add a
        warehouse card for the channel and establish it via a bone that
        precedes B2. No new warehouse card is required if the SVO is revised
        to resolve against the actor already established.

    - id: fault-002
      type: fault
      what: >
        B3 SVO "taylor-hebert-kl-122ac adds the jarvis-form to the
        sera-arrangement-file" — both "the jarvis-form" and
        "the sera-arrangement-file" are named as physical prop-objects with
        no prior grounding.
        (a) "the sera-arrangement-file": Sera's protection arrangement is
        established in series/book contracts and b01c03-c04 handoffs as a
        relational contract ("Sera's exposure: being managed; protection
        confirmed functional"). No bones file, handoff, warehouse card, or
        substance note has materialized this arrangement as a named physical
        file-object that Taylor handles.
        (b) "the jarvis-form": a Jarvis-format report document implied by B2's
        routing event. B2 establishes "the enforcement-report," not a distinct
        "jarvis-form." The "jarvis-form" is a new named object that is neither
        independently established nor derived from an object named in any
        prior chapter.
      why: >
        B3 introduces two unnamed prop-objects simultaneously, the second
        (sera-arrangement-file) without any prior-chapter license and the first
        (jarvis-form) without independent establishment in B2 itself. At
        /and-facets, state-env and loc-state facet authors must be able to
        cite the object against a bones anchor that names it; neither object
        has a bone that establishes it before B3 uses it. The "adds X to Y"
        SVO pattern (per b01c04s02n11 "adds the courier to the body-map"
        precedent) is formally valid, but both X and Y must independently
        resolve. Here neither does.
      criteria: >
        Before B3 can reference "the jarvis-form" and "the sera-arrangement-
        file," each must be independently established. Acceptable paths for
        each object: (a) establish "the jarvis-form" as a named object in B2
        or in a bone earlier in b01c05 before B3's insertion point; (b)
        establish "the sera-arrangement-file" as a named prop in a bone before
        B3, or replace it with a reference to an existing named object (e.g.,
        the report-sheet from b01c04s03 if that object recurs, or a generic
        "the filing record" that has prior grounding); (c) collapse B2/B3 into
        a single bone whose SVO references only already-established objects.
        Fixer determines minimum change. New warehouse prop cards may be
        required if the named objects are retained.

    - id: fault-003
      type: fault
      what: >
        B2 and B3 are inserted after @16 ("taylor-hebert-kl-122ac delivers the
        enforcement report-entry") and before @17 ("the three figures exit the
        alley-mouth") in s02. This places the full routing-and-filing chain
        (report enters channel; form added to arrangement-file) while the
        enforcement incident is still in progress — the alley-mouth is not yet
        cleared.
      why: >
        b01c04 establishes the Jarvis-delivery model: reports are prepared
        and handed to Jarvis at scheduled yard meetings (b01c04s01/s03), not
        transmitted in real-time during in-ward operations. The b01c05s02 chunk
        confirms Taylor is at the ward's far end and "begins the Jarvis report
        in the same register" — report-drafting during observation, not
        physical routing. Placing B2 ("enforcement-report enters the
        jarvis-channel") and B3 ("adds the jarvis-form to the
        sera-arrangement-file") before @17 compresses three sequential
        routing/filing acts (@16 → B2 → B3) into in-ward active time,
        contradicting the prior-established batch-report-and-hand-off
        mechanism. Taylor cannot have physically routed and filed a report
        while still observing an incident whose subjects have not yet left the
        scene. This is a temporal state inconsistency against the b01c04
        channel-delivery precedent.
      criteria: >
        B2 and B3 must be placed at a point in the sequence that is temporally
        consistent with b01c04's Jarvis-delivery model. If B2/B3 represent
        Taylor's in-ward internal logging (drafting, not delivery), their SVOs
        must reflect that distinction clearly — "enters the jarvis-channel"
        implies transmission, not drafting. If they represent the physical
        hand-off to Jarvis, they belong after the in-ward observation sequence
        is fully closed (at minimum after @19, or re-anchored to the s03
        evening-review scene where Taylor's post-action accounting runs and
        where the routing event would be temporally consistent with the Jarvis
        meeting model). Fixer determines minimum placement adjustment that
        preserves the cause-chain logic and is consistent with the b01c04
        delivery precedent.

    - id: flag-001
      type: flag
      what: >
        A1 "the insect-feed returns the courier" inserted immediately after @8
        "the courier enters the lane-mouth" — the third-morning recurrence
        event risks reading as a restatement of @8 rather than a distinct
        prior-encounter confirmation.
      why: >
        The Phase 4 amendment justifies "returns the courier" as the feed
        surfacing the courier's body in coverage on the third morning (parallel
        to @13 "the side-alley returns the sound"). The structural logic is
        sound. However, because A1 immediately follows @8 ("the courier enters
        the lane-mouth"), a first-pass reader of the integrated bones may
        interpret A1 as the feed registering the same entrance event rather
        than confirming a pre-existing three-morning recognition pattern. The
        cf-d10-courier-face thread depends on the recurrence being legible as
        accumulated history, not same-moment registration. No blocking
        downstream consequence; /and-facets NI and memory facets can carry the
        disambiguation. Non-blocking advisory.
      criteria: null

    - id: pass-001
      type: pass
      what: >
        B1 "the courier raises the spine" — POV-license check.
      why: >
        The courier is the acting subject; Taylor is the observing narrator-
        witness. SVO pattern is consistent with established chapter bones
        (e.g., @13 "the side-alley returns the sound," @8 "the courier enters
        the lane-mouth," @10 "the three figures enter the side-alley"). The
        SVO names the external acting entity, not a Taylor perception-verb or
        interiority marker. POV-clean. No fault.
      criteria: null

    - id: pass-002
      type: pass
      what: >
        C1 "the rushwick-feed holds the color" — referent resolution for
        "the color" and "the rushwick-feed."
      why: >
        "The rushwick-feed" is established at @23 in the existing bones.
        "The color" is established within b01c05's own s03 substance notes,
        chunk text ("the color has arrived in the feed"), and political_
        register-prot axis notes ("the discipline's real-time categorization
        frame was holding neutral-instrumentally-observant in acquisition but
        the substrate was not neutral"). C1 inserts before @25 in s03, the
        same scene where the color event is established. Within-chapter
        establishment is sufficient for SVO reference; the concept need not
        precede the chapter. "Holds" is licensed by @29 ("the provisioner-
        train holds the rushwick-pass") and @31 ("the courier-walk holds the
        rushwick-pass"). Referent and verb form: clean. No fault.
      criteria: null

    - id: pass-003
      type: pass
      what: >
        FAULT-REACHABILITY check — chapter goal delivery under the integrated
        36-bone scaffold.
      why: >
        Goal: "Show the audience the moment the insect-feed stops being neutral
        — the color arrives before Taylor names it — and plant the courier
        figure whose face will matter at d10." The political_register-prot
        +1.5 axis move lands at s03n06 (@25), which is unaffected by the new
        bones. C1 (before @25) strengthens the mechanism leading to the
        recognition without displacing the recognition bone. A1/B1 strengthen
        the cf-d10-courier-face thread. Goal: deliverable. No reachability
        fault introduced.
      criteria: null

    - id: pass-004
      type: pass
      what: >
        Handoff_out integrity — required thread elements under the integrated
        bones.
      why: >
        political_register-prot rank 2.5: axis move at @25 unaffected by
        additions — clean. cf-d10-courier-face thread: A1 and B1 strengthen
        the anchor — clean. Faction-violence first incident logged: B2/B3
        add the routing chain (subject to fault-001/002/003 corrections on
        object naming, not on thread existence). Wren: absent from all 5 new
        bones — anchor rank 2 unchanged, no leakage. Position-world rank 6:
        no new bone carries a position-world axis move; all 5 are axes_held
        or chatter+cl-d05 — unchanged. No inadvertent axis shifts from any
        of the 5 new bones.
      criteria: null

    - id: pass-005
      type: pass
      what: >
        Handoff_in thread consistency — b01c04.handoff_out → b01c05.handoff_in
        threads against the integrated bones.
      why: >
        "Flea Bottom intelligence layer: routing to Otto through Jarvis":
        B2/B3 make this physical for the first time in c05's bones —
        directionally consistent with the thread (object-naming corrections
        per fault-001/002 do not affect thread direction). "Sera's exposure:
        managed": B3 references the arrangement — directionally consistent
        (naming correction per fault-002 does not affect thread presence).
        "Wren: in expanded coverage map; anchor rank 2": Wren absent from all
        5 bones — clean. "Position-world rank 6" and all other handoff_in
        world/character state values: unaffected by the additions. No
        handoff-in mismatch introduced beyond what is captured in the fault
        findings above.
      criteria: null

  verdict: FINDINGS-PRESENT
  summary: >
    3 faults, 1 flag, 5 pass entries. Faults are FAULT-REFERENCE ×2
    (fault-001: "the jarvis-channel" unresolved; fault-002: "the jarvis-form"
    and "the sera-arrangement-file" both unresolved as named prop-objects) and
    FAULT-STATE ×1 (fault-003: B2/B3 temporal placement before @17 contradicts
    the b01c04 Jarvis-delivery model). All three faults are in the B2/B3 cluster
    (SITE B). SITE A (A1) and SITE C (C1) are clean. Flag-001 on A1 is
    non-blocking. Fixer scope: SITE B only; SITE A and SITE C require no
    correction.
```
