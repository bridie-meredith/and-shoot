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

  # /and-substance series Phase 4 — signature authored 2026-05-24; pulp-enthusiast Phase 4b accept verdict.
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

      - slug: position
        dimension: "legibility and standing within the KL court power structure"
        one_means: "smallfolk-anonymous — no rank, no coin above subsistence, invisible to every court layer"
        five_means: "known-quantity-to-one-court-layer — Otto aware of Taylor; function defined; no formal standing"
        nine_means: "Otto's-unofficial-instrument-at-full-load — position-of-no-exit; too legible to be released"
        perspective: protagonist
        start_rank: 1
        end_rank: 1
        class: plot
        notes: "rise-then-collapse; rises to ~6 at d07 (Otto's-unofficial-instrument), peaks ~7 at d10 (position-of-no-exit), collapses to 1 at d14 (dead/expelled); LOCKED end-state; per-chapter contracts track rise and collapse separately"

      - slug: position
        dimension: "Green-faction consolidation of KL institutional control"
        one_means: "contested succession, no faction controls court apparatus; council fluid"
        five_means: "Green faction dominant in council but succession unresolved; Viserys alive, Rhaenyra a live claimant"
        nine_means: "Green-faction control of Maegor Holdfast, Small Council, and succession angle — apparatus locked"
        perspective: world
        start_rank: 5
        end_rank: 9
        class: plot
        notes: "monotonic rise; Taylor's intelligence deliveries are the consolidation mechanism; world gains exactly as protagonist pays moral_framework"

      - slug: social_tether
        dimension: "depth and load-bearing weight of Taylor's relational and institutional ties in KL"
        one_means: "nil — arrived in an alley with nothing; no name anyone will remember; no institutional cover"
        five_means: "smallfolk-embedded and patron-adjacent — Flea Bottom contacts; Otto aware but arrangement not yet structural"
        nine_means: "load-bearing-in-Otto's-architecture — network structural to Greens; Taylor cannot exit without triggering collapse"
        perspective: protagonist
        start_rank: 1
        end_rank: 1
        class: plot
        notes: "rise-then-collapse; rises to ~7 at d04, peaks ~8 at d07, exposed and non-extractable at d10, severed at d14; LOCKED end-state; per-chapter contracts track rise and collapse separately"

      - slug: social_tether
        dimension: "Otto Hightower's leverage over Taylor through the network she builds"
        one_means: "Otto has no knowledge of Taylor; no leverage exists"
        five_means: "Otto has identified the capability and made the offer; leverage embryonic — Taylor could still walk"
        nine_means: "Taylor is too load-bearing to withdraw; Otto's leverage is structural; exit would trigger counter-action"
        perspective: antagonist
        start_rank: 1
        end_rank: 9
        class: plot
        notes: "monotonic rise tracking Taylor's embeddedness; Otto gains leverage at d03, leverages it fully by d10 (non-extractable confirmed)"

      - slug: relational_anchor_status
        dimension: "operational weight loading onto the un-priced relational anchor ([cost-bearer])"
        one_means: "anchor present; no operational weight — Taylor is attached, [cost-bearer] not yet in any calculus"
        five_means: "anchor inside the protection architecture without [cost-bearer]'s knowledge or consent; Taylor routing around use-vectors"
        nine_means: "[cost-bearer]'s exclusion from the ledger is structurally causal to their death — the un-priced item is the one Taylor could not defend"
        perspective: protagonist
        start_rank: 1
        end_rank: 9
        class: emotional
        notes: "monotonic rise in pressure — the relationship itself does not change, the weight of not-pricing it does; [cost-bearer] never enters the ledger; d14 is the revelation; LOCKED"

      - slug: moral_legibility_to_self
        dimension: "accuracy and completeness of Taylor's self-accounting against what she is actually doing"
        one_means: "no accounting at all — operating blind or in full denial; impossible for Taylor; floor is 3"
        five_means: "rationalizing-each-trade — accounting runs but each entry is filed as acceptable; recognition exists, is suppressed"
        nine_means: "recognition-too-late: full clarity on the repetition, delivered by the ledger, in time only to be unable to deny it"
        perspective: protagonist
        start_rank: 4
        end_rank: 8
        class: emotional
        notes: "non-linear net-positive; start 4 (atoning-and-aware, believes she's succeeding); cracks d02/d06/d10; recognition suppressed at d10; full recognition at d14; end 8 not 9 because too-late diminishes usability; LOCKED"

      - slug: political_register_toward_elite
        dimension: "Taylor's stance toward the Westerosi ruling class as revealed by what the insect-feed returns"
        one_means: "neutral-instrumentally-observant — reads the court as a system; no investment, no contempt, no affect"
        five_means: "readable-resentment — color has accumulated; not yet named; the insects bring it back and Taylor notices"
        nine_means: "contempt-without-refusal — fully articulate, cold, named by name, bound to continued service; clarity as its own trap"
        perspective: protagonist
        start_rank: 1
        end_rank: 9
        class: emotional
        notes: "monotonic rise; d05 resentment readable, d09 articulated-contempt, d13 contempt-without-refusal (LOCKED end); the contempt is the ledger in its final form"

      - slug: political_register_toward_elite
        dimension: "Green-faction succession position — the continuity Taylor's trades guarantee"
        one_means: "succession unresolved; Greens without institutional advantage; rival claims live"
        five_means: "Green faction dominant in informal channels; Otto operating effectively outside council"
        nine_means: "Green-faction position secured — Maegor Holdfast, Small Council, dynastic angle locked; continuity guaranteed until Dance ignites"
        perspective: world
        start_rank: 5
        end_rank: 9
        class: plot
        notes: "monotonic rise; mirrors Taylor's political_register rise — she despises what she is consolidating; world benefits in exact proportion to her contempt growing"

    # actor_baselines: AUTHORED AT STEP 4d (post-cast); HARD-ABORT on first /and-substance book Phase 0 if empty.
    actor_baselines: []

    cost_ledger:
      - id: cl01
        gain: "capability +2, social_tether +2"
        cost: "opportunity-missed: rescue is witnessed; witch-label forms; [cost-bearer] block enters the exposure radius"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl02
        gain: "position +4"
        cost: "moral_framework -3"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl03
        gain: "capability +3, social_tether +4"
        cost: "moral_framework -3"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl04
        gain: "relational_anchor_status +3"
        cost: "opportunity-missed: extraction path before network became non-withdrawable"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl05
        gain: "capability +2"
        cost: "moral_framework -2"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl06
        gain: "political_register_toward_elite +5"
        cost: "opportunity-missed: contempt arrives with no exit attached; clarity forecloses nothing"
        anchor: { book: b01, chapter: null, scene: null }
      - id: cl07
        gain: "moral_legibility_to_self +4"
        cost: "relational_anchor_status +4, social_tether -7, position -6"
        anchor: { book: b01, chapter: null, scene: null }

    antagonist_pressure:
      - axis: moral_framework
        pressure_source: "Otto Hightower — each ask prices a specific protection, making refusal a calculation rather than a prohibition"
        cost_curve: "escalates monotonically; d03 opens the account, d07 formalizes it, d12 makes it irrevocable; Otto never presses — the calculation does"
      - axis: social_tether
        pressure_source: "Otto Hightower — the network Taylor builds to survive is simultaneously the architecture that makes her non-extractable"
        cost_curve: "escalates then caps; peaks at d10 (non-extractable confirmed); d14 collapses the tether entirely as the patron channel dissolves with Taylor's removal"
      - axis: position
        pressure_source: "Otto Hightower — formal legibility as his unofficial instrument; too load-bearing to release, too informal to protect"
        cost_curve: "escalates to d10 peak (position-of-no-exit), then collapses at d14 when Taylor's removal makes the position irrelevant"
      - axis: relational_anchor_status
        pressure_source: "cond-kl-witch-label-formation-122ac — the witch-label social physics that makes Taylor's insect-use publicly visible and routes community suspicion toward her contacts"
        cost_curve: "escalates monotonically from d01 (witnesses at rescue) through d04 (network threads through wards); caps when Taylor routes around vectors that might expose [cost-bearer] to Otto"
      - axis: relational_anchor_status
        pressure_source: "Dance-ignition timeline — the structural antagonist Taylor cannot name or see; the background war schedule that makes every protection window provisional"
        cost_curve: "invisible and constant; not escalating in Taylor's perception; catastrophically present at d14 when the timeline's bladed answer moves through the mapped streets"
      - axis: moral_legibility_to_self
        pressure_source: "Gold Morning memory — internal antagonist; the standard against which Taylor measures every override; the specific shape she is repeating"
        cost_curve: "oscillates; suppressed at each rationalization beat (d06, d10, d11); surfaces sharply at d09 (articulated contempt) and terminally at d14 (recognition-too-late)"

    chunk_targets:
      series:  { delta_per_signature_axis: 4-8,     density_target: 0.6-0.9 }
      book:    { delta_per_signature_axis: 3-4,     density_target: 0.7-0.9, bone_count: 270-500 }
      chapter: { delta_per_signature_axis: 0.5-1.5, density_target: 0.5-0.9, bone_count: 15-75 }
      scene:   { delta_per_signature_axis: 0-1.5,   density_target: 0.6-0.9, bone_count: 5-15 }
      bone:    { delta_per_axis: 1-3, axes_per_bone: 1-2 }

    # Phase 4b verdict (pulp-enthusiast taste-judge): ACCEPT.
    # Watch-items (downstream execution):
    #   - Dance-ignition timeline (d10-d14): chapter contracts must keep visible, on-page complications;
    #     do not let the countdown-only sequences become slow-burn-interiority.
    #   - Position/social_tether rise-then-collapse: d14 collapse must read as complication cascade, not deflation.
    #   - relational_anchor_status: keep beats attached to plot events (network decisions, interception, coverage),
    #     not interiority alone; d06/d08/d11 already structured for this.
    # Verdict transcript: active-project/staff/showrunner/_drafts/phase-4b-pulp-verdict.md
