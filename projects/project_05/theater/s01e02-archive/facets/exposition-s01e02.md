facet: exposition
episode: s01e02
author: exposition-author (R1 retrofit blind authoring; 2026-05-12)
audience-modeled-against: [cape-fic-reader, dark-fantasy-reader, worm-canon-pedant]
---

# Episode-open scopes (render before body, italic)

1 @0 prior-episode-bridge: "Through the first weeks in Flea Bottom I had walked my three hundred metres twice a day, mapped the market-side junction and the apothecary's upper room where the broken maester kept his hours, and made my first transactional pass with the dock-runner through the tanner-elder. The log was current. The tanner-village was a day's walk south and had stayed there." | scope: prior-episode-bridge | renders-as: italic-preamble | sources: season-plan §s01-content-beats-6-7-8, series-plan §s01-chunk, cond-clinical-self-erasure §the-s1-register, loc-flea-bottom-base §radius-note, episode-s01e02.chunk, exposition-s01e01:4 (the log), exposition-s01e01:7 (flea-bottom), exposition-s01e01:8 (maester) | licensed-by: all-personas-need-prior-episode-terminal-state-recap (cape-fic-needs-300m-and-network-state-recall; dark-fantasy-needs-village-distance-and-flea-bottom-position; worm-canon-needs-pre-arc-anchors-restated)

# First-mention scopes (fold in at anchor per renders-as)

2 @66 fish-gate: "the Fish Gate — the southern dock-side gate of King's Landing, the city's busy fish-trade mouth" | scope: first-mention-place | renders-as: em-dash-fold | sources: loc-flea-bottom-base §radius-note, world-build:kings-landing-flea-bottom | licensed-by: cape-fic-doesnt-know-Fish-Gate-as-KL-specific-gate, worm-canon-doesnt-know-Fish-Gate-location (dark-fantasy may know from canon; the em-dash-fold is light enough to not disrupt the canon-familiar reader)

3 @100 customary-wage-claim: "what the Crownlands called the customary wage — the unwritten claim a family carried for the labour a returned child owed them, a tally without paper" | scope: first-mention-term | renders-as: parenthetical-aside | sources: cond-westerosi-customary-authority-125ac §flea-bottom-tied-landless-distinction, cond-westerosi-customary-authority-125ac §taylors-specific-legal-position, cond-crownlands-superstition-frame-125ac §the-tanner-family-situation-as-ongoing-cost, season-s01-plan §content-beat-13, episode-s01e02.chunk | licensed-by: cape-fic-doesnt-know-Crownlands-customary-wage-mechanism, worm-canon-doesnt-know-feudal-wage-claim-machinery, dark-fantasy-needs-the-Crownlands-specific-register-not-generic-feudal-debt

4 @173 vigil-candle: "the vigil candle — a Stranger-light kept burning for the dead until the family released them" | scope: first-mention-object | renders-as: em-dash-fold | sources: cond-crownlands-superstition-frame-125ac §the-stranger-leavings-frame, cond-crownlands-superstition-frame-125ac §the-tanner-family-situation-as-ongoing-cost, season-s01-plan §content-beat-17, episode-s01e02.chunk | licensed-by: cape-fic-doesnt-know-Westerosi-Stranger-theology, worm-canon-doesnt-know-Crownlands-vigil-practice, dark-fantasy-needs-Crownlands-specific-Stranger-light-register-not-generic-Catholic-vigil

# Scene-open-orient scopes (conditional fire per schema § scene-open-orient fire-rule)

