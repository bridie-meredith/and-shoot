# pitch-lab — RESULTS

A run that started as a 33-pitch tournament and, under the principal's corrections, became something more useful: a **discerning critic + feedback loop**, and finally a reusable **black box**. This file records the honest end state, including where the early framing was wrong.

---

## What was built (the deliverables)

| Artifact | What it is |
|---|---|
| `RUNBOOK.md` | the repeatable prompt → plan → rework-until-best process |
| `reviewer-spec.md` | **the discerning critic** — independent blind forks, self-escalating bar, 10-criterion brutal scale, the field-critic role |
| `generator-spec.md` | the generator as a first-class object that *improves* (GEN-v1 → GEN-v2, nine rules from reviewer insight) |
| `summarizer-spec.md` | the fixed-schema, honest-flagging summarizer |
| `00-pitches.md` + `plans/` | 33 single-sentence fantasy–sci-fi pitches expanded into substance-backed plans |
| `eval/round-1..3.md` | the field-narrowing rounds (33 → 15 → 5+2) |
| `eval/discernment/` | the independent blind-fork reviews + the non-blind field-critic + the corrected verdict |
| **`blackbox/iterate-to-best.workflow.js`** | **the black box** — (prompt, maxIterations) → generate → loop[harsh independent critic → fresh reviser] → full history; best = last |
| `blackbox/demo-run.md` | a real run of the black box, with its full per-iteration history |
| `process-improvements.md` | 19 harvested improvements (PI-01..19), spanning the whole arc |

---

## The corrected verdict (this supersedes the early "best-3")

The first pass produced a `best-3/` of P01, P30, P32 at **24/25** via a Tier-4 "gauntlet." **That framing was wrong and is retired.** A gauntlet asks "which summary survived furthest"; it inflates (everything that survives looks near-perfect) and it teaches nothing. Under the principal's corrections — *be more critical, use independent forks, escalate the bar, discern don't filter, and feed insight back* — the honest picture is:

**Under independent, blind, self-escalating brutal forks:**

| Summary | gauntlet | **honest (blind)** | **brutal (L3)** |
|---|---|---|---|
| SX1 / SX2 (deliberately-awful straws) | — | **3–4/25 AWFUL** | — |
| P29 cartomancer (weak) | eliminated | **17 MEDIOCRE** | — |
| P09 year-debt (competent) | eliminated | **19 GOOD** | — |
| P01 bonewright | **24** | **19 GOOD** | **12 BAD** |
| P30 famine-saint | **24** | **18 GOOD** | **12 BAD** |
| P32 weather-priest | **24** | **19 GOOD** | **13 BAD** |

The reviewer now **discerns** (sorts awful→best with spread scores; refuses to award BEST), and at the brutal bar it exposes every "winner" as **clever, concrete, formulaic, and unproven** (BAD).

**The field-critic (non-blind) found the deeper truth blind forks structurally cannot see:** the entire field is *one shape* — "a mechanism whose operation IS the harm," tragic-irony, paid on the body. Severe range deficit — no comedy, no hope, no winnable plot, no human antagonist. Its ranking: **P09 > P32 > P01 > P30**, with the verdict that *none is "best" in absolute terms — P09 is "best of a samey field, a designation that is accurate and indicting simultaneously."*

So the honest top-3 is **P09, P32, P01** — stated with the field-critic's caveat: they are the least-cramped corners of a field the generator (and the original 33-prompt brief) over-narrowed to one tragic register. The real fix is upstream: GEN-v2 R8 (category coverage + structural-sameness penalty).

---

## The black box (the portable result)

`blackbox/iterate-to-best.workflow.js` distills the whole run into one re-runnable mechanism. Demonstrated on a fresh, deliberately off-formula prompt (a heist with a human antagonist and a winnable ending):

```
Trajectory:  i1 GOOD 32/50  →  i2 GOOD 34/50  →  i3 GOOD 34/50  →  final GOOD 33/50
```

What this single run shows:
- The loop **works** (generate → independent harsh critic → fresh reviser, 9 forks) and **improves** (32 → 34).
- The off-formula prompt scored *higher* than the tragic-irony field under the same bar — direct evidence for the range critique.
- **"Best = last" is a default, not a law:** the final revision over-corrected to 33, below the iteration peak of 34. The box returns the full trajectory so this is auditable (PI-19); an argmax variant is noted for anyone who wants the strict guarantee.

---

## The one-line answer to "the runbook is my actual goal"

Take a prompt → generate a substance-backed summary → hand it to an **independent, blind, self-escalating** critic that grades on ten criteria with a near-unreachable ceiling and treats an unproven pitch as a liability → hand the critique to a **fresh** reviser → repeat, ratcheting the bar each pass → keep the full history, and *verify* rather than assume which summary is best. Run it across a field and add a **non-blind field-critic** to catch the sameness no single review can see. That loop — not a bracket of survivors — is what turns a one-line prompt into the best version of its story, and it is now a button: `blackbox/iterate-to-best.workflow.js`.
