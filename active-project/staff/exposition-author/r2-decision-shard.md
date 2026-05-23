---
facet: exposition
episode: b01c01
layer: R2.5
cite_index_hash: c9d9284f144d447503712cabdad2b985e60c03d16234c1821562fac039c8113c
f-r2-counts: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0}
verdict-counts: {KEEP: 0, REWORD: 3, DELETE: 2, ADD: 0, SCENE-ORIENT-REFUSAL: 3, CAP-REFUSAL: 3}
---

# R2.5 Exposition Decision Shard — b01c01

## Pre-flight: scene-open-orient fire-rule re-validation

The s01e01 dogfood lesson is binding: Phase 2 refused 11 of 11 scene-orient entries that Phase 1 authored, because NI/loc-state covered them. I walked the three scene-opens against the rubric's three-clause fire-rule before reading the entries.

Scene A opens at @1. loc-state:1 fires at @1 ("the corner-room threshold where an anonymous copper-star transaction purchases entry"). Clause (b) FAILS — loc-state at-establishment carries the scene-orient. NI:1 fires at @2 (within first-2-anchors of scene) and carries threshold-cognition ("the drain channel puts the yard on one side and the alley-mouth on the other"), reinforcing the refusal. REFUSED.

Scene B opens at @11. loc-state:4 fires at @11 with NEW time-of-day (midday) and new place-anchor (working corner off the Hook). Clause (b) FAILS. NI in first-2-anchors of scene B (anchors @11-@12) is silent. REFUSED on (b).

Scene C opens at @22. loc-state:6 + loc-state:7 both fire at @22 with NEW time-of-day (afternoon) and entry-verb (alley-mouth-open, meat-stall-direction). Clause (b) FAILS. REFUSED.

Three of three scene-opens fail fire-rule. No scene-open-orient entries are licensable in this chapter. The R1 author appears not to have authored any (the existing five entries are all first-mention scopes), which is the correct outcome — but I confirmed the routing rather than assuming.

## Per-entry verdicts

### exposition:1 @1 — kings-landing-122ac / flea-bottom / copper-currency-star-penny

I read this cold and the cluster does work the lens facets don't. loc-state:1 names "the corner-room threshold where an anonymous copper-star transaction purchases entry" — that carries the place-as-state and the payment mechanic in body. But Flea Bottom as an institution (the bottommost ward of King's Landing, no titles, no guild rolls, subsistence-class permanent) is not loc-state's register. loc-state is environmental; this is sociological. The dark-fantasy-reader specifically wants Planetos-local-color landing as Planetos-specific (hot-button: "Westerosi local color that lands as Planetos-specific, not generic medieval"). The worm-canon-pedant needs the geographic anchor named for series-locus tracking. Cape-fic-reader does not gap here (the payment mechanic is enough to read class-position from action), so I do not list them in licensed-by — that's a clean two-of-three persona license, which is sufficient. The R1 entry had no schema fields (no scope, renders-as, sources, licensed-by). That's a license-completeness fail per the rubric's CONSTRAINT class — REWORD to add the fields, choose `em-dash-fold` (cheapest viable for a cluster gloss that reads as an aside), and pin the gap-claims. Content survives; surface tightens.
VERDICT: REWORD

### exposition:2 @4 — coll (first-mention-character)

Coll appears in prose at @3 (the lift-eyes bone) and @4 (the works-the-net bone). NI does not fire at @4 — Taylor's interiority is anchored elsewhere (@2, @9 in scene A). loc-state:1 doesn't name Coll; loc-state:4 names him at @11 as "coll-at-corner" condition, but that's mid-scene-B and after the first-mention. state-updates introduces Coll as present in environment but doesn't carry his social role. The R1 entry's payload is the fixture-not-confidant orientation: "range of interest runs one street; does not ask what strangers are" — that's the structural function lens facets do not establish. Dark-fantasy-reader needs Coll grounded as Planetos-specific smallfolk substrate; cape-fic-reader needs the marker that says stop expecting interpretation from him. The R1 entry is missing schema fields. REWORD to add them; keep the body content essentially intact, lean to `em-dash-fold` rendering.
VERDICT: REWORD

### exposition:3 @9 — the-prohibition

The hardest call in the file. R1 argued all three personas gap on the prohibition — cape-fic needs it framed as series premise, worm-canon needs the passive-read scope confirmed, dark-fantasy needs to know what wasn't deployed. The R1 reasoning was made blind to the lens stack at @9. Now that I can see the stack: @9 is the chapter's densest pile-up (7 co-located facets). NI:2 carries "no one here has a power that requires containing; the sense runs along the walls and stops because the walls are the limit, not because something forced it back." That IS the prohibition stated in interior voice. mem:1 carries "the block is not requiring anything of the kind she is no longer doing -> (earth-bet: override-architecture-prohibition-enacted-via-inverse-observation)" — the displaced-register articulation of exactly the same operating rule. vibes:3 + vibes:4 carry "absence-as-the-evidence-of-discipline, the-prohibition-enacted-in-the-not-doing, first-on-screen-check-passes" and "the-block-does-not-require-her, the-check-is-the-practice, trained-attention-to-what-is-not-there." feel:1 carries the somatic correlate. The rubric's never-gloss rule is direct: "mem establishing a callback-anchor → exposition does NOT explain the callback's prior context." mem:1 IS the callback-anchor. The R1 exposition gloss is doing exactly what the rubric forbids — explaining the prohibition the mem-anchor refers back to. The s01e01 dogfood lesson is binding here: Phase-2 refuses where lens carries. The cape-fic argument that "the operating rule is the series premise without it @9 reads as pause not discipline" is what NI + mem + feel + vibes are FOR — that stack reads as discipline if it reads at all; if it doesn't, the stitcher will fail the cold-read gate downstream and the fix lives at /and-write or stitcher Phase 9, not at exposition. The exposition entry would AP-double the mem/NI register. DELETE.
VERDICT: DELETE

