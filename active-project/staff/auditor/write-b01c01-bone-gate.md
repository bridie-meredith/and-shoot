# write-b01c01-bone-gate report
phase: /and-write b01c01 Phase 6 substance bone-gate (auditor) — RE-AUDIT ROUND 2
date: 2026-05-25
auditor: auditor
chapter_class: standard
artifact_audited: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md
prior_report: round 1 (same file, verdict AUDITOR-HARD-PRESENT, 3 HARDs + 3 SIGNALs)
fixer_log_session: SESSION-START 2026-05-25T04:00:00Z — write-b01c01-phase6-bone-gate

summary:
  bones_audited: 27
  moving_bones: 2
  held_bones: 25
  chatter_bones: 0
  hard_findings: 0
  signal_findings: 3
  signal_dispositions_open: 0

# ---------------------------------------------------------------------------
# HARD-FIX VERIFICATION (round 1 fault-001, fault-002, fault-003)
# ---------------------------------------------------------------------------

hard_fix_verification:

  - id: fault-001 (round-1)
    bone: b01c01s02n02
    prior_axes_held: [capability]
    current_axes_held: [moral_framework]
    contracted_for_s02: moral_framework is in s02 axes_held (memory line 1774) — CONTRACTED
    rationale_check: |
      "the prohibition is intact at this bone — the insect-sense reads body-vibration
      through the cobbles as passive baseline perception, not active deployment;
      moral_framework held as not-yet-cracked; the sense-mechanism is doing its baseline
      work, which the prohibition has always permitted; the scene's tension is what
      happens when this baseline is exceeded, which has not happened yet at this bone"
      Rationale enacts prohibition-intact discipline (pre-crack held state). CREDIBLE.
    held_axis_uncontracted: CLEARED
    verdict: RESOLVED

  - id: fault-002 (round-1)
    bone: b01c01s02n04
    prior_axes_held: [moral_framework, capability]
    current_axes_held: [moral_framework]
    contracted_for_s02: moral_framework is in s02 axes_held — CONTRACTED
    rationale_check: |
      "the last beat of prohibition-maintenance before the crack — Taylor's body
      planted, the range pressing, the prohibition still running; this is the
      prohibition's final held moment in the scene; the threshold-crossing at the next
      bone reads as a crossing because this bone holds the line right before it"
      Rationale enacts prohibition's-final-held-moment discipline. CREDIBLE.
      capability entry is absent from axes_held. No residual uncontracted axis.
    held_axis_uncontracted: CLEARED
    verdict: RESOLVED

  - id: fault-003 (round-1)
    bone: b01c01s02n08
    prior_axes_held: [capability]
    current_axes_held: [moral_framework]
    contracted_for_s02: moral_framework is in s02 axes_held — CONTRACTED
    rationale_check: |
      "the crack continues — the deployment's wave-effect persists as the gap
      propagates outward, bodies continuing to yield to insect-pressure; the
      prohibition's violation extends beat-by-beat without being filed as violation;
      moral_framework held as load-bearing dormancy through the deployment's cascade"
      Rationale enacts crack-extending discipline (prohibition violated without being
      filed as violated; reader-visible, not Taylor-legible). CREDIBLE.
    held_axis_uncontracted: CLEARED
    verdict: RESOLVED

# ---------------------------------------------------------------------------
# SIGNAL-REMEDIATION VERIFICATION
# ---------------------------------------------------------------------------

