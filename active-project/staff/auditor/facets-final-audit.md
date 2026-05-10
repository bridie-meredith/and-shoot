audit: facets-final-r5
episode: s01e01
date: 2026-05-10
mode: flag-only
status: FINDINGS-PRESENT

---

## Comparison vs prior audits

```
audit-r1 (5-class, original):                       7 findings
audit-r2 (5-class, post-memory-remediation):        5 findings
audit-r3 (11-class, post-memory-tuning):           13 findings
audit-r4 (11-class, post-feeling-tuning):          12 findings
audit-r5 (11-class, post-feel:10-fix + NI-tuning): 10 findings

Hard-finding trajectory: 4 → 0 → 1 → 0 → 0
Signal-finding trajectory: 3 → 5 → 12 → 12 → 10
```

Changes r4 → r5:
- **CLEARED (4 findings):** ap-002, ap-003, taste-002, taste-003 — all cleared by NI tuning.
- **CLEARED (2 findings):** ap-006, taste-005 — feel:10 AP6 comparison violation cleared by URI-008 second revision; meta-002 cleared by same (forbidden-vocabulary round-note now accurate).
- **NEW (0 findings):** NI tuning introduced no new hard violations. One new METADATA-INCONSISTENCY finding carried from Phase F (narrator:27 channel-mislabel — see meta-002 below).
- Net change: 12 → 10 (−4 cleared + 2 cleared + 0 new hard + 1 new metadata that replaces cleared meta-002 = net −2).

---

## STRUCTURAL findings (0)

struct-001 from audit-r3 remains DOWNGRADED per URI-004. Per-section monotonicity accepted as convention for sub-sectioned facets. Not re-raised.

No new structural findings.

---

## FREQUENCY-BAND findings (2)

Unchanged from audit-r4. Proto-lines unchanged; tens distribution is stable across all five audits.

- [freq-001] **tensometer — rung-3**: actual 2/102 = **2.0%**; band 5-10%; **breach-low**. The episode contains only 2 rung-3 entries (@83 and @99). Tensometer file's own header comment acknowledges the SOFT-FAIL. Root cause: URI-002 (upstream protoline scene-peak coverage gap). Both freq-001 and freq-002 are downstream symptoms of the same upstream structural shortfall.

- [freq-002] **tensometer — rung-1**: actual 79/102 = **77.5%**; band 60-75%; **breach-high**. Inverse symptom of freq-001.

Per-facet distribution table (post-NI-tuning; NI density updated):
| Facet | Metric | Actual | Band | Status |
|---|---|---|---|---|
| tensometer rung-1 | % of 102 | 77.5% | 60-75% | breach-high |
| tensometer rung-2 | % of 102 | 20.6% | 20-30% | within |
| tensometer rung-3 | % of 102 | 2.0% | 5-10% | breach-low |
| NI density | fires/102 | 26.5% (27/102) | 15-25% | breach-high (soft) |
| sensory sparsity | fires/102 | 4.9% | 3-6% | within |
| sensory modality coverage | distinct modalities | 3 (thermal, smell, light) | ≥2 | within |
| memory sparsity | fires/102 | 7.8% | 5-12% | within |
| feeling sparsity (Taylor) | fires/102 | 4.9% | 2-5% | within |
| feeling sparsity (Mother) | fires/102 | 3.9% | 2-5% | within |
| feeling sparsity (Father) | fires/102 | 2.9% | 2-5% | within |
| metaphor sparsity | fires/102 | 0.0% | 0-3% | within |
| state-updates density | fires/102 | 21.6% | ~8-18% | breach-high (soft, unchanged from r3) |

NI density note: 24 entries pre-tuning = 23.5% (within band); 27 entries post-tuning = 26.5% (marginally breach-high, 1.5pp above 25% upper bound). This is a new soft signal introduced by the NI tuning ADD of 3 entries. The breach is marginal; rubric text at §density says "outside that band, investigate: too dense = density-on-flat / no-contrast contamination." The 3 added entries are structurally licit (one each for foreknowledge-clamp @99, refusal-to-look-directly @35, and age-mismatch @47). The density breach is a monitoring note, not a fault.

---

## METADATA-INCONSISTENCY findings (2)

