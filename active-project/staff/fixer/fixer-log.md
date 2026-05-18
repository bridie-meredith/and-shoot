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

## fault-002 — RESOLVED — 2026-05-18T12:42:00Z
fault: both Aemond cards stated age: 10-11 at 122 AC (born 106 AC) — internally inconsistent and wrong per F&B canon; memory.md cast_roster also said "age 10-11"
scope: line
change: updated age field and all age-register mentions in (1) active-project/actors/aemond-targaryen-122ac/card.md, (2) cards/personas/aemond-targaryen-122ac.card.md to "12 at 122 AC (born 110 AC; claimed Vhagar at age 10 at Driftmark in 120 AC)"; updated memory.md cast_roster role line; updated cast-provisioning-log.md card action note and roster splice section; updated cast-selection.md slot 3 description and final roster table. Pre-fix backups written at active-project/actors/aemond-targaryen-122ac/card.pre-2026-05-18T124000Z.md and cards/personas/aemond-targaryen-122ac.pre-2026-05-18T124000Z.card.md.
criteria met: yes — born year (110 AC) and age (12) now internally consistent; F&B canon honored; cast_roster memory.md entry updated; vibe seeds updated (claimed at age 10; "nine years" corrected to "nine years" to Dance per revised age); structural function unchanged
