# Audit Report — Chapter 04 Proto-lines, Pass 5 Continuity
schema: audit-report
run: pass5-continuity
target: active-project/theater/proto-lines/chapter-04.md
auditor-fork: fresh (independent re-verify; no prior-pass carry-in)
date: 2026-05-07
axes: reachability | state-persistence | reference-resolution | POV-consistency | time-consistency | cause-effect | ch03→ch04 boundary | ch04→ch05 boundary

---

## Summary

| Metric | Result |
|--------|--------|
| file-level verdict | FAIL |
| Total lines checked | 102 (including line 99 as a fourth denouement beat) |
| PASS | 94 |
| FAULT | 3 |
| FLAG | 2 |
| ESCALATE | 0 |

---

## Special-focus items

### ID 53 adjudication — `a raven perches taylor-hebert-westeros`

**Iter2 mechanic advisory:** flagged as advisory (not fault) in prior mechanical pass; deferred to continuity layer.

**Continuity adjudication:** PASS. The beat holds at continuity layer.

Reachability: the raven descends at ID 52 (`a raven descends the bell tower`). The bell tower is established as a raven roost from chapter-01 and is within the yard at Harrenhal sept-environs. The descent and perch are sequentially reachable from that roost; no location gap.

State persistence: cond-fauna-control-rules is active throughout chapter-04. The raven descending and landing on Taylor is the chapter's load-bearing involuntary-disclosure beat — the fauna-control condition explicitly anticipates observable anomaly as the chapter's intended event (per pass-2 constraint check, confirmed). The bird's behavior is within the cost envelope established by the condition card.

Reference resolution: `taylor-hebert-westeros` is the named landing target. The verb `perches` takes `taylor-hebert-westeros` as its object; the implied SVO is `a raven perches [on] taylor-hebert-westeros`. This is the same licensed elision as `a raven perches [on] the sill` — the location/target is the direct object. The construction is acceptable within the file's established object-elision conventions. No reference gap.

Witness anchoring: oc-castellan-harrenhal and ser-harwick-plumm are both confirmed in the yard at this point in the sequence (IDs 40–50 establish their yard position; neither has exited). ID 56 (`oc-castellan-harrenhal steps back`) and ID 57 (`ser-harwick-plumm grips the stylus`) confirm both witnesses are present and reactive at ID 53's landing. The castellan witnesses the perch. Plumm marks the page (IDs 60–61). The involuntary-disclosure beat is structurally fully witnessed.

POV: Taylor is in the yard from ID 26 (`taylor-hebert-westeros exits the nave`). Her position is not displaced between 26 and 53. The raven landing on her arm is self-observable and Taylor-POV-accessible. No POV fragmentation at ID 53.

**Verdict: ID 53 passes continuity review. Involuntary-disclosure beat is structurally sound. No fault. Advisory from iter2 mechanic is retired.**

---

### Plumm's rolled page — acquisition anchor and end-of-chapter possession

**Tracking scope:** IDs 45–81.