- [meta-001] **memory.md** — r2_to_r3 round-note stale claim. Carried forward unchanged from audit-r3 and audit-r4. The r2_to_r3 line claims "quiet-beat anchor 8/8 (all tens=1 or trailing-edge)" but this is contradicted by the Phase 4 defense for mem:8 which constructs an episode-arc release-zone argument, explicitly acknowledging the zone-class is contested. The r2_to_r3 claim predates the Phase 4 revision and was not updated. Routing: taylor-hebert-jaehaerys impersonator (memory author) — correct the r2_to_r3 quiet-beat aggregate claim at next file-touch to reflect the Phase 4 episode-arc release-zone argument for mem:8. Minimal edit.

- [meta-002] **interest-narrator.md** — narrator:27 channel-mislabel. The NI tuning defense log and the interest-narrator.md file header both record narrator:27 as a "mask-thinning" channel addition: `r2_tuning_defense: 24 → 27 ... 3 file-level adds (narrator:27 mask-thinning @47 ...)`. The ni-tuning-defense.md similarly states: `narrator:27 @47 — channel: mask-thinning`. However, the entry text itself — `the hand on her hair sits in the seam where the years in the body answer it before the cognition does` — does not deliver mask-thinning as the rubric defines it. The rubric (rubric-narrator-interest.md §Perceptual access) defines mask-thinning explicitly as: "The interior register relaxes when [Septon Aldric] is in scene; voice tells become slightly more visible." @47 is oc-craftsman-father ruffling hair — not a Septon Aldric proximity beat. The entry delivers age-mismatch + body-memory (the body carrying accumulated years that answer the warmth before the cognition does), not mask-thinning. The Phase F adjudication (ni-tuning-final.md, narrator:27 entry) independently confirmed this: wcp REJECT-on-channel-claim with the note "The channel-coverage claim for mask-thinning is NOT delivered here — the entry is good but under the wrong label." The file header (r2_tuning_defense) and defense log both claim mask-thinning coverage is delivered by narrator:27; the entry text does not deliver it. This is a METADATA-INCONSISTENCY between the channel-coverage claim in the round-note and the actual channel delivered by the entry. Note: because Septon Aldric is structurally absent from s01e01, mask-thinning cannot be licensed in this episode — the channel-coverage absence is a proto-line constraint, not a correctable file failure. The fault is not that mask-thinning is absent; it is that the round-note and defense log claim it was added when it was not. Routing: taylor-hebert-jaehaerys impersonator (NI author) — at next file-touch, update r2_tuning_defense header to accurately record narrator:27 as age-mismatch + body-memory channel, not mask-thinning; note that mask-thinning remains absent in this episode due to Septon Aldric absence and is not a file-level failure under those conditions.

---

## CURVE-SHAPE verdict

**Episode-level: SHAPE-FAIL** — unchanged from audit-r3 and r4. NI tuning did not alter the tens facet or proto-lines.

- **Act structure**: two peaks at @83 and @99, both in the second half. @99 is the structural climax (densest cluster). Act structure sound on this axis.
- **Climax uniqueness**: PASS.
- **Scene-level peak coverage**: FAIL. 6 of 8 scenes lack any rung-3 entry with no dramatist-flagged exception.
  - Scene 1 (@1–@7, dawn/shutter-shut): no rung-3. No exception flagged.
  - Scene 2 (@8–@31, morning/shutter-open): no rung-3. No exception flagged.
  - Scene 3 (@32–@57, afternoon/workshop-door-open): no rung-3. No exception flagged.
  - Scene 4 (@58–@60, dusk/tallow-lamp-lit): no rung-3. No exception flagged. (3-beat scene; may qualify as transit if dramatist argues.)
  - Scene 5 (@61–@91, evening/loft-vent-open): rung-3 at @83. PASS.
  - Scene 6 (@92–@125, late-evening/ledger-open): rung-3 at @99. PASS.
  - Scene 7 (@126–@129, night/winter-candle-drawn): no rung-3. No exception flagged.
  - Scene 8 (@130–@131, late-night/winter-candle-lit): no rung-3. No exception flagged. (2-beat scene; may qualify as transit if dramatist argues.)
