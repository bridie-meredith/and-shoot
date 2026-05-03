audit:
  scope: series
  target: taylor-in-westeros — series plan + season 1 plan
  timestamp: 2026-05-03
  findings:
    - id: flag-001
      type: flag
      what: active-project/actors/westerosi-traveling-maester/card.md — thematic purpose section gap
      why: The project card does not override the source card's thematic purpose section, which references "Tanya" and chain-2 scenario elements from a prior project. This will be visible to the impersonator if they load the source card's thematic purpose. Not a constraint violation; an advisory risk.
      criteria: N/A — advisory only. Recommend adding a line to the project card explicitly instructing the impersonator to use voice, action menu, and hard fences sections only; disregard thematic purpose from source card.

    - id: flag-002
      type: flag
      what: season-s01-plan.md — hatchling scale unspecified
      why: S01E01 will need to establish Taylor's physical scale and capabilities as a hatchling (~110 AC, newly hatched). This is not in any existing document. The episode plan step should address it before shoot. Not a plan quality fault; a pre-shoot advisory.
      criteria: N/A — advisory only. Address in episode-plan authoring for S01E01.

    - id: check-all-constraints
      type: pass
      what: all constraint card interactions, series and season plan
      why: No verbal communication required in S1 chunks; no power extension beyond arthropods; patch-protection drive consistent across all 10 episode chunks; escalation-default consistent; genre register (fast/pulpy/action) consistent with 10-episode structure and each chunk's dramatic collision.

    - id: check-plan-quality
      type: pass
      what: series plan + season 1 plan acceptance records
      why: Both plans accepted at attempt 1 by all three audience personas and dramatist. No exhaustion. No outstanding revise flags.

    - id: check-state
      type: pass
      what: studio state, actor states at series open
      why: No show file exists yet; no state violations possible. Actor state files are populated with correct entry states.

    - id: check-structural
      type: pass
      what: delivery chain S01E01 through S01E10
      why: Each episode chunk delivers to the next; S1 end ≠ start; series end ≠ start; series question is answerable by S5 events.
