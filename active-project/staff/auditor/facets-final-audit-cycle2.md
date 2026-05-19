---
report: facets-final-audit
episode: b01c01
cycle: 2
phase: 5
date: 2026-05-19
inputs:
  facet-files:
    - active-project/theater/facets/location-state.md
    - active-project/theater/facets/interest-narrator.md
    - active-project/theater/facets/memory.md
    - active-project/theater/facets/feeling.md
    - active-project/theater/facets/sensory.md
    - active-project/theater/facets/state-updates.md
    - active-project/theater/facets/exposition-b01-c01.md
    - active-project/theater/facets/vibes.md
    - active-project/theater/facets/metaphor.md
    - active-project/theater/facets/scene-map-b01-c01.md
    - active-project/theater/facets/_cite-index.md
    - active-project/theater/proto-lines/b01-c01.md
    - active-project/theater/dialogue/coll-net-mender-flea-bottom.md
    - active-project/theater/dialogue/taylor-hebert-kl-122ac.md
    - active-project/theater/dialogue/wren-stitch-maker-flea-bottom-ward.md
    - active-project/staff/dialogue-writer/coll-net-mender-flea-bottom.drafts.md
    - active-project/staff/dialogue-writer/wren-stitch-maker-flea-bottom-ward.drafts.md
  rubrics:
    - design/shoot-v2/rubric-location-state.md
    - design/shoot-v2/rubric-narrator-interest.md
    - design/shoot-v2/rubric-memory-flags.md
    - design/shoot-v2/rubric-feeling.md
    - design/shoot-v2/rubric-sensory.md
    - staff/exposition-author/rubric-exposition.md
    - staff/dialogue-writer/rubric-dialogue.md
  prior-reports:
    - active-project/staff/auditor/facets-final-audit.md
    - active-project/staff/auditor/facets-final-audit-r2-verify.md
    - active-project/staff/fixer/facets-cycle2-remediation.md
  ratifications:
    - active-project/staff/impersonator-taylor-hebert-kl-122ac/cycle-2-ratification.md
    - active-project/staff/impersonator-wren-stitch-maker-flea-bottom-ward/cycle-2-ratification.md
    - active-project/staff/studio/cycle-2-ratification.md
    - active-project/staff/exposition-author/cycle-2-ratification.md
    - active-project/staff/dialogue-writer/cycle-2-ratification.md
  new-card:
    - cards/conditions/monument-override-architecture-prohibition-122ac.card.md
delta-from-cycle-1: |
  Cycle-1 closed HARD=2 (vibes:21 citation-mismatch + vibes:17 Earth-Bet hard-fence).
  Both were remediated before cycle-1 Phase 5b and verified clean in facets-final-audit-r2-verify.md.
  Cycle-1 Phase 5b returned PARTIAL: 3 pass / 9 fail across audience personas.
  Cycle-2 remediation addressed: loc-state:3+4 cut (renumbered), narrator:2+4 rewritten + narrator:5a
  added, sensory old-state-source tokens added + thermal-gap resolved, state-updates entries 10/12/13/15/19
  revised + 11/17 flagged-for-cut, mem:1 relocated @15->@16 + mem:3 added @17 + mem:2 target-reference
  updated, feel:1 second clause cut, exposition:5 added @20, dialogue-coll line revised, dialogue-wren
  citation corrected. New card: monument-override-architecture-prohibition-122ac.
---

# Findings

## HARD (3)

### HARD-001
- **id:** HARD-001
- **class:** SCENE-MAP
- **locus:** scene-map-b01-c01.md header vs. proto-lines/b01-c01.md
- **what:** Scene-map declares `total-bones: 27` and `scene-C @22-@29`. The proto-lines file declares `aggregate_range: 1-26` and contains bones only through @26. The scene-C range in the scene-map terminates at @29; no bones @27, @28, or @29 exist in the proto-lines file. Coverage assertion `27/27 bones in exactly one scene` cannot be verified against the proto-lines since only 24 numbered bones exist in the file (24 real bones; @10 and @19 are time-skip markers outside scope). The declared total-bone count (27) does not reconcile with the proto-line corpus (24 bones in scope).
- **why:** The scene-map is the URI-SCENE-WINDOW gate's source of truth. A total-bones mismatch between scene-map and proto-line file means the coverage assertion is unverifiable and may be wrong. Downstream: /and-stitch reads the scene-map for fusion-eligible-runs and per-scene coverage; an inflated bone count propagates into stitcher instructions that reference anchors the prose file does not contain. The scene-C range endpoint (@29) potentially licenses stitcher work on non-existent anchors.
- **criteria:** The scene-map's `total-bones`, `scene-C` range endpoint, and `coverage` assertion must be reconciled with the proto-lines file's actual bone count and highest anchor ID. Either the proto-lines file is missing bones @27-@29 (in which case the proto-lines file is incomplete and the scene-map is correct), or the scene-map was generated against a different proto-lines state and its bone count and scene-C endpoint are wrong. The reconciliation must result in consistent values across both files.