# Fire-audit per scene-boundary (s01e02 candidate boundaries based on proto-line time-skip blanks and bone-content):
#   @3   episode-open-into-scene-A | proto-line @3 is "faces the junction" — explicit place in bone; loc-state:1 fires at @3 — REFUSES (loc-state carries)
#   @30  post-scene-A-departure-to-log | time-skip ✓ | loc-state ✗ at @30 | NI@first-2: NI:8@30 (operational log-action; reading as situational not time/place) — FIRES (back-at-base log-scene needs time/place orient after junction departure)
#   @34  post-log-to-relay-scene | time-skip ✓ | loc-state ✗ at @34 | NI@first-2: none at @34; NI:9@35 in second anchor (Watch-patrol relay, situational not time) | bone @34-@35 are pure relay-action — FIRES (a relay-scene needs orienting marker; bones are operational-only)
#   @41  relay-continuation-to-base | proto-line @41 is "enters loc-flea-bottom-base [loc-state:3]" — LOC-STATE FIRES — REFUSES
#   @50  back-out-to-junction | proto-line @50 "enters the market-side junction [loc-state:4]" — LOC-STATE FIRES — REFUSES
#   @60  overnight-network-operation | proto-line @60 "the flies spread the overnight network" — bone itself carries "overnight" time-marker — REFUSES (bone carries; scene-orient is wallpaper)
#   @77  post-overnight-wake | proto-line @77 "taylor wakes" — "wakes" itself is time-shift marker; NI:13@77 fires (content unknown but at first anchor, likely carries) — REFUSES (wake-bone + NI cover)
#   @83  eviction-scene-open | proto-line @83 "the lords-man enters the alley [loc-state:5]" — LOC-STATE FIRES — REFUSES
#   @97  second-tanner-visit | proto-line @97 "oc-tanner-father enters the market-side junction [loc-state:6]" — LOC-STATE FIRES — REFUSES
#   @117 autumn-density-network | proto-line @117 "the flies spread the autumn-density network [narrator:34]" — bone carries "autumn-density" seasonal marker; NI:34@117 fires at first anchor — REFUSES (bone + NI cover)
#   @132 visitor-to-maester | proto-line @132 "the visitor enters the side alley [loc-state:7]" — LOC-STATE FIRES — REFUSES
#   @148 beetles-relay-rhythm | gap from @146 is small (intra-scene log-close to ambient-relay); not a true scene boundary — beetles-relay is continuation of the visitor-arc; REFUSES (no scene break)
#   @156 broken-maester-out | proto-line @156 "oc-broken-maester exits the apothecary [loc-state:9]" — LOC-STATE FIRES — REFUSES
#   @164 third-tanner-visit-mother | proto-line @164 "oc-tanner-mother enters loc-flea-bottom-base [loc-state:11]" — LOC-STATE FIRES — REFUSES
#   @176 post-mother-log | gap from @174 small; log-scene-close; not new scene — REFUSES (continuation)
# Total: 2 fires, 12 refusals (1 of the 12 refusals is the @3 episode-open boundary; the other 11 are mid-episode boundaries where loc-state, NI, or the bone-content carries the orient).

5 @30 scene-open-orient-b: "Back at the base room, I opened the log." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-A-close-was-junction-departure-after-first-tanner-visit, loc-flea-bottom-base §layout | licensed-by: all-personas-need-place-shift-from-junction-back-to-base (loc-state silent at @30; the log-scene is at her base room not at the junction; without bridge reader holds last-cited-location which is junction)

6 @34 scene-open-orient-c: "After, I let the relays run." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-B-close-was-log-write, season-s01-plan §content-beat-10, episode-s01e02.chunk | licensed-by: all-personas-need-temporal-link-to-prior-log-scene (the relay-pass is the next operational beat after logging; without bridge the relay-bones read as a hard jump-cut)

# Cross-episode register (write-back at facet-close)

# After this episode lands, the following keys promote to active-project/staff/exposition-author/glossed-terms.md:
# - fish-gate | first-mention-anchor: @66
# - customary-wage-claim | first-mention-anchor: @100
# - vigil-candle | first-mention-anchor: @173

# Notes

R1 blind authoring. Did not read other R1 facet files. Scene-open-orient fire-audit conducted against (a) time-skip-blanks visible in proto-lines/s01e02.md, (b) loc-state citations annotated on the proto-lines themselves (a proxy for actual loc-state.md content — citations indicate firing), and (c) NI citations + bone-content scanning for time/place register. The fire-audit refuses 12 of 14 candidate boundaries and fires 2; this is a higher refusal rate than s01e01 (1-of-12-refusals) because s01e02 has more loc-state-charged scene-openings (eviction-scene, second-tanner-visit, visitor-to-maester, broken-maester-out, third-tanner-visit-mother all carry loc-state at-establishment).

Cull-pass performed (single attempt): no entries dropped. Initial candidate set was 4 first-mention + 2 scene-orient + 1 bridge = 7 entries. All 7 survived the union-gap test and the cull-pass (none borderline, none duplicating series-plan-resident content, none single-mention-non-load-bearing). Episode 02 is light on first-mention surface because s01e01 already glossed log/reeve/lords-man/flea-bottom/maester/the-Watch — the institutional and series-object terms are reader-resident.

Sparsity: 7 entries / 134 active proto-lines ≈ 5.2% — just at the upper bound of the 1-5% rubric band (functionally at-ceiling). Driver: prior-episode-bridge + 3 first-mention + 2 scene-orient is the load-bearing minimum for a non-cold-start episode that introduces vigil-candle, customary-wage-claim, and Fish-Gate. The over-by-0.2pts edge will be R2's call (or the cull-pass to drop scene-orient-c@34 if the lens facets show NI carries).
