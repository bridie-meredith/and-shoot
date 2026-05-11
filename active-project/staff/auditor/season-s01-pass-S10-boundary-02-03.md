---
report: boundary-carry-audit
scope: season
target: s01 boundary window-02 -> window-03
cycle: 3
iteration: 2-of-2
timestamp: 2026-05-11
verdict: BOUNDARY-CARRIES
---

# Boundary-carry audit — s01 boundary 2→3 — cycle 3 (iteration 2 of 2)

## Cycle context

Cycle 2 returned BOUNDARY-DROPS-vigil-extinguished-grief-debt-shape with two open faults (fault-001, fault-002) and one scope-question carry (fault-004). Screen-writer recast ID 513 from "the beetles relay the base room" to "the beetles relay the cold candle." fault-003 (maester-named) was resolved at cycle 2 by ID 514 and is unchanged. fault-004 (wage-claim) is acknowledged OUT-OF-SCOPE per the orchestrator's cycle-2 ruling; it does not participate in this re-audit.

## Boundary definition (unchanged from cycle 2)

- Window 2 close region: IDs 305–328 (last 20 active bones of window 2; beats 16 and 17)
- Window 3 open region: first 10 active bones of window 3 — IDs 513, 514, 330, 331, 332, 333, 334, 335, 336, 337

State-changes to carry:
1. Vigil candle extinguished (beat 17, mother's visit scene, IDs 315–324)
2. Grief-debt changes shape (same scene; same physical event as 1)
3. Maester named and active in Taylor's log (beat 16, IDs 305–313) — RESOLVED at cycle 2; no re-examination required
4. Wage-claim formalized (beat 13, IDs 246–264) — OUT-OF-SCOPE per orchestrator ruling; carry-forward to Phase 6
5. Range-at-400m (beat 14, IDs 266–278) — CARRIES per cycle 1; no re-examination required

---

## Findings

### fault-001 — vigil-candle-extinguished — RESOLVED

```yaml
- id: fault-001
  type: pass
  what: >
    ID 513 recast: "the beetles relay the cold candle"
    (replaces cycle-2 text: "the beetles relay the base room")

    Cycle-2 criteria required: at least one physical-register bone in W3's
    open region that names or makes physically observable the vigil-candle
    extinguishment, legible cold (without W2 context).

    "The cold candle" names a concrete physical object by its observable
    thermal condition — cold, not burning. SVO form is physical-register
    (beetles relay the object; the object's state is specified by the
    modifier). A downstream facet author reading W3 cold receives: the
    beetle-relay network is covering a candle that is not lit. This is the
    vigil-extinguished state in physical-register form. The bone follows
    the same construction pattern as the resolved fault-003 bone (ID 514,
    "the beetles relay oc-broken-maester") — subject-relay-object in the
    same SVO template, with the object naming the state by its physical
    marker.

    Cold-reader legibility: "cold candle" does not require W2 context to
    read as extinguished. A cold candle is a candle without flame or heat.
    In a medieval register, an unlit candle described as cold is an object
    that has been extinguished or allowed to go out. The vigil-extinguished
    state is recoverable from the object's descriptor alone.

    Fault cleared.
  why: n/a — no problem found
  criteria: ~
```

### fault-002 — grief-debt-shape-change — RESOLVED

```yaml
- id: fault-002
  type: pass
  what: >
    Same bone as fault-001 (ID 513, "the beetles relay the cold candle").

    Cycle-2 criteria explicitly permitted a single bone to resolve both
    fault-001 and fault-002 if it made the state visible in physical
    register: "one adequate physical-register bone suffices if it names
    or makes observable the state that changed." Cycle-2 further specified
    that fault-001 and fault-002 "originated from the same physical event
    (the mother's visit ending the vigil)."

    The cold candle is the physical marker of the mother's decision. The
    grief-debt shape-change (from active-wait / vigil to closed-wait /
    vigil-over) is coextensive with the vigil-end event; the extinguished
    candle physically instantiates both state-changes simultaneously. A
    W3 facet author reading "the beetles relay the cold candle" receives
    the vigil-end signal. That signal carries the grief-debt
    shape-change as its direct consequence — the same consequence the
    cycle-2 report identified as structurally necessary for W3's
    Hightower-apparatus arc (beats 18–26) to compose correctly with the
    village-claim arc's changed register.

    Fault cleared.
  why: n/a — no problem found
  criteria: ~
```

### fault-003 — maester-named — RESOLVED (unchanged from cycle 2)

```yaml
- id: fault-003
  type: pass
  what: >
    ID 514 "the beetles relay oc-broken-maester" — unchanged from cycle 2.
    oc-broken-maester slug present in W3 open in physical-register relay form.
    Named entity legible cold. Fault resolved at cycle 2; no change.
  why: n/a — no problem found
  criteria: ~
```

### fault-004 — wage-claim-formalized — OUT-OF-SCOPE (carry-forward unchanged)

```yaml
- id: fault-004
  type: flag
  what: >
    Wage-claim formalization (IDs 246–264, beat 13) is approximately 45
    active bones before the W2 close region (IDs 305–328, last 20 active
    bones). The S10 Step 4 rule's stated scope is "state-changes in
    windowN's close region (last 20 bones)." The orchestrator ruled this
    OUT-OF-SCOPE at cycle 2; no bone addition was made; ID 515 is absent
    from the bones file (confirmed: bones file shows 513, 514, then 330
    sequentially, with no 515).

    Carry-forward to Phase 6 as scope-question, not bone-gate fault.
    No fixer dispatch. No criteria set.
  why: >
    If the orchestrator at Phase 6 rules the broad reading applies
    (wage-claim carries regardless of close-region position), a W3 open
    bone naming the wage-claim instrument, tanner-family transactional
    surface, or partial-payment outcome will be required. Under the strict
    reading (close-region only), this finding is withdrawn. The Phase 6
    orchestrator-critic verdict is the decision surface.
  criteria: ~
```

### range-at-400m — CARRIES (unchanged from cycle 1)

```yaml
- id: range-at-400m
  type: pass
  what: >
    Range-at-400m carry confirmed at cycle 1; unchanged. W3 open bones
    establish beetle-relay coverage consistent with a 400m+ operational
    range. No re-examination required.
  why: n/a — no problem found
  criteria: ~
```

---

## Verdict

**BOUNDARY-CARRIES**

fault-001 (vigil-candle-extinguished) and fault-002 (grief-debt-shape-change) are both resolved by ID 513 recast to "the beetles relay the cold candle." The cold candle is a physical-register object that names the vigil-extinguished state in its thermal descriptor, legible without W2 context, in the same SVO relay form as the resolved fault-003 bone (ID 514).

fault-003 (maester-named): resolved at cycle 2 by ID 514; unchanged.

fault-004 (wage-claim): OUT-OF-SCOPE per orchestrator ruling; flagged for Phase 6 scope-question, no bone-gate effect.

range-at-400m: carries; unchanged.

All bone-gate-relevant state-changes from W2's close region are signaled as active constraints in W3's open region in physical-register form. The boundary is clear to proceed.

---

## Archive note

Cycle 2 report was written as the first persisted boundary audit for this boundary. This cycle-3 report overwrites it at the same path per the re-fire overwrite convention. The cycle-2 fault-001/002 criteria — specifically the cold-reader legibility requirement and the single-bone resolution permission — were the operative criteria for this check.
