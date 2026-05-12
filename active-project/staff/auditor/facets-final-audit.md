audit: facets-final-r2
episode: s01e03
date: 2026-05-12
mode: flag-only
status: FINDINGS-PRESENT
totals: 18 findings across 7 facets

---

# Phase 5 Facets Audit — s01e03 — r2

## Preamble

Re-audit after fixer pass. Inputs: proto-lines/s01e03.md (155 active proto-lines, post-fixer token rewrites), nine facet files at active-project/theater/facets/ (post-fixer vibes.md), _cite-index.md (335 entries; 54.2% density; rebuilt via build_cite_index.py --skip-merge after fixer pass), .r2-decisions.md, and fixer mapping tables (s01e03-state-update-cite-mapping.md, s01e03-vibes-state-update-mapping.md, s01e03-vibes-feeling-mapping.md). Fixer reported 6 feeling citation token rewrites, 35 state-update citation token rewrites, and 53 vibes licensed-by token rewrites.

Scope of r2 verification: (1) confirm the three r1 HARD findings are CLEAN; (2) scan for new findings introduced by the fixer pass; (3) re-evaluate 16 r1 SIGNAL findings for state changes.

---

## Carry-forward from r1

| r1 id | r1 finding | r2 status |
|-------|-----------|-----------|
| flag-001 (STR-001) | feeling citation token mismatch | CLOSED — see §Verification below |
| flag-002 (STR-002) | NI deletion gaps without in-file comments | CARRIED-FORWARD as flag-002 |
| flag-003 (STR-003) | tensometer dual-file identity | CARRIED-FORWARD as flag-003 |
| flag-004 (STR-004) | state-update citation token mismatch | CLOSED — see §Verification below |
| flag-005 (FB-001) | tens 3s at 4.5% — Exemption 5 | CARRIED-FORWARD as flag-005 |
| flag-006 (FB-002) | tens 2s at 30.3% above ceiling | CARRIED-FORWARD as flag-006 |
| flag-007 (FB-003) | memory fire rate 3.9% vs. 5% floor | CARRIED-FORWARD as flag-007 |
| flag-008 (FB-004) | NI density at 25.2% at ceiling | CARRIED-FORWARD as flag-008 |
| flag-009 (FB-005) | Taylor feeling fire rate 1.9% below floor | CARRIED-FORWARD as flag-009 |
| flag-010 (META-001) | tensometer ~153 entry count vs. actual 155 | CARRIED-FORWARD as flag-010 |
| flag-011 (META-002) | state-updates secondary YAML frontmatter blocks | CARRIED-FORWARD as flag-011 (fixer did not touch file structure) |
| flag-012 (CURVE-001) | two 1→3 direct jumps at @10→@11 and @161→@162 | CARRIED-FORWARD as flag-012 |
| flag-013 (SUP-001) | vibes:2 @15 forward-anchor licensed-by | CARRIED-FORWARD as flag-013 (see note) |
| flag-014 (CON-001) | vibes licensed-by non-canonical token forms | CLOSED — see §Verification below |
| flag-015 (CON-002) | memory monument-type calibration — all PASS | CARRIED-FORWARD as flag-015 (clean note) |
| flag-016 (CON-003) | Earth-Bet hard-fence scan — ZERO HITS | CARRIED-FORWARD as flag-016 (clean note) |
| flag-017 (AP-001) | vibes AP8 sentence-parsability violations | CARRIED-FORWARD as flag-017 (fixer did not touch token text) |
| flag-018 (AP-002) | tensometer AP2 speech-beat default concerns | CARRIED-FORWARD as flag-018 |
| flag-019 (TF-001) | @162 six-vibe pile-up over-decoration candidate | CARRIED-FORWARD as flag-019 |

Totals from r1: 3 CLOSED, 16 CARRIED-FORWARD, 1 new finding introduced by fixer pass (flag-020).

---

## §Verification of r1 HARD findings

