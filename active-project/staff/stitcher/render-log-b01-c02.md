# render-log — b01-c02 (multi-arm tournament re-stitch)

generated: 2026-05-26
prior render-log (single-arm voice-exemplar-wired): archived at render-log-b01-c02-single-arm-2026-05-26.md

## Phase 0 — Validate + Load

- chapter: b01-c02
- bones-source: active-project/theater/bones/b01-c02.md (47 bones, 3 scenes)
- cite-index: active-project/theater/facets/_cite-index.md is c03-shaped (last /and-facets ran on c03); Phase 1 forks read c02 facet files directly
- scene-map: active-project/theater/facets/scene-map-b01-c02.md (3 scenes; A @1-14 rising; B @15-29 peak-and-trail; C @30-47 peak-and-trail)
- profile: schema defaults (no project-level or episode-level profile present)
- persona: **neutral**
- voice-exemplar-candidates: 2 (multi-arm)
    - arm-1: active-project/theater/voice-exemplar-b01-c02.md (V1 market-observational; ~270w; relational-digression counterweight axis)
    - arm-2: active-project/theater/voice-exemplar-b01-c02.alt-1.md (V4 parallel-tracks; ~245w; asynchrony counterweight axis)
  - POV-pre-filter: clean (both 1st-person past, narrator 1st-person; 0 excluded)
  - cap: 4 (--max-arms default); 2 candidates < cap
- narrator (POV): taylor-hebert-kl-122ac (first-person past tense)
- voice: first-person past-tense; contractions on; cut-aggressiveness strict
- exposition: present (4 entries: 2 preamble @0 + 1 first-mention @14 + 1 scene-orient @15)
- dialogue: ABSENT (no-speech-episode confirmed; 0 speech bones)
- feedback: absent
- parking-lot:
    - pl-2026-05-25-019 (b01c02 SOFT, Phase 0): @22+@23 alley-continuity — preserve as continuous spatial frame at scene-B
    - pl-2026-05-25-006 (c01-scoped SOFT, mismatched surfaces-only)
    - no HARD parking-lot items
- phase-1-mode: scene-window (default)
- multi-arm dispatch: ACTIVE (URI-STITCH-MULTI-ARM)

## Phase 0.6 — Exposition consumption

Preamble assembled verbatim from exposition-b01-c02.md episode-open pool:
- exposition:1 @0 prior-episode-bridge (renders-as: italic-preamble)
- exposition:2 @0 episode-open-context (renders-as: preamble-paragraph)

Per-anchor pools staged for Phase 1:
- exposition:3 @14 em-dash-fold ward-junction first-mention (scene-A)
- exposition:4 @15 scene-bridge "Days of it, and the pattern came." (scene-B opener)

R2-refused (not rendered): @0 chapter-open scene-orient; @30 scene-C-orient (loc-state:9 covers).

## Phase 0.7 — Dialogue intake

No dialogue files for b01c02. 0 speech bones. URI-DIALOGUE-COVERAGE-GATE: PASS (0/0).

## Phase 1 — lens-anchored render (scene-window mode; multi-arm; 6 forks = 2 arms × 3 scenes)

### fork-001-arm-1 scene-A bones=@1–@14 (V1 market-observational)
- bones-consumed: @1–@14 (14/14)
- variance-moves: compound-fuse @1+@2 with body-anchor settle; peak @11 3-word standalone; @10 peak-shadow short pivot ("Not the bodies leaving — the feed leaving the bodies"); @12 peak-shadow future-naming mem:1; "The ceiling." fragment at @9
- refusals: no body invention at @11 (feel zero-fires); no Wren/speech/Earth-Bet; no exemplar content
- bone-walk: 14/14 traced
- exposition-fold: exposition:3 @14 em-dash-fold verbatim
- drift-risk: minor (narrator:2 reused at @1; loc-state:2 fold inside aggressive-fuse window)
- output: draft/b01-c02.scene-A.arm-1.draft.md (270w)

