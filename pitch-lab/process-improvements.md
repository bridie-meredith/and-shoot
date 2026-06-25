# pitch-lab — process improvements (running log)

Harvested during the 33-pitch tournament. Tournament-internal findings stay here; findings that expose a real gap in the core and-shoot pipeline are escalated to `staff/admin/process-proposals.md` (per DEC-0121). Format mirrors a lightweight proposal: `PI-NN [scope] — finding → change`.

---

## PI-01 [process] — Summarizer must be a separate, faithful-compression role, not folded into the evaluator
**Finding (Round 0 design):** The temptation is to have one agent summarize-and-score in a single pass to save dispatches. That couples the compression to the judgment — a summarizer that knows it is also the judge will smooth over weaknesses to make a plan it likes look better, defeating the tournament's selection function.
**Change:** Summarizer and evaluator are split. The summarizer's only job is faithful compression + honest weakness-flagging (`[ABSTRACT-ENGINE]`/`[UNPAID]`/`[FLAT-PRESSURE]`/`[NO-TURN]`). The evaluator judges the standardized summary surface, never the raw plan. This makes word-count and idiosyncratic emphasis non-load-bearing and surfaces weaknesses as machine-readable flags.
**Status:** adopted (summarizer-spec.md, evaluator-rubric.md).

## PI-02 [content] — Pre-warning the expander about a prompt's specific abstraction trap measurably improves concreteness
**Finding (Round 0):** P12 (breath-ledger) is the archetypal DEC-0115 trap — "a ledger of every breath," "the count tells him." The expander brief for that batch named the trap explicitly ("the count/ledger as grammatical subject is the disease; push to concrete human action"). The returned plan rendered the engine as a man physically scratching marks while people fall out of the city's memory "like a stone from a wall," and administrators rubbing out marks with a cloth — concrete, picturable, no bookkeeping-as-subject.
**Change:** When expanding a prompt whose imagery courts an abstract engine, the expander brief should name the specific trap for that prompt, not just cite the general rule. Per-prompt trap-naming beats generic rule-citation. (Candidate cross-pipeline escalation: `/and-write` Phase 6 could carry a per-scene "named abstraction risk" hint derived from the chunk, not only the post-hoc ABSTRACTION-AS-SUBJECT gate.)
**Status:** adopted in batch briefs; escalation candidate noted.

## PI-03 [process] — The gate must be three-way (promote / rework / eliminate), or the tournament silently keeps the mediocre
**Finding (Round 0 design):** A pass/fail gate either keeps too much (low bar) or discards fixable-but-currently-short plans that are actually the best raw material (high bar). Neither converges on "the bestest."
**Change:** Every plan at every round is promoted, reworked (cap 2/tier), or eliminated *with a logged reason*. "Rework until best" is literally the gate's middle branch applied at rising tiers. The hardest tiers spend most of their effort in the rework branch, lifting near-best plans rather than discarding them.
**Status:** adopted (RUNBOOK.md T2/T3, evaluator-rubric.md Tier 3-4).

## PI-04 [process] — Escalate the critic's STANCE, not just the numeric threshold
**Finding (Round 0 design):** Raising the total-score floor each round is necessary but not sufficient — a generous critic re-applied at a higher floor just inflates scores to clear it. Real discrimination requires the critic's posture to shift from "credit what works" (Tier 1) to "find the reason to reject" (Tier 3) to "actively try to kill every plan" (Tier 4 adversarial pass).
**Change:** Each tier specifies a critic stance (generous → neutral → skeptical → adversarial) alongside the numeric bar. Tier 4 is an adversarial gauntlet of four named attacks (generic / naive-follow / unavoidability / one-image) that a plan must survive.
**Status:** adopted (evaluator-rubric.md tier stances).

## PI-05 [process] — When the field over-performs the opening tier, ramp difficulty by stance + anti-inflation anchors, not by threshold alone
**Finding (Round 1):** All 33 plans cleared Tier 1; the generous gate did zero selection work because the field was uniformly strong (the screen-writer expansion brief was demanding enough that weak plans never entered the tournament). Scores bunched in a narrow 16-24 band with six plans tied at the top.
**Change:** When a round promotes >~⅔ of the field, the next round must (a) adopt a skeptical stance AND (b) supply explicit anti-inflation calibration anchors — "reserve 5 for the top ~15% on this axis; a field this strong should still spread 2-4; more than N fives in a column means you are inflating." Re-score from scratch; do not just re-threshold the prior round's numbers (those were generated under a generous stance and are upward-biased). This converts a bunched field into a separable one without inventing artificial weaknesses.
**Status:** adopted (Round 2 brief).

