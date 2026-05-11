---
report: mechanic-audit
scope: season
season: s01
window: 01
window-range: IDs 1–155 (includes interpolated IDs 495, 504, 506, 516, 517)
beats: 1–8
date: 2026-05-11
cycle: 2
classes-checked: CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN
tens-file: PRESENT (active-project/theater/facets/tensometer-s01-window-01.md)
verdict: MECHANIC-FAIL-CURVE-SHAPE
---

# Mechanic Audit — s01 Window 01 — Cycle 2

## Inputs read

- `active-project/theater/proto-lines/s01.bones.md` — IDs 1–155 + interpolated IDs 495, 504, 506, 516, 517
- `active-project/theater/facets/tensometer-s01-window-01.md` — 145 entries, covers @1–@155 + @495, @504, @506; IDs 516 and 517 absent
- `active-project/staff/auditor/season-s01-pass-S10-cut-proposal.md` — window shape description
- `design/shoot-v2/rubric-tensometer.md` — CURVE-SHAPE, FREQUENCY-BAND, and anti-pattern definitions
- `.claude/commands/and-season.md` — mechanic brief
- `.claude/commands/and-facets-audit.md` — FILE ABSENT (AP-SCAN formal class library still missing; cycle 1 fault-003 partially resolved)

## Changes from cycle 1

- ID 516 (`taylor-hebert-flea-bottom exhales`) added between ID 152 and ID 153 — physical cost-register bone targeting flat-aftermath fault (fault-001 cycle 1)
- ID 517 (`taylor-hebert-flea-bottom stills`) added in scene 4 (task-routing scene, between ID 57 and ID 58)
- Bone 109 deleted (orphan log-write)
- Tensometer file now present — FREQUENCY-BAND check can run
- `and-facets-audit.md` remains absent — AP-SCAN formal class IDs still unavailable

---

## CURVE-SHAPE

### Window peak and aftermath sequence (revised)

The amended bone sequence at the peak / aftermath boundary is:

```
148  oc-tanner-elder speaks to taylor-hebert-flea-bottom
149  taylor-hebert-flea-bottom faces oc-dock-runner
150  oc-dock-runner speaks to taylor-hebert-flea-bottom
151  taylor-hebert-flea-bottom speaks to oc-dock-runner   ← 3 in tensometer
152  oc-dock-runner exits the junction                    ← 2 in tensometer
516  taylor-hebert-flea-bottom exhales                   ← NO tensometer entry
153  taylor-hebert-flea-bottom opens the log             ← 1 in tensometer
154  taylor-hebert-flea-bottom writes the entry          ← 1 in tensometer
155  taylor-hebert-flea-bottom closes the log            ← 1 in tensometer
```

### CURVE-SHAPE verdict on fault-001

**PARTIALLY RESOLVED — residual fault remains.**

ID 516 (`taylor-hebert-flea-bottom exhales`) is a physical-register aftermath bone. An exhale immediately following a transactional exchange at the window's structural peak carries body-charge (release after held tension) and cost-register (breath cost of first irreversible social commit in KL). As a single bone it is the minimum viable aftermath insert: it marks transaction close at the body level before the log-mechanism opens.

The structural problem from cycle 1 — zero cost-register, zero aftermath-texture between the peak and the log — is addressed. The transition is no longer a direct peak→mechanism drop.

**Residual issue: ID 516 is unrated in the tensometer.** The tensometer file covers IDs 1–155 including @495, @504, @506 but does not include an entry for @516 or @517. ID 516 is an active bone in the window (it appears in the bones file between IDs 152 and 153) and sits at the most load-bearing position in the window — the first aftermath beat following the structural peak. A tensometer that does not carry a scalar for this bone cannot fulfill its cross-facet contract at this position. The stitcher cannot gate on ID 516's charge; the downstream facet-authoring pass has no rung signal for the bone.

