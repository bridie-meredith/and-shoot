# Chapters audit — b01 c01–c15 — new-process adoption + cross-chapter flow

date: 2026-06-04
scope: all shipped chapters (b01-c01 … b01-c15)
question: (1) are the new processes — the **aggregator** (`/and-stitch` Phase 10 forward-thread → `aggregate-state.md`) and the **cohesive** (`/and-cohere` + `/and-review cohere`) — actually implemented? (2) do the chapters flow chapter-to-chapter and hold a narrative? (3) are the chapters produced *since* those processes went live working as expected?
method: read-and-assess audit (no fresh cohere run). Sources: `aggregate-state.md`, `cohere/*-state.md`, all `cohere-*` + `coherence-*` reports, `parking-lot.md`, `cascade-checkpoint.md`, `memory.md` (grep), and direct reads of the c13/c14/c15 drafts + c13/c15 in-chapter coherence reports.

---

## TL;DR

**Both new processes are implemented and demonstrably working.** The aggregator has run unbroken on every chapter from c08 (its init point) through c15 — eight consecutive Phase-10 forward-threads, one of which (c10) actually fired a HOLD and was correctly resolved, proving the gate isn't a rubber stamp. The cohesive process ran on two overlapping windows (c01–c07 and c06–c12); on c06–c12 it caught a genuine **load-bearing** apparatus-register FAIL and drove it to convergence via the prologue-variation fix — the process did real work, not theater.

**The single material gap: the c13–c15 tail has never been cross-chapter cohered.** Cohere coverage stops at c12. The drafts themselves flow well at the seam (verified by direct read), and each has a clean in-chapter Phase-8.5 coherence PASS — but the *cross-chapter* "cohesive" pass that the user is asking about has not been applied to the last three chapters. This is already self-flagged in the parking lot (pl-2026-06-04-c15-004 / DEC-0087) as the designed handler for the two-consecutive-quiet pattern at c14/c15.

**Verdict: PROCESSES-HEALTHY, TAIL-UNCOHERED.** Recommend running `/and-cohere b01 c13-c15` next; it closes the coverage gap and is the designated handler for the accumulating-quiet and pending depth-pass items before book-close.

---

## 1. Process-adoption matrix

| Ch | Aggregator (P10 thread) | aggregate-state roll | In-chapter coherence (P8.5) | Cross-chapter cohere | Ship verdict |
|----|------------------------|----------------------|-----------------------------|----------------------|--------------|
| c01–c05 | pre-aggregator¹ | — | (legacy) | ✓ c01–c07 CAUTION | shipped |
| c06 | pre-aggregator¹ | — | PASS | ✓ c01–c07 **and** c06–c12 | shipped |
| c07 | pre-aggregator¹ | — | (legacy) | ✓ c01–c07 CAUTION | shipped |
| **c08** | **INIT** PASS-THREAD | init | PASS | ✓ c06–c12 | SHIPPED-WITH-CAVEATS² |
| c09 | rolled (light) | ✓ | PASS | ✓ c06–c12 | depth-pass **resolved** ✓ |
| c10 | **HOLD-THREAD → resolved** | ✓ | PASS | ✓ c06–c12 | shipped |
| c11 | PASS-THREAD | ✓ | PASS | ✓ c06–c12 | SHIPPED-WITH-CAVEATS² |
| c12 | PASS-THREAD | ✓ | PASS | ✓ c06–c12 | SHIPPED-WITH-CAVEATS² |
| **c13** | PASS-THREAD | ✓ | PASS | ✗ **not cohered** | clean PASS |
| **c14** | PASS-THREAD | ✓ | PASS | ✗ **not cohered** | SHIPPED-WITH-CAVEATS, depth-pass **pending** |
| **c15** | PASS-THREAD | ✓ | PASS | ✗ **not cohered** | SHIPPED-WITH-CAVEATS, depth-pass **pending** |

¹ The aggregator (Phase 10 / `aggregate-state.md`) was introduced with the chapter-production runbook and **initialized at c08** (commit `7e3aaa3`). c01–c07 predate it by design; they were retro-covered by the cohere process instead.
² Class-B SHIPPED-WITH-CAVEATS = design-inherent (apparatus-register / event-poverty pre-authorized in `chunk_cold_read.cold_read_risk_carry`), not a defect escape.

**Note on naming (avoids a common confusion):** `coherence-b01-cNN-*.md` files are the **in-chapter** Phase-8.5 assembled-prose reviews (part of `/and-stitch`, single chapter). `cohere-b01-cXX-cYY-*.md` files are the **cross-chapter** `/and-cohere` runs. The tail has the former for c13/c14/c15; it lacks the latter.

---

## 2. Are the new processes implemented? — YES

### Aggregator (Phase 10 forward-thread → `aggregate-state.md`)
- **Continuous and unbroken c08→c15.** `aggregate-state.md` carries an explicit roll entry for every chapter c08 through c15 (`Scoped through b01c15`, `through_chapter: b01c15`). No missing link in the chain.
- **It is a real gate, not a stamp.** c10 returned **HOLD-THREAD** (it held a chapter on a threading finding) and was subsequently resolved; `cascade-checkpoint.pending_threading_holds` is now `[]`. A process that has actually blocked at least once is a working process.
- **State-drift discipline holds.** Each roll records explicit STATE-DRIFT checks. c15's entry reconciles three distinct in-world clocks (KL-tenure eleven months / Vhagar-read two months / arrangement third month) and finds them coherent. c14→c15 carry zero applied threading edits *because* every callback was already on-page — which is the healthy steady-state, not a skipped pass.
- **Hooks are tracked across the span:** hook-0006 (Aemond) advanced logistics-reference@c08 → ON-PAGE@c15; hook-0015 (gap-lane courier) opened c12 → PAID@c14; hook-0003 (Wren) PAID@c12. The forward-feed is doing the cross-chapter bookkeeping it was built for.

