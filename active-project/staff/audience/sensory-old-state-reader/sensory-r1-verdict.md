---
reviewer: sensory-old-state-reader
facet: sensory
episode: b01c01
cycle: r1
verdict: accept
date: 2026-05-19
---

## Per-entry old-state lineage readings

Cross-reference inputs: sensory.md (3 entries), location-state.md (6 entries), proto-lines b01-c01.md, cite-index.

---

### [sensory:1] @1 — smell: hook-alley-ambient -> tallow-smoke-room-density

**Lineage trace:**

Most recent prior loc-state at @1: loc-state:1 @1 — "flea-bottom | morning | none | corner-room-threshold | the alley-mouth narrows to a doorway here; the step in is the only gap between street and work-floor."

Old-state field: `hook-alley-ambient`. Does this trace to loc-state:1?

loc-state:1 places Taylor at the corner-room-threshold — she is crossing from alley to interior at this exact beat. The threshold description ("the alley-mouth narrows to a doorway") establishes the "from" side as the Hook alley. loc-state:1 does not name an alley smell explicitly, but it is a transition beat: the old-state is the sensory environment of the location Taylor is leaving (the Hook alley) at the moment she crosses. The entry fires on the crossing beat itself, so the old-state is the alley-side baseline at entry.

The loc-state does not contradict `hook-alley-ambient`. No prior loc-state entry names the alley as having a different smell (or any smell). The baseline is not invented against a contradicting loc-state; it is the natural implication of the entry/exit threshold. This is at the edge of strong-lineage (no explicit loc-state smell field for the alley side), but the transition structure of loc-state:1 supports it.

Delta direction: hook-alley-ambient → tallow-smoke-room-density. Moving from open alley to enclosed workshop is a plausible olfactory direction. loc-state:1's "step in is the only gap between street and work-floor" explicitly marks the crossing. The new-state (tallow-smoke-room-density) is consistent with a working-room interior environment.

**No cross-facet contract break detected. Lineage: traceable by transition structure of loc-state:1. ACCEPT.**

---

### [sensory:2] @9 — sound: corner-room-interior-quiet -> hook-street-noise-entering

**Lineage trace:**

Most recent prior loc-state at @9: loc-state:2 @9 — "flea-bottom | morning | none | door-open-street-facing | the Hook visible through the facing side; the near-alley foot-traffic readable from the threshold without stepping out."

Old-state field: `corner-room-interior-quiet`. Does this trace to loc-state:1 (the baseline before @9)?

The room's prior sound state must be derived from loc-state:1 @1, which established `corner-room-threshold` in the morning with no conditions named. Crucially, loc-state:3 @11 explicitly back-references this: "the alley at its loudest registered density of the day; distinct from the morning quiet of @1." That back-reference confirms that `morning quiet` was the established sound-baseline at @1, making it the correct old-state for the @9 sound fire.

The lineage is: loc-state:1 establishes morning interior state → loc-state:3 (later) explicitly names that state as "morning quiet of @1" → sensory:2's old-state `corner-room-interior-quiet` matches. The chain is verifiable cross-facet.

New-state: `hook-street-noise-entering`. loc-state:2 @9 says "door-open-street-facing" and "near-alley foot-traffic readable from the threshold." The new-state is grounded: an open door facing the Hook means street sound enters. The delta direction is coherent with the loc-state description.

**Cross-facet contract intact. Lineage: strong (explicitly confirmed by loc-state:3's back-reference to "morning quiet of @1"). ACCEPT.**

---

### [sensory:3] @15 — sound: hook-street-ambient -> watch-column-passing # tag: spike

**Lineage trace:**

Most recent prior loc-state at @15: loc-state:5 @15 — "flea-bottom | afternoon | none | hook-mouth-visible | the Watch column passes at the Hook's curve — visible from the corner-room's street-facing side at the angle Coll opened in @9."

Old-state field: `hook-street-ambient`. Where does this come from?

The sound modality's prior sensory entry is sensory:2 @9 with new-state `hook-street-noise-entering`. After the @9 spike (door opens, street sound enters), the sustained sound level in the room becomes the street ambient of the Hook. Sensory:3's old-state `hook-street-ambient` inherits from sensory:2's new-state — the street noise that entered at @9 settled into an ambient level that persists through @11-@14 (loc-state:3 at @11 names this: "working-hour noise through the wall — the alley at its loudest registered density of the day"). The @15 old-state `hook-street-ambient` is consistent with the sound level established at @9 and confirmed in loc-state:3.

The inheritance chain does not skip: sensory:2 new-state → ambient carry through @10-@14 → sensory:3 old-state. loc-state:3 @11 anchors the ambient level in between. No contradiction.

New-state: `watch-column-passing`. loc-state:5 @15 explicitly names the Watch column as the event at this beat. The new-state matches the loc-state event exactly.

**Cross-facet contract intact. Lineage: clear inheritance from sensory:2 new-state, confirmed by loc-state:3 ambient-carry at @11. ACCEPT.**

---

## Cross-facet contract summary

| Entry | Old-state source | Contradiction? | New-state grounded? |
|-------|-----------------|----------------|---------------------|
| sensory:1 @1 | loc-state:1 (threshold transition) | None | Yes (interior workshop) |
| sensory:2 @9 | loc-state:1 + loc-state:3 back-ref | None | Yes (loc-state:2 open door) |
| sensory:3 @15 | sensory:2 new-state + loc-state:3 | None | Yes (loc-state:5 Watch column) |

No unanchored entries (all have traceable loc-state priors). No baseline inventions. No frame mismatches. No delta-with-swapped-modality.

## Convergence with auditor findings

- FB-002 (density breach, SIGNAL) does not touch old-state correctness. My scope is orthogonal.
- The auditor's r2 verify Earth-Bet fence scan cleared sensory entries — no sensory-specific finding. Consistent with my read.

## Verdict

**accept**

All three old-state fields trace to verifiable loc-state baselines. No cross-facet contract breaks, no invented baselines, no frame mismatches. The sensory delta chain (alley→interior at @1; quiet→street-noise at @9; ambient→column-spike at @15) follows the loc-state inheritance sequence without gaps or contradictions.
