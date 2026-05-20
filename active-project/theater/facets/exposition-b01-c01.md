facet: exposition
episode: b01-c01
author: exposition-author (R1)
voice: pov-frame first-person
---

# exposition — b01-c01 (R1)

# Fire-audit (scene-open-orient candidates)
# Scene-A @1: no time-skip-blank precedes (chapter open; preamble covers); condition (a) fails. NO FIRE.
# Scene-B @11: time-skip-blank @10 precedes; condition (a) met. R1 cannot read loc-state/NI;
#   firing scene-open-orient as candidate; R2 (graph-aware) will refuse if (b) loc-state-at-anchor or (c) NI-time-or-place-in-first-2-anchors covers.
# Scene-C @22: time-skip-blank @21 precedes; condition (a) met. R1 candidate; R2 will refuse on lens-cover.

1 @0 episode-open-preamble: I am twenty years old by the calendar I came in with, and the year here is 122 AC — late in Viserys-the-First's reign, though no one in Flea Bottom counts the king's years, only feast, shortage, and the lord's levy. I live in King's Landing now, in the slum south of the three hills. I came here with a rule. Be useful without taking control. Do not do, again, what I once did at the end of the world I came from. | scope: episode-open-preamble | renders-as: italic-preamble | sources: project.constraints.settings, cond-kl-court-state-122ac, cond-kl-geography-122ac, cond-kl-social-physics-122ac, cond-override-architecture-residue-122ac, cond-earth-bet-noun-fence, b01c01.chunk, b01c01s01.chunk | licensed-by: cape-fic-reader:cape-fic-doesnt-know-122-AC-as-westerosi-date-or-kings-landing-as-place-or-flea-bottom-as-slum, dark-fantasy-reader:dark-fantasy-needs-the-prohibition-frame-and-the-world-i-came-from-without-earth-bet-naming, worm-canon-pedant:worm-canon-needs-the-once-deployed-override-rendered-as-the-prohibition-without-naming-khepri

2 @0 episode-open-context: Flea Bottom is the city's lowest ground, the warren south of Aegon's Hill where the smallfolk live who count their coin in copper — pennies for a small meal, stars for a cup of water or a courtesy paid. I pay copper stars for a corner-room off the Hook, a curving lane near the river where the most marginal of Flea Bottom keeps to itself, and I mend nets to pay for the next week. | scope: episode-open-context | renders-as: preamble-paragraph | sources: cond-kl-geography-122ac, cond-kl-social-physics-122ac, b01c01.chunk, b01c01s01.chunk | licensed-by: cape-fic-reader:cape-fic-doesnt-know-flea-bottom-position-or-copper-currency-or-the-hook-as-waterfront-margin, worm-canon-pedant:worm-canon-doesnt-know-kl-internal-geography-or-westerosi-currency-units, dark-fantasy-reader:dark-fantasy-needs-flea-bottom-specifically-as-the-slum-and-not-generic-medieval-poor-quarter

3 @4 coll: Coll — the net-mender who keeps the corner of the building's street face, a man in his fifties whose range of observation runs exactly one street and who asks nothing of strangers who can hold a needle. | scope: first-mention-character | renders-as: inline-appositive | sources: coll-net-mender-flea-bottom.card, b01c01s01.chunk, cond-kl-social-physics-122ac | licensed-by: cape-fic-reader:cape-fic-has-no-roster-anchor-for-coll-as-a-named-individual-entering-prose, dark-fantasy-reader:dark-fantasy-needs-collas-flea-bottom-fixture-not-generic-old-man, worm-canon-pedant:worm-canon-has-no-prior-anchor-for-this-named-individual

# exposition:4 DELETED (F-002, 2026-05-20 — scene-orient-fire-rule condition (b) violated: loc-state:3 fires at @11, covering the orientation; scene-open-orient must not fire when loc-state covers the anchor; R2 refusal stood but delete was not executed)

5 @18 the-city-watch: the city-watch — King's Landing's standing patrol in gold cloaks, a few hundred strong, who move through Flea Bottom on a rotation the block knows by sound. | scope: first-mention-term | renders-as: em-dash-fold | sources: cond-kl-social-physics-122ac, cond-kl-geography-122ac | licensed-by: cape-fic-reader:cape-fic-doesnt-know-westerosi-watch-as-institution-distinct-from-generic-guard, worm-canon-pedant:worm-canon-doesnt-know-kl-watch-as-gold-cloaked-standing-patrol, dark-fantasy-reader:dark-fantasy-needs-watch-as-westerosi-institution-not-generic-medieval-guard

