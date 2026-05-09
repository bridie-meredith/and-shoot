## chapter-01 pass-2 repairs — 2026-05-07

chapter-01 | fault-001 | RECAST-PHYSICAL: removed prepositional padding | `septon-dying-protector breathes in the cottage below` → `septon-dying-protector breathes`
chapter-01 | fault-002 | RECAST-PHYSICAL: removed prepositional padding | `the ravens call in the bell tower` → `the ravens call`
chapter-01 | fault-003 | RECAST-PHYSICAL: removed adverb modifier | `the sept candles gutter low` → `the sept candles gutter`
chapter-01 | fault-004 | RECAST-PHYSICAL: removed prepositional padding | `taylor-hebert-westeros lights a candle at the altar` → `taylor-hebert-westeros lights a candle`
chapter-01 | fault-005 | RECAST-PHYSICAL: removed prepositional padding | `taylor-hebert-westeros opens a book at the altar table` → `taylor-hebert-westeros opens a book`
chapter-01 | fault-006 | RECAST-PHYSICAL: removed prepositional padding | `a village woman knocks at the cottage door` → `a village woman knocks`
chapter-01 | fault-007 | RECAST-PHYSICAL: removed prepositional padding | `septon-dying-protector stirs on the bed` → `septon-dying-protector stirs`
chapter-01 | fault-008 | RECAST-PHYSICAL: removed prepositional padding | `the village woman sets the broth pot on the table` → `the village woman sets the broth pot`
chapter-01 | fault-009 | RECAST-PHYSICAL: removed prepositional padding | `the ravens flush from the bell tower` → `the ravens flush`
chapter-01 | fault-010 | RECAST-PHYSICAL: removed directional padding | `three riders crest the road from the north` → `three riders crest the road`
chapter-01 | fault-011 | RECAST-PHYSICAL: removed prepositional padding | `the riders stop at the sept yard gate` → `the riders stop`
chapter-01 | fault-012 | RECAST-PHYSICAL: transitive recast preserving destination weight | `taylor-hebert-westeros steps back` → `taylor-hebert-westeros retreats`
chapter-01 | fault-013 | RECAST-PHYSICAL: removed prepositional padding (also covered by fault-048 slug rename) | `oc-castellan-harrenhal's officer knocks at the cottage door` → `census-officer knocks`
chapter-01 | fault-014 | RECAST-PHYSICAL: removed prepositional padding (also fault-048) | `oc-castellan-harrenhal's officer makes a notation on the scroll` → `census-officer makes a notation`
chapter-01 | fault-015 | RECAST-PHYSICAL: removed adverb, collapsed to intransitive | `septon-dying-protector falls back` → `septon-dying-protector falls`
chapter-01 | fault-016 | RECAST-PHYSICAL: removed adjective modifier (also fault-048) | `oc-castellan-harrenhal's officer produces a writing quill` → `census-officer produces a quill`
chapter-01 | fault-017 | ABSORBED: line 89 blanked; beat absorbed by fault-040 resolution (quill-drop is downstream of release on line 88) | `the quill drops to the floor` → [blanked; ID 89 preserved as gap]
chapter-01 | fault-018 | RECAST-PHYSICAL: removed adverb (also fault-048) | `oc-castellan-harrenhal's officer marks the scroll again` → `census-officer marks the scroll`
chapter-01 | fault-019 | RECAST-PHYSICAL: removed adjective modifier | `a man-at-arms produces a second scroll` → `a man-at-arms produces a scroll`
chapter-01 | fault-020 | RECAST-PHYSICAL: removed prepositional+adjective padding (also fault-048) | `oc-castellan-harrenhal's officer makes a notation on the second scroll` → `census-officer makes a notation`
chapter-01 | fault-021 | RECAST-PHYSICAL: removed prepositional padding | `taylor-hebert-westeros holds the feet in the yard` → `taylor-hebert-westeros holds the feet`
chapter-01 | fault-022 | RECAST-PHYSICAL: removed adverb+prepositional padding | `the riders turn north on the Harrenhal road` → `the riders turn`
chapter-01 | fault-023 | RECAST-PHYSICAL: removed prepositional padding | `the ravens resettle in the bell tower` → `the ravens resettle`
chapter-01 | fault-024 | RECAST-PHYSICAL: removed directional padding | `taylor-hebert-westeros turns from the window` → `taylor-hebert-westeros turns`
chapter-01 | fault-025 | RECAST-PHYSICAL: removed adjective modifier | `taylor-hebert-westeros takes the septon's writing materials` → `taylor-hebert-westeros takes the septon's materials`
chapter-01 | fault-026 | RECAST-PHYSICAL: substituted verb to avoid adverb | `taylor-hebert-westeros sets the book down` → `taylor-hebert-westeros places the book`
chapter-01 | fault-027 | RECAST-PHYSICAL: removed prepositional padding | `taylor-hebert-westeros kneels at the altar` → `taylor-hebert-westeros kneels`
chapter-01 | fault-028 | DELETE: perception verb, no clean physical recast; line 8 blanked | `taylor-hebert-westeros scans the Harrenhal road` → [deleted; route to narrator/feel facet citing line 7]
chapter-01 | fault-029 | DELETE: perception verb per audit recommendation; line 16 blanked | `taylor-hebert-westeros reads the page` → [deleted; route to narrator/feel facet citing line 15]
chapter-01 | fault-030 | RECAST-PHYSICAL: perception verb recast as physical orientation, modifier dropped | `the village woman glances toward the Harrenhal road` → `the village woman turns`
chapter-01 | fault-031 | DELETE: perception verb, repeat instance; line 33 blanked | `taylor-hebert-westeros scans the Harrenhal road` → [deleted; route to narrator/feel facet citing line 32]
chapter-01 | fault-032 | RECAST-PHYSICAL: perception verb recast as physical orientation (also fault-048) | `oc-castellan-harrenhal's officer looks at taylor-hebert-westeros` → `census-officer turns toward taylor-hebert-westeros`
chapter-01 | fault-033 | RECAST-PHYSICAL: perception verb recast as physical orientation per audit alternative (also fault-048) | `oc-castellan-harrenhal's officer scans the outbuildings` → `census-officer turns toward the outbuildings`
chapter-01 | fault-034 | DELETE: perception verb; line 62 blanked; blank ID preserved as structural gap (also fault-048) | `oc-castellan-harrenhal's officer sees septon-dying-protector on the bed` → [deleted; septon bed-location to state-update facet]
chapter-01 | fault-035 | RECAST-PHYSICAL: idiomatic perception act replaced with physical body-orientation | `taylor-hebert-westeros meets the officer's eyes` → `taylor-hebert-westeros raises her eyes`
chapter-01 | fault-036 | DELETE: perception verb, third instance; line 120 blanked | `taylor-hebert-westeros scans the Harrenhal road` → [deleted; route to narrator/feel facet citing line 119]
chapter-01 | fault-037 | RECAST-PHYSICAL: stative flank recast as discrete positioning act; "beside" modifier retained as minimum viable form — flag for auditor re-review | `two men-at-arms flank a mounted official` → `two men-at-arms take position beside the official`
chapter-01 | fault-038 | DELETE: stative environment-observation, redundant with line 47; line 36 blanked | `a packaged scroll protrudes from the official's saddlebag` → [deleted; route to location-state facet]
chapter-01 | fault-039 | RECAST-PHYSICAL: stative flank recast as motion act (also fault-048) | `the men-at-arms flank the yard entrance` → `the men-at-arms cross to the yard entrance`
chapter-01 | fault-040 | RECAST-PHYSICAL: stative-result verb replaced; actor restored as subject; line 89 blanked as now-redundant downstream | `septon-dying-protector's hand fails` → `septon-dying-protector releases the quill`; line 89 blanked
chapter-01 | fault-041 | DELETE: stative/perceptual gradual-change verb; line 121 blanked | `the riders diminish on the northern road` → [deleted; route to narrator/feel facet]
chapter-01 | fault-042 | RECAST-PHYSICAL: unlicensed abstract-object hold replaced with licensed body-part hold | `taylor-hebert-westeros holds the position` → `taylor-hebert-westeros holds the spine`
chapter-01 | fault-043 | SPLIT-INTO-N: intent verb split into two observable beats | `septon-dying-protector attempts to rise` → line 71: `septon-dying-protector rises`; line 72: `septon-dying-protector falls`
chapter-01 | fault-044 | RECAST-PHYSICAL: perception-noun object replaced with physical body-part object | `taylor-hebert-westeros drops her gaze` → `taylor-hebert-westeros lowers her eyes`
chapter-01 | fault-045 | RECAST-PHYSICAL: intent verb replaced with observable physical act | `septon-dying-protector attempts a signature` → `septon-dying-protector marks the scroll`
chapter-01 | fault-046 | DELETE: copula-equivalent stative construction; line 9 blanked | `the road shows empty` → [deleted; route to narrator/feel or location-state facet]
chapter-01 | fault-047 | RECAST-PHYSICAL: invalid location-listener replaced with physical call-out act | `oc-castellan-harrenhal's officer speaks to the yard` → `census-officer calls out`
chapter-01 | fault-048 | RENAME-SLUG: global replace throughout file | `oc-castellan-harrenhal's officer` → `census-officer` (all subject lines)

