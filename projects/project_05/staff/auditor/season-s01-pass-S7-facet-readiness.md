---
report: season-audit-pass-S7-facet-readiness
scope: season
target: s01
pass: S7
timestamp: 2026-05-11
cycle: 3
verdict: FACET-GAPS-1
---

# Season s01 — Pass S7 Facet Readiness Audit — Cycle 3

## Cycle history

| Cycle | Verdict | Blocking faults |
|-------|---------|-----------------|
| 1 | FACET-GAPS | fault-001 (beat 10 bone density), fault-002 (time-skip cluster) |
| 2 | FACET-GAPS | fault-001 (beat 10 bone density), fault-002 (time-skip cluster) |
| 3 | FACET-GAPS-1 | fault-001 partially resolved (Watch-timing routing bone still absent) |

---

## Cycle-3 changes evaluated

Three bones were inserted:

- **ID 525** `the flies relay the reeve` — inserted between blank line 70 and bone 71.
- **ID 526** `taylor-hebert-flea-bottom enters the market-side junction` — inserted in beat 10, after bone 500 (log close) and before bone 508 (elder pauses).
- **ID 527** `oc-tanner-elder faces taylor-hebert-flea-bottom` — inserted in beat 10, after bone 502 (wasps relay the pass) and before bone 510 (carter exits junction).

---

## Finding 1 — fault-001: Beat 10 bone density (PARTIALLY RESOLVED)

**Prior criteria (3 anchors required):**
1. Movement bone placing Taylor at a chain node location during the three-week period.
2. Routing-action bone representing Watch-movement timing information passing through the chain (parallel structure to bone 200 weather relay).
3. Social-context bone representing an ambient chain-node interaction.

**Cycle-3 evaluation:**

**Criterion 1 — Movement bone:** ID 526 `taylor-hebert-flea-bottom enters the market-side junction` physically places Taylor at the chain node within the three-week window. SATISFIED.

**Criterion 2 — Watch-movement timing routing bone:** No bone added by cycle 3 addresses this. The full beat 10 substantive bone list after cycle 3 is: 187 (flies relay elder), 190 (wasps relay dock-runner), 195 (Taylor enters base), 509 (flies relay the carter), 200 (flies relay the wind), 500 (log close), 526 (Taylor enters junction), 508 (elder pauses), 501 (elder speaks to carter), 502 (wasps relay the pass), 527 (elder faces Taylor), 510 (carter exits junction). None of these bones represents a Watch-movement timing relay as a distinct routing strand. Bone 190 (`the wasps relay oc-dock-runner`) is a dock-runner relay, not Watch movement. Bone 502 (`the wasps relay the pass`) is ambiguous — in context (following elder-speaks-to-carter at 501 and preceding carter-exits at 510), "the pass" reads as information or goods passed in the carter interaction, not Watch patrol movement. The parallel-to-bone-200 requirement (a routing-action bone for Watch-movement timing that establishes Taylor as actively routing Watch intelligence through the chain, not merely receiving weather data) remains unmet. NOT SATISFIED.

**Criterion 3 — Social-context bone:** ID 527 `oc-tanner-elder faces taylor-hebert-flea-bottom` — the elder faces Taylor within the context of the elder-carter interaction sequence (508 → 501 → 502 → 527 → 510). This is an orientation-acknowledgment bone from a named chain node (elder) toward Taylor, occurring at the market-side junction where Taylor is now physically present (bone 526). The criteria permitted "an observed interaction bone" without requiring a `speaks to` form. The elder's face-toward-Taylor in this sequence is a social-context acknowledgment that places Taylor as a recognized presence at the chain node during the three-week operational window. SATISFIED.

**Fault-001 verdict: PARTIALLY RESOLVED.** Criteria 1 and 3 are met. Criterion 2 (Watch-movement timing routing bone) remains unaddressed. Fault-001 carries forward as a blocking fault for facet authors of tensometer and NI at beat 10.

---

## Finding 2 — fault-002: Time-skip cluster density (PARTIALLY RESOLVED)

**Prior status:** Four consecutive time-skip markers (189, 191, 193, 194) flanked by only two thin relay bones (187, 190) left the stitcher with near-zero material between breaks for a three-week load-bearing beat.

**Cycle-3 evaluation:** Bones 526 and 527 are placed after the log sequence (205-207) and the existing bones 500/508/501/502/510, all of which follow the time-skip cluster. The time-skip cluster itself (189, 191, 193, 194) is unchanged — no bones were added within or between those four skip markers. The additions appear after bone 500 (log close following bone 204 time-skip), so they materially enrich the tail of beat 10 but do not address the front-cluster density gap. The four-break cluster at bones 189/191/193/194 with only bones 187 and 190 as substantive material between and around them remains unchanged.

However: fault-002's criteria stated that "the bones identified in fault-001 would satisfy this requirement — fault-001 and fault-002 have the same fix target." Two of the three fault-001 bones (526 and 527) add substantive material to beat 10 overall, reducing the starkness of the ratio problem even though they do not land within the early-cluster gap. The Watch-timing bone (fault-001 criterion 2), if added within or adjacent to the early cluster (between the 4 time-skips), would complete fault-002's fix as well.

