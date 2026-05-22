# Render-log — b01-c02

generated: 2026-05-22
slug: b01-c02
profile: schema defaults (no episode/project profile authored)
persona: neutral
narrator: taylor-hebert-kl-122ac
voice: first-person past-tense, contractions on (schema default)
phase-7-mode: per-scene (3 scene-forks; sentences walked serially inside each)
phase-1-mode: scene-window (default; boundaries from scene-map-b01-c02.md)
flags: (none)

---

## Phase 0 — Validate + Load

- bones file present: `active-project/theater/bones/b01-c02.md` (27 bones, flat IDs 1-29 with time-skip blanks at @11, @21)
- cite-index present: `active-project/theater/facets/_cite-index.md` (54 facet entries; sensory:2 DELETED upstream cycle-3 — accounted)
- scene-map present: `active-project/theater/facets/scene-map-b01-c02.md` (3 scenes; rhythm-shapes rise-peak-settle / rise-peak-residue / build-verdict-close; coverage 27/27)
- exposition present: `active-project/theater/facets/exposition-b01-c02.md` (3 live entries: 1, 4, 5; ID gaps at 2, 3 from R2 deletions)
- dialogue files present: 2 files (taylor, wren), 3 utterances; both speech bones covered (@19 wren, @20 taylor ×2)
- profile: no episode/project profile — schema defaults resolved
- persona: no project-scoped persona card, no project profile declaring non-neutral → resolved `neutral`. No `FAULT-PROFILE-PERSONA-MISMATCH-PROJECT`.
- POV: `narrator: taylor-hebert-kl-122ac` from bones header
- feedback file: absent
- showrunner memory / and-facets summary read OK (orchestrator-critic verdict: ship)

State machine: stitched: false → in-progress

---

## Phase 0.5 — Pre-flight summary

Gate PASS. persona neutral (no project persona — no mismatch fault). 27 anchors, 3 scenes, scene-window mode. Dialogue gate: 2/2 speech bones covered (@19 wren:1; @20 taylor:1+taylor:2), 0 bare bones, 0 unmoored. Exposition present (3 live entries). Proceeding.

---

## Phase 0.6 — Exposition consumption

Exposition facet read: `active-project/theater/facets/exposition-b01-c02.md`.

Categorized live entries:
- **Episode-open pool** (preamble): entry 1 (prior-episode-bridge, italic-preamble), @0
- **Per-anchor first-mention pool**: entry 4 (pressed-labor-sweep, post-bone-clause, @4), entry 5 (ledger, post-bone-clause, @23)
- **Per-anchor scene-orient pool**: empty (R2 fire-audit REFUSED scene-B and scene-C scene-orient — loc-state carries time/place at both scene-opens)
- **Refused/dropped**: 2 deletions (entries 2 water-carrier, 3 near-witness) — skip per upstream R2 authority

Voice-mismatch check: preamble is first-person; uses present-tense framing for the live-threat clause ("come down the Hook ... theory ends") — canonical italic-preamble convention. NO `FAULT-EXPOSITION-VOICE-MISMATCH`.

Preamble assembled and written to `active-project/draft/b01-c02.preamble.md` (one italic paragraph + horizontal-rule separator). Prepended at Phase 8.

Cross-episode register check: glossed-terms.md carries 8 b01c01 terms (coll, wren, the-Hook, the-Watch, flea-bottom, the-prohibition, etc.) — all reader-resident; no re-gloss in c02. No `WARN-EXPOSITION-REGLOSS`.

Anchor pools staged for Phase 1:
- scene-A fork: exposition:4 @4 (post-bone-clause, pressed-labor-sweep)
- scene-C fork: exposition:5 @23 (post-bone-clause, ledger)

---

## Phase 0.7 — Dialogue intake

Dialogue files loaded:
- `theater/dialogue/taylor-hebert-kl-122ac.md`: 2 entries, behavior-card=taylor-hebert-westeros
- `theater/dialogue/wren-stitch-maker-flea-bottom-ward.md`: 1 entry, behavior-card=westeros-smallfolk

