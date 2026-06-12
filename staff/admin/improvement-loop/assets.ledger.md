# Improvement-Loop Assets Ledger

Owner: oskar (studio/foreman). Updated after each improvement-loop pass.

---

## Pass log

### 2026-06-11 — Pass 1

**Asset changed:** `cards/persona-exemplars/literary-snob.md` (new file) + `cards/persona-exemplars/INDEX.md` (row + coverage note updated)

**Change:** Authored the literary-snob persona-exemplar (~270 words, contemporary litfic bereavement-workshop scene). Added index row + coverage note update.

**Why top-ranked:**
- Rule 16 Tier-1 gap: audience personas are required to have exemplars; `/and-project Phase 1c` blocks on missing audience exemplars.
- `literary-snob` is one of three active audience personas in and-experiment; it had a full-quality card but zero exemplar.
- The two other uncovered and-experiment audience personas (`danmachi-reader`, `youjo-senki-reader`) are `quality: scant` — their cards need expansion before an exemplar can be grounded. Two-step work.
- `literary-snob` was one step: card rich enough to identify three load-bearing features (pause cadence, theme-hunting noticing, hot-button firing forms); exemplar authored directly from card. Highest improvement-to-cost ratio in the survey.

**Next candidate:** Expand `danmachi-reader` card from scant to full (isekai/progression-fantasy trope reader — voice section, hot_buttons, fatigue behavior), then author its exemplar. `youjo-senki-reader` follows the same two-step path. Both are Tier-1 audience gaps for the and-experiment project.

---

### 2026-06-11 — Pass 2

**Asset changed:** `staff/dialogue-writer/rubric-dialogue.md`

**Change:** Added a `CURRENT STATUS` preamble block immediately after the authority line. The preamble (a) updates the authority line to name "R1 dialogue-writer" only (removing the stale "R1 + R2" claim), (b) enumerates live vs retired sections by name, (c) names the dispatch-point change (dialogue now authored at `/and-write` Phase 1.5, not `/and-facets`), and (d) hard-prohibits `[DEFERRED-TO-R2]` placeholders — both `card-signatures:` and `facet-licenses:` must be fully populated at R1 submit. No body content removed; dead sections preserved for reference.

**Why top-ranked (among non-persona assets):**
The dialogue-writer is dispatched live at `/and-write` Phase 1.5 and loads this rubric as its primary discipline. The authority line still claimed "R1 + R2" and three large sections described the R2 graph-aware pass and Phase 5b audience-gate — both retired under DEC-0116 + URI-WRITE-DIALOGUE-COBONDED. A dispatched writer reading the rubric blind would infer a downstream R2 completion pass exists and produce `[DEFERRED-TO-R2]` placeholder citations. The `/and-facets` Phase 4 auditor then flags these as HARD (CONSTRAINT § citation-completeness) with no recovery path — a systematic HARD on every chapter's facet audit. Cost of fix: one insertion. Value: eliminates a systematic HARD finding from every future chapter run.

**Next candidate:** `rubric-dialogue.md` body — the three retired sections (`## Contamination disciplines`, `## V2 reviewer protocol`, `## R1 vs R2 differences`) still contain detailed dead workflow text. A follow-on pass could add `[RETIRED — DEC-0116]` headers to each section and update `## Files` to remove R2 artifact paths. Deferred because the new preamble already prevents execution of the dead paths.

---

### 2026-06-12 — Pass 3

**Asset changed:** `schemas/bones.schema.md` — Body format example

**Change:** Replaced the truncated Body format example (showed only `narrator:` + `goal:` — 2 of 7 required header fields; stale slugs `taylor-hebert-westeros` / `septon-dying-protector`) with a complete canonical file example. New example shows all seven header fields, generic non-stale slugs, a time-skip marker (bare flat_id), a citation-bearing licensed-action dialogue anchor, and the canonical `<speaker> speaks to <listener>` speech form. Added a one-paragraph explanation of the three illustrated bone forms below the code block.

**Why top-ranked:**
- The schema is the authoritative reference for `/and-write` Phase 7 emission and `/and-facets` Phase 0's parser. Missing 5/7 header fields in the canonical example is a silent drift accelerant.
- Validated against `active-project/theater/bones/b01-c01.md` (all 7 fields present in real output; the example had 2).
- Stale slug `taylor-hebert-westeros` predates the `-kl-122ac` project-context suffix convention; `septon-dying-protector` is not in the active cast.
- Cost: ~15 lines; no structural change; no downstream breakage.

**Surveyed surfaces this pass:**
- `cards/persona-exemplars/` — all active actors + audience personas covered (Tier-1 gap from Pass 1 is closed)
- `and-experiment/persona-exemplars/` — gael-targaryen.md structure correct; frontmatter complete; no gap
- `scripts/normalize_inflight_r2.py` — dead code (R2 retired under DEC-0116); unreferenced in any command body; low-risk removal but lower value than schema fix
- `scripts/check-threads.py` — active (referenced in `and-reoutline.md` Phase 5); no brittleness finding at this resolution
- `and-facets.md` class library — 12 classes fully enumerated; no clear gap without a live review signal to anchor it

**Next candidate:** `rubric-dialogue.md` body — three retired sections still carry detailed dead workflow text (Pass 2 deferred this). Alternatively `scripts/normalize_inflight_r2.py` removal (dead code from retired R2 round).
