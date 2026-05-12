audit: facets-final-r4
episode: s01e03
date: 2026-05-12
mode: flag-only
status: CLEAN (0 HARD)

---

# Phase 5 Facets Audit — s01e03 — r4 (post-cycle-3-fixer)

## Preamble

Re-audit after cycle-3 fixer pass. Inputs: all facet files (post-cycle-3-fixer), cite-index rebuilt via --skip-merge. Fixer applied targeted remediation on five facets:

- **interest-narrator:** 6 entries rewritten (narrator:29, :37, :42, :43, :44, :45) addressing worm-canon passive-restatement and dark-fantasy apparatus-only callouts; augmentation entries now carry displacement / foreknowledge-clamp / age-mismatch registers.
- **tensometer:** tens:150 @160 upgraded 1→2 (approach-charge ramp restoration); tens:78 @83 + tens:79 @84 downrated 2→1 (market-trip transit). Footer updated with corrected 3s count (6/155 = 3.9%) and orchestrator decision on 3.9% band-floor (SIGNAL under Exemption 5).
- **location-state:** loc-state:4/15/20/21/22/24 trimmed to single perceptible focus element; loc-state:6a @43 added (apothecary smell baseline) to anchor sensory:9.
- **sensory:** sensory:9 @87 old-state now inherits from loc-state:6a @43 baseline.
- **vibes:** vibes:32 token rewritten (the AP8 sentence-form violation `the-log-now-calls-parallel-truths-coincidence` replaced with noun-phrase `parallel-truths-as-coincidence-in-log`).

Cite-index rebuilt via `--skip-merge`.

---

## Carry-forward from r3

| r3 id | r3 finding | r4 status |
|-------|-----------|-----------|
| flag-002 (STR-002) | NI ID gaps without in-file comments | CARRIED-FORWARD |
| flag-003 (STR-003) | tensometer dual-file identity | CARRIED-FORWARD |
| flag-006 (FB-002) | tens 2s at 30.3% above ceiling | UPDATED — see §Verification; 2s back within band at ~28.4% per cycle-3 footer; advisory substantially resolved |
| flag-007 (FB-003) | memory fire rate 3.9% vs. 5% task-dispatch floor | CARRIED-FORWARD |
| flag-008 (FB-004) | NI density at 25.8% | CARRIED-FORWARD — no change (40 entries / 155 protos stable) |
| flag-009 (FB-005) | Taylor feeling rate 1.9% | CARRIED-FORWARD |
| flag-010 (META-001) | tensometer ~153 vs. actual 155 | CARRIED-FORWARD |
| flag-011 (META-002) | state-updates secondary YAML frontmatter blocks | CARRIED-FORWARD |
| flag-013 (SUP-001) | vibes:2 @15 forward-anchor | CARRIED-FORWARD |
| flag-015 (CON-002) | memory monument-type calibration — all PASS | CARRIED-FORWARD (clean note) |
| flag-016 (CON-003) | Earth-Bet hard-fence scan — ZERO HITS | UPDATED — new cycle-3 content rescanned; ZERO HITS maintained |
| flag-019 (TF-001) | @162 eleven-item pile-up | CARRIED-FORWARD |
| flag-021 (FB-006/CURVE-002) | tens 3.9% Exemption 5 floor breach | CARRIED-FORWARD as SIGNAL — orchestrator decision now documented in footer |
| flag-022 (AP-003) | vibes:32 AP8 sentence-form violation | **CLOSED** — see §Verification |
| flag-023 (META-003) | tensometer footer/Active-3s/axis-citations stale | **CLOSED** — see §Verification |

---

## §Verification of targeted r3 items

### flag-022 (AP-003) — vibes:32 AP8 sentence-parsability — CLOSED

Post-cycle-3 vibes:32 token bundle at line 97 of vibes.md:
`[record-discipline-flipped-at-the-wall, parallel-truths-as-coincidence-in-log, log-instrument-now-shaping-what-counts]`

- `record-discipline-flipped-at-the-wall` — compound nominal phrase; no finite verb. PASS.
- `parallel-truths-as-coincidence-in-log` — noun phrase ("parallel truths" + prepositional chain); no finite verb. PASS.
- `log-instrument-now-shaping-what-counts` — present-participle phrase; no finite main verb. PASS (borderline present-participle structure was flagged in r3 as "not conclusively sentence-form"; confirmed PASS in the absence of a finite verb).

