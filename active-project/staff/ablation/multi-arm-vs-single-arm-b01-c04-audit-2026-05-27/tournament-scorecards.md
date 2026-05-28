# Tournament scorecards ledger
# Append-only per URI-STITCH-SCORECARD-BACKREF (2026-05-27).
# Phase 1.5 Step 3 writes the scene-level scorecard rows; Phase 9 Step 4 fills the cold-read fields.
# Cross-chapter signal for rubric tuning per design/tournament-tuning.md.

ledger:
  version: 1
  rows:

    - chapter: b01-c04
      scene: A
      run_id: 2026-05-27T00:00:00Z
      arms_dispatched: 2
      arm_labels: [arm-1=series-Robinson-contemplative, arm-2=alt-auto-procedural-with-pressure]
      tournament_winner: arm-2
      ceiling_collapse: true
      substitutions: 0
      rewards_sum: 10
      peeves_weighted_sum: -21
      scene_score: -11
      tournament_report: active-project/staff/reviews/tournament-b01-c04-scene-A-2026-05-27.md
      cherry_pick_report: active-project/staff/reviews/cherry-pick-b01-c04-scene-A-2026-05-27.md
      scorecard_report: active-project/staff/reviews/scorecard-b01-c04-scene-A-2026-05-27.md
      tuning_notes: "PEEVE-3/4/5 (symbolic / setting-dressing / compound-noun saturation) co-fire on same craft habit — composite peeve candidate."
      cold_read_verdict: PASS
      cold_read_continue: tentative-yes

    - chapter: b01-c04
      scene: B
      run_id: 2026-05-27T00:00:00Z
      arms_dispatched: 2
      arm_labels: [arm-1=series-Robinson-contemplative, arm-2=alt-auto-procedural-with-pressure]
      tournament_winner: arm-2
      ceiling_collapse: true
      substitutions: 0
      rewards_sum: 10
      peeves_weighted_sum: -24
      scene_score: -14
      tournament_report: active-project/staff/reviews/tournament-b01-c04-scene-B-2026-05-27.md
      cherry_pick_report: active-project/staff/reviews/cherry-pick-b01-c04-scene-B-2026-05-27.md
      scorecard_report: active-project/staff/reviews/scorecard-b01-c04-scene-B-2026-05-27.md
      tuning_notes: "8 strong peeves; metronome 'I mapped...' / 'The feed returned...' structurally load-bearing in procedural prime; compound-noun saturation persistent."
      cold_read_verdict: PASS
      cold_read_continue: tentative-yes

    - chapter: b01-c04
      scene: C
      run_id: 2026-05-27T00:00:00Z
      arms_dispatched: 2
      arm_labels: [arm-1=series-Robinson-contemplative, arm-2=alt-auto-procedural-with-pressure]
      tournament_winner: arm-1
      ceiling_collapse: true
      substitutions: 0
      rewards_sum: 4
      peeves_weighted_sum: -31
      scene_score: -27
      walkout_flag: PEEVE-9-protagonist-cost-not-legible
      tournament_report: active-project/staff/reviews/tournament-b01-c04-scene-C-2026-05-27.md
      cherry_pick_report: active-project/staff/reviews/cherry-pick-b01-c04-scene-C-2026-05-27.md
      scorecard_report: active-project/staff/reviews/scorecard-b01-c04-scene-C-2026-05-27.md
      tuning_notes: "WALKOUT-flagged on PEEVE-9 (cost-not-legible); held-trio reads metronomic per scorer; compound-noun saturation high. RUBRIC-VS-REGISTER candidate — Taylor's voice is clinical-accounting by design; tournament rubric may need carve-out for project-register-resident peeves vs novel ones."
      cold_read_verdict: PASS
      cold_read_continue: tentative-yes

# Cross-run signals (3-chapter accumulator threshold per spec):
# - Ceiling-collapse rate: 3/3 scenes on first multi-arm-default run = 100%. Spec: "If ceiling-collapse: true fires on >50% of scenes across multiple chapters, the multi-arm setup isn't differentiating arms enough — feeds back to exemplar-selection at Phase 0 step 4a." First chapter result; not yet enough data to trigger reconsideration. Watch on next 2-3 chapters.
# - Compound-noun saturation fires on all 3 scenes. RUBRIC-VS-REGISTER tension flagged at scene-C. Watch for promotion to rubric carve-out.
