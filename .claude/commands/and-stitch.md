---
description: Stitcher pipeline for one chapter. Eight render phases + a terminal cold-read gate — lens-anchored render → redundancy cull → compression → voice transform → local flow (speaker-paragraph breaks) → buildup preservation → editorial reflection → finalize (strips scene-callout markers) → cold-read terminal gate (Phase 9, blocking). Output - draft/<book>-<chapter>.md + draft/<book>-<chapter>.annotated.md + staff/stitcher/render-log-<book>-<chapter>.md. URI-SUBSTANCE-OVERHAUL (2026-05-17): bones-path renamed; tensometer-derivation fallback removed; speaker-paragraph rule enforced at Phase 5; scene-callout markers stripped at Phase 8. Usage - /and-stitch <book>-<chapter> [--profile <path>] [--persona <slug>] [--phase-1-mode <scene-window|per-anchor>]
---

Stitcher pipeline. One chapter in, clean draft + annotated traced draft + per-fork render-log out. The stitcher assembles a prose draft from the bones and the facet graph; each phase forks at its natural decision granularity (per-anchor, per-paragraph, per-window, per-sentence, etc.). No inter-fork memory; the render-log is the only cross-phase artifact.

**URI-SUBSTANCE-OVERHAUL (2026-05-17) mutations:**
- Phase 0 reads `theater/bones/<book>-<chapter>.md` (not `theater/proto-lines/<slug>.md`). Slug-arg shape: `<book>-<chapter>` (e.g. `b01-c01`).
- Phase 0 scene-boundary detection no longer falls back to tensometer derivation. The scene-map facet is emitted upstream by `/and-write` Phase 7 and validated at `/and-facets` Phase 4d; if missing, Phase 0 fault-aborts or falls back to per-anchor mode per profile (no tens-parse path).
- Phase 5 (local flow) enforces a hard rendering rule: **any new speaker starts a new paragraph.** Each `speaks to` bone's rendered dialogue paragraph begins on its own line.
- Phase 8 (finalize) HARD-strips any surviving `## Scene N` / `[SCENE BREAK]` / `--- SCENE ---` markers from `draft/<book>-<chapter>.md` (clean). The annotated draft may retain machine-readable scene markers.

Under the polish-deferred boundary, `draft/<book>-<chapter>.md` is the terminal deliverable. No `/and-wrap` editor pass follows.

Dialogue and exposition are both **graph-resident facets** consumed by the stitcher (not authored by it). Exposition feeds the preamble + per-anchor first-mention/scene-orient glosses; dialogue feeds the verbatim utterance for every `X speaks to Y` proto-line bone. Both are loaded at Phase 0.6 / 0.7 and surfaced to Phase 1 forks as license to render content the bone-faithfulness fence would otherwise forbid.

You are the orchestrator. Eight render phases plus a terminal cold-read gate (Phase 9) run in strict sequence:

```
theater/bones/<book>-<chapter>.md + theater/facets/* + theater/dialogue/<character-slug>.md + theater/facets/_cite-index.md
        │
        ▼
   PHASE 0 — VALIDATE + LOAD
            Resolve profile (scene override → episode → project → schema default).
            Resolve persona. Read feedback-<slug>.md if present.
            Initialize render-log.
        │
        ▼
   PHASE 1 — LENS-ANCHORED RENDER (per-anchor forks)
            For each anchor: load lenses (NI, mem, sensory, feel);
            apply lens decider (rules 1–6); render bone through lens hierarchy.
            Paragraphs serial; anchors within parallel by default.
        │
        ▼
   PHASE 2 — REDUNDANCY CULL (per anchor + echo window)
            Closing-phrase echo + image-set-overlap detection across co-anchored
            and window-adjacent facets.
        │
        ▼
   PHASE 3 — COMPRESSION (per merge-candidate run)
            Same-subject merges; pronoun substitution after first mention;
            flat-low zero-cite collapses (respecting protected patterns).
        │
        ▼
   PHASE 4 — VOICE TRANSFORM (per paragraph)
            Tense + person shifts; POV-pronoun resolution; third-party preserve;
            bone-object-policy; sensory arrow rendering.
        │
        ▼
   PHASE 5 — LOCAL FLOW (per sliding window)
            Within-anchor reorder; forward sensory deferral; backward NI promotion;
            un-merge to rescue swallowed facets. Refuses on temporal-lock / cross-bone / cross-scene.
        │
        ▼
   PHASE 6 — BUILDUP PRESERVATION (per protected pattern)
            Detect and restore countdowns / three-beat rhythms / threshold sequences.
            Flag PATTERN-ABANDONED when protective facet was cut at Phase 7
            (downstream signal back to Phase 7's bones-cuttable license).
        │
        ▼
   PHASE 7 — EDITORIAL REFLECTION (per sentence, the only taste pass)
            Q1–Q9 binary answers under strict-Q-mode. Routes to CUT / CUT-CLAUSE /
            CUT-ASININE / CUT-HOLLOW / CUT-BONE / RESHOW / REWORD / SIMPLIFY-PUNCT.
            Bones cut only under bones-cuttable license (anchor-also-cut).
            RESHOW requires ≥2 graph sources. REWORD density-capped at 2/sentence.
        │
        ▼
   PHASE 8 — FINALIZE (single)
            Assign stable line-IDs (gaps allowed).
            Write draft/<slug>.md (clean) + draft/<slug>.annotated.md (traced).
            Finalize render-log + STATS + RECONCILE.
        │
        ▼
   PHASE 9 — COLD-READ TERMINAL GATE (blocking)
            One uninformed general-purpose agent reads draft/<slug>.md cold
            (no bones, no facets, no chunk) and answers the reader's questions.
            Additive editorial pass (EXPAND/GROUND/STAGE/NEEDS-BEAT) fires alongside.
            Cold-read FAIL routes to /and-write revise. PASS declares the chapter terminal.
```

Phase 1 and 7 are per-line phases (per-anchor / per-sentence forks). Middle phases fork at larger but still-small decision units. The agent definition and active persona are shared across forks within a phase (system-prompt-stable, user-turn-per-fork pattern); each fork loads minimal additional context for its decision.

## Args

- `$1` — optional. Chapter slug (e.g. `b01-c01` or `b01c01`; normalized to `<book>-<chapter>` form at Phase 0). If omitted, use `active.chapter` from `active-project/staff/showrunner/memory.md`.
- `--profile <path>` — optional. Override the active profile path. Default: `active-project/theater/stitch-profile.md`.
- `--persona <slug>` — optional. Override the active persona. Default: read from profile's `persona:` field; fallback `neutral`.
- `--allow-bare-speech` — optional. Explicit opt-in to the legacy silent-speech fallback (Phase 0.7 § Legacy fallback). Without this flag, an episode with `speaks to` bones and an empty/missing dialogue facet HARD-ABORTS at Phase 0.5; the user must run `/and-facets <slug>` first. Pass this flag only when knowingly stitching a pre-2026-05-12 episode whose dialogue facet cannot be retroactively authored. Marked in the render-log header.
- `--keep-drafts` — optional. Retain the Phase 1–7 `<slug>.phase-*.draft.md` intermediate files in `active-project/draft/` after a successful run. Default behavior at Phase 8 is to prune them (the render-log retains the trace; the drafts are reproducible). Debugging use only.
- `--phase-1-mode <scene-window|per-anchor>` — optional. Override the active profile's `phase-1.mode` field. Default resolves from profile; schema default is `scene-window` (URI-SCENE-WINDOW, 2026-05-13). `scene-window` dispatches one fork per dramatist-marked scene with overlap-read context (back-look on prior rendered scene; forward-look on next scene's bones+facets) — see § "Phase 1 — scene-window mode" below. `per-anchor` is the legacy fallback: one fork per bone with `continuity-context` lookback. Use per-anchor when the scene-map facet is absent, when the episode has low percussion accumulation (modes converge), or for fork-isolation debugging.

---

## Phase 0 — Validate + Load

1. Resolve chapter slug. Normalize to `<book>-<chapter>` form. Verify `active-project/theater/bones/<book>-<chapter>.md` exists.
2. Verify `active-project/theater/facets/_cite-index.md` exists. Abort if not — stitcher requires the cite-index from `/and-facets`.
2a. If resolved `phase-1.mode` is `scene-window` (the default) and `scene-window.boundary-source` resolves to `scene-map-facet` (the default), verify `active-project/theater/facets/scene-map-<slug>.md` exists. If absent: emit `WARN-SCENE-MAP-FACET-ABSENT`, fall back per `phase-1.scene-window.fallback-on-no-scene-map` (default `per-anchor` — soft fallback recorded in render-log header). With `escalate`, abort and surface `FAULT-PHASE-1-NO-SCENE-MAP` to the user.
3. **Profile resolution.** Read in order:
   - Per-scene profile if any matches the active scene (`stitch-profile-<scene-label>.md`)
   - Episode default (`active-project/theater/stitch-profile.md`)
   - Project default (`active-project/stitch-profile.md`) if present
   - Schema defaults from `schemas/stitch-profile.schema.md`
   Shallow-merge top-down. Validate per the schema's fault list.
4. **Persona resolution.** Load `active-project/staff/stitcher/personas/<active>.md` (or library fallback `staff/stitcher/personas/<active>.md`). Default `neutral` if profile carries no `persona:` field. Validate persona's lens-bias and Phase-7-bias tables against the schema.
   - **Project-mismatch check.** If resolved persona is `neutral` AND `active-project/stitch-profile.md` declares a non-neutral persona OR `active-project/staff/stitcher/personas/` contains a project-scoped persona card: emit `FAULT-PROFILE-PERSONA-MISMATCH-PROJECT` and escalate to user. Do not proceed until user either (a) corrects the profile or (b) passes `--persona neutral` explicitly as an override. Silent `neutral` against a tuned project is the canonical failure mode for this pipeline.