---

## chapter-01 pass-2 re-verify repairs — 2026-05-07

chapter-01 | pass2-fault-001 | RECAST-AS-BARE-NOUN: modifier "sept" stripped from subject | `the sept candles gutter` → `the candles gutter`
chapter-01 | pass2-fault-002 | RECAST-AS-BARE-NOUN: indefinite article + modifier stripped; character renamed to consistent bare slug | `a village woman knocks` → `the woman knocks`
chapter-01 | pass2-fault-003 | RECAST-AS-BARE-NOUN: subject "village woman" → "the woman"; object "broth pot" → "the pot" | `the village woman lifts the broth pot` → `the woman lifts the pot`
chapter-01 | pass2-fault-004 | RECAST-AS-BARE-NOUN: subject modifier stripped | `the village woman enters the cottage` → `the woman enters the cottage`
chapter-01 | pass2-fault-005 | RECAST-AS-BARE-NOUN: subject and object both stripped of modifiers | `the village woman sets the broth pot` → `the woman sets the pot`
chapter-01 | pass2-fault-006 | RECAST-AS-BARE-NOUN: subject modifier stripped | `the village woman speaks to taylor-hebert-westeros` → `the woman speaks to taylor-hebert-westeros`
chapter-01 | pass2-fault-007 | RECAST-AS-BARE-NOUN: listener reference modifier stripped | `taylor-hebert-westeros speaks to the village woman` → `taylor-hebert-westeros speaks to the woman`
chapter-01 | pass2-fault-008 | RECAST-AS-BARE-NOUN: subject modifier stripped | `the village woman turns` → `the woman turns`
chapter-01 | pass2-fault-009 | RECAST-AS-BARE-NOUN: subject modifier stripped | `the village woman exits the cottage` → `the woman exits the cottage`
chapter-01 | pass2-fault-010 | RECAST-AS-BARE-NOUN: numeral "three" stripped; consistent with "the riders" at lines 44, 112, 113 | `three riders crest the road` → `the riders crest the road`
chapter-01 | pass2-fault-011 | RECAST-PHYSICAL: numeral stripped, prepositional padding removed, "the official" → census-officer for consistency; recast as discrete motion act | `two men-at-arms take position beside the official` → `the men-at-arms follow census-officer`
chapter-01 | pass2-fault-012 | RECAST-AS-BARE-NOUN: modifier "writing" stripped from object | `taylor-hebert-westeros crosses to the writing materials` → `taylor-hebert-westeros crosses to the materials`
chapter-01 | pass2-fault-013 | RECAST-AS-BARE-NOUN: modifier "census" stripped from scroll object | `census-officer produces the census scroll` → `census-officer produces the scroll`
chapter-01 | pass2-fault-014 | RECAST-AS-BARE-NOUN: modifier "census" stripped from scroll object | `census-officer unrolls the census scroll` → `census-officer unrolls the scroll`
chapter-01 | pass2-fault-015 | RECAST-AS-BARE-NOUN: possessive "her" → definite article "the" | `taylor-hebert-westeros raises her eyes` → `taylor-hebert-westeros raises the eyes`
chapter-01 | pass2-fault-016 | RECAST-AS-BARE-NOUN: possessive "her" → definite article "the" | `taylor-hebert-westeros lowers her eyes` → `taylor-hebert-westeros lowers the eyes`
chapter-01 | pass2-fault-017 | RECAST-PHYSICAL: prepositional particle "for" removed; direct transitive | `septon-dying-protector reaches for the quill` → `septon-dying-protector reaches the quill`
chapter-01 | pass2-fault-018 | RECAST-AS-BARE-NOUN: modifier "census" stripped from scroll object | `census-officer rolls the census scroll` → `census-officer rolls the scroll`
chapter-01 | pass2-fault-019 | RECAST-PHYSICAL: non-action verb + abstract object replaced with discrete physical act per criteria option (b) | `taylor-hebert-westeros holds the chin angle` → `taylor-hebert-westeros lifts the chin`
chapter-01 | pass2-fault-020 | RECAST-AS-BARE-NOUN: indefinite article "a" → "the" on subject | `a man-at-arms produces a scroll` → `the man-at-arms produces a scroll`
chapter-01 | pass2-fault-021 | RECAST-AS-BARE-NOUN: possessive "his" → "the" | `septon-dying-protector closes his eyes` → `septon-dying-protector closes the eyes`
chapter-01 | pass2-fault-022 | RETAINED: anatomical hold is licensed per schema; book not in hand at line 131; no prop-spine reading survives context; line valid as-is
chapter-01 | pass2-flag-003-promoted | RECAST-AS-BARE-NOUN: possessive "his" → "the"; same class as fault-021; promoted per audit direction | `septon-dying-protector opens his eyes` → `septon-dying-protector opens the eyes`

DEPENDENCY FLAG: flag-001 — slug "census-officer" has no oc-* card in the library. Introduced by pass-1 fault-048 global rename. Margit referral required before Pass 5 continuity review. Fixer has not chained this repair; flagging for showrunner direction.

---

## season-S2-shape structural revisions — 2026-05-07

### Revision 1 — chapter-03.md (NO-CLIMAX flag: CHAPTER-STRUCTURAL-FAILURE-03)

**Trigger:** Pass S2 shape verdict: 44 lines of holding/sensing with no agency-meets-resistance beat.
**Goal:** Convert atmospheric absence into failed-attempt structure. Preserve "she cannot reach what caused it" while making the gap dramatic.
**Intended narrative position:** after ID 26 (`a cart passes the sept`), before ID 28 (chapel entry).
**Beats appended (IDs 45–47):**

```
45 taylor-hebert-westeros drives a raven toward the road
46 the raven drops
47 taylor-hebert-westeros presses the temples
```

ID 45: Taylor extends fauna-control toward the cart (agency). ID 46: the raven fails — drops rather than tracks (resistance closes). ID 47: physical cost marker, narrator POV, somatic-only. Three proto-lines form one dramatic unit. No motivation clauses, no `turns to <X>`, no perception verbs, no modifiers. First-person narrator (taylor-hebert-westeros) throughout. New IDs are next monotonic integers after existing max (44).

**Criteria met:** yes — agency-meets-resistance beat present; chapter goal intact; SVO clean.

---

### Revision 2 — chapter-08.md (NO-CLIMAX flag: CHAPTER-STRUCTURAL-FAILURE-08; E5 forward-flag violation)

**Trigger:** Pass S2 shape verdict: primary narrator chapter at season peak ends in stalemate posture (palms on table); E5 flag ("irreversible board action, not stalemate") honored in interlude only, not reaching Taylor.
**Goal:** Convert palms-on-table from waiting posture to landed consequence. One post-interlude line where the hall's outcome reaches Taylor.
**Beat appended (ID 96):**

```
96 a raven strikes the bell tower beam
```

The stationed raven returns agitated — an observable external event reaching Taylor inside the cottage. Physical SVO, no motivation clause, no `turns to <X>`. ID 96 is next monotonic integer after existing max (95). Taylor-hebert-westeros first-person POV implied by cottage setting; no interiority stated.

**Criteria met:** yes — consequence arrives; E5 forward-flag honored in primary file; palms-on-table is no longer the chapter's final state.

---