### STR-001 (flag-001) — feeling citation tokens — CLOSED

Post-fixer proto-lines verified against consolidated feeling.md:
- Proto-line @6: `[feel:2]` — feel:2 @6 (oc-tanner-elder). Correct.
- Proto-line @15: `[feel:5]` — feel:5 @15 (taylor-hebert-flea-bottom). Correct.
- Proto-line @53: `[feel:6]` — feel:6 @53 (taylor-hebert-flea-bottom). Correct.
- Proto-line @98: `[feel:4]` — feel:4 @98 (oc-tanner-father). Spurious `[feel:1]` removed. Correct.
- Proto-line @131: `[feel:3]` — feel:3 @131 (oc-tanner-elder). Spurious `[feel:2]` removed. Correct.
- Proto-line @145: `[feel:7]` — feel:7 @145 (taylor-hebert-flea-bottom). Correct.

Cite-index confirmation: feel:1 back=Y @90 only; feel:2 back=Y @6 only; feel:3 back=Y @131 only; feel:4 back=Y @98 only; feel:5 back=Y @15 only; feel:6 back=Y @53 only; feel:7 back=Y @145 only. No spurious cross-citations. All seven feeling entries correctly anchored. **CLOSED.**

### STR-004 (flag-004) — state-update citation tokens — CLOSED

Post-fixer proto-lines verified against consolidated state-updates.md (env IDs 1-27, per-character IDs 28-62):
- @8: `[state:36]` `[state:2]` — state:36 = taylor.knowledge.first-clerk-record @8 (correct); state:2 = env @8 (correct, env ID unchanged).
- @11: `[state:37]` `[state:4]` — state:37 = taylor.knowledge.first-clerk-record @11 (correct); state:4 = env @11 (correct, env ID unchanged).
- @15: `[state:38]` — taylor.log_entries_episode @15 (correct).
- @22: `[state:39]` `[state:40]` — both taylor @22 (correct).
- @24: `[state:41]`, @26: `[state:42]`, @30: `[state:43]`, @40: `[state:44]`, @42: `[state:45]`, @47: `[state:46]`, @67: `[state:29]` `[state:47]` `[state:13]`, @70: `[state:48]`, @93: `[state:49]`, @96: `[state:33]`, @98: `[state:34]`, @101: `[state:35]`, @103: `[state:50]`, @107: `[state:51]`, @114: `[state:52]`, @116: `[state:53]`, @118: `[state:54]`, @123: `[state:55]`, @125: `[state:20]` `[state:56]`, @129: `[state:30]`, @133: `[state:57]`, @137: `[state:31]`, @139: `[state:32]` `[state:22]`, @142: `[state:58]`, @145: `[state:59]`, @155: `[state:60]`, @161: `[state:25]`, @162: `[state:61]`, @164: `[state:28]` `[state:62]`, @165: `[state:27]` — all correct per the fixer mapping table.

Specific corrections confirmed: @96 `[state:33]` (was `[state:1]`); @125 `[state:56]` (was `[state:21]`); @164 `[state:28]` `[state:62]` (was `[state:1]` `[state:27]`). Cite-index records all 62 state entries with back=Y and correct anchor positions. **CLOSED.**

### CON-001 (flag-014) — vibes licensed-by non-canonical token forms — CLOSED

Post-fixer vibes.md verified: all 34 entries use canonical `state-update:<consolidated-N>` and `feeling:<consolidated-N>` forms exclusively. Cite-index lic-out columns for all vibes entries show only canonical forms (state-update:N, feeling:N, proto:N, tens:N, world-build:gloss). No `state-update-<slug>:N` or `feeling-<slug>:N` forms present. Specific rewrites confirmed:
- vibes:12 @67 and vibes:21 @100: `feeling-oc-tanner-elder:1` → `feeling:2`. Both confirmed in vibes.md and in cite-index (vibes:12 lic-out=[state-update:29, proto:67, feeling:2, tens:3]; vibes:21 lic-out=[state-update:34, proto:98, proto:99, proto:100, feeling:2]).
- All 33 vibes state-update licensed-by tokens confirmed rewritten to consolidated forms. **CLOSED.**

