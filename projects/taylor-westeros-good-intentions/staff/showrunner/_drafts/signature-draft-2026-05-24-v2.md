# Signature Draft v2 — taylor-westeros-good-intentions
# /and-substance series Phase 5 revise attempt 2
# Authored: 2026-05-24
# Revises: signature-draft.md (v1, Phase 4 accepted by pulp-enthusiast)
# Changes-from-v1: see AUTHORING NOTES section at end of this file

---

## YAML BLOCK

```yaml
substance:
  state_axes:

    # ── PROTAGONIST AXES ──────────────────────────────────────────────────────

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

    # position protagonist — split into rise + collapse axes
    # Addresses: fault-001 SCHEMA-SLUG-COLLISION, CURVE-SHAPE FAIL (dramatist), flag-001, flag-002
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

    # social_tether protagonist — split into rise + collapse axes
    # Addresses: fault-001 SCHEMA-SLUG-COLLISION, CURVE-SHAPE FAIL (dramatist), flag-001, flag-002
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

    # ── ANTAGONIST AXIS ───────────────────────────────────────────────────────
    # Addresses: fault-001 SCHEMA-SLUG-COLLISION (social_tether → social_tether-antag)

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

    # ── WORLD AXES ────────────────────────────────────────────────────────────
    # Addresses: fault-001 SCHEMA-SLUG-COLLISION (position → position-world; political_register → political_register-world)

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

    # ── d01 — rescue witnessed; capability onset + tether embedding ────────────
    # v1 cl01 split into cl01a + cl01b (fixes fault-002 multi-axis gain)
    # cl01a capability trimmed from +2 to +1 (fixes fault-004 capability over-sum)

    - id: cl01a
      gain: "capability +1"
      cost: "opportunity-missed: rescue witnessed by Flea Bottom witnesses; witch-label formation begins (cond-kl-witch-label-formation-122ac); [cost-bearer] block enters exposure radius"
      anchor: { book: b01, chapter: null, scene: null }

    - id: cl01b
      gain: "social_tether-prot-rise +2"
      cost: "journey-required: cl01a (same rescue event; tether embedding is the other face of witch-label exposure)"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d03 — Otto offer accepted; position-prot-rise onset + moral_framework first crack

    - id: cl02
      gain: "position-prot-rise +4"
      cost: "moral_framework -3"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d04 — network built outward; capability + tether-rise structuralize ─────
    # v1 cl03 split into cl03a + cl03b (fixes fault-002 multi-axis gain)
    # cl03a cost trimmed from -3 to -2 (fixes fault-004 moral_framework over-sum)

    - id: cl03a
      gain: "capability +3"
      cost: "moral_framework -2"
      anchor: { book: b01, chapter: null, scene: null }

    - id: cl03b
      gain: "social_tether-prot-rise +4"
      cost: "journey-required: cl03a (same network-build event; tether gain is future-cost collateral — this +4 becomes the -7 at cl07a; DOWNSTREAM NOTE: chapter contract for d04 must encode tether gain as future-cost collateral to suppress SUBSTANCE-SUSPECT-cheap-gain-social_tether-prot-rise at /and-substance book Phase 0)"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d04 — world position gains from Taylor's network build ────────────────

    - id: cl-world-d04
      gain: "position-world +2"
      cost: "journey-required: cl03a (Taylor's network delivers the Flea Bottom intelligence layer Otto cannot obtain otherwise; world consolidation is the direct output of capability gain)"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d05 — resentment onset; political_register-prot first movement ─────────
    # NEW entry (fixes fault-004 political_register-prot gap +3)

    - id: cl-d05
      gain: "political_register-prot +3"
      cost: "opportunity-missed: resentment becomes the permanent register of court observation; the insect-feed now returns color Taylor cannot un-notice; neutral-instrumentally-observant is foreclosed from d05 forward"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d06 — [cost-bearer] structurally-at-risk; relational_anchor_status loads ─
    # NEW entry (distributes relational_anchor_status accumulation; fixes fault-004)

    - id: cl-d06
      gain: "relational_anchor_status +2"
      cost: "moral_framework -1"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d07 — Otto formalizes the arrangement; position-prot-rise peaks toward 7 ─
    # NEW entry (closes position-prot-rise ledger gap of +2)

    - id: cl-d07a
      gain: "position-prot-rise +2"
      cost: "opportunity-missed: Otto names the arrangement explicitly; Taylor can no longer read the function as informal; exit calculus is now fully visible to both parties"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d07 — world political register gains from Otto's formalization ────────

    - id: cl-world-d07
      gain: "political_register-world +2"
      cost: "journey-required: cl02 (Otto formalizes the arrangement; Green succession channel solidifies through the intelligence architecture Taylor accepted)"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d03 — Otto's leverage onset (antagonist axis entry) ───────────────────

    - id: cl-antag-d03
      gain: "social_tether-antag +4"
      cost: "journey-required: cl02 (offer accepted; Otto gains leverage proportional to Taylor's position-rise)"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d08 — [cost-bearer] becomes network coverage anchor ───────────────────
    # NEW entry (distributes relational_anchor_status accumulation; fixes fault-004)

    - id: cl-d08
      gain: "relational_anchor_status +2"
      cost: "journey-required: cl03b ([cost-bearer] moves freely in wards Taylor cannot cover without triggering witch-label; [cost-bearer] is structurally necessary to the coverage map without appearing in the ledger)"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d08 — social_tether-prot-rise final +1 ────────────────────────────────
    # NEW entry (closes social_tether-prot-rise ledger gap of +1)

    - id: cl-d08b
      gain: "social_tether-prot-rise +1"
      cost: "journey-required: cl-d08 ([cost-bearer]'s free movement in uncovered wards consolidates the tether; the coverage gap that makes [cost-bearer] useful is the same gap Taylor refuses to route around)"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d10 — extraction window foreclosed; relational_anchor_status loads ────
    # (v1 cl04 — slug updated in cost references; anchor unchanged)

    - id: cl04
      gain: "relational_anchor_status +3"
      cost: "opportunity-missed: extraction path before network became non-withdrawable; Taylor runs the accounting, confirms [protect-target]'s benefit outweighs the courier's harm, and closes the ledger on a person without their knowledge"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d10 — Otto's leverage confirmed non-extractable (antagonist axis entry) ─

    - id: cl-antag-d10
      gain: "social_tether-antag +4"
      cost: "journey-required: cl04 (non-extractable confirmed; Otto's leverage is structural from here)"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d11/d12 — [cost-bearer] use-vector intercepted; capability final push ──
    # cl05 cost trimmed from -2 to -1 (fixes fault-004 moral_framework over-sum)

    - id: cl05
      gain: "capability +2"
      cost: "moral_framework -1"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d11 — [cost-bearer] load-bearing-and-named; relational_anchor_status ──
    # NEW entry (distributes relational_anchor_status accumulation; fixes fault-004)

    - id: cl-d11
      gain: "relational_anchor_status +1"
      cost: "opportunity-missed: Taylor intercepts the use-vector targeting [cost-bearer] and adjusts the network to screen it; she calls this protection; she is running the same override architecture she built to atone for"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d09/d13 — contempt articulated through contempt-without-refusal ────────
    # (v1 cl06 — slug updated from political_register_toward_elite to political_register-prot)

    - id: cl06
      gain: "political_register-prot +5"
      cost: "opportunity-missed: contempt arrives with no exit attached; clarity forecloses nothing; the contempt does not change what she does next"
      anchor: { book: b01, chapter: null, scene: null }

    # ── d14 — recognition + collapse + burn ───────────────────────────────────
    # v1 cl07 split into cl07a + cl07b + cl07c (fixes fault-003 multi-axis cost + wrong-sign cost)

    - id: cl07a
      gain: "moral_legibility_to_self +4"
      cost: "social_tether-prot-collapse -7"
      anchor: { book: b01, chapter: null, scene: null }
      # recognition arrives as the tether severs; the accounting completes in the moment of catastrophe

    - id: cl07b
      gain: "position-world +2"
      cost: "position-prot-collapse -6"
      anchor: { book: b01, chapter: null, scene: null }
      # world's Green consolidation completes as Taylor's position is made irrelevant by removal;
      # her exit IS the apparatus locking — the two are a single event

    - id: cl07c
      gain: "political_register-world +2"
      cost: "opportunity-missed: relational_anchor_status reaches rank 9 — unprotected-at-burn [HIGH = WORST on this axis; rank 9 = [cost-bearer] dies before Taylor can spend the protection she built everything to provide; the un-priced item is the one the calculus came for]"
      anchor: { book: b01, chapter: null, scene: null }
      # succession locked at the moment [cost-bearer] burns; the contempt is the ledger naming this

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

    # Dance-ignition: replaces single 'invisible and constant' entry with two named-eruption-point entries
    # Addresses: SUBSTANCE-FLAT-antagonist_pressure (dark-fantasy-reader)

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
    series:  { delta_per_signature_axis: 4-8,     density_target: 0.6-0.9 }
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
```

