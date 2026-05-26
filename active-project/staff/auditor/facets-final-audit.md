audit:
  scope: chapter
  target: b01c03
  timestamp: 2026-05-26
  mode: flag-only (R2-skipped; R1-only output)
  auditor-note: >
    R2 was SKIPPED under cascade-budget. All twelve classes run against R1-only output.
    R2-sensitive gap: HARD findings that R2 judges (R2.1 NI, R2.5 exposition, R2.6 dialogue)
    would ordinarily catch are surfaced here as HARD; fixer resolves rather than re-running R2.
    HARD count: 3. SIGNAL count: 4.

  findings:

    - id: fault-001
      type: fault
      what: >
        CONSTRAINT (exposition scene-orient fire-rule clause b) — exposition:5 @13,
        scope: scene-open-orient, renders-as: scene-bridge ("After the morning crowd,").
        The fire-rule for scene-open-orient requires REFUSAL when loc-state fires at the
        scene-open anchor. loc-state:2 @13 fires in location-state-b01-c03.md (entry 2,
        anchored at @13, establishing the cooper's yard environment). Clause (b) of the
        conditional fire-rule is therefore violated: the lens facet carries the
        scene-B orientation; the scene-open-orient entry is wallpaper.
        The exposition file's own fire-audit (fire-audit block, @13 entry) claims
        "loc-state at @13: NOT FIRED (c03 location-state file not yet authored at this
        writing pass)" — this claim is factually incorrect. The location-state file
        was authored before the exposition file per the Phase 1 parallel fanout; entry 2
        exists and anchors at @13. R2 judge (R2.5 exposition, full-graph-aware) would
        have caught this; R2 was skipped.
      why: >
        At Phase 5b (audience-gate) and at stitcher Phase 1 fold-in, both loc-state:2
        and exposition:5 will fire at @13. The stitcher receives redundant scene-B
        orientation (loc-state carries yard + time + foot-traffic; exposition:5 supplies
        "After the morning crowd," — which the loc-state already contextualizes). The
        schema's scene-open-orient fire-rule exists precisely to prevent this: the lens
        facet carries, exposition stays out. The s01e01 dogfood validated this routing
        when the Phase 2 graph-aware exposition judge refused 11 of 11 scene-orient
        entries the Phase 1 blind author had fired.
      criteria: >
        exposition:5 @13 must be deleted from exposition-b01-c03.md. No other
        exposition entry is affected. After deletion, the per-episode counts become:
        1 prior-episode-bridge + 1 episode-open-context + 5 first-mention entries +
        0 scene-open-orient = 7 entries total. All per-episode caps remain satisfied.

    - id: fault-002
      type: fault
      what: >
        AP-SCAN saturation (URI-AP-SCAN-SATURATION) — interest-narrator-b01-c03.md.
        Predicate-nominative template ("X was/is the Y") across 4 of 8 NI entries:
          NI:1 @4  "stillness in a market is the cost-tell"
          NI:3 @8  "the count was the size of the leverage he was offering not to use"
          NI:5 @19 "the overlap was the price-tag he had not yet read aloud"
          NI:7 @29 "a day was the smallest unit of deferral the trade-shape would accept"
        Hit rate: 4/8 = 50%. Saturation threshold: hits/total >= 0.40 in a facet whose
        FREQUENCY-BAND ceiling is <= 25% (NI ceiling: 25%). 50% >= 40% threshold.
        Escalation: SIGNAL -> HARD per saturation rule.
      why: >
        At 50% template saturation the reader encounters the construction as a formal
        pattern before engaging with the content — the "reading the construction before
        the content" failure mode the b01c01 audience flagged on narrator-interest.
        The four affected entries span all three scenes (NI:1 scene-A, NI:3/5 scene-B,
        NI:7 scene-C), so the saturation is chapter-wide. Downstream: stitcher Phase 5
        voice-transform will compress redundant constructions; saturation at the facet
        layer produces flattened interiority even before prose rendering.
      criteria: >
        At least 2 of the 4 predicate-nominative entries must be rewritten to a
        different syntactic construction that preserves the semantic content (the
        recognition, the leverage, the price-tag, the deferral unit) without the
        "X was/is the Y" template. Revised entries must remain within the 15-25%
        NI density band and must not introduce named-feeling vocabulary or other
        NI anti-patterns. The remaining 2 entries may retain the construction if
        their anchor positions warrant it on rubric grounds (NI:3 @8 is the scene-A
        peak-bone; NI:7 @29 is the scene-C peak-bone — these are the stronger
        retention candidates).

    - id: fault-003
      type: fault
      what: >
        RUBRIC-FIDELITY (state-updates rubric § Cross-facet contract) —
        state-updates.md Taylor POV NI co-citation gap.
        The Taylor actor-slice self-declares the cross-facet contract: "each
        actor:taylor.* entry requires narrator-interest co-citation at the same anchor"
        and names anchors expecting NI co-fire: @4, @7, @8, @10, @14, @19, @22,
        @23, @29, @31, @33, @36.
        NI entries exist at: @4 (NI:1), @7 (NI:2), @8 (NI:3), @19 (NI:5),
        @23 (NI:6), @29 (NI:7). NI is ABSENT at @10, @14, @22, @31, @33, @36.
        Seven Taylor-actor state entries on six anchor positions lack required
        NI co-citation:
          state:29 @10  tether-prot-rise-ledger: court-layer-added-partial -> full
          state:30 @14  body-posture: still-on-recognition -> still-on-shed-wall
          state:32 @22  feed-mode: actively-counting-inventory -> mapping-against-coverage
          state:35 @31  position-with-patron: courier-named-function -> engaged-interlocutor
          state:36 @33  feed-mode: mapping-against-coverage -> confirming-Jarvis-exit
          state:37 @36  body-posture: still-on-shed-wall -> leaving-yard
          state:38 @36  feed-mode: confirming-Jarvis-exit -> still-running
      why: >
        The rubric requires NI co-citation for every POV actor-state entry so the
        stitcher receives both the state-delta and the POV's registration of that
        delta. Without NI at these anchors, the stitcher renders naked state-changes —
        the reader sees what changed without experiencing Taylor's accounting of the
        change. Load-bearing gaps: @10 (tether-prot-rise-ledger closes to full — the
        court-layer commitment completes; +1.0 axis move), @22 (feed-mode enters
        mapping-against-coverage — the coverage-assessment phase that precedes the
        scene-B peak), @31 (position-with-patron flips to engaged-interlocutor — the
        structural confirmation of non-refusal, a load-bearing chapter-close axis move).
        R2 judge (R2.1 NI, add-cap 5) would have been the standard resolution path;
        R2 was skipped.
      criteria: >
        NI entries must be added at the six uncovered anchor positions. At minimum,
        @10 (court-layer close), @22 (feed-mode → mapping), and @31 (engaged-
        interlocutor) are structurally load-bearing and require NI coverage per the
        cross-facet contract. For @14, @33, and @36 (posture-lock, exit-confirm,
        chapter-close), fixer may apply the rubric's necessity test and write a
        documented defense if the anchor does not independently warrant NI under
        the test; absence of NI at a defended anchor satisfies the contract if the
        defense is on-file. Each added NI entry must be in Taylor's clinical-accounting
        register, register what the state-change means to her accounting at that beat,
        and not duplicate content carried by the nearest existing NI entry.

    - id: fault-004
      type: flag
      what: >
        FREQUENCY-BAND — feeling.md density marginally above ceiling.
        2 entries / 36 bones = 5.56%. Rubric ceiling for feeling: 5%.
        The ceiling corresponds to 1 entry per 20 bones; at 36 bones the implied
        cap is 1.8 entries. Both entries are on scene-peak anchors (@23 scene-B
        peak, @29 scene-C peak). Overshoot: 0.56 percentage points.
      why: >
        The ceiling exists to keep somatic-tell content sparse enough to register as
        significant. The overshoot is marginal and both entries are on the highest-
        pressure bones in the chapter; the practical stitcher impact is low. R2.3
        feeling judge would have applied the per-character per-scene cap (<=1 hard)
        and the multi-justification test (>=3 of 5); R2 was skipped. Both entries
        clear the per-scene cap (1 per scene: feel:1 in scene-B, feel:2 in scene-C).
        Flagged per rubric — the band is mechanical and the audit reports all breaches.

    - id: fault-005
      type: flag
      what: >
        AP-SCAN AP8 (sentence-parsability) — vibes-b01-c03.md entry 8 @23,
        target: episode + prohibition-now-ledger-term,
        keyword array includes token: "audience-legible-before-taylor-completes-accounting".
        The token contains the embedded clause "taylor-completes-accounting" which
        parses as subject (taylor) + finite verb (completes) + object (accounting).
        Vibes schema § token: "A token is forbidden if it parses as a complete sentence
        with subject + finite verb + object." The clause is subordinate but sentence-
        parsable as an independent unit.
      why: >
        Vibes tokens are word-algebra operator-bias; sentence-parsable tokens breach
        the non-prose discipline and create rendering ambiguity if a downstream operator
        reads the token as a prose fragment. The entry is on an episode-scope target,
        so the impact is limited to episode-level vibe-cloud bias; but the schema rule
        is absolute. R2 vibes judging does not run (showrunner R1 vibes stands unless
        audit flags); this is the authoritative catch.

    - id: fault-006
      type: flag
      what: >
        AP-SCAN (POV-adjacent interiority) — vibes-b01-c03.md entry 12 @31,
        target: actor:jarvis-coin-kl-courier ++ transactional-flat-affect,
        token: "non-refusal-registered-without-visible-relief".
        The token "non-refusal-registered" attributes an interior register-event to
        a non-POV character (Jarvis registered the non-refusal). Compare with
        vibes:12's own companion tokens — "unhurried-departure-matching-unhurried-
        arrival" and "departure-matching-arrival-register" — both describe observable
        behavioral register without naming interiority. "Non-refusal-registered" does
        not meet the same standard; "registered" is interior-vocabulary even when
        qualified by "without-visible-relief."
        The c02 Phase 5 audit (PROP-0006) identified this exact pattern: vibes keyword
        arrays on non-POV characters using "registered" attribute non-POV interiority.
      why: >
        Operator-bias tokens on non-POV characters should describe observable position,
        function, or behavioral register — not internal registration events. The token
        as written biases downstream operators toward Jarvis's interior processing,
        which is out-of-POV. Single-entry hit at 1/12 = 8% of vibes entries — below
        the AP-SCAN saturation threshold (40%); SIGNAL, not HARD. Severity reflects
        that the companion tokens are clean; only this one token in the entry breaches
        the observable-register discipline.

    - id: fault-007
      type: flag
      what: >
        RUBRIC-FIDELITY (memory-flags rubric § pressure-signal alignment) —
        memory-b01-c03.md inverted quiet-to-peak ratio.
        Distribution: 2 peak-bone fires (mem:1 @8 scene-A peak; mem:2 @23 scene-B
        peak) + 1 quiet-zone fire (mem:3 @34 scene-C trail). Quiet-to-peak ratio: 1:2.
        Rubric preferred ratio: >= 3x quiet-to-peak (quiet-beat distribution preferred;
        peak-bone fires require displacement-clamp construction exception). File
        documents both peak fires under displacement-clamp exception, defended on
        hinge-chapter structural grounds (the chapter peaks ARE the displacement cues;
        NI carries peak information; memory carries the resonance underneath).
      why: >
        The defense is documented and structurally coherent; auditor does not
        override it. Surfaced as SIGNAL because: the inverted ratio means the memory
        layer concentrates at peaks rather than quiet zones, which reduces the
        chapter's interiority density in the trail sections (scene-C @26-@36 has
        only mem:3 @34 in a quiet position). If the audience-gate had run (Phase 5b
        not completed under R2-skip cascade), the memory concentration at peaks
        would be one attack vector for a revise verdict from a persona reading
        for interiority texture. Advisory for Phase 5b when it fires.

