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
