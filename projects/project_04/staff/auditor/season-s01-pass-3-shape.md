```yaml
audit:
  scope: season
  target: s01
  pass: 3-shape
  timestamp: 2026-05-09
  verdict: RE-ORDER-OR-REVISE
  structural-ranges:
    season-buildup: "1–418"
    season-climax: "419–519  # peak: 455–474"
    season-denouement: "800–912"

  findings:

    - id: shape-001
      type: fault
      what: "IDs 32–60 — 29 consecutive lines in the early-baseline stretch (workshop re-entry through evening bowl scene)"
      why: >
        Three consecutive functional sub-scenes (father returns from market, evening meal, parental conversation)
        contain no stakes escalation, no new information that changes Taylor's position, and no character action
        with downstream consequence. The insect-ecology beats (IDs 27–28: fly at ink-pot) land before this
        block and do not recur inside it. The block is domestic texture without a load-bearing beat — it runs
        to Taylor closing her eyes (ID 80) with no inflection anchored between 32 and 62. This is a flatline
        inside the first sub-arc of the early-baseline stretch. By strict-mode definition, IDs 32–60 qualify
        as an inert stretch.
      criteria: >
        The stretch must contain at least one beat that escalates Taylor's stakes, registers new information,
        or commits a character action with downstream consequence before ID 62. A single insect-ecology
        inflection beat or a parental observation that marks a named change in the household's relationship
        to Taylor would satisfy. The named change required by the season plan ("one thing in the household is
        different at beat-close from beat-open") must be visible here or immediately adjacent.
      routing: fixer

    - id: shape-002
      type: fault
      what: "IDs 654–699 — Taylor POV stretch 2 (post-IGNITION family return)"
      why: >
        46 lines covering Edwyn's return to workshop, private ledger review, and Elara's market-basket
        re-entry contain no load-bearing beat registering IGNITION's consequence inside the family unit from
        Taylor's POV. The IGNITION event closes at approximately ID 519; the Elara interlude does not begin
        until ID 701. The 46-line Taylor stretch in between (IDs 654–699) is transit — physical re-entry,
        ledger review, Elara re-entry — without an inflection beat. Taylor's changed situation post-IGNITION
        (she is no longer invisible; the note exists) does not register on-page in her POV before the Elara
        interlude. This is a flatline at a structurally critical juncture: the falling action has not begun
        in Taylor's register.
      criteria: >
        At least one proto-line in IDs 654–699 must carry the weight of Taylor's post-IGNITION changed
        state as an active beat — not ambient processing, but a discrete action, observation, or decision
        that marks her awareness of the new board. The ledger scene (IDs 676–690) is the most viable
        location for this anchor. The beat must be distinguishable from the baseline ledger-review beats
        that precede the ignition.
      routing: fixer

    - id: shape-003
      type: fault
      what: >
        IDs 490 and 519 (blank lines in aggregate) — missing child-body cost-onset beats during and
        immediately after IGNITION
      why: >
        The season plan committed explicitly: "The cost mechanic (headache onset at IDs 490, 519) should
        land the climax cleanly." IDs 490 and 519 are gap/blank lines in the aggregate. The closest
        approximation in the surrounding bones — ID 504 (taylor-hebert-jaehaerys clenches the jaw) and
        ID 505 (taylor-hebert-jaehaerys exhales) — are generic physical-affect beats that do not commit
        the headache-onset signal the plan specified. The child-body cost ceiling is a binding constraint
        (persona card: "sustained active control of 3–10 minutes produces headache onset"). The IGNITION
        is the only active-control event in S1. The cost must be marked as a discrete named beat.
        Without it, the climax does not close cleanly and the cost mechanic that anchors the suppression-arc
        logic (the swarm is involuntary AND costs Taylor physically) is not on the page.
      criteria: >
        At minimum one proto-line must explicitly commit Taylor's physical cost state during or immediately
        after the swarm contraction (IDs 474–519 range). The beat must be readable as a consequence of
        active swarm use, not ambient stress. The plan-specified locations are IDs 490 and 519; fixer may
        place the beat at either or at an adjacent line, provided the cost-onset is unambiguous.
      routing: fixer

    - id: shape-004
      type: fault
      what: "ID 787 — single closing line for Elara-interlude beat-close and Taylor's present-tense decision"
      why: >
        The season plan committed: "Taylor closes the beat facing a present-tense decision: both parents
        are now acting in concert, and she must choose whether to begin lying explicitly to them or accept
        the closing of her operational cover." ID 787 (taylor-hebert-jaehaerys faces the table) is the
        sole beat available to carry this structural weight. One SVO line of positional description cannot
        sustain the named present-tense decision the plan required. The Elara interlude's resolution
        depends on Taylor's decision being readable at beat-close; without it, the interlude resolves as
        Elara's arc only and Taylor's cost (her management options closing) is not on the page. The
        resolution discharges Elara's stakes without discharging Taylor's.
      criteria: >
        One or two additional proto-lines must anchor Taylor's present-tense decision at the Elara-interlude
        close (IDs 785–788 range). The beat does not require interiority — the bones are SVO only —
        but the physical action committed must be readable as a decision-state: Taylor doing something
        (holding a position, releasing a grip, facing a direction) that registers the closing of her
        management options as a concrete change in her body or behavior.
      routing: fixer

    - id: shape-005
      type: fault
      what: >
        Maester-visit beat (IDs 854–862) — missing notation proto-line for body-clock/age assessment
      why: >
        The season plan committed: "the maester notes Taylor's age and physical state in his assessment —
        a detail he records, not a scene Taylor controls." This is designated the S2 body-clock plant:
        the adolescent-body ceiling transition at ~age 13–14 is seeded here. In the aggregate, IDs 839–846
        cover the maester's ledger-query notation (pre-Taylor); IDs 848–863 cover maester speaking to the
        family and directly to Taylor. There is no proto-line after ID 860 (taylor speaks to maester)
        in which the maester draws or marks a notation that includes Taylor's physical state or age. The
        plant is absent. Without it, the denouement does not deposit the S2 hook the plan specified.
      criteria: >
        A proto-line must be added in IDs 861–863 range in which the maester draws or marks a notation
        after his direct exchange with Taylor — a discrete recording action that the bones can carry as
        the age/physical-state notation. The notation must occur after the maester's assessment of Taylor,
        not before.
      routing: fixer

    - id: shape-006
      type: flag
      what: "Early-baseline beat-close named change (plan commitment)"
      why: >
        The season plan's structural note states: "Aggregate authoring must identify one named thing that
        is concretely different at beat-close from beat-open. Not a mood shift — a social or physical fact."
        The early-baseline stretch (IDs 1–149) closes with Taylor holding her eyes (ID 147), candle catching
        (ID 148), father marking ledger (ID 149). The named change in social or physical fact is not
        legible in the bones. The ledger mark (ID 149) is closest — if the ledger entry marks a trade-fact
        change (Edwyn returning with market news that "changes the household's week" per the plan), this
        could satisfy; but the SVO at ID 149 is "oc-craftsman-father marks the ledger entry" — no
        distinguishing information about what changed. Editor should verify whether dialogue content in
        Phase 3 makes this concrete. If not, this escalates to fault.
      routing: editor (advisory; escalates to fixer if Phase 3 dialogue does not anchor the named change)

    - id: shape-007
      type: flag
      what: "Mira-interlude rendering constraint (plan carry-forward)"
      why: >
        The season plan's rendering constraint: "Render Mira's political arithmetic — what visibility
        costs — not sympathetic deliberation." The bones (IDs 565–644) are structurally clean and the
        local arc passes. The rendering constraint is a Phase 3 dialogue concern, not a bone-level structural
        fault. Flagged for Phase 3 coach/impersonator guidance. Mira's cost-calculation (what withholding
        from Pryor costs her vs. what disclosure costs Taylor) must read as calculation, not as warmth or
        loyalty. The alley-return exchange (IDs 628–643) is the primary delivery point.
      routing: editor (advisory for Phase 3)

    - id: shape-008
      type: flag
      what: "Elara-interlude rendering constraint (plan carry-forward)"
      why: >
        The season plan's rendering constraint: "Render failure-mode cost in what Elara does not understand,
        not what she resolves." The bones are structurally adequate through ID 787. The rendering constraint
        is Phase 3 dialogue scope. Flagged for Phase 3. The Rowan scene (IDs 714–728) and the reeve visit
        (IDs 744–747, content unspecified in SVO) are the primary delivery points for Elara's failure-mode
        costs. The SVO at ID 747 (reeve's door closes) gives no bones-level signal of what Elara said or
        accomplished; Phase 3 must carry this.
      routing: editor (advisory for Phase 3)

    - id: shape-009
      type: pass
      what: "Season-wide escalation arc — buildup integrity (IDs 1–418)"
      why: >
        The buildup arc is structurally present and rising. Stakes-trajectory: static at baseline
        (IDs 1–80), rising via sept access (IDs 151–217), spiking via child-witness scrutiny (IDs 261–314),
        spike-continuing via census dock (IDs 329–417). Each beat closes on a changed condition: sept
        establishes Rowan's pastoral claim; child-witness slip creates the unmanageable variable (Clem);
        census closes a management option (literacy folio + Rymer filing Taylor). Antagonist agency: Pryor
        is active (stylus pause, dual folios, Rymer positioned). Try-fail integrity: Taylor holds still
        through census (successful suppression), at cost of the literacy folio handoff she cannot prevent.
        Buildup passes.
      routing: ~

    - id: shape-010
      type: pass
      what: "Season climax — IGNITION beat (IDs 419–519)"
      why: >
        Rise-peak-fall shape is intact at the beat level. Rise: collector queue, weight dispute escalation
        (IDs 434–454). Peak: swarm mass and expansion (IDs 455–465), chaos and structural consequence
        (IDs 466–474: horse rears, table overturns, levy roll falls, collector retreats). Fall: swarm
        contracts and releases (IDs 474–480), Pryor documents (IDs 492–500), family draws Taylor away
        (IDs 502–519). Peak is load-bearing and non-reversible — the note exists. Antagonist agency: Pryor
        draws incident folio (ID 496), marks it (ID 497), faces the stall edge (ID 498). The swarm event
        is correctly involuntary (triggered by coercion-of-smallfolk reflex per persona card). Climax passes,
        subject to fault-003 (missing cost-onset beat).
      routing: ~

    - id: shape-011
      type: pass
      what: "Season denouement — networked surveillance beat (IDs 800–912)"
      why: >
        Denouement structure is present. The maester functions as a Pryor-originated move dressed as
        institutional routine (season plan commitment honored: IDs 802, 808 — maester arrives with
        folio from Pryor). The institutional tier-crossing is legible: maester conducts ledger query +
        direct Taylor assessment + sept register review + folio handoff to ferryman. The closing image
        sequence (IDs 900–912: sept fly orbits basin, dock mosquito circles, ferry folio crosses water,
        Taylor on loft, mother calls) is a networked-surveillance image that establishes the new
        equilibrium. The S2 hook (folio traveling via ferryman, 909) is present. Denouement passes,
        subject to fault-005 (missing age/physical-state notation).
      routing: ~

    - id: shape-012
      type: pass
      what: "Mira-interlude — local arc (IDs 565–644)"
      why: >
        Local arc: rise via alley confrontation and Mira's political exposure (IDs 565–581), spike via
        Pryor inquiry at stall (IDs 599–626), fall via alley return and debt transaction (IDs 628–643).
        Inflection: ID 618 (Pryor marks folio after Mira's testimony — withholding transacted). End state
        differs from start state: Mira has withheld from Pryor and Taylor now carries a real unnamed debt.
        No flatlines. Local arc passes.
      routing: ~

    - id: shape-013
      type: pass
      what: "Elara-interlude — local arc (IDs 701–788)"
      why: >
        Local arc: rise via Rowan pastoral session (IDs 704–729), spike via Elara's irreversible action
        at reeve's house (IDs 741–747), fall via family re-cohesion scene (IDs 751–787). Inflection 1:
        ID 722 (Elara grips bench edge — commits to action). Inflection 2: ID 746 (crosses threshold —
        irreversible action executed). Close: ID 787 (Taylor faces table). Local arc structurally present.
        Subject to fault-004 (weight of the close insufficient for the named decision).
      routing: ~

    - id: shape-014
      type: pass
      what: "Sept-access sub-arc — local arc (IDs 151–250)"
      why: >
        Rise via reading access and fly-at-basin surveillance (IDs 159–175), inflection at ID 206–213
        (volume offered/taken — Rowan's pastoral claim transacted). Fall via Taylor exiting (IDs 214–217)
        and mother reclamation (IDs 220–231). End state differs: the sept is Taylor's literacy node and
        Rowan holds the first pastoral claim she did not choose. Local arc passes.
      routing: ~

    - id: shape-015
      type: pass
      what: "Child-witness sub-arc — local arc (IDs 252–327)"
      why: >
        Rise via Clem's persistent noticing (IDs 256–280), inflection at IDs 311–316 (Taylor holds mouth,
        closes it, Clem stills — the slip and its arrest). Fall via mother intervention and draw (IDs
        322–327). End state differs: Taylor carries an unmanageable variable. Local arc passes.
      routing: ~

    - id: shape-016
      type: pass
      what: "Census-paperwork sub-arc — local arc (IDs 329–417)"
      why: >
        Rise via retinue arrival and dock pressure (IDs 329–370), first inflection at IDs 365–370 (Pryor
        pauses stylus, Rymer faces Taylor — dual surveillance committed). Second inflection at IDs 399–411
        (literacy folio handoff — non-reactive paperwork pull closes a management option). Fall via
        Pryor mounting and departing (IDs 414–417). Local arc passes. Rymer filing Taylor watching (ID
        370, 394) honored per plan commitment.
      routing: ~
```

