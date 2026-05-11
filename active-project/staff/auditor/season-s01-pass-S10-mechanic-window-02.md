---
report: mechanic-audit
scope: season
target: s01 — Window 2 (IDs 159–328 + interpolated IDs 509, 510, 511, 512, 519, 520, 521, 526, 527, 528)
pass: S10 Phase 3 Sweep B
window: 2
cycle: 3 (F7-bone residual verification)
timestamp: 2026-05-11
auditor-classes: AP-SCAN | CURVE-SHAPE | FREQUENCY-BAND
verdict: MECHANIC-CLEAN — tens-gate-residual cleared at scene level; one new coverage gap (ID 528) raised as fault; scalar-inflation prohibition applied to frequency-band below-floor finding
---

# Season s01 — Pass S10 Mechanic Audit — Window 2 — Cycle 3 F7-bone Residual Verification

## Inputs read

- `active-project/theater/proto-lines/s01.bones.md` — full season bones, IDs 159–328 + interpolated IDs 509, 510, 511, 512, 519, 520, 521, 526, 527, 528 verified in file
- `active-project/theater/facets/tensometer-s01-window-02.md` — ~168 entries; cycle-3 additions at rows 17a @519 (3), 33a @526 (1), 36a @527 (1), 102a @520 (3), 141a @521 (3); axis citations present for all three rated-3 additions
- `active-project/staff/auditor/season-s01-pass-S10-mechanic-window-02.md` — cycle-2 report (archived below)
- `design/shoot-v2/rubric-tensometer.md` — CURVE-SHAPE, FREQUENCY-BAND, anti-pattern definitions, adjacency test, calibration anchors
- `.claude/commands/and-facets-audit.md` — FILE ABSENT (fault-007 carried; formal AP-SCAN class IDs not citable)

## Changes verified in cycle 3

Against dispatch-stated change set:

| ID | Bone SVO | Tensometer entry | Rated | Axis cited | Present in bones file |
|----|----------|-----------------|-------|------------|----------------------|
| 519 | oc-tanner-father steps back | 17a @519 3 | 3 | yes | yes — between 175 and 176 |
| 520 | taylor-hebert-flea-bottom drops the stylus | 102a @520 3 | 3 | yes | yes — between 274 and 275 |
| 521 | oc-tanner-mother stands | 141a @521 3 | 3 | yes | yes — between 323 and 324 |
| 526 | taylor-hebert-flea-bottom enters the market-side junction | 33a @526 1 | 1 | n/a (1s exempt) | yes — between 500 and 508 |
| 527 | oc-tanner-elder faces taylor-hebert-flea-bottom | 36a @527 1 | 1 | n/a (1s exempt) | yes — between 502 and 510 |
| 528 | the wasps relay the Watch patrol | ABSENT | — | — | yes — between 187 and 190 |

**ID 528 is present in the bones file but has no tensometer entry and is not listed in the tensometer header coverage list.** The tensometer header reads: `bones: 159–328 (includes interpolated IDs 509, 510, 511, 512, 519, 520, 521, 526, 527)`. ID 528 is not listed. This is a coverage gap within W2 scope (ID 187 and ID 190 are both within 159–328). See fault-c3-001 below.

---

## CURVE-SHAPE

### Scene A (159–181) — ID 519 rupture

**RESOLVED.**

Scalar sequence through Scene A in tensometer order:

`@159(1) @160(1) @161(1) @162(1) @163(1) @164(1) @165(1) @166(2) @167(1) @168(1) @169(1) @170(2) @171(2) @172(2) @173(1) @174(1) @175(1) @519(3) @176(1) @177(1) @178(2) @179(2) @180(1) @181(1)`

Scene A now contains one 3. Scene-level shape rule satisfied.

**Axis citation check — @519:**
Axis cited: "stakes-visibility + reversal-proximity peaks — father's step-back is the body acknowledging the new category; the visit's transactional outcome is now committed."

