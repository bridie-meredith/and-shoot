---
reviewer: sensory-old-state-reader
chapter: b01-c05
facet: sensory
cycle: r1
timestamp: 2026-05-28
verdict: revise
entries-reviewed: 2
entries-flagged: 1
entries-clean: 1
auditor-findings-consulted: pass-039, signal-006 (for completeness; not load-bearing here)
---

# Sensory Old-State Reader — b01-c05 R1 Verdict

## Entry-level review

### [sensory:1] @4 `tactile: lane-stone-surface-baseline -> provisioner-cart-load-on-stone`

verdict: ACCEPT

Lineage walk:
- Anchor: @4 (`the provisioner-train crosses the junction`)
- Location: oc-rushwick (scene-A, junction)
- Most recent prior loc-state entry: loc-state:1 @1 — "cool-damp stone underfoot; overnight damp still in the paving; stone skirt holds shade at the lane-mouth"
- Old-state `lane-stone-surface-baseline` traces directly to loc-state:1 @1. The composite name captures the stone-underfoot + paving baseline established there. No modality mismatch: loc-state:1 names a tactile surface condition ("cool-damp stone underfoot"); the sensory entry's old-state is the tactile register of that same surface. Delta direction (ambient stone-surface → cart-loaded-stone) is consistent with what the provisioner-train crossing would produce.
- No invention; no contradiction; no frame mismatch.

The dispatch's stated attribution "old-state from loc-state:1 @1 (stone skirt at grade)" is confirmed. Lineage intact.

---

### [sensory:2] @13 `sound: alley-stone-contained-silence -> courier-effortful-body-sound`

verdict: REVISE

Lineage walk:
- Anchor: @13 (`the three figures pin the courier`)
- Location: oc-rushwick, side-alley interior
- Most recent prior loc-state entries at @13: loc-state:6 @12 ("alley-mouth sealed by two bodies at its full width; alley-mouth width is the containment fact") and loc-state:5 @11 ("one-person-wide stone passage off the east exit; rough original-construction walls, uneven floor")
- Old-state: `alley-stone-contained-silence`

**Attack 1 — wrong ID in stated attribution.**
The dispatch attributes this old-state to "loc-state:7 @11 (alley-interior contained)." loc-state:7 fires @20, not @11 — that is the alley-exit entry ("alley-mouth open; three figures have cleared to the east"). loc-state:5 fires @11. The attribution carries the wrong ID number. The old-state, if it has lineage at all, traces to loc-state:5 @11 — not :7. The stated cite is broken.

**Attack 2 — no sound level named in any prior loc-state entry.**
Neither loc-state:5 @11 nor loc-state:6 @12 names an auditory baseline. loc-state:5 establishes the spatial description: "rough original-construction walls, uneven floor." loc-state:6 establishes containment geometry: "two bodies at the mouth control all egress." Neither says silence. Neither carries a §sensory or §sound note. The old-state `alley-stone-contained-silence` names a modality (sound) and a level (silence) that no loc-state entry explicitly establishes for the alley interior. The silence baseline is inferred from enclosed-stone geometry — not sourced from loc-state's auditory content.

The oc-rushwick.card.md §Hazards does independently corroborate this inference ("a low, effortful sound from a body inside a side alley does not reach the junction"), but §Hazards is a location-card field, not a loc-state facet entry. The rubric requires old-state lineage from the locked loc-state file or from a prior sensory entry on the same modality. No prior sound-modality sensory entry exists (sensory:1 is tactile). No loc-state entry establishes the alley's auditory level. The baseline is geometrically implied but not facet-stated.

This is the implicit-baseline case: not a direct contradiction of loc-state (loc-state does not assert a non-silence sound level for the alley interior), but not an explicit derivation either. Under the card's attack protocol — "identify the most recent prior loc-state entry; are the old-state and loc-state consistent?" — the answer is: consistent with geometry, but the auditory content is not in loc-state at all. The old-state is filling a gap that loc-state does not cover.

Convergence with auditor: The auditor's pass-039 accepted this entry on disambiguation and form grounds ("fire warranted; 'effortful' qualifier migrated from bone SVO to sensory facet per note-003"). The auditor did not run the old-state lineage check — that is this reviewer's domain. The auditor's pass confirms the entry's other axes pass; this callout is narrowly the old-state-lineage gap the auditor's mechanical scan did not cover.

**Required fix:** Either (a) add a loc-state entry at @11 or @12 that names an explicit auditory baseline for the alley interior (e.g., "enclosed stone; no ambient sound source; interior acoustically isolated at human-audible register" — or equivalent §sensory note appended to the existing loc-state:5 or loc-state:6 content), OR (b) amend the sensory:2 old-state derivation note to cite loc-state:5 @11 (correcting the wrong ID) and extend loc-state:5 with a sound-level annotation that makes the silence derivation explicit. The §Hazards card content is available as supporting material for the extension. The fix must land in loc-state FIRST; the sensory entry's old-state can then resolve against the amended baseline.

Note: if option (a) is chosen by extending loc-state:5 or :6 with a sound-level annotation, the auditor's pass-039 may need a brief re-check against the loc-state-rubric cross-facet clause — but no new HARD is anticipated since the extension would be additive, not contradictory.

---

## Aggregate verdict

**REVISE**

sensory:1 @4 is clean — old-state lineage intact to loc-state:1 @1.

sensory:2 @13 has two issues: (1) the dispatch's ID attribution for the old-state anchor is wrong (states loc-state:7 @11; correct entry is loc-state:5 @11), and (2) no loc-state entry explicitly names an auditory baseline for the alley interior — the `alley-stone-contained-silence` old-state is a geometric inference with no facet-stated sound level to anchor it. The rubric's old-state lineage requirement is not satisfied by geometric implication alone. The loc-state file needs an explicit auditory annotation at @11 or @12 before sensory:2's old-state chain is traceable.

One entry unanchored. Facet fails this cycle.