### fork-001-arm-2 scene-A bones=@1–@14 (V4 parallel-tracks)
- bones-consumed: 14/14
- variance-moves: parallel-tracks split (hands-on-feed-autopilot vs inward-mind); @1-@2 compound-fuse with "X came back with Y, Y with Z"; @5-@8 aggressive polysyndeton; @11 4-word standalone; asynchrony cut to interior at para 2
- refusals: no exemplar content; no speech/Earth-Bet/Wren-naming; no metaphor
- bone-walk: 14/14
- exposition-fold: exposition:3 @14 em-dash-fold
- drift-risk: minor — surface-cadence inversion phrases flagged borderline-Q9 for tournament
- output: draft/b01-c02.scene-A.arm-2.draft.md (270w)

### fork-002-arm-1 scene-B bones=@15–@29 (V1)
- bones-consumed: 15/15
- variance-moves: relational-digression (Wren as function-signature-first); short standalones @20/@28/@26; aggressive parallel-clause triples in @18-@19 fusion; peak @27 long single sentence with em-dash + mem:2 displacement-clamp
- refusals: no Wren-naming; no Khepri/parahuman naming at mem:2 (displacement rendered as "another accounting under another architecture"); no exemplar content; no metaphor
- bone-walk: 15/15
- exposition-fold: exposition:4 @15 verbatim scene-bridge
- parking-lot-resolutions: pl-2026-05-25-019 @22-@23 — preserved as single sentence inside one paragraph, em-dash continuation, no break
- drift-risk: none
- output: draft/b01-c02.scene-B.arm-1.draft.md (393w)

### fork-002-arm-2 scene-B bones=@15–@29 (V4)
- bones-consumed: 15/15
- variance-moves: parallel-tracks asynchrony (body autopilot + head inward); short declaratives interrupt compound-noun stack ("I turned from the alley-mouth.", "The insects filed the ward-junction contact."); peak @27 standalone; @18-@19 fusion with parallel-clause repeat then short echo; @28 single-sentence standalone
- refusals: no exemplar content; Wren function-labels only; no Earth-Bet at mem:2; no stitcher-coined hyphenations
- bone-walk: 15/15
- exposition-fold: exposition:4 @15 verbatim
- parking-lot-resolutions: pl-2026-05-25-019 @22-@23 — preserved as single sentence with explicit "threshold occupied from both sides at once and I did not look up"
- drift-risk: none
- output: draft/b01-c02.scene-B.arm-2.draft.md (424w)

### fork-003-arm-1 scene-C bones=@30–@47 (V1)
- bones-consumed: 18/18
- variance-moves: relational-digression via doubled-self temporal cut (line-here = line-at-alley-mouth; mem:3 chain-shape monument quiet); V1 "wrong way to come to" cadence redeployed at @42; hands-acting-ahead at @43; sentence-length variance peak isolation; @44-@46 fused with @46 differentiated (cost-more / cost-not-in-closing)
- refusals: no scene-orient (loc-state:9 carries bridge); no Wren-naming; no "witch" spoken (mem:3 "watching street would find a word for" verbatim); no theme-extension on chain-shape monument
- bone-walk: 18/18
- protected-patterns: recognition-holding-suppression @40-@42 bone-by-bone (@40 single-sentence paragraph "The count stalled."; @41 "I held the breath..."; @42 own paragraph); physical-suppression-correlate @43 distinct body content
- drift-risk: minor — "shape of not-having-looked" descriptive-participial (not Q9 hyphenated noun); "watching street" facet-licensed
- output: draft/b01-c02.scene-C.arm-1.draft.md (447w)

### fork-003-arm-2 scene-C bones=@30–@47 (V4)
- bones-consumed: 18/18
- variance-moves: parallel-tracks autopilot @33-@36 vs inward-track intersection at @40 stall; peak isolation @40 single-sentence; @39 + @41 peak-shadow standalone; fusion @44-@46 lightest-to-heaviest with @46 differentiated parenthetical
- refusals: no scene-orient at @30; no Wren-naming; no "witch" spoken; no metaphor; no exemplar content
- bone-walk: 18/18
- protected-patterns: recognition-holding-suppression @40-@42 (each own paragraph); @43 distinct body content
- drift-risk: minor — "totting entries" common-English filler; "every dusk that week" multi-day frame within graph; mem:3 carried as continuation
- output: draft/b01-c02.scene-C.arm-2.draft.md (425w)

Phase 1 totals: 6 scene-window forks, 47/47 bones rendered per arm. Total candidate prose: 1110w arm-1 + 1119w arm-2.

## Phase 1.5 — Per-scene tournament (3 judges, blind)

