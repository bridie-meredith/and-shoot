audit:
  scope: episode
  target: chapter-03
  timestamp: 2026-05-07
  findings:
    - id: fault-001
      type: fault
      what: chapter-03.md line 60 — "the steward sets the scroll"
      why: "sets" is transitive; no landing surface named. An observer cannot confirm where the scroll was placed. Established format allows prepositions (ch01 line 25: "sets the broth pot on the table"). Missing object-destination leaves the physical action unanchored and underspecified.
      criteria: the proto-line must name the surface or location the scroll is set upon

    - id: fault-002
      type: fault
      what: chapter-03.md header — narrator: taylor-hebert-westeros; lines 1–79 (plumms-man scroll completion, delivery, records clerk intake, ser-harwick-plumm interception attempt, oc-castellan-harrenhal review)
      why: The chapter declares Taylor as narrator, but lines 1–79 are scenes she cannot observe — no fauna-mediation beats appear in this range, and the chapter-03 goal explicitly states she has not yet been told. A Taylor narrator who witnesses these scenes contradicts the goal; a Taylor narrator who does not witness them cannot narrate them. The narrator field and the goal are structurally incompatible as written.
      criteria: either the narrator field must be corrected to reflect an observational stance compatible with the goal, or fauna-mediation beats must be introduced that explain Taylor's partial access while preserving her ignorance of the report's content and destination

    - id: fault-003
      type: flag
      what: chapter-03.md line count — 98 content proto-lines vs. expected_lines: 95 in chapter-03-plan.md
      why: 3 lines over plan. Not a hard-limit violation but the excess may indicate compound beats that should be split or collapsed. Editor advisory.
