---
report: facets-final-audit
chapter: b01c01
timestamp: 2026-05-24
audit-classes-run: 11
HARD: 1
SIGNAL: 8
earth-bet-hits: 0
cite-graph-coherence: PASS
scene-map-coverage: PASS
cycle: 3-post-fixer-post-delete
cycle3-scope: interest-narrator (narrator:5/narrator:7 recasts) + vibes (B1–B5 token/license edits) + dialogue-coll (cap-burn DELETE of coll-net-mender-flea-bottom:1 @8)
---

# Facets Final Audit — b01c01 (Cycle 3, Post-Fixer, Post-DELETE)

Cycle-3 changes since cycle-2 audit:
- **A1**: narrator:7 @20 content recast — ledger-satisfaction → ledger-cost register.
- **A2**: narrator:5 @24 content recast — author-annotation → completed-fact pre-calc register.
- **B1**: vibes:2 @6 license trim — `state-update:2` removed from `licensed-by` chain.
- **B2**: vibes:5 @13 token #3 replacement — `confirmed-on-screen-b01c01` → `overhead-that-runs-without-charging-the-ledger`.
- **B3**: vibes:7 @26 tokens #1 and #3 replacement — `first-on-screen-naming-of-what-she-saw` → `names-the-proximate-not-the-meaning`; `the-flies-report-as-demonstration` → `withholds-the-frame-delivers-the-data`.
- **B4**: vibes:8 @26 two token replacements — `the-follow-up-withheld-on-screen` → `question-the-ward-keeps-to-itself`; `first-confirmed-shape-of-the-mutual-silence` → `shape-of-the-mutual-silence-going-forward`.
- **B5**: vibes:9 @27 token replacement — `the-anomaly-confirmed-on-screen` → `the-gap-in-the-ledger-that-does-not-close`.
- **C1-DELETE**: `coll-net-mender-flea-bottom:1 @8` deleted from dialogue file and sidecar; deletion markers in place per A5; cite-index rebuilt; `[coll-net-mender-flea-bottom:1]` token AUTO-STRIPPED from proto-line @8.

---

audit:
  scope: chapter
  target: b01c01
  timestamp: 2026-05-24

---