---

# Audit summary

HARD count: 3
SIGNAL count: 4
Headline: FINDINGS-PRESENT — Phase 5b BLOCKED until 3 HARD findings resolved.

## HARD findings requiring fixer dispatch

fault-001 (CONSTRAINT scene-orient fire-rule): delete exposition:5 @13 from
  exposition-b01-c03.md.

fault-002 (AP-SCAN saturation NI predicate-nominative 50%): rewrite >= 2 of 4
  "X was/is the Y" entries in interest-narrator-b01-c03.md to distinct syntactic
  construction.

fault-003 (RUBRIC-FIDELITY state-updates POV NI co-citation gap): add NI entries at
  @10, @22, @31 (load-bearing minimum); write necessity-test defenses for @14, @33,
  @36 if fixer judges those anchors below NI threshold.

## SIGNAL findings (advisory, no fixer dispatch required)

fault-004: feeling density 5.56% vs 5% ceiling (marginal; both entries on peak-bones).
fault-005: vibes:8 token "audience-legible-before-taylor-completes-accounting"
  sentence-parsable under AP8.
fault-006: vibes:12 token "non-refusal-registered" attributes interior-vocabulary
  to non-POV Jarvis; c02 PROP-0006 pattern recurrence.
fault-007: memory inverted quiet-to-peak ratio (1:2 vs >= 3:1 preferred);
  displacement-clamp exception documented.

