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
- `--max-arms <N>` — optional. Override the multi-arm dispatch cap (default 4). Caps the voice-exemplar candidate-set size at Phase 0 step 4a. Set `--max-arms 1` to force single-arm dispatch regardless of resolved candidates (debugging / control-baseline). See Phase 0 § 4a (URI-STITCH-MULTI-ARM, 2026-05-26).
- `--include-pov-mismatch` — optional. Disable the POV-pre-filter at Phase 0 step 4a. Candidates whose exemplar prose is in a different person (1st / 3rd) than the bones-header `narrator:` field will be promoted to the dispatch set anyway. Debugging only — closes the Criston-Cole third-person-slip failure mode by default; this flag re-opens it. See Phase 0 § 4a (URI-EXEMPLAR-POV-FENCE, 2026-05-26).
- `--cherry-pick <off|paragraph>` — optional. **Default `off` (URI-STITCH-CHERRY-PICK-DEFAULT-OFF, 2026-05-27; remediation of the prior `paragraph` default — see § Audit note below).** When `paragraph`, Phase 1.5 composes a paragraph-level cherry-pick aggregate across the N arms after per-scene ranking — Step 2 composes, Step 3 scores the assembled cherry-pick, and the result becomes the canonical scene draft consumed by Phases 2-8. When `off` (default), Phase 1.5 stops at per-scene pure-winner selection. N=1 collapses cherry-pick to a no-op (pure-winner = single arm). See Phase 1.5 § Per-scene cherry-pick composition + scoring.

  **Audit note (URI-STITCH-CHERRY-PICK-DEFAULT-OFF, 2026-05-27 remediation):** the prior `paragraph` default (URI-STITCH-CHERRY-PICK-DEFAULT-ON, 2026-05-27) was codified ~12 minutes after the b01-c02 cherry-pick experiment (commit `2d525d2`) whose own conclusion was the opposite: *"cherry-pick fires same walkout-severity peeves as pure-winner because cost-legibility lives in bones SVO authoring, not stitch paragraph composition. Per-paragraph craft optimization is not predictive of continue-rate."* The "paragraph-level lifts" cited as evidence (the "no signature against it" / "feed thinned" / unnamed-woman-grounding lines on scene-B) were per-paragraph craft improvements that the experiment's own pet-peeve audit identified as failing to address the walkout-severity peeves (protagonist-arc-cost-not-legible, setting-dressing-as-meaning, symbolic-relationship). The b01-c04 first-chapter validation under cherry-pick-default-on produced 3/3 ceiling-collapse + multi-judge ranking confirming single-arm > cherry-pick — consistent with the c02 experiment's actual finding. Cherry-pick is preserved as an on-demand opt-in (`--cherry-pick=paragraph`) for chapters where craft-layer tuning is wanted; the experiment's actually-recommended lever is option E (cold-read FAIL → /and-write revise --from-signals feedback loop; see Phase 9 Step 4 routing).

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
4a. **Voice-exemplar resolution (PROP-0003-A / DEC-0015; URI-STITCH-MULTI-ARM, 2026-05-26).** Resolve the voice-exemplar candidate set. The resolution is now a SET, not a single path — single-candidate (the historical behavior) is the N=1 case of the multi-arm path.

    **Candidate-set resolution order:**
    - **Per-chapter overrides** (highest priority):
      - Primary: `active-project/theater/voice-exemplar-<book>-<chapter>.md` (if present).
      - Alternates: `active-project/theater/voice-exemplar-<book>-<chapter>.alt-*.md` siblings — every file matching the glob is a candidate. Numeric or descriptive suffixes both accepted (`.alt-1.md`, `.alt-relational.md`).
      - If primary + alts exist: multi-arm candidate set = `[primary, alt-1, alt-2, ...]` in glob order.
      - If only primary exists: single-arm; candidate set = `[primary]`.
    - **Series-level default**: `active-project/voice-exemplar.md`. If no per-chapter override exists and series-level is present: candidate set = `[series-default]`.
    - **Else**: no voice exemplar — Phase 1 forks run un-primed (baseline behavior). Candidate set = `[]`. Record `voice-exemplar: ABSENT` in render-log header.

    **POV pre-filter (URI-EXEMPLAR-POV-FENCE, 2026-05-26 — closes the Criston-Cole third-person-slip failure mode):** before promoting any candidate to the dispatch set, verify the candidate's exemplar prose is in the same person (1st / 3rd) as the bones-file `narrator:` field implies. If a candidate is third-person and the bones-header is first-person (or vice versa): exclude the candidate from the dispatch set, record `EXCLUDED-POV-MISMATCH <path>` in the render-log Phase 0 entry, and do NOT silently transform. Manual override available via `--include-pov-mismatch` flag (debugging only; never default).

    **Cap (cost discipline):** the dispatch set is capped at 4 candidates per chapter. If more candidates resolve, the first 4 in glob order win; remainder logged as `EXCLUDED-OVER-CAP <path>`. Cap is a soft default; override via `--max-arms=<N>`.

    For each candidate in the dispatch set: validate the file is non-empty and contains a prose passage. Read the passage into the Phase 1 fork dispatch payload for each arm; do NOT abstract or describe it back to yourself — it is held as a concrete artifact for pattern-matching.

    Record `voice-exemplar-candidates: [<paths>]` in render-log header. When `|candidates| == 1` the behavior is the historical single-arm path; when `|candidates| >= 2` Phase 1 fans out per-arm and Phase 1.5 runs the per-scene tournament (see Phase 1 § multi-arm dispatch and Phase 1.5 § per-scene tournament).

    **Surface-convention fence (injected at Phase 1 fork dispatch — applies to EVERY arm):**
    > The voice exemplar demonstrates prose register, sentence shape, and cadence. Do NOT import the exemplar's specific content (characters, place-names, events, surface conventions like italics formatting, scene-break symbols, or address forms) into the rendered prose. Only the cadence, sentence-shape, register, and noticing-patterns transfer.
    This fence closed the v17 leak in the renderer experiment and is non-negotiable wherever the exemplar is consumed.

    **Counterweight discipline (URI-STITCH-COUNTERWEIGHT, 2026-05-26):** when the candidate set has 2+ arms, candidate authoring guidance is that arms should COUNTERWEIGHT the bones' default cadence-shape, not match it. A prime whose sentence-shape matches the bones' default cadence amplifies the bones' load (compound-noun saturation, parallel-clause metronome, etc.) and ranks below baseline. The taste-aligned ablation on b01-c02 scene-A (`active-project/staff/ablation/voice-exemplar-experiment-taste-aligned-2026-05-26/cold-read-report.md`) demonstrated: V2 porter-active (matched bones' clipped cadence) ranked LAST, below V0 baseline; V1 market-observational (counterweighted with variance + embodied digression) ranked FIRST. Candidate authoring SHOULD pick cadence-shapes that invert the bones' default. Phase 1.5 tournament will surface mis-counterweighted arms as low ranks regardless.

    **REMOVED (URI-STITCH-MULTI-ARM-DEFAULT-OFF, 2026-05-27 remediation):** an auto-alt-authoring step (URI-STITCH-MULTI-ARM-DEFAULT-ON) was briefly added at step 4b to make multi-arm the practical default by auto-generating a counterweight alt-exemplar when no per-chapter alt was on disk. The rewire was built on top of the (also misrepresented) URI-STITCH-CHERRY-PICK-DEFAULT-ON decision — see § Audit note in the `--cherry-pick` flag description above. Multi-judge verification on b01-c04 confirmed the multi-arm path did not outperform the single-arm path; the rewire is reverted. Multi-arm remains available as opt-in by authoring `active-project/theater/voice-exemplar-<book>-<chapter>.md` (primary) + one or more `.alt-*.md` siblings; the candidate-set resolution in step 4a above is the canonical path.

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
  voice-exemplar:   <N candidates | single (path) | ABSENT>   # PROP-0003-A; URI-STITCH-MULTI-ARM 2026-05-26
                    if N >= 2: list each candidate path + word-count + content-match + cadence-axis;
                               phase-1 fanout becomes N × scene-count = <T> Phase-1 dispatches;
                               Phase 1.5 per-scene tournament dispatches: <scene-count>
                    if single:  <word-count> words; content-match per exemplar frontmatter
                    POV-pre-filter: <P excluded | clean> — excluded candidates listed at render-log
                    cap: 4 candidates by default (--max-arms to override)
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

