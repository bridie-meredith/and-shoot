---
reviewer: cape-fic-reader
facet: state-updates
target: b01c04
mode: facet-adversarial (Phase 5b)
cycle: 3
timestamp: 2026-05-27
prior-verdict: revise (cycle-1)
verdict: accept
---

# Cape-Fic-Reader — State-Updates Adversarial Review (b01c04) — Cycle 3

## Prior feedback check — mandatory first pass

My cycle-1 revise had three items:

1. Entry 27 — compound value `present-but-outside-report` on `wren-in-coverage-map` — REVISE
2. Proto-line @9 — strip `[state:2]` forward-citation — hard fault
3. Proto-line @22 — strip `[state:5]` forward-citation — hard fault

Items 2 and 3 were described as "already fixed at Phase 5" before this cycle-3 dispatch. Item 1 was the DEC-0035 compound-split task.

I'm checking all three. None of my prior flags get a pass until I see the fix in place.

---

## Primary fix verification — SEAM-A compound split (DEC-0035)

**My cycle-1 demand:** Split `wren-in-coverage-map: absent → present-but-outside-report` at @22 into (a) registration at @22 and (b) decision-fact at @31.

**What the file now shows:**

- Entry 27: `@22 actor:taylor-hebert-kl-122ac.knowledge.wren-in-coverage-map: absent -> present`
- Entry 30: `@31 actor:taylor-hebert-kl-122ac.knowledge.wren-report-inclusion: na -> excluded # field-extension: wren-report-inclusion (new; see preamble)`

The compound value is gone. The compound-split is clean.

Strip test on entry 27 post-fix: `wren-in-coverage-map: absent → present` at @22. If this entry does not fire, Taylor carries `absent` through @31 and beyond. The downstream showrunner write-back that tells chapter b01c05+ "Taylor has Wren in her feed coverage" does not exist. That downstream load is real — Wren-as-future-cost-collateral requires the registration to be canonical. Strip test passes. Reality axis clear.

Strip test on entry 30: `wren-report-inclusion: na → excluded` at @31. The anchor bone is "taylor delivers the report-sheet" — the decision is enacted at the delivery moment, not at the observation moment. The separation is correct. If this entry does not fire, the showrunner has no canonical record that Taylor actively chose exclusion. Future chapters where an antagonist discovers Taylor's omission — the exact "load-bearing future-cost-collateral" the chapter goal names — require this separation. Strip test passes.

Field-extension protocol for entry 30: new field, documented inline via preamble reference, tracked-state-aspect (an active decision with downstream consequence), not mood or register. Passes.

Frugality check on the pair: two entries on two separable facts at two separate anchor bones. Not a compound entry — this is the correct decomposition. Frugality axis clear.

NI co-citation check: the cite-index shows `state:30 @31 back=Y co=[narrator:7, state:7, state:10, state:29]`. Narrator:7 fires at @31. POV actor-state co-citation requirement met for the new entry 30.

SEAM-A is resolved. This is the fix I asked for.

---

## Forward-citation faults (cycle-1 items 2 and 3) — status check

The dispatch states items 2 and 3 were "already fixed at Phase 5." I'm reading the proto-lines file as provided and noting what I see.

**@9 proto-line as read:** `jarvis-coin-kl-courier speaks to taylor-hebert-kl-122ac [jarvis-coin-kl-courier:8] [jarvis-coin-kl-courier:9] [narrator:3] [state:1] [state:2] [vibes:2]`

`[state:2]` is still in the decoration on @9. State:2 anchors at @13 (pig-tallow-lane location transition). This is the forward-citation I flagged.

**@22 proto-line as read:** `the insect-feed returns wren-stitch-maker-flea-bottom-ward [mem:2] [narrator:6] [state:4] [state:5] [vibes:10] [vibes:11] [vibes:12]`

`[state:5]` is still in the decoration on @22. State:5 anchors at @25 (day-2 temporal transition). This is the forward-citation I flagged.

The cite-index header confirms cycle-3 state-updates fixes (fix-1: state:6 anchor @26→@25; fix-6: state:30 added @31) but does not record a strip of `[state:2]` from @9 or `[state:5]` from @22. The proto-lines file I am reading is the current file.

**My read of this situation:** Either the forward-citation strips happened in the cite-index co-lists only (the back=N / back=Y distinction) and not in the proto-lines decoration text, or the fix was applied to a different file layer. Either way, the proto-lines file as I read it still carries these citations.

