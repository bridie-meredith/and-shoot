---
phase: H — rubric carry-back
date: 2026-05-10
run: and-season-tuning-r1
input: A-corpus, B-baseline, C-seams, E-defense, F-final, season-tuning-r1-audit, E-r2-defense
locked-rubric: design/shoot-v2/and-season-tuning-r1/rubric-and-season.md (V1, anchored to .claude/commands/and-season.md @ cd4aa6595c701483d17ff3b90ab46fd7f11d5ca4)
---

# Phase H — Rubric Carry-Back Queue Entries

The Run R1 tuning surfaced rubric gaps the V1 rubric could not adjudicate. This phase captures them as candidate V2 edits. Per the packet's discipline, **rubric edits do NOT land in this run.** They are queued for a separate rubric-tuning session that will use the corpus + seams + defenses from R1 as input.

This file is the source-of-truth for R1's carry-back proposals. It is mirrored into `design/shoot-v2/upstream-tuning-queue.md` as URI-007 through URI-012 (numbered from the queue's existing tail at URI-006).

---

## Carry-back item 1 — Idiom depletion as named fault class

**Source:** C-seams U17 (worm + dark-fantasy STRONG convergence); E-r2 U17 REVISE; auditor fault-AP-1 HARD; B-baseline S6 carry-forward (worm: shard-load-suppressed; dark-fantasy: procedural-recurrence).

**The gap:** V1 has three partial mechanics that point at idiom depletion (S3.5 5-instance drift-pattern threshold, S5 first-to-last voice register coherence, S6 live carry-forward) but no formalism that quantifies "depletion through overuse" as distinct from "drift through inconsistency" or from "state-verb deny-list violation." `holds the feet` appears 18+ times in the aggregate (60+ instances in the full physical-stasis cluster); the schema's narrow-license `holds` exemption is syntactically satisfied per instance but the cumulative pattern flattens cost-register and patience-register into the same physical form, suppressing shard-cost legibility.

**The schema reconciliation question (to settle alongside this carry-back):** does the schema's narrow-license `holds` exemption (`schemas/proto-line.schema.md`) license unbounded use of the same physical-stasis idiom across a season aggregate? Or does S3.5's "5+ appearances as borderline state-verb idiom" override the schema's per-instance license at the cumulative-pattern level?

**Candidate V2 mechanic (lifted from E-defense U17):**

> For any physical-stasis idiom appearing 10+ times in the aggregate, at minimum 25% of instances must carry a contextual differentiator (preceding scene density, following board-change, or direct proximity to a named shard-load beat) that allows a reader to distinguish cost-register from patience-register. Idioms below this differentiation rate trigger a `IDIOM-DEPLETION-{idiom}` flag and route to screen-writer for systematic recast.

**Validation corpus for V2:** the 20 named instances from C-seams worm-canon-pedant concentration list (aggregate lines 35, 277, 293, 332, 349, 386, 390, 417, 427, 440, 502, 518, 560, 583, 629, 642, 699, 789, 799, 907) become the test set — under V2, what fraction of those instances would the new mechanic flag, and does the flag set match the audience's STRONG convergence?

**Cost:** medium. Rubric edit + 20-instance verification on s01 corpus + screen-writer regeneration of flagged instances under the new criterion (deferred to a separate session).

---

## Carry-back item 2 — Denouement-share quantification

**Source:** C-seams U1 (dark-fantasy + pulp STRONG); E-r2 U1 REVISE (engages the seam directly); B-baseline rubric explicit gap.

**The gap:** S2 names "back half of the aggregate" as the threshold for climax position (rejected as `EARLY-SEASON-PEAK` if earlier; rejected as `LATE-SEASON-PEAK` if later) but does NOT name a maximum permissible denouement share. s01's denouement at 520–912 is 393 lines = 43% of the 912-line aggregate. The C-seams attack pressed this as the season's atmospheric-collapse vector; the U1 DEFEND argued tone-law mandates the long-cost shape; F rejected the defense; E-r2 routed targeted bone additions but the structural finding (denouement > 40% of aggregate) remains uncovered by V1.

