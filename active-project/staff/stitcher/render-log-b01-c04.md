# render-log — b01-c04 (multi-arm; tournament + cherry-pick default)

profile: schema-defaults
persona: neutral (no project-scoped persona; matches c01-c03)
narrator: taylor-hebert-kl-122ac
voice: first-person past, contractions: off (clinical-utilitarian)
phase-7-mode: strict
generated-date: 2026-05-27
slug: b01-c04
bones-file: active-project/theater/bones/b01-c04.md
cite-index: active-project/theater/facets/_cite-index.md
scene-map: active-project/theater/facets/scene-map-b01-c04.md
phase-1-mode: scene-window
cherry-pick: paragraph (default; URI-STITCH-CHERRY-PICK-DEFAULT-ON 2026-05-27)
flags: (none — auto-alt + tournament + cherry-pick all default-on per URI-STITCH-MULTI-ARM-DEFAULT-ON 2026-05-27)
rewire-note: This run uses the URI-STITCH-MULTI-ARM-DEFAULT-ON behavior committed 2026-05-27 — Phase 0 step 4b auto-authors one counterweight alt-exemplar when |candidates| < 2 on-disk, making multi-arm + tournament + cherry-pick the practical default.

## Phase 0 — validate + load

inputs present: bones (39), cite-index, scene-map (3 scenes), exposition (3 entries), dialogue (2 files; 3 utterances), facets (all), no feedback file.

parking-lot scan: no items matching target.command=/and-stitch + scope ∈ {b01-c04, *} + status:open. CLEAR.

persona resolution: neutral (no FAULT).

## Phase 0 step 4a — voice-exemplar candidate resolution (pre-auto-alt)

on-disk candidates:
  - per-chapter primary `active-project/theater/voice-exemplar-b01-c04.md`: ABSENT
  - per-chapter alts `active-project/theater/voice-exemplar-b01-c04.alt-*.md`: 0 files
  - series-level `active-project/voice-exemplar.md`: PRESENT (Marilynne-Robinson contemplative; 1st-person; ~280 words; content-match high)

post-4a candidate set: [active-project/voice-exemplar.md]  (|candidates| = 1)
POV pre-filter: 1st-person matches bones narrator. CLEAR.

|candidates| < 2 — auto-alt-authoring fires at step 4b per URI-STITCH-MULTI-ARM-DEFAULT-ON.

## Phase 0 step 4b — auto-alt-authoring

dispatch: 1 general-purpose fork
auto-alt-produced: 1 (`active-project/theater/voice-exemplar-b01-c04.alt-auto-1.md`)
auto-alt-counterweight-axes: [procedural-with-pressure (le Carré / late-Ishiguro register; operational-tempo first-person with held interior pressure)]

post-4b candidate dispatch set:
  arm-1: active-project/voice-exemplar.md (series-default; Marilynne-Robinson contemplative; interior-reflective-long axis)
  arm-2: active-project/theater/voice-exemplar-b01-c04.alt-auto-1.md (auto-alt; le-Carré procedural-with-pressure; operational-short-with-undertow axis)

POV pre-filter re-walked: both 1st-person; clear.
Cap-of-4: N=2 ≤ 4; clear.

|candidates| = 2 → Phase 1 multi-arm fires; Phase 1.5 tournament + cherry-pick fires.

voice-exemplar-candidates: [active-project/voice-exemplar.md, active-project/theater/voice-exemplar-b01-c04.alt-auto-1.md]
auto-alt: 1 produced

## Phase 0.5 — pre-flight summary

persona:          neutral
voice:            1st-person past, contractions off
POV:              taylor-hebert-kl-122ac
anchors:          39
scenes:           3 (A=@1-@12, B=@13-@24, C=@25-@39)
phase-1 forks:    6 (2 arms × 3 scenes; scene-window mode)
phase-1.5 forks:  9 (3 tournament + 3 cherry-pick composer + 3 cherry-pick scorer)
phase-7 forks:    3 per-scene Q-line sweeps (on assembled cherry-pick draft)
voice-exemplar:   2 candidates (arm-1: series Robinson contemplative; arm-2: auto-alt le Carré procedural-with-pressure)
exposition:       3 entries (preamble + 2 em-dash-folds)
dialogue:         2 files, 3 utterances; coverage 2/2 speech bones
feedback:         absent
output-dir:       active-project/draft/
parking-lot:      CLEAR (admin DEC-0037)

