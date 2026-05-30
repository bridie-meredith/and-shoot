audit:
  scope: chapter
  target: b01c06
  phase: "/and-write Phase 5 — continuity audit"
  timestamp: 2026-05-30
  sources_read:
    - active-project/staff/showrunner/_drafts/b01c06-bones-draft-2026-05-30.md
    - active-project/staff/showrunner/memory.md (b01c05 handoff_out; b01c06 chunk/substance_delta/scenes/handoff_in/handoff_out; series constraints; cost_ledger; actor_baselines)
    - active-project/actors/taylor-hebert-kl-122ac/state.md
    - active-project/actors/wren-stitch-maker-flea-bottom-ward/state.md
    - active-project/actors/jarvis-coin-kl-courier/state.md
    - active-project/actors/sera-hightower-kl-122ac/state.md
    - active-project/warehouse/cond-earth-bet-noun-fence.md
    - active-project/warehouse/cond-taylor-pov-behavior.md
    - active-project/warehouse/cond-kl-geography-122ac.md
    - active-project/staff/showrunner/parking-lot.md (pl-2026-05-30-001, pl-2026-05-30-002)

  verdict: CONTINUITY-OK

  findings:

    - id: fault-001
      type: pass
      what: "FAULT-HANDOFF-IN-MISMATCH check — b01c06 handoff_in vs b01c05 handoff_out"
      why: |
        b01c05 handoff_out character_state: "Taylor: political_register-prot rank 2.5;
        capability rank 4.5; position rank 3; moral_framework cracked."
        b01c06 handoff_in character_state: "Taylor: political_register-prot rank 2.5;
        capability rank 4.5; position rank 3; moral_framework cracked." Exact match.
        b01c05 handoff_out open_threads: "Wren: in coverage map; anchor rank 2."
        b01c06 handoff_in open_threads: "Wren: in coverage map; one seen-not-spoken
        contact; anchor rank 2." Match — the "seen-not-spoken" qualifier in c06
        carries forward c05's state without contradiction.
        b01c05 handoff_out: "political_register-prot: resentment color now present in
        all court-tier feed interpretation" / "Flea Bottom intelligence routing:
        continuing" / "cf-d10-courier-face thread: courier body observed three times."
        b01c06 handoff_in: "political_register-prot: resentment color present in all
        court-tier feed" / "Flea Bottom intelligence routing: continuing" /
        "cf-d10-courier-face: courier body in Taylor's memory." Match on all three.
        State.md entering c06: moral_framework_axis 1, relational_anchor_status_axis 2,
        moral_legibility_to_self_axis 4, capability_axis 4.5, position_prot_rise_axis 3,
        political_register_prot_axis 2.5, social_tether_prot_rise_axis 3. All consistent
        with c06 handoff_in character_state. No mismatch.

    - id: fault-002
      type: pass
      what: "FAULT-HANDOFF-IN-MISMATCH check — Wren 'seen-not-spoken' → first spoken exchange (s01n04)"
      why: |
        The transition from anchor rank 2 (seen-not-spoken) to first spoken exchange
        at s01n04 is the chapter's intended relational advance, not a contradiction.
        handoff_in correctly records the entering state; the chapter's bones then
        advance from that state. s01n04 "wren-stitch-maker-flea-bottom-ward speaks to
        taylor-hebert-kl-122ac" is the event that moves relational_anchor_status +1.0.
        The handoff_out correctly reflects the post-advance state: "Wren: first spoken
        exchange; omitted from deliverable; anchor rank 3." No mismatch — the advance
        is the chapter's substantive delivery, fully consistent with the contract.

    - id: fault-003
      type: pass
      what: "FAULT-STATE check — rank arithmetic across the chapter (moral_framework)"
      why: |
        Entering rank (state.md): moral_framework_axis 1.
        Chapter move: -1.0 (s03n06, cl-d06 cost side).
        Exiting rank (handoff_out): moral_framework rank 0.
        Arithmetic: 1 - 1.0 = 0. Consistent.
        The series axis end_rank is 8 (high = worse, monotonic collapse).
        Two units of movement by chapter 6 is within the 6-rank collapse trajectory
        (d03 through d12). No inconsistency.

    - id: fault-004
      type: pass
      what: "FAULT-STATE check — rank arithmetic (relational_anchor_status)"
      why: |
        Entering rank (state.md): relational_anchor_status_axis 2.
        Chapter move: +1.0 (s01n04, cl-d06 gain side, first tranche).
        Exiting rank (handoff_out): anchor rank 3.
        Arithmetic: 2 + 1.0 = 3. Consistent. cl-d06 second tranche (+1.0) correctly
        deferred to b01c08–b01c10 per pl-2026-05-30-001 (open, non-blocking).

    - id: fault-005
      type: pass
      what: "FAULT-STATE check — rank arithmetic (moral_legibility_to_self)"
      why: |
        Entering rank (state.md): moral_legibility_to_self_axis 4.
        Chapter move: +1.0 realized (s03n08; scene-aggregate target +0.5, realized at
        DEC-0030 bone floor; within ±1 tolerance, open SIGNAL for Phase 6 bone-gate).
        Exiting rank (handoff_out): moral_legibility rank 5.
        Arithmetic: 4 + 1.0 = 5. Consistent with realized magnitude. SIGNAL-flag
        already acknowledged in bones draft; not a continuity fault.

    - id: fault-006
      type: pass
      what: "FAULT-STATE check — held axes (capability, position-prot-rise, political_register-prot, social_tether-prot-rise)"
      why: |
        All four held axes enter and exit at the same rank per handoff_in → handoff_out:
        capability 4.5 → 4.5 (no expansion; coverage-recall only). ✓
        position-prot-rise rank 3 → rank 3 (no new formalization event). ✓
        political_register-prot rank 2.5 → rank 2.5 (no court-tier content in s01/s02/s03;
        resentment correctly not advanced; all three scene bones rationales confirm). ✓
        social_tether-prot-rise rank 3 → handoff_out does not explicitly state this rank,
        but the axis is confirmed held across all three scenes ("no new tether addition;
        the Wren contact is explicitly kept OUT of the deliverable tether layer"). Consistent
        with entering state. ✓

    - id: fault-007
      type: pass
      what: "FAULT-REACHABILITY — chapter goal delivery by bones"
      why: |
        Goal: "Show the audience the first named-person delivery and the accounting that
        precedes it, so the rationalize-each-trade pattern is legible — and show Wren's
        omission from the deliverable as the un-priced move it is."
        First named-person delivery: s03n06 (seals the jarvis-channel form) + s03n07
        (courier takes the jarvis-channel form). Both concrete SVO EVENT-NOT-CONCRETE
        PASS. Delivery enacted, not narrated. ✓
        Accounting (rationalize-each-trade): s03n01 (opens accounting ledger) / s03n02
        (writes first arm) / s03n03 (writes second arm) / s03n05 (closes accounting entry)
        / s03n10 (squares the form — close→act hinge). Four-step form complete. ✓
        Wren's omission as un-priced move: s01n07 (marks contact-role field — writes
        'ward-resident, Hook, routine') + s01n08 CENTRAL (blanks the contact-source field).
        Both enacted as physical field-acts per pl-2026-05-30-002(a) discipline. ✓
        Handoff_out delivers: "rationalize-each-trade pattern: established; first
        named-person delivery on record" / "Wren: first spoken exchange; omitted from
        deliverable; anchor rank 3." Goal fully delivered by bones. ✓

    - id: fault-008
      type: pass
      what: "FAULT-REFERENCE — 'the courier' at s03n07"
      why: |
        SVO: "the courier takes the jarvis-channel form." The actor used is a generic
        unnamed Jarvis-channel delivery person, not claiming to be jarvis-coin-kl-courier.
        jarvis-coin-kl-courier is the structural intermediary to Otto (the channel itself),
        not every individual courier in the dispatch chain. The chapter chunk (s03) reads:
        "a Jarvis courier will move the information." The bone correctly renders a generic
        institutional courier as the bone's subject. No slug resolution required for an
        un-named dispatch figure in a scene where the named character is the channel, not
        the individual runner. Not a FAULT-REFERENCE.

    - id: fault-009
      type: pass
      what: "FAULT-REFERENCE — 'the red-keep coverage record' at s03n04"
      why: |
        Taylor "marks the red-keep coverage record" — this references Taylor's existing
        insect-feed coverage of the Red Keep servant-passage ward (the Rushwick), established
        at b01c05 and confirmed in state.md ("ward-coverage now extends Rushwick (Red Keep
        servant-passage abutting) via c05"). This is a reference to Taylor's own operational
        records within the coverage architecture, not an invented prop or named entity
        requiring a card. The s03 chunk confirms: "Sera as she appears in the feed's Red Keep
        coverage." The reference resolves to established canon. Not a FAULT-REFERENCE.

    - id: fault-010
      type: pass
      what: "FAULT-REFERENCE — sera-hightower-kl-122ac resolution in s03n02/n03/n04"
      why: |
        Sera is referenced obliquely via "names against Sera's protection" (s03n02) and
        "omission risk against Sera's exposure" (s03n03) and the "red-keep coverage record"
        that represents her (s03n04). sera-hightower-kl-122ac is a confirmed cast member
        (actor card and state.md present). State: red-keep-maegor-holdfast, Alicent's
        household, legitimacy_question structural-non-resolving. These bones reference her
        correctly as the protection-architecture object. No contradiction with her state. ✓

    - id: fault-011
      type: pass
      what: "FAULT-REFERENCE — 'otto-hightower' / 'Jarvis' reference chain in s02"
      why: |
        The Jarvis channel is established. The bones reference "the jarvis-channel message"
        (s02n01), "the jarvis-channel form" (s02n05, n06), and "the jarvis-channel form"
        throughout s03. jarvis-coin-kl-courier is a confirmed actor. otto-hightower is a
        confirmed actor. The channel is the established routing mechanism (b01c03+). No
        invented entities. ✓

    - id: fault-012
      type: pass
      what: "FAULT-REFERENCE — three record-substrates distinct and consistently referenced (pl-2026-05-30-002(b))"
      why: |
        Substrate 1 — ward-coverage notes: s01n06 (opens coverage-notes entry), s01n07
        (marks contact-role field), s01n08 (blanks contact-source field), s01n09 (closes
        coverage-notes entry), s03n08 (opens ward-coverage notes post-send), s03n09 (closes
        ward-coverage notes). Distinct from the other two substrates throughout. ✓
        Substrate 2 — Jarvis-channel form: s02n05 (fills the jarvis-channel form), s02n06
        (lowers the jarvis-channel form), s03n06 (seals the jarvis-channel form), s03n07
        (courier takes the jarvis-channel form). This substrate is sealed and dispatched at
        s03n06-n07, physically absent from s03n08-n09. ✓
        Substrate 3 — accounting ledger: s03n01 (opens accounting ledger), s03n02 (writes
        first arm), s03n03 (writes second arm), s03n05 (closes accounting entry). Fully
        separate from both other substrates; receives the explicit moral-accounting text;
        never confused with the coverage notes or the Jarvis form. ✓
        The substrates are never conflated across bones. The four names go into the
        Jarvis-channel form (s02n05), not into the coverage notes (where Wren's name was
        blanked in s01). The bones-level staging meets pl-2026-05-30-002(b) discipline. ✓

    - id: fault-013
      type: pass
      what: "Earth-Bet fence — 'the feed' in SVO fields; parahuman jargon check"
      why: |
        cond-earth-bet-noun-fence: parahuman jargon dialogue-banned; inner-monologue-rare.
        The bones file notes and rationales use "the feed" as operational shorthand (licensed
        in planning-layer notes per the condition card's "authoring fence" scope and per
        cond-taylor-pov-behavior §Layer scope: "Bones (authored by /and-write) use
        third-person-named-subject SVO form by mechanical design; the first-person
        transformation is the responsibility of /and-stitch"). The SVO fields themselves
        contain no Earth-Bet proper nouns. SVOs use: "the handcart", "the crowd",
        "wren-stitch-maker-flea-bottom-ward", "taylor-hebert-kl-122ac", "the coverage-notes
        entry", "the contact-role field", "the contact-source field", "the jarvis-channel
        message/form", "the accounting ledger", "the courier", "the red-keep coverage record",
        "the morning light". None of these are parahuman vocabulary. ✓
        No Khepri, no "parahuman", no "power", no Gold Morning, no Worm-canon institutional
        name appears in any SVO field. Earth-Bet fence clean at bones layer.

    - id: fault-014
      type: pass
      what: "POV check — Taylor bones subject consistency"
      why: |
        Per cond-taylor-pov-behavior: "Bones use third-person-named-subject SVO form by
        mechanical design. Do NOT flag scene chunks or bones files for being in third-person
        named-subject form — this is pipeline convention at the planning and bone-authoring
        layers; the first-person transformation happens at /and-stitch. The auditor's POV
        check applies to the rendered draft layer only."
        Taylor's bones subjects are consistently "taylor-hebert-kl-122ac" (or ambient
        environmental subjects: "the handcart", "the crowd", "the morning light", "the
        jarvis-channel message"). Wren's subject is "wren-stitch-maker-flea-bottom-ward".
        No first-person leakage at the bones layer. No non-Taylor subject where Taylor
        should be subject. ✓

    - id: fault-015
      type: pass
      what: "Geography/time coherence — s01 Hook → s01n10 morning-light bridge → s02 late-morning Jarvis window → s03 accounting + send"
      why: |
        s01: ward-walk in the Hook's early-work hour (lane-mouth blocked, south court). 
        Locations named: lane-mouth, south court, drain-angle. All are Flea Bottom-layer 
        per cond-kl-geography-122ac (Hook = curved street near waterfront, in Flea Bottom 
        between hills, dense smallfolk). ✓
        s01n10: "the morning light crosses the lane-mouth" — temporal bridge bone (MT-01).
        Notes confirm: "bridges the s01→s02 seam (ward-walk continues → morning advances
        to the late-morning Jarvis window)." This is a deliberate time-passage bone, not
        contradictory to s01. Morning → late morning is coherent progression. ✓
        s02: "The Jarvis channel opens in the late-morning window" (per chunk). Bones confirm
        this timing: s02n01 "the jarvis-channel message arrives." No contradiction with s01's
        morning setting. ✓
        s03: accounting and send, temporally subsequent to s02. No time markers conflict.
        The sequence morning → late-morning → accounting is spatially and temporally coherent
        for a single chapter-day. ✓

    - id: fault-016
      type: pass
      what: "FAULT-REACHABILITY — handoff_out derivable from bones"
      why: |
        handoff_out open_threads:
        "rationalize-each-trade pattern: established; first named-person delivery on
        record" → bones s03n01–n10 (the accounting form) + s03n06 (seal/send). ✓
        "Wren: first spoken exchange; omitted from deliverable; anchor rank 3 (weight
        added by omission)" → bones s01n04 (Wren speaks) + s01n07/n08 (marks role, blanks
        name) + relational_anchor_status +1.0 at s01n04. ✓
        "moral_legibility crack: deeper; accounting is honest and that honesty is visible"
        → bones s03n08 (opens ward-coverage notes post-send; moral_legibility_to_self +1.0
        realized). ✓
        "Black-faction ward elders named to Otto: downstream consequence pending" →
        bones s03n06/n07 (sealed form dispatched; four names gone). ✓
        "cf-d10-courier-face: courier in memory; not yet a face" → carried from c05; not
        advanced in c06 bones (no new courier encounter in c06). The handoff_out correctly
        carries this thread forward without change. ✓
        handoff_out character_state:
        "Taylor: moral_framework rank 0; relational_anchor_status rank 3; moral_legibility
        rank 5; position rank 3; political_register-prot rank 2.5" → all derivable from
        bones arithmetic as verified in fault-003 through fault-006. ✓
        "Wren: in coverage map; spoken-contact made; not in deliverable layer" → bones
        confirm: s01n03/n04 (Wren crosses crowd, speaks), s01n07/n08 (name omitted from
        coverage notes contact-source field, not in Jarvis channel). ✓

    - id: fault-017
      type: flag
      what: "s03n08 (opens the ward-coverage notes, moral_legibility_to_self +1.0) — bone magnitude realized above scene-aggregate target"
      why: |
        Scene s03 aggregate target for moral_legibility_to_self is +0.5. The DEC-0030 bone
        floor requires magnitude ≥ 1.0 per move, so the bone realizes +1.0 against a +0.5
        target. This is within the declared ±1 tolerance and is an open SIGNAL already
        acknowledged in the bones draft ("SIGNAL-flag for Phase 6 bone-gate — multi-scene
        distribution artifact"). Not a continuity fault — the substance contract and the
        bones draft both document this disposition. Carrying forward to Phase 6 bone-gate
        as intended.
      # No criteria field — this is a flag, not a fault.

    - id: fault-018
      type: pass
      what: "Wren actor state — location and condition consistent with s01 encounter"
      why: |
        wren-stitch-maker-flea-bottom-ward state.md: location flea-bottom-hook-district,
        condition [story-open-d01], stats household: stitch-maker-ward.
        s01 chunk: Wren is in the stitch-house lane feeding into the blocked junction.
        The Hook is in flea-bottom-hook-district. Wren's location in the Hook stitch-house
        lane is fully consistent with her state file. ✓
        No prop usage by Wren; no location mismatch; no chapter-close location update
        required (she returns to the stitch-house after directing Taylor; no state transition
        authored in the bones for Wren, which is correct — she is not a POV actor and
        her state is not changed by a brief direction exchange). ✓

    - id: fault-019
      type: pass
      what: "pl-2026-05-30-002 parking-lot watches satisfied at bones layer"
      why: |
        pl-2026-05-30-002(a) — dark-fantasy-reader: "Wren omission must be enacted as
        physical pause + field-entry, NOT interior moral narration." Check:
        s01n07 "marks the contact-role field" (writes 'ward-resident, Hook, routine') —
        concrete physical writing act. s01n08 "blanks the contact-source field" — concrete
        physical omission act. Notes on n08 explicitly confirm: "enacted as physical
        field-act, NOT interior moral narration." ✓
        pl-2026-05-30-002(b) — cape-fic + pedant: "ward-coverage-notes vs Jarvis-channel
        substrate gap must be staged as a concrete institutional mechanism." Check:
        The bones file stages three distinct substrates (fault-012 above) with explicit
        rationale at s02n05: "the Jarvis-channel form and the ward-coverage notes are two
        distinct institutional substrates — the four names go into the form, not into the
        coverage notes where Wren's name was blanked in s01." The gap is an institutional
        architectural fact in the bones, not a hope. ✓
        Both parking-lot watches satisfied at the bones level.

  summary: |
    26 bones across 3 scenes audited against: b01c05 handoff_out, b01c06 handoff_in/out,
    state.md (taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward, jarvis-coin-kl-courier,
    sera-hightower-kl-122ac), cond-earth-bet-noun-fence, cond-taylor-pov-behavior,
    cond-kl-geography-122ac, parking-lot pl-2026-05-30-001 and pl-2026-05-30-002.

    VERDICT: CONTINUITY-OK.

    0 faults. 0 escalations. 1 flag (fault-017: moral_legibility_to_self s03 +1.0 realized
    vs +0.5 target — within ±1 tolerance, documented in bones draft, routes to Phase 6
    bone-gate as SIGNAL). All 19 checks pass.

    Specific verifications requested:
    1. Handoff-in honored: s01 opens consistent with c05 close — resentment present but
       not advanced (no court-tier content in s01/s02/s03 Flea Bottom bones), Wren entering
       first spoken exchange from seen-not-spoken (intended advance, not contradiction),
       arrangement and Jarvis channel active (s02n01 message arrives). ✓
    2. Geography/time: s01 (Hook, morning) → s01n10 (morning-light bridge, deliberate) →
       s02 (late-morning Jarvis channel) → s03 (accounting + send) — spatially and temporally
       coherent. ✓
    3. Three record-substrates: ward-coverage notes / Jarvis-channel form / accounting ledger
       kept distinct and never conflated across all 26 bones. ✓
    4. Earth-Bet fence: "the feed" appears only in rationale/notes (bones-layer planning
       convention, not a rendered line); no parahuman jargon in any SVO field. ✓
    5. Goal delivery: first named-person delivery (s03n06/n07) + accounting (s03n01–n10) +
       Wren's omission as un-priced move (s01n07/n08) all fully delivered. handoff_out
       derivable from bones. ✓
