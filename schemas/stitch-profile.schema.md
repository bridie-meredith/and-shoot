# Stitch Profile Schema

Tuning surface for the Stitcher agent. Defines voice target, lens-decider configuration, fork granularity, redundancy rules, compression aggressiveness, local-flow constraints, render-vs-ignore by facet type, protected-pattern overrides, output mode, and re-stitch behavior.

Schema authority: this file.

Status: **draft (tuning)**. The knob inventory will expand as more scenes surface decisions Scene C and Scene L don't.

---

## File path conventions

- **Episode default:** `active-project/theater/stitch-profile.md` — one profile per active episode. Read by every fork.
- **Per-scene override (optional):** `active-project/theater/stitch-profile-<scene-label>.md` — overrides episode default for the matching scene only. Scene labels resolve via `interest-narrator.md`'s sparsity-gradient section.
- **Project default (optional):** `active-project/stitch-profile.md` — applies to any episode without an episode-level profile.

Resolution order: scene override → episode default → project default → schema defaults.

---

## Profile structure

YAML frontmatter, optionally with a markdown body for human notes.

```yaml
---
profile-name: <descriptive label>
scope: episode | scene | project
applies-to: <episode-slug | scene-label | project-slug>
persona: <stitcher-persona-slug>            # default: neutral

project:                                    # project-scoped fences (typically authored at the project-default profile only)
  anti-jargon:                              # invented compounds and jargon-nominalizations the project has accumulated. Phase 1 forks see this list and pre-empt; Phase 7 Q9 references it. Substring match, case-insensitive.
    - <token>                               # e.g. watch-cost / mother-singing / density-compound / pricing
  hollow-prose-patterns:                    # surface patterns Q5 cuts on sight under strict mode
    - <pattern>                             # e.g. "X was the verdict" / "X is what Y does when Z runs out"
  bone-faithfulness-fence:                  # what Phase 1 forks MUST NOT invent in prose
    invent-dialogue-content: false          # bone "speaks to X" does not license "asked where" / "told me Y"
    invent-body-detail: false               # bone "exits the margin" does not license "slid past the gatepost"
    invent-spatial-detail: false            # bone "enters the village" does not license "through the yard gate"
    invent-scene-prose: false               # no "quick, low, threading the stalls" beyond bone/facet content

voice:
  tense: past | present                     # default: past
  person: first | third                     # default: first
  pov: <actor-slug>                         # default: resolved from proto-lines header `narrator:`
  contractions: true | false                # default: true

render:
  facet-types:
    bones: true                             # never false (fault if set false)
    narrator: true
    feel: true
    memory: true
    sensory: true
    metaphor: true
    tens: false                             # always false — selection signal only (fault if true)
    state: false                            # always false — continuity only (fault if true)
    vibes: false                            # always false — bias only (fault if true)
    location-state: at-establishment        # at-establishment | always | never
  cap-per-anchor: 5
  peak-priority: [feel, narrator, memory, sensory, metaphor]
  nonpeak-priority: [narrator, feel, sensory, memory, metaphor]

phase-1:
  fork-granularity: per-anchor
  continuity-context: previous-2-lines      # previous-2-lines | previous-paragraph | none
  parallel: within-paragraph                # within-paragraph | full | sequential
  lens-decider:
    enable-rule-1-foreknowledge-clamp: true
    enable-rule-2-sensory-spike: true
    enable-rule-3-peak-feel: true
    enable-rule-4-kinetic-order: true
    enable-rule-5-recent-focus-damping: true
    rule-5-window: 2
    persona-overrides: enabled
    tiebreaker: neutral-default             # neutral-default | explore (future)
  foreknowledge-language:                   # rule-1 trigger words
    - already
    - had been
    - had counted
    - had mapped
    - had cleared
    - had named

redundancy:
  detector: closing-phrase-echo             # closing-phrase-echo | image-set-overlap | both | off
  echo-window: 1                            # bones within this distance count for echo
  preserve-anchor: narrator                 # which facet wins when echo detected

compression:
  same-subject-merge: true
  pronoun-substitution: after-first         # after-first | strategic | preserve-all
  tens1-run-collapse: preserve-buildups     # aggressive | preserve-buildups | off
  exit-trio-merge: true
  zero-cite-bone-policy: render             # render | merge-with-adjacent | drop

voice-transform:
  bone-object-policy: verbatim              # verbatim | idiom-fit
  third-party-preserve: [Tya, Watch]
  feeling-clause-pov-resolution: auto       # auto | manual
  sensory-arrow-rendering: prose-template   # prose-template | drop-if-covered

local-flow:
  window-size: 3
  sensory-deferral-cap: 2
  ni-promotion-cap: 1
  within-anchor-order: em-dash-fusion       # em-dash-fusion | cite-index | body-first | meaning-first
  temporal-lock-words:
    - first
    - second
    - third
    - next
    - before
    - after
    - soon
    - now
    - then
    - immediately
  un-merge-license: true

protected-patterns:
  - three-note-buildup
  - countdown
  - threshold-cross
  - return-of

phase-7:
  enabled: true
  questions: standard                       # standard (Q1-Q9) | strict-only (Q1) | extended (future)
  cut-aggressiveness: strict                # strict (borderline=reject) | standard | permissive
  persona-overrides: enabled
  reshow-enabled: true                      # Q8 may trigger RESHOW with ≥2-source license
  reshow-min-sources: 2                     # minimum graph sources licensing a reshow
  reword-enabled: true                      # Q9 may trigger REWORD
  reword-density-cap: 2                     # max REWORDs per sentence; 3+ escalates to RESHOW
  reword-vocabulary-policy: common-english  # no invented compounds in replacements
  bones-cuttable: anchor-cut-only           # never | anchor-cut-only | strict-q1 | always
  borderline-policy: reject                 # reject (strict) | keep (standard) | flag (permissive)

output:
  mode: dual                                # dual | clean-only
  line-ids: stable                          # stable (gaps allowed) | dense
  trace-verbosity: change-only              # change-only | full

interval-bridge:                            # brief frame paragraph prepended to the polish
  enabled: true | false                     # default: true at project scope
  mode: cold-start | prior-episode | auto   # default: auto (resolves from showrunner memory's prior_episode field)
  voice: pov-frame | omniscient | author    # default: pov-frame (renders in narrator's voice as a remembered/told frame)
  length-target: brief | medium             # brief: ≤80 words; medium: ≤160 words
  cold-start-sources:                       # used when no prior episode exists
    - series-plan.plot.start
    - series-plan.protagonist_arc
    - world-build-cards (relevant only)
    - episode.chunk
  prior-episode-sources:                    # used when prior_episode exists
    - prior-episode.terminal-state          # from showrunner memory or prior polish's last scene
    - prior-episode.unfinished-business     # carry-forward stakes
    - episode.chunk                         # this episode's opening
    - interval-delta                        # what changed between prior-terminal and this-open (time-gap, locale-shift, character-state-shift)
  set-off:                                  # how to mark the bridge as frame vs body
    style: italic                           # italic | header | quote-block
    separator: rule                         # rule (---) | blank-line | none
  forbidden-content:                        # the bridge MUST NOT do these
    - plot-content-not-in-graph             # bridge is recap/orient only; no new events
    - character-card-paraphrase             # don't write the cast as a glossary
    - explicit-author-meta                  # no "in this episode..." TV-narrator voice unless voice: author

feedback:
  feedback-file: staff/stitcher/feedback-<slug>.md
  re-stitch-scope: fork-plus-downstream     # fork-only | fork-plus-downstream | full

scene-overrides:
  scene-c:
    voice.person: first
  scene-l:
    render.peak-priority: [memory, narrator, sensory]
---

# Optional notes
Free-form human notes — why this profile, what's been tuned, what's an open question.
```

