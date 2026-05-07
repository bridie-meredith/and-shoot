---
facet: state-updates
episode: s01e01
authors: split — studio (studio.* + prop:*) | dialogue-writer fork per character (actor:*)
phase: shipped (Phase 5 final adjudication: 13/13 = 100%; READY-WITH-CAVEATS)
rubric: design/shoot-v2/rubric-state-updates.md (V2 locked)
distribution: 13 fires / 77 beats = 16.9% [within 8–18% rubric band]
density-alignment: 1.46× (non-1 vs 1-zone) [SHAPE soft-fail vs 2× rubric minimum — chain-flip-beat distribution is structural, not contaminating; defensible under §"Curve-shape rubric / When curve-shape fails"]
caveats: 4 residuals named in phase5-state-updates-final.md (margit referral for prop card authoring; density-alignment soft-fail; Edric `<old>` project-setup baseline grounding; @77 cluster density advisory)
---
1  @9  prop:oc-district-ledger.physical-condition: rolled -> unrolled
2  @38 prop:oc-letter.holder: taylor -> extended-by-taylor
3  @40 prop:oc-letter.holder: extended-by-taylor -> officer
4  @41 prop:oc-letter.seal-condition: intact -> broken
5  @45 prop:oc-letter.holder: officer -> taylor
6  @48 prop:oc-district-ledger.taylor-entry: pending -> dictated-provisional
7  @48 actor:taylor-hebert-westeros.administrative-status: child-or-ward -> provisional-labor-eligible
8  @57 studio.actors_in_yard: officer+taylor+mira+edric -> officer+taylor+mira
9  @57 actor:edric-cray.sublocation: yard (near sept door) -> sept interior (past threshold)
10 @64 prop:oc-district-ledger.taylor-entry: dictated-provisional -> marked-parallel-margin
11 @64 actor:taylor-hebert-westeros.knowledge.record-state: name-on-line-provisional -> name-on-line-with-parallel-margin-marks
12 @77 actor:taylor-hebert-westeros.sublocation: yard -> sept-interior
13 @77 actor:taylor-hebert-westeros.mask-state: maintained-cooperative-child -> mask-thinned-private

---

## Field-extensions declared (per rubric §"Field-extension protocol")

- `prop:oc-district-ledger.physical-condition` — first-touch s01e01; ledger deployed at @9; field stays at unrolled through episode close.
- `prop:oc-district-ledger.taylor-entry` — first-touch s01e01 from `pending` (project-setup baseline per calibration anchor); irreversible chain through @48 → @64.
- `prop:oc-letter.holder` — standard prop-state field; chain @38 → @40 → @45.
- `prop:oc-letter.seal-condition` — standard seal-bearing-prop field; irreversible at @41.
- `actor:taylor-hebert-westeros.administrative-status` — first-touch s01e01; baseline `child-or-ward` from persona card project-setup; new value `provisional-labor-eligible` is season-arc-load-bearing.
- `actor:taylor-hebert-westeros.knowledge.record-state` — first-touch s01e01; chain-grounded to studio's @48 ledger entry.
- `actor:taylor-hebert-westeros.mask-state` — first-touch s01e01; baseline `maintained-cooperative-child` per behavior pack §"Voice tells / Mask-thinning"; persists into s01e02.
- `actor:taylor-hebert-westeros.sublocation` — on-schema field; baseline yard from @14 onward.
- `actor:edric-cray.sublocation` — on-schema field; baseline `yard (near sept door)` from project-setup (corroborated by @54 + @57 proto-line context).
- `studio.actors_in_yard` — on-schema studio field; first-touch this episode.

## Margit referral (mandatory follow-up, not blocking ship)

**Author cards for `oc-letter` and `oc-district-ledger`** before s01e02 authoring. Both are project-original props introduced in s01e01 with no formal `cards/props/` cards. Recommended schemas:

- **`oc-letter` card:** the wardship document Septon Osmynd left for Taylor. Tracked fields: holder, physical-condition (folded/unfolded/torn), seal-condition (intact/broken). Recurs as the season's identity-document for Taylor; load-bearing for s01e02+ administrative confrontations.
- **`oc-district-ledger` card:** the census ledger the clerk maintains; the Plumm-claim and Bracken-counter-claim live on its sept-precinct page. Tracked fields: physical-condition, taylor-entry (pending/dictated-provisional/marked-parallel-margin/etc.), other-entries (per-character map). Recurs as the season's administrative spine.

## Cross-facet contract notes (forward to downstream consumers)

- **Showrunner (canonical write-back consumer):** 13 mutations to apply at the cross-facet → stitch boundary.
  - `prop:oc-district-ledger`: physical-condition + taylor-entry chain through episode.
  - `prop:oc-letter`: holder chain (taylor → extended-by-taylor → officer → taylor); seal-condition flipped at @41.
  - `studio.actors_in_yard`: composition delta at @57.
  - `actor:taylor-hebert-westeros`: administrative-status (@48), knowledge.record-state (@64), sublocation (@77), mask-state (@77).
  - `actor:edric-cray`: sublocation (@57).
- **Stitcher:** 13 render-anchors at irreversible turns. The confrontation cluster (@38, @40, @41, @45, @48, @57, @64) carries 9 of 13 entries; the @77 close carries 2; the @9 deployment carries 1. Beats with state-updates are load-bearing for canonical memory and should render at high weight.
- **Future-episode authors (s01e02+):** Taylor's project-open state at s01e02 inherits administrative-status=provisional-labor-eligible, knowledge.record-state=name-on-line-with-parallel-margin-marks, sublocation=sept-interior, mask-state=mask-thinned-private. Edric's project-open state inherits sublocation=sept-interior. The ledger and letter inherit their @64 / @45 final states.

## Density notation (advisory)

13/77 = 16.9% within band. Density-alignment ratio 1.46× below 2× rubric heuristic — **shipped with notation**, not as a contamination. The @9, @40, @41, @45, @77 1-zone fires are chain-flip-beats whose registration-peaks are at adjacent non-1 beats; this is structural to a flip-beat facet (state-updates fires on the *mechanical* delta beat, not the *registration* peak). Future facet authoring may revisit the 2× heuristic for state-updates specifically.