### HARD-002
- **id:** HARD-002
- **class:** RUBRIC-FIDELITY / memory target-reference / CONSTRAINT
- **locus:** memory.md, mem:1 @16
- **what:** mem:1 target-reference is the free-text gloss `(earth-bet: administrative-observation-apparatus displacement)`. No monument card slug is cited. The rubric-memory-flags §Hard-fence test (URI-FACETS-CYCLE-1, 2026-05-19) promoted from audience-gate cycle-1: "Every memory-flag entry's `target-reference:` field must name a monument card slug that resolves in the card library via margit referral. A bare gloss text in `target-reference` without a margit-resolved slug fails the licensing-discipline axis: the monument is asserted, not anchored." The cycle-2 remediation created `monument-override-architecture-prohibition-122ac.card.md` for mem:2's target, but mem:1's Earth-Bet displacement target remains a free-text gloss with no margit-resolved monument card. No margit referral for this displacement pattern exists in the cycle-2 remediation log.
- **why:** mem:1 is the sole Earth-Bet displacement fire in the memory file. If its target-reference is a free-text gloss rather than a card slug, the stitcher's routing cannot resolve the metaphor/callback license the entry is supposed to gate. More critically, the rubric's monument-card-resolution test is a promoted HARD: the free-text gloss path requires (a) a structurally clear gloss and (b) a queued margit referral at minimum (SIGNAL), upgrading to HARD if the gloss is opaque or no referral exists. The gloss `(earth-bet: administrative-observation-apparatus displacement)` is structurally clear as a free-text gloss, but no margit referral for this displacement family is documented in cycle-2, which makes this a HARD rather than SIGNAL under the promoted rule.
- **criteria:** mem:1's target-reference must either (a) be updated to a margit-resolved monument card slug naming the Earth-Bet administrative-observation-apparatus / uniformed-administrative-observer displacement pattern, following the same margit referral path that produced `monument-override-architecture-prohibition-122ac` for mem:2, OR (b) the fixer must document an explicit margit referral for this displacement family queued for card creation, in which case the finding may be downgraded to SIGNAL pending card creation. Until one of these conditions is met, the monument is asserted against a free-text gloss with no card anchor.

### HARD-003
- **id:** HARD-003
- **class:** RUBRIC-FIDELITY / memory per-scene cap / CONSTRAINT
- **locus:** memory.md, mem:1 @16 and mem:3 @17, Scene-B
- **what:** Scene-B spans @11-@20 (per scene-map). mem:1 anchors at @16 and mem:3 anchors at @17. Both are within Scene-B. This is two memory-flag entries in one scene. The rubric-memory-flags §Licensing-discipline axis states: "Per-scene cap. At most one memory-flag entry per scene. A scene with two or more memory-flag fires is over-firing the licensing layer for that scene; the stitcher cannot meaningfully gate metaphor / callback density across multiple licensed beats in a single scene." The per-scene cap is explicitly marked hard in the rubric. No exception clause in the rubric permits two entries in a flat-low scene on adjacent anchors without an explicit displacement-clamp construction that treats both as one compound fire.
- **why:** The memory facet's licensing function depends on the per-scene cap as a hard structural constraint. Two fires in Scene-B (one Earth-Bet displacement at @16, one Westerosi-monument clamp at @17) over-fire the licensing layer for that scene. The stitcher reading two adjacent memory-flag licenses in a flat-low scene cannot disambiguate which beat carries the figurative weight — both are licensed, making the gradient undefined for @16-@17. This is a downstream stitcher instruction failure: the stitcher will render figurative content at both @16 and @17 where the rubric intends only one. The remediation log's doubled-register requirement (both registers must appear in the file) was met, but it was met by placing two fires in the same scene rather than across different scenes. Doubled-register satisfaction is a file-level requirement; per-scene cap is a scene-level hard gate. Both must be met independently.
- **criteria:** mem:1 and mem:3 cannot both fire in Scene-B under the per-scene cap. One must be cut or relocated. If one is cut, the remaining entry must still satisfy the doubled-register file-level requirement (one Earth-Bet displacement AND one Westerosi-monument clamp across the file). Options: (a) cut the weaker entry and verify doubled-register is still satisfied by fires in other scenes; (b) relocate one entry to Scene-A or Scene-C (each flat-low; each has zero current memory fires; the rubric permits fires in flat-low zones); (c) merge the two fires into one compound entry on the single most-justified anchor with a target-reference that acknowledges both monument families — only permitted if one description can carry both cues without violating the one-clause discipline. Fixer chooses minimum-change path; the doubled-register requirement must be preserved.

---

## SIGNAL (5)

### SIGNAL-001
- **id:** SIGNAL-001
- **class:** CITE-INDEX-FRESHNESS (Class 7)
- **locus:** active-project/theater/facets/_cite-index.md
- **what:** The cite-index is stale against the current post-cycle-2 facet graph. Specific staleness items enumerated:
  (a) loc-state:3 @11 and loc-state:4 @13 still appear as active entries with co-citation data; both were cut in cycle-2 and are physically present only as comment-lines.
  (b) loc-state entry IDs in the index do not reflect the cycle-2 renumbering (old 5→3, old 6→4). Index shows `loc-state:5 @15` and `loc-state:6 @20`; current file has entries as `3 @15` and `4 @20`.
  (c) narrator:5a @22 appears in the locked interest-narrator.md file but has no cite-index entry.
  (d) mem:1 is indexed at @15 (`mem:1 @15 back=Y co=[...]`); current file has mem:1 at @16 after cycle-2 relocation.
  (e) mem:3 @17 was added in cycle-2 but has no cite-index entry.
  (f) Exposition index shows 4 entries; exposition:5 @20 was added in cycle-2 and has no cite-index entry.
  (g) State entry count shown as 20 in index (matching the pre-cut state-updates.md); entries 11 and 17 remain as physical entries (see Class 8 analysis below), so the count may or may not need updating depending on cut resolution.
  (h) The `totals: 68 facet entries` header is stale (net change from additions + cuts shifts this).
