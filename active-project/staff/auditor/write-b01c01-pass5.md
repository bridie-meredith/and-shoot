```yaml
audit:
  scope: chapter
  target: b01c01 (27 bones post-trim, 3 scenes)
  phase: 5
  timestamp: 2026-05-23
  findings:

    # -----------------------------------------------------------------------
    # FAULT-STATE-001  SVO and deletion-record conflict — s01n01 vs s01n02
    # -----------------------------------------------------------------------
    - id: fault-001
      type: fault
      class: FAULT-STATE
      what: >
        The phase-1-decomposition file (the audited target) records s01n01 as
        "taylor-hebert-kl-122ac pays the building-keeper" and s01n02 as deleted
        (chatter echo, 2-of-3 audience trim). Memory.md (lines 734–749) records s01n01
        as "taylor-hebert-kl-122ac enters the corner-room", s01n02 as "taylor-hebert-
        kl-122ac pays the building-keeper", and the deleted slots as s01n03 and s01n11
        — not s01n02. The two canonical records assign different SVOs to the n01 slug
        and disagree on which slugs were deleted at Phase 4.
      why: >
        Memory.md is the source of truth for per-bone state-delta (CLAUDE.md memory
        rules). The flat_id assignment at memory.md line 710 and the stitched draft
        were produced from the memory.md bone record. A re-run of /and-write or any
        downstream command that reads the decomposition file will reconstruct a
        different chapter from the one that was stitched. The discrepancy is silent —
        no error surfaces unless both records are compared.
      criteria: >
        The two records must agree on (a) which slug carries the payment SVO and
        (b) which slug(s) were deleted at Phase 4 trim. One record must be designated
        authoritative. Given that the stitched draft (the terminal deliverable) was
        produced from the memory.md bone record, memory.md has priority; the
        decomposition file should be brought into alignment unless fixer determines
        that memory.md's Phase 4 deletion record is itself the error. The resolution
        must be consistent across all three surfaces: decomposition file, memory.md
        bones block, and the flat_id assignment comment at memory.md line 710.

    # -----------------------------------------------------------------------
    # FAULT-STATE-002  SVO identity conflict — s02n01 and s02n03
    # -----------------------------------------------------------------------
    - id: fault-002
      type: fault
      class: FAULT-STATE
      what: >
        In the phase-1-decomposition file, s02n01 = "taylor-hebert-kl-122ac threads
        the needle" (chatter, working-day rhythm opener). In memory.md (line 819),
        s02n01 = "taylor-hebert-kl-122ac lifts the basket" (chatter). The decomposition
        file's s02n03 = "the needle crosses the mesh" with knowledge 0.02; memory.md's
        s02n03 = "taylor-hebert-kl-122ac threads the needle" with knowledge 0.03.
        The SVOs assigned to the n01 and n03 slots differ between the two records,
        and the axis magnitude at n03 differs (0.02 vs 0.03).
      why: >
        Same downstream risk as fault-001. The bones file and stitched draft are
        anchored to the memory.md SVO set. A re-run reading the decomposition file
        would emit a different SVO walk for s02, including a different SVO at flat_id
        11 (s02n01) and a different knowledge delta attribution at flat_id 13 (s02n03).
        The magnitude discrepancy (0.02 vs 0.03) also affects the per-axis aggregate
        logged in the decomposition file's s02 tally (0.20 exact) vs the memory.md
        aggregate comment (also 0.20 but the individual n03 entry is 0.03 vs 0.02 in
        decomposition's n03 entry) — the tally totals may mask which individual bone
        carries the third centesimal.
      criteria: >
        The SVO and axis magnitude at s02n01 and s02n03 must be identical across the
        decomposition file and memory.md. The authoritative source is the memory.md
        record that produced the stitched draft. Fixer must align the decomposition
        file to memory.md at both slugs, or confirm that memory.md is the record
        in error and update it, then verify the per-axis aggregate remains consistent.

    # -----------------------------------------------------------------------
    # FAULT-STATE-003  Duplicate slug entry — s02n11 appears twice
    # -----------------------------------------------------------------------
    - id: fault-003
      type: fault
      class: FAULT-STATE
      what: >
        The phase-1-decomposition file contains two entries for slug b01c01s02n11
        (decomposition lines 227–242). The first carries shape: moving with
        axis_moves direction:up magnitude:0.00 (self-annotated as malformed). The
        second is the corrected chatter form. Both share the same slug. The
        reconciliation note at line 366 designates the second as canonical but does
        not remove the first.
      why: >
        A duplicate slug in the bones source is not schema-valid. Any automated pass
        that processes entries in order encounters the malformed entry first. If the
        bones file (theater/bones/b01-c01.md) was emitted before the self-correction
        was annotated, the bones file may carry the malformed entry. The presence of
        two entries under one slug also makes the total bone count ambiguous (the
        file would parse as 28 bones, not 27).
      criteria: >
        The first (malformed) b01c01s02n11 entry must be removed from the decomposition
        file so that only the corrected chatter-form entry remains under that slug.
        The chapter-level reconciliation note at line 366 should confirm the removal.
        If the bones file at theater/bones/b01-c01.md contains the malformed entry,
        it must also be corrected to the chatter form.

    # -----------------------------------------------------------------------
    # PASSING CHECKS
    # -----------------------------------------------------------------------

    - id: pass-goal-delivery
      type: pass
      class: CONTINUITY-OK
      what: >
        All three goal loads delivered. (a) Operating rule: enacted as held-capability
        bones across all three scenes — s01n10 (holds the feet), s02n07 (holds the
        hands), s02n10 (holds the eyes), s03n06 (holds the eyes), s03n08 (lifts the
        needle/closing verdict). Never labelled; always staged with named opposing-force.
        (b) Ward: Flea Bottom established via drain-channel, tallow-stall, well-step,
        cobbles, alley-mouth, meat-stall distributed across 27 bones. (c) Child: Wren
        enters at s03n01, demonstrates clear-seeing at s03n05 (flies not on Taylor),
        departs un-filed at s03n07 with Taylor returning to work at s03n08.
      why: none — passes
      criteria: none — passes

    - id: pass-handoff-out
      type: pass
      class: CONTINUITY-OK
      what: >
        handoff_out declarations are consistent with surviving bones. Rule intact-but-
        untested against external ask: no external ask in chapter; opposing-force in
        s03 is Taylor's own trained pattern-reading, not an external actor. Wren
        introduced as recurring street presence: eight bones in s03. Insect-sense
        passive: s02n04/n05 (ambient-drift, held at observation-only). Coll provides
        cover by proximity without arrangement: s01n04/n05, s02n09. Knowledge delta
        sums to approximately 0.48 (within band of 3→3.5 per handoff_out). All other
        ranks unmoved in the chapter; no bone moves moral-framework, capability,
        position, social-tether, relational-anchor, moral-legibility, political-register,
        or agency.
      why: none — passes
      criteria: none — passes

    - id: pass-state-location
      type: pass
      class: CONTINUITY-OK
      what: >
        Taylor's location sequence is contiguous and free of teleports. s01: building
        threshold → yard/drain-channel (n03) → block circuit (n07) → tallow-stall
        (n06) → corner-stoop (n08–n10). s02: working at the corner beside Coll. s03:
        same corner; Wren approaches from alley-mouth direction. The n01→n03 jump
        (n02 deleted from decomposition file) is coherent: payment precedes yard-
        crossing without a required intermediate beat. No actor appears in two
        locations simultaneously.
      why: none — passes
      criteria: none — passes

    - id: pass-cast-reference
      type: pass
      class: CONTINUITY-OK
      what: >
        All cast slugs appearing in the 27 bones resolve to cast_roster entries in
        memory.md. taylor-hebert-kl-122ac (roster line 575), coll-net-mender-flea-
        bottom (roster line 593), wren-stitch-maker-flea-bottom-ward (roster line 584).
        Ambient actors (building-keeper, city-watch) are single-scene unnamed fixtures;
        no card is required for ambient non-cast actors per the chapter's scope.
      why: none — passes
      criteria: none — passes

    - id: pass-location-reference
      type: pass
      class: CONTINUITY-OK
      what: >
        All sub-location references (the Hook, drain-channel, tallow-stall, well-step,
        alley-mouth, meat-stall, the block, cobbles) fall within the Flea Bottom ward
        scope. Memory.md confirms Flea Bottom / Hook as the chapter's sole location.
        No bone places any actor outside Flea Bottom or in a location not established
        in this chapter.
      why: none — passes
      criteria: none — passes

    - id: pass-pov
      type: pass
      class: CONTINUITY-OK
      what: >
        No perception-verb leak on the POV narrator. All Taylor-subject SVOs use action
        verbs: pays, crosses, circles, passes, drops, threads, holds, lifts, speaks.
        None use sees / watches / feels / notices / observes. Ambient-subject bones
        ("the insects fill the block", "the walls cool", "the boots strike the cobbles",
        "the city-watch passes the hook", "the needle crosses the mesh") use object-as-
        subject form — licit per command-body ambient-drift rule (bone SVO object-as-
        subject for unknown/ambient agents).
      why: none — passes
      criteria: none — passes

    - id: pass-handoff-in
      type: pass
      class: CONTINUITY-OK
      what: >
        FAULT-HANDOFF-IN-MISMATCH check skipped per dispatch brief. b01c01 is the
        first chapter in the series; prior_episode is none; no handoff_out exists
        to validate against.
      why: none — passes
      criteria: none — passes

summary:
  verdict: FINDINGS-PRESENT
  faults: 3
  faults_by_class:
    FAULT-STATE: 3
    FAULT-REACHABILITY: 0
    FAULT-REFERENCE: 0
    FAULT-POV: 0
    FAULT-HANDOFF-IN-MISMATCH: 0  # skipped — first chapter
```
