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

## Phase 2 — redundancy cull

scope: per-anchor decisions across multi-cite anchors + echo window=1 detection across adjacent paragraphs.

multi-cite anchor inventory (anchors with 2+ facets rendered in body prose):
- @1 (loc-state:1 + exposition:4 + exposition:5): single fused sentence; no closing-phrase echo with neighbor (@2 is sensory-arrow facet-led). KEEP-OVER-ECHO.
- @3 (bone + memory:1 + narrator:7): two-sentence holding-block, semicolon-relayed; closing phrase "every morning" — no overlap with @4's "the count completed". KEEP-OVER-ECHO.
- @4 (bone + narrator:1): two-sentence swell-block; closing phrase "before the count completed" — no overlap with adjacent @5 ("narrowed the lane") or @3 ("every morning"). KEEP-OVER-ECHO.
- @8 (bone + narrator:2): single-sentence sequence-of-knowledge collapse; image-set: ground/child/breath/crowd; @9 "crowd compressed" shares "crowd" token but compression is a different image-set (mass-action vs awareness-precedence). KEEP-OVER-ECHO.
- @11 (bone + narrator:3): em-dash-fold "the dozen I'd need, and the second dozen I wouldn't"; closing-phrase "I wouldn't" — no overlap with @12's "wouldn't name" at sentence-level rhythm but both end on negation-clause. Echo window=1 check: distinct image-sets (crowd-arithmetic vs naming-refusal); preserve narrator per redundancy.preserve-anchor default. KEEP-OVER-ECHO.
- @12 (bone + narrator:4): peak; "the telling was a thing I wouldn't name" foreknowledge-clamped (narrator:4 leads per Rule 1). Standalone paragraph; no echo-window neighbor competition. KEEP-OVER-ECHO.
- @16 (bone + dialogue:1/2/3): speaker-paragraph; 3 verbatim utterances under single "I said" attribution. Dialogue not subject to echo-cull. KEEP-OVER-ECHO.
- @18 (bone + exposition:7 bridge): single "After the gap closed" bridge into "the crowd came apart the way Flea Bottom crowds did"; no closing-phrase echo with @19's "He did not speak." KEEP-OVER-ECHO.
- @21 (bone + exposition:8 + feel:1 + narrator:5): 3-sentence peak cluster; exposition:8 em-dash-folded in same sentence as bone; feel:1 ("His hands settled at his apron-front") is somatic surface; narrator:5 ("a week before he would have the word for it") is foreknowledge. Image-sets distinct (street-tenure / somatic-tell / foreknowledge). KEEP-OVER-ECHO.
- @24 (bone + narrator:8): two-sentence cluster; "I faced the alley-mouth. I set my body to it..." — narrator:8 surface continuation without image-overlap to @25 atmosphere. KEEP-OVER-ECHO.
- @26 (bone + memory:2 + narrator:9): 3-sentence cluster (bone-action / memory:2 country's-older-stories / narrator:9 filed-in-category-he-recognized). Distinct image-sets across all three. KEEP-OVER-ECHO.
- @27 (bone + exposition:9 + feel:4-as-surface + narrator:6): chapter-close 3-sentence cluster (Phase 6 protected). Distinct image-sets (exposition gloss / observable somatic / interior file). KEEP-OVER-ECHO.

echo window=1 cross-paragraph scan: no DROP-ECHO or DROP-IMAGE-OVERLAP triggered. Scene-window mode landed clean as predicted.

cull outcome: 0 facets dropped; 12 KEEP-OVER-ECHO logged.

## Phase 3 — compression

merge-candidate scan:

- P1 @1: standalone establishment paragraph; no merge candidate.
- P2 @2: facet-led sensory arrow; cannot merge (different subject from @1, scene-A-opener).
- P3 @3: two-sentence hold-block (bone + memory:1 + narrator:7 fused); same-subject ("I"/"the feet") within paragraph; SUBSTITUTE-PRONOUN already applied at fork time ("the holding cost a quarter of me" — sentence-2 carries the action-noun forward, no re-introduction of "the feet"). NO-MERGE further (semicolon-relay already at minimum compression).
- P4 @4: two-sentence swell-block (bone + narrator:1); same-subject ("the swell"/"I'd"); semicolon-relay already minimum. NO-MERGE.
- P5 @5: standalone geometric beat; scene-A flat-low setup. NO-MERGE (peak-rhythm-protected setup; merging into @4 or @6 would collapse the scene-A rhythm).
- P6 @6: standalone exhale closer; scene-A close. NO-MERGE pattern-protected (scene-A closes on body action).
- P7 @7: scene-B opener with em-dash exposition fold-in; standalone. NO-MERGE (scene-boundary).
- P8 @8: standalone; ground-transmission single sentence. NO-MERGE (image-set distinct from @7 and @9).
- P9 @9: standalone short sensory-spike. NO-MERGE pattern-protected (peak-shadow @11 awaits; scene-B rhythm-build).
- P10 @10: standalone "I kept the feet" pronoun-led. NO-MERGE (verb-varied callback to @3; merging into @9 would collapse the breath-hold register).
- P11 @11: peak-shadow standalone with narrator:3 em-dash-fold. NO-MERGE pattern-protected (peak-shadow standalone discipline).
- P12 @12: PEAK standalone paragraph. NO-MERGE pattern-protected (peak standalone HARD).
- P13 @13: peak-shadow standalone. NO-MERGE pattern-protected.
- P14 @14: short "outward" release. NO-MERGE (cross-bone temporal; @13→@14 is the gap-propagation arc that needs the visible step).
- P15 @15: pronoun-led short. NO-MERGE (turn-toward beat; speaker-paragraph @16 follows).
- P16 @16: bone-as-speech-act standalone; SPEAKER-PARAGRAPH-BREAK HARD. NO-MERGE.
- P17 dialogue paragraph: 3 utterances + attribution. NO-MERGE (speaker-paragraph rule; verbatim).
- P18 @17: "I lifted my hands" standalone closing still-frame. NO-MERGE pattern-protected (scene-B close on still-frame; forward-look fence honored).
- P19 @18: scene-bridge "After the gap closed, the crowd came apart the way Flea Bottom crowds did." Single sentence. NO-MERGE (scene-bridge; scene-C opener).
- P20 @18+@19+@20: four-sentence dispersal block ("The thinning went uneven... He did not speak. Two women..."). Multiple subjects (thinning / fish-cart-man / two-women); SUBSTITUTE-PRONOUN applied (fish-cart-man→He after first mention). MERGE-SAME-SUBJECT not applied across subjects; the existing paragraph groups the dispersal cluster by spatial register (one paragraph), which is the right granularity. NO-MERGE further.
- P21 @21: 3-sentence peak cluster. NO-MERGE pattern-protected (peak standalone). Repeated subjects within paragraph: "Oswyn Mudway" → "the Mudway man" (em-dash apposition, exposition:8) → "His hands" → "The elder" — SUBSTITUTE-PRONOUN partially applied at fork time; "The elder" in sentence-3 is exposition:8's term-of-art (canonical re-introduction), not a redundant repeat. NO-MERGE further.
- P22 @22: "The child cleared the lane." standalone. NO-MERGE pattern-protected (peak-shadow standalone).
- P23 @23: "The gap closed." three-word standalone. NO-MERGE pattern-protected.
- P24 @24: two-sentence cluster (bone + narrator:8 surface). Same-subject ("I"). NO-MERGE (already minimum; narrator:8 is the registration-refusal surface, semantically distinct second sentence).
- P25 @25: atmospheric tallow-smoke standalone. NO-MERGE (atmospheric specification; image-set distinct from @24 and @26).
- P26 @26: 3-sentence Oswyn-chin-lift cluster. Same-subject across all three (Oswyn / the chin / The chin-lift). SUBSTITUTE-PRONOUN: sentence-2 uses "The chin lifted" (canonical bone-noun re-introduction for the rhetorical mirror, not a redundant repeat); sentence-3 uses "The chin-lift" (compound noun shift, narrator:9 surface). NO-MERGE pattern-protected (3-sentence buildup-candidate; flagged for Phase 6).
- P27 @27: chapter-close 3-sentence cluster (Phase 6 PROTECTED HARD). NO-MERGE pattern-protected.

zero-cite bone runs: no qualifying COLLAPSE-FLAT-LOW-RUN (scene-A flat-low has @5/@6 zero-cite but they are scene-rhythm-protected; scene-B/C have no flat-low runs).

exit trios: no MERGE-EXIT-TRIO candidates (no triple exit at scene-close).

compression outcome: 0 merges applied; 4 SUBSTITUTE-PRONOUN already-applied (at @3, @20, @21, @26); 27 NO-MERGE pattern-protected or no-candidate.

## Phase 4 — voice transform

walk per paragraph:

- P1 @1 (drain-water establishment): TENSE-CONFIRM past ("threaded"). PERSON-CONFIRM third-person observational (drain-water as subject). PRESERVE-THIRD-PARTY: "Flea Bottom" / "King's Landing" / "the Hook" — all preserved on first mention; subsequent references will pronominalize where idiomatic (none in this paragraph). BONE-OBJECT-IDIOM-FIT: bone-shape "threads the angle-gap" rendered "threaded the angle-gap of the stitch-house lane" — preposition "of the stitch-house lane" idiom-fit-allowed per bone-object-policy (the lane is the scene's location-state, not invention). EXPOSITION VERBATIM modulo voice: exposition:4 "the lane-warren of Flea Bottom..." past-tense compatible (states a present-tense definition; voice-fit at Phase 0.6 confirmed no FAULT-EXPOSITION-VOICE-MISMATCH). CONTRACTION: none required this paragraph.
- P2 @2 (sensory-arrow): SENSORY-PROSE-FIT confirmed — "Lane-ambient — then tallow-smoke-onset: the smoke crossed the stitch-house lane." Facet tokens "lane-ambient" / "tallow-smoke-onset" preserved as compounds (no rephrasing); connectives "— then" / ":" are schema-allowed; bone-verb "crossed" past. TENSE-CONFIRM past.
- P3 @3 (hold-block): TENSE-CONFIRM past ("held" / "had brought" / "did" / "cost" / "paid"). PERSON-CONFIRM first ("I held" / "I'd brought" / "I paid"). POV-PRONOUN-RESOLVE: "the feet" → bone uses canonical "the feet"; first-person owns the feet but the bone's noun is preserved as the body-part-as-discipline figure (narrator:7 frames it that way: "discipline I'd brought"); NO RESOLVE applied here — "the feet" is the figure-of-speech subject, not a body-part owned-by-me reference. CONTRACTION confirmed: "I'd" (had).
- P4 @4 (swell-block): TENSE-CONFIRM past ("swelled" / "was" / "I'd pulled"). PERSON-CONFIRM first ("I'd pulled it back"). CONTRACTION: "I'd" fired.
- P5 @5 (angle-wall): TENSE-CONFIRM past ("narrowed"). PERSON: third-person observational. BONE-OBJECT-IDIOM-FIT: bare; no preposition added.
- P6 @6 (exhale): TENSE-CONFIRM past ("exhaled"). PERSON-CONFIRM first.
- P7 @7 (fish-cart): TENSE-CONFIRM past ("blocked" / "ran" / "parked"). PERSON: third-person observational. EXPOSITION VERBATIM modulo voice: exposition:6 "the morning fish-trade ran through the Hook from the river-side gate" past compatible. PRESERVE-THIRD-PARTY: "the Hook" preserved.
- P8 @8 (ground-transmits): TENSE-CONFIRM past ("carried" / "registered"). BONE-OBJECT: bone "transmits the child's breath" rendered "carried the child's breath" — REWORD-equivalent? No, "carried" is a Phase 4 voice substitute that preserves the bone-verb's semantic content within the kinetic register; NOT a Phase 7 REWORD. Hold — checking: bone-verb is "transmits"; "carried" is a synonym substitution. This is borderline Phase 4 vs Phase 7. The Phase 1 fork (fork-002) selected "carried" at render-time within the kinetic frame; treat as PRESERVED-AT-PHASE-1 (the fork's lens-anchored render produced this surface as the bone-verb's voice-fit form). NOTE for future audit: "transmits" → "carried" is a verb-surface choice; if a stricter fence reviewer marks it FAULT-VERB-SURFACE, escalate to Phase 7 REWORD evaluation. For now: KEEP.
- P9 @9 (crowd-compresses): TENSE-CONFIRM past ("compressed"). Sensory:2 absorbed into verb (sensory-prose-fit at fork time).
- P10 @10 (I-kept-the-feet): TENSE-CONFIRM past ("kept"). PERSON-CONFIRM first. POV-PRONOUN-RESOLVE: "the feet" — same as P3; bone-canonical figure preserved (the feet as discipline-figure), NO RESOLVE.
- P11 @11 (lane-mouth-presses): TENSE-CONFIRM past ("pressed"). CONTRACTION: "I'd need" / "I wouldn't" fired.
- P12 @12 (insects-propagate): TENSE-CONFIRM past ("propagated" / "I'd told" / "telling was" / "wouldn't name"). PERSON-CONFIRM first ("I'd told them" / "I wouldn't name"). CONTRACTION: "I'd" / "wouldn't" fired.
- P13 @13 (dozen-yields): TENSE-CONFIRM past ("yielded").
- P14 @14 (gap-propagates-outward): TENSE-CONFIRM past ("propagated outward"). Verb varied from scene-A swell — Phase 1 fork choice preserved.
- P15 @15 (I-face-child): TENSE-CONFIRM past ("faced"). PERSON-CONFIRM first.
- **P16 @16 (raises-the-voice): POV-PRONOUN-RESOLVE FIRED — "I raised the voice" → "I raised my voice".** Bone-canonical "the voice" is third-person preserving; first-person POV requires the possessive "my" for the body-part/owned-noun. This is the expected key transform from the dispatch instructions. APPLIED.
- P17 dialogue paragraph: VERBATIM-FENCE — utterances unchanged ("Fever. Not the croup." / "She needs air. Stand back." / "Who knows her? Fetch them."). Attribution "I said" first-person past. CONTRACTION: none fire (utterances are clipped declarative imperatives; no contraction-eligible auxiliaries).
- P18 @17 (lift-the-hands): POV-PRONOUN-RESOLVE FIRED at Phase 1 fork time — "I lifted my hands" (bone "lifts the hands" → first-person possessive). KEEP as-rendered.
- P19 @18 (scene-bridge crowd-thins): TENSE-CONFIRM past ("closed" / "came apart" / "did"). EXPOSITION VERBATIM: exposition:7 "the way Flea Bottom crowds did" past-tense.
- P20 @18+@19+@20 (dispersal cluster): TENSE-CONFIRM past throughout ("went uneven" / "stayed" / "drifted" / "was the older habit" / "turned" / "faced" / "did not speak"). PRESERVE-THIRD-PARTY: "the fish-cart man" first-mention scene-C preserved; subsequent "He" pronoun (sentence-3) — CORRECT pronoun-after-first-mention. "Two women" first-mention preserved; no subsequent pronoun reference in this paragraph.
- **P21 @21 (Oswyn peak cluster): POV-PRONOUN-RESOLVE THIRD-PARTY FIRED — "His hands settled at the apron-front" → "His hands settled at his apron-front".** The apron belongs to Oswyn (the elder); first-mention-pronoun-possessive is the idiomatic surface. APPLIED. PRESERVE-THIRD-PARTY: "Oswyn Mudway" first mention scene-C; em-dash apposition "the Mudway man" (exposition:8 verbatim); subsequent "The elder" (exposition-canonical re-introduction, not a pronoun substitute — narrator:5 frames "the elder had taken the lane-mouth" with the term-of-art). TENSE-CONFIRM past ("took" / "had stood" / "named" / "had noticed" / "settled" / "had taken" / "would have"). CONTRACTION: none (no auxiliary contractions in this paragraph; "would have" not contracted to "would've" — schema default is contractions:true but past-perfect modal "would have" reads better non-contracted in narrative register; KEEP non-contracted).
- P22 @22 (child-clears): TENSE-CONFIRM past ("cleared").
- P23 @23 (gap-closes): TENSE-CONFIRM past ("closed").
- **P24 @24 (face-the-alley-mouth): POV-PRONOUN-RESOLVE FIRED — "I set the body to it" → "I set my body to it".** Bone-canonical "the body" is third-person preserving; first-person POV requires "my body" (Taylor's own body). APPLIED. TENSE-CONFIRM past ("faced" / "set" / "would not need"). CONTRACTION: "would not" → kept non-contracted (narrative register; the prohibition phrase carries weight at non-contracted form).
- P25 @25 (tallow-smoke-layers): TENSE-CONFIRM past ("layered" / "laid down" / "dropped" / "were near"). SENSORY-PROSE-FIT: bone "layers the lane-floor" rendered with low-and-slow specification (DRIFT-FLAGGED at Phase 1 for Phase 7 review; not Phase 4's job to cut).
- **P26 @26 (Oswyn-chin cluster): POV-PRONOUN-RESOLVE THIRD-PARTY FIRED — "Oswyn lifted the chin" → "Oswyn lifted his chin".** The chin belongs to Oswyn; third-party possessive idiom. APPLIED. Sentence-2 "The chin lifted the way it lifted..." — the bone-noun "the chin" is preserved as canonical rhetorical-mirror subject (the chin-as-figure does the action in the country's-older-stories register); NO RESOLVE on sentence-2 (the chin-as-figure is the narrator:9/memory:2 surface; "his chin" would collapse the figure). Sentence-3 "The chin-lift filed me..." — compound-noun shift; narrator:9 surface preserved. TENSE-CONFIRM past ("lifted" / "lifted" / "had been waiting" / "had finally arrived" / "filed" / "recognized" / "needing").
- P27 @27 (Wren chapter-close): TENSE-CONFIRM past ("faced" / "found" / "filed" / "kept" / "did not enter"). PERSON: third-person Wren first-mention via exposition:9 em-dash-apposition ("a Hook girl of eleven who watched cloth..."); first-person Taylor in sentence-3 ("I filed"). EXPOSITION VERBATIM: exposition:9 prose preserved modulo past-tense. PRESERVE-THIRD-PARTY: "the stitch-maker's ward" canonical first-mention (Wren's term-of-art surface; named at narrator:6 register as "stitch-maker's ward" not "Wren"). CONTRACTION: "did not" — kept non-contracted (the chapter-close register favors uncontracted negation; the prohibition-echo from preamble carries weight).

voice-transform outcome:
- TENSE-SHIFT: 0 (already past from Phase 1)
- PERSON-SHIFT-POV: 0 (already first from Phase 1)
- POV-PRONOUN-RESOLVE: 5 fired total
  - @16 "the voice" → "my voice" (Phase 4 explicit per dispatch instructions; CRITICAL KEY)
  - @17 "the hands" → "my hands" (Phase 1 fork-time; reconfirmed)
  - @21 "the apron-front" → "his apron-front" (third-party; Phase 4 fired)
  - @24 "the body" → "my body" (Phase 4 fired)
  - @26 "the chin" → "his chin" sentence-1 only (third-party; sentence-2/3 preserve bone-figure)
- PRESERVE-THIRD-PARTY: 4 confirmed (Oswyn Mudway / Wren as "stitch-maker's ward" / fish-cart man / two women — all first-mention preserved, pronouns thereafter)
- SENSORY-PROSE-FIT: 2 confirmed (@2 sensory-arrow lane-ambient→tallow-smoke-onset; @9 sensory:2 absorbed-into-verb)
- BONE-OBJECT-IDIOM-FIT: confirmed throughout (no prepositional inventions; "of the stitch-house lane" at @1 is location-anchored idiom-fit)
- CONTRACTION: 5 fired ("I'd" ×4 — P3/P4/P11/P12; "wouldn't" ×2 — P11/P12); "would not" / "did not" kept non-contracted in 2 places (P24/P27) for narrative-register weight; all schema-compatible.

## Phase 5 — local flow

walk per sliding window (window=3 paragraphs):

windows scanned: W1=P1/P2/P3, W2=P2/P3/P4, ... W25=P25/P26/P27. 25 windows total.

within-anchor cite reorder:
- W1-W3: @1 single fused sentence with 3 facets (loc-state:1 + exposition:4 + exposition:5); already optimal-order at Phase 1 fork (drain-trickle establishes location, exposition:4 fold-in defines Hook, exposition:5 parenthetical-aside defines ward, cobblestone-underfoot tactile closes). NO-REORDER.
- W2-W4: @2 sensory-arrow + bone single sentence; no within-anchor reorder candidate.
- W3-W5: @3 hold-block (bone + memory:1 + narrator:7); fork-time order is bone-subject → memory:1-fold → narrator:7-fold (cost-paid-on-principle closes the paragraph). NO-REORDER.
- W4-W6: @4 swell-block; same NO-REORDER.
- W10-W12: @11 (bone + narrator:3 em-dash-fold) — single sentence with em-dash-fusion already applied at Phase 1. EM-DASH-FUSE confirmed-as-rendered.
- W11-W13: @12 PEAK; bone + narrator:4 fused into single foreknowledge-clamped sentence (narrator:4 leads per Rule 1 — "where I'd told them to go, and the telling was a thing I wouldn't name" — Phase 1 fork applied the foreknowledge-clamp). NO-REORDER (Rule 1 foreknowledge-clamp determined the order).
- W19-W21: @21 peak cluster (bone + exposition:8 em-dash + feel:1 somatic + narrator:5 foreknowledge). Sentence order at Phase 1: (1) bone+exposition:8 fused, (2) feel:1 somatic surface "His hands settled at his apron-front", (3) narrator:5 foreknowledge "had taken the lane-mouth a week before...". Rule check: peak with feel → feel leads (Rule 3). But this is a peak-shadow-of-peak structure (@21 is scene-C's peak; feel:1 fires here); the Phase 1 fork chose bone-first ordering (Rule 4 default-kinetic) over feel-leads (Rule 3) because the bone-action is the peak-action and feel:1 is somatic-surface-corroboration, not the load-bearing peak gesture. WITHIN-ANCHOR-REORDER candidate evaluation: would Rule 3 require feel-leads? Reading rule 3 strictly: "At tens=3 with feel firing on any character, feel leads." Tens has been DROPPED per the substance overhaul; rule 3 has no firing condition in this run. Fall through to Rule 4 kinetic order. Phase 1 fork's ordering stands. NO-REORDER.
- W25-W27: @27 chapter-close 3-sentence cluster (bone+exposition:9 / feel:4-as-surface / narrator:6). Sentence order at Phase 1: bone+exposition:9 fused, then feel:4 as observable surface ("Her face found mine, eyes first"), then narrator:6 ("I filed the registration..."). PROTECTED at Phase 6; NO-REORDER.

forward sensory deferral: no candidate (sensory facets at @2 and @9 already at their anchor positions; no profile-cap-driven deferral).

backward NI promotion: NI promotion candidate scan:
- narrator:1 @4: "before the count completed" — temporal-lock phrase "before"; REFUSE-MIGRATE (temporal-lock).
- narrator:2 @8: "before the crowd registered the absence of one" — temporal-lock "before"; REFUSE-MIGRATE.
- narrator:3 @11: "the dozen I'd need, and the second dozen I wouldn't" — no temporal lock; em-dash-fused at anchor; promotion to @10 would cross scene-rhythm (peak-shadow-aware); REFUSE-MIGRATE.
- narrator:4 @12: foreknowledge-clamped at anchor by Rule 1; not promotable.
- narrator:5 @21: "a week before he would have the word for it" — temporal-lock "before"; REFUSE-MIGRATE.
- narrator:6 @27: chapter-close protected; not promotable.
- narrator:7 @3: "on principle every morning" — temporal-lock "every morning"; REFUSE-MIGRATE.
- narrator:8 @24: "so the stitch-house lane would not need to be registered again" — temporal-lock "again"; REFUSE-MIGRATE.
- narrator:9 @26: "filed me in a category he recognized" — no temporal lock; but cluster-protected at @26 with memory:2; promotion to @25 would split the 3-sentence Oswyn-chin cluster; REFUSE-MIGRATE (pattern-protected).

un-merge to rescue swallowed facets: no facet was swallowed at Phase 1 (all 43 facet entries traceable to a rendered surface or explicit render=false). No UN-MERGE.

speaker-paragraph rule HARD check at @16:
- L29: "I faced the child." (own paragraph)
- L31: "I raised my voice." (own paragraph — bone-as-speech-act surface)
- L33: dialogue paragraph "Fever. Not the croup," I said. "She needs air. Stand back. Who knows her? Fetch them." (own paragraph)
- L35: "I lifted my hands." (own paragraph)
SPEAKER-PARAGRAPH-BREAK @16 VERIFIED — dialogue is on its own paragraph, separated from "I raised my voice" (bone-as-speech-act anchor) and from "I lifted my hands" (@17 closer). No same-paragraph speaker collision.

local-flow outcome:
- WITHIN-ANCHOR-REORDER: 0 fired (Phase 1 fork-time orders held)
- EM-DASH-FUSE: 1 confirmed-as-rendered (@11)
- MIGRATE-SENSORY-FORWARD: 0
- MIGRATE-NI-BACKWARD: 0 (9 REFUSE-MIGRATE — 7 temporal-lock, 2 pattern-protected)
- UN-MERGE: 0
- SPEAKER-PARAGRAPH-BREAK: VERIFIED at @16 (no enforcement needed; Phase 1 fork already produced compliant layout)

## Phase 6 — buildup preservation

scene-map declared protected-patterns: none. Emergent-pattern walk:

countdown candidates: none in body prose. (No 3-2-1, no "the third time", no enumerated descent.)

three-beat rhythm candidates:
- @11/@12/@13 (lane-mouth-presses / insects-propagate / dozen-yields) — scene-B peak triplet. Bones-as-rhythm: peak-shadow / PEAK / peak-shadow per scene-map; the three-beat is the rhythm-shape of scene-B's release, not a structural countdown. PATTERN-OK (intact at Phase 6; standalone paragraphs preserve the percussion).
- @26 (3-sentence Oswyn-chin cluster: bone-action / memory:2 country's-older-stories / narrator:9 filed-in-category). NEW-PATTERN-CANDIDATE: three-sentence-buildup at scene-C climax, each load-bearing. Flag for future scene-map enrichment; no Phase 6 action required.
- @27 (chapter-close 3-sentence cluster: bone+exposition:9 / feel:4-as-surface / narrator:6) — DECLARED PROTECTED IN DISPATCH INSTRUCTIONS. Verify intactness:
  - sentence 1: "The stitch-maker's ward — a Hook girl of eleven who watched cloth before she cut it, and watched people the same way — faced me." (bone + exposition:9 em-dash-fold)
  - sentence 2: "Her face found mine, eyes first." (feel:4 as observable surface, POV-fence-honored — NOT Wren-interior)
  - sentence 3: "I filed the registration in the same fold where I kept the things that did not enter the ledger." (narrator:6 Taylor-interior; cost-bearer first-contact close)
  PATTERN-OK — three-sentence cluster intact, each load-bearing, chapter-close on cost-bearer first contact. PROTECTED-PRESERVED.

threshold sequences: scene-B is the threshold-crossing scene (substance: first deployment); rendered as peak-and-release with @12 the PEAK. The threshold itself is a single anchor (@12), not a multi-anchor threshold sequence. PATTERN-OK.

buildup outcome:
- PATTERN-OK: 3 (@11/@12/@13 three-beat scene-B peak; @27 chapter-close 3-sentence cluster; scene-B threshold @12)
- RESTORE-PATTERN: 0 (nothing degraded)
- PATTERN-ABANDONED: 0
- NEW-PATTERN-CANDIDATE: 1 (@26 three-sentence Oswyn-chin cluster — flag for future scene-map enrichment; no action this run)

---

Phase 2-6 SUMMARY:
- redundancy cull: 0 drops; 12 KEEP-OVER-ECHO (scene-window landed clean)
- compression: 0 merges; 4 SUBSTITUTE-PRONOUN already-applied; 27 NO-MERGE
- voice transform: 5 POV-PRONOUN-RESOLVE fired (@16 my voice CRITICAL KEY; @17 my hands; @21 his apron-front; @24 my body; @26 his chin sentence-1); contractions schema-default applied; preserve-third-party confirmed
- local flow: 0 reorders; speaker-paragraph @16 VERIFIED-INTACT; 9 REFUSE-MIGRATE on NI-promotion (temporal-lock / pattern-protected)
- buildup preservation: 3 PATTERN-OK (including @27 chapter-close PROTECTED-PRESERVED); 1 NEW-PATTERN-CANDIDATE flag at @26

Phase 6 draft written: active-project/draft/b01-c01.phase-6.draft.md (body only; preamble prepended separately at Phase 8).

drift-risks from Phase 1 carry forward unchanged to Phase 7: @7, @18, @19, @25.

## Phase 7 — editorial reflection

per-sentence sweep dispatch: single-fork sweep across the body draft (27 paragraphs / 35 sentences). Neutral persona, balanced cut-aggressiveness (schema default). Exposition-derived sentences (L1, L13, L37, L41.1, L53.1) treated per dispatch carve-out (Q1/Q5/Q8 pre-cleared upstream; Q6/Q9 normal). Dialogue utterances (L33 utterances) treated per dispatch carve-out (Q1/Q5/Q8/Q9/Q6 pre-cleared); attribution "I said" Q-checked normally.

per-sentence Q-lines:

```
L1.1:   Q1=y Q2=y Q3=y Q4=y Q5=n Q6=y Q7=n Q8=n Q9=n → KEEP  (exposition-derived; em-dash-fold + parenthetical-aside both upstream-authored; Q6 reach acceptable — em-dashes are structural for compound first-mention folds, not ornamental)
L3.1:   Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (sensory-arrow facet-token render; compounds "lane-ambient" / "tallow-smoke-onset" are facet tokens, not stitcher-coined)
L5.1:   Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (bone-only declarative; load-bearing — establishes the holding-action)
L5.2:   Q1=y Q2=y Q3=y Q4=y Q5=n Q6=y Q7=n Q8=n Q9=n → KEEP  (memory:1 + narrator:7 fused; Q6 semicolon is structural — joining two consequence-clauses on one cost-paid breath)
L7.1:   Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (bone-only declarative; load-bearing — the swell is the slip-event)
L7.2:   Q1=y Q2=y Q3=y Q4=y Q5=n Q6=y Q7=n Q8=n Q9=n → KEEP  (narrator:1 fused; Q6 semicolon structural — relays slip→correction)
L9.1:   Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (bone-only geometric beat; scene-A rhythm-protected)
L11.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (scene-A close on body action)
L13.1:  Q1=y Q2=y Q3=y Q4=n Q5=n Q6=y Q7=n Q8=n Q9=n → CUT-CLAUSE ", parked across the angle-pinch at the wrong hour" → DRIFT-RISK @7 resolved (Q4=no on invented spatial+judgment tail; the bone "blocks the lane" + exposition:6 carry load; "wrong hour" is narrator-judgment invention beyond NI/mem facets at @7)
L15.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (narrator:2 sequence-of-knowledge; load-bearing — the ground-precedes-crowd inversion is the bone's interior payload)
L17.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (bone-only; load-bearing kinetic step)
L19.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (verb-varied callback to L5.1; load-bearing — the hold continues across the crowd-pressure)
L21.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=y Q7=n Q8=n Q9=n → KEEP  (narrator:3 em-dash-fold; Q6 em-dash structural for crowd-arithmetic fold)
L23.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (PEAK; narrator:4 foreknowledge-clamp; Rule 1 lens-led)
L25.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (peak-shadow; load-bearing — the yield is the gap-source)
L27.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (gap-propagation kinetic; load-bearing)
L29.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (face-turn; speaker-paragraph setup)
L31.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (bone-as-speech-act surface; SPEAKER-PARAGRAPH-BREAK-anchor)
L33.utt: pre-cleared → KEEP  (verbatim dialogue, fence-protected)
L33.att: Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (first attribution carries speaker identity; per dispatch carve-out)
L35.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (scene-B close still-frame; forward-look fence honored)
L37.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (exposition-derived scene-bridge; upstream-cleared)
L39.1:  Q1=n Q2=n Q3=y Q4=n Q5=y Q6=y Q7=n Q8=n Q9=n → CUT  (DRIFT-RISK @18 resolved; "The thinning went uneven — a few stayed for the look of staying, more drifted because drifting was the older habit." — Q1=no: L37.1 already carries the dispersal payload "the crowd came apart the way Flea Bottom crowds did"; Q5=yes: declarative-verdict on crowd-habit without observation source; Q4=no: invention beyond bone @18 + exposition:7. Whole sentence cut. Q2 continuity preserved — L37→L39.2 reads: "After the gap closed, the crowd came apart the way Flea Bottom crowds did. The fish-cart man...")
L39.2:  Q1=n Q2=n Q3=y Q4=n Q5=n Q6=n Q7=n Q8=n Q9=n → CUT-CLAUSE "turned the cart on its pole, and turned with it, and" → DRIFT-RISK @19 partial-resolve (Q4=no on invented body/spatial: bone @19 = "fish-cart-man faces taylor"; "turned the cart on its pole, and turned with it" is invented body/spatial sequence beyond bone+facets — no location-state or feel facet supports the cart-on-pole rotation. Kept fragment "The fish-cart man faced me." stands alone and preserves the bone-action.)
L39.3:  Q1=n Q2=n Q3=y Q4=n Q5=y Q6=n Q7=n Q8=n Q9=n → CUT  (DRIFT-RISK @19 resolved; "He did not speak." — Q1=no: not load-bearing (no plot/motivation/scene-logic depends on the non-speech of the fish-cart man at this anchor — Oswyn's speech-or-not arrives at @21); Q5=yes: non-event declarative without graph license — there is no bone, feel, narrator, or sensory facet that licenses naming his silence; Q4=no: invention beyond bone @19. Whole sentence cut.)
L39.4:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (bone @20 + location-state spatial "side by side at the edge of the press"; load-bearing kinetic registration of second witness-cluster)
L41.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=y Q7=n Q8=n Q9=n → KEEP  (exposition:8 em-dash-fold; upstream-cleared; Q6 em-dash structural)
L41.2:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (feel:1 somatic surface "His hands settled at his apron-front"; load-bearing — observable somatic tell at peak)
L41.3:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (narrator:5 foreknowledge "a week before he would have the word for it"; load-bearing — narrator's recognition predates Oswyn's)
L43.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (peak-shadow; load-bearing — child-clears-lane is the substance payoff)
L45.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (peak-shadow; three-word standalone; bone-only)
L47.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (bone-only face-turn)
L47.2:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (narrator:8 registration-refusal surface; load-bearing — the not-need-to-be-registered-again clause carries the cost-of-attention payload)
L49.1:  Q1=y Q2=y Q3=y Q4=n Q5=n Q6=y Q7=n Q8=n Q9=n → CUT-CLAUSE ", low and slow, the way it laid down in the Hook when the wind dropped and the rendering-fires were near" → DRIFT-RISK @25 resolved (Q4=no on invented atmospheric specification: bone @25 = "tallow-smoke layers lane-floor" + sensory:absorbed; "low and slow / wind dropped / rendering-fires near" is invented atmospheric beyond bone+facets — no sensory, location-state, or memory facet supports the wind/rendering-fires specification. Kept fragment "The tallow smoke layered the lane-floor." stands alone and preserves the bone-action.)
L51.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (bone-action standalone; POV-pronoun-resolved at Phase 4)
L51.2:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (memory:2 country's-older-stories register; load-bearing — the rhetorical-mirror is the bone-cluster's interior payload)
L51.3:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (narrator:9 filed-in-category; load-bearing — closes the Oswyn-recognition arc)
L53.1:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=y Q7=n Q8=n Q9=n → KEEP  (exposition:9 em-dash-fold; chapter-close PROTECTED; upstream-cleared)
L53.2:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (feel:4-as-surface "eyes first"; chapter-close PROTECTED; observable-only, POV-fence honored)
L53.3:  Q1=y Q2=y Q3=y Q4=y Q5=n Q6=n Q7=n Q8=n Q9=n → KEEP  (narrator:6 chapter-close interior; cost-bearer first-contact close; PROTECTED HARD)
```

per-sentence sweep: 35 sentences swept across 27 paragraphs.
moves: cuts=2, cut-clauses=3, reshows=0, rewords=0, simplify-puncts=0, keeps=30

drift-risk dispositions:
  - @7 L13 "parked across the angle-pinch at the wrong hour": CUT-CLAUSE — invented narrator-judgment ("wrong hour") on timing plus invented spatial ("parked across") beyond bone+exposition. Q4=no, Q1=no on the tail. Kept fragment "The fish-cart blocked the lane — a handcart of the kind the morning fish-trade ran through the Hook from the river-side gate." stands alone; the bone-action and exposition:6 fold-in are preserved intact.
  - @18 L39.1 "thinning went uneven... older habit": CUT (whole sentence) — Q1=no (L37.1 carries dispersal payload "came apart the way Flea Bottom crowds did"); Q5=yes (declarative crowd-habit judgment without observation); Q4=no (invention beyond bone @18 + exposition:7). Continuity preserved by L37.1 → L39.2 ("After the gap closed... The fish-cart man faced me.").
  - @19 L39.2-3 "turned the cart on its pole... He did not speak.": CUT-CLAUSE on L39.2's body-rotation specifics (kept fragment "The fish-cart man faced me." preserves bone @19 = fish-cart-man faces taylor); CUT on L39.3 "He did not speak." — non-event tail with no graph source for the named silence and not load-bearing for the scene's @21 Oswyn-speaks payoff. Bone @19 fully rendered by the kept fragment.
  - @25 L49 "low and slow... rendering-fires were near": CUT-CLAUSE — invented atmospheric specification beyond bone @25 + sensory:absorbed. No sensory, location-state, or memory facet licenses "low and slow / wind dropped / rendering-fires near". Kept fragment "The tallow smoke layered the lane-floor." preserves the bone-action.

residuals:
- All 4 dispatch-flagged drift-risks resolved at CUT or CUT-CLAUSE.
- Non-drift sentences: 30/30 KEEP. Q1 load-bearing held across the entire body except at the four flagged surfaces.
- Q6 em-dash/semicolon checks: 6 paragraphs use em-dashes or semicolons (L1, L5.2, L7.2, L13, L21, L41.1, L53.1). All KEEP — each em-dash or semicolon is structural (exposition fold, semicolon-relay between cause-and-correction, em-dash crowd-arithmetic fold) rather than ornamental reach.
- Q9 anti-jargon checks: zero stitcher-coined compounds; all hyphen-compounds in the body trace to bones or facet tokens (angle-gap / stitch-house / lane-ambient / tallow-smoke-onset / angle-wall / lane-mouth / peak-shadow vocabulary is bones/facets-derived; "angle-pinch" cut as part of the L13 CUT-CLAUSE).
- Q5 hollow-prose: 2 hits, both at drift-risk sentences (L39.1 and L39.3); both cut.

Phase 7 draft written: active-project/draft/b01-c01.phase-7.draft.md (body only; preamble prepended at Phase 8 finalize).