---

## AT-A-GLANCE TABLE

| axis slug | perspective | start | end | declared Δ | class | arc shape |
|---|---|---|---|---|---|---|
| moral_framework | protagonist | 2 | 8 | +6 | emotional | monotonic collapse |
| capability | protagonist | 2 | 8 | +6 | plot | monotonic rise |
| position-prot-rise | protagonist | 1 | 7 | +6 | plot | rise only (d03→d10) |
| position-prot-collapse | protagonist | 7 | 1 | −6 | plot | collapse only (d10→d14) |
| relational_anchor_status | protagonist | 1 | 9 | +8 | emotional | monotonic rise; HIGH=WORST; LOCKED |
| moral_legibility_to_self | protagonist | 4 | 8 | +4 | emotional | non-linear net-positive; LOCKED end 8 |
| political_register-prot | protagonist | 1 | 9 | +8 | emotional | monotonic rise; LOCKED end 9 |
| social_tether-prot-rise | protagonist | 1 | 8 | +7 | plot | rise only (d01→d10) |
| social_tether-prot-collapse | protagonist | 8 | 1 | −7 | plot | collapse only (d10→d14) |
| social_tether-antag | antagonist | 1 | 9 | +8 | plot | monotonic rise |
| position-world | world | 5 | 9 | +4 | plot | monotonic rise |
| political_register-world | world | 5 | 9 | +4 | plot | monotonic rise |

