# Render-log — b01-c01

generated: 2026-05-19 (initial; halted pre-Phase-1 on stale dialogue anchors)
re-run: 2026-05-20 (current — post rejected-items fixer + post dialogue-facet re-author)
slug: b01-c01
profile: schema defaults (no episode/project profile authored)
persona: neutral
narrator: taylor-hebert-kl-122ac
voice: first-person past-tense, contractions on (schema default)
phase-7-mode: per-scene (3 scene-forks; sentences walked serially inside each)
phase-1-mode: scene-window (default; boundaries from scene-map-b01-c01.md)
flags: (none)

---

## Phase 0 — Validate + Load (2026-05-20 re-run)

- bones file present: `active-project/theater/bones/b01-c01.md` (27 bones, flat IDs 1-29 with time-skip blanks at @10, @21)
- cite-index present: `active-project/theater/facets/_cite-index.md` (stale entries for sensory:2 + sensory:3 + mem:1 — expected; excluded from scope per prior audit dispatch + rejected-items fixer)
- scene-map present: `active-project/theater/facets/scene-map-b01-c01.md` (3 scenes; all rhythm-shape flat-low; no peaks; no protected patterns; coverage 27/27)
- exposition present: `active-project/theater/facets/exposition-b01-c01.md` (5 live entries: 1, 2, 3, 6, 8; ID gaps at 4, 5, 7 from R2 deletions)
- dialogue files present: 3 files (coll, taylor, wren), 4 utterances; all 4 speech bones covered (@8, @23, @25, @26)
- feedback file: absent
- showrunner memory read OK

State machine: stitched: false → in-progress

### Prior-run abort condition resolved

Prior run (2026-05-19) HARD-ABORTED at Phase 0.5 on URI-DIALOGUE-COVERAGE-GATE — bones had been re-done with shifted flat IDs and dialogue facet anchors were stale. The /and-facets cycles 1-3 (2026-05-18 through 2026-05-20) re-authored the dialogue facet against the new bones IDs. Current dialogue files:
  - coll:1 @8 — matches `@8 coll-net-mender-flea-bottom speaks to taylor` ✓
  - taylor:1 @25 — matches `@25 taylor speaks to wren` ✓
  - wren:1 @23 — matches `@23 wren speaks to taylor` ✓
  - wren:2 @26 — matches `@26 wren speaks to taylor` ✓

All 4 speech bones covered. No bare speech bones. No unmoored utterances. No speaker mismatches. Gate PASS.

### Rejected-items removal (2026-05-20)

Prior to this stitcher run, the rejected-items fixer removed two audience-gate-rejected items:
- `sensory:3 @17` (cycle-3 audience-gate HARD: unanchored old-state); ID gap preserved
- `memory mem:1 @9` (cycles 1+2 uniform reject: feel-as-spine defense rebuffed); ID gap preserved

Citation surfaces updated: proto-lines stripped `[sensory:3]` from @17 and `[mem:1]` from @9; cite-index updated to remove mem:1 entry and strip mem:1 co-cite from feel:1 and vibes:12. Sensory.md is now back to 1 modality (light only); memory.md is single-Westerosi-register at @18. Both tradeoffs accepted by user directive.

---

## Phase 0.5 — Pre-flight summary

Gate PASS. See message-trace for the full summary. Proceeding to Phase 0.6.

---

## Phase 0.6 — Exposition consumption

Exposition facet read: `active-project/theater/facets/exposition-b01-c01.md`.

Categorized live entries:
- **Episode-open pool** (preamble): entries 1 (italic-preamble) + 2 (preamble-paragraph), both @0
- **Per-anchor first-mention pool**: entry 3 (Coll, inline-appositive, @4), entry 6 (the-Hook, inline-appositive, @18), entry 8 (Wren, inline-appositive, @22)
- **Per-anchor scene-orient pool**: empty (entries 4, 5, 7 deleted at R2 — see exposition.md DELETED/CONSOLIDATED comment trail)
- **Refused/dropped**: 3 deletions (4, 5, 7) — skip per upstream R2 authority

