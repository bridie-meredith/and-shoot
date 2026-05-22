---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 2
episode: b01c02
date: 2026-05-21
verdict: accept
---

# Verdict reasoning

Cycle-1 finding: both old-states unanchored. Fix added conditions notes to loc-state:2 @4 (anchor for sensory:1) and loc-state:11 @22 (anchor for sensory:2). I hold both files open and re-walk the lineage for each entry.

**sensory:1 @7** — old-state: `watch-press-alley-ambient`. New-state: `watch-column-footfall`.

Cycle-1 finding: no loc-state sensory/conditions note in entries @2-@6 established this ambient baseline. The fix: loc-state:2 @4 now carries a conditions note — "ambient-sound baseline before column arrival — ordinary morning street noise and shoe-leather on cobbles; no column-echo yet; this is the watch-press-alley-ambient state (anchor for sensory:1 old-state)."

Lineage walk: loc-state:2 is at @4. sensory:1 fires at @7. The loc-state:2 conditions note names `watch-press-alley-ambient` explicitly and marks it as the anchor for sensory:1 old-state. The derivation is now direct — the conditions note establishes the ambient sound level at @4 and the sensory entry fires at @7 (three beats later, same location, same morning). The inheritance does not skip; no intervening loc-state changes the sound level between @4 and @7.

Cross-check: loc-state:3 @5 is a lane-mouth entry (insect-density sealing exits); it concerns spatial geometry, not ambient sound. loc-state:4 @6 names Wren's figure at the far threshold. Neither entry introduces a sound-level change that would invalidate the @4 ambient baseline at @7.

The old-state `watch-press-alley-ambient` now traces to loc-state:2 @4 conditions note. Lineage: verified. PASS.

**sensory:2 @23** — old-state: `unlit-lodging-interior`. New-state: `lamp-lit-tight-radius`.

Cycle-1 finding: no loc-state entry between @17 and @22 covered the lodging interior in its pre-lamp state. Fix: (a) loc-state:11 @22 now carries a conditions note — "interior-darkness baseline before @22 — lodging-interior unlit, night scene-open (time-skip blank @21); this is the unlit-lodging-interior old-state (anchor for sensory:2 old-state at @23)"; (b) sensory:2 anchor relocated from @22 to @23.

Lineage walk: the conditions note on loc-state:11 @22 establishes `unlit-lodging-interior` as the pre-lamp darkness baseline. The note explicitly ties this to the time-skip blank at @21 — the interior has been dark from scene-open (night). sensory:2 fires at @23, the beat after the lamp-lighting. The conditions note describes the state that held before @22's lamp event; sensory:2 at @23 is the first authored bone under the post-lamp condition, using the pre-lamp darkness as old-state.

This is a subtle inheritance: the old-state `unlit-lodging-interior` is the state that obtained before @22 (the lamp-lighting bone), referenced by an entry anchored at @23. The conditions note on loc-state:11 explicitly frames it as "interior-darkness baseline before @22" — exactly the period sensory:2's old-state claims. The lineage holds.

Does the relocation to @23 introduce a new concern? The delta `light: unlit-lodging-interior -> lamp-lit-tight-radius` fires at @23 (`opens the ledger`), not at @22 (`lights the lamp`). The light change itself happened at @22. The sensory flag at @23 is not firing on the moment of change but on the first bone under the changed state. I check whether this creates a lineage mismatch: sensory:2's old-state is `unlit-lodging-interior` (the pre-lamp state) and new-state is `lamp-lit-tight-radius` (the post-lamp state). The entry describes the transition even though the flag fires one beat after the transition. This is a timing-note concern, not a lineage-contradiction concern — the old-state and new-state are both loc-state-anchored, and the relocation rationale (avoiding action-verb self-charge at @22) is sound. The cross-facet contract is satisfied.

Modality-continuity check: sound modality was established at sensory:1 @7. sensory:2 is on light modality — different channel, no prior-sensory-on-same-modality to chain from. The old-state must trace to loc-state, which it now does via the conditions note. No chain-skip.

Both old-states now have verifiable loc-state lineage. File passes my axis.

# Entry-level callouts

None. Both old-state lineages now trace cleanly.

Cycle-1 findings resolved:
- `[sensory:1] @7 unanchored` → resolved by loc-state:2 @4 conditions note naming `watch-press-alley-ambient` as anchor.
- `[sensory:2] @22 unanchored` → resolved by loc-state:11 @22 conditions note naming `unlit-lodging-interior` as pre-lamp baseline, plus relocation to @23 where the anchored old-state is correctly inherited.

No new lineage seams from the relocation or from the conditions note additions.

# Convergence trace

- sensory:1 old-state anchor: cycle-1 finding covered no auditor detection. Fix-log item 8b confirms loc-state:2 @4 conditions note landed first (A3 sequence) before sensory entry updated. The A3 sequencing requirement (upstream edit before sensory ADD) is the protocol the rubric V3 §14 mandates; satisfied here.
- sensory:2 relocation and anchor: cite-index updated — sensory:2 now at @23, co=[exposition:5, state:5]. loc-state:11's co-citations updated to remove sensory:2 (it no longer co-locates at @22). The structural update is consistent with the lineage claim.
- URI-FACETS-CYCLE-1 pattern (unanchored old-state HARD): both instances of the pattern from cycle-1 are resolved. The fix followed the rubric §Axis-1 prescribed resolution: "backfill the loc-state baseline." Conditions notes are the correct backfill vehicle for baselines that predate the beat without requiring a full loc-state entry at the anchor.
