---
reviewer: sensory-modality-coverage
facet: sensory
chapter: b01c08
cycle: r1
verdict: accept
generated: 2026-05-31
auditor-overlap: none (Phase 5 auditor report not present at dispatch time; adversarial read is independent)
---

# Sensory Modality Coverage — b01c08 Adversarial Verdict

## File inventory

| entry | anchor | modality | old-state | new-state | tag | scene |
|-------|--------|----------|-----------|-----------|-----|-------|
| sensory:1 | @10 | sound | feed-station-working-quiet | wax-seal-crack | spike | B |
| sensory:2 | @16 | light | afternoon-stone-lane-light | evening-lane-dusk-fall | down | C (open) |

Total entries: 2. Bone count: 24. Distinct modalities: 2 (sound, light). Sparsity: 2/24 = 8.3%.

---

## Modality-floor check

Floor ≥2 modalities: MET. Sound + light. Cross-modal coverage cleared at minimum.

---

## Dominance-ceiling check

Only 2 entries total. Ceiling (no single modality ≥67% when total ≥3) is n/a by entry count. Each modality is 50% of fires. No dominance violation possible.

---

## Sparsity check

8.3% exceeds the nominal 3–6% ceiling. However: bone_count = 24 < 30 AND modality count = 2 (the floor). The V3 short-chapter floor-vs-ceiling exemption applies directly. Effective ceiling = max(6%, 2/24) = max(6%, 8.3%) = 8.3%. The exemption permits exactly this configuration. Sparsity is at the exemption boundary — not above it, not advisory-flagging territory beyond what the exemption already absorbs.

**Sparsity: EXEMPT, not blocking.**

---

## Distribution check — scene-level

Scene-A (@1–@8, lane-junction + hook-ward, afternoon): zero fires.
Scene-B (@9–@15, feed-station, afternoon): one fire (sensory:1 @10, sound spike).
Scene-C (@16–@24, hook-ward, evening): one fire (sensory:2 @16, light down).

**Scene-A silence — is it defensible?**

The dispatch brief flags this as the question to attack. My read:

Scene-A is a circuit-read pass at the lane-junction and surrounding ward positions. The location-state entry @1 notes the hill's stone skirt cutting the view at the junction — this is a spatial/geometric observation, not a perceptual inflection event. The language ("cuts the view") is structural description of sightline geometry, not a charged perceptual register-shift. The loc-state entry does not assert a discrete perceptual event (no thermal release, no audible-texture change, no smell-onset). It asserts a persistent environmental constraint.

Under the rubric: loc-state holds sustained sensory level; sensory-flags holds inflection on top of that level. The loc-state:1 hill-skirt note is a sustained-level architectural fact, not a delta. No modality inflection-event is asserted or implied. The question is whether any scene-A bone independently earns a fire the author skipped.

Working through scene-A bones:
- @1: taylor enters the lane-junction. Entry is bare. Is there a perceptual inflection at entry? The scene-map notes "circuit-start" and "lane open." Entry into an afternoon lane junction is not asserted as a sensory register-shift — no lamp-lighting, no weather-change, no audible rupture. The afternoon-lane ambience is baseline, not inflection. REFUSE — no discrete modality event.
- @2: insect-feed returns the chandler-corner. Interior-faculty event (feed-return). No environmental sensory modality changes out there. REFUSE — fauna-feed-extension territory at best; interior-only.
- @3–@4: watcher-boy faces water-point; basket-woman faces lane-mouth. Positional observations. No perceptual modality inflection attached. REFUSE.
- @5: apprentice drops the nailing-rate. A nailing-rate drop is not a sensory-flag event; it's a social-signal. If the nailing sound itself is dropping, that is a sound inflection candidate — but "drops the nailing-rate" reads as a social/economic observation (the apprentice is not hammering as fast), not a literal sound-delta the audience would register. Per bare-word + magnitude tests: the language is bare BUT the audience experiential threshold for a nailing-rate drop (as opposed to a nailing-stop or a sudden silence) is sub-threshold. Cumulative-drift, not discrete inflection. REFUSE — magnitude-insufficient.
- @6: taylor traces the watcher-sightlines. Cognitive/interior action. No environmental perceptual change. REFUSE.
- @7: insect-feed delivers the gap-corridors. Interior-faculty. REFUSE.
- @8: the circuit closes the feed-pass. Cognitive closure. No perceptual modality change. REFUSE.

Scene-A silence verdict: every bone either presents no perceptual modality change, or presents a magnitude-insufficient or interior/fauna-feed candidate. The hill's stone skirt in loc-state:1 is a sustained-level architectural fact, not a firing-eligible inflection. **Scene-A zero-fire is correct. No silent-gap.**

---