## Phase 1 — multi-arm dispatch (URI-STITCH-MULTI-ARM, 2026-05-26)

**When this fires.** When Phase 0 step 4a candidate-set resolution produced a dispatch set of size N ≥ 2 (a user-authored `voice-exemplar-<book>-<chapter>.md` primary plus one or more `.alt-*.md` siblings), Phase 1 fans out N × scene-count scene-window dispatches instead of scene-count. Per-anchor mode also supports multi-arm: dispatches become N × anchor-count. N = 1 collapses to the historical single-arm behavior (the default — see URI-STITCH-MULTI-ARM-DEFAULT-OFF remediation note at Phase 0 step 4a). Multi-arm is on-demand opt-in by user-authored alts on disk; it is not the default.

**Why it exists.** The 2026-05-26 taste-aligned voice-exemplar ablation (`active-project/staff/ablation/voice-exemplar-experiment-taste-aligned-2026-05-26/cold-read-report.md`) demonstrated that exemplar register-fit at authoring time does NOT predict reading-experience outcome on the rendered chapter. The same chapter's bones produce dramatically different prose under different exemplar primes, and per-chapter-per-scene the winner can differ. Single-arm dispatch locks in one prime per chapter without evidence; multi-arm dispatch + per-scene tournament (Phase 1.5) picks the winner per-scene from actual rendered outputs.

