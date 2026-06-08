## SESSION-START — 2026-05-25T07:00:00Z — facets-cycle1-state-updates-remediation
dispatch: Phase 5b cycle-1 remediation for state-updates facet — all 3 reviewers dissented; cross-reviewer dedupe + minimum-change fixes to per-character slice files and consolidated state-updates.md
target: active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md + state-updates-wren-stitch-maker-flea-bottom-ward.md + state-updates.md
audit-report: active-project/staff/audience/{cape-fic-reader,dark-fantasy-reader,worm-canon-pedant}/state-updates-r1-verdict.md
findings-queued: tbd (deduping across 3 verdicts)

## SESSION-START — 2026-05-25T10:00:00Z — and-facets-cycle1-fixes-state-updates
dispatch: /and-facets Phase 5b cycle-1 remediation — state-updates facet, all 3 reviewers dissented; cross-reviewer dedupe + minimum-change fixes; log to this file
target: active-project/theater/facets/state-updates-taylor-hebert-kl-122ac.md + state-updates-wren-stitch-maker-flea-bottom-ward.md + state-updates.md
audit-report: active-project/staff/audience/cape-fic-reader/state-updates-r1-verdict.md + dark-fantasy-reader/state-updates-r1-verdict.md + worm-canon-pedant/state-updates-r1-verdict.md
findings-queued: tbd — deduplication pass required before count

## DEDUPE-ANALYSIS — WORKING — 2026-05-25T10:05:00Z
note: reading all 3 verdicts + facet files + state.md + cite-index; mapping deduped findings before applying patches

## DEDUPED FINDINGS TABLE

| Entry | cape-fic | dark-fantasy | worm-canon | Deduped verdict | Action |
|-------|----------|--------------|------------|-----------------|--------|
| state:1 @21 oswyn.location | ACCEPT | CORRECT | ACCEPT | PASS | no change |
| state:2 @26 oswyn.relationship_to_taylor | ACCEPT+note | CORRECT | ACCEPT | PASS | no change |
| state:3 @12 taylor.deployment-state | ACCEPT | CORRECT | ACCEPT | PASS | no change |
| state:4 @12 taylor.capability_axis | FLAG | CONTESTED (field-on-schema) | REJECT (ledger-as-state) | REJECT | DELETE — ledger-as-state anti-pattern #7; field IS on state.md but entry posts chapter-aggregate delta as real-time bone flip |
| state:5 @17 taylor.posture | ACCEPT | REJECT (NI co-citation absent) | ACCEPT+NI note | REJECT | DELETE — POV actor-state rule requires NI co-citation at @17; cite-index confirms state:5 @17 is lonely; no NI entry at @17; cannot add NI here (different facet author); note for NI author |
| state:6 @21 taylor.social_tether_prot_axis | FLAG (registration framing) | CONTESTED | REJECT (ledger-as-state + invented field) | REJECT | DELETE — field not on actor:taylor state.md (only capability_axis, moral_framework_axis, political_register_prot_axis, relational_anchor_status_axis, moral_legibility_to_self_axis exist); also ledger-as-state; also registration framing |
| state:7 @24 taylor.body-orientation | ACCEPT | CORRECT | ACCEPT | PASS | no change |
| state:8 @26 taylor.ward-recognition | FLAG (ambiguous authority + NI absent) | REJECT (NI absent + double-filing) | REJECT (cross-POV + NI absent) | REJECT | DELETE — Oswyn's categorization already canonical in state:2 on Oswyn slice; authority violation on Taylor slice; NI absent |
| state:9 @27 wren.relational_anchor_to_taylor | ACCEPT+note | CORRECT (value note) | soft-flag (missing field-extension + malformed value) | REVISE | ADD field-extension comment; FIX value from "observation-traced-d01-deterrence" to "observation-traced-chapter-1" |

Total deduped findings: 5 (4 DELETE + 1 REVISE)

## fault-SU-001 (state:4 DELETE) — RESOLVED — 2026-05-25T10:15:00Z
fault: capability_axis @12 posted chapter-aggregate substance delta as a real-time mid-bone canonical field-flip; anti-pattern #7 (pre-empting / ledger-as-state); convergent REJECT from worm-canon-pedant + CONTESTED from dark-fantasy-reader
scope: line
change: entry deleted from state-updates-taylor-hebert-kl-122ac.md and from consolidated state-updates.md; [state:4] citation removed from proto-lines @12; cite-index state:4 entry deleted; state:3 co-list updated to remove state:4; narrator:4 co-list updated to remove state:4; vibes:3/4/8 co-lists updated to remove state:4; deletion comment added to Taylor slice and consolidated file
criteria met: yes — ledger-as-state entry removed; handoff_out canonical record of capability rank 3 not affected; no actor state.md mutation

