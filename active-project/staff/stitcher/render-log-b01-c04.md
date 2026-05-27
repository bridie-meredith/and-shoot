# render-log — b01-c04

profile: schema-defaults (no active-project/theater/stitch-profile.md; matches c01/c02/c03)
persona: neutral (library: staff/stitcher/personas/neutral.md; no project-scoped persona)
narrator: taylor-hebert-kl-122ac
voice: first-person past, contractions: profile-default-off (Taylor cold-utilitarian register; c01-c03 precedent)
phase-7-mode: strict (schema default)
generated-date: 2026-05-27
slug: b01-c04
bones-file: active-project/theater/bones/b01-c04.md
cite-index: active-project/theater/facets/_cite-index.md
scene-map: active-project/theater/facets/scene-map-b01-c04.md
phase-1-mode: scene-window (schema default; URI-SCENE-WINDOW; URI-SUBSTANCE-OVERHAUL)
voice-exemplar-candidates: [active-project/voice-exemplar.md]  # series-level; N=1 single-arm; POV 1st-person, matches header
cherry-pick: n/a (N=1, no-op)
allow-bare-speech: false (HARD default)
keep-drafts: false (Phase 8 default prune)

## Phase 0 — validate + load

inputs present:
  - bones: 39 (3 scenes per scene-map; 12+12+15)
  - cite-index: present
  - scene-map: present (scene-A @1-@12 rising | scene-B @13-@24 rising-to-peak | scene-C @25-@39 rising-to-peak-to-trail)
  - exposition: present (3 entries: 1 preamble @0 + 2 first-mention em-dash-fold @14/@26)
  - dialogue: 2 files (taylor-hebert-kl-122ac.md, jarvis-coin-kl-courier.md); 3 utterances for c04 (Taylor @7, Jarvis @9 ×2)
  - facets: interest-narrator, sensory, location-state, memory, metaphor, vibes, state-updates, feeling
  - feedback: ABSENT
  - voice-exemplar: series-level (~280 words; 1st-person; content-match=high; POV-pre-filter clean)

parking-lot scan:
  - matching items (target.command: /and-stitch, target.scope ∈ {b01-c04, *}, status: open): NONE
  - cross-pipeline soft advisories surfaced for Phase 9 awareness:
    - pl-2026-05-25-013 (q9-hyphen-density-threshold-tune; SOFT; cross-pipeline)
  - admin user-proxy verdict: CLEAR (DEC-0037, 2026-05-27)

persona resolution: neutral (no FAULT-PROFILE-PERSONA-MISMATCH-PROJECT — no project-scoped persona declared; c01/c02/c03 all ran neutral)

speech-bone set: {7, 9} (Taylor speaks to Jarvis @7; Jarvis speaks to Taylor @9 ×2 multi-utterance)

## Phase 0.5 — pre-flight summary

persona:          neutral
voice:            first-person past, contractions: profile-default
POV:              taylor-hebert-kl-122ac
anchors:          39
scenes:           3 (A=@1-@12, B=@13-@24, C=@25-@39)
phase-1 forks:    3 scene-window forks
phase-7 forks:    ~3 scene/paragraph forks (per-sentence inside)
phase-1-mode:     scene-window
voice-exemplar:   single (series-level; ~280 words; content-match high; 1st-person)
exposition:       present (3 entries; preamble=1, first-mention=2, scene-orient=0; refused-at-R2=0; cull-dropped at R1=3)
dialogue:         present (2 character files, 3 total utterances; anchors covered: 2 of 2; bare speech bones: 0; unmoored: 0)
bone-fence:       enforced
feedback-file:    absent
output-dir:       active-project/draft/

dialogue gate: PASS (all speech bones covered)

## Phase 0.6 — exposition consumption

