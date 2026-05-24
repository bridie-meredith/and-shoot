---
report: stitch-pipeline-audit
scope: chapter
target: b01c01
run-label: cycle-3-cap-burn-redo
timestamp: 2026-05-24T06:00:00Z
auditor: auditor-fork
---

# Stitch Pipeline Audit — b01c01 (cycle-3-cap-burn-redo)

Sources read:
- `active-project/staff/stitcher/render-log-b01-c01.md`
- `active-project/draft/b01-c01.md`
- `active-project/draft/b01-c01.annotated.md`
- `active-project/staff/showrunner/memory.md` (chapters[b01c01] section)
- `staff/stitcher/card.md`
- `.claude/commands/and-stitch.md`
- `schemas/stitch-render-log.schema.md`
- `schemas/stitch-feedback.schema.md` (referenced; not materially applicable to this run)
- `schemas/stitch-profile.schema.md` (referenced via schema defaults)
- `staff/auditor/card.md`

---

## audit

scope: chapter
target: b01c01
timestamp: 2026-05-24T06:00:00Z

findings:

---

### fault-001
- id: fault-001
- type: pass
- what: FAULT-PHASE-7-NO-SWEEP check — render-log Phase 7 Q-walk section
- why: The spec requires one Q-line per post-Phase-6 sentence. Phase 6 completion summary declared 37 sentences. Phase 7 Q-walk emits exactly 37 entries (¶1:1 / ¶2:6 / ¶3:4 / ¶4:3 / ¶5:4 / ¶6:3 / ¶7:2 / ¶8:1 / ¶9:2 / ¶10:2 / ¶11:2 / ¶12:4 / ¶13:2 / ¶14:1 = 37). Each entry contains a Q1–Q9 line and an explicit KEEP or REWORD disposition. Phase 7 completion summary confirms "sentences Q-walked: 37 of 37." The walk was dispatched as "per-scene (3 scene-forks; sentences walked serially inside each)" — this is within the spec's "per-paragraph or per-scene (each subagent walks the paragraph/scene's sentences serially)" dispatch granularity. FAULT-PHASE-7-NO-SWEEP does NOT apply.
- criteria: N/A

---

### fault-002
- id: fault-002
- type: pass
- what: FAULT-RECONCILE-IMBALANCE check — render-log Phase 8 RECONCILE block
- why: The spec requires two RECONCILE equalities: bones rendered+merged+dropped+illegible = authored; facets rendered+dropped+unrendered_remainder = cite-index count. The render-log emits: `RECONCILE: bones rendered=27+merged=0+dropped=0+illegible=0=27 | authored bones = 27 ✓` and `RECONCILE: facets rendered=24+dropped=25+unrendered_remainder=0=49 | cite-index facet entries = 49 (after cap-burn DELETE of dialogue-coll:1) ✓`. Both sides check: 27=27 and 24+25+0=49. Phase 0 independently confirms bones file has 27 live bones (flat IDs 1–29 with time-skip blanks at @10, @21) and cite-index has 49 facet entries (after cap-burn DELETE). FAULT-RECONCILE-IMBALANCE does NOT apply.

  Additional accounting integrity check: facets_dropped=25 is declared as 24 schema-forbidden (14 state:* + 10 vibes:*) + 1 Phase-2 DROP-IMAGE-OVERLAP (mem:1 @9). 14+10+1=25. Internally consistent. No FLAG-UNRENDERED-REMAINDER. No FAULT-RECONCILE-MISSING (RECONCILE block present).
- criteria: N/A

---

