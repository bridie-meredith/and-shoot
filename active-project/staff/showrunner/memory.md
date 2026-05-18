# showrunner memory — schema: schemas/showrunner-memory.schema.md

project:
  brief: "taylor hebert, post gold morning, in westeros king's landing before dance of dragons. theme should be 'road to hell is paved with good intentions' where taylor does bad things for a good reason which later turns out to be bad. one book long series"
  constraints:
    settings:
      - "currency: gold dragon / silver stag / copper penny + star"
      - "class: smallfolk / landed / lordly / royal / Faith / Maesters (Westerosi)"
      - "year: 122 AC, late Viserys-I reign, pre-Dance of Dragons"
      - "place: King's Landing — Flea Bottom anchor + Red Keep + Dragonpit + Great Sept + seven gates + three hills"
      - "canonicity: F&B-aligned (HOTD where F&B silent); AU-tolerant for Worm transit"
      - "magic: dormant on KL court layer; rumor-permitted; not narrator-confirmed"
      - "dragons: backgrounded with instrumental pressure; not on-stage scene partners"
    themes_as_bounds:
      - "spine: road to hell is paved with good intentions — instrumental moral causation"
      - "story-type: slow-prevention-tragedy (mirror-of-canon)"
      - "tonal: tragic / ironic-causal; smallfolk gallows humor permitted; no comic relief; no fairytale-stasis"
      - "protagonist register: cold-utilitarian; explicit moral ledger; affect suppressed not absent; theme never spoken on-page"
    hard_fences:
      - "Earth-Bet proper-noun fence: parahuman jargon dialogue-banned, inner-monologue-rare"
      - "POV: Taylor first-person only; non-Taylor chapters must be marked interludes"
      - "no titles authored on book or chapter (slugs only)"
      - "end-place is structural-bad — locus is 'both' (Taylor dead/expelled + [cost-bearer] smallfolk class-slot dies in Dance's opening Flea Bottom violence; specific identity TBD at /and-cast)"
      - "single-book length floor: 18 chapters, 3 scenes/chapter minimum (re-run OQ-9 to compress)"
  staff:
    audience: [cape-fic-reader, dark-fantasy-reader, worm-canon-pedant]
    screen_writer: screen-writer
    dramatist: dramatist
    auditor: auditor
    editor: editor
    orchestrator_critic: v1.3
  series_audit:
    approved_at: ~
    approved_by: ~
    report_path: ~
    stale_since: ~

