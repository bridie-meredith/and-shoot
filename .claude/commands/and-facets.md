---
description: Unified facet pipeline for one chapter. Single command, six phases — R1 fanout → R1 fanin → R2 fanout → R2 fanin → audit (mechanical) → audience-gate (adversarial, blocking). Tensometer dropped under the substance overhaul; scene-map facet is upstream-emitted by /and-write Phase 7 (Phase 4d here is validation, not derivation). Output - active-project/theater/facets/ + active-project/theater/dialogue/ + audit report + audience-gate verdict. Usage - /and-facets <book>-<chapter>
---

Unified facet pipeline. One chapter in, audited + audience-accepted graph out. The four legacy sub-commands (-r1, -r2, -r3, -audit) are folded into this command; R3 is retired. Phase 5b — audience adversarial gate — is the final blocking gate; the auditor's mechanical scan and the audience's adversarial reading must BOTH come back clean before /and-facets is "done." **Dialogue** is folded in alongside exposition — R1 author + R2 judge + audit-class additions + audience-gate inclusion. Discipline lifts from v1 round-trip work (`design/shoot-v2/round-trip-method.md`, `dialogue-corpus.md`) via the locked rubric at `staff/dialogue-writer/rubric-dialogue.md`.

**URI-SUBSTANCE-OVERHAUL (2026-05-17) mutations:**
- Tensometer facet **removed** from R1/R2 fanout. R1 rubric input lists no longer read `tensometer.md`. Where pressure-signal is needed, rubrics consult `series.substance.*` + per-chapter `substance_delta` from showrunner memory instead.
- Phase 4d scene-map **downgraded from derivation to validation**. `/and-write` Phase 7 emits the scene-map facet directly from `chapters[].scenes[]` in memory; Phase 4d confirms its presence + runs the URI-SCENE-WINDOW coverage check.
- Phase 0 input-path renamed: `theater/proto-lines/<slug>.md` → `theater/bones/<book>-<chapter>.md`. Slug-arg shape: `<book>-<chapter>` (e.g. `b01-c01`).
- Phase 0 step 4 tens-precondition abort **removed** as dead code.
- Facet output-path convention: flat naming under `theater/facets/` — `<facet>-<book>-<chapter>.md`, `<facet>-<book>-<chapter>-<character>.md`, `_cite-index-<book>-<chapter>.md`, `scene-map-<book>-<chapter>.md`.

You are the orchestrator. Six phases run in strict sequence:

```
theater/bones/<book>-<chapter>.md  (bones; upstream from /and-write Phase 7)
theater/facets/scene-map-<book>-<chapter>.md  (scene-map; upstream from /and-write Phase 7)
        │
        ▼
   PHASE 1 — FANOUT (R1 parallel authoring)
            8 facet authors in one Agent block; each writes its
            own facet file (or per-character slice) + its own
            annotated proto-lines copy under _inflight/.
        │
        ▼
   PHASE 2 — FANIN (merge + cite-index)
            build_cite_index.py:
              - body-integrity check
              - citation union → canonical proto-lines
              - slice consolidation (feeling, state-updates)
              - stale-citation check
              - cite-index build
        │
        ▼
   PHASE 3 — FANOUT (R2 parallel judging)
            4 midband judges in one Agent block, full graph in each
            payload. Each writes its own mutated facet file +
            decision-log shard + its own annotated proto-lines copy
            under _inflight-r2/. Self-scoped delete only;
            citation cascade on the author's copy.
        │
        ▼
   PHASE 4 — FANIN (decision-log consolidate + merge + cite-index)
            build_cite_index.py rerun against _inflight-r2/;
            decision-log shards concatenated to .r2-decisions.md;
            arbiter glue (T1/T4 interventions) runs over shards.
        │
        ▼
   PHASE 5 — AUDIT (single auditor dispatch, mechanical)
            Flag-only cross-cutting graph audit.
            Output: active-project/staff/auditor/facets-final-audit.md.
            HARD findings remediate via fixer; re-audit until 0 HARD.
        │
        ▼
   PHASE 5b — AUDIENCE-GATE (adversarial, BLOCKING)
            Per-facet audience adversarial dispatches reading the
            annotated proto-lines + facet graph + cite-index.
            Specialists fire for facets that have them
            (e.g. sensory); active project audience falls back for
            the rest. Per-facet aggregate verdict (accept / revise
            / fail). Any revise/fail routes to fixer; re-audit
            (Phase 5) + re-fire 5b. Cycle cap: 3.
        │
        ▼
   PHASE 6 — PERSIST + orchestrator-critic verdict
            (only after Phase 5 = 0 HARD AND Phase 5b = ACCEPT)
```

R1 is **blind**: each author reads only its rubric + non-facet upstreams (cards/state/vibes) + base bones. R2 is **graph-aware**: every judge gets all R1 facet outputs (facet files + per-character dialogue files) + the cite-index. The audit is **cross-cutting**: one fork, full graph. The audience-gate is **adversarial-graph-aware**: per-facet adversarial reviewers attack the locked graph the way the auditor's mechanical scan cannot.

## Args

- `$1` — required. Chapter slug in `<book>-<chapter>` form (e.g. `b01-c01`), or the in-memory chapter slug `b01c01` (the command normalizes either form). If omitted, use `active.chapter` from `active-project/staff/showrunner/memory.md`.

---

## Phase 0 — Validate

1. Resolve chapter slug. Normalize to `<book>-<chapter>` form for file paths and to `b<NN>c<MM>` for showrunner-memory lookup.
2. Read `active-project/staff/showrunner/memory.md`. Determine resume point from `chapters[<slug>].status`:
   - `bones-written` — fresh run; start at Phase 1.
   - `faceted-r1` — partial-run resume; skip Phase 1+2, start at Phase 3.
   - `faceted-r2` — partial-run resume; skip Phase 1–4, start at Phase 5.
   - `audited-r1-mechanical` — Phase 5 cleared (0 HARD) but audience-gate not yet run or in mid-cycle. Resume at Phase 5b.
   - `audited-r1` — both Phase 5 + Phase 5b cleared; already done. Print "already audited; re-run requires explicit re-audit" and exit unless re-audit is wanted.
