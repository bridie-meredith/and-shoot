---
report: mechanic-audit
scope: season
season: s01
window: 01
window-range: IDs 1–155
beats: 1–8
date: 2026-05-11
classes-checked: CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN
tens-file: ABSENT
verdict: MECHANIC-FAIL-CURVE-SHAPE
---

# Mechanic Audit — s01 Window 01 — IDs 1–155

## Inputs read

- `active-project/theater/proto-lines/s01.bones.md` — IDs 1–155
- `active-project/staff/auditor/season-s01-pass-S10-cut-proposal.md` — window shape description
- `design/shoot-v2/rubric-tensometer.md` — CURVE-SHAPE and FREQUENCY-BAND class definitions
- `.claude/commands/and-season.md` §Pass S10 Step 3 — mechanic brief
- `.claude/commands/and-facets-audit.md` — FILE ABSENT (class library missing; see fault-003 below)

---

## Protocol status

**Tensometer file for Window 01 is absent.** Expected path: `active-project/theater/facets/tensometer-s01-window-01.md` (or equivalent naming). No file found at any naming variant checked. FREQUENCY-BAND cannot be evaluated without tensometer scalars. This is a protocol fault (tens authoring did not produce output readable by this fork). See fault-003.

---

## CURVE-SHAPE

### Window-level shape (from cut proposal + bones)

