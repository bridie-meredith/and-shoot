---
phase: C — auditor self-review
date: 2026-05-10
run: and-season-tuning-r2
input: season-tuning-r1-audit.md (own R1 output) + B-r2-seams.md (audience SLEEPERs)
type: meta-review of own audit
---

# Phase C — Auditor Self-Review

---

## Block 1: Per-class self-review

### Class 1 — STRUCTURAL

**R1 findings:** 3 findings (fault-001 HARD, fault-002 HARD, fault-003 reclassified to signal-001 SIGNAL). Net: 2 HARD, 1 SIGNAL after reclassification.

**R2 in-territory seams:** STRUCTURAL covers file-level integrity, monotonic ID ordering, header field completeness, body comment-cleanliness, aggregate_range contiguity. None of the R2 SLEEPERs sit in STRUCTURAL territory. R2's Block 3 seams are all dramatic-shape and voice-register concerns. The closest R2 touch is the aggregated U5 citation of "Phase 4 Step 2 — CLOSE-EARNS-NEXT" but that is a rubric-class concern, not a schema-integrity concern.

**Caught vs missed:** STRUCTURAL operated correctly in R1. fault-001 (non-monotonic IDs) was genuinely new and not caught by any prior pass. fault-002 (pre-execution header gap) correctly named the pending state. The reclassification of fault-003 was correct on re-read. No R2 seam falls in STRUCTURAL territory.

**Refinement candidate:** No refinement needed. The class is calibrated for schema-integrity. The user verdict on URI-010 (stable-overrides-monotonic) closes fault-001 as compliant; the class correctly escalated for human decision rather than auto-failing. That is the right behavior.

---

### Class 2 — FREQUENCY-BAND

**R1 findings:** 2 findings (fault-004 HARD on predictive POV-honor violation, signal-004 SIGNAL on cast distribution, signal-005 SIGNAL on POV distribution). Net: 1 HARD, 2 SIGNAL.

**R2 in-territory seams:** FREQUENCY-BAND covers episode size (80–160 line band), cast density, and POV distribution. R2 does not directly attack line-count or cast-density; R2's dramatic-shape attacks (U3, U4, U5) are about interior arc quality within a band-compliant episode, not about band violation. The episode-size band was already passed in R1 (with the e03/e06 over-band noted as pre-execution findings).

**Caught vs missed:** No R2 seam sits strictly in frequency-band territory. fault-004's predictive POV-honor finding was forward-looking and technically not a current-corpus fault; R2 does not revisit it. The class performed its mechanical function — it confirmed the split was within band and flagged the predictive risk at U16 execution. Nothing was missed.

**Refinement candidate:** No refinement needed. The class is narrow by design (schema + rubric band validation). The dramatic-quality concerns that R2 surfaces inside band-compliant episodes are correctly not this class's territory — they belong to CURVE-SHAPE and AP-SCAN.

---

### Class 3 — METADATA-INCONSISTENCY

