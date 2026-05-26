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
        stitched_stale_since: 2026-05-26T00:00:00Z   # bones revised post-stitch; /and-facets + /and-stitch must re-run before draft is current
        draft_file: active-project/draft/b01-c02.md
        render_log: active-project/staff/stitcher/render-log-b01-c02.md
        cold_read:
          read_at: 2026-05-26T00:00:00Z
          verdict: PASS-WITH-CAVEATS
          recovered_summary: "A surveillance-obsessed narrator with insect-based senses spends a day monitoring an alley from a hiding spot, notices a recurring woman pass by without speaking to her, and logs her in a mental ledger that closes a fraction-second slower than the others."
          report_path: active-project/staff/reviews/coldread-b01-c02-2026-05-26-revise.md
          prior_report_path: active-project/staff/reviews/coldread-b01-c02-2026-05-26.md   # superseded
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
          reviewed_at: 2026-05-26T00:00:00Z
          report_path: active-project/staff/reviews/bones-b01c03-fidelity-2026-05-26.md
          verdict: PASS-WITH-NOTES
          bones_file_mtime_at_review: 0  # cascade-budget; mtime captured implicitly via cascade emit
          stale_since: null
          # 0 HARD, 3 SIGNAL (signal-001 s02 stakes-axis-not-dominant — thesis-correct exception; others advisory), 2 FLAG (advisory), 0 FAULT.
          # Cold-read prediction: HIGH on all 5 target elements (Otto terms / proposal accuracy / Taylor engagement / asking-for-a-day hinge / Jarvis register). Partial-recovery risk noted on irrevocability clause; b01c04 acceptance depends on this landing as closure.
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
        status: planned
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
              target_delta_magnitude: 1.5
              cost_ledger_anchor: cl03a
              notes: "network expands across three wards; Khepri-rhyming architecture beginning to form; cl03a gain side"
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
              notes: "acceptance = leverage solidified; Otto gains proportional to Taylor's position-rise; cl-antag-d03 completed"
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

      - slug: b01c05
        status: planned
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

      - slug: b01c06
        status: planned
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

      - slug: b01c07
        status: planned
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

      - slug: b01c08
        status: planned
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

      - slug: b01c09
        status: planned
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
              cost_ledger_anchor: null
              notes: "coverage extends to Wren's daily pattern; structural surveillance without ledger entry; anchor weight increases through omission-architecture"
            - axis: political_register-prot
              direction: up
              target_delta_magnitude: 0.5
              cost_ledger_anchor: null
              notes: "courier's Dragonpit-gate meeting: Black-faction contact inferred; color accumulates on the feed content; minor advance"
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

      - slug: b01c10
        status: planned
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
              notes: "Green succession channel solidifies through formalized arrangement; cl-world-d07 completed"
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
            - "position-world rank 7; political_register-world rank 7"
          character_state:
            - "Taylor: position-prot-rise rank 4.5 (approaching peak); social_tether-prot-rise rank 4; social_tether-antag rank 6 (structural); moral_framework rank -1 (systematic-override entered); moral_legibility rank 5.5 (crack); position-world advancing"
            - "courier-figure: detained; ledger entry closed on a named person; face to the cost"
            - "Otto: leverage structural post-formalization"
          target_chapter: b01c11

      - slug: b01c11
        status: planned
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
              cost_ledger_anchor: cl-d08
              notes: "coverage gap = Wren structurally necessary to coverage map without entering the ledger; cl-d08 cost paid"
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