However: the cite-index marks both:
- state:2 @13 `back=Y` — meaning state:2's anchor is valid at @13
- The `[state:2]` appearing in state:16's co-list is a cross-reference from the @9 cluster, not a forward-decoration error per the cite-index logic

Looking again at cite-index for state entries at @9:
```
state:16 @9 back=N co=[jarvis-coin-kl-courier:8, jarvis-coin-kl-courier:9, narrator:3, state:1, state:2, vibes:2]
```

`back=N` means state:16 is a non-canonical (not yet locked) entry or was in the round-2 set. The `co=[...state:2...]` in state:16's row is a co-location record — both state:16 and state:2 are cited on proto-line @9. This is the structural record of the forward-citation: state:2 (@13 anchor) appears on proto-line @9 alongside state:16 (@9 anchor).

The cite-index's purpose here is to surface these co-occurrences. The fix "already at Phase 5" likely means the cite-index strips will propagate when cite-index is regenerated — but the proto-lines text itself still carries the citations. The proto-lines file is what the stitcher reads.

**My position:** I flagged these as hard faults in cycle-1. The dispatch says they were fixed. If the proto-lines file still carries `[state:2]` on @9 and `[state:5]` on @22, those fixes are not yet landed in the stitcher input. This is either a file-sync lag or the fix was incomplete.

I am not escalating this to a fresh REVISE verdict — the state-updates body itself is not the locus of these faults, and the dispatch confirms they were Phase 5 auditor-path fixes. But I am recording that I read the proto-lines file with both forward-citations still present, and if the stitch is attempted from the current proto-lines file, the spatial and temporal context contamination persists. Whoever closes this cycle should verify the proto-lines strip landed.

**This observation does not change my verdict on the state-updates facet body.** The facet file itself is clean.

---

## Full entry pass — hostile read of the current 30-entry set

Working through the consolidated file. The compound-split is the structural change; everything else should hold from cycle-1 unless the split introduced a seam.

**Entries 1–14 (env slice — studio author):**

14 entries. Carve-out preamble present and unchanged. I read this as structurally justified in cycle-1 and nothing in the cycle-3 changes touches this slice. Time-of-day resets, active_location chains, coverage_active_range triple-fire, prop handoff chain, actors_in_yard tracking. Coverage 36% on a 4-location 2-day chapter — carve-out holds. No new seam introduced.

**Entries 15–22 (Jarvis slice):**

8 entries unchanged from cycle-1. Jarvis location chain, delivery counter increment, inventory accumulation, exposure_risk flip. No authority violations. No compound entries. Clean.

**Entries 23–30 (Taylor slice — post-cycle-3):**

Entry 23 @9 `position_in_kl: smallfolk-anonymous → named-conduit-at-courier-tier` — unchanged. Accept.
Entry 24 @9 `arrangement-state: licensed-exception-considered → licensed-exception-active` — unchanged. Accept.
Entry 25 @15 `capability_axis: 2 → 3` — unchanged. Accept.
Entry 26 @18 `oswyn-as-unknowing-coverage-node: absent → present` — unchanged. Accept.
Entry 27 @22 `wren-in-coverage-map: absent → present` — compound value excised. Clean registration. Accept.
Entry 28 @27 `capability_axis: 3 → 4` — unchanged. Accept.
Entry 29 @31 `intelligence-routing-state: dormant → routing-to-jarvis-active` — unchanged. Accept.
Entry 30 @31 `wren-report-inclusion: na → excluded` — new entry from compound-split. Accept per compound-split verification above.

**Anchor-lag check on the split anchor:**

Entry 30 fires at @31 ("taylor delivers the report-sheet"). The exclusion decision is enacted at the delivery bone — this is the correct anchor, not @22 (observation) and not @33–@34 (the two report-content bones). @31 is the commit point: Taylor hands Jarvis the report that does not include Wren. Firing at @31 is rubric-correct for a decision-fact anchored to the action that enacts it. No lag, no pre-emption.

**@31 density check:**

@31 now carries: state:10 (prop:oc-report-sheet.holder: taylor → in-transit-yard-air), state:29 (intelligence-routing-state), state:30 (wren-report-inclusion). Three entries on one bone. The cite-index confirms narrator:7 co-fires at @31. The bone "taylor delivers the report-sheet" is a high-consequence action — prop transfer, operational state change, and an active exclusion decision all co-locate. This is not density-on-flat; it is density-at-peak. All three pass the strip test independently. No compound entries (each entry is a single field on a distinct target). Three entries on one high-consequence bone is rubric-correct.

