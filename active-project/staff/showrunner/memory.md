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
    # drama: authored downstream at /and-substance book Phase 4
    # chapters[]: authored downstream at /and-substance book Phase 2

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
