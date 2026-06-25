# The iterate-to-best loop

A self-contained, re-runnable mechanism that takes **a prompt and a maximum number of iterations** and returns **the full history of every summary and every critique**, with the best assumed to be the last summary. It is the portable distillation of the entire pitch-lab run — every lesson is baked in.

## Interface

```
Workflow({
  scriptPath: "pitch-lab/iterate-to-best/iterate-to-best.workflow.js",
  args: { prompt: "<one-line story or series prompt>", mode: "story" | "series", maxIterations: <N> }
})
```

Output (returned object + persisted to `demo-run.md`):
```
{ prompt, mode, maxIterations, converged,
  trajectory: [{ i, band, total }, ...],     // band/score per iteration
  finalBand, finalTotal,                       // the last summary's score
  bestIsLast: true,
  persisted: "pitch-lab/iterate-to-best/demo-run.md"  // full history: every summary + critique
}
```

## Topology (exactly as specified)

```
prompt ─▶ [GENERATE fork] ─▶ summary v0
                               │
        ┌──────────────────────┘
        ▼   (loop up to maxIterations)
   [CRITIC fork]  ── independent, blind, self-escalating, brutal ──▶ structured feedback
        │                                                            (scores/band/weaknesses/fixes/generator-feedback)
        ▼
   [REVISER fork] ── NEW fork; receives old summary + that feedback ──▶ revised summary
        │
        └──▶ (becomes the next iteration's input)
        ▼   (after the loop)
   [FINAL CRITIC fork] ── scores the last summary so the history is complete
        ▼
   history of {summary, critique} × N  +  finalSummary (best = last)
```

Every fork is a **fresh subagent** — independence is structural, not promised. The critic **self-escalates**: iteration *i* is told to raise its bar above *i−1* and that any prior critic was too soft.

## The lessons it ships with

The critic grades on the **10-criterion brutal rubric** (`../reviewer-spec.md`): C·PS·ST·CO·CR·IN·AC·HK·AL·MK, /50, where 5 is near-unreachable and an unproven pitch is treated as a liability, not a triumph. It runs the attack battery (PITCH-NOT-STORY / FORMULA / SENTIMENTALITY / SUSTAINABILITY / GENERIC / UNAVOIDABILITY / ANTAGONIST-AS-FUNCTION).

The generator and reviser ship with **GEN-v2** (`../generator-spec.md`): reversal-not-escalation, antagonist-with-a-will, close-the-trap, reserve-a-discovery, answer-the-logline's-layer, name-the-sufferer, demonstrate-don't-imply-depth, and a 10-field summary schema mapped 1:1 to the criteria.

## Why "best = last" is sound here

Each iteration's reviser receives the harshest available critique and must address every named fault. Quality is therefore monotonic-by-construction (the reviser never sees a reason to regress), so the last summary has absorbed the most feedback. The final critic pass records the last summary's actual band so the claim is **checkable**, not asserted — see `demo-run.md` for the trajectory of a real run.

## Notes / honest limits

- **Best=last is an assumption, not a proof.** A reviser can over-correct. The final-critic score lets you verify; if the trajectory dips, take the highest-scored iteration instead. (A stricter variant would track the argmax and return that; this version honors the principal's "best = last" spec and exposes the trajectory so the assumption is auditable.)
- **Single-prompt scope.** The iterate-to-best loop improves one summary. The *field-level* faults (formula sameness, range deficit) need the non-blind **field-critic** (`../reviewer-spec.md`) across many prompts — that is deliberately outside this box.
- **Convergence.** If a critic ever returns BEST the box stops early (`converged: true`). At the brutal bar this is rare and that is the point.
