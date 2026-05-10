audit: facets-final-r4
episode: s01e01
date: 2026-05-10
mode: flag-only
status: FINDINGS-PRESENT
totals: 12 findings across 4 facets (0 hard, 12 signal/soft)

---

## Comparison vs prior audits

audit-r1 (5-class, original):                        7 findings
audit-r2 (5-class, post-memory-remediation):         5 findings
audit-r3 (11-class, post-memory-tuning):            13 findings
audit-r4 (11-class, post-feeling-tuning):           12 findings

Hard-finding trajectory: 4 (r1) -> 0 (r2) -> 1 (r3) -> 0 (r4)
Signal-finding trajectory: 3 (r1) -> 5 (r2) -> 12 (r3) -> 12 (r4)

Note: The r3 HARD finding (struct-001, feeling.md ID non-monotonicity) is DOWNGRADED in r4 per URI-004. The per-section monotonicity convention (Taylor block ascending, mother block ascending, father block ascending) is the intended file structure for sub-sectioned facets. The audit-r3 STRUCTURAL check was over-strict; URI-004 directs updating the audit command to accept per-section convention. Net change r3→r4: -1 hard (struct-001 downgraded), +0 hard new; one new AP-SCAN finding and one new TASTE-FLAG finding introduced by feeling tuning. One prior AP-SCAN and one prior TASTE-FLAG from r3 are consolidated or re-scoped. Total count: 12 (from 13).

---

## STRUCTURAL findings (0)

**struct-001 (audit-r3) — DOWNGRADED.**

feeling.md ID arrangement: Taylor section 1,2,3,4,13; mother section 5,6,7,14; father section 9,10,11. Each per-character section is strictly ascending. Deletion gaps (feel:8 deleted from mother section; feel:12 deleted from Taylor section) are correctly documented in round-notes. Cross-section ordering (Taylor ends at 13; mother starts at 5) is the intended per-section convention for sub-sectioned facets, per URI-004. The schema requirement "IDs strictly increasing within each facet file" is satisfied within each logical subsection. URI-004 names this as an audit over-strictness requiring a command-file edit; the finding is not re-raised as a HARD fault.

Disposition: DOWNGRADED — per-section monotonicity accepted as convention for sub-sectioned facets per URI-004 (cost: small; command-file edit to `and-facets-audit.md` pending).

---

## FREQUENCY-BAND findings (2)

Unchanged from audit-r3. The proto-lines did not change; tens distribution is stable.

- [freq-001] **tensometer — rung-3**: actual 2/102 = **2.0%**; band 5-10%; **breach-low**. The episode has only 2 entries at rung-3 (@83 and @99). The tensometer file's own header comment acknowledges: "3-rung SOFT-FAIL — 2.0% < 5-10% target band." Root cause is upstream (URI-002 protoline scene-peak coverage gap). Both freq-001 and freq-002 are downstream symptoms of the same upstream structural gap.

- [freq-002] **tensometer — rung-1**: actual 79/102 = **77.5%**; band 60-75%; **breach-high**. The 1-rung is elevated above the upper band boundary. Inverse symptom of freq-001. Both findings persist at identical values; the feeling tuning did not alter the tens facet.

Per-facet distribution table:
| Facet | Metric | Actual | Band | Status |
|---|---|---|---|---|
| tensometer rung-1 | % of 102 | 77.5% | 60-75% | breach-high |
| tensometer rung-2 | % of 102 | 20.6% | 20-30% | within |
| tensometer rung-3 | % of 102 | 2.0% | 5-10% | breach-low |
| NI density | fires/102 | 23.5% | 15-25% | within |
| sensory sparsity | fires/102 | 4.9% | 3-6% | within |
| sensory modality coverage | distinct modalities | 3 (thermal, smell, light) | ≥2 | within |
| memory sparsity | fires/102 | 7.8% | 5-12% | within |
| feeling sparsity (Taylor) | fires/102 | 4.9% | 2-5% | within |
| feeling sparsity (Mother) | fires/102 | 3.9% | 2-5% | within |
| feeling sparsity (Father) | fires/102 | 2.9% | 2-5% | within |
| metaphor sparsity | fires/102 | 0.0% | 0-3% | within |
| state-updates density | fires/102 | 21.6% | ~8-18% | breach-high (soft) |

Note on state-updates: unchanged from r3; see r3 note on 102-beat scale adjustment.

