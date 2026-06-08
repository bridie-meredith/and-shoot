---
reviewer: sensory-disambiguation-pedant
facet: sensory
episode: b01-c04
cycle: r1
date: 2026-05-27
verdict: revise
exemplar: absent (baseline card only)
---

# Per-Entry Callouts

## [sensory:1] @1 — smell: eel-alley-dawn-air -> tallow-damp-lane-caulking

**ATTACK — charged-noun redundancy.**

Proto-line @1: `the tallow-damp marks the cooper's-yard shed-wall`

The proto-line puts "tallow-damp" in subject position. That compound noun names a specific olfactory substance — tallow (rendered animal fat, recognizable smell) plus damp (moisture carrier). "Tallow-damp marks the shed-wall" delivers the smell-agent before the sentence ends. The reader has the olfactory register from the subject alone.

The flag then writes `smell: eel-alley-dawn-air -> tallow-damp-lane-caulking`, arriving at exactly the state the proto-line's subject already named. This does not disambiguate — it doubles. Without the flag, the audience still knows the difference: "tallow-damp" is not a bare word. Compare: "the wind crosses the yard" (bare — audience needs the thermal flag to land the register) vs. "the tallow-damp marks the wall" (charged compound noun — the smell is in the noun, not inferred from a bare verb).

Action-verb self-charge check: "marks" is a bare attribution verb, not a sensory-act verb. The charging here is in the noun, not the verb — but charged-noun redundancy is the same failure mode as charged-verb. The flag's job is to separate bare from charged. This noun is charged.

**Convergence-trace:** Auditor flag-003 addresses density geometry (7.7% overshoot as architectural). No auditor finding covers the bare-vs-charged axis for sensory:1. This attack is independent.

**Entry verdict: REVISE or DELETE.** If the proto-line is restructured so "tallow-damp" is not in subject position — or replaced with a bare-noun scene anchor — the flag earns its fire. As written, the flag doubles a charged compound noun.

---

## [sensory:2] @13 — smell: tallow-damp-lane-caulking -> middens-discard-compound

**SOFT ATTACK — location-noun pre-loads the register at the subject level.**

Proto-line @13: `the waste-middens junction draws the discard-air`

"Waste-middens" in subject position is the load-bearing charged element. "Middens" names refuse heaps specifically — historically loaded, olfactory-register-strong. A reader who lands on "waste-middens junction" already holds the smell-register before reaching "discard-air." The object "discard-air" is comparatively generic (discard = refuse, air = air) — it lacks the self-charging intensity of "stench" or "reek," so it is not itself a charged word. But the smell-register has already been supplied by the subject.

This is a softer failure than sensory:1: the charging happens in the location noun (subject), not in the directly flagged object. A reader without "middens" fluency might need the flag to land the smell; a reader with it does not. Borderline.

**Old-state lineage:** `tallow-damp-lane-caulking` chains correctly from sensory:1's new-state. If sensory:1 is deleted, this old-state chain anchor breaks — sensory:2's old-state would need re-sourcing from loc-state:3's sensory baseline.

**Convergence-trace:** No auditor finding covers the disambiguation axis for sensory:2. Old-state lineage (URI-FACETS-CYCLE-1) is clean for this entry as long as sensory:1 survives.

**Entry verdict: ADVISORY.** Not independently blocking. Secondary consequence: removal of sensory:1 creates a downstream chain dependency here.

---

## [sensory:3] @25 — sound: carter-work-ambient -> roper's-court-near-silence

**CONDITIONAL PASS — disambiguation gate clears; old-state lineage unverified.**

Proto-line @25: `the early-morning grey empties Roper's Court`

The proto-line fires on a visual-temporal image: early-morning light quality, spatial emptying. The sound modality is not named by the surface language. The verb "empties" implies absence of persons — from which the inference to reduced ambient sound is available — but "empties" is a spatial verb, not a sonic one. The inference chain runs: emptied court → fewer people → near-silence. That chain requires a hop.

Compare the card's action-verb self-charge class: "opens the shutter" self-charges light-onset because opening IS the light act. "Empties" is not in that class — it names a spatial state, not a sonic event. The sound register does not arrive directly from "empties." Without the flag, the reader lands the visual and might infer the quiet; with the flag, the quiet is explicit. The flag does work the proto-line surface does not.

Disambiguation gate: CLEARS.

**Old-state lineage (flagged — requires external verification):** "carter-work-ambient" must trace to loc-state:3 @13 (the most recent prior loc-state; scene-B open at waste-middens junction) or to a prior sensory-sound entry. No prior sensory-sound entry exists in this file (sensory:1 and sensory:2 are both smell). The penny-a-barrel carter at proto-line @17 (vibes:8) names the carter in scene-B, consistent with the sound label. But loc-state:3 must hold "carter-work-ambient" explicitly in its sensory clause for this old-state to be anchored — not inferred from the carter's appearance in a vibes entry. If loc-state:3 does not name this baseline, the old-state is a free-floating invention — an unanchored-old-state HARD per URI-FACETS-CYCLE-1.

This facet file alone cannot resolve the question. Location-state-b01-c04.md scene-B sensory clause is the check surface.

**Convergence-trace:** Auditor flag-003 (density geometry) does not address old-state lineage for sensory:3. The URI-FACETS-CYCLE-1 unanchored-old-state HARD check was not surfaced by the auditor for this entry. This is an independent seam.

**Entry verdict: CONDITIONAL PASS.** Disambiguation gate clean. Ships only after loc-state:3 confirms "carter-work-ambient" (or equivalent) in its sensory baseline. If loc-state:3 does not establish that baseline, sensory:3 carries an unanchored-old-state HARD and must be revised before stitch.

---

# File-Level Observations

**Modality coverage:** smell × 2, sound × 1. Two modalities meet the ≥2 floor. No file-level attack on coverage.

**Density:** 3 / 39 = 7.7%. Auditor flag-003 identifies this as architectural — 3 scenes × 1 scene-open fire minimum. Concur; no disambiguation-pedant finding here.

**Pattern observation:** Both smell entries fire at scene-open anchors where the location noun is the sensory carrier. This is the disambiguation-at-scene-open failure pattern: the loc-state transition establishes the new sensory environment, the scene-open proto-line names the environment's sensory substance in subject position, and the sensory-flag then formally records what the noun already delivered. The flag is correct in form but wrong in function — it is not disambiguating bare language; it is ratifying language that already disambiguated itself.

---

# VERDICT

**revise**

sensory:1 @1 fails the disambiguation gate. "Tallow-damp" is a charged compound noun in subject position; the smell-flag doubles what the proto-line already names. Primary blocking callout.

sensory:2 @13 is a soft attack. "Waste-middens" pre-loads the olfactory register at the subject level. Advisory; not independently blocking. If sensory:1 is deleted, sensory:2's old-state chain anchor breaks and must be re-sourced from loc-state:3.

sensory:3 @25 clears the disambiguation gate but carries an unverified old-state lineage ("carter-work-ambient") requiring loc-state:3 confirmation. If loc-state:3 does not hold that baseline, this entry carries an unanchored-old-state HARD per URI-FACETS-CYCLE-1.

Resolution path: (1) revise or delete sensory:1 — if the proto-line is restructured away from "tallow-damp" as subject, fire may earn; if deleted, proceed to (2); (2) re-source sensory:2's old-state from loc-state:3's established sensory baseline; (3) verify loc-state:3 names "carter-work-ambient" or equivalent in its scene-B sensory clause before certifying sensory:3.