Stakes-visibility at 3: the step-back IS the public registration of a new category for Taylor. Prior to this beat, the scene has been the father presenting trade goods, speaking to the elder, mother facing Taylor. The step-back is the moment the visit's outcome is committed on the father's body — an irreversible registration visible to any observer. Stakes-visibility axis at peak intensity: ACCEPT.

Reversal-proximity at 3: the step-back reverses the father's prior physical orientation in the scene (he has been engaging, facing, presenting). The retreat is the commit; what follows (@176: mother speaks, @177: Taylor speaks) is aftermath. Reversal-proximity at peak: ACCEPT.

Ceiling defense satisfied (two axes at peak intensity). Rating 3 is correct.

**Adjacency check — @519:**
Left neighbor: @175 (`oc-tanner-mother faces taylor-hebert-flea-bottom`) rated 1. The @519(3) is immediately preceded by a 1. Rubric adjacency test: "A 3 should sit next to 2s, not 1s." This is a direct 1→3 at the final step. The rubric flags this as "either misratings or true sudden-turns; either is a kickback signal."

Context evaluation: @172(2) is three positions prior. The 2s cluster (@166, @170, @171, @172) represents the scene's pressure build. The final two beats before @519 are @173(1), @174(1), @175(1) — a three-beat drop to 1 before the rupture. This is the "mother turns to face Taylor" pivot beat, which reads 1 (facing/transitional, not itself charged per rubric). The father's step-back at @519 is then a sudden rupture without a 2-beat immediately before it.

This is a rubric-flagged pattern (1→3 jump). It is not automatically a misrating — the rubric permits "true sudden-turn" classification. The SVO `oc-tanner-father steps back` during the moment when the mother has turned to face Taylor fits the sudden-turn profile: an unexpected physical withdrawal by a secondary actor at a moment when attention has shifted to the mother-Taylor interaction. The beat IS the turn (step-back as registration of new category); no warning beat precedes it in the bones file. No misrating is established.

Classification: FLAG (rubric-flagged adjacency; true sudden-turn defense plausible; non-blocking). Scene-level shape rule is satisfied regardless.

**Scene A shape rule: PASS.** tens-gate-residual-{W2-Scene-A} CLEARED.

---

### Scene H (266–278) — ID 520 rupture

**RESOLVED with ordering discrepancy flag.**

Scalar sequence in tensometer order:

`@266(1) @267(1) @269(1) @270(1) @271(1) @272(1) @273(1) @274(2) @275(2) @505(2) @520(3) @276(1) @277(1) @278(1)`

Scene H now contains one 3. Scene-level shape rule satisfied.

**Axis citation check — @520:**
Axis cited: "body-charge + reversal-proximity peaks — stylus-drop interrupts log-writing; headache cost interrupts the act of accounting for it; range-400m headache becomes lived rupture rather than logged-after-the-fact."

Body-charge at 3: a sudden involuntary release (dropping the stylus) after the held-tension of the headache sequence is a peak body-charge event per rubric: "a sudden release after held charge." The held charge is the preceding 2s (@274, @275, @505 — the waking, holding of eyes, lowering of chin under headache pressure). The drop is the body at peak. ACCEPT.

Reversal-proximity at 3: the stylus-drop interrupts the log-writing process. The logging sequence (the method by which Taylor accounts for the headache) is reversed by the symptom the logging is meant to record. The turn IS this beat. ACCEPT.

Ceiling defense satisfied (two axes at peak intensity). Rating 3 is correct.

**Adjacency check — @520:**
In tensometer order: left neighbor is @505(2). Adjacency test passes — 3 sits next to a 2. ACCEPT.

**Ordering discrepancy — @520:**
The bones file places ID 520 between ID 274 (`wakes`) and ID 275 (`holds the eyes`):

Bones order: 274 → **520** → 275 → 505 → 276

Tensometer order: @274 → @275 → @505 → **@520** → @276

