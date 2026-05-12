---
audit: facets-final-r1
episode: s01e02
date: 2026-05-11
mode: flag-only
status: FINDINGS-PRESENT
totals: 8 findings across 6 facets (1 HARD + 7 SIGNAL)
---

# Facets Final Audit — s01e02

Auditor: cross-cutting graph auditor fork (Phase 5 of /and-facets)
Mode: FLAG-ONLY. No mutations performed. HARD findings are flagged for fixer dispatch; SIGNAL findings are advisory and do not block Phase 5b.

---

## STRUCTURAL findings (2)

**Finding S-001 — metaphor:2 anchor resolves to a deleted memory entry (HARD)**

[metaphor:2] @114 — R2 concurrent-fork anchor-deletion collision. The R2 memory judge deleted mem:5 @107 (VERDICT: DELETE-spine-missing). The R2 metaphor judge in the same parallel block resolved meta:2's provisional `licensed-by:` hint to `mem:5 +tens:1`. These two forks ran concurrently and each operated on its own self-scoped file; neither could observe the other's deletions during the R2 pass. The post-R2 canonical memory.md contains IDs 2, 3, 4, 7, 9, 10, 11, 12 — ID 5 is absent. The cite-index `meta:2 @114 lic-out=[mem:5, tens:1]` references mem:5, which does not appear in the `### mem` section of the post-R2 cite-index. The `licensed-by:` field is unresolvable against the canonical graph. **HARD.**

**Finding S-002 — state-updates consolidated file has duplicate source-header lines (SIGNAL)**

[state-updates.md consolidated] — The consolidation produced adjacent duplicate comment-markers for each per-character source section. Example: `# source: oc-broken-maester` appears twice consecutively before that slice's entries (visible at lines 25-26 of the consolidated file). Same pattern occurs for oc-dock-runner, oc-tanner-elder, oc-tanner-father, oc-tanner-mother, taylor-hebert-flea-bottom. The per-character source slice files themselves do not exhibit the duplication. This is a merge artifact in the consolidated file; the canonical entry data and cite-index integrity are unaffected. **SIGNAL** (cosmetic merge artifact).

---

## FREQUENCY-BAND findings (2)

**Finding F-001 — tens frequency-band: EXEMPT-UNDER-TONE-LAW (no finding)**

Tens distribution: 1s 81.5%, 2s 14.3%, 3s 4.2% (155 entries). All three rungs breach the standard band (60-75% 1s / 20-30% 2s / 5-10% 3s). Exemption 5 (exempt-tone-law-slow-burn) is claimed in the tensometer footer. Criteria verified against `design/shoot-v2/rubric-tensometer.md` §"Frequency-band exemptions" Exemption 5 and `cond-series-tone-constraints-125ac`:

- **(a) tone-law citation:** `cond-series-tone-constraints-125ac` confirmed present in `active-project/warehouse/`. Card §"The Primary Register" explicitly declares "Slow-burn / low-rupture-density register. Foreknowledge-clamp as primary register" and states "The standard tens frequency-band gate ... does not apply." PASS.
- **(b) quantified relaxed band:** Card §"Relaxed tens frequency-band for this config (URI-034 Exemption 5)" specifies "1s: 75-85%; 2s: 12-22%; 3s: 4.5-10% season-average, 4.0-10% per-episode." Positive numbers present. PASS. Episode actuals (1s 81.5%, 2s 14.3%, 3s 4.2%) all fall inside the relaxed band.
- **(c) 3s rung discipline:** Per-episode 3s rate 4.2% ≥ relaxed per-episode floor 4.0%. (c.i) Every named scene carries a resolved peak per the tensometer's Kickbacks section: Scene A @22, Scene H @125, Scene L @173 all declared RESOLVED. (c.ii) Scalar inflation refused per AP4 (explicit in tensometer §Frequency-band). PASS.
- **(d) season-wide scope:** Card states "The relaxed band applies across every episode of every season under this tone-law." s01e01 and s01e03 file independent Exemption 5 claims under the same card. PASS.

**Exemption verdict: EXEMPT-UNDER-TONE-LAW. No HARD finding.**

**Finding F-002 — feeling aggregate sparsity 5.8% marginally above 5% ceiling (SIGNAL)**

