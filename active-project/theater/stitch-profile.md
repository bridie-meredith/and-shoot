---
profile-name: s01e01-first-person-past
scope: episode
applies-to: s01e01
persona: neutral

voice:
  tense: past
  person: first
  pov: taylor-hebert-flea-bottom
  contractions: true

render:
  facet-types:
    bones: true
    narrator: true
    feel: true
    memory: true
    sensory: true
    metaphor: true
    tens: false
    state: false
    vibes: false
    location-state: at-establishment
  cap-per-anchor: 5
  peak-priority: [feel, narrator, memory, sensory, metaphor]
  nonpeak-priority: [narrator, feel, sensory, memory, metaphor]

phase-1:
  fork-granularity: per-anchor
  continuity-context: previous-2-lines
  parallel: within-paragraph
  lens-decider:
    enable-rule-1-foreknowledge-clamp: true
    enable-rule-2-sensory-spike: true
    enable-rule-3-peak-feel: true
    enable-rule-4-kinetic-order: true
    enable-rule-5-recent-focus-damping: true
    rule-5-window: 2
    persona-overrides: enabled
    tiebreaker: neutral-default
  foreknowledge-language:
    - already
    - had been
    - had counted
    - had mapped
    - had cleared
    - had named

redundancy:
  detector: closing-phrase-echo
  echo-window: 1
  preserve-anchor: narrator

compression:
  same-subject-merge: true
  pronoun-substitution: after-first
  tens1-run-collapse: preserve-buildups
  exit-trio-merge: true
  zero-cite-bone-policy: render

voice-transform:
  bone-object-policy: idiom-fit
  third-party-preserve: [Tya, Watch, King's Landing, Fish Gate]
  feeling-clause-pov-resolution: auto
  sensory-arrow-rendering: prose-template

local-flow:
  window-size: 3
  sensory-deferral-cap: 2
  ni-promotion-cap: 1
  within-anchor-order: em-dash-fusion
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
  questions: standard
  cut-aggressiveness: strict
  persona-overrides: enabled
  reshow-enabled: true
  reshow-min-sources: 2
  reword-enabled: true
  reword-density-cap: 2
  reword-vocabulary-policy: common-english
  bones-cuttable: anchor-cut-only
  borderline-policy: reject

output:
  mode: dual
  line-ids: stable
  trace-verbosity: change-only

feedback:
  feedback-file: staff/stitcher/feedback-s01e01.md
  re-stitch-scope: fork-plus-downstream
---

# Notes

First-person past-tense stitch of s01e01. POV = taylor-hebert-flea-bottom (sole POV per series spec). Voice: past tense, first person, contractions on. Reads s01e01-archive proto-lines and facets (the canonical s01e01 inputs, archived 2026-05-11).