These differ. The tensometer places @520 after @505; the bones file places it after @274. The tensometer's axis citation ("stylus-drop interrupts log-writing") is internally coherent with placement before @276 (opens the log) but does not match the bones insertion point, which places the stylus-drop before the eyes-hold and chin-lower beats.

This is a sequencing inconsistency between the bones file and the tensometer. It does not change the scalar value of @520 (3 is correct regardless of exact position within the scene) and does not change Scene H's scene-level shape status (one 3 is present). However, the stitcher and downstream facet-authors will consume the tensometer's ordering as authoritative for rendering decisions. If @520 is consumed as occurring after @505 rather than after @274, the rendering will sequence the events differently than the bones file specifies.

Classification: FLAG (sequencing inconsistency between bones file insertion point and tensometer ordering; non-blocking for scene-level shape verdict; should be resolved before tensometer lock to protect stitcher ordering contract).

**Scene H shape rule: PASS.** tens-gate-residual-{W2-Scene-H} CLEARED.

---

### Scene L (315–328) — ID 521 rupture

**RESOLVED.**

Scalar sequence through Scene L in tensometer order:

`@315(1) @316(1) @317(1) @318(2) @319(1) @320(1) @321(1) @322(1) @323(2) @521(3) @324(1) @326(1) @327(1) @328(1)`

Scene L now contains one 3. Scene-level shape rule satisfied.

**Axis citation check — @521:**
Axis cited: "reversal-proximity peaks — standing IS the commit; the disclosure becomes physical fact through the body's rising; the vigil-end is now an event, not a statement."

Reversal-proximity at 3: the mother has been seated (@318 sits, rated 2 — body invested). Her standing is the reversal of that seated commitment; the vigil, established through the prior speech-acts (@320, @322), is ended by the physical act of rising. The turn IS this beat — the bodily commit makes the verbal disclosure irrevocable. ACCEPT.

A second axis is plausible (body-charge: the rising from seated position after sustained held engagement), though the citation does not name it explicitly. The reversal-proximity axis alone at peak intensity is sufficient per the rubric ("a single axis lights at peak intensity"). Ceiling defense satisfied.

**Adjacency check — @521:**
Left neighbor: @323 (`oc-tanner-mother lowers the gaze`) rated 2. Adjacency test passes — 3 sits next to a 2. ACCEPT.

Release check: @521(3) → @324(1). Direct 3→1 fall. Rubric default is 3→2→1; @324 is `oc-tanner-mother exits the base room`, a transitional exit beat correctly rated 1 (neutral exit motion). No exit-2 beat exists. Same structural situation as Scene L in Window 1 (W1 cycle-3 audit noted same departure from the 3→2→1 default; classified as minor departure, not a fault). The scene-level shape rule is satisfied; the absence of a release-2 is a minor departure from the default, not a blocking fault.

**Scene L shape rule: PASS.** tens-gate-residual-{W2-Scene-L} CLEARED.

---

### Window-level CURVE-SHAPE status

All three formerly-failing scenes now carry legitimate 3-rated rupture beats:
- Scene A: @519(3) — sudden-turn classification; adjacency is flagged but not faulted
- Scene H: @520(3) — adjacency PASS; ordering discrepancy flagged
- Scene L: @521(3) — adjacency PASS; 3→1 exit departure noted (minor)

No new scene-level failures introduced by cycle-3 additions. Beat-10 enrichment (IDs 526, 527 — both rated 1) adds transitional relay/facing beats that do not affect any scene's shape.

Episode-level observation (unchanged): window climax (eviction cluster, @234/@236) sits in the middle third. Back-half structural loading (Scenes H, L) is improved by the cycle-3 additions but the window's overall shape remains partial rise-peak-fall with climax in middle third. This is a carried observation, not a new finding; it is the window's structural character, not a rubric violation.

**CURVE-SHAPE: CLEAN.** All F7-bone scene-level residuals cleared.