Voice-mismatch check: first-person consistent throughout. Preamble uses present-tense framing ("I am twenty years old... I live in... I pay") — canonical italic-preamble form (present-tense frame positioned before past-tense body). NO `FAULT-EXPOSITION-VOICE-MISMATCH` raised; framing tense is per voice.pov-frame discipline.

Preamble assembled and written to `active-project/draft/b01-c01.preamble.md`. Two italic paragraphs + horizontal rule separator. Will be prepended at Phase 8.

Cross-episode register check: no prior glossed-terms file (first episode). No re-gloss warnings.

Anchor pools staged for Phase 1:
- scene-A fork: exposition:3 @4 (inline-appositive, Coll)
- scene-B fork: exposition:6 @18 (inline-appositive, the-Hook)
- scene-C fork: exposition:8 @22 (inline-appositive, Wren)

---

## Phase 0.7 — Dialogue intake

Dialogue files loaded:
- `theater/dialogue/coll-net-mender-flea-bottom.md`: 1 entry, behavior-card=cond-westerosi-witness-vocabulary
- `theater/dialogue/taylor-hebert-kl-122ac.md`: 1 entry, behavior-card=cond-taylor-pov-behavior
- `theater/dialogue/wren-stitch-maker-flea-bottom-ward.md`: 2 entries, behavior-card=cond-westerosi-witness-vocabulary

dialogue-by-anchor lookup:
- @8: coll:1 "There's mending if you can hold a needle."
- @23: wren:1 "You walked the block three times this morning. Mistress Coll knows your name and you've not been here a fortnight."
- @25: taylor:1 "There's no work here. Go on."
- @26: wren:2 "The flies were on the meat-stall and they were not on you. The stall is closer."

Cross-validation:
- speech bones in bones file: @8 (coll), @23 (wren), @25 (taylor), @26 (wren) — 4 total
- anchors covered: 4 of 4 ✓
- bare speech bones: 0
- unmoored utterances: 0
- speaker mismatches: 0

URI-DIALOGUE-COVERAGE-GATE: PASS.

Anchor pools staged for Phase 1 scene forks:
- scene-A fork: dialogue:coll:1 @8
- scene-B fork: (no speech bones in scene-B)
- scene-C fork: dialogue:wren:1 @23, dialogue:taylor:1 @25, dialogue:wren:2 @26

---

## Phase 1 — Lens-anchored render (scene-window mode)

