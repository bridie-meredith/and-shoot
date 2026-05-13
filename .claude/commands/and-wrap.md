---
description: Editor pass for one episode. Wraps the stitcher draft into a ship-ready manuscript. Three phases — audience review (advisory) → auditor pass (rendered-prose, classified) → editor (prose pass + audience-flag remediation + audit-finding remediation). Reads draft/<slug>.md + draft/<slug>.annotated.md + render-log + scene-map + facets; writes polish/<slug>.md. Usage - /and-wrap [episode-slug | --all-stitched | s01e01..s01e05]
---

Wraps a stitcher draft into a ship-ready manuscript. Reads from `active-project/draft/<slug>.md` and the upstream graph (render-log, scene-map, facets, dialogue, exposition); writes to `active-project/polish/<slug>.md`. Three phases: audience review (advisory), auditor pass (rendered-prose audit, classified faults), editor pass (prose work + flag/finding remediation).

You are the orchestrator. All dispatches use the Agent tool — inline generation is not a substitute. Showrunner is not in the orchestration chain.

**Why this command exists.** The stitcher (`/and-stitch`) produces a clean draft from the facet graph but operates fork-by-fork: per-scene in `scene-window` mode, per-anchor in `per-anchor` mode. Neither fork sees the whole text at once. The editor pass is the only phase in the pipeline with whole-text view — it catches percussion that crosses scene boundaries, voice drift the scene-fork's variance moves accidentally introduced, repetition the per-anchor fork couldn't perceive, and continuity issues that slipped through Phase 4 voice-transform. It also remediates audience entertainment flags and auditor constraint findings against the rendered prose.

The editor does NOT add plot content, change blocking, modify dialogue verbatim, or override bone-faithfulness. Those fences from the stitcher persist into wrap. The editor's license is over **prose surface** — economy, variance, continuity, voice consistency — within the graph's truth.

---

## Args

- `$1` — selects what to wrap. Forms:
  - omitted → wraps the most recent episode whose status is `stitched` and not yet `wrapped`
  - episode slug (e.g., `s01e03`) → wraps that single episode
  - `--all-stitched` → wraps every episode currently in `stitched` status, in season order
  - range `s01e01..s01e05` → wraps each episode in the range whose status is `stitched`, in order
- `--skip-audience` — optional. Skip Phase 1 audience review. Use when wrap is being re-run after an audience pass already landed and you only want to re-edit. Audience flags from the prior run remain on disk and are still consumed by the editor.
- `--skip-auditor` — optional. Skip Phase 2 auditor pass. Use when the prior auditor pass already landed clean. Audit report from the prior run remains on disk.
- `--editor-mode <strict|standard|permissive>` — optional. Override the editor's cut-aggressiveness. Default: `standard`. Strict cuts more aggressively on hollow patterns and over-qualification; permissive flags rather than cuts.

In bulk modes, episodes wrap one at a time, sequentially. If one fails or escalates, stop and surface state — do not continue past a failure.

---

## Phase 0 — Validate + Load (per target)

Read `active-project/staff/showrunner/memory.md`. For each target slug:

1. **Status.** Episode status must be `stitched` (post `/and-stitch`). Not `planned`, not `audited-r1`, not already `wrapped`.
2. **Draft existence.** `active-project/draft/<slug>.md` exists and is non-empty. `active-project/draft/<slug>.annotated.md` exists (used by editor for trace lookup).
3. **Render-log existence.** `active-project/staff/stitcher/render-log-<slug>.md` exists. Used by editor to confirm bone-faithfulness coverage when in doubt.
4. **Scene-map existence.** `active-project/theater/facets/scene-map-<slug>.md` exists. Used by audience review (per-scene flagging) and editor (cross-scene percussion detection).
5. **Facet graph.** `active-project/theater/facets/_cite-index.md` exists. Used by auditor for graph-prose cross-checks.
6. **Audience persona membership.** Read `active-project/audience/` for the project's three audience personas. Audience membership is project-defined and does not change at wrap.
7. **Polish dir.** Create `active-project/polish/` if not present.

If any check fails, print the missing input + path and stop.

If wrap log files already exist for this target (`wrap-audience-<slug>.md`, `wrap-audit-<slug>.md`, `wrap-edit-log-<slug>.md`), wrap may have been interrupted mid-run. Print:

```
Wrap log files already exist for <slug>:
  - <list of existing files>
Wrap may have been interrupted mid-run. Review the existing logs to see how far wrap progressed.
Delete the wrap log files in active-project/staff/editor/ to restart, then re-run /and-wrap.
Or pass --skip-audience / --skip-auditor to resume from the editor step.
```

---

## Phase 0.5 — Pre-flight summary (user-visible gate)

```
/and-wrap pre-flight for <slug>:
  draft:               active-project/draft/<slug>.md (<N> words, <N> sentences, <N> paragraphs)
  annotated draft:     active-project/draft/<slug>.annotated.md
  render-log:          active-project/staff/stitcher/render-log-<slug>.md
                       phase-1 mode: <scene-window | per-anchor>; <S> scene-forks or <N> per-anchor forks
  scene-map:           active-project/theater/facets/scene-map-<slug>.md (<S> scenes covering <N> bones)
  cite-index:          active-project/theater/facets/_cite-index.md
  facets:              <list>
  audience:            <persona-1>, <persona-2>, <persona-3>
  editor-mode:         <strict | standard | permissive>
  skip-flags:          <none | --skip-audience | --skip-auditor>
  output-dir:          active-project/polish/
```

If anything looks wrong (wrong draft, wrong render-log mode, missing scene-map), stop here.

---

## Phase 1 — Audience review (advisory; per-persona forks; parallel)

**Skip if `--skip-audience`.** Otherwise dispatch the three audience persona agents in parallel. Each reads:

- `active-project/draft/<slug>.md` (the rendered prose)
- `active-project/theater/facets/scene-map-<slug>.md` (scene boundaries + rhythm-shape per scene; for per-scene structural review)
- The persona's own card at `active-project/audience/<slug>/card.md`
- The persona's STM at `active-project/audience/<slug>/stm.md` (load prior wrap-review feedback before reviewing)
- The episode vibe-cloud (from facets/vibes.md slice for this episode)

Each persona reviews at the rendered-prose level (NOT the facet-graph level — that already happened at `/and-facets` Phase 5b). The review focuses on:

- **Pacing.** Does the prose breathe? Are peaks landing? Are transition runs draggy?
- **Variance.** Does the prose feel metronomic anywhere? Specific sentences that read as wallpaper?
- **Voice.** Is the POV register consistent? Does any passage read out-of-character?
- **Entertainment.** Lines that land flat, exchanges that feel inert, beats that fail to engage.
- **Confusion.** Anything that breaks comprehension — pronoun ambiguity, dropped antecedent, blocking unclear.

Each persona produces an inline-flagged version of the draft (sentence-keyed flags, advisory only — the editor decides whether to act):

```
[⚑ <persona-slug>: <one-line reason>]
```

Each persona also writes a wrap-verdict to their STM (`active-project/audience/<slug>/stm.md`): what they flagged, what they accepted, why. A wrap review that does not write to STM has not completed.

**Output.** The inline-flagged drafts are merged into a single `active-project/staff/editor/wrap-audience-<slug>.md` with all three personas' flags overlaid (one section per persona; each flag carries its persona slug).

```
# Audience Wrap Review — <episode-slug>

## <persona-1>
<N flags>
[per-line entries with sentence excerpt + flag reason]

## <persona-2>
...

## <persona-3>
...

## Summary
<persona-1>: <N flags> — <high-level concern summary or "no flags">
<persona-2>: ...
<persona-3>: ...
shared concerns (≥2 personas flagged same line): <list or "none">
```