## fault-001 — RESOLVED
fault: line 58 "a girl appears the mill hamlet road edge" — existential verb, no actor action
scope: line
change: recast to "oc-girl-from-hamlet rounds the mill hamlet road edge" — physical movement verb, named actor
criteria met: yes

## fault-002 — RESOLVED
fault: line 31 "the headache starts" — state-onset verb, no actor action
scope: line
change: recast to "taylor-hebert-westeros presses the temples" — physical action marks onset
criteria met: yes

## fault-003 — RESOLVED
fault: line 52 "the nosebleed starts" — state-onset verb, no actor action
scope: line
change: recast to "blood marks the lip" — physical event, active verb
criteria met: yes

## fault-004 — RESOLVED
fault: protagonist named "Taylor" throughout ch02 instead of slug "taylor-hebert-westeros"
scope: line (global replace)
change: replace_all Taylor → taylor-hebert-westeros across chapter-02.md
criteria met: yes

---

chapter-03 | structural-narrator-escalation | full re-author with fauna-feed framing

---

## chapter-04 pass-2 repairs — 2026-05-07

chapter-04 | fault-001 | RECAST-PHYSICAL: dropped false location-object | `the riders dismount the north track` → `the riders dismount`
chapter-04 | fault-002 | RECAST-PHYSICAL: dropped measurement qualifier | `oc-castellan-harrenhal walks the nave length` → `oc-castellan-harrenhal walks the nave`
chapter-04 | fault-003 | RECAST-PHYSICAL: `turns to` recast as transitive directional verb | `oc-castellan-harrenhal turns to the raven` → `oc-castellan-harrenhal faces the raven`
chapter-04 | fault-004 | RECAST-PHYSICAL: dropped prepositional directional phrase | `the raven swings the head to oc-castellan-harrenhal` → `the raven swings the head`
chapter-04 | fault-005 | RECAST-PHYSICAL: instrument-as-object replaced with physical target as object | `the raven digs the talons` → `the raven clamps the arm`
chapter-04 | fault-006 | RECAST-PHYSICAL: achievement verb replaced with final observable physical act | `ser-harwick-plumm completes the sketch` → `ser-harwick-plumm lifts the stylus`
chapter-04 | fault-007 | RECAST-PHYSICAL: perception verb replaced with observable physical handling act | `oc-castellan-harrenhal examines the page` → `oc-castellan-harrenhal turns the page`
chapter-04 | fault-008 | RECAST-PHYSICAL: `turns to` recast as transitive directional verb (same ruling as fault-003) | `oc-castellan-harrenhal turns to the bell tower` → `oc-castellan-harrenhal faces the bell tower`

---

## fault-001 — RESOLVED
fault: line 11 `the riders dismount the north track` — location as false direct object
scope: line
change: `the riders dismount` — intransitive; location context routes to citation at facet time
criteria met: yes

## fault-002 — RESOLVED
fault: line 17 `oc-castellan-harrenhal walks the nave length` — measurement abstraction as object qualifier
scope: line
change: `oc-castellan-harrenhal walks the nave` — `length` dropped
criteria met: yes

## fault-003 — RESOLVED
fault: line 62 `oc-castellan-harrenhal turns to the raven` — `to X` prepositional directional phrase, not direct object
scope: line
change: `oc-castellan-harrenhal faces the raven` — transitive directional verb, raven is direct object
criteria met: yes

## fault-004 — RESOLVED
fault: line 63 `the raven swings the head to oc-castellan-harrenhal` — directional phrase appended after complete SVO
scope: line
change: `the raven swings the head` — directional phrase stripped
criteria met: yes

## fault-005 — RESOLVED
fault: line 68 `the raven digs the talons` — instrument retained as object instead of physical target
scope: line
change: `the raven clamps the arm` — Taylor's arm named as direct object of grip action
criteria met: yes

## fault-006 — RESOLVED
fault: line 75 `ser-harwick-plumm completes the sketch` — achievement/state-termination verb, not discrete physical act
scope: line
change: `ser-harwick-plumm lifts the stylus` — final observable physical act of drawing; completion inference is downstream
criteria met: yes

## fault-007 — RESOLVED
fault: line 78 `oc-castellan-harrenhal examines the page` — perception-inspection verb, not physical act
scope: line
change: `oc-castellan-harrenhal turns the page` — discrete physical handling act an observer can verify
criteria met: yes

## fault-008 — RESOLVED
fault: line 86 `oc-castellan-harrenhal turns to the bell tower` — identical structure to fault-003, directional `to X` phrase
scope: line
change: `oc-castellan-harrenhal faces the bell tower` — same ruling applied uniformly with fault-003
criteria met: yes

---

## chapter-10 pass-2 repairs — 2026-05-07

## ch10-fault-001 — RESOLVED
fault: line 4 `ser-harwick-plumm sets the census file on the table` — prepositional destination padding
scope: line
change: `ser-harwick-plumm sets the census file` — "on the table" dropped; destination routes to location-state facet citation
criteria met: yes

## ch10-fault-002 — RESOLVED
fault: line 10 `oc-castellan-harrenhal sets the census file down` — directional adverb "down"
scope: line
change: `oc-castellan-harrenhal sets the census file` — "down" dropped; direction implicit from prior lift on line 7
criteria met: yes

## ch10-fault-003 — RESOLVED
fault: line 26 `taylor-hebert-westeros holds the chin angle` — abstract compound noun object, not body part
scope: line
change: `taylor-hebert-westeros holds the chin` — "angle" dropped; licensed hold-body-part form restored
criteria met: yes

## ch10-fault-004 — RESOLVED
fault: line 41 `ser-harwick-plumm presses the seal into the wax` — prepositional destination phrase
scope: line
change: `ser-harwick-plumm presses the seal` — "into the wax" dropped; contact state routes to state-update facet
criteria met: yes

## ch10-fault-005 — RESOLVED
fault: line 42 `ser-harwick-plumm lifts the seal off the wax` — prepositional source phrase
scope: line
change: `ser-harwick-plumm lifts the seal` — "off the wax" dropped; seal-impression state routes to state-update facet
criteria met: yes

## ch10-fault-006 — RESOLVED
fault: line 48 `taylor-hebert-westeros drops the gaze to the floor` — interiority object ("gaze") + prepositional padding; primary fault FAULT-FORM-INTERIORITY
scope: line
change: `taylor-hebert-westeros drops the chin` — physical body-part recast per audit criteria; attentional/perceptual content routes to feeling-flag facet
criteria met: yes

---

## chapter-09 pass-2 repairs — 2026-05-07

chapter-09 | fault-001 | DELETE: `the man-at-arms blocks the doorway` (old line 19) — state-naming of line 18's result; line 18 carries the full act
chapter-09 | fault-002 | RECAST-PHYSICAL: `ser-aemon-bracken draws a folded page` → `ser-aemon-bracken draws a page` — adjective modifier dropped; prop condition routes to facet
chapter-09 | fault-003 | DELETE: `oc-castellan-harrenhal reads the page` (old line 40) — perception verb; lines 39 (lifts) and 41 (sets beside) bracket the beat adequately
chapter-09 | fault-004 | RECAST-PHYSICAL: `ser-edwyn-celtigar rides beside the cart` → `ser-edwyn-celtigar rides` — prepositional spatial phrase dropped; pure intransitive motion
chapter-09 | fault-005 | DELETE: `two riders flank the cart` — spatial arrangement assertion; unnamed environmental detail; cart entry covers arrival beat
chapter-09 | fault-006 | RECAST-PHYSICAL: `the guard examines the document` → `the guard turns the document` — perception-evaluation verb replaced with observable physical handling act
chapter-09 | fault-007 | RECAST-PHYSICAL: `oc-castellan-harrenhal receives ser-edwyn-celtigar` → `oc-castellan-harrenhal turns to ser-edwyn-celtigar` — social-ceremonial state replaced with discrete physical act
chapter-09 | fault-008 | RECAST-PHYSICAL: `ser-edwyn-celtigar examines the document` → `ser-edwyn-celtigar turns the document` — perception-evaluation verb replaced with physical handling act (parallel with fault-009)
chapter-09 | fault-009 | RECAST-PHYSICAL: `ser-edwyn-celtigar examines the page` → `ser-edwyn-celtigar turns the page` — perception-evaluation verb replaced with physical handling act (parallel with fault-008)
chapter-09 | fault-010 | RECAST-PHYSICAL: `taylor-hebert-westeros presses the palms flat` → `taylor-hebert-westeros presses the palms` — adverbial modifier "flat" dropped
chapter-09 | fault-011 | RECAST-PHYSICAL: `taylor-hebert-westeros holds the chin angle` → `taylor-hebert-westeros lifts the chin` — abstract compound noun replaced with licensed body-part hold-initiation act

