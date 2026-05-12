audit: facets-final-r3
episode: s01e03
date: 2026-05-12
mode: flag-only
status: FINDINGS-PRESENT

---

# Phase 5 Facets Audit — s01e03 — r3

## Preamble

Re-audit after fixer pass (cycle 2). Inputs: all nine facet files (post-fixer), _cite-index.md (327 entries; 50.3% density; rebuilt via build_cite_index.py --skip-merge after cycle-2 fixer pass), .r2-decisions.md (unchanged). Fixer reported 4 tensometer rating edits, 5 vibes token/license rewrites plus orchestrator stale-license cleanup, 11 state-update log_entries_episode counter entry deletions plus state:61 rewrite plus state:28 relocation, 5 loc-state entry rewrites plus 2 new entries (loc-state:24/25), 3 narrator entry deletions plus 4 narrator entry rewrites plus 4 narrator entries added (narrator:42-45), 1 metaphor rider clause trim, 1 sensory entry deleted plus 4 old-state baselines fixed plus 1 sensory entry added, 3 memory description rewrites, 2 feeling rewrites, 21 cascade proto-line token edits.

Scope of r3 verification: (1) confirm the r2 HARD=0 status is maintained; (2) verify specific fixer-pass targets from the dispatch task; (3) identify any new findings introduced by the cycle-2 fixer pass; (4) re-evaluate SIGNAL findings for state changes.

---

## Carry-forward from r2

| r2 id | r2 finding | r3 status |
|-------|-----------|-----------|
| flag-001 (STR-001) | feeling citation token mismatch | CLOSED r1 — not re-opened |
| flag-002 (STR-002) | NI deletion gaps without in-file comments | CARRIED-FORWARD as flag-002 |
| flag-003 (STR-003) | tensometer dual-file identity | CARRIED-FORWARD as flag-003 |
| flag-004 (STR-004) | state-update citation token mismatch | CLOSED r1 — not re-opened |
| flag-005 (FB-001) | tens 3s at 4.5% — Exemption 5 | SEE flag-021 (status changed; see §New findings below) |
| flag-006 (FB-002) | tens 2s at 30.3% above ceiling | UPDATED as flag-006 (count unchanged; see note) |
| flag-007 (FB-003) | memory fire rate 3.9% vs. 5% floor | CARRIED-FORWARD as flag-007 |
| flag-008 (FB-004) | NI density at 25.2% at ceiling | UPDATED as flag-008 (density worsened to 25.8%) |
| flag-009 (FB-005) | Taylor feeling fire rate 1.9% below floor | CARRIED-FORWARD as flag-009 |
| flag-010 (META-001) | tensometer ~153 entry count vs. actual 155 | CARRIED-FORWARD as flag-010 |
| flag-011 (META-002) | state-updates secondary YAML frontmatter blocks | CARRIED-FORWARD as flag-011 |
| flag-012 (CURVE-001) | two 1→3 direct jumps at @10→@11 and @161→@162 | CLOSED — see §Verification below |
| flag-013 (SUP-001) | vibes:2 @15 forward-anchor licensed-by | CARRIED-FORWARD as flag-013 |
| flag-014 (CON-001) | vibes licensed-by non-canonical token forms | CLOSED r1 — not re-opened |
| flag-015 (CON-002) | memory monument-type calibration — all PASS | CARRIED-FORWARD as flag-015 (clean note) |
| flag-016 (CON-003) | Earth-Bet hard-fence scan — ZERO HITS | CARRIED-FORWARD as flag-016 (clean note, new content re-scanned) |
| flag-017 (AP-001) | vibes AP8 sentence-parsability violations — vibes:1/7/8 | CLOSED for original three; see flag-022 (new violation at vibes:32 introduced by fixer) |
| flag-018 (AP-002) | tensometer AP2 speech-beat default concerns | CLOSED — tens:48 @51 and tens:97 @103 downgraded to r=1 by fixer |
| flag-019 (TF-001) | @162 six-vibe pile-up over-decoration candidate | CARRIED-FORWARD as flag-019 (updated count: 11-item pile-up) |
| flag-020 (CON-004) | vibes:7/28 forward state-update:60 license | CLOSED — see §Verification below |

