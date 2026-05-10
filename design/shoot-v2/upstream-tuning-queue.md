---
queue: upstream-tuning
date: 2026-05-10
status: ACCRUING — items added as audit / tuning / facet runs surface upstream issues
purpose: collect upstream issues that cannot be fixed at line-level. Do NOT block downstream work; flag and continue.
---

# Upstream Tuning Queue

When facet-tuning or audit runs surface issues that require **upstream intervention** (rubric edits, protoline re-authoring, card authoring, agent-definition changes), they're flagged here rather than blocking the active work. The queue is processed as a separate session.

Categories:

1. **Rubric tuning** — locked rubric files (`design/shoot-v2/rubric-*.md`) need edits validated against tuning corpus.
2. **Protoline upstream** — `/and-protolines-v2` or `/and-season` produced output that doesn't carry the dramatic shape downstream facets need.
3. **Card authoring** — warehouse cards (props, monuments, conditions) referenced as free-text glosses need to be promoted to formal slugs.
4. **Agent definition** — agent permissions (e.g., dramatist Read-only) need adjustment.
5. **Schema** — schema text needs clarification or extension.
6. **Audit** — the audit command itself needs further coverage upgrades.

---

## Open queue items

### URI-001 — Memory rubric V2.1 carry-back (3 audience-confirmed)

- **Category:** Rubric tuning.
- **Source:** `design/shoot-v2/memory-tuning-r2-final.md` Phase 5 audience adjudication, 2026-05-10.
- **Items:**
  1. **Tens=2 zone-class scene-frame anchor.** The quiet-beat test cannot classify a tens=2 beat as rising-edge or trailing-edge without a mechanical scene-frame anchor. Currently relies on judgment. Need a quantified rule for episodes without dramatist-locked scene boundaries.
  2. **Mask-bleed vs clinical-of-the-horrible.** Anti-pattern §10 does not sharply separate somatic-fact registration from mask-bleed (voice-register performance). Rubric needs a positive carve-out definition.
  3. **AP §3a — analytical-frame primary-noun extension.** Anti-pattern §3 (stage-named-cue) covers act-of-remembering labels but not analytical-frame primary-nouns naming the cue's mechanism (map / apparatus / performance / system / mechanism). Extension warranted.
- **Action:** rubric edit + Phase-5 mechanic re-verify on s01e01 corpus + rubric-carry-back validation against next-episode tuning data.
- **Cost:** small. Rubric-only edit; no facet retune needed (lift was already audience-validated under V2).

### URI-002 — Protoline scene-peak coverage gap (s01e01)

- **Category:** Protoline upstream (`/and-protolines-v2` or `/and-season`).
- **Source:** `active-project/staff/auditor/facets-final-audit.md` audit-r3, 2026-05-10. CURVE-SHAPE verdict: SHAPE-FAIL.
- **Issue:** 6 of 8 scenes in s01e01 lack any rung-3 peak with no dramatist-flagged exception. Direct 1→3 jump at @83 with no rung-2 precursor at @81/@82. Episode-level act structure is sound (climax @99, not inverted); failure is scene-level coverage.
- **Where the gap originates:** the protoline file as authored does not carry enough peak-quality beats per scene. Either the scene boundaries need re-thinking (some "scenes" are transit/respite and should be flagged as scene-exceptions), or the protolines need additional charged beats added by screen-writer.
- **Action:** dramatist re-pass on s01e01 protolines with scene-exception authority (allow scenes to be flagged as transit/respite explicitly), OR screen-writer kickback to add peak beats. Update tens facet with re-rated beats. Re-run cite-index and audit.
- **Cost:** medium. Touches protolines + tens facet. Cascade implications for any facet citing affected protolines.
- **Frequency-band linkage:** the tens 1-rung breach-high (77.5% > 75%) and 3-rung breach-low (2.0% < 5%) trace to the same root cause. Resolving URI-002 likely resolves the FREQUENCY-BAND finding too.

### URI-003 — Margit referrals from R1 (cards to author)

- **Category:** Card authoring.
- **Source:** R1 facet authoring reports, 2026-05-10.
- **Items:**
  - Prop card: `oc-account-ledger` (used by env state-updates 4-6 via field-extensions on `prop:oc-account-ledger.{cover-state,entry-state,apprentice-mark}`).
  - Field-extension formalization on actor cards:
    - Taylor: `hair-state`, `public-role`.
    - Mother: `apprentice-ratification`, `relationship-role-toward-taylor`.
    - Father: `household-economic-tracking`, `role-as-master`, `ledger-authority-state`.
  - Memory monument cards (referenced as free-text glosses in memory.md mem:3, mem:4, mem:6, mem:7):
    - `monument-cape-reflex-trained-body` (or fold into `cond-shard-behavioral-weight` adjacency).
    - `monument-parent-as-cost-vector` / `monument-annette-pattern` (or fold into Annette monument card if authored).
    - `monument-child-performance-grooves`.
    - `monument-control-as-evidence`.
- **Action:** margit dispatch — promote field-extensions to formal state-schema entries; author missing prop/monument cards.
- **Cost:** medium. Per-card authoring + cross-reference updates.
- **AP-SCAN linkage:** AP14 free-text gloss findings (4 entries) clear once monument cards land.

