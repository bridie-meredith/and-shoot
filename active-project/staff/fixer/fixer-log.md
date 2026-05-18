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
