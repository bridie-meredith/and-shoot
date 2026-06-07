```yaml
audit:
  scope: chapter
  target: b01c04
  timestamp: 2026-05-27
  trigger: "/and-write b01c04 Phase 2 re-audit on redo — DEC-0030 follow-up"

  summary:
    verdict: FAIL
    fault_count_hard: 2
    bones_audited: 33
    per_class_counts:
      FAULT-FORM: 0
      FAULT-CONSTRAINT: 0
      FAULT-PHYSICAL: 1
      FAULT-BONE-DELTA-MALFORMED: 1
      FAULT-AGGREGATE-DELTA-MISMATCH: 0
      FAULT-COST-LEDGER-UNRESOLVED: 0
    recurrence_vs_prior:
      - "FAULT-FORM-MODIFIER: NOT RECURRENT — all 33 bones PP-clean. Corrective brief worked on its primary target."
      - "FAULT-BONE-DELTA-MALFORMED magnitude-floor: NOT RECURRENT — all 7 moving bones at magnitude 1.0; no 0.5 splits."
      - "FAULT-BONE-DELTA-MALFORMED speech-bone-no-axis: NOT RECURRENT — both dialogue-anchor bones carry communication-class axes."
      - "Actor-slug abbreviation (prior flag-001): PARTIALLY RECURRENT — oswyn-mudway vs canonical oswyn-mudway-flea-bottom-elder is now confirmed as a FAULT-PHYSICAL. wren-stitch-house remains unconfirmed (flag promoted below)."
      - "New fault class introduced by redo: FAULT-BONE-DELTA-MALFORMED shape-vs-axes_held (s01n10)."

  clean_pass_checks:
    - "PP ban (place/direction/source/destination/instrument/accompaniment/time): PASS — all 33 bones PP-clean"
    - "Magnitude floor (≥1.0 per moving bone): PASS — 7 moving bones, all at magnitude 1.0; no 0.5 splits"
    - "Speech-bone communication-class axis: PASS — s01n06 (social_tether-antag), s01n08 (position-prot-rise) both confirmed"
    - "Canonical speech form (speaks to): PASS — both dialogue-anchor bones use licensed form"
    - "Holds license: PASS — two instances (s01n07, s02n10), both body-part DO (feet), both licensed"
    - "Banned verbs (keeps/maintains/sustains/senses/feels/experiences/notices/realizes/recognizes): PASS — none present"
    - "turns to ban: PASS — not present"
    - "Copula ban: PASS — no is/was/were/be/been/being in any SVO"
    - "Negation ban: PASS — no not/don't/didn't in any SVO"
    - "Conjunction ban (and/but/while/as): PASS — none in SVOs"
    - "Temporal subordinate clauses (before/after): PASS — none"
    - "Perception verb ban: PASS — registers with insect-feed as subject (feed returns) is canonical per c03 precedent and c02 reference"
    - "Interiority ban: PASS — all SVOs are external/physical actions"
    - "Multi-subject ban: PASS — plural collective nouns (the stitch-house frames) follow established b01-c02 pattern (the flies, the insects)"
    - "Abstraction-as-object: PASS — compound feed-output nouns (junction-agitation, oswyn-mudway interval, discard-air) follow b01-c02 vocabulary precedent"
    - "Theme-silence (no 'protection and the trap' verbatim): PASS — thesis phrase absent from all 33 SVOs"
    - "Earth-Bet proper-noun fence: PASS — no parahuman jargon"
    - "Worm-canon sequential acquisition: PASS — s02 = day 1 (wards 1+2), s03 = day 2 (ward 3); distinct bone structure"
    - "Worm-canon anchor-discipline (two bone-level contents per scene): PASS — s02 n09+n10; s03 n11+n12"
    - "Westerosi magic dormant: PASS"
    - "Dragon proximity: PASS"
    - "KL court state / geography: PASS"
    - "FAULT-AGGREGATE-DELTA-MISMATCH: PASS — all 5 axes exact at scene and chapter level (capability +2.0, position-prot-rise +1.0, social_tether-prot-rise +2.0, social_tether-antag +1.0, position-world +1.0)"
    - "FAULT-COST-LEDGER-UNRESOLVED: PASS — cl-antag-d03, cl02, cl03a, cl03b, cl-world-d04 all resolve against cost_ledger[]"
    - "Axis slugs in axis_moves[] valid: PASS — social_tether-antag, position-prot-rise, capability, social_tether-prot-rise, position-world all in state_axes[]"
    - "Axis slugs in axes_held[] valid: PASS — moral_framework, relational_anchor_status, political_register-prot, moral_legibility_to_self all in state_axes[]"
    - "Sensory grounding quota (≥1 per scene): PASS — s01:1, s02:3, s03:3"
    - "Scene conflict coverage: PASS — protagonist_force + opposing_force bones present in all three scenes"
    - "Bone count: PASS — 33 bones within chapter contract range (15-75)"

  recurrence_prevention_assessment: |
    DEC-0030's corrective brief succeeded on its three declared targets:
    (1) PP ban enforcement: 33/33 bones PP-clean. No place, direction, source, destination,
        instrument, accompaniment, or time PPs in any SVO text. The primary failure pattern
        from the prior 45-finding audit is fully remediated.
    (2) Magnitude floor: All 7 moving bones at 1.0. The 0.5+0.5 pair-split pattern that
        produced 11 FAULT-BONE-DELTA-MALFORMED findings is gone. Consolidation is executed
        correctly throughout.
    (3) Speech-bone-no-axis: Both dialogue-anchor bones carry communication-class axes.
        s01n06 (social_tether-antag tether/trust class), s01n08 (position-prot-rise
        position/reputation class). The specific fault that produced fault-037 in the prior
        audit is resolved.
    The redo introduced one new fault not present in the prior draft (s01n10 shape/axes_held
    mismatch) and promoted one prior advisory flag to a confirmed fault (oswyn-mudway slug).
    Both are isolated, fixer-scope.

findings:

  - id: fault-001
    type: fault
    class: FAULT-PHYSICAL
    bone: b01c04s02n06
    svo: "the insect-feed returns oswyn-mudway"
    what: >
      Actor slug `oswyn-mudway` does not match the canonical form `oswyn-mudway-flea-bottom-elder`
      as recorded in memory.md series.substance.actor_baselines[actor: oswyn-mudway-flea-bottom-elder].
      The redo uses the abbreviated form in two bones: s02n06 and s02n07 (where it also appears
      as DO in compound noun form "the oswyn-mudway interval").
    why: >
      Slug mismatch between the bones file and the cast roster / actor_baselines will cause
      the /and-write Phase 7 slug-grep (bones file cast field computation) and /and-facets
      Phase 0 parser to emit a mismatched cast entry. If dialogue files or state-update facets
      reference the canonical slug, the citation chain breaks. Prior audit flag-001 (unconfirmed)
      is confirmed as a fault at this re-audit because the canonical slug is directly readable
      from memory.md actor_baselines at line 1039.
    criteria: >
      Replace `oswyn-mudway` with `oswyn-mudway-flea-bottom-elder` in s02n06 SVO and
      s02n07 SVO (and DO compound noun "the oswyn-mudway-flea-bottom-elder interval" or
      restructure the compound noun to avoid the full slug as noun — e.g. "the oswyn interval"
      or "the elder-ward interval" if the slug is too long for compound-noun form). Both
      instances must use the canonical slug or a restructured DO that avoids the slug-as-noun
      problem.
    additional_instances:
      - bone: b01c04s02n07
        svo: "taylor-hebert-kl-122ac maps the oswyn-mudway interval"
        note: >
          oswyn-mudway appears here as the possessive root of the compound noun
          "the oswyn-mudway interval." The DO compound noun must be restructured if the
          full canonical slug cannot form a clean compound noun.

  - id: fault-002
    type: fault
    class: FAULT-BONE-DELTA-MALFORMED
    bone: b01c04s01n10
    svo: "taylor-hebert-kl-122ac exits the cooper's yard"
    what: >
      Bone is declared `shape: chatter` but carries a populated `axes_held` list
      (axis: relational_anchor_status, with rationale). A chatter bone has neither
      axis_moves nor axes_held populated. A bone with populated axes_held must be
      declared `shape: held` (or `shape: moving` if axis_moves are also present).
      The shape declaration `chatter` conflicts with the bones's structural role as a
      held-axis enactment.
    why: >
      The shape field is the gate-check handle for the substance bone-gate and for
      /and-review bones fidelity checking. A chatter bone with axes_held populated is
      invisible to the held-bone accounting: the held axis does not get credited in the
      gate's held-coverage scan, and the bone's cost_ledger_anchor is absent (chatter
      without anchor is a separate malformation, but here the anchor is absent because
      the author intended this as a held bone, not a chatter bone). The
      relational_anchor_status hold enacted at chapter close (Taylor exits without
      performing Wren's street-walk) is narratively load-bearing; it must be correctly
      typed to survive the /and-review bones gate.
    criteria: >
      Change `shape: chatter` to `shape: held` on b01c04s01n10. Remove the
      `cost_ledger_anchor` field if present (held bones are exempt from the anchor
      requirement). The axes_held population and rationale are correct as authored;
      only the shape declaration requires correction.

advisory_flags:

  - id: flag-001
    type: flag
    bone: "b01c04s02n09, b01c04s03n11"
    svo: "the insect-feed returns wren-stitch-house"
    what: >
      Actor slug `wren-stitch-house` is used in s02n09 and s03n11. Prior audit flag-001
      identified this as a possible abbreviated form vs canonical `wren-stitch-maker-flea-bottom-ward`.
      The Wren actor_baselines entry was not readable in the memory segments available to
      this audit (the entry appears to lie between Halvard's section and the cost_ledger,
      a range where Wren's actor block may not have been authored at actor_baselines time
      given that [cost-bearer] identity was TBD at /and-cast). The slug cannot be confirmed
      or denied as abbreviated at this audit.
    why: >
      If Wren's canonical slug is `wren-stitch-maker-flea-bottom-ward`, the same downstream
      citation-chain breakage applies as for oswyn-mudway. If `wren-stitch-house` is the
      canonical slug (as authored in /and-cast or in Wren's actor card), no fault exists.
    resolution: >
      Fixer must confirm Wren's canonical slug against active-project/actors/ directory
      and/or Wren's card at active-project/actors/wren-*/. If canonical slug differs from
      `wren-stitch-house`, upgrade this flag to a fault and apply the same correction
      pattern as fault-001.

  - id: flag-002
    type: flag
    bone: "chapter-level"
    what: >
      s01n10 (now flagged as fault-002 shape mismatch) does not carry a cost_ledger_anchor.
      If corrected to shape: held, this is structurally correct (held bones are exempt from
      the anchor requirement). However, the scene-level axis_aggregate_check in the redo
      does not list relational_anchor_status as an in-motion axis for s01 — it appears only
      in axes_held. This is consistent with the chapter contract (relational_anchor_status
      is a held axis for this chapter). No aggregate fault. Flagging only to note that
      the correction of fault-002 must not accidentally add relational_anchor_status to
      the s01 axis_moves[] — the bone is held-only, no Δ.
    why: "Downstream protection: the held bone must not be miscounted as a moving bone at /and-review bones."
    resolution: "Confirm held-only on correction. No Δ on relational_anchor_status for this chapter."
```