6 @18 the-hook: the Hook — a curving lane at Flea Bottom's waterfront edge, the slum's lowest margin, where the most transient and least-protected smallfolk keep their rooms. | scope: first-mention-place | renders-as: inline-appositive | sources: cond-kl-geography-122ac, cond-kl-social-physics-122ac, wren-stitch-maker-flea-bottom-ward.card | licensed-by: cape-fic-reader:cape-fic-doesnt-know-the-hook-as-flea-bottoms-waterfront-margin, worm-canon-pedant:worm-canon-doesnt-know-kl-flea-bottom-internal-geography, dark-fantasy-reader:dark-fantasy-needs-the-hook-as-place-frame-not-institution

# exposition:7 DELETED (F-003, 2026-05-20 — scene-orient-fire-rule condition (b) violated: loc-state:5 fires at @22, covering the orientation; scene-open-orient must not fire when loc-state covers the anchor; R2 refusal stood but delete was not executed)

8 @22 wren: Wren — a stitch-maker's ward from two buildings over, eleven years old, kept in light work and two meals for trim-work and thread-sorting, with the close-watching habit a trade like that teaches. | scope: first-mention-character | renders-as: inline-appositive | sources: wren-stitch-maker-flea-bottom-ward.card, b01c01s03.chunk, cond-kl-social-physics-122ac | licensed-by: cape-fic-reader:cape-fic-has-no-roster-anchor-for-wren-as-named-individual-entering-prose, dark-fantasy-reader:dark-fantasy-needs-wren-as-flea-bottom-ward-not-generic-child, worm-canon-pedant:worm-canon-has-no-prior-anchor-for-this-named-individual

# Cross-episode register write-back (b01c01 baseline establishment)
# - kings-landing-122ac | first-mention-anchor: @0 | gloss-id: 1
# - flea-bottom | first-mention-anchor: @0 | gloss-id: 1 (preamble) + @0 gloss-id: 2 (context)
# - the-prohibition | first-mention-anchor: @0 | gloss-id: 1
# - copper-currency-star-penny | first-mention-anchor: @0 | gloss-id: 2
# - coll | first-mention-anchor: @4 | gloss-id: 3
# - the-city-watch | first-mention-anchor: @18 | gloss-id: 5
# - the-hook | first-mention-anchor: @18 | gloss-id: 6
# - wren | first-mention-anchor: @22 | gloss-id: 8

# Flagged seams (R1 author-handoff notes; for R2 + audience-gate review)
# - Sparsity 8 / 27 in-scope proto-lines = 29.6%, above the 1-5% band. Cold-start chapter override: chapter 1 of 18
#   carries cold-read load no other chapter will, including the episode-open preamble + context (mandatory at series open),
#   first-mention of the chapter's three named individuals (Coll, the building-keeper considered then refused,
#   Wren), first-mention of the city-watch + the Hook (both will recur across the book), and two scene-open
#   candidates that R2 will likely refuse against lens-cover. Authored generously per the R1-generous / R2-trim shape.
# - Dark-fantasy reader's Khepri-side gap is intentionally only partially bridged in prose (preamble: "what I once did
#   at the end of the world I came from") per the Earth-Bet hard-fence. The remainder is reserved for vibes / memory
#   facets to carry offstage. R1 cannot bridge what the fence forbids naming.
# - building-keeper @2 considered as first-mention-character candidate and REFUSED at R1 cull: single-mention,
#   plain-English compound (building + keeper), recognizable as rent-collecting role from context; no later return;
#   not in cast roster; the rubric's "single-mention non-load-bearing terms can survive without gloss" clause applies.
# - "the corner-room" @1 considered as first-mention-place and REFUSED at R1 cull: common-English compound,
#   loc-state lens-facet expected to carry at-establishment per never-gloss "loc-state firing at-establishment".
# - "the insects fill the block" @15: Khepri-residue surface. Cannot be glossed in-prose under the Earth-Bet
#   fence. Residue resolution lives in vibes / memory facets. R1 deliberately silent at this anchor.
# - Embedded-noun audit per rubric URI-FACETS-CYCLE-1: Wren gloss-text (entry 8) references "stitch-maker"
#   (plain-English compound, no gloss needed) and implicitly the household; "two buildings over" presupposes
#   no proper noun. The Hook is glossed at entry 6 @18 which is PRIOR to entry 8 @22 — chain resolves.
#   Coll gloss-text (entry 3) references no embedded proper nouns. The-city-watch gloss (entry 5) references
#   King's Landing (covered by preamble entry 1) + Flea Bottom (covered by preamble entry 1 + context entry 2).
#   Preamble (entry 1) references Viserys-the-First (proper noun, not separately glossed) — judged acceptable
#   under the "always-known register" path: late-Viserys-I reign is the cold-start frame for the chapter and the
#   king's name appearing in the preamble's own framing sentence does not delegate context to an unoriented term;
#   the preamble's claim is that the year is 122 AC late-Viserys-reign, which is self-contained as a calendar marker.
#   Aegon's Hill (entry 2) — proper noun, not separately glossed, judged acceptable as a place-of-the-city named
#   in the city-orientation context paragraph (always-known to anyone who has read the preamble naming KL).
