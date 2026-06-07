---
reviewer: sensory-modality-coverage
facet: sensory
cycle: 1
episode: b01-c07
date: 2026-05-31
verdict: accept
---

# Sensory Modality Coverage — b01-c07 — Cycle 1 Verdict

## File-level tally

| modality | entries | anchors |
|----------|---------|---------|
| sound    | 1       | @12     |
| tactile  | 1       | @17     |
| thermal  | 2       | @16, @22 |
| **total** | **4** | — |

Distinct modalities: 3 (sound, tactile, thermal). Thermal fires twice.

Density: 4/25 = 16%. Entries 1+2 at 8%; entries 3+4 carry licensed-grounding-exception grd-001/grd-002. Density-cap attack is foreclosed by the ledger exemption — not considered.

---

## Modality-coverage assessment

**Is 3 modalities adequate?** Yes. The rubric floor is ≥2; the card's taste ceiling is ≥3-4 for a textured read. This file delivers 3. That passes coverage cleanly, not at the floor.

**Is thermal-twice a monoculture risk?** Tally: sound=1, tactile=1, thermal=2. Thermal is 50% of entries. That sits at the hot-button threshold ("one modality >50% → strong flag"). But the tally is 2-of-4, not 2-of-2. If the file were thermal-only or thermal-dominant by larger margin, I would flag. At 50% across four entries, with the two remaining entries covering two distinct non-thermal modalities, the distribution is skewed but not monoculture. The file does not read single-channel: sound at the dialogue-pivot (@12), tactile at the ground-contact beat (@17), and thermal twice at the exhale and the held-stand. Three distinct sensory textures come off this file. I am not flagging thermal-dominance as a coverage problem here.

**Do the two thermals collapse together?** This is the load-bearing question. The dispatch explicitly arms it.

- sensory:3 @16 — thermal: sept-corner-held-cold -> halvard-breath-in-cold-air. The inflection is the exhale becoming visible — a vapor-puff in the cold-saturated stone corner. It is primarily a thermal-visual event: the breath registers as cold-made-visible. Old-state anchored to loc-state:3@9 (cold-holding ground; unwarmed stone). Bone: "septon-halvard-flea-bottom exhales." Subject is Halvard. The cold is what the exhale reveals; it is an outward-facing registration of the ambient cold through Halvard's body. Spike-class: transient (the vapor-puff appears and dissipates).

- sensory:4 @22 — thermal: sept-corner-stone-cold-underfoot -> cold-settled-through-standing-weight. The inflection is cold that has transferred upward through the soles over the duration of the argument, re-registering as the feet are deliberately replanted against the departure impulse. Old-state anchored to loc-state:4@15 (stone underfoot cold grips through soles at planted weight). Bone: "taylor-hebert-kl-122ac steadies the feet." Subject is Taylor. The cold is what the ground has pressed into the body over time — an accumulated thermal load re-registered at a moment of stillness. Up-class: sustained increase (cold-transfer, not transient).

These two do not collapse. Three distinct axes of separation:

1. **Subject.** @16 is Halvard's exhale; @22 is Taylor's feet. Different bodies.
2. **Mechanism.** @16 is exhalation-into-ambient-cold (breath meeting air, out to in). @22 is contact-load-transfer (stone pressing cold upward through soles, in to surface). Different thermal physics.
3. **Class.** @16 is spike (transient event); @22 is an accumulated-transfer re-registration that reads up (new state replaces old state with the charged version). Different inflection shapes.

The grounding-ledger's own note at grd-002 flags the differentiation requirement ("must NOT duplicate sensory:2@17's cobble-grip token — differentiate the modality or the locus") and confirms the authors executed it: "thermal modality; content=temperature-transfer vs. @17's surface-texture. Distinct." The ledger's self-check validates what the text demonstrates.

**Is there a silent-gap violation?** Loc-state must be checked for sensory-note events that lack a corresponding sensory flag. The auditor's CLASS 5 CONTRADICTION confirms loc-state:3@9 and loc-state:4@15 are the relevant baseline anchors. Neither loc-state entry appears to assert a standalone sensory-event note that goes unflagged (the cold-holding stone is baseline ambient; the sensory flags are the inflection deltas on top of it). No cross-facet silent-gap found. The loc-state ↔ sensory contract is satisfied.

**Is there a location-palette mismatch?** The card asks: do modality choices suit the location's natural sensory palette? oc-sept-corner is a cold, stone, passage-corner in Flea Bottom — outdoor or near-outdoor urban lane geometry, cold-holding stone, tallow-and-wax ambient smell (auditor's constraint check confirms this from the warehouse card). The palette expectation would carry: thermal (stone cold), tactile (ground surface), sound (lane ambient + voices), possibly smell (tallow-wax). This file covers thermal and tactile directly, and sound at the dialogue-pivot. The palette match is good. No palette silent-gap: tallow-wax smell is the one absent palette element; given 25-bone density constraints and the waived cap, the absence is defensible — the argument-scene is not a smell-forward beat, and forcing a smell entry to round out the palette at this density level would be anti-pattern inflation.

**Pressure-signal correlation (observation only, not gating).** Sound@12 fires on a peak-shadow-class bone (auditor confirms: "sensory:1@12 … scene-B peak-shadow bone"). Tactile@17 fires at a scene-B bone inside the rising-to-peak span. Thermal@16 and thermal@22 fire at scene-B/@16 and scene-C/@22, both in rising-or-peak contexts. Correlation is positive and internally coherent; all fires are in charged zones. No inflection-not-sustained violations visible at this distribution.

---

## Callouts

None. The file has no modality problem this lens can mount a defensible attack on.

The thermal-twice question was the only live seam. Both entries are genuinely distinct. The distribution is slightly skewed toward thermal, but at 3 distinct modalities across 4 entries on a 25-bone chapter with two ledger-licensed grounding adds, skew is expected and defensible. The location's palette is well-served. No silent-gap, no monoculture, no single-channel read.

---

## Convergence trace

- Auditor fault-003 (sensory FREQUENCY-BAND SIGNAL): addressed under exemption; not a content-coverage finding. Convergence: N/A (exemption blocks the attack).
- Auditor fault-003 notes "entries 3+4 are waived" — supports my accept on density.
- Auditor CLASS 8 CONSTRAINT: per-scene cap for Scene-B = 3 (exactly at cap). Confirmed. This lens does not attack per-scene caps (that's per-entry, not file-level distribution).
- Auditor CLASS 7 SUPERFLUOUS: sensory:3@16 confirmed not superfluous. Supports accept.
- Grounding-ledger grd-001/grd-002: both satisfied, both entries confirm distinct modalities and mechanisms. Supports accept on thermal-twice question.

---

## Verdict

**ACCEPT.**

3 distinct modalities across 4 entries. Thermal fires twice but the two entries are subject-distinct, mechanism-distinct, and inflection-class-distinct — they do not collapse. Location palette covered. No silent-gap. No monoculture.
