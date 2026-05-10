# showrunner memory — schema: schemas/showrunner-memory.schema.md

routing:
  show_file: active-project/theater/show.md
  episode_plan: active-project/theater/episode-plan.md
  series_plan: active-project/staff/showrunner/series-plan.md
  season_plan: active-project/staff/showrunner/season-s02-plan.md
  season_plan_s01: active-project/staff/showrunner/season-s01-plan.md

series:
  theme: "What it costs to build something in a world that does not have a word for what you are building — and what gets charged to people who never agreed to pay."
  laws:
    - cond-feudal-hierarchy-law
    - cond-westerosi-customary-authority-jaehaerys
    - cond-suppression-policy-progression
    - cond-series-tone-constraints-84ac
  lore:
    - cond-riverlands-84ac-state
    - cond-faith-of-seven-jaehaerys
    - cond-maester-network-behavior
    - cond-westerosi-superstition-frame
    - cond-no-parahuman-infrastructure
    - cond-reincarnation-mechanics-84ac
  behaviors:
    - cond-smallfolk-political-physics
    - cond-fauna-control-rules
    - cond-shard-behavioral-weight
    - condition-swarm-in-foreign-ecology
  plot:
    start: "A reincarnated organizer wakes in a smallfolk child's body in a Riverlands market town, carrying thirty years of foreknowledge and a cape-war's worth of failure modes, with no authority, no legible identity, and no institutional channel through which any of it applies."
    end: "At the Great Council of 101 AC, the suppression apparatus built against Taylor's coalition over seventeen years renders judgment — not through defeat, but through the costs coming due at the worst possible moment, leaving what survives in damaged, diminished, or transformed form as the Dance approaches regardless."
    protagonist_arc: "Taylor arrives operational and willing, builds outward from Fairstead through every form of informal coalition her instincts can generate, extracts the institutional response she was always going to extract — and discovers across seventeen years that her control calculus is not a tool she deploys but a tax she levies on everyone who trusts her; the Great Council closes not on whether she was right, but on what being right the way she is right has cost."
    series_question: "Can a structure built from below, by someone who cannot stop running the control calculus on the people she recruits, hold together long enough to matter — and what does it cost the people inside it when it does?"
  cast_roster:
    - taylor-hebert-jaehaerys: "lead — Taylor reborn smallfolk Riverlands ~84 AC, dyer's daughter, Fairstead"
    - oc-craftsman-mother: "Elara Ashford — warm constraint; senses Taylor is strange"
    - oc-craftsman-father: "Edwyn Ashford — dyer-with-accounts; Taylor's first social map"
    - oc-lords-steward: "Aldric Pryor — Ryger steward; first institutional record-maker"
    - septon-rowan: "Fairstead parish septon; sincere theology-around-Taylor"
    - mira-stonefield-jaehaerys: "~50; smallfolk peer-ally + community-elder function fused"
    - rymer-hedge: "Riverlands hedge knight; ground-level non-convert witness"
    - oc-child-peer: "Clem Ferris — reeve's son, age ~8; genuine peer mirror"
  stage_elements:
    - loc-river-market-town: "Fairstead — composite primary setting, Blue Fork tributary"
    - loc-craftsman-workshop-home: "Ashford dye-workshop and dwelling"
    - loc-market-square: "ignition site (~86 AC tax-collection swarm event)"
    - loc-local-sept: "Septon Rowan's seat; Taylor's literacy-origin"
    - loc-river-ferry-dock: "town's throat; census/taxation chokepoint"
    - westerosi-smallfolk-village-common: "ambient texture; smallfolk exterior"
    - westerosi-smallfolk-dwelling-interior: "ambient texture; smallfolk interior"

