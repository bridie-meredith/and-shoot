# Season Continuity Audit — s01 Pass S4 — CYCLE 2 RE-FIRE
# schema: schemas/audit-report.schema.md
# Supersedes: season-s01-pass-S4-continuity.md (cycle-2 version)
# Scope of re-fire: ID 515 deletion impact on log-state chain; ID 513 vigil-signal revision.
# Carry-forward acknowledged: fault-011 POV-leak at bones 71-77 (screen-writer REGEN-ADD deferred; Phase 6 residual).

SEASON-CONTINUITY-OK

```yaml
audit:
  scope: season
  target: s01
  timestamp: 2026-05-11
  cycle: 2-refire

  findings:

    # ── CYCLE-2 RE-FIRE CHECKS ────────────────────────────────────────────────

    - id: refire-001
      type: pass
      what: >
        ID 515 deletion — log-state chain integrity. Cycle-2 fault-015 cited
        bone 515 ("taylor-hebert-flea-bottom writes the entry") as a bare
        log-write without open/close brackets, inserted after log-close 328
        and before log-open 340, violating the invariant open/write/close
        triple pattern. Bone 515 is now absent from the file (confirmed: file
        sequence at the relevant position reads 513 → 514 → 330, with ID 515
        gap visible). The log-state chain in the affected window is:
          328 taylor-hebert-flea-bottom closes the log
          [time-skip 329]
          513 the beetles relay the cold candle   [no log operation]
          514 the beetles relay oc-broken-maester  [no log operation]
          330 the clerk enters the market-side junction
          ...
          340 taylor-hebert-flea-bottom opens the log
          341 taylor-hebert-flea-bottom writes the entry
          342 taylor-hebert-flea-bottom closes the log
        Log is closed at 328, no log operation appears between 328 and 340,
        log opens at 340. The chain is clean. No orphaned open or close
        resulted from the deletion. The broken-triple fault is resolved.
      why: ~
      criteria: ~

    - id: refire-002
      type: pass
      what: >
        ID 513 vigil-signal revision. Previous cycle-2 text: "the beetles
        relay the base room." Current text: "the beetles relay the cold
        candle." Beat 17 plan: the tanner-mother reports she has stopped
        lighting the vigil candle as a practical decision; the vigil is over.
        The cold candle is the physical correlate of that decision — an
        extinguished, cooled-wax object in a space within beetle-coverage
        territory. The relay verb pattern throughout the bones is
        consistently "the [insect] relay the [physically-perceptible
        phenomenon]": the beetles relay the sound, the beetles relay the
        pen-scratch, the beetles relay the register, the beetles relay the
        footfall, the beetles relay oc-broken-maester. A cold candle
        (thermally distinct from a burning candle, physically present as a
        wax object) is within the class of physically perceptible phenomena
        the relay pattern covers. The bone does not render Taylor knowing
        the candle was previously lit, does not render interiority, and does
        not require her to infer the mother's decision from the relay. The
        vigil signal is physically legible as an environmental relay event.
        No FAULT-FORM-INTERIORITY, no FAULT-POV. The revision resolves the
        ambiguity noted in cycle-2 flag-016's observation that the prior
        "base room" formulation lacked clear narrative function at that
        position. The cold-candle relay gives bone 513 a distinct and
        plan-anchored observable target.
      why: ~
      criteria: ~

    # ── CARRY-FORWARD FROM CYCLE 2 — STATUS CONFIRMED ────────────────────────

    - id: fault-011
      type: fault
      what: >
        Bones 71-77 (lord's-man record sequence, beat 5): no insect relay
        anchor precedes or accompanies this sequence. Taylor's insects at
        this point cover the tanner-family yard perimeter only (bones 25-34);
        no spread bone covers the wider village or the location where the
        lord's man meets the reeve and writes his record. The sequence is
        narratively rendered as observed fact without a POV anchor. Confirmed
        unchanged in the re-fire read. No new bones address this window.
        Screen-writer REGEN-ADD (a new relay anchor bone before ID 71) was
        deferred due to dispatch budget. This fault is acknowledged as
        carry-forward to Phase 6 residual.
      why: >
        Season plan: "One POV: Taylor (taylor-hebert-flea-bottom)." Beat 5
        is the Hightower-file arc opening — one of the two season-defining
        records. An unanchored direct-narration sequence at this structurally
        load-bearing beat is a FAULT-POV-LEAK. The lord's-man writing the
        file entry (bone 75) is the event that opens the arc; rendered as
        omniscient narration rather than Taylor-accessible observation, the
        POV contract breaks at the arc's inception.
      criteria: >
        The beat-5 lord's-man sequence must either (a) be preceded by an
        insect relay anchor establishing Taylor's village coverage sufficient
        to reach the reeve-lord's-man meeting location, or (b) be
        restructured so the lord's-man visit and record entry reach Taylor
        post-hoc via a POV-consistent channel (the reeve mentioning it, or
        later relay), with bones replacing the unanchored sequence. The
        recording event (bone 75 equivalent) may be elided as off-stage
        (per the carry-forward decision on fault-001) provided the
        information reaches Taylor through a POV-consistent channel.
        Resolution deferred to Phase 6 residual per dispatch-budget
        acknowledgment.

    # ── CYCLE-2 FLAGS — UNRESOLVED, CARRY-FORWARD ────────────────────────────
    # (No change to status from cycle 2; re-fire did not touch these windows.)

    - id: fault-016
      type: flag
      what: >
        Bones 513-514 at file position between time-skip 329 and bone 330
        (clerk enters market-side junction, beat 18). Re-fire confirms: bone
        513 now reads "the beetles relay the cold candle" (revised from
        "the beetles relay the base room"). The cold-candle revision gives
        bone 513 a plan-anchored function (beat 17 vigil-end signal). The
        functional gap identified in cycle 2 remains: bones 513-514 are
        ambient monitoring beats, not relay anchors for the clerk scene that
        follows them. The clerk is at the market-side junction, not the base
        room or apothecary; beetle coverage of the cold candle and of
        oc-broken-maester does not extend Taylor's observable range to the
        junction clerk exchange. Screen-writer must understand bones 513-514
        are ambient monitoring inserts, not POV coverage for bone 330 onward.
      why: >
        Ambiguity risk at screen-writer pass: if bones 513-514 are read as
        POV anchors for the clerk scene, screen-writer may render the clerk's
        record-book exchange as Taylor-accessible without a separate relay
        anchor. Bones 338-339 (the flies relay the junction / the flies relay
        the clerk) are the actual POV anchors for the clerk scene's conclusion
        and exit, not its opening exchange. The opening of the clerk scene
        (bones 330-337) remains without a relay anchor in the same sequence.
        Low fault risk if screen-writer briefing correctly identifies 338-339
        as the coverage boundary.
      criteria: ~

    - id: fault-002
      type: flag
      what: >
        Range expansion traverse (300m → 330m → 400m → 500m → 600m) across
        beats 11, 14, 19, 24 carries no explicit range-value notation at
        bone level. Bones 223-224, 271-272, 352, 446 are the log-write bones
        where range values must appear at screen-writer prose pass. Unchanged
        from cycle 2.
      why: >
        Screen-writer dependency: if these log-write bones are expanded
        without the specific range values in the beat plan, the numeric
        progression may be omitted or inconsistent. Not a structural block;
        advisory for screen-writer briefing.
      criteria: ~

    - id: fault-003
      type: flag
      what: >
        Taylor's log first appears at bone 21 while actor state file shows
        inventory: [] and research_log_active: false. No bone records the
        log's acquisition; no state update records it entering inventory.
        Unchanged from cycle 2.
      why: >
        Cross-season continuity risk: s02 audits have no state-file anchor
        for log existence.
      criteria: ~

    - id: fault-004
      type: flag
      what: >
        Dock-side insect cluster thin state (bone 389) is not recorded in
        any state file or studio record. Beat 24 overnight network (bones
        438-444) correctly omits dock-side alleys from spread, consistent
        with thinned state. Unchanged from cycle 2.
      why: >
        s02 open state has no studio-file anchor for the thin cluster; s02
        screen-writer may treat cluster as full-density.
      criteria: ~

    - id: fault-005
      type: flag
      what: >
        The maester-to-oc-broken-maester slug transition naming moment
        (beat 16) is not anchored by a single explicitly-designated
        log-write bone. Candidate bones remain 292-294, 299-301, or
        311-313. Bones 513-514 (the beetles relay the cold candle / the
        beetles relay oc-broken-maester) are at beat 18 territory and do
        not resolve the beat-16 naming ambiguity. Unchanged from cycle 2.
      why: >
        Screen-writer may misplace the naming entry across the three
        candidate log-write sequences, producing a prose pass where the
        slug change and the explicit log characterization appear in the
        wrong episode.
      criteria: ~

    - id: fault-007
      type: flag
      what: >
        Slug "the arrival" at bones 164-165 only. No plan-text anchor.
        Unchanged from cycle 2.
      why: >
        One-time anonymous slug with no narrative anchor risks
        screen-writer elaboration or omission error.
      criteria: ~

    - id: fault-008
      type: flag
      what: >
        Slug "the dogs" at bone 12 only. No exit bone; no relay bone;
        no beat-1 plan reference. Unchanged from cycle 2.
      why: Low risk. One-time environmental slug with no narrative
        function after bone 12.
      criteria: ~

    - id: fault-009
      type: flag
      what: >
        Apothecary owner named at bones 363-366 only; unnamed in all
        other oc-broken-maester apothecary traversals. Unchanged from
        cycle 2.
      why: >
        Slug inconsistency across recurring-presence character.
        Editor-facing advisory.
      criteria: ~

    - id: fault-012
      type: flag
      what: >
        Bones 363-366 (second clerk and apothecary owner, beat 20):
        beetle presence established at bone 350 but no speech-relay bone
        covers the spoken dialogue content of the clerk-owner
        conversation. Unchanged from cycle 2.
      why: >
        The owner naming Taylor is load-bearing for beat 20's
        file-completion plot function. Screen-writer must interpolate the
        relay without bone guidance, risking POV violation at prose pass.
      criteria: ~

    - id: fault-013
      type: flag
      what: >
        Bones 465-469 (oc-tanner-elder in writing room, beat 25):
        interior actions of writing room rendered without POV anchor.
        The flies relay at bone 471 covers middleman exit from junction,
        not writing room interior. Unchanged from cycle 2.
      why: >
        Beat 25 plan: Taylor "cannot observe what is written or where it
        goes." The bones narrate the interior act as observable events.
        Minor FAULT-POV-LEAK; bones should render only
        junction-observable actions from Taylor's POV.
      criteria: ~

    - id: fault-014
      type: flag
      what: >
        Bones 404-411 (oc-broken-maester at eastern-quarter market stall,
        beat 22): movement tracked via beetle relay (bones 403, 412) but
        no speech-relay bone covers the spoken dialogue (bones 405-409).
        Unchanged from cycle 2.
      why: >
        The spoken content (maester sharpening through inquiry about
        insect anomalies) is plot-significant. Screen-writer may render
        it as Taylor-accessible (POV violation) or leave it too thin.
      criteria: ~

    - id: fault-017
      type: flag
      what: >
        Bone 509 ("the flies relay the carter") introduces a new slug
        ("the carter") without prior establishment. Carter subsequently
        appears at bones 501-502, 508, 510. Beat 10 plan text does not
        name the carter. Unchanged from cycle 2.
      why: >
        Moderate risk if screen-writer interprets the carter as a named
        recurring character the plan does not mention; low risk if
        treated as anonymous chain node.
      criteria: ~

    - id: fault-018
      type: flag
      what: >
        Bone 507 ("taylor-hebert-flea-bottom faces the Red Keep"):
        "faces the Red Keep" at loc-flea-bottom-base may render an
        internal orientation as a physical act, which faults
        FAULT-FORM-INTERIORITY under the schema. The Red Keep is not
        visible from street level in Flea Bottom's alleys. Unchanged
        from cycle 2.
      why: >
        If "faces the Red Keep" is interiority rendered as physical
        action, it violates the no-interiority rule at proto-line level.
        The plan's framing ("the log does not record the distance")
        suggests this beat is about what Taylor does NOT write — an
        absence-of-action, which is not a valid proto-line subject.
      criteria: ~

    # ── PASSES CONFIRMED FROM CYCLE 2 ────────────────────────────────────────

    - id: fault-001
      type: pass
      what: >
        Lord's-man wage-claim reachability. Resolved via elder relay
        (bones 430-431). Beat 23 plan mechanism confirmed. Unchanged.
      why: ~
      criteria: ~

    - id: fault-006
      type: pass
      what: >
        Non-monotonic file-position IDs. Carry-forward schema decision:
        not a fault per schema (IDs are stable identifiers; stitcher
        walks citation order, not numeric order). Unchanged.
      why: ~
      criteria: ~

    - id: fault-010
      type: pass
      what: >
        Duplicate "the flies relay the messenger" at bones 461/462.
        Bone 462 is absent (ID gap confirmed in cycle 2). Resolved.
      why: ~
      criteria: ~
```

## Summary

Re-fire scope: two targeted checks.

**ID 515 deletion (refire-001): PASS.** The bare log-write bone is absent. The log-state chain (close at 328, no log operations at 513-514, open at 340) is clean. Fault-015 from cycle 2 is resolved with no secondary damage.

**ID 513 vigil-signal revision (refire-002): PASS.** "The beetles relay the cold candle" is physically legible as a relay event. The cold candle is a thermally distinct physical object within beetle-coverage territory, consistent with the relay pattern throughout the bones. The bone does not render interiority. The vigil-end signal (beat 17) is now POV-consistently anchored. The prior cycle-2 flag-016 observation about bones 513-514 not serving as relay anchors for the clerk scene remains advisory — unchanged in this re-fire.

**Carry-forward fault-011 (POV-leak, bones 71-77): FAULT — Phase 6 residual.** Confirmed unchanged. Screen-writer REGEN-ADD deferred due to dispatch budget. Acknowledged by dispatch as carry-forward; no action expected before Phase 6.

All other cycle-2 findings carry forward without change. No new faults introduced by the two targeted edits.
