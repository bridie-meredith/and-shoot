---
reviewer: sensory-disambiguation-pedant
facet: sensory
episode: b01-c04
cycle: r3
date: 2026-05-27
verdict: revise
exemplar: absent (baseline card only)
---

# Cycle-3 Context

Prior cycle state:
- sensory:1 @1 — cycle-1 REVISE (charged-subject disambiguation fail). Cycle-3 fix: DELETED.
- sensory:2 @13 — cycle-1 SOFT ATTACK (advisory). Old-state `tallow-damp-lane-caulking` previously chained from sensory:1's new-state. Cycle-3 fix: sensory:1 deleted; sensory:2's old-state must re-source.
- sensory:3 @25 — cycle-1 CONDITIONAL PASS. Conditioned on loc-state:3 establishing carter-work-ambient baseline.

The specific question this cycle: does sensory:2's old-state `tallow-damp-lane-caulking` resolve from loc-state:1's `tallow-damp-present` now that the sensory:1 chain anchor is gone? Does the chain still hold?

---

# Chain Resolution Trace — sensory:2 @13

**Entry (post-fix):** `2 @13 smell: tallow-damp-lane-caulking -> middens-discard-compound`

**Old-state under review:** `tallow-damp-lane-caulking`

## Rubric anchor rule (Axis 1, Modality-inflection, ACCEPT signatures)

> "Source the old-state from the locked location-state for the most recent loc-state-cited beat, OR from the most recent prior sensory-flag entry on the same modality."

Two paths. Both checked with sensory:1 deleted.

---

## Path A — Prior sensory entry on smell modality

sensory:1 was the only prior smell entry in this file. It is deleted. No prior sensory-smell entry exists.

**Path A: CLOSED.**

---

## Path B — Most recent loc-state entry for the beat's location

sensory:2 is anchored @13. At @13, the location is oc-pig-tallow-lane (loc-state:3 @13).

loc-state:3 reads:
> `3 @13 oc-pig-tallow-lane | morning | none | middens-junction-active, carter-work-ongoing | three alleys converge at the junction-mouth where the discard-air sits heaviest`

Conditions: `middens-junction-active`, `carter-work-ongoing`. The descriptive note foregrounds `discard-air`. No tallow-damp condition appears in any field of loc-state:3.

The old-state `tallow-damp-lane-caulking` does not correspond to any condition or descriptive element in loc-state:3.

**Path B: FAILS.** loc-state:3 does not establish tallow-damp as the sensory baseline at oc-pig-tallow-lane at @13.

---

## The dispatch assumption — loc-state:1 cross-location carry

The cycle-3 fix premise holds that sensory:2's old-state "must re-source from loc-state:1's `tallow-damp-present`."

loc-state:1 is at `oc-cooper-yard-eel-alley`. loc-state:3 is at `oc-pig-tallow-lane`. These are distinct location records — different location slugs, separate condition sets, different timestamps in the episode. The rubric's anchor rule specifies the most recent loc-state for the beat's location — not any prior loc-state from any location visited earlier in the episode. Sourcing across a location boundary is not a path the rubric permits.

The rubric's REJECT signature under Axis 1 names this failure mode explicitly:

> "Unanchored old-state (HARD). Entry's old-state does not resolve to (a) the most recent loc-state file's § sensory or § conditions baseline for the beat's location, OR (b) the most recent prior sensory-flag entry on the same modality. A free-floating old-state ('hook-alley-ambient' with no loc-state or prior-sensory anchor) is a fictive baseline."

`tallow-damp-lane-caulking` names a specific environmental detail — tallow caulking on the lane's timber joints — which appears in loc-state:1's descriptive note for the cooper's yard ("the tallow-damp off the lane-caulking reaches the shed-wall"). That detail was authored for oc-cooper-yard-eel-alley. It does not appear in loc-state:3's conditions or note for oc-pig-tallow-lane.

The environmental logic — Pig Tallow Lane is named for tallow processing, the surrounding environment probably carries some tallow-damp residue — is plausible worldbuilding but is not in the loc-state file. What is not in the loc-state file is not an anchor. Per memory rules: if a change is not in a state file, it did not happen. If a condition is not in a loc-state entry, it is not an established baseline.

**Cross-location carry: REJECTED.** loc-state:1's `tallow-damp-present` belongs to oc-cooper-yard-eel-alley. It does not anchor sensory:2's old-state at @13 (oc-pig-tallow-lane / loc-state:3).

---

## HARD Finding — sensory:2 @13

**[sensory:2] @13 — smell: tallow-damp-lane-caulking -> middens-discard-compound**

UNANCHORED-OLD-STATE HARD. Path A closed (sensory:1 deleted; no prior smell entry). Path B fails (loc-state:3 at oc-pig-tallow-lane carries no tallow-damp condition). Cross-location carry from loc-state:1 (oc-cooper-yard-eel-alley) rejected — rubric anchor rule is per-location. Old-state `tallow-damp-lane-caulking` is a free-floating baseline. Per URI-FACETS-CYCLE-1, this is a HARD finding.

