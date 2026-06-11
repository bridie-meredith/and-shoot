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
      status: resolved
      resolved_at: 2026-06-02T21:40:00Z
      resolved_by: "/and-substance chapter b01c11 Phase 3 (admin user-proxy DEC-0071; via pl-2026-06-02-stitch-thread-002)"
      resolution_note: |
        Superseded/closed by the c12 re-window (DEC-0071). The c08-c10 window closed unsettled
        (relational_anchor_status held flat c08-c11). Re-windowed to c12, whose authored
        relational_anchor_status +1.0 axis-move settles the outstanding cl-d06 2nd tranche
        (cost_ledger_anchor extended to [cl-d08, cl-d06] in chapters[b01c12].substance_delta).
        cl-d08 = mechanism; cl-d06 = debt; one axis-move settles both. The recurring
        worm-canon-pedant partial-settlement pattern is closed for cl-d06.

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
      status: resolved
      resolved_at: 2026-06-07T01:00:00Z
      resolved_by: "fixer (STRUCT-006; /and-review pipeline 20260607T004417Z)"
      resolution_note: "bones.schema.md §Dialogue-anchor bones lines 140+165 generalized this session (STRUCT-006) to '≥1 communication/relational-class axis per the active signature' with an explicit custom-signature clause; memory.md series.substance block now has communication_class_axes comment naming relational_anchor_status + social_tether-* as this project's communication/relational-class axes."

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
      status: resolved
      resolved_at: 2026-06-07T01:00:00Z
      resolved_by: "fixer (STRUCT-007; /and-review pipeline 20260607T004417Z)"
      resolution_note: "option (a) conditional now in showrunner-memory.schema.md chunk_targets.bone line ~144 and inline note at memory.md chunk_targets.bone line ~1465, both citing DEC-0002 as precedent."

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

    - id: pl-2026-06-01-001
      created_at: 2026-06-01T00:00:00Z
      created_by: "/and-write b01c09 Phase 5 (continuity auditor fault-001 + flag-001)"
      label: corwick-referenced-figure-uncarded + c09-canonical-geo-cards
      target:
        command: /and-facets
        scope: "b01c09"
        phase: Phase 0
      severity: SOFT
      description: |
        Two non-blocking continuity-audit carries from /and-write b01c09 Phase 5:
        (a) FAULT-REFERENCE fault-001: bones b01c09s02n09/n04/n05 use bare slug
            `corwick` as SVO subject; no carded actor with this slug exists in
            active-project/actors/. RESOLVED-BY-PRECEDENT at /and-write: c08 bones
            (theater/bones/b01-c08.md lines 35/38 + cast header) used the identical
            bare slug `corwick` for the same figure and SHIPPED (c08 terminal +
            /and-facets COMPLETE). corwick is the established slug for the courier
            figure named at c08s03; using it in c09 is correct continuity, not a
            fault. The Phase-5 auditor flagged HARD only because it is forbidden from
            loading c08 bones (could not see the precedent). Optional cross-chapter
            cleanup: margit may card `corwick` (and `wenna-cobb`, same class) as
            referenced-figure cards if uncarded-bone-subject figures should be
            registered. NOT a c09 blocker.
        (b) flag-001: dragonpit-margin lane + lower-gate side-exit entered as set
            pieces for the first time in c09 bones; warehouse has oc-rushwick /
            oc-stitch-house-lane / oc-pig-tallow-lane / cond-dragon-proximity but no
            dragonpit-margin or lower-gate card. Canonical Westerosi geography
            (Dragonpit is F&B canon), not invented oc- locations. Mirrors oc-rushwick
            handling at pl-2026-05-28-001 (/and-facets Phase 0 margit dispatch).
            /and-facets b01c09 Phase 0 should confirm coverage or dispatch margit.
      context_refs:
        - active-project/staff/auditor/write-b01c09-pass5.md
        - active-project/theater/bones/b01-c08.md
        - active-project/staff/showrunner/b01c09-bones-draft-2026-05-31.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    # ── Session 2026-05-31 cold-read audit findings (sub-section b01 c01-c07) ──
    # Source: active-project/draft/_combined-b01-c01-c07-audit.md
    # Branch: session/audit-and-stitch-2026-05-31
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
      # Phase-10 progress (2026-06-01, /and-stitch b01-c08 Phase 10): c08 lands the courier-FACE
      # leg — Oswyn names "Corwick" ("runs errands for someone above his station, up the hill
      # twice this month"). The enforcement-incident PAYOFF leg remains unpaid and deliberately
      # deferred within the c08-c10 design window. Item stays SOFT/open; routes to /and-substance
      # for a real scene-chunk (no draft-layer fix possible — paying it is a new declared event).
      # Carried forward in aggregate-state open_hooks[] (hook on Rushwick courier-attack thread).
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
      # Phase-10 progress (2026-06-01, /and-stitch b01-c08 Phase 10): c08's prologue now carries a
      # calendar anchor (presentation-reinforcement edit rev-0001: "into the Crone's stretch, the
      # bay-damp settled on the morning stone... before the first bell") using c07's already-declared
      # season register. c08 addressed; item stays open (scope "*") for the remaining chapters.
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

    - id: pl-2026-06-01-cohere-001
      created_at: 2026-06-01T04:20:31Z
      created_by: "/and-review cohere b01 c01-c07 (Fork A naive Q5)"
      target:
        command: /and-write
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        Sensory texture distribution thins through c02 and c04 middles per
        naive Q5. Strong at openings/thresholds; weak through long observation
        stretches. Advisory only — for future chapter authoring (c08+),
        consider scattering one or two concrete sensory anchors mid-scene
        when the protagonist's interior accounting runs >300 words without
        a physical/sensory beat. Routes to /and-write via grounding-ledger
        line items at /and-facets Phase 2.5 (existing PROP-0022 channel).
      context_refs:
        - active-project/staff/reviews/cohere-naive-b01-c01-c07-2026-06-01T04-20-31Z.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-01-cohere-002
      created_at: 2026-06-01T04:20:31Z
      created_by: "/and-review cohere b01 c01-c07 (Fork A naive Q6 — load-bearing CAUTION)"
      target:
        command: /and-write
        scope: "*"
        phase: null
      severity: SOFT
      description: |
        Apparatus-register cumulative load strained but did not break. c06/c07
        actively dramatize the cost of the register, which is what kept the
        reader engaged through the densest passages. For c08+: continue the
        c06/c07 pattern of dramatizing the register-cost when register density
        exceeds the per-scene band; do not let dense-register passages run
        without an interior-cost-of-the-register beat. Advisory — load-bearing
        Q6 CAUTION is closer to the FAIL band than other axes, so this item
        carries higher priority than the other cohere-soft items.
      context_refs:
        - active-project/staff/reviews/cohere-naive-b01-c01-c07-2026-06-01T04-20-31Z.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-01-cohere-003
      created_at: 2026-06-01T04:20:31Z
      created_by: "/and-review cohere b01 c01-c07 (Fork B dramatist axis3)"
      target:
        command: /and-substance
        scope: "chapter b01c08-b01c<MM>"
        phase: null
      severity: SOFT
      description: |
        Antagonist pressure fragments between transaction points (C03/C04/C06
        Otto spikes; intervals carry structural-not-agentive pressure). b01
        reads as interior-pressure narrative; Otto is episodic demand-escalator,
        not continuous pressure. For c08+: consider whether a between-transaction
        agentive antagonist beat (Otto courier intercept; subordinate visit;
        formal-channel demand outside the schedule) would sharpen the
        antagonist curve without breaking the interior-pressure mode. Advisory.
      context_refs:
        - active-project/staff/reviews/cohere-dramatist-b01-c01-c07-2026-06-01T04-20-31Z.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-01-cohere-004
      created_at: 2026-06-01T04:20:31Z
      created_by: "/and-review cohere b01 c01-c07 (Fork B dramatist axis4)"
      target:
        command: /and-substance
        scope: "chapter b01c08-b01c<MM>"
        phase: null
      severity: SOFT
      description: |
        Scene-shape distribution narrow: ~1 action / ~5 interior / ~4 transaction
        / ~1 argument (c07) across seven chapters. C07 argument carried full
        weight of being the first opposition voice in the stretch. For c08+:
        consider whether a contested-argument scene before next argument-fall
        would distribute argument-load across the book rather than concentrating
        it. Advisory — interior-dominance is consistent with POV architecture
        (first-person observation-as-control).
      context_refs:
        - active-project/staff/reviews/cohere-dramatist-b01-c01-c07-2026-06-01T04-20-31Z.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-01-cohere-005
      created_at: 2026-06-01T04:20:31Z
      created_by: "/and-review cohere b01 c01-c07 (Fork C audience dark-fantasy-reader axis2)"
      target:
        command: /and-substance
        scope: "chapter b01c08-b01c<MM>"
        phase: null
      severity: SOFT
      description: |
        Audience threshold discipline cumulative — two soft flags:
        (a) the insect-instrument never operationally fails the protagonist
        across seven chapters — cost is named but capability is unbroken;
        instrument as undefeated apparatus risks reading as plot armor by mid-book;
        (b) no contesting force until c07 — Jarvis/Otto channel accepts terms;
        world has been *available* rather than *pressing*. For c08+: an
        operational instrument-failure (a count that gets a fact wrong; a
        sensory gap the apparatus cannot bridge) AND/OR a pressing-world beat
        (a Black-side ward elder or Halvard-aligned figure who actively resists)
        would address both flags. Advisory.
      context_refs:
        - active-project/staff/reviews/cohere-audience-dark-fantasy-reader-b01-c01-c07-2026-06-01T04-20-31Z.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-01-stitch-thread-001
      created_at: 2026-06-01T05:08:00Z
      created_by: "/and-stitch b01-c08 Phase 10 Step 4 (aggregate-emit fork divergence flag)"
      label: capability-rank-lineage-divergence
      target:
        command: /and-substance
        scope: "chapter b01c09"
        phase: Phase 0
      severity: SOFT
      description: |
        Initial aggregate-state.md emit (through_chapter b01c08) records the capability
        axis at measured-delta-authoritative rank 5.5 (c01 +1.0 / c04 +2.0 measured /
        c08 +0.5). The book-chunk handoff_out character_state narratives carry a STALE
        capability lineage of 5.0 — never re-synced past the c04 /and-write Phase 1 redo
        that raised the c04 capability delta +1.5 → +2.0. This is a +0.5 divergence
        between aggregate (5.5, authoritative) and handoff_in (5.0, stale).
        Per aggregate-state schema § conflict resolution, aggregate WINS at
        /and-substance chapter Phase 0; the conflict is logged in the chapter chunk
        metadata. b01c09 Phase 0 should detect the aggregate-vs-handoff_in disagreement,
        log a conflict_log entry (conflict_type: aggregate-vs-handoff_in,
        resolution: aggregate-wins), and proceed on capability = 5.5.
        Secondary (informational, same root): social_tether-prot-rise also reads
        measured-delta 6 vs lagging handoff narratives at 3; resolved to 6 in aggregate.
        Advisory — does NOT block; the schema's Phase-0 conflict path handles it
        mechanically. Surfaced so c09 production addresses it explicitly rather than
        relying on a reader noticing the aggregate note.
      context_refs:
        - active-project/staff/showrunner/aggregate-state.md   # axis_state capability notes (ESTIMATE-DIVERGENCE)
        - active-project/staff/reviews/forward-thread-b01-c08-20260601T050033Z.md
      resolution_suggestion: "/and-substance chapter b01c09 Phase 0 — read aggregate-state, log aggregate-vs-handoff_in conflict on capability, proceed on rank 5.5"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-01-002
      created_at: 2026-06-01T16:00:00Z
      created_by: "/and-facets b01c09 Phase 5b convergence trace (bidirectional loop one-sided)"
      target:
        command: /and-review
        scope: pipeline
        phase: null
      severity: SOFT
      description: |
        CALIBRATION GAP (Rule-11 TASTE-FLAG → RUBRIC-FIDELITY promotion candidate).
        At /and-facets b01c09, the sensory facet failed the Phase 5b audience gate on two
        HARD old-state-lineage findings (sensory:1 @8 thermal + sensory:3 @11 light old-states
        unanchored to any prior loc-state sensory-baseline field), caught by the
        sensory-old-state-reader specialist. The Phase-5 mechanical auditor did NOT
        independently fire these — even though the sensory author had left explicit SEAM-011 /
        SEAM-012 self-flags naming the gap. The auditor's RUBRIC-FIDELITY (c) cross-facet
        co-citation / old-state-anchor scan should be able to mechanize this check: a sensory
        entry's declared old-state must resolve to a named prior loc-state sensory-baseline
        field (or a prior sensory entry) at an earlier beat; if no such anchor exists → HARD
        rubric-fidelity-old-state-anchor finding. Promoting this to a mechanical auditor check
        (per rubric-sensory.md § old-state anchor REJECT enumeration) would catch the gap at
        Phase 5 instead of relying on the audience specialist at Phase 5b.
      context_refs:
        - active-project/staff/auditor/facets-audience-gate-r1.md  # convergence trace + calibration note
        - active-project/staff/audience/sensory-old-state-reader/sensory-r1-verdict.md
        - design/shoot-v2/rubric-sensory.md  # § old-state anchor
        - .claude/commands/and-facets.md  # Phase 5 RUBRIC-FIDELITY (c)
      resolution_suggestion: "Add sensory old-state-anchor lineage check to the auditor RUBRIC-FIDELITY enumeration (rubric-sensory.md REJECT section), so it promotes to a mechanical Phase-5 check."
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-01-003
      created_at: 2026-06-01T16:00:00Z
      created_by: "/and-facets b01c09 (auditor + orchestrator silent-write incident)"
      target:
        command: /and-facets
        scope: "*"
        phase: Phase 5
      severity: SOFT
      description: |
        INCIDENT (process-reliability). The Phase-5 auditor fork for b01c09 returned a complete,
        well-formed audit report in its result message but did NOT write
        active-project/staff/auditor/facets-final-audit.md (the on-disk file remained the stale
        c08 report). The orchestrator detected the miss (committed file still had episode: b01c08),
        archived the stale c08 report, and transcribed the c09 report from the fork return.
        Recurrence of the "agent reports a write it did not perform" pattern (cf. silent subagent
        deaths logged at /and-write b01c09). Mitigation already in practice: orchestrator verifies
        the audit file's episode header on disk after the auditor returns, before proceeding to
        Phase 6. Worth a process note: Phase 5 should always stat + episode-check the audit report
        on disk after the auditor fork, not trust the fork's "wrote the file" claim.
      context_refs:
        - active-project/staff/auditor/facets-final-audit.md  # orchestrator-transcribed
        - active-project/theater/_archive/20260601T152450Z-b01c08-stale-r2-shards/staff/auditor/facets-final-audit.md  # archived c08
      resolution_suggestion: "Add a Phase-5 post-auditor on-disk episode-header verification step to the /and-facets command body."
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-02-001
      created_at: 2026-06-02T00:00:00Z
      created_by: "/and-substance chapter b01c10 Phase 5 (audience trio split) + Phase 5.5 (chunk cold-read)"
      target:
        command: /and-write
        scope: "b01c10"
        phase: null
      severity: SOFT
      description: |
        Convergent bones-execution watches for b01c10 — all three audience personas AND the
        chunk cold-read independently flagged the same two soft spots (PASS-CHUNK-VOICE-RISK
        was banked partly on these). These are write-time bone/prose disciplines, NOT contract
        changes:
        - W1 (s02 Corwick-surrender, cape-fic + dark-fantasy + worm + cold-read): the surrender
          of the withheld body-map ("she provides it") must be ENACTED as an irreversible act
          with a physical correlate — months of accumulated observation visible AS months before
          becoming a line item; the substrate-split/translation must be a structurally distinct
          cognitive bone BEFORE the routing bone. If rendered as a clean procedural clause, the
          moral_framework cost goes inert and the central choice reads as decided, not chosen.
        - W2 (s04 face-as-terminal-weight, dark-fantasy + worm): the face must land as the
          chapter's TERMINAL weight, as a physical feed-datum (posture-class / errand-geometry /
          gait-signature persisting in the feed-record), NOT as interior emotional realization
          ("she cannot forget his face"). Two structurally distinct bones — one ledger-closes,
          one record-remains; the surplus of the second over the first is the scene's argument.
          The three "he did not consent" beats stay 3 distinct bones, not collapsed to one
          interior report. Bone ordering must land the face LAST, not the closure notation.
        - W3 (s03 absence-read, worm): enact the prior-circuit presence-count BEFORE the absence
          reads as deviation, so the feed-discipline is not assertion.
        - W4 (aliveness, cold-read): 4 single-POV scenes, no dialogue, no second on-stage body —
          keep the formalization + detention CONCRETE and grounded; the detention especially as a
          perceptual feed-event, not a data-record transaction. (Also armed at /and-stitch Phase
          8.5 via chunk_cold_read.voice_risk.voice_risk_carry.)
      context_refs:
        - active-project/audience/cape-fic-reader/b01c10-chunk-review.md
        - active-project/audience/dark-fantasy-reader/b01c10-chunk-review.md
        - active-project/audience/worm-canon-pedant/b01c10-chunk-review.md
        - active-project/staff/reviews/chunk-coldread-b01c10-2026-06-01.md
        - active-project/staff/showrunner/memory.md  # chapters[b01c10].chunk_cold_read.voice_risk
      resolution_suggestion: "/and-write b01c10 Phase 1 scene-decomposition + Phase 3-5 bone authoring honors W1-W4; Phase 6 bone-gate confirms the s02 surrender and s04 face land as enacted bones."
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-02-002
      created_at: 2026-06-02T00:00:00Z
      created_by: "/and-substance chapter b01c10 Phase 5 (auditor returned-message fault-002)"
      target:
        command: /and-substance
        scope: "*"
        phase: Phase 3
      severity: SOFT
      description: |
        cl-antag-d10 (gain: social_tether-antag +4; cost: journey-required cl04) draws +1.5 at
        b01c10 (s02 +0.5 + s03 +1.0). Its journey-required dependency cl04 (gain:
        relational_anchor_status +3; cost: extraction-path-foreclosed / non-extractable confirmed)
        is NOT drawn at c10 — relational_anchor_status is held flat all four scenes (Wren excluded).
        cl04's relational_anchor accumulation is trajectory-anchored across cl-d06/cl-d08/cl-d11/cl04
        and its non-extractable-confirmation cost is the same d10/d11 "extraction path foreclosed"
        beat c10 begins enacting (handoff_out: "non-extractable confirmation: in progress"). The
        +1.5 cl-antag-d10 draw therefore rides a journey-required dependency that completes across
        c10-c11+, not at a single anchored draw. Auditor flagged this as an unverified authorization
        (advisory, non-blocking — no over-draw; cl-antag-d10 +1.5 of +4.0 drawn). Same cross-chapter
        partial-settle family as pl-2026-05-30-001 (cl-d06) and pl-2026-05-25-001 (cl01b).
        Resolution: the resolving chapter (c11+) Phase 3 should state the cl04 deferred-draw plan
        explicitly when relational_anchor_status next moves, so the cl-antag-d10 journey-required
        dependency is closed in the accounting rather than left implicit.
      context_refs:
        - active-project/staff/showrunner/memory.md  # cost-ledger cl-antag-d10 (~line 1394), cl04 (~line 1388)
        - active-project/staff/showrunner/memory.md  # chapters[b01c10].handoff_out non-extractable in progress
      resolution_suggestion: "c11+ Phase 3 states cl04 deferred-draw plan when relational_anchor_status next moves; closes cl-antag-d10 journey-required dependency in the ledger accounting."
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-02-stitch-thread-001
      created_at: 2026-06-02T00:00:00Z
      created_by: "/and-stitch b01-c10 phase-10 (threading-review ft-c10-001)"
      target:
        command: /and-substance
        scope: "chapter b01c11"
        phase: Phase 3
      severity: HARD
      description: |
        UNPAID-HOOK (substantive). hook-0007 (Halvard counter-argument, opened c07,
        expected_payoff slipped to c10) is NOT addressed in c10 — c10 carries no Halvard
        content (correctly: c10's contract holds Halvard offstage; the formalization +
        detention occupy the chapter's whole weight). The hook has now reached/passed its
        c10 window without resolution. The resolving chapter (c11+) Phase 3 must address
        hook-0007: resolve it, foreclose it, or explicitly re-window it. Returning to the
        Halvard argument is new on-page engagement + axis material the contract held
        offstage — it cannot be threaded into c10 at Phase 10 (bone-faithfulness fence);
        it routes upstream to /and-substance c11+ Phase 3.
      context_refs:
        - active-project/staff/reviews/forward-thread-b01-c10-2026-06-02.md  # ft-c10-001
        - active-project/staff/showrunner/aggregate-state.md  # hook-0007 (Halvard counter-argument)
        - active-project/staff/showrunner/memory.md  # chapters[b01c10].handoff_out "Halvard: counter-argument unresolved; Taylor's engagement becoming thinner"
      status: resolved
      resolved_at: 2026-06-02T21:40:00Z
      resolved_by: "/and-substance chapter b01c11 Phase 3 (admin user-proxy DEC-0071)"
      resolution_note: |
        FORECLOSE — designated foreclosed-at-c13. Admin DEC-0071: the hook is not unpaid; the
        c13 contract is already authored with the resolution ("Halvard appears for what is
        effectively his last substantive encounter ... engagement foreclosed") and c11/c12/c13
        handoffs all carry "counter-argument thinning in Taylor's engagement." Re-windowing
        would misrepresent state (re-window implies not-yet-written); foreclose recognizes the
        content is written and designated. c11 correctly holds Halvard OFFSTAGE; the thinning
        is carried as a handoff thread, not staged in c11. No c11 contract change required.

    - id: pl-2026-06-02-stitch-thread-002
      created_at: 2026-06-02T00:00:00Z
      created_by: "/and-stitch b01-c10 phase-10 (threading-review ft-c10-004)"
      target:
        command: /and-substance
        scope: "chapter b01c11"
        phase: Phase 3
      severity: HARD
      description: |
        UNPAID-HOOK (substantive) — EXTENDS pl-2026-05-30-001. hook-0003 / cl-d06
        relational_anchor_status +2 ledger gain: the SECOND +1.0 tranche reaches the END of
        its declared c08-c10 payoff window (pl-2026-05-30-001 named the b01c08-b01c10 window)
        WITHOUT settling. c10 holds relational_anchor_status FLAT all four scenes (Wren
        excluded by c10's contract). Settling the tranche requires relational_anchor_status
        movement (Wren becoming structurally necessary to the coverage map / entering the
        ledger), which c10 cannot do (forbidden axis-movement under its contract + the
        bone-faithfulness fence at Phase 10). The window has now closed unsettled. c11+ Phase 3
        MUST anchor the remaining cl-d06 +1.0 with cost_ledger_anchor: cl-d06 when
        relational_anchor_status next moves, OR formally re-window the tranche. Closes the
        cl-d06 partial-settle that pl-2026-05-30-001 has been tracking since c06.
      context_refs:
        - active-project/staff/reviews/forward-thread-b01-c10-2026-06-02.md  # ft-c10-004
        - active-project/staff/showrunner/parking-lot.md  # pl-2026-05-30-001 (cl-d06 first-tranche / window b01c08-b01c10)
        - active-project/staff/showrunner/memory.md  # chapters[b01c10] relational_anchor_status held all 4 scenes
      status: resolved
      resolved_at: 2026-06-02T21:40:00Z
      resolved_by: "/and-substance chapter b01c11 Phase 3 (admin user-proxy DEC-0071)"
      resolution_note: |
        RE-WINDOW to c12. Admin DEC-0071: c11 (rising) structurally holds relational_anchor_status
        FLAT (axes_held — Wren in coverage, anchor 3.5, no new weight). c12 (climax) moves
        relational_anchor_status +1.0; that move is the settlement event for the outstanding cl-d06
        2nd tranche. The cl-d08/cl-d06 distinction is mechanism-attribution, not competition:
        cl-d08 is the MECHANISM (Wren structurally necessary to coverage map without entering ledger),
        cl-d06 is the DEBT. Axis movement settles outstanding axis debt; the framework does not gate
        tranche settlement on which ledger id is cited as mechanism. c12's relational_anchor_status
        entry annotated: cost_ledger_anchor extended to [cl-d08, cl-d06] with settlement note.
        Closes the cl-d06 partial-settle pl-2026-05-30-001 has tracked since c06.

    - id: pl-2026-06-03-001
      created_at: 2026-06-03T00:00:00Z
      created_by: "/and-facets b01c11 Phase 5 audit (fault-005/011 RUBRIC-FIDELITY card-resolution SIGNAL)"
      target:
        command: /and-stitch
        scope: "b01-c11"
        phase: Phase 0
      severity: SOFT
      description: |
        New location + prop slugs introduced in b01c11 facets have no warehouse cards
        (all glosses structurally clear + author-defended; SIGNAL not HARD at Phase 5):
        - oc-cloth-merchant-shop (loc; Hook south end; back-worktable + rushlight + iron-dish;
          may nest under a hook-ward umbrella slug per existing taxonomy — margit canonicalization)
        - oc-soap-rendering-lane (loc; cross-lane approach; nighttime-visitor-report delivery point)
        - oc-cloth-merchant-paper (prop; burns @11, exits tracking — low urgency)
        - oc-soap-lane-report-packet (prop; sealed @21, PERSISTS into b01c12 — author before c12)
        - oc-feed-ledger field-extensions (source-field-entry, cloth-merchant-entry, jarvis/oswyn/
          contacts/arrangement-entry) — schema extension on the existing oc-feed-ledger card
        /and-stitch Phase 0 may margit-dispatch the two location cards (scene-window mode uses
        loc slugs) like the c05 oc-rushwick precedent; the oc-soap-lane-report-packet prop card
        is required before /and-substance chapter b01c12 Phase 0 (carried-forward prop).
      context_refs:
        - active-project/staff/auditor/facets-final-audit.md  # fault-005, fault-011
        - active-project/theater/facets/state-updates.md  # Margit referrals section
        - active-project/theater/facets/location-state-b01-c11.md  # SEAM-C11-LOC-001/002/004
      status: resolved
      resolved_at: 2026-06-03T00:00:00Z
      resolved_by: "margit dispatch during /and-substance chapter b01c12 cascade Phase 0"
      resolution_note: |
        All HIGH-priority and REQUIRED cards authored. Canonicalization decisions:

        (1) oc-cloth-merchant-shop — SEAM-C11-LOC-004 canonicalization: library card already
        existed at cards/locations/oc-cloth-merchant-shop.card.md (full quality; had been authored
        but not yet added to INDEX.md or given a warehouse copy). Decision: DO NOT nest under a
        hook-ward umbrella slug. The card is a distinct named location (a specific shop on a
        specific corner, with distinct fixed-props and intelligence-node function) and the existing
        oc- taxonomy does not use umbrella nesting — oc-rushwick, oc-pig-tallow-lane, etc. are all
        flat. Stored as oc-cloth-merchant-shop. Library card confirmed at path; warehouse copy
        created at active-project/warehouse/oc-cloth-merchant-shop.md. INDEX.md updated (added
        to by_world/planetos + by_quality/full).

        (2) oc-soap-rendering-lane — new library card authored at full quality:
        cards/locations/oc-soap-rendering-lane.card.md. Geography: cross-lane approach and lane
        interior between cloth-trade and tallow-rendering quarters; soap-rendering workshop at
        mid-lane; cross-lane mouth is the exchange geometry for nighttime-visitor reports. Warehouse
        copy at active-project/warehouse/oc-soap-rendering-lane.md. INDEX.md updated.

        (3) oc-soap-lane-report-packet — new prop card authored at full quality:
        cards/props/oc-soap-lane-report-packet.card.md. Functional state as of b01c11 @21 close:
        seal_state route-ready, content complete (nighttime-visitor observation + precinct-pattern
        sourcing annotation), location feed-station outbound stack, dispatch_state pending. Carry-
        forward note to b01c12 in Functional State section. Warehouse copy at
        active-project/warehouse/oc-soap-lane-report-packet.md. Props INDEX.md updated.

        (4) oc-cloth-merchant-paper — DEFERRED. Burns @11 and exits tracking in c11; no
        downstream persistence. Not required for b01c12. Noted as not-required-downstream.

        (5) oc-feed-ledger field-extensions — NOT APPLIED. No oc-feed-ledger card found in
        warehouse or library. This item is a schema extension on an existing card that does not
        appear to have been authored yet. Noted for future: when oc-feed-ledger is authored,
        the field-extension schema (source-field-entry, cloth-merchant-entry, jarvis/oswyn/
        contacts/arrangement-entry) should be incorporated.

    - id: pl-2026-06-03-002
      created_at: 2026-06-03T00:00:00Z
      created_by: "/and-facets b01c11 Phase 5 audit (fault-004 RUBRIC-FIDELITY card-resolution SIGNAL)"
      target:
        command: /and-review
        scope: "verdict b01"
        phase: null
      severity: SOFT
      description: |
        memory mem:2@16 target `monument-mass-casualty-foreshadow` has no card in
        cards/conditions/ or warehouse (gloss structurally clear; SIGNAL). Recommended
        margit slug: cond-mass-casualty-foreshadow-122ac (Earth-Bet displacement weight as
        resonance shape — smaller-wars-still-burn, reaching from Gold-Morning scale to KL
        smallfolk-casualty contexts). Create before /and-review verdict b01 (unresolved slug
        would flag at the book verdict pass). Companion to the recurring monument-card-class
        referral pattern (cf pl-2026-05-25-005).
      context_refs:
        - active-project/staff/auditor/facets-final-audit.md  # fault-004
        - active-project/theater/facets/memory-b01-c11.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-03-003
      created_at: 2026-06-03T00:00:00Z
      created_by: "/and-facets b01c11 Phase 5 audit (fault-003 CONSTRAINT state-old-state-continuity SIGNAL) + fault-001/006 cite-index tool quirks"
      target:
        command: /and-stitch
        scope: "b01-c11"
        phase: null
      severity: SOFT
      description: |
        (a) state:9 @22 studio.time_of_day: afternoon->end-of-day — the "afternoon" old-state is
        inferred from the scene-map (scene-C "early afternoon"), not anchored by a prior state-update
        at the scene-B/C boundary (@17). Continuity gap on time_of_day between morning (loc-state:1 @1)
        and end-of-day (@22). Non-blocking: chapter-close projection is end-of-day (correct); the interim
        afternoon is overwritten. /and-stitch should render the time progression morning->afternoon->
        end-of-day smoothly without relying on a missing canonical afternoon anchor.
        (b) cite-index tool quirks (build-tool, not content): phantom display row `sensory:27 @- back=-`
        (no proto-line carries [sensory:27]; harmless) + multi-anchor vibes entries indexed at first
        anchor only (vibes:1/:2 @25+@27 -> indexed @25 only). Both are build_cite_index.py display
        artifacts; a future tool fix should clear them. Stitcher resolves from proto-line tokens, not
        cite-index back-links, so neither affects render correctness.
      context_refs:
        - active-project/staff/auditor/facets-final-audit.md  # fault-003, fault-001, fault-006
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-03-004
      created_at: 2026-06-03T00:00:00Z
      created_by: "/and-substance chapter b01c12 Phase 5 (audience trio bones-execution watches: cape-fic 3 + dark-fantasy 2, convergent)"
      target:
        command: /and-write
        scope: "b01c12"
        phase: null
      severity: SOFT
      description: |
        Five convergent bones-execution watches attached to the b01c12 Phase 5 3/3 SUBSTANCE-FELT
        ACCEPT — write-time prose/SVO discipline for /and-write Phase 1 scene-decomposition, NOT
        chunk revisions. Each is a place the chunk-layer planning language could drift into
        stated-rather-than-enacted prose at bones if not watched:
        (a) s02 closing weather image ("the morning is already warm with the kind of warm that comes
            before the bay-wind clears it") — ENACT as Taylor's body paired to setting (stylus set
            beside the packet, the warm settling on a held hand) = indifferent-world-continuance.
            NOT ambient atmosphere filling space after the collision (cape-fic + dark-fantasy both).
        (b) s03 the three un-routed-content clauses ("the fact that / that / that ... she is not
            naming as one") — ENACT as a physical stopping-before-writing beat (hand stops, the
            stylus not reaching the field), NOT Taylor's interior enumeration of what she declines
            to write. Enacted vs stated withholding read differently and the distinction is not
            recoverable at stitch (cape-fic).
        (c) s03 hand-on-ledger beat ("Her hand stays on it a moment before she lifts it") — must
            LIFT AND MOVE (entry closes, scene ends on function), NOT a camera-lingers-on-what-she-
            protects moment (dark-fantasy). The danger is catharsis-that-isn't-earned.
        (d) s04 "the thing-she-did-at-Gold-Morning word" — must carry accumulated referent-weight
            through the chapter's prior bones (rhymes-with framing, aggregate-shape language, full-feed
            density building toward the threshold) so the un-named word arrives as FELT weight, not
            vague circling (cape-fic). Keep Earth-Bet fence: shape-language only, no proper-noun
            "Khepri" in prose (worm-canon, fence ruled CLEAN at chunk).
        (e) s01/s03 Wren-as-boundary + relational-anchor settlement — ENACTED as record-keeping /
            operational act (indexed-but-unwritten state, the column entry), NOT interior moral
            narration or affection (dark-fantasy + the recurring pl-2026-05-30-002 watch).
      context_refs:
        - active-project/audience/cape-fic-reader/stm.md
        - active-project/audience/dark-fantasy-reader/stm.md
        - active-project/staff/showrunner/memory.md  # chapters[b01c12].scenes (per-scene bones-execution-watch comments)
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-03-005
      created_at: 2026-06-03T00:00:00Z
      created_by: "/and-facets b01c12 Phase 5 audit (flag-005 CONSTRAINT/RUBRIC-FIDELITY card-resolution SIGNAL)"
      target:
        command: margit-card-class-review
        scope: "b01c12 facet card-slugs"
        phase: null
      severity: SOFT
      description: |
        Three facet card-slugs introduced/referenced in b01c12 facets do not resolve to warehouse
        cards (all glosses reader-clear; SIGNAL not HARD at Phase 5):
        - cond-kl-witch-label-formation-122ac (mem:1 @3 target) — the recurring witch-label monument
          referral (companion to pl-2026-05-25-005 / pl-2026-06-03-002 monument-card-class family).
          Margit should author the cond-* (or monument-*) card.
        - loc:east-water-gate-lanes (vibes:4) — the chapter's coverage-gap spine location; reader-
          established geography; margit canonicalize as oc-east-water-gate-lanes (or nest under a
          hook-ward umbrella per existing taxonomy).
        - loc:the-muddy-way (vibes:16) — s04 second-cluster location; reader-established; margit
          canonicalize as oc-muddy-way (or hook-ward nest).
        Non-blocking for /and-stitch (glosses carry). Create before /and-review verdict b01 (unresolved
        slugs would flag at the book verdict pass).
      context_refs:
        - active-project/staff/auditor/facets-final-audit.md  # flag-005
        - active-project/theater/facets/memory-b01-c12.md
        - active-project/theater/facets/vibes-b01-c12.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-03-006
      created_at: 2026-06-03T00:00:00Z
      created_by: "/and-cohere b01 c06-c12 iteration-1 FAIL-COHERE (dramatist + naive structural CAUTIONs; admin DEC-0081 routes structural items here)"
      target:
        command: /and-review
        scope: "verdict b01"
        phase: null
      severity: SOFT
      description: |
        Cross-chapter structural CAUTIONs from /and-cohere b01 c06-c12 (NOT per-chapter bones-revises — book-substance /
        back-half shape items; the load-bearing Q6 apparatus-density is handled separately via the DEC-0081 prologue-variation pass):
        (a) HALVARD counter-argument drift — seeded c07, no re-entry c08-c12; dramatist flags HOLD->DROP-RISK; needs >=1
            structural re-entry before book close. PARTLY ADDRESSED: DEC-0071 already designates Halvard FORECLOSE@c13
            ("last substantive encounter") — verify c13 actually lands the re-entry/foreclosure; if c13 holds him offstage
            again, the thread drops. Watch at /and-substance chapter b01c13 Phase 3 + /and-review verdict b01.
        (b) c11 ANTAGONIST-PRESSURE gap (dramatist REVISE) — c11 ran with no Otto move + absorbed the Rhaenyra cross-pressure
            as color; c11 should have been the pressure-apex before c12. c11 shipped SHIPPED-WITH-CAVEATS; this is a retroactive
            structural note for /and-review verdict b01 (book-level awareness) — not a c11 re-open unless verdict escalates.
        (c) SERA payoff hole — the entire arrangement is owed against the protect-target (Sera), who never appears on-page
            c06-c12. The protect-target must appear / the protection must pay (or visibly fail) before book close. Book-substance:
            /and-substance book b01 forward chapters + /and-review verdict b01.
        (d) DRAGONSTONE receipt — the c11 burned-message (Rhaenyra's faction read the cut thread) needs an in-book receipt;
            tracked by hook-0012 (open). Future-chapter payoff; verify before book close.
      context_refs:
        - active-project/staff/reviews/cohere-b01-c06-c12-20260603T151822Z.md
        - active-project/staff/reviews/cohere-dramatist-b01-c06-c12-20260603T151822Z.md
        - active-project/staff/showrunner/aggregate-state.md  # hook-0007 Halvard, hook-0012 Dragonstone, hook-0005 Sera
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-03-c14-001
      created_at: 2026-06-03T00:00:00Z
      created_by: "/and-substance chapter b01c14 Phase 5 (audience 3-of-3 SUBSTANCE-FELT) + Phase 5.5 (chunk cold-read PASS-CHUNK-VOICE-RISK)"
      target:
        command: /and-write
        scope: "b01c14"
        phase: null
      severity: SOFT
      description: |
        b01c14 bones-execution watches (chunk PASSED 3-of-3 SUBSTANCE-FELT; cold-read
        PASS-CHUNK-VOICE-RISK). These are write-time prose/bone disciplines, NOT chunk
        revisions — a climax chapter whose central event (confirmation -> detention)
        is rendered in a dense accounting/ledger register that risks abstraction-muffle.

        From the audience trio (10 watches):
        - WATCH-01 [S01]: absent merchant must read as a person who LEFT a place (oil-cloth flat,
          samples on hook, missing bag-peg) — not collapsed to "node went dark."
        - WATCH-02 [S02]: person-before-paths sequencing. The figure's face (low-set left eye)
          and pause-habit must be introduced in the bones BEFORE the two alternative paths are
          enumerated. Reorder if bones sequence paths first.
        - WATCH-03 [S03]: harm-before-protection column entry. The harm column must be entered
          and held before the protection column opens, or the accounting reads as rationalization.
        - WATCH-04 [S03]: "she does not let it take less" — render as action/posture/time-held,
          not as a narrated fact about Taylor's discipline.
        - WATCH-05 [S03]: stylus-above-closed-entry is a physical beat (body-position + absence-
          of-action), not a cognitive summary of the accounting's accuracy.
        - WATCH-06 [S04]: pause-habit fires one last time — "both hands going to the strap the way
          they always do" — full physical presence; the chapter's earned-cost peak image; do NOT
          subordinate to the detention geometry.
        - WATCH-07 [S04]: Wren retroactive-naming kept minimal and physical (two column-positions,
          one breath, hand off surface). Over-explanation of the parallel = authorial-cleverness read.
        - WATCH-08 [S04]: Gold-Morning echo ("a city, a different kind of count, a different kind of
          named-and-unpriced") — three clauses, NO proper nouns, NO power mechanics, NO event
          description. Earth-Bet fence, shape-language only. Worm-specific content here = HARD fence
          violation, flag immediately.
        - WATCH-09 [S04]: "non-extractable" arrives as prior-known/settled, not as revelation; a
          thing she has been AVOIDING writing, not one she has not yet written.
        - WATCH-10 [S02/S03]: the walk-detail (adjusted weight, low-set eye) Taylor adds to the
          confirmation sheet is the moment her withheld 11-week tracking becomes the instrument of
          the detention — the inversion (private knowledge becoming the delivery) should be visible.

        From the chunk cold-read (PASS-CHUNK-VOICE-RISK, Signals A+B):
        - WATCH-11: vary the accounting-register across S2/S3/S4. Cold reader flagged "four
          near-identical 'she holds both columns' passages — the accounting repeats almost verbatim."
          Bones must differentiate the three column-runs (weighing / deciding-and-writing / closing-
          and-recognizing) so the assembled prose does not read as one passage three times.
        - WATCH-12: the concrete central-event spine (stylus-to-sheet, wax-seal, two men at the
          junction, hands-on-strap, lane going empty) must carry the event ABOVE the accounting-
          register. PASS-CHUNK-VOICE-RISK arms /and-stitch Phase 8.5 Check 3; bones should give that
          check a concrete spine to verify against.
      context_refs:
        - active-project/staff/reviews/chunk-coldread-b01c14-2026-06-03.md
        - active-project/staff/auditor/substance-b01c14-scenes.md
        - active-project/staff/showrunner/_drafts/b01c14-draft-2026-06-03.md
        - active-project/staff/showrunner/memory.md  # chapters[b01c14].chunk_cold_read.voice_risk
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-001
      created_at: 2026-06-04T00:00:00Z
      created_by: "/and-facets b01c14 Phase 5 audit (flag-002)"
      target:
        command: margit-card-authoring
        scope: "b01c14 warehouse cards"
        phase: null
      severity: SOFT
      description: |
        Five slugs referenced in b01c14 facets lack warehouse cards (pre-flagged
        seams; non-blocking — entries carry sufficient inline description):
        - the-channel-station (loc; SEAM-C14-LOC-001) — Taylor's Jarvis channel-station
        - the-gap-lanes-east-water-gate (loc; SEAM-C14-LOC-002) — the courier gap-lanes
        - prop:oc-feed-ledger (SEAM-C14-ENV) — Taylor's interior accounting ledger
        - prop:oc-jarvis-packet — the courier packet
        - prop:oc-response-sheet (SEAM-C14-ENV-001) — the confirmation sheet
        margit should author these (mechanism-descriptive) so future loc-state
        old-state continuity audits + /and-cast revise can verify constraint
        compliance. Matches the oc-rushwick precedent (pl-2026-05-28-001).
      context_refs:
        - active-project/theater/facets/location-state-b01-c14.md
        - active-project/theater/facets/state-updates.md
        - active-project/staff/auditor/facets-final-audit.md  # flag-002
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-002
      created_at: 2026-06-04T00:00:00Z
      created_by: "/and-stitch b01c14 Phase 9 cold-read (DEC-0085 SHIPPED-WITH-CAVEATS)"
      label: depth-pass-mandatory-b01c14
      target:
        command: /and-write
        scope: b01c14
        phase: null
      severity: HARD
      description: |
        b01c14 shipped SHIPPED-WITH-CAVEATS (DEC-0085) on a Class-B cold-read FAIL
        (CONTINUE=no; events recovered; cause = design-inherent accounting-abstraction
        density, flagged upstream as PASS-CHUNK-VOICE-RISK; Phase 8.5 muffle-check PASSED).
        MANDATORY depth pass before book-close (gates /and-substance book b02 Phase 0 +
        /and-review verdict b01). Consume the cold-read signals via
        /and-write b01c14 revise --from-signals + re-cascade /and-facets + /and-stitch:
        - concretize the courier as a felt person (the cold-reader "never felt the courier
          as a person; told to") -- the 11-week-tracking + low-set-eye detail exists in
          bones but reads abstract in aggregate; stage more body/scene around him.
        - stage Sera as a felt stake (the body never dramatizes Sera; the guarantee is
          known only from the preamble). The degraded-alternative stake needs on-page weight.
        Resolution: run the depth pass; on Phase 9 re-PASS stamp depth_pass_resolved_at.
      context_refs:
        - active-project/staff/reviews/coldread-b01c14-2026-06-04.md
        - active-project/staff/reviews/coherence-b01-c14-2026-06-04.md
        - staff/admin/decisions.md  # DEC-0085
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-c15-001
      created_at: 2026-06-04T00:00:00Z
      created_by: "/and-substance chapter b01c15 Phase 5.5 (chunk cold-read CHUNK-CLASS-B) + admin DEC-0087 (P disposition) + Phase 5 audience trio + dramatist + auditor"
      target:
        command: /and-write
        scope: "b01c15"
        phase: Phase 6
      severity: HARD
      description: |
        b01c15 is a FALLING accounting chapter (Aemond-through-compound-eyes; the space before the
        cascade). Chunk cold-read returned CHUNK-CLASS-B (CONTINUE-strict=No; event-poverty/jeopardy-
        offstage/"nothing-changes" — the SAME failure family as the b01c14 cold-read FAIL). Principal
        (admin DEC-0087) chose PROCEED with the explicit condition that the quietness be carried by
        bones-layer CONCRETENESS, not by adding plot. The c14 lesson applied prophylactically: de-
        abstract the bones so event-poverty renders as vivid quiet rather than accounting-register muffle.
        /and-write Phase 6 (bone-gate; EVENT-NOT-CONCRETE / ABSTRACTION-DOMINANT spine-legibility checks)
        MUST verify these three watches or HARD-abort:

        (1) FEED-TEXTURE CONTRAST CONCRETE (audience SW-c15-2). The relational_anchor_status +1.5 (S3,
            cl04) is contingent on bones executing the gap-lane "person-shaped quality" as a SPECIFIC
            feed-texture contrast — what the fringe-flies return WITH thermal-noise/resolution-dropout
            vs. what the gap returns as CLEAN absence (figure-ground, "shadow against a lit wall") —
            rendered as concrete sensory description, NOT as Taylor's interior labeling. If bones abstract
            over the perceptual mechanism, the +1.5 loses physical grounding → HARD.
        (2) S4 LEDGER-ACT NOT CONCLUSION (audience SW-c15-3 / SW-DFR-c15-1 + dramatist S4-recap-drift).
            S4 (axes_in_motion: []; accounting-close) must ENACT Taylor doing something with the feed —
            a ledger-act, a coverage notation, a physical gesture — NOT a drawn conclusion / interior
            declaration. S4 bones must stay on the NEW articulation (the register-change: the gap is now
            a named absence with a shape) and must NOT recap the S3 perceptual event → HARD if S4 bones
            read as S3 rephrase or as reflective summary.
        (3) AXIS-SLUG FENCE AT BONES (audience SW-c15-1 / SW-WCP-c15-1 / auditor fault-002). The chunk-
            prose axis-slug literals were purged at the chunk layer (fault-002 fixed). Bones must NOT re-
            introduce pipeline-internal vocabulary (axis slugs, "the relational_anchor advances," etc.)
            into Taylor's feed-utilitarian register → HARD if any bone SVO/mechanism names a pipeline slug.

        ARMING (carried to /and-stitch, not resolved at /and-write): chunk_cold_read.voice_risk
        (triggered, Signal B) arms /and-stitch Phase 8.5 Check 3 central-event-muffle verification;
        cold_read_risk_carry arms /and-stitch Phase 9 (a Phase 9 FAIL Class-B on the SAME categories
        — event-poverty/jeopardy-offstage/nothing-changes — ships SHIPPED-WITH-CAVEATS automatically per
        DEC-0087; NEW categories re-dispatch admin).
      context_refs:
        - active-project/staff/auditor/substance-b01c15-scenes.md  # fault-002 axis-slug bleed
        - active-project/staff/showrunner/memory.md  # chapters[b01c15].chunk_cold_read + scenes
        - active-project/audience/cape-fic-reader/stm.md  # SW-c15-1/2/3
        - active-project/audience/dark-fantasy-reader/stm.md  # SW-DFR-c15-1/2
        - active-project/audience/worm-canon-pedant/stm.md  # SW-WCP-c15-1
        - staff/admin/decisions.md  # DEC-0087
      resolution_suggestion: "/and-write b01c15 Phase 6 bone-gate verifies the three watches (concrete feed-texture contrast; S4 ledger-act-not-conclusion; axis-slug fence); stamp resolved on PASS or HARD-abort to a Phase-1 redo."
      status: resolved
      resolved_at: 2026-06-04T00:00:00Z
      resolved_by: "/and-write b01c15 Phase 6 bone-gate (auditor fault-025/026/027 PASS)"
      resolution_note: |
        All three HARD watches adjudicated PASS. (1) FEED-TEXTURE CONTRAST CONCRETE:
        s03n02 (fringe drops image-resolution) / s03n03 (gap-lane returns silence) /
        s03n04 (gap-lane opens a hole in the feed-image) deliver the gap as physical
        figure-ground feed-texture, not interior labeling. (2) S04 LEDGER-ACT NOT
        CONCLUSION: all 9 S04 bones are physical acts (circuit-close, record-run,
        notation-written, stylus-lifted-past-name-field, afternoon-circuit-run); no
        drawn conclusion; no S03 recap. (3) AXIS-SLUG FENCE: zero pipeline slugs in
        any of 40 bone SVOs. Downstream arming intact: chunk_cold_read.voice_risk
        (Signal B) → /and-stitch Phase 8.5 Check 3; cold_read_risk_carry → Phase 9.
        Note: REGISTER-AS-MANNERISM fly-template (signal-002) carried to /and-stitch
        Phase 4 for structural variation.

    - id: pl-2026-06-04-c15-002
      created_at: 2026-06-04T00:00:00Z
      created_by: "/and-write b01c15 Phase 2 auditor (fault-010 inter-document canon conflict)"
      target:
        command: margit-card-authoring
        scope: "Aemond age / lore card"
        phase: null
      severity: SOFT
      description: |
        Inter-document Aemond-age conflict surfaced at /and-write b01c15 Phase 2:
        - actor card: 12, born 110 AC  (F&B-canon-correct)
        - lore card (cond-kl-court-state-122ac or adjacent): 16, born 106 AC  (CANON-WRONG)
        - c15 chapter chunk + goal: said "13" (FIXED at Phase 2 -> 12)
        - c15 bones: "twelve" (canon-correct, unchanged)
        F&B: Aemond Targaryen born 110 AC -> age 12 in 122 AC. Lost left eye at Driftmark
        (120 AC, age 10); wears a sapphire. The lore-card 106 AC/age-16 value is a canon
        error that should be reconciled to 110 AC/age-12 so future chapters touching court-
        tier Targaryen ages do not inherit the wrong baseline. Non-blocking for c15 (bones
        + chunk + goal now all at canon-correct 12). margit should locate the offending lore
        card and correct the Targaryen-children birth-year/age block against F&B.
      context_refs:
        - active-project/staff/auditor/write-b01c15-pass2.md  # fault-010
        - active-project/staff/showrunner/memory.md  # series.lore cond-kl-court-state-122ac
      resolution_suggestion: "margit reconciles the lore card's Aemond birth-year to 110 AC (age 12 in 122 AC) per F&B; cross-check other Targaryen-children ages in the same card."
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-c15-003
      created_at: 2026-06-04T00:00:00Z
      created_by: "/and-facets b01c15 Phase 5 audit (RUBRIC-FIDELITY card-resolution SIGNAL) + state-updates-env field-extension self-flag"
      target:
        command: margit-card-authoring
        scope: "b01c15 warehouse cards"
        phase: null
      severity: SOFT
      description: |
        b01c15 state-updates-env introduces one new prop + three new studio sub-fields
        in use without warehouse cards (non-blocking — entries carry sufficient inline
        description; field-extension protocol self-flagged; matches the oc-rushwick /
        c14-seam precedent pl-2026-05-28-001 / pl-2026-06-04-001):
        - prop:oc-coverage-record (4 fields: site-condition-entries.thermal-rise,
          eastern-boundary-entry, final-notation, condition) — Taylor's per-session
          internal circuit coverage-record.
        - studio.ambient_conditions.thermal-rise-status (tracks Vhagar-backwash thermal event)
        - studio.fauna_sense_status.eastern-fringe-interference (tracks fringe thermal-noise)
        - studio.fauna_sense_status.feed-density (scan-density state; reconcile with the
          b01c12+ fauna_sense_status schema)
        margit should author / reconcile these so future loc-state old-state continuity
        audits + /and-cast revise can verify constraint compliance.
      context_refs:
        - active-project/theater/facets/state-updates-env-b01-c15.md  # field-extension block + margit referrals
        - active-project/staff/auditor/facets-final-audit.md  # RUBRIC-FIDELITY card-resolution SIGNAL
      resolution_suggestion: "margit authors prop:oc-coverage-record.card.md + reconciles the three studio sub-fields against the fauna_sense_status / ambient_conditions schema."
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-c15-004
      created_at: 2026-06-04T00:00:00Z
      created_by: "/and-stitch b01c15 Phase 9 cold-read (SHIPPED-WITH-CAVEATS; Class-B DEC-0087 coupling)"
      label: depth-pass-mandatory-b01c15
      target:
        command: /and-write
        scope: b01c15
        phase: null
      severity: HARD
      description: |
        b01c15 shipped SHIPPED-WITH-CAVEATS on a Class-B cold-read FAIL (CONTINUE=no;
        events recovered + summary maps to goal; cause = design-inherent event-poverty /
        jeopardy-offstage / nothing-changes, ALL pre-authorized in chunk_cold_read.cold_read_risk_carry
        per DEC-0087; auto-shipped terminal per the Phase-9 Step-4 SHIPPED-WITH-RISK-RECORDED
        coupling, mirroring c14 DEC-0085). Phase 8.5 confirmed the central-event-muffle did NOT
        materialize (all 4 events legible) — this is NOT the c14 abstraction-muffle failure; it is
        the deliberately-quiet falling chapter shipping with the known event-poverty caveat.
        MANDATORY depth pass before book-close (gates /and-substance book b02 Phase 0 +
        /and-review verdict b01). Consume the cold-read signals via
        /and-write b01c15 revise --from-signals + re-cascade /and-facets + /and-stitch:
        - the cold-reader's "no character to care about / no stake to follow" is the uninformedness
          leg — a reader 15 chapters in HAS Taylor/Wren/the-arrangement; but the depth-pass should
          still consider whether ONE more on-page anchor of stake (the Wren-cost made a hair more
          present, or the Aemond-as-the-war's-engine weight) would lift the in-chapter continue-pull
          without breaking the falling-arc design.
        - NOTE the two-consecutive-quiet pattern (c14 + c15 both Class-B SHIPPED-WITH-CAVEATS):
          DEC-0087 named /and-cohere before book-close as the designed accumulation handler for this.
          Consider /and-cohere b01 over the c13-c15 stretch.
        Resolution: run the depth pass; on Phase 9 re-PASS stamp chapters[b01c15].cold_read.depth_pass_resolved_at.
      context_refs:
        - active-project/staff/reviews/coldread-b01-c15-2026-06-04.md
        - active-project/staff/reviews/coherence-b01-c15-2026-06-04.md
        - active-project/staff/showrunner/memory.md  # chapters[b01c15].cold_read
        - staff/admin/decisions.md  # DEC-0087
      resolution_suggestion: "/and-write b01c15 revise --from-signals + re-cascade; OR /and-cohere b01 c13-c15 (two-consecutive-quiet accumulation handler per DEC-0087)"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-c16-001
      created_at: 2026-06-04T16:40:00Z
      created_by: "/and-stitch b01c16 Phase 9 cold-read (SHIPPED-WITH-CAVEATS; Class-B DEC-0090 coupling)"
      label: depth-pass-mandatory-b01c16
      target:
        command: /and-write
        scope: b01c16
        phase: null
      severity: HARD
      description: |
        b01c16 (the Halvard walk-away / foreclosure chapter) shipped SHIPPED-WITH-CAVEATS on a
        Class-B cold-read FAIL (CONTINUE=no; central event RECOVERED + summary maps to goal; cause =
        design-inherent event-poverty / jeopardy-offstage / quiet-aftermath / argument-foreclosed-not-
        dramatized, ALL pre-authorized in chunk_cold_read.cold_read_risk_carry per DEC-0090; auto-shipped
        terminal per the Phase-9 Step-4 SHIPPED-WITH-RISK-RECORDED coupling, mirroring c14 DEC-0085 / c15
        DEC-0087). Phase 8.5 coherence PASS (weave/followability clean; DEC-0090 no-thesis-restatement
        confirmed). The "what is the narrator literally" opacity is the known uninformed-reader artifact
        (the assembled book resolves it c01-c15). MANDATORY depth pass before book-close (gates
        /and-substance book b02 Phase 0 + /and-review verdict b01). Consume via /and-write b01c16 revise
        --from-signals + re-cascade; OR fold into /and-cohere b01 c13-c16 (the now-FOUR-consecutive-quiet
        accumulation c13/c14/c15/c16 — the cohere stretch handler is the more efficient lever per DEC-0087).
      context_refs:
        - active-project/staff/reviews/coldread-b01-c16-2026-06-04.md
        - active-project/staff/showrunner/memory.md  # chapters[b01c16].cold_read
      resolution_suggestion: "/and-cohere b01 c13-c16 (four-consecutive-quiet accumulation handler) OR /and-write b01c16 revise --from-signals + re-cascade"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-c17-001
      created_at: 2026-06-04T23:10:00Z
      created_by: "/and-substance chapter b01c17 Phase 5 (auditor fault-002)"
      target:
        command: /and-substance
        scope: "chapter b01c18"
        phase: Phase 3
      severity: SOFT
      description: |
        cl-d11 in series.substance.cost_ledger declares gain "relational_anchor_status +1"
        but b01c17 settles only +0.5 (anchored at b01c17s04 — apparatus-query closes / Wren
        screened). The remaining +0.5 is named but not anchored downstream. Matches the
        recurring worm-canon-pedant partial-settlement pattern (cf. pl-2026-05-25-001 /
        pl-2026-05-30-001). c17 deliberately moves relational_anchor_status only +0.5 (Wren
        held in coverage but screened); c18 holds the axis flat ("anchor holds at 7.5"), so the
        cl-d11 2nd tranche is NOT settled at c18 either. Surface at b01c18 Phase 3: anchor the
        remaining +0.5 to a later chapter, or document it as a cost-forward carry to the d14
        collapse settlement. Non-blocking; the +0.5 c17 move is contract-honored.
      context_refs:
        - active-project/staff/auditor/substance-b01c17-scenes.md  # fault-002
        - active-project/staff/showrunner/memory.md  # cl-d11 (~line 1402); chapters[b01c17s04].substance_delta
      resolution_suggestion: "b01c18 Phase 3 anchor remaining cl-d11 +0.5, or document cost-forward carry to d14"
      status: resolved
      resolved_at: 2026-06-05T02:30:00Z
      resolved_by: "/and-substance chapter b01c18 Phase 3 (cost-forward carry to d14 documented)"
      resolution_note: |
        c18 holds relational_anchor_status flat at 7.5 (Wren screened throughout the full-coverage
        deployment; her gap-lane held blank even at maximum density — structurally significant but not
        a recognition event that moves the axis). The cl-d11 +0.5 2nd tranche is therefore NOT settled
        at c18; it is documented as a cost-forward carry to the d14 collapse settlement (c20), where the
        un-priced relational item the calculus comes for settles. The discipline is recorded in the
        relational_anchor_status axes_held rationale at c18 scenes s01/s02/s03/s05 + the AUTHORING NOTES.
        Auditor fault-004 (process-hygiene) requested this stamp to prevent spurious surfacing at b01c19
        Phase 0. Confirmed by auditor substance-b01c18-scenes.md and dramatist ACCEPT.

    - id: pl-2026-06-04-c17-002
      created_at: 2026-06-04T23:10:00Z
      created_by: "/and-substance chapter b01c17 Phase 5 (auditor fault-001 + audience trio + admin DEC-0094)"
      target:
        command: /and-write
        scope: "b01c17"
        phase: Phase 6
      severity: HARD
      description: |
        ENACTMENT GATE for /and-write b01c17. Three reviewers converged: the chapter's substance
        is interior-accounting and must be ENACTED as physical staging at bone level, not narrated
        as Taylor-interiority — or it risks SUBSTANCE-FLAT at Phase 6 bone-gate (esp. the two
        collapse axes whose trap-tightening mechanism the auditor found living only in
        substance_delta.notes, not chunk prose). Required bone-level enactment (consolidated):
        1. (auditor fault-001) s03 collapse-axis activation must be a bone giving the collapse a
           PHYSICAL form — what is structurally different in the architecture AFTER the writing
           that was not before (extraction now requires resolving the false record; the tether
           now carries the false attribution as a structural constraint). The trap made visible,
           not interiority about the trap.
        2. (audience watch 2) the Norren false-attribution staged as a present-tense physical
           write-action (pen on log, the three specific lines), not a summarized decision/plan.
        3. (audience watch 1) s01 wren-identification = feed-event bone (subject = the feed
           returning the gait), not Taylor-cognition; s02 accounting-recognition arrives through
           the pricing arithmetic (subject = the accounting), not Taylor's emotional register.
        4. (audience watch 3 / WCP) echo-naming uses cipher/shape-language form and CLOSES — no
           Taylor interiority after the shape-language statement (leave the pen, end the scene);
           s04 blank-ledger close = ENACTED ABSENCE (hand not writing / stylus past the column),
           not interior monologue about not writing.
        Earth-Bet fence: Khepri-echo shape-language only; NO Khepri/Gold Morning/parahuman leak
        (WCP Phase 5 CLEAN — keep clean). Chunk cold-read CHUNK-CLASS-B (DEC-0094 P); the genuine
        non-uninformedness signal (ledger-recalc over physical staging) is what this gate targets.
      context_refs:
        - active-project/staff/auditor/substance-b01c17-scenes.md  # fault-001
        - active-project/audience/cape-fic-reader/stm.md  # SW-c17-1..4
        - active-project/audience/literary-snob/stm.md  # SW-c17-LS-1..3
        - active-project/audience/worm-canon-pedant/stm.md  # SW-c17-WCP-1..3
        - active-project/staff/showrunner/memory.md  # chapters[b01c17].chunk_cold_read.cold_read_risk_carry
      resolution_suggestion: "/and-write b01c17 Phase 1 brief on enacted-not-narrated; Phase 6 bone-gate verifies"
      status: resolved
      resolved_at: 2026-06-04T23:55:00Z
      resolved_by: "/and-write b01c17 Phase 6 bone-gate (auditor gate-001: enactment-gate MET)"
      resolution_note: |
        All four enactment points verified MET at bone level by the Phase 6 auditor:
        (1) s03 collapse-axis physical form — @22 writes first Norren-attribution-line +
            @23 pen adds two supplementary lines; the false record now sits in the log
            (extraction requires resolving what is written). (2) Norren false-attribution as
            present-tense physical write-action — @21/@22/@23, no future-tense/summary framing.
            (3) s01 wren-identification as feed/log-event — @6 subject "the feed" / @7 subject
            "the coverage log", not Taylor-cognition. (4) Echo-naming closes on shape-language
            (@27 compound) + s03 leave-the-open-log (@28) + s04 enacted-absence positive-form
            (@33 lifts the pen / @34 column holds the blank slot). Audience 3-of-3 SUBSTANCE-FELT
            confirmed the enactment LANDS (the collapse axes felt as structural consequence, not
            arithmetic; the pen-on-page the tactical high point). Earth-Bet fence CLEAN.
            The interior-ledger-recalculation risk (the genuine cold-read signal) is targeted at
            bone level; remaining prose-render watches (s02 embodiment, returns-verb variation,
            leave-the-open-log not softened) carried to /and-stitch via scene-map protected-patterns.

    - id: pl-2026-06-05-c17-001
      created_at: 2026-06-05T00:30:00Z
      created_by: "/and-facets b01c17 Phase 5 audit (signal-008 + signal-009)"
      target:
        command: /and-facets
        scope: "b01c18"
        phase: Phase 1
      severity: SOFT
      description: |
        Two schema-hygiene carries from b01c17 facet authoring (audience-gate confirmed
        non-blocking; both relevant to future chapters):
        (a) signal-008: vibes-b01-c17 uses `++` ops on wren-stitch-maker-flea-bottom-ward
            (rising entrapment, tragic-causal) and jarvis-coin-kl-courier — `++` requires the
            keyword pre-seeded in the entity's vibes.md. Verify Wren's + Jarvis's vibes.md carry
            these keywords before b01c18 vibes authoring (else use `+` fresh-keyword form).
        (b) signal-009: five env state-update SEAMs touch props with no margit card —
            prop:oc-coverage-log, prop:apparatus-picture, prop:cost-ledger (possible identity
            with oc-feed-ledger), studio.dead-drop-channel.query-status. Margit referral pending;
            these props recur (coverage-log especially) and warrant cards before they accrue more
            state. Non-blocking for c17 (per-anchor resolution clean).
        Also minor: vibes keyword-spacing (signal-001, spaces vs hyphenated handles) + exposition
        header dash-form `b01-c17` vs undashed `b01c17` (signal-006) — normalize at next convenient pass.
      context_refs:
        - active-project/staff/auditor/facets-final-audit.md  # signals 001/006/008/009
        - active-project/theater/facets/vibes-b01-c17.md
        - active-project/theater/facets/state-updates-env-b01-c17.md
      resolution_suggestion: "verify Wren/Jarvis vibes pre-seed at /and-facets b01c18 Phase 1; margit prop-card referrals for coverage-log/apparatus/ledger"
      status: resolved
      resolved_at: 2026-06-05T00:00:00Z
      resolved_by: "/and-facets b01c18 vibes authoring (showrunner)"
      resolution_note: |
        (a) signal-008 resolved: Wren vibes.md carries rising entrapment (pre-seed) and
        tragic-causal (pre-seed); both ++ ops valid. Jarvis vibes.md carries rising entrapment
        (pre-seed) and tragic-causal (pre-seed); ++ ops valid. Used ++ form for all Wren and
        Jarvis entrapment/tragic-causal extensions in vibes-b01-c18.md. No fresh + misuse.
        (b) signal-009 (prop cards for coverage-log/apparatus/ledger): carried forward — not
        within scope of vibes authoring; margit referral still pending for future pass.

    - id: pl-2026-06-05-c17-001
      created_at: 2026-06-05T01:00:00Z
      created_by: "/and-stitch b01-c17 Phase 9 cold-read terminal gate"
      target:
        command: /and-write
        scope: b01-c17
        phase: null
      severity: SOFT
      description: |
        b01c17 (the use-vector intercept / Wren-screening forge) shipped SHIPPED-WITH-CAVEATS on a
        Class-B cold-read (CONTINUE=no; central event RECOVERED + summary maps to goal — "re-committed,
        small-scale, the sin they fled"; cause = design-inherent event-poverty / interior-accounting-
        density / withheld prior-chapter motive [Wren + override-architecture = Earth-Bet fence +
        c01-c16 reader context] / jargon-opacity, ALL pre-authorized in chunk_cold_read.cold_read_risk_carry
        per DEC-0094; auto-shipped terminal per the Phase-9 SHIPPED-WITH-RISK-RECORDED coupling, mirroring
        c14 DEC-0085 / c15 DEC-0087 / c16 DEC-0090 — the FIFTH consecutive [DEC-0095/PROP-0037 recurrence
        4->5]). Phase 8.5 coherence PASS (central-event-muffle does-not-fire; the forge lands as deliberate
        falsification, not muffled paperwork). The withheld-motive opacity is the known uninformed-reader
        artifact (the assembled book resolves it c01-c16). MANDATORY depth pass before book-close (gates
        /and-substance book b02 Phase 0 + /and-review verdict b01). Consume via /and-write b01c17 revise
        --from-signals + re-cascade; OR fold into /and-cohere b01 c13-c17 (the now-FIVE-consecutive-quiet
        accumulation c13/c14/c15/c16/c17 — the cohere stretch handler is the named accumulation lever per
        DEC-0095, and the more efficient path than per-chapter depth passes).
      context_refs:
        - active-project/staff/reviews/coldread-b01-c17-2026-06-05.md
        - active-project/staff/showrunner/memory.md  # chapters[b01c17].cold_read
        - staff/admin/process-proposals.md  # PROP-0037 (depth-pass-before-book-close HARD-abort, open/untriaged)
      resolution_suggestion: "/and-cohere b01 c13-c17 (five-consecutive-quiet accumulation handler, DEC-0095) OR /and-write b01c17 revise --from-signals + re-cascade"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-cohere-c1315-001
      created_at: 2026-06-04T00:00:00Z
      created_by: "/and-cohere b01 c13-c15 iteration-0 (naive Q6 borderline-high CAUTION)"
      label: apparatus-register-closing-gesture-cadence-hardening
      target: {command: /and-review, scope: "verdict b01", phase: null}
      severity: SOFT
      description: |
        Across c13/c14/c15 every chapter closes on the identical gesture — a withheld/unwritten
        ledger entry ("a finding... filed, held, walk on under it" c13 / "in the record without
        being written" c14 / "set no name down" c15). Naive cold-read: closing beat predictable
        by c15; a 4th consecutive chapter on this cadence would tip Q6 from CAUTION to FAIL (same
        family as the c06-c12 load-bearing Q6 FAIL fixed via prologue-variation). NON-LOAD-BEARING
        here. Partially addressed by the c15 depth-pass (vary the close). Watch the closing-gesture
        cadence at b02 chapter authoring; consider a closing-move variation pass if it recurs.
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-cohere-c1315-002
      created_at: 2026-06-04T00:00:00Z
      created_by: "/and-cohere b01 c13-c15 iteration-0 (naive Q5 CAUTION)"
      label: sensory-texture-thins-in-interior-accounting-centers
      target: {command: /and-stitch, scope: "*", phase: null}
      severity: SOFT
      description: |
        Sensory texture clusters at chapter openings + set-pieces (salt-fish brine, wax giving
        under thumb, Vhagar-heat "like a hand near a wall in the dark") but thins markedly through
        the long interior accounting passages (c14 middle, c15 closing third) where the world
        recedes into column/figure/entry abstraction. Vivid at the edges, abstract in the centers.
        NON-LOAD-BEARING. Grounding-ledger discipline already addresses this per-chapter; flagged as
        a cross-stretch tendency for stitch voice-embodiment awareness at b02.
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-04-cohere-c1315-003
      created_at: 2026-06-04T00:00:00Z
      created_by: "/and-cohere b01 c13-c15 iteration-0 (naive Q4 + dramatist axis4 CAUTION)"
      label: aemond-courier-atmospheric-walk-on-weighting
      target: {command: /and-review, scope: "verdict b01", phase: null}
      severity: SOFT
      description: |
        Aemond (c15) and the gap-lane courier (c14) each appear, do thematic work, exit within
        their chapter — atmospheric/specimen weighting rather than accruing presences. DELIBERATE
        (Aemond: "I routed nothing of him anywhere"; the apparatus brushing powers it cannot touch),
        and both are open hooks (hook-0006 Aemond, future payoff), so not a drop. The courier leg
        overlaps the pl-2026-06-04-002 depth-pass (courier-as-person). NON-LOAD-BEARING. Book-level
        awareness for /and-review verdict b01.
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-05-c18-001
      created_at: 2026-06-05T02:30:00Z
      created_by: "/and-substance chapter b01c18 Phase 5 (audience trio converging — worm-canon-pedant HARD watch + cape-fic-reader + literary-snob)"
      label: khepri-declarative-s02-enactment-gate-c18
      target:
        command: /and-write
        scope: "b01c18"
        phase: Phase 6
      severity: HARD
      description: |
        ENACTMENT / EARTH-BET-FENCE GATE for /and-write b01c18 Phase 6 bone-gate.
        b01c18s02 chunk prose contains the word "Khepri" in DECLARATIVE form: "the one piece of the
        architecture that is not Khepri. Everything else is." This departs from the established
        suppressed-shape-word form (c12: shape-word surfaces under pressure and is willfully suppressed)
        and the cipher-only form (c17: shape-language without the proper noun). The audience trio
        (worm-canon-pedant lead; cape-fic-reader SW-c18-CFR-1; literary-snob SW-c18-LS-1) converged:
        FENCE-RISK-NOT-FENCE-VIOLATED at chunk level — the register the declarative lands in is a
        BONE/PROSE decision, so the call moves to /and-write Phase 6.

        RULING (worm-canon-pedant): If bones deliver the s02 phrase as the NARRATING register's
        structural identification — subject = the architecture, NOT Taylor's interiority; the reader
        sees the identification, Taylor's POV does not NAME herself — the fence holds and the s05 irony
        is intact (the blank-column-where-full-recognition-would-go irony REQUIRES that Taylor is not
        naming herself Khepri). If ANY bone gives Taylor the interior recognition "I am Khepri" or any
        functional equivalent (Taylor naming herself = knowing what she is = collapses the suppression
        architecture the whole chapter builds), that bone is a HARD finding at Phase 6 and blocks persist.
        Two breaks fire simultaneously on violation: (1) Earth-Bet fence violated; (2) s05 irony collapses.

        The c18 AUTHORING NOTES section (d) already names the correct mitigation: "enactment in the
        physical act of opening the nodes + the count running past the threshold number, not in any
        interior accounting Taylor runs about it." /and-write Phase 1 must brief the bone-author on the
        register-split; Phase 6 verifies. Rest of chapter Earth-Bet fence is CLEAN (all other shape-
        language — "a different architecture, in a different place," "a city before this one," "before
        this city" — is suppressed cipher; s02 declarative is the ONLY fence-pressure point).
      context_refs:
        - active-project/audience/worm-canon-pedant/stm.md  # SW-c18-WCP-HARD-1 + explicit Khepri-fence ruling
        - active-project/audience/cape-fic-reader/stm.md    # SW-c18-CFR-1
        - active-project/audience/literary-snob/stm.md      # SW-c18-LS-1
        - active-project/staff/showrunner/memory.md          # chapters[b01c18].scenes[b01c18s02].chunk
      resolution_suggestion: "/and-write b01c18 Phase 1 brief bone-author on narrating-vs-interior register-split for the s02 Khepri identification; Phase 6 bone-gate verifies Taylor does not name herself"
      status: resolved
      resolved_at: 2026-06-05T04:30:00Z
      resolved_by: "/and-write b01c18 Phase 6 bone-gate (auditor KHEPRI-ENACTMENT-GATE MET + audience 3-of-3 SATISFIED)"
      resolution_note: |
        KHEPRI-ENACTMENT-GATE MET. The s02 threshold is enacted at bone level through architecture-as-subject
        (s02n07 "the architecture opens the nodes" — moral_framework -1.0 fires as the architecture's structural
        fact) and count-as-subject (s02n08 "the count crosses the threshold"). The word "Khepri" appears in NO
        SVO across all 46 bones; Earth-Bet hard-fence substring scan CLEAN. No bone gives Taylor the interior
        self-recognition "I am Khepri" or any equivalent. The s05 blank-column suppression irony survives
        (s05n10 "passes the recognition column" — full recognition deferred to d14). All three audience personas
        converged: SW-c18-WCP-HARD-1 / SW-c18-CFR-1 / SW-c18-LS-1 all SATISFIED. Evidence:
        active-project/staff/auditor/write-b01c18-bone-gate.md + the three audience STM Phase-6 blocks.

    - id: pl-2026-06-05-c18-002
      created_at: 2026-06-05T02:30:00Z
      created_by: "/and-substance chapter b01c18 Phase 5 (literary-snob + worm-canon-pedant soft watches) + Phase 5.5 admin DEC-0096 carry"
      label: c18-bones-execution-watches
      target:
        command: /and-write
        scope: "b01c18"
        phase: null
      severity: SOFT
      description: |
        Bones-execution watches for /and-write b01c18 Phase 1 scene-decomposition discipline (non-blocking;
        carried from Phase 5 audience soft watches + the dramatist montage note + admin DEC-0096 op-friction):
        (a) SW-c18-LS-2 / SW-c18-WCP-soft: s04 axis-slug language ("The position-world entry is:" /
            "The political_register-world entry is:") is planning-document annotation bleeding into Taylor's
            POV. MUST be stripped at bones — Taylor's ledger-consciousness uses operative accounting language
            (margin cipher read, line written, record closed), NOT axis-slug labels.
        (b) SW-c18-LS-3: s05 interior-accounting-density. Six distinct accounting entries in the closing
            scene must be structurally distinct bones with DIFFERENT physical grounding, not sequential
            iterations of the same ledger-closing weight. If collapsed, the c17 cold-read's interior-
            accounting-density risk fires in stitched prose.
        (c) dramatist montage note: s03 (six days) + s04 (nine days) span compressed time. Both must land as
            SPECIFIC events through compound-eye imagery (s03: grooms/maids/knight/septa as system-embodiment;
            s04: margin-cipher single-line confirmation), NOT as summary/montage narration.
        (d) admin DEC-0096 op-friction-signal: at least one scene should carry operational friction so the
            chapter is not a flawless-op-with-no-resistance (the surviving cold-read signal). A small
            on-page friction beat (a node that returns noise, a corridor that reads wrong, a near-miss on
            the Wren-screen) keeps the climax from reading as frictionless competence.
      context_refs:
        - active-project/audience/literary-snob/stm.md   # SW-c18-LS-2, SW-c18-LS-3
        - active-project/audience/worm-canon-pedant/stm.md
        - active-project/staff/reviews/chunk-coldread-b01c18-2026-06-05.md
        - staff/admin/decisions.md  # DEC-0096
      resolution_suggestion: "/and-write b01c18 Phase 1 decomposition honors (a)-(d); Phase 6/stitch verify"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-05-c18-003
      created_at: 2026-06-05T02:30:00Z
      created_by: "/and-substance chapter b01c18 Phase 5 (auditor fault-003)"
      label: cl02-cost-side-completed-verification-c18
      target:
        command: /and-substance
        scope: "book b02"
        phase: Phase 0
      severity: SOFT
      description: |
        Auditor fault-003 (FLAG, no criteria). b01c18s02 notes claim "cl02 cost side completed."
        c18 handoff_in shows moral_framework aggregate at -3, which equals cl02's total declared cost
        (moral_framework -3). If all prior -3 was drawn under cl02, the entry was exhausted before c18
        and c18's draw would attribute to a zero-capacity anchor; if prior draws split across
        cl03a/cl-d06/cl05, cl02 may still have had capacity for the c18 -1.0. The aggregate-state
        moral_framework notes show the collapse distributed across cl02 (c03) + cl-d06 (c06) + cl03a
        (c10/c12) + cl03a (c17) — suggesting cl02 was NOT the sole moral_framework anchor and the c18
        -1.0 attribution to cl02 needs a clean continuity reconciliation. Non-blocking for c18 (the
        magnitude and direction are correct; only the ledger-anchor attribution is in question).
        Verify at /and-substance book b02 Phase 0 continuity check (or a dedicated cost-ledger audit).
      context_refs:
        - active-project/staff/auditor/substance-b01c18-scenes.md  # fault-003
        - active-project/staff/showrunner/memory.md  # series.substance.cost_ledger cl02 (~line 1346); aggregate-state moral_framework notes
      resolution_suggestion: "cost-ledger continuity reconciliation at /and-substance book b02 Phase 0"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-05-c18-deptpass
      created_at: 2026-06-05T06:20:00Z
      created_by: "/and-stitch b01-c18 Phase 9 cold-read terminal gate"
      label: depth-pass-required-before-book-close-b01c18
      target:
        command: /and-write
        scope: b01c18
        phase: null   # gates BOOK-CLOSE, NOT a chapter Phase 0 (does NOT add an unacknowledged-substantive aggregate-state entry)
      severity: SOFT
      description: |
        b01c18 (the irrevocable-deployment climax) shipped SHIPPED-WITH-CAVEATS on a Class-B cold-read
        (CONTINUE=no; central event RECOVERED + one-line summary maps to goal — "a spy runs their whole
        network at maximum for two weeks to hand an enemy faction the intelligence they need, then shuts
        it down and notes they'll get no credit"; cause = design-inherent interior-accounting-density /
        no-dialogue / anti-climax (nothing-external-lands) / withheld prior-chapter motive (who is Wren/
        Sera/Jarvis/Norren = Earth-Bet fence + c01-c17 reader context) / mechanism-opacity, ALL
        pre-authorized in chunk_cold_read.cold_read_risk_carry per DEC-0096; auto-shipped terminal per the
        Phase-9 SHIPPED-WITH-RISK-RECORDED coupling, mirroring c14 DEC-0085 / c15 DEC-0087 / c16 DEC-0090 /
        c17 DEC-0094 — the FIFTH consecutive [PROP-0037 recurrence 5->6, DEC-0098]). Phase 8.5 coherence
        PASS (central-event-muffle does-not-fire; the KHEPRI-REGISTER-SPLIT does not abstract the deployment
        below legibility — exposition:2 @14 + before/after magnitude carry the event-weight). MANDATORY depth
        pass before book-close (gates /and-substance book b02 Phase 0 + /and-review verdict b01). Consume via
        /and-write b01c18 revise --from-signals + re-cascade; OR fold into /and-cohere b01 c13-c18 (the
        now-SIX-consecutive Class-B accumulation c13-c18 — the cohere stretch handler is the named
        accumulation lever per DEC-0095, and the more efficient path than per-chapter depth passes; DEC-0098
        elevates PROP-0037 triage urgency to HIGH before /and-review verdict b01).
      context_refs:
        - active-project/staff/reviews/coldread-b01-c18-2026-06-05.md
        - active-project/staff/reviews/coherence-b01-c18-2026-06-05.md
        - active-project/staff/showrunner/memory.md  # chapters[b01c18].cold_read
        - staff/admin/process-proposals.md  # PROP-0037 (depth-pass-before-book-close, open/untriaged; recurrence 6); DEC-0098
      resolution_suggestion: "/and-cohere b01 c13-c18 (six-consecutive-Class-B accumulation handler, DEC-0095/0098) OR /and-write b01c18 revise --from-signals + re-cascade"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-05-c19-001
      created_at: 2026-06-05T00:00:00Z
      created_by: "/and-substance chapter b01c19 Phase 5.5 (admin user-proxy DEC-0099)"
      label: c19-s04-label-reach-must-be-concrete
      target:
        command: /and-write
        scope: "b01c19"
        phase: Phase 6
      severity: HARD
      description: |
        DEC-0099 cold-read carry. The s04 central event — the witch-label reaching
        the upper city and reaching Daven's service-layer — was flagged at the chunk
        cold-read as inferred-off-page / asserted-not-dramatized. /and-write MUST land
        this as a concrete SVO bone on-page (the shuttered vat-house window, the empty
        corner across forty-three prior approaches, Daven's non-appearance as the
        readable instrument of the inference). An inferred-off-page arrival fires
        EVENT-NOT-CONCRETE (HARD) at Phase 6. This is the ONE finding from the c19
        chunk cold-read that is NOT auto-dispositioned at /and-stitch Phase 9 — it is
        tractable and must be staged concretely upstream.
      resolution_suggestion: "Phase 1 scene-decomposition: ensure s04 has a concrete central-event bone staging the shuttered-window/empty-corner instrument of the inference; Phase 6 verifies EVENT-NOT-CONCRETE clean on the s04 central event."
      status: resolved
      resolved_at: 2026-06-05T18:30:00Z
      resolved_by: "/and-write b01c19 Phase 6 bone-gate (auditor EVENT-NOT-CONCRETE clean on s04)"
      resolution_note: |
        s04 witch-label-reach staged concretely on-page: @28 the second-bell passes the empty Tallow Croft corner, @29 the vat-house shutter closes the window (against forty-three prior-open approaches), @31 daven absents the corner, @34 the coverage-map drops the daven node. Auditor Phase 6 confirmed EVENT-NOT-CONCRETE does not fire; the inference is carried by physical instruments, not inferred-off-page abstraction. HARD watch satisfied. (Stitch must preserve LABEL-REACH-CONCRETE per scene-map protected-patterns; a stitch-layer revert to interior inference reopens this as a NEW non-auto-dispositioned Phase-9 finding per DEC-0099.)

    - id: pl-2026-06-05-c19-002
      created_at: 2026-06-05T00:00:00Z
      created_by: "/and-substance chapter b01c19 Phase 5.5 (admin user-proxy DEC-0099)"
      label: c19-voice-risk-abstraction-muffle
      target:
        command: /and-stitch
        scope: "b01c19"
        phase: Phase 8.5
      severity: SOFT
      description: |
        DEC-0099 voice-risk carry (chunk_cold_read.voice_risk.triggered=true, signal B).
        ABSTRACTION-DOMINANT: chunk cold-read flagged heavy proprietary vocabulary
        ("the accounting", "bottlefly nodes", "contempt-color", "a different column")
        as a central-event-muffle risk. /and-stitch Phase 8.5 Check 3 must verify the
        s03 contempt-lock + s04 severance reach cold-reader legibility in assembled
        prose; prefer person-first faithful rendering over apparatus-register within
        the bone-faithfulness fence (PROP-0022 voice-embodiment). Also armed via the
        chunk_cold_read.voice_risk block in memory (auto-read at Phase 8.5).
      resolution_suggestion: "/and-stitch Phase 8.5 Check 3 central-event-muffle verification; Phase 4 voice-embodiment discipline."
      status: resolved
      resolved_at: 2026-06-05T20:05:00Z
      resolved_by: "/and-stitch b01c19 Phase 8.5 coherence (central-event-muffle check)"
      resolution_note: |
        Voice-risk signal-B muffle NOT-MATERIALIZED. Phase 8.5 armed central-event-muffle check confirmed both spine events reach cold-reader legibility AS events (s3 contempt-lock via stylus-beside-not-into choreography + dead-name-in-ledger figure, high confidence; s4 severance via empty-corner + shutter-against-43-approaches + Daven absence, high confidence). label-reach-concrete HARD watch did not reopen. Voice-embodiment person-first throughout.

    - id: pl-2026-06-05-c19-003
      created_at: 2026-06-05T00:00:00Z
      created_by: "/and-substance chapter b01c19 Phase 5 (audience trio bones-execution watches)"
      label: c19-bones-execution-watches
      target:
        command: /and-write
        scope: "b01c19"
        phase: null
      severity: SOFT
      description: |
        Three bones-execution watches the audience trio attached to their c19 3-of-3
        SUBSTANCE-FELT ACCEPT, for /and-write Phase 1 scene-decomposition discipline:
        (SW-c19-CFR-1, cape-fic-reader) s02 "not a feeling, an observation" must land
          at bone level as a physical enumeration act through the accounting's own
          arithmetic — NOT a labeled interior-state shift.
        (SW-c19-CFR-2, cape-fic-reader) s03 "beside, not away from" (Taylor sets the
          stylus beside the ledger, not away from it) must be an ENACTED physical
          distinction at bones level; two-bone minimum; structural, not a prose flourish.
        (SW-c19-DFR-1, dark-fantasy-reader) s04 "The contempt is complete. The
          continuation is unchanged." must land as a HORROR-beat (the trap completing),
          not a resolution-beat — this is primarily a /and-stitch Phase 4 register
          concern (see pl-2026-06-05-c19-004) but the bones must not pre-resolve it.
      resolution_suggestion: "/and-write Phase 1 honors CFR-1 (enumeration-act bones) + CFR-2 (two-bone beside-distinction); Phase 6 verifies."
      status: resolved
      resolved_at: 2026-06-05T18:30:00Z
      resolved_by: "/and-write b01c19 Phase 4+6 audience bone-gate (CFR-1 + CFR-2 CLOSED)"
      resolution_note: |
        SW-c19-CFR-1 CLOSED: s02 pattern-recognition lands as physical enumeration (@10 runs the factional-reading column / @11 the column repeats its shape / @13 marks the column entry), not an interior-state label. SW-c19-CFR-2 CLOSED: s03 beside-not-away is a two-bone-plus enacted distinction (@24 lifts the stylus -> @25 the stylus meets the ledger-edge -> @26 the ledger-edge receives the stylus). SW-c19-DFR-1 (s04 close horror-beat-not-resolution) carries to /and-stitch Phase 4 -> tracked at pl-2026-06-05-c19-004.

    - id: pl-2026-06-05-c19-004
      created_at: 2026-06-05T00:00:00Z
      created_by: "/and-substance chapter b01c19 Phase 5 (dark-fantasy-reader SW-c19-DFR-1)"
      label: c19-s04-close-horror-not-resolution
      target:
        command: /and-stitch
        scope: "b01c19"
        phase: Phase 4
      severity: SOFT
      description: |
        SW-c19-DFR-1 (dark-fantasy-reader). The s04 close couplet "The contempt is
        complete. The continuation is unchanged." must land in prose as a horror-beat
        (the trap completing one chapter before the catastrophe), NOT as a wrap-up /
        resolution-beat. The dramatist also flagged that these summary lines risk
        becoming a tell that competes with the showing already in the scene. /and-stitch
        Phase 4 voice-transform must render the close so the unchanged-continuation is
        the horror, not the resolution.
      resolution_suggestion: "/and-stitch Phase 4 register-execution: render the s04 close as horror-beat; avoid tell-competing-with-show on the summary couplet."
      status: resolved
      resolved_at: 2026-06-05T20:05:00Z
      resolved_by: "/and-stitch b01c19 Phase 4 voice-transform + Phase 8.5"
      resolution_note: |
        Render honored horror-beat-not-resolution: close couplet weighted to continuation ("The architecture is still running, one node lighter... and the count that took the node out sits in no record I have written today"). Not warmed, not resolved. Phase 8.5 flagged low-med residual resolution-reading risk, within pre-authorized Class-B category (a) per DEC-0099; accepted at SHIPPED-WITH-CAVEATS.

    - id: pl-2026-06-05-c19-005
      created_at: 2026-06-05T00:00:00Z
      created_by: "/and-facets b01c19 Phase 5b (audience-native soft flag, no auditor convergent)"
      label: c19-expo3-conditional-framing
      target:
        command: /and-stitch
        scope: "b01c19"
        phase: Phase 3
      severity: SOFT
      description: |
        exposition:3 @27 ("the cost of being one of them has been priced") approaches
        present-tense certainty BEFORE the inference instruments (@28 empty corner /
        @29 shuttered window / @31 Daven absents) confirm the break. /and-stitch must
        render expo:3 as Taylor's operative inference-FRAMEWORK (what a contact-break
        means given the witch-label traveling), NOT as confirmed knowledge at the moment
        of scene-arrival. The @28/@29/@31 instrument sequence retains its evidentiary
        force only if expo:3 reads as conditional framing, not established fact. Also
        carries NI:3 @14 (flatten thesis-statement surface, preserve non-continuation
        content) per the same audience-gate.
      resolution_suggestion: "/and-stitch Phase 3 sequencing: expo:3 conditional, instruments evidentiary; NI:3 @14 flatten-explanatory."
      status: resolved
      resolved_at: 2026-06-05T20:05:00Z
      resolved_by: "/and-stitch b01c19 Phase 3 sequencing"
      resolution_note: |
        expo:3 @27 rendered CONDITIONAL ("if the witch-label has reached the people who know my accessible face, then the cost... has been priced, and a closed shutter is what the price looks like from the lane") - inference-framework not confirmed-arrival; the @28/@29/@31 instruments retain evidentiary force. NI:3 @14 flattened from thesis-statement to enacted prose ("the naming was not the stop. The entry going forward unchanged was").

    - id: pl-2026-06-05-c19-deptpass
      created_at: 2026-06-05T20:05:00Z
      created_by: "/and-stitch b01c19 Phase 9 cold-read terminal gate"
      label: depth-pass-required-b01c19-book-close
      target:
        command: /and-write
        scope: "book-close"
        phase: null
      severity: HARD
      description: |
        b01c19 shipped SHIPPED-WITH-CAVEATS (Phase 9 cold-read CONTINUE=no on pre-disposed
        Class-B grounds: interior-sameness + abstraction-density; DEC-0099 coupling). The
        mandatory depth-pass gates BOOK-CLOSE (NOT b01c20 Phase 0): before /and-review verdict
        b01 / /and-postop b01c19 milestone / /and-substance book b02, this chapter (and the
        c14-c18 cohort) needs the depth-pass resolution per the SHIPPED-WITH-CAVEATS contract.
        6th consecutive Class-B (c14-c19). Candidate: /and-write b01c19 revise --from-signals
        consuming the cold-read confusion log (chamberlain-half abstraction; the two-thread
        structure reading theme-linked-not-causal). NOT a b01c20 Phase 0 blocker — c20 Phase 0
        stays CLEAR.
      resolution_suggestion: "book-close: /and-write b01c19 revise --from-signals + re-cascade, OR principal accepts the Class-B cohort caveat at /and-review verdict b01. Consider /and-cohere b01 c13-c19 for the accumulated Class-B stretch."
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-06-cohere-001
      created_at: 2026-06-06T22:00:00Z
      created_by: "/and-review cohere b01 all (dramatist promise/payoff REVISE)"
      label: sera-payoff-weight-drop-whole-book
      target:
        command: /and-write
        scope: "b01c03"
        phase: null
      severity: SOFT
      description: |
        Whole-book cohere (FAIL-COHERE) load-bearing finding on the dramatist promise/payoff axis,
        surviving Phase 3 triage as the one item NOT already principal-accepted at book scope.
        Sera Hightower is the entire cost-justification of the Otto arrangement (introduced c03,
        the court-tier [protect-target] whose quiet Taylor buys) but the reader never feels her
        weight: she never appears as a person, her threat is never staged, and the c20 decommission
        does not confirm she was protected. The moral engine's human face reads as a ledger entry.
        DISTINCT from the on-page non-naming, which is BY DESIGN (pl-2026-05-28-002, verified c05 —
        Taylor never articulates the Sera-link; it lives at the facet layer). This finding is at the
        reader-reception / whole-book payoff layer, not the on-page-articulation layer. Secondary:
        Norren's c17 false-attribution consequence is deferred-then-unpaid (series-HOLD / book-DROP).
        NOTE: the book is complete + shipped + verdict-PASSED (PASS-WITH-NOTES) + Class-B cohort
        accepted at DEC-0105. Fixing this requires a substantive revise mutating finished drafts
        (c03 establish + c20 confirm at minimum). Fire-vs-defer decision routed to principal per
        Rule 13; NOT auto-fired by /and-cohere Phase 4. Recorded primarily as analysis input.
        SPLIT: this item = c03 ESTABLISH-leg only (add reader-facing Sera weight at introduction
        point). The c20 CONFIRM-leg (decommission must confirm protect-target was actually shielded)
        is tracked separately at pl-2026-06-06-cohere-002.
      context_refs:
        - active-project/staff/reviews/cohere-b01-all-20260606T215813Z.md
        - active-project/staff/reviews/cohere-dramatist-b01-all-20260606T215813Z.md
        - active-project/staff/showrunner/parking-lot.md  # pl-2026-05-28-002 (on-page non-naming = design)
        - staff/admin/decisions.md  # DEC-0105 (book-close Class-B cohort acceptance)
      resolution_suggestion: "principal decision: (a) accept as documented structural note on a finished book (fold into analysis); or (b) /and-write b01c03 revise --from-signals + c20 + re-cascade to add Sera reader-facing weight (substantive; mutates shipped drafts)"
      status: resolved
      resolved_at: 2026-06-07T03:45:00Z
      resolved_by: "surgical re-stitch (DEC-0113) — c03 establish-leg integrated to draft/b01-c03.md; confirmed ACCEPT by dramatist re-cohere (cohere-confirm-sera-20260607.md)"
      resolution_note: "c03 cooper's-yard passage revised: Jarvis stages Sera's concrete fate (put out / record does not reopen) in courier register; Taylor's stakes-beat lands the human fact BARE (principal note 'no accounting' — ledger-framing removed); grounding beat (boy at hoop-stack) added; fence held (Taylor names no motive). Dramatist confirm Q1+Q4: reader-facing weight CLOSES, no residue."

    - id: pl-2026-06-06-cohere-002
      created_at: 2026-06-06T23:00:00Z
      created_by: "fixer fault-004 (cohere-b01-all-aggregate-audit split; companion to pl-2026-06-06-cohere-001)"
      label: sera-payoff-weight-drop-c20-confirm
      target:
        command: /and-write
        scope: "b01c20"
        phase: null
      severity: SOFT
      description: |
        CONFIRM-leg companion to pl-2026-06-06-cohere-001 (c03 establish-leg). The c20
        decommission scene (Taylor exits KL, the Otto arrangement ends) does not confirm
        that the protect-target (Sera Hightower) was actually shielded — the reader never
        receives a payoff signal that the arrangement achieved its stated purpose. The
        moral engine's guarantee fires hollow at close: c03 introduced Sera as the cost-
        justification, but c20 decommissions the architecture without confirming the
        protection succeeded. Per the whole-book cohere (FAIL-COHERE,
        dramatist-promise-payoff axis), this is the CONFIRM half of the two-chapter
        repair: c03 establishes Sera as a felt person (establish-leg), c20 confirms the
        protect-target was shielded (confirm-leg). NOTE: same constraints as c03 establish-
        leg — book is complete + shipped + verdict-PASSED (PASS-WITH-NOTES) + principal-
        accepted per DEC-0108. Any revise mutates a finished terminal draft. This item is
        only actionable if the principal authorizes Phase 4 dispatch per DEC-0108's
        fire-vs-defer decision. Recorded as analysis input.
      context_refs:
        - active-project/staff/reviews/cohere-b01-all-20260606T215813Z.md
        - active-project/staff/reviews/cohere-dramatist-b01-all-20260606T215813Z.md
        - active-project/staff/showrunner/parking-lot.md  # pl-2026-06-06-cohere-001 (establish-leg; this item is the confirm-leg)
        - staff/admin/decisions.md  # DEC-0108 (phase 4 fire-vs-defer — defer accepted; revise-dismissal on finished+accepted book)
      resolution_suggestion: "confirm-leg companion to pl-2026-06-06-cohere-001; only actionable jointly with that item if principal authorizes /and-write b01c03 + b01c20 revise + re-cascade"
      status: resolved
      resolved_at: 2026-06-07T03:45:00Z
      resolved_by: "surgical re-stitch (DEC-0113) — c20 confirm-leg integrated to draft/b01-c20.md; confirmed ACCEPT by dramatist re-cohere (cohere-confirm-sera-20260607.md)"
      resolution_note: "c20 decommission paragraph: payoff confirmed as OVERTAKEN BY EVENTS (principal decision) — the council that could rule on Sera's parentage is filing into the junctions to take the crown; the question has nowhere left to be asked. No-accounting, fence held, minor-key (pre-Wren). Dramatist confirm Q2+Q3: payoff lands + stays subordinate to Wren climax, CLOSES."

    - id: pl-2026-06-07-pipeline-001
      created_at: 2026-06-07T01:15:00Z
      created_by: "/and-review pipeline legs23 (STRUCT-025) + admin DEC-0111"
      label: rubric-exposition-deferred-to-b02
      target:
        command: /and-substance
        scope: "b02"
        phase: null
      severity: SOFT
      description: |
        STRUCT-025 (pipeline legs23) found .claude/commands/and-facets.md Phase 1 item 10
        named a nonexistent design/shoot-v2/rubric-exposition.md as the exposition facet's
        authority. The exposition facet shipped all 20 b01 chapters WITHOUT that rubric,
        operating off schema § exposition + the union-of-audience-personas gap test +
        the context-ledger discipline + glossed-terms.md. DEC-0111 resolved the HARD by
        DE-REFERENCING (and-facets.md item 10 now names the real authority sources; dead
        pointer removed). A dedicated rubric-exposition.md is DEFERRED to b02-activation:
        if a second book is authorized, author rubric-exposition.md (REJECT / anti-pattern /
        cross-facet-contract sections, matching the other 9 rubric-*.md) using 20 chapters
        of real exposition-author behavior as evidence. No action while b01 is the only book.
      context_refs:
        - active-project/staff/reviews/pipeline-legs23-20260607T010305Z.md  # STRUCT-025
        - .claude/commands/and-facets.md  # Phase 1 item 10 (de-referenced)
        - schemas/facet.schema.md  # §exposition (the operating authority)
        - staff/admin/decisions.md  # DEC-0111
      resolution_suggestion: "at b02-activation (/and-substance book b02 or first b02 /and-facets): author design/shoot-v2/rubric-exposition.md from schema §exposition + b01 exposition-author corpus, then restore the rubric reference in and-facets.md item 10"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-08-slimfacets-001
      created_at: 2026-06-08T00:00:00Z
      created_by: "/and-facets b01-c07 slim-pipeline live test (DEC-0116 validation)"
      target:
        command: /and-facets
        scope: "*"
        phase: Phase 4
      severity: SOFT
      description: |
        During the URI-FACETS-SLIM live test on b01-c07, the Phase 4 auditor returned
        2 false-positive HARD findings ("feeling files absent", "actor state-update files
        absent") because it searched for ABBREVIATED actor slugs (feeling-taylor-b01-c07.md)
        instead of the full per-character slug filenames that exist on disk
        (feeling-taylor-hebert-kl-122ac-b01-c07.md). Caught by the Rule-19 on-disk verify;
        no real defect. Root cause: the test skipped the Phase 2 cite-index merge, which in
        production consolidates per-character slices into feeling.md / state-updates.md with
        a manifest the auditor reads — so this class does NOT arise in a normal run. BUT it
        is a real robustness gap: the auditor brief should resolve per-character slice files
        by GLOBBING the full actor slug (feeling-*-<book>-<chapter>.md), not by reconstructing
        an abbreviated name, so a partial/merge-skipped run cannot produce phantom-absent HARDs.
      context_refs:
        - active-project/staff/reviews/slim-facets-test-b01-c07.md  # caveat 1
        - active-project/staff/auditor/facets-final-audit.md  # FIXER RESOLUTION + CORRECTION addendum
        - .claude/commands/and-facets.md  # Phase 4 auditor read-inputs (slice file resolution)
      resolution_suggestion: "harden the /and-facets Phase 4 auditor read-inputs brief: enumerate per-character slice facets by glob over the full actor slug (feeling-*-<chapter>.md, state-updates-*-<chapter>.md) and treat a STRUCTURAL absent-file finding as valid only after a glob confirms absence — never from a reconstructed abbreviated filename."
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-08-sameness-001
      created_at: 2026-06-08T00:00:00Z
      created_by: "structural-sameness detector (PROP-0052 prototype run) on rebuilt b01 mid-book"
      target:
        command: /and-cohere
        scope: "b01 c11-c19"
        phase: null
      severity: SOFT
      description: |
        SAMENESS-HIGH on the rebuilt b01 mid-book: 8 of 10 chapters c10-c19 run one scene template
        (TEMPLATE-T: packet-arrives -> transcribe-to-channel -> withhold-the-protected-name -> lift-stylus
        -> hand-off-surface). The withhold-name invariant + meaning-accretion (Wren -> false-name ->
        blank-column -> Daven) is BY DESIGN and earns the c20 payoff; the problem is RUN-LENGTH at the
        tail (unbroken c17->c18->c19 right before the payoff; c19 narrates its own repetitiveness) and
        a literal terminal tic ("the hand came off the surface") in 6 chapters. The no-ledger rebuild
        made the sameness more legible, not less. Cheapest fix = LIGHT targeted cohere on 3 chapters,
        NOT a restructure: (1) c18 PRIMARY — re-anchor scene entry/exit off-template to break the
        c17-c19 run (/and-write revise on entry/exit bones; zero substance-delta change); (2) c11
        TERTIARY — swap scene-entry so it does not open with the same packet-arrives beat as adjacent c12;
        (3) terminal-tic SECONDARY — vary the lift-stylus/hand-off close on ~3 of the 6 sharing chapters.
        Leave c13/c16 (the dialogue-argument breaks) and the withhold-name invariant untouched.
        NOTE: this MUTATES shipped+assembled drafts (completed-works/book-one.md) — archive baselines
        first per the revisions protocol; principal-gated (do not auto-fire).
      context_refs:
        - active-project/staff/reviews/sameness-scan-b01-c08-c20.md
        - staff/admin/process-proposals.md  # PROP-0052
      resolution_suggestion: "principal greenlight -> /and-cohere b01 c11-c19 (light, 3-chapter structural pass per the scan's cheapest-fix list); archive draft baselines first; re-run the sameness detector + /and-review cohere on c11-c19 to confirm the run broke"
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-08-formdebt-001
      created_at: 2026-06-08T00:00:00Z
      created_by: "cross-chapter bones form-scan (post-no-ledger-rebuild certification)"
      target:
        command: /and-write
        scope: "b01 (perception-heavy chapters: c03 c04 c06 c07 c08 c09 c12 c14 c18)"
        phase: null
      severity: SOFT
      description: |
        The no-ledger rebuild re-emitted all 20 b01 chapters' bones via a render shortcut that SKIPPED
        the bones-gate. Cross-chapter form-scan (bones-formscan-b01-2026-06-08.md) found SYSTEMIC SVO-form
        debt: ~95 fault instances across 19 of 20 chapters (only c01/c02 near-clean). BUT severity is
        mostly beneath-the-prose hygiene, NOT reader-facing:
          - ABSTRACTION-AS-SUBJECT (the DEC-0115 no-ledger fence — the thing that mattered): only 1-2
            instances book-wide. The rebuild HIT its primary target. The single clean fence violation is
            c19:25 "the contempt rests beside the work" (highest-priority single fix).
          - PERCEPTION-VERB (~46, "watches X"): dominant debt; partially reader-facing (cold-distance);
            the stitcher rendered past these (why the prose cold-read still PASSED — verdict-rebuilt-b01).
            Worst pocket: c18.
          - STATIVE (~28, "holds the feet" motif): hygiene only + design-intentional; does not survive to prose.
          - ABSTRACTION-OBJECT (~18): hygiene.
        The reader-facing PROSE passes (PASS-WITH-NOTES re-certification, verdict-rebuilt-b01-2026-06-08).
        This is bone-layer hygiene debt, logged as b01 known-debt — it does NOT block forward motion.
      context_refs:
        - active-project/staff/reviews/bones-formscan-b01-2026-06-08.md
        - active-project/staff/reviews/verdict-rebuilt-b01-2026-06-08.md  # process caveat (form-scan resolution)
        - staff/admin/decisions.md  # DEC-0115 (no-ledger fence — the axis the rebuild cleared)
      resolution_suggestion: "OPTIONAL + principal-gated (mutates shipped drafts via re-cascade). Minimum: fix the single DEC-0115 fence fault c19:25 (1 bone + re-stitch c19). Fuller: a fixer-class /and-write revise form-pass on the 9 perception-heavy chapters (~45 bone-line edits, no substance-arc change) -> re-cascade. Tolerate-to-b02 is defensible: the prose cold-read passed; this is hygiene beneath alive prose."
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-11-pipeline-001
      created_at: 2026-06-11T00:00:00Z
      created_by: "improvement-loop/test run 1 (/and-review pipeline)"
      target:
        command: /fixer
        scope: "schemas/audit-report.schema.md"
        phase: null
      severity: SOFT
      description: |
        schemas/audit-report.schema.md retains a live-schema R2 decision-shard section
        (objects: r2-decision-shard, r2-decisions-consolidated, F-R2-* failure classes,
        f-r2-counts frontmatter, cite_index_hash REQUIRED field) — all from the R2 round
        retired by DEC-0116. Also: "Phase 6 verdict reads f-r2-counts" reference is stale;
        current /and-facets orchestrator-critic verdict is Phase 5, not Phase 6.
        Fix: mark R2 section RETIRED/DEPRECATED with DEC-0116 reference + date, or move to
        archive. Correct Phase 6 → Phase 5 in the consumer contract note.
      context_refs:
        - active-project/staff/reviews/pipeline-2026-06-11T000000Z.md
        - schemas/audit-report.schema.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-11-pipeline-002
      created_at: 2026-06-11T00:00:00Z
      created_by: "improvement-loop/test run 1 (/and-review pipeline)"
      target:
        command: /fixer
        scope: ".claude/commands/and-write.md"
        phase: null
      severity: HARD
      description: |
        .claude/commands/and-write.md Phase 4 (Trim) audience dispatch context block loads
        `series.theme` — a field that does not exist in schemas/showrunner-memory.schema.md.
        The series block defines series.chunk, series.substance, series.laws, series.lore,
        series.behaviors, series.vibe_cloud — no series.theme at any path. A dispatch loading
        a missing key will silently load nothing or mismatch. Thematic content likely intended
        lives in series.chunk.path.{motivation,trade,irony} or series.substance.state_axes[].
        Fix: replace `series.theme` with the correct schema field(s) per showrunner-memory.schema.md.
      context_refs:
        - active-project/staff/reviews/pipeline-2026-06-11T000000Z.md
        - .claude/commands/and-write.md
        - schemas/showrunner-memory.schema.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-11-pipeline-003
      created_at: 2026-06-11T00:00:00Z
      created_by: "improvement-loop/test run 1 (/and-review pipeline)"
      target:
        command: /fixer
        scope: ".claude/commands/and-facets.md"
        phase: null
      severity: HARD
      description: |
        .claude/commands/and-facets.md Phase 5c (orchestrator-critic verdict) reads the OC card
        from `staff/audience/and-facets-orchestrator-critic/card.md`. The canonical path per
        CLAUDE.md routing table is `staff/orchestrator-critic/card.md`. The
        `staff/audience/and-facets-orchestrator-critic/` path does not correspond to any
        registered directory. A silent card-miss on this path invalidates the facet-layer
        success gate (SUCCESS / SHIPPABLE-WITH-CAVEATS / NOT-SUCCESSFUL).
        Fix: correct Phase 5c to read from `staff/orchestrator-critic/card.md`. If a
        facet-specific OC variant is intentional, register it in CLAUDE.md routing table.
      context_refs:
        - active-project/staff/reviews/pipeline-2026-06-11T000000Z.md
        - .claude/commands/and-facets.md
        - CLAUDE.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null

    - id: pl-2026-06-11-pipeline-004
      created_at: 2026-06-11T00:00:00Z
      created_by: "improvement-loop/test run 1 (/and-review pipeline)"
      target:
        command: /fixer
        scope: "schemas/showrunner-memory.schema.md"
        phase: null
      severity: SOFT
      description: |
        /and-stitch Phase 8.5 actively writes chapters[<slug>].coherence_review to showrunner
        memory (subfields: reviewed_at, verdict, weave_gaps, followability_breaks,
        cold_read_risk_high, cold_read_risk_advisory, findings, report_path). This field is NOT
        defined in schemas/showrunner-memory.schema.md. This is a fully wired, actively executed
        phase — not a pending-triage item. Schema validation will surface it as an unknown field.
        Fix: add chapters[<slug>].coherence_review with all Phase 8.5 subfields to the memory schema.
      context_refs:
        - active-project/staff/reviews/pipeline-2026-06-11T000000Z.md
        - schemas/showrunner-memory.schema.md
        - .claude/commands/and-stitch.md
      status: open
      resolved_at: null
      resolved_by: null
      resolution_note: null
