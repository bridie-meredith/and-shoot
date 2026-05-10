---
phase: B2b-rerun — decision-discipline review against native R2 decision logs
project: R2 hybrid judge tuning
date: 2026-05-10
scope: s01e01 native .r2-decisions.md emitted at Plan C C1
parent: design/shoot-v2/r2-judge-tuning/B-locked-rubric.md
companion: design/shoot-v2/r2-judge-tuning/2b-baseline.md (reconstructed-from-git scoring; F-R2-2 unscoreable)
predecessor: design/shoot-v2/plan-c-2026-05-10-unified.md C1 (validation re-run)
status: COMPLETE
---

# B2b-rerun — Native R2 decision-log scoring against G1–G4

## Scope

B2b-baseline scored the reconstructed-from-git baseline (8 memory + 12 feeling = 20 entries) and could only score G1, G3, G4 reliably; G2 (motive honesty) was unscoreable because raw git-diff decisions don't preserve author motive. B2b-rerun closes that gap by scoring native `.r2-decisions.md` shards emitted by R2 authors who wrote their motive into the prose, not reconstructed by an analyst from a diff.

**Corpus:** Plan C C1 native shards — 6 decision-log files covering the full 4-layer R2 chain:
- `active-project/staff/interest-narrator/r2-decision-shard.md` (R2.1; 21 existing + 2 adds)
- `active-project/staff/memory/r2-decision-shard.md` (R2.2; 4 existing + 1 add)
- `active-project/staff/feeling/r2-decision-shard-taylor-hebert-jaehaerys.md` (R2.3 Taylor; 4 existing + 0 adds)
- `active-project/staff/feeling/r2-decision-shard-oc-craftsman-mother.md` (R2.3 mother; 4 existing + 0 adds)
- `active-project/staff/feeling/r2-decision-shard-oc-craftsman-father.md` (R2.3 father; 3 existing + 0 adds)
- `active-project/staff/metaphor/r2-decision-shard.md` (R2.4; 1 existing + 0 adds)

**Consolidated artifact:** `active-project/theater/facets/.r2-decisions.md` (456 lines, summed `f-r2-counts: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 2}`).

## Plan C C1 gate evaluation

Gate: **0× F-R2-1, ≤2 combined F-R2-2/3/4** across all R2-touched entries.

Result:
- F-R2-1: 0 ✓
- F-R2-2: 0
- F-R2-3: 0
- F-R2-4: 2 (NI within-character pre-calc-frame saturation; Taylor-feeling breath-clause formula)
- Combined F-R2-2/3/4: **2 ≤ 2 ✓**

**Gate verdict: PASS.**

This is the first execution of the edited `/and-facets-r2.md` command after URI-023 item 9 (§Form re-test) and Plan B B2a G5 position-gate landed. Both F-R2-4 instances were caught **and mitigated in the same dispatch** — revise narrator:8 to non-formula construction; delete feel:2 + strip breath-clause from feel:3/feel:4. The discipline working as designed.

## G1 — "Does the revision still earn its place when I read it cold?"

**Failure mode addressed:** F-R2-1 (form-discipline drift on revisions).

**Score: PASS across all shards.**

Native log evidence:

- **NI narrator:1 REVISE:** reviewer names what the cold-read trips on (`"the original 'the loft boards hold their cold; the dye-yard fauna are already where they were last night' is a two-clause spine"`) and articulates the form failure specific to this entry, not a label citation. URI-023 #9 re-test working.
- **NI narrator:2 REVISE:** same cold-read discipline (`"reads as a base-register inventory cadence (the X — A, B), not a single-clause spotlight"`). Specific to the entry.
- **NI narrator:8 REVISE:** the most load-bearing G1 trace in the run. Reviewer identifies F-R2-4 formula-saturation, then asks G1: "the cold-read after revision does not trip; the new construction names the moment-of-arrival distinctly from narrator:7's eye-line-arrival."
- **NI narrator:11 REVISE:** "Cold-read trips on the semicolon. Same form-discipline failure mode as narrator:1." Names failure mode AND specific entry pattern.
- **Memory memory:1 REVISE:** "The §Form re-test on the revision: one clause, one arrow, free-text gloss naming the monument family precisely."
- **Feeling Taylor feel:3 REVISE:** "G1 cold-read on revision holds; the single clause is the full somatic, expressed yes."
- **Feeling Taylor feel:4 REVISE:** card-§-anchored cold-read named explicitly.
- **Metaphor metaphor:1 REVISE:** citation-ID correction only (`tens:2 → tens:52`); no §Form re-test needed (no content change).

