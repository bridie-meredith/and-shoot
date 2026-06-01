---
audit: facets-final-r1-depthpass
episode: b01-c09
scope: chapter
target: b01c09
mode: flag-only
timestamp: 2026-06-01
bones: 27
hard-total: 0
phase-5b-clear: YES
headline: "0 HARD / 6 SIGNAL — 27-bone depth-pass graph is mechanically clean; all sensory old-states anchored; sensory density exemptions correctly applied."
---

# Facet Final Audit — b01-c09 (depth-pass re-run; DEC-0063 streamlined)

## Per-class counts

| Class             | HARD | SIGNAL |
|-------------------|------|--------|
| STRUCTURAL        | 0    | 0      |
| FREQUENCY-BAND    | 0    | 3      |
| METADATA          | 0    | 1      |
| CURVE-SHAPE       | 0    | 0      |
| CONTRADICTION     | 0    | 0      |
| DEDUP             | 0    | 0      |
| SUPERFLUOUS       | 0    | 0      |
| CONSTRAINT        | 0    | 1      |
| AP-SCAN           | 0    | 1      |
| TASTE-FLAG        | 0    | 0      |
| PILE-UP           | 0    | 0      |
| RUBRIC-FIDELITY   | 0    | 0      |
| **TOTAL**         | **0**| **6**  |

HARD total: 0. Phase 5b gate: CLEAR.

---

## Findings

