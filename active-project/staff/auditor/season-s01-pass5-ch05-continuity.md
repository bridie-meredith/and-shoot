audit:
  scope: episode
  target: chapter-05 (proto-lines — pass 5 continuity, post-fixer)
  timestamp: 2026-05-07
  narrator: septon-rowan
  interlude: true
  file_level: FAIL
  fault_count: 3
  flag_count: 3

  # ── SUMMARY ──────────────────────────────────────────────────────────────────
  # Three faults, three flags. One fault is a prop-location break (ledger at ID 85).
  # One fault is a location-transit break (cottage → chancel with no exit beat).
  # One fault is a narrative-gap coherence break (the intercession itself is entirely voided,
  # leaving no surviving spine signal for the chapter's load-bearing dramatic event).
  # Flags cover a duplicate act pair, a POV-subject edge, and the gap-70→72 comprehension beat.
  # The Plumm deputization worldbuilding patch is honored: no fault there.

  findings:

    # ── FAULT-CONTINUITY ─────────────────────────────────────────────────────

    - id: FAULT-CONTINUITY-001
      type: fault
      what: >
        ID 85 — "septon-rowan touches the ledger" — in the sept yard during the denouement
        (IDs 75–88). The septon's ledger was last physically handled in the cottage at IDs 13–15
        (opened, pages turned, closed). No beat shows Rowan taking the ledger out of the cottage.
        The prop he carries to and from Harrenhal is the travel pack (IDs 9, 86). The ledger is a
        fixed cottage prop per loc-harrenhal-sept-environs. No chain-of-custody beat transfers it
        to the yard.
      why: >
        Rowan cannot touch an object in location A (sept yard) when the object's last recorded
        position is location B (cottage interior) and no transit beat exists. If the ledger is used
        as a closing emotional beat — Rowan touching it as he prepares to leave or as he addresses
        Taylor — that beat collapses unless the ledger is present in the yard. Either the ledger
        must travel to the yard via an explicit carry beat, or ID 85 must use a prop that is
        actually in the yard at this point.
      criteria: >
        ID 85 must either (a) be preceded by a beat showing Rowan carrying the ledger from the
        cottage to the yard, establishing chain of custody, or (b) be recast to reference a prop
        that is present in the yard without a missing transit beat.

    - id: FAULT-CONTINUITY-002
      type: fault
      what: >
        Location-transit gap between ID 15 and ID 20. ID 15: "septon-rowan closes the ledger" —
        Rowan is inside the septon's cottage. ID 20: "septon-rowan enters the chancel" — Rowan is
        now inside the sept nave/chancel. The voided IDs 16–19 covered the exits required to move
        between these two distinct structures. The cottage and the sept are separate buildings at
        loc-harrenhal-sept-environs. At minimum: Rowan exits the cottage, crosses the yard, enters
        the sept, enters the chancel. The gap (four voided IDs) had content that bridged this
        transit; that content is gone. ID 20 is now unreachable from ID 15 without an exit beat.
      why: >
        Rowan cannot be inside the chancel (ID 20) if the last recorded position was inside the
        cottage (ID 15) with no intervening exit. This is a hard location-state break: the
        chapter's POV narrator teleports between two non-adjacent enclosed structures. Prose-writing
        pass cannot recover this from the spine alone — the transit is architecturally required.
      criteria: >
        At minimum one beat must exist between IDs 15 and 20 that places Rowan in transit — either
        an exit from the cottage or an entry into the sept — sufficient to establish he moved from
        one structure to the other. A single transit beat (e.g., "septon-rowan enters the sept")
        is the minimum viable bridge; cottage-exit is implied by the passage through the sept entry.

    - id: FAULT-CONTINUITY-003
      type: fault
      what: >
        Narrative coherence gap: IDs 35–40 (six consecutive voided IDs) cover the entire
        intercession exchange — Rowan's ecclesiastical claim, Plumm's reception of it, the
        escalation that causes Plumm to reach for the record book. The surviving spine around
        this gap is: ID 34 "ser-harwick-plumm speaks to septon-rowan" (Plumm's initial response
        to Rowan's arrival), then six voids, then ID 41 "septon-rowan speaks to ser-harwick-plumm"
        (Rowan's final appeal), then ID 42 "ser-harwick-plumm draws the record book." The chapter
        plan states: "He goes to the inspector and asserts ecclesiastical interest in the girl's
        welfare — a protective claim, not a formal guardianship. His intervention is sincere and
        has the opposite effect." The assertion itself — the load-bearing dramatic act of the
        chapter — has no surviving spine beat. What the prose-writing pass receives is: Plumm
        said something, six blank slots, Rowan said something, Plumm drew the book. The cause
        (Rowan's intercession) that produces the effect (Plumm's recording) is entirely absent
        from the spine.
      why: >
        The chapter's thematic and narrative purpose is explicitly "Rowan's failed intercession."
        The spine must carry at minimum one beat showing Rowan making the claim — not the full
        exchange, but the act that constitutes the intercession. Without it, the chapter's change
        statement ("Start: Taylor is the sole named figure. End: Rowan's name is in the report")
        has no causal spine anchor. The prose-writing pass cannot reconstruct causation from a
        blank gap; it can only fill in texture around a stated act. If the act is absent, the
        chapter's logic is suspended mid-air. This is not a shape question (how many beats); it
        is a minimum-viable-causation question.
      criteria: >
        At minimum one beat in the ID 35–40 range must record Rowan's ecclesiastical claim act —
        the specific speech-act or formal invocation that constitutes the intercession. One beat
        of the form "septon-rowan [asserts / names / invokes / presents] [the claim]" is sufficient
        to anchor causation. The full procedural exchange does not need to be restored; only the
        cause-act that triggers Plumm's recording response.

    # ── FLAGS ────────────────────────────────────────────────────────────────

    - id: flag-001
      type: flag
      what: >
        IDs 87–88 — "septon-rowan lowers the eyes" followed immediately by "septon-rowan drops
        the eyes." Two sequential beats by the same subject performing the same physical act class
        (downward eye movement). "Lowers" and "drops" both describe the eyes moving downward; no
        intervening beat separates them to make these two distinct moments.
      why: >
        The pair reads as a duplicate of the same beat rather than two distinct physical events.
        One of these IDs is likely a residual from a prior iteration that was not consolidated
        during fixer runs. At prose-writing, the writer will have two identical spine slots to
        fill with the same gesture, which either produces a stutter or requires a distinction
        that the spine does not supply. Not a blocking fault — prose can absorb this — but editor
        should flag for consolidation.

    - id: flag-002
      type: flag
      what: >
        ID 30 — "ser-harwick-plumm reaches the gatehouse postern" — Plumm is the subject in a
        Rowan-POV chapter. This line records Plumm's action (reaching the postern) rather than
        Rowan observing Plumm. The construction is physically observable — Rowan is approaching
        (ID 31) and can see Plumm's arrival/position — but the SVO form places Plumm as acting
        subject, not as observed object. This is a POV-consistency edge case, not a hard fault,
        because the form is standard for proto-lines (action inventory, not filtered perception).
        However: if the prose-writing pass requires strict Rowan-POV narration, ID 30 must be
        rendered as Rowan perceiving Plumm at the postern, not as a third-person omniscient
        statement of Plumm's movement.
      why: >
        Advisory for prose-writing pass only. No fixer dispatch needed. Note that IDs 69–70
        (Plumm passes the gate, pulls the gate shut) use the same construction and carry the same
        advisory.

    - id: flag-003
      type: flag
      what: >
        Gap between IDs 70 and 72 — one voided ID (71). Pass 3 shape audit (ch05-pass3-shape.md)
        explicitly identified this gap and required: "Add 1 beat — Rowan's comprehension that
        the record now contains two names where one was before." ID 71 is present as a gap slot.
        Whether a single voided ID is sufficient depends on whether the screen-writer or fixer
        has been directed to add a beat there. As of this audit, ID 71 is a blank gap in the
        file — no content has been added. The Pass 3 instruction is outstanding.
      why: >
        No blocking fault — the physical sequence (gate shuts → Rowan stops → Rowan turns) is
        reachable. But the Pass 3 shape directive to add a comprehension beat at ID 71 is not
        fulfilled. If this chapter proceeds to prose-writing without that beat, the narrative
        will lose the moment of Rowan's understanding that his intervention made things worse —
        the thematic hinge of the chapter. Advisory: confirm whether the Pass 3 addition
        directive has been executed or is still outstanding before prose-writing begins.

    # ── BOUNDARY CHECKS ──────────────────────────────────────────────────────

    # CH04 → CH05 boundary:
    #   Ch04 ends: taylor-hebert-westeros reaches the well (ID 99, Taylor-POV).
    #   Ch05 opens: septon-rowan enters the sept yard (ID 1, Rowan-POV).
    #   POV switch is the clean cut. Rowan is "newly arrived" per chapter plan. Taylor is in
    #   the yard and approaches (ID 3). No continuity obligation at this chapter boundary.
    #   PASS.

    # CH05 → CH06 boundary:
    #   Ch05 ends: septon-rowan drops the eyes (ID 88). The dying septon is not referenced
    #   in ch05's denouement — he is presumably alive but offstage. Ch06 opens with
    #   septon-dying-protector exhaling his last breath (ID 1). No ch05 beat states or
    #   implies the dying septon has died. The boundary is clean.
    #   PASS.

    # ── PLUMM DEPUTIZATION CHECK ─────────────────────────────────────────────

    # Margit TASK 12 patch: Plumm deputized by Hatch for census/anomaly documentation.
    # Ch05 positions Plumm at the Harrenhal gatehouse postern (ID 30). Rowan approaches
    # Plumm there to contest the anomaly classification (intercession). The deputization
    # establishes Plumm holds field-level intake authority — making him the correct target
    # for an ecclesiastical challenge to the field documentation.
    # The chapter honors this: Rowan goes to Plumm (not to Hatch directly), the intercession
    # is conducted at the gatehouse (the field intake point), and Plumm's recording response
    # (IDs 42–66) is institutionally correct under the deputization.
    # PASS. No plausibility fault.

    # ── GAP COHERENCE — SURVIVING LOAD-BEARING BEATS ─────────────────────────

    # The four anchoring beats (name written 48, sept entry written 53, numbered 55,
    # book pocketed 66) survive the iter1 trim.
    # Beat 48 (first name written): present. Load-bearing — Rowan's name enters the record.
    # Beat 53 (sept entry written): present. Load-bearing — the sept is flagged.
    # Beat 55 (entry numbered): present. Load-bearing — the record is formalized.
    # Beat 66 (book pocketed): present. Load-bearing — the record is sealed and closed.
    # These four beats constitute the minimum viable outcome sequence. PASS for this sub-check.
    #
    # However: the cause that triggers beats 42–66 (Rowan's intercession claim, IDs 35–40)
    # is absent. See FAULT-CONTINUITY-003.

    # ── POV CONSISTENCY ──────────────────────────────────────────────────────

    # All septon-rowan subject lines are physically executable by Rowan as POV narrator.
    # taylor-hebert-westeros appears in the chapter at IDs 3–8 and 75–84 — both are
    # in scenes where Rowan and Taylor share physical space (sept yard). Observable. PASS.
    # ser-harwick-plumm actions (IDs 30, 33, 34, 42, 43, 48, 53, 54, 55, 56, 60, 61,
    # 62, 66, 67, 69, 70) occur while Rowan is present at the gatehouse. Observable. PASS.
    # See flag-002 for the POV-form advisory on Plumm-subject lines.
    # "the ravens lift" (ID 84): ravens are in the sept yard per established loc state.
    # Observable by Rowan as POV narrator. PASS.

    # ── TIME CONSISTENCY ─────────────────────────────────────────────────────

    # Chapter is a single continuous sequence: arrival → cottage → prayer → road → gatehouse
    # → return. Three explicit time gaps (IDs 16–19, 22–23+25, 27–28) bridge transitions
    # and are structurally sound except for FAULT-CONTINUITY-002 (cottage→chancel break).
    # No time-reversal or impossible simultaneity detected.
    # PASS (subject to FAULT-CONTINUITY-002 resolution).