All three tokens are noun-phrase or participle form. AP8 violation resolved. CLOSED.

---

### flag-023 (META-003) — tensometer footer staleness — CLOSED

Post-cycle-3 tensometer.md frequency-band footer (lines 193–196):
- "Total entries: ~155" — correct.
- "3s: 6/155 ≈ 3.9%" — correct; matches actual 3s count (@11, @42, @67, @68, @139, @162).
- Active-3s list (line 213): "Six total (down from seven; local-@90/season-@417 maester-sets-pen downgraded 3→2)" — correct; @90 is no longer listed as a live 3.
- Axis citations summary "3s justified (active; 6 total)" — lists @394, @395, @468, @522, @523, @524 (local @67, @68, @139, @11, @42, @162). Six entries. @417/@90 listed under "Previously rated 3, downgraded." Correct.
- "2s: ~44/155 ≈ 28.4%" — updated to reflect cycle-3 downrates (@83+@84) and upgrade (@160).
- "1s: ~105/155 ≈ 67.7%" — updated.
- Orchestrator decision language present: "orchestrator decision: 3.9% band-floor breach is SIGNAL not HARD per Exemption 5 + auditor r3 + worm-canon explicit acceptance of the @90 downgrade price; dark-fantasy dissent noted but auditor classification governs."

All three stale elements resolved. CLOSED.

---

### flag-021 (FB-006/CURVE-002) — tens 3.9% Exemption 5 floor breach — SIGNAL (orchestrator-decided)

Footer accurately reflects the breach and the orchestrator-classification decision. The 3.9% per-episode rate is 0.1 points below the relaxed per-episode floor of 4.0% under Exemption 5. The footer records:

- The four positive Exemption 5 criteria (a)–(d) quoted against the tone-law card.
- The breach quantum (0.1 points).
- Structural-climax preservation (@139, @162 both remain 3).
- Scene-level rupture criteria met at all named scenes.
- Orchestrator classification: SIGNAL not HARD; dark-fantasy dissent documented but auditor classification governs.

Per orchestrator decision, this stays SIGNAL. No HARD finding. The footer is now the canonical record of this decision. CARRIED-FORWARD as SIGNAL — no further fixer action required; disposition is by design.

---

### flag-006 (FB-002) — tens 2s at 30.3% — SUBSTANTIALLY RESOLVED

Cycle-3 edits to the 2s rung: @83 downrated 2→1 (-1), @84 downrated 2→1 (-1), @160 upgraded 1→2 (+1). Net: -1 from the pre-cycle-3 count. Post-cycle-3 footer reads "~44/155 ≈ 28.4%."

28.4% is within the standard 20-30% band. The advisory concern about 2s ceiling breach is resolved at the approximate count level. Note: the r3 count was ~47 (30.3%), and the arithmetic of net-1 from 47 yields ~46 (29.7%), not 44 (28.4%). The "~" qualifier on the footer count absorbs this discrepancy under the existing META-001 approximation flag (flag-010). The result falls within band regardless of whether the true 2s count is 44, 45, or 46 (all produce rates of 28.4%–29.7%, all within the 20-30% standard band). Advisory concern does not warrant independent carry-forward at this count. Routing to flag-010 for the approximation note.

---

### New content — Earth-Bet hard-fence scan — ZERO HITS

Case-insensitive substring scan on all cycle-3 fixer content:

**interest-narrator rewrites (narrator:29, :37, :42, :43, :44, :45):**
- narrator:29: "the south-wall column is the fifth count in the log and the hand that closes the cover is hers" — PASS.
- narrator:37: "the wall comes up under the eye and the apparatus reads two open columns on the same page as the same kind of record" — PASS.
- narrator:42: "the second seal fires and the interior does not count this as the second — it already knew the shape a file of this kind carries before the first seal landed" — PASS.
- narrator:43: "the coin arrives and the body already knows the denomination before the fist closes — the knowing is older than this hand" — "older than this hand" is generic body-age language; not an Earth-Bet proper noun. PASS.
- narrator:44: "the seal closes and the interior recognizes the architecture — a place that receives and does not reply; the body has been on the other side of this kind of seal" — PASS.
- narrator:45: "the body knows this angle — it is older than any wall faced before; the body that has stood here in a different room does not need the log to know the decision is already made" — "different room" is generic spatial reference; not an Earth-Bet proper noun. PASS.