### fault-003
- id: fault-003
- type: pass
- what: FAULT-PHASE-1-CONSOLIDATED check — render-log Phase 1 section
- why: The spec states the orchestrator must NOT render Phase 1 prose inline; every Phase 1 prose block must correspond to a fork-id entry. The render-log shows three scene-fork entries under Phase 1: fork-001 (scene-A @1–@9), fork-002 (scene-B @11–@20), fork-003 (scene-C @22–@29). Each fork entry contains a full bones-consumed list, lens-decider trace per bone, variance-moves, refusals, bone-walk with per-bone dispositions, and drift-risk assessment. The render-log Phase 1 header declares: "Three scene-forks, serialized across scenes… Dispatched as general-purpose Agent forks under the stitcher-card protocol." All 27 bones are accounted for in one of the three fork bone-walks. No Phase 1 prose block appears without a corresponding fork entry. FAULT-PHASE-1-CONSOLIDATED does NOT apply.

  Note: the render-log describes these as "general-purpose Agent forks" rather than stitcher-typed forks. The stitcher card explicitly notes "no stitcher subagent type registered; general-purpose with full inline protocol" — this is compliant with the spec's requirement for real Agent calls, not orchestrator inline-generation.
- criteria: N/A

---

### fault-004
- id: fault-004
- type: pass
- what: FAULT-EXPOSITION-AUDIT-MISS check — Phase 7 Q9/Q6 application to exposition-derived sentences
- why: The spec requires Phase 7 to apply Q9 (awkward words) and Q6 (fancy punctuation) normally to exposition-derived sentences while treating Q1/Q5/Q8 borderlines as KEEP. Three exposition-derived sentences were Q-walked: ¶1 S1 (exposition:1 @1 em-dash-fold), ¶2 S4 (exposition:2 @4 em-dash-fold), ¶8 S1 (exposition:5 @22 em-dash-fold). Phase 7 completion summary records "FAULT-EXPOSITION-AUDIT-MISS: 0 (Q9 + Q6 checks on exposition-derived sentences ¶1 / ¶2 S4 / ¶8 all PASS)." Reviewing the Q-walk entries: ¶1 S1 Q9=no, Q6=no → KEEP; ¶2 S4 Q9=no, Q6=no → KEEP (exposition-policy noted); ¶8 S1 Q9=no, Q6=no → KEEP (Q6 checked: two em-dashes + one semicolon judged necessary, not reached-for). All three passed Q9 and Q6 without generating FAULT-EXPOSITION-AUDIT-MISS findings. Carve-out applied correctly (Q1/Q5/Q8 pre-cleared on these sentences). FAULT-EXPOSITION-AUDIT-MISS does NOT apply.
- criteria: N/A

---

### fault-005
- id: fault-005
- type: pass
- what: FAULT-DIALOGUE-AUDIT-MISS check — Phase 7 Q-application to dialogue-utterance-derived sentences
- why: The spec requires dialogue utterances to have Q1/Q5/Q8/Q9/Q6 all pre-cleared (KEEP), with Q9 hits surfaced as FAULT-DIALOGUE-AUDIT-MISS rather than triggering stitcher REWORD. Attribution clauses remain subject to all Q-checks normally. The render-log Q-walk entries for dialogue sentences: ¶9 S1–S2 (wren:1), ¶11 S1–S2 (taylor:2), ¶12 S2–S3 (wren:2) — all marked KEEP with "DIALOGUE-UTTERANCE-DERIVED → all Q pre-cleared." Attribution clauses ("she said," "I said") are Q1-checked separately and passed. Phase 7 completion summary confirms "FAULT-DIALOGUE-AUDIT-MISS: 0." FAULT-DIALOGUE-AUDIT-MISS does NOT apply.
- criteria: N/A

---

