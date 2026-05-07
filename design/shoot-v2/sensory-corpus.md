# Sensory-Flags Corpus — s01e01

Phase 0 corpus selection for the **sensory-flags** facet (working name; was "loudness flags" in `schemas/facet.schema.md`; rename pending). Stratifies s01e01 (77 proto-lines) by candidate modality × proto-line-word-charge × tens-zone (correlative, not gating). All entries below are *candidates*, not pre-decided fires.

Authority: `cards/locations/*` for environment baselines; `active-project/staff/studio/*` for studio's recorded sensory state; `active-project/theater/facets/location-state.md` (locked) for per-beat environmental frame; the user's pre-Phase-0 framing on the disambiguation-not-redundancy gate.

This facet is **studio-authored**, **delta-shaped** (`<modality>: <old> -> <new>`), and **independent of tensometer** (sensory inflections may correlate with high tens but do not gate on it). The facet's licensing function is to *separate bare proto-line language from its charged variant where the audience needs the flag to land the perception*. A flag is not redundant intensity-restatement of language that already self-carries weight; it is the disambiguator that says "this bare verb names a perceptual inflection the surrounding text does not surface."

---

## Stratification axes

- **Modality** (sound / light / smell / thermal / humidity / pressure / tactile).
- **Proto-line-word-charge** (BARE = the proto-line uses a generic noun/verb that does not self-carry the perceptual intensity; CHARGED = the proto-line uses a word that self-carries — "thunder", "shadow", "stench" — flag would be redundant).
- **Tens-zone** (1 / 2 / 3) — correlative observation only. Sensory inflections may fire in any zone; high-tens beats often correlate with sensory shocks (rupture, peak), but tens=1 environmental beats also carry sensory inflections (a sudden chill in an idle moment).
- **Inflection class** (CHANGE = perceptual delta; SUSTAINED = ambient continuous level — sustained sensory state belongs in `location-state.md` § sensory note or § conditions, NOT in sensory-flags).

---

## Strong candidates (high-priority for FIRE)

### CAND-1 — @13 — sound:up — officer's first command voice

- **Proto-line:** *the officer speaks to the yard*
- **Tens:** 1.
- **Modality:** sound.
- **Tag candidate:** `up` (sustained increase from ambient yard murmur to command-voice register).
- **Bare/charged:** **BARE.** "speaks" carries no volume signature. The yard had been at ambient murmur (clerk dictating, footfalls, beetles). The officer's command-voice is a sustained sound:up from that baseline.
- **Delta:** `sound: yard-ambient-murmur -> officer-command-voice`
- **Audience-perceptibility:** universally legible once flagged; the bare verb does not surface it.
- **Multi-justification:** modality identified + tag correct + bare-not-charged + audience-perceptible + inflection-not-sustained (the establishment of command voice is the inflection beat; subsequent officer-speech beats are sustained).

### CAND-2 — @24 — sound:drop — stylus-rhythm rupture

- **Proto-line:** *the stylus stops on the board*
- **Tens:** 3 (rupture peak).
- **Modality:** sound.
- **Tag candidate:** `drop` (transient absence — the rhythm stops; this beat marks the silence-cut, not a sustained quiet that follows).
- **Bare/charged:** **BARE.** "stops" names the action of stopping; the audible rhythm-break (stylus-on-wax-rhythm → silence) is not in the verb. The audience needs the flag to register the perceptual event the verb describes mechanically.
- **Delta:** `sound: stylus-on-wax-rhythm -> silence`
- **Audience-perceptibility:** universally legible once flagged.
- **Multi-justification:** all five gates clear. Anchor-expected per locked tensometer cross-facet note ("Loudness-flag author: @24 stylus-stop perception").
- **Note:** even though sensory-flags is independent of tensometer, the @24 anchor expectation in the locked tens file remains — this is correlative inheritance, not gating inheritance.

### CAND-3 — @30 — sound:up — stylus-rhythm resumes on Taylor's name

- **Proto-line:** *the stylus moves on taylor's name*
- **Tens:** 2.
- **Modality:** sound.
- **Tag candidate:** `up` (rhythm returns from silence; sustained re-onset).
- **Bare/charged:** **BARE.** "moves" carries no audible rhythm signature; the resumption-of-marking is the perceptual inflection.
- **Delta:** `sound: silence -> stylus-on-wax-rhythm`
- **Audience-perceptibility:** legible once flagged; paired-event with @24's drop.
- **Multi-justification:** all gates clear.

### CAND-4 — @41 — sound:spike — seal-break crack

- **Proto-line:** *the seal breaks at the crease under his thumb*
- **Tens:** 1 (release-zone after @38-39 cluster).
- **Modality:** sound.
- **Tag candidate:** `spike` (transient discrete loud event — the wax cracks).
- **Bare/charged:** **BARE-LEANING.** "breaks at the crease under his thumb" describes the mechanical action; the small-but-discrete audible crack is not foregrounded by the language. The seal-as-ritual-object carries some sound resonance for source-fluent readers, but the proto-line foregrounds tactile mechanism, not sound.
- **Delta:** `sound: yard-quiet -> wax-crack`
- **Audience-perceptibility:** legible once flagged.
- **Multi-justification:** all gates clear.

