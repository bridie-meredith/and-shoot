# Audit Report — Pass 5 Continuity — Chapter 02
# target: active-project/theater/proto-lines/chapter-02.md
# auditor-fork: independent re-verify (no prior pass-4 report read)
# date: 2026-05-07
# schema: schemas/audit-report.schema.md

file_level: FAIL

---

## Summary

Three faults, one flag. The iter1 SW sparrow block (IDs 104–110) contains the most significant fault: Taylor dispatches a sparrow to the orchard from the kitchen garden — a range that exceeds the fauna-control ceiling at non-cost-onset use, and the stated cost (brief blackout/head-bow at ID 110) does not match the cost-curve the dispatched operation would actually incur under cond-fauna-control-rules. Secondary faults: the sparrow at IDs 23–26 (pre-iter1 material) is ambiguous as to whether it is Taylor-controlled, which creates an unresolved state-consistency gap; and the nosebleed at IDs 52–54 lacks a cost-onset anchor — no prior use in the chapter accumulates sufficient time to justify nosebleed-phase cost. One flag on the starlings at IDs 62–65 (potentially Taylor-controlled, no assertion either way).

---

## Findings

---

### fault-001
- **id:** fault-001
- **type:** fault
- **what:** IDs 104–110. Taylor (in the kitchen garden) dispatches a sparrow to the orchard edge, where oc-plumms-man has just entered. The sparrow lifts the orchard edge (ID 105), plumms-man turns and stills (IDs 106–107), then Taylor releases the sparrow (ID 108). This is a directed send of a small bird to a specific location followed by a held channel and deliberate release.
- **why:** The kitchen garden is Taylor's operational position throughout the chapter. The orchard is oc-plumms-man's location at IDs 104–110. Earlier in the chapter the route is: postern gate → farmstead → orchard → mill hamlet track → Harrenhal road. The orchard is explicitly placed beyond the farmstead and up a rise (IDs 32–36: mounts road, crests rise, reaches orchard boundary). In this geography the orchard is well outside Taylor's extended-concentration range (400m) and may reach or exceed the 600m maximum threshold. Under cond-fauna-control-rules: "Maximum range: Under extreme focus, range may extend to 600+ meters, but this pushes into immediate physical cost territory. Not a sustainable operational mode." The card further states: "ravens can be dispatched from her range and continue on trajectory, but she loses granular control beyond range. She can send a raven in a direction; she cannot fine-steer it after it leaves her radius." This "dispatch and lose control" rule is for ravens; sparrows receive no special long-range exception. A directed dispatch of a sparrow to a target outside the 400m concentration ceiling, followed by a held channel and deliberate release at the right moment (plumms-man stills, then Taylor releases), requires granular control at extended range. The cost on the body at ID 110 (Taylor catches the garden wall, bows head) is rendered as a brief single-beat physical event — consistent with the headache/dizziness tier (5–15 min of use), not the blackout tier. But the operation described is maximum-range + held channel + directed release, which should place cost in the immediate-physical-cost / blackout-risk territory, not the mild dizziness tier. The rendered cost and the rendered operation are incoherent: either the range is within bounds (in which case the sparrow-to-orchard dispatch is not an orchard-range operation and the geography must be revised), or the range is at maximum (in which case the cost is dramatically understated).
- **criteria:** Fixer must choose one of two resolutions: (A) establish that the orchard is within Taylor's 400m extended-concentration range by narrowing the chapter geography — the farmstead, rise, and orchard must all sit within the 400m envelope from the kitchen garden; OR (B) accept that the orchard is at maximum range, escalate the cost representation at IDs 108–110 to blackout-tier (sustained blackout or near-blackout, not a single wall-catch), and confirm the sparrow dispatch is a one-way send without fine-steer (so IDs 108 "Taylor releases the sparrow" becomes a cost-of-losing-the-channel event, not a deliberate tactical release timed to plumms-man's stillness). Option B also requires reconciling IDs 106–107 (plumms-man turns head, stills) — the causal chain implies Taylor directed the sparrow close enough to plumms-man to disturb him, which at maximum range she cannot fine-steer.

---