series:
  chunk:
    path:
      motivation: "Taylor came to Westeros atoning for Khepri — the mass override of human will she performed at Gold Morning — with no plan except to be useful, to heal, to do good without taking control."
      anchor: "[cost-bearer] — smallfolk class-slot (identity TBD at /and-cast); the un-priced relationship Taylor refuses to enter into the ledger; closing-image bearer of what the trades cost."
      escalation: "Otto Hightower identifies Taylor's pattern-reading + insect-residue intelligence capability and offers her a function — not a title, not a rank — calibrated information-delivery to the Greens in exchange for his quiet shielding of [protect-target] (court-tier class-slot, identity TBD at /and-cast). Taylor accepts because the alternative is the protected node falls, the war comes, and Flea Bottom burns. The atonement-prohibition collapses into the rebuilt-Khepri-architecture: she reads bodies, routes information, and moves people without their knowledge — for better reasons, more carefully."
      trade: "To sustain the function and keep [protect-target] alive, Taylor progressively feeds Otto intelligence that consolidates Green-faction control over Maegor's Holdfast, the Small Council, and the dynastic succession. The trades are accurate. The accuracy is the catastrophe."
      irony: "The trades work — [protect-target] is shielded, the apparatus holds, the war is delayed — and Taylor comes to despise the elite she is preserving. She watches Aegon's court through the insect-feed and develops cold, articulated contempt for the royal family and the Westerosi elite whose continuity her work guarantees. The contempt does not free her: she despises the system she is consolidating, and continues, because the only thing more expensive than the trades is letting [cost-bearer] burn. When the Dance ignites anyway and Flea Bottom is among the first wards to burn, the contempt is what remains — a clear ledger entry naming exactly whom she empowered, in exchange for whom, and what it cost. The atonement was the repetition; the recognition was contempt without refusal."
    trajectory:
      # canonical content in active-project/staff/showrunner/series-trajectory.md
      # 7 axes: moral_framework, capability, position, social_tether, relational_anchor_status, moral_legibility_to_self, political_register_toward_elite
      # 14 deltas (d01–d14); Otto-offer at d03; contempt-onset d05, articulation d09, contempt-without-refusal d13; locked burn at d14
      source: active-project/staff/showrunner/series-trajectory.md
    lens_used: "composed (path-4 penitential motivation + path-2 political mechanism + contempt-emergence layer)"
    # NOTE: prose field permanently retired 2026-05-17 — canonical chunk is path + trajectory only
    # SLOT-DEFERRED: [cost-bearer] + [protect-target] resolved at /and-cast
  structure:
    book_count: 1
    book_length:
      chapters_per_book: 18-22
      scenes_per_chapter: 3-5
      bones_per_scene: 5-15
    cyclical: false
    pov: single
    cross_book_continuity:
      recurring_antagonists: []
      ongoing_subplots: []
    world_evolution: evolving
    series_end_shape: tragic
  laws:
    - cond-khepri-residue-122ac
    - cond-earth-bet-noun-fence
    - cond-westerosi-magic-dormant-122ac
    - cond-dragon-proximity-122ac
    - cond-kl-witch-label-formation-122ac
  lore:
    - cond-kl-court-state-122ac
    - cond-kl-geography-122ac
    - cond-kl-social-physics-122ac
  behaviors:
    - cond-taylor-pov-behavior
    - cond-westerosi-witness-vocabulary
    - cond-maester-chronicler-voice
    - cond-cost-bearer-scene-frequency
    - cond-road-to-hell-chain-shape
  substance:
    state_axes:
      # 9 axes × 3 perspectives = 27 entries; anchors duplicated per schema
      - slug: moral-framework
        dimension: "ethical accounting integrity — does the prohibition still refuse?"
        one_means: "ledger consumed itself; prohibition is the most violated line"
        five_means: "functional moral system with visible strain; exceptions rationalized"
        nine_means: "prohibition intact and generative; refusal-of-control is the atonement working"
        perspective: protagonist
        start_rank: 3
        end_rank: 1
        class: emotional
      - slug: moral-framework
        dimension: "ethical accounting integrity"
        one_means: "ledger consumed itself"
        five_means: "functional with strain"
        nine_means: "prohibition generative"
        perspective: antagonist
        start_rank: 7
        end_rank: 8
        class: emotional
      - slug: moral-framework
        dimension: "ethical accounting integrity"
        one_means: "moral order collapsed"
        five_means: "patterned-if-strained order"
        nine_means: "moral order generative"
        perspective: world
        start_rank: 3
        end_rank: 1
        class: emotional

      - slug: capability
        dimension: "insect-network operational scope"
        one_means: "dormant by choice; close-range insect-sense only"
        five_means: "localized deployment; few-block coverage; pattern-reading systematizing"
        nine_means: "insect network threaded through multiple wards reading bodies and routing intelligence at scale — the morally-rhyming repetition, not the architectural one; surveillance + unconsented instrumentalization, not control-override"
        perspective: protagonist
        start_rank: 3
        end_rank: 7
        class: plot
      - slug: capability
        dimension: "intelligence apparatus reach"
        one_means: "no functional intelligence"
        five_means: "court informants; factional couriers; no ground layer"
        nine_means: "full-spectrum coverage from Flea Bottom to Holdfast"
        perspective: antagonist
        start_rank: 5
        end_rank: 8
        class: plot
      - slug: capability
        dimension: "institutional functional capacity"
        one_means: "institutions collapsed"
        five_means: "stratified-but-functional"
        nine_means: "robust cross-layer institutional capacity"
        perspective: world
        start_rank: 4
        end_rank: 3
        class: plot

      - slug: position
        dimension: "court-layer visibility / structural standing"
        one_means: "invisible or dead/expelled — no patron, no name, no coin"
        five_means: "known to one court layer as a functional asset; unranked; identifiable to users"
        nine_means: "formally embedded with title + rank + recognized standing"
        perspective: protagonist
        start_rank: 1
        end_rank: 1
        class: plot
        notes: "axis tracks two phases: visibility-phase (d01–d09; the rise to court-asset legibility) and entrapment-phase (d10–d14; the collapse to no-exit then expulsion). Bone-gate at /and-write Phase 6 should evaluate against whichever phase the chapter's d-range falls into."
        # 0-net intentional: rise-and-fall (peak 5 at d07 Otto's-unofficial-instrument, collapse to 1 at d14)
      - slug: position
        dimension: "factional standing"
        one_means: "absent from any court"
        five_means: "advisory-from-outside"
        nine_means: "Hand-in-fact"
        perspective: antagonist
        start_rank: 6
        end_rank: 8
        class: plot
        notes: "axis tracks two phases: visibility-phase (d01–d09) and entrapment-phase (d10–d14). Bone-gate at /and-write Phase 6 should evaluate against whichever phase the chapter's d-range falls into."
      - slug: position
        dimension: "dynastic position stability"
        one_means: "succession ruptured into open war"
        five_means: "contested-but-functional dynastic order"
        nine_means: "uncontested dynastic order"
        perspective: world
        start_rank: 4
        end_rank: 1
        class: plot
        notes: "axis tracks two phases: visibility-phase (d01–d09) and entrapment-phase (d10–d14). Bone-gate at /and-write Phase 6 should evaluate against whichever phase the chapter's d-range falls into."

      - slug: social-tether
        dimension: "institutional + relational embedding"
        one_means: "all cover severed; cost-bearer dead; structurally isolated"
        five_means: "one community layer + functional patron channel"
        nine_means: "deep cross-layer embedding; robust patron network"
        perspective: protagonist
        start_rank: 2
        end_rank: 1
        class: emotional
      - slug: social-tether
        dimension: "factional apparatus"
        one_means: "no faction"
        five_means: "single-layer faction"
        nine_means: "cross-layer factional dominance"
        perspective: antagonist
        start_rank: 7
        end_rank: 9
        class: plot
      - slug: social-tether
        dimension: "community substrate"
        one_means: "community destroyed"
        five_means: "intact-if-precarious"
        nine_means: "robust cross-layer solidarity"
        perspective: world
        start_rank: 4
        end_rank: 1
        class: emotional

      - slug: relational-anchor-status
        dimension: "the un-priced relationship's position to the ledger"
        one_means: "cost-bearer dead; anchor retroactively revealed as priced out"
        five_means: "named + structurally present + still outside the ledger"
        nine_means: "fully priced + held openly + entered as a protected node"
        perspective: protagonist
        start_rank: 3
        end_rank: 1
        class: emotional
      - slug: relational-anchor-status
        dimension: "instrumentalized relational apparatus"
        one_means: "no relational anchors"
        five_means: "functional instrumentalized anchors"
        nine_means: "robust inner-circle attachment + utility"
        perspective: antagonist
        start_rank: 5
        end_rank: 6
        class: emotional
      - slug: relational-anchor-status
        dimension: "smallfolk un-priced bond density"
        one_means: "anchors severed by violence"
        five_means: "intact subsistence-bonds"
        nine_means: "robust cross-class un-priced bonds"
        perspective: world
        start_rank: 3
        end_rank: 1
        class: emotional

      - slug: moral-legibility-to-self
        dimension: "self-accounting accuracy and reception"
        one_means: "accounting suppressed or its outputs unread"
        five_means: "ledger runs; outputs rationalized; conclusions deferred"
        nine_means: "atoning-and-aware; framework conscious; legibility as active instrument"
        perspective: protagonist
        start_rank: 7
        end_rank: 4
        class: emotional
        # inverted from standard emotional rubric: starts high, ends in recognition-too-late
      - slug: moral-legibility-to-self
        dimension: "political-actor self-knowledge"
        one_means: "self-knowledge absent"
        five_means: "instrumental self-reading"
        nine_means: "fully self-confirming"
        perspective: antagonist
        start_rank: 6
        end_rank: 7
        class: emotional
      - slug: moral-legibility-to-self
        dimension: "collective moral legibility"
        one_means: "no collective accounting possible"
        five_means: "chronicled-not-acted-on"
        nine_means: "collective accounting both legible and active"
        perspective: world
        start_rank: 3
        end_rank: 2
        class: emotional

      - slug: political-register-toward-elite
        dimension: "stance toward the court elite"
        one_means: "absent; no register possible (dead/expelled)"
        five_means: "neutral-instrumentally-observant; system to be read; no investment"
        nine_means: "contempt-without-refusal — articulated, legible, bound to continued service"
        perspective: protagonist
        start_rank: 5
        end_rank: 9
        class: emotional
      - slug: political-register-toward-elite
        dimension: "elite self-regard"
        one_means: "elite self-regard collapsed"
        five_means: "factional-but-coherent self-regard"
        nine_means: "structurally reinforced dynastic prerogative"
        perspective: antagonist
        start_rank: 7
        end_rank: 8
        class: plot
      - slug: political-register-toward-elite
        dimension: "elite-smallfolk social physics"
        one_means: "social physics erased by violence"
        five_means: "patterned exploitation with predictable modes"
        nine_means: "patterned mobility + dignity"
        perspective: world
        start_rank: 4
        end_rank: 2
        class: plot

      - slug: knowledge
        dimension: "court-layer intelligence picture"
        one_means: "immediate-block awareness only"
        five_means: "one faction's structure + Flea Bottom→lower-court pipeline mapped"
        nine_means: "more complete picture than most Small Council members"
        perspective: protagonist
        start_rank: 3
        end_rank: 8
        class: plot
      - slug: knowledge
        dimension: "factional intelligence holdings"
        one_means: "no faction-internal knowledge"
        five_means: "experienced court-layer reach"
        nine_means: "complete KL intelligence picture"
        perspective: antagonist
        start_rank: 7
        end_rank: 9
        class: plot
      - slug: knowledge
        dimension: "smallfolk systematic awareness"
        one_means: "no warning possible"
        five_means: "rumor-rich-but-unsystematic"
        nine_means: "smallfolk see the politics that consume them"
        perspective: world
        start_rank: 2
        end_rank: 2
        class: plot

      - slug: agency
        dimension: "self-direction over own outcomes"
        one_means: "zero agency; locked into position-of-no-exit or dead/expelled"
        five_means: "self-directed within one domain; cannot extract without cost"
        nine_means: "full autonomous direction; could leave or dissolve the network"
        perspective: protagonist
        start_rank: 5
        end_rank: 1
        class: plot
      - slug: agency
        dimension: "factional control over outcomes"
        one_means: "no directional agency"
        five_means: "constrained-but-directing"
        nine_means: "structural maximum over dynastic outcomes"
        perspective: antagonist
        start_rank: 7
        end_rank: 9
        class: plot
      - slug: agency
        dimension: "smallfolk agency over survival"
        one_means: "agency collapsed to survive-or-die"
        five_means: "subsistence + social-navigation choice"
        nine_means: "meaningful collective agency over conditions"
        perspective: world
        start_rank: 3
        end_rank: 1
        class: plot

    cost_ledger:
      - id: cl-otto-trade
        gain: agency -1
        cost: moral-framework -1
        description: "each intelligence delivery sustains [protect-target]'s shielding but pays moral-framework down; d03 first-sanctioned-exception → d07 systematic-override-rationalized → d12 irrevocable-Khepri-repetition"
        anchor: { book: b01, chapter: ~, scene: ~ }
      - id: cl-intelligence-arrangement
        gain: knowledge +1
        cost: agency -1
        description: "each intelligence delivery deepens Taylor's court-layer picture but extends the arrangement that makes her non-extractable; the more she learns, the less she can leave"
        anchor: { book: b01, chapter: ~, scene: ~ }
        # NOTE: contempt (political-register-toward-elite) is a consequence-axis driven by trajectory d05/d09/d13,
        # not a ledger trade. It arrives via observation, not a paid exchange.
        # notes: "consequence-axis; arrives via observation, not a paid trade"
      - id: cl-network-position
        gain: capability +1
        cost: agency -1
        description: "each network expansion makes Taylor more load-bearing to Otto and less extractable; the network that makes her effective is the cage"
        anchor: { book: b01, chapter: ~, scene: ~ }
      - id: cl-unpriced-cost-bearer
        gain: relational-anchor-status -1
        cost: moral-legibility-to-self -1
        description: "STRUCTURAL ERROR ENTRY — no realized gain; the 'gain' is the relationship sliding because she refuses to ledger it; refusal-to-price corrodes self-accounting; load-bearing at d08, fatal at d14. Note: combined with cl-protection-buys-consolidation (also -1 on this axis), the two entries sum to -2 net, matching the declared target_delta_magnitude of 2 (3→1). The compounding mechanism: cl-unpriced-cost-bearer operates via Taylor's sustained refusal to price [cost-bearer]; cl-protection-buys-consolidation operates via each protect-target extension deferring cost-bearer's entry another notch — the same refusal compounded by each trade."
        anchor: { book: b01, chapter: ~, scene: ~ }
      - id: cl-social-tether-build
        gain: social-tether +1
        cost: position +1
        description: "Flea Bottom embeddedness trades anonymity for utility; same tether that protects in smallfolk layer makes her visible and non-extractable to Otto"
        cost_note: "note: position rising is a cost in this trajectory — higher position = more legible to Otto = less extractable."
        anchor: { book: b01, chapter: ~, scene: ~ }
      - id: cl-protection-buys-consolidation
        gain: relational-anchor-status -1
        cost: political-register-toward-elite +1
        description: "each protect-target extension defers cost-bearer's entry into the ledger another notch; each gain on the protect-target relationship is paid in cost-bearer non-pricing — the relational-anchor-status slides further from the ledger with every trade that keeps [protect-target] alive"
        cost_note: "note: political-register-toward-elite +1 is structurally a cost — axis nine_means = contempt-without-refusal; cost recorded as +1 because the axis moves toward its damaging end."
        anchor: { book: b01, chapter: ~, scene: ~ }

    antagonist_pressure:
      - axis: moral-framework
        pressure_source: "Otto Hightower — calibrated asks; never threatens, proposes; the pressure is being right about the arithmetic"
        cost_curve: "each ask priced just below Taylor's refusal threshold; cumulative pressure compounds because each accepted trade lowers the next refusal-threshold"
      - axis: agency
        pressure_source: "Green-faction apparatus (Alicent household + Small Council + factional couriers)"
        cost_curve: "expanding-dependency; each delivery makes the apparatus more structurally dependent on the Flea Bottom coverage layer; partial deliveries prime larger asks"
      - axis: knowledge
        pressure_source: "dynastic succession clock (Viserys I's decline + Black/Green convergence)"
        cost_curve: "background-obligation; the clock is not a character but its pressure is permanent; each Viserys-survives chapter is one Dance-delayed chapter; knowing the structural logic makes each trade feel obligatory"
      - axis: capability
        pressure_source: "[protect-target]'s structural vulnerability (court-tier slot, identity TBD at /and-cast)"
        cost_curve: "unbounded-protection-demand; each factional maneuver closing off a survival path ratchets the protection ask upward; capability expansion is the only response shape"

    chunk_targets:
      series:  { delta_per_signature_axis: 1-8,   density_target: 0.6-0.9 }
      book:    { delta_per_signature_axis: 1-8,   density_target: 0.5-0.9, bone_count: ~ }
      chapter: { delta_per_signature_axis: 0.5-1.5, density_target: 0.5-0.9, bone_count: ~ }
      scene:   { delta_per_signature_axis: 0-1.5, density_target: 0.6-0.9, bone_count: 5-15 }
      bone:    { delta_per_axis: 1-3, axes_per_bone: 1-2 }
    # tuning notes:
    # - series delta_min lowered 4→1 to accommodate small-magnitude loss moves as signature axes in this loss-arc tragedy
    #   rationale: social-tether (magnitude 1) and moral-framework (magnitude 2) are primary dramatic axes, not support axes;
    #   reclassifying as support would cost semantic clarity; floor of 1 explicitly permits small-magnitude loss moves
    #   on signature axes where the tragedy requires a narrow loss arc rather than a large-delta gain arc
    # - series and book bands identical because book_count=1 (b01 IS the series arc, not an opening book)
    # - position 0-net (1→1) is intentional rise-and-fall; reviewers should NOT flag SUBSTANCE-FLAT on position
    # - moral-legibility starts at 7 ends at 4 (inverts standard emotional baseline framing); deliberate

  vibe_cloud:
    keys:
      - "cold-utilitarian interiority — the ledger runs even when the reader wishes it would not"
      - "penitential-grey King's Landing — stone, tallow, rain-smell; beauty available only to people not paying attention"
      - "tragic-causal — every good act auditable backward to the harm it enabled"
      - "contempt-without-refusal — the protagonist sees clearly, names accurately, and continues; clarity as its own trap"
      - "smallfolk-gallows register permitted; no comic relief"
      - "no spectacle of magic — only its residue and others' fear of it"
      - "the atonement that is the repetition"
      - "earned collapse, not surprise"
  cast_roster:
    - slug: taylor-hebert-kl-122ac
      role: Post-Gold-Morning Taylor, Khepri-residue insect-network, cold-utilitarian POV, sole first-person narrator
      perspective: protagonist
    - slug: otto-hightower
      role: Hand of the King (off formal record), intelligence architect, primary antagonist, calibrated-ask pressure source
      perspective: antagonist
    - slug: aemond-targaryen-122ac
      role: Green-faction coercive arm, Vhagar rider at age 12 (born 110 AC; claimed Vhagar at age 10 at Driftmark in 120 AC), walk-on at structural crisis points; each appearance must shift a named plot axis
      perspective: antagonist
    - slug: wren-stitch-maker-flea-bottom-ward
      role: Cost-bearer; seamstress-family ward age 11; the un-priced relationship; observer-training habit; d14 closing-image death
      perspective: supporting
    - slug: sera-hightower-kl-122ac
      role: Protect-target; Hightower cadet-branch ward age 14; court-tier; structural legitimacy-question; does not know Taylor exists
      perspective: supporting
    - slug: gylda-saltwater-flea-bottom
      role: Witness-mirror; water-carrier age ~40s; names too-many-places pattern once at d09-d10; non-confidant hard fence
      perspective: supporting
    - slug: coll-net-mender-flea-bottom
      role: Flea Bottom fixture; net-mender age ~50s; stationary block-visibility; non-interpretive community-substrate carrier; never names
      perspective: world
    - slug: corvan-archmaester-retrospective-coda
      role: Maester-chronicler; Archmaester writing c.160 AC; coda-only archival voice; counterfactual naming; does not know Taylor's name
      perspective: world
  stage_elements: []