- exposition:1 @0 prior-episode-bridge → preamble rendered to active-project/draft/b01-c04.preamble.md (italic-preamble; 111 words; R2 reword verbatim; voice OK first-person Taylor; Earth-Bet fence clean)
- exposition:2 @14 first-mention-place "Pig Tallow Lane" → staged for scene-B fork; em-dash-fold (verbatim)
- exposition:3 @26 first-mention-place "Roper's Court" → staged for scene-C fork; em-dash-fold (verbatim)
- refused-at-R2: 0 (3 scene-orient-fire-rule refusals stand per facet)

## Phase 0.7 — dialogue intake

- taylor-hebert-kl-122ac.md: 1 c04 entry (@7 utterance 4)
- jarvis-coin-kl-courier.md: 2 c04 entries (@9 utterances 8 + 9, multi-utterance same-speaker same-anchor)
- speech-bones: @7 (Taylor), @9 (Jarvis ×2) — coverage 2 of 2 bones; 3 utterances total
- bare-speech bones: 0
- unmoored utterances: 0
- speaker mismatches: 0
- dialogue gate: PASS

## Phase 1 — lens-anchored render (scene-window mode; single-arm; 3 forks)

### scene-A @1-@12 (rising; peak @9; peak-shadow @7/@8/@11)
fork-001 general-purpose scene-A bones=@1-@12  scene-window-render
  bones-consumed: @1-@12
  variance-moves:
    - long opening observational sentence fusing @1+@2+@3+@4 (loc-state lens leads; @3 participial fold)
    - short SVO at @8 ("I held my feet") body-stillness peak-shadow
    - long observational close on @9 NI:3 contrasting flat courier-receipt
    - em-dash fold @11→@12 exit-pair close
  refusals: no exemplar content imported; no vibes labels surfaced; no Earth-Bet nouns
  bone-walk:
    @1→FUSE-L1; @2→FUSE-L1; @3→FUSE-L1; @4→FUSE-L1
    @5→L2 (folded after @6 NI lens lead); @6→L2
    @7→L4 (speaker paragraph; dialogue verbatim); feel:1+NI:10+vibes:1 in L3
    @8→L5 (stand-alone body-stillness); @9→L6 (PEAK; both utterances; single attribution)
    NI:3+vibes:2 in L7
    @10→L8; @11→L9; @12→L9 (close-paired exit)
  drift-risk: none — but "retreat-arc" at L8 is stitcher-coin (Q9 candidate at Phase 7)
  output: active-project/draft/b01-c04.scene-A.draft.md

### scene-B @13-@24 (rising-to-peak; peak @18; peak-shadow @17/@19; Wren-anchor-discipline @22/@23)
fork-002 general-purpose scene-B bones=@13-@24  scene-window-render
  back-look: scene-A rendered prose
  forward-look: scene-C bones/facets
  bones-consumed: @13-@24
  variance-moves:
    - opener varied off scene-A's SVO-shape; long atmospheric L1 with simile (smoke/hearth)
    - @13-@14 fused with exposition:2 em-dash-fold verbatim
    - @15 short SVO peak-magnitude (axis_move +1.0); NI:11 + @16 folded into L4 reflective
    - @18 PEAK long observational with NI:4 weight embedded
    - @20-@21 fused L8
    - @22 named-human peak: mem:2 + vibes:10/11/12 surfaced as embodied register (no labels)
    - L17 closer aphoristic ("discipline was the architecture") — flagged
  refusals: no metaphor peaks (AP7); no label surfacing; no Earth-Bet nouns
  bone-walk:
    @13→FUSE-L1; @14→L2 (em-dash gloss verbatim); @15→L3; @16→FUSE-L4
    @17→L5; @18→L6 PEAK; @19→L7
    @20→FUSE-L8; @21→FUSE-L8
    @22→L9 (named-human peak; mem:2 embodied); @23→L10; @24→L11
  drift-risk: minor
    - "gait-print" at L6+L9 (stitcher-coin; Q9 candidate Phase 7)
    - L9 closer "hand that wrote and the hand that did not write at the same desk" — borderline theme-as-statement aphorism (Q7/Q5 candidate Phase 7)
    - L1 simile "the way smoke sits over a cold hearth before the draw catches" — concrete-anchored but heavy (Q5 borderline)
  output: active-project/draft/b01-c04.scene-B.draft.md