**Arbiter check:** does the justification name something specific to this entry rather than reciting rubric labels? **YES across all 8 revises.** No mechanical recitation pattern.

**Note on R1-authored form drifts caught at cold-read:** narrator:1, narrator:2, narrator:11 were R1-authored semicolon-spine / em-dash-list violations that R1 itself missed. The §Form re-test at R2 visited them on a graph-aware pass and caught them at-rest. **The gate is doing more structural work than "guard against R2 introducing new violations on revise" — it's a backstop against R1 form drift as well.** This is the structural fix URI-023 #9 was designed to install.

## G2 — "Why does this entry want to be added — and is that wanting honest?"

**Failure mode addressed:** F-R2-2 (multi-justification under-strictness on adds).

**Score: PASS across all 3 adds.**

The gap B2b-baseline could not score. Native logs make it scoreable for the first time.

- **NI narrator:22 @34 ADD (approach-zone):** at-rest reading first ("the reading: she has stilled her feet a beat before the slip emerges"); the niche enables the question, the at-rest reading answers it ("the fire registers her pre-cognition of the @35 event rather than her reaction to it; that is forward-motion work, not register-decoration"). Honest motive.
- **NI narrator:23 @84 ADD (trailing-edge):** at-rest reading explicit ("the at-rest reading: she holds her head at the angle her mother's hand chose"). Position-gate (G5) reasoning integrated with at-rest reading. Honest motive.
- **Memory memory:5 @99 ADD (peak):** the only borderline case. Reviewer leads with "The graph reveals @99 as a structural absence" — niche-recognition step. Per A-corpus, niche-recognition is allowed as the **enabling** step; the motive is honest if the at-rest reading then **answers** the question. Reviewer pivots to G2 explicitly ("the proto-line is *asking* for the entry") and traces displacement-content honestly. The at-rest reading is substantive. Honest motive judged by full paragraph context.

**Arbiter check at Phase 5.5 considered firing T4 ("niche-driven add justification") on memory:5 because the lead sentence is niche-recognition. Decision: do not fire — the paragraph as a whole carries at-rest reading as the load-bearing argument; the niche is the enabling cue, not the answer.**

**Decision-discipline finding (load-bearing for B-locked-rubric):** the G2 question is "is the wanting honest?" — and "honest" includes the case where the reviewer **opens** with niche-recognition and then traces the at-rest motive. The arbiter T4 trigger as specified ("Set aside the cite-index for a moment. Does it want this entry?") fires on **niche-only justifications**, not justifications where niche is the lead but at-rest reading is the bulk. Native logs validate this interpretation; B2b-baseline could not have surfaced it.

## G3 — "Does this entry hold up when I block out what comes next?"

**Failure mode addressed:** F-R2-3 (lonely-entry adjacent-context dependency).

**Score: PASS across all entries that carry an at-rest defense.**

Native log evidence:

- **Memory memory:2 KEEP G3 trace:** "the entry's work is complete at its anchor — 'this paper is the leaf the apparatus opens with' does not lean on what comes next."
- **Memory memory:3 KEEP G3 trace:** "the entry stands at @69 — the body-was-taught construction is complete-at-anchor and does not lean on @76+."
- **Memory memory:4 KEEP G3 trace:** "the entry holds at @119 — the daughter-has-not-handed-over construction is complete."
- **Memory memory:5 ADD G3 trace:** "the entry stands at @99 — 'the stroke fixes the role' is complete at anchor; the consequence-line closes the displacement at @99, not at @100+."
- **NI shard:** G3 not named per-entry as a separate gate, but each KEEP's justification names what the entry **does at its anchor** without referring to adjacent stream — meets the gate substantively.

