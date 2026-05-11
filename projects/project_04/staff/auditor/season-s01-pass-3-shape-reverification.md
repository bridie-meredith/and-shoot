```yaml
audit:
  scope: season
  target: s01
  pass: 3-shape-reverification
  timestamp: 2026-05-09
  verdict: CLEAN
  prior-audit: season-s01-pass-3-shape.md
  inserts-reviewed: [916, 917, 918, 919, 920, 921]

findings:

  - insert: 916
    fault-resolved: shape-001
    position: insert-at-48 (inside inert stretch IDs 32–60)
    verdict: PASS — THIN
    note: >
      Beat lands inside the inert block, recurs the insect-ecology signal established
      at IDs 11–13. Prior criteria accepted a single insect-ecology inflection beat as
      satisfying. The beat is environmental texture, not stakes escalation or new
      information. It passes the minimum stated criterion and is legible given the
      prior ecology-as-signal framing, but carries no independent structural load —
      it functions as a recurrence marker, not an inflection. If Phase 3 dialogue does
      not give the 32–60 block a named change per shape-006, this insert remains the
      sole structural anchor for a 29-line stretch. Advisory: shape-006 escalation
      path to fixer remains open if Phase 3 fails to anchor the named change.

  - insert: 917
    fault-resolved: shape-003 (cost onset)
    position: insert-at-490
    verdict: PASS
    note: >
      "taylor-hebert-jaehaerys presses the temple" at gap-490 is unambiguous
      cost-onset signal. Distinguishable from the generic physical-affect beats at
      IDs 504–505 (jaw clench, exhale). Slots into blank gap line — no action beats
      displaced.

  - insert: 918
    fault-resolved: shape-003 (cost sustain)
    position: insert-at-519
    verdict: PASS
    note: >
      "taylor-hebert-jaehaerys cradles the head" at gap-519 is cost-sustain.
      With 917, the pair delivers onset and persistence, landing the child-body cost
      mechanic as the plan required. Slots into blank gap line — no action beats
      displaced. No affect-overemphasis: neither beat displaces an action beat;
      both occupy vacant positions.

  - insert: 919
    fault-resolved: shape-002
    position: insert-at-690
    verdict: PASS — THIN
    note: >
      "taylor-hebert-jaehaerys releases the page" at position 690 is behaviorally
      distinguishable from pre-IGNITION ledger engagement beats (traces, presses,
      opens). The withdrawal register signals changed state. In a bones-only file,
      the post-IGNITION awareness reading depends on the reader having the prior
      engagement pattern; interiority is not available. Beat passes the structural
      criterion but relies on context for full weight. Adequate at bone level.

  - insert: 920
    fault-resolved: shape-004
    position: insert-at-787
    verdict: PASS
    note: >
      "taylor-hebert-jaehaerys grips the chair edge" alongside existing ID 787
      (faces the table) delivers the decisional physical register the fault required.
      Grip reads as held position under pressure — Taylor bracing rather than yielding.
      The Elara-interlude close now has two beats: positional (faces table) and
      decisional (grips edge). The present-tense decision is legible at bone level.

  - insert: 921
    fault-resolved: shape-005
    position: insert-at-862
    verdict: PASS
    note: >
      "the maester marks the ledger entry" slots between maester-holds-eyes (861)
      and maester-speaks-to-craftsman-father (862), after the direct Taylor exchange
      (855–861). Post-assessment placement satisfies the criteria. The S2 body-clock
      plant is on the page as a discrete recording action. The beat is correctly
      positioned after Taylor's assessment.

structural-checks:
  new-flatlines: none
  action-beats-displaced: none
  affect-overemphasis: no — both cost beats (917/918) occupy previously blank gaps
  advisory-flags-006-007-008: unchanged; still Phase 3 / editor scope
  shape-006-escalation-path: >
    Remains open. Shape-001 minimum satisfied by ID 916, but the plan's named
    "one concrete social or physical fact changed at early-baseline close" is not
    legible in the bones. Phase 3 dialogue must anchor it via ID 149 ledger-mark
    content or adjacent exchange. If not, shape-006 escalates to fault at Phase 3
    audit.

routing: Pass 4 (audience trim) may dispatch.
```