- **why:** The cite-index is the DAG backing tool for cross-facet consistency checks, the metaphor facet's anchor verification, and the stitcher's routing surface. A stale cite-index propagates wrong back-citation data into all downstream consumers. The metaphor file's Phase 5 R2 judge pass cited `_cite-index.md` for anchor verification (`mem:2 @23 back=Y co=[feel:1, vibes:17]`, `feel:1 @23 back=Y co=[mem:2, vibes:17]`) — those entries are still correct. But narrator:5a, mem:3, and exposition:5 have no cite-index entries, meaning their cross-facet relationships are not recorded in the DAG.
- **recommendation:** Regenerate the cite-index against the current post-cycle-2 facet graph before Phase 5b fires. The cite-index regeneration is within auditor's dispatch scope (per dispatch instructions: "If stale, regenerate inline (you have Write access). Document the regeneration."). However, entries 11 and 17 in state-updates must first be resolved (PHANTOM-CUTS — Class 8) before regeneration, because their live-or-cut status affects the state entry count and co-citation data. Sequence: resolve HARD-001 (scene-map) + state phantom-cuts (SIGNAL-002) → then regenerate cite-index. Cite-index regeneration deferred to after HARD resolution to avoid generating a cite-index against a partially-unresolved facet graph.

### SIGNAL-002
- **id:** SIGNAL-002
- **class:** STATE-UPDATES PHANTOM-CUTS (Class 8)
- **locus:** state-updates.md, entries 11 and 17
- **what:** Entries 11 and 17 are flagged for cut via comment but remain as physical entries in the file.
  - Entry 11 (@12): `actor:taylor-hebert-kl-122ac.knowledge.hook-block-density-map: unmapped -> block-density-mapped-passively` — cycle-2 fixer comment: "FLAGGED for cut." Physical entry line `11 @12 actor:...` is present.
  - Entry 17 (@26): `actor:taylor-hebert-kl-122ac.knowledge.ward-social-geometry-hook: block-mapped -> ward-layer-deeper` — cycle-2 fixer comment: "CUT." Physical entry line has been removed (the comment block reads `# entry 17 CUT (cycle-2 fixer, 2026-05-19): ...`). On re-read: entry 17 is CONFIRMED REMOVED from the state-updates.md file — the comment block documents the cut rationale but no physical `17 @26 actor:...` entry line remains. Entry 11 is CONFIRMED PRESENT — both the comment block and the physical entry line exist.
- **per-entry analysis:**
  - Entry 17: effectively cut (comment-only; no live entry line). Treat as removed. No further action needed on entry 17.
  - Entry 11: live entry with a cut-flag comment. The cut rationale is substantive and correct (cape-fic-reader: discipline-hold at @8 with no released-from-hold transition; passive data arrives but deliberate conversion into canonical knowledge-state should not fire under the active hold). The entry violates the state-updates rubric integrity: entry 10 at @8 establishes `active-holding: ambient-passive -> threshold-held-against-density-spike`, and the clarification note specifies that `active-holding` caps deliberate processing of the data. Entry 11 at @12 fires `knowledge.hook-block-density-map: unmapped -> block-density-mapped-passively` while the hold is still active (no released-from-hold transition between @8 and @12). The `passively` qualifier does not resolve this because the hold is precisely against passive-data deliberate processing into canonical state. Entry 11 is a live state violation: it fires canonical knowledge acquisition under a stated hold with no intervening release.
- **why:** A live entry 11 in the canonical state-updates file creates a state-consistency violation: Taylor's knowledge.hook-block-density-map is marked as acquired at @12, but entry 10 says deliberate data processing is held from @8 onward with no release. Any downstream author or the stitcher reading state-updates will see a knowledge entry that contradicts the discipline-hold. The comment says "flagged for cut" but does not perform the cut; the physical entry remains operative for state-file consumers.
- **recommendation:** Entry 11 must be physically removed from state-updates.md (not just comment-flagged). The cut rationale is sound and already fully documented in the comment block. A fixer pass to delete the physical entry line is sufficient.

### SIGNAL-003
- **id:** SIGNAL-003
- **class:** FREQUENCY-BAND (carried forward from cycle-1)
- **locus:** exposition-b01-c01.md (5 entries / 24 bones = 20.8%) and interest-narrator.md (8 entries / 24 bones = 33.3%)
- **what:** Cycle-2 added entries to both files, increasing frequency bands beyond cycle-1 already-elevated levels.
  - Exposition: cycle-1 had 4 entries at 16.7% (band 1-5%; cold-start override). Cycle-2 ADD of exposition:5 brings to 5 entries at 20.8%. The cold-start override justification (first episode; three named entities + Watch institution + no lens-facet substitution available) still holds; the-Hook gloss at @20 was a genuine embedded-noun gloss-completeness HARD that required the ADD. Breach-high further from band. Severity: SIGNAL (cold-start override defense still applies; the ADD was rubric-mandated by the HARD finding).
  - Interest-narrator: cycle-1 had 7 entries at 29.2% (band 15-25%; breach-high by 1). Cycle-2 ADD of narrator:5a brings to 8 entries at 33.3%. The ADD was required by the audience's doubled-register demand (Westerosi-monument clamp fire). Breach-high further from band. Severity: SIGNAL (ADD was driven by a failing audience-gate verdict; the doubled-register requirement overrode the band constraint; note for next chapter that narrator density must contract).