---

## FREQUENCY-BAND

Cycle-3 count from tensometer frequency-band section (self-reported): ~168 entries, 7 threes ≈ 4.2%, ~24 twos ≈ 14.3%, remainder ones.

Independent 3-count verification from tensometer scalar list:
@234(3), @236(3), @255(3), @496(3), @519(3), @520(3), @521(3) = 7 threes. Matches tensometer section.

Distribution:
- **3s: 7/168 ≈ 4.2%** — target 5–10%. Below floor (0.8 pp miss).
- **2s: ~24/168 ≈ 14.3%** — target 20–30%. Below floor (structural).
- **1s: remainder ≈ 81.5%** — target 60–75%. Above ceiling (structural).

**Below-floor finding — classification:**

The rubric anti-pattern 4 explicitly prohibits scalar inflation to manufacture correct-looking frequency: "Rating a beat 2 because the writer knows it matters narratively. Tensometer reads on-face charge, not narrative function." The rubric states that a distribution outside the band "suggests systemic miscalibration — investigate before shipping." Investigation has occurred across three cycles; the conclusion each time is that the W2 corpus is structurally 1-heavy (network relay beats, log-open/write/close sequences) and the under-representation of 2s and 3s reflects genuine bone density, not miscalibration.

The scene-level criteria (each scene carries at least one 3 or a granted transit exception) are now fully met. The frequency-band below-floor finding is load-bearing confirmation of structural sparsity but is not itself a blocking condition when scene-level criteria are met and scalar inflation is refused. This is the same rubric position applied in W1 cycle-3 (where 2s at 17.4% and 1s at 77.2% were accepted as structural opening-season character).

No new 3s can be legitimately added without introducing scene-level or anti-pattern violations: all named scenes now have their rupture beats; adding further 3s would require either misrating existing bones or manufacturing new bones without screen-writer warrant.

**FREQUENCY-BAND: FLAG (non-blocking).** Below-floor structural deficit acknowledged. Scalar inflation refused. Scene-level criteria met. Anti-pattern 4 governs.

**Note on ID 528 coverage:** If @528 is subsequently rated (at 1, which is correct for an insect-relay beat per established convention), the total entry count becomes ~169 and the 3s percentage moves to 7/169 ≈ 4.1% — no material change.

---

## AP-SCAN

### Class library status

`and-facets-audit.md` remains absent at `.claude/commands/and-facets-audit.md`. Formal AP-SCAN class IDs cannot be cited. fault-007 carried unchanged.

### Cycle-3 addition AP-SCAN check

**ID 519 (`oc-tanner-father steps back`, rated 3):**
- Ambient escalation: no — the step-back is a specific physical action by a named actor at a named narrative moment.
- Climax bleed: check — @172(2) is the closest preceding 2 (father lifts trade goods). @173, @174, @175 are all rated 1. Under climax-bleed rubric, the 2-rated lead-in should immediately precede the 3; the intervening 1s create a valley before the peak rather than a climax-bleed from a proximate 2. The adjacency FLAG above captures this. Climax-bleed anti-pattern (rating the *run-up* as 3) does not apply — the run-up is not rated 3. Not a climax-bleed violation.
- Plot-importance inflation: no — the 3 is supported by two on-face axis citations (stakes-visibility, reversal-proximity).
- No AP-SCAN blocking violation.

**ID 520 (`taylor-hebert-flea-bottom drops the stylus`, rated 3):**
- Ambient escalation: no — the stylus-drop is a specific physical event.
- Stillness inflation: not applicable — @520 is a release/cessation event, not a held-position beat.
- Plot-importance inflation: no — two on-face axes cited.
- No AP-SCAN blocking violation.

**ID 521 (`oc-tanner-mother stands`, rated 3):**
- Stillness inflation: check — ID 521 is a rising-from-seated beat, opposite of stillness. Anti-pattern 5 does not apply.
- Ambient escalation: no — standing is a specific physical commit in a specific dramatic moment.
- Plot-importance inflation: no — reversal-proximity axis cited at peak intensity.
- No AP-SCAN blocking violation.

