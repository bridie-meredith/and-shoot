```yaml
audit:
  scope: episode
  target: active-project/theater/proto-lines/chapter-03.md
  timestamp: 2026-05-07
  run: pass-5-continuity (fresh fork, independent re-verify)
  verdict: FAIL

  summary:
    file_level: FAIL
    total_content_lines: 46
    blank_timeskip_lines: 7
    findings:
      fault_count: 3
      flag_count: 2
      fault_breakdown:
        FAULT-CONTINUITY-SEQUENCE: 1
        FAULT-CONTINUITY-REACHABILITY: 1
        FAULT-CONTINUITY-REFERENCE-DRIFT: 1

  findings:

    # ─── RESTRUCTURE COHERENCE ──────────────────────────────────────────

    - id: fault-001
      type: fault
      class: FAULT-CONTINUITY-SEQUENCE
      what: >
        IDs 77 → 37 → 38 (file lines 63–65): `taylor-hebert-westeros exits the sept`
        is followed immediately by `taylor-hebert-westeros speaks to the septon` and
        `the septon draws the breath`. Taylor is outside the sept at ID 77 and speaking
        to the septon in the same beat sequence with no re-entry, no doorway beat, and
        no location-bridge between exit and speech.
      why: >
        The spatial logic is broken. Either:
        (A) the conversation with the septon occurs at the sept doorway, in which case
        ID 77 should be `taylor-hebert-westeros reaches the sept door` or similar —
        not a full exterior exit — and IDs 37–38 would be spatially plausible; OR
        (B) the conversation occurs before the exit, in which case IDs 37–38 should
        precede ID 77 in citation order, not follow it.

        The iter2 S2 shape audit flagged this ordering for editor pass. This audit
        classifies it as a blocking fault: `exits` places Taylor outside the building;
        the next line requires her to address the septon who is inside or in the
        doorway without establishing where that exchange occurs. A stitcher walking
        citation order will produce a spatial contradiction: character exits, then
        speaks from an unresolved location. Facet authors citing both beats will
        produce conflicting location-state and dialogue entries.

        Downstream consequence is systematic: narrator-interest, feeling-flags, and
        state-updates facets will all independently resolve the ambiguity in different
        directions, producing incoherent cross-facet records for this beat.
      criteria: >
        One of the following must be achieved:
        (A) Reorder: move IDs 37–38 to precede ID 77 in the citation walk, so the
        septon exchange occurs before the exit. This requires no new lines, only
        reordering within the segment.
        (B) Replace: replace ID 77 with a beat that positions Taylor at the threshold
        rather than fully outside (e.g., `taylor-hebert-westeros reaches the sept door`
        or `taylor-hebert-westeros turns at the sept door`), making the doorway
        exchange spatially coherent.
        (C) Insert: insert a re-entry or doorway beat between ID 77 and ID 37 to
        resolve the spatial gap. This adds a line to a file that is already near
        expected_lines (44).
        Option (A) is minimum-change. Option (B) is minimum-add. Option (C) adds
        load to an already-at-capacity file.

    # ─── STATE PERSISTENCE ──────────────────────────────────────────────

    - id: fault-002
      type: fault
      class: FAULT-CONTINUITY-REACHABILITY
      what: >
        ID 70 (line 45): `a raven lifts the sept yard`. This is the fourth distinct
        fauna-relay attempt in the chapter (attempts 1–3 are the hedgerow-stall sequences
        at IDs 56–60 and 62–67). ID 47 ends the third attempt with
        `taylor-hebert-westeros presses the temples` (cost marker). ID 71 then shows
        `blood reaches the lip` — a nosebleed onset, the highest cost marker in the
        file. The sequence implies Taylor is at or near cost ceiling before ID 70 fires.

        ID 70 introduces a new raven from the sept yard without any established
        cost-recovery beat between ID 47 (third-attempt cost) and ID 70 (fourth-attempt
        dispatch). Under cond-fauna-control-rules, the cost curve is cumulative and
        physiological: three failed relay attempts at field range in sequence produce
        progressively higher cost markers. Dispatching a fourth raven immediately after
        the nosebleed onset (ID 71 is post-attempt, but the attempt at ID 70 precedes
        ID 71 only in line order — causally, the dispatch is what produces the bleed)
        is narratively coherent only if this is a deliberate-attempt-despite-cost beat.

        The file does not include a beat showing Taylor choosing to push past the cost
        ceiling; ID 70 reads as a fresh dispatch with no contextual signal that it is
        a costly override. The restructure was intended to produce a
        failure → deliberate-attempt → cost-cascade structure (per fixer log). The
        deliberate-attempt beat (the choice to push) is implied but not present in SVO
        form. Facet authors cannot infer agency versus automaticity from the bone alone.

        This is a reachability fault: the fauna-control cost state is not confirmed as
        reset or acknowledged as pushed before ID 70 fires.
      why: >
        cond-fauna-control-rules requires cost accumulation to be tracked. Three failed
        relay attempts at extended range (hedgerow: ~400–600m, per prior audits) produce
        cost. ID 70 dispatches a fourth attempt without establishing that cost was
        absorbed or that the dispatch is a deliberate override. The nosebleed at ID 71
        follows as the consequence, which is correct — but without a choice-to-push beat
        between the third-attempt cost marker (ID 47) and the fourth dispatch (ID 70),
        the cost cascade reads as a passive onset rather than a deliberate-cost-acceptance
        arc. The fixer log's stated restructure goal ("deliberate-attempt structure") is
        not fully present in the bones.

        Downstream consequence: feeling-flags and narrator-interest facet authors have
        no bone to cite for the moment Taylor decides to push past cost ceiling. The
        dramatic weight the restructure intended to create is not anchored in the SVO.
      criteria: >
        Insert one beat between ID 47 and ID 70 that establishes the fourth dispatch
        as deliberate. A valid form: `taylor-hebert-westeros lifts the chin` (resolve)
        or `taylor-hebert-westeros releases the hands` (prior hold released, body
        repositioned for effort) — any licensed body-repositioning beat that implies
        re-engagement rather than passive continuation. The beat must be SVO-clean,
        Taylor-subject, physical only, no motivation clause. This is a one-line fix.

    # ─── REFERENCE RESOLUTION ───────────────────────────────────────────

    - id: fault-003
      type: fault
      class: FAULT-CONTINUITY-REFERENCE-DRIFT
      what: >
        ID 37 (line 64): `taylor-hebert-westeros speaks to the septon`. The character
        referenced as `the septon` is unnamed. Chapter 04 (lines 8, 9, 10, 16, 21, 25)
        uses the slug `septon-rowan` — a specific named character who is established
        as present at the sept from ch04 forward. Chapter 01 uses `septon-dying-protector`
        for the resident septon at chapter-01 open. The septon-dying-protector's
        status after ch01 is not confirmed in this file; ch03 plan's actor list
        includes only `taylor-hebert-westeros`.

        `the septon` at ID 37 is an unresolved reference. Two septon characters exist
        in the series cast roster (septon-dying-protector and septon-rowan). ch04
        opens with `septon-rowan rises from the chancel steps` (line 8), which
        establishes septon-rowan at the sept at chapter-04 open. ch03 ends with
        Taylor speaking to `the septon` — if that is septon-rowan, his ch03-close
        position (at the sept, speaking to Taylor) must flow to ch04-open without
        gap. If it is septon-dying-protector, that character's survival through
        ch03 is unrecorded and his presence at ch04-open as `septon-rowan` is a
        different character — no continuity fault there, but the ambiguity in ch03
        prevents the stitcher from assigning a slug.
      why: >
        Bare `the septon` is a pronoun-equivalent reference at a moment where two
        septon-slugged characters exist in the cast. The stitcher cannot resolve
        which character `the septon` names without external context. Facet authors
        citing ID 37 will make independent resolution choices, producing inconsistent
        actor assignments. State-updates facets will update the wrong septon's
        location if they resolve differently.

        ch02→ch03 boundary: ch02 does not include either septon. ch03 does not
        establish which septon is present. ch04 names septon-rowan at the sept
        without establishing how he arrived or when. The `the septon` reference
        at ch03 ID 37 is the only cross-chapter link — if unresolved, the ch03–ch04
        boundary has a character-identity gap at the connecting beat.
      criteria: >
        Replace `the septon` with the correct slug — either `septon-rowan` or
        `septon-dying-protector` — consistent with the chapter plan's intended
        character. Given ch04 opens with septon-rowan established at the sept and
        ch03 ends with Taylor speaking to `the septon`, the most likely intended
        resolution is `septon-rowan`. Confirm against chapter plan authority, then
        apply the slug. Simultaneously update ID 38 (`the septon draws the breath`)
        to `septon-rowan draws the breath` for matching resolution.

    # ─── FLAGS ──────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      what: >
        ch02→ch03 boundary: ch02 closes with Taylor taking the sept road (ID 68:
        `taylor-hebert-westeros takes the sept road`). ch03 opens with ID 1:
        `taylor-hebert-westeros descends the loft ladder`. The transit from the
        sept road to the loft interior is unrecorded — Taylor was traveling toward
        the sept at ch02 close and is already in the loft at ch03 open.
      why: >
        The gap is a timeskip — consistent with the blank-ID timeskip convention
        used throughout the file sequence. The loft position at ch03-open is
        reachable from ch02-close without a spatial contradiction (taylor takes
        the road → arrives at sept → climbs to loft). No actor is placed in a
        location they could not have reached. This is a flag not a fault because
        the arrival transit is narratively inferable and timeskip-style ellipsis
        is established convention in this pipeline.
      criteria: >
        No fixer action required. Editor pass may insert a transition note if
        prose continuity requires it. Pass 5 scope: no further action.

    - id: flag-002
      type: flag
      what: >
        ch03→ch04 boundary: ch03 closes with ID 43 (`the cottage fire snaps`) after
        Taylor climbs the loft ladder (ID 41) and holds the feet (ID 42). ch04 opens
        with `the ravens flush the bell tower` (ID 1) and Taylor entering the yard
        (ID 2). Taylor's position at ch04-open is the sept yard exterior. ch03-close
        has her in the loft. The transit from loft to yard is again unrecorded.
      why: >
        Same timeskip convention as flag-001. The loft→yard transit is physically
        trivial (descend ladder, cross yard). No spatial contradiction. Taylor's
        ch04-open inventory and state are consistent with the ch03-close position —
        no props are carried that aren't established. Flag, not fault.
      criteria: >
        No fixer action required at pass 5. Editor pass handles prose transition
        if needed.

  # ─── SPECIAL-FOCUS VERDICT: 77→37-38 ORDERING ──────────────────────

  special_focus_ID77_ordering:
    question: >
      Does the spatial logic hold for ID 77 (`taylor-hebert-westeros exits the sept`)
      preceding IDs 37–38 (`speaks to the septon` / `the septon draws the breath`)?
    verdict: DOES NOT HOLD
    rationale: >
      ID 77 places Taylor outside the sept building. IDs 37–38 place her in dialogue
      with the septon who is inside or near the chancel. No doorway beat, no
      threshold-hold beat, and no re-entry beat bridges the two positions. The
      stitcher walking citation order reads: [Taylor is outside] → [Taylor speaks
      to septon]. The interaction at IDs 37–38 cannot occur at Taylor's post-ID-77
      exterior position. This is a sequencing error, not a doorway-exchange reading —
      a doorway exchange would require ID 77 to name a doorway position, not a full
      exit. Classified as fault-001 above.

  # ─── POV CONSISTENCY (cond-fauna-control-rules) ─────────────────────

  pov_consistency:
    result: PASS (with fault-002 noted)
    detail: >
      All events in the restructured ch03 are observable from Taylor's physical
      position at or near the sept environs. The pass-2 reverify faults (POV
      violations for Harrenhal-interior events) have been resolved: no Harrenhal-
      interior, records-hall, or garrison-hall beats appear in the current file.
      All fauna-relay beats (hedgerow stalls, field crossings, sept-yard raven)
      target locations at plausible range from the sept. The nosebleed / cost
      accumulation chain is present and physically consistent with cond-fauna-
      control-rules. The one reachability fault (fault-002) concerns a missing
      cost-state signal at the fourth dispatch, not a range violation.

  # ─── STATE PERSISTENCE ───────────────────────────────────────────────

  state_persistence:
    result: PASS (with flag-001 and flag-002 for boundary gaps)
    detail: >
      Ravens: introduced at loft perch (ID 56), bell tower (ID 62), sept yard (ID 70),
      and ambient lift (IDs 48–52). Ravens settle at ID 34, then Taylor releases at
      ID 72. Release is the correct close for an active-dispatch session. No raven
      appears in a location before being established there.
      Body holds: feet (ID 8 / ID 42), chin (ID 9 / ID 69), hands (ID 39) — all
      holds are consistent with accumulated cost posture and are released or implicitly
      closed by the chapter's physical resolution. No hold is opened without a
      prior cost-marker establishing the need.
      Blood / nosebleed: appears at ID 71 (`blood reaches the lip`). This is the
      correct form (physicial-event verb, no state-assertion). Consistent with the
      pass-3 shape flag in ch02 that noted `blood marks the lip` was borderline —
      ch03 uses `reaches`, which is the cleaner form.
      Fire: ID 43 (`the cottage fire snaps`) is an ambient environment event,
      Taylor-observer position consistent with loft interior. No fire was established
      as absent in prior chapters; no state violation.

  # ─── TIME CONSISTENCY ────────────────────────────────────────────────

  time_consistency:
    result: PASS
    detail: >
      Three sequential fauna-relay attempts (field → hedgerow → hedgerow stall;
      bell-tower relay → same stall; sept-yard drive → drop) imply sustained
      effort over a single session. No time markers conflict. The blank-ID timeskips
      (10, 16, 21, 27, 33, 40) are used consistently as narrative ellipsis within
      the chapter. Chapter plan states the chapter covers Taylor holding position
      at the sept while events she cannot observe occur at Harrenhal — the timeline
      is a single holding period, which the sequence represents without contradiction.

  # ─── CAUSE-EFFECT ────────────────────────────────────────────────────

  cause_effect:
    result: PASS (with fault-002 noted as a missing cause beat)
    detail: >
      Each raven dispatch is followed by a raven-action sequence and a cost
      marker (temples / chin hold / blood). The chain is: dispatch → relay attempt →
      stall/drop → cost beat. This is internally coherent. The exception at
      ID 70 (fourth dispatch) is flagged at fault-002: the cause-beat showing
      Taylor's choice to re-engage after the third-attempt bleed is absent.
      All other cause-effect pairs resolve cleanly.

  # ─── NON-MONOTONIC ID EXEMPTION ─────────────────────────────────────

  id_ordering_exemption:
    status: VERIFIED
    detail: >
      The file header exemption comment is present and correct. The stitcher is
      directed to walk citation order, not ID-monotonic order. This audit has
      conducted all checks in citation order (as listed above in segment walk).
      The exemption is valid: IDs 1–9, 34, 37–44, 45–47 are surviving original
      IDs interleaved with new IDs 48–77. The citation-order walk produces a
      coherent narrative sequence (fault-001 excepted). No additional non-monotonic
      ordering faults are present beyond fault-001's sequencing error.

  file_level_verdict: FAIL
  reason: >
    Three blocking faults present. fault-001 (spatial sequence error ID 77→37–38)
    and fault-003 (unresolved septon slug) are minimum-change fixes. fault-002
    (missing deliberate-attempt bone before fourth raven dispatch) requires one
    inserted line. All three must be resolved before the file can advance to
    downstream facet authoring.
```
