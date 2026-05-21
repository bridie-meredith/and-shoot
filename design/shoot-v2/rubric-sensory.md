# Sensory-Flags Facet Rubric

Authoring + review rubric for `facets/sensory.md` entries (working filename; previously `loudness.md` per `schemas/facet.schema.md`; rename pending). Phase 1 reviewer-tuning artifact for the shoot-v2 facet-tuning process. Authority for the studio writer-fork when authoring sensory-flag entries, and for the mechanic auditor when reviewing them.

Status: **V3 locked 2026-05-21.** V2 was locked at end of Phase 1 (original tuning). V3 adds two clauses derived from the b01c01 cycle-3 cap-burn: a short-chapter floor-vs-ceiling exemption (resolves the 27-bone × 6%-ceiling × 2-modality-floor arithmetic collision) and a cycle-N ADD pre-validation anti-pattern (resolves the fixer-ADD-introduces-new-HARD failure mode that the same-cycle audit could not catch).

## V3 changes summary (2026-05-21)

- **Curve-shape rubric / Episode-level shape / Modality-coverage health-check** — new "Short-chapter floor-vs-ceiling exemption" sub-clause. When `bone_count < 30` AND modality count equals the floor (2), above-band density up to `max(6%, 2/bone_count)` is ADVISORY not blocking. Modality-floor takes precedence over sparsity-ceiling because monoculture is the load-bearing pathology, not marginal density. Promoted from `URI-FACETS-V3-SHORT-CHAPTER`.
- **Anti-patterns** — new entry #14: "Cycle-N ADD without pre-validation." Fixer ADD operations introduced at audience-gate cycle N must satisfy the full per-entry rubric (modality, disambiguation, magnitude, perceptibility, AND old-state lineage) BEFORE the ADD commits — the cycle-N audit slot is too late to catch ADD-introduced HARDs. Promoted from `URI-FACETS-V3-CYCLE-N-ADD`.

Both V3 additions trace to the b01c01 sensory-modality-coverage + sensory-old-state-reader cycle-3 verdicts (`active-project/staff/audience/sensory-*/sensory-r3-verdict.md`).

---

The rubric depends on the locked location-state file (for environmental baseline at each beat) and the scene-map facet file (`theater/facets/scene-map-<book>-<chapter>.md`) (correlative observation only, NOT gating — `rhythm-shape` and `peak-bones` fields provide the same structural orientation that tensometer scalars previously provided). It does NOT depend on narrator-interest, memory-flags, or state-updates content; sensory-flags is independent of those facets.

---

## What sensory-flags is for

Sensory-flags marks beats where a **perceptual modality undergoes a discrete inflection** that the surrounding proto-line language does not self-carry. The facet's licensing function is to **disambiguate bare environmental nouns/verbs from their charged variants where the audience needs the flag to land the perception.**

The facet covers **all perceptual modalities** — not just sound. The schema's original "loudness flags" name is a misnomer; the facet captures sensory intensity inflections across:

- **sound** — volume, rhythm, timbre, attack-and-decay events.
- **light** — brightness, glare, dimming, sudden flashes.
- **smell** — odor onset, intensity changes, decay.
- **thermal** — temperature shifts (chill, heat, swelter).
- **humidity** — moisture/dryness shifts (sauna, parched).
- **pressure** — atmospheric/spatial pressure changes (compressed doorway, vacuum, deep cellar).
- **tactile** — surface contact changes (firmness, texture, grain underfoot).

The renaming from "loudness" to "sensory" reflects the facet's actual scope.

The facet serves four jobs, in priority order:

1. **Disambiguation gate (load-bearing).** A flag fires where the proto-line word is *bare* and the audience experience requires an intensity-tag the language does not already supply. *Wind* is bare; *blistering wind* is the flagged variant where the perception is its own register. *Thunder* is charged — the word self-carries booming-loud; flagging would be redundant intensity-restatement. The flag's job is the **separation** — bare-from-charged — not the addition of intensity to charged words.

2. **Stitcher selection signal.** Flags bias the stitcher toward foregrounding the perceptual inflection in the rendered output. A flagged beat may surface its perceptual register in stitched prose; an unflagged beat renders without sensory-register elevation. The flag does not generate prose; it gates whether the stitcher chooses to make the perception load-bearing in selection.

3. **Inflection register, not sustained baseline.** A flag fires on the *change* (silence → rhythm; sun → blistering glare; ambient summer → sudden chill from cellar mouth). Sustained sensory state — yard-ambient-murmur across @1-12, sustained command-voice across @13-22 — belongs in `location-state.md` § sensory note or § conditions. The flag is the inflection beat; loc-state is the baseline. **Sensory-flags is the delta on top of loc-state's level.**

4. **Cross-modal coverage.** A healthy file across an episode covers ≥2 modalities. Sensory experience is multimodal; a file that fires only sound (the most accessible modality) is monoculturing the perceptual register. The modality-coverage health-check enforces cross-modal authoring discipline.

