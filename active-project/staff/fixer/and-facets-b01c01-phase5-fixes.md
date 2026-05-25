# Fix Log — /and-facets b01c01 Phase 5 Remediation
date: 2026-05-25
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-count: 5 HARD
fixer-session: SESSION-START 2026-05-25T05:00:00Z in fixer-log.md

---

## fault-001 — RESOLVED

**fault:** proto-lines/b01-c01.md @12 cited [state:1][state:2] (Oswyn's pre-consolidation IDs: state:1=oswyn.location@21, state:2=oswyn.relationship@26). Taylor's deployment-state (state:3@12) and capability_axis (state:4@12) had back=N in the cite-index — the stitcher would have read Oswyn's state entries at the wrong bone. The chapter's capability+1 axis-move anchor was invisible to the stitcher.

**change (before/after):**
```
before: 12 the insects propagate [narrator:4] [state:1] [state:2] [vibes:3] [vibes:4] [vibes:8]
after:  12 the insects propagate [narrator:4] [state:3] [state:4] [vibes:3] [vibes:4] [vibes:8]
```

**verification:** cite-index regenerated. state:3 back=Y anchored @12; state:4 back=Y anchored @12. Co-citation lists for narrator:4, vibes:3, vibes:4, vibes:8 updated to replace state:1,state:2 with state:3,state:4.

---

## fault-002 — RESOLVED

**fault:** proto-lines/b01-c01.md @10 cited [feel:1][feel:2]. feel:1 is Oswyn's somatic tell anchored @21 ("the hands settle at the apron-front"). Citing feel:1 at @10 placed Oswyn's post-rescue composure tell before Oswyn had arrived on stage. The cite-index showed feel:1 back=Y keyed to @21 (via @21 citation) and also back-linked spuriously from @10.

**change (before/after):**
```
before: 10 taylor-hebert-kl-122ac holds the feet [feel:1] [feel:2]
after:  10 taylor-hebert-kl-122ac holds the feet [feel:2]
```

**verification:** cite-index regenerated. feel:1 back=Y anchored exclusively @21 (no back-link from @10). feel:2 back=Y anchored exclusively @10.

---

## fault-003 — RESOLVED

**fault:** proto-lines contained five additional citation-ID mismatches from the same root cause (pre-consolidation ID namespace used post-consolidation):
- @17 cited [state:3] (Taylor deployment @12) instead of [state:5] (Taylor posture @17)
- @21 cited [state:4] (Taylor capability @12) instead of [state:6] (Taylor social_tether @21)
- @24 cited [feel:2] (Taylor breath @10, wrong anchor) + [state:5] (Taylor posture @17) instead of [feel:3] + [state:7] (Taylor body-orientation @24)
- @26 cited [state:6] (Taylor social_tether @21) instead of [state:8] (Taylor ward-recognition @26)
- @27 missing [state:9] (Wren relational_anchor @27) entirely

**change (before/after):**
```
before: 17 taylor-hebert-kl-122ac lifts the hands [state:3]
after:  17 taylor-hebert-kl-122ac lifts the hands [state:5]

before: 21 oswyn-mudway-flea-bottom-elder takes the lane-mouth [exposition:8] [feel:1] [narrator:5] [state:1] [state:4] [vibes:5] [vibes:6] [vibes:7]
after:  21 oswyn-mudway-flea-bottom-elder takes the lane-mouth [exposition:8] [feel:1] [narrator:5] [state:1] [state:6] [vibes:5] [vibes:6] [vibes:7]

before: 24 taylor-hebert-kl-122ac faces the alley-mouth [feel:2] [feel:3] [narrator:8] [state:5]
after:  24 taylor-hebert-kl-122ac faces the alley-mouth [feel:3] [narrator:8] [state:7]

before: 26 oswyn-mudway-flea-bottom-elder lifts the chin [mem:2] [state:2] [state:6]
after:  26 oswyn-mudway-flea-bottom-elder lifts the chin [mem:2] [state:2] [state:8]

before: 27 wren-stitch-maker-flea-bottom-ward faces taylor-hebert-kl-122ac [exposition:9] [feel:4] [narrator:6] [vibes:9] [vibes:10]
after:  27 wren-stitch-maker-flea-bottom-ward faces taylor-hebert-kl-122ac [exposition:9] [feel:4] [narrator:6] [state:9] [vibes:9] [vibes:10]
```

**verification:** cite-index regenerated. All post-consolidation IDs now carry back=Y at their correct anchors:
- state:3 back=Y @12 (was back=N)
- state:4 back=Y @12 (was back=N)
- state:5 back=Y @17 (was back=N)
- state:6 back=Y @21 (was back=N)
- state:7 back=Y @24 (was back=N)
- state:8 back=Y @26 (was back=N)
- state:9 back=Y @27 (was back=N)
- feel:1 back=Y exclusively @21 (spurious @10 back-link removed)
- feel:2 back=Y exclusively @10 (spurious @24 back-link removed)
- feel:3 back=Y exclusively @24 (confirmed)

**cite-index note:** The cite-index file was updated manually (no shell execution available in this fixer run). The `/and-stitch b01c01 Phase 0` cite-index hash check must re-hash `active-project/theater/facets/_cite-index.md` against the updated proto-lines file before proceeding. If `build_cite_index.py b01-c01 --skip-merge` is available in the pipeline runtime, running it will confirm the manual update is consistent with the script's derivation.

---

## fault-004 — DOWNGRADED TO FLAG

**fault:** 3 utterances from taylor-hebert-kl-122ac anchored @16; per-speaker per-anchor sub-cap "no two utterances of the same speaker at the same anchor unless deliberate single-turn split documented in drafts sidecar" cited as potentially breached.

**rubric determination:** `staff/dialogue-writer/rubric-dialogue.md` § "Per-anchor caps" reads:
> "No two utterances of the same speaker at the same anchor unless they are a deliberate single-turn split (e.g. interruption-of-self, beat-and-clarify). Multi-entry single-turn must be justified in the drafts sidecar."

The exception path IS satisfied:

1. The s02 chunk text explicitly specifies three discrete information-deliveries: "fever, not dying, needs air and water and someone whose name she knows." Three separate board-moves, not one message split arbitrarily.
2. The drafts sidecar (`active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md`) documents per-entry Q1+Q2 rationale for each of the three utterances at @16, with distinct objectives (diagnosis / physical-intervention imperative / known-adult routing).
3. The sidecar explicitly notes "Per-anchor count: 3 (cap = 3; at cap)" and documents why each utterance is a distinct board-move.
4. The parking-lot resolution (pl-2026-05-25-004) confirmed routing (a) with three utterances matching the chunk's three-part information delivery.

**change:** none.

**rationale note (flag form):** The audit-class spec language "per-anchor cap ≤3 AND per-speaker per-anchor ≤1" is ambiguous when read in isolation. The rubric body grants the exception when documented as deliberate single-turn split. The auditor's criteria correctly required fixer to determine which rule is operative. Determination: per-speaker ≤1 sub-cap is the binding form, but the three-part chunk-delivery sequence satisfies the deliberate-single-turn-split exception as documented. Fault downgraded. No reduction of dialogue file required.

---

## fault-005 — RESOLVED

**fault:** vibes-b01-c01.md vibes:3 @12 token "instinct-preceded-the-ledger-entry" parses as a complete sentence: subject (instinct) + finite verb (preceded, past tense) + object (the-ledger-entry). Vibes schema forbids tokens that parse as subject+finite-verb+object; tokens must be noun-phrase form for word-algebra operator use.

**change (before/after):**
```
before: 3 [@12] actor:taylor-hebert-kl-122ac + the-first-crack: [prohibition-crossed-before-it-was-filed, instinct-preceded-the-ledger-entry, deployment-preceding-permission] | licensed-by: proto:12, proto:13
after:  3 [@12] actor:taylor-hebert-kl-122ac + the-first-crack: [prohibition-crossed-before-it-was-filed, instinct-preceding-the-ledger-entry, deployment-preceding-permission] | licensed-by: proto:12, proto:13
```

**token choice:** "instinct-preceding-the-ledger-entry" (gerund / present participle) chosen over "the-ledger-entry-outrun-by-instinct" (nominalised past-participle form). Rationale: "preceding" as a present participle modifying "instinct" maintains the active-before-filing semantic with the same actor-primacy as the original (instinct is the subject of the action, the ledger is the object of the preceding-relation). "the-ledger-entry-outrun-by-instinct" inverts the subject-prominence; "instinct-preceding-the-ledger-entry" preserves it. Both are grammatically noun-phrase form (no finite verb); "instinct-preceding-the-ledger-entry" chosen for semantic-primacy preservation.

**verification:** "instinct-preceding-the-ledger-entry" — "preceding" is a present participle (gerund modifier), not a finite verb. The token does not parse as subject+finite-verb+object. Schema constraint met.

---

## Summary

| fault | disposition | file changed |
|-------|-------------|--------------|
| fault-001 | RESOLVED | active-project/theater/proto-lines/b01-c01.md, active-project/theater/facets/_cite-index.md |
| fault-002 | RESOLVED | active-project/theater/proto-lines/b01-c01.md, active-project/theater/facets/_cite-index.md |
| fault-003 | RESOLVED | active-project/theater/proto-lines/b01-c01.md, active-project/theater/facets/_cite-index.md |
| fault-004 | DOWNGRADED TO FLAG | none |
| fault-005 | RESOLVED | active-project/theater/facets/vibes-b01-c01.md |

remaining HARDs: 0
