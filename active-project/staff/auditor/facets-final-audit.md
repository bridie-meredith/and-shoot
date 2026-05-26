audit: facets-final-r1
episode: b01c02
date: 2026-05-26
mode: flag-only
status: FINDINGS-PRESENT
totals: 10 findings across 6 facets

---

## STRUCTURAL findings (2)

- [state:8–17] — ID-namespace anomaly — state-updates.md renumbers the actor-slice entries starting at 8 rather than 1. The consolidated file carries env entries 1–7 and then actor entries 8–17; per `schemas/facet.schema.md` ID monotonicity requirement, consolidated facets must renumber from 1 in a single sequence (or document the consolidation explicitly in the schema note — the schema says IDs are "scoped per facet file" and slice consolidation under Phase 2 is supposed to renumber monotonically). The consolidated file keeps the raw actor-slice IDs (8–17) rather than renumbering to 8–17 post-consolidation. **Severity: SIGNAL** (consolidation tool is documented to renumber; the gap is between the raw slice numbering and the final consolidated output, but the cite-index correctly back-references `state:1`–`state:17` as consecutive. The ID set is 1–17 without gaps; no anchor resolution fails. The apparent anomaly is that the actor-slice begins at 8 because env has 7 entries — which is the correct consolidated sequence. Downgrade to pass on closer examination: IDs 1–17 are monotonic and gapless in the consolidated file.)

  **Revised disposition:** PASS. The consolidated state-updates.md runs IDs 1–7 (env) followed by 8–17 (actor), making the full set 1–17 monotonically. No structural fault.

- [state:8–9 cite-index back=N] — Back-reference discrepancy — cite-index shows state:8 @11 back=N and state:9 @11 back=N, but proto-lines bone @11 reads `[loc-state:3] [narrator:2] [state:1] [state:2] [state:4] [vibes:1]` — only state:1, state:2, state:4 are cited on @11 in the proto-lines file; state:8 and state:9 are absent from the @11 proto-line citation set. Similarly, cite-index lists state:10 @12 back=N and state:11 @15 back=N, and state:12–17 all back=N. The proto-lines file citations at @11 do not include state:8 or state:9; at @12 do not include state:10; at @15 do not include state:11. The cite-index `back=N` flags confirm the reverse-citation is absent, meaning the actor state entries at @11, @12, @15, @27, @40, @41, @42, @43, @47 carry no `[state:N]` token on the corresponding proto-line. This is a systematic pattern: all 10 actor-slice state entries (state:8–17) are back=N. **Severity: HARD.** Every `actor:taylor-hebert-kl-122ac.*` state update entry requires a citation token on its anchor proto-line for stitcher routing; 10 of 17 state entries are uncited on the canonical proto-lines. The env slice entries (state:1–7) are back=Y; the actor slice (state:8–17) is uniformly back=N.

  - id: fault-001
    type: fault
    what: cite-index entries state:8 through state:17 all carry back=N; proto-lines @11, @12, @15, @27, @40, @41, @42, @43, @47 carry no [state:N] citation token for the actor-slice entries anchored there
    why: The stitcher resolves state-update entries by following `[state:N]` citation tokens on proto-lines; uncited entries are invisible to the stitcher at render time. All 10 actor-state entries for taylor-hebert-kl-122ac will be silently dropped.
    criteria: the canonical proto-lines file must carry [state:N] tokens on each anchor bone matching the actor-slice entries state:8–17; tokens must be added to bones @11 (state:8, state:9), @12 (state:10), @15 (state:11), @27 (state:12), @40 (state:13), @41 (state:14), @42 (state:15), @43 (state:16), @47 (state:17)

---

## FREQUENCY-BAND findings (2)

