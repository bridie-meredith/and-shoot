```yaml
audit:
  scope: chapter
  target: b01c18
  gate: /and-facets Phase 5 mechanical audit (flag-only, full-graph)
  timestamp: 2026-06-05
  headline: FINDINGS-PRESENT — HARD: 1 / SIGNAL: 5
  hard_to_proceed: 0
  note: >
    HARD count is 1 (fault-001). The HARD=0 requirement before the audience-gate is NOT
    met. fault-001 routes to fixer before the audience-gate fires. All five SIGNAL findings
    are advisory; none block.

  findings:

    - id: fault-001
      type: fault
      axis: STRUCTURAL / CONSTRAINT (vibes licensed-by — dangling bone reference)
      what: >
        vibes-b01-c18.md, entry vibes:17 — licensed-by field reads:
          "peak-bone:38, peak-bone:48"
        peak-bone:48 does not exist. The b01c18 bones file declares aggregate_range: 1-46;
        the chapter contains exactly 46 bones. Bone 48 is out of range.
      why: >
        A dangling licensed-by reference means vibes:17's second license token points to
        a non-existent bone. Any downstream consumer that validates licensed-by tokens
        against the bones range (auditor, stitch pre-flight, pipeline-review) will report
        a hard failure. The entry itself is otherwise well-formed — vibes:17 fires at @38
        (the chandler-quarter moths settle the eaves; s05 grounding anchor; sensory:4
        co-citation confirmed) and the structural rationale is sound. Only the stray
        peak-bone:48 token is defective.
      criteria: >
        vibes:17 licensed-by must reference only bones in the range 1-46. The token
        "peak-bone:48" must be removed or corrected. If the intent was peak-bone:46
        (taylor sets the stylus — the chapter's terminal bone; structurally adjacent to
        @38 in the s05 closing sequence), that is the candidate replacement; fixer must
        confirm the vibes rubric licenses @38 against @46 before substituting. If no
        second peak-bone is warranted beyond @38, the single-token form "peak-bone:38"
        is sufficient.

    - id: signal-001
      type: flag
      axis: STRUCTURAL (metaphor facet ID)
      what: >
        metaphor-b01-c18.md — entry id is meta:0. Standard facet entry IDs begin at 1.
        The cite-index logs this as "meta:0 @- back=-" with a null anchor.
      why: >
        meta:0 is a non-standard ID. The zero-entry metaphor disposition is substantively
        correct (default-refuse discipline; 0.0% within 0-3% band; cold-accounting register
        warrants zero per the rubric). The anomaly is the ID itself. If any downstream
        consumer enforces monotonic-starting-at-1 across facet entry IDs, meta:0 will
        fail the check. The null anchor (@-) is consistent with a zero-entry record
        but is similarly non-standard.
      criteria: null

    - id: signal-002
      type: flag
      axis: EARTH-BET FENCE (rationale-text surface)
      what: >
        exposition-b01-c18.md — the word "Khepri" appears multiple times in the file's
        comment and rationale lines (not in any numbered entry's gloss-text body). Specific
        locations: the opening fence-check comment block; the scene-B orient rationale
        (R2 note referencing KHEPRI-REGISTER-SPLIT); the cross-episode register write-back
        section (lines referencing COUNT-NAMED-IN-SHAPE-LANGUAGE and the prior-architecture
        echo fence). The Earth-Bet hard-fence scan targets EVERY text field of every facet
        entry including NI rationale.
      why: >
        The numbered gloss-entry bodies (exposition:1, :2, :3) are clean — no Earth-Bet
        proper nouns appear in the story-facing prose. However the audit instruction
        includes rationale text in the scan perimeter, and the exposition file's authoring
        comments are functionally rationale. Any downstream agent that reads the full
        facet file body (stitch, impersonator, renderer-minimal) will encounter "Khepri"
        in the comment layer. The exposition file's own fence-check comment declares
        "Fence CLEAN" for gloss-entry text; this signal is the auditor's independent
        surface of the rationale-text question for the record, not a contradiction of
        that declaration. Low contamination risk; the occurrences are clearly
        production-internal labels and fence-holding notes.
      criteria: null

    - id: signal-003
      type: flag
      axis: FREQUENCY-BAND (exposition total sparsity)
      what: >
        exposition-b01-c18.md — total sparsity is 3 entries / 46 bones = 6.5%, above
        the 1-5% band. The exposition author self-flags this: "same disposition as c14
        [6.5%] + c17 [5.6%] silent-chapter denominator effect." The two ctx-licensed
        entries (exposition:2 at @14 / exposition:3 at @30) are anti-exposition-penalty-
        EXEMPT and not R1-cull-eligible. The R2 condition that would bring sparsity
        in-band: if the lens facets (NI or loc-state) are found at R2 to already carry
        the @14 mode-distinction or the @30 window-mechanism, the corresponding
        scene-open-orient entry DELETEs and sparsity falls toward 2.2%.
      why: >
        Above-band total exposition is a signal for R2 review. The out-of-band condition
        is characterized and contingent on lens-coverage findings; it does not block the
        audience-gate but should be checked at R2 before stitch dispatch. If neither ctx
        entry deletes at R2, the 6.5% figure stands at the same level as the two prior
        silent chapters (accepted precedent).
      criteria: null

    - id: signal-004
      type: flag
      axis: STRUCTURAL (exposition:1 virtual anchor)
      what: >
        exposition-b01-c18.md entry exposition:1 anchors at @0. The cite-index records
        this as "exposition:1 @0 back=N." @0 is not a bone in the 1-46 range; it is a
        virtual anchor for the prior-episode-bridge entry. No proto-line cites
        exposition:1 (back=N is expected for this entry type).
      why: >
        This is structurally anomalous — the only facet entry in the full b01c18 graph
        whose anchor is outside the 1-46 bone range. The @0 prior-episode-bridge
        convention is consistent with prior chapters (c14/c17 self-cited precedents);
        the entry does not need a proto-line citation by design (it fires pre-chapter
        at the episode-open). The anomaly is structural, not substantive. If any
        validator enforces "every facet entry anchor must be in 1-46," exposition:1 @0
        fails. Flagged for pipeline-review; not a blocking finding.
      criteria: null

    - id: signal-005
      type: flag
      axis: DEDUP / PILE-UP (stitch density watch)
      what: >
        _cite-index.md pile-up section — two bones carry 7 co-located facet citations
        each:
          @14 (7): exposition:2, narrator:3, state:15, state:16, vibes:1, vibes:2, vibes:3
            bone: "the architecture opens the nodes"
          @25 (7): mem:2, narrator:5, state:17, vibes:8, vibes:9, vibes:10, vibes:11
            bone: "the insect-feed returns the apparatus"
        Both are the chapter's declared peak-zone bones (moral_framework -1.0 at @14;
        political_register-prot +1.0 at @25). @26 carries 5 co-located entries.
      why: >
        Seven-facet pile-ups at the two peak bones are the chapter's highest-density
        co-location points. Stitch Phase 2 redundancy cull must resolve these without
        collapsing substance delivery. The scene-map's KHEPRI-REGISTER-SPLIT hard watch
        (@14/@15) and CONTEMPT-AS-MECHANISM-NOT-AFFECT hard watch (@25/@26) are both
        anchored at the pile-up nodes. At @14, the six facets carry distinct axis functions
        (exposition orients mode-change; NI carries architectural recognition; state:15/16
        record the threshold-crossing; vibes:1/2/3 carry the full vibe-payload); at @25,
        the seven facets each serve a distinct facet-type. Signal is informational — no
        structural fault — but the stitcher's Phase 2 cull priority should land on these
        nodes first.
      criteria: null
```

