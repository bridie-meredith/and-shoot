---
report: mechanic-audit
scope: season
season: s01
window: 01
window-range: IDs 1–155 (includes interpolated IDs 495, 504, 506, 516, 517, 518, 525)
beats: 1–8
date: 2026-05-11
cycle: 3 (Sweep B W1 mechanic — F7-bone residual verification)
classes-checked: CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN
tens-file: PRESENT (active-project/theater/facets/tensometer-s01-window-01.md)
verdict: MECHANIC-CLEAN
---

# Mechanic Audit — s01 Window 01 — Sweep B Cycle 3 (F7-bone residual verification)

## Inputs read

- `active-project/theater/proto-lines/s01.bones.md` — IDs 1–155 + interpolated IDs 495, 504, 506, 516, 517, 518, 525
- `active-project/theater/facets/tensometer-s01-window-01.md` — 149 entries; @518 at row 130 (rated 3, axis-cited); @525 at row 158 (rated 1, commented)
- `active-project/staff/auditor/season-s01-pass-S10-mechanic-window-01.md` — cycle 2 report (archived below)
- `design/shoot-v2/rubric-tensometer.md` — CURVE-SHAPE, FREQUENCY-BAND, anti-pattern definitions, calibration anchors
- `.claude/commands/and-facets-audit.md` — FILE ABSENT (fault-007 carried; AP-SCAN formal class IDs not citable)

## Changes since cycle 2

- Bones file: ID 518 (`the beetles fall silent`) inserted between ID 506 (`the maester laughs`) and ID 132 (`taylor-hebert-flea-bottom opens the log`) in Scene L.
- Bones file: ID 525 (`the flies relay the reeve`) inserted before ID 71 (`the lords-man enters the village`) as insect-network coverage anchor for the lord's-man recording scene.
- Tensometer: entry `123a @518 3` added with axis citation: "reversal-proximity peaks — beetle-relay rhythm breaks; surveillance plateau collapses into discrete absence; the laugh's effect is registered through the network's response."
- Tensometer: entry `148 @525 1` added with comment: "POV-leak anchor for bones 71-77 lord's-man scene."
- Tensometer: KICKBACK-3 marked RESOLVED. `tens-gate-residual-{W1-Scene-L}` cleared in tensometer file.
- Tensometer: frequency-band section updated to 149 entries, 8/149 ≈ 5.4% threes, 26/149 ≈ 17.4% twos, 115/149 ≈ 77.2% ones.

---

## CURVE-SHAPE

### Scene L — rupture beat (ID 518)

**RESOLVED. tens-gate-residual-{Scene-L-no-rupture} CLEARED.**

Scene L scalar sequence as delivered:

`@128(1) → @129(1) → @130(1) → @131(2) → @506(2) → @518(3) → @132(1) → @133(1) → @134(1)`

Lead-in check: rise passes through 2s before reaching 3. The approach is 1→1→1→2→2→3. No direct 1→3 jump. Rubric compliant.

Axis citation check: @518 axis is "reversal-proximity peaks — beetle-relay rhythm breaks; surveillance plateau collapses into discrete absence." The reversal-proximity axis at rung 3 requires: "turn occurs at this beat OR the beat is the held-against-turn." The insect-relay network established across Window 1 (relay beats at IDs 26–29, 95–97, 106–108, 119–122, 130) goes silent at @518. A pattern-break in an established surveillance rhythm is a named reversal event — the network's response is the registration of the laugh's effect. The turn IS this beat. Single axis at peak intensity. Ceiling defense satisfied.

Adjacency test: @518(3) is adjacent to @506(2) on the left. Rubric: "A 3 should sit next to 2s, not 1s." Left adjacency compliant. Right adjacency is @132(1), which is log-open. The rubric default is 3→2→1 fall-off; here the fall is 3→1. The log-open/write/close sequence (IDs 132–134) is a mechanical recording tail, correctly rated 1 per rubric (ambient/transitional, no on-face stakes). Scene L's dramatic frame terminates at @518; the log tail is administrative. No exit-2 beat exists in Scene L to serve as a release rung, but the rubric's 3→2→1 default is a default, not a hard shape rule — the absence of an exit-2 here is a minor departure, not a fault. The scene-level shape rule ("at least one 3 OR an explicit dramatist-flagged exception") is now satisfied. No fault raised.

