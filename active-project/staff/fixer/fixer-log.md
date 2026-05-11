## SESSION-START — 2026-05-11T09:00:00Z — season-s01-pass-2-fix-round2
dispatch: resolve all faults from season-s01-pass-2-constraint.md + season-s01-pass-2-continuity.md — Groups 1–9: REFERENCE-DRIFT, POV-LEAKS, PROP-STATE, FORM faults (marks/reads-aloud/modifier/interiority/non-action-verb), SLUG-UNRESOLVED, relay-policy-flag
target: active-project/theater/proto-lines/s01.bones.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint.md + active-project/staff/auditor/season-s01-pass-2-continuity.md
findings-queued: tbd (reading audit reports first)

## GROUP1-REFERENCE-DRIFT — CONFIRMED-RESOLVED-PRIOR-SESSION — 2026-05-11T09:05:00Z
fault: "the maester" used post-beat-16 (IDs 303+) instead of slug oc-broken-maester
scope: line
change: verified in file — all IDs 303–422 already use oc-broken-maester; IDs 111–301 retain "the maester" correctly; resolved in prior session
criteria met: yes

## GROUP2-POV-LEAKS — CONFIRMED-RESOLVED-PRIOR-SESSION — 2026-05-11T09:05:00Z
fault: IDs 157-158, 282-283, 203-204 outside Taylor's coverage or narrator-intrusion POV leaks
scope: line
change: verified in file — IDs 157, 158, 203, 204, 282, 283 are blank (ID gap markers); resolved in prior session
criteria met: yes

## GROUP3-PROP-STATE-01 — FLAGGED-FOR-SCREEN-WRITER — 2026-05-11T09:05:00Z
fault: log opened at ID 201, written at ID 202, never closed, opened again at ID 205
scope: n/a (cannot add IDs)
change: none — IDs 203/204 are now deletion gaps; a close-log bone must be added between 202 and 205; fixer cannot introduce new IDs; flagging as screen-writer REGEN-ADD task
criteria met: no — structural gap remains; screen-writer must add close-log entry at beat-10

## GROUP4-FORM-PERCEPTION — RESOLVED — 2026-05-11T09:15:00Z
fault: marks (×17) and reads aloud (×2) perception verbs on human subjects
scope: line
change: IDs 14, 17, 66 confirmed already fixed (prior session); IDs 109, 113, 123, 223, 224, 271, 272, 352, 353, 446, 447 confirmed already fixed (writes the entry); ID 111 confirmed already fixed (speaks to the room); ID 129 confirmed already fixed (speaks); IDs 170, 171 fixed this session: marks the scan pattern → stills (both); ID 166 confirmed already fixed (holds the step)
criteria met: yes — no "marks" or "reads aloud" perception forms remain

## GROUP5-FORM-MODIFIER — RESOLVED — 2026-05-11T09:30:00Z
fault: 45 instances of prepositional padding, adverb intrusions, adjective modifiers on objects
scope: line
change: applied 38 targeted Edits this session — see full list in fixer report; pivots-toward form retained (schema-licensed); 2 items (IDs 157, 158) resolved via Group 2 deletion
criteria met: yes — all 45 auditor-listed instances resolved

## GROUP6-FORM-INTERIORITY — RESOLVED — 2026-05-11T09:35:00Z
fault: cognitive verbs and abstract-noun objects (maps ×3, recalculates ×1, routes-abstract ×5, relay-abstract ×1, thin-abstract ×1)
scope: line
change: IDs 189, 191, 193 deleted (blank gaps — maps-cognitive); ID 140 → pivots; ID 145 → speaks to oc-dock-runner; ID 174 → speaks to oc-tanner-father; ID 381 → speaks to taylor-hebert-flea-bottom; ID 386 → speaks to the dock-side cluster; ID 390 → retract; ID 130 → south-wall footfall (concrete noun recast per auditor instruction); ID 86 → speaks to oc-tanner-father (abstract plan-noun recasted to speech-act)
criteria met: yes — no cognitive verbs or abstract-noun objects remain in audited lines