## fault-SU-002 (state:5 DELETE) — RESOLVED — 2026-05-25T10:15:00Z
fault: posture @17 is a POV actor-state entry with no narrator-interest co-citation at @17; cite-index confirms state:5 is a lonely entry; rubric cross-facet contract: actor:<POV>.* requires NI co-citation; REJECT from dark-fantasy-reader; NI gap noted by worm-canon-pedant
scope: line
change: entry deleted from state-updates-taylor-hebert-kl-122ac.md and consolidated state-updates.md; [state:5] citation removed from proto-lines @17 (bone now bare); cite-index state:5 entry deleted; deletion comment added noting entry may be re-added once narrator-interest author provides @17 NI entry; @17 added to bare-protolines list in cite-index
criteria met: yes — cross-facet-contract-violating entry removed; re-add path documented for narrator-interest author
cross-facet-impact: narrator-interest author must add @17 entry (taylor lifts the hands — hands-up-mouth-shut witness-facing is the chapter's key public-frame transition) before state:5 can be re-authored

## fault-SU-003 (state:6 DELETE) — RESOLVED — 2026-05-25T10:15:00Z
fault: social_tether_prot_axis @21 — (a) field not present on actor:taylor-hebert-kl-122ac/state.md (confirmed: stats block has capability_axis, moral_framework_axis, political_register_prot_axis, relational_anchor_status_axis, moral_legibility_to_self_axis — no social_tether_prot_axis); (b) ledger-as-state: chapter-aggregate delta posted as bone-anchored canonical field-flip; (c) registration framing ("Taylor enters Oswyn's awareness layer"); REJECT from worm-canon-pedant; CONTESTED from dark-fantasy-reader; FLAG from cape-fic-reader
scope: line
change: entry deleted from state-updates-taylor-hebert-kl-122ac.md and consolidated state-updates.md; [state:6] citation removed from proto-lines @21; cite-index state:6 entry deleted; state:1 co-list updated to remove state:6; narrator:5 co-list updated to remove state:6; feel:1 co-list updated to remove state:6; vibes:5/6/7 co-lists updated to remove state:6; exposition:8 co-list updated to remove state:6; @21 pile-up count drops from 8 to 7; deletion comment added
criteria met: yes — invented-field + ledger-as-state entry removed

## fault-SU-004 (state:8 DELETE) — RESOLVED — 2026-05-25T10:15:00Z
fault: ward-recognition @26 — (a) cross-POV authority violation: encodes Oswyn's categorization of Taylor on Taylor's actor slice; Oswyn's categorization already canonically filed in Oswyn slice as state:2 (relationship_to_taylor: categorized-known-unknown-witch-adjacent); (b) NI co-citation absent for POV actor-state entry; convergent REJECT from worm-canon-pedant and dark-fantasy-reader; FLAG from cape-fic-reader
scope: line
change: entry deleted from state-updates-taylor-hebert-kl-122ac.md and consolidated state-updates.md; [state:8] citation removed from proto-lines @26; cite-index state:8 entry deleted; state:2 co-list updated to remove state:8; narrator:9 co-list updated to remove state:8; mem:2 co-list updated to remove state:8; deletion comment added
criteria met: yes — cross-POV authority violation removed; Oswyn's categorization remains canonical in Oswyn slice; no double-filing

## fault-SU-005 (state:9 REVISE) — RESOLVED — 2026-05-25T10:20:00Z
fault: wren relational_anchor_to_taylor entry missing field-extension comment (rubric §"Field-extension protocol" requires documentation); value "observation-traced-d01-deterrence" contains authoring metadata ("d01") and an inaccurate affect charge ("deterrence" implies Wren is warned-off; chapter text does not support this — Wren faces Taylor with no exchange); convergent soft-flag from worm-canon-pedant + value note from dark-fantasy-reader + cape-fic-reader
scope: line
change: (a) field-extension comment added per rubric §field-extension protocol, documenting new field, old and new value semantics, and persistence claim; (b) value changed from "observation-traced-d01-deterrence" to "observation-traced-chapter-1" — removes authoring metadata slug and inaccurate deterrence charge; "chapter-1" anchors the observation to the chapter without inventing an affect; change applied to per-character slice (state-updates-wren-stitch-maker-flea-bottom-ward.md) and consolidated state-updates.md; state:9 entry in cite-index carries correct @27 back=Y with full co-list (unchanged)
criteria met: yes — field-extension documented per rubric; value is clean, no embedded metadata, no inaccurate affect claim; state:9 back-link and co-citations unchanged

## SESSION-END — 2026-05-25T10:20:00Z — and-facets-cycle1-fixes-state-updates
findings-applied: 5 (4 DELETEs + 1 REVISE)
findings-skipped: 0
exit: CLEAN
cross-facet-impacts:
  1. narrator-interest author MUST add @17 NI entry before state:5 (taylor.posture) can be re-added; @17 is now a bare protoline
  2. proto-lines @12/@17/@21/@26 updated (citation removals)
  3. cite-index updated: state section reduced from 9 to 5 entries; all co-citation lists purged of deleted state IDs
  4. wren value change ("observation-traced-chapter-1") has no downstream cite-index impact — state:9 entry IDs and back-links are stable
