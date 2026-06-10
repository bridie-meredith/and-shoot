---
description: Slim facet pipeline for one chapter. Single command, one authoring round + one mechanical audit — R1 fanout → fanin → context/aliveness review → (conditional) remediation → audit → persist. The R2 judging round and the Phase 5b adversarial audience-gate are RETIRED under URI-FACETS-SLIM (DEC-0116). Output - active-project/theater/facets/ + audit report + orchestrator-critic verdict. Usage - /and-facets <book>-<chapter>
---

Slim facet pipeline. One chapter in, mechanically-audited facet graph out. **The facet layer authors once and audits once.** The expensive second-look machinery — the R2 facet-judging round and the per-facet 3-of-3 adversarial audience-gate — is retired (DEC-0116). The adversarial reading of the *actual prose a reader sees* now lives where it belongs: `/and-stitch` Phase 9 cold-read + naive-follow gate (hardened under DEC-0115). The facet-layer's own gate is the single mechanical auditor (Phase 4): schema/constraint/cap/fence-clean before persist.

**URI-FACETS-SLIM (2026-06-08, DEC-0116) mutations — the simplification this command was rebuilt around:**
- **R2 judging round RETIRED.** The old Phase 3 (R2 fanout) + Phase 4 (R2 fanin) + Phase 4.5 (post-R2 re-review) are removed. R1's per-author cull + the Phase 4 mechanical auditor's DEDUP / SUPERFLUOUS / FREQUENCY-BAND classes do the culling the R2 judges used to do — and they do it as 1 auditor dispatch instead of ~6 judge dispatches. The R2 dialogue judge (the locked-graph KEEP/DELETE/REWRITE pass that survived URI-WRITE-DIALOGUE-COBONDED) is retired too; its one non-mechanical concern — dialogue duplicating a lens facet at the same anchor — is the Phase 4 auditor's DEDUP class.
- **Phase 5b adversarial audience-gate RETIRED.** The per-facet 3-of-3 audience reviewers + the 3-cycle remediation loop + cap-burn DELETE semantics are removed in full. Evidence (DEC-0115): the audience-gate reviewed an intermediate artifact the reader never sees and blessed 16 consecutive AIRLESS chapters "by signature" while the reader found the book unreadable. The gate's real-prose equivalent is `/and-stitch` Phase 9. The auditor (Phase 4) remains the facet-layer gate; the orchestrator-critic verdict (Phase 5) remains the facet-layer success standard.
- **Exposition demoted to consulted-by-stitcher (PROP-0004 / DEC-0014).** Exposition is still authored at Phase 1 (the union-of-personas gap test is the c05 followability content source), but its entries default to `surface: reference` — the stitcher and facet authors consult them for world-grounding; they are NOT folded inline as prose unless a context-ledger license fires. The em-dash inline-gloss fold-in that the ablation showed crushes pacing is off by default.
- **Conditional remediation preserved (the c05 + readability fix).** Phase 2.5's context-weave (PROP-0020) and readability-twin (PROP-0022) survive. The old Phase 4.6 remediation is now Phase 3, fired directly off Phase 2.5's open ledger holes (there is no Phase 4.5 to gate it anymore). Common case: 0 dispatches.
- Dispatch cost: ~60-100 → ~10-12 typical. The cut is entirely in the retired review rounds; the R1 author set and the mechanical auditor are unchanged.

**Carried forward from URI-SUBSTANCE-OVERHAUL (2026-05-17):**
- Tensometer facet removed; pressure-signal sourced from `series.substance.*` + per-chapter `substance_delta`.
- Scene-map facet is upstream-emitted by `/and-write` Phase 7; the Phase 4 auditor validates coverage (does not derive).
- Dialogue is upstream-emitted by `/and-write` Phase 7 (URI-WRITE-DIALOGUE-COBONDED, 2026-05-25); Phase 0 verifies presence, does not author.
- Facet output-path convention: flat naming under `theater/facets/` — `<facet>-<book>-<chapter>.md`, `_cite-index-<book>-<chapter>.md`, `scene-map-<book>-<chapter>.md`.

You are the orchestrator. The phases run in strict sequence:

```
theater/bones/<book>-<chapter>.md          (bones; upstream from /and-write Phase 7)
theater/facets/scene-map-<book>-<chapter>.md (scene-map; upstream from /and-write Phase 7)
        │
        ▼
   PHASE 1 — FANOUT (R1 parallel authoring)
            Facet authors in one Agent block; each writes its own
            facet file (or per-character slice) + its own annotated
            proto-lines copy under _inflight/. Exposition authored
            with surface:reference default (PROP-0004).
        │
        ▼
   PHASE 2 — FANIN (merge + cite-index)
            build_cite_index.py: body-integrity → citation union →
            slice consolidation → stale-citation check → cite-index.
        │
        ▼
   PHASE 2.5 — CONTEXT + ALIVENESS REVIEW   ← PROP-0020 / PROP-0022
            Series-context-aware reviewer reads the merged R1 graph.
            Writes the context-ledger (CONTEXT-REQUIRED) + the
            grounding-ledger (GROUNDING-REQUIRED). Non-blocking;
            feeds Phase 3.
        │
        ▼
   PHASE 3 — CONDITIONAL REMEDIATION        ← PROP-0020 / PROP-0022
            Fires ONLY if Phase 2.5 left open ledger holes on the
            spine (central event / load-bearing stake / causal
            hand-off, or an AIRLESS hole on a peak). Targeted
            exposition/sensory add round → re-cite-index → fixer or
            WARN. Common case: skipped (0 dispatches).
        │
        ▼
   PHASE 4 — AUDIT (single auditor dispatch, mechanical)
            Flag-only cross-cutting graph audit. Twelve classes incl.
            scene-map coverage, Earth-Bet fence, dialogue dedup +
            coverage sanity, the per-facet caps R2 used to enforce.
            Output: staff/auditor/facets-final-audit.md.
            HARD findings remediate via fixer; re-audit until 0 HARD.
            THIS IS THE FACET-LAYER GATE.
        │
        ▼
   PHASE 4.5 — Admin process-critic (non-blocking, conditional)
        │
        ▼
   PHASE 5 — PERSIST + orchestrator-critic verdict
            (only after Phase 4 = 0 HARD)
```

R1 is **blind**: each author reads only its rubric + non-facet upstreams (cards/state/vibes) + base bones. The audit is **cross-cutting**: one fork, full graph, mechanical. There is no second authoring round and no adversarial reviewer layer — the facet graph is locked by R1 + audit, and the prose-level adversarial read happens downstream at `/and-stitch` Phase 9 against rendered prose, not against this intermediate graph.

**Context-weave track (PROP-0020).** The b01-c05 three-FAIL trace's root cause was a context gap surfaced too late. Phase 2.5 reads the assembled R1 graph as a reader who has read prior chapters and identifies where context is genuinely required vs. where a lens facet already carries it. Required context is recorded as a **licensed exception** in the context-ledger (`active-project/staff/showrunner/context-ledger-<book>-<chapter>.md`) — exempt downstream from the anti-exposition penalty. Phase 3 authors the licensed adds (conditionally); the Phase 4 auditor honors the exemption.