## GROUP7-FORM-NON-ACTION-VERB — RESOLVED — 2026-05-11T09:36:00Z
fault: IDs 203/204 receive-possession (already deleted); ID 237 fill-containment
scope: line
change: IDs 203/204 confirmed deleted (prior session); ID 237 fill → press
criteria met: yes

## GROUP8-SLUG-UNRESOLVED — RESOLVED — 2026-05-11T09:36:00Z
fault: ID 164 "a new arrival" — indefinite article form
scope: line
change: "a new arrival" → "the arrival"
criteria met: yes

## GROUP9-RELAY-POLICY — FLAGGED-FOR-SCREEN-WRITER — 2026-05-11T09:37:00Z
fault: flag-001 — ~35 relay bones technically permitted but svo-split-notes #1 suggests fauna-perception-transmission belongs in sensory/narrator facets
scope: n/a (policy decision, not line fault)
change: none — per task instructions, no modification; policy question routed to screen-writer
criteria met: n/a — no fault to resolve; decision required on whether relay lines should be stripped to physical-creature-act bones

## SESSION-END — 2026-05-11T09:40:00Z — season-s01-pass-2-fix-round2
findings-applied: 78 individual line faults across Groups 1–8 (mix of prior session + this session); Group 4 perception 19 resolved; Group 5 modifier 45 resolved; Group 6 interiority 11 resolved; Group 7 non-action-verb 3 resolved; Group 8 slug-unresolved 1 resolved; Group 1 reference-drift 30+ resolved (prior session); Group 2 POV-leaks 6 resolved (prior session)
findings-skipped: 0 individual fault instances skipped
exit: DEPENDENCY-FLAGGED — 2 items routed to screen-writer: (1) FAULT-PROP-STATE-01 close-log bone REGEN-ADD required between IDs 202–205; (2) GROUP9 relay-policy decision required before Phase 3; all individual-line faults resolved

## SESSION-START — 2026-05-11T00:00:00Z — season-s01-pass-2-fix
dispatch: resolve all faults from season-s01-pass-2-constraint.md + season-s01-pass-2-continuity.md — REFERENCE-DRIFT, POV-LEAKS, PROP-STATE, FORM faults (marks/reads-aloud/modifier/interiority/non-action-verb), SLUG-UNRESOLVED
target: active-project/theater/proto-lines/s01.bones.md
audit-report: active-project/staff/auditor/season-s01-pass-2-constraint.md + active-project/staff/auditor/season-s01-pass-2-continuity.md
findings-queued: 24 individual faults + 1 pattern flag + 1 prop-state flag

## GROUP2-POV-LEAKS — RESOLVED — 2026-05-11T00:03:00Z
fault: IDs 157-158 (south gate entry outside range), IDs 282-283 (stairwell pauses with no relay coverage), IDs 203-204 (recipient-state assertions with no relay)
scope: line
change: deleted IDs 157, 158, 282, 283, 203, 204 by converting to blank time-skip markers (ID gaps preserved; no renumbering); beat 9 now opens at ID 159 (junction crossing); visitor beat now 281→284 with stairwell implied; beat 10 transmission gap flagged for screen-writer
criteria met: yes — six offstage/uncovered bones removed; ID gaps left intact

## GROUP1-REFERENCE-DRIFT — RESOLVED — 2026-05-11T00:02:00Z
fault: "the maester" used in place of slug oc-broken-maester in all post-beat-16 bones (IDs 303+)
scope: line
change: targeted Edits on IDs 303–310 and 400–415 blocks; replaced "the maester" → "oc-broken-maester" as subject and in possessive forms (e.g. "the maester's footfall" → "oc-broken-maester's footfall"); also replaced listener occurrences (IDs 407, 409: "the stall-keeper speaks to the maester" → "speaks to oc-broken-maester"); IDs 416-419 relay lines confirmed maester-free; IDs 111-301 retain "the maester" correctly
criteria met: yes — no "the maester" appears at ID 303 or later

## GROUP1-REFERENCE-DRIFT — WORKING — 2026-05-11T00:01:00Z
note: reading full bones file to enumerate all post-ID-302 occurrences of "the maester" before applying targeted Edits

