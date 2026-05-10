# Fixer Fix Log — Season s01 Pass S3 Trim
# session: 2026-05-09
# target: active-project/theater/proto-lines/s01.aggregate.md

---

## SESSION-START — 2026-05-09T14:00:00Z — phase3-S3-trim
dispatch: fixer round 11 — Phase 3 S3 trim deletions (all 3 personas REVISE)
target: active-project/theater/proto-lines/s01.aggregate.md
audit-reports:
  - active-project/staff/auditor/season-s01-pass-S3-trim-pulp-enthusiast.md
  - active-project/staff/auditor/season-s01-pass-S3-trim-dark-fantasy-reader.md
  - active-project/staff/auditor/season-s01-pass-S3-trim-worm-canon-pedant.md
findings-queued: tbd (intersect candidate lists per ≥2-persona threshold)
note: pulp ~38 candidates + flatlines 21-60/83-135; worm 6 specific candidates + 15.8% TOLERATED; dark-fantasy 15 candidates + 1 BORED W05 (55-68) + flatlines 83-123/645-699. Convergent: line 123 fauna constraint, early-baseline thinning, post-witness-inquiry stretch.

---

## Intersect Table (pre-deletion)

Threshold rules applied in order:
1. ≥2-persona flag → DELETE (unless voice-load-bearing exception from any persona)
2. BORED W05 override (lines 55-68): any 1-persona deletion candidate → DELETE
3. Flatline-aggressive range (21-135): any 1-persona deletion candidate not voice-load-bearing or structural anchor → DELETE
4. Flatline-aggressive range (645-699): any 1-persona deletion candidate not voice-load-bearing or structural anchor → DELETE (dark-fantasy flagged W40-W42)
5. Inserts 916-933: protected unless ≥2 personas explicitly flagged specific insert

Dark-fantasy explicitly retained lines 73-78, 123, 193-194, 246-247, 144, 148-149, 904-906 as voice-load-bearing or season-goal adjacent.
Worm explicitly retained lines 11-13, 27-28, 68-71 (partial), 78, 93, 159/193/194/247 (partial).

---

## Deletion Log

### ≥2-Persona Deletes (8 IDs)
- 36: DELETED — father removes cap; pulp + dark-fantasy
- 47: DELETED — mother approaches mordant station; pulp + dark-fantasy
- 58: DELETED — Taylor takes bowl; pulp + dark-fantasy
- 59: DELETED — mother fills bowl; pulp + dark-fantasy
- 92: DELETED — Taylor wipes vat rim; pulp + dark-fantasy
- 104: DELETED — mother faces table; pulp + dark-fantasy
- 116: DELETED — mother pours water cup; pulp + dark-fantasy
- 117: DELETED — mother sets cup; pulp + dark-fantasy

### BORED W05 Override Deletes (5 IDs, lines 55–68)
- 55: DELETED — Taylor rises; dark-fantasy BORED W05
- 56: DELETED — Taylor speaks to mother; dark-fantasy BORED W05
- 57: DELETED — mother speaks to Taylor; dark-fantasy BORED W05
- 63: DELETED — Taylor climbs loft ladder; dark-fantasy BORED W05
- 65: DELETED — Taylor reaches loft floor; dark-fantasy BORED W05

### Flatline 21–135 Aggressive Deletes (9 IDs, 1-persona, not voice-load-bearing)
- 33: DELETED — mother faces doorway; dark-fantasy solo
- 48: DELETED — father draws stool; dark-fantasy solo
- 76: DELETED — Taylor exhales; pulp solo (redundant with 75 stills)
- 83: DELETED — mother approaches basin; dark-fantasy solo
- 88: DELETED — father takes market satchel; dark-fantasy solo
- 89: DELETED — father exits workshop; dark-fantasy solo
- 91: DELETED — Taylor takes cloth-strip; dark-fantasy solo
- 102: DELETED — father enters workshop; dark-fantasy solo
- 103: DELETED — father sets satchel; dark-fantasy solo

### Flatline 645–699 Aggressive Deletes (2 IDs, 1-persona, not voice-load-bearing)
- 651: DELETED — Rymer holds feet; pulp solo (repeat of 648–649)
- 675: DELETED — workshop door closes; pulp solo (redundant with 674 mother exits)

### SKIP — SOLO-PERSONA (outside flatline/BORED ranges)
28, 71, 173, 178, 191, 194, 247, 264, 294, 326, 334, 342, 390, 440, 478, 483, 526, 537, 593, 635, 709, 740, 793, 799, 803, 814, 815, 819, 821, 914

### SKIP — VOICE-LOAD-BEARING EXCEPTION
- 84: pulp explicit retain ("both needed to establish household rhythm")
- 85: pulp explicit retain (paired with 84)
- 123: dark-fantasy explicit retain (POV anchor; "swallow beats function as POV anchors"; overrides pulp+worm deletion flags)
- 247: dark-fantasy explicit retain (in "Lines Not Deletion Candidates")

---

## Constraint Fault — Line 123
Read cond-fauna-control-rules.card.md. Species scope includes "any bird without complex social cognition (sparrows, pigeons, starlings)" — swallows are in scope. Line 123 depicts the dye-yard swallow touching a gutter (environmental behavior, no implication of Taylor directing or sensing through it). No constraint violation. Pulp's "ecological inconsistency" tag is incorrect against the card. Dark-fantasy explicit retain applies. ID 123: SKIP-VOICE-LOAD-BEARING.

---

## Dependency Check
No deletions create reference orphans. All deleted lines are blocking/procedural with no IDs that other lines reference by number. Inserted bones 916–933 untouched (no persona flagged any insert as deletion candidate). Stable-ID rule maintained: deleted IDs are removed entirely (not blanked), per deletion-removes-ID-line-entirely protocol.

---

## SESSION-END — 2026-05-09T14:30:00Z — phase3-S3-trim
deletions-applied: 24 (8 intersect + 5 BORED-W05 + 9 flatline-21-135 + 2 flatline-645-699)
skipped-solo-persona: 30 IDs (outside flatline/BORED ranges)
skipped-voice-load-bearing: 4 IDs (84, 85, 123, 247)
constraint-fault-123: SKIP — no species scope violation per card; dark-fantasy explicit retain
inserted-bones-916-933: all protected — no persona flagged any
dependency-conflicts: 0
exit: CLEAN
