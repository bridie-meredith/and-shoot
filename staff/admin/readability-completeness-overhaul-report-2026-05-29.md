# Readability + Completeness Overhaul — session report

**Date:** 2026-05-29
**Branch:** `claude/intelligent-gauss-qacpV` (merged to `main` at session close)
**Scope:** pipeline command bodies + showrunner-memory schema + CLAUDE.md. No new commands; all changes ride existing checkpoints.
**Evidence base:** the b01-c05 three-FAIL trace (`archive/c05-three-fail-trace/`). All verification was retroactive on the already-shipped c05; **none of these gates has yet fired on a live chapter.**

---

## 1. Why — the root cause

The b01-c05 chapter exhausted the pipeline with three consecutive `/and-stitch` Phase 9 cold-read FAILs (~50 dispatches) and shipped under DEC-0044 (ship-with-caveats). Decomposing the trace:

- **FAIL #1** — the central beating "muffled" by abstracted prose ("a beating I almost missed").
- **FAIL #2** — the @14 "below the register I would have called human" phrasing misread as sexual assault.
- **FAIL #3** — design-inherent CONTINUE=No (stranger-violence, feed-mechanics opacity, abstract payoff).

The principal's framing of the root cause: **the cold-reader lacks context** — a no-context reader judging a mid-series chapter flags the accumulated world/character context as confusion. Investigation refined this into **two** distinct, compounding failures:

1. **A completeness/context gap caught too late.** The only reader-question pass (`/and-stitch` Phase 9 cold-read) fires at the most expensive recovery point, and it is context-blind by design — so it generates context-noise on every mid-series chapter and catches genuine gaps only after bones+facets+stitch have committed.
2. **An airless voice.** The prose renders concrete bones through instrument register ("the feed filled the junction / the categorization held / the count let him go") — the cold-readers' "I cannot find a person to follow." This is a *render-layer* defect: c05's **bones were concrete** ("the three figures strike the courier") and passed every floor; the density was injected at stitch.

A structural observation tied both together: **the pipeline's editorial verbs are almost all subtractive** (`CUT`/`COMPRESS`/`SIMPLIFY`); the one additive pass (`/and-review staging`) was advisory. So the chain monotonically thins prose and certifies the thinnest-survivable version clean — and **completeness and readability trade off invisibly** (an informed reviewer reads the airless version as both clear *and* economical, so it scores clean on a single judgment).

---

## 2. What — the changes (in build order)

### PROP-0019 validation + PROP-0019-A re-scope (the chunk-cold-read / coherence legs)

Validated the two PROP-0019 gates against the c05 archive:
- **`/and-stitch` Phase 8.5 (assembled-prose coherence) — VALIDATED.** Catches FAIL #2's @14 misread at HIGH confidence one phase upstream, routing to the exact `@13 pin→strike` bones-fix the team took three FAILs to find.
- **`/and-substance` Phase 5.5 (chunk cold-read) — NOT validated against this trace.** The chunk-reader recovered the event and returned CONTINUE=yes (`PASS-CHUNK`); it neither pre-empts FAIL #1 nor surfaces FAIL #3, because (a) readers extend *outline-charity* to opacity they'd reject in prose, and (b) the muffle defect doesn't exist at chunk-read time.

**PROP-0019-A** re-scoped Phase 5.5: new `PASS-CHUNK-VOICE-RISK` verdict + Step 2.5 voice-density guard (Signal A excused-confusion, Signal B abstraction-dense central event) + a no-charity Q7 with strict-CONTINUE; the verdict *arms* `/and-stitch` Phase 8.5's new **central-event-muffle** check (the FAIL #1 mechanism the chunk layer can't see). A Step-2 logic bug (a dead PASS-CHUNK branch) was surfaced *by the rerun* and fixed.

### Spine-legibility pair (URI-WRITE-EVENT-CONCRETENESS + URI-STITCH-SPINE-STAGING)