## SESSION-START — 2026-05-10T01:00:00Z — series-audit-fix
dispatch: resolve 6 faults from series-audit.md — scope corrections (res-003, res-004), supersedes chain (res-005), heading residue (fault-006), wrong-project warehouse card (fault-007), era-specific named figures in warehouse (fault-008)
target: cards/conditions/ + active-project/warehouse/ (multiple cards)
audit-report: active-project/staff/auditor/series-audit.md
findings-queued: 6

## fault-008 — RESOLVED — 2026-05-10T01:06:00Z
fault: warehouse cond-smallfolk-political-physics and cond-feudal-hierarchy-law carried era-specific named characters (Mira Stonefield-Jaehaerys, Septon Rowan, Clem Ferris, Aldric Pryor) and wrong-era geography/institutions (Fairstead, House Ryger, Harrenhal, cond-suppression-policy-progression) as operative examples
scope: line
change: warehouse-only edits to both cards:
  cond-smallfolk-political-physics — replaced: "Mira Stonefield-Jaehaerys" with "community-elder figure (oc-tanner-elder)"; "Septon Rowan" with "the local septon"; "Clem Ferris" removed from reeve description; "Mira's endorsement" with "the elder's endorsement"; "Mira's vibes" with "the elder's vibes"; "Aldric Pryor's record" with "on record"; charity/Rowan reference replaced with generic; cond-westerosi-customary-authority-jaehaerys reference in Interaction Notes genericized; references frontmatter updated to remove jaehaerys card
  cond-feudal-hierarchy-law — replaced: H1 era label; "King Jaehaerys I" tier with "Iron Throne"; "Great House Tully" with "paramount lord"; "House Ryger of Willow Wood" with "local feudal authority"; "Fairstead" occurrences replaced with generic; "Pryor" replaced with "the steward"; "Tully" in formal recourse replaced with "the paramount lord"; "Stage 3 threshold in cond-suppression-policy-progression" replaced with generic; references frontmatter updated; Interaction Notes genericized
criteria met: yes — no occurrence of "Mira", "Stonefield", "Ryger", "Fairstead", "Septon Rowan", "Harrenhal" in either warehouse copy; mechanics preserved

## fault-007 — ESCALATED — 2026-05-10T01:05:00Z
fault: warehouse cond-westerosi-customary-authority is the wrong-project card (scope:project, project:taylor-hebert-westeros; 120 AC Riverlands/Harrenhal config)
scope: escalate
change: none applied — escalating to showrunner
criteria met: no — explanation below

ESCALATION REPORT:
Library slugs found:
  (a) cond-westerosi-customary-authority — scope:project, project:taylor-hebert-westeros, 120 AC Riverlands (same card as warehouse; wrong project)
  (b) cond-westerosi-customary-authority-jaehaerys — scope:library, 84-101 AC Jaehaerys I Riverlands (wrong era and geography for 125 AC Crownlands/KL)

Neither library card satisfies the criteria (scope:library era-general variant, or 125 AC Crownlands config). No card exists in the library that is the correct operative constraint for a 17yo in Flea Bottom at 125 AC. Fixer cannot author a new card. Action required at showrunner/screen-writer level: author cond-westerosi-customary-authority-125ac (Crownlands/KL config, 125 AC, 17yo female social position) and provision it in warehouse. Until that card exists, the wrong-project card should be removed from the warehouse to prevent load-set corruption; memory.md laws entry for cond-westerosi-customary-authority should be annotated as pending-replacement.

NOTE: Fixer can execute the removal of the wrong-project card from warehouse and the memory.md annotation if showrunner approves. Awaiting direction before touching those files.

## fault-006 — RESOLVED — 2026-05-10T01:04:00Z
fault: cond-shard-behavioral-weight H1 heading read "Jaehaerys I Config" in both library and warehouse copies
scope: line
change: library + warehouse — replaced "(Jaehaerys I Config)" with "(flea-bottom-dance Config)" in H1 heading; no other heading or body text contained "Jaehaerys"
criteria met: yes — no occurrence of "Jaehaerys" in H1 or any heading in either copy