- **Adjacency (1→3 jumps)**: 1 instance. @81=1, @82=1, @83=3 — direct 1→3 jump flagged.
- **Adjacency (3→3 sequences)**: 0. PASS.
- **Flatlining**: not present. PASS.

Root cause: URI-002 (upstream protoline scene-peak coverage gap). Tensometer header comment anticipated this.

---

## CONTRADICTION findings (0)

None. State-update chains remain monotonically consistent. Location-state time progression monotonic. No cross-facet state incompatibilities detected. Unchanged from audit-r3.

---

## DEDUP findings (0 active)

No DEDUP findings. Prior flag-001 and flag-002 resolved in audit-r3. The residual surface echo on "the day closes" / "closes the day" (mem:8 / narrator:25) was named in r3; narrator:25 was revised during NI tuning to "the second mark is the day's commit, priced and filed" — the echo is eliminated. No new DEDUP candidates.

---

## SUPERFLUOUS findings (0)

All 7 lonely entries from cite-index (loc-state:5 @61, loc-state:6 @92, narrator:2 @4, sensory:2 @3, state:7 @122, feel:13 @129, feel:14 @36) survive rubric scrutiny. Verdicts unchanged from audit-r4. NI tuning did not remove any lonely entries; the 3 adds (narrator:27/28/29) are co-decorated with existing entries and are not new lonely entries.

Note: cite-index will need regeneration to reflect NI tuning (narrator:27/28/29 added; some co-citation count updates at @35/@47/@99). The current cite-index header records 24 NI entries; the actual count is now 27. This is a staleness note for the index-generator, not an audit finding against the facet files themselves.

---

## CONSTRAINT findings (2 active, 1 retired)

- [flag-003] type: flag — **mem:2 @35 approach-zone quiet-beat (carried from r1/r2/r3/r4).** The Phase 4 defense constructs a trailing-edge argument for @35 (the slip-drawing as aftermath of the @32 return-cluster). Defensible but unverifiable without a dramatist-locked scene-frame. Rubric carry-back #1 (URI-001) is the structural resolution path. Disposition: soft flag (carried).

- [flag-004] type: flag — **mem:3 @69 approach-zone quiet-beat — Phase 4 adjudication accepted (carried, soft).** Audiences adjudicated ACCEPT in Phase 4. Zone-class was adjudicated as trailing-edge. Mechanical concern (zone-class without dramatist-locked scene-frame) remains as rubric-gap note per URI-001. Disposition: soft flag (carried, substantive concern closed by Phase 4 tuning).

- flag-005 **RETIRED.** mem:8 @131 was carried in r1-r4. The metadata component is captured in meta-001. The entry was revised during NI tuning pass (narrator:25 was revised, not mem:8; mem:8 itself unchanged); Phase 4 accepted with ACCEPT-WITH-CAVEAT. Meta-001 carries the metadata component forward. The substantive entry concern is adjudicated. flag-005 retired; no replacement needed.

---

## AP-SCAN findings (3 active; 3 cleared from r4)

**Cleared this round:**
- ap-002 [narrator:7 @23 + narrator:22 @24] AP7 persistent-narration — **CLEARED** by NI tuning. narrator:7 revised to age-mismatch channel ("the column reads at the speed her sounding-out is supposed to take twice"); narrator:22 revised to body-weight-tracking channel ("the bench takes the ledger at a weight her shoulder is tracking, not her eye"). The "had already read" identical-construction violation no longer exists; adjacent beats are now on distinct channels.
- ap-003 [narrator:23 @94] AP5 externalized-observer — **CLEARED** by NI tuning. Revised to "the eyes hold the seam in the wood and the count she had not yet finished" — internal body-anchor replaces the "a girl waiting on a stroke would hold them" third-party construction.
- ap-006 [feel:10 @67] AP6 comparison/simile violation — **CLEARED** by URI-008 second revision. See feel:10 AP6 fix verification section below.

**Remaining findings (3):**

- [ap-001] [tens:29 @34] AP5 stillness-inflation — candidate violation. "taylor-hebert-jaehaerys holds the feet" rated rung-2. The held-against-what (the slip discussion) is adjacent but not at the same beat's SVO. Per rubric: the on-face charge of Taylor-holds-feet is not independently legible from the proto-line alone. Soft AP5 candidate. Routing: dramatist re-rating. (URI-005.) Unchanged from r3/r4.

