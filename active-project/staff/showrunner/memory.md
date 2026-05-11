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
    bones_active_count: 456 active-bone lines (with SVO content) across season-global IDs 1-528 with deletion gaps; ~48 numbered blank time-skip lines (504 total numbered lines including blanks). Corrected 2026-05-11 — prior count "~480 (across IDs 1-517 with deletion gaps)" was pre-cycle-3 and missed F7-bone-rescue additions 518-528.
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
    orchestrator_verdict: "PASS-WITH-NOTES — F7-bone CLEARED by cycle-3 cleanup (IDs 518-528); high-dispatch (~95 vs 60-hard); long-run (~12h); deep-iteration on S10/S7/boundary; rubric-recalibration-recommended; frequency-band W2/W3 below floor (structural); audience-S3 not re-fired (carry-forward to edit pass)"
    orchestrator_verdict_file: active-project/staff/auditor/season-s01-orchestrator-verdict.md
    protolines_complete: 2026-05-11
    episodes:
      - slug: s01e01
        status: audited-r1   # FLIPPED 2026-05-11 per /and-facets resume r5 — flag-005 closed as EXEMPT-TONE-LAW-SLOW-BURN once card amendment landed; 0 HARD across r3/r4/r5 audit passes; only carry-forward editor-call SIGNALs (NI density 25.2%, non-POV feeling sparsity) remain by design
        narrator: taylor-hebert-flea-bottom
        interlude: false
        chunk: "Taylor wakes in Tya's body and the tanner-village category closes around her on the first morning; she moves to King's Landing via the tanner-elder, maps her 300m sphere in Flea Bottom, identifies the broken maester's upper room as ambient surveillance, and runs her first transactional exchange via the dock-runner."
        proto_lines_path: active-project/theater/proto-lines/s01e01.md
        tens_path: active-project/theater/facets/tensometer-s01e01.md
        cast: [taylor-hebert-flea-bottom, oc-tanner-father, oc-tanner-mother, oc-tanner-elder, oc-broken-maester, oc-dock-runner]
        locations: [loc-flea-bottom, loc-flea-bottom-base]
        prior_episode: none
        aggregate_range: 1-155 (+ interpolated narrative-scope: 495, 504, 506, 516, 517, 518, 525)
        aggregate_range_revised_at: 2026-05-11   # URI-028 honest-form declaration; body not yet re-rendered against full roster
        per_episode_tens_band_verdict: {1s: 80.1, 2s: 14.9, 3s: 5.0, status: "exempt-tone-law-slow-burn (URI-034 Exemption 5)", rationale: "all three rungs within relaxed band per cond-series-tone-constraints-125ac §Relaxed tens frequency-band; flag-005 closeable"}
        facets_path: active-project/theater/facets/
        round_1_complete: true
        round_2_complete: true
        audit_path: active-project/staff/auditor/facets-final-audit-r5.md   # canonical latest; r3/r4/r5 are sequential SIGNAL-closure audits in this session
        audit_complete: true
        audit_findings: 14   # initial r1: 4 HARD + 1 HARD-proximity + 9 SIGNAL; 5 pile-ups all warranted
        audit_findings_hard_initial: 4
        reaudit_path: active-project/theater/s01e01-archive/auditor/facets-final-audit-r2.md
        reaudit_complete: true
        audit_paths_chronological:
          - active-project/theater/s01e01-archive/auditor/facets-final-audit-r1.md  # r1 (initial; 4 HARD; archived 2026-05-11 during s01e02 run)
          - active-project/theater/s01e01-archive/auditor/facets-final-audit-r2.md  # r2 (post-fixer-1; 1 HARD residual = flag-005; archived 2026-05-11)
          - active-project/staff/auditor/facets-final-audit-r3.md    # r3 (post-URI-034-tens-exemption; 0 HARD, 7 SIGNAL — flag-005 downgraded pending card amendment)
          - active-project/staff/auditor/facets-final-audit-r4.md    # r4 (post-fixer-2 + card amendment; 0 HARD, 4 SIGNAL — flag-005 EXEMPT; 2 new SIGNALs)
          - active-project/staff/auditor/facets-final-audit-r5.md    # r5 (post-fixer-3; 0 HARD, 2 SIGNAL — both editor-call deferrals by design); CANONICAL FINAL
        remediation_passes_hard: 1 of 1 (r1 -> r2; criterion-2 budget; cleared 4 HARD)
        remediation_passes_signal: 2 (r3 -> r4 fixer, r4 -> r5 manual; SIGNAL-only closure cycles)
        audit_findings_hard_residual: 0   # flag-005 confirmed EXEMPT-TONE-LAW-SLOW-BURN in r4/r5 against the now-amended cond-series-tone-constraints-125ac card
        audit_findings_signal_residual: 2 # NI density 25.2% (editor-call); non-POV feeling sparsity (editor-call) — both designed deferrals, not faults
        r2_decisions_path: active-project/theater/facets/.r2-decisions.md
        r2_f_r2_counts: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0}
        r2_discipline_fails: 0
        process_gaps:
          - cite-index parser bug (rpartition strips only last trailing bracket; patched in active-project/staff/cite-index/build_cite_index.py) — see URI-029
          - R2 inflight-r2/ protocol misunderstanding (judges did not carry forward R1 citations; canonical proto-lines rebuilt from facet files directly as Phase 4 fallback) — see URI-030
          - /and-season Phase 7 Step 4 leaked season-window bones into per-episode tens (4 of 5 initial HARD findings traced here) — see URI-028 [ADDRESSED 2026-05-11]
          - frequency-band rubric lacks exemption taxonomy (flag-005 residual HARD cannot be cleanly closed) — see URI-034 [ADDRESSED 2026-05-11; card sync landed in r4 cycle]
          - memory rubric admitted Earth-Bet proper nouns as margit-referral slug components — see URI-032 [ADDRESSED 2026-05-11; mem:6 + mem:9 fence violations cleaned in r3/r4 fixer cycles]
          - /and-facets bidirectional-loop criterion structurally not-validatable in current shape — see URI-035 [ADDRESSED 2026-05-11 BY DESIGN: Phase 5b audience adversarial gate wired into .claude/commands/and-facets.md as the final blocking gate (3 cycles max, fixer-routed remediation); orchestrator-critic criterion 4 replaced (bidirectional-loop → audience-gate ACCEPT 3-of-3 per facet). NOT VALIDATED on s01e01 per user direction (implement-only; s01e01 retains SHIPPABLE-WITH-CAVEATS verdict). First validation will be s01e02 /and-facets run.]
          - build_cite_index consolidate_slices stripped frontmatter on output, producing multi-block YAML in consolidated state-updates.md and feeling.md — see URI-040 [ADDRESSED 2026-05-11 in this session: tool patched to emit single top-of-file frontmatter; slices converted to plain-comment headers across state-updates + feeling]
          - per-character slice files defaulted to YAML frontmatter that the consolidator would stack — see URI-041 [ADDRESSED 2026-05-11: convention now plain-comment slice headers; consolidator owns the canonical frontmatter]
          - URI-034 rubric amendment landed without sync to the tone-law card body — see URI-042 [ADDRESSED 2026-05-11 in r4 cycle: cond-series-tone-constraints-125ac amended additively with Tensometer register characterization paragraph + Relaxed tens frequency-band section; auditor confirmed criteria (a)/(b) on r4 read]
        upstream_tuning_queue_entries: [URI-028, URI-029, URI-030, URI-031, URI-032, URI-033, URI-034, URI-035, URI-036, URI-037, URI-038, URI-039, URI-040, URI-041, URI-042]
        upstream_tuning_queue_addressed: [URI-028, URI-029, URI-032, URI-034, URI-035, URI-036, URI-037, URI-038, URI-039, URI-040, URI-041, URI-042]   # 2026-05-11 fourth round: Phase 5b audience-gate wired into /and-facets, closing URI-035 by design (validation deferred to s01e02). URI-030/031/033 (R2 protocol + tooling) remain open.
      - slug: s01e02
        status: faceted-r2
        narrator: taylor-hebert-flea-bottom
        interlude: false
        chunk: "The tanner-family's claim escalates from informal grief to formalized customary wage-claim across three visits; the broken maester transitions from ambient signal to named log entry; range expands from 300m to 400m with first physiological cost; the mother extinguishes the vigil candle."
        proto_lines_path: active-project/theater/proto-lines/s01e02.md
        tens_path: active-project/theater/facets/tensometer-s01e02.md
        cast: [taylor-hebert-flea-bottom, oc-tanner-father, oc-tanner-mother, oc-tanner-elder, oc-broken-maester, oc-dock-runner]
        locations: [loc-flea-bottom-base]
        prior_episode: s01e01
        aggregate_range: 159-328 (+ interpolated narrative-scope: 496, 500, 501, 502, 505, 508, 509, 510, 511, 512, 519, 520, 521, 526, 527, 528)
        aggregate_range_revised_at: 2026-05-11   # URI-028 honest-form declaration
        per_episode_tens_band_verdict: {1s: 81.5, 2s: 14.3, 3s: 4.2, status: "exempt-tone-law-slow-burn (URI-034 Exemption 5)"}
      - slug: s01e03
        status: protolined
        narrator: taylor-hebert-flea-bottom
        interlude: false
        chunk: "The Hightower apparatus opens its file on Taylor across two clerks and a senior operative's written request through the elder; the village-claim closes around her externally via the lord's-man record; range reaches 600m with the Red Keep 400m beyond ceiling; the season closes on two log entries written side-by-side — the architecture has changed but she does not know what file she is in."
        proto_lines_path: active-project/theater/proto-lines/s01e03.md
        tens_path: active-project/theater/facets/tensometer-s01e03.md
        cast: [taylor-hebert-flea-bottom, oc-tanner-father, oc-tanner-elder, oc-broken-maester]
        locations: [loc-flea-bottom-base]
        prior_episode: s01e02
        aggregate_range: 330-494 (+ interpolated narrative-scope: 497, 498, 499, 503, 507, 513, 514, 522, 523, 524)
        aggregate_range_revised_at: 2026-05-11   # URI-028 honest-form declaration
        per_episode_tens_band_verdict: {1s: 65.2, 2s: 30.3, 3s: 4.5, status: "exempt-tone-law-slow-burn-on-3s-only (URI-034 Exemption 5; 1s/2s within standard band)"}
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
  episode: s01e02