Post-repair: proto-line numbering resequenced end-to-end to close gaps left by three deletions (former lines 19, 40, 70). No facet citations existed on this chapter prior to this pass; no downstream citation breakage.

---

## chapter-07 pass-2 re-verify repairs — 2026-05-07

chapter-07 | fault-001 | RECAST-PHYSICAL: perception verb replaced with physical handling act | `the recorder scans Rowan's filing` → `the recorder taps the filing`
chapter-07 | fault-002 | RECAST-PHYSICAL: stative positional verb replaced with discrete arrival act | `taylor-hebert-westeros leans against the counter` → `taylor-hebert-westeros steps to the counter`
chapter-07 | fault-003 | RECAST-PHYSICAL: perception/cognitive verb replaced with physical marking act; prepositional destination phrase stripped simultaneously | `the recorder notes the cross-reference to Rowan's entry` → `the recorder marks the cross-reference entry`
chapter-07 | fault-004 | DELETE (prepositional tail) | `taylor-hebert-westeros stops on the road` → `taylor-hebert-westeros stops`
chapter-07 | fault-005 | DELETE (prepositional directional phrase) | `taylor-hebert-westeros turns back toward Harrenhal` → `taylor-hebert-westeros turns`
chapter-07 | fault-006 | RECAST-PHYSICAL: stative positional replaced with discrete seating act | `taylor-hebert-westeros sits at the table` → `taylor-hebert-westeros takes the chair`
chapter-07 | fault-007 | DELETE (possessive modifier + prepositional destination phrase) | `septon-rowan sets his satchel on the table` → `septon-rowan sets the satchel down`
chapter-07 | fault-008 | DELETE (possessive modifier only) | `septon-rowan opens his satchel` → `septon-rowan opens the satchel`
chapter-07 | fault-009 | DELETE (prepositional destination phrase) | `taylor-hebert-westeros sets the document on the table` → `taylor-hebert-westeros sets the document down`
chapter-07 | fault-010 | DELETE (prepositional origin phrase) | `a raven launches from the bell tower` → `a raven launches`
chapter-07 | fault-011 | DELETE (prepositional location phrase) | `taylor-hebert-westeros stops at the garden wall` → `taylor-hebert-westeros stops`
chapter-07 | fault-012 | DELETE (prepositional chain on object) | `taylor-hebert-westeros grips the top of the garden wall` → `taylor-hebert-westeros grips the wall`
chapter-07 | fault-013 | DELETE (prepositional destination + possessive modifier) | `the recorder adds a notation to Plumm's entry` → `the recorder adds a notation`
chapter-07 | fault-014 | DELETE (prepositional location phrase) | `taylor-hebert-westeros kneels at the altar` → `taylor-hebert-westeros kneels`
chapter-07 | fault-015 | DELETE (prepositional origin phrase) | `taylor-hebert-westeros rises from the altar` → `taylor-hebert-westeros rises`
chapter-07 | fault-016 | RECAST-PHYSICAL: prepositional destination recast as direct object | `taylor-hebert-westeros crosses to the sept door` → `taylor-hebert-westeros crosses the sept door`
chapter-07 | fault-017 | INSERT (prop-absent): new proto-line 93 inserted before line 17 to establish inventory prior to entry | `93 ser-harwick-plumm takes the claim document` — placed between time-skip 16 and entry beat 17; existing IDs preserved; ID 93 is next available integer in file

---

## chapter-02 pass-2 repairs — 2026-05-07

chapter-02 | fault-001 | RECAST: removed directional adverb | `plumms-man mounts the road south` → `plumms-man mounts the road`
chapter-02 | fault-002 | RECAST: removed adjective modifier on object | `the raven crosses the south field` → `the raven crosses the field`
chapter-02 | fault-003 | RECAST: removed ordinal adjective | `plumms-man reaches the first farmstead boundary` → `plumms-man reaches the farmstead boundary`
chapter-02 | fault-004 | RECAST: removed adverbial sequence modifier | `plumms-man marks the ledger a second time` → `plumms-man marks the ledger`
chapter-02 | fault-005 | RECAST: removed repetition adverb | `plumms-man mounts the road again` → `plumms-man mounts the road`
chapter-02 | fault-006 | RECAST: removed adjective modifier on object | `plumms-man crests the low rise` → `plumms-man crests the rise`
chapter-02 | fault-007 | RECAST: removed ordinal + em-dash clause | `plumms-man reaches the second location — the dead orchard boundary` → `plumms-man reaches the orchard boundary`
chapter-02 | fault-008 | RECAST: removed adjective modifier on object | `three ravens settle the dead apple tree` → `three ravens settle the apple tree`
chapter-02 | fault-009 | RECAST: stative position verb replaced with discrete landing action | `the ravens hold the branch` → `the ravens settle the branch`
chapter-02 | fault-010 | RECAST: removed adverbial sequence modifier | `plumms-man marks the ledger a third time` → `plumms-man marks the ledger`
chapter-02 | fault-011 | RECAST: removed ordinal + em-dash clause | `plumms-man marks a fourth entry — date, location` → `plumms-man marks the entry`
chapter-02 | fault-012 | RECAST: state-description verb replaced with discrete flow event | `blood marks the lip` → `blood reaches the lip`
chapter-02 | fault-013 | RECAST: removed possessive modifier on object | `plumms-man marks the girl's description` → `plumms-man marks the description`
chapter-02 | fault-014 | RECAST: removed em-dash annotation | `plumms-man marks the location — mill hamlet road` → `plumms-man marks the location`
chapter-02 | fault-015 | RECAST: removed compound-noun descriptor on object | `the girl rounds the road bend` → `the girl rounds the bend`
chapter-02 | fault-016 | RECAST: removed possessive + adjective double modifier | `plumms-man reaches Harrenhal's outer wall` → `plumms-man reaches Harrenhal`
chapter-02 | fault-017–021 | RECAST (block): transcription block differentiated by physical sub-act; ordinals and em-dash annotations stripped; five distinct beats: `takes the quill` / `dips the quill` / `marks the entry` / `turns the page` / `marks the entry`

## chapter-02 fault-022 — DEPENDENCY-FLAGGED
fault: slug `plumms-man` used as subject on ~40 lines; no card exists; character is Plumm's retainer doing field-recording work inconsistent with ser-harwick-plumm (knight); cannot be renamed to existing cast slug without misattributing action
scope: card (requires margit) then global rename
change: NONE applied — requires margit to author `oc-plumms-man` card before rename proceeds; all `plumms-man` lines untouched pending card
criteria met: no — blocked on card authoring

## chapter-02 fault-023 — DEPENDENCY-FLAGGED
fault: slug `oc-girl-from-hamlet` used as subject line 58 and referenced lines 61–64, 73; no card at active-project/warehouse/oc-girl-from-hamlet.card.md
scope: card (requires margit) then slug confirmation
change: NONE applied — slug is correct and consistent; card must be authored by margit; line untouched pending card
criteria met: no — blocked on card authoring

---

## chapter-08 pass-2 re-verify repairs — 2026-05-07