## STRUCTURAL (Citation resolution and bidirectional integrity)

    - id: fault-001
      type: pass
      convergence-with-cycle2: fault-001/002/003 (all REPAIRED)
      what: cite-index bidirectional integrity re-verified post-cycle-3 edits. All back=Y entries confirmed. No new stale anchor introduced by A1/A2 NI content recasts (no anchor changes; IDs narrator:5 and narrator:7 both present in cite-index at their declared anchors @24 and @20 respectively). No new stale anchor introduced by B1–B5 vibes token/license edits (no anchor changes; vibes:2 through vibes:9 all resolve in cite-index). Proto-line @8 now bare (coll-net-mender-flea-bottom:1 stripped); cite-index rebuilt and confirms @8 has no remaining `<character-slug>:<id>` citations — consistent with deletion.
      why: PASS for all cycle-2 STRUCTURAL REPAIRED entries. No cycle-3 edit introduced new STRUCTURAL faults in the bidirectional graph.

    - id: fault-030
      type: fault
      what: |
        [dialogue:--] @8 — dialogue-coverage — bare speech bone: coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac.
        Proto-line @8 (`coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac`) is a speech bone. Phase 0 inventory listed `coll-net-mender-flea-bottom` in `speakers` and @8 in `speech_bones`. Post-DELETE, proto-line @8 carries zero `<character-slug>:<id>` citations; cite-index confirms `@8` appears in the "Bare protolines" list with no facet entries.
        Per `.claude/commands/and-facets.md` § CONSTRAINT § dialogue-coverage: "Bare speech bone (a `<X> speaks to <Y>` proto-line with zero dialogue citations post-R2) → HARD per bone. Emit `[dialogue:--] @<proto> — dialogue-coverage — bare speech bone: <subject> speaks to <object>`."
        ACCEPTED-AT-CAP-BURN per URI-FACETS-CAP-BURN-SEMANTICS A2, cycle-3 DELETE of `[coll-net-mender-flea-bottom:1] @8`. Trade-off documented in sidecar deletion marker and fixer log C1. Cap-burn report (pending write) will formalize. This HARD does NOT route to fixer. The bare-speech-bone condition is structurally inevitable post-DELETE; no further remediation attempt is permitted within this cap-burn cycle.
      why: Structural gate URI-DIALOGUE-COVERAGE-GATE requires every speech bone carry ≥1 dialogue citation post-R2. The DELETE removed the only citation. Downstream consequence: /and-stitch Phase 0 dialogue-coverage gate will surface this bare bone; the stitcher must be made aware via the cap-burn record that @8 is a deliberate bare-bone trade-off. Stitcher cannot infer dialogue for @8 from the blank anchor; the scene will render @8 as a non-dialogue action beat (bones-only rendering).
      criteria: NOT ROUTED TO FIXER. Accepted at cap-burn. Cap-burn report must note the trade-off for /and-stitch Phase 0 guidance.

    - id: fault-031
      type: fault
      what: |
        [dialogue:--] @-- — dialogue-coverage — speaker file body empty: coll-net-mender-flea-bottom.
        `theater/dialogue/coll-net-mender-flea-bottom.md` exists on disk but contains only a deletion marker (no `<id> @<anchor>` entries). Phase 0 `speakers` inventory includes `coll-net-mender-flea-bottom`.
        Per § CONSTRAINT § dialogue-coverage: "Missing speaker file (a speaker slug from Phase 0 inventory with no dialogue file on disk) → HARD per speaker."
        Auditor interpretation: the gate language reads "missing file" literally; the file exists on disk. However, the gate's purpose is to confirm every speaker slug has ≥1 dialogue entry post-R2. A deletion-marker-only file is functionally equivalent to a missing file for the gate's operative requirement (non-empty body). The gate language in Phase 6 persistence check reinforces this: "every speaker in Phase 0's `speakers` inventory, `theater/dialogue/<speaker-slug>.md` exists with ≥1 entry." The "≥1 entry" clause is not satisfied by a deletion-marker-only body.
        This finding therefore classifies as a second HARD. Auditor notes the edge case: the file IS present on disk; the Phase 0 "missing speaker file" language is met only if read as "present with ≥1 entry." Auditor applies the ≥1-entry reading as the operative standard.
        ACCEPTED-AT-CAP-BURN per URI-FACETS-CAP-BURN-SEMANTICS A2, same DELETE event as fault-030. This HARD does NOT route to fixer.
      why: Phase 6 persistence gate explicitly requires `theater/dialogue/<speaker-slug>.md` exists with ≥1 entry. The Coll speaker file has 0 entries post-DELETE. This will cause Phase 6 to fail the dialogue-coverage gate check unless the cap-burn acceptance is explicitly carried into the Phase 6 audit. The phase-6 orchestrator must be notified that Coll's speaker file is cap-burn-empty and the gate is intentionally unmet for this speaker.
      criteria: NOT ROUTED TO FIXER. Accepted at cap-burn alongside fault-030. Cap-burn report must note both gate failures (bare speech bone + empty speaker file) for /and-stitch Phase 0 and Phase 6 guidance.

---

## FREQUENCY-BAND

    - id: fault-005
      type: flag
      convergence-with-cycle2: fault-005
      what: memory-b01-c01.md; 2 entries on 27 bones = 7.4%; sparsity target 1-5% (0-1 entries); above-band defense (doubled-register mandate) on-file per R2.2 judge.
      why: Unchanged from cycle-2. Defense on-file and rubric-grounded. Advisory only. No cycle-3 edit affected memory.

    - id: fault-006
      type: flag
      convergence-with-cycle2: fault-006
      what: feeling.md (taylor-hebert-kl-122ac slice); 2 entries on 27 bones = 7.4%; sparsity target 2-5%; V3 feel-as-spine carve-out defense on-file.
      why: Unchanged from cycle-2. Defense on-file. No cycle-3 edit affected feeling.

    - id: fault-007
      type: flag
      convergence-with-cycle2: fault-007
      what: location-state-b01-c01.md; 7 entries on 27 bones = 25.9%; standard rubric guidance 4-9%; continuity-carry + flat-low fusion-eligible-run defense on-file.
      why: Unchanged from cycle-2. Advisory only. No cycle-3 edit affected location-state.

---

## METADATA-INCONSISTENCY

No new metadata inconsistencies introduced by cycle-3 edits. NI file header accurately documents the semicolons-now-permitted state (post "Remove semicolon check" directive) and the cycle-2 fixer scope. The cycle-3 content recasts (narrator:5/7) do not affect file-header metadata claims. Vibes file header carries no explicit entry-count attestation that would be invalidated by B1–B5 token edits. Coll dialogue file and sidecar both carry the deletion marker per A5 canonical format.