---

## COST-LEDGER SUMMARY TABLE

| id | traj ref | gain axis | gain Δ | cost form | cost detail |
|---|---|---|---|---|---|
| cl01a | d01 | capability | +1 | opportunity-missed | witch-label onset; exposure radius |
| cl01b | d01 | social_tether-prot-rise | +2 | journey-required | cl01a |
| cl02 | d03 | position-prot-rise | +4 | axis cost | moral_framework −3 |
| cl03a | d04 | capability | +3 | axis cost | moral_framework −2 |
| cl03b | d04 | social_tether-prot-rise | +4 | journey-required | cl03a (future-cost collateral) |
| cl-world-d04 | d04 | position-world | +2 | journey-required | cl03a |
| cl-d05 | d05 | political_register-prot | +3 | opportunity-missed | resentment-register foreclosure |
| cl-d06 | d06 | relational_anchor_status | +2 | axis cost | moral_framework −1 |
| cl-d07a | d07 | position-prot-rise | +2 | opportunity-missed | arrangement named; exit visible |
| cl-world-d07 | d07 | political_register-world | +2 | journey-required | cl02 |
| cl-antag-d03 | d03 | social_tether-antag | +4 | journey-required | cl02 |
| cl-d08 | d08 | relational_anchor_status | +2 | journey-required | cl03b |
| cl-d08b | d08 | social_tether-prot-rise | +1 | journey-required | cl-d08 |
| cl04 | d10 | relational_anchor_status | +3 | opportunity-missed | extraction window foreclosed |
| cl-antag-d10 | d10 | social_tether-antag | +4 | journey-required | cl04 |
| cl05 | d11/d12 | capability | +2 | axis cost | moral_framework −1 |
| cl-d11 | d11 | relational_anchor_status | +1 | opportunity-missed | [cost-bearer] use-vector intercepted |
| cl06 | d09/d13 | political_register-prot | +5 | opportunity-missed | contempt with no exit |
| cl07a | d14 | moral_legibility_to_self | +4 | axis cost | social_tether-prot-collapse −7 |
| cl07b | d14 | position-world | +2 | axis cost | position-prot-collapse −6 |
| cl07c | d14 | political_register-world | +2 | opportunity-missed | relational_anchor_status at rank 9 [HIGH=WORST] |

---

## LEDGER SUM RECONCILIATION

Tolerance: ±1 rank per schema convention.