5. **POV resolution.** Read `narrator:` from the bones file header (`active-project/theater/bones/<book>-<chapter>.md` § `narrator:` field — the seven-field extended header per `schemas/bones.schema.md`). If profile's `voice.pov` is unset, use the header value. Fault if both are absent.
6. **Scene boundary detection.** Default (scene-window mode): scene boundaries are sourced at Phase 1 from `active-project/theater/facets/scene-map-<book>-<chapter>.md` (per the scene-window mode's Scene-boundary resolution below); no Phase 0 work needed beyond verifying the scene-map facet exists per step 2a. Per-anchor mode (opt-in fallback): paragraph breaks fall on scene boundaries derived during Phase 1 fork-by-fork, or on explicit time-skip blanks in the bones file.
7. **Feedback intake (if present).** Read `active-project/staff/stitcher/feedback-<slug>.md`:
   - Line-level directives (CUT/KEEP/MERGE/UNMERGE/LENS/RESHOW-REVERT/REWORD-REVERT) → write to `anchor-overrides:` block in a session-scoped profile copy (do not mutate the canonical profile)
   - Pattern-level entries (PATTERN blocks) → flag for human review; do not auto-apply unless explicitly PROMOTED
   - Free-form notes → list in render-log Phase 0 entry for human review
8. **Initialize render-log.** Create `active-project/staff/stitcher/render-log-<slug>.md` with header (profile path, persona slug, narrator, voice config, phase-7-mode, generated-date).
9. **Parking-lot scan (Rule 14).** Read `active-project/staff/showrunner/parking-lot.md`. Items matching this invocation (`target.command: /and-stitch` + `target.scope` = `<book>-<chapter>` or `*` wildcard + `status: open`): HARD → abort unless this run resolves; SOFT → carry to the Phase 9 cold-read summary + render-log Phase 0 entry. Resolving phase stamps `resolved_at` + `resolved_by` + `resolution_note`; never delete.

State machine: showrunner memory `stitched: false` → in-progress → `stitched: true` at Phase 8 completion.

---

## Phase 0.5 — Pre-flight summary (user-visible gate)

Before dispatching Phase 1, emit a one-screen summary to the user:

```
/and-stitch pre-flight for <slug>:
  persona:          <slug>           # FAULT if neutral and project has tuned persona
  voice:            <person>-person <tense>-tense, contractions <on/off>
  POV:              <actor-slug>
  anchors:          <N>              # from bones file (theater/bones/<book>-<chapter>.md)
  scenes:           <M>              # from scene-map facet (theater/facets/scene-map-<book>-<chapter>.md)
  phase-1 forks:    <M scene-forks>  # or <N per-anchor forks> if dispatch-budget allows
  phase-7 forks:    <M scene-forks> per-sentence inside
  anti-jargon:      <K tokens loaded from project.anti-jargon>
  hollow patterns:  <K patterns loaded>
  asinine patterns: <K patterns loaded>
  bone-fence:       enforced (dialogue=no, body=no, spatial=no, route=no, scene-prose=no, cognitive=no)
  feedback-file:    <present | absent>
  exposition:       <present | ABSENT (legacy-fallback)>
                    if present: <N> entries (preamble=<n>, first-mention=<n>, scene-orient=<n>; refused-at-R2=<n>)
                    cross-episode register: <N> terms reader-resident from prior episodes
  phase-1-mode:     <scene-window | per-anchor>     # from profile.phase-1.mode; default scene-window
                    if scene-window: <S> scene-forks (boundaries from scene-map facet; tensometer fallback removed under URI-SUBSTANCE-OVERHAUL 2026-05-17)
                    if per-anchor:   <N> per-anchor forks (fallback mode; ad-hoc or legacy episodes)
  output-dir:       active-project/draft/           # stitcher output (not polished — editor pass lands in active-project/polish/)
  dialogue:         <present | ABSENT (no-speech-episode | legacy-fallback)>
                    if present: <K> character files, <N> total utterances
                    anchors covered: <M> of <S> "speaks-to" bones in proto-lines
                    unmoored utterances: <U>  # entries whose @anchor has no matching proto-line
                    bare speech bones: <B>    # "speaks-to" bones with no dialogue entry — flagged for re-author
```

This summary is the gate. If anything looks wrong (persona is `neutral` when it shouldn't be; anti-jargon list is empty when the project has one; voice config is unexpected; exposition is absent for a project where it should exist), the user catches it here, not at the polish file 1,500 words later. **`exposition: ABSENT` on a project that has run `/and-facets` post-2026-05-12 is a strong signal something went wrong upstream** — re-run `/and-facets` rather than proceeding with legacy fallback.

**Dialogue gate (URI-DIALOGUE-COVERAGE-GATE, 2026-05-12) — HARD STOP, not advisory.** If proto-lines contains any `speaks to` bones (`S > 0`) AND any of the following hold, ABORT before Phase 1 dispatch:
- `dialogue: ABSENT` (no files under `theater/dialogue/`), OR
- `bare speech bones: > 0` (any `speaks to` proto-line has no `<character-slug>:<id>` citation), OR
- any speaker subject of a `speaks to` bone has no `theater/dialogue/<slug>.md` file.

The abort message names the missing files / bare bones / missing speakers and recommends `/and-facets <slug>`. This mirrors the `/and-facets` Phase 6a dialogue-coverage precondition; the stitcher refuses to consume a graph that the facet pipeline should not have finalized. **Opt-out**: pass `--allow-bare-speech` to proceed with the legacy silent-speech fallback (Phase 0.7 § Legacy fallback) — reserved for pre-2026-05-12 episodes whose dialogue facet cannot be retroactively authored. The flag is recorded in the render-log header. The default — silent invention of dialogue or silent rendering of speech beats as silent action without the user's explicit consent — is the canonical FAULT-DIALOGUE-MISSING failure mode and is structurally prevented.

---

## Phase 0.6 — Read exposition facet (preamble assembly)

The exposition facet is authored upstream at `/and-facets` time by the `exposition-author` subagent. Phase 0.6 reads that facet and assembles the preamble. **This phase does NOT dispatch an Agent call** — exposition is graph-resident, audience-modeled, source-cited, and already-judged through R2 + audit + audience-gate. The stitcher's job is to **consume** it, not re-author it.

**1. Read exposition facet.**
- Load `active-project/theater/facets/exposition-<slug>.md`.
- If absent: **fallback mode** — emit `WARN-EXPOSITION-FACET-ABSENT` to the user and dispatch the legacy interval-bridge fork (see § Legacy fallback below). This path exists for episodes authored before exposition was wired upstream; flag for `/and-facets` re-run when convenient.
- If present: parse entries; categorize by scope.

**2. Categorize entries.**
- **Episode-open pool**: entries with `scope: episode-open-preamble`, `scope: episode-open-context`, or `scope: prior-episode-bridge`. Always at `@0` (synthetic anchor). These render as the preamble.
- **Per-anchor first-mention pool**: entries with `scope: first-mention-term`, `first-mention-object`, `first-mention-place`. Keyed by `@<anchor>`. These fold in during Phase 1 forks at their cited anchors.
- **Per-anchor scene-orient pool**: entries with `scope: scene-open-orient`. Keyed by `@<anchor>`. Render at scene-open during Phase 1, BEFORE the scene's first bone-rendered sentence.
- **Refused/dropped entries**: if any entry in the file has a `refused: <reason>` field or has been DELETED at R2 (gap-line in monotonic ID sequence with `# DELETED` comment), skip — do not render. The R2 judge's refusals are the canonical authority.

**3. Assemble preamble.**
Order the episode-open pool by entry ID. Render each in sequence:
- `renders-as: italic-preamble` → italicized paragraph.
- `renders-as: preamble-paragraph` → italicized paragraph following the preamble (the preamble can be one paragraph or several; the schema allows ≤4 episode-open entries total).
- Apply voice transform per profile `voice.person` and `voice.tense` (the exposition-author's R1+R2 should have rendered in the profile's voice, but the stitcher re-checks: any 3rd-person pronouns in entries where `voice: pov-frame: first-person` is profile-default trigger a **fault** at this phase — emit `FAULT-EXPOSITION-VOICE-MISMATCH` and either auto-rewrite via REWORD or escalate to user).
- Separate the preamble block from the body with a single horizontal rule (`---`).

**4. Write preamble artifact.**
Save assembled preamble to `active-project/draft/<slug>.preamble.md`. Phase 8 prepends this to the final polish.

**5. Stage anchor pools for Phase 1.**
Make the first-mention pool and scene-orient pool available to Phase 1 fork dispatches. Each scene-fork's input payload now includes:
- The exposition entries firing at its anchor range (per their `@<anchor>` keys).
- The `renders-as` directive for each entry.

**Render-log entries** under `## Phase 0.6 — exposition consumption`:
- The full preamble as rendered.
- For each preamble entry: source-claim mapping (already cited by the facet; the render-log copies this for the auditor's trace).
- Total entries categorized by scope; refused-at-R2 entries listed for the auditor.

### Legacy fallback (when exposition facet absent)

If `active-project/theater/facets/exposition-<slug>.md` does not exist:

1. Emit `WARN-EXPOSITION-FACET-ABSENT` to the user. Recommend `/and-facets <slug>` re-run to author the missing facet.
2. Read the legacy `interval-bridge:` block from the resolved profile (still defined in `schemas/stitch-profile.schema.md` for backwards-compat).
3. Dispatch the legacy interval-bridge fork as previously specified. The fork's output is provisional — the auditor will not have source-traceability for it because no upstream facet authored the content with cited sources. Flag the polish in the render-log as `legacy-preamble-from-stitcher-fork` so downstream consumers know.

This fallback is for transition — episodes authored under the old pipeline still produce. New episodes (post 2026-05-12) should always have an exposition facet from `/and-facets`. The fallback path will be deprecated once all in-flight episodes have been re-audited.

**Why this design:** for the first episode of a series, the reader has no graph context — the bones+facets assume the upstream graph as background, but the polish is supposed to read standalone. For subsequent episodes, the reader has time between sessions and needs a recap. AND for any episode, audience-specific terms / objects / places require glossing for the union-of-personas-gap. The exposition facet handles all three as one upstream-authored-and-audited problem — bridge the implicit/explicit gap between the prior chapter's end and this chapter's start, plus brief in-line glosses for what the audience can't be expected to know, all source-cited and audit-gated. The stitcher is the renderer, not the author.

---

## Phase 0.7 — Read dialogue facets (utterance assembly)

The dialogue facet is authored upstream at `/and-facets` time by the per-character `dialogue-writer` fork (one file per speaking character — see `schemas/dialogue.schema.md`). Phase 0.7 reads those files and builds an anchor→utterance lookup that Phase 1 forks consume. **This phase does NOT dispatch an Agent call** — dialogue is graph-resident, voice-shaped against each character's behavior card, audience-modeled, and audit-gated upstream. The stitcher's job is to **render**, not re-author or re-voice.

**1. Read dialogue files.**
- Enumerate `active-project/theater/dialogue/*.md`. Each file is one character's utterances across the episode.
- For each file, read frontmatter: `character:`, `episode:`, `behavior-card:`. Reject (warn-and-skip) any file whose `episode:` does not match the active episode slug.
- If the directory is empty AND the proto-lines file contains any `<X> speaks to <Y>` bones: **HARD ABORT by default** (URI-DIALOGUE-COVERAGE-GATE) — emit `FAULT-DIALOGUE-FACET-ABSENT` to the user with the count of bare speech bones and the recommendation to run `/and-facets <slug>`. Phase 0.5's gate should have already caught this; reaching here means the gate was bypassed or the directory was emptied between Phase 0.5 and Phase 0.7 — surface as a build defect. **Only** when `--allow-bare-speech` was passed at command-invocation time does this drop through to legacy silent-action mode (`he turned to her` rather than `he said "..."`), logged as `LEGACY-SILENT-SPEECH` per bone.
- If the directory has files but a specific speech bone has no anchored utterance: **HARD ABORT by default** — emit `FAULT-DIALOGUE-MISSING-AT-<anchor>` with the bare bone IDs listed; recommend `/and-facets <slug>` re-run so the dialogue-writer fork can author the missing utterances. With `--allow-bare-speech`, the Phase 1 fork for that anchor renders silent action and logs the fault (legacy behavior).

**2. Build the anchor→utterance lookup.**

Parse every entry under each character file:

```
<id> @<proto-line-id> | <objective> | <utterance>
```

Index by `@<proto-line-id>` into a map:

```
dialogue-by-anchor[<proto-line-id>] = [
  { character: <slug>, dialogue-id: <id>, objective: <text>, utterance: <text>, behavior-card: <slug> },
  ...
]
```

Multiple utterances may share an anchor (multi-utterance exchange under one bone). Preserve **file order** within an anchor — the dialogue-writer fork authored them in screen-time order; the stitcher renders them in that order under the bone's beat.

**3. Cross-validate against proto-lines.**
- Every `<X> speaks to <Y>` bone in proto-lines should have ≥1 entry in `dialogue-by-anchor[<that-bone-id>]`. Bones with no entry → log `BARE-SPEECH-BONE` (count surfaces at Phase 0.5).
- Every entry in `dialogue-by-anchor` should point at a `<X> speaks to <Y>` bone whose speaker matches the entry's `character:`. Mismatches → log `DIALOGUE-SPEAKER-MISMATCH` (e.g. entry from `oc-tanner-father` keyed `@15` but proto-line 15 is `taylor speaks to ...`).
- Entries with `@anchor` not present in proto-lines → log `UNMOORED-UTTERANCE`. These will not render (no bone to attach to).

These cross-checks surface to Phase 0.5 pre-flight and to the render-log under `## Phase 0.7 — dialogue intake`. They do not halt the run unless `--strict-dialogue` is set on the call.

**4. Stage anchor pools for Phase 1.**
The `dialogue-by-anchor` map is made available to Phase 1 fork dispatches. For each fork whose anchor is a speech bone, the fork's input payload includes:
- Every utterance entry keyed at that anchor (verbatim).
- Each entry's `character:` slug (to drive attribution) and `behavior-card:` slug (to drive attribution-verb constraints).

**Render-log entries** under `## Phase 0.7 — dialogue intake`:
- Per character file loaded: filename, entry count, behavior-card slug.
- Summary table: anchors covered / total speech bones; bare bones (with anchor IDs); unmoored utterances; speaker mismatches.
- The dialogue-writer's authored objectives are preserved in the log for the auditor's trace, but they do NOT render in the polish — only utterances do.

### Legacy fallback (when dialogue facet absent — opt-in only via `--allow-bare-speech`)

For episodes authored before the dialogue facet was wired upstream, and only when the user has passed `--allow-bare-speech` at command-invocation:

1. Emit `WARN-DIALOGUE-FACET-ABSENT` with the count of speech bones.
2. Phase 1 forks for those bones render silent action only — `he turned to her, mouth closing on the word he didn't say` is acceptable; `he said "no"` is not. The bone-faithfulness fence holds: no invented dialogue.
3. Flag every silent-speech bone in the render-log as `LEGACY-SILENT-SPEECH`. The polish is provisional — re-run `/and-facets <slug>` to author the missing utterances and re-stitch.

Without `--allow-bare-speech`, this path is unreachable — Phase 0.5 and Phase 0.7 step 1 hard-abort first. This is the structural prevention of FAULT-DIALOGUE-MISSING.

**Why this design:** dialogue is character voice, not narrator voice. Letting the stitcher invent dialogue under the bone-faithfulness fence violates the character primitive's exclusive authority over what their characters say. Authoring dialogue upstream as a per-character fork (one hermetic run per character, loading their behavior card + ltm + stm + state) is the only place where the voice is correctly shaped against the union-of-prompts that character has across the whole episode. The stitcher is the renderer — verbatim utterance + connective attribution, nothing more.

---

## Phase 1 — Lens-anchored render

**Hard rule: forks only, no orchestrator-inline rendering.** The `/and-stitch` command body MUST dispatch Agent calls to produce Phase 1 prose. The orchestrator's job is to fan out, collect, assemble — never to render. A Phase 1 prose block in the polish file that does not correspond to a fork-id entry in the render-log is `FAULT-PHASE-1-CONSOLIDATED` and the run must be re-dispatched. (See `staff/stitcher/card.md § Pet Peeves "orchestrator-consolidated Phase 1"`.)

**Dispatch granularity (per-anchor mode).** One Agent call per @N. **Default mode is scene-window** (see § Phase 1 — scene-window mode below); the per-anchor procedure documented in the rest of this section runs only when `phase-1.mode: per-anchor` is set in the profile or `--phase-1-mode per-anchor` is passed at the command line. If running per-anchor and the episode's anchor count exceeds the session's practical dispatch budget, batch to per-scene (one Agent call per scene; the subagent walks anchors serially within scene with previous-2-lines continuity, applies the lens decider one anchor at a time, and returns rendered prose + per-anchor log entries). Per-scene batching of per-anchor forks is acceptable; orchestrator inline rendering is not. Document the dispatch granularity in the render-log header. Note: the per-scene *batching* form (anchor-by-anchor inside scene) is distinct from scene-window *mode* (one render covering the whole scene with overlap-read context) — see scene-window section below.

Per-fork dispatch:
- Shared inputs (cached, loaded once per Phase 1 dispatch): stitcher card, active persona, active profile
- Per-fork inputs:
  - The bone at @N (verbatim)
  - The facets at @N (verbatim — narrator, memory, sensory, feel that fire)
  - **Exposition entries at @N** (verbatim from `exposition-<slug>.md` per Phase 0.6 staging): any `first-mention-*` or `scene-open-orient` entries keyed to this anchor, with their `<gloss-text>`, `scope`, and `renders-as` directive. These are graph-resident license to render the gloss content — the fork MUST fold the gloss exactly as specified by `renders-as`, NOT rewrite or invent around it.
  - **Dialogue entries at @N** (verbatim from `dialogue/<character>.md` per Phase 0.7 staging): for a `<X> speaks to <Y>` speech bone, every utterance keyed `@N` with its `<character>`, `<dialogue-id>`, `<behavior-card>`, and `<utterance>` (and `<objective>` for trace). These are graph-resident license to render character speech — without them, the bone-faithfulness fence forbids speech. Multi-utterance anchors render in file order under one beat.
  - Scene label
  - Narrator slug (POV)
  - Previous 1–2 rendered lines in same paragraph (per `phase-1.continuity-context`)
  - **Project anti-jargon list** (from active profile's `project.anti-jargon`) — fork must REWORD or drop any token on this list at render time
  - **Project hollow-prose patterns** (from `project.hollow-prose-patterns`) — fork must not produce these surface forms; cut at render
  - **Project asinine patterns** (from `project.asinine-patterns`) — fork must reshow or drop
  - **Bone-faithfulness fence** (from `project.bone-faithfulness-fence` + card § Bone-faithfulness fence) — fork must not invent dialogue / body / spatial / route / scene / cognitive detail
- Per-fork output:
  - One or more sentences for @N (multi-line at peaks where multiple facets render; exposition fold-in counts as graph-resident, not invention)
  - Render-log entry (fork-id, lens-decider trace, structural-decision, exposition entries folded with their render-as positions, any pre-empted Q5/Q8/Q9 cut)

### Exposition fold-in mechanics

When an exposition entry fires at the fork's anchor, the fork renders it per its `renders-as` directive (defined in `schemas/facet.schema.md` § exposition):

| renders-as | Where the gloss text lands |
|---|---|
| `scene-bridge` | Single short sentence at the scene-open, BEFORE the first bone's rendered prose for the scene. Renders only on the first anchor of a new scene (post-time-skip-blank). |
| `inline-appositive` | Em-dash appositive immediately after the first-mention noun in the bone-rendered sentence: `"the reeve — the lord's bookkeeper — came through the gate"`. |
| `em-dash-fold` | Em-dash phrase mid-sentence: `"the morning bowl — porridge and salt — on the table"`. Functionally similar to inline-appositive but more flexible on placement (mid-sentence vs immediately-after-noun). |
| `parenthetical-aside` | Parenthetical immediately after the first-mention sentence: `"He spoke to the reeve. (Our reeve was the lord's hand for village peace.)"`. Reads as narrator-aside; acceptable in first-person pov-frame. |
| `post-bone-clause` | Full clause after the bone, period-separated: `"He opened the book. Different rank than the reeve — he rode from the lord himself."`. Heavier than appositive; reserved for content that needs sentence-length. |
| `italic-preamble` / `preamble-paragraph` | Handled at Phase 0.6 (preamble assembly); does NOT appear in Phase 1 fork outputs. |

**Hard rule: the fork renders the gloss text VERBATIM modulo voice-transform.** The exposition-author's R1+R2 already shaped the gloss for audience-fit, anti-jargon, hollow-prose, asinine, voice. The fork does not re-author. The fork applies only:
- Voice transform (tense/person/contractions) per the active profile.
- The `renders-as` positional placement.
- POV-pronoun resolution if the gloss uses 3rd-person pronouns the profile says should be 1st-person.

**Cross-episode register check (informational only).** The fork can check `active-project/staff/exposition-author/glossed-terms.md` to see which terms were glossed in prior episodes. The R2 judge should have already culled re-gloss entries; if one slips through, the fork emits a `WARN-EXPOSITION-REGLOSS` to the render-log but still renders (the judge's call is canonical; the warning is for the next-episode auditor to catch).

### Dialogue fold-in mechanics

When the fork's anchor is a `<X> speaks to <Y>` proto-line bone, every dialogue entry keyed `@N` renders under that bone. Dialogue is graph-resident: the bone-faithfulness fence's `dialogue=no` clause forbids **invented** dialogue, not **facet-licensed** dialogue. The fork:

| step | rule |
|---|---|
| **Verbatim utterance** | Render the `<utterance>` field exactly as authored. No paraphrase, no re-voicing, no rewording — even Q9 anti-jargon is **not** applied to utterances at Phase 1 (the dialogue-writer fork loaded the project anti-jargon list and the character's behavior card; a Q9 hit on a finalized utterance is `FAULT-DIALOGUE-AUDIT-MISS` for the auditor, not a stitcher rewrite license). |
| **Attribution** | Generated as connective tissue only. Use the speaker's display name (resolved from the character's persona card, NOT the slug). Verbs constrained to: `said`, `answered`, `replied`, `asked` (default); plus any verb explicitly listed in the speaker's behavior-card `preferred-attribution-verbs:` field if present. No invented verbs (no `intoned`, `growled`, `whispered` unless the behavior card lists them). |
| **Beat placement** | Attribution may precede, follow, or split the utterance per voice-fit. Single-utterance anchor: `He said, "<utterance>"` or `"<utterance>," he said.` Multi-utterance same-anchor (file-order preserved): render successive utterances under one attribution if the speaker is the same; introduce a fresh attribution when the speaker changes within the anchor. |
| **POV reference** | If the speaker is the narrator (POV actor), use first-person pronoun per `voice.person` and the active profile. Third-party speakers keep their display name on first mention in a scene; pronoun thereafter per `voice-transform.third-party-preserve`. |
| **Multi-speaker anchor** | When `dialogue-by-anchor[@N]` lists entries from multiple speakers (the bone is `X speaks to Y` but Y's response shares the anchor), render in file order, switching attribution per speaker. The render-log notes `MULTI-SPEAKER-ANCHOR @N`. |
| **Sensory + feel co-citations** | When a speech bone co-cites `feel:` or `sensory:` facets, render those per the standard lens decider as accompanying narration (before, after, or splitting the utterance). The lens decider's scene-map peak/flat-low rule (under `rhythm-shape` + `peak-bones`) still governs whether feel/sensory beats the speech beat for the sentence rhythm. Default neutral-kinetic order: speech first, then feel/sensory beat. |

**Bare speech bone (no dialogue entry):** the fork renders silent action only. Acceptable: `He turned to her, mouth opening on a word that did not arrive.` Unacceptable: any speech-shaped clause with a quote, or any paraphrase-of-content. Log `LEGACY-SILENT-SPEECH @N` and `FAULT-DIALOGUE-MISSING @N`. The user sees the count at Phase 0.5 and at Phase 8 STATS; the polish is provisional until the dialogue facet is re-authored.

**Render-log per fork (speech bones):** the fork-id line names the dialogue entries folded (`folded: dialogue:<character>:<id>, dialogue:<character>:<id>`), the attribution verb chosen, and the speaker-attribution-form (display-name / pronoun / first-person).

### Sensory + loc-state co-anchor fold

When the fork's anchor co-cites a `sensory:` facet AND a `loc-state:` facet at the same anchor (e.g. an entry beat where the POV crosses a threshold and the location-state's composite-state + observable-affordance fire alongside a sensory drop or spike), the fork MUST render the two as one perceptual unit in a single sentence, NOT split them across two sentences.

The pattern this rule prevents: bone renders as sentence 1, loc-state details land as a free-standing fragment sentence 2 with no subject and no verb. From s01e02 dogfood — `"The daylight dropped as I stepped in. Empty room, alley-sound through the second-floor window."` The fragment second sentence reads as stitcher stage-direction rather than lived perception.

The correct rendering folds the loc-state details into the bone-plus-sensory sentence via em-dash, comma-appositive, or participial clause:
- `"The daylight dropped when I stepped inside — the room empty, alley sound through the second-floor window."`
- `"I crossed the threshold into the dim of the room, the second-floor window carrying alley sound."`

The fork chooses the form that fits the rhythm; the rule is that they render together, not the form they take. The loc-state detail does not get its own sentence at an entry beat — it folds into the entry sentence. The bone-faithfulness fence still holds: the loc-state phrasing must come from the loc-state facet entry, not be invented.

This rule fires when:
- A `sensory:` facet and a `loc-state:` facet both cite the same `@N`
- The fork is rendering a threshold-cross / entry / scene-open beat (not a peak inside a scene)
- The persona does not specifically prefer the fragmentary form for this anchor's voice register (none currently do; worm-tight prefers the fold)

The rule does NOT fire when:
- The sensory and loc-state cite different anchors (independent beats)
- The loc-state alone fires (no sensory co-cite); render the loc-state per its own usual position
- The anchor is a peak where the loc-state is doing rhetorical work as standalone weight (rare; flag in fork log if so)

### Lens decider

The fork applies the lens decider (rules 1–6) per `staff/stitcher/card.md § Lens decider`. The persona's lens-bias table overrides rules 1–5 where applicable. Tiebreaker per profile's `phase-1.lens-decider.tiebreaker` (default: neutral-default kinetic order).

Output draft: `active-project/draft/<slug>.phase-1.draft.md`. Log fork entries to render-log under `## Phase 1 — lens-anchored render`. **Every rendered prose block must have a corresponding fork-id line in the log.** No fork-id ⇒ FAULT-PHASE-1-CONSOLIDATED.

---

## Phase 1 — scene-window mode (default, URI-SCENE-WINDOW)

**When this fires.** Default Phase 1 mode as of 2026-05-13 (URI-SCENE-WINDOW). Active when profile carries `phase-1.mode: scene-window` (the schema default) or when `--phase-1-mode scene-window` is passed at the command line. The per-anchor mode described above remains available as opt-in fallback (`phase-1.mode: per-anchor` in profile, or `--phase-1-mode per-anchor`); use it when the scene-map facet is absent, the episode has low percussion accumulation, or fork-isolation debugging is wanted.

**Why it exists.** Three dogfoods on s01e02 (breath-pass, organic-render-p4, scene-window-dogfood — see `active-project/staff/stitcher/`) showed the per-anchor fork is structurally unable to break percussion that spans multiple bones: stilling-trios rendered as three identical "went still" verbs, exhale-pairs as two identical "I exhaled.", `I + verb` chains accumulating across paragraphs. The fork sees only its own anchor (plus the previous 1–2 rendered lines per `continuity-context`); it cannot see that this is the third log-trio in 10 bones or that the next sentence will be the third stilling. Scene-window mode lifts the fork unit from one anchor to one scene so the fork can see and break local percussion within bone-faithfulness.

**Dispatch granularity.** One Agent call per dramatist-marked scene. Typical episode: ~10–14 scene-forks vs ~150 per-anchor forks. Each scene-fork's input is wider (~3× per-anchor) but the total fork count drops ~10×; net token cost typically ~30% of per-anchor.

### Scene-boundary resolution

Scene boundaries are required at Phase 1 dispatch in this mode. Resolution order:

1. **Scene-map facet** (default, URI-SCENE-WINDOW 2026-05-13; emission re-sourced under URI-SUBSTANCE-OVERHAUL 2026-05-17). When `active-project/theater/facets/scene-map-<slug>.md` exists, parse it per `schemas/scene-map.schema.md`. The scene-map facet is emitted by `/and-write` Phase 7 directly from `chapters[].scenes[]` in showrunner memory; `/and-facets` Phase 4d validates (not derives) the facet for coverage against the bones file. If the file passed those gates, its boundaries are canonical. This is the canonical authoring path.
2. **Tensometer derivation** (REMOVED 2026-05-17 under URI-SUBSTANCE-OVERHAUL). The tensometer-fallback path is dead code under the new chain — tensometer is gone. The scene-map facet is the only canonical source; if missing, fall back per `phase-1.scene-window.fallback-on-no-scene-map` (default `per-anchor`, soft fallback recorded in render-log header) or escalate per profile.
3. **Failure mode.** If neither produces ≥3 scenes covering all bones, emit `FAULT-PHASE-1-NO-SCENE-MAP` and either escalate to user or fall back to `per-anchor` mode per `phase-1.scene-window.fallback-on-no-scene-map` (record the fallback in the render-log header).

Validate the scene-map: every bone in `proto-lines/<slug>.md` must fall inside exactly one scene's bone-range. Coverage gaps or overlaps → `FAULT-PHASE-1-SCENE-MAP-COVERAGE`.

### Fork input payload

Each scene-fork's inputs:

| Source | Content |
|---|---|
| Scene's bones | All bones with IDs inside the scene's range, in order, verbatim from `proto-lines/<slug>.md`. |
| Scene's facet citations | Every facet entry citing a bone in the scene's range — pulled from `_cite-index.md` and the per-facet files. NI, sensory, feel, memory, metaphor, loc-state, exposition, dialogue. The fork sees the lens against the whole scene, not against a single anchor. |
| **Scene-map rhythm-aware fields** (URI-SCENE-RHYTHM, 2026-05-13; URI-SUBSTANCE-OVERHAUL 2026-05-17) | The scene's `rhythm-shape`, `peak-bones`, `peak-shadow-bones`, `fusion-eligible-runs`, `protected-patterns` from `scene-map-<slug>.md`. These give the fork concrete bone-level rhythm guidance: which bones must stand alone (peaks + their shadows), where multi-bone fusion is safe (fusion-eligible-runs), what overall variance posture the scene wants (rhythm-shape). The scene-map's fields replace the pre-overhaul tensometer scalar; see § "Rhythm-shape guidance" below. |
| **Back-look context** | The rendered prose of scene N-1 (empty for the first scene of the episode). Read-only. Used for anti-repetition of openers, verb-register, cadence across the scene boundary. The fork MUST NOT re-render or modify scene N-1's prose. |
| **Forward-look context** | The bones + facets of scene N+1 (not the rendered prose — it doesn't exist yet). Empty for the last scene. Read-only. Used for transition-sentence awareness: if scene N+1 opens with a particular pattern (relay sweep, log-trio variant, peak), scene N can avoid closing on a clashing or duplicative form. |
| Persona card + active profile | Same as per-anchor. The persona's lens-bias table and Phase-7 biases apply unchanged. |
| Project anti-jargon list, hollow-prose patterns, asinine patterns, bone-faithfulness fence | Same as per-anchor. |

### Fork procedure

For each scene N in order (forks serialize across scenes — back-look requires prior scene's rendered prose):

1. **Load inputs.** Bones, facets, back-look, forward-look, persona, profile, scene-map rhythm fields.
2. **Plan the scene's prose-shape.** Identify percussion risks within the scene: clustered same-verb bones (stillings, exhales, openings), repeated subject anaphora (`I + verb` chains), protected-pattern instances (log-trio, cardinal-distribution quartet, three-note buildup) and which variant fits the scene's other instances.
3. **Render.** Produce the scene as one prose block. Choose paragraph breaks, verb-register variance, sentence-fusion within bone-faithfulness, log-trio variant selection, opener variance. The fork applies the lens decider (rules 1–6) per bone; the difference from per-anchor is that the fork *also* sees the cluster and can vary the surface choices accordingly.
4. **Per-bone discipline walk (mandatory).** After rendering, walk the scene's bone list in order and confirm every bone has a renderable trace in the prose — either as a rendered sentence, an em-dash fuse, a fused-into-prior, a CUT-BONE with rationale, or `RENDERED-ILLEGIBLE`. **This step is the catch for the scene-window failure mode** (see § Failure modes below). The fork emits a `bone-walk:` block in its render-log entry listing each bone-id and its disposition. A bone with no trace is `FAULT-BONE-FOLDED-INTO-SUMMARY` — re-render to restore the bone. **`RENDERED-ILLEGIBLE` discipline (URI-STITCH-ACCOUNTING-HONESTY):** when a bone's SVO action reaches the prose only as a label or abstraction — the bone-walk finds a trace, but the trace does not let a reader recover the action as a dramatized event — the fork records `RENDERED-ILLEGIBLE` (not a clean `-> L<N>`). This is distinct from `CUT-BONE` (which removes the bone). The stitcher cannot fix it — the bone-faithfulness fence forbids adding the missing dramatization — so `RENDERED-ILLEGIBLE` is an honest disposition that surfaces to the Phase 9 terminal gate and routes to `/and-write revise`. The pre-overhaul log had no category for "bone label survives, bone meaning does not"; this is that category.
5. **Emit fork output.** Rendered scene + render-log entry (see § Render-log entry shape below).

### Rhythm-shape guidance (URI-SCENE-RHYTHM, 2026-05-13; URI-SUBSTANCE-OVERHAUL 2026-05-17)

The scene-map facet supplies five rhythm fields per scene. The scene-window fork honors them as follows:

| Field | Fork behavior |
|---|---|
| `rhythm-shape: flat-low` | Transition scene; relay sweeps; logged-and-moved. Variance posture: aggressive fusion eligible, log-trio variant selection encouraged, opener variance important (these scenes are where percussion accumulates). |
| `rhythm-shape: flat-mid` | Pressure beats; stakes visible without rupture. Variance posture: moderate. Standalone-treat pressure bones (mid-magnitude bones — bones with non-trivial `axis_moves[].magnitude` carry weight); fusion only across genuine flat-low-zone bones. |
| `rhythm-shape: rising` | Approach scene. Variance posture: structured pacing — short standalone for ascending bones; do not fuse-and-flatten the climb. |
| `rhythm-shape: rising-to-peak` | Full arc with climax at end. Variance posture: tighten as the peak approaches; peak-bone standalone-treated; release-tail (post-peak) can fuse. |
| `rhythm-shape: peak-and-release` | Rupture in first/middle third with low tail. Variance posture: standalone for peak + peak-shadow; aggressive variance and fusion-license on the tail's flat-low run. |
| `rhythm-shape: double-peak` | Two ruptures in one scene. Variance posture: each peak standalone; the inter-peak run is rarely fusion-eligible because peak-shadow extends from both sides. |
| `rhythm-shape: resolving` / `release-only` | Post-prior-scene-peak settle. Variance posture: aggressive — these are charge-release scenes; fusion and variance both encouraged. |
| `peak-bones: @<id>, ...` | Each listed bone MUST be rendered standalone. No fusion across a peak-bone boundary. The peak's sentence stands alone in its paragraph or carries the paragraph's anchor weight. This formalizes the long-standing peak-stands-alone discipline. (Schema-field shape: flat list of flat_ids; the pre-overhaul `@<id>=<tens>` annotation is dropped — magnitude is now in showrunner memory's per-bone `axis_moves[].magnitude`, not in the scene-map.) |
| `peak-shadow-bones: @<id>, ...` | Each listed bone MUST be rendered standalone — even though it's a flat-low-zone bone, it's flanking a peak and the short-sentence rhythm IS the charge/release pacing. Do not fuse a peak-shadow bone with another flat-low-zone bone, even when the persona's lens-bias would otherwise allow it. |
| `fusion-eligible-runs: @<start>-@<end>, ...` | Each listed range is a run of 3+ consecutive flat-low-zone bones with NO peak-shadow inside. The fork has explicit license to fuse aggressively inside these ranges — multi-bone same-subject merge, em-dash continuation, comma-list parallel-structure, semicolon-fold for relay pairs. Per-anchor and earlier scene-window decisions sometimes refused these fusions on peak-adjacency grounds; the scene-map's derivation already excluded peak-shadow, so the license is safe to spend here. |
| `protected-patterns: <name> @<start>-@<end>, ...` | Each listed pattern overrides fusion-eligible-runs at its bone range. The fork picks a variant within the pattern's variant set (canonical / compressed / single-verb / truncated-tail / payload-tail) rather than collapsing it. A protected pattern that overlaps a fusion-eligible-run STAYS protected — the run's license does not extend over it. The pattern's variant choice is the fork's variance lever for that range. |

**The fusion-eligible-run is the lever that addresses bone-percussion in low-charge stretches.** Previous discussion considered changing the substance rubric (item 7 of the tuning menu) to make peak-adjacent bones fusion-eligible; that's rejected. Instead, the scene-map's mechanical derivation reads the existing per-bone `substance_delta.axis_moves[].magnitude` topology and pre-computes which flat-low-zone runs are safe to fuse without touching peak treatment. The stitcher gets the granular guidance without the rubric ripple.

### Constraints that still bind in scene-window mode

- **Bone-faithfulness fence.** Per-bone, not per-scene. Every bone's SVO meaning must be preserved (rendered, fused, or CUT-BONE with rationale logged). The wider window is for variance choice — NOT a license to invent body, dialogue, spatial, route, scene-prose, or cognitive detail outside the graph.
- **Dialogue verbatim.** Same as per-anchor. Utterance text from the dialogue facet is not rewritten; attribution is connective tissue only.
- **Protected patterns.** Log-trio, cardinal-distribution quartet, three-note buildup, countdown, threshold-cross, return-of, fauna-relay refrain remain recognizable. The fork picks the variant (canonical / compressed / single-verb / truncated-tail / payload-tail) that fits the scene's other instances rather than a global default. The fork does NOT abolish a protected pattern.
- **Q9 anti-jargon.** Same as per-anchor. The fork must not emit stitcher-coined hyphenated nominalizations (`alley-sound`, `placement-look`, `autumn-density`). Q9 hits in *bones themselves* (the bone-author put a coined compound in the SVO) are upstream faults: emit `FAULT-BONE-AUDIT-MISS @<id>` in the render-log and render the bone as-is — Phase 7 cannot REWORD a bone-content compound without violating bone-faithfulness.
- **Sensory + loc-state co-anchor fold.** Same rule as per-anchor (see § Sensory + loc-state co-anchor fold above). In scene-window mode this rule retires from special-case to natural fork judgment — but the rule is still in force as a fence.
- **Exposition fold-in mechanics.** Same as per-anchor. The exposition facet's `renders-as` directive is verbatim-honored.

### Constraints that loosen vs. per-anchor

- **Multi-bone fusion within fusion-eligible-runs** (URI-SCENE-RHYTHM). The fork has explicit license to fuse 2+ adjacent flat-low-zone bones inside any `fusion-eligible-runs` range. The scene-map's derivation already excluded peak-shadow bones, so the license is safe to spend without re-checking peak-adjacency. Per-anchor refused these on fork-window grounds, not on rule grounds; scene-window with rhythm-aware scene-map promotes the license to explicit.
- **Verb-register variance** (abstraction-aware, URI-STITCH-VARIANCE-CONCRETE). The fork may pick differentiating verbs across an `I + verb` chain or a same-action cluster (e.g. three stillings → stopped / held / held with) provided each chosen verb is idiom-fit to its bone's action (bone-faithfulness fence still per-bone) **AND each chosen verb is at least as concrete as the bone's own verb.** The variance lever may not trade a concrete physical verb for an abstract one (`lifts the eyes → turned my reading outward` is barred — it converts a physical action into an abstraction in the name of breaking repetition). If breaking repetition would require an abstract re-rendering, the fork does NOT abstract — it logs `FAULT-VARIANCE-ABSTRACTION @<id>` and renders the bone with a concrete verb, accepting the repetition. Repeated concrete physical actions across bones are an upstream bones problem (the bones should differ, or one is redundant); the fault surfaces as an `/and-write revise` signal, not a render-time abstraction license. Every variance move in the render-log `variance-moves:` block records the abstraction direction (concrete→concrete is clean; concrete→abstract is the fault).
- **Protected-pattern variant selection.** The fork reads the scene-map's `protected-patterns` field and chooses a variant within the pattern's variant set (canonical / compressed / single-verb / truncated-tail / payload-tail / load-bearing-full) per scene-position and per other-instance density across the episode. Per-anchor had a global default and rarely varied; scene-window's per-scene awareness plus the explicit pattern list makes variance selection the norm.
- **Re-paragraphing within scene.** The fork chooses paragraph breaks inside its scene. Phase 6 paragraph-grouping does not override scene-window paragraph choices.
- **Variance posture per `rhythm-shape`.** The fork takes posture cues from the scene's classified shape: aggressive variance + fusion on `flat-low` / `resolving` / `release-only`; structured pacing on `rising` / `rising-to-peak`; tightened-around-peak on `peak-and-release`. See § Rhythm-shape guidance above.

### Render-log entry shape

Per scene-fork:

```
fork-<NNN> scene-<label> bones=@<start>–@<end>  scene-window-render
   bones-consumed: @<start>, ..., @<end>
   back-look: <prior-scene-label | empty>
   forward-look: <next-scene-label | empty>
   variance-moves:
     - <move-1> (e.g. "stilling-trio differentiated: stopped/held/held-with at @12/@16/@17")
     - <move-2>
   refusals:
     - <refusal-1> (e.g. "did not fuse @14/@15 speech-pair: address-register needs own beat")
   bone-walk:
     - @<id> -> <rendered-sentence-index | FUSE-into-L<n> | CUT-BONE | RESHOW>
     - ...
   drift-risk: <none | minor | flag with bone IDs>
```

The `bone-walk:` block is the auditable trace for the per-bone discipline walk. Every bone in the scene appears exactly once.

### Failure modes specific to scene-window

| Fault | Trigger | Recovery |
|---|---|---|
| `FAULT-BONE-FOLDED-INTO-SUMMARY` | Per-bone walk finds a bone with no rendered trace, no fuse target, no CUT-BONE entry. The wider window let the fork summarize a cluster and lose a bone. | Re-render the scene with the missing bone restored. Recurrent at the same bone-id across re-runs ⇒ flag the bone as fusion-resistant. |
| `FAULT-PHASE-1-NO-SCENE-MAP` | Scene-map facet absent and no per-anchor fallback configured. (Tensometer-derivation fallback was removed 2026-05-17 under URI-SUBSTANCE-OVERHAUL.) | Fall back to `per-anchor` mode (record in render-log header) or escalate to user to author scene-map. |
| `FAULT-PHASE-1-SCENE-MAP-COVERAGE` | Scene-map resolved but a bone falls outside every scene's range or inside multiple. | Refuse the dispatch; surface the coverage gap; fix scene-map. |
| `FAULT-BONE-AUDIT-MISS @<id>` | Bone-content carries a Q9-coined hyphen-compound the stitcher cannot REWORD without violating bone-faithfulness. | Render the bone as-is; surface to upstream (`/and-write` Phase 6 bone-gate / SVO rubric pass). NOT a stitcher fix. |
| `FAULT-NI-VERB-FOLD-STRETCH @<id>` | The fork's bone-verb chosen folds an NI register-verb beyond the bone's SVO (e.g. NI says "names X as ambient signal", bone says "relays X", fork renders "named X through"). Defensible under lens-fold license; surface as soft Q-check for the auditor. | Keep render; surface in `drift-risk:` field. Auditor decides. |

### Convergence with per-anchor

Scene-window mode is not strictly-better than per-anchor in all cases. The s01e02 dogfood confirmed:

- **Convergence** on protected-pattern scenes (cardinal-quartet, three-note buildup), short transit scenes (wake/log/sleep), and hard scene-jumps (time-and-place discontinuity) — both modes produce the same prose.
- **Material gain** on multi-bone percussion clusters (stilling-trios, exhale-pairs, opener-chains), seams where transition-awareness pays (relay-register carry, name-prime), and lens-fold positioning at peaks (sensory spike at known peak, NI fold at transitional verb).
- **Material risk** on bone-folding-into-summary (caught by the per-bone walk) and NI verb-fold stretches (caught as soft Q-check by the auditor).

Use scene-window when prior runs of the same episode read metronomic at multi-bone seams. Use per-anchor when bones are already magnitude-balanced (per per-bone `axis_moves[].magnitude` distribution from showrunner memory) with low percussion accumulation (the modes converge fully on such episodes and per-anchor is cheaper per-fork to reason about).

---

## Phase 2 — Redundancy cull

Per-anchor forks with `phase-2.echo-window` context (default 1 — same-anchor only).

For each anchor with 2+ facets rendered at Phase 1:
- Apply the configured detector (default `closing-phrase-echo`)
- When echo fires: drop the facet not in `redundancy.preserve-anchor` (default: preserve narrator)
- Log `DROP-ECHO` / `DROP-IMAGE-OVERLAP` / `KEEP-OVER-ECHO`

Output draft: `active-project/draft/<slug>.phase-2.draft.md`.

---

## Phase 3 — Compression

Per-merge-candidate run. Walk the Phase 2 draft in paragraph order. Identify:
- Same-subject adjacent bones with continuous action → `MERGE-SAME-SUBJECT`
- Repeated subjects within paragraph → `SUBSTITUTE-PRONOUN`
- Runs of flat-low-zone zero-cite bones outside protected patterns → `COLLAPSE-FLAT-LOW-RUN` (formerly `COLLAPSE-TENS1-RUN` pre-overhaul)
- Exit trios → `MERGE-EXIT-TRIO` (per `compression.exit-trio-merge`)
- Time-skip-adjacent zero-cite bones → `MERGE-TIMESKIP`

Refuse merges when protected patterns would break (`NO-MERGE` with `pattern-protected` reason). Phase 6 verifies pattern intactness later; the refusal here is the first defense.

Output draft: `active-project/draft/<slug>.phase-3.draft.md`.

---

## Phase 4 — Voice transform

Per-paragraph forks. Walk paragraphs. For each paragraph:
- Apply tense shift per `voice.tense` (default past)
- Apply person shift per `voice.person` (default first)
- POV-pronoun resolution per `voice-transform.feeling-clause-pov-resolution` (default auto)
- Preserve third-party names per `voice-transform.third-party-preserve`
- Render sensory arrows per `voice-transform.sensory-arrow-rendering` (default prose-template; drop-if-covered for worm-tight)
- Apply bone-object-policy (default idiom-fit)
- Apply contractions per `voice.contractions`

Output draft: `active-project/draft/<slug>.phase-4.draft.md`. Log each transform as `TENSE-SHIFT` / `PERSON-SHIFT-POV` / `POV-PRONOUN-RESOLVE` / `PRESERVE-THIRD-PARTY` / `SENSORY-PROSE-FIT` / `SENSORY-DROP-COVERED` / `BONE-OBJECT-IDIOM-FIT` / `CONTRACTION`.

---

## Phase 5 — Local flow

Per-sliding-window forks (window size per `local-flow.window-size`, default 3). For each window:
- Within-anchor cite reorder per `local-flow.within-anchor-order` (default em-dash-fusion for 2-cite anchors)
- Forward sensory deferral (cumulative deltas only; cap per `sensory-deferral-cap`)
- Backward NI promotion (no temporal-lock words; cap per `ni-promotion-cap`)
- Un-merge to rescue swallowed facets per `un-merge-license`
- Refuse moves that violate cross-bone-temporal / cross-scene / temporal-lock
- **Speaker-paragraph rule (URI-SUBSTANCE-OVERHAUL, 2026-05-17).** Any new speaker starts a new paragraph. Each `speaks to` bone's rendered dialogue paragraph begins on its own line. Back-to-back dialogue between two speakers always paragraph-breaks between speakers. Mixed action-and-dialogue paragraphs are allowed only when the action is the same character's. The fork enforces this as a hard rendering rule — paragraph-break violations are `FAULT-LOCAL-FLOW-SPEAKER-PARAGRAPH` and must be repaired before Phase 5 closes.

Log per move: `MIGRATE-SENSORY-FORWARD` / `MIGRATE-NI-BACKWARD` / `WITHIN-ANCHOR-REORDER` / `EM-DASH-FUSE` / `UN-MERGE` / `REFUSE-MIGRATE` / `SPEAKER-PARAGRAPH-BREAK`.

Output draft: `active-project/draft/<slug>.phase-5.draft.md`.

---

## Phase 6 — Buildup preservation

Per-protected-pattern forks. For each pattern listed in `protected-patterns`:
- Detect occurrences in the current draft
- Confirm intactness (`PATTERN-OK`) or restore (`RESTORE-PATTERN`)
- If the protective facet was cut at Phase 2 or by an upstream condition, log `PATTERN-ABANDONED` — Phase 7 will read this and may elect `CUT-BONE` for the bones in the abandoned pattern
- Flag patterns not in the protected list but detected as structural: `NEW-PATTERN-CANDIDATE` (no action; for human review)

Output draft: `active-project/draft/<slug>.phase-6.draft.md`.

---

## Phase 7 — Editorial reflection

**Hard rule: per-sentence Q-line for every sentence; "0 moves" is not a legitimate outcome without the sweep.** Phase 7 MUST dispatch Agent calls. Default granularity is per-paragraph or per-scene (each subagent walks the paragraph/scene's sentences serially, emitting one Q-line per sentence). A render-log that reports "0 cuts" without per-sentence Q-evaluation entries equal to the post-Phase-6 sentence count is `FAULT-PHASE-7-NO-SWEEP` and the phase must be re-dispatched. (See card § Pet Peeves "hand-waved Phase 7".)

The 0-moves outcome IS legitimate when the sweep happens and the post-Phase-6 draft is clean — in that case the log shows N Q-lines each with `→ KEEP` and the stats record `cuts: 0, rewords: 0, reshows: 0`. The fault is missing the sweep, not the absence of moves.

Per-fork dispatch:
- Shared inputs: stitcher card, active persona, active profile (including `project.anti-jargon`, `project.hollow-prose-patterns`, `project.asinine-patterns`)
- Per-fork inputs: the paragraph/scene's sentences from the Phase 6 draft + trace block for each sentence (source bone, lens that fired at Phase 1, any pre-empted decisions)
- Per-fork output: one Q-line per sentence + applied moves + post-edit prose

For each sentence in the Phase 6 draft:
- Answer Q1–Q9 binary (yes/no) per the card § Phase 7
- Apply persona's Phase-7 biases (per-question aggressiveness)
- **Q9 enforcement is generative, not literal.** The fork MUST scan every hyphenated noun-compound in the rendered sentence and test each against the rule (does this compound have a fixed referent in common English?). The persona's Q9 example list is *orientation*, not an exhaustive catalogue; a compound that matches the pattern but is not on the list is still Q9=yes. Locative compounds with fixed common-English referents (`dock-side`, `second-floor`, `eastern-quarter`, `two-room`, `upper-room`, `side-alley`, `market-side`, `south-wall`) and established named roles or place-names (`tanner-elder`, `dock-runner`, `tanner-village`) are not Q9 hits. Sensory-tag compounds (`alley-sound`, `alley-murmur`, `autumn-density`), NI register-tokens (`placement-look`, `watch-cost`, `chin-hold`), and structural nominalizations (`route-recalibration`, `parade-cadence`) are Q9 hits whether or not they appear on the persona's literal list. Reword to the natural-English phrasing from the source facet entry, or CUT if the body register already covers.
- **Exposition-derived sentences (preamble paragraphs, scene-orient bridges, fold-in glosses): apply Q9 (anti-jargon) and Q6 (fancy punctuation) normally; treat Q1 (load-bearing) as pre-cleared by upstream audience-modeling and Q5 (hollow-prose) / Q8 (asinine) as pre-cleared by R2 + audit. Borderline Q1/Q5/Q8 on exposition-derived prose = KEEP (the audience-gap is the load-bearing claim; second-guessing it at Phase 7 invalidates the upstream gap-test). Q9 + Q6 still cut/reword normally — a Q9 jargon-hit on exposition is a fault that should have been caught at the audit stage; surface as `FAULT-EXPOSITION-AUDIT-MISS` and REWORD inline.**
- **Dialogue-derived sentences (the utterance itself, NOT the surrounding attribution clause): treat Q1 / Q5 / Q8 / Q9 / Q6 as ALL pre-cleared by the dialogue-writer fork's behavior-card-anchored authoring plus the audience-gate. Borderline = KEEP. A Q9 jargon-hit on an utterance is `FAULT-DIALOGUE-AUDIT-MISS` and surfaces for re-author at `/and-facets`; the stitcher does NOT REWORD utterances (the verbatim invariant from Phase 1 holds through Phase 7). The attribution clause (`he said`, `she answered`) IS subject to all of Q1–Q9 normally — Phase 7 may cut a redundant attribution (`Q1=no → CUT`) but cannot touch the utterance it attributed.**
- Under strict `cut-aggressiveness`: borderline = reject (except for exposition-derived and dialogue-utterance-derived per above)
- Route to move per the move-class taxonomy:
  - Q1=no → CUT (unless bones-cuttable license fires)
  - Q5 or Q8 + boundary → CUT-CLAUSE
  - Q8=yes + ≥2 graph sources (or ≥3 under worm-tight) → RESHOW
  - Q8=yes + no sources → CUT-ASININE
  - Q9=yes + clean substitution → REWORD (≤2 per sentence)
  - Q9=yes + 3+ awkward in sentence → escalate to RESHOW (per `reword-density-cap`)
  - PATTERN-ABANDONED bones (from Phase 6) + Q1=no → CUT-BONE

Each fork logs the per-sentence Q-line plus any moves. Output draft: `active-project/draft/<slug>.phase-7.draft.md`.

---

## Phase 8 — Finalize

Single fork. Walk Phase 7 draft:
- Assign stable line-IDs (sequential; gaps allowed where Phase 7 cut)
- Prepend the Phase 0.6 exposition preamble: italic-rendered paragraphs + horizontal rule before the body
- Write clean polish: `active-project/draft/<book>-<chapter>.md` (no line-IDs, no traces; preamble + body)
- **Scene-callout suppression (URI-SUBSTANCE-OVERHAUL, 2026-05-17).** HARD-strip any surviving `## Scene N` markdown headers, `[SCENE BREAK]` literals, `--- SCENE ---` separators, or similar scene-callout markers from the clean draft. Scene boundaries are conveyed by paragraph break only (an empty line between paragraphs, no extra inline marker). Any surviving scene-callout in the clean draft is a build defect — `FAULT-PHASE-8-SCENE-CALLOUT-LEAK`; the fault is repaired by stripping the marker before the file is finalized. The annotated draft MAY retain machine-readable scene markers (it's the traced/debug view); the clean draft must not.
- If `output.mode: dual`: write annotated polish: `active-project/draft/<slug>.annotated.md` with `[L<N>]` prefixes, `<trace>...</trace>` blocks per sentence, and `<trace scope="preamble">` for the bridge (the trace cites the exposition entry IDs that fed the preamble)
- For each fold-in rendered at Phase 1, the annotated trace cites `exposition:<id>` alongside the bone and lens facets — exposition is now a first-class citation in the trace alongside narrator/feel/mem/sensory/metaphor
- For each utterance rendered at Phase 1, the annotated trace cites `dialogue:<character>:<id>` alongside the speech bone — dialogue is also a first-class citation. Multi-utterance anchors emit one citation per entry. The attribution clause carries the bone citation; the utterance carries the dialogue citation.
- Finalize render-log with STATS section (word count, sentence count, paragraph count, bones rendered/merged/dropped/rendered-illegible, facets rendered/dropped/unrendered-remainder, reshow count, reword count, preamble-source: `exposition-facet` or `legacy-fallback`, exposition entries-rendered/refused-at-R2/cross-episode-register-skipped, dialogue-source: `dialogue-facet` or `legacy-silent-speech`, dialogue character-files-loaded / utterances-rendered / bare-speech-bones / unmoored-utterances / speaker-mismatches)
- **Accounting reconciliation (URI-STITCH-ACCOUNTING-HONESTY).** Emit a `RECONCILE` line per `schemas/stitch-render-log.schema.md § Accounting reconciliation`. Reconcile against the cite-index entry count: bones `rendered + merged + dropped + rendered-illegible` MUST equal authored bone count; facets `rendered + dropped + unrendered-remainder` MUST equal the cite-index facet-entry count. The pre-overhaul log tracked only what it *deleted* (every R2 tombstone has a rationale) and was blind to what it *never picked up* — facet entries that survived R2 but reached the draft as zero citations fell out of the accounting entirely (b01c02: 14 vibes + 15 state-updates entries vanished from both columns). Any non-zero `unrendered-remainder` is surfaced as a `FLAG-UNRENDERED-REMAINDER` entry naming the unaccounted facet entries — never left as a silent `dropped: 0`. A missing or unbalanced `RECONCILE` line is `FAULT-RECONCILE-MISSING` and Phase 8 must re-run the reconciliation.
- **Prune intermediates.** After the clean + annotated polish are confirmed on disk, delete the Phase 1–7 draft files for this episode: `active-project/draft/<slug>.phase-*.draft.md` and the standalone preamble at `active-project/draft/<slug>.preamble.md` (its content is already prepended to the clean polish). The render-log retains the trace of every intermediate phase; the draft files are reproducible from the render-log + facet graph and should not accumulate in the polish directory. Pass `--keep-drafts` at command-invocation to retain them (debugging only). The `active-project/draft/deprecated/` directory, if present, is out of scope for Phase 8 — pre-rerun archives are user-managed (move to `projects/<title>/archive/` at project close, or delete when no longer needed).
- Update showrunner memory: `stitched: true`

---

## Phase 9 — Cold-read terminal gate (URI-STITCH-COLD-READ — blocking)

**The highest-leverage gate in the chain.** Every other gate in the pipeline measures a *part* — per-bone axis ticks, per-facet mechanical compliance, per-facet taste, per-sentence cut-worthiness, run-health criteria. Readability, jeopardy, and "did the scene happen" are emergent properties of the *assembled* chapter, and no other stage holds the whole and asks the reader's questions. b01c02 walked the entire pipeline green — every gate passed, the orchestrator-critic returned 7/7 — while missing all three of its core events. Phase 9 is the one check that measures the whole instead of a part. One dispatch.

This phase runs after Phase 8 has written `draft/<book>-<chapter>.md`. It does NOT modify the draft. It either declares the chapter terminal (cold-read PASS) or routes it back to `/and-write revise` (cold-read FAIL).

### Step 1 — Cold read (one `general-purpose` agent, uninformed)

Dispatch ONE `general-purpose` agent with exactly this prompt (the agent must read only the draft — the test is void if it reads anything else):

> You are a first-time reader. You have been handed one chapter of a novel and nothing else — no outline, no synopsis, no notes. Read it once, at reading pace, the way someone who picked up the book would.
>
> Read ONLY this file: `active-project/draft/<book>-<chapter>.md`. Do not open bones, facets, scene chunks, render-logs, showrunner memory, or any other project file. If you read anything else, the test is void — your value here is that you are uninformed.
>
> Then answer, from the text alone:
> 1. **EVENTS** — What physically happens in this chapter? List the events in order, plainly. If a stretch of the chapter contains no event you can name, say so explicitly.
> 2. **JEOPARDY** — Is anyone at risk of anything? Who, of what, and how do you know it from the text? If nothing is at stake, answer "no jeopardy."
> 3. **CAUSALITY** — Does each scene connect to the next by cause? Point to any place where you could not tell why something happened, or why a character did what they did.
> 4. **PAYOFF** — Does the chapter end on something earned — a consequence, a decision, a turn? Did the ending land, given what the chapter actually showed you (not what it gestured at)?
> 5. **CONTINUE?** — Would you, as a reader, turn to the next chapter? Answer yes or no, one sentence why.
> 6. **ONE-LINE SUMMARY** — Summarize the chapter in one sentence, the way you would to a friend.
>
> Be blunt. Do not be generous. If you were confused, say you were confused and where. Report under 500 words.

Substitute the resolved `<book>-<chapter>` into the path. Persist the agent's answer to `staff/reviews/coldread-<chapter>-<timestamp>.md`.

### Step 2 — Diff against intent (harness)

The orchestrator reads `chapters[<slug>].goal` and the per-scene `scene_conflict` + `dramatic_shape` from showrunner memory and diffs them against the cold reader's answers. **Fail the terminal gate** when any of:
- The cold reader's recovered events (answer 1) do not include the chapter's central event (the event named by `goal` / the dominant `scene_conflict.protagonist_force`).
- Answer 5 is "no" (the reader would not continue).
- Answer 2 is "no jeopardy" on a chapter whose `dramatic_shape` is not a pure coda (`frame-coda` chapters are exempt — they may legitimately carry no jeopardy).

### Step 3 — Additive editorial pass (fires alongside, non-blocking)

Run the `/and-review staging <chapter>` reviewer routine (auditor + dramatist, graph-aware) — the one pass whose verbs ADD rather than cut: `EXPAND` / `GROUND` / `STAGE` / `NEEDS-BEAT`. Its findings are SIGNAL-class and do not block on their own, but they are recorded and surfaced. Persist to `staff/reviews/staging-<chapter>-<timestamp>.md`. (The pipeline's other editorial motions are all subtractive; this is the additive counterweight — see `/and-review staging`.)

### Step 3.5 — Prose-rationale-mute audit (URI-STITCH-PROSE-RATIONALE-MUTE; 2026-05-25; soft-block at threshold)

**The prose-layer counterpart to Phase 6's rationale-layer `opposing_force_visible` check.** Phase 6 audits *whether the bone's rationale names an opposing force, a body, a register-enactment*; this audit asks *whether the rendered prose actually stages it*. The b01c01 post-ship process audit found that 12 of 30 enumerated depth-of-quality issues classify as `WRONG-LAYER` — Phase 6 passed at rationale, Phase 9 staging review caught the prose-layer gap as advisory, the chapter shipped with the gap. This step inserts a mechanical pre-ship audit at the prose layer to close that gap.

Dispatch ONE `auditor` fork with the following inputs (READ-ONLY):
- `active-project/draft/<book>-<chapter>.md` — the rendered prose
- `active-project/draft/<book>-<chapter>.annotated.md` — sentence-ID trace
- `active-project/staff/showrunner/memory.md` — `chapters[<slug>].scenes[].bones[]` including each bone's `substance_delta.axes_held[].rationale` and any rationale-named opposing-force / body-staging / register-enactment elements
- `active-project/staff/stitcher/render-log-<book>-<chapter>.md` — bone-to-prose mapping per Phase 1 bone-walk

**Auditor task — per bone with a non-empty rationale:**
For each bone whose `axes_held[].rationale` (or scene-level `scene_conflict.opposing_force` mapped to this bone via `held` enactment) names a concrete physical element — an opposing force, a body posture, a register-enactment — locate the bone's rendered prose span (via render-log + annotated draft). Apply a mechanical lexical-scan:
- Does the prose span contain ≥1 concrete-physical token (a body part, a physical object, a surface, a sensory particular) that corresponds to the rationale-named element?
- "I exhaled" carries three held axes via discipline-rationale → does the prose stage a body / a held breath / a held discipline beyond the bare verb?
- A rationale of "rule holds capability through Wren-cost-bearer-in-frame" → does the prose physically place Wren in Taylor's perceptual frame?

A bone whose rationale names a concrete element AND whose prose span fails to stage it with ≥1 concrete-physical token is `PROSE-RATIONALE-MUTE-<bone-id>` (SIGNAL). The auditor lists each finding with `bone_id`, `rationale_element`, `rationale_text`, `prose_span`.

**Threshold (soft-block):** if `count(PROSE-RATIONALE-MUTE-*) >= 3` chapter-wide, the verdict at Step 4 is `PASS-WITH-DEPTH-PASS-REQUIRED` (mandatory depth-pass before project-stable; see Step 4 tightening). Below threshold, findings record as SIGNAL on the cold_read block but do not soft-block.

Persist findings to `chapters[<slug>].cold_read.prose_rationale_audit` per schema. Auditor returns the count + the finding list. Spend: one auditor fork, one mechanical lexical pass — comparable to a Phase 7 sweep.

This audit complements Phase 6's `OPPOSING-FORCE-MISSING` (rationale-layer HARD) without replacing it — neither check covers the other's failure mode. Phase 6 catches missing rationale; Phase 9 Step 3.5 catches present rationale + absent prose.

### Step 4 — Verdict + memory

Write `chapters[<slug>].cold_read = {read_at, verdict, recovered_summary: <answer 6>, report_path, staging_signals: <N>, staging_report_path, signal_clusters: <[...]>, prose_rationale_audit: <{...}>, stale_since: null}`.

**Cluster check (URI-STITCH-SIGNAL-CLUSTER — soft-gate; 2026-05-24; threshold tightened 2026-05-25).** Before printing the verdict, scan the staging report's findings and bin them by pattern label AND by zone (peak vs non-peak via `chapters[<slug>].cold_read.zone_density_observation` or per-bone peak-flag from staging review) AND by bone-class (axis-move vs held-vs chatter from `bones[].substance_delta`). A *cluster* fires when ANY of:

- **same-pattern ≥5** — `N >= 5 SIGNAL findings sharing the same pattern label` (e.g. `body-staging-gap`, `opposing-force-prose-mute`, `held-bone-rationale-only`). (Original 2026-05-24 trigger; retained.)
- **adjacent-in-peak-zone ≥3** — `N >= 3 SIGNAL findings sharing the same pattern label AND ≥3 of those findings are on bones inside a peak zone (3+ consecutive flat-ids inside the scene-conflict peak)`. The b01c01 cluster — 4 peak-under-staged findings at @11/@12/@13/@21 with 3 adjacent in scene-B's peak — sat below the same-pattern≥5 threshold and shipped advisory. This trigger catches that exact failure mode.
- **on-axis-move-bones ≥3** — `N >= 3 SIGNAL findings sharing the same pattern label AND all findings are on bones whose substance_delta.axis_moves is non-empty`. A pattern concentrated on axis-move bones is the difference between a stylistic note (cluster across held + chatter) and a substance-delivery failure (cluster on the bones that carry the chapter's declared deltas). Tighter threshold than same-pattern≥5 because the axis-move concentration is itself the signal.

Record `signal_clusters[]` in the cold_read block: each entry `{pattern: <label>, count: <N>, bone_ids: [<ids>], trigger: same-pattern>=5 | adjacent-in-peak-zone>=3 | on-axis-move-bones>=3}`.

The post-ship process audit on b01c01 (2026-05-25) confirmed the same-pattern≥5 threshold let the c01 cluster through (4 findings, threshold 5). The tightened triggers above use the `zone_density_observation` data the chapter already records, plus the per-bone `axis_moves` already in memory — no new dispatches.

- **PASS** — the chapter is terminal, no cluster present AND `prose_rationale_audit.verdict != SOFT-BLOCK`. Print the cold reader's one-line summary, the staging-signal count, and `next:`. If `staging_signals > 0` but no cluster, recommend `/and-write <chapter> revise` + re-cascade as an optional depth pass (non-blocking). **Depth-pass resolution stamp:** if `chapters[<slug>].depth_pass_pending == true` (set by `/and-write` Phase 7 in revise --from-signals after a prior PASS-WITH-DEPTH-PASS-REQUIRED), stamp `chapters[<slug>].depth_pass_resolved_at = <iso-timestamp>` and clear the pending flag. This confirms the depth pass delivered; downstream consumers (`/and-substance book` Phase 0, `/and-review verdict <book>`) treat the chapter as resolved.
- **PASS-WITH-DEPTH-PASS-REQUIRED (MANDATORY; 2026-05-25 promotion)** — Phase 9 cold-read returned PASS but the cluster check fired OR `prose_rationale_audit.verdict == SOFT-BLOCK` (≥3 PROSE-RATIONALE-MUTE findings). The chapter ships at the terminal gate, **but the depth pass is now mandatory before the chapter is considered project-stable** — pre-2026-05-25 framing allowed indefinite deferral, which produced the b01c01 ship-with-known-gap pattern. The depth pass MUST run before any of: `/and-postop <chapter> milestone`, `/and-review verdict <book>` against the parent book, or `/and-substance book <next-book>` (the latter HARD-aborts if any chapter in the prior book has `cold_read.verdict == PASS-WITH-DEPTH-PASS-REQUIRED` with no `chapters[<slug>].depth_pass_resolved_at` stamp). Print the cold reader's one-line summary, the cluster / prose-mute summary, and route:
  ```
  /and-stitch Phase 9 PASS-WITH-DEPTH-PASS-REQUIRED (MANDATORY) — <chapter> ships but depth pass required before book-close.
  Cluster: <N> SIGNAL findings on <pattern> across bones <ids> (trigger: <trigger>).
  Prose-rationale-mute: <K> findings on bones <ids>.
  next: /and-write <chapter> revise --from-signals   (then re-cascade /and-facets + /and-stitch)
  ```
  In a `--cascade` run, this does NOT halt the cascade (the chapter is terminal at the gate) but the depth pass appears in the cascade's exit checkpoint as `pending_depth_passes: [<chapter>, ...]`. The book-level orchestrator-critic verdict gate will refuse to PASS the book until every `pending_depth_passes[]` entry is resolved.
- **FAIL** — the chapter is NOT terminal. It is a structural failure, not a polish problem — re-decompose from the bones up. Print the cold reader's answers, the diff finding (which intent element the reader could not recover), and route:
  ```
  /and-stitch Phase 9 COLD-READ FAIL — <chapter> is not terminal.
  The cold reader could not recover: <central event | jeopardy | would-not-continue>.
  Recovered summary: <answer 6>
  Intended goal:      <chapters[].goal>
  This is a structural failure — re-decompose, do not polish.
  next: /and-write <chapter> revise   (then re-cascade /and-facets + /and-stitch)
  ```
  In a `--cascade` run, a Phase 9 FAIL halts the cascade per the standard cascade-failure surfacing (checkpoint `reason: halted-on-failure`).

---

## Phase 9.5 — Admin process-critic dispatch (URI-ADMIN-PROCESS-CRITIC, 2026-05-25; non-blocking)

Fire on any Phase 9 verdict other than clean PASS — that is, on **FAIL**, on **PASS-WITH-DEPTH-PASS-REQUIRED**, or on PASS with `signal_clusters[]` non-empty even when the verdict was clean (recurring cluster shape across chapters is itself a process signal). Non-blocking — the run exits per Phase 9's routing whether or not admin returns.

Dispatch:
- `subagent_type: admin`
- prompt carries:
  - `mode: process-critic`
  - `trigger.reason: failure` (FAIL / PASS-WITH-DEPTH-PASS-REQUIRED) or `trigger.reason: postop` if invoked after a downstream `/and-postop` convergence reports back to stitcher
  - `trigger.source_report: active-project/staff/reviews/coldread-<book><chapter>-<timestamp>.md`
  - `trigger.source_verdict: <PASS | PASS-WITH-DEPTH-PASS-REQUIRED | FAIL>`
  - `gate_path: .claude/commands/and-stitch.md#phase-9`
  - Optional: `secondary_gate_paths: [.claude/commands/and-write.md#phase-6]` when Phase 9 routes to `/and-write revise` — a FAIL at the terminal gate is evidence the upstream gate let something through

Admin's return logged in the cold-read report tail under `## admin-process-critic`. If a cluster pattern is recurring (admin will find prior occurrences in `staff/reviews/`), expect a `PROCESS-CHANGE-PROPOSED` with `change_type: modify` against the cluster-trigger thresholds — that's the URI-STITCH-SIGNAL-CLUSTER threshold being tuned via accumulated evidence. See CLAUDE.md Rules §13.

On clean PASS with no clusters: skip the dispatch.

---

## Re-stitch on feedback

If `staff/stitcher/feedback-<slug>.md` was read at Phase 0 with new line-level directives or PROMOTED pattern-level entries, the run proceeds as a re-stitch:

- Per `feedback.re-stitch-scope` (default `fork-plus-downstream`):
  - **`fork-only`**: only the originating fork for each affected anchor re-runs; downstream phases reuse their prior log entries
  - **`fork-plus-downstream`**: originating fork + every downstream phase whose log entries reference the affected anchor or line-ID re-runs
  - **`full`**: re-run the entire chain
- Unaffected lines: preserved verbatim from the prior polish file
- Line-IDs: preserved across re-stitches (a cut line's ID stays cut; a kept line's ID stays kept; new lines get fresh IDs)
- Render-log: appended-to, not rewritten. The new run's entries follow the prior run's; the auditor can read run-by-run history.

---

## Exit conditions

- **Success**: Phase 8 STATS + RECONCILE emitted; clean + annotated polish files present; render-log finalized; Phase 9 cold-read returned PASS or PASS-WITH-DEPTH-PASS-REQUIRED; `chapters[].cold_read` recorded with `signal_clusters[]`; showrunner memory updated. PASS-WITH-DEPTH-PASS-REQUIRED ships terminal but flags the chapter for `/and-write revise --from-signals` before project-stable.
- **Phase 9 cold-read FAIL**: the assembled chapter failed the terminal gate — the cold reader could not recover the chapter's central event / jeopardy, or would not continue. Not a stitch defect; a decomposition defect. Route to `/and-write <chapter> revise` and re-cascade. In a `--cascade` run, halts the cascade.
- **Phase 8 fault**: `FAULT-RECONCILE-MISSING` — the render-log's `RECONCILE` line is absent or does not balance. Re-run the Phase 8 reconciliation.
- **Phase 0 abort**: missing inputs (proto-lines, cite-index, profile). Print the missing-input path and exit.
- **Phase 0 escalation**: `FAULT-PROFILE-PERSONA-MISMATCH-PROJECT` — resolved persona is `neutral` and a project-specific persona exists. Print the mismatch and exit; user must correct profile or pass `--persona neutral` explicitly.
- **Phase 1 fault**: `FAULT-PHASE-1-CONSOLIDATED` — Phase 1 prose appears in the draft without per-fork log entries. Indicates orchestrator-inline rendering. Re-dispatch as real Agent forks.
- **Phase 7 fault**: `FAULT-PHASE-7-NO-SWEEP` — render-log reports moves count without per-sentence Q-line entries equal to post-Phase-6 sentence count. Re-dispatch the per-sentence sweep.
- **Mid-phase fault**: any per-fork dispatch returns a validation fault (e.g. RESHOW without sufficient sources, REWORD with invented compound, bone-faithfulness fence violation at Phase 1). Phase pauses; fault logged; re-dispatch the offending fork after fix, or escalate to user.
- **Phase 7 RESHOW failure cascade**: if a sentence's RESHOW output fails its own Q-check, fall through to CUT-ASININE. Log both attempts.

---

## What this command does not do

- Does not modify bones or facets. Source pipeline is upstream (`/and-write` for bones; `/and-facets` for facets). This includes the dialogue facet — utterances are verbatim through every phase; stitcher's only freedom on speech bones is the attribution clause and beat placement.
- Does not address audience flags or NEEDS_EDIT annotations. Those are the editor's concern under a future polish revival (`/and-wrap` is currently deferred; `draft/<book>-<chapter>.md` is the terminal deliverable).
- Does not commit changes to canonical profile or persona. Session-scoped overrides from feedback are applied to a working copy; promotion to canonical files is a separate step (see `staff/stitcher/tuning-guide.md § Promotion`).
- Does not parallelize across episodes. One episode per dispatch.
