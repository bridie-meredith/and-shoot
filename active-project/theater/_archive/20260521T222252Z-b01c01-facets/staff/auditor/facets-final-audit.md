---
audit: facets-final-r1
episode: b01-c01
date: 2026-05-20
mode: flag-only
status: FINDINGS-PRESENT
totals: 21 findings across 9 facets and 1 cross-facet surface
---

## STRUCTURAL findings (5)

- [interest-narrator:--] — episode-slug-inconsistency — File header reads `episode: b01-c01` (hyphenated). Canonical episode slug per bones-file header and showrunner memory is `b01c01` (unhyphenated). The cite-index header also uses `b01-c01`. Bones file, scene-map, and showrunner memory all use `b01c01`. Inconsistent slug surface; cross-episode register lookups keying on this string may resolve incorrectly. SIGNAL.

- [state-updates:--] — episode-slug-inconsistency and stale-sub-header — Per-source slice headers for coll, taylor, and wren slices each read `episode: b01-c01` (hyphenated vs canonical `b01c01`). The top-level consolidated frontmatter carries no `episode:` field. Additionally, the `env` sub-header at line 9 retains `facet: state-updates-env` — a pre-consolidation label; the canonical post-consolidation label is `facet: state-updates`. SIGNAL.

- [dialogue:coll:--] — episode-slug-inconsistency — `coll-net-mender-flea-bottom.md` header reads `episode: b01-c01`. The peer files `taylor-hebert-kl-122ac.md` and `wren-stitch-maker-flea-bottom-ward.md` both read `episode: b01c01`. Three dialogue files for the same chapter carry two distinct episode slug formats. SIGNAL.

- [memory:--] — R2-shard-anchor-mismatch — The R2 decision shard reviewed entries labeled `mem:1 @15` and `mem:2 @23`. The locked canonical `memory.md` contains `mem:1 @9` and `mem:2 @18`. Anchor, content, and co-citations differ completely between the shard's reviewed entries and the on-disk canonical entries. The `.r2-decisions.md` graph-reconciliation note acknowledges this and zeroes f-r2-counts on the basis that un-enacted adds produced no in-file pathology. However, the shard's KEEP verdicts do not constitute R2 review of the actual canonical entries: `mem:1 @9` and `mem:2 @18` have not been verified by any R2 judge against the locked graph. SIGNAL.

- [interest-narrator:--] — R2-shard-anchor-mismatch — The R2 NI shard reviewed entries labeled narrator:1 @1, narrator:2 @8, narrator:3 @12, narrator:4 @15, narrator:5 @21, narrator:6 @24. The locked canonical `interest-narrator.md` contains entries at anchors @4, @6, @15, @18, @22, @27 respectively. Four of six anchors do not match. Only the shard's narrator:4 @15 shares an anchor with a canonical entry (@15 = canonical entry 3). The shard's KEEP verdicts do not cover the canonical entries at @4, @6, @18, @22, @27. Same structural failure as the memory shard: R2 review obligation for the on-disk NI entries is unsatisfied at those anchors. SIGNAL.

---

## FREQUENCY-BAND findings (3)

- sensory: actual 2/27 = 7.4%; band ceiling 6%. Breach-high by 1 entry. The integer floor at 6% on 27 bones yields a fractional max of 1.62; the minimum non-zero integer above the ceiling is 2. This is a single-entry arithmetic breach. SIGNAL: `[sensory:--] 7.4% vs ceiling 6%; breach-high; breach is integer-floor arithmetic on a 27-bone chapter.`

- feeling:taylor: actual 2/27 = 7.4% for the taylor-hebert-kl-122ac character slice; per-character band ceiling 5%. Breach-high by 1 entry. Same integer-floor condition as sensory. SIGNAL: `[feel:taylor:--] 7.4% (2 entries) vs ceiling 5%; breach-high; same integer-floor arithmetic.`

- exposition: actual 6 in-body entries (2 preamble at @0 + 4 anchored in prose) = 22.2% against 27 bones; descriptive band 1-5%. Cold-start override asserted by both R1 and R2 authors: chapter 1 of 18 carries mandatory preamble + three first-mention glosses + two scene-orient candidates. Rubric's authoritative caps (episode-open ≤4; first-mention ≤12; scene-open-orient ≤1/scene) are respected. Flagged advisory: SIGNAL. `[exposition:--] 22.2% vs descriptive band 1-5%; cold-start override defense accepted per integer caps; flag for downstream chapter comparison to confirm cold-start does not normalize a higher baseline.`

