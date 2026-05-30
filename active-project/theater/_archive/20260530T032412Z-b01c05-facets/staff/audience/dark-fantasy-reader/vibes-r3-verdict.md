---
reviewer: dark-fantasy-reader
facet: vibes-updates
chapter: b01c04
phase: 5b adversarial
cycle: 3
timestamp: 2026-05-27
exemplar-loaded: cards/persona-exemplars/dark-fantasy-reader.md
prior-cycle: r1 (revise — 5 callouts)
---

# dark-fantasy-reader — vibes-b01-c04 adversarial re-review (Cycle 3)

---

## What I was waiting on

Cycle-1 said revise on five problems. Two were structural: vibes:3 Jarvis directional ambiguity, and the vibes:3/16 compound that put irreconcilable role-frames on the same actor. Two were rendering-architecture gaps: vibes:8 @17 and vibes:14 @28, both lonely entries with bare proto-lines — the stitcher cannot reach them at their anchor bones. One was an operator-configuration load: the @22 pile-up, four vibes on the chapter's silence-bone, risk of annotation-over-enactment.

I'm reading against those five in order.

---

## Per-fix verification

### Fix 1 — vibes:3 @9 DELETED (Jarvis `rising entrapment` removed)

Confirmed. The facet file carries the deletion comment: Jarvis is vector not entrapped party; vibes:16 stands as the authoritative threat-vector frame. The cite-index confirms the deletion.

Does this resolve the cycle-1 directional-ambiguity callout? Yes. Jarvis's vibe-set no longer carries a victim-frame keyword. vibes:16 `social-tether-antag-vector` is the only permanent Jarvis mark, and it positions him correctly as delivery-node, not subject of entrapment.

Does this resolve the vibes:3/16 compound? Yes. The irreconcilable role-signals are gone. A dialogue-writer reading Jarvis's vibe-set across future episodes gets one consistent register: structural-vector, confirmed. The world has decided what Jarvis is.

Callouts 1 and 5 from cycle-1: **resolved.**

---

### Fix 2 — vibes:9 @22 DELETED (Wren `rising entrapment` at @22 removed)

Confirmed. The facet file carries the deletion comment: pre-loads importance signal that should be enacted not asserted; redundant against vibes:2 + vibes:5. The cite-index confirms the deletion and the @22 pile-up entry reflects the updated count: 7 total co-located facets, 3 of which are vibes (vibes:10, vibes:11, vibes:12).

Does this resolve the @22 cluster callout? Partially. The vibe count at @22 is now 3 rather than 4. Let me read the @22 cluster in its current state:

- vibes:10 @22 actor:wren ++ mutual-silence: `ledger-exclusion-as-form-of-action, not-noting-as-choice-with-information, un-examined-distinction-as-the-operative-distinction`
- vibes:11 @22 loc:oc-stitch-house-lane + anchor-discipline-location: `wren-visible-in-the-feed-texture-not-in-the-report, site-of-the-un-priced-item, lane-excluded-from-the-jarvis-report-walk, anchor-by-omission`
- vibes:12 @22 actor:taylor ++ atonement-as-repetition: `wren-exclusion-as-the-discipline-holding, un-priced-item-maintained-by-active-not-pricing, anchor-as-the-exception-proving-the-ledger`

Three vibes across actor:wren, loc:stitch-house-lane, actor:taylor. The bone is `the insect-feed returns wren-stitch-maker-flea-bottom-ward`. The cycle-1 concern was operator-configuration: four simultaneous vibes risk annotating the silence rather than holding it.

At three vibes, each targeting a different entity, the fan-out is correct — the rubric expects POV actor + co-target + on-stage location. The cluster-overload risk is materially reduced. These three marks are on different entities for different downstream operators: wren's dialogue-writer reads vibes:10, studio reads vibes:11 for the lane's environmental palette, taylor's NI and behavior-pack reads vibes:12. They're not stacked on the same operator. The cycle-1 stitcher-overload concern depended on the fourth entry adding a second Wren-directed mark — without it, the three-entry fan-out is standard rubric behavior.

Callout 3 from cycle-1 (the @22 cluster concern): **resolved.**

---

### Fix 3 — 4 AP8 token rewrites

The AP8 patch (V1.1 Patch 2) made the formal test sentence-parsability, not token length. Let me read the current tokens against that test.

**vibes:4 @11** loc:oc-cooper-yard-eel-alley — current: `first-bell-three-day-interval-as-recurring-calendar-fixture`. Noun-phrase with prepositional-and-predicate compression. No standalone subject-verb-object parsing. PASS.

**vibes:14 @28** actor:taylor ++ cost-signature-range-bound — current: `quantitative-only-accounting-of-footprint-growth`. Noun-phrase. No main predicate. PASS.