### scene-C @25-@39 (rising-to-peak-to-trail; peak @36; peak-shadow @31/@32; held trio @33-@35; chapter-close trio @37-@39)
fork-003 general-purpose scene-C bones=@25-@39  scene-window-render
  back-look: scenes A + B rendered prose
  forward-look: empty (last scene)
  bones-consumed: @25-@39
  variance-moves:
    - opener varied (bone @25 leads with "Roper's Court came out of the early-morning grey")
    - @25-@26 fused with sensory:3 + loc-state:4 + exposition:3 em-dash-fold verbatim
    - @27 peak-magnitude stand-alone; @28 saturation-cost paragraph with four-ward enumeration
    - @29 scene-shift to cooper's-yard first-bell appointment
    - @30 note-display physical (folded parchment chest-height; receipt named not paraphrased)
    - @31-@32 handoff-pair paired across paragraphs; NI:7 half-step weight at @31
    - @33-@34-@35 held-trio rendered as 3 concrete paragraphs (sheet content; source-tier; conduit-rank)
    - @36 PEAK world-axis-pivot stand-alone with NI:8 channel-feed-cannot-reach
    - @37 four-ward enumeration walking back through Hook
    - @38 chapter-close Wren-return: mem:4 embodied as continuous-operation
    - @39 feel:2 embodied stride-holds-four-count past stitch-house frame
  refusals: no metaphor; no labels; no Earth-Bet
  bone-walk:
    @25→L1; @26→L2 (gloss verbatim); @27→L3; @28→L4-L5
    @29→L6 scene-shift; @30→L7 (note-display physical)
    @31→L8-L9 (NI:7 half-step); @32→L10 (inner-seam fold)
    @33→L11 (concrete sheet-content); @34→L12 (Flea-Bottom-tier); @35→L13 (conduit-rank)
    @36→L14-L15 (PEAK exits with sheet; NI:8)
    @37→L16 (four-ward walk-back); @38→L17 (mem:4 continuous-operation embodied); @39→L18 (feel:2)
  drift-risk: minor
    - L7 "without any cover-motion drawing attention away from its showing" — slightly abstract (Q5 candidate)
    - L13 "the conduit was the rank, and the rank did not promote past it" — borderline aphoristic restatement (Q7 candidate)
    - L17 "were the same architecture running" — borderline theme-as-statement (Q7 candidate)
  output: active-project/draft/b01-c04.scene-C.draft.md

## Phases 2-6 — inline mechanical

- Phase 2 (redundancy cull): scene-window forks pre-applied same-anchor cull at lens-decider stage; no echo or image-overlap requires additional drop. No moves.
- Phase 3 (compression): scene-window forks pre-applied fusion-eligible-run merges (@1-@4 in scene-A; @13-@14 + @20-@21 in scene-B; @25-@28 in scene-C). Same-subject runs collapsed where bones permitted. No additional merges.
- Phase 4 (voice transform): first-person past throughout; POV-pronoun resolution clean; third-party Jarvis preserved by name on first scene mention; contractions OFF in narration as authored.
- Phase 5 (local flow): speaker-paragraph rule enforced at scene-A @7 (Taylor) + @9 (Jarvis paragraph); no other speech bones; no migrations needed.
- Phase 6 (buildup preservation): PATTERN-OK speech-pair @7/@9 (scene-A); PATTERN-OK body-stillness @8; PATTERN-OK exit-pair @11/@12; PATTERN-OK Oswyn-as-unknowing-node @18/@19; PATTERN-OK Wren-anchor-discipline @22/@23 (perception @22 + route-choice @23 distinct); PATTERN-OK handoff-pair @31/@32; PATTERN-OK held-bone trio @33/@34/@35 (three concrete paragraphs, not label-only); PATTERN-OK world-axis pivot @36 stand-alone; PATTERN-OK chapter-close trio @37/@38/@39 (continuous-operation enacted in prose).