### fault-006
- id: fault-006
- type: pass
- what: Bone-faithfulness fence compliance — all six axes (dialogue=no, body=no, spatial=no, route=no, scene-prose=no, cognitive=no) at Phase 1 across all three scene-forks
- why: The spec enforces the bone-faithfulness fence at Phase 1: no invented dialogue, body detail, spatial detail, route detail, scene prose, or cognitive content beyond cited facets. Each scene-fork's refusals block was checked:
  - fork-001 refusals: did not invent dialogue for @8 (bare per cap-burn), did not render schema-forbidden vibes:1/2/3/4 or state:1/2/3/6/7/8/9, did not invent body/spatial/route/scene-prose/cognitive detail beyond cited facets. @8 silent-action rendered per cap-burn license — this is not invented dialogue content; it is a bare-speech-bone disposition, which is fence-compliant (the fence forbids inventing dialogue content, not rendering a bare bone as silent action).
  - fork-002 refusals: did not add Watch/Hook gloss (deleted exposition entries), did not invent NI at @19 (narrator:4 deleted), did not render schema-forbidden facets, did not invent body/dialogue/spatial/cognitive content beyond facets.
  - fork-003 refusals: did not invent interior at @27, did not expand @29 beyond SVO, did not name Khepri in interior, no non-basic attribution verbs, exposition:5 rendered once only, speaker-paragraph rule honored, schema-forbidden vibes not rendered.
  Annotated draft trace blocks independently confirm all six fence axes held (bone-faithfulness fence header in Phase 0.5 pre-flight confirms `bone-fence: enforced (dialogue=no, body=no, spatial=no, route=no, scene-prose=no, cognitive=no)`). No fence violation found.
- criteria: N/A

---

### fault-007
- id: fault-007
- type: pass
- what: Cap-burn @8 carry-through — logged as LEGACY-SILENT-SPEECH + BARE-SPEECH-BONE-CAP-BURN, NOT as FAULT-DIALOGUE-MISSING
- why: The spec (Phase 0.5 and 0.7) requires the bare-speech-bone @8, admitted under cap-burn license from `staff/auditor/facets-cap-burn-b01c01-20260524T021822Z.md`, to be rendered as silent action and logged as LEGACY-SILENT-SPEECH + BARE-SPEECH-BONE-CAP-BURN — NOT as FAULT-DIALOGUE-MISSING. Checking: Phase 0.5 pre-flight explicitly states "BARE-SPEECH-BONE-CAP-BURN @8 (NOT FAULT-DIALOGUE-MISSING — disposition is upstream-ACCEPTED)." Phase 0.7 dialogue intake confirms the same. Phase 1 fork-001 @8 entry: "BARE-SPEECH-BONE-CAP-BURN per cap-burn DELETE (fault-030 ACCEPTED-AT-CAP-BURN); LEGACY-SILENT-SPEECH." Phase 8 STATS confirms cap_burn_handling field records "1 bare-speech-bone @8 ACCEPTED-AT-CAP-BURN." The deleted utterance "There's mending if you can hold a needle." does not appear anywhere in the clean draft or annotated draft. The clean draft L9 reads "Coll's needle moved, his attention not landing on my face." — silent needle-action per cap-burn license. FAULT-DIALOGUE-MISSING was correctly NOT logged. Cap-burn carry-through is clean.
- criteria: N/A

---

### fault-008
- id: fault-008
- type: pass
- what: Phase 8 scene-callout HARD-strip — clean draft contains no ## Scene N / [SCENE BREAK] / --- SCENE --- literals
- why: The spec requires HARD-stripping of scene-callout markers from the clean draft. Phase 8 render-log records: "Clean draft HARD-strip check: scanned `active-project/draft/b01-c01.md` for `## Scene N` / `[SCENE BREAK]` / `--- SCENE ---` / HTML scene-comments — NONE found. Scene boundaries surface as paragraph breaks only. PASS." Direct inspection of `active-project/draft/b01-c01.md` confirms: the file contains no `## Scene`, `[SCENE BREAK]`, or `--- SCENE ---` literals. Scene boundaries are conveyed only by blank-line paragraph breaks. HTML scene comments (`<!-- SCENE-A -->` etc.) appear only in the annotated draft (`b01-c01.annotated.md`), which is the traced/debug view where their presence is explicitly permitted per the spec. Clean draft is callout-free.
- criteria: N/A

---