---

## Field rules

### `voice:`

- **`tense`** — applied at Phase 4. Affects bone verbs, NI clauses, feel clauses, mem clauses, sensory arrow forms.
- **`person`** — applied at Phase 4. POV character (per `pov:`) maps to the chosen person; everyone else stays third-person.
- **`pov`** — defaults to the proto-lines file's `narrator:` field. Override only when proto-lines narrator and rendered POV intentionally differ (e.g. a flashback in another character's POV).
- **`contractions`** — `true` renders "did not" → "didn't" etc.

### `render:`

- **`facet-types`** — boolean per type. `bones: false` is a fault. `tens`, `state`, `vibes` forced false by the schema; setting true is a fault.
- **`cap-per-anchor`** — maximum cites rendered at a single anchor. Excess dropped per priority list. Counts the bone plus rendered facets.
- **`peak-priority`** / **`nonpeak-priority`** — ordered list. At tens=3 (peak) anchors, when cap is reached, render in `peak-priority` order. Tens=1 and tens=2 use `nonpeak-priority`. First wins.
- **`location-state`** — render-or-not is anchor-dependent. `at-establishment` renders at the first anchor in a new location; skips thereafter unless conditions field changes. `always` renders every cite. `never` skips entirely.

### `phase-1:`

The lens-anchored render configuration.