**Readability twin (PROP-0022).** The same Phase 2.5 reviewer answers a second question — *is there a person to follow, or only an apparatus reporting?* AIRLESS stretches on the spine write `GROUNDING-REQUIRED` lines to the **grounding-ledger** (`active-project/staff/showrunner/grounding-ledger-<book>-<chapter>.md`), which license a sensory add past the frequency-band cap. `VOICE-FIXABLE` findings (embodied content rendered apparatus-first) carry to `/and-stitch` Phase 4 voice-embodiment discipline — calibrated against `active-project/voice-exemplar.md`. This is the upstream half of the DEC-0115 no-ledger fence; the downstream half is `/and-stitch` Phase 4 + Phase 9 naive-follow.

## Args

- `$1` — required. Chapter slug in `<book>-<chapter>` form (e.g. `b01-c01`), or the in-memory chapter slug `b01c01` (the command normalizes either form). If omitted, use `active.chapter` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate

1. Resolve chapter slug. Normalize to `<book>-<chapter>` form for file paths and to `b<NN>c<MM>` for showrunner-memory lookup.
2. Read `active-project/staff/showrunner/memory.md`. Determine resume point from `chapters[<slug>].status`:
   - `bones-written` — fresh run; start at Phase 1.
   - `faceted-r1` — R1 authored + merged; skip Phase 1+2, start at Phase 2.5.
   - `audited-r1-mechanical` — Phase 4 cleared (0 HARD); skip to Phase 5 persist.
   - `audited-r1` — already done. Print "already audited; re-run requires explicit re-audit" and exit unless re-audit is wanted.
   - (Legacy `faceted-r2` from pre-slim runs: treat as `faceted-r1` for resume — start at Phase 2.5. The R2 round no longer exists.)
3. Read the bones file at `active-project/theater/bones/<book>-<chapter>.md`. Lift the seven extended-header fields: `episode`, `narrator`, `goal`, `cast`, `locations`, `prior_episode`, `aggregate_range`. (The field name `episode:` is preserved for downstream-compatibility; value is the chapter slug.)
4. **Upstream scene-map precondition.** Confirm `active-project/theater/facets/scene-map-<book>-<chapter>.md` exists (emitted by `/and-write` Phase 7). Abort if missing — `/and-write` must be re-run.
4a. **Anchor-refresh gate (URI-FACETS-ANCHOR-REFRESH, A1).** HARD-ABORT (not warn) if the bones file is newer than any pre-existing facet for this chapter OR if any pre-existing facet contains anchor IDs that no longer resolve in the current bones file. Two checks:
    - **mtime check:** `mtime(theater/bones/<book>-<chapter>.md)` vs `mtime(theater/facets/<facet>-<book>-<chapter>.md)` for every facet file at this chapter (excluding `scene-map-<book>-<chapter>.md`, which is bones-co-emitted). If bones is newer than ANY facet, HARD-ABORT.
    - **anchor-resolution check:** scan every pre-existing facet file for `@<flat_id>` anchors and `[<facet>:<flat_id>]` citations. Any anchor whose flat_id is not in the current bones file (deletion gap OR id-space shift from `/and-write redo`) is a `STALE-ANCHOR` HARD finding.
    On HARD-ABORT, print:
    ```
    /and-facets Phase 0 HARD-ABORT (anchor-refresh): bones file at <path> is newer than existing facets, OR existing facets cite anchors that no longer resolve in the current bones.
    Stale facets: <list of paths>
    Stale anchors: <list of [<facet>:<flat_id>]>
    Resolution: archive existing facet files to active-project/theater/_archive/<timestamp>-stale-from-rewrite/ and re-run /and-facets <chapter> for a clean traversal.
    ```
4b. **Bones-review precondition (URI-WRITE-BONES-REVIEW-GATE — HARD-ABORT).** Confirm `chapters[<slug>].bones_review` is present in showrunner memory AND fresh. Fresh means `bones_review.bones_file_mtime_at_review` equals the current `mtime(theater/bones/<book>-<chapter>.md)` AND `bones_review.stale_since` is null. If absent or stale, HARD-ABORT:
    ```
    /and-facets Phase 0 HARD-ABORT (bones-review): chapter <slug> has no fresh /and-review bones record.
    Resolution: run /and-review bones <slug>, then re-invoke /and-facets <slug>.
    ```
    A `bones_review.verdict: FAIL` does not by itself abort (the user may knowingly proceed past notes), but absence or staleness does. **`bones_review.follow_check: FOLLOW-FAIL` DOES HARD-ABORT** — gross un-followability at the bone layer must be fixed at `/and-write <slug> revise` before any facet spend:
    ```
    /and-facets Phase 0 HARD-ABORT (followability): chapter <slug> bones_review.follow_check = FOLLOW-FAIL.
    The bones are not followable as-is; facet skin cannot rescue a bone-level coherence gap.
    Resolution: run /and-write <slug> revise to close the gap, re-run /and-review bones, then re-invoke /and-facets.
    ```
5. **Facet-namespace clearance (URI-FACETS-CROSS-CHAPTER-ARCHIVE).** The facet pipeline writes to chapter-unnamespaced shared paths — `theater/facets/<facet>.md`, `theater/facets/_cite-index.md`, `theater/proto-lines/<slug>.md`, `theater/dialogue/<character-slug>.md`, `staff/auditor/facets-*.md`. Two cases:
    - **Prior-chapter facet output present (cross-chapter collision).** Scan `theater/facets/*.md` (excluding `scene-map-<current-chapter>.md`). Read each facet file's `episode:` header. If ANY facet file, the `_cite-index.md` header, or `theater/proto-lines/*.md` belongs to a **different** chapter, AUTO-ARCHIVE the entire prior-chapter working set:
      1. `mkdir -p active-project/theater/_archive/<UTC-timestamp>-<prior-chapter>-facets/`.
      2. `git mv` (fallback `mv`) into it, mirroring paths relative to `active-project/`: all of `theater/facets/*` except `scene-map-<current-chapter>.md`; `theater/facets/_inflight*/`; `theater/proto-lines/<prior-slug>.md`; all `theater/dialogue/*.md`; `staff/auditor/facets-*.md`; `staff/fixer/{and-facets,facets}-*.md`; `staff/showrunner/and-facets-<prior-chapter>-summary.md`. **Do NOT archive** cross-chapter persistent files: `staff/exposition-author/glossed-terms.md`, all persona/agent `card.md` files, `theater/bones/`.
      3. Write a `MANIFEST.md` into the archive root recording timestamp, reason, contents, and the restore command (`cp -rn` from the archive back into `active-project/`).
      Print the archive root path and the moved-file count. Continue the run.
    - **Current-chapter facet output present (re-run case).** If facet files for the *current* chapter exist, abort with paths printed; the user re-archives manually before re-running. (Skip this check on partial-run resume.)

    Confirm `active-project/theater/dialogue/` holds no stray `<character-slug>.md` files belonging to a prior chapter after clearance.