### fault-009
- id: fault-009
- type: pass
- what: Phase 9 cold-read agent uninformed — read only clean draft, did not open bones/facets/render-log
- why: The spec requires the Phase 9 cold-read agent to be dispatched as "ONE general-purpose agent" with the canonical Phase 9 prompt instructing it to read ONLY the clean draft. The render-log Phase 9 records: "Dispatched one general-purpose agent with the canonical Phase 9 prompt; agent instructed to read ONLY `active-project/draft/b01-c01.md`." The cold reader's six answers are consistent with an uninformed reader: answer 1 lists events that are all recoverable from the clean draft alone; answer 3 explicitly acknowledges the causality as dependent on faith ("routine I have to take on faith") rather than on graph-context; answer 6's one-line summary references only what the clean draft contains ("a covert outsider… quietly made by a local ward-girl who notices that insects won't land on him"). There is no evidence the cold reader accessed the bones file, facets, render-log, or showrunner memory — these are inaccessible to an uninformed agent absent explicit dispatch context. Cold-read agent was correctly uninformed.
- criteria: N/A

---

### fault-010
- id: fault-010
- type: pass
- what: Intermediate-draft pruning — no .phase-1/6/7.draft.md files remain on disk
- why: The spec requires Phase 8 to delete `active-project/draft/<slug>.phase-*.draft.md` files after the clean + annotated draft are confirmed on disk (absent `--keep-drafts` flag, which was not passed on this run). Phase 8 render-log records deletion of three files: `b01-c01.phase-1.draft.md`, `b01-c01.phase-6.draft.md`, `b01-c01.phase-7.draft.md`. Direct read-attempts at those paths confirm none exist (file-not-found for all three). No `b01-c01.preamble.md` exists (Phase 0.6 produced no episode-open content; preamble_source=none, consistent with the spec's pruning rule). Intermediate drafts are fully pruned.
- criteria: N/A

---

### fault-011
- id: fault-011
- type: pass
- what: Showrunner memory writeback scope — stitcher metadata only, no other fields touched
- why: The spec requires Phase 8 to update showrunner memory scoped to stitcher metadata only: `stitched`, `stitch_path`, `stitch_render_log`, `stitch_stats`, and `chapters[b01c01].cold_read` (Phase 9). All other fields (`chunk`, `scenes`, `substance`, `bones`, `handoff`, `audience-gate`, `orchestrator_critic_verdict`, `substance_bone_gate_verdict`) must be preserved as-is. Render-log Phase 8 showrunner memory writeback section declares exactly four fields updated: `stitched: false→true`, `stitch_path`, `stitch_render_log`, `stitch_stats`. Phase 9 Step 4 records writing `chapters[b01c01].cold_read`. Reading showrunner memory `chapters[b01c01]` confirms: bones_count=27, status=audited-r1, substance_bone_gate_verdict=PASS, bones_review, all audience-gate fields, chunk, handoff_in/out — all preserved. The `stitched: true` and `stitch_*` fields are present and consistent with the render-log values. `cold_read` block is present with the Phase 9 PASS verdict and recovered_summary. Writeback is correctly scoped to stitcher metadata.
- criteria: N/A

---

### fault-012
- id: fault-012
- type: flag
- what: Phase 1 fork-002 @16 — proactive-cull of feel:2 before Phase 2 redundancy cull
- why: The stitcher card specifies Phase 1 renders all facet content and defers redundancy decisions to Phase 2. Fork-002 proactively culled feel:2 @16 at Phase 1 (subsumed into mem:2) rather than rendering both and letting Phase 2 decide. This is a mild protocol deviation: Phase 1 forks are not licensed to cull; only Phase 2 holds the cull authority. The deviation was caught by the fork's own drift-risk log and resolved correctly via Phase 5 UN-MERGE-RESCUE. The final prose at L17 ("I held both hands flat against the mesh.") is feel:2 verbatim, correctly restored. No downstream prose damage; the deviation is historically documented and mechanically resolved. This is a SOFT flag, not a HARD fault, because the Phase 5 rescue path is the canonical repair mechanism and it fired correctly.
- criteria: N/A (no fix required; the deviation was self-corrected within the run)

---

### fault-013
- id: fault-013
- type: flag
- what: Phase 1 fork-002 @17 — lens-trace mis-citation (rule 2 cited for tag=up; correct rule is rule 4 default kinetic)
- why: Fork-002 lens-decider trace for @17 mis-cited rule 2 as firing (sensory spike/drop rule) when sensory:4 carries tag=up, not tag=spike or tag=drop. Rule 2 fires only on spike or drop. The correct trace is rule 4 default kinetic (sensory leads trivially as the only active lens). Render outcome is identical; the surface deviation is render-log trace quality only. The render-log itself notes "LENS-TRACE-MIS-CITATION (minor; outcome correct)" and the Phase 6 completion summary acknowledges it as corrected in the render-log only. No prose change required. Auditor-trace quality flag; no fixer dispatch.
- criteria: N/A (render-log correction only; no prose or downstream change)

---

### fault-014
- id: fault-014
- type: pass
- what: Phase 7 Q-walk — per-sentence counts reconciled against Phase 6 sentence-terminator count
- why: Phase 6 completion summary states "sentence-terminator count: 37 (approximate sentence count ~34, allowing for em-dash internal pauses)." Phase 7 Q-walk summary states "sentences Q-walked: 37 of 37." The Phase 7 sentence inventory at the top of the Q-walk section declares "37 sentences across 14 paragraphs" and enumerates the paragraph breakdown (totals to 37). Clean draft inspection: counting sentence-ending punctuation (periods, question marks — no exclamation marks present) across the 14-paragraph draft yields 37 terminal sentences. The discrepancy between Phase 6's "~34 allowing for em-dashes" and the actual 37 is immaterial — Phase 6 noted this was approximate, and Phase 7's authoritative 37-sentence count takes precedence. 37 Q-lines were emitted for 37 sentences. Count checks out.
- criteria: N/A

---

### fault-015
- id: fault-015
- type: pass
- what: Phase 8 STATS word count — render-log vs annotated draft consistency
- why: Phase 6 summary: 551 words. Phase 7 REWORD removed "-sensation" (2 characters, part of one word — Phase 7 draft delta: 551→549 words). Phase 8 STATS reports words=551. This appears to contradict the Phase 7 delta. However, Phase 7 completion summary reads "word count: 549 (Phase 6: 551; delta -2 from '-sensation' removal)" while Phase 8 STATS reports 551. The render-log Phase 8 STATS block shows words=551, which conflicts with Phase 7's final word count of 549. Checking the clean draft directly: counting words in the clean draft yields a result consistent with the draft's prose (not auditor-countable to exact figure from static inspection, but the 2-word discrepancy between 549 and 551 is within Phase 7's own stated single-word REWORD scope). This is a minor internal inconsistency in the render-log's word-count field (Phase 7 reports 549, Phase 8 STATS reports 551). The 2-word delta is the "-sensation" removal. The STATS field at Phase 8 appears to have used the Phase 6 word count rather than re-counting post-Phase-7. This is a SOFT logging inconsistency — the draft prose itself is consistent with the Phase 7 REWORD (the annotated draft at L13 shows "the hand taking its first count of the day" without "-sensation"). The discrepancy is in the render-log STATS field only, not in the prose.
- criteria: N/A (prose correct; render-log STATS word-count field has a 2-word logging inconsistency of no downstream consequence)

---

## PIPELINE-CLEAN verdict block

All twelve primary checks resolved as follows:

| Check | Result | Finding |
|---|---|---|
| FAULT-PHASE-7-NO-SWEEP | PASS | 37 Q-lines emitted for 37 post-Phase-6 sentences; one per sentence; dispatched as 3 scene-forks walking sentences serially |
| FAULT-RECONCILE-IMBALANCE (bones=27) | PASS | bones 27+0+0+0=27 = authored 27 ✓ |
| FAULT-RECONCILE-IMBALANCE (facets=49) | PASS | facets 24+25+0=49 = cite-index 49 ✓ |
| FAULT-PHASE-1-CONSOLIDATED (3 real Agent forks) | PASS | 3 scene-window scene-forks declared and logged; fork-001/002/003 with full bone-walks; no orchestrator-inline rendering evidence |
| FAULT-EXPOSITION-AUDIT-MISS | PASS | Q9/Q6 applied normally to all 3 exposition-derived sentences; all passed; Q1/Q5/Q8 carve-out correctly applied |
| FAULT-DIALOGUE-AUDIT-MISS | PASS | All dialogue-utterance-derived sentences pre-cleared for Q1/Q5/Q8/Q9/Q6; attribution clauses Q-checked normally; no fault |
| Bone-faithfulness fence | PASS | All 6 axes (dialogue/body/spatial/route/scene-prose/cognitive=no) held across all 3 scene-forks; verified via fork refusals + annotated draft traces |
| Cap-burn @8 carry-through | PASS | Logged LEGACY-SILENT-SPEECH + BARE-SPEECH-BONE-CAP-BURN; NOT FAULT-DIALOGUE-MISSING; deleted utterance absent from draft; silent-action render per license |
| Phase 8 scene-callout HARD-strip | PASS | Clean draft contains no ## Scene N / [SCENE BREAK] / --- SCENE --- literals; scene-comments confined to annotated draft |
| Phase 9 cold-read agent uninformed | PASS | Dispatched general-purpose agent with canonical Phase 9 prompt; answers consistent with draft-only access; no graph-context leakage |
| Intermediate-draft pruning | PASS | b01-c01.phase-1.draft.md, b01-c01.phase-6.draft.md, b01-c01.phase-7.draft.md all absent from disk; no preamble artifact |
| Showrunner memory writeback scope | PASS | 4 stitcher-metadata fields updated (stitched/stitch_path/stitch_render_log/stitch_stats) + cold_read block at Phase 9; all other chapter fields preserved |

Additional secondary checks:
| Check | Result | Finding |
|---|---|---|
| Phase 7 sentence count reconciliation (37=37) | PASS | Phase 6 terminator count 37; Phase 7 inventory 37; clean draft terminal sentences 37 |
| FAULT-RECONCILE-MISSING (block present) | PASS | RECONCILE block present in Phase 8; both lines balance |
| FLAG-UNRENDERED-REMAINDER | PASS | unrendered_remainder=0; all 49 cite-index entries accounted for in rendered or dropped columns |
| Phase 1 fork-002 proactive feel:2 cull | SOFT flag (fault-012) | Protocol deviation (Phase 1 culled instead of Phase 2); self-corrected via Phase 5 UN-MERGE-RESCUE; no prose damage |
| Phase 1 fork-002 lens-trace mis-citation @17 | SOFT flag (fault-013) | Render-log trace quality only; outcome correct; no prose change |
| Phase 8 STATS word-count field | SOFT flag (fault-015) | 2-word discrepancy (549 vs 551) between Phase 7 final count and Phase 8 STATS; prose correct; render-log field inconsistency only |

**VERDICT: PIPELINE-CLEAN**

Total checks run: 15. HARD findings: 0. SOFT findings: 3 (fault-012, fault-013, fault-015 — all flags, no fixer dispatch required). SIGNAL findings: 0 from this audit (11 staging signals from Phase 9 `/and-review staging` are already recorded in `active-project/staff/reviews/staging-b01c01-20260524T1.md` and are outside the scope of this pipeline-fidelity audit).

The three SOFT flags are:
- fault-012: Phase 1 fork-002 proactive feel:2 cull — protocol deviation self-corrected within the run by Phase 5 UN-MERGE-RESCUE.
- fault-013: Phase 1 fork-002 lens-trace mis-citation @17 — render-log trace quality; no prose change.
- fault-015: Phase 8 STATS word-count field 2-word logging inconsistency — prose correct; render-log metadata only.

None of the three SOFT flags represent papering-over of a problem. None require fixer dispatch. The pipeline executed per spec on all twelve primary checks.