**Fault-002 verdict: PARTIALLY RESOLVED.** Beat 10's overall substantive bone count has increased; the tail of beat 10 now has sufficient material for the elder-at-junction scene. The early time-skip cluster (189/191/193/194) with only bones 187/190 flanking it remains thin. Fault-002 is contingent on fault-001 criterion 2: adding the Watch-timing routing bone within or adjacent to the early cluster would close this fault simultaneously.

---

## Finding 3 — fault-004: Beat 5 bones 71-77 POV-distance marker (RESOLVED)

**Prior status:** No POV-marker or relay-bone preceded bone 71 (lord's man enters village), leaving narrator-interest and sensory facet authors without a signal that bones 71-77 are network-mediated, not direct-POV.

**Cycle-3 evaluation:** ID 525 `the flies relay the reeve` is placed between blank line 70 and bone 71. The flies are tracking the reeve at the point the lord's man arrives and speaks with him. This is a relay bone — the flies cover the reeve, and through the reeve the encounter with the lord's man. This satisfies the fault-004 criteria: "A POV-distance marker or a relay-bone should precede bone 71 to signal that the lord's-man sequence is not direct-POV observation." The relay-bone form (network coverage of the reeve, not direct presence in the village street) correctly signals mediated access. Narrator-interest and sensory facet authors now have a bone establishing the mechanism (fly relay via the reeve) before the lord's-man sequence opens.

Note: bone 525 establishes relay-of-the-reeve, not relay-of-the-lord's-man directly. The fly network's coverage of the reeve as the lord's man approaches gives Taylor network-proximity to the encounter, not direct observation. This matches the plan's statement that Taylor learns of the lord's man's visit indirectly; the relay-via-reeve mechanism is consistent with the insect-network's operational logic (the insects track a known person — the reeve — who then enters proximity with the lord's man). NI and sensory authors should treat bones 71-77 as network-mediated via the reeve, not as a Watch-relay of the lord's man himself.

**Fault-004 verdict: RESOLVED.** Flag converts to advisory note for NI and sensory authors: the mechanism is fly-relay-of-reeve, so Taylor's access to bones 71-77 is through the reeve's movements, not direct observation of the lord's man.

---

## Remaining faults and flags (carry forward from cycle 1)

The following findings are unchanged and carry forward from the cycle-1 report. They are not re-audited in cycle 3; their status is unchanged.