### URI-004 — Audit: per-section monotonicity acceptance

- **Category:** Audit (the command itself).
- **Source:** audit-r3 STRUCTURAL finding on feeling.md ID non-monotonicity, 2026-05-10.
- **Issue:** audit-r3 flagged feeling.md as STRUCTURAL HARD violation because IDs run 1,2,3,4,13 (Taylor) | 5,6,7,14 (mother) | 9,10,11 (father) — not monotone top-to-bottom. But the schema only requires file-scoped monotonicity (no duplicates, no out-of-order WITHIN a logical sub-section). Per-character section grouping is intentional; the audit's STRUCTURAL check is over-strict.
- **Action:** update `.claude/commands/and-facets-audit.md` STRUCTURAL class to allow per-section monotonicity for facets that organize by sub-section (feeling per-character; state-updates env vs actor). Document the per-section convention.
- **Cost:** small. Command-file edit only.

### URI-005 — AP-SCAN remediation (5 candidates from audit-r3)

- **Category:** Per-facet author work; route to next facet-tuning round.
- **Source:** audit-r3 AP-SCAN class findings, 2026-05-10.
- **Items:**
  - AP5 stillness-inflation: tens:29 @34 (`Taylor holds the feet`) — dramatist re-rating.
  - AP7 persistent-narration: NI @23/@24 consecutive "had already read" — NI revision.
  - AP5/voice-fidelity: NI:23 @94 externalized-observer construction — NI revision.
  - AP8 prose-token: vibes:7 @15 token contains finite-verb construction — showrunner revision.
  - AP14 free-text gloss on 4 memory target-references — clears with URI-003.
- **Action:** route to next per-facet tuning round (NI is next in the queue). The AP7 + AP5/voice-fidelity items will be addressed when NI tuning runs.

### URI-006 — Auditor itself needs tuning (Step G design item)

- **Category:** Agent tuning.
- **Source:** Step G design (`design/shoot-v2/three-pass-alpha-design.md` § Final audit teeth). Audit currently runs flag-only because auditor is not yet tuned for delete-authority.
- **Action:** apply the same five-phase facet-tuning process (`design/shoot-v2/facet-tuning-process.md`) to the auditor. Corpus = the audit-r1/r2/r3 reports we have plus next-episode audits. Goal: tune the auditor's rubric + threshold + refusal discipline so deletes can be authorized.
- **Cost:** large. Multi-session tuning project.
- **Linkage:** this is the gating item for moving the audit from flag-only to delete-authoritative.

### URI-007 — /and-season rubric: idiom depletion as named fault class — **LANDED 2026-05-10**

- **Landed location:** `.claude/commands/and-season.md` Pass S3.5 — added idiom-depletion check (10+ instances, 25%-differentiator threshold).

- **Category:** Rubric tuning.
- **Source:** `design/shoot-v2/and-season-tuning-r1/H-carry-back.md` Item 1. C-seams U17 (worm + dark-fantasy STRONG), E-r2 U17 REVISE, auditor fault-AP-1 HARD.
- **Issue:** V1 has 3 partial mechanics (S3.5 5-instance threshold, S5 first-to-last voice, S6 live carry-forward) but no formalism for idiom-depletion-through-overuse as distinct from drift-through-inconsistency or state-verb deny-list violation. `holds the feet` 18+ instances on s01; full physical-stasis cluster 60+. Schema's narrow-license `holds` exemption is satisfied per-instance but cumulative pattern flattens cost-register.
- **Action:** rubric edit + schema reconciliation (does narrow-license `holds` extend to depletion-at-scale?) + 20-named-instance validation on s01 corpus + screen-writer regeneration deferred to separate session.
- **Cost:** medium. Candidate mechanic drafted in H-carry-back.

### URI-008 — /and-season rubric: denouement-share quantification — **LANDED 2026-05-10**

- **Landed location:** `.claude/commands/and-season.md` Pass S2 — added denouement-share LATE-WEIGHT >40% clause + tone-law-licensed exception requiring explicit season-plan designation.

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 2. C-seams U1, E-r2 U1 REVISE.
- **Issue:** S2 names "back half of the aggregate" for climax position but no max denouement share. s01 denouement at 43% triggered audience attack; rubric had no V1 answer.
- **Action:** rubric clause edit. Candidate: `LATE-WEIGHT` flag if denouement >40% of aggregate; tone-law-licensed exception when season-plan explicitly designates the post-peak arc as cost-bearing.
- **Cost:** small. Clause-only edit.

### URI-009 — /and-season rubric: narrator-field rule for interlude episodes — **LANDED 2026-05-10**

- **Landed location:** `.claude/commands/and-season.md` Phase 4 Step 3 — replaced dominant-POV-by-line-count rule with plan-designated-narrator clause per user verdict (Phase I, R1).