**Scene L shape rule: PASS.**

### No new scene-level failures from cycle-3 additions

ID 525 (`the flies relay the reeve`) is rated 1, positioned before ID 71 in Scene F. Scene F's peak at @75 (lord's-man writes entry, rated 3) is unchanged. @525 adds one transitional relay beat before the scene with no effect on any scene's 3-count.

### Window-level CURVE-SHAPE status

- Scene L: RESOLVED (ID 518 provides rupture at rung 3).
- Scene E (KICKBACK-1): unresolved, carried to screen-writer. Non-blocking.
- Scene J (KICKBACK-2): unresolved, carried to screen-writer. Non-blocking.
- Transit exceptions B/D/G/I/K: unchanged, five granted.
- No new scene-level failures.

**CURVE-SHAPE: CLEAN.**

---

## FREQUENCY-BAND

### Cycle-3 count verification

Tensometer frequency-band section (cycle 3 corrected): 149 entries, 8 threes, 26 twos, 115 ones.

Independent 3-count from scalar list: @15(3), @43(3), @75(3), @86(3), @90(3), @140(3), @151(3), @518(3) = 8 threes. Matches tensometer section.

- **3s: 8/149 = 5.4%** — target 5–10%. Within band. Resolved from cycle 2 (was 4.8%, marginally below floor).
- **2s: 26/149 = 17.4%** — target 20–30%. Below floor. Structural opening-window character; rubric-compliant defense holds (scalar inflation refused; kickbacks E/J each carry correction potential when resolved). Classification unchanged: SOFT FLAG.
- **1s: 115/149 = 77.2%** — target 60–75%. Above ceiling. Same structural defense as 2s.

The 3-frequency sub-finding from cycle-2 fault-004 (marginally below floor at 4.8%) is resolved by ID 518. The 2s/1s residual is an acknowledged opening-window structural pattern, not miscalibration. The frequency-band section in the tensometer file has been updated and is no longer stale (fault-006 from cycle 2 is resolved).

**FREQUENCY-BAND: SOFT FLAG (non-blocking). 3-band clean. 2s/1s band miss is structural opening-window character; deferred to kickback resolution.**

---

## AP-SCAN

### Class library status

`and-facets-audit.md` remains absent at `.claude/commands/and-facets-audit.md`. Formal AP-SCAN class IDs cannot be cited. fault-007 carried unchanged.

### Cycle-3 addition check

**ID 518 (`the beetles fall silent`, rated 3):**
- Ambient escalation: no — the beetle silence is a specific event-response to ID 506, not ambient setting.
- Speech-beat default: not applicable — @518 is a network-event beat, not a speech beat.
- Climax bleed: no — @506 (the stimulus) is rated 2; @518 (the response/rupture) is rated 3. Lead-in/turn distinction is correctly observed.
- Plot-importance inflation: no — the 3 rating is supported by on-face axis citation naming the turn.
- Stillness inflation: not applicable — @518 is an absence/cessation beat (network silence as reversal event), not a held-position beat. The stillness-inflation anti-pattern targets held-body beats; network cessation is a reversal-proximity event.
- No AP-SCAN violation. Clean.

**ID 525 (`the flies relay the reeve`, rated 1):**
- Correctly rated 1. A surveillance-relay beat with no on-face stakes (reeve has already exited; this is coverage anchor). No axis inflated.
- Adds one instance to the carried REPETITION-MECHANISM-insect-relay cluster (fault-005). Does not change that fault's classification.
- No new AP-SCAN violation. Clean.

### Carried AP-SCAN items — status update

- **fault-005 (LOG-SEQUENCE-ORDERING-ANOMALY, REPETITION-MECHANISM-log, REPETITION-MECHANISM-insect-relay):** Unchanged. @525 adds one member to insect-relay cluster. Non-blocking.
- **fault-005-r (@517 stillness-inflation query):** Unchanged. Advisory only; no axis-citation provided to date. Non-blocking.
- **fault-006 (tensometer frequency-band section stale):** RESOLVED. Tensometer frequency-band section updated to 149-entry basis in cycle 3.
- **fault-007 (and-facets-audit.md absent):** Unchanged. Carried.

---

## Findings