| axis | declared Δ | ledger entries | ledger sum | verdict |
|---|---|---|---|---|
| capability | +6 | cl01a(+1) + cl03a(+3) + cl05(+2) | +6 | EXACT |
| moral_framework | +6 cost (2→8) | cl02(−3) + cl03a(−2) + cl-d06(−1) + cl05(−1) | −7 | within ±1 |
| position-prot-rise | +6 | cl02(+4) + cl-d07a(+2) | +6 | EXACT |
| position-prot-collapse | −6 | cl07b cost(−6) | −6 | EXACT |
| relational_anchor_status | +8 | cl-d06(+2) + cl-d08(+2) + cl04(+3) + cl-d11(+1) | +8 | EXACT |
| moral_legibility_to_self | +4 | cl07a(+4) | +4 | EXACT |
| political_register-prot | +8 | cl-d05(+3) + cl06(+5) | +8 | EXACT |
| social_tether-prot-rise | +7 | cl01b(+2) + cl03b(+4) + cl-d08b(+1) | +7 | EXACT |
| social_tether-prot-collapse | −7 | cl07a cost(−7) | −7 | EXACT |
| social_tether-antag | +8 | cl-antag-d03(+4) + cl-antag-d10(+4) | +8 | EXACT |
| position-world | +4 | cl-world-d04(+2) + cl07b(+2) | +4 | EXACT |
| political_register-world | +4 | cl-world-d07(+2) + cl07c(+2) | +4 | EXACT |

**moral_framework reconciliation note:** declared arc is rank 2→8 = +6 rank movement (framework deterioration). Ledger prices seven units of cost (−7 total). The extra unit comes from cl-d06 (moral_framework −1 at d06), which is trajectory-anchored: trajectory d06 text states "she begins choosing which trades to rationalize by asking whether they keep the network intact" — this is a moral_framework fracture beat. The −7 ledger sum against a +6 declared arc is within the ±1 tolerance. No revision required; rationale documented here.

---

## AUTHORING NOTES — CHANGES FROM v1 TO v2

### Hard findings resolved

**fault-001 SCHEMA-SLUG-COLLISION — RESOLVED**
Three colliding slug pairs eliminated by perspective suffixing and rise/collapse splitting:
- `position` (protagonist) → `position-prot-rise` + `position-prot-collapse`
- `position` (world) → `position-world`
- `social_tether` (protagonist) → `social_tether-prot-rise` + `social_tether-prot-collapse`
- `social_tether` (antagonist) → `social_tether-antag`
- `political_register_toward_elite` (protagonist) → `political_register-prot`
- `political_register_toward_elite` (world) → `political_register-world`
All cost_ledger gain/cost fields and all antagonist_pressure axis fields updated to new slugs throughout. No dangling references remain.

**CURVE-SHAPE FAIL (dramatist) + flag-001 + flag-002 — RESOLVED**
The net-zero start_rank=end_rank=1 encoding for position and social_tether protagonist axes is eliminated. Each is now two axis entries with start_rank ≠ end_rank:
- `position-prot-rise` (1→7): rise arc; independently allocatable at chapter level for d03–d10 chapters
- `position-prot-collapse` (7→1): collapse arc; independently allocatable at chapter level for d10–d14 chapters
- `social_tether-prot-rise` (1→8): rise arc
- `social_tether-prot-collapse` (8→1): collapse arc
Downstream /and-substance book Phase 3 now reads four distinct in-motion axes with non-zero declared deltas where v1 had two net-zero axes that would have been classified as held-flat. The rise-phase chapter contract allocation problem is eliminated.

**fault-002 SCHEMA-GAIN-MULTI-AXIS — RESOLVED**
- v1 cl01 (`capability +2, social_tether +2`) → cl01a (`capability +1`) + cl01b (`social_tether-prot-rise +2`). Each entry carries singular gain, valid cost form.
- v1 cl03 (`capability +3, social_tether +4`) → cl03a (`capability +3`) + cl03b (`social_tether-prot-rise +4`). Each entry carries singular gain, valid cost form.

**fault-003 SCHEMA-COST-MALFORMED — RESOLVED**
v1 cl07 (three axes in cost field; relational_anchor_status +4 with wrong sign) split into three entries, each with singular gain and singular cost:
- cl07a: gain `moral_legibility_to_self +4` / cost `social_tether-prot-collapse -7` — recognition arrives as tether severs
- cl07b: gain `position-world +2` / cost `position-prot-collapse -6` — world consolidation completes as Taylor's removal makes her position irrelevant; the two movements are a single event
- cl07c: gain `political_register-world +2` / cost `opportunity-missed: relational_anchor_status at rank 9` — the wrong-sign cost entry eliminated; relational_anchor_status reaching its damaging end expressed as opportunity-missed with explicit [HIGH=WORST] annotation per schema cost_note pattern