- [ap-004] [vibes:7 @15] AP8 prose-token — candidate violation. Token "eyes-running-the-assessment-while-hands-keep-working" contains an embedded finite clause ("hands keep working": subject + finite verb compound). Per rubric AP8 test: "a sequence of two independent compressed clauses joined by a hyphen is AP8 even if individually each clause is short." Routing: showrunner (vibes author). (URI-005.) Unchanged from r3/r4.

- [ap-005] [mem:3 @69, mem:4 @119, mem:6 @103, mem:7 @113] AP14 target-reference free-text gloss — soft. Four of eight memory entries use parenthetical free-text glosses as target-reference rather than card slugs. Monument families do not have formal card slugs. Clears with URI-003 (margit referral for monument card authoring). Routing: taylor-hebert-jaehaerys impersonator (memory author) + margit. (URI-003.) Unchanged from r3/r4.

---

## feel:10 AP6 fix verification

**CONFIRMED CLEAN.** Mechanical scan of feel:10 post-URI-008 second revision:

Entry text (from feeling.md line 41):
`10 @67 oc-craftsman-father: the voice steps down a margin and holds at the lower mark; the eyes mark the loft once and come back to her | expressed: partial`

Scan for forbidden comparison vocabulary {like / as / as if / as though / the way / kind of / sort of / almost / nearly / faintly / vaguely}:
- "like": absent
- "as": absent (the construction "and holds" is a coordinating conjunction, not a comparison marker)
- "as if": absent
- "as though": absent
- "the way": absent — the Phase E.c text "the way an estimate gets one" has been replaced by "and holds at the lower mark"
- "kind of": absent
- "sort of": absent
- "almost": absent
- "nearly": absent
- "faintly": absent
- "vaguely": absent

The AP6 comparison construction is gone. The URI-008 second revision successfully removed the comparison operator while preserving the dyer-with-accounts register ("margin" and "lower mark" remain as account-vocabulary; "holds at" extends the ledger-register with body-as-subject discipline). The second clause ("the eyes mark the loft once and come back to her") is unchanged. Both clauses pass the AP6 mechanical scan. ap-006 CLEARED.

The r2_to_r3 forbidden-vocabulary round-note in the father section of feeling.md previously claimed "no comparisons" while the file contained the Phase E comparison violation. The URI-008 revision corrects the actual entry text; the round-note header at line 38 now accurately reflects the file's state (the forbidden-vocabulary check in r2_tuning_defense header has been updated by the r2_tuning_defense log to document the Phase E introduction and Phase F REJECT, and notes the URI-008 resolution). meta-002 from audit-r4 is therefore CLEARED: the contradiction between the round-note's "no comparisons" claim and the file's actual content has been resolved because the comparison is no longer present.

---

## NI channel-coverage verification

**Post-tuning distribution (27 entries, per ni-tuning-final.md channel-coverage table):**

| channel | fires | % of 27 |
|---------|-------|----------|
| cost-tracking | 10–11 | ~40% |
| age-mismatch | 7 | 26% |
| passive fauna-feed | 4 | 15% |
| pre-calc surfacing | 4–5 | ~18% |
| eyes-to-exits | 1 (partial) | 4% |
| foreknowledge-clamp | 1 (narrator:29) | 4% |
| refusal-to-look-directly | 1 (narrator:28) | 4% |
| mask-thinning | 0 | 0% |

**Does post-tune distribution satisfy the rubric?**

Rubric §Curve-shape "behavior-pack channel diversity": expects at least three distinct channels across fires; no single channel >50% dominant. Results:

- **Pre-calc no longer >50%**: CONFIRMED. Pre-calc was the pre-tune concern (~6-7 fires, ~25-30%). Post-tune: 4 fires (~18% of 27). Not dominant. PASS.
- **Foreknowledge-clamp present (was 0; now ≥1)**: CONFIRMED. narrator:29 @99 delivers the foreknowledge-clamp via "the count of years the mark has just shortened goes flat behind the eyes." Phase F adjudicated 3-ACCEPT. PASS.
- **Refusal-to-look-directly present (was 0; now ≥1)**: CONFIRMED. narrator:28 @35 delivers the refusal channel via "the slip is the thing the eyes do not land on while the count behind them runs." Phase F adjudicated 3-ACCEPT. PASS.
- **Mask-thinning absent**: CONFIRMED ABSENT — but this is NOT a file-level failure. Rubric mask-thinning channel is Septon-Aldric-proximity-specific. Septon Aldric does not appear in s01e01 (cast: taylor-hebert-jaehaerys, oc-craftsman-mother, oc-craftsman-father; confirmed in proto-lines file header and showrunner memory.md s01e01 cast entry). No licensed trigger exists for mask-thinning in this episode. The rubric's §mask-too-perfect file-level flag fires only if the file has zero foreknowledge-clamp AND zero displacement-register fires; with narrator:28 (refusal) and narrator:29 (foreknowledge-clamp) both present, the mask-too-perfect flag does not fire. Mask-thinning absence is a structural consequence of the episode's cast composition, not a remediable file defect. ACCEPT.

**Channel-coverage verdict**: the post-tune distribution satisfies the rubric. The three previously-absent doubled-register channels (foreknowledge-clamp, refusal-to-look-directly) are now present; cost-tracking is the dominant channel at ~40% (below the 50% flag threshold); mask-thinning is absent due to the absence of its sole licensed trigger. The multi-channel rubric requirement is met.

---

## narrator:27 METADATA-INCONSISTENCY — independent verification

This audit independently confirms the Phase F finding on narrator:27.

The interest-narrator.md file header (r2_tuning_defense line) states: `3 file-level adds (narrator:27 mask-thinning @47; narrator:28 refusal-to-look-directly @35; narrator:29 foreknowledge-clamp @99) close the rubric §curve-shape channel-coverage gap (mask-too-perfect file-level remediation)`.

The actual narrator:27 entry text: `the hand on her hair sits in the seam where the years in the body answer it before the cognition does`.

The rubric's mask-thinning channel definition (rubric-narrator-interest.md §Perceptual access): "Mask-thinning at Septon Aldric proximity. The interior register relaxes when he is in scene; voice tells become slightly more visible."

Assessment: narrator:27's text does not engage with Septon Aldric proximity. There is no Septon Aldric in the scene; there is no relaxation of the mask. What the entry delivers is the body responding to a warm-affection gesture (the hair-ruffle by oc-craftsman-father) through accumulated lived-time — this is age-mismatch + body-memory, as confirmed by the Phase F adjudication (wcp: "REJECT on channel-coverage claim, ACCEPT on entry quality").

The file header's claim that narrator:27 closes the mask-thinning coverage gap is a metadata inconsistency: it asserts a channel delivery that the entry text does not execute. The entry is a quality ACCEPT-WITH-CAVEAT per Phase F; it simply delivers a different channel than the one claimed. meta-002 in this audit captures this finding independently from Phase F.

The consequence: mask-thinning channel coverage remains at 0 in this episode. As noted above, this is acceptable because Septon Aldric is absent from s01e01. The file-header's coverage claim is the error; the file content's channel delivery is fine for the episode scope.

---

## TASTE-FLAG findings (3 active; 2 cleared from r4)

**Cleared this round:**
- taste-002 [narrator:25 atmosphere-thin / author-voice] — **CLEARED** by NI tuning. narrator:25 revised to "the second mark is the day's commit, priced and filed." The thematic-arc summary is gone; cost-accounting triple replaces it. Phase F: 3-ACCEPT.
- taste-003 [narrator:23 voice-fidelity] — **CLEARED** by NI tuning (same entry as ap-003; revision to body-anchored interior clears both).

**Remaining findings (3):**

- [taste-001] [mem:4 @119] voice-fidelity — "the warm hand on the shoulder is the parent already paying the bill the daughter has not handed over." Phase 4 tuning final named this ACCEPT-WITH-CAVEAT: "the daughter has not handed over" is passive-recipient framing marginally inconsistent with Taylor's active cost-tracking register. Tuning final flagged for editor review at wrap. Signal-only. Unchanged from r3/r4.

