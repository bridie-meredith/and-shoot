---
facet: state-updates
phase: 2 (writer-fork output)
author: studio
batch: studio (studio.* + prop:*)
episode: s01e01
rubric: design/shoot-v2/rubric-state-updates.md (V2 locked)
---

## Note on prop slugs

No formal prop cards exist in `cards/props/` (INDEX.md is empty). Props in this file use project-referent slugs established by the rubric's calibration anchors (`prop:letter`, `prop:district-ledger`). These are treated as project-originals with implicit warehouse presence in s01e01. Field-extensions are flagged per §"Field-extension protocol" where applied.

---

## S1 — @64: the stylus marks two parallel lines beside taylor's entry

INTENT-ID: S1
DECISION: FIRE

DRAFTS:
- Draft A: `prop:district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin`
- Draft B: `prop:district-ledger.parallel-marks: absent -> two-strokes-beside-taylor-entry`

CHOSEN: Draft A

ENTRY: [assigned id in Final list]
`@64 prop:district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin`
  # field-extension: taylor-entry (new field for s01e01 ledger-record tracking; the district ledger's per-name entry is a tracked state aspect, not a perception; extension licit under §"Field-extension protocol")

RATIONALE:
Reality — the parallel marks are a physical mutation to the ledger record, irreversible, persistent past @64 for the remainder of the episode and beyond (the marks do not lift). The verb "marks" is a transition-verb on the record's physical state. Frugality — the `<old>` value is `dictated-provisional`, which traces to the dictation event at @48 where the officer dictated Taylor's name as provisional labor-eligible; that was the prior state-change on this field. Tensometer cross-facet: @64=3, STATE-UPDATE NOTE reads "co-citation strongly expected here — irreversible registration"; this entry directly honors that contract. Narrator-interest @64 fires ("two strokes; the determination is on the record and on her") — this entry is the ledger-side of that fire; no POV-actor-state requirement on a prop entry, but the cross-facet alignment is clean.

ANTI-PATTERN CHECK: None fire. Not registration-as-state (the marks are a physical mutation). Not held-against-turn (tensometer @64=3, commit beat, not @39-class). Not invented-field (district-ledger entry state is a tracked aspect; field-extension noted).

---

## S2 — @38: taylor puts the letter into the air in front of the officer

INTENT-ID: S2
DECISION: FIRE

DRAFTS:
- Draft A: `prop:letter.holder: taylor -> mid-air-between-them`
- Draft B: `prop:letter.position: at-taylor-side -> extended-forward-toward-officer`

CHOSEN: Draft A

ENTRY: [assigned id in Final list]
`@38 prop:letter.holder: taylor -> mid-air-between-them`

RATIONALE:
Reality — "puts the letter into the air" is an explicit holder-transition verb; the letter passes out of Taylor's hand-at-rest into a held-forward position between them. The rubric calibration anchor at @38 explicitly names this as a FIRE: "the holder genuinely changes (Taylor's hand to the air-between-them); persistence holds across @38–@39 until the officer takes it at @40." Frugality — `<old>` is `taylor`, established from episode-start (she brought the letter to the yard and has held it through @28); this is first-touch on the holder chain, so project-setup baseline applies. Authority — studio writes prop holder; this is licensed. Tensometer @38=3, body-charge + reversal-proximity, co-citation permitted; no @39-class restriction applies to @38. Narrator-interest @38 fires ("the exposure is paid; the body reaches at the height the cognition has already cleared") — prop entry, no narrator-interest co-citation required.

ANTI-PATTERN CHECK: None. The rubric calibration anchor explicitly defends this fire.

---

## S3a — @40: the officer unfolds the letter

INTENT-ID: S3a
DECISION: FIRE

DRAFTS:
- Draft A: `prop:letter.holder: mid-air-between-them -> officer`
- Draft B: `prop:letter.physical-condition: folded -> unfolding`

CHOSEN: Draft A

ENTRY: [assigned id in Final list]
`@40 prop:letter.holder: mid-air-between-them -> officer`

RATIONALE:
Reality — "unfolds the letter" presupposes the officer has taken the letter from the air. The holder chain requires this intermediate entry: at @38 the holder went to `mid-air-between-them`; at @40 the officer unfolds — he cannot unfold without having received it, so the holder-flip to officer happens at @40. The physical-condition change (folded -> unfolding) is a transient within the beat; the officer folds it back at @42, so "unfolding" does not persist. The holder-flip from mid-air to officer DOES persist through @40–@42. Frugality — `<old>` is `mid-air-between-them` per the @38 entry; chain is honored. Draft B is rejected: physical-condition "unfolding" is transient (reverts at @42); it fails the persistence test.