**Tensometer coverage gap for ID 516 is a fault, not a flag.** The bone is not an interpolation of a pre-existing beat — it is a new structural bone inserted precisely to carry aftermath charge. Its absence from the tensometer is not a minor omission: the peak-to-aftermath transition is the window's most structurally sensitive zone, and the downstream facets depend on this rung signal.

Expected rung for ID 516 (`taylor-hebert-flea-bottom exhales` immediately post-peak): rubric body-charge axis — "sudden release after held charge" = 3, OR body invested against perceived cost = 2. Given adjacency (immediately follows @152 rated 2; @151 rated 3), the exhale is the release beat. Rubric: `taylor's back leaves the wall` = 3. An exhale as release after a transactional peak aligns with that anchor. Expected rating: 2 or 3. Missing.

**ID 517 is also unrated.** `taylor-hebert-flea-bottom stills` in the task-routing scene (between IDs 57 and 58) — a stillness beat. Per rubric, stillness-inflation is a named anti-pattern; default is 1 unless "held-against-what" is on screen. Context: ID 57 (father routes neighbor-boy) then 517 (Taylor stills) then 58 (Taylor opens log). The stilling here is adjacent to the father's routing pattern. Rubric: stillness is 1 unless the scene-frame names what is being held against. Given scene context (father routing, not watching Taylor; no named pressure), expected rating is 1. But the tensometer has no entry — it cannot be verified and the stitcher cannot process it.

**Classification of outstanding CURVE-SHAPE status:** The flat-aftermath HARD fault (fault-001 cycle 1) is functionally resolved at the bone level — ID 516 is the required physical-register aftermath bone. However, the tensometer does not cover ID 516, making the curve as rated still technically incomplete at the peak-aftermath boundary. This is not a new SHAPE-COHERENT-FLAT-AFTERMATH fault (the bone exists); it is a tensometer-coverage fault at the most sensitive structural position.

### Scene L shape (bones 128–134/506)

Tensometer self-reports KICKBACK-3: scene L peaks at 2, no rupture. Bone 506 (maester laughs) is rated 2. No 3 in scene. The scene has a structural gap (no rupture/commit/registration beat for a scene that contains a named observation by a character of institutional significance). This is a carried issue from the tensometer's own kickback notation — not newly introduced in cycle 2, but still unresolved.

Classification: KICKBACK-3 from tensometer is an outstanding screen-writer kickback. Not an auditor-generated new fault; it is noted as an open structural issue reported by the dramatist's own curve-shape pass. Auditor concurs with the dramatist's structural read: scene L's highest bone is @506 rated 2 (maester laughs), and no commit bone exists. This scene does not satisfy the scene-level shape rule (at least one 3 or explicit dramatist-flagged exception). The scene-as-transit exception has not been granted for scene L in the tensometer file — "five scene-as-transit exceptions granted (B/D/G/I/K)" is stated, and L is not among them.

This is a SHAPE-COHERENT scene-level failure (no peak in scene L; maester observation scene has no registration beat). Per rubric, the response is a screen-writer kickback, which the tensometer already flags. Auditor escalates this to a fault for the mechanic report since the kickback routing has not yet been acted on.

---

## FREQUENCY-BAND

Tensometer file is present. Scalar distribution per the file's own frequency-band section: 3s 7/145 = 4.8%, 2s 23/145 = 15.9%, 1s 115/145 = 79.3%.

Independent recount from the tensometer scalar list:
- 3s: @15, @43, @75, @86, @90, @140, @151 = 7
- 2s: @7, @11, @13, @14, @42, @66, @74, @76, @504, @87, @89, @111, @112, @113, @131, @506, @138, @139, @141, @142, @148, @149, @150, @152 = 24
- 1s: 145 - 7 - 24 = 114

Recount yields 24 twos (file states 23 — one-entry discrepancy, likely @141 which the file may have counted differently). Either way the band result is the same.

