# Stitcher Tuning Guide

How to read stitcher output, identify what needs to change, and route feedback into the right knob.

Status: **draft (tuning)** — this guide will accumulate worked examples as tuning proceeds.

---

## The tuning loop

```
1.  /and-stitch <episode-slug>
        produces polish/<slug>.md (clean), polish/<slug>.annotated.md (with traces),
        and staff/stitcher/render-log-<slug>.md

2.  Read polish/<slug>.md
        if it reads right end-to-end, done

3.  When a line reads wrong, open polish/<slug>.annotated.md
        find the [L<N>] you want to fix
        read its <trace> block

4.  Identify the knob
        the trace tells you what decision produced this line

5.  Write feedback
        edit staff/stitcher/feedback-<slug>.md
        line-level for one-shot fixes, pattern-level for promotion candidates

6.  Re-stitch
        /and-stitch <episode-slug>
        the stitcher reads the feedback, patches the active profile and persona,
        re-runs only the affected forks + downstream phases

7.  Repeat from step 2 until the polish file is clean
```

The annotated file is the tuning surface. The clean file is what ships.

---

## Reading the annotated file

Each prose sentence is prefixed with a stable line-ID and followed by a `<trace>` block:

```
[L25] Her hands stilled on the apron-front, her gaze held my face.
<trace>
  source: @43 feel:8
  tens: 3
  lenses-firing: narrator:12, feel:8, sensory:3 (tag=drop)
  lens-decider:
    rule-3-peak-feel: candidate
    rule-6-persona-override: FIRES (worm-tight)
  lens-leads: feel
  phase-history:
    P1 fork-043 render-cite feel:8 (lead position)
    P4 pov-pronoun-resolve "the hands" -> "her hands"
    P4 tense-shift past
</trace>
```

The trace records:
- `source:` — which proto-line bone and/or facets produced this sentence
- `tens:` — tension scalar at the source anchor
- `lenses-firing:` — which facets fired at this anchor
- `lens-decider:` — which lens-leading rule fired (Phase 1 only)
- `phase-history:` — every phase that touched this line and what it did

If the line reads wrong, the trace tells you which decision to revisit.

---

## Common feedback patterns

### "Too cognitive / writerly / abstract"

Symptom: the line names interpretation rather than showing event.
Trace pattern: `lens-leads: narrator` at a low-tens anchor.
Knob: persona's lens biases — shift NI-priority down at this tens level. Or strict-Q1 — under strict, most NI cuts as not-load-bearing.

Feedback example:
```
[L23] too cognitive — Taylor's interior commentary on the eye-hold reads as
              authorial. cut or pull body-only.
```

### "Body anchor is missing"

Symptom: a peak landed without showing the character's body.
Trace pattern: `facets-rendered:` doesn't list a feel cite at a tens=3.
Knob: profile's `peak-priority` — raise feel; or persona's lens-bias for that anchor.

Feedback example:
```
[L26] body anchor missing — feel:8 should have led here.
              the song-drop without the mother's stillness reads as arbitrary.
```

### "Reads asinine"

