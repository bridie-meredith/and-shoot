# Audit Report — Season S01 Pass 5 Continuity — Chapter 10
schema: audit-report
run: season-s01-pass5-ch10-continuity
date: 2026-05-07
auditor: fork (fresh context)
target: active-project/theater/proto-lines/chapter-10.md
pass: 5 — continuity
file-level: FAIL

axes-checked:
  - reachability
  - state-persistence
  - reference-resolution
  - POV-consistency
  - time-consistency
  - cause-effect
  - ch09→ch10-boundary
  - climax-anchor (ID 24)
  - prop-census-file adjudication
  - denouement-exit-sequence

prior-passes:
  - pass-2 (constraint audit): 6 faults resolved by fixer
  - pass-3 (shape): CLEAN (no re-order required; shape correct for season finale)
  - pass-4 (trim): no report found; not adjudicated

---

## Summary

total-lines-in-scope: 57 (IDs 51–57 transit block + IDs 1–50 main sequence)
correct: 53
faults: 3
flags: 1
escalate: 0

fault-breakdown:
  FAULT-CONTINUITY-LOCATION: 1 (ID 52 — unanchored sept-interior beat)
  FAULT-CONTINUITY-PROP-ABSENT: 1 (ID 14 — ward-record scroll not in Plumm's established inventory)
  FAULT-CONTINUITY-ENTRY-MISSING: 1 (Rowan enters approach road ID 53; never enters hall)

---

## Findings

---

### fault-001

id: fault-001
type: fault
fault-class: FAULT-CONTINUITY-LOCATION
line-id: 52
line: `taylor-hebert-westeros exits the sept`
what: Chapter 09 closes with Taylor at the roadside rise (ch09 IDs 100–102 header: `taylor-hebert-westeros crosses the approach road / taylor-hebert-westeros reaches the roadside rise`). Her final beat in ch09 is ID 99 `taylor-hebert-westeros repositions the raven` — she is on the approach road at the elevated vantage, not inside the sept. Chapter 10 ID 52 asserts she exits the sept, which requires her to have re-entered the sept from the roadside rise between ch09-close and ch10-open. No proto-line records that transit. There is no re-entry beat, no approach-to-sept beat, and no interior-sept beat preceding ID 52. The sept-exit at ID 52 is therefore an unreachable state: Taylor cannot exit a location she has no recorded path into.
why: An unanchored location assertion at a chapter boundary breaks the spatial continuity chain the downstream shape and prose passes depend on. If Taylor exited the sept, she must have been in the sept. If she was in the sept, she must have re-entered it from the roadside rise. Neither re-entry beat exists. The ch09→ch10 transit block (IDs 51–57) was intended to bridge the roadside-rise → hall gap; instead ID 52 inserts an unearned location, creating a contradiction rather than resolving one. ID 53 (`septon-rowan enters the approach road`) and ID 54 (`taylor-hebert-westeros enters the approach road`) are correct transit beats for her position at ch09-close; ID 52 preceding them is the problem.
criteria: Delete ID 52 (`taylor-hebert-westeros exits the sept`) from the transit block. The remaining sequence — ID 53 Rowan enters approach road, ID 54 Taylor enters approach road, ID 55 Taylor enters postern gate, ID 56 Taylor enters hall — reads as a coherent transit from the roadside-rise position where ch09 closes. If a departure-from-vantage beat is needed before the approach road entry, it must be grounded at the roadside rise, not at the sept.
scope: line

---

### fault-002

id: fault-002
type: fault
fault-class: FAULT-CONTINUITY-ENTRY-MISSING
actor: septon-rowan
what: Rowan is assigned a transit beat at ID 53 (`septon-rowan enters the approach road`). He then appears at ID 9 as an active participant in the hall scene (`septon-rowan speaks to oc-castellan-harrenhal`). No proto-line records Rowan entering the hall. The transit block (IDs 51–57) includes Taylor's hall entry at ID 56 (`taylor-hebert-westeros enters the hall`) but contains no corresponding entry beat for Rowan. His last positional beat is the approach road (ID 53). The hall at ID 9 is unreachable without an entry line.
why: An enter/exit continuity gap for a named character at a chapter's scene boundary breaks the actor-position tracking the pass-5 continuity layer exists to maintain. Rowan is a witness at the climax (ID 24); his presence must be spatially grounded. Showrunner memory fault-006 flags Rowan's transit from village-common to hall as an open continuity fault, but that fault covers a larger gap. The specific missing beat here — Rowan entering the hall — is a line-level gap within the ch10 transit block that fault-006 does not resolve. A line for Rowan entering the hall was simply not included in IDs 51–57 when Taylor's parallel entry (ID 56) was.
criteria: Insert a line in the transit block: `septon-rowan enters the hall`. Placement: immediately before or after ID 56 (`taylor-hebert-westeros enters the hall`), as they arrive together per the transit sequence. Both enter the approach road in the same transit block; both should enter the hall. Assign the next available monotonic integer ID.
scope: line (insert)

---

### fault-003

id: fault-003
type: fault
fault-class: FAULT-CONTINUITY-PROP-ABSENT
prop: prop-ward-record-scroll
line-id: 14
line: `ser-harwick-plumm opens the ward-record scroll`
what: The ward-record scroll appears in Plumm's hands at ID 14 with no prior establishment line in chapter 10 or in Plumm's recorded pre-ch10 inventory. Showrunner memory records Plumm's pre-ch10 inventory as `[prop-intercession-record-book]` (acquired ch05 line 66; not produced again). The census file (ID 4) was adjudicated as acceptable below (see flag-001). The ward-record scroll is a distinct prop from the census file and from the intercession-record-book — it is the formal administrative record that will receive the ward-of-administration entry (ID 24) and is later sealed and carried out (IDs 38–44). This prop is the direct instrument of the climax and has no establishment line anywhere in the proto-line sequence. Plumm sets the census file at ID 4 (his arrival prop); produces the stylus at ID 23 (implied from ID 36 `dips the stylus`); but the ward-record scroll simply opens at ID 14 with no prior lines showing Plumm produced or carried it into the hall.
why: The prop that receives the season's climactic act (ID 24) must be traceable to the actor's inventory at the point it is used. Unlike the census file (an ongoing working instrument Plumm carries in his administrative role), the ward-record scroll is a specific formal record being created in this scene — a blank that did not exist before this moment in the administrative process. Its appearance at ID 14 without an introduction beat means the climax instrument is unanchored. Downstream facet passes (state-updates, narrator-interest) will cite IDs 14 and 24 as load-bearing; if the scroll has no establishment beat, those citations have no traceable source. This is load-bearing.
criteria: Insert a line before ID 14 that establishes Plumm producing the scroll: e.g., `ser-harwick-plumm produces the ward-record scroll` or `ser-harwick-plumm draws the ward-record scroll`. Placement: between ID 13 (`oc-castellan-harrenhal speaks to ser-harwick-plumm` — the instruction to write) and ID 14 (the opening of the scroll). The instruction at ID 13 is the logical trigger; the production beat fills the gap between instruction and use.
scope: line (insert)

---

## Flag (non-fault)

---

### flag-001

id: flag-001
type: flag
prop: prop-census-file
line-id: 4
line: `ser-harwick-plumm sets the census file`
what: The census file has no upstream proto-line establishing it. It appears at ID 4 without a prior introduction beat in ch10 or in Plumm's recorded ch10-open inventory. The ch10 pass-2 report flagged this as a pipeline gap (non-actionable without a hall location card) and routed it to the orchestrator.
adjudication (continuity layer): Not a blocking fault. The census file is Plumm's ongoing administrative working document — he has been conducting the wardship census across ch04, ch05, ch07, and ch09 in his role as Celtigar-deputized census agent. A census file carried by the census agent to a wardship determination meeting is a contextually implied carry, not a prop conjured from nothing. This is structurally different from the ward-record scroll (fault-003), which is a blank formal record created specifically for this proceeding. The census file is a running document Plumm already possessed; its absence from the inventory record is a record-keeping gap, not an impossibility gap. Fixer does not need to add an introduction beat for the census file. Orchestrator should update Plumm's inventory record to include `prop-census-file` as a carried-forward working document from ch09.
criteria: None required at line level. Route to orchestrator: add `prop-census-file` to Plumm's inventory tracking as a chapter-09-carried-forward item.

---

## Axis-by-axis summary

### reachability
FAIL — fault-001 (ID 52: Taylor cannot exit the sept without having entered it; ch09 closes her at roadside rise, not inside the sept).

### state-persistence
FAIL — fault-003 (ward-record scroll appears at ID 14 without establishment; prop state has no traceable origin in Plumm's inventory at ch10-open).

### reference-resolution
PASS — all named actors resolve to series cast roster. All prop slugs used (census file, ward-record scroll, stylus, seal) are contextually coherent with the scene function. `oc-castellan-harrenhal` resolves correctly throughout.

### POV consistency
PASS — narrator `taylor-hebert-westeros` maintained throughout. No interiority verbs survive pass-2. Non-Taylor actors rendered objectively. No POV leak.

### time consistency
PASS — no time discontinuity within ch10. The hall scene is a single continuous event. No time-skip markers (blank IDs) appear between IDs 1–50, consistent with a single unbroken scene.

### cause-effect
PASS — beat sequence is causally coherent throughout. ID 13 (castellan instructs Plumm to write) → ID 23 (stylus dipped) → ID 24 (entry written) is properly chained. Exit sequence (Celtigar 30, castellan 35, Plumm 44, Rowan 47, Taylor alone 48–50) is causally ordered and each exit is preceded by the final verbal exchange that closes that character's participation. No cause-effect inversion found.

### ch09→ch10 boundary
FAIL — fault-001 (ID 52 inserts an unanchored sept-interior location between the ch09-close roadside-rise position and the approach-road transit). FAULT — fault-002 (Rowan enters approach road in transit block but never enters the hall; entry beat missing).

### climax anchor (ID 24)
PASS — all five required parties are spatially present and unexited at ID 24:
  - ser-harwick-plumm: IDs 23–24 (active). ANCHORED.
  - oc-castellan-harrenhal: last act ID 22; exits ID 35. ANCHORED.
  - septon-rowan: last act ID 21; exits ID 47. ANCHORED. (Entry fault fault-002 is upstream of climax; presence is continuous from arrival.)
  - ser-edwyn-celtigar: last act ID 12; next act ID 29; exits ID 30. ANCHORED.
  - taylor-hebert-westeros: last act ID 18; next act ID 26. ANCHORED.
  - ser-aemon-bracken: absent. Established by ch09 line 60 (`exits the outer ward`) + ID 57 advisory beat. ANCHORED as absent.

### denouement exit sequence
PASS — all four exits are ordered, causally preceded, and non-overlapping:
  - Celtigar: ID 30. Last act 29. Sequential. CORRECT.
  - Castellan: ID 35. Last act 34 (Taylor speaks to castellan). Sequential. CORRECT.
  - Plumm: ID 44. Sealing sequence IDs 38–43 complete before exit. Sequential. CORRECT.
  - Rowan: ID 47. Exchange with Taylor IDs 45–46 complete before exit. Sequential. CORRECT.
  - Taylor alone: IDs 48–50. CORRECT.

---

## Pipeline gaps (route to orchestrator, not fixer)

gap-001 (carried from pass-2):
  what: No warehouse location card for "the hall" (the ch10 scene location).
  why: Without a card defining exits and fixed props for loc-harrenhal-administrative-hall (or equivalent), FAULT-PHYSICAL-EXIT-INVALID cannot be adjudicated for enter/exit beats. The postern gate re-opening for Taylor at ID 55 (it was explicitly closed at ch09 ID 98) cannot be classified as a fault or a pass without a card defining gate-opening permissions.
  route: Orchestrator. Author loc-harrenhal-administrative-hall before any further physical-layer audit.

gap-002:
  what: `prop-census-file` absent from Plumm's pre-ch10 inventory record.
  why: See flag-001. Adjudicated as non-blocking at continuity layer; but the inventory record is incomplete.
  route: Orchestrator. Add `prop-census-file` to Plumm's inventory tracking as carried forward from ch09.

---

## Open continuity faults inherited from prior passes (not re-audited here)

fault-002 (showrunner memory): Taylor transit from approach road (ch08-close) to Harrenhal hall (ch10-open) — residual gap covers ch09 roadside-rise descent and hall entry. The IDs 51–57 transit block was introduced to address this gap. After removal of the faulty ID 52 (fault-001 above) and addition of Rowan's hall entry (fault-002 above), the remaining transit sequence (53→54→55→56) provides Taylor's hall-entry path. This resolves the ch09-roadside-rise → hall portion of the residual gap. Orchestrator should update showrunner memory fault-002 status after fixer commits fault-001 and fault-002 repairs.

fault-006 (showrunner memory): Rowan transit from village-common to hall unrecorded. The transit block ID 53 (`septon-rowan enters the approach road`) partially addresses this; it does not record the full path from village-common. This remains open but is not within ch10's scope to resolve — it is a ch09 or inter-chapter gap.

---

## Fixer dispatch criteria summary

fault-001: DELETE ID 52 (`taylor-hebert-westeros exits the sept`). No replacement needed — the remaining transit sequence is coherent without it.

fault-002: INSERT one line `septon-rowan enters the hall` in the transit block, adjacent to ID 56 (`taylor-hebert-westeros enters the hall`). Assign next available monotonic integer ID.

fault-003: INSERT one line `ser-harwick-plumm produces the ward-record scroll` between ID 13 and ID 14. Assign next available monotonic integer ID.

All three are line-scope changes. No structural re-ordering required. Pass-3 shape verdict (CLEAN) is not disturbed by these insertions/deletions — they are transit-block corrections and a single prop-introduction line preceding an existing beat.
