# showrunner memory — schema: schemas/showrunner-memory.schema.md

routing:
  show_file: active-project/theater/show.md
  episode_plan: active-project/theater/episode-plan.md
  series_plan: active-project/staff/showrunner/series-plan.md
  season_plan: active-project/staff/showrunner/season-s01-plan.md

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
        status: faceted-r1
        narrator: taylor-hebert-jaehaerys
        chunk: "Show the audience the shape of the household Taylor wakes into and the apprentice mark that fixes her visible role inside it."
        proto_lines_path: active-project/theater/proto-lines/s01e01.md
        facets_path: active-project/theater/facets/
        round_1_complete: true
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

active:
  season: s01
  episode: s01e01