[feeling.md] — 9 total firing entries across 155 proto-lines = 5.8% aggregate episode rate. The schema states "Sparsity 2-5%." If the sparsity gate is interpreted as an aggregate-episode rate (all character fires combined against total proto-lines), 5.8% breaches the 5% ceiling by 0.8 points. Per-character individual rates: taylor-hebert-flea-bottom 4/155=2.6%, oc-tanner-father 2/155=1.3%, oc-tanner-elder 2/155=1.3%, oc-tanner-mother 1/155=0.6%, oc-broken-maester 0, oc-dock-runner 0. All individual per-character rates fall below 5%. The rubric's per-character-per-scene cap (≤1 hard) is a separate gate that all entries satisfy. The schema does not explicitly disambiguate whether "2-5%" is per-character-episode or aggregate-episode. At 5.8% aggregate the breach is marginal; per-character rates are all clean. **SIGNAL** (ambiguous rubric scope; marginal aggregate breach).

---

## METADATA-INCONSISTENCY findings (2)

**Finding M-001 — NI shard frontmatter uses f-r2-counts as verdict-class counts, not failure-code counts (SIGNAL)**

[.r2-decisions.md §narrator-interest shard] — Shard frontmatter: `f-r2-counts: {f-r2-1: 0, f-r2-2: 32, f-r2-3: 0, f-r2-4: 5}`. Per `schemas/audit-report.schema.md` §F-R2-* class definitions, f-r2-2 = "motive-honesty failure" and f-r2-4 = "graph-incoherence." The NI shard's values (f-r2-2: 32, f-r2-4: 5) are KEEP and ADD verdict counts respectively, not failure-code counts. The consolidator note in `.r2-decisions.md` documents this: "NI shard frontmatter mis-uses f-r2-counts as K/A counts... Corrected here to the canonical F-R2 failure-code interpretation." The corrected consolidated frontmatter sets these to 0. The source shard is preserved uncorrected. The consolidator's correction is procedurally appropriate; the source shard inconsistency is documented. **SIGNAL** (consolidator addressed; source shard preserved for traceability per documented intent).

**Finding M-002 — oc-tanner-elder feeling shard classifies a REVISE verdict as F-R2-3 (SIGNAL)**

[.r2-decisions.md §feeling — oc-tanner-elder shard] — Shard frontmatter: `f-r2-counts: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 1, f-r2-4: 0}`. The shard's sole verdict was REVISE on feel:2 @54 (G3 adjacent-context lean — the content of the entry leaned on adjacent beats to read). Per the F-R2 taxonomy: F-R2-3 is "niche-driven add: R2 added an entry that the layer's rubric does not warrant." A REVISE (content-swap on an existing entry) is not an add; classifying it as F-R2-3 misapplies the failure taxonomy. A G3 form-discipline failure on a REVISE would classify as F-R2-1 ("rubric-form discipline failure") if it classifies at all — though the R2 pipeline treats REVISE as a permitted correction verb rather than a discipline failure per se. For comparison, the oc-tanner-father shard classified an identical REVISE verdict as 0 across all F-R2 codes. The elder shard's `f-r2-3: 1` propagated into the consolidated total (`f-r2-counts: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 1, f-r2-4: 0}`). Per the orchestrator-critic contract, the SIGNAL threshold is `f-r2-2 + f-r2-3 + f-r2-4 > 2`; current consolidated total is 1, below threshold. **SIGNAL** (taxonomy misclassification in source shard; does not affect gate).

---

## CURVE-SHAPE verdict

**Episode-level: SHAPE-OK.**

