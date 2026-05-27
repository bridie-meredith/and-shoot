---
report: audit
scope: chapter
target: b01c04
trigger: /and-write Phase 6 bone-gate (auditor leg) — REDO 2026-05-27 (33-bone post-trim set)
timestamp: 2026-05-27
---

# Audit — /and-write b01c04 Phase 6 Bone-Gate (Auditor Leg)

## Summary

verdict: FAIL
hard_count: 5
signal_count: 6
flag_count: 1

per_class_counts:
  HELD-AXIS-NOT-WITNESSED: 5 HARD (s01 capability; s02 political_register-prot; s03 moral_framework, political_register-prot, position-prot-rise)
  CHATTER-OVER-CAP: 2 SIGNAL (s01: 5 vs cap 4; s03: 6 vs cap 4)
  REGISTER-AS-MANNERISM: 4 SIGNAL (maps-[noun] ×3; [insect-feed]-returns-[entity] ×4; exits-[location] ×4; enters-[location] ×5)
  STAKES-AXIS-TIED: 1 FLAG (all 3 scenes; structural tie at +1.0 per magnitude-floor rules)

All SIGNALs dispositioned: 5 accepted, 1 remediated.
All HARD findings require fixer action before /and-review bones.

---

## Per-Bone Verification: Pass

All 33 bones reviewed. Findings below address only deviations.

