# Finalize & export protocol

**Status:** live (authored 2026-06-07, first run: b01 taylor-westeros-good-intentions).
**Trigger phrases:** "finalize the book" / "export the book" / "single file for Google Docs" / "package the completed work" / "close out the project" / any phrasing meaning *take the shipped book and produce a reader-facing deliverable, then retire the project.*

This is the **session-close / book-close operation**, distinct from chapter-production (`RUNBOOK.md § Producing a chapter`) and from book-complete revisions (`RUNBOOK.md § Producing revisions`). It runs **after** a book is verdict-passed and produces a polished, trimmed, reader-facing single file, saves it to the cross-project `completed-works/` library, then archives the active project and harvests its new artifacts back into the shared libraries.

It is the practical un-defer of the polish layer (`/and-wrap`, deferred under the substance overhaul) — but scoped narrowly: **it polishes a derived export copy, it does NOT re-cascade the bones chain.** Canonical `active-project/draft/` + `theater/` remain the source of truth.

---

## Preconditions (hard-gate before starting)

1. The target book is **complete**: every planned chapter shipped through `/and-stitch` Phase 9, and `/and-review verdict b<NN>` has issued (PASS / PASS-WITH-NOTES). If not complete → this is not the right protocol; route to chapter-production or revisions.
2. A current **consolidated manuscript** exists at `active-project/draft/b<NN>-manuscript.md` and matches the per-chapter drafts (verify chapter count + tail). If stale or absent, rebuild it first (concatenate `b<NN>-c01.md … b<NN>-cMM.md` with chapter dividers).
3. Disposition on the four export questions is settled (route to **admin user-proxy** per CLAUDE.md Rule 13; see Phase 0). Defaults below.

---

## The four dispositions (admin user-proxy; Rule 13)

Before running, dispatch admin (`subagent_type: admin`, `mode: user-proxy`) with these four. Honor the answer; ESCALATE only what genuinely needs the human. Established defaults (DEC-0114):

| # | Question | Default |
|---|----------|---------|
| 1 | **Trim aggressiveness** | MODERATE, voice-preserving. Cut true redundancy + drag the cold-readers independently flag. NEVER flatten the signature voice. Design-inherent density (logged as accepted Class-B / DEC-origin) is OFF-LIMITS. |
| 2 | **Editing mechanism** | `editor` agent on the **export copy only**. No `/and-write revise` re-cascade (that would be ~30-40 dispatches/chapter and displace `theater/` state). Canonical `draft/` + bones stay source of truth; the export is allowed to diverge from bones. |
| 3 | **Completed-works dir** | `completed-works/<project-slug>/`. |
| 4 | **Export format** | Markdown (`# book` / `## Chapter N` / `*italic*` preambles) tuned for Google Docs paste-from-Markdown, plus a `.txt` plain fallback. `.docx` only if explicitly required (needs pandoc install). |

**Trim concurrence rule (DEC-0114 / DEC-0058 ceiling):** the editor trims only what the cold-read evidence corroborates — a CUT entry, a TIGHTEN with a stated reader-fatigue reason, or a repetition the fork documented with a recurrence count. A lone speculative FLAG is advisory, not a mandate. The editor's own hollow-prose scan still applies. When in doubt, keep the line.

---

## Phases

### Phase 0 — orient & gate
- Verify preconditions (above). Verify manuscript == per-chapter concatenation (chapter count + tail line).
- Dispatch admin for the four dispositions. Queue any ESCALATE to the end-of-run summary; proceed on defaults.
- Create working dir `active-project/staff/finalize/` and `active-project/polish/`.

### Phase 1 — cold-read (parallel forks)
- Split the book into act-batches (~5 chapters each for a 20-chapter book). One **naive cold-reader fork** (`general-purpose`) per batch.
- Each fork reads ONLY its chapter range of the manuscript, knows nothing of production history, and flags drag: airless-without-anchor stretches, restatement, over-repeated motifs/images. Each entry carries CHAPTER + verbatim ANCHOR (5–12 words) + SEVERITY (CUT / TIGHTEN / FLAG) + WHY + a concrete TRIM instruction (deletions/compressions only — never a voice rewrite). Plus a per-batch REPETITION section with recurrence counts.
- Brief each fork on the signature voice so it does not mis-flag intentional coldness/density.
- Output: `active-project/staff/finalize/coldread-c<aa>-c<bb>.md` per batch.