Totals from r2: 6 CLOSED (flag-001, flag-004, flag-012, flag-014, flag-017-partial, flag-018, flag-020), 13 CARRIED-FORWARD/UPDATED, 3 new findings (flag-021, flag-022, flag-023).

---

## §Verification of targeted r2 items

### flag-012 (CURVE-001) — two 1→3 jumps — CLOSED

**@161→@162 arm:** Fixer edited tens:151 @161 1→2. Post-fixer tensometer sequence: @160(r=1) → @161(r=2) → @162(r=3). Bridge is present. Jump resolved. CLOSED.

**@10→@11 arm:** tens:11 @10 r=2 was already present in the file (cite-index confirms `tens:11 @10 r=2 back=N`). Sequence: @9(r=1) → @10(r=2) → @11(r=3). Bridge was in place; r2 carry-forward was in error — the @10 bridging entry existed pre-r3. Both arms of flag-012 are now confirmed resolved. CLOSED.

### flag-017 (AP-001) — AP8 sentence-parsability — vibes:1/7/8 — CLOSED

Post-fixer vibes:1 tokens: `[first-external-record-now-beyond-reach, name-carried-beyond-retrieval-window, debt-acquiring-administrative-mobility]` — no sentence-form tokens. PASS.

Post-fixer vibes:7 tokens: `[ceiling-named-not-yet-reached, red-keep-400m-past-current-radius, front-met-structural-wall]` — no sentence-form tokens. PASS.

Post-fixer vibes:8 tokens: `[architecture-changed-file-unknown, capability-expanding-legibility-not-matching, file-status-opaque-to-subject]` — no sentence-form tokens. PASS.

Original three sentence-form violations resolved. CLOSED. See flag-022 for new violation introduced by the same fixer pass.

### flag-018 (AP-002) — tensometer AP2 speech-beat defaults — CLOSED

tens:48 @51 downgraded to r=1 (confirmed in tensometer.md: entry 48 reads `@51 1`). tens:97 @103 downgraded to r=1 (confirmed: entry 97 reads `@103 1`). cite-index confirms `tens:48 @51 r=1` and `tens:97 @103 r=1`. Advisory concern resolved by rating correction. CLOSED.

### flag-020 (CON-004) — vibes:7/28 forward state-update:60 license — CLOSED

Post-fixer vibes:7 licensed-by: `state-update:56, proto:125` — state-update:60 removed. Confirmed in cite-index: `vibes:7 lic-out=[state-update:56, proto:125]`.

Post-fixer vibes:28 licensed-by: `state-update:56, proto:125, tens:2` — state-update:60 removed. Confirmed in cite-index: `vibes:28 lic-out=[state-update:56, proto:125, tens:2]`.

Both forward-license citations to state-update:60 (@155) removed from vibes anchored at @125. CLOSED.

### state:28 relocation — no contradiction

state:28 @164 now targets `actor:taylor-hebert-flea-bottom.knowledge.maester-in-log: unknown -> named-in-log-paired-with-hightower-file`. Taylor's actor state.md contains no prior `knowledge.maester-in-log` field. Field extension is first-touch at @164. Old value `unknown` is consistent with Taylor having no prior documented awareness of the maester as a log subject. No contradiction with prior Taylor state. CLEAN.

### state:61 new value — no contradiction

state:61 @162 value `close-states-recorded-without-cause-assigned` is consistent with vibes:31's `close-states-recorded-without-cause-is-the-season-exit-condition` and with the denouement scene's structural function. The knowledge field `record-discipline-state` transitions from `parallel-logs-honest` (established baseline per field-extension note) to the new value at the wall-facing beat. No cross-facet contradiction. CLEAN.

### sensory:1/2/4/8 old-state lineage — CLEAN

- sensory:1 @11 old-state `flea-bottom-junction-ambient`: consistent with loc-state:2 @3 `junction-open`. PASS.
- sensory:2 @34 old-state `flea-bottom-morning-clear-cold`: consistent with loc-state:4 @23 `morning | wind-cold`. PASS.
- sensory:4 @67 old-state `alley-ambient-air`: consistent with loc-state:8 @56 `alley-narrow, dock-adjacent` (scene location preceding the exchange). PASS.
- sensory:8 @148 old-state `room-ambient-cold`: consistent with loc-state:16 @118 `loc-flea-bottom-base | dawn | cold` (interior); new-state `outdoor-winter-cold` consistent with loc-state:19 @148 `base-door, circuit-start`. PASS.