findings:

  - id: signal-fb-001
    type: flag
    class: FREQUENCY-BAND
    what: >
      sensory file density 6/27 = 22.2%; the 4 grounding-ledger-exempt entries
      (sensory:2 grd-001, sensory:4 grd-002, sensory:5 grd-003, sensory:6 grd-004)
      are cap-exempt per grounding-ledger-b01-c09.md SATISFIED entries. The 2
      remaining non-exempt fires (sensory:1 @11, sensory:3 @27) = 7.4% of 27 bones,
      marginally above the 6% standard ceiling. The V3 short-chapter exemption
      (bone_count < 30) applies when modality-count equals the floor (2); here
      modality-count = 3, so the exemption's automatic relief does not activate. The
      exceedance is 0.07 fires over band on only the non-licensed subset.
    why: >
      Marginal. The carve-out preamble in the sensory file treats the whole density as
      licensed by the grounding-ledger, which is the correct authority per the dispatch
      instructions (PROP-0022 licensed-grounding-exception). Advisory only — the
      grounding-ledger is the controlling surface; auditor notes the non-exempt residual
      for the record as the prior signal-fb-001 did.
    note: no fixer action warranted.

  - id: signal-fb-002
    type: flag
    class: FREQUENCY-BAND
    what: >
      feeling file density 2/27 = 7.4%. Rubric band is 2-5%. Both fires respect the
      per-scene cap ≤1 (s01=1, s02=1, s03=0). The above-band reading is a
      denominator-collision artifact: 2 fires on a 27-bone chapter mechanically
      exceeds the 5% ceiling even at the floor fire-count.
    why: >
      The feeling file documents this, notes the per-fire defensibility band is met,
      and the per-scene cap is respected. No rubric violation of substance. This is the
      same denominator-collision that the sensory V3 short-chapter exemption was
      created to handle; feeling lacks the equivalent formal exemption clause. Advisory.
    note: no fixer action warranted. Candidate for a feeling rubric V3 short-chapter
      exemption analogous to the sensory V3 clause if the pattern recurs.

  - id: signal-fb-003
    type: flag
    class: FREQUENCY-BAND
    what: >
      exposition sparsity 3/27 = 11.1%, above the 1-5% rubric band. Exposition:1
      @0 prior-episode-bridge body is 122 words, 2 over the ≤120 cap. Both are
      carry-forward dispositions from the pre-depth-pass audit (rev-0002
      calendar-clock license for the +2 words; denominator-driven + bridge-suppression
      + fusion-minimized for the sparsity exceedance).
    why: >
      The +2 words are licensed by the rev-0002 cross-chapter clock-continuity mandate
      (a Phase-10 forward-thread requirement). The sparsity exceedance is
      denominator-driven — removing any one of the 3 entries fails a rule or a
      pre-licensed flag. Both carry-forward as SIGNAL, not HARD. No new finding.
    note: no fixer action warranted. Rev-0002 license controls the bridge length.

  - id: signal-meta-001
    type: flag
    class: METADATA-INCONSISTENCY
    what: >
      Episode slug format inconsistency across facet file headers: location-state,
      narrator, sensory, state-updates-env, memory, and scene-map use `b01c09`
      (no hyphen); vibes-updates and exposition use `b01-c09` (hyphen). Cite-index
      header uses `b01-c09`. Proto-lines header uses `b01c09`.
    why: >
      Pre-existing pattern (observed in prior audit). No structural downstream
      consequence — the stitcher anchors on the scene-map, which uses `b01c09`. Does
      not cause misrouting. Advisory.
    note: no fixer action warranted. Candidate for a project-level slug-format
      normalization pass at book close.

  - id: signal-con-001
    type: flag
    class: CONSTRAINT
    what: >
      exposition:3 @11 (scene-open-orient) fires at the same anchor where loc-state:3
      @11 also fires. The scene-open-orient conditional fire-rule clause (b) states:
      "if loc-state fires at the scene-open anchor, the scene-orient is wallpaper."
      Loc-state:3 @11 establishes the evening Dragonpit-margin setting (time, place,
      weather, conditions). The exposition:3 carries the "second-circuit same-day
      relation" framing ("That evening, the second circuit ran the Dragonpit margin —
      the outer lanes south, toward the hill").
    why: >
      The exposition file's fire-audit argues the second-circuit same-day relation is
      distinct content not carried by loc-state:3, and the entry is pre-licensed by
      bones-review follow-001. The argument is defensible: loc-state:3 holds the
      environmental state (evening, hill-lane, lane-open); it does not name the
      circuit-sequence relation (this is the second circuit, on the same day). The
      clause-b refusal condition's rationale is that loc-state carries the
      "time/place" — here it carries the location and time-of-day, but not the
      circuit-continuity relation the stitcher needs to prevent the scene pivot from
      reading as a new-day skip. Advisory flag; not a HARD.
    note: no fixer action warranted. The stitcher should render the scene-bridge as
      genuinely additive to the loc-state's at-establishment content.

  - id: signal-apscan-001
    type: flag
    class: AP-SCAN
    what: >
      narrator:6 @23: "the wax comes down under her hand at the weight she has already
      settled; the packet is closed, and what the packet holds is the only thing the
      channel will ever see." The second clause — "what the packet holds is the only
      thing the channel will ever see" — is a substrate-boundary statement rendered in
      Taylor's voice.
    why: >
      Scene-C protected-patterns: "moral_legibility_to_self HELD at rank 5 — the gap
      exists in the material arrangement... NOT in Taylor's named recognition. Do NOT
      add interior weighing / naming / recognition at stitch." The clause as written
      frames what the channel sees as a substrate fact, not as Taylor naming the
      omission-as-withholding. It is on the right side of the line: it states the
      channel's content (what flows through), not the gap between that content and
      what exists in other substrates. However the phrase "the only thing" carries a
      limiting frame that could, at stitch, shade toward Taylor recognizing the limit.
      The stitcher must render this as a channel-technical statement (this is the
      deliverable's substrate-content) and not as Taylor perceiving the boundary as
      a withholding. Advisory for Phase 6 stitcher — this is the load-bearing edge
      of the moral_legibility hold.
    note: no fixer action warranted unless the stitcher produces a recognition-read
      at this beat, at which point the NI entry's second clause should be trimmed to
      the physical act only.

---

## Sensory old-state lineage confirmation (pl-2026-06-01-002 mechanized check)

All six sensory entries have old-states that resolve to loc-state baselines. Confirmation per entry:

| Entry | Old-state | Anchors to | Loc-state field |
|---|---|---|---|
| sensory:1 @11 | stone-lane-late-morning-warmth | loc-state:1 @1 | "cold-season morning lane-stone, dry-stone pre-damp register... grounds the cold-season morning that carries to the @11 hill-lane thermal" |
| sensory:2 @14 | lane-ambient-empty-distribution | loc-state:3 @11 | "no non-baseline body present (thermal/light/visual; scene-B baseline — anchors... sensory:2 @14 light old-state lane-ambient-empty-distribution)" |
| sensory:3 @27 | wax-soft-warm | loc-state:5 @21 | "tactile-prop-baseline: sealing-wax pliable-warm pre-application (anchors sensory:3 @27 old-state wax-soft-warm)" |
| sensory:4 @3 (depth-pass ADD) | dry-stone | loc-state:1 @1 | "dry-stone pre-damp register named explicitly... anchors sensory:4 @3 old-state dry-stone" |
| sensory:5 @9 (depth-pass ADD) | warm-hand | loc-state:1 @1 | "sensory:5 @9 old-state warm-hand cold-season-morning context" |
| sensory:6 @15 (depth-pass ADD) | unburdened-shoulders | loc-state:3 @11 | "sensory:6 @15 old-state unburdened evening-cold context" |

Verdict: ANCHORED (all 6). No unanchored old-state. The loc-state file was re-anchored at the depth pass and explicitly names each sensory old-state as a sensory-baseline field. pl-2026-06-01-002 mechanized check: PASS.

---

## Class-level verdicts (summary)

- STRUCTURAL: PASS — all 27 anchors resolve; bidirectional citations match; IDs monotonic; scene-map 27/27.
- FREQUENCY-BAND: 3 SIGNAL (sensory non-exempt marginal advisory; feeling denominator-collision; exposition sparsity + bridge-length carry-forward). No HARD.
- METADATA-INCONSISTENCY: 1 SIGNAL (slug format inconsistency b01c09 vs b01-c09 across headers). No HARD.
- CURVE-SHAPE: PASS — NI spine, memory, sensory, and vibes distribution compatible with rising dramatic_shape + falling-to-thesis-image scene-C close.
- CONTRADICTION: PASS — no cross-facet state contradiction.
- DEDUP: PASS — no duplicate entries within or across files.
- SUPERFLUOUS: PASS — no entries surviving Q1+Q2 with zero load.
- CONSTRAINT: 1 SIGNAL (exposition:3 @11 scene-open-orient fires where loc-state also fires; clause-b is defensible on distinct-content grounds; pre-licensed by follow-001). Earth-Bet fence clean. Scene-map coverage 27/27. Exposition source-traceability clean. @9 NI de-fog + sensory:5 co-citation: PASS.
- AP-SCAN: 1 SIGNAL (narrator:6 @23 substrate-boundary statement at the moral_legibility-hold edge; advisory for stitcher). No saturation finding.
- TASTE-FLAG: PASS — all voice register in-character; somatic-tell discipline clean.
- PILE-UP: PASS — no proto-line exceeds 4 co-located entries; densest bones (@6, @18) = 4.
- RUBRIC-FIDELITY: PASS — carve-out annotations present and complete; memory peak-bone exception cleared; feeling card-match satisfied; vibes op-coherence and token-structure clean; sensory old-state lineage ANCHORED (all 6).
