---
audit: phase1-metaphor-baseline-review
facet: metaphor
episode: s01e01
target: design/shoot-v2/phase1-metaphor-baseline-naive.md (3 fires: @33, @64, @73)
authority: design/shoot-v2/rubric-metaphor.md (V1 LOCKED) + design/shoot-v2/metaphor-corpus.md
auditor-phase: 1 (rubric-blind baseline assessment — V1 lenient + V2 strict)
date: 2026-05-07
---

## Baseline under review

Three entries:

```
1 @33 allegory: the door that holds is the shape a closed room takes when the person behind it no longer answers
2 @64 allegory: two parallel lines — the mark a ledger makes when it has already decided and wants you to know it knew before you asked
3 @73 simile: the shadow of the frame takes her the way a threshold takes a body that has stood at one before and knows what is on the other side does not open toward her
```

---

## PASS 1 — V1 LENIENT

Criterion: does the entry not violate the schema text? Schema text (facet.schema.md § metaphor flags): "Comparisons, similes, allegories. Sparse by design — almost never used in end state unless dark humor or memory callback."

Two requirements extractable from this minimal text:
1. The entry must be a comparison, simile, or allegory (form).
2. The entry must be sparse by design — "almost never used unless dark humor or memory callback" (register).

### Entry 1 — @33 allegory

Form: "the door that holds is the shape a closed room takes when the person behind it no longer answers" — structurally an identity claim (door = shape a closed room takes). Allegory form is present.
Register: @33 is the beat where Osmynd's door stays shut. Memory-flag fires at @33 (dying-tutor cluster). Schema says "almost never used unless… memory callback" — this is plausibly a memory callback beat (the closed-door memory-flag is the anchor). The author's note names memory callback explicitly.

V1 verdict: **ACCEPT** (form present; memory-callback register plausible under lenient reading).

### Entry 2 — @64 allegory

Form: "two parallel lines — the mark a ledger makes when it has already decided and wants you to know it knew before you asked" — the ledger is personified and the parallel lines are treated as an intentional declaration. The structure is loose: the dash makes this a paratactic expansion rather than a strict identity-claim or simile. Under lenient reading, this reads as extended allegory (the ledger-act is portrayed as a pre-judged verdict; multi-element correspondence). Form is marginal but allowable under V1 lenient.
Register: @64 is the bureaucratic climax. The author's note claims "dark humor." Schema permits dark humor. Under lenient reading: dark humor register claimed; entry is sardonic.

V1 verdict: **ACCEPT** (form barely present under lenient; dark humor register claimed).

### Entry 3 — @73 simile

Form: "the shadow of the frame takes her the way a threshold takes a body that has stood at one before and knows what is on the other side does not open toward her" — explicit comparator "the way" is present. Simile form is clearly satisfied.
Register: @73 has both memory-flag and feeling-flag. Author's note names memory callback. Schema permits memory callback.

V1 verdict: **ACCEPT** (form clear; memory-callback register present).

### Lenient pass summary

**3/3 ACCEPT — lenient accept rate: 3/3 (100%)**

This is the expected result. V1 lenient is a form-only + register-label floor. The baseline clears it because the author selected beats with surface-plausible figurative justification and named the register in the author's note. The lenient pass does not mean the baseline is correct; it means the baseline understood the schema text at a surface level.

---

## PASS 2 — V2 STRICT

Applies full V1 rubric. Per-entry verdict: CORRECT / INCORRECT-{AP-axis} / REFUSE-CORRECT.