Sensory-flags is **not** narration. It is not paraphrase of the SVO. It is not an inventory of every perceptible event. It is a one-line delta entry, fired sparsely on beats where a perceptual modality undergoes a discrete inflection the surrounding proto-line language does not self-carry.

**The test for any beat is the two-question defensibility gate (both must clear):**

- **Q1 — Audience-without-flag test.** Would the audience know the difference WITHOUT the flag there? If yes (the proto-line word self-carries the inflection, OR no real inflection is present), REFUSE. The flag does nothing the language does not already do.
- **Q2 — Magnitude-large-enough test.** Is the difference LARGE ENOUGH to justify a flag? If no (sub-threshold, micro-grain, fine-texture beneath audience experiential threshold), REFUSE. Small-but-real perceptual changes do not earn flags; the facet is for inflections the audience can experientially register.

Both must answer in favor of firing. Plus: the change must be a discrete inflection rather than a sustained level (sustained → loc-state); the change must be audience-side perceptible (not interior-only / fauna-feed-extension).

If all gates clear, fire. The default is silence.

---

## Form

Sensory-flags adopts a **state-updates-aligned delta shape**: `<modality>: <old> -> <new>`. This pattern alignment is intentional — both facets record changes in environmental/perceptual state. State-updates writes back to canonical memory; sensory-flags does not (it is a stitcher selection signal only). Both are studio-authored (sensory entirely; state-updates partially).

### Schema content shape

```
<id> @<proto-line-id> <modality>: <old-state> -> <new-state>
```

