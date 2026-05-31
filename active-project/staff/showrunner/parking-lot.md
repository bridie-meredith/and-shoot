# parking-lot — schema: schemas/parking-lot.schema.md
#
# Cross-chunk watch-items targeting future command invocations.
# Append-only. Resolution stamps add fields; entries are never deleted.
# Read by Phase 0 of every re-runnable command per CLAUDE.md Rule 14.

parking_lot:
  version: 1
  items:

    - id: pl-2026-05-25-001
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-substance chapter b01c01 Phase 5 (fixer fault-001)"
      target:
        command: /and-substance
        scope: "chapter b01c03"
        phase: Phase 3
      severity: HARD
      description: |
        cl01b in series.substance.cost_ledger declares gain "social_tether-prot-rise +2"
        but only +1 settled at b01c01s03 (ward-layer half — Oswyn-categorization).
        The remaining +1 (court-layer half — Otto's awareness of the rescue via
        Jarvis Coin) must anchor at b01c03. b01c03's chapter contract currently
        holds social_tether-prot-rise in axes_held ("tether has not formed through
        Jarvis yet; the offer is pending"). Phase 3 at b01c03 must move
        social_tether-prot-rise into axes_in_motion with
        target_delta_magnitude: 1.0 and cost_ledger_anchor: cl01b. Otherwise the
        +2 cl01b gain remains under-anchored and the book-level roll-up's tether
        accounting carries an undeclared partial-settle indefinitely.
      context_refs:
        - active-project/staff/showrunner/memory.md:1698  # b01c01 persist comment
        - active-project/staff/showrunner/memory.md:1821  # b01c01s03 notes field
        - active-project/staff/reviews/b01c01-scenes-audit-2026-05-25.md
        - active-project/staff/showrunner/_drafts/b01c01-draft-2026-05-25.md  # authoring notes G4 block
      status: resolved
      resolved_at: 2026-05-26T00:00:00Z
      resolved_by: "/and-substance chapter b01c03 Phase 3 contract update (pre-screen-writer dispatch)"
      resolution_note: |
        chapters[b01c03].substance_delta.axes_in_motion updated to add
        social_tether-prot-rise +1.0 anchored at cl01b. social_tether-prot-rise removed
        from axes_held; the chapter now moves all four axes per the corrected contract.
        Scene-level decomposition (Phase 3 screen-writer fanout) honors the +1.0 by
        anchoring it at one of the 3 scenes — typically scene 2 (Jarvis-courier contact
        is where Otto's awareness completes via the courier vector).

    - id: pl-2026-05-25-002
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-substance chapter b01c01 Phase 5 (audience trio soft watch)"
      target:
        command: /and-write
        scope: "b01c01"
        phase: null
      severity: SOFT
      description: |
        Audience trio (cape-fic-reader, dark-fantasy-reader, worm-canon-pedant)
        flagged at /and-substance chapter b01c01 Phase 5: the Wren stitch-house
        plant must land as quietly loaded, not background noise. Dormancy framing
        is structurally correct at the contract level — but bones in s01 and s03
        that touch the stitch-house (smell two lanes over, Taylor not looking
        toward it) need prose texture that makes the sensory plant intentional
        rather than ambient detail. Not a contract change; a write-time prose
        discipline.
      context_refs:
        - active-project/audience/cape-fic-reader/stm.md
        - active-project/audience/dark-fantasy-reader/stm.md
        - active-project/audience/worm-canon-pedant/stm.md
        - active-project/staff/showrunner/memory.md:1701  # b01c01 persist comment SOFT-WATCH line
      status: resolved
      resolved_at: 2026-05-25T00:00:00Z
      resolved_by: "/and-write b01c01 Phase 7 emit"
      resolution_note: |
        Stitch-house plant authored as three concrete physical bones, not ambient detail:
        s01n02 (flat_id 2) "the tallow smoke crosses the stitch-house lane" — opening
        sensory ground naming the stitch-house as a working-class craft district fact;
        s03n08 (flat_id 25) "the tallow smoke layers the lane-floor" — chapter-close
        confirming the smell continues as the cost-bearer's location physical-presence;
        s03n07 (flat_id 24) "taylor faces the alley-mouth" — the body-direction that
        excludes the stitch-house, enacted positively per the no-negation rule.
        s03n10 (flat_id 27) "wren-stitch-maker-flea-bottom-ward faces taylor-hebert-kl-122ac"
        (added at Phase 5) delivers the chapter-close cost-bearer orientation that
        the handoff_out asserts. Audience Phase 6 bone-gate verdicts: all three personas
        SUBSTANCE-FELT; cape-fic-reader specifically noted "three-station dormancy arc
        complete (s01n02 smoke → s02n09 in the crowd unregistered → s03n10 orienting
        toward Taylor), reader knows who it is, Taylor does not." Decoration test passed.

    - id: pl-2026-05-25-003
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-substance book b01 Phase 5 (auditor soft findings, backfilled 2026-05-25)"
      target:
        command: /and-write
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        Two non-blocking soft findings carried from /and-substance book b01
        Phase 5 ACCEPT (attempt 3) into /and-write runs across the book:
        (a) SOFT-CURVE-moral_framework — the book contract distributes the
            6-rank moral_framework collapse across chapters as uniform drops;
            the series trajectory concentrates the collapse at 3 specific
            deltas (d03 first crack, d07 systematic-override-rationalized,
            d12 irrevocable-Khepri-repetition). Per-chapter bone-level
            moral_framework movements should respect concentration rather than
            uniform distribution.
        (b) 8 INFERENTIAL-ANCHOR / NAMING-INCONSISTENCY findings on the
            cost_ledger — inference-derived anchor relationships and a mixed
            slug naming convention. Non-blocking but noted for /and-write
            cross-checks on cost-ledger entries.
      context_refs:
        - active-project/staff/showrunner/memory.md:1601  # book b01 persist soft-findings comment
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-004
      created_at: 2026-05-25T04:30:00Z
      created_by: "/and-review bones b01c01 (fidelity-fork fault-001)"
      target:
        command: /and-facets
        scope: "b01c01"
        phase: null
      severity: SOFT
      description: |
        b01c01s02n11 (flat_id 16) SVO is "taylor-hebert-kl-122ac raises the
        voice" — a physical-action shape, not a "speaks to listener"
        speech-act shape. The chunk text for s02 is explicit that Taylor
        speaks to the crowd-adjacent persons ("uses a voice that does not
        ask whether they will comply"; the voice-of-instruction event in
        event_map). At /and-facets, the dialogue-facet author for
        taylor-hebert-kl-122ac will need a citable speech anchor in s02.
        Three resolution options, ordered by cost:
          (a) Cite n11 as-is and accept the physical-action SVO as the
              dialogue-bone anchor — the chunk text is explicit that the
              voice carries instruction. Lowest cost; preserves flat_id
              stability for all 27 bones.
          (b) Treat n11 as the body-act and emit the dialogue facet as
              derived-from-chunk rather than bone-anchored. Cost: a
              one-time dialogue-facet authoring exception; preserves
              flat_id stability.
          (c) /and-write b01c01 revise to recast n11 as a speech-act SVO.
              Cost: highest — breaks flat_id stability for downstream
              consumers (currently none authored, so cost is recoverable;
              would still require re-firing the bone-gate). Lowest-friction
              path if /and-facets author judges (a) and (b) both leave the
              dialogue facet untenable.
        Recommend deferring the resolution call to /and-facets Phase 0 /
        dialogue-facet author. Not blocking: /and-review bones b01c01
        verdict was PASS-WITH-NOTES; /and-facets b01c01 is cleared to
        dispatch.
      context_refs:
        - active-project/staff/showrunner/memory.md:2020   # s02n11 bone entry
        - active-project/staff/showrunner/memory.md:1903   # s02 event_map voice-of-instruction
        - active-project/staff/showrunner/memory.md:1855   # s02 chunk "uses a voice that does not ask whether they will comply"
        - active-project/staff/reviews/bones-b01c01-fidelity-2026-05-25T04-30-00Z.md
        - active-project/staff/reviews/bones-b01c01-2026-05-25T04-30-00Z.md
      status: resolved
      resolved_at: 2026-05-25T00:00:00Z
      resolved_by: "URI-WRITE-DIALOGUE-COBONDED (CLAUDE.md Rule 15)"
      resolution_note: |
        Resolved structurally by the dialogue-cobonded process change. The
        bones schema now explicitly licenses action-form dialogue-anchor
        bones whose substance_delta declares a communication-class axis
        movement (per schemas/bones.schema.md § Dialogue-anchor bones).
        Routing (a) from this entry is now the default — no flat_id break,
        bone 16 carries [taylor-hebert-kl-122ac:1, :2, :3] citations as
        emitted by /and-write Phase 7 Step 3a. No further /and-facets action
        needed; the routing question is no longer a per-chapter decision.

    - id: pl-2026-05-25-005
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-facets b01c01 Phase 5b cycle 1+2 (worm-canon-pedant + dark-fantasy-reader verdicts on memory facet flag-013)"
      target:
        command: margit-card-class-review
        scope: "b01c01 memory mem:1, mem:2"
        phase: null
      severity: SOFT
      description: |
        mem:1 and mem:2 in memory-b01-c01.md use cond-* slug class, but
        worm-canon-pedant and dark-fantasy-reader flagged at Phase 5b cycle 1
        and cycle 2 that the substantive content (witch-label-formation-as-monument,
        override-architecture-residue-as-monument) warrants monument-* slug class
        per URI-032 referral. Not a blocking finding at /and-facets — facets passed
        with cond-* slugs. Resolution deferred to next /and-cast or /and-substance
        command that touches these slugs, or to a dedicated margit card-class review.
        Resolution: margit authors monument-* class cards for these concepts, updates
        target-reference slugs in memory-b01-c01.md, and updates cards/ taxonomy if
        URI-032 needs revision.
      context_refs:
        - active-project/theater/facets/memory-b01-c01.md
        - active-project/staff/showrunner/memory.md  # b01c01 bones_review + facets note
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-006
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-facets b01c01 Phase 5 cycle 3 audit flag-C3-001"
      target:
        command: /and-stitch
        scope: "b01c01"
        phase: null
      severity: SOFT
      description: |
        Dialogue sidecar entries 1+2 in taylor-hebert-kl-122ac.drafts.md cite
        sensory:2 @9 (tactile) cleanly after cycle-2 cleanup, but the original
        utterances were authored against sound modality @16 ("the croup / Stand
        back"). The mechanical citation walks but semantic fit between the utterance
        and its facet license is loose — sidecar cites a tactile anchor for
        speech-acts whose authority register is sonic. Stitcher or /and-postop
        should review whether the body-language read (crowd-compression as somatic
        context) carries the speech-act's authority register, or whether dialogue
        should be re-authored to restore a direct sound-modality anchor.
      context_refs:
        - active-project/theater/dialogue/taylor-hebert-kl-122ac.drafts.md
        - active-project/theater/facets/sensory-b01-c01.md
        - active-project/staff/showrunner/memory.md  # b01c01 facets note
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-007
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-facets b01c01 cycle-1 state-updates fixer"
      target:
        command: /and-write
        scope: "b01c01"
        phase: null
      severity: SOFT
      description: |
        state:5 (Taylor posture @17) was deleted in cycle-1 state-updates
        remediation because no narrator-interest co-citation existed at @17.
        Re-add is a candidate if/when narrator-interest gets an entry at @17.
        If a future /and-write revise or /and-facets re-run authors an NI entry
        at @17 (hands-up-mouth-shut public-frame transition), the state-updates
        author may re-add state:5 with proper co-citation at that point.
        Non-blocking; no correctness gap in current facets.
      context_refs:
        - active-project/theater/facets/state-updates-b01-c01.md
        - active-project/theater/facets/narrator-interest-b01-c01.md
        - active-project/staff/showrunner/memory.md  # b01c01 facets note
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-008
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-facets b01c01 cycle-2 feeling worm-canon-pedant + cape-fic-reader ADVISORY notes"
      target:
        command: /and-postop
        scope: "b01c01"
        phase: null
      severity: SOFT
      description: |
        Feeling facet fires at 3/27 bones = 11.1% in b01c01, above the rubric
        2-5% band. Cycle-2 worm-canon-pedant and cape-fic-reader noted this as
        ADVISORY (non-blocking) — the three entries are each load-bearing and no
        single one was recommended for deletion. Resolution options: (a) /and-postop
        confirms all three fires are structurally necessary and recommends a
        short-chapter exemption note be added to the feeling rubric's frequency
        band; or (b) /and-postop judges one entry cuttable and flags for a targeted
        /and-facets revise. Advisory; does not block /and-stitch.
      context_refs:
        - active-project/theater/facets/feeling-b01-c01.md
        - active-project/staff/showrunner/memory.md  # b01c01 facets note
      status: resolved
      resolved_at: 2026-05-25T00:00:00Z
      resolved_by: "/and-postop b01c01 Fork A substance-delivery audit"
      resolution_note: |
        OPTION (a). All 3 feeling entries judged structurally necessary:
        feel:1 @21 (Oswyn apron-front somatic at tether-peak), feel:2 @10
        (Taylor breath-empties at prohibition's-last-held-moment), feel:4 @27
        (Wren eyes-first at chapter-close cost-bearer plant). 11.1% rate is
        structural concentration in a 27-bone short chapter, not over-fire.
        Recommended short-chapter exemption note for feeling rubric's
        frequency band promoted to pl-2026-05-25-017 (target: future rubric
        edit). Secondary anomaly on feel:2 @10 prose-anchor promoted to
        pl-2026-05-25-014 (target: /and-facets b01c01 spot-check), orthogonal
        to the rubric-band call.

    - id: pl-2026-05-25-009
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-facets b01c01 cycle-2 Phase 5 confirm-audit fault-C2C-001"
      target:
        command: /and-facets
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        During cycle-2 Phase 5 fixer pass, the fixer reclassified 2 HARD dialogue
        findings as "SIGNAL — anchor-association citation" using a concept absent
        from rubric-dialogue.md. The confirm-audit caught this and reinstated the
        HARDs. The pattern is generalizable: fixer invents a SIGNAL category not
        enumerated in the rubric to reclassify findings it cannot fix. Worth an
        AP-SCAN promotion to mechanize detection. Suggested entry: "fixer-classification-evasion"
        — auditor enumerates rubric's SIGNAL signatures and rejects any SIGNAL
        classification using a category not present in the rubric. Target for
        promotion: auditor class library in .claude/commands/and-facets.md (TASTE-FLAG
        to AP-SCAN pathway per CLAUDE.md Rule 11).
      context_refs:
        - .claude/commands/and-facets.md  # auditor class library (AP-SCAN section)
        - active-project/staff/showrunner/memory.md  # b01c01 facets note
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-010
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-facets b01c01 cycle-3 sensory admin DEC-0007"
      target:
        command: /and-facets
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        Cycle 3 sensory required an interpretation ruling on whether a cross-facet
        upstream REVISE of an existing entry's field constitutes an ADD under cap-burn
        pre-validation. Admin DEC-0007 ruled: REVISE operations on existing entries
        (field additions, value updates) are not ADDs and do not trigger cap-burn
        pre-validation. Only introduction of a new facet entry triggers the rule.
        This ruling is not currently explicit in the /and-facets command body's
        URI-FACETS-CYCLE-N-ADD section. Worth promoting to spec text to prevent
        re-litigation in future cycles. Target: add a clarifying sentence to the
        cap-burn handling block in .claude/commands/and-facets.md.
      context_refs:
        - .claude/commands/and-facets.md  # URI-FACETS-CYCLE-N-ADD / cap-burn section
        - active-project/staff/showrunner/memory.md  # b01c01 facets note DEC-0007
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-011
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-stitch b01c01 Phase 9 cold-read terminal gate"
      label: depth-pass-recommended-b01c01
      target:
        command: /and-write
        scope: b01c01
        phase: null
      severity: SOFT
      description: |
        /and-stitch Phase 9 PASS (staging signals 15; no cluster above >=5 threshold).
        Optional depth pass recommended per Phase 9 Step 4. Use /and-write b01c01
        revise --from-signals to consume the staging report's findings
        (peak-under-staged x4, held-bone-rationale-only x3, body-staging-gap x2,
        others) — most are GROUND/STAGE/NEEDS-BEAT class.
      context_refs:
        - active-project/staff/reviews/staging-b01-c01-2026-05-25.md
        - active-project/staff/reviews/coldread-b01-c01-2026-05-25.md
      resolution_suggestion: "/and-write b01c01 revise --from-signals + re-cascade /and-facets + /and-stitch (typical depth-pass loop)"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-012
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-stitch b01c01 Phase 9 cold-read terminal gate"
      label: cold-read-caveat-bug-mechanic-staging
      target:
        command: /and-write
        scope: b01c01
        phase: null
      severity: SOFT
      description: |
        Cold reader (uninformed first-time reader) could not tell HOW Taylor's bugs
        part the crowd. The rendered prose at @12 says "the insects propagated where
        I'd told them to go" — registers as mind-control or unspecified mechanism.
        The substance graph has the bug-mechanic implied; the bone-faithfulness fence
        kept the staging out. STAGE this if depth-pass fires.
      context_refs:
        - active-project/staff/reviews/coldread-b01-c01-2026-05-25.md
        - active-project/staff/reviews/staging-b01-c01-2026-05-25.md  # sensory-channel-named-not-felt @9
      resolution_suggestion: |
        /and-write revise; add a sub-bone STAGING the physical sensation of how the
        crowd-yield happens (people feeling bugs at ankles, flinching, parting).
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-013
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-stitch b01c01 Phase 9 cold-read terminal gate"
      label: q9-hyphen-density-threshold-tune
      target:
        command: future spec edit on stitcher persona / Phase 7 Q9 rubric
        scope: cross-pipeline
        phase: null
      severity: SOFT
      description: |
        Cold reader noted "prose dense with hyphen-compound nouns (angle-wall,
        lane-mouth, chin-lift) and short declarative fragments that read like stage
        directions. I had to reread the middle three times to confirm an event was
        happening." Phase 7 Q9 sweep applied 0 REWORDS — the strict Q9 rule allows
        bone/facet tokens through, and many of these hyphen-compounds ARE bone/facet
        tokens. But aggregate density in rendered prose creates a different kind of
        readability hit than per-sentence Q9 catches. Consider an aggregate-density
        check at Phase 7 (or a stitcher persona variant that defaults to natural-English
        unfolding for bone tokens).
      context_refs:
        - active-project/staff/reviews/coldread-b01-c01-2026-05-25.md
      resolution_suggestion: "future stitcher persona / Phase 7 rubric edit"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-014
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-postop b01c01 Fork A substance-delivery audit"
      label: feel-2-at-10-render-anomaly
      target:
        command: /and-facets
        scope: "b01c01"
        phase: null
      severity: SOFT
      description: |
        feel:2 @10 in feeling-b01-c01.md is authored but has no clear prose anchor
        in the annotated draft at @10. Orthogonal to the rubric-band call resolved
        in pl-2026-05-25-008 (which judged all three feeling entries structurally
        necessary). If the entry's prose anchor is genuinely absent, this is a
        cite-index walk that landed without prose rendering it. Suggested
        resolution: /and-facets revise spot-check on feel:2 @10 — either
        confirm the anchor is present (read-error on Fork A's part) or re-anchor
        / drop the entry.
      context_refs:
        - active-project/theater/facets/feeling-b01-c01.md
        - active-project/draft/b01-c01.annotated.md
        - active-project/staff/reviews/substance-delivery-b01-c01-2026-05-25T-postop.md
      resolution_suggestion: "/and-facets b01c01 revise (spot-check feel:2 @10)"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-015
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-postop b01c01 Phase 3 convergence (Forks B + C)"
      label: opening-graf-em-dash-glossary-onboarding
      target:
        command: /and-write
        scope: "b01c01"
        phase: null
      severity: SOFT
      description: |
        Naive cold-read (Fork B) and cape-fic-reader (Fork C) independently flagged
        the opening graf 9 em-dash glossary stack (stitch-house / Hook / ward
        defined inline within stacked parentheticals and em-dashes) as the
        prose-surface drag point. Fork B drifted past it ("I knew I'd be told again");
        Fork C called it "fidget, not walkout" but explicitly distrust-flagged. The
        compound-hyphen-noun density across the chapter (graf 9 + lines 11-19
        stacked one-liners) creates onboarding labor that costs immersion. Folds
        into the existing depth-pass queue (pl-2026-05-25-002/003/004 already
        staged for /and-write revise --from-signals) as an additional signal:
        targeted prose-economy on the opening onboarding paragraph + dispersal
        of glossary loads across scenes.
      context_refs:
        - active-project/staff/reviews/pleasure-read-b01-c01-2026-05-25T-postop.md
        - active-project/staff/reviews/audience-cape-fic-reader-b01-c01-2026-05-25T-postop.md
        - active-project/staff/showrunner/parking-lot.md  # see pl-2026-05-25-002/003/004
      resolution_suggestion: "/and-write b01c01 revise --from-signals (rolled into existing depth-pass queue)"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-016
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-postop b01c01 Fork A substance-delivery audit"
      label: held-axis-bare-assertion-at-7
      target:
        command: /and-write
        scope: "b01c01"
        phase: null
      severity: SOFT
      description: |
        Fork A substance-delivery audit found @7 ("I exhaled") carrying three
        held axes on a bare two-word verb with no opposing-pressure-resistance
        on the page. Substance-layer finding only — neither Fork B (cold-read)
        nor Fork C (cape-fic-reader) surfaced this at prose-reception layer,
        but the prose-layer Of-visible check that Phase 6 bone-gate cannot do
        (Phase 6 audits at rationale layer) catches it post-hoc. Folds into
        the same depth-pass queue.
      context_refs:
        - active-project/staff/reviews/substance-delivery-b01-c01-2026-05-25T-postop.md
        - active-project/theater/bones/b01-c01.md
      resolution_suggestion: "/and-write b01c01 revise --from-signals (rolled into existing depth-pass queue)"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-019
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-review bones b01c02 (fidelity-fork flag-001)"
      label: prohibition-spatial-continuity-b01c02-s02
      target:
        command: /and-stitch
        scope: b01c02
        phase: Phase 0
      severity: SOFT
      description: |
        b01c02s02 distributes the Taylor-cannot-cross-alley prohibition across two
        bones: n13 (`the alley admits the ward-junction body` = flat_id 13) and n16
        (`taylor-hebert-kl-122ac yields the alley-mouth` = flat_id 16). The chunk's
        original line carried both events; the SVO-form fix split them. The bones
        honor the chunk and the event_map covers both — but the discipline reading
        depends on stitcher prose treating n13 and n16 as continuous spatial frame
        (the alley Wren entered is the same alley-mouth Taylor then yields). If
        rendered as disconnected images, the discipline softens to environmental.
        /and-stitch Phase 0 lens-anchoring should preserve the spatial continuity.
      context_refs:
        - active-project/theater/bones/b01-c02.md
        - active-project/staff/reviews/bones-b01c02-fidelity-2026-05-25.md
      resolution_suggestion: "/and-stitch Phase 0 lens-anchor n13 + n16 as the same alley"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-018
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-write b01c02 Phase 6 auditor (schema-ambiguity flags 2 + 3)"
      label: post-move-axes-held-listing-schema-ambiguity
      target:
        command: /and-review
        scope: pipeline
        phase: null
      severity: SOFT
      description: |
        At b01c02 Phase 6 bone-gate, auditor flagged that schemas/showrunner-memory.schema.md
        does not specify whether post-move holding of an in-motion axis (e.g. s02n09/n10
        holding relational_anchor_status after s02n07 moved it; s03 multiple bones holding
        moral_legibility_to_self around s03n05's move) requires the axis to be listed in
        the scene-level axes_held[] declaration. The b01c02 scene contracts declare
        in-motion axes ONLY in axes_in_motion[] and exclude them from axes_held[] —
        and several bones in those scenes carry post-move holds on those axes. The Phase 6
        HELD-AXIS-UNCONTRACTED gate could fire false-positive if interpreted strictly;
        the auditor noted but did not fault, calling it schema-ambiguity to surface.
        Resolution path: /and-review pipeline cross-walk decides whether (a) post-move
        held-on-in-motion-axis is implicitly licensed (no schema edit; auditor docs the
        carve-out) or (b) scene-level axes_held[] must list every axis any bone holds
        (would require backfill on b01c01 and b01c02 contracts).
      context_refs:
        - active-project/staff/auditor/write-b01-c02-bone-gate.md
        - schemas/showrunner-memory.schema.md
        - active-project/staff/showrunner/memory.md  # b01c02 scenes[].substance_delta
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-25-017
      created_at: 2026-05-25T00:00:00Z
      created_by: "/and-postop b01c01 Fork A (resolution of pl-2026-05-25-008)"
      label: feeling-rubric-short-chapter-exemption
      target:
        command: future spec edit on rubric-feeling
        scope: cross-pipeline
        phase: null
      severity: SOFT
      description: |
        pl-2026-05-25-008 resolved option (a): all 3 b01c01 feeling entries
        structurally necessary; 11.1% rate is structural concentration in a
        27-bone short chapter. Fork A drafted exemption text for the feeling
        rubric's frequency band: short chapters (<~30 bones) may exceed the
        2-5% band when each entry is load-bearing (no single entry recommended
        for deletion in audience cycles). Promotion path: edit
        design/shoot-v2/rubric-feeling.md or the equivalent rubric file at
        next rubric-edit pass.
      context_refs:
        - active-project/staff/reviews/substance-delivery-b01-c01-2026-05-25T-postop.md
        - active-project/staff/showrunner/parking-lot.md  # pl-2026-05-25-008
      resolution_suggestion: "future rubric edit"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-27-002
      created_at: 2026-05-27T00:00:00Z
      created_by: "/and-stitch b01-c04 Phase 9 cold-read terminal gate"
      label: cold-read-soft-jeopardy-and-interior-cartography-b01c04
      target:
        command: /and-write
        scope: b01-c04
        phase: null
      severity: SOFT
      description: |
        /and-stitch b01-c04 Phase 9 PASS (clean — no MANDATORY flag; no signal-clusters; prose-rationale-mute 10/10 PASS). Cold reader recovered all central events + thesis-enactment ("the body that walked through the Hook carried both of them at the same count") + tentative-yes continue. Two soft observations the depth-pass could address if user elects:

        (a) Jeopardy reads "Soft and offstage. ... Functionally low." Sera-threat referenced ("Otto's confirmation that Sera was managed and that the three-month window had closed") but not staged in c04 prose; Taylor's saturation-cost named but consequences undefined. This is structurally appropriate for the routing-installation chapter (the threat is c01-c03 inheritance + offstage by design), but a depth-pass could surface body-weight on the saturation-cost (NI:13 "saturation-cost gone past the load she has carried before" registers but does not somatically land) so jeopardy isn't entirely offstage.

        (b) Cold reader noted "the middle walk (~lines 22–53) is almost pure interior cartography — only physical action is walking and looking." Scene-B's mid-section (Oswyn-peak + ward-tier-only + Wren-anchor-discipline) and scene-C's report-handoff aftermath could carry more body-staging at the held-bones. Phase 9 Step 3.5 audit verified concrete tokens are PRESENT on every held bone (10/10 PASS) — this is not a prose-rationale-mute issue. It's a held-bone-body-weight density observation, separable from mute/not-mute.

        Not blocking; chapter is terminal. Optional depth-pass loop: /and-write b01-c04 revise --from-signals + re-cascade /and-facets + /and-stitch.
      context_refs:
        - active-project/staff/reviews/coldread-b01-c04-2026-05-27.md
        - active-project/staff/reviews/prose-rationale-audit-b01-c04-2026-05-27.md
        - active-project/draft/b01-c04.md
        - active-project/staff/stitcher/render-log-b01-c04.md
      resolution_suggestion: "optional /and-write b01-c04 revise --from-signals + re-cascade (typical depth-pass loop)"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-27-001
      created_at: 2026-05-27T00:00:00Z
      created_by: "/and-write b01c04 Phase 2 audit + admin DEC-0030"
      label: c03-bones-svo-form-contamination
      target:
        command: /and-write
        scope: "*"
        phase: Phase 1
      severity: SOFT
      description: |
        c03 bones file (theater/bones/b01-c03.md) shipped with PP-heavy SVO text
        (banned modifiers of place/direction/time/instrument/accompaniment) and
        pair-split 0.5-magnitude axis_moves (below the schema's bone delta floor
        of 1.0) because /and-write b01c03 Phase 2 was SKIPPED under cascade-budget
        compression. c03 was never independently SVO-form audited.

        c04's screen-writer absorbed c03's permissive style as canonical and
        produced 33 FAULT-FORM-MODIFIER + 11 magnitude-floor violations.
        Resolved via DEC-0030 Phase 1 redo with corrective brief naming c02
        (revised, Phase 2 clean) as canonical reference.

        Future /and-write Phase 1 dispatches should: (a) name c02 revised bones
        as the canonical SVO-form/delta-magnitude reference; (b) warn explicitly
        against c03 as a form model; OR (c) the c03 bones file should be
        retroactively form-fixed to bring it into compliance (which would
        require re-running /and-facets b01-c03 + /and-stitch b01-c03 because
        bone-content changes invalidate downstream artifacts — high cost).

        Process-critic dispatch deferred until Phase 2 re-audit on c04 confirms
        whether the corrective brief was sufficient — if c04 Phase 2 redo clears,
        the brief is the structural fix and a PROP for "Phase 1 dispatch must
        name canonical reference bones" becomes the natural promotion. If c04
        Phase 2 redo fails on the same grounds, the root cause is elsewhere
        and warrants reassessment.
      context_refs:
        - active-project/staff/auditor/write-b01c04-pass2.md (45 HARD findings)
        - staff/admin/decisions.md DEC-0030
        - active-project/staff/showrunner/memory.md chapters[b01c03] cascade-budget
          notes (line ~2766: "Phase 2-6 audit chain: SKIPPED under cascade budget")
        - active-project/theater/bones/b01-c02.md (canonical form reference)
        - active-project/theater/bones/b01-c03.md (contamination source)
        - schemas/bones.schema.md line 107 (PP ban)
        - active-project/staff/showrunner/memory.md line 1465 (chunk_targets.bone.delta_per_axis: 1-3)
      resolution_suggestion: "Phase 1 corrective brief + Phase 2 re-audit confirms; promote to PROP if recurrence"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-28-001
      created_at: 2026-05-28T00:00:00Z
      created_by: "/and-write b01c05 Phase 2 (signal-003) + Phase 7 emit"
      label: oc-rushwick-card-absent
      target:
        command: /and-facets
        scope: "b01c05"
        phase: Phase 0
      severity: SOFT
      description: |
        b01c05 introduces the Rushwick — a ward abutting the lower Red Keep
        servant passages — as the chapter's primary location, but no
        oc-rushwick.card.md exists in active-project/warehouse/. The Rushwick
        is referenced as "the-rushwick" in the bones file header (locations
        field) and scene-map facet (per-scene location field). Geography
        internally consistent (junction, lane-mouth, side-alley, east exit,
        alley-mouth, hill's stone skirt). Phase 5 continuity audit accepted
        the location consistency as non-faulting.

        /and-facets Phase 0 should either (a) trigger a margit dispatch to
        author oc-rushwick.card.md before facet authoring begins, or
        (b) carry the noun-form reference forward through facet authoring
        and surface the card as a Phase 5 audit deferral.

        Card content required: ward layout (lane-cluster between Aegon's
        Hill stone skirt and the city's upward lean), abuttment to Red Keep
        servant passages, characteristic alleys (too narrow to sell from,
        wide enough to pass at a run), period geography reference for KL
        122 AC.
      context_refs:
        - active-project/theater/bones/b01-c05.md  # locations: the-rushwick
        - active-project/theater/facets/scene-map-b01-c05.md
        - active-project/staff/auditor/write-b01c05-pass2.md  # signal-003
        - active-project/staff/auditor/write-b01c05-pass5.md  # geography consistency check
      resolution_suggestion: "margit dispatch at /and-facets Phase 0 to author oc-rushwick.card.md from chunk-text geography references"
      status: resolved
      resolved_at: 2026-05-28T00:00:00Z
      resolved_by: "margit dispatch at /and-facets b01c05 Phase 0"
      resolution_note: |
        oc-rushwick.card.md authored from chunk-text geography references (bones
        file locations header, scene-map-b01-c05.md per-scene location notes,
        showrunner memory b01c05 chunk text for s01/s02/s03); library + warehouse
        copies present. Library: cards/locations/oc-rushwick.card.md (full quality).
        Warehouse: active-project/warehouse/oc-rushwick.md (copy per warehouse
        convention — .md suffix, no .card.md). cards/locations/INDEX.md updated
        (oc-rushwick added to by_world/planetos and by_quality/full).

    - id: pl-2026-05-28-002
      created_at: 2026-05-28T00:00:00Z
      created_by: "/and-write b01c05 revise --from-signals Phase 6 (dark-fantasy-reader escalated soft carry)"
      label: sera-architecture-facet-mandatory-c05
      target:
        command: /and-facets
        scope: "b01c05"
        phase: null   # resolved at final facet-emit / Phase 5b audience-gate, not a specific phase abort
      severity: HARD
      description: |
        Sera-architecture delivery is now MANDATORY at the /and-facets b01c05 re-run.
        B3 (Sera-arrangement filing bone) was dropped at /and-write Phase 5 continuity
        audit (FAULT-REFERENCE: "the jarvis-form" + "the sera-arrangement-file" both
        unestablished named entities; bone-realizing the Sera-connection would also
        violate the chapter's substance discipline — s01/s03 force-blocks explicitly
        state Taylor does not name the connection on-page). The Sera-link therefore
        migrated to the facet layer.

        Per dark-fantasy-reader Phase 6 bone-gate verdict: "this is not optional at
        the facet layer." Without facet-layer delivery, the political_register-prot
        +1.5 axis-move at @29 (taylor stops the rushwick-pass) lands as
        resentment-of-enforcement, not the chapter's specific irony (the feed stops
        running flat on the content Taylor has been routing through the same
        architecture that serves the Sera-protection).

        Required facet-layer deliveries (per dark-fantasy-reader brief):
        - memory facet: Taylor's prior context on Sera-protection arrangement;
          must anchor at a chapter-open or s02-filing beat where the Jarvis-report
          drafting bone (@19) implicitly serves the protective architecture.
        - exposition facet: reader-facing world-state surface — who Sera is, what
          the protective architecture protects against, why the Jarvis-routed
          intelligence is the mechanism. The cold-reader at /and-stitch Phase 9
          flagged "Sera named once, never explained" — exposition facet must close
          this without inventing on-page protagonist articulation.
        - narrator-interest facet: the implicit Sera-connection as a quality of
          the routing — Taylor's interior posture acknowledges the architecture
          without naming it (consistent with s01/s03 force-block disciplines).

        Resolution gate: /and-facets b01c05 Phase 5b audience-gate (3-of-3 strict).
        If dark-fantasy-reader's Phase 5b verdict on memory + narrator-interest +
        exposition facets returns SUBSTANCE-FELT on the Sera-link irony, this item
        resolves. If any persona returns FAIL on the Sera-architecture absence,
        the gate cap-burns or returns to cycle-N fixer to add the missing facet
        entries — and this item remains HARD until resolved.
      context_refs:
        - active-project/staff/auditor/write-b01c05-pass5-revise.md  # B3 drop continuity rationale
        - active-project/audience/dark-fantasy-reader/stm.md  # Phase 6 bone-gate ESCALATED soft carry
        - active-project/audience/cape-fic-reader/stm.md  # Phase 6 bone-gate concurring read on Sera-migration
        - active-project/audience/worm-canon-pedant/stm.md  # Phase 6 bone-gate "B3 dropped: CORRECT" with facet-layer migration appropriate
        - active-project/staff/reviews/coldread-b01-c05-2026-05-28.md  # original cold-read confusion (iii) on Sera identity
        - active-project/staff/showrunner/_drafts/b01c05-revise-fromsignals-2026-05-28.md  # B3 drop section + migration plan
      resolution_suggestion: |
        /and-facets b01c05 Phase 1 R1 fanout should brief memory + narrator-interest +
        exposition authors explicitly on the Sera-architecture migration. Add to each
        author's brief: "B3 (Sera-arrangement filing bone) was dropped at /and-write
        Phase 5; your facet must carry the Sera-link without Taylor articulating it on
        page. See parking-lot pl-2026-05-28-002 for required deliveries per facet."
        Phase 5b audience-gate must include dark-fantasy-reader verdict on the
        Sera-link irony landing.
      status: resolved
      resolved_at: 2026-05-28T00:00:00Z
      resolved_by: "/and-facets b01-c05 Phase 5b cycle 1 audience-gate (all 3 personas concurring SERA-ARCHITECTURE LANDS)"
      resolution_note: |
        Three audience personas independently verified the Sera-architecture irony
        lands without Taylor naming it on-page:
        - cape-fic-reader: "exposition:2 @0 gives the reader the mechanism before
          the body starts: Jarvis-routed intelligence pays for the quiet on Sera's
          parentage question. Memory:1 @19 fires at the filing bone connecting
          enforcement Jarvis-routing to protective architecture in real time. NI:5
          @19 confirms routing-destination as interior cognition without Taylor
          naming. When @29 lands, the reader is equipped to read it as the instrument
          recognizing the content it routes through the same architecture that
          protects Sera — not abstract resentment."
        - dark-fantasy-reader: "SERA-ARCHITECTURE: LANDS. Three-facet delivery
          complete: exposition:2 @0 (WHO+WHAT+WHY trio: Sera as Hightower-cadet ward
          of Alicent's household; parentage-question liability; Jarvis-routed
          intelligence pays for the quiet) + memory:1 @19 (interior register of
          routing's destination 'the architecture that holds someone else's exposure
          at a length of someone else's arm') + NI carriers @5/@19/@29 (posture
          without naming). The +1.5 at @29 lands as instrument-complicity (feed
          stops being neutral on substrate it routes harm through), not as
          resentment-of-enforcement. The Sera-link irony is structurally anchored."
        - worm-canon-pedant: Earth-Bet fence CLEAN; canonicity discipline holds
          (mem:2 Earth-Bet displacement via override-architecture-residue uses
          shape-language only, no Khepri / Gold Morning leak).
        Final-cycle aggregate: vibes 3/3 ACCEPT, memory 3/3 ACCEPT, exposition 3/3
        ACCEPT (the three Sera-architecture carrier facets).
        Evidence: active-project/staff/auditor/facets-audience-gate-r2.md

    - id: pl-2026-05-30-001
      created_at: 2026-05-30T00:00:00Z
      created_by: "/and-substance chapter b01c06 Phase 4 (auditor flag-001, v2)"
      target:
        command: /and-substance
        scope: "chapter b01c08"
        phase: Phase 3
      severity: SOFT
      description: |
        cl-d06 in series.substance.cost_ledger declares gain "relational_anchor_status +2"
        but b01c06 settles only +1.0 (first tranche, anchored at b01c06s01 — the Wren
        spoken-exchange + name-omission). The cost side (moral_framework -1) is FULLY
        settled at b01c06s03. The remaining +1.0 relational_anchor_status gain is named
        but not yet anchored downstream. b01c06s01 notes name the candidate window
        b01c08-b01c10 ("when Wren becomes structurally necessary to the coverage map
        without appearing in the ledger, per d08 delta"). The resolving chapter
        (b01c08/c09/c10) Phase 3 must add relational_anchor_status +1.0 with
        cost_ledger_anchor: cl-d06 to its axes_in_motion, or the +2 cl-d06 gain carries
        an undeclared partial-settle indefinitely. Matches the recurring
        worm-canon-pedant partial-settlement pattern (cf. pl-2026-05-25-001).
      context_refs:
        - active-project/staff/auditor/substance-b01c06-scenes-v2.md  # flag-001
        - active-project/staff/showrunner/memory.md  # b01c06s01 substance_delta notes
        - active-project/staff/showrunner/series-trajectory.md  # d08 delta
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-30-002
      created_at: 2026-05-30T00:00:00Z
      created_by: "/and-substance chapter b01c06 Phase 5 (audience 3-of-3 ACCEPT, bones-execution watches)"
      target:
        command: /and-write
        scope: "b01c06"
        phase: null
      severity: SOFT
      description: |
        Two bones-execution watches the audience trio attached to their b01c06 ACCEPT,
        for /and-write Phase 1 scene-decomposition discipline:
        (a) dark-fantasy-reader: the Wren name-omission in s01 must be ENACTED as a
            physical pause + specific field-entry ("ward-resident, Hook, routine" written;
            name-field left blank by visible choice), NOT as interior moral narration.
            If the bones let the protective logic become Taylor running a moral narrative
            ("she considers what naming Wren means..."), the omission loses its weight.
            Keep it physical: hand pauses over the field; she writes the role, not the name.
        (b) cape-fic-reader + worm-canon-pedant: the ward-coverage-notes vs Jarvis-channel
            substrate gap must be staged as a concrete institutional mechanism (two distinct
            substrates; the notes inferable-with-effort but not Jarvis-accessible), not as
            "Taylor hoping" the gap holds. This is Taylor applying her pattern-reading
            discipline to her own record-keeping — an operational-security act, not a wish.
        Both are write-time prose/bone discipline, not contract changes. Also carry the
        Phase 5 audience-gate (Phase 5b downstream) expectation that s03's "the accounting
        is honest / the accounting is the breach" stays enacted, not stated as theme.
      context_refs:
        - active-project/audience/dark-fantasy-reader/stm.md
        - active-project/audience/cape-fic-reader/stm.md
        - active-project/audience/worm-canon-pedant/stm.md
        - active-project/staff/showrunner/memory.md  # b01c06 attempt-2 persist comment
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-30-003
      created_at: 2026-05-30T00:00:00Z
      created_by: "/and-write b01c06 Phase 2 (auditor fault-002 + admin DEC ruling)"
      target:
        command: /and-review
        scope: pipeline
        phase: null
      severity: SOFT
      description: |
        SCHEMA AMBIGUITY (ruled, needs formalization). bones.schema.md §"Dialogue-anchor
        bones" requires a canonical speech-form bone (`<speaker> speaks to <listener>`) to
        move ">=1 communication-class axis (community / knowledge / reputation / trust)".
        That enumerated set is the UNIVERSAL questionnaire taxonomy. This project remapped
        to a fully custom signature (state_axes: moral_framework, capability, position-*,
        relational_anchor_status, moral_legibility_to_self, political_register-*,
        social_tether-* ; class only ever emotional|plot). No axis named
        community/knowledge/reputation/trust exists, so a literal slug-match would make
        EVERY speech bone in the project invalid — contradicted by c03/c04 speech bones
        (jarvis<->taylor) that shipped through the same Phase-6 gate.

        RULING (admin user-proxy, 2026-05-30; "custom signature authoritative over universal
        scaffolding"): relational_anchor_status (and the social_tether-* family) ARE this
        project's communication/relational-class axes. b01c06s01n04 (Wren's first spoken
        line) declaring relational_anchor_status +1.0 is a VALID canonical speech bone;
        Phase 2 fault-002 is NOT a real fault.

        FORMALIZATION (two edits proposed):
        (a) bones.schema.md: generalize the speech-bone requirement text to
            ">=1 communication/relational-class axis per the active signature (universal
            questionnaire: community/knowledge/reputation/trust; custom signature: the
            axis/axes the signature designates relational/communicative)."
        (b) series.substance signature block: add a one-line note naming
            relational_anchor_status + social_tether-* as the communication-class axes, so
            the next chapter's Phase-2 auditor does not re-flag this.
        Resolve at a /and-review pipeline tri-walk (schema vs command-body vs rubric) or a
        dedicated schema-edit pass. Until then this ruling is the binding precedent.
      context_refs:
        - schemas/bones.schema.md  # §Dialogue-anchor bones, lines ~140 + ~165
        - active-project/staff/auditor/write-b01c06-pass2.md  # fault-002
        - active-project/staff/showrunner/memory.md  # series.substance.state_axes
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-30-004
      created_at: 2026-05-30T00:00:00Z
      created_by: "/and-substance chapter b01c07 Phase 5 (audience trio) + Phase 5.5 (chunk-cold-read) + Phase 5 (auditor)"
      target:
        command: /and-write
        scope: "b01c07"
        phase: null
      severity: SOFT
      description: |
        b01c07 bones-execution watches (chunk PASSED structure 3-of-3; these are write-time prose/SVO
        disciplines, NOT chunk revisions — a breathing/argument hinge chapter at seminar-risk):
        - WATCH-1 (cape-fic + worm-canon + chunk-cold-read): the named death ("the body that prompted
          her here", s03) MUST decompose to a concrete SVO — a specific name, a specific street, a
          specific failure-mechanism (what the maester-call would have changed; why it was not routed).
          The whole chapter's CONTINUE leans on this beat; gestured-at = the counter reads as
          rationalization, not a real counter. (EVENT-NOT-CONCRETE risk.)
        - WATCH-2 (dark-fantasy + chunk-cold-read CAUSALITY gap): s02 must show the compound-corruption
          thesis GETTING THROUGH — one moment it lands somewhere Taylor can feel it (a crack, not
          resolution) — BEFORE she picks up the counter. Otherwise "genuine engagement" is unearned and
          the cold-read's "why does she stay?" gap (asserted-not-caused) ships. Motivate why the argument
          grips her.
        - WATCH-3 (worm-canon): the [mechanism: foreclosure-planted-not-enacted] note (s03) must render in
          TAYLOR's ledger-accounting interior voice ("this is what I am not doing, and I know it"), NOT as
          a narratorial/author-structural framing note.
        - WATCH-4 (dark-fantasy): moral_legibility HELD at rank 5 is a discipline against escalating, NOT a
          license to make Taylor immune — the engagement costing her the KNOWLEDGE of the available road is
          a small felt cost; render it felt without advancing the axis.
        - WATCH-5 (cape-fic): give one texture beat of Taylor noticing the irony that her surveillance
          architecture has peripherally tracked Halvard (since week one) while his whole mode is to be
          ungovernable by it — the gap between knowing and being ready is where the social_tether deepening
          lives.
        - AUDITOR fault-009 (s01 stakes_axis disambiguation): s01 scene_conflict.stakes_axis is
          social_tether-prot-rise, a HELD axis this scene (legal per Phase-3 union rule). /and-write Phase 1
          must read it as a conflict-frame label, NOT a Δ-authoring mandate — do not generate bone-gate
          pressure to move a held axis at s01.
        Chunk-cold-read verdict PASS-CHUNK-VOICE-RISK arms /and-stitch Phase 8.5 central-event-muffle +
        Phase 9 jeopardy scrutiny (low present jeopardy on a non-coda hinge is partly design-inherent but
        the named-death anchor must carry).
      context_refs:
        - active-project/staff/reviews/chunk-coldread-b01c07-2026-05-30.md
        - active-project/staff/auditor/substance-chapter-b01c07-audit.md
        - active-project/staff/showrunner/memory.md  # chapters[b01c07].scenes[] + chunk_cold_read
      status: resolved
      resolved_at: 2026-05-30T00:00:00Z
      resolved_by: "/and-write b01c07 Phase 1-7 (rev2 bone-gate PASS)"
      resolution_note: |
        WATCH-1 honored (Wenna Cobb concrete named-death in dialogue @s03n02: name+street+failure-mechanism).
        WATCH-2 honored (thesis-lands @s02n05 'goes still' BEFORE counter @s02n06 'faces' — causality gap closed).
        WATCH-3/4/5 routed to narrator-interest facet anchors (foreclosure @s03n06 leaves; two-accountings @s03n03 absorbs; surveillance-irony @s01n06). fault-009 honored (no social_tether Δ at s01).
        NOTE: the argument-spine interiority that took 3 bone-gate attempts to clear is the live evidence behind PROP-0024 (DEC-0051) + the DEC-0052 discriminator (physical-observable-verb witnesses; delete-over-invent for interiority).

    - id: pl-2026-05-31-001
      created_at: 2026-05-31T00:00:00Z
      created_by: "/and-stitch b01c07 Phase 9 cold-read terminal gate + staging pass"
      label: depth-pass-recommended-b01c07-apparatus-register
      target:
        command: /and-write
        scope: b01c07
        phase: null
      severity: SOFT
      description: |
        /and-stitch b01c07 Phase 9 = PASS-WITH-CAVEATS (READABLE PASS / AIRLESS ALIVE-at-the-edge /
        MUFFLE-CHECK CONCRETE / CONTINUE barely-yes). Chapter is TERMINAL (shipped). Optional depth
        pass available; NOT blocking. The cold-read caveat (predicted exactly by the chunk-cold-read
        PASS-CHUNK-VOICE-RISK): the ledger/apparatus/surveillance register that powers Taylor's voice
        also saturates the connective tissue + the middle argument, making a perfectly followable
        chapter read colder/more seminar-like than it needs to — and making her STAYING land asserted
        ("staying was the more expensive option, and I paid it") rather than felt.
        Staging pass (5 SIGNAL findings; no >=5 cluster so full depth-pass not mandated by the cluster
        rule; report staging-b01-c07-2026-05-31.md). Two load-bearing WATCH-item findings if a depth
        pass is elected:
        - signal-002 NEEDS-BEAT @12-@13: the going-still is caused by recognition arriving passively
          rather than by Taylor's deflection/route-around impulse being ARRESTED — the genuine-engagement
          premise wants the impulse-then-arrest visible, not asserted. (WATCH-2.)
        - signal-003 STAGE @18-@19: the decision to DEPLOY the counter (cross from holding it to
          deploying because the argument's honesty requires completing the account) is fused into the
          speech's opening breath; @18 peak-bone wants the choice staged, not performed. (WATCH-1.)
        - signal-005 EXPAND @22-@23 (lower-risk): the staying-before-leaving (+0.5 social_tether peak)
          is compressed to a single heel/cobble sensory beat; may be underweighted vs its arc place.
        Resolution: optional /and-write b01c07 revise --from-signals (targeted @12-@13 + @18-@19) +
        re-cascade /and-facets + /and-stitch. Or accept terminal as-is (the FAIL triggers all cleared).
      context_refs:
        - active-project/staff/reviews/coldread-b01-c07-2026-05-31.md
        - active-project/staff/reviews/staging-b01-c07-2026-05-31.md
        - active-project/draft/b01-c07.md
      resolution_suggestion: "optional /and-write b01c07 revise --from-signals (@12-13 + @18-19) + re-cascade; or accept terminal"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-31-003
      created_at: 2026-05-31T17:00:00Z
      created_by: "/and-write b01c08 Phase 2 (auditor fault-001 + admin DEC-0002 override)"
      label: bone-floor-sub-1.0-exception-formalization
      target:
        command: /and-review
        scope: pipeline
        phase: null
      severity: SOFT
      description: |
        SCHEMA / PRECEDENT RECONCILIATION. chunk_targets.bone.delta_per_axis is "1-3"
        (memory.md line 1465) but project practice has shipped sub-1.0 bone magnitudes
        without explicit exception: c07 used 0.3/0.5/0.2/0.5 (4 sub-1.0 bone deltas,
        all PASS Phase 6, shipped to draft/b01-c07.md). c08 reproduces the same shape:
        chapter target_delta_magnitude 0.5 → s01n06 capability magnitude 0.5 → fault-001
        flagged by Phase 2 auditor → admin DEC-0002 overrode via precedent (no schema
        carve-out exists; the precedent is silent).

        Formalize the carve-out at next /and-review pipeline pass. Two options:
        (a) Add a sub-1.0-allowed-when conditional to chunk_targets.bone.delta_per_axis
            (e.g. "1-3 when scene_target_delta_magnitude >= 1.0; magnitude = scene_target
             when scene_target_delta_magnitude < 1.0"). Preserves the 1-3 floor for
            normal scenes; carves an exception for sub-1.0 scene targets.
        (b) Revise the floor to 0.5-3.0. Simpler; lets sub-1.0 sub-increments through
            without precedent-citation. Risk: erodes the discipline against 0.5-Δ proxy-hold
            bones being authored where 1.0+ moves are intended.
        Recommended: (a) — preserves discipline + matches precedent shape.
      context_refs:
        - active-project/staff/showrunner/memory.md  # line 1465 chunk_targets.bone
        - active-project/staff/auditor/write-b01-c08-pass2.md  # fault-001
        - staff/admin/decisions.md  # DEC-0002 override rationale
        - active-project/staff/showrunner/_drafts/b01c07-bones-draft-2026-05-30-rev2.md  # precedent lines 402, 430, 544, 632
      resolution_suggestion: "/and-review pipeline at next pass; (a) preferred"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-31-002
      created_at: 2026-05-31T00:00:00Z
      created_by: "/and-write b01c06 revise --from-signals Phase 6 (audience s03 verdicts — render-layer soft carries)"
      label: c06-s03-stitch-render-watches-post-deabstraction
      target:
        command: /and-stitch
        scope: b01c06
        phase: Phase 4
      severity: SOFT
      description: |
        Two render-layer watches the audience trio attached to their b01c06 revise
        Phase-6 SUBSTANCE-FELT verdicts on the de-abstracted s03. Both are /and-stitch
        Phase 4 voice-embodiment disciplines, NOT bone defects (bones are concrete +
        airless-cleared 3/3 at the bone layer). Also surfaced in scene-map-b01-c06.md
        s03 protected-patterns.
        (a) dark-fantasy-reader — flat 19 `taylor marks the red-keep coverage record`:
            clean concrete bone, but the ONE place airlessness could re-enter at the
            render layer. Render as a physical act; do NOT expand into a structural-
            architecture summary sentence ("she checked the record to confirm the
            arrangement was still purchasing something real"). That re-introduces the
            instrument-reporting-itself register the depth pass removed.
        (b) worm-canon-pedant — the two `opens` bones (@16 opens the ledger-board,
            @25 opens the ward-coverage notes): space them in prose rendering to prevent
            a metronomic open/close rhythm. Not a bone-level tic (separated by the full
            accounting + the send); a prose-cadence watch.
        The depth pass's whole purpose is the readability cure; these protect it from
        regressing at the render layer. The DEC-0048 escalation clause is live — the
        re-cascade /and-stitch Phase 9 cold-read is the terminal test (AIRLESS-on-central-
        event -> FAIL/re-decompose).
      context_refs:
        - active-project/audience/dark-fantasy-reader/bone-gate-b01c06-revise.md
        - active-project/audience/worm-canon-pedant/bone-gate-b01c06-revise.md
        - active-project/theater/facets/scene-map-b01-c06.md  # s03 protected-patterns
        - active-project/staff/auditor/write-b01c06-bone-gate-revise.md
      resolution_suggestion: "/and-stitch b01c06 Phase 4 voice-embodiment: render flat 19 as physical act; space the two 'opens'"
      status: resolved
      resolved_at: 2026-05-31T00:00:00Z
      resolved_by: "/and-stitch b01c06 (depth-pass re-cascade) Phase 1 render + Phase 9"
      resolution_note: |
        Both watches honored. flat-19 rendered as a concrete physical act ("I drew the line
        that marked the red-keep coverage — one stroke, the stylus laid flat and pulled across
        the record, the paid mark"), NOT an architecture-summary; Phase 8.5 coherence + Phase 9
        Step 3.5 (0 mutes) both confirmed @19 cleared. opens-spacing honored: @6/@16/@25 rendered
        with three distinct textures (no metronome). Chapter terminal per DEC-0058.

    # ── Session 2026-05-31 cold-read audit findings (sub-section b01 c01-c07) ──
    # Source: active-project/draft/_combined-b01-c01-c07-audit.md
    # Branch: session/audit-and-stitch-2026-05-31

    - id: pl-2026-05-31-004
      created_at: 2026-05-31T22:00:00Z
      created_by: "session cold-read audit of combined b01 c01-c07 (principal-directed)"
      label: c07-four-names-consequence-absent
      target:
        command: /and-write
        scope: b01c07
        phase: null
      severity: SOFT
      description: |
        c06's chapter-defining beat — sealing the form with four Black-faction ward
        elders by name (the cost-axis crossing from movement-patterns to persons) —
        has zero on-page consequence in c07. c07's prologue declares "the circuit is
        routine" and the chapter pivots to the Septon-Halvard argument. Cold-read
        across the sub-section: this is the largest narrative ball drop in the seven
        chapters. A reader closes c06 with maximum loaded expectation and opens c07
        on quiet. Two resolution shapes:
          (a) Re-open c07 to plant a single on-page register of the four-names
              consequence in the Hook morning before the Septon scene — an absence
              on Taylor's count where a Black-faction elder was, a new gait pattern
              filling the slot, a piece of news in the chandler's-storehouse murmur.
              The Halvard argument then *arrives because* the consequence is in the
              air, not as a separate ethics seminar. Costs: c07 revise + re-cascade.
          (b) Defer the consequence to c08+ as a delayed-reveal mechanic, accepting
              that c06 closes a stress-loaded chapter and c07 deliberately runs cold.
              Risk: contempt-onset (series axis d05) may need this beat to land
              before the contempt is earned. Defer-cost is low if a c08-c10 window
              registers the consequence within ~3 chapters of the sealing.
        Recommend (a). The trajectory wants contempt-onset surfacing in b01's first
        half and the cleanest scaffold is the Hook *feeling different* the morning
        after a delivered name-set.
      context_refs:
        - active-project/draft/_combined-b01-c01-c07-audit.md
        - active-project/draft/b01-c06.md
        - active-project/draft/b01-c07.md
      resolution_suggestion: "/and-write b01c07 revise — plant four-names consequence in chapter open before Halvard scene; re-cascade facets + stitch"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-31-005
      created_at: 2026-05-31T22:00:00Z
      created_by: "session cold-read audit of combined b01 c01-c07"
      label: wren-under-seeded-c01-to-c06
      target:
        command: /and-write
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        Wren Stitch-Maker is structurally the cost-bearer; her c06 intervention
        ("there's a way past — cut before the cart, by the tallow-boiler's wall — I
        been through") is the sub-section's single strongest line. But across c01-c06
        Wren has only three on-page presences: c01 close (introduction by name),
        c02 ambient feed-flag, c04 feed-return-not-written-down. She is otherwise
        absent. The c06 line should ring like a struck bell; cold-read says it lands
        like a stranger we were told about in chapter one. Recommend authoring one
        sub-bone of on-page Wren-presence in c03 (the morning market is exactly the
        ground she would cross; she could pass through the salt-fish stall sightline
        before Jarvis enters), and one in c05 (a Hook-feed return as Taylor evening-
        reviews and Wren's print is the one print held a length longer than the
        others). Costs: small bone additions during revise; no axis movement required.
        Both candidate plants are passive-observation, not contact — preserves the
        c06 four-month-silence framing.
      context_refs:
        - active-project/draft/_combined-b01-c01-c07-audit.md
        - active-project/draft/b01-c01.md
        - active-project/draft/b01-c06.md
      resolution_suggestion: "/and-write b01c03 revise + /and-write b01c05 revise — add passive Wren-presence sub-bones; re-cascade both"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-31-006
      created_at: 2026-05-31T22:00:00Z
      created_by: "session cold-read audit of combined b01 c01-c07"
      label: halvard-cold-walk-on-c07
      target:
        command: /and-write
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        Septon Halvard is the Faith's man for the Hook stretch in c07; per the prose
        Taylor has tracked his circuit for two months. He is on-page for the first
        time in c07, and the founding-entry name (Wenna Cobb, six-year-old, fever,
        two seasons back) lands in his dialogue with no prior on-page anchor. The
        Halvard argument is the sub-section's purest argument-chapter beat; the
        argument suffers because the antagonist arrives cold. Resolve by:
          (a) Plant Halvard as an on-page body in c04 or c05 — the kind of fixture
              Taylor's feed has logged a hundred times — passing in the lane,
              tending a sick body, exchanged a nod with. One sub-bone.
          (b) Plant a brief on-page mention of the Cobb death (or an equivalent
              founding-entry death) before c07 — a name Taylor has carried since
              before coverage came up; her ledger has the entry under a prior
              column. Without this c07's "she's the first name in the count" reads
              as authored-into-existence-for-the-scene rather than carried.
        Both costs are small. Prefer doing both.
      context_refs:
        - active-project/draft/_combined-b01-c01-c07-audit.md
        - active-project/draft/b01-c07.md
      resolution_suggestion: "/and-write b01c04 or b01c05 revise — seed Halvard body + Cobb founding entry; re-cascade"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-31-007
      created_at: 2026-05-31T22:00:00Z
      created_by: "session cold-read audit of combined b01 c01-c07"
      label: rushwick-courier-attack-unprocessed
      target:
        command: /and-substance
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        c05 stages an enforcement-incident in the side-alley off the Rushwick east
        exit — three figures, one body, the work of force absorbed and not answered.
        Taylor files the body-record and routes the report-entry. The courier-walk
        "holds the rushwick-pass" in the evening flat-read; this is c05's load-bearing
        readability beat (the apparatus recognizing the architecture it runs through).
        Then nothing. c06 and c07 do not register the Rushwick courier, the
        enforcement-incident, or the consequence of the report Taylor delivered. As
        staged it is a single-instance set-up. The reader expected either the courier
        to recur (the body whose record Taylor opened in the body-map under the
        recurring-body anchor) or the enforcement-pattern to escalate. Neither
        happens. Resolution belongs at /and-substance: either author a downstream
        chapter scene-chunk that picks up the Rushwick thread (cleanest at c08-c10
        scene 2 or 3 in a court-tier ward), or re-frame c05's enforcement-incident
        contractually as an *example* of court-tier substrate rather than a setup
        for downstream payoff (which would change c05's chunk + bone-gate verdict
        but is the only honest move if no payoff is planned).
        Recommend the downstream payoff path; the structural promise c05 made is
        the kind the genre contract enforces.
      context_refs:
        - active-project/draft/_combined-b01-c01-c07-audit.md
        - active-project/draft/b01-c05.md
      resolution_suggestion: "/and-substance chapter b01c0X revise — author Rushwick-thread payoff scene in next available court-tier chapter; or re-frame c05 contractually"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-31-008
      created_at: 2026-05-31T22:00:00Z
      created_by: "session cold-read audit of combined b01 c01-c07"
      label: calendar-drift-across-c01-c07
      target:
        command: /and-write
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        Time across the sub-section is impossible to pin down from the prose body.
        Best estimate from prologue cues: c01 = arrival + 3 weeks; c02 = "by end of
        that day" (compressed days); c03 = next morning; c04 = next day; c05 = next
        morning (or unspecified later); c06 = unspecified; c07 prologue = "the
        arrangement is two months old now". ~3 months total. The reader loses
        calendar between c04 and c07. The fix is light: one calendar/season anchor
        per chapter prologue (a market-day name, a Faith-calendar reference, a
        weather/season shift) costs almost nothing and recovers the structural rate
        the sub-section is actually moving at. Not bone-level; prologue-only edit.
        Author at /and-write revise phase 1 (the prologue is the italic block above
        the prose body and is part of the bones emit by convention).
      context_refs:
        - active-project/draft/_combined-b01-c01-c07-audit.md
      resolution_suggestion: "/and-write revise (each chapter) — add one calendar/season anchor to prologue; lowest-blast-radius path"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-05-31-009
      created_at: 2026-05-31T22:00:00Z
      created_by: "session cold-read audit of combined b01 c01-c07"
      label: cross-chapter-aliveness-scoring-question
      target:
        command: /and-review
        scope: pipeline
        phase: null
      severity: SOFT
      description: |
        c05 received an ALIVE verdict on the retroactive PROP-0022 aliveness-twin
        test. Cold-read of c02-c05 as a continuous stretch says the apparatus-
        register accumulates across those four chapters in a way the single-chapter
        ALIVE verdict did not catch. c01 prologues and c07 ledger-stylus prose are
        the only sustained voice-embodiment passages in the sub-section. The
        question is whether aliveness scoring at /and-stitch Phase 4.5 + Phase 9 is
        chapter-isolated by design (which is reasonable: each chapter ships
        independently) or whether it should be optionally cross-chapter when N
        consecutive chapters have shipped and a sub-section read is available. This
        is a process-design question, not a chapter-specific revise. Surfaced to
        /and-review pipeline. Related to PROP-0023 (false-ALIVE on apparatus-
        dominant whole chapter) — the cross-chapter version of the same failure
        class. May fold into PROP-0023 or warrant PROP-0030 (drafted same session).
      context_refs:
        - active-project/draft/_combined-b01-c01-c07-audit.md
        - staff/admin/process-proposals.md  # PROP-0023
        - staff/admin/process-proposals.md  # PROP-0030 (drafted 2026-05-31)
      resolution_suggestion: "/and-review pipeline — discriminate cross-chapter aliveness audit from chapter-isolated; route to PROP-0023 or PROP-0030 disposition"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null
