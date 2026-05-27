---
reviewer: worm-canon-pedant
facet: state-updates
chapter: b01c04
phase: 5b-adversarial
mode: facet-adversarial (URI-AUDIENCE-AGGREGATION-RULE; single-reviewer verdict; any revise or fail blocks)
timestamp: 2026-05-27
---

# state-updates — adversarial read (b01c04, 39-bone)

*[running the consolidated state-updates file. wiki-tab equivalent open: rubric, proto-lines, cite-index, scene-map, auditor Phase 5 report. looking for what the mechanical scan missed.]*

---

## Reading posture

State-updates is canon-memory write-back. Every entry the showrunner applies at the cross-facet boundary carries forward into downstream chapters. A bad entry in b01c04 becomes a corrupt baseline for b01c05. My read is adversarial because state-tracking lies compound — the error that looks small in isolation becomes the contradiction that breaks the chapter five bones.

The auditor ran the mechanical pass and caught the forward-citation faults (fault-002, fault-003) and the duplicate-entry miss in the cite-index. My job is what the mechanical scan cannot reach: wrong anchor timing, non-canonical value forms, undeclared field extensions, and identical-duplicate pairs that aren't incompatible-state (so the contradiction scanner skips them).

Three-error fatigue threshold: if I clock more than three hard callouts, I move to arm's-length distance. I track as I go.

---

## ENV SLICE — per-entry read

**state:1 @1 — studio.time_of_day: third-bell-noon → first-bell-morning**

Chapter-open time reset. Prior chapter closed at third-bell-noon; b01c04 opens at first-bell-morning. Strip test: persists through state:5 at @25. Persistence: 24 bones. Authority: studio. Reality: the clock moved between chapters; @1 is the first-bone reset record.

That tracks.

**state:2 @13 — studio.active_location: oc-cooper-yard-eel-alley → oc-pig-tallow-lane**

Scene-B open, location transition. The auditor's fault-002 caught the forward-citation problem: proto-line @9 wrongly cites state:2, pulling the pig-tallow-lane location into scene-A's dialogue peak. The entry itself is correctly anchored at @13. The fault is in the proto-line citation token, not in this entry.

Entry: CORRECT. The forward-citation contamination is a proto-line problem; the entry anchors on the right bone.

**state:3 @15 — studio.coverage_active_range: oc-hook-precinct → oc-hook-precinct + oc-pig-tallow-lane**

Field-extension. New field tracking which ward-zones are under Taylor's insect-feed as an env-observable fact. The carve-out preamble defends it: studio.coverage_active_range tracks environmental presence (insects in zone = env fact); actor:taylor.capability tracks the deployment scale. The distinction holds if you read "which zones have Taylor's insects present" as a location-state corollary — an observer in oc-pig-tallow-lane would note unusual insects. That's environmental.

The field-extension is documented inline. The field is a tracked-state-aspect (which zones are covered), not a perception or stylistic flourish. Reality: coverage genuinely changes at @15 (Taylor extends the range). Persistence: the field remains at the new value until state:4 extends it further.

Reluctant accept. The author needed a home for this and the documentation is present. On the border between env-fact and capability-state, but the carve-out is properly filed.

Entry: ACCEPT with noted boundary tension on field classification.

**state:4 @22 — studio.coverage_active_range: oc-hook-precinct + oc-pig-tallow-lane → oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane**

Same field-extension, second ward added. The auditor's fault-003 caught the forward-citation at @22 (proto-line @22 wrongly cites state:5, the day-2 time-of-day entry). Again: the entry itself is correctly anchored at @22.

Scene-map check: @22 is in scene-B's Wren-anchor-discipline protected-pattern (@22 feed returns Wren, @23 Taylor holds the feet). Scene-B peak-bone is @18. @22 is post-peak within scene-B, in the protected-pattern zone — not a held-against-turn class bone (held-against-turn requires immediately adjacent to a peak-bone; @22 is four bones past @18). State-update at @22 is not forbidden by the held-against-turn rule. Reality: the stitch-house-lane zone genuinely enters coverage at @22. Persistence: field stays at the new value until state:7 flips it to the complete-set at @27.

Entry: CORRECT.

**state:5 @25 — studio.time_of_day: first-bell-morning-day-1 → early-morning-grey-day-2**

Day-skip. Scene-C opens on day-2. The temporal transition occurs in the inter-scene gap (between @24 and @25). @25 is the first bone where the new temporal state is established in the narrative. No proto-line exists for the inter-scene gap — firing at @25 (first rendering of the new time state) is the closest valid anchor. Strip test: early-morning-grey-day-2 persists through chapter close. Reality: the day genuinely changed. Authority: studio.