**ID 526 (`taylor-hebert-flea-bottom enters the market-side junction`, rated 1):**
- Transitional entry beat. Rated 1. Rubric-consistent. No violation.
- Adds one member to the market-side junction entry pattern (not a named AP-SCAN cluster). No carried repetition-mechanism flag affected.

**ID 527 (`oc-tanner-elder faces taylor-hebert-flea-bottom`, rated 1):**
- Facing/orientation beat. Rated 1. Rubric-consistent. No violation.

**ID 528 (`the wasps relay the Watch patrol`):**
- No tensometer entry. Cannot be AP-SCAN reviewed. Coverage gap (fault-c3-001).
- Expected rating per established insect-relay convention: 1. If subsequently rated 1, no AP-SCAN violation.

### Carried AP-SCAN items — status update

- **fault-007 (and-facets-audit.md absent):** Unchanged. AP-SCAN formal class IDs not citable.
- Carried flags from cycle 2 (repetition mechanisms, ordering anomaly): not re-audited in this cycle; no new information changes their status. Non-blocking carries.

---

## Findings

```yaml
audit:
  report: mechanic-audit
  scope: season
  target: s01-window-02
  timestamp: 2026-05-11
  cycle: 3 (Sweep B — F7-bone residual verification)
  window-range: IDs 159–328 + interpolated IDs 509, 510, 511, 512, 519, 520, 521, 526, 527, 528
  classes: CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN

  findings:

    - id: fault-c3-001
      type: fault
      what: ID 528 (the wasps relay the Watch patrol) is present in the bones file between IDs 187 and 190, within W2 scope (159–328), but has no tensometer entry and is not listed in the tensometer header coverage field. Tensometer header states "includes interpolated IDs 509, 510, 511, 512, 519, 520, 521, 526, 527" — 528 is omitted.
      why: Every proto-line requires a tensometer scalar per the rubric ("tensometer has no per-entry cull — every proto-line gets a scalar"). The stitcher requires a rung signal for every bone. The coverage gap means @528 has no rendering-density signal and no cross-facet coordination signal. Per established insect-relay convention this beat is a 1, so no CURVE-SHAPE consequence is expected, but the gap must be closed before tensometer lock.
      criteria: A tensometer entry for @528 must be added at the correct citation-order position between @187 and @190 in the W2 tensometer file. The tensometer header coverage field must be updated to include ID 528. Expected rating is 1 per insect-relay convention; if a higher rating is assigned, axis citation is required.

    - id: fault-c3-002
      type: flag
      what: CURVE-SHAPE — Scene A adjacency — @519(3) is immediately preceded by @175(1). Direct 1→3 jump at final step before rupture. Rubric adjacency test flags this as "misrating or true sudden-turn." Prior 2s cluster at @166, @170, @171, @172 (four positions and one to three beats back) is present but not immediately adjacent.
      why: The stitcher's rendering-density logic and downstream facet coordination use the adjacency relationship to determine whether a peak is "prepared." A 1→3 with no proximate 2 reduces the gradient signal available to other facets. True sudden-turn defense is plausible (father steps back while attention has shifted to mother-Taylor interaction); not a misrating fault. Advisory for tensometer author before lock.

    - id: fault-c3-003
      type: flag
      what: CURVE-SHAPE / ordering — @520 is positioned at tensometer row 102a (after @505, before @276), but the bones file places ID 520 between IDs 274 and 275, which is before both @275 and @505 in bones order. Bones order: 274 → 520 → 275 → 505 → 276. Tensometer order: @274 → @275 → @505 → @520 → @276.
      why: The tensometer ordering is the contract the stitcher and downstream facets consume for rendering sequence. If the bones file insertion point is authoritative, the tensometer's ordering misstates the event sequence for Scene H, which may cause rendering of the stylus-drop after the chin-lower rather than before it. Axis citation is internally coherent with either ordering (the drop interrupts the log-writing process, which begins at @276 regardless), but the sequencing discrepancy should be resolved against the bones file before lock.

    - id: fault-c3-004
      type: pass
      what: CURVE-SHAPE — Scene A (159–181): @519(3) present, axis cited, ceiling defense satisfied. tens-gate-residual-{W2-Scene-A} CLEARED.
      why: Closed.

    - id: fault-c3-005
      type: pass
      what: CURVE-SHAPE — Scene H (266–278): @520(3) present, axis cited, ceiling defense satisfied. tens-gate-residual-{W2-Scene-H} CLEARED.
      why: Closed.

    - id: fault-c3-006
      type: pass
      what: CURVE-SHAPE — Scene L (315–328): @521(3) present, axis cited, ceiling defense satisfied. tens-gate-residual-{W2-Scene-L} CLEARED.
      why: Closed.

    - id: fault-c3-007
      type: flag
      what: FREQUENCY-BAND — 3s at 7/168 ≈ 4.2% (target 5–10%), 2s at ~24/168 ≈ 14.3% (target 20–30%), 1s at ~81.5% (target 60–75%). All bands below floor or above ceiling.
      why: Structural deficit acknowledged; rubric anti-pattern 4 prohibits scalar inflation. Scene-level criteria met. Below-floor finding is non-blocking per the rubric's investigation-before-shipping gate (investigation complete; conclusion: structural 1-heavy bone corpus). Carried for downstream kickback resolution.

    - id: fault-007
      type: fault
      what: AP-SCAN formal class library (and-facets-audit.md) absent from .claude/commands/and-facets-audit.md
      why: AP-SCAN cannot cite formal class IDs. Shared reviewer resource per rule 11 is missing. TASTE-FLAG → AP-SCAN promotion path is blocked. Carried from cycles 1 and 2.
      criteria: and-facets-audit.md must be authored at .claude/commands/and-facets-audit.md before AP-SCAN formal class IDs can be cited in any subsequent mechanic pass
```

