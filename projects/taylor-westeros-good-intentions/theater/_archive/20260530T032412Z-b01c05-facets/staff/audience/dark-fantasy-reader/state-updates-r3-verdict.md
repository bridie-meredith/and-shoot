---
reviewer: dark-fantasy-reader
facet: state-updates
chapter: b01-c04
phase: 5b-adversarial
cycle: 3
date: 2026-05-27
verdict: revise
---

# dark-fantasy-reader — state-updates adversarial review, b01-c04, cycle 3

## Reviewing stance

Same as cycle 1. The state-updates file is the world's memory. I'm checking whether the record was corrected cleanly, not whether it was corrected at all.

---

## The 5 mechanical fixes: assessment

The cycle-3 fixer session (SESSION-START 2026-05-27T02:00:00Z) applied 6 fixes to the state-updates slices. Five of those are the "mechanical corrections" in scope for this re-review; fix-6 is the compound-split add (state:30) which is separately load-bearing. I'm treating all 6.

**Fix 1 — state:6 anchor @26 → @25 (active_location lag correction).**
Accepted. The `studio.active_location: oc-pig-tallow-lane → oc-ropers-court` fire was on the actor-entry bone (@26: "taylor-hebert-kl-122ac enters Roper's Court") when it should be on the scene-open env-frame bone (@25: "the early-morning grey empties Roper's Court"). Loc-state:4 is already at @25. The env-frame and the location-state fire now co-anchor. That is correct: the location changes when the scene opens, not when the character steps in. The anchor-lag was real; the move is real. ACCEPT.

**Fix 2 — state:7 @27 descriptor-value → slug-list.**
Accepted. `four-ward-complete` was a stage-direction descriptor masquerading as a zone-set value. `oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane + oc-ropers-court` is the canonical form consistent with the coverage_active_range chain at entries 3 and 4. Field-extension comment preserved. This is a form correction that strengthens canonical integrity — downstream chapters reading this entry now get a zone-set they can compare against. ACCEPT.

**Fix 3 — state:9 @29 compound roster → incremental.**
Accepted. The old form `[] → [taylor, jarvis]` erased Taylor's prior yard-presence and wrote both actors as simultaneous fresh arrivals. The world was on record as empty before Jarvis entered when Taylor had been in that yard since @3. The corrected form `[taylor-hebert-kl-122ac] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier]` records the actual increment: Jarvis joins. The world's memory was wrong before; it is right now. ACCEPT.

**Fix 4 — state:14 @39 label → canonical slug.**
Accepted. `chapter-close-stitch-house-lane-exit` is a stage note, not a location. `oc-stitch-house-lane` is the canonical post-exit location — Taylor crosses out of the cooper's yard into stitch-house-lane territory. The world records where she is, not what the scene is called. ACCEPT.

**Fix 5 — state:16/22 Jarvis field-extensions declared.**
Accepted. The extensions `stats.active_deliveries` and `stats.exposure_risk` were used without being declared in the preamble. The preamble now carries the rubric-compliant annotation for both — tracked-state-aspects, irreversible flip, handoff_out propagation obligation. The entries themselves were always defensible; the documentation gap was the failure and it is closed. ACCEPT.

**Fix 6 — state:27 @22 compound → split (wren-in-coverage-map + wren-report-inclusion).**
Accepted. `present-but-outside-report` was two facts in one value: the registration fact (Wren is in the feed) and the decision fact (she will not appear in the report). These are separable canonical states with different anchors and different stakes. State:27 (@22) now carries the registration fact only: `absent → present`. State:30 (@31) carries the decision fact: `wren-report-inclusion: na → excluded`. The split is correct because the facts enact at different bones — the feed returns Wren at @22; the exclusion decision enacts at @31 when Taylor hands off the report without Wren's name in it. Both field-extensions are declared in the preamble. The compound encoding obscured which fact became canonical when. The split clarifies the record. ACCEPT.

---

## State:13 — the open finding

This was my sole finding from cycle 1. It was not in admin's cycle-3 scope.

The finding remains present. Reading the current consolidated file:

```
13 @37 studio.actors_in_yard: [taylor-hebert-kl-122ac] → []
```

Proto-line @37: `taylor-hebert-kl-122ac runs the ward-feed`
Proto-line @38: `the insect-feed returns wren-stitch-maker-flea-bottom-ward`
Proto-line @39: `taylor-hebert-kl-122ac exits the stitch-house lane`

The yard goes to empty at @37. Taylor is still in the yard running the feed at @37 and @38. She exits at @39. The world's memory records the yard empty while Taylor operates inside it.

Strip test: is the yard actually empty at @37? No. The persistence test: does the field stay at `[]` from @37 forward? It does — but it is wrong at @37 and @38. The field should flip at @39 (the exit bone), not at @37.

The cycle-3 fixer session notes are explicit: this finding was not dispatched for fix. The cite-index confirms state:13 is still at @37 with back=Y and no co-citations. The lonely-entries list still flags it.

Nothing has changed from my cycle-1 callout. The actors_in_yard field goes to empty on the wrong bone. It will corrupt downstream canonical state if applied as written — any chapter reading the c04 handoff will record Taylor as having left the yard two bones before she actually did. That is a genuine record error, not a formatting issue.

---

## TASTE-FLAG carry

Per the dispatch brief: state:13 remaining unresolved is a 1-of-3 dissent, not a 3-of-3 block. I am carrying this as a TASTE-FLAG for the orchestrator's disposition.

The TASTE-FLAG is:

`[state-updates:state13-anchor-lag] state:13 @37 studio.actors_in_yard exits too early — yard recorded empty while Taylor operates inside it at @38; anchor must move to @39. Not addressed in cycle-3 fixes.`

This is not a new finding. It is the same finding from cycle 1, carried forward unresolved.

---

## Summary

All 6 cycle-3 fixes are accepted. The state-updates file is structurally improved: anchor lags corrected, value formats consistent with the established chain, field-extensions properly declared, compound encoding split into separable canonical facts.

The single unresolved item is state:13 @37, the actors_in_yard anchor-lag I flagged in cycle 1. That finding was explicitly out of admin's cycle-3 scope. It remains a reality-axis failure by the rubric's strip test. I am carrying it as a TASTE-FLAG, not blocking the facet unilaterally.

If the orchestrator's aggregation rule routes this to ACCEPT (other two reviewers accepted), the TASTE-FLAG should be routed to the parking lot as a canonical write-back watch item — the showrunner should apply the actors_in_yard flip at @39, not @37, when mutating the canonical state file.

---

VERDICT
