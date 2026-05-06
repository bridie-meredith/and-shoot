# Location-State Facet — Phase 2 Lift Report

Phase 2 (writer-fork + auditor) of the shoot-v2 facet-tuning process for the location-state facet. Run 2026-05-06.

**Outcome:** writer-fork rubric-compliance = **94.7%** vs. Phase 1 baseline **53.8%** under the same single mechanic auditor. **Lift: +40.9 points.** One residual form violation (Intent 5). The dialect-audience floor-defense entries from Phase 1 do *not* survive mechanic audit — surfaces a rubric-refinement decision for Phase 3.

---

## Method change vs. Phase 1

Phase 1 used the project's three dialect-audience personas as taste reviewers. That worked for tuning a soft rubric to a hard one, but their taste contaminated the seam-zone with floor-defense reasoning the rubric did not formally carry. To preserve their calibration for dialogue/prose work and to give Phase 2 a deterministic mechanic check, the reviewer for Phase 2 (and the re-baselined Phase 1) is a single facet-mechanic auditor. No taste calls; just the rubric's three axes, four cross-axis tests, and six anti-patterns.

**Audience preservation.** STM files for `dark-fantasy-reader`, `pulp-enthusiast`, `worm-canon-pedant` were verified clean of loc-state contamination — last touched 2026-05-05 (pre-loc-state work). The V1/V2 dispatches in Phase 1 wrote only to dedicated `loc-state-v[12]-review.md` files and did not update STM. Dialect audience retired from facet-mechanic review going forward.

---

## Numbers

| Round | Corpus | Reviewer | Pass-rate | Notes |
|---|---|---|---|---|
| Phase 1 (originally reported) | 65 candidates | 3 dialect-audience personas, aggregate ≥2/3 | 30/65 = 46% | Includes 2 floor-defense accepts |
| Phase 1 re-baseline | 65 candidates | 1 mechanic auditor | **35/65 = 53.8%** | The honest comparison floor |
| Phase 2 | 19 decisions (11 FIRE + 8 NONE) | 1 mechanic auditor | **18/19 = 94.7%** | Lift: **+40.9** |

The Phase-1-reported number (46%) was lower than the re-baselined number (53.8%) because the dialect audience rejected several entries the rubric mechanically warrants. That's taste-noise, not rubric-failure. The 53.8% baseline is the right floor.

Phase 2 metric clarification: rubric-compliance counts both FIRE-CORRECT (entry passes rubric) and NONE-CORRECT (refusal warranted by rubric). The writer's *decision discipline* — knowing when to refuse — is part of what we tuned. In Phase 1 my permissive seeding had no NONE option; every anchor got an entry. In Phase 2 studio refused 8 of 19 anchors and was correct on every refusal.

---

## Phase 2 result by intent stratum

| Stratum | Anchors | Studio fired | Studio refused | Auditor verdict |
|---|---|---|---|---|
| Calibration anchor | 1 (C) | 1 | 0 | 1 FIRE-CORRECT |
| Boundary-crossings | 5 (1–5) | 5 | 0 | 4 FIRE-CORRECT, 1 FIRE-INCORRECT (Intent 5) |
| Scene-anchors | 2 (6, 7) | 2 | 0 | 2 FIRE-CORRECT |
| State-changes | 3 (8, 9, 10) | 3 | 0 | 3 FIRE-CORRECT |
| Fauna-feed (was Phase-1 floor-defense) | 1 (11) | 0 | 1 | 1 NONE-CORRECT |
| Within-scene traps | 4 (12–15) | 0 | 4 | 4 NONE-CORRECT |
| Persistence/atmosphere traps | 2 (16, 17) | 0 | 2 | 2 NONE-CORRECT |
| Sound-arrival (was Phase-1 floor-defense) | 1 (18) | 0 | 1 | 1 NONE-CORRECT |

**Reading:** every trap (within-scene, persistence, atmosphere) was correctly refused. Every legitimate fire-anchor (boundary-crossing, scene-anchor, state-change) was correctly fired *except* Intent 5. Both floor-defense candidates from Phase 1 came back as NONE-CORRECT under mechanic audit — confirming the rubric as written does not warrant entries for fauna-feed or remote-sound-arrival.

---

## The residual fault — Intent 5

Studio fired on Intent 5 (`@s01e06-pl72 oc-sept-nave-interior | predawn | none | door-shut-behind, channel-reindexed | nave interior, yard drops off the plane`). The auditor flagged two violations:

1. **Sensory note has two focus-elements** — "nave interior" + "yard drops off the plane." The pointing test wants one perceptible focus.
2. **Conditions slot carries actor-state** — `channel-reindexed` describes Taylor's perception-channel state, not an observable location condition. Anti-pattern: actor-state laundered as loc-state.