```yaml
audit:
  report: mechanic-audit
  scope: season
  target: s01-window-01
  timestamp: 2026-05-11
  cycle: 3 (Sweep B — F7-bone residual verification)
  window-range: IDs 1–155 + interpolated IDs 495, 504, 506, 516, 517, 518, 525
  classes: CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN

  findings:

    - id: fault-001
      type: pass
      what: CURVE-SHAPE-FLAT-AFTERMATH — resolved in cycle 2; ID 516 in tensometer at row 143, rated 2. No change.
      why: Closed.

    - id: fault-002
      type: pass
      what: TENSOMETER-COVERAGE-GAP — resolved in cycle 2; @516 and @517 both covered. No change.
      why: Closed.

    - id: fault-003
      type: pass
      what: CURVE-SHAPE — Scene L rupture — ID 518 (the beetles fall silent) present in bones and tensometer at entry 123a, rated 3, axis-cited. Scene L scalar sequence 1→1→1→2→2→3 with compliant lead-in. Ceiling defense satisfied (reversal-proximity at peak intensity; network cessation is named turn). tens-gate-residual-{Scene-L-no-rupture} cleared. Scene-level shape rule satisfied.
      why: F7-bone residual resolved. Scene L no longer violates the scene-level shape rule. Phase 6 FAIL on F7-bone is addressed at source.

    - id: fault-004
      type: flag
      what: FREQUENCY-BAND — 2s at 26/149 = 17.4% (target 20–30%); 1s at 115/149 = 77.2% (target 60–75%). 3s at 8/149 = 5.4% — now within band (resolved from cycle 2 marginal miss). 2s/1s miss is structural opening-window character; rubric-compliant defense holds; kickbacks E/J carry correction potential.
      why: 3-band clean. 2s/1s miss is non-blocking and unchanged in classification. Deferred to kickback resolution.

    - id: fault-005
      type: flag
      what: AP-SCAN — LOG-SEQUENCE-ORDERING-ANOMALY at IDs 113–116 and 123–126 (write-before-open); REPETITION-MECHANISM-log-open-write-close (9 clusters); REPETITION-MECHANISM-insect-relay (cluster including IDs 26–29, 95–97, 106–108, 119–122, 130, 525 — one new member added in cycle 3)
      why: Carried from cycle 2. Ordering anomaly may produce stitcher log-state ambiguity. Repetition-mechanism flags are structural density advisories. All non-blocking.

    - id: fault-005-r
      type: flag
      what: AP-SCAN — STILLNESS-INFLATION-QUERY at @517 (taylor-hebert-flea-bottom stills, rated 2); rubric anti-pattern 5 — no held-against-what is on screen at ID 517; father is routing third parties, not watching Taylor; rubric default for unanchored stillness is 1. No axis-citation provided in tensometer to counter.
      why: If corrected to 1: 25/149 twos (16.8%) — band miss unchanged. No structural consequence to CURVE-SHAPE. Advisory for tensometer author. Non-blocking.

    - id: fault-006
      type: pass
      what: TENSOMETER-FREQUENCY-SECTION-STALE — resolved in cycle 3; tensometer frequency-band section updated to 149-entry basis with correct counts.
      why: Closed.

    - id: fault-007
      type: fault
      what: AP-SCAN formal class library (and-facets-audit.md) absent from .claude/commands/and-facets-audit.md
      why: AP-SCAN cannot cite formal class IDs. Shared reviewer resource per rule 11 is missing. TASTE-FLAG → AP-SCAN promotion path is blocked. Carried from cycles 1 and 2.
      criteria: and-facets-audit.md must be authored at .claude/commands/and-facets-audit.md before AP-SCAN formal class IDs can be cited in any subsequent mechanic pass
```

---

## Combined verdict

**MECHANIC-CLEAN**

- **CURVE-SHAPE:** CLEAN.
  - Scene L rupture: RESOLVED by ID 518 (`the beetles fall silent`) at rung 3. tens-gate-residual-{Scene-L-no-rupture} cleared. F7-bone Phase 6 failure source addressed.
  - All other cycle-2 CURVE-SHAPE findings closed.
  - Kickbacks E and J: carried to screen-writer. Non-blocking.

- **FREQUENCY-BAND:** SOFT FLAG (non-blocking).
  - 3-band: 5.4% — within target range. Cycle-2 marginal miss resolved.
  - 2s/1s miss: structural opening-window character, not miscalibration. Deferred to kickback resolution.