The editor will read this in Phase 3 and remediate flagged lines per its allowed-moves contract. Audience flags are advisory: the editor may keep a flagged line if its judgment overrides (the editor's reason goes in the edit-log).

---

## Phase 2 — Auditor pass (rendered-prose audit; classified faults)

**Skip if `--skip-auditor`.** Otherwise dispatch the auditor as a fork. The auditor receives:

- `active-project/draft/<slug>.md` (clean rendered prose)
- `active-project/draft/<slug>.annotated.md` (line-by-line trace to bones / facets / lens-decider)
- `active-project/staff/stitcher/render-log-<slug>.md` (per-fork decisions)
- `active-project/theater/proto-lines/<slug>.md` (canonical bones)
- `active-project/theater/facets/_cite-index.md` (graph index)
- `active-project/theater/facets/scene-map-<slug>.md` (scene boundaries + rhythm fields)
- `active-project/theater/dialogue/<character-slug>.md` (per-character dialogue files — utterance verbatim source)
- `active-project/theater/facets/exposition-<slug>.md` (exposition gloss source)

The auditor checks the **rendered prose against the graph** — a different audit than `/and-facets` Phase 5 (which checked the graph internal). Eight classes:

1. **BONE-COVERAGE.** Every bone in proto-lines has a corresponding rendered trace in the annotated draft (rendered sentence, FUSE-into, CUT-BONE entry). Missing bone → HARD `FAULT-EDITOR-BONE-LOST @<id>`.

2. **DIALOGUE-VERBATIM.** Every quoted utterance in the prose matches its source `<utterance>` field in `theater/dialogue/<character-slug>.md` exactly (modulo voice-transform on attribution clauses, which is allowed). Modified utterance → HARD `FAULT-EDITOR-DIALOGUE-MODIFIED @<dialogue-id>`.

3. **EXPOSITION-VERBATIM.** Every exposition gloss in the prose matches its source `<gloss-text>` field in `exposition-<slug>.md` (modulo voice-transform). Modified gloss → HARD `FAULT-EDITOR-EXPOSITION-MODIFIED @<exposition-id>`.

4. **NO-INVENTION.** No prose content names a character, location, prop, condition, behavior, or event not present in the facet graph or its referenced cards. Earth-Bet hard-fence list still applies (per `/and-facets` Phase 5 CONSTRAINT class). Invention → HARD `FAULT-EDITOR-INVENTION` with the invented content quoted.

5. **CONTINUITY.** Tense, person, and pronoun continuity hold across the whole text. Tense shift mid-paragraph that's not a flashback → HARD. Pronoun antecedent ambiguity (a pronoun whose closest noun-phrase referent is the wrong character) → HARD. Possessive register breaks per the persona's tuning notes → SIGNAL.

6. **BLOCKING.** Spatial relations preserved across the text. Character at location-A in scene N and at location-B in scene N+1 with no transition bone → HARD. State-update facets (`state-updates-<character-slug>.md`) cited as the canonical record of position/state changes.

7. **SCENE-MAP-RESPECT.** Scene boundaries from `scene-map-<slug>.md` honored. The polish manuscript may use scene-break markers (e.g. blank-line, asterism, horizontal rule) but the boundaries themselves match the scene-map. Reordered or merged scenes → HARD.

8. **EARTH-BET-HARD-FENCE.** Re-scan the rendered prose for the Earth-Bet proper-noun list (per `/and-facets` Phase 5 CONSTRAINT). Any hit is HARD even if it slipped through the facet-graph audit upstream — the wrap auditor is the last gate before ship.

**Output.** `active-project/staff/auditor/<slug>-wrap-audit.md` per `schemas/audit-report.schema.md`. Classified findings; HARD findings block the run, SIGNAL findings advise the editor.

If HARD findings exist, route to fixer per the standard repair flow OR escalate to user. The editor cannot proceed with HARD findings unresolved — its job is prose surface, not graph repair. Only SIGNAL findings flow into the editor as advisory.

---

## Phase 3 — Editor pass (prose work; flag/finding remediation)

Dispatch the editor (`staff/editor/card.md`) as a single Agent call. The editor receives:

- `active-project/draft/<slug>.md` (the canonical input — what becomes the polish manuscript)
- `active-project/draft/<slug>.annotated.md` (per-sentence trace; consult when in doubt about whether a line is bone-faithful)
- `active-project/staff/stitcher/render-log-<slug>.md` (full provenance for any sentence)
- `active-project/theater/facets/scene-map-<slug>.md` (scene boundaries + rhythm-shape; informs cross-scene continuity work)
- `active-project/staff/editor/wrap-audience-<slug>.md` (audience flags from Phase 1, if not skipped)
- `active-project/staff/auditor/<slug>-wrap-audit.md` (audit report from Phase 2, if not skipped — SIGNAL findings only; HARDs blocked the phase)
- `active-project/theater/dialogue/<character-slug>.md` for each speaker (utterance verbatim reference — editor does NOT modify these)
- `active-project/theater/facets/exposition-<slug>.md` (exposition gloss reference — editor does NOT modify these)
- `editor-mode: strict | standard | permissive` (cut-aggressiveness override from CLI flag)
- The active project's anti-jargon list, hollow-prose patterns, asinine patterns (from project-default stitch-profile if present)

### The editor's allowed-moves contract

**ALLOWED** — the editor MAY:

- **Prose economy.** Tighten over-qualified phrasing (`seemed to`, `appeared to`, `couldn't help but`, `found himself [verb]ing`); cut thought announcements (`He thought about`, `She wondered if`); cut explanatory echoes (a sentence restating in plain terms what the previous sentence already showed); cut narrator intrusions (stepping outside the POV to explain to the reader); cut told emotion (`felt [emotion]`, `realized`, `understood`, `knew suddenly`).
- **Whole-text variance.** Break percussion that crosses scene boundaries — the scene-window fork could not see this. Specifically: `I + verb` chains across scene seams; opener-form repetition across consecutive paragraphs; same-attribution-verb runs across dialogue scenes; log-trio-form repetition the scene-fork's variant selection couldn't catch at episode scale.
- **Continuity fixes.** Tense, pronoun, possessive register, blocking continuity. Catch errors that crept through Phase 4 voice-transform.
- **Repetition cull.** Remove instances of repeated-with-no-load-bearing-purpose phrasing across the whole text. The protected patterns (log-trio, cardinal-quartet, three-note-buildup) stay protected per their listing in `scene-map-<slug>.md § protected-patterns`.
- **Audience-flag remediation.** Address Phase 1 audience flags. Cut, reword, or re-paragraph as needed. The editor may also override an audience flag (keep the flagged line) if its judgment differs — the override goes in the edit-log with rationale.
- **Auditor-finding remediation.** Address Phase 2 SIGNAL findings (HARDs already blocked). Most SIGNAL findings are surface-level (possessive register, soft Q-checks); editor reworks the surface.
- **Paragraph-break adjustments.** Re-paragraph where the scene-fork's choice doesn't read well at full-text scale. Scene boundaries from scene-map are NOT moved; intra-scene paragraph breaks are the editor's call.
- **Voice consistency.** If the character's voice shifts unexpectedly in one exchange, that exchange is suspect — investigate and fix.
- **Real-opening cut.** Writers warm up. The scene's actual beginning is sometimes a few lines in. Cutting prologue cruft IS allowed even though the cut bones are technically rendered — flag the cut bones in the edit-log (`CUT-BONE-AS-WARMUP @<id>`) so the auditor's BONE-COVERAGE check on the next run knows.

**FORBIDDEN** — the editor MUST NOT:

- **Add plot content** not in the bones or facets. Bone-faithfulness fence persists. New events, new actions, new beats are FAULT-EDITOR-INVENTION territory.
- **Modify dialogue utterance text.** Verbatim invariant from `/and-facets` dialogue authoring holds through editor. Attribution clauses (`he said`) ARE editable; the utterance inside the quotes is NOT.
- **Modify exposition gloss content.** The `<gloss-text>` from `exposition-<slug>.md` was audience-modeled and source-cited at `/and-facets` R2; editor does not re-author. Position/format adjustments OK; content adjustments NOT.
- **Invent characters, places, props, conditions, body details, spatial facts.** The graph is canonical.
- **Re-order scenes.** Scene boundaries from scene-map are fixed. The polish manuscript renders scenes in scene-map order.
- **Re-attribute dialogue.** Speakers from `<X> speaks to <Y>` proto-line bones are fixed.
- **Make plot decisions.** If the manuscript needs a different plot outcome, the editor escalates to user; it does not author the change.
- **Override scene-map's rhythm fields.** The `peak-bones` and `peak-shadow-bones` standalone discipline still holds — editor may not fuse a peak-shadow bone into a longer sentence even if the prose would read smoother.

### Editor procedure

1. **Read everything.** Draft, annotated draft, render-log, scene-map, audience flags, audit findings, dialogue, exposition.
2. **Plan the pass.** List intended moves by category (prose-economy cuts, whole-text variance breaks, continuity fixes, repetition culls, audience-flag remediations, audit-finding remediations, paragraph adjustments). For each, name the target sentence(s) by line excerpt or scene/paragraph reference.
3. **Apply moves in order.**
   - Pass A: HARD-equivalent rule violations (continuity, blocking, audience-flag-shared-by-≥2-personas) — these are the must-fix items.
   - Pass B: Audience flags from individual personas (advisory).
   - Pass C: Auditor SIGNAL findings.
   - Pass D: Whole-text prose pass (economy, variance, repetition, paragraph adjustments, voice consistency).
4. **Per-bone discipline walk.** After all moves, walk the bone-list (from render-log) and confirm each bone still has a renderable trace in the polish manuscript — except for editor-CUT-BONE-AS-WARMUP cases, which are listed explicitly. A bone with no trace and no CUT-BONE entry is `FAULT-EDITOR-BONE-LOST` — restore the bone or document the cut.
5. **Write polish.** `active-project/polish/<slug>.md`. Clean prose, no inline flags, no trace blocks. The editor's draft is the ship-ready manuscript.
6. **Write edit-log.** `active-project/staff/editor/wrap-edit-log-<slug>.md`. Per-move entries:

```
edit-<NNN> <move-class> | <one-line reason>
   from: "<excerpt of original text>"
   to:   "<excerpt of edited text>"
   bones: <@<id>, ...> | none-changed
   audience-flag-addressed: <persona-slug:flag-id> | n/a
   audit-finding-addressed: <finding-id> | n/a
```

Move classes for the edit log:
- `EDIT-PROSE-ECONOMY` — over-qualification cut, hollow pattern cut, etc.
- `EDIT-VARIANCE-CROSS-SCENE` — broke percussion across scene seam
- `EDIT-CONTINUITY` — tense / pronoun / blocking fix
- `EDIT-REPETITION-CULL` — duplicated phrasing removed
- `EDIT-AUDIENCE-REMEDIATE` — addressed an audience flag
- `EDIT-AUDIT-REMEDIATE` — addressed a SIGNAL finding
- `EDIT-PARAGRAPH-BREAK` — re-paragraphed
- `EDIT-VOICE-CONSISTENCY` — voice drift caught and fixed
- `CUT-BONE-AS-WARMUP` — prologue warmup cut; bone(s) in `bones:` field
- `KEEP-OVER-FLAG` — kept a flagged line; reason explains override
- `KEEP-OVER-FINDING` — kept a SIGNAL-finding line; reason explains override

7. **Stats footer in edit-log.**

```
edits: <count> total
  by class: <class>=<count>, ...
audience flags addressed: <N> of <M> ; overrides: <K>
audit findings addressed: <N> of <M> ; overrides: <K>
bones cut: <N> (warmup); rendered: <M>; editor-introduced fault: 0
```

`editor-introduced fault: 0` is mandatory — if the editor's per-bone walk found any FAULT-EDITOR-BONE-LOST it must be resolved before the polish is written. A non-zero count is a wrap failure.

### Editor failure modes

| Fault | Trigger | Recovery |
|---|---|---|
| `FAULT-EDITOR-BONE-LOST @<id>` | Per-bone walk finds a bone with no rendered trace and no CUT-BONE-AS-WARMUP entry. | Restore the bone or add the warmup cut. Re-run editor or escalate to user. |
| `FAULT-EDITOR-DIALOGUE-MODIFIED @<dialogue-id>` | Auditor (Phase 2 re-run on polish, optional) finds the editor changed an utterance. | Restore verbatim from `theater/dialogue/<character-slug>.md`. |
| `FAULT-EDITOR-EXPOSITION-MODIFIED @<exposition-id>` | Editor changed gloss content. | Restore from `exposition-<slug>.md`. |
| `FAULT-EDITOR-INVENTION` | Editor added prose content not in the graph. | Cut the invented content. Surface to user with the quoted invention. |
| `FAULT-EDITOR-CONTINUITY-INTRODUCED` | Editor's edit broke a continuity (changed pronoun and broke blocking, etc.). | Revert the offending edit; address the continuity differently. |
| `FAULT-EDITOR-PROTECTED-PATTERN-BROKEN` | Editor abolished a `protected-patterns` instance from scene-map. | Restore the pattern. Variance within the pattern's variant set is OK; abolition is not. |
| `FAULT-EDITOR-PEAK-SHADOW-FUSED` | Editor fused a `peak-shadow-bones` entry into a longer sentence. | Restore standalone treatment. Peak-shadow discipline is non-negotiable. |

---

## Phase 4 — Memory: minimal movement

After the editor completes:

1. Mark episode status `wrapped` in `active-project/staff/showrunner/memory.md`.
2. Advance `active.episode` only if the just-wrapped slug is the current `active.episode` AND no later episode has already been stitched.
3. **Off-scene event check.** If something significant happened between this episode's bones and the next planned episode (time-skip across episodes, off-screen events established by the next episode's exposition entries), record in the relevant actor LTMs and append to `active-project/staff/showrunner/world-notes.md`.
4. **Actor memory close.** For each actor active this episode: read the polish manuscript and identify any significant events — relationship shifts, discoveries, residue that will carry forward. Append qualifying events to `active-project/actors/<slug>/ltm.md` (format: `[YYYY-MM-DD] EVENT: what changed | why significant`). Then prune `active-project/actors/<slug>/stm.md` to ~10 items: keep only what is genuinely on top of mind going into the next episode. Overwrite STM, do not append. A missing or stale LTM/STM at episode close is a schema violation.

