# Multi-judge verification — P3 (single-arm) vs P2 (multi-arm) on b01-c04
## Date: 2026-05-27 (remediation Phase D)

## Methodology

Three independent blind tournament judges (`general-purpose` agents) each ranked two variants on the same taste-aligned rubric. Position labels A/B randomized per judge to control for position-bias:

| Judge | Label A | Label B |
|-------|---------|---------|
| J1 | P3 single-arm | P2 multi-arm |
| J2 | P2 multi-arm | P3 single-arm |
| J3 | P3 single-arm | P2 multi-arm |

Each judge had no access to other judges' verdicts, no access to bones/facets/render-logs/showrunner-memory/prior-reports, and was instructed not to speculate which variant produced which mode. Rubric identical to Phase 1.5 tournament-judge rubric (9 PEEVES + 9 REWARDS, severity-weighted scoring).

## Per-judge results (un-blinded)

| Judge | Winner (label) | Winner (un-blinded) | Margin | Confidence |
|-------|----------------|---------------------|--------|------------|
| J1 | A | **P3 single-arm** | +9 vs −5 (14 pts) | high |
| J2 | B | **P3 single-arm** | +2 vs −14 (16 pts) | high |
| J3 | A | **P3 single-arm** | +4 vs −5 (9 pts) | high |

**3 of 3 judges declare P3 single-arm the winner with high confidence, position-bias controlled.**

## Aggregate findings across judges

- **Concrete handoff staging** (parchment chest-height + clean crease + inner-seam-of-coat pocketing) — P3 stages the @30/@31/@32 handoff as embodied physical event; P2 reports the same beat in flat function-token predicates ("I delivered the report-sheet. Jarvis Coin pocketed the report-sheet."). All three judges flagged this as the decisive differential.
- **Wren as named character** — J2 specifically: "B gives the central moral subject a named, quiet line ('She would not be written down… and her body would not be among them') that makes the protection-as-trap reading legible; A leaves the same beat as a function-token return." (B was P3 for J2; the moral-subject naming is the chapter's load-bearing beat.)
- **Theme-statement at chapter close** — P2 closes with "the recognition that the shape would hold the next cycle and the cycle after that" — gestured-at-recognition + theme-as-statement firing simultaneously. P3 closes with embodied stride-holds-four-count past the stitch-house frame.
- **Cost-crossing at @31** — P3: "the cost had crossed before my hand had registered it crossing" carries the cost as an embedded perceptual lag inside a sentence with weight. P2 has the same NI:7 content but in surrounding metronome cadence.

## Comparison with single-judge comparative-scorecard

The original 4-way comparative scorecard ranked P3 > P2 by 18 points (P3: −8, P2: −26). Multi-judge replication confirms direction and approximate magnitude:
- J1 spread: 14 pts
- J2 spread: 16 pts
- J3 spread: 9 pts
- Average: ~13 pts

Single-judge result and multi-judge mean are consistent within sampling noise. The direction (P3 > P2) is robust.

## Evidence for the audit

This verification confirms with multi-judge methodology what the c02 cherry-pick experiment commit (`2d525d2`) said in plain language:

> Cherry-pick fires same walkout-severity peeves as pure-winner because cost-legibility lives in bones SVO authoring, not stitch paragraph composition. Per-paragraph craft optimization is not predictive of continue-rate.

Both the c02 cold-read (CONTINUE=NO on cherry-pick) and the c04 multi-judge ranking (3/3 single-arm > multi-arm) converge on the same finding: the multi-arm + cherry-pick path does not produce reader-experience improvements over the single-arm path at this chapter's substrate.

The URI-STITCH-CHERRY-PICK-DEFAULT-ON codification was contradicted by its own cited experiment and is reverted under URI-STITCH-CHERRY-PICK-DEFAULT-OFF.

## What this does NOT establish

- This is one chapter (b01-c04) with one substrate-shape (compound-noun-heavy clinical-accounting register). It does not establish that cherry-pick is universally suboptimal for all chapter types.
- This is a single-instance comparison of a single-arm Phase-1 sample vs a multi-arm Phase-1 pair. LLM sampling variance at Phase 1 contributes meaningful noise; a multi-run comparison (N=3 single-arm × N=3 multi-arm) would more cleanly attribute to the mode rather than the sample.
- Cherry-pick remains available as an on-demand opt-in (`--cherry-pick=paragraph`) for chapters where paragraph-level craft tuning is wanted; the audit reverts only the default-on setting.

## Recommended forward path

1. Keep cherry-pick + multi-arm + tournament as opt-in capabilities, not defaults.
2. The lever the c02 experiment actually recommended (option E — cold-read FAIL → /and-write revise --from-signals) is now emphasized at Phase 9 Step 4 per URI-STITCH-COLD-READ-FEEDBACK-LOOP.
3. b01-c04 ships as P3 single-arm.
