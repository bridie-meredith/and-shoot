---
reviewer: sensory-old-state-reader
facet: sensory
cycle: 1
episode: b01c01
date: 2026-05-19
verdict: revise
---

# Verdict reasoning

Two of three entries carry old-states with no explicit sensory baseline in the governing loc-state. loc-state:1 @1 describes a physical threshold; it names no smell field for the alley exterior. loc-state:1 and loc-state:2 @9 name spatial orientation and visibility; neither names an interior sound-baseline. The old-states for sensory:1 and sensory:2 are inferences from location type, not traceable to any stated loc-state sensory field. That is the baseline-invention failure mode, even when the inferences are plausible.

# Entry-level callouts (revise / fail only)

- [sensory:1] @1 — old-state `hook-alley-ambient` has no loc-state lineage for smell. loc-state:1 @1 reads: "the alley-mouth narrows to a doorway here; the step in is the only gap between street and work-floor." It names geometry, not olfactory state. No loc-state entry at or before @1 establishes an alley smell baseline. `hook-alley-ambient` is invented for this entry; the smell old-state cannot be derived from any loc-state field. Studio's loc-state needs a sensory note for the Hook-alley exterior baseline, or this entry's old-state is unsupported. Flag back to studio.

- [sensory:2] @9 — old-state `corner-room-interior-quiet` has no loc-state lineage for sound. The governing loc-state entries at or before @9 are: loc-state:1 @1 (geometry, no sound field) and loc-state:2 @9 (door-open-street-facing, no prior-state sound field). loc-state:3 @11 retroactively names "morning quiet of @1" but fires at @11 — it is downstream, not an anchor for @9's old-state. The old-state `corner-room-interior-quiet` at @9 is not derivable from any explicit loc-state sensory field at or before @9. The naming is plausible but unanchored by explicit loc-state text. Flag back to studio for a sensory-note addition to loc-state:1 naming the interior-quiet baseline.

# Convergence trace (orchestrator-critic input)

- Neither callout converges with any Phase 5 auditor finding. The r1 and r2-verify reports do not surface old-state-lineage issues for sensory:1 or sensory:2; the auditor's cross-facet contract check passed both. My callouts are original to this review, attacking the gap between "plausibly implied baseline" and "explicitly stated loc-state baseline" — a seam the mechanical scan's loc-state-contradiction check does not cover (it looks for contradiction, not for absence of explicit anchoring).
- sensory:3 @15 is not called out. Its old-state `hook-street-ambient` inherits from sensory:2's new-state `hook-street-noise-entering` — the rubric explicitly permits old-state sourcing from a prior sensory entry on the same modality. The inheritance chain is visible even if the label shifts from inflection-description to settled-state-description.
