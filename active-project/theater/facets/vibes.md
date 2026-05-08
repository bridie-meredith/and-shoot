---
facet: vibes
episode: s01e01
author: showrunner (Phase 4 revised; Phase 5 final adjudication 12/12 = 100% mechanic)
phase: shipped (READY-WITH-CAVEATS)
rubric: design/shoot-v2/rubric-vibes.md (V1 LOCKED + V1.1 patch applied this commit)
schema: schemas/facet.schema.md § vibes updates (REVISED THIS COMMIT — content shape `<id> [@<proto-line-id>] <target> <op> <keyword>: [<token>, ...] | licensed-by: <source>[, ...]`; targets extended to entity slugs; `licensed-by:` field formalized)
distribution: 12 entries / 77 beats = 15.6% (pre-seeded-project notation; expected range 9-14 for `++`-and-fresh-add subset)
op-distribution: 3 fresh `+` (1 actor + 2 loc) | 9 `++` extensions (5 actor + 1 loc + 3 episode) | 0 `-`
target-distribution: actor:5 (taylor:3, mira:1, edric:1, septon-dying-protector:1, census-officer:1 — total 5 entries on 5 actors) | loc:2 (harrenhal-sept-environs ×2) | episode:3 | season:0 | series:0
caveats: 5 residuals named below (none blocking)
calibration-anchors: C1 (taylor + the-machinery-arrives) PASS via entry 6 ++; C2 (septon + the-septon-as-absence) PASS via entry 3 fresh +; C3 (mira + the-yard-as-witness) PASS via entry 1 ++; C4 (episode + the-naming) PASS via pre-load coverage (no in-episode `++` warranted, DELETE confirmed)
---

1  @6  actor:mira-stonefield ++ the-yard-as-witness: [the-door-already-marked-before-the-ask, exit-located-before-the-weight-arrived] | licensed-by: feeling:1, proto:6, proto:51

2  @11 loc:harrenhal-sept-environs + the-machinery-arrives: [the-space-that-makes-smallfolk-legible, authority-day-contracted-into-two-body-lengths, the-ground-where-the-lord-collects, the-yard-that-cannot-claim-ignorance] | licensed-by: proto:11, proto:12, proto:13, world-build:smallfolk-common-authority-day-function

3  @33 actor:septon-dying-protector + the-septon-as-absence: [present-but-cannot-appear, the-protector-who-cannot-act, the-letter-in-place-of-the-body, kindness-that-runs-out-before-it-can-hold] | licensed-by: proto:32, proto:33, canon:osmynd-bedridden-pre-episode

4  @33 loc:harrenhal-sept-environs + the-septon-as-absence: [the-space-where-the-door-stayed-shut, the-building-whose-occupant-cannot-reach-its-threshold, charged-ground-for-what-did-not-emerge] | licensed-by: proto:32, proto:33, canon:osmynd-bedridden-pre-episode

5  @57 actor:edric-cray ++ the-yard-as-witness: [the-sept-interior-as-exit-destination, sublocation-confirmed-not-returned] | licensed-by: state-update:9, proto:55, proto:57

6  @57 episode ++ the-yard-as-witness: [the-refusal-with-the-officer-watching, edric-after-the-gate-cleared] | licensed-by: feeling:1, feeling:3, proto:52, proto:57

7  @64 actor:taylor-hebert-westeros ++ the-machinery-arrives: [the-marks-beside-her-name-invisible-to-her, the-notation-the-machine-added-without-her-knowledge] | licensed-by: state-update:10, state-update:11, proto:64

8  @64 actor:census-officer ++ the-machinery-arrives: [the-two-parallel-lines-as-notation-not-judgment, the-annotation-that-travels-with-her-name] | licensed-by: state-update:10, proto:64

9  @64 episode ++ the-machinery-arrives: [the-notation-sealed-with-the-ledger, the-officer-who-exited-with-the-ledger] | licensed-by: state-update:10, proto:64

10 @74 actor:taylor-hebert-westeros ++ the-letter: [still-in-her-fist-at-the-threshold, the-object-she-carries-through-the-door] | licensed-by: proto:49, proto:74, proto:77, state-update:12

11 @77 actor:taylor-hebert-westeros ++ the-septon-as-absence: [the-door-she-can-open-after-the-machine-leaves, the-return-to-find-what-waits] | licensed-by: state-update:12, memory:3, proto:70, proto:77

12 @77 episode ++ the-letter: [still-carried-through-the-threshold, the-object-that-entered-the-sept] | licensed-by: state-update:12, proto:74, proto:77

---

# Caveats

**caveat-001 (rubric merge):** V1.1 patch text (`design/shoot-v2/rubric-vibes-v1.1-patch.md`) merges into main rubric file at this ship commit. Future auditor coherence depends on V1.1 being readable inline.