---

## METADATA-INCONSISTENCY findings (2)

- [meta-001] **memory.md** — r2_to_r3 round-note stale claim (carried from audit-r3). The r2_to_r3 line claims "quiet-beat anchor 8/8 (all tens=1 or trailing-edge)" but this is contradicted by the Phase 4 defense for mem:8 which constructs an episode-arc release-zone argument, explicitly acknowledging the zone-class is contested. The r2_to_r3 claim predates the Phase 4 revision and was not updated. **Carried forward unchanged from audit-r3.** Routing: taylor-hebert-jaehaerys impersonator (memory author) — correct the r2_to_r3 quiet-beat claim at next file-touch to reflect the Phase 4 episode-arc release-zone argument for mem:8, or add a superseding r3_to_r4 note.

- [meta-002] **feeling.md — father section** — r2_to_r3 forbidden-vocabulary check contradicted by actual content. Line 38 of feeling.md (father section r2_to_r3 round-note) contains: `# forbidden-vocabulary check: clean — no named-feeling, no "feels" verb, no hedges, no similes, no comparisons, no compound-naming`. However the actual feel:10 entry at line 41 reads: `the voice steps down a margin the way an estimate gets one; the eyes mark the loft once and come back to her`. The phrase "the way an estimate gets one" is a comparison construction (comparison operator "the way" equivalent to "as"). The r2_to_r3 note was written before Phase E tuning; after Phase E revision, the comparison violation was introduced. The round-note was not updated to reflect the Phase E mutation. The note now contradicts the file's own content. **New finding introduced by feeling tuning.** Routing: oc-craftsman-father impersonator — update the r2_to_r3 forbidden-vocabulary claim in the father section to reflect that feel:10 was revised during Phase E and that the Phase E revision introduced a comparison violation subsequently flagged as REJECT in Phase F adjudication; the note should not claim "no comparisons" while the file contains feel:10 in its current REJECT-flagged state.

---

## CURVE-SHAPE verdict

**Episode-level: SHAPE-FAIL** — unchanged from audit-r3. The feeling tuning did not alter the tens facet or the proto-lines.

- **Act structure**: two peaks at @83 and @99, both in the second half; @99 is the structural climax (densest cluster, 15 co-facets). Episode is not inverted. Act structure sound on this axis.
- **Climax uniqueness**: PASS. @99 is the uniquely dense cluster.
- **Scene-level peak coverage**: FAIL. 6 of 8 scenes lack any rung-3 entry with no dramatist-flagged exception.
  - Scene 1 (@1–@7, dawn/shutter-shut): no rung-3. No exception flagged.
  - Scene 2 (@8–@31, morning/shutter-open): no rung-3. No exception flagged.
  - Scene 3 (@32–@57, afternoon/workshop-door-open): no rung-3. No exception flagged.
  - Scene 4 (@58–@60, dusk/tallow-lamp-lit): no rung-3. No exception flagged. (3-beat scene; may qualify as transit if dramatist argues.)
  - Scene 5 (@61–@91, evening/loft-vent-open): rung-3 at @83. PASS.
  - Scene 6 (@92–@125, late-evening/ledger-open): rung-3 at @99. PASS.
  - Scene 7 (@126–@129, night/winter-candle-drawn): no rung-3. No exception flagged.
  - Scene 8 (@130–@131, late-night/winter-candle-lit): no rung-3. No exception flagged. (2-beat scene; may qualify as transit if dramatist argues.)
- **Adjacency (1→3 jumps)**: 1 instance. @81=r=1, @82=r=1, @83=r=3 — direct 1→3 jump; broader approach includes @67=2, @69=2 (several beats earlier) but immediate pre-peak beats are rung-1. Flagged.
- **Adjacency (3→3 sequences)**: 0. PASS.
- **Flatlining**: not present. Longest rung-1 run is ~8 content-bearing beats. PASS.

Tensometer header comment anticipated this finding: "Pending Round-2 verdict; flag for re-author if curve-shape audit is added at Step G." Root cause is URI-002 (upstream protoline scene-peak coverage gap).

---

## CONTRADICTION findings (0)

None. State-update chains remain monotonically consistent (tallow-lamp: unlit→lit→guttering→dark; winter-candle: stored→drawn→lit; all other field-update chains single-entry or internally consistent). Location-state time progression monotonic (dawn→morning→afternoon→dusk→evening→late-evening→night→late-night). No cross-facet state incompatibilities detected. Unchanged from audit-r3.