### Cohesive (`/and-cohere` / `/and-review cohere`)
- **c01–c07:** converged CAUTION-COHERE, 0 load-bearing fails, 5 SOFT advisories (sensory distribution, apparatus-register, antagonist-pressure fragmentation, scene-shape narrowness, threshold discipline).
- **c06–c12:** iteration-0 **FAIL-COHERE** on a load-bearing axis (naive-Q6 apparatus-register cumulative load tipping airless c08–c11) → DEC-0081 prologue-variation pass (7 distinct chapter openings, fence-clean, bodies untouched) → iteration-1 **CAUTION-COHERE**, converged. **This is the process catching a real cross-chapter defect and fixing it.**
- Structural CAUTIONs that aren't clean per-chapter fixes were correctly **routed forward** to `pl-2026-06-03-006` (target `/and-review verdict b01`), not force-fit into bones-revises.

**Conclusion:** both processes are wired, exercised, and have each demonstrably altered an outcome (c10 HOLD; c06–c12 prologue-variation). They are not vestigial.

---

## 3. Do the chapters flow? — YES for c01–c12 (cohered + verified); LIKELY-YES for c13–c15 (in-chapter verified, cross-chapter unconfirmed)

### What's confirmed
- **c01–c12** carry positive cohere verdicts on every load-bearing axis. Setup→payoff is the strongest axis (c06 "four names" → c07 "four absences"; Cobb-girl c04 italics → c07 reveal). Recurring bodies stay filed where they were left. Calendar/time legibility holds via sept-bell name-days + bay-weather.
- **c13→c14→c15 seam (my own direct read):** the handoffs are clean and the narrative is genuinely continuous —
  - **Wren-as-unpriced-item:** named in c14's preamble ("a person-shaped item the ledger had simply left open"), retroactively named in c14 body @21, then paid forward in c15 as the **gap-as-negative-shape** (the deliberately-uncovered east-water-gate lane made perceptible). Three-chapter propagation, on-page each step.
  - **cl04 courier:** opened (S03) and closed (S04, figure detained) within c14; the closing logic explicitly rhymes the closed entry with the open Wren omission. Self-contained and clean.
  - **Aemond:** handler-note cipher@c08 → ON-PAGE-observed@c15, explicitly logged-NOT-routed ("I routed nothing of him anywhere") — the escalation engine becomes visible without breaking the falling-arc design.
  - **The non-extractable lock:** "a channel found from both ends does not unmake" (c15 @9) deliberately completes the c14 confirmation. The c14 climax → c15 falling/quiet shape is intentional, not a sag.
- **In-chapter coherence PASS on c13, c14, c15** (Phase 8.5), each verifying the load-bearing hand-offs at the assembled-prose layer.

### What is NOT confirmed
- The **cross-chapter** cohere pass over c13–c15 has not run. The in-chapter reviews verify each chapter against its own bones; they do not run the naive/dramatist/audience cold-read *across* the three-chapter span the way `/and-cohere` does. Given that c14 + c15 are **both** Class-B SHIPPED-WITH-CAVEATS for the same event-poverty/apparatus-register family, the accumulation risk over the tail is exactly the thing the cohesive process exists to measure — and it hasn't measured it.

---

## 4. Open items the audit surfaces (in priority order)

1. **c13–c15 never cross-chapter cohered (coverage gap in the new process).** Closes with `/and-cohere b01 c13-c15`. Self-flagged: pl-2026-06-04-c15-004 + DEC-0087.
2. **Two mandatory depth-passes pending, both gate book-close:** c14 `pl-2026-06-04-002` (courier-not-felt-as-person) and c15 `pl-2026-06-04-c15-004` (event-poverty / two-consecutive-quiet). `cascade-checkpoint.pending_depth_passes: [b01c14, b01c15]`.
3. **`pl-2026-06-03-006` back-half structural items — partially paid, one real hole remains:**
   - Halvard re-entry/foreclosure — **LANDED@c13** ✓ (verified in c13 coherence report).
   - Dragonstone receipt — **ADVANCED@c14** ✓ (cloth-merchant flight = Dragonstone-side inference).
   - cl04 courier — **CLOSED@c14** ✓.
   - **Sera payoff hole — STILL OPEN.** The entire arrangement is owed against a protect-target who has never appeared on-page (she is *named* as the stake/guarantee throughout, but is not an embodied character in any draft c06–c15). This is the most significant standing narrative-integrity risk for book-close; correctly parked for `/and-review verdict b01`.
4. **Accumulating-quiet pattern (c14+c15 both Class-B):** the designed handler is cohere-before-book-close (DEC-0087). Item 1 above is also the fix for this.

---

## 5. Recommendation

The chapters since the processes went live are working as expected — the machinery is sound and the prose flows. The work that remains is **finishing the application of the new processes to the tail**, in this order:

1. `/and-cohere b01 c13-c15` — closes the cohere coverage gap (#1), serves as the accumulation handler for the two-consecutive-quiet pattern (#4), and informs the depth-pass scope (#2).
2. Resolve the two depth-passes (c14, c15) — both gate book-close.
3. `/and-review verdict b01` — consumes `pl-2026-06-03-006`, where the **Sera-never-on-page** hole (#3) is the one item that should be confronted before book-close rather than carried into b02.

None of these are defects in the new processes; they are the processes' own outstanding work, already self-flagged in the parking lot. The audit's net finding is that the aggregator + cohesive are healthy and the only thing missing is running the cohesive over the final three chapters.