6. Confirm warehouse loc cards for every slug in `locations:` resolve. Confirm every `cast:` slug resolves under `active-project/actors/<slug>/`.
7. Read `schemas/facet.schema.md`, `schemas/bones.schema.md`, `schemas/audit-report.schema.md`, `schemas/dialogue.schema.md` once (orchestrator reference).
8. Create `active-project/theater/facets/_inflight/`.
9. **Speaking-character + speech-bone inventory (verification only under URI-WRITE-DIALOGUE-COBONDED).** Grep the canonical bones file for dialogue-anchor bones (speech-form `speaks to` AND licensed action-form bones carrying `[<character-slug>:<id>]` citation tokens). Record:
   - `speech_bones`: the full list of bone flat_ids where the SVO is `<X> speaks to <Y>`.
   - `speakers`: the distinct set of subject slugs across those bones.
   Dialogue files are **mandatory and upstream**: the per-character files at `theater/dialogue/<speaker-slug>.md` are co-emitted by `/and-write` Phase 7, and the bones file already carries `[<speaker-slug>:<id>]` citation tokens on every dialogue-anchor bone. **Phase 0 verifies (does not author) dialogue presence** — if any expected speaker file is missing or any dialogue-anchor bone has no citation, abort and route back to `/and-write` (the gate that should have caught this is `/and-write` Phase 7 downstream-gate pre-verify). There is no dialogue author in this command.
10. **Parking-lot scan (Rule 14).** Read `active-project/staff/showrunner/parking-lot.md`. Items matching this invocation (`target.command: /and-facets` + `target.scope` = `<book>-<chapter>` or `*` + `status: open`): HARD → abort unless this run resolves; SOFT → carry to the Phase 4 audit report + final summary. Resolving phase stamps `resolved_at` + `resolved_by` + `resolution_note`; never delete.

Print:
```
Chapter: <slug>
Narrator: <slug>
Goal: <one sentence>
Cast: <slug>, <slug>, ...
Locations: <slug>, ...
Bones: <path>  (<count> bones)
Scene-map: <path>  (<S> scenes covering 1-<N>)
Speech bones: <count>  (speakers: <slug>, <slug>, ...)
Starting phase: <Phase 1 | Phase 2.5 | Phase 5>
```

---

## Phase 1 — FANOUT: R1 parallel authoring

**Dispatch discipline:**

- **One parallel Agent block.** All R1 authors fire in a single message with concurrent Agent tool calls. Sequential dispatch is a build defect.
- **No shared-file race.** Each author writes (i) its facet file (or per-character slice — distinct paths) and (ii) an annotated proto-lines copy under `_inflight/proto-lines-<facet>.md`. The base proto-lines file is **not** mutated during R1.
- **Citation write-back on the author's copy.** Each author copies the base proto-lines file to its `_inflight/` path and appends `[<facet-prefix>:<id>]` to every proto-line it decorated. Prefixes: `loc-state`, `narrator`, `sensory`, `state`, `mem`, `feel`, `meta`, `vibes`, `exposition`. (Dialogue authors do not exist here — dialogue citations `[<character-slug>:<id>]` are already on the bones from `/and-write` Phase 7.)
- **Forbid loading other R1 facet files.** Each author reads only its rubric + the inputs the rubric names + the base proto-lines. No cross-R1-facet peeking. Where pressure-signal is needed, the per-chapter `substance_delta` from showrunner memory is the substitute.
- **Per-file cull is the author's last act.** Per `schemas/facet.schema.md` § "Per-file cull" — delete-only, one pass. (Under the slim pipeline there is no R2 judge to do a second cull, so the R1 author's own cull is the only per-facet self-review; the cross-facet cull is the Phase 4 auditor's DEDUP/SUPERFLUOUS pass.)
- **Body integrity.** Authors append citations only; SVO bodies in `_inflight/` must be byte-identical to the base. Merge tool aborts the run if any body diverges.
- **Each dispatch returns:** path to written facet file, path to `_inflight/` proto-lines copy, entry count, cull count, any flagged seams.

### R1 authors (in the parallel block)

**1. location-state (studio)** — base proto-lines; all loc cards named in `locations:`; schema § location-state; `design/shoot-v2/rubric-location-state.md`; movement-verb gate; per-chapter `substance_delta`. Out: `location-state.md` + `_inflight/proto-lines-loc-state.md`.

**2. narrator-interest (POV impersonator)** — POV stack (card + behavior cards + LTM + STM + state); base proto-lines; per-chapter `substance_delta`; `rubric-narrator-interest.md`; schema § interest flags — narrator. Override impersonator: facet-authoring (no show.md, no action costs). Out: `interest-narrator.md` + `_inflight/proto-lines-narrator.md`.

**3. sensory (studio — fresh fork)** — base proto-lines; per-chapter `substance_delta`; all loc cards; `rubric-sensory.md`; disambiguation gate; per-scene cap ≤3; sparsity 3-6%; modality ≥2 per episode. Out: `sensory.md` + `_inflight/proto-lines-sensory.md`.

**4. state-updates env (studio — fresh fork)** — base proto-lines; per-chapter `substance_delta`; all loc + prop cards; `rubric-state-updates.md`; schema § state updates (`<target>.<field>: <old> -> <new>`, `target` ∈ {`studio`, `prop:<slug>`}). Scope: environmental + location + prop only. Out: `state-updates-env.md` + `_inflight/proto-lines-state-env.md`.

**5. state-updates actor (per-character impersonators ×N)** — for each `cast:` slug, one impersonator dispatch in the same parallel block. Character stack + base proto-lines + per-chapter `substance_delta` + `rubric-state-updates.md` § actor-state. Override impersonator: facet-authoring. Out: `state-updates-<slug>.md` + `_inflight/proto-lines-state-<slug>.md`.