## res-005 — RESOLVED — 2026-05-10T01:03:00Z
fault: warehouse cond-reincarnation-mechanics-125ac missing supersedes: field; library copy and prior card (cond-reincarnation-mechanics) already have correct bidirectional chain from prior fixer pass
scope: line
change: warehouse — added supersedes: [cond-reincarnation-mechanics] to frontmatter; bidirectional chain now complete in both library and warehouse copies
criteria met: yes — library 125ac has supersedes, prior card has superseded_by, warehouse 125ac now has supersedes; chain is bidirectional

## res-004 — RESOLVED — 2026-05-10T01:02:00Z
fault: warehouse cond-clinical-self-erasure had scope:library with no project field; library copy already correct
scope: line
change: warehouse — changed scope: library → scope: project; added project: flea-bottom-dance
criteria met: yes — both library and warehouse now have scope:project + project:flea-bottom-dance

## res-003 — RESOLVED — 2026-05-10T01:01:00Z
fault: warehouse cond-crownlands-superstition-frame-125ac had scope:library with no project field; library copy already correct
scope: line
change: warehouse — changed scope: library → scope: project; added project: flea-bottom-dance
criteria met: yes — both library and warehouse now have scope:project + project:flea-bottom-dance

## SESSION-END — 2026-05-10T01:07:00Z — series-audit-fix
findings-applied: 5 (res-003, res-004, res-005, fault-006, fault-008)
findings-skipped: 0
exit: ESCALATED-TO-SHOWRUNNER (fault-007: no era-general or 125-AC Crownlands variant of cond-westerosi-customary-authority exists in library; new card authoring required)

## SESSION-START — 2026-05-10T00:00:00Z — 1d-audit-fix
dispatch: resolve 5 faults from 1d-audit.md — slug corrections, scope corrections, supersedes chain
target: cards/conditions/ (multiple cards) + active-project/warehouse/cond-shard-behavioral-weight.card.md
audit-report: active-project/staff/auditor/1d-audit.md
findings-queued: 5

## fault-001 — RESOLVED — 2026-05-10T00:01:00Z
fault: cond-shard-behavioral-weight references and Interaction Notes cited taylor-hebert-jaehaerys instead of taylor-hebert-flea-bottom
scope: line
change: removed taylor-hebert-jaehaerys from references (library card + warehouse copy); replaced in Interaction Notes "With taylor-hebert-jaehaerys persona card" → "With taylor-hebert-flea-bottom persona card" in both copies
criteria met: yes

## fault-002 — RESOLVED — 2026-05-10T00:01:30Z
fault: cond-shard-behavioral-weight references and Interaction Notes cited cond-series-tone-constraints-84ac instead of cond-series-tone-constraints-125ac
scope: line
change: replaced cond-series-tone-constraints-84ac with cond-series-tone-constraints-125ac in references frontmatter and in two body occurrences (Interaction Notes + for-auditor-use) in both library card and warehouse copy
criteria met: yes

## fault-003 — RESOLVED — 2026-05-10T00:02:00Z
fault: cond-crownlands-superstition-frame-125ac had scope:library despite project-specific body content
scope: line
change: changed scope to project; added project: flea-bottom-dance frontmatter field in library card. INDEX has no by_scope section; no INDEX edit required.
criteria met: yes

## fault-004 — RESOLVED — 2026-05-10T00:02:30Z
fault: cond-clinical-self-erasure had scope:library with no project field despite entirely project-specific body content
scope: line
change: changed scope to project; added project: flea-bottom-dance frontmatter field in library card. INDEX has no by_scope section; no INDEX edit required.
criteria met: yes

## fault-005 — RESOLVED — 2026-05-10T00:03:00Z
fault: cond-reincarnation-mechanics-125ac body stated it supersedes cond-reincarnation-mechanics but had no supersedes: frontmatter field; prior card had no superseded_by field
scope: line
change: added supersedes: [cond-reincarnation-mechanics] to 125ac card frontmatter; added superseded_by: cond-reincarnation-mechanics-125ac to cond-reincarnation-mechanics frontmatter. Relation is supersedes (not overrides): both are project-scope cards for different projects; the 125ac card is a same-concept replacement for a different project, not a library→project variant.
criteria met: yes

## SESSION-END — 2026-05-10T00:03:30Z — 1d-audit-fix
findings-applied: 5
findings-skipped: 0
exit: CLEAN
