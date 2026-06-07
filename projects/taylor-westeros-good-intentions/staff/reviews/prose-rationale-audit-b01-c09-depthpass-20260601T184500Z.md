audit:
  scope: chapter
  target: b01c09
  timestamp: 2026-06-01T18:45:00Z
  run_class: prose-rationale-mute (Phase 9 Step 3.5; DEPTH-PASS re-render; 27 bones)
  auditor_note: |
    Checked all 27 bones. For each bone: extracted concrete physical elements named in
    axes_held[].rationale (or scene opposing_force). Located prose span via annotated trace.
    Confirmed presence of ≥1 concrete-physical token per named element. Depth-pass bones
    (@2/@3/@9/@15) rationale sourced from render-log Phase 1 depth-pass bone-walk (NI/sensory
    facet citations), which is the authoritative held-axis rationale for those additions.
    DEC-0062 honored: s03 moral_legibility HELD — the double-omission is staged by physical
    object arrangement, not by a recognition beat; absence of recognition is design-forbidden
    and is NOT scored as a mute.

  bones_checked: 27
  bones_with_concrete_rationale_element: 16
    # @2, @3, @5, @7, @9, @12, @13, @15, @16, @17, @21, @22, @23, @24, @27
    # + scene B opposing_force (@23-@27 station surface cluster)
  bones_without_concrete_rationale_element: 11
    # @1, @4, @6(moving), @8, @10, @11, @14, @18(moving), @19, @20, @25, @26
    # Rationales for these describe operational/informational states or axis-move mechanics
    # with no named body/object/surface/sensory particular to look for in prose.

  findings:

    - id: fault-001
      type: pass
      what: "@2 (taylor presses lane-stone) — rationale names lane-stone, boot-sole, cold"
      why: n/a
      prose_span: "I pressed the lane-stone underfoot, and the stone was cold up through the boot-sole, and for the length of the press I was only a body standing in a cold lane"
      tokens_found: [lane-stone, boot-sole, cold]
      verdict: STAGED

    - id: fault-002
      type: pass
      what: "@3 (bay-damp beads lane-stone) — rationale names bay-damp, lane-stone, cold wet film"
      why: n/a
      prose_span: "The bay-damp had beaded the lane-stone, a cold wet film resolving on the dry surface where the sun had not yet reached it"
      tokens_found: [bay-damp, lane-stone, cold wet film]
      verdict: STAGED

    - id: fault-003
      type: pass
      what: "@5 (stitch-shop door opens lane-mouth) — rationale names stitch-shop door as physical anchor"
      why: n/a
      prose_span: "the stitch-shop door stood open at the lane-mouth"
      tokens_found: [stitch-shop door]
      verdict: STAGED

    - id: fault-004
      type: pass
      what: "@7 (wren reaches bread-seller corner) — rationale names bread-seller corner as named physical location"
      why: n/a
      prose_span: "My gaze held on the bread-seller's corner a beat before she reached it. She reached the corner."
      tokens_found: [bread-seller's corner]
      verdict: STAGED

    - id: fault-005
      type: pass
      what: "@9 (cold stiffens the fingers) — rationale names cold, fingers, hand, supply cart (fold-and-set)"
      why: n/a
      prose_span: "The cold had stiffened my fingers, and they filed the route anyway, the same fold and set the hand gives a supply cart or a gate, and nothing in the set of the hand marked that this one was Wren — and the keeping has indexed her without once asking."
      tokens_found: [cold, fingers, hand, supply cart]
      verdict: STAGED

    - id: fault-006
      type: pass
      what: "@12 (supply cart marks lower-gate road) — rationale names supply cart as a named physical object"
      why: n/a
      prose_span: "The supply cart marked the lower-gate road"
      tokens_found: [supply cart]
      verdict: STAGED

    - id: fault-007
      type: pass
      what: "@13 (stone-post marks lower gate side-exit) — rationale names stone-post as physical location anchor"
      why: n/a
      prose_span: "The stone-post marked the lower-gate side-exit."
      tokens_found: [stone-post]
      verdict: STAGED

    - id: fault-008
      type: pass
      what: "@15 (cold weights the shoulders) — rationale names cold, shoulders, feed-edge"
      why: n/a
      prose_span: "The cold had settled its weight on my shoulders where I held still at the feed-edge."
      tokens_found: [cold, shoulders, feed-edge]
      verdict: STAGED

    - id: fault-009
      type: pass
      what: "@16 (corwick faces the second man) — rationale names 'physical body-angle' / 'physical orientation'; body is the concrete referent"
      why: n/a
      prose_span: "He went still in me too as his body turned. Corwick faced the second man."
      tokens_found: [body]
      verdict: STAGED

    - id: fault-010
      type: pass
      what: "@17 (corwick squares the shoulders) — rationale names 'held-stance' (physical posture); shoulders is the concrete referent"
      why: n/a
      prose_span: "He squared the shoulders."
      tokens_found: [shoulders]
      verdict: STAGED

    - id: fault-011
      type: pass
      what: "@21 (takes the feed-station) — rationale names feed-station as physical location/substrate"
      why: n/a
      prose_span: "I took the feed-station."
      tokens_found: [feed-station]
      verdict: STAGED

    - id: fault-012
      type: pass
      what: "@22 (folds the packet) — rationale names packet as physical object"
      why: n/a
      prose_span: "I folded the packet."
      tokens_found: [packet]
      verdict: STAGED

    - id: fault-013
      type: pass
      what: "@23 (seals the packet) — rationale names seal, packet, wax, hand"
      why: n/a
      prose_span: "The wax came down under my hand at the weight I had already settled; I sealed the packet, and what the packet held was the only thing the channel would ever see."
      tokens_found: [wax, hand, packet]
      verdict: STAGED

    - id: fault-014
      type: pass
      what: "@24 (ward-coverage notes mark the station-left) — rationale names notes, station surface as physical objects in the thesis-image arrangement"
      why: n/a
      prose_span: "To the left of it the ward-coverage notes marked the station I had left."
      tokens_found: [ward-coverage notes, station]
      verdict: STAGED

    - id: fault-015
      type: pass
      what: "@27 (seal dries) — rationale names drying seal, wax, seal's dry surface as concrete physical elements"
      why: n/a
      prose_span: "The seal dried, the wax gone from soft and warm under the thumb to set firm."
      tokens_found: [seal, wax, thumb]
      verdict: STAGED

  bones_without_checkable_concrete_element:
    # These bones have rationales that describe operational states, axis-move mechanics,
    # or informational absences — no named body/object/surface/sensory particular to look for.
    # They are out of scope for this audit axis and generate no findings.
    - "@1: capability/social_tether rationales describe maintenance-mode circuit entry (abstract)"
    - "@4: capability rationale describes maintenance-mode feed threading (abstract)"
    - "@6: moving axis bone (relational_anchor_status +0.5) — no axes_held rationale"
    - "@8: moral_legibility/moral_framework rationales describe filing action without naming a physical element"
    - "@10: political_register/moral_framework rationales describe informational absence (abstract)"
    - "@11: capability/social_tether rationales describe maintenance-mode circuit entry (abstract); grounding comment names 'lane stones + hill-skyline' but this is a non-rationale authoring note"
    - "@14: capability/political_register rationales describe feed-intake return (abstract)"
    - "@18: moving axis bone (political_register-prot +0.5) — no axes_held rationale"
    - "@19: political_register/moral_legibility rationales describe substrate-close (abstract)"
    - "@20: moral_framework/capability rationales describe operational completion (abstract)"
    - "@25: relational_anchor/moral_legibility rationales name 'internal map' — apparatus-register construct, not a body/object/surface/sensory particular in the concrete-physical sense; no staging check warranted"
    - "@26: political_register/moral_legibility rationales name 'feed-record' — apparatus-register construct; same disposition as @25"

  summary:
    prose_rationale_mute_count: 0
    bones_with_rationale_element_checked: 15
    bones_without_rationale_element: 12
    threshold: 3 (SOFT-BLOCK if ≥3; SIGNAL-ONLY/PASS if <3)
    verdict: PASS
    basis: |
      Every concrete physical element named in a held-axis rationale (or scene opposing_force)
      is staged in the prose span with ≥1 corresponding concrete-physical token. The four
      depth-pass embodiment bones (@2/@3/@9/@15) — the primary additions of this re-render —
      all stage their named physical elements (lane-stone/boot-sole/cold; bay-damp/lane-stone/
      cold-wet-film; cold/fingers/hand/supply-cart; cold/shoulders/feed-edge). No PROSE-
      RATIONALE-MUTE findings. 0 < threshold of 3. Verdict: PASS (not SOFT-BLOCK).