**loc-state:6a:** "the ground floor's ambient smell — dried compound and mineral residue — faintly acrid at baseline; smell-baseline established for this space" — PASS.

**sensory:9 (rewrite):** "smell: apothecary-compound-ambient -> stair-compound-concentration" — PASS.

Total Earth-Bet proper-noun hits across all new cycle-3 content: ZERO. flag-016 CLEAN status maintained.

---

### New content — structural scan

**loc-state:6a @43:** Entry is at correct episodic anchor (@43 is within the apothecary scene); single perceptible focus element (smell baseline); correctly anchors sensory:9's old-state chain. The comment "# added cycle-3: sensory:9 @87 old-state baseline chain" documents the purpose. PASS.

**sensory:9 @87 old-state chain:** old-state `apothecary-compound-ambient` now maps to the smell baseline established at loc-state:6a @43 (which fires before @87). The sequence: loc-state:6 @34 (apothecary-door-open, no smell noted) → loc-state:6a @43 (smell-baseline established: "dried compound and mineral residue — faintly acrid at baseline") → loc-state:25 @87 (stair-mid, dispensary-below) → sensory:9 @87 (smell: apothecary-compound-ambient → stair-compound-concentration). Chain is coherent; old-state inherits from the established @43 baseline; new-state fires on concentration increase at the stair. PASS.

**tens:78 @83 and tens:79 @84 downrates:** Entry 78 reads `@83 1` with comment "# downrated 2→1: maester-market trip is transit/respite; no commit bone; 2 overstatement per screen-writer advisory (cycle-3 cape-fic callout)". Entry 79 reads `@84 1` with analogous comment. Market-trip transit context; no rupture in adjacent bones; downrate defensible per AP1 (ambient escalation refusal). Adjacency: @82=1, @83=1, @84=1, @85=1 — flat transit stretch is correct for a market-trip scene with no commit bone. PASS.

**tens:150 @160 upgrade:** Entry 150 reads `@160 2` with axis note: "approach-charge — eastern-quarter walk is the pre-commit load for the wall-facing terminal beat; ramp 2→2→2→3 (@159=2, @160=2, @161=2, @162=3) restores clean escalation into denouement registration." Adjacency: @159(2)→@160(2)→@161(2)→@162(3) — clean 2-2-2-3 ramp; no 1→3 jump. Bridge preserved. PASS.

**NI density post-cycle-3:** 4 deletions (cycle 1→2) + 4 additions (cycle-2 augmentation entries narrator:42–45) = stable. Task-dispatch states 40 entries / 155 protos = 25.8%. Confirms flag-008 count unchanged. No new density movement.

---

### Cross-facet consistency — new entries

**loc-state:6a @43 ↔ sensory:9 @87:** Mutual co-citation confirmed in cite-index context (loc-state:6a added @43; sensory:9 old-state inherits the baseline). Directional consistency: loc-state fires first, sensory fires at @87 citing the established baseline. PASS.

**narrator:42–45 ↔ tens contract:** All four augmentation entries fire at tens=3 anchors (@42, @67, @139, @162). Cross-facet contract: NI entries expected to cluster around tens-transitions and at tens=3 peaks. All four satisfy this. PASS.

---

## Class 1 — STRUCTURAL

### flag-002 (STR-002) — NI ID gaps — CARRIED-FORWARD

- **id:** flag-002
- **type:** flag
- **class:** STRUCTURAL — SIGNAL
- **what:** interest-narrator.md ID gaps at positions 7, 19, 22, 27, 28. File jumps: 6→8, 18→20, 21→23, 26→29. Inline deletion notes present for :19, :22, :28; absent for :7 and :27. No change in substance since r3.
- **why:** Downstream tooling monotonic-ID assumption risk. Editor advisory.
- **routing:** interest-narrator author (advisory)

---