**Candidate V2 mechanic:**

> Denouement share: the post-climax stretch must not exceed 40% of the aggregate's total numbered-line count. If the denouement share exceeds 40%, S2 issues a `LATE-WEIGHT` flag for human review. Tone-law-mandated long-cost structures (e.g., cond-series-tone-constraints-84ac mandating cost-migration over kinetic peaks) qualify for an `LATE-WEIGHT-LICENSED-{condition-card}` exception when the season-plan explicitly designates the post-peak arc as cost-bearing — but the exception requires the season plan to name the cost-bearing arc and provide its expected share.

**Validation corpus for V2:** s01 at 43% triggers `LATE-WEIGHT`; the season-plan §B drama statement does name "the four years that follow are the long cost" — qualifies as `LATE-WEIGHT-LICENSED-cond-series-tone-constraints-84ac` if the V2 exception language lands. s02–s04 chunks in the series-plan have implied denouement-share patterns that should be tested against the new threshold.

**Cost:** small. Rubric clause edit only; no corpus regeneration.

---

## Carry-back item 3 — Narrator-field rule for interlude episodes (Gap 8 corrected)

**Source:** B-baseline Gap 8 (corrected by auditor signal-006); auditor fault-005 HARD; E-r2 Block 3 acknowledgment.

**Correction note:** B-baseline Gap 8 originally named both s01e05 and s01e06 as anomalous. Auditor signal-006 demonstrated that s01e05's `narrator: mira-stonefield-jaehaerys` is **compliant** under the V1 dominant-POV spec — Mira ~82 lines vs Taylor ~54 in the per-episode file body. The prior B-baseline analysis confused aggregate IDs with file line counts. **Only s01e06 is the real Gap 8 anomaly.**

**The gap:** /and-season Phase 4 Step 3 says "narrator: the POV character resolved from the dominant inline `# pov:` marker inside the episode's stretch." s01e06.md names `narrator: oc-craftsman-mother` but the dominant POV is Taylor (~122 lines vs Elara ~86). The shipped state appears to apply an unwritten rule "interlude POV wins when present." The rubric does not say this.

**Candidate V2 resolution (two options, choose at V2 session):**

**Option A — interlude-POV-wins clause:**
> When an episode contains a designated interlude (per `season-plan.md` POV rulings) as its primary dramatic arc — even if the interlude POV does not dominate by raw line count — the interlude POV is the named `narrator:`. The season-plan's interlude designation is the authoritative source.

**Option B — dominant-line-count rule (literal V1):**
> `narrator:` is always the POV character with the most numbered-line presence in the episode's body, regardless of season-plan interlude designation. Episodes with interlude POVs that do not dominate by line count must either (a) be re-cut to make the interlude POV dominant, or (b) accept the dominant POV as `narrator:` with the interlude flagged separately in `memory.md`.

**Effect on s01e06 if V2 lands:**
- Option A → `narrator: oc-craftsman-mother` is correct as authored. fault-005 closes.
- Option B → s01e06.md and memory.md must update to `narrator: taylor-hebert-jaehaerys`; interlude flag remains separately recorded.

**Cost:** small. Rubric clause edit + at most one per-episode header + memory.md correction (Option B path only).

---

## Carry-back item 4 — Aggregate non-monotonic IDs schema clarification

**Source:** auditor fault-001 HARD (NEW); requires human escalation per E-r2 Block 2.

**The gap:** `s01.aggregate.md` contains 21 900-range IDs (922, 924, 930, 931, 916, 935, 926, 925, 927, 928, 932, 919–921, 923, 904–907, 910–911) interspersed within the e01-range content region (lines mapping to aggregate IDs 1–149). The schema (`schemas/proto-line.schema.md`) declares IDs are "monotonic positive integer, file-scoped" AND "stable — once assigned, never reused, never reassigned" AND "re-ordering preserves IDs."