### New entries citation token resolution — CLEAN

- loc-state:24 @162: cite-index `back=Y`, co-entries all resolve at @162. PASS.
- loc-state:25 @87: cite-index `back=Y co=[sensory:9]`. sensory:9 @87 exists and resolves. PASS.
- narrator:42 @42, narrator:43 @67, narrator:44 @139, narrator:45 @162: all show `back=Y` in cite-index with correct co-citations. PASS.
- sensory:9 @87: cite-index `back=Y co=[loc-state:25]`. loc-state:25 @87 exists. PASS.

### Vibes stale-license cleanup verification — CLEAN

vibes:15 lic-out=[proto:89, proto:90, tens:3] — no deleted state-update references. PASS.
vibes:16 lic-out=[proto:89, proto:90, tens:3] — no deleted state-update references. PASS.
vibes:18 lic-out=[proto:90, proto:93, proto:94, tens:3] — no deleted state-update references. PASS.
vibes:31 lic-out=[state-update:61, proto:162, proto:165, tens:3] — state-update:61 exists at @162. PASS.
vibes:34 lic-out=[state-update:61, proto:163, proto:164, proto:165, tens:3] — state-update:61 @162 exists. PASS.

### Deleted state-update ID cascade verification — CLEAN

Deleted IDs: 38, 41, 43, 46, 48, 49, 51, 53, 55, 59, 62. Cite-index `### state` section confirms none of these IDs appear as live entries. No back=Y entries for any deleted ID. Cascade-clean confirmed. PASS.

---

## Class 1 — STRUCTURAL

### Finding STR-002 (CARRIED-FORWARD)
- **id:** flag-002
- **type:** flag
- **class:** STRUCTURAL — SIGNAL
- **what:** interest-narrator.md ID gaps at positions 7, 19, 22, 27, 28 (post-R2 deletions of narrator:7, narrator:19, narrator:22, narrator:28). File jumps from ID 6 to ID 8, from ID 18 to ID 20, from ID 21 to ID 23, from ID 26 to ID 29. No in-file deletion-gap comments except for narrator:19, narrator:22, narrator:28 which have inline deletion notes. No change in substance since r2.
- **why:** Downstream tooling that expects monotonic IDs without gaps may misparse. Editor-call.
- **routing:** interest-narrator author (advisory)

---

### Finding STR-003 (CARRIED-FORWARD)
- **id:** flag-003
- **type:** flag
- **class:** STRUCTURAL — SIGNAL
- **what:** tensometer.md and tensometer-s01e03.md are confirmed identical. URI-028 carry-forward note present. Dual-file redundancy structurally sound per dual-provenance rule. No change since r2.
- **why:** No downstream risk. Informational only.
- **routing:** n/a

---

## Class 2 — FREQUENCY-BAND

### Finding FB-001 — STATUS CHANGED: see flag-021 below

The fixer downgraded tens:85 @90 from r=3 to r=2. This changes the 3s count and affects the Exemption 5 criteria. See Class 10 (new finding flag-021) for the updated FREQUENCY-BAND / CURVE-SHAPE joint finding on the Exemption 5 floor breach.

---

### Finding FB-002 (CARRIED-FORWARD with count update)
- **id:** flag-006
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** Post-fixer 2s count: fixer made four rating edits — tens:48 @51 (2→1, net -1 from 2s), tens:97 @103 (2→1, net -1 from 2s), tens:85 @90 (3→2, net +1 to 2s), tens:151 @161 (1→2, net +1 to 2s). Net change to 2s count: -1-1+1+1 = 0. 2s count remains at ~47/155 ≈ 30.3%. Standard band ceiling is 30%. 0.3% over ceiling, within "roughly" qualifier. No change in verdict from r2. The tensometer footer still reads "2s: ~47/155 ≈ 30.3%."
- **why:** 2s above ceiling advisory for ambient-escalation inflation.
- **routing:** dramatist (advisory at wrap)

