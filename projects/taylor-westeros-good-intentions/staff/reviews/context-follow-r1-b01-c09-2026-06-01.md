review:
  type: context-followability + aliveness (PROP-0020 + PROP-0022)
  phase: /and-facets b01c09 Phase 2.5
  reviewer_disposition: CONTEXT-AWARE (read to chapter 8; NOT a cold read)
  target: b01-c09
  graph: active-project/theater/proto-lines/b01-c09.md (23 bones, R1-annotated)
  timestamp: 2026-06-01
  chapter_class: B (design-inherent omission-chapter, apparatus vocabulary; DEC-0062 — NOT re-litigated)
  scene_ranges: "scene-A @1-@7 (late-morning Hook/Wren) | scene-B @8-@16 (evening Dragonpit-margin/courier) | scene-C @17-@23 (end-of-day accounting)"

# ════════════════════════════════════════════════════════════════════════
# AXIS 1 — COMPLETENESS / FOLLOWABILITY (PROP-0020)
# Verdict: PASS. Zero CONTEXT-REQUIRED gaps. All carries confirmed closed/weave-fixable.
# ════════════════════════════════════════════════════════════════════════

axis_1_completeness:
  verdict: PASS
  context_required_count: 0
  findings:

    # ── The pre-flagged bones-review carry: follow-001 @8 ──────────────────
    - id: follow-001
      anchor: "@8"
      classification: OK   # CLOSED by R1 weave — see disposition
      symptom_at_bones_review: |
        scene-B pivot @8 ("enters the dragonpit-margin lane") is a location + time jump
        (late-morning Wren circuit @1-@7 → evening Dragonpit circuit @8) with NO temporal
        marker on the bone. same-day-evening vs later-day was slightly ambiguous; "evening"
        lived only in scene-map metadata. Flagged context-addable at Phase 2.5 (NOT FOLLOW-FAIL).
      disposition: CLOSED
      rationale: |
        CONFIRMED CLOSED by two converging R1 weave channels — no ledger entry needed:
        (1) exposition:3 @8 scene-open-orient FIRES: "That evening, the second circuit ran
            the Dragonpit margin — the outer lanes south, toward the hill." This is exactly
            the fill the bones-review pre-licensed: it carries (a) the same-day relation
            ("That evening"), (b) the SECOND-CIRCUIT scheduled-pass framing (resolves the
            same-day-evening-vs-later-day ambiguity → same day's later circuit), and
            (c) a light Dragonpit-margin place-orient distinct from the @9 gate-gloss.
        (2) exposition:1 @0 prior-episode-bridge pre-orients the southward coverage
            extension ("the count runs the Hook and four wards past it now, and the coverage
            extends … the feed has been threading her street since the boundary moved") — so
            a context-bearing reader arrives at @8 already holding the post-Rushwick
            south-push frame; the Dragonpit-margin pass reads as the coverage architecture
            returning to known ground, not an unanchored jump.
        loc-state:3 @8 (evening, Dragonpit-margin, supply-cart-on-gate-road) + sensory:1 @8
        (thermal: late-morning-warmth → hill-lane-evening-cool) independently corroborate the
        evening time-band at the physical layer. The follow-001 temporal/location gap is
        comprehensively closed; this is a WEAVE-FIXABLE that the R1 weave already fixed.

    # ── @9 / @14 the Dragonpit-gate + faction inference ───────────────────
    - id: follow-004
      anchor: "@9 → @14"
      classification: OK   # WEAVE-FIXABLE, already carried
      symptom: |
        @9-@10 introduce "the lower gate" / "lower gate side-exit" as a new load-bearing
        location; @11-@14 turn on a Black-faction-contact inference the reader must be able
        to place. Cold-read flagged "Dragonpit dropped in with zero referent" + "what faction
        does the lower-gate household belong to, and why does it matter."
      disposition: OK (weave carries)
      rationale: |
        exposition:2 @9 first-mention-place fires the fused gloss: "the lower gate — the
        Dragonpit's court-margin side, under Rhaenys's Hill, where bodies on the heir's
        business pass and not the Queen's: not a Green-faction gate." This orients the PLACE
        (Dragonpit court-margin under Rhaenys's Hill — closes the b01c03 embedded-noun trail)
        AND the minimum faction-axis (Queen's-side = Green / heir's-side = Black) WITHOUT
        pre-drawing the @14 conclusion. The @14 inference (NI:4 "the wrong-hour and the
        squared shoulders and the gate that backs onto the wrong faction resolve to a
        direction, not a name") is therefore FOLLOWABLE for a context-bearing reader:
        the place-gloss supplies the faction-adjacency frame, the bone sequence supplies the
        physical data (wrong-hour @8/exposition:3 + wrong-ward + delivery-stance @12/@13),
        and the inference resolves to "a direction, not a name" — matching the gloss's
        deliberate non-identification of the household. No genuine context the reader cannot
        recover; the weave carries it. No ledger entry.

    # ── Central-event followability (the chapter's three spines) ──────────
    - id: follow-005
      anchor: "scene-A @4/@6/@7 | scene-B @11-@16 | scene-C @19-@23"
      classification: OK
      rationale: |
        SW-1 substrate-split (s01): @6 files Wren's route to the internal map; @7 the
        ward-coverage notes receive only the boundary geometry. NI:1/NI:2 + mem:1 make the
        person-vs-geometry split legible ("the map takes Wren's pattern the way it takes any
        pattern, clean, indexed, kept"). The @0 bridge pre-frames it ("I have not had to ask
        it to"). Followable.
        SW-2/SW-3 (s02): courier-appears @11 → faces @12 → squares @13 → categorization @14
        → withhold @15/@16. Physical-data-THEN-inference order preserved; NI:5 @19 + the
        scene-C substrate components (@20 deliverable-left / @21 Wren-route / @22 courier-
        entry) carry the double-omission as structural fact. Followable for a context-bearing
        reader.

  # ── DESIGN-INHERENT items NOT litigated as FOLLOW-GAPs (per brief + DEC-0062/CHUNK-CLASS-B) ──
  design_inherent_not_gaps:
    - "internal-map / feed-record substrate-split opacity — chapter thesis-mechanism; SW-1 plot content; moral_legibility hold FORBIDS naming it as a withholding. NOT a FOLLOW-GAP."
    - "apparatus vocabulary (the count / the coverage / the feed / the circuit / the column / the feed-record / the internal map) — coverage-map-instrument-family register-resident (b01c02); ruled design-inherent. NOT a FOLLOW-GAP."
    - "withheld-motive opacity — the override-pattern is visible to the reader, un-named by Taylor BY DESIGN. NOT a FOLLOW-GAP (chunk_cold_read cold_read_risk_carry confirms design-intentional)."
    - "color-metaphor ('resentment arrived with color') — project metaphor-vocabulary c01-c08; reader-resident anchor sufficient; NOT an exposition/context gap here."

# ════════════════════════════════════════════════════════════════════════
# AXIS 2 — READABILITY / ALIVENESS (PROP-0022)
# Verdict: ONE GROUNDING-REQUIRED (@11/@12 courier-appears) + ancillary VOICE-FIXABLE notes.
# ════════════════════════════════════════════════════════════════════════

axis_2_aliveness:
  verdict: GROUNDING-REQUIRED x1 (@11/@12) + VOICE-FIXABLE x1 (@8 scene-B opening register)
  grounding_required_count: 1
  findings:

    # ── PRIORITY: the courier-arrival span @8-@13 (bones-review BONES-AIRLESS-RISK) ──
    - id: alive-001
      anchor: "@11 (with grounding-target @11/@12)"
      classification: GROUNDING-REQUIRED
      symptom: AIRLESS @11 — courier-appears beat rendered instrument-first, no body to inhabit AT the appearance-moment
      rationale: |
        This is the bones-review signal-001 BONES-AIRLESS-RISK, now adjudicated against the
        full R1 facet weave. Bone @11 "the insect-feed returns corwick" is instrument-class
        (feed = subject, corwick = returned object) — the courier-appears beat reads as a
        data-record transaction at the bone level. Examining what the R1 lenses actually put
        at @11/@12:
          - narrator:3 @11 FIRES: "evening feed runs the margin and the figure in it is
            wrong-houred and wrong-warded, a man standing where a man at this hour should not
            be standing." This DOES introduce a person ("a man standing") — but it frames him
            FROM INSIDE THE APPARATUS ("the figure IN IT [the feed]"), an analytic
            wrong-houred/wrong-warded read, not a perceptual arrival.
          - feeling:2 @12 FIRES: "she goes still at the feed-edge as the courier's body turns
            toward the second man" — a somatic tell, the closest thing to embodiment in the span.
          - sensory FIRES @8 (thermal entry) but does NOT fire @11 or @12. There is no
            perceptual-arrival sensory grounding ON the courier-appears beat itself.
        The net: the @8-@13 span is NOT wholly airless (sensory @8 grounds the entry;
        feeling @12 + NI @11 supply some body), but the LOAD-BEARING appearance-moment — the
        instant Corwick resolves out of the feed-distribution into a tracked body — is carried
        by an instrument-frame NI line and a held-still tell, with the bone itself
        instrument-class. The courier-resolves-from-the-feed beat has no SENSORY perceptual
        anchor, and the sensory frequency-band cap BLOCKS a third fire (2/23 = 8.7% already at
        the short-chapter-exemption ceiling; adding @11/@12 raises modality-count and trips
        the standard 6% ceiling per the sensory file's own cull math). This is precisely the
        case the grounding-ledger exists for: the grounding is genuinely ABSENT at the beat
        AND the cap would block adding it. → GROUNDING-REQUIRED. Ledger entry grd-001 licenses
        a sensory perceptual-arrival fire at @11/@12 that escapes the frequency-band cap (the
        designed remedy named in the brief + bones-review forward-carry).
      not_voice_fixable_because: |
        Considered VOICE-FIXABLE (render-choice at /and-stitch Phase 4). REJECTED: a Phase 4
        voice-embodiment pass can re-front the EXISTING NI:3 figure-line and feeling:2 tell
        from person-first instead of apparatus-first, and it SHOULD (see alive-002 VOICE-FIXABLE
        below) — but Phase 4 cannot manufacture a perceptual SENSORY anchor that does not exist
        in any facet at @11/@12, because the sensory cap blocks the studio from authoring one
        without a license. The missing element is a perceptual grounding ADD, not a re-render
        of present content. Hence GROUNDING-REQUIRED (license the add) rather than VOICE-FIXABLE
        (defer the re-render). Both apply: grd-001 licenses the sensory add now; alive-002 carries
        the person-first re-front to stitch.

    # ── Ancillary: scene-B opening register (VOICE-FIXABLE, carries to stitch) ──
    - id: alive-002
      anchor: "@8-@11 (scene-B opening run)"
      classification: VOICE-FIXABLE
      symptom: embodied content present but rendered apparatus-first across the scene-B opening
      rationale: |
        @8 (enters dragonpit-margin) / @9-@10 (supply-cart / stone-post baseline) / @11
        (feed-returns-corwick) run as four consecutive apparatus/environment-frame beats. The
        embodiment IS available — sensory:1 @8 thermal, loc-state:3/:4 physical staging,
        NI:3 @11 "a man standing where a man at this hour should not be standing", feeling:2
        @12 held-still. The content is there; it is fronted instrument-first. /and-stitch
        Phase 4 voice-embodiment discipline should prefer the person-first faithful rendering
        (Taylor crossing into the cooling hill-lane; the man resolving out of the feed as a
        seen body, not "the figure in it") within the bone-faithfulness fence — calibrated
        against active-project/voice-exemplar.md. This is a render-choice, NOT a content gap →
        carries to stitch, NOT a ledger entry. (Paired with grd-001: the licensed sensory add
        gives Phase 4 the perceptual material to front.)

  # ── Spans confirmed ALIVE (no finding) ──
  alive_ok:
    - "scene-A @4-@7: NI:1/NI:2 + feeling:1 @5 (gaze holds on the bread-seller's corner a beat before Wren reaches it) + mem:1 @6 — a person inhabiting the surveillance, the radar-tell embodied. ALIVE."
    - "scene-C @19-@23: NI:5 @19 (the wax comes down under her hand at the weight she has already settled) + sensory:2 @23 tactile (wax-soft-warm → wax-set-firm) + mem:2 — the seal-down close is grounded at the hand and the wax; terminal image breathes. ALIVE."
    - "@12-@13: feeling:2 @12 + feel:2 (corwick faces the second man) + @13 squares-the-shoulders — Corwick's body grounded once the appearance-moment passes; the grounding RESUMES here (the @11 deficit is the appearance-instant specifically)."

# ════════════════════════════════════════════════════════════════════════
summary:
  axis_1_completeness: PASS — 0 CONTEXT-REQUIRED. follow-001 @8 CONFIRMED CLOSED (exposition:3 scene-orient + @0 bridge). No context-ledger entries.
  axis_2_aliveness: 1 GROUNDING-REQUIRED (grd-001 @11/@12 courier-appears perceptual-arrival) + 1 VOICE-FIXABLE (alive-002 scene-B opening register → stitch Phase 4).
  ledger_writes:
    context_ledger: empty (note: no CONTEXT-REQUIRED gaps found)
    grounding_ledger: 1 entry (grd-001)
