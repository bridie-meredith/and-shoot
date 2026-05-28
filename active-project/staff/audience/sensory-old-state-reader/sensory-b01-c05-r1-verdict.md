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
auditor-findings-consulted: pass-039
---

# Sensory Old-State Reader — b01-c05 R1 Verdict

## Entry-level review

### [sensory:1] @4 `tactile: lane-stone-surface-baseline -> provisioner-cart-load-on-stone`

verdict: ACCEPT

Lineage walk:
- Anchor: @4 (`the provisioner-train crosses the junction`)
- Location: oc-rushwick (scene-A, junction)
- Most recent prior loc-state entry: loc-state:1 @1 — `oc-rushwick | morning | clear | north face of junction in hill-shade; cool-damp stone underfoot | stone skirt holds shade at the lane-mouth; overnight damp still in the paving`
- Old-state `lane-stone-surface-baseline` traces directly to loc-state:1 @1. The composite name captures the stone-underfoot and paving baseline established there. No modality mismatch: loc-state:1 names a tactile surface condition (`cool-damp stone underfoot`); the sensory old-state is the tactile register of that same undisturbed surface. Delta direction (ambient-stone-surface → cart-loaded-stone) is consistent with what the provisioner-train crossing would produce against that baseline.
- No invention. No contradiction. No frame mismatch.

The dispatch's stated attribution "old-state from loc-state:1 @1 (stone skirt at grade)" is confirmed. Lineage intact.

---

### [sensory:2] @13 `sound: alley-stone-contained-silence -> courier-effortful-body-sound`

verdict: REVISE

Lineage walk:
- Anchor: @13 (`the three figures pin the courier`)
- Location: oc-rushwick, side-alley interior
- Most recent prior loc-state entries before @13: loc-state:6 @12 (`alley-mouth sealed by two bodies at its full width; alley-mouth width is the containment fact; two bodies at the mouth control all egress`) and loc-state:5 @11 (`side-alley mouth visible from junction; interior not | one-person-wide stone passage off the east exit; rough original-construction walls, uneven floor`)
- Old-state: `alley-stone-contained-silence`

**[sensory:2] @13 — Attack 1: dispatch ID attribution is broken.**
Dispatch states "old-state from loc-state:7 @11 (alley-interior contained)." loc-state:7 fires at @20 (`alley-mouth open; three figures have cleared to the east`). That is the post-enforcement exit entry, placed well after @13. loc-state:5 fires at @11. The stated ID is wrong. If the old-state has any loc-state lineage, it traces to loc-state:5 @11, not loc-state:7. The attribution carries a broken ID.

**[sensory:2] @13 — Attack 2: no sound-level field in any prior loc-state entry for this location.**
Neither loc-state:5 @11 nor loc-state:6 @12 names an auditory baseline. loc-state:5 establishes spatial description only: `one-person-wide stone passage; rough original-construction walls, uneven floor`. loc-state:6 establishes containment geometry only: `alley-mouth width is the containment fact; two bodies at the mouth control all egress`. Neither entry carries a §sensory note, a §sound note, or any silence-level annotation. The old-state component `silence` — the acoustic level named as the pre-delta baseline — does not appear in any loc-state entry preceding @13. The sound baseline is inferred from enclosed-stone geometry, not sourced from loc-state's auditory content.

The oc-rushwick.card.md §Hazards does corroborate the inference: "A low, effortful sound from a body inside a side alley does not reach the junction at any register the human ear recovers." But §Hazards is a location-card field, not a loc-state facet entry. The rubric requires old-state lineage from the locked loc-state file or from a prior sensory entry on the same modality. No prior sound-modality sensory entry exists before @13 (sensory:1 is tactile). No loc-state entry establishes an auditory level for the alley interior. The baseline is geometrically implied but not facet-stated.

This is the implicit-baseline case: not a contradiction of loc-state (no loc-state entry asserts a non-silence sound level for the alley) but also not an explicit derivation. The old-state is filling a gap loc-state does not cover. Under the rubric's REJECT signature: "Unanchored old-state (HARD). Entry's old-state does not resolve to (a) the most recent loc-state file's § sensory or § conditions baseline for the beat's location, OR (b) the most recent prior sensory-flag entry on the same modality." Neither condition is met for the `silence` component.

Convergence-trace with auditor: pass-039 accepted this entry on disambiguation and form grounds ("fire warranted; 'effortful' qualifier migrated from bone SVO to sensory facet per note-003 carry-forward"). pass-039 did not run the old-state-lineage check as a distinct verification step — it confirmed the bare-verb test and the oc-rushwick §Hazards derivation without verifying whether §Hazards is a rubric-compliant anchor for the old-state field. This callout is the seam pass-039 did not cover.

**Required fix:** Option A — extend loc-state:5 @11 or loc-state:6 @12 with an explicit auditory note for the alley interior (e.g., appending `| enclosed stone; no ambient sound source; interior acoustically isolated at human-audible register` to loc-state:5's detail field). The §Hazards card content supports this extension. Option B — amend the old-state in sensory:2 to a form whose sound-level component is directly derivable from existing loc-state content (e.g., `alley-stone-enclosed-ambient` where `enclosed` derives from loc-state geometry and the ambient-sound level is treated as implied by enclosure — though this is a weaker derivation and will need defense). Either way, loc-state must be corrected first; sensory:2's old-state resolves against it after.

---

## Aggregate verdict

**REVISE**

sensory:1 @4: old-state lineage intact to loc-state:1 @1. Clean.

sensory:2 @13: two issues. (1) The dispatch's ID attribution for the old-state anchor names the wrong loc-state entry (states loc-state:7 @11; the actual entry at @11 is loc-state:5). (2) No loc-state entry explicitly names an auditory baseline for the alley interior — the `alley-stone-contained-silence` old-state invents a sound level that geometry implies but loc-state does not state. The rubric's unanchored-old-state REJECT signature applies. Loc-state requires a backfill (§sound or §conditions annotation at @11 or @12) before sensory:2's old-state chain is traceable. One entry unanchored on its modality-specific old-state component. Facet fails this cycle.