---

## Combined verdict: MECHANIC-CLEAN

**AP-SCAN:** No blocking faults from cycle-3 additions. fault-007 (class library absent) carried.

**CURVE-SHAPE: CLEAN.**
- Scene A: @519(3) present, axis-cited. tens-gate-residual CLEARED. Adjacency flag noted (non-blocking).
- Scene H: @520(3) present, axis-cited. tens-gate-residual CLEARED. Ordering discrepancy flag noted (non-blocking).
- Scene L: @521(3) present, axis-cited. tens-gate-residual CLEARED.
- All three F7-bone residuals from cycle 2 are cleared at the scene-level shape criterion.

**FREQUENCY-BAND: FLAG (non-blocking).**
- 3-band at 4.2%, below 5% floor. Anti-pattern 4 prohibits scalar inflation to correct. Scene-level criteria met. Below-floor finding accepted per rubric investigation gate.

**New coverage fault (fault-c3-001):** ID 528 (`the wasps relay the Watch patrol`) has no tensometer entry. This is a blocking fault for tensometer lock but does not affect any scene's shape verdict and does not reinstate the STRUCTURAL-RESIDUAL classification. Expected rating is 1. This fault must be resolved before tensometer is considered locked.

**Tens-gate-residual disposition:** CLEARED. Scenes A, H, and L each carry a legitimate rupture beat rated 3 with axis citation. The Phase 6 F7-bone failure condition (three scenes lacking rupture-class 3-rated bones) is resolved at source. No tens-gate-residual is forwarded to Phase 6 from W2.