---

## Summary

**Verdict: RE-ORDER-OR-REVISE.**

**Three structural ID ranges:**
- Season buildup: 1–418
- Season climax: 419–519 (peak: 455–474)
- Season denouement: 800–912

The season-wide escalation arc has its spine. The climax beat (IGNITION) is structurally intact — involuntary swarm, non-reversible consequence, Pryor documenting. The denouement (maester visit through ferry-folio close) is structurally present. The buildup sub-arcs (sept access, child-witness slip, census) each carry their inflections cleanly.

**Five faults route to fixer:**

1. **fault-003** (most urgent): Missing child-body cost-onset beats at IDs 490 and 519. The plan committed these explicitly; both are blank in the aggregate. Surrounding bones (IDs 504–505) carry generic physical-affect (jaw clench, exhale) but not the discrete cost-onset signal. The child-body cost mechanic that makes the involuntary swarm morally legible is not on the page.

2. **fault-004**: The Elara-interlude close at ID 787 cannot carry Taylor's present-tense decision. One positional line is insufficient. Beat must register her closed management options as a physical commitment.

3. **fault-001**: IDs 32–60 is a 29-line inert stretch — no escalation, no new information, no downstream-consequential action. Plan-required named change at early-baseline close not legible.

4. **fault-002**: IDs 654–699 missing post-IGNITION inflection in Taylor POV. 46 lines of transit between climax fall and Elara interlude.

5. **fault-005**: Missing maester age/physical-state notation in IDs 861–863. S2 body-clock plant absent.

**Routing:** all five faults to fixer for line-scope insertion. No screen-writer regen, no escalation. Three flags advisory (one for Phase 3 dialogue scope on plan-commitment named change, two for Mira/Elara rendering constraints).