## Scene-B distribution — sensory:1 @10

One fire on the seal-break at the feed-station. Scene-B is 7 bones (@9–@15). One fire at 14.3% of scene bones is within per-scene frugality — the 3-entry cap is honored. The sound spike at seal-break is the appropriate high-magnitude discrete event in a flat-tense logistics scene. No modality saturation. **Distribution: appropriate to scene-B's flat-tense rhythm-shape.**

---

## Scene-C distribution — sensory:2 @16

One fire at scene-open — the afternoon-to-evening light transition. Scene-C is 9 bones (@16–@24). One fire at 11% of scene bones is within per-scene frugality. The light:down fire at the scene-open (@16) marks the structural transition that the scene-map explicitly encodes as "evening (return circuit pass)." The dusk-fall is the environmental registration the scene-C location change earns. **Distribution: appropriate to scene-C's rising-to-quiet-peak rhythm-shape.**

---

## Location palette check

Scene-A: outdoor lane, afternoon. Palette: sound (ambient lane-noise, nailing, ward activity), light (afternoon sun), thermal (ambient), tactile (stone underfoot). The palette has candidates but no discrete inflection fires earned (per per-bone analysis above). The scene is a circuit read — low-event, observation-pass. Consistent with a zero-fire scene.

Scene-B: indoor feed-station. Palette: sound (working-quiet baseline, seal-break spike), light (indoor/ambient), smell (possible — wax, paper). The sound spike at @10 correctly anchors to the working-quiet indoor baseline. No indoor light-transition or smell-onset is asserted in the scene. Palette appropriately covered by one sound fire.

Scene-C: outdoor hook-ward, evening. Palette: light (dusk-fall), sound (evening ambient vs. afternoon), thermal (evening cooling). The light:down fire at @16 captures the transition the scene-map asserts as "evening." Evening versus afternoon sound-ambient is not asserted as a discrete inflection event (no onset or spike — just baseline shift, which belongs in loc-state). **No silent-gap in scene-C.**

---

## Hot-button inventory (per card)

- One modality dominating (>50%): NO. Sound: 1, light: 1. Even 50/50 split.
- Major modalities absent that the location palette should carry: BORDERLINE. The outdoor scene-A has no sound/thermal fire, but none is earned (no discrete inflection events). The feed-station scene-B has no smell fire, but the working-quiet / wax-crack pair is dominant and no smell-onset is asserted. Not a silent-gap — a correct silence.
- Sparsity out of 3–6% band: YES, 8.3% — but V3 exemption absorbs this. Not a live flag.
- Per-modality density imbalanced within a scene: NO. Both fires are in different scenes; no per-scene accumulation.
- No fires on key environmental beats (lamp-lighting, candle-catching, weather-change): the afternoon-to-evening transition IS fired at @16. No lamp-lighting or candle events in this chapter. The weather is static (no rain, no wind onset). **No inflection-skip on environmental beats.**

---

## Convergence-trace notes

No auditor Phase 5 report was present at dispatch time. Independent adversarial read only. No overlapping finding IDs to trace.

The carve-out preamble in the facet file is noted: both old-states are sourced from carve-out authority (series-established vocabulary for feed-station-working-quiet; scene-map time-of-day assertion for afternoon-stone-lane-light). The carve-out validity is out-of-scope for this reviewer (old-state lineage is the sensory-old-state-reader's domain). I do not attack old-state sourcing.

---

## Verdict

`accept`

**Rationale (card-register):**

2 modalities, 2 entries, 24 bones. Sound + light — the split is clean. The scene-B sound-spike at the feed-station is the right fire in the right scene; the scene-C light-down at scene-open catches the dusk-fall that the scene-map asserts as a structural fact. Scene-A silence is earned — every scene-A bone is either interior, fauna-feed, magnitude-sub-threshold, or sustained-baseline. The hill's stone skirt in loc-state:1 is architectural geometry, not a perceptual inflection event; a fire there would be sustained-as-inflection anti-pattern.

The 8.3% sparsity is the V3 exemption activating cleanly: bone_count 24 < 30, modality count = floor (2), arithmetic collision absorbed. No dominance problem. No silent-gap on environmental inflection beats. No modality saturating. The file reads two-channel but the chapter is 24 bones with three lean scenes — two-channel is the correct texture for this volume. I would push for a third modality on a longer chapter (outdoor thermal or feed-station smell would be natural candidates), but this chapter's event-load does not generate a third earned inflection.

The file as a whole is sparse and clean. It does not oversell. In a chapter where Taylor does not make anything happen — she reads the ward, reads the packet, reads Oswyn — the sensory file registering exactly two discrete perceptual events is the correct weight. The disambiguation gradient is intact. This file earns its fires and keeps its silence.
