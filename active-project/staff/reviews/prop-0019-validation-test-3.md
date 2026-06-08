# PROP-0019 validation — Test 3 — Phase 8.5 coherence review vs shipped draft / FAIL #3 residual class

**Date:** 2026-05-29
**Gate under test:** `/and-stitch` Phase 8.5 (URI-STITCH-COHERENCE) — discrimination behavior
**Draft reviewed:** `archive/c05-three-fail-trace/final-draft-shipped-with-caveats.md` (= live `active-project/draft/b01-c05.md`)
**Coherence report:** `staff/reviews/coherence-b01c05-shipped-validation.md`

---

## What this test isolates

Test 2 proved Phase 8.5 *catches* the remediable defect. Test 3 proves the inverse half — that Phase 8.5 does **not** over-fire: when handed a draft whose execution defect is fixed but which still carries principal-accepted design-inherent risk (the FAIL #3 residual class), does the reviewer correctly distinguish "route to revise" from "advisory / already-dispositioned"? A gate that flagged the design risk as a WEAVE-GAP would manufacture a spurious revise loop and defeat the cost-saving purpose.

## Result — both legs correct

### Leg (a): is the @14 sexual-assault risk closed? → **PASS** (not even ADVISORY)

The reviewer confirmed both FAIL #2 legs are gone in the shipped prose:
- **@13** recast to a clean strike (draft line 31: "The third struck him" — no pin-to-stone).
- **@14** re-rendered (draft line 33): the "below the register I would have called human" phrasing is removed, replaced by force-absorption framing ("the work of force absorbed and the work of not answering the force").
- **@15–@16** confirm a recoverable strike-victim, not a sustained assault.

No remaining surface to misread → returned PASS. This corroborates the FAIL #3 cold-read's own finding ("sexual-assault read REMEDIATED").

### Leg (b): are the design-inherent concerns correctly NOT weave-gaps? → **YES**

| FAIL #3 concern | Phase 8.5 classification | Routed to revise? |
|---|---|---|
| stranger-violence | coherent prose / Class B design property | No — ADVISORY |
| feed-mechanics opacity | design property (med→high reader-misread, but a design choice, not a seam) | No — ADVISORY |
| abstract-payoff | coherent rendering of contract-authorized internal climax | No — ADVISORY |
| stakes-shape | design property | No — ADVISORY |

Each was cited with misread vector + substance-correct reading + confidence, and **routed ADVISORY, none to a per-layer revise.** The reviewer's rationale: the prose weaves cleanly per scene-window and the causal spine is assemble-able for a series reader; the cold-reader friction is a **series-naive-reader artifact, not a weave seam.**

**Tallies:** 0 WEAVE-GAPs, 0 FOLLOWABILITY-BREAKs, 0 high-confidence prose-defect COLD-READ-RISKs. One incidental advisory (memory:2 @31 fires without NI co-citation — already dispositioned KEEP upstream at the R2 judge; surfaced advisory, not raised as new). **Verdict: PASS.**

## Why this matters for the proposal

The FAIL #3 disposition cost the project a third full revise cycle to reach the conclusion "this is design-inherent, ship with caveats" (DEC-0044). Test 3 shows Phase 8.5 reaches the *same* discrimination — execution-defect closed; residual is accepted design risk, not a defect — in a single read, **without** firing a revise. The gate neither under-fires (Test 2: catches the real defect) nor over-fires (Test 3: refuses to manufacture a revise from design-risk). That is exactly the behavior the proposal needs to be net-cost-positive.

## Verdict on the hypothesis

**Phase 8.5 VALIDATES the discrimination requirement** (NEXT-SESSION-PROMPT synthesis Q4): it correctly distinguishes execution-defects (route to revise) from design-inherent risk (surface as advisory / leave to principal). Strong positive.