chapter-08 | fault-001 | RECAST-PHYSICAL: perception verb replaced with physical handling beat | `reads the word-list aloud` → `taps the word-list`
chapter-08 | fault-002 | DELETE-APPOSITIVE: em-dash appositive tail stripped from object | `produces a sketch — a diagram of grain-measures` → `produces a sketch`
chapter-08 | fault-003 | RECAST-PHYSICAL: adjective modifier + locative PP stripped; pinning verb substituted | `presses the hands flat on the knees` → `pins the hands to the knees`
chapter-08 | fault-004 | DELETE: non-action stative verb; interior frozen-state routes to feeling-flag facet | `roots the feet to the floor` → [line 27 blanked]
chapter-08 | fault-005 | RECAST-PHYSICAL: perception verb replaced with physical handling beat | `reads the document` → `taps the document`
chapter-08 | fault-006 | RECAST-PHYSICAL: bare intransitive departure recast with observable landing | `withdraws from the table` → `steps back from the table`
chapter-08 | fault-007 | RECAST-PHYSICAL: perception verb replaced with physical handling beat | `reads the counter-claim document` → `turns the counter-claim document`
chapter-08 | fault-008 | DELETE-LOCATIVE-PP: prepositional location phrase stripped; bare intransitive retained | `stops at the chancel step` → `stops`
chapter-08 | fault-009 | RECAST-PHYSICAL: perception verb replaced with physical handling beat | `reads the letter` → `taps the letter`
chapter-08 | fault-010 | RECAST-PHYSICAL: perception verb + adverb modifier replaced with speech-act verb | `reads the letter aloud` → `speaks the letter`
chapter-08 | fault-011 | DELETE-MODIFIER: adjective `controlled` removed | `draws a controlled breath` → `draws a breath`
chapter-08 | fault-012 | DELETE: negation construction + indefinite collective subject; silence routes to feeling/sensory facet | `those present do not speak` → [line 81 blanked]
chapter-08 | fault-013 | DELETE-CONJUNCTION+LOCATIVE: conjoined locative PP dropped; bare SVO retained | `places the letter beside the sealed roll and the counter-claim` → `places the letter`
chapter-08 | fault-014 | RECAST: indefinite collective subject replaced with object-as-subject licensed form | `those present file out of the hall` → `the hall empties`
chapter-08 | fault-015 | DELETE-ADVERB: adverb `last` removed; named destination added | `exits last` → `exits the hall`
chapter-08 | fault-016 | RECAST-PHYSICAL: stative positional `sits at` replaced with discrete seating act | `sits at the septon's table` → `takes the septon's seat`
chapter-08 | fault-017 | RECAST-PHYSICAL: adjective modifier + locative PP stripped; pinning verb substituted (mirrors fault-003 pattern) | `presses the palms flat on the table` → `pins the palms to the table`

---

## chapter-06 pass-2 repairs — 2026-05-07

chapter-06 | fault-001 | RECAST-PHYSICAL: perception verb `scans` replaced with physical body-orientation; Harrenhal road retained as direct object per motion-verb destination rule | `taylor-hebert-westeros scans the Harrenhal road` → `taylor-hebert-westeros turns toward the Harrenhal road`
chapter-06 | fault-002 | DELETE-MODIFIER: directional adverb `south` stripped | `taylor-hebert-westeros turns south` → `taylor-hebert-westeros turns`
chapter-06 | fault-003 | DELETE-MODIFIER: prepositional destination phrase stripped | `septon-rowan crosses to his writing table` → `septon-rowan crosses`
chapter-06 | fault-004 | RECAST-PHYSICAL: directional particle `down` removed; verb substituted to avoid implied direction | `septon-rowan sets the stylus down` → `septon-rowan places the stylus`
chapter-06 | fault-005 | DELETE-MODIFIER: temporal adverb `again` stripped | `septon-rowan takes the stylus again` → `septon-rowan takes the stylus`
chapter-06 | fault-006 | DELETE-MODIFIER: result-state adjective `dry` stripped | `septon-rowan blows the ink dry` → `septon-rowan blows the ink`
chapter-06 | fault-007 | RECAST-PHYSICAL: perception verb `watches` replaced with physical body-orientation; septon-rowan retained as direct object (transitive directional verb) | `taylor-hebert-westeros watches septon-rowan` → `taylor-hebert-westeros turns toward septon-rowan`
chapter-06 | fault-008 | DELETE-MODIFIER: adverb `back` and prepositional phrase `toward the bell tower` stripped | `taylor-hebert-westeros turns back toward the bell tower` → `taylor-hebert-westeros turns`
chapter-06 | fault-009 | RECAST-PHYSICAL: abstract-object interiority line replaced with concrete fauna-activation beat (raven drop); network-extension state routes to state-update facet | `taylor-hebert-westeros extends the network` → `a raven drops from the tower lip`
chapter-06 | fault-010 | DELETE-MODIFIER: manner modifier `in two groups` stripped (repaired in same edit as fault-009) | `the ravens lift in two groups` → `the ravens lift`
chapter-06 | fault-011 | DELETE-MODIFIER: adjective `north` stripped from object | `the first group crosses the north field` → `the first group crosses the field`
chapter-06 | fault-012 | DELETE-MODIFIER: prepositional destination phrase stripped | `the second group banks toward the Harrenhal road` → `the second group banks`
chapter-06 | fault-013 | DELETE-MODIFIER: prepositional phrase `to her temple` stripped | `taylor-hebert-westeros presses a fist to her temple` → `taylor-hebert-westeros presses a fist`
chapter-06 | fault-014 | DELETE-MODIFIER: comparative adverb `harder` and prepositional phrase `against the temple` stripped | `taylor-hebert-westeros presses the fist harder against the temple` → `taylor-hebert-westeros presses the fist`
chapter-06 | fault-015 | DELETE-MODIFIER: directional adverb `south` stripped | `the courier mounts the road south` → `the courier mounts the road`
chapter-06 | fault-016 | DELETE-MODIFIER: adverb `low` and prepositional phrase `over the road` stripped | `the ravens drop low over the road` → `the ravens drop`
chapter-06 | fault-017 | DELETE-MODIFIER: temporal adverb `again` stripped | `the courier reins the horse again` → `the courier reins the horse`
chapter-06 | fault-018 | DELETE-MODIFIER: directional adverb `wide` stripped | `taylor-hebert-westeros pulls the second group wide` → `taylor-hebert-westeros pulls the second group`
chapter-06 | fault-019 | DELETE-MODIFIER: directional adverb `north` stripped | `the second group wheels north` → `the second group wheels`
chapter-06 | fault-020 | DELETE-MODIFIER: adjective `full` stripped from object | `the courier's horse turns a full circle` → `the courier's horse turns a circle`
chapter-06 | fault-021 | DELETE-MODIFIER: prepositional phrase `at the road surface` stripped | `taylor-hebert-westeros drives the first group at the road surface` → `taylor-hebert-westeros drives the first group`
chapter-06 | fault-022 | DELETE-MODIFIER: prepositional phrase `across the track` stripped | `the ravens scatter across the track` → `the ravens scatter`
chapter-06 | fault-023 | DELETE-MODIFIER: prepositional destination phrase stripped | `taylor-hebert-westeros directs the first group onto the verge track` → `taylor-hebert-westeros directs the first group`
chapter-06 | fault-024 | DELETE-MODIFIER: prepositional phrase `off the road` stripped | `the courier leads the horse off the road` → `the courier leads the horse`
chapter-06 | fault-025 | DELETE-MODIFIER: prepositional location phrase `at the verge` stripped | `the courier pauses at the verge` → `the courier pauses`
chapter-06 | fault-026 | DELETE-MODIFIER: comparative adverb `lower` and prepositional phrase `along the track surface` stripped | `taylor-hebert-westeros drives the first group lower along the track surface` → `taylor-hebert-westeros drives the first group`
chapter-06 | fault-027 | DELETE-MODIFIER: adverb `back` and prepositional phrase `toward Harrenhal` stripped | `the courier turns back toward Harrenhal` → `the courier turns`
chapter-06 | fault-028 | DELETE-MODIFIER: result adverb `clear` stripped | `the ravens lift clear` → `the ravens lift`
chapter-06 | fault-029 | DELETE-MODIFIER: prepositional phrase `across the approach mouth` stripped | `taylor-hebert-westeros spreads the second group across the approach mouth` → `taylor-hebert-westeros spreads the second group`
chapter-06 | fault-030 | DELETE-MODIFIER: prepositional phrase `across the approach` stripped | `the second group fans across the approach` → `the second group fans`
chapter-06 | fault-031 | DELETE-MODIFIER: prepositional phrase `at the second courier` stripped | `taylor-hebert-westeros drives the second group at the second courier` → `taylor-hebert-westeros drives the second group`
chapter-06 | fault-032 | RENAME-ACTOR: unlisted `the gate guard` renamed to bare-noun `the guard`; no oc-* card required for generic background role | `the gate guard speaks to the second courier` → `the guard speaks to the second courier`
chapter-06 | fault-033 | DELETE-MODIFIER: prepositional phrase `to one knee` stripped | `taylor-hebert-westeros drops to one knee` → `taylor-hebert-westeros drops`
chapter-06 | fault-034 | DELETE-MODIFIER: adjective `both` and prepositional phrase `to the earth` stripped | `taylor-hebert-westeros presses both hands to the earth` → `taylor-hebert-westeros presses the hands`
chapter-06 | fault-035 | DELETE-MODIFIER: prepositional phrase `along the bell tower` stripped | `the ravens land along the bell tower` → `the ravens land`