**R1 findings:** 2 findings (fault-005 HARD on s01e06 narrator field, signal-006 SIGNAL correcting B-baseline's false positive on e05, signal-007 SIGNAL on memory.md mirror, signal-008 SIGNAL on memory.md aggregate_range, signal-009 SIGNAL on proto_lines_path). Net: 1 HARD, 4 SIGNAL.

**R2 in-territory seams:** METADATA-INCONSISTENCY covers narrator field, header field values, and memory.md mirrors. None of the R2 SLEEPERs are metadata concerns. The user verdict on URI-009 closes fault-005 as correct-as-authored (plan-designated narrator wins), which means the R1 HARD was based on a rubric ambiguity that has since been resolved in favor of the corpus.

**Caught vs missed:** The class correctly surfaced the narrator-field ambiguity, which prompted the URI-009 resolution. signal-006 correctly identified a prior analysis error in B-baseline. No R2 seam is in this territory.

**Refinement candidate:** No refinement needed, with one note: the class correctly detected that the rubric itself was ambiguous (not the corpus). Producing a HARD finding that turned into a rubric clarification rather than a corpus fix is the right outcome — the class should not be softened to avoid this. The HARD classification created the escalation path that produced URI-009.

---

### Class 4 — CURVE-SHAPE

**R1 findings:** 2 findings (signal-010 SIGNAL on season-level climax midpoint placement, signal-011 SIGNAL on denouement share). Net: 0 HARD, 2 SIGNAL.

**R2 in-territory seams:** This class is the most directly implicated by R2. The SLEEPER-1 seam (U5 dark-fantasy SHAPE-COHERENT failure) names "Phase 4 Step 2 — SHAPE-COHERENT" as the mechanic that should have caught it. R1's CURVE-SHAPE class ran at season scope only — it checked the season-level rise-peak-fall shape (S2 territory) but did not run a per-episode interior shape check. B-r2-seams SLEEPER-1 explicitly states: "If the auditor class had a 'per-episode interior shape' check that was distinct from the 'season-plan mandate' defense, this seam would have been flagged as STRONG in R1."

**Caught vs missed:**
- signal-010 (season-level climax midpoint borderline): caught. The borderline 50% placement was correctly flagged. R2 does not re-attack this finding.
- signal-011 (denouement share): caught. R2's U1 seam confirms the post-IGNITION arc is proportionally oversized; signal-011 anticipated this. URI-008 is in queue.
- SLEEPER-1 (U5 episode-interior SHAPE-COHERENT): MISSED. The R1 audit ran CURVE-SHAPE at season scope only. The e04 post-IGNITION section (475–563 = 89 bones, approximately 60% of the episode's content after the peak) is a per-episode interior shape failure: the episode's post-peak section vastly outweighs its peak, and there is only one board-change in 89 bones. A per-episode SHAPE-COHERENT check would have caught this as a HARD finding. Instead, signal-017 named it as a SIGNAL ("over-aftermath post-IGNITION, 93 bones after swarm contracts") but did not classify it at the CURVE-SHAPE class level — it was routed to AP-SCAN (Class 9) as "over-aftermath" rather than to CURVE-SHAPE as an episode-interior shape failure.

**Refinement candidate:** Add a per-episode sub-class to CURVE-SHAPE: **EPISODE-INTERIOR-SHAPE**. For each per-episode file, the class checks whether the post-peak section (measured from the episode's highest-stakes beat to the episode close) is proportionally disproportionate. A candidate threshold: if the post-peak section exceeds 50% of the episode's line count AND contains fewer than 2 board-changes, flag HARD. This would have caught e04 (89-bone post-peak = ~60% of episode, 1 board-change). This is a per-episode check, not a season-scope check, and is distinct from the season-level S2 denouement-share concern.

---

### Class 5 — CONTRADICTION

**R1 findings:** 1 finding (signal-012 SIGNAL on post-rider letter state-propagation gap). Net: 0 HARD, 1 SIGNAL.

**R2 in-territory seams:** CONTRADICTION covers logical contradictions — a state-change denied or reversed. The R2 seams (U7–U11 continuity boundaries) are state-propagation gaps, not contradictions — a state-change that fails to appear at the next episode's open is a different failure mode than a state-change that is actively reversed. The distinction matters: CONTRADICTION should not be expanded to cover state-propagation gaps; those belong to CONSTRAINT (cast-presence, behavior card) or a new CONTINUITY sub-class.

SLEEPER-3 (U2 apprentice-mark register failure) names "S5 voice-register" as the mechanic and specifically calls for flagging *absence* of required response-bones after named state-changes. This is adjacent to CONTRADICTION territory — one could argue that an actor with an established behavioral pattern (operational tracking) who produces zero response to a named state-change is behaving "contrary to their established character logic" — but this is a stretch from CONTRADICTION's intended scope (logical impossibility / reversal). The SLEEPER-3 mechanic is better housed in CONSTRAINT or a new sub-class.

**Caught vs missed:** signal-012 correctly identified the letter-state gap as a state-propagation concern, not a contradiction, and correctly noted it was "not a hard contradiction." No R2 seam requires CONTRADICTION to have caught it. The class performed its function: it looked for hard logical reversals and found none.

**Refinement candidate:** No refinement to CONTRADICTION itself. The class is correctly scoped. SLEEPER-3's required-response-bone check should NOT be added to CONTRADICTION — see CONSTRAINT refinement below.

---

### Class 6 — DEDUP

**R1 findings:** 0 findings. Class ran clean.

**R2 in-territory seams:** DEDUP covers episode-boundary content duplication. No R2 seam touches duplicate content. The continuity-gap seams (U7–U11) are the inverse: content that *should* appear at an episode boundary is absent, not duplicated.

**Caught vs missed:** Nothing to catch. The class is correctly scoped for what it does.

**Refinement candidate:** No refinement needed. However, it is worth noting that DEDUP's inverse problem (required content absent at a boundary) is the territory SLEEPER-3 identifies — the absence check is structurally the mirror of DEDUP, but it is not DEDUP's territory. Naming this explicitly helps calibrate scope: DEDUP catches repeated material; a new sub-class in CONSTRAINT or CONTRADICTION would catch required-but-absent material. Do not conflate the two.

---

### Class 7 — SUPERFLUOUS

**R1 findings:** 1 finding (signal-013 SIGNAL on e02 aftermath superfluous, lines 70–103).

**R2 in-territory seams:** SUPERFLUOUS covers content whose deletion would not change downstream comprehension. R2's U3 (e02 aftermath padding), U4 (fishwife dispute), and U5 (post-IGNITION aftermath) all attack excess-after-board-change patterns that are structurally in SUPERFLUOUS territory.

**Caught vs missed:**
- signal-013 (e02 aftermath): caught at SIGNAL. R2 rates this STRONG (all three personas). The R1 SIGNAL was correct about what was happening; the severity was understated. The R1 SIGNAL said "previously identified: E-defense U3/U13" and deferred to the E-defense routing. Under R2's tightened brief, deference to "already routed" is explicitly suspended. The SUPERFLUOUS class's mechanism would have caught the e02 aftermath as HARD if it had not self-deferred to the E-defense routing.
- U4 fishwife misdirection (SLEEPER-2b): MISSED as a distinct seam. signal-013 caught the e02 aftermath. The fishwife sequence (372–393 in e03) was not directly named as a SUPERFLUOUS finding in R1. The R1 class checked e02 but did not apply a parallel check to the e03 fishwife sequence. The fishwife sequence has a structural parallel: content after a board-change (Rymer faces Taylor at 370) that does not advance the season forward beyond what the board-change already established. If SUPERFLUOUS had been applied consistently to all episodes, the fishwife sequence would have been a signal-level finding.
- U5 post-IGNITION aftermath: signal-017 in AP-SCAN named "over-aftermath post-IGNITION" — this was classified in AP-SCAN, not SUPERFLUOUS. The over-aftermath finding was there; it was placed in the wrong class. AP-SCAN caught the pattern via anti-pattern logic; SUPERFLUOUS should have caught it as excess-after-payoff logic. Both can be true, but the SUPERFLUOUS class should not have routed around this.

**Refinement candidate:** Two refinements:
1. Remove the self-deferral logic from SUPERFLUOUS — a finding that is "previously named in E-defense" should still be classified at its earned severity. The E-defense routing status does not reduce a SIGNAL to a non-finding; it means the finding is already queued, but the severity classification should stand.
2. Apply SUPERFLUOUS consistently to all post-board-change aftermath sections across all episodes, not only the most obvious case (e02). The current R1 run treated e02 as the canonical example and did not apply the same check to e03's fishwife sequence or e04's post-IGNITION aftermath.

---

### Class 8 — CONSTRAINT

**R1 findings:** 1 finding (signal-014 SIGNAL on Rowan's location plausibility in e03). Net: 0 HARD, 1 SIGNAL. Plus the series-law compliance note (no violations found).

**R2 in-territory seams:** CONSTRAINT covers series laws, condition cards, and actor-presence logic. Three SLEEPERs are adjacent to or within CONSTRAINT territory:

- SLEEPER-2a (U3 cost-inversion): R2 names this as an S5 voice-register fault AND S8a character-plausibility fault. The behavior card for Taylor should specify cost-processing order. If CONSTRAINT checked behavior-card compliance per actor, the jaw-tighten at line 203 before the volume offer at 206 is a behavior-card violation: Taylor's shard-weighted operational-calculus should register cost after accepting a constraint, not before. CONSTRAINT did not check behavior-card cost-sequencing; it only checked series laws, condition cards, and location/prop presence.
- SLEEPER-3 (U2 apprentice-mark register failure): R2 names this as an S5 voice-register fault. The behavior card specifies that Taylor tracks information-asymmetry changes as operational-priority updates. No response-bone after the apprentice mark is a behavior-card absence. CONSTRAINT, as run in R1, checked for presence of out-of-register *actions* (actor doing something their card prohibits). It did not check for absence of *required* actions following a named state-change.
- signal-014 was correctly in CONSTRAINT territory (actor location plausibility).

**Caught vs missed:**
- signal-014: caught at appropriate severity.
- Series-law compliance: correctly confirmed clean.
- SLEEPER-2a cost-inversion (behavior-card sequence): MISSED. CONSTRAINT did not cover behavior-card cost-processing order as a checkable constraint.
- SLEEPER-3 required-response-bone absence: MISSED. CONSTRAINT did not cover required-action absence after named state-changes.

**Refinement candidate:** Add two sub-classes to CONSTRAINT:

1. **CONSTRAINT-BEHAVIOR-SEQUENCE**: For actors with behavior cards that specify a cost-processing order (accept → register cost; state-change → operational-tally), check that the sequence of bones in the episode honors the order. A jaw-tighten before the decisive action is a sequence violation when the behavior card specifies cost follows action.

2. **CONSTRAINT-RESPONSE-BONE-REQUIRED**: After a named state-change within an episode (documentary-exposure event, resource-acceptance, surveillance-vector established), check whether the actor whose behavioral weight is most implicated has at least one response-bone within the episode. Absence of any response-bone after a named state-change is a SIGNAL-level finding; absence when the behavior card explicitly names tracking of that state-change type (e.g., information-asymmetry changes) is HARD. This is the class that SLEEPER-3 requires.

---

### Class 9 — AP-SCAN (anti-pattern scan)

**R1 findings:** 4 findings (fault-AP-1 HARD on idiom depletion, signal-015 SIGNAL on procedural recurrence, signal-016 SIGNAL on shard-load suppression, signal-017 SIGNAL on over-aftermath post-IGNITION). Net: 1 HARD, 3 SIGNAL.

**R2 in-territory seams:** AP-SCAN covers anti-patterns at season scope. R2's U17 (idiom depletion across 55+ instances), U4/SLEEPER-2b (fishwife-misdirection as TOLERATED-window anti-pattern), and U5/SLEEPER-1 (over-aftermath as SHAPE-COHERENT failure) are all adjacent to AP-SCAN territory.

**Caught vs missed:**
- fault-AP-1 (idiom depletion, 18+ holds-the-feet): caught at HARD. R2 confirms this at STRONG (all three personas). The R1 HARD finding was correct. The R2 count revision (55+ total cluster instances vs R1's 18+) is a scope refinement, not a new finding. fault-AP-1 correctly identified the seam.
- signal-015 (procedural recurrence — ledger fatigue): caught at SIGNAL. R2 confirms this as a live S6 carry-forward. Severity calibration is reasonable at SIGNAL since it is a vibe-level pattern, not a schema violation.
- signal-016 (shard-load suppression): caught at SIGNAL. R2 confirms this as a live carry-forward. The SIGNAL was appropriate — the finding is a named prior, not a new discovery.
- signal-017 (over-aftermath post-IGNITION): named at SIGNAL. The finding exists. However, AP-SCAN routed it as an anti-pattern observation rather than flagging it as a CURVE-SHAPE failure. This is a classification placement error: the over-aftermath is both an anti-pattern AND an episode-interior shape failure. signal-017 caught the content but misrouted it to the wrong class.
- SLEEPER-2b fishwife misdirection: PARTIALLY CAUGHT. signal-015 named procedural recurrence and signal-016 named idiom flattening, but the specific fishwife-sequence pattern — a TOLERATED window immediately after the episode's highest-stakes beat — was not caught as a distinct AP-SCAN finding. R2's mechanic analysis says this is an S3 entertainment-window quality concern: the window at 372–393 should have registered as TOLERATED specifically because it follows the Rymer-facing-Taylor beat at 370. AP-SCAN's existing S3-level scanning did not include post-peak window quality as a distinct concern.

**Refinement candidate:** Add a sub-class to AP-SCAN: **AP-SCAN-POST-PEAK-WINDOW-QUALITY**. After the episode's identified highest-stakes beat (the beat with the highest surveillance-vector or board-change weight), check the immediately following 20-line window for entertainment quality. A TOLERATED window in ordinary sequence is within S3 cap; a TOLERATED window immediately following the episode's peak beat is a different class of failure — it actively displaces the peak from the reader's working memory. The threshold: any TOLERATED window within 10 lines of the episode's identified peak beat flags as SIGNAL; a TOLERATED window that runs 15+ lines after the peak beat flags as HARD. This would have caught the fishwife sequence (22 bones, immediately after Rymer-faces-Taylor at 370) as HARD.

---

### Class 10 — TASTE-FLAG

**R1 findings:** 2 findings (signal-018 SIGNAL on maester-arrival procedural recurrence risk, signal-019 SIGNAL on season-close image quality). Net: 0 HARD, 2 SIGNAL.

**R2 in-territory seams:** TASTE-FLAG is explicitly non-blocking and anticipatory. R2 does not produce findings that are purely taste-flags; R2's seams are graded STRONG/MODERATE/THIN with mechanical citations. However, signal-018 anticipated the maester-arrival procedural concern, and R2's U6 (Elara interlude 100-bone toll) confirms that procedural-sequence fatigue is a live seam.

**Caught vs missed:** signal-018's anticipation of the maester-arrival risk was directionally correct. The R2 U6 STRONG finding is about Elara's 100-bone competence-sequence before the maester arrives; signal-018 anticipated the maester arrival itself as the procedural-recurrence risk. Adjacent but not identical. signal-019 (season-close image) is a carry-forward for s02 planning and R2 does not re-attack it.

**Refinement candidate:** No refinement needed. TASTE-FLAG is correctly scoped as anticipatory and non-blocking. The two signals in R1 each correctly identified a future audit surface. The class performed its advisory function.

---

### Class 11 — PILE-UP REVIEW

**R1 findings:** 3 findings (signal-020 SIGNAL on e03 12-actor pile-up, signal-021 SIGNAL on e04 11-actor pile-up, signal-022 SIGNAL on e01 cast thinness). Net: 0 HARD, 3 SIGNAL.

**R2 in-territory seams:** PILE-UP REVIEW covers cast density and whether it is narratively warranted. No R2 seam directly attacks cast pile-up as a fault. R2's U4 fishwife-misdirection seam is adjacent — the fishwife is one of the 12 actors in e03 and her dispute sequence is the misdirection that buries the Rymer beat — but R2 does not characterize this as a pile-up problem. It characterizes it as a post-peak TOLERATED window problem.

**Caught vs missed:** The three pile-up signals correctly identified the density patterns and confirmed they were narratively warranted. The class did not need to catch anything beyond what it found. The connection between cast pile-up and misdirection risk (too many actors means too many possible focal objects, which makes it easier for aftermath sequences to redirect attention from the highest-stakes actor) was not made explicit in R1. This is a calibration note, not a missed finding.

**Refinement candidate:** No refinement needed for the class mechanism. One optional extension: when a pile-up episode is flagged, note specifically whether any minor-actor sequences (fishwife, cloth-factor's wife) are positioned immediately after the episode's highest-stakes beat. This would connect PILE-UP to the AP-SCAN-POST-PEAK-WINDOW-QUALITY sub-class proposed above. Not a separate class refinement — a linking note in the PILE-UP output.

---

## Block 2: SLEEPER reckoning

### SLEEPER-1 (U5 dark-fantasy SHAPE-COHERENT failure)

**R2's named mechanic:** "Phase 4 Step 2 — SHAPE-COHERENT. The rubric states 'episode's interior arc (rise / peak / fall scaled to episode size) reads as one unit.' The 89-bone post-peak section of e04 is 60% of the episode by line count and has one board-change; this fails SHAPE-COHERENT by almost any reading. If the auditor class had a 'per-episode interior shape' check that was distinct from the 'season-plan mandate' defense, this seam would have been flagged as STRONG in R1."

**R1 audit's coverage:** The closest class was CURVE-SHAPE (Class 4), which ran at season scope only (S2 territory: buildup, climax, denouement proportions for the full 912-line aggregate). signal-017 in AP-SCAN named the 93-bone over-aftermath and classified it SIGNAL, but did not route it to CURVE-SHAPE or apply a SHAPE-COHERENT test at the per-episode level. The CURVE-SHAPE class had no per-episode sub-scope.

Why it didn't catch: Two compounding reasons. First, CURVE-SHAPE was season-scoped; it ran S2 metrics (aggregate climax position, denouement share) without stepping down to per-episode interior shape. Second, signal-017 was explicitly tied to the E-defense U1 DEFEND routing — the annotation says "the rubric's S2 denouement characterization covers this. Signal only per U1 DEFEND." The E-defense's DEFEND vote deferred the finding; the R1 audit followed the deferral rather than classifying the per-episode shape failure independently. This is the "formulaic-scoring bypass" pattern A-tightening-brief predicted: the E-defense DEFEND created a cover that the R1 audit accepted when a pure shape-test would have rejected it.

**Recommendation:** CURVE-SHAPE should add a per-episode sub-class: **CURVE-SHAPE-EPISODE-INTERIOR**. This sub-class runs at per-episode scope and applies a SHAPE-COHERENT test independently of season-plan mandate defenses. The test: for each episode, identify the episode's highest-stakes beat (peak), measure the post-peak line count as a percentage of the episode total, and count board-changes in the post-peak section. If post-peak section exceeds 50% of episode length with fewer than 2 board-changes, classify HARD (not SIGNAL). Season-plan mandate is not a defense for per-episode interior shape; the episode must read as one unit regardless of what the season plan designated the aftermath register to be.

Do not create a new class for this. It is a sub-scope of CURVE-SHAPE, not a new category. The season-scope CURVE-SHAPE check (signal-010, signal-011 type findings) and the per-episode CURVE-SHAPE-EPISODE-INTERIOR check are parallel concerns at different scopes, both appropriate to the same class.

---

### SLEEPER-2 (U3 cost-inversion + U4 fishwife misdirection)

**R2's named mechanics:**
- SLEEPER-2a: "S5 — verbs an actor takes match the actor's voice signature. S8a — would this character actually do that, given their behavior card. The behavior card for Taylor should specify cost-processing order (accept → register cost) not (anticipate → accept). The auditor's S8a class should have caught the jaw-tighten before the volume-offer as a plausibility flag."
- SLEEPER-2b: "S3 — entertainment-window check. The window containing lines 372–393 should have registered as TOLERATED or BORED for the pulp reader specifically because it immediately follows the episode's highest-stakes moment. A threshold that looks at post-peak window quality specifically would catch this."

**R1 audit's coverage:**
- For SLEEPER-2a (cost-inversion): CONSTRAINT (Class 8) scanned actor presence and series-law compliance, but did not check behavior-card cost-processing sequence. The R1 CONSTRAINT scan confirmed "no series-law violations found" and logged the Rowan location plausibility finding. It did not examine the ordering of cost-signals relative to decisive actions within an episode. The cost-inversion at line 203 was not surfaced by any R1 class.
- For SLEEPER-2b (fishwife misdirection): AP-SCAN (Class 9) covered the ledger-sequence fatigue and idiom depletion. It did not include a post-peak-window quality check. The S3 pass in the nine-pass review was an audience pass (not an auditor pass); AP-SCAN is the auditor's proxy for entertainment-pattern concerns but it operated at aggregate scope (idiom count across the season) not at per-episode post-peak window scope.

Why they didn't catch:
- SLEEPER-2a: R1's CONSTRAINT class was anchored to "series laws, condition cards, slug/reference resolution" — the rubric's S1 formulation. Behavior-card sequence compliance (cost follows action, not precedes it) is a more granular behavioral check that the class did not have. The V1 rubric's S5 check is a dramatist pass (audience-side), not an auditor pass; the auditor had no structural equivalent for voice-register sequencing.
- SLEEPER-2b: The S3 entertainment-window check is an audience responsibility in the V1 rubric, not an auditor responsibility. AP-SCAN approximates anti-pattern detection but does not run per-window entertainment checks. The 5-instance S3.5 threshold is the auditor's only entertainment-related mechanism, and it fires on verb frequency, not on window quality relative to beat position.

**Recommendations:**

For SLEEPER-2a: AP-SCAN should add a sub-class **AP-SCAN-COST-SEQUENCE** that checks the ordering of cost-signal bones relative to decisive-action bones for actors with behavior cards specifying shard-weighted cost-processing. The check: for any episode containing a resource-acceptance or constraint-acceptance beat, verify that the actor's cost-register bones (jaw-tighten, temple-press, exhale as cost-signal) follow the acceptance beat rather than precede it. A pre-acceptance cost-signal is a SIGNAL finding; a pre-acceptance cost-signal immediately before a named resource-acceptance is HARD. This is a mechanical check (ordering of bones within a ±5 line window of the decisive action) that does not require dramatic judgment.

For SLEEPER-2b: AP-SCAN should add the **AP-SCAN-POST-PEAK-WINDOW-QUALITY** sub-class described under Class 9 above. This directly addresses the fishwife-misdirection pattern. Note that this requires the auditor to first identify the episode's peak beat — which connects to the CURVE-SHAPE-EPISODE-INTERIOR sub-class proposed above. The two refinements are dependent: post-peak window quality requires a defined "peak beat" at the episode level, which CURVE-SHAPE-EPISODE-INTERIOR would provide.

---

### SLEEPER-3 (U2 absent response-bones after apprentice-mark)

**R2's named mechanic:** "S5 — verbs an actor takes match the actor's voice signature; no drift between an actor's first-stretch voice and last-stretch voice. A refinement: S5 should also flag when a character with an established behavioral-weight pattern (operational tracking, cost-registration) produces zero response-bones after a named state-change within the same episode."

**R1 audit's coverage:** The worm-canon-pedant's U2 attack produced a MODERATE in R1 (the worm accepted because "the OPEN-ENGAGES question for this reader is answered by the accuracy of the Worm-behavioral-weight suppression"). This was the formulaic-scoring concession: tolerance for slow construction when the register is honest. The R1 audit did not have a class that checked for required-response-bone absence after named state-changes. CONTRADICTION (Class 5) looked for logical reversals; CONSTRAINT (Class 8) checked actor presence, series-law compliance, and location plausibility; neither checked for behavioral-absence after state-change.

**Class ownership decision:**

The three candidates are:
- CONTRADICTION: a state-change that produces no follow-up reads as if it didn't happen. This is the conceptual framing, but CONTRADICTION's mechanism is wrong — it checks for impossible states, not for behavioral absences. The state-change DID happen; the absence of Taylor's response does not logically contradict anything. CONTRADICTION should not own this.
- CONSTRAINT: the character's behavior-card pattern is violated by absence. This is the correct framing. Taylor's behavior card specifies that she tracks information-asymmetry changes as operational-priority updates. Zero response-bones after the apprentice mark (a new documentary-exposure event) violates the behavior-card's specified behavioral pattern. CONSTRAINT owns behavior-card compliance; it should own behavioral-absence-after-state-change.
- New class: not warranted. The check is a behavior-card compliance check, which is already CONSTRAINT territory.

**Recommendation:** CONSTRAINT should own this via the **CONSTRAINT-RESPONSE-BONE-REQUIRED** sub-class described under Class 8 above. The mechanism: after any named state-change within an episode (documentary-exposure event, resource-acceptance, surveillance-vector establishment, or debt-creation), check whether the actor whose behavioral-weight card specifies tracking of that state-change type has at least one response-bone within the same episode. Absence is a SIGNAL if the state-change is in the episode's interior (response-bone may have been omitted as part of compression). Absence is HARD if the state-change is at or near the episode's close (the episode ends on a state-change with no visible processing — exactly what the apprentice-mark sequence does: episode closes 50 bones after the mark with zero Taylor response-bone registering the exposure change).

This sub-class is distinct from CONSTRAINT-BEHAVIOR-SEQUENCE (SLEEPER-2a): BEHAVIOR-SEQUENCE checks ordering of bones around a decisive action; RESPONSE-BONE-REQUIRED checks for presence of at least one response-bone after a named state-change. Both are behavior-card compliance checks, both in CONSTRAINT, but they answer different questions.

---

## Block 3: Audit-class roadmap toward URI-006

### Top 3 refinements (ranked)

**1. CURVE-SHAPE per-episode sub-class (CURVE-SHAPE-EPISODE-INTERIOR)**

Impact: catches SLEEPER-1 directly; also provides the "peak beat" anchor that the AP-SCAN-POST-PEAK-WINDOW-QUALITY sub-class (refinement 2) depends on. Without this, refinement 2 cannot run mechanically — there is no defined episode-level peak position to anchor the post-peak window check. This refinement is the structural prerequisite for multiple downstream improvements.

On the R2 seam distribution: SLEEPER-1 is the only SLEEPER that belongs directly to this class; but the per-episode interior-shape check would also have surfaced signal-level findings on e02 (42-bone post-board-change aftermath with no second board-change), e03 (48-bone post-Rymer-faces-Taylor aftermath), and e06 (Elara 100-bone competent-action sequence before any board-change). The single refinement would have produced HARD findings on at least 3 episodes beyond the SLEEPER.

Cost: medium. Requires: (a) a definition of "episode-level peak beat" in the rubric (currently only the season-level peak has a defined mechanic — URI-011 is in queue for Phase 4 Step 2 mechanics; this refinement would depend on URI-011's SHAPE-COHERENT sub-mechanic definition), (b) a threshold for the post-peak section proportion (proposed: >50% of episode length + <2 board-changes = HARD), (c) test against all 6 s01 episodes to confirm the threshold calibration. Dependencies: URI-011 (Phase 4 Step 2 SHAPE-COHERENT mechanic definition) must land first, or must be co-produced. If URI-011 defines the SHAPE-COHERENT mechanic for audience use, the auditor's CURVE-SHAPE-EPISODE-INTERIOR sub-class can use the same mechanic for mechanical checking.

**2. CONSTRAINT behavior-card compliance sub-classes (CONSTRAINT-BEHAVIOR-SEQUENCE + CONSTRAINT-RESPONSE-BONE-REQUIRED)**

Impact: catches SLEEPER-2a (cost-inversion) and SLEEPER-3 (absent response-bones) directly. Both are behavior-card compliance failures that require the auditor to read the actor's behavior card and check specific bone-ordering and bone-presence requirements.

Cost: medium. Requires: (a) behavior cards to explicitly specify cost-processing order (accept → cost-register) and state-change tracking obligations — the current behavior cards may not have this at the granularity needed for mechanical checking; margit would need to verify card completeness before the sub-class can run against new episodes; (b) a definition of "named state-change" for RESPONSE-BONE-REQUIRED — the rubric does not currently define which event types count as state-changes requiring response-bones; (c) threshold calibration (how many lines post-state-change before absence becomes HARD). Dependencies: behavior cards for Taylor must include an explicit cost-processing-order field and a state-change-tracking-obligation field. If those fields are absent from the card, the sub-class cannot run mechanically. This is a card-authoring dependency on URI-003 (margit referrals). If URI-003 completes and adds the relevant fields, this sub-class becomes runnable.

**3. AP-SCAN-POST-PEAK-WINDOW-QUALITY sub-class**

Impact: catches SLEEPER-2b (fishwife misdirection) directly. Also addresses the "formulaic-scoring bypass" concern from A-tightening-brief: the S3 10% TOLERATED cap was within budget when computed across the full episode, but the specific post-peak window at 372–393 was a taste failure at that position regardless of the aggregate count. The sub-class makes peak-position context a factor in TOLERATED-window severity.

Cost: small-to-medium. Requires: (a) the episode-level peak-beat anchor from refinement 1 (CURVE-SHAPE-EPISODE-INTERIOR) — if the peak is not defined, the "post-peak window" cannot be bounded; (b) a definition of "post-peak window" scope (proposed: the 20-line window immediately following the peak beat); (c) a severity threshold (proposed: TOLERATED window of 15+ lines immediately after episode peak = HARD; TOLERATED window of any length within 10 lines of peak = SIGNAL). The sub-class is computationally straightforward once the peak-beat anchor exists; the main cost is the dependency on refinement 1. Dependencies: refinement 1 (CURVE-SHAPE-EPISODE-INTERIOR) for the peak-beat anchor; URI-011 for SHAPE-COHERENT mechanic definition.

---

### Where R1 audit was strong

**STRUCTURAL (Class 1):** The class found fault-001 (non-monotonic aggregate IDs) which was genuinely new — not surfaced by any prior phase. It correctly escalated for human decision rather than auto-failing, and the human verdict produced URI-010 with a clear schema clarification. The class also correctly self-corrected (fault-003 reclassified to signal-001) when re-reading showed the schema licensed the marker. No refinement needed.

**METADATA-INCONSISTENCY (Class 3):** The class surfaced the narrator-field ambiguity (fault-005) that produced URI-009 and the user verdict that closed it. More importantly, the class corrected a prior false positive (signal-006: B-baseline's Gap 8 e05 analysis was based on file-line/aggregate-ID confusion). Catching and correcting a prior analysis error is high-value auditor work. No refinement needed.

**AP-SCAN Class 9 — idiom depletion (fault-AP-1):** The S3.5 drift-pattern check at season scope correctly identified the idiom-depletion problem at 18+ instances of `holds the feet` and classified it HARD. R2 confirms this at STRONG (all three personas) with a revised count of 55+. The class was right on the finding even when the E-defense DEFENDED it; the HARD classification created the escalation pressure that produced URI-007. The class should not have soft-pedaled this into a SIGNAL. The HARD was correct.

**DEDUP (Class 6) and PILE-UP REVIEW (Class 11):** Both ran their respective checks cleanly, confirmed clean results, and did not over-produce findings in areas where the corpus was compliant. The ability to return clean results without manufacturing findings is as important as catching problems.

**FREQUENCY-BAND (Class 2) — predictive fault-004:** Identifying a predictive fault (the U16 cut at 692 would bisect the Taylor-POV stretch) that the E-defense routing had not flagged is an example of the class adding value beyond its basic band-validation function. The finding was not in any prior routing. It correctly anticipated a risk that the U16 dramatist task would need to check.

---

### URI-006 progress note

URI-006 as written is a "large, multi-session" project defined as: "apply the same five-phase facet-tuning process to the auditor; goal: tune the auditor's rubric + threshold + refusal discipline so deletes can be authorized."

R2 provides the following concrete inputs toward URI-006:

**What R2 closes or partially closes for URI-006:**

Three of the five gap areas are now concretely specified:
1. The CURVE-SHAPE per-episode sub-class (refinement 1) has a candidate threshold, a candidate mechanic, and a dependency chain (URI-011). R2 provides the corpus evidence to validate the threshold against (e04's 89-bone post-peak is the calibration case).
2. The CONSTRAINT behavior-card sub-classes (refinement 2) have defined target findings (SLEEPER-2a, SLEEPER-3) and a concrete card-authoring dependency (URI-003 behavior-card field additions). R2 surfaces what behavior-card fields would need to exist for the sub-classes to run.
3. The AP-SCAN-POST-PEAK-WINDOW-QUALITY sub-class (refinement 3) has a concrete misdirection case (fishwife sequence at 372–393) to calibrate against.

Additionally, R2 confirms which classes do NOT need refinement (STRUCTURAL, METADATA-INCONSISTENCY, DEDUP, FREQUENCY-BAND, PILE-UP, TASTE-FLAG, CONTRADICTION) — narrowing URI-006's scope to three classes rather than all eleven.

**What remains for the URI-006 dedicated project:**

1. The "delete-authority" half of URI-006 (allowing auditor to authorize deletes rather than flag-only) is not addressed by R2 at all. That requires a separate tuning pass on the auditor's criteria field calibration — when a HARD finding justifies a fixer dispatch with deletion authority vs. when it requires human review. R2 surfaces the finding quality problems; the authority question is separate.

2. URI-011 (Phase 4 Step 2 mechanics) must land before CURVE-SHAPE-EPISODE-INTERIOR can be formalized. R2 does not produce URI-011's content; it only confirms the dependency.

3. URI-003 (behavior-card field completeness) must land before CONSTRAINT-BEHAVIOR-SEQUENCE and CONSTRAINT-RESPONSE-BONE-REQUIRED can run. R2 does not produce the card additions; it specifies what fields are needed.

4. Threshold validation: the candidate thresholds proposed above (50% post-peak section + <2 board-changes = HARD; 15+ line post-peak TOLERATED window = HARD; etc.) are proposals derived from a single corpus (s01). URI-006's tuning process should validate these thresholds against a second corpus before locking them.

R2 closes approximately 30% of URI-006's design work — it provides the what and the why for three class refinements, the dependency map, and the non-refinement list. The remaining 70% (delete-authority calibration, rubric preconditions, threshold validation against future corpora) requires the dedicated multi-session project.

---

## Phase C complete
