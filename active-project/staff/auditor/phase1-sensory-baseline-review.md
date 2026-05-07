# Phase 1 — Sensory-Flags Baseline Review

Mechanic auditor review of `design/shoot-v2/phase1-sensory-baseline-naive.md` (12 entries, rubric-blind). Two passes: V1 lenient (form-only) + V2 strict (full V1 rubric per `design/shoot-v2/rubric-sensory.md`).

---

## V1 lenient pass — form-only

ACCEPT iff entry is form-correct (well-formed: `<id> @<proto-line-id> <up|down|spike|drop> <description>`), anchors to a real proto-line, names a perceptual modality plausibly. No disambiguation check, no magnitude check, no inflection-vs-sustained check, no audience-side check, no curve-shape check.

| # | Beat | Tag | Form OK | Anchor real | Modality plausible | V1 verdict |
|---|---|---|---|---|---|---|
| 1 | @13 | up | yes | yes | yes (sound) | ACCEPT |
| 2 | @21 | up | yes | yes | yes (sound) | ACCEPT |
| 3 | @24 | drop | yes | yes | yes (sound) | ACCEPT |
| 4 | @30 | up | yes | yes | yes (sound) | ACCEPT |
| 5 | @38 | spike | yes | yes | yes (sound — silence-as-spike, contested but plausible) | ACCEPT |
| 6 | @41 | spike | yes | yes | yes (sound) | ACCEPT |
| 7 | @47 | up | yes | yes | yes (sound) | ACCEPT |
| 8 | @57 | drop | yes | yes | yes (sound) | ACCEPT |
| 9 | @58 | up | yes | yes | yes (sound) | ACCEPT |
| 10 | @64 | spike | yes | yes | yes (sound) | ACCEPT |
| 11 | @67 | spike | yes | yes | yes (sound) | ACCEPT |
| 12 | @69 | drop | yes | yes | yes (tactile/pressure — schema says volume but description is tremor; lenient pass admits) | ACCEPT |

**V1 lenient: 12/12 = 100% accept.** Form is easy to satisfy. The lenient pass admits all entries because each has a well-formed delta and an anchor; substantive failures live in the V2 axes.

---

## V2 strict pass — full V1 rubric

ACCEPT iff entry clears all four axes (modality-inflection, disambiguation-discipline, magnitude-sufficiency, audience-side-perceptibility) and no anti-pattern fires. Per the locked rubric's two defensibility questions: would the audience know the difference WITHOUT the flag? AND is the difference LARGE ENOUGH to justify a flag?

