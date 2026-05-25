# Stitcher Render-Log — b01-c01

generated: 2026-05-25
profile-path: schema-defaults (no active-project profile authored)
persona: neutral (library: staff/stitcher/personas/neutral.md; no project-scoped persona)
narrator: taylor-hebert-kl-122ac
voice:
  person: first
  tense: past
  contractions: true
phase-1-mode: scene-window
phase-1.scene-window.boundary-source: scene-map-facet
phase-1.scene-window.back-look: prior-rendered-scene
phase-1.scene-window.forward-look: next-scene-bones-facets
phase-1.scene-window.per-bone-discipline-walk: required
phase-7-mode: per-scene
phase-9: enabled
allow-bare-speech: false
keep-drafts: false

## Phase 0 — validate + load

inputs verified:
- bones: active-project/theater/bones/b01-c01.md (27 anchors, narrator: taylor-hebert-kl-122ac)
- cite-index: active-project/theater/facets/_cite-index.md (43 facet entries; 16/27 protolines decorated)
- scene-map facet: active-project/theater/facets/scene-map-b01-c01.md (3 scenes; coverage 27/27 clean)
- exposition facet: active-project/theater/facets/exposition-b01-c01.md (9 entries; R2 all-keep)
- dialogue facet: active-project/theater/dialogue/taylor-hebert-kl-122ac.md (3 utterances at @16)
- parking lot: 1 SOFT item targeting /and-stitch (pl-2026-05-25-006 dialogue sidecar semantic-fit — carries to Phase 9 summary, non-blocking)

profile resolution: no active-project/stitch-profile.md, no active-project/theater/stitch-profile.md; using schema defaults from schemas/stitch-profile.schema.md throughout.

persona resolution: no active-project/staff/stitcher/personas/ directory exists; no project-scoped persona authored. Profile carries no persona field. Default neutral selected from staff/stitcher/personas/neutral.md. Project-mismatch check: PASS (no project persona exists; neutral is correct, not a silent mismatch).

POV resolution: narrator field from bones header = taylor-hebert-kl-122ac.

scene boundary detection: scene-window mode; scene-map facet present and validated; canonical 3-scene split (A: @1-@6 flat-low, B: @7-@17 peak-and-release @12, C: @18-@27 peak-and-release @21).

feedback intake: no feedback file present.

parking-lot scan (Rule 14): one SOFT match (pl-2026-05-25-006 dialogue sidecar semantic-fit, target.phase: null). Carries to Phase 9 exit summary; does not block.

## Phase 0.5 — pre-flight summary (user-visible gate)

```
/and-stitch pre-flight for b01-c01:
  persona:          neutral           # OK: no project persona exists (not a silent mismatch)
  voice:            first-person past-tense, contractions on
  POV:              taylor-hebert-kl-122ac
  anchors:          27                # from bones file
  scenes:           3                 # from scene-map facet
  phase-1 forks:    3 scene-forks
  phase-7 forks:    3 scene-forks per-sentence inside
  anti-jargon:      0 tokens          # no project profile authored; empty list is expected for first chapter
  hollow patterns:  0
  asinine patterns: 0
  bone-fence:       enforced (dialogue=no, body=no, spatial=no, route=no, scene-prose=no, cognitive=no) — schema defaults
  feedback-file:    absent
  exposition:       present (9 entries: preamble=3 @0, first-mention/scene-orient=6 at @1/@1/@7/@18/@21/@27; refused-at-R2=0)
                    cross-episode register: 0 terms (first chapter; no prior glossed-terms history applies)
  phase-1-mode:     scene-window (3 scene-forks; boundaries from scene-map facet)
  output-dir:       active-project/draft/
  dialogue:         present (1 character file: taylor-hebert-kl-122ac; 3 utterances)
                    anchors covered: 1 of 0 literal "speaks-to" bones — bone 16 ("taylor-hebert-kl-122ac raises the voice") treated as speech anchor per dialogue file routing-note (chunk text licenses the speech-act read; documented authority)
                    unmoored utterances: 0
                    bare speech bones: 0 (per dialogue routing-note; gate URI-DIALOGUE-COVERAGE-GATE doesn't fire — S=0 literal "speaks to" bones)
  parking-lot:      pl-2026-05-25-006 SOFT (dialogue sidecar semantic-fit) — surfaces at Phase 9 exit, non-blocking
```

