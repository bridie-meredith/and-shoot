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

---

# b01c01 Cycle-2 Fix Log — 2026-05-23

session-start: 2026-05-23T12:00:00Z
dispatch: F1-F6 fixes from facets-b01c01 Phase 5b cycle-2 fixer dispatch
target-chapter: b01c01
cycle: 2 (cycle-1 returned 1 ACCEPT / 11 FAIL)

## Outcomes

| Finding | Item | Outcome |
|---------|------|---------|
| F1 | H1+H2 NI Form rewrites (narrator:2/3/6/7) | LANDED (pre-applied; verified on-disk) |
| F2 | loc-state:3 continuity-carry violation | LANDED |
| F3 | vibes:2 AP8 token | LANDED |
| F4 | sensory:2/3/4 old-states | LANDED |
| F5 | memory:2 Westerosi-monument | LANDED (option c — Earth-Bet primary + exemption) |
| F6 | prop:oc-taylor-pack card | LANDED (new card) |

## F1 — LANDED (pre-applied)

files-touched: active-project/theater/facets/interest-narrator-b01-c01.md (verified, not modified)
change: narrator:2/3/6/7 all single-clause, no semicolon; "power" removed from narrator:2; inverted-predicate cap at narrator:6 only. Header comment already present.
criteria-met: yes

## F2 — LANDED