---

## Class 1 — STRUCTURAL

### Finding STR-002 (CARRIED-FORWARD)
- **id:** flag-002
- **type:** flag
- **class:** STRUCTURAL — SIGNAL
- **what:** interest-narrator.md ID gaps at positions 7 and 27 (post-R2 deletions). File jumps from ID 6 to ID 8, and from ID 26 to ID 28. No in-file deletion-gap comments. Schema permits gaps; R2 decisions document the deletions. No change since r1.
- **why:** Downstream tooling that expects monotonic IDs without gaps may misparse. Editor-call.
- **routing:** interest-narrator author (advisory)

---

### Finding STR-003 (CARRIED-FORWARD)
- **id:** flag-003
- **type:** flag
- **class:** STRUCTURAL — SIGNAL
- **what:** tensometer.md and tensometer-s01e03.md are confirmed identical. URI-028 carry-forward note present and accurate. Dual-file redundancy structurally sound per dual-provenance rule. No change since r1.
- **why:** No downstream risk. Informational only.
- **routing:** n/a

---

## Class 2 — FREQUENCY-BAND

### Finding FB-001 (CARRIED-FORWARD)
- **id:** flag-005
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** tensometer.md 3s frequency at 4.5% (7/155). Exemption 5 (Tone-law-licensed slow-burn) confirmed valid against all four rubric criteria. Per-episode rate 4.5% ≥ relaxed per-episode floor 4.0%. Season-average 3s across s01: 21/464 ≈ 4.5%, at the relaxed season-average floor exactly. No change since r1.
- **why:** Season-average at relaxed floor with no attrition margin. Any further 3s attrition in subsequent episodes would breach the 4.5% season-average criterion and invalidate the exemption retroactively.
- **routing:** dramatist (advisory)

---

### Finding FB-002 (CARRIED-FORWARD)
- **id:** flag-006
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** tensometer.md 2s frequency at 30.3% (47/155 approx). Standard band ceiling is 30%. The fixer pass did not touch tensometer.md. 0.3% over ceiling. Rubric "roughly" qualifier applies.
- **why:** 2s above ceiling advisory for ambient-escalation inflation. At 0.3% over ceiling with "roughly" qualifier, advisory only.
- **routing:** dramatist (advisory at wrap)

---

### Finding FB-003 (CARRIED-FORWARD)
- **id:** flag-007
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** memory.md fire rate at 6/155 = 3.9%. Task-dispatch FREQUENCY-BAND class specifies memory band as 5-12%; memory rubric internally claims 1-5%. Unresolved inconsistency between task-dispatch band and internal rubric. At 3.9%, below 5% floor if task-dispatch is authoritative. No change since r1.
- **why:** If authoritative band is 5-12%, below floor. Band inconsistency between task-dispatch and memory rubric unresolved.
- **routing:** memory author + rubric maintainer (clarify authoritative band)

---

### Finding FB-004 (CARRIED-FORWARD)
- **id:** flag-008
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** interest-narrator.md fire rate at 39/155 = 25.2% (after R2 deletions; 39 active entries). Task-dispatch NI band ceiling is 25%. At 25.2% the file is 0.2% over the ceiling. No change since r1.
- **why:** NI at or above ceiling is advisory signal for momentum risk. Not a protocol violation at 0.2% margin.
- **routing:** interest-narrator author (editor advisory)

---

### Finding FB-005 (CARRIED-FORWARD)
- **id:** flag-009
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** Taylor feeling fire rate 3/155 = 1.9%, nominally below the 2% per-character floor. Shortfall is 0.1% at 155-line denominator. No change since r1.
- **why:** Within rounding at 0.1% shortfall. Editor-advisory.
- **routing:** feeling author — taylor slice (advisory)

---

