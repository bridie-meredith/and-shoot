# Season Continuity Audit — s01 Pass S4
# schema: schemas/audit-report.schema.md

SEASON-CONTINUITY-FAIL

```yaml
audit:
  scope: season
  target: s01
  timestamp: 2026-05-11
  findings:

    # ── SWEEP 1: REACHABILITY ────────────────────────────────────────────────

    - id: fault-001
      type: escalate
      what: >
        Season-end reachability requires two records in existence: (1) village
        wage-claim in lord's-man record (beat 23 / season-s01-plan.md structural
        commitments) and (2) Hand's-apparatus file (beat 25). The Hand's file is
        covered by bones 466-470 (elder writes/seals account, middleman exits).
        The village wage-claim record is NOT traversed in the bones. Beat 13
        (bones 246-260) shows Taylor making partial payment to oc-tanner-father
        but contains no bone showing the lord's-man receiving or recording the
        wage claim. Beat 23 (bones 424-436) shows oc-tanner-father reporting
        to oc-tanner-elder that the claim is on customary record with the lord's
        man — but no bones exist showing the lord's-man actually receiving and
        recording that claim. The only lord's-man record-writing sequence in the
        bones (75: "the lords-man writes the entry") is the beat-5 "fever-return,
        behavior irregular" entry, not a wage claim. Season-end state requires
        the wage claim to be a lord's-man record fact; the bone aggregate does
        not traverse that delta.
      why: >
        The season chunk's terminal state explicitly requires "village wage claim
        in lord's-man record" as one of the two season-close records. Without a
        bone sequence where the lord's-man receives and records the wage claim,
        Phase 7 episode-boundary write-out cannot assign this event to any
        episode, and the season's structural commitment (village-claim arc
        "has an instrument" per beat 13, formalizes to formal record per beat 23)
        is unreachable from the existing aggregate. The season-end state cannot
        be achieved from the bones as written.
      criteria: >
        The bones must include a sequence in which the lord's-man (or a
        lord's-man-equivalent agent of the feudal record apparatus) receives the
        wage claim and writes it into a record — either during the beat-13 or
        beat-23 section — such that the season-close state "village wage claim
        in lord's-man record" is traversed by at least one bone. The sequence
        does not need to be observed directly by Taylor if insect relay is
        present, but the recording event must exist in the aggregate.

    - id: fault-002
      type: flag
      what: >
        Range expansion traverse (300m → 330m → 400m → 500m → 600m across beats
        11, 14, 19, 24). Each expansion cycle is represented by the pattern
        "spread bones + perimeter walk + writes + headache" (e.g., bones 209-230
        for beat 11, bones 266-278 for beat 14, bones 344-359 for beat 19,
        bones 438-453 for beat 24). No bone in any of these cycles carries an
        explicit range marker or notation. The plan states log entries record
        "new perimeter, date, ambient conditions, headache duration" and "specific
        new geography" — this notational content is expected at the prose layer
        (screen-writer fills log-write bones with specific range values), not
        necessarily at bone level.
      why: >
        If Phase 7 episode boundaries are written without explicit range markers
        in the bones, screen-writer may produce log-write prose (bones 223-224,
        271-272, 352-353, 446-447) that omits or misplaces the specific range
        values. The bones as structured depend on the prose layer to carry the
        expansion amounts. This is acceptable if the convention is understood,
        but poses a documentation-gap risk. Not a structural block.
      criteria: ~

    # ── SWEEP 2: STATE ───────────────────────────────────────────────────────

    - id: fault-003
      type: flag
      what: >
        The log (Taylor's notebook) first appears at bone 21
        ("taylor-hebert-flea-bottom opens the log") while Taylor is still at
        loc-tanner-village. The actor state file for taylor-hebert-flea-bottom
        shows inventory: [] and research_log_active: false (season-start state).
        The log is used continuously from bone 21 through bone 494 (final log
        close) and is never dropped or lost. However, the log's acquisition is
        not recorded in any state file or prop card — there is no bone showing
        Taylor obtaining the log, and no state update recording its entry into
        inventory. Per memory rules ("Nothing changes without being recorded"),
        the log's creation or first-use constitutes a prop state change that
        should be recorded.
      why: >
        The log is load-bearing across the entire season (used at every beat;
        plan describes it as the primary documentation instrument; s03 plan
        references "this entry will not exist in the log by s03"). If the log's
        existence is not grounded in a state record, future audits (episode-wrap
        audits, s02 continuity checks) have no anchor for log continuity. Minor
        in s01 since the log is used consistently; higher risk in cross-season
        continuity.
      criteria: ~

    - id: fault-004
      type: flag
      what: >
        Dock-side insect cluster thin state (bone 389: "the dock-side cluster
        thins") is stated once and is correctly not re-spread in subsequent beat
        sequences (beat 24 overnight network at bones 438-444 uses wasps at Fish
        Gate margin rather than dock-side alleys, consistent with thinned cluster).
        However, the thinned state is noted only in bone 389 and is not carried
        in any state file or studio record. The cluster's thin state is
        plot-relevant ("will need weeks to reseed" per beat 21 plan) and persists
        to season close.
      why: >
        If s02 bones are authored without a recorded thin state for the dock-side
        cluster, screen-writer may inadvertently treat the cluster as full-density
        at s02 open, contradicting the s01 season-close state. Low risk if s02
        planning explicitly notes the thin state; moderate risk if it does not.
      criteria: ~

    - id: fault-005
      type: flag
      what: >
        The maester-to-oc-broken-maester slug transition happens between bone 286
        ("the maester speaks to the visitor") and bone 305 ("oc-broken-maester
        exits the apothecary"). Bones 292-294 and 299-301 are log open/write/close
        sequences that occur between these two appearances — one of these log
        entries is likely the naming moment per beat 16. Bone 311-313 is another
        log entry immediately after the first oc-broken-maester appearance. No
        bone explicitly marks the moment of Taylor's recognition or slug
        reassignment. The transition at plan beat 16 should be anchored by a
        specific log-write bone that names the subject.
      why: >
        The plan (beat 16) specifies: "logged as 'subject: chain-stripped maester,
        eastern quarter, consistent high-density notation activity.'" If the
        naming log-write bone is ambiguous (could be any of bones 292-294,
        299-301, or 311-313), screen-writer may misplace the naming entry.
        The slug change without explicit anchor also makes editor continuity
        checking harder.
      criteria: ~

    # ── SWEEP 3: REFERENCE / ORPHAN SLUGS ───────────────────────────────────

    - id: fault-006
      type: fault
      what: >
        The bones file header states "Continuous flat numbering 1..N" but the
        aggregate contains multiple out-of-sequence high-number IDs inserted
        between low-numbered bones: 495 (between bones 85 and 86), 504 (between
        bones 85 and 86 region), 496 (between bones 298 and 299), 497 (between
        bones 356 and 357), 498 (between bones 450 and 451), 499 (between bones
        450 and 451 region), 500 (between bones 202 and 205 region), 501 (between
        bones 500 and 205), 502 (between bones 501 and 205), 503 (between bones
        417 and 420), 505 (between bones 274 and 276), 506 (between bones 131
        and 132), 507 (between bones 453 and 454 region), 508 (between bones
        245 and 501 region). These IDs (495-508) appear in the file body at
        positions inconsistent with their numeric values.
      why: >
        Phase 7 writes episode boundaries mechanically from bone IDs assuming
        1..N flat continuous numbering. Out-of-sequence IDs corrupt this
        mechanical write-out: a Phase 7 pass treating IDs as ordered will
        misplace these bones, producing episode boundaries that do not correspond
        to the narrative sequence. Additionally, "Continuous flat numbering 1..N"
        is a stated schema requirement (bones file header, line 3); the aggregate
        violates it.
      criteria: >
        The out-of-sequence bones (IDs 495-508) must be renumbered to fit their
        correct narrative position in the 1..N flat sequence, or the bones must
        be confirmed as intentionally positioned and the Phase 7 write-out
        algorithm confirmed to use file-position order rather than numeric-ID
        order. If file-position order is the intended read, the header comment
        must be corrected to reflect that ordering convention.

    - id: fault-007
      type: flag
      what: >
        Slug "the arrival" appears at bones 164-165 only
        ("the arrival enters the junction" / "taylor-hebert-flea-bottom pivots
        toward the arrival"). Beat 9 plan text describes the family visit and
        Taylor's half-second strategic-scan tell, but does not name or reference
        "the arrival" as a distinct character or plot element. The slug is
        anonymous, appears once, has no resolution or reappearance.
      why: >
        A one-time unnamed slug with no plan-text anchor risks being interpreted
        by screen-writer as a significant character requiring elaboration, or
        conversely omitted as an error. If "the arrival" is intended as a generic
        background-person trigger for Taylor's tell, that function should be
        clarified. If it is an unintended bone, it should be removed.
      criteria: ~

    - id: fault-008
      type: flag
      what: >
        Slug "the dogs" appears at bone 12 only ("the dogs enter the yard").
        No further reference across 494 subsequent bones. Not mentioned in beat 1
        plan text. The dogs enter the yard as a single action and are not used
        again — no relay, no behavioral significance, no exit bone.
      why: >
        One-time environmental slug with no narrative anchor. Low risk; noted
        per bias-when-in-doubt instruction.
      criteria: ~

    - id: fault-009
      type: flag
      what: >
        The apothecary owner appears as a named slug at bones 363-366 (beat 20,
        second clerk scene) but is not named in other scenes where oc-broken-maester
        passes through the apothecary ground floor (bones 305, 400-401, 413-414).
        In those bones, oc-broken-maester enters/exits/ascends/descends without
        any reference to the apothecary owner. The owner is structurally present
        (runs the shop oc-broken-maester lives above) but receives a slug only
        in the intelligence-contact scene.
      why: >
        Slug inconsistency: a recurring-presence character is named only when
        narratively convenient. Screen-writer may inconsistently render the
        owner's presence or absence across the episodes containing these bones.
        Editor-facing advisory.
      criteria: ~

    - id: fault-010
      type: flag
      what: >
        Bones 461 and 462 have identical content: "the flies relay the messenger"
        (beat 25 messenger sequence). This appears to be a duplicate bone entry
        rather than two distinct relay actions.
      why: >
        Duplicate bones produce redundant prose lines at screen-writer pass, and
        may cause phase 7 episode-boundary logic to count this as two distinct
        beats. If both are intentional (e.g., relay of departure and relay of
        route), the bone content should distinguish them.
      criteria: ~

    # ── SWEEP 4: POV ─────────────────────────────────────────────────────────

    - id: fault-011
      type: fault
      what: >
        Bones 71-77 (lord's man record sequence, beat 5): "the lords-man enters
        the village / speaks to the reeve / the reeve speaks to the lords-man /
        the lords-man opens the record book / the lords-man writes the entry /
        the lords-man closes the record book / the lords-man exits the village."
        This entire sequence proceeds with no insect relay bone. At this point
        in the season (bones 1-92 are all in the tanner-village phase), Taylor's
        insect network has been established only for the tanner-family yard
        perimeter (bones 25-34: flies/beetles/wasps spreading the yard perimeter
        in beat 2). There is no bone showing insects spreading through the wider
        village to cover the location where the lord's man speaks with the reeve
        and writes his record. This sequence is narratively rendered as observed
        fact without a POV anchor.
      why: >
        The season plan is explicit: "One POV: Taylor (taylor-hebert-flea-bottom)."
        Dispatch rules classify this as FAULT-POV-LEAK. The lord's-man's record
        entry (bone 75: "writes the entry") is the opening of the Hightower-file
        arc — one of the two season-defining records. Its appearance as
        unanchored narration rather than Taylor-observed event is a structural
        POV violation at a load-bearing beat.
      criteria: >
        Bones 71-77 must be preceded by (or contain) an insect relay anchor
        establishing Taylor's coverage of the location where the lord's man and
        reeve interact. Alternatively, the sequence must be restructured so that
        Taylor learns of the lord's-man visit and record entry through a
        post-hoc relay or through oc-tanner-elder's report — with appropriate
        relay or mediated-knowledge bones replacing the currently unanchored
        direct-narration sequence.

    - id: fault-012
      type: flag
      what: >
        Bones 363-366 (second clerk and apothecary owner, beat 20): the clerk
        names Taylor's behavioral profile and the owner names Taylor
        — the plot-significant speech content. The flies relay at bones 371-372
        covers the doorframe and the clerk's exit only; no relay bone covers the
        spoken content of bones 363-366. Bone 350 established beetles on the
        apothecary ground floor ("the beetles spread the apothecary ground floor")
        in the winter-onset network, so insect presence exists. However, no
        explicit speech-relay bone (comparable to bone 287: "the beetles relay
        the register" in the visitor scene) is present for the clerk-owner
        conversation.
      why: >
        Taylor's log at bones 373-374 records this as "second lord's-apparatus
        intelligence contact, eastern-quarter apothecary" — she clearly knows
        something happened. But the bones do not show how she accessed the spoken
        content (her behavioral profile being named, her identity being named by
        the owner). Without a speech-relay bone, this is partial FAULT-POV-LEAK:
        the insect presence is established but the speech-relay is missing. The
        omission matters because the plan states "The owner names her; the clerk
        records and leaves" — Taylor's awareness of being named is load-bearing
        for the file-completion beat.
      criteria: ~

    - id: fault-013
      type: flag
      what: >
        Bones 465-469 (oc-tanner-elder in writing room, beat 25): "oc-tanner-elder
        exits the junction / enters the writing room / writes the account / seals
        the account / the middleman takes the sealed account." These actions occur
        in "the writing room" — a location not previously established in the bones
        or the location card inventory. No insect relay bone covers the writing
        room interior. The flies relay at bone 471 covers "the junction departure"
        (after the middleman exits) — not the writing room. The plan states Taylor
        "cannot observe what is written or where it goes," which is consistent
        with the lack of content relay, but the physical act of writing and sealing
        (bones 467-468) and the middleman taking the account (bone 469) are
        rendered as observed fact without a POV anchor for the writing room.
      why: >
        The writing room is an unestablished location appearing only in bones
        465-470. If Taylor cannot access it (consistent with plan), the bones
        narrating interior events there without a relay anchor are a mild
        FAULT-POV-LEAK. The plan's framing ("observes messenger and elder's
        response but cannot observe what is written") suggests Taylor knows the
        elder responded (observable at junction) but not the content — the bones
        should render only the junction-observable actions from Taylor's POV,
        not the writing-room interior.
      criteria: ~

    - id: fault-014
      type: flag
      what: >
        Bones 404-411 (oc-broken-maester at market stall, beat 22): oc-broken-maester
        speaks with the stall-keeper about "insect coordination anomalies in
        Flea Bottom-adjacent alleys" (per plan beat 22). Positional relay bones
        exist (bone 403: "the beetles relay the footfall"; bone 412: "the beetles
        relay oc-broken-maester") covering movement tracking. No speech-relay
        bone covers the spoken content of bones 405-409. The spoken content —
        oc-broken-maester raising insect anomalies with the stall-keeper — is
        plot-significant (it establishes the maester is actively investigating
        Taylor's network before she understands the implications). The bones
        render this dialogue without an explicit speech-relay.
      why: >
        The plot-critical element of beat 22 is that the maester's pen-scratch
        continues six hours past usual stopping point after the market visit
        (bone 416-417: "the beetles relay the onset / the beetles relay the
        cessation"). If the maester's spoken inquiry at the stall is not
        relay-anchored, screen-writer may render it as Taylor knowing the content
        of the conversation — which would be a POV violation — or may leave the
        conversation content entirely implied, which may be too thin for a beat
        the plan describes as the maester "sharpening" through. Editor-facing
        advisory.
      criteria: ~
```