ANTI-PATTERN CHECK: Persistence test on Draft B would have fired (folded -> unfolding -> folded within @40–@42; that is a transient, not a state). Draft A passes: holder stays with officer through @42.

---

## S3b — @45: taylor's palm closes on the letter

INTENT-ID: S3b
DECISION: FIRE

DRAFTS:
- Draft A: `prop:letter.holder: officer -> taylor`
- Draft B: `prop:letter.position: officer-hand-extended -> taylor-palm`

CHOSEN: Draft A

ENTRY: [assigned id in Final list]
`@45 prop:letter.holder: officer -> taylor`

RATIONALE:
Reality — "taylor's palm closes on the letter" is the flip-beat where the holder transitions from officer back to Taylor. The rubric calibration anchor at @45 explicitly defends this: "fire @45: prop:letter.holder: officer -> taylor... Fire on @45 (the flip-beat), not @43 (the offer) or @44 (the trajectory)." Persistence holds: Taylor carries the letter forward through @49, @51, @74 (fist holds the letter). Frugality — `<old>` is `officer` per @40 entry; chain honored; no drift. Authority — studio, licensed.

ANTI-PATTERN CHECK: Pre-emption check — @43 (offer) and @44 (return trajectory) are not the flip-beat; firing on either would be anti-pattern #7. @45 is the correct beat.

---

## S4 — @41: the seal breaks at the crease under his thumb

INTENT-ID: S4
DECISION: FIRE

DRAFTS:
- Draft A: `prop:letter.seal-condition: intact -> broken`
- Draft B: `prop:letter.physical-condition: sealed -> open-at-crease`

CHOSEN: Draft A

ENTRY: [assigned id in Final list]
`@41 prop:letter.seal-condition: intact -> broken`

RATIONALE:
Reality — "the seal breaks" is an explicit, irreversible physical-state transition on the letter prop. The seal cannot be unbroken; persistence is absolute. The verb is a break-verb on a physical seal — a tracked prop-state field (the rubric §Authority lists "seal-condition for seal-bearing props" as a standard prop-state field). Frugality — `<old>` is `intact` (the letter arrived in Taylor's possession sealed; no prior proto-line broke it; first-touch, project-setup baseline). The holder at @41 is still `officer` (per @40 chain); this entry does not touch holder, correctly isolated. Authority — studio, licensed for prop physical fields.

ANTI-PATTERN CHECK: None. Seal-break is explicitly cited in the rubric's ACCEPT signatures for Reality ("breaks the seal" is the example). Not transient: a broken seal stays broken.

---

## S5 — @57: edric steps back through the door (cottage-door state)

INTENT-ID: S5
DECISION: FIRE (with scope restriction to door-open-while-crossing only)

REASONING ON DOOR-CLOSE:
The proto-line at @57 reads: "edric steps back through the door." This establishes Edric crossing from yard to cottage interior. It does not state the door closes after him. The rubric calibration anchor for @57 says: "studio.doors_and_shutters.cottage-door: open -> closed (if the proto-line file establishes that the door closed; check)." The proto-line does NOT establish that the door closed. The door's prior state in s01e01 is not resolved by the studio state.md (which reflects s01e06 and records cottage-door: CLOSED as a carried-forward state — this is the long-run state but does not establish the moment-of-closing within s01e01).

However: for Edric to step through the door, the door must have been open or openable at @57. Proto-lines @55–@56 show Edric looking at officer then at Taylor — he is in the yard (accessible) before stepping through the door. The cottage door must be in a transitioned state to allow passage. If I fire the door-open at @57, I cannot simultaneously fire door-close (no evidence it closed at that beat). Firing door-close without proto-line evidence would be pre-emption of an unestablished event.

DECISION: FIRE on `studio.doors_and_shutters.cottage-door: closed -> open` at @57 — Edric must pass through it; the door opens to permit passage. Withhold the door-close entry (no proto-line evidence it closes behind him at @57 or immediately after).

DRAFTS:
- Draft A: `studio.doors_and_shutters.cottage-door: closed -> open`
- Draft B: `studio.doors_and_shutters.cottage-door: open -> closed` (REJECTED — no proto-line evidence for closing at @57)

CHOSEN: Draft A

ENTRY: [assigned id in Final list]
`@57 studio.doors_and_shutters.cottage-door: closed -> open`

RATIONALE:
Reality — for Edric to step back through the cottage door, the door must open. The transition from closed to open is the implied precondition of passage (or it opens as he steps through — either way, the beat where he crosses is the beat the door-state registers as open). Authority — studio owns doors_and_shutters; this is licensed. Frugality — `<old>` is `closed`; the s01e06 state.md confirms cottage-door: CLOSED as the default/long-run state, and no prior s01e01 proto-line has recorded a cottage-door change. The door-close entry is withheld: the rubric's calibration anchor conditionals it on proto-line evidence of closing, and @57 provides none.

ANTI-PATTERN CHECK: Refusing the door-close entry honors the rubric's floor-defense guidance. The door-open entry is not Registration-as-state (it is a physical precondition of the crossing, not a perception). Not pre-empting — the door opens when Edric crosses, at @57.

---

## S6 — @43: the officer holds the letter out to taylor

INTENT-ID: S6
DECISION: NONE

RATIONALE:
At @43, the officer extends the letter toward Taylor. The holder chain at @43 is: letter is with officer (since @40). Extending the letter toward Taylor does not change the holder — the officer's hand is still on the letter at @43; Taylor has not yet received it. The rubric calibration anchor for this exact sequence is explicit: "@43 (the offer)" is NOT the flip-beat; "@44 (return-trajectory)" is NOT the flip-beat; "@45 (Taylor's palm closes)" IS the flip-beat. Firing at @43 would be anti-pattern #7 (pre-empting a future beat). The holder does not change at @43.