---

### Finding FB-003 (CARRIED-FORWARD)
- **id:** flag-007
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** memory.md fire rate at 6/155 = 3.9%. Unresolved inconsistency between task-dispatch band (5-12%) and internal rubric (1-5%). No change since r2.
- **why:** Below 5% floor if task-dispatch band is authoritative.
- **routing:** memory author + rubric maintainer

---

### Finding FB-004 (UPDATED — count worsened)
- **id:** flag-008
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** interest-narrator.md fire rate at 40/155 = 25.8% after cycle-2 fixer pass. Fixer deleted narrator:19/22/28 (-3 entries) and added narrator:42-45 (+4 entries): net +1 entry, moving from 39/155 = 25.2% (r2) to 40/155 = 25.8%. Task-dispatch NI band ceiling is 25%. Now 0.8% over ceiling (was 0.2% in r2). Still SIGNAL, not HARD. The exceedance has grown modestly.
- **why:** NI above ceiling is advisory signal for momentum risk. Exceedance has increased from 0.2% to 0.8%.
- **routing:** interest-narrator author (editor advisory — the four cycle-2 augmentation entries that pushed density from 25.2% to 25.8% should be noted at wrap)

---

### Finding FB-005 (CARRIED-FORWARD)
- **id:** flag-009
- **type:** flag
- **class:** FREQUENCY-BAND — SIGNAL
- **what:** Taylor feeling fire rate 3/155 = 1.9%, 0.1% below 2% per-character floor. No change since r2.
- **why:** Within rounding at 0.1% shortfall.
- **routing:** feeling author — taylor slice (advisory)

---

## Class 3 — METADATA-INCONSISTENCY

### Finding META-001 (CARRIED-FORWARD)
- **id:** flag-010
- **type:** flag
- **class:** METADATA-INCONSISTENCY — SIGNAL
- **what:** tensometer.md URI-028 carry-forward note states "Total active tens entries post-prune: ~153" but cite-index records 155 tens entries and the frequency-band footer counts "Total entries: ~155." No change since r1/r2.
- **why:** Documentation inconsistency; "~153" should read "155."
- **routing:** tensometer author (documentation fix)

---

### Finding META-002 (CARRIED-FORWARD)
- **id:** flag-011
- **type:** flag
- **class:** METADATA-INCONSISTENCY — SIGNAL
- **what:** state-updates.md consolidated file contains secondary raw YAML-frontmatter-style blocks in per-character source sections (oc-broken-maester and oc-tanner-father source sections). No change since r1/r2.
- **why:** YAML parsers encountering multiple frontmatter-style blocks may fail or misparse.
- **routing:** state-updates consolidator

---

### Finding META-003 (NEW — introduced by fixer rating edit)
- **id:** flag-023
- **type:** flag
- **class:** METADATA-INCONSISTENCY — SIGNAL
- **what:** tensometer.md frequency-band footer and axis citations summary are stale after the fixer downgraded tens:85 @90 from r=3 to r=2.
  - Footer line "3s: 7/155 ≈ 4.5%" is now incorrect; actual 3s post-fixer = 6/155 ≈ 3.9%.
  - The "Active 3s" list in the frequency-band footer still enumerates "@417" (per-episode local @90, the pen-set beat) as a live 3. @90 is now r=2.
  - The axis citations summary section "3s justified" still reads "@417: reversal-proximity peaks — oc-broken-maester sets the pen" as a listed 3.
  - None of these documentary sections were updated when the tens:85 entry was edited.
- **why:** The stale footer actively misrepresents the 3s rate, which is now 3.9% — below the relaxed per-episode floor of 4.0% cited in the Exemption 5 claim. A reader of the tensometer file cannot determine the actual 3s frequency without re-counting. This interacts with flag-021 (the Exemption 5 floor breach).
- **routing:** tensometer author (update footer count, Active 3s list, and axis citations summary to reflect @90 as r=2)

---

## Class 4 — CURVE-SHAPE

### Finding CURVE-001 — CLOSED

See §Verification above. Both arms of the 1→3 jump (at @10→@11 and @161→@162) are now bridged by intervening r=2 entries. CLOSED.

---

