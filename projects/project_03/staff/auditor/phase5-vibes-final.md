---
audit:
  scope: episode
  target: s01e01 / vibes-updates facet / Phase 5 final adjudication
  timestamp: 2026-05-07
  reviewer: mechanic-auditor
  rubric: design/shoot-v2/rubric-vibes.md (V1 LOCKED) + design/shoot-v2/rubric-vibes-v1.1-patch.md (V1.1 patch, ships same commit)
  phase4-output: design/shoot-v2/phase4-vibes-revised.md (12 entries)
  phase2-audit: active-project/staff/auditor/phase2-vibes-audit.md
  phase3-seams: active-project/staff/auditor/phase3-vibes-seams.md
  vibe-clouds-verified:
    - active-project/actors/taylor-hebert-westeros/vibes.md
    - active-project/actors/mira-stonefield/vibes.md
    - active-project/actors/edric-cray/vibes.md
    - active-project/actors/census-officer/vibes.md
    - active-project/actors/septon-dying-protector/vibes.md
    - active-project/staff/studio/vibes.md
    - active-project/warehouse/loc-harrenhal-sept-environs.card.md
  upstream-locked-verified:
    - active-project/theater/facets/state-updates.md
    - active-project/theater/facets/memory.md
    - active-project/theater/facets/feeling.md
    - active-project/theater/facets/metaphor.md
---

# Phase 5 Vibes-Updates — Final Adjudication (s01e01)

---

## 1. Per-fire verdicts (12 entries)

Entries are reviewed in the final ascending order shown in Phase 4's entry list. Rubric applied: V1 LOCKED + V1.1 patch.

---

### Entry 1 — `@6 actor:mira-stonefield ++ the-yard-as-witness`
**Tokens:** `[the-door-already-marked-before-the-ask, exit-located-before-the-weight-arrived]`
**Licensed-by:** `feeling:1, proto:6, proto:51`

**Verdict: CORRECT**

Gate 1: `actor:mira-stonefield` confirmed in active-project actors. PASS.
Gate 2: `mira-stonefield/vibes.md` carries `the-yard-as-witness: [the-ask-that-came-to-her, the-yard-stones-she-looked-at, the-officer-still-present-when-she-said-nothing, the-cost-she-assessed-before-she-decided, self-preservation-in-a-hierarchical-world]`. Keyword present. `++` is the correct op. PASS.
AP11 (string-overlap formal gate): `the-door-already-marked-before-the-ask` and `exit-located-before-the-weight-arrived` — no string overlap with existing bundle. PASS.
AP8 sentence-parsability: both tokens are 5-6 segments; noun-phrase compressions. Neither parses as a complete sentence with standalone subject+finite-verb+object. PASS under V1.1 patch formal test.
Gate 4 (licensed-by): `feeling:1` is confirmed in locked `feeling.md` at @6 (`mira-stonefield: her eyes find the door before they find the wards | expressed: partial`). `proto:6` and `proto:51` are on-screen beats. All sources resolve. PASS.
Gate 5 (permanence): pre-positioning orientation is a durable character trait (not transient mood). PASS.
Gate 6 (operator-bias actionability): biases dialogue-writer on Mira's situational-awareness register; behavior-pack for proactive-threat-orientation vs reactive-self-preservation (distinct from the existing decision-moment framing). Distinct downstream behavior. PASS.
AP1 (transient-as-vibe): not transient — a door-orientation reflex established at episode open persists as behavioral baseline. PASS.
AP13 press: tokens are compressed noun-phrases, not narrator prose. PASS.

Semantic adjacency advisory (V1.1 AP11 advisory): `self-preservation-in-a-hierarchical-world` (existing) and `exit-located-before-the-weight-arrived` (new) are in adjacent registers. Event-frame distinction: existing bundle encodes the decision-under-pressure moment (E5); new tokens encode the pre-decision orientation established 45 beats earlier. Operator would generate different bias: existing bundle → Mira as someone who calculates under pressure; new tokens → Mira as someone who orients BEFORE pressure arrives. Distinct. Advisory satisfied.

---

### Entry 2 — `@11 loc:harrenhal-sept-environs + the-machinery-arrives`
**Tokens:** `[the-space-that-makes-smallfolk-legible, authority-day-contracted-into-two-body-lengths, the-ground-where-the-lord-collects, the-yard-that-cannot-claim-ignorance]`
**Licensed-by:** `proto:11, proto:12, proto:13, world-build:smallfolk-common-authority-day-function`

**Verdict: CORRECT**

Gate 1: `loc:harrenhal-sept-environs` confirmed in `active-project/warehouse/loc-harrenhal-sept-environs.card.md`. Card carries NO VIBES section — empty vibe-set confirmed by direct file inspection. PASS.
Gate 2: keyword absent from empty vibe-set. `+` is the correct op. PASS.
AP8/AP13: All four tokens are noun-phrase word-algebra. Longest is `the-yard-that-cannot-claim-ignorance` (7 segments; noun-phrase with relative clause; not sentential). PASS under V1.1 AP8 formal test.
Gate 4: proto references are on-screen beats. `world-build:smallfolk-common-authority-day-function` gloss matches the location card's Movement/authority-day section explicitly. PASS.
Gate 6: biases studio environmental palette (the sept yard as authority-day collection space); sensory-flag selection on the location; NI interest-pattern for authority-day scenes. Actionable. PASS.
AP9: entity-target (loc) preferred over episode-scope — correct placement. PASS.
Gate 7 (fan-out): the E1 event affects the location as its physical site; including the location in the fan-out satisfies entity-preference under AP9. The episode-scope `++` in entry 9 adds a departure-register not carried by this loc entry; no scope duplication. PASS.