## Class 3 — METADATA-INCONSISTENCY

### Finding META-001 (CARRIED-FORWARD)
- **id:** flag-010
- **type:** flag
- **class:** METADATA-INCONSISTENCY — SIGNAL
- **what:** tensometer.md URI-028 carry-forward note states "Total active tens entries post-prune: ~153" but cite-index records 155 tens entries and the frequency-band footer counts "Total entries: ~155." The "~153" figure predates the final prune count. No change since r1.
- **why:** Documentation inconsistency; the "~153" note should read "155."
- **routing:** tensometer author (documentation fix)

---

### Finding META-002 (CARRIED-FORWARD)
- **id:** flag-011
- **type:** flag
- **class:** METADATA-INCONSISTENCY — SIGNAL
- **what:** state-updates.md consolidated file still contains secondary raw YAML frontmatter-style blocks in per-character source sections. The oc-broken-maester source section (after the canonical top-of-file frontmatter block) begins with `facet: state-updates / episode: s01e03 / target-scope: actor:oc-broken-maester / author: dialogue-writer-fork:oc-broken-maester` as undelimited YAML fields. The oc-tanner-father source section contains the same pattern (`facet: state-updates / episode: s01e03 / target-scope: actor:oc-tanner-father / author: dialogue-writer-fork:oc-tanner-father`). Per URI-040 convention, these should be plain-comment slice headers only. The fixer pass addressed token content but not file structure. No change since r1.
- **why:** YAML parsers encountering multiple frontmatter-style blocks may fail or misparse.
- **routing:** state-updates consolidator (YAML→comment headers)

---

## Class 4 — CURVE-SHAPE

### Finding CURVE-001 (CARRIED-FORWARD)
- **id:** flag-012
- **type:** flag
- **class:** CURVE-SHAPE — SIGNAL
- **what:** Two 1→3 direct jumps without a bridging 2 at the immediately-preceding beat: @10(r=1)→@11(r=3) and @161(r=1)→@162(r=3). Both have documented axis justifications (cycle-3 F7-bone rescue rupture additions). No change since r1.
- **why:** 1→3 direct jumps may cause stitcher misread; documented axis justifications present. Not a hard fail.
- **routing:** dramatist (advisory)

---

## Class 5 — CONTRADICTION

No cross-facet contradictions found. State-update chains are internally consistent. The log open/close sequence, maester pen, elder account cascade all verified clean. No new contradictions introduced by the fixer pass. (The @125 pile-up anomaly noted in r1 as "may cause false co-citation" due to the stale state:21 is now resolved — state:56 is the correct consolidated citation, and state:21 remains correctly at @138 for the oc-elder-account.physical_condition entry.)

One note from r1 carried forward: state-update env entry 19 fires at @90 (`oc-maester-pen.physical_condition: writing -> set`) with `<old>` value "writing" assumed; maester-pen initial condition is untestable without prior-episode write-back record for this first-touch OC prop. No new information.

---

## Class 6 — DEDUP

No within-facet same-anchor duplicates found. The double-3 at @67/@68 is the intentional double-tap device. No dedup violations found. No change since r1.

---

## Class 7 — SUPERFLUOUS

### Finding SUP-001 (CARRIED-FORWARD)
- **id:** flag-013
- **type:** flag
- **class:** SUPERFLUOUS — SIGNAL
- **what:** vibes:2 @15 forward-anchor fire: the vibe fires at @15 but its licensed-by sources (state-update:37 @11, state-update:36 @8) are from prior beats. Post-fixer the token forms are now canonical (state-update:37, state-update:36), making the forward-anchor relationship clearly visible. The vibe placement at @15 is one beat after the state events at @8/@11 that license it. The schema allows post-event placement; the placement is defensible (the log entry beat is the first moment where the register-pressure can express in the POV); the issue is advisory. No change in substance since r1.
- **why:** Post-event vibe placement at one beat remove. Advisory, not hard.
- **routing:** vibes author (advisory)

