```yaml
audit:
  scope: episode
  target: chapter-06
  timestamp: 2026-05-07
  findings:
    - id: fault-001
      type: fault
      what: line 62 — "taylor-hebert-westeros holds the position"
      why: abstraction-as-object hold; "the position" is not a physical object Taylor can hold — this is a state-maintenance abstraction, not a physical action; FAULT-FORM-NON-ACTION-VERB; writer self-reported
      criteria: line must name a physical action Taylor performs at this beat (e.g., a bodily stance, a muscular hold, a sensory re-anchor) — not an abstract state she maintains

    - id: fault-002
      type: fault
      what: line 84 — "taylor-hebert-westeros holds the network"
      why: abstraction-as-object hold; "the network" is a fauna-control abstraction, not a physical object; FAULT-FORM-NON-ACTION-VERB; writer self-reported
      criteria: line must name a physical or fauna-facing action (e.g., a specific group she keeps on a specific track, a physical cost she absorbs) — not a generic abstract-object hold

    - id: fault-003
      type: fault
      what: line 87 — "taylor-hebert-westeros holds the ravens on the track"
      why: abstraction-as-object hold; "holds the ravens on the track" names a maintained state, not a discrete physical action; FAULT-FORM-NON-ACTION-VERB; writer self-reported
      criteria: line must name the discrete action Taylor takes to keep the ravens in position — not a hold-state framing

    - id: fault-004
      type: fault
      what: line 91 — "taylor-hebert-westeros holds the second group"
      why: abstraction-as-object hold matching the pattern of fault-001 through fault-003; "holds the second group" is state-maintenance abstraction, not a physical action; FAULT-FORM-NON-ACTION-VERB; NOT self-reported by writer
      criteria: line must name a discrete physical or fauna-facing action Taylor performs on the second group at this beat — not a hold-state abstraction
```
