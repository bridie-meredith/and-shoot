---
analysis: and-season-exit-format
date: 2026-05-09
scope: ideal exit format /and-season Phase 4/5 must produce so /and-shoot-v2 can consume cleanly
status: design analysis (no commands modified; recommendations only)
inputs:
  - design/shoot-v2/README.md
  - design/shoot-v2/facet-dependency-audit.md
  - design/shoot-v2/facet-tuning-process.md
  - design/shoot-v2/round-trip-method.md
  - design/shoot-v2/decisions.md
  - design/shoot-v2/open-questions.md
  - schemas/proto-line.schema.md
  - schemas/facet.schema.md
  - schemas/dialogue.schema.md
  - schemas/showrunner-memory.schema.md
  - design/shoot-v2/rubric-{location-state,tensometer,narrator-interest,state-updates,memory-flags,feeling,vibes}.md
  - design/shoot-v2/{locstate,tensometer}-tuning-package.md
  - .claude/commands/and-season.md (Phase 4/5 + S7)
constraint: read-only analysis. No edits to /and-season.md and no touch on s01.aggregate.md (parallel fixer).
---

# /and-season exit-format analysis

## Executive summary

`/and-season` Phase 4/5 currently emits per-episode proto-line files with a two-line header (`narrator:` + `goal:`) plus renumbered SVO bones carrying an `# aggregate-id:` traceability comment, and writes an `episodes[]` array into showrunner memory. That is **necessary but underspecified** for the facet-execution model `/and-shoot-v2` is being designed against.

The facet DAG (`facet-dependency-audit.md`) shows ten facet authors per episode, each loading a *very specific* context bundle: tensometer needs episode-scope vibes, loc-state needs the location card set + loc-scope vibes, NI needs behavior cards + tens + loc-state, state-updates needs the actor's state.md baseline + locked tens + locked NI, memory needs prior-episode monument fires, vibes-updates is cross-cutting. Almost none of this is supplied by the proto-line file alone — it is meant to be loaded around the proto-line file by whatever orchestrates the per-episode facet pass. But several inputs are *episode-instance-specific* (active cast list, on-stage location set, prior-episode handoff state, episode-scope vibe-cloud) and only `/and-season` knows them at split time. If `/and-season` doesn't write them down, the per-episode orchestrator either rediscovers them by re-scanning the aggregate (wasteful, error-prone) or skips them (silent quality loss).

**Recommendation: hybrid (a)+(c).** Augment Phase 4 per-episode header with five additional fields (`episode:`, `cast:`, `locations:`, `prior_episode:`, `aggregate_range:`) — none invasive to the existing schema, all derivable at split time. Phase 5 episodes[] entries gain three fields (`cast`, `locations`, `aggregate_range`). Drop the `# aggregate-id:` comment in favor of a single `aggregate_range:` header field — the per-line comment is dead weight nobody reads. Cross-episode handoff (location-state baseline, state.md snapshot, vibe-cloud snapshot) is **out of scope for `/and-season`** — it lives in the canonical state files showrunner already maintains, and `/and-shoot-v2` should snapshot those at episode-open. Surface that as a tuning note for `/and-shoot-v2`. Keep the `narrator:` and `goal:` fields exactly as currently specified — both are load-bearing and present in the schema.

---

## Section A — Facet-author input contract

For each facet author at episode scope, what they need to start work, in priority order. Compiled from `rubric-*.md` "Author/reviewer notes" and the dependency audit.

### A.1 — Universal inputs (every facet)

Every facet author loads:

1. **The per-episode proto-line file** — `narrator:`, `goal:`, the bones. Authority: the file itself.
2. **`schemas/facet.schema.md`** — the universal line shape `<id> @<proto-line-id> <content>` plus the per-type content rules. Authority: schema.
3. **The facet's own rubric** under `design/shoot-v2/rubric-<facet>.md` — author signatures + anti-patterns + curve-shape (where applicable).
4. **Episode slug** — for header frontmatter (`episode: <slug>`) on the facet file itself.

These are stable across all ten facet authors. Nothing here demands more than the current per-episode file already supplies, modulo the episode slug — which is currently *implicit* in the filename, never explicit in the file's content.