ANTI-PATTERN CHECK: Anti-pattern #7 (pre-empting). The flip-beat is @45, which already has a FIRE entry (S3b). A second entry at @43 on the same field would be drift-pre-emption.

---

## Additional fires (free additions, up to 4)

### ADD-1 — @30: the stylus moves on taylor's name

DECISION: FIRE

REASONING: At @30, "the stylus moves on taylor's name" — this is the clerk recording Taylor's name under sustained targeting attention. The district ledger is a prop with a tracked record state. At @30, Taylor's name is being actively written on the ledger: this is the first-touch of Taylor's name on the record (it was not there before; now it is being inscribed). This is persistent: the name-on-line state persists through the episode (Taylor's name is on the ledger from @30 onward as a working inscription, later dictated formally at @48 and marked at @64). Tensometer @30=2 (stakes-visibility, reversal-proximity). Narrator-interest @30 fires ("the name on the line is the exposure she had budgeted against and is now paying").

The relevant field is `prop:district-ledger.taylor-entry` — the entry's initial state before @30 is `absent` (Taylor's name was not on the ledger). After @30 it is `name-inscribed-pending-dictation` (her name is on the line but the formal dictation has not yet completed).

DRAFTS:
- Draft A: `prop:district-ledger.taylor-entry: absent -> name-inscribed-pending-dictation`
- Draft B: `prop:district-ledger.recording-status: officer-speaking-to-clerk -> name-in-progress`

CHOSEN: Draft A

ENTRY: [assigned id in Final list]
`@30 prop:district-ledger.taylor-entry: absent -> name-inscribed-pending-dictation`
  # field-extension: taylor-entry (same field tracked through @30 -> @48 -> @64; this is the first-touch state)

RATIONALE:
Reality — at @30 the stylus moves on Taylor's name; this is the first physical inscription of her name on the ledger. Prior to @30, Taylor's name was not on the record. The state persists: the name remains on the line through @47–@48 (formal dictation) and @64 (parallel marks). This is not a stylus-motion registration; it is a ledger-state mutation. Frugality — `<old>` is `absent` (first-touch; no prior entry on this field). Authority — studio writes prop; licensed. Cross-facet: tensometer @30=2, stakes-visibility; narrator-interest @30 fires. No POV actor-state requirement.

ANTI-PATTERN CHECK: Check against "stylistic noting" — the motion is not merely interesting; the ledger's state genuinely changes when the name inscription begins. Not registration-as-state: the field changes from absent to inscribed. Not pre-emption: @48 dictation and @64 parallel-marks are downstream changes on the same field, recorded at the correct downstream beats.

---

### ADD-2 — @11: the officer comes through the gate