**fault-004 COST-LEDGER-DELTA-MISMATCH — RESOLVED**
Four axes reconciled:

*capability (+7 → +6):* cl01a trimmed from +2 to +1. Ledger: cl01a(+1) + cl03a(+3) + cl05(+2) = +6. Exact match.

*moral_framework (−8 → −6 to −7):* cl03a cost trimmed from −3 to −2; cl05 cost trimmed from −2 to −1. cl-d06 adds −1 at d06 (trajectory-anchored: d06 is the "begins choosing which trades to rationalize" beat). Net −7, within ±1 of declared +6. Rationale documented in reconciliation table.

*political_register-prot (+5 → +8):* New entry cl-d05 (+3) at d05. Trajectory d05 explicitly names the resentment-color onset from court observation — this is not invented substance. Ledger: cl-d05(+3) + cl06(+5) = +8. Exact match.

*relational_anchor_status (+3 → +8):* Three new entries distributing the accumulation across trajectory-anchored deltas: cl-d06 (+2 at d06), cl-d08 (+2 at d08), cl-d11 (+1 at d11). Plus existing cl04 (+3 at d10). All trajectory-anchored; no new substance introduced. Ledger: +2 + +2 + +3 + +1 = +8. Exact match.

**chunk_targets.book.delta_per_signature_axis 3-4 → 4-8 (dramatist) — RESOLVED**
Band raised from 3-4 to 4-8, matching the series band and the actual declared axis Δ requirements (moral_framework +6, capability +6, relational_anchor_status +8, political_register-prot +8). Sub-note added explicitly: rise-then-collapse axes tracked as gross motion at chapter level; -rise and -collapse are independent Δ tracks; net-zero series-aggregate does not reduce chapter-level allocation.

**SUBSTANCE-FLAT-antagonist_pressure / Dance-ignition (dark-fantasy-reader) — RESOLVED**
The single vague 'invisible and constant' entry replaced with two entries that name specific on-page eruption points:
1. `relational_anchor_status` pressure entry: names d10 (courier detained because Taylor's route-map reached Otto's apparatus) and d12 (war-pressure forces full-coverage push) as explicit on-page eruption points. Cost-curve language changed from "invisible and constant" to "punctuated; on-page eruptions at d10 and d12; catastrophic at d14." Both beats exist in the trajectory — they are surfaced, not invented.
2. `political_register-prot` sub-pressure entry: faction-violence as the on-page mechanism that makes the contempt accumulation felt (courier detentions, surveillance counter-moves, smallfolk in factional logistics at d07/d10/d12 feeding the insect-network). This names the sub-pressure the dark-fantasy-reader required: specific tactical complications before d14 that Taylor cannot neutralize by accounting.

### Soft findings resolved

**cl07 sign convention** — covered by fault-003 resolution above. relational_anchor_status +4 in a cost field eliminated; cl07c uses opportunity-missed with explicit [HIGH=WORST] annotation.

**moral_legibility_to_self end_rank=8 LOCKED annotation** — added to notes field: "end 8 LOCKED — recognition at full force but too-late; 9 is narratively unavailable (too-late diminishes usability; recognition-without-refusal requires the ledger to complete, not to overwhelm)"

**bone_count ceiling raised 270-500 → 270-700** — auditor flag-003 addressed. Headroom added for chapter sums without immediately busting the book ceiling on any single scene expansion.

**cl03b cheap-gain pre-flag** — added to cl03b cost field: downstream note naming the SUBSTANCE-SUSPECT risk and the chapter-contract mitigation required at /and-substance book Phase 0.

### What was NOT changed

- Emotional/thematic axis shape: moral_framework collapse, contempt arc, relational_anchor_status accumulation, moral_legibility_to_self arc — unanimous-accept across all three audience personas; not disturbed.
- Any trajectory delta content — no trajectory revisions authored.
- LOCKED annotations on end-state ranks — all preserved; moral_legibility_to_self LOCKED annotation added per soft finding.
- actor_baselines — remains empty; correct at pre-cast stage; HARD-ABORT annotation preserved.
- Series chunk, structure, laws, lore, behaviors — outside revision scope.
- Phase 4b pulp-enthusiast ACCEPT verdict and watch-items — carried forward unchanged; revision does not invalidate taste-judge acceptance.
```