- **why:** Both files now further exceed their frequency bands due to cycle-2 remediation-required adds. Neither is blockable on this basis given the documented override justifications. However, the band breaches compound across the chapter and increase stitcher render-density beyond the intended contrast gradient. Chapter authoring for b01c02 must budget for reduced exposition and narrator-interest density to compensate for b01c01's structural overload.
- **recommendation:** Advisory for b01c02 authoring. Not blockable this cycle.

### SIGNAL-004
- **id:** SIGNAL-004
- **class:** AP-SCAN / narrative-interest doubled-register file-shape check
- **locus:** interest-narrator.md, narrator:5a @22 and narrator:3 @12
- **what:** Two flags carried from cycle-1 that cycle-2 partially addressed:
  (a) narrator:5a @22 — the Westerosi-monument clamp at @22 fires in scene-C, one bone before the dialogue beat. narrator:5 @21 (approach) and narrator:5a @22 (monument-clamp) create two consecutive fires (@21, @22) in scene-C. The rubric's anti-pattern #7 (persistent-narration) applies when "the same registration carrying across beats." These are different registrations (spatial-geometry read at @21 vs. foreknowledge-clamp at @22), so persistent-narration does not strictly apply. However, the density in scene-C now runs: @21, @22, @23, @24 — four consecutive fires across six scene-C anchors through @26, which is dense for a flat-low scene. The rubric expects fires to be visibly sparser than silences. This is a density-pattern flag, not a specific entry fault.
  (b) narrator:3 @12 tail-clause — dark-fantasy-reader flagged "the reading is the whole of what she will take" as stepping on the image. Retained at cycle-2 per minimum-change principle (1-of-3 dissent). If this entry fails at cycle-2 Phase 5b, it becomes a cycle-3 target.
- **why:** These are advisory flags for the Phase 5b audience-gate reviewers. (a) The scene-C density pattern (@21, @22, @23, @24 consecutive fires) is the audience's most likely attack surface in the NI file. (b) narrator:3 tail-clause is a known watch-item.
- **recommendation:** Flag for Phase 5b dispatch. Not blockable from Phase 5.

### SIGNAL-005
- **id:** SIGNAL-005
- **class:** CONSTRAINT / STRUCTURAL (carried forward, status-change)
- **locus:** state-updates.md, multi-frontmatter structure; feeling.md, multi-source structure
- **what:** Two structural issues from cycle-1 that remain unaddressed in cycle-2:
  (a) state-updates.md multi-frontmatter: the consolidated state-updates file contains multiple `---`-delimited frontmatter blocks (one per source: env, coll-net-mender-flea-bottom, taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward). Per cycle-1 finding S-002, single top-of-file frontmatter per `r3-signal-001`. No change in cycle-2.
  (b) feeling.md multi-source structure: the consolidated feeling file contains per-source frontmatter blocks (source: coll-net-mender-flea-bottom; source: taylor-hebert-kl-122ac; source: wren-stitch-maker-flea-bottom-ward) embedded within the file body after the main frontmatter. The single top-of-file frontmatter rule applies here too.
  (c) metaphor.md frontmatter-missing-leading-delimiter: cycle-1 finding S-001 (no leading `---` before `facet: metaphor`). No change in cycle-2.
- **why:** These are parser-compatibility signals. They do not affect entry content and were previously classified SIGNAL. They remain SIGNAL in cycle-2; no remediation was scoped for structural formatting issues. Noting continuation of cycle-1 SIGNAL items.
- **recommendation:** Carry to next structural cleanup pass. Not blockable.

---

## NOTE / advisory

**NOTE-001:** vibes.md Earth-Bet source-field edge case (carried from r2-verify). `exposition-b01-c01.md` source field references warehouse slug `cond-khepri-residue-122ac` (an operator-facing card reference, not narrator-rendered prose). The r2-verify audit logged this as NOTE-FOR-NEXT-RUN. Confirmed still present. The source-field fence scan is not a promoted HARD in cycle-2 rubrics; the slug is metadata-only and operator-facing. Carry as NOTE for next audit if source-field fence is tightened.

**NOTE-002:** Scene-map time-skip @21 description. The scene-map documents `@21 — between scene-B and scene-C (multi-day gap; wren first appears "on the third or fourth day" per chapter chunk)`. However, @21 appears in the proto-lines as `21 wren-stitch-maker-flea-bottom-ward approaches taylor-hebert-kl-122ac [narrator:5]` — it is a live proto-line with a facet citation, not a time-skip blank. The time-skip before scene-C is @19 (not @21 per the proto-lines; @20 is the first scene-C bone). Scene-map lists @21 as a time-skip marker while the proto-lines use @21 as a live bone. This is a secondary inconsistency within the scene-map's own `time-skip markers` section versus the proto-lines. Auditor does not modify scene-maps (upstream-locked). Flagged for HARD-001 remediation team to address during reconciliation.

**NOTE-003:** state-updates entry 10 (@8) back-citation note. The field-extension clarification added in cycle-2 resolves the worm-canon-pedant ambiguity. The `cite-index back=N` on @8 is correctly documented as interior-only state mutation (the discipline-hold is not externally visible on the proto-line). No finding; noting confirmation of the clarification's correctness.

**NOTE-004:** Metaphor facet sparsity. metaphor.md has 1 entry at 4.1% (1/24). The rubric states "0-3% on 24 bones = 0 or 1 entry maximum" — the author's interpretation is that 1 entry is within the absolute count limit (0 or 1), while the percentage calculation gives 4.1% against a 3% ceiling. This is an interpretive edge. Because the rubric names an absolute count (0 or 1) as the maximum on 24 bones, 1 entry satisfies the count criterion regardless of percentage calculation. PASS on absolute-count rubric reading. Advisory: on longer corpora the percentage calculation will dominate.