---

## DEDUP findings (0 active)

No new DEDUP findings from feeling tuning. Prior flag-001 (mem:5 / narrator:26 @9) and flag-002 (mem:8 / narrator:25 @131) both resolved in audit-r3 by Phase 4 memory tuning revisions. The residual surface echo on flag-002 ("the day closes" / "closes the day") was named for stitcher-layer awareness in r3 and is not re-raised. No new DEDUP candidates introduced by feeling tuning.

---

## SUPERFLUOUS findings (0)

All 7 lonely entries from cite-index (loc-state:5 @61, loc-state:6 @92, narrator:2 @4, sensory:2 @3, state:7 @122, feel:13 @129, feel:14 @36) survive rubric scrutiny. Feeling tuning did not remove any of these entries; the Phase E revisions modified content but preserved anchors and IDs. Rubric scrutiny verdicts unchanged from audit-r3:

- loc-state:5 and loc-state:6: scene-entry frame-anchors for Scenes 5 and 6; rubric-licensed as first-beat place-anchors for inherited environments.
- narrator:2 @4: approach-zone channel-coverage fire (passive fauna-feed baseline establishment).
- sensory:2 @3: smell modality inflection (bare verb "stirs"; mordant-stir-sharp is audience-perceptible disambiguation).
- state:7 @122: genuine state-change (tallow-lamp lit→guttering) that drives @126 winter-candle draw.
- feel:13 @129: Q1-clean (no NI on @129), Q2-structural (pre-closure body-set), multi-justification ≥3/5.
- feel:14 @36: non-POV mother somatic-tell; Q1-clean (proto-line carries no interior); Q2-structural (first-steward-name landing); multi-justification ≥3/5.

---

## CONSTRAINT findings (3 — all soft, carried from r3)

Prior flags 003, 004, 005 from r2/r3 reviewed. Feeling tuning did not touch the memory facet, so these are unchanged.

- [flag-003] type: flag — **mem:2 @35 approach-zone quiet-beat (carried from r1/r2/r3).** The Phase 4 defense constructs a trailing-edge argument for @35 (the slip-drawing as aftermath of the @32 return-cluster). The argument is defensible but unverifiable without a dramatist-locked scene-frame. Rubric carry-back #1 (URI-001) is the structural resolution path. Disposition: soft flag (carried). Functional registers remain strong.

- [flag-004] type: flag — **mem:3 @69 approach-zone quiet-beat — Phase 4 adjudication accepted (carried from r1/r2/r3).** Audiences adjudicated this as ACCEPT in Phase 4 tuning (wcp ACCEPT, dfr ACCEPT, pe ACCEPT). The zone-class was adjudicated as trailing-edge. The mechanical concern (zone-class without dramatist-locked scene-frame) remains as a rubric-gap note per carry-back #1 (URI-001). Disposition: **soft flag downgraded — Phase 4 tuning closed the substantive concern.** Carried only as rubric-gap note.

- [flag-005] type: flag — **mem:8 @131 rising-2 at episode close; metadata inconsistency (superseded in part by meta-001, carried from r1/r2/r3).** Phase 4 revised the entry and constructed the episode-close release-zone trailing-edge argument. The tuning final accepted this defense (wcp ACCEPT-WITH-CAVEAT, pe ACCEPT). The metadata component is captured in meta-001. The substantive entry concern was adjudicated ACCEPT-WITH-CAVEAT in Phase 4. Disposition: **soft flag superseded by meta-001 for the metadata component.** Entry itself post-tuning cleared with caveats. Flag-005 is retired; meta-001 carries forward.

---

## AP-SCAN findings (6)

Findings ap-001 through ap-005 carried from audit-r3 (unchanged). One new finding introduced by feeling tuning.

- [ap-001] [tens:29 @34] AP5 stillness-inflation — candidate violation. "taylor-hebert-jaehaerys holds the feet" rated rung-2. The held-against-what (the slip discussion) is adjacent but not at the same beat's SVO. Per rubric: "the answer is 'the scene is tense'" is a rung-1 call; the on-face charge of Taylor-holds-feet is not independently legible from the proto-line alone. Soft AP5 candidate. Routing: dramatist re-rating. (URI-005.)

