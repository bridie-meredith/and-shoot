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
    - cond-override-architecture-residue-122ac
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

  # /and-substance series Phase 4 — signature authored 2026-05-24; pulp-enthusiast Phase 4b ACCEPT verdict.
  # Phase 5 attempt 1 → REVISE (audience SUBSTANCE-FLAT-antagonist_pressure; dramatist roll-up + curve-shape;
  # auditor fault-001/002/003/004). Phase 5 attempt 2 → revised signature persisted below (v2).
  substance:
    state_axes:

      - slug: moral_framework
        dimension: "integrity of the anti-instrumentalization prohibition as operating compass"
        one_means: "prohibition intact and operationally enforced — Taylor refuses every act of directing others"
        five_means: "prohibition named and believed but licensed exceptions accumulating — first sanctioned breach acknowledged"
        nine_means: "framework consumed as compass: ledger still runs, all entries rationalized, prohibition the most violated line"
        perspective: protagonist
        start_rank: 2
        end_rank: 8
        class: emotional
        notes: "monotonic collapse; start 2 (prohibition explicit and initially held — Khepri-haunted refusal-of-control); d03 first crack, d12 irrevocable; end 8 LOCKED — framework eaten as compass"

      - slug: capability
        dimension: "scope and systematization of insect-network intelligence deployment"
        one_means: "fully suppressed by choice — insects kept at subsistence range, no systematic reading"
        five_means: "localized deployment — Flea Bottom coverage, reading bodies in known wards, not yet feeding a patron"
        nine_means: "Khepri-rhyming surveillance architecture: full ward coverage, unconsented instrumentalization at scale, network structural to Greens"
        perspective: protagonist
        start_rank: 2
        end_rank: 8
        class: plot
        notes: "monotonic rise; start 2 (residue range intact while suppressed); end 8 LOCKED — network outlasts Taylor as transferred structure (d12 fully-deployed-and-load-bearing, d14 network outlasts architect)"

      - slug: position-prot-rise
        dimension: "legibility and standing within the KL court power structure — rise phase"
        one_means: "smallfolk-anonymous — no rank, no coin above subsistence, invisible to every court layer"
        five_means: "known-quantity-to-one-court-layer — Otto aware of Taylor; function defined; no formal standing"
        nine_means: "Otto's-unofficial-instrument-at-full-load — position-of-no-exit; too legible to be released"
        perspective: protagonist
        start_rank: 1
        end_rank: 7
        class: plot
        notes: "rise phase only; peaks ~7 at d07 (Otto's-unofficial-instrument formalized), confirmed non-extractable at d10; collapse handed off to position-prot-collapse axis"

      - slug: position-prot-collapse
        dimension: "legibility and standing within the KL court power structure — collapse phase"
        one_means: "smallfolk-anonymous — no rank, no coin above subsistence, invisible to every court layer"
        five_means: "position held but under structural threat — Taylor's exposure is a recognized risk to Otto"
        nine_means: "position at full non-exit load before removal — too load-bearing to release, too informal to protect"
        perspective: protagonist
        start_rank: 7
        end_rank: 1
        class: plot
        notes: "collapse phase only; starts from d10 peak state (~7); collapses to 1 at d14 (dead/expelled); LOCKED end-state; per-chapter contracts allocate as a separate Δ track from the rise"

      - slug: relational_anchor_status
        dimension: "operational weight loading onto the un-priced relational anchor ([cost-bearer])"
        one_means: "anchor present; no operational weight — Taylor is attached, [cost-bearer] not yet in any calculus"
        five_means: "anchor inside the protection architecture without [cost-bearer]'s knowledge or consent; Taylor routing around use-vectors"
        nine_means: "[cost-bearer]'s exclusion from the ledger is structurally causal to their death — the un-priced item is the one Taylor could not defend"
        perspective: protagonist
        start_rank: 1
        end_rank: 9
        class: emotional
        notes: "monotonic rise in pressure — the relationship itself does not change, the weight of not-pricing it does; [cost-bearer] never enters the ledger; d14 is the revelation; LOCKED; HIGH = WORST (rank 9 = unprotected-at-burn; damaging end is high)"

      - slug: moral_legibility_to_self
        dimension: "accuracy and completeness of Taylor's self-accounting against what she is actually doing"
        one_means: "no accounting at all — operating blind or in full denial; impossible for Taylor; floor is 3"
        five_means: "rationalizing-each-trade — accounting runs but each entry is filed as acceptable; recognition exists, is suppressed"
        nine_means: "recognition-too-late: full clarity on the repetition, delivered by the ledger, in time only to be unable to deny it"
        perspective: protagonist
        start_rank: 4
        end_rank: 8
        class: emotional
        notes: "non-linear net-positive; start 4 (atoning-and-aware, believes she's succeeding); cracks d02/d06/d10; recognition suppressed at d10; full recognition at d14; end 8 LOCKED — recognition at full force but too-late; 9 is narratively unavailable (too-late diminishes usability; recognition-without-refusal requires the ledger to complete, not to overwhelm)"

      - slug: political_register-prot
        dimension: "Taylor's stance toward the Westerosi ruling class as revealed by what the insect-feed returns"
        one_means: "neutral-instrumentally-observant — reads the court as a system; no investment, no contempt, no affect"
        five_means: "readable-resentment — color has accumulated; not yet named; the insects bring it back and Taylor notices"
        nine_means: "contempt-without-refusal — fully articulate, cold, named by name, bound to continued service; clarity as its own trap"
        perspective: protagonist
        start_rank: 1
        end_rank: 9
        class: emotional
        notes: "monotonic rise; d05 resentment readable (+3 from 1 to ~4), d09 articulated-contempt, d13 contempt-without-refusal; LOCKED end 9 — thematic spine; the contempt is the ledger in its final form"

      - slug: social_tether-prot-rise
        dimension: "depth and load-bearing weight of Taylor's relational and institutional ties in KL — rise phase"
        one_means: "nil — arrived in an alley with nothing; no name anyone will remember; no institutional cover"
        five_means: "smallfolk-embedded and patron-adjacent — Flea Bottom contacts; Otto aware but arrangement not yet structural"
        nine_means: "load-bearing-in-Otto's-architecture — network structural to Greens; Taylor cannot exit without triggering collapse"
        perspective: protagonist
        start_rank: 1
        end_rank: 8
        class: plot
        notes: "rise phase only; peaks ~8 at d07 (load-bearing formalized); confirmed non-extractable at d10; collapse handed off to social_tether-prot-collapse axis"

      - slug: social_tether-prot-collapse
        dimension: "depth and load-bearing weight of Taylor's relational and institutional ties in KL — collapse phase"
        one_means: "severed — tether gone; patron dissolved; network transferred"
        five_means: "tether under structural strain — exposure risk recognized, exit calculus failing"
        nine_means: "tether at full non-exit load before severance — every contact inside Otto's architecture"
        perspective: protagonist
        start_rank: 8
        end_rank: 1
        class: plot
        notes: "collapse phase only; starts from d10 peak state (~8); collapses to 1 at d14 (tether severed, patron dissolved, network transferred); LOCKED end-state; per-chapter contracts allocate as separate Δ track"

      - slug: social_tether-antag
        dimension: "Otto Hightower's leverage over Taylor through the network she builds"
        one_means: "Otto has no knowledge of Taylor; no leverage exists"
        five_means: "Otto has identified the capability and made the offer; leverage embryonic — Taylor could still walk"
        nine_means: "Taylor is too load-bearing to withdraw; Otto's leverage is structural; exit would trigger counter-action"
        perspective: antagonist
        start_rank: 1
        end_rank: 9
        class: plot
        notes: "monotonic rise tracking Taylor's embeddedness; Otto gains leverage at d03, leverages it fully by d10 (non-extractable confirmed)"

      - slug: position-world
        dimension: "Green-faction consolidation of KL institutional control"
        one_means: "contested succession, no faction controls court apparatus; council fluid"
        five_means: "Green faction dominant in council but succession unresolved; Viserys alive, Rhaenyra a live claimant"
        nine_means: "Green-faction control of Maegor Holdfast, Small Council, and succession angle — apparatus locked"
        perspective: world
        start_rank: 5
        end_rank: 9
        class: plot
        notes: "monotonic rise; Taylor's intelligence deliveries are the consolidation mechanism; world gains exactly as protagonist pays moral_framework"

      - slug: political_register-world
        dimension: "Green-faction succession position — the continuity Taylor's trades guarantee"
        one_means: "succession unresolved; Greens without institutional advantage; rival claims live"
        five_means: "Green faction dominant in informal channels; Otto operating effectively outside council"
        nine_means: "Green-faction position secured — Maegor Holdfast, Small Council, dynastic angle locked; continuity guaranteed until Dance ignites"
        perspective: world
        start_rank: 5
        end_rank: 9
        class: plot
        notes: "monotonic rise; mirrors political_register-prot rise — Taylor despises what she is consolidating; world benefits in exact proportion to her contempt growing"

    # actor_baselines: AUTHORED AT STEP 4d (post-cast); HARD-ABORT on first /and-substance book Phase 0 if empty.
    actor_baselines: []

    cost_ledger:
      - id: cl01a
        gain: "capability +1"
        cost: "opportunity-missed: rescue witnessed by Flea Bottom witnesses; witch-label formation begins (cond-kl-witch-label-formation-122ac); [cost-bearer] block enters exposure radius"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl01b
        gain: "social_tether-prot-rise +2"
        cost: "journey-required: cl01a (same rescue event; tether embedding is the other face of witch-label exposure)"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl02
        gain: "position-prot-rise +4"
        cost: "moral_framework -3"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl03a
        gain: "capability +3"
        cost: "moral_framework -2"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl03b
        gain: "social_tether-prot-rise +4"
        cost: "journey-required: cl03a (same network-build event; tether gain is future-cost collateral — this +4 becomes the -7 at cl07a; DOWNSTREAM NOTE: chapter contract for d04 must encode tether gain as future-cost collateral to suppress SUBSTANCE-SUSPECT-cheap-gain-social_tether-prot-rise at /and-substance book Phase 0)"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-world-d04
        gain: "position-world +2"
        cost: "journey-required: cl03a (Taylor's network delivers the Flea Bottom intelligence layer Otto cannot obtain otherwise; world consolidation is the direct output of capability gain)"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-d05
        gain: "political_register-prot +3"
        cost: "opportunity-missed: resentment becomes the permanent register of court observation; the insect-feed now returns color Taylor cannot un-notice; neutral-instrumentally-observant is foreclosed from d05 forward"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-d06
        gain: "relational_anchor_status +2"
        cost: "moral_framework -1"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-d07a
        gain: "position-prot-rise +2"
        cost: "opportunity-missed: Otto names the arrangement explicitly; Taylor can no longer read the function as informal; exit calculus is now fully visible to both parties"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-world-d07
        gain: "political_register-world +2"
        cost: "journey-required: cl02 (Otto formalizes the arrangement; Green succession channel solidifies through the intelligence architecture Taylor accepted)"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-antag-d03
        gain: "social_tether-antag +4"
        cost: "journey-required: cl02 (offer accepted; Otto gains leverage proportional to Taylor's position-rise)"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-d08
        gain: "relational_anchor_status +2"
        cost: "journey-required: cl03b ([cost-bearer] moves freely in wards Taylor cannot cover without triggering witch-label; [cost-bearer] is structurally necessary to the coverage map without appearing in the ledger)"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-d08b
        gain: "social_tether-prot-rise +1"
        cost: "journey-required: cl-d08 ([cost-bearer]'s free movement in uncovered wards consolidates the tether; the coverage gap that makes [cost-bearer] useful is the same gap Taylor refuses to route around)"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl04
        gain: "relational_anchor_status +3"
        cost: "opportunity-missed: extraction path before network became non-withdrawable; Taylor runs the accounting, confirms [protect-target]'s benefit outweighs the courier's harm, and closes the ledger on a person without their knowledge"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-antag-d10
        gain: "social_tether-antag +4"
        cost: "journey-required: cl04 (non-extractable confirmed; Otto's leverage is structural from here)"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl05
        gain: "capability +2"
        cost: "moral_framework -1"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl-d11
        gain: "relational_anchor_status +1"
        cost: "opportunity-missed: Taylor intercepts the use-vector targeting [cost-bearer] and adjusts the network to screen it; she calls this protection; she is running the same override architecture she built to atone for"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl06
        gain: "political_register-prot +5"
        cost: "opportunity-missed: contempt arrives with no exit attached; clarity forecloses nothing; the contempt does not change what she does next"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl07a
        gain: "moral_legibility_to_self +4"
        cost: "social_tether-prot-collapse -7"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl07b
        gain: "position-world +2"
        cost: "position-prot-collapse -6"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl07c
        gain: "political_register-world +2"
        cost: "opportunity-missed: relational_anchor_status reaches rank 9 — unprotected-at-burn [HIGH = WORST on this axis; rank 9 = [cost-bearer] dies before Taylor can spend the protection she built everything to provide; the un-priced item is the one the calculus came for]"
        anchor: { book: b01, chapter: null, scene: null }

    antagonist_pressure:
      - axis: moral_framework
        pressure_source: "Otto Hightower — each ask prices a specific protection, making refusal a calculation rather than a prohibition"
        cost_curve: "escalates monotonically; d03 opens the account, d07 formalizes it, d12 makes it irrevocable; Otto never presses — the calculation does"
      - axis: social_tether-prot-rise
        pressure_source: "Otto Hightower — the network Taylor builds to survive is simultaneously the architecture that makes her non-extractable; tether rise is the trap loading"
        cost_curve: "escalates through d04-d07; d10 confirms non-extractable; the rise feeds directly into the collapse at d14"
      - axis: social_tether-prot-collapse
        pressure_source: "Otto Hightower — the network Taylor cannot dismantle without triggering counter-action; at d14 the patron channel dissolves with her removal"
        cost_curve: "dormant until d10 (non-extractable confirmed); collapses at d14 when Taylor's removal makes the position irrelevant"
      - axis: position-prot-rise
        pressure_source: "Otto Hightower — formal legibility as his unofficial instrument; too load-bearing to release, too informal to protect"
        cost_curve: "escalates d03 to d10 peak (position-of-no-exit); feeds position-prot-collapse at d14"
      - axis: position-prot-collapse
        pressure_source: "Otto Hightower — the removal that makes Taylor's informal position irrelevant; no formal standing means no formal protection when the Dance ignites"
        cost_curve: "single-event collapse at d14; position collapses in the same moment [cost-bearer] burns"
      - axis: relational_anchor_status
        pressure_source: "cond-kl-witch-label-formation-122ac — the witch-label social physics that makes Taylor's insect-use publicly visible and routes community suspicion toward her contacts"
        cost_curve: "escalates monotonically from d01 (witnesses at rescue) through d04 (network threads through wards); caps when Taylor routes around vectors that might expose [cost-bearer] to Otto"
      - axis: relational_anchor_status
        pressure_source: "Dance-ignition timeline — punctuated on-page eruptions: d10 (opposing-faction courier detained because Taylor's route-map reached Otto's apparatus — the war's logic moving through Taylor's network without her consent or control); d12 (war-pressure on [protect-target]'s succession exposure forces full-coverage push, network deployed at scale to cover more bodies through more wards than at any prior point); final hammer-fall at d14 (Dance ignites; Flea Bottom burns; streets Taylor mapped are the streets the violence moves through)"
        cost_curve: "punctuated; not escalating in Taylor's perception between eruptions but producing on-page tactical complications at d10 and d12 that Taylor cannot neutralize with accounting alone; catastrophic and irrevocable at d14"
      - axis: political_register-prot
        pressure_source: "faction-violence as sub-pressure — the Dance's pre-ignition maneuvers produce on-page courier detentions, surveillance counter-moves, and smallfolk caught in factional logistics at d07, d10, d12; Taylor reads these through the insect-feed; each incident advances the contempt from diffuse resentment toward articulate naming"
        cost_curve: "feeds political_register-prot monotonically between d05 (first resentment color) and d13 (contempt-without-refusal); the pressure is the feed-content, not a separate force — faction violence and court observation are the same stream through the insect network"
      - axis: moral_legibility_to_self
        pressure_source: "Gold Morning memory — internal antagonist; the standard against which Taylor measures every override; the specific shape she is repeating"
        cost_curve: "oscillates; suppressed at each rationalization beat (d06, d10, d11); surfaces sharply at d09 (articulated contempt) and terminally at d14 (recognition-too-late)"

    chunk_targets:
      series:  { delta_per_signature_axis: 4-8, density_target: 0.6-0.9 }
      book:
        delta_per_signature_axis: 4-8
        density_target: 0.7-0.9
        bone_count: 270-700
        # RISE-THEN-COLLAPSE NOTE: position-prot-rise/collapse and social_tether-prot-rise/collapse are tracked
        # as GROSS motion at chapter level. Rise arc and collapse arc are each a separate chapter-level Δ
        # allocation. Net-zero series-aggregate does NOT reduce chapter-level Δ allocation on these axes.
        # /and-substance book Phase 3 treats -rise and -collapse as independent in-motion axes:
        # rise-phase chapters allocate Δ on the -rise axis; collapse-phase chapters allocate Δ on the -collapse axis.
      chapter: { delta_per_signature_axis: 0.5-1.5, density_target: 0.5-0.9, bone_count: 15-75 }
      scene:   { delta_per_signature_axis: 0-1.5,   density_target: 0.6-0.9, bone_count: 5-15 }
      bone:    { delta_per_axis: 1-3, axes_per_bone: 1-2 }

    # Phase 4b verdict (pulp-enthusiast taste-judge): ACCEPT (v1 substance; carried to v2).
    # Phase 5 attempt 1 aggregate: REVISE (audience SUBSTANCE-FLAT-antagonist_pressure;
    #   dramatist ROLL-UP + CURVE-SHAPE FAIL; auditor fault-001/002/003/004).
    # Phase 5 attempt 2 aggregate: ACCEPT (audience 3-of-3 SUBSTANCE-FELT; dramatist ACCEPT
    #   all 5 checks PASS; auditor ACCEPT zero hard / 4 soft non-blocking).
    #
    # Downstream watch-items (carried forward into /and-cast and /and-substance book):
    #   - Dance-ignition timeline (d10-d14): chapter contracts must keep visible on-page
    #     complications; v2 antagonist_pressure entries name d10/d12 eruption points explicitly.
    #   - Position/social_tether rise/collapse: d14 collapse must read as complication cascade;
    #     v2 splits into independent -rise / -collapse axes with non-zero deltas at chapter level.
    #   - relational_anchor_status: beats attached to plot events; v2 distributes accumulation
    #     across cl-d06 / cl-d08 / cl-d11 / cl04 (trajectory-anchored).
    #   - cl-d08b social_tether-prot-rise +1 at d08 inferentially-anchored (auditor flag-001);
    #     /and-substance book Phase 3 may challenge if working from shifts blocks only.
    #   - Slug naming convention mixed (auditor flag-002); latent confusion risk only.
    #   - cl07c opportunity-missed annotation multi-sentence (auditor flag-003); not blocking.
    # Reviewer reports: active-project/staff/showrunner/_drafts/{phase-4b-pulp-verdict,
    #   phase-5-{audience-attempt1,auditor-report,dramatist-review,
    #             audience-attempt2,auditor-report-attempt-2,dramatist-review-attempt-2}}.md