- **`/and-write` Phase 6:** `EVENT-NOT-CONCRETE` (HARD — the central-event bone must be concrete actor-verb-object, not an instrument/process rendering) + `ABSTRACTION-DOMINANT` (SIGNAL — grounding bones < 25% of non-chatter). Strengthens the existing `≥1-grounding-bone` floor to protect the *spine* and *scale*.
- **`/and-stitch` Phase 9:** spine-promotion — a single `STAGE`/`GROUND`/`NEEDS-BEAT`/`EXPAND` finding on a central-event/stakes-axis bone now blocks (new `spine-staging-gap` cluster trigger; a central-event `STAGE`/`NEEDS-BEAT` escalates to FAIL). Gives the one additive pass blocking teeth on the spine, mirroring the cut verbs.

### PROP-0020 — completeness / context-weave track

Moves followability review *upstream and progressive*, four checkpoints:
1. `/and-review bones` followability **pre-check** (`follow_check`; `FOLLOW-FAIL` HARD-gates `/and-facets`).
2. `/and-facets` **Phase 2.5** post-R1 context review → **context-ledger** of `CONTEXT-REQUIRED` licensed exceptions (which let the R2 exposition judge add orienting glosses **past the add-cap and exempt from the new-plot-content / over-explain penalties** — resolving the "context the reader needs is the exposition the pipeline penalizes" tension).
3. `/and-facets` **Phase 4.5** post-R2 re-check (terminal in the common case).
4. `/and-facets` **Phase 4.6** conditional R3 + fixer-edit-or-WARN.
Auditor (Phase 5) + audience-gate (Phase 5b) read the ledger and suppress the anti-exposition penalty for ledger-licensed entries only.

### PROP-0022 — readability / aliveness twin