### A.2 — Layer-1 facets (tens, loc-state, pre-seed vibes)

Read SVO/proto-lines only, plus their bias inputs.

| Facet | Specific inputs (beyond universal) |
|---|---|
| **tensometer** | episode-scope vibes (curve-shape bias per dependency-audit RE-TUNE-MINOR §1) |
| **loc-state** | active location cards (`active-project/warehouse/loc-*.card.md` + `cards/locations/*.card.md` for any referenced); loc-scope vibes |
| **pre-seed vibes** | already populated at world-build; not authored at episode time |

The **active location set for this episode** is critical for loc-state — it tells the studio fork *which* location cards to load. Currently the proto-line file does not list this; the studio fork would either grep slugs out of the proto-lines or load every location in the warehouse. Both paths work but the first is brittle (depends on slug-grep accuracy) and the second is wasteful.

### A.3 — Layer-2 facets (NI, sensory)

| Facet | Inputs |
|---|---|
| **narrator-interest** | base behavior card + variant behavior card + persona card *for the POV character*; locked tens; locked loc-state |
| **sensory** | locked loc-state (mandatory baseline); locked tens (correlative); loc-scope vibes |

The POV character is `narrator:` from the header — current spec covers this. The behavior-card stack is resolved by margit from the persona card's `behavior-card:` field, so no header change needed there.

### A.4 — Layer-3 facets (state-updates, memory)

Both depend on locked tens + locked NI. Critical addition for state-updates:

| Facet | Inputs |
|---|---|
| **state-updates (studio fork)** | locked tens + NI; locked loc-state; the proto-line file; **studio state schema**; relevant location/prop cards |
| **state-updates (per-character dialogue-writer fork)** | locked tens + NI; the proto-line file; that character's persona card + state.md schema + behavior pack |
| **memory** | base + variant behavior cards (POV); persona card; locked tens (inverted-tens density gate); locked NI (mandatory spine co-citation) |

Two implications:

- **Active cast list** — state-updates dispatches one fork per actor in the episode. The orchestrator must know which actors fired in this episode. This is derivable from the proto-lines (every subject slug + every dialogue-beat's listener slug) but requires a scan. Better: have `/and-season` write the cast list directly into the per-episode header at split time.
- **Prior-episode state baseline** — state-update content is `<old> -> <new>`. The `<old>` value must reflect the state-as-of-this-episode-open, which is the post-write-back state from the prior episode. This baseline lives in `actors/<slug>/state.md` (already maintained by showrunner write-back) and `staff/studio/state.md` — not in any proto-line file. **`/and-season` does not need to do anything about this**; showrunner write-back at the boundary between cross-facet consistency and stitch (per `decisions.md` §"Memory write-back") is the canonical mechanism. But `/and-shoot-v2` must explicitly snapshot these at episode-open, not at facet-author dispatch, to pin the `<old>` reference.

### A.5 — Layer-4/5/6 facets (feeling, metaphor, vibes-updates)

| Facet | Inputs |
|---|---|
| **feeling** | behavior pack + persona card per character; locked NI (POV non-redundancy); locked sensory; locked SU; per-character vibes |
| **metaphor** | locked memory OR feeling (mandatory anchor); tens; sensory; NI |
| **vibes-updates** | locked SU + memory + feeling + tens + proto; full vibe-cloud snapshot across actors/locations/studio |

Vibes-updates is cross-cutting and is the *only* facet that explicitly reads across episodes (a vibe added in s01e01 persists into s01e02+). It needs the per-actor + per-location + studio vibe-cloud snapshots as of episode-open. Same as state-updates: showrunner-maintained, snapshotted at episode-open by `/and-shoot-v2`.

### A.6 — Layer-7 (dialogue/stitch)

The dialogue-writer fork dispatch (per character per episode) loads:
- character card + ltm + stm + state + behavior card stack + coach prompt with all that character's speaking beats

The coach prompt is built from the proto-line file (every `<character> speaks to <listener>` beat). Cast list again — same input.

The stitcher reads everything: proto-lines, all facet files, dialogue files. It is the terminal consumer.

### A.7 — Priority synthesis (what each facet author absolutely needs)

In priority order, every facet author must have:

1. **Per-episode proto-line file** with stable narrator + goal headers + clean SVO bones. *(Currently provided.)*
2. **Episode slug** (for facet file frontmatter `episode:` field). *(Currently implicit in filename only.)*
3. **Active cast roster for this episode** (which actors actually appear). *(Currently must be derived from proto-line slug-grep.)*
4. **Active location set for this episode** (which location cards are in scope). *(Currently must be derived from proto-line slug-grep + loc-state authoring discovery.)*
5. **Episode-scope vibe handle** (which scope-keyed vibe-cloud bundle to load). *(Currently the orchestrator resolves to `staff/studio/vibes.md` EPISODE_<N>_VIBES if present, but the episode number / sequence index is not in the per-episode file.)*
6. **Prior-episode handoff context** (last-known location-state, prop holdings, actor-state, vibe-cloud-as-of-prior-close). *(Already lives in canonical state files maintained by showrunner write-back; not in any proto-line file.)*
7. **Aggregate-range traceability** (for cross-checking against the season aggregate when a fault routes back). *(Currently per-line `# aggregate-id:` comments — works but is per-line dead weight.)*

---

## Section B — Current /and-season exit gap analysis

Mapping current Phase 4/5 outputs against §A.7 priorities.

### B.1 — Currently provided (correctly)

| Need | Supplied by | Status |
|---|---|---|
| Per-episode proto-line file with bones | Phase 4 Step 3 mechanical write-out | OK |
| `narrator:` header | Phase 4 Step 3.1 | OK — POV character resolved from inline `# pov:` markers |
| `goal:` header | Phase 4 Step 3.1 | OK — distilled by orchestrator from stretch + dramatist rationale |
| Renumbered 1..M IDs | Phase 4 Step 3.2 | OK — new file-scoped numbering |
| `episodes[]` in showrunner memory | Phase 5 Step 1 | OK — slug, status, narrator, interlude, chunk, proto_lines_path |
| Aggregate preserved as canonical | Phase 4 Step 4 | OK — re-run path is intact |

### B.2 — Missing (relative to §A.7)

| Need | Currently | Gap class |
|---|---|---|
| **Episode slug in file** | Implicit in filename only | MINOR — add `episode:` header line |
| **Active cast roster per episode** | Derivable from proto-line slug-grep; not pre-computed | MEDIUM — slug-grep is brittle (esp. dialogue listener-slugs may not be subjects); split-time computation is canonical |
| **Active location set per episode** | Derivable from proto-line slug-grep + studio inference | MEDIUM — same brittleness; `/and-season` already reads location cards at S4 continuity, can record what's in scope |
| **Episode sequence index for vibes scope** | Implicit (s01e01 → 01) | MINOR — add `episode_index:` or rely on slug parse |
| **Prior-episode reference for handoff** | Not recorded; orchestrator must compute "previous episode in season order" | MINOR — add `prior_episode:` field; null for e01 |
| **Aggregate range** | Per-line `# aggregate-id: <N>` comments | DEAD-WEIGHT — replace with single `aggregate_range: <from>-<to>` header field |
| **Phase 5 episodes[] cast/locations** | Not written | MEDIUM — companion to per-episode header fields |

### B.3 — Currently present but unused

- **`# aggregate-id: <N>` per-line comments.** No facet author or downstream agent in `design/shoot-v2/` reads these. The aggregate-range can be expressed once in the file header (`aggregate_range: 1-87`) without per-line decoration, halving file weight and removing per-line clutter that the SVO author was explicitly told NOT to leave (the harsh-SVO discipline in the proto-line schema treats trailing comments as visual noise — see `proto-line.schema.md` §Body format: "No section headers, no scene markers, no markdown bullets"). The per-line aggregate-id comment is in tension with that spec.

  Counterargument considered: per-line comments help fixer route a fault back to the aggregate ID. But the fixer can do the same with an aggregate-range + a fixed offset (`aggregate_id = aggregate_range_start + episode_id - 1` if the renumbering is contiguous, which it is per Phase 4 Step 3.2). The comment is redundant.

  **Recommendation: drop per-line comments; keep range in header.**

### B.4 — Cross-episode handoff anchors — out of scope for /and-season

The proto-line file should NOT carry last-known location-state, prop holdings, actor-emotional-residue, or tensometer-baseline at its open. Reasons:

1. **Layering violation.** Proto-lines are bone-only per `proto-line.schema.md`. Adding a state-snapshot header makes the file a state document AND a bone document — two responsibilities, breaks the schema's single-purpose intent.
2. **Source-of-truth duplication.** Actor state lives in `actors/<slug>/state.md`. Studio state lives in `staff/studio/state.md`. Vibe-clouds live in `actors/*/vibes.md` + `cards/locations/*.card.md` § VIBES + `staff/studio/vibes.md`. These are showrunner's responsibility per the Memory Rules in CLAUDE.md ("If a change is not in a state file, it did not happen"). Mirroring them into the proto-line file creates a stale copy by the time facet authoring runs.
3. **Phase ordering.** `/and-season` runs *before* showrunner has written-back any state-updates from this season's facet pass (write-back is per-episode and happens during/after facet authoring, not during /and-season). At /and-season Phase 5, the canonical state files reflect the prior season's final state (or the activation seed for s01). That IS the correct baseline for s01e01's facet authoring.

**The right place to snapshot handoff context is in `/and-shoot-v2` Phase 0**, dispatched per-episode at facet-authoring time. Not in `/and-season`.

### B.5 — S7 facet-readiness pass — already covers density but not the contract

S7 (and-season.md L205-211) checks that "for each load-bearing beat, verify a citable bone exists for each facet author downstream." This is correct as far as it goes, but it audits the *bones* against facet existence, not the *episode-file output* against facet-author input contract. The audit operates on the aggregate, not on the post-split per-episode files. Recommend leaving S7 as-is (it's doing the right work at the right scope) and adding a *Phase 4 Step 4 validate* item (post-split, pre-Phase-5) that confirms each per-episode file has the new header fields populated. See §C.

---

## Section C — Recommendation

**Hybrid (a) + tuning notes for /and-shoot-v2.**

### C.1 — Phase 4 Step 3 — augmented per-episode header

Replace the current header spec at `and-season.md` L286-289 with:

```
# proto-lines — <episode-slug>

episode: <episode-slug>
narrator: <pov-actor-slug>
goal: <one sentence — what this episode shows the audience>
cast: <slug>, <slug>, <slug>, ...
locations: <loc-slug>, <loc-slug>, ...
prior_episode: <previous-episode-slug | none>
aggregate_range: <from>-<to>

<id> SUBJECT VERB OBJECT
<id> SUBJECT VERB OBJECT
...
```

Field rules:

- **`episode:`** — the episode slug (`s01e01`). Required. Match the filename. The facet authors lift this verbatim into their facet file frontmatter `episode:` field.
- **`narrator:`** — unchanged from current spec.
- **`goal:`** — unchanged from current spec.
- **`cast:`** — comma-separated actor slugs that appear as a SUBJECT or as a `speaks to <listener>` listener anywhere in this episode's bones. Computed by orchestrator at split time via slug-grep over the episode's proto-lines (no inference, no card lookup). Order: by first-appearance ID. Listener-only slugs (someone spoken to but never speaking or acting) included with a `?` suffix annotation if the orchestrator wants to flag them, otherwise plain.
- **`locations:`** — comma-separated location slugs (the slug set the studio fork must load to author location-state). Two sources: (a) location slugs that appear as SUBJECT or as object-of-transitional-verb in the proto-lines (`taylor enters the yard` → resolve "the yard" to the active loc card); (b) inline `# loc:` comments if the screen-writer added any (currently none specified, but the schema accommodates `# pov:` so `# loc:` is a natural extension — flag for separate decision). Initial implementation can derive only from (a) and accept that the studio fork may discover additional implicit locations during loc-state authoring; record those at facet-author time as a feedback signal.
- **`prior_episode:`** — slug of the previous episode in season order, or `none` for e01. Computed at Phase 4 Step 3 by walking the just-numbered episode list. Used by `/and-shoot-v2` Phase 0 to know which prior-episode state files to snapshot for handoff baseline.
- **`aggregate_range:`** — the contiguous aggregate-id range covered by this episode (e.g. `1-87`). Replaces per-line `# aggregate-id:` comments. Computed from Phase 4 Step 3.2 renumbering (the first proto-line maps to aggregate-id N; the last to aggregate-id N+M-1).

A blank line follows the header before the body (unchanged).

### C.2 — Drop per-line `# aggregate-id:` comments

Phase 4 Step 3.2 currently specifies "The aggregate's continuous numbering is preserved as a `# aggregate-id: <N>` comment on each line for traceability." Replace with: "The aggregate's continuous numbering is preserved as the `aggregate_range:` header field (single line). Per-line aggregate-id comments are not authored — fixers compute the aggregate-id by `aggregate_range_start + episode_id - 1` when routing faults back to the aggregate."

This removes per-line clutter that nothing reads, conforms to the proto-line schema's no-comments-on-body-lines spirit, and keeps full traceability.

### C.3 — Phase 4 Step 4 validate — extend

Current validate (and-season.md L289): "each per-episode file has `narrator`, `goal`, contiguous numbering 1..M, no orphan content."

Extend to: "each per-episode file has `episode`, `narrator`, `goal`, `cast`, `locations`, `prior_episode`, `aggregate_range`, contiguous numbering 1..M, no orphan content. `cast` matches the slug-grep over the episode's bones (sanity check, not gate). `aggregate_range` is contiguous and non-overlapping with sibling episodes' ranges."

### C.4 — Phase 5 episodes[] augmentation

Current Phase 5 Step 1 writes per-episode entry: `slug`, `status: protolined`, `narrator`, `interlude`, `chunk`, `proto_lines_path`. Extend each entry with:

- **`cast`** — same comma-separated slug list as the file header. Mirrored into memory so showrunner can answer "who's in episode N" without opening the file.
- **`locations`** — same as header.
- **`aggregate_range`** — same as header.
- **`prior_episode`** — same as header.

Order in entry: existing fields first, new fields at end. No schema authority change — the showrunner-memory schema treats `episodes[]` entries as open-shape (it specifies `slug`, `status`, `chunk` and notes the entry is one-line per item; extension fields are licit per the schema's "Optimized for Claude" framing).

### C.5 — Tuning notes for /and-shoot-v2 (Phase 0 baseline snapshot)

When `/and-shoot-v2` is implemented, its Phase 0 (per-episode setup) MUST snapshot the cross-episode handoff baseline before any facet author dispatches. Required snapshots:

1. **Actor state baseline.** For each slug in `cast`, copy `actors/<slug>/state.md` content into a per-episode handoff bundle (`active-project/theater/<episode-slug>-handoff/<slug>.state.snapshot`). State-updates fork reads `<old>` from this snapshot, not from the live state file (which may shift mid-episode if write-back is staggered).
2. **Studio state baseline.** Copy `staff/studio/state.md` into `active-project/theater/<episode-slug>-handoff/studio.state.snapshot`. Studio fork's state-updates `<old>` reference.
3. **Vibe-cloud baseline.** Copy each cast actor's `actors/<slug>/vibes.md`, each `locations:` slug's `cards/locations/<slug>.card.md` § VIBES, and `staff/studio/vibes.md` into `active-project/theater/<episode-slug>-handoff/vibes.snapshot.md`. Vibes-updates reads pre-load state from this snapshot; pre-loaded keywords trigger `++`-or-skip per RF-001.
4. **Prior-episode last-cited loc-state.** If `prior_episode` is non-null, the loc-state file from the prior episode (`active-project/theater/facets/<prior_episode>/location-state.md`) is consulted by this episode's studio fork to honor frame-inheritance across the episode boundary. The first loc-state entry in the new episode either matches the prior close (continuous frame, no new entry needed at episode-open) or fires a fresh entry (frame-change at boundary). Both are licit; the audit checks consistency.

These are NOT `/and-season`'s job. `/and-season` provides the handles (`cast`, `locations`, `prior_episode`); `/and-shoot-v2` does the snapshotting at episode-open.

### C.6 — What stays unchanged

- The `narrator:` and `goal:` fields stay exactly as currently specified. Both are load-bearing for the SVO writer and downstream pipeline (per `proto-line.schema.md` §"File header (required)"). No facet author needs more than these two header items beyond what §C.1 adds.
- The proto-line schema (`schemas/proto-line.schema.md`) needs a small update to accept the additional header fields (`episode`, `cast`, `locations`, `prior_episode`, `aggregate_range`). These are appended to the existing required header pair. The schema currently defines only `narrator` and `goal` as required; the new fields are required-when-emitted-by-/and-season, optional otherwise (e.g. ad-hoc per-episode files authored via `/and-protolines-v2` may lack them and that's OK — those files don't go through facet authoring without an /and-shoot-v2 dispatch that supplies the missing context).
- Phase 4's interpretive split logic (dramatist proposes, audience reviews) stays unchanged. The augmented header is downstream of the split, written at mechanical write-out only.
- S7 facet-readiness audit stays at aggregate scope. The new header validation is a separate Phase 4 Step 4 check.

### C.7 — Migration cost

- `and-season.md` Phase 4 Step 3 + Step 4 + Phase 5 Step 1: ~30 lines of edits, all to the orchestration spec; no new agent dispatches; no new files.
- `proto-line.schema.md`: ~20 lines added to §"File header (required)" describing the new optional-when-not-from-/and-season fields.
- `showrunner-memory.schema.md`: ~5 lines extending the `episodes[]` entry shape doc.
- No re-tuning of any facet rubric is required (the augmented header is a *superset* of what facet authors currently expect).
- No effect on any locked facet output (loc-state, tens, NI, SU, memory, sensory, feeling, metaphor, vibes from the s01e01 corpus). Those were authored against single per-episode proto-line files that did not have the augmented header; adding the header to future episodes does not invalidate prior runs.

### C.8 — What this analysis does NOT recommend

- **Inline `# loc:` comments in proto-lines** parallel to `# pov:`. Tempting, but loc inheritance is much more granular than pov and risks bloating the bone file. Defer until /and-shoot-v2 implementation reveals whether the loc-state author needs inline location markers vs. discovering them from the cast/locations header + bone slug-grep.
- **Per-character handoff residue files in the proto-line directory.** Belongs to /and-shoot-v2's Phase 0, not /and-season's outputs. Different command, different scope.
- **A separate "episode-context.yaml" sidecar file.** Considered, rejected. The header-in-the-proto-line-file pattern is consistent with `narrator:` / `goal:` precedent and avoids splitting the facet authors' single-file load into two-file load.
- **Dropping the aggregate as canonical pre-split artifact.** Aggregate-as-canonical is a Phase 2/3 design commitment per `and-season.md` L84-89; nothing in this analysis touches that.

---

## Open issues for user review

1. **`cast` field listener-only annotation.** Should slugs that appear only as dialogue listeners (never as SUBJECT, never speaking) get a `?` suffix or be omitted? Default proposal: include plain (no suffix); /and-shoot-v2 dialogue-writer-fork dispatch decides whether to fork for a non-speaking listener.
2. **`locations` field source.** Slug-grep over bone OBJECTs is the cheap path; inline `# loc:` markers would be cleaner but extend the schema. Default proposal: slug-grep only at /and-season time; /and-shoot-v2 studio fork records discovered-but-missing locations as a feedback signal back to /and-season for next-season run.
3. **Schema authority.** The augmented per-episode header fields should land in `schemas/proto-line.schema.md` so margit and the auditor have a single source of truth. Confirm before applying.
4. **Backfill of existing episodes.** If a project has already-split per-episode files lacking the new header (e.g. if s01 split has run before this change), backfill is a one-time orchestrator dispatch (re-derive `cast` / `locations` / `aggregate_range` from the aggregate + the per-episode file). Cheap.