---

## Audit summary

**Status:** FINDINGS-PRESENT

| Metric | Value |
|--------|-------|
| HARD count | 1 |
| SIGNAL count | 5 |
| Earth-Bet fence (gloss-entry bodies) | CLEAN |
| Earth-Bet fence (rationale/comment text) | SEE signal-002 |
| Scene-map coverage | CLEAN |
| HARD=0 gate | NOT MET |

**Class breakdown:**

| Class | Verdict |
|-------|---------|
| STRUCTURAL | FINDINGS-PRESENT — fault-001 (vibes:17 peak-bone:48 out-of-range); signal-001 (meta:0 non-standard ID); signal-004 (exposition:1 @0 virtual anchor) |
| EARTH-BET FENCE | CLEAN on all numbered gloss-entry bodies; signal-002 flags "Khepri" in exposition rationale/comment lines |
| SCENE-MAP COVERAGE | CLEAN — 5 scenes partition bones 1-46 with no gaps or overlaps; total-scenes:5 and total-bones:46 frontmatter match |
| FREQUENCY-BAND | CLEAN — sensory-std 4.3% (band 3-6%); memory 6.5% (band 5-12%); feeling 2.2% (at floor, OK); NI 23.9% (band 15-25%); exposition-std 2.2% (band 1-5%); metaphor 0% (band 0-3%); vibes content-driven; signal-003 flags total-exposition 6.5% above band (contingent on R2 lens-coverage cull) |
| CONSTRAINT | FINDINGS-PRESENT — fault-001 (dangling licensed-by in vibes:17); all ctx-NNN licenses resolve in context-ledger; all grd-NNN licenses resolve in grounding-ledger; all memory NI-spine co-citations present; all actor state-update NI co-citations present; card-resolution on cond-override-architecture-residue-122ac and cond-kl-witch-label-formation-122ac confirmed resolvable |
| RUBRIC-FIDELITY | CLEAN — memory doubled-register met (Earth-Bet-displacement-via-shape at mem:1/@15 + mem:2/@25; Westerosi-monument at mem:3/@45); sensory old-state anchors present on all 5 entries; loc-state movement-verb gate clear; no per-facet REJECT-signature or anti-pattern matches found |
| CURVE-SHAPE | CLEAN — climax-establishment / climax-peak / climax-consequence / climax-consequence / climax-fall coherent with declared dramatic_shape: climax |
| DEDUP / CONTRADICTION | CLEAN — no duplicate entries, no contradictions detected; signal-005 flags pile-up density at @14 and @25 for stitch Phase 2 attention |

**Route:**
- fault-001 to fixer (vibes-b01-c18.md vibes:17 licensed-by field); audience-gate blocked until HARD=0 confirmed.
- signal-001 through signal-005 to facet authors for disposition; none block.