- **`fork-granularity`** — `per-anchor` is the working default. Other values not yet supported.
- **`continuity-context`** — what previous output each fork sees. `previous-2-lines` (default) gives continuity but serializes adjacent forks within a paragraph. `previous-paragraph` is more serial; `none` is maximally parallel but accepts continuity drift (Phase 5 and 7 catch it).
- **`parallel`** — `within-paragraph` runs forks in parallel within a paragraph (serial across paragraphs); `full` parallelizes everything (only valid with `continuity-context: none`); `sequential` runs one fork at a time.
- **`lens-decider`** — rule toggles. Each `enable-rule-N-*` flag turns one rule on or off; disabling rules is for experimentation. Defaults: all on.
- **`lens-decider.rule-5-window`** — recent-focus damping lookback. Higher values dampen lens-rhythm saturation more aggressively.
- **`lens-decider.persona-overrides`** — whether persona's `## Lens biases` table is consulted. Default enabled.
- **`lens-decider.tiebreaker`** — `neutral-default` falls through to neutral-persona kinetic order. `explore` (future enhancement, not v1) emits both candidates with a `CHOICE-DEFERRED` trace tag.
- **`foreknowledge-language`** — list of words/phrases that trigger rule 1 (NI leads). The default list covers the canonical foreknowledge-clamp register; project-specific additions land here.

### `redundancy:`

- **`detector`** — `closing-phrase-echo` matches last N words of co-anchored facet clauses; `image-set-overlap` matches noun-set overlap; `both` requires both to fire; `off` disables.
- **`echo-window`** — how many bones a facet's content is checked against. `1` means same-anchor only; higher values catch cross-bone echoes.
- **`preserve-anchor`** — when echo fires, which facet type wins. The other is dropped with a log entry.

### `compression:`

- **`same-subject-merge`** — bones N and N+1 with same subject and continuous action merge.
- **`pronoun-substitution`** — `after-first` substitutes "she" for second-onward occurrence of "the mother" within a paragraph; `strategic` substitutes only when repetition would saturate; `preserve-all` disables.
- **`tens1-run-collapse`** — `aggressive` collapses any run of ≥3 tens=1 zero-cite bones; `preserve-buildups` keeps the buildup-pattern detector active to protect structural sequences; `off` disables collapse.
- **`exit-trio-merge`** — boolean. The specific case of three terminal bones (set-bowl / face-wall / exit pattern).
- **`zero-cite-bone-policy`** — what to do with bones carrying no facet citations. `render` keeps them; `merge-with-adjacent` folds them into neighbor; `drop` removes (logged).

### `voice-transform:`

- **`bone-object-policy`** — `verbatim` preserves the bone's object exactly ("holds the eyes"); `idiom-fit` allows English-idiom adjustment ("holds her gaze"). Verbatim is the schema-faithful default.
- **`third-party-preserve`** — named entities that never person-shift even if grammatically adjacent to POV.
- **`feeling-clause-pov-resolution`** — `auto` resolves "the girl's face" → "my face" when POV is the only matching referent at the anchor; `manual` requires explicit mapping.
- **`sensory-arrow-rendering`** — `prose-template` applies a template ("X gave way to Y"); `drop-if-covered` drops the sensory delta if the adjacent bone verb already carries the modality shift.

### `local-flow:`

