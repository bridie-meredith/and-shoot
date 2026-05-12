# Stitch Profile Schema

Tuning surface for the Stitcher agent. Defines voice target, redundancy rules, compression aggressiveness, local-flow constraints, render-vs-ignore by facet type, and protected-pattern overrides.

Schema authority: this file.

Status: **draft (tuning)**. The knob inventory will expand as more scenes surface decisions Scene C and Scene L don't.

---

## File path conventions

- **Episode default:** `active-project/theater/stitch-profile.md` — one profile per active episode. Read by every pass.
- **Per-scene override (optional):** `active-project/theater/stitch-profile-<scene-label>.md` — e.g. `stitch-profile-scene-c.md`. Overrides episode-default for the matching scene only. Scene labels resolve via `interest-narrator.md`'s sparsity-gradient section.
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
persona: <stitcher-persona-slug>   # optional; see staff/stitcher/personas/

voice:
  tense: past | present
  person: first | third
  pov: <actor-slug>                # default: resolved from proto-lines header `narrator:`
  contractions: true | false       # default: true

render:
  facet-types:
    bones: true                    # never false
    narrator: true
    feel: true
    memory: true
    sensory: true
    metaphor: true
    tens: false                    # always false — selection signal only
    state: false                   # always false — continuity only
    vibes: false                   # always false — bias only
    location-state: <see below>
  cap-per-anchor: 5 | <integer>
  peak-priority: [feel, narrator, memory, sensory, metaphor]
  nonpeak-priority: [narrator, feel, sensory, memory, metaphor]

redundancy:
  detector: closing-phrase-echo | image-set-overlap | both | off
  echo-window: 1 | <integer>       # bones within this distance count for echo
  preserve-anchor: narrator        # which facet wins when echo detected

compression:
  same-subject-merge: true | false
  pronoun-substitution: after-first | strategic | preserve-all
  tens1-run-collapse: aggressive | preserve | off
  exit-trio-merge: true | false
  zero-cite-bone-policy: render | merge-with-adjacent | drop

voice-transform:
  bone-object-policy: verbatim | idiom-fit
  third-party-preserve: [Tya, Watch, ...]  # named entities that never person-shift
  feeling-clause-pov-resolution: auto | manual
  sensory-arrow-rendering: prose-template | drop-if-covered

local-flow:
  window-size: 3 | <integer>       # bones in sliding window
  sensory-deferral-cap: 2 | <integer>
  ni-promotion-cap: 1 | <integer>
  within-anchor-order: em-dash-fusion | cite-index | body-first | meaning-first
  temporal-lock-words: [first, second, third, next, before, after, soon, now, then, immediately]
  un-merge-license: true | false

protected-patterns:
  - three-note-buildup           # any 3-bone monotonic structural-pivot sequence
  - countdown                     # N-1-bone descent
  - threshold-cross               # gate / door / commit cluster
  - return-of                     # callback bones
  # patterns listed here are reviewed at Phase 6 and restored if Phase 3 flattened them

scene-overrides:                  # optional inline overrides
  scene-c:
    voice.person: first
  scene-l:
    render.peak-priority: [memory, narrator, sensory]   # no feel co-cite at @134
---