- **`<id>`** monotonic positive integer scoped to this file.
- **`@<proto-line-id>`** required anchor to a proto-line.
- **`<modality>`** one of: `sound | light | smell | thermal | humidity | pressure | tactile`. Lowercase. No abbreviation.
- **`:`** literal colon separator (matches state-updates' `<target>.<field>:` shape).
- **`<old-state>`** brief named description of the prior perceptual state (e.g., `stylus-on-wax-rhythm`, `yard-ambient-murmur`, `dirt-yielding`). Hyphenate compound names. Source the old-state from the locked location-state for the most recent loc-state-cited beat, OR from the prior sensory-flag entry if the modality has fired earlier in the episode.
- **`->`** literal arrow separator.
- **`<new-state>`** brief named description of the inflected perceptual state (e.g., `silence`, `officer-command-voice`, `stone-firm`).

### Optional tag annotation (legacy compatibility)

The schema's original loudness-flag form used `<up|down|spike|drop>` tags. These map onto the delta shape as descriptive shorthand:

- **`up`** — sustained increase. Old-state and new-state are both perceptible levels; new-state is the higher/more-intense.
- **`down`** — sustained decrease. New-state is the lower/less-intense.
- **`spike`** — transient discrete event. The new-state is brief; the old-state is what resumes immediately after.
- **`drop`** — transient discrete absence. The new-state is silence/dark/absence; the old-state is what resumes immediately after.

These tags are **not required** in the content shape. They may be added as inline annotations after the delta if useful (`# tag: up`). The delta itself is the source of truth.

### Hard-fence on description naming

The old-state and new-state names should be **environmental/perceptual nouns**, not narrative gestures or character interiority. *the stylus stops on the board* yields `sound: stylus-on-wax-rhythm -> silence`, NOT `sound: ambient -> Taylor-feels-the-quiet`. Sensory-flags is studio-authored and POV-agnostic; the entry describes what changed *out there*, not what the narrator made of it.

---

## V1 rubric (locked at end of Phase 1) — four axes

A sensory-flag entry passes review iff it **affirmatively demonstrates** at least one signature on each of four axes (modality-inflection, disambiguation-discipline, magnitude-sufficiency, audience-side-perceptibility) and does not violate any anti-pattern.

The two **defensibility questions** are the rubric's primary gates and apply across multiple axes:

- **Q1 (audience-without-flag test):** Would the audience know the difference WITHOUT the flag? Cleared by the **disambiguation-discipline** axis (Axis 2). If yes, REFUSE.
- **Q2 (magnitude-large-enough test):** Is the difference LARGE ENOUGH to justify a flag? Cleared by the **magnitude-sufficiency** axis (Axis 3, new). If no, REFUSE.

Both questions must answer in favor of firing. The default is silence; the burden of justification is on the fire.

### 1. Modality-inflection

Does a perceptual modality undergo a discrete inflection at this beat?

ACCEPT signatures:

- **Modality identifiable.** The modality is one of the seven enumerated above; the entry names it correctly. Cross-modal entries are forbidden (no `sound+thermal:` composite); cull to the dominant modality or split into two entries if both are genuinely present and audience-perceptible.
- **Inflection class clear.** The change is `up | down | spike | drop` (sustained-up / sustained-down / transient-spike / transient-drop). The old-state and new-state are both nameable; the inflection direction is unambiguous.
- **Anchored to a real perceptual baseline.** The old-state matches the most recent location-state file's § sensory or § conditions field for the beat's location, OR the most recent prior sensory-flag entry on the same modality. A flag whose old-state contradicts loc-state is a cross-facet violation.

REJECT signatures:

- **No-modality fire.** The entry fires on a beat where no perceptual modality undergoes a discrete change. (E.g., fire on @50 *taylor turns to mira* — no perceptual inflection; transitional movement only.)
- **Cross-modal blur.** Entry names two modalities or compounds them. Cull to dominant; split if two distinct entries are genuinely earned.
- **Old-state contradicts loc-state.** Entry's old-state does not match the loc-state baseline. Either flag back to studio for loc-state revision or revise the sensory entry.
- **Unanchored old-state (HARD).** Entry's old-state does not resolve to (a) the most recent loc-state file's § sensory or § conditions baseline for the beat's location, OR (b) the most recent prior sensory-flag entry on the same modality. A free-floating old-state ("hook-alley-ambient" with no loc-state or prior-sensory anchor) is a fictive baseline — the inflection is asserted against a baseline the file does not establish. Either backfill the loc-state baseline OR cite a prior sensory entry. (URI-FACETS-CYCLE-1, 2026-05-19 — promoted from audience-gate cycle-1 attack on b01c01 sensory:1 @1 and sensory:2 @9: sensory-old-state-reader specialist flagged the unanchored old-state pattern across both entries.)

### Cross-facet modality silent-gap (loc-state ↔ sensory contract)

A perceptual *event* named in a loc-state sensory note (e.g., "the stone of the far wall has begun releasing its morning-caught warmth" — a thermal change-event) without a corresponding sensory-flag at or near the anchor leaves the modality silent at exactly the beat the loc-state asserts it. **Cross-facet REJECT signature:** loc-state sensory note that names a discrete perceptual event (thermal release, audible texture change, smell drift) must be accompanied by a sensory-flag at the same anchor (preferred) OR the loc-state author must downgrade the sensory note to non-event ambient language (persistence / texture / state). If both layers stay silent on the event after audit, the chapter has a documented modality silent-gap — flag for cross-facet review. (URI-FACETS-CYCLE-1, 2026-05-19 — promoted from audience-gate cycle-1 attack on b01c01 sensory file at @13: sensory-modality-coverage specialist flagged the thermal silent-gap; the loc-state file authoritatively named a thermal change at @13 with no sensory-side ratification.)

### 2. Disambiguation-discipline (load-bearing)

Is the proto-line word *bare* (does not self-carry the perceptual intensity), such that the flag is the disambiguator?

This is the rubric's load-bearing axis.

ACCEPT signatures:

- **Bare proto-line word.** The proto-line uses a generic noun/verb that does not surface the perceptual register. *Speaks*, *stops*, *moves*, *breaks at the crease*, *steps on the stone* are bare verbs/nouns; the perceptual inflection (volume, rhythm, audible-crack, footing-firmness) is not in the language. The flag adds the disambiguating tag.
- **Audience needs the flag.** Without the flag, the audience receives the action mechanically; with the flag, the audience receives the perceptual register that the action carries. The flag does work the language does not.
- **Charged-word audit clears.** Search the proto-line for charged words ("thunder", "scream", "shadow", "blaze", "stench", "shriek", "blistering", "silent", "dazzle", "swelter", "freeze", and similar). If a charged word is in the proto-line and self-carries the perceptual register the flag would name, the flag is redundant — REJECT.

REJECT signatures:

- **Charged-word redundancy.** The proto-line word self-carries the intensity. Examples:
  - @73 *taylor steps into the shadow of the frame*. "shadow" charges the light-down; flagging `light: sun -> shadow` is redundant. The audience already perceives the dimming from "shadow".
  - Hypothetical *the thunder cracks the sky*. "thunder" charges the sound-spike; flagging `sound: storm-rumble -> thunder-clap` is redundant.
  - Hypothetical *the stench rolls out of the cellar*. "stench" charges the smell-up; flagging `smell: cellar-musty -> stench` is redundant.
  - The user's exemplar: *blistering wind* is the flagged variant of bare *wind*; the bare proto-line *the wind crosses the yard* would license `thermal: ambient -> wind-blistering` because *wind* is bare. The proto-line *the blistering wind crosses the yard* would NOT license a thermal flag because *blistering* charges the word.
- **Stage-named flagging.** Entry names the flag as flag (e.g., `sound: nothing -> SOUND_SPIKE`). The delta names *what changes*, not *that a flag fires*.
- **Generic descriptions.** Old-state or new-state names like `quiet`, `loud`, `dark`, `bright`, `cold`, `hot` without specifying the source/cue. The naming should be specific enough that a reader can distinguish *this* perceptual state from another (`stylus-on-wax-rhythm` not `quiet`; `officer-command-voice` not `loud`).

### 3. Magnitude-sufficiency (load-bearing — new in V1)

Is the perceptual change LARGE ENOUGH to warrant a flag? The Q2 defensibility test.

ACCEPT signatures:

- **Audience-experiential threshold cleared.** A reader without source-material fluency, reading the proto-line plus the flag, would experience the inflection as a perceptual register-shift large enough to land. Volume changes the audience can imagine hearing; light changes the audience can imagine seeing; thermal changes the audience can imagine feeling.
- **Difference matters.** The flag is doing register-work the unflagged proto-line does not do. The new-state and old-state are not just different but distinguishably so at audience-experiential scale.
- **Justification defensible.** The author can name *why* this inflection earns a flag: it is a structural perceptual marker (rupture, threshold, register-shift), not a fine-texture or continuous-grain change.

REJECT signatures:

- **Sub-threshold magnitude.** The change is real but below audience experiential threshold. The small audible texture of stylus-marking at @64 is real (the wax-tip moves) but the audible event is fine-grain, not register-shifting; the audience would not experientially register the difference. REJECT.
- **Micro-grain texture.** Continuous fine-texture changes — the slight change in the officer's voice as he angles toward the threshold (@31), the small variation in beetle-noise across @1-12 — are perceptual but not register-shifting. REJECT.
- **Cumulative-only difference.** The inflection only registers if accumulated across many beats. Sensory-flags fires on discrete inflection beats, not on cumulative drift.
- **Inflection-real-but-not-large-enough.** A genuine modality inflection that does not clear the experiential threshold for audience-side register-shift. The author may be tempted to fire on technical grounds (the modality genuinely changed); the rubric's magnitude gate forbids it. **The default is silence; the burden of justification is on the fire.**

The user's framing exemplars:

- *Thunder is booming loud* — clears Q2 (large magnitude) but FAILS Q1 (charged word). Refusal-CORRECT.
- *Wind* (bare) → *blistering wind* (flagged) — clears both Q1 (bare; audience needs flag to register the swelter) and Q2 (blistering is large-magnitude thermal/tactile inflection). Fire-CORRECT.
- *Stylus marks at @64* — borderline Q1 (the marking is bare in the proto-line) but FAILS Q2 (magnitude sub-threshold; the audible event of stylus-on-wax-marking is fine-grain). Refusal-CORRECT.
- *The seal breaks at the crease* — clears Q1 (bare phrasing foregrounding tactile mechanism not audible event) and clears Q2 (the wax-crack is a discrete audible inflection at audience-experiential scale; seal-cracks are recognizably perceptible). Fire-CORRECT.

### 4. Audience-side perceptibility

Is the perceptual change something the audience can register from the rendered output (with the flag), or is it interior-only / fauna-feed-extension that requires Taylor's perceptual faculty to detect?

ACCEPT signatures:

- **Universally legible once flagged.** A reader without source-material fluency can register the perceptual change from the proto-line plus the flag. Volume changes, light changes, thermal changes that physically register on a body the audience can imagine.
- **Studio-recordable.** The change is environmental — something studio's state files can hold as a recorded change. (Studio is the author for a reason; environmental sensory state is studio's domain.)

