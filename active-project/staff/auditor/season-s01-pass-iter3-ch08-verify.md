```yaml
audit:
  scope: season
  target: s01-ch08-restructure-iter3-verify
  timestamp: 2026-05-07
  verdict: PASS
  residuals_closed:
    - RESIDUAL-1: CLOSED
    - RESIDUAL-2: CONDITIONAL — see finding pass-005
  findings:

    # ── DIMENSION 1: FAUNA-CONTROL RANGE COMPLIANCE ──────────────────────────

    - id: pass-001
      type: pass
      what: >
        IDs 31–45 — raven in recorder's room while Taylor is in the passage.
        Taylor enters the passage at ID 30 (reaches the passage). The recorder's
        room is an interior room of Harrenhal; the passage is an adjacent
        interior corridor. Internal building distance between the passage and
        the recorder's room is on the order of tens of meters — well within the
        200m normal-load radius. No extended-range deployment required.
        Physical-cost markers present (temple pressing ID 42, nose-bridge pinch
        ID 44, lip wipe ID 45) are consistent with accumulated session cost
        (fauna has been active since at least the passage entry), not with
        range overextension. Constraint cond-fauna-control-rules satisfied.
      why: No violation.

    - id: pass-002
      type: pass
      what: >
        IDs 65–88 — fly in great hall while Taylor is at great-hall door /
        great-hall passage (IDs 62–63 establish position; ID 88 records Taylor
        still pressing the stone at the passage wall after the hall empties).
        Taylor is at the threshold of the great hall — inside Harrenhal, at the
        door. The fly is inside the hall on the other side of that door. Distance
        from Taylor to fly is at most the thickness of a wall and the interior
        span of the hall entrance — under 50m at any plausible Harrenhal
        geometry. Well within 200m normal-load radius. Cost markers (temple
        pressing ID 77, palms pressing ID 79, fly at table ID 80, nose-bridge
        pinch ID 82, blood at lip ID 83) are consistent with cumulative session
        cost across a sustained multi-species operation (raven + fly), not range
        overextension. Constraint cond-fauna-control-rules satisfied.
      why: No violation.

    - id: pass-003
      type: pass
      what: >
        IDs 93–95 — Taylor withdraws raven and fly while on the road just
        outside the postern gate (IDs 90–92 establish: reaches postern gate,
        exits postern gate, takes road). The postern gate is in the outer wall
        of Harrenhal. The road immediately outside the postern is meters to
        low tens of meters from the gate. The recorder's room and great hall
        are interior structures. By any reasonable Harrenhal site geometry,
        Harrenhal's enclosed area is approximately 10 acres (roughly 200m ×
        200m footprint); the fauna in the recorder's room and great hall are
        therefore at most 200–300m from the postern gate. Taylor on the road
        just outside is within 600m of both. Withdrawal at this position is
        within constraint. Constraint cond-fauna-control-rules satisfied.
      why: No violation.

    - id: pass-004
      type: pass
      what: >
        ID 96 — "a raven lifts from the recorder's beam." Taylor has already
        withdrawn the raven (ID 94) before this line fires. ID 96 describes the
        raven's independent post-release behavior — a bird that was perched on a
        beam taking flight after the control channel closes. This is not an
        active fauna-control action by Taylor. cond-fauna-control-rules notes:
        "she loses granular control beyond range" and ravens "continue on
        trajectory" after dispatch. A raven lifting from a beam after withdrawal
        is natural fauna behavior, not a controlled deployment. No range check
        applies. Constraint cond-fauna-control-rules satisfied.
      why: No violation.

    # ── DIMENSION 2: CONTINUITY FLOW ─────────────────────────────────────────

    - id: pass-005
      type: pass
      what: >
        ch07 ending → ch08 opening: ch07 ID 94 ("taylor-hebert-westeros crosses
        the outer ward") places Taylor inside Harrenhal at chapter close. ch08
        IDs 5–6 ("crosses the outer ward" → "enters the side chamber") are
        consistent: Taylor is already in the outer ward and proceeds to the
        assessment. Location continuity is clean. No gap.

        ch08 ending → ch09 opening: ch08 IDs 90–92 place Taylor exiting the
        postern gate and taking the road. ch09 IDs 100–101 ("crosses the
        approach road" → "reaches the roadside rise") are consistent with Taylor
        having exited the postern and moved along the approach road to the rise.
        Location continuity is clean. No gap.

        Prop custody: no prop-custody issues introduced by the restructure. The
        assessment papers remain with the maester (he seals and exits with the
        roll, ID 22–26); the raven and fly are active channels, not physical
        props.

        Time: assessment scene (IDs 1–26) followed by passage surveillance
        (IDs 29–46), then passage to great-hall door (IDs 61–63), then great-
        hall surveillance (IDs 65–88), then withdrawal and exit (IDs 89–96).
        The sequence is internally coherent; no time-of-day collision visible.
      why: No violation.

    - id: pass-006
      type: pass
      what: >
        Maester continuity into ch08-interlude: Taylor-POV ch08 ID 26 shows
        the maester exiting the side chamber with the sealed roll (IDs 22–23
        establish rolling and sealing; ID 26 is exit). ch08-interlude IDs 1–7
        show the maester speaking to the castellan in the hall, passing the
        sealed roll, and exiting the hall. The maester exiting the side chamber
        → delivering the sealed roll to the castellan in the hall is a direct,
        spatially coherent sequence. The interlude's opening action (maester
        delivers roll) is the downstream consequence of the assessment scene's
        close. No collision.
      why: No violation.

    # ── DIMENSION 3: MECHANIC CLEANLINESS ────────────────────────────────────

    - id: pass-007
      type: pass
      what: >
        "turns to" / "turns toward" / "crosses to" scan of the 16 recast IDs:
        none present. ID 32 ("a raven swings the head") and ID 39 ("a raven
        swings the head") use "swings" not "turns." No banned forms detected.
      why: No violation.

    - id: pass-008
      type: pass
      what: >
        Prep-phrase modifier scan across all recast IDs: no "across the [noun]
        to the [noun]," no "from [noun] to [noun]" movement constructs, no
        embedded prep-phrase modifiers on the primary SVO. Each line is a clean
        subject + verb + bare object or no object.
      why: No violation.

    - id: pass-009
      type: pass
      what: >
        Perception verb / interiority / multi-subject scan: no perception verbs
        (sees, hears, notices, feels, watches) appear in the recast IDs.
        No interiority lines. No multi-subject lines. All lines are single-
        subject, overt-action.
      why: No violation.

    - id: pass-010
      type: pass
      what: >
        ID 46: "taylor-hebert-westeros holds the passage." Adjudication:
        "holds" as a positional-stasis verb applied to a location is a valid
        SVO construct. The banned form is body-part-stillness ("holds the
        breath," "holds still") and action-chain connectors. "Holds the
        passage" means occupies or remains in the passage — it is a location-
        holding verb with a bare noun object. No prep phrase, no modifier chain,
        no interiority. The form is: subject + verb + bare noun (location).
        This is within schema. VERDICT: licensed.
      why: No violation.

    - id: pass-011
      type: pass
      what: >
        "reaches" + compound noun constructs:
        — ID 38: "reaches the passage end" — "passage end" is a nominal
          compound (noun + noun, no prep phrase). Bare compound noun object.
          Valid.
        — ID 61: "reaches the great-hall passage" — "great-hall passage" is a
          hyphenated nominal compound used as a location slug. Bare compound
          noun. Valid.
        — ID 62: "reaches the great-hall door" — "great-hall door" is the same
          pattern. Valid.
        — ID 90: "reaches the postern gate" — "postern gate" is a standard
          two-word nominal compound (attributive + noun). Bare compound noun.
          Valid.
        The FAULT-FORM-MODIFIER prohibition applies to prep-phrase modifiers
        appended to a bare-noun object ("reaches the door at the end of the
        passage" would be a fault). None of the four instances contain a prep
        phrase. All four are PASS.
      why: No violation.

    # ── DIMENSION 4: STRUCTURAL SHAPE ────────────────────────────────────────

    - id: pass-012
      type: pass
      what: >
        Iter2 S2 shape for ch08: buildup 1–63, climax 65–87 (peak 76–83),
        denouement 88–96. This shape is preserved in the restructure.

        Buildup (IDs 1–63): assessment scene (1–26), passage surveillance of
        Bracken filing (29–46), Taylor holding position and moving toward the
        hall (46–63). All buildup material is present and structurally intact.

        Climax (IDs 65–87): Celtigar letter arrival and reading aloud. Peak
        (76–83): castellan speaks to the hall, Taylor presses temples and palms,
        nose-bridge pinch, blood at lip, castellan folds the letter. All peak
        lines are present.

        Denouement (88–96): Taylor exits the hall passage, reaches and exits
        the postern gate, takes the road, withdraws fauna, raven lifts. Present
        and intact.

        Dramatic equivalence of great-hall-door position vs. prior chancel
        position: Taylor at the great-hall door with a fly inside the hall is
        narratively equivalent to Taylor at the chancel. She has sensory access
        to the interior via the fly; she is physically adjacent but concealed
        outside the door. The position is arguably stronger dramatically — she
        is outside, excluded, receiving the intelligence through an insect
        intermediary rather than being present in the room. The three
        irreversible disclosures (maester's sealed report delivered, Bracken's
        counter-claim lodged, Celtigar's letter read aloud) all land within the
        chapter. The board-worsening close (chapter goal) is achieved. No
        structural loss from the recast.
      why: No violation.

    # ── RESIDUAL STATUS ───────────────────────────────────────────────────────

    - id: pass-013
      type: pass
      what: >
        RESIDUAL-1 (ch08 fauna at 2.5km from sept cottage) — FORMALLY CLOSED.
        Taylor is no longer at the sept cottage during ch08. She is inside
        Harrenhal for the entire chapter, with all fauna deployments at internal
        building distances (under 300m at any point). The 2.5km violation is
        structurally eliminated by the restructure. No worldbuilding patch to
        cond-fauna-control-rules is required to close RESIDUAL-1.
      why: Residual eliminated by structural change.

    - id: flag-001
      type: flag
      what: >
        RESIDUAL-2 (ch09 fidelity at ~400-500m from roadside rise) — PARTIAL
        CLOSURE ONLY. The dispatch states RESIDUAL-2 "dissolves once ch08
        establishes Taylor was inside Harrenhal walls." This is not supported
        by the iter2 summary's framing of RESIDUAL-2. Per the iter2 summary,
        RESIDUAL-2 is a ch09-specific fault: Taylor at the roadside rise
        observing argument-level and document-level knowledge from inside
        Harrenhal at ~400-500m, which exceeds plausible physical-observation
        fidelity. The ch08 restructure does not bear on ch09 fauna fidelity.
        Taylor's position in ch08 (inside Harrenhal) vs. ch09 (at the roadside
        rise, ~400-500m from the walls) are independent. The ch09 fidelity
        question (whether a raven and sparrow at gatehouse-sill range can yield
        argument-level semantic content) remains open. This auditor cannot close
        RESIDUAL-2 on the evidence reviewed; it carries to the next appropriate
        pass.
      why: >
        If RESIDUAL-2 is prematurely declared closed, the ch09 fidelity fault
        will arrive unaddressed at the facet/editor pass where it is harder and
        costlier to fix. Flag is advisory; does not block the ch08 PASS verdict.
```