The two clauses are in tension when bones get reordered: if a bone originally assigned ID 922 is moved earlier in the narrative, "stable" says ID 922 is preserved (not reassigned to fit the new position), but "monotonic" says the file's IDs should run in increasing order. The reorder produces non-monotonic IDs — schema-compliant under "stable" but schema-violation under "monotonic."

**Downstream impact:** the fixer formula `aggregate_id = aggregate_range_start + episode_id - 1` (per /and-season Phase 4 Step 3) assumes monotonic IDs. If the aggregate has non-monotonic IDs, this formula mis-maps for any episode covering an out-of-order region. s01e01 covers aggregate range 1–148/149, which contains the 21 900-range IDs — fixer routing for s01e01 bones is unreliable.

**Candidate V2 schema clarification (two options):**

**Option A — stable-overrides-monotonic (legal-survivors path):**
> When IDs are assigned at write-time and bones are subsequently reordered, the original IDs are preserved. The "monotonic" rule applies to ID *assignment* (no reuse, no reassignment) but not to ID *position*. Aggregate files MAY contain non-monotonic IDs as legal artifacts of reordering. Fixer routing for bones in non-monotonic regions must use a position-aware mapping function (e.g., file line position) rather than the `aggregate_range_start + episode_id - 1` shortcut.

**Option B — monotonic-overrides-stable (re-number-on-reorder):**
> Reordering bones in the aggregate triggers an ID renumbering pass. The original ID assignments are not preserved when their narrative position changes. This requires updating any downstream artifact that cited the old IDs. Fixer formula remains valid.

**Effect on s01 corpus if V2 lands:**
- Option A → fault-001 closes; the fixer formula in /and-season Phase 4 Step 3 must be updated to handle non-monotonic IDs.
- Option B → fault-001 routes to a re-numbering pass on the s01 aggregate; downstream artifacts (per-episode files with cited aggregate IDs in commits or external references) must be updated.

**Recommendation for the human reviewer:** check the s01 aggregate's pass-2 / pass-3 reorder history (per the season-s01-pass-S2-shape and S3-trim audit reports) to determine whether the 900-range IDs are reorder artifacts or were assigned at that range during late-pass insertions. The answer informs which option is consistent with how the season was actually authored.

**Cost:** small for the rubric/schema decision; medium for the s01 corpus impact (a re-numbering pass affects downstream mapping if Option B is chosen).

---

## Carry-back item 5 — Episode-shape and boundary mechanics (Gaps 1 + 3)

**Source:** B-baseline Gaps 1 and 3; C-seams Axis 2 (per-episode shape) and Axis 4 (boundary placement); 9 of the 12 STRONG seams pressured one of these axes.

**The gap:** Phase 4 Step 2 names three verdicts (`OPEN-ENGAGES`, `CLOSE-EARNS-NEXT`, `SHAPE-COHERENT`) but does not formalize how to test them. The audience surfaced specific candidate close-points (volume-handoff at 207 for e02; Rymer at 370 for e03; candle-catches at 148 for e01; releases-the-page at ~692 for e05) but the rubric gave them no mechanic for triaging or quantifying the verdicts. Each persona had to use plain-English judgment.

**Candidate V2 mechanics (three sub-items):**

**5a — OPEN-ENGAGES test:**
> An episode's first 10 numbered-line bones must contain at least one of: (i) a board-change beat (a state-change or board-state shift visible at bone level); (ii) a tension-bearing image carrying forward state from the prior episode's close; (iii) a season-plan-designated establishing-register beat (e.g., the early-baseline ecological uncanny). If none of (i)/(ii)/(iii) is present in the first 10 bones, flag `OPEN-ENGAGES-FAIL`. Note: (iii) requires explicit season-plan designation — the establishing register is permitted only where the plan names it.

