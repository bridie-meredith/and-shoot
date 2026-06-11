# improvement-loop/test — lens rotation ledger

Records each test pass: which lens ran, headline verdict, findings filed, next lens in rotation.
Append-only. One entry per run.

Lens rotation order:
  a. /and-review pipeline        — schema vs command-body vs rubric tri-walk
  b. /and-review consistency     — cross-level / cross-chapter sweep on recent chapter or spine
  c. /and-ablate <chapter>       — facet ablation study on a shipped chapter
  d. auditor fork on most-recently-changed artifact — targeted constraint/state/drift check

---

## Run 001 — 2026-06-11T21:11:19Z

**Lens:** (a) `/and-review pipeline` — schema vs command-body vs rubric tri-walk

**Scope:** Targeted at post-June-7 changes (DEC-0115 no-ledger overhaul + DEC-0116 facets slim)
plus status check on prior HARD findings (STRUCT-017 through STRUCT-026 from pipeline-legs23).

**Report:** `active-project/staff/reviews/pipeline-20260611T211119Z.md`

**Headline verdict:** FAIL-WITH-HARD

**Prior findings resolved:**
- STRUCT-017/018/019/026 (tensometer vocabulary in rubric-metaphor.md + rubric-vibes.md): RESOLVED
- STRUCT-025 (missing rubric-exposition.md): DISPOSITIONED via DEC-0111 de-reference + b02 deferral

**New findings filed:**
- `pl-2026-06-11-001` (HARD) — STRUCT-031: CLAUDE.md Rule 22 circuit-breaker (N=2 consecutive
  design-inherent dispositions → auto-promote) declared but not implemented in any schema field or
  command body. PROP-0048 reference in and-stitch.md Phase 9 line 886 is dangling.
  Owner: and-stitch.md Phase 9 Step 4 + schemas/showrunner-memory.schema.md
- `pl-2026-06-11-002` (SOFT) — STRUCT-032: CLAUDE.md Rule 22 requires signatures to declare a
  readability/concreteness floor. Partially resolved: PROP-0050 (commit d3e288b, same branch)
  already wired the field into the schema + and-substance.md Phase 4c gate. Remaining gap:
  /and-review signature has no matching check for pre-PROP-0050 signatures. Owner: and-review.md.

**No fixes applied.** Findings route to the owning agents; fixes belong to a separate session.

**Next lens in rotation:** (b) `/and-review consistency` on a recent chapter range or the
b01 and-experiment spine (consider b01 c16-c20 as the freshest unreviewed range).