Checks per entry:
- Licensing anchor (memory OR feeling cite — mandatory)
- Multi-justification (≥2 layers from {memory, feeling, tens})
- Q1 (adds what proto-line + cited facets don't already carry)
- Q2 (audience-meaningful, transitive via memory-flag co-cite)
- Per-scene cap (≤1 per scene)
- Tens-curve discipline (AP7: tens=3 default-refuse)
- Functional register (callback or dark-humor only)
- Hard fences (no Earth-Bet leak)
- Form rules (one clause, comparator required, single anchor)
- AP-axis violations

---

### Entry 1 — @33 allegory

**Beat context:** proto-line `the door stays shut`. Tensometer: 2 (stakes-visibility). Memory-flag 1 fires: `a closed-door-over-a-failing-tutor is not the first such door her body has stood at`. NI 6 fires: `the threshold holds and what is on the other side stays the size she will not name`. Feeling: none. Sensory: none.

**Licensing anchor check:** No `licensed-by:` field cited. The rubric (§ Schema content-shape revision) proposes this field; the current schema doesn't require it. However, anchor existence is mandatory under the rubric regardless of field notation. The author's note implies memory-flag @33 is the intended anchor. Memory-flag @33 IS a locked upstream fire. Anchor exists in substance if not in notation.

**Multi-justification:** If memory-flag @33 is the anchor (layer 1) and tens=2 at @33 (layer 2), two layers from {memory, feeling, tens} are present. Multi-justification criterion formally met — but only if the baseline author is credited with the implied tens reading. The baseline carries no explicit tens citation. Under strict reading, multi-justification is unverifiable without explicit citation. Flag: multi-justification not demonstrated in entry.

**Q1 — AP4 risk (figurative-already-in-memory):** This is the decisive fault. Memory-flag @33 reads: "a closed-door-over-a-failing-tutor is not the first such door her body has stood at." The comparison structure in the memory-flag is: *this door = one in a series of doors her body has stood at*. The baseline allegory reads: "the door that holds is the shape a closed room takes when the person behind it no longer answers." This restates: *this door = the shape a room-with-an-absent-person takes*. Both entries deploy the door as a figure standing in for historical recurrence and absence. The memory-flag has already done the figurative work (predicative identification of this door with a remembered class of doors + the absent person behind them). The baseline allegory is not adding a new figure — it is paraphrasing the memory-flag's figure with different nouns.

AP4 (figurative-already-in-memory): the memory-flag callback already carries the comparison shape. The baseline restates it.

**AP3 — NI redundancy check:** NI @33: "the threshold holds and what is on the other side stays the size she will not name." The NI entry registers the refusal-to-look at the door's contents. The baseline allegory adds "the person behind it no longer answers" — this names the door's contents (Osmynd's absence / non-response). NI is performing the refusal-to-name. The allegory names what NI refuses to name. This is not strictly AP3 (the allegory is saying something NI omits by design), but it risks inverting NI's register — NI withholds; the allegory fills in. This is a register-tension flag, not a clean AP3 violation. However, under strict Q1: does this entry add what proto-line + memory + NI do not already carry? Memory covers: this-door-as-historical-series. NI covers: threshold-holds + refusal-to-name-the-other-side. The allegory adds: the-person-behind-it-no-longer-answers. This is new information (naming Osmynd's absence directly as content). But the rubric's Q1 asks whether the *figurative move* is new — not whether the factual content is new. The figurative move (door = shape an absent person's room takes) is covered by the memory-flag's own comparative shape. Q1 fails.

**Tens-curve discipline:** tens=2 at @33 (trailing edge of first rupture @24). Per rubric: "tens=2 (pressure): acceptable IF the beat is a trailing-edge of a peak (post-3-cluster) and the metaphor renders the recoil/aftermath." @33 is 9 beats after @24 (the first 3-peak). The 3-cluster is single-beat (@24 only; @23=2, @25=2). @33 is not a trailing edge — it is a return to ambient stakes-visibility well past the peak. AP13 is debatable; tens=2 at @33 is not peak-zone (AP7 not triggered), but it is not "trailing-edge recoil" either. The rubric's tens=2 permission requires "trailing-edge of a peak (post-3-cluster) and the metaphor renders the recoil." @33 does not render recoil from @24; it renders a new stakes-registration event. Tens-zone is marginal for callback use but not a clean AP13 violation. Noted as weak rather than hard-fault.

**Functional register:** The author claims memory callback. Memory-flag @33 is a legitimate anchor; callback register is plausible.

**Hard fences:** No Earth-Bet vocabulary in the entry text. The referent (Osmynd / the failing tutor) is Westerosi. Clean.

**Form:** Single-clause allegory, one anchor implied. The structure "the door that holds is the shape a closed room takes when…" is a compound predicate — "the door… is the shape… when the person… no longer answers." This is multi-clause. Rule: "One clause per entry. Multi-clause metaphors collapse to single clause or refuse." This entry is two-clause (the door is the shape + when the person no longer answers). Form fault under strict reading.

**Verdict: REFUSE-CORRECT — AP4 (figurative-already-in-memory) primary. Secondary: form fault (multi-clause). Supporting: multi-justification not verifiable from entry notation.**

---

### Entry 2 — @64 allegory

**Beat context:** proto-line `the stylus marks two parallel lines beside taylor's entry`. Tensometer: 3 (peak — stakes-visibility + reversal-proximity; the bureaucratic determination). Memory-flag: none at @64. Feeling-flag: none at @64. NI 17: `two strokes; the determination is on the record and on her`. Sensory: none at @64.

**Licensing anchor check:** No memory-flag or feeling-flag fires at @64. Memory-flags: @33, @52, @73. Feeling-flags: @6, @39, @57, @73. @64 is in neither set. There is **no anchor** available at @64. The baseline has no licensed anchor to cite.

AP1 (unlicensed novel figuration): this is the dominant fault. The metaphor-eligible-beat union is memory ∪ feeling = {6, 33, 39, 52, 57, 73}. @64 is not in this set. No anchor exists. The baseline's author's note does not claim a memory or feeling anchor — it implicitly relies on tens=3 (the dramatic weight) and the state-update (irreversible registration). But tens alone is support, not anchor; and state-update does not license metaphor (rubric §Cross-facet contract: "State-updates does not license metaphor").

**AP7 — peak-zone fire:** @64 is tens=3. Rubric: "tens=3 (peak): default refuse. Figurative reach during rupture is anti-form." The exception is "dark-humor metaphor at peak that deflates the rupture." The author's note claims dark humor: "the ledger's pre-judicial authority… The marks arrive as if the record already contained her outcome and is merely confirming it. The tone is grim and slightly sardonic." This is the only possible exception path. However: the dark-humor exception still requires an anchor from {memory, feeling}. There is no feeling-flag at @64 and no memory-flag at @64. The dark-humor register is claimed but structurally unanchored. AP7 stands; AP1 is a pre-condition fault (no anchor is available to license even the exception).

**Q2 (audience-meaningful, transitive via memory-flag co-cite):** Q2 is transitive from memory-flag. There is no memory-flag at @64 to inherit from. Q2 cannot be satisfied.

**Multi-justification:** Memory or feeling anchor = zero layers. Multi-justification requires ≥2 layers from {memory, feeling, tens}. Zero memory + zero feeling = fails before tens contributes.

**Form:** The entry uses an em-dash construction: "two parallel lines — the mark a ledger makes when it has already decided and wants you to know it knew before you asked." This is not a clean allegory form. Rubric: "allegory must contain a structural correspondence operator." The em-dash parataxis does not constitute a structural correspondence operator; it is elaboration, not correspondence. The comparator is absent or extremely weak. Form is marginal to fail.

Additionally: "wants you to know it knew before you asked" attributes will and foreknowledge to the ledger. This is personification-of-administrative-record, not allegory. Under Reading A: allegory requires "structural multi-element correspondence collapsed to a single figure." There is no multi-element structural correspondence here — only a single-noun personification extended through a weak parataxis. This fails the Reading A allegory definition.

**Hard fences:** No Earth-Bet vocabulary in the text. Clean on that axis.

**Voice register:** The entry "wants you to know it knew before you asked" has an informal-address register ("you") that breaks Taylor's behavior pack. Taylor's pack is close-third-person with Westerosi overlay; the direct-address "you" is not in that register. AP6 (voice-register mismatch) applies.

**Verdict: REFUSE-CORRECT — AP1 (no anchor; @64 not in eligible-beat union) primary. AP7 (tens=3 peak; no licensed exception) secondary. AP6 (voice-register informal-address break) tertiary. Supporting: form fail (no structural correspondence operator; Reading A allegory definition not met); Q2 fails (no memory-flag anchor to inherit from).**

---

### Entry 3 — @73 simile

**Beat context:** proto-line `taylor steps into the shadow of the frame`. Tensometer: 1 (quiet). Memory-flag 3 fires: `a threshold whose far side does not yield is not a new shape for her body -> (earth-bet: locker-displacement)`. Feeling-flag 4 fires: `taylor-hebert-westeros: her breath empties between one step and the next | expressed: no`. NI 19: `the frame's shadow takes her and what is on its other side stays the size it has been`. Sensory: @72 adjacent (tactile, distinct beat).

**Licensing anchor check:** Memory-flag @73 is a locked upstream fire. Feeling-flag @73 is a locked upstream fire. Double-anchor available. This is the strongest anchor set in the file (calibration anchor C3: FIRE expected).

**Multi-justification:** Memory anchor (layer 1) + feeling anchor (layer 2) + tens=1 (layer 3). Three layers from {memory, feeling, tens}. Multi-justification: passes with maximum available signal. The baseline entry does not cite these explicitly (no `licensed-by:` notation), but the anchors exist in the locked files and the beat matches.

**Q1 — AP4 / AP3 / AP2 risk check:**

The memory-flag @73 reads: "a threshold whose far side does not yield is not a new shape for her body." The figurative move in the memory-flag is: *this threshold = one in a historical series of non-yielding thresholds*. The shape-metaphor is the memory-flag's own figure.

The NI @73 reads: "the frame's shadow takes her and what is on its other side stays the size it has been." NI deploys environmental-agency idiom ("takes her") — Reading B, not Reading A. Per rubric: this is out of scope for metaphor. AP3 (figurative-already-in-NI) applies only to Reading A figures; NI's environmental-agency idiom does not preclude a new Reading A metaphor at @73 provided the new metaphor adds a different figure.

The proto-line reads: "taylor steps into the shadow of the frame." The shadow and the frame are present as physical description. The proto-line is not figurative (it is a spatial-entry description).

The feeling-flag reads: "her breath empties between one step and the next | expressed: no." The somatic register is breath-as-interior-cost. The feeling-flag does not deploy a Reading A figure.

The baseline simile: "the shadow of the frame takes her the way a threshold takes a body that has stood at one before and knows what is on the other side does not open toward her."

The comparator "the way" is present (simile form). The comparison is: *this shadow-taking = the way a threshold takes a body that has stood at one before.* This is a simile comparing the shadow-entry act to a threshold-crossing act. The figure being added is: the shadow-as-threshold (environmental experience = threshold-body-memory). The memory-flag adds: *this threshold = not-a-new-shape.* The simile adds: *this shadow-taking = the way a threshold takes a body that already knows.* These are close but not identical — the simile adds the *quality of the threshold-experience* (the body already knows; the other side does not open toward her) as the figure, whereas the memory-flag names the historical series.

However: the memory-flag's text "is not a new shape for her body" is structural shorthand for "her body knows this." The simile's content "a body that has stood at one before and knows what is on the other side does not open toward her" is a verbal expansion of "is not a new shape for her body." The figurative content is the same knowledge-of-threshold expressed in different words. This is AP4 — figurative-already-in-memory, restated not extended.

Additionally: "the frame's shadow takes her" appears in NI @73 as "the frame's shadow takes her." The baseline simile opens with "the shadow of the frame takes her the way…" — it directly lifts the NI's agency-idiom opening ("shadow takes her") and extends it with a simile. The NI is Reading B (environmental-agency idiom, out-of-scope for metaphor). The baseline takes that Reading B idiom and extends it into a Reading A simile by attaching the comparator. This is a borderline AP3 case: the baseline is not simply restating NI, but it is taking NI's figurative opening as the base and extending it. Q1 asks whether the metaphor adds what NI doesn't carry. NI says: "shadow takes her + other side stays the size." The simile adds: "the way a threshold takes a body that has stood at one before." The addition is the historical-repetition figure — which the memory-flag already provides.

**AP4 verdict:** The body-knowledge / historical-repetition figure is the memory-flag's core contribution. The simile restates it. AP4 applies.

**AP3 verdict:** The simile lifts NI's opening idiom ("shadow takes her") into its comparandum. The simile's new content (what it adds beyond NI) is the historical-repetition figure — which goes to AP4, not AP3. AP3 is a secondary flag here, not a hard fault on its own.

**Form check:** Simile comparator "the way" is present. Single-clause requirement: "the shadow of the frame takes her the way a threshold takes a body that has stood at one before and knows what is on the other side does not open toward her." This is syntactically a single comparative clause (A takes her the way B takes a body). The subordinate clause "that has stood at one before and knows what is on the other side does not open toward her" is embedded in the comparandum, not a second comparator. Form: single comparator, one comparison. Passes form.

Hard fences: "locker-displacement" (the memory-flag's earth-bet gloss) does not appear in the entry text. "body that has stood at one before" is Westerosi-compatible body-history register. Clean.

**Voice register:** "the way a threshold takes a body that has stood at one before and knows what is on the other side does not open toward her" — this is close-third, past-behavioral register. The phrase "knows what is on the other side does not open toward her" is Taylor's cognitive style (anticipatory cost-accounting) rendered figuratively. Taylor's behavior pack supports this register. Passes AP6.

**Tens discipline:** tens=1 at @73. Quiet zone — strong candidate per rubric. AP7 not triggered. AP13 not triggered.

**Functional register:** Memory callback. Memory-flag @73 is the callback anchor. Functional register satisfied.

**Q2:** Q2 is transitive from memory-flag co-cite. Memory-flag @73 is locked and passed audience-meaningful at Phase 5 (100% final). Q2 inherited. Satisfied.

**Overall Q1 decision for @73:** The dominant fault is AP4 — the simile's figurative content (body that has stood at one before + other side does not open toward her) is a restatement of the memory-flag's own figure ("is not a new shape for her body"). The corpus note at C3 identifies this risk: "the figure to add must be one the memory's own gloss does not deploy." The memory's gloss deploys exactly the shape-recurrence / body-knowledge figure. The simile must take a step beyond — "e.g., compress the flagstone-figure with a different comparison shape, or render the recognition as figurative move the proto-line + memory gloss + NI + feeling individually don't carry." The corpus specifically flags breath-as-figure as the best-form candidate at @73 (since feeling-flag's somatic register and memory-flag's body-shape register intersect through breath). The baseline simile ignores the breath register entirely and lands on the same threshold-body-knowledge figure the memory-flag already deploys. The form is correct; the content fails Q1.

**Verdict: REFUSE-CORRECT — AP4 (figurative-already-in-memory; simile restates the memory-flag's body-knowledge/threshold-recurrence figure rather than adding a new comparison shape) primary. Secondary AP3 flag (comparandum lifted from NI's environmental-agency opening). The correct fire at @73 exists and should be recovered — this entry's form is right but its figure duplicates the upstream anchor.**

---

## STRICT PASS SUMMARY

| Entry | Beat | V2 Verdict | Primary fault | Secondary faults |
|---|---|---|---|---|
| 1 | @33 | REFUSE-CORRECT | AP4 (memory figure restated) | Form: multi-clause; multi-justification not verifiable |
| 2 | @64 | REFUSE-CORRECT | AP1 (no anchor; not in eligible-beat union) | AP7 (tens=3 peak); AP6 (voice-register); form fail (no structural correspondence) |
| 3 | @73 | REFUSE-CORRECT | AP4 (simile restates memory-flag's body-knowledge figure) | AP3 flag (comparandum lifted from NI) |

**Strict accept rate: 0/3 (0%) — this is the baseline-to-beat for Phase 2.**

---

## SKIP ANALYSIS

### Non-fired beats from eligible union

The eligible-beat union is @6, @33, @39, @52, @57, @73. Baseline fired at @33 and @73 (refused above) and @64 (outside eligible union). Baseline explicitly declined @52, @38-@39. Baseline did not address @6 or @57.

### @6 (mira straightens — Scene A)

Calibration anchor C4: REFUSE expected.
Baseline: no fire, no mention.
AP risk: AP12 (non-POV interior — editor doesn't have mira's interior); AP9 (no callback potential; mira's introducing-register; no monument cite available); functional-register fail (mira's eyes-find-door is establishing, not callback or dark humor).
Corpus verdict: REFUSE expected. Non-POV + no callback + functional-register fail.

**Skip verdict: SKIP-CORRECT** — the baseline was right not to fire here, though not for explicitly stated reasons.

### @33 (the door stays shut — Scene B)

Baseline fired and was refused (AP4). Calibration anchor: corpus says REFUSE on AP4 + AP3 (memory + NI together cover the figurative ground). The corpus expected this to be a refuse-correct beat.

**Skip verdict: not applicable** — baseline fired; entry was refuse-correct. Consistent with corpus expectation (refuse expected per AP4+AP3).

### @39 (taylor sets her feet — Scene B)

Calibration anchor C1: REFUSE expected (AP7 tens=3 peak + AP5 cape-fence + no memory anchor).
Baseline explicitly declined @38-@39: "The confrontation peak is most powerful flat."
The decline reason is aesthetic ("most powerful flat") not rubric-correct. But the outcome is correct — @39 should be refused. The rubric reason is: no memory anchor (AP1 pre-condition), tens=3 (AP7), cape-fence risk (AP5).

**Skip verdict: SKIP-CORRECT** — correct outcome; rubric-blind rationale (aesthetic) not rubric-correct, but decline is right.

### @52 (mira drops her eyes — Scene C)

Calibration anchor C2: FIRE-OR-REFUSE (strongest secondary candidate; memory anchor + tens=1 + callback; AP4 borderline).
Baseline explicitly declined @52: "A metaphor entry would be redundant — the proto-line IS the simile."
Rubric analysis: Memory-flag @52 reads: "a peer's eyes-down beside her under adult attention is a flagstone she has stood beside before." The memory-flag deploys a comparison (eyes-down-peer = flagstone-stood-beside-before). NI @52: "mira's eyes are on the flagstones and the count of allies in the yard drops to one." The proto-line: "mira drops her eyes to the flagstones." The corpus notes the AP4 borderline: "the memory's own gloss does not deploy" — the memory-flag's figure is "is a flagstone she has stood beside before" (predicative simile-equivalent). A metaphor at @52 must take a step beyond. The corpus suggested: "compress the flagstone-figure with a different comparison shape, or render the recognition as figurative move the proto-line + memory gloss + NI count don't carry."

The baseline's decline reason ("the proto-line IS the simile") is not rubric-correct as stated (the proto-line is "mira drops her eyes to the flagstones" — no comparator, no simile). The baseline's author seems to be reading the memory-flag as the comparison, not the proto-line. The underlying intuition (that the figurative ground is already covered) is consistent with AP4 risk at this beat, but the stated reasoning is wrong.

Is @52 a SKIP-MISSED? The corpus calibration anchor C2 says FIRE-OR-REFUSE — meaning the corpus itself was uncertain. The corpus notes AP4 is "borderline." The rubric standard is: a fire at @52 would need to add a figure the memory-flag doesn't carry. The memory-flag's figure is flagstone-as-prior-betrayal-site. A correctly authored @52 fire could render, for example, the recoil/recognition as a different comparison shape (not threshold or flagstone) — but the constraint landscape is tight (memory already figurative, NI covers the count-drop). The ruling: @52 was correctly declined in outcome given AP4 risk, but the corpus allowed for a possible fire with the right figure. The baseline's decision (decline) aligns with the rubric's REFUSE branch of C2. This is borderline.

**Skip verdict: SKIP-CORRECT (marginal)** — the correct outcome given AP4 risk is defensible; a correctly authored entry could potentially clear @52, but the rubric's AP4 risk is real and the baseline's decline (even for wrong reasons) is not a miss that Phase 2 must recover.

### @57 (edric steps back — Scene C)

Calibration anchor: REFUSE expected (AP12 non-POV + AP2 proto-line/NI already personify door + AP3 NI personifies door-as-cover-thief; functional-register fail — no memory anchor).
Baseline: no fire, no mention.

**Skip verdict: SKIP-CORRECT** — correct not to fire. AP12 + AP2 + AP3 + functional-register fail.

### @73 (taylor steps into the shadow of the frame — Scene D)

Baseline fired and was refused (AP4). Calibration anchor C3: FIRE expected (strongest single fire; triple-anchor + tens=1 quiet + callback + Q1+Q2 clear). The corpus identified the best-form figure as breath-as-figure, fusing threshold + breath into a comparison the proto-line + memory + NI + feeling individually don't carry. The baseline ignored the breath register and re-deployed the threshold-body-knowledge figure already in the memory-flag.

**Skip verdict: SKIP-MISSED** — @73 should fire; the baseline produced a fire at this beat but the entry is refuse-correct on AP4. A correctly authored @73 entry exists (breath-fused threshold comparison). Phase 2 must recover this fire with a new figure.

---

## SKIP ANALYSIS SUMMARY

| Beat | Status | Verdict |
|---|---|---|
| @6 | No fire | SKIP-CORRECT |
| @33 | Fired / refused | REFUSE-CORRECT (AP4; consistent with corpus REFUSE expectation) |
| @39 | No fire | SKIP-CORRECT (outcome correct; rubric-blind rationale aesthetic only) |
| @52 | No fire | SKIP-CORRECT (marginal; AP4 risk real; C2 was FIRE-OR-REFUSE) |
| @57 | No fire | SKIP-CORRECT |
| @73 | Fired / refused | REFUSE-CORRECT (AP4); **SKIP-MISSED** — correctly licensed beat; wrong figure chosen |

---

## FILE-SHAPE VERDICT

### Sparsity

3 fires on 77 beats = 3.9%. Rubric requires ≤2 fires on 77 beats (0-3%; ≤2 fires). 3 fires = **SHAPE-FAIL** — 1 fire over the hard cap. Even if all three entries were correct, the file would violate sparsity.

Note: all three entries are refused under strict rubric, so the sparsity violation is moot for the corrected file. Phase 2 file should fire 1 fire maximum (the @73 recovery, with possible @52 conditional) to hold within the ≤2 sparsity ceiling. The per-scene cap also applies.

### Per-scene cap

Scene A (@1-@22): 0 fires. OK.
Scene B (@23-@48): 1 fire (@33 attempted). If @33 is corrected to no-fire, Scene B = 0. Current baseline: 1. Cap: ≤1. Cap honored in Scene B.
Scene C (@49-@67): 1 fire (@64 attempted). If @64 is corrected to no-fire, Scene C = 0. Current baseline: 1. Cap: ≤1. Cap honored in Scene C. However @64 is outside the eligible-beat union entirely; this was a scene-cap non-issue since the fire should not exist.
Scene D (@68-@77): 1 fire (@73 attempted). If @73 is revised to the correct figure, Scene D = 1. Cap: ≤1. Cap would be honored.

Per-scene cap: **SHAPE-OK on current distribution** (no scene has >1 fire); **SHAPE-FAIL on sparsity** (3 total fires > ≤2 ceiling).

### Schema content-shape

The baseline uses `<id> @<pid> <kind>: <text>` format — current schema format. The proposed format adds `| licensed-by: <anchor> [+<support> ...]`. The baseline has no `licensed-by:` field on any entry. As the rubric notes: "current schema accepts simpler shape; rubric proposes `licensed-by:` field." Under current schema, the baseline format is technically schema-conforming. The licensing is not verifiable from entry notation alone.

Schema content-shape: **SHAPE-OK under current schema** (proposed `licensed-by:` field is schema-revision-pending-Phase-5; not yet required). However, this validates the rubric's case for shipping the revision: the lack of `licensed-by:` notation meant licensing could only be verified by cross-file lookup — and when that lookup was done, two of the three entries failed on AP1 (no anchor) or AP4 (anchor restated).

---

## SYSTEMIC FAULTS (baseline failure modes)

Six named:

**1. AP4-dominance across all fired beats.** Both @33 and @73 fail on AP4 — figurative-already-in-memory. The editor, writing rubric-blind, found the memory-flag gloss and used it as the model for the metaphor. The result is the metaphor mirrors the upstream anchor rather than extending it. This is the most likely baseline failure mode for any capstone facet: the anchor is the resource the editor reads first and the content of the anchor becomes the content of the metaphor. Rubric's Q1 requirement and explicit AP4 definition exist precisely to counter this.

**2. AP1 at @64 — out-of-eligible-union fire.** @64 is tens=3, no memory anchor, no feeling anchor. The editor fired at the tensometer's dramatic peak without consulting the eligible-beat union. This is the expected baseline contamination pattern (corpus §Anti-corpus: "Peak beats: @24, @38, @64 — these are tens=3 peaks with strong dramatic surface; rubric forbids per AP7"). The baseline contaminated at exactly the anti-corpus-predicted peak.

**3. AP7 compounding AP1 at @64.** Not only does @64 lack an anchor (AP1), it is tens=3 (AP7 default-refuse). The editor's author's note attempts to invoke the dark-humor exception, but the exception requires a feeling-flag anchor that doesn't exist at @64. Both faults are structural — the beat is outside the eligible union and in the peak zone.

**4. Licensing not verifiable from entry notation.** No `licensed-by:` field in any entry. Cross-file lookup was required to determine that @64 has no anchor, that @33's anchor is already figurative, and that @73's anchor shares the comparison shape. The proposed schema field would have made these faults visible at authoring time.

**5. No breath-figure at @73.** The strongest single fire in the episode has a correctly identified anchor set but the wrong figure. The corpus explicitly named breath-as-figure as the best-form candidate: "render the recognition as figurative move the proto-line + memory gloss + NI + feeling individually don't carry." Feeling-flag @73 fires on breath ("her breath empties between one step and the next | expressed: no"). The baseline simile ignores breath entirely and re-deploys threshold-body-knowledge — which is the memory-flag's figure. The figurative ground that is genuinely open at @73 (the breath-threshold fusion) was left unworked.

**6. Multi-clause form fault at @33.** The baseline produces a two-clause allegory at @33 ("the door that holds is the shape… when the person behind it no longer answers") where the rubric requires single-clause entries. The editor produced extended figuration under conditions where the rubric requires compression. This is symptomatic of rubric-blind authoring: the editor extended the figure to "complete" the statement rather than collapsing to single clause.

---

## FLOOR-DEFENSE CHECK

Are any of these refusals genuinely defensible by the entry?

**@33:** Author's note argues the allegory earns figurative reach because "the memory callback licenses it." This is partially correct — the memory-flag @33 is a legitimate anchor, and the functional register (callback) is correct. The defense fails only at Q1: the entry restates the memory-flag's figure rather than adding a new one. This is not a soft ruling — AP4 is one of the rubric's most explicit anti-patterns. Defense does not earn a pass; AP4 stands.

**@64:** The dark-humor claim is the entry's defense. Dark humor is a legitimate register. However: the rubric's dark-humor exception to AP7 still requires a feeling-flag anchor at the beat. There is no feeling-flag at @64. The author's note says the tone is "grim and slightly sardonic" — this is a prose description of tone, not a licensed structural register per the rubric. The defense does not create an anchor from thin air. AP1 stands; AP7 stands. No rubric-pushback warranted.

**@73:** The entry correctly identifies the beat (calibration anchor C3: FIRE expected) and the simile form is correct. The author's note says "the simile earns the fire because 'the shadow takes her' is already partway figurative in the proto-line." This is the wrong argument — the proto-line's "shadow of the frame" is spatial description, not figurative. The defense also claims the simile "completes the gesture rather than adding decoration." But the gesture it completes is the NI's environmental-agency idiom ("shadow takes her"), which is Reading B. Completing a Reading B idiom by extension is not a Reading A metaphor entry. The defense is structurally wrong about what it's doing. AP4 stands; this entry needs a new figure, not a defense.

No refusals are overturned by floor-defense. The rubric stands locked.

---

## COMBINED RESULTS

| Phase | Rate | Notes |
|---|---|---|
| V1 lenient | 3/3 (100%) | Form + register-label floor only; expected |
| V2 strict | 0/3 (0%) | All three entries refuse-correct |
| SKIP-MISSED | 1 (@73) | Correctly licensed beat; wrong figure |
| SKIP-CORRECT | 4 (@6, @39, @52 marginal, @57) | Correct non-fires |
| Sparsity | SHAPE-FAIL | 3 fires > ≤2 ceiling |
| Per-scene cap | SHAPE-OK | No scene exceeded ≤1 |
| Schema | SHAPE-OK (current) | Proposed `licensed-by:` field not yet required; absence validated the case for shipping it |

**Baseline-to-beat for Phase 2: 0/3 (0%) strict.**

Phase 2 target: recover the @73 SKIP-MISSED fire with a breath-fused figure that clears AP4, passes Q1 (adds what memory + NI + feeling + proto-line do not carry individually), and holds within ≤2 sparsity ceiling. Optional: evaluate @52 for a correctly authored entry if the figure available there can clear AP4 without duplicating the memory-flag's flagstone-recurrence shape.