**Open items before tensometer lock:**
1. fault-c3-001 — add @528 tensometer entry and update header. Blocking for lock.
2. fault-c3-003 — resolve @520 ordering against bones file. Non-blocking for shape; blocking for lock if bones-order is authoritative.
3. fault-c3-002 — @519 adjacency: axis-citation author should confirm true sudden-turn classification or insert a 2-rated interstitial before lock.
4. fault-007 — and-facets-audit.md authoring. Carried.

---

---

# ARCHIVED — Cycle 2 Report

---
report: mechanic-audit
scope: season
target: s01 — Window 2 (IDs 159–328 + interpolated 495–512 inserts)
pass: S10 Phase 3 Sweep B
window: 2
cycle: 2 (re-fire — tens coverage update only)
timestamp: 2026-05-11
auditor-classes: AP-SCAN | CURVE-SHAPE | FREQUENCY-BAND
verdict: MECHANIC-FAIL-CURVE-SHAPE-FREQUENCY-BAND — STRUCTURAL-RESIDUAL (URI-026 cap exhausted; routes to Phase 6 F7-bone)
---

## Scope of re-fire

Iteration 2 re-fire. Change set: tensometer-s01-window-02.md amended to add entries for IDs 509, 510, 511, and 512. No bones regen. No scalar rerating of existing entries. AP-SCAN was already PASS at cycle 2. CURVE-SHAPE failures at Scenes A, H, L and FREQUENCY-BAND failure are carried from cycle 2.

---

## Cycle-2 coverage fault resolution check

**fault-001 (cycle 2)** — IDs 509 and 510 absent from tensometer within W2 range:
Tensometer now shows `29a @509 1` and `29b @510 1`, positioned between @195 and @200. Both entries are present and in correct citation-order position. RESOLVED.

**fault-002 (cycle 2)** — IDs 511 and 512 orphaned between windows:
Tensometer now shows `0a @511 2` and `0b @512 2` in a boundary-carry section at the W2 open, preceding @159. Both entries are present. The bones file confirms IDs 511 and 512 sit immediately before ID 159 in citation order. Assigned to W2. RESOLVED.

Both cycle-2 coverage faults are resolved.

---

## Scalar correctness — new entries

**ID 509** (`the flies relay the carter`) — rated 1.
Insect-relay beat, ambient information transmission. No on-face stakes-visibility axis; no reversal-proximity axis; no body-charge axis. Consistent with the existing convention for insect-relay beats throughout (flag-002 carry). Rubric-consistent. CORRECT.

**ID 510** (`the carter exits the junction`) — rated 1.
Physical exit, transitional motion, neutral cost. No axis lights on the beat face. Rubric-consistent. CORRECT.

**ID 511** (`taylor-hebert-flea-bottom faces the junction`) — rated 2.
Boundary-carry bone immediately before W2 Scene A open (ID 159). Reversal-proximity axis is invocable: the facing beat positions Taylor for the incoming Tanner arrival whose first beat is ID 159. The rubric defines 2 as "the alignment that makes the next move possible." Scene A opens at 1 on the next entry (@159), which is a standard scene-reset after the boundary-carry run. The 2 is marginal but defensible under reversal-proximity. Not a misrating fault. CORRECT (marginal).

