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
    # Episodes are not pre-listed under aggregate-first /and-season.
    # /and-season Phase 4 splits the converged season aggregate into N episodes
    # (N a multiple of 3, decided by ideal size + dramatic shape) and writes the
    # episodes[] array at that point. Until then the canonical content scope
    # for the season lives in season-s01-plan.md as continuous content guidance.
    episodes: []
    next_season_sketch: "The steward's quarterly monitoring report names Mira's market-day gatherings as the new perimeter, and the lord's apparatus shifts from incident-response to patterned-response as Taylor's coalition expands past the family she can individually shield; the suppression apparatus gains institutional vocabulary for what it is watching, while Taylor's Shard-weighted instinct to escalate rather than withdraw pulls her into confrontations that cost the coalition members she cannot protect from the institutional record."

active:
  season: s01
  episode: ~  # set by /and-season Phase 5 once split decides actual episodes
