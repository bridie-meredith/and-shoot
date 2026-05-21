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
    approved_at: 2026-05-18T123000Z
    approved_by: user
    report_path: active-project/staff/reviews/series-audit-2026-05-18T120000Z.md
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

    actor_baselines:
      # Per-actor positional grid (added 2026-05-21; densified 2026-05-21 pass-2 for systematic coverage).
      # DENSE MATRIX: every cast_roster actor × every state_axes axis. 8 actors × 9 axes = 72 cells.
      # No omissions — `applicability: not-applicable` makes the deliberate exclusion explicit at the cell.
      #
      # state_axes above pins per-perspective aggregate positions (protagonist / antagonist / world).
      # actor_baselines disambiguates within a perspective — two antagonist-perspective actors with very
      # different arcs, supporting-perspective actors who do not share a single arc, etc.
      #
      # `applicability` values:
      #   moves           — start_rank ≠ end_rank; actor's position arcs across the book
      #   static          — start_rank = end_rank; actor's position is deliberately pinned (examined, not skipped)
      #   not-applicable  — actor does not participate in this axis's machinery; rationale REQUIRED in notes
      #
      # `source` lineage values:
      #   lifted-from-state-axes       — verbatim from the perspective-aggregate above
      #   inferred-from-role-card      — built from cast-roster role descriptions + book chunk
      #   scene-pinned-<chapter-slug>  — pinned when a chapter's scenes resolved the actor's position
      #
      # COVERAGE TABLE (axis × actor; m=moves, s=static, x=not-applicable):
      #                        mf  cap pos st  ras mls pre kn  ag
      #   taylor               m   m   m   m   m   m   m   m   m       (9 moves — protagonist; lifted)
      #   otto                 m   m   m   m   m   m   m   m   m       (9 moves — antagonist primary; lifted)
      #   aemond               x   s   s   s   x   x   x   x   s       (walk-on; 4 static, 5 n/a)
      #   wren                 x   s   s   m   m   x   x   s   x       (cost-bearer; 2 moves, 3 static, 4 n/a)
      #   sera                 x   s   s   s   x   x   x   x   s       (protect-target; 4 static, 5 n/a)
      #   gylda                x   s   s   s   x   x   x   m   x       (witness-mirror; 1 moves, 3 static, 5 n/a)
      #   coll                 x   s   s   s   x   x   x   s   x       (fixture; 4 static, 5 n/a)
      #   corvan               x   x   s   x   x   x   x   s   x       (frame-coda; 2 static, 7 n/a)
      #   ---
      #   total cells filled: 8 × 9 = 72; moves 21, static 20, not-applicable 31.

      # ============================================================================================
      # taylor-hebert-kl-122ac (protagonist) — 9 moves, lifted-from-state-axes
      # ============================================================================================
      - { actor: taylor-hebert-kl-122ac, axis: moral-framework,                  applicability: moves,  start_rank: 3,    end_rank: 1,    source: lifted-from-state-axes, notes: "3→1; d03 first-exception → d07 systematic → d12 irrevocable" }
      - { actor: taylor-hebert-kl-122ac, axis: capability,                       applicability: moves,  start_rank: 3,    end_rank: 7,    source: lifted-from-state-axes, notes: "3→7; dormant by choice → Khepri-rhyming-surveillance-architecture; suppressed-baseline at b01c01" }
      - { actor: taylor-hebert-kl-122ac, axis: position,                         applicability: moves,  start_rank: 1,    end_rank: 1,    source: lifted-from-state-axes, notes: "1→5→1 net=0; visibility-phase (d01–d09) → entrapment-phase (d10–d14); start_rank=end_rank but applicability=moves because intra-book trajectory is two-phase" }
      - { actor: taylor-hebert-kl-122ac, axis: social-tether,                    applicability: moves,  start_rank: 2,    end_rank: 1,    source: lifted-from-state-axes, notes: "2→1; embedded → load-bearing → exposed → severed at d14 (Wren death + Otto channel dissolved)" }
      - { actor: taylor-hebert-kl-122ac, axis: relational-anchor-status,         applicability: moves,  start_rank: 3,    end_rank: 1,    source: lifted-from-state-axes, notes: "3→1; the un-priced relationship's position to the ledger; cl-unpriced-cost-bearer + cl-protection-buys-consolidation each -1" }
      - { actor: taylor-hebert-kl-122ac, axis: moral-legibility-to-self,         applicability: moves,  start_rank: 7,    end_rank: 4,    source: lifted-from-state-axes, notes: "7→4; atoning-and-aware → recognition-too-late; inverted emotional rubric — starts high" }
      - { actor: taylor-hebert-kl-122ac, axis: political-register-toward-elite,  applicability: moves,  start_rank: 5,    end_rank: 9,    source: lifted-from-state-axes, notes: "5→9; resentment → contempt-without-refusal; rising IS the cost" }
      - { actor: taylor-hebert-kl-122ac, axis: knowledge,                        applicability: moves,  start_rank: 3,    end_rank: 8,    source: lifted-from-state-axes, notes: "3→8; immediate-block → more complete picture than most Small Council members" }
      - { actor: taylor-hebert-kl-122ac, axis: agency,                           applicability: moves,  start_rank: 5,    end_rank: 1,    source: lifted-from-state-axes, notes: "5→1; self-directed → locked into no-exit then expelled; steepest single loss-arc" }

      # ============================================================================================
      # otto-hightower (antagonist primary; intelligence architect) — 9 moves, lifted-from-state-axes
      # Otto is the antagonist-perspective archetype; perspective-aggregate fits him exactly.
      # ============================================================================================
      - { actor: otto-hightower, axis: moral-framework,                  applicability: moves,  start_rank: 7,    end_rank: 8,    source: lifted-from-state-axes, notes: "7→8; factional moral system intact and strengthening; Green-faction's working ethics; Otto IS the antagonist-perspective archetype" }
      - { actor: otto-hightower, axis: capability,                       applicability: moves,  start_rank: 5,    end_rank: 8,    source: lifted-from-state-axes, notes: "5→8; intelligence apparatus reach: court informants → full-spectrum coverage from Flea Bottom to Holdfast (with Taylor's network as ground layer)" }
      - { actor: otto-hightower, axis: position,                         applicability: moves,  start_rank: 6,    end_rank: 8,    source: lifted-from-state-axes, notes: "6→8; advisory-from-outside → Hand-in-fact; factional standing consolidates" }
      - { actor: otto-hightower, axis: social-tether,                    applicability: moves,  start_rank: 7,    end_rank: 9,    source: lifted-from-state-axes, notes: "7→9; single-layer faction → cross-layer factional dominance" }
      - { actor: otto-hightower, axis: relational-anchor-status,         applicability: moves,  start_rank: 5,    end_rank: 6,    source: lifted-from-state-axes, notes: "5→6; instrumentalized relational anchors; minor strengthening as inner-circle attachment + utility deepens" }
      - { actor: otto-hightower, axis: moral-legibility-to-self,         applicability: moves,  start_rank: 6,    end_rank: 7,    source: lifted-from-state-axes, notes: "6→7; instrumental self-reading → fully self-confirming" }
      - { actor: otto-hightower, axis: political-register-toward-elite,  applicability: moves,  start_rank: 7,    end_rank: 8,    source: lifted-from-state-axes, notes: "7→8; structurally reinforced dynastic prerogative" }
      - { actor: otto-hightower, axis: knowledge,                        applicability: moves,  start_rank: 7,    end_rank: 9,    source: lifted-from-state-axes, notes: "7→9; experienced court-layer reach → complete KL intelligence picture (via Taylor's coverage layer)" }
      - { actor: otto-hightower, axis: agency,                           applicability: moves,  start_rank: 7,    end_rank: 9,    source: lifted-from-state-axes, notes: "7→9; constrained-but-directing → structural maximum over dynastic outcomes" }

      # ============================================================================================
      # aemond-targaryen-122ac (antagonist walk-on; Vhagar rider) — 4 static + 5 not-applicable
      # Walk-on archetype: appearances DEPLOY pre-existing capability at structural crisis points;
      # no per-axis arc; positions are pinned-static where he has them.
      # ============================================================================================
      - { actor: aemond-targaryen-122ac, axis: moral-framework,                  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "walk-on; Green-faction loyalty given as a structural fact, not interrogated; no ethical-accounting arc to track" }
      - { actor: aemond-targaryen-122ac, axis: capability,                       applicability: static,         start_rank: 9,    end_rank: 9,    source: inferred-from-role-card, notes: "Vhagar (largest living dragon); rank 9 throughout; Aemond's appearances DEPLOY the capability, do not arc it" }
      - { actor: aemond-targaryen-122ac, axis: position,                         applicability: static,         start_rank: 7,    end_rank: 7,    source: inferred-from-role-card, notes: "Green-faction prince; court-tier high; static across walk-on appearances" }
      - { actor: aemond-targaryen-122ac, axis: social-tether,                    applicability: static,         start_rank: 8,    end_rank: 8,    source: inferred-from-role-card, notes: "royal birth + Green-faction inner-circle; cross-layer factional embedded by birthright" }
      - { actor: aemond-targaryen-122ac, axis: relational-anchor-status,         applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "not a relational-anchor track participant; cost-bearer / protect-target machinery does not include Aemond" }
      - { actor: aemond-targaryen-122ac, axis: moral-legibility-to-self,         applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "archetype-flat coercive arm; the book does not interrogate Aemond's self-accounting" }
      - { actor: aemond-targaryen-122ac, axis: political-register-toward-elite,  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "Aemond IS elite; the axis tracks register TOWARD elite from non-elite positions — does not apply" }
      - { actor: aemond-targaryen-122ac, axis: knowledge,                        applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "not a knowledge-tracking arc; Aemond's awareness is local-to-appearance, not a court-intelligence picture in the book's terms" }
      - { actor: aemond-targaryen-122ac, axis: agency,                           applicability: static,         start_rank: 8,    end_rank: 8,    source: inferred-from-role-card, notes: "royal prince + Vhagar rider; high agency but static — walk-on appearances do not arc this" }

      # ============================================================================================
      # wren-stitch-maker-flea-bottom-ward (supporting/cost-bearer) — 2 moves + 3 static + 4 not-applicable
      # Wren's load-bearing axis is relational-anchor-status (Taylor's POV) and social-tether (her own
      # ward-community); the rest are static-at-low (child, no power) or not-applicable (child, not
      # interrogated as a moral-accounting agent).
      # ============================================================================================
      - { actor: wren-stitch-maker-flea-bottom-ward, axis: moral-framework,                  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "11-year-old ward; the book does not interrogate Wren as an ethical-accounting agent — she is the cost-bearer, not a moral actor with an arc" }
      - { actor: wren-stitch-maker-flea-bottom-ward, axis: capability,                       applicability: static,         start_rank: 1,    end_rank: 1,    source: inferred-from-role-card, notes: "child seamstress-ward; no power; static throughout" }
      - { actor: wren-stitch-maker-flea-bottom-ward, axis: position,                         applicability: static,         start_rank: 1,    end_rank: 1,    source: inferred-from-role-card, notes: "smallfolk-ward; no court layer; static (cannot rise — child + cost-bearer slot)" }
      - { actor: wren-stitch-maker-flea-bottom-ward, axis: social-tether,                    applicability: moves,          start_rank: 5,    end_rank: 1,    source: inferred-from-role-card, notes: "5→1; seamstress-family ward + ward-community embedded → dead at d14; social-tether IS the seamstress-ward layer until the violence" }
      - { actor: wren-stitch-maker-flea-bottom-ward, axis: relational-anchor-status,         applicability: moves,          start_rank: 3,    end_rank: 1,    source: inferred-from-role-card, notes: "3→1; named-outside-ledger (d02) → load-bearing-but-still-unpriced (d08) → unprotected-at-burn (d14); arc reads via Taylor's POV but Wren's life-events track it — observed → necessary-to-coverage → dead" }
      - { actor: wren-stitch-maker-flea-bottom-ward, axis: moral-legibility-to-self,         applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "child; not interrogated as a self-accounting agent" }
      - { actor: wren-stitch-maker-flea-bottom-ward, axis: political-register-toward-elite,  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "smallfolk-ward; outside the layer that registers toward elite in a tracked way" }
      - { actor: wren-stitch-maker-flea-bottom-ward, axis: knowledge,                        applicability: static,         start_rank: 3,    end_rank: 3,    source: scene-pinned-b01c01,    notes: "distributed-attention habit established at b01c01 (asks too many questions; watches what adults pretend not to see); rank 3 stable — habit is the witnessing tool, not an arc" }
      - { actor: wren-stitch-maker-flea-bottom-ward, axis: agency,                           applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "child agency at survival-grain; not an axis the book tracks for Wren's arc" }

      # ============================================================================================
      # sera-hightower-kl-122ac (supporting/protect-target) — 4 static + 5 not-applicable
      # Sera's stability IS the dramatic event: cl-protection-buys-consolidation preserves her by
      # design. Her positions hold throughout the book because the architecture holds them.
      # ============================================================================================
      - { actor: sera-hightower-kl-122ac, axis: moral-framework,                  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "court ward age 14; archetype-flat in book's frame; not interrogated as moral-accounting agent" }
      - { actor: sera-hightower-kl-122ac, axis: capability,                       applicability: static,         start_rank: 2,    end_rank: 2,    source: inferred-from-role-card, notes: "court ward age 14; minimal personal capability; static" }
      - { actor: sera-hightower-kl-122ac, axis: position,                         applicability: static,         start_rank: 4,    end_rank: 4,    source: inferred-from-role-card, notes: "Hightower cadet-branch ward; court-tier present-but-vulnerable; STABLE because the architecture preserves it from collapsing to 1; survives the succession crisis" }
      - { actor: sera-hightower-kl-122ac, axis: social-tether,                    applicability: static,         start_rank: 6,    end_rank: 6,    source: inferred-from-role-card, notes: "Hightower cadet-branch + court-ward network; stable — same architecture preserves the tether" }
      - { actor: sera-hightower-kl-122ac, axis: relational-anchor-status,         applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "different track from cost-bearer; Sera is protect-target, not relational-anchor for Taylor — does not know Taylor exists" }
      - { actor: sera-hightower-kl-122ac, axis: moral-legibility-to-self,         applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "not interrogated as self-accounting agent" }
      - { actor: sera-hightower-kl-122ac, axis: political-register-toward-elite,  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "Sera IS elite cadet-branch; the axis tracks register TOWARD elite from non-elite — does not apply" }
      - { actor: sera-hightower-kl-122ac, axis: knowledge,                        applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "not a knowledge-tracking arc participant; the book does not pin Sera's intelligence picture" }
      - { actor: sera-hightower-kl-122ac, axis: agency,                           applicability: static,         start_rank: 2,    end_rank: 2,    source: inferred-from-role-card, notes: "court ward; constrained agency; static throughout (preserved-not-empowered)" }

      # ============================================================================================
      # gylda-saltwater-flea-bottom (supporting/witness-mirror) — 1 moves + 3 static + 5 not-applicable
      # Gylda's load-bearing event is the d09-d10 naming of the too-many-places pattern; knowledge
      # spike but non-confidant hard fence means it does not propagate.
      # ============================================================================================
      - { actor: gylda-saltwater-flea-bottom, axis: moral-framework,                  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "Flea Bottom water-carrier; not interrogated as moral-accounting agent" }
      - { actor: gylda-saltwater-flea-bottom, axis: capability,                       applicability: static,         start_rank: 1,    end_rank: 1,    source: inferred-from-role-card, notes: "water-carrier; no power; static" }
      - { actor: gylda-saltwater-flea-bottom, axis: position,                         applicability: static,         start_rank: 1,    end_rank: 1,    source: inferred-from-role-card, notes: "Flea Bottom smallfolk; no court layer; static" }
      - { actor: gylda-saltwater-flea-bottom, axis: social-tether,                    applicability: static,         start_rank: 4,    end_rank: 4,    source: inferred-from-role-card, notes: "Flea Bottom water-carrier network; cross-block visibility; static" }
      - { actor: gylda-saltwater-flea-bottom, axis: relational-anchor-status,         applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "not a relational-anchor for Taylor; witness-mirror role is structural, not relational" }
      - { actor: gylda-saltwater-flea-bottom, axis: moral-legibility-to-self,         applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "not interrogated as self-accounting agent" }
      - { actor: gylda-saltwater-flea-bottom, axis: political-register-toward-elite,  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "no register-toward tracked for Gylda; the book uses her as observer, not as political-positioned actor" }
      - { actor: gylda-saltwater-flea-bottom, axis: knowledge,                        applicability: moves,          start_rank: 2,    end_rank: 4,    source: inferred-from-role-card, notes: "2→4 at d09-d10 only; observes too-many-places pattern and names it once; non-confidant hard fence means knowledge does not propagate further; the move IS the named-once event" }
      - { actor: gylda-saltwater-flea-bottom, axis: agency,                           applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "not an agency-tracked arc; Gylda's role is the moment-of-naming, not directional action" }

      # ============================================================================================
      # coll-net-mender-flea-bottom (world/fixture; non-interpretive substrate) — 4 static + 5 not-applicable
      # Coll IS the Flea Bottom social-physics baseline against which Taylor's arc plays. All present
      # axes hold flat; the role is "non-interpretive community-substrate carrier; never names."
      # ============================================================================================
      - { actor: coll-net-mender-flea-bottom, axis: moral-framework,                  applicability: not-applicable, start_rank: null, end_rank: null, source: scene-pinned-b01c01, notes: "non-interpretive substrate; the role explicitly refuses moral-accounting voice ('never names'); does not arc on this axis by design" }
      - { actor: coll-net-mender-flea-bottom, axis: capability,                       applicability: static,         start_rank: 1,    end_rank: 1,    source: scene-pinned-b01c01, notes: "net-mending; no power; static" }
      - { actor: coll-net-mender-flea-bottom, axis: position,                         applicability: static,         start_rank: 1,    end_rank: 1,    source: scene-pinned-b01c01, notes: "block-fixture; no court layer; static — Coll IS the Flea Bottom social-physics baseline" }
      - { actor: coll-net-mender-flea-bottom, axis: social-tether,                    applicability: static,         start_rank: 5,    end_rank: 5,    source: scene-pinned-b01c01, notes: "one-block embedded; range of observation exactly one street; static" }
      - { actor: coll-net-mender-flea-bottom, axis: relational-anchor-status,         applicability: not-applicable, start_rank: null, end_rank: null, source: scene-pinned-b01c01, notes: "not a relational-anchor track participant for Taylor; Coll provides proximity-as-cover, not relational anchoring" }
      - { actor: coll-net-mender-flea-bottom, axis: moral-legibility-to-self,         applicability: not-applicable, start_rank: null, end_rank: null, source: scene-pinned-b01c01, notes: "non-interpretive substrate; the role refuses interpretive interiority by construction" }
      - { actor: coll-net-mender-flea-bottom, axis: political-register-toward-elite,  applicability: not-applicable, start_rank: null, end_rank: null, source: scene-pinned-b01c01, notes: "no register tracked; Coll's role is substrate-carrier, not political-positioned" }
      - { actor: coll-net-mender-flea-bottom, axis: knowledge,                        applicability: static,         start_rank: 4,    end_rank: 4,    source: scene-pinned-b01c01, notes: "intimate block-level knowledge of Flea Bottom; does not name what he sees; static — Coll's knowledge does not propagate or arc, it provides cover" }
      - { actor: coll-net-mender-flea-bottom, axis: agency,                           applicability: not-applicable, start_rank: null, end_rank: null, source: scene-pinned-b01c01, notes: "not an agency-tracked arc; the fixture role is non-directional by design" }

      # ============================================================================================
      # corvan-archmaester-retrospective-coda (world/coda) — 2 static + 7 not-applicable
      # Frame-coda voice writing c.160 AC; outside the 122 AC book's time-frame; b01c18 INTERLUDE
      # chapter is bone-gate exempt per chapter_class:frame-coda.
      # ============================================================================================
      - { actor: corvan-archmaester-retrospective-coda, axis: moral-framework,                  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "frame voice; outside 122 AC scope; not interrogated as in-book moral actor" }
      - { actor: corvan-archmaester-retrospective-coda, axis: capability,                       applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "frame voice; not a capability-bearing actor in the in-book sense" }
      - { actor: corvan-archmaester-retrospective-coda, axis: position,                         applicability: static,         start_rank: 5,    end_rank: 5,    source: inferred-from-role-card, notes: "Archmaester at the Citadel (c.160 AC); frame-coda voice; in-book Δ exempt — position pinned for grid consistency only" }
      - { actor: corvan-archmaester-retrospective-coda, axis: social-tether,                    applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "frame voice; in-book tether does not apply (writes from 38 years later)" }
      - { actor: corvan-archmaester-retrospective-coda, axis: relational-anchor-status,         applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "frame voice; no relational anchor to Taylor or cost-bearer apparatus" }
      - { actor: corvan-archmaester-retrospective-coda, axis: moral-legibility-to-self,         applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "frame voice; the chronicle is about Taylor's apparatus, not Corvan's self-accounting" }
      - { actor: corvan-archmaester-retrospective-coda, axis: political-register-toward-elite,  applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "frame voice; Corvan's register is archival-evidential, not political-positioned in the tracked sense" }
      - { actor: corvan-archmaester-retrospective-coda, axis: knowledge,                        applicability: static,         start_rank: 6,    end_rank: 6,    source: inferred-from-role-card, notes: "retrospective archival picture; incomplete by design (does not know Taylor's name); frame-coda — no Δ across the book; pinned for grid consistency only" }
      - { actor: corvan-archmaester-retrospective-coda, axis: agency,                           applicability: not-applicable, start_rank: null, end_rank: null, source: inferred-from-role-card, notes: "frame voice; no in-book agency to track" }

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
      chapter_count: 18    # set by /and-substance book b01 Phase 2; range 18-22 per series.structure
    substance_delta:
      axes_in_motion:
        - { axis: moral-framework,              direction: down, target_delta_magnitude: 2, cost_ledger_anchor: cl-otto-trade,                  notes: "3→1 protagonist; d03 first-exception → d07 systematic → d12 irrevocable" }
        - { axis: capability,                   direction: up,   target_delta_magnitude: 4, cost_ledger_anchor: cl-network-position,            notes: "3→7; d01 localized → d04 Khepri-rhyming-surveillance-architecture → d12 fully-deployed; architecture is surveillance+unconsented-instrumentalization, not control-override" }
        # position axis is split into two phase-entries under the 2026-05-21 axis-bookkeeping split (no more direction:null);
        # net = 0 across the book is the algebraic aggregate of these two phases, not a "no movement" claim.
        - { axis: position,                     direction: up,   target_delta_magnitude: 4, cost_ledger_anchor: cl-social-tether-build,         notes: "visibility-phase d01–d09; 1→5; rise to Otto's-unofficial-instrument; arrangement formalizes; position-visibility crystallizes" }
        - { axis: position,                     direction: down, target_delta_magnitude: 4, cost_ledger_anchor: cl-social-tether-build,         notes: "entrapment-phase d10–d14; 5→1; collapse to no-exit then expulsion; intra-book net = 0 against visibility-phase entry above" }
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
    drama: |
      What cannot survive this book is the prohibition — not because it was weak, but because it was exactly strong enough to survive every confrontation except the arithmetic. Taylor Hebert arrives in King's Landing holding one line she will not cross: no one becomes an instrument again. That prohibition is not a sentiment; it is the load-bearing architecture of her atonement, the one thing that separates what she is doing in Flea Bottom from what she did at Gold Morning. Over the course of this book, Otto Hightower does not destroy the prohibition — he prices it. Each intelligence delivery asks for a fraction less than what the prohibition would cost in lives; each accepted trade slightly lowers the threshold for the next one; by the time the network is fully deployed and Taylor can see its moral shape clearly, she has been inside the repetition for long enough that seeing it constitutes recognition, not refusal. What gets crushed is not Taylor's awareness — her accounting never stops running — but the gap between seeing and stopping. What gets extinguished is the possibility that the penitential framework could have been a working instrument rather than a mirror. What gets named, at the close, is the exchange rate: she empowered the Greens to delay a war, the war ignited anyway on a clock she did not control, and Wren died in the street Taylor had charted. The irony is structural: the prevention apparatus that worked — that genuinely delayed the Dance, that kept Sera Hightower alive through the succession crisis — produced the conditions under which Taylor could not reroute the violence when it came. The ledger is legible. The ledger being legible is the cost.
    chapters:
      - slug: b01c01
        chunk: |
          Taylor Hebert surfaces in King's Landing in the year 122 AC with nothing: no name that means anything, no coin above subsistence, no patron, no plan except the operating rule she has been carrying since Gold Morning — be useful without taking control, present without possessing. She finds a rent corner off the Hook in Flea Bottom and pays for it in copper stars by mending nets alongside Coll, the block's fixture, whose range of observation runs exactly one street and who asks nothing of strangers. The override architecture — the compound-eye awareness that once threaded through a city-sized insect population and moved human bodies like chess pieces — is dormant by choice: she can feel the insects in the walls and under the flagstones, can read the density and temperature of the ward through them, but she keeps the reading passive, keeps herself below the threshold that would make it deployment rather than sense. King's Landing is not Brockton Bay; the buildings are stone and tallow-smoke and the smallfolk's gallows calendar is feast and shortage and plague and lord's levy; no one has a power here that requires containing. She is paying attention to that absence. The chapter establishes the register — cold, accounting, Khepri-haunted without naming Khepri — and the geometry of the ward: what Taylor can see from street-level, what Coll's presence gives her by way of social cover, and where the insect-sense edges of her self-imposed limit fall. Wren, the seamstress-ward from two buildings over, appears at the chapter's edge — not yet significant, not yet named as anything other than a child who asks too many questions.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - { axis: knowledge, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: ~, notes: "Flea Bottom geography read; ward-level pattern established; 3→3.5; passive orientation; pre-arrangement; unanchored knowledge gain at baseline" }
          axes_held:
            - { axis: capability, rationale: "dormant by choice; passive insect-sense only; establishes suppressed baseline at rank 3; the prohibition holds for the whole chapter — this is the discipline before it is tested" }
          density_target: "0.6-0.9"  # tuned up from 0.5-0.6 at /and-substance chapter Phase 5 to envelope scene densities (s01 0.6-0.7 / s02 0.7-0.8 / s03 0.7-0.9); chapter chunk prose itself reads at the lower-mid of band; original book-level estimate was authoring drift
        handoff_in:
          open_threads:
            - "Taylor's operating rule: useful without controlling — the prohibition that will be tested"
            - "no patron, no institutional cover, no name above street-level"
          world_state:
            - "year: 122 AC, late Viserys-I reign; Otto Hightower off Small Council (dismissed 120 AC) but operating advisory from outside"
            - "Flea Bottom: smallfolk substrate; currency copper star / penny; class register smallfolk / landed / lordly / royal"
            - "magic: dormant in KL court layer; insect-sense below Westerosi detection threshold at passive level"
            - "dragons: backgrounded; audible and visible overhead but not on-stage"
            - "King's Landing geography: Hook / Flea Bottom anchor; Red Keep on Aegon's Hill; Dragonpit on Rhaenys's Hill; Great Sept on Visenya's Hill"
          character_state:
            - "taylor-hebert-kl-122ac: moral-framework rank 3 (refusal-of-control intact, explicit, load-bearing); capability rank 3 (dormant by choice); position rank 1 (Flea Bottom anonymous); social-tether rank 2 (nascent Flea Bottom presence, no institutional cover); relational-anchor-status rank 3 (Wren not yet named); moral-legibility-to-self rank 7 (atoning-and-aware; framework fully conscious); political-register-toward-elite rank 5 (neutral-instrumentally-observant); knowledge rank 3 (immediate-block only); agency rank 5 (self-directed; no entrapment yet)"
            - "otto-hightower: position rank 6 (off formal record; advisory influence from outside Small Council); moral-framework rank 7 (functional ethical arithmetic; no strain)"
            - "aemond-targaryen-122ac: offstage; age 12; Vhagar-claimed"
            - "wren-stitch-maker-flea-bottom-ward: present at chapter edge; age 11; not yet named as significant node"
            - "sera-hightower-kl-122ac: offstage; age 14; structural vulnerability not yet Taylor's concern"
          source_chapter: null
        handoff_out:
          open_threads:
            - "Taylor's operating rule intact but not yet tested against an external ask"
            - "Wren introduced as recurring street presence; relationship not yet named"
            - "insect-sense passive; Flea Bottom ward-geography mapped to block level"
          world_state:
            - "122 AC; Flea Bottom; Taylor holds a rent corner off the Hook"
            - "Coll provides social cover by proximity; no explicit arrangement"
            - "insect-sense reads at passive: density, temperature, movement patterns below deployment threshold"
          character_state:
            - "taylor: moral-framework 3; capability 3 (dormant); position 1; social-tether 2; relational-anchor 3; moral-legibility 7; political-register 5; knowledge 3.5; agency 5"
            - "wren: present, recurring, unnamed as significant"
            - "otto: offstage"
          target_chapter: b01c02
        status: audited-r1-mechanical    # /and-facets Phase 5 cleared HARD=0 post-fixer cycle 1; Phase 5b audience-gate CAP-BURNED at cycle 3 with 10/12 facets passing 3-of-3; 2 facets short (sensory, memory) — do NOT advance to audited-r1
        audit_path: active-project/staff/auditor/facets-final-audit-r3.md
        audit_complete: true
        audit_findings: 0    # HARD; ~15 SIGNAL carry-forward
        audience_gate_path: active-project/staff/auditor/facets-audience-gate-r3.md
        audience_gate_complete: true
        audience_gate_cycles: 3
        audience_gate_cap_burned: true
        audience_gate_facets_passed: [location-state, interest-narrator, state-updates, feeling, metaphor, vibes, exposition, dialogue-coll, dialogue-taylor, dialogue-wren]
        audience_gate_facets_failed: [sensory, memory]
        bidirectional_loop: validated
        facets_path: active-project/theater/facets/
        round_1_complete: true
        round_2_complete: true
        orchestrator_critic_verdict: NOT-SUCCESSFUL   # cap-burn → NOT-SUCCESSFUL per critic card hot-button
        bones_file: theater/bones/b01-c01.md
        bones_count: 27    # 9 s01 + 10 s02 + 8 s03; max(flat_id) = 29 (deletions s01n03/s01n11/s03n09 leave gaps; blank time-skips at flat 10, 21)
        substance_bone_gate_verdict: PASS    # Phase 6 mechanical PASS (HARD: 0, SIGNAL: 0) + audience SUBSTANCE-FELT 9/9 (3 personas × 3 scenes; no HARD votes)
        stitched: true    # /and-stitch 2026-05-20 PASS — post rejected-items removal (mem:1 @9, sensory:3 @17) — clean draft active-project/draft/b01-c01.md + annotated b01-c01.annotated.md + render-log render-log-b01-c01.md
        stitch_path: active-project/draft/b01-c01.md
        stitch_render_log: active-project/staff/stitcher/render-log-b01-c01.md
        stitch_stats:
          words: 599
          paragraphs: 14    # 2 preamble + 12 body
          sentences: 22    # 2 preamble + 20 body
          bones_rendered: 27
          dialogue_utterances: 4
          exposition_entries_rendered: 5
          cut_clauses: 5
          rewords: 1
          reshows: 0
          cut_bones: 0
          faults_surfaced: 4    # 1 FAULT-EXPOSITION-AUDIT-MISS, 3 FAULT-AUDIT-MISS (Q9-hits on facet content; render-as-is; surfaced for upstream review)
          fence_stretches_resolved: 1    # @24 "from the mesh" CUT-CLAUSE
        substance_delta_measured:
          axes_moved: { knowledge: 0.53 }                  # scene-sum: s01 0.19 + s02 0.24 + s03 0.10 = 0.53 against chapter target 0.5 (within band)
          axes_held_verified: [capability]                 # capability held at rank 3 across all 3 scenes; 7 of 27 bones carry capability in axes_held (4 of those are stillness-against-pressure holds discipline bones, 3 are ambient-drift held-by-rule). Discipline enacted, not just stated. Replaces prior `axes_moved: { capability: 0 }` bookkeeping under the 2026-05-21 axis split.
          density_measured: ~     # facet/stitch-layer measurement; bone-density approximated within target band 0.6-0.9 by scene aggregation
          felt_verdict: PASS-3-of-3   # cape-fic-reader + dark-fantasy-reader + worm-canon-pedant all SUBSTANCE-FELT across all three scene windows; one stitch-layer informational flag from worm-canon-pedant on s02n04 'fill' verb stability (avoid drift to active-class sweep at stitch)
        # /and-write Phase 7 flat_id assignment (scene-internal walk in dramatist-shaped order; deletions left as slug-gaps; blank-numbered time-skips at flat 10, 21):
        #   s01: n01→1, n02→2, n05→3, n04→4, n06→5, n07→6, n08→7, n09→8, n10→9   (n03, n11 deleted at Phase 4)
        #   s02: n01→11, n02→12, n03→13, n06→14, n04→15, n05→16, n10→17, n07→18, n08→19, n09→20
        #   s03: n01→22, n02→23, n03→24, n04→25, n05→26, n06→27, n07→28, n08→29   (n09 deleted at Phase 4)
        pov_narrator: taylor-hebert-kl-122ac    # series.structure.pov = single → inherited from protagonist
        dramatic_shape: hinge                    # chapter 1 of 18 in tragedy; load-bearing baseline placement against which all subsequent collisions are audible; "rising" would imply tonal escalation that does not occur here (no antagonist pressure, no collision); reviewed and accepted by dramatist Phase 5
        goal: "the operating rule in its intact form, the ward it will fail to protect, and the child who will pay the price of its failure."   # audience-facing chapter purpose; bones-file header source for /and-write Phase 7
        scenes:
          - slug: b01c01s01
            chunk: |
              Taylor Hebert arrives at the corner off the Hook the way she arrives everywhere now — without announcement, without apparatus, paying copper stars for a sleeping space in a building that does not ask about prior addresses. The transaction is the method: she is not here to be known, she is here to be present, and the distinction is the entire operating rule she carried out of Gold Morning — useful without controlling, present without possessing, anonymity as the proof-of-concept that she can be in a place without threading through it. Coll the net-mender occupies the building's street-facing corner the way a fixture occupies space: not by arrangement but by accumulated duration, his range of observation exactly one street in any direction, his interest in strangers bounded by whether they can hold a needle. The collision of the scene is small and structural: King's Landing operates on vouching, and Taylor cannot afford to be vouched-for in any way that creates a claim or a debt or a name above the street level — and yet without some social surface against which to settle, a stranger alone in Flea Bottom reads as wrong in ways that accumulate. Coll resolves this by being a wall: his proximity functions as cover without arrangement, his lack of questions is not incuriosity but the Flea Bottom courtesy of not naming what you see in a neighbor's work. Taylor pays for the corner, inventories the ward at ground level — stone, tallow-smoke, the gallows calendar of feast and shortage and levy — and notes, with the deliberate attention she has been training toward, that no one here has a power that requires containing. She is paying attention to that absence. The insect-sense runs at the threshold of passive, reading walls and flagstones and the temperature of rooms through what lives in them, and she keeps it there: below deployment, below the line that would make it an act rather than a sense.
            substance_delta:
              axes_in_motion:
                - { axis: knowledge, direction: up, target_delta_magnitude: 0.2, cost_ledger_anchor: ~, notes: "immediate ward geometry established: the Hook, Coll's block, social physics of Flea Bottom vouching; 3→3.2; passive orientation layer" }
              axes_held:
                - { axis: capability, rationale: "insect-sense held passive at threshold; capability rank 3 unchanged; dormancy enacted, not just stated; the held axis IS the scene's stakes_axis" }
              density_target: "0.6-0.7"
            scene_conflict:
              protagonist_force: "Taylor establishing street-level presence without incurring debt, claim, or visibility above the block"
              opposing_force: "Flea Bottom's social physics require vouching; a stranger who settles without vouching reads as wrong and accumulates notice"
              stakes_axis: capability   # held axis (axes_held) — refusal to deploy insect-sense above passive is the load-bearing discipline; capability stays at rank 3 by choice. Bone-gate Phase 6 validates against axes_in_motion ∪ axes_held.
            bones:
              # Phase 1 scene-decomposition + Phase 2 fixer (s01n04 'faces' → 'lifts the eyes') +
              # Phase 3 dramatist (n05↔n04 cause-before-effect swap) + Phase 3 bridge n11 (yard-exit).
              # Order: n01, n02, n03, n11, n05, n04, n06, n07, n08, n09, n10.
              - slug: b01c01s01n01
                svo: "taylor-hebert-kl-122ac enters the corner-room"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.02, notes: "building threshold registered; room geometry available as first ward layer" }
                  cost_ledger_anchor: ~
              - slug: b01c01s01n02
                svo: "taylor-hebert-kl-122ac pays the building-keeper"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.03, notes: "transaction-as-settlement enacted; anonymous entry purchased; operating rule confirmed viable at this threshold" }
                  cost_ledger_anchor: ~
              # b01c01s01n03 + b01c01s01n11 deleted at Phase 4 audience trim
              # (2-of-3 vote: cape-fic-reader + dark-fantasy-reader).
              # n03 (keeper pockets copper-stars): payment-receipt echo; n02 carries the transaction sufficiently.
              # n11 (Taylor enters yard, dramatist bridge): collapses into n05 (crosses the yard) at prose level.
              # Slugs preserved in skip; no renumbering. Aggregate s01 knowledge now 0.19 (was 0.21; within 0.15-0.25 PASS band).
              - slug: b01c01s01n05
                svo: "taylor-hebert-kl-122ac crosses the yard"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.02, notes: "yard geometry traversed; block layout legible at ground level" }
                  cost_ledger_anchor: ~
              - slug: b01c01s01n04
                svo: "coll-net-mender-flea-bottom lifts the eyes"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.04, notes: "opposing-force bone — surveillance response: Coll's eye-lift registers Taylor's appearance in the open yard; block-level witness who does not name what he sees; range-of-observation one street; proximity-as-cover without arrangement visible" }
                  cost_ledger_anchor: ~
              - slug: b01c01s01n06
                svo: "coll-net-mender-flea-bottom works the net"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.02, notes: "opposing-force bone (secondary) — feigned-indifference: Coll returns to work while still watching; needle-criterion signaled; lack of questions is Flea Bottom courtesy of not naming what you see in a neighbor's work; proximity-as-cover solidified" }
                  cost_ledger_anchor: ~
              - slug: b01c01s01n07
                svo: "taylor-hebert-kl-122ac circles the block"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.04, notes: "ward perimeter established at ground level: stone, tallow-smoke, shortage-calendar rhythm; the Hook's feast-and-levy cadence legible from a single circuit" }
                  cost_ledger_anchor: ~
              - slug: b01c01s01n08
                svo: "taylor-hebert-kl-122ac drops the pack"
                substance_delta:
                  axis_moves: []                       # chatter bone — pure transition / occupation marker
                  axes_held: []
                  cost_ledger_anchor: ~
                  # chatter-rationale: physical-anchor — settling enacted; pack-down marks occupation of space without claim; stillness marker before scene-close hinge. Density-cap permits chatter at this scene position.
              - slug: b01c01s01n09
                svo: "coll-net-mender-flea-bottom speaks to taylor-hebert-kl-122ac"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.02, notes: "speech bone — minimal social surface established via needle-criterion exchange; no name given, no claim made, no vouching initiated; knowledge gain is the confirmed social physics" }
                  cost_ledger_anchor: ~
              - slug: b01c01s01n10
                svo: "taylor-hebert-kl-122ac holds the feet"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - { axis: capability, rationale: "stillness-against-pressure — licensed holds form on body part; insect-sense runs at passive threshold; capability held at rank 3 by discipline enacted, not just stated; the load-bearing dormancy bone — satisfies scene's stakes_axis: capability via axes_held" }
                  cost_ledger_anchor: ~

          - slug: b01c01s02
            chunk: |
              The working day has a rhythm Taylor can run the ledger inside of: Coll mends nets at the street corner, and she mends nets beside him, and the work is repetitive enough that the accounting-mind can run a background process without visibly stalling. What she is running in the background is Flea Bottom — not the social surface of it, which Coll mediates for her by existing beside her, but the substrate geometry that the insect-sense opens and the operating rule governs. She can read the ward through the insects in the walls: density means population, temperature means occupation, movement patterns trace the routes the smallfolk use and the gaps they avoid. She reads it. She does not deploy. The chapter's central discipline is enacted here in its clearest form — sense without instrumentalization, observation without action, the gap between capability available and capability held at bay made visible in the texture of the work. The needle moves. The awareness runs. The prohibition holds. The collision this scene is staging is the smallest possible version of the book's central event: the insect-sense could route, could track, could do any number of things it is not being asked to do, and the only thing preventing it is a rule Taylor authored and is enforcing on herself. She notes the geography she has built by the end of the day — block-level density maps, movement corridors, the location of the city watch's patrol rotation relative to the Hook — as passive observation, not as intelligence. The distinction is real to her. She enters it in the accounting as knowledge gained, cost zero, tool unused.
            substance_delta:
              axes_in_motion:
                - { axis: knowledge, direction: up, target_delta_magnitude: 0.2, cost_ledger_anchor: ~, notes: "block-level density maps, movement corridors, watch patrol rotation read passively; 3.2→3.4; ward-pattern orientation; pre-arrangement; unanchored" }
              axes_held:
                - { axis: capability, rationale: "insect-sense passive throughout; prohibition enacted against no external pressure; capability rank 3 unchanged; this scene is the discipline before it is tested" }
              density_target: "0.7-0.8"
            scene_conflict:
              protagonist_force: "Taylor reading the ward through insect-sense while holding the prohibition against deployment"
              opposing_force: "the capability is available and the ward's geometry is legible; the rule is the only thing holding the gap open"
              stakes_axis: capability   # held axis (axes_held); the refusal to move is the event; capability stays at rank 3 by choice
            bones:
              # Phase 1 scene-decomposition + Phase 2 fixer (n02 'taut' strip, n06 'through the mesh' → 'the needle crosses the mesh',
              # n09 'aside' → 'folds') + Phase 3 dramatist reorder (hand-work / ambient drift / watch-pressure grouped) +
              # Phase 3 bridge n10 (boots-strike-cobbles, watch approach signal).
              # Order: n01, n02, n03, n06, n04, n05, n10, n07, n08, n09.
              # Phase 4 audience flag (1-of-3 advisory; not auto-deleted): cape-fic-reader and dark-fantasy-reader
              # both noted the s02n01+n02 rhythm-pair as borderline-redundant, but disagreed on which half to drop.
              # ORCHESTRATOR DECISION: keep both — they establish the working-day rhythm and Taylor-beside-Coll co-presence.
              # Downstream stitcher should consider compressing or interleaving at render time if the prose reads bumpy.
              - slug: b01c01s02n01
                svo: "taylor-hebert-kl-122ac lifts the basket"
                substance_delta:
                  axis_moves: []                       # chatter bone — working-day rhythm opener
                  axes_held: []
                  cost_ledger_anchor: ~
                  # chatter-rationale: posture-act opening beat; establishes the working-day rhythm underway (avoids 'threads the needle' collision with s01n06-equivalent label)
              - slug: b01c01s02n02
                svo: "coll-net-mender-flea-bottom pulls the net"
                substance_delta:
                  axis_moves: []                       # chatter bone — co-presence rhythm anchor
                  axes_held: []
                  cost_ledger_anchor: ~
                  # chatter-rationale: rhythm-anchor; Coll's physical presence beside Taylor; social-cover-by-proximity established in s01 continues; sets the repetitive working beat
              - slug: b01c01s02n03
                svo: "taylor-hebert-kl-122ac threads the needle"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.03, notes: "first passive read: hands find the rhythm; the accounting-mind opens; ward-pattern orientation begins; pre-arrangement; unanchored" }
                  cost_ledger_anchor: ~
              - slug: b01c01s02n06
                svo: "the needle crosses the mesh"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.03, notes: "working rhythm continues; accounting-mind's background process runs against the net-work; movement corridors accumulate passively through the day's pass; pre-arrangement; unanchored" }
                  cost_ledger_anchor: ~
              - slug: b01c01s02n04
                svo: "the insects fill the block"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.05, notes: "block-level density registered passively; ambient drift at rank 3 ceiling; ward-pattern orientation — population density across the Hook; pre-arrangement; unanchored" }
                  axes_held:
                    - { axis: capability, rationale: "ambient-drift verb 'fill'; passive sense at rank 3; capability available and visible; the rule is the only thing holding it at 3; signal-002 mitigation — not active sweep" }
                  cost_ledger_anchor: ~
              - slug: b01c01s02n05
                svo: "the walls cool"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.04, notes: "temperature gradient registered passively; occupation pattern read — which walls are peopled, which are empty; movement-corridor inference begins; pre-arrangement; unanchored" }
                  axes_held:
                    - { axis: capability, rationale: "ambient-drift verb 'cool'; ward legibility in plain view; capability could route from this; rule holds it at observation only; opposing-force visible" }
                  cost_ledger_anchor: ~
              - slug: b01c01s02n10
                svo: "the boots strike the cobbles"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.01, notes: "Phase 3 bridge (transition-002) — approach registers as pre-watch-pressure cue; footfall on stone establishes watch as approaching event; gives n07 the weight of an event rather than ambient continuation" }
                  cost_ledger_anchor: ~
              - slug: b01c01s02n07
                svo: "the city-watch passes the hook"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.05, notes: "watch patrol rotation registered; spatial position of watch relative to the Hook confirmed; ward-pattern orientation — patrol geometry known; pre-arrangement; unanchored" }
                  cost_ledger_anchor: ~
              - slug: b01c01s02n08
                svo: "taylor-hebert-kl-122ac holds the eyes"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - { axis: capability, rationale: "discipline bone; capability at its ceiling, held by the rule Taylor authored; the watch passing is the pressure; the body is the instrument of the prohibition; the load-bearing dormancy beat of the scene — satisfies scene's stakes_axis: capability via axes_held" }
                  cost_ledger_anchor: ~
                  # NOTE 2026-05-21: prior shape had a second 'knowledge null/0' entry alongside capability null. Dropped under the axis-bookkeeping split — knowledge does not move and is not held by discipline at this bone (no information enters; no information is refused). The capability hold carries the bone alone.
              - slug: b01c01s02n09
                svo: "coll-net-mender-flea-bottom folds the net"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.03, notes: "end-of-day rhythm marker; working day closes; Taylor's passive register completes — block-level density maps, movement corridors, watch rotation all logged as knowledge gained, cost zero, tool unused; pre-arrangement; unanchored" }
                  cost_ledger_anchor: ~

          - slug: b01c01s03
            chunk: |
              Wren appears in Taylor's field of attention on the third or fourth day — seamstress-ward, two buildings over, eleven years old, and already running the kind of distributed social accounting that smallfolk children run in wards where reading the room is survival competency. She asks too many questions. She watches what the adults pretend not to see. Taylor's training — the pattern-reading that preceded Khepri and that Khepri enlarged and that she is attempting to suppress into something less than what it was — reads the child instrumentally before the rule can intervene: node, observation-radius, trust-network map, potential access-point. The assessment runs. The rule catches it. Taylor does not let the attention loop close — does not file Wren as a node, does not enter her into any model, marks her as a face and holds her there. The scene's collision is interior and exact: the operating rule is working exactly as intended, catching an assessment before it becomes a use, and the fact that the rule had to catch something at all is the cost the chapter closes on. Wren leaves when the light goes, recurring in the ward's geometry from this point forward without Taylor having named her as significant, and the accounting Taylor runs afterward is brief — child, present, noted, not filed — and the brevity is the tell. The chapter places Wren here, in this position, so that when the ledger finally prices her, the reader has been watching the gap between the two entries from the first page.
              # SIGNAL-002 from auditor: explicit "Khepri" naming in interior monologue is in tension with chapter chunk's "Khepri-haunted without naming Khepri" register commitment; classified SIGNAL (not HARD) because the discipline lives in chapter-chunk prose rather than project.constraints.hard_fences; routed to /and-write for bone-level smoothing
            substance_delta:
              axes_in_motion:
                - { axis: knowledge, direction: up, target_delta_magnitude: 0.1, cost_ledger_anchor: ~, notes: "Wren registered as face-not-node; ward social geometry one layer deeper; 3.4→3.5; minimal gain because Taylor deliberately refuses full assessment" }
              axes_held:
                - { axis: capability, rationale: "pattern-reading runs and is caught by the rule; capability not deployed; rank 3 unchanged; the assessment-and-catch is the proof-of-function — held axis carries the scene's structural event even though knowledge is what moves" }
              density_target: "0.7-0.9"
            scene_conflict:
              protagonist_force: "Taylor refusing to complete the instrumental assessment of Wren — holding her as a face, not a node"
              opposing_force: "Taylor's own trained pattern-reading initiates the assessment automatically; the prohibition must actively catch it"
              stakes_axis: knowledge   # in-motion axis; the constrained delta IS the load-bearing event (refusal-to-complete-assessment caps the knowledge gain). Capability-as-held is the secondary axis that proves the prohibition is functioning.
            bones:
              # Phase 1 scene-decomposition + Phase 2 fixer (s03n03 'faces' → 'lifts the eyes') +
              # Phase 3 dramatist (order unchanged for s03) + Phase 3 bridge n09 (Wren proximity-establishment).
              # Order: n01, n09, n02, n03, n04, n05, n06, n07, n08.
              - slug: b01c01s03n01
                svo: "wren-stitch-maker-flea-bottom-ward enters the street"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.02, notes: "Wren's face registers in Taylor's field — proximity initiates face-entry, below the threshold of model-entry" }
                  axes_held:
                    - { axis: capability, rationale: "assessment-pattern initiates on contact; rule catches before deployment; capability rank unchanged" }
                  cost_ledger_anchor: ~
              # b01c01s03n09 deleted at Phase 4 audience trim (2-of-3 vote: cape-fic-reader + dark-fantasy-reader).
              # Dramatist bridge n09 (Wren approaches Taylor): absorbed by the speak bone n02 that follows;
              # dark-fantasy-reader flagged sentimental-warming risk on the cost-bearer pre-pricing.
              # Slug preserved in skip; aggregate s03 knowledge unchanged at 0.10.
              - slug: b01c01s03n02
                svo: "wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.03, notes: "Wren's questions confirm her observer-radius and distributed-attention habit; Taylor receives ward-social-geometry data at face level" }
                  cost_ledger_anchor: ~
              - slug: b01c01s03n03
                svo: "taylor-hebert-kl-122ac lifts the eyes"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.01, notes: "physical orientation deepens face-recognition; proximity-dwell registers Wren's position in ward geometry at street-corner granularity" }
                  axes_held:
                    - { axis: capability, rationale: "opposing-force bone — trained pattern-reading initiates full assessment automatically on direct orientation (node-id, observation-radius, trust-network map); operating rule catches before close; capability not deployed; assessment-starting is proof-of-function, catch is rule working as intended" }
                  cost_ledger_anchor: ~
              - slug: b01c01s03n04
                svo: "taylor-hebert-kl-122ac speaks to wren-stitch-maker-flea-bottom-ward"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.02, notes: "Taylor's reply extends face-registration — Wren's approximate age, ward-affiliation (seamstress-ward, two buildings over) enter the face-layer; no model entry" }
                  cost_ledger_anchor: ~
              - slug: b01c01s03n05
                svo: "wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac"
                substance_delta:
                  axis_moves:
                    - { axis: knowledge, direction: up, magnitude: 0.02, notes: "second round of questions opens one additional layer of ward social geometry — Wren's questions map what the adults in this ward pretend not to see; implicit information about the ward's unspoken social ledger" }
                  cost_ledger_anchor: ~
              - slug: b01c01s03n06
                svo: "taylor-hebert-kl-122ac holds the eyes"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - { axis: capability, rationale: "stillness-against-pressure: eye-orientation is the pressure surface; assessment-run is caught mid-cycle by the operating rule; Taylor holds gaze-direction fixed against trained pull toward completing the node-map; rule working as intended; the hold prevents rather than produces information-entry — load-bearing held bone for the scene's structural collision" }
                  cost_ledger_anchor: ~
              - slug: b01c01s03n07
                svo: "wren-stitch-maker-flea-bottom-ward crosses the street"
                substance_delta:
                  axis_moves: []                       # chatter bone — cost-bearer-placement beat
                  axes_held: []
                  cost_ledger_anchor: ~
                  # chatter-rationale: Wren's departure; no further face-data registered; exit is the cost-bearer-placement beat — Wren leaves the scene un-named-as-significant, recurring in ward geometry from this point forward without having been filed as a node
              - slug: b01c01s03n08
                svo: "taylor-hebert-kl-122ac lifts the needle"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - { axis: capability, rationale: "closing bone; Taylor returns to physical task — assessment closed, ledger not opened, Wren not filed; brevity of return-to-task is the tell: child, present, noted, not filed; operating rule held; gap between this moment and the future ledger-pricing of Wren begins here" }
                  cost_ledger_anchor: ~
        # Prior /and-write run history (cleared at redo 2026-05-19; preserved for historical reference):
        #   - SIGNAL-003 (s01 social-physics knowledge-acquisition implicit): RESOLVED at /and-write Phase 1 — b01c01s01n03 (coll speaks to taylor) was the explicit vouching-knowledge anchor.
        #   - SIGNAL-002 (Khepri naming smoothing for s03 chunk): RESOLVED at /and-write — no bone referenced Khepri; interiority deferred to facets.
        #   - Phase 6 SIGNALS recorded on prior emission: signal-001 (identical "threads the needle" label on s01n05/s02n01), signal-002 (s02n02 upper-edge rank-3 capability), signal-003 (vouching-anchor pre-labelled).

      - slug: b01c02
        chunk: |
          Danger moves through Flea Bottom in the form of a pressed-labor sweep — city watch rounding up debtor-class smallfolk for a lord's work-levy — and Wren, too young and too visible, is in the path of it. Taylor uses insect-sense to locate and pull Wren clear of the sweep without being seen to act: the insects guide, the routing is real, but from the street it reads as a child ducking into the right alley at the right moment. The act is not control — no nervous system override, no hijack of the body — but it is deployment, and the insects move with a density and precision that at least two witnesses on the street notice as wrong. Taylor runs the accounting afterward and finds the ledger shows: capability deployed (acceptable, it was rescue), Wren safe (acceptable), two witnesses who now have a question they cannot name (cost, unpriced). The prohibition held — she did not take control — but it flexed. The chapter's weight is in the accounting scene: Taylor itemizing what happened, what category the action falls into, and whether it was inside the rule or not, and arriving at a verdict she believes and that the reader will not quite believe with her. Coll, present at the sweep's edge, sees Taylor's hand in the alley's geometry but says nothing — the Flea Bottom courtesy of not naming what you've seen in a neighbor's work.
        structure:
          scene_count: 3
        substance_delta:
          chapter_class: standard   # on-protagonist-arc; three moving axes; not a temporally-displaced retrospective coda (/and-write Phase 6 substance bone-gate fires normally)
          axes_in_motion:
            - { axis: capability, direction: up, target_delta_magnitude: 1.0, cost_ledger_anchor: ~, notes: "suppressed → first-deployment (localized, defensive); 3→4; d01 shift; first-deployment; self-directed rescue; pre-Otto-arrangement, not yet network expansion" }
            - { axis: social-tether, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-social-tether-build, notes: "anonymous → smallfolk-present; Wren + Coll layer laid; 2→2.5; d01 social-embed; direction records initial rise before net-fall" }
            - { axis: knowledge, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: ~, notes: "watch-sweep patterns + ward movement first read; 3.5→4; watch-sweep-pattern observation; pre-arrangement; unanchored" }
          density_target: "0.6-0.7"
        handoff_in:
          open_threads:
            - "Taylor's operating rule intact but not yet tested against an external ask"
            - "Wren introduced as recurring street presence; relationship not yet named"
            - "insect-sense passive; Flea Bottom ward-geography mapped to block level"
          world_state:
            - "122 AC; Flea Bottom; Taylor holds a rent corner off the Hook"
            - "Coll provides social cover by proximity; no explicit arrangement"
            - "insect-sense reads at passive: density, temperature, movement patterns below deployment threshold"
          character_state:
            - "taylor: moral-framework 3; capability 3 (dormant); position 1; social-tether 2; relational-anchor 3; moral-legibility 7; political-register 5; knowledge 3.5; agency 5"
            - "wren: present, recurring, unnamed as significant"
            - "otto: offstage"
          source_chapter: b01c01
        handoff_out:
          open_threads:
            - "two street witnesses have seen insect-density anomaly; no name attached yet but the observation exists"
            - "Wren now specifically attached to Taylor's block presence; Coll saw the alley geometry"
            - "prohibition flexed but Taylor's accounting holds it as compliant; reader knows the verdict is strained"
            - "city watch sweep pattern now mapped in Taylor's insect-read"
          world_state:
            - "122 AC; Flea Bottom; Taylor visible to her immediate block but not yet to any layer above"
            - "Coll maintains non-interpretive witness role; did not name what he saw"
            - "insect capability now at first-deployment level; covered approximately two-block radius around the Hook"
          character_state:
            - "taylor: moral-framework 3 (strained but holding); capability 4 (first deployment executed); position 1; social-tether 2.5 (Wren + Coll layer); relational-anchor 3; moral-legibility 7; political-register 5; knowledge 4; agency 5"
            - "wren: rescued; present; still unnamed as significant node in Taylor's ledger"
            - "otto: offstage"
          target_chapter: b01c03
        status: audited-r1-mechanical   # /and-facets Phase 5 — 2026-05-21; auditor 12-class scan; 2 HARD remediated (fixer cycle 1), cycle-2 re-audit HARD=0; 8 SIGNAL advisory; Phase 5b audience-gate pending
        pov_narrator: taylor-hebert-kl-122ac    # series.structure.pov = single → inherited from protagonist
        dramatic_shape: hinge                    # first-flex hinge: prohibition pivots from theoretical-intact to road-tested-strained in s01's deployment; differs from b01c01's baseline-placement hinge (no antagonist pressure, no collision there); dramatist Phase 5 ACCEPT confirmed the two hinge functions are structurally distinguishable.
        goal: "the prohibition in its first real test — deployed against a genuine threat, technically held, and already bent enough that the accounting cannot close cleanly."   # audience-facing chapter purpose; bones-file header source for /and-write Phase 7
        bones_file: theater/bones/b01-c02.md
        bones_count: 27   # 10 (s01) + 9 (s02) + 8 (s03); s01n01 deleted at Phase 4 (2-of-3 audience vote); Phase 3 additions s01n11 + s02n09 + s03n08 included
        substance_bone_gate_verdict: PASS
        substance_delta_measured:
          axes_moved:
            capability:    { ticks: 4,  rank_delta: 0.4, target: 1.0, gap: -0.6 }  # within ±1; hinge-pivot bone @5 carries 3 ticks; threshold-crossing @4 carries 1 tick
            social-tether: { ticks: 5,  rank_delta: 0.5, target: 0.5, gap:  0.0 }  # chapter aggregate exact-match (s01 0.1 + s02 0.4 + s03 0.1 = 0.6 with addition; effective 0.5 vs target 0.5)
            knowledge:     { ticks: 13, rank_delta: 1.3, target: 0.5, gap: +0.8 }  # within ±1; sweep-pattern observation cluster in s01 + categorical-structural cluster in s03; type-distinction preserved per worm-canon-pedant TASTE-FLAG
          axes_held:
            capability:      { scenes: [s02, s03], witnessed_at_bones: [13, 18, 28] }   # @13 coll proxy-hold (SIGNAL fragility — Phase 6 auditor); @18 taylor threads needle; @28 taylor holds hand
            moral-framework: { scenes: [s03],      witnessed_at_bones: [28] }            # @28 dual-discipline body-part hold
          density_measured: { s01: 0.78, s02: 0.75, s03: 0.65 }   # all scenes within their target bands
          felt_verdict: PASS   # audience 9-of-9 SUBSTANCE-FELT across all three scenes
        scenes:
          - slug: b01c02s01
            chunk: |
              The pressed-labor sweep comes through Flea Bottom the way all watch-mobilizations come: percussion before visibility — boots on stone in the wrong cadence, the street's social noise dropping a register as people read the pressure-front and begin finding reasons to be elsewhere. Taylor reads it first through the insects, which register the watch's heat-signature moving in organized columns down the Hook and the adjacent laneways, and then through the street itself, which reads the same way but slower: a water-carrier stepping back into a doorway, a net-mender's needles going still, the particular geometry of smallfolk bodies reorienting away from something. Wren is in the path of it. Taylor knows this before she can see the child — the insect-feed has the ward at sufficient density that Wren's specific heat and motion signature are legible at thirty yards, which is itself a fact Taylor registers and files as cost before she acts. The deployment is not a control act. She is clear on this while it is happening and after. The insects do not route through Wren's nervous system, do not override her decisions, do not hijack her body in any way the prohibition covers. What they do is close off the wrong turns — the laneways that feed into the sweep's path — and leave the right one open: a side-alley that Wren's own feet can find if they are looking for exit, and that a child with good distributed-attention habits can read as available. Wren finds the alley. The insects move at a density and precision that two witnesses standing at the lane's mouth will register as wrong — not as insects, necessarily, but as the air having a quality it did not have a moment ago, as a space that seemed closed reading as open — and Taylor, standing at the corner where Coll is still at his net, does not look at the alley. The sweep passes. Wren is not in it.
            substance_delta:
              axes_in_motion:
                - { axis: capability, direction: up, target_delta_magnitude: 1.0, cost_ledger_anchor: ~, notes: "suppressed-baseline → first-deployment; rank 3→4; the act is localized and defensive (non-control routing); pre-Otto, unanchored to ledger trade; the full chapter capability move lands here" }
                - { axis: social-tether, direction: up, target_delta_magnitude: 0.1, cost_ledger_anchor: cl-social-tether-build, notes: "rescue creates the seed attachment — Wren is now a known variable in Taylor's deployment, not only a face on the street; social-tether rank 2→2.1; Wren-layer seed" }
                - { axis: knowledge, direction: up, target_delta_magnitude: 0.2, cost_ledger_anchor: ~, notes: "watch-sweep approach pattern first read: column formation, heat-signature advance, Hook approach route, press-levy timing; 3.5→3.7; sweep-pattern-observation; pre-arrangement; unanchored" }
              density_target: "0.7-0.8"
            scene_conflict:
              protagonist_force: "Taylor routing Wren clear of the sweep without physical contact, name-call, or any act that reads as intervention from street level"
              opposing_force: "the insect deployment violates the spirit-threshold of the prohibition even as it observes the letter; the capability is now unambiguously deployed, not sensed"
              stakes_axis: capability   # in-motion axis; the first rank-change of this axis in the book; the prohibition flexes here

          - slug: b01c02s02
            chunk: |
              The sweep clears and the street returns to itself in the particular way of Flea Bottom streets that have been through a watch-press: carefully, with the deliberate amnesia of people who did not see anything and know that nothing was seen. Coll is already working the net again when Taylor reaches the corner, and his eyes come up once to find her face and then go back down, and he does not say the thing his face said. This is the Flea Bottom courtesy. Wren, from the far side of the alley mouth, is watching Taylor the way Taylor watched Wren in the earlier days: too directly, too steadily, with the look of someone running an accounting. Taylor notes this and does not look back. The two witnesses at the lane's mouth are already moving on — they are not standing still and pointing; they are doing the thing witnesses do in Flea Bottom, which is to continue functioning while carrying a question they cannot name. Taylor reads them through the insects: heart-rate above settled, attention still pulled toward the alley mouth, neither of them has the vocabulary for what they saw but both of them have a word-shaped gap where the vocabulary would go. Coll's geometry-sight — his reading of the alley's changed angles, the lane's traffic-weighting in the moments of the sweep, the way a space closes and opens — is a different kind of knowing; he grew up in wards where the geography is always communicating and the correct response is to not have needed to notice. He will not name what he saw. He is already demonstrating the not-naming. Wren, however, is specifically attached now, in a way that has a different shape from her prior appearing-and-asking: she is in Taylor's quadrant, watching, because a thing has been done for her and she has run the accounting and found the source.
            substance_delta:
              axes_in_motion:
                - { axis: social-tether, direction: up, target_delta_magnitude: 0.3, cost_ledger_anchor: cl-social-tether-build, notes: "Wren-attached + Coll-witness layer crystallizes; rank 2.1→2.4; Coll's non-naming confirms his function as social-cover anchor; Wren's specific attachment is a new social-tether node; cl-social-tether-build anchors the Wren-layer build" }
                - { axis: knowledge, direction: up, target_delta_magnitude: 0.2, cost_ledger_anchor: ~, notes: "witness-residue read: heart-rate above settled, attention-pull toward alley, vocabulary-gap registered; Coll's geometry-sight read at a distance; Wren's attachment behavior mapped; 3.7→3.9; witness-pattern observation; pre-arrangement; unanchored" }
              axes_held:
                - { axis: capability, rationale: "capability held at rank 4 post-deployment; no further insects moved; the new baseline is real and is not extended; Taylor is accounting for what happened, not continuing to act; held-at-new-rank is the discipline" }
              density_target: "0.7-0.8"
            scene_conflict:
              protagonist_force: "Taylor reading the aftermath without naming it — registering witnesses, Coll's silence, Wren's attachment, without entering any of it into the ledger as cost"
              opposing_force: "the street is already organizing itself around what happened; two witnesses have a question they cannot name; Wren has run her own accounting; the costs are accruing whether or not Taylor enters them"
              stakes_axis: social-tether   # in-motion axis; the Wren + Coll layer crystallizing is the scene's load-bearing movement

          - slug: b01c02s03
            chunk: |
              The accounting runs that night. Taylor opens the ledger with the precision she has been trained toward and the honesty she has been maintaining since Gold Morning: line by line, category by category, the way you do it when the categories are the atonement and you cannot afford to let any entry go unchallenged. The action was: insect deployment, localized, defensive, non-control. The outcome was: Wren routed clear, sweep averted for one child, two witnesses with a question-shaped gap they cannot name. The classification question is whether deployment-without-control falls inside or outside the prohibition. Taylor examines this. She looks at it from the outside, from the inside, from the edge cases: is routing-without-override a meaningful distinction from control, or is it the same thing with a smaller footprint? She arrives at a verdict: it is a meaningful distinction. The prohibition is no nervous system override, no hijack of the body — it is not a prohibition against deployment, it is a prohibition against one specific mode of deployment. The insects guided; Wren's own feet chose. The verdict is: compliant, defensible, cost-acknowledged. Taylor enters the cost line — two unpriced witnesses — and notes that the accounting for Wren herself is incomplete but that the incompleteness is not a ledger failure, it is the appropriate result of treating Wren as a person and not a variable. She believes this. The scene makes legible, without editorializing, the exact shape of a rationalization that is also correct: the distinction Taylor is drawing is real, the witnesses are genuinely unpriced, and the verdict she has reached is one she can defend to herself. The reader has watched the deployment. The reader knows what the ledger is not entering.
            substance_delta:
              axes_in_motion:
                - { axis: social-tether, direction: up, target_delta_magnitude: 0.1, cost_ledger_anchor: cl-social-tether-build, notes: "Wren entered into the ledger's negative space as 'incompleteness is the appropriate result of treating her as a person, not a variable' — the methodological-decision entry IS a social-tether crystallization (Wren is now a node Taylor knows she is not pricing); Coll's non-naming logged as social-fabric fact; rank 2.4→2.5; final social-tether seat for the chapter (addresses Phase 5 auditor flag-001: event-specific anchor named)" }
                - { axis: knowledge, direction: up, target_delta_magnitude: 0.1, cost_ledger_anchor: ~, notes: "categorical knowledge: the deployment-without-control distinction named and examined; the distinction's architectural meaning — what falls inside the prohibition and what does not — registered as structural knowledge; 3.9→4.0; categorical-accounting; pre-arrangement; unanchored" }
              axes_held:
                - { axis: capability, rationale: "capability held at rank 4; the accounting scene is interior and static; no deployment; no insect-movement; the new baseline sits at 4, held in place by an accounting that has resolved around it rather than extending it — the discipline after the flex, not the flex itself" }
                - { axis: moral-framework, rationale: "moral-framework held at rank 3 (strained but not breached); the verdict Taylor reaches is that the prohibition held; the reader does not quite believe the verdict with her; the axis is not moved here — the strain is visible and real but the breach is not yet; holding at 3 is the scene's primary structural event alongside the knowledge move" }
              density_target: "0.6-0.7"
              # cl-unpriced-cost-bearer anchor note: the accounting scene surfaces the seed moment (two witnesses unpriced;
              # Wren's attachment not entered as a variable) that this ledger entry will later anchor at b01c03+ when
              # Taylor explicitly removes Wren from the prevention model. Per Phase 3 cost-ledger refinement (G4): no
              # refinement at b01c02 — no trade is closed here. cl-unpriced-cost-bearer.anchor.chapter remains as
              # authored at series level (book b01; chapter unset; finest-grained anchor = b01).
            scene_conflict:
              protagonist_force: "Taylor constructing a verdict that holds the prohibition intact — the deployment was compliant, the distinction is real, the accounting is honest"
              opposing_force: "the ledger cannot close cleanly because the witness-costs are unpriced and Wren's attachment is entered as a methodological decision rather than a relationship; the verdict is structurally load-bearing but the reader can read the seam"
              stakes_axis: knowledge   # in-motion axis; the categorical-structural knowledge gain IS the scene's event — Taylor naming what category the action falls into
        # Phase 5 review (2026-05-21):
        #   audience: PASS 3-of-3 (cape-fic-reader + dark-fantasy-reader + worm-canon-pedant; all SUBSTANCE-FELT)
        #   dramatist: ACCEPT — clean rise-peak-fall (event / reverberation / accounting); hinge-function distinct from b01c01's baseline-hinge; load-bearing pivot for /and-write Phase 6 named as "the insect deployment in s01 — capability crosses from dormant to deployed in a single localized rescue act that is technically compliant with the prohibition and already costs more than Taylor's accounting will admit"
        #   auditor: ACCEPT (zero faults; flag-001 on s03 social-tether note addressed inline pre-persist)
        # Sum-roll-up (exact): capability s01 1.0 = chapter 1.0; social-tether s01 0.1 + s02 0.3 + s03 0.1 = 0.5 = chapter 0.5; knowledge s01 0.2 + s02 0.2 + s03 0.1 = 0.5 = chapter 0.5.
        # Audience TASTE-FLAGs (forward to bone-gate + future-chapter monitoring):
        #   cape-fic-reader: witness-residue (two unpriced witnesses from s01) must remain unresolved forward; a future chapter that prices them without consequence-friction is cleanup-without-consequence.
        #   dark-fantasy-reader: Coll-as-loyal-sidekick-function is a hostile read; future scenes must preserve Coll-as-person-who-already-did-the-accounting. Witness vocabulary-gap should remain dangerous, not resolve into incuriosity.
        #   worm-canon-pedant: knowledge-type distinction (observational sweep-pattern → categorical structural knowledge in s03) flagged for bone-gate attention; the jump-type must be preserved in interior-scene bones, not collapsed into homogeneous-knowledge.
        # /and-write 5-pass + bone-gate review (2026-05-21):
        #   Phase 2 constraint audit: 5 faults (4 FAULT-FORM + 1 FAULT-BONE-DELTA-MALFORMED) repaired by fixer; sub-rank-tick scale ruling (1 mag = 0.1 rank) persisted.
        #   Phase 3 dramatist: ACCEPT (order unchanged); 3 missing-transition additions authored (s01n11 faces-the-alley-mouth threshold-crossing; s02n09 faces-the-alley-mouth attentional-shift; s03n08 sets-the-pen pressure-arrives).
        #   Phase 4 audience trim: 3-of-3 ACCEPT; s01n01 (the boots strike the cobbles) auto-deleted on 2-of-3 vote (dark-fantasy + worm-canon-pedant — wrong-sensor-priority / canon-register).
        #   Phase 5 continuity: CONTINUITY-OK; zero faults; two advisory flags (singular near-witness vs chunk-plural; insect object-as-subject convention from c01).
        #   Phase 6 bone-gate auditor: PASS; 0 HARD; 1 SIGNAL (s02n02 proxy-hold — capability-held satisfied independently by s02n06 @18 taylor threads the needle).
        #   Phase 6 bone-gate audience: 9-of-9 SUBSTANCE-FELT across all 3 scenes × 3 personas (coverage discipline A9 verified).
        # /and-write Phase 6 audience TASTE-FLAGs (forward to /and-facets + future-chapter monitoring):
        #   cape-fic-reader: cost-register at s01 is double-anchored by witness residue (@8) + held-feet (@9); cleared SUBSTANCE-SUSPECT-cheap-gain-capability. The double-anchoring pattern is the surface to preserve at facet-authoring.
        #   dark-fantasy-reader: Wren-as-future-cost-bearer crystallization at @15 lands as world-building consequence; preserve at facet-authoring; do NOT facet-skin the cost-bearer load.
        #   worm-canon-pedant: pen-set bone @25 carries the s03 sequence past SUBSTANCE-SUSPECT-cheap-gain-knowledge by making the ledger gap a specific recognition before the held-hand discipline. Facet-authoring must preserve the moral-framework strain as a real impulse-resisted, not a technicality.
        #   coverage TASTE-FLAGs from Phase 4 trim still forward: SVO surface collision @4 vs @14 "faces the alley-mouth" needs distinct facet treatment; insect-routing precision at @5 must not drift toward directed-individual-agency override in stitch.

      - slug: b01c03
        chunk: |
          Wren attaches. This is the fact Taylor cannot enter cleanly into the ledger: the seamstress-ward from two buildings over starts appearing in Taylor's corner of the ward with the frequency and comfort of someone who has decided the attachment is acceptable and has not asked if that's permitted. Taylor does not tell her to stop. She runs the accounting on that choice — the prevention model, the risk scenario, the acceptable-outcome framework — and when she runs the model with Wren as a variable, Wren keeps appearing in the output in places that require a calculation she cannot complete without knowing what outcome she would accept for Wren. She removes Wren from the model. She tells herself this is the atonement working: she is treating Wren as a person, not as a variable. The crack is that she notices the removal — registers that she has deliberately excluded a node from the prevention architecture and that the exclusion is not neutral, it is a choice with downstream consequences she is refusing to calculate. The chapter is interior: Taylor and the accounting, Wren's presence as the thing that makes the accounting stall, and the first time the ledger produces an entry she does not enter. It is not an emotional chapter by Taylor's register — she does not call it caring; she calls it a methodological decision. The reader knows what she has done.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - { axis: relational-anchor-status, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-unpriced-cost-bearer, notes: "un-priced → named-but-still-kept-outside-ledger; 3→2.5; d02 shift" }
            - { axis: moral-legibility-to-self, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-unpriced-cost-bearer, notes: "atoning-and-aware → atoning-with-first-crack; 7→6.5; d02 shift; crack is noticing the removal" }
          density_target: "0.6-0.7"
        handoff_in:
          open_threads:
            - "two street witnesses have seen insect-density anomaly; no name attached yet but the observation exists"
            - "Wren now specifically attached to Taylor's block presence; Coll saw the alley geometry"
            - "prohibition flexed but Taylor's accounting holds it as compliant; reader knows the verdict is strained"
            - "city watch sweep pattern now mapped in Taylor's insect-read"
          world_state:
            - "122 AC; Flea Bottom; Taylor visible to her immediate block but not yet to any layer above"
            - "Coll maintains non-interpretive witness role; did not name what he saw"
            - "insect capability now at first-deployment level; covered approximately two-block radius around the Hook"
          character_state:
            - "taylor: moral-framework 3 (strained but holding); capability 4; position 1; social-tether 2.5; relational-anchor 3; moral-legibility 7; political-register 5; knowledge 4; agency 5"
            - "wren: rescued; present; still unnamed as significant node in Taylor's ledger"
            - "otto: offstage"
          source_chapter: b01c02
        handoff_out:
          open_threads:
            - "Wren is now a named attachment — Taylor has run the model and removed her; this is the first ledger gap"
            - "two street witnesses still unresolved; their observation floats without a name above it"
            - "prohibition still holding but first-crack registered in Taylor's self-accounting"
          world_state:
            - "122 AC; Flea Bottom; Taylor's block presence solidifying; Wren appears daily"
            - "insect-read still passive-to-localized-defensive; no systematic coverage beyond immediate ward"
          character_state:
            - "taylor: moral-framework 3; capability 4; position 1; social-tether 2.5; relational-anchor 2.5 (Wren named but outside ledger); moral-legibility 6.5 (first crack: noticed the removal); political-register 5; knowledge 4; agency 5"
            - "wren: attached; not named as variable in Taylor's model; Taylor knows she has done this"
            - "otto: offstage"
          target_chapter: b01c04
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c04
        chunk: |
          Otto Hightower finds Taylor before Taylor knows she has been findable. The witnesses from the sweep — one of them a smallfolk-layer informant in the Green-faction network — carried the insect-density anomaly upward through a chain of three relays, and Otto has a picture: a foreign woman with some variety of insect-witchery operating in Flea Bottom, pattern-reading capability, no known patron, no name on record. He does not send an intermediary. He appears himself, in a street-merchant's plain wool, and the conversation is direct. He names the function he needs: court-layer intelligence that his network cannot reach from above. He names the exchange he is offering. And he names Sera Hightower — her position in the succession calculus, the threat-shape as he reads it, the probability distribution on her survival without an inside adjustment. He does not ask Taylor to accept. He names the situation and leaves the calculation to her. Taylor refuses. She refuses clearly and without hesitation: she names the prohibition — atonement-via-refusal-of-control, the operating rule that does not bend because bending it is what made Gold Morning — and Otto receives the refusal without pressure. He nods, adjusts his posture as though making a note, and leaves. The chapter's dramatic weight is the refusal: Taylor articulating the prohibition in full for the first time to someone who has reason to hear it, and the refusal holding. The reader watches Otto not press and understands that he has learned something from the refusal — not that she cannot be moved, but where the threshold is. Taylor runs the accounting afterward and files the encounter as: prohibition held; function declined; position unchanged. That evening, Taylor's insect-feed registers a Green-faction courtier moving through the Flea Bottom ward with the particular quality of someone mapping coverage rather than traversing it — a systematic sweep-pattern, not transit. Otto's apparatus is not paused. It is calibrating. The refusal holds through this too. But the apparatus is visibly present, and Sera Hightower's survival picture — the information Otto left in the room — sits in Taylor's model like an entry not yet closed. The chapter also begins the court-knowledge intake: Taylor, to track whether Otto will resurface, begins reading the Flea Bottom political layer more systematically, which is the first step toward the surveillance architecture.
          # d03 capability sub-shift "systematic-reading-begun" is absorbed within c02's already-claimed +1.0 (continuous deployment expansion); no separate magnitude needed here.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - { axis: position, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-otto-trade, notes: "anonymous → known-to-one-agent-outside-Flea-Bottom; 1→1.5; d03 first beat (refusal); identification-as-asset; pre-acceptance position-visibility shift through Otto recognizing Taylor's capability" }
            - { axis: knowledge, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-intelligence-arrangement, notes: "Otto identified; Green-faction structure begins mapping; Sera Hightower's threat-shape named by Otto in meeting; 4→4.5; systematic reading begun" }
          density_target: "0.6-0.7"
        handoff_in:
          open_threads:
            - "Wren is now a named attachment — Taylor has run the model and removed her; this is the first ledger gap"
            - "two street witnesses still unresolved; their observation floats without a name above it"
            - "prohibition still holding but first-crack registered in Taylor's self-accounting"
          world_state:
            - "122 AC; Flea Bottom; Taylor's block presence solidifying; Wren appears daily"
            - "insect-read still passive-to-localized-defensive; no systematic coverage beyond immediate ward"
          character_state:
            - "taylor: moral-framework 3; capability 4; position 1; social-tether 2.5; relational-anchor 2.5; moral-legibility 6.5; political-register 5; knowledge 4; agency 5"
            - "wren: attached; not named as variable in Taylor's model"
            - "otto: offstage"
          source_chapter: b01c03
        handoff_out:
          open_threads:
            - "Otto's offer declined but his presence means Taylor is now a known quantity to one court-adjacent layer"
            - "Otto named Sera Hightower in the meeting: her succession-calculus position, the threat-shape, the probability distribution; this information is in Taylor's model, unresolved"
            - "Otto's apparatus is not paused: a courtier swept the ward the same evening; the apparatus is calibrating"
            - "Taylor beginning systematic Flea Bottom political-layer reading to track whether Otto resurfaces"
            - "Wren's ledger-exclusion and the first crack in self-accounting both unresolved"
          world_state:
            - "122 AC; Taylor known to Otto's network; her Flea Bottom position now carries court-layer visibility (upward only)"
            - "insect-read shifting from defensive-localized toward systematic; no formal coverage yet"
            - "Otto's apparatus visibly present and moving in the ward even after the refusal"
          character_state:
            - "taylor: moral-framework 3 (prohibition stated and held); capability 4; position 1.5 (known to one court-adjacent agent); social-tether 2.5; relational-anchor 2.5; moral-legibility 6.5; political-register 5; knowledge 4.5 (Otto identified; Green-faction map begun; Sera Hightower's threat-shape received); agency 5"
            - "wren: attached; daily presence"
            - "otto: active; has heard the refusal; has what he needed from it; apparatus calibrating"
          target_chapter: b01c05
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c05
        chunk: |
          The calculation does what Otto did not: it returns a result that destroys the refusal. Taylor runs the prevention model with the information she has now assembled — the court-tier picture of Sera Hightower's position that Otto named in their meeting, supplemented by what Taylor's systematic ward-layer reading in the days since has filled in: rumor-pickup at the market level, the movements of Green-faction household staff through Flea Bottom, the particular patterns of courier-transit that confirm the succession angle Otto named is real. The Sera Hightower probability model is not conjecture. It is built from what Otto provided and from what Taylor's own reading has verified. The probability distribution on Sera's survival without an inside adjustment is unfavorable. The downstream consequences of that particular loss for the Green-faction stability that is the only thing between the Dance and Flea Bottom burning are not ambiguous. The numbers are not ambiguous. The prohibition is the only item in the model that blocks the acceptable outcome, and blocking the acceptable outcome means Wren dies in the violence Taylor could have prevented. Taylor does not decide quickly. She holds the refusal through one full iteration, through two. The prohibition holds long enough that the second answer is a choice — she can see both answers clearly, she has not been coerced, the door is still open. She accepts on the second answer. She contacts Otto's channel through a Flea Bottom relay and names her terms: she will route the intelligence his faction cannot reach in exchange for his quiet shielding of Sera Hightower in the succession calculus. The first trade. The chapter closes on Taylor running the accounting of the decision — every line entered, every cost acknowledged, the ledger reading as she believed it should — and the reader can see the auditable mistake: the prohibition named, the prohibition held through one answer, the prohibition crossed on the second. She crossed it. She chose to.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - { axis: moral-framework, direction: down, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-otto-trade, notes: "refusal-of-control → first-sanctioned-exception; 3→2; d03 acceptance beat; the prohibition crossed with full accounting" }
            - { axis: position, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-otto-trade, notes: "known-to-one-agent → known-quantity-to-one-court-layer; 1.5→2; d03 position shift on acceptance; acceptance formalizes asset-identification; position visibility crystallizes through the first trade" }
            - { axis: agency, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-otto-trade, notes: "self-directed → first-commitment-to-arrangement; 5→4.5; cl-otto-trade gain-agency -1 begins here" }
          density_target: "0.7-0.8"
        handoff_in:
          open_threads:
            - "Otto's offer declined but his presence means Taylor is now a known quantity to one court-adjacent layer"
            - "Otto named Sera Hightower in the meeting: her succession-calculus position, the threat-shape, the probability distribution; this information is in Taylor's model, unresolved"
            - "Otto's apparatus is not paused: a courtier swept the ward the same evening; the apparatus is calibrating"
            - "Taylor beginning systematic Flea Bottom political-layer reading to track whether Otto resurfaces"
            - "Wren's ledger-exclusion and the first crack in self-accounting both unresolved"
          world_state:
            - "122 AC; Taylor known to Otto's network; her Flea Bottom position now carries court-layer visibility (upward only)"
            - "insect-read shifting from defensive-localized toward systematic; no formal coverage yet"
            - "Otto's apparatus visibly present and moving in the ward even after the refusal"
          character_state:
            - "taylor: moral-framework 3 (prohibition stated and held); capability 4; position 1.5; social-tether 2.5; relational-anchor 2.5; moral-legibility 6.5; political-register 5; knowledge 4.5; agency 5"
            - "wren: attached; daily presence"
            - "otto: active; has heard the refusal; apparatus calibrating"
          source_chapter: b01c04
        handoff_out:
          open_threads:
            - "first trade executed: Taylor is now Otto's intelligence asset; the arrangement is live"
            - "prohibition crossed and accounted for; Taylor's ledger shows the crossing as a line-item, not an erasure"
            - "Sera Hightower's protection is now a term of the arrangement; Taylor has not met her"
            - "Wren's ledger-exclusion still unresolved and now more charged: the trade was partly for Wren's survival"
          world_state:
            - "122 AC; Taylor now formally (if unofficially) part of the Green-faction intelligence circuit"
            - "Sera Hightower under Otto's quiet protection as an explicit arrangement-term"
            - "insect-read beginning to systematize; coverage expanding beyond the immediate Hook area"
          character_state:
            - "taylor: moral-framework 2 (first-sanctioned-exception; prohibition crossed on second answer); capability 4; position 2 (known-quantity-to-one-court-layer); social-tether 2.5; relational-anchor 2.5; moral-legibility 6.5; political-register 5; knowledge 4.5; agency 4.5 (first-commitment-to-arrangement)"
            - "wren: attached; unknowingly the downstream justification for the first trade"
            - "otto: arrangement live; quiet protection of Sera Hightower in effect"
            - "sera-hightower: protected; does not know Taylor exists"
          target_chapter: b01c06
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c06
        chunk: |
          To sustain the intelligence deliveries Otto's arrangement requires, Taylor builds the insect network outward. It is not a decision in a single moment; it accumulates across the chapter in a series of operational choices, each of which is individually defensible. The network needs ground-level sourcing Otto cannot obtain any other way — that sourcing requires coverage across Flea Bottom and the adjacent wards, which requires threading the insects through living quarters and work-yards where people move without knowing they are being observed. Taylor watches bodies and routes information derived from those observations. The sin — and she knows it is a sin, she runs the accounting, the accounting names it — is surveillance and unconsented instrumentalization of movement patterns, not override. She does not possess anyone. She does not redirect anyone. She observes. The distinction is real and matters to her. The chapter holds the distinction under examination through three scenes: the first network expansion (small, defensible), the first information delivery that required reading a specific person's movements (larger, rationalized), and the third scene in which Wren's block is inside the coverage perimeter and Taylor does not flag it to herself as a problem. The Khepri-rhyming architecture is under construction. Taylor has not called it that. She is reading each expansion against the prohibition and finding each one compliant. Each finding is correct by the criterion she is applying. The criterion is the problem.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - { axis: capability, direction: up, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-network-position, notes: "localized-deployment → Khepri-rhyming-surveillance-architecture; 4→5; d04 shift" }
            - { axis: social-tether, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-social-tether-build, notes: "smallfolk-embedded → load-bearing-in-Otto's-architecture begins; 2.5→3; d04 tether becoming trap" }
            - { axis: knowledge, direction: up, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-intelligence-arrangement, notes: "one-faction structure + Flea Bottom pipeline mapped; 4.5→5.5; d04 coverage operational" }
            - { axis: agency, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-network-position, notes: "network dependency begins; 4.5→4; cl-network-position: capability +1 costs agency -1" }
          density_target: "0.6-0.7"
        handoff_in:
          open_threads:
            - "first trade executed: Taylor is now Otto's intelligence asset; the arrangement is live"
            - "prohibition crossed and accounted for; Taylor's ledger shows the crossing as a line-item, not an erasure"
            - "Sera Hightower's protection is now a term of the arrangement; Taylor has not met her"
            - "Wren's ledger-exclusion still unresolved and now more charged: the trade was partly for Wren's survival"
          world_state:
            - "122 AC; Taylor now formally (if unofficially) part of the Green-faction intelligence circuit"
            - "Sera Hightower under Otto's quiet protection as an explicit arrangement-term"
            - "insect-read beginning to systematize; coverage expanding beyond the immediate Hook area"
          character_state:
            - "taylor: moral-framework 2; capability 4; position 2; social-tether 2.5; relational-anchor 2.5; moral-legibility 6.5; political-register 5; knowledge 4.5; agency 4.5"
            - "wren: attached; unknowingly the downstream justification for the first trade"
            - "otto: arrangement live"
            - "sera-hightower: protected; offstage"
          source_chapter: b01c05
        handoff_out:
          open_threads:
            - "Khepri-rhyming surveillance architecture now under construction; Taylor finds each expansion compliant by her criterion"
            - "Wren's block is inside the coverage perimeter; Taylor has not flagged this"
            - "first intelligence deliveries made; Otto's apparatus has received and acted on them"
            - "network is becoming load-bearing for Otto's factional picture"
          world_state:
            - "122 AC; Taylor's insect network covers Flea Bottom and adjacent wards; systematic, operational"
            - "Otto's Green-faction intelligence picture has a Flea Bottom ground layer it did not have before"
            - "Sera Hightower's protection holding per arrangement-term"
          character_state:
            - "taylor: moral-framework 2; capability 5 (Khepri-rhyming architecture operational); position 2; social-tether 3 (load-bearing begins); relational-anchor 2.5; moral-legibility 6.5; political-register 5; knowledge 5.5 (one faction + Flea Bottom pipeline mapped); agency 4 (network dependency begun)"
            - "wren: inside coverage perimeter; not flagged; not entered in ledger"
            - "otto: intelligence deliveries received; architecture load-bearing for Green-faction picture"
          target_chapter: b01c07
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c07
        chunk: |
          Intelligence delivery requires court-layer surveillance, and court-layer surveillance requires Taylor to watch. She threads the insects through Red Keep approaches and the courier-corridors feeding Maegor's Holdfast, reading the political feed at close range: what the Green faction's inner circle does with a morning, what the Small Council adjusts for in its phrasing, what the household consumes in a day. The data is not abstract. The insects bring back warmth and movement and the particular quality of attention that comes through a stone wall when a room is occupied by people who have never had to calculate whether they will eat. Taylor has not had contempt for the Targaryen court — her register has been neutral-instrumentally-observant, the court a system to be read for pressure points. What arrives in this chapter is not contempt yet; it is the color the data has. The resentment is pre-verbal, a quality of attention, an accumulation of observed moments that does not yet have language — yet. The chapter is structured as three intelligence-gathering passes, each one deeper into the court-layer feed, each one delivering more specific observation of what the elite does with the power Taylor's intelligence is helping consolidate. Gylda, the water-carrier, appears at the chapter's close — not interpreting, not naming, just present in Taylor's street view as a figure who moves through more of Flea Bottom than Taylor does and sees things from angles the insects miss.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - { axis: political-register-toward-elite, direction: up, target_delta_magnitude: 1.0, cost_ledger_anchor: ~, notes: "neutral-instrumentally-observant → readable-resentment; 5→6; d05 shift; consequence-axis, observation-driven" }
            - { axis: knowledge, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-intelligence-arrangement, notes: "court-layer feed operational; Holdfast + Small Council read at close range; 5.5→6" }
          density_target: "0.6-0.7"
        handoff_in:
          open_threads:
            - "Khepri-rhyming surveillance architecture now under construction; Taylor finds each expansion compliant by her criterion"
            - "Wren's block is inside the coverage perimeter; Taylor has not flagged this"
            - "first intelligence deliveries made; Otto's apparatus has received and acted on them"
            - "network is becoming load-bearing for Otto's factional picture"
          world_state:
            - "122 AC; Taylor's insect network covers Flea Bottom and adjacent wards; systematic, operational"
            - "Otto's Green-faction intelligence picture has a Flea Bottom ground layer it did not have before"
            - "Sera Hightower's protection holding per arrangement-term"
          character_state:
            - "taylor: moral-framework 2; capability 5; position 2; social-tether 3; relational-anchor 2.5; moral-legibility 6.5; political-register 5; knowledge 5.5; agency 4"
            - "wren: inside coverage perimeter; not flagged"
            - "otto: deliveries received; architecture load-bearing"
          source_chapter: b01c06
        handoff_out:
          open_threads:
            - "readable-resentment accumulating; not yet named; the color of the court-layer data"
            - "Gylda introduced as peripheral figure with broader street-range than Taylor's insects"
            - "Wren's block inside coverage; still not flagged"
            - "intelligence deliveries continuing; court-layer picture deepening"
          world_state:
            - "122 AC; Taylor monitoring Red Keep approaches and Maegor's Holdfast courier-corridors"
            - "Green-faction intelligence picture has full Flea Bottom ground layer; Taylor is load-bearing"
            - "Sera Hightower's protection holding"
          character_state:
            - "taylor: moral-framework 2; capability 5; position 2; social-tether 3; relational-anchor 2.5; moral-legibility 6.5; political-register 6 (readable-resentment); knowledge 6 (Holdfast + Small Council at close range); agency 4"
            - "wren: inside coverage; daily presence"
            - "gylda: introduced; non-interpretive; peripheral"
            - "otto: arrangement operational"
          target_chapter: b01c08
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c08
        chunk: |
          The network now covers Wren's block. Taylor has been choosing which trades to rationalize by asking whether they keep the network intact — a criterion that has displaced asking whether they are inside the prohibition. The displacement has been gradual enough that Taylor has not named it. This chapter names it: Taylor realizes, in an accounting session reviewing a specific intelligence delivery that required reading movement patterns in Wren's immediate block, that she rationalized the delivery's legitimacy by checking network-integrity rather than prohibition-compliance. The two criteria would have aligned if the delivery had been marginal; for this delivery, they do not. She runs the accounting again using the correct criterion and arrives at: she surveilled Wren's block, derived information from Wren's neighbors' movements, and delivered it to Otto without knowing whether it would harm anyone in that block. She files the revised accounting. She does not revise the delivery. She tells herself the network is still inside the prohibition because no one's nervous system was taken over. She is rationalizing each trade. The chapter also shows Wren more fully — the seamstress work, the questions Wren asks about the stitching and about the ward in the same register, the habit of observation Taylor has begun unconsciously noting. Taylor does not enter any of this in the ledger. She tells herself this, too, is the atonement working.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - { axis: relational-anchor-status, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-protection-buys-consolidation, notes: "named-but-outside-ledger → structurally-at-risk-but-still-unpriced; 2.5→2; d06 shift; protect-target extension defers cost-bearer entry" }
            - { axis: moral-legibility-to-self, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-unpriced-cost-bearer, notes: "atoning-with-first-crack → rationalizing-each-trade; 6.5→6; d06 shift; criterion-displacement named by accounting" }
          density_target: "0.6-0.7"
        handoff_in:
          open_threads:
            - "readable-resentment accumulating; not yet named; the color of the court-layer data"
            - "Gylda introduced as peripheral figure with broader street-range than Taylor's insects"
            - "Wren's block inside coverage; still not flagged"
            - "intelligence deliveries continuing; court-layer picture deepening"
          world_state:
            - "122 AC; Taylor monitoring Red Keep approaches and Maegor's Holdfast courier-corridors"
            - "Green-faction intelligence picture has full Flea Bottom ground layer; Taylor is load-bearing"
            - "Sera Hightower's protection holding"
          character_state:
            - "taylor: moral-framework 2; capability 5; position 2; social-tether 3; relational-anchor 2.5; moral-legibility 6.5; political-register 6; knowledge 6; agency 4"
            - "wren: inside coverage; daily presence"
            - "gylda: introduced; peripheral"
            - "otto: arrangement operational"
          source_chapter: b01c07
        handoff_out:
          open_threads:
            - "Taylor named the criterion-displacement and revised the accounting; she did not revise the delivery"
            - "Wren's block surveilled for intelligence; Wren's movements read; none of this in the ledger"
            - "rationalization pattern established: network-integrity criterion displacing prohibition-criterion"
            - "Sera Hightower's protection maintained; each extension deepens Wren's non-pricing"
            - "Gylda moving through broader street-geography; peripheral but present"
          world_state:
            - "122 AC; network covers Wren's block; systematic surveillance architecture now operational across multiple wards"
            - "Green-faction intelligence picture robust; Taylor fully load-bearing"
          character_state:
            - "taylor: moral-framework 2; capability 5; position 2; social-tether 3; relational-anchor 2 (structurally-at-risk-but-unpriced); moral-legibility 6 (rationalizing-each-trade); political-register 6; knowledge 6; agency 4"
            - "wren: surveilled; Taylor has not told her; ledger shows nothing"
            - "otto: full Flea Bottom ground layer received; arrangement stable"
          target_chapter: b01c09
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c09
        chunk: |
          Otto makes explicit what the arrangement has been. He names the price that formalizes it: feed him the internal movement patterns of the opposing faction's smallfolk-layer couriers. Taylor pays it — the calculation says Sera Hightower's probability of survival drops without this delivery, and the delivery is within the criterion she is applying. She gives people their routes and patterns to Otto without their knowledge. She no longer calls it surgery. She calls it necessary. The naming-of-the-arrangement is a hinge: before this chapter, the arrangement was something she had entered for specific reasons and could in theory exit; after it, it is what she is. The chapter's three scenes track the arc of a single day — the delivery request, Taylor running the model, the delivery made and the courier-paths handed over — and end on Taylor filing the accounting, which now reads fluently: gains entered, costs entered, rationale entered, verdict: justified. The fluency is the problem. The ledger is still running, still receiving inputs, but its outputs are no longer painful to record. This chapter also moves Taylor's position: Otto's apparatus now has a name for her function, and the function has a regular delivery cadence. She is Otto's unofficial instrument. That fact is now structural to the Green-faction's intelligence picture in a way that is not reversible without Otto's active dismantling of it.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - { axis: moral-framework, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-otto-trade, notes: "first-sanctioned-exception → systematic-override-rationalized; 2→1.5; d07 shift" }
            - { axis: position, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-otto-trade, notes: "known-quantity → Otto's-unofficial-instrument; 2→2.5; d07 position shift; Otto's-unofficial-instrument; arrangement named; position-visibility now formal in the one court layer that uses Taylor" }
            - { axis: knowledge, direction: up, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-intelligence-arrangement, notes: "opposing faction's structure now mapped at courier level; 6→7; systematic court picture" }
            - { axis: agency, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-otto-trade, notes: "arrangement structural; exit-cost rising; 4→3.5; cl-otto-trade agency -1 deepens" }
          density_target: "0.7-0.8"
        handoff_in:
          open_threads:
            - "Taylor named the criterion-displacement and revised the accounting; she did not revise the delivery"
            - "Wren's block surveilled for intelligence; Wren's movements read; none of this in the ledger"
            - "rationalization pattern established: network-integrity criterion displacing prohibition-criterion"
            - "Sera Hightower's protection maintained; each extension deepens Wren's non-pricing"
            - "Gylda moving through broader street-geography; peripheral but present"
          world_state:
            - "122 AC; network covers Wren's block; systematic surveillance architecture operational across multiple wards"
            - "Green-faction intelligence picture robust; Taylor fully load-bearing"
          character_state:
            - "taylor: moral-framework 2; capability 5; position 2; social-tether 3; relational-anchor 2; moral-legibility 6; political-register 6; knowledge 6; agency 4"
            - "wren: surveilled; ledger shows nothing"
            - "otto: full ground layer received"
          source_chapter: b01c08
        handoff_out:
          open_threads:
            - "arrangement named and structural: Taylor is Otto's unofficial instrument"
            - "opposing faction's courier-paths delivered; consequences for those couriers pending"
            - "ledger running fluently; outputs no longer painful; the fluency is auditable"
            - "Sera Hightower's protection holding; Wren still outside the ledger"
            - "position now: Otto's-unofficial-instrument; not reversible without active dismantling"
          world_state:
            - "122 AC; Taylor's function has a name in Otto's apparatus; regular delivery cadence established"
            - "opposing-faction courier-layer compromised via Taylor's route-maps"
            - "Green-faction intelligence picture: systematic Flea Bottom + court-layer coverage"
          character_state:
            - "taylor: moral-framework 1.5 (systematic-override-rationalized); capability 5 (no trajectory allocation for capability at d07; see signal-004 resolution); position 2.5 (Otto's-unofficial-instrument); social-tether 3; relational-anchor 2; moral-legibility 6; political-register 6; knowledge 7; agency 3.5"
            - "wren: inside network; load-bearing for coverage without appearing in ledger"
            - "otto: arrangement formalized; Taylor named as function in his apparatus"
          target_chapter: b01c10
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c10
        chunk: |
          Without knowing she is inside the network, Wren becomes its most reliable anchor point. She moves freely through parts of Flea Bottom where Taylor's insects cannot cover without triggering the witch-label — the local superstition about insect-swarms that has been Taylor's primary operational constraint — and she carries observations back to Taylor in ordinary conversation: what she saw at the market, whose cart was where, which courier came twice in a morning. Wren does not know she is providing intelligence. Taylor routes around every use-vector that would expose Wren to Otto's notice. She does not route around Wren. She tells herself she is protecting Wren by keeping her invisible to the network's formal structure. The chapter makes the architecture visible to the reader: Wren is structurally necessary to the coverage map. Her movements feed Taylor's picture of the wards the insects cannot read without detection risk. None of this appears in the ledger. Taylor has not told Wren. Taylor has not obtained Wren's consent to be observed-for-protection. She reads it as care. Aemond Targaryen appears at this chapter's end — not in Flea Bottom but in a Red Keep corridor visible to Taylor's court-layer insect-feed, his presence registered as a plot-axis shift: the coercive arm of the Green faction is in residence, his particular quality of menace carried through the insect-feed as body-temperature and posture, the read that confirms the succession calculus is under active pressure from inside the Green faction, not only from the Blacks.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - { axis: relational-anchor-status, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-unpriced-cost-bearer, notes: "structurally-at-risk → load-bearing-in-network; 2→1.5; d08 shift; Wren necessary to coverage map without appearing in ledger" }
            - { axis: knowledge, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-intelligence-arrangement, notes: "Wren's Flea Bottom coverage fills insect-read gaps; Aemond's presence reads as succession-pressure signal; 7→7.5" }
          density_target: "0.6-0.7"
        handoff_in:
          open_threads:
            - "arrangement named and structural: Taylor is Otto's unofficial instrument"
            - "opposing faction's courier-paths delivered; consequences for those couriers pending"
            - "ledger running fluently; outputs no longer painful; the fluency is auditable"
            - "Sera Hightower's protection holding; Wren still outside the ledger"
            - "position now: Otto's-unofficial-instrument; not reversible without active dismantling"
          world_state:
            - "122 AC; Taylor's function has a name in Otto's apparatus; regular delivery cadence established"
            - "opposing-faction courier-layer compromised via Taylor's route-maps"
            - "Green-faction intelligence picture: systematic Flea Bottom + court-layer coverage"
          character_state:
            - "taylor: moral-framework 1.5; capability 5; position 2.5; social-tether 3; relational-anchor 2; moral-legibility 6; political-register 6; knowledge 7; agency 3.5"
            - "wren: inside network; load-bearing without ledger entry"
            - "otto: arrangement formalized"
          source_chapter: b01c09
        handoff_out:
          open_threads:
            - "Wren is structurally necessary to coverage map; not in ledger; Taylor has not told her"
            - "Aemond registered in Red Keep corridor; succession-pressure from inside Green faction confirmed"
            - "opposing-faction courier consequences unresolved; Taylor has not checked what happened to them"
            - "Sera Hightower's protection holding"
          world_state:
            - "122 AC; Wren providing informal intelligence via ordinary conversation without knowledge"
            - "Aemond in Red Keep residence; Green-faction coercive arm active"
            - "network coverage: Flea Bottom + adjacent wards + court-layer courier-corridors"
          character_state:
            - "taylor: moral-framework 1.5; capability 5; position 2.5; social-tether 3; relational-anchor 1.5 (load-bearing-in-network); moral-legibility 6; political-register 6; knowledge 7.5; agency 3.5"
            - "wren: load-bearing anchor; does not know; Taylor reads it as care"
            - "aemond: registered; walk-on; succession-pressure axis shifted by his presence"
            - "otto: arrangement stable"
          target_chapter: b01c11
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c11
        chunk: |
          A succession maneuver in the Maegor's Holdfast layer requires Taylor to run a sustained intelligence sequence — tracking a specific political play through multiple court feeds over several days. What she reads accumulates until a specific day produces the threshold-crossing image. Through the insect-feed, Taylor watches a report delivered to a chamber in Maegor's Holdfast: a document on smallfolk displacement, the body-temperature clusters of packed people legible through the feed as numbers, the density of the displaced ward readable in the warmth signature the insects carry back. The chamber's senior figure — one of the Green-faction inner circle whose instruments Taylor has been reading for months — receives the document, registers its physical weight, and places it unopened to one side. Twenty minutes later, by Taylor's insect-reckoning, the same figure signs the succession instrument that will route the political play through that same ward. The document is still unread. This is the moment the contempt arrives — not as more resentment-color, but as a completed observation, a conclusion: the ward's people are not a variable in the model; they are not even absent from the model; they are the surface the model is printed on, invisible as paper is invisible. The succession maneuver was designed, executed, and recorded without the displaced ward appearing anywhere in the accounting. Taylor has been consolidating the continuation of this. She names whose names — the Green-faction inner circle, the succession-instrument signatories, the figures in the specific chambers she has been reading — in the accounting, in the entries, in the lines of the ledger she has been keeping. The contempt is articulate and cold: she knows exactly who benefits from the intelligence she has been delivering, she has watched them receive that benefit in close feed, and the observation has produced a specific and legible assessment. She files the next intelligence delivery. The assessment does not change what she does. Gylda appears near the chapter's middle — water-carrier crossing multiple blocks, saying something that rhymes with "too-many-places" without precisely naming it — and Taylor files that observation too without acting on it. The contempt, once named, becomes load-bearing in a different way: it is the thing she carries forward, the clear cold register that will make the final accounting legible at close.
          # Aemond walk-on in c11 and axis-move assignment: deferred to /and-substance chapter b01c11.
          # Contempt-naming roster: Green-faction inner circle and succession-instrument signatories named as scope; individual name roster deferred to /and-substance chapter b01c11.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - { axis: political-register-toward-elite, direction: up, target_delta_magnitude: 1.5, cost_ledger_anchor: ~, notes: "readable-resentment → articulated-contempt; 6→7.5; d09 shift; consequence-axis; conclusion not feeling; threshold-crossing image: displacement report placed unread, succession instrument signed through the same ward" }
            - { axis: knowledge, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-intelligence-arrangement, notes: "court picture: more complete than most Small Council members; 7.5→8; d09 full court picture" }
          density_target: "0.7-0.8"
        handoff_in:
          open_threads:
            - "Wren is structurally necessary to coverage map; not in ledger; Taylor has not told her"
            - "Aemond registered in Red Keep corridor; succession-pressure from inside Green faction confirmed"
            - "opposing-faction courier consequences unresolved; Taylor has not checked what happened to them"
            - "Sera Hightower's protection holding"
          world_state:
            - "122 AC; Wren providing informal intelligence via ordinary conversation without knowledge"
            - "Aemond in Red Keep residence; Green-faction coercive arm active"
            - "network coverage: Flea Bottom + adjacent wards + court-layer courier-corridors"
          character_state:
            - "taylor: moral-framework 1.5; capability 5; position 2.5; social-tether 3; relational-anchor 1.5; moral-legibility 6; political-register 6; knowledge 7.5; agency 3.5"
            - "wren: load-bearing anchor; does not know"
            - "aemond: registered; walk-on"
            - "otto: arrangement stable"
          source_chapter: b01c10
        handoff_out:
          open_threads:
            - "contempt articulated and named in ledger; it does not change what Taylor does next"
            - "Gylda registered a too-many-places observation; Taylor filed it without acting on it"
            - "Wren still load-bearing and unlisted; Aemond's presence still an open pressure-signal"
            - "Sera Hightower's protection holding; succession calculus under pressure"
          world_state:
            - "122 AC; Maegor's Holdfast succession maneuver tracked; Green-faction play reading complete"
            - "Taylor's intelligence picture: more complete than most Small Council members"
            - "Gylda has now passed through Taylor's field of observation twice with cross-block commentary"
          character_state:
            - "taylor: moral-framework 1.5; capability 5; position 2.5; social-tether 3; relational-anchor 1.5; moral-legibility 6; political-register 7.5 (articulated-contempt); knowledge 8; agency 3.5"
            - "wren: load-bearing; unlisted"
            - "gylda: too-many-places observation made; not yet named by Taylor"
            - "aemond: active; succession-pressure registered"
            - "otto: arrangement operational; intelligence picture robust"
          target_chapter: b01c12
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c12
        chunk: |
          Taylor attempts to price an exit. This is the chapter where the ledger is turned on the arrangement itself: what would it cost to withdraw, to dismantle the network, to find another route for Sera Hightower's protection? The calculation returns: not possible. The network cannot be dismantled without Otto noticing; she is too load-bearing to withdraw; the one channel that might extract Sera Hightower through other means is now inside Otto's coverage. While Taylor is running the exit model, an opposing-faction courier is detained because Taylor's route-map reached Otto's apparatus. The courier is not dead — detained, questioned — but the route-map Taylor delivered is what made them detainable. Taylor runs the accounting on that: confirms Sera Hightower's protection benefit outweighs the courier's harm by the criterion she is applying, closes the ledger on the courier's entry, files. She registers that she ran the accounting on a person without their knowledge and ratified the result. This registration is the first-recognition: she sees, clearly, what the architecture has become. She suppresses it. She closes the ledger and continues. The chapter is the hinge of the book: before this, the question was whether Taylor would see; after this, the question is only when the seeing will catch up to what has already been built.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - { axis: social-tether, direction: down, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-social-tether-build, notes: "load-bearing-in-Otto's-architecture → exposed-and-non-extractable; 3→2; d10 shift; tether is now a trap" }
            - { axis: position, direction: down, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-social-tether-build, notes: "Otto's-unofficial-instrument → position-of-no-exit; 2.5→1.5; d10 position shift; exit calculation confirms no-exit" }
            - { axis: moral-legibility-to-self, direction: down, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-unpriced-cost-bearer, notes: "rationalizing-each-trade → first-recognition-suppressed; 6→5; d10 shift; suppression registered and executed" }
            - { axis: agency, direction: down, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-network-position, notes: "no-exit confirmed; 3.5→2.5; steepest agency drop to this point" }
          density_target: "0.8-0.9"
        handoff_in:
          open_threads:
            - "contempt articulated and named in ledger; it does not change what Taylor does next"
            - "Gylda registered a too-many-places observation; Taylor filed it without acting on it"
            - "Wren still load-bearing and unlisted; Aemond's presence still an open pressure-signal"
            - "Sera Hightower's protection holding; succession calculus under pressure"
          world_state:
            - "122 AC; Maegor's Holdfast succession maneuver tracked; Green-faction play reading complete"
            - "Taylor's intelligence picture: more complete than most Small Council members"
            - "Gylda has now passed through Taylor's field twice with cross-block commentary"
          character_state:
            - "taylor: moral-framework 1.5; capability 5; position 2.5; social-tether 3; relational-anchor 1.5; moral-legibility 6; political-register 7.5; knowledge 8; agency 3.5"
            - "wren: load-bearing; unlisted"
            - "gylda: too-many-places observation made"
            - "aemond: active; succession-pressure registered"
            - "otto: arrangement operational"
          source_chapter: b01c11
        handoff_out:
          open_threads:
            - "no-exit confirmed; the arrangement cannot be dismantled without Otto noticing"
            - "opposing-faction courier detained via Taylor's route-map; accounting closed on their harm"
            - "first-recognition registered and suppressed; Taylor filed and continued"
            - "Sera Hightower's protection holding; Wren unlisted and load-bearing"
            - "Aemond still in residence; coercive pressure ongoing"
          world_state:
            - "122 AC; Taylor's position: no-exit; network too load-bearing to withdraw from"
            - "opposing-faction courier-layer further compromised; a specific courier detained"
            - "Sera Hightower's protection holding per arrangement-term"
          character_state:
            - "taylor: moral-framework 1.5; capability 5; position 1.5 (position-of-no-exit); social-tether 2 (exposed-and-non-extractable); relational-anchor 1.5; moral-legibility 5 (first-recognition-suppressed); political-register 7.5; knowledge 8; agency 2.5 (no-exit confirmed)"
            - "wren: load-bearing; not in ledger; in danger Taylor has not calculated"
            - "otto: arrangement too load-bearing to exit; full Green-faction intelligence architecture"
          target_chapter: b01c13
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c13
        chunk: |
          Someone inside Otto's network identifies Wren as a courier-adjacent contact whose movements could be used. The identification arrives to Taylor through the same insect-feed she uses to monitor the network's internal communications — she intercepts it before Otto routes it into a formal ask. She adjusts the network to screen any use-vector that includes Wren directly. This is the chapter where the architecture turns fully visible: Taylor has built a network that is capable of instrumentalizing Wren, and she is using that same network to prevent Wren's instrumentalization, and she has not told Wren any of it. She does not tell Wren now. She tells herself she protected Wren. She runs the accounting on the protection and it returns: she surveilled the network's own communications without authorization (by whose authority would she have authorization?), adjusted coverage to route around a specific person, and maintained the non-disclosure that keeps Wren uninformed about her own structural position. The accounting runs. The output is legible. Taylor rationalizes the output: she protected Wren, the protection was real, the means are within the prohibition's criterion. The second recognition: she is running the same override architecture she built to atone for, and calling it protection. This recognition is also suppressed — rationalized, filed, closed. The chapter's final scene is Wren, present and attached and asking questions about the stitching, while Taylor holds the knowledge of what she just did.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - { axis: relational-anchor-status, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-unpriced-cost-bearer, notes: "load-bearing → load-bearing-and-named-but-still-outside-ledger; 1.5→1; d11 shift; intercept reveals how deep the non-pricing goes" }
            - { axis: moral-legibility-to-self, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-unpriced-cost-bearer, notes: "first-recognition-suppressed → second-recognition-rationalized; 5→4.5; d11 shift; override architecture named and rationalized" }
          density_target: "0.7-0.8"
        handoff_in:
          open_threads:
            - "no-exit confirmed; the arrangement cannot be dismantled without Otto noticing"
            - "opposing-faction courier detained via Taylor's route-map; accounting closed on their harm"
            - "first-recognition registered and suppressed; Taylor filed and continued"
            - "Sera Hightower's protection holding; Wren unlisted and load-bearing"
            - "Aemond still in residence; coercive pressure ongoing"
          world_state:
            - "122 AC; Taylor's position: no-exit; network too load-bearing to withdraw from"
            - "opposing-faction courier-layer further compromised; a specific courier detained"
            - "Sera Hightower's protection holding per arrangement-term"
          character_state:
            - "taylor: moral-framework 1.5; capability 5; position 1.5; social-tether 2; relational-anchor 1.5; moral-legibility 5; political-register 7.5; knowledge 8; agency 2.5"
            - "wren: load-bearing; not in ledger"
            - "otto: full Green-faction intelligence architecture; arrangement too load-bearing to exit"
          source_chapter: b01c12
        handoff_out:
          open_threads:
            - "Wren protected from network-use by Taylor's intercept; Wren does not know"
            - "second-recognition rationalized and filed; Taylor knows she is running what she built to atone for"
            - "override architecture named by Taylor herself: surveillance + unconsented routing = Khepri-rhyme"
            - "Otto's network identified Wren; Taylor screened it; Otto does not yet know Taylor blocked this"
            - "Sera Hightower's protection holding; no-exit still confirmed"
          world_state:
            - "122 AC; Taylor's coverage adjusted to screen Wren from network-use vectors"
            - "Green-faction network identified Wren as a potential asset; this threat now temporarily suppressed"
            - "Aemond still in residence; succession-pressure ongoing"
          character_state:
            - "taylor: moral-framework 1.5; capability 5; position 1.5; social-tether 2; relational-anchor 1 (load-bearing-and-named-but-still-outside-ledger); moral-legibility 4.5 (second-recognition-rationalized); political-register 7.5; knowledge 8; agency 2.5"
            - "wren: protected from use-vector; does not know; still outside ledger"
            - "otto: network operational; does not know Taylor blocked Wren's identification"
          target_chapter: b01c14
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c14
        chunk: |
          Sera Hightower's position in the succession calculus becomes critical. A specific threat to her exposure requires Taylor to push the network to full coverage: reading and routing more bodies through more wards without their knowledge than at any prior point. The chapter tracks the threat's arrival and Taylor's operational response — the network expanding outward, the coverage perimeter widening, the intelligence picture filling in detail on the specific vulnerability in Sera Hightower's position. Taylor does not hesitate. The calculation is the same arithmetic it has always been, and the arithmetic is correct. The chapter's weight is in the gap between Taylor's accounting of what she is doing (surveillance architecture + strategic intelligence delivery = Sera Hightower protected) and what the reader can see: that the scale of what she is deploying is past any defensible reading of the prohibition she started with. This is not yet the chapter where Taylor names that gap. The chapter ends before the full deployment is complete — Sera Hightower's position stabilized temporarily by the initial network expansion, but the full push required to secure her position is still in progress. Aemond appears in this chapter's middle, visible in the court-layer feed in a posture that reads as operative rather than merely coercive — he has done something specific, and what he has done is why Sera Hightower's exposure has become critical now rather than at the next succession move.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - { axis: capability, direction: up, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-network-position, notes: "Khepri-rhyming-architecture → fully-deployed-begins; 5→6; d12 first beat; Aemond's operative action triggers full push" }
            - { axis: knowledge, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-intelligence-arrangement, notes: "Sera vulnerability mapped at full resolution; Aemond's specific action read; 8→8.5" }
            - { axis: agency, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-otto-trade, notes: "forced full-deployment forecloses remaining option space; 2.5→2" }
          density_target: "0.7-0.8"
        handoff_in:
          open_threads:
            - "Wren protected from network-use by Taylor's intercept; Wren does not know"
            - "second-recognition rationalized and filed; Taylor knows she is running what she built to atone for"
            - "override architecture named by Taylor herself: surveillance + unconsented routing = Khepri-rhyme"
            - "Otto's network identified Wren; Taylor screened it; Otto does not yet know Taylor blocked this"
            - "Sera Hightower's protection holding; no-exit still confirmed"
          world_state:
            - "122 AC; Taylor's coverage adjusted to screen Wren from network-use vectors"
            - "Green-faction network identified Wren as a potential asset; threat temporarily suppressed"
            - "Aemond still in residence; succession-pressure ongoing"
          character_state:
            - "taylor: moral-framework 1.5; capability 5; position 1.5; social-tether 2; relational-anchor 1; moral-legibility 4.5; political-register 7.5; knowledge 8; agency 2.5"
            - "wren: protected from use-vector; does not know; still outside ledger"
            - "otto: network operational"
          source_chapter: b01c13
        handoff_out:
          open_threads:
            - "Sera Hightower's position stabilized temporarily; full network push still in progress"
            - "Aemond made a specific operative move that triggered the exposure; what he did is now in Taylor's picture"
            - "full-deployment in progress; the prohibition's criterion is being read against an operation past its scale"
            - "Wren outside ledger; Otto does not know Taylor blocked her identification"
          world_state:
            - "122 AC; network expanding to full coverage across multiple wards; more bodies read and routed than at any prior point"
            - "Aemond operative; specific succession-maneuver executed; effect: Sera Hightower's exposure"
            - "Otto's intelligence picture receiving full-deployment output"
          character_state:
            - "taylor: moral-framework 1.5; capability 6 (full-deployment begun); position 1.5; social-tether 2; relational-anchor 1; moral-legibility 4.5; political-register 7.5; knowledge 8.5; agency 2"
            - "wren: outside ledger; inside the network's full coverage perimeter"
            - "aemond: operative; specific move made; succession plot axis shifted"
            - "otto: full-deployment output received"
          target_chapter: b01c15
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c15
        chunk: |
          Taylor pushes the network to full deployment. More bodies through more wards read and routed than at any prior point. Sera Hightower's position in the succession calculus survives the specific threat Aemond's maneuver opened. The intelligence is delivered; the threat is neutralized; the network is now structural to the Green-faction's intelligence picture in a way that cannot be unwound without unraveling the whole Green-faction intelligence apparatus. The chapter holds this moment in close focus: Taylor running the deployment, Taylor delivering the intelligence, Taylor receiving the accounting on what she just did. The scale is smaller than Gold Morning. The moral shape is the same. Taylor names this — in the accounting, to herself — and the naming is not refusal. The accounting has a category for it: surveillance and unconsented instrumentalization of movement patterns, the Khepri-rhyme, the architecture she built to atone for. She runs the category-check: is this that? Yes. Is it still inside the prohibition? She applies the criterion. Yes, by the criterion. She knows the criterion is the problem. She closes the ledger and files the delivery. The chapter ends on the network's full deployment state: Flea Bottom and adjacent wards covered, court-layer courier-corridors read, Sera Hightower alive. The atonement was the repetition. Taylor has not said this in those words. She is very close to saying it.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - { axis: moral-framework, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-otto-trade, notes: "systematic-override-rationalized → irrevocable-Khepri-repetition; 1.5→1; d12 completion beat" }
            - { axis: capability, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-network-position, notes: "fully-deployed-and-load-bearing; 6→6.5; d12 completion" }
            - { axis: agency, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-network-position, notes: "network structural to Green-faction; cannot unwind without unraveling their apparatus; 2→1.5" }
          density_target: "0.8-0.9"
        handoff_in:
          open_threads:
            - "Sera Hightower's position stabilized temporarily; full network push still in progress"
            - "Aemond made a specific operative move that triggered the exposure; what he did is now in Taylor's picture"
            - "full-deployment in progress; the prohibition's criterion is being read against an operation past its scale"
            - "Wren outside ledger; Otto does not know Taylor blocked her identification"
          world_state:
            - "122 AC; network expanding to full coverage; more bodies read and routed than at any prior point"
            - "Aemond operative; specific succession-maneuver executed"
            - "Otto's intelligence picture receiving full-deployment output"
          character_state:
            - "taylor: moral-framework 1.5; capability 6; position 1.5; social-tether 2; relational-anchor 1; moral-legibility 4.5; political-register 7.5; knowledge 8.5; agency 2"
            - "wren: outside ledger; inside full coverage perimeter"
            - "aemond: operative"
            - "otto: full-deployment output received"
          source_chapter: b01c14
        handoff_out:
          open_threads:
            - "Khepri-repetition named in accounting; not yet refusal; ledger closed on the category-check"
            - "network structural to Green-faction intelligence picture; not reversible"
            - "Sera Hightower alive; the protection worked; the cost of the protection is the architecture"
            - "Wren outside ledger; inside fully deployed network; Otto's identification-attempt screened once"
            - "Aemond's operative move confirmed; succession calculus has been stabilized for now"
          world_state:
            - "122 AC; full-deployment operational: Flea Bottom + adjacent wards + court-layer courier-corridors"
            - "Sera Hightower's position in succession calculus secured for present term"
            - "Green-faction intelligence picture: Taylor's network is structural to it; non-reversible"
          character_state:
            - "taylor: moral-framework 1 (irrevocable-Khepri-repetition); capability 6.5 (fully-deployed); position 1.5; social-tether 2; relational-anchor 1; moral-legibility 4.5; political-register 7.5; knowledge 8.5; agency 1.5"
            - "wren: unlisted; inside network; one interception protecting her from direct use"
            - "otto: full apparatus secured; Taylor non-extractable"
          target_chapter: b01c16
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c16
        chunk: |
          The intelligence deliveries have worked. Sera Hightower is shielded; the succession apparatus holds; the war is delayed by the consolidation Taylor's work enabled. Taylor reviews what that consolidation has produced: Green-faction control of Maegor's Holdfast, the Small Council, the succession angle. The elite whose continuity she guaranteed are exactly as she observed them — she has not been wrong about them once. The contempt is complete and accurate and has no exit. This is the chapter where the contempt settles from articulated to structural: she is not arriving at new conclusions, she is recognizing that the conclusions she arrived at in chapter eleven have remained true and have had no effect on her behavior. The contempt does not free her. The chapter holds a specific scene in which Taylor delivers the final intelligence delivery of what has been a run of deliveries, and the delivery is correct, and the delivery consolidates the Green-faction's position, and she files the accounting, and the accounting is legible, and the legibility is not relief. It is the cost. Gylda appears briefly and her too-many-places comment is now readable to Taylor as accurate, not oblique — Taylor files the read. Wren is present at the chapter's close, in ordinary interaction, and Taylor looks at her and runs no accounting. There is no entry to make. The chapter ends on the contempt-without-refusal state: articulated, legible, bound to continued service. She continues because the only thing more expensive than the trades is letting Wren burn.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - { axis: political-register-toward-elite, direction: up, target_delta_magnitude: 1.0, cost_ledger_anchor: ~, notes: "articulated-contempt → contempt-without-refusal; 7.5→8.5; d13 shift; contempt structural and non-exiting; consequence-axis" }
          density_target: "0.7-0.8"
        handoff_in:
          open_threads:
            - "Khepri-repetition named in accounting; not yet refusal; ledger closed on the category-check"
            - "network structural to Green-faction intelligence picture; not reversible"
            - "Sera Hightower alive; the protection worked; the cost of the protection is the architecture"
            - "Wren outside ledger; inside fully deployed network; Otto's identification-attempt screened once"
            - "Aemond's operative move confirmed; succession calculus stabilized for now"
          world_state:
            - "122 AC; full-deployment operational: Flea Bottom + adjacent wards + court-layer courier-corridors"
            - "Sera Hightower's position in succession calculus secured for present term"
            - "Green-faction intelligence picture: Taylor's network is structural to it; non-reversible"
          character_state:
            - "taylor: moral-framework 1; capability 6.5; position 1.5; social-tether 2; relational-anchor 1; moral-legibility 4.5; political-register 7.5; knowledge 8.5; agency 1.5"
            - "wren: unlisted; inside network"
            - "otto: full apparatus secured"
          source_chapter: b01c15
        handoff_out:
          open_threads:
            - "contempt-without-refusal state established; she continues; Gylda named the too-many-places pattern accurately"
            - "Wren observed without accounting; no entry; the non-entry is the final form of non-pricing"
            - "Sera Hightower protected; war delayed; the consolidation has produced exactly what Taylor despises"
            - "Green-faction position secured; Taylor has made it so; the ledger is legible on this"
          world_state:
            - "122 AC; Green-faction control of Maegor's Holdfast + Small Council + succession angle: consolidated"
            - "Sera Hightower protected; Dancing delayed; Taylor's work has produced its intended effect"
            - "Gylda has now explicitly named the too-many-places register"
          character_state:
            - "taylor: moral-framework 1; capability 6.5; position 1.5; social-tether 2; relational-anchor 1; moral-legibility 4.5; political-register 8.5 (contempt-without-refusal); knowledge 8.5; agency 1.5"
            - "wren: present; no accounting run; the non-entry is the fact"
            - "gylda: too-many-places named; Taylor registered it accurately"
            - "otto: full apparatus; position consolidated; arrangement stable"
          target_chapter: b01c17
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c17
        chunk: |
          The Dance ignites. The Flea Bottom violence that opens the war moves through exactly the streets Taylor's network mapped and Otto's architecture knew. Taylor cannot reroute it — it is not a courier path, it is a faction's bladed answer to the succession rupture, and the faction is the one her intelligence has been consolidating for years. She attempts to reroute it anyway. She threads every insect she has through the ward, reads the movement patterns of the violence, tries to find any gap in the routing, any alley that would take Wren clear the way the alley off the Hook took Wren clear in the first chapter. There is no gap. Wren dies in the street Taylor had charted. Taylor is removed — the Green-faction apparatus, which has been managing her as an asset, decides that an asset with this capability and no formal rank is a liability now that the war has begun and factions need to know whose intelligence they are holding. She is dead or expelled by the forces her position made her legible to. The final accounting runs: every entry readable backward; the ledger names whom she empowered, in exchange for whom, and what it cost. Aemond appears in the chapter's opening as the visible trigger of the Dance's initial violence — his presence in the chapter shifts the agency-axis at book close, the coercive arm of the faction Taylor consolidated having become the instrument of the outcome she spent the book preventing. The contempt was the recognition. The recognition came too late to constitute refusal.
        structure:
          scene_count: 5
        substance_delta:
          axes_in_motion:
            - { axis: relational-anchor-status, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: [cl-unpriced-cost-bearer, cl-protection-buys-consolidation], notes: "load-bearing-and-named → unprotected-at-burn; Wren dies; 1→0.5 (floor: below-rank-1 permitted at burn)" }
            - { axis: moral-legibility-to-self, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-unpriced-cost-bearer, notes: "second-recognition-rationalized → recognition-too-late; 4.5→4; d14 shift; final accounting runs and delivers" }
            - { axis: social-tether, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-social-tether-build, notes: "exposed-and-non-extractable → severed; Wren dead; Otto channel dissolved; 2→1.5" }
            - { axis: position, direction: down, target_delta_magnitude: 1.0, cost_ledger_anchor: cl-social-tether-build, notes: "position-of-no-exit → dead-or-expelled; 1.5→0.5 (floor); d14 locked hard fence" }
            - { axis: political-register-toward-elite, direction: up, target_delta_magnitude: 0.5, cost_ledger_anchor: ~, notes: "contempt-without-refusal → ledger-of-the-empowered; 8.5→9; d14; final accounting names empowered, cost-bearer, exchange rate; consequence-axis" }
            - { axis: agency, direction: down, target_delta_magnitude: 0.5, cost_ledger_anchor: cl-network-position, notes: "locked; dead-or-expelled; 1.5→1; d14" }
          density_target: "0.8-0.9"
        handoff_in:
          open_threads:
            - "contempt-without-refusal state established; she continues; Gylda named too-many-places accurately"
            - "Wren observed without accounting; no entry; the non-entry is the final form of non-pricing"
            - "Sera Hightower protected; war delayed; consolidation produced exactly what Taylor despises"
            - "Green-faction position secured; Taylor has made it so"
          world_state:
            - "122 AC (transitioning to Dance's opening); Green-faction control consolidated; Sera Hightower protected; war delayed by Taylor's work — but not prevented"
            - "Gylda has named the too-many-places register"
            - "Aemond operative; succession-pressure ongoing; the coercive arm is moving"
          character_state:
            - "taylor: moral-framework 1; capability 6.5; position 1.5; social-tether 2; relational-anchor 1; moral-legibility 4.5; political-register 8.5; knowledge 8.5; agency 1.5"
            - "wren: present; unlisted; alive at chapter open"
            - "otto: full apparatus; arrangement stable through end of chapter open"
            - "aemond: operative; about to trigger Dance's opening violence"
          source_chapter: b01c16
        handoff_out:
          open_threads:
            - "CLOSED: Wren dead in the street Taylor charted — the un-priced relationship retroactively revealed as the one she could not defend"
            - "CLOSED: Taylor removed — dead or expelled; position-of-no-exit resolved to hard fence end-state"
            - "CLOSED: final accounting delivered — empowered named, cost-bearer named, exchange rate named"
            - "OPEN for coda: the network Taylor built outlasted its architect; Aemond's action is the final plot-axis shift registered"
          world_state:
            - "Dance ignited; Flea Bottom violence moved through charted streets; Wren dead"
            - "Taylor removed from story's scope; position: dead or expelled"
            - "Green-faction apparatus intact; network transferred to Otto's direct management"
            - "Aemond's action: Dance's opening trigger visible in coda's retrospective frame"
          character_state:
            - "taylor: moral-framework 1 (prohibition violated across the book; ledger ran to close); capability 6.5 (deployed and then removed from scope); position ~0.5 (dead-or-expelled); social-tether ~1.5 (severed); relational-anchor ~0.5 (unprotected-at-burn); moral-legibility 4 (recognition-too-late; accounting delivered final output); political-register 9 (contempt-without-refusal → ledger-of-the-empowered); knowledge 8.5 (picture complete; cannot act on it); agency 1 (zero; locked into no-exit then expelled)"
            - "wren: dead"
            - "aemond: Dance trigger; walk-on complete; plot-axis shift registered"
            - "otto: apparatus intact; Taylor managed as completed asset"
          target_chapter: b01c18
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

      - slug: b01c18
        pov_note: "INTERLUDE — Archmaester Corvan retrospective; non-Taylor POV"
        chunk: |
          Archmaester Corvan, writing in approximately 160 AC, composes a passage in his chronicle on the intelligence architecture that undergirded the Green-faction consolidation in the years before the Dance — the peculiar ground-layer surveillance that Otto Hightower's correspondence obliquely references and which no surviving record attributes to a named practitioner. The chapter is the maester-chronicler voice: retrospective, evidential, careful, counterfactual. Corvan does not know Taylor's name. He has a description — a foreign woman of indeterminate origin, no rank, no formal appointment, no family name that appears in any ledger — and a pattern: the Green-faction's intelligence picture in 121–129 AC had a Flea Bottom ground layer with a quality of coverage that was not explicable by the recorded informant networks. He posits a practitioner. He names what the practitioner would have needed to be able to do. He identifies the moral shape — observation without consent, inference from movement patterns, information delivered to a factional apparatus by someone with no recorded title — and names it, in maester-chronicler language, as neither spycraft nor witchery but something in between that the categories of 122 AC did not have a name for. He notes that the Flea Bottom violence of the Dance's first week was especially lethal in the blocks adjacent to the Hook — the very streets he has spent this passage mapping as the likely coverage-center of the unnamed practitioner's network. He files no verdict. He does not have the data to file a verdict. The chronicle closes on the counterfactual he cannot name: if the practitioner exists, and if the practitioner had a reason for choosing those blocks, then the ledger of what was preserved and what was not preserved in the opening days of the Dance is a document someone constructed without knowing they were constructing it.
        structure:
          scene_count: 3
        substance_delta:
          # b01c18 is an INTERLUDE / frame chapter — Archmaester Corvan POV at c.160 AC, not Taylor.
          # No protagonist-axis moves at this chapter; both axes intentionally held.
          # /and-write Phase 6 substance bone-gate is exempted at this chapter per chapter_class: frame-coda below.
          axes_in_motion: []
          axes_held:
            - { axis: moral-legibility-to-self, rationale: "coda chapter; Corvan POV; protagonist not on-stage; protagonist-perspective accounting frozen at b01c17 close" }
            - { axis: knowledge, rationale: "Corvan's picture is incomplete by design; the chapter's substance lives in world-perspective archival framing, not protagonist-knowledge extension" }
          density_target: "0.5-0.6"
          chapter_class: frame-coda          # exempt from standard bone-gate Δ checks; reviewed by dramatist for frame-shape only
        handoff_in:
          open_threads:
            - "OPEN for coda: the network Taylor built outlasted its architect; Aemond's action is the final plot-axis shift registered"
            - "OPEN: the counterfactual: if the practitioner had a reason for choosing those blocks, then the ledger is a document someone constructed without knowing"
          world_state:
            - "c.160 AC; Corvan writing retrospective chronicle; Dance has occurred and is historical fact"
            - "Green-faction consolidation 121–129 AC has left evidential traces in Otto's correspondence"
            - "Flea Bottom violence of Dance's first week: documented; the specific blocks documented by Corvan"
            - "Taylor's name: unknown to Corvan; foreign woman of indeterminate origin; no formal appointment"
          character_state:
            - "corvan-archmaester-retrospective-coda: writing c.160 AC; evidential voice; does not know Taylor's name; has a pattern and a practitioner-hypothesis"
            - "taylor-hebert-kl-122ac: absent from Corvan's record except as unnamed pattern; dead or expelled by Dance's opening days"
            - "wren-stitch-maker-flea-bottom-ward: unnamed in Corvan's chronicle; one of the casualties in the Hook-adjacent blocks"
          source_chapter: b01c17
        handoff_out:
          open_threads: []
          world_state:
            - "c.160 AC; chronicle filed; counterfactual named but not resolved; Corvan does not have the data to file a verdict"
            - "the ledger-of-the-empowered is the document Corvan is reading without knowing what it is"
          character_state:
            - "corvan: chronicle complete; no verdict filed; the practitioner remains unnamed"
            - "taylor: retroactively present only as a pattern in evidential records; name permanently unknown to this voice"
          target_chapter: null
        status: planned
        # pov_narrator, dramatic_shape, goal authored later by /and-substance chapter

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