**Band result:**
- 3s: 7/145 = 4.8% — target 5–10%. Marginally below floor (0.2 percentage points).
- 2s: 24/145 = 16.6% — target 20–30%. Below floor by ~3.4 percentage points.
- 1s: 114/145 = 78.6% — target 60–75%. Above ceiling by ~3.6 percentage points.

The tensometer's own explanation: "Misses are real but reflect structurally appropriate low-charge establishing material. Window 1 is opening; village-domestic + KL-arrival scenes are inherently low-charge. Scalar inflation refused."

**Auditor assessment:** The rubric states "outside that band, investigate: too few 3s = flatness OR a structurally-underloaded episode." The 2s band miss is the more significant of the two. A 2s band at 16.6% against a 20–30% target indicates the gradient between 1 and 3 is underpopulated — the stitcher will have a coarser density signal than designed.

However: the tensometer's defense is valid under the rubric. The rubric explicitly states the dramatist's response to a failing curve is not to retune scalars but to flag kickbacks. The tensometer flags three kickbacks (scenes E, J, L) which, if resolved, would add registration beats and likely add 2–3 entries — bringing the band closer to target. The 2s underpopulation is structurally explained by the kickback scenes.

**Classification:** FREQUENCY-BAND SOFT. The band is outside target, but the tensometer's defense (scalar inflation refused; kickback routing identified) is rubric-compliant. This is a flag, not a HARD fault. The kickback scenes (E, J, L) must be resolved before FREQUENCY-BAND can be re-evaluated in a clean pass.

**Note on coverage gap:** IDs 516 and 517 are absent from the tensometer. Adding them would bring the total to 147 entries. If 516 is rated 2 or 3 (expected) and 517 is rated 1 (expected), the 2s count would be 25/147 = 17.0% — still below floor, but the coverage gap makes the exact band result unverifiable at this position.

---

## AP-SCAN

### Class library status

`and-facets-audit.md` remains absent at `.claude/commands/and-facets-audit.md`. Formal AP-SCAN class IDs cannot be cited. Anti-patterns are named per `rubric-tensometer.md` anti-pattern list.

### AP-SCAN findings (carried from cycle 1, re-evaluated)

**REPETITION-MECHANISM-log-open-write-close (flag, carried):**

Log mechanism clusters after cycle 2 modifications: bone 109 deleted (orphan log-write removed). The ID 109 (write only, embedded in perimeter scene) from cycle 1's cluster list is now removed. Remaining clusters:
- IDs 21–23
- IDs 32–34
- IDs 58–60
- IDs 79–81
- IDs 101–103
- IDs 113–116 (write + open + write + close — note: these IDs appear disordered; the log-open at 114 follows the log-write at 113, then another write at 115, close at 116 — this sequence is structurally irregular within the log-mechanism convention and merits a bone-sequence review)
- IDs 123–126 (write + open + write + close — same ordering anomaly: 123 write, 124 open, 125 write, 126 close)
- IDs 132–134 (open / write / close)
- IDs 153–155 (open / write / close)

Nine clusters remain. The deletion of bone 109 removed one orphan; it does not change the density assessment substantially. Log-mechanism bones still account for approximately 25–26 active bones across the window.

The tensometer correctly rates all log-mechanism bones as 1 (log-open @101=1, @103=1, @107=1, @114=1, @116=1, @124=1, @126=1, @132=1, @134=1, @153=1, @154=1, @155=1). No ambient escalation detected at log-mechanism beats. AP-SCAN flag is not a misrating complaint — the log-mechanism bones are correctly rated. The flag is a structural density advisory only.

**Ordering anomaly at IDs 113–126:** Scenes J and K show log-mechanism sequences where write precedes open (ID 113 write, ID 114 open; ID 123 write, ID 124 open). This is either a bone-ordering error or a deliberate representation of Taylor recording mid-sweep before formally opening/closing the log. Either way, the sequence does not conform to the standard open→write→close convention and could create stitcher ambiguity. Flag for fixer or screen-writer review.

