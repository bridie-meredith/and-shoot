audit:
  scope: episode
  target: chapter-05
  timestamp: 2026-05-07
  findings:

    - id: fault-001
      type: fault
      what: chapter-05.md line 53 — "the postern gate closes"
      why: Subject is an inanimate environmental object, not a cast actor. FAULT-FORM-NON-ACTION-VERB class: non-actor subject executing the verb. No cast member drives this action.
      criteria: line must use a cast actor as subject, or be recast so a cast actor's action causes or constitutes the gate closing

    - id: fault-002
      type: fault
      what: chapter-05.md line 67 — "the ravens lift from the bell tower"
      why: Subject is fauna, not a named cast actor. Fauna appear as autonomous subjects without an actor driving them. FAULT-FORM-NON-ACTION-VERB class. Also a narrator-POV leak: septon-rowan is narrator and cannot interiority-attribute raven behavior without establishing observation.
      criteria: line must use a cast actor as subject, or be recast so the acting entity is an on-cast actor (e.g., septon-rowan observes, hears, or registers the ravens)

    - id: fault-003
      type: fault
      what: chapter-05.md lines 16, 24, 29, 54, 57 — blank numbered positions
      why: Five bullet slots carry no content. The file format uses numbered lines as deliverable action units; blank slots are undelivered bullets, not scene-break notation. The chapter delivers ~62 active lines against an expected_lines of 100 — material underdelivery that leaves the chapter structurally incomplete.
      criteria: blank positions must be filled with valid action-verb bullets, or the chapter must be renumbered with explicit scene-break notation if blank lines are intentional structural markers; total active lines must approach the expected_lines target of 100

    - id: fault-004
      type: fault
      what: constraint cards cond-westerosi-customary-authority, cond-riverlands-120ac-state, cond-series-tone-constraints — files not found at cards/conditions/
      why: Three of three plan-listed constraints are unavailable for audit. Constraint axis cannot be completed. Any violations against those conditions in chapter-05.md are undetectable until the cards are located or recreated.
      criteria: constraint card files must be locatable at their canonical library paths so constraint-axis audit can be completed; this audit pass is incomplete on the constraint axis until that is resolved