---

## METADATA-INCONSISTENCY findings (2)

- [.r2-decisions.md:--] — shard-ADD-not-classified — The metaphor R2 shard declares `VERDICT: ADD` for `meta:1 @23` and the NI R2 shard declares `VERDICT: ADD` for `narrator:7 @23`. Both adds reference spine-anchors that do not exist in the locked graph (`feel:1 @23` and `vibes:17 @23` — the locked graph has feel:1 @9 and vibes:17 @22). The graph-reconciliation note correctly identifies the non-enactment. The f-r2-counts zeroing is justified. However, the shard ADD verdicts are preserved verbatim in the consolidated file and not marked as non-enacted in the shard body — a reader of the shards sees two ADD verdicts that never produced entries. No in-file pathology, but the shard record is misleading without a per-shard non-enactment annotation. SIGNAL.

- [state-updates:--] — wren-slice-fence-format — The wren source slice at lines 77-81 of state-updates.md begins with `# source: wren-stitch-maker-flea-bottom-ward` followed immediately by `facet: state-updates` without an enclosing `---` fence. The prior coll and taylor slices each open with `---` before their sub-header fields. The wren slice sub-header is unfenced, making its attribution lines syntactically ambiguous (markdown comment vs YAML). SIGNAL.

---

## CURVE-SHAPE verdict

- Episode-level: SHAPE-CHECK — Chapter declared `dramatic_shape: hinge` in showrunner memory, reviewed and accepted by dramatist at Phase 5. The scene-map shows all three scenes as `rhythm-shape: flat-low` with `peak-bones: none` in every scene. The CURVE-SHAPE class definition requires a hinge chapter to show "scene-level flat-low zones building toward a peak-bones hinge beat with resolving afterward." No peak-bones beat exists anywhere. The hinge label is being used in the narrative-dramatic sense (baseline-placement chapter; the conditions for future hinge events established here) rather than the pressure-signal sense (a peak-bones bone mid-chapter). The usage is coherent with the substance contract — a chapter whose highest single-bone magnitude is 0.05 cannot produce peak-bones under the scene-map algorithm's 0.15 threshold — but it diverges from the CURVE-SHAPE class's pressure-signal vocabulary. Advisory: the dramatist-accepted `dramatic_shape: hinge` label and the scene-map's all-flat-low profile are structurally reconcilable only if `hinge` is understood as a narrative-shape term rather than a peak-bones pressure term. Flag for the rubric authority to resolve the vocabulary collision.

- Per-scene: scene-A flat-low / no peak, scene-B flat-low / no peak, scene-C flat-low / no peak.

- Adjacency: no 1→3 jumps possible (no peak-bones exist). No 3→3 sequences.

- Flatlining: 27 contiguous flat-low bones (entire chapter). Structurally consistent with declared purpose; not a deficit given the substance contract.

---

## CONTRADICTION findings (0)

State-update sequences verified for `<old>` / `<new>` chain integrity. No incompatible-state pairs detected. Needle cycles, Wren location transitions, and Coll work-state transitions all check out as internally consistent.

---

## DEDUP findings (2)

- [vibes:20] @25 — dual-anchor citation — The vibes file declares `20 @25` (anchor is proto-line 25). The cite-index records `lic-out=[proto:25, proto:27]`, and the canonical proto-lines file carries `[vibes:20]` at both @25 and @27. The vibes schema defines one `@<proto-line-id>` anchor per entry — a single-point fire, not a range. Proto @27 citing `[vibes:20]` when the entry's anchor is @25 is an off-anchor citation. SIGNAL: `[vibes:20] @25 — vibes-dual-anchor — proto:27 cites vibes:20 whose declared anchor is @25; either a stale citation or an unsupported range-fire pattern.`

- [vibes:10] @4 — dual-anchor citation — Same pattern. Vibes:10 is declared `@4`; cite-index records `lic-out=[proto:4, proto:5]`; canonical proto-lines file shows `[vibes:10]` at both @4 and @5. SIGNAL: `[vibes:10] @4 — vibes-dual-anchor — proto:5 cites vibes:10 whose declared anchor is @4; same off-anchor citation pattern as vibes:20.`

---

## SUPERFLUOUS findings (0)

Cite-index lonely candidates evaluated:

- state:7 @12: no co-citations. Rubric three-axis test: necessity passes — state:7 establishes `coll.work-state: between-days -> at-work-on-net`; this `<old>` value is required for state:8's `at-work-on-net -> day-packed-net-folded` close at @20 to be valid. The state-gate function is preserved. PASS.

- vibes:16 @19 and vibes:19 @24: both in scene-C, which is flat-low. Per the SUPERFLUOUS class definition, "bones in rhythm-shape: flat-low zones... are never superfluous." Both PASS on the flat-low carve-out.

- exposition:1 @0 and exposition:2 @0: both are `@0` synthetic-anchor preamble entries. Back=N is expected and correct for pre-body preamble scope. The `@0` anchor is specifically exempt from the loneliness test — preamble entries do not decorate proto-lines. Both PASS.

---

## CONSTRAINT findings (6)

- [memory:1] @9 — HARD — NI-spine-absent — `mem:1 @9` ("the feet hold and the architecture stays the shape she will not build") has co-citations `[feel:1, vibes:12]` but no NI entry. The canonical NI file has no entry at @9; nearest NI entries are at @6 and @15. The cross-facet contract requires a co-cited NI entry on the same beat as a memory entry. Feel:1 @9 is co-present, which provides partial defense (the R2 memory shard argued feeling-as-spine is acceptable when the substance is interior-feeling-of-rule-catching), but that defense was argued by the shard for its `mem:2 @23` entry — not for the canonical `mem:1 @9`. No R2 judge reviewed the canonical mem:1 @9 entry (see STRUCTURAL finding: R2-shard-anchor-mismatch). No documented defense exists for the canonical entry. HARD: `[memory:1] @9 — constraint-memory-no-NI-spine — narrator-interest absent at @9; feel:1 co-cited but no R2-verified NI-spine defense on record for this canonical entry.`

- [exposition:4] @11 — HARD — scene-orient-fire-rule — `exposition:4` is a `scope: scene-open-orient` entry at @11 (`The next morning, the working day.`). Fire-rule condition (b): "loc-state does NOT fire at the scene-open anchor." The cite-index shows `loc-state:3 @11` — loc-state fires at @11. Condition (b) is violated: the lens covers the scene orientation, so exposition must not fire. The R2 exposition shard correctly concluded the refusal stands ("Both refusals are correct against the locked graph. No scene-open-orient fires this chapter."), but the on-disk canonical exposition file still contains exposition:4 as a live entry. The R2 judgment that this entry should not exist was not executed as a delete. HARD: `[exposition:4] @11 — constraint-exposition-scene-orient-fire-rule — condition (b) violated: loc-state:3 fires at @11; scene-open-orient must not fire when loc-state covers the anchor; R2 judged the refusal correct but did not execute the delete.`

- [exposition:7] @22 — HARD — scene-orient-fire-rule — `exposition:7` is a `scope: scene-open-orient` entry at @22 (`On the third or fourth day, near evening.`). Condition (b): `loc-state:5 @22` is present. Condition (b) violated. Same analysis as exposition:4 above. The R2 shard again concluded the refusal stands; the on-disk file retains the entry. HARD: `[exposition:7] @22 — constraint-exposition-scene-orient-fire-rule — condition (b) violated: loc-state:5 fires at @22; same failure mode as exposition:4.`

- [exposition:5, exposition:6] @18 — HARD — per-anchor-cap — Two exposition entries at @18: exposition:5 is `scope: first-mention-term` (the-city-watch) and exposition:6 is `scope: first-mention-place` (the-hook). The schema's per-anchor-cap rule states: "Multiple exposition entries on the same anchor are permitted only as one of these pairs: episode-open-* + scene-open-orient, scene-open-orient + first-mention-*, episode-open-* + first-mention-*. No two entries of the same scope on the same anchor." The pair `first-mention-term + first-mention-place` does not appear in the permitted pairs enumeration. HARD: `[exposition:5, exposition:6] @18 — constraint-exposition-per-anchor-cap — first-mention-term + first-mention-place pair not in the permitted-pairs enumeration; cap breach.`

- [vibes:10] @4 — SIGNAL — dual-anchor citation — Covered under DEDUP. The CONSTRAINT class fires this also as a forward-citing or off-anchor vibes entry: vibes:10 licenses proto:5 via the cite-index but the entry's declared anchor is @4. If proto:5 is "forward" from the declared anchor @4, the vibes schema requirement "no forward-citing licensed-by" may apply depending on interpretation. If `lic-out` represents post-authored citation accumulation rather than the author's declared license, this is a citation-tool artifact rather than an authoring fault. SIGNAL advisory.