# /and-substance series Phase 2 + Phase 3 — book chunk + structure + substance_delta + vibe_cloud
# Authored 2026-05-24; roll-up verified 12 of 12 axes within ±1 tolerance (10 EXACT, 2 within-±1).
# Draft preserved: active-project/staff/showrunner/_drafts/book-b01-draft-2026-05-24.md
books:
  - slug: b01
    chunk: |
      Taylor arrives in King's Landing as a penitent who has stripped herself
      of every instrument of control — and discovers, inside the first season,
      that the only path that keeps [cost-bearer] out of the coming war runs
      directly through Otto Hightower's offer. She accepts, and in accepting
      begins rebuilding the architecture she came to Westeros to atone for:
      insect-surveillance threading the wards, unconsented observation of
      bodies that do not know they are being read, calibrated intelligence
      routed to a faction she will come to name and despise. The book traces
      the full arc of that construction — from the first sanctioned exception
      at d03, through the formalizing of position at d07, through the
      non-extractable confirmation at d10, through the irrevocable Khepri-
      repetition at d12, to the Dance's ignition and the locked burn at d14.
      What cannot survive this book: Taylor as agent of refusal-of-control
      (the prohibition is the most violated line); the un-priced relational
      anchor ([cost-bearer] dies in the streets Taylor mapped); and
      atonement-as-distinct-from-repetition (the ledger's final entry is the
      recognition that the atonement was the repetition). The contempt arrives
      accurate and complete and without exit. The trades worked. The accuracy
      was the catastrophe.
    structure:
      chapter_count: 20
      # Rationale: midpoint of 18-22 hard-fenced range. Distribution: chapters 1-9 absorb
      # setup zone (d01-d06; front-loaded embeddedness before lock), chapters 10-16 absorb
      # lock zone (d07-d10; non-extractable confirmation needs escalation room), chapters
      # 17-20 absorb cascade (d11-d14; one delta per chapter — compressed to read as
      # acceleration per pulp-enthusiast watch-item).
    substance_delta:
      axes_in_motion:
        - axis: moral_framework
          direction: down
          target_delta_magnitude: 6
          cost_ledger_anchor: [cl02, cl03a, cl-d06, cl05]
          notes: "d03 first-sanctioned-exception → d07 systematic-override-rationalized → d12 irrevocable-Khepri-repetition; 6-rank collapse across full book"
        - axis: capability
          direction: up
          target_delta_magnitude: 6
          cost_ledger_anchor: [cl01a, cl03a, cl05]
          notes: "d01 first-deployment → d04 Khepri-rhyming-surveillance → d12 fully-deployed-and-load-bearing; 6-rank rise across full book"
        - axis: position-prot-rise
          direction: up
          target_delta_magnitude: 6
          cost_ledger_anchor: [cl02, cl-d07a]
          notes: "rise phase only (d03→d10); ranks 1→7; collapse handed to position-prot-collapse axis; gross motion tracked separately per RISE-THEN-COLLAPSE NOTE"
        - axis: position-prot-collapse
          direction: down
          target_delta_magnitude: 6
          cost_ledger_anchor: [cl07b]
          notes: "collapse phase only (d10→d14); starts from peak ~7 confirmed at d10; collapses to 1 at d14 (dead/expelled); gross motion tracked separately"
        - axis: relational_anchor_status
          direction: up
          target_delta_magnitude: 8
          cost_ledger_anchor: [cl-d06, cl-d08, cl-d11, cl04]
          notes: "monotonic pressure rise; HIGH=WORST; d02 named-but-outside-ledger → d06 structurally-at-risk → d08 load-bearing-in-network → d11 load-bearing-and-named → d14 unprotected-at-burn; rank 9 is the catastrophe"
        - axis: moral_legibility_to_self
          direction: up
          target_delta_magnitude: 4
          cost_ledger_anchor: [cl07a]
          notes: "non-linear net-positive; start 4 (atoning-and-aware); cracks d02/d06/d10; recognition suppressed; full recognition too-late at d14; end 8 LOCKED"
        - axis: political_register-prot
          direction: up
          target_delta_magnitude: 8
          cost_ledger_anchor: [cl-d05, cl06]
          notes: "monotonic contempt rise; d05 readable-resentment (+3) → d09 articulated-contempt → d13 contempt-without-refusal → d14 ledger-of-the-empowered; end 9 LOCKED"
        - axis: social_tether-prot-rise
          direction: up
          target_delta_magnitude: 7
          cost_ledger_anchor: [cl01b, cl03b, cl-d08b]
          notes: "rise phase only (d01→d10); ranks 1→8; peaks at d07 (load-bearing formalized); non-extractable confirmed d10; collapse handed to social_tether-prot-collapse axis"
        - axis: social_tether-prot-collapse
          direction: down
          target_delta_magnitude: 7
          cost_ledger_anchor: [cl07a]
          notes: "collapse phase only (d10→d14); starts from peak ~8; collapses to 1 at d14 (tether severed, patron dissolved, network transferred); gross motion tracked separately"
        - axis: social_tether-antag
          direction: up
          target_delta_magnitude: 8
          cost_ledger_anchor: [cl-antag-d03, cl-antag-d10]
          notes: "Otto leverage rise; d03 offer-accepted (+4) → d10 non-extractable-confirmed (+4); mirrors position-prot rise; end 9 LOCKED"
        - axis: position-world
          direction: up
          target_delta_magnitude: 4
          cost_ledger_anchor: [cl-world-d04, cl07b]
          notes: "Green-faction KL institutional consolidation; d04 Flea Bottom intelligence layer → d07 arrangement formalized → d14 locked; rises in exact proportion to moral_framework collapse"
        - axis: political_register-world
          direction: up
          target_delta_magnitude: 4
          cost_ledger_anchor: [cl-world-d07, cl07c]
          notes: "Green succession position secured; mirrors political_register-prot contempt rise — Taylor despises what she consolidates; +2 ledger-explicit + ~+2 trajectory-narrative fill (within ±1 tolerance)"
      axes_held: []
      density_target: 0.7-0.9
    stale_since: null
    vibe_cloud:
      keys:
        - "cold-utilitarian interiority — the ledger runs even when the reader wishes it would not"
        - "penitential-grey King's Landing — stone, tallow, rain-smell; beauty available only to people not paying attention"
        - "tragic-causal (every good act auditable backward to the harm it enabled)"
        - "contempt-without-refusal — the protagonist sees clearly, names accurately, and continues"
        - "smallfolk-gallows register — permitted; no comic relief; gallows before spectacle"
        - "residue not spectacle (magic) — insect-sense as texture and dread, never wonder"
        - "atonement-as-repetition — the ledger's final entry names this explicitly"
        - "rising entrapment — each chapter closes a door that was open at the chapter's open"
    # drama: authored downstream at /and-substance book Phase 4
    # chapters[]: authored downstream at /and-substance book Phase 2