**Arbiter check:** does the justification stand when adjacent context is omitted? **YES across the 4 memory entries explicitly named with G3 trace.** The gate functions correctly as a "fires when needed" gate, not a per-entry recital.

## G4 — "Does the facet, as a whole, feel patterned in a way it shouldn't?"

**Failure mode addressed:** F-R2-4 (within-character / cross-character pattern blindness).

**Score: PASS-WITH-NOTES.**

Native log evidence (the strongest signal in the run):

- **NI PATTERN-SCAN:** reviewer end-to-end scan caught the `"she had already X"` formula across narrator:4/7/8/16/17 (5 of 21 entries; 24%). Pattern flag came with remediation argument — "Mitigation lands on narrator:8 (the most redundant instance); narrator:17 at the peak is preserved because the formula's recurrence at the @99 peak serves the spotlight." This is the "I'd cut these, here's why" structure G4 requires. F-R2-4 incremented to 1.
- **Memory PATTERN-SCAN:** end-to-end scan with mem:5 added — explicit per-entry construction-template check ("'the X meets her the way the Y' (mem:1), 'the paper is the leaf the apparatus' (mem:2), ..."). Single-register-soft Earth-Bet displacement pattern flagged but defensible at episode-level under per-season carve-out, with watch-item for s01e02+. **Exactly the discipline G4 was designed to produce.**
- **Feeling Taylor PATTERN-SCAN:** breath-as-second-clause across all four R1 entries (4 of 4; 100%). F-R2-4 incremented to 1. Mitigation explicit and asymmetric: feel:1 keeps load-bearing breath signature, feel:2 deleted, feel:3 + feel:4 revise to strip the formula clause. Post-revision count: 1-in-3 (signature instance + 2 distinct body-anchored tells).
- **Feeling mother / father:** small files (4 + 3 entries), no within-character patterns detected. Cross-character pattern between Taylor and mother/father explicitly checked at mother fork and verified not to fire (different anatomy / scene-position / register). G4 fires only when warranted.
- **Metaphor:** single-entry file; pattern-scan returns "Nothing patterned. One entry, one construction, one character. The refuse-by-default discipline held."

**Arbiter check:** does the pattern flag come with what specifically should change? **YES in both F-R2-4 instances.** NI traces revise-not-delete reasoning with peak-position carve-out. Feeling traces delete-plus-revise asymmetric mitigation with card-signature defense for the spared clause.

**PASS-WITH-NOTES:** per-season-soft carve-out for memory's Earth-Bet displacement pattern is acceptable at episode-1 scope but creates a watch-item for s01e02+. Rubric does not change; queue carries the watch (URI-023 #1-8 carry-back is the parent surface for memory rubric V2.1 items).

## G5 — "Does this entry want to fire here, given where the scene is?"

**Score: PASS across all 3 adds.**

Gate added at B2a carry-back from audience finding on R2-adds at @131 closing in archival/filing register. C1 is the first execution under the gate.

- **NI narrator:22 ADD:** position-category named explicitly ("position: approach-zone"); scene-motion named; contribution-vs-motion articulated ("forward-motion work, not register-decoration").
- **NI narrator:23 ADD:** position-category named ("position: trailing-edge"); contribution ("extends the @83 peak's consequence into the trailing beat rather than archiving it").
- **NI cap-refusals invoking G5:** cap-refusal trace explicitly invokes G5 on @113 (post-peak body-automaticity), @120 (would compound to filing register adjacent to narrator:20), @131 (episode-close paired-archive failure mode named directly: "would compound to filing register at the @131 ledger-entry, which is the structural failure mode G5 explicitly names for episode-close"). **G5 doing its work both on adds it accepts and on adds it refuses.**
- **Memory memory:5 ADD:** position-category named ("position: peak"); special-case check explicit ("@99 is at 75% of the proto-line stream, NOT in the final 5–10% (@125–@131). The @131 marks-the-ledger-entry beat carries no R2-touched memory entry, so no paired-archive seam exists"). G5 special-case fully traced.
- **Metaphor refusals:** G5 implicit in position-aware refusals at @99 (peak; AP7 default-refuse stack), @119 (figurative-restatement on existing memory).