REJECT signatures:

- **Fauna-feed-extension fires.** The perception requires Taylor's faculty extending her range (the verge-beetles register the wheel-tremor; the corvid-feed registers a sound source two streets over). The audience does not have access to the extended-range perception. **Per the user's pre-Phase-0 framing: fires must be where the audience perceives the inflection, not where the narrator's faculty extends her range to perceive it.** Reject. (These perceptions belong in narrator-interest where Taylor-interior registration is the facet's domain.)
- **Interior-only registration.** The "perceptual" change is actually an interior shift (mood, alertness, focus). Sensory-flags is environmental; interior shifts belong in narrator-interest or feeling-flags or state-updates (actor-state).
- **Sub-threshold perception.** The change is real but below the audience's experiential threshold (the small audible texture of stylus-marking at @64; the micro-changes in air-pressure as a body shifts). Sub-threshold inflections are not the facet's job. Refuse.

---

## Cross-axis tests

- **The bare-word test (Q1 defensibility).** Read the proto-line aloud. Highlight the noun/verb the flag is keying on. If the word's plain meaning already supplies the perceptual intensity (thunder, shadow, stench, blistering, scream, blaze), REJECT — the audience would know the difference without the flag. If the word is bare (speaks, stops, moves, steps, breaks, comes), proceed to magnitude test.
- **The magnitude test (Q2 defensibility).** Picture an audience member reading the proto-line plus the proposed flag. Is the inflection large enough that they experientially register a perceptual register-shift? If sub-threshold (fine-grain, micro-texture, cumulative-only), REJECT. If experientially register-shifting (rupture, threshold, large delta), proceed.
- **The inflection-not-sustained test.** Look up the surrounding 3-5 beats. Is this beat the *change-point* or part of a sustained level? If sustained (officer's command-voice across @13-22; yard-ambient-summer across @1-12), the sustained state belongs in loc-state, not in sensory-flags. The flag fires on the inflection beat only.
- **The audience-side test.** Strip Taylor's faculty (no fauna-feed, no extended-range, no interior). Can the audience still register the perceptual change from the proto-line plus the flag? If yes, ACCEPT. If the audience can't perceive without Taylor's faculty, REJECT.
- **The modality-coverage test (file-level).** Across the file, count distinct modalities fired. If only one modality (sound-only file), the file is monoculturing. Audit unflagged beats for tactile/light/thermal/pressure inflections that earned and were skipped.
- **The loc-state-baseline test.** For each fire, locate the most recent location-state entry for the beat's location. Does the old-state match loc-state's baseline? If contradicting, cross-facet violation; flag back.

---

## Anti-patterns (named for the rubric)

These are the contamination patterns the writer must resist and the reviewer must call out.

1. **Charged-word redundancy.** Flagging on proto-line words that self-carry the perceptual register (thunder, shadow, stench, blistering, scream).
2. **Sustained-as-inflection.** Flagging on every beat of a sustained perceptual level (every officer-speech beat after the establishment beat).
3. **Fauna-feed-extension.** Flagging on perceptions Taylor's extended-range faculty registers but the audience cannot.
4. **Interior-only registration.** Flagging on interior shifts (mood, alertness) instead of environmental change.
5. **Sub-threshold magnitude.** Flagging on changes below audience experiential threshold (micro-textures, fine-grain). Q2 defensibility failure.
6. **Modality-monoculture (file-level).** All fires on one modality (typically sound). Cross-modal coverage required.
7. **Cross-modal blur.** Naming two modalities in one entry instead of splitting or culling.
8. **Generic naming.** `quiet -> loud`, `dark -> bright`, `cold -> hot` without specifying source/cue.
9. **Loc-state contradiction.** Old-state contradicts the locked location-state baseline. Cross-facet violation.
10. **Pressure-signal gating misread.** Author treats bones in `peak-bones` arrays as eligible / bones in `flat-low` zones as ineligible (or vice versa). Sensory-flags is independent of the scene-map pressure-signal; rhythm-shape correlation is observation, not gating.
11. **Stage-named flagging.** Naming the flag as flag (`sound: nothing -> SOUND_SPIKE`) instead of naming the change.
12. **Density-on-charged-beats.** Firing on every `peak-bones`-class beat to hit dramatic peaks. Sensory inflections do correlate with peak-bones-class beats (rupture, peak), but many such beats have no perceptual modality change; firing for charge alone is anti-pattern.
13. **Interior-cue mistaken for environmental cue.** *the air thickens around her* — is this environmental humidity-up, or interior-pressure registration? Default to interior unless studio's state file independently records the environmental change.
14. **Cycle-N ADD without pre-validation (V3, 2026-05-21).** A fixer ADD operation introduced at audience-gate cycle N must satisfy the **full per-entry rubric** — modality-inflection, disambiguation-discipline, magnitude-sufficiency, audience-side-perceptibility, AND old-state lineage from loc-state or prior sensory entry on the same modality — BEFORE the ADD is written to the facets file. The audience-gate cycle N is too late to catch ADD-introduced HARDs: the audit-revise cap leaves no slot to fix what cycle N itself introduced. **Authors / fixers:** validate the proposed ADD against the full rubric (especially old-state lineage) before committing. If the ADD requires a loc-state edit (because the old-state has no prior anchor), the loc-state edit must land FIRST and the sensory ADD must reference the now-anchored baseline. **Auditors:** an ADD that lands at cycle N AND introduces a NEW finding the prior cycles did not surface is a process violation in addition to whatever content violation it carries; both should be reported. (URI-FACETS-V3-CYCLE-N-ADD, 2026-05-21 — promoted from b01c01 cycle-3 cap-burn: sensory:3 @17 ADD by fixer at cycle-3 to clear modality-floor introduced unanchored-old-state HARD on the very fix-path; no cycle remained to remediate. Related: A3 in `active-project/staff/reviews/run-action-plan-b01c01-2026-05-20.md` — command-body Phase 5b iteration logic carries the structural fix; this anti-pattern carries the rubric-side enforcement.)

---

## Curve-shape rubric (file-level)

The sensory-flags file as a whole must demonstrate disambiguation-layer shape across the episode. The mechanic auditor checks the curve in addition to per-entry correctness.

### Episode-level shape

The full sensory-flags file across an episode must satisfy:

- **Sparsity.** 3–6% of proto-lines fire (s01e01 expected: ~2–5 entries on 77 beats). Sparsity is load-bearing — the disambiguation function depends on contrast against unflagged baseline.
- **Short-chapter floor-vs-ceiling exemption (V3, 2026-05-21).** When `bone_count < 30`, the modality-floor (≥2 modalities below) and the sparsity ceiling (6%) collide arithmetically: 2 entries on a 27-bone chapter yields 7.4%, exceeding 6%. **The modality-floor takes precedence.** Under the exemption, when (a) `bone_count < 30` AND (b) the file's modality count equals the floor (2), the effective sparsity ceiling is relaxed to `max(6%, 2 / bone_count)` — automatically permitting the floor-minimum entry count. The disambiguation-gradient remains intact (two entries on 27 bones still preserve contrast); the floor cannot be sacrificed because sensory monoculture is the load-bearing pathology, not marginal density. Above-band density under these conditions is **ADVISORY**, not blocking. The exemption does NOT apply if modality count exceeds the floor (3+ modalities at 27 bones → standard 6% ceiling applies; cull to the strongest disambiguation cases). (URI-FACETS-V3-SHORT-CHAPTER, 2026-05-21 — promoted from b01c01 cycle-3 sensory-modality-coverage verdict: "Irresolvable arithmetic consequence of meeting the floor on a short episode.")
- **Modality-coverage health-check.** ≥2 modalities represented across the file. A sound-only file fails coverage; a sound+tactile or sound+light or sound+thermal file passes. Cross-modal authoring discipline is the structural addition for sensory-flags relative to single-axis facets.
- **Pressure-signal correlation observation (not gating).** Sensory fires distribute across scene zones. Correlation observation: bones in `peak-bones` arrays often fire (rupture, peak); `flat-low` environmental bones also fire (a chill in an idle moment). The rubric does NOT require any particular rhythm-shape distribution. The mechanic auditor reports the distribution as observation, consulting the scene-map file (`theater/facets/scene-map-<book>-<chapter>.md`) for `rhythm-shape` and `peak-bones` context — not as a verdict.
- **Bare-not-charged audit (file-level).** Each fire's proto-line text searched for charged-self-carrying words. Zero fires on charged words.
- **Inflection-not-sustained audit (file-level).** Each fire's surrounding 3-5 beats checked for sustained level vs. change-point. Zero fires on sustained-level beats.

### Scene-level shape

For each scene (per the scene-map file's `@<start>-@<end>` ranges):

- **Per-scene cap ≤ 3 (frugality rule).** A scene may carry **at most 3 sensory fires** — frugal by design. Prefer modality-diversity over modality-repeat: two sound-spikes in one scene → cull the weaker; sound + thermal + light all firing once each in one scene → all three permitted (within the 3 cap). The cap is hard, not a guideline. Most scenes will carry 0–1 fires; 2–3 fires per scene is reserved for confrontation-class scenes with multiple genuine cross-modal inflections.
- **Inflection-pair coherence.** When a `drop` and a subsequent `up` fire on the same modality (e.g., @24 sound:drop + @30 sound:up), the pair should reach a sensible *back-to-baseline* state. The new-state of the up should match the old-state of the drop (modulo natural variation). If they don't match, one entry is wrong.

### When curve-shape fails

The author's response to a failing curve is **not** to inflate fires to hit density. The response is:

- **Modality-coverage fix.** If sound-only, audit unflagged beats for tactile/light/thermal/pressure inflections that earned and were skipped. Add fires where genuinely earned.
- **Sparsity fix.** If over 6%, audit fires for sustained-as-inflection, charged-word redundancy, fauna-feed-extension. Strip what fails.
- **Bare-not-charged fix.** If any fire's proto-line word is charged, strip the fire.
- **Inflection-not-sustained fix.** If any fire is on a sustained-level beat, strip and consider whether loc-state needs updating to hold the sustained state.

Inflating fires to hit density without earning each fire on all three axes is the prohibited move.

---

## Cross-facet contract

Sensory-flags' upstream and downstream consumers.

### Anchor expectations (consumer side)

- **Location-state (locked, upstream).** Sensory-flags' old-state must match the most recent loc-state baseline for the beat's location. Cross-facet violation if contradicting. Loc-state holds sustained sensory level; sensory-flags holds inflection on top of that level. Pattern: loc-state is the level, sensory-flags is the delta.
- **Scene-map (upstream — correlative-not-gating).** Sensory-flags is **independent of the scene-map pressure-signal**. Fires may occur in any scene zone. Correlation observation only — bones in `peak-bones` arrays often have sensory inflections (rupture, peak); some peak-bones-class bones do not. The scene-map's `rhythm-shape` and `peak-bones` fields (loaded from `theater/facets/scene-map-<book>-<chapter>.md`) are **correlative context, not anchor-requirement**. @24 fires (perceptibility large; bare verb — and happens to be in `peak-bones`); @64 likely refuses (perceptibility small; sub-threshold — regardless of scene-map classification). Sensory-flags does not inherit memory-flags' inverted pressure-signal rule and does not inherit any scene-map-gating rule.
- **State-updates (parallel, structural).** Sensory-flags and state-updates share the delta-shape `<target>: <old> -> <new>` pattern. They are distinct facets: state-updates writes back to canonical memory (persistent change); sensory-flags is stitcher selection signal only (no writeback). A sensory-flag may co-occur with a state-update on the same beat (a perceptual inflection that is also a persistent state change), but they fire independently and are not gated on each other.

### Back-contract (what sensory-flags owes downstream)

- **Stitcher (primary consumer).** Sensory-flags fires bias the stitcher toward foregrounding the perceptual register at the fired beat. The stitcher reads sensory-flags as a selection signal (which beats to surface in full sensory register vs. compress).
- **Metaphor facet (downstream, editor-authored).** Editor *may* author metaphors against sensory-flag fires (a sensory inflection is a natural metaphor-anchor candidate). Co-citation is **permitted but not required** — metaphor's licensing layer is memory-flags, not sensory-flags. Sensory-flags is one of several signals metaphor may co-cite.
- **Audience-interest flags (advisory).** Audience personas may have interest-flag fires on sensory-flag-fired beats; aggregate audience-interest density on sensory-flag fires is expected to be elevated (the beats *are* perceptually charged; multiple audience perspectives notice).

### What sensory-flags does NOT condition

- Scene-map (forward). Sensory-flags does not change scene-map fields.
- Narrator-interest (forward). Sensory-flags does not require narrator-interest co-citation. They are independent.
- Memory-flags (forward). Sensory-flags does not gate memory-flags. They are independent.
- State-updates (forward). Sensory-flags does not gate state-updates. They are independent.
- Vibes-updates. Vibe shifts are showrunner's call.

---

## Calibration anchors (drawn from s01e01 corpus)

Six worked examples spanning the rubric. Used during Phase 1 reviewer tuning and Phase 2 writer-fork.

- **`s01e01:13 the officer speaks to the yard` — FIRE.** Sound:up. Delta: `sound: yard-ambient-murmur -> officer-command-voice`. Bare verb ("speaks"); audience-perceptible (command-voice register is universally legible once flagged); inflection-not-sustained (this is the establishment beat; subsequent officer-speech beats are sustained at the new level). Scene-map: bone in `flat-low` rhythm zone (correlative observation — sensory fires in any zone). ACCEPT.

- **`s01e01:24 the stylus stops on the board` — FIRE.** Sound:drop. Delta: `sound: stylus-on-wax-rhythm -> silence`. Bare verb ("stops"); audience-perceptible (silence-cut is universally legible); inflection (transient — @30 resumes the rhythm). Scene-map: bone listed in scene's `peak-bones` array (correlative observation; peak-bones-class beat with sensory inflection — both fire; sensory is not gated by this). ACCEPT.

- **`s01e01:30 the stylus moves on taylor's name` — FIRE.** Sound:up. Delta: `sound: silence -> stylus-on-wax-rhythm`. Bare verb ("moves"); audience-perceptible; paired-event with @24 (drop). Scene-map: bone in `rising` zone (correlative). ACCEPT. Inflection-pair-coherence test: @24's old-state was `stylus-on-wax-rhythm`; @30's new-state is `stylus-on-wax-rhythm`. Match — back-to-baseline rhythm pair coherent.

- **`s01e01:41 the seal breaks at the crease under his thumb` — FIRE.** Sound:spike. Delta: `sound: yard-quiet -> wax-crack`. Bare phrasing ("breaks at the crease under his thumb" foregrounds tactile mechanism, not audible event); audience-perceptible (the seal-break crack is universally legible once flagged); inflection (transient discrete event). Scene-map: bone in `flat-low` zone (correlative). ACCEPT.

- **`s01e01:73 taylor steps into the shadow of the frame` — REFUSE.** Modality candidate light:down. The proto-line word "shadow" is **charged** — it self-carries light-dimming for the audience. Adding `light: sun -> shadow` is redundant intensity-restatement. **Calibration anchor for charged-word redundancy.** Refusal-CORRECT.

- **`s01e01:50 taylor turns to mira` — REFUSE.** No perceptual modality undergoes inflection. Transitional movement only. Refusal-CORRECT on no-modality-fire test.

---

## Author / reviewer notes

- **Author:** studio writer-fork. Loads: locked location-state file (for old-state baseline at each beat), scene-map facet file (`theater/facets/scene-map-<book>-<chapter>.md`) (correlative observation only — NOT gating; `rhythm-shape` and `peak-bones` replace the pre-overhaul tensometer scalar for correlative context), the bones file, this rubric, the corpus-selection note. **Two-pass authoring:**
  1. **Per-beat pass.** Walk the proto-line file. For each beat, decide FIRE or NONE. If FIRE, identify modality, write the old-state from loc-state (or prior sensory entry on same modality), write the new-state, verify bare-not-charged, verify audience-side perceptibility, verify inflection-not-sustained.
  2. **File-shape pass.** Read the file as a curve. Check episode-level density (3–6%), modality-coverage (≥2 modalities), bare-not-charged audit (zero fires on charged words), inflection-not-sustained audit (zero fires on sustained beats), inflection-pair coherence (drop/up pairs reach back to baseline). Either fix misfires (NONE→FIRE add for missing coverage; FIRE→NONE strip for charged-word / sustained / sub-threshold) or flag screen-writer kickback for structural gaps. **Do not inflate to hit density.**
- **Reviewer (mechanic auditor):** under this rubric. Per-entry verdict for fires: CORRECT (all three axes earned, no anti-pattern fired) or INCORRECT (named axis-failure or anti-pattern). Per-entry verdict for refusals: CORRECT (no modality earned / charged-word / sustained / interior-only) or MISSED (a modality + bare-word + inflection earned a fire that the author skipped). File-level verdict: SHAPE-OK / SHAPE-FAIL with named density / modality-coverage / bare-charged / sustained failure mode. Cross-facet contract pre-ship check is mandatory (loc-state baseline match; tens correlation observation noted; no narrator-interest / memory-flags gating).
- **Reviewer (dialect audience):** **NOT INVOKED.** Sensory-flags is studio-authored, environmental, voice-light. The description names a perceptual cue, not character voice. Same precedent as state-updates and loc-state. Mechanic-only single-gate review.
- **Verdict combination.** Mechanic verdict alone. No hybrid gate.
- **Cull:** sensory-flags has per-file cull (per `schemas/facet.schema.md`). Cull is delete-only — entries that fail any axis or any anti-pattern are deleted. No rewrites at cull time. The Phase 2 writer-fork output IS the cull-stage authoring; revision happens in Phase 4 only.
- **Floor defense.** If the author defends a NONE against a reviewer push to FIRE by citing rubric (charged word self-carries, sustained-not-inflection, sub-threshold, fauna-feed-extension), accept the defense. Sparsity is load-bearing; over-firing dissolves the disambiguation gradient.
- **Ceiling defense.** If the author defends a FIRE that the reviewer would push to NONE, the burden is on the author to name (a) the modality, (b) the inflection class (up/down/spike/drop), (c) the bare proto-line word, (d) the audience-side perceptibility argument, (e) the loc-state baseline match. A FIRE that survives ceiling defense should also pass the modality-coverage file-level test and the inflection-pair-coherence test where applicable.
- **Cross-author dependencies.** Sensory-flags is single-author (studio). No cross-author dependency check at Phase 5; the cross-facet contract check (vs. loc-state, scene-map correlation, no narrator-interest / memory-flags / state-updates gating) replaces it.

---

## V1 lenient form (retained for lift comparison only)

V1: ACCEPT iff the entry is form-correct (well-formed delta with modality + old-state + new-state, anchor-to-real-proto-line) AND any perceptual modality is plausibly invoked at any reading. No disambiguation-discipline check, no audience-side check, no inflection-vs-sustained check, no curve-shape check.

V1 exists only to produce a baseline accept-rate for round-trip comparison after writer-tuning. It is not an authoring target. Do not soften V2 toward V1 between rounds.

---

## What sensory-flags is not

- Not narration. Not paraphrase of the SVO. Not an inventory of all perceptible state.
- Not loc-state. Loc-state holds sustained sensory level; sensory-flags holds inflection. Loc-state is the baseline; sensory-flags is the delta on top. **Note (URI-SCENE-RHYTHM, 2026-05-13):** transition-run continuity (an established sensory baseline persisting through a `flat-low` transition stretch, e.g. alley-sound carrying across a flat-low scene) belongs in loc-state's transition-run continuity license, NOT in sensory-flags. Sensory-flags fires on inflection (spike/drop/change); continuity is sustained baseline carry — the loc-state continuity-carry slot is the correct home. See `design/shoot-v2/rubric-location-state.md § Transition-run continuity license`.
- Not narrator-interest. Narrator-interest is what the POV character registers. Sensory-flags is what changes *out there*, audience-side. The two facets may co-fire on the same beat but are independent.
- Not memory-flags. Memory-flags fires the licensing layer for figurative reach. Sensory-flags fires the disambiguation layer for bare environmental language. Independent.
- Not state-updates. State-updates writes back to canonical memory (persistent). Sensory-flags is stitcher selection signal only (no writeback). Pattern-aligned (delta shape), domain-distinct.
- Not editable after cross-facet consistency. Once locked, entries are an input to the stitcher and to metaphor-facet authoring.
- Not symmetric with loudness's original schema definition. The schema's `<up|down|spike|drop> <one-clause description>` form is generalized to `<modality>: <old> -> <new>` with optional tag annotation. Schema update pending Phase 5 ship.

---

## Schema rename (pending)

`schemas/facet.schema.md` § "loudness flags" requires update at Phase 5 ship to:

- Rename section heading to "sensory flags".
- Update file path from `facets/loudness.md` to `facets/sensory.md`.
- Update content shape from `<up|down|spike|drop> <one-clause description>` to `<modality>: <old> -> <new>` with optional `# tag: <up|down|spike|drop>` annotation.
- Update author from "studio" to "studio" (unchanged).
- Add modality enumeration (sound / light / smell / thermal / humidity / pressure / tactile).

The schema edit is deferred to Phase 5 to avoid premature lock; the locked rubric and locked facet file are the authority during tuning.