The mirror of PROP-0020, riding the same checkpoints with a **second axis**:
- The bones pre-check + Phase 2.5 + Phase 4.5 also ask **aliveness** ("a person to follow, or only an apparatus?"), classifying `OK` / `VOICE-FIXABLE` (render-choice fix) / `GROUNDING-REQUIRED`.
- **Grounding-ledger** (mirror of the context-ledger): a `GROUNDING-REQUIRED` line licenses a sensory add **past the frequency-band cap** — the symmetric fix to "the grounding that makes dense prose breathe is what the sensory cap trims." Exemptions wired into Phase 5 auditor + Phase 5b audience-gate; adds authored by the sensory-author at Phase 4.6.
- **Separated scoring (#5):** Phase 4.5 and the Phase 9 terminal gate score completeness and readability **independently and require both** — a chapter cannot ship clean by being maximally complete while reading airless.
- **Voice-embodiment discipline (#6):** `/and-stitch` Phase 4 — for an instrument-mediated POV, prefer the **person-first** faithful rendering over apparatus-register, **within the bone-faithfulness fence** (re-choose phrasing, never add content). `VOICE-APPARATUS-DEFAULT` → re-render; `EMBODIMENT-BLOCKED` → route upstream. Calibrated against `active-project/voice-exemplar.md`.

### Cleanup
- `schemas/showrunner-memory.schema.md`: added `chunk_cold_read` (incl. `voice_risk`), `bones_review.follow_check`, `context_followability` (both axes + ledger counts), `cold_read.readability_axis`.
- `CLAUDE.md`: new Rule 17 documenting both tracks + the spine pair; pointer to this report.

---

## 3. Observed outcomes (verification — all retroactive on shipped c05)

| Gate | Run | Result |
|---|---|---|
| PROP-0019-A Phase 5.5 | rerun on c05 chunk | original `PASS-CHUNK` → revised **`PASS-CHUNK-VOICE-RISK`** (Signals A+B). Reproduced cleanly after the logic-bug fix. |
| PROP-0019-A Phase 8.5 | rerun on shipped draft | central-event-muffle **PASS on quoted evidence** ("The third struck him." L31) vs the original PASS-*by-omission*. Would SOFT-BLOCK on a muffled draft. |
| PROP-0020 Phase 2.5 | rerun on c05 graph | **1 CONTEXT-REQUIRED + 3 WEAVE-FIXABLE.** The one real gap (ctx-001 @19: the report rides the same Jarvis→Otto channel as the enforcement) is an *inverse-frame* find a cold-reader can't surface — the Sera/Jarvis/feed confusions came back closed for a context-aware reader. |
| PROP-0020 Phase 3 coupling | exposition ledger-add | licensed gloss `exposition:5 @19` authored exempt from add-cap; ledger `satisfied`. |
| PROP-0020 Phase 4.5 | rerun | **FOLLOWABLE** — ctx-001 closed; no Phase 4.6. |
| PROP-0022 aliveness axis | rerun on c05 graph | **AIRLESS** (8 VOICE-FIXABLE + 5 GROUNDING-REQUIRED) **where completeness returned FOLLOWABLE** — the twin catches the c05 cold-read's "abstracted into feed and count" complaint exactly where the completeness pass structurally could not. |
| PROP-0022 voice-embodiment | re-render c05 s03 | **12 of 13 beats person-first with ZERO content invention**; 1 correctly held `EMBODIMENT-BLOCKED`. Finding: *the airlessness is in the render, not the bones.* |

**Headline outcomes:**
1. The **detection gap is closed** — the readability axis flags airless where completeness passed (PROP-0022 verification A).
2. The **fix is the right lever and is sufficient for c05** — person-first rendering de-airless without invention, confirming the density was render-layer, which is why the bone-layer floors (#1/#2) were correctly scoped as *not* the density fix and the voice discipline (#6) *is* (PROP-0022 verification B).
3. The **context-aware review finds sharper gaps than the cold-reader** — it discards the cold-reader's series-context noise and surfaces the one real load-bearing seam (PROP-0020 Phase 2.5).

---

## 4. Honest limitations

- **Nothing is live-proven.** Every verification ran retroactively on already-shipped, already-remediated c05. We showed the gates *don't false-alarm on a clean chapter* and *detect/fix in isolation* — we have **not** shown they would have prevented the original three FAILs on the first pass. **b01-c06 is the first live test.**
- **The context-aware reviews found *different* gaps than the original FAILs.** ctx-001 (Jarvis→Otto) is real but was not the dominant FAIL driver (prose-abstraction + the @14 misread were). "Found the real gap" ≠ "found the gap that caused the FAILs."
- **The terminal Phase 9 cold-read is still context-blind by design.** We drained context-catching upstream and added a readability axis; we did not change the cold-read's uninformed stance. A mid-series chapter can still generate context-noise there.
- **The voice-exemplar was leaned on, not freshly authored.** The existing Robinson contemplative exemplar is a decent "dense-but-breathing" target but may want tuning as the locked series voice.
- **The ledgers + new memory fields are now schema'd** (this session), but the two ledger *file formats* live as inline schemas in the command bodies, not as standalone `schemas/*.md`.

---

## 5. Change ledger

| Tag | Change | Files | Status |
|---|---|---|---|
| PROP-0019 | validation + addendum | `staff/admin/process-proposals.md` | validated (8.5) / not-validated-vs-trace (5.5) |
| PROP-0019-A | Phase 5.5 re-scope + 8.5 muffle coupling | `and-substance.md`, `and-stitch.md` | wired + rerun-reproduced |
| URI-WRITE-EVENT-CONCRETENESS | EVENT-NOT-CONCRETE / ABSTRACTION-DOMINANT | `and-write.md` Phase 6 | wired, untested-live |
| URI-STITCH-SPINE-STAGING | spine-promotion | `and-stitch.md` Phase 9 | wired, untested-live |
| PROP-0020 | context-weave track (4 checkpoints + context-ledger) | `and-facets.md`, `and-review.md` | wired + exploration-rerun on c05 |
| PROP-0022 | readability twin (aliveness axis + grounding-ledger + separated scoring + voice-embodiment) | `and-facets.md`, `and-stitch.md`, `and-review.md` | wired + verified on c05 |
| — | schema + CLAUDE.md sync | `schemas/showrunner-memory.schema.md`, `CLAUDE.md` | done |

Reports/artifacts under `active-project/staff/reviews/`: `prop-0019-validation-*`, `prop-0019a-rerun-comparison.md`, `context-follow-r1/r2-b01c05-*`, `aliveness-r1-b01c05-verify.md`, `voice-embodiment-rerender-b01c05-s03-verify.md`; ledgers under `active-project/staff/showrunner/{context,grounding}-ledger-b01-c05.md`.

---

## 6. Next

- **b01-c06 is the live test.** Run the chapter forward through the chain and watch whether these gates fire *before* anything ships — the real validation this session could not provide.
- Optional: tune `active-project/voice-exemplar.md` as the locked series voice; promote the two ledger formats to standalone schemas if they prove durable.
