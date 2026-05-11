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

# Season s01 — Pass S10 Mechanic Audit — Window 2 — Cycle 2 Re-fire

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
      criteria: N/A

    - id: fault-002
      type: pass
      what: Tensometer coverage fault-002 (cycle 2) — IDs 511, 512 orphaned
      why: N/A — resolved
      criteria: N/A

    - id: fault-003
      type: escalate
      what: CURVE-SHAPE — Scenes A (159–181), H (266–278), L (315–324): rise-without-peak. URI-026 per-window iteration cap exhausted at cycle 2. Bones regen did not occur.
      why: Three scenes carry no rupture/commit/registration beat. CURVE-SHAPE and FREQUENCY-BAND both fail on this root cause. Per the orchestrator-critic card, tens-gate residual HARD findings auto-trigger F7 (FAIL) at Phase 6 — bones-first principle. The window cannot self-correct within the per-window cap.
      criteria: Phase 6 orchestrator-critic must receive this as tens-gate-residual-HARD attribution for Scenes A, H, L and produce a FAIL verdict (F7-bone) unless the human gatekeeper authorizes an out-of-cap regen cycle for Window 2.
```

---

## Combined verdict: MECHANIC-FAIL-CURVE-SHAPE-FREQUENCY-BAND

AP-SCAN: PASS. Coverage faults: RESOLVED.

CURVE-SHAPE and FREQUENCY-BAND: FAIL — STRUCTURAL-RESIDUAL. Root cause: bones deficit at Scenes A, H, L. Per-window iteration cap (URI-026, cycle 2 of 2) exhausted.

**MECHANIC-CLEAN-with-tens-gate-residual is not the applicable verdict.** MECHANIC-CLEAN requires AP-SCAN PASS and no hard shape failures. CURVE-SHAPE fails on three scenes against the locked rubric. The tens-gate-residual designation describes the disposition of those failures (routes to Phase 6 F7-bone), not their severity. The failures are real and unresolved.

**Routing:** tens-gate-residual-HARD (Scenes A, H, L) surfaces at Phase 6 orchestrator-critic as F7-bone. The orchestrator-critic card's failure-mode enumeration applies. Human escalation path is Phase 6 FAIL verdict.
