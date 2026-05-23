# Location-State Facet Rubric

Authoring + review rubric for `facets/location-state.md` entries. Phase 1 reviewer-tuning artifact for the shoot-v2 facet-tuning process. Authority for studio when authoring location-state entries and for audience when reviewing them.

Status: V2 (locked at end of Phase 1). V1 lenient form retained below for round-trip lift comparison only.

---

## What location-state is for

Location-state decorates proto-lines with environmental fact **only when location is what makes a move legible**. It is not scene-painting. It is not ambient flavor. It is not the "set" the actors stand on — that's the location card's job. Location-state fires at the proto-line where an actor's (or salient object's) movement, positioning, or perceptible action *turns on* something the location supplies: line of sight, foot traction, sound-cover, distance, available cover, who is visible to whom, what the move costs the body.

A herald at the wall earns an entry. A cart by the wall does not.

The default for any anchor proto-line is *no entry*. Sparse by design. The corpus, after rubric application, should be visibly thin — most beats render in inherited environment from the most recent cited entry, no new state.

---

## Form

Per `schemas/facet.schema.md`:

```
<id> @<proto-line-id> <location-slug> | <time> | <weather> | <conditions> | <one-clause sensory note>
```

- **`<location-slug>`** — slug of an authored location card (or `oc-…` for project-original).
- **`<time>`** — predawn / dawn / morning / midday / afternoon / dusk / night / specific clock if the world supports it.
- **`<weather>`** — one word or short phrase. `clear`, `wind-cold`, `rain-recent`, `frost`. `none` is a valid value.
- **`<conditions>`** — comma-separated active conditions affecting interaction at this beat. e.g. `door-shut, lantern-on-far-wall, mud-recent`. Empty allowed.
- **`<one-clause sensory note>`** — a single perceptible thing the move turns on. **The most load-bearing field.** This is where the rubric's interestingness/focus axis lives.

Form is necessary but not sufficient — a well-formed entry that fires on a non-movement beat is still a violation.

---

## V2 rubric (locked) — three axes

A location-state entry passes review iff it **affirmatively demonstrates** all three of necessity, interestingness, and frugality, AND does not violate any of them.

### 1. Necessity

The anchor proto-line is a movement, positioning, or physical-action beat whose legibility depends on a location fact. Strip the entry: if the proto-line still resolves cleanly without it, the entry is parasitic.

ACCEPT signatures:
- Anchor verb is a transitional or positioning verb (`crosses`, `enters`, `steps to`, `passes through`, `reaches`, `stops at`, `holds the line of sight to`).
- The one-clause sensory note names a fact the verb requires (a far-end-of-yard distance, a threshold, a piece of cover, a path through mud, a held door).
- A non-movement beat earns an entry only if it is the *first* beat in a new location-and-moment (entry serves as place-anchor for subsequent inherited beats).

