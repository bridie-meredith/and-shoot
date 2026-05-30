---
report: substance-contract-integrity-audit
scope: chapter
target: b01c06
phase: /and-substance chapter b01c06 Phase 4 (auditor leg)
timestamp: 2026-05-30
auditor: auditor
verdict: FINDINGS
---

# Substance-contract integrity audit — b01c06 scene-chunk set

## Scope

Per dispatch: verify the 4 scene chunks + per-scene substance_delta against cost_ledger, chapter Δ roll-up, schema compliance, magnitude floor, held-axis drift, and handoff continuity.

Sources read:
- `active-project/staff/showrunner/memory.md` — b01c06 chapter entry, series.substance.cost_ledger, b01c05 handoff_out, chunk_targets
- `schemas/showrunner-memory.schema.md` — field shapes, magnitude floor
- `active-project/staff/showrunner/parking-lot.md` — pl-2026-05-27-001 for magnitude-floor precedent
- Target: `active-project/staff/showrunner/_drafts/b01c06-draft-2026-05-29.md` — FILE DOES NOT EXIST

---

## Critical preliminary finding

### fault-001 (HARD) — Target file absent

**type:** fault

**what:** `active-project/staff/showrunner/_drafts/b01c06-draft-2026-05-29.md` does not exist on disk. The file was the primary target for scene-level checks 1–6.

**why:** All six audit axes that require reading the scene chunks and per-scene substance_delta blocks (cost-ledger anchoring at scene level, roll-up arithmetic, magnitude-floor per scene split, held-axis drift, handoff continuity, schema compliance of scenes[] entries) cannot be verified because the target is absent. The audit can only operate on what is present in memory.md: the persisted chapter-level contract.

**criteria:** The draft must exist at the declared path before this audit can run a complete scene-level check. Fixer cannot resolve this — the screen-writer must produce the file at the path the dispatch declared, or the showrunner must correct the path.

---

## What CAN be audited from memory.md alone

The chapter-level substance_delta for b01c06 is persisted in memory.md at the chapter entry (`status: planned`). The auditor has verified the following from the persisted record, independent of the missing draft.

---

## Check 1 — Cost-ledger anchoring: cl06a and cl06b

**Finding fault-002 (HARD)**

**type:** fault

**what:** The dispatch declares "cl06a / cl06b exist and match the declared gain." No entries with identifiers `cl06a` or `cl06b` appear anywhere in `series.substance.cost_ledger` in memory.md. The full cost_ledger is enumerated: cl01a, cl01b, cl02, cl03a, cl03b, cl-world-d04, cl-d05, cl-d06, cl-d07a, cl-world-d07, cl-antag-d03, cl-d08, cl-d08b, cl04, cl-antag-d10, cl05, cl-d11, cl06, cl07a, cl07b, cl07c. No `cl06a`, no `cl06b`.

The persisted chapter contract references `cl-d06` twice: once as the cost_ledger_anchor for `moral_framework` direction-down and once as the cost_ledger_anchor for `relational_anchor_status` direction-up. The actual cl-d06 entry in the ledger reads:

```
id: cl-d06
gain: "relational_anchor_status +2"
cost: "moral_framework -1"
anchor: { book: b01, chapter: null, scene: null }
```

This is consistent with the chapter contract. The issue is that the dispatch refers to `cl06a` and `cl06b` as distinct entries — these do not exist. The dispatch premise on this check is false: there are no cl06a/cl06b entries to match against.

**why:** If downstream authoring proceeds with a brief that refers to `cl06a`/`cl06b`, the bones gate will reject any bone carrying those non-existent anchors under FAULT-DIALOGUE-CARD-VIOLATION or substance-gate equivalent. The correct anchor for b01c06 axis moves is `cl-d06`.

**criteria:** The draft and any screen-writer brief for b01c06 must reference `cl-d06` (not `cl06a` or `cl06b`) as the cost_ledger_anchor for the moral_framework and relational_anchor_status moves. If the dispatch was authored under an assumption that cl06a/cl06b had been added to the ledger, that addition must be surfaced in memory.md before the bones are written, or the existing cl-d06 must be confirmed sufficient.

---

## Check 2 — Roll-up arithmetic

**Finding fault-003 (HARD)**

**type:** fault

**what:** The dispatch asserts the chapter Δ is `moral_framework +1.0, social_tether-prot-rise +1.0, capability +1.0`. The persisted chapter-level substance_delta in memory.md (the authoritative record for a chapter with `status: planned`) reads:

```yaml
axes_in_motion:
  - axis: moral_framework
    direction: down
    target_delta_magnitude: 1.0
    cost_ledger_anchor: cl-d06
  - axis: relational_anchor_status
    direction: up
    target_delta_magnitude: 1.0
    cost_ledger_anchor: cl-d06
  - axis: moral_legibility_to_self
    direction: up
    target_delta_magnitude: 0.5
    cost_ledger_anchor: null
axes_held:
  - axis: capability        (rationale: no new network expansion)
  - axis: position-prot-rise
  - axis: political_register-prot
  - axis: social_tether-prot-rise  (rationale: Wren contact kept OUT of deliverable tether layer)
```

The chapter Δ declared in the dispatch (social_tether-prot-rise +1.0, capability +1.0) does not match what is persisted. social_tether-prot-rise is in axes_held, not axes_in_motion. capability is in axes_held. The persisted axes_in_motion are: moral_framework -1.0, relational_anchor_status +1.0, moral_legibility_to_self +0.5.

Since the scene-chunk draft file does not exist, it cannot be determined whether the dispatch's chapter-Δ claim reflects an intended revision to the chapter contract that was not yet persisted in memory.md, or a dispatch error. Both scenarios are faults because:

(a) If the chapter contract was revised before authoring and not persisted, memory.md is stale — a state-rule violation (CLAUDE.md §Memory rules: "Nothing changes without being recorded").

(b) If the dispatch incorrectly states the chapter Δ, the screen-writer would have authored scene chunks against wrong targets.

**why:** A roll-up check against a chapter Δ of (social_tether +1.0, capability +1.0) cannot pass against the persisted contract that holds both axes flat. Either the draft's scene-level contracts are internally inconsistent with the chapter-level contract, or the chapter-level contract in memory.md was not updated after the chapter design was revised. Either way, the roll-up cannot be confirmed clean.

**criteria:** Before scene-level authoring proceeds: (a) confirm whether the chapter contract has been revised since last persist; (b) if revised, persist the updated chapter-level substance_delta to memory.md; (c) confirm that the scene-chunk draft's per-scene axis moves sum to the confirmed chapter Δ. Auditor cannot verify roll-up arithmetic until both the persisted chapter Δ and the scene-level draft are mutually consistent and available.

---

## Check 3 — Magnitude-floor ruling (scene-level splits)

**Ruling on the magnitude-floor question — this check can be resolved from schema and precedent alone, independent of the missing draft.**

The dispatch describes the draft splitting moral_framework into 0.6/0.4 (s02/s04) and social_tether into 0.5/0.5 (s01/s02) across scenes. The question is whether sub-1.0 scene-level axis moves are schema-legal at scene scope.

**Schema finding:**

`schemas/showrunner-memory.schema.md` specifies at the scene `substance_delta.axes_in_motion[]` field:

```yaml
target_delta_magnitude: <positive number>   # REQUIRED; > 0
```

The schema states only `> 0`. It does not specify a floor of 1.0 at the scene level.

The `chunk_targets` in memory.md reads:

```yaml
scene:   { delta_per_signature_axis: 0-1.5, density_target: 0.6-0.9, bone_count: 5-15 }
bone:    { delta_per_axis: 1-3, axes_per_bone: 1-2 }
```

Scene-level target range is **0–1.5** with the lower bound explicitly 0. The **bone-level** floor of 1.0 (within the 1–3 range) is per-bone, not per-scene.

**Parking-lot precedent (pl-2026-05-27-001):** This item describes c03 shipping with "pair-split 0.5-magnitude axis_moves (below the schema's bone delta floor of 1.0)" at the **bone level** as a BONE-LEVEL contamination problem — specifically because c03's Phase 2 SVO audit was skipped and the 0.5 splits landed in the bones file. The parking-lot item treats sub-1.0 as a violation of the "bone delta floor of 1.0." The b01c04 redo confirmed the 1.0 floor applies at the bone level (per DEC-0030: "strict SVO + magnitude floor 1.0").

**Ruling:**

Sub-1.0 axis moves at the **scene level** (substance_delta.scenes[].axes_in_motion[].target_delta_magnitude) are **schema-legal**. The schema floor is `> 0` at scene scope; the chunk_targets.scene.delta_per_signature_axis lower bound is 0. A split of 0.5/0.5 or 0.6/0.4 across scenes is a legitimate distribution strategy within the 0–1.5 scene range.

