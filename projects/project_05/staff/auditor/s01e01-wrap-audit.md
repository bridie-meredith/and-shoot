---
report: wrap-audit
episode: s01e01
date: 2026-05-13
auditor-fork: one-time agent (and-wrap Phase 2)
inputs:
  - active-project/draft/s01e01.md
  - active-project/draft/s01e01.annotated.md
  - active-project/staff/stitcher/render-log-s01e01.md
  - active-project/theater/proto-lines/s01e01.md
  - active-project/theater/s01e01-archive/facets/_cite-index.md
  - active-project/theater/facets/scene-map-s01e01.md
  - active-project/theater/facets/exposition-s01e01.md
  - active-project/theater/s01e01-archive/facets/tensometer-s01e01.md
  - active-project/theater/s01e01-archive/facets/sensory.md
  - active-project/theater/s01e01-archive/facets/location-state.md
  - active-project/theater/s01e01-archive/facets/vibes.md
  - active-project/theater/s01e01-archive/facets/memory.md
  - active-project/theater/s01e01-archive/facets/feeling-taylor-hebert-flea-bottom.md
  - active-project/theater/s01e01-archive/facets/feeling-oc-tanner-mother.md
  - active-project/theater/s01e01-archive/facets/feeling-oc-broken-maester.md
verdict: HARDS-PRESENT
counts:
  hard: 3
  signal: 4
---

# /and-wrap Phase 2 auditor report — s01e01

Eight-class rendered-prose-against-graph audit. Audit target is `active-project/draft/s01e01.md` (clean draft). The annotated draft (`s01e01.annotated.md`) is the tracing document; divergences between annotated and clean are noted where they affect trace reliability. Dialogue facet is absent (pre-2026-05-12 episode); DIALOGUE-VERBATIM passes trivially.

---

## BONE-COVERAGE findings (1 HARD, 1 SIGNAL)

Proto-lines total: 146 bones. Authorized cuts per render-log and annotated trace:
- Scene B: @32-@34 (log-trio) — CUT, repetition discipline
- Scene D: @59-@61 (log-trio) — CUT, repetition discipline
- Scene F: @81-@83 (Taylor log-trio) — CUT, redundant with lord's-man inscription
- Scene I: @105-@107 (log-trio) — CUT, repetition discipline
- Scene J: @113 (duplicate walk), @116-@118 (log-trio) — CUT
- Scene K: @125-@127 (log-trio) — CUT, three-beat IS the scene close
- Scene M: @146 — CUT, fauna-relay refrain saturation

All listed cuts are render-log-licensed. Remaining bones trace to the annotated draft without fault — with two exceptions below.

---

[HARD] fault-001 — BONE-COVERAGE
  what: bone @72 "the flies relay the reeve [tens:67]" — no rendered surface in clean draft, no CUT-BONE, FUSE-into, or DROP entry in render-log
  detail: Scene F in the render-log (Phase 1 per-scene returns) states "8 anchors + Taylor log @81-83 CUT." Scene F covers anchors @72-@83 (11 bones, excluding @80 blank). With @81-@83 CUT, 8 bones should render, including @72. The annotated draft Scene F (anchors 72-79 per its heading) lists rendered lines L71-L76 corresponding to @73-@79. @72 is not addressed in the annotated trace, not listed as a CUT, not listed as a FUSE, and no sentence in the clean Scene F renders a flies-relay-the-reeve beat. The Scene E close ("Then the reeve left." = @70) immediately precedes Scene F's prose, but no fauna-relay beat appears between it and the lord's-man arrival.
  why: @72 carries tens:67 with back=Y — it is part of the active citation graph. The flies-relay-the-reeve beat is the operational transition that closes the surveillance track on the reeve before the lord's-man's arrival opens a new track. Its absence is a coverage gap in the fauna-network operational register. The render-log's "8 anchors" count confirms the fork's intent to render it; its disappearance is unexplained.
  criteria: the rendered prose must surface @72 — the flies registering the reeve's exit — with at minimum the fauna-relay register in Taylor's observational voice. The surface may be compact (a single clause or sentence) and may be folded into the Scene E close or the Scene F open without reordering scenes.
  disposition: prose-surface

---

