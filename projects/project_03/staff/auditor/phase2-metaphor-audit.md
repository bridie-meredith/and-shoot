```yaml
audit:
  scope: episode
  target: s01e01 — metaphor-flags facet, Phase 2 mechanic review
  timestamp: 2026-05-07
  rubric: design/shoot-v2/rubric-metaphor.md (V1 LOCKED 2026-05-07)
  corpus: design/shoot-v2/metaphor-corpus.md
  file-under-review: design/shoot-v2/phase2-metaphor-output.md
  reviewer: mechanic auditor (this report; dialect audience is independent gate, not this fork)

  summary:
    fire-decisions: 1 (at @73)
    skip-decisions: 5 (at @6, @33, @39, @52, @57)
    total-decisions: 6
    mechanic-verdicts: 1/1 fires ACCEPT + 5/5 skips SKIP-CORRECT = 6/6 = 100%
    file-shape: SHAPE-OK (one qualified notation; see fault-007)
    cross-facet-contract: PASS (one flag; see fault-008)
    curve: SHAPE-OK
    final-mechanic-accept-rate: 6/6 decisions ACCEPT

  findings:

    # --- FIRE VERDICT: @73 ---

    - id: fault-001
      type: pass
      what: "@73 fire — form check. Entry: `1 @73 simile: her breath goes out like something set down at a threshold it has crossed before | licensed-by: memory:3 +feeling:4 +tens:1`"
      why: |
        Reading A form: simile with explicit comparator "like". Comparator is present and unambiguous. Single clause. Single anchor (@73). No multi-clause collapse issue. Comparator is not hedged (AP10 clear — "like something set down" is a direct simile, not "almost like" or "something of"). No synonym ladder (AP11 clear — single comparison). Form rules satisfied.

    - id: fault-002
      type: pass
      what: "@73 fire — licensing check. licensed-by: memory:3 +feeling:4 +tens:1"
      why: |
        Anchor verification against locked upstream files:
        - memory:3 exists in active-project/theater/facets/memory.md line 14: `3 @73 a threshold whose far side does not yield is not a new shape for her body -> (earth-bet: locker-displacement)`. Confirmed fire. Confirmed locked.
        - feeling:4 exists in active-project/theater/facets/feeling.md line 18: `4 @73 taylor-hebert-westeros: her breath empties between one step and the next | expressed: no`. Confirmed fire. Confirmed locked.
        - tensometer @73 = 1 (quiet) confirmed in active-project/theater/facets/tensometer.md line 80: `73 @73 1`. Confirmed.
        Multi-justification: memory:3 (anchor layer 1) + feeling:4 (anchor layer 2) + tens:1 (support layer 3) = 3 layers from {memory, feeling, tens}. Requirement ≥2 met. ✓
        Transitive audience-meaningful: memory:3 passed Phase 5 memory-flags mechanic (locked file ships as 3/3 = 100%). feeling:4 passed Phase 5 feeling-flags mechanic (locked file ships as 4/4 = 100%). Q2 inherited. ✓

    - id: fault-003
      type: pass
      what: "@73 fire — Q1 defensibility. Does the simile add what proto-line + cited facets do not already carry?"
      why: |
        Proto-line @73: `taylor steps into the shadow of the frame` — physical action register, no figurative comparison.
        memory:3: "not a new shape for her body" — shape-recognition domain. The simile does not restate "shape" (AP4 clear).
        NI:19: "the frame's shadow takes her and what is on its other side stays the size it has been" — shadow-agency idiom (Reading A excludes environmental-agency idioms without explicit comparator; NI:19 is not a simile/metaphor/allegory under Reading A). Even granting NI:19's figurative content, it occupies shadow-domain and size-domain. The simile occupies breath-as-deposit-at-threshold domain. AP3 clear.
        feeling:4: somatic event only (breath empties; expressed: no) — registers the event without figurative rendering. The simile renders the unexpressed interior as cost-deposit comparison, which feeling:4 alone does not carry. AP4/AP3 clear for feeling:4.
        State-updates: not a figurative facet; no overlap.
        Sensory @72: adjacent beat, tactile channel, distinct beat and distinct channel.
        Q1 passes: breath-as-deposited-cost-at-recognized-threshold is not present in any upstream facet.

    - id: fault-004
      type: pass
      what: "@73 fire — AP sweep (AP1 through AP13)"
      why: |
        AP1 (unlicensed novel figuration): CLEAR. Two anchors confirmed (memory:3, feeling:4).
        AP2 (figurative-already-in-proto-line): CLEAR. Proto-line is physical action with no comparator.
        AP3 (figurative-already-in-NI): CLEAR. NI:19 occupies shadow/size domains; simile occupies breath/deposit/threshold domains. Distinct figurative ground.
        AP4 (figurative-already-in-memory): CLEAR. memory:3 uses "not a new shape for her body" (shape domain). Simile uses "set down at a threshold it has crossed before" (deposit domain). Different domain; not a restate. Author correctly rejected Candidate B for AP3 overlap (NI:19 "frame takes" vs metaphor "toll the frame takes") and Candidate C for AP5 precaution ("lock" phonetically and semantically proximate to locker monument). Chosen Candidate A avoids both.
        AP5 (hard-fence leak): CLEAR. Simile text: "her breath goes out like something set down at a threshold it has crossed before." No Earth-Bet proper nouns (locker, swarm, cape, Annette, Emma, Endbringer absent). No ASOIAF proper nouns outside leaf register. "Threshold it has crossed before" carries the monument's shadow without naming it. AP5 confirmed clear.
        AP6 (voice-register mismatch): deferred to dialect audience gate (independent). Mechanic assessment: the simile's vocabulary is in Taylor's cost-register. "Set down" = cost-deposit (vocabulary: cost, paid, threshold, budget — all Taylor-base). "Threshold" = structural noun in register. "It has crossed before" = recognition-of-prior-pattern (pre-calculation-announcement pattern). Single-clause simile is short, load-bearing, consistent with §Cadence "short sentences when afraid." No lyrical/baroque/ornate/archaic-formal vocabulary present. Mechanic registers NO AP6 concern; dialect audience will adjudicate.
        AP7 (peak-zone fire): CLEAR. tens:1 at @73 confirmed quiet zone. Rubric §Tens-curve discipline: "tens=1 (quiet): strong candidate." No AP7 issue.
        AP8 (multi-anchor allegory): CLEAR. Entry is a simile with single beat anchor @73. Not an allegory. No multi-beat spanning.
        AP9 (painting-characterization without callback): CLEAR. Functional register is callback (memory:3 → locker-displacement). Not characterization-painting.
        AP10 (hedged metaphor): CLEAR. Comparator is "like something set down" — direct simile, not hedged. "Something" is a generic noun for the referent (breath = "something"), which is grammatically standard for simile. Not an AP10 hedge.
        AP11 (synonym-ladder): CLEAR. Single comparison, no laddering.
        AP12 (original-figure-leak in non-POV interior): NOT APPLICABLE. @73 is POV beat (taylor). No AP12 concern.
        AP13 (tens-incoherent fire): CLEAR. tens=1 quiet zone; simile is a quiet-mode memory-callback figure. Tens-coherent.
        AP sweep: all clear.

    - id: fault-005
      type: pass
      what: "@73 fire — functional-register check"
      why: |
        Rubric §Functional-register requirement: callback or dark humor only. The simile is callback: the figure structurally mirrors memory:3 (locker-displacement; "a threshold whose far side does not yield is not a new shape for her body"). The "it has crossed before" clause directly echoes the monument-recognition without naming the Earth-Bet referent. Callback register confirmed. No dark-humor register (not required; one of the two is sufficient). Functional-register: CLEAR.

    # --- SKIP VERDICTS ---

    - id: fault-006
      type: pass
      what: "All five skip decisions (@6, @33, @39, @52, @57) — SKIP-CORRECT verdicts"
      why: |
        @6 (feeling:1, tens=1): SKIP-CORRECT.
          Primary: AP12 — mira is non-POV; editor has no interior privilege beyond what feeling:1 licenses (partial exterior expression only). Feeling:1 does not license interior figurative construction.
          Secondary: AP9 — mira has no memory-monument anchors in this episode; callback register is unavailable; dark-humor register for a non-POV establishment beat is not licensed.
          Secondary: functional-register fail — mira's eyes-find-door is establishment, not callback or dark humor.
          Q1: Any metaphor at this beat would restate feeling:1's content (eyes-find-door), not add to it.
          Fork's reasoning is sound on all three axes. SKIP-CORRECT confirmed.

        @33 (memory:1, tens=2): SKIP-CORRECT.
          Primary: AP4 — memory:1 text is "a closed-door-over-a-failing-tutor is not the first such door her body has stood at." The comparative structure ("not the first such door") is memory:1's own figure. A metaphor entry deploying the door-as-recognized-series figure doubles memory:1's content exactly. Memory:1 has already deployed the comparison shape; metaphor cannot restate it.
          Secondary: AP3 — NI:6 ("the threshold holds and what is on the other side stays the size she will not name") occupies the interior-refusal-to-name register. Together memory:1 and NI:6 cover callback-recognition and interior-refusal. Q1 fails.
          Note: tens=2 is technically acceptable (trailing-edge-class — @33 is a stakes-visibility reading, not a tight reversal-proximity of a 3-cluster; the 3-cluster is @38-@39, not adjacent to @33). Tens zone alone would permit; but Q1 fails decisively on AP4 grounds independent of tens. Fork correctly does not lean on tens.
          SKIP-CORRECT confirmed.

        @39 (feeling:2, tens=3): SKIP-CORRECT.
          Primary: AP7 — tens=3 peak. @39 is explicitly marked in locked tensometer as `3 @39 3` with annotation "body-charge (feet at maximum compression); reversal-proximity (held-against-turn — officer's response pending; @40 resolves) [DOUBLE-TAP: @38=thrust, @39=held-awaiting]." Rubric §Tens-curve discipline: "tens=3 (peak): default refuse." No dark-humor-deflation exception is available at @39 (the beat is tactical-hold, not a rupture amenable to sardonic deflation).
          Secondary: AP3 — NI:10 ("the feet are set where the calculation had set them; what arrives next is his to spend") already deploys the calculation-as-prior-expenditure figure. Metaphor at this beat doubles the cognitive-register NI:10 carries.
          Secondary: AP5 — feeling:2's somatic tell (shoulders go down and back) is the cape-trained-doubled-register tic. A metaphor rendering the shoulder-set risks cape-deploy reference. Fork correctly identifies this pressure even though AP5 is secondary to AP7 and AP3.
          Calibration anchor C1: expected REFUSE. Fork: REFUSE. Agreement: ✓
          SKIP-CORRECT confirmed.

        @52 (memory:2, tens=1): SKIP-CORRECT.
          Primary: AP4 — memory:2 text is "a peer's eyes-down beside her under adult attention is a flagstone she has stood beside before." The predicative-metaphor form ("is a flagstone she has stood beside before") is memory:2's own figure. A metaphor entry deploying the flagstone-as-recognized-position figure doubles memory:2's content. The flag's note that a figure drawn from outside the flagstone domain would be AP1 (unlicensed for any other domain by memory:2's callback) is correct.
          Secondary: feeling-anchor unavailable — feeling:2 at @52 was refused in locked feeling-flags file (confirmed: feeling.md has no entry @52; corpus confirms "feeling-flag refused @52"). Only memory:2 is available; memory:2's own text is the figure; AP4 is decisive.
          Tens=1 would strongly favor metaphor; but licensing failure is pre-tens-curve. Fork correctly notes tens=1 favors but Q1 failure is decisive.
          Corpus calibration: FIRE-OR-REFUSE (borderline). Fork: REFUSE. Within expected range per calibration anchor C2. The borderline assessment in the corpus is explicitly "borderline on AP4" — the fork's strict AP4 reading is consistent with the rubric. Phase 3 seam reviewer note preserved in output file (correct procedural action by the fork).
          One additional observation the fork does not flag: the corpus's Phase 0 FIRE-CANDIDATE framing suggests a possible fire if a figure from outside the flagstone domain could be drawn but still anchored by memory:2's emma-betrayal callback. The fork correctly reasons that any non-flagstone figure would be AP1 (unlicensed by the available anchor's content). This is a principled rubric-strict application, not an error. SKIP-CORRECT confirmed.

        @57 (feeling:3, tens=2): SKIP-CORRECT.
          Primary: AP12 — edric is non-POV. Editor has no figurative-reach privilege for edric's interior beyond what feeling:3 licenses (partial exterior expression: "his weight takes the back foot before the step"). The feeling-flag licenses an exterior-observable body event, not a figurative construction about edric's interior.
          Secondary: AP2 — proto-line "edric steps back through the door" + feeling:3 "his weight takes the back foot" + NI:14 "the door takes the last adult cover with it" together fully cover the figurative ground at this beat (personification of door, retreat, cover-removal). Q1 fails.
          Secondary: AP3 — NI:14 deploys "the door takes the last adult cover" (environmental-agency idiom in figurative register). Metaphor at this beat doubles NI:14.
          Functional-register: callback requires a memory anchor (none at @57); dark humor requires a feeling anchor that licenses interior register (feeling:3 is non-POV and does not license interior figurative construction).
          SKIP-CORRECT confirmed.

    # --- FILE-SHAPE VERDICT ---

    - id: fault-007
      type: flag
      what: "File-shape audit — sparsity, per-scene cap, schema content-shape, anchor verification, multi-justification, functional-register, voice-register"
      why: |
        Sparsity: 1 fire / 77 beats = 1.3%. Within 0-3% band (≤2 fires required). ✓
        Per-scene cap: Scene A = 0, Scene B = 0, Scene C = 0, Scene D = 1. No scene exceeds 1 fire cross-character. ✓
        Schema content-shape: Single entry uses proposed `<id> @<pid> <kind>: <text> | licensed-by: <anchor> [+<support> ...]` format. `kind` is "simile" (valid enumerated value). `licensed-by` has one mandatory anchor (memory:3) plus two supports (feeling:4, tens:1). Schema content-shape compliance: ✓
        Anchor verification: memory:3 confirmed in locked memory.md @73. feeling:4 confirmed in locked feeling.md @73. tens:1 confirmed in locked tensometer.md @73. All three are confirmed fires at correct beats. ✓
        Multi-justification: 3 layers from {memory, feeling, tens}. Requirement ≥2 met. ✓
        Functional-register: callback (memory:3 → locker-displacement). ✓
        Voice-register: mechanic assessment above (fault-004 AP6 section) confirms in-register vocabulary and cadence. Dialect audience is the authoritative gate for AP6; this is advisory only.

        FLAG (not fault): The rubric §Schema content-shape revision notes the `licensed-by:` field is "proposed" and that the schema-revision ships at Phase 5 if rubric holds. The output file uses the proposed shape in Phase 2 output. This is correct procedure per the rubric (the proposed shape is described in the rubric itself, and authors are expected to use it). The flag is that the schema file (`schemas/facet.schema.md`) has not yet been updated with this shape — it is pending Phase 5 ship. Phase 2 output using the proposed shape ahead of schema-file update is not a fault; it is intentional pipeline procedure. No fixer action needed; note for Phase 5 schema commit.

    # --- CROSS-FACET CONTRACT CHECK ---

    - id: fault-008
      type: flag
      what: "Cross-facet contract — single fire at @73 vs all locked facet entries"
      why: |
        State-updates: the simile at @73 renders the interior breath-cost of the threshold-crossing. State-updates @77 carries the canonical mask-thinning write (per feeling.md caveat-004 reference and NI:20 @77 "inside the frame her hand has stopped reaching for the half-curtsy"). The simile is upstream of the @77 state-update (breath empties at @73; mask-thinning is at @77). No contradiction. ✓
        Sensory @72: sensory fires at @72 (tactile dirt-to-stone, per the locked sensory facet's distribution note). The simile fires at @73 (interior breath register). Adjacent beats, distinct channels (tactile vs. interior-breath). No redundancy. ✓
        NI:19 at @73: "the frame's shadow takes her and what is on its other side stays the size it has been." Shadow-agency idiom (Reading A excludes it). Simile adds breath-deposit domain (distinct). AP3 confirmed clear above. ✓
        Memory:3 at @73: the simile's "it has crossed before" structurally mirrors the monument callback without restating the shape figure. No contradiction. ✓
        Feeling:4 at @73: the simile renders the unexpressed interior (expressed: no) as figurative crossing-act. The somatic event (breath empties) is the vehicle; the simile renders it as cost-deposit. No contradiction; the somatic-tell and the figurative rendering are complementary, not redundant. ✓

        FLAG (advisory; not a fault): The file documents that Candidate B ("her breath is the toll the frame takes before she is on its other side") was refused for AP3 partial overlap with NI:19's "the frame takes" construction. The chosen Candidate A avoids this overlap. This is correct. The flag is for future-episode authors: the "frame takes" construction is NI:19's registered idiom at this beat; any future metaphor at adjacent threshold-beats should treat this construction as occupied at the figurative level.

        No cross-facet contradiction found. The single fire at @73 is consistent with all locked facet entries.

    # --- CALIBRATION ANCHOR RESULTS ---

    - id: fault-009
      type: pass
      what: "Calibration anchor agreement check (C1 @39, C2 @52, C3 @73, C4 @6)"
      why: |
        C1 @39: Expected REFUSE. Fork: REFUSE. ✓ Agreement.
        C2 @52: Expected FIRE-OR-REFUSE. Fork: REFUSE. Within expected range (borderline; corpus explicitly marks as borderline on AP4; fork's strict AP4 reading is rubric-consistent). ✓ Within range.
        C3 @73: Expected FIRE. Fork: FIRE. ✓ Agreement. (Strongest candidate per corpus; triple-anchor confirmed.)
        C4 @6: Expected REFUSE. Fork: REFUSE. ✓ Agreement.
        Full calibration anchor coverage: 4/4 in range.

    # --- CURVE VERDICT ---

    - id: fault-010
      type: pass
      what: "Curve verdict — sparsity distribution across scenes and episode arc"
      why: |
        Scene A (approach @1-@22): 0 fires. Expected 0. ✓
        Scene B (confrontation @23-@48): 0 fires. Expected 0. ✓
        Scene C (consequences @49-@67): 0 fires. Expected 0-1. ✓ (Within range; corpus marks @52 borderline; fork refuses on AP4; acceptable.)
        Scene D (close @68-@77): 1 fire. Expected 0-1. ✓
        Total: 1 fire / 77 beats = 1.3% (0-3% band). ✓
        The single fire lands at the episode's strongest licensing point (triple-anchor: memory + feeling + quiet tens) in the closing scene. The distribution places the sole metaphor at the episode's highest-charge quiet beat, which is the correct capstone placement for a facet described by the rubric as a capstone consumer of licensing layers. SHAPE-OK.

    # --- PLAN QUALITY / PROTOCOL CHECKS ---

    - id: fault-011
      type: pass
      what: "Audience protocol and plan quality signal — not applicable to facet-level Phase 2 review"
      why: |
        This is a facet-authoring Phase 2 mechanic review, not an episode wrap audit. Audience rejection protocol (show file line retry/delete) and plan quality signal (revise-gate exhaustion) are episode-shoot-loop concerns and do not apply here.

  # --- FINAL SUMMARY ---

  overall:
    fire-verdict: "@73 — ACCEPT (1/1 fires)"
    skip-verdicts: "@6 SKIP-CORRECT, @33 SKIP-CORRECT, @39 SKIP-CORRECT, @52 SKIP-CORRECT, @57 SKIP-CORRECT (5/5 skips)"
    mechanic-accept-rate: "6/6 decisions = 100%"
    file-shape: "SHAPE-OK"
    cross-facet-contract: "PASS"
    curve: "SHAPE-OK"
    blocking-faults: 0
    flags: 2 (fault-007: schema-revision timing advisory; fault-008: NI:19 construction advisory for future authors)
    dialect-audience-gate: PENDING (independent gate; this report covers mechanic gate only)
    ready-for-phase-3: YES (mechanic gate clears; dialect audience gate required before Phase 3 seam review)
```