- Scene-level peaks: Scene A peak @22 (r=3, father's step-back, body-committed-withdrawal). Scene H dual-peak @85 (r=3, latch-break) and @87 (r=3, family-exit): the @86=r=2 intervening beat makes this a 3→2→3 sequence — permitted per rubric "3→3 only when the second 3 reverses or commits the first" (family-exit commits the latch-break). Scene H secondary rupture @125 (r=3, stylus-drop). Scene L peak @173 (r=3, mother stands). All named scene-rupture sites carry peaks. PASS.
- Rise-to-peak adjacency: @22 is preceded by @14=r=2, @15=r=2, @16=r=2, @17=r=2 — four-beat 2-ramp. CLEAN. @85: immediate approach is @83=r=1, @84=r=1 → @85=r=3. This is a 1→1→3 sequence: two consecutive r=1 beats before the rupture with no r=2 immediate approach. The rubric states "beats leading into a 3 should ramp through 2s, not jump from 1 directly; direct 1→3 jumps are flagged as either misratings or true sudden-turns." The lords-man's entrance (@83, narrator:15 firing "wrong leverage-load for an Eastern-Quarter alley") and the lords-man speaking to the family (@84) are both rated r=1. The approach at @65=r=2, @66=r=2 in the prior block provides distant approach signal, but the immediate adjacency fails the ramp test. **One 1→3 adjacency gap flagged at @83-@85.** @125 is preceded by @124=r=2 — CLEAN. @173 is preceded by @172=r=2, @171=r=1, @170=r=1, @169=r=1, @168=r=1, @167=r=2 — two-beat 2s approach via @167 and @172 with quiet beats between; CLEAN.
- 3→3 sequences: @85=3 and @87=3 with @86=2 intervening — not consecutive. No 3→3 adjacency violations.
- Flatlining 30+: Longest identifiable contiguous r=1 run in the proto-lines: the network-spread block @60-@76 (bones @60, @61, @62, @63, @64, @65, @66, @67, @68, @69, @70, @71, @72, @73, @74, @75, @76 — 17 proto-lines). Some carry r=2 within (tens:54=r=2 @66, tens:57=r=1 @69, tens:61=r=1 @73). Counting strict r=1 only: @60, @61, @62, @63 (r=1), then @64=r=1, @65=r=1, @66=r=2 — run breaks at @66. Maximum strict-r=1 run ≈ 17 consecutive beats in the overnight-network-spread block. Well below 30-beat flatline threshold. CLEAN.
- Episode-level act structure: first-third peak at @22; middle-third climax at @85-@87 (eviction — densest cluster); late peaks at @125 and @173. Not structurally inverted (highest-peak-density in middle, not first third). SHAPE-OK.

**Flagged adjacency: 1→3 at @83-@85 (latch-break). Not a structural fail; flagged for dramatist review as a potential misrating or true sudden-turn documentation.**

---

## CONTRADICTION findings (0)

No incompatible state pairs found on the same anchor across facet files. The vigil-candle state is recorded by three separate entries: env state-update @173 (`prop:oc-vigil-candle.state: lit -> extinguished`), tanner-mother state-update @173 (`vigil-state: kept-for-tya -> extinguished`), and taylor state-update @171 (`knowledge.vigil-candle: lit -> extinguished`). These are distinct fields on distinct targets with different anchor points (@171 vs @173); not contradictory. No other incompatible pairs found.

---

## DEDUP findings (0)

No within-facet same-anchor duplicates and no cross-facet same-channel duplicates found. High-density pile-ups at @22, @107, @125, @159, @173 reviewed: all co-located entries occupy distinct facet classes with distinct content shape. No dedup finding.

---

## SUPERFLUOUS findings (0)

Lonely entries from the cite-index reviewed against rubric. Tens=1 entries are never superfluous per audit-class definition. Lonely non-tens entries: loc-state:4, loc-state:7-10 (all carry proto-line back-citations in the proto-lines file — the cite-index's `back=Y/N` field tracks co-location with other facets, not back-citation from proto-lines; all loc-state entries are cited by proto-lines); narrator lonely entries (R2 judge verified each at-rest; all KEPT with documented rationale); state:2 @73 (back-cited from `[state:2]` on proto-line @73); feel:2 @54 (back-cited from `[feel:2]` on proto-line @54); vibes:20 @169 (back-cited from proto-line @169). meta:2 @114 — survivability under rubric contingent on resolution of Finding C-001 (the HARD CONSTRAINT finding); not independently superfluous if the anchor is repaired. No superfluous entries independent of the anchor fault.

---

## CONSTRAINT findings (1)

**Finding C-001 — metaphor:2 `licensed-by:` cites deleted memory entry (HARD)**

[metaphor:2] @114 — `licensed-by: mem:5 +tens:1`. This constraint violation is the downstream consequence of the R2 concurrent-fork collision documented in Finding S-001. mem:5 was deleted from the canonical graph by the R2 memory judge. The schema requires metaphor entries to carry a "machine-resolvable `licensed-by:` anchor." The `licensed-by:` field cannot resolve: mem:5 does not exist in the post-R2 memory.md or the post-R2 cite-index. The figure itself ("the entry is a receipt she writes for herself") is structurally coherent — the coin-payment/wage-claim-formalization register that mem:5 represented is a real narrative beat. But the anchor is absent. **HARD.**

Criteria for fixer: the `licensed-by:` field must resolve to a currently-existing post-R2 memory or feeling entry whose content covers the coin-payment or wage-claim-formalization register at or near @107-@114. Candidate anchors from the surviving graph: feel:8 @106 (`taylor-hebert-flea-bottom: counts the coins a second time across the open palm before extending | expressed: partial`) — somatic tell on the coin-extension beat; feel:3 @22 is on a different beat. No surviving memory entry directly covers the transactional-surface-closes-around-the-gap register at @107 (mem:5 was the only one). If no clean anchor exists, the entry must be deleted and the cite-index `[meta:2]` citation stripped from proto-line @114.

---

## AP-SCAN findings (2)

**Finding A-001 — tens approach at @83-@84 lacks r=2 ramp before the @85 latch-break peak (SIGNAL)**

[tens:70 @83, tens:71 @84] — The lords-man enters the alley (r=1) and the lords-man speaks to the tenant family (r=1), followed immediately by the latch-break at @85 (r=3). The rubric adjacency test states: "beats leading into a 3 should ramp through 2s, not jump from 1 directly." narrator:15 fires at @83 reading "the lords-man's gait has the wrong leverage-load for an Eastern-Quarter alley" — the pre-calc channel lighting on a stakes-visibility axis, which would make @83 a candidate for r=2 under the rubric's stakes-visibility axis ("watch-cost: the officer's gaze fixes on Taylor at the yard's far end" is given as a r=2 exemplar). The dramatist rated @83=r=1. AP1 anti-pattern (ambient escalation) prohibits bumping because the scene is tense — but the converse question here is whether the approach beat is *underrated* (AP-inverse: approach too quiet given the NI fire). **SIGNAL.** Auditor cannot resolve the misrating question without dramatist's axis-citation. Flagged for dramatist review.

**Finding A-002 — metaphor:1 at tens=1 anchor (AP7 tens ≠ 3 default-refuse discipline) (SIGNAL)**

[metaphor:1] @89 — `simile: the flies are an ear pressed to a wall | licensed-by: feel:7 +tens:1`. The tens rubric cross-facet contract states: "Metaphor flags. Default permitted only at tens = 3. Metaphor at tens = 1 is almost always cut." The metaphor rubric's AP7 is "default-refuse at tens ≠ 3." The R2 metaphor judge KEPTs this with a documented defense: the figure names the instrument's condition (passive reception) consistent with Taylor's operational register, and the figure does not ornament — it is the content of the eviction-witness posture. The judge's defense invokes the "almost always" exception in the rubric. The defend-space exists; the fire is held. AP7 flag is documented here as a Phase 5b adversarial-gate candidate for the audience to evaluate whether the tens=1 defense is earned. **SIGNAL.** (Note: metaphor:2's AP7 status is subsumed by the HARD CONSTRAINT finding C-001.)

---

## TASTE-FLAG findings (1)

**Finding T-001 — eviction approach @83-@84 momentum-stall candidate (SIGNAL)**

[tens @83-@84] — The lords-man's entrance and initial speech to the tenant family are both rated r=1 and neither carries non-tens facet citation except narrator:15 at @83. Arriving at the episode's climax scene (middle-third-peak per the tensometer's Window Shape), two consecutive bare r=1 beats before the r=3 latch-break could read as a momentum-stall rather than a deliberate approach. The contemplative-procedural-horror register under Exemption 5 licenses quiet approach; whether this specific approach is quiet-by-design or under-charged is an audience-gate question. **SIGNAL** (atmosphere-thin candidate; overlaps with A-001; route to Phase 5b audience).

---

## PILE-UP REVIEW (5 pile-ups reviewed)

- **@173** (11 facets): `oc-tanner-mother stands`. feel:1, mem:12, narrator:31, sensory:5, state:4, state:8, state:9, vibes:18, vibes:19, vibes:22, vibes:23. Verdict: **WARRANTED.** Scene L rupture (r=3), the episode's terminal structural peak. Three simultaneous state-changes (mother's posture, mother's vigil-state, taylor's knowledge.vigil-candle), one memory discharge (failed-recognition-by-dying-parent, third variant), one sensory inflection (chair-floor-creak), one feeling entry (mother's thumb-on-bench-edge before rising), one NI entry (standing IS the vigil ending), four vibes entries (two on the mother with distinct keywords, one on taylor extending existing keyword, one on loc and episode scope). Each entry occupies a distinct facet class with distinct content. The density is structurally appropriate for an irreversible grief-ritual closing at the episode's terminal rupture. No over-decoration.

- **@22** (7 facets): `oc-tanner-father steps back`. feel:1, narrator:6, state:2, state:3, vibes:1, vibes:2, vibes:3. Verdict: **WARRANTED.** Scene A rupture (r=3). Two simultaneous state-changes (stance-on-tya-category + proximity-to-taylor), one feeling entry (rear-foot weight + gaze-on-strap-end), one NI entry (step-back as body-confirmation of new category), three vibes entries (father withdrawal++ extending existing keyword, new keyword on father for suppressed-declaration-enacted, taylor witness++ extending the-Tya-shaped-debt). All entries carry distinct content. WARRANTED.

- **@125** (6 facets): `taylor-hebert-flea-bottom drops the stylus`. mem:10, narrator:23, sensory:3, state:7, vibes:9, vibes:10. Verdict: **WARRANTED.** Scene H rupture (r=3). One state-change (physical_condition intact→migraine-onset), one memory discharge (operational-cost-at-prior-scale monument), one sensory inflection (stylus-drop-clatter spike), one NI entry (apparatus reporting failure before apparatus has noticed), two vibes entries on taylor (first-physiological-cost new keyword, range-cost-registered on loc:loc-flea-bottom-base new keyword). Each distinct. WARRANTED.

- **@107** (5 facets): `oc-tanner-father takes the coins`. feel:2, state:5, state:7, vibes:6, vibes:7. Verdict: **WARRANTED.** Scene F coin-acceptance (r=2). Two state-changes on distinct targets (tanner-father wage-claim-state, taylor knowledge.tanner-wage-claim), one feeling entry (hand-closes-on-coins without gaze-lift), two vibes entries with distinct keywords on distinct targets (father task-yield-result, episode debt-payment-precedent). All distinct. WARRANTED.

- **@159** (5 facets): `the beetles relay oc-broken-maester`. mem:7, narrator:29, vibes:15, vibes:16, vibes:17. Verdict: **WARRANTED.** Maester-named-subject threshold (r=2). One memory discharge (swarm-feed-as-cognition-extension), one NI entry (maester relay-route names him no longer hypothesis), three vibes entries (two on maester with distinct keywords, one episode scope). The absence of a state-update co-cite at this r=2 beat is not a fault — state:32 @145 records the canonical named-log-entry transition one beat prior at the log-write; @159 is the beetles-relay confirmation, not the initial recording event. WARRANTED.

---

## Audit summary

- Total entries reviewed: 285 facet entries (155 tens + 12 loc-state + 37 NI + 5 sensory + 34 state + 8 memory + 9 feeling + 2 metaphor + 23 vibes); 155 proto-lines; 5 pile-ups; 1 consolidated R2 decisions file
- **HARD findings: 1** — S-001/C-001 ([metaphor:2] — R2 concurrent-fork anchor-deletion collision + unresolvable licensed-by). These two findings target the same entry and will be resolved by a single fixer action.
- **SIGNAL findings: 7** — S-002 (state-updates duplicate headers); F-002 (feeling aggregate 5.8%); M-001 (NI shard f-r2-counts misuse); M-002 (elder feeling shard F-R2-3 misclassification); A-001 (approach beats AP1 candidate @83-@84); A-002 (metaphor:1 AP7 tens=1 discipline); T-001 (eviction approach momentum-stall candidate)
- **FREQUENCY-BAND:** tens EXEMPT-UNDER-TONE-LAW (all criteria satisfied); sensory 3.2% within 3-6%; memory 5.2% within 5-12%; NI 23.9% within 15-25%; metaphor 1.3% within 0-3%; feeling 5.8% aggregate SIGNAL.
- **CURVE-SHAPE:** SHAPE-OK. One flagged adjacency (1→3 at @83-@85 latch-break approach). Exemption 5 relaxed-band in effect; no structural fail.

---

## Routing

Flag-only mode — no executes issued.

**HARD findings — route to fixer before Phase 5b:**

| Finding | Entry | Author | Action required |
|---------|-------|--------|-----------------|
| S-001 + C-001 | [metaphor:2] @114 | editor (metaphor author) | Resolve `licensed-by: mem:5` to a currently-existing post-R2 anchor (candidate: feel:8 @106 or feel:3 @106 if feel IDs shifted) or delete the entry and strip `[meta:2]` from proto-line @114 in the canonical proto-lines file and cite-index. The figure is not faulted — only the anchor. |

**SIGNAL findings — advisory to respective authors; do not block Phase 5b:**

| Finding | Routing | Note |
|---------|---------|------|
| S-002 (duplicate source-headers) | studio (consolidation build process) | Cosmetic merge artifact; no content correction needed |
| F-002 (feeling 5.8%) | all feeling authors + editor | Track against s01e03; rubric scope ambiguity flagged |
| M-001 (NI f-r2-counts misuse) | POV impersonator (NI author) | Discipline note for future shards; consolidator already corrected |
| M-002 (elder feeling F-R2-3 misclassification) | oc-tanner-elder feeling author | Taxonomy note; consolidated total (1) below SIGNAL threshold |
| A-001 (approach beats @83-@84) | dramatist (tensometer author) | Review axis-citation for @83; confirm r=1 vs r=2 at approach to latch-break |
| A-002 (metaphor:1 AP7) | editor (metaphor author) | Advisory; R2 judge's defense documented; Phase 5b audience-gate to evaluate |
| T-001 (eviction approach) | Phase 5b audience | Momentum-stall candidate for adversarial review |
