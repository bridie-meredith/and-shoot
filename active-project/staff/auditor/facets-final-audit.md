```yaml
audit:
  scope: chapter
  target: b01c09
  timestamp: 2026-06-01
  headline: CLEAN — HARD: 0 (non-deferral), SIGNAL: 4
  phase5b_verdict: CLEAN-FOR-PHASE-5b
  earth_bet_fence: CLEAN
  scene_map_coverage: CLEAN (23/23 bones, no gaps, no overlaps)
  findings:

    # ── PASS findings ────────────────────────────────────────────────────────

    - id: pass-001
      type: pass
      what: >
        Cite-index bidirectional verification — all 33 facet entries.
        back=Y on every anchored entry. @- correctly used for vibes:4 and
        vibes:7 (episode-scope; no single-bone anchor). exposition:1 @0
        back=N is structurally correct (@0 synthetic preamble has no
        proto-line back-citation).
      why: No stale or broken citations found.

    - id: pass-002
      type: pass
      what: >
        Earth-Bet hard-fence scan across all facet text fields (all nine
        files). memory target slugs monument-movement-routing-without-consent
        and monument-faction-war-foreknowledge are metadata identifiers, not
        rendered prose; the prose bodies that carry them use Westerosi-register
        language throughout. exposition file's inline Earth-Bet fence audit
        section corroborates.
      why: No Earth-Bet proper nouns in any rendered prose field. CLEAN.

    - id: pass-003
      type: pass
      what: >
        Scene-map coverage (URI-SCENE-WINDOW): scene-A @1-@7 (7 bones),
        scene-B @8-@16 (9 bones), scene-C @17-@23 (7 bones). Total = 23.
        Scene-map coverage field: 23/23 bones in exactly one scene. Gaps
        and overlaps fields both empty.
      why: All 23 bones map to exactly one scene. CLEAN.

    - id: pass-004
      type: pass
      what: >
        Cross-facet actor-state / narrator-interest co-citation contract.
        state:5 @6 (actor:taylor relational_anchor_status 2->2.5): cite-index
        confirms co=[mem:1, narrator:2] — narrator:2 @6 present.
        state:6 @14 (actor:taylor political_register-prot 2.5->3): cite-index
        confirms co=[mem:2, narrator:4, vibes:5] — narrator:4 @14 present.
      why: Both mandatory cross-facet contracts satisfied.

    - id: pass-005
      type: pass
      what: >
        Curve-shape vs. dramatic_shape rising. Scene-A rhythm-shape
        rising-to-quiet-peak; scene-B rising-to-quiet-peak; scene-C
        falling-to-thesis-image (structural close). Narrator-interest fires
        at @4, @6, @11, @14 (rising through scenes A and B) with terminal
        anchor at @19. Vibes escalate through scenes A (atonement-as-repetition
        ++, rising-entrapment ++) and B (political-register-color-present ++).
      why: Pattern is consistent with rising dramatic shape closing on a
           structural thesis-image. No contradiction found.

    - id: pass-006
      type: pass
      what: >
        Exposition source-traceability — all 3 entries. exposition:1 @0:
        every claim traces to handoff_in/out, scene chunks, and glossed-terms
        entries. exposition:2 @9: every claim traces to cond-kl-geography,
        cond-kl-court-state, scene chunk, and scene-map. exposition:3 @8:
        every claim traces to scene-map scene-B, bones-review follow-001
        (pre-licensed), and bone @8.
      why: No claim in any entry is absent from its source list. CLEAN.

    - id: pass-007
      type: pass
      what: >
        Exposition first-mention coverage — mandatory new locations and terms.
        The Dragonpit lower gate (chapter's sole new load-bearing location)
        fires at exposition:2 @9 with the minimum Green/Black faction-frame
        folded in (fuses two cold-read gaps into one entry). Wren and Corwick
        are register-resident (re-gloss hard-blocked) and are refreshed via
        bridge restatement in the @0 prior-episode-bridge, not a gloss entry —
        documented as correct per c08 precedent. Coverage-instrument-family,
        feed-station, and substrate-split apparatus are register-resident or
        plot-content; none require first-mention entries.
      why: No mandatory first-mention gap identified.

    - id: pass-008
      type: pass
      what: >
        Sensory SEAM-011 and SEAM-012 cross-check against authored loc-state
        graph. SEAM-011 (sensory:1 old-state "stone-lane-late-morning-warmth"):
        loc-state:3 @8 establishes the dragonpit-margin at evening — it does
        not contradict the hook-ward morning thermal (the prior-state the
        transition departs from). SEAM-012 (sensory:3 old-state
        "lane-ambient-empty-distribution"): loc-state:4 fires AT @11 registering
        Corwick's presence; there is no loc-state entry naming a body-presence
        in the dragonpit-margin BEFORE @11, so the old-state claim is
        uncontradicted.
      why: Both SEAM checks pass against the authored graph. No residual
           contradiction.

    - id: pass-009
      type: pass
      what: >
        Pile-up check across all proto-lines. Cite-index pile-up section:
        "(none)" for entries exceeding 4 facets co-located on one proto-line.
        Highest co-citation density is 4 entries at @14 (mem:2, narrator:4,
        state:6, vibes:5) — at the threshold, not above it.
      why: No pile-up faults.

    - id: pass-010
      type: pass
      what: >
        Dialogue coverage gate (URI-WRITE-DIALOGUE-COBONDED / silent chapter).
        Scene-map: "dialogue: none (silent chapter — zero dialogue-anchor bones;
        no per-character dialogue files emitted)." 23-bone verb-set contains
        zero speech-act verbs (confirmed by exposition file's speech-bone
        construction pass). PROP-0001/DEC-0010 dialogue-adjacent fold-in fence
        does not trigger in a silent chapter.
      why: No dialogue-coverage fault applicable. CLEAN.

    - id: pass-011
      type: pass
      what: >
        Grounding-ledger grd-001 resolution. grounding-ledger-b01-c09.md entry
        grd-001 status: "satisfied" by sensory:3; resolved_at and satisfied_by
        fields populated. sensory:3 @11 carries "licensed-grounding-exception:
        grd-001" and the sensory file's density record marks it cap-exempt.
      why: No dangling licensed-grounding-exception. CLEAN.

    - id: pass-012
      type: pass
      what: >
        Context-ledger — no CONTEXT-REQUIRED gaps. context-ledger-b01-c09.md
        entries: [] with explicit NOTE that Axis-1 completeness verdict is PASS.
        Bones-review follow-001 pre-flagged carry (@8 temporal pivot) confirmed
        closed by exposition:3 @8 scene-open-orient.
      why: No open context-required items remain.

    - id: pass-013
      type: pass
      what: >
        AP-SCAN new-plot-content check — exposition entries. exposition:2 @9:
        gloss does not invent household identity; says only "bodies on the
        heir's business pass" (faction-adjacency read); consistent with
        cond-kl-court-state §for-narrative-use (Taylor has inference, not
        court-level intelligence). exposition:1 and exposition:3: every claim
        traces to documented sources; no new-plot-content introduced.
      why: CLEAN.

    - id: pass-014
      type: pass
      what: >
        Deduplication check. vibes:1, vibes:2, vibes:3 co-anchor at @4 but
        cover distinct actors and keyword bundles (atonement-as-repetition /
        rising-entrapment / cost-bearer rising-entrapment — three different
        targets). mem:1 @6 and state:5 @6 carry different facet-class content
        (memory resonance vs. axis-state write). No cross-facet semantic
        duplication identified.
      why: CLEAN.

    - id: pass-015
      type: pass
      what: >
        R2 absence — DEC-0063 Option B. R2 was deliberately SKIPPED; the R1
        graph is final. Absence of .r2-decisions.md is correct under this
        decision.
      why: Not a defect.

    # ── SIGNAL findings ───────────────────────────────────────────────────────

    - id: signal-001
      type: flag
      what: >
        Exposition frequency-band — 3/23 = 13.0%, above the standard 1-5%
        rubric band. Out-of-band by count.
      why: >
        The exposition file documents the justification as denominator-driven
        (23-bone lean quiet chapter), bridge-suppression (the @0 bridge carries
        two register-blocked figure refreshes suppressing two otherwise-required
        entries), and fusion-minimized (two cold-read gaps fused into one @9
        entry). All three entries are individually mandatory per their sourcing;
        removing any one fails a rule or leaves a pre-licensed gap open.
        Not HARD — out-of-band state is fully documented with per-entry
        mandatory arguments. Signal for reviewer awareness only; no fixer
        action warranted.

    - id: signal-002
      type: flag
      what: >
        sensory-b01-c09.md header field: "loc-state: theater/facets/
        location-state-b01-c09.md (not yet authored — seam flagged below)"
        — stale documentation artifact.
      why: >
        The loc-state facet IS authored and populated (5 entries, all back=Y).
        The "not yet authored" note is a stale artifact of the R1 blind-authoring
        sequence. No downstream consequence — SEAM-011 and SEAM-012 both pass
        against the actual loc-state entries (see pass-008). Stale documentation
        note only; no fixer action warranted.

    - id: signal-003
      type: flag
      what: >
        vibes:4 off-anchor (loc:the-hook-ward, @-, no formal warehouse card)
        with gate-1 carve-out invoked.
      why: >
        Vibes rubric gate 1 requires the target slug to exist in the card
        library. the-hook-ward has no card at cards/locations/ or
        active-project/warehouse/. The vibes file documents the c08 carve-out
        precedent (vibes-b01-c08.md carve-out preamble for the same location
        and keyword; the c09 entry is a ++ extension of the carve-out-established
        keyword, not a fresh add). Not HARD because carve-out is documented and
        the c08 precedent is established. Card-promotion task (the-hook-ward
        to warehouse) is the correct downstream resolution — margit dispatch
        recommended.

    - id: signal-004
      type: flag
      what: >
        Memory rubric default-forbidden path: both mem:1 @6 and mem:2 @14
        fire on peak-bones (the default-forbidden case; requires the peak-bone
        exception).
      why: >
        The memory file documents the exception with explicit reasoning: NI-spine
        in a rising chapter forces all co-citable bones to be peak-bones (no
        non-peak bone in this chapter carries NI co-citation). The peak-bone
        carve-out two-part test (displacement-clamp + resonance-not-action) is
        cleared per the inline annotations for both entries. Pressure-signal-
        inversion ratio of 0 is documented as an NI-spine artifact of a rising
        chapter, not density-inflation. Not HARD — carve-out is documented with
        explicit test results. Signal for reviewer awareness.

    # ── CARRY-FORWARD DEFERRALS (DEC-0063) ───────────────────────────────────
    # Classified SIGNAL per dispatch briefing. Each has a documented carve-out
    # or defense inline. None count toward the HARD gate.

    - id: deferral-001
      type: flag
      what: >
        corwick — referenced in proto-lines cast header and in bones
        (@11, @12, @13, @14) without a formal actor card in
        active-project/actors/.
      why: >
        Same pattern as wenna-cobb in c08, which shipped under the same
        carve-out. Uncarded figure with inline chapter-internal mentions;
        margit referral owed. No HARD reference fault per DEC-0063 and c08
        precedent.

    - id: deferral-002
      type: flag
      what: >
        Uncarded descriptive geography slugs used in location-state entries:
        oc-hook-precinct, oc-stitch-house-lane, oc-dragonpit-margin, and
        the-feed-station (or their descriptive variants) lack formal warehouse
        cards.
      why: >
        c08 used uncarded descriptive location slugs routinely. Carve-out
        documented per DEC-0063; margit card-promotion owed. SIGNAL.

    - id: deferral-003
      type: flag
      what: >
        oc-props oc-jarvis-packet and oc-ward-coverage-notes used in
        state-updates.md without authored prop cards.
      why: >
        state-updates.md §Field-extension carve-out preamble documents both
        entries per design/shoot-v2/rubric-state-updates.md §Field-extension
        protocol. Margit referrals pending (b01c08 precedent). SIGNAL.

    - id: deferral-004
      type: flag
      what: >
        Memory target slugs monument-movement-routing-without-consent and
        monument-faction-war-foreknowledge — no warehouse cards; margit
        referral outstanding per pl-2026-05-25-005 monument-* class deferral
        precedent.
      why: >
        Glosses are structurally clear; displacement-clamp targets explicitly
        defined in the memory file with prose renderings. Margit referral
        owed. SIGNAL per briefing.

  summary:
    hard_count: 0
    signal_count: 4
    deferral_count: 4
    earth_bet_fence: CLEAN
    scene_map_coverage: CLEAN (23/23; no gaps; no overlaps)
    cross_facet_contracts: SATISFIED (state:5@6+narrator:2; state:6@14+narrator:4)
    grd001_resolution: SATISFIED (sensory:3 cap-exempt; ledger stamped resolved)
    context_ledger: PASS (no CONTEXT-REQUIRED gaps)
    phase5b_verdict: CLEAN-FOR-PHASE-5b
```