- [feel:2, feel:3] @27 — PASS — per-character per-scene cap check — feel:2 is taylor (@27, scene-C) and feel:3 is wren (@27, scene-C). Taylor's scene-C count: 1 (feel:2 only; feel:1 is @9 in scene-A). Wren's scene-C count: 1 (feel:3 only). Both within ≤1 per character per scene. No finding.

---

## AP-SCAN findings (2)

- [interest-narrator:--] @6/@18/@27 — HARD — AP-template-saturation — Construction `"X is what Y"` (predicate-nominative inversion) appears at: entry 2 @6 (`"useful without controlling is what the threshold means today"`), entry 4 @18 (`"the cost of being legible is what she counts"`), entry 6 @27 (`"face, not node, is what she holds"`). Three hits in 6 entries = 50%. URI-AP-SCAN-SATURATION threshold: hits/total ≥ 0.40 in a facet whose FREQUENCY-BAND ceiling is ≤ 25%. NI band ceiling is 25%; 50% > 40%. Escalates to HARD. The R2 NI shard self-flagged this pattern as "on the edge" but did not act. HARD: `[interest-narrator:--] AP-template-saturation — "X is what Y" construction 3/6 entries (50%) in NI (band 15-25%; saturation threshold 40%); URI-AP-SCAN-SATURATION escalates to HARD.`

- [state:11] @6 — SIGNAL — AP-registration-vocabulary — `actor:taylor-hebert-kl-122ac.knowledge.flea-bottom-geometry: arrival-baseline -> hook-block-route-mapped`. The `<old>` field value `arrival-baseline` contains the registration-vocabulary term "baseline." The RUBRIC-FIDELITY class applies its check more precisely; noted here as an AP-SCAN advisory. The state-author's cull-notes show `arrival-baseline` is a deliberate semantic marker for the starting knowledge state (not a perception-registration) — the defense may hold. SIGNAL advisory.

---

## TASTE-FLAG findings (2)

- [interest-narrator:1] @4 — atmosphere-thin — Entry 1 @4: `"the network has him before he has her."` The noun phrase "the network" labels the insect-feed as a proper-noun-class entity. The chapter's declared register is "Khepri-haunted without naming Khepri" (showrunner memory chapter chunk). "The network" as a named-entity label is adjacent to the Worm-canon metonym that the Earth-Bet hard fence and capability-dormant register are suppressing. Not a hard-fence violation (no canonical Earth-Bet proper noun substring), but cape-fic-reader and worm-canon-pedant may read the label as sufficiently close to the boundary to disrupt the chapter's register discipline. SIGNAL.

- [exposition:1] @0 — voice-fidelity — Preamble text: `"I am twenty years old by the calendar I came in with."` The clause "the calendar I came in with" frames Taylor's transit from another world in a reader-address register — she is explaining to a reader that she arrived from elsewhere. This borders on the `cond-taylor-pov-behavior §Theme Silence` rule ("she does not narrate her arc from above her own perspective"). The preamble's `voice: pov-frame first-person` declaration positions this as interior monologue, but "the calendar I came in with" is structurally a narrator-to-reader orientation statement, not a first-person interior reflection. SIGNAL.

---

## PILE-UP REVIEW (3)

- @18 (6 facets: exposition:5, exposition:6, loc-state:4, mem:2, narrator:4, vibes:15) — `the city-watch passes the hook` — verdict: **warranted**. The Watch passage is the chapter's sole external institutional-pressure event. Each of the six co-located facets serves a distinct function: NI:4 is the interior cost-ledger; loc-state:4 grounds the physical scene; mem:2 provides the displacement callback; vibes:15 ties to the gallows-calendar vibe-cloud; exposition:5 and :6 are first-mention glosses for the Watch institution and the Hook toponym. Note: the exposition:5+:6 per-anchor-cap violation (see CONSTRAINT above) is a schema fault independent of the pile-up warrant. The decoration density is earned; the cap issue is a citation-schema error.

- @22 (6 facets: exposition:7, exposition:8, loc-state:5, narrator:5, state:19, vibes:17) — `wren-stitch-maker-flea-bottom-ward enters the street` — verdict: **warranted**. Wren's first physical appearance is the chapter's most load-bearing single bone: cost-bearer introduction, scene-C open, multi-day skip, new character. The six facets serve distinct loads: loc-state:5 establishes the new scene; NI:5 registers the approach geometry; exposition:7 is the scene-open-orient (see CONSTRAINT: fire-rule violation — present in file but should have been deleted); exposition:8 is the first-mention-character gloss for Wren; state:19 registers Wren's location-entry; vibes:17 ties Wren to the observation-inventory vibe register. The pile-up is warranted at the narrative level; exposition:7 is a constraint error within it.

