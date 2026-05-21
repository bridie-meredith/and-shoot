# Fixer Log

## SESSION-START — 2026-05-17T00:00:00Z — 1d-audit-fix-pass-1
dispatch: route 7 HARD findings from active-project/staff/auditor/1d-audit.md to minimum-change fixes
target: active-project/warehouse/* + cards/conditions/* (multiple card files)
audit-report: active-project/staff/auditor/1d-audit.md
findings-queued: 7 faults (fault-001 through fault-007) + 6 flags (flags not actioned)

## fault-001 — RESOLVED — 2026-05-17T00:01:00Z
fault: cond-khepri-residue-122ac scope conflict (scope: library with project: field)
scope: line
change: warehouse copy already had scope: project / project: taylor-hebert-kl-122ac (correct). Created library copy at cards/conditions/cond-khepri-residue-122ac.md with scope: project and project: taylor-hebert-kl-122ac. Both copies now consistent.
criteria met: yes

## fault-002 — RESOLVED — 2026-05-17T00:02:00Z
fault: cond-taylor-pov-behavior, cond-westerosi-witness-vocabulary, cond-maester-chronicler-voice declare subclass: behavior on class: condition cards (invalid subclass value)
scope: line
change: removed subclass: behavior field from all three warehouse copies. No valid condition subclass exists in schema; field removed per audit criteria. Library copies to be created without the field.
criteria met: yes

## fault-003 — RESOLVED — 2026-05-17T00:03:00Z
fault: cond-shard-behavioral-weight has dead references (taylor-hebert-flea-bottom, cond-series-tone-constraints-125ac from mirror-tragedy). Card is a library card from prior project.
scope: line
change: dropped cond-shard-behavioral-weight from this project's reference set by removing it from cond-taylor-pov-behavior's references: list. No warehouse card now points to it. Margit workshop ticket for cond-shard-behavioral-weight-122ac variant batched with fault-005 ticket (dispatched below).
criteria met: yes — dead reference chain severed; workshop ticket routing note appended

## fault-004 — RESOLVED — 2026-05-17T00:04:00Z
fault: cond-dance-faction-state-previserys is mirror-tragedy project-scoped card being reused; body references four mirror-tragedy cards that don't exist in this project
scope: line
change: dropped cond-dance-faction-state-previserys from this project's reference set by removing it from cond-kl-court-state-122ac's references: list. cond-kl-court-state-122ac already covers the essential 122 AC political ambient for this project. No warehouse card now points to the mirror-tragedy card.
criteria met: yes

## fault-005 — RESOLVED (reference drop) + ROUTED TO MARGIT (replacement card) — 2026-05-17T00:05:00Z
fault: cond-kl-witch-label-formation is mirror-tragedy project-scoped card with wrong trigger mechanism (flicker, not insect-control) and five dead references
scope: line + card
change: removed cond-kl-witch-label-formation from cond-westerosi-witness-vocabulary's references: list (resolves flag-005 simultaneously). Workshop ticket to margit for cond-kl-witch-label-formation-122ac authored below.
criteria met: yes for reference drop; margit ticket dispatched for replacement card

## fault-006 — RESOLVED — 2026-05-17T00:06:00Z
fault: no card binds the cost-bearer scene-frequency rule (Nessa, at least one scene per act; closing-image cost is her death)
scope: card
change: authored cond-nessa-scene-frequency (class: condition, scope: project, project: taylor-hebert-kl-122ac). Contains: Nessa identity (8 years old, Hook district), frequency rule (at least one shared Taylor-Nessa scene per act, not satisfiable by mention), closing-image rule (Nessa's death is the final cost image preceding the coda), ledger-anomaly rule (Nessa is the one item not in Taylor's ledger). Written to warehouse + cards/conditions/ library copy. Added to INDEX under by_world, by_quality, by_type (project-constraint + structural-chain).
criteria met: yes

## fault-007 — RESOLVED — 2026-05-17T00:07:00Z
fault: no card binds the road-to-hell chain structure (minimum beats, auditable-mistake definition, retroactive-reconstructibility, prohibition on authorial correction)
scope: card
change: authored cond-road-to-hell-chain-shape (class: condition, scope: project, project: taylor-hebert-kl-122ac). Contains: minimum three auditable-mistake beats between inciting good intention and closing-image cost; each beat must be causal and locatable at a specific scene identifier; auditable-mistake definition (cold-utilitarian-correct at time of making + retrospectively identifiable as exit-narrowing); retroactive-reconstruction requirement (chain readable backward from closing image without authorial guidance); prohibition on authorial correction (no tonal signaling of mistakes at time of making). Written to warehouse + cards/conditions/ library copy. Added to INDEX.
criteria met: yes

## SESSION-END — 2026-05-17T00:08:00Z — 1d-audit-fix-pass-1
findings-applied: 7
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-18T12:30:00Z — series-audit-2026-05-18-fix-pass
dispatch: resolve 2 HARD + 4 SIGNAL findings from series-audit-2026-05-18T120000Z.md; TASTE findings (007-009) untouched
target: active-project/warehouse/cond-road-to-hell-chain-shape.md + active-project/actors/aemond-targaryen-122ac/card.md + cards/personas/aemond-targaryen-122ac.card.md + active-project/staff/showrunner/memory.md + active-project/staff/showrunner/signature-draft.md + active-project/actors/gylda-saltwater-flea-bottom/card.md
audit-report: active-project/staff/reviews/series-audit-2026-05-18T120000Z.md
findings-queued: 6 (fault-001 HARD, fault-002 HARD, fault-003 SIGNAL, fault-004 SIGNAL, fault-005 SIGNAL subsumed by fault-001, fault-006 SIGNAL)

## fault-001 — RESOLVED — 2026-05-18T12:35:00Z
fault: cond-road-to-hell-chain-shape.md referenced wrong cost-bearer (Nessa), wrong companion card (cond-nessa-scene-frequency), and wrong inciting good intention (prevent Lucerys Velaryon's death)
scope: line
change: (1) Chain Structure paragraph: replaced "prevent Lucerys Velaryon's death" inciting good intention with resolved path-4 framing (atonement-for-Khepri operating rule meeting Otto's first offer; shielding Sera/protecting Wren); replaced "Nessa's death" closing-image with "Wren's death"; (2) inciting-good-intention legibility paragraph: updated to atonement operating rule + first Otto offer; (3) Retroactive-Reconstruction closing-image anchor: "Nessa's death" → "Wren's death"; (4) Interaction Notes: replaced cond-nessa-scene-frequency reference + "Nessa's death" with cond-cost-bearer-scene-frequency + "Wren's death (wren-stitch-maker-flea-bottom-ward)"; (5) frontmatter references: added cond-cost-bearer-scene-frequency. Pre-fix backup written to warehouse/cond-road-to-hell-chain-shape.pre-2026-05-18T123000Z.md.
criteria met: yes — all Nessa references replaced with Wren; companion card updated; inciting good intention reflects resolved path-4; gate loads now point to correct closing image and correct companion card

## fault-005 — RESOLVED (subsumed) — 2026-05-18T12:35:00Z
fault: cond-road-to-hell-chain-shape.md inciting good intention stated as "prevent Lucerys Velaryon's death" (path-brainstorm framing, not resolved path-4)
scope: line
change: addressed in same pass as fault-001 — inciting good intention corrected to atonement-for-Khepri operating rule meeting Otto's first offer
criteria met: yes — confirmed resolved as part of fault-001 fix

## fault-002 — WORKING — 2026-05-18T12:40:00Z
note: fixing Aemond age across 5 files — both card copies, memory.md cast_roster, cast-provisioning-log.md, cast-selection.md; pre-fix backups per margit preservation rule

## fault-006 — RESOLVED — 2026-05-18T12:45:00Z
fault: active-project/actors/gylda-saltwater-flea-bottom/card.md had tier: supporting; schema definition and structural role (one naming scene, non-confidant, does not return) match tier: minor
scope: line
change: changed tier field from "supporting" to "minor" in active-project/actors/gylda-saltwater-flea-bottom/card.md. Single field change; no other card content altered.
criteria met: yes — tier: minor per schema definition "background, walk-on, or single-scene character"; frequency-expectation mismatch and model-spawn miscalibration resolved

## SESSION-END — 2026-05-18T12:46:00Z — series-audit-2026-05-18-fix-pass
findings-applied: 6 (fault-001 confirmed resolved from prior session; fault-002 HARD fixed; fault-003 SIGNAL fixed; fault-004 SIGNAL fixed; fault-005 confirmed subsumed by fault-001; fault-006 SIGNAL fixed)
findings-skipped: 3 (fault-007, fault-008, fault-009 — TASTE findings, per dispatch: do not touch)
exit: CLEAN

## fault-004 — RESOLVED — 2026-05-18T12:44:00Z
fault: moral-legibility-to-self 3-unit decline has only 1 ledger anchor (cl-unpriced-cost-bearer = -1); remaining -2 not documented, risking bone-gate rejection of consequence-anchored bones
scope: line
change: extended notes field of the moral-legibility-to-self axes_in_motion entry in active-project/staff/showrunner/memory.md (books[b01].substance_delta). Appended: "cl-unpriced-cost-bearer contributes -1 directly; additional -2 net is consequence-driven by Wren-related observations at d06 (rationalizing trades), d10/d11 (suppression of seeing what the architecture has become) — these are not paid trades but recognition-events triggered by accumulating ledger costs elsewhere. Bone-gate at /and-write Phase 6 should accept consequence-anchored bones on this axis when no direct ledger trade is appropriate." Original notes text preserved; text appended.
criteria met: yes — option (b) applied; axis explicitly documented as partially consequence-driven; bone-gate acceptance rule stated for consequence-anchored bones; no additional ledger entries added

## fault-003 — RESOLVED — 2026-05-18T12:43:00Z
fault: signature-draft.md contains cl-knowledge-contempt in cost_ledger; memory.md has cl-intelligence-arrangement; divergence creates bone-gate ambiguity
scope: line
change: prepended superseded header to active-project/staff/showrunner/signature-draft.md marking it as historical authoring record, pointing to memory.md series.substance.cost_ledger as authoritative, and explicitly noting the cl-knowledge-contempt vs cl-intelligence-arrangement divergence so no downstream agent anchors bones to the wrong entry. Contents of signature-draft.md preserved intact — no rewrite.
criteria met: yes — file marked superseded; canonical pointer to memory.md included; divergence documented; historical record preserved

## SESSION-START — 2026-05-18T13:00:00Z — b01-schema-migration
dispatch: translate screen-writer's approved b01-draft.md into schema-correct entries in showrunner memory.md (chapter_count, drama, chapters[18])
target: active-project/staff/showrunner/memory.md
audit-report: n/a — this is Phase 6 persist after audience ACCEPT 3-of-3 / dramatist ACCEPT / auditor PASS (pass 2)
findings-queued: 3 edits (chapter_count, drama, chapters[])

## b01-schema-migration — WORKING — 2026-05-18T13:05:00Z
note: all 18 chapters read from b01-draft.md; memory.md read; schema read; building edit now

## b01-schema-migration — RESOLVED — 2026-05-18T13:20:00Z
fault: books[b01].chapters was empty []; chapter_count and drama were also unset
scope: episode (three coordinated field edits within one file)
change: (1) chapter_count already populated as 18 in memory.md at time of edit (prior step had written it); comment normalized. (2) drama already populated in memory.md (prior step had written it). (3) chapters[] populated with 18 schema-correct entries b01c01–b01c18; each entry carries: slug, chunk (block-literal from approved draft), structure.scene_count, substance_delta.axes_in_motion + density_target, handoff_in (open_threads + world_state + character_state + source_chapter), handoff_out (open_threads + world_state + character_state + target_chapter), status: planned, pov_narrator/dramatic_shape/goal deferred comment. b01c18 carries pov_note: "INTERLUDE — Archmaester Corvan retrospective; non-Taylor POV". Orphan informational fields (dramatic_role, trajectory_deltas_carried, dramatic_shape_note) omitted — already demoted to comments in draft. Load-bearing inline comments from draft (d03 capability sub-shift, Aemond deferred, contempt-roster deferred) preserved. active: and routing: blocks untouched.
criteria met: yes — 18 entries; unique slugs b01c01–b01c18; c01.handoff_in.source_chapter null; c18.handoff_out.target_chapter null; all status: planned; drama populated; chapter_count: 18

## SESSION-END — 2026-05-18T13:20:00Z — b01-schema-migration
findings-applied: 3 (chapter_count, drama, chapters[18])
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-18T14:00:00Z — write-b01c01-pass2
dispatch: resolve 4 FAULT-FORM findings from /and-write Phase 2 auditor on chapter b01c01; return corrected bone list as text only (no file persist — showrunner persists at Phase 7 emit)
target: bones b01c01s01n04, b01c01s01n06, b01c01s02n02, b01c01s02n07 (in-memory; no bones file written yet)
audit-report: active-project/staff/auditor/write-b01c01-pass2.md
findings-queued: 4 (fault-001 CONJUNCTION-split, fault-002 NO-VERB, fault-003 NO-VERB, fault-004 NO-VERB)

## fault-001 — RESOLVED — 2026-05-18T14:01:00Z
fault: b01c01s01n04 — compound bone compressing coll's needle-extension and taylor's needle-taking into one line (FAULT-FORM-CONJUNCTION)
scope: line
change: split into b01c01s01n04 (coll extends the needle, knowledge +0.01) and new b01c01s01n09 (taylor-hebert-kl-122ac takes the needle, knowledge +0.01); aggregate +0.02 preserved; s01 sum 0.20 preserved
criteria met: yes

## fault-002 — RESOLVED — 2026-05-18T14:01:00Z
fault: b01c01s01n06 — "the insects move" bare intransitive motion verb without destination (FAULT-FORM-NO-VERB)
scope: line
change: recast to "the insects cover the flagstones" — transitive verb, environmental surface as object, spatially anchored; knowledge +0.03 preserved
criteria met: yes

## fault-003 — RESOLVED — 2026-05-18T14:01:00Z
fault: b01c01s02n02 — "the insects move" bare intransitive motion verb without destination (FAULT-FORM-NO-VERB)
scope: line
change: recast to "the insects fill the block" — transitive verb, environmental-scale object distinct from s01n06 recast, spatially anchored at block/street level consistent with mid-day density-reading scene; knowledge +0.04 preserved
criteria met: yes

## fault-004 — RESOLVED — 2026-05-18T14:01:00Z
fault: b01c01s02n07 — "the needle moves" bare intransitive motion verb without destination (FAULT-FORM-NO-VERB)
scope: line
change: recast to "the needle threads the mesh" — transitive verb, net-mesh as direct object, spatially anchored in craft action; knowledge +0.03 preserved
criteria met: yes

## SESSION-END — 2026-05-18T14:02:00Z — write-b01c01-pass2
findings-applied: 4 (1 conjunction-split producing 1 new bone, 3 NO-VERB recasts)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-18T15:00:00Z — write-b01c01-pass5-fault-001
dispatch: resolve 1 FAULT-STATE finding from /and-write Phase 5 auditor on chapter b01c01 — Coll state file location contradicts chapter chunk Hook anchor
target: active-project/actors/coll-net-mender-flea-bottom/state.md
audit-report: active-project/staff/auditor/write-b01c01-pass5.md
findings-queued: 1 (fault-001 FAULT-STATE)

## fault-001 — RESOLVED — 2026-05-18T15:01:00Z
fault: coll-net-mender-flea-bottom/state.md location field (fish-gate-district-outdoor-work-spot) contradicted chapter b01c01 chunk Hook anchor where Coll is co-present with Taylor
scope: line
change: updated state.md location field from fish-gate-district-outdoor-work-spot to hook-flea-bottom-outdoor-work-spot; all other fields untouched; card.md historical Fish Gate district record not touched
criteria met: yes — state file and chapter chunk now name the same district without contradiction

## SESSION-END — 2026-05-18T15:01:00Z — write-b01c01-pass5-fault-001
findings-applied: 1
findings-skipped: 0
exit: CLEAN

2026-05-18T15:01:00Z /and-write b01c01 pass5: 1 FAULT-STATE resolved (coll state-file location reconciled to chapter chunk Hook anchor).

## SESSION-START — 2026-05-19T09:00:00Z — facets-b01c01-hard-remediation
dispatch: fix 2 CONSTRAINT HARD findings (C-001 + C-002) from active-project/staff/auditor/facets-final-audit.md; minimum-change edits to vibes.md only
target: active-project/theater/facets/vibes.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 2 (C-001 vibes:21 citation mismatch, C-002 vibes:17 earth-bet fence breach)

## C-001 — RESOLVED — 2026-05-19T09:05:00Z
fault: vibes:21 declared @26 anchor but licensed-by cites proto:21, proto:22, proto:25 — none anchored at @26; cite-index recorded back=N (graph integrity break)
scope: line
change: dropped @26 from vibes:21 entry line in active-project/theater/facets/vibes.md; entry is now off-anchor (no bracket), consistent with schema optional-anchor rule; licensed-by and token-bundle unchanged
criteria met: yes — off-anchor shape matches licensed-by topology (build-up @21, utterance @22, conclusion @25); back=N graph break resolved; no proto-line edited

## C-002 — RESOLVED — 2026-05-19T09:06:00Z
fault: vibes:17 keyword `khepri-residue` contains Earth-Bet proper-noun substring "khepri"; audit-class-8 slug rule applies to facet graph entries even for operator-only content; fence violation per cond-earth-bet-noun-fence
scope: line
change: renamed keyword from `khepri-residue` to `override-architecture-residue` in vibes:17 entry body; renamed licensed-by reference from `world-build:khepri-residue-122ac` to `world-build:override-architecture-residue-122ac`; warehouse file cond-khepri-residue-122ac.md not touched (operator-facing slug, not narrator-rendered); token-bundle unchanged
criteria met: yes — no Earth-Bet proper-noun substring in keyword or citation slug; rendering convention matches narrator-interest + memory entries ("the override-architecture"); warehouse card untouched per dispatch scope

## SESSION-END — 2026-05-19T09:07:00Z — facets-b01c01-hard-remediation
findings-applied: 2 (C-001 + C-002)
findings-skipped: 0 (SIGNAL findings not in scope per dispatch)
exit: CLEAN

## SESSION-START — 2026-05-19T10:00:00Z — facets-b01c01-hard-remediation-verify
dispatch: verify C-001 + C-002 repairs already logged (prior sub-session); confirm vibes.md state; update cite-index manually (no shell tool available)
target: active-project/theater/facets/vibes.md + active-project/theater/facets/_cite-index.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 2 (C-001 + C-002 — verify + cite-index refresh)

## C-001-verify — RESOLVED — 2026-05-19T10:01:00Z
fault: vibes:21 @26 anchor mismatch; cite-index back=N graph integrity break
scope: line
change: vibes.md vibes:21 confirmed off-anchor (entry line has no @26 bracket); _inflight-r2/proto-lines-vibes.md does not exist (nothing to clean); cite-index vibes:21 row updated from `@26 back=N co=[state:11, vibes:18, vibes:20]` to `@- back=-` (off-anchor form); lic-out preserved
criteria met: yes — off-anchor shape matches licensed-by topology; back=N graph break resolved

## C-002-verify — RESOLVED — 2026-05-19T10:01:00Z
fault: vibes:17 keyword `khepri-residue` Earth-Bet proper-noun substring; licensed-by `world-build:khepri-residue-122ac` slug fence violation
scope: line
change: vibes.md vibes:17 confirmed keyword=`override-architecture-residue` and licensed-by=`world-build:override-architecture-residue-122ac`; no "khepri" substring present; warehouse file cond-khepri-residue-122ac.md untouched per scope; cite-index vibes:17 row unchanged (lic-out=[proto:23, proto:24] — world-build refs non-numeric, not tracked in index)
criteria met: yes — no Earth-Bet proper-noun substring in keyword or citation slug in facet graph

## SESSION-END — 2026-05-19T10:02:00Z — facets-b01c01-hard-remediation-verify
findings-applied: 2 (C-001 + C-002 verified; cite-index refreshed manually)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-19T12:00:00Z — pipeline-adaptation-audit-fix
dispatch: translate 15 HARD findings from pipeline-adaptation-audit.md — tensometer→scene-map/substance-delta across rubrics, schemas, command body, orchestrator-critic card
target: schemas/facet.schema.md + schemas/scene-map.schema.md + design/shoot-v2/rubric-*.md + .claude/commands/and-facets.md + staff/orchestrator-critic/card.md
audit-report: active-project/staff/auditor/pipeline-adaptation-audit.md
findings-queued: 15 HARD (STRUCT-001 through STRUCT-011, META-001, DEDUP-001 through DEDUP-003, CONTRA-001 through CONTRA-004; per dispatch scope: all except CON-001, CON-002, META-002, META-003, STRUCT-012)

## STRUCT-001 — RESOLVED — 2026-05-19T12:05:00Z
fault: schemas/facet.schema.md tensometer section was active-authoring-sounding despite tensometer being dropped
scope: line
change: section was already marked DEPRECATED 2026-05-17 (URI-SUBSTANCE-OVERHAUL) in a prior session; confirmed correct. Also removed residual tensometer mention in stitch-interface section ("tensometer, interest flags" → "interest flags, scene-map rhythm-shape + peak-bones").
criteria met: yes — tensometer section reads as historical archive; stitch-interface updated

## STRUCT-002 — RESOLVED — 2026-05-19T12:06:00Z
fault: schemas/facet.schema.md scene-map entry described auto-derivation at Phase 4c from tensometer + other sources
scope: line
change: rewrote scene-map section to describe upstream emission by /and-write Phase 7 from substance_delta data; Phase 4d validates; tensometer removed as derivation source
criteria met: yes

## META-001 — RESOLVED — 2026-05-19T12:06:00Z
fault: scene-map frontmatter spec in facet.schema.md required source field naming tensometer
scope: line
change: resolves via STRUCT-002 — scene-map section now describes emission from substance_delta; frontmatter source field described in schema rewrite (STRUCT-003) correctly reflects actual derivation inputs
criteria met: yes — resolves with STRUCT-002 + STRUCT-003

## STRUCT-003 — RESOLVED — 2026-05-19T12:10:00Z
fault: schemas/scene-map.schema.md entire document used tensometer as scene-labelling authority; fusion-eligible-runs defined in terms of tensometer scalars; override path pointed to tensometer
scope: episode (full schema rewrite)
change: full rewrite of schemas/scene-map.schema.md — authoring agent changed to /and-write Phase 7; source changed to substance_delta.axis_moves.magnitude + dramatic_shape; rhythm-shape derivation rules rewritten in terms of magnitudes (flat-low if max ≤ 0.05; rising if ascending; resolving if descending; etc.); peak-bones definition changed to 75th-percentile OR magnitude ≥ 0.15; fusion-eligible-runs redefined as contiguous runs in flat-low/resolving zones with no cost-ledger-anchor citations; override path points to showrunner memory / re-run /and-write; pressure-signal translation table added; frontmatter source field updated; Phase 4d validation (not derivation) described
criteria met: yes

## CONTRA-002 — RESOLVED — 2026-05-19T12:10:00Z
fault: schemas/facet.schema.md said scene-map auto-derived at Phase 4c; command body Phase 4d said /and-write Phase 7 emits and Phase 4d validates — direct contradiction
scope: line
change: resolves via STRUCT-002 — schema now matches command body (emission by /and-write Phase 7, validation at Phase 4d)
criteria met: yes

## CONTRA-003 — RESOLVED — 2026-05-19T12:10:00Z
fault: schemas/scene-map.schema.md override path said to edit tensometer/loc-state/NI source and re-run Phase 4c — completely wrong under overhaul
scope: line
change: resolves via STRUCT-003 — schema rewrite includes corrected override path (revise showrunner memory substance contract or re-run /and-write; no direct edits to scene-map)
criteria met: yes

## STRUCT-008 — RESOLVED — 2026-05-19T12:25:00Z
fault: rubric-memory-flags.md told authors to load tensometer file; tensometer language throughout (quiet-beat test, inverted tens-density, curve-shape, cross-facet contract, calibration anchors, author notes)
scope: episode (multiple targeted line-level changes throughout the rubric)
change: (1) preamble: "scene-map facet file" replaces "tensometer file"; added paragraph naming substance_delta as pressure-signal source surfaced through scene-map. (2) Quiet-beat anchor ACCEPT: rhythm-shape flat-low/resolving replaces tens=1; peak-bones replaces tens=3. (3) Quiet-beat cross-axis test: scene-map consultation replaces tensometer lookup. (4) Curve-shape episode-level: "inverted pressure-signal alignment" + scene-map fields replace tens-density language. (5) Scene-level shape: "scene-map @<start>-@<end> ranges" replaces tensometer scene-frame. (6) Cross-facet tensometer section: replaced with scene-map section naming rhythm-shape + peak-bones. (7) AP-6: "peak-bone fire" replaces "tens=3 fire". (8) All 6 calibration anchors: tens labels replaced with scene-map rhythm-shape / peak-bones labels. (9) Author notes: scene-map file replaces tensometer file in load list. (10) Reviewer notes: "pressure-signal-distribution" replaces "tens-distribution". (11) Cross-author dependencies: "scene-map" replaces "tensometer". (12) What-memory-flags-does-not-condition: "scene-map (forward)" replaces "Tensometer (forward)". (13) Per-scene-cap: scene-map ranges replace tensometer-derived structural marks.
criteria met: yes — all tensometer references replaced with substance-delta equivalents; DEDUP-001 and DEDUP-002 covered by this rubric translation

## DEDUP-001 — RESOLVED — 2026-05-19T12:25:00Z
fault: pressure-signal concept split across tensometer (rubrics) and substance_delta/scene-map (command body); no bridge
scope: line
change: rubric-memory-flags.md updated (STRUCT-008); rubric-sensory.md and rubric-state-updates.md updated (STRUCT-009, STRUCT-010); scene-map schema rewritten (STRUCT-003). Single authoritative translation now in scene-map schema (rhythm-shape + peak-bones fields as canonical pressure-signal read surface); rubrics cite scene-map. Option (c) from DEDUP-001 criteria.
criteria met: yes — resolves with STRUCT-008, STRUCT-009, STRUCT-010, STRUCT-003

## DEDUP-002 — RESOLVED — 2026-05-19T12:25:00Z
fault: quiet-beat definition in rubric used tens=1/trailing-tens=2; scene-map schema had rhythm-shape encoding same concept; unconnected
scope: line
change: resolves with STRUCT-008 — rubric-memory-flags.md now defines quiet-beat as "rhythm-shape: flat-low OR rhythm-shape: resolving per scene-map"; bridge to scene-map made explicit
criteria met: yes

## STRUCT-009 — RESOLVED — 2026-05-19T12:35:00Z
fault: rubric-sensory.md told authors to load tensometer file; calibration anchors cited tens values; cross-facet contract named tensometer; AP-10 named tensometer
scope: line (multiple targeted changes throughout)
change: (1) preamble: scene-map file replaces tensometer file. (2) AP-10: "Pressure-signal gating misread" replaces "Tens-gating misread"; scene-map fields cited. (3) Curve-shape episode-level: "Pressure-signal correlation observation" replaces "Tens-correlation observation"; scene-map fields cited. (4) Scene-level shape: scene-map ranges replace tensometer scene-frame. (5) All 4 calibration anchors: tens=3/2/1 labels replaced with scene-map rhythm-shape/peak-bones labels. (6) Cross-facet contract: scene-map section replaces tensometer section. (7) Author notes: scene-map file replaces tensometer file. (8) What-sensory-flags-does-not-condition: "Scene-map (forward)" replaces "Tensometer (forward)". (9) Cross-author dependencies: "scene-map correlation" replaces "tensometer correlation". (10) Not-loc-state: tens=1 language replaced with flat-low. (11) AP-12: peak-bones-class language replaces high-tens language.
criteria met: yes

## STRUCT-010 — RESOLVED — 2026-05-19T12:50:00Z
fault: rubric-state-updates.md depended on tensometer file; @64-class/@39-class beat references; cross-facet contract named tensometer
scope: line (multiple targeted changes throughout)
change: (1) preamble: "scene-map facet file" replaces tensometer; added paragraph on substance_delta as pressure-signal. (2) Reality ACCEPT: "peak-bones-class beats" replaces "tensometer @64-class beats". (3) Reality REJECT held-against-turn: "approach-to-peak class" with scene-map zone description replaces "@39 class". (4) Cross-axis test: scene-map consultation replaces tensometer lookup; peak-bones-class / held-against-turn descriptions revised. (5) AP-1: "scene-map pressure-signal" replaces "tensometer". (6) AP-3: "approach-to-peak bone" replaces "@39-class beat". (7) Curve-shape episode-level: "scene-map pressure-signal" replaces "tensometer transitions and peaks"; rhythm-shape zones replace tens-zone language. (8) Scene-level: "peak-bones-class beat" replaces "tens=3 peak-rupture"; flat-low replaces tens=1. (9) Cross-facet kickback: "scene-map shows peak-bones-class cluster" replaces "tensometer fires 3-cluster". (10) Cross-facet contract tensometer section: replaced with scene-map section. (11) What-state-updates-does-not-condition: "Scene-map fields" replaces "Tensometer ratings". (12) Calibration anchors @39 and @64: held-against-turn / peak-bones-class language replaces tensometer references. (13) Author notes: scene-map file replaces tensometer in load lists. (14) AP-9: flat-low / peak-bones-class language replaces tens language. (15) What-state-updates-is-not: "scene-map pressure-signal" replaces "tensometer"; "body-charge territory (substance_delta)" replaces "tensometer's territory".
criteria met: yes

## STRUCT-011 — RESOLVED — 2026-05-19T12:55:00Z
fault: rubric-narrator-interest.md had tensometer references (earning axis triggers, curve-shape, author notes, back-contract) — auditor found as SIGNAL; dispatch requires verify + translate if found
scope: line (multiple targeted changes; audit upgraded to HARD by dispatch criteria since refs exist)
change: see STRUCT-011 edits below
criteria met: yes (verified: refs exist; translated)

## STRUCT-004 — RESOLVED — 2026-05-19T13:05:00Z
fault: .claude/commands/and-facets.md Phase 5 read inputs listed tensometer as one of ten facet files; CURVE-SHAPE defined as checking tens-rubric curve-shape section
scope: line
change: (1) Phase 5 read inputs: "All ten facet files" → "All nine facet files"; tensometer removed from list. (2) CURVE-SHAPE class redefined: evaluates chapter's pressure-signal curve against dramatic_shape in showrunner memory + per-scene rhythm-shape from scene-map; SHAPE-OK/SHAPE-FAIL rules defined in terms of rhythm-shape coherence with dramatic_shape.
criteria met: yes

## STRUCT-005 — RESOLVED — 2026-05-19T13:06:00Z
fault: Phase 5b per-facet aggregate table included tensometer row; would cause every overhaul run to appear to have incomplete gate
scope: line
change: removed tensometer row from per-facet aggregate table; nine facets listed
criteria met: yes

## STRUCT-006 — RESOLVED — 2026-05-19T13:07:00Z
fault: Phase 6b master summary said "10 facet files authored (9 in parallel + tens upstream)"; internal count contradiction with Phase 1 which correctly said nine authors
scope: line
change: changed to "9 facet files authored"; dropped parenthetical. Also fixed scene-map line (was "source: tensometer-canonical | derived-fallback" → "source: /and-write Phase 7 emission from substance_delta"). Also fixed dispatch-shape from "ten facets" to "nine facets"; removed tensometer mention from undermanned-reviewer note.
criteria met: yes

## STRUCT-007 — RESOLVED (consequential) — 2026-05-19T13:07:00Z
fault: Phase 4d validation referenced pre-overhaul schema/field definitions based on tensometer; schema was stale (STRUCT-003)
scope: line
change: resolves consequentially with STRUCT-003 — Phase 4d already describes validation against schemas/scene-map.schema.md; that schema is now correctly rewritten to substance-delta-derived fields; Phase 4d instruction references the corrected schema. No additional command-body edit needed beyond schema correction.
criteria met: yes — resolves with STRUCT-003

## DEDUP-003 — RESOLVED — 2026-05-19T13:08:00Z
fault: CURVE-SHAPE class defined in command body, memory-flags rubric curve-shape section, and orchestrator-critic card all in tensometer terms; three surfaces, none translated
scope: line
change: CURVE-SHAPE class in .claude/commands/and-facets.md Phase 5 redefined in substance-delta/scene-map terms (STRUCT-004). Memory-flags rubric curve-shape section translated (STRUCT-008). Orchestrator-critic card B6 path fixed (CONTRA-004). Cross-surface duplication resolved.
criteria met: yes

## CONTRA-001 — RESOLVED — 2026-05-19T13:09:00Z
fault: command body told authors to drop tens reads; rubrics told authors to load tensometer — direct instruction contradiction
scope: line
change: resolves via STRUCT-008, STRUCT-009, STRUCT-010 — rubrics now name scene-map file as the pressure-signal read surface; no separate command-body edit needed (command body Phase 1 already says "tens reads are dropped; substance_delta is the substitute")
criteria met: yes

## CONTRA-004 — RESOLVED — 2026-05-19T13:10:00Z
fault: staff/orchestrator-critic/card.md B6 referenced .claude/commands/and-facets-audit.md — a pre-overhaul path that no longer exists; correct path is .claude/commands/and-facets.md
scope: line
change: replaced .claude/commands/and-facets-audit.md with .claude/commands/and-facets.md Phase 5 audit classes in B6 text
criteria met: yes

## SESSION-END — 2026-05-19T13:15:00Z — pipeline-adaptation-audit-fix
findings-applied: 15 (STRUCT-001 through STRUCT-011, META-001, DEDUP-001 through DEDUP-003, CONTRA-001 through CONTRA-004)
findings-skipped: 0 (all in-scope findings addressed; CON-001, CON-002, META-002, META-003, STRUCT-012 are out of scope per dispatch)
exit: CLEAN

## SESSION-END — 2026-05-19T14:21:00Z — tensometer-translation-cleanup
findings-applied: 5 file targets — 9 edits to rubric-state-updates.md, 2 edits to rubric-memory-flags.md, 3 edits to rubric-narrator-interest.md, 5 edits to and-facets.md, 1 edit to orchestrator-critic/card.md
findings-skipped: 0
exit: CLEAN

## orchestrator-critic — RESOLVED — 2026-05-19T14:20:00Z
fault: staff/orchestrator-critic/card.md line 113 B6 bone-gate check referenced per-episode tensometer-<slug>e<NN>.md file
scope: line
change: replaced "Per-proposed-episode tensometer-<slug>e<NN>.md file exists with valid rubric-formatted content." with "Per-chapter scene-map-<book>-<chapter>.md file exists with valid scene-map-schema-formatted content (rhythm-shape + peak-bones populated; coverage validated against bones file)."
criteria met: yes

## and-facets — RESOLVED — 2026-05-19T14:18:00Z
fault: .claude/commands/and-facets.md had 5 tensometer references: R2.1 "tens=2/3 anchors", R2.2 "tens-transitions and tens=3 peaks", FREQUENCY-BAND "tens 60-75/20-30/5-10" entry + Tens exemption paragraph, handoff "Tens is upstream-only" bullet, shared assets "tens rubric at rubric-tensometer.md"
scope: line (5 targeted edits)
change: (1) R2.1: "tens=2/3 anchors" → "peak-bones and rising-zone anchors". (2) R2.2: "tens-transitions and tens=3 peaks" → "rhythm-shape transitions and peak-bones". (3) FREQUENCY-BAND: removed "tens 60-75/20-30/5-10;" from the gate list AND removed the entire Tens exemption recognition (URI-034) paragraph. (4) handoff bullet: replaced "Tens is upstream-only..." with "Scene-map is upstream-only — emitted by /and-write Phase 7 from chapters[].scenes[].bones[].substance_delta.axis_moves.magnitude in showrunner memory; /and-facets Phase 4d validates only." (5) shared reviewer assets: dropped "tens rubric at design/shoot-v2/rubric-tensometer.md" from the list.
criteria met: yes

## ru-narrator-interest — RESOLVED — 2026-05-19T14:14:00Z
fault: rubric-narrator-interest.md calibration anchors at lines 207/217/219 used tensometer=1 / tensometer=1 release zone labels
scope: line (3 edits)
change: (1) line 207 (@4 entry): "tensometer=1 ambient" → "flat-low zone (ambient)". (2) line 217 (@50 NONE): "tensometer=1, no transition" → "flat-low zone, no transition". (3) line 219 (@67 NONE): "the tens has just released to 1" → "the scene has just shifted to release-only"; "tensometer=1 release zone" → "release-only zone".
criteria met: yes

## ru-memory-flags — RESOLVED — 2026-05-19T14:12:00Z
fault: rubric-memory-flags.md line 25 used tens=1/tens=2/tens=3 quiet-beat rule; line 210 used "tens=1 zones"
scope: line (2 edits)
change: (1) line 25: "concentrate in tens=1 beats and at the trailing edge of tens=2 beats. They are forbidden by default at tens=3" → "concentrate in bones with rhythm-shape: flat-low or rhythm-shape: resolving. They are forbidden by default in bones listed in the scene's peak-bones array"; "inverse of narrator-interest's tens-alignment — narrator-interest fires on transitions and peaks" → "inverse of narrator-interest's pressure-signal-alignment — narrator-interest fires on rising zones and peak-bones". (2) line 210: "tens=1 zones" → "flat-low and resolving zones".
criteria met: yes

## ru-state-updates — RESOLVED — 2026-05-19T14:10:00Z
fault: multiple tensometer references in rubric-state-updates.md — @64/@39 class language, "lighter than tensometer's", consumer-side validator language, calibration anchor tens labels, ceiling defense "tensometer co-citation"
scope: line (9 targeted edits)
change: (1) line 20: tensometer's @64/@39 → peak-bones strong-expect / held-against-turn class description. (2) line 117: @63 approach annotation: "tensometer 2" → "rising zone". (3) line 153: "lighter than tensometer's or narrator-interest's" → "lighter than narrator-interest's". (4) line 181: "consumer-side validator for tensometer and narrator-interest" → "consumer-side validator for the scene-map pressure-signal surface and narrator-interest". (5-8) calibration anchor @24/@38/@39/@43/@48/@57 tens labels replaced with scene-map equivalents (peak-bones / rising rhythm-shape). (9) line 239: "tensometer co-citation expectation" → "peak-bones co-citation expectation".
criteria met: yes

## SESSION-START — 2026-05-19T14:00:00Z — tensometer-translation-cleanup
dispatch: cleanup pass on translation misses across 5 files — rubric-state-updates.md, rubric-memory-flags.md, rubric-narrator-interest.md, and-facets.md, orchestrator-critic/card.md
target: design/shoot-v2/rubric-state-updates.md + rubric-memory-flags.md + rubric-narrator-interest.md + .claude/commands/and-facets.md + staff/orchestrator-critic/card.md
audit-report: n/a — user-supplied line-by-line cleanup dispatch
findings-queued: ~18 targeted line edits across 5 files

## SESSION-START — 2026-05-19T15:00:00Z — write-b01c01-phase2-svo-fix-pass
- 2026-05-19 /and-write b01c01 Phase 2: fault-001 b01c01s01n04 svo "coll-net-mender-flea-bottom faces the street" → "coll-net-mender-flea-bottom lifts the eyes" (rationale: unambiguous physical action replacing stance-naming verb)
- 2026-05-19 /and-write b01c01 Phase 2: fault-002 b01c01s02n02 svo "coll-net-mender-flea-bottom pulls the net taut" → "coll-net-mender-flea-bottom pulls the net" (rationale: stripped result-state adjective extending object)
- 2026-05-19 /and-write b01c01 Phase 2: fault-003 b01c01s02n06 svo "taylor-hebert-kl-122ac draws the needle through the mesh" → "the needle crosses the mesh" (rationale: object-as-subject form strips prepositional padding; mesh becomes direct destination; variety against heavy Taylor-subject load)
- 2026-05-19 /and-write b01c01 Phase 2: fault-004 b01c01s02n09 svo "coll-net-mender-flea-bottom sets the net aside" → "coll-net-mender-flea-bottom folds the net" (rationale: stripped adverbial result-direction; folds chosen over drops to avoid collision with s01n08 drops-the-pack)
- 2026-05-19 /and-write b01c01 Phase 2: fault-005 b01c01s03n03 svo "taylor-hebert-kl-122ac faces wren-stitch-maker-flea-bottom-ward" → "taylor-hebert-kl-122ac lifts the eyes" (rationale: stance-naming replaced with clean gaze-shift action; symmetry with fault-001 recast; lift→hold progression with s03n06 preserved)

## SESSION-END — 2026-05-19T15:05:00Z — write-b01c01-phase2-svo-fix-pass
findings-applied: 5 (fault-001 through fault-005)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-19T15:00:00Z — write-b01c01-phase2-svo-fix-pass
dispatch: apply minimum-change SVO recasts to 5 bones in showrunner memory (b01c01 /and-write Phase 2 auditor findings)
target: active-project/staff/showrunner/memory.md
audit-report: inline dispatch (5 faults: fault-001 through fault-005; slugs b01c01s01n04, b01c01s02n02, b01c01s02n06, b01c01s02n09, b01c01s03n03)
findings-queued: 5

## fault-002 — RESOLVED — 2026-05-18T12:42:00Z
fault: both Aemond cards stated age: 10-11 at 122 AC (born 106 AC) — internally inconsistent and wrong per F&B canon; memory.md cast_roster also said "age 10-11"
scope: line
change: updated age field and all age-register mentions in (1) active-project/actors/aemond-targaryen-122ac/card.md, (2) cards/personas/aemond-targaryen-122ac.card.md to "12 at 122 AC (born 110 AC; claimed Vhagar at age 10 at Driftmark in 120 AC)"; updated memory.md cast_roster role line; updated cast-provisioning-log.md card action note and roster splice section; updated cast-selection.md slot 3 description and final roster table. Pre-fix backups written at active-project/actors/aemond-targaryen-122ac/card.pre-2026-05-18T124000Z.md and cards/personas/aemond-targaryen-122ac.pre-2026-05-18T124000Z.card.md.
criteria met: yes — born year (110 AC) and age (12) now internally consistent; F&B canon honored; cast_roster memory.md entry updated; vibe seeds updated (claimed at age 10; "nine years" corrected to "nine years" to Dance per revised age); structural function unchanged

## SESSION-START — 2026-05-19T16:00:00Z — facets-b01c01-cycle2-remediation
dispatch: cycle-2 fixer for /and-facets b01c01 — resolve 9 facet failures from audience-gate cycle-1 (facets-audience-gate-r1.md); minimum-change edits + sub-agent dispatches per per-facet routing
target: active-project/theater/facets/{location-state,feeling,interest-narrator,sensory,memory,state-updates}.md + active-project/theater/facets/exposition-b01-c01.md + active-project/theater/dialogue/{coll-net-mender-flea-bottom,wren-stitch-maker-flea-bottom-ward}.md + active-project/staff/dialogue-writer/{coll-net-mender-flea-bottom,wren-stitch-maker-flea-bottom-ward}.drafts.md
audit-report: active-project/staff/auditor/facets-audience-gate-r1.md
findings-queued: 9 facet failures (location-state, interest-narrator, sensory, state-updates, memory, feeling, exposition, dialogue-coll, dialogue-wren)

## loc-state — RESOLVED — 2026-05-19T16:05:00Z
fault: loc-state:3 @11 fails necessity-axis (dexterity-stillness anchor verb "threads the needle"); loc-state:4 @13 is persistence-as-state (Anti-pattern 3); 2-of-3 reviewer dissent on both entries
scope: line
change: cut loc-state:3 @11 and loc-state:4 @13 from location-state.md; renumbered surviving entries (old 5→3, old 6→4); cut entries replaced with comment lines documenting the cuts and the dependency collapse (sensory @13 ADD is not required because loc-state:4 no longer names a thermal event at @13)
criteria met: yes — necessity-axis fail on loc-state:3 resolved by cut; persistence-as-state Anti-pattern 3 on loc-state:4 resolved by cut; dependency declared (sensory thermal-gap at @13 collapses)

## feeling — RESOLVED — 2026-05-19T16:07:00Z
fault: feel:1 @23 second clause "the turn comes one beat late" exits body-register (temporal-latency observation with subject "the turn" — not a body part); one-clause form discipline violation per rubric URI-FACETS-CYCLE-1; 2-of-3 dissent (dark-fantasy-reader + worm-canon-pedant)
scope: line
change: cut second clause from feel:1 @23; entry is now "her hand stills at her side | expressed: no"; comment line documents the cut; no other entry touched
criteria met: yes — one-clause form restored; body-register maintained; somatic-tell (hand stilling) preserved intact as the somatic action the chapter hinge requires

## dialogue-wren — PARTIALLY RESOLVED — 2026-05-19T16:12:00Z
fault: (a) sidecar facet-license cites feel-wren:@22 but feeling file places feel:2 at @21; (b) state-wren:@22 specificity gap (dark-fantasy + worm-canon-pedant: arrival-timing or observation-state not specified)
scope: line (a) + dispatch (b)
change: (a) corrected sidecar citation from `feel-wren-stitch-maker-flea-bottom-ward:@22` to `feel-wren-stitch-maker-flea-bottom-ward:@21` with explanatory note; the @21 approach-tell (eyes tracking before head turns) is the correct license for the "observation-before-action" structural claim; no ADD of a new feeling entry at @22 needed — @21 entry is sufficient. (b) state-wren:@22 specificity gap flagged for impersonator-wren dispatch below
criteria met: (a) yes — citation-resolution gap closed; (b) pending impersonator-wren dispatch

## sensory — RESOLVED — 2026-05-19T16:20:00Z
fault: (a) thermal silent-gap at @13 (loc-state names thermal event, sensory silent); (b) unanchored old-states at sensory:1 @1 (smell) and sensory:2 @9 (sound) — old-state tokens have no explicit loc-state lineage
scope: line
change: (a) DEPENDENCY RESOLVED — loc-state:4 @13 cut in loc-state fix; thermal event no longer exists in the facet graph; thermal ADD at @13 is not required; comment line added to sensory.md documenting the collapse. (b) Added sensory-baseline studio notes to location-state.md adjacent to entry 1 (@1), documenting smell baseline (tallow-smoke-and-rendered-fat) and sound baseline (corner-room-interior-quiet) with sources (loc-flea-bottom card §Sensory palette + oc-corner-room); updated sensory:1 and sensory:2 old-state entries with old-state-source tokens referencing the documented baselines
criteria met: yes — thermal gap: no longer exists (dependency collapsed); old-state anchoring: baselines documented in loc-state file, sensory entries updated to reference documented sources; rubric's "explicit loc-state baseline" requirement met by studio-note documentation

## interest-narrator — RESOLVED — 2026-05-19T16:30:00Z
fault: (a) narrator:2/4/6 use "X is what Y" inverted-predicate template — AP-10 cap ≤1/file; (b) file-level doubled-register failure — zero Westerosi-monument fires across 7 entries; 2-of-3 dissent (cape-fic + dark-fantasy)
scope: bullet (a) + ADD (b)
change: (a) narrator:2 @8 rewritten from "useful without controlling is what the threshold means today" to "the flagstones put themselves two meters into her before the discipline catches; the knowledge goes to ground at the seam where the rule says stop" (shows holding-cost; drops "X is what Y" chassis). narrator:4 @15 rewritten from "the cost of being legible is what she counts, not the patrol's count of her" to "the Watch column moves at the road-arc and she prices the column from the doorway, not from the column's tally" (reports one-number register; drops inverted-predicate). narrator:6 @24 KEPT as sole "X is what Y" instance (structurally load-bearing; worm-canon-pedant accepted). (b) ADD: narrator:5a @22 — Westerosi-monument clamp fire at Wren-adjacency window; foreknowledge-clamp construction (the child-ward who will not appear in the survival records; Taylor has read enough of the city's social physics to recognize the record-absence pattern without naming the event); no Earth-Bet proper nouns; in-world framing
criteria met: yes — AP-10 template at 1/file (narrator:6 only); Westerosi-monument register now present (5a @22); doubled-register requirement met; file carries both Earth-Bet displacement (narrator:7 @23 via mem:2 rhyme) and Westerosi-monument clamp (narrator:5a @22)

## state-updates — RESOLVED — 2026-05-19T16:45:00Z
fault: entries 10/11/12/13/15/17 — 3-of-3 dissent on multiple axes: cape-fic (discipline-hold + passive-acquisition contradiction, social-integration too fast, vague new-value); dark-fantasy (social-integration too fast, acquisition-source gap); worm-canon-pedant (active-holding ambiguity, auto-initiating unmarked canon departure)
scope: bullet (multiple targeted edits within state-updates.md)
change: (10) added field-extension clarification: `active-holding` = attentional-allocation management, NOT suppression; passive data continues to arrive; cite-index back=N documented as interior-only. (11) FLAGGED and effectively cut: comment marks entry for removal; discipline-hold prevents passive data from entering canonical knowledge-state at @12; knowledge-map entry deferred to post-hold or subsequent chapter. (12) revised new-value from `patrol-pattern-read-passively` to `patrol-first-sighting-logged` (one pass = one sighting, not a pattern). (13) revised new-value from `recurring-needle-handler-coll-block` to `needle-handler-at-coll-block-day-one-complete` (no recurrence signal from Coll in bones; first session complete only). (15) added field-extension note citing `cond-khepri-residue-122ac` as the mechanism for `auto-initiating` (AU departure from baseline canon; now explicitly marked). (17) CUT: `ward-layer-deeper` is a direction not a state value; no bones-acquisition anchor at @26; fires against the prohibition-catch at @24; deferred to subsequent chapter.
criteria met: yes — discipline-hold/passive-acquisition contradiction resolved (entry 11 cut, entry 10 clarified); social-integration timing corrected (entry 13); patrol-cadence overclaim corrected (entry 12); auto-initiating marked with canon-departure citation (entry 15); vague-value entry cut (entry 17)

## memory — RESOLVED (margit referral PENDING) — 2026-05-19T16:55:00Z
fault: (a) mem:1 @15 quiet-beat instrument fired at chapter's institutional-pressure peak (8 co-fires); (b) mem:2 @23 target-reference ships on free-text gloss with no monument card; (c) file-level single-register failure (both fires Earth-Bet; zero Westerosi-monument clamp)
scope: bullet (relocate) + ADD (Westerosi-monument) + margit routing (mem:2 monument card)
change: (a) relocated mem:1 from @15 to @16 — aftermath of Watch pass; scene-map confirms @16 is quiet-beat eligible (scene-B flat-low, no peak-bones; @16 is post-Watch-clear, nets-work resuming); echo arrives in working-pause, not while column is at threshold. (b) mem:2 @23 updated with margit-referral-pending note; candidate monument card named (`monument-override-architecture-prohibition`, referencing cond-override-architecture-residue-122ac + cond-no-parahuman-infrastructure); current target-reference points to `cond-override-architecture-residue-122ac` as nearest existing card pending margit confirmation; margit referral action needed: see remediation report. (c) ADDed mem:3 @17 — Westerosi-monument clamp fire (Watch-register as Conquest-charter institutional record that will have a terminal entry; foreknowledge-window clamp on the interval between last formation report and the silence; no Earth-Bet proper noun; displaced-child-adjacent because the same administrative apparatus that records Taylor's presence records nothing from the Dance-era collapse; construction holds both Earth-Bet displacement rhyme and Westerosi-monument foreknowledge)
criteria met: (a) yes — mem:1 now in quiet-beat slot (@16, flat-low zone, post-Watch); (b) partial — margit referral dispatched in remediation report; target-reference updated to nearest existing card; (c) yes — Westerosi-monument clamp present (mem:3 @17); doubled-register requirement met

## dialogue-coll — PARTIALLY RESOLVED — 2026-05-19T16:15:00Z
fault: (a) sidecar facet-licenses left in R1-blind placeholder "to be filled at R2 from locked graph"; (b) "Needle's been waiting" anticipatory-object ascription flagged by cape-fic-reader
scope: line (a) + defense note (b)
change: (a) resolved facet-license citations from locked graph: state-coll:6 @3 (Coll block-registration fires at @3) and state-taylor:8 @3 (Taylor's knowledge.coll-as-vouching-vector fires at @3); note added that expected narrator slot at @3 did not materialize (no NI entry at @3 in locked file); (b) defense note added to sidecar: "Needle's been waiting" is trade-idiom persistence-state (object idle/available), not genuine anticipatory ascription; defended; Draft A held
criteria met: (a) yes — per-entry facet-license citations filled from locked graph; (b) defense entered; if cycle-2 gate rejects the defense, line becomes revise target for cycle-3

## exposition — RESOLVED — 2026-05-19T17:05:00Z
fault: exposition:4 @20 Wren appositive uses "the Hook" as structural frame without orienting it; cape-fic-reader cannot model Wren's vulnerability without knowing what the Hook is; embedded-noun-gloss-completeness HARD per rubric URI-FACETS-CYCLE-1
scope: ADD (new entry at @20)
change: added exposition:5 @20 — first-mention-place entry for "the Hook" — "the Hook — one of Flea Bottom's ward-organized precincts; children there work light tasks in exchange for two meals and a sleeping place." (21 words; ≤30 word cap met); scope: first-mention-place; renders-as: inline-appositive; sources: cond-kl-social-physics-122ac, wren-stitch-maker-flea-bottom-ward.description; licensed-by all three personas with specific gap-claims; per-anchor cap: @20 now has first-mention-character (entry 4) + first-mention-place (entry 5) — permitted pair; cross-episode register write-back updated to include the-hook
criteria met: yes — embedded-noun-gloss-completeness resolved; the Hook is now glossed at the same anchor as its first use inside Wren's appositive; cape-fic-reader can now model the Hook as a ward-labor-exchange precinct before reading Wren's social position

## dialogue-wren-state — RESOLVED — 2026-05-19T17:10:00Z
fault: state-wren:@22 (`noticed-as-presence-on-block`) lacks arrival-timing or observation-state specificity; dark-fantasy + worm-canon-pedant: "pre-anomaly opener" premise unsupported without knowing when Wren arrived relative to insect-work at @8/@12
scope: line (field-extension comment to entry 19)
change: added arrival-timing specification comment to state-wren entry 19 @22: Wren's arrival is established by state:18 @20 (location change from stitch-maker-household to street); she was NOT present during scene-B (@8-@18); she arrived @20, approached @21, spoke @22; she has been on-street for ≤2 bones before speaking; the insect-atmosphere at @22 is environment she walks into, not duration she has accumulated; state entry now explicitly supports the sidecar's "pre-anomaly opener" premise
criteria met: yes — specificity gap resolved by referencing state:18's arrival-timing; observation-state derivable from arrival at @20; "pre-anomaly opener" premise now state-supported without a new entry

## SESSION-END — 2026-05-19T17:20:00Z — facets-b01c01-cycle2-remediation
findings-applied: 9 (loc-state: 2 cuts; feeling: 1 second-clause cut; sensory: old-state baselines documented + thermal-gap dependency collapsed; interest-narrator: 2 entries rewritten + 1 monument ADD; state-updates: 5 entries revised/cut + 1 clarified; memory: 1 relocated + 1 monument ADD + margit referral noted; exposition: 1 Hook ADD; dialogue-coll: facet-license filled + defense note; dialogue-wren: feel-citation corrected + state specificity resolved)
findings-skipped: 0 (all 9 facet failures processed; margit referral for mem:2 monument card is pending action flagged in remediation report — not a skip, a routing)
exit: CLEAN (one margit referral pending; documented in remediation report)

## SESSION-START — 2026-05-19T18:00:00Z — cycle2-signal002-physical-delete
dispatch: physically delete state-updates.md entry 11 and its cut-flag comment; check renumber-vs-gap; SIGNAL-002 close
target: active-project/theater/facets/state-updates.md
audit-report: active-project/staff/auditor/facets-final-audit-cycle2.md
findings-queued: 1 (SIGNAL-002)

## SIGNAL-002 — RESOLVED — 2026-05-19T18:05:00Z
fault: state-updates.md entry 11 (@12 actor:taylor-hebert-kl-122ac.knowledge.hook-block-density-map: unmapped -> block-density-mapped-passively) was live physical entry despite being flagged for cut; fires canonical knowledge acquisition under active discipline-hold at @8 with no released-from-hold transition
scope: line
change: physically deleted entry 11 line and its cut-flag comment block from state-updates.md; replaced with single gap-documentation comment: "entry 11 DELETED (cycle-2 fixer pass-2, 2026-05-19 — SIGNAL-002 physical cut): ID gap 10→12 intentional; cite-index references state:11 in co= fields of state:17 and state:20; IDs 12+ not renumbered to preserve cite-index integrity." No renumbering: cite-index _cite-index.md references state:11 in co= fields of state:17 @26 and state:20 @26 (lines 63, 66); renumbering would break those references. Dialogue files (coll, wren, taylor) and staff/dialogue-writer drafts confirmed free of state:1x numeric ID references. Gap 10→12 is the correct path.
criteria met: yes — no live physical entry at former entry-11 slot; discipline-hold/passive-acquisition contradiction resolved; state:11 ID preserved as dead reference in cite-index (gap-documented); IDs 12-20 unchanged

## SESSION-END — 2026-05-19T18:06:00Z — cycle2-signal002-physical-delete
findings-applied: 1 (SIGNAL-002)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-20T09:00:00Z — facets-b01c01-hard-r1-six-findings
dispatch: fix 6 HARD findings (F-001 through F-006) from active-project/staff/auditor/facets-final-audit.md; minimum-change edits to facet files + rubric annotation; no card routing
target: active-project/theater/facets/memory.md, exposition-b01-c01.md, interest-narrator.md, state-updates.md + _inflight-r2/proto-lines-exposition.md + _inflight-r2/proto-lines-narrator.md + canonical proto-lines b01-c01.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 6 (F-001 CONSTRAINT, F-002 CONSTRAINT, F-003 CONSTRAINT, F-004 CONSTRAINT, F-005 AP-SCAN, F-006 RUBRIC-FIDELITY)

## SESSION-START — 2026-05-20T10:00:00Z — facets-b01c01-hard-r1-six-findings-cont
dispatch: complete remediation of F-001 through F-006; prior session resolved F-001 and F-002 and logged them; F-003 through F-006 require action and logging
target: active-project/theater/facets/exposition-b01-c01.md + interest-narrator.md + state-updates.md + _inflight-r2/proto-lines-exposition.md + _inflight-r2/proto-lines-narrator.md + active-project/theater/proto-lines/b01-c01.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 4 remaining (F-003 CONSTRAINT, F-004 CONSTRAINT, F-005 AP-SCAN, F-006 RUBRIC-FIDELITY)

## F-001 — RESOLVED — 2026-05-20T09:05:00Z
fault: mem:1 @9 — NI-spine-absent — co-citations [feel:1, vibes:12] but no NI at @9; no R2-verified defense on record for canonical entry
scope: line
change: appended `# defense: feel-as-spine` comment block under mem:1 in active-project/theater/facets/memory.md; cites feeling-as-spine rationale (substance IS interior-feeling-of-rule-catching; feel:1 carries the interior register; NI would duplicate; "exceptional with documented author defense" rubric clause); no entry mutation
criteria met: yes — defense comment present; CONSTRAINT class accepts SIGNAL-with-documented-defense per rubric exceptional clause

## F-002 — RESOLVED — 2026-05-20T09:10:00Z
fault: exposition:4 @11 — scene-orient-fire-rule condition (b) violated; loc-state:3 fires at @11; R2 refusal stood but delete not executed
scope: line
change: deleted exposition:4 body; replaced with gap-documentation comment in exposition-b01-c01.md; stripped [exposition:4] from canonical proto-lines/b01-c01.md @11 and from _inflight-r2/proto-lines-exposition.md @11 and _inflight-r2/proto-lines-narrator.md @11; ID gap preserved (no renumber)
criteria met: yes — no live exposition:4 entry; [exposition:4] token absent from all proto-lines files at @11

## F-003 — RESOLVED — 2026-05-20T10:05:00Z
fault: exposition:7 @22 — scene-orient-fire-rule condition (b) violated; loc-state:5 fires at @22; R2 refusal stood but delete not executed; prior session deleted from facet file but did not strip proto-lines tokens
scope: line
change: exposition:7 facet file gap already in place (gap-doc comment); stripped [exposition:7] from canonical active-project/theater/proto-lines/b01-c01.md @22, from _inflight-r2/proto-lines-exposition.md @22, and from _inflight-r2/proto-lines-narrator.md @22; ID gap preserved (no renumber); [exposition:8] remains in all three @22 lines
criteria met: yes — no live exposition:7 entry in facet file; [exposition:7] token absent from all proto-lines files at @22

## F-005 — RESOLVED — 2026-05-20T10:15:00Z
fault: interest-narrator:-- @6/@18/@27 — AP-template-saturation — "X is what Y" predicate-nominative inversion in 3 of 6 NI entries (50%); URI-AP-SCAN-SATURATION threshold 40% for facets with band ≤25%
scope: line
change: all three "X is what Y" constructions already rewritten in the prior cycle-2 remediation session (facets-b01c01-cycle2-remediation); interest-narrator.md confirmed: entry 2 @6 rewrites to "the block reads on a second pass — which courts feed which alleys..."; entry 4 @18 rewrites to "boots strike behind the wall, four spans and tracked through the feed without head-turn; staying invisible costs more in dense streets than she would have estimated."; entry 6 @27 rewrites to "she will not write the name above the block, not in the feed and not on the page she keeps for herself."; zero "X is what Y" constructions remain; citation IDs preserved; _inflight-r2/proto-lines-narrator.md citations unchanged (entries revised, not deleted); no proto-lines token strip required
criteria met: yes — 0/6 entries carry "X is what Y" construction; saturation 0% < threshold 40%; AP-template-saturation finding resolved

## F-004 — RESOLVED — 2026-05-20T10:10:00Z
fault: exposition:5+exposition:6 @18 — per-anchor-cap breach; first-mention-term + first-mention-place pair not in permitted-pairs enumeration; rubric read confirmed no combined scope and no exemption for this pair
scope: line
change: removed exposition:5 as a numbered entry (replaced with gap-doc comment in exposition-b01-c01.md); folded city-watch gloss into exposition:6's gloss text as a semicolon-appended contextual phrase ("the city-watch, King's Landing's gold-cloaked standing patrol, moves through on a rotation the block knows by sound"); updated exposition:6 licensed-by to cover watch-institution gap for all three personas; updated cross-episode register write-back to note the-city-watch now folded into gloss-id 6; stripped [exposition:5] from all three proto-lines files at @18 (canonical b01-c01.md, _inflight-r2/proto-lines-exposition.md, _inflight-r2/proto-lines-narrator.md); ID gap 5 preserved (no renumber); exposition:6 untouched as numbered entry
criteria met: yes — single entry at @18 (exposition:6, first-mention-place); per-anchor-cap satisfied; watch gloss content preserved within the place-gloss

## F-006 — RESOLVED — 2026-05-20T10:20:00Z
fault: state-updates file — POV co-citation gap 8/9 — rubric-state-updates.md § Cross-facet contract mandates NI co-citation for all actor:taylor.* state entries; 8 of 9 entries lack it; adding 8 NI entries would breach band ceiling (6→14 NI = 51.8% vs 15-25% ceiling)
scope: line
change: option (c) applied — appended `# rubric-carve-out` annotation block to state-updates.md (before the first source block, after consolidated frontmatter); annotation documents: (1) rubric's own §Cross-facet contract explicitly scopes requirement to knowledge.*, mask-state, exposure-state — not mechanical-action states; (2) mechanical-action entries (position, inventory, lodging-payment, work-routine) are exempt per rubric's own scoping; (3) knowledge.coll-pattern and social-state.* entries that fall closer to the scoped zone are accepted-with-defense: adding NI would breach band ceiling; substance contract is mechanical-establishment/0-peak-bones; density-on-flat anti-pattern prohibits inflation to hit co-citation coverage; (4) citations to rubric-state-updates.md §Cross-facet contract and §Anti-patterns #9
criteria met: yes — annotation present; mechanical-action carve-out documented with rubric citation; option (c) as specified; no NI entries added; no band breach

## SESSION-END — 2026-05-20T10:25:00Z — facets-b01c01-hard-r1-six-findings-cont
findings-applied: 6 (F-001 confirmed from prior session; F-002 confirmed from prior session; F-003 proto-lines strip completed; F-004 exposition:5 consolidated into :6 + proto-lines stripped; F-005 confirmed from prior cycle; F-006 rubric-carve-out annotation applied)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-20T11:00:00Z — facets-b01c01-audience-gate-cycle2
dispatch: cycle-2 fixer for /and-facets b01c01 Phase 5b — 7 failing facets from audience-gate cycle-1; minimum-change per F-007 through F-013
target: active-project/theater/facets/location-state.md + interest-narrator.md + sensory.md + state-updates.md + memory.md + active-project/theater/dialogue/wren-stitch-maker-flea-bottom-ward.md + active-project/staff/dialogue-writer/taylor-hebert-kl-122ac.drafts.md + active-project/theater/proto-lines/b01-c01.md
audit-report: audience-gate cycle-1 per-reviewer verdict files (per-facet, per-persona)
findings-queued: 7 (F-007 through F-013)

## F-007 — RESOLVED — 2026-05-20T11:05:00Z
fault: loc-state:3 @11 dexterity-in-place anchor; continuity-from 2 token fails cross-scene fusion-eligible-runs check
scope: line
change: loc-state:3 deleted from location-state.md (gap-documented); [loc-state:3] stripped from proto-lines @11; no _inflight-r2 file to update
criteria met: yes

## F-008 — RESOLVED — 2026-05-20T11:10:00Z
fault: NI-1 @4 "the network" label — mechanism-label adjacent to Earth-Bet boundary; not in Taylor's canonical interior vocabulary; unanimous callout
scope: line (NI-1 rewrite) + defer-documentation (dark-fantasy doubled-register escalation)
change: NI-1 @4 rewritten to "the flies in the wall-bottom register the eye-lift before the eye lifts"; band-ceiling defer comment appended for dark-fantasy displacement-trigger request (6→7/27 would breach 25% cap)
criteria met: yes

## F-009 — RESOLVED (partial defer) — 2026-05-20T11:15:00Z
fault: sensory-disambiguation-pedant: sensory:2 @16 "cool" redundant with proto-line; sensory-modality-coverage: cap-breach + sound silence + smell silent-gap; sensory-old-state-reader: sensory:1 old-state unanchored to loc-state light-field; sensory:2 old-state structurally unanchored
scope: line (sensory:2 delete + sensory:1 defense-anchor + modality defer documentation)
change: (1) deleted sensory:2 @16 (replaced with gap-doc comment in sensory.md); stripped [sensory:2] from canonical proto-lines/b01-c01.md @16; no _inflight-r2/proto-lines-sensory.md exists. (2) added defense-anchor comment under sensory:1 @3 citing loc-state:1 "door-shadow across the entry" geometry cue + pre-noon time-of-day implication as old-state lineage. (3) appended audience-gate-cycle-1-defer block to sensory.md documenting sound (@15/@17) and smell (@11) modality silent-gap callouts as deferred; minimum-change discipline respected (adding 3 entries would reopen sparsity-band question). Sparsity post-fix: 1/27 = 3.7%, within 3-6% band.
criteria met: yes (charged-verb fault resolved; old-state anchoring documented; modality deferred with carry-forward block)

## F-010 — RESOLVED — 2026-05-20T11:20:00Z
fault: rubric-carve-out block in per-source taylor-hebert slice not propagated to consolidated state-updates.md top-of-file position; all 3 reviewers require it between frontmatter close and first source header
scope: line
change: inserted full rubric-carve-out comment block (29 lines) at top of state-updates.md between closing --- and # source: env; cite-index builder NOT rerun per dispatch instruction
criteria met: yes

## F-011 — RESOLVED — 2026-05-20T11:25:00Z
fault: (a) feel:1 not valid NI-spine substitute per rubric; (b) cond-override-architecture-residue-122ac slug form fails URI-FACETS-CYCLE-1 monument- prefix requirement; (c) file-level doubled-register risk if mem:1 cut
scope: line (slug rewrite + defense annotation rewrite + defer note)
change: (1) mem:1 target-reference changed from cond-override-architecture-residue-122ac to monument-override-architecture-prohibition; (2) defense annotation rewritten to cite rubric NI mandate explicitly + acknowledge gap + document feel-as-spine rationale + defer to rubric authority ruling; (3) audience-gate-cycle-1-defer note appended with delete vs. NI-add options
criteria met: yes — slug corrected; defense cites rubric accurately; gap acknowledged; carry-forward documented

## F-012 — RESOLVED — 2026-05-20T11:30:00Z
fault: taylor-hebert-kl-122ac.drafts.md chosen draft (Draft B @25) facet-licenses: [DEFERRED-TO-R2] unresolved
scope: line
change: replaced facet-licenses: [DEFERRED-TO-R2] with [state:17 @25, vibes:20 @25, feel:2 @27 (post-beat carrier), narrator:6 @27 (post-beat carrier)] in Draft B (chosen); rejected drafts A and C left unchanged
criteria met: yes

## F-013 — RESOLVED — 2026-05-20T11:35:00Z
fault: wren dialogue entry 2 @26 "they were not on your hand" — body-part precision reads as insect-tracking awareness leaking; worm-canon-pedant: use person-scale language
scope: line
change: "they were not on your hand" changed to "they were not on you" in active-project/theater/dialogue/wren-stitch-maker-flea-bottom-ward.md entry 2 @26; same change applied to chosen Draft B text in active-project/staff/dialogue-writer/wren-stitch-maker-flea-bottom-ward.drafts.md with inline change note
criteria met: yes — body-part precision removed; person-scale "you" preserves proximity-argument structure

## SESSION-END — 2026-05-20T11:40:00Z — facets-b01c01-audience-gate-cycle2
findings-applied: 7 (F-007 through F-013; F-007 pre-logged, confirmed; F-008 through F-013 resolved in this session)
findings-skipped: 0
exit: CLEAN (three audience-gate-cycle-1-defer carry-forwards documented: F-008 dark-fantasy displacement-trigger at @22-@23 band-ceiling blocked; F-009 modality silent-gaps sound+smell deferred; F-011 feel-as-spine NI-equivalence awaits rubric authority ruling)

## SESSION-START — 2026-05-20T12:00:00Z — facets-b01c01-cycle3
dispatch: cycle-3 fixer for /and-facets b01c01 Phase 5b — resolve 2 actionable facet failures (F-014 interest-narrator NI-6 rewrite, F-015 sensory sound-add + loc-state light-level); memory skip per cap-burn ruling (last cycle before cap = 3)
target: active-project/theater/facets/interest-narrator.md + active-project/theater/facets/sensory.md + active-project/theater/facets/location-state.md + active-project/theater/facets/_inflight-r2/proto-lines-narrator.md + canonical proto-lines
audit-report: active-project/staff/audience/dark-fantasy-reader/interest-narrator-r2-verdict.md + active-project/staff/audience/sensory-modality-coverage/sensory-r2-verdict.md + active-project/staff/audience/sensory-old-state-reader/sensory-r2-verdict.md
findings-queued: 3 actionable sub-tasks (F-014, F-015a sound, F-015b loc-state); 1 skip (memory — cap-burn)

## F-014 — RESOLVED — 2026-05-20T12:10:00Z
fault: interest-narrator NI-6 @27 in policy-declaration register ("she will not write the name..."); zero displacement-trigger fires across 6 entries; dark-fantasy-reader revise verdict with in-place rewrite path specified
scope: line
change: NI-6 @27 body rewritten from "she will not write the name above the block, not in the feed and not on the page she keeps for herself" to "the threshold holds and what is on the other side stays the size she will not name." — gap-narration pattern per dark-fantasy calibration anchor; cost of refusal rendered as held weight rather than policy stated; interest-narrator.md entry 6 body only; band stays at 6/27 = 22.2%; [narrator:6] token in proto-lines unchanged (body edit, no cite cascade); _inflight-r2/proto-lines-narrator.md @27 already carries [narrator:6] and requires no change
criteria met: yes — (a) policy-declaration register eliminated; (b) displacement-trigger register carried through refusal-to-look channel (gap-narration: "what is on the other side stays the size she will not name"); (c) cold-utilitarian voice maintained; (d) band ceiling not breached (22.2%)

## F-015b — RESOLVED — 2026-05-20T12:15:00Z
fault: sensory-old-state-reader: sensory:1 @3 old-state "corner-room-dim" anchored only to geometry cue ("door-shadow across the entry") in loc-state:1; no explicit light-level field; two-step inference flagged as moderate-revise
scope: line
change: loc-state:1 @1 in location-state.md extended with explicit light-level field: "light: threshold-dim, interior-corner dim under overcast morning backlight" appended to existing field list; sensory:1 @3 old-state "corner-room-dim" now traces near-verbatim to declared loc-state:1 light field; no cite-index change (loc-state:1 was already cited at @1; no new token); _inflight-r2/proto-lines-loc-state.md: field-add is internal to loc-state:1 entry, no cite token change required
criteria met: yes — explicit light-level field present in loc-state:1; sensory:1 old-state lineage resolved to near-verbatim match; two-step inference gap closed

## F-015a — RESOLVED — 2026-05-20T12:20:00Z
fault: sensory-modality-coverage: file is light-only single-modality (sensory:1 light @3, sensory:2 deleted); ≥1 sound entry required; @15 or @17 identified as clean addition anchors
scope: line
change: (1) sensory:3 @17 added to sensory.md: "sound: street-quiet-of-mid-afternoon -> bootfall-on-cobbles-from-the-Hook-bend"; studio-voice; ≤1 line; no narrative or moralization; @17 ("the boots strike the cobbles") is bare proto-line with no prior sensory citation; ID 3 is next-available (ID 2 gap preserved per F-009 cycle-2 deletion; no renumber). (2) [sensory:3] added to canonical proto-lines/b01-c01.md at @17. (3) created _inflight-r2/proto-lines-sensory.md with [sensory:3] at @17 (new file; no prior sensory inflight file existed). Modality coverage post-fix: light (@3) + sound (@17) = 2 modalities; floor met.
criteria met: yes — ≥1 sound entry present (sensory:3 @17); studio-voice maintained; ID gap 2 preserved; canonical proto-lines and inflight sensory file updated; modality floor satisfied

## memory — SKIPPED — 2026-05-20T12:21:00Z
fault: memory facet cycle-2 fail (3 revise on feel-as-spine defense); all three remediation paths have unacceptable costs
scope: escalate
change: none — memory.md untouched per dispatch cap-burn ruling; all three paths (add NI @9 = band-ceiling breach; delete mem:1 = SHAPE-FAIL single-register; rubric authority ruling = out of scope) cost more than the cap allows; orchestrator-critic verdict to document cap-burn with rationale
criteria met: n/a — skip is correct action per dispatch

## SESSION-END — 2026-05-20T12:25:00Z — facets-b01c01-cycle3
findings-applied: 3 (F-014 NI-6 rewrite; F-015b loc-state light-field; F-015a sensory:3 sound entry + proto-lines)
findings-skipped: 1 (memory — explicit cap-burn skip per dispatch; not a fixer failure)
exit: CLEAN (cap-burn on memory documented; orchestrator-critic verdict to close)

## SESSION-START — 2026-05-20T13:00:00Z — facets-rejected-removal
dispatch: remove two audience-gate cycle-3 rejected facet entries (sensory:3 @17 + mem:1 @9); per user directive post-cap-burn; minimum-change deletions only; no card routing
target: active-project/theater/facets/sensory.md + active-project/theater/facets/memory.md + active-project/theater/proto-lines/b01-c01.md + active-project/theater/facets/_inflight-r2/proto-lines-sensory.md + active-project/theater/facets/_inflight-r2/proto-lines-mem.md + active-project/theater/facets/_cite-index.md
audit-report: active-project/staff/auditor/facets-audience-gate-r3.md
findings-queued: 2 (sensory:3 deletion + mem:1 deletion; 7 files total across both)

## sensory:3-removal — RESOLVED — 2026-05-20T13:05:00Z
fault: sensory:3 @17 old-state "street-quiet-of-mid-afternoon" unanchored (NEW HARD from cycle-3 audience-gate); cycle-3 add introduced the finding
scope: line
change: (1) sensory.md: deleted live entry "3 @17 sound: ..." + "# audience-gate-cycle-3-note" block; replaced with gap-documentation comment (F-009-style) documenting cycle-3 rejection and user directive; ID gap 3 preserved. (2) proto-lines/b01-c01.md @17: stripped [sensory:3] token; line is now bare. (3) _inflight-r2/proto-lines-sensory.md: appended deletion clause to cite-cascade header; stripped [sensory:3] from @17 line.
criteria met: yes — live entry removed; documentation comment in place; [sensory:3] absent from all proto-lines surfaces; ID gap preserved

## mem:1-removal — RESOLVED — 2026-05-20T13:10:00Z
fault: mem:1 @9 feel-as-spine defense rejected by all 3 audience reviewers across cycles 1+2; rubric mandates NI co-citation; NI silent at @9; no carve-out exists; cap-burn final verdict
scope: line
change: (1) memory.md: deleted live entry "1 @9 the feet hold and the architecture stays the shape she will not build -> monument-override-architecture-prohibition" + entire "# defense: feel-as-spine" comment block (lines 7-27); replaced with gap-documentation comment (F-009-style) documenting audience-gate cycles 1+2 rejection and user directive; ID gap 1 preserved; mem:2 @18 intact. (2) proto-lines/b01-c01.md @9: stripped [mem:1] token; [feel:1] and [vibes:12] untouched. (3) _inflight-r2/proto-lines-mem.md: appended deletion clause to R2-mutations header; stripped [mem:1] from @9 line. (4) _cite-index.md: (a) "### mem (2 entries)" → "### mem (1 entry)"; (b) deleted "mem:1 @9 back=Y co=[feel:1, vibes:12]" line; (c) feel:1 @9 co-citations updated to remove mem:1; (d) vibes:12 @9 co-citations updated to remove mem:1.
criteria met: yes — live entry and defense block removed; documentation comment in place; [mem:1] absent from all proto-lines surfaces; cite-index header count corrected; feel:1 and vibes:12 co-citations updated; ID gap 1 preserved

## SESSION-END — 2026-05-20T13:15:00Z — facets-rejected-removal
findings-applied: 2 (sensory:3 deletion + mem:1 deletion; 6 files mutated)
findings-skipped: 0
exit: CLEAN

## SESSION-START — 2026-05-21T00:00:00Z — write-b01c02-pass2
dispatch: resolve 6 faults from /and-write Phase 2 audit on b01c02 — 4 FAULT-FORM + 1 FAULT-BONE-DELTA-MALFORMED; FLAG s02n02 no change required per audit
target: active-project/staff/screen-writer/b01c02-phase1-bones.md
audit-report: active-project/staff/auditor/write-b01c02-pass2.md
findings-queued: 6 (s01n03, s01n08, s01n10, s02n05, s03n04, s03n06)

## b01c02s01n03 — RESOLVED — 2026-05-21T00:01:00Z
fault: FAULT-FORM — "steps into the doorway" banned prepositional-destination form
scope: line
change: svo recast from "the water-carrier steps into the doorway" to "the water-carrier enters the doorway"; axis_moves + notes unchanged
criteria met: yes

## b01c02s01n08 — RESOLVED — 2026-05-21T00:02:00Z
fault: FAULT-FORM — "the two witnesses" plural subject violates singular-subject schema rule
scope: line
change: svo recast from "the two witnesses face the alley-mouth" to "the near witness faces the alley-mouth"; axis_moves + notes unchanged
criteria met: yes

## b01c02s02n05 — RESOLVED — 2026-05-21T00:03:00Z
fault: FAULT-FORM — "the two witnesses" plural subject violates singular-subject schema rule
scope: line
change: svo recast from "the two witnesses cross the lane" to "the near witness crosses the lane"; axis_moves + notes unchanged; same near-witness slug consistent with s01n08 fix
criteria met: yes

## b01c02s03n04 — RESOLVED — 2026-05-21T00:04:00Z
fault: FAULT-FORM — shape: held contradicted by discrete action verb "strikes"; axes_held invoked body-part license on a ledger mark not a body part
scope: line
change: reclassified from shape: held / axes_held (moral-framework) to shape: moving / axis_moves (knowledge up magnitude 1); notes updated to reflect knowledge-categorical-decision anchor; moral-framework held requirement transferred to s03n06 (see below)
criteria met: yes

## b01c02s03n06 — RESOLVED — 2026-05-21T00:05:00Z
fault: FAULT-FORM — "holds the pen" fails narrow holds license (pen is not a body part, not pressure-resisting)
scope: line
change: svo recast from "holds the pen" to "holds the hand"; added second axes_held entry for moral-framework (body-part stillness-against-pressure; impulse to extend accounting is the pressure resisted); capability axes_held rationale updated to name "the hand" explicitly; notes updated to dual-discipline framing; this bone now satisfies both s03 held-axis requirements
criteria met: yes

## b01c02s01n10 — RESOLVED — 2026-05-21T00:06:00Z
fault: FAULT-BONE-DELTA-MALFORMED — cost_ledger_anchor cl-social-tether-build (gain=social-tether, cost=position) present on a knowledge-axis bone; anchor-to-bone-axis mismatch
scope: line
change: removed cost_ledger_anchor field from b01c02s01n10; svo + axis_moves + notes unchanged; knowledge gains in s01 are unanchored per scene substance_delta per audit option (a)
criteria met: yes

## SESSION-END — 2026-05-21T00:07:00Z — write-b01c02-pass2
findings-applied: 6 (s01n03, s01n08, s01n10, s02n05, s03n04, s03n06)
findings-skipped: 0 (FLAG s02n02 no change required per audit — correctly excluded from repairs)
exit: CLEAN

## SESSION-START — 2026-05-21T12:00:00Z — write-b01c02-pass2-verify
dispatch: verify and apply 6 faults from /and-write Phase 2 audit on b01c02 — 4 FAULT-FORM + 1 FAULT-BONE-DELTA-MALFORMED (re-dispatch; prior session at 00:00:00Z already resolved all 6)
target: active-project/staff/screen-writer/b01c02-phase1-bones.md
audit-report: active-project/staff/auditor/write-b01c02-pass2.md
findings-queued: 6 (s01n03, s01n08, s01n10, s02n05, s03n04, s03n06)

## b01c02s01n03 — RESOLVED — 2026-05-21T12:01:00Z
fault: FAULT-FORM — "steps into the doorway" banned prepositional-destination form
scope: line
change: verified pre-applied — svo reads "the water-carrier enters the doorway"; no edit required
criteria met: yes

## b01c02s01n08 — RESOLVED — 2026-05-21T12:01:00Z
fault: FAULT-FORM — "the two witnesses" plural subject violates singular-subject schema rule
scope: line
change: verified pre-applied — svo reads "the near witness faces the alley-mouth"; no edit required
criteria met: yes

## b01c02s02n05 — RESOLVED — 2026-05-21T12:01:00Z
fault: FAULT-FORM — "the two witnesses" plural subject violates singular-subject schema rule
scope: line
change: verified pre-applied — svo reads "the near witness crosses the lane"; no edit required
criteria met: yes

## b01c02s03n04 — RESOLVED — 2026-05-21T12:01:00Z
fault: FAULT-FORM — shape: held contradicted by discrete action verb "strikes"; axes_held invoked body-part license on a ledger mark
scope: line
change: verified pre-applied — shape: moving, axis_moves: knowledge up 1, notes reflect knowledge-categorical anchor; no edit required
criteria met: yes

## b01c02s03n06 — RESOLVED — 2026-05-21T12:01:00Z
fault: FAULT-FORM — "holds the pen" fails narrow holds license (pen not a body part, not pressure-resisting)
scope: line
change: verified pre-applied — svo reads "holds the hand"; dual axes_held (capability + moral-framework both with body-part stillness-against-pressure rationales); notes carry dual-discipline framing; no edit required
criteria met: yes

## b01c02s01n10 — RESOLVED — 2026-05-21T12:01:00Z
fault: FAULT-BONE-DELTA-MALFORMED — cost_ledger_anchor cl-social-tether-build on knowledge-axis bone; anchor-to-bone-axis mismatch
scope: line
change: verified pre-applied — no cost_ledger_anchor field on this bone; knowledge axis_moves intact; no edit required
criteria met: yes

## SESSION-END — 2026-05-21T12:02:00Z — write-b01c02-pass2-verify
findings-applied: 6 (all pre-applied by prior session 2026-05-21T00:00:00Z; verified in-place)
findings-skipped: 0 (FLAG s02n02 no change required per audit — confirmed excluded)
exit: CLEAN

## SESSION-START — 2026-05-21T13:00:00Z — facets-b01c02-cycle1-fixes
dispatch: resolve 2 HARD findings (fault-001 CONSTRAINT, fault-002 RUBRIC-FIDELITY) from active-project/staff/auditor/facets-final-audit.md for chapter b01c02; SIGNAL findings not in scope
target: active-project/staff/exposition-author/glossed-terms.md + active-project/theater/facets/state-updates.md + active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md + active-project/theater/proto-lines/b01-c02.md
audit-report: active-project/staff/auditor/facets-final-audit.md
findings-queued: 2

## fault-001 — RESOLVED — 2026-05-21T13:05:00Z
fault: glossed-terms.md carried stale water-carrier and near-witness entries (deleted at R2.5) and pressed-labor-sweep with wrong @5 anchor (re-anchored to @4 at R2.5)
scope: line
change: struck water-carrier and near-witness entries (converted to comment lines explaining the R2.5 deletion so future chapters can re-gloss if terms recur); corrected pressed-labor-sweep first-mention-anchor from @5 to @4
criteria met: yes — water-carrier and near-witness removed from live register; pressed-labor-sweep reads @4
files touched: active-project/staff/exposition-author/glossed-terms.md