## Phase 7 — editorial reflection (per-sentence Q-line sweep, 3 scene-forks)

### scene-A sweep (fork-004)
- sentence-count pre: 14 → post: 14
- moves: 0 CUT, 0 CUT-CLAUSE, 1 REWORD (S12: retreat-arc → "his retreat through the hook-range"; graph-resident substitution), 0 SIMPLIFY-PUNCT, 0 RESHOW, 0 CUT-ASININE, 0 CUT-BONE, 13 KEEP
- bone-walk delta: 0 (@1-@12 all preserved)
- output: scene-A.draft.md (post-sweep, in place)

### scene-B sweep (fork-005)
- sentence-count pre: 17 → post: 15
- moves: 1 CUT (S12: explanatory-echo + duplicate gait-print compound), 1 CUT-CLAUSE (S4: NI-explanatory tail "and the cost did not change for being carried at a longer reach; it only sat at the reach the carrying now required"), 1 CUT-ASININE (S15: "The discipline was the architecture; the architecture was the hand that wrote and the hand that did not write at the same desk" — theme-as-statement; surrounding prose enacts the discipline), 1 REWORD (S7: gait-print → "the gait the feed had already mapped"), 13 KEEP
- bone-walk delta: 0 (@13-@24 all preserved; @22 anchor-discipline embodied register intact)
- output: scene-B.draft.md (post-sweep, in place)