## PI-06 [content] — A demanding expansion brief is the cheapest quality lever in the whole pipeline
**Finding (Round 1):** Zero `[ABSTRACT-ENGINE]`/`[UNPAID]`/`[NO-TURN]` flags across 33 plans. The expansion briefs hard-coded the project's discriminators (DEC-0115 concreteness, paid cost ledger, escalating antagonist pressure, real road-to-hell turn) as HARD REQUIREMENTS up front. The result: the evaluator spent its effort discriminating *among strong plans* rather than rejecting broken ones.
**Change:** Front-load the discriminators into the generator brief, not just the evaluator. It is far cheaper to prevent a flaw at expansion than to detect-and-rework it later. (Cross-pipeline parallel: this is the same logic as `/and-write`'s bone-gate criteria being known to the bone *author*, not only the auditor.)
**Status:** validated.

## PI-07 [process] — Spend rework budget where it can change the WINNER, not where it pads the shortlist
**Finding (Round 2-3):** With a strong field, many plans land just below the bar with a fixable flaw. Reworking all of them is expensive and pointless if they still can't reach the top 3. At Round 3, six plans earned REWORK but five clean promotes already filled the contender pool.
**Change:** Carry into rework only the near-misses whose lift could plausibly displace a current top-tier plan — judged by (a) how close the fix gets them and (b) whether a prior round rated them top. Log the rest with their fix instruction as "honorable mention, not carried." This keeps the iterate-to-best loop pointed at the decision, not at completeness.
**Status:** adopted (Round 3 carried only P03, P32 of 6 reworks).

## PI-08 [content→ESCALATE candidate] — Re-judge concreteness at a HARDER stance downstream of the summarizer; the summarizer's pass is necessary but not sufficient
**Finding (Round 2):** P12 (breath-ledger) passed the summarizer's concreteness check (engine rendered as "a man scratching marks; people fall out of memory like a stone from a wall") but the skeptical Round-2 evaluator caught it as abstract under harder reading ("marks *select for persistence*" is a metaphysical assertion, not a physical mechanism). The DEC-0115 trap the expander was warned about reappeared two layers downstream.
**Change:** Concreteness must be gated more than once, at rising stances — exactly as the and-shoot pipeline already does (write-time bone-gate → stitch Phase 4 → Phase 9 naive-follow). A single concreteness check anywhere is insufficient; the disease hides from a generous reader and surfaces under a skeptical one.
**Status:** local-adopted. **ESCALATE candidate:** this is a genuine cross-pipeline confirmation that DEC-0115's multi-surface enforcement is correct — worth a note to staff/admin that the pitch-lab independently reproduced the "abstraction survives a single lenient gate" failure mode.

## PI-09 [content] — In a concreteness-and-substance-disciplined field, ORIGINALITY is the axis that actually selects
**Finding (Round 3):** All four Tier-3 eliminations (P05, P09, P26, P31) died on the same disqualifier: Originality capped at 3 because the *engine* was a nameable archetype, even though concreteness, cost, and antagonist pressure were all solid. When the generator brief enforces C/S/D well (PI-06), every survivor is followable and substantial — so the discriminator shifts entirely to "is the mechanism one I can name."
**Change:** Once a field is concreteness-disciplined, weight the evaluator's escalation toward originality and have it state the "X meets Y" name explicitly — a plan that can be named is capped; a plan whose mechanism resists naming wins. The single most useful evaluator output at the hard tiers is the attempted name of the engine.
**Status:** adopted (Tier 3/4 O-cap rule + generic-attack).

## PI-10 [process] — Inter-round score DISAGREEMENT is the signal for where rework should adjudicate
**Finding (Round 2 vs 3):** P03 was called "strongest plan in the field" at Round 2 and merely-competent (all 4s, no exceptional axis) at Round 3. That variance is not noise to average away — it marks a plan whose quality is real but unevenly surfaced, which is exactly what a targeted rework can fix.
**Change:** When a plan's rank swings hard between rounds, prioritize it for rework over a plan that is stably mid. The tournament's own scoring variance is a free signal for where a lift has the most headroom. (P03's rework targeted the two axes Round 3 dinged; outcome judged in Round 4.)
**Status:** adopted.

## PI-11 [process] — A rework instruction only works if it names the exact axis AND the exact concrete change; "make it better" is inert
**Finding (Round 3-4):** Both reworks (P03, P32) landed on the first pass because the evaluator's REWORK directive was surgical: not "improve originality" but "reveal the ordination ceremony itself was a guild contract, so faith was commercial property before he held it." The screen-writer could execute it directly with no guesswork.
**Change:** Make the specific-actionable-fix a HARD requirement of any REWORK verdict (already in evaluator-rubric.md honesty discipline). The evaluator that finds a flaw must also author the fix at the level of a concrete scene/mechanism change. This is the difference between a tournament that converges and one that thrashes.
**Status:** adopted + validated (2/2 reworks cleared on first pass).

## PI-12 [process] — A gauntlet (survival filter) is the WRONG frame; a discerning critic + feedback loop is the right one
**Finding (principal feedback):** The Tier-4 gauntlet passed its three finalists at 24/25 each. A reviewer that grades its own survivors at near-perfect is curving, not judging — and a gauntlet produces *survivors*, never *insight*. It never tells the generator how to improve.
**Change:** Replace the gauntlet with a **discerning critic** (`reviewer-spec.md`) whose job is to (a) place each summary honestly on an awful→best spectrum and (b) emit insight to improve both the summary AND the generator. "Best" = highest honest band under the harshest independent review, not last-one-standing. Validated: independent forks sorted a deliberate spectrum to 3/4 (awful straws) · 17 (weak) · 18-19 (strong), refusing to award BEST to any.
**Status:** adopted (gauntlet retired; reviewer-spec.md is authoritative).

## PI-13 [process] — Reviews must be INDEPENDENT BLIND FORKS, one per summary
**Finding (principal feedback):** One critic batch-scoring a field curves (scores relative to the batch) and anchors (early scores set the scale). 
**Change:** Each review is its own fork seeing exactly one summary and nothing else — no other summaries, no other scores, no tournament history. Convergence is then real, not curved (three separate forks independently landed P01/P09/P32 at 19). 
**Status:** adopted.

## PI-14 [process] — Escalate by refreshing the critic's BAR each pass, and recalibrate the scale so a 5 is near-unreachable
**Finding (principal feedback, twice — "24/25 too nice", then "still not critical enough"):** Capping fives-per-column wasn't enough; the strong plans still floated to GOOD (18-19). 
**Change:** An escalation ladder (L1 generous → L2 skeptical → L3 brutal), where each pass is told the prior was too soft and raises its bar. The brutal anchor: *a pitch is unproven potential; credit only what's demonstrated; treat unproven payoff as a liability.* Re-scored, the strong plans dropped to BAD (12-13). A genuinely strong but unproven pitch should land BAD–MEDIOCRE; GOOD requires defeating every attack; BEST is near-impossible for a pitch.
**Status:** adopted (reviewer-spec.md escalation ladder + L3 attacks).

## PI-15 [process] — Independence has a blind spot; pair blind forks with a non-blind FIELD-CRITIC
**Finding:** Blind forks each see one plan, so none can see that the whole field is one shape repeated. That sameness is the single most damning criticism of this field and was invisible until a non-blind field-critic read the strong plans together.
**Change:** A multi-prompt run requires BOTH independent blind forks (per-plan discernment, no curve) AND one non-blind field-critic (shared-formula / range / sentimentality / what-none-of-them-do). They are complementary.
**Status:** adopted (reviewer-spec.md field-critic role).

## PI-16 [content→ESCALATE candidate] — The 33-prompt brief over-selected ONE shape; coverage must be a designed constraint
**Finding (field-critic):** All 33 prompts (and certainly the top of the field) are the tragic-irony-mechanism shape — "a power whose use IS the harm." No comedy, no hope, no winnable plot, no human antagonist, no tonal range. The defect is upstream: the generation brief rewarded individual tragic-irony quality and never solicited range, so the field converged.
**Change (GEN-v2 R8):** A field brief must fill explicit tonal slots (tragic/comic/ambiguous/adventure/mystery), require a human antagonist in ≥⅓, require ≥1 winnable-protagonist prompt, and PENALIZE structural convergence. **ESCALATE candidate:** this is the same failure mode as a substance signature collapsing to a single register (DEC-0115/0120 lineage) — a note to staff/admin that "diversity/coverage as an explicit anti-convergence constraint" generalizes to series-level premise generation in the core pipeline.
**Status:** local-adopted (generator-spec.md R8); escalation candidate noted.

## PI-17 [criteria] — Five axes are too few to judge a pitch; expand to ten and tie fields 1:1 to criteria
**Finding (principal feedback):** The C/D/S/O/A set omits stakes, interestingness, action, hook, and marketability — things an acquiring editor weighs.
**Change:** Ten criteria (C / PS / ST / CO / CR / IN / AC / HK / AL / MK), /50, with bands rescaled. The generator's summary schema emits one field per criterion, so a weak axis is a visible hole, not a hidden one. The black box and reviewer-spec both use the 10-criterion rubric.
**Status:** adopted (reviewer-spec.md expanded criteria; generator-spec.md 10-field schema).

## PI-18 [process] — The whole loop generalizes into a reusable BLACK BOX
**Finding (principal direction):** All the above — independent forks, self-escalating brutal critic, 10-criterion rubric, fresh-reviser-per-iteration, generator feedback, best=last — composes into one parameterized mechanism: (prompt, maxIterations) → generate → loop[harsh independent critic → fresh reviser] → full history.
**Change:** Built as a committed, re-runnable workflow at `blackbox/iterate-to-best.workflow.js`. Each fork is fresh (independence structural); the critic self-escalates per iteration; output is the history of every summary + critique with best assumed last. This is the portable distillation of the entire pitch-lab run.
**Status:** built + demonstrated.

## PI-19 [process] — Empirical: "best = last" is a useful default but NOT a guarantee — track the argmax
**Finding (black box demo run):** On the heist demo, the independent per-iteration critics scored the trajectory **i1 GOOD 32 → i2 GOOD 34 → i3 GOOD 34 → final 33**. The loop improved the summary (32→34), but the *last* revision slightly over-corrected, scoring 33 — below the iteration peak of 34. Because each critic is an independent blind fork, scores are not monotonic; a reviser handed a long fix-list can trade a gain on one axis for a loss on another.
**Change:** "Best = last" (the principal's spec) is the right *default* and the box honors it, but the box also runs a final independent score and returns the full per-iteration `trajectory` so the assumption is **auditable**. Recommended stricter variant (noted in `blackbox/README.md`): track the running argmax and return the highest-scored summary, not the last, when they differ. The demo is left as-is precisely because it shows the caveat is real, not hypothetical.
**Status:** demonstrated; argmax variant noted for future.

## PI-12 [content→ESCALATE candidate] — "Unavoidability" (structural trap vs. character choice) is the single sharpest discriminator at the top of the field
**Finding (Round 4):** The adversarial gauntlet's third attack — *can a smarter protagonist sidestep the tragedy by the premise's own rules?* — was the decisive killer. It eliminated THREE of seven finalists (P10 sisters, P19 life-vote-senate, P03 healing-wasps), all on the identical fault: the bad outcome depends on the protagonist *choosing* the self-destructive path when the premise does not structurally forbid the obvious alternative (Renne could negotiate via the notebook; Elia could abstain on procedural motions; Davan could stop curing and leave after cure 2). The three SURVIVORS (P01, P30, P32) all have the trap built into the premise's own laws — disease+guild+love (P01), her-nature-cannot-watch-hunger (P30), theology-forecloses-the-workaround (P32).
**Change:** The unavoidability test should be applied EARLIER (it's cheap and brutal) and should be a named axis sub-criterion under Substance, not only a Tier-4 attack. The cleanest line between a good tragedy and a great one is: *is the catastrophe forced by the rules, or chosen by a protagonist who had an out?* A great premise leaves the protagonist no out a smarter person would take.
**Status:** local-adopted. **ESCALATE candidate:** this maps directly onto the and-shoot substance contract — the cost ledger and antagonist pressure already exist, but "unavoidability / no-smarter-sidestep" is not an explicit gate at `/and-substance` or `/and-write`. Worth proposing as a substance-signature sub-check.

## PI-13 [process] — A single-axis rework can leave a DIFFERENT axis exposed at the next-harder tier; re-test the whole gauntlet, not just the fixed axis
**Finding (Round 4):** P03's rework correctly lifted A (4→5) and D (the two axes Round 3 named) and both fixes landed — but the Tier-4 gauntlet then killed P03 on **unavoidability (S)**, an axis the rework never touched and Round 3 had not flagged because Tier 3 doesn't run the unavoidability attack. The fix was real; it just wasn't the binding constraint at the harder tier. By contrast P32's rework happened to deepen S and D as a side-effect of the O-fix, so it survived.
**Change:** After a rework, re-run the FULL evaluation at the target tier, not just a re-check of the fixed axis. A rework changes the plan; the new hardest-tier binding constraint may be somewhere the rework didn't look. (Cross-pipeline parallel: this is why `/and-write revise` re-runs the whole bone-gate, not just the bones it touched — Rule 5.)
**Status:** adopted (Round 4 re-scored all 5 axes + all 4 attacks on the reworked plans).

---

## Escalations to the real proposals log

The following local findings cross the boundary into the core and-shoot pipeline and have been (or should be) surfaced to `staff/admin/process-proposals.md` per DEC-0121:
- **PI-08** — concreteness must be gated at multiple rising stances; the pitch-lab independently reproduced the "abstraction survives a single lenient gate" failure (P12) that DEC-0115's multi-surface enforcement exists to catch. *Confirmatory evidence for the existing design — filed as a note.*
- **PI-12** — "unavoidability / no-smarter-sidestep" as an explicit substance sub-gate. *Genuinely additive — the substance contract gates cost and pressure but not whether the tragedy is premise-forced vs. character-chosen.* This is the one worth a real PROP.