---

## chapter-05 pass-2 repairs — 2026-05-07

chapter-05 | fault-001 | RECAST-PHYSICAL: possessive "his" stripped; prepositional destination stripped | `septon-rowan drops his travel pack against the rain-barrel` → `septon-rowan drops the travel pack`
chapter-05 | fault-002 | RECAST-PHYSICAL: prepositional directional tail stripped | `taylor-hebert-westeros crosses the yard toward septon-rowan` → `taylor-hebert-westeros crosses the yard`
chapter-05 | fault-003 | RECAST-PHYSICAL: possessive "her" → "the"; prepositional tail stripped; bare licensed hold-body-part form restored | `taylor-hebert-westeros holds her eyes on septon-rowan` → `taylor-hebert-westeros holds the eyes`
chapter-05 | fault-004 | RECAST-PHYSICAL: prepositional destination stripped | `septon-rowan sets the travel pack on the table` → `septon-rowan sets the travel pack`
chapter-05 | fault-005 | RECAST-PHYSICAL: prepositional destination stripped | `septon-rowan opens the septon's ledger on the table` → `septon-rowan opens the septon's ledger`
chapter-05 | fault-006 | RECAST-PHYSICAL: prepositional destination stripped | `septon-rowan crosses the yard to the sept door` → `septon-rowan crosses the yard`
chapter-05 | fault-007 | RECAST-PHYSICAL: objectless intransitive + prep phrase replaced with transitive motion verb taking destination as direct object | `septon-rowan advances to the chancel` → `septon-rowan enters the chancel`
chapter-05 | fault-008 | RECAST-PHYSICAL: prepositional locating phrase stripped; bare intransitive restored | `septon-rowan kneels at the altar table` → `septon-rowan kneels`
chapter-05 | fault-009 | RECAST-PHYSICAL: prepositional origin phrase stripped; bare intransitive restored | `septon-rowan rises from the altar table` → `septon-rowan rises`
chapter-05 | fault-010 | RECAST-PHYSICAL: prepositional route phrase stripped | `septon-rowan exits the sept yard through the gate` → `septon-rowan exits the sept yard`
chapter-05 | fault-011 | RECAST-PHYSICAL: directional adverb "north" stripped | `septon-rowan takes the Harrenhal road north` → `septon-rowan takes the Harrenhal road`
chapter-05 | fault-012 | RECAST-PHYSICAL: directional adverb "north" and prepositional tail stripped | `septon-rowan continues the road north toward Harrenhal` → `septon-rowan continues the road`
chapter-05 | fault-013 | RECAST-PHYSICAL: prepositional directional tail stripped; bare intransitive restored | `ser-harwick-plumm turns toward septon-rowan` → `ser-harwick-plumm turns`
chapter-05 | fault-014 | RECAST-PHYSICAL: possessive "his" stripped; prepositional origin phrase stripped | `ser-harwick-plumm draws the record book from his satchel` → `ser-harwick-plumm draws the record book`
chapter-05 | fault-015 | RECAST-PHYSICAL: prepositional destination eliminated; page becomes direct object of touch | `ser-harwick-plumm touches the nib to the page` → `ser-harwick-plumm touches the page`
chapter-05 | fault-016 | RECAST-PHYSICAL: possessive "rowan's" → "the"; prepositional destination stripped | `ser-harwick-plumm writes rowan's name into the record book` → `ser-harwick-plumm writes the name`
chapter-05 | fault-017 | RECAST-PHYSICAL: same ruling as fault-015; second occurrence (line 52) | `ser-harwick-plumm touches the nib to the page` → `ser-harwick-plumm touches the page`
chapter-05 | fault-018 | RECAST-PHYSICAL: prepositional destination stripped | `ser-harwick-plumm writes the sept entry into the record book` → `ser-harwick-plumm writes the sept entry`
chapter-05 | fault-019 | RECAST-PHYSICAL: prepositional locating phrase stripped; entry remains direct object | `ser-harwick-plumm numbers the entry in the record book` → `ser-harwick-plumm numbers the entry`
chapter-05 | fault-020 | RECAST-PHYSICAL: same ruling as fault-015; third occurrence (line 61) | `ser-harwick-plumm touches the nib to the page` → `ser-harwick-plumm touches the page`
chapter-05 | fault-021 | RECAST-PHYSICAL: possessive "taylor's" → "the"; prepositional destination stripped | `ser-harwick-plumm writes taylor's name into the record book` → `ser-harwick-plumm writes the name`
chapter-05 | fault-022 | RECAST-PHYSICAL: possessive "his" stripped; prepositional destination replaced by transitive containment verb | `ser-harwick-plumm returns the record book to his satchel` → `ser-harwick-plumm pockets the record book`
chapter-05 | fault-023 | RECAST-PHYSICAL: turn+prepositional-path replaced with transitive motion verb taking gate as direct object | `ser-harwick-plumm turns through the postern gate` → `ser-harwick-plumm passes the postern gate`
chapter-05 | fault-024 | RECAST-PHYSICAL: directional adverb "south" and prepositional locating phrase stripped; bare intransitive restored | `septon-rowan turns south on the Harrenhal road` → `septon-rowan turns`
chapter-05 | fault-025 | RECAST-PHYSICAL: prepositional origin phrase stripped; bare intransitive restored | `taylor-hebert-westeros rises from the garden wall` → `taylor-hebert-westeros rises`
chapter-05 | fault-026 | RECAST-PHYSICAL: possessive "his" → "the"; prepositional tail stripped; bare licensed hold-body-part form restored | `septon-rowan holds his eyes on taylor-hebert-westeros` → `septon-rowan holds the eyes`
chapter-05 | fault-027 | RECAST-PHYSICAL: stative "stands at" replaced with arrival motion verb taking postern as direct object | `ser-harwick-plumm stands at the gatehouse postern` → `ser-harwick-plumm reaches the gatehouse postern`
chapter-05 | fault-028 | RECAST-PHYSICAL: abstract-object hold + positional stative collapsed to bare concrete intransitive | `septon-rowan holds his position at the gatehouse wall` → `septon-rowan stops`
chapter-05 | fault-029 | RECAST-PHYSICAL: abstract compound noun "chin angle" stripped to licensed bare body-part form | `taylor-hebert-westeros holds the chin angle` → `taylor-hebert-westeros holds the chin`
chapter-05 | fault-030 | RECAST-PHYSICAL: perception subordinate clause stripped; spine retains only physical cresting act; perceptual consequence (castle walls visible) routed to narrator-interest facet citing line 27 | `septon-rowan crests the rise where the castle walls come into view` → `septon-rowan crests the rise`

---

## chapter-01 pass-3 structural revisions — 2026-05-07

### INERT-STRETCH fix (IDs 18–29)

chapter-01 | pass3-struct-001 | BLANK-INERT-STRETCH: 12-beat woman-delivers-broth sequence (IDs 18–29) removed; all IDs blanked (preserved as gap markers per schema); zero downstream propagation confirmed by pass-3 audit
chapter-01 | pass3-struct-002 | NEW-BEAT (ID 132): single load-bearing replacement for woman's visit — `the woman speaks to taylor-hebert-westeros` — dialogue facet will carry the signaling content (septon incapacity / strangers on road); placed at bottom of file per schema append rule; intended narrative position: between ID 15 and ID 30

### DOUBLE-PEAK fix (IDs 84–93)

chapter-01 | pass3-struct-003 | BLANK-ATTESTATION-BLOCK: IDs 84–93 blanked (10 procedural beats compressed); peak at ID 68 (naming notation) preserved as chapter high-water mark; falling-action completion replaced by 4-beat sequence appended at bottom
chapter-01 | pass3-struct-004 | NEW-BEAT (ID 133): `census-officer speaks to septon-dying-protector` — instruction to attest; falling action; replaces ID 85
chapter-01 | pass3-struct-005 | NEW-BEAT (ID 134): `septon-dying-protector marks the scroll` — attestation act; falling action; replaces IDs 86–87
chapter-01 | pass3-struct-006 | NEW-BEAT (ID 135): `census-officer retrieves the quill` — procedural completion; falling action; replaces IDs 88–90
chapter-01 | pass3-struct-007 | NEW-BEAT (ID 136): `census-officer rolls the scroll` — bureaucratic finalization; falling action; replaces IDs 91–93; second census-officer notation (ID 84) and officer-speaks-to-septon repeat (ID 91) dropped as redundant weight

