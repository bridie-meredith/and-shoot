facet: sensory
chapter: b01c11
author: studio
rubric: design/shoot-v2/rubric-sensory.md (V3 locked 2026-05-21)
bones: 27
entries: 2 (pre-cull) | 2 (post-cull: 0 removed)
density: 2/27 = 7.4%
density-note: SHORT-CHAPTER EXEMPTION ACTIVE (27 < 30; modality-count = floor = 2; effective ceiling = max(6%, 2/27) = 7.4%; ADVISORY not blocking)
modalities: smell + sound (2; ≥2 floor met)
per-scene-cap: scene-A=0, scene-B=1, scene-C=0, scene-D=1 (all ≤3)
mode: BLIND

---

sensory:1 @11 smell: shop-ambient -> paper-burning-char
sensory:2 @27 sound: stylus-on-surface-rhythm -> silence

---

## Authoring notes

### Entry defensibility

sensory:1 @11 (cloth-merchant burns the paper — smell:up, spike):
  Proto-line: "the cloth-merchant burns the paper."
  Q1 (bare-word test): "burns" is partially charged (implies fire) but does not self-carry the specific modality of smell — the acrid onset of burning paper/wax in a small enclosed shop is not in the word "burns." The word supplies the act; the modality (smell: the character-onset of char-smoke before it disperses) is not in the language. BARE on smell-modality. Q1 CLEARS.
  Q2 (magnitude test): Paper burned in a small enclosed back-worktable space with a rushlight already burning — the smell-onset of fresh char is a discrete, sudden inflection, not a fine-grain texture. A reader imagining this space would register the smell-onset as a perceptual register-shift at the burn-beat. Q2 CLEARS.
  Audience-side perceptibility: the burn is a physical event at the cloth-merchant's shop rendered through the feed-POV narrative. The smell is real-world perceptible at the burn location; the stitcher renders the shop space through the feed, making the smell accessible to the audience through the scene's rendered environment. Not fauna-feed-extension (the smell does not require Taylor's insect-faculty to exist — it is a physical consequence of the burn that an observer in the room would register; the feed relays what is there). CLEARS.
  Inflection-not-sustained: @11 is the burn-beat; @12 is ash-aftermath (the char has dissipated to settled ash). The smell-onset is the inflection at @11; it does not sustain as a new baseline through @12-@16. CLEARS.
  Old-state anchor: loc-state:2 @8 establishes oc-cloth-merchant-shop with rushlight-lit ambient. The shop-ambient old-state (rushlight-smoke, closed-wood-and-cloth warehouse smell) is the baseline established at @8. No prior sensory fire on smell in this chapter. Old-state: "shop-ambient" (rushlight + fabric/wood scent; the baseline the loc-state establishes for the shop interior).
  Modality cross-check: smell. No loc-state sensory note at @8 or @9 named a smell-event — the old-state is ambient-level, not a prior event. No cross-facet modality-silent-gap violation (the loc-state did not name a smell-event requiring co-citation).

sensory:2 @27 (taylor sets the stylus down — sound:drop):
  Proto-line: "taylor-hebert-kl-122ac sets the stylus down."
  Calibration-anchor precedent: s01e01:24 "the stylus stops on the board" — sound:drop, `sound: stylus-on-wax-rhythm -> silence` — FIRE (ACCEPT; calibration anchor).
  Q1 (bare-word test): "sets the stylus down" is bare on the audible quality. The word does not self-carry the sound of the stylus going still after sustained rhythm. "Silence" is not in the language; the cutoff is not charged. BARE. Q1 CLEARS.
  Q2 (magnitude test): The stylus has been active through scene-A (@5-@7), scene-B (@16), scene-C (@20), and scene-D (@23-@26) — sustained rhythm of an accounting session. The abrupt cutoff at the chapter's terminal bone is a discrete inflection: the rhythm has been present and then is gone. Register-shift magnitude is sufficient. Q2 CLEARS.
  Audience-side perceptibility: the stylus rhythm and its cutoff are universally legible. No fauna-feed-extension required. CLEARS.
  Inflection-not-sustained: @27 is the terminal bone; there are no subsequent beats. The silence at @27 IS the inflection (not the beginning of a new sustained level). CLEARS.
  Old-state anchor: loc-state:5 @22 establishes the-feed-station | end-of-day | accounting-in-motion. The accounting session involves sustained stylus-on-surface writing (ledger entries being closed across @23-@26). The old-state is "stylus-on-surface-rhythm" — the established administrative writing rhythm present across the scene-D arm-close sequence. No prior sensory fire on sound in this chapter; old-state sourced from the accounting-in-motion loc-state baseline (scene-D) + series-established administrative-quiet vocabulary (cf. b01c08 sensory file sound vocabulary).
  Chapter enclosure: scene-map notes the stylus-frame (@5/@6 stylus-in-use at chapter open → @27 stylus-down as chapter close) as "the chapter's enclosure." The terminal sensory fire honors this structural design while remaining rubric-correct.

### Candidate decisions (refused entries)

@1 (Jarvis takes packet — transitional at feed-station):
  No discrete perceptual modality inflection. Transitional movement. REJECT.

@3/@4 (Oswyn presses cart-frame; wool-dyer returns observation — grain-measures junction):
  Feed-relay beats. Audience-side: would require Taylor's insect-faculty to perceive junction activity at distance. Fauna-feed-extension reject. Additionally: no discrete perceptual inflection in the proto-line language that clears Q2. REJECT.

@5-@7 (stylus set / lane-pattern written / stylus lifted — feed-station dexterity):
  @5: transitional; no modality inflection at threshold magnitude. @6: writing sustained — this is not the inflection-beat, merely continuation. @7: "lifts the stylus" IS a potential sound:drop candidate (stylus stops moving). BUT: the stylus is not explicitly making sound during @5-@6; setting it to the source-field is the beginning of writing, not continuation. The distinction from @27 is that @27 follows an extended accounting-in-motion sequence with a clear sustained-rhythm old-state; @5-@7 is the morning's first writing sequence without a prior sound-baseline in this chapter. Borderline, but the magnitude at @7 is lower (the withhold-lift is a physical act, not the terminal close of a multi-hour accounting session). REJECT on Q2 (magnitude insufficient relative to the @27 fire; adding @7 would create two sound-drop events in different scenes, which would require both to independently clear the rubric; @7 does not have the same accumulated-rhythm old-state @27 does).

@11/@12 cross-modal consideration:
  @11 smell FIRES (see above). Additional modality at @11: light (flame from burn) — "burns" charges the light-up event (fire = light-up). Light is charged by "burns." REJECT on Q1 (charged-word redundancy). Thermal at @11: the iron-dish heating — sub-threshold (a paper-burn in a small dish does not produce a room-level thermal inflection an audience would register at distance). REJECT on Q2.
  @12 (iron-dish receives ash — dexterity): tactile candidate (ash settling in dish, warmth of dish). Sub-threshold Q2 (the ash-settling is fine-grain; the dish warmth is below audience experiential threshold for a flag). REJECT.

@13/@14 (insect-feed thermal-shift / smoke-curl — feed-relay):
  FAUNA-FEED-EXTENSION REJECT. Both @13 and @14 require Taylor's insect-faculty to detect: the thermal-shift at the worktable ambient zone and the smoke-curl are perceived through the insects in the merchant's shop. An audience member cannot perceive the thermal-shift or smoke-curl without Taylor's extended-range faculty. Audience-side-perceptibility axis: REJECT.
  NOTE — SEAM-C11-SENSORY-001: The grounding-ledger and /and-review bones priority brief anticipated sensory fires at @13/@14 for the insect-feed thermal/smoke relay. These CANNOT be satisfied by sensory-flags under the fauna-feed-extension rule. The physical materiality of the burn relay must be carried by narrator-interest (where Taylor's feed-perception IS the facet's domain) and by the prose-phase grounding at /and-stitch Phase 4 (voice-embodiment discipline + grounding-ledger license). The sensory-flags facet cannot carry this load without violating its audience-side-perceptibility gate. Flagged for R2 reviewer and showrunner attention.

@16 (taylor marks timestamp — feed-station dexterity):
  Writing-in-place. No discrete perceptual inflection above threshold. The timestamp marking is fine-grain. REJECT.

@17-@21 (soap-lane approach, packet exchange, writing, sealing):
  @17: crossing — movement; no perceptual modality inflection in the cross-lane environment that clears Q2. @18-@21: dexterity chain (delivery, open, write, seal). @21 "seals the packet" — seal-sound candidate. Calibration anchor s01e01:41 (seal-breaks = sound:spike). But here the seal is being APPLIED (sealed), not broken; the wax-seal application sound is sub-threshold compared to a wax-seal break. REJECT on Q2.

### Modality-coverage health-check
  smell + sound = 2 modalities. Floor ≥2 met. No monoculture.
  Distribution: scene-B = 1 (smell @11), scene-D = 1 (sound @27). Two different scenes, two different modalities. Healthy distribution.

### Short-chapter exemption application
  27 bones < 30; modality-count = 2 (floor). Effective ceiling = max(6%, 2/27) = max(6%, 7.4%) = 7.4%. Density = 2/27 = 7.4%. At the exemption ceiling — ADVISORY not blocking. Modality-floor takes precedence over sparsity ceiling; two-modality floor is met; the disambiguation-gradient is intact (2 fires on 27 bones preserves strong contrast against unflagged baseline).

### Flagged seams for R2
  SEAM-C11-SENSORY-001 (see above): @13/@14 anticipated grounding cannot be delivered by sensory-flags. Narrator-interest + prose-phase grounding must carry the insect-feed thermal/smoke physical materiality.
  SEAM-C11-SENSORY-002: sensory:2 @27 old-state "stylus-on-surface-rhythm" has partial old-state lineage (no prior sensory-fire on sound in this chapter; sourced from loc-state:5 accounting-in-motion baseline + series vocabulary). R2 reviewer should confirm this anchoring is sufficient or flag for a loc-state sensory-note addition at @22 that would formally establish the writing-rhythm as a named condition.