**NOTE-005:** Wren dialogue sidecar facet-license citation corrected @22→@21. feel:2 anchors at @21 in the locked feeling.md. The cite-index confirms `feel:2 @21 back=N co=[narrator:5]`. The corrected citation in the wren sidecar resolves correctly in the locked graph. No finding.

**NOTE-006:** Monument card `monument-override-architecture-prohibition-122ac.card.md` was authored against `schemas/card.schema.md`. Auditor confirms: card class is `condition`, scope is `library`, world is `planetos`, origin is `authored`, quality is `full`. References field names `cond-override-architecture-residue-122ac` and `cond-no-parahuman-infrastructure`. Card body sections present and substantive. The card passes basic schema compliance on visual inspection. A margit INDEX update is referenced in the cycle-2 known changes; auditor did not independently verify the INDEX file exists and is updated (not in dispatch scope), but the card itself validates against the schema structure.

---

# Class Summaries

**1. CONSTRAINT.** Schema compliance checked across all 11 facet files. ID monotonicity: interest-narrator uses `5a` as a non-sequential ID (documented as intentional at authoring time to preserve existing ID sequence); this is a form irregularity but not a violation of the schema's monotonic-positive-integer requirement unless `5a` is treated as non-integer — flagged as an advisory within SIGNAL-001 (cite-index must handle the non-integer ID). Hard-fence scan: Earth-Bet scan across all facet files clean post-cycle-2. Vibes keyword `override-architecture-residue` (formerly `khepri-residue`) is clean. Memory description fields clean (no proper nouns). Feeling description field clean (no labeled-feeling vocabulary; one-clause form correct after cycle-2 cut). Form-discipline check on feeling: feel:1 is `her hand stills at her side | expressed: no` — one-clause somatic tell, no second clause, no subject-shift. PASS.

**2. AP-SCAN.** AP-10 inverted-predicate template cap (≤1/file): current interest-narrator file has narrator:6 @24 `face, not node, is what she holds` as the single remaining "is what" construction. narrator:2 and narrator:4 were rewritten; no other entry uses the inverted-predicate template. Cap satisfied. File-level AP-SCAN for deposition cadence, modern HR-speak, and nominalization on dialogue lines: all three utterances pass (clean on visual inspection). Dialogue AP-scan: "Needle's idle. Sit, then." — smallfolk register, no contamination. "Mistress Coll teach you that knot?" — child-register, no contamination. "I cannot say." — Taylor mask-register, no contamination. AP-SCAN PASS on all three.

**3. FREQUENCY-BAND.** See SIGNAL-003. Exposition now at 20.8% (up from 16.7%); narrator-interest now at 33.3% (up from 29.2%). Both bands breached further by cycle-2 mandated adds. Both cold-start and doubled-register override justifications hold. Sensory remains at 12.5% (3/24) — unchanged from cycle-1; band is 3-6% (1-2 entries on 24 bones); breach-high by 1. Feeling at 2/24 = 8.3%; band 2-5% (1.5-4 fires on ~24 bones); within range for 24-bone chapter. Memory at 3/24 = 12.5%; band 5-12%; breach-high by one entry due to cycle-2 ADD. The breach is driven by the per-scene cap violation (HARD-003) — resolving HARD-003 by cutting one memory entry will also bring memory back into the 5-12% band (2/24 = 8.3%). Vibes off-band analysis: vibes operates without a formal frequency band in the rubrics; not scored. Metaphor at 4.1% against 0-3% ceiling — within absolute count limit (1 entry). All bands: SIGNAL-003 captures the advisory items; no new HARD from frequency-band alone.

