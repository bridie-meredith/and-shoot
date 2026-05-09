```yaml
audit:
  scope: series
  target: taylor-hebert-westeros
  timestamp: 2026-05-03
  findings:

    - id: fault-001
      type: fault
      what: season-s01-plan.md, Episode Chunk s01e04 body text
      why: >
        The s01e04 chunk body describes the septon's death and Plumm's move to formalize
        Taylor's status as a ward, with Taylor as a passive subject of the succession
        mechanism closing around her. The planning note appended to the same chunk states
        explicitly: "Taylor must make an active attempt to intervene in or delay the
        succession mechanism before it closes — the episode cannot be passive witness."
        The chunk body and its own planning note are in direct tension. The planning note
        correctly identifies the dramaturgical requirement (an active escalation attempt
        that fails or costs her), but the chunk text does not include this attempt. If
        episode planning proceeds from the chunk as written, the shoot will produce a
        passive-witness episode that violates the pulp-enthusiast escalation condition
        (cond-series-tone-constraints: escalation-ratchet rule; every scene ends at higher
        tension than it started, driven by action not process). A ward being administratively
        processed with no active resistance produces no escalation event within the episode
        and flattens the season's complication distribution.
      criteria: >
        The s01e04 chunk body must include a specific active attempt by Taylor to intervene
        in, delay, or redirect the succession mechanism before it closes. The attempt must
        be present in the chunk text itself, not only in the planning note. The attempt may
        fail — the chunk end-state (Taylor placed under Plumm's remit) can stand — but the
        failure must result from Taylor's action being overcome, not from Taylor's absence
        of action.

    - id: fault-002
      type: flag
      what: series-plan.md Season 2 chunk; season-s01-plan.md s01e06 end-state
      why: >
        The s01e06 end-state names Taylor "ward of the castellan's administration, assigned
        to Plumm's operational remit." The Season 2 series chunk says Taylor is "positioned
        inside a minor Riverlord's household." These are compatible only if Plumm is
        understood to be a minor riverlord operating his own household (distinct from the
        castellan's administrative seat), or if the S2 transition involves a transfer from
        the castellan's household to Plumm's separate household as a riverlord. Neither
        Plumm's status nor the transition mechanism is specified in either plan. If Plumm is
        the castellan's man rather than an independent riverlord, the S1 end-state places
        Taylor inside the castellan's structure at Harrenhal, not inside a minor riverlord's
        household, and the S2 starting position described in the series plan does not follow
        from the S1 end-state without a transfer event that is currently unplanned. This is
        not a blocker for S1 episode planning but must be resolved before S2 episode planning
        begins, or the S2 starting condition will be misread.
      criteria: null

    - id: fault-003
      type: pass
      what: Constraints — Taylor hard fences (explaining knowledge, parahuman infrastructure access, return to Earth-Bet)
      why: >
        No episode chunk in season-s01-plan.md calls for Taylor to explain her foreknowledge,
        access parahuman infrastructure, or seek return to Earth-Bet. All six chunks are
        external administrative/procedural collisions. The hard fences in taylor-hebert-westeros
        card.md (Hard Fences section) are not implicated by any chunk.
      criteria: null

    - id: fault-004
      type: pass
      what: Tone constraints — cond-series-tone-constraints vs. season-s01-plan.md episode chunks
      why: >
        All six episode chunks are written as external structural collisions with no
        interiority statements and no character psychology. No chunk contains extended
        introspection, chess-match scheming as a scene function, or lore-dump framing.
        The chunks are appropriately brief structural descriptions of external events. The
        series tone constraint (fast, pulpy, dramatic; no introspection-dominant register)
        is not violated at the plan level.
      criteria: null

    - id: fault-005
      type: pass
      what: Fauna control cost curve — cond-fauna-control-rules vs. season-s01-plan.md
      why: >
        No episode chunk specifies sustained fauna-control use that would violate the cost
        curve. The chunks reference fauna anomalies as observed consequences (grain store
        rat-cleared, ravens roosting against pattern, raven perched on Taylor's arm) rather
        than mandating extended continuous-use sessions. The cost curve is not pre-violated
        at the plan level. Episode-level planning and shoot will need to respect the 0-5/5-15/
        15-30/30+ minute cost structure when operationalizing these events.
      criteria: null

    - id: fault-006
      type: pass
      what: Series escalation spine consistency — series-plan.md vs. season-s01-plan.md
      why: >
        The series spine labels Anonymity as the S1 loss. The season ends with Taylor named,
        placed, and assigned a function she did not choose — Anonymity is lost. The season
        spine (Named → Pattern documented → Witnessed anomaly → Cover removed → Competed
        over → Resolved) is an episode-granularity operational description of how Anonymity
        is lost, not a contradiction of the macro-spine. The two spines are complementary at
        different levels of resolution.
      criteria: null

    - id: fault-007
      type: pass
      what: Pulp-enthusiast condition — complication distribution across s01 episodes
      why: >
        Complications are distributed: E01 (name enters census ledger), E02 (first written
        report, anomaly pattern established), E03 (concrete witnessed anomaly, Rowan's
        intercession broadens exposure), E04 (septon dies, succession mechanism triggered),
        E05 (maester assessment flags her, Bracken counter-claim filed, Celtigar letter
        arrives), E06 (administrative resolution closes the window). No concentration at
        finale. The S1 pulp-enthusiast condition from series-plan.md Forward Flags is met.
      criteria: null

    - id: fault-008
      type: pass
      what: Drama sizing — all six episode chunks
      why: >
        All six chunks are sized at structural collision level. E01: the administrative
        machine acquires Taylor's name and places her on a provisional list — genuine
        pressure event, not a minor incident. E02-E06 escalate the board in increments that
        are each load-bearing. No chunk is a minor incident dressed as an episode.
      criteria: null

    - id: fault-009
      type: pass
      what: Forward flags consistency — season-s01-plan.md Forward Flags section vs. chunk planning notes
      why: >
        The E4 planning note in the chunk body and its Forward Flags entry are consistent
        in content. The E5 planning note and its Forward Flags entry are consistent. The E3
        raven scene note (inspector reaction: discomfort not curiosity) and the E5 maester
        note (detached documentation, not recognition) are both present in Forward Flags and
        appropriately operational. No forward flag contradicts or drifts from its source
        chunk note.
      criteria: null

    - id: fault-010
      type: pass
      what: Series question — answerability by planned arc
      why: >
        The series question ("Can someone who already paid the full price once build enough
        from nothing to matter when the second catastrophe arrives — and should they?") is
        not foreclosed by the four-season plan. The arc brings Taylor to a position of
        maximum leverage (her network is the only coherent intelligence picture in the
        Dance theater) precisely when she loses the ability to use it neutrally — which is
        the structural condition that makes the question answerable rather than merely posed.
        The open S4 landing (survival-at-cost / transformation / destruction) correctly
        defers the specific answer to S4 planning without foreclosing any of the three
        options.
      criteria: null

    - id: fault-011
      type: flag
      what: series-plan.md S4 end-state open flag
      why: >
        The series plan itself notes: "S4 end-state is open: season 4 episode planning must
        commit to a specific landing — not a blocker now, required for S4 planning." This is
        correctly self-identified and correctly deferred. Noted here for completeness and
        tracking continuity. This flag must be resolved before S4 season planning begins.
      criteria: null

    - id: fault-012
      type: pass
      what: Reincarnation mechanics — no return implied in any chunk
      why: >
        No chunk implies a return path to Earth-Bet, another displaced soul, or any
        violation of cond-reincarnation-mechanics. The no-return rule and uniqueness
        constraint are not implicated at the plan level.
      criteria: null

    - id: fault-013
      type: pass
      what: No parahuman infrastructure — cond-no-parahuman-infrastructure vs. all plans
      why: >
        No chunk implies Shard contact, trigger events, second capes, or parahuman
        institutional apparatus. The prohibition is fully respected at the plan level.
      criteria: null
```