Entry: CORRECT.

**state:6 @26 — studio.active_location: oc-pig-tallow-lane → oc-ropers-court**

Here is where I stop and push.

Scene-C opens at @25: "the early-morning grey empties Roper's Court." That proto-line establishes Roper's Court as the rendering environment. loc-state:4 fires at @25 with co-citations to sensory:3 and state:5. The env-frame turns over at @25.

State-updates fires studio.active_location at @26 — one bone later. Proto-line @26 is "taylor-hebert-kl-122ac enters Roper's Court." That's the actor-entry beat, not the env-frame-turnover beat.

The rubric says fire "on the beat the field actually flips." The question is when does studio.active_location flip — when the scene-open env-frame establishes the location (@25) or when the POV actor enters that location (@26)?

The s01e01 calibration anchor for location transitions uses env-frame establishment as the flip-beat. loc-state:4 fires at @25. The studio.active_location should co-fire with the env-frame. Firing at @26 instead is a one-bone lag — anti-pattern #7 (lagging variant). At @25, the studio.active_location field is still oc-pig-tallow-lane by record, but the proto-line establishes Roper's Court as the env. The stitcher rendering @25 receives location-state saying pig-tallow-lane while the env-frame says Roper's Court. One-bone contradiction window.

Error count: 1.

The auditor's flag-001 noted a state:6 dual-anchor cite-index gap (the @27 cross-citation of state:6 not reflected in state:6's own cite-index entry) but did not trace the gap to the root cause — the entry itself is on the wrong bone.

`[state-updates:state:6] @26 — studio.active_location fires one bone late. Entry should anchor at @25 (scene-open env-frame; loc-state:4 fires here), not @26 (actor-entry). At @25, the field record reads oc-pig-tallow-lane while the proto-line establishes Roper's Court — one-bone contradiction window for the stitcher. Move entry to @25.` Auditor overlap: flag-001 (cite-index dual-anchor gap noted; root cause of the lag not identified).

Entry: INCORRECT — lagging (anti-pattern #7).

**state:7 @27 — studio.coverage_active_range: oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane → four-ward-complete**

The third ward extension completing the chapter's capability arc. Strip test: four-ward-complete persists through chapter close. Reality: coverage genuinely extends to the fourth ward at @27. Authority: studio (field-extension).

Now the value form: states:3 and :4 used explicit zone-set notation — "oc-hook-precinct + oc-pig-tallow-lane." State:7 switches to "four-ward-complete." That's a descriptor, not a zone-set. The showrunner's write-back receives "four-ward-complete" as the canonical field value for studio.coverage_active_range. What does b01c05 inherit? A label, not a zone-set. If b01c05 adds a fifth ward to the coverage map, the prior entry the author needs to chain from is "four-ward-complete," not a parseable zone-set.

The frugality axis requires `<new>` values that are canonical-correct and consistent with the field's established value format. The explicit zone-set format is established by two prior entries. Switching to a descriptor at the third entry breaks the chain.

Error count: 2.

`[state-updates:state:7] @27 — <new> value "four-ward-complete" is a completion descriptor, not an explicit zone-set. Prior entries (states:3, :4) establish the format: oc-hook-precinct + oc-pig-tallow-lane + [next zone]. The showrunner write-back carries "four-ward-complete" forward; b01c05 cannot chain from this without resolving the descriptor. Correct to explicit form: oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane + oc-ropers-court.` Auditor overlap: none.

Entry: INCORRECT — frugality violation (value-form inconsistency with established field format).

**state:8 @29 — studio.actors_in_yard: [] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier]**

**state:9 @29 — studio.actors_in_yard: [] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier]**

Two entries. Same target. Same field. Same beat. Same old value. Same new value. Identical.

The rubric's back-contract: "no mid-beat ambiguity. Each (target, field) at each beat resolves to exactly one new value. Contradictions across entries on the same (target, field, beat) trigger the schema's contradiction rule: delete both, flag for re-author."

These are not contradictory — they're identical. But the effect is the same problem: the field is written twice at the same beat, once per each of the two actors entering the yard. The author split the yard-entry into two actor-entry events but used the full resulting roster for both entries, rather than building the roster incrementally ([] → [taylor] at the first entry, [taylor] → [taylor, jarvis] at the second). The identical form is a different error from incompatible-state but is still a violation: the schema expects one (target, field) resolution per beat.