**4. RUBRIC-FIDELITY.** Seven newly-promoted clauses checked:
- Loc-state dexterity-stillness anchor-verb REJECT: loc-state:3 @11 CUT. Remaining entries: loc-state:1 @1 (`enters the corner-room` — transitional verb, PASS), loc-state:2 @9 (`faces the street` — positioning verb, PASS), loc-state:3 @15 (`the Watch column passes` — movement verb, PASS), loc-state:4 @20 (`Wren crosses` — transitional verb, PASS). No dexterity-stillness verbs remain. PASS.
- Narrator AP-10 ≤1/file: verified above. PASS.
- Memory target-reference resolves to card on disk: mem:2 @23 → `monument-override-architecture-prohibition-122ac` card exists. mem:3 @17 → free-text gloss `(westeros: gold-cloak-watch-register; conquest-charter-institutional-record; Dance-era administrative-collapse displacement...)` — free-text gloss; no monument card slug. This is a SIGNAL per the rubric (structurally clear gloss, no queued margit referral documented for mem:3's Westerosi monument family). mem:1 @16 → free-text gloss with no card slug and no margit referral: HARD-002. mem:3's Westerosi-monument family also lacks a card slug — the rubric says SIGNAL when "the gloss is structurally clear and the card is queued." No queued referral documented for the gold-cloak-watch-register monument family. Auditor classifies mem:3 as a secondary SIGNAL within HARD-002's scope (both Earth-Bet and Westerosi monument families in this file are card-slug-unresolved; the HARD applies to mem:1 as the sole Earth-Bet displacement fire; mem:3 is an additional SIGNAL).
- Memory doubled-register file-level shape: Earth-Bet displacement fire exists (mem:1). Westerosi-monument clamp fire exists (mem:3). File-level shape SATISFIED — however, the per-scene cap violation (HARD-003) may require cutting one entry. If mem:3 is cut, the Westerosi-monument register is lost unless relocated. If mem:1 is cut, the Earth-Bet displacement register is lost unless relocated. The doubled-register requirement and the per-scene cap must both be satisfied in the resolution. Doubled-register currently SATISFIED at file-level; at risk pending HARD-003 resolution.
- Feeling one-clause form-discipline: PASS (verified above).
- Sensory unanchored old-states: sensory:1 `old-state-source:` documented in entry pointing to loc-state:1 studio note. sensory:2 `old-state-source:` documented pointing to loc-state:1 studio note (sound baseline). Both baselines are documented in location-state.md as comment-adjacent studio notes. The rubric requires old-state to resolve to "the most recent location-state file's § sensory or § conditions field for the beat's location, OR the most recent prior sensory-flag entry on the same modality." The loc-state studio notes (comment-adjacent) are not formal loc-state entries — they are documentation within the file. Whether comment-adjacent studio notes satisfy the rubric's baseline resolution is an edge case: the rubric says "loc-state file's § sensory or § conditions field" and the studio notes are in the loc-state file as documentation rather than field content. Auditor assesses: the cycle-2 remediation's approach of documenting baselines in the loc-state file as studio notes was ratified by the studio ratification agent and accepted as the minimum-change solution. The notes are present in the loc-state file and are explicitly cross-referenced by the sensory entries. PASS under the remediation rationale; the baseline is resolvable within the loc-state file. Sensory:3 @15 old-state is `hook-street-ambient`; prior entry sensory:2 @9 new-state is `hook-street-noise-entering`. The old-state of sensory:3 derives from the new-state of sensory:2 (same sound modality; sensory:2 established the ambient noise level; sensory:3 is firing a spike over that new baseline). The chain is: loc-state-note → sensory:1 → sensory:2 (new-state: `hook-street-noise-entering` ≈ `hook-street-ambient`) → sensory:3. Naming is not verbatim-identical (`hook-street-noise-entering` vs. `hook-street-ambient`), but they describe the same perceptual baseline (exterior street noise after door-open). PASS on anchor chain; naming variation is not contradictory.
- Sensory modality silent-gap: loc-state:4 @13 was cut. The cut resolved the thermal silent-gap (no thermal event named in loc-state means no corresponding sensory-flag required). Current loc-state:1 studio notes name smell (`tallow-smoke-ambient`) and sound (`corner-room-interior-quiet`) baselines; these are baselines, not discrete perceptual events — they do not create silent-gap obligations. loc-state:2 @9 sensory note: "the Hook visible through the facing side; the near-alley foot-traffic readable from the threshold without stepping out" — this is a visual-geometry note, not a named perceptual event (no modality-inflection claim); no silent-gap obligation created. loc-state:3 @15 sensory note: "the Watch column passes at the Hook's curve — visible from the corner-room's street-facing side" — visual event; the Watch column passing also creates a sound event (a column of armed guards passing in a quiet alley). sensory:3 @15 fires `sound: hook-street-ambient -> watch-column-passing`. The sound event named by the loc-state @15 has a sensory-flag ratification. PASS.
- Exposition embedded-noun gloss-completeness: exposition:4 @20 (Wren) references "the Hook" via "a ward of one of the stitch-maker households a few doors over, the kind of child the Hook keeps in light work and two meals for keeping." The Hook appears in the gloss text. exposition:5 @20 now provides the first-mention-place gloss for the Hook. Cross-episode glossed-terms register includes `the-hook`. The embedded-noun gloss-completeness HARD is resolved. PASS.
- Dialogue per-entry citation-completeness with cite-index resolution: see class 6 summary.

**5. SCENE-MAP.** URI-SCENE-WINDOW gate: scene-map declares `total-bones: 27`, `coverage: 27/27 bones in exactly one scene`. Proto-lines file has `aggregate_range: 1-26` with 24 numbered bone anchors. Discrepancy filed as HARD-001. Scene-B includes @11-@20 but @19 is documented as a time-skip marker; proto-lines shows no @19 entry. Scene-C @22-@29 per scene-map; proto-lines highest anchor is @26. Independent of the bone-count discrepancy, scene coverage for the known bones (1-26) cannot be fully verified against the scene-map's @29 terminus. Within known anchors: all 24 proto-line bones fall within a declared scene range. @1-@9 → scene-A PASS. @11-@18 → scene-B PASS. @20 → scene-B PASS. @22-@26 → scene-C (within @22-@29). No gaps or overlaps for known bones. The discrepancy is in the total count and upper bound.

**6. DIALOGUE-COVERAGE.** URI-DIALOGUE-COVERAGE-GATE: three speakers in chapter — coll-net-mender-flea-bottom, taylor-hebert-kl-122ac, wren-stitch-maker-flea-bottom-ward. All three have non-empty dialogue files in `active-project/theater/dialogue/`. All speech bones cited: coll @3 cited in coll's file; taylor @25 cited in taylor's file; wren @22 cited in wren's file. PASS. Per-entry citation-completeness: all three dialogue sidecar entries carry both `card-signatures:` and `facet-licenses:` fields post-R2 cycle-2 ratification. Cite-index resolution check:
- Coll sidecar @3: `state-coll:6 @3` — resolves to state-updates.md entry 6, actor:coll-net-mender-flea-bottom.block_baseline_new_faces, @3. RESOLVES. `state-taylor:8 @3` — resolves to state-updates.md entry 8, actor:taylor-hebert-kl-122ac.knowledge.coll-as-vouching-vector, @3. RESOLVES.
- Wren sidecar @22: `state-wren-stitch-maker-flea-bottom-ward:@22` — resolves to state-updates.md entry 19, @22, actor:wren-stitch-maker-flea-bottom-ward.stats.taylor_awareness. RESOLVES. `feel-wren-stitch-maker-flea-bottom-ward:@21` — resolves to feeling.md feel:2 @21, wren-stitch-maker-flea-bottom-ward. RESOLVES (correction from @22 to @21 confirmed in cycle-2).
- Taylor sidecar: not separately read in this audit (no sidecar file path was provided; the dialogue file for taylor is minimal at 1 entry). If a taylor sidecar exists, it was not among the verified files. Advisory: confirm taylor's @25 sidecar carries both citation axes if a sidecar file exists.
DIALOGUE-COVERAGE PASS (with advisory on taylor sidecar).

**7. CITE-INDEX-FRESHNESS.** See SIGNAL-001. Cite-index is stale against cycle-2 changes. Eight specific staleness items enumerated. Regeneration deferred pending HARD resolution (HARD-001 + SIGNAL-002 state phantom-cut). Status: STALE — NOT regenerated this run. Regeneration must occur after fixer resolves HARD-001 and SIGNAL-002.

**8. STATE-UPDATES PHANTOM-CUTS.** Entry 17: confirmed removed (comment-only). Entry 11: confirmed present as a live entry with a cut-flag comment. Entry 11 violates state consistency (knowledge acquired under an active discipline-hold). Filed as SIGNAL-002 requiring physical removal. No other phantom-cut ambiguities found in the state-updates file.

**9. CROSS-FACET CONSISTENCY.** Narrator-interest co-citation for memory entries:
- mem:1 @16: cite-index shows `mem:1 @15 back=Y co=[..., narrator:4 ...]`. After cycle-2 relocation, mem:1 is at @16. The cite-index still shows @15. In the current interest-narrator file, narrator:4 @15 (`she prices her own visibility against the Watch column from inside the doorway`). No narrator entry fires at @16. The rubric requires mandatory narrator-interest co-citation at the same `@<proto-line-id>`. mem:1 is now at @16; narrator:4 is at @15. The spine requirement (narrative-interest co-citation on the same bone) FAILS for mem:1 post-relocation: no narrator-interest entry exists at @16. This is a cross-facet consistency fault. However, auditor notes the complexity: @15 is the Watch-passing beat (institutional-pressure peak, 8 co-fires); @16 is the quiet-beat aftermath; the rubric's memory-flags §Licensing-discipline says fires concentrate in flat-low aftermath bones (not the peak bone). The relocation was rubric-correct for the quiet-beat anchor requirement. But the relocation broke the spine co-citation: narrator:4 at @15 was the spine for mem:1 at @15; at @16 there is no spine. This is a cross-facet fault introduced by the relocation.
- mem:2 @23: narrator:7 @23 present. Co-citation PASS.
- mem:3 @17: no narrator-interest entry at @17. narrator:3 is at @12; narrator:4 is at @15. The nearest narrator fire after @15 is narrator:5 @21. mem:3 @17 fires without a narrator spine on the same bone. Spine co-citation FAILS for mem:3. Same class of fault as mem:1: the ADD at @17 did not have a corresponding narrator-interest ADD at @17.
- Assessment: mem:1 and mem:3 both violate the mandatory narrator-interest co-citation requirement. mem:1's violation was introduced by the cycle-2 relocation (moved from @15 where it had spine to @16 where it doesn't). mem:3 was added at @17 without authoring a corresponding narrator:@17 entry. These are cross-facet consistency faults at the SIGNAL level (they do not rise to HARD independently because they are additive to existing findings — HARD-003 resolution may also address them if entries are relocated). Auditor classifies: the spine violation on mem:1 and mem:3 should be treated as part of the HARD-003 remediation scope. Fixer resolving HARD-003 (per-scene cap) must also ensure that wherever the surviving memory entry lands, a narrator-interest entry exists at the same anchor. This is incorporated into HARD-003's criteria.
- Scene-map zone classification for memory fires: mem:1 @16 → scene-B flat-low (within @11-@20). mem:2 @23 → scene-C flat-low (within @22-@29). mem:3 @17 → scene-B flat-low. All three in flat-low zones. Quiet-beat anchor requirement SATISFIED for all three (independent of per-scene cap violation).