- **Category:** Rubric tuning.
- **Status:** USER-VERDICT-RECEIVED — designate narrator at plan time, hold consistent within chunk; do not derive from line counts post-hoc. Rubric language drafted in `design/shoot-v2/and-season-tuning-r1/I-user-verdicts.md`.
- **Source:** H-carry-back Item 3. B-baseline Gap 8 (corrected per auditor signal-006: e05 is compliant; only e06 is anomalous), auditor fault-005 HARD.
- **Issue:** Phase 4 Step 3 spec says `narrator:` is dominant POV by line count; s01e06 names interlude POV (Elara) against dominant Taylor (~122 vs ~86). Spec ambiguity.
- **Resolution:** plan-designated narrator wins. The /and-season Phase 4 Step 3 mechanical computation rule is replaced with: `narrator:` is the plan-designated narrator for the chunk, set before line generation, held consistent within the chunk. **fault-005 closes; e06 narrator field is correct as authored. No s01 corpus mutation required.**
- **Action remaining:** V2 rubric edit to /and-season Phase 4 Step 3 with the new clause. Effect on future runs only.
- **Cost:** small. Clause edit only.

### URI-010 — Schema clarification: aggregate non-monotonic IDs — **LANDED 2026-05-10 (partial — command-side note; schema-side stable-overrides-monotonic clause still pending)**

- **Landed location:** `.claude/commands/and-season.md` Phase 4 Step 3 — added position-aware-mapping note for non-monotonic-ID aggregate regions per user verdict (Phase I, R1, Option A).
- **Remaining:** explicit clause in `schemas/proto-line.schema.md` formalizing "stable-overrides-monotonic" interpretation. Optional follow-up.

- **Category:** Schema.
- **Status:** USER-VERDICT-RECEIVED — Option A (stable-overrides-monotonic; legal survivors). Schema/command language drafted in `design/shoot-v2/and-season-tuning-r1/I-user-verdicts.md`.
- **Source:** H-carry-back Item 4. Auditor fault-001 HARD (NEW); resolved by user verdict.
- **Issue:** s01 aggregate contains 21 900-range IDs interspersed in e01-range content. Schema "stable IDs / re-ordering preserves IDs" rule is in tension with "monotonic positive integer, file-scoped" rule when bones get reordered. Fixer formula `aggregate_id = aggregate_range_start + episode_id - 1` mis-maps for any episode covering the out-of-order region.
- **Resolution:** Option A. The 21 non-monotonic IDs are schema-compliant legal survivors. **fault-001 closes; no corpus mutation required.** Fixer routing for s01e01 bones in the non-monotonic region must use position-aware mapping (file-line position within the aggregate), not ID arithmetic.
- **Action remaining:** V2 schema clarification clause + /and-season Phase 4 Step 3 documentation update on the position-aware mapping requirement. Effect on future runs and any future fixer dispatch on s01.
- **Cost:** small. Schema clause + command-file note.

### URI-011 — /and-season rubric: episode-shape mechanics for Phase 4 Step 2 — **LANDED 2026-05-10**

- **Landed location:** `.claude/commands/and-season.md` Phase 4 Step 2 — replaced plain-English verdicts with mechanic-bearing tests: OPEN-ENGAGES (3-condition first-10-bones check + OPEN-ENGAGES-FAIL), CLOSE-EARNS-NEXT (2-condition final-5-bones check + AFTERMATH-DRIFT flag at >20 bones), SHAPE-COHERENT (peak-position rule + 30-bone-window flatline check + post-peak-flat-aftermath HARD/SIGNAL thresholds).

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 5. B-baseline Gaps 1+3, C-seams Axis 2 + Axis 4 (9 of 12 STRONG seams pressured one of these).
- **Issue:** Phase 4 Step 2 names verdicts (`OPEN-ENGAGES`, `CLOSE-EARNS-NEXT`, `SHAPE-COHERENT`) without mechanics for testing them. Audience surfaced specific candidate close-points; rubric gave them no triage.
- **Action:** rubric edit — three candidate sub-mechanics drafted (5a OPEN-ENGAGES test, 5b CLOSE-EARNS-NEXT test, 5c SHAPE-COHERENT test). Validate against s01e01–e06.
- **Cost:** medium. Three new clauses + 6-episode validation.

### URI-012 — /and-season rubric: post-split continuity pass (S4.5) — **LANDED 2026-05-10**

- **Landed location:** `.claude/commands/and-season.md` — inserted new Pass S4.5 between S4 and S5. Per-boundary BOUNDARY-CARRIES / BOUNDARY-DROPS verdicts; routes to screen-writer for targeted bone additions at failing eN+1 open. Phase 5 print summary updated.

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 6. B-baseline Gap 2, C-seams Axis 3 (5 of 5 boundary continuity units returned STRONG/MODERATE).
- **Issue:** S4 covers within-aggregate continuity; nothing checks the split's effect on continuity across post-split episode boundaries.
- **Action:** new rubric pass S4.5. Per-boundary verdict: `BOUNDARY-CARRIES` or `BOUNDARY-DROPS-{state}`. File-level: `POST-SPLIT-CONTINUITY-OK` or `POST-SPLIT-CONTINUITY-FAIL-{boundary-list}`.
- **Cost:** medium. New pass + 5-boundary validation on s01 + integration into /and-season command.

