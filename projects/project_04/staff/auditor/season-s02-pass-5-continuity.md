```yaml
audit:
  scope: season
  target: s02
  pass: phase2-pass-5-continuity
  timestamp: 2026-05-10
  verdict: SEASON-CONTINUITY-OK
  finding_count: 7
  escalations: 0
  findings:

    # ─── SWEEP 1: REACHABILITY ───────────────────────────────────────────────

    - id: fault-001
      type: flag
      what: >
        Suppression tier at S2 close. Series-plan §6 suppression arc requires S2
        to close at "patterned-response" (not policy, not action). Season-plan §H
        explicitly states "S2 close must not overstate." The aggregate ends at bone
        1091 with Taylor passively logging the newcomer's arrival from the
        road-edge — no enforcement event, no directive closure. The reeve-summons
        in B5 (bones 848–922) is received and partially resisted but not resolved
        in a named terminal beat. The aggregate does not contain a bone or group
        of bones that commits the apparatus tier to "patterned-response" as the
        closing institutional state. The final 48 bones (1044–1091) are Taylor's
        exterior register on the newcomer; no bone names or implies the tier
        ceiling.
      why: >
        Without a closing-tier anchor the aggregate is compatible with both
        "patterned-response" (correct) and "policy-adjacent" (overstated). Phase 4
        split may assign B5's reeve-summons interaction as the tier-commit event,
        but no bone in the B5 block makes the distinction legible — the reeve
        draws the summons folio and exits (bone 921–922) without a bone showing
        what the summons did not accomplish (i.e., no formal enforcement issued,
        no name placed on a registry). This is a Phase 4 editorial risk, not a
        current structural hole, hence flag not fault.

    - id: fault-002
      type: pass
      what: >
        Season-start state traversal (s01 terminal handoff → S2 arc).
        Named open threads at s01 close: mira_recruitment (tacit), rowan_pastoral
        claim (active), clem_ferris_noticing (live), rymer_hedge_witness (present),
        family_in_concert (closed). Named terminal image: Taylor in loft, swarm-
        tracking sept fly + dock mosquito + ferry folio crossing water; Elara calls;
        Taylor presses loft floor.
        Aggregate opens (bones 1–7): Taylor descends loft, crosses workshop floor,
        reaches workshop shutter, plants feet. Bone 9–10: dock mosquito circles
        ferry planking, sept fly orbits baptismal basin. Bone 12–13: Elara speaks to
        Taylor, Taylor replies. Bone 40: Taylor presses the loft floor. All five
        named elements of the terminal image are present in bones 1–40 of the
        aggregate. Each open thread activates: Mira appears at market square bones
        48–52; Rowan is present at sept bones 813–831; Clem appears at bones
        342–350, 567–580; Rymer at bones 267–284, 644–723; family-in-concert
        (closed) correctly receives no re-opening.
      why: Reachability traversal confirmed. No gap.

    - id: fault-003
      type: pass
      what: >
        Season-end state (Mira dissolves market-day gatherings; newcomer arrives at
        sept; suppression at patterned-response). B6 interlude (bones 941–1040)
        delivers: Mira publicly dissolves gatherings in the market square (bones
        963–970) in front of the wool factor's cousin, fishwife, and town reeve.
        Newcomer arrives at the sept door (bones 1054–1082) and Septon Rowan
        receives her. Taylor's passive-sense logs the arrival from road-edge (bones
        1066–1087). Season-end state is reachable from the aggregate.
      why: Season-end state traversal confirmed. No gap.

    # ─── SWEEP 2: STATE ──────────────────────────────────────────────────────

    - id: fault-004
      type: fault
      what: >
        Pryor's quarterly report folio — ownership and handling coherence. The
        plan (§B B1) establishes the folio as carried by the ferryman or a rider
        on a fixed schedule, received by the town reeve. The aggregate presents
        multiple folio-bearing events:
        (a) B1: oc-lords-steward draws the folio at the dock (bone 57), hands it
            to the town reeve indirectly via rider (bones 170–179). Garrison
            captain then appears (bones 181–184) and takes the "sealed packet" —
            a distinct object from the folio. This is coherent.
        (b) B2: oc-lords-steward's rider crosses the far bank carrying folio
            (bones 383–406, 481–498). Town reeve takes the folio packet (bone 498).
            Coherent.
        (c) B4 (bones 762–785): oc-lords-steward reaches the ferry dock, draws the
            folio (bone 765), then draws "the sealed acknowledgment" (bone 769) and
            a "second folio" (bone 772). The oc-garrison-captain takes the second
            folio and marks the acknowledgment (bones 777–778). oc-lords-steward
            then boards the ferry gripping "the folio" (bone 784). Three folio-type
            objects are in play in bones 765–784 simultaneously: (1) the original
            report folio, (2) the sealed acknowledgment, (3) the second folio. The
            aggregate does not disambiguate which Pryor boards with. Season plan §B
            B4 specifies "the garrison captain acknowledge receipt by hand — a paper
            trail requiring a named military officer's signature." The acknowledgment
            should return with Rymer (who "carries the acknowledgment packet back"
            per plan). But in the aggregate, oc-lords-steward seals the
            acknowledgment himself (bone 780) and boards the ferry with it (bones
            782–785), while Rymer's B4 bones (644–728) show Rymer only traveling
            the road and logging the garrison waypost stop — Rymer does not carry a
            packet back. The plan's mechanism (Rymer carries the acknowledgment
            back) is not executed in the aggregate; oc-lords-steward carries the
            acknowledgment himself. This is a plan-vs-aggregate drift on the
            acknowledgment-courier mechanism.
      why: >
        The plan's B4 structural note ("Rymer Hedge, on courier duty for a
        day-trip between Fairstead and the garrison outpost, carries the
        acknowledgment packet back. He reads nothing; he delivers the packet; he is
        not in Pryor's coalition. But after the delivery Rymer's behavior shifts...")
        requires that Rymer's route causes his behavioral shift. If oc-lords-steward
        carries the acknowledgment himself, the causal link between Rymer's
        courier-duty and his behavioral anomaly is severed. The behavioral-anomaly
        logging of Rymer (bones 693–728) therefore lacks its causal anchor. The
        Rymer anomaly carry-forward (plan §H) will be ungrounded at S3 unless this
        mechanism is coherent.
      criteria: >
        The aggregate must establish a clear single carrier for the signed
        acknowledgment packet. If Rymer is to be the courier (per plan B4), bones
        in the B4 stretch must show Rymer carrying and delivering the acknowledgment
        packet, and the garrison-captain signing sequence (bones 777–780) must
        precede a handoff to Rymer rather than a direct seal-and-board by Pryor. If
        the aggregate writer has chosen to route the acknowledgment via Pryor
        directly, the causal chain for Rymer's behavioral anomaly requires a
        different anchor bone establishing why Rymer's road-behavior changed.

    - id: fault-005
      type: flag
      what: >
        Body-clock ceiling transition at B3. Season-plan §H states: "Child-body
        ceiling (~3/10/20-minute actor-card constraints) applies through Beat 2. The
        transition event at Beat 3 shifts the cost curve upward; the new ceiling
        applies from Beat 3 forward." The B3 segment (identified by the workshop-
        domestic-frame bones at approximately bones 507–632, including the extended
        fly-grid demonstration at bones 522–626) shows Taylor running an extended
        passive-sense grid that spans the workshop, market square, village common,
        and blue-fork road approach. Bones 542–559 show the flies tracing all three
        areas simultaneously in sequence. Bones 597–626 show an extended two-stretch
        grid hold covering the full road to the tributary bend. This is consistent
        with the plan's requirement that the transition be demonstrated through
        quiet operational shift ("insects work a grid they could not hold last
        autumn"). However: the aggregate contains no bone that marks which ceiling
        applies before vs. after the transition within B3 itself. The transition is
        implied by the extended hold but not committed as a discrete boundary event.
        Plan §H requires "the old ceiling was a hard wall Taylor could point to and
        hold; the new ceiling is a moving threshold." This is a flag, not a fault,
        because the operational shift is present — the absence is the naming.
      why: >
        Phase 3 voice-pass and Phase 4 split will need to know where the ceiling
        boundary falls within B3 to correctly differentiate pre-/post-transition
        active-control references in facets. If the boundary is implicit, the voice
        and vibe passes cannot cleanly distinguish the registers.

    - id: fault-006
      type: fault
      what: >
        Body-clock cost-register differentiation at B4 (plan requirement, bones
        593–729). Season-plan §B B4 structural note: "A response-bone must commit
        to differentiating this new cost-register from the pre-transition baseline:
        the reach Taylor now has (extended insect-grid coverage of the road
        corridor, sustained passive-sense through the garrison outpost's insect-
        wrong zone) is what makes the behavioral-delta logging possible, and the
        aggregate writer must show the difference between what the old ceiling would
        have returned and what the new ceiling returns here — not as exposition,
        but as a bone showing the physical cost of the extended hold." The B4 grid-
        hold sequence (bones 637–728) shows Taylor extending the flies to the
        garrison waypost and holding the perimeter arc (bones 664–677), sustaining
        through retreat and re-cover (bones 680–760). The hold is present and
        extended. However: no bone in this stretch shows the physical cost of the
        extended hold distinguishable from a pre-transition hold. The plan explicitly
        requires a cost-differentiation bone — one that shows what the hold does to
        Taylor's body at the new ceiling that the old ceiling would have foreclosed.
        Bones 679 ("presses the temple"), 691 ("presses the temple"), 718 ("presses
        the temple") appear, but "presses the temple" is Taylor's standard
        attentional gesture throughout the aggregate from bone 19 onward; it does
        not differentiate new-ceiling cost from old-ceiling cost. No bone in B4
        marks a distinct physical-cost shape (e.g., duration-of-hold, nosebleed
        analog, recovery time) that could not have been present in B2.
      why: >
        Plan §B and §H both name this as a carry-forward mandate with downstream
        season-wide consequence: "deformed proto-lines cannot be rescued by
        downstream facet skin" (bone-gate principle). The facets pass requires this
        differentiation to be in the bone; if absent, the B4 cost-register
        differentiation cannot be supplied at the facet layer. The worm-canon-pedant
        audience carry-forward flag (plan §H) explicitly names this requirement.
      criteria: >
        At least one bone in the B4 garrison-road extended hold (approximately
        bones 637–728) must mark a physical cost or duration-of-hold consequence
        distinguishable from the pre-transition ceiling — i.e., something Taylor
        experiences or registers in her body that would not have been possible or
        would have ended the hold earlier under the child-body ceiling. The bone
        must be present in the proto-line layer, not supplied at facet layer.

    - id: fault-007
      type: fault
      what: >
        Body-clock cost-register differentiation at B5 (plan requirement, bones
        874–937). Season-plan §B B5 structural note: "B5 is the first beat where
        Taylor deploys the new Shard-surface-area in a confrontation context. The
        response-bone must distinguish the new active-control ceiling from the
        pre-transition baseline — not merely assert the expanded capacity, but mark
        the cost-shape: what the extended hold does to Taylor's body that the old
        ceiling would have foreclosed, and what the Shard reads as license in the
        aftermath." The B5 confrontation sequence (Taylor approaches the town reeve
        about the summons, bones 899–922, with grid extensions at bones 874–892 and
        914–924) shows the flies covering the extended road grid and the garrison
        outpost perimeter (bones 879–887, 914–917). Taylor speaks to the town reeve
        (bones 902–921). However: the same absence found in B4 applies here. No
        bone in the B5 block marks a distinct cost-shape distinguishable from pre-
        transition behavior. The "presses the temple" gesture appears at bones 887
        and 917 and 932 — identical in form to its usage in B1 (bone 19), B2 (bone
        258), and the pre-transition stretch. No bone names what the Shard reads as
        license, no bone marks a recovery consequence.
      why: >
        Same downstream consequence as fault-006. B5 is the peak, and the season
        plan's dramatist execution constraint and worm-canon-pedant carry-forward
        both require this differentiation at the bone layer. If it is absent at B5
        — the first confrontation deployment of the new ceiling — the series
        cost-register arc cannot be grounded here. Phase 3 voice-pass cannot supply
        what the proto-line layer did not commit.
      criteria: >
        At least one bone in the B5 confrontation window (approximately bones
        874–937) must mark a distinct cost-shape consequence of operating at the
        new ceiling in a confrontation context — a body-resident consequence Taylor
        experiences during or immediately after the extended confrontation hold that
        the old ceiling would have foreclosed or ended sooner. The differentiation
        must be in the bone, not in a facet-layer addition.

    # ─── SWEEP 3: REFERENCE ──────────────────────────────────────────────────

    - id: fault-008
      type: fault
      what: >
        Slug "loc-blue-fork-river-road" is used as a narrative reference
        throughout the aggregate (bones 284, 288, 338, 430–431, 453, 543–544,
        601, 603, 615, 636, 637, 639, 640, 736, 741, 981 [implied], etc.) but
        no card exists at active-project/warehouse/loc-blue-fork-river-road.card.md.
        The series-plan §5 and season-plan §G both name this location as a new S2
        addition ("new locations from series-plan S2 additions"). No warehouse card
        has been provisioned.
      why: >
        Reference sweep: slug used in aggregate, no card present in warehouse. The
        location is load-bearing — B2 and B4 primary setting, B5 grid extension
        boundary. At Phase 4 split and Phase 3 facet passes, the absence of a card
        means the location's insect ecology, exit structure, and distance markers
        are undocumented. Facet authors cannot anchor sensory or spatial bones to
        a sourced card. Margit provisioning required.
      criteria: >
        A location card for loc-blue-fork-river-road must be provisioned at
        active-project/warehouse/ before Phase 3 facet work begins on any B2 or
        B4 episode. Card must include the road's insect ecology, distance markers
        (Fairstead to tributary bend, tributary bend to east mill, east mill to
        garrison waypost), and exit structure.

    - id: fault-009
      type: flag
      what: >
        Slug "loc-tully-bannerman-seat" appears in series-plan §5 and season-plan
        §G as a named S2 addition ("offstage presence; the institutional tier
        generating Pryor's directives; named but not physically entered in S2").
        It does not appear in the aggregate by slug. The aggregate renders Pryor's
        institutional origin through "oc-lords-steward" and "folio" references
        without naming the location. Season-plan §G: "named but not physically
        entered in S2." No warehouse card present. No aggregate reference either.
      why: >
        The plan specifies this location is named but not entered. The aggregate
        correctly does not enter it. If the location is named in S2 per plan, the
        absence of both a card and any aggregate reference means the naming
        commitment has not been fulfilled. However, because the plan says "named but
        not physically entered," the naming could occur in facet-layer prose rather
        than a proto-line bone. This is a flag for the facet authors to verify
        whether the location name must appear in a bone, or whether facet-layer
        naming satisfies the plan commitment.
      why: >
        If the plan requires a bone-level location name (e.g., Pryor riding from
        Willow Wood, or a rider named as coming from the bannerman seat), and the
        aggregate contains no such bone, Phase 3 facet authors cannot add it at
        that layer. Flag for Phase 4 review.

    # ─── SWEEP 4: POV ────────────────────────────────────────────────────────

    - id: fault-010
      type: pass
      what: >
        Opening POV marker. File line 6: "# pov: taylor-hebert-jaehaerys"
        present at aggregate open, preceding bone 1. Required by dispatch brief.
        Confirmed present.
      why: No finding.

    - id: fault-011
      type: pass
      what: >
        B6 Mira interlude POV marker. The dispatch brief requires
        "# pov: mira-stonefield-jaehaerys" immediately preceding bone 942.
        Aggregate line 1334: "941 # pov: mira-stonefield-jaehaerys" followed
        immediately by bone 942. Marker is in the correct position. Mira's
        physical presence at the market square at the POV switch is established
        by the prior context (market-square dissolution scene). Reachability
        confirmed: Mira's active role in B5 (bones 838–871) and the continuity
        of her gathering-dissolution role in B6 make her physical presence at
        the market square at bone 942 coherent.
      why: No finding.

    - id: fault-012
      type: pass
      what: >
        B6 Taylor POV return marker. The dispatch brief requires
        "# pov: taylor-hebert-jaehaerys" immediately preceding bone 1044.
        Aggregate line 1478: "1043 # pov: taylor-hebert-jaehaerys" followed
        immediately by bone 1044. Marker is in the correct position. Taylor's
        physical position at loft/workshop (bone 1044: "descends the loft ladder")
        is reachable — Taylor's last Taylor-POV bones (934–937) placed her in the
        loft (presses the loft floor, bone 935). The transition to the Mira
        interlude did not move Taylor. Her re-emergence from the loft at bone 1044
        is physically coherent.
      why: No finding.

    - id: fault-013
      type: flag
      what: >
        Newcomer identification in Taylor's exterior-register close (bones
        1054–1091). The season plan §B B6 specifies the newcomer as
        "oc-tributary-village-newcomer" and plan §G names this as a walk-on not
        requiring a card at season-planning level. In the aggregate, the newcomer
        is referred to only as "a figure" (bones 1055, 1059, 1061, 1065, 1069,
        1070, 1071, 1074, 1075, 1079, 1082). The letter of introduction appears
        at bone 1062 ("the figure draws the letter of introduction") and bone 1075
        ("the figure draws the letter of introduction"). The slug
        "oc-tributary-village-newcomer" does not appear in the aggregate at any
        point. The plan's B6 forward-thread requirement states: "the logged-presence
        bone is specific enough to anchor whichever function S3 assigns." Using
        "a figure" throughout preserves ambiguity but does not anchor the slug.
      why: >
        Phase 4 split and Phase 3 facet work will need to refer to this character
        by slug to coordinate S3 planning. If the aggregate uses "a figure" and
        no slug, the Phase 4 split proposal cannot cite the character by name, and
        Margit cannot provision a walk-on card against an unslugified reference.
        Flag: if Margit provisioning of oc-tributary-village-newcomer as a walk-on
        is required before Phase 3, the aggregate's "a figure" designation will
        require a targeted slug insertion at the bone layer. This is editorial, not
        structural — the bones are present and correctly positioned.

    - id: fault-014
      type: flag
      what: >
        Mira's withholding-recognition arithmetic in the interlude (plan §H
        coalition-discovers-the-withholding distribution, execution constraint from
        dramatist iteration-2 review). Plan §H states: "The B6 Mira interlude must
        make the arithmetic legible as Mira's recognition of the specific shape of
        the withholding — not just 'the institution pressed hard enough,' but Mira
        understanding what Taylor held back and when. If B6 renders the dissolution
        as institutional pressure alone, without Mira's recognition of the gap
        between what Taylor knew and what Taylor shared, the series commitment is
        not met." The interlude (bones 942–1040) shows Mira dissolving the
        gathering (bones 963–970), interacting with Septon Rowan (bones 982–990),
        consulting a folio record (bones 992–1000, 1019–1020), and returning to
        the sept for a chapter-house letter exchange (bones 1027–1035). At the
        proto-line layer, bones show action verbs and object-relationships. No bone
        in the interlude explicitly marks Mira's recognition of the withholding-
        shape as a discrete event; the bones "mira-stonefield-jaehaerys holds the
        eyes" (bones 979, 989, 1010, 1014, 1032, 1039) and "presses the temple"
        (bones 980, 993, 1018, 1038) are present but are also Mira's general
        attentional register throughout. This is a flag: at proto-line level, the
        "holds the eyes" and "presses the temple" bones could carry the withholding-
        recognition in facet-layer prose. The risk is that they will be read as
        Mira processing institutional pressure rather than Taylor's specific
        withholding, if the facet layer does not commit.
      why: >
        The dramatist's execution constraint is a named delivery requirement for the
        series-plan series question. If the B6 interlude is rendered only as
        institutional pressure at the facet layer, the series-plan commitment
        ("the people Taylor recruited to trust her discover the specific shape of
        what she withholds") is unmet at S2. Phase 3 voice pass and vibe pass
        should treat this as a named targeting constraint. Flag here so Phase 3
        auditor can verify the facet-layer execution.
```