## Class 5 — CONTRADICTION

No cross-facet contradictions found. State-update chains internally consistent. New entries (loc-state:24/25, narrator:42-45, sensory:9, state:28, state:61 rewrite) verified clean against prior state and adjacent facet entries. The state:28 relocation to Taylor's knowledge field is consistent with POV-authority rules and first-touch field-extension protocol. No new contradictions introduced by the cycle-2 fixer pass.

---

## Class 6 — DEDUP

No within-facet same-anchor duplicates found. No change since r2.

---

## Class 7 — SUPERFLUOUS

### Finding SUP-001 (CARRIED-FORWARD)
- **id:** flag-013
- **type:** flag
- **class:** SUPERFLUOUS — SIGNAL
- **what:** vibes:2 @15 forward-anchor fire: licensed by state events at @8/@11, fires at @15. Advisory placement; schema permits. No change since r2.
- **why:** Post-event vibe placement at one beat remove. Advisory.
- **routing:** vibes author (advisory)

---

## Class 8 — CONSTRAINT

### Finding CON-002 (CARRIED-FORWARD — clean)
- **id:** flag-015
- **type:** flag
- **class:** CONSTRAINT — SIGNAL — memory monument-type calibration
- **what:** All six active memory entries (mem:4, mem:7, mem:8, mem:10, mem:11, mem:12) pass monument-type calibration. The three rewritten entries (mem:4, mem:11, mem:12) target free-text mechanism glosses, not condition-card slugs. mem:4 target: `previous-life classification-architecture / register-of-act-without-content`. mem:11 target: `previous-life dying-tutor / helpless-protector pattern / tutor-figure whose session terminates`. mem:12 target: `previous-life refusal-to-look / enclosed-space-with-the-decision-the-record-will-not-name`. All three pass. No change in verdict.
- **why:** All pass. Noting for completeness.
- **routing:** n/a (clean)

---

### Finding CON-003 (CARRIED-FORWARD — clean, new content re-scanned)
- **id:** flag-016
- **type:** flag
- **class:** CONSTRAINT — SIGNAL — Earth-Bet hard-fence scan
- **what:** Case-insensitive substring scan on all new content introduced by the cycle-2 fixer pass: vibes:1/7/8/32 token rewrites, narrator:42-45 additions, loc-state:24/25 additions, sensory:9 addition, memory:4/11/12 rewrites, feeling:3/7 rewrites. ZERO HITS on Earth-Bet proper nouns in any story-payload text field. Clean.
- **why:** Clean. Noting for completeness.
- **routing:** n/a (clean)

---

## Class 9 — AP-SCAN

### Finding AP-001 — CLOSED for vibes:1/7/8

See §Verification above. All three original sentence-form tokens replaced with nominal hyphenated phrases. CLOSED.

---

### Finding AP-002 — CLOSED

See §Verification above. tens:48 and tens:97 downgraded to r=1 by fixer. Advisory concern resolved. CLOSED.

---

### Finding AP-003 (NEW — introduced by fixer vibes:32 rewrite)
- **id:** flag-022
- **type:** flag
- **class:** AP-SCAN — SIGNAL — vibes AP8 sentence-parsability (vibes:32)
- **what:** vibes:32 @162 token bundle post-fixer: `[record-discipline-flipped-at-the-wall, the-log-now-calls-parallel-truths-coincidence, log-instrument-now-shaping-what-counts]`. The token `the-log-now-calls-parallel-truths-coincidence` parses as a complete sentence: subject("the log") + adverb("now") + verb("calls") + direct object("parallel truths") + object complement("coincidence"). Sentence-form tokens are forbidden per vibes AP8. The token `log-instrument-now-shaping-what-counts` is a present-participle phrase without a finite main verb — borderline but not conclusively sentence-form. The first token is a clear AP8 violation.
  - This violation was introduced by the cycle-2 fixer rewrite of vibes:32 (r2 flagged the original vibes:32 via flag-017 as one of the three AP8 violations; fixer rewrote it; the rewrite contains a new AP8 violation).
- **why:** Sentence-form tokens forbidden per vibes schema; the operator receives this as narrative-ready prose rather than a compressed keyword, which defeats the compression function of the token layer.
- **routing:** vibes author (revise `the-log-now-calls-parallel-truths-coincidence` to noun-phrase or compressed form)