### flag-003 (STR-003) — tensometer dual-file identity — CARRIED-FORWARD

- **id:** flag-003
- **type:** flag
- **class:** STRUCTURAL — SIGNAL
- **what:** tensometer.md and tensometer-s01e03.md remain confirmed identical. URI-028 carry-forward note present. Dual-file redundancy structurally sound per dual-provenance rule. No change.
- **why:** Informational only.
- **routing:** n/a

---

## Class 2 — FREQUENCY-BAND

### flag-006 (FB-002) — tens 2s — SUBSTANTIALLY RESOLVED

- **id:** flag-006
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL (downgraded advisory)
- **what:** Post-cycle-3 footer reports ~44/155 ≈ 28.4% 2s. Within the standard 20-30% band. Cycle-3 edits (@83+@84 downrated, @160 upgraded) brought the 2s rung back inside band from the r3 reading of ~30.3%. A ~2-unit discrepancy between the arithmetic expectation from r3 (+net -1 = ~46) and the footer's ~44 remains; absorbed by existing META-001 approximation flag. Advisory concern substantially resolved.
- **why:** 2s now within standard band. Residual approximation concern folds into flag-010.
- **routing:** n/a (advisory downgraded; flag-010 carries the approximation concern)

---

### flag-007 (FB-003) — memory fire rate 3.9% — CARRIED-FORWARD

- **id:** flag-007
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** memory.md fire rate at 6/155 = 3.9%. Unresolved inconsistency between task-dispatch band (5-12%) and internal rubric (1-5%). No change.
- **why:** Below 5% floor if task-dispatch band is authoritative.
- **routing:** memory author + rubric maintainer

---

### flag-008 (FB-004) — NI density 25.8% — CARRIED-FORWARD

- **id:** flag-008
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** interest-narrator.md fire rate at 40/155 = 25.8%. 4 deletions (cycle 1→2) + 4 additions (augmentation entries narrator:42–45) = net stable from the 25.8% reading established in r3. No change.
- **why:** NI above 25% ceiling advisory; editor-call at wrap.
- **routing:** interest-narrator author (editor advisory)

---

### flag-009 (FB-005) — Taylor feeling rate 1.9% — CARRIED-FORWARD

- **id:** flag-009
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** Taylor feeling fire rate 3/155 = 1.9%, 0.1% below 2% per-character floor. No change.
- **why:** Within rounding at 0.1% shortfall.
- **routing:** feeling author — taylor slice (advisory)

---

### flag-021 (FB-006/CURVE-002) — tens 3.9% Exemption 5 — SIGNAL (orchestrator-decided, no action required)

- **id:** flag-021
- **type:** flag
- **class:** FREQUENCY-BAND + CURVE-SHAPE — SIGNAL
- **what:** tens 3s at 6/155 = 3.9%, 0.1 points below relaxed per-episode floor of 4.0% (Exemption 5). Footer updated with orchestrator decision: SIGNAL not HARD. Dark-fantasy dissent documented; auditor classification governs. All six active 3s verified (@11, @42, @67, @68, @139, @162). Scene-level rupture criteria met at all named scenes. The Exemption 5 criteria and breach quantum are now accurately stated in the footer.
- **why:** Remains SIGNAL per orchestrator decision. Disposition is final for this cycle.
- **routing:** n/a (orchestrator decision on file; no further remediation)

---

## Class 3 — METADATA-INCONSISTENCY

### flag-010 (META-001) — tensometer ~153 vs. actual 155 — CARRIED-FORWARD

- **id:** flag-010
- **type:** flag
- **class:** METADATA-INCONSISTENCY — SIGNAL
- **what:** tensometer.md URI-028 carry-forward note body states "Total active tens entries post-prune: ~153" but cite-index and the frequency-band footer both record 155. Additionally, the cycle-3 footer 2s count (~44) diverges from the arithmetic expectation of ~46 derived from the r3 count (~47) minus the cycle-3 net -1 edit; the "~" qualifier absorbs this. No change in the ~153 vs. 155 discrepancy since r1.
- **why:** Documentation inconsistency; carry-forward note says "~153" and should read "155." Approximation discrepancies in the footer are advisory only.
- **routing:** tensometer author (documentation fix: update URI-028 carry-forward note count)

