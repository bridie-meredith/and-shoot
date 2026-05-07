# Phase 2 — State-Updates Author Output (Taylor fork)

Author: dialogue-writer fork for `taylor-hebert-westeros`, state-update output mode
Episode: s01e01
Scope: `actor:taylor-hebert-westeros.*` entries only
Authority: V2 locked rubric (`design/shoot-v2/rubric-state-updates.md`); locked tensometer; locked narrator-interest

---

## Core intents

### T1 — @39 taylor sets her feet on the dirt where his next pace commits

DECISION: NONE (REFUSE-WITH-RUBRIC-CITATION)

ANTI-PATTERN CHECK: Firing here would trigger anti-pattern #3 (held-against-turn fire) and anti-pattern #8 (posture-as-state). Tensometer @39's locked STATE-UPDATE NOTE is explicit: "any co-citation here must be actor-posture only; pure registration class — canonical state does not change at @39." The DOUBLE-TAP annotation (@38=thrust, @39=held-awaiting) confirms @39 is the held-against-turn beat by name. Per Reality axis: the feet-set is body-charge, not persistent posture-state — it resolves at @40 when the officer takes the letter and the standoff releases. The strip-test passes for refusal: at @40 Taylor's position is not load-bearing on the canonical schema; the field that mattered was `prop:letter.holder` (studio's domain at @38) and the officer's response. Floor-defense: sparsity is load-bearing; this is the rubric's calibration anchor for refusal.

---

### T2 — @48 the officer dictates taylor's name as provisional labor-eligible

DECISION: FIRE

DRAFTS:
- (a) `@48 actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible`
- (b) `@48 actor:taylor-hebert-westeros.administrative-status: unattached-ward -> provisional-labor-eligible`

CHOSEN: (a) — matches the rubric calibration anchor's phrasing; "child-or-ward" reflects Taylor's pre-census informal status under Septon Osmynd's protection per the persona card, before the dictation creates the formal labor-eligibility classification.

ENTRY:
```
1 @48 actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible
```

RATIONALE: Reality — irreversible bureaucratic mutation; the dictation creates a record-state that persists past the beat and through the season's administrative arc (per persona card's "she does not go back" hard fence on this kind of formal capture). Authority — Taylor fork is the licensed author for `actor:taylor-hebert-westeros.*`; `administrative-status` is a licit field-extension under §"Field-extension protocol" (it is a tracked-state-aspect, not a perception, mood, or stylistic flourish). Frugality — one entry, one field, on the beat where the field flips (the dictation IS the act of recording determination per tensometer @48's DEFENDED note). Cross-facet contract: tensometer @48=2 (DEFENDED, documents prior turn) does not forbid state-update; it is not @39-class. Narrator-interest @48 fires (`she has heard the shape of that word before in another tongue` — foreknowledge-clamp on "provisional"); POV co-citation requirement satisfied. Calibration anchor in rubric explicitly authorizes this entry.

ANTI-PATTERN CHECK: not registration-as-state (real field-mutation); not cross-POV (own actor); not held-against-turn (@48 not @39-class); not compound (single field); not drift-old (canonical baseline matches persona card opening state); not invented-field (administrative-status is tracked-aspect class); not pre-empting (fire on the dictation beat, not earlier); not posture-as-state; not density-on-flat; not stylistic noting.

---

### T3 — @64 the stylus moves on the line under taylor's name (parallel-margin marks)

DECISION: FIRE

DRAFTS:
- (a) `@64 actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks`
- (b) `@64 actor:taylor-hebert-westeros.knowledge.record-state: dictated-provisional -> dictated-provisional-with-parallel-marks`

CHOSEN: (a) — matches rubric calibration anchor's exact phrasing; aligns with the prop-side ledger entry the studio fork will write.

ENTRY:
```
2 @64 actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks
```

RATIONALE: Reality — Taylor's knowledge of the record-state changes at @64 because she perceives the marking (per narrator-interest @64 `two strokes; the determination is on the record and on her`); this is the POV-side knowledge field corresponding to the prop-side ledger mutation. Persistence is absolute (the marks do not unmark; her knowledge of them does not unknow). Authority — Taylor fork is the licensed author for `actor:taylor-hebert-westeros.knowledge.*`; field-extension is licit per rubric (knowledge is explicitly named as a tracked-state-aspect). Frugality — one entry, one field, on the flip-beat (@64 IS the determination per tensometer's DEFENDED note distinguishing @64 from @48). Cross-facet contract: tensometer @64=3 with locked STATE-UPDATE NOTE "co-citation strongly expected here — irreversible registration"; this entry honors that contract. Narrator-interest @64 fires; POV co-citation requirement satisfied. Calibration anchor in rubric explicitly authorizes.