---

## Class 10 — TASTE-FLAG

### Finding TF-001 (CARRIED-FORWARD — count updated)
- **id:** flag-019
- **type:** flag
- **class:** TASTE-FLAG — SIGNAL — over-decoration candidate at @162
- **what:** Proto-line @162 ("taylor-hebert-flea-bottom faces the wall") now carries 11 co-cited facet entries (up from 9 in r2): loc-state:24, mem:12, narrator:37, narrator:45, state:61, vibes:8, vibes:29, vibes:30, vibes:31, vibes:32, vibes:33. The fixer added loc-state:24 and narrator:45 to this anchor. Six vibes entries remain. Count increased from 9 to 11.
- **why:** Eleven-item pile-up at single anchor is the highest density in the graph. Pre-flagged for audience adversarial gate.
- **routing:** vibes author + audience adversarial gate

---

## Class 11 — NEW FINDINGS (not mapped to previous classes)

### Finding FB-006 / CURVE-002 (NEW — introduced by fixer rating edit)
- **id:** flag-021
- **type:** flag
- **class:** FREQUENCY-BAND + CURVE-SHAPE — SIGNAL — Exemption 5 floor breach
- **what:** Fixer downgraded tens:85 @90 from r=3 to r=2. This removes one 3 from the episode count. Post-fixer 3s count: 6/155 = 3.87% ≈ 3.9%.

  The tensometer's Exemption 5 claim (URI-034, 2026-05-11) states the per-episode relaxed floor is 4.0%. Criterion (c) requires "per-episode 3s rate ≥ relaxed per-episode floor 4.0%." At 3.9% the per-episode rate is **below the relaxed per-episode floor** by ~0.1 percentage points.

  Additionally, the season-average 3s rate was cited in r2 as "21/464 ≈ 4.5% at the relaxed season-average floor exactly." The @90 downgrade removes one 3 from the s01e03 count. If s01e03 now contributes 6 threes instead of 7, the season total drops to 20/464 ≈ 4.3%. This remains above the 4.0% relaxed per-episode equivalent but the s01e03 contribution is now below the stated per-episode floor.

  The Active 3s list in the tensometer footer (stale, per flag-023) still claims @417 (=@90) as a live 3. The actual active 3s in s01e03 are: @11, @42, @67, @68, @139, @162 — six entries.

  Note: the r=2 annotation on tens:85 @90 carries an axis note `# axis: approach-charge (reversal-proximity light)` which explicitly characterizes the beat as "approach-charge" not "reversal-proximity peaks," consistent with the downgrade rationale.
- **why:** The Exemption 5 claim's per-episode criterion (c.i) now fails by 0.1%. If the exemption is voided, the 3s rung at 3.9% falls below both the standard floor (5%) and the relaxed floor (4.0%), which is a FREQUENCY-BAND below-floor advisory. The exemption claim must be re-evaluated against the corrected 3s count. This interacts with flag-023 (stale footer).
- **routing:** tensometer author + dramatist (re-evaluate Exemption 5 criterion (c.i) at 6/155 = 3.9%; update footer per flag-023; determine whether exemption holds at new rate or whether the below-floor reading requires acknowledgment)

---

## Pile-up Review (updated)

| anchor | proto-line | count | verdict |
|--------|-----------|-------|---------|
| @162 | taylor faces the wall | 11 | warranted — season-close structural climax; all 11 serve distinct structural purposes; vibe-density flagged as TF-001; count increased from 9 (r2) to 11 (r3) via fixer additions of loc-state:24 and narrator:45 |
| @11 | clerk crosses Fish Gate | 7 | warranted — Scene 1 rupture peak; all 7 facets serve distinct functions |
| @67 | elder places coin | 7 | warranted — coin-transfer peak (tens=3); all 7 cover distinct ground |
| @125 | Taylor faces Red Keep | 7 | warranted — season-ceiling registration; forward-license on state-update:60 now CLOSED (flag-020) |
| @139 | elder seals account | 7 | warranted — structural climax; all 7 facets cover distinct structural surfaces |
| @42 | second clerk releases book | 6 | warranted — Scene 3 rupture peak |
| @90 | maester sets pen | 6 | warranted — Scene 5 peak; note: tens:85 @90 now r=2 per fixer downgrade; pile-up count unchanged (feel:1, mem:11, narrator:21, state:19, vibes:15, vibes:16); structural justification for co-citation remains (approach-charge classification; all six facets still address distinct functional surfaces) |
| @98 | father speaks to elder | 5 | warranted — village-claim formalization peak |

