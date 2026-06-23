> **⚠ SUPERSEDED — provenance only; do not build from this layer.** run-02 is an early revision framework; its
> chapter structure was carried forward and reshaped through run-03 → **run-04 (canonical)**. Build target:
> `intake/spine.md` + `design/run-04/series-outline.md` (check-threads PASS).

# run-02 — plot-revision framework

**What run-02 is.** The working layer for *revising the converged story* one chapter-note at a
time, while keeping character-state, world-state, and the causal threads consistent. run-01 =
the bible + the convergence to a single outline; **run-02 = controlled mutation of that outline**
under the principal's two-desires re-axis (`design/restructured-books-two-desires.md`).

Built to **reuse existing machinery** and add only what was genuinely missing.

## The loop (one chapter note → consistent revision)

A chapter note is treated as a **post-convergence principal enrichment** per
`design/convergence-process.md` (the same pattern that folded in the Cauldron-Belly in run-01):

```
note (messy, ok) → INTAKE/triage → ratify + GUARDS → slot into ledger → recompute downstream
   → thread audit (mechanical + judgment) → flag breaks + opportunities → re-thread → re-check
```

Notes are allowed to be messy and non-cohesive — coherence is the framework's job, not the input's.

## Assets

| Asset | What it is | New / existing |
|---|---|---|
| `book-i-state-ledger.md` | per-chapter character/world state vectors + blast-radius + the change-propagation protocol | **new** (chapter-granularity layer nothing else holds) |
| `idea-inbox.md` | the front door: raw note dumps land here, get triaged, marked processed | **new** (thin) |
| `thread-config.txt` | story-specific aliases + accepted plant-only/payoff-only exceptions | **new** (data for the checker) |
| `../../../scripts/check-threads.py` | mechanical thread-integrity checker (orphans / gift→spend order / curdle rungs) | **new tool** — mechanizes a convergence criterion |
| `design/convergence-process.md` | the revision loop + six criteria + enrichment-round pattern | **existing** — the governing process |
| `convergence/convergence-ledger.md` | cumulative record; enrichment-round digests append here | **existing** |
| `convergence/chapters/round-02/fusion.md` | the canonical 30-ch outline (pre-change baseline; preserved) | **existing** |
| agents: `screen-writer` / `dramatist` / `audience` / `auditor` | re-author / structural+orphan critic / taste / state-drift | **existing** |
| `staff/showrunner/memory.md` + substance signature | state home-of-record once a revision stabilizes | **existing** (promote upward) |

## Running the checker

```
python3 scripts/check-threads.py \
  active-project/convergence/chapters/round-02/fusion.md \
  --config active-project/design/run-02/thread-config.txt
```

PASS = no new breaks beyond the catalogued exceptions. After any edit, the canonical outline must
still PASS. Baseline status: **PASS** (35 plants / 36 fires; R0–R4 all present).

## Conventions

- **Ripple scope: opportunistic** — required consistency fixes + a separate, opt-in Opportunities block.
- **Baseline preserved** — `convergence/` files are the untouched pre-change record; revisions live in
  the ledger until you ask to re-fuse into a new `convergence/round-NN/`.
- **Fences & FROZEN beats are never silently broken** — flagged, ratified with a written GUARD.
- **Promotion** — when a revised arc stabilizes, push it up into `convergence/` (re-fuse) and
  `showrunner/memory.md` (book deltas), and derive the substance signature from the state vectors.

## Re-baselining around a new outline

`idea-inbox.md` is the **small-grain** front door (one chapter note). When the principal brings a
whole **tentative outline** that should adapt-or-retire this planning wholesale, that's a
**re-baseline** — use the scaffold at **`../../intake/`** (run `../../intake/INTAKE-RUNBOOK.md`, or
`/and-reoutline`). It produces the next `design/run-NN/` from the adopted outline, carries over the
GUARDS + thread-config, archives superseded artifacts (never deletes), and re-checks PASS.

**Canonical run-02 Book I structure** now lives in `book-i-outline.md` (re-fused, thread-checked
PASS); `book-i-state-ledger.md` is the change-history + GUARDS + state/blast-radius working memory.