signal_remediation:

  - id: signal-001 (round-1) — propagate-mannerism REMEDIATE
    prior_svo: "the insects propagate" (s01n04)
    current_svo: "the insects swell" (s01n04)
    svo_clean_check: |
      'swell' — intransitive process verb; no modifier; no negation; no perception
      verb; no non-action verb; not a copula; not a conjunction; subject 'the insects'
      is a named environment entity (singular collective); no object required for
      intransitive landing. CLEAN.
    substance_delta_check: |
      s01n04 substance_delta unchanged: axis_moves[], axes_held [capability,
      moral_framework] with rationales intact. capability is in s01 axes_held
      (memory line 1724) — CONTRACTED. moral_framework is in s01 axes_held
      (memory line 1722) — CONTRACTED. Both axes are correctly contracted-held
      for s01. No new finding introduced.
    propagate_count_after_recast: |
      s02n06: "the insects propagate" — 1
      s02n08: "the gap propagates" — 1
      Total: 2 instances chapter-wide. Below ≥3 threshold. Identical-SVO pair
      (s01n04/s02n06) eliminated.
    verdict: SIGNAL CLEARED

  - id: signal-002 (round-1) — faces-verb ACCEPTED-WITH-RATIONALE
    fixer_disposition: ACCEPT-WITH-RATIONALE (session 04:09)
    rationale_recorded: |
      No single VERB+OBJECT pair hits ≥3 threshold (max 'faces taylor' at 2).
      Body-orientation register is load-bearing for ward-categorization beats.
      Synonyms reintroduce banned prepositional forms ('turns to', 'pivots toward')
      or damage posture-vocabulary register.
    re-audit_check: |
      Current faces/face count from draft:
        s02n09 "taylor faces the child" — 1
        s03n02 "the fish-cart man faces taylor" — 1
        s03n03 "the two women face the lane" — 1
        s03n07 "taylor faces the alley-mouth" — 1
        s03n10 "wren-stitch-maker-flea-bottom-ward faces taylor" — 1
      Total: 5 across 4 distinct VERB+OBJECT pairs. No pair ≥3.
      Disposition is on record; rationale is credible; mechanical threshold not
      crossed. DISPOSED.
    verdict: SIGNAL DISPOSED (accept-with-rationale)

  - id: signal-003 (round-1) — s01n07 axes-per-bone ACCEPTED-WITH-RATIONALE
    fixer_disposition: ACCEPT-WITH-RATIONALE (session 04:10)
    rationale_recorded: |
      Third axis (political_register-prot) is a repair-move consequence of s01n05
      drop at Pass 2 round 1. Removing it would require authoring a new s01
      political_register-prot held bone (over-engineering) or losing scene-level
      held-coverage (HELD-AXIS-NOT-WITNESSED fault). /and-facets flagged to
      distribute three axes across separate facet entries.
    re-audit_check: |
      b01c01s01n07 axes_held: [moral_legibility_to_self, moral_framework,
      political_register-prot] — 3 entries. All three are in s01 axes_held per
      memory lines 1722–1733. CONTRACTED. The overage (1 above the 1–2 guideline)
      is a documented repair-move artifact. Disposition is on record.
    verdict: SIGNAL DISPOSED (accept-with-rationale)

# ---------------------------------------------------------------------------
# PER-BONE TABLE (full re-scan)
# ---------------------------------------------------------------------------

