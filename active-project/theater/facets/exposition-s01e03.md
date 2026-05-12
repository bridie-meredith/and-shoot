facet: exposition
episode: s01e03
author: exposition-author (R1 retrofit blind authoring; 2026-05-12)
audience-modeled-against: [cape-fic-reader, dark-fantasy-reader, worm-canon-pedant]
---

# Episode-open scopes (render before body, italic)

1 @0 prior-episode-bridge: "By the next winter the tanner-family's wage-claim was on customary record; my mother had stopped lighting the vigil candle; the broken maester had become a named entry in my log; my insects ran to four hundred metres. I kept writing." | scope: prior-episode-bridge | renders-as: italic-preamble | sources: season-s01-plan §beat-13 (tanner-family customary wage-claim), season-s01-plan §beat-17 (mother stopped vigil candle), season-s01-plan §beat-16 (maester named-log entry), season-s01-plan §beat-14 (range crosses 400m), cond-clinical-self-erasure §the-log-as-instrument | licensed-by: all-personas-need-prior-episode-terminal-state-recap (non-first-episode; replaces episode-open-preamble per schema § prior-episode-bridge rule)

# First-mention scopes (fold in at anchor per renders-as)

2 @3 clerk: "Different rank than reeve or lord's-man, different office — the clerk's work was the entry, not the errand." | scope: first-mention-term | renders-as: post-bone-clause | sources: cond-westerosi-customary-authority-125ac §The-Hand-of-the-King's-administrative-apparatus (Hand's office manages tax rolls, guild oversight, census-adjacent records), s01e01-glossed-register §reeve+lords-man (distinguishes prior glosses) | licensed-by: cape-fic-doesnt-know-Westerosi-administrative-rank-distinct-from-watch-roles, worm-canon-needs-Hand-apparatus-clerk-distinct-from-already-glossed-reeve-and-lords-man, dark-fantasy-borderline-but-disambiguation-from-prior-glosses-is-load-bearing

# fish-gate dropped post-author-cull: s01e02 retrofit (concurrent) authored fish-gate at @66 first; per cross-episode register no-re-gloss rule, s01e02 owns the gloss. The s01e03 author's flagged-overlap-low-probability note in §Notes was confirmed in reconciliation — original entry deleted, IDs renumbered, [exposition:3] stripped from annotated proto-lines @11.