- [ap-002] [narrator:7 @23 + narrator:22 @24] AP7 persistent-narration — candidate violation. NI:7 = "the stool brings the eye-line to the column she had already read" and NI:22 = "the ledger goes down on the bench at the angle she had already read for it." Both fire on consecutive content-bearing beats (@23, @24) using the "had already read" pre-calc construction on the same interior channel. Per rubric AP7: "same registration sustained across consecutive beats; reject all but the first." The shared interior channel (pre-calc surfacing at both beats) is the violation candidate. Routing: taylor-hebert-jaehaerys impersonator (NI author). (URI-005.)

- [ap-003] [narrator:23 @94] AP5/voice-fidelity — candidate violation. "the eyes hold steady longer than a girl waiting on a stroke would hold them" uses a comparative externalization construction that registers Taylor's own interior through how she appears to an imagined observer. Base-register interiority does not typically frame the narrator's own behavior through third-party observer comparison. The entry is not strictly prohibited but the comparative construction (observing self from outside) is mask-register-adjacent. Routing: taylor-hebert-jaehaerys impersonator (NI author). (URI-005.)

- [ap-004] [vibes:7 @15] AP8 prose-token — candidate violation. Token "eyes-running-the-assessment-while-hands-keep-working" contains an embedded finite clause ("hands keep working": subject + finite verb compound). Per rubric AP8 test: "a sequence of two independent compressed clauses joined by a hyphen is AP8 even if individually each clause is short." The token structure has "eyes-running-the-assessment" and "hands-keep-working" joined by "while." Whether parsed as a compound structure with embedded finite clause or two independent clauses determines the verdict; flagged for author review. Routing: showrunner (vibes author). (URI-005.)

- [ap-005] [mem:3 @69, mem:4 @119, mem:6 @103, mem:7 @113] AP14 target-reference free-text gloss — soft. Four of eight memory entries use parenthetical free-text glosses as target-reference rather than card slugs. Per rubric: "Free-text glosses are the soft path; the conservative move is a margit referral to author the missing monument card." Monument families (cape-reflex/trained-body, parent-as-cost-vector/dying-tutor, child-performance-grooves, control-as-evidence) do not have formal card slugs. Clears with URI-003 (margit referral for monument card authoring). Routing: taylor-hebert-jaehaerys impersonator (memory author) + margit. (URI-003.)

- [ap-006] [feel:10 @67] **AP6 comparison/simile violation — NEW finding introduced by feeling tuning.** The Phase E revision of feel:10 produced the entry: "the voice steps down a margin the way an estimate gets one." The phrase "the way an estimate gets one" is a comparison construction. The rubric §Form discipline hard-bans comparisons: "Hard ban: any 'X like Y' / 'X as Y' / 'X as if Y' construction. The body action is what it is, not what it resembles." "The way" functions as a comparison operator equivalent to "as": "the voice steps down a margin [the way] an estimate gets one" = "the voice steps down a margin [as] an estimate gets one." This is the comparison/simile form violation the rubric names under AP6 (anti-pattern 14 in the rubric catalog: "Simile / comparison. 'Like X' / 'as if X' / 'as Y' structures used to render feeling-show. Hard refuse"). The Phase F final adjudication issued a REJECT verdict on this basis (3/3 persona votes: dark-fantasy-reader REJECT, pulp-enthusiast REJECT, worm-canon-pedant REJECT). This AP-SCAN finding was generated independently from the tuning-final; the REJECT and the AP-SCAN agree. The second clause ("the eyes mark the loft once and come back to her") is clean per the tuning final. Routing: oc-craftsman-father impersonator (URI-008); brief: revise first clause of feel:10 to preserve dyer-with-accounts register without comparison operator; second clause retained unchanged.

---

## TASTE-FLAG findings (5)

Findings taste-001 through taste-004 carried from audit-r3. One new finding introduced by feeling tuning.

- [taste-001] [mem:4 @119] voice-fidelity — "the warm hand on the shoulder is the parent already paying the bill the daughter has not handed over." Phase 4 tuning final named this ACCEPT-WITH-CAVEAT: "the daughter has not handed over" is passive-recipient framing marginally inconsistent with Taylor's active cost-tracking register. The audience accepted the defense but named the residual honestly. Signal-only; tuning final flagged for editor review at wrap. Unchanged from r3.