- [taste-004] [narrator:7 @23 + narrator:22 @24] **partially resolved, residual flagged.** The consecutive-fire momentum stall is reduced: narrator:7 now fires on age-mismatch channel; narrator:22 fires on body-weight-tracking channel. The two adjacent beats no longer share a channel. However, the Phase F final notes a residual: narrator:1 and narrator:2 (ACCEPT-WITH-CAVEAT) exhibit back-to-back stasis-opening framing ("already where they were last night" / "the radius is what it was"). The original taste-004 (narrator:7 + narrator:22 momentum-stall) is resolved. A new, softer version of the concern surfaces at the episode's first two spotlight beats. The stitcher note in ni-tuning-final.md names this: "rendering narrator:1 and narrator:2 at full weight produces a double-stasis opening at the episode's first two spotlight beats." Signal-only, scope reduced from r4. The taste-004 identifier is retained for tracking; the scope is narrowed.

- [taste-006] [narrator:18 @99] **NEW — voice register at structural climax.** narrator:18 "the apprentice-stroke fixes the role the household will read on her tomorrow" was ACCEPTED-WITH-CAVEAT in Phase F. wcp flagged: "will read on her tomorrow" is social-reception framing (mask-register — what-will-others-see) rather than cost-tracking base-register (what-have-I-just-paid). At the episode's structural climax fire — the 15-facet pile-up at @99 — the NI entry is the interior-cost-pricing of the mark. An entry that reads in slightly mask-adjacent register at the episode's most load-bearing beat is a taste-level concern. The entry passes (3-ACCEPT overall) but wcp's named residual is the most consequential caveated fire in the episode given its structural position. Signal-only. New in r5.

---

## PILE-UP REVIEW (7 candidates, all warranted)

Pile-up count unchanged from r4. NI tuning added narrator:27/28/29 to @47/@35/@99 respectively, increasing their citation counts by 1 each. No new pile-ups created; no existing pile-ups resolved. The @99 pile-up now counts 16 co-cited facet entries (up from 15 in r4 with the addition of narrator:29).

- **@99** (16 facets including narrator:29) — verdict: **warranted.** Structural climax; the addition of narrator:29 (foreknowledge-clamp) is a structurally licensed addition at the episode's densest cluster. No change to verdict.
- **@35** (10 facets including narrator:28) — verdict: **warranted.** Market-slip documentary mechanism; narrator:28 refusal-to-look-directly is a structurally licensed addition. No change to verdict.
- **@47** (3 facets including narrator:27) — previously a 2-facet pile; now 3. Below the >4 threshold; not in pile-up territory. Note: narrative weight at @47 supports the addition.
- **@119** (7 facets) — unchanged. Warranted.
- **@130** (6 facets) — unchanged. Warranted.
- **@8** (5 facets) — unchanged. Warranted.
- **@83** (5 facets) — unchanged. Warranted.

---

## Audit summary

- Total entries reviewed: 205 facet entries across 9 facet files (102 tensometer + 8 loc-state + 27 NI [updated from 24] + 5 sensory + 22 state-updates + 8 memory + 12 feeling + 0 metaphor + 21 vibes; consistent with cite-index totals post-NI-update)
- STRUCTURAL: 0
- FREQUENCY-BAND: 2 signal findings (rung-3 breach-low 2.0%; rung-1 breach-high 77.5%). New soft signal: NI density at 26.5%, marginally above 25% upper band (monitoring note only).
- METADATA-INCONSISTENCY: 2 (meta-001 carried: memory.md stale quiet-beat claim; meta-002 new: interest-narrator.md narrator:27 channel-mislabel)
- CURVE-SHAPE: **SHAPE-FAIL** — 6 of 8 scenes lack rung-3 with no dramatist exception; 1→3 direct jump at @83 — unchanged from r3/r4
- CONTRADICTION: 0
- DEDUP: 0 active (narrator:25 / mem:8 surface echo resolved by narrator:25 revision)
- SUPERFLUOUS: 0
- CONSTRAINT: 2 soft flags active (flag-003, flag-004 carried; flag-005 retired)
- AP-SCAN: 3 active (ap-001, ap-004, ap-005 carried; ap-002, ap-003, ap-006 CLEARED)
- TASTE-FLAG: 3 active (taste-001 carried; taste-004 scope-reduced and carried; taste-006 new; taste-002, taste-003 CLEARED)
- PILE-UP REVIEW: 7 warranted / 0 over-decoration