### fault-002
- **id:** fault-002
- **type:** fault
- **what:** IDs 52–54. "blood reaches the lip / taylor-hebert-westeros pinches the nose bridge / taylor-hebert-westeros tilts the head." This is explicit nosebleed-phase cost (cond-fauna-control-rules: "15–30 minutes of sustained use: Nosebleed onset"). The nosebleed appears after: raven dispatch and recall (IDs 7–8, 17), fly routing (IDs 18–21), and rat direction (IDs 41–44). Taylor releases the rat at ID 50, then the nosebleed presents at IDs 52–54.
- **why:** Under cond-fauna-control-rules the nosebleed phase requires 15–30 minutes of sustained use. The chapter's chapter-02 plan (a single morning's surveillance operation: "while Plumm's man completes his circuit") does not establish elapsed time clearly, but the operations are: one raven dispatch/recall (IDs 7, 17 — brief), one fly routing (ID 19 — brief transit to ditch edge), and one rat direction into a shed (IDs 41–44 — held briefly). These are three brief deployments, not a sustained 15–30 minute continuous load. Each appears to be a short-burst use with rest intervals in between (the chapter has blank-line gaps at IDs 28 and 49 suggesting pauses). The cost rendered at IDs 29–31 (stretches back, presses knuckles, presses temples) is headache-tier, consistent with the 5–15 minute phase. For the cost to escalate to nosebleed at ID 52, there must be an additional load — which the iter1 sparrow block (IDs 104–110, inserted before IDs 45–48 in chapter sequence) provides. But the sparrow block itself renders its own cost at ID 110 (wall-catch, head-bow). Two separate cost events in quick succession (IDs 108–110 and then IDs 52–54) without establishing elapsed recovery time is coherent only if the sparrow operation drove the cost from headache-phase into nosebleed-phase territory. That causal chain is not stated and is not resolvable without the sparrow block's range being confirmed as within the cost-triggering zone. The nosebleed at IDs 52–54 is either the consequence of the sparrow operation cost OR it is a separate escalation that requires a longer elapsed operational load not present in the chapter's line sequence. As written, the cause-effect chain from operation → cost is ambiguous enough to constitute a fault, not merely a flag.
- **criteria:** Fixer must either: (A) establish a continuous or cumulative elapsed-use chain from IDs 7–44 that accumulates to 15–30 minutes of sustained use (requiring elapsed-time markers in the chapter that are not currently present), making the nosebleed cost-curve consistent without the sparrow block; OR (B) confirm that the sparrow block (IDs 104–110) is the precipitating load event that drives the cost from headache-tier into nosebleed-tier, and ensure the wall-catch at ID 110 and the nosebleed at IDs 52–54 are rendered as the same continuous cost event (not two separate events), with no recovery interval between them.

---