### exposition:4 @18 — the-city-watch / the-hook

loc-state:6 @18 reads: "the Hook's bend: four-body patrol in gold cloaks; working corner has unobstructed line-of-sight to the bend." Both terms — the Hook and the Watch — land in loc-state's body at the at-establishment fire. The Watch becomes "four-body patrol in gold cloaks" which is functional first-mention orientation (the audience reads "gold cloaks" + "patrol" + "four-body" and gets uniformed policing presence without needing exposition). The Hook becomes "the Hook's bend" with adjacency to the working corner — that's geographic orientation in body. The rubric's never-gloss rule applies: "NI establishing place-name → exposition does NOT add a place-gloss for the same name." loc-state at-establishment is the lens-equivalent here (the rule explicitly catches both NI and loc-state under "lens-carries"). The R1 entry's unique payload is the channel-cut-district-with-compressed-alleys topology — that's not load-bearing for @18 (it's wallpaper at the watch-pass beat), and the only way to fire it would be as scene-B-open scene-orient, which fails fire-rule because loc-state:4 fires at @11. The cape-fic-reader does not gap on the Watch (they read it from "gold cloaks + patrol"). The dark-fantasy-reader's gap on "the Hook" is closed by loc-state's at-establishment naming. DELETE.
VERDICT: DELETE

### exposition:5 @22 — wren (first-mention-character)

Wren enters in prose at @22 (the chapter's payload-bearer). loc-state:6/7 at @22 carry the alley-mouth geometry but not Wren's social role. NI fires at @24 (after first-mention) and at @26 — both interior cognition ABOUT Wren, neither functioning as introduction. feel-wren:1 @26 is Wren's somatic tell during speech. The dialogue-writer fork carries her speech-content but not her structural orientation. The R1 entry's payload — ward of the stitch-maker's household, eleven-ish, has been here long enough that she is not new, watches before she acts — is the structural first-mention-character coverage that all three personas need to read the @22-@28 sequence as load-bearing rather than decorative. Cape-fic-reader needs the cost-bearer-introduction with class-tier + presence-status (they're tracking the cast for who pays what; Wren needs to land as someone who can pay). Dark-fantasy-reader needs the smallfolk-ward arrangement as Planetos-specific (not generic medieval orphan trope). Worm-canon-pedant needs the cost-bearer-anchor flagged at first on-screen because the @26 flies-observation is the chapter payload and they're tracking whether the cost-bearer is properly seeded. Embedded-noun check: the gloss references "Flea Bottom" (on register, gloss-id 2) and "stitch-maker" (common-English compound, self-explanatory). No unresolved embedded proper-nouns. PASS the HARD-embedded-noun gate. The R1 entry's body content survives; schema-fields are added; render-as set to em-dash-fold (cheapest viable for the gloss length).
VERDICT: REWORD

## ADD candidates considered (cap 3; refused all)

CAP-REFUSAL: building-keeper @1 — I considered this as a first-mention-term candidate. The role appears in proto-line @1 ("pays the building-keeper") and loc-state:1 carries "building-keeper-present" as condition. The audience-gap is thin — dark-fantasy-reader can read the role from action + condition (a person who keeps the building and collects rent), and cape-fic-reader doesn't need it spelled out. Worm-canon-pedant has no gap. The R1 author appears to have considered and refused this — that refusal is correct. Lens carries.

CAP-REFUSAL: drain-channel @2 — common-English noun; loc-state:2 names it explicitly with state ("the drain-cut mud channel: wet stone gap at the yard crossing"). No audience-gap. Lens carries.

CAP-REFUSAL: stitch-maker @22 — common-English compound (a stitcher who mends); self-explanatory; the gloss embedded inside the Wren entry contextualizes the role without needing a separate first-mention-term. The embedded-noun HARD-gate passes because stitch-maker is not a proper-noun frame. No ADD warranted.

## Pattern-scan

Reading the file as a whole after R2.5 mutation — three REWORDs and two DELETEs — the surviving entries cluster around character-introduction (Coll at @4, Wren at @22) and one place-cluster (the @1 institutional orient). The shape after the cuts is what an exposition file SHOULD look like at series-opener under the substance-overhaul routing: lens-facet-heavy chapter, exposition narrow to the gaps lens doesn't cover. The two DELETEs (the-prohibition @9, the-city-watch/the-hook @18) were both lens-redundancy faults the R1 audience-pure pass couldn't see. No formulaic surface pattern across the three survivors — each does distinct work (place-as-institution, character-as-fixture, character-as-cost-bearer). Pattern-scan clean.

## Arbiter notes

No arbiter interventions fired during this judge pass. Each verdict above names entry-specific content (the @9 mem-callback-anchor protection, the @18 loc-state body-carry of both terms, the @22 cost-bearer-seeding payload) rather than reciting rubric labels. T1 and T4 (the v2 active triggers) had no occasion to fire. f-r2-counts: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0}.

## Frontmatter pass-count reconciliation

- KEEP: 0 (all surviving entries required schema-shape REWORD to add scope/renders-as/sources/licensed-by fields)
- REWORD: 3 (exposition:1, exposition:2, exposition:5 — IDs preserved, bodies re-rendered with schema compliance)
- DELETE: 2 (exposition:3 @9 the-prohibition; exposition:4 @18 the-city-watch/the-hook)
- ADD: 0
- SCENE-ORIENT-REFUSAL: 3 (all three scene-opens refused on fire-rule clause b)
- CAP-REFUSAL: 3 (building-keeper @1; drain-channel @2; stitch-maker @22)