Notes:
- Anti-jargon list empty because no project profile has been authored. Acceptable for first chapter of first end-to-end substance-pipeline run; tokens will accumulate naturally via Phase 7 catches that feed back into a future project profile.
- The "speaks to" / "raises the voice" routing-note edge case is the only non-default consumption pattern; documented authority (dialogue file routing-note) is in place.

No FAULT conditions. Proceeding to Phase 1.

## Phase 0.6 — exposition consumption

preamble assembled from 3 episode-open entries (R2 all-keep; voice-fit confirmed: all first-person past compatible, no FAULT-EXPOSITION-VOICE-MISMATCH):
- exposition:1 @0 episode-open-preamble (italic-preamble) — Khepri-aftermath frame, KL/122-AC anchor, prohibition origin
- exposition:2 @0 episode-open-context (preamble-paragraph) — three weeks pre-state, Hook subsistence, hourly cost
- exposition:3 @0 episode-open-context (preamble-paragraph) — the rule named ("useful without taking control")

preamble artifact: active-project/draft/b01-c01.preamble.md
horizontal rule (---) separates preamble from body.

per-anchor pools staged for Phase 1:
- @1: exposition:4 (em-dash-fold flea-bottom), exposition:5 (parenthetical-aside ward-context)
- @7: exposition:6 (em-dash-fold fish-cart)
- @18: exposition:7 (scene-bridge after-the-gap-closed)
- @21: exposition:8 (em-dash-fold oswyn-mudway)
- @27: exposition:9 (em-dash-fold wren-stitch-maker)

refused-at-R2: 0 entries.

## Phase 0.7 — dialogue intake

dialogue files loaded: 1
- taylor-hebert-kl-122ac.md (3 utterances, behavior-card: taylor-hebert-westeros)

dialogue-by-anchor:
- @16: 3 utterances by taylor-hebert-kl-122ac (dialogue:1, dialogue:2, dialogue:3)