| # | Beat | Description | Q1 (bare?) | Q2 (large?) | Sustained? | Audience-side? | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | @13 | officer's voice rises over yard murmur | bare ("speaks") ✓ | large ✓ | inflection ✓ | yes ✓ | **CORRECT** |
| 2 | @21 | officer continues addressing each ward | bare ("speaks") | large | **SUSTAINED** ✗ (officer-command-voice already established at @13) | yes | **INCORRECT — sustained-as-inflection** (anti-pattern #2) |
| 3 | @24 | stylus stops abruptly on the board | bare ("stops") ✓ | large ✓ | inflection ✓ | yes ✓ | **CORRECT** |
| 4 | @30 | stylus resumes on taylor's name | bare ("moves") ✓ | large ✓ | inflection ✓ | yes ✓ | **CORRECT** (note: description uses "resumes" but proto-line is "moves" — author description leak, but the keyed word is the proto-line "moves" which is bare) |
| 5 | @38 | the moment of the letter pressed forward goes quiet | NO bare-word in proto-line for sound | **NO** — this is "silence-as-spike" reading the dramatic peak; magnitude-sufficiency fails (no actual sound event; ambient quiet of a held moment is sustained, not inflection); also density-on-charged-tens=3 | sustained / interior | interior-only | **INCORRECT — no-modality-fire / density-on-charged-tens / interior-only** |
| 6 | @41 | wax seal cracks under officer's thumb | bare ("breaks at the crease") ✓ | large ✓ | inflection ✓ (transient discrete) | yes ✓ | **CORRECT** |
| 7 | @47 | officer's voice returns dictating | "speaks" bare | large | **SUSTAINED** ✗ (officer-command-voice resumes after pause but is the same established register; not new inflection) | yes | **INCORRECT — sustained-as-inflection** |
| 8 | @57 | edric's footsteps recede through doorway | bare ("steps") | **SUB-THRESHOLD** ✗ (footstep-receding is fine-grain; not register-shifting at audience-experiential scale) | inflection-leaning | yes-marginally | **INCORRECT — sub-threshold magnitude** (Q2 fail) |
| 9 | @58 | stylus resumes its rhythm on the board | proto-line word "resumes" — **CHARGED-LEANING** (resumes carries re-onset for audience without flag) | large | inflection | yes | **INCORRECT — charged-word redundancy** (Q1 fail; "resumes" partially self-carries) |
| 10 | @64 | two parallel lines marked beside entry | bare ("marks") | **SUB-THRESHOLD** ✗ (stylus-marking audible event is fine-grain; not register-shifting at audience-experiential scale; the proto-line's force is in the *visual* mark, not in any audible event) | inflection | sub-threshold | **INCORRECT — sub-threshold magnitude** (Q2 fail) + density-on-charged-tens=3 |
| 11 | @67 | officer's foot moves toward the horse | bare ("lifts") | **SUB-THRESHOLD** ✗ (foot-movement is not a sound event; no perceptible inflection) | no-inflection | no | **INCORRECT — no-modality-fire / sub-threshold** |
| 12 | @69 | wheel-tremor leaves verge-beetles east | bare ("leaves") | large-leaning | inflection-leaning | **NO** — fauna-feed-extension; audience cannot perceive ground-tremor through Taylor's beetle-sensorium | **INCORRECT — fauna-feed-extension** (anti-pattern #3) |

**V2 strict: 4/12 = 33.3% accept.**

CORRECT: #1 (@13), #3 (@24), #4 (@30), #6 (@41).
INCORRECT: #2, #5, #7, #8, #9, #10, #11, #12 (8 fails).

---

## Missed-fires audit (refusals to add)

The naive baseline did not consider non-sound modalities (correctly; the schema was volume-only). Under the V1 rubric (post-rename multi-modal), the auditor checks whether non-sound inflections were missed:

- **@72 (taylor steps on the stone) — MISSED-FIRE candidate.** Tactile:up — dirt-yielding → stone-firm. Bare verb ("steps"); large enough to register experientially (firmness change); audience-perceptible. The naive baseline skipped because schema was volume-only. Under multi-modal V1 rubric this is a legitimate fire candidate. **MISSED.**
- **No other strong missed-fire candidates** in s01e01. Light, smell, thermal, humidity, pressure beats either fail bare-not-charged (@73 light/shadow charged), fail magnitude (no sub-threshold thermal/humidity inflections in the episode), or fail audience-side (the wheel-tremor at @69 already-considered).

---

## Systemic faults (the contamination patterns the V2 strict review surfaces)

Six failure modes named in the corpus' predicted-naive-failure-modes section, all observed:

1. **Sustained-as-inflection (anti-pattern #2).** #2 (@21), #7 (@47). Naive author fires on every officer-speech beat; the officer-command-voice was established at @13 and is sustained across @13-22 + @26-32 + @47+. Subsequent fires are saturated, not inflection.

2. **Sub-threshold magnitude (anti-pattern #5).** #8 (@57), #10 (@64), #11 (@67). Naive author fires on small audible events that are real-but-not-register-shifting: footsteps receding, stylus-marking texture, foot lifting toward horse. The Q2 magnitude gate strips all three.

3. **Density-on-charged-tens (anti-pattern #12).** #5 (@38), #10 (@64). Naive author fires on dramatic peak-tens beats because they read as charged; sensory-flags is independent of tensometer (correlative not gating), and many high-tens beats have no perceptual modality change. @38 is body-commit (no sound event); @64 is bureaucratic registration (sub-threshold sound).

4. **Fauna-feed-extension (anti-pattern #3).** #12 (@69). Audience cannot perceive ground-tremor through Taylor's beetle-sensorium; this is interior-extended-range, not audience-side perceptibility.

5. **Charged-word redundancy (anti-pattern #1, leaning).** #9 (@58). The proto-line word "resumes" partly self-carries the re-onset for the audience; flagging is borderline-redundant.

6. **No-modality-fire (anti-pattern, REJECT signature on Axis 1).** #5 (@38), #11 (@67). No actual perceptual modality undergoes inflection; the fires are dramatic-charge-driven, not perception-driven.

Modality-monoculture (anti-pattern #6) does NOT count against the naive baseline because the schema-blind author was working on the volume-only definition. Post-rename, file-shape audit would flag sound-only as monoculturing — the corrective is the missed-fire audit (add @72 tactile) which is rubric-tuning territory, not naive-baseline territory.

---

## Defended-floor check

V2 strict rejects 8 of 12 entries. The audience would push back if the rubric were over-rejecting; checking each rejection:

- **#2 (@21), #7 (@47):** clearly sustained; officer-command-voice already at register. Defended floor — these belong in loc-state baseline (which already holds officer-presence), not in sensory-flags. Reject sustained.
- **#5 (@38), #11 (@67):** clearly no-modality-fire. The dramatic charge is bureaucratic-confrontational, not sensory. Reject.
- **#8 (@57), #10 (@64), #11 (@67):** Q2 magnitude gate. The user's pre-rubric framing supports these rejections: "is the difference LARGE ENOUGH to justify a flag?" — sub-threshold events are exactly what the gate strips.
- **#9 (@58):** charged-word redundancy on "resumes". Borderline; the user's pre-rubric framing supports rejection ("the word carries the weight on its own" applies to "resumes" at lower intensity than "thunder" but in same family).
- **#12 (@69):** clearly fauna-feed-extension. The user's pre-Phase-0 framing names this exact pattern as the anti-pattern.

Floor defended. The rubric is not over-rejecting; the naive baseline is genuinely naive on the disambiguation-not-redundancy and magnitude-sufficiency axes.

---

## Lift target

V2 strict baseline: **4/12 = 33.3%** (the baseline-to-beat for Phase 2).

Comparable to prior runs:

| Facet | Baseline V2 | Final | Lift |
|---|---|---|---|
| dialogue | 40% | 100% | +60pp |
| loc-state | 53.8% | 100% | +46.2pp |
| tensometer | 50.6% | 100% | +49.4pp |
| narrator-interest | 22.2% | 100% | +77.8pp |
| state-updates | 6.7% | 100% | +93.3pp |
| memory-flags | 19.0% | 100% | +81.0pp |
| **sensory (baseline)** | **33.3%** | **TBD** | TBD |

Sensory's 33.3% baseline is the highest yet — naive-author hits 4 correct fires (@13, @24, @30, @41) on first try because the disambiguation-discipline and inflection-not-sustained tests, while load-bearing, do not fully prevent the schema-only writer from landing on the strongest fires by sound-following. The contamination concentrates at the sub-threshold / sustained / fauna-feed edges, not at the obvious-fire core.

Phase 2 expectation: writer-fork rubric-aware lift to ~85-100%, with the new tactile-modality fire (@72) added for modality-coverage.

---

## V1 rubric: defended-floor and locked

Per `design/shoot-v2/facet-tuning-process.md` Phase 1 step 4: **lock the rubric**.

V1 rubric `design/shoot-v2/rubric-sensory.md` LOCKED at end of Phase 1. Four axes (modality-inflection, disambiguation-discipline, magnitude-sufficiency, audience-side-perceptibility); two defensibility questions (Q1 audience-without-flag; Q2 magnitude-large-enough); 13 anti-patterns; per-scene cap ≤3; sparsity 3-6%; modality-coverage ≥2; cross-facet contract independent of tensometer (correlative-not-gating), independent of NI/memory-flags/state-updates, dependent on loc-state for old-state baseline.

Do not soften V2 toward V1 between rounds. Phase 2 writer-fork is rubric-aware and rubric-locked.
