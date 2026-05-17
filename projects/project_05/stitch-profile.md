---
profile-name: and-shoot-project-default
scope: project
applies-to: and-shoot
persona: worm-tight

project:
  anti-jargon:
    # Invented compounds and jargon-nominalizations observed in s01e01 facets that must
    # be REWORDed or cut at Phase 1. Substring match, case-insensitive.
    # Sources / categories noted in comments below; the list itself is what forks consume.
    - watch-cost                # NI register-token; reword to plain English or cut
    - mother-singing            # sensory-tag compound, never prose
    - yard-work-ambient         # sensory-tag compound
    - room-silence              # sensory-tag compound; usually drop-if-covered by bone
    - door-swing-impact         # sensory-tag compound
    - flea-bottom-density-compound  # sensory-tag; reword to concrete smells ("leather, bone, ash, sweat")
    - alley-canopy-dim          # sensory-tag; reword ("the canopy cut the light")
    - tanner-village-extrapolation  # NI nominalization; "extrapolated from the village"
    - parade-cadence            # reword to "parade beat"
    - category-event            # cut-clause; no clean substitution
    - salt-reach                # NI nominalization; "the salt"
    - eye-hold                  # body-tell nominalization; "I held her eyes"
    - mouth-parts               # body-tell nominalization; "her mouth parted"
    - pricing                   # Q9 jargon-nominalization in NI; "reading me"
    - chin-hold                 # NI nominalization
    - tanner-father             # invented compound; use "the father"
    - tanner-mother             # invented compound; use "the mother"
    - latch-tremor              # sensory nominalization; "the latch trembled"
    - position-relay            # NI nominalization
    - south-wall-footfall       # sensory nominalization
    # General categories (subagent forks should also flag any X-Y or X-Y-Z hyphenated
    # noun-compound that doesn't have a fixed referent in common English).

  hollow-prose-patterns:
    # Surface patterns Q5 cuts on sight under strict mode. Pattern templates; subagent
    # forks identify by structure not literal token.
    - "X was the verdict"
    - "X is the verdict"
    - "X was the variable Y had been waiting on"
    - "X is what Y does when Z [runs out / is unavailable]"
    - "X is the registration; Y is what Z gives W who is not W"
    - "X is the only honest thing Y has to offer; honest by what it withholds"
    - "X is the last second before Y"
    - "X is the thing Y has been waiting for and the thing Y would have refused if refusal were available"
    - "X is the body's argument, not Y's"
    - "X is the cost-of-Y to Z"

  asinine-patterns:
    # Q8 fires on these surface formulations; RESHOW preferred over CUT when ≥3 sources;
    # otherwise CUT-ASININE.
    - "the body that came back wrong"      # non-sentient-negation contrast applied to body
    - "X is not for Y; X is for the thing Y contains"   # non-sentient-negation contrast
    - "X wasn't theirs"                    # non-sentient-negation contrast on perception
    - "the gaze rested on X"               # passive-objectified gaze
    - "the wrong evidence is anything"     # non-sentient-negation with degenerate object

  bone-faithfulness-fence:
    # Phase 1 forks MUST NOT invent prose beyond what the bone + cited facets specify.
    # Voice transform (tense/person/pronoun/contraction) and listed connectives
    # (and / then / em-dash / colon / semicolon / comma) are permitted additions; all else fault.
    invent-dialogue-content: false
    invent-body-detail: false
    invent-spatial-detail: false
    invent-scene-prose: false
    # Examples of fence violations observed in prior neutral-persona run:
    #   - "I asked where. He told me." (bone @87/@88 = bare "speaks to"; dialogue content invented)
    #   - "She slid out past the gatepost on the dock line and the margin closed behind her." (bone @144 bare exit; spatial detail invented)
    #   - "The flies marked her — quick, low, threading the stalls." (bone @142 bare relay; scene prose invented)
    #   - "from the dock side" (bone @141 = "enters the Fish Gate margin"; direction invented)
    #   - "eyes down" (bone @75 = "speaks to"; body detail invented)
    #   - "through the yard gate" (bone @63 = "enters the tanner-family yard"; spatial detail invented)
    #   - "back out the way he'd come" (bone @79 = "exits the village"; route detail invented)

