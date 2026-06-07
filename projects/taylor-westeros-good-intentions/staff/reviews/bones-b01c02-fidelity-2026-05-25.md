```yaml
audit:
  scope: chapter
  target: b01c02
  phase: and-review-bones (chunk→bones fidelity review; URI-WRITE-BONES-REVIEW-GATE)
  timestamp: 2026-05-25
  verdict: PASS-WITH-NOTES

  summary: |
    29 bones across 3 scenes. All load-bearing events from all 3 scene chunks are carried by the
    bone set. Causal arcs are recoverable by an independent reader across all 3 scenes. No
    demonstrable fidelity gap — no event is claimed covered by event_map but undelivered in physical
    bone action. Five specific watch items reviewed; all 5 pass with one minor note on the s02n13
    prohibition-distribution question (flag, not fault). Dialogue-coverage gate: trivially passes
    (zero dialogue-anchor bones; Taylor speaks to no one). One PASS-WITH-NOTES finding (flag-001)
    is soft and parking-lot appropriate; it does not block /and-facets.

  findings:

    # ─── SCENE 1: s01 ALL-HELD OPENING (9 bones, no axis movement) ────────────

    - id: pass-001
      type: pass
      what: s01 bones 1-9 read as coherent mechanism-establishment, not 9 inert sentences
      why: |
        The watch item: "does the scene read as coherent mechanism-establishment, or as 9 sentences
        in a row that don't do anything?"

        The scene has a causal spine that an independent reader can recover:
          bones 1-2 (leaves drain angle → insects fan alleys): Taylor at subsistence range, the
            feed operating at its ambient baseline. These two bones set the "before" state against
            which the decision reads as change.
          bone 3 (ward delivers heat-signatures): the fever-cluster arrives as the force that
            initiates the decision. Causal: the feed at subsistence range returns a problem it
            cannot locate. Without bone 3, bones 4-9 have no mechanical trigger.
          bone 4 (takes the alley-mouth): the decision-body, physically enacted. Taylor moves
            to the threshold before the rationale is drawn. This is the decision in physical form,
            not in interior statement.
          bone 5 (insects cross threshold-stones): mechanism specification — the relay pathway
            that makes the sweep generate heat-data without skin contact. Precondition for the
            "without contact" premise that s02 relies on.
          bone 6 (extends the range): the deliberate extension enacted as movement past the first
            alley-junction. The decision from bone 4 expressed as a deployment act.
          bone 7 (draws the line): the harm-reduction reframe — reads ≠ directs — as a physical
            stopping-point. The framing is the prohibition boundary drawn in the same motion as the
            extension. Structural: without this bone, the reader cannot see where Taylor places the
            line before crossing it.
          bone 8 (insects fill the Hook): sweep architecture activated, corner-to-corner. This is
            the event_map tag "event: Taylor begins the first precinct sweep" in its spatial form.
          bone 9 (foot-traffic knots the ward-junction): sweep output arrives as ward data. The
            mechanism delivers its first return.

        The arc is: ambient-read → fever-problem → body-decision → mechanism-specified →
        extension-enacted → line-drawn → sweep-fills → output-returns. Causal at every step.
        PASS.

    # ─── SCENE 2: WREN AS PERCEPTUAL EVENT ─────────────────────────────────────

    - id: pass-002
      type: pass
      what: s02 bones 10, 12, 13, 16, 17, 18, 19 — Wren as observable feed-output, not reasoning
      why: |
        Watch item: "bones n10-n19 must carry [Wren's perceptual pattern] as observable feed-output,
        NOT as Taylor's reasoning."

        Reviewing the specific bones flagged:

        bone 10 (the insects return the ward-junction body): the ward-junction body enters the feed
          as a return from the coverage mechanism, not as a named person Taylor is reasoning about.
          Phrased as a feed-output ("return"), not as Taylor noticing or inferring.

        bone 12 (the ward-junction body crosses the thresholds): movement rendered as the physical
          act of threshold-crossing, not as Taylor reasoning about network-centrality. Six specific
          threshold-crossings are behavioral data produced by the feed.

        bone 13 (the alley admits the ward-junction body): the alley-entry is rendered from the
          ward's physical geometry — the alley admits the body; Taylor is absent as grammatical
          subject. The perceptual event is the admittance itself.

        bone 16 (taylor-hebert-kl-122ac yields the alley-mouth): Taylor's body yields, not Taylor
          deciding to not approach. The discipline against approaching reads as physical act, not
          inner rationale. This is the bone flagged in the brief as carrying the prohibition-against-
          Taylor; see flag-001 below on the distribution between n13 and n16.

        bone 17 (the insects file the ward-junction contact): filing as feed-model-building, not as
          Taylor deciding to categorize. The insects are the grammatical subject — the model builds
          itself from the data.

        bone 18 (the coverage map opens the gap): the gap is a property the map opens — a physical
          fact of the coverage architecture, not an inference Taylor draws about where she cannot go.

        bone 19 (the coverage map holds the gap): the gap is held by the map, not narrated as
          Taylor's awareness of the gap. The distinction between "the map holds the gap" and "Taylor
          realized there were gaps where Wren moved" is the difference between perceptual event and
          reasoning chain. The bone is on the correct side of that line.

        All 8 specific watch-bones execute Wren as a physical pattern in the feed. No bone collapses
        to interior-state report or reasoning chain. PASS.

    # ─── SCENE 2: PROHIBITION DISTRIBUTION (n13 + n16) ─────────────────────────

    - id: flag-001
      type: flag
      what: |
        s02n13 ("the alley admits the ward-junction body") + s02n16 ("taylor-hebert-kl-122ac yields
        the alley-mouth") — prohibition-against-Taylor distributed across two bones; question of
        whether discipline remains Taylor's enacted choice or dissolves into scenery
      why: |
        The brief flags: "the prohibition-against-Taylor was originally in the line, now distributed
        across n13+n16 (yields alley-mouth). Does the prohibition still read as Taylor's discipline,
        or does it dissolve?"

        On the bones as written: n13 renders the alley-entry from the ward's geometry (the alley
        admits the body; Taylor is not the subject). n16 renders Taylor yielding the alley-mouth
        as a transitive act — Taylor is the agent, the alley-mouth is the object, and "yields" is
        a volitional verb. The discipline is present in n16: yielding is an act, not an absence.

        The two-bone distribution is not a fidelity failure — both bones are in the event_map and
        both cover assigned chunk events. However, there is a soft risk at stitching time: if the
        prose renders n13 as Taylor observing from outside the alley and n16 as Taylor simply
        turning away without the reader recovering the connection between them (the alley Wren
        entered is the alley-mouth Taylor then yields), the prohibition's force could read as
        environmental rather than disciplinary.

        The fidelity gap is not at bone level — the bones deliver the required events. The risk is
        a stitcher-execution problem: if the gap between n13 and n16 is prose-filled with two
        unrelated images rather than a continuous scene in one physical space, the discipline reading
        softens. This is worth flagging for /and-stitch Phase 0 lens-anchoring — the stitcher should
        understand n13 and n16 share a spatial frame (Taylor at the alley-mouth watching the body
        enter the alley she cannot follow into, then turning away from that same alley-mouth).

        Flag, not fault: bones honor the chunks. The risk is downstream prose execution.
      criteria: null

    # ─── SCENE 3: CRACK-AND-SUPPRESS TWO-BONE REQUIREMENT ──────────────────────

    - id: pass-003
      type: pass
      what: |
        s03 bones 24-25 (stalls the count → draws the line) — recognition-then-suppression as two
        structurally separate events
      why: |
        Watch item: "does the stall-then-draw-line sequence land as recognition-then-suppression, or
        does the abstracted vocabulary blur the beat?"

        The vocabulary audit:
          bone 24 ("taylor-hebert-kl-122ac stalls the count"): the verb "stalls" is volitional but
            describes a failure to continue — the count in progress stops mid-run. The draft notes
            gloss this as "somatic halt: the body stalls the in-progress accounting — enacted as
            Taylor's body halting the count." The abstracted vocabulary (stalls, count) is in the
            same register as the bones that precede it (runs the map, closes the count) — the
            accounting vocabulary is established by bones 21-23, so "stalls the count" reads as the
            accounting stopping, not as a general pause. The recognition arrives as the count stops;
            the stopping is the recognition's physical form.
          bone 25 ("taylor-hebert-kl-122ac draws the line"): the vocabulary repeats the gesture from
            s01 bone 7 (the same "draws the line" construction). The echo is structurally intentional:
            the reader saw the prohibition-line-drawing deployed as setup in s01; it fires here as the
            suppression mechanism. The gesture's meaning is already loaded. The bone does not need to
            explain suppression — the echo does it.

        The two-bone crack-and-suppress reads as structurally distinct:
          - bone 24 is passive in its causation (the body stops the count — something arrives that
            causes the stall)
          - bone 25 is active as a response (Taylor draws the line — she applies the prohibition
            gesture in reply to the stall)
          The sequence is cause-and-response. An independent reader recovers: something stopped the
          accounting, and Taylor applied a specific closing mechanism to restart and complete it.

        The abstracted vocabulary does not blur the beat because the accounting register (established
        across bones 21-24) makes "stalls" land as halting a specific ongoing action, and the echo of
        "draws the line" from s01 provides the suppression frame without needing to name it. PASS.

    # ─── SCENE 3: CHAPTER GOAL DELIVERY ────────────────────────────────────────

    - id: pass-004
      type: pass
      what: |
        s03 bone 22 (the map returns the bodies) — scope-of-the-surveillance-map delivery;
        s03 bones 26-28 (ledger closes fever-cluster entry → dark-junction entry → ward-junction
        contact) — "files it and continues" delivery
      why: |
        Chapter goal: "Show the audience Taylor's first self-constructed surveillance map and the
        moment she recognizes what it is — then files it and continues — so the pattern is visible
        before any patron arrives to name it."

        Bone 22 ("the map returns the bodies"): the draft notes specify this bone "returns forty-three
        bodies" — the number makes the map's scope physical and concrete. An independent reader
        recovering the causal arc would see: Taylor runs the map (bone 21) → the map returns a
        specific count (bone 22, forty-three bodies) → the accounting arrives at its edge (bone 23).
        The scope of the surveillance map is delivered as the map's own output — not as Taylor
        thinking "I have forty-three people under surveillance," but as the map returning forty-three
        bodies to the accounting process. The vocabulary keeps the map as the instrument acting on
        Taylor's accounting, not as a conclusion Taylor reaches. The chapter goal's "first
        self-constructed surveillance map" is visible at bone level through the count that the map
        itself produces.

        Bones 26-28 (closes the fever-cluster entry → closes the dark-junction entry → closes the
        ward-junction contact): the ledger-closing sequence runs three entries in the same procedural
        register. Wren-unnamed (the ward-junction contact at bone 28) is processed in the same
        accounting frame as anonymous ward data (fever-cluster at bone 26, dark-junction at bone 27).
        An independent reader recovers: after the recognition and suppression (bones 24-25), Taylor
        does not sit with the recognition — she applies the same closing procedure to each entry in
        the map and the accounting is done (bone 29's exhale confirms the accounting is complete).
        The "files it and continues" beat is enacted as three sequential ledger-closing actions
        followed by a physical chapter-close (exhale at drain angle). Not a report that Taylor
        filed and continued — an enactment of the filing sequence.

        Both the map-scope delivery and the ledger-close sequence read as the chapter goal's
        requirements honored at bone level. PASS.

    # ─── DIALOGUE-COVERAGE GATE ─────────────────────────────────────────────────

    - id: pass-005
      type: pass
      what: Dialogue-anchor bones — URI-WRITE-DIALOGUE-COBONDED gate
      why: |
        Taylor speaks to no one in b01c02. Zero dialogue-anchor bones expected. Confirmed: no bone
        in the 29-bone set carries a [<character-slug>:<id>] citation token. No per-character
        dialogue files are required or expected for this chapter. Gate trivially passes.

    # ─── CROSS-SCENE CAUSAL ARC ──────────────────────────────────────────────────

    - id: pass-006
      type: pass
      what: Chapter-level causal arc — recoverable by independent reader across all 3 scenes
      why: |
        The question the mechanical gate cannot answer: would an independent reader, reading only
        the 29 bones, recover the chapter's central causal arc?

        The arc as the chunks specify it:
          Taylor extends coverage under harm-reduction framing (s01) →
          Wren enters the feed as a pattern Taylor cannot follow into (s02) →
          Taylor runs the completed map, the recognition arrives, she suppresses it and files it
          under harm-reduction (s03)

        An independent reader reading bones 1-29 in sequence recovers:
          1-9: Taylor starts from an anonymous sleeping position, has a fever-cluster problem she
            cannot locate at ambient range, decides to extend the range deliberately, draws a
            prohibition line (reads ≠ directs), and fills the ward with insects corner-to-corner.
            The sweep produces output (foot-traffic at the ward-junction).
          10-19: The coverage sweep returns a body repeatedly — a high-traffic node that touches
            many thresholds, enters alleys the sweep does not fully reach, gets categorized as a
            connector-type and filed under a specific sensory-anchor. The coverage map opens and
            holds a gap wherever this body moved.
          20-29: Taylor returns to the sleeping position, runs the map, gets forty-three bodies
            back, the accounting reaches its edge and stalls, Taylor applies the prohibition-line
            gesture to close the stall, the ledger closes three specific entries (fever-cluster,
            dark-junction, the ward-junction contact), the accounting is done, Taylor exhales.

        The recognition is recoverable from the stall + draws-the-line sequence (bone 24: something
        stops the count; bone 25: Taylor applies the suppression). The suppression is recoverable
        from the ledger-closing sequence (26-28: the accounting proceeds through each entry without
        reopening the recognition). The map's scope is recoverable from bone 22 (forty-three
        bodies). Wren's negative-space is recoverable from bones 18-19 (gap opened and held at
        every alley the junction-body entered).

        All central events are carried. The causal arc is intact across all 3 scenes. PASS.

    # ─── VERDICT ─────────────────────────────────────────────────────────────────

    # PASS-WITH-NOTES.
    # No fidelity gap found. All chunk events are physically enacted in the bone set.
    # All 5 specific watch items reviewed: PASS (pass-001 through pass-004) with one flag
    # (flag-001: prohibition-distribution n13+n16, soft stitcher-execution risk, parking-lot).
    # Dialogue-coverage gate: PASS (trivially; no dialogue-anchor bones).
    # Chapter-level causal arc: recoverable by independent reader. PASS.
    # /and-facets is unblocked.
```
