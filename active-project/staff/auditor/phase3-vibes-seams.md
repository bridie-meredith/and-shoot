---
audit:
  scope: seam-finding (adversarial Phase 3)
  target: s01e01 / vibes-updates facet / Phase 2 output
  timestamp: 2026-05-07
  reviewer: auditor (hostile mode)
  rubric: design/shoot-v2/rubric-vibes.md (V1 LOCKED)
  phase2-output: design/shoot-v2/phase2-vibes-output.md
  phase2-mechanic-audit: active-project/staff/auditor/phase2-vibes-audit.md
  corpus: design/shoot-v2/vibes-corpus.md
  vibe-clouds: active-project/staff/studio/vibes.md + active-project/actors/*/vibes.md
  upstream-locked: theater/facets/state-updates.md, memory.md, feeling.md
---

# Phase 3 Vibes-Updates — Adversarial Seam-Finding

---

## SEAM 1 — RF-001 ESCALATION: World-build pre-load vs in-episode license-event (LOAD-BEARING)

**Tag: LOAD-BEARING — must be resolved at Phase 4 before any fixer revision**

Three readings of the rubric's op-coherence rule (gate 2 / AP5), each with a fully-developed argument:

### Reading (a) — STRICT: Pre-loaded vibe-cloud is authoritative; in-episode events fire `++` only with token-non-overlap; vast majority of s01e01 fires are `++` or skip

**Case:** Gate 2 is unambiguous — "`+` requires keyword absent from target's current vibe-set." The vibe-cloud files are live state. `actor:taylor-hebert-westeros/vibes.md`, `mira/vibes.md`, `edric/vibes.md`, `actor:census-officer/vibes.md`, and `staff/studio/vibes.md` (episode-scope section) all carry the five s01e01 keywords with token-bundles. This is not a planning shadow — it is the canonical record. The showrunner's activation-time authoring of those bundles was itself a vibe-authoring act; the facet file is the add-to-show record of that act. Nothing in the rubric says world-build-sourced vibes are "pre-authoritative" and episode-facet-sourced vibes are "officially authoritative." The state is the state. Pre-loaded = present. Present = `++` or skip, never `+`.

**Implication for s01e01:** 16 corpus fires collapse to ~9 valid entries (entries 8, 9, 10, 11 from Phase 2 + entry 1 + entry 7 + the mira/edric/episode `++` extensions that pass AP11). The C1–C4 calibration anchors are satisfied by the pre-load alone, not by fresh `+` fires.

**Implication for locked facet shape:** The Phase 0 corpus was authored under the assumption that s01e01 is the project's first episode and no vibes exist yet. That assumption was wrong for this project — vibe-clouds were seeded at activation. The corpus's 16 × `+` format is internally consistent with a clean-slate world, but is not valid as the Phase 2 target for a world-build-pre-seeded project. The corpus is a correct fiction for a different pipeline state; it was used as the wrong reference.

**Strongest argument for (a):** The rubric explicitly defines `++` as the extension operator and AP5 prohibits duplicate `+`. There is no exception clause for "world-build pre-loads." The precedent from metaphor tuning (monument-scope determination) confirms: if the token is already there, the correct response is `++` with genuinely new scope, not re-addition. (a) is the strictly correct reading of the written rubric.

---

### Reading (b) — RELAXED: Pre-loaded vibe-cloud is a planning shadow; facet entries fire `+` regardless and cloud-files are reconciled at write-back time

**Case:** The vibe-cloud files (`actors/*/vibes.md`, `studio/vibes.md`) are showrunner working-memory — planning artifacts populated during world-build to give downstream operators something to read before any episode-facet is authored. They are not facet entries; they have no `@<proto-line-id>` anchors, no `licensed-by:` chains, no op-notation. They are a different document class than `theater/facets/vibes.md`. The facet file is the canonical episodic record; the cloud files are operational shortcuts. Therefore: the facet file's `+` fires are valid adds that establish on-screen-licensed vibe authority, and the showrunner performs a write-back pass (cloud-files updated from facet entries, potentially replacing planning-shadow bundles). This is consistent with the "write side" definition in the rubric: vibes-updates *writes* the facet; downstream operators read *the cloud files* — which implies the cloud files are the output of a write-back pass, not themselves the authoritative fire record.

**Implication for s01e01:** All 16 corpus fires are valid. The Phase 2 fork's actor-level diagnosis was correct; it should have applied the same logic to episode-scope (`studio/vibes.md` episode section is also a planning shadow). Under reading (b), entries 2–6 in Phase 2 are valid `+` fires and the phase-2-audit's five faults are wrong.

**Implication for locked facet shape:** The corpus shape holds. The Phase 2 fork gets a 6/11 → 11/11 reversal under this reading.

**Strongest argument for (b):** The rubric's "write side — vibes-updates bias" section says downstream operators read the cloud files. But the cloud files don't auto-update — something must write them. If the facet is the write event, the cloud-files start as planning shadows and are updated after each episode's facet is authored. This is exactly how `state-updates` works: state files carry the running state, but the state-updates facet records the delta. The vibe-cloud files ARE the running state; the vibes-updates facet IS the delta record. Under this model, `+` fires on keywords that exist in the cloud ARE duplicate-adds by gate-2 — which collapses (b) back toward (a) unless the rubric carves out an exception for cloud-file pre-loads.

**Critical crack in (b):** Reading (b) requires the rubric to distinguish between two document classes (planning clouds vs facet entries) that the rubric text does not distinguish. The rubric gate-2 refers to "target's current vibe-set" — which is read from the cloud files. If the cloud files carry the keyword, gate-2 fires. Reading (b) survives only if the rubric explicitly defines cloud-files as excluded from gate-2 checking, which it does not.

---

### Reading (c) — HYBRID: World-build series + season scope is authoritative pre-load; episode-scope and entity-target adds fire fresh `+` per-episode; cloud-files written-back from facet entries

**Case:** The rubric defines three scope levels: series, season, episode. World-build produces series and season vibe-clouds. Episode-scope (`EPISODE_1_VIBES` in `studio/vibes.md`) and per-episode entity adds are authored by the facet file and represent a distinct episodic pass. Series + season clouds are authoritative; the facet file's episode-scope and entity-target fires are the source of truth for episode-level granularity. Post-facet-authoring, the showrunner writes back: episode-scope vibes promoted to clouds; entity-target new keywords added to actor/location cloud files.

**Implication:** For actor targets with only world-build / series / season bundles, the episode facet fires `+` fresh. For actor targets whose keywords were pre-loaded IN THE EPISODE SECTION of the cloud (as happened here, where s01e01 keywords were added to `actors/*/vibes.md` at activation with episode-event specificity), the episode facet must use `++`. The distinction is scope: series/season-scoped pre-loads are planning artifacts; episode-scoped entity pre-loads are facet-anticipatory authorings.

**Problem for (c):** In this project, the `actors/*/vibes.md` files carry the five s01e01 keywords in their flat VIBES section (not in an "EPISODE_1" subsection), meaning gate-2 reads them as simply present. The `studio/vibes.md` has explicit `EPISODE_1_VIBES:` subsections — which makes the scope-layering visible there. But the actor-level cloud files have no such section structure. Reading (c) requires a structural distinction that the actor-level files do not encode.

**Hybrid resolution path:** Reading (c) is the most coherent resolution IF the pipeline is redesigned so that: (i) cloud-files use section headings (`SERIES_VIBES`, `SEASON_1_VIBES`, `EPISODE_N_VIBES`) for entity-level targets, matching the studio/vibes.md structure; (ii) gate-2 checking is scoped to the current episode's section — keywords pre-loaded in future-episode sections are not yet authoritative; (iii) write-back explicitly promotes facet entries into episode section headers. This is a pipeline design change, not a rubric-text-only fix.

---

### Auditor recommendation on RF-001

**Commit to reading (a) as the correct rubric interpretation, with one targeted supplement.**

The rubric as written supports (a). Gate-2's "target's current vibe-set" means the cloud file state at time of facet authoring. Pre-loaded = present. AP5 prohibits `+`. The corpus was authored against a clean-slate assumption that is false for this project.

**Supplement required:** Phase 4 must add one rubric clause: "Where world-build or project-activation populates cloud-files prior to the first episode's facet authoring, the showrunner treats those bundles as authoritative existing state. Episode-facet authoring uses `++` to extend with genuinely on-screen-licensed non-duplicate tokens, or omits an entry if the existing bundle already covers the event's qualitative-consequence range. The corpus's `+`-only format reflects a clean-slate scenario; in pre-seeded projects, the predominant op is `++` or skip."

**Why not (b):** Reading (b) cannot survive gate-2 as written. It requires the rubric to say something it does not say.

**Why not (c):** Reading (c) is architecturally appealing but requires cloud-file restructuring that has not been done and is not in the current pipeline. It is the correct long-term design but cannot be retroactively applied to this corpus without schema work.

**Why (a) wins:** It is what the rubric says. The Phase 2 fork correctly applied (a) to actor targets; the Phase 2 audit correctly extended that finding to episode-scope targets. The corpus shape must be re-evaluated: the 16 × `+` reference fires are wrong for a pre-seeded project. Phase 4 must restate the corpus as: 9–12 valid entries (mix of `+` on empty targets + `++` extensions + episode-scope `++` where on-screen beats add non-duplicate tokens).

---

## Per-entry seam analysis (entries 1–11)

### Entry 1 — `@33 actor:septon-dying-protector + the-septon-as-absence`

**Seam: THIN**

Phase 2 audit marked CORRECT. Septon's cloud file carries `dying`, `protection`, `kindness`, `ward`, `the-septon-failing`, `observer-arriving` — none of which is `the-septon-as-absence`. Gate-2 passes.

Adversarial press: Is `the-septon-as-absence` semantically contained within the existing `the-septon-failing` bundle (`kindness-running-out`, `the-first-genuine-thing`, `protection-from-someone-who-cannot-protect`, `the-timer`)? The argument for containment: `the-septon-failing` already encodes that protection is expiring. But `the-septon-as-absence` encodes a different register — not the process of failing but the completed-absence event (door-stays-shut; body-that-cannot-come-to-threshold). Gate-6 actionability is distinct: `the-septon-failing` biases operators toward ongoing-decline; `the-septon-as-absence` biases operators toward completed-absence-as-event. The distinction is load-bearing (septon's behavior-pack fires on completed-absence differently than ongoing-decline).

AP2 press: Is `the-septon-as-absence` restating the state-updates fact that the door stayed shut? No — state-updates does not record a state change here (the door staying shut is the absence of a state change). The vibe derives qualitative consequence from non-event. Passes AP2.

**Verdict: THIN seam. Entry 1 survives hostile review.**

---

### Entry 2 — `@11 episode + the-machinery-arrives`

**Seam: STRONG (fault confirmed by Phase 2 audit)**

`studio/vibes.md` EPISODE_1_VIBES carries `the-machinery-arrives` with token-bundle `[efficient-not-hostile, procedure-requires-no-malice, the-ledger-as-weapon, bureaucratic-momentum-indifferent-to-the-person]`. The Phase 2 authored bundle is token-for-token identical. AP5 + gate-2 fault is confirmed.

**Salvage question (SEAM 2):** Can entry 2 be salvaged as `++` with non-duplicate tokens? The pre-loaded bundle covers the officer-as-instrument framing. On-screen beats @64–@77 add: the notation added to Taylor's margin without her knowledge; the officer's exit after annotation. Possible non-duplicate tokens for a `++` extension: `the-notation-she-added-and-left` (the officer's specific departure-with-annotation), `the-census-that-travels-sealed` (the ledger proceeding beyond the village after @64). These are not covered by the pre-loaded bundle.

**Salvage verdict:** A `++` extension IS possible for entry 2 if the Phase 4 fixer identifies tokens that are both (i) not in the pre-loaded bundle and (ii) licensed by s01e01 on-screen beats beyond what the pre-load covers. The identical-bundle form authored in Phase 2 cannot be salvaged; it must be either replaced with `++` + non-duplicate tokens, or deleted if no such tokens exist. See also entry 8 (actor:taylor ++ the-machinery-arrives) for token guidance on what @64 adds.

---

### Entry 3 — `@45 episode + the-letter`

**Seam: STRONG (fault confirmed by Phase 2 audit)**

Pre-loaded bundle in `studio/vibes.md` EPISODE_1_VIBES: `[the-useless-object, what-he-could-give, held-at-her-side, traveling-back-unchanged, the-form-that-does-not-fit-the-rule]`. Phase 2 authored bundle is token-for-token identical.

**Salvage question:** Entry 9 (`actor:taylor ++ the-letter`) adds `[still-in-her-fist-at-the-threshold, the-object-she-carries-through-the-door]` via `state-update:12` (Taylor enters sept at @77). These tokens describe what the letter does AT THE END of the episode — not the @45 letter-return event. An episode-scope `++` extension citing state-update:12 + proto:77 could add `still-carried-through-the-threshold`, `the-object-that-entered-the-sept` — genuinely non-duplicate.

**Salvage verdict:** Partial. Entry 3 can be salvaged as `++` anchored to @77 rather than @45, adding tokens that describe the letter's persistence past the episode-close event. However, entry 3's `@45` anchor would need updating to `@77` or a later anchor.

Additional press: The semantic overlap seam (SEAM 4) is directly relevant here. See SEAM 4 below for the `traveling-back-to-her-unchanged` vs `still-in-her-fist-at-the-threshold` argument.

---

### Entry 4 — `@48 episode + the-naming`

**Seam: STRONG (fault confirmed by Phase 2 audit)**

Pre-loaded bundle in `studio/vibes.md` EPISODE_1_VIBES: `[the-moment-of-being-asked, the-name-given-aloud, the-dictation-as-finality, the-door-that-closes-on-its-own-momentum]`. Phase 2 authored bundle is token-for-token identical.

**Salvage question:** Is there anything on-screen in s01e01 that the pre-loaded bundle does NOT cover? The pre-load captures the episode-scope ambient framing. What the episode-scope target does NOT carry: the specific form-compliance angle (the officer's phrase, the scribal notation form), and — critically — the episode-6 resonance token that `studio/vibes.md` shows in EPISODE_6_VIBES's `the-naming` keyword (`function-given-aloud, irrevocable`). Episode-6 vibes are not yet authored into episode-1 scope. A `++` extension could add: `the-form-that-accepts-her-answer`, `dictated-as-fact-not-question` — tokens reflecting the s01e01 on-screen event's specific texture not captured in the pre-load.

**Salvage verdict:** Marginal. The pre-loaded bundle is already fairly complete for episode-scope ambient. A `++` extension is possible but requires genuine on-screen anchoring that doesn't merely restate the pre-load's conceptual content.

---

### Entry 5 — `@33 episode + the-septon-as-absence`

**Seam: STRONG (fault confirmed by Phase 2 audit)**

Pre-loaded bundle in `studio/vibes.md` EPISODE_1_VIBES: `[present-but-cannot-appear, the-protector-who-cannot-act, the-letter-in-place-of-the-body, kindness-that-runs-out-before-it-can-hold]`. Phase 2 authored bundle is token-for-token identical.

**Salvage question:** The pre-loaded bundle is complete for the E4 event as scoped to episode-ambient. The on-screen beats at @31–@33 are: officer addresses threshold; door stays shut. No non-duplicate token is obvious from these beats beyond what the pre-load encodes. However: state-update:12 (Taylor enters sept at @77) adds a new dimension to the absence that is not in the pre-load — Taylor opens the door the septon never could. A `++` extension at @77: `the-door-she-opened-after-the-machine-left`, `the-absence-confirmed-at-threshold-cross`. These would be genuinely non-duplicate and on-screen-licensed.

**Salvage verdict:** Weak but present. Episode-scope `++` for the-septon-as-absence is defensible only if anchored to @77 (not @33). If anchored to @33 only, no non-duplicate tokens exist; delete is correct.

---

### Entry 6 — `@57 episode + the-yard-as-witness`

**Seam: STRONG (fault confirmed by Phase 2 audit)**

Pre-loaded bundle in `studio/vibes.md` EPISODE_1_VIBES: `[mira-delivering-verdict-before-it-happens, edric-watching-the-road-without-watching, what-everyone-already-knew]`. Phase 2 authored bundle is token-for-token identical.

**Salvage question:** The pre-load captures the ambient social-dynamics framing. What the episode does on-screen that the pre-load doesn't capture: the specific spatial sequence (officer still in yard when Mira drops eyes at @52; officer exits before Edric steps back at @57). Possible non-duplicate tokens: `the-refusal-with-the-officer-present`, `edric-after-the-gate-cleared`. These are genuinely non-duplicate and on-screen-licensed.

**Salvage verdict:** Possible. `++` extension plausible with spatial/sequencing tokens that the pre-load's ambient framing omits. Anchored to @57 (correct for E5 close).

---

### Entry 7 — `@11 loc:westerosi-smallfolk-village-common + the-machinery-arrives`

**Seam: THIN**

Phase 2 audit marked CORRECT. Location's vibe-set is empty (no pre-load confirmed: card carries no VIBES section; no active-project warehouse vibe file). Gate-2 passes. Token-bundle is word-algebra. Licensed-by resolves.

Adversarial press on AP9 (abstract-scope-when-entity-fits): entry 2's episode-scope `the-machinery-arrives` and entry 7's loc-scope `the-machinery-arrives` carry partly overlapping semantic content. Under AP9, entity-target is preferred. But entry 7 IS the entity-target (the loc). The episode-scope entry (entry 2) may be the AP9 violation — it should be checked whether the episode-scope `the-machinery-arrives` is fully covered by the loc-scope entry 7 + actor-scope entries 8/11, in which case the episode-scope entry should be deleted rather than corrected to `++`.

**Token-overlap press:** entry 7's `the-yard-that-cannot-claim-ignorance` is semantically adjacent to entry 6's pre-loaded episode token `what-everyone-already-knew`. Not a mechanical AP11 violation (different targets), but a semantic coherence question: are these encoding the same qualitative consequence at different targets? Under (a) reading, entry 6 (episode-scope) should either be a `++` with non-duplicative tokens OR deleted if entry 7 already carries the entity-bound form of the insight.

**Verdict: THIN seam for entry 7 in isolation. MODERATE seam when entry 7 is read against entries 2 and 6 (AP9 and scope-layering interaction).**

---

### Entry 8 — `@64 actor:taylor-hebert-westeros ++ the-machinery-arrives`

**Seam: MODERATE**

Phase 2 audit marked CORRECT. New tokens `[the-marks-beside-her-name-invisible-to-her, the-notation-the-machine-added-without-her-knowledge]` checked against existing bundle `[the-officer-as-instrument-not-enemy, forms-have-no-slot-for-her-situation, the-refusal-that-requires-no-malice, bureaucratic-weight-she-cannot-argue-with]`. No string overlap. Mechanic passed.

**Semantic-overlap press (SEAM 4):** The pre-loaded bundle already contains `forms-have-no-slot-for-her-situation`. The new token `the-marks-beside-her-name-invisible-to-her` adds a knowledge-gap register (she doesn't know the marks exist). These are semantically distinct: "no-slot" = form cannot accommodate her; "marks-invisible-to-her" = action taken on her record without her awareness. Passes semantic-overlap test.

**AP13 press:** `the-marks-beside-her-name-invisible-to-her` — is this prose-narration? The rubric says AP13 fires on tokens that "read as a sentence the narrator might say." The token is a noun-phrase (the-X-[modifier]-Y structure), not a sentence. It contains `invisible-to-her` as a participial compression. Compare to AP13's example: `the-officer-was-efficient-and-she-knew-it` (rejected) vs `efficient-not-hostile` (accepted). The token `the-marks-beside-her-name-invisible-to-her` is longer than `efficient-not-hostile` but is still noun-phrase-structured, not sentential. The rubric's AP8 says "Maximum: a noun-phrase or short clausal compression bound by hyphens." This token is a compressed noun phrase. PASSES AP8/AP13 under strict word-algebra test — but see SEAM 6 for the token-length heuristic question.

**Verdict: MODERATE seam (AP8/AP13 press is live; token is near the AP8 boundary). Entry 8 survives but Phase 4 must commit the token-length heuristic.**

---

### Entry 9 — `@74 actor:taylor-hebert-westeros ++ the-letter`

**Seam: MODERATE (semantic-overlap attack live — see SEAM 4)**

Phase 2 audit marked CORRECT. New tokens `[still-in-her-fist-at-the-threshold, the-object-she-carries-through-the-door]` checked against existing bundle `[the-thing-that-wont-work-before-she-tries-it, held-at-her-side, presenting-it-anyway-because-what-else, traveling-back-to-her-unchanged, the-form-of-what-he-could-give]`.

**Semantic-overlap attack:** The pre-loaded bundle contains `traveling-back-to-her-unchanged`. The new token `still-in-her-fist-at-the-threshold` is not a string duplicate — but SEMANTICALLY both encode "letter does not change / letter stays with her." The difference: `traveling-back-to-her-unchanged` captures the letter's return-journey quality (it went to the officer and came back the same); `still-in-her-fist-at-the-threshold` captures the letter's persistence INTO a new scene (she's entering the sept still holding it). These are distinct events: one is about the object's failure to transform during the confrontation; the other is about the object's persistence past the confrontation into the close. Semantically non-overlapping at the event-level, though adjacent in register.

**AP11 question:** AP11 says "tokens appended via `++` that duplicate tokens already in the existing bundle." The rubric says "token-set difference required." The formal test is token-string difference. The semantic question is not formally required by AP11 — but see SEAM 4 for whether semantic-overlap should be the correct test.

**Verdict: MODERATE seam under semantic-overlap reading. Survives string-overlap test but is the strongest AP11-semantic-overlap candidate in the file.**

---

### Entry 10 — `@77 actor:taylor-hebert-westeros ++ the-septon-as-absence`

**Seam: THIN**

Phase 2 audit marked CORRECT. New tokens `[the-door-she-can-open-after-the-machine-leaves, the-return-to-find-what-waits]` checked against existing bundle `[what-he-could-not-give, the-closed-doors-as-answer, kindness-running-out-before-it-could-hold, the-letter-she-prepared-that-did-not-fit]`.

Semantic-overlap press: `the-closed-doors-as-answer` (pre-load) vs `the-door-she-can-open-after-the-machine-leaves` (new). These are not merely non-overlapping — they are INVERSIONS: one records the door she could NOT open (septon's door during the confrontation); the other records the door she CAN open (same door, post-officer-exit). This is a legitimate semantic extension, not a semantic duplicate. Passes.

AP8 press: `the-door-she-can-open-after-the-machine-leaves` — 9-word compression. Is this a noun-phrase or a sentence? "the door [that] she can open after the machine leaves" — this is a relative clause compressed into a hyphenated token. It contains a temporal clause ("after-the-machine-leaves"). The rubric's AP8 allows "short clausal compression bound by hyphens." The temporal clause is compressed but present. This is the AP8 boundary case. Compare to `traveling-back-to-her-unchanged` (acceptable, 4 words) vs `the-door-she-can-open-after-the-machine-leaves` (9 words). See SEAM 6.

**Verdict: THIN seam on AP11-semantic. MODERATE seam on AP8 token-length (9-word token at the AP8 boundary).**

---

### Entry 11 — `@64 actor:census-officer ++ the-machinery-arrives`

**Seam: THIN**

Phase 2 audit marked CORRECT. New tokens `[the-two-parallel-lines-as-notation-not-judgment, the-annotation-that-travels-with-her-name]` checked against existing bundle `[efficient-not-hostile, procedure-requires-no-malice, the-ledger-as-weapon, bureaucratic-momentum-indifferent-to-the-person]`.

**AP8 press:** `the-two-parallel-lines-as-notation-not-judgment` — 8-word token. Is "as-notation-not-judgment" a compressed phrase or a clause? It reads as a noun-phrase with a predicate-nominative compression (X as Y-not-Z). The token describes the annotation as a category distinction, not a sentence. This is strong word-algebra: `the-two-parallel-lines` is the noun; `as-notation-not-judgment` is the compressed predicate-as-modifier. Passes AP8.

**Semantic-overlap press:** The pre-loaded bundle `the-ledger-as-weapon` partially overlaps in register with `the-two-parallel-lines-as-notation-not-judgment`. But the registers are distinct: `the-ledger-as-weapon` encodes the structural/systemic quality of bureaucratic violence; `the-two-parallel-lines-as-notation-not-judgment` encodes the officer's specific act as administratively-routine (not-judgment), which is precisely the qualitative-consequence of state-update:10. Passes.

**Verdict: THIN seam. Entry 11 survives hostile review.**

---

## SKIP-MISSED seam analysis

### Skip-1 — Mira `++` on `the-yard-as-witness`

**Tag: MODERATE**

Mira's pre-loaded bundle: `[the-ask-that-came-to-her, the-yard-stones-she-looked-at, the-officer-still-present-when-she-said-nothing, the-cost-she-assessed-before-she-decided, self-preservation-in-a-hierarchical-world]`.

The Phase 2 audit (per-skip section) judged: "pre-load may cover it." Press: `feeling:1` fires at @6 (`mira-stonefield: her eyes find the door before they find the wards | expressed: partial`). This is mira's somatic tell AT THE EPISODE OPEN — before the E5 event. The rubric's cross-facet contract says vibes can co-fire on feeling: a feeling-fire can license a `++` if it provides durable-consequence tokens not in the pre-load. Does feeling:1 add anything? The @6 somatic tell captures Mira's orientation-reflex (door before wards). Her pre-loaded `the-yard-as-witness` bundle focuses on the decision-moment (the-cost-she-assessed, self-preservation). The @6 tell is EARLIER in episode time than the yard-witness event and establishes that Mira's awareness was already threat-oriented when Taylor approached. A possible non-duplicate token: `the-door-already-marked-before-the-ask` or `exit-located-before-the-weight-arrived`. These would add the pre-positioning register not present in the existing bundle.

**Verdict: MODERATE SKIP-MISSED.** The Phase 2 fork's skip is defensible under a "pre-load covers it" reading, but feeling:1 licenses a non-duplicate token that the Phase 2 fork missed. A `++` extension on mira's `the-yard-as-witness` via `feeling:1` is a legitimate Phase 4 candidate.

---

### Skip-2 — Edric `++` on `the-yard-as-witness` via state-update:9

**Tag: STRONG**

Edric's pre-loaded bundle: `[the-officer-at-the-gate, the-look-he-gave-the-officer-then-taylor, the-door-he-stepped-back-through, the-math-he-ran-before-he-moved, one-exit-and-he-used-it]`.

State-update:9 fires: `actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)`. This is a confirmed sublocation change: Edric moves THROUGH the sept door at @57. His pre-loaded bundle includes `the-door-he-stepped-back-through` — but this was authored at activation-time as an anticipated event, not an on-screen-confirmed-sublocation-change. The state-update confirms the sublocation change with specific spatial precision: he is now inside the sept. The corpus's gold-standard entry 15 cites `state-update:9` as the licensing event for edric's `the-yard-as-witness` fire.

**Critical distinction:** The pre-loaded bundle `one-exit-and-he-used-it` encodes the exit as a conceptual fact. State-update:9 confirms the sublocation change as a mechanical state change — edric is now in `sept interior`. A `++` extension can add the sublocation-confirmation register: `the-sept-interior-as-exit-destination` or `sublocation-confirmed-not-returned`. These are genuinely non-duplicate tokens derived from state-update:9's specific data.

The Phase 2 audit (per-skip section) noted: "state-update:8 (edric sublocation change at @57)" — this should be state-update:9, which is the correct entry (state-update:8 is `studio.actors_in_yard` composition delta; state-update:9 is edric's sublocation change). The audit's `state-update:8` citation is a minor error that does not change the finding. The relevant entry is state-update:9.

**Verdict: STRONG SKIP-MISSED.** Edric `++ the-yard-as-witness` licensed by `state-update:9` is a genuine skip. The pre-loaded `one-exit-and-he-used-it` does not cover the sublocation-confirmation register. Phase 4 should add this entry.

---

### Skip-3 — Actor:taylor `++` on `the-naming`

**Tag: MODERATE**

Taylor's pre-loaded bundle: `[giving-her-name-aloud-to-a-ledger, the-moment-the-window-closes, the-irrevocable-action-she-takes-herself, she-said-it, no-going-back-in-that-specific-direction]`.

State-update:7 fires: `actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible`. This is the primary licensing event. The pre-loaded bundle captures the experiential quality of the naming (she said it; irrevocable). What the bundle does not capture: the SPECIFIC ADMINISTRATIVE LABEL — `provisional-labor-eligible`. The rubric's AP2 prohibits restating the state fact as a vibe. But the vibe layer derives QUALITATIVE CONSEQUENCE from the label. The qualitative consequence of `provisional-labor-eligible` not captured in the pre-load: the category-placement (not-ward, not-freeborn; the administrative liminal state). Possible non-duplicate token: `the-category-she-was-placed-in-not-chosen` or `provisional-as-permanent-until-proven-otherwise`.

The phase2-audit flags this as "flag-level" — pre-load may cover it. Press: the pre-load covers "the act of saying" but not "the category into which the saying placed her." These are distinct qualitative consequences.

**Verdict: MODERATE SKIP-MISSED.** Taylor `++ the-naming` via `state-update:7` for the category-placement register is a Phase 4 candidate. Not as strong as the edric case because the pre-load already encodes the event's primary impact.

---

### Skip-4 — `loc:westerosi-smallfolk-village-common` for events beyond E1

**Tag: THIN**

Entry 7 fires `the-machinery-arrives` on the location. The E5 event (yard-witnesses-decline-help) also occurs in this location. Should the location receive a second keyword for E5? Candidate: `loc:westerosi-smallfolk-village-common + the-yard-as-witness`.

Press: The E5 event is a social dynamics event between characters, not an event that changes the location's qualitative character. The location already absorbs the E1 event via `the-machinery-arrives`. The E5 event's qualitative consequence is primarily borne by the characters, not the space. The rubric's AP9 says prefer entity targets — this is exactly the case where the entity targets (actor:mira, actor:edric) carry the consequence and the location does not.

**Verdict: THIN SKIP-MISSED.** Skipping the location for E5 is defensible. Not a Phase 4 candidate.

---

### Skip-5 — `prop:oc-letter` vibe-set

**Tag: THIN**

The Phase 2 audit notes prop:oc-letter card is not yet authored (margit referral outstanding). The corpus marks this as optional. No active-project prop vibe file exists to check for pre-load. Absence is contingent on margit referral resolution.

Press: The letter is a load-bearing prop in entries 3 (episode-scope the-letter) and 9 (taylor ++ the-letter). If the prop card is authored, the prop should receive its own `+the-letter` vibe entry with prop-perspective tokens (the-object-that-cannot-be-received, the-ward-document-in-smallfolk-context). These would bias the studio fork's prop-state descriptions.

**Verdict: THIN SKIP-MISSED (contingent). Becomes MODERATE if margit referral resolves before Phase 5 ship.**

---

## SEAM 2 — Episode-scope pre-load entries 2–6: Salvage summary

Under reading (a) — the recommended rubric reading — all five entries (2–6) are faults. Salvage path per entry:

| Entry | Salvage as `++`? | Non-duplicate tokens available? | Verdict |
|---|---|---|---|
| 2 (episode + the-machinery-arrives) | Yes | Yes — annotation exits, ledger-travels-sealed from @64 | SALVAGEABLE as `++` anchored to @64 |
| 3 (episode + the-letter) | Yes | Yes — letter-enters-sept, carried-through-threshold from @77 | SALVAGEABLE as `++` anchored to @77 |
| 4 (episode + the-naming) | Marginal | Possible — form-acceptance-register, dictated-as-fact from @48 | MARGINAL — delete is safer unless a strong token is identified |
| 5 (episode + the-septon-as-absence) | Weak | Possible — door-opened-after-machine-leaves from @77 | WEAK — delete is safer unless anchored to @77 |
| 6 (episode + the-yard-as-witness) | Yes | Yes — spatial-sequencing tokens (refusal-with-officer-present, edric-after-gate-cleared) from @52–@57 | SALVAGEABLE as `++` anchored to @57 |

Three of five (entries 2, 3, 6) are clearly salvageable as `++` with non-duplicate tokens. Entries 4 and 5 may be deleted without losing coverage (the entity-target fires and pre-load already cover the qualitative range).

---

## SEAM 3 — Co-witness `++` extensions (mira / edric)

See SKIP-MISSED seams above. Summary:

- **Edric `++` the-yard-as-witness via state-update:9:** STRONG SKIP-MISSED. The sublocation-confirmation register is genuinely non-duplicate. Phase 4 should add.
- **Mira `++` the-yard-as-witness via feeling:1:** MODERATE SKIP-MISSED. The pre-positioning register (door-already-marked before the ask) is non-duplicate. Defensible addition.

The Phase 2 fork's conclusion that "mira/edric pre-loads are complete" is incorrect for edric (state-update:9 adds sublocation-confirmation not in pre-load) and partially incorrect for mira (feeling:1 adds pre-positioning register). The Phase 2 audit's flag-002 correctly flagged these but underrated the edric finding (should have been a fault-level skip under strict fan-out coherence, given state-update:9 is the canonical anchor for edric's E5 action and is not reflected in his pre-loaded bundle).

---

## SEAM 4 — Token-overlap ambiguity on AP11 (entries 8–11): string-overlap vs semantic-overlap test

**Tag: MODERATE (rubric must commit)**

The Phase 2 fork claimed "no token-overlap" via string-overlap check. The question: does AP11 require string-overlap non-duplication or semantic-overlap non-duplication?

**String-overlap case:** AP11 is written as "tokens appended via `++` that duplicate tokens already in the existing bundle." The word "duplicate" in the context of token-algebra most naturally means "exact string match." This is a mechanical, auditor-checkable test. Semantic overlap would require judgment about meaning — which is not mechanical.

**Semantic-overlap case:** The purpose of `++` is to add *new information* to the vibe-set. If a token is semantically redundant with an existing token (same qualitative consequence, different words), the downstream operator reads a redundant bias — not a genuinely extended model of the target. The facet's purpose is operator-bias precision; semantic duplicates degrade that precision.

**Critical case — entry 9:** `traveling-back-to-her-unchanged` (pre-load) vs `still-in-her-fist-at-the-threshold` (new token). String test: PASS (no overlap). Semantic test: MARGINAL — both encode letter-does-not-transform, but at different event-frames (return-journey vs episode-close persistence). The events are distinct: one is the letter's failure during the confrontation; the other is the letter's persistence into the sept. A downstream dialogue-writer reading `still-in-her-fist-at-the-threshold` would generate a different bias (Taylor entering the sept still holding the letter, a potential scene-open image) than `traveling-back-to-her-unchanged` (the confrontation-register bias). These generate distinct operator behavior. Passes semantic-overlap test on this specific case.

**Rubric recommendation:** Commit to string-overlap as the formal AP11 test, with a supplemental advisory: "Where new tokens are semantically adjacent to existing tokens (same register, different event-frame), authors should add a comment-line justifying the event-frame distinction." This is not a blocking gate but an authoring-quality signal.

**Verdict on entries 8–11 under semantic-overlap:** All four pass. Entry 9 is the closest case and provides the justification for why string-overlap is the right formal test — semantic adjacency at different event-frames is legitimate extension, not duplication.

---

## SEAM 5 — `loc:` pre-load gap

**Tag: MODERATE**

**Confirmed: location vibe-set is genuinely empty.** `active-project/staff/studio/vibes.md` has no per-location vibe sections (only episode/season/series scope sections). No `active-project/warehouse/` location vibe file for `westerosi-smallfolk-village-common`. The library card carries no VIBES section. Gate-2 confirmed: the `+` op in entry 7 is correct.

**Adjacent-location gap press:** The `studio/vibes.md` file carries `harrenhal: [cursed-ground, ambition-burned, ...]` in the series-scope VIBES section. `loc:harrenhal-exterior` does not appear in the s01e01 canon event set — but the SERIES_VIBES and SEASON_1_VIBES in `studio/vibes.md` carry `harrenhal-close: [the-castle-in-peripheral-vision, wrong-scale-every-day, ...]`. These are scope-level vibes, not location-entity vibes. The question: should `loc:harrenhal-exterior` have received an entity-level vibe-fire from the SEASON_1_VIBES content?

Under AP9, if `harrenhal-close` truly belongs to `loc:harrenhal-exterior` as an entity, the season/series scope entries are AP9 violations — they should be location-entity fires. However: the s01e01 episode takes place at the smallfolk village, not at Harrenhal. Harrenhal is in-peripheral-vision (thematic presence, not on-stage). A location entity fire requires the location to be on-stage or affecting on-stage actors in an on-screen event. Harrenhal's presence in s01e01 is ambient and off-screen. Scope-level vibes are the correct target for off-stage ambient. AP9 does NOT fire here.

**Other on-stage-adjacent location gap:** The sept itself (`loc:sept-interior` if such a card exists) receives Taylor in state-update:12 (@77 sublocation change). Does the sept receive a vibe fire? The sept is the destination of Taylor's episode-close journey; state-update:9 also places Edric inside the sept. The sept as a location may warrant a vibe fire for the-septon-as-absence (the sept IS where the septon is failing; it is the charged space). If a `loc:sept-interior` card exists and its vibe-set is empty, a `+the-septon-as-absence` or `+the-protector-failing` fire is warranted.

**Verdict: MODERATE SKIP-MISSED candidate on `loc:sept-interior` if the card exists.** Phase 4 should verify whether a sept location card exists and whether the sept warrants a vibe-fire for E4 / E5 outcomes.

---

## SEAM 6 — AP8 multi-clause token length (entries 8, 10, 11)

**Tag: MODERATE (rubric must commit heuristic)**

The rubric's AP8 says: "Tokens are hyphenated word-algebra only. Multi-clause-as-token forbidden. Maximum: a noun-phrase or short clausal compression bound by hyphens."

Tokens at or near the length boundary:

| Entry | Token | Word-count | Structure | AP8 verdict |
|---|---|---|---|---|
| 8 | `the-marks-beside-her-name-invisible-to-her` | 8 | noun-phrase + participial | PASS (noun-phrase structure) |
| 8 | `the-notation-the-machine-added-without-her-knowledge` | 8 | noun-phrase + relative clause + PP | BORDERLINE (relative clause compressed) |
| 10 | `the-door-she-can-open-after-the-machine-leaves` | 9 | noun-phrase + relative clause + temporal clause | BORDERLINE (two compressed clauses) |
| 11 | `the-two-parallel-lines-as-notation-not-judgment` | 7 | noun-phrase + as-predicate compression | PASS (no clause structure) |

**Borderline cases analysis:**

`the-notation-the-machine-added-without-her-knowledge` (entry 8): "the notation [that] the machine added without her knowledge." This is a relative clause ("the machine added") plus a prepositional phrase ("without her knowledge"). Two subordinate elements, but both compressed into a noun-phrase-with-modifier form. The rubric's example of an AP13 violation: `the-officer-was-efficient-and-she-knew-it` — this is explicitly sentential (subject + predicate + coordinate clause). The borderline token is NOT sentential (no standalone predicate; it is the object of an implied "notation [that+VP]"). BORDERLINE-PASS.

`the-door-she-can-open-after-the-machine-leaves` (entry 10): "the door [that] she can open after the machine leaves." Two compressed clauses: relative + temporal. This is longer than any accepted comparable token in the locked facets. The rubric says "short clausal compression" — "short" is the operative word. This token may exceed "short." However, the semantic compression is legitimate: the token encodes a specific inversion-event (she-opens-the-door-the-septon-never-could) in a way that no shorter token would capture. This is a judgment call.

**Recommended heuristic for Phase 4 rubric commit:**

"Token maximum: 7 hyphenated segments. Tokens up to 7 segments are presumed word-algebra. Tokens of 8–9 segments require structural justification: the token must be a single noun-phrase with compressed modifiers (participial, prepositional, or as-predicate), not a sequence of clauses. Tokens of 10+ segments are refused as AP8 violations unless demonstrably a single noun-phrase with a single compressed modifier. The test is NOT word-count alone but sentence-parsability: if the token can be parsed as a full sentence with subject, verb, and object, it fails AP8 regardless of length."

Under this heuristic: all four borderline tokens above pass (none is parsable as a complete sentence; all are noun-phrases with compressed modifiers). The heuristic gives a principled basis for future review without setting an arbitrary length cap.

**Verdict: MODERATE seam. Rubric must commit a token-length heuristic or explicitly state that the prose-vs-word-algebra test is structural (sentence-parsability) rather than length-based. The current AP8 text implies length-based but does not define it.**

---

## SEAM 7 — Cross-facet contract pre-render hazard

**Tag: STRONG**

The Phase 2 `++` extensions (entries 8, 9, 10, 11) add new tokens to Taylor's and the census-officer's vibe-sets. The downstream locked facets (feeling, memory, state-updates) were authored BEFORE the vibes-updates facet. The question: do the `++` extensions retroactively change what the locked facets should have produced?

**Formal framing:** The vibes-updates facet is UPSTREAM of the dialogue-writer, studio, feeling-fork, and NI-fork. But the feeling/memory/state-updates facets are ALSO upstream of those same operators, and they are already locked. The vibes-updates facet does not cite or change locked upstream facets — it runs in parallel. The concern is: if the dialogue-writer fork reads Taylor's vibe-set (which now includes `++` extensions via entries 8–10) when generating s01e01 dialogue, will it produce different output than the s01e01 facets (feeling, memory) that were generated without those extensions?

**Answer:** s01e01 facets are already locked. The locked facets DO NOT need to be re-run because they are the source documents — they are not rendered output that could differ. The `++` extensions add tokens that the locked facets cited as their OWN licensing events (state-update:10 licensed entry 8; feeling:1 licensed the mira/edric connections; etc.). The locked facets were authored CORRECTLY without reading the vibes-updates facet, because the vibes-updates facet is a WRITE-side product, not a read-side input to same-episode facets. The read-side consumers are the SHOOT-phase operators (dialogue-writer, studio) in future episodes.

**The real hazard:** If s01e01 were to be RENDERED (stitcher pass) after vibes-updates ships, the stitcher reads the vibe-set. The `++` extensions added by entries 8–11 add nuance (the-marks-beside-her-name-invisible-to-her; still-in-her-fist-at-the-threshold) that was not available when the feeling/memory facets were authored. Could a stitcher produce different prose at @64 or @77 knowing those vibe-extensions?

**Verdict:** STRONG seam in the abstract, but the answer is no-retroactive-invalidation for a specific reason: the locked facets are authoritative for their own scope. The vibes-updates `++` extensions add operator-bias context for FUTURE episodes (s01e02+). The locked s01e01 facets do not change. A stitcher running a FIRST-RENDER of s01e01 would read the updated vibe-set; but since the feeling/memory/state-updates facets already capture the same events at their own layers (the `++` extensions are derived FROM those facets' licensed events), the stitcher reading both the locked facets and the updated vibe-set should produce coherent, non-contradictory output — the vibe adds a bias-layer; the locked facets add the content-layer. The two layers do not conflict.

**However:** This is a structural assumption that the pipeline has not formally stated. Phase 4 should add a rubric clause: "Vibes-updates `++` extensions that derive from locked upstream facets do not retroactively invalidate those facets. The vibe-set provides bias-layer context; the locked facets provide content-layer authority. Stitcher reads both simultaneously; conflicts are resolved in favor of the content-layer facet."

---

## Summary cross-cutting seam table

| Seam | Tag | Phase 4 action required |
|---|---|---|
| RF-001: world-build pre-load vs in-episode license-event | LOAD-BEARING | Rubric clause required; commit reading (a); restate corpus |
| Per-entry entries 2–6 (AP5/gate-2) | STRONG | Revise to `++` or delete per salvage table above |
| Entry 7 vs entries 2+6 AP9 interaction | MODERATE | Phase 4 should confirm whether episode-scope `the-machinery-arrives` is fully redundant with loc+actor entity fires |
| Entry 8 AP8 borderline tokens | MODERATE | Token-length heuristic commit at Phase 4 |
| Entry 9 semantic-overlap AP11 | MODERATE | String-overlap formal test commit; advisory for semantic-adjacent tokens |
| Entry 10 AP8 borderline (9-word token) | MODERATE | Same as entry 8 heuristic |
| Edric `++` the-yard-as-witness (SKIP-MISSED) | STRONG | Add entry in Phase 4 via state-update:9 |
| Mira `++` the-yard-as-witness (SKIP-MISSED) | MODERATE | Phase 4 candidate via feeling:1 |
| Taylor `++` the-naming (SKIP-MISSED) | MODERATE | Phase 4 candidate via state-update:7 (category-placement register) |
| loc:sept-interior gap (SKIP-MISSED) | MODERATE | Verify card existence; if present, fire warranted |
| Cross-facet pre-render hazard | STRONG | Rubric clause required: `++` extensions do not invalidate locked upstream facets |
| AP8 prose-vs-word-algebra commitment | MODERATE | Rubric must define test as structural (sentence-parsability) not length-based |