- sensory: actual 2/47 = 4.3%; band 3–6%; within band.
- memory: actual 3/47 = 6.4%; band 5–12%; within band.
- feeling: actual 1/47 = 2.1%; band 2–5%; just below band lower bound — accepted-with-defense by R2 judge per rubric's silence-default. **SIGNAL: feeling density 2.1% sits at the 2% floor; the deleted feel:1 reduced from 2 to 1 entry. No fault — the rubric explicitly licenses the silence default when a form-failed entry is removed; R2 documented the trade-off.** Advisory for downstream chapter authors: one more deletion of a feeling entry in c03 would produce a sub-band file.
- metaphor: actual 0/47 = 0.0%; band 0–3%; within band.
- NI: actual 12/47 = 25.5%; band 15–25%; **SIGNAL: 0.5% above band ceiling.** R2 documented the defense (cross-facet contract requires NI spine at 7 POV state-update anchors + 3 memory anchors + 2 feeling anchors, reducing to 10 distinct anchors; 12 entries serve these contract slots). The defense is architecturally sound — the chapter's solo-POV dense-state structure drives a natural NI-count above the generic 25% ceiling. Fixer need not act; this is an advisory signal for rubric calibration in solo-POV mapping chapters.
- exposition: actual 4/47 = 8.5%; band 1–5% per episode; **SIGNAL: above sparsity-ratio band.** R2 documented the governing constraint is per-episode caps (not sparsity ratio) under URI-SUBSTANCE-OVERHAUL precedent. Per-episode caps: 1 prior-episode-bridge (cap 1, used 1), 1 episode-open-context (cap 3, used 1), 1 first-mention-place (cap 12, used 1), 1 scene-open-orient (cap 1/scene, used 1/3 scenes). All caps clear. Sparsity-ratio breach is advisory under the per-cap governing rule.

---

## METADATA-INCONSISTENCY findings (2)

