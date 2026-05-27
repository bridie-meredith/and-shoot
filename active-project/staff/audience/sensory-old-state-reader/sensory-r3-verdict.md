---
reviewer: sensory-old-state-reader
facet: sensory
episode: b01-c04
cycle: r3
date: 2026-05-27
verdict: accept
---

# Cycle-3 Context

Cycle-1 verdict: REVISE. sensory:1 @1 STRONG ATTACK — old-state `eel-alley-dawn-air` unanchored (no loc-state entry at or before @1 establishes this baseline; @1 is chapter-open with no prior entry; compound: loc-state:1 @1 places tallow-damp already present, making any delta-from-prior-ambient structurally unsupported). sensory:2 @13 ACCEPT conditional — old-state `tallow-damp-lane-caulking` held via dual path: (a) sensory:1 new-state chain OR (b) direct loc-state:1 derivation. sensory:3 @25 ACCEPT — cross-location carry within rubric tolerance.

Cycle-3 fix: sensory:1 @1 DELETED (2/3 convergence: disambiguation fail + unanchored old-state confirmed clean deletion path). Cite-index and proto-line @1 updated to remove sensory:1.

Re-review scope: verify sensory:2 @13 old-state chain re-resolves from loc-state:1 `tallow-damp-present` now that sensory:1 no longer exists as an intermediate chain-link.

---

# Old-State Re-Resolution — sensory:2 @13

**Entry (post-fix):** `smell: tallow-damp-lane-caulking -> middens-discard-compound`

## Step 1 — prior smell-modality sensory entry

sensory:1 deleted. sensory:2 is now the chapter's first smell fire. The prior-sensory-chain path (sensory:1 new-state → sensory:2 old-state) is gone. Old-state must resolve via direct loc-state derivation.

## Step 2 — loc-state scan for smell-relevant baseline at or before @13

Walk backward from @13:

- **loc-state:3 @13** — `oc-pig-tallow-lane | morning | none | middens-junction-active, carter-work-ongoing | three alleys converge at the junction-mouth where the discard-air sits heaviest.` Smell content: `discard-air sits heaviest`. This is the new-state source, not the old-state source.

- **loc-state:2 @4** — `oc-cooper-yard-eel-alley | predawn | none | shed-wall-cover-active | the shed-wall puts her back to timber with the lane-mouth across open yard.` No smell note. Does not supply old-state.

- **loc-state:1 @1** — `oc-cooper-yard-eel-alley | predawn | none | tallow-damp-present, yard-workers-at-near-shed, third-bell-quiet | the tallow-damp off the lane-caulking reaches the shed-wall before the yard is visible.` Conditions: `tallow-damp-present`. Sensory note: "the tallow-damp off the lane-caulking." RESOLVED. The old-state descriptor `tallow-damp-lane-caulking` is a direct compact of `tallow-damp-present` (condition) + "lane-caulking" (sensory note language). Verbatim component match. No invention.

## Step 3 — cross-location carry assessment

loc-state:1 @1 is at oc-cooper-yard-eel-alley; sensory:2 @13 is anchored at oc-pig-tallow-lane. The old-state names the smell ambient of the prior location zone — the established tallow-damp of the cooper's yard / eel-alley zone that Taylor is departing as she transits to pig-tallow-lane. This is the standard cross-location transition-inflection pattern: old-state = ambient carried from the departing location; new-state = ambient of the arriving location. The same pattern was accepted for sensory:3 @25 (old-state `carter-work-ambient` derived from loc-state:3 at the prior location). Single-hop derivation. Named and traceable.

## Step 4 — new-state check (unchanged)

`middens-discard-compound` traces to loc-state:3 @13 `discard-air sits heaviest at the junction-mouth.` Direct. Clean.

## Step 5 — delta direction

oc-cooper-yard-eel-alley (tallow-damp baseline) → oc-pig-tallow-lane middens junction (concentrated discard-air). Smell intensifies from lane-caulking tallow zone to middens junction compound. Direction unambiguous.

