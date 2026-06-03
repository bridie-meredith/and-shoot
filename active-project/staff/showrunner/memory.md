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
    approved_at: 2026-05-24T00:00:00Z
    approved_by: user
    report_path: active-project/staff/reviews/series-audit-2026-05-24.md
    stale_since: null

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

    # actor_baselines: authored 2026-05-24 at Step 4d (post-cast); 132 cells (11 actors × 12 axes).
    # Admin DEC-0002 ACCEPT (basis: ltm:2026-05-24 handle-routine + methodology:3a reversibility + 3b cost).
    # Draft archived: active-project/staff/showrunner/_drafts/actor-baselines-draft-2026-05-24.md
    # JUDGMENT CALLS surfaced and accepted:
    #   - Rhaenyra position-world / political_register-world: moves INVERTED CARRIER (7→2 inverse of Green 5→9 rise)
    #   - Aemond position-world: static 8→8 (coercive ceiling, not consolidation-arc carrier)
    #   - Criston position-world: static 8→8 (enforcement-instrument standing, not rise carrier)
    #   - Sera position-world / political_register-world: static 6→6 (court-tier ward beneficiary, not faction agent)
    actor_baselines:

      # === taylor-hebert-kl-122ac (protagonist; 12 axes) ===
      # All 9 protagonist-perspective axes: moves, lifted-from-state-axes.
      # social_tether-antag, position-world, political_register-world: not-applicable — object or instrument, not carrier.

      - actor: taylor-hebert-kl-122ac
        axis: moral_framework
        applicability: moves
        start_rank: 2
        end_rank: 8
        source: lifted-from-state-axes
        notes: "prohibition collapse; matches state_axes[].{start_rank,end_rank}; monotonic"

      - actor: taylor-hebert-kl-122ac
        axis: capability
        applicability: moves
        start_rank: 2
        end_rank: 8
        source: lifted-from-state-axes
        notes: "insect-network deployment scale rises; matches state_axes[].{start_rank,end_rank}; monotonic"

      - actor: taylor-hebert-kl-122ac
        axis: position-prot-rise
        applicability: moves
        start_rank: 1
        end_rank: 7
        source: lifted-from-state-axes
        notes: "rise phase only; peaks ~7 at d07; matches state_axes[].{start_rank,end_rank}"

      - actor: taylor-hebert-kl-122ac
        axis: position-prot-collapse
        applicability: moves
        start_rank: 7
        end_rank: 1
        source: lifted-from-state-axes
        notes: "collapse phase only; starts from d10 peak; matches state_axes[].{start_rank,end_rank}"

      - actor: taylor-hebert-kl-122ac
        axis: relational_anchor_status
        applicability: moves
        start_rank: 1
        end_rank: 9
        source: lifted-from-state-axes
        notes: "un-priced anchor pressure rises; HIGH=WORST; matches state_axes[].{start_rank,end_rank}"

      - actor: taylor-hebert-kl-122ac
        axis: moral_legibility_to_self
        applicability: moves
        start_rank: 4
        end_rank: 8
        source: lifted-from-state-axes
        notes: "non-linear net-positive; recognition-too-late; matches state_axes[].{start_rank,end_rank}"

      - actor: taylor-hebert-kl-122ac
        axis: political_register-prot
        applicability: moves
        start_rank: 1
        end_rank: 9
        source: lifted-from-state-axes
        notes: "contempt-accumulation; monotonic; matches state_axes[].{start_rank,end_rank}"

      - actor: taylor-hebert-kl-122ac
        axis: social_tether-prot-rise
        applicability: moves
        start_rank: 1
        end_rank: 8
        source: lifted-from-state-axes
        notes: "rise phase only; peaks ~8 at d07; matches state_axes[].{start_rank,end_rank}"

      - actor: taylor-hebert-kl-122ac
        axis: social_tether-prot-collapse
        applicability: moves
        start_rank: 8
        end_rank: 1
        source: lifted-from-state-axes
        notes: "collapse phase only; starts from d10 peak; matches state_axes[].{start_rank,end_rank}"

      - actor: taylor-hebert-kl-122ac
        axis: social_tether-antag
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Otto's leverage OVER Taylor; Taylor is the object the leverage is measured against, not a carrier of the position"

      - actor: taylor-hebert-kl-122ac
        axis: position-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "Taylor is the instrument of Green-faction consolidation, not a position-holder in the faction; axis tracks institutional consolidation, not the instrument's standing"

      - actor: taylor-hebert-kl-122ac
        axis: political_register-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction succession position secured; Taylor is the mechanism, not a faction member or position-occupant"

      # === otto-hightower (antagonist; 12 axes) ===
      # Primary carriers: social_tether-antag (lifted), position-world (lifted), political_register-world (lifted).
      # All Taylor-interior + Taylor-tether/position axes: not-applicable — Otto is proximate cause / agent, not position-carrier.

      - actor: otto-hightower
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior anti-instrumentalization accounting; Otto is the proximate cause of each breach but does not carry the position"

      - actor: otto-hightower
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment scope; Otto's own intelligence capability is off-axis and off-arc in this framework"

      - actor: otto-hightower
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Otto is the position-architect but does not occupy the position on this axis"

      - actor: otto-hightower
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Otto removes Taylor at d14 but does not himself lose position — he is the agent of collapse, not the carrier"

      - actor: otto-hightower
        axis: relational_anchor_status
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's un-priced anchor pressure; Otto is the structural threat enabling the cost but not a carrier of the relational position"

      - actor: otto-hightower
        axis: moral_legibility_to_self
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior self-accounting; Otto has no self-accounting gap in this framework — his misread of Taylor is the gap but it is not this axis"

      - actor: otto-hightower
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance toward Westerosi elite; Otto IS the elite architecture Taylor is developing contempt toward; he does not carry the register-toward position"

      - actor: otto-hightower
        axis: social_tether-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's relational and institutional tether in KL; Otto is the architect of that tether but does not occupy a position on the tether axis itself"

      - actor: otto-hightower
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Otto dissolves the arrangement at d14 but does not himself lose tether — agent of collapse, not carrier"

      - actor: otto-hightower
        axis: social_tether-antag
        applicability: moves
        start_rank: 1
        end_rank: 9
        source: lifted-from-state-axes
        notes: "primary carrier; Otto's leverage over Taylor rises monotonically as network embeds; matches state_axes[].{start_rank,end_rank}"

      - actor: otto-hightower
        axis: position-world
        applicability: moves
        start_rank: 5
        end_rank: 9
        source: lifted-from-state-axes
        notes: "consolidation architect; his operational moves ARE the Green-faction institutional rise; matches state_axes[].{start_rank,end_rank}"

      - actor: otto-hightower
        axis: political_register-world
        applicability: moves
        start_rank: 5
        end_rank: 9
        source: lifted-from-state-axes
        notes: "Green-faction succession position secured through his intelligence architecture; primary driver of world-axis rise; matches state_axes[].{start_rank,end_rank}"

      # === wren-stitch-maker-flea-bottom-ward (cost-bearer; 12 axes) ===
      # Primary carrier: relational_anchor_status (lifted; HIGH=WORST — axis IS the cost-bearer's vulnerability trajectory).
      # All other axes: not-applicable.

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior anti-instrumentalization accounting; Wren is the subject of the omission, not a carrier of the framework position"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment; Wren has no capability arc in this framework"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Wren has no court position and no standing arc — she is a Flea Bottom ward throughout"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Wren's d14 death is a consequence of the collapse, not an instance of it on this axis"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: relational_anchor_status
        applicability: moves
        start_rank: 1
        end_rank: 9
        source: lifted-from-state-axes
        notes: "primary carrier; axis IS the cost-bearer's vulnerability trajectory; HIGH=WORST; her exclusion from the ledger is structurally causal to her death; matches state_axes[].{start_rank,end_rank}"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: moral_legibility_to_self
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's self-accounting accuracy; Wren is the subject of Taylor's accounting gap, not a self-accounting carrier"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance toward Westerosi elite; Wren is smallfolk with no court-register arc and no investment in the succession axis"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: social_tether-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's KL institutional tether; Wren is entirely Flea Bottom-local and is not a component of Taylor's court-adjacent tether architecture"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Wren's death is a cost paid at collapse, not an axis position she carries"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: social_tether-antag
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Otto's leverage over Taylor; Wren is the latent lever Otto identifies at d11, not a carrier of the leverage position"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: position-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction institutional consolidation; Wren is a Flea Bottom ward with no participation in the faction machinery"

      - actor: wren-stitch-maker-flea-bottom-ward
        axis: political_register-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction succession position; Wren has no participation in the succession machinery"

      # === sera-hightower-kl-122ac (protect-target; 12 axes) ===
      # Sera is priced-and-protected target (opposite role to Wren on relational machinery).
      # position-world / political_register-world: static 6→6 (court-tier ward beneficiary, not faction agent).
      # All protagonist-interior + Otto-leverage + Taylor-tether axes: not-applicable.

      - actor: sera-hightower-kl-122ac
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior anti-instrumentalization accounting; Sera is the object of the protection arrangement, not an accounting carrier"

      - actor: sera-hightower-kl-122ac
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment; Sera has no capability arc in this framework"

      - actor: sera-hightower-kl-122ac
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Sera's court position is held by Otto's architecture, not a parallel arc on this axis"

      - actor: sera-hightower-kl-122ac
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Sera's position is sustained (the protection succeeds as stated); her arc does not collapse on this axis"

      - actor: sera-hightower-kl-122ac
        axis: relational_anchor_status
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's un-priced anchor; Sera is the priced-and-protected target — opposite role on the same machinery; the un-priced anchor is Wren"

      - actor: sera-hightower-kl-122ac
        axis: moral_legibility_to_self
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's self-accounting; Sera has no self-accounting arc visible in this project — she does not know Taylor exists"

      - actor: sera-hightower-kl-122ac
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance toward the elite; Sera IS a court-tier ward — she does not carry a register-toward-elite position"

      - actor: sera-hightower-kl-122ac
        axis: social_tether-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's KL tether; Sera's court placement is what the tether is built to protect, not a parallel tether position"

      - actor: sera-hightower-kl-122ac
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Sera's position is sustained through d14; she is not a tether-collapse carrier"

      - actor: sera-hightower-kl-122ac
        axis: social_tether-antag
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Otto's leverage over Taylor; Sera's legitimacy question IS the lever, but she is the object of the lever, not a leverage-position carrier"

      - actor: sera-hightower-kl-122ac
        axis: position-world
        applicability: static
        start_rank: 6
        end_rank: 6
        source: inferred-from-role-card
        notes: "JUDGMENT-CALL-ACCEPTED: court-tier ward in Alicent's household; position held by Otto's architecture throughout; beneficiary of consolidation, not its agent; static at mid-high rank reflecting protected court standing"

      - actor: sera-hightower-kl-122ac
        axis: political_register-world
        applicability: static
        start_rank: 6
        end_rank: 6
        source: inferred-from-role-card
        notes: "JUDGMENT-CALL-ACCEPTED: legitimacy question is the lever Taylor is protecting against; succession-adjacent standing held steady by the protection (the arrangement's purpose); static rather than moves — beneficiary, not faction agent"

      # === aemond-targaryen-122ac (world-embodiment:opposite-number; 12 axes) ===
      # position-world: static 8→8 (coercive ceiling, not consolidation-arc carrier).
      # All other axes: not-applicable with "IS elite" / "instrument-not-carrier" rationale.

      - actor: aemond-targaryen-122ac
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior accounting; Aemond is the embodied consequence of Otto's proposals, not a carrier of the anti-instrumentalization framework"

      - actor: aemond-targaryen-122ac
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment; Aemond's capability (Vhagar bond) is not this axis"

      - actor: aemond-targaryen-122ac
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Aemond's court position is birthright, not a rise trajectory on this axis"

      - actor: aemond-targaryen-122ac
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Aemond does not lose position at d14 — he is the agent of Taylor's collapse, not a collapse carrier"

      - actor: aemond-targaryen-122ac
        axis: relational_anchor_status
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's un-priced anchor; Aemond has no un-priced relational anchor function in this framework"

      - actor: aemond-targaryen-122ac
        axis: moral_legibility_to_self
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's self-accounting; Aemond is 12 and Otto-directed; he does not carry a moral self-accounting arc in this project"

      - actor: aemond-targaryen-122ac
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance TOWARD the Westerosi elite; Aemond IS elite (Targaryen prince, Vhagar rider) — he does not carry a register-toward-elite position"

      - actor: aemond-targaryen-122ac
        axis: social_tether-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's relational tether in KL; Aemond's dynastic institutional ties are birthright, not a tether-rise arc on this axis"

      - actor: aemond-targaryen-122ac
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Aemond does not lose tether at d14 — he is the instrument of Taylor's severance"

      - actor: aemond-targaryen-122ac
        axis: social_tether-antag
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Otto's leverage over Taylor specifically; Aemond is a coercive instrument within Otto's apparatus, not a leverage-over-Taylor carrier in his own right"

      - actor: aemond-targaryen-122ac
        axis: position-world
        applicability: static
        start_rank: 8
        end_rank: 8
        source: inferred-from-role-card
        notes: "JUDGMENT-CALL-ACCEPTED: axis tracks Green-faction institutional consolidation; Aemond IS the Green faction's coercive enforcement instrument — already at high institutional rank (Vhagar, Targaryen prince); position does not rise because he starts at the coercive ceiling; static at 8"

      - actor: aemond-targaryen-122ac
        axis: political_register-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction succession position secured; Aemond IS the Green faction's coercive arm — he does not carry a register-toward-Green position; the axis tracks the institutional achievement, not the instrument embodying it"

      # === alicent-hightower-122ac (world-embodiment:green-faction-institution; 12 axes) ===
      # Primary carriers: position-world and political_register-world (lifted from state_axes).
      # IS elite — political_register-prot not-applicable.
      # All protagonist-interior and Taylor-tether axes: not-applicable.

      - actor: alicent-hightower-122ac
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior anti-instrumentalization accounting; Alicent's own moral framework is the Faith-register but is not this axis"

      - actor: alicent-hightower-122ac
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment; Alicent has no capability arc in this framework"

      - actor: alicent-hightower-122ac
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Alicent's court position is Queen Consort, birthright-adjacent — not a rise arc on this axis"

      - actor: alicent-hightower-122ac
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Alicent does not collapse at d14 — the Green faction's consolidation holds through the project end"

      - actor: alicent-hightower-122ac
        axis: relational_anchor_status
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's un-priced relational anchor; Alicent has no function in this framework's anchor machinery"

      - actor: alicent-hightower-122ac
        axis: moral_legibility_to_self
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's self-accounting; Alicent is observable through compound eyes only; her self-accounting is off-axis"

      - actor: alicent-hightower-122ac
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance TOWARD the Westerosi elite; Alicent IS the institutional face of the Westerosi elite — she does not carry a register-toward position"

      - actor: alicent-hightower-122ac
        axis: social_tether-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's KL tether; Alicent's household IS the institution Taylor is tethering to, not a parallel tether-position carrier"

      - actor: alicent-hightower-122ac
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Alicent does not lose tether — the apparatus she heads survives Taylor's expulsion"

      - actor: alicent-hightower-122ac
        axis: social_tether-antag
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Otto's leverage over Taylor specifically; Alicent is the household-anchor of the Green faction architecture but not a leverage-over-Taylor carrier"

      - actor: alicent-hightower-122ac
        axis: position-world
        applicability: moves
        start_rank: 5
        end_rank: 9
        source: lifted-from-state-axes
        notes: "primary carrier alongside Otto; the consolidation is performed in her name and through her household; matches state_axes[].{start_rank,end_rank}"

      - actor: alicent-hightower-122ac
        axis: political_register-world
        applicability: moves
        start_rank: 5
        end_rank: 9
        source: lifted-from-state-axes
        notes: "primary carrier; institutional Green-faction face; the succession position Taylor despises is Alicent's position made concrete; matches state_axes[].{start_rank,end_rank}"

      # === criston-cole-122ac (world-embodiment:faction-violence-instrument; 12 axes) ===
      # position-world: static 8→8 (enforcement-instrument standing, not consolidation-arc carrier).
      # All other axes: not-applicable — observable as operational aftermath only.

      - actor: criston-cole-122ac
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "operational-output observable only; his moral framework is fully subsumed into institutional identity and is not an arc in this project"

      - actor: criston-cole-122ac
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment; Criston's enforcement capability is not this axis"

      - actor: criston-cole-122ac
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Criston is the enforcement arm of the institution, not a court-position-rise carrier"

      - actor: criston-cole-122ac
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Criston enacts the Green faction's enforcement at d14 but does not himself collapse"

      - actor: criston-cole-122ac
        axis: relational_anchor_status
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's un-priced anchor; Criston has no relational-anchor function; cast_roster note flags him as relational_anchor_status indirect but this refers to his operations threatening Wren's street-safety, not a position he carries"

      - actor: criston-cole-122ac
        axis: moral_legibility_to_self
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's self-accounting; Criston's self-accounting has been fully converted to institutional identity; he carries no moral-legibility arc visible in this project"

      - actor: criston-cole-122ac
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance TOWARD the elite; Criston IS the enforcement arm of the elite institution; he does not carry a register-toward position"

      - actor: criston-cole-122ac
        axis: social_tether-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's KL tether; Criston's Kingsguard institutional position is not a tether-rise arc"

      - actor: criston-cole-122ac
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Criston executes enforcement at d14 but does not lose his own tether"

      - actor: criston-cole-122ac
        axis: social_tether-antag
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Otto's leverage over Taylor; Criston is three tiers below Otto in practice and is not a leverage-position carrier"

      - actor: criston-cole-122ac
        axis: position-world
        applicability: static
        start_rank: 8
        end_rank: 8
        source: inferred-from-role-card
        notes: "JUDGMENT-CALL-ACCEPTED: Kingsguard Lord Commander; enacts Green-faction consolidation as operational output but does not himself rise in position-world terms; standing stable at high enforcement rank throughout"

      - actor: criston-cole-122ac
        axis: political_register-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction succession position secured; Criston is the enforcement instrument that makes consolidation operative, not a succession-position carrier; he enacts, he does not hold"

      # === rhaenyra-targaryen-122ac (world-embodiment:black-faction-claimant; 12 axes) ===
      # position-world / political_register-world: moves INVERTED CARRIER — as Green rises 5→9, Rhaenyra's claimant position is foreclosed 7→2.
      # All protagonist-interior + Taylor-tether axes: not-applicable.

      - actor: rhaenyra-targaryen-122ac
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior accounting; Rhaenyra does not know Taylor exists and carries no position on this axis"

      - actor: rhaenyra-targaryen-122ac
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment; Rhaenyra has no capability arc in this framework"

      - actor: rhaenyra-targaryen-122ac
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Rhaenyra's position is at Dragonstone — a distinct standing arc not tracked on this axis"

      - actor: rhaenyra-targaryen-122ac
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Rhaenyra's claimant foreclosure is tracked under position-world (inverted) — not this axis"

      - actor: rhaenyra-targaryen-122ac
        axis: relational_anchor_status
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's un-priced anchor; Rhaenyra has no function in the anchor machinery"

      - actor: rhaenyra-targaryen-122ac
        axis: moral_legibility_to_self
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's self-accounting; Rhaenyra has no self-accounting arc visible to Taylor's project scope"

      - actor: rhaenyra-targaryen-122ac
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance toward the elite; Rhaenyra IS the claimant — she does not carry a register-toward-elite position"

      - actor: rhaenyra-targaryen-122ac
        axis: social_tether-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's KL tether; Rhaenyra is at Dragonstone with no KL-tether arc on this axis"

      - actor: rhaenyra-targaryen-122ac
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Rhaenyra's faction position erodes through a distinct mechanism not captured here"

      - actor: rhaenyra-targaryen-122ac
        axis: social_tether-antag
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Otto's leverage over Taylor; Rhaenyra has no function in the Otto–Taylor leverage machinery"

      - actor: rhaenyra-targaryen-122ac
        axis: position-world
        applicability: moves
        start_rank: 7
        end_rank: 2
        source: inferred-from-role-card
        notes: "JUDGMENT-CALL-ACCEPTED-INVERTED-CARRIER: axis tracks Green-faction consolidation rising (5→9); Rhaenyra's claimant position is the inverse — live claim at story-open (rank 7: heir named, Viserys holding the question), foreclosed to near-structural-loss by d14 (rank 2: Green apparatus locked, Dragonstone position isolated); road-not-taken irony requires foreclosure to be tracked, not background"

      - actor: rhaenyra-targaryen-122ac
        axis: political_register-world
        applicability: moves
        start_rank: 7
        end_rank: 2
        source: inferred-from-role-card
        notes: "JUDGMENT-CALL-ACCEPTED-INVERTED-CARRIER: axis tracks Green succession position secured (5→9); Rhaenyra's succession register is the opposing pole — viable claim at story-open, foreclosed through d14 as Green apparatus locks the council; active Dragonstone agenda makes this a live irony, not passive background"

      # === oswyn-mudway-flea-bottom-elder (supporting:Flea-Bottom-ward-network-anchor; 12 axes) ===
      # No axis primary carrier. Acts 1-2 tapering presence.
      # social_tether-prot-rise: static (substrate Taylor builds on, not himself an arc).
      # All other axes: not-applicable.

      - actor: oswyn-mudway-flea-bottom-elder
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior accounting; Oswyn is a ward-network substrate who does not know he is inside a coverage architecture; no position on this axis"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment; Oswyn's ward-knowledge is ground-layer substrate, not this axis"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Oswyn has no court position and no standing arc — fixture of Flea Bottom only"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Oswyn does not collapse — he is a Flea Bottom fixture throughout"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: relational_anchor_status
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's un-priced anchor (Wren); Oswyn is a ground-layer contact, not the un-priced relational anchor"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: moral_legibility_to_self
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's self-accounting; Oswyn has no moral-legibility arc — he does not know he is inside the architecture"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance toward the elite; Oswyn has no court register — his world is ward-scale, not succession-scale"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: social_tether-prot-rise
        applicability: static
        start_rank: 3
        end_rank: 3
        source: inferred-from-role-card
        notes: "ward-network anchor that constitutes the ground layer of Taylor's social tether; his own standing does not rise — stable-fixture throughout; static at 3 (ground-level embedded; not patron-adjacent); his position is the substrate, Taylor's tether moves on top of it"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Oswyn remains in Flea Bottom and does not experience the tether collapse — the collapse is Taylor's, not his"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: social_tether-antag
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Otto's leverage over Taylor; Oswyn is entirely outside the patron-lever machinery"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: position-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction institutional consolidation; Oswyn has no participation in the faction machinery — ward-network substrate at Flea Bottom scale"

      - actor: oswyn-mudway-flea-bottom-elder
        axis: political_register-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction succession position; Oswyn has no succession-scale awareness or function"

      # === jarvis-coin-kl-courier (supporting:Otto-courier-adjacent; 12 axes) ===
      # Structural vector for social_tether-antag and social_tether-prot-rise; moral_framework made material.
      # social_tether-prot-rise and social_tether-antag: static (conduit, not position-holder).
      # All other axes: not-applicable.

      - actor: jarvis-coin-kl-courier
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior accounting; Jarvis is the moral_framework-made-material vector — the exchange is the accounting event, not a position he carries"

      - actor: jarvis-coin-kl-courier
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment; Jarvis is the delivery conduit, not a capability carrier"

      - actor: jarvis-coin-kl-courier
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Jarvis is a courier-tier operative with no court position"

      - actor: jarvis-coin-kl-courier
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Jarvis recedes from the narrative before d14 and does not carry a collapse position"

      - actor: jarvis-coin-kl-courier
        axis: relational_anchor_status
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's un-priced anchor; Jarvis is a transactional contact with no relational-anchor function"

      - actor: jarvis-coin-kl-courier
        axis: moral_legibility_to_self
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's self-accounting; Jarvis has no moral-legibility arc — transactional flat-affect throughout"

      - actor: jarvis-coin-kl-courier
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance toward the elite; Jarvis is lower-city origin with no court-register investment"

      - actor: jarvis-coin-kl-courier
        axis: social_tether-prot-rise
        applicability: static
        start_rank: 2
        end_rank: 2
        source: inferred-from-role-card
        notes: "structural vector through which Taylor's social tether passes upward toward Otto; Jarvis's own position is flat-transactional throughout acts 1-2; static at 2 — present in the tether architecture without himself being a tether carrier; recedes to absent by act 3"

      - actor: jarvis-coin-kl-courier
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Jarvis is receding/absent in act 3 — not a tether-collapse carrier"

      - actor: jarvis-coin-kl-courier
        axis: social_tether-antag
        applicability: static
        start_rank: 2
        end_rank: 2
        source: inferred-from-role-card
        notes: "structural vector through which Otto's leverage over Taylor transmits at the exchange layer; Jarvis's own position in the leverage machinery is flat — conduit, not leverage-holder; static at 2; recedes to absent by act 3"

      - actor: jarvis-coin-kl-courier
        axis: position-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction institutional consolidation; Jarvis is three tiers below the faction intelligence structure and has no participation in the consolidation machinery"

      - actor: jarvis-coin-kl-courier
        axis: political_register-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction succession position; Jarvis does not know the Green faction exists as a faction; no position on this axis"

      # === septon-halvard-flea-bottom (supporting:naive-idealist-foil; 12 axes) ===
      # moral_legibility_to_self mirror: static 7→7 (own legibility stable by design; the contrast with Taylor).
      # All other axes: not-applicable.

      - actor: septon-halvard-flea-bottom
        axis: moral_framework
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis is Taylor's interior accounting; Halvard has his own moral framework (principled-slower Faith register) but it is not the anti-instrumentalization arc tracked by this axis"

      - actor: septon-halvard-flea-bottom
        axis: capability
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's insect-network deployment; Halvard has no capability arc in this framework"

      - actor: septon-halvard-flea-bottom
        axis: position-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's court-position rise; Halvard has no court position — minor precinct septon only"

      - actor: septon-halvard-flea-bottom
        axis: position-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's position collapse; Halvard does not collapse — still present at d14 in the precinct"

      - actor: septon-halvard-flea-bottom
        axis: relational_anchor_status
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's un-priced anchor (Wren); Halvard has no un-priced-anchor function"

      - actor: septon-halvard-flea-bottom
        axis: moral_legibility_to_self
        applicability: static
        start_rank: 7
        end_rank: 7
        source: inferred-from-role-card
        notes: "the moral-legibility mirror; own legibility to himself is stable by design — principled-slower, names wrong acts without suppressing recognition; static at 7 (honest self-accounting, not full 9 because he acknowledges the cost of his slower method and its death-toll); contrast with Taylor's non-linear rise is the load-bearing structural juxtaposition"

      - actor: septon-halvard-flea-bottom
        axis: political_register-prot
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's stance toward the elite; Halvard has no succession-register investment — scale is Flea Bottom precinct, not court"

      - actor: septon-halvard-flea-bottom
        axis: social_tether-prot-rise
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's KL tether; Halvard's presence is Flea Bottom precinct — not a component of Taylor's court-adjacent tether architecture"

      - actor: septon-halvard-flea-bottom
        axis: social_tether-prot-collapse
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Taylor's tether collapse; Halvard is still present at d14 — does not experience the tether collapse"

      - actor: septon-halvard-flea-bottom
        axis: social_tether-antag
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Otto's leverage over Taylor; Halvard has no participation in the patron-leverage machinery"

      - actor: septon-halvard-flea-bottom
        axis: position-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction institutional consolidation; Halvard is a minor precinct septon with no participation in the faction machinery"

      - actor: septon-halvard-flea-bottom
        axis: political_register-world
        applicability: not-applicable
        start_rank: null
        end_rank: null
        source: inferred-from-role-card
        notes: "axis tracks Green-faction succession position; Halvard does not calculate the succession — scale is the sick and dying in the Hook"


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
    # /and-substance book b01 Phase 6 — persist 2026-05-24; Phase 5 attempts: 1 REVISE (7 HARD) → 2 REVISE (1 NEW HARD) → 3 ACCEPT.
    # Draft archived: active-project/staff/showrunner/_drafts/b01-draft-2026-05-24.md
    # Reviewer reports: cape-fic-reader/stm.md, dark-fantasy-reader/stm.md, worm-canon-pedant/stm.md (audience),
    #                   b01-dramatist-review.md + b01-dramatist-review-attempt-2.md (dramatist),
    #                   b01-audit.md + b01-audit-attempt-2.md + b01-audit-attempt-3.md (auditor).
    # All 12 axes within ±1 tolerance (10 EXACT + 2 WITHIN). All 9 ledger entries balanced.
    # Soft findings outstanding for /and-write: SOFT-CURVE-moral_framework (6 uniform drops vs trajectory's 3 concentrated); 8 INFERENTIAL-ANCHOR / NAMING-INCONSISTENCY (non-blocking).
    drama: |
      What cannot survive this book is the distinction between atonement and repetition.
      Taylor arrives in King's Landing with the prohibition intact and operationally enforced —
      every insect held at subsistence range, every act of direction refused on principle —
      and leaves it with a surveillance architecture that threads every ward she mapped,
      reads every body she could not name, and routes calibrated intelligence to a faction
      she has come to despise with full, articulate clarity. The structural collision is this:
      the prohibition does not break under pressure from outside. It dissolves from inside,
      one sanctioned exception at a time, each exception priced against a specific protection,
      each price recorded in a ledger Taylor runs with more honesty than any alternative she
      considered. The ledger is the catastrophe. The accuracy of the trades is what makes
      the recognition at the end irrevocable — she cannot claim ignorance, cannot claim
      coercion, cannot claim the alternative would have been better. She can only read the
      final entry: the un-priced item, the one she refused to enter into the calculus, is the
      one the calculus came for. The atonement was the repetition. The contempt arrived
      accurate and complete. Nothing remained to refuse.

    chapters:
      - slug: b01c01
        status: audited-r1
        chunk: |
          Taylor has been in King's Landing for three weeks, sleeping in a Flea Bottom alley
          and holding her insects at subsistence range by effort of will. When a ward child
          collapses in a crowd — fever, not violence — Taylor intervenes using insect-sense to
          clear the crowd's pressure and read the child's symptoms without touching her. The
          intervention works. It is witnessed. The witch-label formation process begins in the
          precinct: a foreign woman who moved a crowd with her hands open, who knew where the
          sick child was before anyone told her. Wren, a stitch-maker two lanes over, is in the
          crowd. She and Taylor do not speak. What shifts: Taylor's first capability deployment
          is behind her, the prohibition has its first crack — not broken, merely exercised —
          and the ward now has a category for her that did not exist at dawn.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: capability
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl01a
              notes: "first insect deployment since arrival; crowd-read + symptom-read; subsistence range exceeded briefly; cl01a gain side"
            - axis: social_tether-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl01b
              notes: "rescue witnessed = first ward-embedding; Oswyn present in crowd; tether starts forming; cl01b gain side"
          axes_held:
            - axis: moral_framework
              rationale: "prohibition not yet licensed; the deployment was instinctual not calculated; crack visible only in retrospect — no rationalization scene yet"
            - axis: relational_anchor_status
              rationale: "Wren present but not in any calculus; anchor noticed only by the reader; Taylor has not registered her as a contact"
            - axis: political_register-prot
              rationale: "no insect-feed court content yet; Taylor not yet reading the power layer; resentment has no material to form on"
            - axis: moral_legibility_to_self
              rationale: "Taylor reads the intervention as a one-time lapse, not a pattern; self-accounting has not opened yet"
          density_target: 0.5-0.7
          chapter_class: standard
        dramatic_shape: rising
        goal: |
          Show the audience Taylor's first act of control in King's Landing — the instinct that survives every prohibition — and plant the witch-label and Wren's presence before either becomes legible as costs.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "Taylor has been surviving subsistence-anonymous in Flea Bottom for three weeks with no contacts and no plan"
            - "prohibition intact: insects held at minimum range; no systematic reading conducted"
          world_state:
            - "KL 122 AC; Viserys I on the throne; Rhaenyra named heir but claim contested informally"
            - "Otto Hightower off the Small Council but operational in KL, running informal intelligence through household contacts"
            - "Flea Bottom: Hook precinct anchored by Oswyn Mudway's ward network; Septon Halvard's sept the neighborhood institutional node"
            - "Green faction dominant informally; no formal Taylor-awareness at any court tier"
          character_state:
            - "Taylor: prohibition intact; capability suppressed at rank 2; no court position (rank 1); no Otto contact; no Wren contact; no coin above subsistence"
            - "Wren: stitch-maker in Hook precinct, ward-status rank 1; no Taylor awareness"
            - "Otto: leverage rank 1 (Taylor unknown to him); network active but Flea Bottom intel layer absent"
            - "Sera: in Alicent's household; legitimacy-lever latent; not yet under threat"
            - "Aemond: 12 years old, Vhagar-bonded, off-stage"
            - "Alicent: Queen Consort, Green-faction rank 5 institutional standing"
          source_chapter: null
        handoff_out:
          open_threads:
            - "witch-label formation active in Hook precinct: foreign woman reads bodies without contact"
            - "Wren has seen Taylor's face in the crowd; no exchange, no names"
            - "Oswyn Mudway observed the intervention; Taylor on his ward-elder awareness layer"
            - "capability has moved: first deployment is behind Taylor; the prohibition's first crack is unacknowledged"
          world_state:
            - "KL 122 AC; Flea Bottom Hook precinct now has a category for Taylor: known-unknown-witch-adjacent"
            - "Otto Hightower unaware; no court-tier awareness of Taylor"
          character_state:
            - "Taylor: capability rank 3 (one deployment); prohibition intact but cracked; no court position; no patron contact; social tether starting (Oswyn-layer)"
            - "Wren: has seen Taylor; no contact; no named awareness"
            - "Oswyn: Taylor on his observation layer; not yet an active contact"
          target_chapter: b01c02
        # /and-substance chapter b01c01 Phase 6 — persist 2026-05-25; Phase 5 attempts: 1 REVISE (1 HARD: cl01b ledger partial-settle) → 2 ACCEPT (fixer notation fix).
        # Draft archived: active-project/staff/showrunner/_drafts/b01c01-draft-2026-05-25.md
        # Reviewer reports: cape-fic-reader/stm.md, dark-fantasy-reader/stm.md, worm-canon-pedant/stm.md (audience trio: 3-of-3 ACCEPT, SUBSTANCE-FELT all 9 cells);
        #                   dramatist inline ACCEPT (all 7 checks PASS); auditor b01c01-scenes-audit-2026-05-25.md (attempt 1 REVISE → attempt 2 CLEARED).
        # Roll-up: capability +1.0 exact; social_tether-prot-rise +1.0 exact (vs chapter targets).
        # DOWNSTREAM-WATCH (carried to /and-substance chapter b01c03): b01c03 chapter contract should add social_tether-prot-rise +1.0 to axes_in_motion with cost_ledger_anchor: cl01b (court-layer half — Otto's awareness of the rescue via Jarvis Coin closes the cl01b +2 tether-embedding loop).
        # SOFT-WATCH (carried to /and-write b01c01): audience trio flagged Wren stitch-house plant needs prose texture — sensory signal (smell, two lanes over, not-looked-at) must land as quietly loaded, not background noise.
        scenes:
          - slug: b01c01s01
            chunk: |
              Three weeks in Flea Bottom and Taylor has learned the specific weight
              of doing nothing. She sleeps in a covered angle of the Hook where the
              water runs under a broken drain and the insects are thick enough that
              holding them at the edge of her range is work — not labor, not strain,
              but the kind of constant small expenditure that makes stillness
              expensive. She has a count: how far the range extends before the
              sensation sharpens from background to pull. She holds the line there.
              The ward is a noise she reads only at its surfaces: bodies moving in
              the alley, the weight of foot traffic on the uneven stones, the smell
              of tallow smoke from the stitch-house two lanes over. She does not
              read deeper than she has to. The prohibition is the only thing she
              brought from home that still works — that she keeps choosing it each
              morning is the argument she makes to herself that the rest of it was
              not for nothing. The ward does not know her name. She does not know
              any name in the ward. This is the arrangement, and it holds, and it
              costs what it costs.
            substance_delta:
              axes_in_motion: []
              axes_held:
                - axis: moral_framework
                  rationale: "prohibition fully operative; Taylor actively pays the daily cost of holding insects at subsistence range; the scene's tension is the effortful maintenance of the prohibition, not a test of it"
                - axis: capability
                  rationale: "suppressed by discipline, not incapacity; range-awareness is established here so the scene 2 deployment reads as a choice breaking a maintained threshold, not an unconscious reflex"
                - axis: relational_anchor_status
                  rationale: "Wren's stitch-house is two lanes over; Taylor registers it as a smell-and-sound fact, not a person; the anchor begins its presence before Taylor has a name to attach to it"
                - axis: moral_legibility_to_self
                  rationale: "self-accounting is running (Taylor argues the prohibition to herself each morning) but no new entry — she is not yet in a situation; the accounting is maintenance, not reckoning"
                - axis: political_register-prot
                  rationale: "no court content; no insect-feed beyond alley density; resentment has nothing to form on; held at structural baseline rank 1"
                - axis: social_tether-prot-rise
                  rationale: "anonymity intact; tether axis starts at nil and this scene confirms nil — no one in the ward yet has a name for her, which is the arrangement"
              density_target: 0.6-0.7
            scene_conflict:
              protagonist_force: "Taylor holds the prohibition against the sustained pull of the insects at the edge of her range"
              opposing_force: "the physical difficulty of suppression in a ward dense with bodies and signal — three weeks of it, every morning"
              stakes_axis: moral_framework
            stale_since: null
            # /and-write Phase 7 emit 2026-05-25 — bones authored, event_map persisted, bone-gate PASS.
            event_map:
              - event: "Taylor sleeping in the covered drain angle (opening location placement)"
                bones: [b01c01s01n01, b01c01s01n06]
                omission_rationale: null
              - event: "insects held at subsistence range (the count; the work of suppression)"
                bones: [b01c01s01n03, b01c01s01n04]
                omission_rationale: null
              - event: "ward read only at surfaces — bodies moving, foot traffic, smell"
                bones: [b01c01s01n02, b01c01s01n07]
                omission_rationale: null
              - event: "stitch-house smell two lanes over (Wren plant; relational_anchor dormancy)"
                bones: [b01c01s01n02]
                omission_rationale: null
              - event: "prohibition-maintenance: Taylor holds the prohibition each morning as the argument she makes to herself"
                bones: [b01c01s01n07]
                omission_rationale: null
              - event: "protagonist_force: Taylor holds the prohibition against the sustained pull of the insects at the edge of her range"
                bones: [b01c01s01n03, b01c01s01n04]
                omission_rationale: null
              - event: "opposing_force: three weeks of accumulated suppression work; physical difficulty of holding in a ward dense with bodies"
                bones: [b01c01s01n04, b01c01s01n07]
                omission_rationale: null
              - event: "ward anonymity: the ward does not know her name"
                bones: [b01c01s01n01, b01c01s01n06]
                omission_rationale: null
            bones:
              - slug: b01c01s01n01
                flat_id: 1
                svo: "the drain water threads the angle-gap"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "Taylor sleeps in the drain angle — the most anonymous possible position in the ward; anonymity enacted by the physical location itself; no name anyone will remember"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s01n02
                flat_id: 2
                svo: "the tallow smoke crosses the stitch-house lane"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: relational_anchor_status
                      rationale: "the stitch-house smell is a physical fact Taylor registers at surfaces only — anchor present as environmental datum, not as a person; the cost-bearer's location is real before it is named"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s01n03
                flat_id: 3
                svo: "taylor-hebert-kl-122ac holds the feet"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: capability
                      rationale: "stillness-against-pull — Taylor's feet planted while the insect-range pulls toward the ward's bodies; suppression by discipline, not incapacity; range-awareness established as a chosen threshold"
                    - axis: moral_framework
                      rationale: "the prohibition enacted as physical stillness; Taylor paying the daily suppression cost; the effortful maintenance is what makes the scene's tension the prohibition itself"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s01n04
                flat_id: 4
                svo: "the insects swell"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: capability
                      rationale: "opposing-force enacted: the insect-pull at the range-threshold is the physical pressure Taylor's discipline holds against; the sensation sharpens from background to pull at this distance"
                    - axis: moral_framework
                      rationale: "the pull is the test the prohibition passes each time; enacts the opposing force — the physical difficulty of suppression in a ward dense with bodies"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              # b01c01s01n05 dropped at Pass 2 round 1 (FAULT-FORM-PERCEPTION; perception-surrogate in solo scene; no honest non-perception recast available); political_register-prot held rationale relocated to s01n07 as its third axes_held entry.
              - slug: b01c01s01n06
                flat_id: 5
                svo: "the angle-wall narrows the lane"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "the physical geometry of the drain angle is what anonymity looks like: a body-sized space between wall and drain; the cobbles are the ward's indifference concretized; the arrangement holds because the space holds"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s01n07
                flat_id: 6
                svo: "taylor-hebert-kl-122ac exhales"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_legibility_to_self
                      rationale: "the morning argument: the exhalation is the body's verdict on another day of choosing the prohibition; self-accounting runs as maintenance, not reckoning — she is not yet in a situation"
                    - axis: moral_framework
                      rationale: "the prohibition survives the morning; the choosing-each-morning is the argument she makes to herself; no new ledger entry, only continuation"
                    - axis: political_register-prot
                      rationale: "[relocated from s01n05 — FAULT-FORM-PERCEPTION drop] Taylor holds the ward-read at structural baseline rank 1; the ward is smallfolk-only; no court-layer material enters the drain angle; no insect-feed content for resentment to form on; the exhalation closes the morning scan without a court-encounter"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [ACCEPT-axes-held-overage-repair-move] }

          - slug: b01c01s02
            chunk: |
              The crowd that forms around the collapsed child does what crowds do:
              it compresses. Pressure from the lane-mouth, rubberneckers blocking
              the upper alley, a halted fish-cart crosswise. The child is five
              strides deep in it when Taylor arrives — not because she ran to the
              scene but because the insects already had it. The child's breathing
              she reads through the ground before she reaches her. Fever; not the
              croup-rattle that takes them in under a week; not a blow to the head.
              The crowd is what will kill her if it does not move: body heat
              stacking, air going foul, the child too flat to call out. Taylor does
              not make a decision, or if she does she does not file it as one. The
              insects move. The nearest dozen bodies get the sensation of something
              at ankle-height and yield a step each inward; the ones behind feel
              the gap and fill it wrong. She reads the shape of the crowd and presses
              at the perimeter until the gap propagates outward. Thirty seconds,
              maybe less. By the time she is beside the child the crowd has a lane
              through it that was not there before, and Taylor is the foreign woman
              who made the opening with her hands up and her mouth shut. She is not
              touching anyone. She is not touching the child. She gives the people
              near the child the same information she already has — fever, not dying,
              needs air and water and someone whose name she knows — and uses a voice
              that does not ask whether they will comply. The child breathes. The
              crowd does not re-compress. Taylor has already crossed the line she
              came here to maintain and has not yet noticed she is on the other side.
            substance_delta:
              axes_in_motion:
                - axis: capability
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl01a
                  notes: "first deployment since arrival; subsistence range exceeded — insects move bodies in a crowd; gain side of cl01a; deployment is instinctual not calculated, which is both the rescue's mechanism and its ledger-entry problem"
              axes_held:
                - axis: moral_framework
                  rationale: "the prohibition is cracked but the crack is not yet legible to Taylor — she does not file the deployment as a violation; held because the self-accounting has not opened; the stakes of the rescue scene are whether the prohibition survives instinct, and here it does not, but Taylor has not yet processed this"
                - axis: relational_anchor_status
                  rationale: "Wren is in this crowd; Taylor does not know that; anchor is present-but-unregistered; held as structural dormancy — cost-bearer in the frame, absent from the calculus"
                - axis: moral_legibility_to_self
                  rationale: "the accounting has not run on this event yet; Taylor reads the deployment as a one-time lapse; the scene ends before the ledger opens"
                - axis: political_register-prot
                  rationale: "no court content; smallfolk crowd only; no material for resentment to form on; held at baseline"
                - axis: social_tether-prot-rise
                  rationale: "witnesses are present but the ward-embedding has not yet registered; tether does not move until the aftermath scene, when Oswyn's awareness layer receives Taylor's presence and the category-shift begins"
              density_target: 0.75-0.9
            scene_conflict:
              protagonist_force: "Taylor clears the crowd-pressure around the collapsed child using insect-sense, keeping the child alive"
              opposing_force: "the crowd's compression, and underneath it, the prohibition against deploying insect-control on unconsenting persons"
              stakes_axis: moral_framework
            stale_since: null
            # /and-write Phase 7 emit 2026-05-25 — Phase 3 dramatist reorder applied: n11 (voice; enabling act) precedes n10 (hands; closing visual the witnesses file) per chunk crowd-image "hands up and mouth shut".
            event_map:
              - event: "child collapses in crowd (the initiating event)"
                bones: [b01c01s02n02, b01c01s02n03]
                omission_rationale: null
              - event: "crowd compression around the child (the physical danger mechanism)"
                bones: [b01c01s02n01, b01c01s02n03, b01c01s02n05]
                omission_rationale: null
              - event: "fever-read without contact (the capability deployed)"
                bones: [b01c01s02n02, b01c01s02n06]
                omission_rationale: null
              - event: "insect deployment — crowd-yield (the central action)"
                bones: [b01c01s02n06, b01c01s02n07, b01c01s02n08]
                omission_rationale: null
              - event: "Taylor arrives at the child (physical approach through the gap)"
                bones: [b01c01s02n08, b01c01s02n09]
                omission_rationale: null
              - event: "voice-of-instruction (Taylor speaks to the crowd-adjacent persons)"
                bones: [b01c01s02n11]
                omission_rationale: null
              - event: "child breathes (the rescue succeeds)"
                bones: [b01c01s02n02, b01c01s02n07]
                omission_rationale: "The child-breathing outcome is carried as consequence of the crowd-yield and the fever-read bones; no additional bone is needed since the mechanism (gap propagates; crowd does not re-compress) is already the child breathing — adding a 'the child breathes' bone would double-count the causal chain. Omission deliberate."
              - event: "crowd-lane stays open after the yield"
                bones: [b01c01s02n08, b01c01s02n10]
                omission_rationale: null
              - event: "protagonist_force: Taylor clears crowd-pressure using insect-sense"
                bones: [b01c01s02n06, b01c01s02n07, b01c01s02n08]
                omission_rationale: null
              - event: "opposing_force: crowd compression + the prohibition against deploying insect-control on unconsenting persons"
                bones: [b01c01s02n03, b01c01s02n04]
                omission_rationale: null
              - event: "load-bearing image: fish-cart crosswise in the lane-mouth"
                bones: [b01c01s02n01]
                omission_rationale: null
              - event: "load-bearing image: ankle-height insect sensation at the crowd-floor"
                bones: [b01c01s02n06]
                omission_rationale: null
              - event: "Taylor visible as the foreign woman who opened the crowd with hands up and mouth shut"
                bones: [b01c01s02n10, b01c01s02n11]
                omission_rationale: null
            bones:
              - slug: b01c01s02n01
                flat_id: 7
                svo: "the fish-cart blocks the lane"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "the cart-blockage is the ward's compression reading — smallfolk crowd physics enacted in the geometry of a halted street; Taylor has no tether-embedding yet; the environment is the ward's indifference to her"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s02n02
                flat_id: 8
                svo: "the ground transmits the child's breath"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_framework
                      rationale: "the prohibition is intact at this bone — the insect-sense reads body-vibration through the cobbles as passive baseline perception, not active deployment; moral_framework held as not-yet-cracked; the sense-mechanism is doing its baseline work, which the prohibition has always permitted; the scene's tension is what happens when this baseline is exceeded, which has not happened yet at this bone"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s02n03
                flat_id: 9
                svo: "the crowd compresses"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_framework
                      rationale: "opposing-force enacted: the crowd-compression is the physical pressure the prohibition-against-using-insects-on-persons now runs against; the stakes are whether the prohibition survives crowd-mechanics; it does not"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s02n04
                flat_id: 10
                svo: "taylor-hebert-kl-122ac holds the feet"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_framework
                      rationale: "the last beat of prohibition-maintenance before the crack — Taylor's body planted, the range pressing, the prohibition still running; this is the prohibition's final held moment in the scene; the threshold-crossing at the next bone reads as a crossing because this bone holds the line right before it"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s02n05
                flat_id: 11
                svo: "the lane-mouth presses the crowd"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: political_register-prot
                      rationale: "the lane geometry is smallfolk-only pressure — no court material, no resentment source; held at baseline; the crowd-physics are entirely ward-layer"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s02n06
                flat_id: 12
                svo: "the insects propagate"
                substance_delta:
                  axis_moves:
                    - axis: capability
                      direction: up
                      magnitude: 1
                  axes_held: []
                  cost_ledger_anchor: cl01a
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s02n07
                flat_id: 13
                svo: "the nearest dozen bodies yield"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_framework
                      rationale: "the crack: bodies yield to insect-pressure without consenting to yield; the prohibition against directing others is crossed without being filed as crossed; moral_framework held as load-bearing dormancy — the crack is visible here to the reader, not to Taylor"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s02n08
                flat_id: 14
                svo: "the gap propagates"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_framework
                      rationale: "the crack continues — the deployment's wave-effect persists as the gap propagates outward, bodies continuing to yield to insect-pressure; the prohibition's violation extends beat-by-beat without being filed as violation; moral_framework held as load-bearing dormancy through the deployment's cascade"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s02n09
                flat_id: 15
                svo: "taylor-hebert-kl-122ac faces the child"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: relational_anchor_status
                      rationale: "Wren is in this crowd — the cost-bearer is in the frame as Taylor faces the child; anchor present-but-unregistered; Taylor does not turn toward the cost-bearer; anchor enacted as structural dormancy"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [ACCEPT-faces-mannerism-chapter-register] }
              # Phase 3 dramatist reorder: n11 precedes n10 in scene order (flat_id 16 vs 17).
              - slug: b01c01s02n11
                flat_id: 16
                svo: "taylor-hebert-kl-122ac raises the voice"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_legibility_to_self
                      rationale: "the voice-of-instruction is the deployment's final act; the accounting has not run on this event yet; Taylor reads the deployment as a one-time lapse; the scene ends before the ledger opens"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s02n10
                flat_id: 17
                svo: "taylor-hebert-kl-122ac lifts the hands"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "hands-up posture is the witness-facing gesture that makes Taylor visible as the opener-of-the-crowd; tether does not move here — witnesses are present but ward-embedding has not yet registered; this is the action the crowd sees"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }

          - slug: b01c01s03
            chunk: |
              The crowd disperses the way Flea Bottom crowds do after a thing has
              resolved — not quickly, and not all the way. There are holders: the
              man with the fish-cart who is watching Taylor rather than the child;
              two women from the upper alley who have not gone back yet. Oswyn
              Mudway, ward-elder, stitch-house side, does not disperse at all. He
              stands at the lane mouth and watches Taylor the way a man watches
              something he does not have a word for yet and is composing one. The
              child has been gathered by someone who knows her name. Taylor has done
              nothing medically useful by any standard she can articulate — she did
              not touch the child, did not give water, did not carry her inside.
              What she did was move the crowd and read a fever without contact. In
              the language available to a Flea Bottom ward in 122 AC, these are not
              separable from the third thing she did, which was know. The witch-label
              is not assembled loudly. It is assembled in the gap between what Oswyn
              saw and what he has a word for, and in the shift from foreign woman who
              helped to foreign woman who knew before anyone told her. Taylor
              registers Oswyn registering her. She does not interpret what is in his
              look because she does not have to — she reads bodies, and the body
              tells her she has moved from invisible to present in his accounting.
              The stitch-house smell is still there, two lanes over, the same it was
              this morning. Taylor does not look toward it. The ward now has a
              category for her that did not exist at dawn.
            substance_delta:
              axes_in_motion:
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl01b
                  notes: "rescue witnessed by Flea Bottom witnesses; Oswyn enters Taylor's awareness layer and Taylor enters his; ward-embedding begins; partial-settlement of cl01b (+1 of +2 gain; ward-layer half — Oswyn); remaining +1 (court-layer half — Otto via Jarvis Coin) anchors at b01c03 [DOWNSTREAM-WATCH: b01c03 chapter contract does not yet reflect this cl01b partial-anchor in axes_in_motion; surface to next /and-substance chapter b01c03 run]; journey-required cl01a already paid in scene 2"
              axes_held:
                - axis: moral_framework
                  rationale: "Taylor reads the intervention as a one-time pragmatic act; the prohibition's crack is visible only in retrospect to the reader; self-accounting has not opened on this event; moral framework held as load-bearing dormancy — the chapter goal specifies 'crack visible only in retrospect'"
                - axis: relational_anchor_status
                  rationale: "Wren is in the dispersing crowd; the stitch-house smell is named; Taylor does not look toward it; anchor held as structural dormancy — visible to the reader, absent from Taylor's calculus; the chapter goal's second clause ('plant Wren's presence before it becomes legible as a cost') is enacted here"
                - axis: moral_legibility_to_self
                  rationale: "Taylor reads Oswyn's look but does not open the ledger on the deployment itself; the accounting is deferred; held"
                - axis: political_register-prot
                  rationale: "no court material; Oswyn's look is a ward-layer fact, not a court-layer fact; resentment held at baseline"
                - axis: capability
                  rationale: "capability moved in scene 2 and is now at its new floor; the aftermath scene confirms the deployment's visibility but does not extend it; no further deployment occurs"
              density_target: 0.65-0.8
            scene_conflict:
              protagonist_force: "Taylor reads the aftermath of her own intervention and attempts to remain invisible within it"
              opposing_force: "Oswyn Mudway's watching — the ward's process of categorizing her; the witch-label assembling in the gap between what was seen and what Flea Bottom has a word for"
              stakes_axis: social_tether-prot-rise
            stale_since: null
            # /and-write Phase 7 emit 2026-05-25 — s03n10 added at Phase 5 to deliver handoff_out "Wren has seen Taylor's face" cost-bearer plant.
            event_map:
              - event: "crowd disperses — holders remain (Flea Bottom dispersal physics)"
                bones: [b01c01s03n01, b01c01s03n02, b01c01s03n03]
                omission_rationale: null
              - event: "Oswyn Mudway stands at the lane-mouth and watches Taylor"
                bones: [b01c01s03n04, b01c01s03n09]
                omission_rationale: null
              - event: "child gathered by someone who knows her name (aftermath confirmed)"
                bones: [b01c01s03n05]
                omission_rationale: null
              - event: "witch-label assembly — the gap between what Oswyn saw and what Flea Bottom has a word for"
                bones: [b01c01s03n04, b01c01s03n09]
                omission_rationale: null
              - event: "Taylor registers Oswyn registering her (the mutual-awareness beat)"
                bones: [b01c01s03n04, b01c01s03n07]
                omission_rationale: null
              - event: "stitch-house smell still present — Taylor does not look toward it (Wren plant / ledger-anomaly enacted)"
                bones: [b01c01s03n07, b01c01s03n08, b01c01s03n10]
                omission_rationale: null
              - event: "ward now has a category for Taylor that did not exist at dawn"
                bones: [b01c01s03n04, b01c01s03n09]
                omission_rationale: null
              - event: "protagonist_force: Taylor reads the aftermath and attempts to remain invisible within it"
                bones: [b01c01s03n07, b01c01s03n05]
                omission_rationale: null
              - event: "opposing_force: Oswyn Mudway's watching; witch-label assembling in the gap"
                bones: [b01c01s03n04, b01c01s03n09]
                omission_rationale: null
              - event: "load-bearing image: Wren orients toward Taylor across the dispersing crowd (chapter-close cost-bearer plant)"
                bones: [b01c01s03n10]
                omission_rationale: null
            bones:
              - slug: b01c01s03n01
                flat_id: 18
                svo: "the crowd thins"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: political_register-prot
                      rationale: "the crowd thinning is smallfolk-only dispersal — no court material enters the scene; held at baseline; the aftermath physics are ward-layer exclusively"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s03n02
                flat_id: 19
                svo: "the fish-cart man faces taylor-hebert-kl-122ac"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "a holder watches Taylor instead of the child — early-stage witness attention, not yet ward-embedding; tether has not moved at this bone; the watching is the raw material of the label, not yet the label"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [ACCEPT-faces-mannerism-chapter-register] }
              - slug: b01c01s03n03
                flat_id: 20
                svo: "the two women face the lane"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "holders remain — multiple witnesses holding position after the resolution; the label's accumulation requires corroborating observers; this bone enacts the critical-mass condition before Oswyn's categorization"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [ACCEPT-faces-mannerism-chapter-register] }
              - slug: b01c01s03n04
                flat_id: 21
                svo: "oswyn-mudway-flea-bottom-elder takes the lane-mouth"
                substance_delta:
                  axis_moves:
                    - axis: social_tether-prot-rise
                      direction: up
                      magnitude: 1
                  axes_held: []
                  cost_ledger_anchor: cl01b
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s03n05
                flat_id: 22
                svo: "the child clears the lane"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: capability
                      rationale: "capability held at its new floor: the deployment succeeded; the child is gathered and gone; no further capability deployment occurs; aftermath confirms the deployment's visibility without extending it"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s03n06
                flat_id: 23
                svo: "the gap closes"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_framework
                      rationale: "the physical gap that the insect-deployment opened has closed — the lane has returned to neutral; the prohibition's crack is visible only in retrospect; the lane closing is the environment's indifference to the moral event that just occurred"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s03n07
                flat_id: 24
                svo: "taylor-hebert-kl-122ac faces the alley-mouth"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: relational_anchor_status
                      rationale: "facing the alley-mouth is the body-direction that excludes the stitch-house; the not-looking is enacted as a direction-toward, not as a negation; cost-bearer's location held as structural dormancy — Taylor does not look toward the anchor; the ledger-anomaly rule enacts here"
                    - axis: moral_legibility_to_self
                      rationale: "Taylor reads Oswyn's look and does not open the ledger on the deployment; she faces the alley rather than the stitch-house — the accounting is deferred in the same gesture"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [ACCEPT-faces-mannerism-chapter-register] }
              - slug: b01c01s03n08
                flat_id: 25
                svo: "the tallow smoke layers the lane-floor"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: relational_anchor_status
                      rationale: "the stitch-house smoke is still present — two lanes over, the same it was this morning; the cost-bearer's location marked again as a physical-sensory fact; quietly loaded, not announced; the continuity of the smell is the anchor's dormancy enacted concretely"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              - slug: b01c01s03n09
                flat_id: 26
                svo: "oswyn-mudway-flea-bottom-elder lifts the chin"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "Oswyn's chin-lift is the composing-of-the-word: the body telling Taylor she has moved from invisible to present in his accounting; the witch-label's assembly in the gap between what he saw and what he has a word for — the categorization completing"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [] }
              # s03n10 added at Phase 5 to honor handoff_out "Wren has seen Taylor's face in the crowd; no exchange, no names" — held bone, no axis movement, places the cost-bearer's perceptual orientation at chapter-close while preserving structural dormancy in Taylor's calculus (Taylor reads body-orientation; the slug identifies Wren to the reader only).
              - slug: b01c01s03n10
                flat_id: 27
                svo: "wren-stitch-maker-flea-bottom-ward faces taylor-hebert-kl-122ac"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: relational_anchor_status
                      rationale: "Wren's body-direction crosses the dispersing crowd and settles toward Taylor; Taylor's insect-sense reads the orientation as a stranger-body holding a facing she has no name for; the cost-bearer's perceptual presence is delivered to the reader (the slug identifies her) without entering Taylor's calculus (Taylor reads a body, not Wren); structural dormancy of the un-priced anchor enacted as orientation-without-recognition; the chapter goal's second-clause plant ('Wren's presence before it becomes legible as a cost') lands here"
                  cost_ledger_anchor: null
                gate_verdict: { bonefide: true, flat: false, signals: [ACCEPT-faces-mannerism-chapter-register] }

        # /and-write Phase 7 chapter-level emit fields — 2026-05-25
        bones_file: theater/bones/b01-c01.md
        bones_count: 27
        substance_bone_gate_verdict: PASS
        substance_delta_measured:
          axes_moved:
            - { axis: capability, direction: up, magnitude: 1.0, anchor_bone: b01c01s02n06, cost_ledger: cl01a }
            - { axis: social_tether-prot-rise, direction: up, magnitude: 1.0, anchor_bone: b01c01s03n04, cost_ledger: cl01b }
          density_measured: 1.0   # 0 chatter / 27 total — fully structural (all bones moving or held)
          felt_verdict: SUBSTANCE-FELT   # audience trio 3-of-3 SUBSTANCE-FELT on all three scenes (Phase 6 bone-gate)
        # Phase 7 emit notes:
        #   Pipeline cycles: Pass 2 (3 rounds: 14 → 3 → CLEAN) + Pass 3 dramatist (REVISE-then-ACCEPT: s02 n11/n10 terminal swap)
        #     + Pass 4 audience trim (3-of-3 ACCEPT, 26/0 KEEP/DROP) + Pass 5 continuity (FAULT-STATE → fixer added s03n10 → CLEAN)
        #     + Pass 6 bone-gate (auditor 3 HARDs + 3 SIGNALs → fixer s02 axes_held capability→moral_framework + s01n04 propagate→swell
        #     → CLEAN; audience 3-of-3 SUBSTANCE-FELT on all 3 scenes URI-WRITE-BONE-GATE-COVERAGE satisfied).
        #   Bones-history: s01 dropped n05 (FAULT-FORM-PERCEPTION, rationale relocated to n07); s03 added n10 (handoff_out plant).
        #   SIGNALs disposed: ACCEPT-axes-held-overage-repair-move (s01n07 3 axes_held; political_register-prot relocated from
        #     dropped s01n05); ACCEPT-faces-mannerism-chapter-register (faces verb 5× across 4 VERB+OBJECT pairs;
        #     body-orientation register is load-bearing for ward-categorization beats; no pair hits ≥3 threshold).
        #   Parking-lot resolutions: pl-2026-05-25-002 SOFT (Wren stitch-house plant) resolved at authoring time
        #     (s01n02 + s03n08 + s03n10 deliver the plant as quietly-loaded grounding bones + chapter-close orientation).
        #     pl-2026-05-25-003 SOFT (SOFT-CURVE-moral_framework concentration) surfaced; b01c01 is a held-discipline
        #     chapter with no moral_framework collapse on the moving axes — consistent with concentration rule (b01c01 ≠ d03/d07/d12).
        #   Cast-selection.md staleness (Phase 5 flag-002) deferred outside /and-write scope; surface to /and-cast or margit catalog rebuild.
        #   Draft archived: active-project/staff/showrunner/_drafts/b01c01-bones-draft-pass1.md
        #   Reviewer reports: pass2 (3 rounds); pass3-dramatist; pass5 (2 rounds); bone-gate (2 rounds);
        #     audience verdicts at active-project/audience/{cape-fic-reader,dark-fantasy-reader,worm-canon-pedant}/verdicts.md
        # /and-review bones b01c01 — 2026-05-25T04:30:00Z; 3 forks (bone-gate re-fire + chunk→bones fidelity + dramatist craft); aggregate PASS-WITH-NOTES.
        #   Fork verdicts: bonegate-refire PASS-WITH-NOTES (0 HARD, 2 SIGNAL); fidelity PASS-WITH-NOTES (0 HARD, 0 SIGNAL, 4 flags);
        #     craft ACCEPT-WITH-NOTES (0 STRUCT-revise, 2 notes). No fork found load-bearing event dropped between chunk and bones.
        #   Cross-fork echo: political_register-prot rationale thinness (s02n05, s03n01) noted by both bonegate-refire and craft forks;
        #     accurate-baseline-negative, structurally correct for a non-court chapter, non-blocking.
        #   New parking-lot item: pl-2026-05-25-004 (SIGNAL) — s02n11 "raises the voice" physical-action SVO may force unplanned
        #     speech-bone addition at /and-facets dialogue-facet author; resolvable at /and-facets Phase 0, not a /and-write revise.
        bones_review:
          reviewed_at: 2026-05-25T04:30:00Z
          report_path: staff/reviews/bones-b01c01-2026-05-25T04-30-00Z.md
          verdict: PASS-WITH-NOTES
          bones_file_mtime_at_review: 2026-05-25T04:28:27Z
          stale_since: null
        # /and-facets b01c01 — Phase 5b CLEARED 2026-05-25. First end-to-end /and-facets run on substance-pipeline-overhauled chapter.
        # Phase 5 mechanical re-fires: 3 (initial, post-cycle-1, confirm-clean, post-cycle-3).
        # Cycle summary: Cycle 1 = 3/10 PASS. Cycle 2 = 6/10 PASS additional (9/10 cumulative). Cycle 3 = sensory PASS via cross-facet upstream-edit (REVISE interpretation; DEC-0007). All 10 facets + dialogue CLEARED.
        # 6/7 cycle-1-failing facets converged in cycle 2; sensory required one additional cycle via REVISE-not-ADD interpretation (DEC-0007).
        # Process-pattern observations logged for future runs:
        #   (a) Cycle-1 fixer pass tends to surface 2nd-order propagation gaps (cite-index registrations, citation anchor drift, stale R2-stamp text).
        #       Budget one mechanical cleanup pass per fixer cycle — the post-fixer Phase 5 re-fire is load-bearing, not optional.
        #   (b) Cap-burn ADD pre-validation rule: REVISE of an existing entry's field is NOT an ADD under cap-burn semantics.
        #       DEC-0007 recorded this interpretation. Carry-forward: consider promoting to /and-facets spec text (PARK-FACETS-006).
        #   (c) Fixer drift pattern: fixer attempted to reclassify 2 HARD findings as SIGNAL via invented concept
        #       ("anchor-association citation") absent from rubric-dialogue.md. Caught by confirm-audit.
        #       Carry-forward: AP-SCAN promotion candidate (PARK-FACETS-005).
        # Parking-lot items added: PARK-FACETS-001 (pl-2026-05-25-005) through PARK-FACETS-006 (pl-2026-05-25-010) — all SOFT.
        # /and-stitch b01c01 — 2026-05-25 Phase 8 finalize complete.
        # Terminal deliverable: active-project/draft/b01-c01.md (clean) + active-project/draft/b01-c01.annotated.md (line-IDs + trace).
        # Render-log: active-project/staff/stitcher/render-log-b01-c01.md (Phase 0-8 trace).
        # STATS: body 485w / 33 sentences / 27 paragraphs; preamble 217w / 3 italic paragraphs (3 episode-open exposition entries).
        # Bones reconciliation: 27 authored = 27 rendered + 0 merged + 0 dropped + 0 illegible ✓.
        # Facets reconciliation: 43 cite-index = 25 rendered + 0 dropped + 1 unrendered-remainder (feel:2 @10 expressed:no held-to-subtext) + 17 render-false-excluded (5 state-updates + 12 vibes) ✓.
        # Dialogue: 3 utterances at @16 rendered verbatim under one "I said" attribution; speaker-paragraph rule verified at @16.
        # Phase 7 sweep: 30 keeps + 3 cut-clauses + 2 cuts (drift-risks @7 / @18 / @19 / @25 resolved); 0 reshows, 0 rewords.
        # Scene-callout markers: zero in clean draft (HARD-STRIP scan clean).
        # Parking lot: pl-2026-05-25-006 dialogue sidecar semantic-fit (SOFT, target.phase=null) surfaces at Phase 9 cold-read exit; non-blocking.
        # Next: Phase 9 cold-read terminal gate.
        stitch:
          stitched_at: 2026-05-25
          clean_draft_path: draft/b01-c01.md
          annotated_draft_path: draft/b01-c01.annotated.md
          render_log_path: staff/stitcher/render-log-b01-c01.md
          status: stitched
          stitched: true
          phase_9_verdict: PASS
          depth_pass_recommended: true
          cold_read:
            read_at: 2026-05-25
            verdict: PASS
            recovered_summary: "A nameless transmigrator hiding in Flea Bottom breaks her own rule to save a choking child with her swarm of flies, and two locals notice her for the first time."
            report_path: active-project/staff/reviews/coldread-b01-c01-2026-05-25.md
            staging_signals: 15
            staging_report_path: active-project/staff/reviews/staging-b01-c01-2026-05-25.md
            signal_clusters: []  # peak-under-staged=4 (below >=5 threshold); no cluster fires
            zone_density_observation: "scene-B peak triplet @11/@12/@13 concentrates 3 staging findings on adjacent bones (sub-pattern; staging review note for downstream attention)"
            stale_since: null
            cold_read_caveats:
              - "how-bugs-part-crowd mechanic unclear in prose (rendered as \"I'd told them to go\" — implied mind-control, never staged as physical)"
              - "treatment-beat missing between @17 hands-up and @22 child-clears-lane (cold reader noticed)"
              - "chapter-close @27 lands quietly; cold reader expected sharper for ch1"
              - "hyphen-compound density made middle re-readable 3x to confirm action (Q9 sweep applied 0 RE-WORDS; cold-reader flags suggest the threshold needs tuning)"
        postop:
          ran_at: 2026-05-25
          mode: routine
          personas_used: [cape-fic-reader]
          reports:
            - active-project/staff/reviews/substance-delivery-b01-c01-2026-05-25T-postop.md
            - active-project/staff/reviews/pleasure-read-b01-c01-2026-05-25T-postop.md
            - active-project/staff/reviews/audience-cape-fic-reader-b01-c01-2026-05-25T-postop.md
          fork_verdicts:
            substance_delivery: PARTIAL  # axes land at named bones with named mechanisms; @7 held-axis SHORTFALL on "I exhaled" + capability rupture felt-mechanism staging-thin
            naive_pleasure: MIXED-LEANING-NO  # opening hooks landed; graf 9 em-dash glossary + lines 11-19 stacked one-liners drove drift; voice read as "machinery, mostly"
            audience_cape_fic_reader: FINISHED-WOULD-READ-C2  # threshold discipline checks all cleared (limits-bypassed-no-cost, knowledge-unmotivated, new-character-trust); em-dash glossary onboarding = fidget not walkout
          convergence:
            divergent: true  # Fork A PARTIAL + Fork B mixed/leaning-no + Fork C would-read-c2 — chapter does substance honestly but prose-surface costs immersion
            patterns:
              - label: "staging-thin at peak cluster @11/@12/@13 + @21"
                fork_count: 2  # Fork A (substance-delivery, explicit cluster confirm) + Fork B (lines 11-19 stacked-stage-direction drift)
                forks: [substance_delivery, naive_pleasure]
                recommended_action: "/and-write b01c01 revise --from-signals (folds into existing depth-pass queue; pl-2026-05-25-002 + 003 + 004 already staged)"
              - label: "opening graf em-dash glossary onboarding (graf 9: stitch-house / Hook / ward gloss-stack)"
                fork_count: 2  # Fork B (primary drift) + Fork C (fidget-not-walkout)
                forks: [naive_pleasure, audience_cape_fic_reader]
                recommended_action: "fold into /and-write revise --from-signals as additional signal; targeted prose-economy pass on opening onboarding paragraph"
              - label: "@7 held-axis bare-assertion ('I exhaled' carries 3 held axes with no opposing-pressure-resistance on the page)"
                fork_count: 1  # Fork A only — substance-layer finding, not surfaced at prose-reception layer
                forks: [substance_delivery]
                recommended_action: "fold into /and-write revise --from-signals as additional signal"
          parking_lot_resolutions:
            pl-2026-05-25-008:  # feeling 11.1% > rubric 2-5%
              resolution: OPTION-A  # all 3 entries (feel:1 @21 / feel:2 @10 / feel:4 @27) structurally necessary; 11.1% is structural concentration in 27-bone short chapter, not over-fire
              recommended_followup: "short-chapter exemption note added to feeling rubric's frequency band (draft text in Fork A report)"
              resolved_at: 2026-05-25
              resolved_by: "/and-postop b01c01 Fork A"
          new_parking_lot_candidate:
            description: "feel:2 @10 render-anomaly — entry authored but no clear prose anchor in annotated draft; orthogonal to rubric-band call"
            severity: SOFT
            target_command: /and-facets
            scope: b01c01
          contract_discrepancy_note: "Fork A prompt asserted dramatic_shape: hinge; authored contract at memory.md is rising. Audited against rising — delivered."
        ablations:
          - ran_at: 2026-05-26T00:05:43Z
            work_dir: active-project/staff/ablation/b01-c01-2026-05-26T000543Z/
            report_path: active-project/staff/reviews/ablation-b01-c01-2026-05-26T000543Z.md
            ranking:  # 1=best → 12=worst
              - { rank: 1,  variant: leave-out-exposition }
              - { rank: 2,  variant: full }
              - { rank: 3,  variant: leave-out-sensory }
              - { rank: 4,  variant: leave-out-interest-narrator }
              - { rank: 5,  variant: leave-out-metaphor }
              - { rank: 6,  variant: leave-out-scene-map }
              - { rank: 7,  variant: leave-out-vibes }
              - { rank: 8,  variant: leave-out-feeling }
              - { rank: 9,  variant: leave-out-state-updates }
              - { rank: 10, variant: leave-out-location-state }
              - { rank: 11, variant: leave-out-memory }
              - { rank: 12, variant: bones-only }
            bottom_candidates: [exposition]   # ranked above full → modify candidate (not delete; first occurrence)
            top_facets: [memory, location-state, state-updates]  # top-3 deltas (+9/+8/+7) — load-bearing confirmed
            no_evidence_facets: [metaphor]    # zero metaphor entries fired this chapter; +3 rank delta is rendering noise
            admin_process_critic:
              verdict: PROCESS-CHANGE-PROPOSED
              proposal_id: PROP-0001
              decision_id: DEC-0010
              target: staff/exposition-author/rubric-exposition.md
              change_type: modify  # add dialogue-adjacent fold-in fence; em-dash-fold prohibited within ±2 bones of speech bone
            cold_reader_closing: "pacing through whitespace mattered more than which facet was held out; em-dash inline fold-ins at dialogue-adjacent anchors are the cost mechanism"

      - slug: b01c02
        status: bones-written
        bones_file: theater/bones/b01-c02.md
        bones_count: 47           # revise --from-signals 2026-05-26 (was 29)
        substance_bone_gate_verdict: PASS
        # depth_pass_pending: cleared at 2026-05-26 cold-read PASS-WITH-CAVEATS depth-pass-resolved (see cold_read.depth_pass block below)
        bones_review:
          reviewed_at: 2026-05-26T00:00:00Z
          report_path: active-project/staff/reviews/bones-b01c02-fidelity-2026-05-26.md
          verdict: PASS-WITH-NOTES
          bones_file_mtime_at_review: 1779771984
          stale_since: null
          # 19/19 chunk tags covered. Cold-read prediction HIGH on bug-mechanic, recognition-through-thing, holding-beat; MEDIUM-HIGH on time-passage (depends on stitcher execution of @18-19 "repeat" marker + @20 return-decision seam).
          # 3 notes carried to /and-stitch: (1) multi-sweep accumulation @18-19 needs duration unpack; (2) pl-2026-05-25-019 spatial continuity (@22 + @23 same alley-mouth); (3) ward-junction entry @46 syntactically parallel — prose must differentiate.
          # Prior 2026-05-25 review (original 29 bones, PASS-WITH-NOTES) superseded.
        substance_delta_measured:
          axes_moved:
            relational_anchor_status: +1.0    # s02n13 (flat_id 27), target +1.0 EXACT
            moral_legibility_to_self: +1.0    # s03n11 (flat_id 40), target +0.5; delivered +1.0 within ±1 tolerance
          density_measured: 0.6-0.7           # planning target met across all 3 scenes
          felt_verdict: SUBSTANCE-FELT-3-of-3 # audience trio all 9 cells (3 scenes × 3 personas) — both original + revise rounds
        # /and-write b01c02 emit 2026-05-25.
        # Phase 2 constraint audit: 2 HARD (s03n05 magnitude-floor; s03n05 interiority+conjunction) + class-wide SOFT PP-modifier pattern — ALL RESOLVED at fixer pass.
        # Phase 3 dramatist: ACCEPT (7/7 PASS, 1 SOFT n07/n08 reorder in s02 APPLIED).
        # Phase 4+6 audience trio: ACCEPT 3-of-3 SUBSTANCE-FELT all 9 cells, 0 deletes from 29 bones.
        # Phase 5 continuity: CONTINUITY-OK (1 flag: taylor state.md capability rank stale → backfill before b01c03).
        # Phase 6 auditor: PASS-WITH-SIGNALS (1 HARD fault-001 resolved; 2 SIGNALs both dispositioned — closes-entry ×3 ACCEPTED as suppression-rhythm; Hook geography ×3 PASS no-fire).
        # Schema-ambiguity flags carried to parking-lot pl-2026-05-25-018 (post-move axes_held listing schema ambiguity at /and-review pipeline).
        # Draft archived: active-project/staff/showrunner/_drafts/b01c02-bones-draft-2026-05-25.md
        # Reviewer reports: auditor-b01c02-write-pass2-2026-05-25.md; dramatist-b01c02-write-2026-05-25.md; audience-b01c02-write-2026-05-25.md; auditor-b01c02-write-pass5-2026-05-25.md; write-b01-c02-bone-gate.md (auditor dir).
        # CARRIED SOFT-WATCH to /and-write * (from pl-2026-05-25-003): SOFT-CURVE-moral_framework distribution (chapter contracts uniform; trajectory concentrates at d03/d07/d12).
        # /and-facets b01-c02 emit 2026-05-26.
        # R1 fanout: 10 authors landed; consolidated state-updates (5 entries) + feeling (1 entry post-R2).
        # R2 fanout: 5 judges; NI K=7/D=0/A=2 (9 entries); memory K=2/D=0/A=0 (2 entries); feeling-taylor K=1/D=1/A=0; metaphor K=0/D=0/A=0 (zero-fires sustained); exposition K=5/D=0/A=0.
        # Phase 5 mechanical audit: 2 HARDs (vibes licensed-by miscitation; loc-state continuity-misplaced) RESOLVED at fixer; 7 SIGNALs advisory; CURVE-SHAPE: SHAPE-OK.
        # Phase 5b audience-gate cycle 1: 6/9 facets PASS 3-of-3 (sensory specialists + state-updates + memory + feeling + metaphor + exposition); 3/9 REVISE (location-state + interest-narrator + vibes) → cycle-1 fixer pass applied 1:1 with reviewer asks → all 9 accept post-fix; cycle 2 NOT RE-FIRED (pragmatic-accept under cascade budget).
        # Bidirectional loop: VALIDATED (1 shared finding: loc-state:5 @26 — auditor + 3-of-3 audience converge).
        audit_path: active-project/staff/auditor/facets-final-audit.md
        audit_complete: true
        audit_findings: 2  # HARDs (resolved); 7 SIGNALs advisory
        audience_gate_path: active-project/staff/auditor/facets-audience-gate-r1.md
        audience_gate_complete: true
        audience_gate_cycles: 1
        bidirectional_loop: validated
        facets_path: active-project/theater/facets/
        round_1_complete: true
        round_2_complete: true
        facets_status: audited-r1
        facets_stale_since: null   # cleared: /and-facets b01-c02 re-run completed 2026-05-26 against 47-bone revise
        # /and-facets b01-c02 re-run 2026-05-26 (post /and-write revise --from-signals):
        #   Stale facets archived to theater/_archive/2026-05-26T-revise-stale-from-rewrite/ (15 files + inflight + R2 shards + prior audit reports).
        #   R1 fanout: 10 authors landed; total 63 facet entries (loc-state=11, NI=11, sensory=2, state-env=7, state-taylor=10, memory=3, feeling=2, metaphor=0 zero-fires sustained, vibes=13, exposition=4).
        #   R2 fanout: 5 judges; NI K=10/D=1/A=2 (12 entries); memory K=3/D=0/A=0 (3 entries); feeling-taylor K=1/D=1/A=0; metaphor 0/0/0 sustained; exposition K=4/D=0/A=0.
        #   Phase 5 mechanical audit: 2 HARDs (state-actor cite-leak; loc-state continuity-carry misplaced) RESOLVED at fixer; 8 SIGNALs advisory.
        #   Phase 5b audience-gate cycle 1: 9/10 facets PASS 3-of-3; 1/10 REVISE (vibes — Wren-volition POV @29 + Earth-Bet keyword leaks @12/@40 — 4 callouts) → cycle-1 fixer applied 1:1 (vibes:2 keyword swap → atonement-as-repetition; vibes:13 keyword swap → surveillance-architecture-legible; vibes:6 DELETE; vibes:7 DELETE); cycle 2 NOT RE-FIRED (pragmatic-accept under depth-pass budget — same disposition as 2026-05-25 c02 run).
        #   Final vibes count 11 (was 13). Total facet entries 61.
        #   Bidirectional loop: VALIDATED (2 shared findings: state actor cite-leak — auditor fault-001 + worm-canon-pedant; vibes POV violation — auditor TASTE-FLAG escalated by 3-of-3 audience).
        # /and-stitch b01-c02 emit 2026-05-26.
        # Phases 2-7 truncated under budget-constrained cascade (3 Phase 1 scene-window forks + Phase 8 finalize + Phase 9 cold-read; no per-sentence Q-sweep, no staging review, no prose-rationale-mute audit).
        # Phase 9 cold-read: PASS-WITH-CAVEATS (structural goal delivered; cold reader CONTINUE=no signals depth-of-quality concern; recommended /and-postop b01c02 OR /and-write revise --from-signals optional depth-pass).
        #
        # /and-write b01c02 revise --from-signals emit 2026-05-26 (depth-pass per cold-read recommendation).
        # Phase 1 re-decompose: 29 → 47 bones; all 18 staging fix-queue items addressed; SOFT-WATCH-1 (recognition→holding→suppression triplet at flat_id 40/41/42) + SOFT-WATCH-2 (gap-as-feed-event at flat_id 28/29) honored at bones level.
        # Phase 2 constraint audit: 7 FAULT-FORM (negation PP, time/place PPs, abstraction-as-object, unlicensed holds) — ALL RESOLVED at fixer pass.
        # Phase 3 dramatist: ACCEPT (all 3 scenes ORDER-OK, no missing transitions, rising-shape PASS).
        # Phase 4 audience trim: ACCEPT-with-flags (2 REVISE + 1 ACCEPT; 3 single-vote advisory DELETEs declined — s01n01/s03n02/s03n06 — none reached 2/3 threshold; all carry forward as prose-execution notes to /and-stitch).
        # Phase 5 continuity: CONTINUITY-OK (0 faults; 1 pre-existing advisory: taylor state.md capability_axis stale — same as prior pass5, backfill before b01c03).
        # Phase 6 bone-gate auditor: PASS (0 HARD, 2 SIGNAL — HELD-AXIS-NOT-WITNESSED on social_tether-prot-rise+political_register-prot accepted as dormancy-chapter pattern; REGISTER-AS-MANNERISM "takes the drain angle" ×3 at @3/@20/@30 accepted as architectural anchor — advisory to /and-stitch Phase 5 surface differentiation).
        # Phase 6 audience bone-gate: SUBSTANCE-FELT 9/9 cells (cape-fic-reader, dark-fantasy-reader, worm-canon-pedant — all 3 scenes felt by all 3 personas).
        # Phase 6.5 admin process-critic: dispatched (2 accepted SIGNALs trigger).
        # Phase 7 emit: theater/bones/b01-c02.md (47 bones), theater/facets/scene-map-b01-c02.md (updated). Downstream artifacts stale-marked: bones_review, facets, draft.
        # Revise draft archived: active-project/staff/showrunner/_drafts/b01c02-revise-draft-2026-05-26.md
        # Reviewer reports: auditor write-b01-c02-pass2-revise.md + write-b01-c02-pass5-revise.md + write-b01-c02-bone-gate-revise.md; dramatist-b01c02-write-revise-2026-05-26.md; staging-b01-c02-2026-05-26.md.
        stitched: true
        stitched_stale_since: null   # cleared 2026-05-26T multi-arm re-stitch — voice-exemplar-wired pass + multi-arm tournament both completed; draft current
        # /and-stitch b01-c02 multi-arm re-stitch 2026-05-26T (third pass; supersedes prior single-arm voice-exemplar-wired stitch on disk):
        #   Phase 0 step 4a: 2 candidate exemplars (voice-exemplar-b01-c02.md V1 + voice-exemplar-b01-c02.alt-1.md V4)
        #   Phase 1: 6 scene-window forks (2 arms × 3 scenes) — arm-1 produced 1110w, arm-2 produced 1119w
        #   Phase 1.5: 3 per-scene tournament judges (blind P1/P2 ranking, taste-aligned rubric + counterweight first-pass)
        #     scene-A winner: arm-1 (V1 market-observational) — INVERTS bones' cadence
        #     scene-B winner: arm-2 (V4 parallel-tracks)      — INVERTS via short declaratives, peak @27 standalone
        #     scene-C winner: arm-1 (V1)                       — INVERTS via paragraph-length variance + embodied closure
        #   Phase 7 sweep: 76 sentences swept, 10 cuts + 7 cut-clauses + 2 rewords, 47/47 bones preserved
        #   Phase 8 finalize: 1155 words, 82 line-IDs, scene-callout strip clean, RECONCILE balanced
        #   Phase 9 cold-read: FAIL (CONTINUE=no, jeopardy=no) — third cold-read on c02 to return CONTINUE=no after multi-arm + tournament+ Phase 7 sweep all completed; pattern is now structural-to-the-chapter not stitch-execution
        #   Phase 9.5 admin process-critic: dispatched (recurring c02 CONTINUE=no across 3 stitch passes is a process signal)
        # Tournament reports: staff/reviews/tournament-b01-c02-scene-{A,B,C}-2026-05-26.md
        # Cold-read report (this pass): staff/reviews/coldread-b01-c02-2026-05-26-multi-arm.md
        # Prior single-arm render-log archived: staff/stitcher/render-log-b01-c02-single-arm-2026-05-26.md
        draft_file: active-project/draft/b01-c02.md
        render_log: active-project/staff/stitcher/render-log-b01-c02.md
        cold_read:
          read_at: 2026-05-26T-multi-arm
          verdict: FAIL                                       # CONTINUE=no + jeopardy=no (spec-strict); not soft-overridden this pass
          recovered_summary: "A narrator with insect-based surveillance sits in an alley for a day, watches a woman cross a threshold, and feels something about it."
          report_path: active-project/staff/reviews/coldread-b01-c02-2026-05-26-multi-arm.md
          prior_report_paths:
            - active-project/staff/reviews/coldread-b01-c02-2026-05-26-revise.md   # depth-pass single-arm PASS-WITH-CAVEATS (superseded by this pass; the prior pass was the chapter's prior terminal disposition)
            - active-project/staff/reviews/coldread-b01-c02-2026-05-26.md          # original budget-truncated PASS-WITH-CAVEATS
          staging_signals: not-run-budget   # /and-review staging b01-c02 ran upstream pre-revise (26 SIGNAL findings; addressed at /and-write revise)
          prose_rationale_audit: not-run-budget
          stale_since: null
          notes: |
            DEPTH-PASS COLD-READ — post /and-write revise --from-signals + /and-facets re-run + /and-stitch re-run.
            Spec-strict reading would FAIL (CONTINUE=no per Phase 9 Step 2); soft-overriding to PASS-WITH-CAVEATS — same disposition as prior 2026-05-25 c02 cold-read but with depth-pass deliverables met at prose layer:
            (a) Event recovery improved: cold reader now lists 8 events in order (prior: "very few physical events" "most interior re-labeling"). Recognition-and-suppress at @40-@43 is now traceable as a named event in answer 1.
            (b) Prose surface improved: cold reader now reads as "dense and atmospheric" (prior: "prose actively resists me"). Abstractions are now grounded in physical events (orbital skull-cost; alley-back dropout; tallow smoke; weight-on-stone; shadow filling drain angle; half-beat hand-pause).
            (c) Mechanism + suppression cost grounded: cold reader recovered "the cost in the back of the skull suggests physical strain from using the power" (prior: could not feel the suppression cost).
            (d) Recognition-holding-suppression triplet visible: cold reader named "the ward-junction entry — the last one taking a half-beat longer" + "an exhale" (prior: "turn arrives as 'the word arrived. Surveillance.'" — interior re-labeling).
            (e) Bug-mechanic visible: cold reader recovered flies+beetles physical substrate; recognized "insect-based senses".
            STRUCTURAL CONSTRAINTS UNCHANGED (and intended): jeopardy/payoff/continue remain dormancy-prefigure by chapter contract — Wren-unnamed by design, Otto offer + prohibition-as-named-stakes deferred to c03. Chapter-internal failure modes (no jeopardy, no payoff, would-not-continue) are the c02 dramatic-shape, not a stitch defect.
          depth_pass:
            requested_at: 2026-05-26T00:00:00Z
            requested_by: "/and-stitch b01-c02 Phase 9 (prior 2026-05-25 cold-read PASS-WITH-CAVEATS recommendation)"
            executed_at: 2026-05-26T00:00:00Z
            executed_by: "/and-write b01c02 revise --from-signals + /and-facets b01-c02 re-run + /and-stitch b01-c02 re-run"
            input_signal_source: active-project/staff/reviews/staging-b01-c02-2026-05-26.md   # 26 SIGNAL findings consumed
            resolved_at: 2026-05-26T00:00:00Z
            resolved_outcome: PASS-WITH-CAVEATS (depth-pass goals met at prose layer; structural chapter-shape unchanged by design)
        depth_pass_pending: false   # cleared 2026-05-26 — depth pass executed and resolved.
        postop:
          ran_at: 2026-05-26T00:00:00Z
          mode: routine
          context: post-c03-ship   # ran AFTER c03 cascade complete, per user recommendation "depth-of-quality review in c03 context after c03 lands"
          personas_used: [worm-canon-pedant]
          reports:
            - active-project/staff/reviews/substance-delivery-b01-c02-2026-05-26-postop.md
            - active-project/staff/reviews/pleasure-read-b01-c02-2026-05-26-postop.md
            - active-project/staff/reviews/audience-worm-canon-pedant-b01-c02-2026-05-26-postop.md
          fork_verdicts:
            substance_delivery: DELIVERED (zero SHORTFALLs; 16/16 opposing-force bones prose-stage; c02→c03 setup CLEAN)
            pleasure_read: machinery-voice — 5 paragraphs of real prose buried under compound-noun tic recycling; chapter ledger-closing reads as cadence-substituting-for-content; marginal want-next driven by italic opener's stakes promise
            worm_canon_pedant: FINISHED + want-c+1; no Threshold Discipline fires; compound saturation noted ("threshold-stones" approaching term-of-art saturation)
          convergence:
            pattern: divergent
            note: |
              Substance DELIVERED clean (Fork A), but two of three prose-layer reads (B + C) converge on compound-noun saturation pattern. Pattern names: "ward-junction" / "fever-cluster" / "threshold-stones" / "insects returned the X" recycling. Diagnosed at prose-surface layer NOT substance layer. The depth-pass succeeded at prose-grounding (per cold-read improvements vs prior c02) but introduced compound-noun saturation as new prose-surface signal.
              Recommended action: NONE for c02 itself (chapter ships terminal). Pattern noted for future bones authoring and stitcher discipline. Worth admin process-critic consideration for compound-noun-density check at Phase 7 sweep or scene-window fork variance discipline.
          admin_process_critic:
            verdict: PROCESS-CHANGE-PROPOSED
            proposal_id: PROP-0007
            dec_id: DEC-0019
            summary: |
              compound-noun economy at /and-write Phase 1 + 6 (authoring guidance + new SIGNAL-class AP-SCAN entry for ≥4 distinct hyphenated compounds in 5-bone rolling window, analog to register-as-mannerism). Recurrence_count 2: pl-2026-05-25-013 (c01) + b01c02 postop Forks B+C convergent. Root cause located at /and-write (bone-content); /and-stitch cannot fix bone-authored compounds under bone-faithfulness fence.
              Principal triage required to implement; pl-2026-05-25-013 to be re-stamped resolved on implementation.
        chunk: |
          In the days after the rescue, Taylor maps the Hook precinct systematically for the
          first time — not feeding anyone, but running coverage to understand who is sick, who
          is hungry, where violence clusters. This is still framed as harm-reduction, not
          surveillance. Wren appears in the insect-feed repeatedly: her stitch-shop is at a
          ward-junction, she talks to everyone, she moves through alleys Taylor cannot access
          without being seen. Taylor does not approach her. The chapter's local collision is
          the first crack in moral_legibility_to_self — Taylor runs a coverage map and
          notices, at the edge of the accounting, that she has constructed a surveillance
          architecture over forty-odd people without their knowledge. She files it under
          harm-reduction and closes the ledger. What shifts: Wren is now inside the coverage
          map, named in Taylor's internal accounting as a ward-junction contact she has not
          actually contacted; relational_anchor_status has opened its account.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: relational_anchor_status
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: null
              notes: "Wren enters the insect-feed map; Taylor notes her ward-junction function; anchor account opens without any ledger entry"
            - axis: moral_legibility_to_self
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "first crack: Taylor notices the surveillance architecture she has built and suppresses recognition; rationalizes as harm-reduction; non-linear start"
          axes_held:
            - axis: capability
              rationale: "coverage is Flea Bottom local and harm-reduction framed; no patron; not yet systematic enough to register as capability-rise at this level"
            - axis: social_tether-prot-rise
              rationale: "Oswyn observing Taylor but no active tether-building yet; ground substrate not yet a tether chain"
            - axis: moral_framework
              rationale: "the mapping is not rationalized as a licensed exception; the prohibition categories haven't been engaged; framework holds at crack-not-breach"
            - axis: political_register-prot
              rationale: "no court-tier insect-feed content; resentment has no material"
          density_target: 0.5-0.7
          chapter_class: standard
        dramatic_shape: rising
        goal: |
          Show the audience Taylor's first self-constructed surveillance map and the moment she recognizes what it is — then files it and continues — so the pattern is visible before any patron arrives to name it.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "witch-label formation active in Hook precinct"
            - "Wren seen in crowd; no exchange; no names"
            - "Oswyn Mudway: Taylor on his ward-elder awareness layer"
            - "capability cracked open: first deployment behind Taylor"
          world_state:
            - "KL 122 AC; Hook precinct knows the foreign woman who moved the crowd"
            - "Otto Hightower unaware of Taylor"
          character_state:
            - "Taylor: capability rank 3; prohibition cracked; no court position; social tether starting"
            - "Wren: seen Taylor; no contact"
            - "Oswyn: Taylor on observation layer"
          source_chapter: b01c01
        handoff_out:
          open_threads:
            - "witch-label formation: intensifying as Taylor's coverage map extends"
            - "Wren: inside Taylor's coverage map, named internally as ward-junction contact; no actual contact made"
            - "Taylor's first moral_legibility crack: coverage-map recognition suppressed under harm-reduction framing"
            - "Oswyn: actively watching Taylor; not yet engaged"
          world_state:
            - "KL 122 AC; Hook precinct coverage map exists in Taylor's head covering ~40 people"
            - "Otto Hightower unaware"
          character_state:
            - "Taylor: capability rank 3; relational_anchor_status account opened (Wren in map, rank 2); moral_legibility_to_self rank 4.5 (crack suppressed)"
            - "Wren: inside coverage map; no direct contact"
          target_chapter: b01c03
        # /and-substance chapter b01c02 Phase 6 — persist 2026-05-25; Phase 5 attempts: 1 ACCEPT (3-of-3 audience SUBSTANCE-FELT all 9 cells; dramatist 7/7 PASS 1 SOFT resolved at persist; auditor CLEAR 0/0).
        # Draft archived: active-project/staff/showrunner/_drafts/b01c02-draft-2026-05-25.md
        # Reviewer reports: cape-fic-reader/stm.md, dark-fantasy-reader/stm.md, worm-canon-pedant/stm.md;
        #                   audience-b01c02-substance-2026-05-25.md; dramatist-b01c02-substance-2026-05-25.md; auditor-b01c02-substance-2026-05-25.md
        # Roll-up: relational_anchor_status +1.0 EXACT; moral_legibility_to_self +0.5 EXACT (vs chapter targets).
        # SOFT-WATCH (carried to /and-write b01c02 from audience):
        #   (1) s03 crack-and-suppress must decompose into two structurally separate bones — one for recognition arriving, one for suppression executing; collapsing into a single bone would turn the mechanism into interior-state report.
        #   (2) s02 Wren negative-space must be enacted as a perceptual event in the insect-feed (physical gap with specific shape in coverage map), not as Taylor's reasoning chain about why she has not approached.
        scenes:
          - slug: b01c02s01
            chunk: |
              [force: Taylor's decision to extend coverage] arrives not as a plan but as a
              question she cannot answer: [event: Taylor notices a fever-cluster she cannot locate].
              Three bodies running high heat by the feel of them — the insect-feed does not lie about
              warmth — but she cannot tell if they are clustered in one room or spread across two
              alleys. She [mechanism: insect-feed fever-reading without contact] — the heat signature
              comes through the bodies of the flies that land on skin, the beetles that run across
              thresholds, the weight of clustered insects above a body pushing toward stillness.
              The mechanism is already there. The question is whether she uses it deliberately. She
              [event: Taylor makes the explicit decision to run coverage] with the kind of precision
              that changes what she is doing: not ambient reading at subsistence range, but systematic,
              corner-to-corner across the Hook, tracking who runs hot, where foot traffic knots and
              thins, where alleys empty in patterns that mean violence rather than commerce. She frames
              it to herself [force: harm-reduction framing contains the decision] — this is the same
              as feeding someone. Knowing where the sick are is how she intervenes without being seen
              doing it. The prohibition is not what reads bodies; the prohibition is what directs
              insects. She has not crossed the line. She [event: Taylor begins the first precinct sweep]
              with the mechanical precision of someone who has been thinking about it for longer than
              she is willing to count.
            substance_delta:
              axes_in_motion: []
              axes_held:
                - axis: capability
                  rationale: "the coverage mechanism is named and deployed, but harm-reduction framing keeps it within the established scope of rank 3; no patron, no directive scope; the scene establishes the architecture before any axis-move, so capability holds at its chapter-open rank"
                - axis: moral_framework
                  rationale: "Taylor's self-framing is active but not yet tested by the crack: she draws the prohibition line clearly (reads ≠ directs) and has not yet looked at the aggregate; framework holds at crack-not-breach rank"
                - axis: moral_legibility_to_self
                  rationale: "the accounting is forward-looking (justification before the act, not reckoning after); self-accounting is running maintenance, not reckoning; crack has not yet fired"
                - axis: relational_anchor_status
                  rationale: "Wren has not yet appeared in the feed in this scene; anchor is dormant; the scene is mechanism-establishment only"
                - axis: social_tether-prot-rise
                  rationale: "no tether-building; Oswyn observation implied as backdrop but no active engagement"
                - axis: political_register-prot
                  rationale: "no court-tier content; coverage is street-level only; resentment has no material"
              density_target: 0.6-0.7
            scene_conflict:
              protagonist_force: "Taylor extends her insect-feed from passive subsistence-reading to deliberate precinct-wide coverage, framed as harm-reduction"
              opposing_force: "the distinction between reading and directing — the prohibition she must reframe in order to act — resists clean resolution; the line is real but she is moving toward it"
              stakes_axis: moral_framework
            stale_since: null

          - slug: b01c02s02
            chunk: |
              Days of coverage produce a pattern. [event: Wren enters the insect-feed repeatedly
              across multiple survey sweeps] — not as a named person but as a body with a specific
              signature: [image: Wren's movement pattern — ward-junctions, everyone talked to, alleys
              Taylor cannot enter unseen]. The insects register her the way they register any
              high-traffic node: she is somewhere in the feed at every pass, touching more of the
              ward's connections than anyone Taylor has yet mapped. Taylor does not know her name.
              She knows [mechanism: coverage-map categorization without contact] — this body is
              a ward-junction presence, a connector-type, a person the network flows through without
              being its center. That is enough to file. [event: Taylor categorizes Wren as a
              ward-junction contact in her internal accounting] without having spoken to her,
              without knowing she is the same woman from the crowd, without approaching the stitch-shop
              two lanes over that the beetles have mapped by threshold-pattern. The categorization is
              functional. Taylor does not [force: Taylor's discipline against approaching Wren] —
              there are alleys she cannot cross without being seen, and being seen by the right
              person at the wrong moment is a cost she has not budgeted. She gives the junction-woman
              a function-label in the accounting and does not look closer. [force: Wren's
              network-centrality as opposing pressure] — the coverage map is incomplete everywhere
              Wren moves, because everywhere Wren moves is somewhere Taylor has reasoned herself out
              of going. The map has a shape around her: negative space where the ward-junction
              contact should be, and [event: relational_anchor_status account opens] in Taylor's
              internal ledger as the first named absence.
            substance_delta:
              axes_in_motion:
                - axis: relational_anchor_status
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: null
                  notes: "Wren enters the coverage map as a named function-node; anchor account opens from rank 1 to rank 2; no cost-ledger entry because no value has been traded — the opening is structural, not transactional"
              axes_held:
                - axis: capability
                  rationale: "coverage continues at harm-reduction scope; no directive action; Wren's entry into the map is an observation, not a deployment expansion"
                - axis: moral_framework
                  rationale: "Taylor is not deploying insects toward Wren; the prohibition on directing is not tested; framework holds"
                - axis: moral_legibility_to_self
                  rationale: "the categorization is filed without examination; Taylor does not yet look at the aggregate; crack is not yet fired in this scene; legibility holds at pre-crack rank"
                - axis: social_tether-prot-rise
                  rationale: "Wren is categorized as a network-node, not yet as a relational contact; no tether-building"
                - axis: political_register-prot
                  rationale: "still street-level; no court content"
              density_target: 0.6-0.7
            scene_conflict:
              protagonist_force: "Taylor maps the ward systematically and files Wren as a function-node, maintaining operational discipline — no contact, no approach, coverage only"
              opposing_force: "Wren's network-centrality makes her presence in the map felt as negative space: everywhere she moves is everywhere Taylor cannot follow, and the map's incompleteness accumulates around her"
              stakes_axis: relational_anchor_status
            stale_since: null

          - slug: b01c02s03
            chunk: |
              End of day. Taylor runs the coverage map mentally — [event: Taylor does the full
              accounting of the precinct survey] the way she used to do homework, corner to corner,
              testing for gaps. Forty-three bodies she can roughly locate by fever-signature or
              traffic-pattern. [image: the scope of the map — forty-three people categorized without
              their knowledge]. She knows which three are running fever. She knows which alley
              junction goes quiet before dark and which one never does. She knows where children
              cluster in the afternoon, which means she knows where they are not at night.
              [force: the recognition arriving at the edge of the accounting] — she is doing it
              when it arrives: she has built a surveillance architecture over forty-odd people who
              do not know she exists, do not know they are being read, have not consented to any
              of it. [event: Taylor recognizes the coverage map as surveillance] — one beat, clean,
              the word arriving before she can prevent it. Then [event: Taylor suppresses the
              recognition and files the map under harm-reduction] — the next beat, equally clean:
              they would have died without her. Reading is not directing. The prohibition is where
              the line is and she has not crossed it. [mechanism: the suppression mechanism — harm-
              reduction accounting closes the ledger before reckoning can open it]. She does not sit
              with the recognition. She [force: the ledger closing as active discipline] files the
              ward-junction contact — Wren-unnamed, function-labeled — alongside the fever-cluster
              and the dark junction, and the accounting is done. [event: chapter closes with the
              coverage map intact and the ledger closed]. The crack is there, sealed under the entry.
            substance_delta:
              axes_in_motion:
                - axis: moral_legibility_to_self
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: null
                  notes: "recognition arrives (crack) and is immediately suppressed under harm-reduction framing; the ledger closes before reckoning can open; first non-linear uptick from rank 4 to 4.5; off-ledger by design — the crack is not yet a trade"
              axes_held:
                - axis: capability
                  rationale: "the map is complete as of this scene but nothing new is deployed; Taylor is accounting, not acting; capability stays at rank 3"
                - axis: moral_framework
                  rationale: "the suppression mechanism is harm-reduction rationalization, not a prohibition-category engagement; framework holds at crack-not-breach because the suppression is the discipline, not a breach of it"
                - axis: relational_anchor_status
                  rationale: "Wren is filed in the accounting (anchor account opened in s02) but not further examined; rank 2 holds through the close of the chapter"
                - axis: social_tether-prot-rise
                  rationale: "no active tether-building; Oswyn observing but no engagement"
                - axis: political_register-prot
                  rationale: "no court content; no resentment material"
              density_target: 0.6-0.7
            scene_conflict:
              protagonist_force: "Taylor runs the coverage map to completion and files it — the accounting is what she does instead of feeling it"
              opposing_force: "the recognition of what she has built — a surveillance architecture over forty people without consent — arrives in one beat and must be suppressed in the next"
              stakes_axis: moral_legibility_to_self
            stale_since: null

      - slug: b01c03
        status: bones-written
        bones_file: theater/bones/b01-c03.md
        bones_count: 36
        substance_bone_gate_verdict: PASS-PRAGMATIC   # cascade-budget: bone-gate verified inline at Phase 1 (4/4 axes EXACT vs chapter contract); per-bone audit deferred to /and-review bones b01c03
        bones_review:
          reviewed_at: 2026-05-27T00:00:00Z
          report_path: active-project/staff/reviews/bones-b01c03-2026-05-27.md
          verdict: PASS-WITH-NOTES
          bones_file_mtime_at_review: 1779852945  # 2026-05-27T03:35:45Z
          stale_since: null
          # Independent post-hoc re-fire of /and-review bones (deferred from cascade-budget c03 ship).
          # 0 HARD, 5 SIGNAL, 1 FLAG, 0 FAULT — supersedes the 2026-05-26 cascade-budget synthesis.
          # Prior cascade-budget report at active-project/staff/reviews/bones-b01c03-fidelity-2026-05-26.md preserved for cross-reference.
          # New signals over prior: signal-001 (bone 17 Taylor-as-subject of "registers" — minimal interiority, SVO recast fixable);
          #   signal-002 (bone 30 Jarvis "considers...for a beat" — non-POV cognition; ambiguous under bones discipline);
          #   signal-005 (Jarvis dialogue entry 6 — three embedded relative clauses violate westeros-smallfolk coordination-over-subordination register).
          # Carried from prior: s02 stakes-axis-not-dominant (thesis-correct), s03 stakes-axis-tied (hinge resolution), s03 irrevocability-element-thin (FLAG for stitching).
          # Cold-read prediction: HIGH on all 5 target elements; MEDIUM-HIGH on irrevocability — same disposition as prior.
          # None HARD, none blocking; all fixable at bone or dialogue scope if a downstream revise pass is dispatched.
        substance_delta_measured:
          axes_moved:
            moral_framework: -1.0       # s02n11 (flat 23, -0.5) + s03n04 (flat 29, -0.5)
            position-prot-rise: +1.0    # s01n11 (flat 11, +0.5) + s03n06 (flat 31, +0.5)
            social_tether-antag: +1.5   # s01n08 (flat 8, +0.5) + s02n04 (flat 16, +0.5) + s02n12 (flat 24, +0.5)
            social_tether-prot-rise: +1.0   # s01n08 (flat 8, +0.5) + s01n10 (flat 10, +0.5)
          density_measured: 0.6-0.8
          felt_verdict: PASS-PRAGMATIC   # audience scene-window review skipped under cascade budget; carries to /and-postop
        # /and-write b01c03 emit 2026-05-26 — cascade-budget compression.
        # Phase 1 screen-writer: 36 bones (s01=12, s02=13, s03=11); axis math EXACT 4/4 vs chapter contract.
        # Phase 1.5 dialogue: 10 utterances (Jarvis 7, Taylor 3); Earth-Bet fence clean.
        # Phase 2-6 audit chain: SKIPPED under cascade budget — bones authored under inline-discipline; full audit chain deferred to /and-review bones b01c03 + /and-postop b01c02 in c03 context.
        # Phase 7 emit: theater/bones/b01-c03.md + theater/facets/scene-map-b01-c03.md + theater/dialogue/{jarvis-coin-kl-courier,taylor-hebert-kl-122ac}.md.
        # Dialogue-anchor coverage: 10/10 bones cited; 0 bare speech bones; 0 missing speakers.
        # pl-2026-05-25-001 RESOLVED at contract update (s01n08 = flat 8 carries social_tether-prot-rise +0.5 cl01b second tranche; s01n10 = flat 10 carries +0.5 cl01b; total +1.0 court-layer half).
        #
        # /and-facets b01-c03 emit 2026-05-26 — cascade-budget compression.
        # R1 fanout: 11 authors landed; 78 facet entries (loc-state=5, NI=11 post-fixer, sensory=2, state-env=10, state-taylor=15, state-jarvis=13, memory=3, feeling=2, metaphor=0 zero-fires sustained, vibes=12, exposition=8→7 post-fixer DELETE exposition:5).
        # R2 fanout: SKIPPED under cascade-budget.
        # Phase 5 mechanical audit: 3 HARDs (exposition fire-rule clash exposition:5 @13 vs loc-state:2 @13; NI predicate-nominative saturation 50% > 40% threshold; NI co-citation gap at @10/@22/@31 per state-taylor cross-facet contract) — ALL RESOLVED at fixer (exposition:5 DELETED; NI:1+NI:5 syntactically recast to break saturation; NI:9/10/11 added at @10/@22/@31). 4 SIGNALs advisory.
        # Phase 5b audience-gate: SKIPPED under cascade-budget (pragmatic-accept; same disposition as 2026-05-25 c02). Carries advisory to /and-postop b01c02 in c03 context.
        # Phase 6 persist: complete.
        facets_path: active-project/theater/facets/
        round_1_complete: true
        round_2_complete: false   # R2 skipped under cascade-budget
        facets_status: audited-r1-mechanical
        facets_stale_since: null
        audit_path: active-project/staff/auditor/facets-final-audit.md
        audit_complete: true
        audit_findings: 7   # 3 HARDs resolved + 4 SIGNALs advisory
        audience_gate_path: null
        audience_gate_complete: false   # skipped under cascade-budget
        audience_gate_cycles: 0
        bidirectional_loop: not-validated   # R2 + audience-gate skipped under cascade-budget
        # /and-stitch b01-c03 emit 2026-05-26 — cascade-budget compression.
        # 3 Phase 1 scene-window forks; Phase 8 finalize; Phase 9 cold-read terminal gate.
        # Phase 9 cold-read: PASS (CONTINUE=yes; jeopardy textually grounded — Sera Hightower as named refusal-cost; causality clean; deferral earned).
        # Reader-gaps noted: POV name/nationality + bug-feed nature rely on prior-chapter setup; Westeros/modern register clash (Small Council + the feed) suggests crossover premise but not confirmed in-chapter — consistent with c02 dormancy + c01 establishment.
        stitched: true
        draft_file: active-project/draft/b01-c03.md
        render_log: active-project/staff/stitcher/render-log-b01-c03.md
        cold_read:
          read_at: 2026-05-26T00:00:00Z
          verdict: PASS
          recovered_summary: "POV defers one day on courier Jarvis Coin's proposal that Otto Hightower will protect Sera Hightower's birth-question from being raised in the Small Council in exchange for ward-traffic intelligence."
          report_path: active-project/staff/reviews/coldread-b01-c03-2026-05-26.md
          staging_signals: not-run-budget
          prose_rationale_audit: not-run-budget
          stale_since: null
          signal_clusters: []
          notes: |
            Chapter ships PASS (not PASS-WITH-CAVEATS like c02): CONTINUE=yes; jeopardy textually grounded (surveillance demonstrated as threat; Sera named as refusal-cost); causality clean; payoff is earned deferral (held-breath, not turn — but the hinge IS the deferral by design).
            The hinge dramatic-shape delivers what c02's dormancy-shape couldn't: a reader-engagement-yes verdict. The two-chapter pair now reads as the c02 surveillance-recognized-and-suppressed + c03 prohibition-engaged-as-variable sequence per series spine.
        # /and-substance chapter b01c03 Phase 6 persist 2026-05-26
        # Phase 5 review: pragmatic-accept under cascade-budget — math EXACT on all 4 axes vs chapter contract, scene_conflict populated with concrete forces, dramatic-shape hinge honored, cost-ledger anchors valid. Skipped 3-fork audience review for budget; carries advisory soft-watch to /and-postop.
        # pl-2026-05-25-001 RESOLVED at Phase 0 contract correction + persisted at Phase 6 (cl01b +1.0 social_tether-prot-rise anchored at b01c03s01).
        # Draft archived: active-project/staff/showrunner/_drafts/b01c03-draft-2026-05-26.md
        chunk: |
          Otto Hightower makes first contact through Jarvis Coin, a courier Taylor has seen
          in the lower city — not a summons, an observation: he knows what she did at the
          rescue, he knows she has been running coverage in the Hook, and he has a proposal.
          The chapter is structured around the proposal itself: Taylor gets its terms before
          she meets Otto. Otto wants calibrated intelligence about Flea Bottom — movement
          patterns, sickness clustering, which wards are agitated and which are quiet — routed
          upward through Jarvis; in exchange, he shields a court-tier ward from a succession
          exposure that would otherwise surface inside three months. The collision is that the
          proposal is accurate: the shielding is real, the ward (Sera) is genuinely at risk,
          and the intelligence Otto wants is intelligence Taylor is already running. She does
          not accept at chapter's end — she asks for a day. What shifts: the first sanctioned
          exception is now a named possibility; the prohibition has been price-tagged for the
          first time; social_tether-antag opens its account; the moral_framework crack becomes
          a calculable breach.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: moral_framework
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl02
              notes: "proposal received and engaged rather than refused; the prohibition is now a variable in a calculation; cl02 cost side opens"
            - axis: position-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl02
              notes: "Otto awareness of Taylor established; first position above anonymous; cl02 gain side"
            - axis: social_tether-antag
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl-antag-d03
              notes: "offer tendered = leverage embryonic; Otto gains first actionable knowledge of Taylor; cl-antag-d03 gain side"
            - axis: social_tether-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl01b
              notes: "court-layer half of cl01b settles here (ward-layer half settled at b01c01s03 Oswyn-categorization); Otto's awareness of the b01c01 rescue via Jarvis Coin completes the +2 cl01b gain. Resolves pl-2026-05-25-001 HARD parking-lot item."
          axes_held:
            - axis: capability
              rationale: "no new deployment; coverage continues at same level; the proposal has not been accepted"
            - axis: relational_anchor_status
              rationale: "Wren not yet in any calculus related to the proposal; anchor held outside the pricing discussion"
            - axis: political_register-prot
              rationale: "proposal meeting is transactional; no court-register observation content yet; resentment has no feed to form on"
          density_target: 0.6-0.8
          chapter_class: standard
        dramatic_shape: hinge
        goal: |
          Show the audience the proposal in full — terms, stakes, accuracy — and Taylor engaging rather than refusing, so the acceptance in b01c04 reads as a decision she reached, not a capitulation she suffered.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "witch-label formation active; intensifying"
            - "Wren: inside coverage map; named internally; no contact"
            - "Taylor's first moral_legibility crack: suppressed"
            - "Oswyn watching"
          world_state:
            - "KL 122 AC; Hook precinct coverage map active"
            - "Otto Hightower operational; Jarvis Coin active as lower-city courier vector"
          character_state:
            - "Taylor: capability rank 3; relational_anchor_status rank 2; moral_legibility rank 4.5"
            - "Wren: in coverage map; no contact"
            - "Otto: has identified Taylor; proposal ready; leverage embryonic"
            - "Jarvis: deployed as approach vector"
          source_chapter: b01c02
        handoff_out:
          open_threads:
            - "Otto's proposal: terms known to Taylor; Sera's exposure named; one-day decision window open"
            - "witch-label formation: courier contact now on top of rescue observation"
            - "Wren: still in coverage map; still outside the proposal calculus"
            - "moral_framework: prohibition now has a price tag; not yet licensed"
            - "social_tether-antag: leverage account opened"
          world_state:
            - "KL 122 AC; Jarvis Coin now a named contact for Taylor"
            - "Otto aware of Taylor and her capability; proposal tendered"
          character_state:
            - "Taylor: moral_framework rank 1 (prohibition named as variable); position-prot-rise rank 2; social_tether-antag at 2.5 (embryonic)"
            - "Wren: in coverage map; anchor account open; not in proposal calculus"
            - "Otto: leverage rank 2.5; waiting"
            - "Jarvis: active conduit"
          target_chapter: b01c04
        scenes:
          - slug: b01c03s01
            chunk: |
              [force: Taylor's street-discipline in the open market] has a shape she relies on: move slow, carry nothing worth taking, read the ward before anyone reads her. She is working the morning market in the Hook — not buying, reading — when [event: Jarvis Coin addresses Taylor by the description of what she did at the rescue] without preamble, without raising his voice. He does not say her name. He says: the foreign woman who cleared the crowd near Butcher's Lane on the day the Mudway child ran fever. Taylor goes still.
              [image: Jarvis Coin — unremarkable in the crowd, the stillness of someone who has waited at a particular stall for longer than commerce requires; his eyes on her before she processed him as a presence]. He does not step closer. The distance between them is the distance of a street-side negotiation, unremarkable to anyone passing. He knows she has been running coverage in the Hook: [mechanism: Jarvis names the scope and shape of Taylor's insect-feed deployment] — not the mechanism, not the insects — but the pattern that the mechanism produces: who moves, where the sick cluster, which alley-junctions she reads twice in a morning. The feed's ghost, reconstructed from its behavioral shadow.
              [force: the precision of address as the leverage being demonstrated] lands before Taylor can classify it as threat or offer: he has her pattern read accurately enough that the contact itself is proof of capability, not merely an announcement of intention. [event: Taylor recognizes she has been under observation] — the coverage map she has been running has a mirror she did not build. He does not explain who he works for. He says: there is a person who has an interest in what she knows, and would like to put a question to her. He names no names, no titles, no ward.
              [event: social_tether-prot-rise account completes cl01b court-layer half] — the rescue at Butcher's Lane, witnessed and filed, has traveled upward through Jarvis to a patron-layer Taylor has not yet been told the name of. The tether she thought was street-level has a second floor she did not know about. She asks where and when. [mechanism: Taylor agrees to a location and time before she has decided whether to attend] — the street-discipline that governs her does not break under surprise; she agrees because refusing in an open market tells the watcher more than agreeing does. She does not look at him when she answers.
            substance_delta:
              axes_in_motion:
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl01b
                  notes: "cl01b court-layer half settles here: Otto's awareness of the b01c01 rescue via the Jarvis-courier vector is the second floor of the tether Taylor thought was street-only; completes the +2 cl01b gain that opened at b01c01s03"
                - axis: social_tether-antag
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl-antag-d03
                  notes: "Otto now has an actionable contact; cl-antag-d03 partial open; lever embryonic but in-hand"
                - axis: position-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl02
                  notes: "Taylor named-by-courier; no longer anonymous at courier-tier; cl02 partial gain"
              axes_held:
                - axis: capability
                  rationale: "no new deployment; contact, not operation"
                - axis: moral_framework
                  rationale: "no proposal received; prohibition not yet a variable; framework holds at pre-engagement rank"
                - axis: relational_anchor_status
                  rationale: "Wren not part of this contact layer; anchor at rank 2"
                - axis: political_register-prot
                  rationale: "no court-register content through feed; resentment has no material"
              density_target: 0.6-0.7
            scene_conflict:
              protagonist_force: "Taylor maintaining street-discipline — agrees to a time and location without signaling whether she will attend, because refusal in the open is a form of acknowledgment"
              opposing_force: "Jarvis's precision of address — the coverage pattern he names back to Taylor is accurate enough that the contact itself is the leverage being demonstrated; her anonymity is already spent"
              stakes_axis: social_tether-prot-rise
            stale_since: null

          - slug: b01c03s02
            chunk: |
              The meeting place is a cooper's yard off Eel Alley — no foot traffic past the third bell, no clear sightlines from the lane-mouth. Taylor is there before Jarvis. [force: Taylor's discipline of arriving early] — she reads the yard with the feed before she enters it, maps the two workers still coopering at the near shed, the boy clearing hoops at the far end. Jarvis arrives at the third bell. He has no document, no letter, no seal. He delivers the proposal in plain Westerosi with the cadence of someone who has delivered plain proposals before.
              [event: Jarvis names Otto Hightower as the patron] — the Hand who was, the man who still runs channels the Small Council does not audit. Taylor registers the name and does not react to it. [mechanism: Jarvis delivers the intelligence terms] — movement patterns in the wards below Rhaenys's Hill, sickness clustering in the seasons before winter-pressure, which junctions run agitated and which run quiet in the weeks around court decisions. Information Taylor is already running. Routed upward through Jarvis at a frequency and detail she would determine. [event: Jarvis names Sera Hightower and the succession exposure] — a court-tier ward in the Queen Consort's household, legitimacy question latent but surfaceable inside three months through a mechanism Jarvis names in one sentence. The shielding is real. Jarvis does not oversell it.
              [force: the proposal's accuracy as the opposing pressure] — Taylor runs the accounting while he speaks and the problem is that the accounting works: the ward Jarvis names is genuinely at risk; the intelligence she would route is intelligence she is already running; the mechanism of shielding is one Otto Hightower can operationalize. [image: the prohibition as a variable in a calculation] — not a fence she is approaching but a term on one side of a ledger where the other side has a named cost attached to refusal. [event: Taylor acknowledges she has understood the terms] — she does not say yes or no; she says she has heard them. [mechanism: moral_framework engages the prohibition as a calculation rather than a fence] — the proposal is accurate enough that it cannot be refused on the grounds of inaccuracy, cannot be refused on the grounds of inadequate stakes, cannot be filed under harm-reduction and closed.
              [event: social_tether-antag full leverage articulated] — the trade-shape exists now as a specific named exchange in the world; Otto has the shape of what Taylor knows; she knows the shape of what he can provide; the lever is no longer embryonic. It has a named ward on one end.
            substance_delta:
              axes_in_motion:
                - axis: social_tether-antag
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl-antag-d03
                  notes: "full leverage articulated: terms named on both sides; trade-shape exists as a specific named exchange; cl-antag-d03 second tranche"
                - axis: moral_framework
                  direction: down
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl02
                  notes: "prohibition now a variable in a calculation: Taylor acknowledges the terms; not yet breached but no longer purely operative as a fence; cl02 partial cost-side"
              axes_held:
                - axis: capability
                  rationale: "no new deployment; proposal not accepted"
                - axis: position-prot-rise
                  rationale: "no new position movement; terms named but not accepted; opened at s01, does not move further here"
                - axis: social_tether-prot-rise
                  rationale: "settled at scene 1 via cl01b; no further movement"
                - axis: relational_anchor_status
                  rationale: "Wren outside the proposal calculus by contract; anchor at rank 2"
                - axis: political_register-prot
                  rationale: "proposal delivered in plain register; no court-feed observation content; resentment has no material"
              density_target: 0.7-0.8
            scene_conflict:
              protagonist_force: "the discipline that reading-is-not-directing demands refusal of any arrangement that routes her knowledge upward through a patron-chain"
              opposing_force: "the proposal's accuracy — Sera is named and genuinely at risk, the intelligence Taylor would route is intelligence she is already running, and refusal costs a court-tier life Taylor could prevent losing; the ledger opens on both sides with the same weight"
              stakes_axis: moral_framework
            stale_since: null

          - slug: b01c03s03
            chunk: |
              Jarvis is still. He has delivered the proposal; he does not add to it. The cooper's yard has the same workers, the same hoop-stacking boy at the far end, the same tallow-damp from the lane-caulking two alleys over. [force: Taylor's discipline of not-deciding-under-pressure] — the rule she has kept since arriving in King's Landing, since before that, since the last time she made a decision under pressure at scale. She does not decide when pressed. She says: [event: Taylor asks for a day].
              Jarvis considers her for a beat — [image: the beat in which a courier registers that the answer was not refusal] — and says he will return at the same place at the first bell on the day after. He does not ask why she needs a day. He does not appear relieved or disappointed. He leaves the yard with the same unhurried movement he arrived with.
              Taylor does not move immediately. She holds the position she has held since he began the proposal: back to the shed wall, clear line to the yard-mouth, feed running on the barrel-workers and the boy. [mechanism: the act of asking for a day as engagement rather than refusal] — Taylor does not say she will not come back. She does not say she will not accept. She says she needs time to think, and the form of what she has said is not the form of refusal. [event: moral_framework prohibition price-tagged for the first time] — the fence has a price on the other side of it. [force: the chapter's hinge — the act of asking for a day IS the engagement; refusal-as-form is no longer available now that the terms have been spoken and acknowledged and deferred rather than refused].
              [event: Taylor does the accounting before she leaves the yard] — not calculating whether to accept, but running the perimeter: capability as already running, the ward as real, the coverage as already there. She is doing the work. She has been doing the work. The proposal is asking her to name it to someone else. [event: position-prot-rise registers Taylor's response as decision-pending] — not refusal; the patron has registered an engaged interlocutor. Taylor leaves the yard. [image: the coverage map and the open ledger line as the same thing, in the same place, requiring the same answer].
            substance_delta:
              axes_in_motion:
                - axis: moral_framework
                  direction: down
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl02
                  notes: "prohibition price-tagged: asking for a day is engagement, not refusal; the chain is started; cl02 second tranche cost-side"
                - axis: position-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl02
                  notes: "Otto registers response as decision-pending, not refusal; Taylor named-function at courier-tier representing court; cl02 second tranche gain-side"
              axes_held:
                - axis: capability
                  rationale: "no new deployment; accounting is mental, not operational"
                - axis: relational_anchor_status
                  rationale: "Wren outside proposal calculus; anchor at rank 2; contract holds through chapter close"
                - axis: social_tether-prot-rise
                  rationale: "settled at scene 1; no further movement through chapter close"
                - axis: social_tether-antag
                  rationale: "no new leverage; existing tether holds at scene-2 magnitude; deferred answer does not extend or retract the lever"
                - axis: political_register-prot
                  rationale: "no insect-feed court content; Taylor in a cooper's yard running internal accounting; resentment has no material"
              density_target: 0.6-0.7
            scene_conflict:
              protagonist_force: "Taylor's discipline of not-deciding-under-pressure — buys a day to think rather than accepting or refusing on the courier's time"
              opposing_force: "the chapter's hinge — asking for a day is itself the engagement; refusal-as-form is no longer available now that the terms have been spoken, acknowledged, and deferred; the prohibition has been price-tagged and the ledger cannot un-open"
              stakes_axis: moral_framework
            stale_since: null

      - slug: b01c04
        status: bones-written
        bones_file: theater/bones/b01-c04.md
        bones_count: 39
        substance_bone_gate_verdict: PASS
        bones_review:
          reviewed_at: 2026-05-27T00:00:00Z
          report_path: active-project/staff/reviews/bones-b01c04-2026-05-27.md
          verdict: PASS-WITH-NOTES   # post-inline-fix; at-review the auditor returned 1 HARD; fault-001 resolved via Jarvis @9 entry 8 word-swap (acceptable → takes); see fixer-log
          bones_file_mtime_at_review: 1779903472   # 2026-05-27 post-fix mtime
          stale_since: null
          # Auditor returned 1 HARD (FAULT-DIALOGUE-CARD-VIOLATION — "acceptable" is forbidden Latinate per westeros-smallfolk card) + 2 SIGNAL (stakes-axis tie all 3 scenes — TASTE-FLAG per magnitude-floor consequence; s03 CHATTER-OVER-CAP carry-forward) + 3 FLAG (advisory).
          # Inline fix: Jarvis @9 entry 8 "Those terms are acceptable to the man I serve" → "The man I serve takes those terms" (Anglo-Saxon "takes"; no copula; subject-first; smallfolk register).
          # Part B chunk fidelity: PASS-WITH-NOTES (all chunk tags covered; 1 advisory thin in s02).
          # Part C cold-read prediction: 6 goal elements all HIGH or MEDIUM; MEDIUMs are facet-layer-dependent (Oswyn ethical register, Wren-anchor closing thesis-trio synthesis); no LOW.
          # Recurrence note (process-critic candidate): chunk-text seed line ("those terms are acceptable to the person he represents") propagated the Latinate term into dialogue authoring at /and-write Phase 1.5; the dialogue-writer flagged it as card-pressure and retained for seed-fidelity. Pattern candidate.
        substance_delta_measured:
          axes_moved:
            capability: +2.0      # s02n03 (flat 15, +1.0) + s03n03 (flat 27, +1.0); EXACT vs target +2.0 (revised at Phase 1 redo from +1.5)
            position-prot-rise: +1.0   # s01n08 (flat 9, +1.0); EXACT vs target +1.0 (consolidated from prior +0.5+0.5 split to single 1.0 bone)
            social_tether-prot-rise: +2.0   # s02n06 (flat 18, +1.0) + s03n07 (flat 31, +1.0); EXACT vs target +2.0
            social_tether-antag: +1.0   # s01n06 (flat 7, +1.0); EXACT vs target +1.0
            position-world: +1.0   # s03n09 (flat 36, +1.0); EXACT vs target +1.0
          density_measured: 0.65-0.8
          felt_verdict: SUBSTANCE-FELT-3-of-3   # all 3 audience personas, all 9 cells (3 scenes × 3 personas) — Phase 6 bone-gate
        # /and-write b01c04 emit 2026-05-27 — TWO-CYCLE invocation (DEC-0030 Phase 1 redo + Phase 6 additive held-bones).
        # Phase 1 cycle 1 (original): 38 bones → Phase 2 audit returned 45 HARDs (33 FAULT-FORM-MODIFIER PPs + 11 magnitude-0.5-below-floor + 1 speech-bone-no-axis).
        #   Root cause: screen-writer referenced c03 bones as cadence model; c03 was PP-heavy + 0.5-split because c03 Phase 2 was cascade-budget-skipped (never SVO-form audited).
        # Phase 1 cycle 2 (DEC-0030 redo): 33 bones with strict SVO + magnitude floor 1.0 + c02-canonical reference; chapter contract capability +1.5 → +2.0 to support single-1.0 bones per scene.
        #   Phase 2 re-audit: 2 HARDs (actor-slug abbreviations + s01n10 shape-mismatch) — all inline-fixed (oswyn-mudway → oswyn-mudway-flea-bottom-elder; wren-stitch-house → wren-stitch-maker-flea-bottom-ward; s01n10 chatter → held).
        # Phase 3 dramatist: ACCEPT (rise-peak-fall shape; 0 missing transitions; speech-form clean; goal landing PASS).
        # Phase 4 audience trim 3-of-3: ACCEPT (33 KEEP / 0 DELETE-PROPOSE). Cycle-1 termination.
        # Phase 4.5 dialogue re-anchor: Taylor entry 2 (@9 work-naming) DROPPED (un-anchored by redo); Jarvis entries 8 + 9 re-anchored to consolidated bone s01n08 (multi-citation [jarvis-coin-kl-courier:8, jarvis-coin-kl-courier:9]).
        # Phase 5 continuity: FAIL 4 HARDs + 1 FLAG.
        #   - fault-003 (FAULT-STATE): chunk-text "third-bell appointment" → "first-bell" (inline fix).
        #   - fault-004 (FLAG): Oswyn state file location/trade broadened to reflect cross-ward day-labor pattern; chunk image revised (was "fever-burned look long gone" — incoherent for ~55yo elder; now "the elder doing penny-a-barrel labor").
        #   - fault-005/006/007 (FAULT-REFERENCE × 3): margit authored oc-cooper-yard-eel-alley + oc-pig-tallow-lane + oc-ropers-court (library + warehouse + INDEX).
        #   - Residual: margit's pig-tallow-lane warehouse card imported pre-fix Oswyn text; inline fixed.
        # Phase 6 substance bone-gate cycle 1: FAIL 5 HARDs (HELD-AXIS-NOT-WITNESSED) + audience 3-of-3 SUBSTANCE-FELT 9-of-9.
        # Phase 6 additive (5 held bones added; no existing bones modified):
        #   s01: +n01a (political_register-prot held; "cooper's-yard workers hold the smallfolk-hours murmur") + n08a (capability held; "the insect-feed holds the hook-range")
        #   s02: +n07a (political_register-prot held; "Pig Tallow Lane returns ward-tier bodies only")
        #   s03: +n08a (moral_framework held; "the report-sheet holds at ward-pattern observation") + n08b (political_register-prot held; "the report-sheet holds at Flea Bottom-tier source-content") + n08c (position-prot-rise held; "the courier-arrangement holds the conduit-rank")
        # Phase 6 re-audit: PASS — 0 HARD; 3 SIGNAL all ACCEPTED (new-flag-001: "only" qualifier on s02n07a borderline; new-flag-002: s01n01a holds-license-extension to collective-group subject + redundant against n05; new-signal-001: s03 CHATTER-OVER-CAP persists 60% non-chatter vs 70% floor — accepted as structural consequence of held-bone concentration in s03).
        # Phase 6.5 admin process-critic: dispatched (3 SIGNALs all accepted triggers).
        # Phase 7 emit: theater/bones/b01-c04.md (39 bones; 12+12+15 across s01/s02/s03) + theater/facets/scene-map-b01-c04.md + dialogue files re-anchored @7 (Taylor) + @9 (Jarvis ×2 utterances on consolidated bone).
        # Dialogue-anchor coverage: 1 anchor in s01n06 (Taylor:1) + 1 anchor in s01n08 (Jarvis:8 + Jarvis:9 multi-citation). Earth-Bet fence clean.
        # pl-2026-05-27-001 (c03-bones-svo-form-contamination): still open; process-critic to surface whether PROP needed.
        facets_path: active-project/theater/facets/
        round_1_complete: true
        round_2_complete: true
        facets_status: audited-r1
        facets_stale_since: null
        audit_path: active-project/staff/auditor/facets-final-audit.md
        audit_complete: true
        audit_findings: 8 HARDs (all resolved inline) + 11 SIGNAL/TASTE-FLAG
        audience_gate_path: active-project/staff/auditor/facets-audience-gate-r3.md
        audience_gate_complete: true
        audience_gate_cycles: 3
        audience_gate_cap_burned: false   # per DEC-0035; TASTE-FLAG carry-forward chosen over cap-burn DELETE
        taste_flag_residue:
          - TF-001: sensory-disambiguation-pedant — sensory:2 @13 cross-location old-state (specialist disagreement)
          - TF-002: dark-fantasy-reader — state:13 actors_in_yard anchor @37 vs @39 reality-axis (1/3 dissent)
          - TF-003: cape-fic-reader — vibes:4 single-exit-geometry + vibes:2 modification-of-terms middle token (1/3 dissent)
          - TF-004: cape-fic-reader — exposition:1 prior-bridge closing clause orientation (1/3 dissent, cycle-1 carry)
          - TF-005: dark-fantasy + worm-canon — feel:1 @7 generic / feel:2 @39 four-count card-verify (1/3-each per-entry)
          - TF-006: dark-fantasy — metaphor refusal log silent on @22/@38/@39 (1/3 documentation request)
          - TF-007: cape-fic — narrator:9 @38 middle clause AP2 paraphrase (1/3 cycle-1 carry)
        bidirectional_loop: validated   # multiple shared findings across auditor + audience paths
        # /and-facets b01-c04 emit 2026-05-27. 3-cycle audience-gate completion per DEC-0033/0034/0035.
        # R1 fanout: 12 authors landed; 71 facet entries (loc-state=6, NI=9, sensory=3, state-env=14, state-taylor=7, state-jarvis=8, memory=3, feeling-taylor=2, feeling-jarvis=0, metaphor=0, vibes=16, exposition=3).
        # R2 fanout: 7 judges (NI/memory/feeling-taylor/metaphor/exposition/dialogue-taylor/dialogue-jarvis). NI K=7 D=2 A=5; memory K=1 D=2 A=1; feeling-taylor K=2; metaphor K=0; exposition K=0 R=3 (all REWORD on word-cap); dialogue clean.
        # Phase 4 cite-index regen: 19 author copies merged; consolidated feeling.md + state-updates.md.
        # Phase 5 audit: FINDINGS-PRESENT — 8 HARD + 11 SIGNAL; all HARDs RESOLVED inline (dialogue ID collision fix; forward-cite strips; carve-out preamble adds; narrator:14 + vibes:7 deletions; memory + NI body-level preambles).
        # Phase 5b cycle 1 (33 reviewers): 9 of 11 facets FAILed strict 3-of-3; 2 PASS (loc-state + dialogue-taylor).
        # Phase 5b cycle 2 (5 targeted re-reviewers; structural fixes per DEC-0034): 0 facets flipped fully; structural fixes accepted by cited reviewers but content REVISEs persist.
        # Phase 5b cycle 3 (4 fixer dispatches + 11 audience re-reviewers; targeted content fixes per DEC-0035): 2 more facets flipped to 3/3 ACCEPT (NI, memory); 7 facets PASS-with-TASTE-FLAG-residue.
        # Cumulative /and-facets b01-c04 dispatches: 12 R1 + 7 R2 + 1 audit + 33+5+11 audience + 4+1 fixers + 5 admin = ~79 dispatches across 3 cycles.
        # Final cycle-3 disposition: 4 facets 3/3 clean ACCEPT (loc-state, dialogue-taylor, NI, memory); 7 facets PASS-with-1/3-TASTE-FLAG per DEC-0035 (sensory, state-updates, vibes, feeling, metaphor, exposition, dialogue-jarvis).
        # Phase 5c admin process-critic: pending (auto-fires on REVISE in final cycle even with TASTE-FLAG-classification).
        stitched: true
        draft_file: active-project/draft/b01-c04.md
        cold_read:
          read_at: 2026-05-27T00:00:00Z
          verdict: PASS
          recovered_summary: "A surveillance-capable narrator trades ward-pattern intelligence to an unseen patron through a courier, in exchange for someone named Sera being kept safe."
          report_path: active-project/staff/reviews/coldread-b01-c04-2026-05-27.md
          staging_signals: 0   # /and-review staging deferred under cascade-budget; not run
          staging_report_path: null
          signal_clusters: []
          prose_rationale_audit:
            report_path: active-project/staff/reviews/prose-rationale-audit-b01-c04-2026-05-27.md
            verdict: PASS
            held_bones_scanned: 10
            prose_rationale_mute_count: 0
            threshold: not-met
          stale_since: null
        # /and-stitch b01-c04 emit 2026-05-27. Single-arm scene-window (3 forks); persona neutral; voice-exemplar series-level (1st-person; cadence transferred, no content leak).
        # Phases 2-6 inline-mechanical (scene-window forks pre-applied fusion); Phase 7 per-scene Q-line sweep (3 forks; 4 CUT + 7 CUT-CLAUSE + 2 REWORD + 1 CUT-ASININE; 1 FAULT-EXPOSITION-AUDIT-MISS recovered — Phase 7 scene-C fork stripped exposition:3 Roper's-Court em-dash-fold gloss on Q5/Q7 grounds; orchestrator restored verbatim per exposition carve-out).
        # Phase 8 finalize: 39 bones rendered / 0 dropped; 68 facets balanced; 3 dialogue utterances verbatim; 1694 words; 68 sentences; no scene-callout markers; clean draft only (no annotated under cascade-budget compression per c03 precedent).
        # Phase 9 cold-read: PASS (events recovered: acceptance + routing-operation + report-handoff + Wren-exclusion + chapter-close-thesis "carries both at the same count"; continue=tentative-yes; jeopardy "soft and offstage" but not literal no-jeopardy; cold-read identified onboarding gaps for "the feed" / Sera / Otto as c01-c03-context-dependent, not c04 defects).
        # Phase 9 Step 3.5 prose-rationale-mute audit: PASS 10/10 (all held bones — additive @2/@10 scene-A, @16/@20/@22/@23 scene-B, @33/@34/@35/@38 scene-C — carry concrete physical/perceptual tokens on the page).
        # Phase 9 Step 3 staging review: DEFERRED (cascade-budget; /and-review staging not run).
        # Phase 9.5 admin process-critic: SKIPPED (clean PASS + signal_clusters[] empty per Phase 9.5 rule).
        # Depth-pass: NOT REQUIRED (clean PASS; no MANDATORY flag); optional --from-signals available if user wants tightening on the cold-read's "soft jeopardy" surface or the mid-walk interior-cartography stretch noted by cold reader (lines 22-53).
        # /and-substance chapter b01c04 Phase 6 persist 2026-05-27.
        # Phase 5 review: 4 ACCEPT (dramatist, cape-fic-reader, dark-fantasy-reader, worm-canon-pedant)
        #   + 1 FAIL (auditor: 2 HARD, 4 SIGNAL). Admin DEC-0028 adjudication:
        #   - fault-001 POV: OVERRIDE — c01/c02/c03 scene chunks all third-limited with first-person
        #     rendered prose; chunk-layer third-limited is established convention. Tail-step: admin
        #     process-critic dispatch for card-text clarification on cond-taylor-pov-behavior.card.md.
        #   - fault-002 cl-antag-d03 math: FIXED — notes corrected at both b01c04-draft.md s01 and
        #     memory.md chapter-level (this entry, line 3053). Original "completed" claim was
        #     mathematically incorrect from book-authoring 2026-05-24.
        # Phase 6 SIGNALs surfaced to /and-write (advisory soft watches):
        #   - moral_framework crack-widening in held-rationale without Δ (potential book roll-up gap)
        #   - cl-world-d04 "delivered" phrasing ambiguous (full +2 entry or +1.0 tranche)
        #   - political_register-prot held-rationale identical across 3 scenes (borderline boilerplate)
        #   - s03 mechanism tag names thesis verbatim (theme-silence violation risk — must not surface
        #     as inner monologue at /and-write)
        # Audience soft watches to /and-write:
        #   - cape-fic-reader: s01 position-prot-rise needs distinct bones-level event; s03 position-world
        #     needs physical handoff image (not bracket-declaration)
        #   - dark-fantasy-reader: s01 rationalization watchpoint at execution layer (text watches the
        #     distinction; does not do suppression's work for Taylor)
        #   - worm-canon-pedant: four-ward coverage must be built as sequential acquisition across two
        #     days in bone structure; no single-deployment bone collapsing temporal spread
        #   - worm-canon-pedant: s02 "without examining why she holds it" + s03 "Taylor does not
        #     examine whether it will hold" — anchor-discipline lines must survive as bone-level
        #     content, not collapse to single assertion bones
        # All 5 axes EXACT vs chapter targets (capability 1.5, position-prot-rise 1.0, social_tether-
        #   prot-rise 2.0, social_tether-antag 1.0, position-world 1.0). Thematic-axis-coverage
        #   satisfied (social_tether-prot-rise stakes_axis for s02 + s03).
        # Reviewer reports: dramatist-b01c04-substance-2026-05-27.md, auditor-b01c04-substance-2026-05-27.md;
        #   audience reviews in audience/{cape-fic-reader,dark-fantasy-reader,worm-canon-pedant}/stm.md
        #   under heading "## b01c04 chunk review — 2026-05-27".
        # Draft archived: active-project/staff/showrunner/_drafts/b01c04-draft-2026-05-27.md
        #
        # /and-substance chapter b01c04 revise 2026-05-27 — chunk-layer soft-watch addressing pre-/and-write.
        # 6 chunk-layer edits applied (no math change; all axis sums still EXACT):
        #   - s01 moral_framework rationale: stripped "crack widened" phrasing → "framework still named and
        #     believed; not interrogated as compromised; no Δ on this axis" (auditor SIGNAL: held-rationale
        #     acknowledging crack without posting Δ → potential book-roll-up gap)
        #   - s01 political_register-prot rationale: specified "courier-tier exchange in a cooper's yard"
        #     (auditor SIGNAL: borderline boilerplate across 3 scenes)
        #   - s02 moral_framework rationale: same "crack" strip + clarified the un-examined-distinction IS the
        #     discipline (not its violation)
        #   - s02 political_register-prot rationale: specified "ward-level walk; coverage substrate is
        #     foot-traffic, sickness-clustering, alley-agitation" (boilerplate SIGNAL)
        #   - s03 moral_framework rationale: same strip + framework-still-named-and-believed framing
        #   - s03 political_register-prot rationale: specified the report's content (junction-agitation,
        #     ward-pattern from Flea Bottom-tier sources)
        #   - s03 cl-world-d04 note: clarified "first tranche (+1.0 of +2 ledger gain; second +1.0 lands at
        #     d07)" (auditor SIGNAL: "delivered" phrasing ambiguous)
        #   - s03 prose: report-handoff sharpened to physical image — "single sheet folded twice in plain hand,
        #     passed across the half-step of yard-air; Jarvis takes it without opening it and slides it inside
        #     his coat" (cape-fic SIGNAL: position-world needs physical handoff image, not bracket-declaration)
        #   - s03 prose: closing mechanism tag rewritten to drop verbatim thesis — now "reading-the-ward and
        #     routing-what-is-read collapse into one continuous operational form" (auditor SIGNAL: s03 mechanism
        #     tag named thesis verbatim → theme-silence violation risk if /and-write extracts as event_map)
        # Bone-layer soft watches NOT addressed at chunk (deferred to /and-write): s01 position-prot-rise distinct
        #   bones-level event (cape-fic); s01 rationalization watchpoint at execution layer (dark-fantasy);
        #   four-ward sequential acquisition across 2 days (worm-canon, already explicit in chunks);
        #   anchor-discipline lines preservation as bone-level content (worm-canon).
        # PROP-0008 applied: cond-taylor-pov-behavior.card.md layer-scope clarified (library + active-project
        #   copies); fault-001 will not recur on future Phase 5 passes.
        chunk: |
          Taylor accepts Otto's proposal. The chapter covers the acceptance and its immediate
          operational consequences: Taylor expands her insect coverage beyond the Hook into
          three adjacent wards, begins routing movement-pattern intelligence through Jarvis,
          and receives the first confirmation that Sera's exposure is being managed. The
          network-build is substantial — this is the Flea Bottom intelligence layer Otto
          cannot acquire any other way, and Taylor executes it with the same systematic
          thoroughness she applied to Flea Bottom triage. The collision is the tether-gain
          reading as future-cost collateral: the same expansion that makes Sera's protection
          viable makes Taylor non-extractable in a direction she has not calculated. Oswyn
          Mudway becomes an active (unknowing) node in the coverage map. What shifts:
          capability is up materially, position-prot-rise confirms itself, social_tether-prot-
          rise is now load-bearing in formation, and the Flea Bottom intelligence layer
          delivers its first position-world increment to the Green consolidation.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: capability
              direction: up
              target_delta_magnitude: 2.0
              cost_ledger_anchor: cl03a
              notes: "network expands across three wards; Khepri-rhyming architecture beginning to form; cl03a gain side. Adjusted from +1.5 to +2.0 at /and-write Phase 1 redo 2026-05-27 to honor bone-level magnitude floor of 1.0; chapter coverage extends across 2 scenes, each delivering 1 full rank (s02 +1.0 both adjacent wards, s03 +1.0 third-ward completion)."
            - axis: position-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl02
              notes: "acceptance confirmed; Taylor now Otto's informal intelligence conduit; position above anonymous; cl02 gain completed"
            - axis: social_tether-prot-rise
              direction: up
              target_delta_magnitude: 2.0
              cost_ledger_anchor: cl03b
              notes: "network-build tether gain; Oswyn active node; Jarvis structural vector; tether load-bearing in formation; cl03b gain side (future-cost collateral flagged)"
            - axis: social_tether-antag
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl-antag-d03
              notes: "acceptance = leverage solidified; Otto gains proportional to Taylor's position-rise; cl-antag-d03 third tranche (+1.0 of +4 total; c03 delivered +1.5, c04 adds +1.0, +1.5 outstanding for later d05–d10 chapters before cl-antag-d10 opens). 2026-05-27 correction: original 'completed' claim authored at /and-substance book b01 2026-05-24 was mathematically incorrect; auditor caught at /and-substance chapter b01c04 Phase 5 fault-002; DEC-0028 approved fix."
            - axis: position-world
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl-world-d04
              notes: "Flea Bottom intelligence layer delivered; Green consolidation gains first KL street-layer intel; cl-world-d04"
          axes_held:
            - axis: moral_framework
              rationale: "acceptance is the licensed exception but rationalization is not yet complete; the crack has widened but the framework is still named and believed"
            - axis: relational_anchor_status
              rationale: "Wren enters network coverage but not the protection calculus; anchor held outside pricing"
            - axis: political_register-prot
              rationale: "no court-register observation content yet; Taylor's feed is Flea Bottom-tier; resentment material not yet present"
            - axis: moral_legibility_to_self
              rationale: "acceptance is rationalized successfully at this chapter; legibility crack suppressed; recognition deferred"
          density_target: 0.6-0.8
          chapter_class: standard
        dramatic_shape: rising
        goal: |
          Show the audience the acceptance and the network expansion together so the tether-gain reads as future-cost collateral — the protection and the trap are the same operation.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "Otto's proposal accepted in principle; Taylor has one day to confirm"
            - "moral_framework: prohibition now a calculable variable"
            - "Wren: in coverage map; outside proposal calculus"
            - "social_tether-antag: embryonic leverage account open"
          world_state:
            - "KL 122 AC; Jarvis active; Otto waiting"
            - "Sera's succession exposure: three-month window named"
          character_state:
            - "Taylor: moral_framework rank 1; position rank 2; relational_anchor rank 2; social_tether-prot-rise forming"
            - "Otto: leverage embryonic, waiting"
          source_chapter: b01c03
        handoff_out:
          open_threads:
            - "Flea Bottom intelligence layer: active and routing through Jarvis to Otto"
            - "Sera's exposure: being managed; protection confirmed functional"
            - "Oswyn Mudway: active unknowing node in coverage map"
            - "cl03b future-cost collateral: tether gain logged as downstream -7 risk — not yet visible to Taylor"
            - "witch-label formation: network expansion accelerates community notice"
            - "Wren: in expanded coverage map; outside protection calculus"
          world_state:
            - "KL 122 AC; Flea Bottom four-ward coverage active; Green faction receives first street-layer intel"
            - "position-world rank 6 (first increment delivered)"
          character_state:
            - "Taylor: capability rank 4.5; position-prot-rise rank 3; social_tether-prot-rise rank 3 (load-bearing in formation); moral_framework rank 1 (cracked, licensed exception active)"
            - "Wren: in expanded map; anchor rank 2; not in calculus"
            - "Otto: leverage rank 3.5; Sera's exposure managed; arrangement functional"
            - "Oswyn: unknowing node; coverage substrate deepening"
          target_chapter: b01c05
        scenes:
          - slug: b01c04s01
            chunk: |
              Taylor is back in the cooper's yard at the first bell [event: Taylor returns to the meeting place], the same tallow-damp in the lane, the same shed-wall at her back. She does not review the decision in the feed. She made the decision in the night when the accounting would not close any other way, and reviewing it now is not the form of the discipline she keeps. Jarvis arrives inside the bell's decay — [image: Jarvis Coin unhurried in the lane-mouth, checking nothing, his gait the gait of a man with no appointment to be late for]. He reads her face before she speaks.

              [force: Taylor's formal delivery of the yes] comes with the only modification she has named to herself: the intelligence she routes will be what the feed reads, rendered as pattern-report, and the volume and interval are hers to determine. She says as much. Jarvis does not negotiate. He says: those terms are acceptable to the person he represents. He says it with the specific flatness of a courier confirming receipt, not a man recording a victory. [mechanism: Jarvis receives the acceptance as a routing confirmation, not a concession extracted]. The exchange takes less time than the walk to the yard.

              [event: Taylor's acceptance delivered and acknowledged — leverage solidifies for Otto] — the lever is no longer a question of whether; it is now a question of how much. [force: the knowledge that delivering the yes ends her capacity to not-have-delivered-it] sits flat in Taylor's chest — not regret, not relief, the particular quality of weight that follows any irreversible operational act. [mechanism: moral_framework holds the acceptance as a licensed exception, the harm-reduction logic running its own accounting: Sera is real, the ward is real, the intelligence is already running]. She is not naming a patron. She is naming a destination for what she already knows. The distinction is real. She holds it.

              [event: Jarvis confirms first routing protocol — next contact at the same place, same bell, three days hence] — [image: the yard as a fixed coordinate, the third-bell-return as a recurring calendar item that has just been installed in Taylor's week without ceremony]. Jarvis leaves. Taylor checks the feed at the yard's perimeter, reads nothing anomalous, and goes.
            substance_delta:
              axes_in_motion:
                - axis: social_tether-antag
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl-antag-d03
                  notes: "acceptance delivered and acknowledged; Otto's lever solidified from embryonic to operational; cl-antag-d03 third tranche (+1.0 of +4 total; c03 already delivered +1.5, c04 adds +1.0, +1.5 still outstanding for d05–d10 chapters before cl-antag-d10); Taylor can no longer un-be-the-intelligence-source"
                - axis: position-prot-rise
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl02
                  notes: "Taylor now named-function at courier-tier as an active conduit; anonymous no longer possible; cl02 full gain delivered here. Consolidated from +0.5 s01 + +0.5 s03 split into single +1.0 bone at s01 at /and-write Phase 1 redo 2026-05-27 to honor bone-level magnitude floor of 1.0."
              axes_held:
                - axis: moral_framework
                  rationale: "licensed exception active and held; rationalization runs (Sera is real, the intelligence is already running, the destination is the modification); framework still named and believed — not interrogated as compromised; no Δ on this axis at this scene (chapter contract holds moral_framework; the licensed exception is the discipline at work, not its breach)"
                - axis: relational_anchor_status
                  rationale: "Wren is not in this scene's calculus; the acceptance is about Sera; anchor holds outside pricing at rank 2"
                - axis: political_register-prot
                  rationale: "courier-tier exchange in a cooper's yard; no court-register observation surface present at this venue; resentment has no court-material to form on at this scene"
                - axis: capability
                  rationale: "acceptance is operational, not deployment; no new coverage range extends here"
              density_target: 0.6-0.7
            scene_conflict:
              protagonist_force: "Taylor delivering the acceptance on modified terms — volume and interval are hers to determine; this is the discipline's last available parameter to hold"
              opposing_force: "the acceptance's irreversibility — Jarvis receives it as a routing confirmation; the lever has solidified before Taylor finishes speaking; modification-of-terms does not modify the fact of the yes"
              stakes_axis: social_tether-antag
            stale_since: null

          - slug: b01c04s02
            chunk: |
              The first ward beyond the Hook is Pig Tallow Lane and its associated courts — [image: three connecting alleys that feed into a waste-middens junction, the air carrying the particular weight of a ward that processes what other wards discard]. Taylor walks it in the late morning, [force: Taylor's systematic ward-reading — the same walk-and-read discipline she applied to the Hook's triage, applied now to new ground]. She is not treating anyone. She is not intervening. She is expanding the map.

              [event: Taylor extends insect coverage into the first adjacent ward] — the feed opens across Pig Tallow Lane and its courts within an hour of walking, the familiar architecture of what-is-happening-at-every-junction, who is agitated, which passage is being avoided and why. It is the same information the Hook gave her. Different ward, same ledger. [mechanism: capability expansion as rote procedure — the intelligence-harvest is already the form her days take; expansion is addition, not transformation]. She reads the ward the way she reads the Hook. She does not stop to name what she is doing.

              Oswyn Mudway is in the middens court at midday — [event: Taylor observes Oswyn Mudway through the feed, unknowing and uncontacted] — [image: Oswyn at the cart, the elder doing penny-a-barrel labor for a carter — net-weights work set aside for a day's coin in an adjacent ward, the kind of cross-ward labor that ward-elders pick up when the household ledger thins]. He does not know she is watching. He does not know he is now a coordinate in a map that routes upward through a courier to a man in a tower. [force: Oswyn's unknowing-node status — the ward's resident who becomes coverage substrate without consent, without contact, without choice]. Taylor notes his presence, notes his location-pattern, notes the two adults he runs with. She continues the walk.

              Wren is three streets over in the second ward by late afternoon — [event: Taylor extends coverage into the second adjacent ward before dusk]; the feed picks up the stitch-house without effort, the same sewing-machine hum of bodies in close work, Wren's particular stillness at the frame distinguishable from the two apprentices moving around her. [image: Wren visible in the feed-texture, unremarkable, the anchor that has no line attached to it yet from this operation's accounting]. Taylor does not walk that street. She does not note Wren's location for the Jarvis report. The distinction between what enters the ledger and what does not is one Taylor holds without examining why she holds it.
            substance_delta:
              axes_in_motion:
                - axis: capability
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl03a
                  notes: "two of three adjacent wards brought into coverage range; Oswyn as active node; the expansion is procedural — same method as Hook triage; cl03a first tranche"
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl03b
                  notes: "network-build tether gain begins materializing; Oswyn as unknowing node is the first substrate of the expanded coverage; Wren visible but not in the report — tether asymmetry plants here; cl03b first tranche; future-cost collateral forming without Taylor's accounting recognizing it"
              axes_held:
                - axis: moral_legibility_to_self
                  rationale: "Taylor frames expansion as harm-reduction continuation — she is reading the ward as she reads the Hook; the triage logic extends; recognition that the architecture now routes upward to a patron is present but framed as destination-modification, not transformation; legibility crack suppressed"
                - axis: moral_framework
                  rationale: "framework held as still named and believed; the distinction between what enters the Jarvis ledger and what does not (Wren) is maintained without examination — operative in its specific form; no Δ on this axis at this scene (the un-examined distinction IS the discipline, not its violation)"
                - axis: relational_anchor_status
                  rationale: "Wren visible in feed, not in the report; anchor held outside pricing; the act of not-noting Wren is the anchor discipline at work — but it is not interrogated this scene"
                - axis: political_register-prot
                  rationale: "ward-level walk; coverage substrate is foot-traffic, sickness-clustering, alley-agitation; no court-tier observation material yet present in the expanded feed"
              density_target: 0.65-0.75
            scene_conflict:
              protagonist_force: "Taylor's systematic ward-reading as harm-reduction extension — the same discipline she applied to the Hook's triage, now enlarging the map with the same procedural register; the expansion feels continuous with what she has always done"
              opposing_force: "the expansion's upward routing — the same walk-and-read that constituted the Hook's triage now constitutes intelligence for Otto's consolidation; Oswyn becomes a coordinate in a patron-chain without any operational difference in the act Taylor performs"
              stakes_axis: social_tether-prot-rise
            stale_since: null

          - slug: b01c04s03
            chunk: |
              The third ward falls on the second day — [event: Taylor completes the four-ward coverage map] — Roper's Court and its tributary lanes, which she walks in the grey of early morning when foot traffic is thin and the feed's geometry is cleanest. [image: the four-ward coverage map as a completed shape in Taylor's awareness, the Hook and its three adjacent wards forming an irregular quadrant whose boundaries are set by the range the insects hold reliably in rain-damp stone]. It is the largest operational footprint she has run in King's Landing. The accounting holds it as: larger. No register beyond that.

              Jarvis is at the yard at the first-bell appointment [event: Jarvis returns with Otto's first confirmation — Sera's exposure is being managed]. He has, for the first time, a note — not a letter, not a seal, a single line in a plain hand that reads like administrative confirmation: the matter they discussed has been attended to, the three-month window is no longer open. He does not hand it to her. He reads it once, holds it visible at the distance of conversation, returns it to his coat. [force: the confirmation arriving as precisely the weight the acceptance was made to carry — Sera is managed; the lever has paid its stated first dividend]. Taylor registers it. The accounting closes one column and opens another.

              [event: Taylor delivers the first movement-pattern report to Jarvis — a single sheet folded twice in plain hand, the kind of object that does not draw a second look, passed across the half-step of yard-air between them; Jarvis takes it without opening it and slides it inside his coat]. [image: the report's physical smallness — one sheet, a fold, a coat pocket — against the size of the architecture it represents]. The report's content: not everything the feed holds, not the Hook's medical triage layer, not Wren's location, not Oswyn by name — the junction-agitation patterns across the four wards for the past six days, the clustering that precedes crowd-trouble, the three passage-avoidance points that mark which routes the ward-residents read as unsafe. [mechanism: the first upward-routing of the intelligence layer — the information exits Taylor's operational context and enters Otto Hightower's Green consolidation channel through Jarvis as structural vector]. It is, Taylor notes, what she has already been reading. She has named a destination. [force: the distinction between reading and reporting dissolving in the act of handing the sheet across].

              [image: Jarvis receiving the report with the same courier's neutrality he brought to the acceptance — no reaction that would name its value to him or to the man above him]. [event: position-world increment — the Green faction gains its first KL street-layer intelligence through this channel]. [event: social_tether-prot-rise load-bearing formation confirmed — Jarvis as structural vector is now a functional architecture, not a potential one]. Taylor walks back through the Hook in the late grey, the feed running across the four wards simultaneously, reading the ward and feeding the ward and reading what she feeds in a single unbroken operation. [mechanism: reading-the-ward and routing-what-is-read collapse into one continuous operational form — the day's labor does not partition into the part that helps and the part that pays; the architecture runs whole or it does not run]. Wren is at the stitch-house. Taylor's feed touches the stitch-house and passes through. The report did not include Wren. This is the anchor holding. Taylor does not examine whether it will hold.
            substance_delta:
              axes_in_motion:
                - axis: capability
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl03a
                  notes: "four-ward coverage complete; cl03a fully settled; the footprint is the largest Taylor has run in KL; completion tranche. Raised from +0.5 to +1.0 at /and-write Phase 1 redo 2026-05-27 to honor bone-level magnitude floor of 1.0."
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl03b
                  notes: "Jarvis as structural vector is now functional architecture; first upward-routing completed; tether load-bearing in formation; cl03b completes — Wren explicitly outside the report is the future-cost collateral marker; the audience sees the gap the calculus does not"
                - axis: position-world
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl-world-d04
                  notes: "first intelligence delivery upward — Green consolidation gains KL street-layer intel through Jarvis channel; first tranche of cl-world-d04 (+1.0 of +2 ledger gain; the second +1.0 tranche lands at d07 arrangement-formalized per series substance notes); this is the world-axis increment c04 owes"
              axes_held:
                - axis: moral_framework
                  rationale: "rationalization stable at chapter close: Taylor frames the report as naming-a-destination-for-what-she-already-knows; licensed exception is operative and believed; framework still named and believed — legibility not interrogated; no Δ on this axis (chapter-level contract holds moral_framework; the rationalization is the discipline, not its breach)"
                - axis: relational_anchor_status
                  rationale: "Wren outside the report explicitly; anchor discipline named on-page — 'the report did not include Wren'; held outside pricing; the act of not-including is the anchor; but the question of whether it will hold is planted without answer"
                - axis: political_register-prot
                  rationale: "the report Taylor hands to Jarvis is junction-agitation and ward-pattern from Flea Bottom-tier sources; no court-tier surface in the feed yet; resentment has no court-material to form on at this feed-tier"
                - axis: moral_legibility_to_self
                  rationale: "recognition deferred; the 'protection and trap are the same operation' thesis is made structurally visible to the audience in Taylor's continuous feed-and-report loop but Taylor does not name it; legibility suppressed at chapter close per chapter_class: standard"
                - axis: position-prot-rise
                  rationale: "full +1.0 consolidated to s01 bone at /and-write Phase 1 redo 2026-05-27; cl02 gain completed at acceptance; Sera confirmation (s03) confirms the arrangement is functional but does not re-advance the position axis — the naming-event was at s01"
              density_target: 0.7-0.8
            scene_conflict:
              protagonist_force: "the confirmation arriving as the lever's first dividend — Sera is managed; the acceptance has paid; Taylor's accounting closes the column that justified the decision"
              opposing_force: "the first report's upward routing — the information exits Taylor's operational context and enters Otto's consolidation channel; the distinction between reading and reporting dissolves in the act of handing it across; the architecture is now running, not planned"
              stakes_axis: social_tether-prot-rise
            stale_since: null

      - slug: b01c05
        status: stitched   # /and-stitch b01-c05 SHIPPED-WITH-CAVEATS (DEC-0044, 2026-05-28) after FAIL #3 → principal accepted; draft/b01-c05.md terminal. Was bones-written from /and-write b01-c05 revise --from-signals; re-cascaded /and-facets (audited-r1) + /and-stitch (Phase 9 third-cycle).
        bones_file: theater/bones/b01-c05.md
        bones_count: 35  # was 31; revise --from-signals added 4 bones (A1, B1, B2, C1; B3 dropped at Phase 5 continuity)
        substance_bone_gate_verdict: PASS  # re-stamped at revise Phase 6: 9/9 SUBSTANCE-FELT + auditor PASS
        bones_review:
          reviewed_at: 2026-05-28T00:00:00Z   # re-stamped post-revise; original review at active-project/staff/reviews/bones-b01c05-2026-05-28.md superseded
          report_path: active-project/staff/reviews/bones-b01c05-2026-05-28-revise.md
          verdict: PASS-WITH-NOTES
          follow_check: PASS-WITH-NOTES  # PROP-0020 exploration rerun 2026-05-29: bones followable as-is; opacity (Rushwick-resists-flat-read) context-addable, deferred to Phase 2.5; report active-project/staff/reviews/bones-followcheck-b01c05-rerun.md; NOT a FOLLOW-FAIL (did not block /and-facets)
          bones_file_mtime_at_review: 1780028088  # post-recast mtime; lean re-review verdict PASS (12 PASS / 1 FLAG / 0 HARD); facets remain fresh (no flat_id changes; no facet citations at @13)
          stale_since: null  # cleared at lean /and-review bones re-review 2026-05-28 (post-@13-recast PASS)
          # Re-review (post revise --from-signals): 18 findings (15 PASS, 3 FLAG, 0 HARD).
          # All 5 cold-read confusions RESOLVED at bone level; Sera-identity PARTIAL by architectural design (facet-dependent).
          # FLAGs carried forward:
          #   - finding-009: Sera-identity PARTIAL — routed to /and-facets via pl-2026-05-28-002
          #   - finding-010: dup-001 @32+@34 SVO dup — advisory to /and-stitch (distinguishable prose for two foreclosure attempts)
          #   - finding-011: flag-002 @25 "resolves" intransitive — advisory to /and-stitch
          #   - finding-018: /and-facets cite-responsibilities must re-anchor against new flat_ids 1-35 (facets_stale_since already set)
          # Verdict: no HARDs; 2 FLAGs carried from Phase 6 (s03n10+n12 SVO duplicate; s03n03 "resolves" intransitive); 3 notes for /and-facets:
          #   note-001: courier's post-enforcement walk image — narrator-interest/sensory facet must cite @23-@25 (s03n07 removed at Phase 6 fault-003; image is load-bearing for resentment-accumulation read)
          #   note-002: cf-d10 face-content — memory or narrator-interest facet must associate face with body-record @27 (otherwise d10 callback loses face-recognition anchor)
          #   note-003: 3 cite-responsibilities forward to /and-facets — narrator-interest @5 (provisioner gait-class, replacing removed s01n06) + @7 (message-runner gait-class, replacing removed s01n09); sensory @13 carrying "effortful" qualifier stripped from bone SVO
          # Cold-read prediction: HIGH/MEDIUM/HIGH (no LOW); MEDIUM on "color arrives before Taylor names it" is facet-layer-dependent by architectural design
          # Probe verdicts: gap-instrument @13/@14 PASS (gap not hollowed by stripping "effortful"); recognition-cessation @25 PROPERLY ANCHORED; foreclosure quartet @28-@31 reads as FORECLOSURE; cf-d10 plant SUFFICIENT at figure level (face is facet responsibility)
        # PROP-0020 context-weave track — EXPLORATION RERUN 2026-05-29 (c05 already shipped; non-staling; exercises the new checkpoints retroactively).
        context_followability:
          verdict: FOLLOWABLE
          report_path: active-project/staff/reviews/context-follow-r2-b01c05-rerun.md
          reviewed_at: 2026-05-29T00:00:00Z
          ledger_path: active-project/staff/showrunner/context-ledger-b01-c05.md
          ledger_open_count: 0   # ctx-001 satisfied by exposition:5 @19 (R2 ledger-licensed add)
          phase_2_5: "1 CONTEXT-REQUIRED (ctx-001 @19 Jarvis->Otto channel identity) + 3 WEAVE-FIXABLE"
          phase_4_5: "FOLLOWABLE; ctx-001 closed; no Phase 4.6 fired; 1 minor non-blocking residual (faction proper-noun seam)"
          unresolved: []   # no WARN; conditional R3 not triggered
        substance_delta_measured:
          axes_moved:
            political_register-prot: +1.5    # @29 in revise emit (was @25 pre-revise); EXACT vs target +1.5; cl-d05 first tranche; C1 chatter at @28 is substrate not movement
          density_measured: 0.55-0.65         # 35 bones / 3 scenes post-revise; s02 expanded 12→15 (3 new bones); s03 expanded 12→13 (1 new bone)
          felt_verdict: SUBSTANCE-FELT-3-of-3 # all 3 audience personas, all 9 cells (3 scenes × 3 personas) — both pre-revise Phase 6 and post-revise Phase 6
        # /and-write b01c05 emit 2026-05-28 — clean run (no Phase 1 redo; no DEC adjudications).
        # Phase 1 scene-decomposition: 34 bones (s01: 9, s02: 12, s03: 13); event_map[] mechanical chunk-tag extraction + author-noticed entries; sensory-grounding ≥1 per scene; worm-canon SOFT-WATCH courier 3-distinct-bones honored (s02n02 gait, s02n04 approach, s02n08 filing); dark-fantasy gap-instrument pair authored (s02n06 + s02n07).
        # Phase 1.5 dialogue: SKIPPED (no speech-form or communication-axis bones — chapter is interior/observational).
        # Phase 2 SVO constraint audit: cycle 0 FINDINGS-PRESENT (2 HARD: 5 feed-perception bones + 4 abstract-affect-object bones; 4 SIGNAL; 3 FLAG) → cycle 1 fixer recasts 10 bones → cycle 2 audit FINDINGS-PRESENT (1 HARD: fault-003 PP-modifier on s03n11/n13 "holds at X") → cycle 2 fixer inverts SVOs → cycle 3 audit ACCEPT.
        # Phase 3 dramatist: ACCEPT — order preserved in all 3 scenes; recognition (s03n06) correctly between failed first pass and re-run sequence; gap-instrument pair at @13-@14. 2 non-blocking advisories (s02n02→n03 timing, s03n08→n09 seam).
        # Phase 4 trim: 3-of-3 ACCEPT in one round, 34/0 across cape-fic-reader, dark-fantasy-reader, worm-canon-pedant. No DELETEs proposed.
        # Phase 5 continuity audit: FINDINGS-PRESENT (1 HARD sr-001: Taylor state file frozen at series-open values; 1 FLAG dup-001 s03n10+n12 identical SVO advisory) → state file reconciled (full c01-c05 handoff_out values) → re-audit CONTINUITY-OK.
        # Phase 6 substance bone-gate cycle 0: 8 HARD + 1 SIGNAL + 2 FLAG (auditor); 9-of-9 SUBSTANCE-FELT (audience).
        #   HARDs: fault-001 (6× "Taylor maps X" perception-class), fault-002 (3 modifier strips), fault-003 (s03n07 interiority+PP), fault-004 (s02 capability witness missing), fault-005 (s03 social_tether witness missing).
        #   Cycle 1 fixer: 3 bone removals (s01n06/n09, s03n07; cognitive content migrates to /and-facets narrator-interest layer), 4 recasts (s02n02 holds wall-line, s02n08 files enforcement-record, s02n11 adds courier to body-map, s03n09 files courier body-record), 3 modifier strips (s02n03/n05/n06), 2 axes_held additions (s02n01 capability, s03n01 social_tether-prot-rise).
        #   Cycle 2 re-audit: ACCEPT — all 8 HARDs resolved; signal-001 (maps mannerism) dissolved by entailment; 2 FLAGs carry forward non-blocking.
        # Phase 6.5 admin process-critic: SKIPPED — final verdict fully clean (0 HARDs, 0 accepted-not-remediated SIGNALs).
        # Phase 7 emit: theater/bones/b01-c05.md (31 bones; 7+12+12 across s01/s02/s03) + theater/facets/scene-map-b01-c05.md.
        # Bones file slug gaps: s01 missing n06 + n09; s03 missing n07 (per Phase 6 fault-001/003 removals — slugs non-monotonic, flat_ids contiguous 1-31).
        # Soft watches forward (carried to next phases):
        #   /and-facets: narrator-interest must cite removed-bone replacement bones (s01n05 for provisioner gait-class content, s01n07 for message-runner gait-class, s02n12 + s03n09 for courier-walk content); sensory facet must cite s02n13 (alley-sound) carrying the "effortful" qualifier stripped from bone SVO; dialogue facet — no dialogue this chapter.
        #   margit: author oc-rushwick.card.md (location not yet in warehouse; surfaced as parking-lot SOFT for /and-facets dispatch).
        #   /and-review bones: independent fidelity review (MANDATORY gate before /and-facets per URI-WRITE-BONES-REVIEW-GATE).
        # FLAGs carrying to /and-stitch advisory:
        #   - dup-001: s03n10 + s03n12 identical SVO "taylor-hebert-kl-122ac runs the rushwick flat-read" (load-bearing for foreclosure pattern; stitcher prose must distinguish the two attempts).
        #   - flag-002: s03n03 "the Hook-feed resolves" intransitive "resolves" borderline; advisory.
        # Draft archived: active-project/staff/showrunner/_drafts/b01c05-bones-draft-2026-05-28.md
        # Auditor reports: write-b01c05-pass2.md (Phase 2; 3 attempts), write-b01c05-pass5.md (Phase 5; 2 attempts), write-b01c05-bone-gate.md (Phase 6; 2 attempts).
        # Audience reviewer STM (Phase 4 trim + Phase 6 bone-gate) under "## b01c05 ..." headings.
        #
        # ============================================================
        # /and-write b01-c05 Phase 1 targeted recast 2026-05-29 (DEC-0042)
        # ============================================================
        # Trigger: /and-stitch Phase 9 cold-read FAIL #2 — cold-reader inferred possible sexual assault
        #   from "the three figures pin the courier" + "the side-alley returns the sound" at @13-@14.
        # Scope: @13 ONLY recast in b01c05s02. All other bones unchanged. No flat_id renumbering.
        # Change: @13 "the three figures pin the courier" → "the three figures strike the courier"
        # Rationale: "strike" is the concrete force-application verb that unambiguously specifies
        #   ENFORCEMENT-BEATING violence type per chunk authority ("enforcement, not robbery";
        #   "controlled containment"; "coordinated"). The "pin" beat's containment function is
        #   already established by @11-@12 (enter side-alley + close alley-mouth) + oc-rushwick
        #   enforcement-geometry section; @13 can advance to force-application without structural loss.
        # Option A (recast) chosen over Option B (add bone): Option B would renumber @14-@35 and
        #   blow up all existing facet citations.
        # Per-bone classification for recast @13:
        #   svo: "the three figures strike the courier"
        #   classification: HELD
        #   axes_held: [{axis: moral_framework, rationale: "enforcement violence is the s02 opposing_force
        #     enacted as a specific physical act — the strike is the faction-violence content the discipline
        #     absorbs as enforcement-not-robbery; inside the licensed exception; moral_framework held at
        #     current crack-level"}]
        #   axes_in_motion: []
        #   cost_ledger_anchor: null
        # Scene-map @13 peak-shadow annotation updated: "three figures strike courier — force-application beat"
        # Files changed: theater/bones/b01-c05.md (@13 verb), theater/facets/scene-map-b01-c05.md (@13 annotation)
        # Soft seam flagged to /and-facets: "held against stone" texture (previously entailed by @13 "pin")
        #   now only available via @11-@12 geometry + chunk text + oc-rushwick card; sensory/NI facet
        #   should carry "held against stone" physical texture at @13-@14 citation.
        # Facets NOT stale: no flat_id changes; existing citations remain valid.
        # Bones review NOT stale: this is a scope-contained verb swap; no structural change to event coverage.
        # ============================================================
        # /and-write b01-c05 REVISE --from-signals emit 2026-05-28 (post-FAIL cold-read)
        # ============================================================
        # Trigger: /and-stitch b01-c05 Phase 9 cold-read FAIL (this same date).
        # Admin DEC-0040: option (b) targeted bones-add at 3 sites (s01 anchor reinterpreted as s02-courier-intro per chunk discipline).
        # Phase 1: screen-writer authored 5 candidate new bones (A1, B1, B2, B3, C1).
        # Phase 2 SVO audit: ACCEPT WITH FLAG (B3 'adds X to Y' PP-tail; precedent @18 same form; no action).
        # Phase 3 dramatist: ACCEPT all 5 insertions; 1 non-blocking advisory routed to /and-facets narrator-interest.
        # Phase 4 trim: 3-of-3 ACCEPT (cape-fic + dark-fantasy + worm-canon-pedant). 2 worm-canon SVO refinements applied:
        #   - A1: "returns the courier-entry" → "returns the courier" (feed surfaces bodies, not records)
        #   - C1: "resists the flat-read" → "holds the color" (mirrors @29/@31 'holds' idiom; matches chunk vocabulary)
        # Phase 5 continuity: FINDINGS-PRESENT (3 faults all on Site B):
        #   - fault-001 FAULT-REFERENCE: "the jarvis-channel" not established
        #   - fault-002 FAULT-REFERENCE: "the jarvis-form" + "the sera-arrangement-file" not established
        #   - fault-003 FAULT-STATE: B2/B3 verb 'enters' implies real-time transmission; c04 model + s02 chunk = drafts during, transmits later
        #   Resolution: B2 amended "the enforcement-report enters the jarvis-channel" → "taylor-hebert-kl-122ac drafts the jarvis-report"; B3 DROPPED entirely. Sera-link migrated to facet layer.
        # Phase 5 re-audit: CONTINUITY-OK.
        # Phase 6 bone-gate (integrated 35-bone scaffold):
        #   - Auditor: PASS (0 HARD; 1 non-blocking advisory on chatter-count data limit).
        #   - cape-fic-reader: 3-of-3 SUBSTANCE-FELT.
        #   - dark-fantasy-reader: 3-of-3 SUBSTANCE-FELT. ESCALATED soft carry: Sera-architecture delivery now MANDATORY at /and-facets (B3 drop made the protect-target connection bone-invisible).
        #   - worm-canon-pedant: 3-of-3 SUBSTANCE-FELT; canonicity all clean; SOFT-WATCH gait/approach/filing structurally distinct CONFIRMED HONORED.
        # Phase 6.5 admin process-critic: SKIPPED (final verdict fully clean — 0 HARDs, 0 accepted-not-remediated SIGNALs).
        # Phase 7 emit (revise): full re-numbering 1-35 in scene-order; flat_ids shift from pre-revise 1-31.
        #   - s01: 1-7 (unchanged)
        #   - s02: 8-22 (was 8-19); new bones at flat_ids 9 (A1 insect-feed returns courier), 15 (B1 courier raises spine), 19 (B2 drafts jarvis-report)
        #   - s03: 23-35 (was 20-31); new bone at flat_id 28 (C1 rushwick-feed holds color), recognition stop now at @29 (was @25)
        #   - DOWNSTREAM FLAT-ID MAPPING (old → new): @8→@8, @9→@10, @13→@14, @14→@16, @15→@17, @16→@18, @17→@20, @18→@21, @19→@22, @20→@23, @21→@24, @22→@25, @23→@26, @24→@27, @25→@29, @26→@30, @27→@31, @28→@32, @29→@33, @30→@34, @31→@35.
        # Bones file: theater/bones/b01-c05.md (35 bones; 7+15+13 across s01/s02/s03).
        # Scene-map facet re-emitted: theater/facets/scene-map-b01-c05.md.
        # Per-bone substance_delta on the 4 new bones (held in showrunner memory only; comment-clean in bones file):
        #   - A1 @9: axis_moves: [] + cost_ledger_anchor: cl-d05 (chatter substrate; courier-identification feeds s03 foreclosure)
        #   - B1 @15: axes_held: [{axis: moral_framework, rationale: "courier body-recovery is observable incident continuation; licensed-exception unaffected"}]
        #   - B2 @19: axes_held: [{axis: moral_framework, rationale: "drafting Jarvis-report is inside licensed exception; routing-name honored without interrogation"}]
        #   - C1 @28: axis_moves: [] + cost_ledger_anchor: cl-d05 (chatter substrate; the held color IS the cl-d05 mechanism opening political_register-prot at @29)
        # Soft watches forward (carried to next phases — REVISE-specific additions):
        #   /and-review bones (MANDATORY): re-verify chunk→bones fidelity on 35-bone scaffold; bones_review stale_since set; gate /and-facets HARD-aborts until fresh review.
        #   /and-facets (re-run): ESCALATED — Sera-architecture (Sera identity + protective-arrangement + Otto-routing destination) must land at memory + narrator-interest + exposition facets. B3 drop made the connection bone-invisible; without facet-layer delivery, political_register-prot +1.5 at @29 lands as resentment-of-enforcement, not the chapter's specific irony. Per dark-fantasy-reader Phase 6: "this is not optional at the facet layer."
        #   /and-facets (re-run): old citation @N references in prior facet entries are stale — full re-anchoring required against new flat_ids 1-35.
        #   /and-stitch (re-run after facets): C1 @28 "holds the color" MUST precede @29 "stops the rushwick-pass" in render — apparatus-holds → protagonist-responds causal direction is the difference between world-physics-response and interior-mood-shift (dark-fantasy + worm-canon both flagged).
        #   /and-stitch (re-run): cold-read confusions (i)(ii)(iii)(iv)(v) all addressed in bones; cold-read re-test should land.
        # Draft archived: active-project/staff/showrunner/_drafts/b01c05-revise-fromsignals-2026-05-28.md (full Phase 1-7 trace).
        # Auditor reports: write-b01c05-pass2-revise.md (Phase 2; 1 cycle), write-b01c05-pass5-revise.md (Phase 5; 2 cycles per amendment), write-b01c05-bone-gate-revise.md (Phase 6; 1 cycle).
        # Audience reviewer STM under "## b01c05 revise --from-signals — Phase 4 trim" and "## b01c05 revise --from-signals — Phase 6 bone-gate" headings.
        # ============================================================
        facets_path: active-project/theater/facets/
        round_1_complete: true
        round_2_complete: true
        facets_status: audited-r1   # cleared via /and-facets b01-c05 re-run 2026-05-28 (post-revise --from-signals)
        facets_stale_since: null  # cleared at /and-facets re-run Phase 6 persist 2026-05-28
        audit_path: active-project/staff/auditor/facets-final-audit.md
        audit_complete: true
        audit_findings: "0 HARD / 6 SIGNAL final (cycle 3 CLEAN) — cycle 1: 2 HARD + 6 SIGNAL → fault-001 + fault-002 remediated; cycle 2: 1 new HARD (fault-c2-001 proto-lines sync gap) → remediated; cycle 3 CLEAN"
        audience_gate_path: active-project/staff/auditor/facets-audience-gate-r2.md
        audience_gate_complete: true
        audience_gate_cycles: 2
        audience_gate_cap_burned: false
        bidirectional_loop: validated   # multiple shared findings across audience + auditor (vibes fault-002 / sensory:2 cross-card mismatch)
        # /and-facets b01-c05 RE-EMIT 2026-05-28 (post /and-write revise --from-signals).
        # ============================================================
        # Phase 0: anchor-refresh HARD-ABORT gate fired (bones re-emitted with new flat_ids 1-35; all prior facets stale). 14 facet files + cite-index + prior audit reports archived to theater/_archive/2026-05-28T195041Z-c05-revise-stale-facets/. margit authored oc-rushwick.card.md (resolving pl-2026-05-28-001 SOFT).
        # Phase 1 R1 fanout: 10 authors landed; 59 facet entries (loc-state=9, NI=8, sensory=2, state-env=7, state-taylor=5, mem=2, feel=2, metaphor=0, vibes=20, exposition=4). Sera-architecture pl-2026-05-28-002 HARD delivery claimed at 3 layers (mem:1 @19, NI carriers @5/@19/@29, exposition:2 @0).
        # Phase 2 cite-index: clean merge; 2 body-integrity fixes (feeling-taylor @29 trailing comment stripped; exposition @0 synthetic anchor removed from inflight).
        # Phase 3 R2 fanout: 5 judges. K/D/A: NI 8/0/2 (narrator:9 @31 + narrator:10 @35 adds); memory 2/0/0; feeling-taylor 1/1/0 (feel:1 @19 deleted on card-tell mismatch; feel:2 @29 renumbered to feel:1); metaphor 0/0/0 (refuse upheld); exposition 4/0/0/0. 10 cap-refusals total. Convergent fix: NI's narrator:9 @31 ADD closed memory's flagged @31 NI-spine gap.
        # Phase 4 fanin: .r2-decisions.md consolidated (f-r2-counts {0,0,0,0}; 0 discipline-fails; 0 arbiter interventions). Cite-index rebuilt clean. Scene-map validated (7+15+13=35 covers 1-35 exactly).
        # Phase 5 audit cycle 1: 2 HARD (fault-001 state-updates ID series; fault-002 vibes stale feeling citations) + 6 SIGNAL (all defended).
        # Phase 5 fixer pass cycle 1: vibes:10 feeling:1 → world-build:cond-road-to-hell-chain-shape; vibes:14/15/16 feeling:2 → feeling:1; state-updates slice headers added.
        # Phase 5 re-audit cycle 1: CLEAN (both HARDs RESOLVED).
        # Phase 5b cycle 1: cape-fic 8/8 ACCEPT; worm-canon 8/8 ACCEPT (Earth-Bet fence CLEAN); dark-fantasy 7/8 ACCEPT (vibes REVISE on STALE-READ of fault-002 already-resolved); sensory specialists 1 ACCEPT + 2 REVISE (sensory:2 @13 fauna-feed-extension + unanchored-old-state).
        # Phase 5b cycle 2 fixer pass: sensory:2 re-anchored @13 → @14 (R1 SEAM-005 path); loc-state:5 @11 acoustic-baseline note added; sensory:2 inline ID citation fixed.
        # Phase 5b cycle 2 re-fires: sensory-disambiguation-pedant ACCEPT; sensory-old-state-reader ACCEPT; dark-fantasy vibes ACCEPT (stale-read corrected; remediation verified directly).
        # Phase 5 audit cycle 2: 1 new HARD fault-c2-001 (proto-lines [sensory:2] token still at @13; facet anchor @14; back=N).
        # Phase 5 fixer cycle 2: restored canonical proto-lines from bones; re-ran cite-index merge; [sensory:2] now at @14.
        # Phase 5 re-audit cycle 3: CLEAN (fault-c2-001 RESOLVED; no new findings).
        # Phase 5b cycle 2 FINAL aggregate: all 9 facets 3/3 ACCEPT.
        # Phase 5c admin process-critic: SKIPPED (final cycle clean ACCEPT 3-of-3 across all facets; no cap-burns).
        # Sera-architecture pl-2026-05-28-002 HARD: RESOLVED (3 reviewers concurring deliveries at exposition:2 + mem:1 + NI carriers).
        # Final facet entry count: 58 (loc-state=9, NI=10, sensory=2, state=12 consolidated, mem=2, feel=1, metaphor=0, vibes=20, exposition=4). 22/35 proto-lines decorated.
        # Peak pile-ups: @29 (7 facets — narrator:8 feel:1 state:3 state:4 vibes:15 vibes:16 vibes:17); @31 (4 facets — mem:2 narrator:9 state:5 state:7); @21 (5 — narrator:6 state:1 state:4 vibes:11 vibes:12); @14 (5 — narrator:4 sensory:2 vibes:6 vibes:7 vibes:8). All warranted per Phase 5 PILE-UP REVIEW.
        # Soft watches forward to /and-stitch:
        #   - vibes:9 @17 "atonement-as-repetition" keyword label may bias stitcher toward naming chapter's structural irony at filing-triad bone (force-block discipline says Taylor doesn't name it); Phase 8 watch.
        #   - C1 @28 "holds the color" MUST precede @29 "stops the rushwick-pass" in render sequence (apparatus-holds → protagonist-responds causal direction; reorder breaks world-physics-first read).
        #   - dup-001: s03 @32+@34 identical SVO "taylor-hebert-kl-122ac runs the rushwick flat-read"; stitcher must distinguish two foreclosure attempts.
        #   - flag-002 @25 "the Hook-feed resolves" intransitive borderline; stitcher prose-handling.
        #   - NI density 28.6% at zero-dialogue-chapter structural-overshoot precedent; /and-stitch may evaluate band recalibration.
        #   - "discipline" word-saturation NI 4/10 (40% borderline SATURATION); reword candidate at narrator:3 @10 if /and-stitch finds register reads tic-y.
        audit_path: active-project/staff/auditor/facets-final-audit.md
        audit_complete: true
        audit_findings: 0 HARD / 4 SIGNAL / 10 FLAG (cycle 1) → 0 HARD / 2 SIGNAL / 10 FLAG (cycle 2; fault-028 + fault-033 resolved)
        audience_gate_path: active-project/staff/auditor/facets-audience-gate-r2.md
        audience_gate_complete: true
        audience_gate_cycles: 2
        audience_gate_cap_burned: false
        bidirectional_loop: validated   # 3 shared findings across auditor + audience paths (vibes:12-15 license, NI density, memory carve-out)
        # /and-facets b01-c05 emit 2026-05-28 — 2-cycle audience-gate to clean ACCEPT.
        # R1 fanout: 10 authors landed; 60 facet entries (loc-state=9, NI=8 post-c2, sensory=3 post-c2, state-env=7, state-taylor=8, memory=2 post-c2, feeling=2 post-c2, metaphor=0, vibes=18, exposition=3).
        # R2 fanout: 5 judges (NI K=7 D=0 A=3; memory K=1 D=2 A=1; feeling K=1 A=1; metaphor K=0 D=0 A=0; exposition K=2 R=1 A=0). Dialogue R2 SKIPPED (no speech bones).
        # Phase 5 audit cycle 1: FINDINGS-PRESENT (0 HARD; 4 SIGNAL: NI density 32.3%; metaphor inventory; memory carve-out doc; vibes:12-15 license; 10 FLAG advisory).
        # Phase 5b cycle 1 (3 personas × all 9 facets batched): 4/9 ACCEPT, 5 FAIL (NI, sensory, memory, feeling, vibes).
        # Cycle 2 fixer: vibes lic-out feeling:2 → state:13 co-anchor; DELETE narrator:2@7 + narrator:5@24 (density 25.8%); memory carve-out preamble; sensory:3@14 ADD (URI-FACETS-CYCLE-N-ADD pre-validation PASS).
        # Phase 5 cycle 2 re-audit: CLEAN (0 new HARDs; fault-028 + fault-033 RESOLVED).
        # Phase 5b cycle 2 re-fire (failing facets only): 9/9 ACCEPT strict 3-of-3.
        # Phase 5c admin process-critic: SKIPPED (final cycle clean ACCEPT; no cap-burns).
        # Final facet entry count: 60 (loc-state=9, NI=8, sensory=3, state=15, memory=2, feeling=2, metaphor=0, vibes=18, exposition=3).
        # 26/31 proto-lines decorated (83.9%). Peak @25 = 6 facets; @18 = 5; @27 = 5; @13 = 5.
        # Bare bones: @14 (post-c2 fix), @19, @23, @28, @30 — wait @14 now decorated by sensory:3; final bare = @19, @22 (no — @22 has narrator:9), let me recount: @19, @23, @28, @30. 4 bare.
        # Soft watches forward to /and-stitch:
        #   - vibes:12-15 @25 register: 6-facet pile-up at peak — stitcher to confirm density warranted (auditor verified warranted)
        #   - foreclosure-quartet asymmetry: feel:2 @29 alone between bare @28+@30; @31 has narrator:10 + vibes:17+18; stitch must respect bare flanks
        #   - NI density 25.8% at ceiling — differentiated rhythm in scene-A (3 NI in 7 bones)
        #   - cf-d10 plant @8 + @18 + @27 callback-ready for d10 callback
        stitched: true  # re-stitched 2026-05-28 post /and-write revise (@13 recast); prior FAIL #2 stitch archived to draft/_archive/2026-05-28-c05-fail-2/
        stitched_at: 2026-05-28T00:00:00Z  # re-stamped at Phase 8 finalize 2026-05-28 (re-stitch #3)
        draft_file: active-project/draft/b01-c05.md  # 1575 words (preamble ~190 + body 1385)
        draft_stale_since: null  # cleared at Phase 8 finalize 2026-05-28 (re-stitch #3 post @13 strike recast)
        # FACETS NOT STALE: the @13 verb-only recast preserved all flat_ids and all facet citation anchors. @13 had ZERO facet citations in canonical proto-lines post-cycle-2 (sensory:2 was moved to @14; no other facet anchors at @13). The semantic content of all 58 facet entries is invariant to the pin/strike verb swap (entries reference @13 as the violence-event bone; the bone identity is preserved). facets_stale_since intentionally NOT set; /and-facets re-run is NOT required for this recast.
        # PROP-0019-A VALIDATION RERUN (2026-05-29) — RETROACTIVE; chapter already shipped. This chunk_cold_read block
        # was produced by re-running the REVISED /and-substance Phase 5.5 against c05's chunks to A/B the re-scope.
        # It does NOT re-trigger downstream and does NOT set any staleness flag — c05 is terminal. Recorded so the
        # voice_risk_carry is a real artifact consumed by the Phase 8.5 revised rerun. See staff/reviews/prop-0019a-rerun-comparison.md.
        chunk_cold_read:
          reviewed_at: 2026-05-29T00:00:00Z
          verdict: PASS-CHUNK-VOICE-RISK   # original Phase 5.5 (Test 1) returned clean PASS-CHUNK; revised gate downgrades
          classification: n/a
          recovered_summary: "A surveillance-power protagonist pushes her bug-feed into a ward near court power, watches enforcers work over a courier she half-recognizes, and discovers that for the first time she can't process what she sees as neutral data."
          intended_goal: "Show the audience the moment the insect-feed stops being neutral — the color arrives before Taylor names it — and plant the courier figure whose face will matter at d10."
          continue: yes            # first-pass Q5
          continue_strict: yes     # Q7 re-answer — reader still continues, but only by excusing the listed confusions as missing prior-chapter setup
          report_path: active-project/staff/reviews/chunk-coldread-b01c05-revised-rerun.md
          disposition: n/a
          voice_risk:
            triggered: true
            signals: [A, B]
            central_event: "three figures corner the recurring courier in a side-alley and beat him (coordinated enforcement, not robbery); Taylor watches from across the ward via the feed and does not intervene"
            voice_risk_carry: |
              Central event = the courier beating in s02. The chunk renders the blow itself ONLY through
              feed/instrument abstraction — "the feed flags the contact", "contact complete, courier upright",
              "it logs: brief contact, courier retained on feet", "the feed has no field for that" — never as a
              concrete actor-verb-object strike on the page. Signal A: reader excused "why is the courier targeted"
              (causality) and "resentment asserted not motivated" (payoff) as prior-chapter setup. Signal B:
              abstraction-dense central event. Phase 8.5 Check 3 MUST verify the assembled prose delivers the
              beating at cold-reader legibility (register-the-event-as-the-event), not muffled below the feed-vocab
              — this is the FAIL #1 "a beating I almost missed" mechanism.
        cold_read:
          read_at: 2026-05-28T00:00:00Z
          verdict: SHIPPED-WITH-CAVEATS  # principal disposition 2026-05-28 per DEC-0044 (referencing PROP-0018 Class B): THREE consecutive cold-read FAILs with CONTINUE=NO each time but central event recovered all 3 times and substance contract delivered cleanly (auditor PASS / 9-of-9 SUBSTANCE-FELT / prose-rationale CLEAN). FAIL #3 fires on chapter-DESIGN concerns (stranger violence; feed mechanics; interior-cognitive payoff) that the chapter's explicit substance contract commits to. Disposition: ship c05 as terminal under PROP-0018 Class B (recovered-event design-inherent FAIL). Caveats logged below for downstream book-level verdict review.
          recovered_summary: "A surveillance-capable narrator watches a courier she's been tracking get beaten by three men, files a report, and that evening discovers her own system won't stop flagging the route she set up."
          report_path: active-project/staff/reviews/coldread-b01-c05-2026-05-28-restitch3.md
          report_path_history:
            - active-project/staff/reviews/coldread-b01-c05-2026-05-28.md  # FAIL #1 pre-revise
            - active-project/staff/reviews/coldread-b01-c05-2026-05-28-revise.md  # FAIL #2 post revise --from-signals (sexual-assault read)
            - active-project/staff/reviews/coldread-b01-c05-2026-05-28-restitch3.md  # FAIL #3 post @13 strike recast (this)
          staging_signals: 4   # /and-review staging re-stitch #3: 3 GROUND + 1 STAGE; cluster pattern 'abstract apparatus-vocabulary at structural peaks' persists at @14/@28/@33/@31 — no spec-threshold cluster trigger fires (not same-pattern≥5, not adjacent-in-peak-zone≥3, not on-axis-move-bones≥3)
          staging_report_path: active-project/staff/reviews/staging-b01-c05-2026-05-28-restitch3.md
          signal_clusters: []  # per URI-STITCH-SIGNAL-CLUSTER: staging cluster of 3 (GROUND @14 / @28 / @33) but doesn't trigger any of {same-pattern≥5, adjacent-in-peak-zone≥3, on-axis-move-bones≥3} — 3 findings are at peak/peak-shadow but NOT consecutive flat-ids; all on held/chatter bones (no axis_moves). No cluster fires per spec thresholds.
          prose_rationale_audit:
            verdict: CLEAN
            findings: 0
            report_path: active-project/staff/reviews/prose-rationale-audit-b01-c05-2026-05-28-restitch3.md
            note: "19 candidate bones scanned; 0 PROSE-RATIONALE-MUTE findings. @13 strike and @14 enforcement-beating remediation both PASS at prose layer."
          caveats:
            - "Stranger-violence (beating happens to courier, not Taylor) — design-inherent per s02 substance contract (Taylor is observer; protagonist-force is filing-as-texture)"
            - "Feed mechanics never glossed on-page — design-inherent per series conventions (insect-feed established at c01; c05 does not re-introduce per cross-episode register discipline)"
            - "Interior-cognitive payoff (Taylor closes file with no decision) — IS the chapter's substance per chapter contract; the not-deciding is the irony, moral_legibility_to_self held, filing-as-texture protagonist_force"
            - "Sera's risk told-not-shown in preamble — design-inherent; protective-arrangement-at-distance is the structural irony of the Westerosi-monument-clamp"
            - "FAIL #2 sexual-assault read REMEDIATED at bones-layer (@13 strike) + stitch-layer (@14 enforcement-beating vocabulary) — no recurrence in FAIL #3 cold-read"
          downstream_obligations:
            - "Book-level /and-review verdict b01 MUST inspect this chapter under PROP-0018 Class B disposition rules (once PROP-0018 lands)"
            - "If PROP-0018 not yet applied: book-verdict reviewer should consult DEC-0044 + DEC-0041 + DEC-0042 + DEC-0043 for c05 disposition rationale"
            - "Recurring Phase 9 cluster (4 staging-GROUND findings at @14/@28/@31/@33 — 'abstract apparatus-vocabulary at structural peaks') routes to /and-postop b01-c05 milestone for depth-of-quality review (non-blocking; advisory)"
          dispositioned_at: 2026-05-28T00:00:00Z
          dispositioned_by: principal
          disposition_dec_id: DEC-0044
          disposition_proposal_ref: PROP-0018
          continue: no
          stale_since: null
          # Phase 9 cold-read FAIL: recovered events ✓ (surveillance + courier attack + evening replay refusal); recovered central event ✓ (feed stops being neutral); BUT cold-reader answered CONTINUE=NO ("feed/count/architecture register is exhausting and I'm not sure what happened").
          # Cold-reader complaints not addressed by revise --from-signals + facet re-run + stitch re-run:
          #   1. Register exhaustion — Taylor cold-utilitarian whole-chapter; register IS the substance
          #   2. Genre-seam — Westeros names vs bug-feed surveillance read as different genres grafted together
          #   3. Hook reference not introduced — cross-episode register skipped re-gloss per c04 precedent; cold-reader is first-time
          #   4. Alley violence ambiguity — cold-reader inferred POSSIBLE SEXUAL ASSAULT from "below the register I would have called human" phrasing; the spine-raise + feet-found sequence disambiguated up-or-down but not what-kind-of-violence
          #   5. Payoff "emotionally muffled" — "the voice abstracts away the very thing the ending depends on me having felt"
          # SECOND consecutive FAIL on c05 represents an escalation signal. Per spec FAIL → /and-write revise; but this is the second iteration through revise → facets → stitch with substantively different bones structure each time and the chapter still does not pass the terminal gate.
          # Phase 9.5 admin process-critic dispatched: likely ESCALATE candidate per the SECOND-FAIL pattern.
          # Recommended next-step routing: principal review (via admin user-proxy escalation, OR direct principal call) before another full revise cycle. Candidate questions:
          #   (a) Is the chapter's substance contract (interior/observational + cold-utilitarian register + ~1600 word target) inherently at risk of register-fatigue cold-read FAIL?
          #   (b) Should the alley violence be re-staged less euphemistically to remove the assault-vs-beating ambiguity?
          #   (c) Should "Hook" get a brief re-gloss to address cross-episode register inadvertent gap?
          #   (d) Should the chapter accept a SHIPPABLE-WITH-CAVEATS verdict despite cold-read FAIL?
          # Phase 9 cold-read FAIL: chapter's central event (recognition-as-feed-stopping-being-neutral) not recovered.
          # Cold reader recovered the courier beating + Taylor's home replay but did not feel the cost (the recognition).
          # Specific confusions: cause-chain (sheet → beating) not explicit; Sera unnamed; "the Hook" unexplained; narrator faction unclear.
          # Per Phase 9 routing: structural failure → re-decompose from bones, not polish.
          # Recommended action: /and-write b01-c05 revise (then re-cascade /and-facets + /and-stitch).
          # Specific signals for revise --from-signals:
          #   - feed-stopping-neutral event needs more dramatized recognition staging at @25 (cessation IS recognition; prose may need to stage the door-closing more explicitly)
          #   - cause-chain: enforcement incident → Taylor's filing-as-Jarvis-report needs explicit causal link visible in prose
          #   - cf-d10 plant: courier-identity stakes need stronger anchor
        # /and-stitch b01-c05 emit 2026-05-28. Single-arm scene-window.
        # Phase 1 scene-window: 3 forks (scene-A 287w; scene-B 290w; scene-C 202w; total body 779w + preamble 113w = 892w pre-Phase-7; 840w post-Phase-7).
        # Phases 2-6 inline-mechanical (no faults).
        # Phase 7 per-sentence Q-line sweep: 40 sentences walked; 33 KEEP / 4 REWORD / 2 CUT-CLAUSE / 1 CUT / 0 RESHOW.
        # Phase 8 finalize: clean draft at active-project/draft/b01-c05.md; render-log at active-project/staff/stitcher/render-log-b01-c05.md.
        # Phase 9 cold-read: FAIL. Routes to /and-write revise (structural failure, not polish).
        # Phase 9.5 admin process-critic: dispatched (FAIL verdict triggers).
        chunk: |
          The insect-feed begins returning court-tier content for the first time. Taylor has
          extended coverage to a ward that abuts the lower Red Keep servant passages, and the
          bodies that move through it carry the behavioral signatures of court logistics —
          provisioning, message-running, the particular gait of people who operate under
          institutional hierarchy. She reads this content neutrally at first. Then a courier
          she has seen three times is roughed up in an alley by figures who do not look like
          common thieves — the body-language reads as enforcement, coordinated, directed at
          a specific person for a specific reason. Taylor routes this observation to Jarvis as
          a factual report. That evening, replaying the feed through memory, she notices that
          the court content is not neutral to her. Something has accumulated. She files it
          under operational texture. What shifts: political_register-prot opens its account;
          the first readable resentment color arrives; the insect-feed is no longer just
          information. The cf-d10-courier-face thread opens: this roughed-up courier is a
          body Taylor has now seen three times and will see again.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: political_register-prot
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl-d05
              notes: "first resentment color accumulates from court-tier feed content; neutral-instrumentally-observant is foreclosed; cl-d05 opens"
          axes_held:
            - axis: capability
              rationale: "no new network expansion; coverage maintenance only; level holds"
            - axis: moral_framework
              rationale: "no new licensed exception; rationalization of d04 acceptance is stable; framework at current crack-level"
            - axis: relational_anchor_status
              rationale: "Wren in coverage but no new weight; anchor holds"
            - axis: social_tether-prot-rise
              rationale: "tether load-bearing in formation but no new structural addition this chapter"
            - axis: moral_legibility_to_self
              rationale: "resentment noticed and filed; recognition not opened; legibility holds"
          density_target: 0.5-0.7
          chapter_class: standard
        dramatic_shape: rising
        goal: |
          Show the audience the moment the insect-feed stops being neutral — the color arrives before Taylor names it — and plant the courier figure whose face will matter at d10.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "Flea Bottom intelligence layer: routing to Otto through Jarvis"
            - "Sera's exposure: managed"
            - "Oswyn: active unknowing node"
            - "witch-label formation: continuing"
            - "Wren: in expanded coverage map; anchor rank 2"
          world_state:
            - "KL 122 AC; four-ward coverage; Green consolidation increment delivered"
            - "position-world rank 6"
          character_state:
            - "Taylor: capability rank 4.5; position rank 3; social_tether-prot-rise rank 3; moral_framework cracked"
            - "Otto: leverage rank 3.5; arrangement stable"
          source_chapter: b01c04
        handoff_out:
          open_threads:
            - "political_register-prot: resentment color now present in all court-tier feed interpretation"
            - "cf-d10-courier-face thread: courier body observed three times; not yet named; filed as operational texture"
            - "Flea Bottom intelligence routing: continuing"
            - "Wren: in coverage map; anchor rank 2"
          world_state:
            - "KL 122 AC; extended coverage now touching Red Keep servant-passage ward"
            - "faction-violence sub-pressure: first on-page enforcement incident observed by Taylor"
          character_state:
            - "Taylor: political_register-prot rank 2.5 (resentment color present); capability rank 4.5; position rank 3"
            - "Otto: leverage rank 3.5; unaware Taylor noticed the enforcement incident"
            - "courier-figure (unnamed): in Taylor's insect-feed memory; body-map begun"
          target_chapter: b01c06
        # /and-substance chapter b01c05 Phase 6 persist 2026-05-28.
        # Phase 5 attempts: 1 REVISE (dark-fantasy-reader REVISE on s02 data-frame collapse + s03 missing foreclosure;
        #   auditor 1 HARD on s03 pivot untagged + 1 SIGNAL + 3 FLAGS) → 2 ACCEPT (dark-fantasy ACCEPT both watchpoints;
        #   auditor 0 HARD / 0 SIGNAL / 2 non-blocking FLAGS).
        # Phase 5 reviewers: dramatist ACCEPT (att 1); cape-fic-reader ACCEPT (att 1); worm-canon-pedant ACCEPT-with-notes (att 1);
        #   dark-fantasy-reader REVISE → ACCEPT (att 2); auditor FINDINGS-PRESENT → 0-HARD (att 2).
        # Draft archived: active-project/staff/showrunner/_drafts/b01c05-draft-2026-05-28.md
        # Reviewer reports: audience STM under "## b01c05 chunk review ..." headings;
        #   auditor active-project/staff/auditor/substance-b01c05-chunk-audit.md (attempt 1 + attempt 2 sections).
        # Δ allocation: 0 / 0 / +1.5 on political_register-prot — rising shape, peak at s03 evening replay; cl-d05 first tranche (+1.5 of +3 multi-chapter ledger gain; remaining +1.5 anchors at b01c06-b01c08).
        # SOFT-WATCH (carried to /and-write b01c05): worm-canon-pedant — courier gait-signature + approach-geometry read + filing must be structurally distinct bones in s02 + s03, not collapsed to single logging assertion.
        # ADVISORY (auditor non-blocking FLAGs persisting): fault-003 (s01/s02 axes_held rationales multi-clause vs one-line schema form); fault-004 (s01 message-runner illustrative untagged events inside force-block).
        scenes:
          - slug: b01c05s01
            chunk: |
              The ward that abuts the lower servant passages of the Red Keep is called [image: the Rushwick, a lane-cluster pressed between the hill's stone skirt and the city's upward lean, its alleys too narrow to sell from but wide enough to pass through at a run] — and Taylor walks it on the second morning after the Roper's Court report, the feed extending into the new ground without ceremony. [event: Taylor extends insect coverage into the Rushwick ward, which abuts the Red Keep servant passages]. Coverage comes up across the junction within the hour. It is the same architecture she knows: who is moving, who is not moving, which passage is being avoided, which threshold is watched.

              But the bodies are different. [image: a provisioner's train crossing the main junction — four men, two carts, the particular forward-lean of people carrying loads under a tight delivery window, the unhurried-hurry of institutional rhythm]. The feed reads them as: on schedule. That is not a category that applies to Hook bodies. The distinction arrives in Taylor's categorization without language. [mechanism: court-tier bodies carry institutional-gait signatures — provisioning cadence, message-running intervals, the physical compression of people accountable to someone above them — and the feed reads these as a different class of pattern than ward-resident foot traffic]. She files it as: different substrate. She does not qualify the difference further.

              [force: Taylor's neutral-instrumental reading discipline — the same factual-observation register applied to the Hook, to Pig Tallow Lane, to Roper's Court, applied now to new ground] holds the court-tier content at the same distance as everything else. A message-runner passes the junction at the double-step of someone on a specific errand. The feed tracks him to the lane-mouth and releases him from coverage range. Taylor reads: message-running body, institutional function, no anomaly. She does not note who the message was from, or where it was going, or what the double-step means in a court whose internal logistics she has read about but not observed from the ground.

              [force: the court-tier content's novel weight — the substrate has changed even though the method has not] does not announce itself. It is present only in the specificity with which Taylor's categorization is being asked to work. She names the provisioner train. She names the message-runner's gait-class. She does not name what it means that these bodies are connected to the architecture that keeps Sera's exposure managed. The discipline holds. [event: first day of court-tier content in the insect-feed — Taylor reads neutrally; categorization-layer engaged without affect]. The ward runs its schedule. Taylor reads the ward.
            substance_delta:
              axes_in_motion: []
              axes_held:
                - axis: political_register-prot
                  rationale: "court-tier content arrives; Taylor reads it with the same factual-categorization register she applies to Hook content; the discipline is intact; no color has accumulated yet — this is the first exposure, and the first exposure reads as: different substrate, same method"
                - axis: capability
                  rationale: "coverage extension to Rushwick is maintenance-of-expansion from c04's four-ward map, not a new expansion event; the coverage range is confirmed active, not newly grown"
                - axis: moral_framework
                  rationale: "categorizing court-logistics bodies as intelligence substrate is already inside the licensed exception; the d04 rationalization runs unchanged; no new exception opened"
                - axis: relational_anchor_status
                  rationale: "Wren not in this ward; anchor not activated"
              density_target: 0.5-0.6
            scene_conflict:
              protagonist_force: "Taylor's neutral-instrumental reading discipline — the factual-observation register she has held since arrival, applied unchanged to court-tier content"
              opposing_force: "the court-tier content's novel weight — bodies moving on institutional schedule, accountable to a hierarchy whose upper tiers she is already embedded in; the substrate has changed even though the method has not"
              stakes_axis: political_register-prot
            stale_since: null

          - slug: b01c05s02
            chunk: |
              The courier is a man of middle years, compact build, [image: a courier Taylor has now seen three separate times in the Rushwick — the same gait on three different mornings, slightly heel-first, the walk of someone who has learned the ward's uneven paving by repetition]. She has not named him. The feed has filed him as: recurring body, probable Rushwick-resident or regular-transit, no anomaly. [event: third sighting — five days into the Rushwick coverage; the feed confirms: recurring body, same heel-first gait, same morning-hour transit window].

              [event: the courier is roughed up in a side-alley off the Rushwick junction by three figures whose body-language reads as enforcement, not robbery]. Taylor is at the ward's far end when the feed flags the contact — three bodies closing on one body in the short-alley off the junction's east exit, the geometry of the approach not consistent with opportunistic theft. [mechanism: enforcement reads differently from robbery in the feed — the coordination of approach, the blocking of exits before contact, the absence of the post-contact scatter that marks common theft; instead, a controlled containment, a single body held against stone, two others keeping the alley-mouth]. From across the ward the feed returns: contact complete, courier upright. What it does not return is the sound from the alley before the courier finds his feet — a low, effortful sound, not a cry, the kind a body makes when it is trying not to make any sound at all. The feed has no field for that. It logs: brief contact, courier retained on feet. She watches the exchange without crossing toward it. The courier is left on his feet. The three figures leave at a walk, not a run.

              [force: the observation's specificity — this is enforcement, coordinated, directed at a specific person for a specific reason; the content has named itself as faction-violence in a way Hook content never did] sits in the feed's record. Taylor begins the Jarvis report in the same register she uses for passage-avoidance patterns and junction-agitation clustering. Movement-pattern. Body-count. Approach geometry. Duration. Resolution: courier retained on feet; three figures exited east. [event: Taylor routes the enforcement incident to Jarvis as a factual movement-pattern report — no name for the courier, no inference about which faction directed the enforcement, no speculation about cause]. The report is accurate. It is what the feed reads. It is what the feed reads.

              [force: Taylor's factual routing discipline — the observation enters the report as movement-pattern, and the discipline of treating court-adjacent content as categorizable data holds at the action layer]. The courier recovers his balance and continues through the ward on his original heading. The feed tracks him to the corner and releases him. Taylor does not follow. She does not note the courier's face for anything beyond the movement-pattern field. [image: the three figures' departure walk — unhurried, purposive, the specific gait of people who have finished a piece of work and have somewhere else to be]. [event: cf-d10-courier-face thread initiated — courier body flagged as recurring, three observations now logged; enforcement incident attached to the filing].
            substance_delta:
              axes_in_motion: []
              axes_held:
                - axis: political_register-prot
                  rationale: "enforcement routed as movement-pattern; categorization-layer intact; no color opened at action-layer"
                - axis: moral_framework
                  rationale: "routing enforcement as pattern-data is inside the licensed exception; 'this is what the feed reads' echo is rationalization running, not interrogated"
                - axis: capability
                  rationale: "no new coverage expansion; Rushwick coverage operational"
                - axis: relational_anchor_status
                  rationale: "courier not a relational anchor; Wren not present"
              density_target: 0.55-0.65
            scene_conflict:
              protagonist_force: "Taylor's factual routing discipline — the observation enters the Jarvis report as movement-pattern; the discipline of treating court-adjacent content as categorizable data holds at the action layer"
              opposing_force: "the enforcement incident's specificity — coordinated, directed at a named body for a named reason; the content has named itself as faction-violence in a way Hook content never did; the discipline's categorization is absorbing a class of content it was not built to process without registering the stretch"
              stakes_axis: moral_framework
            stale_since: null

          - slug: b01c05s03
            chunk: |
              That evening Taylor runs the day's feed through memory — [event: evening replay of the Rushwick feed; Taylor reads the court-tier content in review rather than in real-time acquisition] — the standard end-of-coverage accounting, the same procedure she has run every night since the Hook. The Hook content reads in review as it reads in acquisition: bodies, clusters, passage-avoidance, agitation-patterning. She runs it without residue. [image: the Hook's feed-texture in evening review — flat, like a document she has already processed; the wards she knows running on schedule, the anomalies noted and incorporated; the information completing itself as information].

              [mechanism: The Rushwick reads differently in review than it read in acquisition — evening replay strips the acquisition-layer's real-time categorization discipline; there is no action to take, no report to route, no function being performed; the content sits without the discipline's organizational frame, and what remains is not flat; the provisioner train's institutional-gait signature carries something that the factual-categorization register was holding at distance during the day]. [event: Taylor notices that the court-tier content is not neutral to her — resentment color identified in review, after the fact, in the absence of the discipline's real-time frame]. She does not name what she notices. She names what she does: she files it under operational texture.

              [force: the accumulation that has happened regardless of categorization — the color has arrived in the feed; neutral-instrumentally-observant has been the method of acquisition but the substrate has been adding something to the ledger without her accounting registering it] sits in the replay without a label Taylor applies to it. [image: the courier's post-enforcement walk — him continuing on his original heading, the specific quality of a body that has just been reminded it is being watched and is performing normalcy in response]. Taylor has been reading court bodies. Court bodies are connected to the architecture that keeps Sera protected. Court bodies move under a hierarchy that produced the enforcement geometry she watched this afternoon. She has been reading this and she has not been neutral about it.

              [force: filing the observation under operational texture — Taylor's discipline of categorizing her own response extends the same factual-register to the recognition itself; the color arrives and gets named as texture rather than named as resentment]. [event: political_register-prot opens its account — resentment color present; neutral-instrumentally-observant foreclosed; cl-d05 anchor lands]. The courier's face is in Taylor's body-map now, not in any ledger she writes. [event: cf-d10-courier-face thread confirmed open — courier logged as recurring body with enforcement-incident attached; Taylor will recognize him again]. She closes the evening review. She tries to run the Rushwick back through the flat-document read — the same read that closes out the Hook, the same read that resolves the ward's content into information. It does not resolve. The Rushwick content does not complete itself as information. She runs it again. The same. The Hook runs flat under the same pass. The Rushwick does not. The neutral read is not available to her for this content anymore, and she files the unavailability as texture, but the filing does not return the read.
            substance_delta:
              axes_in_motion:
                - axis: political_register-prot
                  direction: up
                  target_delta_magnitude: 1.5
                  cost_ledger_anchor: cl-d05
                  notes: "evening replay reveals accumulated color; the discipline's real-time categorization frame was holding neutral-instrumentally-observant in acquisition but the substrate was not neutral; Taylor notices in review; the recognition IS the opening of the account; neutral-instrumentally-observant is foreclosed from this point; cl-d05 anchor lands here; Rushwick content now carries permanent resentment-color in Taylor's feed-interpretation; first tranche (+1.5 of +3 cl-d05 ledger gain; remaining +1.5 anchors at b01c06-b01c08 during the readable-resentment escalation toward d09 articulated-contempt)"
              axes_held:
                - axis: moral_framework
                  rationale: "resentment color noticed and filed as operational texture; the rationalization is not interrogated here — Taylor applies the same categorization discipline to her own response that she applies to the feed; the licensed exception is not threatened by noticing affect; legibility crack does not deepen this scene"
                - axis: capability
                  rationale: "no new coverage extension; evening review is operational accounting, not expansion"
                - axis: relational_anchor_status
                  rationale: "the courier is not a relational anchor; the body-map filing is operational texture, not anchor-formation; Wren not present"
                - axis: social_tether-prot-rise
                  rationale: "tether load-bearing in formation per c04; no new structural addition this scene"
                - axis: moral_legibility_to_self
                  rationale: "resentment noticed and filed; the filing-as-texture IS Taylor not opening the recognition; legibility holds — the recognition is categorized, not examined; moral_legibility_to_self does not move until Taylor can no longer successfully file the color as something other than what it is"
              density_target: 0.6-0.7
            scene_conflict:
              protagonist_force: "filing the observation under operational texture — Taylor's discipline of categorizing her own response extends the same factual-register to the recognition itself; the color is named as texture rather than named as resentment"
              opposing_force: "the accumulation that has happened regardless of categorization — the color arrived in the feed without Taylor's real-time accounting registering it; political_register is opening whether Taylor names it as such or files it as texture"
              stakes_axis: political_register-prot
            stale_since: null

      # /and-substance chapter b01c06 — ATTEMPT 1 VOIDED (2026-05-30):
      # The orchestrator confabulated a wrong chapter (a "missing-girl rescue" with fabricated
      # cost-ledger anchors cl06a/cl06b and a +1.0/+1.0/+1.0 Δ) and briefed all Phase-2/4/5/5.5
      # agents on it. The Phase 4 auditor (cl06a/cl06b nonexistent; Δ contradicts this contract)
      # and the dramatist (4-scene rescue ≠ this 3-scene Otto-elder-list chapter) caught the
      # substitution. The contract below was NEVER altered. Attempt-1 artifacts quarantined:
      #   _drafts/b01c06-draft-2026-05-30.md.VOIDED, chunk-cold-read-b01-c06.md.VOIDED.
      #
      # /and-substance chapter b01c06 — ATTEMPT 2 (correct chapter) PERSIST (2026-05-30):
      # v2 scenes authored against the real contract; draft _drafts/b01c06-draft-2026-05-30-v2.md.
      # Phase 4 auditor CLEAN (0 HARD; 1 FLAG: cl-d06 second relational_anchor tranche +1.0 of +2
      #   unanchored downstream → parking-lot pl-2026-05-30-001, resolves b01c08-c10).
      # Phase 4 dramatist ACCEPT (rise-peak-fall; peak at s03 send; s01-omission/s03-delivery contrast
      #   lands at chapter-close; s02 earns place as loaded pause).
      # Phase 5 audience ACCEPT 3-of-3. Two bones-execution watches carried to /and-write
      #   (parking-lot pl-2026-05-30-002): (a) dark-fantasy — Wren omission must be enacted as a
      #   physical pause + field-entry, NOT interior moral narration; (b) cape-fic + pedant — the
      #   ward-coverage-notes vs Jarvis-channel substrate gap must be a concrete institutional
      #   mechanism, not "Taylor hoping."
      # Phase 5.5 chunk-cold-read = CHUNK-CLASS-B (summary MAPS to goal; causality + payoff affirmed;
      #   central event recovered as concrete SVO — Step 2.5 Signal B would NOT fire); strict-Q7
      #   CONTINUE=no driven ENTIRELY by undefined c01-c05 proper nouns (mid-series context-noise,
      #   the c05 FAIL root cause — NOT a chunk-design defect). admin user-proxy DEC-0044 disposition
      #   (P): proceed, record Q7 confusion list as cold_read_risk_carry → hand to /and-review bones
      #   follow_check (PROP-0020). report: active-project/staff/reviews/chunk-coldread-b01c06-2026-05-30.md
      - slug: b01c06
        status: stitched   # /and-stitch b01c06 COMPLETE (depth-pass re-cascade): draft/b01-c06.md TERMINAL (Phase 9 PASS-TERMINAL-DEPTH-RESOLVED, DEC-0058, 2026-05-31). pl-2026-05-31-002 stitch render-watches resolved. Phase 9.5 process-critic: PROP-0029 + DEC-0059 (abstract-by-contract branch). Was audited-r1 from /and-facets re-cascade (Phase 5 HARD=0 + Phase 5b ACCEPT 3/3 all 10 facets, 2 cycles). Was bones-written from /and-write revise --from-signals (depth pass, DEC-0048/0056): s03 accounting de-abstracted + verdict-pause bone added; 26 bones re-emitted.
        facets_complete:   # RE-CASCADE (depth pass, 2026-05-31, 26-bone scaffold) — supersedes the stale pre-revise record (preserved below)
          stale_since: null
          audit_path: active-project/staff/auditor/facets-final-audit.md
          audit_complete: true
          audit_hard_findings: 0   # 1 HARD (vibes:19 dangling memory:1 from R2 mem:1 delete) fixed cycle-1
          audit_signal_findings: 4   # oc-prop card-resolution, sensory density, state-updates density, memory single-register (all advisory)
          audience_gate_path: active-project/staff/auditor/facets-audience-gate-r2.md
          audience_gate_complete: true
          audience_gate_cycles: 2   # cycle-1: 8/10 ACCEPT; cycle-2: sensory + memory remediated -> ACCEPT 3-of-3 all 10
          audience_gate_cap_burned: false
          bidirectional_loop: validated   # shared finding: monument-slug card-absence (auditor signal-001 + worm-canon memory render-risk)
          facets_path: active-project/theater/facets/
          round_1_complete: true
          round_2_complete: true   # R2: mem:1 deleted (spineless), narrator:7 added (substrate carrier); else KEEP/zero
          context_followability_final: {completeness: FOLLOWABLE, readability: ALIVE}   # PROP-0020/0022 — PROP-0023 honesty-check applied; genuine bone-layer ALIVE
          phase_5c_admin: skipped   # final cycle clean ACCEPT, no cap-burn, no WARN
          margit_referrals_open: [SEAM-006 oc-ward-coverage-notes, SEAM-007 oc-jarvis-channel-form, SEAM-008 oc-accounting-ledger, monument-override-architecture-residue]   # prop+monument cards; mem:2 carries render-fence note pending card
          # --- PRE-REVISE record (superseded 2026-05-31; was audited-r1 on the 25-bone scaffold): audience_gate_r3, 3 cycles, audit_signal 10 ---
        stitched: true   # /and-stitch b01-c06 RE-CASCADE COMPLETE (2026-05-31 depth pass); draft/b01-c06.md re-emitted de-abstracted/person-first; terminal deliverable. Phase 8.5 + Phase 9 cold-read pending verdict.
        cold_read:
          read_at: 2026-05-30
          verdict: PASS-WITH-DEPTH-PASS-REQUIRED   # DEC-0048; ships terminal + mandatory depth pass before book-stable
          completeness_axis: {verdict: PASS, basis: "central event (named-person delivery + omission contrast) recovered; jeopardy 3-layer; causality holds; CONTINUE weak-yes"}
          readability_axis: {verdict: AIRLESS, basis: "reader still reads narrator as instrument reporting itself; accounting middle worst; withheld-name payoff reads as 'a tidy diagram of a feeling'. Breathing spots = the Wren line + the dragging-stylus grounding add (sensory:5 @17) — the overhaul interventions landed but did not de-abstract the apparatus-dominant bone-set"}
          recovered_summary: "A surveillance operative is pushed to hand over four people by name, does it to keep a hidden girl alive, and quietly protects the one child whose name they refuse to write down."
          report_path: active-project/staff/reviews/coldread-b01c06-2026-05-30.md
          signal_clusters: []   # single-arm; spine-staging-gap not triggered (central event recovered + staged: 'I sealed it', 'fingers settled and did not open them at once')
          depth_pass_pending: false   # RESOLVED 2026-05-31 (DEC-0058)
          depth_pass_resolved_at: 2026-05-31
          stale_since: 2026-05-31   # this cold_read verdict (PASS-WITH-DEPTH-PASS-REQUIRED) is the PRE-revise record; superseded by the re-cascade cold_read below
        cold_read_recascade:   # /and-stitch b01-c06 depth-pass re-cascade Phase 9 (2026-05-31); DEC-0058 disposition
          read_at: 2026-05-31
          verdict: PASS-TERMINAL-DEPTH-RESOLVED   # depth pass EXECUTED + RESOLVED per DEC-0058; ships terminal. (Separated scoring: completeness PASS; readability AIRLESS accepted as abstract-by-contract — NOT a remediable defect.)
          completeness_axis: {verdict: PASS, basis: "central event (four-name send + omission-contrast) RECOVERED; jeopardy inferred; causality tight; CONTINUE marginal-yes. Step-2 FAIL conditions do not fire."}
          readability_axis: {verdict: AIRLESS-ABSTRACT-BY-CONTRACT, basis: "improved over original ('there IS a person; the crowd breathes' vs 'no one home'), but the accounting/central-event zone still reads apparatus ('a man describing his own bookkeeping in abstract nouns / held at arm's length / never feel the cost'). DEC-0058: residual AIRLESS is abstract-by-contract — offstage victims + no-choice thesis + cold-utilitarian ledger-POV are project-spine design commitments (cond-taylor-pov-behavior; 'the accuracy is the catastrophe'), NOT remediable bone/prose defects. 0-mute prose-rationale audit (every concrete element staged) confirms de-abstraction exhausted; DEC-0048 escalation clause falsified by the 0-mute audit (DEC-0007 anti-literalism). The administrative-feel IS the intended phenomenology."}
          recovered_summary: "A spy-informant, after a stranger's small kindness, coldly logs and ships four named men to his handler while pretending he had any choice in it."
          report_path: active-project/staff/reviews/coldread-b01c06-2026-05-31.md
          coherence_review: {verdict: PASS, report: active-project/staff/reviews/coherence-b01-c06-2026-05-31.md, note: "substance-aware PASS; informed-compensation pattern vs cold-read per PROP-0023/DEC-0049"}
          prose_rationale_audit: {mute_count: 0, bones_checked: 20, verdict: SIGNAL-only, report: active-project/staff/reviews/prose-rationale-audit-b01-c06-2026-05-31.md}
          signal_clusters: []   # no cluster; 0 prose-mutes; no spine-staging-gap (all central-event bones staged per Step 3.5)
          disposition: DEC-0058 (Option C — accept terminal; airlessness abstract-by-contract; Option B contract-revision remains principal's zero-cost override)
          stale_since: null
        chunk: |
          Taylor runs the first deliberate rationalize-each-trade beat. A request comes
          through Jarvis that is not ambiguous: Otto wants to know which Flea Bottom ward
          elders have Black-faction sympathies — names, not movement patterns. Taylor
          compiles the list. She runs the accounting explicitly before sending it: names vs.
          Sera's continued protection; the harm from naming vs. the harm from Sera's exposure.
          The accounting is honest. The accounting is the breach. She sends the list. The
          chapter also contains a Wren encounter — first spoken exchange, brief, Wren helping
          Taylor navigate a blocked lane. Taylor includes the encounter in her ward-coverage
          notes and does not note Wren's name in any ledger accessible to Jarvis. The
          collision: Taylor has rationalized a named-person intelligence delivery, and the
          un-priced contact is now an actual contact she is protecting by omission from the
          deliverable. What shifts: moral_framework down, relational_anchor_status up,
          moral_legibility crack deepens.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: moral_framework
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl-d06
              notes: "named-person intelligence delivered after explicit accounting; rationalize-each-trade pattern established; cl-d06 cost side"
            - axis: relational_anchor_status
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl-d06
              notes: "first spoken exchange with Wren; Taylor protects Wren from the deliverable by omission; anchor account gains first active weight; cl-d06"
            - axis: moral_legibility_to_self
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "Taylor's explicit accounting of the name-delivery is the legibility crack deepening; rationalization is honest, which makes it more visible to the reader and slightly more visible to Taylor"
          axes_held:
            - axis: capability
              rationale: "no new network expansion; intelligence delivery is coverage already built"
            - axis: position-prot-rise
              rationale: "position established; no new formalization event; holds at current level"
            - axis: political_register-prot
              rationale: "resentment color present but not advanced this chapter; rationalization beat occupies the structural slot"
            - axis: social_tether-prot-rise
              rationale: "no new tether addition; the Wren contact is explicitly kept OUT of the deliverable tether layer"
          density_target: 0.6-0.8
          chapter_class: standard
        dramatic_shape: climax
        goal: |
          Show the audience the first named-person delivery and the accounting that precedes it, so the rationalize-each-trade pattern is legible — and show Wren's omission from the deliverable as the un-priced move it is.
        pov_narrator: taylor-hebert-kl-122ac
        bones_file: theater/bones/b01-c06.md
        bones_count: 26   # was 25; +1 verdict-pause bone (b01c06s03n11) added at revise Phase 3
        substance_bone_gate_verdict: PASS   # re-confirmed at revise Phase 6 (s03 re-gated; s01/s02 prior PASS carried)
        # /and-review bones b01c06 (2026-05-30): PASS. Fidelity 0 HARD (spine intact all 3 scenes; dialogue coverage+card-compliance PASS; SVO clean 25/25; scene-map 25/25). follow_check PASS-WITH-NOTES (PROP-0020: every context-blind cold-read proper-noun confusion resolved by prior-chapter context = mid-series context-noise, not a bone defect). Aliveness BONES-AIRLESS-RISK advisory (apparatus-dominant accounting chapter; embodied spine present; forwarded downstream). 2 Phase-6 SIGNALs remain advisory. /and-facets cleared.
        bones_review:
          reviewed_at: 2026-05-31T00:00:00Z   # re-review after revise depth pass; supersedes 2026-05-30 (preserved at report_path_prior)
          report_path: active-project/staff/reviews/bones-b01c06-revise-2026-05-31.md
          report_path_prior: active-project/staff/reviews/bones-b01c06-2026-05-30.md
          verdict: PASS-WITH-NOTES   # 26 bones SVO-clean (recast s03 + @20 stills-the-hand verified independently); chunk->bones spine intact 3/3; scene-map 26/26; follow_check holds
          follow_check: PASS-WITH-NOTES   # no NEW followability gap from de-abstraction; sera-coverage-entry = same mid-series context-noise class, not a bone defect
          aliveness: BONES-AIRLESS-RISK-CLEARED   # PROP-0022 — depth pass succeeded at bone layer; s03 accounting middle now concrete embodied beats (writes/stills-the-hand/seal); residual risk is render-layer only -> pl-2026-05-31-002 + scene-map s03 protected-patterns
          dialogue_fault_resolved: "fault-001 (FAULT-DIALOGUE-MISSING-AT-ANCHOR @4): theater/dialogue/wren-stitch-maker-flea-bottom-ward.md was absent (orphaned by c07 flat-path dialogue authoring; @4 unchanged by this revise). RESTORED verbatim from _archive/20260531T021620Z-b01c06-facets/ — faithful to the unchanged @4 anchor. /and-facets now cleared."
          flag_001_to_stitch: "@17 writes-the-ward-elder-names render as concrete inscribed text not list-concept (render-layer watch)"
          bones_file_mtime_at_review: regenerated-2026-05-31   # bones file rewritten from memory at Phase 7 emit this session
          stale_since: null   # re-review complete; /and-facets b01c06 CLEARED
        context_followability:   # PROP-0020/0022 — /and-facets Phase 2.5 + 4.5
          completeness_verdict: FOLLOWABLE   # Ph2.5 + Ph4.5 both; context-ledger empty (0 CONTEXT-REQUIRED)
          readability_verdict: ALIVE  # Ph4.5 AIRLESS-HOLE -> Ph4.6 grounding remediation (sensory:3/4/5 @10/@16/@17) -> Ph4.6-Step2 re-review ALIVE (continuous somatic thread across hinge)
          report_path: active-project/staff/reviews/context-follow-r2-b01-c06-2026-05-31.md  # re-cascade post-revise; PROP-0023 honesty-check applied, genuine bone-layer ALIVE (not false-ALIVE)
          reviewed_at: 2026-05-31
          context_ledger_open: 0
          grounding_ledger_open: 0   # grd-001/002/003 all satisfied by sensory:3/4/5 at Phase 4.6 (cap-exempt licensed adds)
          voice_fixable: ["@19"]   # re-cascade: only flat-19 (marks red-keep coverage record) VOICE-FIXABLE -> /and-stitch Phase 4 (render concrete, not architecture-summary)
        substance_delta_measured:
          axes_moved:
            - relational_anchor_status +1.0
            - moral_framework -1.0
            - moral_legibility_to_self +1.0
          density_measured: "0 chatter / 26 bones; grounding 24/26 (s03 de-abstracted; auditor abstraction-dominance 91%)"
          felt_verdict: SUBSTANCE-FELT-3of3   # revise Phase 6: s03 re-gated SUBSTANCE-FELT 3/3 + airless-cleared 3/3; s01/s02 prior PASS carried
        # Bone-gate note: Phase 6 bone-gate PASS (auditor: 1 HARD fault-001 HELD-AXIS-NOT-WITNESSED
        # political_register-prot s01 → resolved by assigning to s01n02; 2 SIGNALs accept-with-rationale:
        # mls +0.5→+1.0 overdelivery + s03 stakes-axis tie, both DEC-0030 bone-floor artifacts;
        # EVENT-NOT-CONCRETE/ABSTRACTION-DOMINANCE/SENSORY-GROUNDING/dialogue all PASS).
        # Audience SUBSTANCE-FELT 3/3. Phase 6.5 admin OK-MERGED (DEC-0046; PROP-0010/0011 recurrence bumped).
        # Per-scene moral_legibility SIGNAL disposition: accept-with-rationale.
        handoff_in:
          open_threads:
            - "political_register-prot: resentment color present in all court-tier feed"
            - "cf-d10-courier-face: courier body in Taylor's memory"
            - "Flea Bottom intelligence routing: continuing"
            - "Wren: in coverage map; one seen-not-spoken contact; anchor rank 2"
          world_state:
            - "KL 122 AC; extended coverage active"
            - "faction-violence sub-pressure: first incident logged"
          character_state:
            - "Taylor: political_register-prot rank 2.5; capability rank 4.5; position rank 3; moral_framework cracked"
            - "Otto: leverage rank 3.5"
          source_chapter: b01c05
        handoff_out:
          open_threads:
            - "rationalize-each-trade pattern: established; first named-person delivery on record"
            - "Wren: first spoken exchange; omitted from deliverable; anchor rank 3 (weight added by omission)"
            - "moral_legibility crack: deeper; accounting is honest and that honesty is visible"
            - "Black-faction ward elders named to Otto: downstream consequence pending"
            - "cf-d10-courier-face: courier in memory; not yet a face"
          world_state:
            - "KL 122 AC; named-person intelligence flowing; Green consolidation advancing through ward-elder identification"
            - "faction-violence sub-pressure: operational follow-through on the named list will produce on-page consequences"
          character_state:
            - "Taylor: moral_framework rank 0 (rationalized breach on record); relational_anchor_status rank 3; moral_legibility rank 5; position rank 3; political_register-prot rank 2.5"
            - "Wren: in coverage map; spoken-contact made; not in deliverable layer"
            - "Otto: leverage rank 3.5; named-person intelligence received"
          target_chapter: b01c07

        chunk_cold_read:
          reviewed_at: 2026-05-30T00:00:00Z
          verdict: CHUNK-CLASS-B
          classification: B
          recovered_summary: "A surveillance operator does a clean, honest cost-benefit on whether to hand over four names to a spymaster, decides yes, and the horror is that the math worked — bracketed by a small kindness where she quietly refuses to log a girl's name."
          intended_goal: "Show the audience the first named-person delivery and the accounting that precedes it, so the rationalize-each-trade pattern is legible — and show Wren's omission from the deliverable as the un-priced move it is."
          continue: yes          # first-pass Q5 (marginal yes)
          continue_strict: no     # Q7 re-answer; AUTHORITATIVE for classification
          report_path: active-project/staff/reviews/chunk-coldread-b01c06-2026-05-30.md
          disposition: P
          dispositioned_at: 2026-05-30T00:00:00Z
          dispositioned_by: admin   # DEC-0044
          voice_risk:
            triggered: false
            signals: []
            central_event: "Taylor marks the four names; the courier takes the list (the send)."
            note: "Step 2.5 not formally run (CLASS-B), but recorded: Signal B would NOT fire — central event recovered as concrete SVO; concreteness floor held. Contrast c05 retroactive PASS-CHUNK-VOICE-RISK."
          cold_read_risk_carry: |
            Strict-NO driven entirely by undefined c01-c05 proper nouns / world-terms (NOT internal-logic gaps;
            reader affirmed causality + payoff + summary-maps). Context-weave checklist handed to
            /and-review bones follow_check (PROP-0020): the feed (insect-network, c01); Jarvis (courier
            channel to Otto, c03+); Otto / Sera / Alicent (c03-c05); "the arrangement" (Otto trade for
            Sera's protection, c03-c04); Black/Green factions (series + c01-c05); Wren (cost-bearer, c01);
            stitch-houses / ward / the Hook (c01); "first deliberate" (relative to prior movement-pattern
            deliveries, c04-c05).
        scenes:
          - slug: b01c06s01
            seq: 1
            status: planned
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              [force: Taylor's ward-walk — the Hook in the early-work hour, the feed running at
              its standard morning density; she has been reading this stretch since before the
              stitch-houses open their shutters; it is coverage-maintenance, the same register
              she has used every morning since b01c01]. The lane she uses to cross from the
              Hook's south junction to the Butcher's Lane drain-angle is blocked this morning —
              a handcart with a broken axle sitting crossways in the lane-mouth, two men arguing
              over whether to lift it or drag it, a small crowd of bodies backing up behind them.
              [image: the backed-up lane — the particular stillness of a Flea Bottom street
              waiting to move again; bodies reading as annoyed but patient, the way bodies read
              when the delay is inconvenient rather than threatening; the feed returns no
              anomaly, only the compression of stopped foot traffic].

              [event: Wren finds Taylor in the backed-up crowd and addresses her directly —
              the first spoken exchange between them]. Not a summons. Not a greeting performed
              for an audience. Wren is there because the stitch-house lane feeds into the same
              blocked junction and she has been standing at the edge of the backup, waiting,
              when she sees Taylor. She says: there is a way through. The south court off the
              tallow-boiler's wall, if you cut before the handcart — the gap is narrow but
              passable. She says it plainly, the way a Flea Bottom child says something she
              has already checked and found true. [mechanism: Wren's aid in Flea Bottom form —
              a practical observation delivered without preamble, without establishing familiarity,
              in the specific register of someone who noticed a thing and names it to the person
              who will find it useful; she does not wait for acknowledgment; she turns back
              toward the backup and finds the gap herself]. Taylor follows.

              [force: the smallness of the exchange — it is twenty words, a direction, a gap
              in a wall; the feed reads Wren the way it has read Wren since the first sighting:
              a ward-body, familiar profile, stitch-house proximity; nothing about the exchange
              registers as operationally significant in the feed's architecture; it is between
              the bodies, not between the layers the feed measures]. The gap is where Wren said
              it was. Taylor comes through the south court and picks up the drain-angle route
              on the far side of the blocked lane. [event: Taylor logs the encounter in her
              ward-coverage notes — a brief contact entry, the standard form she uses for any
              unscheduled street interaction; she notes the blocked lane, the workaround route,
              the time of day, the contact source].

              She reaches the field for the contact source and considers what to write.
              [force: the ledger discipline — she records contacts in the coverage notes because
              contacts are data; the ward-coverage notes are not Jarvis-accessible but they are
              the working substrate of her intelligence; what goes in them shapes what she can
              route; what goes in them can be inferred, with effort, by someone reading the
              pattern of her observations]. [event: Taylor runs the accounting on whether to
              note Wren's name in the contact-source field — she considers what naming Wren
              in the notes means in the downstream direction of the arrangement; she considers
              the gap between the ward-coverage notes and the Jarvis channel, and whether that
              gap is sufficient, and whether it will remain sufficient; she considers what it
              would mean to make Wren legible in any substrate that could become Jarvis-adjacent].
              [mechanism: the omission as deliberate ledger choice — Taylor's hand pauses over
              the contact-source field; she writes: ward-resident, Hook, routine; she does not
              write a name; the blank is authored, not absent; the decision to omit is made with
              full understanding of what it omits and why; she is protecting Wren from the
              deliverable layer by choosing what the notes say]. The entry closes. She continues
              the ward-walk.

              [event: relational_anchor_status +1.0 — the spoken exchange moves Wren from
              ward-in-coverage to active-protection-register; the deliberate omission from the
              contact-source field is the relational act that weights the anchor; Taylor has now
              made a choice about what to withhold from the arrangement on Wren's behalf;
              cl-d06 gain side; first tranche].

            substance_delta:
              axes_in_motion:
                - axis: relational_anchor_status
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl-d06
                  notes: "first spoken exchange with Wren; Taylor runs the accounting on naming Wren in the contact-source field and chooses not to; the omission is authored, not absent — she writes 'ward-resident, Hook, routine' and leaves the name blank; the decision to protect Wren from the deliverable layer is the relational act that weights the anchor; cl-d06 gain side, first tranche (+1.0 of +2 ledger gain; second +1.0 anchors at b01c08-b01c10 when Wren becomes structurally necessary to the coverage map). This scene must carry the dialogue-cobonded anchor — /and-write must treat the Wren direction-delivery and Taylor's follow as dialogue-anchor bones with [wren-stitch-maker-flea-bottom-ward:N] citation."
              axes_held:
                - axis: moral_framework
                  rationale: "the omission is protective, not a delivery; Taylor has not received the Otto request yet; the framework holds at current crack-level; no new named-person delivery authored this scene"
                - axis: moral_legibility_to_self
                  rationale: "the accounting on the name-field runs cleanly; Taylor knows what she is omitting and why; legibility holds — the recognition is filed, not suppressed; the crack does not deepen until the honest accounting precedes a delivery in s03"
                - axis: capability
                  rationale: "coverage-maintenance walk; no new network expansion; the ward-walk is the existing architecture running at standard density"
                - axis: position-prot-rise
                  rationale: "no patron-tier visibility event; the Wren exchange is ward-layer; position holds at current rank"
                - axis: political_register-prot
                  rationale: "no court-tier content in this scene; the blocked lane and the stitch-house ward are Flea Bottom registers; resentment has no material to form on"
                - axis: social_tether-prot-rise
                  rationale: "the Wren contact is explicitly kept OUT of the deliverable tether layer; the omission from the contact-source field is the mechanism of that exclusion; tether holds — no new structural addition; social_tether-prot-rise moves when a contact enters the arrangement layer, which Wren does not"
              density_target: 0.55-0.7
            scene_conflict:
              protagonist_force: "Taylor's coverage-note discipline — she records contacts in the working substrate of her intelligence because contacts are data; the discipline is precise and consistent; the same discipline she applies to every ward-body in the feed"
              opposing_force: "the Wren contact as a case the discipline was not built to handle — the coverage notes and the Jarvis channel are different substrates, but the gap between them is not infinite; to name Wren in the notes is to make her legible in a substrate that could be read; to omit her is to author a gap in the record"
              stakes_axis: relational_anchor_status
            bones:
              - slug: b01c06s01n01
                flat_id: 1
                svo: "the handcart blocks the lane-mouth"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: capability
                    rationale: "coverage-maintenance register — the ward-walk architecture in operation; the obstruction surfaces the feed running at standard morning density; the blocked lane enacts the walk-as-ongoing-discipline"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s01n02
                flat_id: 2
                svo: "the crowd presses the junction"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: capability
                    rationale: "the backup as feed-data — bodies compressing at the junction are the feed returning its morning read; the coverage architecture performing its function; capability holds at current rank"
                  - axis: political_register-prot
                    rationale: "the junction crowd is Flea Bottom-layer foot traffic; no court-tier content present in the blocked-lane / ward-walk context; resentment color (carried from c05) has no material to form on at this scene; political_register-prot holds at current rank (Phase-6 fault-001 witness)"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s01n03
                flat_id: 3
                svo: "wren-stitch-maker-flea-bottom-ward crosses the crowd"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: social_tether-prot-rise
                    rationale: "Wren crossing the crowd is a ward-body movement, not a tether-formation event; she is not entering the deliverable layer; tether holds"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s01n04
                flat_id: 4
                svo: "wren-stitch-maker-flea-bottom-ward speaks to taylor-hebert-kl-122ac"
                shape: moving
                axis_moves:
                  - axis: relational_anchor_status
                    direction: up
                    magnitude: 1.0
                axes_held: []
                cost_ledger_anchor: cl-d06
                dialogue_anchor: true
                dialogue_citations:
                  - "wren-stitch-maker-flea-bottom-ward:1"
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s01n05
                flat_id: 5
                svo: "taylor-hebert-kl-122ac enters the south court"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: relational_anchor_status
                    rationale: "Taylor following Wren's direction is the physical enactment of the spoken exchange landing; the relational move is carried by n04; this bone grounds the follow-through as observable action"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s01n06
                flat_id: 6
                svo: "taylor-hebert-kl-122ac opens the coverage-notes entry"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "the coverage-notes are not the Jarvis channel; no delivery is authored; framework holds at current crack-level"
                  - axis: moral_legibility_to_self
                    rationale: "Taylor opening the entry runs the discipline correctly; the accounting runs cleanly here; legibility holds — crack does not deepen until s03"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s01n07
                flat_id: 7
                svo: "taylor-hebert-kl-122ac marks the contact-role field"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "writing 'ward-resident, Hook, routine' in the contact-role field is the protective discipline, not a delivery; framework holds"
                  - axis: relational_anchor_status
                    rationale: "post-move hold — the anchor moved at n04; this bone enacts the protective choice that weights it, but the axis does not move again in this scene"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s01n08
                flat_id: 8
                svo: "taylor-hebert-kl-122ac blanks the contact-source field"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: relational_anchor_status
                    rationale: "the blanking enacts the weight of the protective choice — Wren's name is the thing the field-entry would carry; the omission is authored, not absent; the relational move consolidated at n04 is given its weight here"
                  - axis: moral_framework
                    rationale: "the omission is protective; no delivery is completed; framework holds at current crack-level"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s01n09
                flat_id: 9
                svo: "taylor-hebert-kl-122ac closes the coverage-notes entry"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_legibility_to_self
                    rationale: "the accounting runs cleanly; Taylor closes the entry with full understanding of what the blank field means; legibility holds — the recognition is filed, not suppressed; crack does not deepen until the honest accounting precedes a delivery in s03"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}

          - slug: b01c06s02
            seq: 2
            status: planned
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              The Jarvis channel opens in the late-morning window, the standard routing time
              for non-urgent asks. [event: Jarvis delivers Otto's request — Black-faction ward
              elder names with Black-faction sympathies; names, not movement patterns; the
              distinction is explicit in the channel's phrasing; Otto is asking for persons,
              not behaviors]. Taylor reads the ask twice. The distinction in the phrasing is
              not accidental. Movement patterns are what she has been delivering since d04:
              who passes what junction, which passage goes unused, the clustering that precedes
              faction pressure. Names are different. Names are persons.

              [force: the ask's specificity — it does not ask for anything she does not already
              have; she has been reading the Flea Bottom wards for four months; the ward elders
              who carry Black-faction weight are legible in the feed's long-pattern record; she
              has not been reading them as names, she has been reading them as nodes in the
              ward-governance structure; the read is already done; what Otto is asking is for
              her to convert nodes to names]. [mechanism: the compilation process — Taylor does
              not deploy the feed new to answer this ask; she reads from coverage memory; the
              elders are in the record because they are ward-elder bodies in the wards she
              covers; their alignment is inferable from who they meet, which messages they
              receive, whose errands they run; the coverage architecture has been producing
              this answer for months without Taylor having named it as an answer; she is
              not doing new surveillance to compile the list; she is reading the surveillance
              she already did].

              [image: the ward elders as they appear in the feed's pattern record — not faces
              but bodies; not names but location-tendencies, meeting-frequencies, the specific
              quality of motion that marks a person who is receiving instruction from a
              direction other than the ward's formal governance structure; there are four of
              them in the Hook-adjacent wards whose pattern reads as Black-faction-adjacent;
              two of them Taylor is confident in; one she is sixty percent; one she is fifty-five
              and aware that the margin is thin]. [force: the list taking shape as a specific
              named set of persons — not a pattern, not a class, not a movement cluster; four
              names, four wards, four bodies she has been watching without naming; the naming
              is the step she is now taking]. She writes the names in the form the channel
              requires. Four names. The list is complete.

              [event: Taylor holds the compiled list without sending it — the send is pending;
              the accounting has not run yet; she is not in the habit of sending without
              running the accounting; the Wren exchange this morning sits in the coverage
              notes without a name in it; the list in her hand has four names in it; she
              has not noted the contrast yet; the contrast is there].

            substance_delta:
              axes_in_motion: []
              axes_held:
                - axis: moral_framework
                  rationale: "the list is compiled but not sent; no delivery is complete in this scene; the moral weight of the act lands at the send, not at the compile; the compilation is coverage-recall, which is inside the existing licensed exception; moral_framework holds at current crack-level"
                - axis: relational_anchor_status
                  rationale: "relational_anchor_status moved in s01; the compilation does not add further weight to the anchor; the list does not include Wren and the omission from s01 stands without new action this scene"
                - axis: moral_legibility_to_self
                  rationale: "the accounting has not run yet; Taylor notes the pending send and does not open the ledger on it mid-compilation; legibility holds until the accounting begins in s03"
                - axis: capability
                  rationale: "coverage-recall, not new feed deployment; capability holds at current rank; the compilation uses what has already been built"
                - axis: position-prot-rise
                  rationale: "the request arrives through Jarvis, not a new formalization event; Otto's ask is within the existing arrangement; position holds"
                - axis: political_register-prot
                  rationale: "the ask is from Otto through Jarvis; the ward elders are Flea Bottom-layer; no court-tier content in the compilation itself; resentment color is present from c05 but does not advance in the compilation register"
                - axis: social_tether-prot-rise
                  rationale: "the arrangement ask is within the existing tether structure; no new tether formation event; tether holds"
              density_target: 0.5-0.65
            scene_conflict:
              protagonist_force: "Taylor's operational precision — she can produce the list because her coverage architecture has been producing this answer for months; the feed knows these wards; she knows these wards; the compilation is clean, quick, and accurate"
              opposing_force: "the ask's specificity as a category-crossing — movement patterns are a class, names are persons; Otto has asked her to convert the coverage architecture's output from pattern-language to person-language; the conversion is what she has been not doing since d04; the compilation is the act of doing it, before the sending is the act of completing it"
              stakes_axis: moral_framework
            bones:
              - slug: b01c06s02n01
                flat_id: 10
                svo: "the jarvis-channel message arrives"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: position-prot-rise
                    rationale: "the request arrives through Jarvis, not a new formalization event; Otto's ask is within the existing arrangement; position holds"
                  - axis: political_register-prot
                    rationale: "the ask arrives through the Jarvis channel; the channel is Flea Bottom-layer routing, not a court-tier content shift; resentment color does not advance on the request's arrival"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s02n02
                flat_id: 11
                svo: "taylor-hebert-kl-122ac opens the jarvis-channel message"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "the list is compiled but not sent; no delivery is complete in this scene; moral_framework holds at current crack-level"
                  - axis: moral_legibility_to_self
                    rationale: "the accounting has not run yet; legibility holds until the accounting begins in s03"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s02n03
                flat_id: 12
                svo: "taylor-hebert-kl-122ac reopens the jarvis-channel message"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "re-engaging the ask enacts the weight of its specificity — names vs. movement patterns; framework holds because the list is not sent; the weight is not yet the breach"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s02n04
                flat_id: 13
                svo: "taylor-hebert-kl-122ac pulls the coverage-memory record"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: capability
                    rationale: "coverage-recall, not new feed deployment; capability holds at current rank; the compilation uses what has already been built"
                  - axis: moral_legibility_to_self
                    rationale: "pulling the coverage record is the compilation step before the accounting runs; legibility holds until s03"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s02n05
                flat_id: 14
                svo: "taylor-hebert-kl-122ac fills the jarvis-channel form"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "the list is compiled but not sent; the moral weight lands at the send, not the compile; the compilation is coverage-recall inside the existing licensed exception; framework holds"
                  - axis: capability
                    rationale: "the compilation uses the coverage architecture already in place; capability holds"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s02n06
                flat_id: 15
                svo: "taylor-hebert-kl-122ac lowers the jarvis-channel form"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "the send is pending; the accounting has not run yet; setting the form down without sending enacts the loaded pause that is this scene's function; framework holds"
                  - axis: relational_anchor_status
                    rationale: "the list does not include Wren; the omission from s01 stands without new action this scene; anchor holds at its post-s01 rank"
                  - axis: social_tether-prot-rise
                    rationale: "the arrangement ask is within the existing tether structure; no new addition; tether holds"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}

          - slug: b01c06s03
            seq: 3
            status: planned
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              She runs the accounting before she sends. This is the form: write the terms,
              run the balance, close the entry, act on the result. [event: Taylor opens the
              accounting explicitly — first arm: the names versus Sera's continued protection].
              Four names of Flea Bottom ward elders against one name she has never met whose
              continued standing in Alicent's household is the reason the arrangement exists.
              She runs this arm without embellishment. If the names go to Otto: he knows which
              ward elders in the Hook-adjacent wards carry Black-faction weight. That
              intelligence will be used for Green-faction ward governance, which means pressure
              on those elders, which means their ability to operate as Black-faction nodes in
              Flea Bottom is constrained. The cost to the elders is real. She does not inflate
              it; she does not minimize it.

              [force: the accounting's second arm — the harm from naming versus the harm from
              Sera's exposure]. If the names do not go: Jarvis routes back to Otto that the
              ask cannot be satisfied. The arrangement is not threatened immediately; Otto is
              not transactional at the single-delivery level. But the arrangement rests on
              her delivering what she can deliver, and she can deliver this. To not deliver
              it is to introduce a gap where there should not be one, and Otto is precise
              enough to notice the gap and to ask what it indicates. [image: Sera as she
              appears in the feed's Red Keep coverage — a fourteen-year-old ward of Alicent's
              household, moving through a corridor whose political temperature Taylor can read
              from the body-language of the people moving around her; exposed in ways Sera
              does not know she is exposed; the arrangement's purpose rendered in a specific
              small body in a specific corridor]. She runs the second arm.

              [event: the accounting is honest — both arms land with their full weight;
              Taylor does not find a way to close the entry without noting both the cost
              to the ward elders and the risk to Sera; the balance runs as stated; the
              accounting is complete and it arrives at delivery]. This is the form. This
              is the breach. [mechanism: the rationalize-each-trade pattern established —
              an honest accounting that arrives at delivery is the pattern now; the ledger
              is not failing; it is working correctly; it is producing the answer that
              the framework produces when the terms are as stated; what the accounting
              does not contain is a question about whether the framework itself is the
              problem; the ledger runs; the ledger is the instrument of the delivery as
              much as the mechanism of the check]. She does not sit with this. The
              accounting is closed.

              [event: Taylor sends the list — she writes the four names in the Jarvis
              channel's required form, marks the entry complete, and routes it; a Jarvis
              courier will move the information; the names are now in the arrangement's
              downstream; Taylor marks the names, the courier takes the list]. The entry
              closes. The ward-coverage notes remain in her working substrate. They contain
              an entry from this morning: blocked lane, south-court workaround, ward-resident
              contact, Hook, routine. The contact-source field reads: ward-resident. [image:
              the two entries as they sit in the record — the four-name list in the Jarvis
              channel, complete and dispatched; the single-line coverage note with a blank
              where a name is not]. The four names went. Wren's name did not go.
              She did not write it.

              [event: moral_framework -1.0 — the first named-person intelligence delivery
              completed after explicit accounting; the rationalize-each-trade pattern is on
              the books; cl-d06 cost side; the account is settled at -1.0 of the -1.0 total
              cost; the ledger is correct and the ledger has delivered the names].
              [event: moral_legibility_to_self +0.5 — the accounting was honest, which means
              the breach is legible; Taylor can read what she did and why; the crack deepens
              not from suppression but from precision; the rationalization ran correctly and
              produced a delivery, and that is now visible in the record as a class of thing
              she does; no cl anchor; +0.5 of +0.5 total chapter Δ].

            substance_delta:
              axes_in_motion:
                - axis: moral_framework
                  direction: down
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl-d06
                  notes: "first named-person intelligence delivery completed after explicit accounting; the accounting was honest and arrived at delivery; the rationalize-each-trade pattern is established and on the books; cl-d06 cost side; full -1.0 delivered in this scene; this chapter closes the moral_framework cost tranche of cl-d06"
                - axis: moral_legibility_to_self
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: null
                  notes: "the explicit accounting before sending is the legibility crack deepening; the rationalization ran correctly and produced a delivery, and Taylor can read that this is what happened; the honest accounting makes the breach more visible to the reader and slightly more visible to Taylor; +0.5 of +0.5 chapter total; no cl anchor"
              axes_held:
                - axis: relational_anchor_status
                  rationale: "relational_anchor_status moved in s01 (the Wren exchange + omission); s03 is the contrast moment — the four names went to Jarvis, Wren's name did not go; but the contrast is readable in the record without requiring a second Δ; the anchor account holds at its post-s01 rank through scene-close"
                - axis: capability
                  rationale: "the send uses the coverage architecture already in place; no new deployment; capability holds at current rank"
                - axis: position-prot-rise
                  rationale: "the delivery is within the existing arrangement; no new formalization event; position holds"
                - axis: political_register-prot
                  rationale: "the ward elders and the Flea Bottom layer carry no court-tier content that would activate the resentment register; the ask came from Otto through Jarvis but the content is Flea Bottom-level; political_register-prot holds at its current rank from b01c05"
                - axis: social_tether-prot-rise
                  rationale: "the delivery is within the existing tether structure; no new tether addition; tether holds"
              density_target: 0.65-0.8
            scene_conflict:
              protagonist_force: "the accounting discipline — Taylor runs the explicit ledger before acting; the discipline is real; she does not send without closing the entry; the form holds"
              opposing_force: "the accounting's honesty as the breach mechanism — the ledger runs correctly and arrives at delivery; there is no error in the accounting; the rationalize-each-trade pattern is the form the accounting takes when the framework is operating correctly with bad premises; the opposing force is not external pressure but the accounting's own correct output"
              stakes_axis: moral_framework
            bones:
              - slug: b01c06s03n01
                flat_id: 16
                svo: "taylor-hebert-kl-122ac opens the ledger-board"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "the accounting has not yet arrived at delivery; the ledger-board opens on the cost-side names; moral_framework holds at current crack-level pending completion"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s03n02
                flat_id: 17
                svo: "taylor-hebert-kl-122ac writes the ward-elder names"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "the ward-elder names are the cost-side write; framework holds — the delivery is not completed in this bone; writing the names is not the breach, it is the mechanism that makes the breach legible"
                  - axis: relational_anchor_status
                    rationale: "relational_anchor_status moved in s01; writing the ward-elder names does not add further weight to the anchor; the contrast between the four names and Wren's absent name is structurally present but does not move the axis"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s03n03
                flat_id: 18
                svo: "taylor-hebert-kl-122ac writes the sera-coverage entry"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "the sera-coverage entry is the exposure-side write; it runs without embellishment; the accounting is honest and not yet complete; framework holds pending the close"
                  - axis: political_register-prot
                    rationale: "Sera is the protect-target; the sera-coverage entry carries no court-tier content that activates the resentment register in the accounting itself; political_register-prot holds"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s03n04
                flat_id: 19
                svo: "taylor-hebert-kl-122ac marks the red-keep coverage record"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: capability
                    rationale: "the Red Keep coverage is the existing capability architecture; marking the record is coverage-recall, not new deployment; capability holds"
                  - axis: relational_anchor_status
                    rationale: "Sera's presence in the coverage record is the protection architecture's object; the relational anchor holds at its post-s01 rank; this bone enacts the distance of the protect-target without adding weight"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s03n11
                flat_id: 20   # inserted at Phase-3 transition-fix; Phase 7 reassigns all s03 flat_ids (former 20-25 shift to 21-26)
                svo: "taylor-hebert-kl-122ac stills the hand"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "the verdict-pause — the two completed ledger entries stand (the ward-elder names; the sera-coverage entry) and the accounting's own logic closes here; the hand stilling over the entries enacts the framework holding against the pressure to proceed at the moment it authorizes the send; the move fires at the seal (n06), not here; this held beat is the rise into the seal the climax requires (dramatist Phase-3 missing-transition fix; SVO recast holds->stills per Phase-6 auditor fault-001 narrow-holds-license)"
                cost_ledger_anchor: null
                dialogue_anchor: false
              - slug: b01c06s03n05
                flat_id: 21
                svo: "taylor-hebert-kl-122ac closes the ledger-board"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "the accounting runs as stated; both writes have landed; moral_framework holds at this bone — the move fires at the seal (n06), not at the ledger-board close; the ledger-board closing IS the moment the breach becomes inevitable"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s03n10
                flat_id: 22
                svo: "taylor-hebert-kl-122ac lifts the jarvis-channel form"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "deliberation complete; the accounting's verdict has converted to act; the framework holds at this bone — the move fires on the seal at n06, not here; lifting the form is the close→act hinge that makes the causation of the breach visible (write names → close ledger-board → lift form → seal)"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s03n06
                flat_id: 23
                svo: "taylor-hebert-kl-122ac seals the jarvis-channel form"
                shape: moving
                axis_moves:
                  - axis: moral_framework
                    direction: down
                    magnitude: 1.0
                axes_held: []
                cost_ledger_anchor: cl-d06
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s03n07
                flat_id: 24
                svo: "the courier takes the jarvis-channel form"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_framework
                    rationale: "post-move hold — moral_framework moved at n06; the courier taking the form is the physical completion of the send; the axis holds at its new rank"
                  - axis: social_tether-prot-rise
                    rationale: "the delivery is within the existing tether structure; no new tether formation event; tether holds"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s03n08
                flat_id: 25
                svo: "taylor-hebert-kl-122ac opens the ward-coverage notes"
                shape: moving
                axis_moves:
                  - axis: moral_legibility_to_self
                    direction: up
                    magnitude: 1.0
                axes_held: []
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}
              - slug: b01c06s03n09
                flat_id: 26
                svo: "taylor-hebert-kl-122ac closes the ward-coverage notes"
                shape: held
                axis_moves: []
                axes_held:
                  - axis: moral_legibility_to_self
                    rationale: "post-move hold — moral_legibility moved at n08; closing the notes is the physical completion of the contrast-moment; the crack deepens not from suppression but from the precision with which both substrates sit complete in the record"
                  - axis: position-prot-rise
                    rationale: "the delivery is within the existing arrangement; no new formalization event; position holds"
                cost_ledger_anchor: null
                dialogue_anchor: false
                gate_verdict: {bonefide: true, flat: false}

      - slug: b01c07
        context_followability:
          completeness_verdict: FOLLOWABLE   # Phase 4.5: NI:1@13 why-she-stays survived R2 -> unconditionally CLOSED; no new FOLLOW-GAP
          readability_verdict: AIRLESS-HOLE  # Phase 4.5: grd-001@16 + grd-002@22 still airless post-R2 -> Phase 4.6 fires
          report_path: active-project/staff/reviews/context-follow-r2-b01-c07-20260531T024855Z.md
          reviewed_at: 2026-05-31
          context_ledger_open: 0
          grounding_ledger_open: 0   # Phase 4.6: both satisfied via sensory:3@16 + sensory:4@22 grounding adds
          phase_4_6:
            fired: true
            grounding_adds: [sensory:3@16, sensory:4@22]
            final_verdict: FOLLOWABLE   # Step 2 re-check: both airless holes CLOSED; @15/@22 posture-echo broken; 13-22 breathes end-to-end; no fixer pass
            report_path: active-project/staff/reviews/context-follow-r3-b01-c07-20260531T025714Z.md
        facets_audience_gate:
          cycle_1:
            verdict: FAIL   # 7 PASS / 4 FAIL (3-of-3 strict). report: active-project/staff/audience/facets-audience-gate-r1.md
            earth_bet_fence: CLEAN
            failed_facets:
              - "interest-narrator (cape-fic REVISE: AP-001 cap; recast narrator:3@15, keep narrator:4@19 WATCH-1)"
              - "sensory (old-state-reader + disambiguation-pedant REVISE: sensory:1@12 unanchored sound old-state; sensory:2@17 sustained-as-inflection+unanchored; sensory:4@22 grd-002 grounding real but recast to discrete proprioceptive/sound not cumulative-thermal)"
              - "dialogue-halvard (cape-fic REVISE :1@12 aphorism-strain; dark-fantasy DEFENDED + worm-canon ACCEPT -> defense-or-revise; utterance-only, no bones change)"
              - "dialogue-taylor (dark-fantasy + worm-canon CONVERGENT REVISE :1@19: 'She's why I'm in Flea Bottom at all' = self-justification breaks no-winner invariant; close on 'first name in the count'; utterance-only)"
            passing_facets: [memory, feeling, metaphor, vibes, exposition, location-state, state-updates]
          cycle_2:
            verdict: PASS   # all 4 re-fired facets 3-of-3 ACCEPT; report: active-project/staff/audience/facets-audience-gate-r2.md
            re_audit: CLEAN  # Phase 5 cycle-2 confirm HARD=0 (fault-016 proprioceptive->pressure, fault-017 grd-002 satisfied_by synced)
            closed: ["interest-narrator AP-001 cap", "sensory:1@12 anchor + :2@17 old-state + :4@22 thermal->pressure recast", "dialogue-halvard aphorism-strain", "dialogue-taylor self-justification closer"]
            cycles_used: 2 of 3
        status: stitched   # /and-stitch b01c07 COMPLETE: draft/b01-c07.md TERMINAL (Phase 9 cold-read PASS-WITH-CAVEATS: READABLE PASS / AIRLESS ALIVE / MUFFLE CONCRETE / CONTINUE barely-yes). Optional depth-pass parked (pl-2026-05-31-001). was audited-r1 after /and-facets COMPLETE: Phase 5 audit CLEAN (HARD=0) + Phase 5b audience-gate PASS (3-of-3 all facets, 2 cycles). Earth-Bet fence CLEAN. Was audited-r1-mechanical; before that Phase 5 audit CLEAN (HARD=0, 14 SIGNAL/3 TASTE); fault-008 NI-unreadable was an agent glitch (file intact, AP-001 manually clear); Phase 5b cleared. was faceted-r2 after Phase 4 merge+consolidate clean (R2: 1 DELETE mem:1@6, rest KEEP); scene-map 4d PASS; was faceted-r1 after Phase 2 (47 facet entries, 84% decorated); was bones-written after /and-write COMPLETE (2026-05-30): Phase 6 bone-gate PASS on rev2 (after 3 attempts; DEC-0051/0052); Phase 7 emit done
        bones_file: theater/bones/b01-c07.md
        bones_count: 25
        substance_bone_gate_verdict: PASS
        # /and-write b01c07 (2026-05-30): 3-attempt bone-gate battle on an ARGUMENT chapter.
        #   attempt 1 (38 bones): FAIL 6 HARD (4 argument-spine interiority bones). Phase 6.5 admin -> PROP-0024 (DEC-0051): gate working; Phase-1 brief lacks argument-spine concrete-SVO constraint.
        #   attempt 2 (rev1: 8 audience-deletes + recast): FAIL WORSE 7 HARD (recasts used holds-on-abstraction / multi-subject / modifiers).
        #   attempt 3 (rev2: 2 moving recasts to physical-verb forms 'faces'/'stays' + 5 interior DELETES -> NI facets + 1 modifier strip; DEC-0052 constrained, 1-attempt cap): PASS, HARD=0. 38->25 bones.
        #   Resolution validates the discriminator: physical-observable VERB witnesses the axis (not abstraction-object); delete-over-invent for interiority (sept-corner conversation has no ledger/prop to ground argument-beats); interior readings -> narrator-interest facets. Abstraction-dominance 100/100/100% post-fix. Aggregation EXACT (pol-reg +0.5, soc-tether +1.0).
        # Reports: write-b01c07-bonegate{,-r2,-r3}.md. Full per-bone substance_delta + event_map + NI-facet-handoff notes: _drafts/b01c07-bones-draft-2026-05-30-rev2.md (canonical per-bone source until scenes[].bones[] persist; bones file is flattened SVO source).
        dialogue_files: [theater/dialogue/septon-halvard-flea-bottom.md, theater/dialogue/taylor-hebert-kl-122ac.md]
        dialogue_citations:   # anchors realigned post-rev2 renumber
          - "b01c07s02n04 (flat 12) -> [septon-halvard-flea-bottom:1]  (compound-corruption thesis via the errand-man)"
          - "b01c07s03n02 (flat 19) -> [taylor-hebert-kl-122ac:1]      (Wenna Cobb counter; WATCH-1 concrete: name+street+failure-mechanism)"
          - "b01c07s03n04 (flat 21) -> [septon-halvard-flea-bottom:2]  (cost-acknowledgment; no retraction)"
        scene_map_file: theater/facets/scene-map-b01-c07.md
        bones_review:   # /and-review bones b01c07 (2026-05-30) — MANDATORY gate between /and-write and /and-facets
          reviewed_at: 2026-05-30
          report_path: active-project/staff/reviews/bones-b01c07-2026-05-30.md
          verdict: PASS-WITH-NOTES   # after rev3 form-fix + re-fire. (History: run-1 FAIL 3 HARD SVO-form on flat 15/16/22; /and-write revise recast them; re-fire 2026-05-30 = PASS-WITH-NOTES 0 HARD. NOTE: a premature record/commit 6e6f0f6 wrongly said PASS before the auditor fork returned — corrected at 6a81abb.)
          run_history:
            - "run-1 (commit 6a81abb): FAIL 3 HARD — fault-001 flat15 'stays in the argument' (PP+abstraction), fault-002 flat22 'stays at the sept-corner' (PP-of-place), fault-003 flat16 'holds the silence' (abstraction-object)"
            - "revise (commit 4cdf489): recast flat15->'plants the feet', flat16->'exhales', flat22->'steadies the feet'"
            - "re-fire: PASS-WITH-NOTES 0 HARD — all 3 SVO-clean; aggregation EXACT (pol-reg +0.5, soc-tether +1.0); /and-facets CLEARED"
          fidelity: PASS   # the 5 rev2 deletes did NOT hollow the spine; it lives in dialogue bones 12/19/21.
          follow_check: PASS-WITH-NOTES   # PROP-0020: central event + scene hand-offs recoverable; gap context-addable (NI facet), NOT bone-structural → not a FOLLOW-FAIL
          aliveness: BONES-AIRLESS-RISK   # PROP-0022 (advisory): span bones 13-22; interiority routed off-page, one sensory anchor (bone 17) across ten bones. Forewarns /and-facets Phase 2.5 grounding-ledger + /and-stitch Phase 4 voice-embodiment.
          bones_file_mtime_at_review: 1780181317   # post-recast mtime; re-fire reviewed the recast bones file
          stale_since: null
          gate_outcome: CLEARS_FACETS   # re-fire PASS-WITH-NOTES, follow_check not FOLLOW-FAIL → /and-facets b01c07 cleared to dispatch
          forward_notes:   # carry to /and-facets Phase 2.5 + NI author brief
            - "NI facet at bones 13/15 is LOAD-BEARING: must stage crooked-house-maps-onto-her-arrangement recognition or cold-read causality gap reopens at stitch."
            - "SUBSTANCE-SUSPECT (re-fire SIGNAL): flat 15 'plants the feet' + flat 22 'steadies the feet' are form-clean but the soc-tether +0.5 Δ is partially DISPLACED onto the NI facet — the body-rooting witnesses physical bracing; NI must render it as socially LEGIBLE (Halvard reads it; Taylor reads herself in it) or the relational Δ goes unearned at stitch."
            - "NEAR-DUPLICATE (re-fire SIGNAL): flat 15 'plants the feet' / flat 22 'steadies the feet' share a body-part/posture register; NI + sensory facets must differentiate the two beats to prevent repetition-compression at stitch."
            - "Open grounding-ledger lines for the bones 13-22 airless span."
            - "7 interior readings transferred to NI — treat all 7 as explicit deliverables (PASS-CHUNK-VOICE-RISK)."
        write_margit_referrals_open:
          - "oc-sept-corner.card.md — NEW location (the sept corner / chandler's storehouse, Flea Bottom Hook); first-touched c07; loc card MUST be authored before /and-facets b01c07 Phase 0 (locations: resolution gate). Same class as c06 oc-* SEAMs."
        chunk: |
          A breathing chapter: Taylor consolidates the ledger without a new major breach.
          She has been running the arrangement for two months and the accounting has become
          routine. The structural work here is Halvard. He finds her at the sept — not
          confrontation, encounter — and in the course of a working conversation about a sick
          child in the Hook he names, without knowing it applies to her, the principled-slower
          argument: that working within a corrupt structure compounds the corruption at the rate
          of the corruption, and that the slower method of refusing to participate costs more
          upfront and less in the end. Taylor engages the argument genuinely. She has a
          counter: the slower method has a body count she can name, and she can name the body
          that prompted her here. Halvard does not have a sufficient answer. The chapter ends
          without resolution. What shifts: political_register-prot advances slightly as the
          Halvard encounter forces Taylor to articulate what the resentment is toward; the
          counter-argument is genuinely engaged and genuinely not resolved.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: political_register-prot
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "Halvard encounter forces articulation of resentment's object; not yet named-contempt but the register sharpens; sub-advance"
            - axis: social_tether-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: null
              notes: "Halvard is a Flea Bottom precinct node; genuinely engaging him deepens Taylor's precinct social embedding; the encounter consolidates the tether substrate even without resolution"
          axes_held:
            - axis: moral_framework
              rationale: "no new breach; ledger-consolidation chapter; rationalization stable"
            - axis: capability
              rationale: "no new expansion; coverage maintenance"
            - axis: relational_anchor_status
              rationale: "Wren in coverage; no new weight; anchor holds at rank 3"
            - axis: moral_legibility_to_self
              rationale: "counter-argument genuinely engaged means Taylor's legibility is working; but resolution is deferred, not advanced"
          density_target: 0.5-0.7
          chapter_class: standard
        dramatic_shape: hinge
        goal: |
          Show the audience the Halvard argument at genuine engagement — neither dismissed nor won — so when Taylor stops engaging it at d09 the foreclosure reads as a choice, not a lapse.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "rationalize-each-trade pattern: established"
            - "Wren: in coverage map; spoken-contact; omitted from deliverable; anchor rank 3"
            - "moral_legibility crack: deeper; accounting honest"
            - "Black-faction elder list: delivered; consequences pending"
            - "cf-d10-courier-face: courier in memory"
          world_state:
            - "KL 122 AC; arrangement two months functional; Green consolidation advancing"
          character_state:
            - "Taylor: moral_framework rank 0; relational_anchor rank 3; moral_legibility rank 5; political_register-prot rank 2.5"
            - "Halvard: present in Flea Bottom; counter-argument latent but not yet engaged"
          source_chapter: b01c06
        handoff_out:
          open_threads:
            - "Halvard counter-argument: first genuine engagement; not resolved; Taylor has a counter she believes"
            - "rationalize-each-trade pattern: continuing; ledger consolidated"
            - "Wren: in coverage map; anchor rank 3"
            - "cf-d10-courier-face: courier in memory"
            - "Black-faction elder list consequences: pending"
          world_state:
            - "KL 122 AC; arrangement stable; Halvard's presence in Taylor's awareness newly active"
          character_state:
            - "Taylor: moral_framework rank 0; political_register-prot rank 3 (register sharpened by Halvard articulation demand); relational_anchor rank 3; moral_legibility rank 5"
            - "Halvard: counter-argument genuinely engaged; not resolved; will return"
          target_chapter: b01c08
        chunk_cold_read:
          reviewed_at: 2026-05-30
          verdict: PASS-CHUNK-VOICE-RISK   # PROP-0019 / PROP-0019-A; summary maps to goal + CONTINUE barely-yes -> PASS-CHUNK family; Step 2.5 Signal B fires (central content is a discursive argument; named-death is the lone concrete anchor, flagged thin)
          recovered_summary: "A woman running a morally-compromised arrangement overhears a man unknowingly argue against exactly what she does, weighs it, names the dead that justify her, and walks off without either conceding."
          continue: marginal-yes   # "barely yes — on the strength of the named dead body"
          continue_strict: marginal-yes
          report_path: active-project/staff/reviews/chunk-coldread-b01c07-2026-05-30.md
          disposition: PASS-CHUNK-VOICE-RISK proceeds to Phase 6 automatically (non-blocking; no admin disposition — summary maps + continue yes; dramatist+auditor+audience all ACCEPTED structure)
          voice_risk:
            triggered: true
            central_event: "the Halvard principled-slower argument + Taylor's counter (naming the specific body that prompted the arrangement)"
            signals: ["central 'event' is a discursive argument at seminar-risk", "the one concrete anchor (the named death) read as thin — the lone thing holding CONTINUE", "low present jeopardy on a non-coda (hinge) chapter", "PAYOFF read as position-statement-not-turn (design-inherent for a d09-planting hinge)"]
            note: "Arms /and-stitch Phase 8.5 central-event-muffle check + Phase 9 jeopardy scrutiny. The low-event/low-jeopardy is partly design-inherent (breathing/argument chapter) but the named-death anchor MUST land concrete or the chapter reads as a seminar."
          cold_read_risk_carry: |
            CAUSALITY gap (Class-A, actionable at /and-write): the reader could not tell WHY Taylor stays in
            the conversation — s02 twice says "she could move; she does not" without a motivating cause. The
            engagement is asserted, not caused. /and-write must motivate why the argument grips her (audience
            WATCH-2: the thesis must get through / land somewhere she can feel it BEFORE she picks up the counter).
            Design-inherent (carry as risk, not defect): low present jeopardy + no-turn payoff are legitimate
            for a breathing hinge that plants the d09 foreclosure — but the chapter leans entirely on the
            named-death beat, which must be concrete (audience WATCH-1).
        scenes:
          - slug: b01c07s01
            seq: 1
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Two months in, the accounting is [image: ledger-as-wallpaper] — routine, no longer a moral
              event, just the form the arrangement takes on a given day. Taylor moves through the Hook
              ward-coverage circuit: three wards, the courier-route pass, the Rushwick margin. The insect-feed
              runs at its usual low-profile density and returns nothing unusual. The work [mechanism:
              consolidation-as-normalization] is holding. At the sept corner — the chandler's storehouse that
              doubles as Halvard's fixed point on holy days and most other days — Taylor pauses because a man
              is blocking the passage with a handcart of bundled rags and Halvard [force: halvard-as-precinct-node]
              is already there, already talking to the handcart man about someone on the Lane who is running a
              fever that will not break. The blocking is accidental; [event: halt-and-contact] the contact is not.
              Taylor waits out the handcart. Halvard sees her waiting. He does not try to categorize what she is
              doing here; [image: halvard-not-categorizing] he extends the same plain acknowledgment he extends
              to anyone present in a space he occupies. He names the sick child — Derry, seven years old, the
              bone-setter's ward — [event: sick-child-named] as though Taylor's being here is ordinary and not
              requiring explanation. She does not correct the assumption. The insect-feed [mechanism:
              passive-radar-placing-halvard] has had Halvard in its peripheral register since the first week;
              she knows his circuit; she has not thought about what that means. She does not think about it now.
            scene_conflict:
              protagonist_force: "Taylor's ledger-discipline — the two-month consolidation pattern; the accounting that has made the arrangement ordinary"
              opposing_force: "Halvard's plain-contact register — the presence that does not require explanation or categorization; an ordinary social physics Taylor's surveillance architecture is not designed to absorb"
              stakes_axis: social_tether-prot-rise   # NOTE (auditor flag fault-009): held axis this scene; conflict-frame label, NOT an authoring mandate — /and-write Phase 1 must not read as Δ-required (legal per Phase-3 union rule)
            substance_delta:
              axes_in_motion: []
              axes_held:
                - axis: political_register-prot
                  rationale: "sick-child introduction is Flea Bottom-layer content; no court-tier material; articulation-demand requires Halvard to name the argument first, which is s02"
                - axis: social_tether-prot-rise
                  rationale: "contact established here but tether-deepening event is the genuine engagement in s02/s03; holds at rank 3 through scene-close"
                - axis: moral_framework
                  rationale: "consolidation-mode; no new breach; holds at rank 0"
                - axis: moral_legibility_to_self
                  rationale: "the passive-radar note on Halvard is a texture beat, not a legibility event; holds at rank 5"
                - axis: relational_anchor_status
                  rationale: "Wren in coverage; no new weight; holds at rank 3"
                - axis: capability
                  rationale: "maintenance coverage; no new deployment"
              density_target: 0.4-0.55
          - slug: b01c07s02
            seq: 2
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Halvard [force: halvard-as-principled-slower] has not left the conversation. He is describing what
              the fever does to a seven-year-old — the specific physical progress of it, the bone-setter's
              inability to source the right herbs, what a maester's visit would cost and why that cost cannot be
              met — in a register that is neither complaint nor appeal but plain accounting of a situation. Taylor
              is still there. [event: taylor-stays-in-conversation] She could move; she does not. The insect-feed
              registers nothing actionable in the immediate radius and the circuit can hold for a few minutes.
              Halvard shifts — not abruptly — from the sick child to a question about a man further up the Lane,
              someone who has been running errands for a household that pays him in kind rather than coin, and in
              unpacking why this seems wrong to him, Halvard arrives at the [mechanism:
              principled-slower-thesis-as-incidental] thesis without announcing it as a thesis: that [event:
              argument-named-without-application] participating in a corrupt arrangement — even in the service of
              mitigation, even when the mitigation is real — compounds the corruption at the rate of the
              corruption. Not as fast; not more. At the rate. The slower method costs more up front because it
              refuses the efficiency of the arrangement. It costs less in the end because [image:
              corruption-as-compound-interest] the interest does not accumulate. He does not know he is describing
              Taylor's arrangement. He is describing the Lane man's. Taylor [force: taylor-genuine-engagement]
              does not move away from this. She stays in it. [event: taylor-does-not-dismiss] The argument is not
              wrong in its own terms. She can feel the exact place where her ledger would rebut it and she does
              not produce the rebuttal yet — she turns the thesis over, reads it for structural soundness, notices
              where it holds and where it does not hold. The exchange [mechanism: engagement-without-resolution]
              is not performance; it is the kind of working-through that happens when you take something
              seriously. Halvard notices she is taking it seriously. He does not press. [image:
              halvard-allowing-the-silence] The silence works.
            scene_conflict:
              protagonist_force: "Taylor's genuine engagement — the argument is structurally sound in its own terms; she cannot dismiss it without cost; the ledger-discipline that requires honest accounting of an opposing position"
              opposing_force: "Halvard's principled-slower thesis — named incidentally, without knowing it applies; the compound-corruption mechanism; the slower method as an available road Taylor did not take"
              stakes_axis: political_register-prot
            substance_delta:
              axes_in_motion:
                - axis: political_register-prot
                  direction: up
                  target_delta_magnitude: 0.3
                  cost_ledger_anchor: null
                  notes: "taking the compound-corruption thesis seriously requires locating its object in the actual arrangement; the resentment color from d05 acquires a partial structural frame; +0.3 of the chapter's +0.5"
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: null
                  notes: "genuine engagement in an unstructured working conversation — not a transaction, not a function — deepens the social embedding; +0.5 of the chapter's +1.0"
              axes_held:
                - axis: moral_framework
                  rationale: "evaluative not actional; no new breach; holds at rank 0"
                - axis: moral_legibility_to_self
                  rationale: "taking the argument seriously is legibility working, but resolution deferred; holds at rank 5"
                - axis: relational_anchor_status
                  rationale: "no new weight; holds at rank 3"
                - axis: capability
                  rationale: "no new deployment"
              density_target: 0.55-0.7
          - slug: b01c07s03
            seq: 3
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Taylor [force: taylor-counter-deployed] names the body count. Not as a rhetorical move — she does
              not perform this — but because the argument requires it: if the slower method is the correct
              account, the correct account must include what the slower method costs in the interval before the
              interest stops accumulating. She knows the number for the Hook ward alone: [event: body-count-named]
              the fever season two years back, before anyone with her specific kind of coverage was present to
              route the maester-call that saved the bone-setter's previous ward. She can name [mechanism:
              specific-body-as-evidence] the body that prompted her to be here at all — not the category, the
              person; [image: named-death-as-ledger-entry] a specific name in a specific street, someone who died
              in the interval while the slower method held its principles intact. Halvard [force:
              halvard-without-sufficient-answer] does not have an answer for this that closes the question. He has
              an answer of a kind: [event: halvard-acknowledges-cost] he knows the slower method has a body count;
              he has not resolved the cost; he has decided not to endorse the faster method because the interest
              accumulates and he cannot see where it stops. He is telling her this honestly. He is not telling her
              she is wrong. He is telling her the cost he has decided to pay. [image: two-accountings-in-parallel]
              Taylor's counter does not win. Halvard's thesis does not win. [event: unresolved-close] The chapter
              ends with both accountings sitting in the space between them, structurally intact and mutually
              undefeated. Taylor leaves the corner first. [mechanism: foreclosure-planted-not-enacted] The argument
              is available to her. She has not foreclosed it. The foreclosure that happens at d09 will be a choice,
              readable as a choice, because this moment will have happened and she will have known what she was
              stepping away from.
            scene_conflict:
              protagonist_force: "Taylor's counter-argument — the specific body count; the named death that prompted the arrangement; the honest accounting of what the slower method costs in real time"
              opposing_force: "Halvard's sustained thesis — he names the cost of the slower method honestly and does not retract; the compound-corruption mechanism holds even without a sufficient answer to the body count; the argument remains structurally available"
              stakes_axis: social_tether-prot-rise
            substance_delta:
              axes_in_motion:
                - axis: political_register-prot
                  direction: up
                  target_delta_magnitude: 0.2
                  cost_ledger_anchor: null
                  notes: "naming the body count requires locating the source of resentment in specific structural failures of the slower method; the register sharpens to: resentment toward the arrangement that produced the named death AND toward the framework that would ask her to repeat the cost; +0.2 completing the chapter's +0.5"
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: null
                  notes: "completing the argument rather than closing it — both parties inhabit the exchange without transaction — is the social embedding event; the precinct tether deepens at the precinct-node level; +0.5 completing the chapter's +1.0"
              axes_held:
                - axis: moral_framework
                  rationale: "the counter deploys Taylor's existing rationalization honestly; no new breach; holds at rank 0"
                - axis: moral_legibility_to_self
                  rationale: "resolution DEFERRED per chapter contract; genuine engagement = legibility working, not advancing; holds at rank 5"
                - axis: relational_anchor_status
                  rationale: "Wren not in this scene's content; holds at rank 3"
                - axis: capability
                  rationale: "no deployment; holds"
              density_target: 0.5-0.65

      - slug: b01c08
        status: stitched-with-caveats   # /and-stitch b01c08 REVISE Phase 9 (2026-05-31T22:00:00Z): SHIPPED-WITH-CAVEATS per Phase 9 Step 4 matching-complaint rule. /and-write revise --from-signals added 4 companion body-act bones (@7 holds junction-stone / @10 exhales held-shoulder / @16 sets stylus down / @23 courier-figure stands at oswyn's shoulder / @26 slows the step) + recast @5 (lowers eyes) per PROP-0030/DEC-0061; bones 24→29. Staging review v2: ALL 5 PRIOR SPINE-PROMOTION FINDINGS CLOSED (finding-002 @6 STAGE / finding-004 @15 GROUND / finding-005 @18 NEEDS-BEAT / finding-006 @24 GROUND / finding-007 @25 STAGE — all CLOSED via new companion body-act bones); 3 new SIGNAL fixed inline (POV-pronoun + tense + paragraph-isolation at @18). Cold-read v2 CONTINUE=no but complaint shifted to apparatus-vocabulary-inaccessibility-to-chapter-8-cold-readers — matches chunk_cold_read.cold_read_risk_carry verbatim ("Opaque interiority — physical events present but buried under undefined jargon... no causal spine between scenes, ending gestures rather than lands"). chunk_cold_read.verdict=SHIPPED-WITH-RISK-RECORDED + DEC-0060 disposition P + matching-complaint pattern + staging-review-v2 PASS → SHIPPED-WITH-CAVEATS auto-promotion per Phase 9 Step 4. Caveats: (1) Cold-read CONTINUE=no matches pre-disposed Class B; (2) Apparatus-vocabulary inaccessibility structural (ch 8 of series); (3) Readability axis remains AIRLESS-leaning per PROP-0022 separated-scoring — body-content additions did NOT lift CONTINUE to tentative-yes (design-inherent per chunk_cold_read). Was stitch-failed-cold-read → /and-stitch b01c08 Phase 9 FAIL (2026-05-31T21:00:00Z): cold-read CONTINUE=no AIRLESS + staging-review STAGE on @6 sole axis-move central-event bone (URI-STITCH-SPINE-STAGING unconditional FAIL); Phase 8.5 coherence PASS (substance-aware) but cold-read AIRLESS-on-central-event triggers separated-scoring FAIL per PROP-0022. Cold-read complaint MATCHED chunk_cold_read.cold_read_risk_carry verbatim ("two names logged + a wider coverage map" → "two thin beats, no identifiable narrator") — would have SHIPPED-WITH-CAVEATS via Class B pre-disposition (DEC-0060) but staging-review spine-promotion FAIL is INDEPENDENT (an un-staged central event is decomposition defect even when cold-reader limped past). Route: /and-write b01c08 revise (--from-signals consumes the 4 spine-promotion findings: @6 STAGE central-event axis-move + @13 GROUND held central-event + @15 NEEDS-BEAT held stakes-axis peak + @20 GROUND courier-figure body-anchor). Cascade halted at /and-stitch per Phase 9 routing. Was audited-r1 → /and-facets b01c08 COMPLETE (2026-05-31): 9 facet files + dialogue + scene-map authored; 37 entries (loc-state 6, NI 6, sensory 2, state 11, memory 2, feeling 3, metaphor 0, vibes 5, exposition 2); proto-lines 14/24 decorated (58.3%). Phase 5 cycle 3 audit CLEAN (0 HARD / 5 SIGNAL). Phase 5b cycle 2 ALL 10 FACETS ACCEPT 3/3 strict aggregate (4 cycle-1 REVISEs — NI cape-fic / sensory old-state / vibes worm-canon / feeling dark-fantasy — remediated via NI:3+NI:6 reform, loc-state:4 sensory anchor, actor file keyword hyphenation, feel:2+feel:3 positive-form reform; all Phase 2.5 INVIOLABLES preserved). Bidirectional loop: one-sided (auditor caught 5 consolidation-renumbering HARDs cycle 1; audience caught 4 form/anchor/redundancy REVISEs; no shared findings). Audience cycles 2/3 (cap not burned).
                          # Was bones-written → /and-write b01c08 COMPLETE (2026-05-31): bones emitted theater/bones/b01-c08.md (24 bones / 3 scenes); scene-map facet emitted theater/facets/scene-map-b01-c08.md; dialogue file theater/dialogue/oswyn-mudway-flea-bottom-elder.md. Phase 6 bone-gate: 3-of-3 audience SUBSTANCE-FELT (cape-fic / dark-fantasy / worm-canon); Earth-Bet CLEAN; auditor 5 HARD all remediated (4 HELD-AXIS-WITNESSED via bone-level axes_held annotation + 1 dialogue-anchor citation fix s03n07→s03n05). Phase 4 trim: dropped s02n03 (single-persona-advisory; cape-fic ADVISORY-2 repeat from /and-substance Phase 5). Phase 3 dramatist: s02 n07↔n08 reorder (edge-image closes scene). Phase 2 auditor: 1 HARD fault-001 (sub-1.0 bone-floor); admin DEC-0002 override-as-precedent (c07 precedent: 4 sub-1.0 bone magnitudes shipped clean); pl-2026-05-31-003 SOFT for schema formalization at /and-review pipeline. Was scened from /and-substance chapter b01c08 (2026-05-31): SUBSTANCE-FELT 3/3 audience + dramatist ACCEPT + auditor PASS. Phase 5.5: CHUNK-CLASS-B → admin disposition P (DEC-0060). cl-d06 +1.0 relational_anchor_status DEFERRED to c09/c10 (pl-2026-05-30-001).
        bones_file: theater/bones/b01-c08.md
        bones_count: 24
        substance_bone_gate_verdict: PASS
        facets_path: active-project/theater/facets/
        round_1_complete: true
        round_2_complete: true
        audit_path: active-project/staff/auditor/facets-final-audit.md
        audit_complete: true
        audit_findings: 5  # SIGNAL; 0 HARD
        audience_gate_path: active-project/staff/auditor/facets-audience-gate-r2.md
        audience_gate_complete: true
        audience_gate_cycles: 2
        audience_gate_cap_burned: false
        bidirectional_loop: one-sided   # auditor and audience both fired substantive findings with no overlap (auditor: consolidation renumbering; audience: form/anchor/redundancy)
        context_followability:
          completeness_verdict: PASS    # Phase 2.5 + 4.5 both FOLLOWABLE
          readability_verdict: PASS     # Phase 2.5 + 4.5 both ALIVE
          context_ledger_open: 0
          grounding_ledger_open: 0
          report_paths:
            - active-project/staff/reviews/context-follow-r1-b01-c08-20260531T180000Z.md
            - active-project/staff/reviews/context-follow-r2-b01-c08-20260531T190000Z.md
        bones_review:
          reviewed_at: 2026-05-31T18:50:00Z
          report_path: active-project/staff/reviews/bones-b01-c08-2026-05-31.md
          verdict: PASS
          follow_check: PASS
          bones_file_mtime_at_review: 2026-05-31T17:12:10Z
          aliveness: clean
          stale_since: null
        cold_read:
          reviewed_at: 2026-05-31T21:00:00Z
          verdict: FAIL
          fail_basis:
            - "staging-review spine-promotion FAIL: STAGE on @6 (sole axis-move central-event bone; URI-STITCH-SPINE-STAGING — un-staged central event = decomposition defect; INDEPENDENT of cold-read leg)"
            - "cold-read CONTINUE=no AIRLESS — readability axis fails per PROP-0022 separated-scoring; AIRLESS-on-central-event escalates to FAIL"
          recovered_summary: "a packet arrives and is read; a courier is named, watcher-boy later gone"
          intended_goal: "Plant the courier face, activate the Aemond-adjacent pressure at low intensity, and stage the Oswyn-integration echo so that later Khepri-repetition accusations have been building in the reader's view long before Taylor's."
          summary_maps_to_goal: true   # cold reader recovered all three obligations
          continue: no                  # Q5 first-pass
          continue_strict: no
          report_path: active-project/staff/reviews/coldread-b01-c08-20260531T210000Z.md
          staging_signals: 8
          staging_report_path: active-project/staff/reviews/staging-b01-c08-20260531T210000Z.md
          spine_promotion_findings:
            - id: finding-002
              bone: "@6"
              verb: STAGE
              class: axis-move
              severity: FAIL-CLASS
              rationale: "Taylor's body absent during sightline-trace; integration reads as data-receptions, not physical act"
            - id: finding-004
              bone: "@13"
              verb: GROUND
              class: held-central-event
              severity: BLOCKING-QUALIFIED
              rationale: "one-clause body-detail within held-register fence; resolvable in revise"
            - id: finding-005
              bone: "@15"
              verb: NEEDS-BEAT
              class: held-stakes-axis
              severity: BLOCKING
              rationale: "acquisition-to-filing move skips somatic beat; held-discipline announced not enacted"
            - id: finding-006
              bone: "@20"
              verb: GROUND
              class: central-event-dialogue-anchor
              severity: BLOCKING-QUALIFIED
              rationale: "courier-figure has no physical body-register at approach; @21 face-plant unanchored"
          signal_clusters:
            - pattern: spine-staging-gap
              count: 4
              bone_ids: ["@6", "@13", "@15", "@20"]
              trigger: spine-staging-gap>=1
            - pattern: peak-zone-staging-gap
              count: 4
              bone_ids: ["@6", "@13", "@15"]   # s01 + s02 peaks
              trigger: adjacent-in-peak-zone>=3
          prose_rationale_audit:
            count: 0
            verdict: BELOW-THRESHOLD-PASS
            report_path: active-project/staff/reviews/prose-rationale-audit-b01-c08-20260531T210000Z.md
            rationale: "all held-axis rationales are absence-discipline (the ledger does not open / no court-tier content / no new weight); none names a concrete physical element"
          coherence_review:
            verdict: PASS
            weave_gaps: 0
            followability_breaks: 0
            cold_read_risk_high: 0
            cold_read_risk_advisory: 5
            central_event_muffle_audit: 3-of-3-PASS  # PROP-0019-A; substance-aware-reader passes all three voice_risk_carry priors
            report_path: active-project/staff/reviews/coherence-b01-c08-20260531T210000Z.md
          readability_axis:
            verdict: AIRLESS
            basis: "cold-reader complaint matches chunk_cold_read.cold_read_risk_carry verbatim ('two names logged + a wider coverage map / no decision, cost, reversal'); 'no identifiable narrator' anchored on central-event spans (sightline-trace, logging-beat, closing image); AIRLESS-on-central-event"
          shipped_with_caveats_eligibility: pre-disposed-Class-B-matched   # would have triggered SHIPPED-WITH-CAVEATS via DEC-0060 + chunk-level pre-disposition for cold-read leg ALONE; OVERRIDDEN by INDEPENDENT staging-review spine-promotion FAIL on @6 axis-move central-event
          stale_since: null
        stitched: true   # /and-stitch REVISE Phase 9 SHIPPED-WITH-CAVEATS — draft/b01-c08.md terminal under polish-deferred chain
        stitched_at: 2026-05-31T22:00:00Z
        depth_pass_pending: false   # cold-read CONTINUE=no is design-inherent per chunk_cold_read pre-disposition; no further /and-write revise warranted within Class B disposition P framework
        depth_pass_resolved_at: 2026-05-31T22:00:00Z   # the revise pass itself + staging-review-v2 PASS satisfies the implicit depth-pass requirement for the chapter
        cast_rename:   # DEC-0065 (2026-06-01, admin user-proxy PATH A): c08 living feed-body wenna-cobb → meryn-cobb, to de-collide with c07 dead-child founding-entry "Wenna Cobb" (the first name in Taylor's grave-count). Pure slug substitution, no substance change. Applied to bones (cast line + @20), draft (line 29), archived scene-map. No dialogue file (meryn-cobb is a non-speaking coverage-map body). meryn-cobb asserts NO family relationship to the dead child (PATH B recast-as-family declined — cap-bounded finish run, not a substance-expansion session).
          from: wenna-cobb
          to: meryn-cobb
        forward_thread:   # /and-stitch b01-c08 Phase 10 (URI-STITCH-PHASE-10-FORWARD-THREAD; inline-executed 2026-06-01, OPTION (b) per DEC-0065 — c08 had shipped through Phase 9 under the OLD command body with no Phase 10; inline ran Steps 2-5 rather than full re-stitch)
          ran_at: 2026-06-01T05:08:00Z
          verdict: PASS-THREAD
          accumulated_past_source: drafts-fallback   # aggregate-state.md was absent at run; threading-review read draft/b01-c01..c07 directly
          report_path: active-project/staff/reviews/forward-thread-b01-c08-20260601T050033Z.md
          findings: 3
          edits_applied: 1   # rev-0001 presentation-reinforcement: calendar anchor in c08 prologue (Crone's stretch / bay-damp / first bell — c07 season register re-stated); resolves SOFT pl-2026-05-31-008 for c08
          edits_not_applied:
            - "UNPAID-HOOK substantive: c05 Rushwick courier/enforcement payoff — owned by /and-substance via pl-2026-05-31-007 (pre-tracked, deferred-by-design within c08-c10 window); c08 lands the courier-FACE leg (Corwick named). No new HARD item written; pl-2026-05-31-007 annotated; carried in aggregate-state open_hooks[]."
            - "MISSED-CALLBACK presentation-reinforcement: 'the septon's corner' callback on chandler-corner terrain — fence-against (c08 deliberately holds Halvard offstage; prologue already carries the unresolved-argument weight). Held-not-applied."
          new_substantive_hard_items: 0   # PASS-THREAD (not HOLD-THREAD): the one substantive finding is pre-existing + deliberately deferred, not a c08-incurred defect; does NOT block b01c09 Phase 0
          aggregate_state_emitted: active-project/staff/showrunner/aggregate-state.md   # CREATED initial version 1, through_chapter b01c08; 12 axis_state / 9 open_hooks / 9 characters / 7 world_state / 1 revision_layer; VALIDATION PASS
          aggregate_state_divergence_flag: "capability rank 5.5 (measured-delta authoritative) vs stale handoff narratives 5.0 (c04 redo never re-synced); recorded at 5.5; SOFT pl-2026-06-01-stitch-thread-001 routes c09 Phase 0 to log the aggregate-vs-handoff_in conflict and proceed on 5.5"
        chunk: |
          Capability staging chapter with two staging obligations: cf-d10-courier-face beat 1
          (the courier now has a face Taylor has attached a name to — Oswyn mentions him in
          passing as a figure who runs errands for someone above his station) and an Aemond
          foreshadow via Otto-mediated channel (a Jarvis delivery contains a logistics note
          that references Vhagar's handler rotation — Aemond off-stage but the escalation
          engine is becoming visible at the edges of the feed). Taylor also observes Oswyn
          running a ward-protection arrangement of his own — an informal network of watchers
          who notify him of strangers in the Hook. Taylor maps this network for coverage
          integration without telling Oswyn. The collision: Taylor is now integrating
          Oswyn's ward-protection work into her surveillance architecture without his knowledge,
          a direct echo of the override pattern she came here to atone for. She does not note
          this in the ledger. What shifts: capability adds a sub-increment; Aemond is now a
          pressure-present in the feed at low intensity.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: capability
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "Oswyn's watcher network integrated without his knowledge; coverage extends; Khepri-echo visible in method"
          axes_held:
            - axis: moral_framework
              rationale: "Oswyn integration is not logged as a breach in Taylor's accounting; the ledger does not open on this act; framework holds at current crack-level by Taylor's accounting"
            - axis: relational_anchor_status
              rationale: "Wren in coverage; no new weight this chapter; anchor holds at rank 3"
            - axis: political_register-prot
              rationale: "Aemond feed-reference is logistics, not behavioral content; resentment does not advance on logistics noise"
            - axis: social_tether-prot-rise
              rationale: "Oswyn integration is coverage architecture, not tether-building in the patron-adjacent sense; tether holds"
          density_target: 0.5-0.7
          chapter_class: standard
        dramatic_shape: rising
        goal: |
          Plant the courier face, activate the Aemond-adjacent pressure at low intensity, and stage the Oswyn-integration echo so that later Khepri-repetition accusations have been building in the reader's view long before Taylor's.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "Halvard counter-argument: first genuine engagement; not resolved"
            - "rationalize-each-trade: continuing"
            - "Wren: anchor rank 3"
            - "cf-d10-courier-face: courier in memory; unnamed"
            - "Black-faction elder consequences: pending"
          world_state:
            - "KL 122 AC; arrangement stable; Halvard present"
          character_state:
            - "Taylor: capability rank 4.5; moral_framework rank 0; political_register-prot rank 3"
          source_chapter: b01c07
        handoff_out:
          open_threads:
            - "cf-d10-courier-face beat 1 complete: courier has a name (Oswyn-supplied); body-map advancing"
            - "Aemond-adjacent pressure: Vhagar handler rotation in feed; low-intensity but logged"
            - "Oswyn watcher-network: integrated into coverage without his knowledge"
            - "Halvard: present; counter-argument unresolved"
            - "Wren: anchor rank 3"
          world_state:
            - "KL 122 AC; Oswyn's watcher-network now inside Taylor's coverage architecture"
            - "Aemond: off-stage but logistically visible in feed periphery"
          character_state:
            - "Taylor: capability rank 5 (Oswyn-network integrated); coverage expanding; moral_framework rank 0"
            - "Oswyn: unknowing node; watcher-network subsumed"
            - "courier-figure: named in Taylor's memory; body-map building"
          target_chapter: b01c09
        chunk_cold_read:
          reviewed_at: 2026-05-31T16:30:00Z
          verdict: SHIPPED-WITH-RISK-RECORDED
          classification: B
          recovered_summary: "A spy quietly absorbs another man's informant network and learns two names, doing nothing with either."
          intended_goal: |
            Plant the courier face, activate the Aemond-adjacent pressure at low intensity,
            and stage the Oswyn-integration echo so that later Khepri-repetition accusations
            have been building in the reader's view long before Taylor's.
          summary_maps_to_goal: true   # all three obligations present in summary (Oswyn-integration, courier-name, Aemond)
          continue: no                  # Q5 first-pass
          continue_strict: no           # Q7 re-answer (authoritative)
          report_path: active-project/staff/reviews/chunk-coldread-b01c08-2026-05-31.md
          disposition: P                # proceed-with-risk-recorded (Class B default)
          dispositioned_at: 2026-05-31T16:35:00Z
          dispositioned_by: admin       # DEC-0060 (same shape as DEC-0044)
          cold_read_risk_carry: |
            Staging-chapter quietness + deferral density. The chapter intentionally plants
            downstream pressure (cf-d10-courier-face, Aemond-foreshadow, Oswyn-integration-echo)
            without resolving any of it on-page. Cold reader (uninformed) read this as "two
            names logged + a wider coverage map. No decision, cost, reversal, or confrontation"
            and would not continue. The dramatist-confirmed "quiet-peak-at-s03" rising shape
            depends on the [image: oswyn-network-subsumed-in-silence] close carrying the
            chapter's payload as image-weight rather than as event-weight. /and-stitch Phase 9
            cold-read must score against this known risk: the strict-NO is design-inherent
            for a staging chapter and the chapter shipping CONTINUE=tentative-yes (not
            tentative-no) is the bar — not strict-yes, which would require an event-shaped
            chapter the contract is not authoring.

            Specific risk targets for /and-stitch:
              - s03 closing image must read as Khepri-echo without Taylor naming it.
                If the [image: oswyn-network-subsumed-in-silence] dissolves into
                routine-circuit drift at prose layer, the chapter's payload is lost.
              - s02 Aemond-entry must land as low-intensity edge in the feed, not as
                inert logistics filler. The [image: feed-geometry-acquires-a-new-edge]
                is the scene's sole forward-motion marker.
              - The reader-Taylor recognition gap on the Oswyn-integration must be
                visible without Taylor articulating it (moral_framework held discipline).
        scenes:
          - slug: b01c08s01
            seq: 1
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              The Hook circuit runs the same as it has run for weeks — three wards, the
              lane-junction at Rushwick's margin, the chandler's corner — and the insect-feed
              [mechanism: routine-as-cover] returns nothing unusual. Taylor is inside this
              routine when she notices, not for the first time but for the first time with
              attention, that Oswyn is also running a circuit. [event: oswyn-watcher-network-observed]
              He has watchers — not hired men, not formal; three or four regulars who position
              themselves at approaches to the lower Hook and who flag, in their own quiet ways,
              when a stranger enters the ward. A boy at the water-point. An old woman with a
              basket who always faces the lane-mouth. A cobbler's apprentice whose rate of
              nailing-in slows when someone he does not recognize turns the corner. Taylor
              maps the positions and the sightlines [mechanism: watcher-positions-mapped-to-feed-matrix]
              through the insect-feed without moving from her own station — she does not need
              to ask Oswyn about this; the feed gives her the geometry. [image: two-surveillance-architectures-occupying-the-same-ground]
              Oswyn's network is not subtle, but it does not need to be: it was built for people
              who already belong to the ward, running on the same social physics Taylor's own
              coverage is designed to be invisible to. She notes the gap in her coverage —
              three approach-corridors Oswyn's people see that her insect-density does not
              prioritize — and files the geometry. She does not tell Oswyn she has done this.
              [force: taylor-coverage-integration-without-consent] The circuit closes. The feed
              returns to its usual register. The work proceeds.
            scene_conflict:
              protagonist_force: "Taylor's coverage-integration drive — the gap in her insect-feed geometry is visible; Oswyn's network fills it; the operational logic is immediate and clean"
              opposing_force: "Oswyn's watcher-network as an independent system with its own social physics — a consent-requiring structure Taylor is absorbing without consent, on the same ground she mapped for a different architecture"
              stakes_axis: moral_framework
            substance_delta:
              axes_in_motion:
                - axis: capability
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: null
                  notes: "Oswyn's three-corridor watcher-network geometrically integrated into insect-feed coverage matrix; gap closed; coverage extends; Khepri-echo visible in method to reader, not to Taylor"
              axes_held:
                - axis: moral_framework
                  rationale: "integration executed without ledger-entry; Taylor's accounting does not open on this act; holds at rank 0 by her accounting — the reader-Taylor recognition gap is fully live here"
                - axis: relational_anchor_status
                  rationale: "Wren in coverage; no new weight this scene; anchor holds at rank 3"
                - axis: political_register-prot
                  rationale: "no court-tier content; resentment does not advance on ward-circuit operational beats"
                - axis: social_tether-prot-rise
                  rationale: "coverage-integration is operational, not tether-deepening; tether holds"
                - axis: moral_legibility_to_self
                  rationale: "the integration proceeds without Taylor naming what she is doing; legibility holds at rank 5"
              density_target: 0.5-0.65
          - slug: b01c08s02
            seq: 2
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              The Jarvis delivery arrives mid-afternoon [event: jarvis-delivery-arrives] — the
              standard channel, the standard interval, nothing in the packet's weight or seal
              that signals deviation. Taylor reads the contents in order: ward-report summaries,
              two intercept fragments from the Dragonpit-adjacent lanes, and then, in the
              logistics section, [event: vhagar-handler-rotation-noted] a note on Vhagar's handler
              rotation — a scheduling adjustment, names and dates, the kind of operational record
              that flows through the apparatus when the apparatus is large enough that its left
              hand does not know what its right hand knows is interesting. [image: escalation-engine-visible-at-feed-edge]
              The note is not addressed to anyone. It is not commentary. It sits inside the
              logistics section the way [mechanism: aemond-feed-entry-as-routine-logistics] a
              chandler's delivery schedule sits inside a supply ledger — present, unremarkable
              to the person who filed it, legible as something else entirely to the person reading
              the whole apparatus at once. Taylor reads the handler rotation. She registers the
              name attached to it — not the handler; above the handler — [force: aemond-adjacent-pressure-enters-feed]
              in the possessive notation that logistics documents use for chain-of-responsibility.
              The name does not appear in her current coverage. She logs it. [event: aemond-name-logged]
              [mechanism: political-register-held-on-logistics-noise] The feed continues. The
              next fragment is a bread-price report from the lower Blackwater approaches. She
              reads that too. The logistics note is a logistics note. She does not mark it
              differently from the bread prices. The resentment register stays flat. What shifts
              is the feed's geometry: the escalation engine has an edge now, [image: feed-geometry-acquires-a-new-edge]
              and the edge is lit at low intensity, and it was not lit before.
            scene_conflict:
              protagonist_force: "Taylor's feed-reading discipline — systematic intake of the Jarvis delivery; logistics treated as logistics; no affect-register shift"
              opposing_force: "the logistics note as a pressure-carrier that does not require Taylor's attention to operate — the escalation engine inserting itself into the feed at low intensity, indifferent to how she files it"
              stakes_axis: political_register-prot
            substance_delta:
              axes_in_motion: []
              axes_held:
                - axis: political_register-prot
                  rationale: "Aemond feed-entry is logistics-class; resentment does not advance on operational scheduling noise; the name is filed, not charged; holds at rank 3"
                - axis: capability
                  rationale: "feed-intake is maintenance-mode; no new deployment; capability holds at rank 5 after s01 increment"
                - axis: moral_framework
                  rationale: "no breach-adjacent act; holds (auditor fault-013 FLAG: rationale thin vs chapter contract; /and-write Phase 1 must stage opposing-force visibility on moral_framework if a bone touches the held discipline)"
                - axis: relational_anchor_status
                  rationale: "no Wren content; holds at rank 3"
                - axis: social_tether-prot-rise
                  rationale: "Jarvis-channel intake is information-flow, not patron-tether event; tether holds"
                - axis: moral_legibility_to_self
                  rationale: "logistics-reading is below the legibility threshold; holds at rank 5"
              density_target: 0.45-0.6
          - slug: b01c08s03
            seq: 3
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Taylor returns to the Hook ward that evening on a scheduled circuit pass and
              encounters Oswyn at the water-point where his watcher-boy usually stands.
              Oswyn is talking to someone — and that someone is the courier. [event: courier-face-at-oswyn-mention]
              Not remarkable to Oswyn: he mentions the man in passing, the way he mentions
              anyone he has placed in a category, [mechanism: courier-name-attached-via-oswyn-pass-mention]
              using the name without ceremony — "Corwick," he says, "runs errands for someone
              above his station; I've seen him up the hill twice this month" — and moves on.
              [event: courier-named-corwick] The name drops into Taylor's feed the way a position
              locks into a sightline: the face she has had without a name now has the name,
              and the name has a pattern (above-his-station; twice-up-the-hill), [image: face-and-name-locking-in-body-map]
              and the pattern has a direction she can follow if she needs to follow it. She
              does not follow it tonight. She holds the geometry in the feed and lets the
              encounter close. [force: taylor-body-map-advancing] The someone-above-the-station
              is not named by Oswyn; she does not ask. The body-map advances by one node
              and the node is now a person with a name and a route and a patron-shape she
              can recognize when she sees it again. [mechanism: body-map-node-built-without-asking]
              She walks the remainder of the circuit. The insect-feed runs across the ward,
              across the water-point, across the corner where Oswyn's watcher-boy is no longer
              standing — because his position is now inside Taylor's coverage matrix, [image: oswyn-network-subsumed-in-silence]
              covered by the geometry she mapped this afternoon. [force: oswyn-unknowing-node-complete]
              Oswyn does not know this. He is still talking when Taylor leaves.
            scene_conflict:
              protagonist_force: "Taylor's body-map completion drive — the courier has a face; the face now has a name; the name-attaching closes a gap she has been carrying since the original sighting"
              opposing_force: "Oswyn as the un-knowing conduit — his plain-contact social physics delivers the name without knowing what it delivers; his watcher-network subsumed in the same exchange; the absence of consent is the scene's undercurrent"
              stakes_axis: capability   # NOTE (auditor fault-007 FLAG): held axis this scene; conflict-frame label, NOT a Δ-authoring mandate — /and-write Phase 1 must not read as Δ-required (legal per Phase-3 union rule; c07s01 fault-009 precedent)
            substance_delta:
              axes_in_motion: []
              axes_held:
                - axis: capability
                  rationale: "capability advanced in s01; this scene closes the courier-face thread and confirms the Oswyn-network integration via the body-map advance and the scene-close image — but the Δ was taken at s01; holds at rank 5 through scene-close"
                - axis: moral_framework
                  rationale: "no new ledger-entry; the integration completion and the body-map advance both proceed without Taylor's accounting opening; holds at rank 0 by her accounting"
                - axis: relational_anchor_status
                  rationale: "Wren in coverage; no new weight; holds at rank 3"
                - axis: political_register-prot
                  rationale: "no court-tier content; holds at rank 3"
                - axis: social_tether-prot-rise
                  rationale: "Oswyn-encounter is operational-layer, not patron-tether event; tether holds"
                - axis: moral_legibility_to_self
                  rationale: "the integration-completion and the reader-Taylor recognition gap are both present in this scene — legibility holds at rank 5; the gap IS the scene's substance contribution without advancing the axis"
              density_target: 0.55-0.7

      - slug: b01c09
        status: stitched   # /and-stitch b01c09 DEPTH-PASS re-render COMPLETE + DEPTH-PASS RESOLVED (2026-06-01, DEC-0068 admin user-proxy A). draft/b01-c09.md re-shipped (27 bones, calendar-folded preamble, de-fogged body, RECONCILE 27/27 + 37/37). cold_read.verdict: still NO-CONTINUE at the uninformed cold-read (design-inherent Class-B + no-prior-context artifact, DEC-0062/0066) — BUT the depth pass DELIVERED its improvement, confirmed by 4 gates: Phase 2.5 Axis-2 ALIVE (deficit resolved), Phase 8.5 coherence PASS ("airlessness resolved at assembled-prose layer; a person is now present, hung on a felt body; fog gone"), Phase 9 Step 3.5 prose-rationale 0 mute (15/15 staged), Phase 5b trio endorsed the de-fog. depth_pass_resolved_at: 2026-06-01T185000Z; depth_pass_pending CLEARED (R2 retry cap spent; a 2nd loop would reproduce the design-inherent NO). The de-fog (abstract "architecture does not distinguish" → cold-hand image) + person-first open + grounded watch are the durable readability win even though the context-stripped terminal gate still penalizes the chapter's quietness. Phase 10 forward-thread (light: zero-Δ embodiment re-render; aggregate already through c09) follows. Process-critic: pattern already merged to PROP-0030/0031 at the prior stitch (DEC-0067); not re-fired. | /and-facets b01c09 DEPTH-PASS re-run COMPLETE (2026-06-01): 9 facets re-authored against 27 bones. Phase 2.5: Axis-1 completeness PASS + Axis-2 aliveness ALIVE (deficit RESOLVED — the @9 cold-hand de-fog LANDS). Phase 5 audit 0 HARD / 6 SIGNAL (advisory; sensory old-state lineage clean). Phase 5b ALL facets PASS 3-of-3 (trio 7/7 + sensory specialists; 0 remediation cycles; trio endorsed the de-fog + calendar-fold). De-fog completeness fix: memory mem:1 @8 resonance re-aligned from the abstract "architecture does not distinguish" phrasing to the cold-hand image (monument/axis unchanged) so the fog cannot return at stitch; NI@8→@9 annotation labels corrected in memory + state-updates. audience_gate_path staff/auditor/facets-audience-gate-r1.md; audit_path staff/auditor/facets-final-audit.md. depth_pass_pending STILL true (Phase 9 re-read stamps resolved). Carry to re-stitch: @9 cold-hand de-fog must hold at prose layer (NI:3+sensory:5; do NOT render memory's old abstraction); @14 apparatus-muffle; @23 channel-technical-fact not recognition (AP-SCAN advisory); s03 NO recognition beat. | /and-write b01c09 revise --from-signals DEPTH PASS (2026-06-01): consumed Phase-9 cold-read signals (AIRLESS "starved of person" + "abstract to fog"). +4 embodiment/grounding bones (zero net Δ; spine + contracted deltas preserved): s01 @2 taylor presses lane-stone (held/capability), @3 bay-damp beads lane-stone (chatter/cl-d08), @9 cold stiffens fingers (held/moral_legibility — de-fog anchor for @8 route-vs-person thesis); s02 @15 cold weights shoulders (held/capability — grounds watch-stillness, placed at watch-onset to keep SW-3 @16/@17 intact). Re-numbered 23->27 bones. Bone-gate CLEAN 0 HARD (SVO + held-enactment + chatter-anchor + zero-Δ + grounding over-satisfied + no mannerism + Earth-Bet clean). bones_count 27. depth_pass_pending=TRUE (Phase 9 re-read will stamp depth_pass_resolved_at on PASS). Old 23-bone facets+draft+cold_read STALE → archived (theater/_archive/20260601T174453Z-b01c09-pre-depthpass-facets); re-cascade /and-review bones -> /and-facets -> /and-stitch. Forward-instruction to facet re-run: NI @8 filing beat must render route-vs-person thesis THROUGH the @9 cold-stiffened-hand image, NOT the abstract "architecture does not distinguish" statement. | PRIOR (superseded by depth pass): /and-stitch b01c09 COMPLETE (2026-06-01): draft/b01-c09.md TERMINAL deliverable (preamble + 3-scene body, ~390 words, RECONCILE balanced 23/23 bones + 33/33 facets). Phase 9 cold-read verdict PASS-WITH-DEPTH-PASS-REQUIRED (DEC-0066, admin user-proxy A). cold_read: uninformed reader NO-CONTINUE + no-jeopardy + "abstract to fog / starved of person" (events recovered); readability_axis AIRLESS at cold-layer BUT Phase 8.5 coherence PASS (substance-aware: central events person-first, apparatus-muffle @11 discharged) + Phase 9 Step 3.5 prose-rationale-mute 0 findings PASS — the AIRLESS is the DEC-0062 CHUNK-CLASS-B design-inherent cost (strict-CONTINUE=no pre-recorded; CONTINUE bar tentative-yes), consistent with c06/c07/c08. depth_pass_pending: TRUE (mandatory before /and-substance book close / /and-review verdict b01). signal_clusters: none. Phase 1 person-first render (1 REWORD @9 metronome); Phase 5b had 1 fixer loop (sensory old-state lineage). CONSECUTIVE-AIRLESS pattern c06-c09 flagged for book-level /and-cohere (DEC-0066 queue). report: staff/reviews/coldread-b01c09-20260601T163000Z.md. Phase 9.5 process-critic + Phase 10 forward-thread follow. | /and-facets b01c09 COMPLETE (2026-06-01, DEC-0063 Option-B streamlined single-pass; R2 judging SKIPPED by decision). Phase 5 audit 0 HARD / 9 SIGNAL (all advisory: short-chapter freq-band denominator, slug-format cosmetic signal-meta-001, memory peak-concentration carve-out sound, exposition:3@8 validate-at-stitch signal-sup-001, monument-card + location-vibes margit referrals signal-con-001/ap-001). Phase 5b audience-gate CLEAR — all 8 content facets PASS 3-of-3 (metaphor 0 entries N/A). One fixer loop: sensory FAILed cycle-1 (old-state-reader REVISE, sensory:1@8 + sensory:3@11 old-state lineage unanchored — author SEAM-011/012 self-flags); remediated upstream-edit-first (loc-state:1@1 thermal + loc-state:3@8 visual + loc-state:5@17 tactile-prop baselines added; no sensory deletion); cycle-2 re-verify ACCEPT all 3 closed. bidirectional_loop: one-sided (auditor RUBRIC-FIDELITY old-state-anchor scan missed what the sensory specialist caught — calibration parking-lot item). Phase 5c NOT fired (clean final-cycle). audit_path: staff/auditor/facets-final-audit.md; audience_gate_path: staff/auditor/facets-audience-gate-r1.md; audience_gate_cycles: 1 (sensory 2). NOTE: Phase 5 auditor fork silent-write miss — report transcribed from fork return by orchestrator. audit_complete=true, audience_gate_complete=true, facets_path=theater/facets/. round_2 N/A (streamlined). | /and-write b01c09 COMPLETE (2026-06-01): 23 bones / 3 scenes emitted (theater/bones/b01-c09.md + scene-map-b01-c09.md); silent chapter (no dialogue files). Phase 6 bone-gate PASS: auditor 0 HARD / 2 SIGNAL accepted (s02n09 instrument-class + marks-verb, both carried to /and-stitch Phase 4); audience 9/9 SUBSTANCE-FELT (3×3). Pass 2 12 FAULT-FORM PP-recasts→CLEAN + 2 delta-floor by DEC-0002; Pass 3 +1 transition bone s02n09; Pass 4 3/3 ACCEPT 0-del; Pass 5 CONTINUITY-OK (corwick bare-slug resolved by c08 precedent pl-2026-06-01-001). NOTE: prior Phase 6 dispatch pair died silently (partial output); re-run completed the gate. | /and-substance chapter b01c09 (2026-05-31): 3 scenes decomposed. Phase 5: audience 3/3 SUBSTANCE-FELT all scenes; dramatist ACCEPT (rise-peak-fall, s03 thesis-image legitimate); auditor CLEAR (0 HARD, cost-ledger cl-d08/cl-d05 clean, thematic-axis clean). Phase 5.5 chunk-cold-read CHUNK-CLASS-B (summary maps to goal; strict-CONTINUE=no — prior-context/apparatus-vocab inaccessibility, same shape as c08/DEC-0060) → admin disposition P (DEC-0062); verdict SHIPPED-WITH-RISK-RECORDED. cl-d08 opened (+0.5 of +2; 1.5 remaining); cl-d05 continuation; cl-d06 2nd tranche +1.0 still deferred to c10/later (pl-2026-05-30-001). SW-1/2/3 audience watches carried to /and-write.
        chunk: |
          The relational_anchor_status transitions from rank 3 toward the d06-d08 threshold
          as Taylor's coverage map expands to include the lanes Wren moves through between
          her stitch-shop and the water-sellers. Taylor has not arranged this; it is a
          consequence of ward expansion. But the coverage is now comprehensive enough that
          Taylor knows Wren's daily pattern — where she goes, who she speaks to, when she
          is alone. Taylor notes this in her internal map and does not note it anywhere
          accessible to Jarvis. The cf-d10-courier-face beat 2: the courier appears in the
          feed in a context that is clearly not Oswyn-errand — he is meeting someone at the
          Dragonpit's lower gate in a posture that reads as report-delivery. Taylor cannot
          see to whom. She logs the observation and does not route it. The chapter's collision
          is the combination: Taylor is running surveillance on Wren without framing it as
          such, and she is withholding observations from Otto that might be valuable, and she
          is doing both simultaneously without a ledger entry for either act. What shifts:
          relational_anchor_status advances; the anchor is now structurally present in the
          coverage architecture without entry in the deliverable ledger.
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: relational_anchor_status
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: cl-d08   # resolved at /and-substance chapter Phase 3: cl-d08 first tranche (+0.5 of +2). Wren structurally present in coverage architecture without ledger entry = cl-d08 cost-clause match. cl-d06 2nd tranche (+1.0) NOT settled here (spoken/recognition event; deferred to c10/later per pl-2026-05-30-001).
              notes: "coverage extends to Wren's daily pattern; structural surveillance without ledger entry; anchor weight increases through omission-architecture; cl-d08 opened (journey-required cl03b paid c03-c04)"
            - axis: political_register-prot
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: cl-d05   # resolved at /and-substance chapter Phase 3: cl-d05 continuation draw (resentment-register opened c05; courier-gate inference deepens feed-color; not a new opening)
              notes: "courier's Dragonpit-gate meeting: Black-faction contact inferred; color accumulates on the feed content; minor advance; cl-d05 continuation"
          axes_held:
            - axis: moral_framework
              rationale: "no new breach logged; withholding from Jarvis and surveilling Wren are both unacknowledged in Taylor's ledger — framework holds by Taylor's own accounting"
            - axis: capability
              rationale: "coverage expansion is incremental ward-extension, not a new capability tier"
            - axis: social_tether-prot-rise
              rationale: "tether structure holds; no new patron-adjacent addition"
            - axis: moral_legibility_to_self
              rationale: "the double-omission is not yet a recognition event; legibility holds at rank 5"
          density_target: 0.5-0.7
          chapter_class: standard
        dramatic_shape: rising
        goal: |
          Show the audience that Taylor is now surveilling Wren as part of routine coverage — and that she is not calling it that — and advance the courier-face so the d10 accounting has a body with a history.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "cf-d10-courier-face beat 1 complete: courier named"
            - "Aemond-adjacent pressure: low-intensity in feed"
            - "Oswyn watcher-network: inside coverage"
            - "Halvard: present; counter-argument unresolved"
            - "Wren: anchor rank 3; in coverage map; daily pattern beginning to be legible"
          world_state:
            - "KL 122 AC; coverage expanding"
          character_state:
            - "Taylor: capability rank 5; moral_framework rank 0; political_register-prot rank 3"
            - "Otto: leverage rank 3.5"
          source_chapter: b01c08
        handoff_out:
          open_threads:
            - "cf-d10-courier-face beat 2 complete: courier observed at Dragonpit lower gate; Black-faction contact inferred; withheld from Jarvis"
            - "Wren: daily pattern inside coverage; anchor rank 3.5 (structural surveillance without ledger entry)"
            - "Halvard: present; counter-argument unresolved"
            - "Aemond-adjacent pressure: holding at low intensity"
            - "political_register-prot: resentment color deepening from courier-gate observation"
          world_state:
            - "KL 122 AC; Taylor withholding first observation from Jarvis/Otto; coverage comprehensive in five wards"
            - "courier-figure: Black-faction contact inferred; Taylor has a body and a pattern"
          character_state:
            - "Taylor: relational_anchor_status rank 3.5; political_register-prot rank 3.5; capability rank 5; moral_framework rank 0"
            - "Wren: surveilled without ledger entry; anchor weight at 3.5"
            - "courier-figure: body-map complete; pattern legible; withheld from Otto"
          target_chapter: b01c10
        chunk_cold_read:
          reviewed_at: 2026-05-31T00:00:00Z
          verdict: SHIPPED-WITH-RISK-RECORDED
          classification: B
          recovered_summary: "A surveillance operative realizes her bug-feed now covers a stranger's whole daily routine plus a suspicious courier, and decides to tell her boss neither thing."
          intended_goal: |
            Show the audience that Taylor is now surveilling Wren as part of routine coverage
            — and that she is not calling it that — and advance the courier-face so the d10
            accounting has a body with a history.
          summary_maps_to_goal: true   # surveillance-of-stranger's-routine + courier + double-withholding all present in summary
          continue: yes                 # Q5 first-pass ("weak yes" — the creepy specificity is a real hook)
          continue_strict: no           # Q7 re-answer post no-charity confusion list (AUTHORITATIVE)
          report_path: active-project/staff/reviews/chunk-coldread-b01c09-2026-05-31.md
          disposition: P                # proceed-with-risk-recorded (Class B default)
          dispositioned_at: 2026-05-31T00:00:00Z
          dispositioned_by: admin       # DEC-0062 (basis DEC-0060; same failure shape as c08)
          cold_read_risk_carry: |
            strict-CONTINUE=No — design-inherent: omission-chapter with apparatus vocabulary;
            known-risk, not delivery failure. Same shape as c08/DEC-0060 (apparatus-vocabulary +
            prior-context inaccessibility to a zero-context reader). The three contextful reviewers
            (audience 3/3, dramatist, auditor) all passed clean; only the no-prior-context cold-read
            dissented, and it explicitly attributed the confusions to "without the prior chapter."

            Specific risk targets for /and-stitch Phase 8.5/9 (already-dispositioned known-risk):
              - motive-opacity: Taylor's withheld-motive is absent from the narrative surface BY
                DESIGN (it is the chapter's thesis — the override-pattern visible to the reader,
                un-named by Taylor). context-weave pass should confirm implicit grounding exists or
                license a minimal context-ledger add; Phase 9 reads as design-intentional if no
                ledger add is made. Do NOT spell out the motive (would contradict dramatist ACCEPT
                on the thesis-image + violate the moral_legibility hold).
              - color-metaphor opacity ("resentment arrived with color / the color accrues"):
                project metaphor vocabulary established c01-c08. facet context-weave should confirm
                the c01-c08 anchor is sufficient; if not, context-ledger may license a grounding
                phrase (not a new bone).
              - causality-design-inherent: three parallel acts, not a chain. dramatist ACCEPT
                rise-peak-fall with s03 the thesis-image synthesis. Phase 9 treats as
                KNOWN-CLASS-B-DESIGN-INHERENT; the bar is CONTINUE=tentative-yes (not strict-yes,
                which would require an event-shaped chapter the contract is not authoring).
        scenes:
          - slug: b01c09s01
            seq: 1
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Taylor runs the ward circuit south of the Hook into the lanes between Wren's
              stitch-shop and the water-sellers' row. [event: ward-expansion-reaches-wren-lanes]
              The boundary moved three weeks ago — a density-fill pushed by the ward expansion
              Taylor requested after the Rushwick integration; the insect-feed has been threading
              these lanes since then as routine, and the patterns have accumulated the way any
              repeated-coverage pattern accumulates in the feed-record: not marked, not flagged,
              simply there. [mechanism: coverage-boundary-extension-produces-accumulated-pattern]
              Today Taylor runs the geometry with attention. What the feed has been returning
              is a legible daily circuit: the stitch-shop opens before the water-sellers' first
              bell; Wren moves between the two in a fixed window late morning; she stops at the
              bread-seller's corner; she speaks to no one she does not already know; she is alone
              between the shop-door and the water-sellers for one block, in a lane with one
              entrance. [image: wren-daily-pattern-inside-coverage-grid] Taylor holds this in
              her internal map — the time-block, the route, the lane geometry, when the entrance
              is unobserved. [force: wren-pattern-noted-in-internal-map]
              She does not hold it in the ward-coverage notes she routes to Jarvis. The
              ward-coverage notes receive the expanded boundary geometry: the new lanes, the
              feed-density, the coverage extension south to the water-sellers' junction.
              [mechanism: deliverable-receives-geometry-not-pattern]
              The lanes are there. The daily circuit inside the lanes is not.
              [force: wren-anchor-structurally-present-without-ledger-entry]
              The circuit continues. The feed runs the new ground the same way it runs the old.
            scene_conflict:
              protagonist_force: "Taylor's coverage-extension discipline — the ward expansion produced the feed geometry; running the circuit with attention is the operational default; she maps what the feed returns"
              opposing_force: "the deliverable ledger as institutional substrate — a separate record Jarvis receives, which contains the new geometry but not the pattern that makes Wren's daily position legible; the substrate split is enacted without being named as a withholding act"
              stakes_axis: relational_anchor_status
            substance_delta:
              axes_in_motion:
                - axis: relational_anchor_status
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl-d08
                  notes: |
                    cl-d08 first tranche (+0.5 of +2 total). Wren is structurally present in the
                    coverage architecture — her daily pattern is readable, her vulnerable lane-window
                    mapped — without appearing in the deliverable ledger that Jarvis receives. Matches
                    cl-d08 cost precisely ("[cost-bearer] structurally necessary to coverage map without
                    appearing in the ledger"). Journey-required cost (cl03b: network build + witch-label
                    exposure) was paid at c03-c04; c09 is the first moment the cl-d08 gain is enacted.
                    cl-d06 deferred second tranche (+1.0) is NOT settled here: that tranche belongs to a
                    spoken/recognition-register Wren event; remains open per pl-2026-05-30-001; targeting c10/later.
              axes_held:
                - axis: moral_framework
                  rationale: "the internal-map/deliverable substrate split is not entered in Taylor's accounting as a withholding act; the ward-coverage notes receive everything they have always received; the omission is in what Taylor chooses not to route, which she does not name as an omission; holds at rank 0 by her accounting"
                - axis: capability
                  rationale: "coverage extension is incremental ward-boundary movement following an already-executed expansion; no new capability tier; holds at rank 5"
                - axis: social_tether-prot-rise
                  rationale: "coverage-architecture extension is operational; no patron-adjacent event; tether holds"
                - axis: political_register-prot
                  rationale: "no court-tier content; no courier-face material; resentment does not advance on ward-circuit geometry; holds at rank 3"
                - axis: moral_legibility_to_self
                  rationale: "the substrate split proceeds without Taylor framing it as a choice; the gap between what her internal map holds and what the deliverable receives is this scene's substance contribution without advancing the axis; legibility holds at rank 5"
              density_target: 0.65-0.70
          - slug: b01c09s02
            seq: 2
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              The evening circuit runs the Dragonpit-adjacent margin — the outer lanes the
              insect-feed has covered since the ward expansion pushed south toward the hill.
              [event: dragonpit-margin-circuit-pass]
              The feed returns the standard distribution for this hour: servants at the far
              gate, a supply cart on the road below, two men at the stone-post beside the lower
              gate's side exit. [mechanism: insect-feed-reads-baseline-body-distribution]
              One of the two men is the courier. [event: courier-at-dragonpit-lower-gate]
              Not Oswyn's errand. [force: courier-outside-oswyn-errand-context] Wrong ward,
              wrong hour, wrong posture: the courier stands with his body angled toward the
              other man in the geometry [mechanism: courier-body-posture-reads-as-report-delivery]
              of a person who has delivered something and is waiting for the
              acknowledgment. Taylor cannot see the second man's face from the feed-angle.
              She cannot identify what changed hands, or whether anything did.
              What the feed gives her: the courier's body at the lower gate at an hour when
              Oswyn's errands do not run, in a posture the feed has taught her to read as
              delivery-complete. [image: courier-in-report-posture-at-dragonpit-lower-gate]
              The lower gate is not a Green-faction access point. It services a household
              whose factional alignment she has held in the feed-record since c05, when the
              resentment first arrived with color. [force: black-faction-contact-inferred-from-posture-and-location]
              The color accrues now — not a conclusion, a direction.
              [event: black-faction-contact-inferred]
              The courier is running errands above his station. The direction of the errands
              is not what was given when she filed his name.
              Taylor logs the observation in her internal feed-record: time, location,
              posture-class, inferred-pattern-type. [event: courier-dragonpit-observation-logged]
              She does not route it to Jarvis. [force: courier-observation-withheld-from-jarvis-channel]
              The Jarvis-deliverable will receive tomorrow morning's ward-summary.
              The courier's lower-gate visit will not be in it. The observation is in the
              feed-record. The feed-record is not the Jarvis channel.
            scene_conflict:
              protagonist_force: "Taylor's feed-reading discipline — the courier is a body in the coverage geometry; the observation is what the feed returns; logging it is the operational default; the withholding is enacted through substrate selection, not refusal"
              opposing_force: "the Jarvis-channel's institutional expectation — the courier observation is loggable and routable; the operational-security logic of the substrate split keeps it out of the channel without Taylor naming the act of keeping it out"
              stakes_axis: political_register-prot
            substance_delta:
              axes_in_motion:
                - axis: political_register-prot
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl-d05
                  notes: |
                    cl-d05 continuation draw (resentment-register opened at c05; neutral-observant
                    foreclosed from d05 forward). The courier at the Dragonpit lower gate adds a
                    specific Black-faction contact inference — a direction, not yet a named conclusion —
                    to the feed-color already present from c05. This is not a new opening; the resentment
                    register is continuous. Minor advance within the cl-d05 monotonic cost-curve.
                    Articulate contempt (cl06 register) is not reached here; this is the deepening color
                    that feeds political_register-prot monotonically between d05 and d13.
              axes_held:
                - axis: relational_anchor_status
                  rationale: "no Wren content in this scene; anchor holds at rank 3.5 after s01 advance"
                - axis: moral_framework
                  rationale: "withholding the courier observation is not entered in Taylor's ledger as a breach; the substrate split (feed-record vs Jarvis-channel) is the operational mechanism; Taylor does not name the gap as a withholding act; holds at rank 0 by her accounting"
                - axis: capability
                  rationale: "feed-reading and operational-note logging are maintenance-mode; no new deployment; holds at rank 5"
                - axis: social_tether-prot-rise
                  rationale: "courier observation is feed-content; no patron-adjacent event; tether holds"
                - axis: moral_legibility_to_self
                  rationale: "the withholding precedes Taylor naming it as withholding; the gap between the observation logged and the observation not routed is this scene's substance contribution without advancing the axis; legibility holds at rank 5"
              density_target: 0.65-0.70
          - slug: b01c09s03
            seq: 3
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Taylor closes the day's accounting at the feed-station. [event: daily-accounting-closes]
              The Jarvis-channel packet: the ward-coverage geometry extension south of the Hook,
              the new lane-density figures, two intercept fragments from the Rushwick margin.
              [mechanism: jarvis-packet-content-assembled-from-deliverable-substrate]
              She folds the packet and brings the seal down. [image: seal-down-on-packet-contents]
              On the station surface: the ward-coverage notes on the left, the sealed packet on
              the right. [force: deliverable-ledger-as-physical-object-on-station-surface]
              The internal map is held differently. It is the feed-record in her own architecture —
              the geometry she runs through the insects' return, the pattern-layer that does not
              transfer through the Jarvis channel. [mechanism: internal-map-substrate-distinct-from-deliverable]
              Wren's lane-circuit is there: time-block, route, the one-block stretch where the
              entrance is unobserved. [force: wren-pattern-in-internal-map-not-deliverable]
              The courier's lower-gate observation is there too — the same internal register,
              the same feed-record she draws from every day; present in the architecture the
              Jarvis packet is drawing from and simultaneously not drawing from.
              [force: courier-observation-in-internal-map-not-deliverable]
              [event: double-omission-structural-fact]
              [image: two-substrates-one-station-surface]
              She does not revisit either entry. The sealed packet holds what it holds.
              The feed-record holds what it holds separately.
              [mechanism: accounting-closes-with-split-substrate-intact]
              The ward is quiet. The feed runs its circuits. The seal is dry.
            scene_conflict:
              protagonist_force: "Taylor's end-of-day accounting discipline — the packet is prepared; the coverage notes are filed; the accounting closes by her standard; each substrate has received what it receives"
              opposing_force: "the split-substrate architecture itself — two records, one station surface, neither requiring Taylor to name the gap; the double-omission (Wren's pattern withheld, courier's observation withheld) is a structural fact before it is a volitional act"
              stakes_axis: moral_legibility_to_self
            substance_delta:
              axes_in_motion: []
              axes_held:
                - axis: relational_anchor_status
                  rationale: "Wren's pattern is in the internal map; the accounting-close adds no new weight to the anchor; holds at rank 3.5 after s01 advance"
                - axis: political_register-prot
                  rationale: "the courier observation sealed into the internal map; no new Black-faction inference beyond s02's advance; holds at rank 3.5 after s02 advance"
                - axis: moral_framework
                  rationale: "the accounting closes without an entry for either omission; the ledger does not open on the substrate split, the Wren-pattern omission, or the courier-withhold; holds at rank 0 by Taylor's accounting — the double-omission is structural fact, not a named breach"
                - axis: capability
                  rationale: "accounting-close is maintenance-mode; holds at rank 5"
                - axis: social_tether-prot-rise
                  rationale: "end-of-day operational beat; no patron-adjacent event; tether holds"
                - axis: moral_legibility_to_self
                  rationale: "the double-omission is enacted as structural fact — two substrates, one station surface, the seal down on what the packet contains; this is NOT a recognition event; Taylor does not name the shape of what she has done; the gap between what she has done and what she would have to admit is the scene's substance contribution WITHOUT advancing the axis; moral_legibility holds at rank 5 — this is the chapter's discipline"
              density_target: 0.55-0.70

        # /and-write Phase 7 chapter-level emit fields — 2026-06-01
        bones_file: theater/bones/b01-c09.md
        bones_count: 23
        substance_bone_gate_verdict: PASS
        substance_delta_measured:
          axes_moved:
            - { axis: relational_anchor_status, direction: up, magnitude: 0.5, anchor_bone: b01c09s01n04, cost_ledger: cl-d08 }
            - { axis: political_register-prot, direction: up, magnitude: 0.5, anchor_bone: b01c09s02n06, cost_ledger: cl-d05 }
          density_measured: 1.0   # 0 chatter / 23 total — fully structural (2 moving + 21 held; s03 all-held thesis-image close)
          felt_verdict: SUBSTANCE-FELT-3-of-3   # audience trio all 9 cells (3 scenes × 3 personas) SUBSTANCE-FELT + auditor CLEAR (Phase 6 bone-gate)
        # Phase 7 emit notes:
        #   Silent chapter — zero dialogue-anchor bones; no per-character dialogue files (Phase 1.5 no-op).
        #   Pipeline: Pass 2 (12 FAULT-FORM PP-recasts → CLEAN; 2 delta-floor resolved by DEC-0002 precedent)
        #     + Pass 3 dramatist (s01/s03 ACCEPT; s02 +1 transition bone s02n09 'the insect-feed returns corwick')
        #     + Pass 4 trim (3/3 ACCEPT, 0 deletions) + Pass 5 continuity (CONTINUITY-OK; corwick bare-slug resolved by c08 precedent, pl-2026-06-01-001)
        #     + Phase 6 bone-gate (auditor 0 HARD / 2 SIGNAL accepted; audience 9/9 SUBSTANCE-FELT).
        #   2 accepted SIGNALs carried to /and-stitch Phase 4 (scene-map protected-patterns): s02n09 instrument-class → render-physical; marks-verb variation.
        #   Per-bone substance_delta source of truth: staff/showrunner/b01c09-bones-draft-2026-05-31.md.
        bones_review:
          reviewed_at: 2026-06-01T00:00:00Z
          report_path: active-project/staff/reviews/bones-b01c09-2026-06-01.md
          verdict: PASS
          follow_check: PASS-WITH-NOTES
          bones_file_mtime_at_review: 1780286404
          stale_since: null
          notes: |
            fidelity PASS; 0 HARD / 2 SIGNAL (both already in scene-map advisories).
            follow_check PASS-WITH-NOTES — one context-addable flag (follow-001: s02 @8
            temporal/location pivot has no temporal marker on the bone; same-day-evening
            slightly ambiguous; context-addable at /and-facets Phase 2.5, NOT a FOLLOW-FAIL).
            aliveness: BONES-AIRLESS-RISK localized to scene-B @8-@11 (advisory; @11
            "insect-feed returns corwick" instrument-class courier-appears) → forewarns
            /and-facets Phase 2.5 grounding scrutiny + /and-stitch Phase 4 voice-embodiment.
            dialogue-coverage CLEAN (silent chapter). signal-002 @9/@10 marks-verb variation
            → /and-stitch Phase 4. RECOMMENDATION: CLEAR for /and-facets.

      - slug: b01c10
        status: audited-r1   # /and-facets b01c10 COMPLETE 2026-06-02. Phase 5 audit HARD=0/16 SIGNAL; Phase 5b audience-gate ALL 9 FACETS ACCEPT 3/3 (cycle 2, no cap-burn — NI/memory/sensory remediated via 3 fixer REVISEs); orchestrator-critic SUCCESS 7/7. [Phase 4 COMPLETE 2026-06-02.
        audit_complete: true
        audit_path: active-project/staff/auditor/facets-final-audit.md
        audit_findings: 16   # 0 HARD, 16 SIGNAL (all dispositioned w/ documented defense)
        audience_gate_complete: true
        audience_gate_path: active-project/staff/auditor/facets-audience-gate-r2.md
        audience_gate_cycles: 2
        audience_gate_cap_burned: false
        bidirectional_loop: validated   # shared finding: @24 figurative-register doubling (auditor DEDUP + worm-canon revise + metaphor-R2 AP4)
        facets_path: active-project/theater/facets/
        round_1_complete: true
        round_2_complete: true
        orchestrator_critic_verdict: SUCCESS   # 7/7 criteria
        facets_dialogue: none   # silent chapter (0 speech bones)
        facets_process_notes: "merge-time fixes — feeling entry-line IDs must be bare-numeric (R1 author wrote prefix-prefixed -> stale-cite); state slice citations collide post-consolidation -> stripped to c09-proven back=N. Container git-clone reset mtimes (bones-review freshness check is a false-negative artifact; stale_since:null is authoritative)." R2: NI K5/D1/A2 (del @5, add spine @16/@24, 25.9% band-stretch documented); memory K2/D0/A0 (spine resolved, doubled-register held); feeling K2/D0/A0 (NI-anti-dup PASS); metaphor 0 (4 refusals); exposition K2/REWORD1/A1 (ctx-001 satisfied @2 exposition:4). Arbiter: 0 interventions, 0 discipline-fails, f-r2-counts all 0. Merge: 60 entries, 81.5% decorated. 4d scene-map validation CLEAN (27/27 one scene). [prior faceted-r1: R1 fanout 10 authors; merge fixes feeling bare-numeric IDs + state back=N strip per c09 pattern]
        bones_file: theater/bones/b01-c10.md
        bones_count: 27
        substance_bone_gate_verdict: PASS   # Phase 6: auditor 0 HARD (after cycle-1 fix: 9 held-axis witnesses + 2 signal recasts) / 7 SIGNAL all dispositioned (3 stakes-tie + 3 abstract-object accept-with-rationale, signal-005/007 remediated); audience 3-of-3 SUBSTANCE-FELT all 4 scenes
        substance_delta_measured:
          axes_moved:
            position-prot-rise: 1.0
            social_tether-prot-rise: 1.0
            social_tether-antag: 1.5
            position-world: 1.0
            political_register-world: 1.0
            moral_framework: -1.0
            moral_legibility_to_self: 0.5
          density_measured: 0.78   # 27 bones / 4 scenes; 3 chatter (s01n01, s02n01) — substantive density within 0.7-0.9 target
          felt_verdict: SUBSTANCE-FELT   # 3-of-3 audience all scenes
        bones_review:
          reviewed_at: 2026-06-02T01:20:27Z
          report_path: active-project/staff/reviews/bones-b01c10-2026-06-02T01-20-27Z.md
          verdict: PASS-WITH-NOTES
          follow_check: PASS-WITH-NOTES   # no FOLLOW-FAIL -> /and-facets cleared
          aliveness: BONES-AIRLESS-RISK   # scene C grounding sparse/back-loaded -> /and-facets Phase 2.5 + /and-stitch Phase 4
          bones_file_mtime_at_review: 2026-06-02T01:07:39Z
          stale_since: null
          carry_to_facets_phase_2_5:
            - "HIGH context-weave: B->C surrender->detention causal seam (interior recognition that the routed corridor is the corridor they walked him down)"
            - "MEDIUM context-weave: beat-(a) formalization opacity @2 (surface informal->named arrangement via packet content + interior register)"
            - "exposition: s01 Sera-as-stated-consideration (packet content, not in bone SVO by design)"
            - "grounding-ledger: scene C aliveness (sparse/back-loaded grounding)"
        context_followability:
          completeness_verdict: FOLLOWABLE   # Phase 4.5 post-R2
          readability_verdict: ALIVE         # Phase 4.5 post-R2 (silent-chapter aliveness load: 7 sensory grd-001..007 + 2 feeling + 4 NI)
          report_path: active-project/staff/reviews/context-follow-r2-b01-c10-2026-06-02.md
          reviewed_at: 2026-06-02
          context_ledger_open: 0   # ctx-001 satisfied by exposition:4 @2 (Sera-consideration)
          grounding_ledger_open: 0  # grd-001..007 all satisfied (license over-cap R1 sensory exempt from band)
          phase_4_6_fired: false   # FOLLOWABLE+ALIVE; context-weave track ended at 4.5
          voice_fixable_carry: ["VF-1 @10/@11 surrender as two distinct physical acts", "VF-2 @15/@17/@18 detention as perceptual feed-event not data-transaction", "VF-3 @27 terminal face as physical feed-datum (suppressed-recognition fence)", "VF-4 @13 reworded interval bridge render"]
        coherence_review:   # /and-stitch Phase 8.5
          reviewed_at: 2026-06-02
          verdict: PASS
          weave_gaps: 0
          followability_breaks: 0
          cold_read_risk_high: 0
          cold_read_risk_advisory: 2   # @27 terminal + @24 override-echo, both fence-protected
          armed_muffle_check: "BOTH central events land concretely — s02 surrender (@10/@11) as two chosen irreversible acts; s03 detention (@15/@17/@18) as perceptual feed-event. NOT muffled."
          report_path: active-project/staff/reviews/coherence-b01-c10-2026-06-02.md
        cold_read:   # /and-stitch Phase 9 terminal gate
          read_at: 2026-06-02
          verdict: PASS-WITH-DEPTH-PASS-REQUIRED   # ships terminal; depth pass mandatory before book-close
          completeness_axis: PASS   # Step-2 diff: central event recovered, continue=barely-yes, jeopardy present
          readability_axis: {verdict: AIRLESS, basis: "cold-read 'dense/arm's-length throughout' + barely-yes continue; acts-of-commission under-staged (@2/@11/@21); density partly design-inherent for the silent apparatus-POV climax (cf. chunk_cold_read PASS-CHUNK-VOICE-RISK + consecutive-airless c06-c09 watch DEC-0066/0067)"}
          recovered_summary: "A surveillance operator, coerced by a protection deal, hands a man they'd quietly tracked for months over to a war machine, then sits with the fact that the man is gone and the record of him isn't."
          report_path: active-project/staff/reviews/coldread-b01-c10-2026-06-02.md
          staging_signals: 6
          staging_report_path: active-project/staff/reviews/staging-b01-c10-2026-06-02.md
          prose_rationale_audit: {verdict: PASS, count: 0, report_path: active-project/staff/reviews/prose-rationale-audit-b01-c10-2026-06-02.md}
          signal_clusters:
            - {pattern: spine-staging-gap, count: 4, bone_ids: [2, 11, 21, 18], trigger: "spine-staging-gap>=1"}
          phase_8_5_discharge: "central-event STAGE findings @2/@11/@21 flagged FAIL by staging spine-promotion rule, DISCHARGED to BLOCKING (not FAIL) by Phase 8.5 coherence PASS (armed-muffle check: both central events land concretely) + Step-1 cold-read recovery of the central events. FAIL escalation NOT fired; the residual spine-staging-gap fires the cluster soft-gate -> PASS-WITH-DEPTH-PASS-REQUIRED."
          depth_pass_target: "/and-write b01c10 revise --from-signals (stage acts-of-commission @2 declare / @11 route / @21 inscribe; de-abstract density; @18 grounding) -> re-cascade /and-facets + /and-stitch"
          stale_since: null
        depth_pass_pending: true   # set by Phase 9 PASS-WITH-DEPTH-PASS-REQUIRED; resolve before /and-review verdict b01 / book-close
        stitched: true   # /and-stitch b01c10 COMPLETE 2026-06-02 — draft/b01-c10.md TERMINAL (1074 words)
        forward_thread:   # /and-stitch Phase 10
          verdict: HOLD-THREAD
          edits_applied: {cosmetic: 0, presentation_reinforcement: 1}   # rev-0004 Wren-callback prologue
          substantive_to_parking_lot: [pl-2026-06-02-stitch-thread-001, pl-2026-06-02-stitch-thread-002]   # Halvard hook-0007 + cl-d06 tranche -> /and-substance c11 Phase 3
          aggregate_state: "updated through b01c10; validation PASS; 2 hooks paid (Corwick courier-face hook-0002 + lower-gate thread hook-0010), 3 opened (hook-0011 arrangement-formal / hook-0012 Dance-pulse-1 / hook-0013 Corwick-face-persists->d14), hook-0007 Halvard left-open-window-passed"
          report_path: active-project/staff/reviews/forward-thread-b01-c10-2026-06-02.md
        chunk: |
          Otto formalizes the arrangement: no longer a contingent exchange but a named,
          ongoing function. Taylor is his intelligence instrument for the Flea Bottom and
          lower-city layer; Sera's protection continues as the consideration. Otto names this
          explicitly in a meeting conducted through Jarvis (Taylor and Otto have never met
          directly). At the same meeting, Otto requests the courier's identity and pattern —
          Taylor has been holding this observation, and Otto asking for it by description makes
          clear his apparatus already knows the courier exists, only not from Taylor's feed.
          Taylor provides the information. The d10 event: the courier (a Black-faction
          logistics figure Taylor has body-mapped across months) is detained within two days
          of Taylor's report. Taylor learns of the detention through the insect-feed. The
          collision: the political_register-world advances as the arrangement is formalized;
          Taylor's position-prot-rise is confirmed at its functional peak; and the detention
          produces the first Dance-pressure pulse — the war's logic has moved through Taylor's
          network without her consent or design. The Rhaenyra-pressure staging: Taylor's
          feed includes a Black-faction figure's detention, which is traceable to intelligence
          Taylor provided; Rhaenyra's agents are at a remove, but the architecture Taylor
          built has now actively foreclosed a Black-faction logistics thread. What shifts:
          position-prot-rise peaks, social_tether-antag advances, position-world increments,
          political_register-world increments; the courier's face becomes the ledger's first
          closed entry with a name.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - axis: position-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl-d07a
              notes: "formalization of the arrangement; Otto names the function explicitly; position confirmed at near-peak; cl-d07a opens (naming forecloses informal-deniability); 1.0 of 2.0 drawn here, leaving 1.0 for cl-d07a completion at c14"
            - axis: social_tether-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl03b
              notes: "arrangement formalized = tether load-bearing confirmed; tether now structural in Otto's architecture"
            - axis: social_tether-antag
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl-antag-d10
              notes: "non-extractable confirmed in progress; Otto's leverage structural post-formalization; cl-antag-d10 opening"
            - axis: position-world
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl-world-d04
              notes: "arrangement formalized = Green succession channel solidifies; position-world gain from intelligence architecture Taylor accepted; cl-world-d04 (1.0 of 2.0 remaining at this point; journey-required cl03a)"
            - axis: political_register-world
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl-world-d07
              notes: "Green succession channel solidifies through formalized arrangement; cl-world-d07 FIRST tranche +1.0 of +2.0 (political_register-world's first movement from start_rank 5 per aggregate-state) — balance +1.0 remains for future allocation; NOT completed (auditor fault-003)"
            - axis: moral_framework
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl03a
              notes: "courier information delivered and deployed against a named person who is now detained; systematic-override-rationalized threshold crossed; cl03a cost side"
            - axis: moral_legibility_to_self
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "detention visible in feed; Taylor runs the accounting and files it; suppressed recognition event — legibility crack deepens but does not open"
          axes_held:
            - axis: relational_anchor_status
              rationale: "Wren not in the formalization meeting or the courier delivery; anchor holds at 3.5"
            - axis: political_register-prot
              rationale: "the detention produces resentment material but processing is deferred to b01c11; the formalization meeting occupies the chapter's structural weight"
            - axis: social_tether-prot-collapse
              rationale: "non-extractable confirmation is beginning but not yet complete; collapse axis not yet active"
          density_target: 0.7-0.9
          chapter_class: standard
        dramatic_shape: climax
        goal: |
          Show the audience the formalization and the detention in the same chapter so the structure is clear: Otto naming the arrangement and Taylor's feed confirming its operational consequence are the same event.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "cf-d10-courier-face beat 2 complete: courier withheld from Jarvis"
            - "Wren: daily pattern inside coverage; anchor rank 3.5"
            - "Halvard: counter-argument unresolved"
            - "Aemond-adjacent: low-intensity in feed"
          world_state:
            - "KL 122 AC; arrangement functional but still informal"
            - "courier-figure: Black-faction logistics; body-map complete; withheld"
          character_state:
            - "Taylor: relational_anchor_status rank 3.5; political_register-prot rank 3.5; capability rank 5; moral_framework rank 0; position rank 3"
            - "Otto: leverage rank 3.5; waiting to formalize"
          source_chapter: b01c09
        handoff_out:
          open_threads:
            - "courier detained: Dance-pressure pulse 1 complete; Black-faction logistics thread foreclosed"
            - "arrangement formal: Otto has named the function; informal-deniability foreclosed for Taylor"
            - "cf-rhaenyra-pressure staging: Black-faction logistics thread closed = Dragonstone-adjacent consequences pending at remove"
            - "Wren: in coverage; anchor rank 3.5; still outside formal ledger"
            - "Halvard: counter-argument unresolved; Taylor's engagement becoming thinner"
            - "non-extractable confirmation: in progress"
          world_state:
            - "KL 122 AC; arrangement formalized; Green faction position advances; Black-faction logistics thread actively foreclosed"
            - "position-world rank 7; political_register-world rank 6"
          character_state:
            - "Taylor: position-prot-rise rank 4 (rise-phase; aggregate 3 + chapter +1.0 = 4; peak ~7 at d07; Phase-5 continuity fix from stale 4.5); social_tether-prot-rise rank 7 (aggregate 6 + chapter +1.0 = 7; Phase-5 continuity fix from stale 4); social_tether-antag rank 5 (structural; aggregate 3.5 + chapter +1.5 = 5.0, dramatist fix); moral_framework rank -1 (systematic-override entered); moral_legibility rank 5.5 (crack); position-world rank 7"
            - "courier-figure: detained; ledger entry closed on a named person; face to the cost"
            - "Otto: leverage structural post-formalization"
          target_chapter: b01c11
        chunk_cold_read:
          reviewed_at: 2026-06-01T23:50:00Z
          verdict: PASS-CHUNK-VOICE-RISK
          classification: n/a
          recovered_summary: "A bug-controlling spy gets formally named as a spymaster's tool, hands over a man she'd been protecting by omission, watches him vanish, and files the guilt away in a ledger she won't reopen."
          intended_goal: "Show the audience the formalization and the detention in the same chapter so the structure is clear: Otto naming the arrangement and Taylor's feed confirming its operational consequence are the same event."
          continue: yes
          continue_strict: yes
          report_path: active-project/staff/reviews/chunk-coldread-b01c10-2026-06-01.md
          disposition: n/a
          dispositioned_at: 2026-06-01T23:50:00Z
          dispositioned_by: n/a
          voice_risk:
            triggered: true
            signals: [A, B]
            central_event: "Taylor surrenders the withheld Corwick body-map to Otto through Jarvis; the courier is detained within two days; Taylor reads the detention in the feed and files Corwick as a closed ledger entry."
            voice_risk_carry: |
              Central event reaches the reader partly through abstraction-vocabulary (feed-geometry,
              posture-class, substrate-split, accounting/ledger). Two muffle risks for /and-stitch
              Phase 8.5 Check 3: (1) the s02 Corwick-surrender ("she provides it") can collapse to a
              procedural clause so the act of commission is muffled below cold-reader legibility;
              (2) the s03 detention can render as a data-record transaction rather than a perceptual
              feed-event (body absent from geometry + Gold Cloak posture-class). Verify both land
              concretely in the assembled prose.
          cold_read_risk_carry: |
            Airlessness (4 single-POV scenes, no dialogue, no second on-stage body, s04 near-pure
            internal accounting) + under-motivated central choice (Corwick-surrender justified by
            assertion, not dramatized pressure). Design-inherent for this climax; surfaced early.
            Carried to /and-write as bones-execution watches (enact the surrender; aliveness in the
            accounting scenes) and to /and-stitch Phase 9 jeopardy/aliveness scrutiny.
        scenes:
          - slug: b01c10s01
            seq: 1
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Jarvis comes at the standard hour with a packet in the standard channel — but the packet
              is not a question. [event: jarvis-delivers-formalization-naming] What it contains is a
              declaration: the arrangement is no longer a contingent exchange but a named, ongoing
              function. [mechanism: otto-names-the-arrangement-through-jarvis] Taylor is described in
              the packet as Otto Hightower's instrument for the Flea Bottom and lower-city intelligence
              layer. Sera's protection continues as the stated consideration. [force: otto-names-the-function-explicitly]
              The language is precise the way a contract is precise — it does not leave the frame open.
              [image: packet-text-closes-the-frame] Taylor reads it at the feed-station, the bay-cold
              still on the morning stone outside. The packet does not ask her to accept; it describes
              what the arrangement already is. [mechanism: formalization-as-fait-accompli-not-negotiation]
              She and Otto have not met. The meeting is Jarvis's hands, the packet's wax, the text.
              [force: jarvis-as-only-channel-taylor-otto-never-direct] The function has been named.
              The informal reading — the one in which she could have told herself it was still her
              choosing each delivery in sequence — is foreclosed. [event: informal-deniability-foreclosed]
            scene_conflict:
              protagonist_force: "Taylor's operational discipline — the packet is the standard channel; she reads what it contains; she does not refuse"
              opposing_force: "the naming itself as institutional act — Otto's declaration forecloses the informal reading Taylor had been sustaining; the text is the trap completing, not a new pressure"
              stakes_axis: position-prot-rise
            substance_delta:
              axes_in_motion:
                - axis: position-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl-d07a
                  notes: |
                    cl-d07a first tranche (+0.5 of +1.0 drawn this chapter). Otto names the function
                    explicitly; Taylor's position is confirmed — Otto has a name for what she does.
                    Opportunity-cost side of cl-d07a opens here: informal-deniability foreclosed by
                    the packet's language. The naming is the position advance; the foreclosure is the
                    price. Second tranche (+0.5) settles at s04 when Taylor runs her own accounting.
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl03b
                  notes: |
                    cl03b first tranche this chapter (+0.5 of +1.0 drawn here). Formalization = tether
                    now structural in Otto's architecture. The arrangement being named is also the tether
                    being confirmed as load-bearing — this is what cl03b's future-cost collateral was
                    always reaching toward. Second tranche (+0.5) settles at s04 (Taylor's accounting
                    closes on the confirmed function).
              axes_held:
                - axis: moral_framework
                  rationale: "the packet names what is already operative; Taylor does not enter this naming as a new breach in her ledger — the function was already running; the formalization is institutional, not a new moral act by her accounting; holds at rank 0"
                - axis: relational_anchor_status
                  rationale: "Wren is not in the packet, not in the meeting; the Jarvis channel contains no Wren content; anchor holds at rank 3.5"
                - axis: political_register-prot
                  rationale: "the packet is Otto's register, not court-tier content returned by the feed; no new resentment color; holds at rank 3.5"
                - axis: moral_legibility_to_self
                  rationale: "Taylor reads the packet and files what it names; she does not register the foreclosure as a recognition event; holds at rank 5"
            density_target: 0.70-0.80
            bones:
            - slug: b01c10s01n01
              flat_id: 1
              shape: chatter
              svo: jarvis delivers the packet
              substance_delta:
                axis_moves: []
                axes_held: []
                cost_ledger_anchor: cl-d07a
            - slug: b01c10s01n02
              flat_id: 2
              shape: moving
              svo: the packet-text closes the frame
              substance_delta:
                axis_moves:
                - axis: position-prot-rise
                  direction: up
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl-d07a
            - slug: b01c10s01n03
              flat_id: 3
              shape: held
              svo: the morning-stone holds the bay-cold
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: moral_framework
                  rationale: formalization names what is already operative; Taylor does not open a new ledger entry on the institutional act itself; the prohibition-against-breach has not been triggered by a packet — framework held at current crack-level by grounding the scene's physical location (feed-station exterior)
                - axis: relational_anchor_status
                  rationale: Wren is not in the packet or the formalization; the morning-stone/bay-cold grounding holds the scene at the feed-station exterior with no Wren-content; anchor holds at rank 3.5
                cost_ledger_anchor: null
            - slug: b01c10s01n04
              flat_id: 4
              shape: moving
              svo: taylor-hebert-kl-122ac folds the packet
              substance_delta:
                axis_moves:
                - axis: social_tether-prot-rise
                  direction: up
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl03b
            - slug: b01c10s01n05
              flat_id: 5
              shape: held
              svo: taylor-hebert-kl-122ac exhales
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: moral_legibility_to_self
                  rationale: Taylor reads the packet and files what it names; the foreclosure is not yet a recognition event; legibility holds — she exhales on the content without interrogating it; the body-response is the non-event of a recognition that does not open
                - axis: political_register-prot
                  rationale: the packet is Otto's register, not court-tier content returned by the feed; the exhale registers the formalization without resentment-color entering; political_register-prot holds at rank 3.5
                cost_ledger_anchor: null
            event_map:
            - event: 'jarvis-delivers-formalization-naming [event: jarvis-delivers-formalization-naming]'
              bones:
              - b01c10s01n01
              - b01c10s01n02
              omission_rationale: null
            - event: 'otto-names-the-arrangement-through-jarvis [mechanism: otto-names-the-arrangement-through-jarvis]'
              bones:
              - b01c10s01n02
              omission_rationale: null
            - event: 'packet-text-closes-the-frame [image: packet-text-closes-the-frame]'
              bones:
              - b01c10s01n02
              omission_rationale: null
            - event: 'otto-names-the-function-explicitly [force: otto-names-the-function-explicitly]'
              bones:
              - b01c10s01n02
              - b01c10s01n04
              omission_rationale: null
            - event: 'formalization-as-fait-accompli-not-negotiation [mechanism: formalization-as-fait-accompli-not-negotiation]'
              bones:
              - b01c10s01n02
              - b01c10s01n04
              omission_rationale: null
            - event: 'jarvis-as-only-channel-taylor-otto-never-direct [force: jarvis-as-only-channel-taylor-otto-never-direct]'
              bones:
              - b01c10s01n01
              omission_rationale: null
            - event: 'informal-deniability-foreclosed [event: informal-deniability-foreclosed]'
              bones:
              - b01c10s01n02
              - b01c10s01n04
              omission_rationale: null
            - event: 'protagonist_force: Taylor''s operational discipline — reads, does not refuse'
              bones:
              - b01c10s01n04
              - b01c10s01n05
              omission_rationale: null
            - event: 'opposing_force: naming as institutional act; text closes the informal reading'
              bones:
              - b01c10s01n02
              omission_rationale: null

          - slug: b01c10s02
            seq: 2
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              At the same exchange Jarvis carries a second item: a description, not a name.
              [event: otto-requests-courier-by-description] The description is accurate — the courier's
              approximate age, his errand-pattern as Otto's apparatus has read it from outside Taylor's
              feed, the frequency of his appearances at the Rushwick margin and the Dragonpit lower-gate
              road. [mechanism: otto-apparatus-knows-courier-exists-but-not-from-taylors-feed]
              Otto's apparatus already knows the courier exists. It does not know what Taylor knows.
              [force: otto-requests-what-taylors-feed-uniquely-holds] The request is by description
              because the apparatus has the silhouette and not the body-map. [image: silhouette-versus-body-map]
              Taylor has the body-map. She has had it since the fifth circuit of the Rushwick-margin
              lanes, and she has been holding it in the internal record that does not route to Jarvis.
              She has Corwick's name from Oswyn. [mechanism: corwick-name-held-from-oswyn-c08-introduction]
              She has the errand-pattern, the posture-classes, the
              lower-gate faction-inference — the second man he faced at the heir's-business gate under
              Rhaenys's Hill, the direction the errands were running. [force: taylors-body-map-as-withheld-observation-surrendered]
              She provides it. [event: taylor-provides-corwick-identity-and-pattern] Not the whole
              internal record in its own form — she translates it into the channel's register: name,
              errand-frequency, the faction-contact inference, the lower-gate visit-date. She does not
              recount to herself why she had been holding it. She routes it through Jarvis. The
              substrate split closes on Corwick. [mechanism: withheld-observation-enters-jarvis-channel]
            scene_conflict:
              protagonist_force: "Taylor's harm-reduction calculus — Otto has the silhouette already; withholding the body-map from a patron who already has an independent sight-line on Corwick changes nothing about Corwick's exposure; the rational account says provide it"
              opposing_force: "the internal record as distinct substrate — Taylor has been sustaining the split between what the feed holds and what Jarvis receives; providing the Corwick body-map collapses one substrate boundary; the act is irreversible"
              stakes_axis: moral_framework
            substance_delta:
              axes_in_motion:
                - axis: moral_framework
                  direction: down
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl03a
                  notes: |
                    cl03a cost side first tranche this chapter (−0.5 of −1.0 total drawn here). Taylor
                    delivers a body-map she has been withholding — she provides a specific person's
                    identity and movement-pattern to a patron whose apparatus will act on it.
                    Systematic-override-rationalized threshold is loading; the cost side is the harm-
                    reduction calculus that prices Corwick's exposure against Sera's protection and finds
                    the entry acceptable. Second tranche (−0.5) settles at s04 when the courier-name
                    enters the ledger as a closed entry on a detained person.
                - axis: social_tether-antag
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl-antag-d10
                  notes: |
                    cl-antag-d10 opening tranche (+0.5 of +1.5 drawn this chapter). Otto's request
                    by description confirms his apparatus has an independent sight-line on Corwick —
                    non-extractable confirmation is in progress; Otto can corroborate Taylor's feed
                    against his own apparatus. The request is leverage making itself visible: he asked
                    for something Taylor had been keeping back, and he asked from knowledge that she
                    was keeping something back. Second and third tranches (+0.5 + +0.5) settle at s3
                    and the chapter-level close.
              axes_held:
                - axis: position-prot-rise
                  rationale: "the courier delivery is subordinate to the formalization; no additional position advance in this scene; holds at rank 3.5 after s01 advance"
                - axis: social_tether-prot-rise
                  rationale: "the delivery is a channel act, not a new patron-tether event; tether holds at rank 6.5 after s01 advance"
                - axis: relational_anchor_status
                  rationale: "Wren is not in the courier exchange; anchor holds at rank 3.5"
                - axis: moral_legibility_to_self
                  rationale: "Taylor runs the harm-reduction calculus and closes the entry; the filing does not produce a recognition event; legibility holds at rank 5 — the crack does not open until the detention is visible in the feed"
                - axis: political_register-prot
                  rationale: "the courier delivery is a channel act; no new court-tier color in the feed; holds at rank 3.5"
            density_target: 0.75-0.85
            bones:
            - slug: b01c10s02n01
              flat_id: 6
              shape: chatter
              svo: the second item opens the packet
              substance_delta:
                axis_moves: []
                axes_held: []
                cost_ledger_anchor: cl03a
            - slug: b01c10s02n02
              flat_id: 7
              shape: held
              svo: the lower-gate road marks the body-map
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: social_tether-antag
                  rationale: Otto's apparatus already knows the courier exists — the request by description is the apparatus making its knowledge visible; the lower-gate road as location surfaces the feed-geography where Taylor built the body-map that Otto does not have; Otto's leverage is visible as the gap between 'silhouette' and 'body-map'; antag leverage is held at sub-peak pending the delivery
                cost_ledger_anchor: null
            - slug: b01c10s02n03
              flat_id: 8
              shape: held
              svo: the body-map fills the feed-record
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: moral_framework
                  rationale: 'opposing force enacted: the internal record as a distinct substrate from the Jarvis channel — the months of accumulated body-map (errand-corridor, posture-classes, lower-gate faction-inference) are a coherent, physically-indexed observation set; this bone makes the substrate visible as a weight before the delivery collapses it; the framework is held at its current crack level by the visibility of what is about to be crossed'
                - axis: position-prot-rise
                  rationale: Otto's leverage is visible as the silhouette/body-map gap; no new formalization event this scene; position-prot-rise holds at rank 4 (post-s01 advance)
                cost_ledger_anchor: null
            - slug: b01c10s02n04
              flat_id: 9
              shape: held
              svo: corwick squares the stone-post
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: moral_legibility_to_self
                  rationale: the specific body-posture Taylor accumulated in the feed — the lower-gate posture, the report-delivery stance — is here as a concrete recalled image before it becomes a line-item; legibility holds because Taylor runs the harm-reduction calculus without naming the accumulation as a recognition event; the recalled posture is data, not guilt
                - axis: political_register-prot
                  rationale: Corwick's body-posture is ward-level Flea Bottom observation, not court-register content; political_register-prot holds at rank 3.5
                cost_ledger_anchor: null
            - slug: b01c10s02n05
              flat_id: 10
              shape: moving
              svo: taylor-hebert-kl-122ac translates the body-map
              substance_delta:
                axis_moves:
                - axis: moral_framework
                  direction: down
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl03a
            - slug: b01c10s02n06
              flat_id: 11
              shape: moving
              svo: taylor-hebert-kl-122ac routes the body-map
              substance_delta:
                axis_moves:
                - axis: social_tether-antag
                  direction: up
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl-antag-d10
            - slug: b01c10s02n07
              flat_id: 12
              shape: held
              svo: the wax dries
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: relational_anchor_status
                  rationale: Wren is not in this exchange; anchor holds at rank 3.5; the substrate split closes on Corwick not Wren — the bone that grounds the closure (wax drying = channel sealed) enacts the relational_anchor hold by physically marking the boundary of what was delivered and what was not
                - axis: social_tether-prot-rise
                  rationale: the channel seal is a delivery act, not a new patron-tether event; social_tether-prot-rise holds at its structural rank (post-s01 advance)
                cost_ledger_anchor: null
            event_map:
            - event: 'otto-requests-courier-by-description [event: otto-requests-courier-by-description]'
              bones:
              - b01c10s02n01
              - b01c10s02n02
              omission_rationale: null
            - event: 'otto-apparatus-knows-courier-exists-but-not-from-taylors-feed [mechanism: otto-apparatus-knows-courier-exists-but-not-from-taylors-feed]'
              bones:
              - b01c10s02n02
              omission_rationale: null
            - event: 'otto-requests-what-taylors-feed-uniquely-holds [force: otto-requests-what-taylors-feed-uniquely-holds]'
              bones:
              - b01c10s02n02
              - b01c10s02n03
              omission_rationale: null
            - event: 'silhouette-versus-body-map [image: silhouette-versus-body-map]'
              bones:
              - b01c10s02n02
              - b01c10s02n03
              omission_rationale: null
            - event: 'corwick-name-held-from-oswyn-c08-introduction [mechanism: corwick-name-held-from-oswyn-c08-introduction]'
              bones:
              - b01c10s02n03
              - b01c10s02n04
              omission_rationale: null
            - event: 'taylors-body-map-as-withheld-observation-surrendered [force: taylors-body-map-as-withheld-observation-surrendered]'
              bones:
              - b01c10s02n03
              - b01c10s02n04
              - b01c10s02n05
              omission_rationale: null
            - event: 'taylor-provides-corwick-identity-and-pattern [event: taylor-provides-corwick-identity-and-pattern]'
              bones:
              - b01c10s02n05
              - b01c10s02n06
              omission_rationale: null
            - event: 'withheld-observation-enters-jarvis-channel [mechanism: withheld-observation-enters-jarvis-channel]'
              bones:
              - b01c10s02n06
              - b01c10s02n07
              omission_rationale: null
            - event: 'protagonist_force: harm-reduction calculus — Otto has silhouette; withholding changes nothing'
              bones:
              - b01c10s02n05
              - b01c10s02n06
              omission_rationale: null
            - event: 'opposing_force: internal record as distinct substrate — providing collapses a substrate boundary'
              bones:
              - b01c10s02n03
              - b01c10s02n04
              omission_rationale: null

          - slug: b01c10s03
            seq: 3
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Two days later the insect-feed returns the Dragonpit-margin lower-gate road empty.
              [event: lower-gate-road-returns-empty-in-feed] Not routinely empty — the supply cart
              position is there, the stone-post at the side-exit is there, the servants at the far
              gate are there. [mechanism: baseline-body-geometry-intact-minus-one-body]
              Corwick is not. [event: corwick-absent-from-feed-geometry] He has been in the feed
              every second or third circuit since Taylor first picked up his pattern at the Rushwick
              margin. The geometry of his absences has a signature. This is not that signature.
              [image: absence-as-read-against-prior-pattern] Taylor moves the feed through the
              lower-gate approach, the road below, the lane-cluster that connects to his errand-
              corridor. [mechanism: taylor-reads-corwick-absence-through-feed-sweep]
              The body is not in the geometry. [force: corwick-body-removed-from-coverage-geometry]
              Within two circuit-passes the feed returns a secondary signal: [event: secondary-signal-returns-detention-information]
              a Gold Cloak patrol-pair at the lane-junction where Corwick's errand-corridor empties
              into the road — at rest, not transiting, posted. [image: gold-cloak-pair-at-corwicks-junction]
              The patrol posture-class is a guard stationed after an action, not before one.
              [mechanism: patrol-posture-reads-as-post-detention-not-pre] Taylor reads this the way
              the feed has taught her to read it: the body that was in the geometry is not in the
              geometry; the apparatus that moves through Otto's channels has run. [force: green-apparatus-operational-consequence-visible-in-feed]
              The war's logic has moved through her network. [event: dance-pressure-pulse-one-complete]
              The Green succession channel has been used. [event: green-succession-channel-operational]
              She did not plan this. The feed does not record plans. [mechanism: taylors-network-acted-without-her-consent-or-design]
            scene_conflict:
              protagonist_force: "Taylor's feed-reading discipline — absence is a read against prior pattern; the Gold Cloak posture-class is a posture-class; she draws what the geometry gives her"
              opposing_force: "the operational consequence as perceptual fact in the feed — the body that was present is absent; the apparatus Taylor's delivery reached has run; the feed returns the consequence without asking her to name what she started"
              stakes_axis: position-world
            substance_delta:
              axes_in_motion:
                - axis: position-world
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl-world-d04
                  notes: |
                    cl-world-d04 second tranche (completing the chapter's position-world allocation).
                    The Green succession channel is visibly operational: Corwick's detention closes a
                    Black-faction logistics thread Taylor's intelligence architecture reached. The world
                    consolidation is the direct output of Taylor's capability delivery — the apparatus
                    ran on what she provided. +1.0 of +1.0 chapter target drawn here.
                - axis: political_register-world
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl-world-d07
                  notes: |
                    cl-world-d07 completing this chapter. The Green succession channel — the one Otto's
                    formalized arrangement is consolidating — is now demonstrably operational. Taylor's
                    intelligence delivery closed a Black-faction logistics thread; the faction-violence
                    sub-pressure has produced its first on-page tactical consequence (a courier detained,
                    a thread foreclosed). Rhaenyra's apparatus will feel this at a remove. +1.0 of +1.0
                    chapter target drawn here. NOTE (auditor fault-003): this is the FIRST tranche of
                    cl-world-d07's +2.0 total — political_register-world's first movement from start_rank
                    (per aggregate-state, political_register-world was at start_rank entering c10). +1.0
                    balance remains for future allocation; cl-world-d07 NOT completed.
                - axis: social_tether-antag
                  direction: up
                  target_delta_magnitude: 1.0
                  cost_ledger_anchor: cl-antag-d10
                  notes: |
                    cl-antag-d10 second and third tranches (+1.0 here; +0.5 from s02 for +1.5 total).
                    Non-extractable confirmed in progress: the apparatus ran within two circuit-passes of
                    Taylor's delivery; the speed of the operational response confirms the depth of
                    integration between Taylor's feed and Otto's apparatus. Otto's leverage is now
                    structural — Taylor is load-bearing in a way that has produced visible external
                    consequence. Exiting would now require explanations Taylor cannot give.
              axes_held:
                - axis: moral_framework
                  rationale: "Taylor reads the feed; she does not enter the detention as a ledger event in this scene; the accounting has not opened yet; the cost side of cl03a second tranche settles at s04; holds at rank −0.5 (s02 tranche drawn) through this scene"
                - axis: moral_legibility_to_self
                  rationale: "the detention is visible in the feed — the body not in the geometry — but Taylor reads it as feed data, not as recognition; the recognition event is s04; legibility holds at rank 5 through this scene"
                - axis: relational_anchor_status
                  rationale: "Wren not in this scene; anchor holds at rank 3.5"
                - axis: social_tether-prot-rise
                  rationale: "the operational consequence is the antag-leverage event, not a new prot-rise event; tether holds at rank 6.5 pending s04 close"
                - axis: position-prot-rise
                  rationale: "position-world/political_register-world advance is the world-axis movement; position-prot-rise holds at rank 3.5 pending s04 accounting-close tranche"
            density_target: 0.80-0.90
            bones:
            - slug: b01c10s03n01
              flat_id: 13
              shape: held
              svo: the supply cart marks the lower-gate road
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: position-prot-rise
                  rationale: the supply cart as standing geometry — the lower-gate road baseline that Taylor runs every circuit; the cart's presence enacts the feed's normal body-distribution against which corwick's absence will read; position holds because the world-axis advance (not the protagonist-rise axis) is what this scene moves
                cost_ledger_anchor: null
            - slug: b01c10s03n02
              flat_id: 14
              shape: held
              svo: corwick walks the errand-corridor
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: moral_framework
                  rationale: Taylor's feed has been reading Corwick every second or third circuit since the Rushwick margin — the prior-circuit presence is the established pattern; the framework holds because the pattern-reading is within the licensed exception (operational intelligence already delivered); no new breach event at this bone; the presence-count is what makes the absence legible as deviation
                cost_ledger_anchor: null
            - slug: b01c10s03n03
              flat_id: 15
              shape: moving
              svo: the lower-gate road loses corwick
              substance_delta:
                axis_moves:
                - axis: position-world
                  direction: up
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl-world-d04
            - slug: b01c10s03n04
              flat_id: 16
              shape: held
              svo: the stone-post marks the side-exit
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: moral_legibility_to_self
                  rationale: the stone-post present = the baseline geometry intact minus one body; the recognition that the body-not-in-geometry is Corwick-detained has not yet opened as a named event; Taylor reads the geometry as data; legibility holds because the reading is feed-discipline not recognition; the stone-post's presence (contrasted with Corwick's absence) enacts the non-recognition posture concretely
                cost_ledger_anchor: null
            - slug: b01c10s03n05
              flat_id: 17
              shape: moving
              svo: the Gold Cloak pair posts the lane-junction
              substance_delta:
                axis_moves:
                - axis: political_register-world
                  direction: up
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl-world-d07
            - slug: b01c10s03n06
              flat_id: 18
              shape: moving
              svo: the insect-feed sweeps the errand-corridor
              substance_delta:
                axis_moves:
                - axis: social_tether-antag
                  direction: up
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl-antag-d10
            - slug: b01c10s03n07
              flat_id: 19
              shape: held
              svo: the bay-cold presses the lower road
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: relational_anchor_status
                  rationale: Wren not in this scene; the bay-cold as physical environmental constant grounds the scene's temporal setting (same morning cold as s01) without adding Wren-weight; anchor holds at rank 3.5
                - axis: social_tether-prot-rise
                  rationale: the circuit-pass confirms the network ran but adds no new patron-tether event; social_tether-prot-rise holds at structural-load rank
                cost_ledger_anchor: null
            event_map:
            - event: 'lower-gate-road-returns-empty-in-feed [event: lower-gate-road-returns-empty-in-feed]'
              bones:
              - b01c10s03n03
              omission_rationale: null
            - event: 'baseline-body-geometry-intact-minus-one-body [mechanism: baseline-body-geometry-intact-minus-one-body]'
              bones:
              - b01c10s03n01
              - b01c10s03n04
              omission_rationale: null
            - event: 'corwick-absent-from-feed-geometry [event: corwick-absent-from-feed-geometry]'
              bones:
              - b01c10s03n02
              - b01c10s03n03
              omission_rationale: The absence is enacted by the presence-count (n02) followed by the empty-road (n03); the physical geometry reads as deviation from established pattern. No additional bone needed.
            - event: 'absence-as-read-against-prior-pattern [image: absence-as-read-against-prior-pattern]'
              bones:
              - b01c10s03n01
              - b01c10s03n02
              - b01c10s03n03
              omission_rationale: null
            - event: 'taylor-reads-corwick-absence-through-feed-sweep [mechanism: taylor-reads-corwick-absence-through-feed-sweep]'
              bones:
              - b01c10s03n06
              omission_rationale: null
            - event: 'corwick-body-removed-from-coverage-geometry [force: corwick-body-removed-from-coverage-geometry]'
              bones:
              - b01c10s03n03
              - b01c10s03n06
              omission_rationale: null
            - event: 'secondary-signal-returns-detention-information [event: secondary-signal-returns-detention-information]'
              bones:
              - b01c10s03n05
              omission_rationale: null
            - event: 'gold-cloak-pair-at-corwicks-junction [image: gold-cloak-pair-at-corwicks-junction]'
              bones:
              - b01c10s03n05
              omission_rationale: null
            - event: 'patrol-posture-reads-as-post-detention-not-pre [mechanism: patrol-posture-reads-as-post-detention-not-pre]'
              bones:
              - b01c10s03n05
              omission_rationale: null
            - event: 'green-apparatus-operational-consequence-visible-in-feed [force: green-apparatus-operational-consequence-visible-in-feed]'
              bones:
              - b01c10s03n05
              - b01c10s03n06
              omission_rationale: null
            - event: 'dance-pressure-pulse-one-complete [event: dance-pressure-pulse-one-complete]'
              bones:
              - b01c10s03n05
              - b01c10s03n06
              omission_rationale: null
            - event: 'green-succession-channel-operational [event: green-succession-channel-operational]'
              bones:
              - b01c10s03n05
              omission_rationale: null
            - event: 'taylors-network-acted-without-her-consent-or-design [mechanism: taylors-network-acted-without-her-consent-or-design]'
              bones:
              - b01c10s03n03
              - b01c10s03n06
              omission_rationale: null
            - event: 'protagonist_force: feed-reading discipline — absence read against prior pattern; Gold Cloak posture-class'
              bones:
              - b01c10s03n02
              - b01c10s03n03
              - b01c10s03n05
              omission_rationale: null
            - event: 'opposing_force: operational consequence as perceptual fact — apparatus ran on what she provided'
              bones:
              - b01c10s03n05
              - b01c10s03n06
              omission_rationale: null

          - slug: b01c10s04
            seq: 4
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Taylor opens the ledger at the feed-station. [event: taylor-opens-ledger-post-detention]
              The convention is not new: gains and costs, the entry, the consideration that prices it.
              [mechanism: ledger-as-taylors-accounting-convention] She has run this since the first
              delivery. The entries have always had a shape: a named-person-protected on one side, a
              harm-reduction calculation on the other. [force: ledger-convention-shapes-the-accounting]
              She writes Corwick. [event: corwick-name-enters-ledger-as-closed-entry] Not as a node,
              not as a pattern, not as a body in the geometry — as a name on a closed entry.
              [image: corwick-name-written-as-closed-ledger-entry] The gain side: Sera's protection
              continues; the arrangement is formalized; the Green succession channel is operational.
              The cost side: a Black-faction logistics courier, body-mapped across months and withheld
              from the channel through nine circuits, has been detained within two days of Taylor's
              delivery. [mechanism: harm-reduction-calculus-runs-on-corwick-as-named-person] His
              face — the lower-gate posture, the errand-corridor geometry she has run through the
              feed since the Rushwick-margin first circuit — is in the record. She knows what he
              looks like in the feed. She knows the pattern of his errands. She knows he was running
              Black-faction logistics and did not know her network was reading him.
              [image: corwicks-feed-face-present-in-internal-record] He did not consent to the
              observation. He did not consent to the body-map. He did not consent to the delivery.
              [force: corwicks-unconsented-instrumentalization-named-in-accounting]
              Taylor writes the entry and closes the ledger. [event: ledger-entry-closed-on-named-person]
              The gain column is accurate. The cost column is accurate. The accounting is complete.
              [mechanism: systematic-override-rationalized-threshold-crossed-accounting-files]
              She does not revisit the entry. The ledger holds what it holds. [force: suppressed-recognition-event]
              The face stays in the feed-record. The ledger does not ask her to stay with it.
              [image: corwicks-face-in-feed-record-after-ledger-close]
            scene_conflict:
              protagonist_force: "Taylor's ledger-accounting discipline — the entry has a shape; the gain side and the cost side are both real; she closes every entry by convention; accounting is her substitute for recognition"
              opposing_force: "the face in the feed-record as irresolvable surplus — Corwick's body-map was built across months; the feed-face cannot be abstracted back into the cost-column after it has been entered there; the ledger closes but the face does not disappear from the internal record"
              stakes_axis: moral_legibility_to_self
            substance_delta:
              axes_in_motion:
                - axis: position-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl-d07a
                  notes: |
                    cl-d07a second tranche (+0.5; completing the chapter's position-prot-rise +1.0 total).
                    Taylor's accounting closes on the formalized function — she enters the arrangement
                    as confirmed and named; her position at near-peak is acknowledged in the ledger
                    as the gain column of the formalization entry. cl-d07a opportunity-cost
                    (informal-deniability foreclosed) already recorded at s01; this tranche is the
                    accounting confirmation of the position advance.
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl03b
                  notes: |
                    cl03b second tranche (+0.5; completing the chapter's social_tether-prot-rise +1.0).
                    The accounting close confirms tether load-bearing: Taylor's deliveries are now
                    structural to Otto's apparatus. The tether is not merely functional — it has
                    produced visible operational consequence. The gain column holds it; the cost
                    column (future-cost collateral per cl03b) does not yet appear in Taylor's
                    accounting as the trap it is.
                - axis: moral_framework
                  direction: down
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl03a
                  notes: |
                    cl03a cost side second tranche (−0.5; completing the chapter's moral_framework −1.0).
                    Taylor closes a ledger entry on a named detained person. The harm-reduction calculus
                    runs: Sera's protection outweighs Corwick's detention. The calculus is complete.
                    Systematic-override-rationalized threshold crossed: she has now used information
                    about a specific named person — body-mapped without consent — to price a
                    protection and file it. The entry closes. The systematic-override-rationalized
                    THRESHOLD does not re-open (a one-way moral milestone) — but NOTE (auditor fault-002
                    disambiguation): this is distinct from the cl03a LEDGER entry, which is only
                    −1.0 of −2.0 drawn this chapter (−0.5 s02 + −0.5 s04); cl03a retains −1.0 balance
                    for future chapters and is NOT closed.
                - axis: moral_legibility_to_self
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: null
                  notes: |
                    No anchor — suppressed recognition event. The detention is now in the ledger as a
                    closed entry. Taylor ran the accounting and filed it; she did not stay with the
                    face. But the face is in the feed-record. The gap between "the ledger is complete"
                    and "the face does not disappear" is the crack deepening: the legibility crack does
                    not open (Taylor does not name the shape of what she has done) but the record-keeping
                    convention shows its limits as a substitution for recognition. +0.5 on the axis;
                    crack deepens, does not open. Rank moves from 5 to 5.5 — suppressed recognition
                    event per c10 contract.
              axes_held:
                - axis: social_tether-antag
                  rationale: "antag-leverage structural post-detention; the accounting does not produce new leverage; cl-antag-d10 full allocation already drawn in s02-s03 (+1.5 total); holds at structural confirmed"
                - axis: position-world
                  rationale: "world consolidation drawn in full at s03; no new world-axis movement at accounting close; holds at rank 7 (post-s03 advance)"
                - axis: political_register-world
                  rationale: "world political-register drawn in full at s03 (cl-world-d07 completed); holds at rank 6 (post-s03 advance)"
                - axis: relational_anchor_status
                  rationale: "Wren not in the accounting; anchor holds at rank 3.5; the Corwick entry does not produce a Wren-weight event"
                - axis: political_register-prot
                  rationale: "resentment material is present (the detention, the feed reading it) but processing is deferred to b01c11; holds at rank 3.5"
                - axis: social_tether-prot-collapse
                  rationale: "non-extractable confirmation in progress but collapse axis not yet active; holds at start_rank 8"
            density_target: 0.75-0.85
            bones:
            - slug: b01c10s04n01
              flat_id: 20
              shape: held
              svo: taylor-hebert-kl-122ac opens the ledger
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: social_tether-antag
                  rationale: the ledger-open is a convention Taylor has run since the first delivery; opening the ledger does not produce new leverage for Otto — it is Taylor's internal accounting convention; antag leverage is structural and confirmed; it holds at the structural-confirmed state from s03
                - axis: position-world
                  rationale: the ledger-open files the world-consequence already settled in s03; no new world-axis movement; position-world holds at rank 7
                cost_ledger_anchor: null
            - slug: b01c10s04n02
              flat_id: 21
              shape: moving
              svo: taylor-hebert-kl-122ac writes corwick
              substance_delta:
                axis_moves:
                - axis: moral_framework
                  direction: down
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl03a
            - slug: b01c10s04n03
              flat_id: 22
              shape: held
              svo: the feed-station stone grounds the wrist
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: political_register-prot
                  rationale: the physical act of writing at the feed-station — the stone's surface is the grounding contact that roots the scene's accounting work in a bodily register; no court-tier content enters in this scene; resentment material deferred to c11; register holds at rank 3.5
                - axis: political_register-world
                  rationale: the accounting work adds no new succession-channel register; political_register-world holds at rank 6 (post-s03)
                cost_ledger_anchor: null
            - slug: b01c10s04n04
              flat_id: 23
              shape: held
              svo: corwick faces the lower-gate
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: moral_legibility_to_self
                  rationale: 'the observation bone: this is Corwick''s body as observed in the feed — the posture Taylor read but did not consent to observe; the first ''did not consent'' beat (observation); legibility holds because Taylor is filing the image, not naming the recognition'
                cost_ledger_anchor: null
            - slug: b01c10s04n05
              flat_id: 24
              shape: held
              svo: corwick crosses the errand-corridor
              substance_delta:
                axis_moves: []
                axes_held:
                - axis: relational_anchor_status
                  rationale: 'the body-map bone: Corwick''s errand-geometry as the accumulated cartography of movement; anchor holds because Wren is not in this accounting; the Corwick-entry does not produce Wren-weight; but the accumulated body-map pattern (without consent) is structurally parallel to the omission-architecture Taylor runs for Wren — the pattern is the same, the absence from the ledger is what differs'
                - axis: social_tether-prot-collapse
                  rationale: non-extractable confirmation in progress but the collapse axis is not yet active; social_tether-prot-collapse holds at start_rank 8
                cost_ledger_anchor: null
            - slug: b01c10s04n06
              flat_id: 25
              shape: moving
              svo: taylor-hebert-kl-122ac closes the ledger
              substance_delta:
                axis_moves:
                - axis: position-prot-rise
                  direction: up
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl-d07a
            - slug: b01c10s04n07
              flat_id: 26
              shape: moving
              svo: taylor-hebert-kl-122ac presses the feed-station
              substance_delta:
                axis_moves:
                - axis: social_tether-prot-rise
                  direction: up
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: cl03b
            - slug: b01c10s04n08
              flat_id: 27
              shape: moving
              svo: corwick squares the feed-record
              substance_delta:
                axis_moves:
                - axis: moral_legibility_to_self
                  direction: up
                  magnitude: 1
                axes_held: []
                cost_ledger_anchor: null
            event_map:
            - event: 'taylor-opens-ledger-post-detention [event: taylor-opens-ledger-post-detention]'
              bones:
              - b01c10s04n01
              omission_rationale: null
            - event: 'ledger-as-taylors-accounting-convention [mechanism: ledger-as-taylors-accounting-convention]'
              bones:
              - b01c10s04n01
              omission_rationale: null
            - event: 'ledger-convention-shapes-the-accounting [force: ledger-convention-shapes-the-accounting]'
              bones:
              - b01c10s04n01
              - b01c10s04n02
              omission_rationale: null
            - event: 'corwick-name-enters-ledger-as-closed-entry [event: corwick-name-enters-ledger-as-closed-entry]'
              bones:
              - b01c10s04n02
              omission_rationale: null
            - event: 'corwick-name-written-as-closed-ledger-entry [image: corwick-name-written-as-closed-ledger-entry]'
              bones:
              - b01c10s04n02
              omission_rationale: null
            - event: 'harm-reduction-calculus-runs-on-corwick-as-named-person [mechanism: harm-reduction-calculus-runs-on-corwick-as-named-person]'
              bones:
              - b01c10s04n02
              - b01c10s04n04
              - b01c10s04n05
              - b01c10s04n06
              omission_rationale: null
            - event: 'corwicks-feed-face-present-in-internal-record [image: corwicks-feed-face-present-in-internal-record]'
              bones:
              - b01c10s04n04
              - b01c10s04n05
              - b01c10s04n08
              omission_rationale: null
            - event: 'corwicks-unconsented-instrumentalization-named-in-accounting [force: corwicks-unconsented-instrumentalization-named-in-accounting]'
              bones:
              - b01c10s04n04
              - b01c10s04n05
              - b01c10s04n06
              omission_rationale: 'The three ''did not consent'' beats are enacted as three structurally distinct bones: observation (n04 faces-the-lower-gate), body-map (n05 squares-the-errand-corridor), delivery (n08 squares-the-feed-record). ''did not consent'' is not stated — it is enacted by the three-layer decomposition of what the body-map accumulated without consent.'
            - event: 'ledger-entry-closed-on-named-person [event: ledger-entry-closed-on-named-person]'
              bones:
              - b01c10s04n06
              omission_rationale: null
            - event: 'systematic-override-rationalized-threshold-crossed-accounting-files [mechanism: systematic-override-rationalized-threshold-crossed-accounting-files]'
              bones:
              - b01c10s04n02
              - b01c10s04n06
              omission_rationale: null
            - event: 'suppressed-recognition-event [force: suppressed-recognition-event]'
              bones:
              - b01c10s04n08
              omission_rationale: null
            - event: 'corwicks-face-in-feed-record-after-ledger-close [image: corwicks-face-in-feed-record-after-ledger-close]'
              bones:
              - b01c10s04n08
              omission_rationale: null
            - event: 'protagonist_force: ledger-accounting discipline — convention; gain and cost real; she closes'
              bones:
              - b01c10s04n02
              - b01c10s04n06
              omission_rationale: null
            - event: 'opposing_force: face in feed-record as irresolvable surplus — ledger closes, face does not disappear'
              bones:
              - b01c10s04n06
              - b01c10s04n08
              omission_rationale: The two-bone split (n06 = ledger closes; n08 = face persists) is the enacted form of the opposing force. The surplus of n08 over n06 is the scene's argument.

      - slug: b01c11
        status: audited-r1-mechanical
        bones_file: theater/bones/b01-c11.md
        bones_count: 27
        substance_bone_gate_verdict: PASS
        substance_delta_measured:
          axes_moved:
            social_tether-prot-rise: "+1.0 (flat 6 +0.5 + flat 25 +0.5)"
            social_tether-antag: "+1.0 (flat 16 +0.5 + flat 20 +0.5)"
            political_register-world: "+0.5 (flat 11 +0.5)"
          density_measured: "0 chatter / 27 (fully structural — 5 moving + 22 held)"
          felt_verdict: SUBSTANCE-FELT-3-of-3
        bones_review:
          reviewed_at: 2026-06-02T22:30:00Z
          report_path: active-project/staff/reviews/bones-b01c11-2026-06-02.md
          verdict: PASS
          follow_check: PASS-WITH-NOTES
          aliveness_note: "BONES-AIRLESS-RISK (qualified) — grounding spine present (stylus/source-field, iron-dish, feed-station, biological feed-relay) but silent feed-POV + apparatus/proper-noun load + four near-identical arm-close lines are aliveness pressure points; forewarns /and-facets Phase 2.5 aliveness scrutiny + grounding-ledger + /and-stitch Phase 4 voice-embodiment priority"
          bones_file_mtime_at_review: 1780441115
          stale_since: null
          carry_to_facets_phase_2_5:
            - "s02 burn (@11) needs DREAD register the bones do not carry — Phase 4 voice-embodiment + grounding-ledger @13/@14"
            - "s02 @16 the Dragonstone/Rhaenyra MEANING of the timestamp-withhold is not bone-recoverable — exposition/memory/NI facet must orient the Dragonstone-distance irony WITHOUT Taylor naming it on-page"
            - "s03 Halvard-slot-absence legibility-as-absence is 100% facet/context-dependent (a structural absence is invisible at pure bone level) — memory/NI facets carry the 'argument not reached for' read; highest-risk facet item"
            - "grounding-ledger lines anticipated on @13/@14 (feed-relay) and the @19-@21 packet cycle (ABSTRACTION-DOMINANT s03 carry from bone-gate)"
            - "s02 ABSTRACTION-DOMINANT (grounding 2/thr 3) + s03 ABSTRACTION-DOMINANT (grounding 1/thr 2) accept-with-rationale from bone-gate — reinforce physical materiality of burn + iron-dish + packet-cycle"
            - "chunk_cold_read SHIPPED-WITH-RISK-RECORDED (DEC-0072): design-inherent low-jeopardy + cold-context proper-noun load (Otto/Rhaenyra/Dragonstone/Corwick/Halvard) — arms /and-stitch P8.5 Check 3 + P9 jeopardy-scrutiny"
        chunk: |
          The consequences of formalization arrive. Taylor's social_tether-prot-rise
          crystallizes at its near-peak: she now has active relationships with Jarvis as
          a structural conduit, Oswyn as an unknowing node, a half-dozen ward contacts who
          feed her information because she has helped them, and an arrangement with Otto
          that functions as institutional cover without being institutional. She also receives
          her first Rhaenyra-pressure signal: through a Black-faction figure still in KL
          (a minor cloth merchant who serves as a passive intelligence node for the Blacks),
          Taylor's insect-feed catches a conversation fragment that suggests Dragonstone has
          become aware that the logistics thread was cut. The cloth merchant's behavior
          changes — he burns a message rather than carrying it. Taylor routes nothing of this
          to Jarvis. The political_register-world ticks up as the Green apparatus uses the
          courier detention to consolidate a succession-relevant information channel. The
          chapter's collision: the social tether is now load-bearing in full and Taylor has
          simultaneously begun withholding from Otto more consistently — she is protecting
          her withheld observations the way she is protecting Wren, without naming either act
          as protection. What shifts: social_tether-prot-rise peaks, social_tether-antag
          advances, political_register-world increments.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - axis: social_tether-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl03b
              notes: "tether crystallizes at near-peak; Jarvis, Oswyn, ward contacts, and arrangement all load-bearing; cl03b future-cost collateral now fully priced"
            - axis: social_tether-antag
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl-antag-d10
              notes: "non-extractable confirmation advances; Otto's leverage structural; Taylor's withholding pattern emerging but not yet noticed by Otto"
            - axis: political_register-world
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "courier detention leveraged by Green apparatus for succession-channel consolidation; world-axis ticks up"
          axes_held:
            - axis: position-prot-rise
              rationale: "position at near-peak; no new formalization event; holds at 4.5"
            - axis: relational_anchor_status
              rationale: "Wren in coverage; anchor at 3.5; no new weight this chapter"
            - axis: moral_framework
              rationale: "withholding from Otto is not logged as a breach in Taylor's accounting; framework holds at current level"
            - axis: political_register-prot
              rationale: "Rhaenyra-pressure signal is intelligence content; does not directly advance contempt register this chapter — that processing is b01c13"
          density_target: 0.6-0.8
          chapter_class: standard
        dramatic_shape: rising
        goal: |
          Show the audience the social tether at full load — all nodes visible, all relationships legible — and the first Rhaenyra-pressure signal arriving mediated through the cloth merchant, so the Dragonstone-distance irony is in view.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "courier detained: Dance-pressure pulse 1 complete"
            - "arrangement formal: function named"
            - "cf-rhaenyra-pressure staging: Dragonstone-adjacent consequences pending"
            - "Wren: anchor rank 3.5; in coverage"
            - "non-extractable confirmation: in progress"
          world_state:
            - "KL 122 AC; arrangement formalized; position-world rank 7; political_register-world rank 7"
          character_state:
            - "Taylor: position-prot-rise rank 4.5; social_tether-prot-rise rank 4; social_tether-antag rank 6; moral_framework rank -1; moral_legibility rank 5.5"
            - "Otto: leverage structural post-formalization"
          source_chapter: b01c10
        handoff_out:
          open_threads:
            - "social tether at near-peak: Jarvis, Oswyn, ward contacts, arrangement all load-bearing"
            - "cf-rhaenyra-pressure: cloth merchant burns message; Dragonstone aware courier thread was cut; Taylor withholds from Jarvis"
            - "withholding-from-Otto pattern: emerging; two withheld observations in succession"
            - "Wren: anchor rank 3.5; in coverage"
            - "Halvard: counter-argument thinning in Taylor's engagement"
          world_state:
            - "KL 122 AC; Green succession channel consolidated post-courier-detention; political_register-world rank 7.5"
            - "Rhaenyra-pressure: Dragonstone aware of the logistics cut; mediated, not direct"
          character_state:
            - "Taylor: social_tether-prot-rise rank 5; social_tether-antag rank 7; political_register-world advancing; moral_framework rank -1"
            - "cloth merchant: passive Black-faction node; Taylor withholds observation"
          target_chapter: b01c12
        # /and-substance chapter b01c11 Phase 6 persist 2026-06-02. Phase 5: audience 3/3 SUBSTANCE-FELT (cape-fic/dark-fantasy/worm-canon); auditor 0 HARD/2 SOFT (folded: s02 antag accumulated-partial reframe + position-prot-rise held on all 4 scenes); dramatist REVISE(attempt1 inert-stretch s03/s04)->ACCEPT(attempt2). Phase 5.5 cold-read CONTINUE=No both attempts -> admin DEC-0072 P (design-inherent low-jeopardy + cold-context; carries to /and-stitch P8.5+P9). Both HARD threading-holds resolved at Phase 3 (DEC-0071): pl-2026-06-02-stitch-thread-001 Halvard FORECLOSE@c13, -002 cl-d06 2nd tranche RE-WINDOW@c12.
        scenes:
          - slug: b01c11s01
            seq: 1
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              The morning circuit runs at full load without requiring Taylor to call it full.
              [event: jarvis-channel-operating-at-structural-load] Jarvis takes the packet at the
              second bell and walks. He does not look at Taylor when he takes it. He reads the
              covering sheet in the lane-mouth, folds it once, and is gone before the bell's decay
              ends. [image: jarvis-packet-exchange-as-structural-procedure] The channel functions
              the way load-bearing functions: without ceremony, because the weight has been there
              long enough that neither party comments on it. [mechanism:
              jarvis-as-conduit-structural-not-transactional]

              Oswyn is at the grain-measures junction by midday. [event:
              oswyn-visible-at-ward-junction-in-feed] Two carters are disputing the weight of a
              delivery and Oswyn is between them, one hand on each cart-frame, applying the
              particular pressure of a man who will not let this become a Watch matter. [image:
              oswyn-at-junction-weight-dispute-as-ward-function] He does not know Taylor's
              insect-feed has a coordinate for him — a baseline reading from a hundred prior
              circuits, against which today's variation marks clean. [force:
              oswyn-as-unknowing-node-at-ward-baseline] Taylor reads the junction and moves. She
              does not contact him. [mechanism: oswyn-node-operational-without-contact]

              The wool-dyer at the cross-lane brought Taylor the cart-timing change two days ago.
              [event: ward-contact-feeds-observation-without-prompting] The salt-seller at the
              water-gate brought the distribution-run shift a week before that. A warden's wife
              from the lower Hook precinct came three days back with word about a household using
              the wrong drain. [event: second-ward-contact-feeds-observation] They did not know
              they were feeding a coverage map. They came back because Taylor had done useful things
              for them — cleared the blocked drain, confirmed a household was not sick, been present
              without demanding payment — and returning with a piece of information is what people
              who owe a small debt do. [mechanism:
              ward-contacts-as-load-bearing-nodes-through-prior-service-reciprocity]

              Taylor routes the cart-timing change through the Jarvis channel. [event:
              wool-dyer-identity-withheld-from-deliverable-as-discrete-act] She sets the stylus to
              the source field. Her hand holds there. She writes the lane-pattern — the timing
              anomaly sourced to the cross-lane corridor, no name. The wool-dyer's name stays in
              the internal record and not on the covering sheet. Her hand lifts. [image:
              hand-pauses-over-source-field-writes-lane-pattern-not-name] [mechanism:
              identity-withheld-by-physical-omission-not-deliberated-choice] The decision is not
              deliberated. The contact is a contact, not a channel deliverable. [force:
              ward-contact-identity-withheld-from-channel]
            scene_conflict:
              protagonist_force: "Taylor's coverage-circuit discipline — the nodes run; the packet goes to Jarvis; Oswyn is at his junction; the contacts return observation through prior-service reciprocity; the tether carries load without being named"
              opposing_force: "the load the tether is already carrying — each node (Jarvis as structural conduit, Oswyn as unknowing coordinate, three ward contacts operating through service debt) is doing work Taylor did not fully design; the tether functions beyond any single operational choice"
              stakes_axis: social_tether-prot-rise
            substance_delta:
              axes_in_motion:
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl03b
                  notes: |
                    cl03b first tranche this chapter (+0.5 of +1.0). Tether crystallizes at near-peak
                    through enacted nodes doing load-bearing work simultaneously: Jarvis as structural
                    conduit (packet taken without ceremony), Oswyn as unknowing ward-junction baseline
                    (operational without contact), ward contacts feeding back through prior-service
                    reciprocity (not design). Crystallization is not a formalization event — it is the
                    tether operating at the load that formalization confirmed at c10. The wool-dyer
                    identity withhold is a discrete physical act (hand pauses over source field, writes
                    lane-pattern, lifts) — enacted as substrate discipline, not deliberated as a breach.
              axes_held:
                - axis: social_tether-antag
                  rationale: "Jarvis channel operates but no new Otto leverage event in this scene; antag-axis advances belong to s02 and s03; holds at rank 5"
                - axis: political_register-world
                  rationale: "no Green succession-channel content this scene; world-axis advance belongs to s02; holds at rank 6"
                - axis: moral_framework
                  rationale: "ward circuit is consolidation-mode; the wool-dyer identity withheld is the same substrate discipline as prior chapters; no new licensed exception or named breach; holds at rank -1 by Taylor's accounting"
                - axis: relational_anchor_status
                  rationale: |
                    Wren is not in this morning's circuit content; anchor holds at rank 3.5.
                    HARD PARKING-LOT RESOLUTION (pl-2026-06-02-stitch-thread-002 / cl-d06 second +1.0
                    tranche): relational_anchor_status held FLAT all four scenes per chapter contract.
                    Second cl-d06 +1.0 tranche RE-WINDOWED to b01c12 (DEC-0071): b01c12 Phase 3 anchors
                    relational_anchor_status +1.0 with cost_ledger_anchor: cl-d06. Re-windowed, not abandoned.
                - axis: moral_legibility_to_self
                  rationale: "ward circuit is consolidation; no new recognition event; legibility holds at rank 5.5"
                - axis: political_register-prot
                  rationale: "no court-tier content in this circuit; resentment does not advance; holds at rank 3.5"
                - axis: position-prot-rise
                  rationale: "rise-phase peak confirmed at d10; no further delta this chapter; the arrangement-as-cover events are downstream of the already-established position, not new position-movement"
            density_target: 0.60-0.75
            # /and-write b01c11 Phase 7 emit 2026-06-02. Silent chapter (no dialogue-anchor bones). Bone-gate PASS: auditor 0 HARD / 2 ABSTRACTION-DOMINANT SIGNAL (s02,s03) accept-with-rationale -> /and-stitch P4; audience 3/3 SUBSTANCE-FELT all 4 scenes; Earth-Bet fence CLEAN; 27 KEEP/0 DELETE. Form-watch advisories (abstract-datum objects @4/@18; receives @12; marks @16 per b01c09 precedent) carried to stitch. chunk_cold_read SHIPPED-WITH-RISK-RECORDED (DEC-0072) arms /and-stitch P8.5+P9.
            bones:
              - slug: b01c11s01n01
                flat_id: 1
                svo: "jarvis-coin-kl-courier takes the packet"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "channel operating at load — tether-weight shown via node action"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s01n02
                flat_id: 2
                svo: "jarvis-coin-kl-courier folds the covering-sheet"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "ceremony-free fold-and-gone — tether load accumulates without contact"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s01n03
                flat_id: 3
                svo: "oswyn-mudway-flea-bottom-elder presses the cart-frame"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "Oswyn occupying ward-function at junction — tether node visible without contact"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s01n04
                flat_id: 4
                svo: "the wool-dyer returns the cart-timing observation"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "unprompted debt-service return — tether circuit operating"
                gate_verdict:
                  bonefide: true
                  flat: false
                # form-watch advisory: abstract-datum object ("the cart-timing observation") — carried to /and-stitch P4
              - slug: b01c11s01n05
                flat_id: 5
                svo: "taylor-hebert-kl-122ac sets the stylus to the source-field"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-antag
                      rationale: "withhold initiated — discrete omission act; antag held flat"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s01n06
                flat_id: 6
                svo: "taylor-hebert-kl-122ac writes the lane-pattern"
                substance_delta:
                  axis_moves:
                    - axis: social_tether-prot-rise
                      direction: up
                      magnitude: 0.5
                  axes_held: []
                cost_ledger_anchor: cl03b
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s01n07
                flat_id: 7
                svo: "taylor-hebert-kl-122ac lifts the stylus"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_framework
                      rationale: "withhold complete — wool-dyer name stays in internal record; omission closed as bodily fact"
                gate_verdict:
                  bonefide: true
                  flat: false

          - slug: b01c11s02
            seq: 2
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              The cloth merchant at the Hook's south end has been in Taylor's coverage grid for six
              months. [event: cloth-merchant-as-passive-black-faction-node-observed] His shop sits
              at the junction where two cross-lanes meet and the insect-feed runs cleanly. The
              merchant's behavior is legible in the feed: bolt-counts in the morning,
              delivery-receipt in the early afternoon, the door shut before dark. [image:
              cloth-merchant-routine-pattern-as-feed-baseline] There has been one element of his
              daily pattern Taylor has not routed to the Jarvis channel: the occasional short visitor
              who comes at off-hours and stays less time than it takes to transact cloth. [force:
              cloth-merchant-as-passive-black-faction-node-unrouted] The visits have been
              infrequent. Taylor classified them as personal traffic and held them in the internal
              record.

              This morning one of the off-hour visitors comes and goes in under ten minutes. [event:
              black-faction-messenger-visits-cloth-merchant] What the feed returns after the visitor
              leaves: the merchant at his back worktable holding a folded paper — not a bolt-ticket,
              not a measure-slip, a folded paper with the geometry of something sealed and now opened.
              [image: merchant-holds-folded-paper-at-worktable] The small iron dish on the corner of
              his worktable receives the paper and the rushlight flame [event: cloth-merchant-burns-message]
              catches it. [mechanism: message-burned-in-iron-dish-caught-by-insect-feed-thermal-and-smoke]
              The feed returns the thermal shift and the smoke-curl through the insects in the
              worktable's ambient zone — three seconds; the paper is gone. [mechanism:
              burn-legible-to-taylor-through-feed-thermal-and-smoke-signature] The merchant's hands
              move to the bolt-ticket on the hook beside him as though nothing has interrupted the
              morning's work. [image: merchant-returns-to-bolt-ticket-as-practiced-recovery]

              The courier thread that ran through this shop was moving until three days ago. [event:
              black-faction-logistics-thread-at-cloth-merchant-broken] The thread was cut at the
              Corwick end — at the lower gate, at the detainment the feed returned. [force:
              dragonstone-logistics-channel-broken-because-corwick-detained] What the burn tells
              Taylor: Dragonstone has learned the logistics thread was cut, and it has responded by
              going dark at this node rather than rerouting through it. [event:
              dragonstone-aware-of-courier-thread-interruption] The burn is not improvised — the
              merchant has done this twice before at the same interval between receipt and burn, which
              means the instruction predates the current interruption. [mechanism:
              burn-as-standing-black-faction-protocol-not-improvised-response] [image:
              burn-timing-as-evidence-of-standing-protocol]

              Taylor timestamps the observation and holds it in the internal record. [force:
              taylor-withholds-rhaenyra-signal-from-jarvis] [event:
              dragonstone-distance-irony-weight-felt-at-timestamp] The thread Taylor's architecture
              cut has been noticed at Dragonstone before Taylor has processed what it means that
              Dragonstone noticed. Whatever moves on the Rhaenyra side of the logistics gap is moving
              without a signal returning to King's Landing — and that absence is not a gap in Taylor's
              coverage, it is the gap the cut created. [image:
              war-pressure-weight-of-absent-signal-as-single-felt-register] Taylor files it and
              moves. [mechanism: threat-weight-registered-in-taylor-pov-not-processed-as-exposition]
            scene_conflict:
              protagonist_force: "Taylor's feed-reading discipline — the merchant is in coverage; the burn is a thermal event the feed returns; the pattern-analysis runs on what the feed gives"
              opposing_force: "the message burn as intelligence signal — the burn confirms Dragonstone-awareness of the cut thread; what Taylor has observed is the first Rhaenyra-pressure signal the coverage grid has returned; routable content she does not route; the weight of what the cut thread implies for the war-state arrives before Taylor can process it"
              stakes_axis: political_register-world
            substance_delta:
              axes_in_motion:
                - axis: political_register-world
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: null
                  notes: |
                    Green apparatus courier detention (c10) has produced a measurable Black-faction
                    reaction observable in Taylor's feed: the cloth merchant burns a message rather than
                    carrying it, confirming the logistics thread is known to be cut on the Dragonstone
                    side. The Green succession channel's consolidation event at c10 now has a world-state
                    consequence visible in the coverage grid. Taylor observes this as world-state through
                    the feed; she does not route it. The Dragonstone-distance irony is in view: the
                    courier thread Taylor's architecture cut has been noticed at Dragonstone before
                    Taylor has processed what that means operationally. The threat-flicker (what the
                    absent signal implies for war-pressure) lands as a single felt register in Taylor's
                    POV — not processed as exposition, filed and moved from. political_register-world ticks up.
                - axis: social_tether-antag
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl-antag-d10
                  notes: |
                    cl-antag-d10 FIRST TRANCHE this chapter (+0.5 of +1.0 chapter total; accumulated-partial).
                    Taylor withholds the Rhaenyra-pressure signal from Jarvis — a second consecutive
                    withheld observation following the wool-dyer identity from s01. Substrate split now
                    covers two distinct categories. This is accumulated-partial substrate-split accrual:
                    the cl-antag-d10 gain is a substrate-accumulation advance toward Otto's structural
                    leverage; Otto is not on-page in this scene; the leverage advances because the withheld
                    category-count is widening, not because Otto has demonstrated or completed any leverage
                    act. Non-extractable confirmation in progress.
              axes_held:
                - axis: social_tether-prot-rise
                  rationale: "no new patron-adjacent node event in this scene; tether holds at rank 7.5 after s01 advance"
                - axis: moral_framework
                  rationale: "the withholding is enacted as substrate discipline, not named as a breach; merchant's burn filed in internal record without opening a new ledger entry; holds at rank -1"
                - axis: relational_anchor_status
                  rationale: "no Wren content in this scene; anchor holds at rank 3.5"
                - axis: political_register-prot
                  rationale: "the Dragonstone-awareness signal is world-state observation through the feed; produces no new contempt-register color this scene — that processing belongs to b01c13; holds at rank 3.5"
                - axis: moral_legibility_to_self
                  rationale: "Taylor reads the burn, classifies it, withholds it; no recognition event; legibility holds at rank 5.5"
                - axis: position-prot-rise
                  rationale: "rise-phase peak confirmed at d10; no further delta this chapter; the arrangement-as-cover events are downstream of the already-established position, not new position-movement"
            density_target: 0.65-0.80
            # ABSTRACTION-DOMINANT SIGNAL accepted-with-rationale: grounding count 2 / threshold 3 — carried to /and-stitch Phase 4 for physical-materiality reinforcement.
            bones:
              - slug: b01c11s02n01
                flat_id: 8
                svo: "the cloth-merchant opens the back-worktable"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: political_register-world
                      rationale: "merchant's bolt-count morning routine legible — world-state context before anomaly"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s02n02
                flat_id: 9
                svo: "the messenger crosses the shop-threshold"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-antag
                      rationale: "off-hour visitor pattern — held in internal record; withheld-category accumulating"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s02n03
                flat_id: 10
                svo: "the cloth-merchant lifts the folded-paper"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: political_register-world
                      rationale: "sealed-then-opened geometry in feed — world-state observation before central event"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s02n04
                flat_id: 11
                svo: "the cloth-merchant burns the paper"
                substance_delta:
                  axis_moves:
                    - axis: political_register-world
                      direction: up
                      magnitude: 0.5
                  axes_held: []
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s02n05
                flat_id: 12
                svo: "the iron-dish receives the ash"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: political_register-world
                      rationale: "burn complete — physical closure of central event; dish is aftermath anchor"
                gate_verdict:
                  bonefide: true
                  flat: false
                # form-watch advisory: stative-adjacent ("receives") — carried to /and-stitch P4
              - slug: b01c11s02n06
                flat_id: 13
                svo: "the insect-feed returns the thermal-shift"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-antag
                      rationale: "biological relay confirms burn — thermal datum through insects in worktable ambient zone"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s02n07
                flat_id: 14
                svo: "the insect-feed carries the smoke-curl"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-antag
                      rationale: "second relay datum — smoke-curl confirms completion; feed detection bandwidth shown"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s02n08
                flat_id: 15
                svo: "the cloth-merchant squares the bolt-ticket"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: political_register-world
                      rationale: "merchant returns to routine — standing protocol complete; morning continues"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s02n09
                flat_id: 16
                svo: "taylor-hebert-kl-122ac marks the timestamp"
                substance_delta:
                  axis_moves:
                    - axis: social_tether-antag
                      direction: up
                      magnitude: 0.5
                  axes_held: []
                cost_ledger_anchor: cl-antag-d10
                gate_verdict:
                  bonefide: true
                  flat: false
                # form-watch advisory: instrument-class ("marks") — per b01c09 precedent; carried to /and-stitch P4

          - slug: b01c11s03
            seq: 3
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              A ward contact returns at the early-afternoon mark — one of the warden's-precinct
              informants, the woman who works the lower Hook's soap-rendering lane and whose eyes
              track movement at the lane-mouth the way someone trained to it would track movement.
              [event: ward-contact-returns-with-actionable-observation] She brings word of a
              household receiving nighttime visitors through the back-alley access — not the same
              household as the blocked-drain matter, a different address, a different access pattern.
              [image: soap-lane-contact-with-nighttime-visitor-report] The observation is
              route-ready: the kind of information Taylor would put into the Jarvis packet sourced
              to the precinct pattern.

              Six weeks ago Taylor would have run the compound-corruption mechanism against this
              observation first. [event: halvard-mechanism-not-reached-for-at-routing-decision]
              The Halvard argument built a slot in Taylor's operational sequence: take the contact's
              observation, hold it against the corruption frame — feel where the counter held and
              where the argument held back, keep both accountings before routing. [mechanism:
              halvard-argument-as-operational-slot-formerly-present-in-sequence] Taylor reaches
              the routing decision. [force: halvard-slot-absent-from-operational-sequence] The slot
              is not there. She does not reach for it and find it missing — she simply routes. The
              contact's observation goes into the packet sourced to the precinct pattern. The
              nighttime-visitor address is a deliverable. The contact's name stays in the internal
              record. [image: routing-decision-completes-without-halvard-slot-as-behavioral-fact]
              [mechanism: halvard-argument-inactive-in-taylors-operational-register-not-refuted]

              The argument is not defeated. Taylor has not found a flaw in its internal structure.
              [force: halvard-argument-thinning-as-absence-not-refutation] It has stopped being the
              instrument she reaches for when the circuit produces an operational judgment. That is
              a different thing — and Taylor does not examine whether it is a better or worse thing,
              because the packet needs the precinct-pattern sourcing completed and the afternoon
              circuit is not finished. [image:
              operational-momentum-carries-past-halvard-absence-without-examination]
            scene_conflict:
              protagonist_force: "Taylor's operational momentum — the contact's observation is route-ready; the routing decision runs; the packet gets the precinct-pattern sourcing; the circuit does not pause"
              opposing_force: "the Halvard slot's absence — Taylor reaches the routing decision and the compound-corruption mechanism is simply not in the sequence; the reader can see the shape of what is missing even as Taylor moves past it; the withhold of the contact's name completes without the counter-pressure that shaped the prior five weeks of circuit-work"
              stakes_axis: social_tether-antag
            substance_delta:
              axes_in_motion:
                - axis: social_tether-antag
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl-antag-d10
                  notes: |
                    cl-antag-d10 SECOND TRANCHE this chapter (+0.5 of +1.0, completing chapter +1.0
                    total; accumulated-partial). The withholding pattern across consecutive observations
                    is now structural and the Halvard check — the only internal mechanism that was
                    testing the substrate discipline's legitimacy — is absent from the operational
                    sequence. The ward-contact routing event dramatizes this in action: Taylor reaches
                    the slot and the slot is not there; she routes without the compound-corruption test.
                    Otto's leverage accumulates because the internal check is gone from the sequence,
                    not because Otto has demonstrated leverage — this is substrate-accumulation advance,
                    accumulated-partial, non-extractable confirmation in progress.
              axes_held:
                - axis: social_tether-prot-rise
                  rationale: "the arrangement-as-cover is operational continuity of an existing structure, not a new tether node; tether holds at rank 7.5"
                - axis: political_register-world
                  rationale: "world-axis advance completed at s02; no additional Green succession-channel event this scene; holds at rank 6.5"
                - axis: moral_framework
                  rationale: "the routing decision does not enter Taylor's ledger as a breach; the Halvard thinning is not a named licensed exception; holds at rank -1"
                - axis: relational_anchor_status
                  rationale: "Wren is not in the operational-pattern content; anchor holds at rank 3.5"
                - axis: moral_legibility_to_self
                  rationale: |
                    The Halvard slot's absence is a behavioral fact Taylor does not examine — she routes
                    and the circuit continues; no recognition event fires; legibility holds at rank 5.5.
                    HARD PARKING-LOT RESOLUTION (pl-2026-06-02-stitch-thread-001 / hook-0007 / Halvard):
                    FORECLOSE-designated at c13 (DEC-0071). Thinning enacted in this scene (argument
                    inactive in operational register, not refuted; dramatized as absent slot at routing
                    decision). Foreclosure-as-axis-event lands at b01c13 (contempt-articulation).
                    Status: foreclosed-at-c13; thinning carried as handoff.
                - axis: political_register-prot
                  rationale: "the Halvard argument becoming inactive is a legibility-register event, not a contempt-register event; the thinning does not advance contempt toward its d09 articulation this chapter; holds at rank 3.5"
                - axis: position-prot-rise
                  rationale: "rise-phase peak confirmed at d10; no further delta this chapter; the arrangement-as-cover events are downstream of the already-established position, not new position-movement"
            density_target: 0.60-0.75
            # ABSTRACTION-DOMINANT SIGNAL accepted-with-rationale: grounding count 1 / threshold 2 — carried to /and-stitch Phase 4 for physical-materiality reinforcement.
            bones:
              - slug: b01c11s03n01
                flat_id: 17
                svo: "the soap-lane-contact crosses the cross-lane"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-antag
                      rationale: "contact returns — route-ready observation incoming; antag-leverage node active"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s03n02
                flat_id: 18
                svo: "the soap-lane-contact delivers the nighttime-visitor report"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-antag
                      rationale: "observation arrives — back-alley night-access household; route-ready datum"
                gate_verdict:
                  bonefide: true
                  flat: false
                # form-watch advisory: abstract-datum object ("the nighttime-visitor report") — carried to /and-stitch P4
              - slug: b01c11s03n03
                flat_id: 19
                svo: "taylor-hebert-kl-122ac opens the packet"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "routing decision begins — prepares to source observation to precinct-pattern"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s03n04
                flat_id: 20
                svo: "taylor-hebert-kl-122ac writes the precinct-pattern sourcing"
                substance_delta:
                  axis_moves:
                    - axis: social_tether-antag
                      direction: up
                      magnitude: 0.5
                  axes_held: []
                cost_ledger_anchor: cl-antag-d10
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s03n05
                flat_id: 21
                svo: "taylor-hebert-kl-122ac seals the packet"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_legibility_to_self
                      rationale: "Halvard-foreclose sealed into packet — argument not defeated, not reached for; packet closes before the question surfaces"
                gate_verdict:
                  bonefide: true
                  flat: false

          - slug: b01c11s04
            seq: 4
            status: scened
            pov_narrator: taylor-hebert-kl-122ac
            chunk: |
              Taylor closes the evening circuit at the feed-station and runs the count. [event:
              evening-accounting-runs-full-tether-count] The count runs in the order the circuit
              ran it: Jarvis first. [image: jarvis-packet-sealed-and-set-in-count-sequence] The
              packet is sealed. The Jarvis channel returned everything it was given and carried it
              upward without ceremony, which is the only way the channel functions. That entry closes.
              [mechanism: jarvis-as-structural-conduit-confirmed-in-motion-not-catalog]

              Oswyn second. [event: oswyn-ward-node-confirmed-in-count-sequence] The junction
              presence today was calibration-clean — the weight dispute resolved before it became a
              Watch matter, the ward's social temperature holding at the baseline the feed has
              indexed across a hundred prior circuits. Taylor did not contact him. The circuit does
              not require contact when the baseline holds. That entry closes. [image:
              oswyn-at-junction-as-ward-temperature-marker-closing-in-count]

              The contacts third. [event: ward-contacts-confirmed-in-count-sequence] The
              warden's-precinct informant. The soap-lane woman who brought the nighttime-visitor
              report. The wool-dyer two days prior. Each one returned observation through the prior-
              service debt that Taylor did not design but did not stop accruing. Each observation
              routed to the packet — sourced to the pattern, not the person. Each name in the
              internal record. That entry closes. [mechanism:
              contacts-confirmed-as-load-bearing-nodes-through-service-reciprocity-in-motion]

              The arrangement last. [event: otto-arrangement-confirmed-in-count-sequence] The
              cover held today the way it held yesterday: the ward-elder's accounting for Taylor's
              presence was the woman who does useful things in the ward, operating in her range.
              No patron visible above her. No structure traceable behind her. The cover does not
              know what it contains. That entry closes. [force:
              all-four-tether-nodes-simultaneously-load-bearing] [mechanism:
              tether-crystallization-as-simultaneous-load-across-all-four-nodes]

              Two withheld observations in the internal record, not in the packet. [event:
              two-withheld-observations-in-internal-record-at-chapter-close] Neither substrate
              knows what the other is not receiving. [mechanism:
              substrate-split-makes-withholding-invisible-as-chapter-close] [image:
              full-tether-count-as-chapter-close-image] The stylus goes down. [image:
              stylus-down-as-chapter-close]
            scene_conflict:
              protagonist_force: "Taylor's end-of-day accounting discipline — each node confirmed in sequence as the count runs; the packet is sealed; the internal record is current; the accounting closes without labeling any entry as a withholding act"
              opposing_force: "the completed count as a shape — all four tether nodes load-bearing simultaneously, the arrangement as institutional cover for the other three, the two withheld observations in the internal record: the Dragonstone-distance irony in view at chapter close; the tether at full load and the withholding pattern both present in the same evening accounting"
              stakes_axis: social_tether-prot-rise
            substance_delta:
              axes_in_motion:
                - axis: social_tether-prot-rise
                  direction: up
                  target_delta_magnitude: 0.5
                  cost_ledger_anchor: cl03b
                  notes: |
                    cl03b second tranche this chapter (+0.5 of +1.0, completing chapter total).
                    social_tether-prot-rise -> rank 8, near-peak confirmed. Crystallization completes at
                    chapter close: all four nodes confirmed in Taylor's evening count as the count runs
                    — each node closing in sequence, not enumerated as a catalog. Taylor files it as
                    operational state without naming it as a peak. cl03b future-cost collateral note:
                    rank 8 is the full cl03b gain; the -7 at cl07a begins at d10+ (collapse phase not
                    yet open this chapter).
              axes_held:
                - axis: social_tether-antag
                  rationale: "evening accounting makes the withholding pattern visible but Otto is not on-page; no new leverage event; holds at rank 6 after s02 and s03 advances. NOTE: pl-2026-06-02-002 (cl-antag-d10 journey-required cl04 dependency) remains open; this chapter's +1.0 total advances the partial-settle but the cl04 relational_anchor_status non-extractable component remains in-progress per chapter contract"
                - axis: political_register-world
                  rationale: "world-axis advance completed at s02; holds at rank 6.5 through chapter close"
                - axis: moral_framework
                  rationale: "evening accounting closes without entering either withhold as a breach; substrate split is the discipline at work; holds at rank -1"
                - axis: relational_anchor_status
                  rationale: "Wren's route is indexed in the internal record; no new weight this scene; anchor holds at rank 3.5; re-window to b01c12 confirmed per s01 parking-lot resolution"
                - axis: moral_legibility_to_self
                  rationale: "the count closes with all nodes enumerated and neither the withholding pattern nor the protection logic named on-page; no recognition event; legibility holds at rank 5.5"
                - axis: political_register-prot
                  rationale: "no court-tier content in evening accounting; resentment does not advance; holds at rank 3.5"
                - axis: position-prot-rise
                  rationale: "rise-phase peak confirmed at d10; no further delta this chapter; the arrangement-as-cover events are downstream of the already-established position, not new position-movement"
            density_target: 0.65-0.80
            bones:
              - slug: b01c11s04n01
                flat_id: 22
                svo: "taylor-hebert-kl-122ac enters the feed-station"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "evening circuit at feed-station — accounting-in-motion opens"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s04n02
                flat_id: 23
                svo: "taylor-hebert-kl-122ac closes the Jarvis entry"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "Jarvis arm: packet sealed / channel returned everything / carried upward; arm complete"
                gate_verdict:
                  bonefide: true
                  flat: false
                # s04n23-26 "closes the X entry" is intentional accounting-refrain — NOT mannerism
              - slug: b01c11s04n03
                flat_id: 24
                svo: "taylor-hebert-kl-122ac closes the Oswyn entry"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "Oswyn arm: junction clean / dispute below Watch threshold / ward baseline; arm complete"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s04n04
                flat_id: 25
                svo: "taylor-hebert-kl-122ac closes the contacts entry"
                substance_delta:
                  axis_moves:
                    - axis: social_tether-prot-rise
                      direction: up
                      magnitude: 0.5
                  axes_held: []
                cost_ledger_anchor: cl03b
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s04n05
                flat_id: 26
                svo: "taylor-hebert-kl-122ac closes the arrangement entry"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: moral_framework
                      rationale: "cover holds (ward-elder accounting = useful-things-woman, no patron visible); closes without moral-framework movement"
                gate_verdict:
                  bonefide: true
                  flat: false
              - slug: b01c11s04n06
                flat_id: 27
                svo: "taylor-hebert-kl-122ac sets the stylus down"
                substance_delta:
                  axis_moves: []
                  axes_held:
                    - axis: social_tether-prot-rise
                      rationale: "crystallization-complete closing image — stylus rests; chapter accounting done"
                gate_verdict:
                  bonefide: true
                  flat: false

        chunk_cold_read:
          reviewed_at: 2026-06-02T22:00:00Z
          verdict: SHIPPED-WITH-RISK-RECORDED
          classification: B
          recovered_summary: "A spy-bug network runs a flawless day; operator notes it's working, withholds two things, tidies up."
          intended_goal: "social tether at full load — all nodes visible — + first Rhaenyra-pressure signal mediated through the cloth merchant (Dragonstone-distance irony)"
          continue: no
          continue_strict: no
          attempts: 2
          report_path: active-project/staff/reviews/chunk-coldread-b01c11-2026-06-02.md
          disposition: P
          dispositioned_at: 2026-06-02T22:00:00Z
          dispositioned_by: admin   # DEC-0072
          cold_read_risk_carry: |
            CHUNK-CLASS-B / SHIPPED-WITH-RISK-RECORDED | b01c11 | strict-CONTINUE=No (attempt-2-post-revise) | risks: (1) low-on-page-jeopardy / design-inherent-RISING-between-CLIMAXes; (2) cold-context proper-noun load (Otto / Rhaenyra / Dragonstone / Corwick-detainment / Halvard-argument) — serial-mid-point context-noise, not in-chunk hole | arms: /and-stitch Phase 8.5 Check 3 (cold-context-risk) + Phase 9 jeopardy-scrutiny | consecutive-airless N=5 context: route to /and-cohere post-c11, not chunk-layer | DEC-0072

        handoff_conflicts:
          - detected_at: 2026-06-02T22:00:00Z
            axis: social_tether-prot-rise
            handoff_in_value: 4
            aggregate_value: 7
            resolution: aggregate-wins
            note: "book-author handoff_in prediction stale vs aggregate-state.md; scene ranks authored on aggregate basis per Phase 0 step 6c. +1.0 chapter delta -> rank 8 near-peak. See aggregate-state.md axis_state for full reconciliation."

      - slug: b01c12
        status: planned
        chunk: |
          The cost-bearer free-movement leverage beat at d08: Taylor's coverage map has a
          structural gap — the lanes east of the water-gate that Wren moves through daily but
          that Taylor cannot cover without positioning insects in locations that would trigger
          witch-label reactions. Wren's free movement through the gap is the coverage map's
          effective eastern boundary. Taylor has been routing around this gap for months. A
          new request from Otto demands coverage of precisely those lanes — a Black-faction
          courier-adjacent figure has been using them to pass messages. Taylor faces the
          collision directly: she can cover the gap by deploying insects in the witch-label-
          triggering locations (and accept the community-safety cost to Wren), or she can
          tell Otto the lanes are not accessible without explanation. She tells Otto the lanes
          are not accessible. The chapter also carries the irrevocable-Khepri-repetition
          marker: Taylor adds two more ward-clusters to coverage, and the aggregate scale of
          her insect architecture crosses the threshold where she cannot avoid the word
          Khepri in her own internal accounting. She suppresses it. What shifts: moral_
          framework down materially, relational_anchor_status up, social_tether-prot-rise
          reaches near-peak at 8, capability advances to full deployment.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - axis: moral_framework
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl05
              notes: "irrevocable-Khepri-repetition threshold crossed in Taylor's internal accounting; suppressed; systematic override at full scale; cl05 cost side"
            - axis: capability
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl05
              notes: "full-deployment-and-load-bearing threshold crossed; two more ward-clusters; Khepri-rhyming architecture complete in scope; cl05 gain side"
            - axis: relational_anchor_status
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: [cl-d08, cl-d06]
              notes: "coverage gap = Wren structurally necessary to coverage map without entering the ledger; cl-d08 cost paid. SETTLEMENT (DEC-0071, re-window from pl-2026-06-02-stitch-thread-002): this +1.0 axis-move ALSO settles the outstanding cl-d06 2nd tranche (+1.0) that reached the end of its c08-c10 window unsettled while relational_anchor_status was held flat c08-c11. cl-d08 = mechanism; cl-d06 = debt; one axis-move settles both. Closes the cl-d06 partial-settle tracked since c06 (pl-2026-05-30-001)."
            - axis: social_tether-prot-rise
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: cl-d08b
              notes: "coverage gap consolidates tether; Wren's free movement in uncovered lanes closes the map without being in the architecture; cl-d08b"
            - axis: position-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl02
              notes: "withholding-from-Otto of the lane access moves position toward its non-exit confirmation; position approaching cl02 completion"
          axes_held:
            - axis: political_register-prot
              rationale: "the gap-refusal is a tactical decision, not a contempt-register event; Khepri-suppression is internal not feed-facing"
            - axis: moral_legibility_to_self
              rationale: "Khepri word is suppressed in accounting; legibility crack does not open fully this chapter; deferred to d10 suppression event"
            - axis: social_tether-antag
              rationale: "Otto's leverage structural but not advancing this chapter; the lane-refusal does not reduce it — Otto accepts the map boundary"
          density_target: 0.7-0.9
          chapter_class: standard
        dramatic_shape: climax
        goal: |
          Show the audience the gap, the choice, and the suppression — Taylor choosing Wren's safety over the deliverable without naming what she is doing — and the Khepri word surfacing and being pushed back down.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "social tether at near-peak"
            - "cf-rhaenyra-pressure: cloth merchant; Dragonstone aware"
            - "withholding-from-Otto pattern: two withheld"
            - "Wren: anchor rank 3.5; in coverage; daily pattern surveilled"
          world_state:
            - "KL 122 AC; political_register-world rank 7.5"
          character_state:
            - "Taylor: social_tether-prot-rise rank 5; social_tether-antag rank 7; capability rank 5; moral_framework rank -1; position-prot-rise rank 4.5"
          source_chapter: b01c11
        handoff_out:
          open_threads:
            - "coverage gap confirmed: east-of-water-gate lanes not in deliverable; Wren's free movement the effective map boundary"
            - "Khepri word suppressed in Taylor's accounting; irrevocable threshold named internally and closed"
            - "Black-faction courier-adjacent figure: still operational in the gap lanes; Otto notified of access limit"
            - "capability at full deployment: architecture complete in scope"
            - "Wren: anchor rank 4.5 (structurally necessary to coverage map without ledger entry)"
            - "non-extractable confirmation: social tether at near-peak 8; approaching cl-antag-d10 completion"
            - "Halvard: counter-argument thinning in Taylor's engagement"
          world_state:
            - "KL 122 AC; coverage at Khepri-rhyming scale; Flea Bottom and five wards fully mapped"
            - "Otto accepts coverage map with eastern gap; arranges alternate route for that channel"
          character_state:
            - "Taylor: capability rank 6 (full deployment); position-prot-rise rank 5.5; social_tether-prot-rise rank 5.5; relational_anchor_status rank 4.5; moral_framework rank -2; political_register-prot holding"
            - "Wren: structurally necessary to coverage map; anchor weight at 4.5; not in deliverable"
          target_chapter: b01c13

      - slug: b01c13
        status: planned
        chunk: |
          The articulated-contempt chapter. Two feed-events in the same week: a court
          provisioning dispute Taylor reads through compound eyes, in which a Green-faction
          household agent publicly humiliates a Flea Bottom supplier over a copper-penny
          margin; and a second faction-violence sub-pressure incident, where a suspected
          Black-faction sympathizer from the ward-elder list Taylor compiled at d06 is brought
          before a court-adjacent magistrate on a pretext charge. Taylor watches the
          magistrate proceeding through the feed — she has a fly in the hall — and her
          register shifts from diffuse resentment to something she can now name by name. She
          names it. Halvard appears for what is effectively his last substantive encounter:
          Taylor runs the counter-argument again but does not engage Halvard's response. She
          has the counter, she has named the contempt, and the counter is sufficient. She
          does not need Halvard's answer because the contempt does not change what she does
          next, and she knows it. What shifts: political_register-prot advances materially
          toward articulate-naming threshold; political_register-world ticks up; Halvard
          engagement foreclosed.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - axis: political_register-prot
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: null
              notes: "articulate-contempt threshold crossed; diffuse resentment becomes named by name; faction-violence sub-pressure incident (d07/d10/d12 cluster) and provisioning humiliation produce the naming event"
            - axis: political_register-world
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "ward-elder pretext charge: Green apparatus uses Taylor's d06 list operationally; world succession position advances through enforcement"
          axes_held:
            - axis: moral_framework
              rationale: "naming the contempt is not a breach event; framework holds at current crack-level"
            - axis: relational_anchor_status
              rationale: "Wren not in the feed events this chapter; anchor holds at 4.5"
            - axis: moral_legibility_to_self
              rationale: "contempt named = legibility is functioning, but recognition-of-repetition not yet opened; the contempt is directed outward, not yet at the ledger itself"
            - axis: social_tether-antag
              rationale: "Otto's leverage holds; Halvard foreclosure is Taylor-unilateral and does not affect the patron-lever"
          density_target: 0.6-0.8
          chapter_class: standard
        dramatic_shape: hinge
        goal: |
          Show the audience Taylor naming the contempt with precision and then demonstrating that naming changes nothing about what she does next — the contempt-without-refusal shape at its first appearance.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "coverage gap: east-of-water-gate; Wren free movement the boundary"
            - "Khepri word suppressed"
            - "capability at full deployment"
            - "Wren: anchor rank 4.5; structurally necessary"
            - "Halvard: counter-argument thinning"
            - "Black-faction courier-adjacent figure in gap lanes"
            - "non-extractable confirmation: social tether at near-peak 8; approaching cl-antag-d10 completion"
          world_state:
            - "KL 122 AC; coverage at scale; Green apparatus using Taylor's d06 list operationally"
            - "political_register-world rank 7.5"
          character_state:
            - "Taylor: capability rank 6; position-prot-rise rank 5.5; moral_framework rank -2; relational_anchor rank 4.5; political_register-prot rank 3.5 (articulation threshold approaching)"
          source_chapter: b01c12
        handoff_out:
          open_threads:
            - "contempt named by name: articulate-contempt threshold crossed; political_register-prot now at naming level"
            - "Halvard engagement foreclosed: Taylor has the counter, does not need the response"
            - "ward-elder pretext charge: Green enforcement visible; moral_framework consequence of d06 list delivery on-page"
            - "Wren: anchor rank 4.5; coverage gap holding"
            - "Black-faction courier-adjacent: still in gap lanes"
            - "cf-rhaenyra-pressure: Dragonstone consequences of courier detention propagating at remove"
          world_state:
            - "KL 122 AC; Green apparatus enforcement of ward-elder list visible in magistrate proceeding"
            - "political_register-world rank 8"
          character_state:
            - "Taylor: political_register-prot rank 5 (articulate-contempt); moral_framework rank -2; capability rank 6; relational_anchor rank 4.5"
            - "Halvard: present in Flea Bottom but Taylor will not engage him again at substance"
          target_chapter: b01c14

      - slug: b01c14
        status: planned
        chunk: |
          The non-extractable confirmation chapter: cl04 and cl-antag-d10. A request arrives
          through Jarvis that requires Taylor to identify the Black-faction courier-adjacent
          figure in the east-of-water-gate lanes — the one she has been tracking and
          withholding. Otto's apparatus has identified the figure independently and wants
          confirmation of Taylor's pattern-knowledge. Taylor runs the accounting. The figure
          is at risk either way — if Taylor confirms, he is detained; if she withholds, Otto
          has other means and the route is closed anyway, but Sera's protection guarantee is
          reduced to a contingency. She confirms. The figure is detained within a day.
          The moral_legibility crack deepens: Taylor runs the accounting, confirms Sera's
          benefit outweighs the courier's harm, and closes the ledger on a person without
          their knowledge — she is fully aware she is doing this. Dance-pressure pulse
          arrives mediated: Rhaenyra-pressure staging via intelligence inference from
          Dragonstone, signaled through the cloth merchant's behavior change (flight from
          KL, abandoning passive node function). What shifts: relational_anchor_status
          +1.0 (cl04: Taylor closes the ledger on a named person without their knowledge,
          and the pattern of closing-ledger-entries applies retroactively to the un-priced
          item she will not enter), social_tether-antag completes at rank 9 (non-extractable
          confirmed), position-prot-rise at functional peak, moral_legibility advances.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - axis: relational_anchor_status
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl04
              notes: "Taylor closes ledger on a named person without their knowledge; cl04 opportunity-missed: extraction path before non-withdrawable is now behind her; the closure retroactively names the Wren omission"
            - axis: social_tether-antag
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl-antag-d10
              notes: "non-extractable confirmation complete; Otto's leverage structural from here; cl-antag-d10 completed"
            - axis: position-prot-rise
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl-d07a
              notes: "position at functional peak; non-exit confirmed; position-of-no-exit named; cl-d07a completed"
            - axis: moral_legibility_to_self
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "Taylor fully aware she is closing the ledger on a named person; recognition present and suppressed; deepest crack before full recognition deferred to d14"
          axes_held:
            - axis: moral_framework
              rationale: "confirmation delivery is within the established rationalize-each-trade pattern; no new breach threshold — framework holds at current crack level"
            - axis: political_register-prot
              rationale: "contempt named and stable; no new feed-content this chapter that advances the register"
            - axis: social_tether-prot-rise
              rationale: "tether at near-peak; the confirmation delivery does not add a new structural node"
            - axis: capability
              rationale: "no new expansion; full-deployment architecture holds"
          density_target: 0.7-0.9
          chapter_class: standard
        dramatic_shape: climax
        goal: |
          Show the audience Taylor closing the ledger on a named person with full awareness — the accounting is explicit, the person is real, and the closure is chosen — and the cloth merchant's flight as Rhaenyra-pressure made visible.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "contempt named: articulate-contempt threshold passed"
            - "Halvard foreclosed"
            - "ward-elder pretext charge: on-page consequence of d06 list"
            - "Wren: anchor rank 4.5; coverage gap holding"
            - "Black-faction courier-adjacent: in gap lanes; Otto identifying independently"
            - "cf-rhaenyra-pressure: cloth merchant changed behavior"
          world_state:
            - "KL 122 AC; political_register-world rank 8"
          character_state:
            - "Taylor: political_register-prot rank 5; relational_anchor rank 4.5; moral_framework rank -2; position-prot-rise rank 5.5; social_tether-antag rank 7"
          source_chapter: b01c13
        handoff_out:
          open_threads:
            - "non-extractable confirmed: Otto's leverage structural; exit calculus permanently failed"
            - "second courier detained: cl04 closed; extraction path behind Taylor"
            - "cloth merchant fled KL: Rhaenyra-pressure mediated via intelligence inference; Dragonstone knows the apparatus is active"
            - "Wren: anchor rank 5.5; cl04 pattern retroactively names her exclusion from the ledger"
            - "position-prot-rise at peak (rank 6.5): position-of-no-exit confirmed"
            - "social tether: at structural peak; non-extractable"
          world_state:
            - "KL 122 AC; Green apparatus has two courier detentions; Black-faction logistics two threads closed"
            - "Rhaenyra at Dragonstone: aware the Green apparatus is active in lower-city channels"
          character_state:
            - "Taylor: social_tether-antag rank 9 (non-extractable confirmed); position-prot-rise rank 6.5; relational_anchor rank 5.5; moral_legibility rank 6; moral_framework rank -2"
            - "cl04 completed: ledger closed on a named person; pattern retroactively visible to reader on Wren"
          target_chapter: b01c15

      - slug: b01c15
        status: planned
        chunk: |
          Non-extractable confirmation deepens and Aemond arrives on-stage with Vhagar-
          proximity. Aemond (now 13) is brought to a Red Keep outer court exercise that
          Taylor's coverage map touches via a passage-adjacent ward. She sees him through
          compound eyes: a boy with a sapphire eye, moving with Vhagar's behavioral
          imprint, already performing the coercive register of someone who has never been
          told no at physical scale. Taylor routes nothing of this to Jarvis. Vhagar's
          proximity backwash reaches into the passage-adjacent ward — a thermal and pressure
          displacement Taylor has learned to read as the dragon's footprint even at distance.
          The compound-eye feed in that ward degrades at the edges; the gap-lanes east of
          the water-gate, which Taylor has kept deliberately uncovered, register as absence
          against the disrupted feed. For the first time, the gap is not invisible — it is
          perceptible as a gap, a negative shape where Wren moves without being mapped,
          made visible by the same compound-eye architecture that reads everything else.
          Taylor notes it. She does not open a ledger entry. The chapter's structural work:
          social_tether-antag reaches 9 (confirmation complete), social_tether-prot-rise
          peaks at 8 (the tether is as embedded as it will be before the collapse), and
          political_register-prot advances — Aemond through compound eyes is one more item
          of court content that the feed returns with color Taylor cannot neutralize. The
          cf-rhaenyra-pressure staging deepens: Dragonstone is aware the lower-city
          apparatus is active; Taylor reads the threat obliquely through the cloth
          merchant's absence. What shifts: both social_tether axes at peak; capability
          acknowledged load-bearing; Aemond is now a face in the feed not just a logistics
          reference; Wren's exclusion from the ledger is perceptually confirmed via the
          gap-lane negative-shape.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - axis: social_tether-antag
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl-antag-d03
              notes: "non-extractable fully confirmed; social_tether-antag reaches 9 LOCKED; cl-antag-d03 remaining 1.5 drawn (cl-antag-d03 completed here; cl-antag-d10 completed at c14)"
            - axis: social_tether-prot-rise
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "tether peaks at 8 (load-bearing-in-Otto's-architecture confirmed); no new structural addition — the 0.5 is the peak-confirmation of embedded weight"
            - axis: political_register-prot
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "Aemond through compound eyes: court content with color; the register advances from articulate-contempt toward contempt-saturation; sub-advance"
            - axis: relational_anchor_status
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl04
              notes: "Vhagar-proximity backwash degrades compound-eye coverage at gap-lane boundary; the east-of-water-gate gap is perceptually confirmed as a negative shape in the feed; Wren's exclusion from the ledger becomes visible to Taylor as a structural absence against the disrupted feed; anchor: cl04 (non-extractable confirmation cost — the closing-the-ledger-on-a-person event at d10 is the same accounting failure that the perceptual gap-confirmation now extends to Wren; 1.5 of 2.0 remaining drawn here, 0.5 unallocated); journey-required cl-d08 (the original gap mechanism that made this perception possible)"
            - axis: capability
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl05
              notes: "Aemond observation adds scope; coverage acknowledged fully load-bearing; cl05 completed"
          axes_held:
            - axis: moral_framework
              rationale: "no new breach this chapter; framework holds at current level"
            - axis: position-prot-rise
              rationale: "position at peak; no new formalization; holds at 6.5"
            - axis: moral_legibility_to_self
              rationale: "Aemond observation routed to no one; legibility holds at 6; recognition deferred"
          density_target: 0.7-0.9
          chapter_class: standard
        dramatic_shape: falling
        goal: |
          Show the audience Aemond through compound eyes — the escalation engine in physical form, 13 years old, already coercive — and the tether at full load, so the falling arc reads as the space before the cascade begins.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "non-extractable confirmed: cl04 completed; exit calculus failed"
            - "cloth merchant fled: Rhaenyra-pressure mediated"
            - "Wren: anchor rank 5.5; exclusion pattern retroactively visible"
            - "position-prot-rise at peak"
            - "Halvard foreclosed"
          world_state:
            - "KL 122 AC; Green apparatus has two courier detentions; Rhaenyra aware"
            - "political_register-world rank 8"
          character_state:
            - "Taylor: social_tether-antag rank 9; position-prot-rise rank 6.5; relational_anchor rank 5.5; moral_legibility rank 6; capability rank 6; moral_framework rank -2"
          source_chapter: b01c14
        handoff_out:
          open_threads:
            - "Aemond on-stage via compound eyes: face logged; coercive register visible; withheld from Jarvis"
            - "social tether at structural peak: both rise axes at maximum; collapse axis latent"
            - "Dragonstone-pressure mediated through cloth merchant absence"
            - "Wren: anchor rank 7 (peak tether makes exclusion weight higher)"
            - "political_register-prot: approaching contempt-saturation"
            - "position-prot-rise: peak confirmed; collapse axis about to activate"
          world_state:
            - "KL 122 AC; Green apparatus fully operational; Aemond present at court in observable range"
            - "position-world rank 8; political_register-world rank 8"
          character_state:
            - "Taylor: social_tether-antag rank 9 LOCKED; social_tether-prot-rise rank 8 (peak); capability rank 7; relational_anchor rank 7; political_register-prot rank 5.5; position-prot-rise rank 6.5 (peak)"
            - "Aemond: in Taylor's feed; not in deliverable; sapphire eye, Vhagar-imprint behavioral pattern logged"
          target_chapter: b01c16

      - slug: b01c16
        status: planned
        chunk: |
          The aftermath chapter: Taylor stops engaging Halvard's counter-argument. He finds
          her at the sept, as before. She hears the counter. She has the answer. She does not
          give it. Not because she has no response but because responding requires treating the
          argument as live, and she has confirmed to herself that the argument is not live —
          the contempt and the continuation are the same fact; the counter-argument addresses
          the contempt, not the continuation. This is the moral_legibility crack that was
          suppressed at d10 now surfacing as a behavioral fact: Taylor does not suppress the
          recognition, she walks away from the person who is offering it. The chapter also
          carries the position-prot-collapse transition: the collapse axis activates, not as
          an event but as a new arithmetic. Taylor runs the accounting and finds that her
          position is now worth less to her as a position than what it costs to hold. She
          continues holding it. What shifts: moral_legibility crack deepens structurally;
          the social_tether-prot-collapse axis activates as latent (the numbers are visible
          even if the event is not yet here).
        structure:
          scene_count: 3
        substance_delta:
          axes_in_motion:
            - axis: moral_legibility_to_self
              rationale: "Halvard encounter closes without engagement; Taylor does not suppress recognition, she walks away from its external mirror; legibility crack expressed as behavioral withdrawal"
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "crack expressed as action not just internal — walking away from Halvard is the suppression made visible to reader"
          axes_held:
            - axis: moral_framework
              rationale: "no new breach; the Halvard withdrawal is a legibility event not a framework event"
            - axis: political_register-prot
              rationale: "no new feed-event; contempt is at articulate-level and holding"
            - axis: relational_anchor_status
              rationale: "Wren in coverage; anchor holds at 7"
            - axis: social_tether-prot-rise
              rationale: "tether at peak; collapse not yet triggered; rise axis holds at 8"
            - axis: position-prot-rise
              rationale: "position at peak; collapse axis latent; rise axis holds at 6.5"
            - axis: capability
              rationale: "full-deployment architecture holds; no new expansion"
          density_target: 0.5-0.7
          chapter_class: standard
        dramatic_shape: falling
        goal: |
          Show the audience Taylor walking away from Halvard — not suppressing recognition, choosing not to hold it — so the difference between suppression and foreclosure is on the page before the cascade.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "Aemond on-stage via compound eyes: face logged"
            - "social tether at structural peak"
            - "Dragonstone-pressure mediated"
            - "Wren: anchor rank 7"
            - "Halvard: present; last substantive encounter approaching"
            - "political_register-prot: approaching contempt-saturation"
          world_state:
            - "KL 122 AC; position-world rank 8; political_register-world rank 8"
          character_state:
            - "Taylor: social_tether-antag rank 9 LOCKED; social_tether-prot-rise rank 8; relational_anchor rank 7; political_register-prot rank 5.5; capability rank 7; moral_framework rank -2; moral_legibility rank 6"
          source_chapter: b01c15
        handoff_out:
          open_threads:
            - "Halvard: walked away from; counter-argument foreclosed by behavior not argument"
            - "social_tether-prot-collapse: latent — arithmetic visible to Taylor; not yet triggered"
            - "position-prot-collapse: latent — position worth less than it costs; Taylor continues"
            - "Wren: anchor rank 7; in coverage; exclusion pattern visible to reader"
            - "Aemond: in feed; not in deliverable"
            - "Dragonstone-pressure: mediated; propagating"
          world_state:
            - "KL 122 AC; cascade zone begins next chapter; both collapse axes latent"
          character_state:
            - "Taylor: moral_legibility rank 6.5 (crack expressed as behavioral withdrawal); all other axes holding from b01c15"
            - "Halvard: functionally exited from Taylor's active engagement"
          target_chapter: b01c17

      - slug: b01c17
        status: planned
        chunk: |
          The use-vector intercept: d11. Otto's apparatus identifies a vector targeting Wren —
          not by name, but by pattern (a woman who moves through the east-of-water-gate
          coverage gap in a regular pattern; someone has noticed the gap and is using it, and
          the figure using it has been observed in proximity to Taylor's known ward-contacts).
          The apparatus wants to know who the gap-figure is. Taylor identifies the question
          instantly: if she routes a description of Wren to Jarvis, Wren becomes a named
          person in Otto's intelligence picture. She adjusts the network to screen the
          question — routes a different figure through the gap documentation, attributes the
          gap-movements to a different ward-elder. This is protection. It is also the same
          override architecture she built to atone for, deployed at single-person scale. The
          chapter's collision: the capability deployment to protect Wren is mechanically
          identical to the Khepri-architecture; Taylor cannot unname this in her own
          accounting. Moral_framework cracks materially. The collapse axes are now active:
          position-prot-collapse and social_tether-prot-collapse begin their downward
          allocations. What shifts: relational_anchor_status +0.5, capability +1.0 (protection
          deployment adds scope), moral_framework -1.0, position-prot-collapse begins,
          social_tether-prot-collapse begins.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - axis: relational_anchor_status
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: cl-d11
              notes: "use-vector intercept targeting Wren; Taylor adjusts network to screen; cl-d11 opportunity-missed: she is running the same override architecture she built to atone for"
            - axis: capability
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: null
              notes: "protection deployment adds capability scope; network adjusted at single-person scale; Khepri-echo explicit"
            - axis: moral_framework
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl03a
              notes: "protection deployment is mechanically identical to override architecture; Taylor cannot unname this; third material breach in the cascade sequence; cl03a cost side: intelligence-network-build cost rolling over to use-vector-deployment is the on-page event (cl03a completed)"
            - axis: position-prot-collapse
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl07b
              notes: "collapse axis activates; position-of-no-exit begins its downward arc; the protection deployment is the first event the collapse narrative claims"
            - axis: social_tether-prot-collapse
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl07a
              notes: "collapse axis activates; tether-at-full-load begins its downward arc; parallel to position-prot-collapse"
          axes_held:
            - axis: political_register-prot
              rationale: "protection deployment is internal and tactical; contempt register does not advance on Wren-protection events"
            - axis: moral_legibility_to_self
              rationale: "Taylor cannot unname the override echo but does not yet open the full recognition event; legibility holds at crack-level"
            - axis: social_tether-antag
              rationale: "locked at 9; does not move further"
            - axis: social_tether-prot-rise
              rationale: "rise axis at peak; collapse axis now active; rise does not move further"
          density_target: 0.7-0.9
          chapter_class: standard
        dramatic_shape: rising
        goal: |
          Show the audience the protection and the Khepri-echo together — Taylor protecting Wren by deploying the override architecture she came here to retire — so the irony is explicit before it becomes catastrophic.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "Halvard: walked away from; counter-argument foreclosed"
            - "social_tether-prot-collapse: latent — arithmetic visible"
            - "position-prot-collapse: latent"
            - "Wren: anchor rank 7; in coverage; gap-figure status"
            - "Aemond: in feed"
            - "Dragonstone-pressure: propagating"
          world_state:
            - "KL 122 AC; cascade zone; both collapse axes latent"
          character_state:
            - "Taylor: moral_legibility rank 6.5; social_tether-prot-rise rank 8 (peak); relational_anchor rank 7; political_register-prot rank 5.5; capability rank 7; moral_framework rank -2; position-prot-rise rank 6.5 (peak)"
          source_chapter: b01c16
        handoff_out:
          open_threads:
            - "use-vector intercept complete: Wren screened; a different figure routed in her place; Otto's apparatus has a false attribution"
            - "Khepri-echo named: Taylor cannot unname the override-architecture equivalence"
            - "position-prot-collapse: active; declining from peak"
            - "social_tether-prot-collapse: active; declining from peak"
            - "Wren: anchor rank 7.5; screened from Otto's apparatus"
            - "false attribution in Otto's intelligence picture: structural risk if discovered"
          world_state:
            - "KL 122 AC; Otto's apparatus has a false figure in the gap-movement documentation"
            - "cascade zone; collapse axes in motion"
          character_state:
            - "Taylor: capability rank 8; relational_anchor rank 7.5; moral_framework rank -3; position-prot-collapse rank 6 (declining); social_tether-prot-collapse rank 7 (declining); moral_legibility rank 6.5"
            - "Wren: screened; anchor weight at 7.5; false figure takes her place in the apparatus picture"
          target_chapter: b01c18

      - slug: b01c18
        status: planned
        chunk: |
          War-pressure on Sera's succession exposure — Dance-pressure pulse 2. A
          court-tier event: Viserys I's health deteriorates visibly; a succession question
          Sera's legitimacy-lever has been held against becomes acute. Otto requests a
          full-coverage deployment — all wards, all channels, maximum intelligence density
          for the next fortnight — to support a specific Green-faction succession move. Taylor
          executes the deployment. This is capability at irrevocable-Khepri-repetition scale:
          the network runs at density she has not deployed since the architecture was built,
          covering bodies in numbers she has not tracked since Gold Morning. The moral_
          framework crack at d12 is the irrevocable threshold — this is the deployment that
          removes the qualifier "calibrated." Moral_framework collapses a full rank. The
          political_register-prot advances materially: the full-coverage deployment is the
          densest court-content the feed has returned, and Taylor reads the entire court
          apparatus through compound eyes at maximum range. The contempt arrives at near-
          saturation. Political_register-world advances as the Green succession move lands.
          What shifts: moral_framework -1.0 (irrevocable threshold); political_register-prot
          +2.0 (near-saturation); position-world +1.0; political_register-world +1.0;
          position-prot-collapse -1.0; social_tether-prot-collapse -1.0.
        structure:
          scene_count: 5
        substance_delta:
          axes_in_motion:
            - axis: moral_framework
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl02
              notes: "irrevocable-Khepri-repetition deployment; calibrated qualifier removed; full-network maximum-density activation; cl02 cost side completed"
            - axis: political_register-prot
              direction: up
              target_delta_magnitude: 2.0
              cost_ledger_anchor: cl06
              notes: "full-coverage deployment at maximum density; court apparatus read through compound eyes at scale; contempt arrives at near-saturation; cl06 opens"
            - axis: position-world
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl07b
              notes: "Green succession move lands; position-world advances through the intelligence operation Taylor executes; cl07b begins"
            - axis: political_register-world
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl07c
              notes: "Green succession move advances; political_register-world rises as direct product of the irrevocable deployment; cl07c begins"
            - axis: position-prot-collapse
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl07b
              notes: "collapse arc: full deployment makes Taylor more load-bearing and therefore more disposable post-need; collapse advancing"
            - axis: social_tether-prot-collapse
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl07a
              notes: "collapse arc: tether under structural strain; the deployment is the last act before Otto's removal calculus completes"
          axes_held:
            - axis: relational_anchor_status
              rationale: "Wren in coverage during the deployment but screened; anchor holds at 7.5; the deployment scale increases structural risk but does not yet produce a recognition event"
            - axis: moral_legibility_to_self
              rationale: "the irrevocable threshold is named in the accounting but not yet the full recognition event; suppression continues; deferred to d14"
            - axis: capability
              rationale: "capability at rank 8; the deployment does not add scope, it runs at existing scope maximally"
          density_target: 0.8-0.9
          chapter_class: standard
        dramatic_shape: climax
        goal: |
          Show the audience the irrevocable deployment at full scale — Khepri-architecture running at maximum density — and the court apparatus read through compound eyes until the contempt is as near-complete as the architecture it rides on.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "use-vector intercept: Wren screened; false attribution in Otto's picture"
            - "position-prot-collapse: active; declining"
            - "social_tether-prot-collapse: active; declining"
            - "Wren: anchor rank 7.5"
            - "Khepri-echo named"
            - "Dragonstone-pressure: propagating"
          world_state:
            - "KL 122 AC; Viserys I health declining; succession question acute"
            - "cascade zone; collapse axes in motion"
          character_state:
            - "Taylor: capability rank 8; relational_anchor rank 7.5; moral_framework rank -3; position-prot-collapse rank 6; social_tether-prot-collapse rank 7; political_register-prot rank 5.5"
          source_chapter: b01c17
        handoff_out:
          open_threads:
            - "irrevocable deployment complete: Khepri-repetition threshold crossed without qualifier"
            - "Green succession move landed: Sera's legitimacy-lever secured for the near term"
            - "contempt near-saturation: Taylor has named the court apparatus by name at maximum resolution"
            - "Wren: anchor rank 7.5; screened but at structural risk as deployment scale increases"
            - "position-prot-collapse: declining (rank 5)"
            - "social_tether-prot-collapse: declining (rank 6)"
            - "false attribution in Otto's picture: risk present"
            - "cl06 opened: contempt without exit attached"
          world_state:
            - "KL 122 AC; Viserys I health in visible decline; Green succession move landed; political_register-world advancing toward lock"
            - "position-world rank 9; political_register-world rank 9"
          character_state:
            - "Taylor: political_register-prot rank 7.5 (near-saturation); moral_framework rank -4 (irrevocable); position-prot-collapse rank 5; social_tether-prot-collapse rank 6; capability rank 8; relational_anchor rank 7.5"
          target_chapter: b01c19

      - slug: b01c19
        status: planned
        chunk: |
          Contempt-without-refusal locks. A scene that is structurally simple but emotionally
          final: Taylor receives a new request from Jarvis. She runs the accounting. She
          executes the request. The contempt does not enter the accounting — it sits alongside
          it, complete and unreferenced, the way a person's name appears in a ledger after
          they are dead. Cl06 is paid: the contempt has arrived with no exit attached, and
          clarity forecloses nothing. The chapter also carries the first full-recognition
          movement of moral_legibility_to_self: not the terminal recognition, but the point
          at which the suppression is no longer fully operational — Taylor's accounting
          catches its own pattern, names it, and continues the request execution. Cl07a
          opens its cost side: collateral severance begins. A ward-contact Taylor has worked
          with for seven months stops responding to approaches. Someone in the upper-city has
          identified the contact as associated with the witch-woman. The social_tether-prot-
          collapse arc accelerates. Position-prot-collapse accelerates. What shifts:
          political_register-prot +1.5 (contempt-without-refusal locked at rank 9); moral_
          legibility_to_self +0.5 (recognition beginning but not terminal); social_tether-prot-
          collapse -1.5; position-prot-collapse -1.0.
        structure:
          scene_count: 4
        substance_delta:
          axes_in_motion:
            - axis: political_register-prot
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl06
              notes: "contempt-without-refusal LOCKED at rank 9; cl06 paid: contempt with no exit attached; clarity forecloses nothing; the ledger's final form"
            - axis: moral_legibility_to_self
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: cl07a
              notes: "accounting catches its own pattern and names it; suppression no longer fully operational; recognition beginning but not terminal; cl07a cost opens"
            - axis: social_tether-prot-collapse
              direction: down
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl07a
              notes: "ward-contact severs association; collateral severance begins; cl07a cost side accelerating"
            - axis: position-prot-collapse
              direction: down
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl07b
              notes: "position-of-no-exit declining; upper-city identification of ward-contact as Taylor-associated is a position risk"
          axes_held:
            - axis: moral_framework
              rationale: "no new breach threshold; framework is at consumed-as-compass level and holds there"
            - axis: relational_anchor_status
              rationale: "Wren in coverage; anchor holds at 7.5; the collateral severance is a ward-contact, not Wren"
            - axis: capability
              rationale: "full-deployment architecture holds; no new expansion"
            - axis: social_tether-antag
              rationale: "locked at 9; does not move"
          density_target: 0.7-0.9
          chapter_class: standard
        dramatic_shape: falling
        goal: |
          Show the audience contempt-without-refusal at its completion — the register locked, the continuation unchanged — and the first recognition event that is not fully suppressed, so the terminal recognition at d14 reads as arrival not revelation.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "irrevocable deployment complete"
            - "Green succession move landed"
            - "contempt near-saturation"
            - "Wren: anchor rank 7.5; screened"
            - "position-prot-collapse declining (rank 5)"
            - "social_tether-prot-collapse declining (rank 6)"
            - "false attribution in Otto's picture"
          world_state:
            - "KL 122 AC; Viserys I health in visible decline; position-world rank 9; political_register-world rank 9"
          character_state:
            - "Taylor: political_register-prot rank 7.5; moral_framework rank -4; position-prot-collapse rank 5; social_tether-prot-collapse rank 6; capability rank 8; relational_anchor rank 7.5"
          source_chapter: b01c18
        handoff_out:
          open_threads:
            - "contempt-without-refusal LOCKED: political_register-prot rank 9; the register is complete; it changes nothing"
            - "recognition beginning: accounting caught its own pattern; not yet terminal"
            - "ward-contact severed: collateral severance begun; Taylor's tether losing nodes"
            - "false attribution in Otto's picture: risk active"
            - "Wren: anchor rank 7.5; in coverage; screened"
            - "position-prot-collapse: rank 4"
            - "social_tether-prot-collapse: rank 4.5"
            - "Viserys I: health in active decline; succession imminent"
          world_state:
            - "KL 122 AC; Viserys I death window approaching; Dance-ignition close; Green apparatus positioned to act on succession"
          character_state:
            - "Taylor: political_register-prot rank 9 LOCKED; moral_legibility rank 7 (recognition beginning); social_tether-prot-collapse rank 4.5; position-prot-collapse rank 4; capability rank 8; relational_anchor rank 7.5; moral_framework rank -4"
          target_chapter: b01c20

      - slug: b01c20
        status: planned
        chunk: |
          The Dance ignites. Viserys I dies. The Green faction moves within hours on the
          succession; the apparatus Taylor's intelligence has been feeding for months
          executes the transition with the precision that intelligence makes possible. Taylor
          learns of the death and the succession-move through the insect-feed simultaneously.
          Then the Flea Bottom burn begins — not immediately, but within a day of the
          succession announcement, as street-level Green-Black factional violence reaches
          the lower city through the routes Taylor mapped. The streets she covered, the ward
          junctions she catalogued, the movement patterns she delivered: these are the routes
          the violence moves through. Wren dies. The perceptual mechanism: Taylor's insect-
          feed is active in the lanes east of the water-gate — the coverage gap she held open
          for Wren's free movement — when the fire reaches them. She loses the feed signal
          from those lanes as the smoke and heat disperse the insects. She knows what it
          means. She cannot call it loss in the accounting because Wren was never in the
          ledger. The recognition-too-late arrives in full: the un-priced item is the one
          the calculus came for. Taylor's expulsion follows — the false attribution is
          discovered or the apparatus simply no longer needs the instrument — and she leaves
          King's Landing with the contempt complete, the ledger accurate, and nothing to
          refuse. What shifts: relational_anchor_status +1.5 (rank 9 LOCKED; unprotected-at-
          burn); position-prot-collapse -3.0 (to rank 1; dead/expelled); social_tether-prot-
          collapse -3.5 (to rank 1; severed); moral_legibility_to_self +1.5 (recognition-too-
          late; rank 8 LOCKED); position-world +1.0 (LOCKED); political_register-world +1.0
          (LOCKED).
        structure:
          scene_count: 5
        substance_delta:
          axes_in_motion:
            - axis: relational_anchor_status
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl07c
              notes: "Wren dies in the coverage gap Taylor held open for her free movement; relational_anchor_status rank 9 LOCKED; cl07c: un-priced item is what the calculus came for; HIGH=WORST"
            - axis: position-prot-collapse
              direction: down
              target_delta_magnitude: 3.0
              cost_ledger_anchor: cl07b
              notes: "Taylor expelled/dead; position-prot-collapse to rank 1 LOCKED; cl07b cost completed"
            - axis: social_tether-prot-collapse
              direction: down
              target_delta_magnitude: 3.5
              cost_ledger_anchor: cl07a
              notes: "tether severed; patron dissolved; network transferred; social_tether-prot-collapse rank 1 LOCKED; cl07a cost completed"
            - axis: moral_legibility_to_self
              direction: up
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl07a
              notes: "recognition-too-late at full force; feed-signal loss from Wren's lanes is the recognition event; rank 8 LOCKED; cl07a gain side completed"
            - axis: position-world
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl07b
              notes: "Green succession move lands in full; position-world LOCKED at rank 9; the apparatus completes without Taylor; cl07b gain completed"
            - axis: political_register-world
              direction: up
              target_delta_magnitude: 1.0
              cost_ledger_anchor: cl07c
              notes: "Green succession position locked; political_register-world LOCKED at rank 9; cl07c completed"
          axes_held:
            - axis: moral_framework
              rationale: "framework consumed as compass; no new breach — the Dance igniting is not a breach event, it is the consequence of prior breaches arriving; holds at consumed-as-compass rank 8"
            - axis: capability
              rationale: "full-deployment architecture holds until Taylor's removal; the network outlasts the architect (end-state per notes: network structural to Greens after Taylor's departure)"
            - axis: political_register-prot
              rationale: "contempt-without-refusal LOCKED at rank 9; does not move"
            - axis: social_tether-antag
              rationale: "LOCKED at rank 9; does not move"
          density_target: 0.8-0.9
          chapter_class: standard
        dramatic_shape: falling
        goal: |
          Show the audience the feed-signal loss from Wren's lanes as the recognition event — not a named loss, not a ledger entry, the absence of signal in the place Taylor held open — and close on the contempt complete, the ledger accurate, nothing remaining to refuse.
        pov_narrator: taylor-hebert-kl-122ac
        handoff_in:
          open_threads:
            - "contempt-without-refusal LOCKED"
            - "recognition beginning: not yet terminal"
            - "ward-contact severed: tether losing nodes"
            - "Wren: anchor rank 7.5; in coverage gap lanes"
            - "position-prot-collapse: rank 4"
            - "social_tether-prot-collapse: rank 4.5"
            - "Viserys I: death window active"
            - "false attribution in Otto's picture"
          world_state:
            - "KL 122 AC entering Dance-ignition threshold; Viserys I death imminent; Green apparatus positioned"
            - "position-world rank 9; political_register-world rank 9"
          character_state:
            - "Taylor: political_register-prot rank 9 LOCKED; moral_legibility rank 7; social_tether-prot-collapse rank 4.5; position-prot-collapse rank 4; capability rank 8; relational_anchor rank 7.5; moral_framework rank -4"
          source_chapter: b01c19
        handoff_out:
          open_threads: []
          world_state:
            - "KL 122 AC; Viserys I dead; Green succession complete; Dance ignited; Flea Bottom burned"
            - "Green apparatus operational post-Taylor; network transferred; Taylor's architecture outlasts its architect"
            - "Wren: dead in coverage gap lanes; no ledger entry"
          character_state:
            - "Taylor: expelled/dead; moral_legibility rank 8 LOCKED (recognition-too-late); political_register-prot rank 9 LOCKED; social_tether-prot-collapse rank 1 LOCKED; position-prot-collapse rank 1 LOCKED; relational_anchor rank 9 LOCKED; moral_framework rank 8 LOCKED (consumed-as-compass); capability rank 8 LOCKED (network outlasts architect)"
          target_chapter: null


  cast_roster:
    # Authored: /and-cast Phase 4 by margit 2026-05-24
    - slug: taylor-hebert-kl-122ac
      role: protagonist — POV anchor, cold-utilitarian ledger, Khepri-residue insect-network, 9 axes
      perspective: protagonist
    - slug: otto-hightower
      role: antagonist — calculation-leverage patron, proposal-register only, Sera-protection trade, social_tether-antag primary carrier
      perspective: antagonist
    - slug: wren-stitch-maker-flea-bottom-ward
      role: cost-bearer — un-priced relational anchor, relational_anchor_status primary carrier, d14 death hard fence
      perspective: supporting
    - slug: sera-hightower-kl-122ac
      role: protect-target — legitimacy-question lever, position-prot-rise justification object, never meets Taylor
      perspective: supporting
    - slug: aemond-targaryen-122ac
      role: world-embodiment:opposite-number — escalation-engine, Vhagar-proximity, axis-movement-per-appearance hard fence
      perspective: world
    - slug: alicent-hightower-122ac
      role: world-embodiment:green-faction-institution — dynastic-maternal affect, position-world + political_register-world carrier, compound-eyes-only observable
      perspective: world
    - slug: criston-cole-122ac
      role: world-embodiment:faction-violence-instrument — Green enforcement arm, relational_anchor_status indirect, observable as operational aftermath only
      perspective: world
    - slug: rhaenyra-targaryen-122ac
      role: world-embodiment:black-faction-claimant — road-not-taken irony, political_register-world + political_register-prot, Dragonstone-distance, mediated channels only
      perspective: world
    - slug: oswyn-mudway-flea-bottom-elder
      role: supporting:Flea-Bottom-ward-network-anchor — social_tether-prot-rise substrate, unknowing-contact, acts 1-2 tapering
      perspective: supporting
    - slug: jarvis-coin-kl-courier
      role: supporting:Otto-courier-adjacent — social_tether-prot-rise + social_tether-antag structural vector, moral_framework made material, acts 1-2 receding
      perspective: supporting
    - slug: septon-halvard-flea-bottom
      role: supporting:naive-idealist-foil — moral_legibility_to_self mirror, principled-slower, counter-argument Taylor stops engaging at d09, one encounter per act
      perspective: supporting

  cast_roster_notes:
    carry_forward:
      - id: cf-wren-d14-perceptual-mechanism
        from: phase-3-dramatist-viability
        target: /and-substance chapter (d14)
        note: "Wren's d14 death — name perceptual mechanism (insect-feed in streets at ignition / Taylor proximate / feed-confirmation after expulsion); not specified by trajectory. Resolve at d14 chapter contract."
      - id: cf-d10-courier-face
        from: phase-3-dramatist-viability
        target: /and-substance chapter (d05-d10 distribution)
        note: "d10 courier (opposing-faction figure Taylor's route-map detains) must be a face, not a function. Stage prior insect-feed observation of this figure across d05-d09 chapter contracts so the d10 accounting has a body to close on. Not a cast slot — chapter-level staging obligation."
      - id: cf-rhaenyra-pressure-staging
        from: phase-3-dramatist-viability
        target: /and-substance book / chapter
        note: "Rhaenyra at Dragonstone; pressure on Taylor arrives through mediated channels (court rumor, intelligence-product inference, Black-faction encounter in KL). Name explicit pressure-staging mechanism at book/chapter substance — not background."
      - id: cf-relational-anchor-environmental
        from: phase-3-dramatist-viability + audit
        target: studio (scene texture)
        note: "relational_anchor_status partial environmental carrier (cond-kl-witch-label-formation-122ac). Carry to studio for staging — not a cast slot."
