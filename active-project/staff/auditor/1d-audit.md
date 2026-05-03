audit:
  scope: series
  target: taylor-hebert-westeros
  timestamp: 2026-05-03
  step: 1d constraint-consistency audit
  findings:
    - id: pass-001
      type: pass
      what: all 7 condition cards (cond-fauna-control-rules, cond-impressment-census-120ac, cond-riverlands-120ac-state, cond-westerosi-customary-authority, cond-dance-of-dragons-foreknowledge, cond-recovery-timeline, cond-cats-ruling)
      why: auditor initially could not locate condition cards on disk — technical failure, not real faults. All 7 cards subsequently confirmed present and passing consistency checks.
    - id: pass-002
      type: pass
      what: internal card consistency across all 7 condition cards
      why: cross-references, scope fields, and constraint language checked; no internal contradictions found.
    - id: pass-003
      type: pass
      what: world-notes fidelity check against condition cards
      why: condition card constraints align with world-notes laws and lore; no contradictions.
    - id: pass-004
      type: pass
      what: recovery timeline and cats ruling canonized in condition card
      why: both adjudicated items are recorded in condition card scope; no floating rulings remain unanchored.
    - id: flag-002
      type: flag
      what: active-project/actors/taylor-hebert/card.md — Relationships > Active (Westeros) > oc-castellan-harrenhal entry
      why: Hightower affiliation of the castellan is established in world-notes (OQ-3/OQ-5 RESOLVED) but not named in Taylor's relationships section; gap between card and world-notes creates impersonator blind spot when the castellan's authority chain becomes plot-relevant.
      criteria: Taylor's card must name the Hightower affiliation in the castellan entry and note what it implies for the succession calculus she is tracking.
    - id: flag-003
      type: flag
      what: active-project/staff/showrunner/world-notes.md — SOURCE section
      why: Taylor's Earth-Bet reading of ASOIAF/Fire & Blood is implied by her hard fence ("She does not know Westerosi high-nobility relationships at the personal level... historical knowledge is not personal knowledge") but no world-notes law explicitly defines the scope and limits of that knowledge; the fence can be misread or under-enforced without a governing law.
      criteria: world-notes SOURCE section must contain a law defining that ASOIAF/Fire & Blood exists as published fiction on Earth-Bet, the extent of Taylor's reading, and the hard distinction between historical-fictional knowledge and actual-personal knowledge.
