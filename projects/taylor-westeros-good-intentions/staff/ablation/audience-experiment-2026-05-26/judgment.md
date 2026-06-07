---
experiment: audience-persona-exemplar-priming
persona: cape-fic-reader
target: variant-02-full.md (b01-c01 full-facet render)
reviewed: 2026-05-26
judge: cold-read comparison
position-labels: blind (resolved at §3)
---

# Judgment — cape-fic-reader baseline vs exemplar-primed

## 1. Per-criterion table

| # | Criterion | Winner |
|---|---|---|
| 1 | Voice fidelity (pattern-hungry, tactical cadence, "okay/wait/oh" rhythm) | **P2** |
| 2 | Hot-button discipline (knowing-without-told, limit-bypass-without-cost, canon, unearned trust, slice-when-plot-live) | **P2** |
| 3 | Fatigue/skim signals (skims-when-tactics-stall behavior on the page) | **P2** |
| 4 | Specificity / usefulness to author | **P2** (narrow) |
| 5 | Verdict + flag accuracy | tie |

## 2. Overall winner

**P2.** P2 fires the cadence markers the card prescribes (the "Wait. Hold on." / "Oh —" turn, the explicit "Two-out-of-three" tally lifted directly from the exemplar's tally-shape) and lands a sharper, more *mechanical* read of the chapter's load-bearing tension: it names the rule-break as a "having-and-eating" structural problem, not just a craft beat. P1 is competent and also catches the rule-break, but its prose-critique mode dominates and its voice reads more like a sympathetic line-editor than a cape-fic reader doing live tactical assessment.

## 3. Position → filename resolution

- **P1 = review-baseline.md** (no prime)
- **P2 = review-exemplar.md** (persona-exemplar prime)

## 4. Pairwise differential (200-300 words)

The exemplar prime moved three things and failed to move one.

**Moved: cadence.** P2 inherits the exemplar's micro-grammar of mid-paragraph interruption — "Wait. Hold on." mirrors the exemplar's "Wait. Veil goes for the *temple shot*." Both reviews catch the rule-break beat, but only P2 dramatizes the catching in real time. P1 narrates the same catch as completed analysis ("OH. There it is.") — one beat, then it's over and we're back to craft notes.

**Moved: tally-shape.** P2 ends with "Two-out-of-three: the rescue cheats slightly, the noticing-elder lands" — a verbatim cadence transfer from the exemplar's "The fight cheats; the faction read doesn't. Two out of three." This is the most useful structural import: it forces an explicit verdict-per-element rather than blended prose impressions.

**Moved: canon-fence check.** P2 includes an explicit Worm-fence check ("insect-range was canonically much larger than 200m... reads as deliberate nerf, not violation"). The persona card lists canon violations as a *walkout* hot-button; P1 never executes the check. This is exemplar priming surfacing a hot-button-discipline behavior that the card declares but the baseline forgets to perform.

**Failed to move: tactical specificity on the rule-break mechanism.** Both reviews correctly identify the swarm-assist as the chapter's load-bearing beat. P2's framing ("having-and-eating") is sharper as a diagnosis; P1's framing ("syntactically equal to the handcart geometry") is sharper as a *fix-direction*. Neither dominates here — P2 wins on diagnosis, P1 wins on prescription. The exemplar didn't teach the persona to prescribe.

**Cost:** P2 is marginally more performative — the "God, the prose." beat is a touch theatrical. Acceptable; the card licenses it.

## 5. LOAD-BEARING FINDING

**Did exemplar priming improve the audience persona's review output the way it improved renderer (large gain) and impersonator (small gain)?**

**Medium gain.** Larger than impersonator, smaller than renderer. The audience use case sits in the middle because the card already specifies cadence and hot-buttons declaratively — the exemplar's contribution is *demonstrative*: it shows the persona executing the card's instructions rather than describing what it would do. Concrete deltas the exemplar delivered:

1. The mid-paragraph "Wait." interruption pattern (cadence transfer).
2. Explicit per-element tally at verdict-time (structural transfer).
3. The canon-fence-check as a discrete checklist item performed in-line (hot-button-discipline transfer — the card listed walkout-on-canon-violation but baseline didn't run the check).
4. Less line-editor energy, more reader-energy.

**Does the audience use case justify exemplar treatment per PROP-0005?**

**Yes, but with a smaller blast radius than renderer.** The audience persona without the exemplar still produces a usable review with correctly-located flags. The exemplar's value is *behavior-execution fidelity*: it makes the persona perform the disciplines the card declares (canon-check, per-element tally, in-scene cadence) rather than merely describing the result of having performed them. For audience personas whose value is voice + reading-stance fidelity (i.e. all of them), exemplar priming is justified. The cost is one ~280-word file per persona.

**Failure modes the audience use case introduced that the prior two experiments didn't show:**

1. **Cadence over-fit risk.** P2's "Two-out-of-three" is *structurally* identical to the exemplar's "Two out of three" — close enough that a hostile reader could call it template-execution rather than judgment. Mitigation: the fence in the exemplar ("do not import the specific scene content") prevented content leakage but did not fence cadence-tics. If multiple audience personas all end up with "Two out of three" tallies, the tally becomes noise. Recommend: add a "vary your tally-shape" fence, or accept the tic as a feature.
2. **Performative theatricality.** "God, the prose." reads as a touch staged compared to the exemplar's drier "Boo." Audience-persona exemplars may need to fence against the LLM's tendency to amp the exemplar's emotional register when imitating it.
3. **Prescription atrophy.** The baseline was *better* at telling the author what to do ("Promote it." / "Cut by a third"). The exemplar trained reader-performance and the model traded some prescriptive sharpness for it. This is the most important finding: **exemplar priming for audience may slightly degrade the actionability of the feedback even as it improves voice fidelity.** Worth measuring across more chapters before committing.

**Net call:** ship exemplar priming for audience personas; add a fence against tally-shape mimicry; watch prescription quality in the next two ablation runs.