seasons:
  - slug: s01
    window: "~84-88 AC"
    status: active
    plan: active-project/staff/showrunner/season-s01-plan.md
    chunk: "The tax-collection swarm event at ~86 AC converts Taylor from invisible smallfolk child to a named anomaly in Aldric Pryor's incident log, and the institutional apparatus that will eventually suppress her coalition takes its first documentary step; Taylor's counter-move is to build depth before breadth, recruiting Mira Stonefield and establishing the sept as her literacy and information node, but the same control instincts that make her effective keep her parents at managed distance and Mira at arm's length precisely when closeness would be cheaper. The personal cost begins paying out before the season closes: Elara Ashford cannot be kept at arm's length indefinitely, and before S1 ends the lord's traveling maester arrives at Fairstead under cover of routine ledger work — the steward's note has reached him, and the board has changed."
    episodes:
      - slug: s01e01
        status: faceted-r2  # 2026-05-10 Plan C C1 COMPLETE: re-fired /and-facets-r2 on R1 baseline with edited command (post URI-023 #9 + B2a G5 position-gate). Native .r2-decisions.md emitted. Gate PASS (0 F-R2-1; F-R2-2/3/4 sum=2 ≤ 2).
        narrator: taylor-hebert-jaehaerys
        chunk: "Show the audience the shape of the household Taylor wakes into and the apprentice mark that fixes her visible role inside it."
        proto_lines_path: active-project/theater/proto-lines/s01e01.md
        facets_path: active-project/theater/facets/
        round_1_complete: true
        round_2_complete: true
        round_3_complete: false
        audit_complete: false
        prior_state_archived_branch: r2-tuning-pre-rerun
        r2_decisions_path: active-project/theater/facets/.r2-decisions.md
        r2_decision_shard_paths:
          - active-project/staff/interest-narrator/r2-decision-shard.md
          - active-project/staff/memory/r2-decision-shard.md
          - active-project/staff/feeling/r2-decision-shard-taylor-hebert-jaehaerys.md
          - active-project/staff/feeling/r2-decision-shard-oc-craftsman-mother.md
          - active-project/staff/feeling/r2-decision-shard-oc-craftsman-father.md
          - active-project/staff/metaphor/r2-decision-shard.md
        r2_summary: "28K/1D/8R/3A; cap-refusals 25; F-R2-counts {1:0, 2:0, 3:0, 4:2}; discipline-fails 0; 1 inline T1 self-resolved; 5 margit referrals queued"
        tuning_rounds_complete:
          - memory (legacy 3-persona pattern; 100% pass / 75% clean)
          - feeling (legacy 3-persona; 92% pass / 75% clean; URI-008 cleared)
          - narrator-interest (legacy 3-persona; 100% pass / 78% clean; +3 file-level adds for channel coverage)
          - vibes (legacy 3-persona; 100% pass / 95% clean; AP8 mass cleanup; vibes:19 WITHDRAWN)
          - sensory (TIGHTER-AUDIENCE pilot; 100% pass / 83% clean post sensory:4 @60->@61 fix; 3 specialist critic cards authored under staff/audience/sensory-*)
        pattern_summary: 4 facets shipped under legacy 3-persona uniform pattern; 1 facet shipped under tighter-audience pattern (pilot validated 2026-05-10g pivot)
        orchestrator_critic_path: active-project/staff/auditor/orchestrator-critic-verdict.md
        orchestrator_critic_status: NOT-SUCCESSFUL on first fire (5/7 criteria) — fixes applied (sensory:4 relocated; this memory updated); re-fire pending
        cast: taylor-hebert-jaehaerys, oc-craftsman-mother, oc-craftsman-father
        locations: loc-craftsman-workshop-home
        prior_episode: none
        aggregate_range: 1-149
      - slug: s01e02
        status: protolined
        narrator: taylor-hebert-jaehaerys
        chunk: "Show the audience Septon Rowan establishing a literacy-shaped pastoral claim on Taylor that she cannot decline."
        proto_lines_path: active-project/theater/proto-lines/s01e02.md
        cast: taylor-hebert-jaehaerys, septon-rowan, oc-craftsman-mother
        locations: loc-local-sept, loc-craftsman-workshop-home
        prior_episode: s01e01
        aggregate_range: 150-250
      - slug: s01e03
        status: protolined
        narrator: taylor-hebert-jaehaerys
        chunk: "Show the audience another child noticing too closely and the lord's-steward census filing the household into folios Taylor cannot reach."
        proto_lines_path: active-project/theater/proto-lines/s01e03.md
        cast: taylor-hebert-jaehaerys, oc-child-peer, oc-craftsman-mother, the cloth-factor's wife, oc-craftsman-father, rymer-hedge, oc-lords-steward, the ferryman, the town reeve, the fishwife, the clerk, septon-rowan
        locations: loc-market-square, loc-river-ferry-dock, loc-local-sept
        prior_episode: s01e02
        aggregate_range: 251-418
      - slug: s01e04
        status: protolined
        narrator: taylor-hebert-jaehaerys
        chunk: "Show the audience the swarm break the collection and the steward mark the incident folio — the season's first irreversible act."
        proto_lines_path: active-project/theater/proto-lines/s01e04.md
        cast: the collector, oc-craftsman-father, taylor-hebert-jaehaerys, mira-stonefield-jaehaerys, rymer-hedge, oc-lords-steward, the townsman, the collector's man, oc-craftsman-mother, the post rider, the town reeve
        locations: loc-market-square, loc-craftsman-workshop-home
        prior_episode: s01e03
        aggregate_range: 419-563
      - slug: s01e05
        status: protolined
        narrator: mira-stonefield-jaehaerys
        interlude: true
        chunk: "Show the audience Mira transact the recruitment arc's first earn at the cost of an unnamed debt, then return Taylor home to a household not yet in concert."
        proto_lines_path: active-project/theater/proto-lines/s01e05.md
        cast: mira-stonefield-jaehaerys, taylor-hebert-jaehaerys, the town reeve, oc-lords-steward, rymer-hedge, oc-craftsman-mother, oc-craftsman-father
        locations: loc-market-square, loc-craftsman-workshop-home
        prior_episode: s01e04
        aggregate_range: 564-699
      - slug: s01e06
        status: protolined
        narrator: oc-craftsman-mother
        interlude: true
        chunk: "Show the audience Elara close Taylor's separate-vector parent management and the maester's folio cross the water — the note has traveled and the apparatus knows the name."
        proto_lines_path: active-project/theater/proto-lines/s01e06.md
        cast: oc-craftsman-mother, septon-rowan, the town reeve, oc-craftsman-father, taylor-hebert-jaehaerys, the maester, mira-stonefield-jaehaerys, rymer-hedge, the ferryman
        locations: loc-local-sept, loc-craftsman-workshop-home, loc-river-market-town, loc-river-ferry-dock, loc-market-square
        prior_episode: s01e05
        aggregate_range: 700-912
    protolines_complete:
      timestamp: 2026-05-09
      aggregate_path: active-project/theater/proto-lines/s01.aggregate.md
      audit_paths:
        phase2_pass2_constraint: active-project/staff/auditor/season-s01-pass-2-constraint-reaudit-r6.md
        phase2_pass3_shape: active-project/staff/auditor/season-s01-pass-3-shape-reverification.md
        phase2_pass4_trim: active-project/staff/auditor/season-s01-pass-4-trim-{persona}-r2|r3.md
        phase2_pass5_continuity: active-project/staff/auditor/season-s01-pass-5-continuity-r2.md
        phase3_pass_S1_constraint: active-project/staff/auditor/season-s01-pass-S1-constraint-r2.md
        phase3_pass_S2_shape: active-project/staff/auditor/season-s01-pass-S2-shape.md
        phase3_pass_S3_trim: active-project/staff/auditor/season-s01-pass-S3-trim-{persona}-r2|r3|r4.md
        phase3_pass_S3_5_ruleset: active-project/staff/auditor/season-s01-pass-S3.5-ruleset-r2.md
        phase3_pass_S4_continuity: active-project/staff/auditor/season-s01-pass-S4-continuity-r2.md
        phase3_pass_S5_voice: active-project/staff/auditor/season-s01-pass-S5-voice-coherence.md
        phase3_pass_S6_vibe: active-project/staff/auditor/season-s01-pass-S6-vibe-{persona}.md (CARRY-FORWARD — see escalation note)
        phase3_pass_S7_facet_readiness: active-project/staff/auditor/season-s01-pass-S7-facet-readiness-r2.md
        phase3_pass_S8a_character_plausibility: active-project/staff/auditor/season-s01-pass-S8a-plausibility-character-r2.md (CARRY-FORWARD on Elara-reeve — see escalation note)
        phase3_pass_S8b_event_plausibility: active-project/staff/auditor/season-s01-pass-S8b-plausibility-event-r2.md
        phase3_pass_S9_comprehensibility: active-project/staff/auditor/season-s01-pass-S9-comprehensibility-{persona}.md (CARRY-FORWARD — see escalation note)
        phase4_split_proposal: active-project/staff/auditor/season-s01-split-proposal.md
        phase4_split_review: active-project/staff/auditor/season-s01-split-review-{persona}.md (2-of-3 ACCEPT)
      carry_forward_notes:
        - active-project/staff/showrunner/escalation-pass2-cap-decision.md
        - active-project/staff/showrunner/escalation-s6-vibe-drift-carry-forward.md
    next_season_sketch: "The steward's quarterly monitoring report names Mira's market-day gatherings as the new perimeter, and the lord's apparatus shifts from incident-response to patterned-response as Taylor's coalition expands past the family she can individually shield; the suppression apparatus gains institutional vocabulary for what it is watching, while Taylor's Shard-weighted instinct to escalate rather than withdraw pulls her into confrontations that cost the coalition members she cannot protect from the institutional record."
    terminal_handoff:
      to_season: s02
      handoff_date: 2026-05-10
      apparatus_tier_at_close: networked-surveillance (maester visited Fairstead, traced literacy register, made notation on Taylor, crossed ferry with folio)
      apparatus_tier_at_s02_open: networked-surveillance entering patterned-response (Pryor's quarterly cycle established as recurring institutional rhythm)
      open_threads:
        - mira_recruitment: tacit; debt unnamed; Mira withheld from Pryor in S1 inquiry (s01e05); not yet a coalition
        - rowan_pastoral_claim: active; literacy-access continuing under pastoral framing; not Taylor's to refuse; S2 deepens, S3 fracture-point
        - clem_ferris_noticing: live but unprocessed; Taylor carries variable she cannot fully model; ages parallel to Taylor in S2
        - rymer_hedge_witness: saw Taylor watching ignition without acting; S2 elevates to ground-level recurrent presence
        - family_in_concert: closed (S1 e06); Elara-Edwyn-Rowan triangle active; manage-parents-as-separate-vectors pattern terminated
      vibe_deltas_to_s02:
        - foregrounded: pryor-as-author-of-vocabulary, quarterly-monitoring-rhythm, coalition-discovers-the-withholding, adolescent-body-ceiling, blue-fork-road-as-perimeter, late-s2-dissolution
        - shifted: intimate-cost (S1 primary) → coalition-cost (S2 primary); the-steward register sharpens to pryor-as-author-of-vocabulary
        - attenuated: family-as-vector becomes continuous low-grade presence rather than primary driver
      named_terminal_image: Taylor in the loft, swarm-sense tracking sept fly + dock mosquito + ferry folio crossing the water; Elara calls; Taylor presses the loft floor

  - slug: s02
    window: "~88-94 AC"
    status: active
    plan: active-project/staff/showrunner/season-s02-plan.md
    plan_log: active-project/staff/showrunner/season-s02-plan-log.md
    chunk: "The steward's quarterly monitoring cycle converts Mira's market-day gatherings from a social nuisance into a named target on Pryor's institutional perimeter — and Taylor's counter-response is to build depth and geographic breadth before the patterned-response apparatus finishes naming what it is watching. The arc turns on a single structural liability: the Shard's weight toward escalation and the coalition's expanding exposure travel in the same direction at the same time, and the people Taylor recruited to trust her are sitting inside that convergence without knowing the shape of what she withholds from them. By season close, Mira publicly dissolves her market-day gatherings under the monitoring record's direct institutional pressure — the relationship does not break, but the structure Taylor built around Mira does not survive, and what remains is smaller and harder to rebuild."
    plan_iteration_history:
      - iteration_1: dark-fantasy-reader ACCEPT; pulp-enthusiast REVISE-B1-BORED-B6-HOOK-WEAK; worm-canon-pedant REVISE-B4-information-asymmetry-tracking-gap; dramatist ACCEPT
      - iteration_2: ACCEPT all 3 personas + dramatist (with execution constraint at H section regarding coalition-discovers-the-withholding distribution to B6 Mira interlude)
    episodes_planned:
      - slug: s02e01-planned
        beat: "Pryor's perimeter — dock sentry posted on report-day, new physical perimeter"
        status: planned
        narrator: taylor-hebert-jaehaerys
      - slug: s02e02-planned
        beat: "coalition expansion pressure — Blue Fork road expansion + Mira's gatherings named on Pryor's quarterly report"
        status: planned
        narrator: taylor-hebert-jaehaerys
      - slug: s02e03-planned
        beat: "body-clock event — adolescent ceiling shifts (~91 AC); season hinge"
        status: planned
        narrator: taylor-hebert-jaehaerys
      - slug: s02e04-planned
        beat: "garrison copy — Pryor sends acknowledgment-by-hand instruction; Rymer behavioral anomaly logged by Taylor's passive-sense"
        status: planned
        narrator: taylor-hebert-jaehaerys
      - slug: s02e05-planned
        beat: "confrontation — Pryor's directive to reeve about discouraging large gatherings; Taylor intervenes; season peak"
        status: planned
        narrator: taylor-hebert-jaehaerys
      - slug: s02e06-planned
        beat: "dissolution — Mira dissolves market-day gatherings; tributary-village newcomer arrives at sept; season close"
        status: planned
        narrator: mira-stonefield-jaehaerys
        interlude: true
    notes:
      planned_episode_count: 6 (multiple of 3 ✓)
      slug_provisional: "the planned slugs above are content anchors; final slugs decided at /and-season Phase 4 split"
      next_session_action: "/and-season s02 — the heavy run with tens bone-gate first live-fire (URI-026)"
    and_season_run_2026_05_10:
      status: PHASE-4-INCOMPLETE (FAIL F7-bone)
      orchestrator_verdict: FAIL — F7-bone (2 tens-gate-residual-HARD findings; URI-026 bone-gate first live-fire validated mechanism)
      verdict_path: active-project/staff/auditor/season-s02-orchestrator-verdict.md
      phase_2_status: iteration 2 applied (regen by screen-writer; iter-2 not formally re-audited; documented gap)
      phase_3_status: SKIPPED (deferred to next session per orchestrator budget; documented gap)
      phase_4_status:
        step_1: COMPLETE (split proposal: 6 episodes; SPLIT-PROPOSAL-COMPLETE; 2 band exceedances flagged at E1+E2; POV honored)
        step_1_5: COMPLETE-WITH-FAIL (URI-026 bone-gate first live-fire; tens authored for 6 episodes; SHAPE-FAIL HARD on s02e01 + s02e02; SHAPE-OK or borderline on others)
        step_2: NOT-RUN (gated on Step 1.5 convergence per F7-bone protocol)
        step_3: NOT-RUN (gated on Step 2)
      bone_gate_uri_026_validation:
        mechanism: WORKED-AS-DESIGNED
        what_it_caught: s02e01 inert-stretch (31 contiguous rung-1) + scene-peaks-absent + single-peak-in-205-bones; s02e02 gathering-scenes-no-rupture-beat + coalition-arc-undercharged
        what_pre_bone_gate_would_have_missed: Pass 4 audience trim returned stretch-flatlines but no per-episode actionable kickback; Pass 3 shape returned 3 different-axis faults; tens-rating produced explicit per-episode SHAPE-FAIL verdicts with criteria
        evidence: active-project/staff/auditor/season-s02-pass-S4-step1.5-tens-mega.md
      next_session_actions:
        - screen-writer regen on s02e01 (add ≥2 rupture beats: 1 in Mira-first-exchange scene + 1 in reeve-household scene; minimum +1 rung-3 in 1-130 range)
        - screen-writer regen on s02e02 (add ≥1 rupture beat in gathering scenes 358-396 OR 461-489 — Mira commits publicly / is witnessed / is recorded)
        - Re-fire Step 1.5 tens for s02e01 + s02e02 only (per-spec parallel-fork dispatch this time for round-trip verification; iteration 2 of bone-gate; cap=2 per window)
        - If Step 1.5 iter-2 PASSes: proceed to Step 2 (audience x3 + mechanic auditor) for all 6 episodes
        - If Step 1.5 iter-2 still HARD on s02e01 or s02e02: F7-bone FAIL persists; escalate to user for plan-level reconsideration of those beats
      orchestrator_critic_notes:
        - Phase 2 iter-2 unverified (acceptable — not F6 because no convergence claim made)
        - Phase 3 entirely skipped (acceptable — not F1 because explicit deferral, not iteration-cap-hit-without-convergence)
        - Step 1.5 single-fork deviation (per-spec parallel-fork verification recommended next iteration)
      f_r2_counts: not-fired (no /and-facets-r2 run on s02 corpus; expected — facet authoring stage not reached)

active:
  season: s02
  episode: s01e01  # not advanced; Phase 4 did not converge to per-episode files

tuning_r1_status:
  phase: I-complete
  date: 2026-05-10
  decisions_file: design/shoot-v2/and-season-tuning-r1/E-r2-defense.md
  prior_decisions_file: design/shoot-v2/and-season-tuning-r1/E-defense.md
  user_verdicts_file: design/shoot-v2/and-season-tuning-r1/I-user-verdicts.md
  defend: 2
  revise: 15
  withdraw: 0
  defend_with_carry_back: 0
  shippability: SHIPPABLE-PENDING-EXECUTION (no remaining human escalations)
  auditor_findings_resolved: 5 HARD all closed (fault-001 RESOLVED by URI-010 Option A; fault-002 covered by U12; fault-004 U16 amended with Taylor-POV bisection check; fault-005 RESOLVED by URI-009 plan-designated-narrator verdict; fault-AP-1 covered by U17 REVISE)
  pending_subtasks:
    dramatist: boundary-rebalance for U3/U13 (e02/e03 cut near 207), U14 (e03/e04 cut to 370 with e04 over-band resolution), U16 (e05/e06 — amended: must verify cut does not bisect Taylor-POV stretch 645-699 OR Elara-POV stretch 700+; provisional 692 target may be non-compliant; dramatist must map marker positions and recommend compliant cut or confirm only 699 is valid)
    screen_writer: bone additions/revisions for U1 (3 bones at post-IGNITION ratchet-clicks 496-499, 530-545, 800-820), U2 (2-3 bones at e01 episode lines 10-30), U6, U7, U9, U10, U11, U17 (targeted pass on 20 named instances: 35, 277, 293, 332, 349, 386, 390, 417, 427, 440, 502, 518, 560, 583, 629, 642, 699, 789, 799, 907; coordinate line 699 with U11)
    showrunner_self: aggregate_range header updates for e01 (1-148), and pending boundary-rebalance outcomes for e02/e03/e04/e05/e06
    human_escalation: none remaining
  carry_back_queue:
    - URI-007 idiom-depletion rubric formalization — V2 quantified mechanic (10+-instance / 25%-contextual-differentiator criterion)
    - URI-008 denouement-share quantification (LATE-WEIGHT >40% candidate)
    - URI-009 narrator-field rule — USER-VERDICT-RECEIVED (designate-at-plan-time wins); V2 rubric edit candidate to /and-season Phase 4 Step 3
    - URI-010 aggregate non-monotonic IDs schema — USER-VERDICT-RECEIVED (Option A; legal survivors); V2 schema clarification + position-aware fixer-mapping note
    - URI-011 episode-shape mechanics for Phase 4 Step 2 (3 sub-mechanics drafted)
    - URI-012 post-split continuity pass S4.5 (new pass)
    - URI-013 S3 vs S9 entertainment-density reconciliation (recommended Option A, explicit-different-purposes)
    - URI-014 season-scope adversarial criteria per persona (per-card schema addition)
    - URI-015 S6 vibe-drift resolution path (when carry-forward is permitted)
    - URI-016 S8a/S8b split-verdict adjudication (restrictive-verdict-wins default)

tuning_r2_status:
  phase: D-complete
  date: 2026-05-10
  type: meta-tuning of review critics
  trigger: user direction — "antagonistic feedback based on tighter audience rather than formulaic scoring; tune our review critics within the process itself"
  hypotheses_predicted: 4
  hypotheses_confirmed: 4
  sleepers_surfaced: 4 (U5 dark-fantasy SHAPE-COHERENT, U3 worm cost-inversion, U4 pulp fishwife misdirection, U2 worm apprentice-mark register failure)
  r1_accepts_flipped: 1 (U5 from F ACCEPT-WITH-CAVEAT to STRONG)
  auditor_classes_needing_refinement: 3 of 11 (CURVE-SHAPE, CONSTRAINT, AP-SCAN)
  auditor_classes_correctly_calibrated: 6 of 11 (STRUCTURAL, METADATA-INCONSISTENCY, DEDUP, FREQUENCY-BAND, PILE-UP, CONTRADICTION, TASTE-FLAG)
  carry_back_queue:
    - URI-017 persona-card Threshold Discipline section (audience-role schema)
    - URI-018 auditor sub-class CURVE-SHAPE-EPISODE-INTERIOR (depends on URI-011)
    - URI-019 auditor sub-classes CONSTRAINT-BEHAVIOR-SEQUENCE + CONSTRAINT-RESPONSE-BONE-REQUIRED (depends on URI-003 card additions)
    - URI-020 auditor sub-class AP-SCAN-POST-PEAK-WINDOW-QUALITY (depends on URI-018)
    - URI-021 meta-tuning loop pattern documentation
  total_v2_carry_backs_r1_plus_r2: 15 (URI-007 through URI-021)
  no_corpus_mutations: true (R2 produces critic improvements only; R1 routed subtasks still apply)

pipeline_landing_status:
  date: 2026-05-10
  landed_items: 11 of 15 V2 carry-backs (URI-007 through URI-017)
  landed_files:
    - .claude/commands/and-season.md (URI-007 idiom-depletion S3.5; URI-008 denouement-share LATE-WEIGHT in S2; URI-009 plan-designated narrator in Phase 4 Step 3; URI-010 position-aware-mapping note in Phase 4 Step 3; URI-011 mechanic-bearing OPEN-ENGAGES/CLOSE-EARNS-NEXT/SHAPE-COHERENT in Phase 4 Step 2; URI-012 new Pass S4.5 post-split-continuity; URI-013 S3-vs-S9 different-purposes note; URI-015 S6 drift-resolution routing; URI-016 S8 split-verdict adjudication)
    - schemas/card.schema.md (URI-017 Threshold Discipline body section; URI-014 Season-Scope Adversarial body section in audience role)
    - active-project/audience/dark-fantasy-reader/card.md (URI-017 + URI-014 persona-specific content)
    - active-project/audience/pulp-enthusiast/card.md (URI-017 + URI-014 persona-specific content)
    - active-project/audience/worm-canon-pedant/card.md (URI-017 + URI-014 persona-specific content)
  remaining_v2_items: 4 (URI-010 schema-side clause optional; URI-018, URI-019, URI-020 auditor sub-classes — gated on URI-006 dedicated auditor-tuning project; URI-021 meta-tuning-loop documentation)
  pipeline_state: V2 LIVE — next /and-season run uses landed mechanics

orchestrator_critic_landed:
  date: 2026-05-10
  uri: URI-022
  card_path: staff/orchestrator-critic/card.md
  invocation: /and-season Phase 6 (Orchestrator verdict)
  scope: library-only; no per-project copy
  thresholds:
    hard_dispatch_cap: 60
    soft_dispatch_cap: 30
    iteration_cap_per_phase: 3
    soft_wallclock_hours: 8
  verdict_format: [PASS, PASS-WITH-NOTES, FAIL]
  failure_modes: 6 (F1 non-convergence; F2 forward-flag breach; F3 hard-rule violation; F4 unrouted-HARD-finding; F5 cap-thrash without rubric carry-back; F6 convergence claimed but residuals masked)
  rule_10_added: /and-season runs gated at Phase 6 by orchestrator-critic; FAIL escalates to user
  retroactive_self_audit: deferred — would assess R1's s01 run against this standard; running it would produce a back-graded verdict on a closed run, useful as calibration data but not as a current decision input

bone_gate_landed:
  date: 2026-05-10
  uri: URI-026
  plan_path: design/shoot-v2/session-plan-2026-05-10-bone-gate.md
  parallel_session: /and-facets tuning ran concurrently; coordinate review side-by-side before next /and-season fire
  next_session_action: |
    Open the plan file (design/shoot-v2/session-plan-2026-05-10-bone-gate.md) AND the /and-facets
    session's plan (whatever the parallel session produced) and review them together for a
    comprehensive integrated picture of the bones-first + shared-reviewer architecture before any
    new /and-season or /and-facets fire. Particular focus: (a) confirm the shared-reviewer assertion
    holds (no facet-session edits collide with /and-season bone-gate edits); (b) Phase 1.5
    persona-card body promotion is unblocked once facet session merges; (c) URI-018/019/020
    sub-classes can land into the shared auditor library and benefit both pipelines.
  landed_files:
    - .claude/commands/and-season.md (Phase 4 Step 1.5 added; Step 2 extended with bones+tens audience + narrow-scope mechanic auditor; REGEN-{REPLACE,ADD,BOTH} discipline; per-window inner cap 2; Phase 5 print summary updated)
    - staff/orchestrator-critic/card.md (F7 bone-gate residual auto-FAIL; B6 bone-gate convergence; §B6 in verdict template; R1 narrative updated; v1.1 versioning entry)
    - schemas/facet.schema.md (tens dual-provenance; /and-shoot Phase 0 rename note; shared class library principle)
    - CLAUDE.md (Rule 10 amended; Rule 11 shared reviewer resources)
    - design/shoot-v2/upstream-tuning-queue.md (URI-026 entry; supersedes URI-025 IP-2 author-mode tens block)
  deferred:
    - Phase 1.5: persona-card body promotion of tens-attack categories (deferred to post-facet-session merge)
    - Phase 2: sensory + state-updates env + loc-state migration; /and-facets-r1 Layer 1 deletion
  first_live_fire: /and-season-plan s02 then /and-season s02 (s01 corpus untouched)
