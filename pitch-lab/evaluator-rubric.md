# Evaluator rubric — 5 axes × 4 escalating tiers

The evaluator scores a plan **summary** (never the raw plan — it judges the standardized surface) on five axes, 0–5 each, 25 max. The gate at each tier combines a **total floor**, **per-axis floors**, and **tier-specific disqualifiers**, plus — from Tier 3 up — an **adversarial stance** that shifts the critic's job from "credit what works" to "find the reason to reject."

This is the difficulty dial the principal asked to crank.

---

## The five axes (0–5 anchors)

### C — Concreteness / Followability  *(the load-bearing axis — DEC-0115 / Rule 22)*
- **5** — A naive reader with zero context could narrate what physically happens in every beat. The engine is concrete human/physical action.
- **3** — Mostly followable; one or two beats lean on abstraction or jargon a reader must take on faith.
- **1** — The engine is an abstraction, a system, or a bookkeeping process ("the count closes," "the gap propagates"); a naive reader cannot reconstruct the scene.
- **0** — Incoherent or `[ABSTRACT-ENGINE]`-flagged with no concrete fallback.

### D — Dramatic shape
- **5** — Clean escalation with a real midpoint reversal and a cost spike; the curve rises and turns. The ending is earned by the shape, not appended.
- **3** — A discernible arc, but escalation is mild or the reversal is soft.
- **1** — Static premise; the situation is interesting but does not *develop*. Or `[NO-TURN]`.
- **0** — No shape; a setting or a vibe, not a story.

### S — Substance  *(cost ledger + antagonist pressure)*
- **5** — Every major gain has a named, escalating, on-page price; antagonist pressure escalates mechanically; the tragedy is *built into the premise's own rules* and could not be avoided by a smarter protagonist.
- **3** — Costs and pressure are present but partly bolted-on or under-escalated.
- **1** — Costs are vague or deferred forever (`[UNPAID]`); pressure is flat (`[FLAT-PRESSURE]`).
- **0** — No cost, no real opposition; wish-fulfilment.

### O — Originality
- **5** — The central *mechanism* is genuinely fresh — not just a new skin on a familiar engine. You cannot name the two stories it's recombining.
- **3** — A fresh combination of known parts, executed with a real new wrinkle.
- **1** — Recognizable trope in new paint; the novelty is cosmetic.
- **0** — Derivative; you've read this exact engine before.

### A — Aliveness
- **5** — A specific, sensory, unforgettable image at the core; the plan has a pulse and an implied voice.
- **3** — Some vivid moments; mostly competent but cool.
- **1** — Airless; theme statements where images should be.
- **0** — Inert.

---

## The four tiers (the rising bar)

### Tier 1 — OPEN  *(Round 1; expect most plans to clear)*
- **Total floor:** ≥ 16 / 25
- **Per-axis floor:** no axis at 0
- **Disqualifiers:** none beyond the floors
- **Critic stance:** *generous* — credit what works; give the benefit of the doubt on near-misses. Goal: eliminate only the genuinely broken (~⅓ cut).

### Tier 2 — STANDARD  *(Round 2)*
- **Total floor:** ≥ 19 / 25
- **Per-axis floor:** no axis below 2; **C ≥ 3**
- **Disqualifiers:** any unresolved `[ABSTRACT-ENGINE]` or `[NO-TURN]` flag
- **Critic stance:** *neutral* — score honestly, no benefit of the doubt. NEAR-MISS plans (1–2 axes short, no disqualifier) get one REWORK before the cut. (~½ of survivors cut.)

### Tier 3 — HARD  *(Round 3; rework is now the main activity)*
- **Total floor:** ≥ 22 / 25
- **Per-axis floor:** no axis below 3; **C ≥ 4** and **S ≥ 4**
- **Disqualifiers:**
  - Any abstraction in the engine (C hard gate — DEC-0115).
  - Any `[UNPAID]` or `[FLAT-PRESSURE]` flag (substance hard gate).
  - "Competent but I've seen the mechanism" → O capped at 3 → fails the floor.
- **Critic stance:** *skeptical* — the default is rejection; the plan must earn each axis. Close plans (within 2 points, fixable flaw) are LIFTED via rework, not dropped — this is where "rework until best" does its real work. (Cut toward target.)

### Tier 4 — BESTEST  *(Round 4; only ~3 survive)*
- **Total floor:** ≥ 24 / 25
- **Per-axis floor:** every axis ≥ 4, with **at least three axes = 5**, and **C = 5**
- **Disqualifiers (adversarial pass — all must be survived):**
  1. **Generic-attack:** the critic writes the strongest one-paragraph case that this plan is actually generic/derivative. If the case lands, the plan fails O.
  2. **Naive-follow:** a reader with zero context must be able to write one plain-English paragraph of "what physically happens." If they can't, the plan fails C (DEC-0115 naive-follow sub-gate).
  3. **Unavoidability:** the tragedy must be unavoidable *by the premise's own rules* — if a smarter protagonist could simply sidestep it, the plan fails S.
  4. **One-image test:** name the single image the story lives on. If there isn't one, the plan fails A.
- **Critic stance:** *adversarial* — the critic's job is to reject every plan and pass only those that defeat all four attacks. A plan passes Tier 4 only if it survives a sincere attempt to kill it.

---

## Scorecard format (per plan, per round)

```
P## <slug> — Round N (Tier <name>)
  C:<0-5> D:<0-5> S:<0-5> O:<0-5> A:<0-5>  TOTAL:<n>/25
  Flags: <any summary flags carried + tier disqualifiers hit>
  Tier-4 attacks (if Round 4): generic:<survived|FELL> naive:<...> unavoid:<...> image:<...>
  GATE: PROMOTE | REWORK(<axis(es) to lift, specific instruction>) | ELIMINATE(<reason>)
  One-line rationale: <why this score — the single most decisive observation>
```

## Honesty discipline (inherited from the orchestrator-critic card)

- **Score arithmetic is authoritative; narrative is not.** A plan does not pass because it "feels strong"; it passes because the axes clear the floor.
- **A REWORK instruction must be specific and actionable** — name the axis, name the flaw, name the change. "Make it better" is not a rework instruction.
- **ELIMINATE always carries a reason** — a fatal flaw or a sub-floor score. No plan is dropped on vibes (T2).
- **The bar only goes up.** A plan that cleared Tier 2 is not re-litigated at Tier 2; it is judged at Tier 3's harder bar. Promotion is monotonic; the field only shrinks.
