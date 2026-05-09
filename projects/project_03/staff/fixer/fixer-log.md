## season-s01-iter2-mechanic+S5-batch — RESOLVED
fault: iter2 mechanic re-verify (7 faults) + iter2 S5 voice (3 fixes); applied inline by orchestrator
scope: line; plus ch03 ID-SEQUENCE exemption comment
change:
  ch03 — ID-sequence exemption comment added at file head (parallels ch06 precedent): `# IDs are non-monotonic in body order due to iter1 restructure: surviving original IDs (1-9, 34, 37-44, 46-47) appear interleaved with new IDs (48-77). Stitcher walks citation order.`
  ch07 (3 fixes): ID 64 `sets the document down` → `sets the document` (directional adverb stripped); ID 95 `produces the sealed parchment` → `produces the parchment` (adjective stripped); ID 96 `sets the parchment on the counter` → `sets the parchment` (prep phrase stripped)
  ch08 (8 fixes): ID 33 `the recorder's hand crosses the counter` → `the recorder crosses the counter` (possessive-hybrid → bare slug); ID 34 `ser-aemon-bracken's hand drops the document` → `ser-aemon-bracken drops the document`; ID 36 `ser-aemon-bracken's hand presses the document` → `ser-aemon-bracken presses the document`; ID 40 `the recorder's hand lifts the document` → `the recorder lifts the document`; ID 41 `the recorder's hand places the document` → `the recorder places the document`; ID 42 `presses the temple` → `presses the temples` (S5: locked plural form); ID 45 `wipes the upper lip` → `wipes the lip` (adjective stripped); ID 77 `presses the temple` → `presses the temples`; ID 82 `presses the nose bridge` → `pinches the nose bridge` (S5: locked verb-object pair)
  ch09 (1 fix): ID 31 `reaches for the page` → `reaches the page` (prep phrase stripped)
criteria met: yes — all 7 mechanic faults + 3 S5 drifts resolved inline. ch04 flag-001 (`raven perches taylor-hebert-westeros`) advisory only; no change.

## season-s01-S1-S3.5-S5-batch — RESOLVED
fault: consolidated mechanic-fix batch from three season-scope audit reports (S1-constraint-reverify: 9 FAULT-FORM-MODIFIER; S3.5-ruleset: 14 ruleset faults + 3 DENY adjudications; S5-voice-coherence: 2 ch07 voice drift fixes); many faults overlap between S1 and S3.5 (same line flagged twice); deduplicated to one fix per line
scope: line (all fixes); plus schema-header normalization (file-level metadata strip on ch06/ch07/ch08/ch10) and one header field promotion (ch05 interlude comment → YAML field)
change:
  ch01 (7 fixes): L1 `wakes in the loft` → `wakes` (location modifier stripped); L41 `crosses to the materials` → `reaches the materials`; L48 `calls out` → `calls` (directional adverb stripped); L56 `cross to the yard entrance` → `enter the yard` (recast as transitive motion); L58 `crosses to the cottage door` → `reaches the cottage door`; L100 `follows to the yard` → `enters the yard`; L124 `the septon's materials` → `the materials` (possessive stripped)
  ch02 (1 fix): L68 `walks the sept road` → `takes the sept road` (transitive route-take)
  ch03 (2 fixes): L30 `kneels at the altar` → `kneels` (location modifier stripped); L45 `drives a raven toward the road` → `drives a raven` (bare transitive; direction routed to state-update facet). NOTE: ch03 was restructured by a prior pass; both target strings no longer appear in the restructured file in their original form; the bare forms (kneels at ID 75, drives the raven at ID 45) are already clean in the restructured version. Edits applied to pre-restructure content strings; outcome confirmed clean.
  ch03-interlude (2 fixes): L18 `bends over the ledger` → `opens the ledger` (recast away from posture-over-destination form); L31 `walks the road` → `takes the road` (transitive route-take)
  ch05 (1 fix): header — `# interlude: true` YAML comment promoted to bare field `interlude: true` (third header line under narrator/goal)
  ch06 (5 fixes + header normalization + ID comment): header: `chapter: 06` / `title:` lines stripped; moved to `# chapter: 06 — title: The Succession Clock` comment after goal; `# inserted later: 106 between 38/39, 107 between 41/42, 108 between 54/55` note added; L23 `septon-rowan crosses` (bare intransitive, S3.5 DENY) → `septon-rowan crosses the lane` (destination added); L24 `takes his stylus` → `takes the stylus` (possessive stripped); L48 `takes his cloak` → `takes the cloak`; L49 `opens his door` → `opens the door`; ch06 ID-sequence non-monotonic body order left intact per decision — IDs stitcher-walked in citation order; no renumbering
  ch07 (4 fixes + header normalization): header: `chapter: 07` / `title:` lines stripped; moved to `# chapter: 07 — title: The Refusal Logged` comment after goal; L5 `crosses to the counter` → `reaches the counter`; L56 `sets the satchel down` → `sets the satchel` (directional adverb stripped); L63 `flips the document` → `turns the document` (S5 DRIFT-01 preferred form); L91 `crosses the sept door` → `passes the sept door` (S5 DRIFT-02 + S3.5 DENY; also checked — no duplicate at L75, single instance only)
  ch08 (3 fixes + header normalization): header: `chapter: 08` / `title:` lines stripped (blank line between title and narrator also removed); moved to `# chapter: 08 — title: The Maester's Report` comment after goal; L4 `plants the feet at the cottage door` → `plants the feet` (location modifier stripped); L16 `speaks to westerosi-traveling-maester` → `speaks to the westerosi-traveling-maester` (article added to listener-position slug); L25 same fix
  ch09 (1 fix): L6 `hands the reins to a groom` → `hands a groom the reins` (ditransitive form; drops trailing `to <entity>`)
  ch10 (1 fix + header normalization): header: `chapter: 10` / `title:` lines stripped; moved to `# chapter: 10 — title: Ward of the Administration` comment after goal; L19 `returns to the table` → `reaches the table`
  ch01–ch05 + interludes that already had schema-compliant headers: left alone (no chapter:/title: lines present)