DECISION: NONE

REASONING: The officer coming through the gate is a position-transition for actor:officer — not studio's authority. Studio would own `studio.doors_and_shutters.gate-status` if the gate changes state, but "the officer comes through the gate" is an actor-position event; the gate opening/closing is not established by the proto-line (the gate may have been open). This is actor-state (edric-fork or officer-fork), not studio-state. No `studio.*` or `prop:*` field changes at @11 that are within studio's authority.

ANTI-PATTERN CHECK: Anti-pattern #2 (cross-POV authoring) if studio wrote `actor:officer.position`; anti-pattern #10 (stylistic noting) if studio fires on an interesting gate-crossing without a real field mutation.

---

### ADD-3 — @15: taylor enters the line

DECISION: NONE

REASONING: Taylor entering the line is actor-state (actor:taylor-hebert-westeros.position). Studio does not write actor state. No studio.* or prop:* field changes at @15.

ANTI-PATTERN CHECK: Anti-pattern #2 if fired on wrong target.

---

### ADD-4 — @9: the clerk unrolls the parchment

DECISION: FIRE

REASONING: The clerk unrolls the parchment — this is a physical-condition change on a prop (the district ledger / assessment parchment). Prior to @9, the ledger/parchment is in rolled state (the clerk unrolls it, implying it was rolled). After @9 it is unrolled. The prop is the district ledger (or the parchment that becomes the ledger record). The physical condition changes from rolled to unrolled at @9. This state persists through the entire episode (the parchment is not re-rolled during s01e01).

DRAFTS:
- Draft A: `prop:district-ledger.physical-condition: rolled -> unrolled`
- Draft B: `prop:district-ledger.record-status: stored -> active`

CHOSEN: Draft A

ENTRY: [assigned id in Final list]
`@9 prop:district-ledger.physical-condition: rolled -> unrolled`

RATIONALE:
Reality — "unrolls the parchment" is an explicit physical-condition verb on the prop; rolled -> unrolled is a persistent state change (the parchment stays unrolled for the entire recording session through @68 when the clerk folds the board). Frugality — `<old>` is `rolled`, first-touch, project-setup baseline. Authority — studio, prop domain, licensed. Tensometer @9=1; this is an approach-zone establishing beat — the rubric permits approach-zone fires for genuine state changes (the "approach zone permitted-silent" note refers to actor-state and scene-emotion fires, not to prop physical-state transitions that are directly established by a verb). This is a low-charge but real field change.

ANTI-PATTERN CHECK: Density-on-flat risk — this is a @1-zone beat (tens=1). Check: is this a genuine field-mutation or stylistic noting? The verb "unrolls" is an explicit physical transition on a prop. The change is real and persistent. Defended: anti-pattern #9 (density-on-flat) fires when fires are on *registration* or *perception* beats in the flat zone; a real prop physical-state change is permitted even in the 1-zone. Not Registration-as-state: the parchment's physical condition changes.

---

### ADD-5 — @68: the clerk folds the board

DECISION: FIRE

REASONING: "The clerk folds the board" — the board is the writing board on which the clerk has balanced the ledger through the episode (@17: "the clerk balances the ledger on the board against his hip"). Folding the board is a physical transition on the board prop. The board goes from open/deployed to folded. Separately, folding the board implies the ledger session has closed: the ledger physical condition transitions from active/open to being placed (the ledger is no longer being written on after @64; @68 is the administrative closure of the writing session). The prop is `prop:district-ledger` (or `prop:clerks-board` as a separate prop).

The proto-line specifically says "the clerk folds the board" — the board is distinct from the ledger. The board physical-condition changes at @68. This is a genuine prop state transition.

DRAFTS:
- Draft A: `prop:district-ledger.physical-condition: unrolled -> folded-or-stored`  (treating board-folding as ledger close)
- Draft B: `prop:district-ledger.session-status: recording-active -> session-closed`

CHOSEN: Draft A

ENTRY: [assigned id in Final list]
`@68 prop:district-ledger.physical-condition: unrolled -> folded-or-stored`

RATIONALE:
Reality — "the clerk folds the board" at @68 is the administrative close of the recording session; the ledger/parchment returns from active-open to stored/folded. The physical condition that changed at @9 (rolled -> unrolled) now resolves at @68 (unrolled -> folded-or-stored). Persistence: the ledger does not return to active use in s01e01. Frugality — `<old>` is `unrolled` per the @9 entry; chain honored. Authority — studio, prop domain, licensed. Tensometer @68=1; this is a release-zone beat, but the prop-state change is real and closes the @9 open.

