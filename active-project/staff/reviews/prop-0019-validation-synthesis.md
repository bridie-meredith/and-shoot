# PROP-0019 validation — synthesis

**Date:** 2026-05-29
**Branch:** claude/intelligent-gauss-qacpV
**Protocol:** `archive/c05-three-fail-trace/NEXT-SESSION-PROMPT.md`
**Evidence base:** `archive/c05-three-fail-trace/` (b01-c05 three-FAIL trace)
**Per-test reports:** `prop-0019-validation-test-{1,2,3}.md` + the three raw agent reports (`chunk-coldread-b01c05-validation.md`, `coherence-b01c05-fail2-validation.md`, `coherence-b01c05-shipped-validation.md`)

---

## One-paragraph bottom line

PROP-0019's **Phase 8.5** (assembled-prose coherence at `/and-stitch`) **validates strongly** — it catches FAIL #2's @14 sexual-assault misread one phase upstream, routes it to the exact bone-fix the team took three FAILs to find, and on the shipped draft correctly refuses to manufacture a revise from accepted design-risk. PROP-0019's **Phase 5.5** (chunk-cold-read at `/and-substance chapter`) **does NOT validate against this trace** — the chunk-reader recovered the central event and returned CONTINUE=yes (`PASS-CHUNK`), so it would neither have pre-empted FAIL #1 nor surfaced FAIL #3's Class B risk for early disposition. The two legs of PROP-0019 are not equally proven: the stitch leg closes the c05 mechanism; the chunk leg addresses a *different* failure class than the one this trace exhibits.

---

## The four synthesis questions

### Q1 — Would Phase 5.5 chunk-cold-read have caught FAIL #1 at chunk layer? ($1 vs $50)

**NO.** The chunk-reader recovered the central event cleanly ("watches a man get worked over by people who clearly meant it… that night discovers she can't pretend it's just data anymore"), mapped it to the chapter goal, called the causal chain "clean," and returned **CONTINUE=yes** → `PASS-CHUNK`. No chunk-revise fires on a PASS. FAIL #1's mechanism was the central beating **muffled by clinical/abstracted prose** ("a beating I almost missed") — a defect introduced *downstream* at the facet + stitch layers. It does not exist at chunk-read time, so the chunk read cannot see it. (Test 1.)

### Q2 — Would Phase 8.5 coherence have caught FAIL #2's @14 misread at stitch-revise layer? ($2 vs $30)

**YES — decisively.** Phase 8.5 flagged `COLD-READ-RISK @14` at **HIGH confidence**, cited both the misread vector (the pin-to-stone + sealed alley-mouth + unnameable sub-human sound reads as sexual assault) and the substance-correct reading (chunk-authorized faction enforcement; the not-naming is feed instrument-failure), and routed primary to **bones-revise of @13 (pin → strike)** — *the exact fix DEC-0042 applied* — plus a secondary stitch-revise of @14. Catches the FAIL #2 mechanism one phase earlier at ~$2 vs the ~$30 full revise cycle actually spent. (Test 2.)

### Q3 — Would Phase 5.5 chunk-cold-read have surfaced FAIL #3's Class B risk for principal disposition before bones commit? (zero-commit vs three-revise-cycle)

**NO.** The chunk-reader gave only a sub-threshold whisper of the abstract-payoff concern ("earned for what it is… but small and internal — no external consequence lands") and did **not** flag stranger-violence or feed-mechanics at all. Critically it returned CONTINUE=yes, so the verdict is `PASS-CHUNK` — which proceeds straight to Phase 6 with **no Step-3 disposition**. Class B surfacing requires CONTINUE=No. The design-inherent risk never reaches principal disposition at the chunk layer. (Test 1.)

### Q4 — Does the coherence review distinguish execution-defects (route to revise) from design-inherent risk (advisory / principal)?

**YES — cleanly, in both directions.** On the FAIL #2 draft it fired SOFT-BLOCK on the real execution defect (Test 2). On the shipped draft it returned PASS — confirmed the @14 risk closed, and classified all four FAIL #3 design-inherent concerns as ADVISORY, **not** WEAVE-GAPs, explicitly reasoning that the prose weaves cleanly and the friction is a series-naive-reader artifact, not a seam. Zero spurious revises manufactured. (Test 3.) This is the discrimination the gate needs to be net-cost-positive.

---

## Net validation

**Did PROP-0019 + PROP-0018 together close the three-FAIL trace's failure mode?** **Partially — and the load is carried by Phase 8.5 + PROP-0018, not Phase 5.5.**

| FAIL | Mechanism | Closed by | Verdict |
|---|---|---|---|
| FAIL #1 | central event muffled by abstracted prose | **Phase 8.5** (assembled-prose read catches muffling/abstraction at the layer where it's introduced) — NOT Phase 5.5 | Closed by the stitch leg, not the chunk leg the proposal credited |
| FAIL #2 | @14 sexual-assault misread (stitch-rendering invention) | **Phase 8.5** (Test 2 — HIGH-conf, correct routing) | **Closed** |
| FAIL #3 | design-inherent CONTINUE=No, ship-or-revise call | **PROP-0018 Class B disposition**, surfaced at Phase 8.5/9 — NOT Phase 5.5 early disposition | Closed at terminal gate, not pre-empted at chunk layer |

**Residual gap (the headline finding):** PROP-0019's GAP-1 premise — that a chunk-level cold-read would have caught FAIL #1 and surfaced FAIL #3 early — **does not hold for this trace.** Two structural reasons (Test 1 root-cause):

1. **Outline-charity.** A reader handed an outline forgives opacity ("reads intentional") that the same reader, handed finished prose, reads as evasion. The chunk-reader and all three Phase-9 readers saw the *same* unexplained beating and unexplained Sera; the chunk-reader excused them, the prose-readers did not. The chunk-cold-read is systematically **more forgiving** on the CONTINUE axis.
2. **The defect lives downstream.** c05's failures were *prose-execution* failures — facet + stitch abstraction muffling a plainly-stated chunk event. None of that exists at chunk-read time.

The chunk-cold-read remains theoretically valuable for a *different* failure class — chapters whose **chunk itself** has a cause-chain hole or a CONTINUE=No design (e.g. a chunk that genuinely omits a connective, or one the reader rejects on premise). c05 is not that class: its chunk was sound; its prose was over-abstracted. So this validation neither kills Phase 5.5 nor confirms it — it shows c05 was the **wrong evidence base** to prove the chunk leg, and that the chunk leg has a structural false-negative bias for the voice-driven-abstraction failure class it was nominally credited with catching.

**Where this leaves PROP-0019 for triage:**
- **Phase 8.5 — keep, validated.** Strong evidence; close the FAIL #2-class mechanism; net-cost-positive (catches real defects, refuses spurious ones).
- **Phase 5.5 — keep but re-scope, or seek fresh evidence.** Its credited catch (FAIL #1 / FAIL #3) is unproven-to-disproven here. It may still earn its keep on genuine chunk-design holes, but the c05 trace does not demonstrate that, and the proposal's rationale overstates the chunk leg's reach. An amendment (PROP-0019-A) should (a) correct the GAP-1 claim, (b) note the outline-charity / downstream-defect limitation, and (c) either re-scope Phase 5.5 to chunk-design-hole detection explicitly or pin a different evidence base to validate it.

## Cost of this validation

3 review dispatches (1 cold-read + 2 coherence) + 0 dispatched writeups (comparisons + synthesis written by main session) = **3 dispatches**, well under the ~10 ceiling.