[SIGNAL] flag-001 — BONE-COVERAGE (trace-reliability)
  what: bone @93 "oc-tanner-father holds the feet [feel:7]" — no explicit trace citation in the annotated Scene H, but a plausible surface exists in the clean draft
  detail: The annotated Scene H trace covers @85-@96 and lists L91 "My father set his eyes on the work and did not lift them to the gate." This sentence renders @93's meaning (father stays put, holds position, does not come to the gate). However, the Scene H trace note does not explicitly cite @93 as FUSE-into-L91 or otherwise account for it. feel:7 at @93 is listed in the cite-index as a lonely entry (no co-location, no inbound license). The sentence at L91 is the natural surface and the feel:7 register (the father's held position as the daughters leaves) is visible in "did not lift them to the gate." The gap is a trace-citation omission rather than a bone-lost.
  why: the annotated draft is the tracing contract that the editor relies on. If @93 has no explicit trace entry, the editor cannot confirm coverage from the annotated alone. No prose change is needed; the trace should note the FUSE relationship.

---

## DIALOGUE-VERBATIM findings (0)

No dialogue facet for s01e01 (pre-2026-05-12 episode). All "speaks to" bones render as silent action per the pre-URI-DIALOGUE-COVERAGE-GATE convention documented in the render-log. No quoted utterances appear in the clean draft body. The preamble is exposition (italic), not character dialogue. Class passes trivially.

---

## EXPOSITION-VERBATIM findings (1 HARD)

Checked all nine exposition entries against the clean draft.

Entries 1-3 (preamble paragraphs): the clean draft preamble matches exposition entries 1-3 verbatim. Note: the annotated draft P1 carries a different rendering ("in a year I would learn was a year before a war" / "Three hundred metres of them, in every direction. The village decided I had come back wrong.") that does not match exposition entry 1. This confirms the annotated draft was generated from a pre-Phase-7 pass; the clean draft is the authoritative surface. Discrepancy is logged at fault-002 (SIGNAL) below.

Entry 4 (@22 log gloss): "scrap parchment my mother had stopped asking about" — clean draft: "scrap parchment my mother had stopped asking about" — verbatim.

Entry 5 (@63 reeve gloss): "Our reeve was the lord's bookkeeper for village debts and the lord's hand for village peace, in that order." — clean draft: "(Our reeve was the lord's bookkeeper for village debts and the lord's hand for village peace, in that order.)" — verbatim (parentheses are renders-as format, not gloss modification).

Entry 6 (@73 lords-man gloss): "Different rank than the reeve, different errand — the lord's-man rode from the lord himself, and his hands were for ink and seals, not ledgers." — clean draft: "Different rank than the reeve, different errand — the lord's-man rode from the lord himself, and his hands were for ink and seals, not ledgers." — verbatim.

Entry 7 (@98 flea-bottom gloss): "into Flea Bottom proper" — clean draft: "into Flea Bottom proper" — verbatim.

Entry 8 (@114 maester gloss): "Maesters were Westeros's scholar-class — half-physician, half-cataloguer, the chained learning the realm ran on." — clean draft: "(Maesters were Westeros's scholar-class — half-physician, half-cataloguer, the chained learning the realm ran on.)" — verbatim.

---

[HARD] fault-002 — EXPOSITION-VERBATIM
  what: exposition entry 9 (@139 Watch gloss) — clean draft modifies the gloss
  detail: exposition entry 9 source gloss: "the gold cloaks, the city's patrol of last resort — their cadence was the city's clock." Clean draft rendering: "the gold cloaks, the city's patrol of last resort, their cadence the city's clock." Differences: (a) the em-dash before "their cadence" is replaced by a comma, altering the gloss's internal structure; (b) the verb "was" is dropped, converting "their cadence was the city's clock" to the noun-phrase "their cadence the city's clock." The render-log records a Phase 7 REWORD for Scene M (NI:37 "pricing" → "reading me" and NI:38 reshown) but does not document a modification to the Watch gloss. No gloss-modification license appears in the annotated trace for this scene. The clean draft integrates the gloss into a longer sentence: "the Watch crossed the Fish Gate margin — the gold cloaks, the city's patrol of last resort, their cadence the city's clock — in what should have been routine cadence." The em-dash pair structure around the gloss is a structural integration move, but the internal gloss text modification (dropping "was" and the dash before "their") exceeds prose-integration license.
  why: the exposition facet is authored as a verbatim-ship surface. Modification without upstream re-author creates a factual-register divergence (the nominal "their cadence the city's clock" is slightly more fragmented than the verbal "their cadence was the city's clock" that exposition:9 was licensed for). The immediately following "The cadence was two beats off" primes on the verb form; the gloss's "was" is load-bearing for that setup.
  criteria: the Watch gloss in the rendered prose must match exposition entry 9 verbatim: "the gold cloaks, the city's patrol of last resort — their cadence was the city's clock." Integration into the surrounding sentence is permitted; internal gloss text must be preserved. If the integration creates a structural problem, the exposition facet source text must be re-authored and re-licensed upstream.
  disposition: prose-surface