ANTI-PATTERN CHECK: not registration-only (the knowledge field genuinely flips because the perception is irreversible knowledge-acquisition, not transient noting); not cross-POV; not held-against-turn (the locked tensometer specifically expects fire here); not compound; not drift-old; not invented-field (knowledge.* is tracked-aspect class); not pre-empting (fire on @64, not @63 approach); not posture-as-state; not density-on-flat; not stylistic noting.

---

### T4 — @50 taylor turns to mira

DECISION: NONE

ANTI-PATTERN CHECK: Firing here would trigger anti-pattern #8 (posture-as-state) and anti-pattern #1 (registration-as-state). Per Reality axis REJECT signature explicitly named in rubric: "*taylor turns to mira* (@50) — turning is a momentary directional shift, not a persistent posture change." Strip-test: at @51 Taylor speaks to Mira (orientation incidental to the speech act); by @54 she has turned across the yard to Edric — the @50 orientation does not persist. The turn-verb is not a tracked-state field on Taylor's schema. Tensometer @50=1 (no axis lit); narrator-interest is silent at @50. No cross-facet expectation of fire. Floor-defense.

---

### T5 — @52 mira drops her eyes to the flagstones

DECISION: REFUSE-WITH-RUBRIC-CITATION

ANTI-PATTERN CHECK: This is the cross-POV trap. Taylor fork has no authorship over `actor:mira.*` — that is the Mira fork's authority (anti-pattern #2, cross-POV authoring). The only candidate Taylor-side target would be a "perception of allies" or "ally-count" field, which the rubric explicitly names as a REJECT signature under Reality: "*the count of allies in the yard drops to one* (narrator-interest @52) — this is Taylor's *perception* of an ally count. The canonical state of `actor:edric.position` may change at @57... the *count-of-allies-as-Taylor-sees-it* is not a tracked field." Per cross-facet contract notes on narrator-interest, the @52 fire is registration-class; "the canonical `actor:mira.engagement-state` field-change (if any) is the Mira fork's authority, not Taylor's." Honor. Floor-defense.

---

## Free additions

### F1 — @45 taylor's palm closes on the letter (POV-side inventory)

DECISION: FIRE

DRAFTS:
- (a) `@45 actor:taylor-hebert-westeros.inventory: empty -> letter`
- (b) `@45 actor:taylor-hebert-westeros.inventory.letter: not-held -> held`

CHOSEN: (a) — clean delta on the inventory field-collection.

ENTRY:
```
3 @45 actor:taylor-hebert-westeros.inventory: -letter-extended -> +letter-held
```

RATIONALE: Reality — the letter-holder change at @45 (studio writes `prop:letter.holder: officer -> taylor`) has a Taylor-side consequence: the letter is now in her inventory, persistent through the rest of the episode (state.md shows it stays in her right hand through @74 and beyond). Authority — Taylor fork is licensed for her own inventory. Frugality — fire on the flip-beat @45 (the palm-closing) per the rubric's anti-pre-emption guidance distinguishing @43/@44/@45.

ANTI-PATTERN CHECK / CROSS-FACET: Narrator-interest @43 fires (`the letter returns by hand; the officer's mark is on it now`) — this is one-beat off from @45. **Co-citation concern flagged.** Per cross-facet contract, POV actor-state shifts require narrator-interest co-citation on the same `@<beat>`. Narrator-interest is silent at @45. Two interpretations: (i) the rubric's letter@45 calibration anchor was authored as a `prop:letter.holder` entry (studio's authority) — not as an `actor:taylor.inventory` entry — precisely because the POV co-citation requirement at @45 is unmet; (ii) the @43 narrator-interest fire stretches across the handover envelope. Conservative read: **WITHDRAW F1**. The studio-side `prop:letter.holder` entry at @45 captures the mutation; Taylor-side inventory is a duplicate-read of the same event without independent narrator-interest support at the flip-beat.