- [taste-002] [mem:8 @131] atmosphere-thin — "the day closes in the shape of a thing already filed; the filing was the whole day." Administrative-permanence closure at the episode's final beat. Well-formed and Phase 4-accepted, but reads somewhat abstract at episode-close. The "the day closes" / "closes the day" surface echo with NI:25 compounds this. The ACCEPT-WITH-CAVEAT verdict from Phase 4 named the residual. Signal-only. Unchanged from r3.

- [taste-003] [narrator:23 @94] voice-fidelity — "the eyes hold steady longer than a girl waiting on a stroke would hold them." The comparative construction frames Taylor's own somatic behavior through an imagined third-party observer perspective ("a girl waiting on a stroke"). Base-register does not typically externalize itself; interiority is cost-tracking and pre-calc, not self-observation-through-imagined-witness. "A girl waiting on a stroke" also carries a passivity framing ("waiting") inconsistent with Taylor's active anticipatory register. Same entry flagged in ap-003. Signal-only. Unchanged from r3.

- [taste-004] [narrator:7 @23 + narrator:22 @24] momentum-stall — consecutive "had already read" pre-calc constructions at @23 and @24. NI:7: "the stool brings the eye-line to the column she had already read." NI:22: "the ledger goes down on the bench at the angle she had already read for it." Consecutive identical-register fires at adjacent beats produce a momentum stall in stitched output because both beats surface the same interior channel (pre-calc) without distinct functional contribution. Signal-only. Unchanged from r3.

- [taste-005] [feel:10 @67] **voice-fidelity / atmosphere-thin — NEW finding introduced by feeling tuning.** Independent of the AP-SCAN AP6 mechanical finding: the comparison construction "the way an estimate gets one" also fails at the taste level. The somatic-tell facet requires body actions named in their own register; "steps down a margin the way an estimate gets one" does not describe a body action — it describes a voice-action using a comparison to an accounting procedure. The somatic-action register is absent from the first clause entirely: "voice steps down a margin" is observable vocal behavior, but "the way an estimate gets one" shifts the register from body-in-its-own-vocabulary to voice-as-compared-to-accounting-object. The intent (inscribe dyer-with-accounts register) is correct but the execution substitutes comparison for somatic vocabulary. The second clause ("the eyes mark the loft once and come back to her") is clean, anchored in body-register (gaze-direction), and survives on its own. The first clause is the isolated failure. At the atmosphere level, the register mismatch weakens the entry at the episode's Scene 4 sole feeling-fire. Signal-only.

---

## PILE-UP REVIEW (7 candidates, all warranted)

Post-feeling-tuning pile-up count (>4 co-located facets): unchanged from r3. Feeling tuning preserved all existing anchors; no new pile-ups introduced; no pile-ups resolved.

- **@99** (15 facets) — verdict: **warranted.** Structural climax (tens=3); five simultaneous canonical field-mutations, seven vibes on distinct targets with distinct licensed-by chains, NI + feeling + tensometer close the set. Density structurally mandated by the irreversibility and fan-out scope of the mark-setting act. No change from r3.

- **@35** (9 facets) — verdict: **warranted.** Market-slip draws the documentary mechanism to the surface for the first time; nine entries across nine distinct jobs. No change from r3.

- **@119** (7 facets) — verdict: **warranted.** Intimate-cost beat fanned across two actors; all sources resolve at or before @119. No residual defect. No change from r3.

- **@69** (5 facets) — verdict: **warranted.** NI:14, mem:3, vibes:4, vibes:13, and tens:52 all independently licensed for this beat. Metaphor deletion (@69) confirmed absent. No change from r3.

- **@130** (6 facets) — verdict: **warranted.** Two real state-mutations + sensory inflection + loc-state frame turnover + NI + vibes:17. No change from r3.

- **@8** (5 facets) — verdict: **warranted.** Real env state-change + loc-state morning-frame + sensory inflection + NI + vibes:16. No change from r3.

- **@83** (5 facets) — verdict: **warranted.** tens=3 peak; NI + two state-updates on distinct targets + feeling:6. Lean for a 3-beat; no over-decoration. No change from r3.

---

## Audit summary