REJECT signatures:
- Anchor is a stillness/hold beat (`X holds Y configuration`, `X stays`, `the cart sits`) — these are location-card content, not loc-state.
- **Anchor is a dexterity-stillness verb** (`threads`, `sews`, `knots`, `stitches`, `pours`, `weighs`, `mends`, `splices`, `picks`, `wipes`, `folds`) — hand-work done in-place. The character is not moving *through* the location; they are working *in it*. Dexterity verbs do not license a loc-state fire unless the fire is first-beat-in-new-location or carries a valid `continuity-from <prior-loc-state-id>:` token under the transition-run continuity license. (URI-FACETS-CYCLE-1, 2026-05-19 — promoted from audience-gate cycle-1 attack on b01c01 loc-state:3 @11 "threads the needle": both dark-fantasy-reader and worm-canon-pedant independently flagged the anchor-verb-licensing seam the mechanical scan could not see.)
- Anchor is a pure dialogue beat (`X speaks to Y`) and no positioning is in question — speaking does not need environment unless the speaking *is* the move (e.g. shouted across a yard, whispered behind a hand).
- Anchor is interiority pushed into physical SVO (perception-feed beats per Phase 0 note #1) — those cite narrator/feel, not loc-state.
- Anchor is environmental persistence (Phase 0 note #10) — persistence is location-card content; loc-state fires on change, not on hold.

### 2. Interestingness / focus selection

The one-clause sensory note must point at *the specific perceptible thing in this location that the move turns on* — not paint the room, not list ambient features, not summarize the location card.

ACCEPT signatures:
- One concrete focus-element named: *the herald at the wall*, *the gatehouse lantern half a league off*, *the rushes underfoot*, *the door-shadow on the threshold*.
- The element is selected — every other thing in the location is implicitly omitted.
- The element is *new* information at this anchor (not inherited from the prior cited loc-state).

REJECT signatures:
- Sensory sweep: more than one focus-element in the clause.
- Generic atmosphere ("the yard is cold," "morning light," "mud everywhere") with no specific element.
- Re-naming a feature already established by location card or prior loc-state entry — no incremental selection.
- Adjective-heavy mood-painting that does not name a perceptible thing.

### 3. Frugality

One loc-state entry licenses every subsequent proto-line in the same location-and-moment until the move changes. Re-citing the same environment without state-change is a violation.

ACCEPT signatures:
- Entry is the first cited loc-state in this location-and-moment, OR
- Entry marks a state-change since the last cited loc-state (door opens, light shifts, weather changes, new entrant changes the focus-element, time advances meaningfully, an active condition resolves or activates).

REJECT signatures:
- Repeats the prior cited loc-state with cosmetic variation.
- Fires on every movement beat in a sustained scene rather than at the moments the environment turns over.
- Decorates a beat that is already covered by inherited loc-state.

---

## Cross-axis tests

- **The strip test.** Remove the entry and read the anchor proto-line in inherited environment. If it resolves cleanly, REJECT.
- **The pointing test.** Ask: what is this entry pointing at? If you can name one perceptible focus-element in five words or fewer, ACCEPT on axis 2. If the answer is a list or a mood, REJECT.
- **The previous-entry test.** Compare against the last accepted loc-state in the same scene. If this entry would render identically in inherited state, REJECT on axis 3.
- **The herald/cart test (heuristic).** A *cart* sitting by a wall is location-card content; it does not change as actors move. A *herald* at a wall is loc-state — the herald's positioning at the wall is what the next move turns on. When in doubt: who or what is doing something perceptible *because* of the location? That's the focus-element.

---

## Anti-patterns (named for the rubric)

These are the contamination patterns the active project's prior `STUDIO:` bullets exhibit; the writer must resist and the reviewer must call them out.

1. **Set-dressing sweep.** Dropping every salient item visible at scene-open into one entry. Symptom: multi-clause sensory note. Fix: one focus-element only; the rest is location-card.
2. **Mood-painting on stillness.** "The yard holds the silence." "The cooling light." Atmosphere standing in for a perceptible focus. Fix: delete the entry; atmospherics with no perceptible focus-element are not authored in this pipeline.
3. **Persistence-as-state.** "The granary holds its three-week shape." Persistence is not state-change; the location card already says what shape the granary holds. Fix: delete the entry; persistence-of-state is location-card content, not a facet.
4. **Inherited re-naming.** Re-citing the sept-yard at every Taylor beat in the sept-yard. Fix: cite once on entry; rely on inheritance until the environment turns over.
5. **Plan-bullet residue.** Direct conversion of shoot-v1 STUDIO bullets that summarized a whole scene's setting. Fix: discard most; keep only the specific perceptible focus-elements that turn on individual movement beats.
6. **Time/weather padding.** Filling the time and weather fields with detail that does no work in the conditions or the sensory note. Fix: time/weather only when the move depends on them (predawn → no light; rain-recent → muddy traction; wind-cold → carries sound).

---

## Transition-run continuity license (URI-SCENE-RHYTHM, 2026-05-13)

The three-axis rubric above is calibrated for state-change beats (movement, threshold, environment-turnover). It correctly refuses entries on flat-low zone bones (scene-map `rhythm-shape: flat-low` or `fusion-eligible-runs` membership) that don't change state. But s01e02 dogfoods (breath-pass, organic-render-p4, scene-window) all identified the same gap: transition runs render facet-bare, and the stitcher has nothing to weave through them. The bones are correctly atomic; the renders feel metronomic because no atmospheric tissue persists across the run.

The transition-run continuity license is a narrow additive — NOT a relaxation of the necessity / interestingness / frugality axes. It fires for ONE specific structural slot per fusion-eligible-run:

**When the license fires:**
- The anchor bone is inside a scene-map `fusion-eligible-runs` range (3+ consecutive flat-low bones, no peak-shadow), AND
- The scene's `rhythm-shape` is `flat-low`, `resolving`, or `release-only` (transition postures), AND
- A prior scene established a sensory baseline (a loc-state entry citing an environment) that the audience can register as continuing into this run.

**What the license permits:** ONE continuity-carry loc-state entry per fusion-eligible-run, anchored to the run's first bone. Entry shape:

```
<id> @<bone-id> <location-slug> | <time> | <weather> | <conditions> | continuity-from <prior-loc-state-id>: <one-clause carry-note>
```

The `continuity-from` token names the prior loc-state entry whose baseline is being carried. The `<one-clause carry-note>` names what specifically persists — usually a sensory thread (alley-sound through the window, wind-off-the-road carrying, relay-register active) that was established earlier and remains audible through the transition run.

**What the license does NOT permit:**
- New state-change content (use a normal loc-state entry at the change beat).
- Inherited re-naming (Anti-pattern 4 still applies in spirit; the carry-note must not just repeat the prior loc-state's sensory note verbatim).
- Multiple carry-notes per run (one is the entire license).
- Continuity carry across `rhythm-shape: rising` / `rising-to-peak` / `peak-and-release` / `double-peak` scenes (those have rising-rhythm momentum that absorbs facet-bare bones differently; the stitcher should not weave continuity through an approach).

**Stitcher consumption.** The scene-window fork reads the `continuity-from` entry and folds the carry-note as connective tissue across the run — em-dash continuation, `still` connective adverb, participial-phrase carry-forward. The render is NOT a standalone sentence; it is tissue that lets the run breathe. Worked example from s01e02 scene-D (bones @41–@49, six of seven facet-bare): `"The flies still had the carter and the wind."` The `still` is the carry-marker; the relay-register established in scene-C is the persisting baseline being carried into scene-D's flat-low run.

**Auditor enforcement.** Continuity-carry entry whose `<bone-id>` is NOT inside a fusion-eligible-run → HARD `FAULT-LOC-STATE-CONTINUITY-MISPLACED`. Entry whose `<prior-loc-state-id>` does not resolve to an earlier loc-state entry in the file → HARD `FAULT-LOC-STATE-CONTINUITY-DANGLING`. Multiple continuity-carry entries on the same fusion-eligible-run → HARD `FAULT-LOC-STATE-CONTINUITY-OVERPACK`. Entry whose carry-note duplicates the prior loc-state's sensory note verbatim → SIGNAL `WARN-LOC-STATE-CONTINUITY-NO-INCREMENT`.

---

## V1 lenient form (retained for lift comparison only)

V1: ACCEPT iff the entry does not violate the form (well-formed slug, time, weather, conditions, sensory note) AND the anchor proto-line is plausibly an environment beat. No necessity test, no interestingness test, no frugality test.

V1 exists only to produce a baseline accept-rate for round-trip comparison after writer-tuning. It is not an authoring target. Do not soften V2 toward V1 between rounds.

---

## Author / reviewer notes

- **Author:** studio. Studio reads the proto-line file, identifies anchors that pass the necessity test, drafts entries.
- **Reviewer:** audience (3 personas) under this rubric. Per-persona verdict, aggregated.
- **Cull:** delete-only after authoring, before cross-facet consistency. The cull pass is the second enforcement of frugality — entries that survive authoring but fail axis 3 in batch context get cut.
- **Floor defense.** If the audience pushes back on a rejection because the entry genuinely earns it under one of the three axes, accept the pushback. A rubric that rejects everything is as broken as one that accepts everything. Plumm-style floor defense is signal.