---

## Mid-priority candidates (defensible FIRE; depends on file-level coverage)

### CAND-5 — @58 — sound:up — stylus resumes after Edric retreat

- **Proto-line:** *the stylus resumes on the board*
- **Tens:** 1.
- **Modality:** sound.
- **Tag candidate:** `up`.
- **Bare/charged:** **CONTESTED.** "resumes" carries some auditory weight (re-onset implies prior absence). Borderline.
- **Possible delta:** `sound: edric-retreat-pause -> stylus-on-wax-rhythm`
- **Default:** REFUSE on bare-not-charged grounds — "resumes" already carries the rhythmic re-onset for the audience without flagging. Fire only if file-level coverage is otherwise thin and the @30/@58 paired-events both deserve flags as a structural register.
- **If accepted:** would create a sound-modality-saturation file (4 of 4 fires sound). See modality-coverage health-check.

### CAND-6 — @72 — tactile:up — footing dirt-to-stone

- **Proto-line:** *taylor steps on the stone*
- **Tens:** 1 (episode-close).
- **Modality:** tactile.
- **Tag candidate:** `up` (sustained firmness increase; dirt → stone underfoot).
- **Bare/charged:** **CONTESTED.** "stone" itself is bare; the contrast against preceding "dirt" (@71) is in the proto-line *file* but not in any single proto-line's verb. The tactile shift (give → no-give underfoot) is not surfaced by either verb. The flag would specify which sensory dimension changes (firmness, sound-of-step, possibly thermal if stone-cool).
- **Possible delta:** `tactile: dirt-yielding -> stone-firm`
- **Default:** ACCEPT contingent on cross-modal coverage. This is the file's strongest non-sound candidate. Drops if file-shape audit demands sound-only coverage (rejected in favor of modality-diversity discipline).
- **Multi-justification:** modality identified + tag correct + bare-not-charged + audience-perceptible-once-flagged + inflection-not-sustained.

---

## Calibration refusals (high-priority for REFUSAL)

### REF-1 — @73 — light:down — sun-to-shadow self-carried by "shadow"

- **Proto-line:** *taylor steps into the shadow of the frame*
- **Tens:** 1.
- **Modality candidate:** light.
- **Tag candidate:** `down` (sun → shadow).
- **Bare/charged:** **CHARGED.** The word "shadow" self-carries the light-down. Adding a sensory-flag here would be redundant intensity-restatement — the audience already perceives the dimming from "shadow". This is the user's "thunder is booming loud" exemplar transposed to vision: the noun does the work; flagging is redundant.
- **Refusal-CORRECT.** Calibration anchor for the disambiguation-not-redundancy gate.

### REF-2 — @38 — peak commit; no sensory inflection

- **Proto-line:** *taylor puts the letter into the air in front of the officer*
- **Tens:** 3 (climax peak).
- **Modality candidate:** none plausibly active.
- **Why refuse:** body-commit beat; no perceptual modality changes; the charge is bureaucratic-confrontational, not sensory. Refusal-CORRECT on the no-modality-active test.

### REF-3 — @64 — stylus marks; perceptibility too small

- **Proto-line:** *the stylus marks two parallel lines beside taylor's entry*
- **Tens:** 3 (irreversible registration peak).
- **Modality candidate:** sound (the marking has small audible texture).
- **Tag candidate:** `spike` × 2 (two parallel marks).
- **Why refuse:** the sound of stylus-on-wax marking is not a perceptual inflection at audience-scale — it is continuous fine-grain texture beneath the bureaucratic registration. The proto-line's force is in the *marks* (visual, permanent record) not in any audible spike. Per the locked tensometer cross-facet note, @64 is a "stylus-mark, smaller volume-event" — but the volume-event is small enough that audience-perceptibility doubts are real. **Default: REFUSE.** If the locked file's expectation is structurally load-bearing for downstream stitching, revisit at Phase 4.

### REF-4 — @11 — officer through gate; no perceptual inflection cued

- **Proto-line:** *the officer comes through the gate*
- **Tens:** 1.
- **Modality candidate:** sound (footfalls, hinge) or light (gate-as-shade-transition) — neither cued by the proto-line.
- **Why refuse:** the proto-line foregrounds entry-as-event, not perceptual inflection. No bare-language gap that a flag would fill. Refusal-CORRECT.

### REF-5 — @69 — wheel-tremor leaves verge-beetles east

- **Proto-line:** *the wheel-tremor leaves the verge-beetles east*
- **Tens:** 1.
- **Modality candidate:** tactile/pressure (ground-vibration delta).
- **Why refuse:** the perception is fauna-feed-interior — Taylor's faculty registers the wheel-tremor through the beetles' response; the audience does not have access to the ground-vibration as an audience-side perceptual event. Per the user's pre-Phase-0 framing: fires must be where the *audience* perceives the inflection, not where the narrator's faculty extends her range to perceive it. Refusal-CORRECT on the audience-side perceptibility gate.