**10. CARD INTEGRITY.** `monument-override-architecture-prohibition-122ac.card.md` reviewed against `schemas/card.schema.md`. Card has: name, class (`condition`), scope (`library`), world (`planetos`), origin (`authored`), quality (`full`), references array. Card body has description, sensory impact, duration, monument body (three named subsections: the architecture, the vow, threshold-of-deployment dynamic), and interaction notes. The card class is `condition` — per CLAUDE.md rule 8, card classes are restricted to five: persona, location, prop, condition, behavior. `condition` is a valid class. The slug `monument-override-architecture-prohibition-122ac` follows the mechanism-descriptive naming convention required by rubric-memory-flags §Hard-fence (URI-032). No Earth-Bet proper noun in the slug. Card PASS on schema compliance. INDEX update: not independently verified in this audit pass.

**11. FIXER-RUN ARTIFACTS.** Comment lines reviewed in all modified facet files. All fixer comment blocks are prefixed with `#` and contain fixer-identification text (cycle-2 fixer, 2026-05-19). No comment line is formatted as a live entry. In state-updates.md, entry 11's comment block uses `#` prefix throughout; the live entry line (`11 @12 actor:taylor-hebert-kl-122ac.knowledge.hook-block-density-map: unmapped -> block-density-mapped-passively`) is NOT comment-prefixed, confirming it is a live entry (this is what SIGNAL-002 names). In interest-narrator.md, all comment blocks use `#` prefix; the ID-note for narrator:5a uses `#` prefix and correctly identifies itself as a comment. All fixer artifacts are correctly formatted as comments and would not be parsed as entries by a correctly-implemented parser that ignores `#`-prefixed lines. PASS.