- Total entries reviewed: 202 facet entries across 9 facet files (102 tensometer + 8 loc-state + 24 NI + 5 sensory + 22 state-updates + 8 memory + 12 feeling + 0 metaphor + 21 vibes; consistent with cite-index totals)
- STRUCTURAL: 0 (audit-r3 struct-001 downgraded to per-section-convention-acceptable per URI-004)
- FREQUENCY-BAND: 2 signal findings (tensometer rung-3 breach-low at 2.0% vs 5-10% band; tensometer rung-1 breach-high at 77.5% vs 60-75% band) — unchanged from r3
- METADATA-INCONSISTENCY: 2 (meta-001 carried from r3: memory.md stale quiet-beat aggregate claim; meta-002 new: feeling.md father-section r2_to_r3 forbidden-vocabulary claim contradicted by actual feel:10 content)
- CURVE-SHAPE: **SHAPE-FAIL** — 6 of 8 scenes lack rung-3 peak with no dramatist-flagged exception; 1→3 direct jump at @83 — unchanged from r3
- CONTRADICTION: 0 (none detected; all state chains monotonic) — unchanged from r3
- DEDUP: 0 active — unchanged from r3
- SUPERFLUOUS: 0 (all 7 lonely entries survive rubric scrutiny) — unchanged from r3
- CONSTRAINT: 3 soft flags (flag-003 carried; flag-004 downgraded; flag-005 superseded by meta-001) — unchanged from r3
- AP-SCAN: 6 (ap-001 through ap-005 carried from r3; ap-006 NEW: feel:10 AP6 comparison/simile violation introduced by Phase E revision)
- TASTE-FLAG: 5 (taste-001 through taste-004 carried from r3; taste-005 NEW: feel:10 voice-fidelity/atmosphere-thin introduced by Phase E revision)
- PILE-UP REVIEW: 7 warranted / 0 over-decoration — unchanged from r3

---

## Cross-character cleanliness verification (mechanical scan result)

Mechanical scan of all 12 feeling entries against three Phase E claims:

**Breath-as-duration zero:**
- feel:1: "the breath leaves before the foot lands" — breath-as-deploy-trigger per card §Non-verbal tics ("The breath out before the swarm goes"). Card-licensed action, not a duration-measurement unit.
- Entries 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14: zero breath tokens.
- Verdict: **CONFIRMED ZERO for breath-as-duration usage.** feel:1's breath is card-licensed action-trigger, not duration-marker. Phase E claim verified.

**Temporal-anchor formula ("before the X comes/lands/falls") zero:**
- feel:1: "before the foot lands" — card-text licensed (ONE occurrence, retained by defense).
- feel:13: "before the throat asks" — retained as internal-anticipation semantic slot (body running ahead of internal need), not cross-character external-event formula. Semantically distinct per tuning final.
- All other 10 entries: zero "before the X" constructions.
- Verdict: **CONFIRMED ZERO for the cross-character external-event formula.** Residual: feel:13's "before the throat asks" in internal-anticipation slot is semantically distinct; surface form echo with feel:1 noted in tuning final as ACCEPT-WITH-CAVEAT. Phase E claim verified with named residual.

**Negative-continuity broken:**
- feel:5 revised: "the spoon turns the corner of the pot and scrapes the rim once on the way around" — positive craft-action. CLEAN.
- feel:6 revised: "the fingers gather the strand against the next strand and lay them flat; the thumb tips the tie under and turns it tight at the nape" — all positive. CLEAN.
- feel:7 revised: "the heel of the hand sets where the small bone runs at the top of the shoulder; the fingers find the seam of the smock and rest along it" — positive. CLEAN.
- feel:14 revised: "the spoon stops a finger clear of the mordant rim and the blue at her knuckle stands out against the iron of the pot" — positive (with tuning-final noted form-discipline caveat on "stands out").
- Verdict: **CONFIRMED BROKEN.** Mother's set contains zero negative-continuity tells post-revision. Taylor's feel:4 ("does not lift to meet it") and father's feel:11 ("does not lift at once") are both card-licensed in distinct semantic slots (refusal-of-casual-touch and artisan-finality respectively) — neither is the registration-by-non-disruption pattern. Phase E claim verified.

---

## Routing

**ap-006 + taste-005** (feel:10 comparison violation): oc-craftsman-father impersonator (URI-008) — targeted brief: revise first clause of feel:10 to remove comparison operator while preserving dyer-with-accounts register and body-as-subject discipline; second clause "the eyes mark the loft once and come back to her" retained unchanged. Rubric §Form discipline check (blind re-test per URI-007 process-protocol item 9) before round close.

