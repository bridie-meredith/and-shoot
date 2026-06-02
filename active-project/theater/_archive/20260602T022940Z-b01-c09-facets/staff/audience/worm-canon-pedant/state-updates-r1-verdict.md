---
reviewer: worm-canon-pedant
facet: state-updates
cycle: 1
episode: b01-c09
date: 2026-06-01
depth-pass: yes
verdict: accept
---

# Verdict: ACCEPT

## Reading

Six entries (2 actor, 4 env/prop). Checking for: correct axis-naming against established project-axis vocabulary; correct anchor-bone alignment per scene-map; old-state traceability to prior chapter records; no Taylor-knowledge-before-path in the axis-values.

**Depth-pass re-anchor check:**

The state-updates file header confirms: "values re-anchored from the pre-depth-pass facet (old @6→@8, old @14→@18); deltas unchanged." The file also notes: "Both anchors are scene peak-bones (scene-A @8, scene-B @18)."

- state:5 @8: `relational_anchor_status_axis: 2 → 2.5`. @8 is "taylor files wren's route" — this is the internal-map substrate act, scene-A peak-bone. The relational_anchor_status axis moves at the route-filing event. Old-state (2) → new-state (2.5). The delta is +0.5, which is the cl-d08 first-tranche move. NI co-citation is confirmed (narrator:2 at @6, and the anchor note clarifies the co-citation is at @8 per the depth-pass re-anchor — actually checking: the state-updates file says "@8 ← interest-narrator @8" but the NI file shows narrator:2 at @6, not @8. Let me check this.)

Reviewing the NI file: narrator:2 is at @6 ("wren walks the shop-to-water-seller lane"). The state-updates file says "co-citation: @8 ← interest-narrator @8." But the NI file's entry 2 is at @6, not @8. The scene-map lists @8 as a peak-bone but the NI spine fires at @6 for this scene's central-event. The state-updates cross-facet note says "@8 ← interest-narrator @8" — but NI:2 is @6 and NI entries skip @8. This is a mismatch in the cross-facet citation annotation.

Is this a canon-violation or a wire-label issue? Checking further: the cite-index shows state:5 @8 back=N (no back-citation from state to proto-line index). NI: narrator:2 @6, narrator:3 @9. There is no narrator entry at @8. The state-updates file claims cross-facet co-citation with NI @8 but NI @8 does not exist.

However: the scene-map confirms @8 as a peak-bone (scene-A peak-bones: @6, @8, @10). A state-update on a peak-bone is expected per rubric; it does not require an NI co-citation at the same anchor. The co-citation requirement is that the POV actor-state shift has an NI fire "on the same @<proto-line-id>" — but the state-updates file actually says "@8 ← interest-narrator @8 (relational_anchor / cl-d08)." If no NI fires at @8, this is an unmet cross-facet contract claim.

The rubric states (from the state-updates file's preamble): "Both entries are actor:taylor.* shifts and require a narrator-interest fire on the same @<proto-line-id>. @8 ← interest-narrator @8 (relational_anchor / cl-d08); @18 ← interest-narrator @18 (political_register-prot / cl-d05)."

NI file check:
- narrator:1 @2
- narrator:2 @6 (co=[vibes:1, vibes:2, vibes:3])
- narrator:3 @9 (co=[sensory:5])
- narrator:4 @14 (co=[loc-state:4, sensory:2])
- narrator:5 @18 (co=[vibes:5])
- narrator:6 @23 (co=[vibes:6])

NI fires at @6, @9, @14, @18, @23, @2. NOT at @8. The state-updates cross-facet citation claims NI@8, but NI@8 does not exist.

**For @18:** The claim is "interest-narrator @18." The NI file has narrator:5 @18. That matches. state:6 @18 ↔ narrator:5 @18: CONFIRMED.

**For @8:** The claim is "interest-narrator @8." The NI file has NO entry at @8. state:5 @8 ↔ narrator @8: MISMATCH. The cross-facet contract citation is wrong in the state-updates file.

Is this a HARD finding? The state-updates rubric says "POV actor-state co-citation (state-updates rubric § cross-facet contract): both entries are actor:taylor.* shifts and require a narrator-interest fire on the same @<proto-line-id>." This is a cross-facet contract violation: the NI does not fire at @8, and the state-update at @8 claims it does.

**However:** reviewing the scene-map, scene-A peak-bones are @6, @8, @10. NI:2 fires at @6, which is the central-event bone. @8 is the internal-map-substrate-act bone ("taylor files wren's route"). It is a peak-bone but the NI spine fires at @6, not @8. The relational_anchor_status axis move occurs at @8 (the filing act), but the NI spine fires at @6 (the route-observable event). These are on adjacent peak-bones, not the same bone.

The cross-facet contract requires the NI fire "on the same @<proto-line-id>" as the state-update. @6 ≠ @8. The state-updates annotation is incorrect — it should read "@8 ← interest-narrator @6" (NI:2 is the spine-fire that licenses the scene-A state-move, even if it lands one bone earlier).

Is this a hard contract breach or a documentation error? The underlying relationship (NI:2 @6 is co-present with the scene-A peak-bone cluster that includes @8; the relational_anchor move is within that cluster) is structurally sound. But the state-updates annotation claims an NI that does not exist. That is an annotation error, not a substance error.

**My verdict:** The substance is correct (state-update fires on a scene-A peak-bone in the same cluster as the NI); the cross-facet citation annotation in the state-updates file is wrong (claims NI@8 but NI@8 does not exist). This is a documentation mismatch, not a canon violation. The axis-delta is correctly valued; the old-state traces correctly; the anchor bone is correct. I'm flagging the annotation error as a callout but not failing the facet — the underlying contract (NI fires in scene-A before or at the state-update bone) is satisfied by NI:2 @6.

## Entry-level callouts

`[state-updates:state:5] @8 — cross-facet citation claims "interest-narrator @8" but NI file has no entry at @8; closest NI spine is narrator:2 @6 (scene-A central-event bone, same peak-cluster). The annotation should read "@8 ← interest-narrator @6 (NI:2)." Substance is correct; citation label is wrong. Advisory — not a HARD contract breach since NI fires within the same scene-A peak-bone cluster.`

## Convergence trace

Auditor: no state-updates findings in Phase-5 report. The annotation error was not caught by mechanical scan. Advisory callout only.