- **`window-size`** — sliding window in bones. 3 (prev + current + next) is the working default.
- **`sensory-deferral-cap`** — forward migration distance limit for sensory deltas. Cumulative deltas can move forward up to N bones; spike/drop cannot move.
- **`ni-promotion-cap`** — backward migration distance for NI clauses.
- **`within-anchor-order`** — when multiple cites land at one anchor after redundancy cull. `em-dash-fusion` joins bone + one facet with em-dash; others as listed in card.
- **`temporal-lock-words`** — clauses containing any of these words cannot migrate. Conservative default; tune by adding scene-specific lock words.
- **`un-merge-license`** — whether local flow may undo a Phase 3 merge to rescue a swallowed facet.

### `protected-patterns:`

A list of named patterns Phase 6 restores if Phase 3 flattened them. Each pattern resolves to a detector: `three-note-buildup` looks for three bones with monotonic ordinal verbs on the same subject; `countdown` for descending; `threshold-cross` for gate/door/commit cluster; `return-of` for callback bones.

### `phase-7:`

Editorial reflection configuration.

- **`enabled`** — boolean. Disabling skips Phase 7 entirely.
- **`questions`** — which question set runs. `standard` is the canonical nine (Q1–Q9, including Q8 RESHOW and Q9 REWORD). `strict-only` runs only Q1 (the load-bearing counterfactual). `extended` is reserved for future projects that add domain-specific questions.
- **`cut-aggressiveness`** — answer posture. **`strict`** (default) treats borderline as reject; the burden of proof is on keeping. `standard` treats borderline as keep. `permissive` keeps unless clear violation. Most projects want strict.
- **`persona-overrides`** — whether persona's `## Phase 7 biases` section is consulted.
- **`reshow-enabled`** — whether Q8 may trigger a `RESHOW` move (clause reauthored through different surface, requiring ≥2 graph sources).
- **`reshow-min-sources`** — minimum number of citable graph sources required to license a RESHOW. Default 2 (the original facet + 1 corroborating source from character cards / vibes / world-build / other facets).
- **`reword-enabled`** — whether Q9 may trigger a `REWORD` move (single word/phrase substitution with meaning-preserving common-English equivalent).
- **`reword-density-cap`** — max REWORDs per sentence. 2 by default. 3+ awkward words escalates the sentence to RESHOW.
- **`reword-vocabulary-policy`** — `common-english` forbids invented compounds in replacements. The replacement uses natural English; no new jargon to replace old jargon.
- **`bones-cuttable`** — when Phase 7 may cut a bone. `never` (strictest preservation), `anchor-cut-only` (default — bone may cut only if a protective facet anchor was also cut at Phase 7 and adjacent merge loses no action), `strict-q1` (any bone failing Q1 cuts), `always` (bones treated like any other line).
- **`borderline-policy`** — `reject` (strict — borderline = cut), `keep` (standard), `flag` (permissive — emit NEEDS_EDIT annotation for the editor).

### `output:`

- **`mode`** — `dual` writes both clean and annotated; `clean-only` writes only the polish file. Default `dual` during tuning; flip to `clean-only` for production.
- **`line-ids`** — `stable` assigns IDs at Phase 8 and preserves them across edits (gaps allowed when sentences are later cut); `dense` renumbers on each run.
- **`trace-verbosity`** — `change-only` records phases that made changes plus the lens-decider firing; `full` records every phase touching every line.

### `feedback:`

- **`feedback-file`** — path to the line-keyed feedback file. Default convention is `staff/stitcher/feedback-<slug>.md`.
- **`re-stitch-scope`** — what re-runs when feedback lands. `fork-only` re-runs just the originating fork; `fork-plus-downstream` (default) also re-runs downstream phases whose log entries reference the affected anchor or line-ID; `full` re-runs the entire chain.

### `interval-bridge:`

A brief frame paragraph prepended to the polish file, bridging the gap between the end of the prior chapter and the start of this one.