### URI-013 — /and-season rubric: S3 vs S9 entertainment-density reconciliation — **LANDED 2026-05-10**

- **Landed location:** `.claude/commands/and-season.md` Pass S3 — added "S3 vs S9 — different purposes" note: S3 = entertainment cap (taste); S9 = attention floor (comprehensibility); non-aligned verdicts both valid.

- **Category:** Rubric tuning (clarification).
- **Source:** H-carry-back Item 7. B-baseline Gap 6.
- **Issue:** S3 caps at ~10% TOLERATED + zero BORED; S9 caps at ≥30% B-or-T in 100-line stretch. Two non-aligned thresholds; on s01 S3 reached ACCEPT but S9 still triggered.
- **Action:** rubric clarification — recommended Option A (explicit different purposes: S3 = entertainment cap; S9 = attention floor; non-aligned verdicts both valid).
- **Cost:** small. Clause clarification only.

### URI-014 — /and-season + card schema: season-scope adversarial criteria per persona — **LANDED 2026-05-10**

- **Landed location:** `schemas/card.schema.md` audience role — added Season-Scope Adversarial body section. Per-persona content landed in `active-project/audience/{dark-fantasy-reader,pulp-enthusiast,worm-canon-pedant}/card.md` with 4-5 named attack categories each (atmospheric drift, board-change density collapse, voice-fidelity drift, etc.).

- **Category:** Schema (per-persona card sections).
- **Source:** H-carry-back Item 8. B-baseline Gap 7.
- **Issue:** Per-line and per-episode adversarial habits implicit in persona cards; season-scope adversarial habits not separately documented. Phase C subagent had to derive them.
- **Action:** add `season-scope-adversarial` section to `class: persona` cards under `schemas/card.schema.md`. 3–5 named attack categories per persona. Candidate categories drafted in H-carry-back.
- **Cost:** small. Schema edit + per-active-persona card update.

### URI-015 — /and-season rubric: S6 vibe-drift resolution path — **LANDED 2026-05-10**

- **Landed location:** `.claude/commands/and-season.md` Pass S6 — added drift-resolution routing clause: localizable drift → screen-writer stretch regen; non-localizable drift → season-scope screen-writer pass OR carry-back; carry-forward permitted only when season-plan acknowledges the pattern explicitly.

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 9. B-baseline Gap 4. Observed in s01 (S6 r1 fired 2-of-3 drift; resolution was carry-forward without re-pass).
- **Issue:** Rubric says "≥2-persona threshold for accepting drift flags" but does not specify resolution path. Carry-forward used by default; not always rubric-permitted.
- **Action:** rubric clause edit — localizable drift routes to screen-writer for stretch regeneration; non-localizable drift routes to season-scope screen-writer pass OR Phase H carry-back; carry-forward only when season-plan acknowledges the pattern.
- **Cost:** small. Clause edit only.

### URI-016 — /and-season rubric: S8a/S8b split-verdict adjudication — **LANDED 2026-05-10**

- **Landed location:** `.claude/commands/and-season.md` Pass S8 — added split-verdict adjudication clause. Default: more-restrictive-verdict-wins (IMPLAUSIBLE-CHARACTER overrides PLAUSIBLE-EVENT). Override: explicit licensing-card citation converts to S8-LICENSED-DIVERGENCE-{card-slug}.

- **Category:** Rubric tuning.
- **Source:** H-carry-back Item 10. B-baseline Gap 5. Observed in s01 (S8a IMPLAUSIBLE on Elara visit; S8b PLAUSIBLE on same beat).
- **Issue:** When character (S8a) and event (S8b) lenses disagree on the same beat, rubric does not describe what to do. Reader does not compute lens-by-lens.
- **Action:** rubric clause edit — divergence triggers `S8-SPLIT-VERDICT-{slug}-{beat}` flag; more restrictive verdict wins by default; condition-card override converts to `S8-LICENSED-DIVERGENCE-{card-slug}`.
- **Cost:** small. Clause edit only.

### URI-017 — Persona-card "Threshold Discipline" section (audience-role schema addition) — **LANDED 2026-05-10**

- **Landed location:** `schemas/card.schema.md` audience role — added Threshold Discipline body section with 3 standard rules (rubric arithmetic advisory; tone-law/season-plan citations cover license not seam; carry-forwards stay open until adjudicated clean). Per-persona content landed in `active-project/audience/{dark-fantasy-reader,pulp-enthusiast,worm-canon-pedant}/card.md` naming each persona's specific traps.

- **Category:** Schema (per-persona card sections).
- **Source:** R2 D-critic-carry-back. R2 demonstrated that the worm-canon-pedant's R1 ACCEPT on U1 + U2 was formulaic deference ("tolerates slow open construction when latent-cost register is honest"); under R2's tightened brief that toleration was suspended and worm flipped to REJECT on the same units without any change to the corpus.
- **Issue:** `class: persona` audience role currently has Voice / Hot Buttons / Fatigue Signals — no section codifying what the persona does when rubric thresholds permit a defense the persona's taste rejects. The discipline currently depends on per-round briefing.
- **Action:** add **Threshold Discipline** body section to the audience role with three explicit rules: (1) rubric arithmetic is advisory, taste authoritative; (2) season-plan / tone-law / project-condition citations cover what the rubric explicitly licenses, not what the persona's lens registers as a fault; (3) carry-forwards are open until adjudicated clean. Mirror into the 3 active audience cards.
- **Cost:** small. Schema edit + 3 audience-card updates.
- **Effect:** the tightened brief becomes default; R1's formulaic-scoring path is the special case.