per_bone:

  # SCENE 1 — b01c01s01 (6 bones; no in-motion axes; 6 held axes contracted)

  - bone: b01c01s01n01
    shape: held
    held_axes: [social_tether-prot-rise]
    scene_contracted: social_tether-prot-rise in s01 axes_held (memory line 1732) — COVERED
    bonefide_or_enactment: PASS
    detail: "anonymity-enacted-by-position; drain water threads the angle-gap; clean SVO (transitive, no modifier, no banned verb)"

  - bone: b01c01s01n02
    shape: held
    held_axes: [relational_anchor_status]
    scene_contracted: relational_anchor_status in s01 axes_held (memory line 1727) — COVERED
    bonefide_or_enactment: PASS
    detail: "tallow smoke crosses the stitch-house lane; anchor-present-as-environmental-datum; clean SVO"

  - bone: b01c01s01n03
    shape: held
    held_axes: [capability, moral_framework]
    scene_contracted: capability (memory line 1724) and moral_framework (memory line 1722) in s01 axes_held — BOTH COVERED
    bonefide_or_enactment: PASS
    detail: "taylor holds the feet; holds licensed (body part + stillness-against-pressure); both disciplines named with credible rationales"

  - bone: b01c01s01n04
    shape: held
    svo: "the insects swell"
    held_axes: [capability, moral_framework]
    scene_contracted: capability (memory line 1724) and moral_framework (memory line 1722) in s01 axes_held — BOTH COVERED
    bonefide_or_enactment: PASS
    detail: "SVO recast to 'swell' (intransitive process verb, CLEAN); opposing-force enacted; both axes contracted-held in s01; no new fault"

  - bone: b01c01s01n06
    shape: held
    held_axes: [social_tether-prot-rise]
    scene_contracted: social_tether-prot-rise in s01 axes_held (memory line 1732) — COVERED
    bonefide_or_enactment: PASS
    detail: "angle-wall narrows the lane; transitive geometry-action; physical-geometry-of-anonymity rationale; clean"

  - bone: b01c01s01n07
    shape: held
    held_axes: [moral_legibility_to_self, moral_framework, political_register-prot]
    scene_contracted: all three in s01 axes_held (memory lines 1729, 1722, 1730) — COVERED
    bonefide_or_enactment: PASS
    detail: "taylor exhales; 3-axis overage disposed (signal-003 accept-with-rationale); all three axes contracted for s01; all three rationales name the held discipline credibly"

  # SCENE 2 — b01c01s02 (11 bones; capability in axes_in_motion; 5 held axes contracted; stakes_axis: moral_framework)

  - bone: b01c01s02n01
    shape: held
    held_axes: [social_tether-prot-rise]
    scene_contracted: social_tether-prot-rise in s02 axes_held (memory line 1782) — COVERED
    bonefide_or_enactment: PASS
    detail: "fish-cart blocks the lane; transitive, no modifier; ward-indifference-enacted; clean"

  - bone: b01c01s02n02
    shape: held
    held_axes: [moral_framework]
    scene_contracted: moral_framework in s02 axes_held (memory line 1774) — COVERED
    bonefide_or_enactment: PASS
    detail: "ground transmits the child's breath; capability ABSENT from axes_held; moral_framework rationale enacts prohibition-intact (baseline-perception-not-deployment discipline); HARD CLEARED"

  - bone: b01c01s02n03
    shape: held
    held_axes: [moral_framework]
    scene_contracted: moral_framework in s02 axes_held — COVERED
    bonefide_or_enactment: PASS
    detail: "crowd compresses; opposing-force enacted; crowd-compression named as pressure the prohibition runs against; clean"

  - bone: b01c01s02n04
    shape: held
    held_axes: [moral_framework]
    scene_contracted: moral_framework in s02 axes_held — COVERED
    bonefide_or_enactment: PASS
    detail: "taylor holds the feet; capability ABSENT from axes_held; single moral_framework entry enacts prohibition's-final-held-moment; holds licensed (body part + stillness-against-pressure); HARD CLEARED"

  - bone: b01c01s02n05
    shape: held
    held_axes: [political_register-prot]
    scene_contracted: political_register-prot in s02 axes_held (memory line 1780) — COVERED
    bonefide_or_enactment: PASS
    detail: "lane-mouth presses the crowd; transitive, no modifier; smallfolk-only dormancy rationale; clean"

  - bone: b01c01s02n06
    shape: moving
    axis_moves: [capability +1]
    cost_ledger_anchor: cl01a
    scene_contracted: capability in s02 axes_in_motion (memory line 1768); cl01a gain correctly anchored
    bonefide_or_enactment: PASS
    detail: "insects propagate; bare intransitive; capability+1 delivered; single moving bone for this axis; cl01a gain side anchored; bonefide clean"

  - bone: b01c01s02n07
    shape: held
    held_axes: [moral_framework]
    scene_contracted: moral_framework in s02 axes_held — COVERED
    bonefide_or_enactment: PASS
    detail: "nearest dozen bodies yield; crack-visible-to-reader enacted; prohibition-crossed-without-being-filed rationale; clean"

  - bone: b01c01s02n08
    shape: held
    held_axes: [moral_framework]
    scene_contracted: moral_framework in s02 axes_held — COVERED
    bonefide_or_enactment: PASS
    detail: "gap propagates; capability ABSENT from axes_held; moral_framework rationale enacts crack-extending discipline; HARD CLEARED"

  - bone: b01c01s02n09
    shape: held
    held_axes: [relational_anchor_status]
    scene_contracted: relational_anchor_status in s02 axes_held (memory line 1776) — COVERED
    bonefide_or_enactment: PASS
    detail: "taylor faces the child; anchor-present-but-unregistered; dormancy rationale names cost-bearer in frame; faces licensed as discrete posture-act; clean"

  - bone: b01c01s02n11
    shape: held
    held_axes: [moral_legibility_to_self]
    scene_contracted: moral_legibility_to_self in s02 axes_held (memory line 1778) — COVERED
    bonefide_or_enactment: PASS
    detail: "taylor raises the voice; accounting-not-yet-opened rationale; raises transitive and not on deny list; the voice is physical sound-production output; clean"

  - bone: b01c01s02n10
    shape: held
    held_axes: [social_tether-prot-rise]
    scene_contracted: social_tether-prot-rise in s02 axes_held (memory line 1782) — COVERED
    bonefide_or_enactment: PASS
    detail: "taylor lifts the hands; witness-facing-gesture enacted; tether-does-not-move rationale explicit; lifts is discrete transitive act; clean"

  # SCENE 3 — b01c01s03 (10 bones; social_tether-prot-rise in axes_in_motion; 5 held axes contracted; stakes_axis: social_tether-prot-rise)

  - bone: b01c01s03n01
    shape: held
    held_axes: [political_register-prot]
    scene_contracted: political_register-prot in s03 axes_held (memory line 1829) — COVERED
    bonefide_or_enactment: PASS
    detail: "crowd thins; intransitive physical process; smallfolk-only-dispersal dormancy rationale; clean"

  - bone: b01c01s03n02
    shape: held
    held_axes: [social_tether-prot-rise]
    scene_contracted: social_tether-prot-rise is s03 stakes_axis (stakes_axis exemption applies) — COVERED
    bonefide_or_enactment: PASS
    detail: "fish-cart man faces taylor; faces licensed as transitive posture-act; held-before-the-move rationale consistent with stakes_axis framing; clean"

  - bone: b01c01s03n03
    shape: held
    held_axes: [social_tether-prot-rise]
    scene_contracted: social_tether-prot-rise is s03 stakes_axis (stakes_axis exemption applies) — COVERED
    bonefide_or_enactment: PASS
    detail: "two women face the lane; faces licensed; holders-remain as critical-mass condition; clean"

  - bone: b01c01s03n04
    shape: moving
    axis_moves: [social_tether-prot-rise +1]
    cost_ledger_anchor: cl01b
    scene_contracted: social_tether-prot-rise in s03 axes_in_motion (memory line 1817); cl01b partial-settlement correctly anchored (ward-layer half; remaining +1 deferred to b01c03 per pl-2026-05-25-001)
    bonefide_or_enactment: PASS
    detail: "oswyn-mudway-flea-bottom-elder takes the lane-mouth; transitive discrete act; bonefide clean; cl01b partial-anchor explicit in memory notes"

  - bone: b01c01s03n05
    shape: held
    held_axes: [capability]
    scene_contracted: capability in s03 axes_held (memory line 1831) — COVERED
    bonefide_or_enactment: PASS
    detail: "child clears the lane; transitive; capability-held-at-new-floor rationale confirms aftermath without extension; clean"

  - bone: b01c01s03n06
    shape: held
    held_axes: [moral_framework]
    scene_contracted: moral_framework in s03 axes_held (memory line 1823) — COVERED
    bonefide_or_enactment: PASS
    detail: "gap closes; bare intransitive; crack-visible-only-in-retrospect rationale; clean"

  - bone: b01c01s03n07
    shape: held
    held_axes: [relational_anchor_status, moral_legibility_to_self]
    scene_contracted: relational_anchor_status (memory line 1825) and moral_legibility_to_self (memory line 1827) in s03 axes_held — BOTH COVERED
    bonefide_or_enactment: PASS
    detail: "taylor faces the alley-mouth; faces licensed; facing-as-direction-toward (not negation) for relational_anchor_status; accounting-deferred-in-the-same-gesture for moral_legibility_to_self; both disciplines named; clean"

  - bone: b01c01s03n08
    shape: held
    held_axes: [relational_anchor_status]
    scene_contracted: relational_anchor_status in s03 axes_held — COVERED
    bonefide_or_enactment: PASS
    detail: "tallow smoke layers the lane-floor; transitive; stitch-house continuity enacted as sensory fact; anchor-dormancy rationale; pl-002 SOFT load-bearing continuity maintained; clean"

  - bone: b01c01s03n09
    shape: held
    held_axes: [social_tether-prot-rise]
    scene_contracted: social_tether-prot-rise is s03 stakes_axis (stakes_axis exemption applies) — COVERED
    bonefide_or_enactment: PASS
    detail: "oswyn-mudway-flea-bottom-elder lifts the chin; lifts is discrete transitive act; categorization-completing rationale; stakes_axis exemption applies; clean"

  - bone: b01c01s03n10
    shape: held
    held_axes: [relational_anchor_status]
    scene_contracted: relational_anchor_status in s03 axes_held — COVERED
    bonefide_or_enactment: PASS
    detail: "wren-stitch-maker-flea-bottom-ward faces taylor; faces licensed; structural dormancy of un-priced anchor enacted (reader identifies Wren via slug; Taylor reads a body, not Wren); handoff_out honored; clean"