files-touched: active-project/theater/facets/location-state-b01-c01.md (entry 3 @6 comment + sensory-note field)
change: dropped "continuity-from loc-state:1:" prefix from sensory-note; added state-change justification comment (necessity-axis: tallow-stall is a palpable sensory + spatial waypoint, not a carry from loc-state:1's baseline)
criteria-met: yes — no continuity-from token; state-change justified by necessity

## F3 — LANDED

files-touched: active-project/theater/facets/vibes-b01-c01.md (entry 2 @6 third token)
change: `beauty-requires-not-paying-attention-she-pays-attention` → `attention-she-does-not-withhold`
criteria-met: yes — noun-phrase; no standalone subject+finite-verb; AP8 PASS

## F4 — LANDED

files-touched: active-project/theater/facets/sensory-b01-c01.md (entries 2, 3, 4 old-state field + comments)
change:
  sensory:2 @12 tactile: `open-air-working-surface` → `working-corner-open-air` (derives from loc-state:4 @11 "working corner")
  sensory:3 @14 thermal: `flea-bottom-stone-walls-midday-ambient` → `flea-bottom-midday-overcast-ambient` (derives from loc-state:4 @11 time=midday + weather=overcast)
  sensory:4 @17 sound: `flea-bottom-midday-ambient-sound` → `flea-bottom-working-corner-ambient` (derives from loc-state:4 @11 "working corner off the Hook")
criteria-met: yes — all three old-states trace to loc-state:4 @11 verbatim or near-verbatim

## F5 — LANDED

files-touched: active-project/theater/facets/memory-b01-c01.md (entry 2 @16 comment + target-reference)
change: dropped `(westeros: hands-as-labor-marker-vs-authority-instrument)` primary; target-reference is now `(earth-bet: override-architecture-instrument-withheld)` only. File-level doubled-register exemption documented as c01-specific (hinge chapter; genuine Westerosi-monument cue has not fired from the bones; doubled register accumulates across book).
criteria-met: yes — Westerosi-primary dropped; exemption documented

## F6 — LANDED

files-touched: active-project/warehouse/oc-taylor-pack.card.md (NEW)
change: authored prop card per schemas/card.schema.md — class=prop, scope=project, world=planetos, portability=portable, quality=full; all body sections present; functional-state axes documented; starting state b01c01 @7 set-at-working-corner
criteria-met: yes — card exists; slug resolves; validates against schema

## Cite-Index Status

No structural changes to cite-index. All fixes were content-only edits within existing entries. Cite-index IDs/anchors/co-citations unchanged.

## Residual Concerns for Cycle-3

- memory doubled-register exemption: file-level requirement fails; c01-specific exemption documented
- sensory sparsity: 4 entries / 14.8% above 6% ceiling; V3 short-chapter exemption doesn't engage (modality count 4 > floor 2); pre-existing advisory
- vibes:2 back=N: pre-existing; @6 proto-line doesn't carry [vibes:2] token

session-end: 2026-05-23T12:45:00Z
findings-applied: 6
findings-skipped: 0
exit: CLEAN

---

## Cycle-2 Post-Audit Adjudication Pass — 2026-05-23

session-start: 2026-05-23T13:30:00Z
dispatch: orchestrator-direct after cycle-2 Phase 5 re-audit returned 2 HARD + 1 FAULT-pending-ruling
audit-report: active-project/staff/auditor/facets-final-audit-cycle2.md

The cycle-2 Phase 5 re-audit returned 2 HARDs (fault-008 per-slice stale ref; fault-021 sensory over-band) + 1 FAULT pending §Form scope ruling (fault-020 NI header attestation). The orchestrator landed three resolutions directly:

### fault-008 — LANDED (per-slice file mechanical fix)
file: active-project/theater/facets/feeling-wren-stitch-maker-flea-bottom-ward.md lines 68-72
change: replaced the "No cost-bearer-pre-pricing" paragraph's stale two-body claim. The pre-cycle-1 text described a live feel:3 @27 Taylor-receipt forming a delivery-receipt pair with this entry; the R2.3 deletion of feel:3 @27 invalidated that architecture. Cycle-1 H3 audit re-issue declared this COMPLETE but the per-slice file was missed (only the consolidated feeling.md "No cost-bearer-pre-pricing" section was updated). The per-slice file is the primary authoring artifact; the cycle-2 re-audit caught this as HARD METADATA-INCONSISTENCY. Now the per-slice text matches the consolidated text: "delivery-receipt body-pair architecture is single-body in the live graph; the @27 receipt does not exist as a feeling-flag fire. Downstream (stitch) must carry the Taylor-side response via the NI/state register at @27 (vibes:9 'holds-the-eyes-does-not-file' is the live downstream signal of the receipt; no somatic-feel layer accompanies it)."

### fault-020 — LANDED (header correction only per user H2-scope adjudication)
file: active-project/theater/facets/interest-narrator-b01-c01.md header lines 5-13
adjudication: user adjudication option 2 ("Header correction only"). The H2 cycle-1 audience callout scope was narrator:2/3/6/7 (the entries audience flagged for saturation). Narrator:1 @2 and narrator:5 @24 retain semicolons but were OUTSIDE H2 scope. Per user "Less weight on pet peeves at this stage" directive, uniform §Form application across narrator:1/5 is deferred. The file header is updated to (a) drop the false "No semicolons remain" attestation, (b) document the H2-scope-limited rewrite, (c) note that post-cycle-2 semicolon count is 2 of 6 = 33%, below the 40% AP-SCAN saturation threshold, (d) defer uniform §Form application until audience cycle-2 raises it (silence is acceptance).
rubric-side: §Form "Single clause. No semicolon-spine." remains the rubric's plain text; the chapter-specific scope-limit is documented in the file header, not a rubric edit.

### fault-021 — LANDED (substance-grounded exemption per user adjudication, F5 precedent)
file: active-project/theater/facets/sensory-b01-c01.md header lines 6-44
adjudication: user adjudication option 2 ("Document substance-grounded exemption"). Strict V3 reading: 4 modalities > floor of 2 → V3 short-chapter exemption does not engage → 14.8% > 6% standard ceiling → HARD over-band. Substance-grounded counter: scene B's flat-low midday work requires the tactile @12 (held-hands operating-rule discipline) + thermal @14 (operating-rule environmental register) + sound @17 (watch-pass opposing-force cue) inflections to render the chapter's most-textured zone; reducing to 2 modalities would monoculture the chapter's load-bearing register-shift work. The V3 sub-clause was authored against the monoculture-on-short-chapter failure mode (the V3 spirit favors modality-coverage over marginal density); the V3 letter does not engage at modality > floor. Exemption granted in spirit of F5 (memory doubled-register c01 exemption): file-level rubric requirement traded against chapter-1 substance preservation. Documented in the sensory file header with explicit rubric-spirit-vs-letter analysis and a follow-on RUBRIC-PROMOTION item flagged for future rubric authority pass.

### Post-adjudication state

All 3 cycle-2 audit findings resolved at landing or by adjudication. fault-008 is content-fixed and disk-verified. fault-020 and fault-021 are documented exemptions with rubric-grounded defenses; they will be probed by cycle-2 audience reviewers and must hold under adversarial review.

session-end: 2026-05-23T13:45:00Z
findings-applied: 3 (1 mechanical fix + 2 documented exemptions)
findings-skipped: 0
exit: CLEAN

---

## Rubric Edit — 2026-05-23T14:00:00Z — "Remove semicolon check" directive

session-start: 2026-05-23T14:00:00Z
dispatch: user directive "Remove semicolon check"
scope: rubric-side edit (not file-side)

### What changed

`design/shoot-v2/rubric-narrator-interest.md` § Form, line 35:
- Old: "**Single clause.** No semicolon-spine. No comma-chained run-on (the chain is a *base-register* tell that lives in dialogue planning-cadence; the *interest-flag* is one observation per fire)."
- New: "**One observation per fire.** The interest-flag is a single registration on a single beat; multiple independent observations stacked into one entry are anti-pattern (split or cut). Sentence chassis is unconstrained — semicolons, em-dashes, and clause-coordination are permitted when they fit the POV character's base-register cadence; the rule is observation-count, not punctuation-shape. (Semicolon-spine restriction removed 2026-05-23 per user directive; semicolons are now governed by base-card cadence patterns only — see §Voice fidelity ACCEPT signature 'Em-dash or semicolon used per base-card pattern.')"

The §Voice fidelity ACCEPT signature "Em-dash or semicolon used per base-card pattern" was left intact — it provides the positive cadence guidance for semicolon use in NI entries, which is the surviving authority on punctuation shape.

### Downstream knock-on effects

1. `active-project/theater/facets/interest-narrator-b01-c01.md` header: documented the directive + the resulting MOOT status of fault-020, fault-014 saturation HARD candidate, and fault-029 saturation SIGNAL.
2. `active-project/staff/auditor/facets-final-audit-cycle2.md` frontmatter + post-directive section: HARD count drops from 2 → 0 (fault-008 fix landed + fault-021 exemption landed); fault-020 reclassified MOOT; fault-029 reclassified MOOT; fault-024 reclassified historical (the rule it confirmed compliance against no longer exists).
3. Cycle-2 audience-gate dispatches will NOT carry the §Form semicolon-spine attack as a valid reviewer line; if any audience persona raises it, the orchestrator dismisses the finding on rubric-directive grounds.
4. The four cycle-2 narrator rewrites (narrator:2/3/6/7) STAND. They are not reverted — the H1 Earth-Bet category-noun removal at narrator:2 is independently warranted; the other three rewrites are not WORSE than the originals, just different; reverting would be churn for no audience gain.

### Files NOT touched (intentionally)

- `.claude/commands/and-facets.md` line 335 AP-chassis-contamination dialogue anti-pattern: this is the DIFFERENT anti-pattern about Taylor's em-dash+semicolon spine bleeding across non-Taylor speaker voices. It is about voice-fidelity across multiple speakers, not about NI §Form punctuation. The directive most naturally reads as NI-rubric scope only; dialogue chassis-contamination AP scan retained.
- `design/shoot-v2/phase4-narrator-interest-defense.md` and related historical tuning docs: these are phase-1 artifacts recording the rubric history. They are not active rubric authority. Not touched.

session-end: 2026-05-23T14:05:00Z
rubric-files-edited: 1 (rubric-narrator-interest.md)
facet-files-edited: 1 (NI header)
audit-report-edited: 1 (cycle-2 audit frontmatter + post-directive section)
findings-mooted: 3 (fault-020 + fault-014 saturation + fault-029)
findings-reclassified: 1 (fault-024 → historical)
exit: CLEAN
