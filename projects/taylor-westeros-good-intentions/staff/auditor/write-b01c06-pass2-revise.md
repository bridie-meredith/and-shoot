audit:
  scope: scene
  target: b01c06s03 (flat_ids 16–21, six recast bones only)
  timestamp: 2026-05-31
  pass: 2-revise
  context: depth-pass de-abstraction revise; six bones recast from apparatus/bookkeeping-metaphor SVOs to concrete physical record-object SVOs; bones outside this set are out of scope
  findings:

    - id: fault-001
      type: fault
      what: >
        theater/bones/b01-c06.md flat_ids 16–21 still carry the OLD (pre-recast) SVOs:
          16: "taylor-hebert-kl-122ac opens the accounting ledger"
          17: "taylor-hebert-kl-122ac writes the first arm — names against Sera's protection"
          18: "taylor-hebert-kl-122ac writes the second arm — omission risk against Sera's exposure"
          19: "taylor-hebert-kl-122ac marks the red-keep coverage record"
          20: "taylor-hebert-kl-122ac closes the accounting entry"
          21: "taylor-hebert-kl-122ac squares the jarvis-channel form"
        The six recast SVOs (from showrunner memory and the task brief) are NOT present in the
        flat bones file. Showrunner memory is the source of truth, but the bones file is the
        flattened serialization that /and-facets and /and-stitch consume. A mismatch between
        memory and bones file is a state consistency fault.
      why: >
        /and-facets and /and-stitch read theater/bones/b01-c06.md, not showrunner memory.
        If the bones file is not updated, the downstream pipeline operates on the old
        apparatus-abstraction SVOs that the cold-read flagged as airless. The depth-pass
        revise produces no improvement at stitch unless the bones file is synced.
      criteria: >
        theater/bones/b01-c06.md flat_ids 16–21 must reflect the six recast SVOs exactly
        as they appear in showrunner memory (b01c06s03n01/n02/n03/n04/n05/n10):
          16: "taylor-hebert-kl-122ac opens the ledger-board"
          17: "taylor-hebert-kl-122ac writes the ward-elder names"
          18: "taylor-hebert-kl-122ac writes the sera-coverage entry"
          19: "taylor-hebert-kl-122ac marks the red-keep coverage record"
          20: "taylor-hebert-kl-122ac closes the ledger-board"
          21: "taylor-hebert-kl-122ac lifts the jarvis-channel form"
        No other lines in the bones file may change. Flat_ids must remain 16–21 (no renumbering).

    - id: pass-001
      type: pass
      what: >
        PP-modifier check (FAULT-FORM-MODIFIER) — all six recast SVOs.
        SVOs examined:
          "opens the ledger-board" — S V O; no PP tail.
          "writes the ward-elder names" — S V O; no PP tail.
          "writes the sera-coverage entry" — S V O; no PP tail.
          "marks the red-keep coverage record" — S V O; no PP tail.
          "closes the ledger-board" — S V O; no PP tail.
          "lifts the jarvis-channel form" — S V O; no PP tail.
        None carries an "at X / in X / with X / from X / into X / toward X" prepositional
        padding tail. The DEC-0053 failure mode (PP-contaminated "stays at the sept-corner")
        does not recur here.
      why: null

    - id: pass-002
      type: pass
      what: >
        Verb class check — all six recast SVOs.
        opens: transitive physical action; not copula, not negation, not perception, not stative. Clean.
        writes (x2): transitive physical action (inscription on surface); not on the schema's
          perception-verb deny-list (read/took/tracked/noted/counted/measured/watches/sees/
          hears/notices). Clean.
        marks: transitive physical action (annotation on record); same deny-list: absent. Clean.
        closes: transitive physical action. Clean.
        lifts: transitive with direct object "the jarvis-channel form"; not a bare intransitive
          motion verb; "lifts" is a force-application verb picking up a physical prop. The bare-
          intransitive-motion rule (FAULT-FORM-NO-VERB) requires destination when the verb is
          directional (e.g., "moves"); "lifts" is not in that class — it takes the lifted object
          as its direct object. Clean.
        No copulas, negations, conjunctions, adjectives, adverbs, or interiority terms present
        in any of the six SVOs.
      why: null

    - id: pass-003
      type: pass
      what: >
        Abstraction-as-direct-object check (FAULT-FORM-INTERIORITY) — all six recast SVOs.
        Objects examined:
          "the ledger-board": compound-noun physical record substrate; follows the
            chapter's established compound-noun prop convention (cf. "coverage-notes entry"
            at flat 6/9, "jarvis-channel form" at flat 14/15/22/23). Not an affective/
            cognitive abstraction. Clean.
          "the ward-elder names": "names" as a direct object of "writes" = the specific
            identifiers being inscribed on a physical record. This is content-as-data
            (four person-identifiers), not an affective state. The prohibited class is
            affective/cognitive ("carries the weight", "holds the silence", "the yard holds
            the tension"). "Writes the ward-elder names" = physical inscription of enumerated
            data. Analogous to established passing forms in this chapter: "fills the
            jarvis-channel form" (flat 14), "marks the contact-role field" (flat 7). Clean.
          "the sera-coverage entry": compound-noun record-object. "Coverage entry" is an
            established record-type in this chapter (compare "coverage-notes entry" at
            flat 6/9, "coverage-memory record" at flat 13, "red-keep coverage record" at
            flat 19). "Sera" is the protect-target (established from c03); used here as
            a record-type modifier, not as an unresolved entity reference. "Sera-coverage
            entry" = the entry in the accounting ledger-board recording Sera's exposure
            status. Physical record-object following the chapter's compound-noun convention.
            Clean. (See also pass-006 for entity-reference check.)
          "the red-keep coverage record": unchanged from prior emit; established compound-noun
            record-object. Clean.
          "the ledger-board" (flat 20): same analysis as flat 16. Clean.
          "the jarvis-channel form" (flat 21): established physical prop throughout c06
            (flats 14, 15, 22, 23 all use this slug). Clean.
      why: null

    - id: pass-004
      type: pass
      what: >
        Earth-Bet proper-noun fence check (cond-earth-bet-noun-fence) — all six recast SVOs.
        Objects scanned:
          "ledger-board": Westerosi-register accounting substrate. Not a parahuman term.
          "ward-elder names": ward elder = Westerosi social role. Not a parahuman term.
          "sera-coverage entry": Sera = Sera Hightower, Westerosi character. "Coverage" =
            Taylor's operational vocabulary for her insect-network, which per the fence card
            uses functional descriptions ("what the bugs show me," "reading the ward"), not
            Earth-Bet proper nouns. "Coverage" is a generic operational term, not Worm-canon
            jargon. Clean.
          "red-keep coverage record": Red Keep = Westerosi location. Not a parahuman term.
          "jarvis-channel form": Jarvis = Jarvis Coin, established Westerosi courier slug.
            "Channel" = operational relay term (not a PRT/Protectorate/Cauldron term).
        All six SVOs: Earth-Bet fence CLEAN. No Worm-canon proper nouns, parahuman
        classifications, or institutional terms present.
      why: null

    - id: pass-005
      type: pass
      what: >
        Bone delta structural check — all six recast bones.
        All six: shape=held, axis_moves=[], cost_ledger_anchor=null, dialogue_anchor=false.
        Held axes: moral_framework (flats 16, 17, 18, 20, 21), relational_anchor_status
        (flat 17), political_register-prot (flat 18), capability + relational_anchor_status
        (flat 19). All named axes confirmed present in series.substance.state_axes (memory
        verified: moral_framework, relational_anchor_status, political_register-prot,
        capability all listed). All six held-axis entries carry rationale text. No missing
        fields; no malformed cost_ledger_anchor entries; no dialogue_anchor mismatch (none
        of the six bones is a speech-form bone and none is in axis_moves with a
        communication-class axis). No FAULT-BONE-DELTA-MALFORMED.
      why: null

    - id: pass-006
      type: pass
      what: >
        Entity-reference / physical resolution check on "sera-coverage entry" (flat 18, new
        compound-noun object).
        "Sera" resolves to sera-hightower-kl-122ac, the established protect-target. The
        character is named and architected from c03 onward; Sera appears in the c06 chapter
        chunk explicitly ("one name she has never met whose continued standing in Alicent's
        household is the reason the arrangement exists"). The "sera-coverage entry" is the
        record entry in the accounting ledger-board documenting Sera's exposure — it is a
        record-object, not a direct reference to Sera as an on-stage actor in this scene.
        Sera is not required to be physically present on the scene's set for this bone to
        be valid; she is the named referent of the record-content, not a participant.
        The object is a record-type compound noun following the same convention as
        "red-keep coverage record" (flat 19, unchanged): both are record-entries whose
        names derive from their subject-matter. No unresolved entity reference.
        No FAULT-REFERENCE.
      why: null

    - id: pass-007
      type: pass
      what: >
        Multi-subject, conjunction, copula, negation, compound-object check — all six SVOs.
        All six are single-subject (taylor-hebert-kl-122ac). No "and/but/while/as"
        conjunctions. No copula forms (is/was/were/be/been/being). No negations. No
        compound comma-list objects. Each SVO is one subject, one verb, one object. Clean.
      why: null

  summary: >
    ONE FAULT (fault-001). The six recast SVO forms are schema-clean: zero PP-modifier
    violations, zero abstraction-as-object violations, zero Earth-Bet fence violations,
    zero verb-class violations, zero delta-malformation findings. The recast successfully
    removes the prior apparatus-abstraction objects ("the first arm", "the second arm",
    "the accounting entry", "squares") and replaces them with concrete physical
    record-object SVOs following the chapter's compound-noun convention. The sole fault
    is a bones-file sync gap: the flat bones file at theater/bones/b01-c06.md still
    carries the pre-recast SVOs. Pass-2 does not terminate clean until fault-001 is
    resolved by updating the bones file to match showrunner memory.