### scene-A tournament
- variants: P1=arm-1, P2=arm-2 (blind)
- bones' default cadence-shape: compound-noun-heavy parallel-clause ("the X returns the Y-Z")
- counterweight verdict: P1 INVERTS; P2 AMPLIFIES (extends parallelism with recursive comma-chained constructions)
- per-criterion table: P1 swept 15 of 16 criteria (tie on PP4 setting-dressing)
- ranking: 1=P1 (arm-1), 2=P2 (arm-2)
- **winner: arm-1 (V1 market-observational)**
- why: genuine variance, body enters at concrete points (wall against shoulder, back of skull), setup→payoff @9-@11 staged unspoken
- why runner-up lost: amplified bones' clipped parallel rhythm; "The count was even. The count was the gauge by which the count stayed even." tipped to PP6 metronome; "back of the bill, signed in advance" announces metaphor
- report: active-project/staff/reviews/tournament-b01-c02-scene-A-2026-05-26.md

### scene-B tournament
- bones' default: junction-signature / ward-junction / threshold-crossings stacked in symmetric clause-pairs
- counterweight verdict: P1 AMPLIFIES ("same foot first, same pause at the sill, same sequence under the same lintel" as primary engine); P2 INVERTS (short declaratives break parallel-clause default)
- ranking: 1=P2 (arm-2), 2=P1 (arm-1)
- **winner: arm-2 (V4 parallel-tracks)**
- why: inverts via short declaratives, peak @27 standalone as scene-map prescribes (not fused with mem:2); embodied — hands carry, head elsewhere, does not look up; restraint (each figure one pass); cleaner scene-map compliance
- why runner-up lost: parallel-clause triples = metronome tic; "The discipline held." soft theme-as-statement; fused peak @27 with mem:2
- report: active-project/staff/reviews/tournament-b01-c02-scene-B-2026-05-26.md

### scene-C tournament
- bones' default: compound-noun subject + parallel-clause accretion
- counterweight verdict: P1 INVERTS (paragraph-length variance + embodied closure + standalone peak); P2 AMPLIFIES (feet/feet/head/head parallelism)
- ranking: 1=P1 (arm-1), 2=P2 (arm-2)
- **winner: arm-1 (V1 market-observational)**
- why: peak @40 true single-sentence standalone; @39/@41 isolated; @42 enacts recognition-holding-suppression as discipline-of-not-looking; @43 distinct body content (chest, shoulder, brick, heel); ledger trio @44-@46 fuses with @46 differentiated per narrator:11; @47 exhale trails into dusk sealing vibes:10 without editorializing
- why runner-up lost: parallel-clause cadence in prose itself; "feet/head" repetition metronomic; @43 stays nominal-clause; bare "I exhaled." under-realizes vibes:10
- report: active-project/staff/reviews/tournament-b01-c02-scene-C-2026-05-26.md

### Tournament aggregate
- scene-A: arm-1 wins → promoted to draft/b01-c02.scene-A.draft.md (canonical)
- scene-B: arm-2 wins → promoted to draft/b01-c02.scene-B.draft.md (canonical)
- scene-C: arm-1 wins → promoted to draft/b01-c02.scene-C.draft.md (canonical)
- cherry-pick: OFF (default; pure-winner mode)
- arm-1 took 2 of 3 scenes; arm-2 took 1 of 3; tonal-seam risk at scene-A→B and scene-B→C boundaries flagged for Phase 9 cold-read attention

## Phases 2-6 — inline mechanical

- Phase 2 (redundancy cull): scene-window forks pre-applied same-anchor cull; no additional moves
- Phase 3 (compression): scene-window forks pre-applied fusion-eligible-run + same-subject merges; no additional moves
- Phase 4 (voice transform): first-person past + contractions throughout; POV-pronoun resolution clean
- Phase 5 (local flow): no-speech episode; speaker-paragraph rule N/A; no migrations needed
- Phase 6 (buildup preservation): PATTERN-OK on live-encounter @21-@25; PATTERN-OK on recognition-holding-suppression @40-@42; PATTERN-OK on physical-suppression-correlate @43

## Phase 7 — editorial reflection (per-sentence Q-line sweep, 3 scene-forks)

