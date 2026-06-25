# Reviewer spec — the discerning critic (NOT a gauntlet)

This replaces the gauntlet framing. The reviewer's job is **not** to let strong summaries survive attacks. It is to **discern** — to place a summary honestly on the quality spectrum — and to **teach**: to hand the generator concrete insight that improves both this summary and the next one it produces.

A gauntlet answers "which summary made it furthest?" That is the wrong question; the furthest-surviving summary can still be mediocre, and the gauntlet never improves anything. The discerning critic answers two right questions: **"how good is this, really?"** and **"what specifically would make it — and the generator — better?"**

---

## Three binding properties

### 1. Independent fork, blind to the field
Each review is its own fork. A reviewer sees **exactly one** summary and **nothing else** — not the other summaries, not other reviewers' scores, not the plan's tournament history. This kills two diseases of batch review: **curving** (scoring relative to the batch instead of against an absolute bar) and **anchoring** (the first few scores set the scale for the rest). An independent fork has no batch to curve against; it must judge against the standard alone.

### 2. Self-escalating antagonism
The fork does not apply a fixed bar — it **raises its own bar as it reads**. Operating instruction: *assume the summary is overrated until it proves otherwise; every time you are tempted to award a 4 or 5, stop, raise the standard, and re-ask whether it truly clears the higher bar.* Each iteration of the loop refreshes the antagonism upward — a summary that satisfied last pass's reviewer must satisfy a harsher one this pass. The bar ratchets; it never relaxes.

### 3. The brutal, true-spectrum scale
The scale must span real quality, so that awful, bad, mediocre, good, and best land in visibly different places. Inflation collapses the spectrum (everything clusters at the top) and destroys discernment.

| Axis score | Meaning |
|---|---|
| **5** | Definitive. Could not be improved by a top editor. Award **at most once across a whole field**, with written justification. Default assumption: not a 5. |
| **4** | Excellent, but a better version is still nameable. |
| **3** | Competent / professional. **The default for a strong plan.** |
| **2** | Functional but flawed; a weakness a reader notices. |
| **1** | Deficient. |
| **0** | Absent / broken. |

Five axes (unchanged): **C** concreteness/followability · **D** dramatic shape · **S** substance (paid escalating cost + escalating antagonist + unavoidable-by-the-rules) · **O** originality (of *mechanism*) · **A** aliveness. 25 max.

### The spectrum bands (the discernment output)
The reviewer places the summary in a band — this is the primary verdict, more important than the exact number:

| Band | Total | What it means |
|---|---|---|
| **BEST** | 22–25 | genuinely exceptional; rare |
| **GOOD** | 18–21 | strong, shippable, with real strengths |
| **MEDIOCRE** | 14–17 | competent but undistinguished; a flaw or two a reader feels |
| **BAD** | 9–13 | structurally broken on one or more axes |
| **AWFUL** | 0–8 | generic, abstract, or stakes-free; not a story |

A correctly-calibrated reviewer, shown a deliberate spread, sorts it across these bands. A reviewer that puts everything in GOOD/BEST is broken, regardless of how strong the field is.

---

## Mandatory output (every review)

A review that names no weakness is an **evaluation failure**, not a perfect summary. Every review must produce:

```
REVIEW — <summary id>   (independent fork; self-escalated bar)
SCORES:  C:<n> D:<n> S:<n> O:<n> A:<n>   TOTAL:<n>/25
BAND:    AWFUL | BAD | MEDIOCRE | GOOD | BEST
WEAKNESSES (≥3, concrete and specific — a named beat, cliché, or structural fault, never a hedge):
  1. ...
  2. ...
  3. ...
SUMMARY INSIGHTS (2-3 actionable fixes that would raise THIS summary's band — name the axis and the exact change):
  - ...
GENERATOR INSIGHT (1-2 systemic patterns this summary reveals about the GENERATOR — what the prompt/process that produced it should change, generalizable beyond this one plan):
  - ...
ONE-LINE VERDICT: <the single most decisive judgment>
```

The **GENERATOR INSIGHT is the load-bearing output** — it is how the review improves the *next* summary, not just this one. A reviewer that only fixes the instance and never teaches the generator is doing half its job.

---

## Expanded criteria (v2 — 10 axes, /50) + the escalation ladder

The 5-axis set (C/D/S/O/A) is too narrow to judge a pitch the way a professional acquiring editor would. The authoritative rubric is now **ten** criteria, 0–5 each (50 max). The brutal scale, independence, and self-escalation all carry over unchanged; only the criteria broaden.