**Arbiter check:** does the justification name a position category and the scene-motion it implies? **YES across all 3 adds.** No position-blind add survived in the corpus.

## Cross-cutting findings

1. **§Form re-test (URI-023 #9) catches both R2-introduced and R1-original form drifts.** NI narrator:1, narrator:2, narrator:11 were R1-authored violations R1 missed. R2's cold-read caught them at-rest. **Rubric implication:** B-locked-rubric.md G1 spec is correct; native log evidence confirms cold-read discipline produces the intended effect on both R1 and R2 form-drift.

2. **G2 niche-vs-at-rest distinction is more nuanced than B-locked-rubric.md captures.** Memory memory:5's lead sentence is niche-recognition; the body is at-rest reading. Arbiter T4 trigger as specified would fire on the lead, but paragraph-as-whole satisfies G2. **Rubric implication:** the gate is correct in intent; T4 trigger guidance in `C-arbiter-protocol.md` should clarify that lead-sentence niche-recognition is not by itself T4 if at-rest reading carries paragraph weight. Logged as B-locked-rubric V3 candidate edit (non-blocking).

3. **G5 position-gate fires on refusals as much as on accepts.** NI cap-refusals show the gate functioning bidirectionally. **Rubric implication:** G5 spec correct; gate functions as directional (accept / refuse with position reasoning), not permissions check.

4. **Free-prose decision format is dramatically more scoreable than labeled-subfield format.** B2b-baseline could not score G2 from git diff because diff doesn't capture motive. B2b-rerun scores G2 cleanly on every add because authors wrote motive into prose. **Process finding (not a rubric edit):** PLAN v1 labeled-subfield template was structurally checklist-shaped and unscoreable for taste; locked-rubric free-prose discipline produces logs downstream review can taste-judge. Deepest validation of URI-017 Threshold Discipline principle ("rubric arithmetic is advisory, taste authoritative") in concrete artifact form.

5. **Margit referrals queued from native logs.** Memory layer surfaced 5 candidate monument-card promotions (`monument-fauna-as-first-responder`, `monument-cape-reflex-trained-body`, `monument-parent-as-cost-vector`, `monument-care-system-as-trap`, `monument-control-as-evidence`, `monument-administrative-record-as-trigger`). URI-003 progress; route to margit at next card-authoring session.

## Disposition

- **URI-023 item 9 (§Form re-test mandatory before any verdict):** ✓ **CLOSED.** Native log evidence confirms cold-read discipline produces specific-entry justification with no mechanical recitation. Pass discipline held across 4 layers and 5 per-character sub-forks.
- **URI-023 items 1-8 (feeling rubric V2.1 carry-back):** unchanged status (out of scope for R2 judge tuning; carry-back belongs to feeling-rubric authoring session).
- **URI-027 (F-R2-* class definition drift between A-corpus.md and audit-report.schema.md):** option 1 (patch schema to match A-corpus) confirmed correct by native log scoring. Schema patch lands at Plan C C5.
- **B-locked-rubric.md V3 candidate edit:** clarify T4 trigger guidance re: lead-sentence niche-recognition vs body-weight at-rest reading. Non-blocking; lives in `C-arbiter-protocol.md` update at next R2 tuning iteration.
- **Watch-item:** memory single-register-soft Earth-Bet displacement pattern at episode-level under per-season carve-out. Re-check at s01e02+ R2 fire.

## Plan B project close (B5)

C2 closes Plan B alongside this scoring:
- This file (`2b-rerun.md`) lands.
- `4-validation.md` updated to reference this file as discipline-review companion to validation re-run.
- `PLAN.md` → v3 (annotate phases A/B/C/D/E/F as historical; B2b split into baseline + rerun; G5 added at B2a; native logs supplant reconstructed baseline as canonical evidence).
- `upstream-tuning-queue.md`: URI-023 item 9 → CLOSED.
- **Plan B as a project: CLOSED.** Items 1-8 remain open under URI-023 parent (feeling rubric V2.1 carry-back) for a future feeling-rubric session.