dialogue-by-anchor lookup:
- @19: wren:1 "The flies were round you again. They were round you on Tickler's Lane two days gone, and the lane went quiet after. It goes quiet where you've been. I weren't looking for it. I just saw."
- @20: taylor:1 "The watch came through. They did not stop. That is all it was." + taylor:2 "Go home, Wren. The street is quiet now." (multi-utterance anchor, file order preserved)

Cross-validation:
- speech bones in bones file: @19 (wren), @20 (taylor) — 2 total
- anchors covered: 2 of 2 ✓
- bare speech bones: 0 | unmoored utterances: 0 | speaker mismatches: 0

URI-DIALOGUE-COVERAGE-GATE: PASS.

Anchor pools staged for Phase 1:
- scene-B fork: dialogue:wren:1 @19, dialogue:taylor:1 @20, dialogue:taylor:2 @20

---

## Phase 1 — Lens-anchored render (scene-window mode)

Three scene-forks; serialized across scenes (back-look requires prior rendered scene's prose). Dispatched as Agent forks (impersonator subagent, taylor-POV).

### fork-001 — scene-A bones=@1-@10
back-look: empty (first scene) · forward-look: scene-B
variance-moves: @1-@3 fused per fusion-eligible-run; @3 "lifts the eyes" → "turned my reading outward" (avoid literal eye-lift repetition); verb-register varied across closures (closed/came/passed/faced); @7 fused sensory:1 + loc-state:5 as one perceptual unit; mem:1 rendered Westerosi-register, monument-tag suppressed.
refusals: did not gloss Coll/Wren/Watch/Hook (b01c01-glossed); no invented dialogue/route/interior; @6/@8 not fused despite scene-map @6-@8 fusion listing — peak-shadow precedence honored.
bone-walk: @1→para1 (fused); @2→para1 (loc-state:1); @3→para2 (narrator:1); @4→standalone+loc-state:2+exposition:4 post-bone-clause; @5→standalone PEAK+narrator:2+loc-state:3; @6→standalone+loc-state:4; @7→standalone+sensory:1+loc-state:5; @8→standalone+loc-state:6+narrator:3+mem:1; @9→standalone (protected body-stillness); @10→standalone bone-only.
drift-risk: none

### fork-002 — scene-B bones=@12-@20
back-look: scene-A rendered prose · forward-look: scene-C
variance-moves: @12-@13 fused; @16 "lifts the eyes" → "raised my eyes to meet hers"; @14 "faces the alley-mouth" → "looked toward the alley-mouth"; @16-@17 fused; peak @15 standalone with narrator:4 + feel:2 (partial expression preserved).
refusals: no invented Coll-interior or Wren prior-knowledge beyond facet/dialogue licence; speaker-paragraph rule honored (@19 and @20 each own paragraph).
bone-walk: @12→loc-state:7 fused; @13→fused with @12; @14→standalone+loc-state:8; @15→standalone PEAK+loc-state:9+feel:2+narrator:4; @16→bare bone (varied); @17→loc-state:10; @18→bare bone short; @19→Wren utterance verbatim, own para, "said"; @20→Taylor 2 utterances verbatim, own para, "answered".
drift-risk: none

### fork-003 — scene-C bones=@22-@29
back-look: scenes A+B rendered prose · forward-look: empty (last scene)
variance-moves: @22-@23 fused per fusion license; @28 "My hand stayed... drew back" — fresh register, no holding-verb echo of scene-A "held the feet still"; peaks @25/@28 + peak-shadows @24/@26 standalone.
refusals: mem:2 monument-tag not rendered (Westerosi-register only); @29 left unresolved ("stayed short" — unpriced residue intact); no invented dialogue/route/interior.
bone-walk: @22→para1+loc-state:11; @23→fused with @22+exposition:5 post-bone-clause; @24→standalone peak-shadow; @25→standalone PEAK+narrator:5+mem:2; @26→standalone peak-shadow; @27→bare bone; @28→standalone PEAK+narrator:6+feel:1 (dual-discipline hold); @29→unresolved-residue close.
drift-risk: **flag @28** — fork-003 appended "and certain, too, of the line I would not let the hand cross" to the narrator:6 render. narrator:6 says Taylor is "certain *only* of the not-closing"; the appended clause adds a second certainty, contradicting "only". Surfaced to Phase 7 for Q1/fence evaluation — CUT-CLAUSE candidate.

Phase 1 draft written: `active-project/draft/b01-c02.phase-1.draft.md` (27 bones across 3 scenes; preamble held separate).

---
## Phase 2 — Redundancy cull

Per-anchor echo-window=1. Detector: closing-phrase-echo (default). Multi-facet anchors scanned: @4 (narrator:1+loc-state:2+exposition:4), @5 (narrator:2+loc-state:3), @7 (sensory:1+loc-state:5), @8 (narrator:3+loc-state:6+mem:1), @15 (narrator:4+loc-state:9+feel:2), @25 (narrator:5+mem:2), @28 (narrator:6+feel:1). No closing-phrase echoes; no image-set overlaps. 0 culls. Clean.

---

## Phase 3 — Compression

Same-subject merges applied at Phase 1 under fusion-eligible-runs license (@1-@3, @12-@13, @16-@17, @22-@23). Pronoun discipline: Coll display-name at recurring subject positions (@10, @12), Wren display-name first-mention-in-scene + pronoun thereafter (@6/@15/@19; @15 "she", @20 "Wren" address). Exit-trio candidates: none. Time-skip-adjacent zero-cite: handled by scene-boundary paragraph breaks. Flat-low-run collapse: no zero-cite run outside protected patterns. 0 compression moves. Clean.

---

## Phase 4 — Voice transform

Tense + person applied at Phase 1 (forks briefed past-tense first-person POV). Per-paragraph re-check:
- All action-verb clauses past tense ✓
- POV-pronoun resolution: feel:1 @28 (hand draws back → "My hand"), narrator:6 @28 (she→I); feel:2 @15 Wren third-party preserved ("her eyes", "she")
- Third-party preserve: Coll + Wren keep display name; pronoun thereafter ✓
- Exposition gloss-register: exposition:4 present-tense gloss-frame preserved (canonical pov-frame convention; not a voice mismatch); exposition:5 rendered past ("was the book I kept")
- Sensory arrow: sensory:1 @7 "watch-press-alley-ambient -> watch-column-footfall" rendered prose-template ("Street-noise gave way under the column's footfall") ✓
- Contractions: dialogue verbatim ("weren't"); body prose contraction-free — within profile tolerance
0 transform moves (applied at Phase 1). Clean.

---

## Phase 5 — Local flow

Per-window scan (window-size=3). Within-anchor reorder: none required (lens-decider order held). Forward sensory deferral: only sensory:1 @7, folded with loc-state — no deferral. Backward NI promotion: NI clauses already lead/frame their anchors. Un-merge: nothing swallowed.
**Speaker-paragraph rule (URI-SUBSTANCE-OVERHAUL hard rule):** scene-B speech bones @19 (Wren) and @20 (Taylor). Phase 1 fork-002 rendered each on its own paragraph; back-to-back speakers (@19→@20) paragraph-break correct. Compliant. No `FAULT-LOCAL-FLOW-SPEAKER-PARAGRAPH`.
0 flow moves. Clean.

---

## Phase 6 — Buildup preservation

Scene-map protected-patterns are single-bone standalone-treatment markers (@4, @5, @9 / @15, @19-@20 / @25, @28, @29), not multi-bone buildup sequences. Intactness check:
- @5 (chapter hinge) standalone ✓ · @9 (held-feet body-stillness) standalone ✓ · @4 (threshold-crossing) standalone ✓
- @15 (wren-attachment crystallization) standalone ✓ · @19-@20 (speech exchange) each own paragraph, not collapsed ✓
- @25 (pen-set/strike) standalone ✓ · @28 (dual-discipline hold) standalone ✓ · @29 (unpriced-residue close) unresolved ✓
All PATTERN-OK. No PATTERN-ABANDONED (no protective facet cut at Phase 2).
Schema-default patterns (three-note-buildup, countdown, threshold-cross, return-of): none detected as multi-bone sequences.
**NEW-PATTERN-CANDIDATE**: cross-chapter holding-discipline beat — c01 flagged "I held" at @9/@19/@27; c02 continues it at @9 ("I held the feet still") and @28 ("My hand stayed... then drew back"). Scene-distributed holding/not-reaching motif. Flagged for next-chapter scene-map authoring; no Phase 6 action.
0 preservation moves. Clean.

---
## Phase 7 — Editorial reflection

Three scene-forks dispatched in parallel (editor subagent). Each walked its scene's sentences serially, one Q-line per sentence, strict cut-aggressiveness (borderline=reject; exposition-derived + dialogue-utterance content pre-cleared per routing rule). 45 body sentences swept (scene-A 18, scene-B 11, scene-C 16).

### fork-A001 — scene-A Q-sweep (18 sentences)
- S2 (@2) → REWORD: Q9 "watch-press" coined nominalization → "thickening with Watch"
- S4 (@4) → CUT-CLAUSE + SIMPLIFY-PUNCT: Q3 first clause "the feed had built the lane into a column before my eyes had finished crossing" redundant with S1's feed-column; semicolon dissolved with the cut. narrator:1 body-lag core preserved → "My body was catching up to a thing already filed."
- S10 (@5) → REWORD: Q9 "column-route" coined compound → "the column blocked"
- S1, S3, S5-S9, S11-S18 → KEEP (15 keeps)
- Scene-A stats: 0 cuts, 1 cut-clause, 2 rewords, 1 simplify-punct, 15 keeps

### fork-B002 — scene-B Q-sweep (11 sentences)
- All 11 → KEEP. Peak @15 (S4-S6) clean; S5's three-facet em-dash fold judged structural (loc-state:9 + narrator:4 + feel:2 folded as one simultaneous impression at the pivot — not punctuation reach). Dialogue utterances (S10, S11) pre-cleared; attributions load-bearing, kept.
- Scene-B stats: 0 cuts, 0 cut-clauses, 0 rewords, 0 keeps-with-moves, 11 keeps. Clean sweep, 0 moves (legitimate — post-Phase-6 scene-B was clean).

### fork-C003 — scene-C Q-sweep (16 sentences)
- S14 (@28) → CUT-CLAUSE: FENCE violation confirmed. narrator:6 licenses "certain ONLY of the not-closing"; Phase 1 fork-003 appended "— and certain, too, of the line I would not let the hand cross", a second certainty contradicting the ONLY qualifier. Unlicensed fence-stretch (Phase 1 drift-flag). Trailing span cut → "Tonight I was certain only of the not-closing." Peak @28 strengthened (stark singular restored).
- S1-S13, S15, S16 → KEEP (15 keeps). @29 (S16) unpriced-residue close left unresolved per bone discipline.
- Scene-C stats: 0 cuts, 1 cut-clause, 0 rewords, 15 keeps

### Phase 7 aggregate
- 0 cuts (whole-sentence)
- 2 cut-clauses (scene-A S4 redundant-clause; scene-C S14 fence-stretch)
- 2 rewords (scene-A S2 "watch-press", S10 "column-route")
- 1 simplify-punct (scene-A S4 semicolon, dissolved by clause cut)
- 0 reshows, 0 cut-bones (no bones-cuttable license fired)
- 41 keeps (out of 45 body sentences; 4 sentences carried moves)
- 1 Phase-1 drift-flag resolved: scene-C S14 @28 fence-stretch CUT-CLAUSE
- faults-surfaced: Q9 coined-compound hits at scene-A S2/S10 were stitcher-render artifacts (caught and reworded in-pass, not facet-content faults — no upstream FAULT-AUDIT-MISS)

Phase 7 draft written: `active-project/draft/b01-c02.phase-7.draft.md`.

---
## Phase 8 — Finalize

1. Stable line-IDs assigned: L1-L46 (1 preamble + 45 body; sequential, no gaps — no whole-sentence cuts fired).
2. Paragraph structure preserved from Phase 1 scene-window choices (Phase 7 has no paragraph-break authority; scene-B fork's reproduced-prose attribution-placement variance discarded — Phase 6 scene-B prose stood since the fork returned 0 moves).
3. Preamble prepended: exposition:1 italic paragraph + horizontal-rule `---` separator before the body.
4. Scene-callout strip: scanned clean draft for `## Scene N`, `[SCENE BREAK]`, `--- SCENE ---` — none present. The single `---` is the schema-licensed preamble-body separator. No `FAULT-PHASE-8-SCENE-CALLOUT-LEAK`. Scene boundaries conveyed by paragraph break only.
5. Clean draft written: `active-project/draft/b01-c02.md` (675 words, 23 paragraphs incl. preamble).
6. Annotated draft written: `active-project/draft/b01-c02.annotated.md` (`[L<N>]` prefixes, `<trace>` per line; preamble trace tagged `scope="preamble"`; exposition + dialogue first-class citations in body traces).
7. Intermediate drafts pruned: `b01-c02.phase-1.draft.md`, `b01-c02.phase-6.draft.md`, `b01-c02.phase-7.draft.md`, `b01-c02.preamble.md`.
8. Showrunner memory: `stitched: true` (b01c02 chapter block).

### STATS

| Metric | Value |
|---|---|
| word count (total) | 675 |
| sentence count | 46 (1 preamble + 45 body) |
| paragraph count | 23 (1 preamble + 22 body: 9 scene-A + 6 scene-B + 7 scene-C) |
| bones rendered | 27 (all bones; ID range 1-29 with time-skip blanks at 11, 21) |
| bones merged (fused) | @2 into @1; @13 into @12; @23 into @22 (fusion-eligible-runs) |
| bones dropped | 0 (no CUT-BONE) |
| facets rendered | narrator (6), loc-state (11), sensory (1), feel (2), memory (2), exposition (3) |
| facets dropped | 0 stitcher-side (sensory:2 deleted upstream cycle-3; meta:1 + feel:1-coll deleted upstream R2 — all accounted) |
| reshow count | 0 |
| reword count | 2 ("watch-press" → "thickening with Watch"; "column-route" → "column blocked") |
| cut-clause count | 2 (scene-A S4 redundant clause; scene-C S14 fence-stretch) |
| simplify-punct count | 1 (scene-A S4 semicolon, dissolved by clause cut) |
| cut count (whole sentence) | 0 |
| cut-bone count | 0 |
| preamble-source | exposition-facet (Phase 0.6 graph-resident; not legacy-fallback) |
| exposition entries-rendered | 3 (entries 1, 4, 5 — preamble + 2 post-bone-clause first-mention glosses) |
| exposition entries-refused-at-R2 | 2 (entries 2 water-carrier, 3 near-witness) |
| cross-episode-register-skipped | 8 (b01c01 terms reader-resident — coll, wren, the-Hook, the-Watch, etc.; none re-glossed) |
| dialogue-source | dialogue-facet (Phase 0.7 graph-resident; not legacy-silent-speech) |
| dialogue character-files-loaded | 2 (taylor, wren) |
| dialogue utterances-rendered | 3 (wren:1 @19, taylor:1 + taylor:2 @20) |
| bare-speech-bones | 0 |
| unmoored-utterances | 0 |
| speaker-mismatches | 0 |

### Faults / flags

| Item | Anchor | Detail |
|---|---|---|
| FENCE-STRETCH-RESOLVED | @28 (S14) | Phase 1 fork-003 appended an unlicensed second certainty contradicting narrator:6's "only" qualifier; Phase 7 CUT-CLAUSE resolved. |

No upstream FAULT-AUDIT-MISS surfaced — the two Q9 coined-compound hits ("watch-press", "column-route") were stitcher-render artifacts caught and reworded within Phase 7, not facet-content faults.

### NEW-PATTERN-CANDIDATE

Cross-chapter holding-discipline beat continues: b01c01 flagged "I held" at @9/@19/@27; b01c02 carries it at @9 ("I held the feet still") and @28 ("My hand stayed... then drew back"). The not-reaching / holding-against-extension motif is becoming the series' structural signature for the prohibition. Flagged for next-chapter scene-map authoring; no Phase 6 action.

---

## Run complete

State: `stitched: false → true` (b01c02).

Deliverables:
- `active-project/draft/b01-c02.md` (clean) — terminal deliverable under polish-deferred chain
- `active-project/draft/b01-c02.annotated.md` (traced, dual-mode output)
- `active-project/staff/stitcher/render-log-b01-c02.md` (this file)

Polish-deferred boundary: no `/and-wrap` editor pass under the current chain. `b01-c02.md` is the terminal deliverable.
