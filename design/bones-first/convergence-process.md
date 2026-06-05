# Convergence process — outline refinement loop (reusable)

**Purpose.** Converge a set of candidate full-story outlines into ONE critic-accepted
outline, via parallel generation + critique + cumulative-memory iteration. Saved here per
the principal's request ("save the process we follow for future reference"). Generalizes
beyond run-01.

**Core principle — fusion, not selection.** Every candidate's good ideas and every critique
are carried forward in a cumulative ledger. Later rounds cross-pollinate ALL prior material,
not just the round's "winner." Convergence is the critic fusing the best of everything into a
single outline that survives deconstruction.

---

## Roles
| Role | Count | Job | and-shoot production mapping |
|---|---|---|---|
| Orchestrator | 1 (main session) | Runs rounds; maintains the cumulative ledger; decides converge/iterate; enforces the cap. | command body |
| Generator | N=3 (parallel) | Each drafts one full-story outline under a distinct **lens**. | `screen-writer` |
| Critic | 1 | Deconstructs every outline (what works / what fails); synthesizes cross-candidate (keep / cut / fix); returns verdict + directives. | `dramatist` (+ `audience` for taste) |

**The three generator lenses (kept fixed across rounds for comparability):**
- **A — Comedy/voice:** funniest, most propulsive; the locked-POV gag and the bits.
- **B — Drama/theme:** the tragic spine, the grief-armor arc, the relationship cost-ledger.
- **C — Structure/mechanics:** the plot machine — causal spine, setups/payoffs, the acquisition
  ladder, the three-rhymes escalation, canon-timeline integration, heist logic.

---

## Artifacts
- `<workspace>/convergence/round-NN/gen-{A,B,C}.md` — the round's three outlines.
- `<workspace>/convergence/round-NN/critique.md` — the critic's deconstruction + verdict.
- `<workspace>/convergence/convergence-ledger.md` — the **cumulative carry-forward** (grows each
  round): the seed, every outline digested, every critique, and the running KEEP / CUT / FIX set
  and standing convergence criteria. This is the file every generator and the critic re-reads.

---

## Round protocol
1. **Generate (parallel).** Dispatch the 3 generators. Each reads: the seed (bible docs) + the
   FULL cumulative ledger, and writes its outline under its fixed lens to `gen-X.md`. A generator
   MUST honor the ledger's KEEP set, repair the FIX set, and explore freely only where the critic
   flagged thinness.
2. **Critique.** Dispatch the critic. It reads all 3 new outlines + the ledger, and writes
   `critique.md`: per-outline what-works / what-fails; a cross-candidate synthesis (best elements
   to KEEP, weakest to CUT, recurring failures to FIX); and a verdict.
3. **Ledger update.** Orchestrator appends the round's digest + critique + updated KEEP/CUT/FIX to
   the ledger.
4. **Branch.** `CONVERGED` → stop; promote the accepted outline. `ITERATE` and round < cap → go to
   step 1. Cap reached without convergence → report the best candidate + residual BLOCKERs.

## Convergence criteria (the critic's CONVERGED test)
The accepted outline must satisfy ALL, with zero unresolved BLOCKER notes:
- **Structure** — a clear causal spine; setups pay off; no orphaned threads.
- **Drama** — real stakes; a legible cost ledger; the tonal curdle is *earned*, not announced.
- **Comedy** — the engine sustains across the length (not just the cold open).
- **Theme** — the meta-question lands (here: "will the immortal ever come down and be mortal?").
- **Canon-fit** — clean against the hard fences.
- **The rhymes hold** — for run-01: one-method-three-locks; gain-then-lose; reagent/geo/tone ladder.

## Cap
**4 rounds.** If unconverged at cap, the orchestrator promotes the strongest candidate and reports
residual BLOCKERs for a human call rather than looping indefinitely.

## Notes / lessons (append as we learn)
- **The loop narrows: diverge → fuse → stress-test.** Round 1 runs N divergent lensed generators;
  once the critic produces a converged *skeleton*, Round 2+ is a single **fusion pass** (one
  continuous draft implementing the skeleton + rulings), not another divergent round. Carrying ALL
  candidates' material forward is precisely what makes the fusion possible.
- **The critic should double as skeleton-author.** Having the critic emit the converged skeleton in
  its synthesis turns "what's wrong" into "here's the thing to build" — the single highest-value
  artifact of the round. (run-01 R1: critique.md §3.)
- **Lensed generation is reliably convergent when the seed is rich.** With a strong shared ledger,
  three independent lenses agreed on major decisions (run-01: Yi-Ti single-reach, the KEEP set), so
  most Round-1 disagreement was about *emphasis*, which fuses cleanly.
- **Ratify smuggled premises explicitly.** Generators will quietly introduce load-bearing premises
  (run-01: prior-death-as-wound). The critic must surface these as ratification gates so a premise
  isn't frozen by accident; the orchestrator (or principal) rules before the next round.
- **Post-convergence principal enrichment → a bounded integration round, not a re-open.** When the
  principal adds material AFTER CONVERGED (run-01 R3: the Cauldron-Belly + poison-path), don't throw
  away the convergence. Ratify the addition, write explicit GUARDS (what the addition must not break),
  run one integration pass that folds it into the accepted outline, and a single critic re-validation
  scoped to "do the six criteria still hold + are the guards honored" — not a fresh divergent round.
- **Convergence was fast (2 rounds) because the seed was a fully-developed bible.** The richer the
  Round-0 seed (bible docs + KEEP/FIX ledger), the fewer rounds to converge.