**Dispatch granularity.** For each arm A in the candidate set, dispatch the same scene-window forks the single-arm path would dispatch — but with arm A's exemplar in the fork's payload. Arms within a scene run in parallel (independent; no inter-arm context); scenes within an arm serialize (back-look requires prior scene's prose, same as single-arm). Practical pattern: dispatch arm-1's scene-A and arm-2's scene-A in parallel; once both return, dispatch arm-1's scene-B (with arm-1's scene-A as back-look) and arm-2's scene-B (with arm-2's scene-A as back-look) in parallel; etc.

**Per-arm output paths.** Each arm's per-scene draft writes to `active-project/draft/<slug>.scene-<L>.arm-<N>.draft.md` where `<L>` is the scene label (A, B, C, ...) and `<N>` is the arm index in the candidate set (1, 2, ...). The single-arm path (N=1) preserves the historical `<slug>.scene-<L>.draft.md` naming.

**Per-arm render-log entries.** Every Phase 1 fork emits its existing render-log entry shape (`fork-<NNN> scene-<L> bones=@<start>–@<end>`) plus an arm tag: `arm: <N> (candidate: <path>)`. The render-log preserves all N × scene-count entries — the per-scene tournament selects but does not delete.

**Cost.** N × scene-count Phase 1 dispatches replaces scene-count. For c02 (3 scenes, double-stitch N=2): 6 scene-window dispatches at Phase 1, plus 3 tournament-judge dispatches at Phase 1.5 — total 9 vs the single-arm 3. ~3× Phase 1 cost; Phases 2-9 unaffected (operate on the assembled post-tournament draft). Net pipeline overhead ~20% for double-stitch, ~30% for triple-stitch. Within the user-confirmed "exemplars and renderer are light, it is affordable" envelope.

**Failure modes.**

| Fault | Trigger | Recovery |
|---|---|---|
| `FAULT-MULTI-ARM-COVERAGE-MISMATCH` | One arm's scene-fork returned a draft missing bones that another arm rendered. Indicates a fork-level bug, not a tournament-eligible signal. | Re-dispatch the failing arm's scene before Phase 1.5. |
| `FAULT-EXEMPLAR-CONTENT-LEAK <arm>` | Per-arm output contains text the candidate exemplar's frontmatter declares forbidden content (e.g. exemplar-character names, exemplar-place-names). Surface-convention fence violation. | The arm is disqualified from Phase 1.5 tournament; flag for exemplar re-authoring. Surfaces in render-log. |
| `FAULT-MULTI-ARM-DEGENERATE` | All N arms returned near-identical prose (e.g. all exemplars had similar cadence-shape; the candidate set had no meaningful spread). Tournament will pick arbitrarily. | Non-blocking; tournament proceeds. Surface to render-log as `MULTI-ARM-DEGENERATE` for future candidate-set curation. |

---

## Phase 1.5 — Per-scene tournament selection (URI-STITCH-TOURNAMENT, 2026-05-26)

**When this fires.** Fires when Phase 1 ran in multi-arm mode (candidate set N ≥ 2 from user-authored on-disk alts at step 4a). Skipped on single-arm runs (N=1; the default). One tournament dispatch per scene.

**Inputs per scene-tournament dispatch:**
- All N candidate variants for this scene (`<slug>.scene-<L>.arm-<N>.draft.md` for N in candidate set)
- The scene's bones (verbatim — judge needs to verify bone-faithfulness)
- The scene-map row for this scene (rhythm-shape, peak-bones, peak-shadow-bones, fusion-eligible-runs, protected-patterns — these inform whether each variant honored the rhythm chart)
- The taste-aligned tournament rubric at `staff/admin/exemplar-tournament-judge-prompts/renderer-voice.md` (PET PEEVES + REWARDS — see § Rubric below)
- The candidate exemplars themselves (to recognize content-fence leaks)

**Judge behavior:**
- Read all N variants for the scene blind (position-labels P1-PN assigned BEFORE the judge reads filenames; mapping revealed only after ranking is finalized).
- Rank 1 through N against the taste-aligned rubric (PET PEEVES as active negatives + REWARDS as active positives).
- Surface the per-criterion best/worst for the auditor's trace.
- Declare a per-scene winner (rank 1).

**Per-scene winner promotion:**
- The winning variant's prose is copied to `active-project/draft/<slug>.scene-<L>.draft.md` (the canonical post-Phase-1 scene draft).
- Render-log Phase 1.5 entry records: `scene-<L> winner: arm-<N> (candidate: <path>); ranking: arm-<N>, arm-<M>, ...; per-criterion verdict path: staff/reviews/tournament-<slug>-scene-<L>-<timestamp>.md`.
- Losing arms' per-scene drafts are retained on disk under `<slug>.scene-<L>.arm-<N>.draft.md` until Phase 8 prunes intermediates (same prune-policy as other phase-N drafts).

**Per-scene cherry-pick composition + scoring (URI-STITCH-CHERRY-PICK, 2026-05-26; default-off under URI-STITCH-CHERRY-PICK-DEFAULT-OFF, 2026-05-27 remediation — see Audit note at the `--cherry-pick` flag):**

The cherry-pick path is **opt-in** (pass `--cherry-pick=paragraph` to enable). When enabled on a multi-arm run (N ≥ 2), it runs as two additional sub-steps after the per-scene blind ranking (Step 1) completes. Cherry-pick collapses to a no-op when N=1 (pure-winner = single arm) or when `--cherry-pick=off` (the default).

**Step 2 — Per-scene cherry-pick composition (one judge fork per scene).**

Dispatch one `general-purpose` agent per scene with the judge prompt at `staff/admin/exemplar-tournament-judge-prompts/cherry-pick-composer.md`. Inputs:
- All N candidate scene drafts (`<slug>.scene-<L>.arm-<N>.draft.md`)
- The Step 1 per-scene tournament verdict (per-criterion table, counterweight verdict, rank order)
- The scene's bones (verbatim; bone-faithfulness fence)
- The scene-map row (rhythm-shape, peak-bones, fusion-eligible-runs, protected-patterns)

The composer's task: paragraph-by-paragraph, identify the arm whose paragraph best satisfies the taste-aligned rubric for that paragraph's bone-range. Compose the scene draft from the per-paragraph winners. Hard fences:
- **Bone-faithfulness fence.** Each picked paragraph MUST render the SAME bone-range as the paragraph it replaces in the per-scene tournament winner's structure. If a paragraph in arm-A renders bones @17-@19 and the corresponding paragraph in arm-B renders bones @17-@20, those are NOT substitutable — keep the winner's version. Violations emit `FAULT-CHERRY-PICK-BONE-MISMATCH`.
- **Tonal-seam awareness.** When picking from a non-winner arm, the composer flags `tonal-seam-risk: <none | low | flag>` on the substitution. `flag` substitutions surface in render-log and Phase 9 cold-read attention.
- **No invention.** The composer composes from the N rendered candidate paragraphs only; no rewriting, no blending.

The composer writes the aggregate to `active-project/draft/<slug>.scene-<L>.draft.md` (canonical scene draft consumed by Phases 2-8). The per-scene pure-winner is retained as `<slug>.scene-<L>.winner.draft.md` for the tournament-tuning ledger (Phase 9.6).

Render-log Phase 1.5 entry adds per scene:
```
cherry-picked: <K> paragraphs from non-winner arms (arm-<X>:<P>, arm-<Y>:<Q>, ...);
tonal-seam-risk: <none | low | flag>; pure-winner retained at <path>;
ceiling-collapse: <true|false>   # true when 0 substitutions were made (winner was already paragraph-level optimal)
```

**Step 3 — Per-scene cherry-pick scoring (one scorer fork per scene).**

Dispatch one `general-purpose` agent per scene with the judge prompt at `staff/admin/exemplar-tournament-judge-prompts/cherry-pick-scorer.md`. Input: the assembled cherry-pick scene draft (post-Step-2). Output: a structured scorecard per `schemas/tournament-scorecard.schema.md`:
- Per-PET-PEEVE: count of fires + severity (soft/strong/walkout/blocker) + anchor sentences
- Per-REWARD: count of hits + anchor sentences
- Scene-level numeric score (rewards-sum − peeves-weighted-sum)
- Notes on tonal-seam landings (does the cross-arm composition read as one voice or two?)

The scorecard is the tuning signal — accumulating these per scene per chapter allows admin process-critic to identify rubric mis-calibrations (peeves that fire on every arm = rubric too strict; rewards that no arm hits = rubric measuring the wrong thing; cherry-pick lift consistently coming from one rubric dimension = the rubric is finding real per-arm strengths).

Per-scene scorecards write to `active-project/staff/reviews/scorecard-<slug>-scene-<L>-<timestamp>.md`. Chapter-level aggregate accumulates at `active-project/staff/showrunner/tournament-scorecards.md` (append-only).

**Risks (DEFAULT-ON acknowledged):**
- **Tonal inconsistency.** Different exemplars produce different voices; mixing within a scene risks reader perceiving the seam. Mitigated by `tonal-seam-risk` flagging at composition + scorer's voice-consistency check.
- **Bone-faithfulness drift.** Mitigated by the same-bone-range fence above.
- **Ceiling collapse with no harm.** When the pure-winner already swept the per-criterion rubric (as on b01-c02 scene-A: 15/16 to arm-1), the cherry-pick composer makes 0 substitutions and emits `ceiling-collapse: true`. This is the no-harm path — render-log records the ceiling-collapse for tuning evidence (recurring ceiling-collapse on a scene class signals the rubric isn't differentiating arms enough).

Pass `--cherry-pick=off` to disable (debugging / control-baseline). Pass `--cherry-pick=paragraph` (the default) explicitly when documenting reproducibility.

**Rubric.** The taste-aligned tournament rubric is loaded from `staff/admin/exemplar-tournament-judge-prompts/renderer-voice.md` (when present) OR inlined per the validated rubric below. The rubric is calibrated to the user's explicit pet peeves and rewards. It is NOT the cold-reader prompt of Phase 9 — that gate measures different criteria (event-recovery + continue-rate). Phase 1.5's judge measures cadence-and-prose-quality only.

PET PEEVES (active negatives — variants exhibiting these get marked down):
1. Theme-as-statement (announcement of moral significance the events should earn)
2. Heavy-handed metaphor that announces itself
3. Symbolic relationships (a person or object exists to mean rather than to be)
4. Setting-dressing-as-meaning (atmosphere asks to be read as significance)
5. Compound-noun saturation (hyphenated nominalizations recycling 3-4 roots; aggregate density, not raw count)
6. Metronome tic-regularity ("I did X. I did Y. I did not Z." / "X was X. Y was Y." / "which was A, which was B")
7. Repetition-as-cadence when verbs run out ("closed the X entry, closed the Y entry, closed the Z entry" fake closure)
8. Gestured-at recognition (a moral or perceptual shift named rather than dramatized)

REWARDS (active positives — variants exhibiting these get marked up):
1. Person in the voice (a particular mind behind the sentences; not a system humming)
2. Embodied (the body in the sentences; hands knowing the work; weight on a foot; body deciding ahead of mind)
3. Sensory-grounded (concrete physical anchors; not vague atmosphere)
4. Variance in sentence length (no metronome rhythm; long sentences earn length, short punctuate)
5. Quiet lines carrying scenes (a small declarative doing paragraph-of-statement work)
6. Setup→payoff recognizable but not announced (setup pays off in action, not narration about the setup)
7. Restraint AND confidence at once (chooses what to say with discipline + without hedging)
8. Bone-faithfulness (prose stays inside scene's actual events; no invented body / dialogue / cognitive / spatial detail)

**The counterweight question (URI-STITCH-COUNTERWEIGHT, 2026-05-26 — load-bearing finding from the taste-aligned ablation):** before scoring the rubric per-variant, the judge MUST name the bones' default cadence-shape in one phrase (e.g. "compound-noun-heavy parallel-clause infrastructure", "short clipped action chain", "long observational sweep") and then judge each variant on whether it INVERTS that shape (counterweight; rewards) or AMPLIFIES it (resonance; penalties). The per-criterion rubric stands, but the counterweight verdict is the top-line discriminator. The b01-c02 taste-aligned ablation showed: a prime that matches the chapter's energy is often the WRONG prime — V2 porter-active's clipped action-rhythm matched c02's bones and ranked LAST, below baseline. V1 market-observational's variance-with-embodiment counterweighted the bones and ranked FIRST. The judge prompt explicitly carries this discrimination as a first-pass classifier.

**Output:**
- Per-scene tournament verdict written to `active-project/staff/reviews/tournament-<slug>-scene-<L>-<timestamp>.md` (ranking table, per-criterion breakdown, counterweight verdict, position-to-arm un-blinding).
- Winning variant copied to `active-project/draft/<slug>.scene-<L>.draft.md`.
- Render-log Phase 1.5 entry per scene.

**Failure modes.**

| Fault | Trigger | Recovery |
|---|---|---|
| `FAULT-TOURNAMENT-NO-WINNER` | Judge returned a tie at rank 1 (technically impossible per the "no ties" rubric directive but possible on judge non-compliance). | Re-dispatch the judge with explicit "break the tie on counterweight; if still tied, break on Embodied (REWARD #2)". |
| `FAULT-TOURNAMENT-ALL-EXCLUDED` | Every arm hit `FAULT-EXEMPLAR-CONTENT-LEAK` at Phase 1. No eligible variants. | Tournament cannot proceed; fall back to the un-primed re-render of the scene (single-arm with no exemplar) and surface the candidate-set failure to the user. |
| `FAULT-CHERRY-PICK-BONE-MISMATCH` | Cherry-pick judge proposed a paragraph that renders different bones than the paragraph it would replace. | Reject the cherry-pick; keep the pure-winner paragraph; log the bone-range mismatch. |

**Resumability.** A multi-arm Phase 1 + Phase 1.5 can resume per the standard `/and-stitch` re-run protocol: completed scene-tournaments remain valid; in-flight tournaments re-dispatch from the per-arm scene drafts (which were written before Phase 1.5 ran). The render-log records the resumption point.

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

## Phase 8.5 — Assembled-prose coherence review (URI-STITCH-COHERENCE; PROP-0019; advisory + routing-bearing)

**Why this exists.** Every reviewer in the pipeline prior to this phase has seen one of: (a) chunks + bones + facets (audience trio at `/and-write` Phase 6 + `/and-facets` Phase 5b; auditor; dramatist; `/and-review bones`), or (b) per-scene fork-window prose (stitcher Phase 1 forks; Phase 7 per-sentence sweep). **None read the assembled preamble + body + facet-fold cohesion end-to-end.** The Phase 9 cold-reader is the first and only fork that reads the assembled draft, and at the most expensive recovery point. Phase 8.5 inserts a substance-aware read of the same artifact one phase earlier — closes the FAIL-mechanism gap that produced b01-c05 FAIL #2 (the "below the register I would have called human" stitch-layer rendering invention at @14 that no upstream fork saw in assembled form). See `staff/admin/process-proposals.md § PROP-0019`.

Fires after Phase 8 has written `draft/<book>-<chapter>.md` and before Phase 9 Step 1. Skipped if `chapters[<slug>].chapter_class: frame-coda` (Phase 9 cold-read terminal gate is symmetric exempt).

**Dispatch.** ONE general-purpose agent. Inputs (READ-ONLY):
- `active-project/draft/<book>-<chapter>.md` (assembled prose, preamble + body)
- `active-project/theater/bones/<book>-<chapter>.md`
- All facet files at `active-project/theater/facets/*-<book>-<chapter>.md`
- `chapters[<slug>].{goal, dramatic_shape, scenes[].chunk, scenes[].substance_delta, scenes[].scene_conflict}`
- `chapters[<slug>].chunk_cold_read` if present (PROP-0019 upstream gate's verdict) — INCLUDING the `voice_risk.voice_risk_carry` block when `verdict == PASS-CHUNK-VOICE-RISK` (arms Check 3 central-event-muffle; PROP-0019-A)
- Exposition entries with their `renders-as` directives (read from `exposition-<slug>.md`)
- `active-project/staff/stitcher/render-log-<book>-<chapter>.md` Phase 1 bone-walk (to trace bone→prose-span)

**Mandate — three checks, in order.**

### Check 1 — Weave

For each scene-window of the assembled prose, do the facet-folds tie together as one fabric? Or are exposition + bone-rendering + sensory + NI + memory arriving as discrete add-ons? A weave-pass scene reads as one perceptual flow; a weave-gap scene reads as bones + facet-folds visibly attached at seams. Flag `WEAVE-GAP @<bone>` with `seam-description` + `routing-suggestion`.

### Check 2 — Followability

Assuming a reader has read prior chapters in the series, can they follow this chapter's narrative arc end-to-end? Where does a causal hand-off between facets fail (preamble names X; body never reconnects to X; reader holds the name without anchor)? Where does a scene-boundary fail (scene-A closes on register Y; scene-B opens incompatible with Y)? Flag `FOLLOWABILITY-BREAK @<bone>` with `hand-off-description` + `routing-suggestion`.

### Check 3 — Cold-read-risk surface

Reading the assembled prose with substance context, flag any span that would PLAUSIBLY misread to a first-time cold-reader despite being substance-correct under the chapter contract. The reviewer must cite:
- The **misread vector** (what the cold-reader's interpretation would be)
- The **substance-correct reading** (what the chunk + bones + facets authorize)
- The **misread confidence** (low / medium / high — would-likely-fire-at-Phase-9)
- The **routing recommendation** (per-layer; see Routing below)

Flag `COLD-READ-RISK @<bone>`. The FAIL #2 sexual-assault mechanism at b01-c05 @14 is the canonical instance of this finding class: substance-correct as enforcement (chunk-authorized), prose-vector misread-prone (generic-object bone + sensory-facet rendering invented connotation).

**Check 3 addendum — central-event-muffle (PROP-0019-A; armed by upstream voice-risk).** If `chapters[<slug>].chunk_cold_read.verdict == PASS-CHUNK-VOICE-RISK`, read `voice_risk.voice_risk_carry` for the named central event + the abstraction-vocabulary that renders it. Then verify the **assembled** prose delivers that central event at cold-reader legibility — a first-time reader must register the event AS the event, not as one more line of process/instrument abstraction. If the event reaches the reader only through abstraction-vocabulary (the FAIL #1 muffling mechanism — "a beating I almost missed"), flag `COLD-READ-RISK central-event-muffled @<bone>` at HIGH confidence, routing to stitch-revise (de-abstract the event span — restore concrete actor-verb-object at the beat) or, if the bone itself lacks a concrete event verb, bones-revise. This is the downstream catch for the defect class the chunk-cold-read structurally cannot see; the upstream `PASS-CHUNK-VOICE-RISK` exists precisely to ensure this check fires.

**Output.** Classified findings to `active-project/staff/reviews/coherence-<book>-<chapter>-<timestamp>.md`. Summary appended to render-log under `## Phase 8.5 — coherence review`.

**Routing.**

| Finding class | Severity | Routing |
|---------------|----------|---------|
| `WEAVE-GAP` | SOFT-BLOCK | per finding's `routing-suggestion`: stitch-layer (per-scene re-render); exposition-layer (re-author entry + re-fire Phase 0.6); bones-layer (`/and-write` revise on named bone) |
| `FOLLOWABILITY-BREAK` | SOFT-BLOCK | same per-layer routing as WEAVE-GAP |
| `COLD-READ-RISK` (high confidence) | SOFT-BLOCK | same per-layer routing |
| `COLD-READ-RISK` (medium / low confidence) | ADVISORY | record on `chapters[<slug>].coherence_review.findings[]`; Phase 9 reads as additional context; does not block |

**SOFT-BLOCK behavior.** Pipeline pauses; offending span re-routed to the named layer (stitch / exposition / bones). After remediation, Phase 8.5 re-runs ONCE on the changed spans only. The gate's purpose is to drain pre-Phase-9 catches; it is not a convergence loop.

**Cap.** Phase 8.5 may trigger at most ONE round of stitch/exposition/bones revise before Phase 9 fires regardless. Unresolved findings carry forward to Phase 9 + render-log; the Phase 9.5 admin process-critic dispatch receives the coherence-review report as additional context.

**Memory writes:**
```yaml
chapters[<slug>].coherence_review:
  reviewed_at: <iso>
  verdict: PASS | SOFT-BLOCK-RESOLVED | SOFT-BLOCK-UNRESOLVED-PROCEED-ANYWAY
  weave_gaps: <N>
  followability_breaks: <N>
  cold_read_risk_high: <N>
  cold_read_risk_advisory: <N>
  findings: [...]
  report_path: active-project/staff/reviews/coherence-<book>-<chapter>-<timestamp>.md
```

The verdict is consumed by Phase 9 Step 4: a Phase 8.5 `PASS` reduces the prior weight on Phase 9 staging-cluster + prose-rationale findings (they've been pre-checked at a more integrated layer); a Phase 8.5 `SOFT-BLOCK-UNRESOLVED-PROCEED-ANYWAY` increases the weight on Phase 9 admin process-critic (the unresolved findings name what to expect).

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

**Spine-promotion (URI-STITCH-SPINE-STAGING — 2026-05-29).** Staging findings block only *in aggregate* via the Step 4 cluster check — which means a single serious additive gap on the chapter's spine ships advisory. That is the exact airless-certification failure the cluster threshold lets through one-at-a-time. Exception, therefore: a `STAGE` / `GROUND` / `NEEDS-BEAT` / `EXPAND` finding whose anchor bone is the scene's **central-event bone** or a **stakes-axis bone** (resolve via `chapters[<slug>].scenes[].event_map[]` central event + `scene_conflict.stakes_axis` → bone) is promoted from advisory to **blocking even singly**. It sets the Step 4 cluster trigger `spine-staging-gap`. A `STAGE` or `NEEDS-BEAT` finding on the **central-event bone itself** (not merely a stakes-axis bone) escalates further to a full **FAIL** — an un-staged central event is a decomposition defect, identical in consequence to a cold-read FAIL. As with all staging routing, the fix goes to `/and-write revise` (re-decompose the spine), never to a stitch-layer addition (the bone-faithfulness fence forbids the stitcher adding content). This is the additive-side counterpart to the subtractive verbs the stitcher already trusts to block.

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

**The canonical lever for cold-read findings is /and-write revise --from-signals (URI-STITCH-COLD-READ-FEEDBACK-LOOP, 2026-05-27 remediation; option E from the b01-c02 cherry-pick experiment).** The c02 experiment (commit `2d525d2`) explicitly concluded *"cost-legibility lives in bones SVO authoring, not stitch paragraph composition. Per-paragraph craft optimization is not predictive of continue-rate."* Cold-read signals — particularly walkout-severity peeves (`protagonist-arc-cost-not-legible`), reader-orientation gaps (`who is anyone` / `who is X`), and gestured-at-recognition patterns — route upstream to `/and-write` rather than to stitcher-layer fixes. Per the routing below: FAIL → `/and-write revise`; PASS-WITH-DEPTH-PASS-REQUIRED → `/and-write revise --from-signals`. The staging report's pattern catalog + the cold-read's confusion log are the canonical signal payload for the upstream revise. Stitch-layer rubric edits (cherry-pick tuning, prime selection) are a smaller-magnitude lever than this loop.

**Tournament scorecard back-reference (URI-STITCH-SCORECARD-BACKREF, 2026-05-27).** Phase 1.5 Step 3 already appended partial rows to `active-project/staff/showrunner/tournament-scorecards.md` (one per scene, with the Phase 9 fields blank). Now update those rows in-place with this chapter's Phase 9 verdict + CONTINUE outcome. The accumulating ledger is the cross-chapter tuning signal (see `design/tournament-tuning.md`). Format per `schemas/tournament-scorecard.schema.md` § Chapter-aggregate ledger format. This is a mechanical write — no fork dispatch needed. (Note: this back-reference fires only when Phase 1.5 actually ran — multi-arm opt-in via user-authored alts on disk. Default single-arm runs do not produce scorecard rows.)

**Cluster check (URI-STITCH-SIGNAL-CLUSTER — soft-gate; 2026-05-24; threshold tightened 2026-05-25).** Before printing the verdict, scan the staging report's findings and bin them by pattern label AND by zone (peak vs non-peak via `chapters[<slug>].cold_read.zone_density_observation` or per-bone peak-flag from staging review) AND by bone-class (axis-move vs held-vs chatter from `bones[].substance_delta`). A *cluster* fires when ANY of:

- **same-pattern ≥5** — `N >= 5 SIGNAL findings sharing the same pattern label` (e.g. `body-staging-gap`, `opposing-force-prose-mute`, `held-bone-rationale-only`). (Original 2026-05-24 trigger; retained.)
- **adjacent-in-peak-zone ≥3** — `N >= 3 SIGNAL findings sharing the same pattern label AND ≥3 of those findings are on bones inside a peak zone (3+ consecutive flat-ids inside the scene-conflict peak)`. The b01c01 cluster — 4 peak-under-staged findings at @11/@12/@13/@21 with 3 adjacent in scene-B's peak — sat below the same-pattern≥5 threshold and shipped advisory. This trigger catches that exact failure mode.
- **on-axis-move-bones ≥3** — `N >= 3 SIGNAL findings sharing the same pattern label AND all findings are on bones whose substance_delta.axis_moves is non-empty`. A pattern concentrated on axis-move bones is the difference between a stylistic note (cluster across held + chatter) and a substance-delivery failure (cluster on the bones that carry the chapter's declared deltas). Tighter threshold than same-pattern≥5 because the axis-move concentration is itself the signal.
- **spine-staging-gap ≥1** — `≥1 staging finding (STAGE / GROUND / NEEDS-BEAT / EXPAND) on a central-event bone or a stakes-axis bone` (URI-STITCH-SPINE-STAGING; 2026-05-29; see Step 3 spine-promotion). The tightest trigger by design: the spine carries the chapter, so one additive gap there is not advisory. Fires the soft-gate (`PASS-WITH-DEPTH-PASS-REQUIRED`). NOTE: a `STAGE` / `NEEDS-BEAT` finding on the **central-event bone itself** does not stop at the soft-gate — it escalates to **FAIL** per Step 3 (route to `/and-write revise`).

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
- **FAIL** — the chapter is NOT terminal. It is a structural failure, not a polish problem — re-decompose from the bones up. FAIL fires on EITHER (a) the Step 2 cold-read diff (the reader could not recover the central event / jeopardy / would-not-continue) OR (b) a Step 3 spine-promotion `STAGE` / `NEEDS-BEAT` finding **on the central-event bone itself** (URI-STITCH-SPINE-STAGING — an un-staged central event is a decomposition defect even when the cold-reader limped past it). Print the cold reader's answers (and, for (b), the spine-staging finding + its bone), the diff finding, and route:
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
