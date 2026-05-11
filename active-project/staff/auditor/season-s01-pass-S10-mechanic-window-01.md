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

# Mechanic Audit — s01 Window 01 — Sweep B Cycle 2 Re-fire

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

## Findings

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

## Combined verdict

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