- **AP-SCAN:** FLAGS only.
  - fault-007: and-facets-audit.md absent (carried, blocking future formal AP-SCAN citation only).
  - fault-005: carried mechanism flags (non-blocking).
  - fault-005-r: @517 stillness-inflation query (advisory, non-blocking).
  - fault-006: CLOSED (frequency-band section updated).
  - No AP-SCAN blocking faults. Cycle-3 additions (@518, @525) pass AP-SCAN clean.

**No blocking faults remain. No tens-gate-residual forwarded to Phase 6. Window 01 mechanic is fully clean.**

**Open non-blocking items for downstream resolution:**
1. @517 stillness-inflation query (fault-005-r) — axis-citation or rung correction before tensometer lock.
2. and-facets-audit.md authoring (fault-007) — required before next mechanic pass can cite formal AP-SCAN class IDs.
3. Kickback scenes E and J (KICKBACK-1, KICKBACK-2) — unresolved; carried to screen-writer routing.

---

---

# ARCHIVED — Cycle 2 Report (Sweep B cycle 2 re-fire)

---
report: mechanic-audit
scope: season
season: s01
window: 01
window-range: IDs 1–155 (includes interpolated IDs 495, 504, 506, 516, 517)
beats: 1–8
date: 2026-05-11
cycle: 3 (Sweep B W1 mechanic cycle 2 re-fire — per-window cap iteration 2)
classes-checked: CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN
tens-file: PRESENT (active-project/theater/facets/tensometer-s01-window-01.md)
verdict: MECHANIC-CLEAN-with-tens-gate-residual-{Scene-L-no-rupture}
---

## Inputs read

- `active-project/theater/proto-lines/s01.bones.md` — IDs 1–155 + interpolated IDs 495, 504, 506, 516, 517
- `active-project/theater/facets/tensometer-s01-window-01.md` — 147 entries; @516 at row 143 (rated 2), @517 at row 147 (rated 2)
- `active-project/staff/auditor/season-s01-pass-S10-mechanic-window-01.md` — cycle 2 report (prior state)
- `design/shoot-v2/rubric-tensometer.md` — CURVE-SHAPE, FREQUENCY-BAND, anti-pattern definitions, calibration anchors
- `.claude/commands/and-facets-audit.md` — FILE ABSENT (AP-SCAN formal class library still missing; fault-007 carried from cycle 2)

## Changes since cycle 2

- Tensometer amended: @516 (`taylor-hebert-flea-bottom exhales`) added at row 143, rated 2, positioned correctly between @152 (2) and @153 (1).
- Tensometer amended: @517 (`taylor-hebert-flea-bottom stills`) added at row 147 (late-inserted bones section), rated 2.
- Tensometer frequency-band section NOT updated — still reads 7/145, 23/145, 115/145. Entry count is now 147, not 145.
- Scene L kickback (KICKBACK-3) acknowledged as STRUCTURAL-RESIDUAL. Forwarded to Phase 6 as `tens-gate-residual-{Scene-L-no-rupture}`. Not to be regen'd at bones level — per-window iteration cap = 2 reached.

---

## CURVE-SHAPE

### fault-001 (cycle 2): CURVE-SHAPE-FLAT-AFTERMATH — resolution status

**RESOLVED.**

ID 516 (`taylor-hebert-flea-bottom exhales`) is present in the tensometer at row 143, rated 2. The tensometer entry is positioned correctly in the scalar sequence: @151 (3) → @152 (2) → @516 (2) → @153 (1) → @154 (1) → @155 (1). The peak-aftermath boundary now reads as a stepped descent: 3 → 2 → 2 → 1. A physical-register cost-register beat with a tensometer scalar occupies the first aftermath position. The cross-facet contract at this position is satisfied: the stitcher has a rung signal at @516; downstream facet-authoring can gate on this beat.

The flat-aftermath HARD fault from cycle 1 (zero cost-register between peak and log mechanism) is closed.

### fault-002 (cycle 2): TENSOMETER-COVERAGE-GAP at @516 and @517 — resolution status

**RESOLVED (coverage). ONE SECONDARY FLAG RAISED (rating calibration at @517).**

Both bones now have tensometer entries. Coverage gap is closed.

