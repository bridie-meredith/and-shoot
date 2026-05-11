---
report: boundary-carry-audit
scope: season
target: s01 boundary window-02 -> window-03
cycle: 2
timestamp: 2026-05-11
verdict: BOUNDARY-DROPS-vigil-extinguished-grief-debt-shape
---

# Boundary-carry audit — s01 boundary 2→3 — cycle 2

## Cycle context

Cycle 1 returned BOUNDARY-DROPS with four faults (fault-001 through fault-004) and one carry (range-at-400m). Screen-writer added IDs 513, 514, 515 between gap 329 and ID 330. This report re-audits the boundary against those additions.

## Boundary definition

- Window 2 close region: IDs 305–328 (last 20 active bones of window 2; beats 16 and 17)
- Window 3 open region: first 10 active bones of window 3 — now IDs 513, 514, 515, 330, 331, 332, 333, 334, 335, 336

State-changes to carry per cycle 1:
1. Vigil candle extinguished (beat 17, mother's visit scene, IDs 315–324)
2. Grief-debt changes shape (same scene; same physical event as 1)
3. Maester named and active in Taylor's log (beat 16, IDs 305–313)
4. Wage-claim formalized (beat 13, IDs 246–264)
5. Range-at-400m (beat 14, IDs 266–278) — CARRIES per cycle 1; no re-examination required

---

## Findings

### fault-001 — vigil-candle-extinguished

```yaml
- id: fault-001
  type: fault
  what: >
    ID 513 "the beetles relay the base room" is the addition intended to carry
    the vigil-extinguished state (dispatch context: "beetles return without
    registering candle flame"). The bone relays a location (the base room,
    loc-flea-bottom-base inner room), not a specific internal state-change.
    The SVO form records physical coverage of the space; it does not name,
    imply, or physically register the absence of flame or the extinguishment
    event. A downstream facet author reading W3's open cold would receive:
    beetles are covering the base room. They would not receive: the vigil
    candle is extinguished; the grief-debt state has changed.
  why: >
    The boundary-carry rule (S10 Step 4) requires state-changes from the close
    region to be signaled as active constraints in physical register in the
    open region. A room-relay bone satisfies the "physical register" form but
    does not satisfy the "active constraint" content requirement for the
    vigil-extinguished state. The state remains implicit — recoverable only by
    reading W2's close region — which is exactly the condition the rule is
    designed to prevent. Downstream facet authors (sensory, narrator, vibes)
    generating W3 content without W2 context will not have the mother's decision
    and its grief-debt implications as a visible constraint in their working window.
  criteria: >
    The W3 open region must contain at least one physical-register bone that
    names or makes physically observable the specific state-change from beat 17:
    the vigil-candle extinguishment or the grief-debt shift from active-wait to
    closed-wait. A relay of the candle-absent room state, a physical beat
    showing the absence of the flame signal in the relay, or an equivalent
    that names the state by its physical marker (not the room that contained it)
    would satisfy the requirement. The bone must be legible cold — without
    reading W2.
```

### fault-002 — grief-debt-shape-change

```yaml
- id: fault-002
  type: fault
  what: >
    Same addition as fault-001 (ID 513). The dispatch identifies ID 513 as
    carrying both vigil-extinguished and grief-debt-shape-change as "combined
    signal." The grief-debt-shape-change is the consequence: the village-claim
    mechanism now operates from a changed emotional posture (mother has stopped
    waiting; the grief has formalized into a different demand-register than beat 3).
    ID 513 "the beetles relay the base room" does not carry this relational or
    transactional state-change any more than it carries the candle. The room
    relay covers the physical space; it does not surface the change in the
    claim's emotional instrument.
  why: >
    Fault-001 and fault-002 are nominally the same physical event (mother's
    visit, beat 17) but distinct downstream constraints: the vigil-extinguished
    state affects the grief-debt arc's register for the remainder of the season;
    the shape-change means the village-claim no longer operates through
    active-wait (vigil) but through a different mechanism. W3's Hightower-apparatus
    arc (beats 18–26) operates in parallel with the village-claim arc; W3 authors
    need the village-claim's changed shape as a visible constraint or the two arcs
    will not compose correctly in the prose pass. The combined-signal approach is
    valid in principle; ID 513 is not a sufficient realization of it.
  criteria: >
    Same criteria as fault-001. If a single bone carries both the candle
    extinguishment and the grief-debt shape-change by making the state visible
    in physical register, both faults resolve together. The criteria does not
    require two separate bones — one adequate physical-register bone suffices
    if it names or makes observable the state that changed.
```

### fault-003 — maester-named — RESOLVED

```yaml
- id: fault-003
  type: pass
  what: >
    ID 514 "the beetles relay oc-broken-maester" — the slug oc-broken-maester
    is directly present in physical-register form, identical in construction to
    the naming bone at ID 310 in W2's close region ("the beetles relay oc-broken-maester").
    Placed in the first active-bone positions of W3's open, this bone makes the
    named maester an explicit active sensory contact with no ambiguity. A
    downstream author reading W3 cold immediately receives oc-broken-maester as
    a named, active entity in Taylor's beetle-relay coverage.
  why: n/a — no problem found
```

### fault-004 — wage-claim-formalized — SCOPE FLAG + FAULT

```yaml
- id: fault-004
  type: fault
  what: >
    ID 515 "taylor-hebert-flea-bottom writes the entry" is the addition intended
    to carry wage-claim operational context. The bone is a generic log-write,
    formally identical to ID 22, ID 33, ID 243, ID 263, ID 277, ID 293, ID 300,
    ID 312, ID 327 — every log-write throughout the bones file. It names no
    wage-claim, no transactional instrument, no tanner-family reference. Its
    positioning after IDs 513 and 514 implies the write integrates the two
    beetle-relays (base room and maester), not the wage-claim formalization from
    beat 13 (IDs 246–264). The wage-claim is not signaled as an active constraint
    in W3's open.

    Scope note: The wage-claim formalization (IDs 246–264, beat 13) is
    approximately 45 active bones before the W2 close region (IDs 305–328,
    last 20 active bones). The S10 Step 4 rule's stated scope is "state-changes
    in windowN's close region (last 20 bones)." Under a strict reading, the
    wage-claim is not a close-region state-change and should not have been
    fault-004 in cycle 1. If the rule is read broadly — as covering any
    season-arc-active state regardless of when in W2 it was established — then
    a carry signal is warranted. This audit treats fault-004 as valid-as-raised
    (cycle 1 returned it; no correction was made; the fix was attempted), notes
    the scope question for the orchestrator, and evaluates the addition on its
    merits.
  why: >
    If the wage-claim formalization is a boundary-carry requirement (per the
    broad reading, or because the cycle 1 verdict is authoritative), ID 515
    does not resolve it. The bone provides no wage-claim-specific signal. W3's
    opening — the Hightower-apparatus clerk scene (IDs 330–342) — initiates the
    institutional arc, and the wage-claim's dual-apparatus significance (village
    claim + apparatus file closing simultaneously around Taylor, season denouement
    structure) requires the claim to be an active constraint for the season-close
    logic to work. Under the broad reading, the omission weakens the payoff at
    beat 23 (father formalizes the claim in the lord's-man record) because W3
    readers may have lost the formalized-transactional-surface state established
    in beat 13.
  criteria: >
    If the orchestrator confirms the broad reading applies (wage-claim carries
    regardless of close-region scope): the W3 open region must contain at least
    one physical-register bone that names the wage-claim instrument, the
    tanner-family transactional surface, or the partial-payment outcome in terms
    specific enough to be legible cold. A generic log-write does not satisfy this.
    If the orchestrator rules the strict reading applies (close-region only):
    fault-004 should be reclassified as out-of-scope and this criteria entry
    withdrawn.
```

### range-at-400m — CARRIES (unchanged from cycle 1)

```yaml
- id: range-at-400m
  type: pass
  what: >
    Range-at-400m carry confirmed in cycle 1; no addition was required. ID 514
    ("the beetles relay oc-broken-maester") and the existing W3 open bones
    (344–359, winter-onset network spread) establish beetle-relay coverage
    consistent with a 400m+ operational range. This finding is unchanged.
  why: n/a — no problem found
```

---

## Verdict

**BOUNDARY-DROPS-vigil-extinguished-grief-debt-shape**

fault-003 (maester-named) is resolved. range-at-400m carries.

fault-001 and fault-002 remain open. ID 513 relays a location; it does not physically signal the vigil-extinguished or grief-debt-shape-change states as active constraints.

fault-004 remains open pending orchestrator scope ruling; the addition (ID 515) does not resolve it under either reading.

Screen-writer must supply at minimum one physical-register bone that names the candle-extinguished / grief-debt-shape-change state in a form legible without W2 context. fault-003's resolution pattern (direct slug in relay form) is the model: the same approach applied to the vigil state would satisfy fault-001 and fault-002.

---

## Archive note

Cycle 1 was delivered as an in-context assistant response; no cycle-1 file was written to disk. This cycle-2 report is the first persisted boundary audit for this boundary. No archive file action required.
