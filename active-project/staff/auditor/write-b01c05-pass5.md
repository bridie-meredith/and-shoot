```yaml
audit:
  scope: chapter
  target: b01c05
  timestamp: 2026-05-28
  pass: write-b01c05-pass5
  findings:

    - id: fault-001
      type: fault
      what: >
        active-project/actors/taylor-hebert-kl-122ac/state.md — field
        political_register_prot_axis is recorded as 1. Bone b01c05s03n06
        delivers axis_moves: [{axis: political_register-prot, direction: up,
        magnitude: 1.5, cost_ledger_anchor: cl-d05}]. The chapter's
        handoff_out (memory.md line 3454) states Taylor's political_register-prot
        rank as 2.5 after this chapter. The actor state file has not been
        updated to reflect the +1.5 move delivered in this chapter.
      why: >
        The state file is the single-source-of-truth for axis values between
        chapters (memory rules: "nothing changes without being recorded"). If
        b01c06 authoring reads the state file and finds political_register_prot_axis: 1,
        it will author against the wrong baseline. The handoff_out already
        records 2.5 correctly but the actor state file — which is what downstream
        commands read — is inconsistent with it.
      criteria: >
        actor state file must record political_register_prot_axis: 2.5 before
        Phase 6 proceeds; the update must match the chapter's delivered +1.5
        axis-move as anchored at cl-d05.

    - id: flag-001
      type: flag
      what: >
        Bone b01c05s01n02 SVO: "taylor-hebert-kl-122ac enters the rushwick."
        The axes_held rationale correctly reads "continuation of four-ward map
        established in c04; not a new expansion event." However, the SVO
        surface form ("enters") carries first-entry semantics that a facet
        author or renderer reading the SVO alone — without the rationale —
        could interpret as an initial-expansion event rather than continuation.
        Handoff_in explicitly states the chapter opens on a four-ward map (c04
        final state); s01n02 must not be read as the expansion event itself.
      why: >
        If the facet author renders this bone as a capability-expansion beat,
        the opening of s01 misrepresents Taylor's state entering the chapter.
        The substance_delta for s01 holds capability (no new expansion); prose
        that frames the Rushwick entry as novel capability growth would conflict
        with that hold. The rationale is correct; the SVO is ambiguous.
      criteria: null

    - id: flag-002
      type: flag
      what: >
        Rushwick geography uses two noun-forms for the east side of the junction:
        "east-lane" (b01c05s01n05 — "the provisioner-train takes the east-lane")
        and "east exit" (b01c05s02n03 — "the three figures enter the side-alley
        off the east exit"). It is not established in the bones whether these
        are the same feature under different noun-forms or two adjacent but
        distinct geographic elements (a lane versus an exit-mouth).
      why: >
        If the facet and stitch authors treat these as the same location,
        spatial consistency within the Rushwick geography is maintained. If
        they treat them as different, the s01 provisioner-train routing and
        the s02 enforcement incident occur in adjacent sub-spaces — a distinction
        the bones do not resolve. This is minor geography ambiguity with no
        load-bearing narrative consequence in this chapter; it matters if the
        Rushwick returns in b01c06+ and a fixed geography is needed.
      criteria: null

    - id: flag-003
      type: flag
      what: >
        Bones b01c05s03n10 and b01c05s03n12 carry identical SVOs:
        "taylor-hebert-kl-122ac runs the rushwick flat-read." The bones
        are distinguished by context (n10 = first attempt, n12 = second attempt)
        and by their notes ("re-run bone 1" vs "re-run bone 3"), but the SVO
        surface is identical.
      why: >
        Identical SVOs in different bones are legal under the schema when the
        substance_delta distinguishes them (which it does here via rationale
        context). However, a facet author dispatched with only the SVO list
        may not distinguish these bones without reading the notes, risking
        duplicate prose rendering of the same surface action. The repeated-SVO
        is load-bearing for the foreclosure pattern (two identical attempts =
        confirmation), so collapsing them would be a fault; this is an
        authoring-surface disambiguation advisory only.
      criteria: null

    - id: pass-001
      type: pass
      what: >
        REACHABILITY — all three chapter goal elements delivered by surviving
        bones: (1) cessation event at s03n06 with confirmed +1.5 axis-move on
        political_register-prot at cl-d05; (2) color arrives before naming —
        s03n05 replay surfaces color without label, s03n08 files it as texture
        (not named as resentment), goal sequence honored; (3) courier figure
        planted — s02n11 cf-d10 thread initiated, s03n07/n09 confirmed open.
      why: null
      criteria: null

    - id: pass-002
      type: pass
      what: >
        HANDOFF-IN CONSISTENCY — opening bones (s01n01-s01n09) are consistent
        with all handoff_in fields (memory.md lines 3431-3443): coverage
        extension reads as continuation of four-ward map (axes_held rationale
        explicit); moral_framework held at licensed-exception level throughout
        s01 (no intact-state read); capability held (no new expansion event);
        Jarvis routing channel active (s02n09); Sera exposure treated as managed
        background; Wren absent from chapter with anchor held at rank 2.
      why: null
      criteria: null

    - id: pass-003
      type: pass
      what: >
        HANDOFF-OUT CONSISTENCY — bone set leaves chapter in the state declared
        in handoff_out (memory.md lines 3444-3457): political_register-prot
        rises from 1 to 2.5 (s03n06 +1.5); cf-d10-courier-face thread open
        (s02n11 initiated, s03n09 confirmed); Rushwick coverage in servant-passage
        ward established (s01n02/n03); faction-violence sub-pressure first
        observed on-page (s02n03-s02n10 enforcement incident). All four
        handoff_out world_state and character_state entries are supported by
        the bone set.
      why: null
      criteria: null

    - id: pass-004
      type: pass
      what: >
        POV CONSTRAINT — all 34 bones use third-person limited SVO form. No
        first-person leaks. No perception-verb subjects on Taylor SVOs (all
        Phase 2 fault-001 recasts correctly reflect physical-observable subjects).
        Narrator subject pattern consistent across all three scenes.
      why: null
      criteria: null

    - id: pass-005
      type: pass
      what: >
        TIME/SEQUENCE CONSISTENCY — s01 (second morning after Roper's Court
        report) is consistent with c04 handoff_out (report delivered at c04's
        final beat); s02 (five days into Rushwick coverage) is consistent with
        s01 establishing day 1 of Rushwick coverage; s03 (that evening, same
        day as s02) is consistent with s03n01 grounding bone placing Taylor
        at the room-floor for evening review. No time-sequence fault.
      why: null
      criteria: null

    - id: pass-006
      type: pass
      what: >
        REFERENCE CONSISTENCY — courier (unnamed, noun-form), three figures
        (unnamed, noun-form), provisioner-train (four-men-two-carts per chunk),
        message-runner, and Jarvis (offstage destination, never claimed
        physically present) are all used consistently. No actor slug appears
        in the chapter without being on-set or acknowledged as offstage. No
        prop reference to inventory items Taylor does not carry.
      why: null
      criteria: null

  verdict: FINDINGS-PRESENT
  verdict_note: >
    1 fault (state file not updated for +1.5 political_register-prot move);
    3 non-blocking flags (SVO first-entry ambiguity, geography noun-form
    ambiguity, duplicate SVO advisory). HARD finding: fault-001 (state record
    must be updated before Phase 6 proceeds). Phase 6 substance bone-gate
    may proceed after fault-001 is resolved.
```
