# Tensometer Facet Rubric

Authoring + review rubric for `facets/tensometer.md` entries. Phase 1 reviewer-tuning artifact for the shoot-v2 facet-tuning process. Authority for dramatist when authoring tensometer scalars and for the mechanic auditor when reviewing them.

Status: V2 (locked at end of Phase 1). V1 lenient form retained at the bottom for round-trip lift comparison only.

---

## What tensometer is for

Tensometer attaches a single tension scalar (1, 2, or 3) to every proto-line. It serves three jobs:

1. **Per-beat charge signal.** Records the perceptible charge of this beat as written. Used by the stitcher to bias rendering density (3-beats in full, 2-beats normal, 1-beats compressible).
2. **Cross-facet coordination signal.** Other facets gate, weight, or are expected to cluster on tens-rung. Once tensometer is locked, downstream facet-authoring conditions on it (see §"Cross-facet contract" below). Inconsistent or noisy ratings break that contract.
3. **Episode-shape guarantor.** The tensometer file across a full episode is a *curve*, not a bag of scalars. The dramatist authors the file as a structural artifact: scenes must show rise → peak → release; episodes must show act-shape. When the proto-line file lacks beats to support the needed curve, the failure is *upstream*; the dramatist flags a screen-writer kickback rather than inflate scalars to manufacture a curve. Tensometer is the structural critic's primary instrument.

Tensometer is not vibe. It is not whether the *scene* is tense. Per-beat: it is whether *this beat* carries pressure on its own face. Per-curve: it is whether the *episode escalates correctly*.

A herald walking up the road is 1. The herald stopping at the wall is 2. The herald looking over the wall and meeting Taylor's eye is 3. Same scene, three rungs — and the rise from 1 to 3 across that mini-arc is the shape the dramatist is engineering.

---

## Form

Per `schemas/facet.schema.md`:

```
<id> @<proto-line-id> <1|2|3>
```

- **1** — quiet, ambient, transitional. No on-face stakes, no reversal in motion, no body-charge.
- **2** — pressure visible. At least one of the three axes carries weight on the beat. Escalation is possible from this beat; it is *charged* but not *ruptured*.
- **3** — peak, rupture, or held-breath threshold. The beat IS the turn, or the held-against-turn moment where the next beat will commit one way or another. Multiple axes light, OR a single axis lights at peak intensity.

Form is necessary but not sufficient — a well-formed scalar that misreads the rung is still a violation.

---

## V2 rubric (locked) — three axes

A tensometer entry passes review iff its scalar **affirmatively demonstrates** the rung against at least one axis (for 2 or 3) and does not violate the rung-frequency or adjacency tests.

### 1. Stakes-visibility

What is at risk in this beat that an external observer could read off the SVO sentence?

ACCEPT signatures by rung:
- **1** — no on-face risk. Ambient ("the cold sits in the nave"), transitional ("Taylor crosses the yard"), persistent setting ("the wire hums").
- **2** — risk legible: a watch-cost ("the officer's gaze fixes on Taylor at the yard's far end"), a public exposure ("the inspector reads from the board"), a procedural commitment in motion ("the stylus marks two parallel lines beside Taylor's entry").
- **3** — risk crests: the beat IS the exposure ("the talons close on Taylor's forearm at four points"), the commit ("Taylor presses the letter forward"), or the registration of an irreversible turn ("the stylus stops on the board" — only at the moment the stop reverses prior motion).

REJECT signatures:
- Rating 2/3 because the *scene* has stakes when this *beat* doesn't carry them on its face. (Anti-pattern: ambient escalation.)
- Rating 1 on a beat that names a watching, a witnessing, or a public commitment.

### 2. Reversal-proximity

How close is this beat to a turn — a commit, an escape, a rupture, an irreversible registration?

ACCEPT signatures by rung:
- **1** — no turn near. Beat extends prior motion or sustains state.
- **2** — turn approaches: the beat is the breath before the move, the alignment that makes the next move possible, the closing distance.
- **3** — turn occurs at this beat OR the beat is the held-against-turn (the breath at peak compression, where the next beat resolves).

