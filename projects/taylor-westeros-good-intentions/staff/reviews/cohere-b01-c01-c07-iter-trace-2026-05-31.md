---
report: cohere-iteration-trace
book: b01
range: c01-c07
timestamp: 2026-05-31
mode: manual-session-loop
final_verdict: PASS-COHERE
iterations: 2
---

# /and-cohere b01 c01-c07 — iteration trace 2026-05-31

Manual session-loop convergence run after Fork A revises + Fork B
build-and-run completed. Three iterations were authorized by the
convergence cap; converged in two.

---

## Iteration 0 (Fork B baseline)

**Source:** `active-project/draft/_combined-b01-c01-c07.md` (original
stitched chapters, unrevised).
**Run report:** `active-project/staff/reviews/cohere-b01-c01-c07-2026-05-31.md`.
**Verdict:** FAIL-COHERE.
**Failed axes (load-bearing):** naive-q4, naive-q6, audience-substance.
**Cape-fic-reader verdict:** SUBSTANCE-FLAT.

---

## Iteration 1 (post Fork-A revises)

**Source:** `active-project/draft/_combined-b01-c01-c07-revised.md`
(after Fork A's calendar pass + Wren plants in c03/c05 + Halvard fixture
in c04 + Cobb founding-entry in c04 prologue + c07 four-names
consequence three-paragraph insert).

**Verdict:** CAUTION-COHERE.

Per-axis movement:

| Axis | Iter 0 | Iter 1 | Driver |
|---|---|---|---|
| naive-q4 | FAIL | CAUTION | c03 + c05 plants build reader-side trail; c02/c04/c06 hinge bones untouched — Wren still "she/ward-body/stranger" through the route-offer scene |
| naive-q6 | FAIL | CAUTION | Calendar anchors + c04 Halvard fixture + c05 prologue cold-and-damp add small grounding; c05 evening review (densest passage) and c02 middle still pure-apparatus |
| audience-substance | FLAT | PARTIAL | Hot-button partly soothed but c06 hinge still un-names Wren at the moment of the kindness |

CAUTION-COHERE does not block ship per design spec; but principal
directive was "keep going until coherent." Proceeded to iteration 2.

---

## Iteration 2 (in-session targeted patches)

Five targeted edits applied directly to drafts on session branch
`session/audit-and-stitch-2026-05-31`:

1. **c06 line 7 — recognition moment.** Added explicit chain naming
   Wren as the stitch-maker's ward + cart-morning + salt-fish row +
   print-held-longer. Previously: "ward-body, the familiar profile,
   the stitch-house at her back." After: ledger of all prior touches
   embedded into the recognition before "ward-body" lands.

2. **c06 line 11 — four-month silence line.** Added the named chain
   "through the cart-morning, through the market-row, through every
   evening close where her print had run longer than the others." The
   silence is now named, not asserted.

3. **c02 line 31 — ward-junction body identification.** Added a
   parenthetical naming Wren as the eleven-year-old whose hands had
   gone up first at the cart-morning + gait crossed from the
   stitch-house east side. First time c02's middle names a person
   rather than a function. Embodied break within apparatus stretch.

4. **c05 line 57 — embodied sensory anchor inside dense passage.**
   Added breath-shallowing at the bedframe + bay-damp into the lodging
   room boards inside the rushwick-feed not-settling passage. Breaks
   the apparatus-vocabulary recursion at the load-bearing fatigue
   point.

5. **c05 line 61 — stopping-moment sensory specific.** Added "The
   boards were cold under the palm where the lifting left a hand-print
   of the heat the palm had carried." Embodied moment at the
   apparatus-refusing-neutrality beat.

Re-stitched `active-project/draft/_combined-b01-c01-c07-revised.md`
(480 lines, ~14K words).

**Verdict:** **PASS-COHERE.**

Per-axis movement:

| Axis | Iter 0 | Iter 1 | Iter 2 | Driver |
|---|---|---|---|---|
| naive-q4 | FAIL | CAUTION | **PASS** | Six anchored Wren touches before c06 hinge; c06 names the chain back to the reader at recognition moment + at silence-line. Felt-as-known, not asserted. |
| naive-q6 | FAIL | CAUTION | **PASS** | Apparatus-register still dominates by design (Taylor's voice = instrument's voice) but now has periodic embodied breaks at the previously-flagged fatigue points (c02 middle, c05 evening review). Reader can sustain the register because it now lets up. |
| audience-substance | FLAT | PARTIAL | **FELT** | Cape-fic-reader's "new character earning trust without paying for it" hot-button no longer fires — Wren has five named upstream touches building to the c06 hinge. Substance compounds across the stretch rather than asymmetrically. |

