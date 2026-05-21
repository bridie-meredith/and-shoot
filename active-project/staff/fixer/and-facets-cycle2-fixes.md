# /and-facets b01c02 — Phase 5b cycle-2 fix log

session-start: 2026-05-21T15:00:00Z
dispatch: resolve 9 numbered items + item 8b (10 callouts) from and-facets-cycle2-callouts.md
target-chapter: b01c02
cycle: 2 (cycle-1 failed 10 of 11; metaphor passed)

---

## item-1 — FIXED-DIRECT — 2026-05-21T15:05:00Z
verdict: FIXED-DIRECT
files-touched: active-project/theater/facets/vibes.md (entry 14 keyword only)
change: `earning-collapse` → `wren-layer-actualization`
dependency-conflicts: none — token bundle, anchor, licensed-by unchanged; vibes:14 cite-index ID unaffected; taylor sidecar facet-licenses in item-3 cites `vibes:14` (ID), so keyword rename does not break the citation
proto-line-citation-moved: no

## item-2 — FIXED-DIRECT — 2026-05-21T15:06:00Z
verdict: FIXED-DIRECT
files-touched: active-project/theater/facets/vibes.md (entry 1 target and keyword)
change: target `actor:taylor-hebert-kl-122ac ++ insects:` → `episode + first-deployment-routing-mode:`; keyword change embedded in target restructuring; @5 anchor held; token bundle unchanged
dependency-conflicts: cite-index records vibes:1 co-citations as co=[loc-state:3, narrator:2, state:2, state:11, vibes:2, vibes:3, vibes:4] — the co-citation is based on anchor @5, not on the target field; no cite-index change needed
proto-line-citation-moved: no

## item-3 — FIXED-DIRECT — 2026-05-21T15:07:00Z
verdict: FIXED-DIRECT
files-touched: active-project/staff/dialogue-writer/wren-stitch-maker-flea-bottom-ward.drafts.md (Draft B facet-licenses); active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md (Entry 1 + Entry 2 facet-licenses)
change: three DEFERRED-TO-R2 placeholders replaced with concrete citations (vibes:13 @19; vibes:14 @20 x2)
dependency-conflicts: vibes:14 keyword renamed in item-1 (earning-collapse → wren-layer-actualization) but cite-index ID unchanged; citations resolve correctly
proto-line-citation-moved: no

## item-4 — FIXED-DIRECT — 2026-05-21T15:08:00Z
verdict: FIXED-DIRECT
files-touched: active-project/theater/facets/exposition-b01-c02.md (entry 4 gloss-text inline appositive)
change: "In Flea Bottom there is rarely anyone who can." → "In Flea Bottom, the city's poorest ward, there is rarely anyone who can."
dependency-conflicts: "the Hook" confirmed on glossed-terms register from b01c01; no change to bridge text needed
proto-line-citation-moved: no

## item-5 — FIXED-DIRECT — 2026-05-21T15:12:00Z
verdict: FIXED-DIRECT
files-touched: active-project/theater/facets/feeling.md (entries 1 and 2)
change: feel:1 @28 recast from compound-predicate to "her hand draws back from the ledger's edge"; feel:2 @15 recast from three-motion-unit compound-complex to "her eyes come to rest on Taylor and do not leave"
dependency-conflicts: none — IDs unchanged; expressed: fields unchanged; no proto-line token moves
proto-line-citation-moved: no

## item-6 — FIXED-DIRECT — 2026-05-21T15:15:00Z
verdict: FIXED-DIRECT
files-touched: active-project/theater/facets/interest-narrator.md (entry 4)
change: narrator:4 @15 revised to surface age-mismatch channel before ledger-frame and remove trailing preposition "about"
dependency-conflicts: none — ID and anchor unchanged; no proto-line token moves
proto-line-citation-moved: no

## item-7 — FIXED-DIRECT — 2026-05-21T15:17:00Z
verdict: FIXED-DIRECT
files-touched: active-project/theater/facets/location-state.md (entry 4, sensory-note field)
change: sensory-note rewritten from spatial-arithmetic ("remaining clear ground...") to concrete perceptible thing ("Wren's figure against the far-end threshold, the sealed lane-mouth directly behind her")
dependency-conflicts: none
proto-line-citation-moved: no