REJECT signatures:
- Climax bleed: rating the lead-up to a 3 also as 3. The 2 rung is for proximity; only the turn itself (or the held-breath at peak) is 3.
- Calling a continuation a turn. A continuation of established motion is 1 unless something else lights.

### 3. Body-charge

Does the beat carry physical investment — held breath, locked posture, deliberate freeze, or sudden release?

ACCEPT signatures by rung:
- **1** — no body-charge. Bodies move at neutral cost.
- **2** — body invested: a held position against pressure ("Taylor presses the shoulder harder into the wood"), a deliberate restraint ("Taylor lowers the chin a quarter-inch"), a charged stillness with named load.
- **3** — body at peak: a held position at maximum compression where the next beat resolves it, OR a sudden release after held charge ("Taylor's back leaves the wall").

REJECT signatures:
- Stillness inflation: rating "X holds the position" as 2 by default. Stillness is 1 unless the held-against-what is on the screen.
- Calling routine motion body-charged. Walking across a yard is 1 unless the yard is itself a charged space (then the scene-frame, not the beat, carries the load — facet entry stays 1).

---

## Cross-axis tests

- **The charge test.** Name what charges this beat in five words or fewer. "Officer's gaze on Taylor" → 2. "Stylus stops mid-stroke" → 3. If you can name nothing, it's 1.
- **The adjacency test.** A 3 should sit next to 2s, not 1s. A 3 surrounded by 1s is either a misrating (the lead-in should be 2) or a true sudden turn (rare; flag for review).
- **The rung-2 test.** A facet entry rated 2 must answer: what specifically is *charged* on the face of this beat? If the answer is "the scene is tense," it's 1. If the answer names a stake, a turn-proximity, or a held body, it's 2.
- **The frequency test.** Across a corpus of ~1100 proto-lines, expect roughly 60–75% 1s, 20–30% 2s, 5–10% 3s. A distribution outside that band suggests systemic miscalibration — investigate before shipping.

---

## Anti-patterns (named for the rubric)

These are the contamination patterns the writer must resist and the reviewer must call out.

1. **Ambient escalation.** Bumping environmental or transitional beats to 2 because the surrounding scene is tense. Tension lives in the scene-frame, not in every beat. Fix: the beat must carry on-face charge against at least one axis.
2. **Speech-beat default.** Auto-rating `<character> speaks to <listener>` beats as 2 or 3 because dialogue carries plot. Speaking is by itself a 1. The dialogue file may be 3-charged, but the *proto-line beat* is 1 unless something else lights (officer publicly accusing → 2; ultimatum delivered → 3).
3. **Climax bleed.** Rating the run-up to a 3 also as 3. Lead-in is 2; only the turn or the held-against-turn is 3.
4. **Plot-importance inflation.** Rating a beat 2 because the writer knows it matters narratively. Tensometer reads on-face charge, not narrative function. A quietly-load-bearing beat is still 1 if it reads quiet.
5. **Stillness inflation.** Rating "X holds Y" beats as 2 by default. Stillness is 1 unless the *what is being held against* is on screen at the same beat. "Taylor holds the head still" while alone in the dark is 1; "Taylor holds the head still" while the inspector watches is 2.
6. **Flat-field failure.** Using only 1 and 3, never 2. The 2 rung must do real work — it's the most common non-trivial rung, and skipping it produces a binary tensometer that gives the stitcher no gradient.

---

## Curve-shape rubric (episode-level)

The tensometer file as a whole must demonstrate dramatic shape. The mechanic auditor checks the curve in addition to per-beat correctness.

### Scene-level shape

Each scene (boundary marker TBD; for now: contiguous run of proto-lines under one location-state inheritance with one continuous dramatic frame) must satisfy:

- **At least one 3 OR an explicit dramatist-flagged exception** ("scene-as-respite" / "scene-as-transit"). Default expectation: every scene contains a rupture/commit/registration beat.
- **A rise to the 3.** Beats leading into a 3 should ramp through 2s, not jump from 1 directly. Direct 1→3 jumps are flagged as either misratings or true sudden-turns; either is a kickback signal.
- **A release after the 3.** A 3 followed immediately by another 3 is suspicious unless the second 3 is a *double-tap* (rare structural device). Default: 3 → 2 → 1 fall-off, OR 3 → 3 only when the second 3 reverses or commits the first.
- **No flatlining.** A scene of 30+ beats with no 2s or 3s is a scene that does no dramatic work — kickback to screen-writer.