---

## Phase 5 — Present results

```
========================================================
=== /and-wrap COMPLETE: <episode-slug> ===
========================================================

DRAFT IN  : active-project/draft/<slug>.md
POLISH OUT: active-project/polish/<slug>.md

PHASE 1 — Audience review:
  <persona-1>: <N flags>
  <persona-2>: <N flags>
  <persona-3>: <N flags>
  shared (≥2 personas): <N flags>
  STM updates: <persona-list>
  Report: active-project/staff/editor/wrap-audience-<slug>.md
  [or: SKIPPED via --skip-audience]

PHASE 2 — Auditor (rendered-prose audit):
  HARD: <N> (<class-list>)
  SIGNAL: <N> (<class-list>)
  Report: active-project/staff/auditor/<slug>-wrap-audit.md
  [or: SKIPPED via --skip-auditor]

PHASE 3 — Editor:
  Edits: <N> total ; by class: <class>=<count>, ...
  Audience flags addressed: <N> of <M> ; overrides: <K>
  Audit findings addressed: <N> of <M> ; overrides: <K>
  Bones cut as warmup: <N>
  Editor-introduced faults: 0
  Edit-log: active-project/staff/editor/wrap-edit-log-<slug>.md

WORD-COUNT DELTA:
  draft: <N> words
  polish: <N> words (delta: <±N>)

NEXT EPISODE: <slug>  [or: season complete]

[Episode wrapped. Review polish/<slug>.md or proceed to next.]
```