**5b — CLOSE-EARNS-NEXT test:**
> An episode's final 5 numbered-line bones must contain at least one of: (i) a board-change beat that is not yet resolved at the close; (ii) a forward-momentum image (active subject + forward verb) that earns a specific next-open. The close must NOT land on aftermath-of-aftermath: if the episode's last board-change is more than 20 bones before the close, flag `CLOSE-EARNS-NEXT-AFTERMATH-DRIFT-{N}` where N is the bone count.

**5c — SHAPE-COHERENT test:**
> Within the episode's body, the bone-density of board-changes must produce a recognizable rise/peak/fall scaled to episode size. Specifically: if the episode has fewer than 1 board-change per 30 bones in any 30-bone window, flag `SHAPE-COHERENT-FLATLINE-{line-range}`. The peak board-change must land in the back two-thirds of the episode body (matching S2's "back half" rule at episode scope).

**Validation corpus for V2:** apply 5a/5b/5c to s01e01–s01e06 under the *current* split; the audience's STRONG seams should be the units flagged. If the V2 mechanics flag the same seams the audience surfaced, the mechanics are calibrated correctly.

**Cost:** medium. Rubric clause edit + 6-episode validation pass.

---

## Carry-back item 6 — Cross-episode continuity post-split (Gap 2)

**Source:** B-baseline Gap 2; C-seams Axis 3 (5 of 5 boundary continuity units returned STRONG/MODERATE seams); E-r2 routed all 5 to REVISE.

**The gap:** S4 covers continuity inside the aggregate. The rubric does NOT describe a continuity check across the post-split episode boundaries. State carryover from `s01eN.md` close → `s01e(N+1).md` open is implicitly covered by the `aggregate_range:` contiguity check, but a reader experiencing the split as discrete episodes meets a different continuity surface than a reader experiencing the aggregate continuously. No rubric pass tests this.

**Candidate V2 mechanic (new pass S4.5):**

> **Pass S4.5 — Post-split continuity (auditor, runs after Phase 4 split is finalized).**
> Inputs: per-episode proto-line files; aggregate; season-plan. Brief: for each episode boundary N → N+1, verify that the state-changes in N's close region (last 20 bones) are visible as active constraints in N+1's open region (first 10 bones). Specifically, for each board-change in N's last 20 bones that introduces a new state (apprentice-mark; pastoral-claim; surveillance-record; debt; letter-event), the N+1 open must carry at least one bone signaling that state as active in the POV character's working state — physical-register, not exposition.
> Verdict per boundary: `BOUNDARY-CARRIES` or `BOUNDARY-DROPS-{state}`. File-level: `POST-SPLIT-CONTINUITY-OK` or `POST-SPLIT-CONTINUITY-FAIL-{boundary-list}`.

**Validation corpus for V2:** s01 has 5 boundaries; the audience surfaced 5 continuity gaps (U7–U11). Under the new S4.5, all 5 should flag, matching the audience's findings. The targeted bone additions routed in E-r2 (U7, U9 cascade-fix, U10, U11) close 4 of 5; U8 closes structurally if U13 cut moves to ~207. After execution, S4.5 should return clean.

**Cost:** medium. New rubric pass + 5-boundary validation on s01 + integration into /and-season command.

---

## Carry-back item 7 — Entertainment-density threshold reconciliation (Gap 6)

**Source:** B-baseline Gap 6; F-final shippability assessment.

**The gap:** S3 caps at "~10% of windows TOLERATED, zero BORED, two consecutive BORED → REVISE." S9 caps at "≥30% of any 100-line stretch BORED-or-TOLERATED → COMPREHENSIBILITY-RISK." The two thresholds are non-equivalent; on s01, S3 ACCEPT was reached after multiple revisions, but S9 still triggered (dark-fantasy-reader: COMPREHENSIBILITY-RISK-attention-early-baseline-gap-density). Either both thresholds are correct and serve different purposes (entertainment cap vs comprehensibility floor) — in which case the rubric should say so explicitly — or they should converge.

**Candidate V2 reconciliation (two options):**

