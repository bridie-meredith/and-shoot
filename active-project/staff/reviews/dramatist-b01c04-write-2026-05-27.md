```yaml
dramatist-shape-review:
  scope: chapter b01c04
  timestamp: 2026-05-27
  trigger: /and-write b01c04 Phase 3 — shape review on constraint-clean 33-bone redo

  per-scene:

    b01c04s01:
      bone_order: ORDER-OK
      missing_transitions: []
      speech_form_check: PASS
        # s01n06: "taylor-hebert-kl-122ac speaks to jarvis-coin-kl-courier" — conforming
        # s01n08: "jarvis-coin-kl-courier speaks to taylor-hebert-kl-122ac" — conforming
        # No other dialogue_anchor: true bones in this scene
      shape_assessment: >
        s01 has correct rise-and-close shape for an opening scene. The sensory approach (n01–n04)
        establishes the yard as a fixed coordinate; n05 (feed-priority-over-eye) enacts the
        courier-tier register before the exchange opens. The stakes event lands at n06 (Taylor
        speaks the yes — social_tether-antag +1.0) with cost registered immediately at n07
        (moral_framework held — the irreversibility is felt and enacted without narration).
        Jarvis's reply at n08 (position-prot-rise +1.0) solidifies the lever as routing-
        confirmation rather than extracted concession — the power asymmetry is correctly placed:
        his speech advances position, not hers. The departure pair (n09/n10) closes the scene
        with the lever walking out and the relational anchor held clean. The axis consolidation
        (both moving bones at +1.0 each) prevents the prior-draft split-momentum problem. The
        scene opens the chapter's rise correctly: acceptance is irreversible, leverage is
        operational, the architecture is live.

    b01c04s02:
      bone_order: ORDER-OK
      missing_transitions: []
      speech_form_check: PASS
        # s02: no dialogue_anchor: true bones — silent scene, conforming
      shape_assessment: >
        s02 carries the chapter's accumulation correctly. The Pig Tallow Lane opening (n01–n04)
        establishes the walk-and-read discipline as procedural — extension-as-addition, not
        transformation — which sets the moral_legibility_to_self hold without narrating the
        rationalization's content. The Oswyn sequence (n05–n07) is the scene's pressure point:
        the penny-a-barrel carter grounds the crowd before the feed returns Oswyn (n06,
        social_tether-prot-rise +1.0), and the mapping bone (n07) enacts the unknowing-node
        routing as moral_framework hold without naming it as such. The scene then correctly
        moves to the second ward via a new sensory grounding bone (n08, stitch-house frames)
        before the Wren pair (n09–n10). The two-bone Wren treatment is correctly sequenced:
        feed returns Wren (n09, relational_anchor_status held — she is in coverage), then
        feet held (n10, relational_anchor_status held — she is not walked toward). The final
        mapping bone (n11, moral_legibility_to_self held — the ledger-distinction is maintained
        without examination) closes the scene on the correct note: the pressure has accumulated
        without releasing. Stakes trajectory across the scene is rising: Ward 1 expansion (n03)
        → Oswyn enters the architecture (n06) → Wren is in coverage but outside the ledger
        (n09–n10). The opposition (n06, n07 — Oswyn becomes coverage substrate without knowing)
        costs something legible to the audience even as Taylor does not name it. No inert stretch.

    b01c04s03:
      bone_order: ORDER-OK
      missing_transitions: []
      speech_form_check: PASS
        # s03: no `speaks to` form bones
        # n07 (taylor-hebert-kl-122ac delivers the report-sheet): physical action + communication-class
        #   axis_move (social_tether-prot-rise +1.0) — licensed action form per schema; not a speech bone
        # n06 (jarvis-coin-kl-courier displays the note): physical gesture; no axis_move; chatter form;
        #   no speech-class issue
        # n09 (jarvis-coin-kl-courier exits the cooper's yard): physical departure + position-world +1.0;
        #   licensed action form; not a speech bone
        # All correct
      shape_assessment: >
        s03 lands the chapter's peak and delivers the thesis structurally. The sequence correctly
        opens with the third-ward completion (n01–n04: Roper's Court → Taylor enters → insect-range
        extends → four-ward feed running), which gives capability its second +1.0 and closes the
        coverage arc. The return to the cooper's yard (n05–n09) is the scene's decisive cluster:
        Jarvis enters (n05), displays the confirmation note without handing it over (n06 — power
        asymmetry correctly enacted: Otto's side controls access to the proof), Taylor delivers
        the report-sheet (n07, social_tether-prot-rise +1.0), Jarvis pockets it (n08), and Jarvis
        exits with position-world +1.0 (n09 — the intelligence's departure is the world-axis
        event). The sequencing of Sera-confirmation-before-report-delivery is dramatically correct:
        Taylor receives the protection dividend first, then hands the report across. This ordering
        shows the exchange is operational rather than coerced — the lever has already paid its first
        dividend at the moment of delivery, so the handoff reads as part of the working architecture,
        not a reluctant payment. The closing quadruple (n10–n12 + the Wren anchor pair) enacts the
        chapter goal: Taylor runs the ward-feed (n10, moral_legibility_to_self held — the continuous
        operation is indivisible), the feed returns Wren (n11, relational_anchor_status held — anchor
        discipline in feed-behavior), Taylor exits the stitch-house lane without examining whether
        the anchor will hold (n12, moral_legibility_to_self held — non-examination enacted physically).
        The audience sees the gap the calculus does not name. No inert stretch. Peak is correctly
        located: the report-handoff sequence (n07–n09) is the moment the architecture becomes
        functional rather than potential. The chapter closes without deflating: the ward-feed
        running and Wren passing through is not resolution — it is the architecture operating.

  chapter-level:

    rising_shape_conformance: PASS
      # s01 closes the acceptance + opens leverage: social_tether-antag +1.0 (lever operational)
      #   + position-prot-rise +1.0 (Taylor is now a named conduit). Rise begins.
      # s02 deepens through expansion: capability +1.0 (two wards covered), social_tether-prot-rise
      #   +1.0 (Oswyn enters as unknowing node). Pressure accumulates: Wren is visible-but-untouched.
      # s03 lands the architecture-running thesis: capability +1.0 (four-ward complete),
      #   social_tether-prot-rise +1.0 (Jarvis structural vector confirmed), position-world +1.0
      #   (intelligence exits into Otto's channel). The Wren anchor-held-but-unexamined close is
      #   the chapter's structural irony — protection and trap as same operation visible to audience,
      #   not to Taylor. Escalation verified at each scene boundary. Axes accumulate; no axis moves
      #   in reverse; no held-axis collapses without a declared Δ. Rising shape confirmed.

    goal_landing: PASS
      # Chapter goal: "Show the audience the acceptance and the network expansion together so the
      #   tether-gain reads as future-cost collateral — the protection and the trap are the same
      #   operation."
      # Lever solidifies in s01 (social_tether-antag +1.0 + position-prot-rise +1.0): Taylor is
      #   now a named function; the lever is operational; the yes is irreversible.
      # Network builds with named human cost in s02 (Oswyn, unknowing node): the expansion
      #   carries a face and a moral-framework hold. Wren is in coverage, not in the report —
      #   the audience sees the asymmetry Taylor does not name.
      # Upward routing makes the trap visible-to-audience-not-Taylor in s03: the report exits
      #   Taylor's context (n09, position-world +1.0), Taylor runs the four-ward feed continuously
      #   (n10), Wren passes through and does not enter the ledger (n11–n12). The indivisibility
      #   of the operation (reading-and-routing collapse) is enacted without the thesis being
      #   spoken. The protection-and-trap thesis is present in structure, not in language —
      #   theme-silence watch correctly honored throughout. Goal landing confirmed.

    summary: >
      The 33-bone chapter has rise-peak-fall shape across its three scenes: acceptance solidifies
      the lever (s01), expansion builds the architecture with human cost (s02), and the first
      report delivery confirms the architecture as functional rather than potential (s03). The
      chapter's structural irony — Wren in coverage, outside the ledger, anchor held without
      examination — is carried by the bones' held-axis pattern without being stated as thesis.
      The opposing force is consistently load-bearing: Jarvis's routing-confirmation takes the yes
      as operational fact (s01), Oswyn enters the architecture without knowledge or choice (s02),
      and the intelligence exits into Otto's channel before Taylor turns for home (s03). End state
      is materially different from start state on five axes. Try-fail mechanics are not applicable
      at this chapter (no failed attempt cycle); the chapter is a one-way door, which is the
      correct shape for an acceptance chapter — the cost is not in repeated failure but in the
      irreversibility of each step.

  verdict: ACCEPT
```