Per `season-s01-pass-S10-cut-proposal.md`:
- Rise: beats 1–7 (village domestic arc → lord's-man file → Flea Bottom arrival + network establishment + maester ambient)
- Peak: beat 8 (dock-runner transactional exchange, IDs 148–152; Taylor moves from cataloged-unknown to active-participant-in-network)
- Fall: "log closes; runner does not know what she is" (IDs 153–155)

### Scene-level inventory

| Scene stretch | IDs | Shape notes |
|---|---|---|
| Domestic village open | 1–23 | Ambient rise; lord's-man record (IDs 71–77) is institutional stakes entry |
| Yard network walks | 25–34 | Transitional / ambient |
| Mother's song | 36–46 | Emotional inflection; song dropped at ID 43 — structural micro-peak |
| Task assignment | 48–60 | Procedural; father's routing pattern |
| Reeve + lord's-man | 62–77 | Institutional stakes; reeve slows step (ID 66) is reversal-proximity beat; lord's-man writes record (ID 75) is registration beat |
| Departure | 83–92 | Structural turn (relocation); Taylor crosses gate |
| Flea Bottom arrival + perimeter | 94–126 | Extended ambient; maester speaks to room (ID 111) is first ambient-3 candidate |
| Maester crosses / speaks / laughs | 128–134 | ID 506 (laughs) — inserted bone; structural registered-observation moment |
| Watch patrol + dock-runner first appearance | 136–143 | Dock-runner pivots and exits; Taylor holds feet |
| Peak — dock-runner exchange | 145–152 | Bilateral transactional dialogue; window's structural climax |
| Aftermath | 153–155 | Log open / write / close — flat mechanism close |

### SHAPE-COHERENT-FLAT-AFTERMATH finding

**Finding:** IDs 153–155 constitute a three-bone flat aftermath immediately following the window's structural peak (IDs 145–152).

The peak exchange is IDs 148–152:
- 148: oc-tanner-elder speaks to taylor-hebert-flea-bottom
- 149: taylor-hebert-flea-bottom faces oc-dock-runner
- 150: oc-dock-runner speaks to taylor-hebert-flea-bottom
- 151: taylor-hebert-flea-bottom speaks to oc-dock-runner
- 152: oc-dock-runner exits the junction

The aftermath is IDs 153–155:
- 153: taylor-hebert-flea-bottom opens the log
- 154: taylor-hebert-flea-bottom writes the entry
- 155: taylor-hebert-flea-bottom closes the log

This is a pure log-mechanism close with zero cost-register, zero aftermath-texture, and zero physical aftermath bones. The cut proposal describes the fall as "runner does not know what she is" — this asymmetry is the structural fall, but it has no physical-register expression in the bones. The reader-level charge of the transactional exchange (Taylor's first active move in the network) is not landed before the cut. Three bones of open/write/close is a structural flat aftermath.

**Classification:** SHAPE-COHERENT-FLAT-AFTERMATH — HARD per Pass S10 Step 3.

**Consequence:** Under Step 3's combined-verdict rule, a SHAPE-COHERENT-FLAT-AFTERMATH HARD blocks WINDOW-ACCEPT regardless of audience verdict. Verdict is WINDOW-REVISE-bones at IDs 152–155.

---

## FREQUENCY-BAND

**Status: BLOCKED**

Tensometer file for Window 01 is absent. Scalar distribution across the ~155 active bones of this window cannot be evaluated. The 60–75% / 20–30% / 5–10% band check cannot run.

This is not a FREQUENCY-BAND finding — the check did not run. See fault-003 for the protocol fault.

---

## AP-SCAN

### Class library status

`and-facets-audit.md` does not exist at `.claude/commands/and-facets-audit.md`. Formal AP-SCAN entries cannot be cited by library class ID. AP-SCAN is run against the named anti-patterns available in `rubric-tensometer.md` and the structural patterns observable in the bones.

### AP-SCAN findings

**REPETITION-MECHANISM-log-open-write-close (flag):**

Log mechanism (open / write / close, or partial equivalents) appears at the following ID clusters within Window 1:
- IDs 21–23
- IDs 32–34
- IDs 58–60
- IDs 79–81
- IDs 101–103
- IDs 109 (write only, embedded in perimeter scene)
- IDs 113–116 (write + open + write + close)
- IDs 123–126 (open + write + close)
- IDs 132–134
- IDs 153–155

Approximately 9–10 distinct log-mechanism clusters in 155 bones. Accounting for active bones only (blank IDs 24, 35, 47, 61, 70, 78, 82, 93, 104, 117, 127, 135, 144 are structural gaps, approximately 13 blanks), the active bone count is approximately 142. Log-mechanism bones account for roughly 27 active bones — approximately 19% of the window's active bone content is log mechanism.

This is not a constraint violation. The log is structurally load-bearing as the POV character's primary externalization device. However, the repetition density across 155 bones creates a rhythm-lock risk: a reader encounters the log-close sequence as the scene-close mechanism for nearly every scene in the window. This is a flag for the tens-authoring pass (ensure log-close beats are rated 1 throughout, not inflated by scene proximity to peaks) and for the stitcher (ensure compression is applied to log mechanism).

**Classification:** AP-SCAN flag — REPETITION-MECHANISM-log-open-write-close. Not a HARD fault. Does not block WINDOW-ACCEPT independently.

**REPETITION-MECHANISM-insect-relay (flag):**

Insect spread/relay sequences appear at IDs 26–29, 95–97, 106–108, 119–122, 130, 137, 139, 143 — multiple multi-beat spread deployments. These are structurally necessary (protagonist's sensory mechanism). Same compression risk as log mechanism: rating risk (ambient escalation if rated above 1) and stitcher density risk. Flag, not fault.

**Classification:** AP-SCAN flag — REPETITION-MECHANISM-insect-relay. Not a HARD fault.

---

## Findings

```yaml
audit:
  scope: season
  target: s01-window-01
  timestamp: 2026-05-11
  window-range: IDs 1–155
  classes: CURVE-SHAPE / FREQUENCY-BAND / AP-SCAN
  findings:
    - id: fault-001
      type: fault
      what: IDs 153–155 — log open/write/close immediately following window peak at IDs 148–152
      why: SHAPE-COHERENT-FLAT-AFTERMATH (HARD). The window's structural peak (dock-runner transactional exchange; Taylor's first active network move) is followed by a three-bone flat log-mechanism close with zero cost-register, zero aftermath-texture, zero physical aftermath bones. The asymmetric fall ("runner does not know what she is") is the structural fall but has no physical-register expression in the bones before the cut. HARD per Pass S10 Step 3 — blocks WINDOW-ACCEPT.
      criteria: at minimum 1–3 physical-register aftermath bones must exist between ID 152 (dock-runner exits) and the log-open at ID 153, carrying Taylor's cost-register or aftermath-texture from the transactional exchange; OR the log-mechanism close must itself be restructured to carry aftermath texture; the aftermath must not be a flat mechanism-only close following the window's peak

    - id: fault-002
      type: flag
      what: AP-SCAN — log open/write/close mechanism (9–10 clusters, ~19% of active bones, IDs 21–23 / 32–34 / 58–60 / 79–81 / 101–103 / 109 / 113–116 / 123–126 / 132–134 / 153–155)
      why: High-density repetition of a single structural mechanism across the window creates rhythm-lock risk and tens-rating inflation risk (ambient escalation at log-close beats near scene peaks). Does not independently block WINDOW-ACCEPT. Advisory for tens-authoring pass and stitcher.

    - id: fault-003
      type: fault
      what: tensometer file for Window 01 absent; and-facets-audit.md class library absent
      why: FREQUENCY-BAND check cannot run without tensometer scalars. Tens authoring (Step 2) did not produce an output file readable by this mechanic fork. AP-SCAN class library (and-facets-audit.md) is missing — formal class IDs cannot be cited. Both are protocol gaps that leave the mechanic audit incomplete.
      criteria: tens authoring must produce active-project/theater/facets/tensometer-s01-window-01.md (or the canonical path per the naming convention in and-season.md Step 2) before FREQUENCY-BAND can be evaluated; and-facets-audit.md must be authored at .claude/commands/and-facets-audit.md before AP-SCAN formal class IDs can be used
```

---

## Combined verdict

**MECHANIC-FAIL-CURVE-SHAPE**

- CURVE-SHAPE: FAIL — SHAPE-COHERENT-FLAT-AFTERMATH HARD at IDs 153–155
- FREQUENCY-BAND: BLOCKED — tensometer file absent; check did not run
- AP-SCAN: FLAG (non-blocking) — REPETITION-MECHANISM-log-open-write-close; REPETITION-MECHANISM-insect-relay

Routing per Step 3: WINDOW-REVISE-bones-152–155. Screen-writer dispatched for REGEN-ADD at IDs 152–155 (1–3 physical-register aftermath bones before log-open; REGEN-ADD discipline, position-aware). FREQUENCY-BAND must re-run after tens authoring completes.