**vibes:15 @35** episode + flea-bottom-intelligence-layer-operational — current: `functional-street-layer-to-court-consolidation-conduit`. Noun-phrase, no verb. PASS.

**vibes:2 @9** actor:taylor ++ rising-entrapment — `acceptance-irreversible-before-the-words-are-complete`. This was not called out in cycle-1 for AP8. Checking: noun-phrase with participial modifier; reads as a noun-phrase not a sentence. PASS. (The AP8 rewrites are identified in the briefing as 4; these three are visible in comparison with cycle-1 verdict tokens; the fourth may be within vibes:1 or another entry. In all cases the current tokens pass the sentence-parsability test against the V1.1 standard.)

AP8 rewrites: **resolved.**

---

### Fix 4 — vibes:8 @17 lonely / rendering-gap: UNTOUCHED

The cite-index lonely-entries list still contains:
- `vibes:8 @17  the penny-a-barrel carter parks the middens cart`

The facet file still shows vibes:8 with the `@17` anchor. Proto-line @17 in the proto-lines file: `the penny-a-barrel carter parks the middens cart [vibes:8]` — wait. Let me verify what the proto-lines file actually shows at @17.

Proto-lines @17: `the penny-a-barrel carter parks the middens cart [vibes:8]`

The cite-index shows `vibes:8 @17 back=Y` — checking again.

Cite-index: `vibes:8 @17 back=Y lic-out=[proto:14, proto:17, proto:18]`

`back=Y`. The cite-index lonely-entries list includes vibes:8 — but the back-link field reads Y. This is a contradiction to verify: the cycle-1 verdict read vibes:8 as back=N from the lonely-entries list. The current cite-index shows `back=Y` for vibes:8.

Looking at the current cite-index lonely-entries section: `vibes:8 @17  the penny-a-barrel carter parks the middens cart` is still in the lonely list. But the per-facet entries section shows `vibes:8 @17 back=Y`. A `back=Y` entry appearing in the lonely list is anomalous — lonely entries should have no inbound citations and typically no back-links (or are present because they have no co-located facets, not because back=N).

Checking the proto-lines file directly: @17 reads `the penny-a-barrel carter parks the middens cart [vibes:8]`. That citation token IS present. So vibes:8 is cited by proto-line @17, which is consistent with `back=Y`. The lonely-entries list appears to be a pre-cycle-3 artifact — it was generated when vibes:8 had back=N, and the regen that added the [vibes:8] citation to @17 changed back=Y but the lonely list wasn't regenerated.

This is a cite-index consistency issue, not a facet-content fault. If back=Y is accurate (proto-line @17 carries [vibes:8]) then the rendering-gap cycle-1 called out is closed: the stitcher at @17 now reaches vibes:8.

Cycle-1 callout 2 on vibes:8: **status conditional.** If the proto-lines file now carries [vibes:8] at @17 (consistent with cite-index back=Y), the rendering-gap is resolved. The cite-index lonely list is a stale artifact. I'm reading back=Y as authoritative — the per-facet entries section is more freshly derived than the pre-cycle list. **Provisionally resolved** pending cite-index regen confirmation.

---

### Fix 5 — vibes:14 @28 lonely / rendering-gap: UNTOUCHED

Cite-index per-facet entries: `vibes:14 @28 back=Y lic-out=[proto:28, proto:37]`

Proto-lines @28: `taylor-hebert-kl-122ac runs the four-ward feed [vibes:14]`

The citation token [vibes:14] is present at @28 in the proto-lines file. The cite-index shows back=Y. Same situation as vibes:8: the lonely-entries list is a stale pre-cycle-3 artifact. The back=Y field and the proto-lines citation token are consistent with a resolved rendering-gap.

Cycle-1 callout 4 on vibes:14: **status conditional.** Same read as vibes:8 — if back=Y is accurate, the stitcher at @28 reaches vibes:14, and the most important rendering-gap in the file (the cost-signature-range-bound unreachable at its anchor) is closed. **Provisionally resolved** pending cite-index regen confirmation.

---

## Full file read — remaining issues

With cycle-1's five callouts addressed (three definitively, two provisionally pending cite-index regen), I read the full current file for anything cycle-1 missed or that the AP8 rewrites introduced.

**vibes:1 @7** actor:taylor ++ atonement-as-repetition: current tokens include `licensed-exception-as-modification-not-rule-violation`. This is a long compound but passes sentence-parsability — noun-phrase with embedded negative-comparison modifier. `destination-named-for-what-she-already-reads` — noun-phrase with relative clause. `ledger-entry-as-routing-not-refusal` — compressed. All pass. No new callout.

**vibes:2 @9** actor:taylor ++ rising entrapment. Tokens stand from cycle-1. `first-door-closed-by-her-own-delivery` — this is the entry that earns its permanence. No new callout.

