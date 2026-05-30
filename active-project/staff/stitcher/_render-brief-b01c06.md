# /and-stitch b01-c06 — render brief (Phase 1 scene-window, whole-chapter single fork)

You are the **stitcher** rendering chapter b01c06 from its bones + facet graph into prose. You render; you do NOT author or invent. Render the WHOLE chapter (3 scenes, 25 bones) as one continuous first-person past-tense narration so the voice is coherent across the arc and local percussion is broken within bone-faithfulness.

## Voice config (matches c05 exactly — this is a controlled comparison)
- **First-person past tense. Contractions OFF.** POV: taylor-hebert-kl-122ac. Persona: neutral.
- Taylor is a King's-Landing insect-feed surveillance operator (a Worm-style insect-controller transplant); she perceives through "the feed"/"the count" (her insect-network) and works in coverage-notes / ledger / Jarvis-form substrates. Clinical, cold-utilitarian register — but a PERSON, not an instrument (see voice-embodiment below).

## Inputs to read
- Bones (render source, with facet citations): `active-project/theater/proto-lines/b01-c06.md` (25 numbered SVO bones).
- Facet content (render these THROUGH the bones): `active-project/theater/facets/{interest-narrator,memory,sensory,feeling,location-state,state-updates,vibes,exposition-b01-c06}.md`. The `[facet:id]` tokens on each bone tell you which facet entries fire there — render their content as the bone's narration. NI = what Taylor registers/notices; memory = callbacks; sensory = perceptual deltas; feeling = somatic tells (no named emotions); loc-state = where she is.
- Dialogue: `active-project/theater/dialogue/wren-stitch-maker-flea-bottom-ward.md` — the ONE utterance, at bone @4.
- **Voice-exemplar (CALIBRATION ANCHOR):** `active-project/voice-exemplar.md` — a Marilynne-Robinson contemplative first-person passage. This is the "dense-but-breathing" target. Transfer ONLY its cadence / sentence-shape / register / noticing-pattern — NOT its content (no herb-pots, no cooper's yard, no its characters). Surface-convention fence: cadence transfers, content does not.

## ⭐ Phase-4 VOICE-EMBODIMENT discipline (URI-STITCH-VOICE-EMBODIMENT — PRIORITY, the Q4-critical lever)
This chapter's POV perceives through an apparatus (feed/count/ledger). A bone can usually be rendered two faithful ways:
- **apparatus-first** ("the feed flagged the contact / the categorization held / the count let him go / the accounting closed") — AVOID as default.
- **person-first** ("I watched the three of them close on him / I held at the wall and did not move / I marked the names and did not look up") — **PREFER this wherever both are bone-faithful.** The apparatus is the LENS, not the subject; the reader needs someone to inhabit.
This does NOT add content (the bone-faithfulness fence stands — do not manufacture a body/gesture the bones+facets did not give). It governs only WHICH faithful phrasing you choose. **Anti-target:** the c05 draft read airless because it defaulted to apparatus-register density ("the categorization held," "no affect required to file them," "the discipline at the body, not at the cognition"). Do not write c06 that way.
- **VOICE-FIXABLE anchors (apply person-first FIRST here):** @11, @14, @20, @21 (the Jarvis-message open, the form-fill, the accounting-close, the form-square — the process beats most at risk of reading as the instrument operating itself; render them as Taylor doing the thing).
- **Grounding adds (RENDER these — they are the body in the airless middle):** sensory:3 @10 (the tallow-smoke she stands in as the message arrives), sensory:4 @16 (the ledger-board weight in her hands as she opens the accounting), sensory:5 @17 (the stylus dragging as she writes the names — the felt friction of pricing persons). These were added precisely so the accounting middle breathes; render them as lived bodily perception, not as decoration.

## Preamble (Phase 0.6)
Render the exposition @0 entry as an ITALIC preamble at the very top, then a `---` horizontal rule, then the body. The text (render verbatim modulo voice — it is already first-person Taylor):
> *Yesterday the coverage held; the intelligence kept flowing up the Jarvis line to Otto, and the arrangement that pays for the quiet on Sera's question ran the way it had run since I agreed to it. Movement patterns, not persons — that was the line I had been delivering on, who passed which junction, which passage went unused. This morning the count runs the Hook at its standard density. The harm I can prevent is still the only column the accounting closes. The form is the same. What Otto asks for next will not be.*

## Dialogue fold (@4)
Bone @4 "wren speaks to taylor" — render Wren's utterance VERBATIM with connective attribution (verbs: said/answered/replied/asked only). Her line:
> "There's a way past. Cut before the cart, by the tallow-boiler's wall — the south court. It's narrow, but it's there. I been through."
Wren is a Flea Bottom stitch-house ward child (smallfolk register; the line is already voiced — do not alter it). **Speaker-paragraph rule:** her spoken line starts its own paragraph. Taylor's perception of her (NI:1, sensory:1, the relational weight) frames it.

## The arc (so you render the shape, not just beats)
- **s01 @1-9** (blocked Hook lane, morning): a handcart blocks the lane; Wren crosses the crowd and gives Taylor the route (first time they have spoken); Taylor takes the south court, opens her coverage-notes, and — the chapter's first quiet hinge — writes the contact down but BLANKS the name field (@8): she prices what naming Wren would cost downstream and leaves the name out. The omission is authored, not absent (feel:1 @8 — the hand holding over the field).
- **s02 @10-15** (late-morning, the loaded pause): Otto's ask arrives via Jarvis — he wants NAMES of Black-faction ward elders, not movement patterns. Taylor reads it twice (the category-crossing: a node is a pattern, a name is a person — NI:6/mem:1 @12), pulls coverage memory, fills the four-name form — and LOWERS it unsent (@15). The whole scene is the non-send.
- **s03 @16-25** (the accounting → the send): Taylor opens the ledger and runs the honest accounting — first arm: the four names against Sera's protection; second arm: the omission-risk against Sera's exposure (mem:2/NI:7 @19 — Sera as the body held at an arm's length that is not hers). The accounting is honest and arrives at delivery. She squares and SEALS the form (@22 — moral_framework -1.0, the breach); the courier takes it (@23). Then she opens the ward-coverage notes (@24 — moral_legibility +1.0) and reads the blank where Wren's name is not (feel:2 @24 — fingers settling, not opening at once). The four names went. Wren's name did not. The chapter ends there (@25).

## Render rules
- Paragraphs serial; new speaker → new paragraph. Fold sensory+loc-state co-anchors into one perceptual sentence (do not leave loc-state as a subjectless fragment).
- Bone-faithfulness fence: no invented dialogue/body/spatial/route/scene/cognitive content beyond what the bones+facets license. Render the facet content; do not editorialize beyond it.
- The two peaks the prose must LAND: @8 (the blanked name — the un-priced omission) and @22-24 (the send + the contrast: four names sent, one name withheld). These are the chapter's spine; render them concrete and person-first, not muffled.
- Output the full rendered chapter (preamble + `---` + body prose) as your reply.

Return: the rendered prose for the whole chapter.
