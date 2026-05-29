# Next-session prompt — PROP-0019 validation against c05 three-FAIL trace

**Copy/paste this into a fresh session to run the comparison.**

---

PROP-0019 wired two new gates into the pipeline last session:
1. `/and-substance chapter` Phase 5.5 — chunk-level cold-read gate
2. `/and-stitch` Phase 8.5 — assembled-prose coherence review

The b01-c05 chapter exhausted the prior pipeline with three consecutive Phase 9 cold-read FAILs (~50 dispatches) and shipped under DEC-0044 (PROP-0018 Class B logic). PROP-0019 proposes that the two new upstream gates would have caught what FAIL #1 and FAIL #2 caught, at the cheapest layers, and would have surfaced FAIL #3's design-inherent class for principal disposition before any bones committed.

This session validates that claim by running the new gates against the c05 evidence archive at `archive/c05-three-fail-trace/`. Read that directory's README first.

## Test 1 — chunk-level cold-read on c05 chunk (validates Phase 5.5 catches FAIL #1)

Read the chapter chunk and scene chunks for b01-c05 from `active-project/staff/showrunner/memory.md` at `chapters[b01c05].chunk` + `chapters[b01c05].scenes[].chunk`.

Dispatch a general-purpose agent with the Phase 5.5 cold-read prompt from `.claude/commands/and-substance.md`. The agent reads ONLY the chunk text. NOT bones, NOT facets, NOT prior chapter chunks, NOT the substance contract.

Persist agent output to `staff/reviews/chunk-coldread-b01c05-validation.md`.

**Diff against intent.** Compare the agent's criterion 6 summary against `chapters[b01c05].goal`. Classify as PASS-CHUNK / CHUNK-CLASS-A / CHUNK-CLASS-B per Phase 5.5 Step 2.

**Compare to archived Phase 9 FAILs.** Read `archive/c05-three-fail-trace/fail-1-coldread.md` (Class A — central event not recovered) and `fail-3-coldread.md` (Class B — design-inherent CONTINUE=NO with central event recovered). Question: did the chunk-level cold-read catch the same FAIL class earlier? Specifically:

- Did the chunk-cold-reader recover the central event (would have prevented FAIL #1 with chunk-revise)?
- Did the chunk-cold-reader flag any of the FAIL #3 design-inherent concerns (stranger-violence; feed-mechanics; abstract-payoff; stakes-shape) BEFORE bones/facets/stitch committed?

Persist comparison to `staff/reviews/prop-0019-validation-test-1.md`.

## Test 2 — assembled-prose coherence review on FAIL #2 draft (validates Phase 8.5 catches FAIL #2 mechanism)

The FAIL #2 draft is preserved at `archive/c05-three-fail-trace/fail-2-draft.md`. It contains the "below the register I would have called human" phrasing at @14 that the cold-reader interpreted as possible sexual assault.

Dispatch a general-purpose agent with the Phase 8.5 mandate (three checks: weave / followability / cold-read-risk surface). Inputs:
- The FAIL #2 draft (`archive/c05-three-fail-trace/fail-2-draft.md`)
- Current bones at `active-project/theater/bones/b01-c05.md` (NOTE: this is the POST-recast bones; for fairest test, the agent should be told the FAIL #2 era had @13="the three figures pin the courier" — explicitly invert the recast in the brief so the agent reads the FAIL #2 prose against the FAIL #2 bones it was rendered from)
- Facets at `active-project/theater/facets/*-b01-c05.md`
- Chunks + scene_conflict + substance_delta from showrunner memory
- Exposition entries

Persist agent output to `staff/reviews/coherence-b01c05-fail2-validation.md`.

**Compare to archived Phase 9 FAIL #2.** Read `archive/c05-three-fail-trace/fail-2-coldread.md`. The cold-reader flagged five complaints, including the sexual-assault read at @14. Question: would the Phase 8.5 coherence reviewer have flagged `COLD-READ-RISK @14` for the "below the register" phrasing? Did it cite the misread vector + the substance-correct reading? Did it route to the right layer (stitch-revise of @14 OR bones-revise of @13)?

Persist comparison to `staff/reviews/prop-0019-validation-test-2.md`.

## Test 3 — coherence review on the FAIL #3 / shipped draft (catches FAIL #3's residual class)

The terminal draft is at `archive/c05-three-fail-trace/final-draft-shipped-with-caveats.md` (same content as the live `active-project/draft/b01-c05.md`).

Dispatch a general-purpose agent with the Phase 8.5 mandate against the SHIPPED draft. The shipped draft addressed the FAIL #2 sexual-assault read; the FAIL #3 cold-read surfaced design-inherent concerns. Question: does the coherence reviewer correctly distinguish "execution-quality defects to route to per-layer revise" from "design-inherent risk to surface to principal"? Specifically:

- The "below the register" phrasing is gone — coherence should return PASS or only ADVISORY findings on the @14 region (the sexual-assault risk is closed).
- The design-inherent concerns (stranger-violence, feed-mechanics, abstract-payoff) — does the coherence review correctly mark these as NOT WEAVE-GAPs (the prose IS coherent; it just renders a challenging chapter design)?

Persist comparison to `staff/reviews/prop-0019-validation-test-3.md`.

## Synthesis

After all three tests, write a synthesis report at `staff/reviews/prop-0019-validation-synthesis.md` answering:

1. Would PROP-0019's Phase 5.5 chunk-cold-read have caught FAIL #1 at chunk layer? (~$1 catch vs $50 actual.)
2. Would PROP-0019's Phase 8.5 coherence review have caught FAIL #2's @14 misread at stitch-revise layer? (~$2 catch vs $30 actual revise cycle.)
3. Would PROP-0019's Phase 5.5 chunk-cold-read have surfaced FAIL #3's Class B risk for principal disposition before bones commit? (Zero-commit disposition vs three-revise-cycle disposition.)
4. Does the coherence review correctly distinguish execution-defects (route to revise) from design-inherent risk (route to principal / surface as advisory)?

Net validation: did PROP-0019 + PROP-0018 together close the three-FAIL trace's failure mode, OR are there residual gaps?

If validation surfaces gaps or false-positives, append findings to `staff/admin/process-proposals.md` (new proposal candidate or amendment to PROP-0019).

## Spend cap

~10 dispatches total (3 cold-read variants + 3 coherence variants + 3 comparison writeups + 1 synthesis). Under the principal's cost ceiling for evidence-gathering on process changes.

## Status reporting

After each test, commit + push to the working branch with a clear message naming the test and verdict. Final state: validation results live + PROP-0019 ready for triage (with evidence) OR an amended PROP-0019-A with the residual-gap addressing.
