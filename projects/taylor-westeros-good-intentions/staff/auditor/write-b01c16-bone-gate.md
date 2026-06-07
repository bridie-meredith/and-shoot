audit:
  scope: chapter
  target: b01c16
  timestamp: 2026-06-04
  gate: /and-write Phase 6 substance bone-gate
  hard_count: 0
  signal_count: 2
  dialogue_hard_count: 0

findings:

  - id: pass-001
    type: pass
    what: PER-BONE — s01 (8 bones)
    why: All held bones enact discipline correctly. Axes moral_legibility, relational_anchor_status, capability each have ≥1 witnessing bone. Grounding-class bones (n02, n03, n08) meet the sensory-grounding floor. Opposing-force visible via n06 (Halvard lifts head). No chatter bones.

  - id: pass-002
    type: pass
    what: PER-BONE — s02 (10 bones)
    why: All held bones enact discipline correctly across four held axes (position-prot-collapse, social_tether-prot-collapse, moral_legibility, capability). Grounding-class (n03, n08, n04) meets floor. Opposing-force visible via n02/n09 (counter) and n01/n05/n06 (physical pressure). Dialogue-anchor bones n02 and n09 carry correct citation tokens. No chatter bones.

  - id: pass-003
    type: pass
    what: PER-BONE — s03 (9 bones)
    why: Moving bones n01 (+0.25) and n03 (+0.25) are bonefide — both are concrete actor-verb-object SVOs that physically enact the claimed moral_legibility movement; cause is visible in each (body-stop as non-answer; turn-away as foreclosure). Aggregate Δ = 0.5 matches target 0.5. All held bones disciplined. Grounding-class (n05, n06, n07) meets floor. Opposing-force via n02/n08 (feed returns Halvard).

  - id: pass-004
    type: pass
    what: EVENT-NOT-CONCRETE check — s02 central event (position-arithmetic) and s03 central event (walk-away)
    why: s02n04 "taylor-hebert-kl-122ac presses the fence-rail" is actor-verb-object; not process-rendered. s03 walk-away covered by n01 (stops) + n03 (turns) + n04 (walks) — all concrete SVOs. EVENT-NOT-CONCRETE does NOT fire on either central event.

  - id: pass-005
    type: pass
    what: ABSTRACTION-DOMINANT SIGNAL check — all three scenes
    why: s01 grounding-class = 3 vs floor ceil(0.25×8) = 2. s02 grounding-class = 3 vs floor ceil(0.25×10) = 3. s03 grounding-class = 3 vs floor ceil(0.25×9) = 3. All three scenes meet or exceed the grounding floor. ABSTRACTION-DOMINANT SIGNAL does not fire.

  - id: pass-006
    type: pass
    what: PER-SCENE event-presence and event_map coverage — all three scenes
    why: Every event_map entry is covered by at least one existing bone that is or occasions the event. Omissions (halvard-pastoral-register-visible s01; halvard-does-not-call-after s03) carry documented rationales. Stakes-axis dominant in s03 (moral_legibility is the sole mover). Opposing-force visible in all three scenes.

  - id: pass-007
    type: pass
    what: COST-NOT-PAID and SUBSTANCE-SUSPECT-cheap-gain checks
    why: All chapter cost-ledger anchors are null per scene contracts. Cheap-gain checks are N/A for this chapter.

  - id: signal-001
    type: flag
    what: Register-as-mannerism — verb "marks" appears 4 times across the chapter: s01n02 "marks the storehouse wall," s01n03 "marks the kneeling-bench," s02n03 "marks the clearing-margin," s03n05 "marks the storehouse wall." The exact VERB+OBJECT pair "marks the storehouse wall" appears twice (s01n02, s03n05); no single pair reaches 3, so the formal register-as-mannerism SIGNAL criterion is not triggered. The aggregate verb-frequency (4 instances of "marks" across 27 bones) and the straight repeat at s03n05 are advisory.
    why: At prose level, four uses of "marks" for environmental set-dressing across three scenes will be perceptible as a tic. The s03n05 exact repeat of s01n02 is the highest-risk instance — it is a bookend-callback but may read as autopilot. Downstream note for /and-stitch Phase 3 (redundancy cull) and Phase 8 (editorial reflection).

  - id: signal-002
    type: flag
    what: s03 event_map entry "taylor-has-full-counter" is mapped to [n02] with no omission_rationale in the event_map, though the event is interior-state (Taylor has the counter but withholds it).
    why: n02 "storehouse-eaves flies return septon-halvard-flea-bottom" covers the occasion for the withheld counter (Taylor's feed registers Halvard mid-sentence, which is the moment the counter could be spoken) but does not directly surface Taylor's interiority. The coverage is legitimate as an occasion-carrier. Absence of a rationale annotation makes the mapping opaque. No fixer action required; note for /and-facets narrator-interest facet to carry the interior-state directly.

  - id: pass-008
    type: pass
    what: DIALOGUE — FAULT-DIALOGUE-MISSING-AT-ANCHOR
    why: Both anchor entries are present. s02n02 → septon-halvard-flea-bottom:1 at @b01c16s02n02. s02n09 → septon-halvard-flea-bottom:2 at @b01c16s02n09. No missing anchors.

  - id: pass-009
    type: pass
    what: DIALOGUE — FAULT-DIALOGUE-CARD-VIOLATION (behavior-card westeros-septon; hard fences 1–5)
    why: Entry 1 names specific survivors (woman with chest-complaint, fishmonger's-lane boy) in plain Westerosi register. Disclaims claiming credit. Does not supply an alternative method. Does not name Taylor's capability or origin. Entry 2 explicitly disclaims the demand to do differently and asks only for self-knowledge. No theological jargon in either entry. No accusation. All five hard fences and all voice tells honored in both utterances.

  - id: pass-010
    type: pass
    what: DIALOGUE — FAULT-DIALOGUE-OBJECTIVE-MISSING
    why: Entry 1 objective ("name the specific people she kept alive and the cost the survivors carry, giving credit without claiming them or demanding anything back") is present and the utterance executes it. Entry 2 objective ("ask her to KNOW what she is doing, explicitly disclaiming any demand that she do differently") is present and the utterance executes it.

  - id: pass-011
    type: pass
    what: DIALOGUE — FAULT-DIALOGUE-EARTH-BET-FENCE
    why: Both entries contain no parahuman jargon, no Earth-Bet proper nouns, no Worm-universe terminology. Both are fully in Westerosi register.

  - id: pass-012
    type: pass
    what: DIALOGUE — FAULT-DIALOGUE-COVERAGE
    why: One speaker with dialogue-anchor bones (septon-halvard-flea-bottom). File present with both entries. Coverage complete.