**Option A — explicitly named different purposes:**
> S3 (Trim) is the *entertainment cap* — what the audience would pay to read. ~10% TOLERATED + zero BORED + two-consecutive-BORED trigger.
> S9 (Comprehensibility) is the *attention floor* — what the audience can sustain reading. ≥30% B-or-T in 100-line stretch trigger.
> The two passes can return non-aligned verdicts and both are valid — entertainment cap can be passed while attention floor fails (slow-but-engaging), and vice versa.

**Option B — converge to single threshold:**
> Both passes use the same threshold. Recommended: ≥20% TOLERATED in any 50-line stretch + zero BORED + two-consecutive-BORED. S3 and S9 then differ only in lens (taste vs comprehensibility), not threshold.

**Recommendation:** Option A (explicit different purposes) is consistent with how the rubric currently names them (Trim is a taste cut; Comprehensibility is a comprehension floor). The reconciliation is documentation, not a threshold change.

**Cost:** small. Rubric clause clarification only.

---

## Carry-back item 8 — Season-scope adversarial criteria per persona (Gap 7)

**Source:** B-baseline Gap 7; C-seams used implicit per-persona habits without a formal documented standard.

**The gap:** Per-line and per-episode adversarial habits are implicit in the persona cards. Season-scope adversarial habits (multi-stretch arc-fatigue, escalation-curve plausibility, monument-callback debt, idiom depletion across multi-episode arcs) are not separately documented. The Phase C subagent had to derive them from the persona cards + corpus + locked rubric.

**Candidate V2 addition:**

> Each persona card's `class: persona` schema (under `schemas/card.schema.md`) gains a season-scope-adversarial section listing 3–5 named attack categories. Examples:
> - `dark-fantasy-reader` season-scope: atmospheric drift across multi-episode arcs; procedural recurrence (anti-pattern: structural beats repeating across 3+ episodes); cost-not-landing across an arc; tonal flatline.
> - `pulp-enthusiast` season-scope: momentum dead zones across multi-episode arcs; board-change density collapse; close-earns-next quality at episode boundaries.
> - `worm-canon-pedant` season-scope: voice-fidelity drift across multi-episode arcs; shard-cost suppression; cost-language vs discipline-language register; idiom depletion suppressing cost-signal.

**Cost:** small for the schema edit; small for the per-persona card updates.

---

## Carry-back item 9 — S6 vibe-drift escalation resolution path (Gap 4)

**Source:** B-baseline Gap 4; observed in s01 nine-pass run (S6 r1 fired 2-of-3 drift; resolution was "carry-forward" per `escalation-s6-vibe-drift-carry-forward.md`).

**The gap:** The rubric says "≥2-persona threshold for accepting drift flags" — this was met — but the resolution path is unclear. Do drift findings route to fixer? Screen-writer? Or is "carry-forward" the rubric-permitted close? The rubric does not say.

**Candidate V2 resolution:**

> When S6 returns ≥2-persona VIBE-DRIFT, the routing is:
> - If the drift is localizable to a stretch (e.g., `VIBE-DRIFT-procedural-recurrence-{line-range}`), route to screen-writer for stretch regeneration.
> - If the drift is non-localizable / season-wide (e.g., `VIBE-DRIFT-shard-load-suppressed`), route to a season-scope screen-writer pass on the named pattern, OR to a Phase H carry-back if the rubric lacks a mechanic for the specific drift form.
> - "Carry-forward" is permitted only when the drift is acknowledged in the season-plan (the season-plan §H structural notes already cite shard-load and procedural recurrence as carry-forward signals). Otherwise the drift must be resolved in-pass.

**Cost:** small. Rubric clause edit only; no immediate corpus impact (s01 already shipped with carry-forward acknowledgment).

---

## Carry-back item 10 — S8a/S8b split verdict adjudication (Gap 5)

**Source:** B-baseline Gap 5; observed in s01 nine-pass run (S8a IMPLAUSIBLE on Elara visit; S8b PLAUSIBLE on the same beat).