### REF-6 — @50 — Taylor turns to Mira; no inflection

- **Proto-line:** *taylor turns to mira*
- **Tens:** 1.
- **Modality candidate:** none.
- **Why refuse:** transitional movement; no perceptual modality changes. Refusal-CORRECT.

---

## Sustained-vs-inflection notes (anti-pattern surface)

The following beats hold sustained sensory state; they belong in `location-state.md` § sensory or § conditions, NOT in sensory-flags:

- @1-12 — yard ambient summer-mid-afternoon. Sustained light, warmth, dirt-smell, beetle-noise. Not a flag fire; loc-state holds the baseline.
- @13-22 — officer's command-voice continuing across multiple beats once established. The *establishment* at @13 is the flag fire; subsequent officer-speech beats are sustained, not inflection.
- @25-37 — Taylor-officer confrontation under sustained command-voice. Not new flags.
- @60-67 — officer's continued procedural dictation. Sustained. Not new flags.

The inflection-not-sustained discipline is the second load-bearing rubric property (after disambiguation-not-redundancy). A flag fires on the *change*, not on the persistence of the changed state.

---

## Expected file shape (Phase 0 estimate)

Synthesizing candidates against the rubric:

- **Density target:** 3–6% of 77 beats = 2–5 entries. Estimate: **4 entries.**
- **Modality coverage (health-check):** ≥2 modalities across the file. Default landing: 3 sound + 1 tactile (CAND-1, 2, 3, 6) — passes coverage. If CAND-6 stripped on file-shape audit (e.g., audience-perceptibility marginal), landing is sound-only (3 entries) — **fails the modality-coverage health-check**, kicks back for re-author.
- **Tens-zone distribution (correlative observation, not gating):**
  - tens=1 fires: @13, @41, possibly @72 → 2-3 fires.
  - tens=2 fires: @30 → 1 fire.
  - tens=3 fires: @24 → 1 fire.
  - Sensory-flags fire across all tens-zones, including peaks. This is the *intended* distribution (the gate-on-2 contract that memory-flags inherited from tensometer does NOT apply here per user's "independent of tensometer" instruction).
- **Bare-not-charged audit (file-level):** each fire's proto-line text searched for charged-self-carrying words; zero fires on charged words.

Best-guess Phase 2 target shape (provisional, not authoritative):

| Entry | Beat | Modality | Tag | Delta | Bare-test | Tens (correlative) |
|---|---|---|---|---|---|---|
| 1 | @13 | sound | up | yard-ambient-murmur -> officer-command-voice | "speaks" bare | 1 |
| 2 | @24 | sound | drop | stylus-on-wax-rhythm -> silence | "stops" bare | 3 |
| 3 | @30 | sound | up | silence -> stylus-on-wax-rhythm | "moves" bare | 2 |
| 4 | @41 | sound | spike | yard-quiet -> wax-crack | "breaks at the crease" bare-leaning | 1 |
| (5?) | @72 | tactile | up | dirt-yielding -> stone-firm | "stone" bare | 1 |

That's **4-5 fires on 77 beats = 5.2–6.5%** — at the upper edge of the 3-6% band. CAND-6 (@72) is the file's structural cross-modal entry; if stripped, the file is sound-only and fails modality-coverage. The Phase 2 writer-fork's file-shape audit should keep at least one non-sound entry if a defensible candidate exists.

The Phase 2 writer-fork is blind to this file. The corpus is the candidate-set the rubric admits; the writer-fork's job is to walk the proto-lines and either land on a similar shape or earn a defensibly different one.

---

## Predicted naive failure modes (Phase 1 baseline writer rubric-blind)

1. **Charged-word redundant flagging.** Naive author fires on @73 *steps into the shadow of the frame* (light:down). The disambiguation-not-redundancy gate is counter-intuitive without rubric.
2. **Sustained-as-inflection.** Naive author fires on multiple beats of officer-command-voice (@13 + @21 + @26) instead of just the establishment beat.
3. **Fauna-feed-extension fires.** Naive author fires on @69 *wheel-tremor leaves verge-beetles east* (tactile/pressure) — the interior-only perception fails audience-side.
4. **Density-on-flat.** Naive author fires on every charged-tens beat (@24, @38, @39, @64) because they are dramatically charged. The tensometer-independence rubric is counter-intuitive — high-tens beats often *do* fire (@24 is in the corpus), but high-tens is correlative not gating, and many high-tens beats have no perceptual modality change.
5. **Modality-monoculture.** Naive author fires only on sound (the most accessible modality), missing tactile/light/thermal candidates. Modality-coverage health-check fails.
6. **Generic descriptions.** Naive author writes deltas like `sound: quiet -> loud` rather than specific naming the source/cue (`stylus-on-wax-rhythm -> silence`). Description specificity is required.

Baseline accept rate (V2 strict) expected: low (~10-25% range). Most naive fires fail either bare-not-charged, inflection-not-sustained, or audience-side perceptibility.

V1 lenient accept rate expected: ~60-80%. Form is easy to satisfy; the substantive failures are at the disambiguation / sustained-vs-inflection / audience-side level which V1 does not check.
