facet: vibes-updates (authoring working notes / proto-lines)
episode: b01c05
author: showrunner
generated: 2026-05-28
---

# Authoring notes — vibes-updates for b01-c05
# R2 resolves provisional licensed-by anchors where facet IDs are pending.

## Pre-seeded state audit (per V1.1 Patch 1 gate-2 requirement)

### actor:taylor-hebert-kl-122ac — pre-loaded keywords (from actors/taylor-hebert-kl-122ac/vibes.md)
  cold-utilitarian interiority       → PRESENT → ++ eligible
  penitential-grey King's Landing    → PRESENT → ++ eligible
  tragic-causal                      → PRESENT → ++ eligible
  contempt-without-refusal           → PRESENT → ++ eligible (formation-phase; d13 articulation pre-loaded; tokens must be non-duplicate)
  smallfolk-gallows register         → PRESENT → no new tokens from b01c05; SKIP
  residue not spectacle              → PRESENT → ++ eligible
  atonement-as-repetition            → PRESENT → ++ eligible (foreclosure-repetition-structure at @28-@31)
  rising entrapment                  → PRESENT → ++ eligible (FIRST on-page door-close at @25)
  khepri-memory-as-standard          → PRESENT → no new activation in b01c05; SKIP
  insect-sense-as-residue-not-spectacle → PRESENT → feed-generates-resentment is new event-frame but separate keyword justified; ++ not clean
  earth-bet-noun-fence               → PRESENT → no new token; SKIP
  cost-signature-range-bound         → PRESENT → no new token; SKIP

  NEW keywords on actor:taylor:
    courier-body-on-map              → fresh + (keyword absent; cf-d10 anchor)
    feed-as-resentment-generator     → fresh + (keyword absent; qualitative-consequence of political_register-prot +1.5 not covered by existing bundles)

### loc:the-rushwick — pre-loaded keywords
  No prior vibe-set (location new in b01c05; card pending margit). All entries are fresh +.
  Gate-1 advisory: rubric-carve-out preamble in vibes.md covers entries 9-11.

### episode — pre-loaded keywords
  No prior episode-scope vibes (b01c05 is first episode with its own vibes.md file in this project; no world-build pre-load for episode scope).
  Fresh + operations throughout.

### season / series — scope check
  No season or series scope entries warranted by b01c05 events. Political_register-prot opening is chapter-class; series arc is not materially advanced beyond what world-build vibe-cloud already covers. SKIP.

---

## Event-to-vibe mapping

### Event 1: court-tier bodies enter feed (@1-@7, scene-A)
  Bones involved: @4 provisioner-train crosses junction, @5 provisioner-train takes east-lane, @6 message-runner crosses junction, @7 message-runner takes lane-mouth
  Peak-bone: @7
  Vibe-causing quality: novel substrate — institutional-gait class distinct from Hook bodies; the method holds but the substrate has changed
  Affected entities:
    actor:taylor-hebert-kl-122ac → tragic-causal ++, residue not spectacle ++, cold-utilitarian interiority ++, penitential-grey King's Landing ++
    loc:the-rushwick → court-tier-substrate + (fresh)
  Licensed-by (provisional): proto:5, proto:7, state-update:2, world-build:Sera-protection-arrangement, peak-bone:7

### Event 2: enforcement incident observed (@8-@19, scene-B)
  Bones involved: @10-@13 (figures close alley, pin courier, alley-sound), @14 courier finds feet, @15-@16 Taylor files Jarvis report, @18 courier added to body-map
  Peak-bone: @13 (gap-instrument; feed has no field for effortful sound)
  Vibe-causing quality: faction-violence absorbed as categorizable data; the discipline holds at action-layer; the gap between world and feed instantiated
  Affected entities:
    actor:taylor-hebert-kl-122ac → penitential-grey King's Landing ++, cold-utilitarian interiority ++, courier-body-on-map +
    loc:the-rushwick → enforcement-geometry-resident + (fresh)
    episode → faction-violence-as-feed-content + (fresh)
  Licensed-by (provisional): proto:13, proto:14, proto:15, proto:16, proto:18, feeling:1, state-update:3, peak-bone:13

### Event 3: evening replay foreclosure (@20-@31, scene-C)
  Bones involved: @22 Hook resolves, @24 provisioner-train re-crosses, @25 Taylor stops rushwick-pass (+1.5 axis), @27 courier body-record filed, @28-@31 flat-read attempts fail
  Peak-bone: @25 (recognition-cessation; +1.5 political_register-prot)
  Vibe-causing quality: neutral-instrumentally-observant foreclosed; door closed; cl-d05 anchor lands; feed revealed as resentment-generator; foreclosure enacted as body-act twice (provisioner-train @29, courier-walk @31)
  Affected entities:
    actor:taylor-hebert-kl-122ac → rising entrapment ++, feed-as-resentment-generator +, contempt-without-refusal ++, tragic-causal ++, atonement-as-repetition ++
    episode → foreclosure-enacted +, faction-violence-as-feed-content ++ (both absorption and foreclosure in same chapter)
  Licensed-by (provisional): state-update:6, state-update:8, feeling:2, proto:25, proto:27, proto:28-proto:31, peak-bone:25, peak-bone:29, canon:contempt-arrives-articulate-d13

