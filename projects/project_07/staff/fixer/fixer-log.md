# Fixer Log — active-project/mirror-tragedy

## SESSION-START — 2026-05-17T00:00:00Z — 1d-hard-findings
dispatch: Fix 5 HARD findings from Phase 1d constraint-consistency audit of condition card set
target: active-project/warehouse/ (condition cards)
audit-report: active-project/staff/auditor/1d-audit.md
findings-queued: 5 (finding-002, finding-003, finding-004, finding-005, finding-015)

## finding-002: RESOLVED — 2026-05-17T00:01:00Z
fault: cond-feudal-hierarchy-law references cond-westerosi-customary-authority-jaehaerys and cond-suppression-policy-progression — both absent from warehouse
scope: line
change: removed both dangling slugs from references: frontmatter; annotated three body-text cross-references to those cards as Riverlands-only companions not stocked in this project, redirecting to cond-kl-feudal-physics-mirror; rewrote Interaction Notes entry for cond-westerosi-customary-authority-jaehaerys to point to cond-kl-feudal-physics-mirror instead
files: active-project/warehouse/cond-feudal-hierarchy-law.card.md
criteria met: yes

## SESSION-START — 2026-05-17T10:00:00Z — 1d-hard-findings-continuation
dispatch: Continue fixing remaining 4 HARD findings (003, 004, 005, 015) from Phase 1d audit; finding-002 was resolved in prior session
target: active-project/warehouse/ (condition cards)
audit-report: active-project/staff/auditor/1d-audit.md
findings-queued: 4 (finding-003, finding-004, finding-005, finding-015)

## finding-003 — RESOLVED — 2026-05-17T10:01:00Z
fault: cond-smallfolk-political-physics references cond-westerosi-customary-authority-jaehaerys (dangling) and Interaction Notes carried Riverlands named characters without KL-project redirect
scope: line
change: already resolved — frontmatter references: already lacks the dangling slug; Interaction Notes already carry KL project note directing to cond-flea-bottom-social-physics as primary smallfolk-physics card and reframing named characters as Riverlands-specific illustrative examples not in KL cast
files: active-project/warehouse/cond-smallfolk-political-physics.card.md
criteria met: yes

## finding-004 — RESOLVED — 2026-05-17T10:02:00Z
fault: cond-kl-witch-label-formation lists superseded cards (cond-westerosi-superstition-frame, cond-crownlands-superstition-frame-125ac) in references: instead of using supersedes: frontmatter field
scope: line
change: removed cond-westerosi-superstition-frame and cond-crownlands-superstition-frame-125ac from references: frontmatter; added supersedes: [cond-westerosi-superstition-frame, cond-crownlands-superstition-frame-125ac] to frontmatter
files: active-project/warehouse/cond-kl-witch-label-formation.card.md
criteria met: yes

## finding-005 — RESOLVED — 2026-05-17T10:03:00Z
fault: cond-shard-deposit-mechanics-mirror (a) references cond-no-parahuman-infrastructure which is not stocked in the warehouse; (b) body text declares supersession of cond-reincarnation-mechanics-125ac without supersedes: frontmatter field
scope: line
change: (a) removed cond-no-parahuman-infrastructure from references: frontmatter; reframed Interaction Notes entry to note the constraint is covered inline in this card (world-notes.md no-parahuman-infrastructure content is verbatim in the What Did Not Carry Over and No Other Worm-Universe Entities sections); (b) added supersedes: [cond-reincarnation-mechanics-125ac] to frontmatter
files: active-project/warehouse/cond-shard-deposit-mechanics-mirror.card.md
criteria met: yes

## finding-015 — RESOLVED — 2026-05-17T10:04:00Z
fault: cond-feudal-hierarchy-law Riverlands 84-101 AC content in auditor-use guidance is a live drift surface for KL 125 AC project — agents could apply Tully/Ryger institutional framework to KL enforcement-threat assessments
scope: line
change: added KL-project auditor note to the For auditor use section, explicitly scoping this card to Riverlands 84-101 AC, naming cond-kl-feudal-physics-mirror as the operative card for KL enforcement-threat assessments, and stating that Tully/Ryger/Riverlands apparatus references in this card are inoperative in KL. The Interaction Notes already carried the KL-redirect; this change closes the gap in the auditor-use guidance specifically.
files: active-project/warehouse/cond-feudal-hierarchy-law.card.md
criteria met: yes

## SESSION-END — 2026-05-17T10:05:00Z — 1d-hard-findings-continuation
findings-applied: 4 (finding-003, finding-004, finding-005, finding-015); finding-002 was applied in prior session
findings-skipped: 0
exit: CLEAN