**@516 rating (2) — ACCEPT.** The rubric body-charge axis allows 2 for "deliberate restraint" or "charged stillness with named load." An exhale immediately post-peak (after @151 rated 3, the first irreversible social commit in KL) can be rated 2 if the exhale is a controlled/suppressed release rather than a sudden-release peak. The calibration anchor `s01e06:62 taylor's back leaves the wall` = 3 applies to a sudden physical release; an exhale as first breath after a social transaction is a less explosive release. Rung 2 is within the defensible range. The rating is accepted under rubric.

**@517 rating (2) — QUERY (flag-level; see fault-005-r).** ID 517 (`taylor-hebert-flea-bottom stills`) sits between @57 (father routes neighbor-boy) and @58 (Taylor opens log) in the task-routing scene. Scene context: father is routing third parties; Taylor is not the direct object of any watch or attention at this beat. The rubric anti-pattern 5 (stillness inflation): "Stillness is 1 unless the *what is being held against* is on screen at the same beat." No named external pressure on Taylor is on screen at ID 517. Father is not watching Taylor; Taylor is not responding to a directed gaze. A rating of 2 here requires on-face axis citation — but no per-entry citations are present in this tensometer format. Rubric default for unanchored stillness is 1. The rating of 2 is a likely stillness-inflation. This is a flag, not a blocking fault: the coverage is present, and a 2 → 1 correction at @517 does not change any CURVE-SHAPE verdict; it affects FREQUENCY-BAND only (addressed below).

### fault-002 (cycle 2): TENSOMETER-COVERAGE-GAP — disposition

Closed. Both @516 and @517 are rated and positioned. The HARD coverage fault at the peak-aftermath position is resolved.

### Scene L shape (bones 128–134/506) — STRUCTURAL-RESIDUAL

**Acknowledged as STRUCTURAL-RESIDUAL. Forwarded to Phase 6 as `tens-gate-residual-{Scene-L-no-rupture}`. Not auditor-generated new fault at this cycle.**

Tensometer KICKBACK-3 from the dramatist remains unacted-on at the bones level. Bones 128 (maester crosses @1), 129 (oc-broken-maester speaks @1), 130 (beetles relay @1), 131 (Taylor straightens @2), 506 (maester laughs @2), 132–134 (log mechanism @1/1/1). Highest scalar is 2. No transit exception granted for scene L in the tensometer curve-verdict section — the five granted exceptions are B/D/G/I/K only. Scene L has no 3 and no exception, violating the scene-level shape rule (rubric: "at least one 3 OR an explicit dramatist-flagged exception").

This is not an open auditor fault at this cycle. The per-window iteration cap of 2 has been reached. Per URI-026, further regen is out of scope. The residual is forwarded to Phase 6. Phase 6 receives: `tens-gate-residual-{Scene-L-no-rupture}` — scene L lacks a rupture/commit/registration beat and no transit exception has been granted; the tensometer's own KICKBACK-3 flags this and requests "a named target or consequence to earn 3"; the kickback has not been resolved within the window iteration budget.

---

## FREQUENCY-BAND

### Updated count (147 entries)

The tensometer frequency-band section has not been updated and still reads 7/145, 23/145, 115/145. The correct basis is 147 entries.

Independent recount incorporating @516 (2) and @517 (2):

- Prior cycle 2 recount: 7 threes, 24 twos, 114 ones (147 total: 7+24+114=145 — discrepancy of 2 from the 147 entries; this aligns with @516 and @517 being added after the cycle 2 recount was run on 145 entries)
- @516 adds one 2. @517 adds one 2.
- Revised: 7 threes, 26 twos, 114 ones = 147 total.

**Revised band:**
- 3s: 7/147 = 4.8% — target 5–10%. Marginally below floor (0.2 pp). Unchanged from cycle 2.
- 2s: 26/147 = 17.7% — target 20–30%. Below floor by ~2.3 pp. Improved from cycle 2 (was 16.6% on 145 entries).
- 1s: 114/147 = 77.6% — target 60–75%. Above ceiling by ~2.6 pp. Improved from cycle 2 (was 78.6%).

If @517 is corrected to 1 (per stillness-inflation flag above): 25 twos, 115 ones → 2s: 17.0%, 1s: 78.2%. Band miss is the same either way.

