# pitch-lab — RESULTS

A 33-pitch fantasy–sci-fi tournament run end-to-end through the pitch-lab runbook: **prompt → plan → summarize → evaluate at rising difficulty → rework the near-best → converge on 3.** The runbook (`RUNBOOK.md`) is the deliverable; this field is its proof.

---

## The best 3

| Rank | Plan | Score | Engine in one line |
|------|------|-------|--------------------|
| **#1** | **P01 bonewright-sister** | 24/25 · SURVIVES-ALL | A bonewright keeps her dying sister walking by grafting living bone grown from her own marrow — but the grafts carry her signature, so the saved sister becomes *her*. The cost of the gift is the recipient's selfhood, paid incrementally, from love. |
| **#2** | **P30 famine-saint** | 24/25 · SURVIVES-ALL | A saint multiplies bread by absorbing others' hunger into her own body; at city scale the hunger stops dissipating and starts *growing*, eating her from inside. Not martyrdom — parasitism. |
| **#3** | **P32 weather-priest-invoice (REWORKED)** | 24/25 · SURVIVES-ALL | A weather-priest finds his own ordination oath printed verbatim in his guild's founding charter: his faith was commercial property before he ever held it. The sacred *was* commercial, at origin. |

Full packages (ranking + summary + adversarial result + why-it-won + full plan) in `best-3/`.

**The headline:** **#3 is a reworked plan.** P32 entered Round 3 *below the cut line* (21/25, held back by one capped axis — Originality). It was carried into the iterate-to-best loop, given one surgical fix, and climbed to 24/25 in the final three. That single trajectory is the runbook's whole thesis: *rework the near-best until it passes as the bestest.*

---

## Convergence trace (33 → 3)

```
33 plans
  │  Round 1  Tier 1 OPEN (generous)      gate: ≥16, no axis 0
  ▼  → ALL 33 PROMOTE  (strong field; the generous tier did no cutting — PI-05)
33
  │  Round 2  Tier 2 STANDARD (skeptical + anti-inflation anchors)   cut line: ≥20
  ▼  → 15 PROMOTE  / 6 rework-not-carried / 6 below-line / 6 structural-elim
15
  │  Round 3  Tier 3 HARD (skeptical; C≥4 & S≥4; O-cap for nameable engines)   gate: ≥22
  ▼  → 5 PROMOTE  + 2 of 6 reworks carried into a lift attempt
5 + 2 reworked (P03, P32)
  │  Round 4  Tier 4 BESTEST (adversarial gauntlet: generic / naive-follow / unavoidability / one-image)
  ▼  → 3 SURVIVE-ALL
BEST 3:  P01, P30, P32(reworked)
```

### What each round actually did

- **Round 1 (Tier 1, generous):** promoted all 33. Not a failure — the field was uniformly strong (the *expansion brief* hard-coded the discriminators, so weak plans never entered — PI-06). Lesson: when the field over-performs the opening tier, escalate by *stance + anti-inflation anchors*, not threshold alone (**PI-05**).
- **Round 2 (Tier 2, skeptical):** the anti-inflation re-score compressed the bunched 16–24 band into a separable 13–23 spread. 18 eliminations across three honest classes (structural fault / near-miss-with-fix / cleared-but-below-line). Caught P12's abstract engine that the summarizer had passed — concreteness must be re-judged at a harder stance (**PI-08**).
- **Round 3 (Tier 3, hard):** all four eliminations died on the *same* disqualifier — **Originality capped because the engine was a nameable archetype**. In a concreteness-and-substance-disciplined field, originality is the axis that actually selects (**PI-09**).
- **Round 4 (Tier 4, adversarial):** the **unavoidability attack** was the decisive killer — it eliminated 3 of 7 finalists (P10, P19, P03), all on the identical fault: tragedy resting on a character *choice* the premise didn't structurally foreclose. The survivors all have premise-*forced* traps (**PI-12** → escalated as PROP-0059).

---

## The iterate-to-best loop, demonstrated

Two near-best plans were reworked under the loop (rework budget reserved for plans that could change the *winner* — **PI-07**):

| Plan | Pre-rework | Fix (surgical, single-axis, concrete) | Post-rework | Outcome |
|------|-----------|----------------------------------------|-------------|---------|
| **P32** weather-priest | 21/25 (O=3, nameable) | Reveal the ordination oath *is* Article 1 of the guild charter — faith was property before vocation | **24/25** | **→ BEST-3 #3** |
| **P03** healing-wasps | 20/25 (A,D soft) | Concrete memory-gap beat + visible causal-loop event | 21/25 | FELL at Tier 4 on unavoidability (S) — an axis the rework didn't touch (**PI-13**) |

Both reworks *landed on the first pass* because each instruction named the exact axis AND the exact concrete change (**PI-11**). P32 is the success case; P03 is the instructive near-miss that produced PI-13 (re-test the whole gauntlet after a rework — the new binding constraint may be elsewhere).

---

## What the tournament taught (process improvements)

Full log in `process-improvements.md` (PI-01 … PI-13). The load-bearing ones:

1. **Split summarizer from evaluator** (PI-01) — faithful compression + honest flags vs. judgment; never the same agent.
2. **Front-load discriminators into the generator, not just the judge** (PI-06) — the cheapest quality lever in the pipeline; it's why the field was strong enough that selection moved to the hard tiers.
3. **Escalate the critic's *stance*, not just the numeric bar** (PI-04, PI-05) — generous → neutral → skeptical → adversarial; re-score from scratch each tier.
4. **The gate is three-way and logged** (PI-03) — promote / rework / eliminate, always with a reason; no plan kept or dropped on vibes.
5. **Reserve rework budget for the winner-deciding plans** (PI-07); **a rework instruction must be axis-specific and concrete** (PI-11); **re-test the full gauntlet after a rework** (PI-13).
6. **Originality is the top-of-field discriminator once concreteness is disciplined** (PI-09); **unavoidability (premise-forced vs. character-chosen) is the sharpest single test** (PI-12).

Two findings crossed into the core and-shoot pipeline (per DEC-0121): **PI-08** (multi-stage concreteness gating — confirmatory of DEC-0115, filed as a note) and **PI-12** (an explicit unavoidability sub-gate for the substance contract — filed as **PROP-0059** for principal triage).

---

## Run accounting

- **Field:** 33 single-sentence prompts (`00-pitches.md`), seeded across all 8 premise lenses.
- **Dispatches:** ~21 agent dispatches total — 1 admin (scope), 6 screen-writer (expansion), 3 summarizer, 6 evaluator (rounds 1-2), 1 evaluator (round 3), 2 screen-writer (rework), 1 summarizer (re-summarize), 1 evaluator (round 4 gauntlet). Batched per DEC-0121 rather than per-item-per-round (which would have been hundreds).
- **Artifacts:** 33 plans + 2 reworks (`plans/`), 35 summaries (`eval/summaries-*`), 4 round reports + scorecards (`eval/round-*`), 3 winner packages (`best-3/`), the runbook + 2 specs, the process log, this file.
- **Escalations:** PROP-0059 (unavoidability sub-gate) filed to `staff/admin/process-proposals.md`.

The runbook ran clean end-to-end and converged on exactly the target of 3 with no human intervention; all flow-control was ratified once via admin user-proxy (DEC-0121).