REVISED DECISION: NONE. (Withdraw F1 on cross-facet co-citation grounds. The letter's holder is studio's authority; Taylor's inventory tracking the held prop is implicit through the prop-side entry, and adding a Taylor-side duplicate without @45 narrator-interest co-citation would fail the cross-facet contract.)

---

### F2 — @77 taylor goes through the door (mask-state shift)

DECISION: FIRE

DRAFTS:
- (a) `@77 actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private`
- (b) `@77 actor:taylor-hebert-westeros.mask-state: in-public-yard -> off-public-stage`

CHOSEN: (a) — captures the mask-thinning content of the narrator-interest fire, not just the spatial transit.

ENTRY:
```
4 @77 actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private
```

RATIONALE: Reality — narrator-interest @77 fires `inside the frame her hand has stopped reaching for the half-curtsy` — the cooperative-child performance she sustained throughout the yard scene drops as she crosses the threshold; the mask-state shifts persistently (she is now interior, no public eyes, no requirement to perform). Per the persona card, the cooperative-child register is an active maintained performance under cost; releasing it is a real state-shift, not a transient. Authority — Taylor fork; `mask-state` is a licit field-extension (rubric §"Field-extension protocol" names mask-state as a tracked-state-aspect alongside knowledge, exposure-state, posture, inventory). Frugality — one entry on the flip-beat (the through-door commit at @77). Cross-facet: tensometer @77=1 (release zone, but rubric does not require non-1 tens for state-update — irreversible bureaucratic and mask-state shifts can fire on tens=1 if Reality holds); narrator-interest @77 fires explicitly with mask-thin content. POV co-citation satisfied.

ANTI-PATTERN CHECK: not registration-only (the mask-state genuinely flips: she is no longer performing for an audience; persistence holds into s01e02); not cross-POV; not held-against-turn; not compound; not drift-old (the maintained-cooperative-child baseline is established by persona card and by performance throughout the yard scene); not invented-field (mask-state is rubric-named tracked-aspect); not pre-empting (the flip lands at @77 commit, not at @73 frame-shadow approach); not posture-as-state; not density-on-flat; not stylistic noting.

---

### F3 — @23 actor:taylor.exposure-state shift (officer's gaze fixes on her)

CONSIDERED, REFUSED.

ANTI-PATTERN CHECK: Anti-pattern #1 (registration-as-state). The rubric explicitly names @23 as a REJECT signature: "*the officer's gaze fixes on taylor at the yard's far end* (@23) does not change a field on `actor:officer` (his gaze is a registration, not a posture-state); it is narrator-interest territory, not state-updates." A symmetric Taylor-side `exposure-state` write would be the same parasitic registration shifted to the perceiver. The narrator-interest fire (`the watch-cost has just been priced to her name`) is the registration; the canonical exposure-state on Taylor does not flip at @23 because the officer's attention is a transient gaze-targeting event, not a recorded condition. The exposure that *does* flip canonically is the @48 administrative-status (already covered by T2). Floor-defense.

---

### F4 — no further additions

The defensible POV actor-state shifts in s01e01 cluster at @48 (administrative) and @64 (knowledge.record-state) plus the @77 mask-thin. Other narrator-interest fires (@4 fauna-feed, @11 exits-count, @24 pause-commit, @30 name-on-line, @33/@34 refusal-to-look, @37 shoulder-path, @38/@39 body-charge, @43 letter-return, @52 ally-count, @57 cover-loss, @60 reduced-field, @63 stylus-margin, @69 wheel-tremor, @73 frame-shadow) are registration / perception / cost-tracking / approach-zone, not canonical Taylor-state mutations. Inflating fires past the defensible set is the prohibited move.

---

## Final entry list (Taylor fork output)

```
1 @48 actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible
2 @64 actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks
3 @77 actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private
```

Field-extensions declared (per rubric §"Field-extension protocol"):
- `administrative-status` — new field for s01e01 census tracking; tracked-state-aspect (administrative classification, persistent past beat, season-arc-load-bearing).
- `knowledge.record-state` — new field for POV knowledge of bureaucratic record; tracked-state-aspect (knowledge is rubric-named).
- `mask-state` — new field for cooperative-child performance state; tracked-state-aspect (mask-state is rubric-named in §"Field-extension protocol" example list).

---

## Curve check

- **Total fires:** 3 on `actor:taylor-hebert-westeros.*`.
- **Refusals:** 3 (T1 @39 held-against-turn; T4 @50 transient-posture; T5 @52 cross-POV trap). Plus 2 considered-and-refused free additions (F1 @45 inventory withdrawn on co-citation grounds; F3 @23 exposure-state as registration-only).
- **Target diversity within fork scope:** three distinct fields on the POV actor (administrative-status, knowledge.record-state, mask-state); covers the formal-record arc, the perceptual-knowledge arc, and the performance-arc.
- **Cross-facet self-check:** every fire has a narrator-interest co-citation on the exact `@<beat>` — @48 (✓ `she has heard the shape of that word...`), @64 (✓ `two strokes; the determination is on the record and on her`), @77 (✓ `inside the frame her hand has stopped reaching for the half-curtsy`). POV co-citation requirement satisfied for all three. Tensometer cross-facet contract honored: @39 refusal honors the locked STATE-UPDATE NOTE; @64 fire honors the strongly-expected co-citation slot.
- **Sparsity:** 3 / 77 = 3.9% of beats fired by this fork (POV actor-state only; environment and props are studio's; other actors are their own forks). Aggregate file density across all forks should land in the 8–18% band per rubric.
