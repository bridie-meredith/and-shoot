```yaml
audit:
  scope: chapter
  target: b01c08
  timestamp: 2026-05-31
  findings:

    - id: fault-001
      type: pass
      what: "Check 1 — Contract↔text fidelity (s01): chunk delivers capability +0.5 via Oswyn watcher-network observed and geometrically integrated into feed matrix; notes field confirms 'Khepri-echo visible in method to reader, not to Taylor'; mechanism, event, force, and image tags all present; substance_delta rationale consistent with chunk text."
      why: "No divergence between declared delta and narrative delivery."

    - id: fault-002
      type: pass
      what: "Check 1 — Contract↔text fidelity (s02): chunk delivers Aemond-adjacent pressure at logistics-class intensity; mechanism tag [mechanism: aemond-feed-entry-as-routine-logistics] and image [image: escalation-engine-visible-at-feed-edge] present; substance_delta rationale 'resentment does not advance on operational scheduling noise' consistent with axes_in_motion: []."
      why: "No divergence."

    - id: fault-003
      type: pass
      what: "Check 1 — Contract↔text fidelity (s03): chunk delivers body-map advance and Oswyn-network integration confirmation; 'body-map advances by one node' and 'Oswyn does not know this' directly execute the chapter contract's courier-face and Oswyn-integration obligations; mechanism [mechanism: body-map-node-built-without-asking] tags the causal sequence."
      why: "No divergence."

    - id: fault-004
      type: pass
      what: "Check 2 — Cost-ledger consistency: all three scenes declare cost_ledger_anchor: null; chapter contract declares cost_ledger_anchor: null for the single in-motion axis (capability +0.5). No ledger anchor claimed anywhere in draft."
      why: "Consistent. No phantom anchor."

    - id: fault-005
      type: pass
      what: "Check 3 — Sum roll-up: capability s01 +0.5 + s02 0 + s03 0 = 0.5 EXACT matches chapter contract +0.5. All other axes declared zero-motion across scenes; chapter contract holds all other axes. No overage, no shortfall."
      why: "Roll-up clean."

    - id: fault-006
      type: pass
      what: "Check 4 — stakes_axis/axes union: s01 stakes_axis=moral_framework present in axes_held (rationale 'integration executed without ledger-entry'); s02 stakes_axis=political_register-prot present in axes_held; s03 stakes_axis=capability present in axes_held (rationale 'capability advanced in s01; this scene closes the courier-face thread ... Δ was taken at s01; holds at rank 5'). All three pass the union rule."
      why: "No stakes_axis absent from its scene's axis union."

    - id: fault-007
      type: flag
      what: "Check 4 note — s03 stakes_axis=capability is a held-axis stakes scene, consistent with c07s01 precedent (parking-lot pl-2026-05-30-004 fault-009). Draft carries no /and-write note flagging this. The c07 precedent resolution note says '/and-write Phase 1 must read it as conflict-frame label, NOT a Δ-authoring mandate.' The b01c08 draft records no equivalent annotation on s03's stakes_axis line."
      why: "No audit fault — legal per Phase-3 union rule — but missing the annotation risks /and-write Phase 1 generating bone-gate pressure to move a held axis, repeating the c07 fault-009 pattern. Recommend adding a NOTE comment to s03.scene_conflict.stakes_axis matching the c07s01 form."

    - id: fault-008
      type: pass
      what: "Check 5 — Thematic-axis-coverage: chapter goal names 'Khepri-repetition accusations' as the thematic thread; chapter contract declares moral_framework in axes_held with rationale 'ledger does not open on this act; framework holds at current crack-level by Taylor's accounting'; all three scenes maintain this rationale. Draft chunk text enacts the Khepri-echo as reader-visible, not Taylor-legible (s01 notes 'Khepri-echo visible in method to reader, not to Taylor'; s03 'Oswyn does not know this'). Thematic thread carried without on-page articulation."
      why: "PASS — load-bearing held discipline is present in contract and enacted in text."

    - id: fault-009
      type: pass
      what: "Check 6 — Chunk-tag protocol: s01 carries event, mechanism, image, and force tags for all load-bearing spans (coverage-integration observed, positions mapped, gap filed, coverage-integration-without-consent). s02 carries event, mechanism, image, and force tags including aemond-feed-entry-as-routine-logistics, aemond-adjacent-pressure-enters-feed, escalation-engine-visible-at-feed-edge. s03 carries event, mechanism, image, and force tags for courier-face-at-oswyn-mention, courier-named-corwick, body-map-advancing, body-map-node-built-without-asking, oswyn-unknowing-node-complete."
      why: "All major load-bearing spans tagged. No untagged central-event, load-bearing image, or force visible."

    - id: fault-010
      type: pass
      what: "Check 7 — Parking-lot pl-2026-05-30-001 disposition: draft header lines 3-10 record 'cl-d06 routing: DEFERRED to c09/c10' with explicit rationale naming b01c08-b01c10 candidate window, stating 'No relational_anchor_status Δ this chapter'; s01-s03 axes_held confirm relational_anchor_status held at rank 3 across all three scenes. Deferral note present; item remains open (status: open in parking-lot). /and-substance chapter b01c09 Phase 3 is the next resolving target."
      why: "Deferral correctly recorded. SOFT item will resurface at b01c09 Phase 0 per Rule 14."

    - id: fault-011
      type: pass
      what: "Check 8 — Handoff mirror: b01c07 handoff_out (memory.md lines 4765-4777) declares: open_threads include 'Halvard counter-argument not resolved', 'Wren anchor rank 3', 'cf-d10-courier-face courier in memory', 'Black-faction elder list consequences pending'; character_state: 'Taylor moral_framework rank 0; political_register-prot rank 3; relational_anchor rank 3; moral_legibility rank 5'; target_chapter: b01c08. b01c08 handoff_in (memory.md lines 4987-4998) declares matching open_threads ('Halvard not resolved', 'cf-d10-courier-face courier in memory unnamed', 'Wren anchor rank 3', 'Black-faction elder consequences pending') and character_state: 'Taylor: capability rank 4.5; moral_framework rank 0; political_register-prot rank 3'. All named items mirror. No new threads in handoff_in that lack a c07 handoff_out source."
      why: "Mirror clean."

    - id: fault-012
      type: pass
      what: "Check 9 — Voice / no-articulation discipline: s01 chunk text has Taylor noting the gap in coverage and filing geometry without any interior articulation of the Khepri-echo or override pattern; 'She does not tell Oswyn she has done this' is behavioral, not reflective. s03 chunk text has Taylor observing the Oswyn-network-subsumed-in-silence image and the body-map advance without naming the pattern: 'Oswyn does not know this. He is still talking when Taylor leaves.' Neither scene contains phrases of the form 'this is what I came to atone for', 'override', 'Khepri', or equivalent pattern-recognition language in Taylor's interior. s01 notes field: 'Khepri-echo visible in method to reader, not to Taylor' — this is a contract annotation, not rendered interior prose."
      why: "No-articulation discipline intact. Held moral_framework rationale matches on-page behavior."

    - id: fault-013
      type: flag
      what: "s02 substance_delta.axes_held includes moral_framework with rationale 'no breach-adjacent act; holds' — a bare three-word rationale vs the chapter contract's more specific 'ledger does not open on this act; framework holds at current crack-level.' The s02 note is technically sufficient but thin for the chapter's most load-bearing held discipline, particularly because s02 is where Aemond-adjacent pressure first enters the feed."
      why: "Not a fault — the held rationale is present and accurate. Flagged as a potential SIGNAL for /and-write Phase 6 bone-gate review: if the bones at this scene carry the moral_framework held with the same thinness, the bone-gate may fire SUBSTANCE-SUSPECT on the absence of opposing-force-visible for the held axis."
```
