---
reviewer: sensory-modality-coverage
facet: sensory
cycle: 2
episode: b01c02
date: 2026-05-21
verdict: revise
---

# Verdict reasoning

Cycle-1 verdict: accept. The fix relocated sensory:2 from @22 to @23 and added conditions notes to loc-state:2 (@4) and loc-state:11 (@22). I re-run file-level distribution.

**Modality tally (post-fix):**
- sound: 1 fire (sensory:1 @7)
- light: 1 fire (sensory:2 @23)
- smell: 0
- thermal: 0
- humidity: 0
- pressure: 0
- tactile: 0

Modality count: 2. Coverage floor met. Distribution is structurally identical to cycle-1 — the relocation @22→@23 does not change the modality tally. My file-level pass on coverage holds on that count.

**Sparsity:** 2 entries / 27 bones = 7.4%. Short-chapter floor-vs-ceiling exemption (V3) still applies: bone_count 27 < 30, modality count = 2 = floor. ADVISORY, not blocking. Unchanged from cycle-1.

**New condition introduced by the conditions notes:** The fix added sensory language to loc-state:2 @4 and loc-state:11 @22. I audit both additions under the cross-facet modality silent-gap rule: a loc-state sensory note that names a discrete perceptual event (thermal release, audible texture change, smell drift) must be accompanied by a sensory-flag at the same anchor OR the loc-state author must downgrade the note to non-event ambient language.

loc-state:2 @4 conditions note: "ambient-sound baseline before column arrival — ordinary morning street noise and shoe-leather on cobbles; no column-echo yet; this is the watch-press-alley-ambient state (anchor for sensory:1 old-state)."

This note names a baseline level, not a discrete perceptual event. "Ordinary morning street noise" describes a sustained ambient level, not a change-point. The rubric's modality-silent-gap rule fires on notes that name a discrete perceptual event. This note names a sustained level — the watch-press-alley-ambient is the pre-column baseline, not an onset event. No sensory-flag required at @4 from my axis. No silent-gap from loc-state:2.

loc-state:11 @22 conditions note: "interior-darkness baseline before @22 — lodging-interior unlit, night scene-open (time-skip blank @21); this is the unlit-lodging-interior old-state (anchor for sensory:2 old-state at @23)."

This note names the pre-lamp darkness as a static baseline state (unlit, night, scene-open). It is framing the darkness that preceded @22, not naming a darkness-onset event. The darkness was always there; it was not a change-point named in the conditions note. The note is ambient-baseline language. No discrete perceptual event is named. No sensory-flag required at @22 from my axis under the silent-gap rule.

However: loc-state:11 @22 also carries its main field content: "the lamp: single flame, tight radius, the ledger surface lit and the rest of the room falling off into dark." The main loc-state:11 body describes the post-lamp state. The lamp-lighting itself is a discrete light-inflection event that the loc-state body describes authoritatively. Under the cross-facet modality silent-gap rule — "loc-state sensory note that names a discrete perceptual event must be accompanied by a sensory-flag at the same anchor OR the loc-state author must downgrade to non-event ambient language" — the lamp-lit state described in loc-state:11 @22 raises the question of whether @22 requires a sensory-flag.

The fix elected to place sensory:2 at @23, not @22, precisely to avoid the action-verb self-charge on `lights the lamp`. But from my distribution axis, the question is whether the lamp-inflection event described at loc-state:11 @22 is now left silent at its own anchor beat. sensory:2 fires at @23, one beat later. The silent-gap rule says the sensory-flag should be "at the same anchor (preferred) OR" it requires the loc-state note to be downgraded to non-event language.

The lamp-lighting IS a discrete perceptual event (darkness → tight lamp circle). loc-state:11 describes it at @22. The sensory-flag fires at @23. The preferred-anchor match is not met; the flag is one beat off the loc-state event anchor. The silent-gap rule's alternative ("OR the loc-state author must downgrade to non-event ambient language") is also not met — loc-state:11's main body is clearly event-descriptive ("lamp: single flame, tight radius, the ledger surface lit").

This is a cross-facet modality silent-gap at @22: loc-state:11 @22 names a discrete light-inflection event; no sensory-flag fires at @22. sensory:2 fires at @23, but @22 itself is silent on the modality at the event anchor. The preferred-anchor match fails; the language downgrade alternative is not in place.

**Updated modality distribution assessment:**

The file maintains 2 modalities and meets the floor. But the light-modality fire's anchor (@23) is misaligned with the discrete event the loc-state anchors at @22. The file has a cross-facet silent-gap at @22 and a lagged fire at @23. From a distribution standpoint: the light inflection event exists in loc-state and is not silently-gapped at file level (it does have a sensory-flag somewhere in the file). But the preferred-anchor alignment is broken — my calibration anchors cite "lamp-lit at @58, lamp-guttering at @122, candle-catching at @130 — only @58 and @130 fire sensory. @122 silent? Inflection-skip." The analogous structure here is: lamp-lit at @22 — sensory:2 fires at @23 instead. @22 inflection-skip.

My cycle-1 accepted on "lamp-lit @22 → light-fire @22, match good." The relocation breaks that alignment. The light-event inflection point in loc-state:11 is @22; the sensory-flag is at @23. The inflection anchor is silent; the settled-state beat carries the fire. This is an inflection-skip at @22.

REVISE. The file maintains modality floor (2 modalities) and short-chapter exemption (advisory density). But the light-modality fire is now one beat off its loc-state anchor, creating an inflection-skip at @22 and a settled-state fire at @23. The cross-facet silent-gap rule requires the fire to match the event anchor or the loc-state language to be downgraded. Neither condition is met.

# Entry-level callouts

None from file-level distribution per se. The concern is anchor-alignment, not modality count.

`[sensory:2 anchor-alignment] — loc-state:11 @22 names the lamp-lighting event (discrete light inflection). sensory:2 fires at @23 (settled-state beat). @22 is inflection-silent; @23 carries the fire. Cross-facet preferred-anchor match broken; @22 is an inflection-skip under the modality-silent-gap rule.`

# Convergence trace

- Cycle-1 accept: held on 2-modality coverage floor, sound+light, short-chapter exemption, correct distribution. That reading was conditional on sensory:2 being at @22, co-located with loc-state:11. The relocation breaks the co-location.
- Modality silent-gap rule (URI-FACETS-CYCLE-1): the rule requires sensory-flag at same anchor as loc-state event note, or loc-state downgrade to non-event language. The loc-state:11 @22 main body names the lamp-lit event. sensory:2 at @23 does not co-locate with @22. The gap is not a zero-fire gap (the light modality does have a file-level fire), but it is a preferred-anchor misalignment.
- The disambiguation-pedant cycle-2 finding (lagged-anchor / inflection-not-at-inflection-beat) and this finding converge: both identify that sensory:2 belongs at @22 (the inflection beat) but cannot be placed there without violating the action-verb self-charge rule. The structural conflict — inflection beat IS the self-charged verb — is what neither the relocation fix nor the loc-state conditions-note strategy can resolve. The two seams point to the same root: sensory:2 has no valid anchor in this episode.
- Auditor FREQUENCY-BAND: short-chapter exemption correctly applied; that finding is unaffected by anchor relocation. The file-level density advisory is unchanged.