fault-008 (METADATA-INCONSISTENCY — feeling-wren per-slice stale ref): Previously HARD in cycle-2; carried as LANDED per cycle-2 routing. Not re-verified in this cycle-3 pass (no cycle-3 edit touched the feeling-wren per-slice file). Status from cycle-2 fixer dispatch: confirmed LANDED.

    - id: fault-032
      type: pass
      what: NI file header cycle-2 summary correctly states "rewrote narrator:2/3/6/7"; does not claim narrator:5/7 were in cycle-2 scope. Cycle-3 recasts of narrator:5 and narrator:7 are not reflected in the header (the header records the cycle-2 history only). No false attestation created — the header does not claim a state that post-cycle-3 is false.
      why: PASS. No metadata inconsistency.

---

## CONSTRAINT (Earth-Bet scan + dialogue-coverage)

Earth-Bet proper-noun scan (all facet files, post-cycle-3 content): PASS. The A1 recast of narrator:7 ("the day held under the count she had been running and the weight of what she had not done was in the count") contains no Earth-Bet proper nouns or category-nouns. The A2 recast of narrator:5 ("she had already mapped the observation-radius and run the circuit count before the held label registered that she had") contains no Earth-Bet terms. B1–B5 vibes token replacements contain no Earth-Bet terms. earth-bet-hits: 0.

Extended category-noun sweep (new tokens): `overhead-that-runs-without-charging-the-ledger`, `names-the-proximate-not-the-meaning`, `withholds-the-frame-delivers-the-data`, `question-the-ward-keeps-to-itself`, `shape-of-the-mutual-silence-going-forward`, `the-gap-in-the-ledger-that-does-not-close` — all Planetos-register compound noun-phrases; no parahuman vocabulary, no PRT rating-class nouns, no Earth-Bet proper-noun substrings. PASS.

Dialogue-coverage gate: see fault-030 and fault-031 above (both HARD, both ACCEPTED-AT-CAP-BURN).

---

## RUBRIC-FIDELITY