**caveat-002 (margit referral, contingent):** `prop:oc-letter` has no card. A prop-level vibe entry for the letter (`prop:oc-letter + the-useless-document` or similar) is deferred pending margit referral resolution. Margit list extends from state-updates' caveat (oc-letter + oc-district-ledger card authoring) and metaphor's caveat (monument-emma-betrayal etc.). Becomes MODERATE if unresolved before s01e02 authoring.

**caveat-003 (pre-seeded-project notation):** Sparsity 15.6% (12/77) sits within the addendum's pre-seeded expected range (9-14 for `++`-and-fresh-add subset). The corpus-specified 16-20 figure assumes a clean-slate project. This project is pre-seeded by world-build / project-activation; the loaded vibe-clouds in `actors/*/vibes.md` and `staff/studio/vibes.md` constitute authoritative existing state. RF-001 resolution: STRICT reading. See V1.1 patch §1.

**caveat-004 (showrunner write-back action):** Twelve delta entries must be applied to actor and studio vibe-cloud files at the cross-facet → stitch boundary, before s01e02 facet authoring begins. Specifically:
- `actor:mira-stonefield/vibes.md` — append the-yard-as-witness ++ tokens
- `actor:edric-cray/vibes.md` — append the-yard-as-witness ++ tokens
- `actor:taylor-hebert-westeros/vibes.md` — append ++ tokens to the-machinery-arrives, the-letter, the-septon-as-absence
- `actor:census-officer/vibes.md` — append the-machinery-arrives ++ tokens
- `actor:septon-dying-protector/vibes.md` — add the-septon-as-absence keyword + bundle (fresh `+`)
- `loc-harrenhal-sept-environs.card.md` — add VIBES section with the-machinery-arrives + the-septon-as-absence keywords + bundles (fresh `+` × 2)
- `staff/studio/vibes.md` EPISODE_1_VIBES — append ++ tokens to the-machinery-arrives, the-letter, the-yard-as-witness

**caveat-005 (read-side coherence — verified):** Phase 5 read-side coherence check passed. The 12 vibe-writes do not retroactively invalidate any locked s01e01 upstream facet (state-updates, memory, feeling, sensory, NI, metaphor). Per V1.1 patch §4 (pre-render hazard clause), `++` extensions are write-side bias for FUTURE renders (s01e02+) and do not alter the s01e01 locked facet record.

# Cross-facet contract notes (forward to downstream consumers)

- **Showrunner (canonical write-back consumer):** 12 deltas to apply at the cross-facet → stitch boundary; see caveat-004 for target file map.
- **Stitcher:** 12 vibe-writes register operator-bias state for s01e02-open. They do not appear in s01e01 prose. Stitcher reads vibes-updates as ambient context for downstream facet authors, not as render content.
- **Future-episode authors (s01e02+):** Taylor's vibe-set at s01e02 open inherits 9 pre-loaded keywords from world-build + 3 ++ extensions from s01e01 facet (the-machinery-arrives, the-letter, the-septon-as-absence with new s01e01-derived tokens). Mira/Edric inherit `the-yard-as-witness` ++ extensions. Census-officer inherits `the-machinery-arrives` ++ extension. Septon-dying-protector inherits new `the-septon-as-absence` keyword. Loc-harrenhal-sept-environs inherits two fresh keyword sets (the-machinery-arrives + the-septon-as-absence). Episode-scope EPISODE_1_VIBES inherits 3 ++ extensions on the-machinery-arrives, the-letter, the-yard-as-witness.
- **Dialogue-writer fork (s01e02+):** read each actor's vibe-set before voice generation. The new s01e01-derived tokens bias toward post-confrontation registers (Taylor: marks-beside-her-name-invisible / still-in-her-fist-at-the-threshold / the-door-she-can-open; Edric: sept-interior-as-exit-destination; Mira: pre-positioning awareness).
- **Studio (s01e02+):** read loc-harrenhal-sept-environs vibe-set before environmental description. The sept now carries charged-absence + authority-day-legibility registers.

# Lift trajectory

| Stage | Result |
|---|---|
| Phase 1 V2 strict (naive baseline; rubric-blind showrunner) | 0/29 = 0% |
| Phase 2 mechanic (rubric-aware showrunner fork) | 6/11 = 54.5% (+54.5pp) |
| Phase 3 adversarial seams | 7 cross-cutting seams + per-entry seams; RF-001 load-bearing |
| Phase 4 defense/revise | 12 final entries (3 DEFEND + 3 REVISE + 2 DELETE + 3 NEW + 1 NEW-edric + 0 from corpus phantom adds) |
| Phase 5 mechanic adjudication | **12/12 = 100%** |

**Lift from V2 baseline 0% to Phase 5 strictly-clean 100%: +100pp** — ties feeling-flags and metaphor-flags as largest absolute lift in the run-set.
