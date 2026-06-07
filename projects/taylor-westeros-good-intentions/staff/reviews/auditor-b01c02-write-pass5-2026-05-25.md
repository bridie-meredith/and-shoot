```yaml
audit:
  scope: chapter
  target: b01c02
  phase: 5 (continuity — /and-write pass)
  timestamp: 2026-05-25
  verdict: CONTINUITY-OK

  findings:

    - id: pass-001
      type: pass
      what: FAULT-HANDOFF-IN-MISMATCH check — b01c02 handoff_in vs b01c01 handoff_out
      why: |
        b01c01 handoff_out declares: capability rank 3, prohibition cracked but intact, no court
        position, social tether starting (Oswyn-layer), Wren has seen Taylor's face no exchange,
        witch-label formation active.
        b01c02 handoff_in honors all threads: "capability cracked open: first deployment behind
        Taylor" matches rank 3; "Wren seen in crowd; no exchange; no names" matches; "Oswyn Mudway:
        Taylor on his ward-elder awareness layer" matches; "witch-label formation active" matches.
        No mismatch.

    - id: pass-002
      type: pass
      what: FAULT-REACHABILITY check — chapter goal vs bones
      why: |
        Chapter goal: "Show the audience Taylor's first self-constructed surveillance map and the
        moment she recognizes what it is — then files it and continues — so the pattern is visible
        before any patron arrives to name it."
        Delivered: s01 establishes the sweep decision and mechanism (n04, n06, n08); s02 delivers
        Wren entering the coverage map as a named function-node (n07); s03 delivers recognition
        arriving (n05), suppression executing (n06), and ledger closing (n07-n09). All three
        goal elements are present and causally sequenced. Goal delivered.

    - id: pass-003
      type: pass
      what: FAULT-REACHABILITY check — handoff_out vs bones
      why: |
        handoff_out declares: relational_anchor_status account opened (Wren in map, rank 2);
        moral_legibility_to_self rank 4.5 (crack suppressed); capability rank 3; coverage map
        exists in Taylor's head covering ~40 people.
        Bones deliver: relational_anchor_status +1.0 at s02n07 (rank 1→2 explicit in notes);
        moral_legibility_to_self +0.5 at s03n05 (rank 4→4.5 in notes); s02n05/n06 categorization
        mechanism; s03n03 "forty-three bodies" count. handoff_out is consistent.

    - id: pass-004
      type: pass
      what: FAULT-STATE check — actor location consistency
      why: |
        Taylor state file: location flea-bottom-hook-district. All 29 bones are anchored in
        Hook precinct geography (drain angle, alley-mouth, ward-junction, stitch-house lane,
        wall-face). No extra-precinct location claimed. Wren does not appear in person.
        Oswyn is not given a bone — present only as backdrop annotation. State-location consistent.

    - id: pass-005
      type: pass
      what: FAULT-STATE check — props/inventory
      why: |
        Taylor state file: inventory []. No prop is referenced in the bones draft that would
        require inventory possession. All objects are environmental (drain, wall-face, threshold-
        stones, alley-mouth). No prop fault.

    - id: pass-006
      type: pass
      what: FAULT-REFERENCE check — cast slug resolution
      why: |
        Named slugs in bones: taylor-hebert-kl-122ac (subject in 9 bones across 3 scenes).
        No other actor slug appears as subject. Wren and Oswyn appear only in notes/rationale,
        not in bone lines. Environment subjects are all anonymous ("the insects", "the ward-junction
        body", "the foot-traffic", "the map", "the tallow smoke", "the harm-reduction accounting",
        "the ledger", "the coverage map", "the accounting"). No unresolved cast slug in any bone
        line.

    - id: pass-007
      type: pass
      what: FAULT-REFERENCE check — location resolution
      why: |
        Locations named: drain angle (Hook district), alley-mouth, ward-junction, stitch-house lane,
        wall-face, threshold-stones. All consistent with Taylor's state file location
        (flea-bottom-hook-district) and series geography constraint (cond-kl-geography-122ac).
        No location claimed outside Hook precinct.

    - id: pass-008
      type: pass
      what: FAULT-POV check — perception-verb audit
      why: |
        Chapter pov_narrator: taylor-hebert-kl-122ac.
        Full scan of all 29 bone lines:
          s01: rises, fan, delivers, plants, spread, extends, draws, push, knots — no perception verb.
          s02: returns (x2), marks, touches, enters, returns, slots, files, turns, opens, names —
            "returns" used for insect-feed output delivery (s02n01: "the insects return the ward-
            junction body a second time"; s02n05: "the insects return the junction-body's function-
            signature without a name") — subject is "the insects", not taylor; this is environmental
            action, not POV character perception; PASS.
          s03: settles, runs, returns (s03n03: "the map returns forty-three bodies" — subject is
            "the map"; environmental), reaches, arrives, draws, closes (x2), closes (x3), exhales.
        No perception verb with taylor-hebert-kl-122ac as subject. FAULT-POV not triggered.

    - id: pass-009
      type: pass
      what: FAULT-POV check — narrator consistency
      why: |
        pov_narrator: taylor-hebert-kl-122ac. SVO subject pattern: bones either have
        taylor-hebert-kl-122ac as explicit subject (rises, plants, extends, draws, turns, settles,
        runs, exhales) or have anonymous environmental entities as subject (insects, ward-junction
        body, tallow smoke, map, foot-traffic, coverage map, harm-reduction accounting, ledger,
        accounting, word). No third-party narrator observation from outside the insect-feed perimeter.
        Environmental subjects are consistent with Taylor's insect-feed POV convention established
        in b01c01. Narrator consistent.

    - id: flag-001
      type: flag
      what: Actor baseline stat discrepancy — taylor-hebert-kl-122ac state.md
      why: |
        taylor-hebert-kl-122ac/state.md records opening stats: capability_axis: 2,
        relational_anchor_status_axis: 1, moral_legibility_to_self_axis: 4. These are series-open
        values, not post-b01c01 values. After b01c01: capability rose to rank 3 (+1.0);
        social_tether-prot-rise rose to rank 2-ish (Oswyn layer +1.0). State file has not been
        updated to reflect b01c01 close. This is outside /and-write b01c02 scope (state file
        update is a Phase 7 or post-write step for b01c01), but the discrepancy is live and could
        cause a FAULT-STATE in a future continuity check if the state file is read as authoritative.
        No bones in b01c02 violate the post-b01c01 inferred state — they are consistent with rank 3
        capability and rank 1→2 social_tether — but the state file requires update.
      criteria: null
```