**Moving bones (7 total):**
- s01n06 social_tether-antag +1.0: bonefide (Taylor's spoken acceptance is the lever-solidification act); cost cl-antag-d03 paid. PASS.
- s01n08 position-prot-rise +1.0: bonefide (Jarvis's routing-confirmation speech names Taylor as formal conduit — rank claim has visible cause in the speech act); cost cl02 paid. PASS.
- s02n03 capability +1.0: bonefide ("extends the insect-range" is the physical act of coverage expansion); cost cl03a paid. PASS.
- s02n06 social_tether-prot-rise +1.0: bonefide (feed returning Oswyn as a named, identifiable entity is the act that creates the unknowing-node relationship); cost cl03b paid (cl03b cost=journey-required cl03a; cl03a paid at n03). PASS.
- s03n03 capability +1.0: bonefide (same extension verb, third ward — covers four-ward completion); cost cl03a paid. PASS.
- s03n07 social_tether-prot-rise +1.0: bonefide (physical delivery of the report sheet is the act that confirms Jarvis as a functional structural vector); cost cl03b paid. PASS.
- s03n09 position-world +1.0: bonefide (Jarvis's physical departure with the report IS the moment the intelligence exits Taylor's operational context and enters Otto's channel — departure is the position-world event); cost cl-world-d04 paid (cost=journey-required cl03a; cl03a settled at s02n03 and s03n03). PASS.

**Held bones (12 total):** All 12 held bones pass discipline-enactment, load-bearing, and schema-license checks. The five HELD-AXIS-NOT-WITNESSED faults below are scene-level failures (missing bones), not individual held-bone failures.

**Chatter bones (14 total):** All 14 chatter bones have cost_ledger_anchors resolving to active scene ledger entries. PAID. Density caps: s01 SIGNAL (signal-001); s02 PASS; s03 SIGNAL (signal-002).

**Dialogue-anchor bones (2 total):**
- s01n06 (taylor-hebert-kl-122ac speaks to jarvis-coin-kl-courier): dialogue file entry 1 @6 present. PASS.
- s01n08 (jarvis-coin-kl-courier speaks to taylor-hebert-kl-122ac): dialogue file entries 8 @8 and 9 @8 present. PASS.

---

## Per-Scene Verification

### b01c04s01

1. Event-presence: All 10 event_map entries covered by bones in post-trim set. PASS.
2. Chunk-tag completeness: All [event:]/[image:]/[force:]/[mechanism:] tags from scene chunk have event_map entries. PASS.
3. Per-axis Δ: social_tether-antag n06 +1.0 vs target +1.0 — EXACT. position-prot-rise n08 +1.0 vs target +1.0 — EXACT. PASS.
4. Stakes-axis dominance: social_tether-antag +1.0 tied with position-prot-rise +1.0. TASTE-FLAG (flag-001).
5. Underdelivery-rationale: both axes at 100% of target. N/A.
6. Sensory-grounding: n01 (tallow-damp marks the cooper's-yard shed-wall). PASS.
7. Held axes bone-level enactment:
   - moral_framework: n07 axes_held [moral_framework]. PASS.
   - relational_anchor_status: n10 axes_held [relational_anchor_status]. PASS.
   - political_register-prot: n05 axes_held [political_register-prot]. PASS.
   - capability: NO BONE with axes_held [capability] in s01. FAULT — fault-001.
8. Stakes-axis in union: social_tether-antag in axes_in_motion. PASS.
9. Opposing force visible: n08 (Jarvis's routing-confirmation — lever solidifies on his speech, not hers) + n09 (departure enacts irreversibility). PASS.
10. Cost-ledger entries paid: cl-antag-d03 at n06 (social_tether-antag rising). cl02 at n08 (position-prot-rise rising). PAID.

### b01c04s02

1. Event-presence: All 13 event_map entries covered by bones in post-trim set. PASS.
2. Chunk-tag completeness: All tags from scene chunk have event_map entries. PASS.
3. Per-axis Δ: capability n03 +1.0 vs target +1.0 — EXACT. social_tether-prot-rise n06 +1.0 vs target +1.0 — EXACT. PASS.
4. Stakes-axis dominance: social_tether-prot-rise +1.0 tied with capability +1.0. TASTE-FLAG (flag-001, same disposition).
5. Underdelivery-rationale: both axes at 100% of target. N/A.
6. Sensory-grounding: n01 (waste-middens junction draws discard-air); n05 (penny-a-barrel carter parks middens cart); n08 (stitch-house frames mark second ward). PASS (3 grounding bones).
7. Held axes bone-level enactment:
   - moral_legibility_to_self: n04 axes_held [moral_legibility_to_self]; n11 axes_held [moral_legibility_to_self]. PASS.
   - moral_framework: n07 axes_held [moral_framework]. PASS.
   - relational_anchor_status: n09 axes_held [relational_anchor_status]; n10 axes_held [relational_anchor_status]. PASS.
   - political_register-prot: NO BONE with axes_held [political_register-prot] in s02. FAULT — fault-002.
8. Stakes-axis in union: social_tether-prot-rise in axes_in_motion. PASS.
9. Opposing force visible: n06 (Oswyn returned by feed — same walk-and-read now constitutes patron-routing) + n07 (maps Oswyn interval without naming it intelligence-routing). PASS.
10. Cost-ledger entries paid: cl03a at n03 (capability rising). cl03b at n06 (social_tether-prot-rise rising). PAID.

### b01c04s03

1. Event-presence: All 15 event_map entries covered by bones in post-trim set. PASS.
2. Chunk-tag completeness: All tags from scene chunk have event_map entries. PASS.
3. Per-axis Δ: capability n03 +1.0 vs target +1.0 — EXACT. social_tether-prot-rise n07 +1.0 vs target +1.0 — EXACT. position-world n09 +1.0 vs target +1.0 — EXACT. position-prot-rise +0 vs s03 target 0 (consolidated to s01) — EXACT. PASS.
4. Stakes-axis dominance: social_tether-prot-rise +1.0 tied with capability +1.0 and position-world +1.0 (three-way tie). TASTE-FLAG (flag-001, same disposition).
5. Underdelivery-rationale: all axes at 100% of target. N/A.
6. Sensory-grounding: n01 (early-morning grey empties Roper's Court); n05 (Jarvis enters the cooper's yard — yard returns as fixed coordinate). PASS (minimum 1 met; n04 also designated as grounding bone by redo but auditor notes "runs the four-ward feed" is an operational action, not a place-situated sensory particular — n01 and n05 independently satisfy the ≥1 quota regardless).
7. Held axes bone-level enactment:
   - moral_legibility_to_self: n10 axes_held [moral_legibility_to_self]; n12 axes_held [moral_legibility_to_self]. PASS.
   - relational_anchor_status: n11 axes_held [relational_anchor_status]. PASS.
   - moral_framework: NO BONE with axes_held [moral_framework] in s03. FAULT — fault-003.
   - political_register-prot: NO BONE with axes_held [political_register-prot] in s03. FAULT — fault-004.
   - position-prot-rise: NO BONE with axes_held [position-prot-rise] in s03. FAULT — fault-005.
8. Stakes-axis in union: social_tether-prot-rise in axes_in_motion. PASS.
9. Opposing force visible: n09 (Jarvis exits with the report — intelligence now in motion toward Otto, no longer in Taylor's context) + n10 (Taylor runs ward-feed — continuous operation enacts its own indivisibility). PASS.
10. Cost-ledger entries paid: cl03a at n03 (capability rising). cl03b at n07 (social_tether-prot-rise rising). cl-world-d04 at n09 (position-world rising; cost journey-required cl03a, settled at s02n03 and s03n03). PAID.

---

## Per-Chapter Verification

**Chapter-level axis aggregate vs target:**
- capability: s02n03 +1.0, s03n03 +1.0 = +2.0 vs target +2.0 — EXACT. PASS.
- position-prot-rise: s01n08 +1.0 = +1.0 vs target +1.0 — EXACT. PASS.
- social_tether-prot-rise: s02n06 +1.0, s03n07 +1.0 = +2.0 vs target +2.0 — EXACT. PASS.
- social_tether-antag: s01n06 +1.0 = +1.0 vs target +1.0 — EXACT. PASS.
- position-world: s03n09 +1.0 = +1.0 vs target +1.0 — EXACT. PASS.
All 5 in-motion axes EXACT vs revised chapter-level contract.

**Bone count:** 33 total (s01: 10; s02: 11; s03: 12). Within chapter chunk_targets.bone_count 15-75. PASS.

**Magnitude floor:** All 7 moving bones at magnitude 1.0. PASS.

**Speech-bone communication-class:** s01n06 social_tether-antag (tether/trust class). s01n08 position-prot-rise (position/reputation class). PASS.

**SVO discipline fence:** PP-stripping, copula, negation, conjunction, perception-verb, non-action-verb deny-list checks: all PASS per redo's own summary (auditor spot-checks confirmed no violations in reviewed bones).

**Earth-Bet proper-noun fence (bones):** No Earth-Bet nouns in any bone SVO. PASS.

**Theme-silence (no verbatim "protection and the trap"):** No bone SVO contains the thesis phrase. PASS.

---

## Dialogue Checks

**FAULT-DIALOGUE-MISSING-AT-ANCHOR:**
- s01n06 (taylor-hebert-kl-122ac speaks to jarvis-coin-kl-courier): dialogue file entry 1 @6 present and matches bone @-position. PASS.
- s01n08 (jarvis-coin-kl-courier speaks to taylor-hebert-kl-122ac): dialogue file entries 8 @8 and 9 @8 present and match bone @-position. PASS.

**FAULT-DIALOGUE-CARD-VIOLATION:**
- Taylor entry 1 @6 ("Yes. The terms hold with two changes. You will have patterns — what moves through the streets, what does not, where the seams sit — not raw report of who said what to whom. The interval is mine to set. The volume is mine to set."): cold-utilitarian register; flat transactional delivery; named modification as assertion not request; no Earth-Bet nouns; no Skitter/Khepri self-reference; no theme narration; no self-justification to the room. Consistent with card hard fences. PASS.
- Jarvis entry 8 @8 ("Those terms are acceptable to the man I serve. The volume yours. The interval yours. The substance pattern-reports from the wards you walk."): transactional flat-affect; begins with most functionally relevant item; no patron name; no moral investment; no lingering. Consistent with card hard fences. PASS.
- Jarvis entry 9 @8 ("Same place. First bell. Three days."): ultra-minimal; logistical; closes exchange immediately. Consistent with card voice tells. PASS.

**FAULT-DIALOGUE-OBJECTIVE-MISSING:**
- Taylor @6: objective non-empty; matches anchor bone's speech-act (delivering the yes = the social_tether-antag +1.0 move). PASS.
- Jarvis @8: objective non-empty; matches anchor bone's routing-confirmation function (converting yes into settled arrangement = position-prot-rise +1.0 move). PASS.
- Jarvis @9: objective non-empty; matches anchor bone's return-schedule installation. PASS.

**FAULT-DIALOGUE-EARTH-BET-FENCE:** No Earth-Bet nouns (Khepri, Endbringer, Skitter, PRT, Brockton Bay, cape, parahuman) in any of the three utterances. PASS.

**FAULT-DIALOGUE-COVERAGE:** Both speakers (taylor-hebert-kl-122ac, jarvis-coin-kl-courier) have per-character dialogue files with ≥1 c04 entry. PASS.

---

## Findings List

```yaml
findings:

  - id: fault-001
    type: fault
    what: >
      b01c04s01 substance_delta.axes_held declares capability held (rationale: "acceptance is
      operational, not deployment; no new coverage range extends here"). No bone in s01 carries
      capability in its axes_held[]. All 10 bones (n01-n10) reviewed; none hold capability.
    why: >
      HELD-AXIS-NOT-WITNESSED (HARD). The scene contract declares capability as a held axis;
      the bone-gate requires ≥1 bone per scene to enact the stillness-against-pressure or
      dormancy on each contracted held axis at bone level. Without a bone-level enactment,
      downstream /and-review bones cannot verify the hold was paid for, and facets have no
      anchor for capability-suppression content in this scene.
    criteria: >
      s01 must contain ≥1 bone whose axes_held[] includes capability, with a rationale naming
      the discipline (e.g. acceptance is operational, not deployment; no coverage range extends
      here). The bone's SVO must be a concrete physical action satisfying the SVO discipline
      fence — no PP, no negation, transitive verb.

  - id: fault-002
    type: fault
    what: >
      b01c04s02 substance_delta.axes_held declares political_register-prot held (rationale:
      "ward-level walk; coverage substrate is foot-traffic, sickness-clustering, alley-
      agitation; no court-tier observation material yet present in the expanded feed"). No bone
      in s02 carries political_register-prot in its axes_held[]. All 11 bones (n01-n11)
      reviewed; none hold political_register-prot.
    why: >
      HELD-AXIS-NOT-WITNESSED (HARD). Same structural failure as fault-001 in s02. The
      chapter-level hold on political_register-prot requires bone-level enactment in each
      scene that contracts the hold; s02 has no such bone. The held entry in the scene
      contract is asserted but not enacted at execution.
    criteria: >
      s02 must contain ≥1 bone whose axes_held[] includes political_register-prot, with a
      rationale naming the discipline (e.g. feed returns Flea Bottom-tier foot-traffic and
      sickness-clustering; no court-register observation surface present at this range).
      SVO discipline fence applies.

  - id: fault-003
    type: fault
    what: >
      b01c04s03 substance_delta.axes_held declares moral_framework held (rationale:
      "rationalization stable at chapter close: Taylor frames the report as naming-a-destination-
      for-what-she-already-knows; licensed exception is operative and believed; framework still
      named and believed"). No bone in s03 carries moral_framework in its axes_held[]. All 12
      bones (n01-n12) reviewed: n10 holds moral_legibility_to_self; n11 holds
      relational_anchor_status; n12 holds moral_legibility_to_self. None hold moral_framework.
    why: >
      HELD-AXIS-NOT-WITNESSED (HARD). The s03 scene contract declares moral_framework as a
      held axis. The chapter's thematic thesis — rationalization operative, framework still
      named and believed — has no bone-level enactment in s03. The two moral_legibility_to_self
      held bones (n10, n12) serve a different axis. The moral_framework hold (the framework
      is intact and running as rationalization-machine, not the legibility of that
      rationalization) must be separately anchored.
    criteria: >
      s03 must contain ≥1 bone whose axes_held[] includes moral_framework, with a rationale
      naming the discipline. The enactment must be distinct in content from the two
      moral_legibility_to_self bones already present. SVO discipline fence applies. Note:
      adding this bone may simultaneously address signal-002 (CHATTER-OVER-CAP) if fixer
      converts an existing s03 chatter into a held bone.

  - id: fault-004
    type: fault
    what: >
      b01c04s03 substance_delta.axes_held declares political_register-prot held (rationale:
      "the report Taylor hands to Jarvis is junction-agitation and ward-pattern from
      Flea Bottom-tier sources; no court-tier surface in the feed yet"). No bone in s03
      carries political_register-prot in its axes_held[]. All 12 bones (n01-n12) reviewed;
      none hold political_register-prot.
    why: >
      HELD-AXIS-NOT-WITNESSED (HARD). The s03 scene contract declares political_register-prot
      as held. The chapter's arc-shaping depends on the feed remaining Flea Bottom-tier through
      c04 — this sets up the political_register-prot opening at c05 as a distinct narrative
      threshold. Without bone-level enactment of the hold in s03, the threshold is asserted
      in the contract but invisible at execution.
    criteria: >
      s03 must contain ≥1 bone whose axes_held[] includes political_register-prot, with a
      rationale naming the discipline (e.g. the report content is junction-agitation and
      ward-pattern; no court-tier observation present in feed at this scene). SVO discipline
      fence applies. Fixer may address fault-003 and fault-004 jointly if a single SVO can
      physically enact both holds with separate axis entries in axes_held[].

  - id: fault-005
    type: fault
    what: >
      b01c04s03 substance_delta.axes_held declares position-prot-rise held (rationale:
      "full +1.0 consolidated to s01 bone at /and-write Phase 1 redo 2026-05-27; cl02 gain
      completed at acceptance; Sera confirmation (s03) confirms the arrangement is functional
      but does not re-advance the position axis"). No bone in s03 carries position-prot-rise
      in its axes_held[]. All 12 bones (n01-n12) reviewed; none hold position-prot-rise.
    why: >
      HELD-AXIS-NOT-WITNESSED (HARD). The scene contract lists position-prot-rise under
      axes_held[], which obligates a bone-level enactment regardless of the rationale
      explaining why the axis does not move. Without a bone confirming the axis is
      disciplined-at-current-rank (held against the pressure of Sera's confirmation arriving),
      the hold is unwitnessed. This also matters for the downstream reader of bones: the Sera
      confirmation scene (n05-n06) is the content most likely to invite a position-prot-rise
      read; a held bone makes the non-advance explicit.
    criteria: >
      s03 must contain ≥1 bone whose axes_held[] includes position-prot-rise, with a rationale
      naming the discipline (e.g. Sera's confirmation confirms the arrangement is functional;
      the position axis does not re-advance — the naming-event completed at s01; confirmation
      is receipt, not re-advancement). SVO discipline fence applies. Alternatively: if fixer
      determines position-prot-rise does not belong in s03 axes_held[] (i.e. the contract
      overclaims the held set), fixer must remove position-prot-rise from s03
      substance_delta.axes_held[] and verify no downstream cascade impact from the contract
      change.

  - id: signal-001
    type: flag
    what: >
      b01c04s01 chatter density: 5 chatter bones (n01, n02, n03, n04, n09) out of 10 total.
      density_target.min = 0.6; cap = (1 − 0.6) × 10 = 4 chatter bones. Actual = 5.
      CHATTER-OVER-CAP by 1 bone.
    why: >
      The realized non-chatter density (50%) falls below the contracted floor (60%). This
      will surface as a density flag at /and-review bones.
    criteria: null
    signal_disposition: accepted
    signal_disposition_rationale: >
      n01 is the scene's sensory-grounding bone — removing it violates the HARD grounding
      requirement. n02 covers [event: Taylor returns] (chunk-tag mandatory). n03 covers
      Taylor's operational positioning at the shed-wall (event_map entry). n04 covers
      [image: Jarvis Coin unhurried] (chunk-tag mandatory). n09 covers [event: lever walks
      out with Jarvis] and the opposing-force departure beat (event_map entry). All five
      chatters serve distinct, non-redundant event_map entries. The PP-stripping discipline
      prevents collapsing any entry into a prior bone. The cap excess is structurally forced
      by the mandatory event-coverage requirements combined with the SVO discipline fence.
      ACCEPTED.

  - id: signal-002
    type: flag
    what: >
      b01c04s03 chatter density: 6 chatter bones (n01, n02, n04, n05, n06, n08) out of 12
      total. density_target.min = 0.7; cap = (1 − 0.7) × 12 = 3.6 → 4 bone ceiling.
      Actual = 6. CHATTER-OVER-CAP by 2 bones.
    why: >
      s03 is the most demanding scene by density contract (0.7-0.8) and the most chatter-
      dense in the chapter (50%). Combined with three HELD-AXIS-NOT-WITNESSED faults in s03
      (fault-003, fault-004, fault-005), the bone-set has headroom that should be occupied
      by held bones witnessing contracted held axes rather than by additional chatter.
    criteria: null
    signal_disposition: remediated
    signal_disposition_rationale: >
      Fixer is obligated to add ≥1 held bone per fault-003 (moral_framework), fault-004
      (political_register-prot), and fault-005 (position-prot-rise) in s03. Adding 3 held
      bones raises bone count to 15 and the chatter ratio to 6/15 = 40%, satisfying the
      density floor (≥70% non-chatter at min). Fixer should assess whether any existing s03
      chatter bone can be converted to a held bone to address the fault findings more
      efficiently while managing total bone count. REMEDIATED (conditional on faults-003,
      004, 005 fix delivering ≥3 non-chatter bones to s03).

  - id: signal-003
    type: flag
    what: >
      REGISTER-AS-MANNERISM-maps-[noun]: verb-object pair "maps the [noun]" appears 3 times
      within s02 (all within a single scene): s02n04 "maps the junction-agitation"; s02n07
      "maps the oswyn-mudway-flea-bottom-elder interval"; s02n11 "maps the second-ward
      junction". Chapter threshold ≥3 met within a single scene.
    why: >
      Three repetitions of the same verb with varying objects within one 11-bone scene risks
      reader perception as an unwitting tic rather than structural parallelism.
    criteria: null
    signal_disposition: accepted
    signal_disposition_rationale: >
      Each of the three "maps" bones anchors a distinct held axis: n04 anchors
      moral_legibility_to_self (ward-mapping as rote); n07 anchors moral_framework (Oswyn
      interval mapped without naming it intelligence-routing); n11 anchors a second
      moral_legibility_to_self instance (second-ward junction mapped without logging Wren).
      The three serve non-redundant structural functions that the worm-canon-pedant watch
      explicitly required (anchor-discipline lines as bone-level content). The repetition is
      intentional structural parallelism: the same procedure enacted three times in service
      of three distinct suppressions. The verb does not repeat in s03. ACCEPTED.

  - id: signal-004
    type: flag
    what: >
      REGISTER-AS-MANNERISM-[insect-feed]-returns-[entity]: "[the insect-feed] returns
      [named entity]" appears 4 times across the chapter: s01n05 (returns jarvis); s02n06
      (returns oswyn); s02n09 (returns wren); s03n11 (returns wren). The s02n09 and s03n11
      instances are identical subject-verb-object.
    why: >
      Four repetitions of the canonical feed-output form across 33 bones; the identical
      "feed returns wren" pair (s02n09/s03n11) across two scenes warrants flagging.
    criteria: null
    signal_disposition: accepted
    signal_disposition_rationale: >
      "Returns" is the canonical feed-output verb established in b01-c02 (bones 1, 2, 6, 15,
      24, 28 per redo notes). It is load-bearing as the insect-feed's behavioral signature
      — encoding the relationship of feed-as-subject yielding person-as-output. The two
      "feed returns wren" instances (s02n09 and s03n11) occur in different scenes serving
      different held axes: s02n09 anchors relational_anchor_status (feed returning Wren into
      coverage, first form); s03n11 anchors relational_anchor_status again (feed touching
      Wren and passing, second form — a distinct enactment). The worm-canon-pedant audience
      watch specifically required these anchor-discipline lines as separate bone-level
      contents. Repetition is by design. ACCEPTED.

  - id: signal-005
    type: flag
    what: >
      REGISTER-AS-MANNERISM-exits-[location]: "exits the [location]" appears 4 times:
      s01n09 (exits the lane-mouth); s01n10 (exits the cooper's yard); s03n09 (exits the
      cooper's yard); s03n12 (exits the stitch-house lane).
    why: >
      Four occurrences of "exits the [location]" across 33 bones, concentrating in
      departure and scene-close positions.
    criteria: null
    signal_disposition: accepted
    signal_disposition_rationale: >
      The SVO discipline fence eliminates all PP-based departure forms ("leaves through
      the lane-mouth" = direction PP; "departs toward Eel Alley" = destination PP; "goes"
      = intransitive motion without destination). "Exits [location-as-DO]" is the only
      compliant transitive departure form under the bones schema. Each of the four instances
      marks a distinct narrative beat and covers a distinct event_map entry. No alternative
      verb form is both transitive and concrete under current schema constraints. ACCEPTED.

  - id: signal-006
    type: flag
    what: >
      REGISTER-AS-MANNERISM-enters-[location]: "enters the [location]" appears 5 times:
      s01n02 (enters the cooper's yard); s01n04 (enters the lane-mouth); s02n02 (enters Pig
      Tallow Lane); s03n02 (enters Roper's Court); s03n05 (enters the cooper's yard).
    why: >
      Five occurrences of "enters [location]" across 33 bones, saturating scene-opening
      arrival beats.
    criteria: null
    signal_disposition: accepted
    signal_disposition_rationale: >
      Same structural necessity as signal-005. The PP-stripping discipline makes "enters
      [location-as-DO]" the correct and only compliant form for scene-initiating arrival
      beats under the bones schema. Each of the five instances opens a new scene or a
      character's arrival in an established scene; none can be merged without creating
      FAULT-FORM-CONJUNCTION. ACCEPTED.

  - id: flag-001
    type: flag
    what: >
      All three scenes (s01, s02, s03) have declared stakes_axis magnitudes tied with at
      least one other in-motion axis: s01 social_tether-antag +1.0 tied with position-prot-rise
      +1.0; s02 social_tether-prot-rise +1.0 tied with capability +1.0; s03 social_tether-
      prot-rise +1.0 tied with capability +1.0 and position-world +1.0 (three-way tie).
    why: >
      The stakes-axis-dominant check requires the declared stakes axis to have the largest
      delivered aggregate magnitude. In all three scenes the stakes axis is tied rather than
      dominant. This is a structural condition created by the bone-level magnitude floor (all
      moving bones must be ≥1.0) combined with per-scene targets of exactly 1.0 per axis,
      which produces structural ties at every scene. In stitched prose, a tied stakes axis
      may not register as the scene's primary tension driver; the rendering agent will need
      to weight stakes-axis content above tied-axis content in the lens-anchoring pass.
    criteria: null
```

---

## Auditor Notes

**Pattern: three paired faults (001+fault-002; 003+004; 003+004+005).** The five HELD-AXIS-NOT-WITNESSED faults follow a consistent pattern: capability (s01), political_register-prot (s02), moral_framework + political_register-prot + position-prot-rise (s03). This is not random omission — the redo correctly identified the need to strip prior drafts' invalid 0.5-magnitude splits and consolidate to single full-rank bones, but the corrective focus was on the moving-bone consolidation. The held-bone witness requirement for contracted held axes was not carried through. The fixer's correction scope is additive (new held bones) rather than revisionary (no existing bones need to change).

**Fixer efficiency path:** The three s03 faults (003, 004, 005) can potentially be addressed by two new bones if one bone witnesses moral_framework + position-prot-rise jointly (two entries in a single bone's axes_held[]) and a second witnesses political_register-prot. This would raise s03 to 14 bones (chatter ratio 6/14 = 43%, satisfying density floor) and simultaneously remediate signal-002. Auditor recommends fixer evaluate this path before authoring three separate bones.

**Dialogue: clean.** All three utterances pass all five FAULT-DIALOGUE-* checks. The Earth-Bet fence is particularly clean — Taylor's acceptance speech uses no parahuman vocabulary. Jarvis's register is consistent with the behavior card throughout.

**Chapter-level axis aggregate: all EXACT.** No per-chapter Δ drift findings.
