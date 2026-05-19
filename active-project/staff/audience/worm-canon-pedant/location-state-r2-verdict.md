---
persona: worm-canon-pedant
facet: location-state
episode: b01c01
cycle: 2
phase: 5b
date: 2026-05-19
verdict: ACCEPT
---
# Verdict

The one entry I flagged is gone. The surviving four are positionally clean and one of them — the light-angle read at @20 — is still the piece of this file I respect most.

# Stage 1 — strict affirmative-demonstration

**loc-state:1 @1** (corner-room-threshold — alley-mouth narrows to a doorway; step in is only gap):
- Necessity: anchor verb is `enters` — transitional, unambiguous. First beat in this location-and-moment; place-anchor license fires automatically per rubric. PASS.
- Interestingness: one focus-element named: the threshold gap as the only passage between street and work-floor. Nothing else in the room invoked. PASS.
- Frugality: first entry. No prior state to inherit. PASS.

**loc-state:2 @9** (door-open-street-facing — Hook visible through facing side; foot-traffic readable from threshold without stepping out):
- Necessity: a door-opening is a state-change; the `door-open-street-facing` condition in the conditions field documents it. The sensory note names what the opening creates: a sightline through which the Hook is visible. Anchor is a physical-action beat that produces new environment. PASS.
- Interestingness: focus-element is the view angle the open door creates — one directional fact, not a room inventory. PASS.
- Frugality: genuine condition-change from prior state (threshold-closed, no street view → door-open, Hook visible). PASS.

**loc-state:3 @15** (afternoon / hook-mouth-visible — Watch column passes Hook's curve, visible from @9's angle):
- Necessity: time has advanced from morning to afternoon (a genuine time-step, not a cosmetic time-field variation), and a new actor (Watch column) moves through the established sightline. Both qualify as state-changes under the rubric. The Watch column passing is itself a movement beat in the environment; loc-state fires on that movement, not on Taylor's stillness. PASS.
- Interestingness: focus-element is the Watch column at the Hook's curve — geographically specific, not generic street activity. The callback to @9's angle is structural tracking, not re-naming. PASS.
- Frugality: two simultaneous state-changes (time, new entrant). @9's sightline is being activated by new content, not re-described. PASS.

**loc-state:4 @20** (morning / alley-street-mouth — same alley-mouth as @1; light angle shifted earlier, third or fourth day):
- Necessity: anchor verb is `enters` on Wren crossing the street-mouth — movement beat. The alley-mouth anchor ties the crossing to the @1 position; the light-angle differential encodes elapsed days through environmental geometry. For this character, reading a sun-angle as elapsed-time is not a narrative shortcut — it is how she processes space. PASS.
- Interestingness: focus-element is the light-angle differential against @1. One perceptible comparison. Not atmosphere; not mood; a measurement. PASS.
- Frugality: different day, morning but not the arrival morning — the time field is correct and the entry marks a genuine state-change (new day, new arrival). PASS.

# Stage 2 — adversarial seam-finding

**loc-state:1 @1:** No anchor-verb concern; `enters` is unambiguous. One seam worth naming: the sensory note says "the step in is the only gap between street and work-floor" — is "only gap" a claim about the floor plan that the location card might contradict? If the corner-room has a second entrance, this entry is factually wrong and Taylor would know it within one scene. This is a factual-accuracy seam, not a rubric-axis seam. It cannot be closed from the facet file alone. Weak concern; does not block under the three-axis test because the place-anchor license does not require the sensory note to be exclusive.

**loc-state:2 @9:** No seam. Door-opening as sightline-change is canonical for this rubric.

**loc-state:3 @15:** The sensory note references "@9" by ID rather than by description ("the angle Coll opened in @9"). This is fine as an authoring convention and is appropriate structural tracking — but a reader consuming the prose render will not see the citation marker. The stitcher must translate this into something the prose can carry. This is a stitcher concern, not a loc-state rubric concern. Does not block.

**loc-state:4 @20:** This entry is the one I praised in cycle-1 and my position has not changed. The only thing to stress-test: the time field says "morning" while the sensory note says "light angle shifted earlier than the arrival morning." These are consistent — it is still morning on day N, but morning on day N has a different light position than morning on day 1. Internally coherent. No block.

# Cycle-2 delta evaluation

My cycle-1 REVISE callout was:
- loc-state:3 @11 — anchor verb "threads the needle" (dexterity-stillness, not transitional); @9 already opened this location-and-moment; no continuity-carry token; sensory note naming ambient noise density rather than a selected perceptible element; necessity axis and interestingness axis both failing.

That entry is CUT in cycle-2. The fixer CUT notation in the facet file reads: "anchor verb 'threads the needle' is dexterity-stillness — REJECT per rubric URI-FACETS-CYCLE-1 dexterity-verb clause; @9 already opened this location-and-moment; necessity-axis fails; 2-of-3 reviewer dissent (dark-fantasy-reader + worm-canon-pedant)." This is an exact match to my r1 callout. The cut is correct. The newly-promoted REJECT clause (URI-FACETS-CYCLE-1 dexterity-verb) is the mechanical promotion of the pattern I identified. My complaint is closed.

The sensory-baseline studio notes appended as comments to loc-state:1 are documentation of smell and sound baselines for the chapter's sensory facet. They are comment-adjacent; they are not new loc-state entries. I do not evaluate them under the three-axis rubric. The renumbering (old loc-state:5 @15 → new loc-state:3 @15; old loc-state:6 @20 → new loc-state:4 @20) is bookkeeping; the surviving entries are unchanged in content.

# Aggregate stance

ACCEPT. Sole cycle-1 callout resolved by cut. Four surviving entries are movement-anchored, correctly necessity-tested, and focused. The light-angle-as-elapsed-days entry at @20 remains the strongest piece. No rubric violation found under adversarial re-read.