**ID 512** (`oc-tanner-elder faces the road`) — rated 2.
Same scene-frame as ID 511. Elder orientation beat at the same boundary-carry moment; same reversal-proximity axis invocable (elder positioning for the family's arrival). The 2→2→1 sequence across @511, @512, @159 is a boundary-carry escalation into a scene-open reset. No adjacency violation — the scene-open reset to 1 at @159 is structurally normal. CORRECT (marginal).

---

## AP-SCAN

PASS. No change from cycle 2. No new deny-list violations. Carry-forward flags from cycle 1 unchanged (flags 002–006).

---

## CURVE-SHAPE

FAIL. No change from cycle 2.

The four new tensometer entries do not affect Scenes A, H, or L. None of the new entries fall within those scene ranges (Scenes A: 159–181; H: 266–278; L: 315–324). No rupture, commit, or registration beats have been added to those scenes. The structural failures persist.

Hard shape failures (unchanged from cycle 2):
- **Scene A (159–181):** rise-without-peak. Six 2s (@166, @170, @171, @172, @178, @179), no 3. No transit exception claimed.
- **Scene H (266–278):** rise-without-peak. Three 2s (@274, @275, @505), no 3. No transit exception claimed.
- **Scene L (315–324):** rise-without-peak. Two 2s (@318, @323), no 3. No transit exception claimed.

Episode-level: window climax (eviction cluster, IDs 234/236) is in the middle third. Back half (Scenes H, I, L) remains structurally underloaded relative to front-half climax.

Per URI-026 per-window iteration cap: cycle 2 of 2 is exhausted. Bones regen did not occur. These failures are classified **STRUCTURAL-RESIDUAL**.

---

## FREQUENCY-BAND

FAIL. No change from cycle 2.

Updated distribution including the four new entries (total corpus ~167 entries):
- 3s: 4 / ~167 ≈ 2.4% (target 5–10%) — below floor
- 2s: ~25 / ~167 ≈ 15% (target 20–30%) — below floor
- 1s: ~138 / ~167 ≈ 83% (target 60–75%) — above ceiling

The four added entries (two 1s, two 2s) move no rung into band. The root cause — bones deficit at Scenes A, H, L — is unchanged. This is not a miscalibration fault; scalar inflation is refused. FREQUENCY-BAND failure is load-bearing confirmation of CURVE-SHAPE findings.

Classified **STRUCTURAL-RESIDUAL** per URI-026 cap.

---

## Findings

```yaml
audit:
  scope: season
  target: s01-window-02
  timestamp: 2026-05-11
  findings:
    - id: fault-001
      type: pass
      what: Tensometer coverage fault-001 (cycle 2) — IDs 509, 510 absent
      why: N/A — resolved

    - id: fault-002
      type: pass
      what: Tensometer coverage fault-002 (cycle 2) — IDs 511, 512 orphaned
      why: N/A — resolved

    - id: fault-003
      type: escalate
      what: CURVE-SHAPE — Scenes A (159–181), H (266–278), L (315–324): rise-without-peak. URI-026 per-window iteration cap exhausted at cycle 2. Bones regen did not occur.
      why: Three scenes carry no rupture/commit/registration beat. CURVE-SHAPE and FREQUENCY-BAND both fail on this root cause. Per the orchestrator-critic card, tens-gate-residual HARD findings auto-trigger F7 (FAIL) at Phase 6 — bones-first principle. The window cannot self-correct within the per-window cap.
      criteria: Phase 6 orchestrator-critic must receive this as tens-gate-residual-HARD attribution for Scenes A, H, L and produce a FAIL verdict (F7-bone) unless the human gatekeeper authorizes an out-of-cap regen cycle for Window 2.
```

---

## Combined verdict: MECHANIC-FAIL-CURVE-SHAPE-FREQUENCY-BAND

AP-SCAN: PASS. Coverage faults: RESOLVED.

CURVE-SHAPE and FREQUENCY-BAND: FAIL — STRUCTURAL-RESIDUAL. Root cause: bones deficit at Scenes A, H, L. Per-window iteration cap (URI-026, cycle 2 of 2) exhausted.

**MECHANIC-CLEAN-with-tens-gate-residual is not the applicable verdict.** MECHANIC-CLEAN requires AP-SCAN PASS and no hard shape failures. CURVE-SHAPE fails on three scenes against the locked rubric. The tens-gate-residual designation describes the disposition of those failures (routes to Phase 6 F7-bone), not their severity. The failures are real and unresolved.

**Routing:** tens-gate-residual-HARD (Scenes A, H, L) surfaces at Phase 6 orchestrator-critic as F7-bone. The orchestrator-critic card's failure-mode enumeration applies. Human escalation path is Phase 6 FAIL verdict.