**meta-002** (feeling.md father-section r2_to_r3 round-note): oc-craftsman-father impersonator — at same dispatch as feel:10 revision, update the r2_to_r3 forbidden-vocabulary claim in the father section to reflect that Phase E introduced a comparison violation into feel:10 and that Phase F adjudicated REJECT.

**meta-001** (memory.md r2_to_r3 stale claim): taylor-hebert-jaehaerys impersonator (memory author) — correct the r2_to_r3 quiet-beat claim at next file-touch to reflect the Phase 4 episode-arc release-zone argument for mem:8. Minimal edit. Unchanged from r3 routing.

**freq-001, freq-002** (tensometer rung distribution): dramatist — root cause is URI-002 protoline scene-peak coverage gap. Routing is to and-wrap curve-shape review; distribution shifts if curve is corrected. Unchanged from r3 routing.

**flag-003** (mem:2 approach-zone): taylor-hebert-jaehaerys impersonator (memory author) at and-wrap — rubric carry-back #1 (URI-001) is the structural resolution path. Unchanged from r3 routing.

**ap-001 through ap-005** (AP candidates carried from r3): unchanged routing — tens AP5 → dramatist; NI AP7/voice → taylor-hebert-jaehaerys impersonator; vibes AP8 → showrunner; memory AP14 → taylor-hebert-jaehaerys impersonator + margit. (URI-005, URI-003.)

**taste-001 through taste-004** (TASTE-FLAG carried from r3): tuning input for next audience-tuning pass. No immediate author action required at flag-only mode. Unchanged from r3 routing.

**taste-005** (feel:10 atmosphere-thin/voice-fidelity): co-routed with ap-006 to oc-craftsman-father impersonator (URI-008). No additional action required beyond the URI-008 revision dispatch.

**CURVE-SHAPE SHAPE-FAIL**: dramatist — as flagged in the tensometer file's own header comment (URI-002). Screen-writer kickback is the rubric's prescribed path for scenes without beats that support rung-3 peaks; alternatively, dramatist argues scene-as-respite / scene-as-transit exceptions for Scenes 1, 2, 3, 4, 7, 8 in the tensometer file.

---

## Mode note

This audit ran in flag-only mode per Step G design. No deletes executed. All findings are advisory.

The 0 hard findings in r4 represent the strongest structural state the graph has reached across four passes. The audit-r3 HARD finding (struct-001, feeling.md ID non-monotonicity) is downgraded to per-section-convention-acceptable per URI-004, which requires a small command-file edit to `and-facets-audit.md` to codify the per-section convention for sub-sectioned facets.

**AP-SCAN performance on feel:10:** AP-SCAN caught the feel:10 comparison violation independently via AP6 (anti-pattern 14 in the rubric catalog: "Simile / comparison — hard refuse"). The finding matches the Phase F REJECT verdict. The detection path is: rubric §Form discipline hard-ban on comparison constructions → "the way an estimate gets one" parses as comparison operator → AP6 violation. TASTE-FLAG independently flagged the same entry under voice-fidelity/atmosphere-thin (the register mismatch, independent of the mechanical form violation). Both detection paths converge on the same entry.

The feeling tuning is confirmed as a near-clean pass (11/12 ACCEPT or ACCEPT-WITH-CAVEAT per Phase F) with one remaining entry (feel:10) requiring a second revision. That single revision is the only blocking action in the feeling facet before ship. The three cross-character cleanliness claims (breath-as-duration zero, temporal-anchor formula zero, negative-continuity broken) are mechanically verified by this audit.

The FREQUENCY-BAND breach (freq-001: rung-3 at 2.0%) and CURVE-SHAPE SHAPE-FAIL remain the primary and-wrap attention items. Both trace to URI-002 (upstream protoline scene-peak coverage gap). The distribution is stable and the root cause is pre-facet.

URI-007 (feeling rubric V2.1 carry-back: 9 audience-confirmed rubric gaps) is queued. Once URI-007 lands, AP-SCAN will be able to catch the following patterns mechanically: cross-character same-strategy saturation, within-character formula-repetition, lonely-entry Q2-stand-alone failure, body-as-subject discipline, and card-licensed-vs-saturation semantic-slot distinction. The current audit catches them only via TASTE-FLAG; graduation to AP-SCAN is pending rubric edit.
