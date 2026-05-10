audit: facets-final-r3
episode: s01e01
date: 2026-05-10
mode: flag-only
status: FINDINGS-PRESENT
totals: 13 findings across 6 facets (1 hard, 12 signal/soft)

---

## Comparison vs prior audits

audit-r1 (original 5-class, pre-remediation): 7 findings
audit-r2 (original 5-class, post-remediation): 5 soft findings
audit-r3 (upgraded 11-class, post-tuning): 13 findings

Hard-finding trajectory: 4 (r1) -> 0 (r2) -> 1 (r3)
Signal-finding trajectory: 3 (r1) -> 5 (r2) -> 12 (r3)

Note: The r3 hard count is 1 (STRUCTURAL — feeling.md ID non-monotonicity). The 12 signal findings include the frequency-band breach the prior 5-class audit silently missed, plus 11 new signal findings from the 6 expanded classes. The r2 DEDUP flags (flag-001, flag-002) are resolved by the Phase 4 tuning revisions and are not carried forward as active findings.

---

## STRUCTURAL findings (1)

- [struct-001] **feeling.md** — id-non-monotonic — The feeling facet file presents IDs in the order 1, 2, 3, 4, 13, 5, 6, 7, 14, 9, 10, 11 across its three per-character sections. IDs are monotonically increasing within each character block (Taylor: 1,2,3,4,13; Mother: 5,6,7,14; Father: 9,10,11) but are NOT monotonically increasing across the file as a whole. Specifically: after feel:13, feel:5 appears; after feel:14, feel:9 appears. The schema requires IDs strictly increasing within each facet file; deletion gaps are permitted but not re-ordering. The per-character sectioning does not override the file-scope monotonicity requirement. Note: feel:8 and feel:12 are documented deletions; feel:8 was deleted in r2_judge (mother section); feel:12 was deleted in r2_judge (Taylor section). The deletions are correctly recorded in round-notes but the remaining IDs across the full file are not monotonically ordered.

---

## FREQUENCY-BAND findings (2)

- [freq-001] **tensometer — rung-3**: actual 2/102 = **2.0%**; band 5-10%; **breach-low**. The episode has only 2 entries at rung-3 (@83 and @99). The tensometer file's own header comment acknowledges this: "3-rung SOFT-FAIL — 2.0% < 5-10% target band." The prior 5-class audits did not formally capture this in the FREQUENCY-BAND class (the class did not exist). Confirmed: the 11-class audit catches this breach the original 5-class audit missed.

- [freq-002] **tensometer — rung-1**: actual 79/102 = **77.5%**; band 60-75%; **breach-high**. The 1-rung is elevated above the upper band boundary. This is the inverse symptom of the 3-rung breach-low: fewer peaks, more quiet beats. The prior 5-class audits did not formally flag this. Both freq-001 and freq-002 describe the same structural phenomenon from opposite sides: the episode's dramatic charge is concentrated at only 2 beats rather than distributing across 5-10% of content-bearing protolines.

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

Note on state-updates: the rubric's band of 8-18% was calibrated for 77-beat episodes; at 102 content-bearing beats the upper bound scales to ~19 entries. 22 entries at 21.6% is a soft breach. No fixed band is stated for state-updates; signal only.

---

## METADATA-INCONSISTENCY findings (1)

- [meta-001] **memory.md** — r2_to_r3 round-note claims "quiet-beat anchor 8/8 (all tens=1 or tens=2-trailing-edge)" but this claim is internally inconsistent with the Phase 4 (r2_tuning_defense) block's own defense for mem:8. The defense for mem:8 constructs an "episode-close release-zone trailing-edge of the @99-peaked arc" argument, explicitly acknowledging that mem:8's micro-beat zone-class is contested (the block following @130=tens:1 at @131=tens:2 reads as a rising 2-beat at micro-beat scale). The r2_to_r3 line predates the Phase 4 revision and was not updated. The r2_to_r3 claim therefore contradicts the file's own Phase 4 defense block. This is carried forward from audit-r2 flag-005 (which flagged the original r2 source of the claim); the Phase 4 tuning did not correct the stale r2_to_r3 metadata.

  Routing: taylor-hebert-jaehaerys impersonator (memory author) — correct the r2_to_r3 quiet-beat claim to reflect the episode-arc release-zone argument, or add a r3_to_r4 note that supersedes the r2_to_r3 aggregate claim.