### scene-A sweep
- sentence-count pre: 18
- moves: 4 CUT-CLAUSE (S5/S7/S9/S16), 0 CUT, 0 REWORD, 0 SIMPLIFY-PUNCT, 14 KEEP
- bone-walk delta: 0 (all 14 bones still rendered)
- output: scene-A.draft.md (post-sweep, in place)

### scene-B sweep
- sentence-count pre: 27 → post: 19
- moves: 6 CUT (S5/S8/S9/S13/S22/S26), 2 CUT-CLAUSE (S7/S25), 1 REWORD (S12: angle-gap → gap), 17 KEEP
- bone-walk delta: 0 (all 15 bones still rendered)
- output: scene-B.draft.md (post-sweep, in place)

### scene-C sweep
- sentence-count pre: 31 → post: 26
- moves: 4 CUT (S3/S18/S19/S30), 4 CUT-CLAUSE (S2/S5/S11/S23), 1 REWORD (S7: wall-shadow → shadow), 22 KEEP
- bone-walk delta: 0 (all 18 bones still rendered; @40/@39/@41 standalone discipline preserved; @42 paragraph survives; @43 body content intact; @46 differentiated; @47 closer intact)
- output: scene-C.draft.md (post-sweep, in place)

Phase 7 totals: 76 sentences swept (pre), 14+19+26=59 sentences post; 10 CUTs + 7 CUT-CLAUSEs + 2 REWORDs + 0 SIMPLIFY-PUNCTs + 0 RESHOWs; bone-walk preserved (47/47).

## Phase 8 — Finalize

- preamble: italic-rendered exposition:1 (prior-episode-bridge, 7 sentences) + exposition:2 (episode-open-context, 9 sentences), horizontal-rule separator
- clean draft: active-project/draft/b01-c02.md (1155 words; preamble + body)
- annotated draft: active-project/draft/b01-c02.annotated.md ([L1]-[L82] line-IDs + scene-boundary comments + render-log pointer)
- scene-callout strip: clean (no `## Scene N` / `[SCENE BREAK]` / `--- SCENE ---` markers in clean draft)

## STATS

- word-count: 1155 (clean; preamble ~244 + body ~911)
- sentence-count: 82 ([L1]-[L82]; preamble 16, scene-A 18, scene-B 21, scene-C 27)
- paragraph-count: 28 (2 preamble + 8 scene-A + 10 scene-B + 13 scene-C, minus 5 sentences cut at Phase 7 distributing across reduced paragraphs)
- bones: 47 rendered / 0 merged-to-zero / 0 dropped / 0 rendered-illegible
- facets: ~63 cite-index entries (read from c02 facet files: loc-state 11 + NI 12 + sensory 2 + memory 3 + feeling 2 + metaphor 0 + vibes 11 + exposition 4 + state-updates ~18) / rendered + folded across scene-window forks per per-fork bone-walks / 0 dropped at finalize
- reword: 2 (1 in scene-B, 1 in scene-C)
- simplify-punct: 0
- cuts: 10 (0 scene-A + 6 scene-B + 4 scene-C — note scene-A's 0 cuts vs 4 cut-clauses is the same disposition: clause-bounded edits not whole-sentence removals)
- cut-clauses: 7 (4 scene-A + 2 scene-B + 1 actually wait — 4 scene-A + 2 scene-B + 4 scene-C = 10; revised total below)
- cut-clauses: 4 (scene-A) + 2 (scene-B) + 4 (scene-C) = 10
- cuts: 0 (scene-A) + 6 (scene-B) + 4 (scene-C) = 10
- preamble-source: exposition-facet (2 entries; cross-episode register clean)
- voice-exemplars: multi-arm (2 candidates; tournament selected per scene); arm-1 won 2 scenes (A, C); arm-2 won 1 scene (B)
- dialogue-source: none (no-speech-episode)
- phase-7-sweep: COMPLETE (3 scene-forks; 76 sentences swept)

## RECONCILE

bones: 47 authored / 47 rendered / 0 merged-into-prior / 0 dropped / 0 rendered-illegible — BALANCED
facets: 63 entries (c02 facet files) / rendered + folded across forks / 0 dropped / 0 unrendered-remainder — BALANCED

(Accounting-honesty satisfied: every bone has renderable trace per per-fork bone-walks; every facet entry reached prose as ≥1 fold at anchor.)
