# showrunner memory — schema: schemas/showrunner-memory.schema.md

routing:
  show_file: active-project/theater/show.md
  episode_plan: active-project/theater/episode-plan.md
  series_plan: active-project/staff/showrunner/series-plan.md
  season_plan: active-project/staff/showrunner/season-s01-plan.md

series:
  theme: protection-and-research-share-the-same-instrument; the guise of saving-the-world may already be eating the saving; cowing the world by being more frightening than the dragons that hold it.
  laws:
    - cond-shard-behavioral-weight
    - cond-no-parahuman-infrastructure
    - cond-smallfolk-political-physics
    - cond-feudal-hierarchy-law
    - cond-westerosi-customary-authority-125ac
    - cond-fauna-control-rules
    - cond-fauna-control-rules-125ac-addendum
    - cond-reincarnation-mechanics-125ac
  lore:
    - cond-westerosi-superstition-frame
    - cond-crownlands-superstition-frame-125ac
  behaviors:
    - cond-clinical-self-erasure
    - cond-series-tone-constraints-125ac
  plot:
    start: post-Khepri Taylor wakes in the just-dead body of Tya, a tanner-family daughter in a Crownlands village outside King's Landing, ~125 AC; shard reseeds at arrival; village reads her as "Tya who came back wrong."
    end: the Dance is over by rational deterrence after one rider-control demonstration; Taylor intact, smallfolk marginally better protected, the burned falsification record permanent, one experimental subject dead and one alive in four-hour memory increments, the scientific-caution self-narrative gone.
    protagonist_arc: from displacement-and-research-onset, through Khepri-threshold crossing (s2 peak), through the demonstration that cows both factions (s3 climax), into the foreclosure that detonates after the war ends (s4) — solitude as permanent condition, one witness (broken maester) who names the line and is not heard.
    series_question: when the guise of saving-the-world stops being a guise, can the person who paid that cost the first time stop themselves the second?
  cast_roster:
    - taylor-hebert-flea-bottom    # protagonist, only POV
    - oc-tanner-mother             # Tya-origin grief axis
    - oc-tanner-father             # Tya-origin suspicion axis
    - oc-tanner-elder              # Flea Bottom conditional embedder
    - oc-dock-runner               # Flea Bottom legs / trust-test
    - oc-tallow-chandler           # unknowing glass-candle salvage source
    - oc-broken-maester            # sole research witness; brake-not-ally
    - rhaenyra-targaryen           # black faction antagonist-instrument
    - aegon-ii-targaryen           # green faction figurehead antagonist
    - otto-hightower               # Hightower intelligence architect
    - aemond-targaryen             # green faction coercive instrument
    - viserys-i-targaryen          # background; dies pre-Dance
  stage_elements:
    - loc-tanner-village
    - loc-flea-bottom
    - loc-flea-bottom-base
    - loc-eastern-quarter-apothecary
    - loc-red-keep-outer-ring

seasons:
  - slug: s01
    chunk: "Taylor's insect-range expands through Flea Bottom while the tanner-village's ongoing claim on the body she inhabits and the Hightower apparatus's first miscategorized intelligence file close simultaneously around her; the season forecloses the possibility of working unnamed — she is already a misread fact in someone else's record before she understands what she is building."
    status: active
    plan_path: active-project/staff/showrunner/season-s01-plan.md
    content_beats: 26
    phase_1_converged_at: attempt-2-of-3
    drama: "The tanner-village's claim on Tya's body and the Hightower apparatus's first miscategorized intelligence file close around Taylor on the same season-timeline, with neither knowing the other exists and neither closeable from inside. What cannot survive the season is the possibility of working unnamed: by season close, Taylor is already a misread fact in someone else's record before she understands what she is building, and the village's grief-debt remains an open transactional surface she cannot pay off."
    bones_path: active-project/theater/proto-lines/s01.bones.md
    bones_complete: 2026-05-11
    bones_active_count: ~480 (across IDs 1-517 with deletion gaps)
    phase_2_cycles: 3 of 3 max
    phase_3_cycles: 2 of 3 max (per-window URI-026 cap=2 reached)
    provisional_split: 3 episodes (cuts at IDs 155/159 and 328/330; 6-episode SPLIT-INFEASIBLE)
    tens_files:
      - active-project/theater/facets/tensometer-s01-window-01.md
      - active-project/theater/facets/tensometer-s01-window-02.md
      - active-project/theater/facets/tensometer-s01-window-03.md
    audit_reports_dir: active-project/staff/auditor/season-s01-pass-*
    residuals:
      - tens-gate-residual-W1-Scene-L-no-rupture (maester laughs without commit)
      - tens-gate-residual-W2-Scene-A-no-3 (family-visit junction)
      - tens-gate-residual-W2-Scene-H-no-3 (headache cluster no peak)
      - tens-gate-residual-W2-Scene-L-no-3 (mother's vigil-candle close)
      - tens-gate-residual-W3-frequency-band-below-floor (4/152 = 2.6%)
      - tens-gate-residual-W3-scene-330-342-no-3 (first Hightower clerk)
      - tens-gate-residual-W3-scene-361-375-no-3 (second clerk)
      - tens-gate-residual-W3-scene-477-494-no-rupture (denouement walk; no transit exception)
      - pov-leak-71-77 (lord's-man records the file; no insect relay anchor)
      - audience-S3-1-of-3-revise (cape-fic, dark-fantasy, worm-canon: 3-of-3 REVISE on range-expansion template + beat 10)
      - audience-S6-localized-drift-W12 (beat 10 thin/relay-mapping flagged by cape-fic + dark-fantasy)
      - audience-S9-2-of-3-comprehensibility-risk (cape-fic fragile-chains, worm-canon formula-lock)
    convergence: PARTIAL — Sweep A 12 of 18 clean; Sweep B 14 of 17 clean. Convergence per spec ("all-clean reports across both sweeps and no fixes in between") not achieved.
    orchestrator_verdict: "FAIL — F7-bone (7+ tens-gate-residual-HARD open) + F1 (Phase 3 S1/S3/S7/S9 not converged) + R1 (~86 dispatches vs 60 cap)"
    orchestrator_verdict_file: active-project/staff/auditor/season-s01-orchestrator-verdict.md
  - slug: s02
    chunk: "The glass-candle acquisition and sustained high-density relay load accumulate against the broken maester's sharpening documentation across the same months; the Khepri-mantle threshold crosses late in the season, the maester names it and is not heard, and Taylor arrives in s03 already changed — what cannot survive is the pre-threshold Taylor and the maester's belief that naming the line constitutes a brake."
    status: planned
  - slug: s03
    chunk: "The Dance ignites and both factions' years of misclassification deliver their envoys to Taylor's door at the same time the faction-convergence engagement forces her hand; the rider-control demonstration terminates the Dance by rational deterrence and terminates also each faction's capacity to model her as a threat with a knowable ceiling."
    status: planned
  - slug: s04
    chunk: "The density-saturation experiment and the surviving subject share the same Fish Gate margin Taylor's log has always under-recorded; the foreclosure event — one subject dead, one broken into four-hour memory increments, the falsification record burned — detonates after the war ends and takes with it the scientific-caution self-narrative the research arc has rested on since s01."
    status: planned

active:
  season: s01
  episode: ~