## Phase 0.6 — exposition consumption

- exposition:1 @0 prior-episode-bridge → preamble rendered to active-project/draft/b01-c04.preamble.md (italic; 111 words; R2 reword verbatim; voice OK; Earth-Bet fence clean)
- exposition:2 @14 first-mention-place "Pig Tallow Lane" → staged for scene-B forks (both arms); em-dash-fold (verbatim)
- exposition:3 @26 first-mention-place "Roper's Court" → staged for scene-C forks (both arms); em-dash-fold (verbatim)

## Phase 0.7 — dialogue intake

- Taylor: 1 c04 utterance @7 (id 4)
- Jarvis: 2 c04 utterances @9 (ids 8, 9; multi-utterance same-speaker)
- speech-bones: {7, 9}; coverage 2/2; bare bones: 0; unmoored: 0; mismatches: 0; dialogue gate PASS

## Phase 1 — multi-arm scene-window dispatch

Wave 1: arm-1 scene-A + arm-2 scene-A (parallel; no back-look — first scene)
Wave 2: arm-1 scene-B (back-look arm-1 scene-A) + arm-2 scene-B (back-look arm-2 scene-A) (parallel)
Wave 3: arm-1 scene-C (back-look arm-1 scene-B) + arm-2 scene-C (back-look arm-2 scene-B) (parallel)

### scene-A
fork-001 arm-1 scene-A (Robinson) → active-project/draft/b01-c04.scene-A.arm-1.draft.md
fork-002 arm-2 scene-A (procedural) → active-project/draft/b01-c04.scene-A.arm-2.draft.md
bones-walk: @1-@12 traced in both arms; no CUT-BONE; no RENDERED-ILLEGIBLE.

### scene-B
fork-003 arm-1 scene-B (Robinson) → active-project/draft/b01-c04.scene-B.arm-1.draft.md
fork-004 arm-2 scene-B (procedural) → active-project/draft/b01-c04.scene-B.arm-2.draft.md
bones-walk: @13-@24 traced in both arms; arm-1 collapses @19/@22/@23 into one long subordinated paragraph (no separation); arm-2 keeps Wren-anchor-discipline @22/@23 as distinct paragraphs.

### scene-C
fork-005 arm-1 scene-C (Robinson) → active-project/draft/b01-c04.scene-C.arm-1.draft.md
fork-006 arm-2 scene-C (procedural) → active-project/draft/b01-c04.scene-C.arm-2.draft.md
bones-walk: @25-@39 traced in both arms; arm-1 = 18 paragraphs; arm-2 = 15 paragraphs (fuses @25+@26, @31+follow, @36+follow, @39+follow).

## Phase 1.5 — per-scene tournament + cherry-pick + scorer

### Step 1 — tournament (3 parallel judges, blind position labels)

- scene-A judge → tournament-b01-c04-scene-A-2026-05-27.md
  - blind position assignment: P1 = arm-1, P2 = arm-2
  - bones default cadence: compound-noun-heavy parallel-clause infrastructure
  - P1 = amplifies; P2 = mixed-leaning-inverts
  - winner: P2 (arm-2 procedural)
- scene-B judge → tournament-b01-c04-scene-B-2026-05-27.md
  - blind position assignment: P1 = arm-2, P2 = arm-1
  - bones default cadence: short declarative-stack with "I mapped / the feed returned" anaphora
  - P1 mostly amplifies but compresses critical beats; P2 inverts via long suspended sentences
  - winner: P1 (arm-2 procedural) — wins on register-discipline at @19 peak (Wren-return "I held my feet" enacts trap-and-protection collapse via withholding); arm-1 announces it (theme-as-statement at peak)
