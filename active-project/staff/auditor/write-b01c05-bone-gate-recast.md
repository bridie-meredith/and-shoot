```yaml
audit:
  scope: bone
  target: b01c05s02@13-recast
  timestamp: 2026-05-29
  trigger: /and-write b01c05 revise Phase 6 — single verb recast, @13 "pin" → "strike"; DEC-0042
  checks_run: [phase-2-svo, phase-5-continuity, phase-6-bone-gate]
  findings:

    - id: check-001
      type: pass
      what: "@13 SVO form — 'the three figures strike the courier'"
      why: |
        Subject: "the three figures" is a `the <noun>` collective noun-phrase acting as single
        grammatical subject. Precedent: identical subject form at @11 and @12 passed prior SVO
        audits without FAULT-FORM-MULTI-SUBJECT. Verb: "strike" is a concrete physical transitive
        verb, observable by any witness (including insect-feed). Not in any deny-list (copula,
        negation, perception, non-action, possession, stative, disallowed holds). No modifiers,
        no adverbs, no prepositional phrases of place/direction/instrument/accompaniment. Object:
        "the courier" is a physical named entity in `the <noun>` form, established throughout
        @8-@22. No abstraction-as-object. No conjunction. No interiority. SVO is clean on all
        nine FAULT-FORM-* axes.

    - id: check-002
      type: pass
      what: "Gap-instrument triple @14-@15-@16 coherence under 'strike' recast"
      why: |
        The protected triple begins at @14 (side-alley returns the sound), not @13. The recast
        does not alter @14, @15, or @16. Physical coherence of the new sequence: @13 strike
        (force-application, discrete completed event) → @14 side-alley returns sound (acoustic
        consequence physically entailed by a blow against a body in a stone-walled alley) →
        @15 courier raises the spine (recovery precursor, unchanged) → @16 courier finds the
        feet (closes recovery, unchanged). The sequence is more explicit under "strike" than
        under the prior "pin" because "strike" is a discrete event that precedes the sound
        rather than a sustained state concurrent with it. Scene-map's protected-pattern entry
        for the triple is unaffected. No coherence fault.

    - id: check-003
      type: pass
      what: "Constraint card and series law check for 'strike' in alley enforcement context"
      why: |
        Five series laws checked: cond-override-architecture-residue-122ac (controls Taylor's
        insect-override architecture, not third-party physical violence), cond-earth-bet-noun-fence
        ("strike" is not Earth-Bet parahuman jargon), cond-westerosi-magic-dormant-122ac (no
        magic implication), cond-dragon-proximity-122ac (N/A), cond-kl-witch-label-formation-122ac
        (concerns Taylor's public insect-sense use being observed; @13 is three unnamed figures
        acting; Taylor is at the wall-line through the feed — no witch-label trigger).
        Chunk authority explicitly licenses the violence type: "enforcement, not robbery";
        "controlled containment"; "coordinated." "Strike" as force-application is inside that
        license. Series behaviors: cond-taylor-pov-behavior (Taylor first-person only) — @13
        subject is "the three figures," an external subject observable through the insect-feed.
        No POV violation. No constraint fires negatively.

    - id: check-004
      type: pass
      what: "Per-bone held-axis classification — moral_framework held, rationale present"
      why: |
        DEC-0042 entry in showrunner memory records: axes_held: [{axis: moral_framework,
        rationale: "enforcement violence is the s02 opposing_force enacted as a specific physical
        act — the strike is the faction-violence content the discipline absorbs as
        enforcement-not-robbery; inside the licensed exception; moral_framework held at current
        crack-level"}], axes_in_motion: []. Cross-checked against (a) scene-level s02
        substance_delta: axes_in_motion: [], axes_held includes moral_framework; (b) chapter-level
        substance_delta: moral_framework held with rationale "no new licensed exception;
        rationalization of d04 acceptance is stable; framework at current crack-level"; (c) s02
        scene_conflict.stakes_axis: moral_framework. The classification is internally consistent
        at bone, scene, and chapter levels. The rationale is non-boilerplate and specifically
        tied to the opposing_force definition ("enforcement incident's specificity — coordinated,
        directed at a named body for a named reason; the content has named itself as
        faction-violence in a way Hook content never did"). Axis is load-bearing. Classification
        is correct.

    - id: check-005
      type: pass
      what: "Event_map coverage — enforcement event covered by @13 strike + @14 sound"
      why: |
        Scene-map B annotation lists @13 as a peak-shadow bone with updated label "three figures
        strike courier — force-application beat; enforcement-type specificity." The chunk event
        ("courier roughed up; enforcement not robbery; controlled containment; coordinated")
        is covered by @11 (enter side-alley) + @12 (close alley-mouth) + @13 (strike courier)
        + @14 (side-alley returns sound). Under the prior "pin," @13 covered containment-in-
        progress and @14 covered the sound; the violence-type was inferential. Under "strike,"
        @13 directly bone-realizes force-application and @14 delivers the acoustic consequence.
        Coverage is more explicit than before, not less. No event that was covered is now
        uncovered. The cold-read FAIL that triggered DEC-0042 was precisely that "pin" left
        the violence-type ambiguous; "strike" resolves that ambiguity at the bone level, making
        the coverage more faithful to the chunk's explicit enforcement-beating characterization.

    - id: check-006
      type: pass
      what: "FAULT-DIALOGUE-* applicability check"
      why: |
        Chapter b01c05 has no speech bones: Phase 1.5 was SKIPPED (no speech-form or
        communication-axis bones — chapter is interior/observational). @13 is not a dialogue-
        anchor bone. DEC-0042 changes @13 verb only; no flat_id changes, no dialogue citation
        changes, no communication-axis axis_moves declared. FAULT-DIALOGUE-* family is N/A
        for this chapter and this recast.

    - id: check-007
      type: pass
      what: "Sensory-grounding at @13 and @14"
      why: |
        @13 "the three figures strike the courier" — concrete physical act between physical
        entities in physical space, directly observable through the insect-feed. Grounding-class
        bone by definition. @14 "the side-alley returns the sound" — concrete environmental
        event (acoustic return in stone-walled alley); scene-map identifies @14 as the scene-B
        peak bone ("the world delivers what the feed cannot categorize"). The sensory:2 facet
        citation was re-anchored to @14 in the /and-facets re-run (memory: "sensory:2
        re-anchored @13 → @14") and is unaffected by the recast because @14 is unchanged.
        DEC-0042 notes a soft seam to /and-facets (the "held against stone" texture previously
        entailed by "pin" is now only available via @11-@12 geometry + chunk text + oc-rushwick
        card), but this is a downstream facet-authoring note, not a bone-level sensory-grounding
        fault. Both @13 and @14 are grounding-class bones.

  summary:
    hard_count: 0
    signal_count: 0
    flag_count: 0
    verdict: PASS
    note: |
      All seven mechanical checks pass. The recast of @13 "pin" → "strike" introduces no new
      FAULT-FORM-*, FAULT-CONSTRAINT-*, FAULT-PHYSICAL-*, FAULT-BONE-DELTA-MALFORMED-*,
      FAULT-CONTINUITY-*, FAULT-POV-*, or FAULT-DIALOGUE-* findings. The held-axis
      classification (moral_framework, held) is correct and internally consistent across bone,
      scene, and chapter levels. The gap-instrument triple @14-@15-@16 is unaffected. The
      enforcement event_map coverage is strengthened, not weakened. The one soft seam
      (oc-rushwick "held against stone" texture previously entailed by "pin") is a downstream
      /and-facets advisory already recorded in DEC-0042 and does not constitute a bone-gate
      fault.
```
