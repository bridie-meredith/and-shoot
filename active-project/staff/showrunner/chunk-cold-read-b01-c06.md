# chunk cold-read — b01-c06 — /and-substance chapter Phase 5.5 (PROP-0019 / PROP-0019-A)

**Date:** 2026-05-29
**Reader:** naive-reader fork (general-purpose, no substance context — prose-only)
**Input:** the 4 scene-chunk prose blocks (scene_conflict + dramatic_shape + goal + chunk narrative), substance_delta/axes/cost-ledger withheld.

## Verdict: PASS-CHUNK   (voice_risk: false)

Reader recovered plot + agency + delta + stakes + turn, would continue, AND neither voice-density signal fired. Clean.

## Reader answers (Q1–Q7)

1. **Plot (recovery):** PASS. "A woman in a poor ward is approached by a stitch-house girl (Wren) she's observed but never spoken to. Wren asks her to find a missing younger girl. The narrator has an ability to sense/read people across the city, and a personal rule against using it to direct/interfere. She breaks the rule, locates the girl (safe at a cousin's two wards over), reunites them, then privately reckons with having made the first self-chosen exception to her own most important rule."
2. **Agency:** PASS. "The narrator's. Wren initiates, but the chapter pivots entirely on the narrator's choice to say yes — emphatically her agency ('I made it myself')."
3. **Delta:** PASS. "Crossed a line she'd been holding. Start: inviolable rule + untouched distance. End: used the ability on a person by choice, formed a real connection with Wren, and acknowledged the rule is now breachable — 'the rule has a door in it now.'"
4. **Stakes:** PASS (read on implication, correctly). "Immediate stakes (missing child) resolve easily — clearly not the point. The real stake is the rule and what its breach foreshadows: a slippery slope, which the narrator herself signals ('I cannot pretend the hinge will rust shut'). Faint menace around 'Otto'."
5. **Turn (peak):** PASS. "Clearly Scene 2, the 'I say yes' moment. Marked explicitly: 'the first time I have ever said it on my own.' Scene 4 is the aftershock."
6. **Gaps:** "Mostly intentional withholding rather than sloppiness: (a) ability-mechanics deliberately vague — reads as established-elsewhere, not frustrating; (b) 'Otto' dropped with no context — the one proper noun that felt walked-in-late; (c) why the rule matters ('carried across an ocean of my own making') is evocative but opaque — backstory felt in shape, not substance; (d) the missing-girl plot resolves so easily there's almost no external tension — all tension is internal/moral." Reader classified all as intentional, not confusion.
7. **Continue:** YES. "The premise — a powerful person doing a small wrong for a good reason and knowing it's the first step toward something worse — is a genuinely compelling moral hook; the last line is a strong ominous button. The controlled, intelligent voice earns trust the slope will be paid off."

## Voice-density guard (Step 2.5 — PROP-0019-A)

- **Signal A (excused-confusion): NOT FIRED.** The reader recovered the central event from the concrete prose narrative itself, not from outline/summary phrasing a scene can't reproduce. The central-event clarity does not depend on summary charity.
- **Signal B (abstraction-dense central event): NOT FIRED.** The chapter's central event (the spoken yes in s02; the directed reading in s03) is rendered as concrete actor-verb-object, not instrument/process abstraction. s03's directed reading is staged physically ("a small body with the right weight and the right favoring of one arm, sitting against a wall beside an older woman"), the opposite of the c05 "the categorization held" register.

## Routing consequence

- PASS-CHUNK → proceed to Phase 6 persist.
- `chapters[b01c06].chunk_cold_read = { verdict: PASS-CHUNK, voice_risk: false, ts: 2026-05-29 }`.
- `/and-stitch` Phase 8.5 central-event-muffle check is **NOT armed** for c06 (arming requires PASS-CHUNK-VOICE-RISK).

## Live-validation note (c06 vs c05)

c05's retroactive Phase 5.5 rerun returned **PASS-CHUNK-VOICE-RISK** (Signals A+B fired; armed the muffle check). c06, authored after the overhaul with the screen-writer briefed to keep the central event concrete, returns a clean **PASS-CHUNK** on first pass — the gate distinguishes the two chapters correctly. First live firing of Phase 5.5: it ran, classified, and did not false-positive on an intentionally concrete chunk.