**Convergence-trace:** Cycle-1 verdict anticipated this directly: "If sensory:1 is deleted, this old-state chain anchor breaks and must be re-sourced from loc-state:3." The cycle-3 fix removed sensory:1 but did not revise sensory:2's old-state. The re-source from loc-state:1 proposed in the dispatch premises is architecturally incorrect — loc-state:1 is the wrong location. The finding the cycle-1 verdict flagged as downstream consequence has now materialized as a live HARD.

---

# Remaining Entry — sensory:3 @25

**Entry:** `3 @25 sound: carter-work-ambient -> roper's-court-near-silence`

Cycle-1 conditional pass. Conditioned on loc-state:3 naming "carter-work-ambient" (or equivalent) in its sensory baseline.

**Verification:** loc-state:3 reads conditions `middens-junction-active, carter-work-ongoing`. The condition `carter-work-ongoing` directly anchors `carter-work-ambient` as the smell old-state label: ongoing cart work in a lane produces an ambient sound level; the label names the sensory register that condition produces. This is the same referent, naming-layer shifted from state-condition to sensory-state. Functionally anchored.

No prior sensory-sound entry exists (sensory:1 was smell; sensory:2 is smell). Path B under the anchor rule: loc-state:3 at @13 (most recent loc-state before @25, and the most recent entry for oc-pig-tallow-lane, which the route passes through before reaching Roper's Court) — the `carter-work-ongoing` condition names the sound environment. loc-state:4 at @25 covers oc-ropers-court, conditions `court-empty, far-tributaries-dark`; descriptive note: "early-morning grey leaves the court sight-clear to all tributary mouths." The loc-state for the new location (@25 = oc-ropers-court) establishes `court-empty` — absence of bodies, which directly supports the new-state `roper's-court-near-silence`. The inflection is: entering an empty court after the ambient sound of the middens lane. The old-state sources from the prior sound environment (loc-state:3 carter-work-ongoing); the new-state sources from the new location's emptiness (loc-state:4 court-empty). Chain resolves.

Cycle-1 conditional requirement: **MET.** sensory:3 @25 **PASSES.**

---

# File-Level Status

**Modality coverage (post-deletion):** sensory:2 (smell) + sensory:3 (sound) = 2 modalities. Floor met at 2.

**Density:** 2/39 = 5.1%. Within 3-6% band. Short-chapter exemption not needed.

**The HARD finding is entry-level only.** File-level geometry is not the problem. sensory:2's old-state breaks on the disambiguation-from-unanchored-baseline axis, which is distinct from modality-floor or density checks.

---

# Resolution Path

Two options exist; both require studio intervention.

**Option A — Revise sensory:2's old-state to anchor in loc-state:3.**
loc-state:3 does not name a pre-middens smell old-state at oc-pig-tallow-lane — it only names the middens junction conditions. For sensory:2 to fire a genuine inflection at @13, a distinct prior smell state must be established. Studio would need to backfill loc-state:3 with an explicit pre-junction smell baseline for oc-pig-tallow-lane (e.g. a lane-ambient-tallow condition naming what the lane smelled like before the middens junction opens into it), then revise sensory:2's old-state to match. The narrative rationale exists (Pig Tallow Lane carries a tallow processing ambient), but the state file must carry it before the sensory entry can reference it. Anti-pattern 14 applies: the loc-state edit must land first; the sensory old-state revision must reference the now-anchored baseline.

**Option B — Delete sensory:2.**
With no available old-state anchor for the smell modality at @13, deletion is the clean path. File would carry sensory:3 only — one modality (sound). This drops below the ≥2 modality floor. A replacement smell entry would need to be authored at a beat where loc-state establishes an explicit, distinct smell baseline. Anti-pattern 14 applies to any replacement ADD: full per-entry rubric pre-validation required before committing, old-state lineage from loc-state verified first.

**Note to fixer:** either option requires studio action before sensory:2's status resolves. Fixer cannot change sensory:2's old-state without a supporting loc-state edit (Option A) or without authoring a replacement smell entry elsewhere with a clear loc-state anchor (Option B).

---

# VERDICT

**revise**

sensory:1 @1: DELETED — confirmed clean. Deletion was the correct action.

sensory:2 @13: UNANCHORED-OLD-STATE HARD. Deletion of sensory:1 severed the only available chain anchor. The proposed re-source from loc-state:1 (oc-cooper-yard-eel-alley) is invalid under the rubric's per-location anchor rule. loc-state:3 (oc-pig-tallow-lane, the beat's location) carries no tallow-damp condition. Old-state `tallow-damp-lane-caulking` is unanchored. Requires studio intervention: backfill loc-state:3 with an explicit pre-junction smell baseline and revise old-state to match (Option A), or delete sensory:2 and author a qualified replacement smell fire with a clean loc-state anchor (Option B).

sensory:3 @25: PASS. Disambiguation gate clear. Old-state `carter-work-ambient` resolves from loc-state:3's `carter-work-ongoing` condition. New-state `roper's-court-near-silence` resolves from loc-state:4's `court-empty` condition. Cycle-1 conditional requirement met.

The cycle does not close. sensory:2's HARD blocks the facet.