---

## Audit Summary

Total findings: 18 active findings across 7 classes.

**HARD (0):**
- No HARD findings. HARD = 0 condition holds.

**SIGNAL (18):**
- flag-002 (STR-002): NI ID gaps without in-file comments (advisory)
- flag-003 (STR-003): tensometer dual-file identity confirmed (informational)
- flag-006 (FB-002): tens 2s at 30.3%, 0.3% above ceiling (unchanged; within "roughly" qualifier)
- flag-007 (FB-003): memory fire rate 3.9% vs. 5% task-dispatch floor; band inconsistency
- flag-008 (FB-004): NI density now 40/155 = 25.8%, 0.8% above 25% ceiling (worsened from r2's 0.2%)
- flag-009 (FB-005): Taylor feeling fire rate 1.9%, 0.1% below 2% floor (rounding margin)
- flag-010 (META-001): tensometer carry-forward note says ~153 entries vs. actual 155
- flag-011 (META-002): state-updates consolidated file has secondary YAML frontmatter blocks in per-character source sections
- flag-013 (SUP-001): vibes:2 @15 forward-anchor fire licensed by state events at @8/@11 (advisory)
- flag-015 (CON-002): memory monument-type calibration — all six entries PASS (clean note)
- flag-016 (CON-003): Earth-Bet hard-fence scan — ZERO HITS (clean note; new content re-scanned)
- flag-019 (TF-001): @162 eleven-item pile-up — over-decoration candidate for audience gate (count increased from 9 to 11)
- flag-021 (FB-006/CURVE-002 NEW): tensometer Exemption 5 per-episode floor breach — 3s at 3.9% after @90 downgrade, below 4.0% relaxed floor; stale footer; Active-3s list includes @90 erroneously
- flag-022 (AP-003 NEW): vibes:32 AP8 sentence-parsability violation — token `the-log-now-calls-parallel-truths-coincidence` is sentence-form; introduced by cycle-2 fixer rewrite
- flag-023 (META-003 NEW): tensometer frequency-band footer, Active-3s list, and axis citations summary stale after @90 rating downgrade

CLOSED between r2 and r3 (5): flag-012 (CURVE-001 both arms), flag-017 (AP-001 for vibes:1/7/8), flag-018 (AP-002), flag-020 (CON-004)

---

## Routing Block

| finding | type | routing |
|---------|------|---------|
| flag-002 (STR-002) | SIGNAL | interest-narrator author (advisory) |
| flag-003 (STR-003) | SIGNAL | n/a |
| flag-006 (FB-002) | SIGNAL | dramatist (advisory at wrap) |
| flag-007 (FB-003) | SIGNAL | memory author + rubric maintainer |
| flag-008 (FB-004) | SIGNAL | interest-narrator author (editor advisory) |
| flag-009 (FB-005) | SIGNAL | feeling author — taylor slice (advisory) |
| flag-010 (META-001) | SIGNAL | tensometer author (documentation fix) |
| flag-011 (META-002) | SIGNAL | state-updates consolidator |
| flag-013 (SUP-001) | SIGNAL | vibes author (advisory) |
| flag-015 (CON-002) | SIGNAL | n/a (clean) |
| flag-016 (CON-003) | SIGNAL | n/a (clean) |
| flag-019 (TF-001) | SIGNAL | vibes author + audience adversarial gate |
| flag-021 (FB-006/CURVE-002) | SIGNAL | tensometer author + dramatist (Exemption 5 re-evaluation at 6/155 = 3.9%) |
| flag-022 (AP-003) | SIGNAL | vibes author (revise vibes:32 sentence-form token) |
| flag-023 (META-003) | SIGNAL | tensometer author (footer + Active-3s + axis citations update) |