## item-8 — FIXED-DIRECT — 2026-05-21T15:22:00Z
verdict: FIXED-DIRECT
files-touched: active-project/theater/facets/state-updates.md (entries 10, 12, 13, 15); active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md (entries 2, 3); active-project/theater/facets/state-updates-coll-net-mender-flea-bottom.md (entry 1); active-project/theater/facets/state-updates-wren-stitch-maker-flea-bottom-ward.md (entry 2)
change: (10) new-value `registered-as-anomaly` → `glance-filed-unrepeated`; comment updated to remove cape vocabulary and resolve both fences explicitly; (12) `crystallized-observer-bond` → `recognized-observer-bond-forming`; (13) `categorical-structural` → `structural-first-read-provisional`; (15) `attachment-crystallized-deliberate-observer` → `watching-with-dread-held-alongside-pull`
dependency-conflicts: none; all IDs and anchors unchanged; no proto-line token moves (state values in field body only, not in IDs)
fixer-adjudication-note for state:13: worm-canon-pedant defended via parallel-processing capacity (1-of-3 accept); cape-fic + dark-fantasy rejected (2-of-3). 3-of-3 ACCEPT threshold requires revision. `structural-first-read-provisional` preserves the fast-synthesis signal while satisfying the provisioning requirement of the two revise reviewers.
proto-line-citation-moved: no

## item-8b — ADD-LANDED-AFTER-UPSTREAM-EDIT — 2026-05-21T15:28:00Z
verdict: ADD-LANDED-AFTER-UPSTREAM-EDIT (sensory:2 relocated @22→@23; upstream loc-state conditions notes added first per A3)
files-touched:
  - active-project/theater/facets/location-state.md (entries 2 and 11: conditions notes added)
  - active-project/theater/facets/sensory.md (entry 2: anchor moved @22→@23; both entries: old-state-source notes added)
  - active-project/theater/proto-lines/b01-c02.md ([sensory:2] moved from @22 to @23)
  - active-project/theater/facets/_cite-index.md (sensory:2 row updated @22→@23; loc-state:11, state:3, state:4 co-citations updated to remove sensory:2; state:5 and exposition:5 co-citations updated to add sensory:2)
change: A3 sequence: upstream loc-state conditions notes landed first (loc-state:2 @4 ambient-sound baseline; loc-state:11 @22 pre-lamp darkness baseline); then sensory entries updated (old-state-source anchors added; sensory:2 relocated to @23); then proto-lines and cite-index updated
dependency-conflicts: sensory:2 relocation required cite-index update — executed in same pass; no other downstream conflicts; ≥2-modality floor maintained (sound @7 + light @23)
proto-line-citation-moved: YES — [sensory:2] moved from @22 to @23; cite-index updated manually; orchestrator should note for any cite-index rebuild

---

## Session summary

session-end: 2026-05-21T15:40:00Z
findings-applied: 10
findings-skipped: 0
cite-index-rebuild-needed: YES — sensory:2 moved @22→@23; cite-index manually updated; confirm with build_cite_index.py
exit: CLEAN

---

## item-9 — ROUTED-TO-MARGIT / RESOLVED — 2026-05-21T15:35:00Z
verdict: ROUTED-TO-MARGIT (both monument cards authored in warehouse; fixer confirms resolution)
files-touched:
  - active-project/warehouse/monument-conquest-charter-language.md (NEW — class: behavior, scope: project)
  - active-project/warehouse/monument-cost-borne-by-the-unconsenting.md (NEW — class: behavior, scope: project)
change: both monument slug targets for mem:1 and mem:2 now resolve to on-disk warehouse cards; mem:2 peak-bone exception is anchored; no re-anchor or cull of mem:2 required
dependency-conflicts: none; memory.md unchanged (the target-reference slugs were already correct; the gap was the absence of the card files)
proto-line-citation-moved: no

