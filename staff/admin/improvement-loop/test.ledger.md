# improvement-loop / test — ledger

Tracks which structural test lens ran each pass, the headline verdict,
findings filed, and what lens is next in rotation.

Lens rotation:
  a. /and-review pipeline  — schema ↔ command-body ↔ rubric tri-walk
  b. /and-review consistency or /and-review tree on a recent chapter
  c. /and-ablate on a shipped chapter
  d. Targeted auditor fork on the most-recently-changed artifact

---

## Pass 1 — 2026-06-12

**Lens:** (a) `/and-review pipeline`

**Context:** First pass; no prior ledger. Two major command-body changes since
the last manual pipeline tri-walk (2026-06-07): DEC-0116 (slim /and-facets —
retired R2 round + Phase 5b audience-gate) and DEC-0115 (no-ledger overhaul —
retired apparatus-register as a prose mode, added ABSTRACTION-AS-SUBJECT +
SCENE-ABSTRACT-DOMINANT + LEDGER-REGISTER + EMBODIMENT-BLOCKED + NAIVE-FOLLOW
fault classes). Book 2 (and-experiment) completed since last audit.
All five prior HARD findings confirmed fixed before running this pass.

**Verdict:** 1 HARD + 8 SIGNAL faults found

**HARD finding:**
- STRUCT-031: `schemas/audit-report.schema.md` §"R2 decision-shard frontmatter"
  still describes an active contract for the retired R2 emission system
  (shard files + orchestrator-critic f-r2-counts consumer contract) with no
  retirement notice. Most critical finding: any fork reading this schema will
  attempt to emit files that nothing reads, and the orchestrator-critic consumer
  contract references metrics never populated post-DEC-0116.
  → pl-2026-06-12-pipeline-001

**Key SIGNAL findings:**
- STRUCT-032: CLAUDE.md Rule 17 says `ABSTRACTION-DOMINANT (SIGNAL)` but Rule 22
  says `SCENE-ABSTRACT-DOMINANT (HARD)` — same-document Rule 17 vs Rule 22
  contradiction introduced by DEC-0115 not updating Rule 17.
  → pl-2026-06-12-pipeline-002
- STRUCT-025/026/027: DEC-0115 fault classes not in schemas — bones.schema.md
  missing ABSTRACTION-AS-SUBJECT + SCENE-ABSTRACT-DOMINANT + 0.6 floor;
  stitch-render-log.schema.md Phase 4 missing LEDGER-REGISTER + EMBODIMENT-BLOCKED;
  no Phase 9 section at all in the schema.
  → pl-2026-06-12-pipeline-003
- STRUCT-033/034/035: DEC-0116 residue — three rubrics (feeling, memory-flags,
  narrator-interest) still prescribe retired dialect-audience gate as mandatory;
  facet.schema.md still documents retired interest-aud facet type; audience.md
  frontmatter inconsistency.
  → pl-2026-06-12-pipeline-004
- STRUCT-028/029 + RESIDUE-002: CLAUDE.md housekeeping — /and-reoutline missing
  from commands table; cohere-state + aggregate-state schemas still absent from
  authority table (third unresolved pass); rubric-sensory AP#14 stale vocabulary.
  → pl-2026-06-12-pipeline-005

**Report:** `active-project/staff/reviews/pipeline-20260612T101408Z.md`

**Parking-lot items filed:** pl-2026-06-12-pipeline-001 through pl-2026-06-12-pipeline-005
(all SOFT — none block forward chapter production)

**All prior HARDs resolved:** STRUCT-006/007/017/018/019 (from 2026-06-07 runs)

**Next lens in rotation:** (b) `/and-review consistency` or `/and-review tree`
on a recent chapter or the and-experiment spine (Book 2 is newly complete — a
cross-chapter consistency sweep across the Book 2 or and-experiment arc is the
natural follow-up).