# ---------------------------------------------------------------------------
# PER-SCENE
# ---------------------------------------------------------------------------

per_scene:
  s01:
    event_presence: PASS
    axis_delta: "target=0/0, observed=0/0 — CLEAN"
    stakes_axis_dominant: "N/A — no in-motion axes"
    sensory_grounding: "PASS — n01 (drain water threads the angle-gap) and n02 (tallow smoke crosses the stitch-house lane); ≥1 met"
    held_axes_coverage: |
      PASS — all 6 contracted axes covered:
        moral_framework: n03, n04, n07
        capability: n03, n04
        relational_anchor_status: n02
        moral_legibility_to_self: n07
        political_register-prot: n07
        social_tether-prot-rise: n01, n06
    stakes_axis_in_union: "PASS — moral_framework in axes_held"
    opposing_force_visible: "PASS — n04 (insects swell) enacts insect-pull at range threshold; n07 (taylor exhales) enacts three weeks of accumulated suppression work"
    cost_ledger_paid: "N/A — no ledger anchor at s01"

  s02:
    event_presence: PASS
    axis_delta: "target=capability+1.0, observed=capability+1 (n06, magnitude:1) — EXACT MATCH"
    stakes_axis_dominant: "N/A — stakes_axis moral_framework is in axes_held, not axes_in_motion"
    sensory_grounding: "PASS — n01 (fish-cart blocks the lane) and n02 (ground transmits the child's breath); ≥1 met"
    held_axes_coverage: |
      PASS — all 5 contracted held axes covered; no capability entries in axes_held
      on any bone (HARDs cleared):
        moral_framework: n02, n03, n04, n07, n08
        relational_anchor_status: n09
        moral_legibility_to_self: n11
        political_register-prot: n05
        social_tether-prot-rise: n01, n10
    stakes_axis_in_union: "PASS — moral_framework in axes_held"
    opposing_force_visible: "PASS — n03 (crowd compresses) and n04 (taylor holds the feet) enact crowd-compression + prohibition-pressure"
    cost_ledger_paid: "PASS — cl01a gain (capability+1) anchored at n06; cost (witch-label formation, opportunity-missed) confirmed by s03 social-process bones"

  s03:
    event_presence: PASS
    axis_delta: "target=social_tether-prot-rise+1.0, observed=social_tether-prot-rise+1 (n04, magnitude:1) — EXACT MATCH"
    stakes_axis_dominant: "PASS — social_tether-prot-rise is the only in-motion axis; trivially dominant"
    sensory_grounding: "PASS — n08 (tallow smoke layers the lane-floor) is primary; n01 (crowd thins) borderline-transition; n08 alone satisfies ≥1"
    held_axes_coverage: |
      PASS — all 5 contracted held axes covered:
        moral_framework: n06
        relational_anchor_status: n07, n08, n10
        moral_legibility_to_self: n07
        political_register-prot: n01
        capability: n05
      n02, n03, n09 hold social_tether-prot-rise (in-motion axis); stakes_axis
      exemption applies.
    stakes_axis_in_union: "PASS — social_tether-prot-rise in axes_in_motion"
    opposing_force_visible: "PASS — n04 (oswyn takes the lane-mouth) and n09 (oswyn lifts the chin) enact Oswyn's watching as opposing force; witch-label assembly bones n04/n09 cover the event_map opposing_force entry"
    cost_ledger_paid: "PASS — cl01b ward-layer half (social_tether-prot-rise+1 of +2) anchored at n04; remaining +1 deferred to b01c03 per pl-2026-05-25-001"