---

## NO-INVENTION findings (1 SIGNAL)

Scanned the clean draft for proper nouns, characters, locations, props, conditions, and behaviors not present in the facet graph or licensed exposition.

Characters: Taylor (POV-implicit), father, mother, elder, reeve, lord's-man, maester, dock-runner, neighbour-boy — all in the proto-lines cast or referenced by graph bones. "Tya" is registered via preamble and @11 NI first-mention-legibility.

Locations: tanner village, yard, King's Landing, Flea Bottom, alley, base room, Fish Gate margin, market-side junction, eastern-quarter — all in location-state, loc-state facet, or exposition gloss.

Props: morning bowl, afternoon bowl, salt, log, travel pack, feed bucket, record book — all in proto-lines bones. "Scrap parchment" is licensed by exposition entry 4.

Fauna: flies, beetles, wasps, spiders — series-resident in the proto-lines graph throughout.

Conditions/institutions: the Watch, septon, reeve, maester, lord's-man — all licensed by exposition glosses or proto-lines cast.

---

[SIGNAL] flag-002 — NO-INVENTION (minor, likely graph-resident)
  what: clean draft Scene L renders "the warder's" as attribution for the south-wall footfall — "The beetles relayed a footfall along the south wall: the warder's."
  detail: bone @131 is "the beetles relay the south-wall footfall [narrator:32]." The proto-line carries no attribution for whose footfall it is. The render-log Scene L trace does not document the source for "the warder's." The word "warder" (a building guard or ward-keeper) does not appear in the proto-lines, location-state, or vibes facets for this episode. It is plausibly graph-resident via the Westeros world-building cards (a lodging house in Flea Bottom would routinely have a warder) but is not explicitly cited. The attribution is structurally useful — it distinguishes the footfall from the maester's (who has just been established at the record-table) — but the source is undocumented.
  why: if "warder" is a character name for a recurring walk-on or a prop-condition of the building, it needs to appear in a card or world-build entry before shipping. If it is generic Westeros vocabulary, the exposition note should confirm it as world-build-resident. The structural function is correct; the provenance is untraced.

---

## CONTINUITY findings (1 SIGNAL)

Tense: simple past first-person throughout the body. Preamble uses simple present ("It has been") which is the episode-open register (first-person journal voice); internally consistent within the preamble block, then returns to past for the body. No mid-body tense shifts detected.

Possessive register: natural possessives ("my father," "my mother," "my hands," "my shoulders," "my breath," "my feet," "my gaze," "my hand," "my spine") throughout. The retracted rule (no "the [body-part]" for Taylor-owned body parts) is honored. No possessive-register breaks found in the clean draft.

Pronoun continuity: "He laughed. He wasn't laughing at the room. He was laughing at me." — antecedent is the maester (the last named subject before the laugh, referenced as "He" in the preceding "He spoke aloud"). Resolution is single and unambiguous.

"He spoke to the reeve. The reeve spoke back." (Scene F) — antecedent "He" = lord's-man (introduced in the sentence immediately prior). Unambiguous.

"Then he was gone." (Scene F) — antecedent "he" = lord's-man (last named subject). Unambiguous.

---

[SIGNAL] flag-003 — CONTINUITY (annotated-clean divergence)
  what: the annotated draft renders Scene A L17-L19 differently from the clean draft in a way that introduces a sentence not present in the annotated
  detail: Annotated L17-L19: "My father went still. He kept his eyes on my hands and didn't let his face shift. He'd reached a decision, and he was holding it off his face the way he would for any stranger he hadn't finished working out." Clean draft: "My father stilled. His eyes stayed on my hands and his face didn't shift. He'd reached his verdict. I might as well have been any stranger he was still working out." The clean draft contains "I might as well have been any stranger he was still working out" — a sentence absent from the annotated. This sentence renders @14 feel:5 / narrator:41 register but is not traced in the annotated. It is an additional Phase 7 surface-level addition that was not logged in the render-log's Phase 7 move tally (which records only 5 REWORDs). The sentence is bone-faithful (it renders the father-verdict beat at @14) but its provenance is untraced.
  detail-2: the annotated draft P1 preamble diverges substantially from the clean draft preamble (documented at EXPOSITION-VERBATIM — annotated P1 uses "a war" not "the Dance of the Dragons" and adds "in every direction" and "The village decided I had come back wrong"). These differences confirm the annotated was not regenerated after Phase 7 finalized the clean draft. The annotated is an unreliable tracing document for any sentence-level provenance check.
  why: the editor reads the annotated for bone-trace provenance when making allowed-moves. If the annotated does not match the clean, the editor may mis-trace a sentence or fail to protect a bone-carry. The gap is not a prose-surface problem but a tooling-reliability problem for the Phase 3 pass.

