# Proto-lines directory

Two artifact families coexist here. Both are valid; their provenance differs.

## chapter-01.md through chapter-10.md (current)

Authored 2026-05-07 via the season-decomposition pipeline (`/and-season` semantics, run manually because schema/promotion prereqs not yet landed).

- Decomposition: 10 chapters, target 100±30 finished lines per chapter.
- Authoring: per-chapter screen-writer dispatches under the locked `svo-writer-pass1-brief.md` (with the non-action-verb deny-list and narrow `holds` license).
- Review: per-chapter Pass 2 (constraint audit) ran for all 10 chapters; fixer applied repairs with the **attention-preservation** discipline (fix-with-substance, not strip-to-bare).
- Status: **Pass-2 cleanup applied. Pass 3 (shape), Pass 4 (trim), Pass 5 (continuity) per-chapter NOT yet run on the chapter files.** Season-scope review S1–S9 also not yet run.

These are the **canonical proto-line files for the season-chapters decomposition** going forward. Facet-tuning sessions should consume these.

| File | Lines (approx post-fix) | Narrator | Notes |
|---|---|---|---|
| chapter-01.md | ~80 (after 47 fixes from 131) | taylor-hebert-westeros | The Name on the List — census logging |
| chapter-02.md | ~97 (4 fixes) | taylor-hebert-westeros | The First Circuit |
| chapter-03.md | 102 (re-authored with fauna-feed framing) | taylor-hebert-westeros | The Report Upstream |
| chapter-04.md | ~98 (7 fixes) | taylor-hebert-westeros | The Raven on Her Arm |
| chapter-05.md | 84 (extended from 67, 2 fixes) | septon-rowan | Rowan's Intercession (POV shift) |
| chapter-06.md | ~105 (4 fixes) | taylor-hebert-westeros | The Succession Clock |
| chapter-07.md | ~92 (5 fixes) | taylor-hebert-westeros | The Refusal Logged |
| chapter-08.md | ~95 (8 fixes) | taylor-hebert-westeros | The Maester's Report |
| chapter-09.md | 101 (1 fault defended, no change) | taylor-hebert-westeros | Two Claims, One File |
| chapter-10.md | ~50 (3 fixes) | taylor-hebert-westeros | Ward of the Administration (finale) |

**Known caveats:**
- Per-chapter pass 3/4/5 not yet run; some shape/trim/continuity issues may remain.
- Season-scope S1–S9 review not yet run; cross-chapter coherence is not yet validated.
- Some auditor-fixer interactions left residual modifier flags (e.g. ch01 `taylor-hebert-westeros follows to the yard`, `take position beside the official`).
- A second pass-2 against the post-fix files would surface any new faults the fixers introduced (ch10's transient `watches` was caught manually).

## s01e01.md through s01e06.md (legacy)

Authored 2026-05-06 as the rough-pass extraction of `active-project/theater/show.md` content into proto-line format (per `project_svo_extraction_v0.md` in auto-memory). Used as **facet-tuning training corpora** for the seven facet-tuning runs (location-state, dialogue, tensometer, narrator-interest, state-updates, memory-flags, sensory, feeling-flags).

These are **kept as-is** for backward compatibility with completed facet-tuning artifacts. New facet-tuning work should consume the chapter-*.md files instead.

## Provenance

- Pipeline architecture: `design/shoot-v2/svo-writer-tuning-package.md`, `design/shoot-v2/phase5-svo-writer-final.md`.
- Per-pass briefs: `design/shoot-v2/svo-writer-pass{1,2,3,4,5}-brief.md`.
- Decomposition: `design/shoot-v2/season-chapters-run/decomposition.md` and `chapter-NN-plan.md` ×10.
- Audit reports: `active-project/staff/auditor/ch{01..10}-pass2.md`.
- Fix logs: `active-project/staff/fixer/svo-chapter-fix-log.md`, `fixer-log.md`.
- Orchestration commands (drafted, not yet promoted): `.claude/commands/and-protolines-v2.md`, `and-protolines-season-v2.md`, `and-season.md`.