# ---------------------------------------------------------------------------
# PER-CHAPTER
# ---------------------------------------------------------------------------

per_chapter:
  register_mannerism:
    propagate_null_count: 2
    propagate_breakdown: |
      s02n06: "the insects propagate"
      s02n08: "the gap propagates"
      (s01n04 recast to "the insects swell" — no longer in propagate count)
    propagate_verdict: "BELOW threshold (2 < 3); identical-SVO pair eliminated; SIGNAL CLEARED"

    faces_count: 5
    faces_breakdown: |
      s02n09: "taylor faces the child" — 1
      s03n02: "the fish-cart man faces taylor" — 1
      s03n03: "the two women face the lane" — 1
      s03n07: "taylor faces the alley-mouth" — 1
      s03n10: "wren-stitch-maker-flea-bottom-ward faces taylor" — 1
    faces_verdict: "BELOW per-pair threshold (max 'faces taylor' at 2 < 3); SIGNAL DISPOSED (accept-with-rationale)"

    lifts_the_count: 2
    lifts_the_breakdown: |
      s02n10: "taylor lifts the hands"
      s03n09: "oswyn-mudway-flea-bottom-elder lifts the chin"
    lifts_verdict: "BELOW threshold (2 < 3); no fire"

    holds_the_feet_count: 2
    holds_the_feet_breakdown: |
      s01n03: "taylor holds the feet"
      s02n04: "taylor holds the feet"
    holds_verdict: "BELOW threshold (2 < 3); no fire"

    swell_count: 1
    swell_note: "introduced by recast of s01n04; unique to that bone; no new mannerism pair"

    new_mannerism_risk: NONE
    signals_raised_this_round: []

  axes_per_bone_watch:
    s01n07_axes_held_count: 3
    s01n07_verdict: "overage disposed (signal-003 accept-with-rationale); no new finding"

  chatter_bones: 0
  moving_bone_sum_check: |
    s02: capability +1 (n06) — target 1.0 ✓
    s03: social_tether-prot-rise +1 (n04) — target 1.0 ✓
    Chapter moving-bone total: 2. Arithmetic clean.

