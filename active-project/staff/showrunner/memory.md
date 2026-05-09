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
    title: "The Steward's Note"
    window: "~84-88 AC"
    status: active
    plan: active-project/staff/showrunner/season-s01-plan.md
    chunk: "The tax-collection swarm event at ~86 AC converts Taylor from invisible smallfolk child to a named anomaly in Aldric Pryor's incident log, and the institutional apparatus that will eventually suppress her coalition takes its first documentary step; Taylor's counter-move is to build depth before breadth, recruiting Mira Stonefield and establishing the sept as her literacy and information node, but the same control instincts that make her effective keep her parents at managed distance and Mira at arm's length precisely when closeness would be cheaper. The personal cost begins paying out before the season closes: Elara Ashford cannot be kept at arm's length indefinitely, and before S1 ends the lord's traveling maester arrives at Fairstead under cover of routine ledger work — the steward's note has reached him, and the board has changed."
    episodes:
      - slug: s01e01
        title: "The Map Is Wrong"
        status: planned
        chunk: "Taylor's passive swarm-sense runs continuously in Fairstead's insect-wrong ecology while Edwyn returns from market with news that changes the household's week; the collision is whether she can hold the child-register long enough for the information to arrive through legitimate channels. What cannot remain unchanged: performing childhood costs something real, and that cost is already running — one thing in the household is different at episode-close from episode-open."
      - slug: s01e02
        title: "The Septon's Offer"
        status: planned
        chunk: "Taylor uses public piety as cover for literacy-access, but Septon Rowan extends a pastoral offer of letters-instruction before Taylor has decided whether to invite it; the collision is whether she can accept without giving Rowan something she cannot take back. What cannot remain unchanged: the sept is now Taylor's literacy node, and Rowan holds the first pastoral claim on her that she did not choose."
      - slug: s01e03
        title: "What Clem Saw"
        status: planned
        chunk: "Taylor's child-performance slips in the market square in front of Clem Ferris — adult-register precision that goes by too fast to name but not too fast to notice; the threshold is whether Clem's unprocessed noticing converts to adult attention before Taylor can assess the damage. What cannot remain unchanged: Taylor now carries a variable she cannot fully model — a child-witness whose honesty is structurally guaranteed and cannot be managed through the adult frames she can subvert."
      - slug: s01e04
        title: "Census at the Dock"
        status: planned
        chunk: "Pryor arrives at the river-ferry dock with a tax-census retinue — Rymer Hedge among the party — to update household rolls; the threshold is whether Taylor holds still while everything in her reads the fishwife's disputed account as the exact kind of coercion her power was calibrated to answer. What cannot remain unchanged: Pryor is a named face and has already requested the sept's literacy roster as routine census paperwork — a non-reactive paperwork pull that costs Taylor a management option before the ignition exists; Rymer files Taylor watching, without acting."
      - slug: s01e05
        title: "The Steward's Note"
        status: planned
        notes: "IGNITION ~86 AC; involuntary swarm rise; first institutional record"
        chunk: "The collection retinue returns for the seasonal levy; a contested-weight seizure triggers the swarm before Taylor decides — horses bolt, two men need treatment, the collection breaks — while Pryor watches from the far end of the square and makes the first institutional record of Taylor as a named anomaly. What cannot remain unchanged: Taylor is no longer invisible to power; the note exists; the season's spine snaps into place and everything after bends away from this."
      - slug: s01e06
        title: "What Mira Stonefield Knows"
        status: planned
        interlude: true
        narrator: mira-stonefield-jaehaerys
        chunk: "Pryor's inquiry reaches the market quarter; Mira Stonefield — ten feet from Taylor when the swarm rose — is the witness whose account would close the inquiry or open it further; the threshold is what Mira says, what she omits, and what she asks Taylor directly in the alley before Pryor reaches her door. What cannot remain unchanged: the first earn of the recruitment arc is transacted in what Mira does not say to Pryor; the debt between them is real, unnamed, and not yet a coalition."
      - slug: s01e07
        title: "Elara's Question"
        status: planned
        interlude: true
        narrator: oc-craftsman-mother
        chunk: "Elara goes to Septon Rowan with the wrongness she can feel but cannot name; Rowan answers in pastoral frame; the threshold is the irreversible action Elara takes after leaving him — she goes directly to Edwyn and the family unit re-coheres around concern for Taylor, closing Taylor's management of each parent as a separate vector. What cannot remain unchanged: Taylor closes the episode facing a present-tense decision: both parents are now acting in concert, and she must choose whether to begin lying explicitly to them or accept the closing of her operational cover."
      - slug: s01e08
        title: "Ledger Work"
        status: planned
        chunk: "The lord's traveling maester arrives at Fairstead on a Pryor-originated directive — Pryor specified the timing and what to look for, making the visit a Pryor move dressed as institutional routine — and Taylor must perform normalcy at the highest possible cost while the maester reads the town. What cannot remain unchanged: the note has crossed a tier; the apparatus that knows Taylor's name has expanded from local incident-log to networked-surveillance; the board has changed, and Taylor knows it."
    next_season_sketch: "The steward's quarterly monitoring report names Mira's market-day gatherings as the new perimeter, and the lord's apparatus shifts from incident-response to patterned-response as Taylor's coalition expands past the family she can individually shield; the suppression apparatus gains institutional vocabulary for what it is watching, while Taylor's Shard-weighted instinct to escalate rather than withdraw pulls her into confrontations that cost the coalition members she cannot protect from the institutional record."

active:
  season: s01
  episode: s01e01