---

## CURVE-SHAPE verdict

**Episode-level: SHAPE-FAIL**

- **Act structure**: two peaks at @83 and @99, both in the second half of the episode. @99 is the later and denser cluster (15 co-facets); structurally the climax is correctly placed. Episode does not invert (highest peak is not in the first third). Episode-level act structure is structurally sound on this axis.
- **Climax uniqueness**: 2 entries at rung-3 (@83 and @99). The densest cluster (@99, 15 co-facets) is unique. PASS.
- **Scene-level peak coverage**: FAIL. 6 of 8 scenes lack any rung-3 entry, with no dramatist-flagged exception present in the tensometer file.
  - Scene 1 (@1–@7, dawn/shutter-shut): no rung-3. No exception flagged.
  - Scene 2 (@8–@31, morning/shutter-open): no rung-3. No exception flagged.
  - Scene 3 (@32–@57, afternoon/workshop-door-open): no rung-3. No exception flagged.
  - Scene 4 (@58–@60, dusk/tallow-lamp-lit): no rung-3. No exception flagged. (3-beat scene; may qualify as transit if dramatist argues.)
  - Scene 5 (@61–@91, evening/loft-vent-open): rung-3 at @83. PASS.
  - Scene 6 (@92–@125, late-evening/ledger-open): rung-3 at @99. PASS.
  - Scene 7 (@126–@129, night/winter-candle-drawn): no rung-3. No exception flagged.
  - Scene 8 (@130–@131, late-night/winter-candle-lit): no rung-3. No exception flagged. (2-beat scene; may qualify as transit if dramatist argues.)
- **Adjacency (1→3 jumps)**: 1 instance. @81=r=1, @82=r=1, @83=r=3 — direct jump from rung-1 to rung-3 with no rung-2 immediately preceding. The broader approach includes @67=2, @69=2 (several beats earlier), but the immediate pre-peak beats are rung-1. Flagged for review — either misrating of @81/@82 or true sudden-turn.
- **Adjacency (3→3 sequences)**: 0. The two rung-3 entries are not consecutive. PASS.
- **Flatlining (30+ contiguous content-bearing beats with no rung-2 or rung-3)**: Not present. The longest rung-1 run is ~8 content-bearing beats. PASS.

The tensometer file's own header comment explicitly anticipated this: "Pending Round-2 verdict; flag for re-author if curve-shape audit is added at Step G." SHAPE-FAIL is consistent with the author's own flagged note.

---

## CONTRADICTION findings (0)

None. State-update chains are monotonically consistent (tallow-lamp: unlit→lit→guttering→dark; winter-candle: stored→drawn→lit; all other field-update chains single-entry or internally consistent). Location-state time progression is monotonic (dawn→morning→afternoon→dusk→evening→late-evening→night→late-night). No cross-facet state incompatibilities detected. Carried forward from r2: 0.

---

## DEDUP findings (0 active — 2 prior flags resolved)

**Prior flag-001 (mem:5 / narrator:26 @9): RESOLVED.** Post-Phase-4 revision of mem:5 to "the body inside the body keeps its older height in the joints" shares no surface vocabulary with narrator:26 "the feet plant at the spread the body had not yet sized to the floor." Different somatic sites, different vocabulary. DEDUP gate closed.