- **First episode of a series** (no `prior_episode` in showrunner memory): `mode: cold-start`. The bridge orients the reader to where the protagonist was at the end of their *implicit* prior chapter (e.g. for a fix-fic, the end of the source canon) and what's now true at episode-open. Sources: `series-plan.plot.start`, `series-plan.protagonist_arc`, relevant world-build cards, this episode's `chunk`.
- **Subsequent episodes**: `mode: prior-episode`. The bridge recaps the prior episode's terminal state, any unfinished business that carries forward, the time-gap or locale-shift between prior-end and this-open, and lands the reader where the new episode picks up. Sources: prior episode's polish (last scene), showrunner memory's terminal-state notes, this episode's `chunk`.
- **`auto`** (default): the command body picks the mode from showrunner memory.

The bridge is **brief and compelling, not encyclopedic**. Length-target `brief` caps at ~80 words; `medium` at ~160. Voice defaults to `pov-frame` — rendered in the narrator's voice as a frame device (a remembered telling, a "before:" preface). Set off from the body via italics + horizontal rule by default.

The bridge must NOT add new plot content, paraphrase character cards as a cast glossary, or reach for explicit TV-narrator framing unless `voice: author` is set. It restates already-graph-resident information in a compressed orienting form. The Phase 0.6 fork's output goes through a faithfulness check: every claim in the bridge must trace to a source in `cold-start-sources` or `prior-episode-sources`.

Inline overrides keyed by scene label. Each override is a partial profile that shallow-merges over the episode default for the named scene only.

### `persona:`

References a stitcher-persona card at `staff/stitcher/personas/<slug>.md`. The persona biases:
- Lens-decider rule 6 (per anchor type)
- Phase 7 question aggressiveness (per question)

Defaults to `neutral` — the reference persona with no overrides.

---

## Resolution and validation

Phase 0 reads:
1. The active scene's per-scene profile if present.
2. The episode default profile.
3. The project default profile if present.
4. The schema defaults from this file.

Each layer shallow-merges over the next. Field-level merge: a scene profile with `voice.person: first` does not need to restate the full `voice:` block.

Validation faults:
- `FAULT-PROFILE-MISSING-POV` — `voice.pov` unset and proto-lines header has no `narrator:` field.
- `FAULT-PROFILE-FORBIDDEN-RENDER` — `render.facet-types.tens|state|vibes` set true.
- `FAULT-PROFILE-BONES-OFF` — `render.facet-types.bones` set false.
- `FAULT-PROFILE-INCONSISTENT-VOICE` — `voice.person: first` with no resolvable `pov:`.
- `FAULT-PROFILE-UNKNOWN-PATTERN` — `protected-patterns` lists a pattern with no detector.
- `FAULT-PROFILE-INVALID-PARALLEL` — `parallel: full` with `continuity-context` not `none`.
- `FAULT-PROFILE-MISSING-PERSONA` — `persona:` set to a slug with no card at `staff/stitcher/personas/<slug>.md`.
- `FAULT-PROFILE-PERSONA-MISMATCH-PROJECT` — resolved persona is `neutral` AND a project-default profile at `active-project/stitch-profile.md` exists declaring a non-neutral persona, OR a project-scoped persona exists at `active-project/staff/stitcher/personas/`. Pipeline must escalate to user — running with `neutral` against a project that has authored a tuned persona is almost always a misconfiguration. User must either confirm `neutral` explicitly (`--persona neutral`) or correct the profile.
- `FAULT-PROFILE-MISSING-PROJECT-ANTI-JARGON` — soft. Project-default profile exists but lacks `project.anti-jargon`. Emit warning at Phase 0; do not block. Phase 1 forks will fall back to persona-card tuning notes only.

---

## Render-log and feedback (cross-reference)

The Stitcher's per-fork output is logged to `staff/stitcher/render-log-<slug>.md`. See `schemas/stitch-render-log.schema.md` for per-fork entry format and the trace block grammar.

Line-keyed feedback consumed by the stitcher on re-runs lives at the path specified in `feedback.feedback-file`. See `schemas/stitch-feedback.schema.md` for entry format.

---

## What this schema does not cover

- The stitcher persona library at `staff/stitcher/personas/`. See `staff/stitcher/card.md § Persona plugin` and individual persona cards.
- Cross-episode continuity (voice register continuity between e01 and e02). Currently the editor's domain in `/and-wrap`, not the stitcher's.
- The actual prose-output schema. Polish files are constrained by what each phase writes, not by a standalone schema.