---

# Hostile Re-Read

Rereading before clearing.

**Attack — does the deletion of sensory:1 create a gap that invalidates sensory:2's old-state by removing the only path?**

No. Cycle-1 explicitly mapped the dual path and flagged this exact scenario: "Even if the prior-sensory chain is discounted (because sensory:1 itself has a baseline-invention fault), the direct loc-state derivation holds: tallow-damp is the established ambient of the eel-alley / cooper's-yard zone per loc-state:1." The dual path was always present; deletion of sensory:1 activates the fallback. The fallback holds on direct inspection. No gap.

**Attack — is loc-state:1 at a different location from sensory:2's anchor, making the derivation a cross-facet violation?**

No. The rubric (Axis 1, Modality-inflection) states old-state must match "the most recent location-state file's § sensory or § conditions field for the beat's location, OR the most recent prior sensory-flag entry on the same modality." With no prior sensory entry on smell, the applicable path is the most recent loc-state. loc-state:1 is the most recent loc-state entry before @13 that names a smell-relevant condition. The cross-location carry is the expected transition-inflection pattern; the old-state names the ambient of the zone being left, not the zone being entered. The rubric's cross-location carry tolerance was explicitly accepted in cycle-1 for sensory:3 @25. Consistent treatment applies.

**Attack — is `tallow-damp-lane-caulking` specific enough, or is it generic naming (anti-pattern 8)?**

The name is compound-specific: `tallow-damp` (substance) + `lane-caulking` (source). It names the originating material and location of the smell. Rubric requires names "specific enough that a reader can distinguish this perceptual state from another." `tallow-damp-lane-caulking` distinguishes from middens-discard (different substance), from tallow-smoke (different form), from unspecified ambient. Passes.

No surviving attack.

---

# sensory:3 @25 — Status Unchanged

`sound: carter-work-ambient -> roper's-court-near-silence` — cycle-1 ACCEPT stands. No change to this entry or its anchors in cycle-3. Lineage: old-state derives from loc-state:3 @13 `carter-work-ongoing` (cross-location carry); new-state derives from loc-state:4 @25 `court-empty, predawn`. Both paths intact.

---

# File-Level Health (post cycle-3)

| entry | modality | old-state | loc-state anchor | lineage status |
|-------|----------|-----------|-----------------|----------------|
| sensory:1 @1 | smell | — | — | DELETED |
| sensory:2 @13 | smell | tallow-damp-lane-caulking | loc-state:1 @1 (tallow-damp-present / lane-caulking language) | VALID — direct loc-state derivation |
| sensory:3 @25 | sound | carter-work-ambient | loc-state:3 @13 (carter-work-ongoing) | VALID — cross-location carry (cycle-1 unchanged) |

- Sparsity: 2/39 = 5.1%. Within 3–6% band. Short-chapter exemption not required — within ceiling without it.
- Modality coverage: smell (sensory:2) + sound (sensory:3) = 2 modalities. Floor met.
- No entries with unanchored old-state.
- Cross-facet contract intact: sensory:2 old-state → loc-state:1; sensory:2 new-state → loc-state:3. sensory:3 old-state → loc-state:3; sensory:3 new-state → loc-state:4.

---

## VERDICT

**verdict: accept**

sensory:1 @1 deletion confirmed clean. sensory:2 @13 old-state `tallow-damp-lane-caulking` re-resolves directly from loc-state:1 @1 `tallow-damp-present` + "lane-caulking" sensory note language. The prior-sensory-chain path is gone with sensory:1's deletion; the direct loc-state derivation (always available as cycle-1's dual path fallback) is now the primary path and holds without structural change to sensory:2. sensory:3 @25 is unchanged; its cycle-1 acceptance carries. Post-cycle-3 sensory file: both old-state lineages anchored, modality floor met, sparsity within band, no unanchored baselines remaining.
