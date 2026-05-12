---
description: Stitcher pipeline for one episode. Eight phases — lens-anchored render → redundancy cull → compression → voice transform → local flow → buildup preservation → editorial reflection → finalize. Output - polish/<slug>.md + polish/<slug>.annotated.md + staff/stitcher/render-log-<slug>.md. Usage - /and-stitch [episode-slug] [--profile <path>] [--persona <slug>]
---

Stitcher pipeline. One episode in, clean polish + annotated traced polish + per-fork render-log out. The Stitcher assembles a final prose draft from the proto-line bones and the facet graph; each phase forks at its natural decision granularity (per-anchor, per-paragraph, per-window, per-sentence, etc.). No inter-fork memory; the render-log is the only cross-phase artifact.

You are the orchestrator. Eight phases run in strict sequence:

```
proto-lines/<slug>.md + facets/* + _cite-index.md
        │
        ▼
   PHASE 0 — VALIDATE + LOAD
            Resolve profile (scene override → episode → project → schema default).
            Resolve persona. Read feedback-<slug>.md if present.
            Initialize render-log.
        │
        ▼
   PHASE 1 — LENS-ANCHORED RENDER (per-anchor forks)
            For each anchor: load lenses (tens, NI, mem, sensory, feel);
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
            tens=1 zero-cite collapses (respecting protected patterns).
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
            Write polish/<slug>.md (clean) + polish/<slug>.annotated.md (traced).
            Finalize render-log + STATS.
```

Phase 1 and 7 are per-line phases (per-anchor / per-sentence forks). Middle phases fork at larger but still-small decision units. The agent definition and active persona are shared across forks within a phase (system-prompt-stable, user-turn-per-fork pattern); each fork loads minimal additional context for its decision.

## Args

- `$1` — optional. Episode slug (e.g. `s01e01`). If omitted, use `active.episode` from `active-project/staff/showrunner/memory.md`.
- `--profile <path>` — optional. Override the active profile path. Default: `active-project/theater/stitch-profile.md`.
- `--persona <slug>` — optional. Override the active persona. Default: read from profile's `persona:` field; fallback `neutral`.

---

## Phase 0 — Validate + Load

1. Resolve episode slug. Verify `active-project/theater/proto-lines/<slug>.md` exists.
2. Verify `active-project/theater/facets/_cite-index.md` exists. Abort if not — stitcher requires the cite-index from `/and-facets`.
3. **Profile resolution.** Read in order:
   - Per-scene profile if any matches the active scene (`stitch-profile-<scene-label>.md`)
   - Episode default (`active-project/theater/stitch-profile.md`)
   - Project default (`active-project/stitch-profile.md`) if present
   - Schema defaults from `schemas/stitch-profile.schema.md`
   Shallow-merge top-down. Validate per the schema's fault list.
4. **Persona resolution.** Load `active-project/staff/stitcher/personas/<active>.md` (or library fallback `staff/stitcher/personas/<active>.md`). Default `neutral` if profile carries no `persona:` field. Validate persona's lens-bias and Phase-7-bias tables against the schema.
   - **Project-mismatch check.** If resolved persona is `neutral` AND `active-project/stitch-profile.md` declares a non-neutral persona OR `active-project/staff/stitcher/personas/` contains a project-scoped persona card: emit `FAULT-PROFILE-PERSONA-MISMATCH-PROJECT` and escalate to user. Do not proceed until user either (a) corrects the profile or (b) passes `--persona neutral` explicitly as an override. Silent `neutral` against a tuned project is the canonical failure mode for this pipeline.
