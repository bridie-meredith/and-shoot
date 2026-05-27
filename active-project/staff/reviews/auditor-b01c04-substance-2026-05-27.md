---
audit:
  scope: chapter
  target: b01c04
  timestamp: 2026-05-27
  trigger: /and-substance chapter b01c04 Phase 5 contract-fidelity review
  reviewer: auditor
  summary:
    verdict: FAIL
    hard_count: 2
    signal_count: 4
    note: >
      Two HARD findings. fault-001 is a pervasive POV fence violation — all three
      scene chunks are authored in third-person limited, not first-person, in direct
      violation of cond-taylor-pov-behavior (series-wide hard rule). This requires
      full redraft of all three chunks. fault-002 is a cost-ledger claim mismatch:
      s01 notes "cl-antag-d03 completed" while the chapter moves only +1.0 of a +4
      ledger entry — the completion claim is false and creates a downstream accounting
      error. Four signals are non-blocking but require attention before bones.
---

findings:

  - id: fault-001
    type: fault
    what: >
      All three scene chunks (b01c04s01, b01c04s02, b01c04s03) — every paragraph of
      narrated prose in the draft — are written in third-person limited: "Taylor is
      back in the cooper's yard," "Taylor walks it in the late morning," "She does not
      review the decision," "The third ward falls on the second day." The subject
      throughout is "Taylor" or "She," not "I."
    why: >
      cond-taylor-pov-behavior states: "This project is first-person Taylor POV
      throughout. Taylor's voice is 'I' — not close-third, not omniscient, not
      limited-third. Every chapter defaults to first-person Taylor. An unmarked
      non-Taylor POV chapter is a structural violation." b01c04 is not marked as
      an interlude. The POV rule is a hard series-wide authoring fence, not a
      stylistic preference. Third-person limited chunks cannot be used as the
      upstream source for bones-authoring without propagating the violation into
      the bones file and the stitch. The cold-read terminal gate at /and-stitch
      Phase 9 will surface this as a structural failure; catching it at Phase 5
      prevents wasted downstream work across /and-write, /and-facets, and
      /and-stitch.
    criteria: >
      All three scene chunks must be redrafted in first-person Taylor POV ("I").
      Every narrative sentence that currently uses "Taylor" or "She" as the
      grammatical subject of an action or perception must be rendered in the
      first-person register. The substance_delta, scene_conflict, and
      axis_aggregate_check blocks are not prose and are not in scope for this
      fix. The fix is the chunk prose bodies only.

  - id: fault-002
    type: fault
    what: >
      b01c04s01 substance_delta notes for social_tether-antag: "acceptance delivered
      and acknowledged; Otto's lever solidified from embryonic to operational;
      cl-antag-d03 completed; Taylor can no longer un-be-the-intelligence-source."
      The series cost_ledger entry for cl-antag-d03 reads: gain "social_tether-antag
      +4" / cost "journey-required: cl02 (offer accepted; Otto gains leverage
      proportional to Taylor's position-rise)." The chapter moves social_tether-antag
      +1.0 in s01 (confirmed by axis_aggregate_check: total chapter +1.0). The
      claim "cl-antag-d03 completed" asserts the full +4 gain entry is consumed.
      +1.0 ≠ +4. The ledger entry is not completed; it is partially consumed.
    why: >
      Mislabeling a ledger entry as "completed" when 75% of its gain allocation
      remains outstanding creates a false accounting baseline for every downstream
      chapter that draws on the social_tether-antag axis. /and-substance book Phase
      3 (per-chapter contract authoring) checks ledger anchor claims against the
      series ledger; a false "completed" at c04 will produce either a gap (no
      remaining anchor for the +3 still outstanding) or a duplicate anchor claim
      in a later chapter. The series aggregate for social_tether-antag is +8 (ranks
      1→9); cl-antag-d03 (+4) and cl-antag-d10 (+4) account for it. If c04 exhausts
      cl-antag-d03, the +3 outstanding gain has no ledger home. This is a
      CAUSE-MISSING + CONTRACT-DRIFT classification at the ledger layer.
    criteria: >
      The s01 substance_delta notes for social_tether-antag must be corrected to
      reflect that cl-antag-d03 is partially consumed — the c04 tranche (+1.0) is
      delivered, but the entry is NOT completed. The notes should identify this as
      a partial tranche (e.g., "cl-antag-d03 first tranche — +1.0 of +4 gain
      allocated here; remaining +3.0 to be distributed in subsequent chapters").
      No prose rewrite required; this is a substance_delta notes correction only.

  - id: flag-001
    type: flag
    what: >
      moral_framework held-rationale in s01, s02, and s03 each acknowledge that the
      crack in Taylor's moral framework "has widened" (s01: "the crack has widened
      but the framework is still named and believed"; s02: "the crack is present but
      the framework is still operative in this specific form"; s03: "the crack is
      present but the framework is still held"). The chapter contract entry
      (memory.md line 3061) also says "the crack has widened." A crack that has
      widened from chapter-start to chapter-close is sub-threshold axis movement,
      but movement. No scene's axes_in_motion posts any moral_framework delta.
    why: >
      This tracking gap is not a HARD at this phase because the chapter contract
      explicitly defers moral_framework interrogation to a later chapter
      ("rationalization is not yet complete"). However, the cl02 and cl03a cost-side
      allocations (moral_framework -3 and -2 respectively) must accrue somewhere in
      the book-level arc. If c04 has already begun accruing the cost (crack widened)
      without posting it to any chapter Δ, the book-level roll-up will either
      show an unanchored moral_framework decline or a later chapter will claim the
      full ledger cost on an axis that is already partially moved. /and-substance
      book Phase 0 will surface this as a potential SUBSTANCE-FLAT or accounting
      gap when it checks the roll-up. Recommend adding a note to the held-rationale
      clarifying whether the crack-widening is sub-threshold (does not register as
      measurable axis movement at chapter granularity) or is a deferred posting that
      will be accounted in a future chapter's axes_in_motion. No fixer dispatch —
      this is an advisory for the screen-writer at the next substance pass.

  - id: flag-002
    type: flag
    what: >
      b01c04s03 substance_delta notes for position-world: "cl-world-d04 delivered;
      this is the world-axis increment." The series cost_ledger entry for cl-world-d04
      reads: gain "position-world +2." The chapter moves position-world +1.0. The
      term "delivered" is ambiguous — it could mean "the delivery event occurred
      (first intelligence report handed to Jarvis)" or "the full +2 ledger entry is
      consumed." The handoff_out at memory.md line 3096 shows "position-world rank 6
      (first increment delivered)" — starting rank 5, +1.0 = 6; this implies only
      the first increment is delivered, not the full entry.
    why: >
      If "cl-world-d04 delivered" means "entry fully consumed," then the +2 gain
      is exhausted at c04 and no position-world gain is available from this entry
      for subsequent chapters. The series position-world arc is start 5, end 9 (+4
      total); cl-world-d04 (+2) and cl07b (+2) account for the full rise. If
      cl-world-d04 is fully consumed at c04, +1.0 of the +4 series total is
      unanchored. The handoff_out phrasing ("first increment") suggests the entry
      is only half-consumed, which is consistent with the math. The notes language
      should be clarified to "cl-world-d04 first tranche (+1.0 of +2 gain allocated
      here)" to prevent the same downstream confusion flagged in fault-002. No
      fixer dispatch — this is a substance_delta notes clarification, not a
      substance error, pending confirmation that the intent is partial consumption.

  - id: flag-003
    type: flag
    what: >
      The held-axis rationale for political_register-prot is substantively identical
      across all three scenes: s01 "no court-register content at courier-tier; terms
      delivered in plain register; resentment has no material"; s02 "ward-level
      coverage only; no court-tier observation material; resentment has no substrate";
      s03 "Taylor's feed is Flea Bottom-tier; the report is ward-pattern and
      crowd-agitation; no court-register observation material; resentment has no
      substrate at this feed-tier." Three scenes, one rationale restated with minor
      variation.
    why: >
      Boilerplate held-axis rationale is a SIGNAL under check 7 (held-axis-boilerplate).
      The rationale is not meaningless — it correctly identifies why political_register-prot
      does not move in c04 — but it does not differentiate what each scene specifically
      does or does not present that would otherwise advance the axis. If the chapter
      contained any court-tier content that Taylor actively chose not to register
      (which would be a distinct discipline), the boilerplate would obscure that.
      As written the three scenes genuinely have no court-tier observation material,
      so the rationale is accurate if repetitive. Advisory only; no fixer dispatch.

  - id: flag-004
    type: flag
    what: >
      b01c04s03 chunk prose (line 85 in draft): "[mechanism: the protection and the
      trap as the same operation, now materially running — not as a future contingency
      but as the present shape of her day]." This mechanism tag names the chapter's
      thematic thesis verbatim in the metadata layer of the chunk.
    why: >
      cond-taylor-pov-behavior Theme Silence rule states: "Taylor does not narrate
      theme. The road-to-hell irony is never voiced by Taylor, never approached as
      a concept by Taylor, never placed in Taylor's inner monologue as a
      generalization about her situation." The mechanism tag is a chunk-authoring
      annotation, not a delivered prose line, and does not itself violate the fence
      — the fence governs narrated prose, not planning metadata. However, if the
      bones-authoring agent at /and-write reads this mechanism tag as a direction
      to produce prose that explicitly states the thesis (rather than prose that
      dramatizes the structural condition the thesis names), it will produce a
      theme-silence violation. The tag's language ("the protection and the trap as
      the same operation") is the exact formulation of the chapter goal, which is
      appropriate as a planning anchor. The /and-write Phase 1 dispatch for this
      scene must be scoped to avoid surfacing this as narrated inner monologue.
      Advisory only; no fixer dispatch required at this phase.