---

## BLOCKING findings (1 SIGNAL)

Spatial relations checked against location-state.md and proto-lines.

Taylor's location arc: tanner village (Scenes A-H) → road → loc-flea-bottom (Scene I @98) → loc-flea-bottom-base (Scene I @103) → loc-flea-bottom-base perimeter (Scenes J-L) → loc-flea-bottom (Scenes M-N). All transitions are bone-anchored and present in rendered prose.

Father: tanner village throughout. State confirmed — enters yard at @19, assigned task at @48. Leaves the gate scene at his work, not at the gate. Matches L91.

Mother: tanner village throughout. Exits room at @46 (state:27), faces door at @92 (feel:9). Both rendered.

Elder: walks road with Taylor at @95-@96. Reappears at @148 "the elder came back." Scene I rendered prose does not explicitly position the elder within loc-flea-bottom-base or any specific scene I location, which is consistent with his bones (@95-@96 road-walk, then absent until @148).

---

[SIGNAL] flag-004 — BLOCKING (minor)
  what: clean draft Scene I renders "The morning was still on the alley when we got there, the sun barely over the rooflines" — the "we" implies the elder is co-present at the alley mouth arrival
  detail: bones @95 (oc-tanner-elder walks the road) and @96 (taylor walks the road) establish both walking together. Bone @98 is "taylor enters loc-flea-bottom." The elder has no loc-state entry placing him in loc-flea-bottom in Scene I, and he has no scene I proto-lines bones. The "we got there" in the clean draft implies shared arrival but the elder's presence in the scene is unregistered in the state facets. The elder next appears at @148. This is consistent with the elder walking Taylor to the location and departing — but the elder's departure from the alley is not bone-anchored in scene I, and "we got there" stages him in scene I against the loc-state record.
  detail-2: this sentence ("The morning was still on the alley when we got there, the sun barely over the rooflines") does not appear in the annotated draft at all, confirming it was added during or after Phase 7 without explicit logging. It is consistent with loc-state:1 (morning) and sensory:4 (flea-bottom-density-compound tag) but the "we" co-presence is not in any of those sources.
  why: if the elder's loc-state is ever back-checked for scene I (e.g., in a continuity check for a later episode where the elder's KL arrival timing matters), the "we got there" surface implies a simultaneous arrival not recorded in the state facets. Minor continuity risk for downstream episodes; not a blocking fault in s01e01 itself.

---

## SCENE-MAP-RESPECT findings (0)

Checked scene ordering and boundaries against scene-map-s01e01.md (13 scenes A-N, G skipped).