**6. memory (POV impersonator — fresh fork; do not re-use NI fork's STM)** — POV stack; base proto-lines; per-chapter `substance_delta`; `rubric-memory-flags.md`; schema § memory flags. Override impersonator: facet-authoring. Out: `memory.md` + `_inflight/proto-lines-mem.md`.

**7. feeling (per-character impersonators ×N)** — for each `cast:` slug, one impersonator dispatch in the same parallel block. Character stack + base proto-lines + per-chapter `substance_delta` + `rubric-feeling.md`; schema § feeling flags — per-character per-scene cap ≤1 hard; sparsity 2-5%; multi-justification ≥3 of 5. Forbid: named-feeling vocabulary, hedges, similes. Override impersonator: facet-authoring. Out: `feeling-<slug>.md` + `_inflight/proto-lines-feel-<slug>.md`.

**8. metaphor (editor)** — base proto-lines; per-chapter `substance_delta` (curve-discipline substitute; AP7 default-refuse on bones outside hinge-magnitude band); `rubric-metaphor.md`; schema § metaphor flags; sparsity 0-3%; per-scene cap ≤1 cross-character. Metaphor entries carry `licensed-by:` notes naming the anchor by `<prefix>:<id>` form, resolved against the merged graph at Phase 2 (no R2 resolution pass exists — author must anchor cleanly or cull). Forbid: vibes, audience personas, behavior cards. Out: `metaphor.md` + `_inflight/proto-lines-meta.md`. (Metaphor is sparse-by-design and the lightest R1 author; the Phase 4 auditor enforces its 0-3% band and `licensed-by:` resolution. Retained under DEC-0116 as a single cheap R1 author with no separate judge.)

**9. vibes-updates (showrunner)** — base proto-lines; per-chapter `substance_delta`; all actor vibes files; all loc card VIBES sections; `staff/studio/vibes.md`; `rubric-vibes.md` + `rubric-vibes-v1.1-patch.md`; schema § vibes-updates (entity-target-primary form; `licensed-by:` mandatory and must resolve against the merged graph). Showrunner-as-author is the one exception to the "showrunner does not author" rule. Out: `vibes.md` + `_inflight/proto-lines-vibes.md`.

**10. exposition (exposition-author) — surface:reference default (PROP-0004 / DEC-0014).** base proto-lines; per-chapter `substance_delta`; audience persona cards `active-project/audience/*/`; series-plan; world-build cards; condition cards; character cards (for series-specific objects); `active-project/staff/showrunner/memory.md` (for `prior_episode`); cross-episode register `active-project/staff/exposition-author/glossed-terms.md` (if exists); schema § exposition. **Authoring authority:** schema § exposition + the union-of-audience-personas gap test + the context-ledger discipline (Phase 2.5). The union-of-audience-personas gap test is the central authoring discipline — it is the c05 followability content source, which is why exposition stays authored even though it is no longer inline-rendered by default. **Surface default:** every exposition entry is authored with `surface: reference` UNLESS it satisfies a context-ledger `CONTEXT-REQUIRED` license written at Phase 2.5 (in which case Phase 3 stamps it `surface: render` with the `licensed-context-exception` token). `surface: reference` entries are consulted by the stitcher and facet authors for world-grounding but are NOT folded inline as prose — the em-dash inline-gloss fold-in that the ablation showed crushes pacing is off by default. Out: `exposition-<slug>.md` + `_inflight/proto-lines-exposition.md` + register write-back annotated.

**Dialogue — NOT authored here.** Per-character dialogue files are co-emitted with the bones by `/and-write` Phase 7 (URI-WRITE-DIALOGUE-COBONDED); the bones already carry `[<character-slug>:<id>]` tokens. Phase 0 verified their presence. The Phase 4 auditor sanity-checks dialogue coverage + dedup; it does not author.

(State-updates-actor and feeling each fan out by cast size, making the parallel block larger by cast count.)

---

## Phase 2 — FANIN: merge + cite-index

```bash
python3 active-project/staff/cite-index/build_cite_index.py <episode-slug>
```

Five sub-phases inside the tool:

1. **Body-integrity check.** Every `_inflight/proto-lines-*.md` SVO body must match base byte-for-byte. Divergence → abort.
2. **Citation union.** Per proto-line ID, merge `[<prefix>:<id>]` tokens across base + all author copies. Deterministic order. Write canonical `theater/proto-lines/<slug>.md`.
3. **Slice consolidation.** `feeling-<slug>.md` → `feeling.md`; `state-updates-env.md` + `state-updates-<slug>.md` → `state-updates.md`. IDs renumbered monotonically; per-source `# source: <slug>` markers preserved. **Dialogue files are NOT consolidated** — per `schemas/dialogue.schema.md`, ID space is per-character. The cite-index builder treats per-character dialogue file IDs as a distinct citation namespace (`<character-slug>:<id>`).
4. **Stale-citation check.** Every `[<prefix>:<id>]` on canonical proto-lines must resolve to a facet-file entry. Unresolved → abort.
5. **Cite-index build.** `theater/facets/_cite-index.md` derived from canonical merged state.

If sub-phases 1 or 4 abort, fix the offending author (re-dispatch the responsible R1 author with a clarifying brief) and re-run. Phase 4 cannot run on a non-clean merge.

Set status `bones-written` → `faceted-r1` in showrunner memory.

---

## Phase 2.5 — CONTEXT + ALIVENESS REVIEW (PROP-0020 / PROP-0022)

**Why this exists.** The b01-c05 three-FAIL trace's root cause was a context gap surfaced too late — only at `/and-stitch` Phase 9, by a cold-reader who lacked the series context a real reader carries. This is the first (and now only) read of the assembled graph by a reviewer who *has* the series context (the inverse of the `/and-stitch` Phase 9 cold-reader). It answers two questions: *where would a reader who has read prior chapters still lose the thread?* (completeness) and *is there a person to follow, or only an apparatus reporting?* (readability).

**Dispatch.** ONE `general-purpose` agent, context-aware (NOT a cold read).

Inputs (read-only):
- The canonical merged proto-lines/bones graph `theater/proto-lines/<slug>.md` (R1-annotated with `[<facet>:<id>]` citations) + the R1 facet files.
- `chapters[<slug>].{goal, dramatic_shape, scenes[].chunk, scenes[].scene_conflict}`.
- `chapters[<slug>].handoff_in` (the series-so-far capsule).
- The cite-index.

### Axis 1 — completeness (context-weave)

Read the graph in order as a reader who has read to chapter N-1. For each place the narrative is not followable, emit a `FOLLOW-GAP @<bone>` finding and classify:

| Class | Meaning | Routing |
|---|---|---|
| `OK` | followable as-is | none |
| `WEAVE-FIXABLE @<bone>` | a lens facet (NI / memory / loc-state / feeling) already carries this | note in the report; no ledger entry (no R2 judge to action it — the facet that carries it is already present) |
| `CONTEXT-REQUIRED @<bone>` | genuinely needs context embedded (a term/person/stake/causal link the reader cannot recover from prior chapters + current graph) | write a **licensed exception** to the context-ledger |

**Output 1 — the report** at `active-project/staff/reviews/context-follow-<book>-<chapter>-<timestamp>.md` (FOLLOW-GAP + AIRLESS findings + per-finding class + rationale).

**Output 2 — the context-ledger** at `active-project/staff/showrunner/context-ledger-<book>-<chapter>.md`. Create if absent; append for re-runs (never delete; stamp superseded). Schema (inline):

```yaml
# context-ledger — <book>-<chapter> — PROP-0020
chapter: <slug>
entries:
  - id: ctx-<NNN>
    anchor: "@<bone>"
    gap: <one line — what the reader cannot follow without it>
    needed_context: <one line — the term/person/stake/link to orient>
    license: CONTEXT-REQUIRED
    licensed_at: 2.5
    licensed_by: context-follow-reviewer
    status: open | satisfied | superseded
    satisfied_by: <exposition entry id, once Phase 3 adds it>
    spine: true | false   # true = touches central event / load-bearing stake / causal hand-off
```

### Axis 2 — readability / aliveness

In the same pass, for each stretch that reads airless (events reaching the reader only through instrument/process register; no body, no sensory anchor, no one to inhabit), emit `AIRLESS @<bone>` and classify:

| Class | Meaning | Routing |
|---|---|---|
| `OK` | a person is present / it breathes | none |
| `VOICE-FIXABLE @<bone>` | the bone content IS embodied but is being rendered apparatus-first; a stitch render-choice fixes it | list in the Output-1 report; carries to `/and-stitch` Phase 4 voice-embodiment discipline; NOT a ledger entry |
| `GROUNDING-REQUIRED @<bone>` | the bones genuinely lack body/sensory material here; grounding must be ADDED, and the sensory frequency-band cap would normally block it | write a **licensed exception** to the grounding-ledger |

**Output 3 — the grounding-ledger** at `active-project/staff/showrunner/grounding-ledger-<book>-<chapter>.md` — mirror of the context-ledger schema, with `id: grd-<NNN>`, `license: GROUNDING-REQUIRED`, `licensed_by: aliveness-reviewer`, `satisfied_by: <sensory entry id>`, an `airless_symptom:` one-liner, and the same `spine:` flag.

**Non-blocking.** Phase 2.5 never aborts. It produces both ledgers and proceeds. (The bones-level "is this even followable / alive at all" stop already happened upstream at `/and-review bones`.) The reviewer's verdict — `FOLLOWABLE`/`GLARING-HOLE` × `ALIVE`/`AIRLESS-HOLE` — is recorded in `chapters[<slug>].context_followability` and decides whether Phase 3 fires.

Record `chapters[<slug>].context_followability.{completeness_verdict, readability_verdict, report_path, reviewed_at, context_ledger_open, grounding_ledger_open}` in showrunner memory.

---

## Phase 3 — CONDITIONAL REMEDIATION (PROP-0020 / PROP-0022)

**Fires ONLY if Phase 2.5 left an open ledger hole on the spine** — a `CONTEXT-REQUIRED` entry with `spine: true` (a `GLARING-HOLE` on the central event / a load-bearing stake / a scene-to-scene causal hand-off) OR a `GROUNDING-REQUIRED` entry with `spine: true` (an `AIRLESS-HOLE` on the central event / a peak). **Skipped otherwise** (the common case: off-spine ledger entries are advisory inputs to `/and-stitch`, not blockers). This is the slimmed descendant of the old Phase 4.6 — fired directly off Phase 2.5 (there is no Phase 4.5 re-review gate anymore).

**Step 1 — Targeted add round (handles whichever ledger has open spine lines).**
- *Context (completeness):* for each open `CONTEXT-REQUIRED @<bone>` with `spine: true`, dispatch the **exposition-author** (add mode) to author the orienting gloss at the anchor, stamped `surface: render` + `licensed-context-exception: ctx-<NNN>`. Ledger-licensed; exempt from add-cap + anti-exposition penalties. (Off-spine `CONTEXT-REQUIRED` entries stay `surface: reference` for the stitcher to consult; they do not get a forced inline render.)
- *Grounding (readability):* for each open `GROUNDING-REQUIRED @<bone>` with `spine: true`, dispatch the **sensory-author** (add mode) to author the concrete body/sensory grounding at the anchor, stamped `licensed-grounding-exception: grd-<NNN>`. Ledger-licensed; exempt from the sensory frequency-band cap. `VOICE-FIXABLE` findings are NOT authored here — they are render-discipline and carry to `/and-stitch` Phase 4.

Re-run `build_cite_index.py`. Stamp each satisfied ledger entry `satisfied` + `satisfied_by`.

**Step 2 — Verify (one reviewer).** Re-dispatch the context-aware reviewer (one `general-purpose`) on the post-add graph, scoped to the satisfied entries only. Return `CLOSED` or `RESIDUAL-HOLE`.

**Step 3 — Fixer or warn (terminal).**
- `CLOSED` → proceed to Phase 4.
- `RESIDUAL-HOLE` → dispatch **fixer** with the named residual gaps + the ledgers + the relevant facet/exposition rubrics; the fixer manually edits the facet/exposition content to close. Re-run the reviewer ONCE more. If now `CLOSED` → Phase 4. If still holed → **WARN**: write the unresolved gaps to `chapters[<slug>].context_followability.unresolved[]` + surface in the Phase 5 summary + the Phase 4.5 admin process-critic dispatch. **Non-blocking** — the chapter proceeds carrying a logged context-debt caveat. `/and-stitch` Phase 9 naive-follow remains the terminal backstop.

**Cap.** Phase 3 runs at most ONE add-round + ONE fixer pass. It is not a convergence loop.

---

## Phase 4 — AUDIT: single auditor dispatch (the facet-layer gate)

Dispatch **auditor** (fork) with the full graph. **This is the facet-layer's terminal gate** — with the R2 round and the Phase 5b audience-gate retired, the mechanical auditor is the sole check between R1 authoring and persist. The adversarial reading of rendered prose happens downstream at `/and-stitch` Phase 9 (cold-read + naive-follow), not here.

**Read inputs:**
- Proto-lines: `active-project/theater/proto-lines/<slug>.md` (canonical, post-remediation).
- All facet files at `active-project/theater/facets/` (`location-state`, `interest-narrator`, `sensory`, `state-updates`, `memory`, `feeling`, `metaphor`, `vibes`, `exposition-<slug>`).
- Scene-map: `active-project/theater/facets/scene-map-<book>-<chapter>.md` (upstream-emitted; validated here).
- All per-character dialogue files at `active-project/theater/dialogue/<character-slug>.md`.
- Cite-index: `_cite-index.md`.
- All active warehouse cards (`active-project/warehouse/*.card.md`) — for constraint checks.
- All behavior cards in scope (`cards/dialects/<character-slug>.card.md` + composition stack via margit) for every speaking character — for behavior-card-compliance checks.
- Series plans (showrunner memory: `series.chunk`, `series.substance`, `series.laws`, `series.lore`, `series.behaviors`) — for series-law constraint checks.
- Schemas: `facet.schema.md`, `dialogue.schema.md`, `audit-report.schema.md`.
- **Context-ledger** (if present) — the authority for which exposition entries are sanctioned context-exceptions.
- **Grounding-ledger** (if present) — the authority for which sensory entries are sanctioned grounding-exceptions (exempt from FREQUENCY-BAND).

**Forbid loading:** vibes-as-bias, audience personas (except loading persona slugs by name to verify exposition `licensed-by:` references resolve), source prose. The auditor reads the graph mechanically against constraints, not aesthetically.

**Mode: flag-only.** Findings route back to facet authors / fixer as flags. (Auditor delete-authority is deferred to a separate tuning effort.)

**Licensed-context-exception exemption.** An exposition entry carrying `licensed-context-exception: ctx-<NNN>` resolving to a `CONTEXT-REQUIRED` ledger entry is **exempt from**: AP-SCAN `new-plot-content`, FREQUENCY-BAND exposition over-count contribution, and SUPERFLUOUS/`rare`-add scrutiny. NOT exempt from STRUCTURAL, CONSTRAINT source-traceability/license-completeness, re-gloss check, or anti-jargon/hollow-prose AP-SCAN. A `licensed-context-exception` whose `ctx-<NNN>` does NOT resolve → HARD `FAULT-CONTEXT-LICENSE-DANGLING`.

**Licensed-grounding-exception exemption.** A sensory entry carrying `licensed-grounding-exception: grd-<NNN>` resolving to a `GROUNDING-REQUIRED` ledger entry is **exempt from the sensory FREQUENCY-BAND cap** and from SUPERFLUOUS/lonely-entry scrutiny. NOT exempt from STRUCTURAL, the sensory old-state anchor rubric, CONTRADICTION, or DEDUP. A dangling `grd-<NNN>` → HARD `FAULT-GROUNDING-LICENSE-DANGLING`.

### Audit classes (twelve)

1. **STRUCTURAL** — schema/format/integrity (headers, line shape, ID monotonicity, anchor resolution, bidirectional citation, proto-body integrity). **Dialogue-specific:** every dialogue entry's `@<proto-line-id>` resolves; every `<character-slug>:<id>` citation in proto-lines resolves to an existing dialogue entry; entry-ID monotonicity per-character; behavior-card slug in dialogue file header matches a real card.
2. **FREQUENCY-BAND** — per-rubric quantitative gates (sensory 3-6%; memory 5-12%; feeling 2-5%/char; metaphor 0-3%; NI 15-25%; **exposition `surface: render` entries 1-5% per episode, episode-open ≤4, first-mention ≤12, scene-open-orient ≤1 per scene** — `surface: reference` entries do not count toward the render band; **dialogue per-anchor cap ≤3 utterances, ≤1 per speaker per anchor unless documented split**).
3. **METADATA-INCONSISTENCY** — file headers / round-notes that contradict actual content.
4. **CURVE-SHAPE** — evaluates the chapter's pressure-signal curve against the `dramatic_shape` declaration + per-scene `rhythm-shape` from the scene-map. SHAPE-OK when scene-level rhythm-shape values cohere with chapter-level dramatic_shape. SHAPE-FAIL when the rhythm-shape sequence contradicts the declared shape (e.g., a `hinge` chapter with no `peak-bones`-class bone anywhere). (`dramatic_shape` enum is `rising | climax | falling | hinge`.)
5. **CONTRADICTION** — two facet entries set incompatible state on the same anchor; both flagged.
6. **DEDUP** — cross-facet-same-anchor / within-facet-different-anchor / within-facet-same-anchor. **Dialogue-specific (absorbs the retired R2 dialogue-judge's dedup concern):** utterance content rendered by NI / feeling / memory at the same anchor (the speaker says aloud what another facet already shows — one yields; default is the lens facet yields to dialogue, since dialogue is verbatim render and lens is render-as signal). This is the home of the "dialogue vs. the facet graph the upstream author was blind to" check that the R2 dialogue judge used to hold.
7. **SUPERFLUOUS** — lonely entries that don't survive rubric scrutiny. Bones in `rhythm-shape: flat-low` zones and off-anchor vibes are never superfluous. Runs the rubric's own three-axis test (necessity / interestingness / frugality) on the entry's own merits — displacement-logic is not a valid defense. (With no R2 judge, SUPERFLUOUS is the cross-facet cull the R2 round used to perform; the auditor flags, the fixer culls on HARD.)
8. **CONSTRAINT** — cross-facet contract violations: memory without NI-spine; metaphor without resolvable `licensed-by:` anchor; feeling duplicating POV NI; vibes with unresolvable or forward-citing `licensed-by:`; state-updates `<old>` contradicting prior state; POV-perceptual access on NI; **exposition source-traceability (every claim in `<gloss-text>` traces to a `<sources>` entry; unresolvable → HARD); exposition license-completeness (every entry's `<licensed-by>` names ≥1 persona-card slug + a specific gap-claim — missing/malformed → SIGNAL); exposition scene-orient fire-rule (`scene-open-orient` entries must satisfy time-skip-blank-precedes + loc-state-silent-at-anchor + NI-silent-on-time-or-place-in-first-2-anchors; violation → HARD); exposition re-gloss check (cross-reference `<key>` against `glossed-terms.md`; hit → HARD); exposition first-mention-character coverage (every named individual on first prose mention has a `first-mention-character` entry keyed to that anchor; POV excluded; dialogue-only mentions excluded; missing → HARD)**; **dialogue behavior-card-compliance (every utterance respects the speaker's behavior card §hard fences / §forbidden vocabulary / §monument rules; violation → HARD); dialogue-coverage sanity (URI-WRITE-DIALOGUE-COBONDED upstream-leak check — every Phase 0 dialogue-anchor bone is cited by ≥1 `<character-slug>:<id>` token, AND every `speakers` slug has a non-empty dialogue file; any miss → HARD `FAULT-UPSTREAM-LEAK` routing to `/and-write revise`, not a facets concern)**; **scene-map coverage (URI-SCENE-WINDOW — every bone in `proto-lines/<slug>.md` falls inside exactly one scene's `@<start>-@<end>` range; uncovered → HARD gap; double-covered → HARD overlap; dangling anchor → HARD; duplicate scene-label → HARD; frontmatter `total-scenes`/`total-bones` mismatch → HARD)**; **scene-map per-scene caps (sensory ≤3, feeling ≤1/char, metaphor ≤1 cross-character, exposition `scope: scene-open-orient` ≤1 — per scene; breach → HARD with scene-label cited)**; **loc-state transition-run continuity-license (per `rubric-location-state.md § Transition-run continuity license` — misplaced/dangling/overpacked continuity-carry entries → HARD)**.

   **Earth-Bet hard-fence proper-noun scan:** case-insensitive substring scan against the Earth-Bet proper-noun list across **every text field** of every facet entry **AND every dialogue utterance** — NI rationale, memory target-reference glosses (incl. `s<NN>e<NN>:<id>` slug components), metaphor `licensed-by:` notes + figure text, vibes target fields, feeling somatic-tell text, state-updates field names + `<old>`/`<new>` values, sensory disambiguation notes, loc-state fields, dialogue `<utterance>` + `<objective>` text. Slug components matter (a referral slug embedding `khepri-` or `gold-morning-` is a hit even without a full English phrase). Names (non-exhaustive — refresh against the canonical list): Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil, Tattletale, Bitch, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea. Any hit is HARD; emit `[<facet>:<id>] @<proto> — earth-bet-hard-fence — <name> at <field>: "<surrounding-text>"`.
9. **AP-SCAN** — per-rubric anti-pattern mechanical scan (memory AP-functional-callback, feeling AP-named-feeling-vocab, metaphor AP3/AP7/AP12, vibes AP-multi-source/AP8, etc.). **Dialogue anti-patterns (from `rubric-dialogue.md`):** AP-chassis-contamination (em-dash + semicolon spine on non-Taylor speakers); AP-modern-hr-speak (procedural/compliance-English in Westerosi register); AP-deposition-cadence; AP-nominalization-substituting-plain-English. **Severity calibration (URI-AP-SCAN-SATURATION):** an AP-SCAN hit is normally SIGNAL; escalates to HARD when `hits / total-entries ≥ 0.40` in a facet whose FREQUENCY-BAND ceiling is ≤ 25% (template-saturation → the "reading the construction before the content" failure). Emit `[<facet>:--] AP<N> <name> — saturation: <hits>/<total>`.
10. **TASTE-FLAG** — atmosphere-thin / momentum-stall / voice-fidelity candidates. Signal-only; feeds tuning. (Under the slim pipeline these are advisory notes for the principal / next-cycle rubric tuning — there is no audience-gate to escalate them to. A recurring TASTE-FLAG pattern graduates into a RUBRIC-FIDELITY check by editing the relevant facet rubric's REJECT section, per CLAUDE.md Rule 11.)
11. **PILE-UP REVIEW** — proto-lines with >4 co-located facets; verdict per pile-up: warranted | over-decoration. (With no R2 density-judge, PILE-UP is the auditor's over-decoration check — flag over-decoration HARD-to-fixer when a pile-up fails the warranted test.)
12. **RUBRIC-FIDELITY** (URI-RUBRIC-FIDELITY) — per-facet rubric-fidelity mechanical scan. For each facet's authored entries, verify against the facet's rubric's enumerated ACCEPT / REJECT signatures, anti-patterns, file-level shape gates, and cross-facet co-citation requirements. Four scan dimensions:
    (a) **Per-entry signature scan** — verb-class / value-class / field-class checks against the rubric's ACCEPT/REJECT enumerations. (e.g. loc-state anchor verb must be in `rubric-location-state.md § ACCEPT signatures`; state-updates `<new>` containing registration vocabulary → HARD anti-pattern.)
    (b) **Per-facet file-level shape gate** — each rubric's "Curve-shape rubric (file-level)" requirements (memory doubled-register test; state-updates POV co-citation completeness; sensory modality distribution floor ≥2 / dominance ceiling; per-facet quiet/peak distribution against scene-map fields).
    (c) **Per-entry cross-facet co-citation symmetric checks** — every co-citation each rubric's "Cross-facet contract" names (e.g. `state-updates actor:<POV>.* without NI co-citation` → HARD).
    (d) **Card-resolution checks** — every facet entry naming a card slug (memory `target-reference`, metaphor/vibes `licensed-by`, state-updates `target`) must resolve to an existing card; free-text glosses with no resolvable slug → HARD (auditor appends a margit-referral candidate slug).
    **Severity:** HARD by default for rubric-enumerated REJECT signatures / named anti-patterns / file-level gate failures / cross-facet co-citation gaps / unresolved card slugs. SIGNAL for borderline cases the rubric marks "exceptional with documented author defense" (defense absent → escalate to HARD).
    **Source enumeration.** Seeded from each facet rubric's §Anti-patterns + §Curve-shape (file-level) + §Cross-axis tests + §ACCEPT/REJECT signatures + §Cross-facet contract of: `rubric-memory-flags.md`, `rubric-sensory.md`, `rubric-state-updates.md`, `rubric-narrator-interest.md`, `rubric-location-state.md`, `rubric-feeling.md`, `rubric-metaphor.md`, `rubric-vibes.md`, `rubric-exposition.md`, `rubric-dialogue.md`. The auditor enumerates these at audit time; new rubric rules get picked up automatically.
    **Relationship to other classes.** Distinct from CONSTRAINT (pipeline-level contracts: schema, EARTH-BET, scene-map coverage, exposition source-traceability) and AP-SCAN (lexical anti-patterns without rubric-grounded REJECT enumeration). When a check appears in both CONSTRAINT and a rubric REJECT, CONSTRAINT takes precedence.

### Audit output

Write to `active-project/staff/auditor/facets-final-audit.md` per `schemas/audit-report.schema.md`:

```
audit: facets-final-r<N>
episode: <slug>
date: <YYYY-MM-DD>
mode: flag-only
status: <CLEAN | FINDINGS-PRESENT>
totals: <count> findings across <count> facets

---
## STRUCTURAL findings (<count>)
## FREQUENCY-BAND findings (<count>)
## METADATA-INCONSISTENCY findings (<count>)
## CURVE-SHAPE verdict
## CONTRADICTION findings (<count>)
## DEDUP findings (<count>)
## SUPERFLUOUS findings (<count>)
## CONSTRAINT findings (<count>)
## AP-SCAN findings (<count>)
## TASTE-FLAG findings (<count>)
## PILE-UP REVIEW (<count>)
## RUBRIC-FIDELITY findings (<count>)
---
## Audit summary
- Total entries reviewed: <count>
- HARD classes: STRUCTURAL <n>, CONTRADICTION <n>, DEDUP <n>, SUPERFLUOUS <n>, CONSTRAINT <n>, RUBRIC-FIDELITY <n>, PILE-UP(over-decoration) <n>
- SIGNAL classes: FREQUENCY-BAND, METADATA-INCONSISTENCY, AP-SCAN, TASTE-FLAG (AP-SCAN escalates to HARD on saturation)
- CURVE-SHAPE: <verdict>
## Routing
For each finding, name the facet author. Flag-only: no executes.
```

**Auditor return to orchestrator:** path to report; finding counts per class; one-line headline (CLEAN | FINDINGS-PRESENT with count).

**Phase 4 gate (the facet-layer gate).** HARD = 0 required before persist. SIGNAL findings are advisory. If HARD > 0, dispatch **fixer** with the audit report; re-fire Phase 4 until HARD = 0 or remediation budget (2 passes) exhausts. If HARD persists past 2 passes, the orchestrator-critic verdict (Phase 5) goes NOT-SUCCESSFUL and the chapter does NOT flip to `audited-r1` — it ships its facets carrying named HARD debt only on explicit principal override (out-of-band, recorded). On Phase 4 clean, set showrunner-memory status: `faceted-r1` → `audited-r1-mechanical`.

**Fixer-ADD pre-validation (URI-FACETS-CYCLE-N-ADD, A3).** If a fixer remediation includes any ADD, the ADD must pre-validate against the full per-entry rubric BEFORE commit: load the relevant facet rubric; walk every REJECT signature / anti-pattern; for cross-facet anchor rubrics validate the required anchor exists in its upstream artifact. On pre-validation fail, land the upstream artifact edit first, then commit the ADD. Log each ADD attempt + result to `staff/fixer/and-facets-fixes.md`.

---

## Phase 4.5 — Admin process-critic dispatch (URI-ADMIN-PROCESS-CRITIC; non-blocking)

Fire on any of:
- A Phase 5 orchestrator-critic verdict of **NOT-SUCCESSFUL** or **SHIPPABLE-WITH-CAVEATS**.
- A Phase 4 HARD-persist-past-2-passes (the auditor could not clear within budget).
- A Phase 3 context-remediation **WARN** (`chapters[<slug>].context_followability.unresolved[]` non-empty).

Non-blocking — Phase 5 persist proceeds. Dispatch:
- `subagent_type: admin`
- prompt carries: `mode: process-critic`; `trigger.reason: failure`; `trigger.source_report: active-project/staff/auditor/facets-final-audit.md`; `trigger.source_verdict: <Phase 5 verdict / WARN summary>`; `gate_path: .claude/commands/and-facets.md#phase-4`.

Admin's return logged in the Phase 5 summary tail under `## admin-process-critic`. New proposals land in `staff/admin/process-proposals.md`. See CLAUDE.md Rule 13. If the Phase 5 verdict is SUCCESS and no WARN fired, skip the dispatch.

---

## Phase 5 — Persist + orchestrator-critic verdict

### 5a. Persist

**Precondition:** Phase 4 = 0 HARD AND scene-map coverage gate clean (URI-SCENE-WINDOW). Dialogue-coverage sanity (Phase 4 CONSTRAINT) clean — regressions route to `/and-write revise`, not facets. If any gate is unclean, do not persist — return to the appropriate phase.

1. Confirm `facets-final-audit.md` (final-cycle) written.
1a. Re-verify dialogue-coverage from Phase 0 inventory. For each `speakers` slug, stat `active-project/theater/dialogue/<slug>.md` and confirm non-empty body. For each dialogue-anchor bone, grep the canonical bones for ≥1 `[<character-slug>:<id>]` token. Any miss → abort and route to `/and-write <chapter> revise`.
2. Update `active-project/staff/showrunner/memory.md`:
   - Status: `audited-r1-mechanical` → `audited-r1`.
   - `audit_path: active-project/staff/auditor/facets-final-audit.md`; `audit_complete: true`; `audit_findings: <count>` if non-zero.
   - `facets_path: active-project/theater/facets/`.
   - `round_1_complete: true`.
   - `context_followability.{...}` from Phase 2.5/3 (incl. any `unresolved[]`).
   - (No `audience_gate_*` fields — the audience-gate is retired. Legacy chapters may carry them; new runs do not set them.)

`_inflight/` may be retained for forensic review or pruned. The canonical proto-lines + facet files + `_cite-index.md` are the source of truth.

### 5b. Master summary

```
========================================================
=== /and-facets COMPLETE: <episode-slug> ===
========================================================

Phase 1 — R1 fanout:
  9 facet files authored (exposition surface:reference unless ledger-licensed)
  <count> total facet entries; <count>/<count> protolines decorated
  Exposition: <count> entries (render=<n>, reference=<n>; episode-open=<n>, first-mention=<n>)

Phase 2 — fanin (merge):
  <count> _inflight/ copies merged; canonical proto-lines written
  Slices consolidated: feeling (<count>), state-updates (<count> + env)
  Stale-cite check: <CLEAN | <n> errors>; cite-index built

Phase 2.5 — context + aliveness review:
  Completeness: <FOLLOWABLE | GLARING-HOLE>  (context-ledger: <n> open, <n> spine)
  Readability:  <ALIVE | AIRLESS-HOLE>  (grounding-ledger: <n> open, <n> spine)
  VOICE-FIXABLE → /and-stitch Phase 4: <count>

Phase 3 — conditional remediation:
  Fired: <yes (spine holes: <n>) | no (skipped)>
  Adds: context <n>, grounding <n>; verdict: <CLOSED | WARN (<n> unresolved)>

Phase 4 — Audit (mechanical; THE facet-layer gate):
  Mode: flag-only
  HARD: STRUCTURAL=<n> CONTRADICTION=<n> DEDUP=<n> SUPERFLUOUS=<n> CONSTRAINT=<n> RUBRIC-FIDELITY=<n> PILE-UP(over)=<n>
  SIGNAL: FREQ-BAND=<n> META=<n> AP-SCAN=<n> TASTE-FLAG=<n>
  CURVE-SHAPE: <verdict>
  Report: active-project/staff/auditor/facets-final-audit.md
  Remediation passes: <count>; final HARD: 0

Status: <slug> audited-r1
```

### 5c. Orchestrator-critic verdict (mandatory)

Read `staff/audience/and-facets-orchestrator-critic/card.md`. The critic evaluates the slim run's acceptance criteria (9 facet files exist; 0 HARD post-audit within budget; Phase 2.5 FOLLOWABLE+ALIVE or any holes ledger-licensed/remediated; showrunner memory current; process gaps captured; dispatch budget stated). Produce verdict appended to the master summary:

```
/and-facets orchestrator-critic verdict — <episode-slug>:
  Result: <SUCCESS | SHIPPABLE-WITH-CAVEATS | NOT-SUCCESSFUL>
  Criteria met: <count> / <total>
  HARD findings post-audit: <count>
  Phase 2.5: completeness <FOLLOWABLE|hole-status>, readability <ALIVE|hole-status>
  Dispatch count: <stated budget | overrun>
  Caveats (if any): <list>
  Recommendation: <ship | iterate | escalate>
```

**Decision rule:** SUCCESS (all met) → downstream may proceed. SHIPPABLE-WITH-CAVEATS (exactly 1 missed) → caveat named + queued; fire Phase 4.5. NOT-SUCCESSFUL (2+ missed) → remediate; do not flip status to `audited-r1`; fire Phase 4.5.

The critic does NOT mutate facets or cancel the run. It produces the standard; orchestrator + principal respond.

---

## Convergence and refusal handling

- **R1 is single-pass per author.** No retry loop. Faults discovered post-hoc surface in the Phase 4 audit (there is no R2 round to catch them mid-stream — the auditor is the catch).
- **Merge-tool aborts (body-integrity / stale-citation) are build defects.** Re-dispatch the responsible author with a clarifying brief; re-run the tool. Subsequent phases cannot proceed on a non-clean merge.
- **Soft refusals** (rubric gap, structural fault, blocking input missing) log under `active-project/staff/<author>/`; the orchestrator continues. The summary lists refusals.

---

## Notes

- **The R2 round and the Phase 5b audience-gate are retired (DEC-0116).** This is the central simplification. Do NOT reintroduce a second facet-authoring round or a per-facet adversarial reviewer layer without a fresh principal decision — the evidence (ablation density-harm + DEC-0115 audience-gate failure) is the basis for their removal. The cross-facet culling the R2 round did is the Phase 4 auditor's DEDUP/SUPERFLUOUS/PILE-UP job; the adversarial reading the audience-gate did is `/and-stitch` Phase 9's job (against real prose).
- **Scene-map is upstream-only** — emitted by `/and-write` Phase 7 from `substance_delta.axis_moves.magnitude`; the Phase 4 auditor validates coverage only. There is no in-pipeline scene-map authoring.
- **Exposition is consulted-by-stitcher by default** (PROP-0004) — authored for followability (the c05 content source) but `surface: reference` unless a context-ledger license fires; the inline em-dash fold-in is off by default.
- **Cross-facet deletion authority** belongs to the audit only (flag-only until the auditor is tuned for delete-authority; until then remediation routes back to authors / fixer).
- **Shared reviewer assets** (auditor class library — `CURVE-SHAPE` / `AP-SCAN` / `FREQUENCY-BAND` / `RUBRIC-FIDELITY` definitions) are authored once and consumed from both `/and-write` and `/and-facets`. Patterns the audience flags at `/and-write` Phase 6 bone-gate graduate into AP-SCAN entries via the auditor's TASTE-FLAG → AP-SCAN promotion path. Patterns worth promoting at `/and-facets` graduate into RUBRIC-FIDELITY by adding the rule to the relevant facet rubric's REJECT / anti-pattern / cross-facet contract section (the auditor enumerates those at audit time).
