---
reviewer: sensory-disambiguation-pedant
facet: sensory
cycle: 2
episode: b01c02
date: 2026-05-21
verdict: revise
---

# Verdict reasoning

Cycle-1 finding: sensory:2 @22 action-verb self-charge on `lights the lamp`. Fix: relocated sensory:2 to @23 (`opens the ledger`). I re-run the disambiguation gate on the remediated file.

**sensory:1 @7 — sound: watch-press-alley-ambient -> watch-column-footfall**

Proto-line: `the city-watch passes the hook`. Unchanged from cycle-1. `passes` is bare locomotion; the column's audible texture is not in the language. Sound modality matches the natural perceptual axis. No charged word; no action-verb self-charge. PASS — unchanged from cycle-1.

**sensory:2 @23 — light: unlit-lodging-interior -> lamp-lit-tight-radius**

Proto-line: `taylor-hebert-kl-122ac opens the ledger`. The relocation moved the anchor one beat forward to avoid the `lights` action-verb self-charge. I apply the disambiguation gate to the new anchor.

Charged-word test on `opens the ledger`: `opens` is a physical manipulation verb — parting covers, separating pages. It does NOT name a light event. `Opens` is not in the action-verb self-charge class of `lights / ignites / extinguishes / catches`. The proto-line is bare on the light modality. The cycle-1 failure mode — action-verb self-charge — does not persist at @23. PASS on charged-word gate.

However the disambiguation gate has a second requirement: the fire must be on the inflection beat, not on a beat within the settled state. The rubric states: "A flag fires on the change (silence → rhythm; sun → blistering glare)." The inflection-not-sustained test: is @23 the change-point, or the first beat of the sustained post-change state?

The lamp is lit at @22 (`lights the lamp`). loc-state:11 @22 establishes the lamp newly lit; the conditions note on loc-state:11 explicitly describes the pre-@22 darkness as "interior-darkness baseline before @22." By @23 the lamp is already on. The room is already lamp-lit-tight-radius at @23. The old-state field claims `unlit-lodging-interior` as the perceptual state at @23 — but that state ended at @22. At @23 the audience is inside the lit environment, not at the moment the lit environment began.

The sensory delta describes the transition dark → lit. The transition happened at @22. At @23 the transition is over; `opens the ledger` is the first action in the settled lamp-lit state. A fire at @23 is a fire on the first beat of the sustained new level, not the inflection beat. The rubric's inflection-not-sustained test refuses exactly this: "The flag fires on the inflection beat only. Sustained sensory state belongs in location-state."

The fix-log's own language confirms this: "anchoring here at @23, the first bone worked under the stable lit state." The phrase "stable lit state" is loc-state language, not sensory-inflection language. A fire on the first bone of a stable state is a sustained-baseline fire, which belongs in loc-state, not in sensory-flags.

The relocation resolved the action-verb self-charge failure and introduced an inflection-not-at-inflection-beat failure. The fire at @23 describes a transition that has already closed. FAIL.

Correct paths: (a) There is no clean proto-line anchor for a light:up fire that avoids both self-charge (@22 is self-charged) and lagged-inflection (@23 onwards are settled state). The architectural problem is that `lights the lamp` IS the inflection and IS action-verb self-charged — the inflection and the self-charge are the same event. No non-self-charged proxy proto-line exists at the transition moment because the transition moment only exists as `lights the lamp`. The entry cannot be saved by relocation. (b) Cut the entry and acknowledge modality-floor consequences.

Both entries on disambiguation: sensory:1 PASS, sensory:2 FAIL. File cannot pass my axis.

# Entry-level callouts

`[sensory:2] @23 — "opens the ledger" is bare on light (action-verb self-charge resolved). But the delta (unlit-lodging-interior -> lamp-lit-tight-radius) describes the @22 transition; at @23 the lamp is already on. Fire lands on the first beat of the settled state, not the inflection beat. Inflection-not-at-inflection-beat failure — the relocation traded self-charge for lagged-anchor.`

# Convergence trace

- sensory:2 @22 action-verb self-charge (cycle-1): resolved. `opens` does not self-charge light. That finding does not persist.
- sensory:2 @23 lagged-anchor: new finding, introduced by the relocation. Not a cycle-1 auditor finding; the mechanical scan does not check whether the delta's described transition matches the perceptual state at the anchor beat. The inflection-not-sustained test (rubric §Curve-shape / §Cross-axis tests) is the governing clause: "The flag fires on the inflection beat only." The seam is a disambiguation-gate concern because it touches the same structural question as the action-verb self-charge note: whether the proto-line's perceptual moment matches the flag's claimed inflection.
- Fix-log item 8b language ("the first bone worked under the stable lit state") inadvertently names the failure: a stable-state beat is not an inflection beat. The rubric's loc-state-vs-sensory boundary (loc-state = sustained level; sensory = inflection delta) makes the stable-state anchoring a cross-boundary violation.
- Old-state-reader cycle-2 verdict notes "timing-note concern" but does not call it a failure, correctly staying within old-state-lineage scope. The lineage-correctness that reviewer found does not cure the inflection-beat problem, which is this reviewer's axis.
- Modality-floor consequence: if sensory:2 is cut, the file holds 1 entry on 1 modality (sound only). The modality-floor (>=2) breaks. This is the modality-coverage specialist's blocking concern, but I name it because the cut is the only clean resolution on my axis.