### Missing transition additions

chapter-01 | pass3-struct-008 | NEW-BEAT (ID 137): spatial bridge between IDs 15 and 132 (formerly 15 and 18) — `the woman crosses the yard` — establishes woman approaching cottage door (not sept door) before her speak beat; resolves spatial ambiguity flagged in pass-3 audit
chapter-01 | pass3-struct-009 | NEW-BEAT (ID 138): decision beat between IDs 35 and 37 — `taylor-hebert-westeros faces the cottage door` — physical re-orientation registering Taylor's read of the riders; recast as transitive directional form per `turns to X` ban; resolves missing-transition flag
chapter-01 | pass3-struct-010 | NEW-BEAT (ID 139): exit beat between IDs 42 and 44 — `taylor-hebert-westeros exits the cottage` — explicit interior-to-exterior transition; resolves causal-jump flag at existing time-skip ID 43
chapter-01 | pass3-struct-011 | NEW-BEAT (ID 140): gate-entry beat between IDs 53 and 55 — `census-officer pushes the gate` — covers yard passage; resolves unanchored entry at ID 55 flagged in pass-3 audit

### Summary

New IDs appended: 132–140 (9 beats). IDs blanked as gap markers: 18–29 (12 gaps), 84–93 (10 gaps, ID 89 already blank from pass-2). Net file beat count change: −22 beats deleted, +9 beats added = −13 net. Climax at ID 68 is now uncontested chapter peak. Four structural gaps resolved.

---

## chapter-05 pass-3 structural repairs — 2026-05-07

Trigger: STRUCTURAL-FAILURE verdict from Pass 3 shape audit (`active-project/staff/auditor/ch05-pass3-shape.md`).
Narrator: septon-rowan. Chapter formally classified as interlude.

**Plan update:**
`design/shoot-v2/season-chapters-run/chapter-05-plan.md`: field `interlude: true` added between `narrator:` and `constraints:`.

**Proto-line file header update:**
`active-project/theater/proto-lines/chapter-05.md`: comment line added after goal header — `# interlude: true — septon-rowan is not the series protagonist; this chapter is narrator-POV of a secondary actor`.

**FLATLINE-IN-BUILDUP fix A — IDs 17–23 (cottage-to-chancel movement):**
IDs 17, 18, 19, 22, 23 blanked (preserved as gap markers). IDs 20 (`septon-rowan enters the chancel`) and 21 (`septon-rowan kneels`) retained as the compressed 2-beat prayer block. Net: −5 beats removed from buildup.

**FLATLINE-IN-BUILDUP fix B — IDs 25–28 (yard-exit to road transit):**
IDs 25, 27, 28 blanked. ID 26 (`septon-rowan takes the Harrenhal road`) retained as single transition beat. Net: −3 beats removed from buildup.

**FLATLINE-AT-PEAK fix — IDs 63–66 (post-peak administrative deflation):**
IDs 63, 64, 65 blanked (lifts stylus / caps stylus / closes record book). ID 66 (`ser-harwick-plumm pockets the record book`) retained as the single departure beat that closes the climax block. Structural peak at ID 62 is now uncontested. Net: −3 beats removed.

**New beat 88 — irreversibility marker (after ID 62, before ID 66 departure):**
`88 septon-rowan drops the eyes` — physically placed after ID 62, before blanked IDs 63–65. Rowan's gaze drops to the written name; marks registration of completion from narrator POV. Physical body-part act, no interiority, septon-rowan POV. ID 88 is next available monotonic integer at time of insertion.

**New beats 85–86 — causal transition (between IDs 15 and 16):**
`85 septon-rowan touches the ledger` — physically placed after ID 15 (closes ledger), before time-skip ID 16. Rowan's hand returns to the closed ledger; marks specific recognition of the entry (Taylor's name) that triggers the decision to ride. Physical, septon-rowan POV, no perception verb.
`86 septon-rowan takes the travel pack` — placed after ID 85. Observable act of picking up the pack; externalizes decision to ride. Physical, septon-rowan POV.
Both placed before time-skip ID 16 in the file body.

**New beat 87 — comprehension marker (between IDs 70 and 71):**
`87 septon-rowan lowers the eyes` — physically placed after ID 70 (gate shut), before time-skip ID 71. Registers Rowan's comprehension that the record is permanent and now contains two names. Physical body-part act, septon-rowan POV, no interiority.

**Constraint checks:**
- No `turns to <X>` constructions introduced. ID 73 (`septon-rowan turns`) is bare intransitive — valid per schema.
- All new beats are septon-rowan POV — only what he can physically do or directly observe.
- No motivation clauses, no copulas, no perception verbs, no modifiers in any new line.
- Surviving IDs unchanged throughout. New IDs 85, 86, 87, 88 are monotonically appended (next available after existing max ID 84).

**Expected structural result:**
Singular peak at ID 62 (`ser-harwick-plumm writes the name`). Buildup flatlines eliminated. Causal bridge (15 → 85 → 86 → 16) in place. Post-peak deflation collapsed to single departure beat (66 → 67). Comprehension beat (70 → 87 → 71 → 72) in place. Net: −11 beats removed, +4 beats added = −7 net.

---

## season-S1-constraint-audit repairs — 2026-05-07

### Scope
52 faults across 13 files (chapter-10 zero-fault; not touched). Fault classes: FAULT-FORM-MODIFIER (28), FAULT-FORM-ID-SEQUENCE (9), FAULT-FORM-INTERIORITY (3), FAULT-FORM-NON-ACTION-VERB (4), FAULT-FORM-PERCEPTION (2), FAULT-CONSTRAINT-slug (3), FAULT-FORM-MULTI-SUBJECT (1), FAULT-FORM-NO-VERB (1), FAULT-FORM-MALFORMED-BEAT (1).

### chapter-01.md

fault-001 | RECAST: `steps into the yard` → `enters the yard` (line 7) — prepositional destination phrase stripped; transitive verb takes destination as direct object
fault-002 | RECAST: `turns toward the sept door` → `faces the sept door` (line 10) — banned turns-toward directional-prep; transitive recast per schema ruling
fault-003 | RECAST: `steps into the yard` → `enters the yard` (line 32) — same as fault-001 (second occurrence)
fault-004 | RECAST: `turns toward taylor-hebert-westeros` → `faces taylor-hebert-westeros` (line 51) — turns-toward banned; faces is schema-recommended recast
fault-005 | RECAST: `turns toward the outbuildings` → `faces the outbuildings` (line 57) — same class as fault-004
fault-006 | RECAST: `turns toward taylor-hebert-westeros` → `faces taylor-hebert-westeros` (line 76) — third occurrence of turns-toward in chapter-01
fault-007 | RECAST: `crosses to the window` → `reaches the window` (line 119) — prepositional destination phrase; `reaches` takes destination as direct object
fault-008 (slug) | RENAME: `census-officer` → `oc-census-officer` globally throughout chapter-01.md — card oc-census-officer.card.md confirmed in active-project/warehouse/; replace_all applied

### chapter-02.md