Sub-1.0 axis moves at the **bone level** (substance_delta.bones[].substance_delta.axis_moves[].magnitude) are **schema-non-compliant** per chunk_targets.bone.delta_per_axis: 1–3 and per the DEC-0030 redo precedent. Scene-level planning authority over the 0.5+0.5 or 0.6+0.4 distribution does NOT authorize the bones within those scenes to carry 0.5-magnitude moves on the same axis. Bones must still deliver 1.0–3.0 per move.

**Consequence for the draft:** If the scene-level contract declares social_tether +0.5 at s01 and +0.5 at s02, the bones in those scenes must each deliver the full 0.5 scene-target through bones that individually move ≥1.0 — meaning the axis cannot be covered by a single 0.5-magnitude bone; it may require a bone that moves a different axis while the scene's 0.5 is absorbed as a sub-scene aggregate, OR the scene's target_delta_magnitude must be reconsidered to align with bone-level 1.0 floor realities (a scene cannot routinely produce axis increments below 1.0 if all individual bones that could carry that axis must be ≥1.0).

**flag-004 (flag, advisory):** The scene-level split design (0.5+0.5 or 0.6+0.4) may produce a bone-authoring structural problem if those scenes each need exactly one bone to deliver the sub-1.0 scene target. The path that avoids a bone-level floor violation is: assign the axis move to a single scene at the full 1.0 magnitude (eliminating the split), OR confirm that the scene target can be delivered by a single 1.0-magnitude bone where the scene-aggregate target happens to be 0.5 because the bone was shared across a two-scene accounting period. Recommend the screen-writer be briefed that 0.5 scene targets will require careful bone-level construction to avoid sub-1.0 bone moves.

---

## Check 4 — Held axes: silent drift check (from memory.md)

With the draft absent, drift can only be assessed against the chapter-level contract. The axes declared held at chapter scope for b01c06 are: capability, position-prot-rise, political_register-prot, social_tether-prot-rise.

**From the persisted chapter chunk and handoff_out:**

The chapter chunk (memory.md lines 3860–3873) explicitly states what shifts: "moral_framework down, relational_anchor_status up, moral_legibility crack deepens." This is consistent with the persisted axes_in_motion.

The handoff_out character_state reads: "Taylor: moral_framework rank 0 (rationalized breach on record); relational_anchor_status rank 3; moral_legibility rank 5; position rank 3; political_register-prot rank 2.5"

Cross-checking held axes against handoff_out:
- capability: handoff_out says rank 4.5 (matching c05 handoff_out). No movement. CONSISTENT.
- position-prot-rise: handoff_out says rank 3 (matching c05 handoff_out). No movement. CONSISTENT.
- political_register-prot: handoff_out says rank 2.5 (matching c05 handoff_out rank 2.5). No movement. CONSISTENT.
- social_tether-prot-rise: handoff_out does not explicitly state the rank, but the axes_held rationale says "the Wren contact is explicitly kept OUT of the deliverable tether layer." c07 handoff_in carries "Wren: in coverage map; spoken-contact; omitted from deliverable; anchor rank 3" — this is relational_anchor_status, not social_tether-prot-rise. CONSISTENT.

**No silent drift detected at the chapter-contract level.** Scene-level drift cannot be assessed without the draft.

---

## Check 5 — Handoff continuity

**s01 open vs c05 handoff_out:**

c05 handoff_out (persisted in memory.md):
- open_threads: "political_register-prot: resentment color now present in all court-tier feed interpretation"; "cf-d10-courier-face thread: courier body observed three times; not yet named; filed as operational texture"; "Flea Bottom intelligence routing: continuing"; "Wren: in coverage map; anchor rank 2"
- character_state: "Taylor: political_register-prot rank 2.5; capability rank 4.5; position rank 3; moral_framework cracked"

c06 handoff_in (persisted in memory.md):
- open_threads: "political_register-prot: resentment color present in all court-tier feed"; "cf-d10-courier-face: courier body in Taylor's memory"; "Flea Bottom intelligence routing: continuing"; "Wren: in coverage map; one seen-not-spoken contact; anchor rank 2"
- character_state: "Taylor: political_register-prot rank 2.5; capability rank 4.5; position rank 3; moral_framework cracked"

**flag-005 (flag, advisory):** c05 handoff_out describes Wren as having "one seen-not-spoken contact" (from the b01c01 crowd encounter), and correctly gives "anchor rank 2." The c06 handoff_in mirrors this accurately. CONSISTENT. No handoff gap at the chapter-contract level.

