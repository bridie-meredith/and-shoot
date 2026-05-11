# Season Continuity Audit — s01 Pass S4 — CYCLE 2
# schema: schemas/audit-report.schema.md
# Supersedes: season-s01-pass-S4-continuity-cycle1-archive.md
# New bones audited: 509, 510, 511, 512, 513, 514, 515, 516, 517

SEASON-CONTINUITY-FAIL

```yaml
audit:
  scope: season
  target: s01
  timestamp: 2026-05-11
  cycle: 2
  findings:

    # ── CARRY-FORWARD DISPOSITIONS (cycle-1 findings re-checked) ─────────────

    - id: fault-001
      type: pass
      what: >
        Cycle-1 escalation on lord's-man wage-claim reachability. Carry-forward
        decision per dispatch: "lord's-man records village wage-claim event
        happens outside Taylor's range; the bones correctly elide off-stage
        events. Reachability holds via the elder's relay to Taylor (bones 430-431)."
        Beat 23 plan text confirms mechanism: tanner-father states claim is on
        customary record with the lord's man; elder routes information to Taylor
        (bones 424-431). Season structural commitment "externalizes into lord's-man
        record (beat 23)" is delivered via relay, not direct observation. Elision
        of off-stage recording event is correct given single POV constraint.
      why: ~
      criteria: ~

    - id: fault-002
      type: flag
      what: >
        Range expansion traverse (300m → 330m → 400m → 500m → 600m) across beats
        11, 14, 19, 24 carries no explicit range-value notation at bone level.
        Bones 223-224, 271-272, 352, 446 are the log-write bones where range
        values must appear at screen-writer prose pass. No change from cycle 1.
      why: >
        Screen-writer dependency: if these log-write bones are expanded without
        the specific range values in the beat plan, the numeric progression may
        be omitted or inconsistent. Not a structural block; advisory for
        screen-writer briefing.
      criteria: ~

    - id: fault-003
      type: flag
      what: >
        Taylor's log first appears at bone 21 while actor state file shows
        inventory: [] and research_log_active: false. No bone records the log's
        acquisition; no state update records it entering inventory. No change
        from cycle 1.
      why: >
        Cross-season continuity risk: s02 audits have no state-file anchor for
        log existence. Minor in s01 given consistent use from bone 21 onward.
      criteria: ~

    - id: fault-004
      type: flag
      what: >
        Dock-side insect cluster thin state (bone 389) is not recorded in any
        state file or studio record. Beat 24 overnight network (bones 438-444)
        correctly omits dock-side alleys from spread, consistent with thinned
        state. No change from cycle 1.
      why: >
        s02 open state has no studio-file anchor for the thin cluster; s02
        screen-writer may treat cluster as full-density.
      criteria: ~

    - id: fault-005
      type: flag
      what: >
        The maester-to-oc-broken-maester slug transition is not anchored by a
        single explicitly-designated log-write bone. The naming log-write (beat 16)
        could be any of bones 292-294, 299-301, or 311-313. New bones 513-514
        (cycle 2) add "the beetles relay the base room" / "the beetles relay
        oc-broken-maester" at position after time-skip 329, but these are at beat
        18 territory (clerk scene), not at the beat-16 naming moment. The
        ambiguity at the naming transition (beats 15-16, bones 285-313 window)
        remains unresolved.
      why: >
        Screen-writer may misplace the naming entry across the three candidate
        log-write sequences, producing a prose pass where the slug change and the
        explicit log characterization ("subject: chain-stripped maester...") appear
        in the wrong episode.
      criteria: ~

    - id: fault-006
      type: pass
      what: >
        Cycle-1 fault on out-of-sequence IDs (495-508, now extended to 495-517).
        Carry-forward decision per dispatch: "Re-ordering preserves IDs; the
        stitcher walks IDs in citation order, not numeric order." Schema
        proto-line.schema.md line 97 confirms: "Re-ordering preserves IDs; the
        stitcher walks IDs in citation order, not numeric order." Cycle-1 fault
        was a schema misreading. IDs are stable identifiers, not positional
        markers; file position determines stitch order. The bones file header
        comment "Continuous flat numbering 1..N" is descriptive of ID assignment
        (each ID is a unique positive integer assigned once and never reused),
        not a requirement that IDs appear in ascending file order.
        No fault.
      why: ~
      criteria: ~

    - id: fault-007
      type: flag
      what: >
        Slug "the arrival" at bones 164-165 only. No plan-text anchor. No change
        from cycle 1.
      why: >
        One-time anonymous slug with no narrative anchor risks screen-writer
        elaboration or omission error. If this is the new-arrival trigger for
        Taylor's strategic-scan tell (beat 9), the slug should be labeled
        "the new arrival" or "a stranger" to make its function legible.
      criteria: ~

    - id: fault-008
      type: flag
      what: >
        Slug "the dogs" at bone 12 only. No exit bone; no relay bone; no beat-1
        plan reference. No change from cycle 1.
      why: >
        One-time environmental slug with no narrative function after bone 12.
        Low risk.
      criteria: ~

    - id: fault-009
      type: flag
      what: >
        Apothecary owner named at bones 363-366 only; unnamed in all other
        oc-broken-maester apothecary traversals. No change from cycle 1.
      why: >
        Slug inconsistency across recurring-presence character. Editor-facing
        advisory.
      criteria: ~

    - id: fault-010
      type: pass
      what: >
        Cycle-1 flag on duplicate "the flies relay the messenger" at bones 461
        and 462. Cycle 2 check: bone 462 is absent from the file (ID 462 is
        skipped — the file shows bone 461 followed directly by bone 463). The
        duplicate was deleted in the form-fixer pass. Resolved.
      why: ~
      criteria: ~

    - id: fault-011
      type: fault
      what: >
        Bones 71-77 (lord's-man record sequence, beat 5): no insect relay anchor
        precedes or accompanies this sequence. Taylor's insects at this point
        cover the tanner-family yard perimeter only (bones 25-34); no spread
        bone covers the wider village or the location where the lord's man meets
        the reeve and writes his record. The sequence is narratively rendered as
        observed fact without a POV anchor. No change from cycle 1. New bones
        509-517 do not address this window (all new bones are in Flea Bottom
        beats 6-23).
      why: >
        Season plan: "One POV: Taylor (taylor-hebert-flea-bottom)." Beat 5 is
        the Hightower-file arc opening — one of the two season-defining records.
        An unanchored direct-narration sequence at this structurally load-bearing
        beat is a FAULT-POV-LEAK. The lord's-man writing the file entry (bone 75)
        is the event that opens the arc; if it is rendered as omniscient narration
        rather than Taylor-accessible observation, the POV contract breaks at
        the arc's inception.
      criteria: >
        The beat-5 lord's-man sequence must either (a) be preceded by an insect
        relay anchor establishing Taylor's village coverage sufficient to reach
        the reeve-lord's-man meeting location, or (b) be restructured so the
        lord's-man visit and record entry reach Taylor post-hoc — via the reeve
        mentioning it, or via later relay — with bones replacing the unanchored
        sequence. The recording event (bone 75 equivalent) may be elided as
        off-stage (per the carry-forward decision on fault-001) provided the
        information reaches Taylor through a POV-consistent channel.

    - id: fault-012
      type: flag
      what: >
        Bones 363-366 (second clerk and apothecary owner, beat 20): beetle
        presence established at bone 350 (apothecary ground floor, winter-onset
        network) but no speech-relay bone covers the spoken dialogue content
        of the clerk-owner conversation. Flies relay at bones 371-372 covers
        the doorframe and the clerk's exit, not the spoken content. No change
        from cycle 1.
      why: >
        Taylor's log at bones 373-374 records awareness of the contact. The
        mechanism by which she accessed the spoken content (her profile named,
        her identity named) is not shown in the bones. Screen-writer must
        interpolate the relay without bone guidance, risking POV violation at
        the prose pass. The owner naming Taylor is load-bearing for beat 20's
        "file-completion" plot function.
      criteria: ~

    - id: fault-013
      type: flag
      what: >
        Bones 465-469 (oc-tanner-elder in writing room, beat 25): interior
        actions of writing room rendered without POV anchor. The flies relay at
        bone 471 covers middleman exit from junction, not writing room interior.
        No change from cycle 1.
      why: >
        Beat 25 plan: Taylor "cannot observe what is written or where it goes."
        The bones narrate the interior act (writes account, seals, middleman
        takes) as observable events. Minor FAULT-POV-LEAK; the plan's framing
        is consistent with eliding interior content, but the bones should render
        only junction-observable actions from Taylor's POV.
      criteria: ~

    - id: fault-014
      type: flag
      what: >
        Bones 404-411 (oc-broken-maester at eastern-quarter market stall, beat 22):
        movement tracked via beetle relay (bones 403, 412) but no speech-relay
        bone covers the spoken dialogue (bones 405-409 — stall-keeper and maester
        discussing insect coordination anomalies). No change from cycle 1.
      why: >
        The plot-significant element of this exchange is that the maester is
        actively investigating Taylor's network. If the spoken content is not
        relay-anchored, screen-writer may render it as Taylor knowing what was
        said (POV violation) or leave the conversation entirely implied (too
        thin for a beat where the plan specifies the maester "sharpening" through
        an inquiry about insect anomalies).
      criteria: ~

    # ── NEW FINDINGS — CYCLE 2 (bones 509-517) ───────────────────────────────

    - id: fault-015
      type: fault
      what: >
        Bone 515 ("taylor-hebert-flea-bottom writes the entry") inserted at
        file position after bones 513-514 (the beetles relay the base room /
        the beetles relay oc-broken-maester) and before bone 330 (clerk enters
        market-side junction). The preceding log-close is bone 328
        ("taylor-hebert-flea-bottom closes the log"); the subsequent log-open
        is bone 340 ("taylor-hebert-flea-bottom opens the log"). Bone 515 is a
        log-write bone without a matching log-open before it or log-close after
        it. The established pattern throughout the aggregate is invariant:
        every log-write bone is bracketed by an open (opens the log) and a
        close (closes the log) in the same local sequence. Bone 515 violates
        this pattern.
      why: >
        Screen-writer pass reads the log open/write/close triple as the prose
        unit for a log entry. A bare write bone without brackets is ambiguous:
        screen-writer may (a) treat it as a second write within the prior
        log-open/close sequence (impossible — 328 already closed), (b) render
        it as an undocumented entry without log-frame prose, or (c) attempt to
        insert a phantom open/close pair. Any of these produces either a prose
        anomaly or a continuity break (the log would be open and then closed
        again at 328 before 515 writes into it). The structural triple pattern
        is load-bearing across the entire season; one broken triple at a new
        bone is a schema-form fault.
      criteria: >
        Bone 515 must be either (a) embedded within a proper open/write/close
        triple (a new log-open bone before 515 and a new log-close bone after
        515, forming a standalone entry for the beetles-relay-oc-broken-maester
        observation), or (b) deleted if the observation recorded in 515 is
        already captured by the log sequence at bones 326-328. The fix must
        not change any existing ID.

    - id: fault-016
      type: flag
      what: >
        New bones 513-514 inserted at file position after time-skip 329 and
        before bone 330 (clerk enters market-side junction, beat 18).
        Bone 513: "the beetles relay the base room."
        Bone 514: "the beetles relay oc-broken-maester."
        At beat 18 (the Hightower-apparatus clerk scene at the junction), the
        range is 400m (expanded at beat 14). Beat 19 plan text states "broken
        maester's full vertical (upper room + ground-floor apothecary) now
        inside the radius" — meaning at beat 18, only the upper room is inside
        the 400m radius (confirmed by beat 14: "maester's upper room remains
        inside the radius with margin to spare"). "The beetles relay the base
        room" is plausible (Taylor's own quarters at loc-flea-bottom-base).
        "The beetles relay oc-broken-maester" at this position implies beetle
        coverage of oc-broken-maester, which should be via upper-room colony
        only. The bone is consistent with the range but its narrative function
        at this position (between the oc-tanner-mother visit at bones 315-324
        and the clerk at bones 330-337) is unclear — it does not serve as a
        relay anchor for the clerk scene (clerk is at the market-side junction,
        not the base room or apothecary).
      why: >
        Bone 513-514 do not provide POV coverage for the clerk scene that
        follows them. If they are intended as a continuous monitoring beat
        (Taylor checking in on oc-broken-maester between the mother visit and
        the clerk arrival), their narrative position is correct but their
        function as POV anchors for the clerk sequence is nil. Screen-writer
        must understand these bones are ambient monitoring, not relay anchors
        for the clerk exchange. Ambiguity risk for screen-writer phase.
      criteria: ~

    - id: fault-017
      type: flag
      what: >
        New bone 509 ("the flies relay the carter") inserted at file position
        immediately after bone 195 (taylor-hebert-flea-bottom enters
        loc-flea-bottom-base) and before time-skip 199. The carter is a new
        slug introduced here without prior establishment. The carter subsequently
        appears as the interlocutor at bones 501-502, 508, 510 (oc-tanner-elder
        pauses / speaks to the carter / wasps relay the pass / carter exits
        junction). The beat 10 plan text describes Taylor routing weather-pattern
        data and Watch-movement timing through the whisper chain without
        identifying the source — no carter is named. "The carter" is a new
        functional slug in the beat-10 whisper-chain bones.
      why: >
        The carter slug is introduced via a relay bone (509) before the
        carter's action bones (500-510 cluster). The relay correctly anchors
        Taylor's awareness of the carter's presence. However the carter as a
        functional element of the whisper chain is not referenced in the beat
        10 plan text — the plan describes anonymous information routing through
        chain nodes. The carter may be a legitimate instantiation of a "chain
        node" (screen-writer to flesh out), or may be a new character who
        requires a plan-text anchor to be narratively grounded. Low risk
        if screen-writer treats the carter as an unnamed relay node; moderate
        risk if screen-writer interprets the carter as a named recurring
        character the plan does not mention.
      criteria: ~

    - id: fault-018
      type: flag
      what: >
        New bone 507 ("taylor-hebert-flea-bottom faces the Red Keep") inserted
        at file position after bone 453 (log close for beat 24 entry) and before
        time-skip 454 (which opens the beat 25 messenger sequence). Beat 24 plan
        text: "The Red Keep's outermost approach is still four hundred meters
        beyond her current ceiling. The distance is known; the math is in her
        log. The log does not record the distance to the Red Keep." The bone
        renders Taylor facing the Red Keep as a physical action. "Faces" is a
        licensed transitive form (per schema: `faces <X>` is the transitive
        recasting of `turns to <X>`). However, "the Red Keep" at 400m beyond
        Taylor's 600m ceiling is not in Taylor's physical line of sight from
        loc-flea-bottom-base in a way that constitutes a discrete observable
        act — the Red Keep is not visible from street level in Flea Bottom's
        alleys at this geography. The bone may be rendering an internal
        orientation (Taylor thinking toward the Red Keep) as a physical act,
        which faults FAULT-FORM-INTERIORITY under the schema.
      why: >
        If "faces the Red Keep" is interiority rendered as physical action, it
        violates the no-interiority rule at the proto-line level. The plan
        text's framing ("the log does not record the distance") suggests this
        beat is about what Taylor does NOT write, which is by definition
        interiority or absence-of-action — neither of which is a valid
        proto-line subject. If the bone is intended as a physical orientation
        gesture (Taylor turns body toward the Red Keep's general direction),
        the spatial implausibility from Flea Bottom alleys makes this a
        marginal form fault. Screen-writer may render this as internalized
        awareness, compounding the interiority problem.
      criteria: ~
```