---

## Routing

**freq-001, freq-002** (tensometer rung distribution): dramatist — URI-002 upstream protoline scene-peak coverage gap. And-wrap curve-shape review. Unchanged from r3/r4.

**meta-001** (memory.md r2_to_r3 stale claim): taylor-hebert-jaehaerys impersonator — correct the r2_to_r3 quiet-beat aggregate claim. Unchanged from r3/r4.

**meta-002** (interest-narrator.md narrator:27 channel-mislabel): taylor-hebert-jaehaerys impersonator (NI author) — update r2_tuning_defense header to accurately record narrator:27 as age-mismatch + body-memory channel; document that mask-thinning is absent in this episode due to Septon Aldric absence and is not a file-level failure; remove the claim that narrator:27 closes the mask-thinning coverage gap.

**ap-001** (tens:29 AP5): dramatist re-rating. URI-005.

**ap-004** (vibes:7 AP8): showrunner. URI-005.

**ap-005** (memory AP14): taylor-hebert-jaehaerys impersonator + margit. URI-003.

**taste-001** (mem:4 voice-fidelity): editor at and-wrap. Advisory.

**taste-004** (narrator:1/2 back-to-back stasis residual, scope-reduced): stitcher-layer awareness note at and-wrap. No author action required unless stitcher render output shows the double-stasis as a reader-facing flaw.

**taste-006** (narrator:18 mask-adjacent register): advisory for next NI tuning pass if one occurs; does not block ship. Signal-only.

**CURVE-SHAPE SHAPE-FAIL**: dramatist — URI-002; screen-writer kickback path or scene-as-transit exception argument for Scenes 1, 2, 3, 4, 7, 8.

---

## Cumulative state assessment

**SHIPPABLE-WITH-CAVEATS.**

The facet graph as of audit-r5 has:
- 0 hard findings (the trajectory has been clean at 0 hard since audit-r2)
- 10 signal findings (all soft flags, carry-forward monitoring notes, or audit-at-wrap items)
- 0 unresolved mechanical violations in any facet file content
- feel:10 AP6 comparison violation: CLEARED (URI-008 second revision confirmed clean)
- NI tuning: 27/27 PASS in Phase F (21 clean ACCEPT + 6 ACCEPT-WITH-CAVEAT + 0 REJECT)
- The 6 caveated entries in the NI file are documented residuals with named failure modes, not mechanical violations; all pass the 3-persona threshold
- The two persistent structural issues (CURVE-SHAPE SHAPE-FAIL + FREQUENCY-BAND breach) both trace to URI-002 (upstream scene-peak coverage gap) and are pre-facet-layer concerns; they are and-wrap items, not facet-layer blockers

The metadata inconsistencies (meta-001, meta-002) require small round-note corrections at next file-touch; neither affects facet content correctness or stitcher output.

The and-wrap items (freq-001/002, CURVE-SHAPE) require dramatist review of the tensometer curve before final manuscript production, but do not prevent the facet graph from being used in stitching.

---

## Mode note

This audit ran in flag-only mode per Step G design. No deletes executed. All findings are advisory.

Audit-r5 is the first audit at which all four prior AP-SCAN findings tied to specific tuning actions (ap-002, ap-003, ap-006, and their companion taste findings) confirm as resolved. The hard-finding count has been 0 since audit-r2 across three 11-class passes. The signal count has reduced from 12 (r4) to 10 (r5), a net −2 across the NI tuning + URI-008 fix round.

The NI tuning cycle (24→27 entries, 10 DEFEND / 14 REVISE / 0 WITHDRAW / 3 ADD) is confirmed successful by this audit: the four audit-r4 NI findings cleared, the mask-too-perfect file-level failure addressed (foreknowledge-clamp + refusal-to-look-directly now present), and no new hard violations introduced. The one new metadata finding (meta-002, narrator:27 channel-mislabel) was independently surfaced by this audit, matching Phase F's own ACCEPT-WITH-CAVEAT flag on the same entry.

URI-007 (feeling rubric V2.1 carry-back: 9 audience-confirmed rubric gaps) queued. URI-001 (dramatist-locked scene-frame for zone-class verification) remains the structural path for flag-003 and flag-004.