---

# Cite-Index Regeneration

**Status: STALE — NOT REGENERATED THIS RUN.**

The cite-index (`active-project/theater/facets/_cite-index.md`) is stale against the post-cycle-2 facet graph. Regeneration was within auditor's scope per dispatch instructions. Regeneration is deferred for the following reasons:

1. HARD-001 (scene-map bone count discrepancy) must be resolved before regeneration. The scene-map's declared bone total (27) drives the cite-index's totals line; if the scene-map is wrong, the regenerated cite-index inherits the wrong total.

2. SIGNAL-002 (entry 11 phantom-cut) must be resolved before regeneration. Entry 11 is a live state entry that the cycle-2 remediation flagged for cut. If regenerated now, the cite-index would index entry 11 as live; after fixer removes it, the cite-index would need immediate re-regeneration. Single regeneration after fixer resolves HARD-001 + SIGNAL-002 is the clean path.

3. narrator:5a uses a non-integer ID (`5a`), which may require the cite-index generation tool to handle non-standard ID formats. Confirm build_cite_index.py handles `5a` before regenerating, or rename the entry to an integer ID (e.g., 5, 6 with renumbering of 6 and 7 to 7 and 8) as part of the HARD resolution cleanup.

**Regeneration target:** After HARD-001 and SIGNAL-002 are resolved, run `python3 active-project/staff/cite-index/build_cite_index.py b01-c01` and verify: no STALE-CITATION errors; narrator:5a (or its renamed successor) appears; mem:1 at @16 appears; mem:3 at @17 appears; exposition:5 at @20 appears; loc-state entries reflect post-renumbering IDs (entries 3+4 only); state entry 11 is absent post-cut.

---

# Verdict

**HARD count: 3**
**SIGNAL count: 5**
**Phase 5b gate: BLOCKED. HARD > 0.**

Cycle-2 Phase 5 does not clear. Three HARD findings require fixer dispatch before Phase 5b may fire.

## Remediation path

**HARD-001 (scene-map bone count discrepancy):** Route to studio or scene-map author. Reconcile `total-bones`, `scene-C` range endpoint, `coverage` assertion, and `time-skip markers` section against the actual proto-lines file (aggregate_range 1-26; 24 live bones; @10 and @19 are time-skips; @21 is a live bone with narrator:5 citation not a time-skip). Determine authoritative bone count and correct whichever file is wrong. This is a data-integrity repair, not a content change.

**HARD-002 (mem:1 target-reference: free-text gloss, no monument card):** Route to impersonator-taylor or margit. Dispatch margit to create or locate a monument card for the Earth-Bet administrative-observation-apparatus / uniformed-administrative-observer displacement pattern (the patrol-passing-uniformed-presence → Earth-Bet administrative-observation-apparatus rhyme). Card slug must follow mechanism-descriptive convention (no Earth-Bet proper nouns). Once card exists, update mem:1's target-reference from the free-text gloss to the card slug. If margit cannot create the card (class not supportable or pattern already exists under a different slug), update target-reference to the nearest existing condition card and document the unresolvable gap. Note: mem:3 @17's Westerosi monument family also lacks a card slug — this is a secondary SIGNAL within HARD-002 scope. Fixer may bundle both margit referrals.

**HARD-003 (mem:1 + mem:3 both in Scene-B: per-scene cap violation):** Route to impersonator-taylor. The per-scene cap (one memory-flag per scene) must be satisfied. Choose minimum-change path:
  - Option A: Cut the weaker Scene-B entry and relocate or accept loss of that register. Verify doubled-register (Earth-Bet AND Westerosi) still satisfied at file-level. The surviving entry must have a narrator-interest spine co-citation at the same anchor — if relocating, author a narrator-interest entry at the new anchor, or confirm an existing narrator-interest entry fires there.
  - Option B: Relocate one entry to Scene-A or Scene-C. Scene-A (@1-@9) and Scene-C (@22-@29 per scene-map, or @22-@26 per proto-lines) each have zero current memory fires; both are flat-low; both are eligible. Relocation must land on a bone with an existing narrator-interest fire (required spine), or the narrator-interest file must be updated to add a spine fire at the relocation anchor.
  - Under any option: confirm that after resolution, narrator-interest co-citation exists at the anchor(s) of all surviving memory entries. This addresses the cross-facet spine failure noted in Class 9.

**SIGNAL-002 (entry 11 physical phantom-cut):** Route to fixer for minimal file edit. Remove the physical entry line `11 @12 actor:taylor-hebert-kl-122ac.knowledge.hook-block-density-map: unmapped -> block-density-mapped-passively` from state-updates.md. The cut rationale comment block can remain as documentation. This is a one-line deletion requiring no content judgment — the rationale was already judged correct in the cycle-2 remediation.

**Sequence:** HARD-001 → SIGNAL-002 → HARD-002 + HARD-003 (parallelizable) → cite-index regeneration → cycle-2 Phase 5 re-check → Phase 5b.