### fault-003
- **id:** fault-003
- **type:** fault
- **what:** IDs 23–26. "oc-plumms-man turns the head / a sparrow lifts / oc-plumms-man turns / the sparrow turns." The sparrow at ID 24 lifts (apparently in response to plumms-man's head-turn — a natural startle lift), but then at ID 26 "the sparrow turns" after "oc-plumms-man turns" (ID 25). The sparrow turning in tandem with plumms-man's turn implies either: (a) the sparrow is Taylor-controlled (mirroring the human's movement), or (b) the sparrow naturally reorients after a startle. If (a), this is an undeclared fauna deployment — no prior line establishes Taylor dispatching or holding a channel to this sparrow at this location. Taylor's stated operations at this point in the chapter are: raven recalled (ID 17), fly routing active to ditch edge (IDs 20–21). No sparrow is dispatched in IDs 1–22.
- **why:** If the sparrow at IDs 24–26 is Taylor-controlled, it represents an undocumented active deployment: no dispatch line, no POV line acknowledging the channel, no cost credit. This violates state-consistency — Taylor's POV lines at this section (IDs 29–31 after the blank gap) show her pressing temples/knuckles, but those cost signals follow gap ID 28, not immediately after the sparrow moment. If the sparrow is not Taylor-controlled, then ID 26 "the sparrow turns" is a natural bird behavior and the causal chain "plumms-man turns → sparrow turns" is incidental, but the rendered sequence creates strong implied causality that will be misread as fauna-control. The proto-line format relies on SVO clarity; an ambiguous subject-verb chain where a bird "turns" directly after a human "turns" in the same scene will be interpreted as controlled behavior by downstream agents.
- **criteria:** Fixer must disambiguate IDs 24–26. Either: (A) add a Taylor-POV dispatch line before ID 24 establishing the sparrow channel (and credit the associated cost), or (B) revise ID 26 so the sparrow's behavior is clearly natural/independent (e.g., "the sparrow lifts" again on its own logic, not "turns" in apparent coordination with plumms-man).

---

### flag-001
- **id:** flag-001
- **type:** flag
- **what:** IDs 62–65. "two starlings circle the girl / the starlings drop / the starlings lift / oc-plumms-man halts." The girl rounds the road edge at ID 58 and starlings appear at IDs 62–65 in apparent coordination with her. Taylor is at this point on the sept road (ID 68 confirms she takes the sept road after wiping her lip at ID 66). Whether these starlings are Taylor-controlled or incidental is not stated.
- **why:** Starlings are in scope (cond-fauna-control-rules: "any bird without complex social cognition (sparrows, pigeons, starlings)"). If Taylor is controlling these starlings she is doing so: (a) after a nosebleed (IDs 52–54), (b) at a range consistent with the mill hamlet track location, and (c) without any dispatching line in Taylor's POV sequence. The nosebleed phase implies she has already exceeded the safe operational window; additional use at this point would push toward blackout risk. If these starlings are not Taylor-controlled their behavior (circling a child, then dropping and lifting) is remarkable enough to be noted by plumms-man (ID 65: plumms-man halts) and would constitute a wrongness-perception event independent of Taylor — which is narratively plausible but not supported by any POV acknowledgment. This is a flag rather than a fault because the chapter's goal ("show the gap between what Taylor thinks she controls and what she has left visible") makes autonomous wrongness-perception events consistent with the chapter's thematic intent. But the ambiguity is load-bearing for downstream impersonators: they need to know whether Taylor did this.
- **why it matters:** If Taylor-controlled: requires a dispatch line, an additional cost event past the nosebleed (blackout-risk territory), and a range check against her position on the sept road vs. the mill hamlet track. If not Taylor-controlled: the chapter contains a second fauna anomaly that plumms-man witnesses but Taylor does not cause — which is a thematically significant beat that should be made explicit in the chapter's design, not left ambiguous.
- **criteria (flag — fixer discretion):** Clarify in chapter notes or via a Taylor-POV line at this location whether the starlings are controlled or incidental. If controlled, add dispatch and cost; if incidental, mark clearly as "natural occurrence observed by plumms-man" in chapter notes so downstream agents do not misattribute.

---

## Boundary Checks

### ch01 → ch02 boundary

Chapter-01 (from the ch01 proto-line) closes with the census officer departing the sept yard and Taylor re-entering the cottage. Chapter-02 opens with oc-plumms-man exiting the Harrenhal postern gate and Taylor entering the kitchen garden. No state inconsistency: Taylor's presence in the kitchen garden at ch02 open is reachable from her sept cottage position at ch01 close (same location complex). oc-plumms-man's appearance as a new agent (distinct from oc-census-officer in ch01) is not flagged by any prior line — this is a new character introduction, consistent with the chapter goal (Plumm's surveillance operation). No ch01→ch02 boundary fault.

### ch02 → ch03 boundary

Chapter-02 closes with: flies dispersing, rats scattering, ravens spreading (IDs 96–99), and plumms-man setting the ledger (ID 101). Taylor's final stated position is the sept yard (ID 80) after taking the sept road (ID 68). Chapter-03 opens with Taylor descending the loft ladder (ID 1) and crossing the yard. The transit from sept yard to loft interior is not recorded in ch02 but is a short, logical interior movement — not a state-gap of significance. The chapter-03 goal ("something has closed upstream without Taylor knowing it — she senses the disturbance") is consistent with ch02 closing on plumms-man setting the ledger (report filed). No ch02→ch03 boundary fault.

---

## POV Consistency

Chapter-02 is declared Taylor POV (narrator: taylor-hebert-westeros). The proto-line file contains extensive oc-plumms-man lines with no Taylor-POV anchor — this is the chapter's structural design (the surveillance operation renders plumms-man's actions as they are observed through fauna feeds). This is consistent with prior chapters' use of third-person SVO proto-lines for observed subjects. No POV violation. The cond-fauna-control-rules 600m ceiling applies to all Taylor operations throughout — verified above in fault-001.

---

## Time Consistency

The chapter spans a single surveillance operation: plumms-man exits Harrenhal, visits farmstead and orchard, passes mill hamlet, returns to Harrenhal, and files the ledger. Taylor holds position at the kitchen garden/sept complex throughout. The elapsed time is consistent for a half-day circuit (postern gate → farmstead → orchard → hamlet track → return). No internal time contradictions detected.

---

## Reachability

All actor positions in chapter-02 are reachable from chapter-01 close states. oc-plumms-man is introduced from Harrenhal (consistent with the established presence of Hatch's administrative apparatus). Taylor's kitchen garden position is consistent with her sept-complex base. The girl at the mill hamlet track (IDs 58–65) is unnamed and incidental — her reachability is not bounded by a state file; no fault.

---

## State Persistence

The ledger in oc-plumms-man's possession is consistent throughout the chapter — marked at the farmstead (IDs 16, 27), closed at the orchard (ID 48), re-opened for the girl notation (IDs 69–72), and set in the garrison hall (ID 101). Prop chain is internally consistent. Taylor's rain-barrel position (ID 52) is consistent with the kitchen garden / sept-exterior complex. The raven at ID 6 (shifts), released at ID 7, recalled at ID 17 — this three-beat sequence (shift, release, recall) is internally coherent. The fly dispatched at IDs 19–21 is not recalled — it reaches the ditch edge and is not mentioned again, which is consistent with a brief surveillance send that runs to its range limit. No state persistence faults beyond those already captured in fault-001 through fault-003.

---

## Reference Resolution

All actors referenced in chapter-02 (taylor-hebert-westeros, oc-plumms-man) resolve to established agents. The girl (IDs 58–65, 73) is unnamed — no card reference required for an incidental non-speaking figure. All locations (kitchen garden, farmstead, orchard, mill hamlet track, garrison hall) are consistent with the Harrenhal / sept-environs geography established in chapter-01 and the studio LTM. No unresolved references.

---

## ID Sequence Note

Chapter-02 contains non-monotonic IDs due to the iter1 SW insert: IDs 104–110 are inserted between ID 44 and ID 45 in body order. The chapter header documents this ("IDs are non-monotonic in body order" — this note is absent from ch02 but present in ch03; ch02 does not carry this explicit note). This is not a continuity fault but is a process flag: the ch02 proto-line file does not carry a non-monotonic sequence warning comparable to ch03's header note, yet the sequence jump from ID 44 to IDs 104–110 and back to ID 45 is potentially confusing for the stitcher. Recommend adding a header note matching the ch03 pattern.

---