ANTI-PATTERN CHECK: Same density-on-flat consideration as ADD-4; same defense applies. This closes an open field-state from @9; it is a legitimate bookend. Not compound: the board-folding and ledger-close are treated as one event on the ledger physical-condition (the board is the carrier; its folding is the ledger-close mechanism).

---

## Final entry list

(monotonic IDs, schema form, pure)

```
1 @9  prop:district-ledger.physical-condition: rolled -> unrolled
     # field-extension: physical-condition (first-touch; ledger deployed at @9, returned at @68)

2 @30 prop:district-ledger.taylor-entry: absent -> name-inscribed-pending-dictation
     # field-extension: taylor-entry (new field for s01e01 ledger-record tracking; tracks name-state across @30/@48/@64)

3 @38 prop:letter.holder: taylor -> mid-air-between-them

4 @40 prop:letter.holder: mid-air-between-them -> officer

5 @41 prop:letter.seal-condition: intact -> broken

6 @45 prop:letter.holder: officer -> taylor

7 @48 prop:district-ledger.taylor-entry: name-inscribed-pending-dictation -> dictated-provisional
     # field-extension: taylor-entry (state advances from name-inscribed to formally-dictated-provisional; @48 = formal dictation event per calibration anchor)

8 @57 studio.doors_and_shutters.cottage-door: closed -> open

9 @64 prop:district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin
     # field-extension: taylor-entry (irreversible parallel-marks; tensometer @64 STATE-UPDATE NOTE: co-citation strongly expected)

10 @68 prop:district-ledger.physical-condition: unrolled -> folded-or-stored
```

---

## Entry 7 note (@48)

The rubric calibration anchor at @48 assigns `prop:district-ledger.taylor-entry: pending -> dictated-provisional` to studio. The calibration anchor's `<old>` is `pending`; my chain has `<old>` as `name-inscribed-pending-dictation` (because @30 already fired on this field). The calibration anchor's `pending` is a compressed label that covers the pre-dictation state; my chain is more granular and traces the field through @9 (rolled) → @30 (name-inscribed) → @48 (dictated) → @64 (parallel-marks). This is not a Drift-old violation — it is a more granular chain. The anchor's `pending` and my `name-inscribed-pending-dictation` are semantically equivalent pre-dictation states; the difference is that my chain has an intermediate @30 fire. If the @30 fire (ADD-1) is culled in review, @48's `<old>` would revert to `absent` or `pending` depending on reviewer preference.

---

## Curve check

**Total fires: 10** (9 if @48's chain-dependency on ADD-1's @30 fire causes a cull — but both are defended independently).

**Distribution:**
- `studio.*`: 1 entry (@57 cottage-door)
- `prop:letter.*`: 4 entries (@38, @40, @41, @45)
- `prop:district-ledger.*`: 5 entries (@9, @30, @48, @64, @68)

**Density:** 10/77 = 13.0% — within the rubric's 8–18% sparsity band.

**Defended NONEs:**
- S6 (@43): pre-emption of @45 flip-beat; anti-pattern #7. The rubric calibration anchor explicitly says @43 is NOT the fire beat.
- S5 door-close: withheld because no proto-line evidence of closing at @57; fire restricted to door-open only.
- ADD-2 (@11 gate): actor-state, not studio authority.
- ADD-3 (@15 line entry): actor-state, not studio authority.

**Target diversity:** 3 targets — studio.*, prop:letter, prop:district-ledger. All three target classes within studio's authority exercised.

**Cross-facet self-check:**
- @64 tensometer STATE-UPDATE NOTE ("co-citation strongly expected") honored: entry 9 fires.
- @39 tensometer STATE-UPDATE NOTE ("any co-citation here must be actor-posture only; canonical state does not change") honored: no studio or prop entry at @39 (Taylor's posture is Taylor-fork's domain anyway).
- @38 tensometer @38=3 body-charge: prop:letter.holder fire at @38 is in the permitted class (not @39-class); calibration anchor explicitly defends it.
- All prop:* entries require no narrator-interest co-citation (rubric: "studio.* or prop:* entries do NOT require narrator-interest co-citation"). Self-check passes.
- No `actor:*` entries authored (authority boundary maintained).