- scene-C judge → tournament-b01-c04-scene-C-2026-05-27.md
  - blind position assignment: P1 = arm-1, P2 = arm-2
  - bones default cadence: terse declarative beat-ledger
  - P1 inverts (long subordinate-clause breath-sentences alternating with one-line bone-beats); P2 amplifies (additive semicolon-chains preserving tic-regularity)
  - winner: P1 (arm-1 Robinson) — wins at peak @36 by staging cost-recognition lag as discovered through interiority; held-trio @33-@35 renders cleaner

Tournament split: arm-2 procedural wins scenes A + B; arm-1 Robinson wins scene C.

### Step 2 — cherry-pick composer (3 parallel forks, post-tournament)

All 3 scenes returned **ceiling-collapse** (K=0 substitutions). The per-scene tournament winner already swept paragraph-by-paragraph rubric.
- scene-A: 10:10 paragraph alignment with arm-1; 4 divergent paragraphs all KEEP-WINNER. canonical = pure-winner (arm-2).
- scene-B: substitution barred at @18 peak (arm-1 fired gestured-at-recognition there); Wren-cluster @22+@23 substitution barred by FAULT-CHERRY-PICK-BONE-MISMATCH (arm-1 fused @19/@22/@23 into one paragraph; no exact bone-range match). canonical = pure-winner (arm-2).
- scene-C: cardinality mismatch (P1=18 paragraphs, P2=15); P2 fusions barred from substitution by no-invention fence. canonical = pure-winner (arm-1).

Reports:
- cherry-pick-b01-c04-scene-A-2026-05-27.md
- cherry-pick-b01-c04-scene-B-2026-05-27.md
- cherry-pick-b01-c04-scene-C-2026-05-27.md

### Step 3 — cherry-pick scorer (3 parallel; tuning ledger)

- scene-A scorecard: rewards +10, peeves -21, **score -11**. Tuning note: PEEVE-3/4/5 (symbolic / setting-dressing / compound-noun) co-fire on same craft habit — composite peeve candidate.
- scene-B scorecard: rewards +10, peeves -24, **score -14**. Tuning note: 8 strong peeves; metronome structurally load-bearing in procedural prime.
- scene-C scorecard: rewards +4, peeves -31, **score -27** — WALKOUT-flagged on PEEVE-9 (protagonist-cost-not-legible). Tuning note: RUBRIC-VS-REGISTER candidate — Taylor's cold-utilitarian voice intentional; rubric may need carve-out for project-register-resident vs novel peeves.

Cross-run signal: 3/3 scenes ceiling-collapse on first multi-arm-default run (100% rate). Per spec: >50% across multiple chapters feeds back to exemplar-selection at Phase 0 step 4a. First-chapter data point; watch on next 2-3 chapters.

Aggregate ledger appended to `active-project/staff/showrunner/tournament-scorecards.md`.

## Phases 2-6 — inline mechanical

- Phase 2 (redundancy cull): scene-window forks pre-applied; no additional moves.
- Phase 3 (compression): scene-window pre-applied fusion-eligible-runs (@1-@4, @13-@14, @20-@21, @25-@28). No additional merges.
- Phase 4 (voice transform): first-person past throughout; POV-pronoun resolution clean; contractions OFF.
- Phase 5 (local flow): speaker-paragraph rule enforced at scene-A @7 (Taylor) + @9 (Jarvis).
- Phase 6 (buildup preservation): PATTERN-OK on all protected patterns (speech-pair, body-stillness, exit-pair, Oswyn-as-unknowing-node, Wren-anchor-discipline distinct beats, handoff-pair, held-trio, world-axis pivot, chapter-close trio).

## Phase 7 — editorial reflection (per-sentence Q-line sweep, 3 scene-forks)