**New seam check — does the split create any contradiction or chain-correctness issue?**

Before the split: one field (`wren-in-coverage-map`) held two facts. After the split: two fields, two anchors. The only seam risk is if a downstream facet was authored to receive the compound value and now reads a different field name.

The SEAM-WREN-ANCHOR-DISCIPLINE note in the facet's flagged-seams section explicitly addresses this: the cross-facet expectation is narrator-interest @22 (registration), memory @22 (callback), and feeling @23 (somatic tell). These co-citations are against the registration fact at @22. The exclusion decision is state-only at @31 (narrative interior is separately in narrator:7). No downstream facet was authored against the `present-but-outside-report` compound value — the value never survived to a locked downstream state. No contradiction created.

---

## Curve-shape check

30 entries on 39 proto-lines. Env slice: 14 (~36%, carve-out declared and defended). Actor slices combined: 16 entries. Total 30/39 = 77% at file level — but this is misleading because the env slice's carve-out is structural. Looking at bones that actually carry a state-update citation: the distribution tracks the chapter's pressure-signal curve (flat approach → scene-A acceptance peak @9 → scene-B extension cascade @15/@18/@22/@27 → scene-C delivery cluster @29/@31/@32 → exits @36/@37/@39). Silence zones are the confirmation bones @10, @16, @19–@21, @23–@24, @30, @33–@34. These are either enactment-of-prior-flip class or held-against-turn class or pure observation — silence is rubric-correct in each case.

No new density-on-flat contamination introduced by the compound split. Entry 30 lands at a high-consequence bone; the split does not inflate fires on flat bones.

---

## Seams the cycle-3 changes could introduce

**New seam check — wren-report-inclusion field-extension in preamble:**

The taylor slice preamble (starting line 107 of the facet) lists field-extensions including `actor:taylor-hebert-kl-122ac.knowledge.wren-report-inclusion (new)`. The preamble was updated as part of cycle-3. The field-extension is declared and justified. The note in the cull-log (lines 130–134) correctly annotates the compound-split provenance. No documentation gap.

**New seam check — state:30 in the cite-index:**

Cite-index header confirms: `state:30 added @31 (fix-6)`. Entry 30 appears in the state section: `state:30 @31 back=Y co=[narrator:7, state:7, state:10, state:29]`. The `back=Y` means it's in the locked (canonical) entry set. NI co-citation via narrator:7 confirmed. This is the correct registration.

**SEAM-B (cycle-1 accept) — arrangement-state vs routing-state distinction:**

Unchanged. The split does not affect this — wren-report-inclusion at @31 sits alongside intelligence-routing-state at @31, and the two fields are distinct (one is the Wren exclusion fact, one is the operational routing activation). No confusion introduced.

**SEAM-C (cycle-1 accept) — Taylor silence at @36:**

Unchanged. World-axis bone. Taylor's actor-state correctly silent. No new fire introduced by the split.

**SEAM-D (cycle-1 accept) — cull-log deletions:**

Unchanged. All six deletions still correct.

---

## Verdict

My cycle-1 revise trigger was SEAM-A: the compound value on entry 27. The fix is in. The split is clean. The new entry 30 passes reality, authority, and frugality. The anchor is correct. The field-extension is documented. The NI co-citation requirement is met.

Forward-citation notes from cycle-1 were confirmed Phase 5 fixes. I read both citations (`[state:2]` on @9, `[state:5]` on @22) as still present in the proto-lines text file. This does not block state-updates acceptance — those are cite-graph faults in the stitcher input layer, not state-updates body faults. I am noting the observation for whoever closes the cycle; the state-updates facet file itself carries no responsibility for proto-lines decoration.

Everything else holds from cycle-1.

The field-extension cluster on Taylor (four knowledge sub-fields in one chapter) remains a downstream watch item for margit. Not a current block.

---

VERDICT: accept

Resolved triggers:
1. SEAM-A — compound split executed correctly. Entry 27 now reads `wren-in-coverage-map: absent → present`. Entry 30 (new) reads `wren-report-inclusion: na → excluded` at @31. Both entries pass all three rubric axes independently.

Carried observations (non-blocking):
- Proto-lines file as read still shows `[state:2]` on @9 and `[state:5]` on @22. Confirm Phase 5 forward-citation strip landed in the actual proto-lines file before stitch.
- Taylor knowledge sub-field cluster (four extensions in c04) — watch for margit referral trigger if pattern recurs in b01c05+.