Note on loc-name discrepancy: Phase 2 entry 7 referenced `loc:westerosi-smallfolk-village-common` (correctly); Phase 4 renamed the target to `loc:harrenhal-sept-environs` to match the actual warehouse card slug. Slug `loc:harrenhal-sept-environs` is the correct target and is confirmed in the warehouse. PASS.

---

### Entry 3 — `@33 actor:septon-dying-protector + the-septon-as-absence`
**Tokens:** `[present-but-cannot-appear, the-protector-who-cannot-act, the-letter-in-place-of-the-body, kindness-that-runs-out-before-it-can-hold]`
**Licensed-by:** `proto:32, proto:33, canon:osmynd-bedridden-pre-episode`

**Verdict: CORRECT**

Gate 1: `actor:septon-dying-protector` confirmed in active-project. PASS.
Gate 2: `septon-dying-protector/vibes.md` carries `dying`, `protection`, `kindness`, `ward`, `the-septon-failing`, `observer-arriving`. Keyword `the-septon-as-absence` is absent. `+` is the correct op. PASS.
AP8: all tokens are noun-phrase word-algebra. `kindness-that-runs-out-before-it-can-hold` (8 segments) — noun-phrase with participial temporal clause; no standalone main predicate. V1.1 AP8 sentence-parsability test: "kindness that runs out before it can hold" does not parse as a complete standalone sentence (no subject+finite-verb+object; it lacks a governing predicate — the noun "kindness" is the head, "that runs out" is a relative clause, "before it can hold" is an adverbial modifier). PASS.
Gate 4: `proto:32, proto:33` are on-screen beats (officer addresses threshold; door stays shut). `canon:osmynd-bedridden-pre-episode` is confirmed in the location card's Hazards section ("The septon's death is anticipated") and the actor card's VIBES keyword `dying`. PASS.
Gate 5: absence-as-completed-event is permanent (the door staying shut is the defining moment of the septon's inability to act; it persists as a durable qualitative fact). PASS.
Gate 6: biases dialogue-writer fork on completed-absence register (distinct from the ongoing-decline `the-septon-failing` keyword); behavior-pack for the absent-actor archetype. PASS.
AP2: token content is qualitative-consequence layer (the completed failure to appear), not a restatement of state-updates fact. State-updates has no entry for the door-staying-shut (non-event). AP2 PASS.

---

### Entry 4 — `@33 loc:harrenhal-sept-environs + the-septon-as-absence`
**Tokens:** `[the-space-where-the-door-stayed-shut, the-building-whose-occupant-cannot-reach-its-threshold, charged-ground-for-what-did-not-emerge]`
**Licensed-by:** `proto:32, proto:33, canon:osmynd-bedridden-pre-episode`

**Verdict: CORRECT**

Gate 1: `loc:harrenhal-sept-environs` confirmed; vibe-set was empty at episode open (no VIBES section in card); first add for `the-machinery-arrives` is entry 2 in this file. By episode-internal ordering, `the-septon-as-absence` is the second keyword added to this location in this episode's facet authoring. The vibe-set does not contain `the-septon-as-absence` at the time of this authoring pass. `+` is the correct op. PASS.

NOTE: Both entries 2 and 4 target `loc:harrenhal-sept-environs` with `+` ops. Entries 2 and 4 add DIFFERENT keywords (`the-machinery-arrives` and `the-septon-as-absence` respectively). Gate 2 checks whether the SPECIFIC KEYWORD is present — each keyword is fresh to the empty starting state. No AP5 conflict. PASS.

AP8: `the-building-whose-occupant-cannot-reach-its-threshold` (8 segments) — noun-phrase with relative clause. Sentence-parsability test: "the building whose occupant cannot reach its threshold" lacks a main predicate (it is a noun-phrase with an embedded relative clause). PASS. `charged-ground-for-what-did-not-emerge` (6 segments) — noun-phrase with prepositional modifier containing a relative clause. Not sentential. PASS.
Gate 4: `proto:32, proto:33` on-screen anchors; `canon:osmynd-bedridden-pre-episode` resolves via location card and septon actor card. PASS.
Gate 6: biases studio environmental palette for the sept interior (the charged-absence quality for Taylor's @77 entry); sensory-flag selection on the sept; behavior-pack for Taylor's approach/enter sequence at @70–@77. Actionable. PASS.
AP2: tokens are qualitative-consequence layer (the space's charged quality), not restatement of state-updates. State-updates:12 fires the sublocation change AT @77 (not at @33); no AP2 conflict. PASS.
AP9: entity-target (loc) is correctly preferred over episode-scope for this location-bound consequence. PASS.

---

### Entry 5 — `@57 actor:edric-cray ++ the-yard-as-witness`
**Tokens:** `[the-sept-interior-as-exit-destination, sublocation-confirmed-not-returned]`
**Licensed-by:** `state-update:9, proto:55, proto:57`

**Verdict: CORRECT**

Gate 1: `actor:edric-cray` confirmed. PASS.
Gate 2: `edric-cray/vibes.md` carries `the-yard-as-witness: [the-officer-at-the-gate, the-look-he-gave-the-officer-then-taylor, the-door-he-stepped-back-through, the-math-he-ran-before-he-moved, one-exit-and-he-used-it]`. Keyword present. `++` is the correct op. PASS.
AP11 (string-overlap): `the-sept-interior-as-exit-destination` and `sublocation-confirmed-not-returned` — no string overlap with existing bundle. PASS.
AP8: both tokens are short (4-5 segments after decomposition). `the-sept-interior-as-exit-destination` (5 segments, hyphenated) = noun-phrase + as-predicate compression. `sublocation-confirmed-not-returned` (4 segments) = compressed participial. PASS.
Gate 4: `state-update:9` confirmed in locked `state-updates.md` at @57 (`actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)`). `proto:55` and `proto:57` are on-screen beats. PASS.
Gate 6: biases dialogue-writer on Edric's s01e02-open sublocation register (inside the sept vs merely absent from yard); behavior-pack for confirmed-exit vs anticipated-exit. Distinct from existing `one-exit-and-he-used-it` (conceptual) — this adds the mechanically-confirmed-spatial register. PASS.
AP2: `the-door-he-stepped-back-through` (existing) encodes the conceptual exit; new tokens encode the sublocation-confirmation from state-update:9. These are qualitative-consequence of the state change, not restatement of it. PASS.

Semantic adjacency (V1.1 advisory): `one-exit-and-he-used-it` (pre-load) vs `sublocation-confirmed-not-returned` (new). Event-frames: pre-load = anticipated-exit as cognitive calculation result; new tokens = mechanically-confirmed sublocation as write-back of state. Distinct: the pre-load captures intentionality; the new tokens capture the canonical consequence. Advisory satisfied.

---

### Entry 6 — `@57 episode ++ the-yard-as-witness`
**Tokens:** `[the-refusal-with-the-officer-watching, edric-after-the-gate-cleared]`
**Licensed-by:** `feeling:1, feeling:3, proto:52, proto:57`

**Verdict: CORRECT**

Gate 2 (episode scope): `studio/vibes.md` EPISODE_1_VIBES carries `the-yard-as-witness: [mira-delivering-verdict-before-it-happens, edric-watching-the-road-without-watching, what-everyone-already-knew]`. Keyword present. `++` is the correct op under V1.1 patch (pre-seeded project; pre-loaded = present; `++` required). PASS.
AP11 (string-overlap): `the-refusal-with-the-officer-watching` and `edric-after-the-gate-cleared` — no string overlap with existing pre-loaded bundle. PASS.
AP8: both tokens are 4-5 segments. Not sentential. PASS.
Gate 4: `feeling:1` confirmed in locked `feeling.md` at @6 (Mira's tell); `feeling:3` confirmed at @57 (Edric's tell). `proto:52` and `proto:57` are on-screen spatial-sequence beats. PASS.
Gate 6: biases ambient episode register toward the witnessed-social-hierarchy sub-dimension; distinct from the pre-loaded inevitability register (`mira-delivering-verdict-before-it-happens`). PASS.
AP9 audit: this is an episode-scope `++` on an episode-scope pre-loaded keyword. The pre-loaded bundle covers ambient framing; the new tokens add a spatial-sequence-under-observation register that the entity-target entries (entry 1 = mira; entry 5 = edric) do not carry in episode-scope form. AP9 is not triggered (no entity-target available for the spatial-sequencing-of-both-characters register simultaneously; the episode-scope is the correct scope for the cross-actor sequential framing). PASS.

---

### Entry 7 — `@64 actor:taylor-hebert-westeros ++ the-machinery-arrives`
**Tokens:** `[the-marks-beside-her-name-invisible-to-her, the-notation-the-machine-added-without-her-knowledge]`
**Licensed-by:** `state-update:10, state-update:11, proto:64`

**Verdict: CORRECT**

Gate 2: `taylor-hebert-westeros/vibes.md` carries `the-machinery-arrives: [the-officer-as-instrument-not-enemy, forms-have-no-slot-for-her-situation, the-refusal-that-requires-no-malice, bureaucratic-weight-she-cannot-argue-with]`. Keyword present. `++` is the correct op. PASS.
AP11 (string-overlap): no overlap with existing bundle. PASS.
AP8 sentence-parsability (V1.1 formal test):
  - `the-marks-beside-her-name-invisible-to-her` (8 segments): noun-phrase (`the marks`) + locative (`beside her name`) + participial modifier (`invisible to her`). "The marks beside her name invisible to her" does not parse as a complete sentence (no finite verb with the noun-phrase as subject in independent-clause position). PASS.
  - `the-notation-the-machine-added-without-her-knowledge` (8 segments): noun-phrase (`the notation`) + relative clause (`the machine added`) + PP (`without her knowledge`). "The notation the machine added without her knowledge" does not parse as a complete standalone sentence. PASS.
Gate 4: `state-update:10` confirmed in locked state-updates.md at @64 (`prop:oc-district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin`). `state-update:11` confirmed at @64 (`actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks`). `proto:64` is on-screen. PASS.
Gate 6: biases dialogue-writer on Taylor's foreknowledge-gap register (she doesn't know the marks exist); NI interest-pattern on the epistemic gap. Actionable and distinct from existing bundle. PASS.
AP2: the state change (marks added) is recorded by state-update:10/11; the vibe records the QUALITATIVE CONSEQUENCE (she doesn't know; marks are invisible to her). Not a restatement of the state fact. PASS.

---

### Entry 8 — `@64 actor:census-officer ++ the-machinery-arrives`
**Tokens:** `[the-two-parallel-lines-as-notation-not-judgment, the-annotation-that-travels-with-her-name]`
**Licensed-by:** `state-update:10, proto:64`

**Verdict: CORRECT**

Gate 2: `census-officer/vibes.md` carries `the-machinery-arrives: [efficient-not-hostile, procedure-requires-no-malice, the-ledger-as-weapon, bureaucratic-momentum-indifferent-to-the-person]`. Keyword present. `++` is the correct op. PASS.
AP11 (string-overlap): no overlap. PASS.
AP8: `the-two-parallel-lines-as-notation-not-judgment` (7 segments) = noun-phrase + as-predicate compression. Not sentential. PASS. `the-annotation-that-travels-with-her-name` (6 segments) = noun-phrase + relative clause. Not sentential. PASS.
Gate 4: `state-update:10` confirmed. `proto:64` on-screen. PASS.
Gate 6: biases dialogue-writer fork on census officer's post-exit register (she marked the ledger as routine procedure, not as judgment). Distinct from `the-ledger-as-weapon` (systemic quality) — new tokens encode the officer's specific act as administratively-routine. PASS.

---

### Entry 9 — `@64 episode ++ the-machinery-arrives`
**Tokens:** `[the-notation-sealed-with-the-ledger, the-officer-who-exited-with-the-ledger]`
**Licensed-by:** `state-update:10, proto:64`

**Verdict: CORRECT**

Gate 2 (episode scope): `studio/vibes.md` EPISODE_1_VIBES carries `the-machinery-arrives: [efficient-not-hostile, procedure-requires-no-malice, the-ledger-as-weapon, bureaucratic-momentum-indifferent-to-the-person]`. Keyword present. `++` is the correct op under V1.1 patch. PASS.
AP11 (string-overlap): no string overlap with pre-loaded bundle. `the-notation-sealed-with-the-ledger` is distinct from `the-ledger-as-weapon` (structural quality vs departure-with-annotation event). PASS.
AP8: both tokens are 5-6 segments; noun-phrase compressions; not sentential. PASS.
Gate 4: `state-update:10` confirmed. `proto:64` on-screen. PASS.
Gate 6: biases episode-scope ambient toward the departure-with-annotation register (the machine exited with the record; the notation travels). Distinct from pre-loaded bundle. PASS.
AP9 audit: episode-scope `++` adds a departure-register not present in entity-target entries 7 (Taylor's knowledge-gap) or 8 (officer's procedure-as-routine). The departure-with-closed-ledger register is genuinely ambient (affects the whole episode's consequential framing, not only one entity). AP9 does not fire; entity-target alternatives do not carry this specific ambient register. PASS.

---

### Entry 10 — `@74 actor:taylor-hebert-westeros ++ the-letter`
**Tokens:** `[still-in-her-fist-at-the-threshold, the-object-she-carries-through-the-door]`
**Licensed-by:** `proto:49, proto:74, proto:77, state-update:12`

**Verdict: CORRECT**

Gate 2: `taylor-hebert-westeros/vibes.md` carries `the-letter: [the-thing-that-wont-work-before-she-tries-it, held-at-her-side, presenting-it-anyway-because-what-else, traveling-back-to-her-unchanged, the-form-of-what-he-could-give]`. Keyword present. `++` is the correct op. PASS.
AP11 (string-overlap): `still-in-her-fist-at-the-threshold` and `the-object-she-carries-through-the-door` — no string overlap. PASS.
AP8: both tokens are 5-7 segments; noun-phrase compressions. `still-in-her-fist-at-the-threshold` — "still" as adverb modifying participial `in-her-fist`, `at-the-threshold` as PP. Not sentential. PASS. `the-object-she-carries-through-the-door` (7 segments) — noun-phrase with relative clause. Not sentential. PASS.
Gate 4: `state-update:12` confirmed in locked state-updates.md at @77 (`actor:taylor-hebert-westeros.sublocation: yard -> sept-interior`). `proto:49`, `proto:74`, `proto:77` are on-screen beats tracing the letter through the episode close. PASS.

NOTE on anchor: Phase 4 assigns entry ID `@74` as anchor beat but cites proto:77 as the threshold-cross beat. `@74` is the approach beat (Taylor moving toward the sept). The anchor proto-line-id `@74` is the earliest beat in the licensing chain — acceptable per schema ("optional; required when licensed by on-screen beat"). The chain resolution (@74 approach + @77 cross) is internally coherent. PASS.

Gate 6: biases dialogue-writer and feeling fork on Taylor carrying the useless object past the threshold; metaphor-licensing context deepens (the letter's persistence into the sept adds an s01e02-open image bias). Distinct from `traveling-back-to-her-unchanged` (confrontation-register) — new tokens encode episode-close persistence. Distinct operator behavior confirmed. PASS.
Semantic adjacency advisory: `traveling-back-to-her-unchanged` vs `still-in-her-fist-at-the-threshold` — event-frame distinction is load-bearing and confirmed (confrontation failure vs episode-close persistence). Advisory satisfied per Phase 3 SEAM 4 analysis.

---

### Entry 11 — `@77 actor:taylor-hebert-westeros ++ the-septon-as-absence`
**Tokens:** `[the-door-she-can-open-after-the-machine-leaves, the-return-to-find-what-waits]`
**Licensed-by:** `state-update:12, memory:3, proto:70, proto:77`

**Verdict: CORRECT**

Gate 2: `taylor-hebert-westeros/vibes.md` carries `the-septon-as-absence: [what-he-could-not-give, the-closed-doors-as-answer, kindness-running-out-before-it-could-hold, the-letter-she-prepared-that-did-not-fit]`. Keyword present. `++` is the correct op. PASS.
AP11 (string-overlap): `the-door-she-can-open-after-the-machine-leaves` and `the-return-to-find-what-waits` — no string overlap with existing bundle. PASS.
AP8 sentence-parsability — AP8 BORDERLINE CASE (ADDRESSED):
  Token: `the-door-she-can-open-after-the-machine-leaves` (9 segments).
  Structure: noun-phrase (`the door`) + relative clause (`she can open`) + temporal clause (`after the machine leaves`).
  V1.1 AP8 formal test: "the door she can open after the machine leaves" — does this parse as a complete sentence? NO: there is no main predicate with `the door` as subject in an independent clause. The token is a noun-phrase with two compressed dependent clauses. Per V1.1 patch example: "the door she can open after the machine leaves" is explicitly given as a PASS example in the patch text. PASS.
  Token: `the-return-to-find-what-waits` (6 segments) — gerundive noun-phrase (`the return`) + infinitive purpose clause (`to find what waits`). Not sentential. PASS.
Gate 4: `state-update:12` confirmed at @77. `memory:3` confirmed in locked `memory.md` at @73 (`a threshold whose far side does not yield is not a new shape for her body -> (earth-bet: locker-displacement)`). `proto:70`, `proto:77` are on-screen beats. PASS.
Gate 6: biases dialogue-writer on Taylor's post-episode register (what she finds inside the sept — the inversion of the closed-door moment); behavior-pack on the completed-absence register shifts from external-closed-door to internal-confirmed-absence. PASS.
Semantic inversion check (Phase 3 SEAM analysis held): `the-closed-doors-as-answer` (pre-load: door she could NOT open) vs `the-door-she-can-open-after-the-machine-leaves` (new: door she CAN open post-officer-exit). These are semantic inversions at the same location, not duplicates. The semantic inversion is itself load-bearing — it encodes a narrative shift (the machine's absence changes what was previously closed). Advisory satisfied; PASS.

---

### Entry 12 — `@77 episode ++ the-letter`
**Tokens:** `[still-carried-through-the-threshold, the-object-that-entered-the-sept]`
**Licensed-by:** `state-update:12, proto:74, proto:77`

**Verdict: CORRECT**

Gate 2 (episode scope): `studio/vibes.md` EPISODE_1_VIBES carries `the-letter: [the-useless-object, what-he-could-give, held-at-her-side, traveling-back-unchanged, the-form-that-does-not-fit-the-rule]`. Keyword present. `++` is the correct op under V1.1 patch. PASS.
AP11 (string-overlap): `still-carried-through-the-threshold` and `the-object-that-entered-the-sept` — no string overlap with pre-loaded bundle. PASS.
AP8: both tokens are 4-6 segments; noun-phrase compressions; not sentential. PASS.
Gate 4: `state-update:12` confirmed. `proto:74`, `proto:77` on-screen. PASS.
Gate 6: biases episode-scope ambient register toward the letter's persistence past the episode. `traveling-back-unchanged` (pre-load) encodes the confrontation failure; `still-carried-through-the-threshold` encodes the episode-close persistence. Distinct operator bias for s01e02-open ambient reading. PASS.
Semantic note: `traveling-back-unchanged` vs `still-carried-through-the-threshold` — event-frame distinction confirmed (return-unchanged during confrontation vs persists-into-new-space at episode close). Advisory satisfied. PASS.

---

## 2. Per-fire verdict summary

| Entry | Target | Op | Keyword | Phase 4 Status | Phase 5 Verdict |
|---|---|---|---|---|---|
| 1 | actor:mira-stonefield | ++ | the-yard-as-witness | NEW | **CORRECT** |
| 2 | loc:harrenhal-sept-environs | + | the-machinery-arrives | DEFEND | **CORRECT** |
| 3 | actor:septon-dying-protector | + | the-septon-as-absence | DEFEND | **CORRECT** |
| 4 | loc:harrenhal-sept-environs | + | the-septon-as-absence | NEW | **CORRECT** |
| 5 | actor:edric-cray | ++ | the-yard-as-witness | NEW | **CORRECT** |
| 6 | episode | ++ | the-yard-as-witness | REVISE | **CORRECT** |
| 7 | actor:taylor-hebert-westeros | ++ | the-machinery-arrives | DEFEND | **CORRECT** |
| 8 | actor:census-officer | ++ | the-machinery-arrives | DEFEND | **CORRECT** |
| 9 | episode | ++ | the-machinery-arrives | REVISE | **CORRECT** |
| 10 | actor:taylor-hebert-westeros | ++ | the-letter | DEFEND | **CORRECT** |
| 11 | actor:taylor-hebert-westeros | ++ | the-septon-as-absence | DEFEND | **CORRECT** |
| 12 | episode | ++ | the-letter | REVISE | **CORRECT** |

**Final accept rate: 12/12 = 100%**

---

## 3. Per-skip verdicts — remaining SKIP-MISSED candidates

Phase 3 identified six SKIP-MISSED candidates. Phase 4 addressed three of them (edric, mira, loc:sept-environs). I now evaluate whether any unaddressed skip-missed candidates remain.

**Skip-3 (Taylor `++` the-naming, Phase 3 MODERATE):** Phase 4 did NOT add this entry. Taylor's pre-loaded `the-naming` bundle: `[giving-her-name-aloud-to-a-ledger, the-moment-the-window-closes, the-irrevocable-action-she-takes-herself, she-said-it, no-going-back-in-that-specific-direction]`. This bundle is dense and event-complete for the naming-act register. Phase 4's decision to omit this `++` is defensible: the pre-loaded bundle covers the primary qualitative-consequence range of state-update:7 (`administrative-status: child-or-ward -> provisional-labor-eligible`). The category-placement register (Phase 3's proposed non-duplicate token: `the-category-she-was-placed-in-not-chosen`) is plausible but not mandated by rubric. The pre-loaded bundle's `giving-her-name-aloud-to-a-ledger` already encodes the category-framing at the act level. **SKIP-CONFIRMED.** Phase 4's decision to omit this entry is within rubric tolerance. Not a fault.

**Skip-4 (loc:westerosi-smallfolk-village-common / loc:harrenhal-sept-environs for E5, Phase 3 THIN):** Phase 3 rated this THIN. Phase 4 did not add this entry. The E5 event's qualitative consequence is primarily actor-borne (mira, edric). The location-as-site of E5 does not require an additional `+the-yard-as-witness` fire on the location — the sept environs' vibe-set now carries `the-machinery-arrives` and `the-septon-as-absence` (entries 2 and 4). Adding `the-yard-as-witness` to the location would be AP9-adjacent (the character-level consequence already covers the social dynamics; the location is not a new charged-space from E5 specifically). **SKIP-CONFIRMED.** Not a fault.

**Skip-5 (prop:oc-letter, Phase 3 THIN contingent):** The `prop:oc-letter` card is not yet authored (margit referral from state-updates audit still outstanding per state-updates.md). Phase 4 correctly deferred. No active-project prop vibe file exists to check for pre-load. Absence is contingent on margit referral resolution. **SKIP-CONFIRMED.** Not a fault; remains a contingent THIN gap.

**Assessment:** No new SKIP-MISSED candidates identified. Phase 4 addressed all STRONG and MODERATE skip-missed cases. All remaining skips are either confirmed as rubric-acceptable omissions or contingent on margit referral.

---

## 4. File-shape verdict

**SHAPE-OK**

Phase 4 file passes all shape requirements:
- `---` metadata block present and complete with required fields (facet, episode, author, phase, rubric, prior-phase references).
- `@<proto-line-id>` anchor format applied correctly across all 12 entries.
- `licensed-by:` field present on all 12 entries with ≥1 source. No `?` placeholders.
- Final entry list presented in ascending proto-line order (confirmed: @6, @11, @33, @33, @57, @57, @64, @64, @64, @74, @77, @77).
- Op notation (`+`, `++`) correctly applied across all entries.
- Token bundles are word-algebra format; no prose tokens surviving to final list.
- Decisions-at-a-glance table present and internally consistent with entry list.

One minor structural note: entries 3 and 4 share anchor `@33`; entries 6 and (implicitly) entry 5 share anchor `@57`; entries 7, 8, 9 share anchor `@64`; entries 11 and 12 share anchor `@77`. Same-anchor ordering is by target type (actor before episode before loc) which is consistent with no declared ordering rule — acceptable. No shape fault.

---

## 5. Phase 4 residual edge cases — direct address

### Edge case A: Token `the-door-she-can-open-after-the-machine-leaves` AP8 under V1.1 sentence-parsability test

**Confirmed: PASS under V1.1.**

V1.1 patch explicitly includes `the-door-she-can-open-after-the-machine-leaves` as an example of a PASS case in the revised AP8 text: "the-door-she-can-open-after-the-machine-leaves (9 segments) — noun-phrase with relative + temporal clause compressed; no standalone main predicate; reads as a noun-phrase; PASS." The Phase 4 rubric patch resolves this edge case definitively. No fault.

### Edge case B: Mira entry @6 anchored before licensing event E5 @51-@57 — temporal-pre-anchor acceptability

**Confirmed: ACCEPTABLE.**

The schema states `@<proto-line-id>` is "required when the vibe is licensed by an on-screen beat." Entry 1 cites `feeling:1` (which fires at @6) as its primary licensing event. The entry's anchor is `@6`, consistent with the feeling-flag's beat position. The proto-line-id anchor is the ANCHOR beat of the licensing event, not the event that the vibe describes in aggregate terms.

`feeling:1` at @6 is the on-screen beat that establishes Mira's door-orientation reflex. The vibe licensed by this beat (`the-door-already-marked-before-the-ask`) is anchored to @6 — the beat that produced the licensing event. The fact that E5 occurs later (@51-@57) does not make the @6 anchor incorrect; the anchor reflects WHEN the licensing event occurs, not when the vibe-keyword's fullest consequence is felt. Additional citations `proto:51` provide the forward linkage. The V1.1 rubric does not require anchors to be placed at the event-being-characterized; it requires the anchor to reflect the on-screen licensing beat. @6 is the on-screen beat. **TEMPORAL-PRE-ANCHOR IS ACCEPTABLE.** No fault.

### Edge case C: `prop:oc-letter` deferred (margit referral pending)

**Confirmed: DEFERRED with contingent flag maintained.**

No `prop:oc-letter` card exists in `cards/props/` (state-updates.md margit referral outstanding). No active-project prop vibe file exists. Per the addendum and Phase 3 Skip-5 analysis, absence is not a fault — it is contingent on margit referral resolution. If the prop card is authored before s01e02 facet authoring begins, a `prop:oc-letter +the-letter [the-object-that-cannot-be-received, the-ward-document-in-smallfolk-context]` fire (or similar) should be authored at that time. **No blocking issue for Phase 5 ship.** Contingent flag carried forward (see caveat-002 below).

---

## 6. Read-side coherence check

**Scene selected:** Scene D close, @68-@77 (4-beat close; Taylor approaches the sept and enters).

**Locked downstream entries active at this scene:**
- `state-updates:12` (@77): `actor:taylor-hebert-westeros.sublocation: yard -> sept-interior`
- `state-updates:13` (@77): `actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private`
- `memory:3` (@73): "a threshold whose far side does not yield is not a new shape for her body" → (earth-bet: locker-displacement)
- `feeling:4` (@73): `taylor-hebert-westeros: her breath empties between one step and the next | expressed: no`
- `metaphor:2` (@73): "her breath goes out like something set down at a threshold it has crossed before" | licensed-by: memory:3 + feeling:4 + tens:1

**Phase 4 vibe extensions that would be read by the dialogue-writer fork on Taylor entering this scene:**
- `actor:taylor ++ the-septon-as-absence` (entry 11): `[the-door-she-can-open-after-the-machine-leaves, the-return-to-find-what-waits]`
- `actor:taylor ++ the-letter` (entry 10): `[still-in-her-fist-at-the-threshold, the-object-she-carries-through-the-door]`
- `actor:taylor ++ the-machinery-arrives` (entry 7): `[the-marks-beside-her-name-invisible-to-her, the-notation-the-machine-added-without-her-knowledge]`
- `loc:harrenhal-sept-environs + the-septon-as-absence` (entry 4): `[the-space-where-the-door-stayed-shut, the-building-whose-occupant-cannot-reach-its-threshold, charged-ground-for-what-did-not-emerge]`

**Coherence analysis:**

The locked feeling/memory/metaphor entries at @73 assume a Taylor who is:
- Carrying a prior monument-recognition at thresholds (memory:3 → locker-displacement)
- In a controlled-body-discipline somatic register (feeling:4 → breath empties between steps, expressed: no)
- Generating a simile-level figurative payload about setting something down at a threshold she has crossed before (metaphor:2)

The Phase 4 vibe extensions would have been read by the dialogue-writer fork as:
- Taylor carries the letter still (the-fist-at-threshold, the-object-through-the-door) — consistent with metaphor:2's "something set down at a threshold" (the letter is the something)
- The door she can now open after the machine leaves — consistent with memory:3's threshold-crossing register (the machine's absence enables the crossing; the monument frames the crossing as a known shape for her body)
- She doesn't know the margin marks exist — consistent with the foreknowledge-gap that makes the close poignant rather than triumphant

**Coherence verdict: COHERENT.** The Phase 4 vibe extensions are downstream of the same licensing events that generated the locked facets (state-update:12, memory:3, feeling:4). They add operator-bias color that reinforces rather than contradicts the locked facets' content. A dialogue-writer reading Taylor's Phase-4-extended vibe-set before s01e01 shoot would have generated a voice that:
- Holds the letter at the threshold (consistent with feeling + metaphor: something set down)
- Reads the door's opening as a possible reversal (consistent with memory:3's threshold-familiarity + the-septon-as-absence inversion)
- Remains epistemically isolated from the margin marks (consistent with the knowledge-gap register in state-update:11)

The locked feeling-flags, memory-flags, and metaphor entries assume exactly this voice-shape for the @73-@77 close. No contradiction. **Read-side coherence confirmed.**

---

## 7. Headline metrics

| Metric | Value |
|---|---|
| Phase 4 entries adjudicated | 12 |
| CORRECT | 12 |
| INCORRECT | 0 |
| REFUSE-CORRECT | 0 |
| Accept rate | **12/12 = 100%** |
| Phase 1 baseline | 0/29 = 0% |
| Phase 2 accept rate | 6/11 = 54.5% |
| Lift from Phase 1 baseline | **+100pp** |
| Skip-missed residuals | 0 (all addressed or confirmed-skip) |
| Shape verdict | SHAPE-OK |
| Fault count | 0 |
| Flag count | 0 (findings below are informational only) |
| Escalation count | 0 |

---

## 8. Ship-readiness verdict

**SHIP-WITH-CAVEATS**

No blocking faults. Residual caveats are informational or contingent.

---

## 9. Residual caveats

**caveat-001 (notation; V1.1 patch ship-timing):** The V1.1 rubric patch (`design/shoot-v2/rubric-vibes-v1.1-patch.md`) was authored as a supplement but is not yet integrated into the main rubric file (`design/shoot-v2/rubric-vibes.md`). Per the patch's own header: "Ship protocol: V1.1 text ships same commit as Phase 5 facet file." The commit that ships the facet file must also update the main rubric document (or formally supersede it with V1.1). No blocking issue for facet acceptance; must be resolved at ship commit.

**caveat-002 (contingent; prop card gap):** `prop:oc-letter` has no card in `cards/props/` (margit referral outstanding from state-updates audit). No `prop:oc-letter` vibe entry can be authored until the card exists. If the margit referral resolves before s01e02 facet authoring begins, a vibes-updates fire for the letter-as-prop should be included in s01e02's facet or as a showrunner reflective-pass inter-episode entry. Becomes MODERATE if not addressed before s01e02 shoot.

**caveat-003 (per-episode volume; informational):** Final yield 12 entries. Within the addendum's stated pre-seeded expected range (9-14 entries). Confirmed inside rubric tolerance. No ceiling violation (rubric has no upper ceiling). Informational only.

**caveat-004 (loc-slug discrepancy; informational):** Phase 2 entry 7 targeted `loc:westerosi-smallfolk-village-common`; Phase 4 entry 2 targets `loc:harrenhal-sept-environs`. These are the same location (the sept and its yard) under two different slug references. The warehouse card is `loc-harrenhal-sept-environs.card.md`. The `loc:harrenhal-sept-environs` slug is the correct active-project warehouse slug. Before s01e02 authoring, verify that any reference to `westerosi-smallfolk-village-common` in the library card index or other files resolves consistently to `harrenhal-sept-environs` at the active-project level. No blocking issue for this facet.

**caveat-005 (cross-facet downstream forward; informational):** The 12 vibe-updates entries add token extensions to actor vibe-sets (Taylor, Mira, Edric, Census Officer) and location vibe-sets (harrenhal-sept-environs), and to the episode-scope entries in studio/vibes.md EPISODE_1_VIBES. These write-back mutations are the showrunner's responsibility at cross-facet write-back time. The facet file is the delta record; write-back to cloud files must occur before s01e02 authoring begins. Specifically: the showrunner must append the new `++` tokens to each actor's vibes.md and to the appropriate studio/vibes.md sections, and add the fresh `+` entries for septon-dying-protector and loc:harrenhal-sept-environs.

---

## 10. Findings (schema-compliant)

```yaml
findings:
  - id: fault-001
    type: pass
    what: all 12 Phase 4 entries across all gates and anti-patterns
    why: no faults found; all entries pass gate 1-7, AP1-AP13, V1.1 sentence-parsability test, string-overlap formal gate, and licensed-by resolution
    criteria: n/a

  - id: flag-001
    type: flag
    what: caveat-001 — V1.1 patch not yet merged into main rubric file
    why: the facet ships with patch clauses active but the main rubric text does not reflect them; future auditors reading only rubric-vibes.md V1 may apply the pre-patch AP8 test and classify entry 11's 9-segment token incorrectly
    criteria: n/a (flag; no fixer dispatch required; ship-commit action for showrunner)

  - id: flag-002
    type: flag
    what: caveat-002 — prop:oc-letter vibe entry deferred pending margit referral
    why: the letter is load-bearing in three facets (state-updates, feeling implied context, vibes entries 10/12); a prop-level vibe entry would complete the fan-out and bias studio prop-state descriptions; currently absent by necessity, not by choice
    criteria: n/a (flag; contingent on margit referral; becomes moderate if unresolved before s01e02)

  - id: flag-003
    type: flag
    what: caveat-005 — write-back of vibe-cloud mutations pending
    why: the vibes-updates facet is the delta record; until the showrunner writes back the 12 entries' mutations to actors/*/vibes.md and studio/vibes.md, the cloud files do not reflect the episode-1 facet results; downstream s01e02 operators will read stale clouds
    criteria: n/a (flag; showrunner write-back required before s01e02 authoring; no fixer dispatch)
```

---

## 11. Facet frontmatter recommendation

Based on Phase 5 findings, the locked facet file should carry the following frontmatter:

```
---
facet: vibes-updates
episode: s01e01
author: showrunner-fork
phase: 5 (final; Phase 4 revised output adjudicated 12/12 = 100%)
rubric: design/shoot-v2/rubric-vibes.md (V1 LOCKED) + rubric-vibes-v1.1-patch.md (patch ships this commit)
sparsity: 15.6% (12 fires / 77 beats) — no upper ceiling; pre-seeded project yield within 9-14 range
distribution:
  entity-target-adds (+): 2 (loc:harrenhal-sept-environs ×2; actor:septon-dying-protector ×1 = 3 total fresh adds)
  entity-target-extends (++): 5 (actor:taylor ×3, actor:mira ×1, actor:edric ×1, actor:census-officer ×1 = 6 total)
  episode-scope-extends (++): 3 (the-machinery-arrives, the-yard-as-witness, the-letter)
  removals (-): 0
  phase2-deletes: 2 (entries 4+5 from Phase 2 correctly deleted; pre-loaded bundles complete)
calibration-anchors:
  C1 (actor:taylor the-machinery-arrives): satisfied (pre-load + entry 7 extension)
  C2 (actor:septon the-septon-as-absence): satisfied (entry 3 fresh add)
  C3 (actor:mira the-yard-as-witness): satisfied (pre-load + entry 1 extension)
  C4 (episode the-naming): satisfied by pre-load; no in-episode ++ warranted; correctly skipped
caveats: 5 (none blocking; see phase5-vibes-final.md)
---
```

Sparsity note: 12/77 = 15.6% is not the standard sparsity framing used by other facets (which count fires against beats). Vibes-updates has no upper ceiling and a no-floor; the 12-entry yield is the correct pre-seeded project output. The frontmatter should note the pre-seeded context to prevent future auditors from comparing this yield against the clean-slate rubric's "~16-20 entries" expectation.