3. Read the bones file at `active-project/theater/bones/<book>-<chapter>.md`. Lift the seven extended-header fields: `episode`, `narrator`, `goal`, `cast`, `locations`, `prior_episode`, `aggregate_range`. (The field name `episode:` is preserved for downstream-compatibility; value is the chapter slug.)
4. **Upstream scene-map precondition.** Confirm `active-project/theater/facets/scene-map-<book>-<chapter>.md` exists (emitted by `/and-write` Phase 7). Abort if missing — `/and-write` must be re-run.
5. Confirm `active-project/theater/facets/` is empty of this-chapter's facet outputs apart from `scene-map-<book>-<chapter>.md`. If other facet files for this chapter exist, abort with paths printed; archive first to re-run. (Skip this check on partial-run resume.) Confirm `active-project/theater/dialogue/<book>-<chapter>.md` does not exist or `mkdir -p` is clean.
6. Confirm warehouse loc cards for every slug in `locations:` resolve. Confirm every `cast:` slug resolves under `active-project/actors/<slug>/`.
7. Read `schemas/facet.schema.md`, `schemas/bones.schema.md`, `schemas/audit-report.schema.md`, `schemas/dialogue.schema.md` once (orchestrator reference).
8. Create `active-project/theater/facets/_inflight/` and `active-project/theater/facets/_inflight-r2/`.
9. **Speaking-character + speech-bone inventory (URI-DIALOGUE-COVERAGE-GATE).** Grep the canonical bones file for `speaks to` bones. Record:
   - `speech_bones`: the full list of bone flat_ids where the SVO is `<X> speaks to <Y>`.
   - `speakers`: the distinct set of subject slugs across those bones.
   If `speech_bones` is non-empty, dialogue is **mandatory** — Phase 1 dialogue author must produce one `theater/dialogue/<book>-<chapter>.md` entry per speaker with ≥1 entry, AND every speech bone must be cited by ≥1 entry post-R2 merge.

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
Starting phase: <Phase 1 | Phase 3 | Phase 5>
```

---

## Phase 1 — FANOUT: R1 parallel authoring

**Dispatch discipline:**

- **One parallel Agent block.** All R1 authors fire in a single message with concurrent Agent tool calls. Sequential dispatch is a build defect.
- **No shared-file race.** Each author writes (i) its facet file (or per-character slice — distinct paths) and (ii) an annotated proto-lines copy under `_inflight/proto-lines-<facet>.md` (or `_inflight/proto-lines-<facet>-<slug>.md` for per-character). The base proto-lines file is **not** mutated during R1.
- **Citation write-back on the author's copy.** Each author copies the base proto-lines file to its `_inflight/` path and appends `[<facet-prefix>:<id>]` to every proto-line it decorated. Prefixes: `loc-state`, `narrator`, `sensory`, `state`, `mem`, `feel`, `meta`, `vibes`. **Dialogue authors append `[<character-slug>:<id>]` instead of a facet-prefix token** (per `schemas/dialogue.schema.md` § Stitch interface — the citation IS the character slug, no `dialogue:` namespace). Upstream `tens:` citations on the base proto-line are preserved.
- **Forbid loading other R1 facet files.** Each author reads only its rubric + the inputs the rubric names + the base proto-lines. No cross-R1-facet peeking. Tens reads are dropped under the substance overhaul; where pressure-signal is needed, the per-chapter `substance_delta` from showrunner memory is the substitute.
- **Per-file cull is the author's last act.** Per `schemas/facet.schema.md` § "Per-file cull" — delete-only, one pass.
- **Body integrity.** Authors append citations only; SVO bodies in `_inflight/` must be byte-identical to the base. Merge tool aborts the run if any body diverges.
- **Each dispatch returns:** path to written facet file, path to `_inflight/` proto-lines copy, entry count, cull count, any flagged seams.

### R1 authors (nine in the parallel block)

**1. location-state (studio)** — base proto-lines; all loc cards named in `locations:`; schema § location-state; `design/shoot-v2/rubric-location-state.md`; movement-verb gate; per-chapter `substance_delta` from showrunner memory (pressure-signal substitute). Forbid: other facet rubrics, vibes. Out: `location-state.md` + `_inflight/proto-lines-loc-state.md`.

**2. narrator-interest (POV impersonator)** — POV stack (card + behavior cards + LTM + STM + state); base proto-lines; per-chapter `substance_delta` from showrunner memory; `rubric-narrator-interest.md`; schema § interest flags — narrator. Override impersonator: facet-authoring (no show.md, no action costs). Forbid: other characters' cards, audience personas, source prose. Out: `interest-narrator.md` + `_inflight/proto-lines-narrator.md`.

**3. sensory (studio — fresh fork)** — base proto-lines; per-chapter `substance_delta` from showrunner memory (pressure-signal substitute); all loc cards; `rubric-sensory.md`; disambiguation gate; per-scene cap ≤3; sparsity 3-6%; modality ≥2 per episode. Out: `sensory.md` + `_inflight/proto-lines-sensory.md`.

**4. state-updates env (studio — fresh fork)** — base proto-lines; per-chapter `substance_delta` from showrunner memory; all loc + prop cards; `rubric-state-updates.md`; schema § state updates (`<target>.<field>: <old> -> <new>`, `target` ∈ {`studio`, `prop:<slug>`}). Scope: environmental + location + prop only. Out: `state-updates-env.md` + `_inflight/proto-lines-state-env.md`.

**5. state-updates actor (per-character impersonators ×N)** — for each `cast:` slug, one impersonator dispatch in the same parallel block. Character stack + base proto-lines + per-chapter `substance_delta` from showrunner memory + `rubric-state-updates.md` § actor-state. Override impersonator: facet-authoring. Out: `state-updates-<slug>.md` + `_inflight/proto-lines-state-<slug>.md`.

**6. memory (POV impersonator — fresh fork; do not re-use NI fork's STM)** — POV stack; base proto-lines; per-chapter `substance_delta` from showrunner memory (substance-density substitute); `rubric-memory-flags.md`; schema § memory flags. NI co-citation is a R2 concern. Override impersonator: facet-authoring. Out: `memory.md` + `_inflight/proto-lines-mem.md`.

**7. feeling (per-character impersonators ×N)** — for each `cast:` slug, one impersonator dispatch in the same parallel block. Character stack + base proto-lines + per-chapter `substance_delta` from showrunner memory + `rubric-feeling.md`; schema § feeling flags — per-character per-scene cap ≤1 hard; sparsity 2-5%; multi-justification ≥3 of 5. Forbid: named-feeling vocabulary, hedges, similes. Override impersonator: facet-authoring. NI non-redundancy is a R2 concern. Out: `feeling-<slug>.md` + `_inflight/proto-lines-feel-<slug>.md`.

**8. metaphor (editor)** — base proto-lines; per-chapter `substance_delta` from showrunner memory (curve-discipline substitute; AP7 default-refuse on bones outside hinge-magnitude band); `rubric-metaphor.md`; schema § metaphor flags; sparsity 0-3%; per-scene cap ≤1 cross-character. R1 metaphor entries may carry **provisional** `licensed-by:` notes naming the intended anchor by description; resolution to machine-readable `<prefix>:<id>` form happens in R2. Forbid: vibes, audience personas, behavior cards. Out: `metaphor.md` + `_inflight/proto-lines-meta.md`.

**9. vibes-updates (showrunner)** — base proto-lines; per-chapter `substance_delta` from showrunner memory; all actor vibes files; all loc card VIBES sections; `staff/studio/vibes.md`; `rubric-vibes.md` + `rubric-vibes-v1.1-patch.md`; schema § vibes-updates (entity-target-primary form; `licensed-by:` mandatory; R1 provisional anchor-hints OK, resolution in R2). Showrunner-as-author is the one exception to the "showrunner does not author" rule. Out: `vibes.md` + `_inflight/proto-lines-vibes.md`.

**10. exposition (exposition-author)** — base proto-lines; per-chapter `substance_delta` from showrunner memory (peak/transitional gate substitute for which anchors warrant heavier render-as); audience persona cards `active-project/audience/*/`; series-plan; world-build cards; condition cards; character cards (for series-specific objects); `active-project/staff/showrunner/memory.md` (for `prior_episode`); cross-episode register `active-project/staff/exposition-author/glossed-terms.md` (if exists); `rubric-exposition.md`; schema § exposition. Audience-modeled-by-construction: the union-of-audience-personas gap test is the central authoring discipline. Forbid: lens facet rubrics (R1 stays blind), source prose. Out: `exposition-<slug>.md` + `_inflight/proto-lines-exposition.md` + register write-back annotated. The exposition author DOES NOT read other R1 facet outputs at R1 (audience-pure gap-identification); the cross-check against lens facets is the R2 judge's job.

**11. dialogue (dialogue-writer) — per-behavior-card fanout** — for each distinct behavior card present in the cast (resolved by reading `cards/dialects/<character-slug>.card.md` for every `cast:` slug and grouping by card), one fork in the parallel block. Each fork authors all speakers sharing that card. Reads: behavior card stack (margit-composed: leaf → `inherits:` parent → universal overlay → `references:` adjacent cards); speaker persona + ltm + stm + state for every speaker the fork covers; base proto-lines (the speaking-beat anchors are proto-lines where this card's speakers appear as subject of a `speaks` SVO); per-chapter `substance_delta` from showrunner memory (peak anchors pressure register state); `staff/dialogue-writer/rubric-dialogue.md`; schema `schemas/dialogue.schema.md`. Discipline: eight v1 round-trip writer patterns (per-card forks, card-stack load order, blind to originals, intent-as-state, multi-draft + chosen-mark, affirmative card-signature citation, anti-patterns explicit, calibration anchor) — all load-bearing per the rubric. Forbid: other R1 facet outputs (R1 stays blind), show files / source prose, behavior cards not in this fork's domain. Out: per-character dialogue files at `active-project/theater/dialogue/<character-slug>.md` per `schemas/dialogue.schema.md` (file location is outside `theater/facets/` per existing schema); drafts sidecar at `active-project/staff/dialogue-writer/<character-slug>.drafts.md` (multi-draft + chosen-mark + card-signature citations); annotated proto-lines copy at `_inflight/proto-lines-dialogue-<card-slug>.md` with `[<character-slug>:<id>]` citations on speaking-beat anchors.

(Ten authors. State-updates-actor and feeling each fan out further by cast size, making the parallel block larger by cast count; exposition adds a single dispatch; dialogue fans out by distinct-behavior-card count present in the cast — typically 3–5 in a Westeros episode.)

---

## Phase 2 — FANIN: merge + cite-index

```bash
python3 active-project/staff/cite-index/build_cite_index.py <episode-slug>
```

Five sub-phases inside the tool (see its module docstring):

1. **Body-integrity check.** Every `_inflight/proto-lines-*.md` SVO body must match base byte-for-byte. Divergence → abort.
2. **Citation union.** Per proto-line ID, merge `[<prefix>:<id>]` tokens across base + all author copies. Deterministic order. Write canonical `theater/proto-lines/<slug>.md`.
3. **Slice consolidation.** `feeling-<slug>.md` → `feeling.md`; `state-updates-env.md` + `state-updates-<slug>.md` → `state-updates.md`. IDs renumbered monotonically; per-source `# source: <slug>` markers preserved. **Dialogue files are NOT consolidated** — per `schemas/dialogue.schema.md`, ID space is per-character and `theater/dialogue/<character-slug>.md` is the canonical per-character location. The cite-index builder treats per-character dialogue file IDs as a distinct citation namespace (`<character-slug>:<id>`) from the facet prefixes.
4. **Stale-citation check.** Every `[<prefix>:<id>]` on canonical proto-lines must resolve to a facet-file entry. Unresolved → abort.
5. **Cite-index build.** `theater/facets/_cite-index.md` derived from canonical merged state.

If sub-phases 1 or 4 abort, fix the offending author (re-dispatch the responsible R1 author with a clarifying brief) and re-run. Phase 5 cannot run on a non-clean merge.

Set status `protolined` → `faceted-r1` in showrunner memory.

---

## Phase 3 — FANOUT: R2 parallel judging

**Dispatch discipline:**

- **One parallel Agent block.** All six midband judges (NI, memory, feeling-per-character, metaphor, exposition, dialogue-per-character) fire concurrently. Each judge sees the locked R1 graph; none sees the others' R2 mutations.
- **Full nine-facet graph + per-character dialogue files + cite-index in every dispatch payload.** Non-negotiable. Dialogue judges additionally receive the drafts sidecars for their characters (card-signature + facet-license citations on chosen drafts).
- **No shared-file race.** Each judge writes (i) its mutated facet file (deletes leave gaps; adds take next-available ID) and (ii) an annotated proto-lines copy under `_inflight-r2/proto-lines-<facet>.md` (or per-character for feeling) reflecting its citation cascades + adds. The base canonical proto-lines file is **not** mutated during R2.
- **Self-scoped deletion only.** A judge may delete only its own facet's entries. Cross-facet deletion authority is reserved for Phase 5 audit.
- **Citation cascade on the author's proto-lines copy.** When the judge deletes `<own>:<id>`, it strips `[<own>:<id>]` from every proto-line in its `_inflight-r2/` copy. The cite-index makes affected proto-lines cheap to identify.
- **Add-cap ≤5 per judge per run** (metaphor ≤3 per its refuse-by-default discipline). Cap-refusals logged.
- **No reordering of existing IDs.** Deleted IDs leave gaps. New entries get next-available IDs per facet.
- **Provisional-anchor binding.** R1 metaphor / vibes entries with descriptive `licensed-by:` hints get resolved here. A judge whose hint cannot resolve cleanly against the locked graph deletes the entry as unanchorable.
- **Locked-rubric + arbiter discipline.** Every judge dispatch carries `design/shoot-v2/r2-judge-tuning/B-locked-rubric.md` (gates G1–G5 as taste-questions) and `design/shoot-v2/r2-judge-tuning/C-arbiter-protocol.md` (T1, T4 only). The §Form re-test before every KEEP / DELETE / REVISE verdict is the operationalisation of G1.
- **Position-gate (G5) on adds.** Every add carries a position-category note in its decision-shard justification (approach-zone / peak / trailing-edge / post-peak / quiet-beat / denouement). At the final 5-10% of the stream, if any other touched entry at the same anchor closes in archival/accounting/filing register, at least one entry at that anchor must hold the prior peak's consequence live.

### R2 judges (five in the parallel block)

**R2.1 narrator-interest (POV impersonator, judge mode)** — POV stack + behavior cards + nine R1 facet files + cite-index + `rubric-narrator-interest.md`. Override impersonator: facet-judge mode. Decide per existing NI entry: KEEP / DELETE-<reason>. Adds: peak-bones and rising-zone anchors with memory/feeling but no NI, or lonely-entry adjacency where NI would license co-location. Add-cap 5. Out: mutated `interest-narrator.md` + `_inflight-r2/proto-lines-narrator.md` + decision-shard `staff/interest-narrator/r2-decision-shard.md`.

**R2.2 memory (POV impersonator, fresh fork)** — POV stack + nine R1 facet files + cite-index + warehouse cond-* cards (monuments) + `rubric-memory.md`. Decide per existing memory: KEEP (monument-grade callback, NI-spine co-cited, target reference resolvable) / DELETE (functional callback, NI-spine missing without defense, unresolvable target reference). Adds: rhythm-shape transitions and peak-bones without memory; NI-present + memory-absent. Hard fences: no Earth-Bet proper nouns. Add-cap 5. Out: mutated `memory.md` + `_inflight-r2/proto-lines-mem.md` + decision-shard `staff/memory/r2-decision-shard.md`.

**R2.3 feeling (per-character impersonators ×N, judge mode)** — for each `cast:` slug, one impersonator dispatch in the same parallel block (POV and non-POV both eligible). Character stack + nine R1 facet files + cite-index + `rubric-feeling.md`. Decide per existing feeling entry for that character: KEEP (somatic-tell card-matched, multi-justification ≥3 of 5, scene cap ≤1) / DELETE (duplicates POV NI register, forbidden vocabulary, multi-justification fail, cap breach). Adds: memory or NI co-cite where somatic register would land. Add-cap 5 per character. Out: mutated `feeling-<slug>.md` slice + `_inflight-r2/proto-lines-feel-<slug>.md` + decision-shard `staff/feeling/r2-decision-shard-<slug>.md`.

**R2.4 metaphor (editor, judge mode)** — nine R1 facet files + cite-index + `rubric-metaphor.md`. Decide per existing metaphor: KEEP (anchor resolves post-cascade, tens-discipline holds, register is callback or dark-humor) / DELETE (anchor unresolvable, AP3 anti-duplication, AP7 default-refuse at tens ≠ 3). Resolve any provisional `licensed-by:` hints from R1 — KEEP-with-anchor-rewrite if it resolves, DELETE-unanchorable otherwise. Adds: ≥2 supporting layers cleanly clear; refuse-by-default. Add-cap 3. Out: mutated `metaphor.md` + `_inflight-r2/proto-lines-meta.md` + decision-shard `staff/metaphor/r2-decision-shard.md`.

**R2.5 exposition (exposition-author, judge mode)** — all R1 facet files (including the now-locked lens facets) + cite-index + audience persona cards + cross-episode register + `rubric-exposition.md`. Override exposition-author: facet-judge mode. The R2 judge is the critical pass that converts the audience-pure R1 output into graph-trusted final state. Decide per existing exposition entry: KEEP (gap still real after lens-facets reviewed; no other facet covers it; sources still resolve) / DELETE (lens facet covers — NI established the term in body, mem carries the callback, loc-state covered the scene-orient) / REWORD (gap is real but surface chose heavy render-as where lighter would do; or anti-jargon list growth in R1 cull mandates re-rendering). Adds: rare — when R1 lens-facet author chose NOT to cover a register exposition can pick up. Add-cap 3. Provisional-anchor resolution: R1 entries with descriptive anchor-hints get bound to actual proto-line IDs via cite-index walk. Scene-open-orient fire-rule re-validated against locked graph (the s01e01 dogfood lesson: Phase 2 exposition refused 11 of 11 scene-orient entries that Phase 1 had authored, because NI/loc-state covered them; R2 enforces this routing). Out: mutated `exposition-<slug>.md` + `_inflight-r2/proto-lines-exposition.md` + decision-shard `staff/exposition-author/r2-decision-shard.md`.

**R2.6 dialogue (dialogue-writer, judge mode, per-character ×N speaking characters)** — for each speaking character in the cast, one fork in the same parallel block (judge mode). Reads: the dialogue file under judgment + its drafts sidecar; all nine other R1 facet files + cite-index; behavior card stack (re-loaded); speaker persona + ltm + stm + state; `staff/dialogue-writer/rubric-dialogue.md`. **Graph payload filtering (rubric § contamination disciplines):** facet entries passed as facts-not-prose (somatic-tell text / monument-name / interest-focus / vibe-target fields only, stripped of rationale); speaker's own slices (`feeling-<speaker>`, `state-updates-<speaker>`, NI iff speaker is POV) first-class; other characters' slices as one-line abstracts. Decide per existing dialogue entry: KEEP (card signature affirmatively demonstrated; facet-license citations resolve in locked graph; somatic-tell / monument adjacency claimed by chosen draft is structurally present; no hard-fence violation; behavior monument rules respected) / DELETE-<reason> (card signature missing — inoffensive ≠ on-card; forbidden vocabulary; facet-license citation does not resolve; hard-fence proper-noun hit; DEDUP with NI / feeling / memory rendering same content) / REWRITE (internal mini-V3 surfaces closable seam; delete + new ID with revised draft citing different §-section or different facet license). Add-cap: 3 per character (adds are exceptional — R1 covers speaking beats; R2 adds only when a beat is genuinely silent that card + graph license a line for). Out: mutated `theater/dialogue/<character-slug>.md` + `_inflight-r2/proto-lines-dialogue-<character>.md` + decision-shard `staff/dialogue-writer/r2-decision-shard-<character>.md`.

Vibes is not re-judged in R2; the showrunner-authored R1 vibes facet stands as-is unless the audit flags it. (R2 vibes judging is a future extension.)

---

## Phase 4 — FANIN: decision-log consolidate + merge + cite-index

### 4a. Decision-log consolidation

Concatenate the six layer shards (R2.1 NI, R2.2 memory, R2.3 feeling — all per-character shards merged in `cast:` order, R2.4 metaphor, R2.5 exposition, R2.6 dialogue — all per-character shards merged in `cast:` order) into `active-project/theater/facets/.r2-decisions.md` under one `## <facet-slug>` heading per shard. Sum the per-shard `f-r2-counts:` into a single top-of-file frontmatter block per `schemas/audit-report.schema.md` § Consolidated file:

```yaml
---
report: r2-decisions-consolidated
episode: <slug>
date: <ISO date>
shards: [<list of source shard paths>]
f-r2-counts: {f-r2-1: <sum>, f-r2-2: <sum>, f-r2-3: <sum>, f-r2-4: <sum>}
discipline-fails: <count>
---
```

The consolidated frontmatter is what `staff/orchestrator-critic/card.md` Phase 6 verdict reads (A2 F7 emission contract; `f-r2-1 > 0` is HARD trips F7-r2; `f-r2-2 + f-r2-3 + f-r2-4 > 2` is SIGNAL B7).

### 4b. Arbiter glue (T1 / T4 over shards)

Main session is the arbiter (per `design/shoot-v2/r2-judge-tuning/C-arbiter-protocol.md`). Read each shard end-to-end and run the two retained triggers:

- **T1 — Rubric-label-heavy, entry-specific-light.** Verdict justification is primarily rubric citations without naming concrete entry content. Intervention: re-dispatch the layer's author with — "What specifically in this entry produced that verdict? Quote the phrase." Fresh fork; rewrites the verdict's justification only.
- **T4 — Niche-driven add justification.** Add-justification works backward from "the graph reveals a niche" rather than forward from "the at-rest reading wants this entry." Intervention: re-dispatch with — "Set aside the cite-index. Read the proto-line. Does it want this entry?"

T2 / T3 / T5 / T6 are deferred until B2a evidence supports them. **Bound:** ≤2 intervention rounds per verdict. After two interventions without a non-mechanical justification, log as **DISCIPLINE-FAIL** in the shard and surface in Phase 6. **No interventions on hard-fence violations.** Append per-shard arbiter trace inline beneath the affected verdict.

### 4c. Merge + cite-index rebuild

```bash
python3 active-project/staff/cite-index/build_cite_index.py <episode-slug>
```

The tool reads `_inflight-r2/` instead of `_inflight/` on the second invocation. (Implementation: the tool reads any `_inflight*/proto-lines-*.md` files present; both directories are consumed if both exist. After Phase 4 the `_inflight/` directory may be pruned; `_inflight-r2/` is the live working set.)

Body-integrity, citation union, slice consolidation, stale-citation check, cite-index rebuild — same five sub-phases as Phase 2. The R2 facet files are already mutated in place by the R2 judges; this run merges their proto-lines copies into the canonical and refreshes the cite-index against R2's KEEP / DELETE / ADD outcome.

Set status `faceted-r1` → `faceted-r2` in showrunner memory.

### 4d. Scene-map validation (URI-SCENE-WINDOW, downgraded from derivation under URI-SUBSTANCE-OVERHAUL 2026-05-17)

Under the substance overhaul, `/and-write` Phase 7 emits the scene-map facet directly from `chapters[].scenes[]` in showrunner memory. Phase 4d **no longer derives** — it validates.

**Validation procedure:**
1. Confirm `active-project/theater/facets/scene-map-<book>-<chapter>.md` exists (it should — Phase 0 step 4 already pre-checked). If absent at this point, abort.
2. Read the scene-map. Validate the URI-SCENE-WINDOW coverage check: every bone in `theater/bones/<book>-<chapter>.md` lands in exactly one scene's `@<start>-@<end>` range; no gaps; no overlaps; no dangling anchors; no duplicate scene labels; frontmatter `total-scenes` / `total-bones` match body.
3. Validate the tens-aware fields (`rhythm-shape`, `peak-bones`, `peak-shadow-bones`, `fusion-eligible-runs`, `protected-patterns`) are populated per `schemas/scene-map.schema.md` if the facet was emitted with them. Under the substance overhaul these fields are derived from the per-bone `substance_delta.axis_moves.magnitude` (treated as the new pressure-signal) instead of tensometer entries; `/and-write` Phase 7 computes them at emit time.
4. **Coverage failures HARD-fault** and surface to Phase 5 audit. The orchestrator does not derive a fallback — under the new chain, scene-map emission is `/and-write`'s job, and a missing/broken scene-map indicates upstream did not run cleanly.

The tensometer-fallback path (which previously parsed `tensometer-<slug>.md`'s scene-footer when the scene-map facet was missing) is removed as dead code.

---

## Phase 5 — AUDIT: single auditor dispatch

Dispatch **auditor** (fork) with the full graph:

**Read inputs:**
- Proto-lines: `active-project/theater/proto-lines/<slug>.md` (canonical, post-R2).
- All nine facet files at `active-project/theater/facets/` (`location-state`, `interest-narrator`, `sensory`, `state-updates`, `memory`, `feeling`, `metaphor`, `vibes`, `exposition-<slug>`).
- Scene-map: `active-project/theater/facets/scene-map-<book>-<chapter>.md` (upstream-emitted by `/and-write` Phase 7; validated at Phase 4d).
- All per-character dialogue files at `active-project/theater/dialogue/<character-slug>.md` (one per speaking character).
- All per-character dialogue drafts sidecars at `active-project/staff/dialogue-writer/<character-slug>.drafts.md` (for CONSTRAINT § citation-completeness).
- Cite-index: `_cite-index.md` (post-R2).
- R2 decision-log: `.r2-decisions.md`.
- All active warehouse cards (`active-project/warehouse/*.card.md`) — for constraint checks against cond-* and loc-* cards.
- All behavior cards in scope (`cards/dialects/<character-slug>.card.md` and composition stack via margit) for every speaking character — for CONSTRAINT § behavior-card-compliance checks.
- Series + season plans (showrunner memory) — for series-law constraint checks.
- Schemas: `facet.schema.md`, `dialogue.schema.md`, `audit-report.schema.md`.

**Forbid loading:** behavior cards, vibes-as-bias, audience personas (except for exposition CONSTRAINT § license-completeness check, which requires loading the persona slugs to verify `licensed-by:` references resolve — load names only, not content), source prose. The auditor reads the graph mechanically against constraints, not aesthetically.

**Mode: flag-only.** Until the auditor itself is tuned for delete-authority, findings are routed back to facet authors as flags. Once tuned (separate work), HARD findings will be executed as deletes (with citation cascade).

### Audit classes (twelve; with exposition-specific rules layered into FREQUENCY-BAND, CONSTRAINT, RUBRIC-FIDELITY, and AP-SCAN)

1. **STRUCTURAL** — schema/format/integrity (headers, line shape, ID monotonicity, anchor resolution, bidirectional citation, proto-body integrity). **Dialogue-specific:** every dialogue entry's `@<proto-line-id>` resolves; every `<character-slug>:<id>` citation in proto-lines resolves to an existing dialogue entry; entry-ID monotonicity per-character (`schemas/dialogue.schema.md` § Entry fields); behavior-card slug in dialogue file header matches a real card.
2. **FREQUENCY-BAND** — per-rubric quantitative gates (sensory 3-6%; memory 5-12%; feeling 2-5%/char; metaphor 0-3%; NI 15-25%; **exposition 1-5% per episode, episode-open ≤4 entries, first-mention ≤12 entries, scene-open-orient ≤1 per scene**; **dialogue sparsity unconstrained — content-driven, not flag-driven — but per-anchor cap ≤3 utterances and ≤1 utterance per speaker per anchor unless deliberate single-turn split documented in drafts sidecar**).
3. **METADATA-INCONSISTENCY** — file headers / round-notes / r1_to_r2 summary lines that contradict actual content.
4. **CURVE-SHAPE** — evaluates the chapter's pressure-signal curve against the `dramatic_shape` declaration in showrunner memory + per-scene `rhythm-shape` from the scene-map. SHAPE-OK when scene-level `rhythm-shape` values are coherent with the chapter-level `dramatic_shape` (e.g., a `hinge` chapter shows scene-level `flat-low` zones building toward a `peak-bones` hinge beat with `resolving` afterward; a `rising` chapter shows ascending `rhythm-shape` values across scenes; a `denouement` chapter shows predominantly `resolving` and `release-only` scenes). SHAPE-FAIL when the scene-map's rhythm-shape sequence contradicts the declared dramatic_shape (e.g., a `hinge` chapter with no `peak-bones`-class bone anywhere, or a `rising` chapter that begins with `resolving` scenes).
5. **CONTRADICTION** — two facet entries set incompatible state on the same anchor; both flagged.
6. **DEDUP** — cross-facet-same-anchor / within-facet-different-anchor / within-facet-same-anchor. **Dialogue-specific:** utterance content rendered by NI / feeling / memory at the same anchor (the speaker says aloud what another facet already shows — one yields; default is the lens facet yields to dialogue when the speaker uses the same phrasing the lens would, since dialogue is verbatim render and lens is render-as signal).
7. **SUPERFLUOUS** — lonely entries that don't survive rubric scrutiny. Convention: bones in `rhythm-shape: flat-low` zones and off-anchor vibes are never superfluous. SUPERFLUOUS evaluation must run the rubric's own three-axis test (necessity / interestingness / frugality) on the entry's own merits — displacement-logic ("entry-X passes because it displaced entry-Y") is not a valid SUPERFLUOUS defense.
8. **CONSTRAINT** — cross-facet contract violations: memory without NI-spine; metaphor without resolvable `licensed-by:` anchor; feeling duplicating POV NI; vibes with unresolvable or forward-citing `licensed-by:`; state-updates `<old>` contradicting prior state; POV-perceptual access on NI; **exposition source-traceability (every claim in `<gloss-text>` must trace to a `<sources>` entry; unresolvable claim → HARD); exposition license-completeness (every entry's `<licensed-by>` field must name ≥1 persona-card slug + a specific gap-claim — missing/malformed → SIGNAL); exposition scene-orient fire-rule (`scene-open-orient` entries must satisfy (a) time-skip-blank-precedes + (b) loc-state-silent-at-anchor + (c) NI-silent-on-time-or-place-in-first-2-anchors-of-new-scene; any violation → HARD because the entry fires when lens should carry); exposition re-gloss check (cross-reference `<key>` against `active-project/staff/exposition-author/glossed-terms.md`; hit → HARD); exposition first-mention-character coverage (walk proto-lines and identify every named individual appearing in narrator-prose for the first time — by definite description like `the carter` / `the dock-runner` / `the lord's-man` / `the maester` or by name like `Tom` / `Ben`. For each, verify a `first-mention-character` exposition entry exists keyed to that anchor. POV character excluded — covered in episode-open preamble. Dialogue-only mentions excluded — a name uttered by a speaker is the speaker's reference, not a prose introduction. Missing entry → HARD: `[exposition:--] @<anchor> — first-mention-character-coverage — no gloss for <character-noun-phrase> on first prose mention`)**; **dialogue behavior-card-compliance (every utterance respects the speaker's behavior card §hard fences, §forbidden vocabulary, §monument rules; violation → HARD); dialogue citation-completeness (every chosen-mark entry in the drafts sidecar has both card-signature §-cite AND facet-license citation post-R2; missing one axis → SIGNAL; missing both → HARD); dialogue objective-anchoring (every entry's `<objective>` field is non-empty and matches a speech-act the proto-line bone licenses — missing/unmatched → SIGNAL); dialogue-coverage (URI-DIALOGUE-COVERAGE-GATE — every Phase 0 `speech_bones` ID is cited by ≥1 `<character-slug>:<id>` token on the canonical proto-lines, AND every Phase 0 `speakers` slug has a non-empty `theater/dialogue/<slug>.md` file. Bare speech bone (a `<X> speaks to <Y>` proto-line with zero dialogue citations post-R2) → HARD per bone. Missing speaker file (a speaker slug from Phase 0 inventory with no dialogue file on disk) → HARD per speaker. This is the structural gate that prevents the FAULT-DIALOGUE-MISSING failure mode — emit `[dialogue:--] @<proto> — dialogue-coverage — bare speech bone: <subject> speaks to <object>` and `[dialogue:--] @-- — dialogue-coverage — missing speaker file: <slug>`.)**; **scene-map coverage (URI-SCENE-WINDOW, 2026-05-13 — every bone in `proto-lines/<slug>.md` MUST fall inside exactly one scene's `@<start>-@<end>` range in `theater/facets/scene-map-<slug>.md`. Uncovered bone → HARD `[scene-map:--] @<id> — scene-map-coverage — gap`. Double-covered bone → HARD `[scene-map:--] @<id> — scene-map-coverage — overlap with scene-<labels>`. Dangling anchor (scene's `@<start>` or `@<end>` does not match any proto-line ID) → HARD `[scene-map:--] scene-<label> @<id> — scene-map-coverage — dangling-anchor`. Duplicate scene-label → HARD. Frontmatter `total-scenes` / `total-bones` mismatch with body → HARD. Per the schema's coverage validation table.)**; **scene-map per-scene caps (URI-SCENE-WINDOW — sensory ≤3 per scene, feeling ≤1 per character per scene, metaphor ≤1 cross-character per scene, exposition `scope: scene-open-orient` ≤1 per scene. Per-scene boundaries read from `scene-map-<slug>.md`'s ranges, not inferred from prose. Breach → HARD per facet type with scene-label cited in the finding: `[<facet>:<count>] scene-<label> @<bone-range> — per-scene-cap — <count> entries exceed cap of <N>`.)**; **loc-state transition-run continuity-license (URI-SCENE-RHYTHM, 2026-05-13 — per `design/shoot-v2/rubric-location-state.md § Transition-run continuity license`. Continuity-carry entry (loc-state entry whose sensory note begins `continuity-from <prior-loc-state-id>:`) is valid only when (a) the entry's anchor bone is inside a scene-map `fusion-eligible-runs` range AND (b) the scene's `rhythm-shape` is `flat-low` / `resolving` / `release-only` AND (c) the `<prior-loc-state-id>` resolves to an earlier loc-state entry in the file AND (d) no other continuity-carry entry exists in the same fusion-eligible-run. Violations: (a) → HARD `FAULT-LOC-STATE-CONTINUITY-MISPLACED`; (c) → HARD `FAULT-LOC-STATE-CONTINUITY-DANGLING`; (d) → HARD `FAULT-LOC-STATE-CONTINUITY-OVERPACK`; (b) is enforced by the licensing rule (entry should not have been authored on a momentum scene; flagged at audit as HARD-misplaced). Carry-note duplicating prior loc-state's sensory note verbatim → SIGNAL `WARN-LOC-STATE-CONTINUITY-NO-INCREMENT`.)**.

   **Earth-Bet hard-fence proper-noun scan (URI-AUDITOR-CONSTRAINT-CALIBRATION, 2026-05-11; dialogue extension 2026-05-12):** case-insensitive substring scan against the Earth-Bet proper-noun list across **every text field** of every facet entry **AND every dialogue utterance** — including but not limited to: NI free-text rationale, memory target-reference glosses (the parenthetical `(earth-bet: ...)` and the `s<NN>e<NN>:<id>` slug components alike), metaphor `licensed-by:` notes and figure text, vibes entity-target-primary fields, feeling somatic-tell text, state-updates field names AND `<old>` / `<new>` values, sensory disambiguation notes, loc-state composite-state and observable-affordance fields, **dialogue `<utterance>` text and `<objective>` text**. Slug components matter: a margit-referral slug embedding `khepri-` or `gold-morning-` is a hard-fence violation even when no full English phrase is rendered. Names to scan (non-exhaustive starter list — refresh against the canonical Earth-Bet hard-fence list at every audit): Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil, Tattletale, Bitch, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea. Any hit is HARD; emit `[<facet>:<id>] @<proto> — earth-bet-hard-fence — <name> at <field>: "<surrounding-text>"`.
9. **AP-SCAN** — per-rubric anti-pattern mechanical scan (memory AP-functional-callback, feeling AP-named-feeling-vocab, metaphor AP3 / AP7 / AP12, vibes AP-multi-source / AP8 sentence-parsability, etc.). **Dialogue anti-patterns (v1 round-trip findings, lifted from `rubric-dialogue.md`):** AP-chassis-contamination (em-dash + semicolon spine on non-Taylor speakers — Taylor's chassis bleeding across cards); AP-modern-hr-speak (procedural/compliance-English in Westerosi register: "labor-eligibility," "procedural grounds," etc.); AP-deposition-cadence (legalistic Q-and-A cadence in non-administrative speakers); AP-nominalization-substituting-plain-English (compound noun-phrases where colloquial register's card calls for verb-driven clauses).

   **Severity calibration (URI-AP-SCAN-SATURATION, 2026-05-19).** An AP-SCAN hit is normally SIGNAL. It escalates to HARD when the per-template / per-construction hit count reaches saturation in a sparse-by-design facet — specifically, when `hits / total-entries ≥ 0.40` in a facet whose FREQUENCY-BAND ceiling is ≤ 25%. Rationale: a 3-of-7 template repetition in a 15-25%-density facet is template-saturation (not isolated misfire) and produces the "reading the construction before the content" failure mode the b01c01 audience flagged on narrator-interest. Threshold pinned at 40% to keep 2-of-7 (29%) advisory and 3-of-7 (43%) blocking. Emit `[<facet>:--] AP<N> <name> — saturation: <hits>/<total> in sparse-by-design facet (band ≤ 25%)`.
10. **TASTE-FLAG** — audience-attack-anticipation candidates: atmosphere-thin / momentum-stall / voice-fidelity. Signal-only; feeds bidirectional tuning loop.
11. **PILE-UP REVIEW** — proto-lines with >4 co-located facets; verdict per pile-up: warranted | over-decoration.
12. **RUBRIC-FIDELITY** (URI-RUBRIC-FIDELITY, 2026-05-19) — per-facet rubric-fidelity mechanical scan. For each facet's authored entries, verify against the facet's rubric's enumerated ACCEPT / REJECT signatures, anti-patterns, file-level shape gates, and cross-facet co-citation requirements. The audience-gate fired faults the auditor's mechanical scan missed in b01c01; this class closes the gap by reading the rubrics' REJECT-signature enumerations as auditor rules rather than as audience-only taste calls. Four scan dimensions:

    (a) **Per-entry signature scan.** Verb-class / value-class / field-class checks against the rubric's enumerated ACCEPT and REJECT signatures. Example: loc-state entry's anchor proto-line verb must be in `rubric-location-state.md § ACCEPT signatures` (transitional/positioning verbs); anchor verb in the REJECT enumeration (stillness/hold beats: `the cart sits`, `threads the needle`, persistence-of-condition) → HARD `[<facet>:<id>] @<anchor> — rubric-fidelity-verb-class — anchor verb '<verb>' fails rubric-<facet>.md ACCEPT enumeration`. Similarly: state-updates `<new>` value containing registration vocabulary (`noticed`, `registered`, `awareness`, `baseline-new-faces`) on an actor extension-field → HARD `[<facet>:<id>] @<anchor> — rubric-fidelity-anti-pattern — registration-as-state (rubric § anti-pattern #1)`.

    (b) **Per-facet file-level shape gate.** Each rubric's "Curve-shape rubric (file-level)" section enumerates file-level requirements distinct from the run-level CURVE-SHAPE class. Examples: memory-flags doubled-register test (at least one Earth-Bet displacement fire AND at least one Westerosi-monument clamp fire; single-register file → HARD `[memory:--] file — rubric-fidelity-doubled-register — single register only`); state-updates file-level POV co-citation completeness (every `actor:<POV>.*` entry pairs with a narrator-interest entry on the same beat; total-coverage gate fires HARD when ≥1 entry is uncovered); sensory modality distribution (modality floor: ≥2 distinct modalities; dominance ceiling: no single modality ≥ 67% of fires when total ≥ 3); per-facet quiet-beat / peak-beat distribution against scene-map fields (memory-flags concentrate in `flat-low`/`resolving` zones, forbidden by default on `peak-bones` except under displacement-clamp; NI concentrates on `peak-bones` and `rising` zones).

    (c) **Per-entry cross-facet co-citation symmetric checks.** Augments CONSTRAINT's existing checks with the symmetric pairs each rubric explicitly names. The pre-overhaul CONSTRAINT class enumerated `memory without NI-spine` but did not enumerate the symmetric `state-updates actor:<POV>.* without NI co-citation` even though `rubric-state-updates.md § Cross-facet contract` states the same REQUIRED / REJECT rule. RUBRIC-FIDELITY reads the rubric's cross-facet contract sections and enforces every named co-citation. Each missing co-citation → HARD `[<facet>:<id>] @<anchor> — rubric-fidelity-cross-facet-co-citation — <rule-citation>`.

    (d) **Card-resolution checks on target / licensed-by / slug fields.** Every facet entry that names a card slug (memory `target-reference`, metaphor `licensed-by`, vibes `licensed-by`, state-updates `target` for prop/condition refs) must resolve to an existing card in `cards/` or `active-project/warehouse/`. Free-text glosses with no resolvable slug → HARD `[<facet>:<id>] @<anchor> — rubric-fidelity-card-resolution — <field> missing margin monument card`. Auditor appends a margit-referral candidate slug to the finding (mechanism-descriptive form derived from the gloss).

    **Severity:** HARD by default for rubric-enumerated REJECT signatures, named anti-patterns, named file-level gate failures, named cross-facet co-citation gaps, and unresolved card slug references. SIGNAL for borderline cases the rubric leaves explicitly unspecified or marks "exceptional with documented author defense" (when defense is absent, escalate to HARD; when defense is present in the entry's notes, accept as SIGNAL).

    **Source enumeration.** Seeded from each facet rubric's §"Anti-patterns" + §"Curve-shape rubric (file-level)" + §"Cross-axis tests" + §"ACCEPT signatures" + §"REJECT signatures" + §"Cross-facet contract" sections of: `rubric-memory-flags.md`, `rubric-sensory.md`, `rubric-state-updates.md`, `rubric-narrator-interest.md`, `rubric-location-state.md`, `rubric-feeling.md`, `rubric-metaphor.md`, `rubric-vibes.md`, `rubric-exposition.md`, `rubric-dialogue.md`. The auditor enumerates these sections at audit time and applies each rule as a mechanical check. New rubric rules added later get picked up automatically by the next audit.

    **Relationship to other classes.** RUBRIC-FIDELITY is distinct from CONSTRAINT (which holds pipeline-level / cross-document contracts: schema integrity, EARTH-BET fence, scene-map coverage, exposition source-traceability) and from AP-SCAN (which holds lexical anti-pattern scans without rubric-grounded REJECT enumeration). When a check appears in both CONSTRAINT and a rubric's REJECT section, CONSTRAINT takes precedence (older citation). When a check appears in a rubric's REJECT section without CONSTRAINT enumeration, RUBRIC-FIDELITY fires it.

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
- [facet:id] — <kind> — <description>.

## FREQUENCY-BAND findings (<count>)
- <facet>: actual <n%>; band <range>%; <within | breach-low | breach-high>.

## METADATA-INCONSISTENCY findings (<count>)
- <file>: <header-claim> contradicts <file-content-fact>.

## CURVE-SHAPE verdict
- Episode-level: <SHAPE-OK | SHAPE-FAIL with named failure mode>.
- Per-scene: scene-1 <peak-present | no-peak>, ...
- Adjacency: <count> 1→3 jumps; <count> 3→3 sequences.
- Flatlining: <count> stretches of 30+ contiguous beats.

## CONTRADICTION findings (<count>)
- [facet:id] @<proto> — paired with [facet:id] @<proto>.

## DEDUP findings (<count>)
- [facet:id] @<proto> — duplicates [facet:id]; type: <kind>.

## SUPERFLUOUS findings (<count>)
- [facet:id] @<proto> — lonely; rubric scrutiny: <pass | fail with rationale>.

## CONSTRAINT findings (<count>)
- [facet:id] @<proto> — <constraint name> — <violation>.

## AP-SCAN findings (<count>)
- [facet:id] @<proto> — AP<N> <name> — candidate violation.
- (Exposition AP-SCAN entries: anti-jargon-hit / hollow-prose-hit / asinine-pattern-hit / new-plot-content / author-meta / voice-fault.)

## TASTE-FLAG findings (<count>)
- [facet:id] @<proto> — <atmosphere-thin | momentum-stall | voice-fidelity> — <rationale>.

## PILE-UP REVIEW (<count>)
- @<proto> (<n> facets) — verdict: <warranted | over-decoration> — <rationale>.

## RUBRIC-FIDELITY findings (<count>)
- [facet:id] @<proto> — rubric-fidelity-<verb-class | anti-pattern | doubled-register | cross-facet-co-citation | card-resolution> — <rubric § citation> — <description>.

---

## Audit summary
- Total entries reviewed: <count>
- HARD classes: STRUCTURAL <n>, CONTRADICTION <n>, DEDUP <n>, SUPERFLUOUS <n>, CONSTRAINT <n>, RUBRIC-FIDELITY <n>
- SIGNAL classes: FREQUENCY-BAND, METADATA-INCONSISTENCY, AP-SCAN, TASTE-FLAG, PILE-UP REVIEW (AP-SCAN escalates to HARD on saturation per URI-AP-SCAN-SATURATION; RUBRIC-FIDELITY borderline-with-defense remains SIGNAL)
- CURVE-SHAPE: <verdict>

## Routing
For each finding, name the facet author. Flag-only: no executes.
```

**Auditor return to orchestrator:** path to report; finding counts per class; one-line headline (CLEAN | FINDINGS-PRESENT with count).

**Phase 5 gate:** HARD = 0 required before Phase 5b fires. SIGNAL findings are advisory (do not block Phase 5b). If HARD > 0, dispatch fixer with the audit report; re-fire Phase 5 until HARD = 0 or remediation budget (1 pass) exhausts. Remediation cap-burn at HARD > 0 escalates to orchestrator-critic NOT-SUCCESSFUL.

On Phase 5 clean, set showrunner-memory status: `faceted-r2` → `audited-r1-mechanical`. The episode is NOT done until Phase 5b also clears.

---

## Phase 5b — AUDIENCE-GATE: per-facet adversarial reviewers (BLOCKING)

The final gate. The auditor's mechanical scan caught what mechanical scans can catch; Phase 5b is where adversarial readers attack the locked graph through their lenses and the pipeline either earns ACCEPT or routes back to fixer for another cycle.

### Reviewer assembly (variable per facet)

For each of the ten facets **plus dialogue (per-character)**, the orchestrator picks the reviewer set:

1. **Specialist personas** — if `staff/audience/<slug>/card.md` files exist with `target-facet: <facet>` in frontmatter, those specialists fire as the reviewer set for that facet. Example: the `sensory` facet currently has `sensory-disambiguation-pedant`, `sensory-modality-coverage`, `sensory-old-state-reader`.
2. **Active project audience (fallback)** — for facets without specialists, the 3 active personas under `active-project/audience/<slug>/card.md` fire in graph-aware adversarial mode (NOT prose mode). Each persona reads the facet entries through its own lens (atmosphere / register / source-fidelity / etc.).

Reviewer membership is recorded in the verdict file. New specialist personas authored later get picked up automatically by the next /and-facets run.

### Dispatch shape

One parallel Agent block per facet, all facets fired concurrently. For nine facets + dialogue-per-character at three reviewers each (specialists or fallback), that is up to (9 + N speaking characters) × 3 concurrent audience dispatches in a single message. (`vibes` may run with a single reviewer dispatch if the audience cards do not yet hold facet-attack rubrics for it; verdict notes which facets ran undermanned. Dialogue per-character runs with full 3-reviewer dispatch using the active-project audience until specialist dialogue personas are authored — see open question in `design/shoot-v2/dialogue-tuning-v2.md`.)

### Dialogue reviewer protocol (V2 + V3, per `staff/dialogue-writer/rubric-dialogue.md`)

Dialogue's audience-gate inherits v1 round-trip tuning. Per reviewer per character file, **two stages** in the same verdict file:

**Stage 1 — V2 strict affirmative-demonstration.** Per entry: ACCEPT (Q1 — line affirmatively demonstrates ≥1 card signature with §-citation; Q2 — line does not violate any card §forbidden vocabulary / §forbidden cadence / §hard fence) / REVISE / FAIL. Inoffensive lines fail Q1. On-card-but-violating fails Q2.

**Stage 2 — V3 adversarial seam-finding.** For every line, accepts included, this persona produces its strongest hostile counter-argument from its lens (atmosphere / board-move / voice-precision — or facet-equivalents from the active audience). Persona-distinct constraint: seams must differ by lens, not generic craft-criticism. Facet evidence is fair attack surface: the chosen draft cites facet-licenses; the seam may attack those citations directly ("the slip claims `feeling-taylor:7` as license, but that entry is a held-breath tell that doesn't carry register-slip in stitch").

Aggregation: strict 3-of-3 ACCEPT per character (URI-AUDIENCE-AGGREGATION-RULE). Single dissent fails the character. Convergence on failure: fixer dispatches dialogue-writer in **defense-or-revise mode** — defended accepts stay; revisions get multi-draft + chosen-mark + rejection-notes treatment per the rubric.

**Exposition is the canonical audience-gate test.** Because the exposition-author IS audience-modeled by construction (the union-of-personas gap test is its central authoring discipline), the audience-gate reviewers have a stronger relationship to exposition than to any other facet. The three personas each read the exposition entries against their own reading-experience and answer:
- Did the gloss successfully orient me to the term/object/place/circumstance?
- Or did it leave me still confused or, conversely, over-explain in a way that disrupted the prose?
Reviewers may also propose ADDS: "I'm cape-fic; I needed a gloss for `kingsguard` at @<N> and there isn't one." This audience-side ADD-surfacing is unique to exposition; for other facets, ADDs from reviewers are exceptional. The exposition author has final call on the ADD's gloss content but cannot refuse an audience-flagged ADD without escalating via TASTE-FLAG → AP-SCAN promotion. Single dissent blocks: 3-of-3 ACCEPT required to clear.

### Read inputs per reviewer

- The facet file under review (`<facet>.md` or per-character slice for `feeling`/`state-updates`).
- The canonical proto-lines file `active-project/theater/proto-lines/<slug>.md` (already annotated with `[<facet>:<id>]` citations from R1+R2 merges — this is the working "stitcher preview" the audience attacks).
- The cite-index `active-project/theater/facets/_cite-index.md`.
- The facet's own rubric (e.g. `design/shoot-v2/rubric-memory-flags.md`).
- The auditor's Phase 5 report (so the audience knows what the mechanical scan caught and can deliberately attack the seams the auditor cannot articulate).
- The reviewer's own persona card.

### Forbidden inputs

- Other facet rubrics not relevant to the under-review facet.
- Source prose / draft stitch (Phase 5b reads the graph layer, not generated prose).
- Other reviewers' verdicts (each reviewer attacks independently; cross-reviewer cross-talk happens at aggregation time, not at reading time).

### Per-reviewer output

Each reviewer produces a single short verdict file under `active-project/staff/audience/<persona-slug>/<facet>-r<N>-verdict.md`:

```yaml
---
reviewer: <persona-slug>
facet: <facet>
cycle: <N>           # 1, 2, or 3
episode: <slug>
date: <YYYY-MM-DD>
verdict: <accept | revise | fail>
---

# Verdict reasoning

<1-3 sentences of direct adversarial reading — what the entries (or the graph) actually do or fail to do through this reviewer's lens. Do not primarily cite rubric clauses; primary attacks are direct readings.>

# Entry-level callouts (revise / fail only)

- [<facet>:<id>] @<proto> — <direct reading attack — what specifically lands wrong, in this reviewer's voice>.
- ...

# Convergence trace (orchestrator-critic input)

<For each callout, note whether the Phase 5 auditor independently flagged the same entry. List the auditor finding IDs that overlap. This is what closes the bidirectional-loop criterion structurally.>
```

### Aggregation

Per facet:
- **3-of-3 accept** → facet passes.
- **any revise / fail** → facet fails this cycle; route callouts to fixer (or facet author, if cross-cutting rewrite is needed).

**Strict-aggregation enforcement (URI-AUDIENCE-AGGREGATION-RULE, 2026-05-11).** Aggregation is performed by the orchestrator from the per-reviewer verdict files on disk. The orchestrator does NOT delegate aggregation to an audience-subagent. The 2-of-3 majority rule that applies to line and plan review (`.claude/agents/audience.md`) does NOT apply here — a single dissenting persona fails the facet. An audience-subagent that returns a single aggregated verdict instead of writing per-reviewer files has drifted; re-dispatch with explicit "write one verdict file per persona under `active-project/staff/audience/<persona-slug>/`; do not aggregate" instructions.

Across all facets:
- **all 9 facets + all per-character dialogue files pass** → Phase 5b passes. Proceed to Phase 6.
- **any facet or any character dialogue fails** → enter remediation cycle.

### Remediation cycle

1. Aggregate revise/fail callouts across all reviewers. Dedupe by `[<facet>:<id>]`.
2. Dispatch **fixer** with the consolidated callouts + the facet rubrics. Fixer routes per-entry — small revisions to the facet file directly; cross-facet conflicts to the responsible author via Agent.
3. Re-fire Phase 5 (auditor, full eleven-class scan) — fixer changes may surface new mechanical findings.
4. Re-fire Phase 5b (audience, all facets that did not 3-of-3 accept in the prior cycle; facets that passed do not re-fire).
5. Increment cycle counter.

### Reviewer-stall handling (URI-AUDIENCE-CYCLE-2-MEMORY-STALL, 2026-05-11)

A reviewer dispatch may stall at the 600s agent-watchdog with no verdict file written. When it does:

1. **Do not re-dispatch the same prompt blindly.** Stalls correlate with payload size (memory facet on cycle 2 is the known case — full nine-facet graph + cite-index + Phase 5 report + cycle-1 verdicts adds up). First re-dispatch trims payload to the reviewer's persona card + the facet under review + the prior-cycle verdict for this same persona + the fixer-pass diff (only what changed since the prior cycle).
2. **If the trimmed re-dispatch also stalls**, write a `mechanical-inference` verdict file at `active-project/staff/audience/<persona-slug>/<facet>-r<N>-verdict.md` containing: the persona-slug, facet, cycle, episode, date, an explicit `verdict: revise` (default-conservative) OR `verdict: accept` only if the fixer diff intersected every cycle-1 callout from this persona AND no new entries were added. Include a clearly marked `# mechanical-inference` block explaining the input set used. Log the stall + inference path in the consolidated audience-gate report.
3. **Default-conservative** — when uncertain, the inferred verdict is `revise`. Audience adversarial mode is hostile by construction; silence under load should not flip to ACCEPT.
4. **Stall pattern surfaces in the orchestrator-critic report** as a process gap entry, not a finding. The pattern is a tooling-bound problem (watchdog interaction with payload) and gets traced to the same URI on every re-encounter.

### Cycle cap

Cap: **3 audience cycles** per `/and-season` convention. On cap-burn (3 cycles without 3-of-3 accept across all facets), the orchestrator-critic verdict goes NOT-SUCCESSFUL with the failing facets named; the run does NOT flip status to `audited-r1`; the user is notified for escalation.

### Output to disk

- Per-reviewer verdict files under `active-project/staff/audience/<persona-slug>/`.
- Consolidated audience-gate report at `active-project/staff/auditor/facets-audience-gate-r<N>.md` summarizing per-facet aggregate + convergence trace.
- Showrunner-memory status: on accept, `audited-r1-mechanical` → `audited-r1`. On cap-burn, status stays at `audited-r1-mechanical` with `audience_gate_cap_burned: true`.

### Convergence trace (closes criterion 4)

The aggregate audience-gate report includes a convergence trace section:

```
# Convergence trace
- Auditor findings: <count> (HARD <n>, SIGNAL <n>)
- Audience callouts (across all reviewers, deduped): <count>
- Shared findings (audience + auditor both flagged the same entry): <list of [<facet>:<id>]>
- Audience-only findings: <count>
- Auditor-only findings: <count>
- Bidirectional loop verdict: <validated | one-sided | not-validated>
```

A `validated` verdict requires at least one shared finding across the two paths. `one-sided` means both paths fired but produced disjoint findings — surface as a TASTE-FLAG for next-cycle calibration. `not-validated` means one path fired empty — typically signals reviewer underpowering for the relevant facet.

---

## Phase 6 — Persist + orchestrator-critic verdict

### 6a. Persist

**Precondition:** Phase 5 = 0 HARD AND Phase 5b = ACCEPT (3-of-3 per facet, all nine facets including exposition, AND 3-of-3 per character dialogue file) AND dialogue-coverage gate clean (URI-DIALOGUE-COVERAGE-GATE — for every speaker in Phase 0's `speakers` inventory, `theater/dialogue/<speaker-slug>.md` exists with ≥1 entry, AND every proto-line ID in Phase 0's `speech_bones` carries ≥1 `<character-slug>:<id>` citation on the canonical proto-lines) AND scene-map coverage gate clean (URI-SCENE-WINDOW — `theater/facets/scene-map-<book>-<chapter>.md` exists, every bone in the bones file lands in exactly one scene, no dangling anchors, no duplicate labels). If any of the four gates is unclean, do not persist — return to the appropriate phase. The dialogue-coverage and scene-map gates are non-bypassable: a speech chapter that finalizes without dialogue is the FAULT-DIALOGUE-MISSING failure mode; a chapter without a clean scene-map breaks scene-window stitcher dispatch. Both must be remediated before `audited-r1` is set.

1. Confirm `facets-final-audit.md` (final-cycle Phase 5 report) and `facets-audience-gate-r<N>.md` (final-cycle Phase 5b report) both written.
1a. Re-verify dialogue-coverage from Phase 0 inventory. For each `speakers` slug, stat `active-project/theater/dialogue/<slug>.md` and confirm non-empty body (≥1 entry past the frontmatter). For each `speech_bones` proto-line ID, grep the canonical proto-lines for at least one `[<character-slug>:<id>]` citation token on that line. Any miss → re-enter Phase 5 with the bare-bone/missing-file list dispatched to fixer; cycle the gate until clean. Cap-burn here flips orchestrator-critic to NOT-SUCCESSFUL.
2. Update `active-project/staff/showrunner/memory.md`:
   - Status: `audited-r1-mechanical` → `audited-r1`.
   - `audit_path: active-project/staff/auditor/facets-final-audit.md`.
   - `audit_complete: true`.
   - `audit_findings: <count>` if non-zero.
   - `audience_gate_path: active-project/staff/auditor/facets-audience-gate-r<N>.md`.
   - `audience_gate_complete: true`.
   - `audience_gate_cycles: <count>` (1, 2, or 3).
   - `bidirectional_loop: <validated | one-sided | not-validated>` from the convergence trace.
   - `facets_path: active-project/theater/facets/`.
   - `round_1_complete: true`, `round_2_complete: true`.

`_inflight/` and `_inflight-r2/` may be retained for forensic review or pruned. The canonical proto-lines + facet files + `_cite-index.md` are the source of truth.

### 6b. Master summary

```
========================================================
=== /and-facets COMPLETE: <episode-slug> ===
========================================================

Phase 1 — R1 fanout:
  9 facet files authored + <count> per-character dialogue files
  <count> total facet entries + <count> dialogue utterances; <count>/<count> protolines decorated
  Exposition: <count> entries (episode-open=<n>, first-mention=<n>, scene-open-orient=<n>)
  Dialogue: <count> entries across <count> characters / <count> behavior cards

Phase 2 — R1 fanin (merge):
  <count> _inflight/ copies merged; canonical proto-lines written
  Slices consolidated: feeling (<count> slices), state-updates (<count> slices + env)
  Stale-cite check: <CLEAN | <n> errors>
  Cite-index built

Phase 3 — R2 fanout (judge):
  6 midband facets judged in parallel
  R1 → R2 deltas:
    narrator-interest:    K=<n> D=<n> A=<n>  (cap-refusals: <n>)
    memory:               K=<n> D=<n> A=<n>  (cap-refusals: <n>)
    feeling:              K=<n> D=<n> A=<n>  (per-character: <slug>=K<n>/D<n>/A<n>, ...)
    metaphor:             K=<n> D=<n> A=<n>  (cap-refusals: <n>)
    exposition:           K=<n> D=<n> A=<n>  (scene-orient-refusals-via-fire-rule: <n>)
    dialogue:             K=<n> D=<n> A=<n> R=<n>  (per-character: <slug>=K<n>/D<n>/A<n>/R<n>, ...)

Phase 4 — R2 fanin (consolidate + merge):
  Decision-log: .r2-decisions.md (f-r2-counts: F1=<n> F2=<n> F3=<n> F4=<n>)
  Arbiter interventions: <count>; discipline-fails: <count>
  Citation accrual: R1 <count> → R2 <count>
  Cite-index rebuilt
  Scene-map validated: <N> scenes covering <N> bones (source: /and-write Phase 7 emission from substance_delta)

Phase 5 — Audit (mechanical):
  Mode: flag-only
  HARD: STRUCTURAL=<n> CONTRADICTION=<n> DEDUP=<n> SUPERFLUOUS=<n> CONSTRAINT=<n>
  SIGNAL: FREQ-BAND=<n> META=<n> AP-SCAN=<n> TASTE-FLAG=<n> PILE-UP=<warranted>/<over>
  CURVE-SHAPE: <verdict>
  Report: active-project/staff/auditor/facets-final-audit.md
  Remediation cycles: <count>; final HARD: 0

Phase 5b — Audience-gate (adversarial):
  Cycles: <count> / 3
  Per-facet aggregate (final cycle):
    location-state:    <accept | revise | fail>
    interest-narrator: <accept | revise | fail>
    sensory:           <accept | revise | fail>
    state-updates:     <accept | revise | fail>
    memory:            <accept | revise | fail>
    feeling:           <accept | revise | fail>
    metaphor:          <accept | revise | fail>
    vibes:             <accept | revise | fail>
    exposition:        <accept | revise | fail>  (audience-side adds: <n>)
    dialogue:          <accept | revise | fail>  (per-character: <slug>=<accept|revise|fail>, ...; cycle-3 seam-defensibility rate: <%>)
  Reviewers fired: <count> dispatches (specialists: <n>; fallback active-audience: <n>)
  Convergence trace: <count> shared / <count> audience-only / <count> auditor-only findings
  Bidirectional loop: <validated | one-sided | not-validated>
  Report: active-project/staff/auditor/facets-audience-gate-r<N>.md

Status: <slug> audited-r1
```

### 6c. Orchestrator-critic verdict (mandatory)

Read `staff/audience/and-facets-orchestrator-critic/card.md`. The critic evaluates the run's 7 acceptance criteria (synopsis: 9 facet files exist; 0 HARD findings post-audit; per-facet pass rate ≥75% clean; Phase 5b audience-gate ACCEPT 3-of-3 per facet; showrunner memory current; process gaps captured; wall-clock budget stated). Produce verdict appended to the master summary:

```
/and-facets orchestrator-critic verdict — <episode-slug>:
  Result: <SUCCESS | SHIPPABLE-WITH-CAVEATS | NOT-SUCCESSFUL>
  Criteria met: <count> / 7
  Cap-refusals: <count> (<%> of seams)
  HARD findings post-audit: <count>
  Audience-gate: <ACCEPT (all 9 facets 3-of-3) | PARTIAL (<n> facets short) | CAP-BURNED>
  Audience-gate cycles: <count> / 3
  Bidirectional loop (convergence trace): <validated | one-sided | not-validated>
  Wall-clock: <stated budget | overrun>
  Caveats (if any): <list>
  Recommendation: <ship | iterate | escalate>
```

**Decision rule:** SUCCESS (all 7 met) → downstream may proceed. SHIPPABLE-WITH-CAVEATS (exactly 1 missed) → caveat named; missed criterion queued. NOT-SUCCESSFUL (2+ missed) → remediate; do not flip status to `audited-r1`.

The critic does NOT mutate facets or cancel the run. It produces the standard; orchestrator + user respond.

---

## Convergence and refusal handling

- **R1 is single-pass per author.** No retry loop. Faults discovered post-hoc surface in R2 or audit.
- **R2 is single-pass per judge.** No mid-layer rebuild (judges run in parallel, blind to each other's mutations). The post-R2 cite-index reflects the union; cross-judge interaction effects (e.g., R2.2 deleting memory:N while R2.4 metaphor keeps a `licensed-by: mem:N` reference) surface in Phase 5 as CONSTRAINT findings.
- **Merge-tool aborts (body-integrity / stale-citation) are build defects.** Re-dispatch the responsible author with a clarifying brief; re-run the tool. Subsequent phases cannot proceed on a non-clean merge.
- **Soft refusals** (rubric gap, structural fault, blocking input missing) log under `active-project/staff/<author>/` and the orchestrator continues. The summary lists refusals; the episode is not blocked.

---

## Notes

- **Scene-map is upstream-only** — emitted by `/and-write` Phase 7 from `chapters[].scenes[].bones[].substance_delta.axis_moves.magnitude` in showrunner memory; `/and-facets` Phase 4d validates only. There is no in-pipeline scene-map authoring.
- **R3 retired.** The relaxation pass was default-skipped in the prior chain (s01e01 produced a fixed point under R2). The fanout-fanin-fanout-fanin-audit shape replaces the four sub-commands; R3's behavior — "repeat the judge round" — is recoverable as a re-run of the command with `faceted-r2` already on disk, but is not the default flow.
- **Audience interest-flags are skipped.** When tuned, it joins the R1 parallel block (one dispatch per persona).
- **Vibe-cloud write-back is deferred.** Post-author propagation of vibe deltas to actor/loc/studio files happens in and-wrap or a follow-on showrunner dispatch.
- **Cross-facet deletion authority** belongs to the audit only. Once auditor is tuned for delete-authority, HARD findings execute as deletes with cascade. Until then, audit is flag-only and remediation routes back to authors as a separate work cycle (re-run /and-facets after fixes land, or fire targeted author dispatches).
- **Shared reviewer assets** (audience persona `Threshold Discipline` + `Season-Scope Adversarial` body sections; auditor class library — `CURVE-SHAPE` / `AP-SCAN` / `FREQUENCY-BAND` definitions) are authored once and consumed from both `/and-season` and `/and-facets`. Patterns the audience flags at `/and-season` bone-gate graduate into AP-SCAN entries via the shared auditor's TASTE-FLAG → AP-SCAN promotion path.
