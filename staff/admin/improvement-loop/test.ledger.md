# Improvement-Loop / Test Ledger

Tracks the rotating lens schedule for the TEST routine. One lens per pass; rotate in order
(a → b → c → d → a…). Each entry records what ran, headline verdict, findings filed, and
the next lens in rotation.

Lens rotation order:
  (a) /and-review pipeline — schema vs command-body vs rubric tri-walk
  (b) /and-review consistency or /and-review tree on a recent chapter or the and-experiment spine
  (c) /and-ablate on a shipped chapter (evidence for which facets earn their place)
  (d) targeted auditor fork on the most-recently-changed artifact (constraint/state/drift check)

---

## Pass 1 — 2026-06-11

**Lens:** (a) `/and-review pipeline`
**Run timestamp:** 2026-06-11T19:06:38Z
**Report:** `active-project/staff/reviews/pipeline-2026-06-11T19-06-38Z.md`

**Verdict:** FAIL
**HARD count:** 3 | **SIGNAL count:** 12 | **TASTE-FLAG count:** 1

**HARD findings:**
- RESIDUE-001: `URI-026` in `schemas/audit-report.schema.md` line 107 (R2 decision-shard header)
- RESIDUE-002: `URI-026` in `schemas/bones.schema.md` line 150 (authoring rules)
- RESIDUE-003: `` `tens:` `` token in `.claude/commands/and-write.md` Notes line 503

**Top SIGNAL findings:**
- STRUCT-001: R2 decision-shard section in `audit-report.schema.md` not marked deprecated (DEC-0116 retired it)
- STRUCT-002: `dialogue.schema.md` line 3 says R2 judge "remains" — contradicts DEC-0116 and current command body
- STRUCT-010/011: `rubric-dialogue.md` + `rubric-exposition.md` named in `/and-facets` Phase 4 RUBRIC-FIDELITY source-enumeration but not confirmed on disk
- STRUCT-012: `schemas/aggregate-state.schema.md` missing from CLAUDE.md schema authority table
- STRUCT-006/007/008/009: "open V3 rubric work for tensometer" parenthetical in three rubric files (stale post-retirement)

**Parking-lot items filed:**
- pl-2026-06-11-pipeline-001 (SOFT → `/and-review pipeline`): URI-026 in 2 active schemas (RESIDUE-001/002)
- pl-2026-06-11-pipeline-002 (SOFT → `/and-review pipeline`): `tens:` token in and-write.md (RESIDUE-003)
- pl-2026-06-11-pipeline-003 (SOFT → `/and-review pipeline`): R2 mechanics undeprecated in 2 schemas (STRUCT-001/002)
- pl-2026-06-11-pipeline-004 (SOFT → `/and-review pipeline`): missing rubric files in Phase 4 enumeration (STRUCT-010/011)
- pl-2026-06-11-pipeline-005 (SOFT → `/and-review pipeline`): aggregate-state.schema.md missing from CLAUDE.md (STRUCT-012)

**Open parking-lot items surfaced (pre-existing, SOFT, targeted at this run):**
- pl-2026-05-25-018: post-move axes-held listing schema ambiguity — NOT resolved this pass (adjudication deferred to dedicated schema-edit session)
- pl-2026-05-31-009: cross-chapter aliveness scoring question — NOT resolved this pass (process-design question, surfaced for principal)
- pl-2026-06-01-002: sensory old-state-anchor lineage check — NOT resolved this pass (rubric promotion deferred to fixer)

**Next lens in rotation:** (b) `/and-review consistency` or `/and-review tree` on a recent chapter
  (suggested target: `/and-review tree b01` or `/and-review consistency b01c20` — the most recently shipped chapter)