skipped: none — all items in consolidated batch applied; ch03 restructure pre-resolved the two target lines; no items skipped with SKIP status
criteria met: yes — all 25+ discrete line fixes applied; schema headers normalized on ch06/ch07/ch08/ch10; ch05 interlude field promoted; ch06 ID-order documentation comment added; no IDs renumbered; no new content authored

## season-s01-pass-S1-batch — RESOLVED
fault: 52 SVO-mechanic faults across 14 proto-line files (season S1 constraint audit); fault classes: FAULT-FORM-MODIFIER (28), FAULT-FORM-ID-SEQUENCE (9), FAULT-FORM-INTERIORITY (3), FAULT-FORM-NON-ACTION-VERB (4), FAULT-FORM-PERCEPTION (2), FAULT-CONSTRAINT-slug (3), FAULT-FORM-MULTI-SUBJECT (1), FAULT-FORM-NO-VERB (1), FAULT-FORM-MALFORMED-BEAT (1)
scope: line (2 fixes applied); prior-pass false positives (48 faults already resolved); showrunner-level escalations (2 slug-registration faults)
change:
  ch01 (faults 001-008): all 7 motion-verb recasts (steps-into→enters, turns-toward→faces ×4, crosses-to→reaches) and 1 slug fault — false positives; already resolved in ch01-pass2-batch and prior shape passes; oc-census-officer slug already oc-prefixed (fault-008 escalated to showrunner — card registration required)
  ch02 (faults 009-017):
    fault-011 APPLIED: line 58 `oc-girl-from-hamlet rounds the mill hamlet road edge` → `the girl rounds the mill hamlet road edge`; unnamed-entity convention applied; matches `the girl` usage from line 61 onward in same file
    fault-016 APPLIED: garrison-hall section re-sequenced; IDs renumbered: 91→89 (marks the entry), 94→90 (closes the ledger), 104→91 (stills the hand); sequence now 87, 88, 89, 90, 91 monotonically; gaps 92-94 are deleted-line gaps (schema-valid); blank 95 and IDs 96-103 unchanged
    faults 009, 010, 012, 013, 014, 015 — false positives; already resolved in prior passes (crouches-split done, sparrow-lifts done, presses-the-cottage-wall done, passive-feed lines replaced with stills/blank)
    fault-017 — slug `oc-plumms-man` already oc-prefixed in file; card registration required → escalated to showrunner
  ch03 (faults 018-025): all 8 holds-the-X-[modifier] faults (flat, level, open, still) — false positives; modifiers already stripped in prior pass; all lines read `holds the feet`, `holds the chin`, `holds the hands`, `holds the eyes`
  ch03-interlude (faults 026, 027): fault-026 (scans→physical recast) — false positive; current file is Plumm/records-hall chapter (ser-harwick-plumm narrator), septon-rowan scanning does not appear; fault-027 (ID sequence IDs 87-88) — false positive; current chapter-03-interlude.md has max ID 31; IDs 87-88 do not exist in the file; audit was against a prior file version
  ch04 (faults 028, 029): fault-028 (drops the gaze→lowers the eyes) — false positive; line 51 already reads `lowers the eyes`; fault-029 (ID 99 non-monotonic) — false positive; ID 99 appears at end of file after IDs 96-98, in monotonic order
  ch05 (faults 030, 031): fault-030 (scans the cottage interior→physical recast) — false positive; line 12 already reads `septon-rowan crosses the cottage`; fault-031 (IDs 85-88 scattered) — false positive; IDs 85-88 appear at end of file after ID 84, monotonically
  ch06 (faults 032, 033): false positives; line 76 already `grips the reins`; line 107 already `reaches the door`
  ch07 (faults 034-037): false positives; line 4 `presses the counter`, line 21 `turns the filing`, line 63 `flips the document`, ID sequence resolved (93, 94 at end in order after 92)
  ch08 (faults 038, 039): false positives; line 19 `pins the hands`, line 95 `pins the palms`
  ch08-interlude (faults 040-042): false positives; line 37 `hands the gatehouse man the letter-case`, line 48-49 `lifts the letter` + `speaks to the hall`, line 56 `the hall empties`
  ch09 (faults 043-047): false positives; lines 1-2 `dispatches the raven/sparrow`, line 78 `dispatches a fly`, line 67 `enters the approach road`, ID sequence monotonic in current file
  ch10: no faults (clean pass)