**The gap:** When the character lens (S8a) and event lens (S8b) return different terminal verdicts on the same beat, the rubric does not describe what to do. The shipped s01 state takes both at face value — IMPLAUSIBLE-CHARACTER-oc-craftsman-mother carry-forward stands, S8b PLAUSIBLE stands. A reader does not compute character vs event separately; they read one beat.

**Candidate V2 resolution:**

> When S8a and S8b return divergent verdicts on the same beat, the divergence triggers a `S8-SPLIT-VERDICT-{slug}-{beat}` flag. Resolution: the more restrictive verdict wins by default (IMPLAUSIBLE-CHARACTER overrides PLAUSIBLE-EVENT). Override path: if the season-plan or a condition-card explicitly licenses the divergence (e.g., "this character's behavior is permitted by political-physics card despite character-card's information-suppression pattern"), the override must cite the licensing card and the divergence converts to `S8-LICENSED-DIVERGENCE-{card-slug}`.

**Effect on s01:** the Elara visit at e06 currently carries a `S8a IMPLAUSIBLE / S8b PLAUSIBLE` split. Under V2: the divergence converts to either `S8-SPLIT-VERDICT-Elara-reeve-visit` (IMPLAUSIBLE wins by default) or `S8-LICENSED-DIVERGENCE-cond-smallfolk-political-physics` (the political-physics card licenses the membrane interaction). E-r2 U6 routes the bone-level register fix; under V2, the verdict structure becomes explicit.

**Cost:** small. Rubric clause edit only.

---

## Summary

10 carry-back candidates produced by Run R1. Categorized:

| Item | Type | Cost | Source |
|---|---|---:|---|
| 1. Idiom depletion mechanic | Rubric (new fault class) | medium | U17, fault-AP-1 |
| 2. Denouement-share quantification | Rubric (threshold) | small | U1 |
| 3. Narrator-field rule for interludes | Rubric (clause) | small | Gap 8, fault-005 |
| 4. Aggregate non-monotonic IDs | Schema (clarification) | small/medium | fault-001 |
| 5. Episode-shape mechanics | Rubric (3 new tests) | medium | Gaps 1+3 |
| 6. Post-split continuity pass | Rubric (new pass S4.5) | medium | Gap 2 |
| 7. Entertainment-density reconciliation | Rubric (clarification) | small | Gap 6 |
| 8. Season-scope adversarial criteria | Schema (per-card section) | small | Gap 7 |
| 9. S6 drift resolution path | Rubric (clause) | small | Gap 4 |
| 10. S8a/S8b split adjudication | Rubric (clause) | small | Gap 5 |

**Total estimated effort to land all 10 in V2:** medium-to-large session of rubric drafting + per-candidate validation against s01 corpus.

**Items that block downstream execution of E-r2 routing:**

- **Item 4 (fault-001 schema clarification)** blocks fixer routing for any s01e01 bone in the non-monotonic region. Human escalation.
- **Item 3 (narrator-field rule)** blocks fault-005 fix; the e06 narrator field stays as-authored until Phase H verdict.

**Items that do NOT block execution:**

- Items 1, 2, 5, 6, 7, 8, 9, 10 are V2 candidates that improve the rubric for future runs but do not block s01 R1 execution. The E-r2 REVISE routing for U17 (idiom depletion), U1 (post-IGNITION ratchet-clicks), U2 (e01 latent-cost bones), U7/U9/U10/U11 (continuity bones), U6 (Elara register), U12 (e01 cut shift), U16 (e05 placement, with fault-004 amendment) all proceed under V1.

---

## Mirror to upstream-tuning-queue.md

The 10 items are mirrored as URI-007 through URI-016 in `design/shoot-v2/upstream-tuning-queue.md`. See queue file for canonical entries.

## Phase H complete

Tuning R1 is closed at decision level. All carry-back items are queued; downstream execution proceeds per E-r2 routing (with two human escalations: fault-001 schema and fault-005 narrator field via Item 3 verdict).