---

## Seam flags for R2

SEAM-1 (semantic-adjacency advisory, AP11):
  vibes:2 (residue not spectacle ++) tokens include `insect-sense-now-generating-political-affect`
  vs
  vibes:13 (feed-as-resentment-generator +) token `insect-feed-generates-political-affect-without-being-directed-to`
  These are in different keywords on the same target. String-overlap test: PASS (different token strings). Semantic-adjacency: PRESENT — both address feed-generates-affect.
  Distinction justification: `residue not spectacle` tokens address HOW the feed presents (substrate, class-reading, register); `feed-as-resentment-generator` tokens address WHAT the feed produces (political-affect, accrual mechanism, naming-gap). Downstream operators would use them differently: residue-not-spectacle biases sensory/NI register toward texture; feed-as-resentment-generator biases feeling/dialogue toward accumulation-register. Semantic frames are distinct.
  R2 determination: verify the frame-distinction holds; if not, consolidate to `residue not spectacle ++` and retire `feed-as-resentment-generator` as redundant.

SEAM-2 (licensed-by resolution — provisional proto: IDs):
  All `proto:<id>` citations are provisional flat-IDs matching bones file @N notation. At R2, the cite-index builder assigns canonical proto-line IDs; these must be verified match @N as expected. If any bone was split or merged during proto-line build, IDs may shift.

SEAM-3 (feeling:1 and feeling:2 citations):
  vibes:5 licensed-by feeling:1 (@13 — hand opens against wall-stone)
  vibes:12 / vibes:13 / vibes:14 licensed-by feeling:2 (@25 — hand lifts off floor)
  These are the two feeling-flags authored in feeling-taylor-hebert-kl-122ac.md. At R2, verify these IDs are stable (file shows entries 1 and 2; should map cleanly).

SEAM-4 (loc:the-rushwick gate-1 deferral):
  R2 must confirm whether margit has authored oc-rushwick.card.md and check the slug matches `the-rushwick` in the vibes entries. If slug differs, entries 9-11 require slug correction.

SEAM-5 (atonement-as-repetition ++ entry 17 token length advisory):
  Token `the-feed-that-was-supposed-to-be-neutral-accretes-the-same-way-the-power-was-supposed-to-be-contained` (17 segments) — long compression.
  AP8 sentence-parsability test: no standalone finite-verb-with-subject-predicate; reads as a noun-phrase with double participial-modifier structure; PASS by formal test.
  Semantic-adjacency to existing bundle: existing `atonement-as-repetition` bundle contains `specific-shape-of-what-she-can-do-meets-what-the-situation-required` and `came-to-refuse-control`. New token adds the FEED as the doubled-structure vehicle (power suppression :: feed neutral-read). Event-frame is distinct (power-is-the-thing vs feed-is-the-thing). Advisory: if R2 auditor reads the 17-segment token as internally multi-clausal, split to `feed-was-supposed-to-be-neutral` + `accretes-the-same-way-the-power-did`.

---

## Fan-out coverage check

| Event | Required fan-out | Entries authored | Gap? |
|-------|-----------------|-----------------|------|
| Court-tier bodies enter feed | taylor + the-rushwick + episode (optional) | 1,2,3,4 (taylor) + 9 (loc) | episode-scope SKIPPED — court-tier-bodies entering feed is subplot-level not episode-defining. Justified by AP9 (entity-target preferred). |
| Enforcement incident | taylor + the-rushwick + episode | 5,7 (taylor) + 10 (loc) + 6 (episode) | COVERED |
| Evening replay / foreclosure | taylor (primary) + episode | 12,13,15,16,17 (taylor) + 14,18 (episode) | COVERED |
| cf-d10 courier thread anchor | taylor | 8 (taylor) | COVERED; courier not a full actor (unnamed); no separate actor target |
| loc:the-rushwick as host location | loc | 9,10,11 (loc) | COVERED |

Fan-out verdict: all structurally required fan-outs are present. Episode-scope skip on court-tier-entry event is AP9-justified (entity targets carry the weight; episode-scope would be redundant).

---

## Entry count summary

actor:taylor-hebert-kl-122ac entries: 13 (entries 1,2,3,4,5,7,8,12,13,15,16,17 — counting unique target-fires)
  ++ extends: tragic-causal(2), residue-not-spectacle(1), cold-utilitarian-interiority(2), penitential-grey-KL(2), rising-entrapment(1), contempt-without-refusal(1), atonement-as-repetition(1)
  + fresh: courier-body-on-map(1), feed-as-resentment-generator(1)

loc:the-rushwick entries: 3 (entries 9,10,11)
  + fresh: court-tier-substrate(1), enforcement-geometry-resident(1), penitential-grey-absorbed(1)

episode entries: 3 (entries 6,14,18)
  + fresh: faction-violence-as-feed-content(1), foreclosure-enacted(1)
  ++ extend: faction-violence-as-feed-content(1) — both events in same chapter; extension adds foreclosure-connection

Total unique vibes.md entries: 18