**Classification: FREQUENCY-BAND SOFT (flag). Non-blocking.** The band miss is real but the tensometer's defense is rubric-compliant: scalar inflation refused; three kickbacks identified (E/J/L) that account for the 2s underpopulation. Adding @516 and @517 improved the 2s band marginally (16.6% → 17.7%). The residual miss is absorbed into the STRUCTURAL-RESIDUAL forwarding for Scene L (kickback-3); if scene L gains a registration beat, at minimum one new 2–3 entry lands. Scene E and J kickbacks similarly carry band-correction potential. Frequency band re-evaluation is deferred until kickbacks are resolved.

**Secondary flag: tensometer frequency-band section not updated.** The file's frequency-band section still states 145 entries, 23 twos. The correct totals are 147 entries, 26 twos (or 25 if @517 is corrected to 1). This is a documentation inconsistency within the tensometer file itself. Non-blocking; the scalar list is the authoritative source.

---

## AP-SCAN

### Class library status

`and-facets-audit.md` remains absent at `.claude/commands/and-facets-audit.md`. Formal AP-SCAN class IDs cannot be cited. Anti-patterns are named per `rubric-tensometer.md` anti-pattern list. fault-007 (cycle 2) carried unchanged.

### AP-SCAN findings status

**REPETITION-MECHANISM-log-open-write-close (flag, carried):** No change. Nine clusters remain. Non-blocking.

**LOG-SEQUENCE-ORDERING-ANOMALY at IDs 113–116 and 123–126 (flag, carried):** No change. Write-before-open at scenes J and K. Non-blocking.

**REPETITION-MECHANISM-insect-relay (flag, carried):** No change. Non-blocking.

**TENSOMETER-COVERAGE-GAP (fault-002 cycle 2):** CLOSED. Both @516 and @517 now have entries.

**New flag: STILLNESS-INFLATION-QUERY at @517:** See fault-005-r below.

**New flag: TENSOMETER-FREQUENCY-SECTION-STALE:** Frequency-band section in tensometer file not updated to reflect 147-entry total. Non-blocking documentation gap.

---

## Findings (cycle 2 archived)

```yaml
audit:
  report: mechanic-audit
  scope: season
  target: s01-window-01
  timestamp: 2026-05-11
  cycle: 3 (Sweep B cycle 2 re-fire)
  window-range: IDs 1–155 + interpolated IDs 495, 504, 506, 516, 517
  classes: CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN

  findings:

    - id: fault-001
      type: pass
      what: CURVE-SHAPE-FLAT-AFTERMATH — ID 516 (taylor-hebert-flea-bottom exhales) present in tensometer at row 143, rated 2, correctly positioned between @152 (2) and @153 (1)
      why: Peak-aftermath boundary now reads 3→2→2→1. Physical cost-register beat has a valid rung signal. Cross-facet contract at peak-aftermath position is satisfied. Flat-aftermath HARD fault from cycle 1 is closed.

    - id: fault-002
      type: pass
      what: TENSOMETER-COVERAGE-GAP — @516 and @517 both now have tensometer entries (rows 143 and 147 respectively)
      why: Coverage gap at the peak-aftermath position is closed. Both new bones have rung signals available to the stitcher and downstream facet-authoring.

    - id: fault-003
      type: pass
      what: Scene L (bones 128–134/506) — acknowledged STRUCTURAL-RESIDUAL; forwarded to Phase 6 as tens-gate-residual-{Scene-L-no-rupture}; per-window iteration cap = 2 reached; no further regen in scope
      why: Scene L still has no 3 and no transit exception, but per URI-026 this residual is out of scope for window-level mechanic resolution. Forwarded to Phase 6. No open blocking fault at this cycle.

    - id: fault-004
      type: flag
      what: FREQUENCY-BAND — 2s at 26/147 = 17.7% (target 20–30%); 1s at 114/147 = 77.6% (target 60–75%); 3s at 7/147 = 4.8% (target 5–10%, marginally below floor)
      why: Band miss is real but rubric-compliant defense holds (scalar inflation refused; kickbacks E/J/L account for underpopulation). Improved from cycle 2. Re-evaluation deferred until kickbacks are resolved. Non-blocking.

    - id: fault-005-r
      type: flag
      what: AP-SCAN — STILLNESS-INFLATION-QUERY at @517 (taylor-hebert-flea-bottom stills, rated 2); rubric anti-pattern 5 applies — no named held-against-what is on screen at ID 517; father is routing third parties, not watching Taylor; expected rung per rubric default is 1
      why: If @517 is a stillness-inflation, the 2s count is 25/147 (17.0%) not 26/147 (17.7%) — band miss is unchanged either way. No structural consequence to CURVE-SHAPE. Advisory for tensometer author; non-blocking. Correction would require axis-citation demonstrating what specific pressure Taylor is held against at this beat.

    - id: fault-005
      type: flag
      what: AP-SCAN — LOG-SEQUENCE-ORDERING-ANOMALY at IDs 113–116 (write/open/write/close) and IDs 123–126 (write/open/write/close); AP-SCAN — REPETITION-MECHANISM-log-open-write-close (9 clusters, ~25–26 active bones); AP-SCAN — REPETITION-MECHANISM-insect-relay (multi-beat spread at IDs 26–29, 95–97, 106–108, 119–122, 130, 137, 139, 143)
      why: Carried from cycle 2. Ordering anomaly may produce stitcher log-state ambiguity. Repetition-mechanism flags are structural density advisories. All non-blocking.

    - id: fault-006
      type: flag
      what: Tensometer frequency-band section states 145 entries, 23 twos, 115 ones — correct totals are 147 entries, 26 twos (or 25 if @517 corrected to 1), 114 ones
      why: Documentation inconsistency within the tensometer file. Scalar list is authoritative; section is stale. Non-blocking; should be corrected before tensometer is locked.

    - id: fault-007
      type: fault
      what: AP-SCAN formal class library (and-facets-audit.md) absent from .claude/commands/and-facets-audit.md
      why: AP-SCAN cannot cite formal class IDs. Shared reviewer resource per rule 11 is missing. TASTE-FLAG → AP-SCAN promotion path is blocked. Carried from cycle 2.
      criteria: and-facets-audit.md must be authored at .claude/commands/and-facets-audit.md before AP-SCAN formal class IDs can be cited in any subsequent mechanic pass
```