books:
  - slug: b01
    chunk: |
      Taylor Hebert arrives in King's Landing with a single operating rule: be useful without taking control, present without possessing, and let the atonement for Khepri be the refusal to do what she did before. The rule does not survive contact with Otto Hightower, who offers her a function instead of a rank — route the intelligence his faction cannot reach, and [protect-target] lives, the war is delayed, and [cost-bearer] does not burn in it. She refuses first; she names the prohibition that is supposed to hold; the prohibition holds long enough to make the second answer audible as a choice. She accepts on the second answer, because the calculation is clear and the arithmetic is correct, and the first trade is the auditable mistake that makes the rest of them necessary. What follows is not a corruption but a construction: she builds something that rhymes with Khepri in the only register left to her — observation without consent, movement without knowledge, decision-making at a remove from the people whose lives she is routing. She becomes embedded in Flea Bottom because the network requires it, and the embedding becomes the same thing that makes her visible to Otto's apparatus — community-as-tether and community-as-trap braid the same rope. The function Otto gave her has no title and no rank, but it has visibility — she is known to one court layer as a functional asset, identifiable to the actors who use her. Reading the court through compound eyes and delivering intelligence accurate enough that it consolidates Green-faction control of the succession apparatus, she comes to despise the elite she is preserving with the cold clarity of someone who has observed them at close range and found nothing to contradict the contempt. She continues anyway, because the only thing more expensive than the trades is letting [cost-bearer] burn, and the contempt does not constitute refusal — it constitutes legibility. When the Dance ignites and the Flea Bottom violence that opens the war moves through the streets her network mapped and Otto's architecture knew, she cannot reroute it; [cost-bearer] dies in the street she had charted; she is removed from the story's scope by the forces her position made her legible to; and the ledger — still running, delivering its final output clearly — names exactly whom she empowered, in exchange for whom, and what it cost. The atonement was the repetition. The recognition came too late to constitute refusal.
    structure:
      chapter_count: ~          # set by /and-substance book b01 Phase 2; range 18-22 per series.structure
    substance_delta:
      axes_in_motion:
        - { axis: moral-framework,              direction: down, target_delta_magnitude: 2, cost_ledger_anchor: cl-otto-trade,                  notes: "3→1 protagonist; d03 first-exception → d07 systematic → d12 irrevocable" }
        - { axis: capability,                   direction: up,   target_delta_magnitude: 4, cost_ledger_anchor: cl-network-position,            notes: "3→7; d01 localized → d04 Khepri-rhyming-surveillance-architecture → d12 fully-deployed; architecture is surveillance+unconsented-instrumentalization, not control-override" }
        - { axis: position,                     direction: ~,    target_delta_magnitude: 0, cost_ledger_anchor: cl-social-tether-build,         notes: "1→1 net; INTENTIONAL rise-and-fall (peak 5 d07, collapse d14); direction null because net is zero — intra-book shape is visibility-phase then entrapment-phase, not a net upward arc" }
        - { axis: social-tether,                direction: down, target_delta_magnitude: 1, cost_ledger_anchor: cl-social-tether-build,         notes: "2→1; d01 embedded → d04 load-bearing → d10 exposed → d14 severed" }
        - { axis: relational-anchor-status,     direction: down, target_delta_magnitude: 2, cost_ledger_anchor: [cl-unpriced-cost-bearer, cl-protection-buys-consolidation], notes: "3→1; d02 named-outside-ledger → d08 load-bearing → d14 unprotected-at-burn; two ledger entries each contribute -1 summing to -2 net; see cl-unpriced-cost-bearer description for compounding mechanism" }
        - { axis: moral-legibility-to-self,     direction: down, target_delta_magnitude: 3, cost_ledger_anchor: cl-unpriced-cost-bearer,        notes: "7→4; d02 first-crack → d06 rationalizing → d10/d11 suppression → d14 recognition-too-late. cl-unpriced-cost-bearer contributes -1 directly; additional -2 net is consequence-driven by Wren-related observations at d06 (rationalizing trades), d10/d11 (suppression of seeing what the architecture has become) — these are not paid trades but recognition-events triggered by accumulating ledger costs elsewhere. Bone-gate at /and-write Phase 6 should accept consequence-anchored bones on this axis when no direct ledger trade is appropriate." }
        - { axis: political-register-toward-elite, direction: up, target_delta_magnitude: 4, cost_ledger_anchor: ~,                               notes: "5→9; d05 resentment → d09 articulated → d13 contempt-without-refusal; consequence-axis driven by trajectory d05/d09/d13 observation sequence, not a direct ledger trade; note: rising IS the cost — nine_means = contempt-without-refusal; +1 direction recorded because axis moves toward its damaging end" }
        - { axis: knowledge,                    direction: up,   target_delta_magnitude: 5, cost_ledger_anchor: cl-intelligence-arrangement,    notes: "3→8; d04 coverage → d07 systematic → d09 full court picture" }
        - { axis: agency,                       direction: down, target_delta_magnitude: 4, cost_ledger_anchor: cl-network-position,            notes: "5→1; d10 no-exit confirmed; d14 dead-or-expelled; steepest single loss-arc" }
      density_target: 0.5-0.9
    stale_since: ~
    vibe_cloud:
      keys: []                  # book-level vibe-cloud authored by /and-substance book b01
    drama: ~                    # authored by /and-substance book b01 Phase 4
    chapters: []

active:
  book: ~
  chapter: ~
  cascade_in_progress: false

routing:
  series_plan: active-project/staff/showrunner/series-plan.md
  staleness_log: active-project/staff/showrunner/staleness-log.md
  cascade_checkpoint: active-project/staff/showrunner/cascade-checkpoint.md
  reviews: active-project/staff/reviews/
  bones_dir: active-project/theater/bones/
  facets_dir: active-project/theater/facets/
  dialogue_dir: active-project/theater/dialogue/
  draft_dir: active-project/draft/