---

### flag-011 (META-002) — state-updates secondary YAML blocks — CARRIED-FORWARD

- **id:** flag-011
- **type:** flag
- **class:** METADATA-INCONSISTENCY — SIGNAL
- **what:** state-updates.md consolidated file contains secondary raw YAML-frontmatter-style blocks in oc-broken-maester and oc-tanner-father source sections. No change.
- **why:** Multiple frontmatter-style blocks; parser risk.
- **routing:** state-updates consolidator

---

## Class 4 — CURVE-SHAPE

No new curve-shape findings. CURVE-001 confirmed CLOSED in r3 (both arms). Post-cycle-3: @159(2)→@160(2)→@161(2)→@162(3) ramp intact. @9(1)→@10(2)→@11(3) ramp intact. No 1→3 direct jumps in the active tensometer. CLEAN.

---

## Class 5 — CONTRADICTION

No contradictions. loc-state:6a @43 → sensory:9 @87 chain is internally coherent. Narrator augmentation entries (narrator:42–45) carry displacement/foreknowledge-clamp/age-mismatch registers consistent with the worm-canon behavioral pack; no contradiction with adjacent facets. No new cross-facet contradictions introduced by cycle-3 fixer.

---

## Class 6 — DEDUP

No within-facet same-anchor duplicates. loc-state:6a @43 fires at @43; no other loc-state entry targets the apothecary interior smell at that anchor. sensory:9 @87 is the sole sensory entry at @87. CLEAN.

---

## Class 7 — SUPERFLUOUS

### flag-013 (SUP-001) — vibes:2 @15 forward-anchor — CARRIED-FORWARD

- **id:** flag-013
- **type:** flag
- **class:** SUPERFLUOUS — SIGNAL
- **what:** vibes:2 @15 forward-anchor fire licensed by state events at @8/@11; fires one beat after. Advisory placement. No change.
- **why:** Post-event vibe placement one beat removed. Advisory.
- **routing:** vibes author (advisory)

---

## Class 8 — CONSTRAINT

### flag-015 (CON-002) — memory monument-type — CARRIED-FORWARD (clean)

- **id:** flag-015
- **type:** flag
- **class:** CONSTRAINT — SIGNAL — memory monument-type (clean note)
- **what:** All six active memory entries (mem:4, mem:7, mem:8, mem:10, mem:11, mem:12) pass monument-type calibration. No condition-card slugs used as target-references. No change.
- **why:** All pass. Noting for completeness.
- **routing:** n/a (clean)

---

### flag-016 (CON-003) — Earth-Bet hard-fence scan — CLEAN (cycle-3 content rescanned)

- **id:** flag-016
- **type:** flag
- **class:** CONSTRAINT — SIGNAL — Earth-Bet hard-fence (clean note)
- **what:** Full rescan of all cycle-3 fixer content (narrator:29/:37/:42/:43/:44/:45 rewrites, loc-state:6a addition, sensory:9 rewrite): ZERO HITS on Earth-Bet proper nouns. "older than this hand" (narrator:43) and "different room" (narrator:45) are generic register language, not proper-noun leaks. ZERO HITS maintained across all facets.
- **why:** Clean. Noting for completeness.
- **routing:** n/a (clean)

---

## Class 9 — AP-SCAN

### flag-022 (AP-003) — vibes:32 AP8 — CLOSED

See §Verification above. Post-cycle-3 token `parallel-truths-as-coincidence-in-log` is a noun phrase; no finite verb. AP8 sentence-form violation resolved. CLOSED.

---

## Class 10 — TASTE-FLAG

### flag-019 (TF-001) — @162 eleven-item pile-up — CARRIED-FORWARD

- **id:** flag-019
- **type:** flag
- **class:** TASTE-FLAG — SIGNAL
- **what:** Proto-line @162 carries 11 co-cited facet entries: loc-state:24, mem:12, narrator:37, narrator:45, state:61, vibes:8, vibes:29, vibes:30, vibes:31, vibes:32, vibes:33. Count unchanged from r3. This is the cycle-3 audience gate's highest-density anchor.
- **why:** Eleven-item pile-up at single anchor; over-decoration candidate.
- **routing:** audience adversarial gate (cycle-3 re-fire)