**Classification:** AP-SCAN flag — REPETITION-MECHANISM-log-open-write-close, plus LOG-SEQUENCE-ORDERING-ANOMALY at IDs 113–116 and 123–126. Non-blocking.

**REPETITION-MECHANISM-insect-relay (flag, carried):**

No change from cycle 1. Bone 109 deletion removed one insect relay from scene J (ID 109 was the spider relay; the file now shows IDs 105–108, 110 in scene J with beetles/flies/spiders at 106–108, then 110 continuing perimeter). The insect-relay density is minimally reduced. Flag carried as non-blocking.

**TENSOMETER-COVERAGE-GAP-interpolated-bones (new):**

IDs 516 and 517 are active bones in the s01 bones file with no tensometer entries. Coverage gap is established. ID 516 sits at the most structurally sensitive position in the window (first aftermath beat post-peak). ID 517 sits in a procedural scene (task-routing) at a stillness beat. Both are unrated.

**Classification:** AP-SCAN fault — TENSOMETER-COVERAGE-GAP at IDs 516 and 517. HARD at ID 516 (peak aftermath position); SOFT at ID 517 (expected rung: 1; low structural consequence).

---

## Findings

```yaml
audit:
  report: mechanic-audit
  scope: season
  target: s01-window-01
  timestamp: 2026-05-11
  cycle: 2
  window-range: IDs 1–155 + interpolated IDs 495, 504, 506, 516, 517
  classes: CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN
  findings:

    - id: fault-001
      type: pass
      what: ID 516 (taylor-hebert-flea-bottom exhales) inserted between ID 152 and ID 153
      why: Physical-register aftermath bone resolves the cycle-1 SHAPE-COHERENT-FLAT-AFTERMATH HARD. The transition from peak (IDs 148–152) to log mechanism (IDs 153–155) now includes a body-charge release beat. Zero-aftermath gap is closed at the bone level.

    - id: fault-002
      type: fault
      what: ID 516 absent from tensometer (tensometer covers @1–@155 + @495, @504, @506; no entry for @516 or @517)
      why: ID 516 is the window's peak-aftermath beat and sits at the most structurally sensitive position in Window 1. Absent tensometer scalar means the stitcher has no rung signal at this position; downstream facet-authoring cannot gate on charge at the peak-aftermath transition. The cross-facet contract (§"Cross-facet contract" in rubric-tensometer.md) is broken at the position where it matters most. ID 517 is also absent; expected rung is 1 (stillness beat in procedural context, no named held-against), structural consequence low but coverage must be complete.
      criteria: tensometer must be amended to include entries for @516 and @517; @516 expected rung 2 or 3 per body-charge axis (release after held-charge peak); @517 expected rung 1 unless scene-frame names a specific held-against pressure; after amendment, FREQUENCY-BAND must re-run on the revised 147-entry total

    - id: fault-003
      type: fault
      what: Scene L (bones 128–134 / 506) — no 3 in scene, scene-as-transit exception not granted; highest rated bone is @506 (maester laughs) at 2
      why: Rubric scene-level shape rule: every scene must contain at least one 3 OR carry an explicit dramatist-flagged scene-as-transit exception. Scene L is not among the five transit exceptions (B/D/G/I/K). The maester observation scene has no registration beat — bones 128 (maester crosses), 129 (maester speaks), 506 (maester laughs), 131 (Taylor straightens spine) — the highest-charge moment is Taylor's spinal adjustment (131 rated 2). No commit, no rupture, no irreversible registration in the scene. The tensometer's own KICKBACK-3 notation flags this and asks screen-writer for "a named target or consequence" to earn the 3. The kickback has not yet been acted on.
      criteria: either (a) screen-writer adds a registration beat to scene L (maester's laugh produces a specific named consequence or directed observation that commits or registers irreversibly — earning a 3 at that bone); or (b) dramatist formally grants scene-as-transit exception to scene L in the tensometer curve-verdict section, with justification; the current state (no 3, no exception) violates the scene-level shape rule

    - id: fault-004
      type: flag
      what: FREQUENCY-BAND — 2s at 24/145 = 16.6% (target 20–30%); 1s at 78.6% (target 60–75%); 3s at 4.8% (target 5–10%; marginally below floor)
      why: Band miss reflects genuine gradient underpopulation in the 2-rung. Stitcher density signal is coarser than designed. Tensometer's defense (inflation refused; three kickbacks identified) is rubric-compliant. Band cannot be definitively re-evaluated until (a) tensometer entries for IDs 516/517 are added, (b) kickback scenes E/J/L are resolved, and (c) any resulting new bones are rated. This flag is advisory pending those resolutions. Does not independently block WINDOW-ACCEPT.

    - id: fault-005
      type: flag
      what: AP-SCAN — LOG-SEQUENCE-ORDERING-ANOMALY at IDs 113–116 (write/open/write/close) and IDs 123–126 (write/open/write/close); write precedes open in both clusters
      why: Standard log-mechanism convention is open→write→close. These clusters invert the sequence, either indicating a bone-ordering error or an intentional mid-sweep entry before formal log-open. Either way, stitcher will encounter an ambiguous log-state at these bones. Advisory for fixer or screen-writer; non-blocking.

    - id: fault-006
      type: flag
      what: AP-SCAN — REPETITION-MECHANISM-log-open-write-close (9 clusters remaining after bone 109 deletion, ~25–26 active bones) and REPETITION-MECHANISM-insect-relay (multi-beat spread at IDs 26–29, 95–97, 106–108, 119–122, 130, 137, 139, 143)
      why: Carried from cycle 1. Rhythm-lock risk and stitcher compression advisory. Tensometer correctly rates all log-mechanism and standard insect-relay bones at 1 — no ambient escalation detected. Non-blocking.

    - id: fault-007
      type: fault
      what: AP-SCAN formal class library (and-facets-audit.md) absent from .claude/commands/and-facets-audit.md
      why: AP-SCAN cannot cite formal class IDs. Anti-patterns are named per rubric-tensometer.md only. Shared reviewer resource (per rule 11 in CLAUDE.md) is missing — any AP-SCAN findings that should graduate from TASTE-FLAG to AP-SCAN promotion path cannot be processed. Carried from cycle 1 fault-003 (partial: tensometer now present; class library still absent).
      criteria: and-facets-audit.md must be authored at .claude/commands/and-facets-audit.md before AP-SCAN formal class IDs can be cited in any subsequent mechanic pass
```