### Phase 2 — editor trim pass (parallel forks, one per batch)
- Dispatch the `editor` agent per act-batch. Input: the batch's chapters (from the manuscript) + that batch's cold-read findings + the trim philosophy (MODERATE, voice-preserving, concurrence rule).
- Editor applies CUT + corroborated TIGHTEN + repetition-thinning + its own hollow-prose scan. **Adds no content. Makes no plot decisions. Preserves the cold ledger voice and all design-inherent density.** Preserves chapter dividers and the italic interior-monologue preambles.
- Output: polished chapters to `active-project/polish/b<NN>-c<aa>-c<bb>.polished.md` (one file per batch).
- **Rule 19:** existence-check every editor output path on disk before consuming. **Rule 20:** the editor writes only its own polish files (not shared state), so read-back is light — but spot-check that the trim respected the voice and didn't drop story beats.

### Phase 3 — assemble & format
- Concatenate the polished batches into one file in chapter order. Normalize to the export format: a `# <book>` title line, `## Chapter N` headings (no chapter titles — the project fences titles; slugs/numbers only), italic preambles preserved, scene breaks as a centered divider or blank-line gap, all annotation artifacts stripped (`[SCENE_*]`, `[NEEDS_EDIT]`, `[AUDIENCE]`, `--scene--` headers, `═══` callouts → clean `## Chapter N`).
- Produce a `.txt` plain variant (headings as plain lines, italics dropped or rendered as plain text).
- Sanity pass: word-count delta vs. the pre-trim manuscript (expect a single-digit-to-low-teens % reduction under MODERATE), chapter count intact, no stray markers, no dropped chapters.

### Phase 4 — save to completed-works
- Write the export + .txt + a short **colophon/README** to `completed-works/<project-slug>/`. The colophon names: title/brief, chapter count, final word count (and pre-trim count), the trim disposition used, the source commit, and a one-line provenance note (where the canonical drafts live in the archive). Do NOT include internal model identifiers.

### Phase 5 — archive the project
- Move `active-project/` to `projects/<project-slug>/` (git mv — recoverable). Write an `ARCHIVE_NOTE.md` at the archive root: completion state, verdict, accepted caveats, location of the export, date.
- `active-project/` is now empty/retired; a future `/and-project` activates the next one.

### Phase 6 — harvest new artifacts (margit)
- Dispatch **margit** to promote project-local artifacts that are new or newer than the shared libraries:
  - **Personas** (highest priority): each `active-project/actors/<slug>/` whose card is new or has diverged from `cards/personas/<slug>.card.md` → validate against `schemas/card.schema.md` and promote (preserving pre-mutation per margit's preservation rule). Same for **persona-exemplars** → `cards/persona-exemplars/`.
  - Locations / props / conditions / behaviors that were authored or revised in-project and don't exist in the shared `cards/` library.
  - Audience persona refinements, voice-exemplar, any reusable staff artifact.
- Margit indexes promotions in the relevant `INDEX.md`. Nothing is destructively overwritten; both pre- and post-mutation are kept.
- **Rule 19/20:** verify each promoted card exists on disk after margit returns; read-back INDEX edits before committing.

### Phase 7 — commit & summary
- Commit the export, the `completed-works/` entry, the archive move, and the harvested cards on the working branch. Push.
- Emit a single end-of-run summary: export path + word counts, trim stats (CUT/TIGHTEN applied per batch), archive location, personas/cards harvested, any queued admin ESCALATE, next-step.

---

## What NOT to do

- Do NOT re-cascade the bones chain for export-level prose edits (Q2 default; ~600 dispatches; methodology §human-only spend).
- Do NOT hand-edit the canonical `active-project/draft/b<NN>-c<MM>.md` files — the editor works on the export copy in `polish/`. The canonical drafts are frozen as the archived source of truth.
- Do NOT flatten the signature voice or trim design-inherent density that prior DECs accepted as contract-origin.
- Do NOT delete the active project — **archive** it (git mv to `projects/`). Everything is recoverable.
- Do NOT destructively overwrite library cards during harvest — margit preserves pre- and post-mutation both.
- Do NOT invent trims a cold-reader did not flag; do NOT bundle a fresh creative rewrite into a trim pass.