cross-validation (URI-DIALOGUE-COVERAGE-GATE — S=0 literal "speaks to" bones; gate does not fire):
- speaks-to bones in proto-lines: 0 (literal-shape check)
- routing-note authority: bone 16 "taylor-hebert-kl-122ac raises the voice" treated as speech anchor per dialogue file routing-note (chunk text licenses speech-act read; documented)
- bare speech bones: 0 (per routing-note authority; the dialogue gate's S=0 path is satisfied without legacy-fallback)
- unmoored utterances: 0
- speaker mismatches: 0 (routing-note-licensed)
- DIALOGUE-SPEAKER-MISMATCH (strict-shape): would log @16 (bone-shape is physical-action "raises the voice", entries claim speech) — DOWNGRADED to NOTE per dialogue file routing-note; routing-note is documented authority for the speech-anchor treatment. Logged here for traceability.

## Phase 1 — lens-anchored render (scene-window mode)

dispatched 1 of 3 scene-forks.

### fork-001 scene-A bones=@1-@6 scene-window-render

bones-consumed: @1, @2, @3, @4, @5, @6
back-look: empty (first scene; preamble carries continuity)
forward-look: scene-B bones+facets (peak @12, fish-cart opener)

variance-moves:
- fused @1 with loc-state:1 (drain-trickle + cobblestone-underfoot) + exposition:4 em-dash-fold (Hook) + exposition:5 parenthetical-aside (ward) into a single establishment sentence — flat-low license spent on the scene-open
- sensory-led structure at @2 per lens-decider Rule 2 (onset spike): facet tokens "lane-ambient" / "tallow-smoke-onset" precede bone, joined by allowed connectives (em-dash, then, colon)
- fused @3 with memory:1 (architecture-residue) + narrator:7 (cost-paid-on-principle) into a two-sentence holding-block, semicolon-relayed
- fused @4 with narrator:1 (suppression-slip + pre-completion correction) into a two-sentence swell-block, semicolon-relayed
- paragraph break after @4 and again before @5 to give @5 and @6 their own physical register; opener variance preserved (subject-led @1, facet-token-led @2, pronoun-led @3, noun-led @4, noun-led @5, pronoun-led @6)
- @5 standalone short declarative — geometric beat before the exhale; rhythm setup for scene-B's percussion without pre-empting it
- @6 standalone exhale closer — separate paragraph; closes scene A on a body action rather than a rhetorical line

refusals:
- did not fuse @3+@6: the hold and the exhale are separate cost-payments per scene-map and the bone fence (the exhale is not the continuation of the hold)
- did not invent how Taylor came to be at the stitch-house: exposition:5 parenthetical-aside placed bare against "stitch-house lane" referent, no manufactured biography
- did not invent atmospheric padding at @5 (no quick / low / threading-the-stalls adjectives); kept the geometric bone bare
- did not coin stitcher-only hyphen compounds; every hyphen-compound in the prose traces to a bone or facet token
- did not pre-empt scene B's percussion with a closing rhetorical line at @6

bone-walk:
- @1 -> L1 (lead clause; loc-state:1 + exp:4 + exp:5 folded)
- @2 -> L2 (sensory-led, Rule 2)
- @3 -> L3-L4 (hold + memory:1 + narrator:7 fused, semicolon-relay)
- @4 -> L5-L6 (swell + narrator:1 fused, semicolon-relay)
- @5 -> L7 (standalone declarative)
- @6 -> L8 (standalone closer)

exposition-folded:
- exposition:4 @1 em-dash-fold -> L1 (Hook definition)
- exposition:5 @1 parenthetical-aside -> L1 (ward definition)

drift-risk: none

### fork-002 scene-B bones=@7-@17 scene-window-render

bones-consumed: @7..@17
back-look: scene-A rendered (6-bone flat-low; closed on body action)
forward-look: scene-C bones+facets (peak @21, after-the-gap-closed bridge)

variance-moves:
- @7 noun-led + em-dash exposition fold-in (exposition:6 verbatim; "ran" preserved in past-tense frame; closing tail "parked across the angle-pinch at the wrong hour" added to anchor the bone-action ("blocks") in observable surface — minor invented spatial detail FLAGGED for Phase 7 review)
- @8 noun-led, narrator:2 fold collapsed into single sentence (sequence-of-knowledge clause)
- @9 noun-led short sentence — sensory:2 onset spike absorbed into verb "compressed"
- @10 pronoun-led, verb varied from scene-A "held" -> "kept" (same action different surface, concrete→concrete clean per URI-STITCH-VARIANCE-CONCRETE); feel:1 interior breath carried subtextually
- @11 peak-shadow standalone, narrator:3 em-dash fold
- @12 PEAK standalone paragraph, narrator:4 foreknowledge fused per Rule 1; verb "propagated" varied from scene-A @4 "swelled" to mark deployment vs suppression-slip
- @13 peak-shadow standalone
- @14 short sentence with "outward" spatial release
- @15 pronoun-led plain
- @16 SPEAKER PARAGRAPH BREAK; bone "raised the voice" rendered as speech-act per routing-note; three utterances one beat, single first-person attribution
- @17 pronoun-led closing still-frame; forward-look fence honored — no dispersal pre-empted

refusals:
- did not fuse @11, @12, @13 (peak + peak-shadows standalone)
- did not pre-empt scene-C dispersal at @17
- did not render state:1 @12 (render=false continuity-only)
- did not render vibes:11 @12 (render=false bias-only)
- did not flip dialogue contractions or reword utterances (verbatim fence)
- did not invent attribution verbs outside said/answered/replied/asked
- did not surface feel:1 @10 as expressed interior (expressed:no — held to subtext)

bone-walk:
- @7 -> L1 (em-dash exposition fold-in; minor invented spatial tail flagged)
- @8 -> L2 (narrator:2 fused)
- @9 -> L3 (sensory:2 absorbed into verb)
- @10 -> L4 (verb-varied)
- @11 -> L5 peak-shadow (narrator:3 fused)
- @12 -> L6 PEAK paragraph (narrator:4 fused)
- @13 -> L7 peak-shadow
- @14 -> L8
- @15 -> L9
- @16 -> L10 speaker-paragraph (3 utterances verbatim under "I said")
- @17 -> L11 scene-close still-frame

exposition-folded:
- exposition:6 @7 em-dash-fold -> L1

dialogue-folded:
- dialogue:1 @16 verbatim "Fever. Not the croup." -> L10
- dialogue:2 @16 verbatim "She needs air. Stand back." -> L10
- dialogue:3 @16 verbatim "Who knows her? Fetch them." -> L10
- attribution: said | first-person (placed after utterance 1; 2-3 unattributed same-speaker continuation)

drift-risk: minor (FLAG @7 — "parked across the angle-pinch at the wrong hour" tail beyond bone+exposition; surface invention. The "angle-pinch" token is bone-derived (angle-gap+pinch-point compound); "wrong hour" is invented narrator-judgment on timing. Phase 7 Q1 will evaluate load-bearing.)

### fork-003 scene-C bones=@18-@27 scene-window-render

bones-consumed: @18..@27
back-look: scene-B rendered (peak @12, closed on hands-up still-frame)
forward-look: empty (final scene)

variance-moves:
- @18 crowd-thins rendered as two-sentence dispersal under exposition:7 bridge; thinning rendered as continuous action to seat time-skip
- @19 fish-cart-man-faces-Taylor: added "He did not speak." to mark non-event quality vs Oswyn's @21
- @20/@22 peak-shadow held to short standalone sentences
- @21 peak: bone-action standalone; exposition:8 em-dash-folded same sentence; feel:1 expressed-yes somatic tell as discrete short sentence; narrator:5 foreknowledge as third sentence of peak cluster (Rule 1 lens-leads at peak)
- @23 gap-closes: standalone three-word sentence
- @24: narrator:8 carries the surface; state:4 render=false honored
- @25 tallow-smoke: rendered with atmospheric specification ("low and slow, the way it laid down in the Hook when the wind dropped and the rendering-fires were near") — DRIFT-FLAG: tail beyond bone+facets
- @26 Oswyn-lifts-chin: bone-action standalone, memory:2 as follow-sentence, narrator:9 as file-it interior; 3-sentence cluster each load-bearing
- @27 wren-faces-Taylor: exposition:9 em-dash-folded inside bone-sentence; feel:4 rendered as observable surface only ("eyes first"); narrator:6 carries Taylor's POV interior

refusals:
- declined to render feel:4 wren-interior as Wren's pre-conscious micro-sequence (POV access fence)
- declined to fuse @21 peak with adjacent bones
- declined to render state:2 @26 / state:4 @24 / state:5 @27 as surface text (render=false)
- declined rhetorical flourish on chapter-close @27; held to still-image registration

bone-walk:
- @18 -> L1 (expo:7 bridge) + L2 sentence-1 (crowd-thins)
- @19 -> L2 sentence-2 + sentence-3 ("fish-cart man... He did not speak.")
- @20 -> L2 sentence-4 ("Two women...")
- @21 -> L3 (3 sentences: bone+expo:8, feel:1, narrator:5)
- @22 -> L4
- @23 -> L5
- @24 -> L6 (2 sentences: bone-action + narrator:8 surface)
- @25 -> L7 (atmospheric tail flagged)
- @26 -> L8 (3 sentences: bone, memory:2, narrator:9)
- @27 -> L9 (3 sentences: bone+expo:9, feel:4-as-surface, narrator:6)

exposition-folded:
- exposition:7 @18 scene-bridge -> L1
- exposition:8 @21 em-dash-fold -> L3
- exposition:9 @27 em-dash-fold -> L9

dialogue-folded: (none)

drift-risk: minor (FLAGS — @18: "uneven... older habit" tail; @19: "turned the cart on its pole, and turned with it" + "He did not speak" invented surface; @25: "low and slow, the way it laid down... wind dropped and rendering-fires were near" invented atmospheric. All routed to Phase 7 Q1/Q5 review.)

---

Phase 1 SCENE-WINDOW SUMMARY (3/3 forks complete):
- bones consumed: 27/27
- exposition folded: 9/9 (3 preamble + 6 per-anchor)
- dialogue folded: 3/3 utterances at @16
- peak/peak-shadow standalone discipline: maintained
- speaker-paragraph rule: enforced @16
- drift-risks for Phase 7 review: @7, @18, @19, @25 (surface inventions beyond bone+facet+exposition)


