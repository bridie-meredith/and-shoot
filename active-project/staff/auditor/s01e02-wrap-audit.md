---
report: wrap-audit
episode: s01e02
date: 2026-05-13
auditor-fork: one-time agent (and-wrap Phase 2)
inputs:
  - active-project/draft/s01e02.md
  - active-project/draft/s01e02.annotated.md
  - active-project/staff/stitcher/render-log-s01e02.md
  - active-project/theater/proto-lines/s01e02.md
  - active-project/theater/s01e02-archive/facets/_cite-index.md
  - active-project/theater/facets/scene-map-s01e02.md
  - active-project/theater/dialogue/oc-tanner-father.md
  - active-project/theater/dialogue/oc-tanner-mother.md
  - active-project/theater/dialogue/oc-tanner-elder.md
  - active-project/theater/dialogue/oc-broken-maester.md
  - active-project/theater/dialogue/oc-dock-runner.md
  - active-project/theater/dialogue/taylor-hebert-flea-bottom.md
  - active-project/theater/s01e02-archive/facets/exposition-s01e02.md
  - active-project/theater/s01e02-archive/facets/metaphor.md
verdict: HARDS-PRESENT
counts:
  hard: 7
  signal: 1
---

# /and-wrap Phase 2 auditor report — s01e02

Eight-class audit of rendered prose against the upstream graph. Audit performed independently of the Phase 1 audience review; both feed Phase 3 editor.

---

## BONE-COVERAGE findings (4)

Bones in `proto-lines/s01e02.md` lacking a rendered surface AND lacking a render-log `CUT-BONE` license. Authorized cuts (e.g. @91) are not faults.

[HARD] FAULT-EDITOR-BONE-LOST @42 — bone "the flies relay the carter" has no rendered trace
  trace search: annotated draft Scene-D (L28–L30) cites @41/@45/@46/@49 plus a loc-state fragment at L29 — no surface for @42
  render-log entry: no CUT-BONE, no FUSE-into-LN, no DROP entry for @42 in P7-2 (Scene B/C/D/E) move tally
  prose surface (Scene D): "The daylight dropped as I stepped in. / Empty room, alley-sound through the second-floor window. / I opened the log, wrote the entry, closed it." — no carter-relay surface

[HARD] FAULT-EDITOR-BONE-LOST @44 — bone "the flies relay the wind" has no rendered trace
  trace search: annotated draft Scene-D (L28–L30) — no surface for @44
  render-log entry: no CUT-BONE/FUSE/DROP for @44 in P7-2 move tally
  note: "alley-sound through the second-floor window" at L29 is annotated as `loc-state:3 folded as scene-fact fragment`, not as a fold for @44; @44 (flies-relay-wind) is a fauna-relay operational bone, not loc-state

[HARD] FAULT-EDITOR-BONE-LOST @101 — bone "taylor-hebert-flea-bottom faces oc-tanner-father" has no rendered trace
  trace search: annotated draft Scene-I jumps L60 (@99 father-faces-taylor) → L61 (@100 father utterance) → L63 (@102 taylor utterance). No "I faced him" / "I turned to him" beat between L60 and L63.
  render-log entry: no CUT-BONE/FUSE/DROP for @101 in P7-5 (Scene I/J) move tally
  comparable bone @13 in Scene A ("taylor faces father") was rendered as L6 "I faced him, shoulders square, weight even" — the symmetric reciprocal-face beat is present in Scene A and absent in Scene I

[HARD] FAULT-EDITOR-BONE-LOST @139 — bone "the beetles relay the register [narrator:25]" trace-citation missing despite probable surface render
  trace search: annotated L85 cites only `bone @138 | dialogue:oc-broken-maester:1` — but the prose surface ("The beetles brought the register through the wall, and from the upper room the maester's voice came down: ...") clearly contains the @139 relay content as the wall-relay framing for the utterance
  render-log entry: Phase 1 re-stitch RS1-L names the relay-frame as "attribution-equivalent" for @138 only; @139 not explicitly cited
  classification note: this is most likely a trace-citation oversight rather than a true bone-lost (the relay-frame IS the surface for @139); auditor flags as HARD per the strict trace-discipline rule, but editor disposition should be light-touch (verify trace, no prose rewrite needed)

(Note: bones @1/@2 in proto-lines are empty numbered placeholders with no SVO content — not findings. Bones @165 "mother enters base room" and @166 "mother faces taylor" appear unflagged in trace at L100/L102 but are rendered: "My mother came in" folds @164/@165; "She faced me" renders @166. These are trace-citation defects on the annotated draft, not BONE-LOST faults; surfaced here for editor awareness but not enumerated as findings.)

---

## DIALOGUE-VERBATIM findings (0)

All 15 quoted utterances (14 anchor-keyed + 1 multi-sentence continuation per @14/@23) verified against per-character dialogue files:

- @14 oc-tanner-father:1 ("We come down with the hides. Your mother would see you.") — verbatim
- @15 taylor:1 ("Goodman. I have not forgotten.") — verbatim
- @19 oc-tanner-father:2 ("Old Tom. A word, when you've a moment. The Crownlands lot, same as before.") — verbatim
- @20 oc-tanner-elder:1 ("Aye. Same slate, same cut. She's earning her place, last I heard. We'll keep it that way.") — verbatim
- @23 oc-tanner-mother:1 ("You've grown thin, child. Are you eating?") — verbatim
- @24 taylor:2 ("Goodwife. The road is yours.") — verbatim
- @52 oc-tanner-elder:2 ("Off with you, then. Tell the dock-man Tom's word is good for the load. Before the bell.") — verbatim
- @100 oc-tanner-father:3 ("There's the wage-claim, girl. Customary. Two coppers a moon till the harvest turn, and we're square.") — verbatim
- @102 taylor:3 ("Name the sum. I will see it paid.") — verbatim
- @103 oc-tanner-father:4 ("Two coppers. That's the way of it. Same as your mother's people done for hers.") — verbatim
- @108 oc-tanner-father:5 ("We'll come again at the next moon's turn. Mind yourself.") — verbatim
- @138 oc-broken-maester:1 ("Yes, yes. Come, sit. Let us see what you have brought.") — verbatim
- @169 oc-tanner-mother:2 ("The candle's gone short. I'll let it burn what's left and trouble you no more.") — verbatim
- @170 taylor:4 ("She is not here, goodwife.") — verbatim
- @171 oc-tanner-mother:3 ("I'll stop coming, after this one. Seven keep you. Whatever you are, you are warm — that's what I came to see.") — verbatim

Attribution clauses ("he said", "my mother said", "I answered") are voice-transformed within the default attribution-verb set and are not gloss-modification.

Bare-speech bones @84 (lords-man) and @137 (visitor→maester) render as silent action per the by-design POV-distance legacy-silent-speech preservation — no dialogue facet entry exists; not faults.

---

## EXPOSITION-VERBATIM findings (1)

