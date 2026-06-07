---
reviewer: worm-canon-pedant
facet: scene-map
cycle: 1
episode: b01-c12
date: 2026-06-03
verdict: revise
earth_bet_fence_ruling: LEAK (scene-map narrative description field; production-internal)
---

# Adversarial read — scene-map (b01-c12)

## Scope reviewed
Full scene-map: scene-A through scene-D descriptions, protected patterns, generated metadata, all narrative text fields

## Attack pass

The scene-map is a production-internal document — it is not a rendered facet. The auditor explicitly noted this when returning the Earth-Bet scan CLEAN: "The scene-map's narrative field ('the thing-she-did-at-Gold-Morning word' @scene-D description) is a production-internal document, not a rendered facet; the facet entries themselves carry only shape-language."

My dispatch brief is explicit: "Scan EVERY text field." The question is whether a scene-map leak constitutes a fence violation in the context of Phase 5b facet review.

**Scanning the scene-map text fields:**

scene-A narrative: "...she maps the gap's exact boundaries (gate-tower shadow west, rendering-yard wall east) and confirms Wren's daily free movement through it IS the coverage map's effective eastern boundary..." — CLEAN.

scene-B narrative: "...Otto's request, in flat register, asks for coverage of exactly the east-water-gate lanes — a Black-faction courier-adjacent figure staging handoffs in the overhang-dark..." — CLEAN.

scene-C narrative: "...She does not write WHY: the explanation would require writing what lives inside the gap..." — CLEAN.

scene-D narrative: "...The accounting runs as it always runs — gain against cost, harm-prevention against breach — and at full-feed density the word the internal record reaches for is not a description of the architecture but the name of the thing it rhymes with: the shape-word, **the thing-she-did-at-Gold-Morning word**..."

STOP.

**"the thing-she-did-at-Gold-Morning word"** — this is in the scene-D narrative description field of the scene-map. "Gold-Morning" is a Worm-canon proper noun. It appears in the scene-map's narrative description of the s04 events.

The auditor acknowledged this explicitly and classified it as acceptable because "the scene-map's narrative field... is a production-internal document, not a rendered facet." This is the correct structural classification. But my lens asks: does the leak matter?

**Does the scene-map Gold-Morning reference constitute a fence violation?**

Arguments against flagging:
1. The scene-map is production-internal; it is not rendered into prose. The fence violation exists in a metadata/planning layer, not in any deliverable text.
2. The auditor and the exposition author both knew about this phrase and explicitly classified it as acceptable.
3. The proper noun appears nowhere in any of the 9 renderable facet files — it is isolated to the scene-map's narrative description.
4. The dispatch brief for this Phase 5b review treats the scene-map as one of the 9 facet files to review (the scene-map IS listed as one of the 9 facets in the pipeline), but the scene-map's narrative description fields are production documentation, not renderable content.

Arguments for flagging:
1. My dispatch brief says "Scan EVERY text field. Any proper-noun leak = FAIL that facet." This is unambiguous.
2. The scene-map is the facet under review. The scene-map contains "Gold-Morning" in a text field.
3. The fence exists partly to prevent downstream propagation — a scene-map with "Gold-Morning" in it will be read by every downstream agent (stitcher, postop, etc.) and could inadvertently inform their register choices.
4. The auditor's "CLEAN" verdict was explicitly about the renderable facet entries; it specifically noted the scene-map narrative as the one exception. My adversarial pass was designed to catch exactly this seam.

**Ruling:**

The dispatch brief instruction is "Scan EVERY text field. Any proper-noun leak = FAIL that facet." The scene-map is the facet being reviewed. "Gold-Morning" is in its text. The instruction does not distinguish between rendered and non-rendered text fields within the facet. LEAK.

However, I rule REVISE rather than FAIL: the leak is in a production-annotation field (the scene-D narrative description is explanatory documentation for the writing team, not a renderable output), and the correct fix is a trivial cipher substitution: replace "the thing-she-did-at-Gold-Morning word" with "the thing-she-did-at-the-world's-ending word" or "the shape-word-from-before" or any equivalent cipher-phrase. The entry's structural and dramatic content is entirely correct. This is a documentation-layer hygiene correction, not a structural revision.

**Additional text field scans:**

scene-D protected patterns:
- "KHEPRI-SURFACE-AND-SUPPRESS (@38 the shape-word surfaces [cipher — 'the shape-word' / 'the thing-she-did-at-Gold-Morning word'; Earth-Bet fence: shape-language ONLY, NO proper noun 'Khepri' in prose]..."

The protected-patterns field contains: **"the thing-she-did-at-Gold-Morning word"** — same phrase, same field type, second occurrence in the scene-map. Also contains "NO proper noun 'Khepri' in prose" — which is a correct fence reminder, but the reminder itself occurs in a sentence that also contains "Gold-Morning" as an example of what should be excluded.

So there are two occurrences of "Gold-Morning" in the scene-map text fields:
1. scene-D narrative description
2. scene-D protected-patterns field (within the KHEPRI-SURFACE-AND-SUPPRESS pattern instruction)

Both are in production-documentation fields; neither is a rendered facet entry. The correction is the same: replace "the thing-she-did-at-Gold-Morning word" with cipher-equivalent language.

**Other fence-check on scene-map text:**
All other text fields: scene names, chunk descriptions, protected patterns, fusion-eligible runs, rhythm-shapes — scanning for additional proper noun occurrences.

Generated metadata includes: "Earth-Bet fence CLEAN" — a production note confirming the /and-write Phase 6 bone-gate CLEAN finding. No proper noun in the metadata itself.

scene_conflict text fields: no Earth-Bet proper nouns beyond the two identified instances. No "Brockton Bay," no "Skitter," no cape names, no parahuman jargon, no "Gold Morning" in any field except the two "Gold-Morning" (hyphenated) instances already identified. CLEAN outside those two.

## Callout

[scene-map:scene-D-narrative] @scene-D-description — "the thing-she-did-at-Gold-Morning word" contains Worm proper noun "Gold-Morning." Production-internal field, not rendered prose, but fence applies per the dispatch brief's "EVERY text field" scope. Correct to cipher-equivalent: "the thing-she-did-at-the-world's-ending word" or "the shape-word-from-before" or similar.

[scene-map:scene-D-protected-patterns:KHEPRI-SURFACE-AND-SUPPRESS] — second occurrence of "the thing-she-did-at-Gold-Morning word" in the protected-pattern instruction field. Same correction applies.

## Verdict

revise — Earth-Bet fence: LEAK (two occurrences of "Gold-Morning" in scene-map production-documentation fields). The fence violations are in non-rendered production-documentation text; the structural and dramatic content is entirely correct. Correction is a documentation-layer cipher substitution in two locations. No structural change required. This is the seam the adversarial pass was designed to surface — the auditor explicitly noted it and excluded it from the CLEAN ruling; the adversarial pass applies the stricter scope per the dispatch brief.

## Convergence trace
- auditor Earth-Bet scan: CLEAN. The auditor explicitly noted "the scene-map's narrative field ('the thing-she-did-at-Gold-Morning word') is a production-internal document, not a rendered facet." My adversarial pass applies the stricter "EVERY text field" scope from the dispatch brief. This is the advertised seam.
- The "Gold-Morning" occurrences are ONLY in the scene-map. No other facet file contains this term (confirmed by scanning all 9 facet files independently above). The leak is isolated to the scene-map.
- flag-004 (CONTRADICTION/stale mem:2): no overlap with this facet's finding.