**Acquisition chain:**
- ID 45: `ser-harwick-plumm opens the satchel` — satchel introduced as Plumm's carry-in prop. The satchel is a valid carry-in for an inspection officer; chapter-04 is its point of introduction. No prior chapter records a satchel in Plumm's inventory and no prior chapter strips it. Pass-2 flag-001 (lines 45–47) deferred prop-chain verification to pass 5. Plumm's state.md records the rolled page at ch04 lines 80–81 as a named chain-of-custody item (prop-rolled-inspection-page). Plumm's state.md does not record the satchel as a named prop, only the resulting roll. The satchel is a vessel, not a consequential prop itself. No fault on the satchel introduction.
- ID 46: `ser-harwick-plumm produces a page` — page produced from satchel. Clean transitive production beat.
- ID 47: `ser-harwick-plumm produces a stylus` — stylus produced from satchel. Clean.
- IDs 57–61: Plumm grips stylus, speaks, raises page, marks page. Page and stylus are in his hands from ID 46–47 through ID 61 without any intervening line that transfers or drops them. Sequence is unbroken.
- ID 75: `ser-harwick-plumm lifts the stylus` — this is the pass-2 fixer recast of the former `completes the sketch`; the stylus lift marks the sketch's end. Stylus in hand from ID 57 through ID 75; no gap.
- ID 76: `ser-harwick-plumm presents the page` — page held from ID 46 through ID 76; no intervening transfer or drop. Page is in Plumm's hand.
- ID 77: `oc-castellan-harrenhal takes the page` — castellan receives the page from Plumm. Transfer is clean: Plumm presents at 76, castellan takes at 77. Page leaves Plumm's hand.
- ID 78: `oc-castellan-harrenhal turns the page` — castellan holds and handles the page.
- ID 79: `oc-castellan-harrenhal returns the page` — page returned to Plumm. Re-transfer is clean.
- ID 80: `ser-harwick-plumm rolls the page` — Plumm rolls it in hand. Page confirmed back in Plumm's possession from ID 79.
- ID 81: `ser-harwick-plumm pockets the roll` — roll pocketed. Acquisition complete.

**End-of-chapter possession:** Plumm exits the yard at ID 93–94 (riders mount, take the north track). No line between ID 81 and ID 94 shows the roll leaving Plumm's possession. Plumm's state.md confirms: `prop-rolled-inspection-page (ch04 line 80-81): pockets the roll` and is carried through chapter-05 and into the administrative contest. Possession is properly anchored within chapter-04 and confirmed in Plumm's state file.

**Verdict: Plumm's rolled page acquisition chain is fully anchored. All transfers in the chain are sequential and unbroken. The prop is in Plumm's possession at chapter end. No fault.**

---

## Faults

---

### fault-001

- **id:** fault-001
- **type:** fault
- **class:** FAULT-CONTINUITY-POV
- **lines:** 32–35
- **content:** `a shadow crosses the cottage window` / `a book scrapes the cottage shelf` / `oc-castellan-harrenhal speaks to ser-harwick-plumm` / `the book strikes the cottage shelf`
- **what:** These four beats are cottage interior events. Taylor exited the nave at ID 26 and was established in the yard from that point. No beat between ID 26 and ID 32 relocates Taylor to a position from which the cottage interior is accessible to her POV. A shadow crossing a window is exterior-observable from the yard. A book scraping a shelf and the subsequent thump (ID 33, 35) are auditory events that could propagate through an open door or window — however, ID 29 establishes that Plumm opens the cottage door (the beat that grants interior access), and IDs 30–31 show oc-castellan-harrenhal and ser-harwick-plumm entering. Whether the door remains open after their entry is not stated. More critically, ID 34 (`oc-castellan-harrenhal speaks to ser-harwick-plumm`) is a direct speech beat rendered at the SVO level — in first-person Taylor POV, a direct speech beat from an interior room is not accessible unless the door is explicitly open and auditory range is established. This beat is inside the cottage and Taylor is not.
- **why:** Pass-3 shape audit (ch04-pass3-shape.md) flagged this block explicitly: "Cottage interior beats — Taylor cannot observe these from the yard. Recast as exterior-observable (sounds through open door / inferred from emergence / visible activity at windows) or cut." That flag specified this as a structural requirement before advance. The chapter-04 file in its current post-fixer state has not had these beats recast. The pass-3 verdict was TRANSITIONS-NEEDED with a recast requirement on this block. This is a continuity POV violation that has not been resolved by fixer: IDs 32–35 remain in the file in their original form, describing interior cottage events from a narrator who is exterior to the cottage.
- **criteria:** Fixer must recast IDs 32–35 to be exterior-POV-accessible from the yard. Acceptable forms: (a) exterior-observable beats (shadow on window glass, muffled sounds through stone, shapes moving past an open door), or (b) cut interior beats and replace with a single exterior inference beat. ID 34 (`oc-castellan-harrenhal speaks to ser-harwick-plumm`) cannot stand as a direct speech beat in interior cottage space when the narrator is in the yard — it must either be cut or recast as an auditory inference (`voices carry the cottage door`) in a form the schema permits. All four beats must pass a single test: is this observable by Taylor standing in the yard?

