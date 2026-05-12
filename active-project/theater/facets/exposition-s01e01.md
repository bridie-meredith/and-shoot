facet: exposition
episode: s01e01
author: exposition-author (hand-authored; merged from Phase 1 + Phase 2 dogfood + reader-feedback iteration 2026-05-12)
audience-modeled-against: [cape-fic-reader, dark-fantasy-reader, worm-canon-pedant]
---

# Episode-open scopes (render before body, italic)

1 @0 episode-open-preamble: "I had won my world by becoming a hive of bugs, and I had not meant to wake. Three days later I woke anyway, in another body — a tanner's daughter dead of fever, in a village outside a king's city, the year before the Dance of the Dragons. The bugs came with me. Three hundred metres of them." | scope: episode-open-preamble | renders-as: italic-preamble | sources: series-plan.plot.start, series-plan.protagonist_arc, world-build:taylor-300m-sphere-flea-bottom-scope, episode.chunk | licensed-by: cape-fic-doesnt-know-Khepri-ending, dark-fantasy-doesnt-know-Worm-protagonist-arc, worm-canon-needs-Westeros-frame

2 @0 episode-open-context: "It has been a month since the fever. My parents have not asked me to leave and have not called me by my name. The bowls keep arriving on the table. The dogs do not come to my hand. I have spent the time learning what the body can do — what it remembers without being told, what it does not — and writing in a log nobody else can read." | scope: episode-open-context | renders-as: preamble-paragraph | sources: series-plan §s01-chunk, cond-crownlands-superstition-frame-125ac §the-tanner-family-situation, cond-clinical-self-erasure §the-log-as-instrument | licensed-by: cape-fic-and-worm-canon-need-grief-debt-frame, dark-fantasy-borderline-but-the-bowl-rhythm-anchors-the-meal-context-without-separate-gloss | derived-from: Phase-2-dogfood-paragraph-2 (transposed to first-person per profile voice=pov-frame; replaces the prior summary-form "first month had been awkward" hand-authored paragraph because Phase 2's concrete behavioral facts read story-grounded rather than recap-style)

3 @0 episode-open-context: "The septon denied a miracle. My parents settled on 'falsely declared dead.' The village settled on 'Tya who came back wrong.' They weren't wrong about the wrong part." | scope: episode-open-context | renders-as: preamble-paragraph | sources: cond-westerosi-superstition-frame-125ac, cond-crownlands-superstition-frame-125ac §the-stranger-leavings-frame, cond-feudal-hierarchy-law, series-plan.plot.start | licensed-by: all-personas-need-resurrection-mechanism-glossed (waking-in-dead-body would cause riot/exile/sanctification in any plausible world; the gloss explains why the family/village absorbed it instead of erupting; Phase 2 dropped this content but the mechanism is structurally required and the previous paragraph leaves the question open)

# First-mention scopes (fold in at anchor per renders-as)

4 @22 log: "scrap parchment my mother had stopped asking about" | scope: first-mention-object | renders-as: em-dash-fold | sources: cond-clinical-self-erasure §the-log-as-instrument, world-build:tanner-village-literacy-economy | licensed-by: all-personas-encounter-the-log-without-context (object is series-specific; cape-fic doesn't read research-register, dark-fantasy doesn't know the habit-from-before, worm-canon-pedant needs the Khepri-descendant-instrument frame grounded in the new context)

5 @63 reeve: "Our reeve was the lord's bookkeeper for village debts and the lord's hand for village peace, in that order." | scope: first-mention-term | renders-as: parenthetical-aside | sources: cond-feudal-hierarchy-law, cond-westerosi-customary-authority-125ac | licensed-by: cape-fic-doesnt-know-Westerosi-feudal-roles, worm-canon-doesnt-know-village-reeve-specifically

6 @73 lords-man: "Different rank than the reeve, different errand — the lord's-man rode from the lord himself, and his hands were for ink and seals, not ledgers." | scope: first-mention-term | renders-as: post-bone-clause | sources: cond-feudal-hierarchy-law, cond-westerosi-customary-authority-125ac | licensed-by: all-personas-need-disambiguation-from-reeve (the prior gloss at @63 establishes reeve; lord's-man arrives 10 anchors later and risks conflation)

7 @98 flea-bottom: "into Flea Bottom proper" | scope: first-mention-place | renders-as: em-dash-fold | sources: world-build:kings-landing-flea-bottom, world-build:kings-landing | licensed-by: cape-fic-and-worm-canon-dont-know-Flea-Bottom-as-slum-district (NI:25 establishes King's-Landing-as-named-city; this entry adds the slum-district granularity NI:25 does not carry)

8 @114 maester: "Maesters were Westeros's scholar-class — half-physician, half-cataloguer, the chained learning the realm ran on." | scope: first-mention-term | renders-as: parenthetical-aside | sources: world-build:westeros-maesters, cond-westerosi-customary-authority-125ac | licensed-by: cape-fic-and-worm-canon-dont-know-maester-institution

9 @139 the-Watch: "the gold cloaks, the city's patrol of last resort — their cadence was the city's clock" | scope: first-mention-term | renders-as: em-dash-fold | sources: world-build:kings-landing, cond-westerosi-customary-authority-125ac | licensed-by: cape-fic-and-worm-canon-dont-know-Gold-Cloaks (Phase 2's "their cadence was the city's clock" register added because it primes Taylor's "the cadence was two beats off" beat that follows immediately)

# Scene-open-orient scopes (conditional fire per schema § scene-open-orient fire-rule)

# Fire-audit per scene-boundary (s01e01 has time-skip blanks at IDs 24, 35, 47, 62, 71, 80, 84, 97, 108, 119, 128, 138, 147, 156):
#   @25  time-skip ✓ | loc-state ✗ | NI@first-2: NI:8@26 (operational, not time/place) — FIRES
#   @36  time-skip ✓ | loc-state ✗ | NI@first-2: none in @36-37 — FIRES
#   @48  time-skip ✓ | loc-state ✗ | NI@first-2: none in @48-49 — FIRES
#   @63  time-skip ✓ | loc-state ✗ | NI@first-2: NI:15@63 carries place-shift (back-gate-up-list) but no time-shift — FIRES (time-marker needed)
#   @73  time-skip ✓ | loc-state ✗ | NI@first-2: NI:17@73 carries situational-weight but no time-shift — FIRES
#   @85  time-skip ✓ | loc-state ✗ | NI@first-2: NI:19@85 carries elder-tone but no time — FIRES (overnight-marker structurally needed)
#   @98  time-skip ✓ | loc-state:1@98 fires (morning/district-open/alley-mouth-ahead) ✗ | — REFUSES (loc-state carries time + place; scene-orient would be wallpaper)
#   @109 time-skip ✓ | loc-state ✗ (loc-state:2 fires at @103 not @109) | NI@first-2: none in @109-110 (NI:28@110 is operational not time) — FIRES
#   @120 time-skip ✓ | loc-state ✗ | NI@first-2: none in @120-121 — FIRES (extended-interval-marker)
#   @129 time-skip ✓ | loc-state ✗ | NI@first-2: none in @129; NI:31@130 carries situational not time — FIRES
#   @139 time-skip ✓ | loc-state ✗ (loc-state:3 fires at @152 not @139) | NI@first-2: NI:35@139 carries situational not time — FIRES
#   @148 time-skip ✓ | loc-state ✗ at @148 | NI@first-2: none in @148-149 — FIRES
# Total: 11 fires, 1 refusal.

10 @25 scene-open-orient-b: "After breakfast I went out to the yard." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-A-close-was-log-write, episode.chunk | licensed-by: all-personas-need-time-and-place-shift-from-indoor-table-to-outdoor-yard

11 @36 scene-open-orient-c: "Mid-morning, my mother came back in." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-B-close-was-outdoor-yard, episode.chunk | licensed-by: all-personas-need-time-shift-plus-location-shift-back-indoor

12 @48 scene-open-orient-d: "By afternoon, my father gave me the yard-edge task" | scope: scene-open-orient | renders-as: scene-bridge | sources: episode.chunk | licensed-by: all-personas-need-time-marker

13 @63 scene-open-orient-e: "Before sundown, the reeve came through the gate." | scope: scene-open-orient | renders-as: scene-bridge | sources: episode.chunk | licensed-by: all-personas-need-time-marker (combines with first-mention-reeve entry 5 at same anchor; per-anchor-cap allows scene-orient + first-mention pair)

14 @73 scene-open-orient-f: "Not long after, the lord's-man came through the gate at a parade beat." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-E-close-was-reeve-leaves | licensed-by: all-personas-need-temporal-link-to-prior-scene (combines with first-mention-lords-man entry 6 at same anchor)

15 @85 scene-open-orient-h: "The next morning, the elder came." | scope: scene-open-orient | renders-as: scene-bridge | sources: episode.chunk, time-skip-blank-at-84 | licensed-by: all-personas-need-overnight-marker (the longest time-skip in the episode; without this the reader places the elder's arrival same-evening rather than day-2-morning)

16 @109 scene-open-orient-j: "Once the pack was down, I walked the perimeter." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-I-close-was-pack-set | licensed-by: all-personas-need-causal-link (the perimeter-walk follows the pack-set, but the time-skip blank means a paragraph break separates them; the bridge clarifies continuity)

17 @120 scene-open-orient-k: "I walked the full perimeter." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-J-close-was-listening-from-base | licensed-by: dark-fantasy-and-cape-fic-need-extended-interval-marker (Scene K is the "later, more comprehensive perimeter walk" beat — the "full" qualifier vs Scene J's "perimeter" suffices as the bridge)

18 @129 scene-open-orient-l: "By evening the maester crossed the room above mine." | scope: scene-open-orient | renders-as: scene-bridge | sources: episode.chunk, prior-scene-K-was-base-survey | licensed-by: all-personas-need-time-shift-plus-vertical-spatial-marker (the maester's room is *above* Taylor's; without "above mine" reader places maester elsewhere)

19 @139 scene-open-orient-m: "Down at street level," | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-L-was-upstairs-listening | licensed-by: all-personas-need-elevation-shift-marker (Taylor moves from second-floor-room to ground-level junction)

20 @148 scene-open-orient-n: "Within the hour, the elder came back, this time with the dock-runner." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-M-close-was-runner-pivot | licensed-by: all-personas-need-temporal-marker-plus-elder-return-marker

# Cross-episode register (write-back at facet-close)

# After this episode lands, the following keys promote to active-project/staff/exposition-author/glossed-terms.md:
# - log | first-mention-anchor: @22
# - reeve | first-mention-anchor: @63
# - lords-man | first-mention-anchor: @73
# - flea-bottom | first-mention-anchor: @98
# - maester | first-mention-anchor: @114
# - the-Watch | first-mention-anchor: @139
# - kings-landing | first-mention-anchor: graph-resident-via-NI:25 (NOT exposition-glossed; recorded here so future-episode exposition-author knows the term is reader-resident via lens-facet)
# - tya | first-mention-anchor: graph-resident-via-preamble-paragraph-1 (the body, the name)

# Notes

This file is the merged version of three concurrent authoring runs:
1. Hand-authored from inline glosses landed in s01e01 polish during 2026-05-12 reader-feedback iterations.
2. Phase 1 dogfood (exposition-author with no lens facets) — produced 25 entries.
3. Phase 2 dogfood (exposition-author with full canonical graph) — produced 8 entries.

The merge preserves audience-modeling decisions (all 3 agreed on the 4 institutional-term entries + the log + Flea-Bottom), takes Phase 2's better preamble paragraph 2 (concrete behavioral facts over summary-form), keeps the resurrection-mechanism paragraph 3 (Phase 2 dropped; structurally required to answer the implicit "why-no-riot" question), and applies the conditional-fire rule to scene-open-orient (11 fires, 1 refusal at @98 where loc-state:1 covers).

This facet is the canonical exposition for s01e01. The polish (active-project/polish/s01e01.md) is re-rendered from this facet — the polish reflects the facet, not the other way around.
