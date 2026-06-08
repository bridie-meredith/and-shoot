```yaml
audit:
  scope: chapter
  target: b01c03
  timestamp: 2026-05-26
  trigger: /and-review bones b01c03 — mandatory chunk→bones fidelity gate; cascade-budget compression chapter; primary independent check
  parts: [A-bone-gate-refire, B-chunk-fidelity, C-cold-read-prediction]

  summary:
    verdict: PASS-WITH-NOTES
    hard_count: 0
    signal_count: 3
    flag_count: 2
    fault_count: 0
    cold_read_prediction: |
      A cold reader recovers all five target elements with high confidence. Otto's
      intelligence-for-shielding terms are explicitly named by three dialogue bones
      across b01c03s02. The accuracy/weight signal (Sera real, coverage already
      running, refusal costs) is delivered through Taylor's analytical intake bones
      (s02n07, s02n09, s02n10) in visible parallel to the speech bones. Taylor's
      engagement-without-refusal is carried by s02n12's "I have heard you" and the
      silence-before-and-after; hinge legibility is very high — s03n04/s03n05/s03n06
      form an explicit three-bone beat anchoring the asking-for-a-day reading.
      Jarvis's courier-professional register (unremarkable, flat-affect, no menace)
      is established at bones s01n03, s02n03, s03n02, s03n07 — the pattern is
      unmistakable. No cold-read failures predicted; one coverage gap flagged below.

  findings:

    # ── PART A: BONE-GATE LOGIC RE-FIRE ──────────────────────────────────────────

    - id: fault-001
      type: pass
      what: "Part A-1 — Per-bone SVO discipline, all 36 flat bones"
      why: |
        All 36 flat-ID bones were walked for FAULT-FORM violations:
        copulas, conjunctions, modifiers beyond licensed compounds,
        perception verbs, interiority.
        — No copula-primary bones found. Bone 23 (s02 flat_id 23) uses "sits" but
          in a concrete locative sense ("the trade-shape sits between… in the
          tallow-damp air"), not a copulative predicate; this is the canonical
          licensed-image form, not a FAULT-FORM.
        — Bone 35 (s03 flat_id 35) uses "sit" similarly ("the open ledger line
          and the coverage map sit in the same place"); same determination.
        — No conjunction-primary bones found. No "but", "and", "because" leading
          the SVO.
        — Bone 25 uses "sits" in same locative register; same determination.
        — Perception verbs: no bare "noticed", "saw", "heard", "felt" as main
          verb. Bone 4 (s01 flat_id 4) uses "registers" but this is the feed
          acting as an instrument-object, not a bare POV perception — form is
          "taylor-hebert-kl-122ac's insect-feed registers"; SVO-compliant (subject
          is the feed, not Taylor bare).
        — Bone 17 (s02 flat_id 17) "registers the name and does not shift…" —
          the compound "registers and does not shift" is a disciplined-action
          double-verb; "registers" here is the analytical intake form established
          as the chapter's allowed verb for Taylor's tactical-processing bones;
          no interiority added; not a FAULT-FORM per the behavioral pattern.
        — All dialogue anchors use canonical "speaker-slug speaks to
          listener-slug" form: flat_ids 6, 8, 10, 11, 16, 18, 20, 24, 29, 31
          verified CLEAR.
        — No motivation clause found ("because", "in order to", "wanting to").
        — No bare interiority narration in bone SVO text. Internal states are
          conveyed through body-signal bones (flat 7: "goes still, weight on
          back foot"), location-of-stance bones (flat 14, 28, 33), and
          analytical-inventory bones (flat 19, 21, 22, 34, 35).
      why: No downstream consequence identified.

    - id: fault-002
      type: pass
      what: "Part A-2 — Per-scene axis-Δ check against contract targets"
      why: |
        s01 targets:
          social_tether-prot-rise +1.0: delivered at n08(+0.5) + n10(+0.5) = +1.0 EXACT
          social_tether-antag +0.5: delivered at n08(+0.5) = +0.5 EXACT
          position-prot-rise +0.5: delivered at n11(+0.5) = +0.5 EXACT
          moral_framework 0.0: held EXACT; no axis-move bones in s01
          capability 0.0: held EXACT
        s02 targets:
          social_tether-antag +1.0: delivered n04(+0.5) + n12(+0.5) = +1.0 EXACT
          moral_framework -0.5: delivered n11(-0.5) = -0.5 EXACT
          position-prot-rise 0.0: held EXACT
          social_tether-prot-rise 0.0: held (settled at s01) EXACT
        s03 targets:
          moral_framework -0.5: delivered n04(-0.5) = -0.5 EXACT
          position-prot-rise +0.5: delivered n06(+0.5) = +0.5 EXACT
          social_tether-antag 0.0: held (settled at s02) EXACT
          social_tether-prot-rise 0.0: held EXACT
        Chapter-level aggregates (from draft axis_delta_math_chapter_level):
          moral_framework: -1.0 (s02 + s03) vs chapter target -1.0 EXACT
          position-prot-rise: +1.0 (s01 + s03) vs chapter target +1.0 EXACT
          social_tether-antag: +1.5 (s01 + s02) vs chapter target +1.5 EXACT
          social_tether-prot-rise: +1.0 (s01 only) vs chapter target +1.0 EXACT
        All per-scene and chapter-level checks EXACT.
      why: No downstream consequence identified. All axis movement is math-clean.

    - id: signal-001
      type: flag
      what: "Part A-3 — Stakes-axis-dominant check, s02: social_tether-antag (+1.0) exceeds moral_framework (-0.5)"
      why: |
        s02 declares stakes_axis: moral_framework. Delivered moral_framework is -0.5.
        social_tether-antag delivers +1.0 in the same scene. The antagonist-tether
        magnitude is 2× the stakes-axis magnitude. Strictly, stakes-axis-dominant
        fails. However: the auditor dispatch instructions classify this as the
        canonical "stakes-axis-not-dominant-but-thesis-correct" pattern and tag it
        SIGNAL not HARD. The moral_framework move IS the chapter's hinge content
        (prohibition-becomes-variable at flat 23); the social_tether-antag magnitude
        is the leverage-fact required to make the moral_framework move credible and
        irreversible. The design is load-bearing, not incidental. No remediation
        required; surfaced for /and-facets awareness — the facet author should
        ensure the prohibition-as-variable bone (flat 23) is not crowded out by
        the leverage-delivery bones in the final prose.
      criteria: null

    - id: signal-002
      type: flag
      what: "Part A-3 — Stakes-axis-dominant check, s03: moral_framework (-0.5) tied with position-prot-rise (+0.5)"
      why: |
        s03 declares stakes_axis: moral_framework. Delivered moral_framework is -0.5;
        position-prot-rise is +0.5 — tied in magnitude. Tie at hinge resolution is
        not a strict dominance failure, but the /and-facets author should note that
        the hinge bone (flat 29: Taylor speaks asking for a day) carries both the
        moral_framework axis-move AND seeds the position-prot-rise move (which lands
        on flat 31: Jarvis's confirmation). If the rendered prose treats s03's
        resolution as primarily a position-gain beat (courier confirms return) rather
        than a moral_framework-crack beat (asking-for-a-day is the price-tag), the
        scene's declared stakes will read as mislabeled. Disposition: SIGNAL, not
        HARD. Awareness flag for stitching phase.
      criteria: null

    - id: fault-003
      type: pass
      what: "Part A-4 — Dialogue-coverage gate (HARD, URI-WRITE-DIALOGUE-COBONDED)"
      why: |
        10 dialogue-anchor bones identified: flat_ids 6, 8, 10, 11, 16, 18, 20, 24, 29, 31.
        Citation tokens in bones file:
          flat 6: [jarvis-coin-kl-courier:1] PRESENT
          flat 8: [jarvis-coin-kl-courier:2] PRESENT
          flat 10: [jarvis-coin-kl-courier:3] PRESENT
          flat 11: [taylor-hebert-kl-122ac:1] PRESENT
          flat 16: [jarvis-coin-kl-courier:4] PRESENT
          flat 18: [jarvis-coin-kl-courier:5] PRESENT
          flat 20: [jarvis-coin-kl-courier:6] PRESENT
          flat 24: [taylor-hebert-kl-122ac:2] PRESENT
          flat 29: [taylor-hebert-kl-122ac:3] PRESENT
          flat 31: [jarvis-coin-kl-courier:7] PRESENT
        All 10 dialogue-anchor bones carry citations. CLEAR.
        Dialogue files: jarvis-coin-kl-courier.md (7 entries verified); taylor-hebert-kl-122ac.md (3 entries verified). Both files non-empty. CLEAR.
        @anchor resolution:
          Jarvis entries @6, @8, @10, @16, @18, @20, @31 → flat_ids 6, 8, 10, 16, 18, 20, 31. All resolve. CLEAR.
          Taylor entries @11, @24, @29 → flat_ids 11, 24, 29. All resolve. CLEAR.
        Earth-Bet noun-fence scan on all 10 utterances and 10 speech objectives:
          — No Worm-canon proper nouns in any utterance or objective text. No
            cape-name self-reference. No parahuman jargon. Taylor's capability
            referenced as "insect-feed", "feed", "coverage", "insects" (SVO objectives
            only; dialogue text does not name the mechanism at all — Jarvis describes
            the behavioral shadow). CLEAR.
        All HARD dialogue-coverage criteria PASS.

    - id: fault-004
      type: pass
      what: "Part A-5 — Sensory-grounding check (HARD, ≥1 grounding bone per scene)"
      why: |
        s01 (flat 1-12): flat 1 (shoulder-to-shoulder foot-traffic, tallow-wax,
          fish-salt); flat 3 (salt-fish stall). Two sensory-grounding bones. PASS.
        s02 (flat 13-25): flat 13 (cooper's yard, Eel Alley, near shed, barrel-hoops,
          no-sightline-from-lane-mouth); flat 25 (tallow-damp). Two sensory-grounding
          bones. PASS.
        s03 (flat 26-36): flat 26 (same workers, same boy at hoop-stack, tallow-damp
          from lane-caulking). One sensory-grounding bone. PASS.
        All three scenes clear the ≥1 threshold.

    - id: signal-003
      type: flag
      what: "Part A-6 — Held-axes witnessing across all three scenes"
      why: |
        s01 contract axes_held: capability, moral_framework. Draft bones:
          capability held at n01 (no), n02, n04, n05, n09, n12 — WITNESSED.
          moral_framework held at n01, n05, n07 — WITNESSED.
        s02 contract axes_held: moral_framework (pre-crack). Draft bones:
          moral_framework held at n05 ("prohibition holds through the name-registration"),
          n07 ("prohibition is still operative; the calculation has opened but not
          cracked"), n10 ("accounting opens here; prohibition about to engage as
          calculation, not yet cracked") — WITNESSED. Note: n11 is the axis-mover
          bone for moral_framework in s02 (-0.5); bones n05, n07, n10 witness the
          held state prior to that movement. CLEAN.
        s03 contract axes_held: moral_framework (post-first-crack, pre-second).
          Draft bones: n03 ("prohibition price-tagging imminent; Taylor has not yet
          spoken"), n10 ("the moral framework crack is open, not yet licensed") — WITNESSED.
        relational_anchor_status appears as a held axis in s03n09 (Wren outside
          proposal calculus at rank 2) — this is a bonus witness, not required by
          the contract. No issue.
        No HELD-AXIS-NOT-WITNESSED faults. This chapter does not need the c02
          dormancy-pattern disposition. CLEAR.

    - id: fault-005
      type: flag
      what: "Part A — axis_correction_required flag in draft constraint_check (b01c03s02n06)"
      why: |
        The draft's constraint_check explicitly notes: "axis_correction_required: YES
        — b01c03s02n06 must have axis_moves set to [] before Phase 2 (over-count
        correction noted inline)." Bone b01c03s02n06 (flat_id 18, Jarvis delivers
        intelligence terms speech) in the draft has axes_held with social_tether-antag
        at held-status — the draft author had an earlier version where n06 carried a
        partial axis-move and corrected it inline, but did not confirm the correction
        was committed to the flat bones file. Checking the flat bones file (b01-c03.md
        line 31): flat_id 18 reads "jarvis-coin-kl-courier speaks to
        taylor-hebert-kl-122ac [jarvis-coin-kl-courier:5]" — it carries no axis-move
        annotation in the flat file (flat file does not embed axis-move detail). The
        over-count risk is in the draft only. However, the draft is the source of truth
        for the bone-gate. Per the draft, b01c03s02n06's axis_moves = [] with
        social_tether-antag in axes_held — this is the corrected state. The inline
        note says the axis-mover was moved to n12 (Taylor's acknowledgment), and the
        axis_aggregate_check for s02 confirms the +1.0 social_tether-antag is
        delivered at n04 + n12 with n06 contributing zero. No over-count survives.
        The correction_required flag is self-resolved within the draft.
        Classification: FLAG (administrative; Phase 2 should verify the draft's
        inline correction was not accidentally reverted; no HARD finding).
      criteria: null

    # ── PART B: CHUNK-TAG FIDELITY ───────────────────────────────────────────────

    - id: fault-006
      type: pass
      what: "Part B — s01 chunk-tag coverage"
      why: |
        [force: Taylor's street-discipline in the open market] →
          event_map covering_bones: s01n02, s01n04, s01n05. Bones present in flat file
          at flat_ids 2, 4, 5. Multi-bone coverage of the discipline-in-the-market
          force. COVERED.
        [event: Jarvis Coin addresses Taylor by the description of what she did at the rescue] →
          event_map: s01n06. flat_id 6. Dialogue bone with speech_objective naming the
          rescue-at-Butcher's-Lane description. COVERED.
        [image: Jarvis Coin — unremarkable in the crowd, stillness of someone who has waited] →
          event_map: s01n03. flat_id 3. Grounding bone with "hands at his sides, eyes on
          taylor-hebert-kl-122ac before she has registered him." COVERED.
        [mechanism: Jarvis names the scope and shape of Taylor's insect-feed deployment] →
          event_map: s01n08. flat_id 8. Speech bone with objective naming the coverage
          pattern (behavioral shadow). COVERED.
        [force: the precision of address as the leverage being demonstrated] →
          event_map: s01n08. Same bone — accuracy is the leverage. COVERED.
        [event: Taylor recognizes she has been under observation] →
          event_map: s01n07. flat_id 7. Body-signal bone ("goes still, weight on back
          foot, both hands visible"). COVERED.
        [event: social_tether-prot-rise account completes cl01b court-layer half] →
          event_map: s01n10. flat_id 10. Speech bone with objective naming the
          patron-existence statement completing the tether's second floor. COVERED.
        [mechanism: Taylor agrees to a location and time before she has decided whether to attend] →
          event_map: s01n11. flat_id 11. Taylor's dialogue bone, speech objective
          "agree to the location and time; eyes on the stall beyond him, not on him;
          confirm without signaling whether she will attend." Dialogue text: "The
          cooper's yard. Third bell." COVERED.
        All 8 s01 chunk-tags: COVERED.

    - id: fault-007
      type: pass
      what: "Part B — s02 chunk-tag coverage"
      why: |
        [force: Taylor's discipline of arriving early] →
          event_map: s02n02. flat_id 14. "reaches the yard before jarvis-coin-kl-courier,
          back to the shed wall." COVERED.
        [event: Jarvis names Otto Hightower as the patron] →
          event_map: s02n04. flat_id 16. Speech bone; dialogue text: "Otto Hightower.
          The Hand who was. The man who still runs the channels the Small Council does
          not audit." COVERED.
        [mechanism: Jarvis delivers the intelligence terms] →
          event_map: s02n06. flat_id 18. Speech bone with objective naming ward-movement
          patterns, sickness clustering, junction agitation reads. COVERED.
        [event: Jarvis names Sera Hightower and the succession exposure] →
          event_map: s02n08. flat_id 20. Speech bone; dialogue text names Sera, the
          ward-placement in Queen Consort's household, the legitimacy question, and
          shielding. COVERED.
        [force: the proposal's accuracy as the opposing pressure] →
          event_map: s02n09, s02n10. flat_ids 21, 22. Dual-track accounting bones
          (ward-workers by feed + mapping Sera-ward against existing coverage). COVERED.
        [image: the prohibition as a variable in a calculation] →
          event_map: s02n11. flat_id 23. "the prohibition engages in
          taylor-hebert-kl-122ac's accounting as a term on one side of a ledger where
          the other side has a named cost attached to refusal." COVERED.
        [event: Taylor acknowledges she has understood the terms] →
          event_map: s02n12. flat_id 24. Dialogue: "I have heard you." COVERED.
        [mechanism: moral_framework engages the prohibition as a calculation rather than a fence] →
          event_map: s02n11. Same bone as the image. COVERED.
        [event: social_tether-antag full leverage articulated] →
          event_map: s02n12, s02n13. flat_ids 24, 25. Acknowledgment + trade-shape
          closure. COVERED.
        All 9 s02 chunk-tags: COVERED.

    - id: fault-008
      type: pass
      what: "Part B — s03 chunk-tag coverage"
      why: |
        [force: Taylor's discipline of not-deciding-under-pressure] →
          event_map: s03n02, s03n03. flat_ids 27, 28. Jarvis's stillness as pressure +
          Taylor's posture-held. COVERED.
        [event: Taylor asks for a day] →
          event_map: s03n04. flat_id 29. Dialogue: "A day." COVERED.
        [image: the beat in which a courier registers that the answer was not refusal] →
          event_map: s03n05. flat_id 30. "jarvis-coin-kl-courier considers
          taylor-hebert-kl-122ac for a beat — the beat in which a courier registers
          that the answer was not refusal." Bone text directly quotes the chunk tag.
          COVERED.
        [mechanism: the act of asking for a day as engagement rather than refusal] →
          event_map: s03n06. flat_id 31. Speech bone; Jarvis accepts the day (confirms
          return), registering Taylor as decision-pending. COVERED.
        [event: moral_framework prohibition price-tagged for the first time] →
          event_map: s03n04. flat_id 29. Same bone as day-request — asking IS the
          price-tag. COVERED.
        [force: the chapter's hinge — asking for a day IS the engagement] →
          event_map: s03n04, s03n08. flat_ids 29, 33. Verbal hinge + physical-hinge
          (Taylor holds position after Jarvis departs). COVERED.
        [event: Taylor does the accounting before she leaves the yard] →
          event_map: s03n09. flat_id 34. "runs the coverage of Rhaenys's Hill
          ward-traffic against the boy at the hoop-stack." COVERED.
        [event: position-prot-rise registers Taylor's response as decision-pending] →
          event_map: s03n06. flat_id 31. Jarvis-confirms-return bone carries
          position-prot-rise axis-move. COVERED.
        [image: the coverage map and the open ledger line as the same thing] →
          event_map: s03n10. flat_id 35. "the open ledger line and the coverage map
          sit in the same place in taylor-hebert-kl-122ac's accounting, requiring the
          same answer." COVERED.
        All 9 s03 chunk-tags: COVERED.

    - id: fault-009
      type: flag
      what: "Part B — s03 hinge: 'refusal-as-form no longer available' tag not explicitly covered"
      why: |
        The s03 chunk includes the sub-tag text: "the deferral IS the engagement;
        refusal-as-form no longer available; ledger cannot un-open." The event_map
        does not list "refusal-as-form no longer available" as a named tag with a
        dedicated covering bone. The closest candidates are s03n04 (day-request is
        engagement) and s03n10 (ledger-cannot-un-open as the coverage-map-sameness
        bone). s03n10's notes say "the gap between now-doing-it and naming-it-to-
        someone-else" which carries the ledger-cannot-un-open reading implicitly.
        However, "refusal-as-form no longer available" is the irrevocability element
        — the chapter hinge's second clause — and no bone directly articulates the
        foreclosure of the refusal form (as distinct from simply not-refusing). At
        stitching, if the prose uses s03n04 and s03n10 alone, a reader might register
        the asking-for-a-day as deferral-pending rather than irrevocable engagement.
        The distinction is load-bearing for the b01c04 acceptance reading as "a
        decision she reached" vs "a capitulation." Classification: FLAG (not HARD —
        the irrevocability is implied by the combined bones, but the implication is
        thin). The /and-facets author should ensure the sensory/feeling facets weight
        s03n10 as the closure bone, not merely as accounting-notation.
      criteria: null

    # ── PART C: COLD-READ PREDICTION ────────────────────────────────────────────

    - id: fault-010
      type: pass
      what: "Part C — Cold-read prediction: all five target elements"
      why: |
        TARGET 1 — Otto's proposal terms (intelligence-for-shielding):
          Covered by s02 flat_ids 16 (Otto named), 18 (intelligence terms named:
          ward-movement, sickness-clustering, junction reads), 20 (Sera + succession
          exposure + shielding available). The three-bone delivery of the terms is
          explicit and sequenced. A cold reader will recover this cleanly.
          Confidence: HIGH.

        TARGET 2 — Accuracy/weight (Sera real, coverage real, refusal costs):
          Covered by flat_ids 21 and 22 (Taylor's dual-track accounting: feed
          running on yard-workers while mapping Sera-ward against existing coverage)
          and flat_id 23 (prohibition-as-ledger-term with named cost attached to
          refusal). The cost-of-refusal element is carried in the bone's text as
          "the other side has a named cost attached to refusal" — Sera's exposure
          as the cost is readable from context (Jarvis's dialogue at flat 20 named
          the mechanism of surfacing). Cold reader recovers this. Confidence: HIGH.

        TARGET 3 — Taylor's engagement without refusal (acknowledged having heard):
          Carried by flat_id 24 ("I have heard you") and the surrounding silence
          bones (flat 17: does not shift weight or eyes; flat 25: no answer yet,
          but trade-shape exists). The "neither yes nor no" form is unambiguous.
          Cold reader recovers engagement-without-refusal. Confidence: HIGH.

        TARGET 4 — The hinge (asking for a day = engagement):
          Three-bone sequence flat_ids 29-30-31 is the clearest structured beat in
          the chapter. flat_id 30 names the register explicitly ("the beat in which
          a courier registers that the answer was not refusal"). The hinge is
          on-the-surface; no cold-read inference required. Confidence: HIGH.

        TARGET 5 — Jarvis as professional courier (not menacing; effective because unremarkable):
          Established across flat_id 3 (eyes on her before she registered him —
          unremarkable at a stall), flat_id 9 (the distance is the distance of a
          street-side negotiation — unremarkable to anyone passing), flat_id 15
          (no document, no letter, no seal), flat_id 27 (stands without adding to
          the proposal, waiting), flat_id 32 (leaves with the same unhurried pace
          he arrived with). Five bones across three scenes establish the
          flat-professional register. The word "menacing" does not appear anywhere
          in the bones, and no bone creates a threat-pressure framing. Confidence: HIGH.

        NOTED RISK (from flag fault-009): refusal-as-form-no-longer-available is
          the one element a cold reader might not recover with certainty. The
          chapter goal ("Taylor engaging rather than refusing, so the acceptance
          in b01c04 reads as a decision she reached, not a capitulation") depends
          on the irrevocability reading landing. If the stitcher treats s03n10
          as background accounting rather than closure, this target weakens.
          Not a cold-read failure at the bone level — flagged for /and-facets.
```
