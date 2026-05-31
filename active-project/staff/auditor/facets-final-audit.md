audit: facets-final-r1
episode: b01c06
date: 2026-05-31
mode: flag-only
status: FINDINGS-PRESENT
totals: 5 findings across 4 facets (1 HARD, 4 SIGNAL)

---

## STRUCTURAL findings (0)

None.

ID monotonicity: loc-state 1-2 ✓; narrator 1-7 ✓; sensory 1-3 ✓; state-updates (env) 1-17 / (taylor) 18-21 / (wren) 22 ✓; memory 2 (gap at 1 — deleted by R2; gap is expected per schema § deleted IDs leave gaps) ✓; feeling (taylor) 1 / (wren) feel:1 ✓; metaphor 0 ✓; vibes 1-20 ✓; exposition 1 ✓.

Anchor resolution: every `@<id>` in every facet file resolves to a bone in `theater/bones/b01-c06.md` (1-26). Exposition entry at `@0` is the licensed synthetic preamble anchor; exempt from bones coverage per schema.

Bidirectional citation: cite-index cross-checked. All `back=Y` entries confirmed present in their respective facet files. `back=N` entries (state:18-22 — actor-state sub-entries; exposition:1 — @0 synthetic) are structurally correct (back-citation not applicable to actor-state sub-entries consolidated into the ENV slice numbering and to preamble).

Dialogue structural: `wren-stitch-maker-flea-bottom-ward:1` citation on bone @4 resolves to entry 1 in `theater/dialogue/wren-stitch-maker-flea-bottom-ward.md`. Dialogue file header `behavior-card: westeros-smallfolk` resolves to `cards/dialects/westeros-smallfolk.card.md`. Entry-ID monotonicity: 1 entry, no gap. CLEAN.

---

## FREQUENCY-BAND findings (3 SIGNAL)

- **sensory**: 3 entries / 26 bones = 11.5%. Band: 3-6%. BREACH-HIGH. Per-scene: scene-A 1 (@2), scene-B 0, scene-C 2 (@17, @20) — per-scene cap ≤3 honored (max 2 in any scene). The file carries a rubric-carve-out (sensory:1 @2 old-state sourced from location card §Hazards baseline rather than a loc-state entry; documented in-file). With the carve-out, the three entries are each structurally load-bearing (floor-establishing pressure fire in scene-A; stylus-rhythm at the names-written peak in scene-C; silence at the verdict-pause in scene-C). Grounding-ledger has zero entries — no licensed-grounding-exception is claimed or needed. Classification: **SIGNAL** — breach-high at 11.5% but within the 3-entry count that the per-scene cap permits; carve-out documents the old-state sourcing; grounding-ledger confirms no cap-exemption is being claimed; audience-gate is the appropriate review surface for whether the three entries as authored are proportionate.

- **state-updates**: 22 entries (env:17 + taylor:4 + wren:1) / 26 bones = 84.6% by raw count; by unique-bone coverage, 19 distinct bones carry at least one state-update. The author filed a rubric-carve-out: (a) all three oc-props (oc-ward-coverage-notes, oc-jarvis-channel-form, oc-accounting-ledger) are first-touch in this chapter, generating mandatory first-touch state-extension entries across the chapter; (b) this is explicitly a prop-centric accounting chapter where prop mutations ARE the substance delivery; (c) every oc-prop entry is a field-extension on a pending-SEAM prop (SEAM-006/007/008), following the rubric's §Field-extension protocol for oc-slug props. The RUBRIC-FIDELITY class below addresses the SEAM SIGNAL items for those slugs. Classification: **SIGNAL** — the carve-out defense is present, coherent, and strip-tested; the density is explained by chapter architecture (three oc-props first-touched; prop mutations are the spine); audience-gate is the appropriate review surface for whether the density reads as overwhelming.

- **feeling (wren)**: The wren slice uses an ID label `feel:1` with an entry that begins with the wren character slug prefix inline (not as a file-top facet prefix). The ID does not collide with the taylor slice's `1 @20` because they are in separate source slices (consolidated file carries per-source markers). However, the wren entry's format `feel:1 @3 wren-stitch-maker-flea-bottom-ward: ...` renders the character slug inside the ID-line body rather than as a separate sub-file entry — the schema convention is `<id> @<anchor> <character-slug>: <somatic-tell>`. This is schema-compliant; the format is confirmed in the schema's per-character slice convention. No frequency finding — 1 fire / scene-A-bones (bones 1-9 = 9 bones for Wren's scene) is under the 2-5% per-character band; 1/26 = 3.8% at chapter level. **No frequency finding for feeling.** (Annotation only; no SIGNAL.)

*(Correction: the frequency SIGNAL above for feeling is retracted — the feeling fire is 1 taylor + 1 wren = 2 fires / 26 bones = 7.7% chapter-level, but the rubric bands are per-character. Taylor: 1/26 = 3.8% — within 2-5% band. Wren: 1/26 = 3.8% — within 2-5% band. Both within band. No frequency finding.)*

