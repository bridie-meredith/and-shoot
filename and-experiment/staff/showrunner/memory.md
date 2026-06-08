# showrunner memory — schema: schemas/showrunner-memory.schema.md
# WORKSPACE: and-experiment (bones-first prototype — NOT active-project)
# This project was scaffolded by hand using /and-project as the structural model,
# then SEEDED from and-experiment/design/run-01/ (idea-board, constraints, treatment,
# book-outlines). Unlike a stock project it is authored bones-first: the bible
# already exists; the apparatus is reverse-derived rather than top-down generated.

project:
  brief: >
    A Targaryen princess who failed to get a dragon — and who is secretly a dead
    cultivation-novel addict with zero knowledge of Westeros — decides that if she
    can't ride the sacred beasts she'll grind them into immortality pills, and
    accidentally builds a realm-spanning trade-and-medicine empire to feed the habit,
    until the Dance of the Dragons hands her a sky full of corpses and takes everyone
    she refused to admit she loved.
  mode: bones-first-experiment
  source_design: and-experiment/design/run-01/
  constraints:
    settings:
      - King's Landing / Red Keep, reign of Viserys I, ~119–131 AC (pre-Dance build-up → the Dance)
      - Essos / Yi Ti / Sothoryos (Book II far-reagent expeditions)
    themes_as_bounds:
      - Comedy-first that curdles to tragedy on the canon Dance timeline (tone is a gradient, not flat)
      - Locked-inside POV — the reader hears the immortal's monologue; the world sees a child eating rocks
      - Cultivation cosmology is WRONG but the materials are genuinely magical (broken-clock seam)
      - Dramatic irony is the reader's — protagonist is setting-blind to Westeros
    hard_fences:
      - Protagonist is setting-blind — NO meta-knowledge of Westeros canon, houses, or the coming war
      - Canon-clean: an original younger daughter of Viserys I (his only canon daughter is Helaena)
      - Real Westeros magic only — she may misclassify, but invents no new substances
      - She never claims/rides a dragon; her power is logistics, not cultivation
  staff:
    audience: [youjo-senki-reader, danmachi-reader, literary-snob]   # youjo-senki + danmachi are library stubs — expand before review duty
    screen_writer: library-default
    dramatist: library-default
    auditor: library-default
    editor: library-default
    orchestrator_critic: library-default
  series_audit:
    approved_at: ~
    approved_by: ~
    report_path: ~
    stale_since: ~