### Episode-level shape

The full tensometer file across an episode must satisfy:

- **Act structure visible.** The cumulative or moving-window mean of the curve should show at least one major rise toward a climax. Episodes ending with their highest peak in the first third are structurally inverted — kickback.
- **Climax beat exists and is unique-or-near-unique.** The episode's structural climax should be visible as the densest cluster of 3s, not as one of many indistinct 3-clusters. If every scene peaks at the same intensity, the episode has no climax — kickback.
- **Frequency band.** Across an episode, expect roughly 60–75% 1s, 20–30% 2s, 5–10% 3s. Outside that band, investigate: too many 3s = inflation OR a structurally-overloaded episode; too few 3s = flatness OR a structurally-underloaded episode.

### When curve-shape fails

The dramatist's response to a failing curve is **not** to retune scalars. The response is:

- **Misrating fix:** if individual beats are misrated and refitting them produces the correct curve, fix the ratings.
- **Screen-writer kickback:** if the proto-line file does not contain the beats that would support the needed curve (no rupture beat in scene; no climax beat in episode; flatlined run), flag a kickback to screen-writer with specific named gaps. This is the dramatist's primary structural-intervention path.
- **Boundary flag:** if the scene boundary is wrong (the rupture happens but it's inside what looks like one continuous scene), flag a scene-boundary issue for and-wrap.

Inflating scalars to make a flat episode look escalating is the prohibited move. The cross-facet contract assumes ratings are honest.

---

## Cross-facet contract

Tensometer's downstream consumers. Once tensometer is locked, these other facets condition on it. The dramatist must assume these contracts are load-bearing when rating; the mechanic auditor must verify ratings will support them.

### Selection / density gates

- **Stitcher rendering density.** 3-beats render in full SVO + all cited facet content; 2-beats render normally; 1-beats are eligible for compression under "and" or for selection-out if narratively redundant.
- **Loudness flags.** Default fires only at tens ≥ 2. A loudness flag at tens = 1 is suspicious (either a misrated tens or a misjudged loudness) and is flagged for cross-facet consistency.
- **Metaphor flags.** Default permitted only at tens = 3 (the rare beats where figurative language earns the cost). Metaphor at tens = 1 is almost always cut; metaphor at tens = 2 must be defensible.
- **Memory flags.** Expected to cluster around tens-transitions (1→2, 2→3) and especially at tens = 3 — callbacks are most legible at peaks. Memory flags on long flat stretches of 1s without anchoring transition are flagged.

### Density expectations

- **Audience interest flags.** Expected to cluster around tens = 3 beats and on the 2-beats immediately preceding them. Persona-specific clustering is allowed; aggregate flatness across all three personas at a 3-cluster is a signal that either the rating is inflated or the scene is failing audiences.
- **Narrator interest flags.** Expected dense around tens-transitions; the POV character notices most where pressure is changing.
- **State-updates.** A tens = 3 beat without a co-cited state-update is suspicious — peaks usually change state. A state-update at tens = 1 is also suspicious — quiet beats rarely move canonical state. Both are flagged for cross-facet review (not auto-rejected; some 3-beats are pure registration without state change).
- **Location-state.** No direct gate, but loc-state entries cluster around tens-transitions (entering a new charged frame is itself a transition) — a long run of high-tens beats with no loc-state citations is a possible loc-state miss.

### What tensometer does NOT condition

- Dialogue file content. Dialogue files carry their own dramatic charge independently. A dialogue-file peak may sit on a tens = 1 proto-line beat (the SVO is "Taylor speaks to the inspector"; the *content* of the dialogue carries the heat, not the proto-line beat).
- Vibes-updates. Vibes shift on narrative pivots, which usually align with peaks but not always.

---

## Cross-rung worked examples (calibration set)

Drawn from the actual proto-line corpus. These are the calibration anchors used during Phase 1 reviewer tuning and Phase 2 writer-fork.

- `s01e01:1 the cart sits outside the timber gate` — **1.** Ambient open-establishing. No charge on face.
- `s01e01:14 taylor crosses the twelve feet of packed dirt` — **1.** Transitional motion in a charged scene-frame, but the beat itself is neutral cost.
- `s01e01:23 the officer's gaze fixes on taylor at the yard's far end` — **2.** Stakes-visibility lights (public selection); reversal-proximity lights (the gaze is the alignment before the next move).
- `s01e01:24 the stylus stops on the board` — **3.** Reversal-proximity peaks (the stop reverses prior motion); stakes-visibility peaks (the procedural turn is registered in this beat).
- `s01e01:38 taylor puts the letter into the air in front of the officer` — **3.** Body-charge peaks (deliberate exposure); reversal-proximity peaks (commit beat).
- `s01e03:25 taylor presses the shoulder harder into the wood` — **2.** Body-charge lights (held against perceived intrusion). Not 3 because the inspector hasn't yet committed to taylor's position.
- `s01e03:62 the talons close on taylor's forearm at four points` — **3.** Body-charge peaks (sudden physical lock); stakes-visibility peaks (raven on Taylor in inspector's sight is irreversible).
- `s01e06:9 the road north stays empty` — **1.** Persistence beat. Watch-cost is in the scene-frame, not in this beat.
- `s01e06:30 the smear changes shape` — **2.** Reversal-proximity lights (something turns at the lights); stakes-visibility lights (Taylor's clock starts).
- `s01e06:62 taylor's back leaves the wall` — **3.** Body-charge peaks (sudden release after sustained held position).

---

## V1 lenient form (retained for lift comparison only)

V1: ACCEPT iff the scalar is in {1, 2, 3} AND any axis is plausibly invoked at any reading. No frequency check, no adjacency check, no axis-discrimination check.

V1 exists only to produce a baseline accept-rate for round-trip comparison after writer-tuning. It is not an authoring target. Do not soften V2 toward V1 between rounds.

---

## Author / reviewer notes

- **Author:** dramatist. Two-pass authoring:
  1. **Per-beat pass.** Read the proto-line file, assign scalars, mark axis-citation per non-trivial entry (every 2 and 3; 1s only need citation if non-obvious).
  2. **Curve-shape pass.** Read the tensometer file as a curve. Check scene-level shape (rise, peak, release) and episode-level shape (act structure, climax, frequency band). Either fix misratings, flag screen-writer kickback for structural gaps, or flag scene-boundary issues. **Do not inflate scalars to manufacture shape.**
- **Reviewer:** mechanic auditor under this rubric. Per-entry verdict: CORRECT or MISRATED-{up|down}-by-N (with axis-citation). Curve-level verdict: SHAPE-OK / SHAPE-FAIL (with named scene/episode failure mode). Aggregate per-rung accuracy + curve compliance.
- **Cull:** tensometer has no per-entry cull — every proto-line gets a scalar. The "cull" equivalent is correctness of rung assignment + curve compliance.
- **Floor defense.** If the dramatist defends a 1 against a reviewer's push to 2 by citing rubric (no on-face axis lights), accept the defense. The 1 floor must hold; bumping all transitional beats to 2 destroys the gradient and breaks the cross-facet contract.
- **Ceiling defense.** If the dramatist defends a 3 as a true peak that the auditor would push down to 2, the burden is on the dramatist to name two distinct axes lighting OR a single axis at peak intensity. A 3 that survives ceiling defense should also satisfy the cross-facet contract (state-update co-cited or registration-only justified).

---

## What tensometer is not

- Not a vibe rating. Vibe is in the vibe-cloud and in the scene-frame; tensometer reads on-face charge.
- Not a plot-importance rating. The most plot-load-bearing beat may read 1 if it reads quiet.
- Not the dialogue file's tension. Dialogue carries its own weight via dialogue-file content. The proto-line beat for `<speaker> speaks to <listener>` is 1 by default.
- Not editable after cross-facet consistency. Once locked, scalars are an input to the stitcher and cannot be retuned without restarting the consistency pass.
