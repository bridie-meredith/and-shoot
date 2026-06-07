```yaml
audit:
  scope: chapter
  target: b01c07
  timestamp: 2026-05-30
  gate: substance-chunk-phase-5
  findings:

    - id: fault-001
      type: pass
      what: "Check axis 1 — Contract-text match: political_register-prot"
      why: "s02 chunk text contains the principled-slower thesis forcing Taylor to locate the object of resentment ([event: argument-named-without-application], [force: taylor-genuine-engagement], 'she turns the thesis over, reads it for structural soundness'). s03 chunk text forces precise articulation via the counter-argument and named-body deployment ([event: body-count-named], [mechanism: specific-body-as-evidence]). Both scenes describe causal events for a +0.3 / +0.2 register-sharpening move respectively. The substance_delta notes trace directly to those events. No rank claim is present without a described cause."
      why: "N/A — pass"

    - id: fault-002
      type: pass
      what: "Check axis 2 — Contract-text match: social_tether-prot-rise"
      why: "s02 chunk text shows Taylor remaining in conversation beyond operational necessity ('She could move; she does not') and engaging in a working-through that is explicitly 'not performance' — a non-transactional embedding event. s03 chunk text names the completion condition: 'neither retreats — is the social embedding event; the encounter has become a working conversation that both parties inhabit without transaction.' Each +0.5 sub-increment has a described cause in the chunk. No rank claim without cause."
      why: "N/A — pass"

    - id: fault-003
      type: pass
      what: "Check axis 3 — Sum roll-up: political_register-prot"
      why: "s01 contributes 0 (axes_in_motion: []). s02 target_delta_magnitude: 0.3 (direction: up). s03 target_delta_magnitude: 0.2 (direction: up). Sum = 0.5. Chapter-level target_delta_magnitude = 0.5. Difference = 0. Within ±1 tolerance. MATCH confirmed."
      why: "N/A — pass"

    - id: fault-004
      type: pass
      what: "Check axis 4 — Sum roll-up: social_tether-prot-rise"
      why: "s01 contributes 0 (axes_in_motion: []). s02 target_delta_magnitude: 0.5 (direction: up). s03 target_delta_magnitude: 0.5 (direction: up). Sum = 1.0. Chapter-level target_delta_magnitude = 1.0. Difference = 0. Within ±1 tolerance. MATCH confirmed."
      why: "N/A — pass"

    - id: fault-005
      type: pass
      what: "Check axis 5 — Thematic axis coverage (URI-CONTRACT-THEMATIC-AXIS, HARD gate)"
      why: "Chapter goal: 'the Halvard argument forces Taylor to ARTICULATE what the resentment is toward → political_register-prot sharpens.' The chapter-level substance_delta declares political_register-prot in axes_in_motion[] with direction: up, target_delta_magnitude: 0.5. The goal-thesis axis is explicitly declared in-motion. THEMATIC-AXIS-UNDECLARED does not fire."
      why: "N/A — pass"

    - id: fault-006
      type: pass
      what: "Check axis 6 — Cost-ledger consistency"
      why: "Both moving axes (political_register-prot and social_tether-prot-rise) carry cost_ledger_anchor: null at both chapter level and per-scene level (s02 and s03). Series trajectory (series-trajectory.md) places no cost-ledger anchor at d05–d08. The d05 shift (readable-resentment) and the social embedding arc that builds toward d07 are progressive accumulations, not ledger-cost events. No cl-anchor in the series trajectory targets c07 or the b01c07-equivalent delta band. Null is correct and consistent. No scene claims a cost-ledger anchor that does not resolve."
      why: "N/A — pass"

    - id: fault-007
      type: pass
      what: "Check axis 7 — Held-axis rationale soundness"
      why: |
        All four held axes inspected across all three scenes:

        moral_framework (rank 0 held throughout):
          s01: 'No new breach; the accounting is consolidation-mode; ledger holds at rank 0' — correct; no actional event in s01.
          s02: 'No new breach; the engagement is evaluative, not actional; moral_framework holds at rank 0' — correct; taking an argument seriously is not a breach under the ledger-discipline framework.
          s03: 'The counter is Taylor's existing rationalization deployed honestly; no new breach; the ledger-discipline is in evidence; moral_framework holds at rank 0' — correct; deploying an existing rationalization does not move the framework axis.
          All three rationales are internally sound. Note: handoff_in character_state records 'moral_framework rank 0' matching these holds.

        moral_legibility_to_self (rank 5 held throughout):
          s01: 'The passive-radar note on Halvard is a texture beat, not a legibility event; Taylor files it without examining it; legibility holds at rank 5' — correct; texture without examination is not a legibility event.
          s02: 'Taking the argument seriously is legibility working, per the chapter contract — but resolution is deferred; legibility holds at rank 5' — correct; the chapter contract explicitly states 'counter-argument genuinely engaged means Taylor's legibility is working; but resolution is deferred, not advanced.' The held rationale matches the chapter-level rationale verbatim.
          s03: 'Resolution DEFERRED, per chapter contract; genuine engagement with the argument is legibility working, not advancing; holds at rank 5' — consistent.
          All rationales sound.

        relational_anchor_status (rank 3 held throughout):
          s01: 'Wren in coverage; no new weight; anchor holds at rank 3' — correct; Halvard is not the anchor; Wren is the anchor; Halvard's presence does not move the anchor axis.
          s02: 'No new weight on the anchor; holds at rank 3' — correct.
          s03: 'Wren not in this scene's content; anchor holds at rank 3' — correct.
          All rationales sound and consistent with handoff_in/out tracking Wren at anchor rank 3.

        capability (held throughout):
          s01: 'Maintenance coverage; no new deployment; holds at current rank' — correct; the insect-feed runs at 'usual low-profile density' (chunk text); no expansion event.
          s02: 'No new deployment; holds' — correct; Taylor is stationary in conversation; no coverage expansion.
          s03: 'No deployment; holds' — correct.
          All rationales sound. Note: b01c08 handoff_in records capability rank 4.5 matching the expectation that c07 does not advance capability.
      why: "N/A — pass"

    - id: fault-008
      type: pass
      what: "Check axis 8 — Earth-Bet fence scan"
      why: |
        Full scan of chunk text, notes, rationales, and bracketed tags across all three scenes and the chapter-level block for Earth-Bet / Worm proper nouns:
          - 'Khepri' does not appear in any chunk text, scene_conflict text, or notes fields in the draft file. 
          - 'parahuman', 'Worm', 'Gold Morning', 'Taylor Hebert' (full name), 'Undersiders', 'Skitter', 'Weaver', or any other Worm-specific jargon: not present in any chunk prose or notes.
          - The term 'Khepri-echo' does not appear in any chunk text.
          - Memory.md b01c08 entry contains 'Khepri-echo' in its notes field ('Oswyn integration is coverage architecture... Khepri-echo visible in method'), but this is in the b01c08 contract, not b01c07. The b01c07 draft file is clean.
          - One occurrence of 'Khepri' appears in b01c08's memory block (line 4712: 'Khepri-echo visible in method') — this is out of scope for this audit but noted for the b01c08 chunk audit.
        Earth-Bet fence: no violation in b01c07 draft.
      why: "N/A — pass"

    - id: fault-009
      type: flag
      what: "s01 stakes_axis field reads 'social_tether-prot-rise' but s01 substance_delta shows axes_in_motion: [] with social_tether held for the full scene."
      why: "The stakes_axis field conventionally names the axis most at tension in the scene conflict. s01 has no axis in motion; social_tether is explicitly held with the rationale that 'the tether-deepening event is the genuine engagement in s02/s03; this scene opens the encounter without delivering the embedding increment.' A stakes_axis pointing to a held axis is not a contract violation — the field names the axis the scene is staging, not the axis that moves. However, if the stakes_axis field is read by downstream authoring as an axis that must move in the scene, this creates drift pressure. The inconsistency is notational, not causal — the substance_delta is authoritative and correctly shows no movement. Fixer action is not required; the flag is for /and-write Phase 1 disambiguation."
      why: "If /and-write Phase 1 interprets stakes_axis as an axis that must receive a bone with an in-motion move, it may generate spurious bone-gate pressure against a scene where the axis is correctly held. Downstream authoring could produce an unearned social_tether movement in s01 that the chunk contract does not support."

    - id: fault-010
      type: pass
      what: "Cross-check: handoff_in character_state versus chapter contract opening ranks"
      why: |
        handoff_in character_state (sourced from b01c06 close):
          moral_framework rank 0 — chapter contract holds at 0 throughout: MATCH
          relational_anchor rank 3 — chapter contract holds at rank 3 throughout: MATCH
          moral_legibility rank 5 — chapter contract holds at rank 5 throughout: MATCH
          political_register-prot rank 2.5 — chapter moves +0.5 to deliver rank 3.0 at close: consistent with handoff_out 'political_register-prot rank 3 (register sharpened by Halvard articulation demand)': MATCH
          social_tether-prot-rise rank 3 — chapter moves +1.0 to deliver rank 4 at close: consistent with handoff_out 'social_tether-prot-rise rank 4': MATCH
        All opening and closing ranks consistent across handoff_in / contract / handoff_out.
      why: "N/A — pass"
```