---

## Class 8 — CONSTRAINT

### Finding CON-001 — CLOSED
(See §Verification above.)

### Finding CON-002 (CARRIED-FORWARD)
- **id:** flag-015
- **type:** flag
- **class:** CONSTRAINT — SIGNAL — memory monument-type calibration
- **what:** All six memory entries (mem:4, mem:7, mem:8, mem:10, mem:11, mem:12) pass the monument-type calibration check. No change since r1.
- **why:** All pass. Noting for completeness.
- **routing:** n/a (clean)

---

### Finding CON-003 (CARRIED-FORWARD)
- **id:** flag-016
- **type:** flag
- **class:** CONSTRAINT — SIGNAL — Earth-Bet hard-fence scan
- **what:** Case-insensitive substring scan across all text fields of all nine facet files — ZERO HITS. No change since r1.
- **why:** Clean. Noting for completeness.
- **routing:** n/a (clean)

---

### Finding CON-004 (NEW — introduced by fixer token rewrite)
- **id:** flag-020
- **type:** flag
- **class:** CONSTRAINT — SIGNAL — vibes forward-license on state-update:60
- **what:** vibes:7 @125 `season + range-at-season-ceiling` cites `licensed-by: state-update:60, state-update:56, proto:125, proto:162`. In the post-fixer state, state-update:60 is `actor:taylor-hebert-flea-bottom.stats.fauna_control_radius_m: 500 -> 600` at **@155** — 30 proto-lines after vibes:7's anchor of @125. Similarly vibes:28 @125 cites `licensed-by: state-update:56, state-update:60, proto:125, tens:2` — the same state-update:60 @155 forward-reference. State-update:56 @125 is on-anchor and correct; only state-update:60 is forward-referenced. Proto:162 in vibes:7's lic-out is also a forward-reference (vibes:7 fires at @125; proto:162 is 37 beats later). These forward-license citations were not visible in r1 because the non-canonical token form `state-update-taylor-hebert-flea-bottom:25` was opaque to the cite-index.
  - Cite-index confirms: vibes:7 lic-out=[state-update:60, state-update:56, proto:125, proto:162]; vibes:28 lic-out=[state-update:56, state-update:60, proto:125, tens:2]. State:60 anchor is @155 in the state section.
  - Note: vibes:5 @155 is correctly anchored at @155 for the 600m event. vibes:7's forward-cite of state-update:60 means it is licensing itself from an event that has not yet occurred at its anchor beat @125. The vibes schema's `licensed-by:` field documents the licensing source; a state-update that fires at @155 cannot be the license for a vibe that fires at @125.
  - Vibes:7's semantic content ("600m-achieved-red-keep-400m-past-reach, s01-range-arc-complete") anticipates the @155 ceiling, framing it as the season closure. This is structurally intentional (the Red Keep sighting at @125 prompts a season-scope vibe that projects the arc completion) but the license source is future. The schema does not define forward-licensing as invalid — `licensed-by:` specifies why the vibe fires, not a causal ordering requirement. The precedent is established by proto:162 also appearing as a forward-reference in vibes:7's lic-out. However, state-update citations carry a stronger resolution implication than proto: citations because state-update:N is expected to be a cite-index-resolved ID pointing to an already-committed state change.
- **why:** Forward-citing a state-update as a license source creates a logical-ordering question for the stitcher: the vibe fires at @125 citing a state change at @155 as its license. The stitcher's operator-guidance interpolation at @125 will include a keyword suggesting range-arc-complete and 600m-achieved, which are true at @155 but not yet true at @125. This is a potential operator over-read at @125 (the operator may write the prose as if 600m is already established when Taylor is at @125 facing the Red Keep at 500m). Advisory: the vibe-7 content may need to be re-scoped to @155 (where the 600m arc completes) or the state-update:60 license removed and replaced with proto:125 alone (acknowledging the 600m as a projected endpoint known from the @125 Red Keep sighting, not a concluded state).
- **routing:** vibes author (advisory — consider whether vibes:7 belongs at @125 or @155, and whether state-update:60 as a forward-license is intentional or a citation error)

