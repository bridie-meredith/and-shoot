# Hygiene Ledger — and-shoot

Append-only. Each run appends a dated block. Artur only; do not editorialize.

---

## Run: 2026-06-12

**Branch:** `claude/gifted-hawking-h1470f`
**Sweep scope:** active-project/ + staff/ + theater/ + cards/ + schemas/

---

### Findings (severity order)

#### 1. HIGH — Orphaned draft files at showrunner root (should be in `_drafts/`)

Seven files sit at `active-project/staff/showrunner/` that belong in the adjacent `_drafts/` subdirectory. They are unique (not duplicated in `_drafts/`), so moving them requires checking `memory.md` for path references before any action.

Files:
- `active-project/staff/showrunner/b01c09-bones-draft-2026-05-31.md`
- `active-project/staff/showrunner/b01c11-bones-draft.md`
- `active-project/staff/showrunner/b01c11-draft.md`
- `active-project/staff/showrunner/b01c15-bones-draft.md`
- `active-project/staff/showrunner/b01c15-draft.md`
- `active-project/staff/showrunner/b01c19-bones-draft.md`
- `active-project/staff/showrunner/b01c20-draft.md`

The `_drafts/` directory already holds analogous draft files for c01–c08. These seven appear to have been written directly to the showrunner root during cascade production runs rather than into `_drafts/`. They are not referenced as canonical artifacts in command-body outputs; they appear to be working notes / intermediate bones drafts.

Route: **oskar** (owns working-memory layout + STM format). Before moving, confirm no `memory.md` path-ref points to any of these seven paths (grep recommended). If refs exist, update them first.

---

#### 2. MEDIUM — Broken `context_refs` in parking-lot item `pl-2026-06-01-002`

Two files cited in `context_refs` of `pl-2026-06-01-002` do not exist on disk:
- `active-project/staff/audience/sensory-old-state-reader/sensory-r1-verdict.md`
- `active-project/staff/auditor/facets-audience-gate-r1.md`

Both are artifacts from the `/and-facets` Phase 5b audience-gate cycle on b01c09 (now retired under DEC-0116). The item is SOFT-severity and targets `/and-review pipeline`. The missing files are supporting-evidence citations only, not structural dependencies — the parking-lot item is otherwise valid.

Route: **showrunner** (owns parking-lot). Add a note to `pl-2026-06-01-002.context_refs` that these two paths are permanently absent (artifacts from the retired Phase 5b audience-gate; the convergence trace and verdict were never persisted to disk per Rule 19 non-compliance at the time).

---

#### 3. MEDIUM — Orphaned per-chapter voice-exemplar experiments at `active-project/theater/` root

Two per-experiment voice-exemplar files sit at `active-project/theater/` rather than any archive or properly namespaced location:
- `active-project/theater/voice-exemplar-b01-c02.md`
- `active-project/theater/voice-exemplar-b01-c02.alt-1.md`

The canonical voice exemplar is at `active-project/voice-exemplar.md`. These two are experiment artifacts from the 2026-05-26 multi-arm stitch tournament (c02 third attempt). Per CLAUDE.md Rule 4 (nothing changes without being recorded), they should either be archived to `active-project/theater/_archive/` with the tournament timestamp, or noted in `memory.md` as superseded. Their presence at `theater/` root is catalog drift.

Route: **showrunner** (owns theater/ layout). Verify whether these files are referenced by any memory.md entry; if not, move to `active-project/theater/_archive/` with a note.

---

#### 4. SOFT — Missing context/grounding ledgers for b01-c16 and b01-c19

- `context-ledger-b01-c16.md` — absent. C16 facets ran (archive folder `20260605T000326Z-b01c16-facets` exists) but the ledger was not emitted or was left in the archive.
- `context-ledger-b01-c19.md` — absent. C19 grounding-ledger exists; context-ledger does not.
- Chapters c01–c06: both ledger types absent. These predate the PROP-0020/0022 context/grounding ledger mechanism (mechanism wired at c07); absence is expected, not a gap.

Route: **showrunner** (owns ledger files). Confirm whether c16/c19 ledgers should be retroactively created or whether memory.md already records the context/aliveness decisions for those chapters inline.

---

#### 5. SOFT — `worm-canon-pedant` audience STM at 993 lines (accumulating)

`active-project/audience/worm-canon-pedant/stm.md` has accumulated a full per-chapter substance verdict block for all 20 chapters (993 lines). `cape-fic-reader/stm.md` is at 388 lines. Both accumulate chapter entries without compression. Risk: context-window pressure when dispatching the audience persona for future chapters (b02+).

Route: **oskar** (owns STM format + audience health). Assess whether the per-chapter verdict history should be compressed to a summary block after chapter-production closes. No merge action until oskar decides the schema.

---

### Action taken

**Routing note — finding #1 to oskar** (routed via parking lot; see entry `pl-2026-06-12-hygiene-001` below).

No files modified. No merges. No persona content touched.

---