---

## Pile-up Review (r4)

| anchor | proto-line | count | verdict |
|--------|-----------|-------|---------|
| @162 | Taylor faces wall | 11 | warranted — season-close structural climax; all 11 serve distinct structural purposes; vibe-density flagged as TF-001; count unchanged from r3 |
| @11 | clerk crosses Fish Gate | 7 | warranted — Scene 1 rupture peak |
| @67 | elder places coin | 7 | warranted — coin-transfer peak (tens=3) |
| @125 | Taylor faces Red Keep | 7 | warranted — season-ceiling registration |
| @139 | elder seals account | 7 | warranted — structural climax (three-axis tens=3) |
| @42 | second clerk releases book | 6 | warranted — Scene 3 rupture peak |
| @90 | maester sets pen | 6 | warranted — approach-charge Scene 5 beat; tens=2 per cycle-1 downgrade; all six facets cover distinct surfaces |
| @98 | father speaks to elder | 5 | warranted — village-claim formalization |

---

## Audit Summary

Total active findings: 13 SIGNAL, 0 HARD.

**HARD (0):** None. HARD = 0 condition holds.

**SIGNAL (13):**
- flag-002 (STR-002): NI ID gaps at :7 and :27 without in-file deletion comments (advisory)
- flag-003 (STR-003): tensometer dual-file identity confirmed (informational)
- flag-006 (FB-002): tens 2s ~28.4%, within band — advisory substantially resolved (approximation residual folds into flag-010)
- flag-007 (FB-003): memory fire rate 3.9% vs. 5% task-dispatch floor; band inconsistency
- flag-008 (FB-004): NI density 40/155 = 25.8%, 0.8% above 25% ceiling (stable; editor advisory)
- flag-009 (FB-005): Taylor feeling rate 1.9%, 0.1% below 2% floor (rounding margin)
- flag-010 (META-001): tensometer carry-forward note "~153" vs. actual 155; cycle-3 2s approximation discrepancy absorbed under "~"
- flag-011 (META-002): state-updates consolidated file secondary YAML frontmatter blocks
- flag-013 (SUP-001): vibes:2 @15 forward-anchor (advisory)
- flag-015 (CON-002): memory monument-type — all six PASS (clean note)
- flag-016 (CON-003): Earth-Bet hard-fence — ZERO HITS across all facets incl. cycle-3 content (clean note)
- flag-019 (TF-001): @162 eleven-item pile-up (audience gate candidate)
- flag-021 (FB-006/CURVE-002): tens 3.9% Exemption 5 breach — SIGNAL per orchestrator decision; footer accurate; no further action

**CLOSED in this pass (r3 → r4):**
- flag-022 (AP-003): vibes:32 AP8 sentence-form — `parallel-truths-as-coincidence-in-log` is noun-phrase; CLOSED
- flag-023 (META-003): tensometer footer/Active-3s/axis-citations stale — all three sections updated; CLOSED

---

## Routing Block

| finding | type | routing |
|---------|------|---------|
| flag-002 (STR-002) | SIGNAL | interest-narrator author (advisory) |
| flag-003 (STR-003) | SIGNAL | n/a |
| flag-006 (FB-002) | SIGNAL | n/a (advisory resolved; approximation note folded into flag-010) |
| flag-007 (FB-003) | SIGNAL | memory author + rubric maintainer |
| flag-008 (FB-004) | SIGNAL | interest-narrator author (editor advisory at wrap) |
| flag-009 (FB-005) | SIGNAL | feeling author — taylor slice (advisory) |
| flag-010 (META-001) | SIGNAL | tensometer author (documentation fix) |
| flag-011 (META-002) | SIGNAL | state-updates consolidator |
| flag-013 (SUP-001) | SIGNAL | vibes author (advisory) |
| flag-015 (CON-002) | SIGNAL | n/a (clean) |
| flag-016 (CON-003) | SIGNAL | n/a (clean) |
| flag-019 (TF-001) | SIGNAL | audience adversarial gate (cycle-3 re-fire) |
| flag-021 (FB-006/CURVE-002) | SIGNAL | n/a (orchestrator decision on file; final) |