fault-009 | RECAST: `taylor-hebert-westeros crouches the kitchen garden` → `taylor-hebert-westeros enters the kitchen garden` (line 4) — false transitive; line 11 entry pattern applied; crouching posture routes to state-update facet citing this line
fault-010 | RECAST: `plumms-man crouches the shed floor` → `oc-plumms-man crouches` (line 12) — false transitive stripped to bare intransitive; entry beat at line 11 already establishes location
fault-011 (slug) | CONFIRMED: `oc-girl-from-hamlet` slug verified correct — card oc-girl-from-hamlet.card.md confirmed in active-project/warehouse/; no rename needed; slug already `oc-` prefixed
fault-012 | RECAST: `a sparrow lifts the barn eave` → `a sparrow lifts` (line 24) — departure verb used intransitively; eave context routes to loc-state facet
fault-013 | RECAST: `leans the cottage wall` → `presses the cottage wall` (line 81) — contact verb replaces suppressed-preposition form; physical surface is direct object
fault-014 | RECAST: `taylor-hebert-westeros opens the passive feed` → `taylor-hebert-westeros stills` (line 96) — interiority stripped; physical observable correlate only; fauna-state routes to state-update facet
fault-015 | BLANK: `taylor-hebert-westeros drops the passive feed` → ID 100 blanked (time-skip marker) — interiority stripped; fauna dispersal lines 97-99 provide observable physical consequence; blank marks elapsed time
fault-016 (ID-seq) | REORDER: chapter-02.md re-emitted with all IDs in monotonic file-body order — IDs 66-68 moved before 69-72; IDs 91, 94 ordered before 104 in garrison section; IDs 102, 103 moved to after 101 at file end; all content preserved; narrative sequence handled via facet citation order
fault-017 (slug) | RENAME: `plumms-man` → `oc-plumms-man` globally throughout chapter-02.md — card oc-plumms-man.card.md confirmed in active-project/warehouse/; replace_all applied

### chapter-03.md

fault-018 | STRIP: `holds the feet flat` → `holds the feet` (line 8) — result-state modifier `flat` stripped; licensed body-part hold preserved
fault-019 | STRIP: `holds the chin level` → `holds the chin` (line 9) — modifier `level` stripped
fault-020 | STRIP: `holds the hands flat` → `holds the hands` (line 14) — modifier `flat` stripped
fault-021 | STRIP: `holds the chin level` → `holds the chin` (line 18) — second occurrence; same ruling as fault-019
fault-022 | STRIP: `holds the eyes open` → `holds the eyes` (line 19) — modifier `open` stripped
fault-023 | STRIP: `holds the feet flat` → `holds the feet` (line 35) — third occurrence; same ruling as fault-018
fault-024 | STRIP: `holds the hands still` → `holds the hands` (line 39) — modifier `still` stripped
fault-025 | STRIP: `holds the feet flat` → `holds the feet` (line 42) — fourth occurrence; same ruling as fault-018

### chapter-03-interlude.md

fault-026 (misattributed by auditor) | NOTE: audit attributes `septon-rowan scans the cottage interior` to chapter-03-interlude.md line 12; actual chapter-03-interlude.md has narrator: ser-harwick-plumm (records hall) with line 12 = `ser-harwick-plumm faces the records hall`; the septon-rowan scans content lives in chapter-05.md; fix applied to chapter-05.md (see fault-030 below)
fault-026 (slug) | RENAME: `plumms-man` → `oc-plumms-man` globally throughout chapter-03-interlude.md — card confirmed; replace_all applied
fault-027 (ID-seq) | VERIFY: chapter-03-interlude.md has IDs 1-31 with gaps; all monotonically increasing in file body; no IDs 87-88 present in this file; audit's ID-sequence fault for chapter-03-interlude may refer to chapter-05.md; chapter-03-interlude.md passes ID-sequence check

### chapter-04.md

fault-028 | RECAST: `drops the gaze` → `lowers the eyes` (line 51) — abstract noun `gaze` replaced with concrete body part; matches established form from chapter-01 line 79
fault-029 (ID-seq) | REORDER: ID 99 removed from between IDs 26 and 27; appended after ID 98 at file end — monotonic body order restored; content `taylor-hebert-westeros reaches the well` preserved at new physical position

### chapter-05.md (septon-rowan interlude; misidentified as chapter-03-interlude by auditor)

fault-030 | RECAST: `septon-rowan scans the cottage interior` → `septon-rowan crosses the cottage` (line 12) — perception verb replaced with physical motion beat; interior-observation content routes to narrator-interest / sensory facets
fault-031 (ID-seq) | REORDER: chapter-05.md re-emitted with all IDs in monotonic file-body order — IDs 85, 86, 87, 88 moved from mid-file positions (after 15, before 16; after 62; after 70) to after ID 84 at file end; all content preserved; narrative positions handled via facet citation order

### chapter-06.md

fault-032 | RECAST: `the courier holds the horse` → `the courier grips the reins` (line 76) — unlicensed holds-verb replaced with discrete physical grip action; reins as direct object
fault-033 | RECAST: `crosses to the door` → `reaches the door` (line 107) — prepositional destination phrase; `reaches` takes destination as direct object

### chapter-07.md

fault-034 | RECAST: `leans against the counter` → `presses the counter` (line 4) — prepositional position phrase stripped; contact verb takes surface as direct object
fault-035 | RECAST: `turns the pages of Plumm's filing` → `turns the filing` (line 21) — prepositional qualifier `of Plumm's filing` stripped; filing used as direct object; document identity established by context
fault-036 | RECAST: `turns the document over` → `flips the document` (line 63) — adverb particle `over` encodes direction; `flips` carries the direction without adverb
fault-037 (ID-seq) | REORDER: chapter-07.md re-emitted — IDs 93 and 94 moved from mid-file positions (93 between 16 and 17; 94 between 28 and 29) to after ID 92 at file end; IDs 86-92 verified already monotonic; all content preserved

### chapter-08.md

fault-038 | STRIP: `pins the hands to the knees` → `pins the hands` (line 19) — prepositional destination phrase stripped; loc-state facet provides surface
fault-039 | STRIP: `pins the palms to the table` → `pins the palms` (line 95) — same as fault-038; prepositional destination stripped

### chapter-08-interlude.md

fault-040 | RECAST: `a courier passes the letter-case to the gatehouse man` → `a courier hands the gatehouse man the letter-case` (line 37) — prepositional recipient phrase replaced with double-object construction; no preposition; same physical event
fault-041 | RECAST: `oc-castellan-harrenhal speaks the letter` → `oc-castellan-harrenhal speaks to the hall` (line 49) — malformed beat; `speaks` with document object is neither dialogue form nor clean physical action; recast to licensed dialogue-beat form; letter content routes to dialogue facet citing this line; preparation beats at lines 47-48 already present
fault-042 | RECAST: `those present file out of the hall` → `the hall empties` (line 56) — multi-subject construction; recast as licensed ambient-action with object-as-subject form

### chapter-09.md

fault-043 | RECAST: `stations a raven on the outer wall` → `dispatches the raven` (line 1) — stative placement verb + prepositional phrase replaced with discrete dispatch action; loc-state handles position
fault-044 | RECAST: `stations a sparrow on the gate lintel` → `dispatches the sparrow` (line 2) — same as fault-043
fault-045 | RECAST: `stations a fly on the gatehouse wall` → `dispatches a fly` (line 78) — same as fault-043; indefinite article retained (first mention of fly in this chapter)
fault-046 | RECAST: `ser-edwyn-celtigar rides` → `ser-edwyn-celtigar enters the approach road` (line 67) — bare intransitive motion verb without destination; transitive motion verb with destination as direct object; cart relationship preserved (adjacent IDs 66 and 68)
fault-047 (ID-seq) | REORDER: chapter-09.md re-emitted — IDs 62-65 moved from after ID 90 to after ID 61; ID 99 moved from between IDs 61 and 66 to after ID 98 at file end; all content preserved; monotonic file-body order restored

### Summary

52 faults addressed. 0 escalated. 0 dependency-flagged.
Slug renames applied: census-officer → oc-census-officer (ch-01), plumms-man → oc-plumms-man (ch-02, ch-03-interlude).
ID-sequence fixes applied: ch-02, ch-03-interlude (verified clean), ch-04, ch-05, ch-07, ch-09.
Holds modifiers stripped: 8 instances in ch-03.
Stations verbs recasted: 3 instances in ch-09.
Turns-toward recasted: 4 instances in ch-01.
Perception verbs recasted: 1 in ch-05 (applies to both fault-026 and fault-030; auditor mislabeled fault-026 as ch-03-interlude).
Interiority removed: ch-02 lines 96, 100; ch-04 line 51.
Prepositional destination phrases recasted: ch-01 line 119, ch-06 line 107, ch-07 lines 4/21.
Non-action verbs recasted: ch-06 line 76, ch-09 lines 1/2/78.
Malformed beat recasted: ch-08-interlude line 49.
Multi-subject recasted: ch-08-interlude line 56.
No-verb recasted: ch-09 line 67.