5. **POV resolution.** Read `narrator:` from proto-lines header. If profile's `voice.pov` is unset, use the header value. Fault if both are absent.
6. **Scene boundary detection.** Parse `active-project/theater/facets/interest-narrator.md` for the sparsity-gradient section; extract scene labels and anchor ranges. Paragraph breaks fall on scene boundaries (or on explicit time-skip blanks in proto-lines).
7. **Feedback intake (if present).** Read `active-project/staff/stitcher/feedback-<slug>.md`:
   - Line-level directives (CUT/KEEP/MERGE/UNMERGE/LENS/RESHOW-REVERT/REWORD-REVERT) → write to `anchor-overrides:` block in a session-scoped profile copy (do not mutate the canonical profile)
   - Pattern-level entries (PATTERN blocks) → flag for human review; do not auto-apply unless explicitly PROMOTED
   - Free-form notes → list in render-log Phase 0 entry for human review
8. **Initialize render-log.** Create `active-project/staff/stitcher/render-log-<slug>.md` with header (profile path, persona slug, narrator, voice config, phase-7-mode, generated-date).

State machine: showrunner memory `stitched: false` → in-progress → `stitched: true` at Phase 8 completion.

---

## Phase 0.5 — Pre-flight summary (user-visible gate)

Before dispatching Phase 1, emit a one-screen summary to the user:

```
/and-stitch pre-flight for <slug>:
  persona:          <slug>           # FAULT if neutral and project has tuned persona
  voice:            <person>-person <tense>-tense, contractions <on/off>
  POV:              <actor-slug>
  anchors:          <N>              # from proto-lines
  scenes:           <M>              # from interest-narrator sparsity gradient
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
```

