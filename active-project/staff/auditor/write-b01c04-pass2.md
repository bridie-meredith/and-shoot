```yaml
audit:
  scope: chapter
  target: b01c04
  timestamp: 2026-05-27
  trigger: /and-write b01c04 Phase 2 — constraint audit

  summary:
    verdict: FAIL
    fault_count_hard: 45
    bones_audited: 38
    per_class_counts:
      FAULT-FORM: 33
      FAULT-CONSTRAINT: 0
      FAULT-PHYSICAL: 0
      FAULT-BONE-DELTA-MALFORMED: 12
      FAULT-AGGREGATE-DELTA-MISMATCH: 0
      FAULT-COST-LEDGER-UNRESOLVED: 0

  clean_pass_checks:
    - Earth-Bet proper-noun fence: PASS — no parahuman jargon in any SVO
    - POV layer (third-person bones per PROP-0008/DEC-0028): PASS — all 38 bones third-person named-subject
    - Copula ban: PASS
    - Negation ban: PASS
    - Motivation clause ban: PASS
    - Theme-silence ("protection and the trap" verbatim): PASS — thesis phrase absent from all SVOs
    - Conjunction-primary (and/but/while/as openers): PASS
    - Westerosi magic dormant: PASS
    - Dragon proximity: PASS
    - KL court state: PASS
    - KL geography: PASS
    - Speech-bone canonical form (speaks to): PASS — all 4 dialogue-anchor bones use canonical form
    - FAULT-AGGREGATE-DELTA-MISMATCH: PASS — all 5 axes EXACT at scene + chapter level
    - FAULT-COST-LEDGER-UNRESOLVED: PASS — cl-antag-d03, cl02, cl03a, cl03b, cl-world-d04 all resolve
    - Axis slugs in axis_moves[] valid: PASS
    - Axis slugs in axes_held[] valid: PASS
    - Sensory grounding quota (≥1 per scene): PASS — s01:1, s02:3, s03:3
    - "registers" with insect-feed as subject (s01n05): PASS — licensed per c03 precedent

  systemic_pattern: |
    Two systematic patterns produced 45 HARD findings:

    (1) FAULT-FORM-MODIFIER (33 bones, ~87% of all bones). Pervasive prepositional
        phrases in SVO text: place, destination, source, direction, instrument,
        accompaniment, time. Per schemas/bones.schema.md line 107: all such PPs are
        explicitly banned. The schema's prescribed recast is transitive verb with
        the location as direct object ("taylor enters the yard" not "taylor walks
        into the yard"). Only 3 of 38 bones are PP-clean (s01n06, s01n07, s01n09 —
        the dialogue-anchor `speaks to` bones).

    (2) FAULT-BONE-DELTA-MALFORMED magnitude (11 bones). All moving bones use
        magnitude 0.5 (except s03n10 at 1.0); chunk_targets.bone.delta_per_axis
        floor is 1. Pair-split design (n06+n07 each 0.5 → scene total 1.0) violates
        the bone-level floor. Resolution requires consolidating pairs into single
        bones at magnitude ≥1.0.

    (3) FAULT-BONE-DELTA-MALFORMED speech-bone (s01n10 only). Dialogue-anchor bone
        with empty axis_moves — schema requires ≥1 communication-class axis on
        speech bones.

    Both systematic patterns trace to a single root cause: the screen-writer
    referenced the c03 bones file as a cadence model. c03's bones were PP-heavy
    and pair-split, but c03's /and-write Phase 2 audit was SKIPPED under cascade-
    budget compression. c03 therefore bypassed the SVO-form check that c01 and
    c02 (post-revise) both passed cleanly. The c04 screen-writer absorbed c03's
    permissive style as if it were the canonical pattern. c02's revised 47-bone
    file is the actual canonical reference for SVO discipline (Phase 2 caught 7
    FAULT-FORM there and resolved them; the post-fix bones are minimalist and
    PP-clean).

  routing_recommendation: |
    45 systematic single-root-cause findings exceed the fixer minimum-change
    operating envelope. Recommend Phase 1 redo with explicit corrective brief:
    - No PPs of place/direction/time/instrument/accompaniment in SVO text.
    - Magnitude floor 1.0 per axis_move; consolidate 0.5+0.5 pair-splits.
    - Use c02 bones (post-revise) as the cadence reference, NOT c03.
    Expected bone count after redo: ~28-32 (vs 38 today) as pair-splits collapse.

  findings_index:
    # Findings enumerated in full at /staff/admin/audit-reports/b01c04-pass2-detail.md
    # (this report's body) — see auditor reply transcript.
    fault-form-modifier:
      [fault-001 (s01n01), fault-002 (s01n02), fault-003 (s01n03),
       fault-004 (s01n04), fault-005 (s01n05), fault-006 (s01n08),
       fault-007 (s01n11), fault-008 (s01n12),
       fault-009 (s02n01), fault-010 (s02n02), fault-011 (s02n03),
       fault-012 (s02n04), fault-013 (s02n05), fault-014 (s02n06),
       fault-015 (s02n07), fault-016 (s02n08), fault-017 (s02n09),
       fault-018 (s02n10), fault-019 (s02n11), fault-020 (s02n12),
       fault-021 (s02n13),
       fault-022 (s03n01), fault-023 (s03n02), fault-024 (s03n03),
       fault-025 (s03n04), fault-026 (s03n05), fault-027 (s03n06),
       fault-028 (s03n07), fault-029 (s03n08), fault-030 (s03n09),
       fault-031 (s03n11), fault-032 (s03n12), fault-033 (s03n13)]
      composite_findings:
        - fault-008 also FAULT-FORM-CONJUNCTION (before-clause encodes 2 actions)
        - fault-027 also FAULT-FORM-NON-ACTION-VERB (unlicensed `holds` on a note)
        - fault-028 also FAULT-FORM-NON-ACTION-VERB (unlicensed `holds her position`) + FAULT-FORM-CONJUNCTION (comma-appended clause)
        - fault-033 also FAULT-FORM-NON-ACTION-VERB (banned `keeps`)
    fault-bone-delta-malformed:
      magnitude_below_floor:
        [fault-034 (s01n06), fault-035 (s01n07), fault-036 (s01n09),
         fault-038 (s02n03), fault-039 (s02n06), fault-040 (s02n07),
         fault-041 (s02n10),
         fault-042 (s03n03), fault-043 (s03n06), fault-044 (s03n08),
         fault-045 (s03n09)]
      speech_bone_no_axis_moves:
        - fault-037 (s01n10)

  advisory_flags:
    - flag-001: Actor slug abbreviation (unconfirmed — actor directory not
      directly readable). Draft uses `oswyn-mudway` and `wren-stitch-house`;
      series.substance.actor_baselines use `oswyn-mudway-flea-bottom-elder` and
      `wren-stitch-maker-flea-bottom-ward`. Verify at Phase 1 redo and correct
      if mismatched.
    - flag-002: c03 bones file is a contamination source for screen-writer
      shape/cadence references. Phase 2 was cascade-budget-skipped at c03;
      c03's PP-heavy style is not canon. Recommend either retroactive c03 form-
      fix or an explicit marker on c03 noting "audited under cascade-budget;
      SVO form discipline not gated at write time." Process-critic candidate.
```