[HARD] FAULT-EDITOR-EXPOSITION-MODIFIED @0 — preamble gloss does not match `exposition-s01e02.md` exposition:1 source
  source gloss: "Through the first weeks in Flea Bottom I had walked my three hundred metres twice a day, mapped the market-side junction and the apothecary's upper room where the broken maester kept his hours, and made my first transactional pass with the dock-runner through the tanner-elder. The log was current. The tanner-village was a day's walk south and had stayed there."
  rendered: "Through the first weeks in Flea Bottom I had walked my three hundred metres twice a day, mapped the market-side junction and the apothecary's upper room where the broken maester kept his hours, and made my first transactional pass with the dock-runner through the tanner-elder. The log was current. The tanner-village was a day's walk south."
  diff: trailing "and had stayed there" removed
  render-log entry: documented as "FAULT-EXPOSITION-AUDIT-MISS @0" / "Phase 7 REWORD post-stitch: dropped 'and had stayed there' (Q8 asinine — non-sentient-negation; locations don't move)" — the modification is documented as a user-override post-stitch surface fix and flagged upstream for exposition-author re-audit (anti-asinine-pattern promotion to AP-SCAN per URI-026)
  editor disposition note: the modification is upstream-documented with reasoning; per the strict EXPOSITION-VERBATIM rule it remains a HARD finding, but editor disposition is ack-and-pass (the source needs upstream re-author; this episode's prose is correct and ships)

The other five exposition entries verified verbatim:
- exposition:2 @66 Fish-Gate em-dash-fold — verbatim
- exposition:3 @100 customary-wage parenthetical-aside — verbatim (capitalization "What" + period inside parens is positional/voice, gloss text identical)
- exposition:4 @173 vigil-candle em-dash-fold — verbatim
- exposition:5 @30 base-room scene-bridge — verbatim
- exposition:6 @34 relays-run scene-bridge — verbatim

---

## NO-INVENTION findings (0)

Scanned the rendered prose for proper nouns, character names, locations, props, conditions, and behaviors not present in the facet graph or referenced cards. All surface content traces:

- Characters: Taylor (POV-implicit), father, mother, elder, maester, visitor, lord's-man, lord's-man's man, neighbour, carter, dock-man (referenced in elder utterance @52, present in graph as oc-dock-runner) — all in cast roster.
- Locations: Flea Bottom, market-side junction, base room, second-floor window, apothecary, upper room, side alley, stairwell, side-alley door, night alley, two-room dwelling, road south, Fish Gate, King's Landing, Crownlands, Eastern-Quarter, south-wall, northern block — all in scene-map locations or licensed exposition glosses (Fish Gate / King's Landing / Crownlands are exposition-gloss residents).
- Props: hides / trade goods, log, stylus, purse, coins, bench, chair, candle / vigil candle, latch, bar — all in graph or licensed exposition.
- Conditions / behaviors: customary wage, Stranger / Stranger-light, Seven, the Watch, Citadel — all in the cards graph (cond-westerosi-customary-authority-125ac, cond-crownlands-superstition-frame-125ac, westeros-maester behavior). "Seven keep you" (mother's blessing) is registered Crownlands superstition register, attested in the mother's dialogue card source.
- Fauna: flies, wasps, beetles, spiders — series-resident.

No invention detected.

---

## CONTINUITY findings (3)

[HARD] FAULT-EDITOR-CONTINUITY-PRONOUN-AMBIGUITY @scene-K — paragraph 25 visitor/maester "he" antecedent
  source: clean draft paragraph 25 "The visitor entered the side alley, then the stairwell, then the upper room. The visitor spoke; I did not hear what. The beetles brought the register through the wall, and from the upper room the maester's voice came down: 'Yes, yes. Come, sit. Let us see what you have brought.' I held my feet still. He went out by the upper room, by the stairwell, by the side-alley door."
  graph: bones @141/@142/@143 = "the visitor exits the upper room / stairwell / side-alley door" — single resolution: the exiting "he" is the visitor
  ambiguity: the maester is the last named-male speaker before "He went out" (closer noun-phrase referent), so a first-pass reader binds "He" → maester before backtracking to visitor; graph supports single resolution → CONTINUITY HARD per spec
  cross-ref: Phase 1 audience (cape-fic-reader, worm-canon-pedant) independently flagged this line as the first place "fixed-anchor live-watch costs comprehension"

[HARD] FAULT-EDITOR-CONTINUITY-PRONOUN-AMBIGUITY @scene-H — paragraph 19 "the lord's-man's man — an ear pressed to a wall"
  source: clean draft paragraph 19 "The flies relayed the lord's-man's man — an ear pressed to a wall."
  graph: bone @89 = "the flies relay the lords-man's man [meta:1]"; metaphor:1 = "the flies are an ear pressed to a wall" — single resolution: the metaphor binds to the flies, not to the lord's-man's man
  ambiguity: em-dash structure "X — an ear pressed to a wall" reads on first pass as an appositive on the closest noun-phrase (the lord's-man's man), reversing the intended metaphor attachment; graph supports single resolution → CONTINUITY HARD
  cross-ref: Phase 1 audience (cape-fic-reader, worm-canon-pedant) flagged

[SIGNAL] FLAG-EDITOR-POSSESSIVE-REGISTER-BREAK @scene-I — paragraph 21 "I let the breath out"
  source: clean draft paragraph 21 "I let the breath out. I opened the purse."
  rule: per `staff/stitcher/personas/worm-tight.md` tuning notes (2026-05-12 retraction), Taylor's body-part possessive register is "my X" not "the X" — "my breath" expected, "the breath" is the retracted form
  graph: bone @104 = "taylor-hebert-flea-bottom exhales [narrator:20]" — exhalation is Taylor's, possessive register applies
  render-log: P7-5 fork records POSSESS-FIX × 3 in Scene J ("the eyes / the chin / the hand" → "my eyes / my chin / my hand") — the breath-beat at @104 escaped the POSSESS-FIX pass; SIGNAL not HARD because possessive-register breaks are explicitly enumerated as SIGNAL in the audit-class rubric

(L13 elder "He turned and faced me square" — graph @54 says elder faces taylor; the "he" antecedent "the elder said" in the immediately preceding clause supports single resolution. The audience's L13 concern referenced a "wagon-driver" gloss not present in the current rendered prose; the live prose is unambiguous. Not a CONTINUITY finding.)

(Tense: simple-past first-person held throughout. Preamble past-perfect ("had walked", "had stayed") is appropriate. No mid-paragraph tense shifts detected.)

---

## BLOCKING findings (0)

Spatial relations preserved.

- Taylor's location across the episode: base room (Scenes B/C/D/F/G/I-second-half/J/N) and market-side junction (Scenes A/E/I-first-half). Transitions all present in the prose: para 5→7 "out of the junction" / "Back at the base room" (exposition:5 bridge); para 11→13 "Out to the market-side junction" (scene-E open); para 21 "He left the junction; she left after him" + "I opened the log" (junction→base implicit return, log indicates base).
- Observational scenes (H eviction-alley, K/L/M apothecary upper room) — Taylor remains at base; the prose holds her at base while flies/beetles relay the remote scenes. The "I held my feet still" beat at L86 confirms Taylor's positional stillness during the visitor-arc, supporting the fixed-anchor live-watch convention.
- Tanner-family movements: enter junction → cross junction → exit junction → return-next-visit — all bone-cited and prose-rendered in order.
- Mother in Scene N: enters loc-flea-bottom-base → sits → stands → leaves the room — all bone-anchored and rendered.

No blocking faults.

---

## SCENE-MAP-RESPECT findings (0)

Scene boundaries from `scene-map-s01e02.md` (14 scenes A–N) honored. The rendered draft has 16 paragraphs (preamble + 14 scene-paragraphs + episode-close log-trio standalone). Paragraph-to-scene mapping is monotone and ordered:

- p1 = preamble
- p5 = scene-A @3-@28
- p7 = scene-B @30-@32
- p9 = scene-C @34-@37
- p11 = scene-D @41-@49
- p13 = scene-E @50-@58
- p15 = scene-F @60-@76
- p17 = scene-G @77-@81
- p19 = scene-H @83-@95
- p21 = scene-I @97-@115
- p23 = scene-J @117-@130
- p25 = scene-K @132-@146
- p27 = scene-L @148-@154
- p29 = scene-M @156-@162
- p31 = scene-N @164-@174
- p33 = episode-close log-trio @176-@178 (Scene-N continuation per scene-map)

No reordered scenes. No merged scenes. Protected patterns (cardinal-quartet @60-@63, three-note-buildup @148-@150, log-trios, route-triples) all intact per render-log Phase 6 + Phase 8 confirmations and verified in prose.

---

## EARTH-BET-HARD-FENCE findings (0)

Full-prose scan for the Earth-Bet proper-noun list: Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil, Tattletale, Bitch, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea.

Zero hits. The fence holds.

---

## Audit summary

verdict: HARDS-PRESENT
HARD: 7
SIGNAL: 1

Per-class breakdown:
- BONE-COVERAGE: 4 HARD (@42, @44, @101, @139)
- DIALOGUE-VERBATIM: 0
- EXPOSITION-VERBATIM: 1 HARD (@0)
- NO-INVENTION: 0
- CONTINUITY: 2 HARD (paragraph 25 visitor/maester "he"; paragraph 19 ear-pressed-to-a-wall attachment) + 1 SIGNAL (paragraph 21 "the breath" possessive-register break)
- BLOCKING: 0
- SCENE-MAP-RESPECT: 0
- EARTH-BET-HARD-FENCE: 0

classes with findings: BONE-COVERAGE, EXPOSITION-VERBATIM, CONTINUITY
classes clean: DIALOGUE-VERBATIM, NO-INVENTION, BLOCKING, SCENE-MAP-RESPECT, EARTH-BET-HARD-FENCE

editor disposition: blocked pending HARDs — but four of the seven HARDs are light-touch:
  - @139 BONE-COVERAGE is a trace-citation defect; the surface is present in prose. Editor verifies trace, no prose rewrite.
  - @0 EXPOSITION-VERBATIM is upstream-documented and is the correct rendered surface; the source-side gloss needs re-authoring (not in scope here). Editor ack-and-passes the rendered prose.
  - @42 and @44 BONE-COVERAGE (flies relay carter / wind) are silent observational fauna-relay bones; the natural fix is fold-into-existing-sentence (e.g. "Empty room, alley-sound through the second-floor window — the flies on the carter, the wind." or similar), small surface insert.
  - @101 BONE-COVERAGE (Scene I taylor faces father) needs a one-clause reciprocal-face beat between L60 and L61 of the annotated draft (paragraph 21 of clean draft) — surface insert, no plot move.
  - paragraph 25 visitor/maester "he" CONTINUITY — disambiguate the pronoun ("The visitor went out by the upper room, by the stairwell..." or pull a "the visitor" naming on first reverse-route step).
  - paragraph 19 lord's-man's man / ear-pressed-to-a-wall CONTINUITY — restructure the em-dash attachment so the metaphor binds visibly to the flies (e.g. "The flies were an ear pressed to a wall, relaying the lord's-man's man." or "The flies relayed the lord's-man's man; they were an ear pressed to a wall.").

recommended fixer routing: not needed — all seven HARDs are within the editor's allowed-moves contract for `/and-wrap` Phase 3:
  - BONE-COVERAGE fixes are "paragraph adjustments" / "prose economy" / single-sentence inserts that respect the bone graph (the bones already exist; the editor is filling rendered surface to honor them).
  - EXPOSITION-VERBATIM @0 is ack-and-pass; the rendered prose is the correct ship-form.
  - CONTINUITY pronoun-ambiguity fixes are explicitly an editor allowed-move (continuity + repetition cull + voice consistency).
  - The single SIGNAL (possessive-register "my breath") is also an editor surface fix.

No fixer dispatch needed. Editor proceeds with the seven HARD remediations plus the audience-flag remediations as an integrated whole-text Phase 3 pass.