---

### fault-002

- **id:** fault-002
- **type:** fault
- **class:** FAULT-CONTINUITY-MISSING-TRANSITION
- **lines:** between 26 and 27
- **what:** Taylor exits the nave at ID 26 (`taylor-hebert-westeros exits the nave`). ID 27 immediately reads `oc-castellan-harrenhal walks the yard` without a beat establishing Taylor's yard position. Pass-3 shape audit identified this as a missing transition: "Taylor exits the nave but her yard position during cottage inspection (27–37) is unestablished. Add a beat: Taylor holds in the yard at a specific exterior location (gate / well / wall) so 27–37 can be exterior-observable." The chapter-04 file does not contain this transition beat. Taylor's yard position during IDs 27–37 is not established by any beat.
- **why:** The POV fault at IDs 32–35 (fault-001 above) is partially downstream of this missing transition. Without a yard-position beat for Taylor, the reader/stitcher cannot locate her during the cottage inspection sequence. If Taylor is at the gate, some beats in IDs 32–35 may be reachable (e.g., she can observe the shadow crossing the window from outside); if she is at the garden wall (IDs 97–98 destination), the angle changes. The missing transition is not merely cosmetic — it determines what Taylor can actually observe during the cottage phase and is required by the pass-3 verdict.
- **criteria:** Insert one beat between IDs 26 and 27 establishing Taylor's yard position during the cottage inspection sequence. Beat must be SVO-clean, first-person Taylor narrator, physical positioning action (e.g., `taylor-hebert-westeros holds the yard wall` or `taylor-hebert-westeros reaches the yard center`). New beat receives next available monotonic ID. Pass-2 re-check required on the new beat only.

---

### fault-003

- **id:** fault-003
- **type:** fault
- **class:** FAULT-CONTINUITY-MISSING-TRANSITION
- **lines:** between 50 and 52
- **what:** ID 50 is the last beat of the interrogation exchange (`oc-castellan-harrenhal speaks to taylor-hebert-westeros`). ID 51 reads `taylor-hebert-westeros lowers the eyes`. ID 52 reads `a raven descends the bell tower`. There is no beat establishing the pause or held silence that creates the opening for the raven descent. Pass-3 shape audit identified this as a missing transition: "Interrogation ends at 50; raven descends at 52. No beat establishes the stall that creates the opening. Add: a pause / held silence / castellan waits for Taylor's signature." The chapter-04 file does not contain this beat.
- **why:** The raven descent at ID 52 is the chapter's load-bearing anomaly event. Its narrative credibility depends on there being an observable interval — a held moment — in which the raven can descend without the scene's attention immediately arresting it. Without a stall beat, the transition from speech exchange to raven descent reads as unmotivated in the chapter's cause-effect chain. This is a continuity cause-effect gap, not only a structural shape concern: the stall beat is the causal condition that allows the raven to land before anyone reacts.
- **criteria:** Insert one beat between IDs 51 and 52 establishing the held pause or silence — a moment of no-action that the raven descent then interrupts. Beat must be SVO-clean. Permitted forms include a body-state hold (e.g., `taylor-hebert-westeros holds the silence` — but note `silence` is abstract; prefer `taylor-hebert-westeros holds the spine` or `oc-castellan-harrenhal holds the yard`) or a physical environmental beat (e.g., `the yard holds`). The beat must be taylor-hebert-westeros narrator POV or an exterior observable event. New beat receives next available monotonic ID. Pass-2 re-check required on the new beat.

---

## Flags

---