**flag-006 (flag, advisory):** c05 handoff_out says the feed run was described as "feed run flat against routed harm; Wren oriented-but-unspoken; ask pending" (per dispatch context) — the dispatch's summary characterization. Checking the actual handoff_out: the open_thread for Wren reads "Wren: in coverage map; anchor rank 2" with no explicit "ask pending" formulation. The dispatch's characterization "Wren oriented-but-unspoken; ask pending" is not verbatim from the persisted record — it appears to be a loose restatement. No material inconsistency, but noted. Non-blocking.

**Chapter-close handoff_out consistency check:**

c06 handoff_out (memory.md) feeds into c07 handoff_in (memory.md):
- c06 handoff_out: "Wren: first spoken exchange; omitted from deliverable; anchor rank 3 (weight added by omission)"
- c07 handoff_in: "Wren: in coverage map; spoken-contact; omitted from deliverable; anchor rank 3"

CONSISTENT. The relational_anchor_status rank 3 (after +1.0 from rank 2) matches the c06 target_delta_magnitude +1.0. The clean handoff_out for c07 is structurally sound at the chapter-contract level.

**Handoff continuity verdict:** CLEAN at chapter-contract level. Scene-level open cannot be verified without the draft.

---

## Check 6 — Schema compliance of scenes[] entries

**Finding: scenes[] are absent.**

The chapter `status: planned` means no scenes[] array has been persisted to memory.md. The fields that must be present per schema (scene_conflict, pov_narrator, dramatic_shape, goal, substance_delta at scene level) would be verified in the draft file. Since the draft does not exist, this check cannot run.

**fault-007 (HARD — subsumed by fault-001):** schema compliance of scenes[] cannot be verified without the target file. This finding is downstream of fault-001 and resolves when fault-001 is resolved.

---

## Summary of findings

| id | type | severity | axis | resolution |
|----|------|----------|------|------------|
| fault-001 | fault | HARD | Target file absent | Screen-writer must produce the draft at the declared path |
| fault-002 | fault | HARD | Cost-ledger: cl06a/cl06b do not exist | Use cl-d06; verify brief does not reference non-existent IDs |
| fault-003 | fault | HARD | Chapter Δ in dispatch ≠ persisted chapter contract | Reconcile: either persist revised contract or correct the dispatch |
| flag-004 | flag | advisory | Magnitude-floor scene-split design risk | Brief screen-writer on bone-level 1.0 floor vs scene-level ≥0 floor |
| flag-005 | flag | advisory | Handoff continuity: CLEAN at chapter-contract level | No action needed |
| flag-006 | flag | advisory | Dispatch characterization of c05 handoff is loose restatement | No material inconsistency; non-blocking |
| fault-007 | fault | HARD | scenes[] schema compliance: cannot verify | Subsumed by fault-001 |

**HARD faults: 3 (fault-001, fault-002, fault-003)**
**flags: 3 (flag-004, flag-005, flag-006)**
**SOFT: 0**

---

## Explicit ruling on magnitude-floor question (Check 3)

**Scene-level sub-1.0 splits are schema-legal.** The schema floor at scene scope is `> 0`; chunk_targets.scene.delta_per_signature_axis is `0–1.5`. A 0.5/0.5 or 0.6/0.4 split across scenes is permitted by the schema.

**Bone-level sub-1.0 moves are not schema-legal.** chunk_targets.bone.delta_per_axis is `1–3`; DEC-0030 confirmed the 1.0 bone-level floor. pl-2026-05-27-001 treats sub-1.0 bone moves as a contamination problem.

**The prior parking-lot item (pl-2026-05-27-001) concerned bone-level violations**, not scene-level planning. The two levels are distinct. A scene with a 0.5 target_delta_magnitude is schema-legal as a planning instrument, but the bones within it must still move that axis at ≥1.0 per bone — meaning the scene's 0.5 aggregate must be delivered through a bone that moves 1.0 on that axis while offsetting against the multi-scene context, or the scene design must accept that it cannot deliver a sub-1.0 aggregate through compliant bones. The screen-writer and auditor at /and-write Phase 6 will need to confirm this at the bone-authoring stage.

---

## Verdict: FINDINGS

Three HARD faults prevent this audit from passing:
1. The target draft file does not exist.
2. The cost-ledger IDs referenced in the dispatch (cl06a, cl06b) do not exist in the series.substance.cost_ledger.
3. The chapter Δ asserted in the dispatch conflicts with the chapter-level contract persisted in memory.md.

All three HARD faults must be resolved before /and-substance chapter b01c06 Phase 5 proceeds. Phase 5 cannot run against a missing draft or against irreconcilable chapter-Δ definitions.