---

## Class 9 — AP-SCAN

### Finding AP-001 (CARRIED-FORWARD)
- **id:** flag-017
- **type:** flag
- **class:** AP-SCAN — SIGNAL — vibes AP8 sentence-parsability
- **what:** Three vibes token-bundle items parse as complete sentences: vibes:1 @11 token `the-file-carries-the-name-out-the-gate`; vibes:7 @125 token `the-front-arrived-at-its-structural-wall`; vibes:8 @162 token `she-does-not-know-what-file-she-is-in`. Fixer did not touch vibes token text, only licensed-by source tokens. No change since r1.
- **why:** Sentence-form tokens forbidden per vibes schema.
- **routing:** vibes author

---

### Finding AP-002 (CARRIED-FORWARD)
- **id:** flag-018
- **type:** flag
- **class:** AP-SCAN — SIGNAL — tensometer AP2 speech-beat default
- **what:** tens:48 @51 r=2 (oc-tanner-elder speaks to taylor) and tens:97 @103 r=2 (oc-tanner-elder speaks to taylor) both rated 2 on bare speech beats. Tensometer not touched by fixer. No change since r1.
- **why:** AP2 speech-beat over-rating could inflate 2s band; already at 30.3% above ceiling.
- **routing:** dramatist (advisory)

---

## Class 10 — TASTE-FLAG

### Finding TF-001 (CARRIED-FORWARD)
- **id:** flag-019
- **type:** flag
- **class:** TASTE-FLAG — SIGNAL — over-decoration candidate at @162
- **what:** Proto-line @162 ("taylor-hebert-flea-bottom faces the wall") carries 9 facet co-citations including six vibes entries (vibes:8, vibes:29, vibes:30, vibes:31, vibes:32, vibes:33). No change since r1. Fixer pass did not alter @162's vibe count (vibes:31 retains state-update:28 as a forward-reference from the elder-account axis, which is valid — the season-close vibe licenses itself from the elder's record-channel commitment at @139; state-update:28 @164 is the maester documentation status flip, also a forward-reference in vibes:31 from @162. This is the same forward-license pattern as CON-004 above, but at @162 the forward-reference is only 2-3 beats ahead and the vibes are thematically continuous with the denouement arc; less operationally disruptive).
- **why:** Six-vibe pile-up at single anchor pre-flagged for audience adversarial gate.
- **routing:** vibes author + audience adversarial gate

---

## Class 11 — PILE-UP REVIEW

Post-fixer pile-up verdicts (updated for corrected citations):

| anchor | proto-line | count | verdict |
|--------|-----------|-------|---------|
| @162 | taylor faces the wall | 9 | warranted — season-close structural climax; all 9 serve distinct structural purposes; vibe-density flagged as TF-001 |
| @11 | clerk crosses Fish Gate | 7 | warranted — Scene 1 rupture peak; all 7 facets serve distinct functions; feeling citation now correct (state:37 correctly cited, no spurious feel:1) |
| @90 | maester sets pen | 7 | warranted — Scene 5 peak; all 7 facets serve distinct functions |
| @125 | Taylor faces Red Keep | 7 | warranted — season-ceiling registration; state:56 now correctly cited (was state:21); CON-004 advisory on vibes:7 forward-license applies |
| @67 | elder places coin | 6 | warranted — coin-transfer peak (tens=3); all 6 cover distinct ground; feel:1 spurious co-citation removed (was wrongly inflating r1 @98 count; @98 pile-up now correctly 5) |
| @139 | elder seals account | 6 | warranted — structural climax (three axes); all 6 facets cover distinct structural surfaces |
| @42 | second clerk releases book | 5 | warranted — Scene 3 rupture peak |
| @98 | father speaks to elder | 5 | warranted — village-claim formalization peak; spurious feel:1 removed; count now correct at 5 (feel:4, narrator:39, state:34, vibes:19, vibes:20) |