- `.r2-decisions.md` metaphor shard header: `episode: b01-c01` and `layer: R2.1` with `date: 2026-05-25`. The metaphor shard body also describes b01c01 anchor IDs (mem:1 @3, mem:2 @26, feel:1 @21, feel:2 @10 — these are b01c01 coordinates, not b01c02 coordinates). The consolidated `.r2-decisions.md` is labeled `episode: b01-c02` in its top-level frontmatter, but the metaphor shard it includes carries the b01c01 episode field and b01c01 bone coordinates. **Severity: SIGNAL.** The metaphor file itself (`metaphor-b01-c02.md`) is correctly authored for b01c02 (47-bone, all b01c02 anchor IDs); the shard in `.r2-decisions.md` is the b01c01 shard that was not replaced by a b01c02-specific one. This creates a metadata mismatch: the consolidated decision-log asserts b01c02 scope but contains a b01c01 metaphor shard. No downstream functional impact (metaphor has 0 entries; the b01c01 shard's verdicts are both "zero-fire confirmed"; the b01c02 file independently carries `r2: r2-metaphor-judge (2026-05-26)` with DEFEND-ZERO). But the orchestrator-critic reads `f-r2-counts` from the consolidated file's top-level frontmatter (which sums to zero for metaphor per the shard's `f-r2-1:0`), so the count is correct even with the wrong-episode shard.

  - id: fault-002
    type: flag
    what: `.r2-decisions.md` § metaphor shard carries `episode: b01-c01`, `date: 2026-05-25`, and b01c01-era anchor references (mem:1 @3, feel:2 @10 in the b01c01 coordinate system)
    why: The consolidated decision-log's metaphor section documents decisions for the wrong chapter; if a future re-run reuses this consolidated file, the shard mismatch may cause confusion in Phase 3 stale-shard checks (cite_index_hash in the metaphor shard is 0241e... not the b01c02 index hash)
    criteria: no fixer action required for gate-passage (functional data is correct); recommend replacing the metaphor shard body with the b01c02-specific zero-fires rationale from `metaphor-b01-c02.md` for provenance correctness

- `feeling.md` frontmatter: declares `r2_actions: kept: 1; deleted: 1; added: 0` — consistent with content (1 entry retained). The header also lists `scene_distribution: scene-A: 0, scene-B: 1, scene-C: 0`, consistent with the single entry at @23. No inconsistency. **PASS.**

- `interest-narrator-b01-c02.md` header: declares `entry_count: 12` and the body contains entries 1–13 with entry 7 absent (narrator:7 deleted in R2, leaving IDs 1–6, 8–13 = 12 entries). Count claim of 12 matches actual count of 12. Additionally, the file header uses `episode: b01-c02` (hyphenated form) while the proto-lines file header uses `episode: b01c02` (concatenated form). **SIGNAL: slug format inconsistency between files.** The facet schema requires `episode: <slug>`; the chapter slug is `b01c02` per bones file header. Using `b01-c02` in some facet headers and `b01c02` in the proto-lines header creates a namespace mismatch that a strict slug-resolver would treat as different chapters.

  - id: fault-003
    type: flag
    what: episode slug format inconsistency — `interest-narrator-b01-c02.md` and `memory-b01-c02.md` use `episode: b01-c02`; `state-updates.md` (actor slice) uses `episode: b01-c02`; `exposition-b01-c02.md` uses `episode: b01-c02`; `sensory-b01-c02.md` uses `episode: b01c02`; proto-lines uses `episode: b01c02`
    why: slug format inconsistency (`b01-c02` vs `b01c02`) could cause slug-resolver mismatches in downstream tools that expect a canonical form
    criteria: advisory only; no gate impact at this phase — the and-facets command body normalizes either form per Phase 0 step 1. No fixer dispatch required.

---

## CURVE-SHAPE verdict

- Episode-level: SHAPE-OK. Chapter declares `dramatic_shape: rising` in substance framework. Scene-A `rhythm-shape: rising` → Scene-B `rhythm-shape: peak-and-trail` → Scene-C `rhythm-shape: peak-and-trail`. A rising chapter whose scenes progress from a local peak (A), through a mid-chapter peak (B), to the terminal peak (C) is coherent with `rising` — the overall arc rises across the three scenes (each scene peak is higher-magnitude: scene-A peak @11 is the range/coverage-mode flip, scene-B peak @27 is the relational_anchor_status +1.0 recognition, scene-C peak @40 is the moral_legibility_to_self crack). `rising` describes the chapter-level trajectory, not a requirement that every scene be `rhythm-shape: rising`. SHAPE-OK.
- Per-scene: scene-A peak-present (@11); scene-B peak-present (@27); scene-C peak-present (@40). All three scenes carry declared peak-bones. Scene-map specifies peak-shadow-bones for all three scenes. No scene is peakless.
- Adjacency: No 1→3 jumps visible in the scene-map (three scenes with continuous @1-@47 coverage; no scene has a bare-low section immediately adjacent to a peak without at least one peak-shadow bone between them per the scene-map declarations).
- Flatlining: Scene-B's flat-low interior (@18–@26 excluding the peak-shadow @26) runs 8 consecutive bones — far below the 30-bone flatlining threshold. No flatlining concern.

---

## CONTRADICTION findings (0)

No same-anchor state contradictions found. State-updates entries at shared anchors:
- @11: state:8 (coverage-mode: subsistence → systematic-deliberate) and state:9 (range-ceiling: working → into-the-fours-under-suppression-cost) — different fields, no contradiction.
- @41: state:14 (moral_legibility_to_self: crack-arriving → crack-held) and narrator:9 — compatible.
- @42: state:15 (moral_legibility_to_self: crack-held → crack-suppressed) and mem:3 — compatible, sequential.

---

## DEDUP findings (1)

- [vibes:6] @29 — back=N in cite-index and anchor @29 carries vibes:5 and vibes:7 but NOT vibes:6 in the proto-lines citation. Cite-index lists `vibes:6 @29 back=N co=[loc-state:8, vibes:5, vibes:7]`. The licensed-by field for vibes:6 cites `proto:27, proto:26, proto:25` — note that vibes:6 is ANCHORED at @29 but its licensed-by points back to @27/@26/@25 (Wren-related filing beats from scene-B). The vibes content (mutual-silence from Wren's perspective: `not-approaching-as-active-decision-with-data, filed-without-contact-as-ledger-form-of-non-approach, ward-junction-entry-prior-to-any-word`) overlaps substantially with vibes:3 @27 (`ward-junction-contact-entered-without-consent, ledger-accepting-entries-without-approach`) — vibes:3 at @27 carries the same mutual-silence / filed-without-contact content. The target is different (`actor:wren-stitch-maker-flea-bottom-ward` vs `actor:taylor-hebert-kl-122ac`) so these are not same-target duplicates, but the observational content ("not-approaching-as-active-decision", "filed-without-contact") overlaps across targets. **SIGNAL:** cross-target vibes entries sharing the same observational frame at different anchors (@27 vs @29) are not structural duplicates but create render-register pile-up risk when stitcher deploys both. No HARD finding; advisory for Phase 5b audience review.

- [vibes:7] @29 and [vibes:5] @29 — both fire on `loc:oc-stitch-house-lane` at @29; vibes:5 (`coverage-edge-as-information: feed-limit-as-second-register-of-the-same-map, attenuation-as-boundary-not-failure`) and vibes:7 (`rising entrapment` on `actor:wren-stitch-maker-flea-bottom-ward`). Different targets (loc vs actor), different content. No DEDUP.

---

## SUPERFLUOUS findings (1)

- [loc-state:11] @44 — continuity-carry entry. The note reads `continuity-from loc-state:10: the shadow holds through the accounting — the drain angle stays dark as the ledger closes entry by entry`. The composite-state is `drain-angle-in-shade` — identical to loc-state:10's `drain-angle-in-shade`. Per URI-SCENE-RHYTHM, a continuity-carry entry requires (a) anchor inside a scene-map `fusion-eligible-runs` range, (b) rhythm-shape `flat-low`/`resolving`/`release-only`, (c) `<prior-loc-state-id>` resolves. Check: scene-C `fusion-eligible-runs: @44-@46`. Bone @44 IS inside the @44-@46 fusion run. Scene-C `rhythm-shape: peak-and-trail`. **Issue:** `peak-and-trail` is not in the licensed rhythm-shapes for continuity-carry (`flat-low`/`resolving`/`release-only`). However, the @44-@46 fusion run is the ledger-close denouement trailing the @40 peak — which functionally operates as the chapter's resolving tail. The carry-note also does not duplicate the prior entry's sensory note verbatim (adds "the drain angle stays dark as the ledger closes entry by entry", extending the prior "shadow-filled, drain-angle-in-shade"). The schema note says SIGNAL for `WARN-LOC-STATE-CONTINUITY-NO-INCREMENT` only when the carry-note duplicates verbatim; here it adds increment. The `peak-and-trail` rhythm-shape licensing issue is the residual concern.

  - id: fault-004
    type: flag
    what: loc-state:11 @44 is a continuity-carry entry on a scene with `rhythm-shape: peak-and-trail`; URI-SCENE-RHYTHM licenses continuity-carry only on `flat-low`/`resolving`/`release-only` rhythm-shapes
    why: the carry entry may be technically misplaced per the transition-run continuity license rule even though the functional context (ledger-close denouement) resembles a resolving tail
    criteria: advisory; the R2 judge did not flag this entry; the carry note adds increment over the prior entry; the anchor is inside the declared fusion-eligible-run. No fixer dispatch required — surfaced for Phase 5b audience review.

---

## CONSTRAINT findings (3)

- [state:8–17 back=N] — POV state-updates actor NI co-citation contract partially failed at cross-check. The state-updates file (actor slice) declares in its cross-facet contract: "POV actor-state requires narrator-interest co-citation at @11, @12, @15, @27, @40, @41, @42, @47." The R2 NI decision shard confirms all seven anchors carry NI spine post-R2 (narrator:2 @11, narrator:3 @12, narrator:13 @15, narrator:6 @27, narrator:8 @40, narrator:9 @41, narrator:10 @42). The co-citation contract is satisfied at the NI level. However, per the STRUCTURAL finding above (fault-001), the actor-state entries carry no `[state:N]` citation tokens on the proto-lines. This means the stitcher cannot resolve the NI co-citation contract at render time because the anchor tokens are missing. The NI entries are cited on proto-lines; the corresponding state entries are not. The cross-facet co-citation is asymmetric: NI → proto-lines ✓, state → proto-lines ✗.

  (This finding is subsumed by fault-001. No separate finding ID issued; co-citation note recorded here for completeness.)

- [exposition:1 @0, exposition:2 @0] — @0 anchor. The proto-lines file covers bones 1–47; @0 is not a bone ID in the proto-lines. The cite-index lists `exposition:1 @0 back=N` and `exposition:2 @0 back=N`. The exposition rubric explicitly licenses @0 as the preamble/episode-open anchor for `renders-as: italic-preamble` and `renders-as: preamble-paragraph` entries. The `back=N` is expected and correct: @0 entries do not decorate a proto-line, they render before the body. **PASS** — @0 is a licensed pre-body anchor for exposition; no constraint violation.

- [exposition:3 @14] — lone citation at @14 (no co-citations). The cite-index lists `exposition:3 @14 back=Y lic-out=[graph-resident-via-exposition:8, b01c01:5]`. The `lic-out` entries reference `graph-resident-via-exposition:8` and `b01c01:5` — these are cross-episode license references, not entries in the current chapter's facet files. They are not resolvable as `[<facet>:<id>]` tokens in the current graph. Per CONSTRAINT exposition license-completeness: every `licensed-by:` field must name ≥1 persona-card slug + a specific gap-claim. The exposition:3 entry's `licensed-by:` field in the exposition file reads: `cape-fic-doesnt-know-the-precinct-ward-geography-as-Hook-internal-structure (...)` — three persona-slug-anchored gap-claims, all resolving to named audience personas. **PASS** — the `lic-out` in the cite-index are traceability notations, not the `licensed-by:` content itself; the actual `licensed-by:` in the file satisfies the persona-slug requirement.

- [vibes:6] @29 back=N — The licensed-by field for vibes:6 cites `proto:27, proto:26, proto:25`. The cite-index rule requires `licensed-by:` to not forward-cite (cite a proto-line with a higher ID than the anchor). Vibes:6 is anchored at @29; its licensed-by references @25, @26, @27 — all lower IDs. No forward-cite issue; back-citations are licit. **PASS.**

- [narrator:7] deletion — R2 deleted narrator:7 @29. The cite-index shows the @29 proto-line carries no narrator citation (back=N for the deleted entry; the deletion cascade should have stripped `[narrator:7]` from the @29 proto-line token set). Confirm: bones @29 in proto-lines reads `the insects reach the junction-lane edge [loc-state:8] [vibes:5] [vibes:7]` — no `[narrator:7]` present. Cascade-strip executed correctly. **PASS.**

- Earth-Bet hard-fence scan — comprehensive substring scan across all text fields of all nine facet files for the canonical fence list (Brockton Bay, Skitter, Lung, Khepri, Bakuda, PRT, Endbringer, Gold Morning, Scion, Echidna, Behemoth, Leviathan, Simurgh, Cauldron, Coil, Tattletale, Grue, Regent, Imp, Aisha, Glaive, Glory Girl, Panacea, locker, trigger event, swarm-radius, parahuman, shard; Dance-specifics: aegon, rhaenyra, aemond, vhagar):
  - NI entries: no hits. "suppression-cost", "prohibition", "pre-calc", "ledger" — all clean.
  - Memory entries: target-ref slugs are `cond-road-to-hell-chain-shape`, `cond-override-architecture-residue-122ac`, `cond-kl-witch-label-formation-122ac` — no Earth-Bet proper-noun substrings.
  - State-updates (actor): field names (`coverage-mode`, `range-ceiling`, `prohibition-line`, `wren-recognition`, `moral_legibility_to_self`, `body-posture`, `coverage-map-state`) and values — no hits.
  - Vibes: entity targets include `actor:wren-stitch-maker-flea-bottom-ward` — no fence hits; wren is a Westerosi name. Keyword arrays: `cost-signature-range-bound`, `atonement-as-repetition`, `the-surveillance-recognized-and-filed`, `surveillance-anchor`, `coverage-edge-as-information`, `mutual-silence`, `rising entrapment`, `cold-utilitarian interiority`, `multi-day-coverage-weight`, `ward-junction-as-negative-space`, `surveillance-architecture-legible` — no hits.
  - Exposition: hard-fence audit block in the file confirms no hits; spot-verified across preamble texts.
  - Feeling, sensory, loc-state, metaphor, scene-map: all in physical/operational register; no hits.
  - **Earth-Bet hard-fence: CLEAN.**

- Scene-map coverage (URI-SCENE-WINDOW): scene-A @1–@14 (14 bones), scene-B @15–@29 (15 bones), scene-C @30–@47 (18 bones) = 47 total. Proto-lines covers 1–47. No gaps, no overlaps. Frontmatter `total-scenes: 3`, `total-bones: 47` match body. Dangling-anchor check: @1, @14, @15, @29, @30, @47 all resolve in proto-lines. **Scene-map coverage: CLEAN.**

- Dialogue coverage (URI-DIALOGUE-COVERAGE-GATE upstream sanity check): exposition:2 dialogue-adjacent fence audit confirms SPEECH-BONE SET = ∅. No `[<character-slug>:<id>]` tokens on any proto-line. No speaker files expected. **Dialogue-coverage sanity check: CLEAN.**

- First-mention-character coverage (CONSTRAINT § exposition): walk proto-lines for named individuals in narrator prose appearing for the first time. Bones text: `taylor-hebert-kl-122ac` (POV character — exempt), `the ward-junction body` / `the junction-body` / `the ward-junction contact` (all function-labels for Wren; the not-knowing contract deliberately withholds the character-name introduction; this is documented in exposition R1 DROP candidate-d and R2 exposition add-cap confirmation). No other named individual or definite description of a new individual appears in narrator prose across the 47 bones. **First-mention-character coverage: PASS** (no qualifying introduction found outside the deliberate not-knowing Wren case, which the exposition R1/R2 judge explicitly reviewed and approved).

---

## AP-SCAN findings (2)

- [narrator:3] @12 and [narrator:10] @42 — AP10 chassis-recurrence (definitional-collapse construction: "is the same prohibition" / "is the same line ... in the same hand"). R2 NI judge assessed these as the load-bearing prohibition-twice pair and defended them as substance (the second drawing IS the chapter's central reading: atonement-as-repetition, architecture-self-sealing-at-the-second-drawing). The deleted narrator:7 was the non-substance third instance. Post-deletion: 2 instances of the AP10 template remain. Per URI-AP-SCAN-SATURATION: saturation fires at ≥40% of entries in a ≤25% density facet. NI has 12 entries; 2/12 = 16.7% AP10 hits — below the 40% saturation threshold. **SIGNAL** (advisory): the pair remains an audience-attack candidate. Defended by monument co-citation (mem:1 / mem:3) and structural function (the chapter's callback pair). Carry to Phase 5b.

  - id: fault-005
    type: flag
    what: narrator:3 @12 ("is the same prohibition she set herself") and narrator:10 @42 ("is the same line she drew at the alley-mouth; she draws it now in the same hand") share the AP10 definitional-collapse chassis
    why: at 16.7% of NI entries the pair is below saturation threshold; defended as substance by R2 with monument co-citation; surfaced as audience-attack candidate for Phase 5b
    criteria: advisory only; no fixer dispatch required

- [mem:1] @12 and [mem:3] @42 — AP12 author-vocabulary-leak soft watch. Both entries share "line" + future-naming construction (mem:1: "line that will be asked of her again"; mem:3: "shape of this line is what a watching street will find a word for"). R2 memory judge documented the soft watch in the file header — distinct monument families (chain-shape vs witch-label), distinct scenes (A vs C), within-tolerance for single-chapter. Not elevated to AP12 violation; carry-forward as parking-lot watch for next-chapter author.

  - id: fault-006
    type: flag
    what: mem:1 @12 and mem:3 @42 share "line" + future-projection construction across two Westerosi-monument clamp entries
    why: AP12 soft watch documented by R2 — a third occurrence in c03 would escalate to actionable; surfaced here to confirm carry-forward
    criteria: advisory only; no fixer dispatch required. Parking-lot item for c03 authoring.

---

## TASTE-FLAG findings (2)

- [vibes:6] @29 (`actor:wren-stitch-maker-flea-bottom-ward ++ mutual-silence`) and [vibes:7] @29 (`actor:wren-stitch-maker-flea-bottom-ward ++ rising entrapment`) — two vibes entries on a non-POV character at the same anchor, both with Wren as target. The chapter's discipline is that Wren is a function-label, not a character in Taylor's interiority. Two ++ (strong) vibes entries targeting Wren's subjective experience at a single anchor (both back=N, meaning the proto-line carries no citation for either) create a reader-legibility risk: the stitcher fires both vibes on the same bone, and both carry register-claims about Wren's interiority ("not-approaching-as-active-decision-with-data" implies Wren's volition; "free-movement-as-what-the-map-reads-as-pattern" implies Wren's freedom). These register-claims are outside Taylor's POV scope and visible only to the reader through the narrative irony layer. **TASTE-FLAG: atmosphere-thin / voice-fidelity.** Risk that rendering both vibes entries at @29 signals Wren's subjective state in a chapter that is deliberately silent about it. Carry to Phase 5b.

  - id: fault-007
    type: flag
    what: vibes:6 @29 and vibes:7 @29 both target actor:wren-stitch-maker-flea-bottom-ward with strong-register (++) entries; neither is cited on the proto-line (back=N); both claim Wren's subjective state in a chapter whose POV discipline forbids Taylor from having access to that state
    why: dual ++ vibes on a non-POV character at the same anchor may leak narrative irony too explicitly; voice-fidelity concern for Phase 5b
    criteria: advisory; no fixer dispatch required

- [exposition:4] @15 ("Days of it, and the pattern came.") — the pov-frame register is defensible (R2 validated) but the entry is a single five-word sentence whose register sits at the border between scene-bridge and authorial-voice intrusion. The absence of a first-person pronoun while functioning as Taylor's perception-of-elapsed-time was flagged by R2 as precedent-based acceptance. **TASTE-FLAG: voice-fidelity.** Carry to Phase 5b for worm-canon-pedant audience review.

  - id: fault-008
    type: flag
    what: exposition:4 @15 "Days of it, and the pattern came." — pov-frame third-person bridge without explicit first-person pronoun; R2 accepted via precedent but the construction is an audience-attack candidate for voice-fidelity
    why: worm-canon-pedant may read this as authorial voice rather than Taylor's perception; the chapter is strict first-person Taylor throughout
    criteria: advisory only; no fixer dispatch required

---

## PILE-UP REVIEW (2)

- @11 (6 facets: loc-state:3, narrator:2, state:1, state:2, state:4, vibes:1) — `taylor-hebert-kl-122ac extends the range`. **Verdict: warranted.** This is the scene-A peak-bone declared in the scene-map. loc-state:3 transitions to Hook-wide coverage; narrator:2 carries the somatic suppression-cost; state:1 (coverage-mode flip), state:2 (range-ceiling flip), state:4 (wren-recognition initiation) are distinct field-changes on distinct state axes; vibes:1 opens the cost-signature-range-bound register. Each entry carries a distinct channel; no two entries render the same information. The scene-A peak at a range-extension moment structurally warrants multi-facet coverage.

- @27 (6 facets: mem:2, narrator:6, state:5, vibes:3, vibes:4, vibes:6) — `the insects file the ward-junction contact`. **Verdict: warranted with notation.** This is the scene-B peak-bone (relational_anchor_status +1.0). mem:2 carries the Earth-Bet displacement cue; narrator:6 carries the clinical filing-without-contact register; state:5 marks the wren-recognition flip; vibes:3 carries the surveillance-recognized-and-filed episode register; vibes:4 carries the surveillance-anchor location register. Each carries distinct content. vibes:6 back=N (not cited on proto-line) and its licensed-by points to @25–@27 — the entry targets Wren's interiority (mutual-silence), which creates the voice-fidelity concern flagged above (fault-007). The five-entry warranted pile-up plus one uncited vibes entry targeting non-POV interiority = warranted with the notation that vibes:6 is the over-decoration risk.

---

## RUBRIC-FIDELITY findings (1)

- [loc-state:11] @44 — rhythm-shape licensing for continuity-carry. URI-SCENE-RHYTHM requires continuity-carry entries to fire on scenes with `rhythm-shape: flat-low | resolving | release-only`. Scene-C is declared `rhythm-shape: peak-and-trail`. The entry is inside the `fusion-eligible-runs: @44-@46` window, satisfying condition (a). The prior-loc-state-id (`loc-state:10`) resolves, satisfying condition (c). No other continuity-carry in the same fusion-eligible-run, satisfying condition (d). But the rhythm-shape check (b) fails: `peak-and-trail` is not a licensed shape for continuity-carry.

  - id: fault-009
    type: flag
    what: loc-state:11 @44 is a continuity-carry entry (`continuity-from loc-state:10`) anchored in scene-C whose `rhythm-shape: peak-and-trail`; URI-SCENE-RHYTHM licenses continuity-carry only on `flat-low | resolving | release-only` rhythm-shapes
    why: the rubric-fidelity check fires HARD on rhythm-shape licensing; however, the @44-@46 fusion-eligible-run is the chapter's denouement tail after the @40 peak, which functions as a resolving register even under `peak-and-trail` labeling. The finding is recorded as HARD per mechanical rule but the functional context argues for Signal treatment.
    criteria: fixer must either (a) confirm the rhythm-shape for the @44-@46 sub-window should be re-declared as `resolving` in the scene-map (upstream fix via /and-write revise), or (b) convert loc-state:11 from a continuity-carry entry to a standalone entry with its own sensory note — the content is already incremental ("the drain angle stays dark as the ledger closes entry by entry"); re-authoring as standalone loc-state removes the continuity-carry constraint

- Per-facet ACCEPT signature scan:
  - loc-state anchor verbs: @3 `leaves` (transitional), @7 `takes` (positioning), @11 `extends` (transitional), @13 `fill` (descriptive event), @16 `marks` (transitional), @20 `takes` (positioning), @22 `admits` (transitional), @29 `reach` (transitional), @30 `takes` (positioning), @32 `fills` (descriptive event), @44 `closes` (event). All within the transitional/positioning/event ACCEPT class. No REJECT-verb candidates found.
  - state-updates registration-vocabulary check: actor-slice field values scanned for `noticed`, `registered`, `awareness`, `baseline-new-faces` in `<new>` values. Finding: `state:11 @15: wren-recognition: unaware -> registered-as-junction-body`. The `<new>` value contains the substring `registered`. This is exactly the registration-vocabulary anti-pattern flagged in RUBRIC-FIDELITY class (a): state-updates `<new>` value containing registration vocabulary on an actor extension-field. **However**, the state-updates actor-slice carries an explicit rubric-carve-out preamble: "Carve-out rule: the field tracks operational categorization of Wren in Taylor's coverage-map ledger (a tracked knowledge-state extension), not Taylor's perceptual noticing. Vocabulary is operational/structural (registered-as-junction-body, filed-as-ward-junction-contact) per prompt directive forbidding `noticed`/`registered`/`awareness`/`baseline-new-faces` registration-as-state vocabulary. The 'registered' prefix in the value-string is operational-ledger-state, not perception."

    - id: fault-010
      type: flag
      what: state:11 @15 value `registered-as-junction-body` contains the substring `registered` — triggers the registration-vocabulary REJECT signature scan; carve-out preamble in the file defends this as operational-ledger-vocabulary
      why: mechanical REJECT-signature scan fires on the substring regardless of intent; the carve-out defense is present and coherent but relies on reading the preamble, which the stitcher and future auditors must do to avoid false-positive deletions
      criteria: advisory; carve-out defense is present and documented; no fixer dispatch required. If the stitcher ever applies a regex-based drop on `registered` in state-update values, this entry would be silently removed. Consider renaming the field value to `entered-as-junction-body` or `ledger-typed-as-junction-body` to remove the substring ambiguity at a future chapter revision.

  - memory doubled-register test: 1 Earth-Bet displacement fire (mem:2 @27) + 2 Westerosi-monument clamp fires (mem:1 @12, mem:3 @42). Doubled-register gate: PASS.
  - sensory modality floor: sensory:1 smell + sensory:2 light = 2 distinct modalities. Floor is ≥2. At 2/47 and 2 modalities, this sits exactly at both the density floor and the modality floor. **SIGNAL:** no single modality exceeds 67% of fires (each modality = 50%); dominance ceiling is 67% for ≥3 fires; at total fires = 2 the ceiling cannot trigger. Modality distribution: PASS.

---

## Audit summary

- Total entries reviewed: 63 facet entries + 47 proto-lines + scene-map (3 scenes)
- HARD classes: STRUCTURAL (fault-001: actor-state back=N systematic miss on proto-lines citation); RUBRIC-FIDELITY (fault-009: loc-state:11 continuity-carry rhythm-shape licensing fail)
- SIGNAL classes: FREQUENCY-BAND (NI 25.5% at ceiling; exposition 8.5% above sparsity-ratio band; feeling 2.1% at floor); METADATA-INCONSISTENCY (metaphor shard episode mismatch; slug format variance); AP-SCAN (narrator:3/10 AP10 pair defended; mem:1/3 AP12 soft watch); TASTE-FLAG (vibes:6/7 @29 Wren-interiority dual++; exposition:4 @15 pronoun-absent bridge); PILE-UP (both warranted, vibes:6 notation)
- CURVE-SHAPE: SHAPE-OK

**HARD count: 2**
**SIGNAL count: 8**
**Headline: FINDINGS-PRESENT**

Phase 5 gate: HARD > 0. Phase 5b must not fire until fault-001 and fault-009 are resolved.

## Routing

- **fault-001** → fixer, routes to build_cite_index operator / proto-lines file: add `[state:8]` and `[state:9]` to @11, `[state:10]` to @12, `[state:11]` to @15, `[state:12]` to @27, `[state:13]` to @40, `[state:14]` to @41, `[state:15]` to @42, `[state:16]` to @43, `[state:17]` to @47 in `active-project/theater/proto-lines/b01-c02.md`; rebuild cite-index.
- **fault-009** → fixer, routes to studio (loc-state author) OR upstream to /and-write revise for scene-map rhythm-shape re-declaration on @44–@46 sub-window; minimum change is converting loc-state:11 to standalone entry.
- **fault-002** (flag) → no fixer dispatch; provenance note for metaphor shard in .r2-decisions.md.
- **fault-003** (flag) → no fixer dispatch; slug normalization advisory.
- **fault-004** (flag) → no fixer dispatch; carry to Phase 5b.
- **fault-005** (flag) → carry to Phase 5b audience review.
- **fault-006** (flag) → parking-lot item for c03 authoring.
- **fault-007** (flag) → carry to Phase 5b audience review (voice-fidelity gate).
- **fault-008** (flag) → carry to Phase 5b (worm-canon-pedant review).
- **fault-010** (flag) → no fixer dispatch; registration-vocabulary substring advisory.
