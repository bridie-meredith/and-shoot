---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 2
episode: b01-c07
date: 2026-05-31
verdict: accept
---

# Sensory Old-State Reader — Cycle 2 Verdict

## Live-read pass — per-entry lineage walk

### sensory:1@12 — sound: halvard-pastoral-account-register -> halvard-direct-address

Cycle-1 callout: old-state had no loc-state baseline; unanchored.

Fix applied: loc-state:3@9 now carries an explicit sensory field — "sound: halvard-pastoral-account-register (ongoing; sick-child account, low-register pastoral counsel, corner ambient)." The old-state name `halvard-pastoral-account-register` matches verbatim the loc-state:3@9 field value. The anchor annotation `old-state-anchor: loc-state:3@9` is present in the sensory file.

Lineage walk: @12 falls after loc-state:3@9 (which establishes the sound baseline at the passage-open beat). No intervening loc-state entry between @9 and @12 on sound. Inheritance chain unambiguous. Old-state traces directly to loc-state:3@9 by exact name match. CLOSED.

### sensory:2@17 — tactile: sept-corner-stone-firm -> sept-corner-cobble-grip

Cycle-1 callout: old-state `passage-lane-packed-earth` reached past the governing stone; cycle-1 fixer corrected to `sept-corner-stone-firm` with anchor `loc-state:4@15`.

loc-state:4@15: "sept-corner stone underfoot — the ground cold grips through the soles at the planted weight." The old-state name `sept-corner-stone-firm` is near-verbatim from "stone underfoot" — specific enough to distinguish from packed earth or other surface types. @17 follows @15 (loc-state:4 establishes ground condition at the planting beat). Inheritance chain: loc-state:4@15 → sensory:2@17. No ambiguity; no intervening loc-state entry on tactile modality. Old-state correctly reads the stone-underfoot baseline. CLOSED.

### sensory:3@16 — thermal: sept-corner-held-cold -> halvard-breath-in-cold-air

No explicit `old-state-anchor:` annotation in the file for sensory:3.

Beat @16 falls between loc-state:3@9 (passage-open; "cold-holding ground unwarmed — the sept-side stone holds the night cold past the morning light shift") and loc-state:4@15 (planted weight). The most recent prior loc-state at @16 is loc-state:3@9. Its description explicitly establishes the thermal baseline: "cold-holding ground unwarmed," "sept-side stone holds the night cold." The old-state name `sept-corner-held-cold` maps closely to "cold-holding ground unwarmed" — same location, same held-night-cold condition.

No anchor annotation is present. This is a mild deficiency in documentation, but the lineage is legible and unambiguous: loc-state:3@9 is the governing entry, the thermal baseline is named there, and the old-state correctly names it. The lack of an explicit `old-state-anchor:` field does not constitute an unanchored-baseline finding when the loc-state establishes the condition explicitly and the derivation is clear. I read the lineage; it closes.

Delta coherence: old-state is environmental cold at the corner; new-state is Halvard's breath becoming visible in that cold — a discrete transient vapor event (tag: spike). The delta does not swap modalities; it names the same thermal environment becoming perceptible in the exhale. Direction is coherent.

No finding here.

### sensory:4@22 — pressure: sept-corner-stone-firm -> heel-settles-cobble-edge

Cycle-1 callout: old-state invalid (loc-state:4@15 governs stone, not passage-lane packed earth — this was already corrected from the `passage-lane-packed-earth` error in sensory:2; sensory:4 also needed old-state correction).

Fix applied: old-state-anchor: loc-state:4@15; old-state name: `sept-corner-stone-firm`.

@22 falls after loc-state:4@15 (last loc-state entry before loc-state:5@23). The governing baseline is loc-state:4@15: "sept-corner stone underfoot." `sept-corner-stone-firm` correctly names the stone-underfoot condition. No intervening loc-state entry between @15 and @22 for pressure modality. The heel settling against the cobble edge at @22 is a discrete event on the same stone the loc-state established. Old-state derives from loc-state:4@15 without invention. CLOSED.

## Convergence trace

- sensory:1@12 old-state closure: cycle-1 callout (unanchored) closed by loc-state:3@9 sound field add + explicit anchor annotation.
- sensory:2@17 old-state closure: cycle-1 callout (wrong baseline) closed by correction to sept-corner-stone-firm + loc-state:4@15 anchor.
- sensory:4@22 old-state: new anchor introduced at cycle 2, anchored correctly to loc-state:4@15.
- sensory:3@16: no prior callout on this entry from this reviewer; no anchor annotation, but lineage is derivable and unambiguous — not flagging.

## Verdict

ACCEPT. All cycle-1 old-state callouts are closed. No new baseline-invention or contract-break findings. The loc-state anchoring across all four entries is now traceable.