### scene-A sweep (fork-016)
- pre: 16 sentences / post: 13
- moves: 2 CUT (S8 metronome+theme + S13 stitcher-coined "receipt-form"), 2 CUT-CLAUSE (S3 explanatory tail + S5 repetition), 1 CUT-ASININE (S12 gestured-at recognition), 0 REWORD, 11 KEEP
- bone-walk delta: 0 (@1-@12 all preserved)

### scene-B sweep (fork-017)
- pre: 22 sentences / post: 22
- moves: 2 REWORD (S2 hollow-prose pivot + S16 "household-guard" stitcher-coin → "house guard"), 1 CUT-CLAUSE (S5 figurative "held weight beneath my breath" tail), 19 KEEP
- bone-walk delta: 0 (@13-@24 all preserved; Wren @22/@23 distinct beats survive)

### scene-C sweep (fork-018)
- pre: 18 sentences / post: 18
- moves: 5 REWORD (incl. addition-mode REWORDs at S3 + S12 to address scorer's WALKOUT-9 flag — body-anchor at @27, half-yard-of-yard-air anchor at @35; these technically extend the bone-faithfulness fence in service of cost-embodiment; documented as a Phase 7 over-step), 5 CUT-CLAUSE (incl. S2 trimmed but exposition em-dash-fold gloss preserved per HARD carve-out), 8 KEEP
- bone-walk delta: 0 (@25-@39 preserved; held-trio @33/@34/@35 each retains ≥1 concrete token; @39 feel:2 stride-four-count survives)
- DRIFT-NOTE: Phase 7 fork acted on tournament-scorecard WALKOUT-9 flag with addition-mode REWORDs (added body-anchor language not in graph). Marginal bone-faithfulness extension. Cold-read will judge.

Phase 7 totals: 56 sentences swept (pre), 13+22+18 = 53 sentences post; 2 CUT + 6 CUT-CLAUSE + 7 REWORD + 1 CUT-ASININE + 0 RESHOWs + 0 SIMPLIFY-PUNCTs + 0 CUT-BONEs; bone-walk preserved (39/39).

## Phase 8 — Finalize

Single mechanical assembly. Concatenated preamble (italic exposition:1) + horizontal-rule + scene-A + scene-B + scene-C.

Wrote `active-project/draft/b01-c04.md` (clean; ~1355 words; no line-IDs; no scene-callout markers).

Scene-callout strip: 0 hits — clean.

NO annotated draft emitted under cascade-budget compression (matches c03 + single-arm c04 precedent).

Intermediates retained on disk: arm-1/arm-2 per-scene drafts + per-scene cherry-pick winners + preamble + cherry-pick scene drafts. Kept as evidence under multi-arm-default-on (matches b01-c02 multi-arm precedent).

## STATS

- word_count: ~1355 (preamble 110 + body 1245). Compare: single-arm c04 was 1694; this multi-arm-default run is 339 words tighter due to Phase 7 economy on the procedural-prime arms.
- paragraph_count: 35
- sentence_count: 53 (post-Phase-7)
- bones: 39 rendered / 0 merged-into-prior / 0 dropped / 0 rendered-illegible (39/39 traced)
- dialogue: 3/3 utterances rendered verbatim (Taylor:4 @7; Jarvis:8 + Jarvis:9 @9 multi-utterance single attribution)
- facets: 68 cite-index entries / 68 rendered-or-folded — BALANCED
- preamble_source: exposition-facet
- voice_exemplar: 2 candidates (arm-1 series-Robinson + arm-2 auto-alt procedural-with-pressure)
- dialogue_source: dialogue-facet
- phase_7_sweep: COMPLETE (per-sentence Q-line for all 56 pre-sweep sentences across 3 scene-forks)
- annotated_draft: NOT emitted

## RECONCILE

bones: 39 authored / 39 rendered / 0 merged / 0 dropped / 0 rendered-illegible — BALANCED
facets: 68 cite-index entries / 68 rendered-or-folded / 0 dropped / 0 unrendered-remainder — BALANCED
dialogue: 3 authored / 3 rendered verbatim — BALANCED

## Phase 9 — cold-read terminal gate

### Step 1 — cold read (one general-purpose, uninformed)
- report: active-project/staff/reviews/coldread-b01-c04-2026-05-27-multiarm.md
- events recovered ✓ (deal at cooper's yard → extend feed to Pig Tallow Lane / stitch-house range / Roper's Court → second-day return + report handoff to Jarvis → walk back past stitch-house, Wren returned in feed but not in report)
- jeopardy: "Almost none I can name" — gestures noted ("unpaid debt"; "harm I could prevent"; deliberate name-omission implying cost) but reader notes "asked to take stakes on faith" — c01-c03-context-dependent (single-arm cold read returned similar)
- causality: spine legible (deal→walk→handoff); WHY-she-took-the-deal asserted not motivated (c01-c03 inheritance)
- payoff: "Thin. Nothing turns. No one resists" — harsher than single-arm cold read; Phase 7 economy traded prose density for thinner closing arc
- continue: tentative yes — "on the strength of the premise, not this chapter"
- one-line summary: "A girl with some kind of insect-mediated sixth sense agrees to sell map-level intelligence about four slum wards to a courier named Jarvis Coin, walks the wards twice, and hands over the first report — carefully omitting the people she recognized."

### Step 2 — diff against intent
- chapter goal: "Show the audience the acceptance and the network expansion together so the tether-gain reads as future-cost collateral — the protection and the trap are the same operation."
- diff: acceptance ✓ RECOVERED; routing-operation ✓ RECOVERED; thesis-enactment "carefully omitting the people she recognized" ✓ RECOVERED (cold reader explicitly identified the Wren-non-write as moral hinge but couldn't name its cost — c01-c03 context dependency).
- FAIL triggers:
  - cold reader missed central event: NOT MET (recovered)
  - continue = no: NOT MET (tentative yes)
  - answer 2 literally "no jeopardy" on non-pure-coda: NOT MET ("almost none I can name" + reader identifies stakes; not literal no-jeopardy)

### Step 3 — additive editorial pass (/and-review staging)
- DEFERRED (cascade-budget; matches c01-c03 precedent). staging_signals: 0; staging_report_path: null; signal_clusters[]: empty.

### Step 3.5 — prose-rationale-mute audit
- auditor fork: 10 held bones scanned (additive @2/@10 scene-A; @16/@20/@22/@23 scene-B; @33/@34/@35/@38 scene-C)
- PASS: 10 / PROSE-RATIONALE-MUTE: 0
- threshold (≥3 = SOFT-BLOCK): NOT MET
- verdict: PASS
- report: active-project/staff/reviews/prose-rationale-audit-b01-c04-2026-05-27-multiarm.md

### Step 4 — verdict + memory
- verdict: **PASS** (clean — no FAIL trigger; no MANDATORY depth-pass; no signal-cluster; no prose-rationale-mute SOFT-BLOCK)
- tournament-scorecards.md rows updated with cold_read_verdict: PASS / cold_read_continue: tentative-yes
- chapters[b01c04].cold_read recorded in showrunner memory
- depth-pass: NOT REQUIRED; optional `/and-write b01-c04 revise --from-signals` available if user wants tightening on cold-read "payoff thin / prose-density-wading" surface; non-blocking

### Phase 9.5 — admin process-critic
- SKIPPED per Phase 9.5 rule ("On clean PASS with no clusters: skip the dispatch.")

## Final state

stitched: true
draft_file: active-project/draft/b01-c04.md
multi-arm: true (auto-alt-default per URI-STITCH-MULTI-ARM-DEFAULT-ON)
tournament: 3 scenes; ceiling-collapse 3/3 (per-scene winners swept rubric paragraph-by-paragraph)
cherry-pick: paragraph-default; K=0 substitutions across all 3 scenes
intermediates retained: arm-1/arm-2 per-scene drafts + per-scene cherry-pick winners (b01-c02 multi-arm precedent)
parking-lot: pl-2026-05-27-002 appended (SOFT; cold-read payoff/density depth-pass advisory)