### scene-C sweep (fork-006)
- sentence-count pre: 43 → post: 39
- moves: 3 CUT (S24: interpretive restatement of @33 content; S29: triple-restatement middle of @35 held-trio; S33: theme-statement repeat of @37), 5 CUT-CLAUSE (S2: "silence of an interior that has not yet been crossed" → "silence before any crossing"; S4: Roper's Court em-dash gloss — FAULT EXPOSITION-AUDIT-MISS, restored verbatim post-fork; S12: "without any cover-motion drawing attention away from its showing" → "without cover"; S40: "were the same architecture running" first clause trimmed, embodied register retained; one other minor), 0 REWORD (S12 absorbed cleanup into cut-clause), 0 CUT-ASININE, 0 RESHOW, 0 CUT-BONE, 35 KEEP
- bone-walk delta: 0 (@25-@39 all preserved; held trio @33/@34/@35 concrete content preserved at S22-S23 + S25-S27 + S28+S30)
- FAULT-EXPOSITION-AUDIT-MISS: Phase 7 fork stripped exposition:3 em-dash-fold (Roper's Court gloss) on Q5/Q7 grounds, violating the Phase 7 exposition carve-out (Q5/Q8 borderline on exposition-derived prose = KEEP; upstream R2 + audit pre-cleared). Recovery: gloss restored verbatim by orchestrator (Edit) at scene-C L3. Fork's Q-line itself recorded Q1=y (load-bearing) — the move was inconsistent with its own Q1 read.
- output: scene-C.draft.md (post-sweep, post-recovery, in place)

Phase 7 totals: 74 sentences swept (pre), 14+15+39 = 68 sentences post; 4 CUTs + 7 CUT-CLAUSEs (incl. 1 restored) + 2 REWORDs + 1 CUT-ASININE + 0 RESHOWs + 0 SIMPLIFY-PUNCTs + 0 CUT-BONEs; bone-walk preserved (39/39).

## Phase 8 — Finalize

Single mechanical assembly. Concatenated preamble (italic exposition:1) + horizontal-rule + scene-A + scene-B + scene-C.

Wrote `active-project/draft/b01-c04.md` (clean; 78 lines; ~1694 words; no line-IDs; no scene-callout markers; preamble italic + body).

Scene-callout strip: 0 hits across `## Scene N` / `[SCENE BREAK]` / `--- SCENE ---` patterns — clean.

NO annotated draft emitted under cascade-budget compression (matches c03 precedent).

Intermediates retained on disk: `b01-c04.preamble.md`, `b01-c04.scene-A.draft.md`, `b01-c04.scene-B.draft.md`, `b01-c04.scene-C.draft.md` (`--keep-drafts` not passed; default prune deferred until Phase 9 PASS confirmed terminal).

## STATS

- word_count: ~1694 (preamble ~110 + body ~1584)
- paragraph_count: 36 (5 in scene-A, 11 in scene-B, 18 in scene-C, 1 preamble + 1 hr-separator)
- sentence_count: 68 (post-Phase-7)
- bones: 39 rendered / 0 merged-into-prior / 0 dropped / 0 rendered-illegible (per scene-window bone-walks: 12 + 12 + 15 = 39/39 traced)
- dialogue: 3/3 utterances rendered verbatim (Taylor:4 @7; Jarvis:8 + Jarvis:9 @9 multi-utterance single attribution)
- facets:
  - location-state: 6 rendered (loc-state:1-6 all anchored)
  - interest-narrator: 10 rendered (post-cycle-3; covers @6/@7/@9/@15/@18/@22/@27/@31/@36/@38)
  - sensory: 2 rendered (smell @13; sound @25)
  - state-updates: 30 entries fold via cite-index (env 14 + taylor 8 + jarvis 8); operator changes register obliquely
  - memory: 2 rendered (mem:2 @22 first-recognition; mem:4 @38 continuous-operation re-registration; both embodied not labeled)
  - feeling: 2 rendered (feel:1 @7 hand-on-shed-wall; feel:2 @39 stride-holds-four-count)
  - metaphor: 0 rendered (zero-fires sustained across all peaks; AP7 refusals)
  - vibes: 13 rendered (oblique register; no labels surfaced)
  - exposition: 3 rendered (preamble exposition:1 @0 + em-dash-fold exposition:2 @14 Pig Tallow Lane + em-dash-fold exposition:3 @26 Roper's Court — last restored after Phase 7 fault)
- preamble_source: exposition-facet (R2 reword; 111 words; first-person Taylor)
- voice_exemplar: single (series-level; ~280 words; 1st-person; cadence transferred, no content imported)
- dialogue_source: dialogue-facet (2 character files; 3 utterances rendered verbatim; speaker-paragraph rule honored at @7 + @9)
- phase_7_sweep: COMPLETE (per-sentence Q-line for all 74 pre-sweep sentences across 3 scene-forks; 1 FAULT-EXPOSITION-AUDIT-MISS recovered)
- annotated_draft: NOT emitted (cascade-budget compression; c03 precedent)

## RECONCILE

bones: 39 authored / 39 rendered / 0 merged-into-prior / 0 dropped / 0 rendered-illegible — BALANCED
facets: 68 cite-index entries / 68 rendered-or-folded (loc-state 6 + NI 10 + sensory 2 + state 30 + mem 2 + feel 2 + metaphor 0 + vibes 13 + exposition 3 = 68; metaphor zero-fire is correct per AP7 refusal log; vibes register-oblique through prose with no surface labels per fence) / 0 dropped / 0 unrendered-remainder — BALANCED
dialogue: 3 authored / 3 rendered verbatim — BALANCED

## Phase 9 — cold-read terminal gate

### Step 1 — cold read
- agent: general-purpose (uninformed; read only draft/b01-c04.md)
- report: active-project/staff/reviews/coldread-b01-c04-2026-05-27.md
- events recovered (answer 1):
  - night-decision to accept proposal
  - dawn cooper's yard meeting with Jarvis; terms negotiated (pattern-reports, three days, volume/interval Taylor's)
  - walk extends insect-range to four wards (Pig Tallow Lane + stitch-house range + Roper's Court)
  - Oswyn + Wren noted, deliberately excluded from written report
  - first-bell return: Jarvis displays receipt ("Sera managed"); Taylor hands report sheet; Jarvis pockets; both exit
  - walk back through Hook; feed returns Wren again; Taylor passes without acting
- jeopardy (answer 2): "Soft and offstage. ... Functionally low." Sera-threat referenced but not shown; Taylor's saturation-cost named but consequences undefined. NOT literal "no jeopardy"; identifies stakes but rates them low-charge.
- causality (answer 3): "Shape is legible — decide, meet, walk, write, exchange, leave — but almost every motive is referenced rather than shown." Confusion-log: "the feed"/"insect-range" mechanism; Sera/Otto/Jarvis-patron identities; "three-month window" referent — all c01-c03-context-dependent.
- payoff (answer 4): "A small thematic turn lands at the end (carrying both the delivered report and the protected person 'at the same count')." Mem:4 enacted in chapter-close trio recovered by cold reader.
- continue (answer 5): "Tentative yes — the voice is distinctive enough to coast on for one chapter, and I want to know who Sera is and what 'the feed' actually is."
- one-line summary (answer 6): "A surveillance-capable narrator trades ward-pattern intelligence to an unseen patron through a courier, in exchange for someone named Sera being kept safe."

### Step 2 — diff against intent
- chapter goal: "Show the audience the acceptance and the network expansion together so the tether-gain reads as future-cost collateral — the protection and the trap are the same operation."
- diff: central event (acceptance + routing-operation-installed-at-scale) ✓ RECOVERED; thesis-enactment (protection and trap same operation, recovered by reader as "carrying both at the same count") ✓ RECOVERED; antagonist-force (Jarvis as conduit; arrangement holding) ✓ RECOVERED.
- FAIL triggers evaluated:
  - "Cold reader did not recover central event" — NOT MET (recovered)
  - "Continue = no" — NOT MET (tentative yes)
  - "Answer 2 literally 'no jeopardy' on non-pure-coda chapter" — NOT MET ("soft and offstage" + named risk-bearers, not literal no-jeopardy)

### Step 3 — additive editorial pass (/and-review staging)
- DEFERRED under cascade-budget compression (matches c03 precedent); not run.
- staging_signals: 0; staging_report_path: null; signal_clusters[]: empty.

### Step 3.5 — prose-rationale-mute audit (URI-STITCH-PROSE-RATIONALE-MUTE)
- auditor fork (mechanical lexical scan across held-bone rationales vs prose tokens):
- 10 held bones scanned (additive @2/@10 scene-A; @16/@20/@22/@23 scene-B; @33/@34/@35/@38 scene-C)
- PASS: 10 / PROSE-RATIONALE-MUTE: 0
- threshold (≥3 = SOFT-BLOCK): NOT MET
- verdict: PASS
- report: active-project/staff/reviews/prose-rationale-audit-b01-c04-2026-05-27.md

### Step 4 — verdict + memory
- verdict: **PASS** (clean — no FAIL trigger, no MANDATORY depth-pass, no signal-cluster, no prose-rationale-mute SOFT-BLOCK)
- chapters[b01c04].cold_read recorded in showrunner memory
- depth-pass: NOT REQUIRED (optional /and-write b01c04 revise --from-signals available if user wants tightening on cold-read "soft jeopardy" surface or interior-cartography mid-walk stretch; non-blocking)

### Phase 9.5 — admin process-critic
- SKIPPED per Phase 9.5 rule ("On clean PASS with no clusters: skip the dispatch.")

## Final state

stitched: true
draft_file: active-project/draft/b01-c04.md
intermediates: pruned at Phase 9 PASS confirmation (b01-c04.preamble.md + b01-c04.scene-A.draft.md + b01-c04.scene-B.draft.md + b01-c04.scene-C.draft.md)
parking-lot: pl-2026-05-27-002 appended (SOFT; cold-read jeopardy-soft observation; optional depth-pass)