- @27 (5 facets: feel:2, feel:3, narrator:6, vibes:20, vibes:21) — `taylor-hebert-kl-122ac holds the eyes` — verdict: **warranted**. Chapter's closing moment: Taylor holds Wren's gaze without completing the assessment. Five facets carry distinct loads: NI:6 (prohibition-catch interior); feel:2 (Taylor's somatic hold); feel:3 (Wren's somatic attention); vibes:20 (atonement-register at first-contact-with-cost-bearer); vibes:21 (ledger-gap-begins). The two feeling entries are for different characters, explicitly permitted. Warranted.

---

## RUBRIC-FIDELITY findings (3)

- [exposition:4] @11 — rubric-fidelity-scene-orient-fire-rule — HARD (same as CONSTRAINT finding above; routing here for completeness). Rubric source: `rubric-exposition.md § Scene-open-orient conditional fire-rule`, condition (b). The R2 judge correctly identified the refusal but did not execute the delete. The failure lies in the R1→canonical-file pipeline: an entry authored as a conditional R2-refuse candidate survived into the locked graph.

- [exposition:7] @22 — rubric-fidelity-scene-orient-fire-rule — HARD (same as CONSTRAINT finding above). Same rubric source and same R2-delete-not-executed failure mode.

- [state-updates:--] file — HARD — rubric-fidelity-cross-facet-co-citation — Rubric source: `rubric-state-updates.md § Cross-facet contract` — every `actor:<POV>.*` state entry must pair with a narrator-interest entry on the same beat. Scanning all `actor:taylor-hebert-kl-122ac.*` entries against the NI file (NI fires at @4, @6, @15, @18, @22, @27): state:9 @1 — no NI at @1; state:10 @2 — no NI at @2; state:12 @7 — no NI at @7; state:14 @13 — no NI at @13; state:15 @20 — no NI at @20; state:16 @20 — no NI at @20; state:17 @25 — no NI at @25; state:18 @29 — no NI at @29. Only state:11 @6 is co-cited with NI (narrator:2 @6). Eight of nine taylor-state entries lack NI co-citation. HARD: `[state-updates:--] file — rubric-fidelity-cross-facet-co-citation — POV-actor state-updates (actor:taylor-hebert-kl-122ac.*) missing NI co-citation on 8 of 9 entries at @1, @2, @7, @13, @20(×2), @25, @29. Rubric-state-updates.md § Cross-facet contract mandates the pair.`

---

## Audit summary

**Total entries reviewed:** 70 facet entries (5 loc-state + 6 NI + 2 sensory + 22 state + 2 memory + 3 feeling + 0 metaphor + 22 vibes + 8 exposition) + 4 dialogue entries (coll:1, taylor:1, wren:1+2) + scene-map (3 scenes / 27 bones).

**HARD findings count:** 6
- CONSTRAINT: 4 (memory:1 NI-spine-absent; exposition:4 scene-orient; exposition:7 scene-orient; exposition:5+6 per-anchor-cap)
- AP-SCAN: 1 (NI template saturation per URI-AP-SCAN-SATURATION)
- RUBRIC-FIDELITY: 1 file-level (state-updates POV co-citation gap; exposition:4+7 already counted under CONSTRAINT)

**SIGNAL findings count:** 15
- STRUCTURAL: 5 (slug inconsistencies ×3; R2-shard-anchor-mismatch ×2)
- FREQUENCY-BAND: 3 (sensory breach-high; feel:taylor breach-high; exposition cold-start advisory)
- METADATA-INCONSISTENCY: 2 (shard ADD non-enactment annotation gap; wren-slice fence format)
- CURVE-SHAPE: 1 (SHAPE-CHECK advisory)
- DEDUP: 2 (vibes:20 dual-anchor; vibes:10 dual-anchor)
- SUPERFLUOUS: 0 (all lonely candidates pass)
- CONSTRAINT: 1 (vibes:10 dual-anchor advisory)
- AP-SCAN: 1 (registration-vocabulary advisory)
- TASTE-FLAG: 2 (atmosphere-thin at NI:1; voice-fidelity at exposition:1)
- PILE-UP REVIEW: 0 findings (all 3 pile-ups warranted)
- RUBRIC-FIDELITY SIGNAL: 0 additional (the two exposition rubric-fidelity findings are already HARD under CONSTRAINT)