This summary is the gate. If anything looks wrong (persona is `neutral` when it shouldn't be; anti-jargon list is empty when the project has one; voice config is unexpected; exposition is absent for a project where it should exist), the user catches it here, not at the polish file 1,500 words later. **`exposition: ABSENT` on a project that has run `/and-facets` post-2026-05-12 is a strong signal something went wrong upstream** — re-run `/and-facets` rather than proceeding with legacy fallback.

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
Save assembled preamble to `active-project/polish/<slug>.preamble.md`. Phase 8 prepends this to the final polish.

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

## Phase 1 — Lens-anchored render

**Hard rule: forks only, no orchestrator-inline rendering.** The `/and-stitch` command body MUST dispatch Agent calls to produce Phase 1 prose. The orchestrator's job is to fan out, collect, assemble — never to render. A Phase 1 prose block in the polish file that does not correspond to a fork-id entry in the render-log is `FAULT-PHASE-1-CONSOLIDATED` and the run must be re-dispatched. (See `staff/stitcher/card.md § Pet Peeves "orchestrator-consolidated Phase 1"`.)

**Dispatch granularity.** Default is per-anchor (one Agent call per @N). If the episode's anchor count exceeds the session's practical dispatch budget, batch to per-scene (one Agent call per scene; the subagent walks anchors serially within scene with previous-2-lines continuity, applies the lens decider one anchor at a time, and returns rendered prose + per-anchor log entries). Per-scene batching is acceptable; orchestrator inline rendering is not. Document the dispatch granularity in the render-log header.

Per-fork dispatch:
- Shared inputs (cached, loaded once per Phase 1 dispatch): stitcher card, active persona, active profile
- Per-fork inputs:
  - The bone at @N (verbatim)
  - The facets at @N (verbatim — tens, narrator, memory, sensory, feel that fire)
  - **Exposition entries at @N** (verbatim from `exposition-<slug>.md` per Phase 0.6 staging): any `first-mention-*` or `scene-open-orient` entries keyed to this anchor, with their `<gloss-text>`, `scope`, and `renders-as` directive. These are graph-resident license to render the gloss content — the fork MUST fold the gloss exactly as specified by `renders-as`, NOT rewrite or invent around it.
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

The fork applies the lens decider (rules 1–6) per `staff/stitcher/card.md § Lens decider`. The persona's lens-bias table overrides rules 1–5 where applicable. Tiebreaker per profile's `phase-1.lens-decider.tiebreaker` (default: neutral-default kinetic order).

Output draft: `active-project/polish/<slug>.phase-1.draft.md`. Log fork entries to render-log under `## Phase 1 — lens-anchored render`. **Every rendered prose block must have a corresponding fork-id line in the log.** No fork-id ⇒ FAULT-PHASE-1-CONSOLIDATED.

---

## Phase 2 — Redundancy cull

Per-anchor forks with `phase-2.echo-window` context (default 1 — same-anchor only).

For each anchor with 2+ facets rendered at Phase 1:
- Apply the configured detector (default `closing-phrase-echo`)
- When echo fires: drop the facet not in `redundancy.preserve-anchor` (default: preserve narrator)
- Log `DROP-ECHO` / `DROP-IMAGE-OVERLAP` / `KEEP-OVER-ECHO`

Output draft: `polish/<slug>.phase-2.draft.md`.

---

## Phase 3 — Compression

Per-merge-candidate run. Walk the Phase 2 draft in paragraph order. Identify:
- Same-subject adjacent bones with continuous action → `MERGE-SAME-SUBJECT`
- Repeated subjects within paragraph → `SUBSTITUTE-PRONOUN`
- Runs of tens=1 zero-cite bones outside protected patterns → `COLLAPSE-TENS1-RUN`
- Exit trios → `MERGE-EXIT-TRIO` (per `compression.exit-trio-merge`)
- Time-skip-adjacent zero-cite bones → `MERGE-TIMESKIP`

Refuse merges when protected patterns would break (`NO-MERGE` with `pattern-protected` reason). Phase 6 verifies pattern intactness later; the refusal here is the first defense.

Output draft: `polish/<slug>.phase-3.draft.md`.

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

Output draft: `polish/<slug>.phase-4.draft.md`. Log each transform as `TENSE-SHIFT` / `PERSON-SHIFT-POV` / `POV-PRONOUN-RESOLVE` / `PRESERVE-THIRD-PARTY` / `SENSORY-PROSE-FIT` / `SENSORY-DROP-COVERED` / `BONE-OBJECT-IDIOM-FIT` / `CONTRACTION`.

---

## Phase 5 — Local flow

Per-sliding-window forks (window size per `local-flow.window-size`, default 3). For each window:
- Within-anchor cite reorder per `local-flow.within-anchor-order` (default em-dash-fusion for 2-cite anchors)
- Forward sensory deferral (cumulative deltas only; cap per `sensory-deferral-cap`)
- Backward NI promotion (no temporal-lock words; cap per `ni-promotion-cap`)
- Un-merge to rescue swallowed facets per `un-merge-license`
- Refuse moves that violate cross-bone-temporal / cross-scene / temporal-lock

Log per move: `MIGRATE-SENSORY-FORWARD` / `MIGRATE-NI-BACKWARD` / `WITHIN-ANCHOR-REORDER` / `EM-DASH-FUSE` / `UN-MERGE` / `REFUSE-MIGRATE`.

Output draft: `polish/<slug>.phase-5.draft.md`.

---

## Phase 6 — Buildup preservation

Per-protected-pattern forks. For each pattern listed in `protected-patterns`:
- Detect occurrences in the current draft
- Confirm intactness (`PATTERN-OK`) or restore (`RESTORE-PATTERN`)
- If the protective facet was cut at Phase 2 or by an upstream condition, log `PATTERN-ABANDONED` — Phase 7 will read this and may elect `CUT-BONE` for the bones in the abandoned pattern
- Flag patterns not in the protected list but detected as structural: `NEW-PATTERN-CANDIDATE` (no action; for human review)

Output draft: `polish/<slug>.phase-6.draft.md`.

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
- **Exposition-derived sentences (preamble paragraphs, scene-orient bridges, fold-in glosses): apply Q9 (anti-jargon) and Q6 (fancy punctuation) normally; treat Q1 (load-bearing) as pre-cleared by upstream audience-modeling and Q5 (hollow-prose) / Q8 (asinine) as pre-cleared by R2 + audit. Borderline Q1/Q5/Q8 on exposition-derived prose = KEEP (the audience-gap is the load-bearing claim; second-guessing it at Phase 7 invalidates the upstream gap-test). Q9 + Q6 still cut/reword normally — a Q9 jargon-hit on exposition is a fault that should have been caught at the audit stage; surface as `FAULT-EXPOSITION-AUDIT-MISS` and REWORD inline.**
- Under strict `cut-aggressiveness`: borderline = reject (except for exposition-derived per above)
- Route to move per the move-class taxonomy:
  - Q1=no → CUT (unless bones-cuttable license fires)
  - Q5 or Q8 + boundary → CUT-CLAUSE
  - Q8=yes + ≥2 graph sources (or ≥3 under worm-tight) → RESHOW
  - Q8=yes + no sources → CUT-ASININE
  - Q9=yes + clean substitution → REWORD (≤2 per sentence)
  - Q9=yes + 3+ awkward in sentence → escalate to RESHOW (per `reword-density-cap`)
  - PATTERN-ABANDONED bones (from Phase 6) + Q1=no → CUT-BONE

Each fork logs the per-sentence Q-line plus any moves. Output draft: `polish/<slug>.phase-7.draft.md`.

---

## Phase 8 — Finalize

Single fork. Walk Phase 7 draft:
- Assign stable line-IDs (sequential; gaps allowed where Phase 7 cut)
- Prepend the Phase 0.6 exposition preamble: italic-rendered paragraphs + horizontal rule before the body
- Write clean polish: `active-project/polish/<slug>.md` (no line-IDs, no traces; preamble + body)
- If `output.mode: dual`: write annotated polish: `active-project/polish/<slug>.annotated.md` with `[L<N>]` prefixes, `<trace>...</trace>` blocks per sentence, and `<trace scope="preamble">` for the bridge (the trace cites the exposition entry IDs that fed the preamble)
- For each fold-in rendered at Phase 1, the annotated trace cites `exposition:<id>` alongside the bone and lens facets — exposition is now a first-class citation in the trace alongside narrator/feel/mem/sensory/metaphor
- Finalize render-log with STATS section (word count, sentence count, paragraph count, bones rendered/merged/dropped, facets rendered/dropped, reshow count, reword count, preamble-source: `exposition-facet` or `legacy-fallback`, exposition entries-rendered/refused-at-R2/cross-episode-register-skipped)
- Update showrunner memory: `stitched: true`

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

- **Success**: Phase 8 STATS emitted; clean + annotated polish files present; render-log finalized; showrunner memory updated.
- **Phase 0 abort**: missing inputs (proto-lines, cite-index, profile). Print the missing-input path and exit.
- **Phase 0 escalation**: `FAULT-PROFILE-PERSONA-MISMATCH-PROJECT` — resolved persona is `neutral` and a project-specific persona exists. Print the mismatch and exit; user must correct profile or pass `--persona neutral` explicitly.
- **Phase 1 fault**: `FAULT-PHASE-1-CONSOLIDATED` — Phase 1 prose appears in the draft without per-fork log entries. Indicates orchestrator-inline rendering. Re-dispatch as real Agent forks.
- **Phase 7 fault**: `FAULT-PHASE-7-NO-SWEEP` — render-log reports moves count without per-sentence Q-line entries equal to post-Phase-6 sentence count. Re-dispatch the per-sentence sweep.
- **Mid-phase fault**: any per-fork dispatch returns a validation fault (e.g. RESHOW without sufficient sources, REWORD with invented compound, bone-faithfulness fence violation at Phase 1). Phase pauses; fault logged; re-dispatch the offending fork after fix, or escalate to user.
- **Phase 7 RESHOW failure cascade**: if a sentence's RESHOW output fails its own Q-check, fall through to CUT-ASININE. Log both attempts.

---

## What this command does not do

- Does not modify proto-lines or facets. Source pipeline is upstream (`/and-protolines-v2`, `/and-facets`).
- Does not address audience flags or NEEDS_EDIT annotations. Those are the editor's job in `/and-wrap`.
- Does not commit changes to canonical profile or persona. Session-scoped overrides from feedback are applied to a working copy; promotion to canonical files is a separate step (see `staff/stitcher/tuning-guide.md § Promotion`).
- Does not parallelize across episodes. One episode per dispatch.