### URI-018 — Auditor sub-class CURVE-SHAPE-EPISODE-INTERIOR

- **Category:** Auditor class refinement (URI-006 progress).
- **Source:** R2 C-auditor-self-review Refinement 1; SLEEPER-1 (U5 dark-fantasy SHAPE-COHERENT failure).
- **Issue:** R1 CURVE-SHAPE ran at season scope only; episode-level SHAPE-COHERENT failures had no mechanic. e04 89-bone post-IGNITION aftermath was caught only via audience attack, not auditor.
- **Action:** new sub-class running per-episode peak-beat identification + post-peak section length and density check. Threshold candidate: post-peak >50% of episode + <2 board-changes = HARD; 40-50% + <2 board-changes = SIGNAL.
- **Validation candidates on s01:** HARD on e04 (matches SLEEPER-1); SIGNAL on e02, e03, e06.
- **Cost:** medium. Sub-class authoring + threshold calibration.
- **Dependencies:** URI-011 (Phase 4 Step 2 SHAPE-COHERENT mechanic) must define episode-level peak-beat first or co-produce.

### URI-019 — Auditor sub-classes CONSTRAINT-BEHAVIOR-SEQUENCE + CONSTRAINT-RESPONSE-BONE-REQUIRED

- **Category:** Auditor class refinement (URI-006 progress).
- **Source:** R2 C-auditor-self-review Refinement 2; SLEEPER-2a (U3 cost-inversion at line 203) + SLEEPER-3 (U2 absent response-bones after apprentice-mark).
- **Issue:** R1 CONSTRAINT checked series laws and cast-presence but not behavior-card sequence-ordering or required-presence at the bone level. Both SLEEPERs are behavior-card compliance failures the class could not see.
- **Action:** two paired sub-classes:
  - **CONSTRAINT-BEHAVIOR-SEQUENCE:** for actors with behavior-card cost-processing-order rules, check multi-bone interactions; flag inversions as SIGNAL by default, HARD at season-plan-named cost-bearing beats.
  - **CONSTRAINT-RESPONSE-BONE-REQUIRED:** for actors with state-change-tracking-obligations on their behavior card, check that named state-changes are followed by ≥1 physical-register response-bone within the same chunk; flag absence as SIGNAL by default, HARD at season-plan-named board-changes.
- **Cost:** medium for sub-classes. Card additions are part of URI-003.
- **Dependencies:** URI-003 (margit referrals) — Taylor's behavior card needs explicit `cost-processing-order` and `state-change-tracking-obligation` fields.

### URI-020 — Auditor sub-class AP-SCAN-POST-PEAK-WINDOW-QUALITY

- **Category:** Auditor class refinement (URI-006 progress).
- **Source:** R2 C-auditor-self-review Refinement 3; SLEEPER-2b (U4 fishwife misdirection at lines 372-393).
- **Issue:** R1 AP-SCAN's window-quality check used aggregate budget across the full episode; a single TOLERATED window after the episode peak was within budget but actively displaced consequence from reader memory.
- **Action:** new sub-class scanning the 20-line window immediately after the episode peak (peak identified per URI-018). Threshold candidate: TOLERATED of 15+ lines within 20 lines after peak = HARD; TOLERATED of any length within 10 lines of peak = SIGNAL.
- **Validation candidate on s01:** HARD on e03 lines 372-393 (matches SLEEPER-2b).
- **Cost:** small-to-medium. Sub-class authoring + threshold validation.
- **Dependencies:** URI-018 (peak-beat anchor).
- **Meta-tuning insight:** the same data (one TOLERATED window) goes from "within budget" to "post-peak misdirection HARD" depending on position. Thresholds aggregated across full units suppress position-dependent severity. This is the formulaic-scoring bypass pattern in concrete form.

### URI-021 — Meta-tuning loop pattern documentation

- **Category:** Process documentation (reusable for future tuning projects).
- **Source:** R2 as a whole. The four-phase pattern (tightening brief → tightened audience attack → auditor self-review → critic-tuning carry-back) surfaced 4 SLEEPERs and 3 auditor refinements; was invented on the fly during R2.
- **Issue:** Future tuning projects (any /and-X tuning, future facet rounds, future /and-season runs with new corpora) would benefit from the same meta-loop. Without documentation, the next project re-invents it.
- **Action:** add `design/shoot-v2/meta-tuning-loop.md` OR fold a section into `design/shoot-v2/facet-tuning-process.md`. Document the four phases with hypothesis-discipline (state predictions before the run; measure results against predictions after; R2 confirmed all 4 predictions).
- **Cost:** small. Doc-only edit.

### URI-022 — Orchestrator-critic card (run-judge for /and-season) — **LANDED 2026-05-10**