Clean draft structure (by --- separator blocks): preamble → A (waking) → B (yard-map) → C (mother sings) → D (task) → E (reeve) → F (lord's-man) → H (routing) → I (FB entry) → J (perimeter) → K (full perimeter) → L (the laugh) → M (Watch/runner) → N (commit). Order is monotone and matches the scene-map exactly.

Scene F (anchors @72-@83) and the G-skip: the render-log fused the Scene F and nominal-G beats into one fork, correctly. The scene-map documents G-skip with label-order WARN-SCENE-MAP-LABEL-ORDER (advisory only per schema). The rendered prose shows no G-labeled section and no merged content that crosses a scene-map boundary.

Protected patterns verified in clean prose:
- log-trio @21-@23 (Scene A) — rendered as "I opened the log — scrap parchment my mother had stopped asking about. I wrote down the salt. I didn't write what it had cost my mother. I closed the log." The log-trio cadence is present (open / write / close), though the write-step is split into two sentences with the first-mention gloss folded at "open." The three-step cadence is honored.
- three-note buildup @39-@41 (Scene C) — "The first note was a song Tya knew. The spiders in the rafters didn't know it. She sang the second. She sang the third —" — buildup present and interrupted at the peak.
- threshold-cross @90 (Scene H) — "The gate was the last threshold that cost nothing to cross." — verbatim per NI:23 protection.
- departure-trio @91-@93 (Scene H) — pack-lift, mother faces door, father holds — all three rendered at L87/L88-L90/L91.
- road-walk-pair @95-@96 (Scene H) — "The elder walked the road. I walked the road." — verbatim pair preserved.
- doubled-walk @28+@30 (Scene B) — "I walked the boundary. [...] I walked the boundary again." — preserved.
- three-beat anaphora @124 (Scene K) — "the corners gave me the shelf, the corners gave me the page, the corners didn't give me the words." — verbatim.
- doubled-register laugh-and-silence @133-@134 (Scene L) — "He laughed. He wasn't laughing at the room. He was laughing at me. / The beetles fell silent. The silence was the shape of what he'd just looked at." — preserved.
- log-trio at Scene L close (@135-@137) — "I opened the log. I wrote the entry. I closed the log." — verbatim three-step.
- log-trio at Scene N close (@157-@159) — "I exhaled. I opened the log. I wrote it down. I closed the log." — four-step (exhale folded in); the open/write/close triad is present within the four-step.

No scene reordering, no merged scenes, no protected-pattern abolition detected.

---

## EARTH-BET-HARD-FENCE findings (0)

Full clean draft scanned for the Earth-Bet proper-noun fence list: Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil, Tattletale, Bitch, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea.

Zero hits. The fence holds.

---

## Audit summary

verdict: HARDS-PRESENT
HARD: 3
SIGNAL: 4

Per-class breakdown:
- BONE-COVERAGE: 1 HARD (fault-001 @72), 1 SIGNAL (flag-001 @93)
- DIALOGUE-VERBATIM: 0
- EXPOSITION-VERBATIM: 1 HARD (fault-002 @139 Watch gloss)
- NO-INVENTION: 1 SIGNAL (flag-002 "warder" attribution)
- CONTINUITY: 1 SIGNAL (flag-003 annotated-clean divergence)
- BLOCKING: 1 SIGNAL (flag-004 "we got there" elder co-presence)
- SCENE-MAP-RESPECT: 0
- EARTH-BET-HARD-FENCE: 0

classes with findings: BONE-COVERAGE, EXPOSITION-VERBATIM, NO-INVENTION (SIGNAL), CONTINUITY (SIGNAL), BLOCKING (SIGNAL)
classes clean: DIALOGUE-VERBATIM, SCENE-MAP-RESPECT, EARTH-BET-HARD-FENCE

editor disposition: blocked pending HARDs — both are prose-surface and within editor allowed-moves:
  - fault-001 (@72 BONE-COVERAGE): a single-clause fauna-relay beat (the flies tracking the reeve's exit) folded into the Scene E close or Scene F open. One sentence, no plot invention, no scene boundary crossing. Editor scope: paragraph adjustment.
  - fault-002 (EXPOSITION-VERBATIM @139 Watch gloss): the verb "was" must be restored and the em-dash structure re-established inside the existing sentence frame. Editor scope: prose-surface correction within the existing sentence structure. If the integration sentence resists verbatim embedding, the exposition facet requires upstream re-authoring.

The four SIGNALs are advisory for the editor's Pass C:
  - flag-001 (@93 trace): no prose change needed; annotated draft trace should note @93 FUSE-into-L91.
  - flag-002 (warder): if the editor cannot confirm graph-residency from the world-build cards, replace "the warder's" with a description that is clearly world-build-licensed ("the patrol's", "the building's third-lap count").
  - flag-003 (annotated-clean drift): the annotated is unreliable as a sentence-level tracing document. Editor should bone-walk against the proto-lines directly rather than relying on the annotated for any sentence not explicitly labeled with a line-ID in the annotated.
  - flag-004 ("we got there"): if the elder's loc-state at KL arrival is materially relevant to downstream episodes, "we got there" should be replaced with "I got there" or the elder's Scene I co-presence should be registered in the state facets. If not downstream-relevant, note and pass.

recommended fixer routing: not needed. Both HARDs are within the editor's allowed-moves contract (paragraph adjustment, verbatim-gloss restoration). No structural invention, no scene reorder, no plot change required by any finding.