Error count: 3.

Fatigue threshold reached. I am now at arm's-length reading for the remaining entries. I can still be won back by one precise moment that shows the file knows what it's doing.

`[state-updates:state:8 + state:9] @29 — Identical entries: studio.actors_in_yard: [] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier] appears twice at the same beat. The schema's one-resolution-per-(target, field, beat) rule is violated. If two actor-entries were intended to be recorded incrementally, the correct form is two entries with distinct transitions: [] → [taylor-hebert-kl-122ac] and [taylor-hebert-kl-122ac] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier], anchored to their respective entry beats. Delete one of the identical entries and, if separate actor-entries are load-bearing, decompose into incremental form at the correct anchors.` Auditor overlap: auditor's pass-002 checked for incompatible-state pairs only; identical-entry pairs were not in scope of the contradiction scan.

Entries: INCORRECT — identical duplicate, schema violation.

**state:10 @31 — prop:oc-report-sheet.holder: taylor-hebert-kl-122ac → in-transit-yard-air**

Report-sheet handoff, release beat. Holder transitions to in-transit-yard-air — consistent with the s01e01 calibration anchor (mid-air-between-them). Protected-pattern in scene-map: @31 peak-shadow bone. Field-extension declared and documented. Persistence: in-transit-yard-air holds until state:11 fires at @32. Strip test passes.

Still reading. This is clean.

Entry: CORRECT.

**state:11 @32 — prop:oc-report-sheet.holder: in-transit-yard-air → jarvis-coin-kl-coat**

