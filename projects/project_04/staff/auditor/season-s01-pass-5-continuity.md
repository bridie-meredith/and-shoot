```yaml
audit:
  scope: season
  target: s01
  pass: 5-continuity
  timestamp: 2026-05-09
  verdict: SEASON-CONTINUITY-FAIL

  findings:

    # ── SWEEP 1: REACHABILITY ──────────────────────────────────────────────────

    - id: cont-001
      type: flag
      what: >
        Season-plan H: "the maester notes Taylor's age and physical state in his
        assessment — a detail he records, not a scene Taylor controls."
        ID 921 (insert-at 862): "the maester marks the ledger entry."
      why: >
        The inserted bone satisfies the Pass 3 shape-005 fault in that a notation
        beat now exists after the maester's direct exchange with Taylor. However
        the SVO text ("marks the ledger entry") is textually indistinguishable
        from the pre-Taylor account-ledger query at IDs 841–846 (same verb, same
        object). The S2 body-clock plant depends on this bone carrying a new
        observation about Taylor's physical state or age — not a continuation of
        the household-ledger query. As an SVO bone the ambiguity cannot be
        resolved without Phase 3 dialogue content. Flagged for Phase 3
        coach/impersonator guidance: the maester's notation at this position must
        be readable as a new physical-state assessment of Taylor, not as a return
        to the account-ledger.
      routing: editor (advisory for Phase 3; escalates to fault if Phase 3 does not differentiate)

    - id: cont-002
      type: pass
      what: "Season-open → season-close reachability: IGNITION / Pryor's note / maester tier-crossing / Mira-debt / Elara irreversible action"
      why: >
        All five required season-close state-transitions are reachable from prior
        bones. IGNITION at IDs 455–474; Pryor incident folio drawn/marked/closed
        at IDs 496–499; maester visit and folio handoff at IDs 802–898; Mira
        debt transacted at IDs 628–643; Elara crosses reeve's threshold at ID 746.
        Taylor age ~9 at IGNITION is consistent with plan window (~86 AC).
        Suppression stage at S1 close is incident-response (tier-crossing via
        ferryman folio at ID 906, not policy action). No reachability gap at
        escalate scope.
      routing: ~

    # ── SWEEP 2: STATE ─────────────────────────────────────────────────────────

    - id: cont-003
      type: fault
      what: >
        The maester folio — transferred to the town reeve at ID 809 ("the town
        reeve receives the folio"), then drawn again by the maester at ID 893
        ("the maester draws the folio") at the ferry dock.
      why: >
        No bone between IDs 809 and 893 records the folio returning from the
        reeve to the maester. The object is in the reeve's hands at ID 809; at
        ID 893 the maester possesses it again without a transfer-back bone. The
        ferry-folio handoff (IDs 893–898) is the S2 hook that closes the
        denouement — its load-bearing status makes the missing transfer-back bone
        a state fault, not an editorial gap. If the folio never left the maester's
        possession (the reeve merely read it), the SVO at ID 809 ("receives")
        overstates the transfer.
      criteria: >
        Either a bone must be present between IDs 809 and 893 showing the reeve
        returning the folio to the maester, or the ID 809 bone must not describe
        a completed transfer (the reeve inspects/reads rather than receives). The
        maester must coherently possess the folio at ID 893.
      routing: fixer

    - id: cont-004
      type: fault
      what: >
        Market slip — ID 922 (insert-at 36): "oc-craftsman-father draws the
        market slip." No subsequent bone tracks the market slip's release,
        use-completion, or coherent persistence across the aggregate.
      why: >
        The market slip is introduced as a drawn object and never consumed,
        handed off, set down, returned, or referenced again. Props introduced
        must be consumed/released or persist coherently (season plan H, structural
        note re: named change at early-baseline close). An orphan prop that
        appears once and vanishes creates a state inconsistency: if Edwyn drew
        it, it must go somewhere. The insert-at target (ID 36 range) is in the
        early-baseline workshop scene; no downstream bone within that scene or
        adjacent scenes accounts for it.
      criteria: >
        The market slip must either be released (set down, read and set aside,
        handed off) within the early-baseline scene, or the insert-at bone must
        be revised to embed the prop action within a bone sequence that
        immediately accounts for it. The named change the season plan requires
        at early-baseline close must be legible from the market-slip introduction
        if it is the load-bearing beat.
      routing: fixer

    - id: cont-005
      type: flag
      what: >
        Mira-stonefield-jaehaerys first appearance — ID 429 ("mira-stonefield-jaehaerys
        faces the wool-factor's stall") — no prior entry bone.
      why: >
        Mira's state file has her at loc-river-market-town, which is consistent
        with a market-square scene presence. The season plan lists Mira as a
        witness at the IGNITION beat. The absence of an entry bone is not a
        state-file contradiction, but for a named actor (not a walk-on) the
        appearance without an establishing presence beat is an editorial gap.
        Phase 3 can render her as already present; the bones do not prevent this.
        Flagged for editor.
      routing: editor (advisory)

    - id: cont-006
      type: pass
      what: "Literacy folio (IDs 399–411), incident folio (IDs 496–499), candle (ID 148), cost-ceiling (IDs 917–918)"
      why: >
        Literacy folio: full hand-off and return cycle present (drawn ID 399,
        taken ID 405, returned ID 410, replaced ID 411). Incident folio: drawn
        ID 496, marked ID 497, closed ID 499 — retained by Pryor as institutional
        record; coherent. Candle: lit ID 148, scene closes ID 149; no release
        bone required. Cost-ceiling: inserted bones ID 917 (temple press at
        insert-at 490) and ID 918 (cradles head at insert-at 519) address
        shape-003 headache-onset requirement and are consistent with child-body
        ceiling (active control → headache). All four pass.
      routing: ~

    - id: cont-007
      type: pass
      what: "Suppression-policy stage at S1 close; Faith/Rowan constraint"
      why: >
        Denouement bones (IDs 802–912) show a single information-gathering
        maester visit — ledger query, literacy register review, folio handoff
        to ferryman. No bone reads as patterned-response or policy action. Stage
        correctly remains incident-response at S1 close per season plan H.
        Rowan interactions (IDs 152–217, 234–250, 399–412, 704–729, 865–883)
        are pastoral and institutional throughout — no armed enforcement, no
        organized faith violence. cond-faith-of-seven-jaehaerys satisfied.
      routing: ~

    # ── SWEEP 3: REFERENCE ────────────────────────────────────────────────────

    - id: cont-008
      type: flag
      what: >
        Actor slug "the maester" (IDs 802–898, ID 921 insert) vs. season plan G
        slug "oc-maester-traveler."
      why: >
        Season plan G introduces this character as "oc-maester-traveler" and
        notes "Margit provisions as a walk-on prop-actor if needed." The aggregate
        consistently uses "the maester" — a legal `the <noun>` walk-on form. No
        actor state file for `oc-maester-traveler` or `the-maester` was found.
        If Margit provisioned `oc-maester-traveler` as an actor card, the
        aggregate's slug form is an orphan reference. If Margit treated the
        character as a `the <noun>` walk-on, the slug is legal. Cannot resolve
        without checking Margit's provision record.
      routing: editor (verify Margit provision status; escalate to fault if oc-maester-traveler actor card exists)

    - id: cont-009
      type: flag
      what: >
        ID 920 (insert-at 787): "taylor-hebert-jaehaerys grips the chair edge."
        The workshop interior uses "bench," "stool," and "ledger bench" throughout
        (IDs 23, 30, 48, 525, 666, 679, 722, 788, etc.). "Chair" does not appear
        elsewhere in the aggregate.
      why: >
        Not an orphan reference (no prop card required for furniture) but a
        terminology inconsistency within the established workshop interior.
        "Chair" vs. "bench/stool" is an editorial concern for Phase 3 continuity.
        Flagged for editor.
      routing: editor (advisory)

    - id: cont-010
      type: pass
      what: "Actor slugs: named cast (8 actors) and walk-on forms"
      why: >
        All eight named cast actor state files resolved. Walk-on forms (the
        fishwife, the inquiry rider, the ferryman, the town reeve, the collector,
        a collector's man, the garrison man, a townsman, a clerk, a mounted man)
        are legal `the/a <noun>` environment references per schema. No orphan
        named-actor slug introductions found.
      routing: ~

    - id: cont-011
      type: pass
      what: "Location slugs (warehouse cards) and sub-location references"
      why: >
        All four named location cards resolve: loc-craftsman-workshop-home,
        loc-market-square, loc-local-sept, loc-river-ferry-dock, and
        loc-river-market-town. Sub-location references (the alley, the
        wool-factor's stall, the craft lane, the reeve's house, the craftsman
        district, the dock, the sept) are legal `the <noun>` environment
        references. Season plan G explicitly states wool-factor's stall and
        alley require no new card.
      routing: ~

    - id: cont-012
      type: pass
      what: "Inserted beats IDs 916–922 — reference resolution"
      why: >
        ID 916: insect/environment reference, legal. ID 917, 918, 919, 920:
        taylor-hebert-jaehaerys — resolved actor. ID 921: "the maester" — see
        cont-008 flag. ID 922: oc-craftsman-father — resolved actor; market-slip
        prop is the novel introduction (see cont-004 fault). No additional orphan
        references beyond those already classified.
      routing: ~

    # ── SWEEP 4: POV ──────────────────────────────────────────────────────────

    - id: cont-013
      type: pass
      what: "All five POV markers present at correct positions"
      why: >
        1. `# pov: taylor-hebert-jaehaerys` — line 6, before ID 1. Present.
        2. `# pov: mira-stonefield-jaehaerys` — line 620, before ID 565. Present.
        3. `# pov: taylor-hebert-jaehaerys` — line 710, before ID 645. Present.
        4. `# pov: oc-craftsman-mother` — line 776, before ID 701. Present.
        5. `# pov: taylor-hebert-jaehaerys` — line 873, before ID 789. Present.
        All five present. Count verified.
      routing: ~

    - id: cont-014
      type: pass
      what: "POV switch boundaries — reachability from prior bones"
      why: >
        Taylor→Mira (before ID 565): Mira established on-stage at IDs 558–562
        (exits alley, speaks, retreats). Taylor follows (ID 563). Switch is
        reachable. Mira→Taylor (before ID 645): Mira exits alley at ID 641;
        Taylor holds feet (642), exhales (643). Switch is clean. Taylor→Elara
        (before ID 701): Elara last in workshop at IDs 692–698; Elara's approach
        to sept (ID 702) follows gap bone at 700. Switch is reachable. Elara→
        Taylor (before ID 789): Taylor on-stage in family re-cohesion scene from
        ID 767; transition at ID 787–788 clean. All four switch boundaries
        reachable from prior bones.
      routing: ~

    - id: cont-015
      type: pass
      what: "POV drift — no Taylor-exclusive beats inside Mira or Elara stretches"
      why: >
        Mira POV (IDs 565–644): no insect-sense beats, no Taylor interior-only
        beats. All Taylor actions (IDs 568, 570, 573–574, 577, 581, 629–642) are
        externally observable. Elara POV (IDs 701–788): no Taylor swarm-sense or
        interior-only beats. Taylor's actions from ID 767 onward (holds eyes,
        speaks, holds breath, faces table) are externally observable from Elara's
        position. No POV drift.
      routing: ~
```

---

## Summary

**File-level verdict: SEASON-CONTINUITY-FAIL**

**Finding counts by sweep:**
- Reachability: 1 pass, 1 flag (cont-001 — maester notation ambiguity; body-clock plant SVO indistinguishable from prior ledger query)
- State: 2 faults (cont-003 — maester folio transfer gap; cont-004 — market-slip orphan prop), 1 flag (cont-005 — Mira entry bone absent), 1 pass
- Reference: 2 flags (cont-008 — `the maester` slug vs. plan's `oc-maester-traveler`; cont-009 — `chair` vs. `bench` terminology), 2 passes
- POV: 3 passes, 0 faults, 0 flags

**Routing recommendation:**
Two faults route to fixer. Both are line-scope: cont-003 requires either a folio-return bone between IDs 809–893 or revision of ID 809's transfer verb; cont-004 requires a release or use-completion bone for the market slip within the early-baseline scene, or revision of the insert-at 36 bone. No escalation — all faults are episode/aggregate scope, correctable by line insertion or verb revision. Flags are advisory for editor and Phase 3 coach; the `the maester` slug flag (cont-008) should be verified against Margit's provision record before Phase 3 dispatch. Phase 2 does not converge cleanly until the two faults are resolved.
