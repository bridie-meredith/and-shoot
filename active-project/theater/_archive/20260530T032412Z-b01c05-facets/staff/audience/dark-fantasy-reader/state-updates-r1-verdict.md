---
reviewer: dark-fantasy-reader
facet: state-updates
chapter: b01-c04
phase: 5b-adversarial
date: 2026-05-27
verdict: revise
---

# dark-fantasy-reader — state-updates adversarial review, b01-c04

## Reviewing stance

The state-updates file is the world's memory. Not Taylor's memory. Not the chapter's atmosphere. The record the world keeps of what changed so that downstream chapters can't pretend it didn't. I'm reading this the way I read a veteran filing a report: did you write down what actually happened, or did you write down what was convenient?

---

## What holds

**The prop chain at @31–@32 earns it.** `prop:oc-report-sheet.holder: taylor → in-transit-yard-air → jarvis-coin-kl-coat`. Three positions, two beats, the intermediate state named. The world doesn't blink and find it in Jarvis's coat; it watches the throw. That's the world paying attention.

**The exposure flip at @36.** `actor:jarvis-coin-kl-courier.stats.exposure_risk: latent → operational`. He walked in as a courier. He's walking out as a man who knows the shape of what she's building. The world records that the threshold was crossed. Whether the bill gets called is the series' debt, not this chapter's. Filed correctly.

**Wren at @22: `knowledge.wren-in-coverage-map: absent → present-but-outside-report`.** The state records the right fact at the right beat. Not "Taylor noticed Wren" — that's narrator-interest. Not "Taylor decided not to write her down" — that's feeling. The field value holds the distinction: in the map, outside the report. The world carries that distinction in canonical memory for every downstream chapter. The moral weight of the omission is in the field value, not in a prose note. Correct.

**The skip-correct log disciplines.** @23 skipped (held-against-turn class; rubric explicitly forbids canonical state-update at approach-to-peak bones); @28/@37 skipped (enactment-after-flip; field already at new value). The author knew what not to write. That's harder than knowing what to write.

**The carve-out preamble is present and per-entry annotated.** Fourteen env entries above the 8–18% single-location band. The preamble documents the structural justification (4 locations, 2 calendar days, prop handoff chain), strip-test pass, persistence-test pass, authority-test pass. Each field-extension carries its rubric clause. The auditor won't find an undefended overshoot here.

---

## Entry-level callouts

### [state-updates:actors_in_yard-empty-before-exit] @37 — actors_in_yard fires empty two bones before the exit bone

`studio.actors_in_yard: [taylor-hebert-kl-122ac] → []` is env entry 13, anchored at @37: `taylor-hebert-kl-122ac runs the ward-feed`.

Taylor's exit bone is @39: `taylor-hebert-kl-122ac exits the stitch-house lane`. Between @37 and @39:
- @38: `the insect-feed returns wren-stitch-maker-flea-bottom-ward` — Taylor is operating inside the yard, running feed.
- @39: the exit.

The canonical actors_in_yard field goes to [] at @37. The downstream state has the yard empty while @38 has Taylor present and operating inside it. Strip test: is the yard actually empty at @37? No. The actors_in_yard value is wrong for @37 and @38; it becomes correct at @39.

This is a reality-axis failure. The skip-correct log notes @37 ("runs the ward-feed") as an enactment-after-flip class and correctly skips a capability_axis fire there. But it does not address why the actors_in_yard flip fires at the enactment bone instead of the exit bone.

The proto-line @37 is tagged `[state:13]`. Proto-line @39 is tagged `[state:14]` (the active_location transition). State:13 should move to @39 alongside state:14. At @39 the actors_in_yard empties and the location transitions simultaneously — both are the exit's consequences.

**Convergence with auditor findings:** flag-001 notes state:13 @37 has back=N in the cite-index despite @37 citing it. The cite-index error and this placement error share a root: if the actors_in_yard entry moves to @39, the back-link at @39 (which already carries state:14) needs to include state:13. The cite-index integrity issue resolves in the same regeneration pass.

---

### [state-updates:forward-citation-contamination] @9 cites state:2 @13; @22 cites state:5 @25

The state-updates entries themselves anchor correctly. State:2 fires at @13 — the scene-B open, where the location changes. State:5 fires at @25 — the scene-C open, where the day-skip lands. Both entries are right.

The proto-line citation tags are wrong. @9 pulls pig-tallow-lane location context into scene-A's dialogue peak. @22 pulls day-2 morning temporal context into scene-B's Wren-anchor bone.

The @22 case is the worse one. The Wren-anchor-discipline bone is the chapter's protected-pattern moment — the held beat where she sees Wren and does not write her down. The world should be at scene-B time (first-bell-morning-day-1) when that moment fires. The day-2 grey at @22 makes the temporal ground wrong at the chapter's most loaded beat. The held quality is contaminated by a tomorrow that hasn't arrived yet.

I'm not pushing this as a state-updates content finding — the entries are correctly placed. I'm confirming the proto-line citation tags need to come out.

**Convergence with auditor findings:** fault-002 and fault-003 exactly. Confirming both from the reader side.

---

### [state-updates:capability_axis-two-fires] @15 and @27 — watching the climb; both steps cost something

`capability_axis: 2 → 3` at @15 (insect-range extends into pig-tallow-lane).
`capability_axis: 3 → 4` at @27 (four-ward completion before Jarvis arrives).

The double-axis-fire on a single chapter is the place most likely to contain a pre-emption or lag. It doesn't here. @15 fires on the extension bone — she's reaching past the hook precinct for the first time. @27 fires on the four-ward-complete bone — the full map committed before the handoff. Both fires are on the threshold-crossing bones, not on bones where she's already running at the new level. The world records the crossings, not the running. Correct.

No finding. Noted as a clean double-fire that earns its entries.

---

## Verdict

**REVISE.**

One finding is new (actors_in_yard fires empty at @37 while Taylor operates in the yard through @38 — state:13 must move from @37 to @39). The forward-citation contamination at @9 and @22 confirms the auditor's fault-002 and fault-003. The state-updates entry content is otherwise clean: authority splits hold, field-extensions are documented, skip-correct discipline is correct, carve-out preamble is present.

Required fixes before ACCEPT:

1. Move env entry 13 (`studio.actors_in_yard: [taylor-hebert-kl-122ac] → []`) from anchor @37 to anchor @39. The exit bone is the correct anchor.
2. Remove `[state:2]` citation tag from proto-line @9 in the proto-lines file (fault-002).
3. Remove `[state:5]` citation tag from proto-line @22 in the proto-lines file (fault-003).
4. Regenerate cite-index — resolves flag-001 back=N error for state:13 and corrects the @22 pile-up count.

Items 2–4 are proto-line and cite-index fixes. Item 1 is a state-updates anchor move.

The world records what happened. Right now it records the yard empty while Taylor is still running the feed inside it. Fix the record.

---

VERDICT