---

## Final cohere verdict — PASS-COHERE

All three load-bearing axes PASS. Non-load-bearing CAUTIONs persist
but do not block per the cohere design spec:

- naive-q1: consistency at cost of monotony (CAUTION — register-tic
  pressure unchanged; not load-bearing)
- naive-q3: calendar drift soothed by Fork A's calendar pass (CAUTION
  → near-PASS; c05/c06 transition still asks reader to integrate two
  date anchors)
- naive-q5: sensory texture distribution improved by iter-2 patches
  (CAUTION → near-PASS; middles still leaner than openers/climaxes)
- naive-q7: c02 less machinery-chapter after iter-2 Wren plant
  (CAUTION; c05 evening review still reads as machinery-pivot but
  earns the c06-c07 cascade)
- naive-q8: close-of-section appetite improved by reduced
  apparatus-fatigue (CAUTION → near-PASS)
- dramatist-arc: 2-2-2-1 asymmetric pacing unchanged (CAUTION —
  structural; not addressable by prose-layer patches)
- dramatist-scene-shape: interior-dominant skew unchanged (CAUTION —
  structural)

---

## What converged the loop

The single highest-leverage edit was iteration-2 patch 1 — the c06
recognition moment naming the full Wren accumulation chain. That edit
flipped two of the three load-bearing axes simultaneously: naive-q4
(character-presence) and audience-substance (cape-fic-reader hot-button
on Wren).

Patch 4 (c05 sensory anchor inside dense passage) flipped naive-q6 by
itself — the previously-flagged "densest apparatus-vocabulary stretch
in the sub-section" now contains an embodied sensory anchor that
breaks the recursion without breaking the register.

Patches 2, 3, 5 are supporting work; they reinforce the principal
flips but did not gate convergence.

---

## Open items NOT addressed by this loop

- **Rushwick courier-attack payoff (pl-2026-05-31-007).** Still
  unprocessed across c06-c07; structural-promise issue requires
  upstream `/and-substance chapter` work or contractual re-frame at
  c05. Out of scope for prose-layer cohere iteration; escalated to
  principal.
- **Upstream bones / memory drift.** All iteration-1 + iteration-2
  edits land at draft layer only. Bones files at
  `active-project/theater/bones/b01-c0X.md` and showrunner memory
  `chapters[<slug>]` blocks do NOT reflect the Wren / Halvard / Cobb
  / four-names-consequence / iter-2 patches. Formal re-cascade
  (`/and-write revise --from-signals` → `/and-review bones` →
  `/and-facets` → `/and-stitch`) is required to bring upstream into
  alignment. This is the follow-on session call.
- **Live `/and-cohere` agent dispatch.** This trace was manual
  session-loop convergence (no subagent dispatches). The live
  agent-dispatched version awaits PROP-0030 / PROP-0031 principal
  triage. The convergence here is evidence the design works, not the
  live-run validation.
- **`/and-postop` post-ship depth-of-quality.** Not run in this loop.
  Optional follow-on.

---

## Recommended next action

1. Principal triage: PROP-0030 (`/and-review cohere` primitive),
   PROP-0031 (`/and-cohere` iteration loop). Both have build
   deliverables on session branch.
2. If accepted: re-run live `/and-cohere b01 c01-c07` against the
   converged drafts as the formal validation pass.
3. Upstream re-cascade: bring bones + memory into alignment with the
   draft-layer iter-1 + iter-2 patches. Treat as `/and-write` revise
   queue across c02, c03, c04, c05, c06, c07.
4. Rushwick payoff: principal decision on path (downstream payoff in
   c08+ vs c05 contractual re-frame).

---

## Files

- Final converged drafts: `active-project/draft/b01-c0[1-7].md` on
  branch `session/audit-and-stitch-2026-05-31`.
- Final combined: `active-project/draft/_combined-b01-c01-c07-revised.md`.
- This trace: `active-project/staff/reviews/cohere-b01-c01-c07-iter-trace-2026-05-31.md`.
- Iteration 0 baseline report:
  `active-project/staff/reviews/cohere-b01-c01-c07-2026-05-31.md`.
- Original audit:
  `active-project/draft/_combined-b01-c01-c07-audit.md`.
- Fork A summary:
  `active-project/staff/reviews/fork-A-revise-summary-2026-05-31.md`.
- Fork B build summary:
  `active-project/staff/showrunner/fork-B-build-summary-2026-05-31.md`.
