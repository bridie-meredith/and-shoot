# Generator spec — the thing that turns a prompt into a summary

The generator is a first-class object whose *improvement is a goal of the loop*, not a fixed black box. Reviewers feed it `GENERATOR INSIGHT`s; those become versioned rules here. A gauntlet improves nothing; this loop makes the **next** summary better by construction.

---

## GEN-v1 (the original 33-pitch expansion brief)

Produced concrete, substance-backed plans by hard-coding the project's discriminators (DEC-0115 concreteness, paid escalating cost ledger, escalating antagonist, a real road-to-hell turn). **It worked too well in one direction:** every one of the 33 plans was followable and substantial — but the brief *also* implicitly demanded the tragic-irony shape, so the entire field converged on it (see G8). GEN-v1's strength (it front-loads the discriminators) is real; its blindness (it equates "good pitch" with "tragic-irony mechanism") is the defect GEN-v2 fixes.

## GEN-v2 (rebuilt from the independent reviews' GENERATOR INSIGHTS)

Nine rules, each traceable to convergent reviewer findings. The first seven raise an individual summary; the last two fix the *field*.

| Rule | From | The change to the generator |
|------|------|------------------------------|
| **R1 — Reversal ≠ escalation** | G1 (4 forks) | A mandatory `PLOT STRUCTURE` field must contain at least one genuine REVERSAL — a beat where the story changes DIRECTION, not just intensifies. `[setup → escalate → collapse]` is banned; it scores D=2–3 forever. |
| **R2 — Stage the image in a beat** | G2 (3 forks) | The single best image is placed AT a named structural beat, not in a detached `HOOK` metadata field; distribute ≥1 concrete image across engine + structure, not one capstone. |
| **R3 — Antagonist is a will** | G3 (4 forks) | Name ≥1 human antagonist with competing goals who **loses something if the protagonist wins** and escalates against them. A mechanism / institution / weather / "the system" is not an antagonist. |
| **R4 — Close the trap** | G4 (2 forks) | One clause makes the worst outcome unavoidable by the world's own rules (no lazy sidestep) — OR the ending is genuinely open (the protagonist might win). No tragedy that a smarter protagonist trivially avoids. |
| **R5 — Reserve a discovery** | G5 (2 forks) | Do NOT reveal the self-payment / escape / twist mechanic in the engine block; reserve one rule the protagonist discovers under crisis, so the ending isn't deducible from the premise. |
| **R6 — Answer the logline's layer** | G6 | If the logline poses a metaphysical question ("what remains holy?"), the ending must physically enact an answer to *that* question, not resolve only the material plot. |
| **R7 — Name the sufferer, braid the tracks** | G7 (3 forks) | Each cost entry names who suffers + what valued thing is lost (never "the mechanism advances"), AND which antagonist force made it unavoidable at that moment. Cost-track and antagonist-track are authored together, not in isolation. |
| **R8 — Category coverage + sameness penalty** | G8 (field-critic) | Across a *field* of prompts, fill explicit tonal slots (tragic / comic / ambiguous / adventure / mystery), require a human antagonist in ≥⅓, require ≥1 prompt where the protagonist WINS and the win creates a forward problem, and PENALIZE structural convergence — do not reward 33 variations of one shape. |
| **R9 — Demonstrate, don't imply, depth** | G9 (L3 forks) | The pitch must SHOW a reversal and one beat of interiority; "the premise implies emotional depth" is not "the pitch demonstrates emotional depth." Unproven payoff is a liability. |

### The summary schema GEN-v2 emits (10 fields)

`LOGLINE · ENGINE (concrete) · PROTAGONIST ARC · ANTAGONIST (with a will) · STAKES · COST PAID · PLOT STRUCTURE (with a reversal) · HOOK IMAGE (staged in a beat) · RANGE/TONE · MARKETABILITY · NOVELTY` — the fields map 1:1 onto the 10 review criteria, so a weak field is a visible, gradeable hole rather than a hidden one.

This schema and these rules are the generator the black box (`blackbox/iterate-to-best.workflow.js`) ships with. The black box's reviser fork applies R1–R9 every iteration; its critic fork grades against the 10 criteria those rules target.

---

## How the generator improves over time

1. Each review emits a `GENERATOR INSIGHT` (a systemic pattern, not a one-off fix).
2. Insights that ≥2 independent forks name converge into a new GEN rule here, with the fork count as evidence.
3. The black box's generator/reviser prompts embed the current ruleset, so improvements compound automatically.
4. Field-level faults (range, sameness) come only from the **non-blind field-critic** — blind forks cannot see them — so the field-critic is a required part of any multi-prompt run.