## Clean classes (no findings)

STRUCTURAL: all headers, ID sequences, anchor resolutions, bidirectional citations,
  dialogue citations resolve cleanly. State-updates IDs 1-38 monotonic. Cite-index
  totals match facet file counts (78 entries, 27/36 decorated).

EARTH-BET HARD-FENCE: zero hits. Full token-level scan executed across all text
  fields of all 9 facet files and all 10 dialogue utterances (Jarvis 7 + Taylor 3).
  Keyword arrays in vibes, NI rationale, memory target-refs, state-updates field
  values, sensory notes, dialogue objective and utterance text — all clean.
  Particular attention to vibes:1 "feed-ghost" (permitted: insect-feed compound,
  not Earth-Bet noun); exposition preamble "the flies / the count / the work"
  (permitted: function-description substitution register per cond-earth-bet-noun-fence).

METADATA-INCONSISTENCY: NI header density 8/36 = 22% matches body. Feeling
  entry_count: 2 matches body. Metaphor entry_count: 0 matches body. Vibes
  entries_count: 12 matches body. State-updates note 10+13+15=38 matches body.
  Cite-index totals 78 match per-facet sum.

CURVE-SHAPE: scene-map sequence (rising -> rising-to-peak -> peak-and-trail) is
  coherent with dramatic_shape: hinge. Hinge arc requires building -> peak pivot ->
  trail; the sequence delivers this across three scenes. Peak-bones present in all
  three scenes (@8, @23, @29). No scene is peakless. SHAPE-OK.