This is a single-anchor revise, not a systemic fault. The decision to fire was correct (entering the sept is a legitimate boundary-crossing); the form was wrong. Phase 4 revise would tighten the entry to a single focus-element and remove the perception-state from the conditions slot.

---

## The floor-defense divergence (rubric refinement question)

Phase 1's dialect audience accepted these on floor-defense grounds (entries #11 and #18 in this Phase 2 stratification correspond to candidate-corpus #53 and #63):

- **Fauna-feed beat** (PL19 mouse-shape steps in seam) — worm-canon-pedant defended on canon-mechanic grounds: Taylor's swarm-network demands spatial resolution; the seam-at-hip + mouse-warm fact is what makes the feed-spike mechanically legible.
- **Sound-arrival beat** (PL67 hoof on cobbles half-a-league north) — pulp-enthusiast defended as canonical "herald at the wall": sound-carrying + cobble-surface as named conditions are what makes auditory detection at distance operate.

The mechanic auditor verdicted both as `NONE-CORRECT`. Studio's reasoning matches: PL19 is a perception-feed beat (interiority pushed to physical SVO, anti-pattern explicitly named in rubric §necessity); PL67's auditory signal resolves against the inherited harrenhal-exterior station — re-citing it is inherited re-naming.

**The divergence is a rubric question, not a Phase 2 failure.** Two paths:

- **Path A — accept the auditor.** The rubric as written excludes fauna-feed and remote-sound-arrival from loc-state. Those beats live in narrator/feel facets (perception) or state-update (channel state). Phase 1 floor-defense was the dialect audience reading taste into the rubric. The strict mechanic verdict is correct.
- **Path B — refine the rubric.** Add an explicit clause to the necessity axis: *fauna-feed beats earn loc-state when the spatial micro-resolution is the operative perception-mechanic*; *auditory detection at distance earns loc-state when the carrying-conditions are the operative load-bearing fact*. This widens the necessity axis to cover what the dialect audience saw.

Recommended: **Path A for now, revisit at Phase 5.** The cleaner rubric is more falsifiable. If Phase 5 shipping audit shows the perception-mechanic load is genuinely lost in the stitched output, refine then. Don't widen the rubric to absorb taste-judgments unless the loss is observable downstream.

---

## What the audit numbers say

- The writer-fork pattern transfers from dialogue to location-state. Same shape: blind-to-originals, intent specifies state not text, multi-draft + chosen-mark + cited signatures, explicit anti-patterns. Same magnitude lift (+40.9 vs. dialogue's +54).
- The rubric is internalizable. Studio refused 8 of 8 anchors that should have been refused, including 4 within-scene movement traps that the original Phase 1 corpus contaminated heavily (those were the dominant Phase 1 reject category).
- The mechanic auditor is the right reviewer for this facet. Faster (one dispatch vs. three), cheaper, deterministic, and competent — the rubric is mechanic-dense, not taste-dense, and a single auditor's per-axis check produces a defensible verdict where three taste-personas produced seam-zone disagreement.
- The schema is robust. Every chosen entry's form passed the auditor except Intent 5's sensory-note plurality and conditions-slot contamination. Two well-defined faults, both fixable in one revise pass.

---

## Phase 3 plan (adversarial seam-finding)

Per `design/shoot-v2/facet-tuning-process.md`:

1. Auditor (or a second reviewer) produces hostile counter-arguments for *every* entry — accepts included. Output: one seam per unit.
2. For loc-state, seams should target: focus-element selection (could a different element have been better?), inheritance assumptions (is the prior cited state actually established?), location-slug accuracy (does the named slug match an authored location card?).
3. Studio fork reads seams; defends with rubric citation OR revises with multi-draft.

The single FIRE-INCORRECT (Intent 5) goes directly to Phase 4 revise without needing Phase 3 seam-finding for it — the auditor's verdict already names the revise targets.

---

## Artifacts

- Phase 2 intents (full): `design/shoot-v2/phase2-locstate-intents.md`
- Phase 2 intents (writer-blind): `design/shoot-v2/phase2-locstate-intents-blind.md`
- Phase 2 studio output: `design/shoot-v2/phase2-locstate-output.md`
- Phase 2 audit: `active-project/staff/auditor/phase2-locstate-audit.md`
- Phase 1 re-baseline audit: `active-project/staff/auditor/phase1-locstate-rebaseline-audit.md`
- This report: `design/shoot-v2/phase2-locstate-report.md`
- Locked rubric (unchanged): `design/shoot-v2/rubric-location-state.md`