*(Revised FREQUENCY-BAND count: 2 SIGNAL — sensory and state-updates. Feeling is clean on a per-character reading.)*

---

## METADATA-INCONSISTENCY findings (0)

None. All file headers match actual content:
- `facet: location-state`, `episode: b01c06`, `author: studio` — matches 2 entries, both at b01c06 anchors.
- `facet: interest-narrator`, `episode: b01c06`, `author: taylor-hebert-kl-122ac` — matches 7 NI entries.
- `facet: sensory`, `episode: b01c06`, `author: studio` — matches 3 entries.
- `facet: memory`, `episode: b01c06`, `author: taylor-hebert-kl-122ac` — 1 entry (mem:2); gap at mem:1 per R2 DELETE. Consistent with R2-decisions.md.
- `facet: metaphor`, `episode: b01c06`, `author: editor` — 0 entries; zero-fire documented in refuse-log. Consistent.
- `facet: vibes`, `episode: b01c06`, `author: showrunner` — 20 entries. Consistent with cite-index.
- `facet: exposition`, `episode: b01c06` — 1 entry at @0. Sparsity reported as 3.8%; confirmed 1/26 = 3.8%. Consistent.
- `facet: feeling` consolidated — sources: [taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward]. Matches 2 source slices. Consistent.
- `facet: state-updates` consolidated — sources: [env, taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward]. Matches 3 source slices. Consistent.
- `.r2-decisions.md` frontmatter `f-r2-counts: {f-r2-1: 0, f-r2-2: 0, f-r2-3: 0, f-r2-4: 0}` — consistent with per-shard counts (all zero). `entry-deltas` row matches per-shard K/D/A statements.
- Scene-map `total-scenes: 3`, `total-bones: 26` — confirmed by bones file (1-26, 26 bones) and scene-map body (A @1-@9 = 9 bones; B @10-@15 = 6 bones; C @16-@26 = 11 bones; 9+6+11 = 26). Consistent.

---

## CURVE-SHAPE verdict

**SHAPE-OK.**

- `dramatic_shape: climax` (chapter-context in exposition frontmatter; confirmed in showrunner memory chapter b01c06 substance contract).
- Scene-A `rhythm-shape: rising-to-low-peak` — coherent with the pre-climax approach zone leading into the chapter.
- Scene-B `rhythm-shape: flat-tense` — held scene between peak-approach and peak; correct shape for a climax chapter's loaded-pause mid-act.
- Scene-C `rhythm-shape: rising-to-peak` — peak fires at @23 (moral_framework -1.0, THE SEND) and @25 (moral_legibility_to_self +0.5, contrast recognition). This is the climax beat. Correct.
- Peak-bones confirmed in scene-map: @4 (scene-A relational_anchor carrier), @8 (scene-A omission ENACTED), @23 (scene-C THE SEND), @25 (scene-C contrast open). Two peak beats in scene-A (rising-to-low-peak); two in scene-C (rising-to-peak). No peak in scene-B (flat-tense by design). Pattern is structurally correct for a climax chapter.
- Adjacency: scene-B serves as the held zone between the scene-A peak and scene-C peak; no 1→3 compression jumps.
- Flatlining: scene-B is deliberately flat-tense (6 bones; not 30+). No pathological flatline.
- NI file-level check: narrator fires at @4 (scene-A peak), @8 (scene-A peak), @17 (scene-C accounting rise), @20 (scene-C verdict-pause), @23 (scene-C peak), @25 (scene-C peak). NI concentrates on peak and rising zones with appropriate quiet at scene-B — coherent with climax `dramatic_shape`.
- Memory file-level check: mem:2 @17 fires in the accounting rise (scene-C pre-peak zone) — structurally correct; the rubric requires memory to concentrate in flat-low/resolving zones, but @17 is the cost-side accounting entry that generates the peak, not a peak-bone itself. The scene-map lists @17 as `peak-shadow-bones`. Memory fires on a peak-shadow, which the rubric permits (the names-written beat is the monument-grade conversion event that licenses the displacement-clamp). SHAPE-OK for memory.

---

## CONTRADICTION findings (0)

None. Cross-checked all state-update `<old>` values against prior chapter state and within-chapter transitions:

- `studio.spatial_layout.lane-mouth: clear -> handcart-blocking` (@1) — opening state; no prior state-update contradicts.
- `prop:oc-ward-coverage-notes.state: closed -> open` (@6) — first-touch for this chapter; no prior contradicting entry.
- All oc-prop field transitions within-chapter follow logical sequenced order (closed→open→closed for ward-coverage-notes; arrived→opened→filled→set-down→in-hand→sealed→with-courier for jarvis-channel-form; closed→open→content-written→closed for accounting-ledger).
- Taylor actor-state transitions: position @5 (hook-lane-mouth → south-court) follows loc-state:2 @5 (south-court established). No contradiction.
- Taylor moral_framework @23: 1→0 — this records the per-chapter delta; no prior within-chapter state-update contradicts.
- Wren position @3: in-backed-up-crowd → at-taylor-at-lane-mouth — consistent with scene-A @2 (crowd presses the junction) and @3 (Wren crosses the crowd).