CONTRADICTION: no same-anchor incompatible state found. Sequential state transitions
  on the same field (time_of_day: morning -> third-bell-noon at @1 then @7) are
  sequential, not contradictory.

DEDUP: no utterance/NI/feeling content overlap. Dialogue speaks content; NI registers
  accounting significance; feeling shows somatic tell — three distinct channels at
  peak-bone pile-ups. Vibes tokens are not rendered as prose; no dedup issue with
  NI/feeling content.

SCENE-MAP COVERAGE (URI-SCENE-WINDOW): 36/36. scene-A @1-@12 (12 bones),
  scene-B @13-@25 (13 bones), scene-C @26-@36 (11 bones) = 36 total. No gaps,
  no overlaps, no dangling anchors. Frontmatter total-scenes: 3, total-bones: 36
  match body.

DIALOGUE-COVERAGE: all 10 dialogue-anchor bones cited (flat_ids 6, 8, 10, 11, 16,
  18, 20, 24, 29, 31 each carry >= 1 [character-slug:id] token). Both speaker files
  present (jarvis-coin-kl-courier.md, taylor-hebert-kl-122ac.md).

PILE-UP REVIEW: all 6 pile-ups (>= 5 co-located facets at @1, @8, @13, @16, @23,
  @29) are warranted. Each pile-up is at a scene-open or peak-bone structural beat
  where multiple load-bearing channels independently fire on distinct content.

CONSTRAINT (partial clean): memory NI-spine present for all 3 memory entries (@8
  NI:3, @23 NI:6, @34 NI:8). Metaphor zero-fires — no license or anchor violations
  possible. Feeling non-duplication of POV NI confirmed (somatic-tell vs cognition
  register). Vibes licensed-by fields present on all 12 entries with resolvable
  source references. Exposition source-traceability: every gloss claim cites sources
  in the entry. Exposition license-completeness: all entries carry >= 1 persona-card
  slug (cape-fic-reader, dark-fantasy-reader, worm-canon-pedant) with specific gap
  claims. Exposition re-gloss check: no b01c03 entry re-glosses a term already in
  glossed-terms.md from b01c01 or b01c02. Exposition first-mention-character
  coverage: narrator-prose first-mention of Jarvis at @3 is covered by exposition:3.
  Dialogue behavior-card-compliance: all Jarvis utterances in courier-transactional
  register (declarative sentences, fragments, no em-dashes or semicolons, no
  modern-HR-speak or deposition cadence). Taylor utterances in minimal-register
  (three-word maximum; no elaboration; form matches card §voice compression).
  Memory target-refs (cond-override-architecture-residue-122ac,
  cond-road-to-hell-chain-shape) resolve to cards/conditions/. PASS.

RUBRIC-FIDELITY (partial clean): memory doubled-register test passes (1 Earth-Bet
  displacement + 2 Westerosi-monument clamps). Sensory modality distribution: 2
  entries, 2 distinct modalities (smell @1, sound @13), no single modality dominance.
  loc-state anchor verbs all in transitional/positioning/event ACCEPT class. No
  loc-state continuity-carry entries in this file (no "continuity-from" syntax used;
  loc-state:4 @26 is an independent entry with its own sensory note, not a carry).
  State-updates registration-vocabulary: no REJECT-signature registration terms
  appear in Taylor-slice <new> field values (moral_framework-position, feed-mode,
  body-posture, tether-prot-rise-ledger, observation-status, position-with-patron
  values are all operational-state descriptors without "noticed"/"registered"/
  "awareness"/"baseline" vocabulary).

## Routing

fault-001 -> fixer; target: exposition-b01-c03.md; delete entry 5.
fault-002 -> fixer; target: interest-narrator-b01-c03.md; rewrite >= 2 entries.
fault-003 -> fixer; target: interest-narrator-b01-c03.md (NI adds at @10, @22, @31
  required; defenses for @14, @33, @36 if below necessity threshold).
fault-004 through fault-007 -> advisory; no fixer dispatch; carry to Phase 5b.