voice:
  tense: past
  person: first
  contractions: true

voice-transform:
  bone-object-policy: idiom-fit
  third-party-preserve: [Tya, Watch, King's Landing, Fish Gate]
  feeling-clause-pov-resolution: auto
  sensory-arrow-rendering: drop-if-covered

phase-7:
  enabled: true
  questions: standard
  cut-aggressiveness: strict
  persona-overrides: enabled
  reshow-enabled: true
  reshow-min-sources: 3              # worm-tight raises to 3 from schema default 2
  reword-enabled: true
  reword-density-cap: 2
  reword-vocabulary-policy: common-english
  bones-cuttable: anchor-cut-only
  borderline-policy: reject

output:
  mode: dual
  line-ids: stable
  trace-verbosity: change-only

interval-bridge:
  # LEGACY / FALLBACK ONLY (2026-05-12 — superseded by exposition facet).
  # The exposition-author subagent in /and-facets Round-1 now authors the
  # preamble + context paragraphs upstream with cited sources, audience-
  # modeling, R2-judging, and audit-gating. The stitcher Phase 0.6 reads
  # the exposition facet directly. This interval-bridge: block runs ONLY
  # when active-project/theater/facets/exposition-<slug>.md is absent
  # (legacy episodes pre-2026-05-12 wiring; re-run /and-facets to author
  # the missing facet). See schemas/facet.schema.md § exposition.
  enabled: true                             # fallback-armed; not normally invoked
  mode: auto                                # cold-start for s01e01; prior-episode for s01e02+
  voice: pov-frame                          # in narrator's first-person voice as a frame device
  length-target: brief                      # ≤80 words
  cold-start-sources:
    - series-plan.plot.start                # the displacement event itself
    - series-plan.protagonist_arc           # what Taylor was at the end of the implicit prior chapter (Worm-Khepri)
    - episode.chunk                         # this episode's opening situation
    - world-build:taylor-300m-sphere-flea-bottom-scope  # the swarm-came-with-her fact
    - cond-westerosi-superstition-frame-125ac  # village's "came-back-wrong" register
  prior-episode-sources:
    - prior-episode.terminal-state          # from showrunner memory; the last scene of the prior polish
    - prior-episode.unfinished-business     # carry-forward stakes (e.g. the lord's-man's record entry persists)
    - episode.chunk
    - interval-delta                        # time-gap or locale-shift between prior-terminal and this-open
  set-off:
    style: italic
    separator: rule
  forbidden-content:
    - plot-content-not-in-graph
    - character-card-paraphrase
    - explicit-author-meta
---

# and-shoot project-default stitch profile

This is the project-default profile. Every episode in the and-shoot project inherits
it unless overridden by an episode-level profile (`active-project/theater/stitch-profile.md`)
or per-scene profile (`active-project/theater/stitch-profile-<scene-label>.md`).

The persona is `worm-tight` — terse, body-first, observational. The project-scoped
fences (anti-jargon, hollow-prose-patterns, asinine-patterns, bone-faithfulness-fence)
accumulate failure modes observed in real runs. Phase 1 fork prompts must surface
these lists; Phase 7 Q5/Q8/Q9 reference them.

**Why this profile exists:** the s01e01 first run used `neutral` persona and
hand-waved Phase 7, producing prose dense with invented compounds and hollow-prose
patterns. The worm-tight re-run cut/reworded them. To prevent recurrence, the
project default now (a) pins persona=worm-tight, (b) enumerates the observed
anti-patterns so every fork sees them, (c) declares the bone-faithfulness fence
explicitly so subagents can refuse invented prose at Phase 1 rather than letting
Phase 7 clean up after.

When a new pattern emerges in future episodes' feedback files, promote it here
via `staff/stitcher/tuning-guide.md § Promotion`.