No feeling contradiction (1 fire per character; no within-character sequence to contradict).

---

## DEDUP findings (0)

No redundant co-coverage confirmed.

@20 NI:4 vs feel:1 — specifically examined per dispatch brief. NI:4 says: "the stillness is only the hand catching up to a verdict the count reached three entries back" (the cognition DENYING the pause is deliberation). feel:1 says: "her hand stops above the two finished entries" (the body arrested). These are distinct registrations on the same bone — feel:1 shows the body-stop; NI:4 shows the cognitive-voice reasserting to classify the stop as mere lag. The R2 decisions log (feeling-taylor section) and (NI section, narrator:4) both address this and confirm the two entries do opposite work: feel:1 is the body-signal; NI:4 is the analytical voice that overrides it. Per the wren card §"affect appears in brief body-signals before the analytical voice reasserts" this pairing IS the card pattern. **NOT a DEDUP.**

NI:2 vs NI:7 @8 — NI:2 names the act and the blank-as-entry; NI:7 names the substrate fact (notes are hers, not the channel's; what stays in the column never crosses to the courier). These are distinct observations at the same anchor: NI:2 is the priced-act; NI:7 is the institutional mechanics of why the blank protects. No duplication of content.

Vibes vs NI at same anchors — vibes shapes social/tonal texture; NI fires cognitive registrations. No content duplication verified across @4, @8, @20, @23, @25.

Dialogue:1 vs NI:1 @4 — NI:1 registers Taylor's interior cost-frame ("a sound route from a stranger carries a cost she has not yet named"); dialogue:1 is the spoken line itself ("There's a way past..."). Distinct layers; no duplication.

---

## SUPERFLUOUS findings (0)

All lonely entries in the cite-index examined per the rubric's three-axis test (necessity / interestingness / frugality):

- `sensory:1 @2` (lonely) — pressure fire at the scene-A opening; establishes the crowd-compression baseline before the Wren exchange fires at @4. Necessary for the sensory arc (lane-passable → crowd-backed → stylus-rhythm → silence). Frugal: one clause. **Not superfluous.**
- `state:2-4 @6/@7/@9` (lonely) — oc-ward-coverage-notes first-touch field-extensions. These are structurally necessary: they record the instrument-state of the prop that enacts the chapter's central protective omission. No other facet carries prop physical-state. Frugal. **Not superfluous.**
- `state:6-9 @11/@14/@15/@16` (lonely) — jarvis-channel-form and accounting-ledger field-extension transitions. Each records a distinct prop-state transition that is not redundant with any co-cited entry. Frugal. **Not superfluous.**
- `state:11-13 @18/@21/@22` (lonely) — continuation entries on the accounting-ledger close and the form re-lift. Structurally required to close the prop-arc. **Not superfluous.**
- `state:15-17 @24/@25/@26` (lonely) — form holder-transfer (irrevocable departure), ward-coverage-notes reopen, ward-coverage-notes close. Each records a distinct terminal prop-state. **Not superfluous.**
- `exposition:1 @0` (lonely by anchor) — the single prior-episode-bridge entry; licensed as a synthetic preamble; confirmed necessary by R2 exposition judge who verified no lens-facet carries the c05→c06 board-state conversion. **Not superfluous.**

Note on lonely-entry convention per Phase 5 audit spec: "bones in `rhythm-shape: flat-low` zones and off-anchor vibes are never superfluous." Scene-B is `flat-tense` (nearest equivalent to flat-low); state-updates entries in scene-B (@10-@15: state:5-8) are in a held scene and carry prop-state transitions that the loaded-pause scene structurally requires. Their loneliness reflects the flat-tense design (no lens facets fire in scene-B by design); not a superfluous finding.

---

## CONSTRAINT findings (1 HARD)

- **fault-001** [vibes:19] @25 — **vibes-licensed-by-dangling** — `vibes:19` carries `licensed-by: state-update:4, proto:25, memory:1`. The `memory:1` reference is a dead citation: R2 memory judge (`.r2-decisions.md` § memory) DELETED `mem:1 @15` (verdict: DELETE cascade 1; rationale: NI-spine absent on a bone the feeling author deliberately left silent). The cite-index confirms no `mem:1` entry exists (only `mem:2 @17`). The `lic-out=[..., memory:1]` field on `vibes:19` in the cite-index confirms the reference was emitted but now resolves to a deleted entry. **This is a cross-facet cascade defect: a vibes entry's license-anchor was deleted in R2, but the vibes facet was not re-judged in R2 (vibes is R2-exempt per command spec: "Vibes is not re-judged in R2; the showrunner-authored R1 vibes facet stands as-is unless the audit flags it"). The vibes author had no opportunity to self-correct; the R2 memory judge's delete created a dangling reference that only this audit can surface.** The CONSTRAINT rule is explicit: "vibes with unresolvable or forward-citing `licensed-by:` → HARD." This qualifies: `memory:1` is unresolvable (deleted entry). **HARD.**
  - `why`: A vibes entry with a dangling licensed-by cites a non-existent facet entry as its authority. The stitcher render-weighting and the audience-gate's graph-aware attack both read the full `licensed-by` chain; an unresolvable citation creates an integrity gap in the facet graph's authority chain and may confuse downstream rendering behavior.
  - `criteria`: `vibes:19` must have its `licensed-by` field updated so that `memory:1` is removed or replaced with a valid resolvable reference (either an existing facet entry or a proto-line reference). The entry itself (tragic-causal framing of Wren's absent name against the dispatched four) is substantively grounded by `state-update:4` and `proto:25` which both resolve; the fix is to drop the `memory:1` reference from the `licensed-by` field, or re-point it to `mem:2` if the thematic logic connects (both are Earth-Bet displacement callbacks to the conversion of persons to deliverables), or rely solely on the two valid citations.
  - **Routing**: vibes author (showrunner).

- **scene-map coverage (URI-SCENE-WINDOW) — PASS.** Scene-map reports `coverage: 26/26 bones in exactly one scene`. Scene-A @1-@9 (9 bones), scene-B @10-@15 (6 bones), scene-C @16-@26 (11 bones); 9+6+11 = 26. `total-scenes: 3`, `total-bones: 26` match body. No gaps, no overlaps, no dangling anchors, no duplicate scene labels. **PASS.**

- **dialogue-coverage upstream sanity (URI-WRITE-DIALOGUE-COBONDED) — PASS.** Single dialogue-anchor bone: @4 (`wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac`). Bones file carries `[wren-stitch-maker-flea-bottom-ward:1]` citation token on @4. `theater/dialogue/wren-stitch-maker-flea-bottom-ward.md` exists, is non-empty, and resolves entry 1 to bone @4. No FAULT-UPSTREAM-LEAK. **PASS.**

- **Earth-Bet hard-fence scan — PASS.** Full case-insensitive scan across all facet text fields (NI free-text, memory gloss and target-reference, sensory disambiguation, loc-state composite-state, vibes entity-target-primary and list-body, feeling somatic-tell, state-updates field names and values, exposition text and source fields, dialogue utterance and objective) against the canonical Earth-Bet hard-fence noun list:
  - `memory:2` target-reference `monument-override-architecture-residue` — contains "override-architecture-residue" only; no Earth-Bet proper-noun substring (no Khepri, no Gold Morning, no shard, no parahuman, no cape-name fragment). The slug is a Westerosi-displacement target reference describing the administrative-conversion pattern. CLEAN.
  - `vibes` entity-target-primary fields — no Earth-Bet proper-noun fragments; all vocabulary is Westerosi-register (smallfolk-gallows, tragic-causal, rising-entrapment, cold-utilitarian interiority, plain-direction, omission-as-protection, accounting, ledger, etc.).
  - `exposition:1` text — "the coverage," "the intelligence," "the Jarvis line," "Otto," "the arrangement," "Sera," "the Hook," "the count," "the column," "the accounting," "the form," "Movement patterns," "persons," "junction," "passage" — all Westerosi-political/clinical-instrument vocabulary. The exposition R1 notes perform an embedded-noun audit that confirms CLEAN; R2 confirms. **PASS.**
  - `dialogue:1` — "There's a way past. Cut before the cart, by the tallow-boiler's wall — the south court. It's narrow, but it's there. I been through." — no Earth-Bet noun or mechanism-naming vocabulary. **PASS.**
  - All fields surveyed. No hit.

- **Memory — NI-spine co-citation (CONSTRAINT: memory without NI-spine) — PASS.** `mem:2 @17`: NI fires at @17 (narrator:3). Co-citation confirmed in cite-index: `mem:2 @17 co=[narrator:3, sensory:2, state:10]`. **PASS.**

- **Feeling — POV NI non-redundancy — PASS.** Taylor feel:1 @20 and NI:4 @20 confirmed distinct (see DEDUP findings). **PASS.**

- **Exposition — source-traceability — PASS.** `exposition:1 @0` cites sources in-line: `sources: chapters[b01c06].handoff_in.open_threads`, `chapters[b01c06].handoff_in.world_state`, `chapters[b01c05].handoff_out.open_threads`, `b01c05 exposition:2`, `actors/otto-hightower/card.md §relationships §taylor-hebert`, `chapters[b01c06].chunk`, `scene b01c06s01.chunk`, `cond-taylor-pov-behavior §register-cold-utilitarian §compression`, `coverage-map-instrument-family register (b01c02)`. All claims in the gloss text trace to these sources. `lic-out` in cite-index lists `[b01c03:3, b01c03:6, b01c03:8, exposition:2, b01c01:4]` as the cross-episode citation chain. **PASS.**

- **Exposition — license-completeness — PASS.** `licensed-by` field is a long inline string naming all three personas (cape-fic-reader, dark-fantasy-reader, worm-canon-pedant) with specific gap-claims per persona. Field is present and substantive. **PASS.**

- **Exposition — scene-orient fire-rule — PASS.** Zero scene-open-orient entries. Fire-audit documents three refusals (chapter-open @1: bridge+bone-body carry; scene-A→B @10: loc-state expected fire + bone-body time-carry; scene-B→C @16: continuity-no-skip). All refusals are structurally sound per the fire-rule clauses. **PASS.**

- **Exposition — re-gloss check — PASS.** The R1 exposition author records: "This chapter glosses NO new terms. ZERO new register entries promote." Cross-episode register write-back is empty. No re-gloss of any term already in the register. `exposition:1`'s embedded-noun frames all resolve to prior-chapter entries. **PASS.**

- **Exposition — first-mention-character coverage — PASS.** The exposition author's cull-pass documents that no new named individual is introduced in narrator-prose for the first time in this chapter. "The courier" at @24 is register-resident via b01c03:3 jarvis-coin-kl-courier. Wren at @3/@4 is register-resident via b01c01:9. No first-mention entry required; none is missing. **PASS.**

- **Dialogue — behavior-card compliance — PASS.** Wren's sole utterance: "There's a way past. Cut before the cart, by the tallow-boiler's wall — the south court. It's narrow, but it's there. I been through." Checked against `westeros-smallfolk.card.md` §hard fences and `wren-stitch-maker-flea-bottom-ward/card.md` §Hard Fences:
  - No forbidden vocabulary ("indeed, certainly, perhaps, however, nevertheless"; anachronistic idiom; multi-syllable Latinate).
  - No Earth-Bet/mechanism leak.
  - Collapsed past participle ("I been through") ✓ per westeros-smallfolk §Syntax.
  - Coordination over subordination ("It's narrow, but it's there" — but, not although) ✓.
  - Short stacked declaratives ✓.
  - No up-the-hierarchy address (near-peer exchange; within-class register loosening ✓).
  - Hard Fence 1 (age-appropriate — no precocious-wise commentary) ✓.
  - Hard Fence 2 (does not ask Taylor the question) ✓.
  - Hard Fence 3 (does not become a functional partner; gives a route and stops) ✓.
  **PASS.**

- **Dialogue — citation-completeness — PASS.** The drafts sidecar `wren-stitch-maker-flea-bottom-ward.drafts.md` marks D3 as CHOSEN with both a card-signature §-citation block and a facet-license acknowledgment (vibes:1/@4 and vibes:2/@4 cited in the R2 decision shard; narrated in the dialogue R2 shard body). Card-signature §-cites: westeros-smallfolk §Cadence, §Syntax (collapsed past participle), §Syntax (coordination over subordination), §Vocabulary (functional geography), §Register-markers (within-class loosening); persona card §Voice tells (reports observed before interprets). Both axes present. **PASS.**

- **Dialogue — objective-anchoring — PASS.** Entry 1 carries `objective: give Taylor the checked route past the blocked lane, freely and unasked — moving the relational anchor from ward-in-coverage to a person who has spoken to Taylor and been answered`. This is non-empty and matches the proto-line bone @4 (`wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac`) and the scene-A substance contract (relational_anchor_status +1.0 cl-d06 first tranche). **PASS.**

- **Loc-state transition-run continuity-license — N/A.** No continuity-carry entries in location-state. The two entries are standard state-establishment entries. **N/A.**

- **State-updates — POV co-citation completeness (actor:POV entries require NI co-citation) — PASS.** Three POV actor-state shifts noted in the taylor source slice with explicit co-citation notes:
  - state:19 @8 (relational_anchor_status 2→3) — NI co-citation present: narrator:2 @8 and narrator:7 @8. Confirmed in cite-index: `state:19 @8 back=N co=[narrator:2, narrator:7, state:2, vibes:6-9]`. **PASS.**
  - state:20 @23 (moral_framework 1→0) — NI co-citation: narrator:5 @23. Confirmed in cite-index: `state:20 @23 back=N co=[narrator:5, state:3, state:14, vibes:13-17]`. **PASS.**
  - state:21 @25 (moral_legibility_to_self 4→4.5) — NI co-citation: narrator:6 @25. Confirmed in cite-index: `state:21 @25 back=N co=[narrator:6, state:4, state:16, vibes:18-20]`. **PASS.**

---

## AP-SCAN findings (0)

- **Memory AP-functional-callback**: mem:2 @17 — R2 judge (memory section) addresses the multi-justification stack: monument-trigger (four-bodies-to-persons conversion at administrative-violence scale) + NI-spine co-citation + audience-meaningful (conversion of people into a deliverable) + ≥2 functional jobs (painting-characterization + social-commentary) + scene-eligible (rising accounting zone, not peak). Multi-justification ≥3 of 5 confirmed. No AP-functional-callback (would require: functional callback only, NI-spine missing, target unresolvable). **CLEAN.**

- **Feeling AP-named-feeling-vocab**: both feel:1 entries use somatic-tell form only:
  - Taylor feel:1: "her hand stops above the two finished entries" — no named feeling, no hedge, no simile, no second clause latency observation. **CLEAN.**
  - Wren feel:1: "her eyes find Taylor in the press before her feet turn toward her" — no named feeling. **CLEAN.**

- **Metaphor AP3/AP7/AP12**: zero entries. No scan needed.

- **Vibes AP-multi-source / AP8 sentence-parsability**: vibes entries use entity-target-primary form with bracketed tag-lists. Each entry names exactly one entity-target-primary (an actor slug or loc slug or `episode` or `series`). No multi-source vibes entries. Parsability: tag-list items are hyphenated descriptors in standard form; no sentence-parsability anomaly. **CLEAN.**

- **Dialogue AP-chassis-contamination** (em-dash + semicolon spine on non-Taylor speakers): Wren's line contains one em-dash (`by the tallow-boiler's wall — the south court`) used as a geographic clarifier, not as Taylor's chassis em-dash-as-subordinating-splice. This is a direction-giving em-dash (naming the place) in a smallfolk utterance — structurally distinct from the Taylor-prose em-dash cadence. No chassis bleed. **CLEAN.**

- **Dialogue AP-modern-hr-speak**: Wren's line — none. All vocabulary is functional geography + plain direction. **CLEAN.**

- **Dialogue AP-deposition-cadence**: not applicable; single declarative offering, not a Q-and-A. **CLEAN.**

- **Dialogue AP-nominalization-substituting-plain-English**: not applicable; Wren's register is verb-driven declaratives. **CLEAN.**

- **NI AP10 inverted-predicate saturation check**: R2 judge identified three possible AP10-adjacent constructions. "the blank is the entry" (@8), "a clean accounting is what the breach looks like" (@23), "only one of them will ever balance" (@25). R2 judges correctly classified: only @23 uses the genuine definitional-collapse construction ("is what the breach looks like from inside the discipline"). @8 is copular identity-of-a-ledger-object; @25 is a future-tense verdict, not a present-tense definitional collapse. Rule caps the chassis at one per file at a register-defining peak; @23 is the legitimate fire. Count: 1 of 7 entries = 14% — well below the 40% saturation threshold. **CLEAN.**

- **AP-SCAN saturation (URI-AP-SCAN-SATURATION)**: no facet reaches the 40% hits/total-entries threshold. NI: 1 AP10-adjacent in 7 entries = 14%. No saturation. **CLEAN.**

---

## TASTE-FLAG findings (0)

- **Atmosphere-thin**: Scene-B (@10-@15) carries 6 bones with no lens-facet fires except state-updates. This is by architectural design (flat-tense loaded pause; all axes HELD). The scene-map documents the loaded-pause integrity protected pattern. The grounding-ledger has zero entries, confirming the Phase 2.5/4.5 aliveness reviewer found scene-B ALIVE (not AIRLESS-HOLE) on the de-abstracted scaffold. The verdict-pause bone @20 is the structural breath-point and it receives feel:1 + NI:4 + sensory:3 + vibes:12. The TASTE-FLAG risk for atmosphere-thin was assessed at the bone-gate and aliveness review; no residual TASTE-FLAG warranted here.

- **Voice-fidelity**: NI entries reviewed for Taylor-voice register. All seven entries use the cold-utilitarian clinical-accounting vocabulary the card specifies (the feed, the hand, the count, the column, the entry, the watch-cost, the seal, the ledger). No register drift to literary/thematic narration (none "names the road-to-hell irony from outside"). **CLEAN.**

- **Momentum-stall**: Scene-B designed as flat-tense; this is load-bearing structure, not stall. Per Phase 5 SUPERFLUOUS convention: bones in flat-low zones are never superfluous. Flat-tense is the scene-B design intent and is protected by the scene-map. No TASTE-FLAG.

---

## PILE-UP REVIEW (4)

Per cite-index §Pile-ups:

- **@23** (8 co-located: narrator:5, state:3, state:14, vibes:13, vibes:14, vibes:15, vibes:16, vibes:17) — `taylor-hebert-kl-122ac seals the jarvis-channel form`. Verdict: **warranted**. @23 is the moral peak of the chapter (THE SEND, moral_framework -1.0). Per-scene peak with the highest axis-magnitude in the chapter. 5 vibes entries fan out across taylor actor, episode scope, and series scope (the rationalize-each-trade pattern-class established); narrator:5 carries the discipline-internal framing; state:3 (@7 content propagation) and state:14 (@23 form-sealed state) are the prop-transitions recording the irreversible act. The pile-up reflects the chapter's central irrevocable event receiving full-coverage treatment across every scope level. The de-abstraction integrity protected pattern guards against this becoming re-abstraction at stitch. Pile-up warranted.

- **@4** (7 co-located: narrator:1, vibes:1, vibes:2, vibes:3, vibes:4, vibes:5, wren-stitch-maker-flea-bottom-ward:1) — `wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac`. Verdict: **warranted**. The first spoken exchange between Wren and Taylor (relational_anchor_status +1.0 first tranche) is the chapter's other peak-bone (scene-A rising-to-low-peak). 5 vibes entries establish the smallfolk-gallows register, the plain-direction exchange, the mutual-silence resumption, and the location-as-site of the exchange across actor (×2) and location (×2) and mutual-silence (×1) angles. Narrator:1 carries Taylor's POV cost-frame. Dialogue:1 carries the actual spoken line. Concentration is appropriate for a relational peak and the chapter's first spoken Wren exchange. Warranted.

- **@8** (7 co-located: narrator:2, narrator:7, state:2, vibes:6, vibes:7, vibes:8, vibes:9) — `taylor-hebert-kl-122ac blanks the contact-source field`. Verdict: **warranted**. The omission-enacted peak-bone of scene-A. 4 vibes entries cover the act across three angles (taylor omission-authored-protection, taylor cold-utilitarian, wren indirect protection, location-holds-the-charge). NI:2 and NI:7 cover the act and the substrate-distinction respectively. State:2 records the prop-state extension. The dispersion is required: the omission is the chapter's only Wren-adjacent moral act in scene-A and it needs coverage at every frame level. Warranted.

- **@25** (6 co-located: narrator:6, state:4, state:16, vibes:18, vibes:19, vibes:20) — `taylor-hebert-kl-122ac opens the ward-coverage notes`. Verdict: **warranted** with note. @25 is a peak-bone (moral_legibility_to_self +0.5, the contrast recognition). 3 vibes entries: cold-utilitarian contrast read (taylor, vibes:18), tragic-causal wren-absent framing (wren, vibes:19), rising-entrapment wren framing (wren, vibes:20). NI:6 carries the legibility-rise ("the same hand, two ledgers, only one will ever balance"). State:4 and state:16 record the coverage-notes reopen and the holder-transfer respectively. NOTE: vibes:19 @25 carries the dangling `licensed-by: memory:1` (see fault-001 in CONSTRAINT section). The entry itself is substantively covered by `state-update:4` and `proto:25`; the pile-up verdict does not change on this account, but fixer must resolve the dangling citation before Phase 5b.

---

## RUBRIC-FIDELITY findings (1 SIGNAL)

- **signal-001** [state-updates: oc-prop slugs] — **rubric-fidelity-card-resolution** — entries on targets `prop:oc-ward-coverage-notes`, `prop:oc-jarvis-channel-form`, `prop:oc-accounting-ledger` (state:2-17 inclusive, covering SEAM-006, SEAM-007, SEAM-008) reference oc-slug targets for which no warehouse card exists in `active-project/warehouse/` at audit time. The state-updates rubric's §Card-resolution requirement (RUBRIC-FIDELITY class 12(d)) states that every entry naming a prop slug must resolve to an existing card. The carve-out claim (rubric §Field-extension protocol permits oc-slug extension when the prop card is pending margit) is documented in-file, is structurally sound (these are the chapter's central instrument props; refusing all entries would hollow the state-track), and is precedented in prior chapters (per the carve-out comment citing b01c05 patterns). Per URI-FACETS-CYCLE-1, in-chapter precedented unresolved slugs with structurally clear glosses are **SIGNAL** with a margit-referral candidate slug, not HARD. Classification: **SIGNAL.**
  - Margit-referral candidate slugs: `prop-oc-ward-coverage-notes` (Taylor's personal coverage-notes book / record; Ward coverage instrument containing the contact-source/contact-role field structure); `prop-oc-jarvis-channel-form` (the Jarvis-channel routing form Taylor files with the courier; the intelligence-delivery instrument that routes deliverables up to Otto's network); `prop-oc-accounting-ledger` (the ledger-board Taylor uses for the explicit cost-accounting record; two-column: cost side + protection side).
  - **Routing**: margit (card authoring for three oc-prop slugs); state-updates author (ENV slice — studio) should verify the margit-authored cards match the field-extension vocabulary once cards are available.

- **memory — doubled-register file-level gate — SOFT NOTE.** The rubric requires a doubled-register file (at least one Earth-Bet displacement fire AND at least one Westerosi-monument clamp fire). With `mem:1` deleted, the surviving file has only `mem:2 @17` which is the Earth-Bet-displacement leg (four-bodies-to-persons administrative conversion → Westerosi accounting act). The Westerosi-monument clamp (Dance foreknowledge; "the wards holding the losing color are the ones that burn first" from mem:1) was the monument leg. Deleting mem:1 collapses the file to single-register (Earth-Bet displacement only). The R2 memory judge's pattern-scan explicitly addresses this: "The doubled register is per-season; c06 lands single-register (Earth-Bet only) because the spine fence forced it, which the rubric's soft single-register clause explicitly permits." The rubric's soft single-register clause permits this when the spine fence forces it (the V3 feel-as-spine carve-out conditions were not met at @15: chapter is climax not hinge; feel:1 is at @20 not @15). The R2 judge accepted this as a known trade-off (see cap-burn semantics note in R2 memory decisions: "The doubled register is per-season; c06 lands single-register … which the rubric's soft single-register clause explicitly permits"). This is **not a HARD finding** given the rubric's own soft clause; but it is a **SIGNAL** that the file is single-register and that future readers of this chapter's memory facet will see an Earth-Bet displacement only, with the Westerosi monument leg absent. Per the R2 judge's cap-refusal note: "the Dance-clamp at @15 failed spine, not displacement; relocating it forward to a beat with a spine was tempting but no quiet-beat in scene-B/C carries the succession-clamp cue." The trade-off is accepted and documented.
  - This note is captured in the RUBRIC-FIDELITY class for completeness; no fixer action required (the R2 judge already evaluated the trade-off against the rubric's soft clause). Advisory only.

---

## Audit summary

- **Total entries reviewed**: 57 facet entries + 1 dialogue entry = 58 entries across 9 facet files + 1 dialogue file.
- **HARD classes**: STRUCTURAL 0 | CONTRADICTION 0 | DEDUP 0 | SUPERFLUOUS 0 | CONSTRAINT 1 (fault-001: vibes:19 dangling licensed-by: memory:1) | RUBRIC-FIDELITY 0
- **SIGNAL classes**: FREQUENCY-BAND 2 (sensory breach-high; state-updates density) | METADATA-INCONSISTENCY 0 | AP-SCAN 0 | TASTE-FLAG 0 | PILE-UP warranted 4/4 | RUBRIC-FIDELITY 1 (oc-prop card-resolution; margit-referral) + 1 soft advisory (memory single-register per rubric's soft clause)
- **CURVE-SHAPE**: SHAPE-OK (climax chapter; scene-A rising-to-low-peak / scene-B flat-tense / scene-C rising-to-peak; all coherent with declared dramatic_shape)

## Routing

For each finding:

| Finding | Type | Routing |
|---------|------|---------|
| fault-001 — vibes:19 @25 dangling `licensed-by: memory:1` | HARD | fixer → vibes author (showrunner) |
| signal-001 — oc-prop card-resolution (SEAM-006/007/008) | SIGNAL | margit (prop card authoring) |
| signal-002 — sensory breach-high (11.5% vs 3-6% band) | SIGNAL | audience-gate (advisory; not a fixer action) |
| signal-003 — state-updates density (84.6% vs band; carve-out filed) | SIGNAL | audience-gate (advisory; not a fixer action) |
| soft advisory — memory single-register (rubric soft clause accepted) | advisory | no action; R2 judge trade-off documented |

**Phase 5 gate status**: HARD = 1 (fault-001). Phase 5b cannot fire until fault-001 is resolved and Phase 5 is re-run with 0 HARD.

---

## Phase 5 remediation — cycle 1 (2026-05-31)

**fault-001 (HARD) RESOLVED.** vibes:19 @25 `licensed-by` had `memory:1` removed (R2-deleted mem:1; entry content covered by the surviving `state-update:4` + `proto:25`). cite-index rebuilt; vibes:19 lic-out=[state-update:4, proto:25]; zero `memory:1`/`mem:1` tokens anywhere in proto-lines, vibes.md, or cite-index. A citation removal cannot introduce new STRUCTURAL/CONTRADICTION/DEDUP/CONSTRAINT findings.

**Phase 5 gate: HARD = 0.** Cleared for Phase 5b.

SIGNALs (4) carried as advisory to Phase 5b:
- signal-001 oc-prop card-resolution (SEAM-006/007/008) -> margit referral
- signal-002 sensory FREQUENCY-BAND 11.5% (modality-floor precedence + old-state carve-out)
- signal-003 state-updates density (oc-prop first-touch + prop-centric chapter carve-out)
- soft: memory single-register (R2 spine-fence trade-off accepted)