If escalations require human decision (HARD audit findings, structural escalations, plot-decision requests), present them before the closing line under `ESCALATIONS REQUIRING YOUR DECISION:`.

---

## Re-wrap on feedback

If the polish manuscript needs revision after a wrap completes (user notes, second-pass review), re-run `/and-wrap <slug>`. The pre-flight check will detect existing wrap log files and prompt:
- Delete the wrap log files to re-run from scratch (full audience + auditor + editor)
- Or pass `--skip-audience` and/or `--skip-auditor` to re-run only the editor against existing logs

A re-wrap with all three phases re-running produces fresh audience flags (audience STM is read but the new review supersedes — STM accretes) and a fresh auditor pass. The editor reads the new flags and findings.

---

## Exit conditions

- **Success.** Polish manuscript written, edit-log finalized, memory updated, no editor-introduced faults.
- **Phase 0 abort.** Missing inputs (draft, render-log, scene-map, facets, audience personas). Print missing path and exit.
- **Phase 1 fault.** Audience persona dispatch failed or didn't write to STM. Re-dispatch the affected persona; persona STM-write is mandatory.
- **Phase 2 HARD findings.** Auditor returned HARD-class findings against the rendered prose. Editor cannot proceed; route HARDs to fixer or escalate to user. The polish is not written.
- **Phase 3 editor-introduced fault.** Editor's per-bone walk found a bone-loss or the editor modified dialogue/exposition. Restore from source or escalate.
- **Mid-phase fault.** Any per-fork dispatch returns a validation fault. Phase pauses; fault logged; re-dispatch after fix.

---

## What this command does not do

- Does not modify proto-lines, facets, dialogue, exposition, or scene-map. The graph is canonical; the editor renders surface, not source.
- Does not re-stitch. Stitcher is upstream (`/and-stitch`); if the draft has structural issues only re-stitching can address, escalate rather than editing around them.
- Does not author new dialogue. Dialogue gaps surface as `/and-facets` re-runs, not editor authoring.
- Does not parallelize across episodes. One episode per dispatch.

---

## Versioning note

This is `/and-wrap` v2 (URI-WRAP-V2, 2026-05-13). v1 lives at `archive/commands/and-wrap.md`; it operated on the v1 `show.md` artifact from per-line shoot and is no longer applicable. v2 operates on the stitcher's `draft/<slug>.md` from `/and-stitch`.