series:
  chunk: >
    One cohesive work in three books — the same refusal at escalating scale. Saerys
    Targaryen builds higher walls against attachment and grief: first a delusion
    (cultivation), then an empire (logistics), then forbidden power (deep magic).
    Bound by three rhymes: (1) one method, three locks — a ledger defeats the
    household (Bk I), the world (Bk II), then the Crown and death itself (Bk III);
    (2) the family and chosen-family she gains in I–II are exactly who the war takes
    in III; (3) reagent tier ↔ geography ↔ tone climb in lockstep, farce → horror.
    Meta-question: will the immortal ever come down and be mortal? She doesn't — she
    runs. A tragedy in a comedy's clothes.
    ACCEPTED OUTLINE (canonical build target, converged + enriched):
    and-experiment/convergence/round-03/fusion-v2.md  (supersedes and-experiment/design/run-01/book-outlines.md).
    Unifying mechanism: the Cauldron-Belly (stomach-as-cauldron); power is poison + logistics, never martial.
    Convergence record: and-experiment/convergence/convergence-ledger.md.
    CONVERGED CHAPTER OUTLINE (30ch, 10/10/10): and-experiment/convergence/chapters/round-02/fusion.md
    (record: and-experiment/convergence/chapters/chapters-ledger.md). Gap cards provisioned by margit
    (and-experiment/warehouse, project-scoped): saerys-targaryen(+behavior), viserys-i-targaryen, helaena-targaryen-122ac,
    daenys-velaryon, ser-harwin-the-patient, nymeria-summer-isles, saerys-septa, comedy-register, loc-red-keep-interior.
  structure:
    book_count: 3
    book_length:
      chapters_per_book: 10       # converged (10/10/10) — chapters/round-02/fusion.md
      scenes_per_chapter: ~
      bones_per_scene: ~
    cyclical: false
    pov: first-person, single, locked-inside (Saerys)
    cross_book_continuity:
      recurring_antagonists: [the marriage-piece role, Otto Hightower (asset-filer), the Dance itself]
      ongoing_subplots: [the trade-and-medicine empire, the dragonrider-girl love, the entourage, the deep-magic horizon]
    world_evolution: pre-Dance court farce → world-spanning adventure → the Dance as apocalypse/windfall
    series_end_shape: ambiguous — the unsanctioned bookkeeping-escape voyage; seeking or fleeing left open
  laws:
    - source: and-experiment/design/run-01/constraints.md §1   # canon ground-truth: cradle-egg custom + failure, septa-handler, Maegor's Holdfast, Dragonpit, incest-marriage norms, betrothal ~13
  lore:
    - source: and-experiment/design/run-01/constraints.md      # full grounded bedrock (canon + the cage + the ship-heist toolkit + reuse map)
  behaviors:
    - westeros-noble-courtly (inherit) + westeros-grrm-mannerisms (overlay) — re-toned for comedy
  substance: ~   # state-axes seed (transcendence↔attachment, agency↔duty, cost-ledger of mortal lives) — to reverse-derive
  vibe_cloud:
    keys: []
  cast_roster:
    # straight-man court — existing library cards, reuse
    - {slug: alicent-hightower-122ac, role: mother / horrified straight-man, source: library}
    - {slug: otto-hightower, role: maternal grandfather / asset-filer, source: library}
    - {slug: aemond-targaryen-122ac, role: dragonless-by-conquest brother / foil, source: library}
    - {slug: rhaenyra-targaryen-122ac, role: half-sister / Black claimant, source: library}
    # to build (margit) — see open-questions.md
    - {slug: saerys-targaryen, role: PROTAGONIST, source: TO-BUILD}
    - {slug: helaena-targaryen-122ac, role: odd ally-sister / the warm spot, source: TO-BUILD}
    - {slug: viserys-i-targaryen, role: the good-king father, source: PROMOTE-FROM-SCANT (projects/project_05 actor copy)}
    - {slug: saerys-septa, role: central handler / chaperone, source: TO-BUILD}
    - {slug: dragonrider-girl-love-interest, role: love interest, source: TO-BUILD (OC vs canon Baela/Rhaena — open)}
    - {slug: entourage-bodyguards, role: found-family retinue / cost-made-flesh, source: TO-BUILD}
  stage_elements:
    # reuse near-verbatim
    - {slug: cond-kl-court-state-122ac, source: library}
    - {slug: cond-kl-geography-122ac, source: library}
    - {slug: cond-dragon-bonding-claiming-rules, source: library}
    - {slug: loc-dragonpit-interior, source: library}
    - {slug: loc-dragonpit-exterior, source: library}
    # gaps to build
    - {slug: loc-red-keep-interior, source: TO-BUILD (only loc-red-keep-outer-ring scant exists)}
    - {slug: comedy-register, source: TO-BUILD (whole substrate is grimdark)}

books:
  - id: b01
    title_slug: spirit-beast-essence
    delta: "age ~3–9 · Tier 0–1 · the Red Keep · PURE FARCE. Climax: defeats the cage (the King's-hand note). See book-outlines.md §Book I."
    status: outlined
  - id: b02
    title_slug: the-long-roads
    delta: "age ~9–13 · Tier 2–3 · Essos→Yi Ti/Sothoryos · adventure with teeth. Climax: defeats the world. Ends: Viserys dying. See §Book II."
    status: outlined
  - id: b03
    title_slug: the-field-of-corpses
    delta: "age ~13–15 · Tier 4 + curdle + escape · the Dance · tragedy→cold escape. Climax: the bookkeeping ship-heist. See §Book III."
    status: outlined

active:
  book: b01
  chapter: ~
  cascade_in_progress: false

routing:
  series_plan: and-experiment/staff/showrunner/series-plan.md
  staleness_log: and-experiment/staff/showrunner/staleness-log.md
  cascade_checkpoint: and-experiment/staff/showrunner/cascade-checkpoint.md
  reviews: and-experiment/staff/reviews/
  bones_dir: and-experiment/theater/bones/
  facets_dir: and-experiment/theater/facets/
  dialogue_dir: and-experiment/theater/dialogue/
  draft_dir: and-experiment/draft/
  cultivation_library: and-experiment/design/cultivation-library/INDEX.md   # FIRST-STOP reference for any cultivation-register / apothecary / substance scene. See INDEX for the full doc set + "use this when" map, the consolidated candidate-card list, [canon-uncertain] worklist, and open rulings. BLOCKING for Bk II+: T-1 oily-black-stone disposition, T-2 human-cauldron explicit-vs-latent, T-3 Daenys-death vs dao-companion archetype.
  counterfactual_life: and-experiment/design/counterfactual-life/INDEX.md   # FIRST-STOP reference for the EXTERIOR well — the ordinary princess life Gael deviates from (servants/handlers, the hour-by-hour day, the expectation-script). Matched pair with cultivation_library (interior well). The INDEX seam map is the production tool: every ordinary element → where the plot hides in/exploits/subverts it. Authored to the LIVE Gael/Jaehaerys-as-father layer (warehouse cards still carry stale Saerys/Viserys-father naming — drift flagged in the INDEX). Process that produced it (reusable): and-experiment/design/counterfactual-baseline-process.md.