### flag-001

- **id:** flag-001
- **type:** flag
- **lines:** 1–3 (ch03→ch04 boundary)
- **what:** Chapter-03 closes with: `41 taylor-hebert-westeros climbs the loft ladder` / `42 taylor-hebert-westeros holds the feet` / `43 the cottage fire snaps`. Taylor's final established position in chapter-03 is the loft (or climbing it). Chapter-04 opens with `1 the ravens flush the bell tower` / `2 taylor-hebert-westeros enters the yard` / `3 taylor-hebert-westeros reaches the road-facing wall`. There is no beat establishing Taylor's descent from the loft between chapter-03-close and chapter-04-open.
- **why:** The loft-to-yard transit is a routine transition and the time gap between chapters is implied. The chapter-04 narrator header is Taylor POV. The ravens flushing the bell tower at ID 1 is consistent with Taylor being in the yard and observing. This gap is expected at chapter-boundary granularity — chapter plans do not require loft-descent to be a recorded beat. This is a flag not a fault because the transit is inferable from the chapter boundary convention and the chapter goal (`the ravens flush` as her first perceptual beat implies she is already in the yard or at the threshold).
- **criteria:** No fixer action required. If a stitcher or SVO writer flags the loft-descent as a missing beat in the prose pass, a single transition sentence covers it without requiring a new proto-line. Note for downstream: if chapter-04 pass-3 recast adds the Taylor yard-position beat (fault-002 fix) and the stall beat (fault-003 fix), those new beats should not introduce a loft-descent sequence — that remains pre-chapter.

---

### flag-002

- **id:** flag-002
- **type:** flag
- **lines:** ch04→ch05 boundary
- **what:** Chapter-04 closes with Taylor at the well (`99 taylor-hebert-westeros reaches the well`). Chapter-05 is an interlude narrated by septon-rowan (narrator: septon-rowan; interlude: true). Chapter-05 opens with `1 septon-rowan enters the sept yard`. Taylor appears in chapter-05 at line 3 (`3 taylor-hebert-westeros crosses the yard`) and at the bell tower at line 85 (`84 the ravens lift` / `85 septon-rowan touches the ledger`). There is no continuity violation from Taylor's perspective — chapter-05 is Rowan POV, not Taylor POV, and Taylor's well-position at chapter-04 close is compatible with her yard-presence in chapter-05. The POV default rule (Taylor first-person; non-Taylor chapters MUST be marked interludes) is satisfied: chapter-05 carries `interlude: true`.
- **why:** No fault. The boundary is clean on POV grounds. Flagging only because the chapter-04 well-position (`taylor-hebert-westeros reaches the well`) and chapter-05's `3 taylor-hebert-westeros crosses the yard` represent a spatial reset without an explicit connecting beat — Taylor moves from the well to the yard between chapter-04-close and chapter-05-open. This is again a chapter-boundary convention gap and is within acceptable range for chapter-level granularity.
- **criteria:** No fixer action required. If a SVO writer needs continuity between the two chapters, a single transitional phrase handles it. Recorded here for downstream awareness only.

---

## Axis-by-axis summary