---

## Combined verdict

**MECHANIC-FAIL-CURVE-SHAPE**

- **CURVE-SHAPE:** FAIL
  - fault-001 RESOLVED: flat-aftermath fault cleared by ID 516 at bone level
  - fault-003 OPEN: scene L has no 3 and no transit exception — scene-level shape rule violated; tensometer KICKBACK-3 unresolved
  - fault-002 OPEN: tensometer coverage gap at ID 516 (HARD — peak-aftermath position) and ID 517 (SOFT)

- **FREQUENCY-BAND:** FLAG (non-blocking pending kickback resolutions and tensometer coverage completion)

- **AP-SCAN:** FLAG (fault-005 log-sequence ordering anomaly; fault-006 repetition mechanism density; fault-007 class library absent — all non-blocking)

**Primary block:** Tensometer coverage gap at ID 516 (fault-002, HARD) and scene L shape failure (fault-003, HARD). Both must resolve before WINDOW-ACCEPT can be reached.

**Routing:** WINDOW-REVISE. Two actions required:
1. Tensometer amended to add @516 and @517 entries — then FREQUENCY-BAND re-evaluated on 147-entry distribution.
2. Scene L resolved via screen-writer registration-beat addition or explicit scene-as-transit exception grant from dramatist.

Mechanic re-fire (cycle 3) required after both resolutions.