# Optional notes
Free-form human notes — why this profile, what's been tuned, what's an open question.
```

---

## Field rules

### `voice:`

- **`tense`** — applied at Phase 4. Affects bone verbs, NI clauses, feel clauses, mem clauses, sensory arrow forms.
- **`person`** — applied at Phase 4. POV character (per `pov:`) maps to the chosen person; everyone else stays third-person. `first` + plural narrators is undefined — fault.
- **`pov`** — defaults to the proto-lines file's `narrator:` field. Override only when the proto-lines narrator and the rendered POV intentionally differ (e.g. a flashback in another character's POV).
- **`contractions`** — `true` renders "did not" → "didn't" etc. Match the prior episode's register if continuing a series.

### `render:`

- **`facet-types`** — boolean per type. `bones: false` is a fault. `tens`, `state`, `vibes` are forced false by the schema; setting true is a fault.
- **`cap-per-anchor`** — maximum number of cites rendered at a single bone. Excess is dropped per priority list. Cap counts the bone itself plus the rendered facets.
- **`peak-priority`** — ordered list of facet types. At tens=3 anchors, when the cap is reached, render in this order. First wins.
- **`nonpeak-priority`** — same as peak-priority, applied at tens=1 and tens=2 anchors.
- **`location-state`** — render-or-not is anchor-dependent. Default policy: render at the first anchor in a new location (location-establishment); skip thereafter unless the conditions field changes.

### `redundancy:`

- **`detector`** — `closing-phrase-echo` matches the last N words of two co-anchored facet clauses; `image-set-overlap` matches noun-set overlap; `both` requires both to fire; `off` disables.
- **`echo-window`** — how many bones a facet's content can be checked against. `1` means same-anchor only; higher values catch cross-bone echoes (rare but possible).
- **`preserve-anchor`** — when echo fires, which facet type wins. The other is dropped with a log entry.

### `compression:`

- **`same-subject-merge`** — bones N and N+1 with the same subject and continuous action merge into one sentence with serial-comma verbs.
- **`pronoun-substitution`** — `after-first` substitutes "she" for the second-onward occurrence of "the mother" within a paragraph; `strategic` substitutes only when repetition would otherwise saturate; `preserve-all` disables.
- **`tens1-run-collapse`** — `aggressive` collapses any run of ≥3 tens=1 bones with no cites into one merged sentence; `preserve` keeps the buildup-pattern detector in play; `off` disables.
- **`exit-trio-merge`** — the specific case of three terminal bones (set-bowl / face-wall / exit pattern). Boolean.
- **`zero-cite-bone-policy`** — what to do with bones that carry no facet citations. Renders by default; can be merged or dropped.

### `voice-transform:`

- **`bone-object-policy`** — `verbatim` preserves the bone's object exactly ("holds the eyes"); `idiom-fit` allows English-idiom adjustment ("holds her gaze"). Verbatim is the schema-faithful default.
- **`third-party-preserve`** — named entities (proper nouns, distinct from POV) that must never person-shift even if grammatically adjacent. Tya is the canonical example: dead third-party referenced by POV, never the speaker.
- **`feeling-clause-pov-resolution`** — `auto` resolves "the girl's face" → "my face" when the POV is the only matching referent in the cast at that anchor; `manual` requires explicit mapping.
- **`sensory-arrow-rendering`** — `prose-template` applies a template ("X gave way to Y" / "X fell behind Y"); `drop-if-covered` drops the sensory delta if the adjacent bone verb already carries the modality shift (e.g. "She dropped the song" already conveys the sound-modality change).

### `local-flow:`

- **`window-size`** — sliding window in bones. 3 (prev + current + next) is the working default. Larger windows surface more migration candidates but slow the pass and increase composition risk.
- **`sensory-deferral-cap`** — forward migration distance limit for sensory deltas. Cumulative deltas can move forward up to N bones; non-cumulative (spike, drop) cannot move.
- **`ni-promotion-cap`** — backward migration distance for NI clauses. Capped because backward movement is rarer-but-riskier than forward.
- **`within-anchor-order`** — when multiple cites land at one bone after redundancy cull. `em-dash-fusion` joins bone + one facet with em-dash; `cite-index` preserves source order; `body-first` puts feel before NI before mem; `meaning-first` reverses.
- **`temporal-lock-words`** — clauses containing any of these words cannot migrate. The list is conservative by default; tune by adding scene-specific lock words.
- **`un-merge-license`** — whether local flow may undo a Phase 3 merge to rescue a swallowed facet. Default true.

### `protected-patterns:`

A list of named patterns Phase 6 (buildup preservation) restores if Phase 3 flattened them. Each pattern name resolves to a detector — three-note-buildup looks for three bones with monotonic ordinal verbs ("first / second / third") on the same subject; countdown for descending; etc. Add new patterns here as new scenes surface them.

### `scene-overrides:`

Inline overrides keyed by scene label. Each override is a partial profile that shallow-merges over the episode default for the named scene only. Useful when one scene wants different voice or different protected patterns without authoring a separate per-scene file.

### `persona:`

Optional. References a stitcher-persona card at `staff/stitcher/personas/<slug>.md`. The persona biases ambiguous calls within the schema's hard constraints. **Provisional — pending tuning.** See `staff/stitcher/card.md` § Persona plugin.

---

## Resolution and validation

The Stitcher's Phase 0 reads:
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

---

## Render-log schema (cross-reference)

The Stitcher's per-phase output is logged to `staff/stitcher/render-log-<episode-slug>.md`. See that file's schema (`schemas/stitch-render-log.schema.md`, pending) for the per-phase entry format.

---

## What this schema does not cover

- The stitcher persona library at `staff/stitcher/personas/`. Provisional. See `staff/stitcher/card.md` § Persona plugin.
- Cross-episode continuity (voice register continuity between e01 and e02). Currently the editor's domain in `/and-wrap`, not the stitcher's.
- The actual prose-output schema. The stitcher writes to `polish/<slug>.md`; the format of that file is constrained by what each pass writes, not by a standalone schema.