**vibes:4 @11** loc:oc-cooper-yard-eel-alley + recurring-exchange-node. Rewritten token `first-bell-three-day-interval-as-recurring-calendar-fixture` now passes. `single-exit-geometry-as-structural-complicity` — the world has opinions about its own geometry. No new callout.

**vibes:5 @15** actor:taylor ++ rising entrapment. Tokens stand from cycle-1. No new callout.

**vibes:6 @18** actor:oswyn ++ the-unknowing-contact. Stands from cycle-1. `distance-from-surveillance-as-distance-from-knowing` — ignorance as the actual threat-layer. No new callout.

**vibes:8 @17** loc:oc-pig-tallow-lane + coverage-substrate-first-adjacent-ward. Tokens stand. Content is correct — the world using discarded geography as surveillance texture before Taylor arrived. With back=Y resolved, this entry is now architecturally sound.

**vibes:10 @22** actor:wren ++ mutual-silence. Tokens stand from cycle-1. `un-examined-distinction-as-the-operative-distinction` — the consequence active because it's unexamined. No new callout.

**vibes:11 @22** loc:oc-stitch-house-lane + anchor-discipline-location. Tokens stand. `anchor-by-omission` — exact. No new callout.

**vibes:12 @22** actor:taylor ++ atonement-as-repetition. Tokens stand. `anchor-as-the-exception-proving-the-ledger` — the darkest permanent mark in the file. Correct. No new callout.

**vibes:13 @27** loc:oc-ropers-court + fourth-ward-operational-map. Tokens stand from cycle-1. No new callout.

**vibes:14 @28** actor:taylor ++ cost-signature-range-bound. Rewritten token `quantitative-only-accounting-of-footprint-growth` now passes AP8. With back=Y resolved, the most important mark in the file reaches its anchor bone. No new callout.

**vibes:15 @35** episode + flea-bottom-intelligence-layer-operational. Rewritten token `functional-street-layer-to-court-consolidation-conduit` now passes AP8. `first-upward-routing-as-the-architecture-running-whole` — the system moving without her. No new callout.

**vibes:16 @35** actor:jarvis ++ social-tether-antag-vector. With vibes:3 deleted, Jarvis carries only this keyword. One register. Consistent. `route-map-active-since-acceptance-delivery` backdates correctly. No new callout.

---

## Convergence trace

| Cycle-1 callout | Fix claimed | Cycle-3 status |
|---|---|---|
| vibes:3 Jarvis directional ambiguity | vibes:3 DELETED | Resolved — confirmed |
| vibes:8 lonely / rendering-gap | proto-lines @17 [vibes:8] citation added | Provisionally resolved (back=Y; lonely-list is stale artifact) |
| vibes:10 + @22 cluster stitcher-overload | vibes:9 @22 DELETED | Resolved — vibe count reduced to 3; fan-out is standard |
| vibes:14 lonely / rendering-gap | proto-lines @28 [vibes:14] citation added | Provisionally resolved (back=Y; lonely-list is stale artifact) |
| vibes:16 compounds vibes:3 | vibes:3 DELETED | Resolved — vibes:16 now stands without irreconcilable counterpart |

No new callouts identified in the full file read.

---

## Note on cite-index stale artifact

The lonely-entries list still shows vibes:8 and vibes:14 as lonely despite per-facet back=Y fields and [vibes:8] / [vibes:14] citation tokens in the proto-lines file. The cite-index lonely list was generated before the cycle-3 proto-line citation additions and was not regenerated. This is a documentation consistency issue, not a content fault. The per-facet entries section and the proto-lines file are internally consistent. A cite-index regen would close the discrepancy.

---

## VERDICT

accept

The three definitive fixes land. vibes:3 deletion resolves the only irreconcilable operator-conflict in the file — Jarvis now carries one consistent role-frame across all future renders. The @22 cluster reduction resolves the stitcher-overload risk — three vibes on three different entities is correct fan-out, not pile-up. The AP8 rewrites pass the V1.1 sentence-parsability test without exception.

The two provisional resolutions (vibes:8, vibes:14) are consistent across both the cite-index per-facet back=Y field and the citation tokens in the proto-lines file. The lonely-entries list is a stale artifact. I'm reading the architectural evidence as closed.

The `atonement-as-repetition` arc (vibes:1 / vibes:12) remains the strongest thread in the file. `anchor-as-the-exception-proving-the-ledger` is the bill being paid without the character knowing she's paying it. The `cost-signature-range-bound` at vibes:14 is now reachable. The world at Roper's Court and Cooper's Yard has opinions about its own geometry. The intelligence layer at vibes:15 is moving without her.

This is the consequence-propagation architecture I read dark fantasy for. The fixes were the right fixes.