# ---------------------------------------------------------------------------
# VERDICT
# ---------------------------------------------------------------------------

verdict: AUDITOR-PASS

hard_count: 0
signal_count: 3
signals_open: 0
signals_disposed: 3

disposition_log:
  signal-001: REMEDIATED (s01n04 svo recast "insects propagate" → "insects swell"; propagate ∅ count drops to 2; threshold cleared)
  signal-002: ACCEPTED-WITH-RATIONALE (faces/face 5×, no pair ≥3; posture-register load-bearing; synonyms reintroduce banned forms)
  signal-003: ACCEPTED-WITH-RATIONALE (s01n07 3 axes_held = repair-move consequence of s01n05 drop; /and-facets to distribute)

hard_summary: |
  All 3 round-1 HARDs are cleared. The root cause (capability held in s02 while
  capability is in s02 axes_in_motion) has been removed from all three bones:
  s02n02, s02n04, and s02n08 now hold only moral_framework, which is contracted as
  held for s02 (memory line 1774). Each rationale credibly enacts a moral_framework
  held discipline (prohibition-intact / prohibition's-final-held-moment /
  crack-extending). HELD-AXIS-UNCONTRACTED is cleared chapter-wide.

signal_summary: |
  signal-001 REMEDIATED: propagate mannerism eliminated by s01n04 recast. Post-fix
  propagate count is 2 (s02n06, s02n08) — below the ≥3 fire condition.
  signal-002 DISPOSED (accept-with-rationale): faces/face at 5 instances, 4 distinct
  pairs, max 2 per pair. Disposition rationale on record in fixer log.
  signal-003 DISPOSED (accept-with-rationale): s01n07 triple-axis overage is a
  documented repair-move artifact. /and-facets flag recorded.
  No new signals introduced by the recast of s01n04 (swell is unique; no new pair).

new_findings: NONE

note: |
  This auditor's gate is now clear. The chapter proceeds to /and-facets when the
  audience trio returns 3-of-3 SUBSTANCE-FELT for all three scenes. Auditor's half
  of the bone-gate: PASS. Constraints (cond-override-architecture-residue-122ac,
  cond-kl-witch-label-formation-122ac, cond-cost-bearer-scene-frequency,
  cond-taylor-pov-behavior) re-checked: no violations at bone level in the post-fix
  draft. Parking-lot items: pl-2026-05-25-001 HARD (b01c03 target, not this
  invocation — no block); pl-2026-05-25-002 SOFT (resolved at Phase 1); pl-2026-05-25-003
  SOFT (noted; no moral_framework collapse in this chapter, consistent with
  concentration rule).