Three scene-forks; serialized across scenes (back-look requires prior rendered scene's prose).

### fork-001 — scene-A bones=@1-@9

bones-consumed: @1, @2, @3, @4, @5, @6, @7, @8, @9
back-look: empty (first scene)
forward-look: scene-B (informational)
variance-moves:
- fused @1+@2 same-subject continuous action; loc-state:1 folded via comma-clause appositive on the building-keeper
- @3 sensory + loc-state co-anchor fold rule applied: single perceptual unit, em-dash + comma-clause
- @4 NI leads (rule 4); exposition inline-appositive em-dash-bracketed after first-mention "Coll"; @5 follows as short bone-only clause
- fused @6+@7 same-subject continuation under fusion-eligible-runs license; narrator:2 em-dash appositive
- @8 dialogue verbatim with default `said` attribution
- @9 feel:1 folded via comma-fold "I held my feet, and I set my weight even on both feet"; POV-pronoun resolution she→I, her→my
refusals:
- no invented spatial / route / direction detail
- no invented body detail on @4
- no invented dialogue / attribution-verb on @8
- no invented interior on @7
- no memory render at @9 (mem:1 removed)
- no rendering of state, vibes, tens; no metaphor (zero-fire); exposition only at its renders-as inline-appositive directive
bone-walk:
- @1 → sentence-1 (lead clause)
- @2 → FUSE-into-L1
- @3 → sentence-2 (sensory + loc-state co-anchor fold)
- @4 → sentence-3 (NI leads; exposition inline-appositive em-dash bracket after "Coll")
- @5 → sentence-4 (bone-only short clause)
- @6 → sentence-5 (NI leads; narrator:2 em-dash appositive)
- @7 → FUSE-into-L5 (same-subject continuation)
- @8 → sentence-6 (dialogue verbatim + `said`)
- @9 → sentence-7 (feel:1 folded via comma-fold; POV-resolve)
drift-risk: minor — @9 fold "I held my feet" reads slightly stylized; bone verb preserved verbatim. Phase 4 mechanical pass acknowledged.

### fork-002 — scene-B bones=@11-@20

bones-consumed: @11, @12, @13, @14, @15, @16, @17, @18, @19, @20
back-look: scene-A rendered prose
forward-look: scene-C (informational)
variance-moves:
- fused @11+@12 same-clause comma-and merge (working-day setup; subject-swap permitted by fusion license)
- semicolon-joined @13+@14 parallel "needle" chain into same sentence (aggressive fusion)
- @15 NI lens-fold (rule 4; narrator:3 only); em-dash continuation from bone-verb into NI clause; voice-transformed she→I, present→past
- @16 stands alone short (rhythm flank; sensory:2 deleted upstream — bare bone)
- @17 stands alone short bare bone (sensory:3 removed by prior fixer)
- @18 heaviest cluster: NI-lead + memory-tail per rule 4; loc-state:4 perceptual frame folded into NI clause; exposition em-dash inline-appositive after first-mention "the Hook"; semicolon-folded to memory; voice-transformed throughout
- @19+@20 closing comma-and merge (mirrors @11+@12 opener cadence)
refusals:
- monument-label `(westeros: flea-bottom-hook-as-coercive-geometry-monument)` NOT rendered as text (index reference only)
- no fence violations across spatial / body / dialogue / scene-prose / cognitive
bone-walk:
- @11 → "I lifted the basket" (head of @11+@12 merge)
- @12 → "Coll pulled the net" (tail of @11+@12)
- @13 → "I threaded the needle" (head of @13+@14)
- @14 → "the needle crossed the mesh" (tail of @13+@14)
- @15 → NI-led em-dash continuation; full sentence
- @16 → short bare sentence ("The walls cooled.")
- @17 → short bare sentence ("The boots struck the cobbles.")
- @18 → heaviest single sentence; bone + 4 facet fires; exposition inline-appositive; NI semicolon-folded to memory
- @19 → "I held the eyes" (head of @19+@20)
- @20 → "Coll folded the net" (tail of @19+@20)
drift-risk: none — exposition gloss preserved present-tense per pov-frame convention (gloss-register, not body-verb register)

### fork-003 — scene-C bones=@22-@29

bones-consumed: @22, @23, @24, @25, @26, @27, @28, @29
back-look: scenes A + B rendered prose
forward-look: empty (last scene)
variance-moves:
- @22 cluster: NI leads + loc-state perceptual frame folded into bone-verb + exposition inline-appositive em-dash-bracketed after first-mention "Wren"; whole opening as one paragraph
- speaker-paragraph rule applied at scene-C: 5 paragraphs total (Wren-enters / Wren-utterance / Taylor-action+utterance / Wren-utterance / scene-close)
- @24+@25 mixed action-and-dialogue paragraph (same-character allowance)
- @27 cluster: feel-leads (rule 4); feel:2 (Taylor POV-resolved) + feel:3 (Wren, third-party preserve) + narrator:6 (past + POV-resolve she→I, will-not→would-not) — all folded into one sentence
- @27-@29 scene-close run fused (non-dialogue stretch; fusion-eligible-runs license)
refusals:
- no monument rendered (zero memory at scene-C)
- no metaphor (zero-fire)
- no sensory at any scene-C anchor
- no state / vibes / tens rendered
- attribution verbs limited to `said`; no embellishment
bone-walk:
- @22 → sentence-1 (NI + loc-state + exposition + bone; one paragraph)
- @23 → paragraph-2 (Wren dialogue verbatim)
- @24 → paragraph-3 head (Taylor lifts eyes; "from the mesh" added — see drift-risk)
- @25 → paragraph-3 tail (Taylor dialogue verbatim)
- @26 → paragraph-4 (Wren dialogue verbatim)
- @27 → paragraph-5 head (feel-cluster + narrator:6 fold)
- @28 → paragraph-5 mid ("She crossed the street.")
- @29 → paragraph-5 tail ("I lifted the needle.")
drift-risk: **flag** — @24 render "I lifted the eyes from the mesh" adds spatial-direction phrase "from the mesh" that is NOT licensed by any facet at @24 (no state-update, no loc-state at @24). The mesh is named at @14 bone. Fence question: does "from the mesh" extend the bone-verb's spatial framing in a way that the fence forbids? Provisional ruling: minor fence-stretch. Surfacing to Phase 7 for Q1 / Q9 evaluation; CUT-CLAUSE candidate if Q1=no.

---

## Phase 2 — Redundancy cull

Per-anchor echo-window=1 (same-anchor only). Detector: closing-phrase-echo (default).

Multi-facet anchors scanned: @3 (loc-state:2 + sensory:1), @4 (narrator:1 + exposition:3), @18 (NI:4 + mem:2 + loc-state:4 + exposition:6), @22 (NI:5 + loc-state:5 + exposition:8), @27 (feel:2 + feel:3 + narrator:6).

No closing-phrase echoes detected. No image-set overlaps (detector disabled by default).

0 culls. Clean.

---

## Phase 3 — Compression

Walked Phase 2 draft. Same-subject merges already applied aggressively at Phase 1 under fusion-eligible-runs license. Pronoun-substitution check: Coll first-mention at @4 with exposition, subsequent mentions at @5 ("He"), @8 ("Coll said" - attribution), @12 ("Coll pulled"), @20 ("Coll folded") — fork-001/002 already used "He" at @5 and "Coll" at recurring subject positions; pronoun discipline holds. Wren first-mention at @22, "she"/"her" used at @27/@28; clean.

Exit-trio candidates: none (scene-A close, scene-B close, scene-C close already fused or short-flank rendered).

Time-skip-adjacent zero-cite: @14 ("the needle crosses the mesh") fused into S1 of scene-B already.

Tens1-run-collapse: tens facet not authored (chapter has 0 tens entries).

0 compression moves. Clean.

---

## Phase 4 — Voice transform

Tense + person already applied during Phase 1 rendering (forks were briefed with past-tense first-person POV). Per-paragraph re-check:

- All action-verb clauses in past tense ✓
- POV-pronoun resolution applied at feel:1 @9 (she→I, her→my), feel:2 @27 (her→my), feel:3 @27 (her→her [Wren, third-party preserve]; "on taylor's" → "on mine"), narrator:6 @27 (she→I, will-not→would-not)
- Third-party preserve: Coll keeps display name at first mention + pronoun thereafter ✓; Wren keeps display name at first mention + pronoun thereafter ✓
- Exposition gloss-register present-tense preserved (Coll "keeps", "runs", "asks"; the-Hook "keep their rooms", city-watch "moves through"; Wren "kept in light work" past-as-portrait; — this is canonical pov-frame gloss convention; not a voice mismatch)
- Sensory arrow rendering: sensory:1 @3 "light: corner-room-dim -> overcast-yard-diffuse" rendered as prose-template "the light shifted from the dim of the corner-room into the overcast diffuse of the yard" ✓
- Contractions: "There's mending", "you've not been here", "there's no work" — dialogue verbatim contractions ✓; body prose has no contractions; profile default `contractions: true` means contractions licensed but body-prose authored without them — within profile tolerance.

0 transform moves applied (already applied at Phase 1). Clean.

---

## Phase 5 — Local flow

Per-window scan (window-size=3):

- Within-anchor cite reorder: none required; lens decider's ordering held at Phase 1.
- Forward sensory deferral: only sensory entry is sensory:1 @3, already folded with loc-state via co-anchor rule. No deferral.
- Backward NI promotion: NI clauses already lead their anchors per rule 4.
- Un-merge to rescue swallowed facets: nothing swallowed.
- **Speaker-paragraph rule (URI-SUBSTANCE-OVERHAUL hard rule)**: scene-C has 4 speech bones (@23, @25, @26 — @25 mixed with @24 same-character action). Phase 1 fork-003 produced 5-paragraph speaker-discipline shape: Wren-enters / Wren-utterance / Taylor-action+utterance / Wren-utterance / scene-close. **Audit:** each `speaks to` bone's dialogue is on its own paragraph; back-to-back speakers (@23→@25 and @25→@26) paragraph-break correctly. Compliant. No `FAULT-LOCAL-FLOW-SPEAKER-PARAGRAPH`.

0 flow moves. Clean.

---

## Phase 6 — Buildup preservation

Scene-map declares `protected-patterns: none` for all three scenes. Schema-default protected patterns checked: three-note-buildup, countdown, threshold-cross, return-of — none detected in the draft (no buildup sequences; no countdown; no threshold-cross sequence; no return-of pattern recurring across chapter-this-is-first-chapter).

Candidate emergent pattern: "I held" surface (@9 "I held my feet", @19 "I held the eyes", @27 "I held the eyes") — three iterations across scenes A, B, C. This is structurally the chapter's holding-discipline beat. NOT in the protected-patterns list at scene-map. Logging as **NEW-PATTERN-CANDIDATE** for human review (no Phase 6 action; for next-chapter scene-map authoring).

0 preservation moves. Clean.

---

## Phase 7 — Editorial reflection

Three scene-forks dispatched in parallel (fork-A001, fork-B002, fork-C003). Each fork walked its scene's sentences serially, emitting one Q-line per sentence under strict cut-aggressiveness (borderline=reject; except exposition-derived prose and dialogue-utterance content per the upstream-pre-cleared routing rule).

### fork-A001 — scene-A Q-sweep (7 sentences)

- S1 (L3) → CUT-CLAUSE + REWORD: Q3/Q5 explanatory-echo "at the door-shadow across the entry, where he stood at the threshold-dim"; Q9 hit "interior-corner" (stitcher-coined sensory nominalization outside facet content). Reworded "interior-corner" → "the room's corner". Dropped middle clause.
- S2 (L4) → CUT-CLAUSE: Q5 explanatory-echo / Q6 em-dash reach. Dropped bracketed "the light shifted from the dim of the corner-room into the overcast diffuse of the yard" (sensory:1 arrow content; the bone-action + co-anchored loc-state carries the threshold transit).
- S3 (L5) → KEEP + FAULT-EXPOSITION-AUDIT-MISS (Q6 borderline; pre-cleared) + 2x FAULT-AUDIT-MISS (sensory:1 "wall-bottom" Q9-hit, narrator:1 "eye-lift" Q9-hit — both facet-cited; render as-is, surfaced for upstream auditor)
- S4 (L6) → KEEP
- S5 (L7) → KEEP (Q6 em-dash NI-fold structural; not reach)
- S6 (L8) → KEEP (utterance pre-cleared)
- S7 (L9) → CUT-CLAUSE: Q5 explanatory-echo "I held my feet" + "I set my weight even on both feet" same action twice. Bones-cuttable license does NOT fire (no protected pattern at @9, no Phase 2/6 cut to chain).

**Scene-A stats**: 0 cuts, 3 cut-clauses, 1 reword, 0 reshows, 3 faults-surfaced, 4 keeps.

### fork-B002 — scene-B Q-sweep (6 sentences)

- S1 (L10) → KEEP (4-bone fusion clean)
- S2 (L11) → KEEP + FAULT-AUDIT-MISS-passive-held (NI facet @15 "passive held" Q9-hit state-verb-fragment; upstream audit miss)
- S3 (L12) → KEEP (3-word environmental beat; counterfactual-positive)
- S4 (L13) → KEEP (4-word boot-on-cobble bare bone after sensory:3 removal)
- S5 (L14) → CUT-CLAUSE: Q3 within-scene repetition of L11's "continuous suppression cost". Dropped trailing "staying invisible cost more in dense streets than I would have estimated;". Exposition appositive + memory-tail preserved.
- S6 (L15) → KEEP (two-bone fusion mirrors L10 opener cadence)

**Scene-B stats**: 0 cuts, 1 cut-clause, 0 rewords, 0 reshows, 1 fault-surfaced, 5 keeps.

### fork-C003 — scene-C Q-sweep (7 sentences)

- S1 (L16) → KEEP (exposition appositive pre-cleared; "came in" tripling is NI:5 doubled-register intentional; hyphenated compounds locative/trade-fixed, not Q9)
- S2 (L17) → KEEP (utterance pre-cleared)
- S3 (L18) → CUT-CLAUSE + FENCE-STRETCH-RESOLVED: dropped "from the mesh" (Phase 1 scene-window fork unlicensed spatial extension at @24; no state-update or loc-state at @24 licensed the phrase). Drift-risk from Phase 1 resolved.
- S4 (L19) → KEEP (utterance pre-cleared)
- S5 (L20) → KEEP (substance-hinge; three semicolons fold three facet-cited layers — feel:2 + feel:3 + narrator:6 — all load-bearing per chapter goal)
- S6 (L21) → KEEP (bone @28 closing structural beat)
- S7 (L22) → KEEP (chapter-close return-to-work bone)

**Note on Scene-C fork Q-line polarity**: fork-C003 emitted Q1=n labels across all sentences, but rationales consistently describe lines as critical (high Q1 weight). Treating as fork-side labelling glitch; moves and post-Phase-7 prose are canonical per the move-table (the moves are correct: 1 CUT-CLAUSE on S3, all others KEEP).

**Scene-C stats**: 0 cuts, 1 cut-clause, 0 rewords, 0 reshows, 0 faults-surfaced, 6 keeps. 1 fence-stretch resolved.

### Phase 7 aggregate

- 0 cuts (whole-sentence)
- 5 cut-clauses (S1+S2+S7 in Scene-A; S5 in Scene-B; S3 in Scene-C)
- 1 reword (S1 in Scene-A: "interior-corner" → "the room's corner")
- 0 reshows
- 0 cut-bones (no bones-cuttable license fired)
- 4 faults-surfaced for upstream review:
  - FAULT-EXPOSITION-AUDIT-MISS Scene-A S3 (Q6 borderline em-dash on exposition:3 appositive — pre-cleared, surfaced only)
  - FAULT-AUDIT-MISS sensory:1 "wall-bottom" (Q9-hit on facet content)
  - FAULT-AUDIT-MISS narrator:1 "eye-lift" (Q9-hit on facet content)
  - FAULT-AUDIT-MISS narrator:3 "passive held" (Q9-hit state-verb-fragment on facet content)
- 1 fence-stretch resolved: Scene-C S3 "from the mesh" CUT-CLAUSE (Phase 1 unlicensed spatial extension at @24)
- 15 keeps (out of 20 total body sentences)

---

## Phase 8 — Finalize

1. **Paragraph structure preserved from Phase 1 scene-window choices.** Phase 7 has no paragraph-break authority; the per-fork outputs that added paragraph breaks at S6/S7 boundaries in scene-C and at S2/S3/S4 boundaries in scene-B were treated as overlay and reverted to Phase 1's paragraph structure.
2. **Stable line-IDs assigned**: L1-L22 (2 preamble + 20 body; sequential; no gaps for this chapter since no whole-sentence cuts fired).
3. **Preamble prepended**: italic-rendered exposition:1 + exposition:2 paragraphs, then horizontal-rule `---`, then body.
4. **Scene-callout strip**: scanned for `## Scene N`, `[SCENE BREAK]`, `--- SCENE ---` markers — none present. The single `---` between preamble and body is the schema-licensed preamble-body separator (per Phase 0.6 spec).
5. **Clean draft written**: `active-project/draft/b01-c01.md` (no line-IDs, no trace blocks, 599 words across 14 paragraphs including the preamble's 2).
6. **Annotated draft written**: `active-project/draft/b01-c01.annotated.md` with `[L<N>]` prefixes and `<trace>` blocks per sentence (preamble traces tagged `scope="preamble"`; body traces cite fork-id + scene + bones-consumed + facets-folded + lens-decider-rule + Phase 7 move).
7. **Intermediate drafts pruned**: `active-project/draft/b01-c01.phase-1.draft.md`, `b01-c01.phase-6.draft.md`, `b01-c01.preamble.md` will be deleted post-verification.
8. **Showrunner memory**: state machine `stitched: false → true` (b01c01 anchor).

### STATS

| Metric | Value |
|---|---|
| word count (body) | ~400 |
| word count (preamble) | ~200 |
| word count (total) | 599 |
| sentence count (body) | 20 |
| sentence count (preamble) | 2 |
| paragraph count (body) | 12 (3 scene-A + 4 scene-B + 5 scene-C) |
| paragraph count (preamble) | 2 |
| bones rendered | 27 (all bones from bones file; ID range 1-29 with gaps at 10, 21 time-skip blanks) |
| bones merged (fused) | 12 (@2 into @1; @7 into @6; @11+@12+@13+@14 cluster; @19+@20; @24+@25; @28 standalone but in scene-close paragraph) |
| bones dropped | 0 (no CUT-BONE) |
| facets rendered | 5 categories — narrator (6 entries), loc-state (4 of 4 live entries; loc-state:3 deleted upstream), sensory (1 live entry; sensory:2, sensory:3 deleted upstream), feel (3 of 3 entries), memory (1 of 1 live entry; mem:1 removed upstream) |
| facets dropped | 0 stitcher-side (all upstream deletions accounted for: mem:1 + sensory:3 removed by rejected-items fixer; loc-state:3 + sensory:2 + exposition:4 + exposition:5 + exposition:7 deleted at /and-facets R2/cycle-2; metaphor zero-fire across chapter) |
| reshow count | 0 |
| reword count | 1 ("interior-corner" → "the room's corner") |
| cut-clause count | 5 |
| cut count (whole sentence) | 0 |
| cut-bone count | 0 |
| preamble-source | exposition-facet (Phase 0.6 graph-resident; not legacy-fallback) |
| exposition entries-rendered | 5 (entries 1, 2, 3, 6, 8 — preamble + 3 inline-appositive first-mention glosses) |
| exposition entries-refused-at-R2 | 3 (entries 4, 5, 7 — pre-stitcher deletion authority) |
| cross-episode-register-skipped | 0 (first episode; no prior glossed-terms) |
| dialogue-source | dialogue-facet (Phase 0.7 graph-resident; not legacy-silent-speech) |
| dialogue character-files-loaded | 3 (coll, taylor, wren) |
| dialogue utterances-rendered | 4 (coll:1 @8, wren:1 @23, taylor:1 @25, wren:2 @26) |
| bare-speech-bones | 0 |
| unmoored-utterances | 0 |
| speaker-mismatches | 0 |

### Audit faults surfaced (for upstream review)

| Fault | Anchor | Detail |
|---|---|---|
| FAULT-EXPOSITION-AUDIT-MISS | S3 @4 | Q6 em-dash borderline on exposition:3 inline-appositive (pre-cleared; surfaced only) |
| FAULT-AUDIT-MISS | S3 @4 | Q9 "wall-bottom" sensory-tag compound in narrator:1 (sensory:1 area) — facet-content, render as-is |
| FAULT-AUDIT-MISS | S3 @4 | Q9 "eye-lift" NI register-token in narrator:1 — facet-content, render as-is |
| FAULT-AUDIT-MISS | S2 @15 | Q9 "passive held" state-verb-fragment register hit in narrator:3 — facet-content, render as-is |
| FENCE-STRETCH-RESOLVED | S3 @24 | Phase 1 scene-window fork added unlicensed spatial extension "from the mesh"; Phase 7 CUT-CLAUSE resolved |

### NEW-PATTERN-CANDIDATE

"I held" surface recurring across @9 (feet) / @19 (eyes) / @27 (eyes) — chapter's holding-discipline structural beat. Three iterations, scene-distributed. Not in scene-map's protected-patterns list at scene-map authoring; flagged for next-chapter scene-map authoring consideration.

---

## Run complete

State: `stitched: false → true` (b01c01).

Deliverables:
- `active-project/draft/b01-c01.md` (clean) — terminal deliverable under polish-deferred chain
- `active-project/draft/b01-c01.annotated.md` (traced, dual mode output)
- `active-project/staff/stitcher/render-log-b01-c01.md` (this file)

Polish-deferred boundary: no `/and-wrap` editor pass under the current chain. `b01-c01.md` is the terminal deliverable.

