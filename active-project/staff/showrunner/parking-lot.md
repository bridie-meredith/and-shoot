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
