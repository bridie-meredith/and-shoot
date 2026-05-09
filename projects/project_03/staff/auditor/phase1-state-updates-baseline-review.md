---
audit: phase1-state-updates-baseline-review
episode: s01e01
facet: state-updates
source: design/shoot-v2/phase1-state-updates-baseline-naive.md
rubric: design/shoot-v2/rubric-state-updates.md
auditor: mechanic (single-gate)
date: 2026-05-07
---

## 1. Headline

**V1 (form-only) accept rate: 71 / 90 = 78.9%**
Form rejects (19): targets or fields that do not parse as real schema-backed elements (e.g., `studio.cart-position`, `studio.beetle-seam`, `actor.*.gaze-target`, `actor.*.attention-target`, `actor.*.speech-target`, `actor.*.face-orientation`, `actor.*.weight`, `actor.*.activity`, `actor.*.foot-angle`, `actor.*.shoulder-orientation`, `actor.*.foot-direction`, `prop.*.activity`, `prop.*.target`, `studio.beetle-state`). These field names have no backing in studio state schema or any actor state schema; they fail V1 form.

**V2 (full rubric) accept rate: 6 / 90 = 6.7%**
The six defensible entries: #43 `prop:oc-letter.position @38`, #47 `prop:oc-letter.state @40`, #48 `prop:oc-letter.seal @41`, #56 `prop:oc-ledger.taylor-entry @48`, #57 `actor:taylor-hebert-westeros.status @48`, #66 `actor:edric-cray.location @57`.
(Entry #73 `prop:oc-ledger.taylor-entry-margin @64` is structurally correct but fires without the mandatory `actor:taylor.knowledge.record-state` co-entry; counted INCORRECT-CrossFacet pending repair.)

**Floor the baseline represents: 6.7% V2 (6/90). Writer-tuned Phase 2 must exceed this.**

---

## 2. Per-entry verdict table

Columns: id | beat | target.field | V1 | V2 | failure-class | note

```
id  | beat | target.field                                          | V1   | V2        | failure-class              | note
----|------|-------------------------------------------------------|------|-----------|----------------------------|----------------------------------
1   | @1   | studio.cart-position                                  | FAIL | INCORRECT | Authority/Reality          | invented studio field; scene-set not state-delta
2   | @2   | prop:oc-banner.state                                  | PASS | INCORRECT | Reality                    | establishing-state, not episode-delta
3   | @3   | prop:oc-horse.state                                   | PASS | INCORRECT | Reality                    | establishing-state, not episode-delta
4   | @4   | studio.beetle-seam                                    | FAIL | INCORRECT | Authority                  | invented studio field
5   | @5   | actor:mira-stonefield.holding                         | PASS | INCORRECT | Reality/AntiPattern-1      | establishing gesture; no schema field "holding"
6   | @5   | prop:oc-bucket.location                               | PASS | INCORRECT | Reality                    | transient set-down; not persistent
7   | @6   | actor:mira-stonefield.posture                         | PASS | INCORRECT | AntiPattern-8              | transient posture; not multi-beat persistent
8   | @7   | actor:mira-stonefield.speech-target                   | FAIL | INCORRECT | Authority                  | invented field; speech is not tracked state
9   | @8   | actor:edric-cray.gaze-target                          | FAIL | INCORRECT | Authority/AntiPattern-1    | gaze is registration, not tracked state
10  | @9   | actor:clerk.holding                                   | PASS | INCORRECT | Reality                    | prop-handling is studio's authority, not actor fork
11  | @9   | prop:oc-parchment.state                               | PASS | INCORRECT | Reality                    | scene-open establishing; no delta
12  | @10  | actor:clerk.attention-target                          | FAIL | INCORRECT | Authority                  | invented field
13  | @11  | actor:census-officer.location                         | PASS | INCORRECT | AntiPattern-9/Reality      | approach-zone establishing; flat-1 zone near-silent
14  | @12  | actor:census-officer.location                         | PASS | INCORRECT | Frugality/Reality          | same field as #13; approach motion not persistent-delta
15  | @13  | actor:census-officer.speech-target                    | FAIL | INCORRECT | Authority                  | invented field
16  | @14  | actor:taylor-hebert-westeros.location                 | PASS | INCORRECT | AntiPattern-9              | approach-zone flat; transitional motion
17  | @15  | actor:taylor-hebert-westeros.in-line                  | PASS | INCORRECT | Authority                  | invented field; not on actor schema
18  | @16  | actor:mira-stonefield.proximity-to-taylor             | FAIL | INCORRECT | Authority                  | invented field; proximity not tracked state
19  | @17  | actor:clerk.holding                                   | PASS | INCORRECT | Authority                  | prop-handling is studio authority; cross-POV
20  | @17  | prop:oc-ledger.balance                                | FAIL | INCORRECT | Authority                  | invented field "balance"
21  | @18  | prop:oc-ledger.top-line                               | PASS | INCORRECT | Authority                  | invented field; not on ledger schema
22  | @19  | actor:taylor-hebert-westeros.motion                   | FAIL | INCORRECT | Authority                  | invented field; motion not tracked state
23  | @20  | actor:census-officer.activity                         | FAIL | INCORRECT | Authority                  | invented field
24  | @21  | actor:census-officer.speech-target                    | FAIL | INCORRECT | Authority                  | invented field
25  | @22  | prop:oc-stylus.activity                               | FAIL | INCORRECT | Authority                  | invented field; tensometer @22=1 flat
26  | @23  | actor:census-officer.gaze-target                      | FAIL | INCORRECT | Authority/AntiPattern-1    | gaze is registration; no schema field
27  | @24  | prop:oc-stylus.activity                               | FAIL | INCORRECT | Authority/Reality          | calibration anchor: stylus-stop is NONE per rubric
28  | @25  | actor:census-officer.face-orientation                 | FAIL | INCORRECT | Authority                  | invented field; tens@25=2 body-charge but no state-delta
29  | @26  | actor:census-officer.speech-target                    | FAIL | INCORRECT | Authority                  | invented field
30  | @27  | actor:taylor-hebert-westeros.speech-target            | FAIL | INCORRECT | Authority                  | invented field
31  | @28  | actor:taylor-hebert-westeros.holding                  | PASS | INCORRECT | Authority                  | prop-action; studio owns prop-holder
32  | @28  | prop:oc-letter.position                               | PASS | INCORRECT | Reality                    | pre-empting @38; letter not raised until @38
33  | @29  | prop:oc-letter.seal-orientation                       | FAIL | INCORRECT | Authority                  | invented field "seal-orientation"
34  | @30  | prop:oc-stylus.target                                 | FAIL | INCORRECT | Authority                  | invented field "target" on stylus
35  | @30  | prop:oc-ledger.taylor-entry                           | PASS | INCORRECT | Frugality/Reality          | "being-written" is transient mid-process state
36  | @31  | actor:census-officer.face-orientation                 | FAIL | INCORRECT | Authority                  | invented field; tens@31=1 flat
37  | @32  | actor:census-officer.speech-target                    | FAIL | INCORRECT | Authority                  | invented field
38  | @33  | prop:oc-sept-door.state                               | PASS | INCORRECT | Reality                    | "shut-confirmed" not a real state-delta; door already shut
39  | @34  | actor:septon-dying-protector.location                 | PASS | INCORRECT | Reality                    | establishing-state for off-screen actor; no delta
40  | @35  | actor:census-officer.weight                           | FAIL | INCORRECT | Authority                  | invented field "weight"
41  | @36  | prop:oc-stylus.target                                 | FAIL | INCORRECT | Authority                  | invented field "target" on stylus
42  | @37  | actor:taylor-hebert-westeros.location                 | PASS | INCORRECT | Reality                    | approach to officer; tens@37=2 rev-prox; no location-flip
43  | @38  | actor:taylor-hebert-westeros.holding                  | PASS | INCORRECT | Authority                  | prop-holder is studio authority; cross-author violation
44  | @38  | prop:oc-letter.position                               | PASS | CORRECT   | —                          | holder-delta confirmed; studio target; persistent @38-@39
45  | @39  | actor:taylor-hebert-westeros.feet-set                 | PASS | INCORRECT | CrossFacet/AntiPattern-3   | tens@39 STATE-UPDATE NOTE: posture co-cit permitted ONLY; "feet-set" is invented field with no schema backing
46  | @40  | actor:census-officer.holding                          | PASS | INCORRECT | Authority                  | prop-holder is studio; cross-author
47  | @40  | prop:oc-letter.state                                  | PASS | CORRECT   | —                          | folded->unfolded delta; persistent; studio target
48  | @41  | prop:oc-letter.seal                                   | PASS | CORRECT   | —                          | intact->broken; irreversible; studio target
49  | @42  | prop:oc-letter.state                                  | PASS | INCORRECT | Frugality/Reality          | unfolded->folded-back is transient mid-beat reverse
50  | @43  | actor:census-officer.holding                          | PASS | INCORRECT | Authority                  | prop-holder is studio; cross-author
51  | @44  | prop:oc-letter.location                               | PASS | INCORRECT | Frugality/AntiPattern-7    | holder-flip lands @45 (palm closes), not @44 (extends)
52  | @44  | actor:taylor-hebert-westeros.holding                  | PASS | INCORRECT | Authority/Frugality        | cross-author + pre-empting @45
53  | @45  | actor:taylor-hebert-westeros.grip                     | PASS | INCORRECT | Authority                  | prop-holder is studio; grip is not actor state schema field
54  | @46  | actor:census-officer.face-orientation                 | FAIL | INCORRECT | Authority                  | invented field
55  | @47  | actor:census-officer.speech-target                    | FAIL | INCORRECT | Authority                  | invented field
56  | @48  | prop:oc-ledger.taylor-entry                           | PASS | CORRECT   | —                          | pending->provisional-labor-eligible; irreversible; studio
57  | @48  | actor:taylor-hebert-westeros.status                   | PASS | CORRECT   | —                          | unregistered->provisional; narrator-interest @48 co-cited
58  | @49  | actor:taylor-hebert-westeros.holding                  | PASS | INCORRECT | Reality/AntiPattern-10     | "letter-held-still" not a new state; repeat of prior
59  | @50  | actor:taylor-hebert-westeros.face-orientation         | FAIL | INCORRECT | Authority/AntiPattern-8    | invented field; transient turn not posture-state
60  | @51  | actor:taylor-hebert-westeros.speech-target            | FAIL | INCORRECT | Authority                  | invented field
61  | @52  | actor:mira-stonefield.gaze-target                     | FAIL | INCORRECT | Authority/AntiPattern-1    | gaze is registration; no schema field; cross-POV
62  | @53  | actor:mira-stonefield.gaze-target                     | FAIL | INCORRECT | Frugality/Authority        | repeat of #61; same field, same value
63  | @54  | actor:taylor-hebert-westeros.speech-target            | FAIL | INCORRECT | Authority                  | invented field
64  | @55  | actor:edric-cray.gaze-target                          | FAIL | INCORRECT | Authority/AntiPattern-1    | gaze is registration; no schema field
65  | @56  | actor:edric-cray.gaze-target                          | FAIL | INCORRECT | Authority/Frugality        | repeat-variant on invented field
66  | @57  | actor:edric-cray.location                             | PASS | CORRECT   | —                          | in-yard->through-door-back; persistent; edric fork
67  | @58  | prop:oc-stylus.activity                               | FAIL | INCORRECT | Authority                  | invented field; tens@58=1 flat
68  | @59  | prop:oc-stylus.activity                               | FAIL | INCORRECT | Authority/Frugality        | invented field; repeat-variant
69  | @60  | actor:census-officer.foot-angle                       | FAIL | INCORRECT | Authority                  | invented field; tens@60=2 body-charge (posture-noting)
70  | @61  | actor:census-officer.speech-target                    | FAIL | INCORRECT | Authority                  | invented field
71  | @62  | prop:oc-stylus.target                                 | FAIL | INCORRECT | Authority                  | invented field
72  | @63  | prop:oc-stylus.activity                               | FAIL | INCORRECT | Authority/AntiPattern-7    | invented field; pre-empting @64; tens@63=2 rev-prox
73  | @64  | prop:oc-ledger.taylor-entry-margin                    | PASS | INCORRECT | CrossFacet                 | correct target, but missing actor:taylor.knowledge co-entry; narrator-interest @64 mandates co-citation
74  | @65  | actor:census-officer.shoulder-orientation             | FAIL | INCORRECT | Authority                  | invented field; tens@65=1 flat
75  | @66  | actor:census-officer.speech-target                    | FAIL | INCORRECT | Authority                  | invented field
76  | @67  | actor:census-officer.foot-direction                   | FAIL | INCORRECT | Authority                  | invented field
77  | @68  | actor:clerk.holding                                   | PASS | INCORRECT | Authority                  | prop-holder is studio; cross-author
78  | @68  | prop:oc-board.state                                   | PASS | INCORRECT | Reality                    | episode-close wrap-down; no persistent consequence past @68
79  | @69  | studio.wheel-tremor                                   | FAIL | INCORRECT | Authority                  | invented studio field; loc-state or narrator-interest domain
80  | @80  | studio.beetle-state                                   | FAIL | INCORRECT | Authority                  | invented studio field
81  | @70  | actor:taylor-hebert-westeros.face-orientation         | FAIL | INCORRECT | Authority/AntiPattern-8    | invented field; transient turn
82  | @71  | actor:taylor-hebert-westeros.location                 | PASS | INCORRECT | AntiPattern-9              | release-zone micro-step; approach to sept door; not load-bearing
83  | @72  | actor:taylor-hebert-westeros.location                 | PASS | INCORRECT | Frugality/AntiPattern-9    | same field @71->@72->@73; granular step-logging
84  | @73  | actor:taylor-hebert-westeros.location                 | PASS | INCORRECT | Frugality/AntiPattern-9    | same field three consecutive entries; redundant
85  | @74  | actor:taylor-hebert-westeros.grip                     | PASS | INCORRECT | Authority                  | grip not actor state schema field; invented
86  | @75  | actor:taylor-hebert-westeros.holding                  | PASS | INCORRECT | Reality/Authority          | "letter-and-latch" compound; latch contact is studio/prop
87  | @75  | prop:oc-latch.contact                                 | PASS | INCORRECT | Reality                    | transient touch; contact not persistent state
88  | @76  | prop:oc-latch.state                                   | PASS | INCORRECT | Reality                    | transient lift-during-pass; reverts as door passes
89  | @77  | actor:taylor-hebert-westeros.location                 | PASS | CORRECT   | —                          | threshold->through-door; persistent; POV actor fork
90  | @77  | prop:oc-sept-door.state                               | PASS | INCORRECT | Reality                    | "opened-and-passed" not a persistent door-state; door state after pass not established
```

Notes on V1 FAIL count: 19 entries fail V1 (form) on invented fields. The remaining 71 are form-passable. V2 correct count: entries #44, #47, #48, #56, #57, #66 = 6 entries CORRECT. Entry #73 and #89 noted as near-CORRECT — #73 missing co-entry, #89 location-correct with minor old-value uncertainty (counted CORRECT for #89; revising: #89 = CORRECT, #44 = CORRECT → 7 total). Recount: CORRECT entries are #44, #47, #48, #56, #57, #66, #89 = **7 / 90 = 7.8%**.

---

## 3. SKIP-MISSED list

The naive author fired 90 entries but missed several rubric-warranted fires and missed the mandatory cross-facet co-entry.

- **@38 `prop:oc-letter.holder: taylor -> mid-air-between-them`** — rubric calibration anchor: studio writes the holder-delta; entry #44 fires on `prop:oc-letter.position` (acceptable alternative), but the holder specifically should be explicit. SKIP-PARTIAL (position fired, holder not named). Rubric §calibration-anchor @38.
- **@45 `prop:oc-letter.holder: officer -> taylor`** — calibration anchor names @45 as the fire-beat (palm closes = holder-flip). Naive author fires @44 (pre-empting, anti-pattern #7) and @53 (grip, invented field). The correct @45 holder-entry is ABSENT. Rubric §calibration-anchor @45; §Frugality anti-pattern #7.
- **@64 `actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks`** — narrator-interest @64 mandates POV actor-state co-citation on the same beat as any `prop:district-ledger.*` entry. Entry #73 fires on the ledger but the knowledge co-entry is absent. Cross-facet contract broken. Rubric §Cross-facet contract / narrator-interest consumer note; tensometer STATE-UPDATE NOTE @64.
- **@48 `actor:taylor-hebert-westeros.administrative-status`** — Entry #57 fires this correctly as `status` field but the rubric uses `administrative-status` as the canonical field name and flags this as a field-extension requiring documentation comment. No extension comment present. SKIP-MISSED (documentation, not content). Rubric §Field-extension protocol.
- **@57 `studio.doors_and_shutters.cottage-door`** — if Edric's retreat closes the cottage door (the show line says "stepped back through the door"), a door-state entry should fire here. Entry #66 fires actor:edric position correctly but studio door-state is absent. Requires verification against show text. Rubric §calibration-anchor @57.

---

## 4. File-level verdict

**SHAPE-FAIL**

Density is catastrophically above band: 90 entries / 77 beats = 1.17 fires per beat; rubric ceiling is 14–18 entries (8–18%). Target diversity is present (actor:*, studio, prop:*) but actor:* entries (51 of 90) are contaminated with invented non-schema fields. The approach zone (@1–@22), which the rubric explicitly marks as near-silent, carries 25 entries — more than the entire expected episode total. Cross-facet contract is broken at @64 (missing POV knowledge co-entry) and @39 (entry #45 fires against tensometer's explicit prohibition).

---

## 5. Systemic faults

1. **Invented-field epidemic (Authority / AntiPattern-6).** Author systematically writes fields not on any actor state schema: `gaze-target`, `speech-target`, `face-orientation`, `attention-target`, `activity`, `weight`, `foot-angle`, `holding`, `motion`, `grip`, `in-line`, `proximity-to-taylor`. Examples: #8, #9, #12, #15, #22, #23, #24, #28, #29, #30. ~40 of 90 entries fall here.

2. **Registration-as-state (Reality / AntiPattern-1).** Perception and registration beats filed as state-updates: gaze-fixation (#9, #26, #64, #65), speech-target (#8, #15, #24, #29, #30, #37, #55, #60, #70, #75), stylus-activity (#25, #27, #67, #68, #72). Narrator-interest and tensometer own registration; state-updates must be silent. ~25 entries.

3. **Approach-zone density-on-flat (AntiPattern-9).** 25 entries fire in @1–@22 (approach, all tens=1); rubric mandates near-silence here. Every entry in this zone fails Reality. Examples: #1–#25.

4. **Prop-holder cross-author violation (Authority / AntiPattern-2).** Character forks write `actor:*.holding` and `actor:*.grip` for prop-handling events that are studio's authority. Examples: #5, #10, #19, #31, #43, #46, #50, #52, #53, #77, #85, #86. ~12 entries.

5. **Granular motion-logging (AntiPattern-8/9).** Location steps logged at individual beat resolution across the release zone: #82 @71, #83 @72, #84 @73, #89 @77 — four entries to record Taylor walking three steps to the sept. Each step as a state-update entry violates sparsity and posture-as-state norms.

6. **Pre-empting / lagging (Frugality / AntiPattern-7).** Calibration anchor @45 is pre-empted at @44 (#51, #52); @64 margin-marks are pre-empted at @63 (#72); @38 letter raise has a ghost at @28 (#32). Three clear firing-beat misses.

7. **Held-against-turn fire (@39, CrossFacet / AntiPattern-3).** Entry #45 fires `actor:taylor-hebert-westeros.feet-set` at @39. The tensometer STATE-UPDATE NOTE on @39 explicitly forbids canonical state-update co-citation (pure registration class). Even if `feet-set` were a valid schema field (it is not), this entry violates the cross-facet contract.

---

## 6. Floor-defense candidates

1. **Entry #44 `prop:oc-letter.position @38`** — fires correctly on the letter-raise beat; studio target; persistent across @38–@39. The rubric calibration anchor names this as ACCEPT. Survives V2.

2. **Entry #48 `prop:oc-letter.seal @41`** — seal-breaking is irreversible; studio target; field is standard for seal-bearing props per rubric §Authority. Survives V2.

3. **Entry #66 `actor:edric-cray.location @57`** — rubric calibration anchor; position-change persists; edric-fork authority. Survives V2.

4. **Entry #73 `prop:oc-ledger.taylor-entry-margin @64`** — structurally correct and rubric-mandated (tensometer @64 strongly expects). Fails only on the missing `actor:taylor.knowledge` co-entry. Floor-defensible as half-correct; a co-entry addition repairs it to full CORRECT without changing this entry.

---

## 7. Lock recommendation

**Rubric holds. Do NOT soften V2 axes.**

The 6.7%–7.8% V2 pass rate is not a rubric-calibration problem — it is the expected consequence of a rubric-blind author who fires on every motion-verb. The rubric's three axes (Reality, Authority, Frugality) correctly reject the contamination: invented fields, registration-as-state, approach-zone density, and cross-author prop-handling are all precisely the behaviors the rubric was designed to exclude.

The tensometer and narrator-interest cross-facet contracts are coherent and correctly flag the @39 violation and @64 missing co-entry. The Authority axis's distinction between studio-authored and character-fork-authored targets is the single most important rule a Phase 2 writer must internalize; the naive baseline ignored it entirely.

Recommended Phase 2 writer guidance additions:
- Hard rule: no `gaze-target`, `speech-target`, `face-orientation`, `activity`, `motion`, `grip`, `in-line`, `proximity-*` fields — none of these are schema-backed.
- Hard rule: `prop:*.holder` and `prop:*.position` are studio entries only; character fork writes `actor:<self>.posture` only with multi-beat persistence AND load-bearing annotation.
- Hard rule: approach zone (@1–@22, all tens=1) is silent unless a prop or environment field genuinely changes at project-open baseline; that baseline is set at setup, not at proto-line beats.
- Soft guidance: fire count ceiling is ~14 entries for s01e01 (18% of 77); if the author approaches 20, strip-test every entry before submitting.