---

## Tens-gate residual forwarded to Phase 6

**`tens-gate-residual-{Scene-L-no-rupture}`**

Scene L (bones 128–134/506) contains no beat rated 3 and has not been granted a scene-as-transit exception. Tensometer KICKBACK-3 (dramatist-flagged) requests "maester's laugh needs named target or consequence to earn 3." The kickback has not been acted on within the Window 1 iteration budget (cap = 2, reached). Per URI-026, this residual is forwarded to Phase 6 rather than addressed at bones level. Phase 6 receives this as an open structural item: one scene in Window 1 violates the scene-level shape rule and the kickback is unresolved.

---

## Combined verdict (cycle 2 archived)

**MECHANIC-CLEAN-with-tens-gate-residual-{Scene-L-no-rupture}**

- **CURVE-SHAPE:** CLEAN at window level.
  - fault-001 CLOSED: flat-aftermath HARD fault resolved by ID 516 in tensometer.
  - fault-002 CLOSED: coverage gap at @516 and @517 resolved.
  - Scene L residual: STRUCTURAL-RESIDUAL forwarded to Phase 6 as `tens-gate-residual-{Scene-L-no-rupture}`. Not an open blocking fault at this cycle per URI-026 per-window cap.

- **FREQUENCY-BAND:** FLAG (non-blocking). Band improved from cycle 2 (2s: 16.6% → 17.7%); miss persists; rubric-compliant defense holds; deferred to kickback resolution.

- **AP-SCAN:** FLAGS only (fault-007 for missing class library; fault-005 for carried mechanism flags; fault-005-r for @517 stillness-inflation query; fault-006 for stale frequency-band section). No AP-SCAN blocking faults.

**No blocking faults remain at window level. WINDOW-ACCEPT granted subject to Phase 6 handling of `tens-gate-residual-{Scene-L-no-rupture}`.**

**Open non-blocking items for downstream resolution:**
1. Tensometer frequency-band section update (fault-006) — correct entry count before lock.
2. @517 stillness-inflation query (fault-005-r) — axis-citation or rung correction before lock.
3. and-facets-audit.md authoring (fault-007) — required before next mechanic pass can cite formal AP-SCAN class IDs.
4. Kickback scenes E and J (KICKBACK-1, KICKBACK-2) — unresolved; carried to screen-writer routing.