3 @125 red-keep: "the king's castle above the city" | scope: first-mention-place | renders-as: em-dash-fold | sources: loc-red-keep-outer-ring §Geography (outer walls, gatehouse approaches), world-build:kings-landing (the king's seat) | licensed-by: cape-fic-and-worm-canon-dont-know-the-Red-Keep-as-king's-castle (dark-fantasy knows; the cheap em-dash-fold keeps the gloss invisible to the persona that doesn't need it)

# Scene-open-orient scopes (conditional fire per schema § scene-open-orient fire-rule)

# Fire-audit per scene-boundary (s01e03 has time-skip blanks before IDs 18, 33, 50, 56, 73, 96, 110, 127, 136, 148):
#   @18  time-skip ✓ | loc-state ✗ at @18 | NI@first-2 (@18, @19): no NI tokens; SVO surface ("winter-onset network", "dock-side alleys") names ambient operation but not time-of-day shift — FIRES (overnight-marker needed)
#   @33  time-skip ✓ | loc-state ✗ at @33 (loc-state:6 fires at @34) | NI@first-2 (@33, @34): NI:8@34 fires alongside loc-state:6@34; the proto-line surface at @33 ("the second clerk enters the eastern-quarter adjacent street") explicitly names place; NI:8 in first 2 anchors carries place-shift content — REFUSES (NI + bone-surface carry the place; scene-orient wallpaper)
#   @50  time-skip ✓ | loc-state:7 fires AT @50 | (b) violated — REFUSES (loc-state carries time/place at scene-open anchor)
#   @56  time-skip ✓ | loc-state:8 fires AT @56 | (b) violated — REFUSES
#   @73  time-skip ✓ | loc-state ✗ at @73 (loc-state:10 fires at @75) | NI@first-2 (@73, @74): no NI tokens on @73 or @74; SVO surface ("descends the stair", "exits the apothecary") names pure action without time-of-day — FIRES (later-that-day marker needed; the maester's market trip is its own scene)
#   @96  time-skip ✓ | loc-state:13 fires AT @96 | (b) violated — REFUSES
#   @110 time-skip ✓ | loc-state ✗ at @110 | NI@first-2 (@110, @111): no NI tokens; SVO surface ("the flies spread the overnight network", "the wasps spread the Fish Gate margin") — "overnight" appears on the bone surface itself; rule-fires under (a)(b)(c), but author-time cull DROPPED post-fire on bone-surface-duplication grounds (a scene-orient bridge here would restate the "overnight" already carried by the bone)
#   @127 time-skip ✓ | loc-state:17 fires AT @127 | (b) violated — REFUSES
#   @136 time-skip ✓ | loc-state ✗ at @136 (loc-state:18 fires at @137) | NI@first-2 (@136, @137): narrator:32@137 fires within first 2 anchors, paired with loc-state:18@137 (writing-room enter); NI:32 carries place-shift content — REFUSES (NI + loc-state carry the place-shift; scene-orient wallpaper)
#   @148 time-skip ✓ | loc-state:19 fires AT @148 | (b) violated — REFUSES
# Total: 2 fires post-cull (3 rule-fires; 1 author-cull at @110 for bone-surface-duplication), 7 refusals.

4 @18 scene-open-orient: "That night I spread the network wide." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-close-was-log-write-at-16, season-s01-plan §beat-19 (incremental expansion through early winter as shard reseed stabilizes — overnight network operation) | licensed-by: all-personas-need-overnight-marker (the scene is an overnight network expansion event; without the time-marker the spreading reads as continuous with the log-write that closed the prior scene)

5 @73 scene-open-orient: "Later that day, the maester left his rooms." | scope: scene-open-orient | renders-as: scene-bridge | sources: prior-scene-close-was-log-write-at-71, season-s01-plan §beat-22 (broken maester walks to eastern-quarter market stall) | licensed-by: all-personas-need-temporal-link-and-actor-handoff (the maester scene observed via insect-network is a distinct beat; without the bridge the reader reads the maester's descent as continuous with Taylor's log-close)

# Cross-episode register (write-back at facet-close)

# After this episode lands, the following keys promote to active-project/staff/exposition-author/glossed-terms.md:
# - clerk | first-mention-anchor: @3
# - red-keep | first-mention-anchor: @125
# (fish-gate dropped — s01e02 retrofit owns the gloss; see entry-list above)

# Notes

# Bridge content respects the episode's load-bearing reader-asymmetry: Taylor does not yet know
# the clerks are of the Hand's apparatus, so the bridge stays in her frame (first-person past)
# and does not preview "Hightower" or "Hand of the King." Naming the apparatus would break the
# beat-26 reader-level asymmetry that the season's terminal denouement is built on.
#
# Clerk gloss avoids naming Hightower/Hand for the same reason. The gloss establishes only the
# administrative-rank-distinct-from-reeve/lord's-man register (cape-fic + worm-canon gap); the
# specific apparatus identity is reserved for reader-level inference at episode close.
#
# Potential s01e02 retrofit overlap (per orchestrator note — s01e02 retrofit concurrent; register
# does not yet list s01e02 entries):
#   - clerk: low-probability overlap. s01e02 bones contain no clerk character (the lord's-man
#     glossed in s01e01 was the s01-beat-5 quarterly-pass visitor; s01e02 covers beats 8-15ish,
#     all village-claim and maester-ambient territory). Flagging for manual reconciliation as
#     defensive measure, but inspection of s01e02 chunk ("tanner-family claim escalates ... maester
#     transitions from ambient signal to named log entry ... range expands 300m→400m ... mother
#     extinguishes vigil candle") suggests no clerk first-mention.
#   - fish-gate: low-probability overlap. s01e02 chunk does not foreground the Fish Gate; s01e01
#     proto-lines mentioned "Fish Gate margin" but the s01e01 exposition register lists no
#     fish-gate entry (the s01e01 author treated it as graph-resident-by-context).
#   - red-keep: very-low-probability overlap. s01e02 does not bring the Red Keep into Taylor's
#     awareness; this is a s01e03-specific first-mention at @125 (Taylor's wall-facing beat).
