audit:
  scope: series
  target: taylor-in-westeros — 1d constraint card set
  timestamp: 2026-05-03
  findings:
    - id: fault-001
      type: flag
      what: cards/personas/westerosi-traveling-maester.card.md — Thematic Purpose section
      why: Section references "Tanya" and "chain-2 collision" from a prior project (dead-capes-in-westeros or similar); this content is not stripped and would be misleading if the full card is loaded by an impersonator without awareness. Does not create a constraint violation; the card's mechanical sections (voice, action menu, hard fences) are fully applicable to this project.
      criteria: N/A — flag only; editor or impersonator should note that the Thematic Purpose section is from a prior project and the project card at active-project/actors/westerosi-traveling-maester/card.md does not override it. Advisory: the impersonator for this actor should be briefed to use the action menu and voice sections, not the thematic purpose.

    - id: fault-002
      type: flag
      what: world-notes.md — series season count
      why: The 19-year runway (~110-129 AC) implies a series of 4-5 seasons. The series plan step should ensure the season chunk structure respects this timeline and does not casually extend past ~131 AC without narrative justification.
      criteria: N/A — flag only; advisory for series planning step.

    - id: check-all-others
      type: pass
      what: all other constraint cards and inter-card interactions
      why: Shard persistence logic internally consistent; dragon body + swarm mechanics consistent; fire/swarm conflict consistent with source card action costs; political condition cards non-contradictory; timeline dates all verified; series spine consistent with character behavior constraints; cast roster complete for S1.
