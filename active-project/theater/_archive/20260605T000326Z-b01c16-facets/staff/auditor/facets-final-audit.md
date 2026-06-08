audit: facets-final-audit
episode: b01-c16
gate: /and-facets Phase 5 mechanical audit
auditor: auditor
run: 2026-06-04
---

headline: FINDINGS-PRESENT
hard-count: 1
signal-count: 4

---

## HARD FINDINGS

### fault-001
- id: fault-001
- type: fault
- what: state-updates entry 5 (@19) records `actor:taylor-hebert-kl-122ac.moral_legibility_to_self_axis: 4 -> 4.5`. The scene-map (scenes B and C narrative bodies) and the vibes header both state the same axis moving `6.0 -> 6.5`. Three files, two different numeric pairs for the same axis on the same chapter.
- why: state-updates is the canonical state record. The scene-map and vibes files derive from it. When they disagree, showrunner memory, the /and-stitch reconcile pass, and the c17 chapter-open state cannot determine the authoritative value. The wrong value will propagate forward.
- criteria: Check showrunner memory and the c15 state-updates closing value for `moral_legibility_to_self_axis`. Identify which number is correct. Correct the two files that hold the wrong number so that state-updates entry 5, the scene-map scene-B and scene-C narrative bodies, and the vibes header all agree on the same from-value and to-value.

---

## SIGNAL FINDINGS (advisory; do not block)

### flag-001
- id: flag-001
- type: flag
- what: Interest-narrator density: 7/27 = 25.9%. Band ceiling is 25%. Marginal overage of ~1 percentage point.
- why: One entry over ceiling. Short-chapter (27 bones) tightens the ratio mechanically. Not a structural failure.

### flag-002
- id: flag-002
- type: flag
- what: Sensory density: 2/27 = 7.4%. Band ceiling is 6%. Short-chapter exception applies; 2 entries is minimal absolute coverage for a 27-bone chapter.
- why: Both entries are warranted onset inflections. Advisory only.

### flag-003
- id: flag-003
- type: flag
- what: Feeling entries for septon-halvard-flea-bottom: 2 entries (feeling:2 @15, feeling:3 @26) = 7.4% of bones. Band ceiling is ≤5%/character.
- why: Both entries are expressed:partial somatic register. Marginal for a non-POV character. Advisory only.

### flag-004
- id: flag-004
- type: flag
- what: memory:1 @10 cites `-> e07:halvard-corner-first-counter` as a cross-episode callback. The e07 slug does not resolve to any same-chapter bone or active warehouse card; it is a production-internal cross-episode reference. The exposition facet independently confirms Halvard as a RESIDENT character (c07/c09/c13 trail) and treats this as an established cross-episode register notation.
- why: Legitimate cross-episode memory gloss per exposition facet confirmation. Unverifiable from the chapter-local facet set alone — a downstream reader consulting only b01-c16 artifacts cannot independently confirm the anchor. Advisory only.

---

## PASSING CHECKS

- STRUCTURAL: All @bone refs in all facets resolve within 1-27. All [prefix:id] proto-line tokens resolve to matching facet entries (full forward + reverse walk clean). Per-facet ID sequences monotone across all facets. CLEAN.
- EARTH-BET FENCE: Zero hits for Khepri/Skitter/Brockton/Gold-Morning/Scion/cape/shard/parahuman/PRT across all facet text and both dialogue utterances. CLEAN.
- SCENE-MAP COVERAGE: s01 @1-8 (8 bones) + s02 @9-18 (10 bones) + s03 @19-27 (9 bones) = 27. No gap, no overlap. Frontmatter totals (27 bones / 3 scenes) match. CLEAN.
- DIALOGUE: @10 carries [septon-halvard-flea-bottom:1]; @17 carries [septon-halvard-flea-bottom:2]. Speaker file has exactly 2 entries, both with objectives. Card-compliance verified: no alternative offered, no accusation, no claim of knowing what Taylor is, no theological jargon. CLEAN.
- VIBES licensed-by anchors: All four entries' licensed-by refs resolve to present proto-line bones or facet entries. CLEAN.
- CURVE-SHAPE: Scene-map rhythm progression (establishment → pressure-peak → walk-away climax then flat resume) coherent with declared dramatic_shape: falling. SHAPE-OK.
- METAPHOR: 0 entries — appropriate. CLEAN.
- EXPOSITION: 0 entries — appropriate for chapter-16 established-world quiet aftermath. CLEAN.