**Prior flag-002 (mem:8 / narrator:25 @131): RESOLVED (substantially).** Post-Phase-4 revision of mem:8 to "the day closes in the shape of a thing already filed; the filing was the whole day" vs narrator:25 "the second mark closes the day the first one opened." The final adjudication artifact confirms DEDUP substantially closed with a named residual surface echo ("the day closes" / "closes the day"). The residual is minor and non-disqualifying per the tuning final. Logged for stitcher-layer awareness (the tuning final's language); not re-raised as an active DEDUP finding.

No new DEDUP findings detected in r3 scan.

---

## SUPERFLUOUS findings (0)

All 7 lonely entries from cite-index (loc-state:5 @61, loc-state:6 @92, narrator:2 @4, sensory:2 @3, state:7 @122, feel:13 @129, feel:14 @36) survive rubric scrutiny:
- loc-state:5 and loc-state:6: scene-entry frame-anchors for Scenes 5 and 6 respectively; rubric-licensed as first-beat place-anchors for inherited environments.
- narrator:2 @4: approach-zone channel-coverage fire (passive fauna-feed baseline establishment).
- sensory:2 @3: smell modality inflection (bare verb "stirs"; mordant-stir-sharp is audience-perceptible disambiguation).
- state:7 @122: genuine state-change (tallow-lamp lit→guttering) that drives @126 winter-candle draw.
- feel:13 @129: Q1-clean (no NI on @129), Q2-structural (pre-closure body-set before second mark falls), multi-justification ≥3/5.
- feel:14 @36: non-POV mother somatic-tell; Q1-clean (proto-line carries no interior); Q2-structural (first-steward-name landing); multi-justification ≥3/5.

---

## CONSTRAINT findings (3 — all soft, status update)

Prior flags 003, 004, 005 from r2 are reviewed in light of Phase 4 tuning:

- [flag-003] type: flag — **mem:2 @35 approach-zone quiet-beat (carried from r1/r2).**
  - what: mem:2 fires at @35 (tens=2). The Phase 4 defense constructs mem:2 as a "tens=2 release-zone anchor — release after @32-34 entry-cluster, the slip is the artifact left after the action, not the action itself." This is a micro-beat trailing-edge argument for @35 (the slip-drawing as the aftermath of the @32 return-cluster). The argument is defensible but was not verified against a dramatist-locked scene-frame. The rubric's carry-back candidate #1 (from the Phase 4 tuning final) confirms this zone-class ambiguity is real: the rubric cannot resolve the trailing-edge vs. approach-zone classification without a dramatist-locked scene-frame.
  - why: Approach-zone 2-beats at memory require explicit backward-reach argument per rubric §quiet-beat test. The Phase 4 defense provides the argument; the rubric ambiguity means the argument cannot be mechanically verified without scene-frame authority.
  - disposition: soft flag (carried). Functional registers remain strong. Rubric carry-back #1 is the structural resolution path.

- [flag-004] type: flag — **mem:3 @69 approach-zone quiet-beat (carried from r1/r2; Phase 4 defense accepted).**
  - what: mem:3 fires at @35 (tens=2). Phase 4 defended: "cite-index back=Y confirms trailing-edge classification per the tensometer's own read; body-ahead-of-cognition temporal logic is the explicit backward-reach argument the rubric requires." The final adjudication accepted this defense (wcp ACCEPT, dfr ACCEPT, pe ACCEPT). The zone-class was adjudicated as trailing-edge.
  - why: The audience adjudicated this as ACCEPT in the Phase 4 tuning. The mechanical concern (zone-class without dramatist-locked scene-frame) remains as a rubric-level issue (carry-back #1), but this specific entry is post-tuning cleared.
  - disposition: **soft flag downgraded — Phase 4 tuning closed the substantive concern.** Carried only as a rubric-gap note per carry-back #1.

- [flag-005] type: flag — **mem:8 @131 rising-2 at episode close; metadata inconsistency (carried from r1/r2; superseded in part by meta-001).**
  - what: mem:8 fires at @131 (tens=2). Phase 4 revised the entry and constructed the "episode-close release-zone trailing-edge of the @99-peaked arc" argument. The final adjudication accepted this defense (wcp ACCEPT-WITH-CAVEAT, pe ACCEPT). However the r2_to_r3 metadata claim ("quiet-beat anchor 8/8 — all tens=1 or tens=2-trailing-edge") was not updated to reflect the Phase 4 zone-class argument, which is what meta-001 above now flags separately.
  - why: The residual metadata inconsistency is now captured in meta-001. The substantive entry concern was adjudicated ACCEPT-WITH-CAVEAT in Phase 4.
  - disposition: **soft flag superseded by meta-001 for the metadata component.** The entry itself is post-tuning cleared with caveats. Flag-005 is retired; meta-001 carries the metadata concern forward.

---

## AP-SCAN findings (5)

- [ap-001] [tens:29 @34] AP5 stillness-inflation — candidate violation. "taylor-hebert-jaehaerys holds the feet" rated rung-2. Stillness-inflation anti-pattern requires the held-against-what to be on-screen at the same beat. @34's on-screen context is a father-mother conversation about the market return. The "held-against" (the slip discussion) is adjacent but not at the same beat's SVO. The axis citation for this 2-rating is not explicit in the file; the charge must be inferred from scene context. Per rubric: "the answer is 'the scene is tense'" is a rung-1 call. The on-face charge of Taylor-holds-feet is not independently legible from the proto-line alone. Soft AP5 candidate.

- [ap-002] [narrator:7 @23 + narrator:22 @24] AP7 persistent-narration — candidate violation. NI:7 = "the stool brings the eye-line to the column she had already read" and NI:22 = "the ledger goes down on the bench at the angle she had already read for it." Both fire on consecutive content-bearing beats (@23, @24) and both use the "had already read" pre-calc construction registering the same perceptual channel (pre-calculation of positioning). Per rubric AP7: "same registration sustained across consecutive beats; reject all but the first; the rest must register change." NI:22 registers a distinct object (ledger vs. stool) but the interior channel is the same (pre-calc surfacing at both beats). Soft persistent-narration candidate on the shared "had already read" construction at consecutive beats.

- [ap-003] [narrator:23 @94] AP5/voice-fidelity — candidate violation. "the eyes hold steady longer than a girl waiting on a stroke would hold them" uses a comparative externalization construction ("a girl waiting on a stroke") that registers Taylor's own interior through how she appears to an imagined observer. This is a mild mask-register-adjacent construction — base-register interiority does not typically frame the narrator's own behavior through a third-party observer comparison. The rubric specifies "POV-restricted: speaker is always the POV character" and warns against "summary-of-the-beat" (paraphrasing the SVO). The entry is not strictly prohibited but the comparative construction (she is registering her own behavior as if from outside) is the kind of framing the base-register test may not pass.

- [ap-004] [vibes:7 @15] AP8 prose-token — candidate violation. Token "eyes-running-the-assessment-while-hands-keep-working" contains the subordinate clause structure "hands-keep-working" (subject "hands" + finite verb compound "keep-working"). Per the formal AP8 test: "A token is AP8 if it can be parsed as a complete sentence with a standalone subject, finite verb, and object." The token structure "eyes-running-the-assessment-while-[hands][keep-working]" has a coordinate clause "hands keep working" with subject + finite verb. The full token is a compound structure with a finite clause embedded via "while." Per the rubric's patch: "a sequence of two independent compressed clauses joined by a hyphen is AP8 even if individually each clause is short." Whether "eyes-running-the-assessment" and "hands-keep-working" are treated as two independent clauses joined by "while" determines the verdict; the auditor flags this as a candidate for author review.

- [ap-005] [mem:3 @69, mem:4 @119, mem:6 @103, mem:7 @113] AP14 target-reference free-text gloss — soft. Four of eight memory entries use parenthetical free-text glosses as target-reference rather than card slugs. Per the rubric: "Free-text glosses are the soft path; the conservative move is a margit referral to author the missing monument card." The rubric confirms these are not hard violations but are the soft path. The three monument families in question (cape-reflex/trained-body, parent-as-cost-vector/dying-tutor, child-performance-grooves, control-as-evidence) do not have formal card slugs in the cite-index or warehouse. Margit referral candidate for four monument families.

---

## TASTE-FLAG findings (4)

- [taste-001] [mem:4 @119] voice-fidelity — "the warm hand on the shoulder is the parent already paying the bill the daughter has not handed over." The Phase 4 tuning final named this as ACCEPT-WITH-CAVEAT: "the daughter has not handed over" is passive-recipient framing marginally inconsistent with Taylor's active cost-tracking register (she calculates costs; she does not frame herself as a cost-submitter). The audience accepted the defense but named the residual honestly. This is the exact pattern TASTE-FLAG anticipates: mechanically sound but carrying a register imprecision the audience would notice under adversarial re-examination. Signal-only; the tuning final itself flagged this for editor review at wrap.

- [taste-002] [mem:8 @131] atmosphere-thin — "the day closes in the shape of a thing already filed; the filing was the whole day." This is an administrative-permanence closure at the episode's final beat (tens=2, @131). The entry is well-formed and the Phase 4 tuning accepted it, but the construction reads somewhat abstract at the episode-close moment. The tuning final's named residual ("the day closes" echoes "closes the day" in NI:25) compounds this: two administrative-permanence figures at the same beat may read as tonally settled rather than weight-bearing at the close. The phrasing "the filing was the whole day" is the stronger clause; the opening "the day closes in the shape of a thing already filed" is where the abstraction accumulates. Signal-only.

- [taste-003] [narrator:23 @94] voice-fidelity — "the eyes hold steady longer than a girl waiting on a stroke would hold them." The comparative construction frames Taylor's own somatic behavior through an imagined third-party observer perspective ("a girl waiting on a stroke"). This is the same entry flagged in ap-003. At the taste level: the base-register does not typically externalize itself; the interiority is cost-tracking and pre-calc, not self-observation-through-imagined-witness. The phrase "a girl waiting on a stroke" also carries a passivity framing ("waiting") inconsistent with Taylor's active anticipatory register. Signal-only.

- [taste-004] [narrator:7 @23 + narrator:22 @24] momentum-stall — consecutive "had already read" pre-calc constructions at @23 and @24. NI:7: "the stool brings the eye-line to the column she had already read." NI:22: "the ledger goes down on the bench at the angle she had already read for it." The Phase 3 seam pattern (carry-back candidate #3: stage-named-cue generalizes to analytical-frame primary nouns) is adjacent to this — the "had already read" is a register that can accumulate quickly across consecutive beats. Consecutive identical-register fires read as momentum stall in the stitched output because both beats surface the same interior channel (pre-calc) without distinct functional contribution. Signal-only.

---

## PILE-UP REVIEW (7 candidates, all warranted)

Post-tuning pile-up count (>4 co-located facets): unchanged from r2.

- **@99** (15 facets) — verdict: **warranted.** Structural climax (tens=3): five simultaneous canonical field-mutations, seven vibes on distinct targets with distinct licensed-by chains, NI + feeling + tensometer close the set. Density is structurally mandated by the irreversibility and fan-out scope of the mark-setting act. No change from r2.

- **@35** (9 facets) — verdict: **warranted.** Market-slip draws the documentary mechanism to the surface for the first time; nine entries across nine distinct jobs. No change from r2.

- **@119** (7 facets) — verdict: **warranted.** Intimate-cost beat fanned across two actors; all sources resolve at or before @119. No residual defect. No change from r2.

- **@69** (5 facets) — verdict: **warranted.** NI:14, mem:3, vibes:4, vibes:13, and tens:52 all independently licensed for this beat. Metaphor deletion (@69) is confirmed absent. No change from r2.

- **@130** (6 facets) — verdict: **warranted.** Two real state-mutations + sensory inflection + loc-state frame turnover + NI + vibes:17. No change from r2.

- **@8** (5 facets) — verdict: **warranted.** Real env state-change + loc-state morning-frame + sensory inflection + NI + vibes:16. No change from r2.

- **@83** (5 facets) — verdict: **warranted.** tens=3 peak; NI + two state-updates on distinct targets + feeling:6. Lean for a 3-beat; no over-decoration. No change from r2.

---

## Audit summary

- Total entries reviewed: 202 facet entries across 9 facet files (102 tensometer + 8 loc-state + 24 NI + 5 sensory + 22 state-updates + 8 memory + 12 feeling + 0 metaphor + 21 vibes; consistent with cite-index totals)
- STRUCTURAL: 1 (HARD — feeling.md ID non-monotonicity across per-character section boundaries)
- FREQUENCY-BAND: 2 signal findings (tensometer rung-3 breach-low at 2.0% vs 5-10% band; tensometer rung-1 breach-high at 77.5% vs 60-75% band)
- METADATA-INCONSISTENCY: 1 (memory.md r2_to_r3 quiet-beat aggregate claim contradicts Phase 4 zone-class defense for mem:8)
- CURVE-SHAPE: **SHAPE-FAIL** — 6 of 8 scenes lack rung-3 peak with no dramatist-flagged exception; 1→3 direct jump at @83 (no immediate rung-2 precursor at @81/@82)
- CONTRADICTION: 0 (none detected; all state chains monotonic)
- DEDUP: 0 active (prior flag-001 and flag-002 resolved by Phase 4 tuning revisions)
- SUPERFLUOUS: 0 (all 7 lonely entries survive rubric scrutiny)
- CONSTRAINT: 3 soft flags (flag-003 carried; flag-004 downgraded per Phase 4 adjudication; flag-005 superseded by meta-001)
- AP-SCAN: 5 (AP5 stillness-inflation candidate on tens:29 @34; AP7 persistent-narration on NI @23/@24; AP5/voice-fidelity on NI @94; AP8 prose-token candidate on vibes:7; AP14 free-text gloss on mem:3/4/6/7)
- TASTE-FLAG: 4 (voice-fidelity on mem:4; atmosphere-thin on mem:8; voice-fidelity on NI:23; momentum-stall on NI:22/NI:7)
- PILE-UP REVIEW: 7 warranted / 0 over-decoration

## Routing

**struct-001** (feeling.md ID non-monotonicity): per-character impersonators (Taylor, mother, father forks) at and-wrap — IDs should be renumbered to be monotonically increasing across the full file, consistent with deletion-gap documentation. No content change required; renumbering only.

**freq-001, freq-002** (tensometer rung distribution): dramatist — the curve-shape failure is the structural source of both band breaches. Routing is to and-wrap curve-shape review; the distribution will shift if the curve is corrected.

**meta-001** (memory.md r2_to_r3 stale claim): taylor-hebert-jaehaerys impersonator (memory author) — correct the r2_to_r3 aggregate quiet-beat claim at next file-touch to reflect the Phase 4 episode-arc release-zone argument for mem:8. Minimal edit.

**CURVE-SHAPE SHAPE-FAIL**: dramatist — as flagged in the tensometer file's own header comment. Screen-writer kickback is the rubric's prescribed path for scenes without beats that support rung-3 peaks; alternatively, dramatist argues scene-as-respite / scene-as-transit exceptions for Scenes 1, 2, 3, 4, 7, 8 in the tensometer file.

**flag-003** (mem:2 approach-zone): taylor-hebert-jaehaerys impersonator (memory author) at and-wrap — unchanged from r2. Rubric carry-back #1 (scene-frame anchor requirement for tens=2 zone-class) is the structural path.

**flag-004** (mem:3 zone-class): taylor-hebert-jaehaerys impersonator — post-tuning adjudication accepted; routing is awareness only.

**ap-001 through ap-005** (AP candidates): routed to original facet authors (tens AP5 → dramatist; NI AP7/voice → taylor-hebert-jaehaerys impersonator; vibes AP8 → showrunner; memory AP14 → taylor-hebert-jaehaerys impersonator + margit for monument card authoring).

**taste-001 through taste-004** (TASTE-FLAG): tuning input for next audience-tuning pass. No immediate author action required at flag-only mode.

## Mode note

This audit ran in flag-only mode per Step G design. No deletes executed. All findings are advisory.

The 1 hard finding (struct-001, feeling.md ID non-monotonicity) is a format defect that does not affect rendered content or stitcher function but should be corrected before any next authoring round on the feeling facet.

The FREQUENCY-BAND breach (freq-001: rung-3 at 2.0%) is the primary signal for and-wrap attention. The tensometer author anticipated this finding. The CURVE-SHAPE SHAPE-FAIL is the structural expression of the same problem.

The Phase 4 tuning of the memory facet is confirmed as a net improvement: 2 prior DEDUP flags resolved; 8/8 entries adjudicated ACCEPT (6 clean, 2 with caveats); 3 prior soft constraint flags either resolved or downgraded. The post-tuning memory graph is in the strongest state it has been across the three audits. Residual concerns (mem:4 passive-recipient register; mem:8 surface echo with NI:25) are correctly logged in the tuning final and are not re-raised at the level of active faults.

The audit + tuning loop is bidirectional: Phase 4 seams surfaced patterns (zone-class ambiguity, mask-bleed vs clinical-of-the-horrible distinction, stage-named-cue generalization) that the rubric carry-backs name for codification. Once codified, ap-scan will catch these mechanically in future episodes. TASTE-FLAG entries taste-003 (NI:23 externalized-observer construction) and taste-004 (consecutive pre-calc register) are candidates for graduation to AP-SCAN once the pattern is rubric-codified.