Jarvis pockets the sheet. The holder value "jarvis-coin-kl-coat" is more precise than just the actor slug — it records the sheet is in the coat pocket. That precision is appropriate (the sheet's specific location within Jarvis matters for how it would be retrieved). Strip test: jarvis-coin-kl-coat persists through chapter close.

Entry: CORRECT.

**state:12 @36 — studio.actors_in_yard: [taylor-hebert-kl-122ac, jarvis-coin-kl-courier] → [taylor-hebert-kl-122ac]**

Jarvis exits at the chapter's peak-bone (@36). The `<old>` value chains from the @29 entry (whichever version survives the dedup). The field goes from both actors to Taylor-only. Persistence: [taylor-hebert-kl-122ac] persists through state:13 at @37. Scene-map: @36 is the chapter peak-bone; state-update at the peak-bone is appropriate and expected.

Entry: CORRECT. (The value it chains from requires the duplicate-entry issue to be resolved, but the entry itself is formally correct.)

**state:13 @37 — studio.actors_in_yard: [taylor-hebert-kl-122ac] → []**

Taylor exits the yard at @37. The proto-line is "taylor-hebert-kl-122ac runs the ward-feed" — a transition bone, Taylor walking back through the ward from the yard. The `<old>` is [taylor-hebert-kl-122ac], matching state:12's `<new>`. Strip test: [] persists through chapter close. The auditor's flag-001 noted this entry's cite-index back=N despite proto-line @37 citing [state:13] — a cite-index defect, not an entry defect.

One clean entry after three errors. Not enough to win me back fully but the Taylor/Jarvis slice is shaping up correctly.

Entry: CORRECT.

**state:14 @39 — studio.active_location: oc-cooper-yard-eel-alley → chapter-close-stitch-house-lane-exit**

The chapter-close location transition. Taylor exits the stitch-house lane — @39 is the final bone.

The `<new>` value: "chapter-close-stitch-house-lane-exit." That is not a location slug. The prior location values in this file are all slugs: oc-cooper-yard-eel-alley, oc-pig-tallow-lane, oc-ropers-court. "Chapter-close-stitch-house-lane-exit" imports a narrative event label (chapter-close) into a canonical location field. The showrunner writes this back to studio.active_location. The b01c05 session opens with studio.active_location = "chapter-close-stitch-house-lane-exit."

That is not a location. That is a stage direction. Whatever b01c05 expects at the start of its scene-A, it expects a location slug, not a chapter-boundary descriptor.

`[state-updates:state:14] @39 — <new> value "chapter-close-stitch-house-lane-exit" is a narrative event label, not a location slug. Canonical write-back corrupts studio.active_location for b01c05 (field carries "chapter-close-stitch-house-lane-exit" into the next chapter). Correct to the exit location slug: oc-stitch-house-lane or the equivalent canonical slug for where Taylor stands at chapter close.` Auditor overlap: none.

Entry: INCORRECT — frugality/reality violation (non-canonical `<new>` value form).

---

## JARVIS SLICE — per-entry read

**state:15 @5 — actor:jarvis-coin-kl-courier.location: lower-city-in-transit → cooper-yard-eel-alley-lane-mouth**

Jarvis at the lane-mouth. Back=N in cite-index (proto-line @5 cites state:1, not state:15). Back=N for a real state change is a coverage gap in the cite-graph but not a rubric violation on the entry itself. The showrunner still applies this at write-back. Reality: Jarvis is at the lane-mouth at @5. Persistence: through @11. Authority: Jarvis fork.

Entry: CORRECT (back=N is a cite-graph gap, not an entry fault).

**state:16 @9 — actor:jarvis-coin-kl-courier.stats.active_deliveries: 0 → 1**

The routing arrangement converts to an active delivery. The Jarvis slice preamble declares: "none; baseline V2 rubric § actor-state applies." No field-extensions declared.

active_deliveries — is this a standard tracked field on Jarvis's state.md schema or an invented field? Standard actor-state fields (as described in the rubric) are position, inventory, knowledge, exposure-state, posture. active_deliveries sits in stats and sounds operationally invented for this chapter's tracking purposes. Without a field-extension declaration, and without access to the actor card from here, I cannot confirm the field exists.

`[state-updates:state:16] @9 — actor:jarvis-coin-kl-courier.stats.active_deliveries used without field-extension declaration in the Jarvis slice preamble (preamble declares no extensions). If this field is not on Jarvis's state.md schema, anti-pattern #6 (invented field) applies. Verify actor card. If the field is not present, delete the entry and add a field-extension declaration if the field is genuinely needed. If the field is on the actor card, add an explicit note in the preamble.` Auditor overlap: none.

Entry: CONDITIONAL — depends on actor card verification.

**state:17 @11 — actor:jarvis-coin-kl-courier.location: cooper-yard-eel-alley-lane-mouth → lower-city-in-transit**

Jarvis exits the lane-mouth. Chain from state:15. Frugality: `<old>` matches state:15's `<new>`. Peak-shadow bone (@11 in scene-A exit-pair). Reality: he exits at @11. Authority: Jarvis fork.

Entry: CORRECT.

**state:18 @29 — actor:jarvis-coin-kl-courier.location: lower-city-in-transit → cooper-yard-eel-alley**

Jarvis returns. Chain from state:17. Frugality passes. Reality: he enters the yard at @29. Authority: Jarvis fork.

Entry: CORRECT.

**state:19 @29 — actor:jarvis-coin-kl-courier.inventory: [] → [otto-confirmation-note]**

Jarvis arrives with the note. Inventory was empty. Fires at @29 (arrival), not @30 (display). Correct timing: he has the note when he enters; the display is a subsequent action, not the possession-acquisition event. Authority: Jarvis fork.

Entry: CORRECT.

**state:20 @32 — actor:jarvis-coin-kl-courier.inventory: [otto-confirmation-note] → [otto-confirmation-note, taylor-movement-pattern-report]**

Pockets the sheet. `<old>` matches state:19's `<new>`. Inventory adds the report alongside the existing note. Cross-check with state:11 (prop:oc-report-sheet.holder → jarvis-coin-kl-coat): consistent — prop tracks the sheet's holder-location, actor inventory tracks possession. No contradiction.

Entry: CORRECT.

**state:21 @36 — actor:jarvis-coin-kl-courier.location: cooper-yard-eel-alley → lower-city-in-transit**

Jarvis exits at the chapter peak-bone. Chain from state:18. Frugality passes. Authority: Jarvis fork.

Entry: CORRECT.

**state:22 @36 — actor:jarvis-coin-kl-courier.stats.exposure_risk: latent → operational**

Same field-extension concern as state:16. exposure_risk is in stats; Jarvis preamble declares no extensions. Standard actor-state schema fields don't include exposure_risk. Operational and latent are plausible state values for an exposure tracking field, but the field itself needs to be on the schema.

`[state-updates:state:22] @36 — actor:jarvis-coin-kl-courier.stats.exposure_risk used without field-extension declaration (same gap as state:16). If not on Jarvis's state.md schema, anti-pattern #6. Verify actor card; add field-extension declaration or delete.` Auditor overlap: none.

Entry: CONDITIONAL — depends on actor card verification.

---

## TAYLOR SLICE — per-entry read

**state:23 @9 — actor:taylor-hebert-kl-122ac.stats.position_in_kl: smallfolk-anonymous → named-conduit-at-courier-tier**

The acceptance converts Taylor's functional status. Peak-bone @9 in scene-A. NI co-citation: narrator:3 @9 confirmed (auditor pass-004). Strip test: named-conduit-at-courier-tier persists through the chapter and into future chapters. Reality: the arrangement is confirmed at @9. Authority: Taylor fork.

position_in_kl is in stats and not among the declared field-extensions. Unlike the Jarvis stats fields (active_deliveries, exposure_risk), position_in_kl reads as a core substance-framework axis — character's social insertion in the setting. That's the kind of field a substance-framework state schema would track by design. Lower concern than the Jarvis fields which sound operational and chapter-specific.

Accept with actor-card caveat, lower urgency.

Entry: ACCEPT.

**state:24 @9 — actor:taylor-hebert-kl-122ac.knowledge.arrangement-state: licensed-exception-considered → licensed-exception-active**

Second entry at peak-bone @9. Field-extension declared. NI co-citation covered by narrator:3 @9. Two entries on two different fields at the peak-bone — licit per rubric (one entry per field per beat). Frugality passes. Reality: the arrangement flips from considered to active at @9.

Entry: CORRECT.

**state:25 @15 — actor:taylor-hebert-kl-122ac.stats.capability_axis: 2 → 3**

First capability_axis flip. Existing integer field; Taylor slice preamble confirms. Chapter contract: +2.0 across c04; first +1 at @15, second +1 at @27. NI co-citation: narrator:11 @15 confirmed (pass-004).

This is the canonical Worm axis-tracking structure. The field moves with demonstrated cause: Taylor extends the range at @15, the capability axis reflects it. No invented mechanics, no excess.

Entry: CORRECT.

**state:26 @18 — actor:taylor-hebert-kl-122ac.knowledge.oswyn-as-unknowing-coverage-node: absent → present**

Scene-B peak-bone (@18). Oswyn enters the feed. Taylor knows he's a node, and the field name encodes that he doesn't know. Field-extension declared. NI co-citation: narrator:4 @18 confirmed (pass-004).

"Unknowing" in the field name is doing double duty — encoding Taylor's knowledge of Oswyn's non-knowledge. That's exactly the kind of tracking the Worm power mechanic requires: the consent state of the person being used matters for downstream cost accounting. The field name is precise.

Entry: CORRECT.

**state:27 @22 — actor:taylor-hebert-kl-122ac.knowledge.wren-in-coverage-map: absent → present-but-outside-report**

The Wren-anchor-discipline bone. Field-extension declared. NI co-citation: narrator:6 @22 confirmed (pass-004). Strip test: present-but-outside-report persists through chapter close (Wren is never added to the report during b01c04).

"Present-but-outside-report" as a compound value: the present part is the state-change; the outside-report part is a deliberate omission that is itself load-bearing for future chapters. The compound is slightly verbose but the canonical memory needs to carry both components — "Wren visible" and "not reported" are different downstream triggers. The value holds.

One clean Wren-discipline entry at the chapter's load-bearing plant bone. This is what I've been waiting for. The file knows what it's doing at the core of the Taylor arc. Won back from arm's-length reading. Finishing at full attention.

Entry: CORRECT.

**state:28 @27 — actor:taylor-hebert-kl-122ac.stats.capability_axis: 3 → 4**

Second capability_axis flip. Chain from state:25. Chapter contract exact delivery: +1 at @15, +1 at @27 = +2 total, matching the chapter contract. NI co-citation: narrator:13 @27 confirmed (pass-004).

Entry: CORRECT.

**state:29 @31 — actor:taylor-hebert-kl-122ac.knowledge.intelligence-routing-state: dormant → routing-to-jarvis-active**

At @31, Taylor delivers the report-sheet. Routing flips from dormant to active. Field-extension declared. NI co-citation: narrator:7 @31 confirmed (pass-004). Strip test: routing-to-jarvis-active persists through chapter close (she's still routing at @37-@39). Reality: the delivery act is the transition point.

Entry: CORRECT.

---

## File-level assessment

**Curve shape:** The carve-out preamble justifies 14 env entries at ~36% of 39 bones, calibrated for multi-location multi-day vs. the baseline 8-18% for single-location single-day. The per-entry defenses in the preamble are filed. 29 total entries across 39 bones. Target diversity: studio.*, prop:oc-report-sheet.*, actor:jarvis-coin-kl-courier.*, actor:taylor-hebert-kl-122ac.*. Four target classes — passes.

**Taylor NI co-citation (SEAM-NI-CO-CITATION):** Verified by auditor pass-004 — all six required anchors (@9/@15/@18/@22/@27/@31) covered. This is the most consequential cross-facet contract and it holds.

**Duplicate-entry scan:** The mechanical contradiction scan (auditor pass-002) checked for incompatible-state pairs on the same (target, field, beat). It did not catch identical pairs — state:8 and state:9 are identical, not contradictory, and slipped through. This is the gap between the auditor's mechanical check and an adversarial read.

**Auditor findings on state-updates specifically:** The auditor's forward-citation faults (fault-002: proto-line @9 cites state:2; fault-003: proto-line @22 cites state:5) both trace to proto-line citation tokens, not to the state-updates entries themselves. The entries are correctly anchored; the citations in the proto-lines file are wrong. My read confirms this analysis.

**What the mechanical scan missed:**
1. state:6 @26 — one-bone lag (studio.active_location on wrong anchor)
2. state:7 @27 — non-slug value form for coverage_active_range
3. state:8 + state:9 @29 — identical duplicate pair (identical, not contradictory; bypassed the incompatible-state scanner)
4. state:14 @39 — narrative label as canonical `<new>` value
5. state:16 + state:22 — undeclared fields on Jarvis actor slice (conditional on actor card)

---

## Callout summary

`[state-updates:state:6] @26 — studio.active_location lags by one bone. Entry anchors at @26 (actor-entry) instead of @25 (scene-open env-frame; loc-state:4 fires here). At @25, the field record reads oc-pig-tallow-lane while the proto-line establishes Roper's Court — one-bone contradiction window for the stitcher. Move entry to @25.` — Auditor overlap: flag-001 (cite-index dual-anchor gap noted; one-bone lag not identified as root cause).

`[state-updates:state:7] @27 — coverage_active_range <new> value "four-ward-complete" is a completion descriptor, not the explicit zone-set format established by states:3 and :4. The showrunner write-back carries "four-ward-complete" forward; b01c05 cannot chain the field without resolving the descriptor. Correct to explicit form: oc-hook-precinct + oc-pig-tallow-lane + oc-stitch-house-lane + oc-ropers-court.` — Auditor overlap: none.

`[state-updates:state:8 + state:9] @29 — Identical entries: studio.actors_in_yard: [] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier] duplicated at the same beat. One-field-one-resolution-per-beat rule violated. If both actor-entries are meant to be recorded, decompose into incremental form at the correct anchor beats: [] → [taylor-hebert-kl-122ac] and [taylor-hebert-kl-122ac] → [taylor-hebert-kl-122ac, jarvis-coin-kl-courier].` — Auditor overlap: auditor pass-002 checked for incompatible-state pairs only; identical pairs were not in scope.

`[state-updates:state:14] @39 — studio.active_location <new> value "chapter-close-stitch-house-lane-exit" is a narrative event label, not a location slug. Canonical write-back sets studio.active_location for b01c05 to this non-slug value. Correct to the exit-location slug: oc-stitch-house-lane or equivalent canonical slug for Taylor's position at chapter close.` — Auditor overlap: none.

`[state-updates:state:16] @9 + [state-updates:state:22] @36 — actor:jarvis-coin-kl-courier.stats.active_deliveries and .stats.exposure_risk used without field-extension declarations in the Jarvis slice preamble (which declares no extensions). If either field is not on Jarvis's state.md schema, anti-pattern #6 (invented field) applies. Verify actor card; add field-extension declarations in the preamble, or delete entries. Required before canonical write-back.` — Auditor overlap: none.

---

## VERDICT

**revise**

The Taylor slice is largely clean. The capability-axis chain is correct, the knowledge field-extensions are properly declared, the NI co-citation contract holds, and the Wren-anchor-discipline entry at @22 is the chapter's load-bearing plant correctly registered. That part knows what it's doing.

The env slice and the Jarvis slice have four hard structural problems the mechanical scan missed: one anchor on the wrong bone (state:6), two non-canonical value forms that will corrupt the showrunner write-back (states:7 and :14), and a duplicate-entry pair that violates the one-resolution-per-field-per-beat rule (states:8+9). The Jarvis operational fields (state:16, state:22) need actor-card verification before the entries can be confirmed.

None of these are canon-consistency problems with the story. All of them are state-tracking integrity problems that compound downstream. That's the kind of error I track because it's the kind that breaks chapter 12.
