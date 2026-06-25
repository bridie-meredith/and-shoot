# Summarizer spec

The summarizer compresses a fleshed story plan into a fixed-schema artifact that the evaluator scores. It exists so the evaluator judges a **standardized surface**, not each plan's idiosyncratic length and emphasis — a long plan can't win by sheer word-count, and a thin plan can't hide behind handwaving.

The summary is also a stress-test in its own right: a plan whose engine cannot be stated concretely in the `engine` field is already failing axis C, before the evaluator scores anything.

## Schema

Every summary is exactly these fields, in order. No prose outside the fields.

```
PLAN: P##  <slug>
LENS: <premise lens>
---
LOGLINE: <one sentence — may be the original prompt or a sharpened version>

ENGINE: <2-3 sentences. The concrete, physical mechanism that drives the story.
  State what literally, physically happens — actions a naive reader could picture.
  If you can only describe it abstractly, that IS the finding: write the abstraction
  AND flag it "[ABSTRACT-ENGINE]".>

PROTAGONIST ARC: <start-state → end-state across the relevant axes:
  capability / social tether / moral framework / legibility / position.
  Name the two or three axes that actually move.>

COST LEDGER: <what the protagonist pays, and how it escalates. Each major gain must
  have a named, on-page price. If the price is vague or deferred forever, flag
  "[UNPAID]".>

ANTAGONIST PRESSURE: <the opposing force — self / person / society / environment —
  and how it escalates round over round. Static opposition flags "[FLAT-PRESSURE]".>

ROAD-TO-HELL TURN: <the single reversal where the protagonist's pursuit of the good
  thing becomes the cause of the bad thing. One sentence. If there is no turn — if
  the protagonist just succeeds or just fails — flag "[NO-TURN]".>

SHAPE: <the dramatic curve in 4-6 beats: setup → escalation → midpoint reversal →
  cost spike → climax → aftermath. Keep each beat to a clause.>

HOOK / ALIVENESS: <one concrete sensory or emotional image the story would live on —
  the thing a reader remembers. Not a theme statement; an image.>

NOVELTY CLAIM: <the one mechanism here that you have not seen done this exact way.
  Be honest: if it's a recombination of known parts, name the parts.>
```

## Summarizer rules

1. **Concreteness is the summarizer's first duty.** The `ENGINE` field must render physical action. If the plan only supports an abstract engine, the summarizer does not paper over it — it writes the abstraction and tags `[ABSTRACT-ENGINE]`. The evaluator weights that tag heavily on axis C.
2. **No inflation.** The summarizer may sharpen a logline but may not invent substance the plan doesn't contain. If a field is unsupported by the plan, it gets the appropriate flag (`[UNPAID]`, `[FLAT-PRESSURE]`, `[NO-TURN]`), not a confabulated answer.
3. **The flags are the point.** `[ABSTRACT-ENGINE]`, `[UNPAID]`, `[FLAT-PRESSURE]`, `[NO-TURN]` are honest signals to the evaluator. A summarizer that hides a plan's weaknesses defeats the tournament. Summarize faithfully, flag freely.
4. **Fixed length.** Target 180–260 words across all fields. A summary that needs more than 260 words to convey the plan is itself evidence the plan is muddy (flag the summary `[OVER-LENGTH]`).