- **Category:** Systemic improvement (new staff-facing card class + new /and-season Phase 6).
- **Source:** User direction 2026-05-10 — "establish an orchestrator-level critic card meant to judge performance by results and run time. it will be the standard to satisfy for and-season to be considered a success."
- **Issue:** Content critics (audience, dramatist, auditor) judge what runs produce; nothing judged whether the run *itself* converged honestly within budget. R1+R2 demonstrated that runs can be SHIPPABLE-PENDING-EXECUTION with named residuals AND still be considered "successful" at the orchestration level — but the standard for that judgment was implicit and inconsistent.
- **Landed location:**
  - `staff/orchestrator-critic/card.md` — new card defining success criteria (Convergence / Quality / Routing categories), runtime budgets (60-dispatch hard cap, 30 soft, 3-iteration cap per phase), failure modes F1–F6, verdict format (PASS / PASS-WITH-NOTES / FAIL), run-report template.
  - `.claude/commands/and-season.md` — new Phase 6 (Orchestrator verdict) added after Phase 5 (Persist). No subagent dispatch; main session reads the card and produces the verdict report. Phase 5 print summary updated to show the verdict line. Front-matter description updated.
  - `CLAUDE.md` — agent routing table includes orchestrator-critic; directory map includes `staff/orchestrator-critic/`; Rules §8 amended to note the staff-facing exception to the cards/ five-class taxonomy; new Rule 10 names Phase 6 as the gate.
- **Discipline:** card is library-only; no per-project copy. Versioning protocol in the card itself permits empirical recalibration of thresholds when runs produce verdict-discipline data.

### URI-023 — Feeling rubric V2.1 carry-back (9 audience-confirmed)

- **Category:** Rubric tuning + process protocol.
- **Source:** `design/shoot-v2/feeling-tuning-final.md` Phase 5 audience adjudication, 2026-05-10. All 9 candidates audience-confirmed as real ambiguities, not defensive constructions.
- **Items:**
  1. Q1 should explicitly test against proto-line-as-somatic-action (R2-graph-aware failure mode confirmed across memory + feeling).
  2. AP §7 should gate cross-character same-strategy + within-character formula-repetition (currently gates only per-character surface-token saturation).
  3. Within-character same-strategy gate (negative-continuity across fires).
  4. Cross-character vocabulary saturation gate at structural level.
  5. Cross-character temporal-anchor formula-repetition gate.
  6. Lonely-entry Q2-must-stand-alone test (R2-add discipline; THIRD confirmation).
  7. Card-licensed-vs-saturation distinction at semantic-slot level.
  8. Body-as-subject discipline for somatic-tell-card-match (NEW — surfaced from feel:10 reshape).
  9. **Process protocol — NOT a rubric edit:** "R2-adds receive a mandatory blind §Form + Q1 + Q2 re-test before round close." First surfaced in memory tuning (E.a Taylor); re-confirmed by mother feel:14 (E.b); strongly extended by feel:10 form-violation regression at Phase-F adjudication (revision introduced a comparison/simile violation while fixing the angular-measurement seam). Pattern: graph-aware authoring systematically loosens rubric discipline. The re-test should cover not just Q1+Q2 but the full §Form pass.
- **Action:** rubric edits 1-8 land in `rubric-feeling.md` V2.1; process-protocol item 9 lands in `.claude/commands/and-facets-r2.md` as a mandatory final-pass before round-close.
- **Cost:** medium. Rubric edits + R2 command edit + Phase-5 mechanic re-verify on s01e01 corpus + cross-validation against next-episode tuning data.
- **Note:** filed as URI-007 in the /and-facets session branch; renumbered to URI-023 on merge to avoid collision with /and-season URI-007 (idiom depletion).
- **Status update 2026-05-10:** item 9 is the load-bearing R2 finding and is being addressed by the **R2 Judge Tuning project** (`design/shoot-v2/r2-judge-tuning/`). Phase A (corpus + failure-mode taxonomy) and Phase B (locked R2 rubric with gates G1–G4) authored. Phases C–F (audience attack → R2 self-review → carry-back → re-run validation) are dispatch-heavy and run in subsequent sessions. Items 1-8 remain feeling-rubric content edits and land separately.

### URI-024 — feel:10 Phase-E author regression

- **Category:** Per-facet author work; small targeted revision.
- **Source:** `design/shoot-v2/feeling-tuning-final.md` Phase 5, REJECT verdict on feel:10.
- **Issue:** Father's Phase-E.c revision of feel:10 swapped angular-measurement violation for comparison violation ("the way an estimate gets one"). Audience adjudication: 1 of 12 entries REJECT.
- **Action:** dispatch father impersonator with a targeted brief: revise feel:10 to remove the comparison construction; preserve the cost-accountant priced-yield register the original revision reached for; verify against rubric §forbidden-vocabulary AP6 (similes / comparisons / "the way X" / "as if Y").
- **Cost:** small. Single dispatch.
- **Linkage:** also caught by audit-r4 (TASTE-FLAG / AP-SCAN AP6) once that runs. Either path works.
- **Note:** filed as URI-008 in the /and-facets session branch; renumbered to URI-024 on merge to avoid collision with /and-season URI-008.

