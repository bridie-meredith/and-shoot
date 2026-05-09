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
    - taylor-hebert-jaehaerys     # lead — Taylor reborn smallfolk Riverlands ~84 AC, dyer's daughter, Fairstead
    - oc-craftsman-mother          # Elara Ashford — warm constraint; senses Taylor is strange
    - oc-craftsman-father          # Edwyn Ashford — dyer-with-accounts; Taylor's first social map
    - oc-lords-steward             # Aldric Pryor — Ryger steward; first institutional record-maker
    - septon-rowan                 # Fairstead parish septon; sincere theology-around-Taylor
    - mira-stonefield-jaehaerys    # ~50; smallfolk peer-ally + community-elder function fused
    - rymer-hedge                  # Riverlands hedge knight; ground-level non-convert witness
    - oc-child-peer                # Clem Ferris — reeve's son, age ~8; genuine peer mirror
  stage_elements:
    - loc-river-market-town        # Fairstead — composite primary setting, Blue Fork tributary
    - loc-craftsman-workshop-home  # Ashford dye-workshop and dwelling
    - loc-market-square            # ignition site (~86 AC tax-collection swarm event)
    - loc-local-sept               # Septon Rowan's seat; Taylor's literacy-origin
    - loc-river-ferry-dock         # town's throat; census/taxation chokepoint
    - westerosi-smallfolk-village-common
    - westerosi-smallfolk-dwelling-interior

seasons:
  - slug: s01
    title: "The Steward's Note"
    window: "~84-88 AC"
    status: active
    plan: active-project/staff/showrunner/season-s01-plan.md
    episodes:
      - slug: s01e01
        title: "The Map Is Wrong"
        status: planned
      - slug: s01e02
        title: "The Septon's Offer"
        status: planned
      - slug: s01e03
        title: "What Clem Saw"
        status: planned
      - slug: s01e04
        title: "Census at the Dock"
        status: planned
      - slug: s01e05
        title: "The Steward's Note"
        status: planned
        notes: "IGNITION ~86 AC; involuntary swarm rise; first institutional record"
      - slug: s01e06
        title: "What Mira Stonefield Knows"
        status: planned
        interlude: true
        narrator: mira-stonefield-jaehaerys
      - slug: s01e07
        title: "Elara's Question"
        status: planned
        interlude: true
        narrator: oc-craftsman-mother
      - slug: s01e08
        title: "Ledger Work"
        status: planned

active:
  season: s01
  episode: s01e01
