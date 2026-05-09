audit:
  scope: episode
  target: s01e01
  timestamp: 2026-05-07
  verdict: CONTINUITY-FAIL
  findings:
    - id: fault-001
      type: fault
      what: line 58 — "taylor-hebert-westeros holds the ledger"
      why: >
        The ledger's state chain is: clerk carries (11) → clerk opens (18) → clerk enters (20, 45, 46).
        Taylor never receives the ledger; the clerk holds it at all times and it exits sealed in the
        clerk's case (episode-plan bullet 24). "Holds the ledger" therefore reads as FAULT-STATE-PROP-DANGLING
        (Taylor in possession of a prop she does not carry). Additionally, the hold-verb idiom throughout
        this file uses body parts ("holds the feet," "holds the eyes") or collectives/abstracts ("the wards
        hold," "the yard holds," "the sept doors hold") to express stillness or fixation — not named props.
        "Holds the ledger" breaks both the state chain and the established idiom pattern; it risks being
        parsed as physical grasping, which is a physical impossibility at this beat.
      criteria: >
        Line 58 must express Taylor's fixation on the ledger entry without implying physical possession.
        The replacement must be consistent with the hold-verb idiom (body part or abstract collective as
        object) or use a different construction that names the ledger as a perceptual anchor, not a held
        prop. Taylor must not be the grammatical agent of any action that requires the ledger to be in
        her hands.
    - id: fault-002
      type: pass
      what: reachability — chunk-end, goal, actor arcs
      why: All five cast members have coherent presence-arcs. Chunk-end state (Taylor named, flagged,
        provisional list, window closed) is fully reachable from chunk-start through the surviving
        beat sequence. Goal as stated is delivered.
    - id: fault-003
      type: pass
      what: state sweep — letter prop chain, ledger prop chain (excluding line 58), actor locations
      why: Letter chain is clean (produced 27, taken 28, returned 31, held 55). Actor locations are
        consistent; no actor appears in two locations simultaneously; all entries and exits are
        sequenced correctly.
    - id: fault-004
      type: pass
      what: reference sweep — all slugs
      why: All five cast slugs resolve to active actors. All prop and location references resolve
        to established elements in the location card or introduced earlier in the file. No
        unresolved slugs.
    - id: fault-005
      type: pass
      what: POV sweep — narrator consistency, perception-leak
      why: Narrator is taylor-hebert-westeros. No perception verbs survive on Taylor as grammatical
        subject. All scenes are witnessable by the POV character. No POV-leak faults found.
