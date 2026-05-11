---
report: mechanic-audit
scope: season
target: s01 — Window 2 (IDs 159–328 + interpolated 495–512 inserts)
pass: S10 Phase 3 Sweep B
window: 2
cycle: 2
timestamp: 2026-05-11
auditor-classes: AP-SCAN | CURVE-SHAPE | FREQUENCY-BAND
verdict: MECHANIC-FAIL-CURVE-SHAPE-FREQUENCY-BAND
---

# Season s01 — Pass S10 Mechanic Audit — Window 2 — Cycle 2

## Scope

Proto-lines `active-project/theater/proto-lines/s01.bones.md` IDs 159–328 (beats 9–17), plus interpolated IDs 495–512 that fall within or at the boundary of Window 2. Tensometer file `active-project/theater/facets/tensometer-s01-window-02.md` now present and read.

## Cycle-1 fault resolution check

Six faults were issued in cycle 1. Status of each:

**fault-001** (ID 166 — `oc-tanner-father holds the step` — FAULT-FORM-NON-ACTION-VERB):
ID 166 now reads `oc-tanner-father stills`. RESOLVED.

**fault-002** (ID 226 — `the headache wakes taylor-hebert-flea-bottom` — FAULT-FORM-INTERIORITY):
ID 226 now reads `taylor-hebert-flea-bottom wakes`. RESOLVED.

**fault-003** (ID 237 — `the neighbors press the doorways` — FAULT-FORM-MULTI-SUBJECT):
ID 237 now reads `the neighbor presses the doorway`. Singular subject, singular object. RESOLVED.

**fault-004** (ID 241 — `the neighbors withdraw` — FAULT-FORM-MULTI-SUBJECT):
ID 241 now reads `the neighbor withdraws`. Singular subject. RESOLVED.

**fault-005** (ID 274 — `the headache wakes taylor-hebert-flea-bottom` — FAULT-FORM-INTERIORITY):
ID 274 now reads `taylor-hebert-flea-bottom wakes`. RESOLVED.

**fault-006** (IDs 500, 508, 501, 502, 505, 496 — out-of-monotonic-sequence insertions — FAULT-FORM-ID-SEQUENCE):
Schema re-read confirms: "Stable — once assigned, never reused, never reassigned. Re-ordering preserves IDs; the stitcher walks IDs in citation order, not numeric order." Out-of-numeric-order IDs are schema-compliant; ID stability is what the schema protects, not monotonic file-position. SCHEMA-COMPLIANT. Cycle-1 fault withdrawn.

All six cycle-1 faults resolved or withdrawn.

---

## New bones check — IDs 509, 510 (beat 10 expansion), 511, 512 (W2 open boundary carry)

**ID 509:** `the flies relay the carter`
Subject: `the flies` — collective insect-group (flag-006 convention, pending ruling). Verb: `relay` — physical transmission act. Object: `the carter` — unnamed environment element in `the <noun>` form. No deny-list verb. No copula, negation, perception verb, modifier, conjunction, abstraction-as-object. CLEAN against AP-SCAN deny-list. Carries existing flag-006 (insect-group collective-singular convention ruling pending).

**ID 510:** `the carter exits the junction`
Subject: `the carter` — unnamed environment element, singular. Verb: `exits` — physical motion, transitive. Object: `the junction` — location. Clean SVO. CLEAN.

**ID 511:** `taylor-hebert-flea-bottom faces the junction`
Subject: actor slug, singular. Verb: `faces` — physical orientation act. Object: location. Clean SVO. CLEAN.

**ID 512:** `oc-tanner-elder faces the road`
Subject: actor slug, singular. Verb: `faces`. Object: location. Clean SVO. CLEAN.

No deny-list violations in new bones 509–512.

---

## AP-SCAN

PASS. No new faults. All cycle-1 faults resolved. Carry-forward flags from cycle 1 unchanged:

- **flag-002** (carries): pervasive abstract-object relay/spread pattern (IDs 187, 190, 200, 209, 214, 216, 266, 267, 269, 287, 296, 297, 298). Convention ruling pending.
- **flag-003** (carries): consecutive duplicate write beats, IDs 223–224. Intent unverified.
- **flag-004** (carries): consecutive duplicate write beats, IDs 271–272. Intent unverified.
- **flag-005** (carries): possessive compound subject `the lords-man's man`, IDs 234–235. No slug assigned.
- **flag-006** (carries): plural insect-group subjects throughout. Collective-singular ruling pending.

---

## CURVE-SHAPE

FAIL. Tensometer now present. Evaluation runs against `active-project/theater/facets/tensometer-s01-window-02.md` and `design/shoot-v2/rubric-tensometer.md`.

### Scene-level shape

The dramatist has identified the following scene-level failures in the tensometer kickback section:

**SCENE A (IDs 159–181) — rise-without-peak.** Six 2s accumulate (@166, @170, @171, @172, @178, @179) with no 3. The rubric requires "at least one 3 OR an explicit dramatist-flagged exception (scene-as-respite / scene-as-transit)." No such exception is claimed for Scene A. The father's goods-presentation (ID 172) is the named 3 candidate and is rated 2. The scene closes without rupture/commit/registration beat at peak. SHAPE-FAIL.

**SCENE E (IDs 209–225) — inert stretch.** 17 consecutive 1s covering network deployment and relay beats. The rubric requires no flatlining: "a scene of 30+ beats with no 2s or 3s is a scene that does no dramatic work." At 17 beats this is below the 30-beat explicit threshold, but the Scene E classification as `[inert-stretch]` in the dramatist's kickback note acknowledges the structural gap. No 2s or 3s in this stretch. Flagged as SHAPE-WEAK (below hard fault threshold, above clean threshold). Escalation path: screen-writer kickback already issued by dramatist.

**SCENE H (IDs 266–278) — rise-without-peak.** Three 2s (@274, @275, @505) without a 3. Same structural failure as Scene A: rise without rupture. SHAPE-FAIL.

**SCENE L (IDs 315–324) — rise-without-peak.** Two 2s (@318, @323) without a 3. Mother's vigil-candle reveal closes without disclosure-rupture. SHAPE-FAIL.

**Scenes with 3s (passing scene-level check):**
- Scene C (IDs 232–244): 3s at @234, @236 (eviction peak). 2s lead in. SHAPE-OK.
- Scene F (IDs 246–264): 3 at @255 (coin-exchange). 2s lead in. SHAPE-OK.
- Scene I (IDs 280–301): 3 at @496 (rhythm-stilling). 2s lead in at @287, @288, @297, @298. SHAPE-OK.

### Episode-level shape

Window 2 shows two legitimate peaks (Scene C eviction at IDs 234/236, Scene F coin-exchange at ID 255) plus one compact peak (Scene I at ID 496). The eviction cluster is the window climax and sits in the middle third of the window — structural inversion risk per the rubric ("Episodes ending with their highest peak in the first third are structurally inverted"). The eviction peak is not in the first third; it is roughly mid-window. The back half (Scenes H, I, L) is structurally underloaded relative to the front-half climax. The climax is not at the back; it is at the center. This constitutes a partial shape failure: the window's highest 3-cluster is not in the back half as the rubric requires for clean act-structure.

### Adjacency check

- @234 (3) preceded by @233 (1): 1→3 jump. The rubric flags direct 1→3 jumps as either misratings or true sudden-turns. ID 233 is `the lords-man speaks to the tenant family` (rated 1); ID 234 is `the lords-man's man breaks the door latch` (rated 3). The rupture of the door-latch is a genuine sudden physical escalation. Defensible as true sudden-turn. Flagged for review but not auto-faulted.

- @496 (3) preceded by @298 (2), @297 (2): 2→2→3 — clean adjacency.

- @236 (3) preceded by @235 (2): 2→3 — clean.

- @255 (3) preceded by @254 (2): 2→3 — clean.

---

## FREQUENCY-BAND

FAIL. Distribution from the tensometer file:

- 3s: 4 / ~163 ≈ 2.5% (target 5–10%) — **below floor**
- 2s: ~23 / ~163 ≈ 14% (target 20–30%) — **below floor**
- 1s: ~136 / ~163 ≈ 83% (target 60–75%) — **above ceiling**

The frequency band is outside target on all three rungs. The dramatist correctly refuses scalar inflation and attributes the miss to Scenes A, H, and L lacking rupture/commit/registration beats — a bones deficit, not a rating error. The frequency fault is load-bearing: it confirms the CURVE-SHAPE finding and triggers the screen-writer kickback path per the rubric.

---

## Tensometer coverage fault

**fault-001 (cycle 2)**

- id: fault-001
- type: fault
- what: IDs 509 and 510 exist within the Window 2 bone range (between IDs 195 and 205 in the bones file) but carry no tensometer entries in `tensometer-s01-window-02.md`. The tensometer jumps from @195 directly to @200 with no @509 or @510 entry.
- why: The tensometer rubric states "tensometer has no per-entry cull — every proto-line gets a scalar." Two bones within the rated window are unrated. The stitcher contract and cross-facet gate depend on every bone having a tensometer scalar. Missing scalars break the cross-facet contract for these two bones.
- criteria: The tensometer must be amended to include entries for @509 and @510 at their correct positions (between @195 and @200 in the facet file's citation-order sequence). Scalars assigned per rubric.

**fault-002 (cycle 2)**

- id: fault-002
- type: fault
- what: IDs 511 and 512 exist in the bones file as boundary-carry bones at the W2 open (immediately before ID 159). They are absent from `tensometer-s01-window-01.md` (which ends at @155) and absent from `tensometer-s01-window-02.md` (which begins at @159). Neither window's tensometer covers them.
- why: Same cross-facet contract violation as fault-001. IDs 511 and 512 are valid rated bones that exist in the aggregate; they have no tensometer scalars in any window's coverage. The stitcher cannot consume them with full facet context.
- criteria: Either the Window 1 tensometer must be amended to include @511 and @512 (if they are classified as W1-close boundary beats), or the Window 2 tensometer must be amended to include them before @159 (if they are classified as W2-open boundary carry). Assignment to one window is required; dual-coverage is not required or permitted.

---

## Findings summary

### AP-SCAN: PASS

No new faults in cycle 2. All cycle-1 faults resolved. Carry-forward flags unchanged (flags 002–006 from cycle 1).

### CURVE-SHAPE: FAIL

Hard shape failures:
- Scene A (IDs 159–181): rise-without-peak. No 3. No transit exception claimed.
- Scene H (IDs 266–278): rise-without-peak. No 3. No transit exception claimed.
- Scene L (IDs 315–324): rise-without-peak. No 3. No transit exception claimed.

Episode-level: window climax located in middle third, not back half. Structurally underloaded back half.

Screen-writer kickbacks already issued by dramatist. Routing confirmed: bones regen required at Scenes A, H, L before CURVE-SHAPE can clear.

### FREQUENCY-BAND: FAIL

All three rungs out of target band. 3s at 2.5% (floor 5%). 2s at 14% (floor 20%). 1s at 83% (ceiling 75%). Caused by bones deficit confirmed by CURVE-SHAPE findings. Not a miscalibration fault.

### Tensometer coverage: FAULT

Two faults (fault-001, fault-002 above):
- IDs 509, 510: unrated, within W2 range
- IDs 511, 512: unrated, orphaned between windows

---

## Combined verdict: MECHANIC-FAIL-CURVE-SHAPE-FREQUENCY-BAND

AP-SCAN is clean. CURVE-SHAPE and FREQUENCY-BAND both fail on the same root cause: bones deficit at Scenes A, H, L (no rupture/commit/registration beat). The fix path is bones regen at those scenes, not tensometer rerating. Additionally, tensometer coverage must be extended to IDs 509, 510, 511, 512 after bones regen lands.

Per-window iteration cap: this is cycle 2 of 2 for Window 2. If bones regen does not produce convergence, the residual is a `tens-gate-residual-HARD` finding for Phase 6 (orchestrator-critic F7-bone).