---

## Audit Summary

Total findings: 18 across 7 facets.

**HARD (0):**
- No HARD findings remain post-fixer.

**SIGNAL (18):**
- flag-002 (STR-002): NI deletion gaps without in-file comments (advisory)
- flag-003 (STR-003): tensometer dual-file identity confirmed (informational)
- flag-005 (FB-001): tens 3s at 4.5% — EXEMPT-TONE-LAW-SLOW-BURN confirmed; season-average at floor, no attrition margin
- flag-006 (FB-002): tens 2s at 30.3%, 0.3% above 30% ceiling (within "roughly" qualifier)
- flag-007 (FB-003): memory fire rate 3.9% vs. task-dispatch 5% floor; rubric band inconsistency surfaced
- flag-008 (FB-004): NI density at 25.2%, at ceiling (editor advisory)
- flag-009 (FB-005): Taylor feeling fire rate 1.9%, 0.1% below 2% floor (rounding margin; editor advisory)
- flag-010 (META-001): tensometer carry-forward note says ~153 entries vs. actual 155
- flag-011 (META-002): state-updates consolidated file has secondary YAML frontmatter blocks in per-character source sections (should be plain-comment headers per URI-040)
- flag-012 (CURVE-001): two 1→3 direct jumps at @10→@11 and @161→@162 without immediately-preceding 2
- flag-013 (SUP-001): vibes:2 @15 forward-anchor fire licensed by state events at @8/@11 (advisory)
- flag-015 (CON-002): memory monument-type calibration — all six entries PASS (clean note)
- flag-016 (CON-003): Earth-Bet hard-fence scan — ZERO HITS (clean note)
- flag-017 (AP-001): vibes AP8 sentence-parsability — three tokens violate (vibes:1, vibes:7, vibes:8)
- flag-018 (AP-002): tensometer AP2 speech-beat default concerns at @51 and @103
- flag-019 (TF-001): @162 six-vibe pile-up — over-decoration candidate for audience gate
- flag-020 (CON-004 NEW): vibes:7 @125 and vibes:28 @125 cite state-update:60 (@155) as a forward-license source — state change at @155 cited as license for vibe firing at @125; operator over-read risk at @125

---

## Routing Block

| finding | type | routing |
|---------|------|---------|
| flag-002 (STR-002) | SIGNAL | interest-narrator author (advisory) |
| flag-003 (STR-003) | SIGNAL | n/a |
| flag-005 (FB-001) | SIGNAL | dramatist (advisory — season-avg at exemption floor) |
| flag-006 (FB-002) | SIGNAL | dramatist (advisory at wrap) |
| flag-007 (FB-003) | SIGNAL | memory author + rubric maintainer (band clarification) |
| flag-008 (FB-004) | SIGNAL | interest-narrator author (editor advisory) |
| flag-009 (FB-005) | SIGNAL | feeling author — taylor slice (advisory) |
| flag-010 (META-001) | SIGNAL | tensometer author (documentation fix) |
| flag-011 (META-002) | SIGNAL | state-updates consolidator (YAML→comment headers) |
| flag-012 (CURVE-001) | SIGNAL | dramatist (advisory — consider bridging 2 at @10 or @161) |
| flag-013 (SUP-001) | SIGNAL | vibes author (advisory) |
| flag-015 (CON-002) | SIGNAL | n/a (clean) |
| flag-016 (CON-003) | SIGNAL | n/a (clean) |
| flag-017 (AP-001) | SIGNAL | vibes author |
| flag-018 (AP-002) | SIGNAL | dramatist (advisory) |
| flag-019 (TF-001) | SIGNAL | vibes author + audience adversarial gate |
| flag-020 (CON-004) | SIGNAL | vibes author (advisory — vibes:7 and vibes:28 forward state-update license at @125) |