### narrator:7 @20 (A1 recast)

    - id: fault-033
      type: pass
      what: narrator:7 @20 post-A1: "the day held under the count she had been running and the weight of what she had not done was in the count." One-observation-per-fire check: the entry fires one observation — the cost register surfacing as the weight of the withheld action carried in the ledger. "The day held" (the prohibition intact) and "the weight of what she had not done was in the count" (the cost lives in the ledger) are two clauses expressing the same observation (the discipline's continuing load), not two stacked independent observations. PASS per new §Form rule. No AP-10 inverted-predicate: subject is "the day" (not a negation-first clause); predicate is "held" (stative verb — permitted); secondary clause subject is "the weight" with straightforward copula. AP-10 does not fire. No Earth-Bet category-nouns. Channel: cost-tracking/ledger-close. No chassis-recurrence — narrator:6 is the inverted-predicate entry (cap consumed); narrator:7 does not use the inverted form. §Form: no semicolon-spine (post-directive permitted anyway). Rubric calibration: "G5 hold-live preserved" per fixer log (cost-tracking still active, not archived) — consistent with the bones-review NOTE-002 requirement.
      why: PASS. A1 recast meets §Form, AP-10 absence, channel diversity, and G5 requirements.

### narrator:5 @24 (A2 recast)

    - id: fault-034
      type: pass
      what: narrator:5 @24 post-A2: "she had already mapped the observation-radius and run the circuit count before the held label registered that she had." One-observation-per-fire check: one pre-calc observation (the assessment already in progress before the held label fires). No stacking. Calibration anchor form: "she had already X-ed" — matches rubric calibration anchor ("she had already counted the four spans of dirt") exactly. "Before the held label registered that she had" is Taylor's own interior discipline catching itself mid-fire — not author-annotation on the fact's generation (the held-label is a first-person interior signal, not an external narrator reporting on the process). No AP-10. No Earth-Bet terms. §Form: single compound pre-calc clause with embedded temporal subordinate — no semicolon, passes post-directive form. Completed-fact register confirmed.
      why: PASS. A2 recast resolves the annotation-register problem from cycle-2. Structural earning (held-label fires) preserved per fixer pre-validation.

---

## AP-SCAN

### AP8 sentence-parsability — cycle-3 vibes tokens

    - id: fault-035
      type: pass
      what: vibes:5 token `overhead-that-runs-without-charging-the-ledger` — AP8 check. Token structure: "overhead" = head noun; "that runs without charging the ledger" = relative clause modifier. No standalone subject + finite-verb main predicate functioning as a sentence. Does not parse as an independent sentence; no AP8 trigger.
      why: PASS.

    - id: fault-036
      type: pass
      what: vibes:7 token `names-the-proximate-not-the-meaning` — AP8 check. Token structure: verb-led ("names"), but this is a participial/appositive form serving as a noun-phrase descriptor, not a standalone imperative or declarative sentence with an independent subject. Precedent: `holds-the-eyes-does-not-file` in vibes:9 was accepted under the same rubric (two-verb compound describing a relational disposition; the subject is the implied actor-entity of the vibes target, not an independent grammatical subject rendering the token a sentence). `names-the-proximate-not-the-meaning` follows the same construction: verb-led compound describing a noticing-class disposition. Does not constitute a standalone subject+finite-verb main predicate sentence. AP8 does NOT trigger.
      why: PASS. Precedent-consistent with `holds-the-eyes-does-not-file` (vibes:9). Verb-led compound disposition tokens in the vibes facet have an established accepted form where the implied actor-entity is the vibe target, not a rendered grammatical subject.

    - id: fault-037
      type: pass
      what: vibes:7 token `withholds-the-frame-delivers-the-data` — AP8 check. Token structure: two-verb contrast compound ("withholds" + "delivers"). The borderline concern is whether this reads as two independent clauses ("she withholds the frame; she delivers the data") and therefore as a sentence with subject+verb. Analysis: the token has no explicit subject; both verbs are in parallel participial/appositive form naming a reporting-class disposition. The two-verb structure is additive (contrasting aspects of a single behavioral disposition), not two independent predications. Closest comparator: `holds-the-eyes-does-not-file` (vibes:9), which is a two-verb contrast compound accepted as a token. `withholds-the-frame-delivers-the-data` is structurally equivalent: two complementary participial predicates describing one disposition (delivers the datum, withholds the frame). No explicit subject renders it an independent sentence. AP8 does NOT trigger.
      why: PASS. Structurally equivalent to the accepted `holds-the-eyes-does-not-file` precedent. Two-verb disposition tokens with implicit-actor subject are within the established vibes token form.

    - id: fault-009
      type: flag
      convergence-with-cycle2: fault-009
      what: vibes:7 @26 and vibes:8 @26 — two vibe entries targeting actor:wren at the same proto-line. Vibes:7 targets `observation` cluster; vibes:8 targets `silence` cluster.
      why: Unchanged from cycle-2. V1.1 Patch permits distinct-cluster splits. Advisory. Cycle-3 token edits on vibes:7/8 do not alter the dedup status (they are still distinct-cluster entries at the same anchor). No cycle-3 escalation warranted.

### AP8 re-check on pre-existing tokens

    - id: fault-038
      type: pass
      what: vibes:2 @6 `attention-she-does-not-withhold` — re-verified post-B1 license trim. Token unchanged from cycle-2 F3 repair. Noun-phrase structure confirmed. AP8 does not trigger.
      why: PASS. No change to token content from B1 edit.

---

## DEDUP

    - id: fault-039
      type: pass
      what: No new dedup conditions introduced by cycle-3 edits. vibes:7/8 same-anchor dedup advisory unchanged (fault-009 above). vibes:10 @- episode-scope anchor-free entry unchanged.
      why: PASS.

---

## CONTRADICTION

No new contradictions introduced by cycle-3 edits. NI recasts (A1/A2) alter content register, not state assertions. Vibes token replacements (B1–B5) alter disposition encoding, not state-update values. DELETE of coll:1 removes the only Coll dialogue entry; no state contradiction is created (Coll's state-updates file carries no new fields from the removed entry; the REFUSE at @8 was on-disk before the DELETE). PASS.

---

## SUPERFLUOUS

Lonely entries unchanged from cycle-2: loc-state:4 @11, narrator:5 @24, sensory:2 @12, sensory:3 @14, state:3 @7, exposition:2 @4. All pass rubric three-axis test independently. Narrator:5 @24 post-A2 recast: content now explicitly in completed-fact register; structural earning (held-label fires) preserved; the bones-review NOTE carrier function is intact. The entry earns its place on the pre-calc surfacing channel. PASS.

---

## CURVE-SHAPE

Unchanged from cycle-2. All three scenes: rhythm-shape flat-low per scene-map. No peak-bones. dramatic_shape: hinge. Cycle-3 edits do not affect the scene-map or rhythm-shape declarations. Flat-low across all three scenes remains architecturally correct for a hinge-baseline chapter. SHAPE-OK.

---

## TASTE-FLAG

    - id: fault-016
      type: flag
      convergence-with-cycle2: fault-016
      what: Scene-C approach zone (@22-@25) has sparse facet coverage. Unchanged from cycle-2. No cycle-3 edit added coverage to this zone.
      why: Advisory. Deferred-with-attribution per pulp-enthusiast arbiter ruling A (cycle-2 orchestrator-judgment arbitration). The five co-located interiority facets at @26 remain the zone's payload anchor. No escalation.

    - id: fault-017-moot
      type: pass
      convergence-with-cycle2: fault-017
      what: vibes:1 and vibes:2 shared-license advisory (fault-017, cycle-2). The cycle-2 fault-017 TASTE-FLAG flagged vibes:1 and vibes:2 sharing the `state-update:1/state-update:2` license pair. B1 removed `state-update:2` from vibes:2's licensed-by chain. Post-B1: vibes:1 `licensed-by: state-update:1, state-update:2, proto:5`; vibes:2 `licensed-by: state-update:1, proto:6`. The two entries no longer share the full state-update pair — vibes:2 no longer cites state-update:2 at all. The shared-license advisory is now reduced to a single shared source (state-update:1), which is the operative license for both (location arrival). Single shared operative source for two distinct king's-landing cluster extensions is not a dedup concern. fault-017 is MOOT by B1 fix.
      why: PASS. fault-017 resolved by B1. Advisory cleared.

---

## PILE-UP REVIEW

Three pile-ups from cycle-2 remain unchanged in structure. Post-cycle-3 verification:

- **@1** (6 facets: exposition:1, loc-state:1, state:1, state:2, vibes:1, vibes:2): WARRANTED. Chapter-open establishment beat. No change. Cite-index confirms same 6-entry structure.
- **@9** (6 facets: feel:1, mem:1, narrator:2, state:9, vibes:3, vibes:4): WARRANTED. Inverted-establishing-fact anchor. No cycle-3 edit touched this pile-up. earth-bet-clean confirmed (narrator:2 "power" removal from cycle-2 stands).
- **@26** (5 facets: feel:3, narrator:6, vibes:7, vibes:8, wren-stitch-maker-flea-bottom-ward:2): WARRANTED. The payload beat pile-up structure unchanged. B3/B4 token replacements in vibes:7/8 do not alter the co-location count or the warranted classification. Cycle-2 label ambiguity note (feel:3 vs feel:4 cite-index label) unchanged; no cycle-3 edit resolved it; remains low-priority metadata flag.

No new pile-ups. DELETE of coll:1 removes a non-pile-up entry (@8 was never a pile-up anchor); no pile-up structure affected.

---

## Pass-through SIGNAL validation — cycle-2 carry

Reviewing the 9 cycle-2 SIGNAL findings against cycle-3 changes:

| Cycle-2 finding | Cycle-3 status |
|---|---|
| fault-004 (vibes:10 episode-scope anchor-free) | CARRIES. No cycle-3 edit affected vibes:10. Advisory unchanged. |
| fault-005 (memory 7.4% over-band) | CARRIES. No cycle-3 edit affected memory. Defense on-file. |
| fault-006 (feeling/taylor 7.4% over-band) | CARRIES. No cycle-3 edit affected feeling. Defense on-file. |
| fault-007 (loc-state 25.9% over-band) | CARRIES. No cycle-3 edit affected location-state. Defense on-file. |
| fault-009 (vibes:7/8 same-actor same-beat dedup) | CARRIES. Token replacements in B3/B4 do not change the dedup condition; distinct-cluster split still valid per V1.1 Patch. |
| fault-015 (exposition:2 simile AP-3) | CARRIES. No cycle-3 edit affected exposition. Advisory unchanged. |
| fault-016 (scene-C approach zone thin coverage) | CARRIES. No cycle-3 ADD. Deferred-with-attribution per arbiter ruling. |
| fault-017 (vibes:1/2 shared-license advisory) | MOOT. B1 removed state-update:2 from vibes:2 licensed-by. See fault-017-moot above. |
| fault-020 (NI header false attestation + narrator:1/5 semicolons) | MOOT post-directive. Retired by "Remove semicolon check" user directive (cycle-2 post-directive update). Semicolons now rubric-compliant. Header false-attestation resolved post-directive (NI file header was updated per cycle-2 fixer pass). |

Net pass-through: **fault-004, fault-005, fault-006, fault-007, fault-009, fault-015, fault-016** carry as SIGNALs. fault-017 and fault-020 are MOOT. 7 SIGNAL carries.

---

## Fault-021 sensory exemption — re-validation

    - id: fault-021
      type: fault
      convergence-with-cycle2: fault-021 (carried unchanged)
      what: sensory-b01-c01.md; 4 entries on 27 bones = 14.8% against 6% standard ceiling. V3 short-chapter exemption defense on-file; user-adjudicated as substance-grounded exemption (F5 precedent) per cycle-2 orchestrator-judgment arbitration (pulp-enthusiast arbiter ruling A — defer-as-taste with attribution trail). Sensory modality-coverage specialist REVISE carries on record as attribution trail.
      why: No cycle-3 edit affected sensory. The exemption defense, the HARD classification, and the user adjudication are all unchanged. Per task brief: "re-validate fault-021 sensory exemption (still on-file from cycle-2 user adjudication; pulp-enthusiast arbiter ruling A defers shape-level) — leave on the same disposition unless new evidence emerges." No new evidence has emerged. Classification remains FAULT with ACCEPTED exemption defense on-file; this HARD is carried-as-resolved-by-adjudication (not ACCEPTED-AT-CAP-BURN — the adjudication predates the cap-burn). This finding does NOT route to fixer under cycle-3.
      criteria: Disposition unchanged. Rubric disambiguation remains deferred per F5 precedent + pulp-enthusiast arbiter ruling. Not re-routed.

Note on HARD count: fault-021 is a HARD finding with an on-file accepted defense (user adjudication). For cycle-3 HARD counting purposes, the two structurally inevitable bare-bone HARDs (fault-030, fault-031) are the ACCEPTED-AT-CAP-BURN findings. fault-021 is carried-as-adjudicated. All three HARD findings have accepted resolutions; none route to fixer.

---

## Bidirectional-loop convergence

Cycle-2 bidirectional loop was VALIDATED (three shared findings across auditor + audience paths). Cycle-3 re-validation:
- Auditor HARD findings: 1 new (fault-030 bare-speech-bone; ACCEPTED-AT-CAP-BURN) + 1 new (fault-031 empty-speaker-file; ACCEPTED-AT-CAP-BURN) + 1 carried-as-adjudicated (fault-021 sensory).
- Auditor SIGNAL findings: 7 carry-through + 0 new from cycle-3 edits.
- Audience-gate cycle-3 not yet fired. Cycle-2 audience convergence shared findings (fault-017 vibes:2 license / fault-016 scene-C coverage / fault-013 exposition:2 cross-anchor consequence) remain on record. fault-017 is now MOOT (B1 fix landed). fault-016 carries. fault-013 consequence (coll:1 facet-license cross-anchor) is now resolved by DELETE.
- Bidirectional loop convergence: PRESERVED. The cycle-2 VALIDATED status is not degraded by cycle-3 changes. The shared finding set (auditor fault-017 ↔ cape-fic vibes:2 license; auditor fault-016 ↔ sensory-modality-coverage @22-@29; auditor exposition:2 advisory ↔ dark-fantasy dialogue-coll citation-completeness consequence) still forms a valid shared-finding body from the cycle-2 passes. Cycle-3 changes resolve or accept all the structural findings that drove the cap-burn decision. **Bidirectional loop: VALIDATED (cycle-2 trace preserved; cycle-3 changes do not invalidate any shared finding; fault-017 resolved as MOOT; fault-016 deferred-with-attribution).**

---

## Audit Summary (Cycle 3, Post-Fixer, Post-DELETE)

### HARD findings (3 total; 0 route to fixer)

- **fault-030** (STRUCTURAL/CONSTRAINT — URI-DIALOGUE-COVERAGE-GATE bare speech bone @8): `coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac` at @8 has zero dialogue citations post-DELETE. **ACCEPTED-AT-CAP-BURN**. Does not route to fixer. Cap-burn report required.
- **fault-031** (STRUCTURAL/CONSTRAINT — URI-DIALOGUE-COVERAGE-GATE speaker file body empty): `theater/dialogue/coll-net-mender-flea-bottom.md` exists with 0 entries post-DELETE (deletion-marker-only body). Phase 6 persistence gate requires ≥1 entry per speaker. Auditor interprets ≥1-entry clause as operative standard. **ACCEPTED-AT-CAP-BURN**. Does not route to fixer. Cap-burn report must flag for Phase 6 orchestrator.
- **fault-021** (FREQUENCY-BAND — sensory over-ceiling, carried-as-adjudicated): 4 entries at 14.8% against 6% ceiling. V3 exemption defense on-file. User-adjudicated cycle-2; disposition unchanged. Does not route to fixer under cycle-3.

### SIGNAL findings (7 carry-through; 0 new)

- fault-004: vibes:10 episode-scope entry anchor-free. FLAG (no change).
- fault-005: memory 7.4% over-band. FLAG (no change).
- fault-006: feeling/taylor 7.4% over-band. FLAG (no change).
- fault-007: loc-state 25.9% over-band. FLAG (no change).
- fault-009: vibes:7/8 same-actor same-beat dedup advisory. FLAG (no change; B3/B4 token replacements do not alter the condition).
- fault-015: exposition:2 simile AP-3 candidate. FLAG (no change).
- fault-016: scene-C approach zone thin coverage. FLAG (no change; deferred-with-attribution).

### MOOT from cycle-2

- fault-017: vibes:1/2 shared-license advisory — MOOT by B1 fix.
- fault-020: NI header false attestation + narrator:1/5 semicolons — MOOT post-directive (retired cycle-2).
- fault-029: AP-SCAN NI semicolon saturation — MOOT post-directive (retired cycle-2).

### Cleared in cycle-3 by fixer

- fault-017 (vibes:2 non-operative license `state-update:2`): CLEARED by B1.
- vibes:5/7/8/9 provenance tokens (B2–B5): CLEARED — all 5 provenance tokens replaced with disposition tokens encoding durable operator-behavior.
- narrator:7 @20 ledger-satisfaction register: CLEARED by A1 — cost register now surfaces.
- narrator:5 @24 author-annotation register: CLEARED by A2 — completed-fact pre-calc form confirmed.
- Coll facet-license cross-anchor (C1-DELETE): RESOLVED via cap-burn DELETE.
- C0 behavior-card-absence: DISMISSED as path-error (card confirmed at `active-project/actors/coll-net-mender-flea-bottom/card.md`).

### Earth-Bet status

- Proper-noun scan: 0 hits.
- Extended category-noun sweep (all cycle-3 new content): 0 hits.
- Total earth-bet-hits: 0.

### Cite-graph coherence: PASS
### Scene-map coverage: PASS (27/27 bones in exactly one scene; no gaps; no overlaps)

---

## Routing (Cycle 3 — final)

- **fault-030 + fault-031** (bare-speech-bone + empty-speaker-file HARDs): ACCEPTED-AT-CAP-BURN. No fixer dispatch. Cap-burn report must be written to `staff/auditor/facets-cap-burn-b01c01-<timestamp>.md` documenting: (a) coll:1 DELETE + callout chain; (b) bare-speech-bone gate failure at @8 accepted at cap-burn; (c) empty-speaker-file Phase-6 gate failure accepted at cap-burn; (d) trade-off — chapter ships with @8 bone underdialogued for Coll; Coll's on-screen role carried through action bones @3/@4/@20 and exposition:2 @4 gloss; (e) pointer for /and-stitch Phase 0 guidance (treat @8 as bare-bone, no dialogue inference) and Phase 6 orchestrator (Coll speaker file intentionally empty at cap-burn). Rubric-edit Path (b) (upstream-same-scene cross-anchor citation permission) flagged as follow-on per fixer log C1.
- **fault-021** (sensory FREQUENCY-BAND, carried-as-adjudicated): No new action. Exemption defense on-file. Not re-routed.
- **All SIGNAL findings** (fault-004/005/006/007/009/015/016): advisory; carry through to Phase 6 record. No fixer dispatch.
- **AP8 verdicts on borderline tokens** (fault-036/037): PASS. `names-the-proximate-not-the-meaning` and `withholds-the-frame-delivers-the-data` both pass AP8 under the `holds-the-eyes-does-not-file` precedent (verb-led compound disposition tokens with implicit-actor subject; two-verb contrast structure within established form).