```yaml
audit:
  scope: season
  target: s01
  pass: S7-facet-readiness
  cycle: 3
  timestamp: 2026-05-11
  verdict: FACET-GAPS-1
  findings:

    - id: fault-001
      type: fault
      what: >
        Beat 10 (bones 187-207 + inserted 509, 510, 526, 527, 500, 508, 501, 502): Watch-movement timing
        routing bone still absent. Criteria 1 (movement bone — bone 526 SATISFIED) and 3 (social-context
        bone — bone 527 SATISFIED) are met. Criterion 2 (Watch-movement timing routing bone parallel to
        bone 200 weather relay) remains unaddressed after cycle 3.
      why: >
        Beat 10 is the season's operational integration beat: Taylor is routing Watch-movement timing
        anonymously through the chain alongside weather-pattern data. Bone 200 anchors the weather-data
        strand; no bone anchors the Watch-timing strand. Tensometer and NI facet authors have no anchor
        for this operational strand, which the plan identifies as the beat's second routing activity.
        Without this bone, beat 10 renders as weather-relay-only for a beat the plan describes as
        dual-routing.
      criteria: >
        One bone must be added to beat 10 that represents Watch-movement timing information passing
        through Taylor's chain. The bone should parallel bone 200's structure (a relay or routing action
        for timing data). Placement within or adjacent to the early time-skip cluster (ideally between
        bones 189-194 or near bone 190) would simultaneously address fault-002's early-cluster gap.
        Alternatively, placement before the log sequence at bones 205-207 is acceptable if the early
        cluster cannot absorb it.

    - id: fault-002
      type: fault
      what: >
        Beat 10 early time-skip cluster (bones 189, 191, 193, 194 — four consecutive time-skip markers)
        with only bones 187 and 190 as substantive flanking material. Cycle-3 additions (526, 527) land
        in the tail of beat 10, not within the early cluster. Early cluster density unchanged.
      why: >
        The stitcher renders four consecutive time-skip markers as four break signals with minimal
        intervening content. Bones 526 and 527 enrich beat 10's tail; the early cluster still presents
        four breaks between bones 187 and 195 with only one relay bone (190) between them.
      criteria: >
        Same fix target as fault-001 criterion 2. The Watch-timing routing bone, if placed within or
        adjacent to the early cluster, resolves both faults in one pass. One fixer pass closes both
        fault-001 and fault-002 simultaneously.

    - id: fault-003
      type: flag
      what: >
        Range-expansion state-change (beats 11, 14, 19, 24) has no explicit actor-state bone in any
        expansion beat. Protagonist's insect-control range field changes in each beat but no bone
        names this as a state event.
      why: >
        State-updates facet author must infer range-expansion state-change from perimeter-walk bones
        and network-spread bones. Inconsistent inference across four beats may produce write-back
        inconsistencies at the memory-write phase.
      criteria: >
        State-updates author must be briefed that perimeter-walk bones (222, 270, 351, 445) and
        new-geography spread bones are the intended range-expansion anchors. If the author cannot
        resolve the range field consistently from this pool, a single state-annotation bone per
        expansion beat must be added. Resolution is author-call first; fixer only if author flags
        inability to resolve.

    - id: fault-004
      type: pass
      what: >
        Beat 5, bones 71-77 POV-distance marker. ID 525 (the flies relay the reeve) inserted before
        bone 71. Resolved in cycle 3.
      why: N/A — resolved.
      criteria: >
        Advisory note for NI and sensory authors: bones 71-77 are network-mediated via fly-relay-of-reeve,
        not direct-POV observation. Authors should treat Taylor's access to the lord's-man sequence as
        insect-relay through the reeve's movements.

    - id: fault-005
      type: flag
      what: >
        Beat 8, bone 144: single time-skip marker for a plan-specified two-day elapsed interval between
        the Watch/runner incident (bones 141-143) and the dock-runner approach via elder (bones 145-155).
      why: >
        Location-state and NI authors may not distinguish the two sub-beats as temporally separated by
        two days, potentially rendering them as a continuous scene.
      criteria: >
        Advisory. If Phase 7 episode-boundary assignment places a break between bones 143 and 145,
        the two-day gap is resolved structurally. If not, the single time-skip at 144 should be expanded
        to two consecutive time-skip markers per schema convention for longer skips.

    - id: fault-006
      type: flag
      what: >
        Beat 25, bones 463 and 472: two `taylor-hebert-flea-bottom holds the feet` bones in one beat.
        Feeling schema per-character per-scene cap is <= 1 (hard).
      why: >
        If beat 25 is one scene, the feeling author must select one of 463/472. Selecting bone 463
        leaves the beat's second half without a Taylor-feeling anchor after the account is sealed.
        Selecting bone 472 leaves the approach sequence without a Taylor-feeling anchor.
      criteria: >
        Phase 7 episode-boundary assignment should determine whether bones 455-463 and 465-475 fall
        in the same episode or separate episodes. If separate, per-scene cap allows both to fire.
        If same episode, the feeling author must choose one and document the selection.

    - id: fault-007
      type: flag
      what: >
        Beat 7, bone 111 (maester speaks to room): tensometer author must evaluate whether ambient
        overheard speech clears the rubric's 2-threshold. Rubric states "Speaking is by itself a 1."
        If bone 111 does not clear, beat 7 has no escalation bones and requires a dramatist
        scene-as-transit flag.
      why: >
        If tensometer assigns bone 111 as a 1 without a scene-as-transit flag, the stitcher treats
        the entire beat as compressible — including the first maester-detection event. Compressing
        the discovery is a narrative structure fault.
      criteria: >
        Tensometer author must evaluate bone 111 on the rubric's 2-threshold and document the
        axis-citation. If 111 does not clear, assign 1 and flag bone 111 for dramatist scene-as-transit
        exemption. Silent assignment of 1 without review is not acceptable.

    - id: fault-008
      type: flag
      what: >
        Beats 1-4 (bones 1-60): no explicit location slug in any bone for the tanner-village setting.
        Character slug is taylor-hebert-flea-bottom throughout, identifying character by destination-city.
      why: >
        Location-state facet author for beats 1-4 must infer loc-tanner-village from context, not from
        any cited loc slug. Incorrect slug propagates to stitcher rendering (wrong set, wrong conditions).
      criteria: >
        Location-state author must be briefed that beats 1-4 are set in loc-tanner-village (per
        showrunner memory stage-elements). If loc-tanner-village is not in the active warehouse loc
        cards, Margit must be notified to onboard the card before location-state authoring begins.
```

---

## Verdict

**FACET-GAPS-1**

One blocking fault remains: the Watch-movement timing routing bone for beat 10 (fault-001 criterion 2). Faults 001 and 002 share a single fix target — one bone added to beat 10 (preferably within or adjacent to the early time-skip cluster at bones 189-194) closes both simultaneously.

Fault-004 is resolved by bone 525. The remaining six advisory flags (003, 005, 006, 007, 008, and the advisory note on 004) do not block facet authoring for any beat other than beat 10.

The 25 beats other than beat 10 are FACET-READY. Beat 10 is FACET-GAPS pending one bone addition.

---

## Archived — Cycle 1 and 2 verdict summary

**Cycle 1 (2026-05-11):** FACET-GAPS. Two blocking faults: fault-001 (beat 10 missing 3 anchors) and fault-002 (early time-skip cluster). Six advisory flags (003-008).

**Cycle 2 (2026-05-11):** FACET-GAPS. Same two blocking faults; no bones added in cycle 2 (cycle 2 was the sweep-A pass that defined the fault structure; cycle 3 is the first fix cycle). Six advisory flags unchanged.