| # | Axis | Judges |
|---|------|--------|
| **C** | Concreteness / Followability | naive reader can reconstruct physical action; no abstraction/bookkeeping engine (DEC-0115). *Load-bearing.* |
| **PS** | Plot Structure | genuine reversal(s), not one-note escalation; a real second gear; sustainable across novel length; resolution earned by the shape. |
| **ST** | Stakes | what is actually at risk, magnitude, personal **and** external; do stakes escalate; is the worst outcome unavoidable by the world's own rules (the trap). |
| **CO** | Cost / Substance | what is actually **paid on-page** + an antagonist with a competing **will** (not a mechanism/weather/legal-system). Distinct from Stakes: stakes = risk, cost = payment. |
| **CR** | Creativity / Originality | novelty of **mechanism AND shape AND world AND voice**. The "clever-mechanism-as-its-own-tragic-cost, road-to-hell" template is itself a cliché — a novel mechanism in that shape is still capped. |
| **IN** | Interestingness | would a reader keep turning pages — intrigue, curiosity, the freshness of the *reading experience*, not just the concept's cleverness. |
| **AC** | Action / Momentum | forward motion; protagonist **drives** events rather than only absorbing them; things happen. Passive/iterative-collapse premises score low. |
| **HK** | Hook | the grab — a logline + opening image/question that pulls immediately and is repeatable to another person in one breath. |
| **AL** | Aliveness / Voice | an earned, specific, **non-sentimental** image; pulse and implied voice; not stock pathos (dying sibling, starving city, dead child). |
| **MK** | Marketability | commercial viability: a nameable audience, genre fit, plausible comp titles, breakout potential; would an editor pitch this to a sales team. |

### Bands (/50)

| Band | Total /50 |
|---|---|
| **BEST** | 40–50 |
| **GOOD** | 32–39 |
| **MEDIOCRE** | 24–31 |
| **BAD** | 14–23 |
| **AWFUL** | 0–13 |

### The escalation ladder (the bar refreshes higher each pass)

The principal's standing instruction is "still not critical enough." The reviewer answers it structurally: each review pass **ratchets the bar above the previous pass**.

- **L1 (generous)** — credit what works. (Retired; it scored everything GOOD/BEST — useless as a filter.)
- **L2 (skeptical)** — neutral scoring, anti-inflation anchors.
- **L3 (brutal — current default)** — *this is a PITCH, not a story.* The hard part (interiority, earned emotion, sustaining a novel, working prose) is **unproven**; credit only what the summary demonstrates and treat unproven payoff as a **liability**. Run the attack battery (PITCH-NOT-STORY / FORMULA / SENTIMENTALITY / SUSTAINABILITY / GENERIC / UNAVOIDABILITY). A strong-but-unproven pitch lands **BAD–MEDIOCRE**; GOOD requires defeating every attack; BEST is near-impossible for a pitch.
- Each further pass refreshes the antagonism above the last and is told the prior score "was too soft."

### The field-critic (a second, non-blind role)

Blind forks have a structural blind spot: each sees one plan, so none can see that **the whole field is one shape repeated**. That sameness is a real, damning criticism. So the reviewer set includes one **non-blind field-critic** that reads the strong plans together and judges the *field* — shared formula, range deficit, sentimentality audit, and what a genuinely best-in-class pitch would do that none of them do. Independence (blind forks) and field-awareness (field-critic) are complementary; run both.

---

## How the loop uses reviews (the runbook proper)

1. **GENERATE** — generator turns a pitch into plan + summary (`generator-spec.md`).
2. **DISCERN** — N independent forks review each summary; aggregate the bands + scores into an honest quality map of the field (awful→best). This is *discrimination*, not elimination.
3. **IMPROVE THE SUMMARY** — apply each summary's SUMMARY INSIGHTS → rework → re-discern with a *refreshed-higher* bar. A summary climbs bands or it doesn't; the reviewer says which.
4. **IMPROVE THE GENERATOR** — aggregate GENERATOR INSIGHTS across the field into concrete changes to the generator brief (`generator-spec.md` changelog). The next generation is better *by construction*, not by luck. This is the half a gauntlet never does.
5. **CONVERGE** — iterate until the field's genuinely-best ~3 stand clear under the harshest independent review, AND the generator has documented, applied improvements.

"Best" here means *highest honest band under the harshest independent fork*, not *last one standing*. The two can differ — and when they do, this spec trusts discernment over survival.