---

## Fault inventory (plain text)

**fault-001** (FAULT-PHYSICAL) — b01c04s02n06, b01c04s02n07  
Actor slug `oswyn-mudway` does not match canonical `oswyn-mudway-flea-bottom-elder` (confirmed at memory.md line 1039). Promoted from prior audit flag-001 (unconfirmed) to confirmed fault. Two bones affected: s02n06 SVO and s02n07 compound-noun DO.  
Fixer criteria: replace abbreviated slug with canonical form in both bones.

**fault-002** (FAULT-BONE-DELTA-MALFORMED) — b01c04s01n10  
Shape declared `chatter` but `axes_held` is populated (relational_anchor_status with rationale). Shape must be `held`. New fault not present in prior draft; introduced by the redo's held-bone authored under a chatter shape declaration.  
Fixer criteria: change `shape: chatter` to `shape: held`. No other change needed.

---

## Recurrence prevention confirmation

Per dispatch requirements:

| Prior failure pattern | Status in redo |
|---|---|
| FAULT-FORM-MODIFIER (33 bones) | RESOLVED — 0 PP violations |
| FAULT-BONE-DELTA-MALFORMED magnitude 0.5 (11 bones) | RESOLVED — all 7 moving bones at 1.0 |
| FAULT-BONE-DELTA-MALFORMED speech-bone-no-axis (1 bone) | RESOLVED — both dialogue-anchors carry communication-class axes |
| Actor-slug abbreviated form (prior flag, unconfirmed) | PARTIALLY RESOLVED — oswyn confirmed as fault; wren unresolvable without actor directory |

DEC-0030 corrective brief is confirmed to have worked on its three declared targets. The two new findings (1 confirmed fault, 1 promoted-from-flag fault) are fixer-scope with minimum-change resolution paths. Neither finding implicates the SVO discipline or magnitude architecture of the redo.
```