| Axis | Result | Notes |
|------|--------|-------|
| Reachability | FAIL | fault-001: cottage interior beats unreachable from yard (Taylor-POV). fault-002: Taylor yard position unestablished during IDs 27–37. |
| State persistence | PASS | Plumm's rolled page chain (IDs 45–81) is fully continuous. Third rider's ledger chain (IDs 39, 72, 74, 91, 92) is internally unbroken and uninterrupted by post-pass-4 trim review; no line removed the ledger from the third rider's possession between introduction and stow. Raven perch (ID 53) is consistent with bell tower roost established throughout prior chapters. |
| Reference resolution | PASS | All actor slugs used in ch04 are established. `septon-rowan` is established in ch04 at ID 8 (rises from chancel steps), which is the first ch04 appearance; consistent with ch03 close (Rowan in sept-environs from prior episodes). `the third rider` is introduced at ID 5 and carried consistently. `oc-castellan-harrenhal` established from prior chapters. |
| POV consistency | FAIL | fault-001 (IDs 32–35): interior cottage beats, narrator is outside. Exterior perceptual recast required. |
| Time consistency | PASS | Chapter is single-session: inspection party arrives, conducts inspection, departs. No time-skip issues within the chapter. Time-skip at ID 95 (blank line) correctly separates the riders' departure from Taylor's yard denouement. |
| Cause-effect | FAIL | fault-003 (between IDs 51–52): no stall beat before raven descent; the anomaly event is causally unmotivated at proto-line level. |
| ch03→ch04 boundary | FLAG | flag-001: loft-to-yard transit implied, not stated. Within chapter-boundary convention. |
| ch04→ch05 boundary | FLAG | flag-002: well-to-yard reset between chapter-04-close and chapter-05-open; within chapter-boundary convention; interlude marker correctly applied. |

---

## ID 53 special finding

- **id:** id53-adjudication
- **type:** pass
- **what:** `a raven perches taylor-hebert-westeros` (line 56 of file)
- **why:** Beat passes all continuity axes: raven is reachable from bell tower roost established in prior chapters; Taylor is in the yard (accessible landing target); witnesses are confirmed in position (castellan and Plumm both present); fauna-control condition allows the observable anomaly; the involuntary-disclosure narrative function is complete (witnesses react at IDs 56–61, evidence is recorded before Taylor can act). The iter2 mechanic advisory is retired at this layer. Beat stands.

---

## Plumm rolled page special finding

- **id:** plumm-roll-adjudication
- **type:** pass
- **what:** Prop chain for prop-rolled-inspection-page (introduced ID 46, rolled ID 80, pocketed ID 81)
- **why:** The acquisition chain is fully sequential and unbroken within chapter-04 (IDs 46 → 47 → 57 → 60 → 61 → 75 → 76 → 77 → 79 → 80 → 81). The transfer to castellan (ID 77) and return (ID 79) are both explicit. The roll is pocketed (ID 81) and Plumm departs with the riders (IDs 93–94). No intervening line strips the roll from Plumm between ID 81 and chapter end. Plumm's state.md confirms prop-rolled-inspection-page in his chain of custody from ch04 line 80–81 onward. Prop is load-bearing and properly anchored.

---

## Fixer routing

Dispatch fixer against: fault-001, fault-002, fault-003.

- **fault-001** (IDs 32–35): RECAST-PHYSICAL — recast all four beats to exterior-POV-accessible forms. Cottage interior events must be rendered as what Taylor in the yard can see or hear. The speech beat (ID 34) is the most constrained: either cut or recast as auditory inference in a permitted SVO form. Fixer should coordinate the ID 32–35 recast with the Taylor yard-position established by the fault-002 fix — the recast content depends on exactly where Taylor is standing.
- **fault-002** (between IDs 26 and 27): INSERT — one Taylor yard-position beat between existing IDs 26 and 27. Beat receives next available monotonic ID after existing max (99). Pass-2 re-check on new beat only.
- **fault-003** (between IDs 51 and 52): INSERT — one stall/pause beat between existing IDs 51 and 52. Beat receives next available ID (or the ID directly following fault-002's new beat). Pass-2 re-check on new beat only.

Ordering recommendation: resolve fault-002 (yard position) before fault-001 (interior recast), because the yard position determines what exterior-observable forms are credible for the IDs 32–35 recast.

---

## File-level verdict

**FAIL**

Three continuity faults are present. Two are unresolved pass-3 required additions (fault-002, fault-003); one is an unresolved pass-3 required recast (fault-001). No fault is structural at season scope. All three are episode-scope fixes. The file does not advance to facet authoring until faults are resolved and a confirmatory pass-5 re-run clears the modified lines.