Symptom: a line states something obvious or vacuous as if meaningful.
Trace pattern: Q8=NO recorded (the line didn't trigger the asinine check).
Knob: persona's Q8 aggressiveness, or pattern-level feedback identifying the structural form.

Feedback example:
```
[L21] asinine — "the spiders didn't know it" is non-sentient negation
              dressed as contrast. cut tail, or RESHOW via passive-sense network.

PATTERN: NI two-clause structures with non-sentient negation tail
DETAIL: "[sentient subject] [knew/has X]; [non-sentient subject] [didn't know/has not Y]"
SCOPE: worm-tight
SEEN-AT: [L21]
PROPOSED-RULE: Q8 fires automatically; cut tail at semicolon, or RESHOW with
               network-vibration register.
```

### "Word reads as jargon"

Symptom: invented compound or technical-sounding nominalization.
Trace pattern: Q9=NO recorded.
Knob: persona's Q9 aggressiveness, or REWORD vocabulary policy.

Feedback example:
```
[L24] "eye-hold" reads as invented compound. REWORD to "look between us"
              or cut the clause entirely.
```

### "Sentence doesn't earn its place"

Symptom: removing the sentence wouldn't affect understanding.
Trace pattern: Q1=YES recorded (line passed strict Q1) but you disagree.
Knob: Q1 calibration. Either the persona is wrong, or this specific anchor needs an override.

Feedback example:
```
[L19] this doesn't carry meaning the audience needs. CUT.

(or if a pattern)
PATTERN: bone-only mid-scene action that has no facet anchor and no plot consequence
SCOPE: worm-tight
SEEN-AT: [L19]
PROPOSED-RULE: zero-cite bones at tens=1 outside protected patterns should
               merge with adjacent bone or drop.
```

### "Three notes in a row reads stilted"

Symptom: a protected pattern (countdown, three-beat) renders mechanically.
Trace pattern: `P6 pattern-ok` confirming the buildup was protected.
Knob: either remove the pattern from `protected-patterns`, or accept the cost. Under strict-Q + bones-cuttable, the buildup collapses when its anchor cuts.

Feedback example:
```
[L21..L22] three-note buildup reads stilted with no anchor justifying it.
                  NI:12 was cut already at L27. apply bones-cuttable-anchor-cut.
```

### "I want more first-person interior"

Symptom: the prose feels third-person-distant despite FPP being on.
Trace pattern: Taylor's "I" lands only where Taylor physically acts; observation phrasings don't surface POV.
Knob: this is a source-material limit. The bones describe events; Taylor's "I" surfaces only on her own action bones. Two adjustments:
1. Source-pipeline: add Taylor-acting bones to scenes that need more first-person presence
2. Stitcher: cannot invent. Phase 4 can't add "I watched" because perception verbs are forbidden in bones and facets

Phase 4 voice-transform's job is restricted to pronoun/tense shift, not narrator-presence amplification.

---

## Anatomy of a knob — finding where to make a change

Each tunable behavior lives in exactly one place. The tree:

```
profile (theater/stitch-profile.md)
├── voice: {tense, person, pov, contractions}
├── render: {facet-types, cap-per-anchor, peak-priority, nonpeak-priority}
├── phase-1: {lens-decider rules, foreknowledge-language, continuity-context}
├── redundancy: {detector, echo-window, preserve-anchor}
├── compression: {merge rules, pronoun-substitution, tens1-run-collapse}
├── voice-transform: {bone-object-policy, third-party-preserve, sensory-arrow-rendering}
├── local-flow: {window, deferral caps, temporal-lock-words}
├── protected-patterns: [...]
├── phase-7: {cut-aggressiveness, reshow-enabled, reword-enabled, bones-cuttable}
├── output: {mode, line-ids, trace-verbosity}
├── feedback: {feedback-file, re-stitch-scope}
└── scene-overrides: {scene-c: {...}, scene-l: {...}}

persona (staff/stitcher/personas/<slug>.md)
├── Lens biases (overrides for lens decider rules 1-5)
├── Phase 7 biases (Q-aggressiveness per question)
├── Bones-cuttable bias
├── RESHOW bias
├── REWORD bias
└── Tuning notes (accumulated from promoted pattern-level feedback)

feedback (staff/stitcher/feedback-<slug>.md)
├── Line-level entries (one-shot patches)
├── Pattern-level entries (promotion candidates)
└── Promoted entries (resolved into persona)
```

### Where to put your tweak

| Want to change | Edit |
|---|---|
| Tense / person / POV / contractions | profile.voice |
| Which facet types render at all | profile.render.facet-types |
| Whether sensory deltas drop when bone covers | profile.voice-transform.sensory-arrow-rendering |
| How aggressively bones merge | profile.compression |
| Whether Q1 treats borderline as cut | profile.phase-7.cut-aggressiveness |
| Whether bones can cut at Phase 7 | profile.phase-7.bones-cuttable |
| Lens hierarchy at a specific anchor type | persona.lens-biases |
| Q-answer aggressiveness | persona.phase-7-biases |
| One-shot fix for L23 | feedback line-level |
| Project-recurring rule | feedback pattern-level → promote → persona.tuning-notes |

---

## Promotion: pattern-level → persona

Pattern-level feedback is advisory until promoted. Promotion process:

1. Review the PATTERN entry in `feedback-<slug>.md`
2. Verify the rule is stable (seen across multiple lines or multiple episodes)
3. Append the rule to the named persona's `## Tuning notes`
4. Mark the feedback entry as PROMOTED with date
5. Future stitcher dispatches read the persona; the rule is applied automatically

Promotion is intentional. Auto-promotion would let pattern-level feedback drift the persona uncontrolled. The bias surface is documented and reviewable.

---

## Common knob settings for new projects

### Worm-canon-anchored (Taylor POV, terse register)

```yaml
persona: worm-tight
voice: {tense: past, person: first, pov: <taylor-slug>}
voice-transform:
  bone-object-policy: idiom-fit
  sensory-arrow-rendering: drop-if-covered
phase-7:
  cut-aggressiveness: strict
  bones-cuttable: anchor-cut-only
  borderline-policy: reject
```

### Lush / literary (more interior surface, longer prose)

```yaml
persona: neutral
voice: {tense: past, person: third}
voice-transform:
  bone-object-policy: verbatim
  sensory-arrow-rendering: prose-template
phase-7:
  cut-aggressiveness: permissive
  bones-cuttable: never
  borderline-policy: keep
```

### Cinematic (sensory-led, visual register)

```yaml
persona: <project-specific>     # author from neutral; lens-bias: sensory leads at most anchors
voice: {tense: past, person: third}
voice-transform:
  sensory-arrow-rendering: prose-template
phase-7:
  cut-aggressiveness: standard
protected-patterns: [...all visual buildups...]
```

These are starting points; tune from there with feedback.

---

## What this guide does not cover

- Auditor's review of the render-log. The auditor agent has its own protocol; see `staff/auditor/card.md`.
- Editor's pass on the clean polish file. Editor runs at `/and-wrap` after stitch; sees only the clean file plus auditor findings.
- Source-pipeline tuning (proto-lines and facets). Stitcher tunes how facets render; if the facets themselves are wrong, that's `/and-protolines` / `/and-facets` territory.
- Performance optimization. The stitcher's parallelism is controlled at `phase-1.parallel`; full performance tuning is beyond this guide.