**CURVE-SHAPE:** SHAPE-CHECK (advisory; narrative-vs-pressure-signal vocabulary collision on `hinge` label; not a production block)

**Phase 5b gate:** HARD = 6. Phase 5b CANNOT fire. Fixer dispatch required before Phase 5b.

---

## Routing

| ID | Finding | Class | Severity | Route to |
|---|---|---|---|---|
| F-001 | memory:1 @9 — NI-spine-absent | CONSTRAINT | HARD | taylor-hebert-kl-122ac (memory fork); requires either NI entry at @9 or documented feeling-as-spine R2 defense for the canonical entry |
| F-002 | exposition:4 @11 — scene-orient-fire-rule | CONSTRAINT | HARD | exposition-author; delete exposition:4 (loc-state:3 covers @11) |
| F-003 | exposition:7 @22 — scene-orient-fire-rule | CONSTRAINT | HARD | exposition-author; delete exposition:7 (loc-state:5 covers @22) |
| F-004 | exposition:5+6 @18 — per-anchor-cap | CONSTRAINT | HARD | exposition-author; one of the two first-mention entries at @18 must be moved to an adjacent anchor or the pair reconciled to a permitted scope combination |
| F-005 | NI AP-template-saturation — "X is what Y" 3/6 | AP-SCAN | HARD | taylor-hebert-kl-122ac (NI impersonator); revise at least one of the three identically-constructed entries |
| F-006 | state-updates file — POV co-citation gap 8/9 | RUBRIC-FIDELITY | HARD | taylor-hebert-kl-122ac (state-updates fork) and/or NI impersonator; NI entries must be added at uncovered taylor-state anchors, or state entries must be reconciled to existing NI coverage |
| S-001 | Episode slug inconsistency (NI, state, dialogue headers) | STRUCTURAL | SIGNAL | All facet authors; normalize to `b01c01` |
| S-002 | R2-shard-anchor-mismatch (memory, NI) | STRUCTURAL | SIGNAL | R2 judges; note only — in-file pathology absent; canonical entries unreviewed at R2 |
| S-003 | Metadata: shard ADD non-enactment unlabeled | METADATA | SIGNAL | Orchestrator / consolidation; annotate non-enacted ADD verdicts in shard body |
| S-004 | Metadata: wren-slice fence format | METADATA | SIGNAL | build_cite_index / studio; add `---` fence to wren slice sub-header |
| S-005 | CURVE-SHAPE SHAPE-CHECK | CURVE-SHAPE | SIGNAL | Dramatist / rubric authority; resolve hinge-label vocabulary collision |
| S-006 | vibes:20 dual-anchor | DEDUP | SIGNAL | Showrunner (vibes); resolve proto:27 citation of vibes:20 anchored at @25 |
| S-007 | vibes:10 dual-anchor | DEDUP | SIGNAL | Showrunner (vibes); resolve proto:5 citation of vibes:10 anchored at @4 |
| S-008 | Sensory frequency-band breach-high | FREQUENCY-BAND | SIGNAL | Studio (sensory); advisory |
| S-009 | feel:taylor frequency-band breach-high | FREQUENCY-BAND | SIGNAL | taylor-hebert-kl-122ac (feeling fork); advisory |
| S-010 | Exposition cold-start sparsity advisory | FREQUENCY-BAND | SIGNAL | Exposition-author; advisory |
| S-011 | NI "the network" atmosphere-thin | TASTE-FLAG | SIGNAL | taylor-hebert-kl-122ac (NI impersonator); advisory for Phase 5b audience |
| S-012 | Preamble voice-fidelity "calendar I came in with" | TASTE-FLAG | SIGNAL | Exposition-author; advisory for Phase 5b audience |
| S-013 | AP registration-vocabulary state:11 | AP-SCAN | SIGNAL | taylor-hebert-kl-122ac (state-updates fork); advisory |
| S-014 | vibes:10 dual-anchor constraint advisory | CONSTRAINT | SIGNAL | Showrunner (vibes); same resolution as S-007 |
| S-015 | State-updates stale sub-header (env slice) | STRUCTURAL | SIGNAL | Studio (env); relabel `facet: state-updates-env` to `facet: state-updates` in consolidated file |