### URI-025 — Shared facet-review mechanism across /and-season and /and-facets

- **Category:** Systemic (cross-pipeline architecture).
- **Source:** User direction 2026-05-10. Framing: "carry the same review mechanism across both pipelines." Aligned with URI-002 (SHAPE-FAIL caught only at facet stage when it originated upstream) and URI-018/019/020 (season-aware auditor classes that overlap the existing facet-auditor's vocabulary).
- **Issue:** /and-facets has a tuned cross-cutting auditor (CURVE-SHAPE, FREQUENCY-BAND, AP-SCAN, STRUCTURAL, CONSTRAINT) running on the per-episode facet graph. /and-season has its own S1–S9 review passes plus the orchestrator-critic at Phase 6, but no facet-shape verdict on the aggregate before split or on per-episode SVOs after split. Same shape-class failures get caught downstream where the fix is more expensive (re-author protolines + re-run facets) than upstream (regenerate bones).
- **Action:** factor the facet review stack into a **shared review module** invoked at three points:
  1. **/and-season Pass S9.5 (new)** — between S9 and Phase 4 split. Aggregate-scope subset: tensometer + sensory + state-updates + facet-auditor (CURVE-SHAPE + AP-SCAN classes only — STRUCTURAL/CONSTRAINT need character-perception facets that don't exist yet at this stage). Catches URI-002-class shape failures at the bone level before episode boundaries lock them in.
  2. **/and-season Phase 5.5 (new)** — after Phase 4 split, before Phase 6 verdict. Per-episode /and-facets pass, but **only on episodes the S9.5 auditor flagged**. Default: skip; opt-in by flag or by S9.5 finding.
  3. **/and-facets (existing)** — unchanged. The shared module is what /and-facets already calls; /and-season just calls into the same surface.
- **Carry-the-mechanism principle:** the auditor rubric, the tensometer rubric, the sensory rubric, the AP-SCAN class definitions are authored once and consumed from both pipelines. No fork. URI-018/019/020 sub-classes land in the shared auditor and immediately benefit /and-facets too.
- **Cost implication (load-bearing):** /and-facets-r1+r2+audit is ~25–30 dispatches per episode. Naive insertion (full pass at S9.5 + full per-episode at 5.5 ×6 episodes) breaks the orchestrator-critic's 60-dispatch hard cap. Mitigations: (a) S9.5 runs a **reduced facet set** (3 facets, not 9); (b) Phase 5.5 is **flag-driven**, not by-default; (c) Phase 6 verdict folds S9.5/5.5 findings into Convergence + Quality categories. Threshold recalibration on the orchestrator-critic card may be needed; that's empirical-runway work the card already permits.
- **Phased rollout (recommended):**
  - **Phase 1 (now, cheap):** wire tensometer + facet-auditor (CURVE-SHAPE + AP-SCAN classes only) into /and-season as Pass S9.5. ~12 dispatches. Catches URI-002-class failures upstream.
  - **Phase 2 (after URI-006 auditor tuning lands):** promote S9.5 auditor to delete-authoritative; add URI-018/019/020 sub-classes which are exactly the season-aware auditor checks this URI is reaching for.
  - **Phase 3 (after Phase 1+2 produce verdict-discipline data):** add Phase 5.5 per-episode /and-facets pass, flag-driven. Recalibrate orchestrator-critic dispatch budget against measured per-run costs.
- **Design sketch:** `design/shoot-v2/shared-review-mechanism.md` (authored 2026-05-10).
- **Tensometer-as-mandatory-gate (user direction 2026-05-10):** after R2 judge tuning completes (see URI-023 status update + `design/shoot-v2/r2-judge-tuning/`), tensometer is **promoted to a mandatory pass** within /and-season Pass S9.5 (no longer "subset, recommended"). Gate: HARD on FREQUENCY-BAND or CURVE-SHAPE failure at season scope blocks Phase 4 split until resolved. Lands as part of URI-025 Phase 1 close, contingent on R2 tuning Phase F validation passing.
- **Dependencies:**
  - URI-002 — its resolution validates that S9.5 catches what facet-stage caught after the fact.
  - URI-006 — Phase 2 requires the tuned auditor.
  - URI-018, URI-019, URI-020 — sub-classes that land *into* the shared auditor as part of Phase 2.
  - **URI-023 R2 judge tuning** — must complete before tensometer-as-mandatory-gate promotion lands (R2 discipline is what makes the gate honest under graph-aware re-passes).
  - Orchestrator-critic card — Phase 6 verdict template extends to include S9.5/5.5 findings.

### URI-026 — Tens-into-/and-season as bones-first hard-gate (Phase 1, shared-reviewer) — **LANDED 2026-05-10**

- **Landed location:**
  - `.claude/commands/and-season.md` — new Phase 4 **Step 1.5** (per-proposed-episode tens authoring via dramatist fork, fork-discipline mirrors `/and-facets-r1` Layer 1a, slug-suffixed output `theater/facets/tensometer-<season-slug>e<NN>.md`); Step 2 EXTENDED with bones+tens audience review + parallel narrow-scope auditor dispatch for mechanic-arithmetic verdict; per-persona reports grow `§ Audience taste verdict` (`OWNER: audience`) and `§ Mechanic arithmetic verdict` (`OWNER: rubric`) sections; combined `SPLIT-ACCEPT` requires both ≥2-persona ACCEPT and `MECHANIC-CLEAN`; `SPLIT-REVISE-bones-{line-range}` and `SPLIT-REVISE-cut-{reason}` distinguish regen scope; `REGEN-{REPLACE,ADD,BOTH}` discipline; per-window inner iteration cap 2.
  - `staff/orchestrator-critic/card.md` — new **F7** (Bone-gate residual auto-FAIL); Category B grows **B6** (Bone-gate convergence); verdict template grows §B6 block; runtime budget R1 narrative updated.
  - `schemas/facet.schema.md` — tensometer dual-provenance documented (primary slug-suffixed under `/and-season` Phase 4 Step 1.5; legacy flat-canonical under `/and-facets-r1` Layer 1); `/and-shoot` Phase 0 rename note; shared class library principle.
  - `CLAUDE.md` — Rule 10 amended with bones-first/F7 reference; **Rule 11** added (Shared reviewer resources principle).

- **Category:** Systemic (cross-pipeline architecture; supersedes URI-025 IP-2 author-mode tens block).
- **Source:** User direction 2026-05-10 — "move the tensometer facet into and-season as a hard gate that must be passed... tensometer facet will be included in the protolines output of and-season"; subsequent direction to "verify the same audience for entertainment review happening on and-season that is also happening on and-facets" + "reviewer resources are to be shared with facets to save on tuning costs"; bones-first principle ("if the bones aren't good, then no matter how nice the skin the subject is deformed and wrong").
- **Principle:** the proto-lines are load-bearing; audience entertainment review must judge tens-rated bones, not bare bones; reviewer assets (persona cards, auditor class library, tens rubric) are authored once and consumed from both pipelines (no pipeline-specific reimplementation).
- **Calibration risk:** the tens rubric is calibrated **per-episode** (~150-line corpus, unique-climax-per-episode clause, scene-boundary by loc-state inheritance). Step 1.5 invocation is **per-proposed-episode** (post-Phase-4-split-proposal scope), matching the calibrated scope. Aggregate-scope authoring would have been structurally incompatible with the rubric — not done.
- **Cost implication:** worst-case ~12 added dispatches at the bone-gate (tens-rate × 6 episodes + mechanic-audit × 6 episodes, parallel). Combined with rest of /and-season trends toward 60-dispatch hard cap; per-window inner iteration cap tightened to 2 (not 3) to constrain growth. Recalibrate empirically after first fire.

#### Phase 1 not yet landed (deferred to Phase 1.5 / Phase 2)

- **Phase 1.5 (post-facet-session merge):** Persona-card body text edits to promote tens-attack categories (RUNG-DISTRIBUTION-FLATLINE, FALSE-PEAK, DENOUEMENT-FLAT, RUNG-CLUSTER-OVERSATURATION) from `/and-season` dispatch brief into the active audience cards' `Season-Scope Adversarial` body sections. **Deferred** because parallel `/and-facets` tuning session reads persona cards mid-flight; shared-asset edit must be coordinated, not mid-flight.
- **Phase 2 (later):** sensory + state-updates env + loc-state migration to /and-season as additional bone-gate facets; `/and-facets-r1` Layer 1 (legacy tens authoring) deletion; URI-018 / URI-019 / URI-020 auditor class refinements land into the shared `/and-facets-audit.md` library and benefit both pipelines.

#### URI-025 supersession

URI-025's IP-2 author-mode tens block (aggregate-scope tens authoring at Pass S9.5) is **superseded by URI-026**. The structural incompatibility between the tens rubric's per-episode calibration and aggregate-scope authoring forced moving the bone-gate to post-split (per-episode). URI-025's IP-2b probe-mode for the remaining facets (feeling, vibes, memory, NI, metaphor) remains a valid Phase 3 extension if desired, but the tens-author block is replaced by URI-026's Phase 4 Step 1.5.

#### Test path

First live-fire: `/and-season-plan s02` then `/and-season s02` on a fresh corpus. Existing s01 corpus left untouched (s01's `tensometer.md` was authored by `/and-facets-r1` Layer 1 — legacy path, no collision with slug-suffixed bone-gate output).

---

## How items leave the queue

An item is closed when:
- **Rubric tuning** — rubric-version-bumped, validated on next-episode corpus, rubric-carry-back-deltas captured.
- **Protoline upstream** — re-pass produced new protolines, downstream facets re-run, new audit clean on the affected scope.
- **Card authoring** — margit promoted the card, INDEX.md updated, downstream references updated.
- **Agent definition** — agent permissions changed (out of scope for this codebase; would require Anthropic-side change).
- **Schema** — schema-version-bumped, downstream consumers updated.
- **Audit** — command-file edit landed, next audit run validates.

Items are **never silently abandoned**. If the team decides a queued item is no longer needed, the queue entry is updated to status `ABANDONED — <reason>` and stays for trace.