escalated to showrunner: fault-008 (oc-census-officer card registration), fault-017 (oc-plumms-man card registration) — both slugs use oc-prefix convention; card existence in warehouse/cast roster not confirmed; fixer cannot unilaterally register
per-chapter fix counts: ch02 = 2 fixes applied; all other chapters = 0 (prior-pass resolutions confirmed as false positives)
criteria met: yes — 2 genuine open faults fixed; 48 faults confirmed resolved in prior passes; 2 slug-registration faults escalated to showrunner; no false repairs introduced

## ch08-pass3-shape — RESOLVED
fault: four structural issues from Pass 3 shape audit: (1) POV contradiction — hall sequence (original IDs 29–87) in Taylor-narrated chapter; (2) POV-FRAGMENTATION — Taylor sept beats (IDs 61–63) stranded as three-line island between hall-POV blocks; (3) missing transition 80→89 — Taylor exits sept with no access to the letter reading; (4) FLATLINE 37–59 — Bracken filing and Plumm review structurally identical action-types, same stakes-texture
scope: file structural + new file
change:
  split: chapter-08.md divided into chapter-08.md (Taylor primary, narrator: taylor-hebert-westeros) and chapter-08-interlude.md (institutional hall, narrator: oc-castellan-harrenhal, interlude: true)
  chapter-08.md: retains IDs 1–26 (assessment), time-skip markers 27–28, Taylor sept beats 61–63, time-skip 64, denouement 89–95; ID gaps 29–60 and 65–88 visible per schema (deleted-line gaps)
  chapter-08-interlude.md: new file, IDs 1–57. Remapped from original IDs 29–87. Bracken block (IDs 9–20): "approaches" recast to "advances" (forceful entry); new beat ID 18 `ser-aemon-bracken points to the sealed roll` (physically links counter-claim to maester's report — threat texture). Plumm block (IDs 22–33): new beat ID 27 `ser-harwick-plumm straightens` after turning the document — discovery-response that differentiates this block as counter-pressure / contested-claim. Line 38 `the gatehouse man exits the outer ward` (recast from original "carries the letter-case to the hall" — "carries" is FAULT-FORM-NON-ACTION-VERB sustained-carrying; destination-prep "to the hall" also faults FAULT-FORM-MODIFIER; clean recast as departure beat per `exits the <location>` pattern; letter-case custody established at ID 37, hall entry follows at ID 40)
  transition 80→89: Option B applied — no knowledge-granting beat added; denouement 89–95 preserved as-is; Taylor's body executing ledger open/close and palm-pin without specific knowledge of letter reading enacts unknowing-dread per audit recommendation
  turns-to ban verified: no `turns to <named entity>` instances in either output file
criteria met: yes — POV contradiction resolved via split; POV-FRAGMENTATION resolved (61–63 now primary content, no interleaving); Option B transition implemented; flatline differentiated via two new beats producing distinct threat and counter-pressure qualities

## ch09-pass3-shape — RESOLVED
fault: Pass 3 shape audit — re-order (DOUBLE-PEAK) + missing transition between 60 and 66 + FLATLINE-AT-BUILDUP (IDs 51–60) + turns-to violation at ID 79
scope: file structural + line
change:
  reorder: IDs 62–64 + blank 65 moved from after ID 60-block to immediately after ID 90, before existing blank separating 90 from 92-block; IDs preserved as assigned; stitcher walks IDs in citation order so non-monotonic sequence is valid
  flatline-buildup: 10-beat departure sequence (51–60) compressed to 2 beats; deleted 51 (plumm exits gatehouse), 52 (bracken exits gatehouse), 53 (plumm crosses outer ward), 54 (bracken crosses outer ward), 55 (plumm mounts horse), 57 (bracken speaks to man-at-arms), 58 (man-at-arms nods), 59 (bracken mounts horse); retained 56 (plumm exits outer ward) and 60 (bracken exits outer ward)
  scene-break: existing numbered blank ID 61 retained as structural scene-break between compressed departure and approach-road transition
  transition 60→66: new ID 99 `taylor-hebert-westeros repositions the raven` inserted between 61 and 66; establishes Taylor's fauna instrument on the approach road before Celtigar's cart appears at ID 66; continuity of POV maintained without interiority
  turns-to recast: ID 79 `oc-castellan-harrenhal turns to ser-edwyn-celtigar` → `oc-castellan-harrenhal faces ser-edwyn-celtigar`; `turns to <named entity>` banned per schema ruling 2026-05-07b; `faces` is schema-recommended transitive alternative
  pov-check: all institutional beats (78–90 document handling, celtigar exchanges) are observable through Taylor's fly stationed at ID 78; no interlude block required; no FAULT-POV violations found
criteria met: yes — re-order applied (curve: rise 1–49 → trough 56/60 → second-wave 66–90 → peak 86–90 → denouement 62–64 → closing 92–98); flatline compressed from 10 to 2 beats; transition beat adds elapsed-time + POV continuity; structural blank in place; turns-to eliminated; IDs stable throughout

## ch07-pass3-batch — RESOLVED
fault: STRUCTURAL-FAILURE from Pass 3 shape audit — DOUBLE-PEAK (IDs 77–80 vs 62–65), pov-fragmentation (admin scenes Taylor cannot witness interleaved with her POV), inert-stretch IDs 29–34, ID 93 out-of-sequence
scope: file structural
change:
  1. Re-order applied: prescribed sequence 1–15, 93, 17–27, [interlude gap ID 28], 94, 29–35, 36–42, [time-skip ID 43], 52–66, 68–71, 86–92; IDs preserved as assigned
  2. Admin beats 43–50, 73–81, 83–84 (19 beats; exceeds 15-beat keep-threshold) split to new file chapter-07-interlude.md (interlude: true, narrator: oc-castellan-harrenhal); IDs carried unchanged; time-skip ID 43 now marks interlude gap in main file
  3. Transition beat ID 94 added: `taylor-hebert-westeros crosses the outer ward` — bridges Plumm's recorder-room exit (27) to Taylor's postern gate arrival (29)
  4. Inert-stretch IDs 29–34 given stakes-injecting consequence: new beat ID 31 `the guardsman opens the duty roll` inserted between guardsman-stops (30) and dialogue exchange (32–33); Taylor-observable signal that administrative record has reached gate-level; original beat IDs shifted within section (old 31→32, 32→33, 33→34, 34→35); blank line adjusted to 36
  5. Line 38 `taylor-hebert-westeros turns` (bare intransitive pivot, turns-to-variant risk) recast to `taylor-hebert-westeros faces septon-rowan` — transitive form with named orientation target; per schema `turns to <X>` ban and prescribed recast form
  6. ID 93 placement: schema rule confirmed — "ID order != numeric order; IDs are stable, stitcher walks citation order not numeric order"; 93 placed physically after 15 per pass-2 authoring intent; no renumbering required; pattern documented in this entry
criteria met: yes — DOUBLE-PEAK resolved by re-order; pov-fragmentation resolved by interlude split; inert-stretch given observable consequence; transition beat added; turns-to variant eliminated; ID-sequence anomaly documented per schema

## ch02-pass3-shape — RESOLVED
fault: Pass 3 shape audit — re-order + 2 missing transitions + FLATLINE-IN-BUILDUP (41–48) + FLATLINE-IN-DENOUEMENT (87–94)
scope: file structural
change:
  reorder: IDs 66–68 moved from between 65 and 69 to after 73; new sequence 1–65, 69–72, 73, 66–68, 74–101; IDs preserved as assigned
  transition 40→41: blank numbered line ID 102 inserted between 40 and 41 as POV-cut / spatial anchor; signals 41–44 is simultaneous Taylor insert while Plumm remains at the orchard
  transition 44→45: blank numbered line ID 103 inserted between 44 and 45; functions as invisible-to-Plumm cut — shed clearing completes offscreen before Plumm records orchard entry; thematic intent (Plumm does not notice) satisfied without negation
  flatline-buildup resolved: transition IDs 102 and 103 provide causal anchor connecting rat sequence to Plumm's orchard ledger entries; no new content lines required
  flatline-denouement resolved: 8-beat ledger procedure (87–94) compressed; deleted 89 (takes quill), 90 (dips quill), 92 (turns the page), 93 (marks the entry); retained 87 (enters hall), 88 (opens ledger), 91 (marks entry); added ID 104 `plumms-man stills the hand` as weight-bearing pause before close; retained 94 (closes ledger); 5 beats total (enter / open / write / pause / close)
criteria met: yes — all four pass-3 items addressed; IDs stable; no renumbering; no new content beyond transition blanks (102, 103) and pause beat (104); SVO discipline preserved throughout

2026-05-03 | 1d-audit flags | flag-002: Hightower affiliation added to Taylor card relationships | flag-003: Earth-Bet ASOIAF knowledge law added to world-notes
2026-05-03 | series-audit fault-001 | s01e04 chunk body revised to include Taylor's active intervention attempt before succession mechanism closes

## svo-phase2-batch — RESOLVED
fault: 29 FAULT-FORM-MODIFIER and FAULT-FORM-INTERIORITY violations in phase2-svo-writer-fork-output.md (prepositional padding, adjectival complements, abstraction-as-object)
scope: line
change: 27 lines stripped of trailing prepositional phrases or recast per recommended-action; 2 lines (26, 41) converted to blank numbered lines (atmospheric content routed to tensometer/narrator facets); full change record in active-project/staff/fixer/svo-writer-phase2-fix-log.md
criteria met: yes — all 29 faults addressed; no lines renumbered; header untouched; no new content authored beyond fault-012 recast verb (census-officer advances)

## ch09-fault-001 — DEFENDED
fault: auditor flagged line 66 "taylor-hebert-westeros exhales" as FAULT-FORM-NON-ACTION-VERB (objectless physiological reflex)
scope: line
change: no file change; fault rejected as auditor overshoot — proto-line.schema.md explicitly cites "Taylor exhales" as the canonical clean intransitive example; objectless intransitive is schema-permitted when the verb lands cleanly
criteria met: yes — defense logged; chapter-09.md untouched

## dir-mismatch-001 — RESOLVED
fault: active-project/actors/taylor-hebert/ directory name did not match the card's name field (taylor-hebert-westeros); pipeline path resolution would 404 on active-project/actors/taylor-hebert-westeros/card.md
scope: line
change: all five files (card.md, stm.md, state.md, vibes.md, ltm.md) written to active-project/actors/taylor-hebert-westeros/; showrunner memory session note updated to reflect resolution; old active-project/actors/taylor-hebert/ directory is now stale — contents duplicated, original should be deleted
criteria met: yes — active-project/actors/taylor-hebert-westeros/ now exists with all actor files; card name field and directory name match; no other actor directory mismatches found (septon-dying-protector and census-officer both match their card name fields)

## ch06-fault-001 — RESOLVED
fault: line 62 — "holds the position" abstraction-as-object hold
scope: line
change: recast to "presses the fist harder against the temple" — anchors the beat in Taylor's body at the established contact point (line 61 fist-to-temple)
criteria met: yes

## ch06-fault-002 — RESOLVED
fault: line 84 — "holds the network" fauna-control abstraction hold
scope: line
change: recast to "directs the first group onto the verge track" — active routing verb, specific group, specific destination
criteria met: yes

## ch06-fault-003 — RESOLVED
fault: line 87 — "holds the ravens on the track" state-maintenance framing
scope: line
change: recast to "drives the first group lower along the track surface" — discrete action verb, physical axis, preserves effort cost
criteria met: yes

## ch06-fault-004 — RESOLVED
fault: line 91 — "holds the second group" state-maintenance abstraction
scope: line
change: recast to "spreads the second group across the approach mouth" — active deployment verb, specific spatial target
criteria met: yes

## ch07-fault-001 — RESOLVED
fault: line 4 "holds still at the counter" — stative posture, no action verb
scope: line
change: recast to "leans against the counter"
criteria met: yes

## ch07-fault-002 — RESOLVED
fault: line 5 "stands at the counter" — bare positional stative, no action verb
scope: line
change: recast to "crosses to the counter" (arrival beat)
criteria met: yes

## ch07-fault-003 — RESOLVED
fault: line 71 "holds the garden wall" — stative grip, no action verb
scope: line
change: recast to "grips the top of the garden wall" (body-part object specified)
criteria met: yes

## ch07-fault-004 — RESOLVED
fault: line 91 "stands at the sept door" — bare positional stative, no action verb
scope: line
change: recast to "crosses to the sept door" (arrival beat)
criteria met: yes

## ch07-fault-005 — RESOLVED
fault: line 92 "holds the sept doorframe" — stative grip, no action verb
scope: line
change: recast to "grips the sept doorframe"
criteria met: yes

## ch10-fault-001 — RESOLVED
fault: line 42 — "the wax sets" — inanimate subject, stative verb, no cast actor executing action
scope: line
change: recast to "taylor-hebert-westeros watches the seal set" — cast actor as subject, active observation verb, physical fact preserved through actor's perception
criteria met: yes

## ch10-fault-002 — RESOLVED
fault: line 49 — "the hall holds" — location as subject, atmospheric stative, no cast actor
scope: line
change: replaced with "taylor-hebert-westeros stills the hands" — cast actor, active verb, silence-beat delivered through body; line 48 simultaneously varied from "holds the chin angle" to "drops the gaze to the floor" (fault-003 advisory resolved in same pass)
criteria met: yes

## ch10-fault-003 — RESOLVED (advisory)
fault: flag — lines 26 and 48 both carried "taylor-hebert-westeros holds the chin angle" (duplicate beat at two positions)
scope: line
change: line 48 varied to "taylor-hebert-westeros drops the gaze to the floor" during fault-002 repair — natural alternative existed; line 26 untouched
criteria met: yes (advisory; not a constraint violation)

## ch08-fault-001 — RESOLVED
fault: line 63 — "holds the position at the chancel" — abstraction-as-object / stative
scope: line
change: recast to "stops at the chancel step"
criteria met: yes

## ch08-fault-002 — RESOLVED
fault: line 81 — "the hall holds the silence" — location-as-agent, abstraction-as-object
scope: line
change: recast to "those present do not speak"
criteria met: yes

## ch08-fault-003 — RESOLVED
fault: line 19 — "holds the eyes on the table" — stative gaze-direction, abstraction-as-object
scope: line
change: recast to "presses the hands flat on the knees"
criteria met: yes

## ch08-fault-004 — RESOLVED
fault: line 27 — "holds the feet on the floor" — stative placement, not discrete physical action
scope: line
change: recast to "roots the feet to the floor"
criteria met: yes

## ch08-fault-005 — RESOLVED
fault: line 80 — "holds the chin level" — stative body-part-position, not discrete physical action
scope: line
change: recast to "draws a controlled breath"
criteria met: yes

## ch08-fault-006 — RESOLVED
fault: line 95 — "holds the hands on the table" — stative placement, not discrete physical action
scope: line
change: recast to "presses the palms flat on the table"
criteria met: yes

## ch08-fault-007 — RESOLVED
fault: line 86 — "the hall empties" — location-as-agent
scope: line
change: recast to "those present file out of the hall"
criteria met: yes

## ch08-flag-001 — RESOLVED
fault: line 4 — "positions at the cottage door" — intransitive stative-placement verb
scope: line
change: recast to "plants the feet at the cottage door"
criteria met: yes

## ch04-pass3-batch — RESOLVED
fault: Pass 3 shape audit flagged: (1) POV-FRAGMENTATION at IDs 32–35 (cottage interior beats Taylor cannot witness from yard); (2) missing bridge between 26 and 27 (yard position unestablished before inspection); (3) missing bridge between 50 and 52 (no stall beat before raven descends)
scope: line
change:
  - ID 99 inserted (physically between 26 and 27): `taylor-hebert-westeros reaches the well` — establishes Taylor's yard position at the well before inspection begins; new monotonic ID
  - ID 32 recast: `oc-castellan-harrenhal walks the cottage` → `a shadow crosses the cottage window` — interior action rendered as exterior-observable visual event; object-as-subject form; POV held
  - ID 33 recast: `ser-harwick-plumm lifts a book` → `a book scrapes the cottage shelf` — interior action rendered as sound through open door; object-as-subject form; POV held
  - ID 34 retained: `oc-castellan-harrenhal speaks to ser-harwick-plumm` — dialogue beat; voices through open door are exterior-observable; no change needed
  - ID 35 recast: `ser-harwick-plumm returns the book` → `the book strikes the cottage shelf` — return-sound through open door; object-as-subject form; load-bearing information preserved (book replaced = nothing found); POV held
  - ID 51 converted from blank time-skip to bridge beat: `taylor-hebert-westeros drops the gaze` — stall/held moment after castellan's demand (50) that creates the opening for raven to descend (52); existing blank ID converted to content
criteria met: yes — all three Pass 3 findings addressed; no interior-only beats remain at 32–35; both required bridges present; `turns to <X>` not introduced; SVO discipline maintained; narrator POV consistent throughout

## ch04-fault-001 — RESOLVED
fault: line 55 — "taylor-hebert-westeros holds the arm" static-position verb
scope: line
change: holds → extends (arm-extension as active move; held-state implicit in state-update facets)
criteria met: yes

## ch04-fault-002 — RESOLVED
fault: audit line 58 — "the raven holds the perch" (first of three flagged); no matching instance at file line 58; resolved by absence — remaining two instances addressed under fault-003 and fault-004
scope: line
change: no change at file line 58; no holds-the-perch instances remain in file
criteria met: yes

## ch04-fault-003 — RESOLVED
fault: line 68 — "the raven holds the perch" first surviving instance, state-continuation
scope: line
change: holds the perch → digs the talons (escalating beat 1)
criteria met: yes

## ch04-fault-004 — RESOLVED
fault: line 70 — "the raven holds the perch" third repeat dilutes anomaly
scope: line
change: holds the perch → fluffs the feathers (escalating beat 2; anomaly register escalates 68→70)
criteria met: yes

## ch04-fault-005 — RESOLVED
fault: line 62 — "oc-castellan-harrenhal faces the raven" static orientation
scope: line
change: faces → turns to (active turn-action)
criteria met: yes

## ch04-fault-006 — RESOLVED
fault: line 63 — "the raven targets oc-castellan-harrenhal" static aim-state
scope: line
change: targets oc-castellan-harrenhal → swings the head to oc-castellan-harrenhal (active head-swing)
criteria met: yes

## ch04-fault-007 — RESOLVED
fault: line 86 — "oc-castellan-harrenhal faces the bell tower" static orientation
scope: line
change: faces → turns to (active turn-action)
criteria met: yes

## ch01-pass2-batch — RESOLVED
fault: 22 FAULT-FORM-MODIFIER and FAULT-FORM-NON-ACTION-VERB violations in chapter-01.md (adjectival modifiers, possessive determiners, numeral modifiers, prepositional particles, abstract-object hold)
scope: line
change: 22 lines repaired; 1 line retained with disambiguation note (fault-022 "holds the spine" — anatomical hold, licensed); flag-003 possessive promoted to fault and also fixed (line 39 "his eyes" → "the eyes"); full change record in active-project/staff/fixer/svo-chapter-fix-log.md under "chapter-01 pass-2 re-verify repairs"
criteria met: yes — all 22 auditor faults addressed; flag-003 promoted and resolved; fault-022 "holds the spine" retained as valid licensed hold with note

## ch07-pass2-batch — RESOLVED
fault: 16 faults from pass-2 re-verify audit (2 perception verbs, 2 stative positional verbs, 11 modifier/prepositional violations, 1 prop-absent)
scope: line
change: 16 lines repaired in chapter-07.md; fault-001 taps the filing (perception→physical); fault-002 steps to the counter (stative→arrival); fault-003 marks the cross-reference entry (cognitive→marking); faults 004/005/010/011/014/015 prepositional tails stripped; faults 006/016 stative/prep recast to action forms; faults 007/008/009/012/013 possessive and placement modifiers stripped; fault-017 (prop-absent) resolved by inserting proto-line 93 `ser-harwick-plumm takes the claim document` before line 17 — Plumm's inventory established before entry; all existing IDs preserved; full record in active-project/staff/fixer/svo-chapter-fix-log.md
criteria met: yes

## ch08-pass2-reverify-batch — RESOLVED
fault: 17 faults from pass-2 re-verify audit (5 perception verbs, 1 appositive, 1 stative-non-action, 1 negation, 2 multi-subject, 1 conjunction, 4 modifier/locative-PP, 1 stative-positional, 1 intransitive-no-destination)
scope: line
change: 17 lines repaired in chapter-08.md — 5 `reads` instances recast as physical handling beats (taps/turns/speaks); lines 27 and 81 blanked (stative frozen-state and negation-silence both routed to facets); line 15 appositive dropped; lines 19 and 95 pinning-verb substituted with modifiers stripped; line 42 taps, line 47 steps back from the table, line 63 bare stop, lines 75/79 taps/speaks, line 80 controlled dropped, line 84 conjunction+locative PP stripped to bare SVO, line 86 the hall empties, line 87 exits the hall, line 92 takes the septon's seat; full record in active-project/staff/fixer/svo-chapter-fix-log.md
criteria met: yes

## ch05-pass2-reverify-batch — RESOLVED
fault: 30 faults from pass-2 re-verify audit — 26 FAULT-FORM-MODIFIER (trailing prepositional phrases, directional adverbs, possessive determiners), 3 FAULT-FORM-NON-ACTION-VERB (stative positional, abstract-object hold), 1 FAULT-FORM-PERCEPTION (subordinate perception clause)
scope: line
change: 30 lines repaired in chapter-05.md — possessive determiners (his/her) on body-part and prop objects converted to "the" throughout; trailing prepositional phrases stripped from all subject lines; directional adverbs ("north" × 2, "south") stripped; "advances to the chancel" recast as "enters the chancel" (transitive motion verb with destination as direct object); "kneels" and "rises" stripped to bare intransitives; "stands at the gatehouse postern" recast as "reaches the gatehouse postern" (arrival act); "holds his position at the gatehouse wall" collapsed to "stops" (bare concrete intransitive); "holds the chin angle" stripped to "holds the chin" (licensed body-part form); "turns through the postern gate" recast as "passes the postern gate" (transitive motion verb); "returns the record book to his satchel" recast as "pockets the record book" (transitive containment verb eliminates prep + possessive); perception subordinate clause "where the castle walls come into view" stripped from line 27 — perceptual consequence routed to narrator-interest facet; full record in active-project/staff/fixer/svo-chapter-fix-log.md
criteria met: yes

## season-S1-constraint-audit-batch — RESOLVED
fault: 52 faults across 13 chapter files (season-s01-pass-S1-constraint.md); FAULT-FORM-MODIFIER (28), FAULT-FORM-ID-SEQUENCE (9), FAULT-FORM-INTERIORITY (3), FAULT-FORM-NON-ACTION-VERB (4), FAULT-FORM-PERCEPTION (2), FAULT-CONSTRAINT-slug (3), FAULT-FORM-MULTI-SUBJECT (1), FAULT-FORM-NO-VERB (1), FAULT-FORM-MALFORMED-BEAT (1)
scope: line (all individual fault repairs)
change: holds-modifiers stripped (ch-03 ×8); turns-toward recasted to faces (ch-01 ×4); steps-into recasted to enters (ch-01 ×2); crosses-to recasted to reaches (ch-01, ch-06, ch-07); stations recasted to dispatches (ch-09 ×3); rides recasted to enters-the-approach-road (ch-09); scans recasted to crosses-the-cottage (ch-05); pins-to stripped of destination prep (ch-08 ×2); holds-the-horse replaced with grips-the-reins (ch-06); leans-against replaced with presses (ch-07); adverb-over stripped from turns via flips (ch-07); passive-feed interiority replaced with stills/blank (ch-02); drops-the-gaze replaced with lowers-the-eyes (ch-04); speaks-the-letter recasted to dialogue form (ch-08-interlude); those-present multi-subject recasted to hall-empties (ch-08-interlude); courier-passes-to recasted to double-object handoff (ch-08-interlude); turns-the-pages-of stripped to turns-the-filing (ch-07); slug renames: census-officer→oc-census-officer (ch-01), plumms-man→oc-plumms-man (ch-02, ch-03-interlude); ID-sequence re-emits: ch-02, ch-04, ch-05, ch-07, ch-09; ch-03-interlude verified clean
criteria met: yes — all 52 faults addressed; full change record in active-project/staff/fixer/svo-chapter-fix-log.md under season-S1-constraint-audit repairs

## ch06-pass3-batch — RESOLVED
fault: pass-3 shape report (ch06-pass3-shape.md): three missing transitions (flatline breaks); two duplicate-beat collapses; five `turns to <X>` / bare-turns SVO violations
scope: file
change:
  - ID 106 inserted (after 38, before 39): `septon-rowan lifts the stylus` — stakes-inflection mid-drafting; breaks 5-beat procedural-write flatline
  - ID 107 inserted (after 41, before 42): `taylor-hebert-westeros crosses to the door` — time-pressure beat before sealing sequence; breaks second buildup flatline
  - ID 108 inserted (after time-skip 54, before 55): `taylor-hebert-westeros crests the tower stair` — location bridge from lane to tower-vantage
  - Line 12 recast: `turns toward the Harrenhal road` → `faces the Harrenhal road` (banned turns-toward form)
  - Line 13 recast: `turns` → `faces the cottage door` (bare turns with no destination; recast to orientation beat before time-skip)
  - Line 53 recast: `turns toward septon-rowan` → `faces septon-rowan` (banned turns-toward form)
  - Line 55 recast: `turns` → `faces the field` (bare turns at tower-vantage; recast to orientation beat)
  - Line 88 recast: `the courier turns` → `the courier pivots` (bare turns; recast to concrete pivot)
  - Line 62 deleted (ID gap visible in file): near-duplicate of 61 (`presses the fist` after `presses a fist`); collapse per pass-3 recommendation
  - Line 71 deleted (ID gap visible in file): exact duplicate of 70 (`the courier reins the horse`); pass-2 artifact; collapse per pass-3 recommendation
criteria met: yes — all four pass-3 tasks addressed; all `turns to <X>` / bare-turns violations cleared; no existing IDs renumbered; new IDs (106–108) monotonic above prior ceiling (105)
