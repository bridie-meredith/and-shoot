# improvement-loop/test — lens rotation ledger

Tracks which test lens ran each pass so lenses rotate fairly across sessions.

## Rotation order

```
a. /and-review pipeline    — schema vs command-body vs rubric tri-walk (cross-file drift)
b. /and-review consistency — or /and-review tree on a recent chapter or the and-experiment spine
c. /and-ablate             — facet-ablation on a shipped chapter (facet-value evidence)
d. auditor fork            — targeted auditor fork on the most-recently-changed artifact
```

After (d), cycle back to (a).

---

## Passes

### Pass 1 — 2026-06-12 — Lens (a): /and-review pipeline

**Report:** `active-project/staff/reviews/pipeline-2026-06-12T090611Z.md`

**Verdict:** 1 HARD · 8 SIGNAL · 3 TASTE-FLAG

**Headline finding (HARD):**
- **STRUCT-001** — `schemas/dialogue.schema.md:3` claims the R2 dialogue judge "remains as a locked-graph review pass." This directly contradicts DEC-0116, which retired the entire R2 round. Any agent dispatched with this schema as authority would believe an R2 locked-graph judging pass still runs at `/and-facets`.

**Key SIGNAL findings:**
- **STRUCT-008** — `staff/dialogue-writer/rubric-dialogue.md` describes R2 authoring, V2 audience-gate (Phase 5b), and R2 decision-shard emission in active-voice present tense. Rubric is loaded by `/and-write` Phase 1.5.
- **STRUCT-009** — `staff/exposition-author/rubric-exposition.md` describes R2 graph-aware authoring, Phase 5b audience-gate, and a `tensometer.md` reference — all retired under DEC-0116 / URI-SUBSTANCE-OVERHAUL. Rubric is loaded by `/and-facets` Phase 1.
- **STRUCT-007** — `/and-facets.md` Phase 4 RUBRIC-FIDELITY enumeration uses bare names; `rubric-exposition.md` and `rubric-dialogue.md` live at non-standard paths (`staff/exposition-author/` and `staff/dialogue-writer/`) vs. `design/shoot-v2/` for the other eight. Auditor dispatched for Phase 4 resolving bare names to `design/shoot-v2/` fails to load these two rubrics.
- **STRUCT-002/003/RESIDUE-001** — `schemas/audit-report.schema.md` R2 decision-shard section (lines 106–157) is unmarked as retired; carries `/and-season` reference; `/and-facets.md` Phase 4 audit output format diverges from schema.
- **STRUCT-004/005/006** — CLAUDE.md sync gaps: `/and-cohere` absent from Commands table; `schemas/aggregate-state.schema.md` absent from schema authority table; `active-project/staff/cite-index/` absent from directory map.

**Findings filed as parking-lot items:**
- `pl-2026-06-12-pipeline-001` (HARD) → fix `schemas/dialogue.schema.md:3` before next `/and-facets`
- `pl-2026-06-12-pipeline-002` (SOFT) → mark R2 sections retired in `staff/dialogue-writer/rubric-dialogue.md`
- `pl-2026-06-12-pipeline-003` (SOFT) → mark R2 sections retired in `staff/exposition-author/rubric-exposition.md`
- `pl-2026-06-12-pipeline-004` (SOFT) → add explicit paths for `rubric-exposition.md` + `rubric-dialogue.md` in `/and-facets.md` Phase 4 RUBRIC-FIDELITY
- `pl-2026-06-12-pipeline-005` (SOFT) → retire R2 decision-shard section in `schemas/audit-report.schema.md`
- `pl-2026-06-12-pipeline-006` (SOFT) → CLAUDE.md sync: add `/and-cohere`, `aggregate-state.schema.md`, `cite-index/`

**Next lens:** (b) `/and-review consistency` or `/and-review tree` on a recent chapter
